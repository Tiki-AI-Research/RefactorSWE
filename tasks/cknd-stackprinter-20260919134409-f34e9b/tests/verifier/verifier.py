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
from pathlib import Path
from typing import Any


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


try:
    from hardgate import COLLECTOR_CODE
except ImportError:
    COLLECTOR_CODE = r"""
import sys
import json
import pytest

class CTRFPlugin:
    def __init__(self):
        self.records = {}

    def pytest_runtest_logreport(self, report):
        node = report.nodeid.replace("\\", "/")
        if node.startswith("./"):
            node = node[2:]
        if report.when == "call":
            msg = str(report.longrepr) if report.failed else ""
            self.records[node] = {
                "status": report.outcome,
                "duration": int(report.duration * 1000),
                "message": msg,
                "trace": msg,
            }
        elif report.when == "setup" and report.outcome != "passed":
            msg = str(report.longrepr)
            self.records[node] = {
                "status": report.outcome,
                "duration": int(report.duration * 1000),
                "message": msg,
                "trace": msg,
            }
        elif report.when == "teardown" and report.failed:
            if node in self.records and self.records[node]["status"] == "passed":
                msg = str(report.longrepr)
                self.records[node]["status"] = "failed"
                self.records[node]["message"] = msg
                self.records[node]["trace"] = msg

collector = CTRFPlugin()
output_file = sys.argv.pop()
pytest_args = sys.argv[1:]
pytest.main(pytest_args, plugins=[collector])
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(collector.records, f)
sys.exit(0)
"""


def run_nodes_batch(repo: Path, nodes: list[str]) -> dict[str, dict[str, Any]]:
    if not nodes:
        return {}

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tf:
        out_json = tf.name

    env = os.environ.copy()
    repo_str = str(repo.resolve())
    tests_str = str((repo / "tests").resolve())
    env["PYTHONPATH"] = f"{repo_str}{os.pathsep}{tests_str}{os.pathsep}{env.get('PYTHONPATH', '')}"
    env["PY_STACKPRINTER_DEBUG"] = "1"

    cmd = [
        sys.executable,
        "-c",
        COLLECTOR_CODE,
        *nodes,
        out_json,
    ]

    try:
        proc = subprocess.run(
            cmd,
            cwd=str(repo),
            env=env,
            capture_output=True,
            text=True,
            timeout=1800,
        )
        if proc.stdout:
            sys.stdout.write(proc.stdout)
            sys.stdout.flush()
        if proc.stderr:
            sys.stderr.write(proc.stderr)
            sys.stderr.flush()
        if Path(out_json).exists() and Path(out_json).stat().st_size > 0:
            with open(out_json, "r", encoding="utf-8") as f:
                return json.load(f)
        return {node: {"status": "failed", "duration": 0, "message": "Collector produced empty report"} for node in nodes}
    except subprocess.TimeoutExpired:
        return {node: {"status": "failed", "duration": 1800 * 1000, "message": "Execution timed out"} for node in nodes}
    except Exception as exc:
        return {node: {"status": "failed", "duration": 0, "message": f"Execution failed: {exc}"} for node in nodes}
    finally:
        try:
            os.remove(out_json)
        except OSError:
            pass


