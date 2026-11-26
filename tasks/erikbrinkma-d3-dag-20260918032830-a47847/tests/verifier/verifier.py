#!/usr/bin/env python3
"""Task-specific F2P/P2P verifier entrypoint."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any

from hardgate import (
    BASELINE_TEST_FILES,
    check_anti_cheat,
    check_build,
    check_post_test_integrity,
    evaluate_hard_gate,
    execute_test_suite,
)


def get_bun_version() -> str:
    bun_bin = os.environ.get("BUN_BIN") or shutil.which("bun")
    if bun_bin:
        try:
            proc = subprocess.run([bun_bin, "--version"], capture_output=True, text=True, timeout=5)
            if proc.returncode == 0 and proc.stdout.strip():
                return proc.stdout.strip()
        except Exception:
            pass
    return "1.4.2"


def build_ctrf_report(
    config: dict[str, Any],
    p2p_statuses: dict[str, str],
    f2p_statuses: dict[str, str],
    testcase_details: dict[str, dict[str, Any]],
    hard_gate_passed: bool = True,
    start_time_ms: int | None = None,
    stop_time_ms: int | None = None,
) -> dict[str, Any]:
    """Build a compliant CTRF report according to DeepSWE schema."""
    tests: list[dict[str, Any]] = []

    if start_time_ms is None:
        start_time_ms = int(time.time() * 1000)
    if stop_time_ms is None:
        stop_time_ms = int(time.time() * 1000)
    if stop_time_ms < start_time_ms:
        stop_time_ms = start_time_ms

    def norm_status(s: str, is_f2p: bool = False) -> str:
        if not hard_gate_passed and is_f2p:
            # If hard gate failed, F2P tests cannot be considered passed in final CTRF
            return "failed"
        if s == "passed":
            return "passed"
        if s in ("failed", "missing", "error"):
            return "failed"
        if s == "skipped":
            return "skipped"
        if s == "pending":
            return "pending"
        return "other"

    # 1. F2P nodes
    for node in config.get("f2p", []):
        node_str = str(node)
        status = norm_status(f2p_statuses.get(node_str, "failed"), is_f2p=True)
        details = testcase_details.get(node_str, {})
        duration = float(details.get("time", 0.0)) * 1000.0  # ms
        entry: dict[str, Any] = {
            "name": node_str.split("::")[-1] if "::" in node_str else node_str,
            "status": status,
            "duration": int(duration),
            "testId": node_str,
            "filePath": node_str.split("::")[0] if "::" in node_str else "",
            "extra": {
                "deepswe": {
                    "group": "F2P",
                    "required": True,
                }
            },
        }
        if status == "failed":
            entry["message"] = details.get("failure_message") or (
                "Candidate failed deterministic hard gate"
                if not hard_gate_passed
                else "Test failed or was not executed"
            )
        tests.append(entry)

    # 2. P2P nodes
    for node in config.get("p2p", []):
        node_str = str(node)
        status = norm_status(p2p_statuses.get(node_str, "failed"), is_f2p=False)
        details = testcase_details.get(node_str, {})
        duration = float(details.get("time", 0.0)) * 1000.0  # ms
        entry = {
            "name": node_str.split("::")[-1] if "::" in node_str else node_str,
            "status": status,
            "duration": int(duration),
            "testId": node_str,
            "filePath": node_str.split("::")[0] if "::" in node_str else "",
            "extra": {
                "deepswe": {
                    "group": "P2P",
                    "required": True,
                }
            },
        }
        if status == "failed":
            entry["message"] = details.get("failure_message") or "P2P test failed or was not executed"
        tests.append(entry)

    statuses = ("passed", "failed", "skipped", "pending", "other")
    summary = {
        "tests": len(tests),
        "passed": sum(item["status"] == "passed" for item in tests),
        "failed": sum(item["status"] == "failed" for item in tests),
        "skipped": sum(item["status"] == "skipped" for item in tests),
        "pending": sum(item["status"] == "pending" for item in tests),
        "other": sum(item["status"] == "other" for item in tests),
        "start": start_time_ms,
        "stop": stop_time_ms,
    }

    return {
        "reportFormat": "CTRF",
        "specVersion": "0.1.0",
        "extra": {
            "reportFormat": "CTRF",
            "reportVersion": "0.1",
        },
        "results": {
            "tool": {
                "name": "bun-test",
                "version": get_bun_version(),
            },
            "summary": summary,
            "tests": tests,
            "extra": {
                "reportFormat": "CTRF",
                "reportVersion": "0.1",
                "deepswe": {
                    "taskId": str(config.get("task_id", "")),
                    "baseCommit": str(config.get("base_commit", "")),
                },
            },
        },
    }


def main() -> int:
    start_time_ms = int(time.time() * 1000)
    parser = argparse.ArgumentParser(description="Task verifier entrypoint.")
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--ctrf-output", type=Path, required=True)
    parser.add_argument("--hard-gate-output", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))

    # Ensure source-manifest.json is available in standard workspace location if provided in tests
    ws_manifest = Path("/workspace/source-manifest.json")
    tests_manifest = Path("/tests/source-manifest.json")
    if not ws_manifest.exists() and tests_manifest.exists():
        try:
            shutil.copyfile(tests_manifest, ws_manifest)
        except Exception:
            pass

    # 1. Anti-cheat and build gate validation before running tests
    anti_cheat_passed, cheat_failed_nodes, cheat_warnings = check_anti_cheat(args.repo, config)
    build_passed, build_failed_nodes = check_build(args.repo, config)
    if "build_bun_not_found" in build_failed_nodes:
        print("INFRA_ERROR: build_bun_not_found - bun binary not found in environment", flush=True)
        return 2

    # 2. Run full test suite exactly ONCE (or skip if anti-cheat/build failed)
    if not anti_cheat_passed or not build_passed or bool(args.apply_failed):
        # Empty execution if gate failed early
        parsed_execution = (1, {}, {}, set(), ["early_gate_failed"])
    else:
        parsed_execution = execute_test_suite(args.repo)

    exit_code, all_statuses, all_details, duplicate_ids, runner_errors = parsed_execution
    if "build_bun_not_found" in runner_errors:
        print("INFRA_ERROR: build_bun_not_found - bun binary not found during test execution", flush=True)
        return 2

    f2p_nodes = [str(n) for n in config.get("f2p", [])]
    p2p_nodes = [str(n) for n in config.get("p2p", [])]

    # Test inventory completeness validation on fixed evaluation suite (G13)
    def is_fixed_test_node(node_id: str) -> bool:
        file_path = node_id.split("::")[0] if "::" in node_id else node_id
        return file_path in BASELINE_TEST_FILES or file_path.startswith("eval_tests/")

    expected_fixed_ids = set(p2p_nodes) | set(f2p_nodes) | set(config.get("advisory_ids", []))
    actual_fixed_ids = {nid for nid in all_statuses.keys() if is_fixed_test_node(nid)}
    unknown_fixed_nodes = actual_fixed_ids - expected_fixed_ids
    missing_fixed_nodes = expected_fixed_ids - set(all_statuses.keys())

    if not bool(args.apply_failed) and anti_cheat_passed and build_passed:
        if unknown_fixed_nodes:
            print(f"ERROR: Found {len(unknown_fixed_nodes)} unmapped fixed test nodes: {sorted(unknown_fixed_nodes)}", flush=True)
            for u in sorted(unknown_fixed_nodes):
                runner_errors.append(f"unmapped_node:{u}")
        if missing_fixed_nodes:
            print(f"ERROR: Found {len(missing_fixed_nodes)} missing fixed test nodes: {sorted(missing_fixed_nodes)}", flush=True)
            for m in sorted(missing_fixed_nodes):
                runner_errors.append(f"missing_node:{m}")
        if unknown_fixed_nodes or missing_fixed_nodes:
            parsed_execution = (exit_code, all_statuses, all_details, duplicate_ids, runner_errors)

    # 3. Post-execution integrity re-check to detect runtime mutations
    if anti_cheat_passed and build_passed and not bool(args.apply_failed):
        post_cheat_passed, post_cheat_failed_nodes, post_cheat_warnings = check_post_test_integrity(args.repo, config)
    else:
        post_cheat_passed, post_cheat_failed_nodes, post_cheat_warnings = True, [], []

    # 4. Evaluate hard gate using the same parsed execution and precomputed checks
    hard_gate_result = evaluate_hard_gate(
        config=config,
        repo=args.repo,
        apply_failed=args.apply_failed,
        parsed_execution=parsed_execution,
        build_result=(build_passed, build_failed_nodes),
        anti_cheat_result=(anti_cheat_passed, cheat_failed_nodes, cheat_warnings),
        post_anti_cheat_result=(post_cheat_passed, post_cheat_failed_nodes, post_cheat_warnings),
    )

    args.hard_gate_output.parent.mkdir(parents=True, exist_ok=True)
    args.hard_gate_output.write_text(json.dumps(hard_gate_result, ensure_ascii=False, indent=2) + "\n")

    # 5. Extract F2P and P2P statuses from the same run

    f2p_statuses: dict[str, str] = {}
    for n in f2p_nodes:
        f2p_statuses[n] = all_statuses.get(n, "failed")

    p2p_statuses: dict[str, str] = {}
    hg_p2p = hard_gate_result.get("p2p_statuses", {})
    for n in p2p_nodes:
        p2p_statuses[n] = hg_p2p.get(n) or all_statuses.get(n, "failed")

    stop_time_ms = int(time.time() * 1000)

    # 4. Generate CTRF report
    ctrf_report = build_ctrf_report(
        config=config,
        p2p_statuses=p2p_statuses,
        f2p_statuses=f2p_statuses,
        testcase_details=all_details,
        hard_gate_passed=hard_gate_result.get("passed", False),
        start_time_ms=start_time_ms,
        stop_time_ms=stop_time_ms,
    )

    args.ctrf_output.parent.mkdir(parents=True, exist_ok=True)
    args.ctrf_output.write_text(json.dumps(ctrf_report, ensure_ascii=False, indent=2) + "\n")

    # 5. Generate reports/nodes.json
    node_report_path = (config.get("diagnostics") or {}).get("node_report")
    if node_report_path:
        nr_file = Path(node_report_path)
        nr_file.parent.mkdir(parents=True, exist_ok=True)
        nodes_list = [
            {"testId": n, "group": "F2P", "status": f2p_statuses.get(n, "failed")}
            for n in f2p_nodes
        ] + [
            {"testId": n, "group": "P2P", "status": p2p_statuses.get(n, "failed")}
            for n in p2p_nodes
        ]
        nr_data = {
            "task_id": str(config.get("task_id", "")),
            "nodes": nodes_list,
            "summary": {
                "total": len(nodes_list),
                "f2p_total": len(f2p_nodes),
                "f2p_passed": sum(f2p_statuses.get(n) == "passed" for n in f2p_nodes),
                "p2p_total": len(p2p_nodes),
                "p2p_passed": sum(p2p_statuses.get(n) == "passed" for n in p2p_nodes),
            },
        }
        nr_file.write_text(json.dumps(nr_data, ensure_ascii=False, indent=2) + "\n")

    # 6. Generate verifier-result.json
    verifier_result_path = (config.get("diagnostics") or {}).get("verifier")
    if verifier_result_path:
        vr_file = Path(verifier_result_path)
        vr_file.parent.mkdir(parents=True, exist_ok=True)
        f2p_passed_cnt = sum(f2p_statuses.get(n) == "passed" for n in f2p_nodes)
        p2p_passed_cnt = sum(p2p_statuses.get(n) == "passed" for n in p2p_nodes)
        hg_passed = hard_gate_result.get("passed", False)
        vr_data = {
            "task_id": str(config.get("task_id", "")),
            "hard_gate_passed": hg_passed,
            "passed": bool(hg_passed and f2p_passed_cnt == len(f2p_nodes) and p2p_passed_cnt == len(p2p_nodes)),
            "f2p_total": len(f2p_nodes),
            "f2p_passed": f2p_passed_cnt,
            "f2p_pass_ratio": f2p_passed_cnt / len(f2p_nodes) if f2p_nodes else 0.0,
            "p2p_total": len(p2p_nodes),
            "p2p_passed": p2p_passed_cnt,
            "p2p_pass_ratio": p2p_passed_cnt / len(p2p_nodes) if p2p_nodes else 1.0,
            "failed_nodes": sorted(
                [n for n in f2p_nodes if f2p_statuses.get(n) != "passed"] +
                [n for n in p2p_nodes if p2p_statuses.get(n) != "passed"]
            ),
        }
        vr_file.write_text(json.dumps(vr_data, ensure_ascii=False, indent=2) + "\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
