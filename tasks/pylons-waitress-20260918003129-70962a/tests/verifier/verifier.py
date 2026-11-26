#!/usr/bin/env python3
"""Unified verifier entrypoint: orchestrates Hard Gate, F2P tests, and CTRF generation.

Flow:
1. Runs Hard Gate (Build Gate, Anti-Cheat Gate, and atomic P2P Gate).
2. If Hard Gate fails -> short-circuits immediately: skips F2P execution, writes CTRF with failure details, exits 0.
3. If Hard Gate passes -> executes F2P tests, aggregates full CTRF report (P2P + F2P), exits 0.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any, Dict, List, Optional

# Ensure verifier directory is on sys.path to import hardgate
VERIFIER_DIR = Path(__file__).resolve().parent
if str(VERIFIER_DIR) not in sys.path:
    sys.path.insert(0, str(VERIFIER_DIR))

import hardgate


def find_refactor_trajectory_record(repo_path: Path) -> Optional[Path]:
    """Locate an optional refactoring trajectory or record file across the repository.
    Since instruction does not specify an exact output path, search root and
    subdirectories with fuzzy matching across common patterns.
    """
    if not repo_path.is_dir():
        return None

    candidates = [
        "refactoring.md",
        "refactor.md",
        "refactor_log.md",
        "refactor_log.json",
        "refactoring_record.md",
        "refactoring_record.txt",
        "trajectory.json",
        "trajectory.md",
        "changelog.md",
        "refactor_manifest.json",
    ]
    for name in candidates:
        target = repo_path / name
        if target.is_file():
            return target

    ignore_dirs = {".git", "__pycache__", ".pytest_cache", "venv", ".venv", "node_modules"}
    for root, dirs, files in os.walk(str(repo_path)):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for f in files:
            f_lower = f.lower()
            if any(k in f_lower for k in ["trajectory", "refactor", "reconstruct", "record", "manifest"]):
                if f_lower.endswith((".md", ".json", ".txt", ".yaml", ".yml")):
                    return Path(root) / f
    return None


def to_ctrf_duration(seconds: Any) -> int:
    try:
        value = float(seconds)
    except (TypeError, ValueError):
        return 0
    return max(0, int(round(value * 1000)))


def build_ctrf_report(
    config: Dict[str, Any],
    p2p_results: Dict[str, Dict[str, Any]],
    f2p_results: Dict[str, Dict[str, Any]],
    hard_gate_passed: bool,
    hard_gate_failure_msg: Optional[str] = None,
    trajectory_record: Optional[str] = None,
    build_results: Optional[Dict[str, Dict[str, Any]]] = None,
    cheating_results: Optional[Dict[str, Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Assemble a conformant CTRF JSON structure expected by grader.py."""
    tests: List[Dict[str, Any]] = []

    build_raw = config.get("build") if isinstance(config, dict) else None
    if not isinstance(build_raw, list):
        build_raw = []
    cheating_raw = config.get("cheating") if isinstance(config, dict) else None
    if not isinstance(cheating_raw, list):
        cheating_raw = []
    f2p_raw = config.get("f2p") if isinstance(config, dict) else None
    if not isinstance(f2p_raw, list):
        f2p_raw = []
    p2p_raw = config.get("p2p") if isinstance(config, dict) else None
    if not isinstance(p2p_raw, list):
        p2p_raw = []

    build_configured = [str(node) for node in build_raw]
    cheating_configured = [str(node) for node in cheating_raw]
    f2p_configured = [str(node) for node in f2p_raw]
    p2p_configured = [str(node) for node in p2p_raw]

    # NOTE: BUILD/CHEATING (hard-gate) nodes are intentionally NOT emitted into
    # the CTRF tests array. The DeepSWE CTRF contract only recognizes F2P/P2P as
    # valid evaluation groups; hard-gate results live in hard-gate.json instead.
    # Emitting group=BUILD/CHEATING here makes the ds ctrf validator reject the
    # report ("invalid extra.deepswe.group") -> evaluation_success=false -> exit 1.
    # These loops used build_configured / cheating_configured / build_results /
    # cheating_results, which are now unused by CTRF assembly.
    _ = (build_configured, cheating_configured, build_results, cheating_results)

    # Populate P2P entries
    for node in p2p_configured:
        rdata = p2p_results.get(node)
        if rdata is not None:
            st = rdata.get("status", "failed")
            dur = to_ctrf_duration(rdata.get("duration", 0.0))
            msg = rdata.get("message")
        else:
            st = "failed"
            dur = 0
            msg = hard_gate_failure_msg or "P2P test not executed"

        entry = {
            "name": node,
            "status": st,
            "duration": dur,
            "testId": node,
            "extra": {
                "deepswe": {
                    "group": "P2P",
                    "required": True,
                }
            },
        }
        if msg:
            entry["message"] = str(msg)
        tests.append(entry)

    # Populate F2P entries
    for node in f2p_configured:
        rdata = f2p_results.get(node)
        if hard_gate_passed and rdata is not None:
            st = rdata.get("status", "failed")
            dur = to_ctrf_duration(rdata.get("duration", 0.0))
            msg = rdata.get("message")
        else:
            st = "failed"
            dur = 0
            msg = hard_gate_failure_msg or "F2P execution skipped due to Hard Gate failure"

        entry = {
            "name": node,
            "status": st,
            "duration": dur,
            "testId": node,
            "extra": {
                "deepswe": {
                    "group": "F2P",
                    "required": True,
                }
            },
        }
        if msg:
            entry["message"] = str(msg)
        tests.append(entry)

    statuses = ("passed", "failed", "skipped", "pending", "other")
    summary = {
        "tests": len(tests),
        "start": int(time.time()),
        "stop": int(time.time()),
        **{status: sum(item.get("status") == status for item in tests) for status in statuses},
    }

    task_id = config.get("task_id") if isinstance(config, dict) else None
    base_commit = config.get("base_commit") if isinstance(config, dict) else None

    report_dict: Dict[str, Any] = {
        "reportFormat": "CTRF",
        "specVersion": "0.0.0",
        "results": {
            "tool": {
                "name": "waitress-deepswe-verifier",
                "version": "2.3.0",
            },
            "summary": summary,
            "tests": tests,
            "extra": {
                "deepswe": {
                    "taskId": task_id,
                    "baseCommit": base_commit,
                }
            },
        }
    }
    if trajectory_record:
        report_dict["results"]["extra"]["refactor_trajectory_record"] = trajectory_record
    return report_dict