def execute_test_nodes(repo: Path, all_nodes: list[str]) -> dict[str, dict[str, Any]]:
    # Run all nodes in one pass
    results = run_nodes_batch(repo, all_nodes)

    # If any node is missing from results, run missing nodes individually as fallback
    missing = [node for node in all_nodes if node not in results]
    for node in missing:
        single_result = run_nodes_batch(repo, [node])
        if node in single_result:
            results[node] = single_result[node]
        else:
            results[node] = {
                "status": "failed",
                "duration": 0,
                "message": f"Test node {node} was not collected or executed.",
            }

    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--ctrf-output", type=Path, required=True)
    parser.add_argument("--hard-gate-output", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args()

    config = read_json(args.config)
    task_id = str(config.get("task_id", "cknd-stackprinter-20260919134409-f34e9b"))
    f2p_nodes = [str(n) for n in config.get("f2p", [])]
    p2p_nodes = [str(n) for n in config.get("p2p", [])]
    all_nodes = f2p_nodes + p2p_nodes

    start_time = time.time()

    # Step 1: Check candidate patch application failure
    if bool(args.apply_failed):
        hard_gate_result = {
            "passed": False,
            "apply_failed": True,
            "compile_paths": config.get("hard_gate", {}).get("compile_paths", []),
            "failed_nodes": ["build::candidate_patch_apply"],
            "cheat_penalty": config.get("hard_gate", {}).get("cheat_penalty", -1.0),
        }
        write_json(args.hard_gate_output, hard_gate_result)

        ctrf_tests = []
        for node in all_nodes:
            group = "F2P" if node in f2p_nodes else "P2P"
            ctrf_tests.append({
                "name": node.split("::")[-1],
                "status": "failed",
                "duration": 0,
                "testId": node,
                "message": "candidate patch failed to apply",
                "extra": {
                    "deepswe": {
                        "group": group,
                        "required": True,
                    }
                },
            })
        stop_time = time.time()
        ctrf_data = {
            "reportFormat": "CTRF",
            "specVersion": "0.0.0",
            "results": {
                "tool": {"name": "pytest"},
                "summary": {
                    "tests": len(ctrf_tests),
                    "passed": 0,
                    "failed": len(ctrf_tests),
                    "skipped": 0,
                    "pending": 0,
                    "other": 0,
                    "start": int(start_time * 1000),
                    "stop": int(stop_time * 1000),
                },
                "tests": ctrf_tests,
                "extra": {
                    "deepswe": {
                        "taskId": task_id,
                        "baseCommit": str(config.get("base_commit", "")),
                    }
                },
            },
        }
        write_json(args.ctrf_output, ctrf_data)
        return 0

    # Step 2: Execute hardgate check (safe from timeouts and uncaught exceptions)
    hardgate_script = Path(__file__).parent / "hardgate.py"
    if hardgate_script.exists():
        try:
            res = subprocess.run([
                sys.executable,
                str(hardgate_script),
                "--config", str(args.config),
                "--repo", str(args.repo),
                "--output", str(args.hard_gate_output),
                "--apply-failed", str(args.apply_failed),
            ], capture_output=True, text=True, timeout=1800)
            if res.returncode != 0:
                print(f"[verifier] hardgate.py returned code {res.returncode}: {res.stderr}")
        except subprocess.TimeoutExpired:
            print("[verifier] hardgate.py execution timed out after 1800s")
        except Exception as exc:
            print(f"[verifier] hardgate.py execution error: {exc}")

        if args.hard_gate_output.exists() and args.hard_gate_output.stat().st_size > 0:
            hard_gate_data = read_json(args.hard_gate_output)
        else:
            hard_gate_data = {
                "passed": False,
                "apply_failed": bool(args.apply_failed),
                "compile_paths": config.get("hard_gate", {}).get("compile_paths", []),
                "failed_nodes": ["hardgate::execution_failed"],
                "cheat_penalty": 0.0,
            }
            write_json(args.hard_gate_output, hard_gate_data)
    else:
        hard_gate_data = {
            "passed": True,
            "apply_failed": False,
            "compile_paths": config.get("hard_gate", {}).get("compile_paths", []),
            "failed_nodes": [],
            "cheat_penalty": 0.0,
        }

    # Step 3: Run test nodes (avoid duplicate P2P execution)
    p2p_outcomes = hard_gate_data.get("p2p_outcomes", {})
    missing_p2p = [node for node in p2p_nodes if node not in p2p_outcomes]
    nodes_to_run = f2p_nodes + missing_p2p

    if nodes_to_run:
        fresh_outcomes = execute_test_nodes(args.repo, nodes_to_run)
    else:
        fresh_outcomes = {}

    test_outcomes = {**p2p_outcomes, **fresh_outcomes}

    # Step 4: Check P2P outcomes and update hard gate
    failed_p2p = [
        node for node in p2p_nodes
        if test_outcomes.get(node, {}).get("status") != "passed"
    ]
    if failed_p2p:
        hard_gate_data["passed"] = False
        existing_failed = hard_gate_data.get("failed_nodes", [])
        hard_gate_data["failed_nodes"] = sorted(list(set(existing_failed + failed_p2p)))

    write_json(args.hard_gate_output, hard_gate_data)

    # Step 5: Assemble CTRF report
    ctrf_tests = []
    for node in all_nodes:
        group = "F2P" if node in f2p_nodes else "P2P"
        rec = test_outcomes.get(node, {"status": "failed", "duration": 0, "message": "missing result"})
        status = rec.get("status", "failed")
        # Ensure status is recognized CTRF status
        if status not in ("passed", "failed", "skipped"):
            status = "failed"
        item: dict[str, Any] = {
            "name": node.split("::")[-1],
            "status": status,
            "duration": rec.get("duration", 0),
            "testId": node,
            "extra": {
                "deepswe": {
                    "group": group,
                    "required": True,
                }
            },
        }
        if rec.get("message"):
            item["message"] = rec["message"]
            item["trace"] = rec.get("trace", rec["message"])
        ctrf_tests.append(item)

    stop_time = time.time()
    ctrf_data = {
        "reportFormat": "CTRF",
        "specVersion": "0.0.0",
        "results": {
            "tool": {"name": "pytest"},
            "summary": {
                "tests": len(ctrf_tests),
                "passed": sum(1 for t in ctrf_tests if t["status"] == "passed"),
                "failed": sum(1 for t in ctrf_tests if t["status"] == "failed"),
                "skipped": sum(1 for t in ctrf_tests if t["status"] == "skipped"),
                "pending": 0,
                "other": 0,
                "start": int(start_time * 1000),
                "stop": int(stop_time * 1000),
            },
            "tests": ctrf_tests,
            "extra": {
                "deepswe": {
                    "taskId": task_id,
                    "baseCommit": str(config.get("base_commit", "")),
                }
            },
        },
    }
    write_json(args.ctrf_output, ctrf_data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
