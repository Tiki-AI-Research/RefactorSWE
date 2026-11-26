#!/usr/bin/env python3
"""Task-specific F2P/P2P verifier entrypoint."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


EXPECTED_CONFIG_SHA256 = "be8ffbc33b0032664e1ea114ad0fed51e15accf44f1ba92302d686d7767e96d2"


class NodeCollector:
    def __init__(self) -> None:
        self.results: dict[str, dict[str, Any]] = {}

    def pytest_runtest_logreport(self, report: Any) -> None:
        if report.when == "call" or (report.when == "setup" and report.failed):
            nodeid = str(report.nodeid)
            if nodeid in self.results and self.results[nodeid]["status"] == "passed":
                return

            if report.passed:
                status = "passed"
                msg = ""
            elif report.skipped:
                # Required nodes must run. Count a skipped required node as failed.
                status = "failed"
                msg = f"skipped: {getattr(report, 'longreprtext', '')}"
            else:
                status = "failed"
                msg = str(getattr(report, "longreprtext", ""))

            duration_ms = max(0, int(report.duration * 1000))
            self.results[nodeid] = {
                "status": status,
                "duration": duration_ms,
                "message": msg,
            }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--ctrf-output", type=Path, required=True)
    parser.add_argument("--hard-gate-output", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args()

    config_bytes = args.config.read_bytes()
    config = json.loads(config_bytes)
    config_matches = hashlib.sha256(config_bytes).hexdigest() == EXPECTED_CONFIG_SHA256
    task_id = config["task_id"]
    base_commit = config["base_commit"]
    f2p_nodes = config.get("f2p", [])
    p2p_nodes = config.get("p2p", [])

    # 1. Run the hard gate checks
    hardgate_script = Path(__file__).parent / "hardgate.py"
    hg_proc = subprocess.run([
        sys.executable,
        "-B",
        str(hardgate_script),
        "--config", str(args.config),
        "--repo", str(args.repo),
        "--output", str(args.hard_gate_output),
        "--apply-failed", str(args.apply_failed),
    ], capture_output=True, text=True)

    if not args.hard_gate_output.exists():
        args.hard_gate_output.parent.mkdir(parents=True, exist_ok=True)
        args.hard_gate_output.write_text(json.dumps({
            "passed": False,
            "apply_failed": bool(args.apply_failed),
            "compile_paths": [],
            "failed_nodes": ["hardgate_exec_error"],
            "cheat_penalty": -1.0,
        }) + "\n", encoding="utf-8")

    hard_gate = json.loads(args.hard_gate_output.read_text(encoding="utf-8"))
    if not config_matches:
        hard_gate["passed"] = False
        hard_gate.setdefault("failed_nodes", []).append("verifier_config_sha256_mismatch")
        args.hard_gate_output.write_text(json.dumps(hard_gate, indent=2) + "\n")

    # 2. Run exactly the protected selection, only after integrity gates pass.
    start_time_ms = int(time.time() * 1000)
    collector = NodeCollector()

    test_file = args.repo / "tests" / "test_verifier_suite.py"
    if test_file.exists() and not args.apply_failed and hard_gate.get("passed") is True:
        old_cwd = os.getcwd()
        old_sys_path = list(sys.path)
        try:
            os.chdir(str(args.repo))
            if str(args.repo) not in sys.path:
                sys.path.insert(0, str(args.repo))
            import pytest
            pytest.main([
                "-q", "-p", "no:cacheprovider",
                "--basetemp", str(args.ctrf_output.parent / "pytest-temp"),
                *f2p_nodes, *p2p_nodes,
            ], plugins=[collector])
        finally:
            os.chdir(old_cwd)
            sys.path = old_sys_path
    stop_time_ms = max(start_time_ms, int(time.time() * 1000))

    # 3. Build the CTRF test case list
    ctrf_tests: list[dict[str, Any]] = []
    
    # Collect the expected nodes
    expected_groups: dict[str, str] = {}
    for node in f2p_nodes:
        expected_groups[str(node)] = "f2p"
    for node in p2p_nodes:
        expected_groups[str(node)] = "p2p"

    for node_id, group in expected_groups.items():
        if node_id in collector.results:
            item = collector.results[node_id]
            status = item["status"]
            duration = item["duration"]
            msg = item["message"]
        else:
            status = "failed"
            duration = 0
            msg = ("test node was not executed or not collected" if hard_gate.get("passed") is True
                   else "hard gate failed before node execution")

        short_name = node_id.split("::")[-1]
        ctrf_tests.append({
            "name": short_name,
            "status": status,
            "duration": duration,
            "testId": node_id,
            "message": msg,
            "extra": {
                "deepswe": {
                    "group": group,
                    "required": True,
                }
            }
        })

    passed_count = sum(t["status"] == "passed" for t in ctrf_tests)
    failed_count = len(ctrf_tests) - passed_count

    ctrf_report = {
        "reportFormat": "CTRF",
        "specVersion": "0.0.1",
        "results": {
            "tool": {
                "name": "pytest"
            },
            "summary": {
                "tests": len(ctrf_tests),
                "passed": passed_count,
                "failed": failed_count,
                "skipped": 0,
                "pending": 0,
                "other": 0,
                "start": start_time_ms,
                "stop": stop_time_ms,
            },
            "tests": ctrf_tests,
            "extra": {
                "deepswe": {
                    "taskId": task_id,
                    "baseCommit": base_commit,
                }
            }
        }
    }

    args.ctrf_output.parent.mkdir(parents=True, exist_ok=True)
    args.ctrf_output.write_text(json.dumps(ctrf_report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