def run_f2p_tests(
    repo_path: Path,
    f2p_nodes: List[str],
) -> Dict[str, Dict[str, Any]]:
    """Execute F2P tests in isolated subprocess and record per-node results."""
    results: Dict[str, Dict[str, Any]] = {}
    if not f2p_nodes:
        return results

    runner_script = """
import json
import os
from pathlib import Path
import sys
import time
import pytest

repo_root = Path(sys.argv[1]).resolve()
src_dir = (repo_root / "src").resolve()
nodes_file = Path(sys.argv[2]).resolve()
results_file = Path(sys.argv[3]).resolve()

sys.path.insert(0, str(src_dir))
sys.path.insert(0, str(repo_root))

target_nodes = set(json.loads(nodes_file.read_text(encoding="utf-8")))

def normalize_nodeid(nodeid: str) -> str:
    parts = nodeid.split("::", 1)
    if len(parts) == 2:
        return parts[0].replace("\\\\", "/") + "::" + parts[1]
    return nodeid.replace("\\\\", "/")

class F2PExecutionPlugin:
    def __init__(self, targets):
        self.targets = targets
        self.results = {}
        self.node_starts = {}
        self.collection_errors = []

    def pytest_collectreport(self, report):
        if report.failed:
            self.collection_errors.append(f"{report.nodeid}: {report.longrepr}")

    def pytest_collection_modifyitems(self, items):
        selected = []
        for item in items:
            normalized_id = normalize_nodeid(item.nodeid)
            if normalized_id in self.targets:
                selected.append(item)
        items[:] = selected

    def pytest_runtest_logstart(self, nodeid, location):
        norm = normalize_nodeid(nodeid)
        self.node_starts[norm] = time.time()

    def pytest_runtest_logreport(self, report):
        norm = normalize_nodeid(report.nodeid)
        if norm not in self.targets:
            return

        if report.when == "setup" and report.skipped:
            self.results[norm] = {
                "status": "skipped",
                "duration": round(report.duration, 4),
                "message": str(report.longrepr or "skipped at setup"),
            }
        elif report.when == "call":
            duration = round(time.time() - self.node_starts.get(norm, time.time()), 4)
            if report.passed:
                self.results[norm] = {"status": "passed", "duration": duration, "message": None}
            elif report.skipped:
                self.results[norm] = {
                    "status": "skipped",
                    "duration": duration,
                    "message": str(report.longrepr or "skipped"),
                }
            elif report.failed:
                self.results[norm] = {
                    "status": "failed",
                    "duration": duration,
                    "message": str(report.longrepr or "failed"),
                }
        elif report.when == "teardown" and report.failed:
            if norm in self.results and self.results[norm]["status"] == "passed":
                self.results[norm]["status"] = "failed"
                self.results[norm]["message"] = str(report.longrepr or "teardown failure")

plugin = F2PExecutionPlugin(target_nodes)
pytest_args = [
    "-o", "addopts=",
    "-q",
    str(repo_root / "tests"),
]

exit_code = pytest.main(pytest_args, plugins=[plugin])
results_file.write_text(
    json.dumps({
        "exit_code": int(exit_code),
        "collection_errors": plugin.collection_errors,
        "results": plugin.results,
    }, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
sys.exit(int(exit_code))
"""
    tmp_nodes_path = repo_path / ".f2p_targets.tmp.json"
    tmp_results_path = repo_path / ".f2p_results.tmp.json"

    try:
        tmp_nodes_path.write_text(json.dumps(f2p_nodes), encoding="utf-8")
        env = os.environ.copy()
        src_path = str((repo_path / "src").resolve())
        repo_path_str = str(repo_path.resolve())
        env["PYTHONPATH"] = f"{src_path}{os.pathsep}{repo_path_str}{os.pathsep}{env.get('PYTHONPATH', '')}"

        proc = subprocess.run(
            [
                sys.executable,
                "-c",
                runner_script,
                str(repo_path),
                str(tmp_nodes_path),
                str(tmp_results_path),
            ],
            cwd=str(repo_path),
            env=env,
            capture_output=True,
            text=True,
            timeout=300,
        )

        # Pytest exit code semantics:
        # 0: all tests passed
        # 1: tests were executed and some failed (expected when capability is missing)
        # 2: interrupted, 3: internal error, 4: command line usage error, 5: no tests collected
        if proc.returncode not in (0, 1):
            err_diag = proc.stderr.strip() or proc.stdout.strip() or f"exit code {proc.returncode}"
            raise RuntimeError(f"Pytest F2P runner infrastructure error (code {proc.returncode}): {err_diag[:500]}")

        if not tmp_results_path.is_file():
            err_diag = proc.stderr.strip() or proc.stdout.strip() or f"exit code {proc.returncode}"
            raise RuntimeError(f"Pytest F2P runner failed to produce results file: {err_diag[:500]}")

        data = json.loads(tmp_results_path.read_text(encoding="utf-8"))
        collection_errors = data.get("collection_errors", [])
        if collection_errors:
            raise RuntimeError(f"Pytest F2P collection error: {'; '.join(collection_errors[:3])}")

        results = data.get("results", {})
        missing_nodes = [node for node in f2p_nodes if node not in results]
        if missing_nodes:
            raise RuntimeError(
                f"Pytest F2P runner failed to collect or execute {len(missing_nodes)} node(s): {missing_nodes[:3]}"
            )
    finally:
        for p in (tmp_nodes_path, tmp_results_path):
            if p.is_file():
                try:
                    p.unlink()
                except OSError:
                    pass

    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Task-specific unified F2P/P2P verifier entrypoint")
    parser.add_argument("--config", type=Path, required=True, help="Path to config.json")
    parser.add_argument("--repo", type=Path, required=True, help="Path to repository under test")
    parser.add_argument("--ctrf-output", type=Path, required=True, help="Path to output ctrf.json")
    parser.add_argument("--hard-gate-output", type=Path, required=True, help="Path to output hard-gate.json")
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args()

    try:
        config = json.loads(args.config.read_text(encoding="utf-8"))
        if not isinstance(config, dict):
            config = {}
    except Exception:
        config = {}

    # Step 1: Execute Hard Gate
    hard_gate_result = hardgate.run_hard_gate(
        config_path=args.config,
        repo_path=args.repo,
        output_path=args.hard_gate_output,
        apply_failed=args.apply_failed,
    )

    hard_gate_passed = hard_gate_result.get("passed") is True
    build_results = hard_gate_result.get("groups", {}).get("BUILD", {}).get("nodes", {})
    cheating_results = hard_gate_result.get("groups", {}).get("CHEATING", {}).get("nodes", {})
    p2p_results = hard_gate_result.get("groups", {}).get("P2P", {}).get("nodes", {})
    if not p2p_results and "node_results" in hard_gate_result:
        p2p_results = hard_gate_result["node_results"]
    f2p_results: Dict[str, Dict[str, Any]] = {}

    # Step 2: Short-circuit on Hard Gate failure
    if not hard_gate_passed:
        failure_reasons = hard_gate_result.get("failed_nodes", [])
        failure_msg = "Hard Gate failed: " + (", ".join(failure_reasons[:3]) if failure_reasons else "Unknown failure")
        ctrf_report = build_ctrf_report(
            config=config,
            p2p_results=p2p_results,
            f2p_results=f2p_results,
            hard_gate_passed=False,
            hard_gate_failure_msg=failure_msg,
            build_results=build_results,
            cheating_results=cheating_results,
        )
        args.ctrf_output.parent.mkdir(parents=True, exist_ok=True)
        args.ctrf_output.write_text(json.dumps(ctrf_report, indent=2) + "\n", encoding="utf-8")
        return 0

    # Step 3: Hard Gate passed -> Execute F2P tests
    f2p_raw = config.get("f2p") if isinstance(config, dict) else None
    f2p_nodes = [str(node) for node in f2p_raw] if isinstance(f2p_raw, list) else []
    if f2p_nodes:
        try:
            f2p_results = run_f2p_tests(args.repo, f2p_nodes)
        except RuntimeError as exc:
            sys.stderr.write(f"FATAL F2P RUNNER ERROR: {exc}\n")
            return 1

    trajectory_record_file = find_refactor_trajectory_record(args.repo)
    trajectory_rel_path = None
    if trajectory_record_file is not None:
        try:
            trajectory_rel_path = str(trajectory_record_file.relative_to(args.repo)).replace("\\", "/")
        except ValueError:
            trajectory_rel_path = str(trajectory_record_file).replace("\\", "/")

    ctrf_report = build_ctrf_report(
        config=config,
        p2p_results=p2p_results,
        f2p_results=f2p_results,
        hard_gate_passed=True,
        trajectory_record=trajectory_rel_path,
        build_results=build_results,
        cheating_results=cheating_results,
    )
    args.ctrf_output.parent.mkdir(parents=True, exist_ok=True)
    args.ctrf_output.write_text(json.dumps(ctrf_report, indent=2) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    sys.exit(main())
