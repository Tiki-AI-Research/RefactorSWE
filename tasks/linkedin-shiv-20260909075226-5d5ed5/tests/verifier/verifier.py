#!/usr/bin/env python3
"""Task-specific F2P/P2P verifier entrypoint."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List

from hardgate import check_config_integrity

EXPECTED_CONFIG_SHA256 = "6a321af6a0a58a6ff6a090c30f89f65e389bbcf72516723f86cee9dc4046536a"


def run_node(repo: Path, node_id: str, timeout: float = 120) -> dict[str, Any]:
    """Keep assertion failures separate from runner, report, skip, and timeout faults."""
    def result(status, category=None, reason=None):
        return {"status": status, "error_category": category, "reason": reason}

    with tempfile.TemporaryDirectory(prefix="pytest_node_") as tmpdir:
        junit_xml = Path(tmpdir) / "junit.xml"
        cmd = [
            sys.executable,
            "-m",
            "pytest",
            "-o",
            "addopts=",
            "-q",
            "--tb=short",
            "--import-mode=importlib",
            f"--junitxml={junit_xml}",
            node_id,
        ]
        env = dict(os.environ)
        src_dir = str((repo / "src").resolve())
        env["PYTHONPATH"] = f"{src_dir}:{env.get('PYTHONPATH', '')}"

        try:
            proc = subprocess.run(
                cmd,
                cwd=repo,
                env=env,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired as exc:
            return result("other", "pytest_timeout", str(exc))
        except Exception as exc:
            return result("other", "runner_error", str(exc))

        # If JUnit XML was not created or empty, pytest failed before test execution
        # (e.g. collection error, syntax error, missing test file)
        if not junit_xml.exists() or junit_xml.stat().st_size == 0:
            return result("other", "junit_missing", proc.stdout[-2000:] + proc.stderr[-2000:])

        try:
            tree = ET.parse(junit_xml)
            root = tree.getroot()
        except Exception:
            return result("other", "junit_invalid", proc.stdout[-2000:] + proc.stderr[-2000:])

        testcases = root.findall(".//testcase")
        if not testcases:
            # Missing testcase or collection failure
            return result("other", "testcase_missing", proc.stdout[-2000:] + proc.stderr[-2000:])

        # Unique confirmation of the target node_id in JUnit XML
        # Node ID is formatted as:
        #   path/to/test_file.py::ClassName::test_name
        #   or path/to/test_file.py::test_name
        parts = node_id.split("::")
        file_path = parts[0]
        expected_name = parts[-1]
        file_stem = file_path[:-3] if file_path.endswith(".py") else file_path
        expected_mod = file_stem.replace("/", ".")
        if len(parts) == 2:
            expected_classname = expected_mod
        else:
            expected_classname = f"{expected_mod}." + ".".join(parts[1:-1])

        matching_cases = [
            tc
            for tc in testcases
            if tc.get("name") == expected_name and tc.get("classname") == expected_classname
        ]

        # Fail closed on missing, duplicate, ambiguous mapping, or unexpected testcases
        if len(matching_cases) != 1 or len(testcases) != 1:
            return result("other", "testcase_mapping_invalid", proc.stdout[-2000:] + proc.stderr[-2000:])

        if proc.returncode not in (0, 1):
            return result("other", "pytest_exit_error", str(proc.returncode))

        tc = matching_cases[0]
        if tc.find("error") is not None:
            return result("other", "pytest_error", proc.stdout[-2000:] + proc.stderr[-2000:])
        if tc.find("failure") is not None:
            return result("failed", "assertion_failure", tc.find("failure").text)
        if tc.find("skipped") is not None:
            return result("skipped", "pytest_skipped", "configured test was skipped")

        # If pytest exit code is non-zero, fail closed even if XML looks clean
        if proc.returncode != 0:
            return result("other", "pytest_exit_error", str(proc.returncode))

        return result("passed")


def build_ctrf(
    f2p_nodes: List[str],
    p2p_nodes: List[str],
    node_statuses: Dict[str, dict[str, Any]],
    start_time: int,
    stop_time: int,
    task_id: str,
    base_commit: str,
) -> Dict[str, Any]:
    tests: List[Dict[str, Any]] = []

    for node in f2p_nodes:
        tests.append({
            "testId": node,
            "name": node,
            "status": node_statuses[node]["status"],
            "duration": 0,
            "extra": {
                "deepswe": {
                    "group": "f2p",
                    "required": True,
                    "error_category": node_statuses[node].get("error_category"),
                    "reason": node_statuses[node].get("reason"),
                }
            },
        })

    for node in p2p_nodes:
        tests.append({
            "testId": node,
            "name": node,
            "status": node_statuses[node]["status"],
            "duration": 0,
            "extra": {
                "deepswe": {
                    "group": "p2p",
                    "required": True,
                    "error_category": node_statuses[node].get("error_category"),
                    "reason": node_statuses[node].get("reason"),
                }
            },
        })

    passed_count = sum(t["status"] == "passed" for t in tests)
    failed_count = sum(t["status"] == "failed" for t in tests)
    skipped_count = sum(t["status"] == "skipped" for t in tests)
    pending_count = sum(t["status"] == "pending" for t in tests)
    other_count = sum(t["status"] == "other" for t in tests)

    return {
        "reportFormat": "CTRF",
        "specVersion": "1.0.0",
        "results": {
            "tool": {
                "name": "pytest",
            },
            "extra": {
                "deepswe": {
                    "taskId": task_id,
                    "baseCommit": base_commit,
                }
            },
            "summary": {
                "tests": len(tests),
                "passed": passed_count,
                "failed": failed_count,
                "skipped": skipped_count,
                "pending": pending_count,
                "other": other_count,
                "start": start_time,
                "stop": stop_time,
            },
            "tests": tests,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--node-report", type=Path, required=True)
    parser.add_argument("--hard-gate-report", type=Path, required=True)
    parser.add_argument("--verifier-report", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args()

    integrity_errors = check_config_integrity(args.config, EXPECTED_CONFIG_SHA256)
    if integrity_errors:
        reports = [
            (args.hard_gate_report, {"passed": False, "success": False, "status": "FAIL",
                                    "failed_nodes": integrity_errors}),
            (args.node_report, {"tests": [], "errors": integrity_errors}),
            (args.verifier_report, {"success": False, "status": "FAIL",
                                    "errors": integrity_errors}),
        ]
        for path, report in reports:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        return 0

    start_time = int(time.time())
    config = json.loads(args.config.read_text(encoding="utf-8"))
    f2p_nodes = [str(n) for n in config.get("f2p", [])]
    p2p_nodes = [str(n) for n in config.get("p2p", [])]

    # 1. Execute hardgate.py (without --run-p2p to prevent duplicate execution)
    hardgate_script = Path(__file__).resolve().parent / "hardgate.py"
    hg_cmd = [
        sys.executable,
        str(hardgate_script),
        "--config", str(args.config),
        "--repo", str(args.repo),
        "--output", str(args.hard_gate_report),
        "--apply-failed", str(args.apply_failed),
    ]

    try:
        subprocess.run(hg_cmd, check=True)
    except (subprocess.CalledProcessError, OSError) as exc:
        args.hard_gate_report.parent.mkdir(parents=True, exist_ok=True)
        args.hard_gate_report.write_text(json.dumps({"passed": False, "success": False, "infrastructure_error": True, "failed_nodes": [f"hardgate_runner_error:{exc}"]}) + "\n")

    # Read hardgate result
    hard_gate_passed = False
    if args.hard_gate_report.exists():
        try:
            hg_res = json.loads(args.hard_gate_report.read_text(encoding="utf-8"))
            hard_gate_passed = hg_res.get("passed") is True and not bool(args.apply_failed)
        except Exception:
            hard_gate_passed = False
    else:
        # Failsafe: write failed hardgate report
        args.hard_gate_report.parent.mkdir(parents=True, exist_ok=True)
        args.hard_gate_report.write_text(json.dumps({
            "passed": False,
            "success": False,
            "infrastructure_error": True,
            "apply_failed": bool(args.apply_failed),
            "failed_nodes": ["hardgate_failed_to_produce_output"],
        }) + "\n", encoding="utf-8")

    # 2. Evaluate test nodes
    node_statuses: Dict[str, dict[str, Any]] = {}

    # Run each P2P node
    for node in p2p_nodes:
        node_statuses[node] = run_node(args.repo, node)

    # If Hard Gate failed, do not award F2P reward
    if not hard_gate_passed:
        for node in f2p_nodes:
            node_statuses[node] = {"status": "failed", "reason": "not evaluated: hard gate failed"}
    else:
        # Run each F2P node independently
        for node in f2p_nodes:
            node_statuses[node] = run_node(args.repo, node)

    stop_time = int(time.time())

    # 3. Generate CTRF report
    ctrf_report = build_ctrf(
        f2p_nodes,
        p2p_nodes,
        node_statuses,
        start_time,
        stop_time,
        config["task_id"],
        config["base_commit"],
    )
    tests = ctrf_report["results"]["tests"]
    for node in tests:
        node_result = node_statuses[node["name"]]
        node["typedStatus"] = {
            "passed": "PASS", "failed": "FAIL", "other": "INFRA_ERROR",
            "skipped": "INCONCLUSIVE", "pending": "INCONCLUSIVE",
        }[node["status"]]
        node["message"] = node_result.get("reason") or ""
    args.node_report.parent.mkdir(parents=True, exist_ok=True)
    args.node_report.write_text(
        json.dumps({"tests": tests}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    infrastructure_error = any(node["typedStatus"] in {"INFRA_ERROR", "INCONCLUSIVE"} for node in tests)
    success = hard_gate_passed and all(node["status"] == "passed" for node in tests)
    args.verifier_report.parent.mkdir(parents=True, exist_ok=True)
    args.verifier_report.write_text(json.dumps({
        "success": success,
        "status": "INFRA_ERROR" if infrastructure_error else "PASS" if success else "FAIL",
    }, indent=2) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
