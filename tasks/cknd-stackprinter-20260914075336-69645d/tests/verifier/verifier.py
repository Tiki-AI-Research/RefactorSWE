#!/usr/bin/env python3
"""Task-specific Verifier entrypoint.

Runs deterministic scope check, injects test patch only if scope check passes,
runs the deterministic Hard Gate (compile, integrity, anti-cheat and P2P nodes),
writes its report, executes the atomic F2P nodes and emits a strict CTRF report
so the grader sees every required node exactly once.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import hardgate  # noqa: E402

# Keep the verifier's binding in sync with the integrity hash enforced by
# hardgate.py.  A stale value here rejects every otherwise valid candidate
# before any configured node can run.
EXPECTED_CONFIG_SHA256 = "61260d38e22ba710e495f79b7e557564363af79d7a91bc7324653d1ca1a93498"


def _write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def _entry(node: str, group: str, passed: bool, message: str, duration: int = 0,
           *, infrastructure_error: bool = False) -> dict:
    return {
        "name": node,
        "testId": node,
        "status": "other" if infrastructure_error else ("passed" if passed else "failed"),
        "typedStatus": "INFRA_ERROR" if infrastructure_error else ("PASS" if passed else "FAIL"),
        "duration": max(0, int(duration)),
        "message": "" if passed else message,
        "extra": {"deepswe": {"group": group, "required": True}},
    }


def _fixed_template_hard_gate(raw: dict, *, apply_failed: bool) -> dict:
    """Project the native hard-gate result into the fixed test.sh contract."""
    failed = list(raw.get("failed_nodes") or [])
    passed = bool(raw.get("passed") is True and not apply_failed)
    return {
        **raw,
        "success": passed,
        "passed": passed,
        "compile_passed": all(bool(value) for value in (raw.get("compile_results") or {}).values()),
        "cheating_detected": any(str(item).startswith("cheat:") for item in failed),
        "scope_violation": bool(raw.get("scope_findings")),
        "infrastructure_error": False,
    }


def _write_fixed_outputs(
    *, node_report: Path | None, hard_gate_report: Path | None,
    verifier_report: Path | None, tests: list[dict], hard_gate: dict,
    apply_failed: bool,
) -> None:
    if node_report is not None:
        _write_json(node_report.parent / "nodes.json" if node_report.name == "nodes.json" else node_report,
                    {"schema_version": "deepswe-node-report/v1", "tests": tests})
    if hard_gate_report is not None:
        _write_json(hard_gate_report, hard_gate)
    if verifier_report is not None:
        infrastructure_error = bool(hard_gate.get("infrastructure_error"))
        _write_json(verifier_report, {
            "status": "INFRA_ERROR" if infrastructure_error else ("FAIL" if apply_failed else "PASS"),
            "success": not (apply_failed or infrastructure_error),
            "apply_failed": bool(apply_failed),
            "tests_executed": len(tests),
            "failed_nodes": [row["name"] for row in tests if row["status"] != "passed"],
        })


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--ctrf-output", type=Path)
    parser.add_argument("--hard-gate-output", type=Path)
    parser.add_argument("--node-report", type=Path)
    parser.add_argument("--hard-gate-report", type=Path)
    parser.add_argument("--verifier-report", type=Path)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    parser.add_argument("--test-patch", type=Path, default=Path("/tests/verifier/test.patch"))
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    started = int(time.time() * 1000)

    # Bind the loaded configuration to the task's frozen verifier contract.
    scope_ok, scope_findings = hardgate.check_candidate_scope(config, args.repo)
    config_findings = hardgate._config_sha256_findings(args.config)
    actual_config_sha256 = hashlib.sha256(args.config.read_bytes()).hexdigest()
    if actual_config_sha256 != EXPECTED_CONFIG_SHA256:
        config_findings.append(f"config-sha256-mismatch:{actual_config_sha256}")
    if config_findings:
        scope_ok = False
        scope_findings.extend(config_findings)

    if not scope_ok or bool(args.apply_failed):
        # Candidate failed candidate scope or patch application failed!
        # Do NOT inject test patch to avoid overlay collision / infra errors
        hard_gate = hardgate.evaluate(
            config,
            args.repo,
            bool(args.apply_failed),
            p2p_passed=False,
            p2p_failed_nodes=list(config.get("p2p", [])),
            scope_failed_findings=scope_findings if not scope_ok else None,
        )
        hard_gate = _fixed_template_hard_gate(hard_gate, apply_failed=bool(args.apply_failed))
        # Emit one deterministic record for every configured node.  The fixed
        # grader canonicalizes this report and treats missing nodes as an
        # infrastructure error, so build the list before writing outputs.
        tests = []
        for node in config.get("f2p", []):
            tests.append(_entry(str(node), "f2p", False, "candidate out of scope or apply failed"))
        for node in config.get("p2p", []):
            tests.append(_entry(str(node), "p2p", False, "candidate out of scope or apply failed"))
        _write_fixed_outputs(node_report=args.node_report, hard_gate_report=args.hard_gate_report,
                             verifier_report=args.verifier_report, tests=tests,
                             hard_gate=hard_gate, apply_failed=bool(args.apply_failed))
        if args.hard_gate_output:
            _write_json(args.hard_gate_output, hard_gate)

        stopped = max(started, int(time.time() * 1000))
        ctrf = {
            "reportFormat": "CTRF",
            "specVersion": "0.0.0",
            "results": {
                "tool": {"name": "pytest"},
                "summary": {
                    "tests": len(tests),
                    "passed": 0,
                    "failed": len(tests),
                    "skipped": 0,
                    "pending": 0,
                    "other": 0,
                    "start": started,
                    "stop": stopped,
                    "duration": max(0, stopped - started),
                },
                "tests": tests,
                "extra": {
                    "deepswe": {
                        "taskId": str(config.get("task_id", "")),
                        "baseCommit": str(config.get("base_commit", "")),
                    }
                },
            },
        }
        if args.ctrf_output:
            _write_json(args.ctrf_output, ctrf)
        return 0

    # 2. Scope is valid: now inject hidden tests
    try:
        if not args.test_patch.is_file() or args.test_patch.stat().st_size == 0:
            raise hardgate.InfrastructureError(f"missing or empty trusted test patch: {args.test_patch}")
        inject_res = subprocess.run(
            ["git", "-C", str(args.repo), "apply", "--whitespace=nowarn", str(args.test_patch)],
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
        if inject_res.returncode != 0:
            raise hardgate.InfrastructureError(f"failed to inject trusted test patch: {inject_res.stderr}")
    except (OSError, subprocess.TimeoutExpired, hardgate.InfrastructureError) as exc:
        hard_gate = {
            "success": False, "passed": False, "infrastructure_error": True,
            "cheating_detected": False, "scope_violation": False,
            "error": str(exc),
        }
        tests = [_entry(str(node), group, False, str(exc), infrastructure_error=True)
                 for group in ("f2p", "p2p") for node in config.get(group, [])]
        _write_fixed_outputs(node_report=args.node_report, hard_gate_report=args.hard_gate_report,
                             verifier_report=args.verifier_report, tests=tests,
                             hard_gate=hard_gate, apply_failed=False)
        if args.hard_gate_output:
            _write_json(args.hard_gate_output, hard_gate)
        return 0

    hard_gate = hardgate.evaluate(config, args.repo, bool(args.apply_failed))
    hard_gate = _fixed_template_hard_gate(hard_gate, apply_failed=bool(args.apply_failed))

    tests = []
    for node in config.get("f2p", []):
        node = str(node)
        passed, message = hardgate._run_cheat_node(args.repo, node)
        tests.append(_entry(node, "f2p", passed, message))

    p2p_results = hard_gate.get("p2p_nodes") or {}
    for node in config.get("p2p", []):
        node = str(node)
        result = p2p_results.get(node) or {}
        passed = result.get("passed") is True
        tests.append(_entry(node, "p2p", passed, str(result.get("message", ""))))

    stopped = max(started, int(time.time() * 1000))
    statuses = ("passed", "failed", "skipped", "pending", "other")
    summary = {
        "tests": len(tests),
        **{status: sum(test["status"] == status for test in tests) for status in statuses},
        "start": started,
        "stop": stopped,
        "duration": max(0, stopped - started),
    }
    ctrf = {
        "reportFormat": "CTRF",
        "specVersion": "0.0.0",
        "results": {
            "tool": {"name": "pytest"},
            "summary": summary,
            "tests": tests,
            "extra": {
                "deepswe": {
                    "taskId": str(config.get("task_id", "")),
                    "baseCommit": str(config.get("base_commit", "")),
                }
            },
        },
    }
    if args.ctrf_output:
        _write_json(args.ctrf_output, ctrf)
    _write_fixed_outputs(node_report=args.node_report, hard_gate_report=args.hard_gate_report,
                         verifier_report=args.verifier_report, tests=tests,
                         hard_gate=hard_gate, apply_failed=bool(args.apply_failed))
    if args.hard_gate_output:
        _write_json(args.hard_gate_output, hard_gate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
