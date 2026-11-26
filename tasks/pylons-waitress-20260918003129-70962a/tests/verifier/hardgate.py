#!/usr/bin/env python3
"""Waitress Hard Gate Verification System.

Hard Gate detects fatal defects after model refactoring across three categories:
1. BUILD Gate: Verifies configuration, schema, task counts, base commit consistency,
   runtime dependencies, AST syntax, py_compile bytecode compilation, module imports,
   patch applicability, and entrypoint integrity.
   (Registered in config['build'] and implemented in tests/test_hardgate_build.py)
2. CHEATING Gate (Fail-Closed): Enforces strict anti-cheat policies: candidate patch scope
   (restricted strictly to src/waitress/), test suite protection (Ground Truth immutability), test runner config
   protection, verifier infrastructure protection, rogue startup hook detection, evasion pattern
   scanning, and fail-closed git inspection.
   (Registered in config['cheating'] and implemented in tests/test_hardgate_cheating.py)
3. P2P Gate: Regression tests verifying task semantics and core constraints remain
   consistent (no task mismatch, intent drift, or lost critical behavior).
   - Strict leaf atomicity: One functional check = one test node.
   - Strict quantity constraint: Count >= 30.
   - Complete inventory: All frozen original nodes in p2p_select.txt must be present.
   - Strict execution: Unexecuted, missing, skipped, or duplicate tests fail by configuration.

Sequential short-circuiting:
- BUILD fails -> CHEATING, P2P, F2P skipped.
- CHEATING fails -> P2P, F2P skipped.
- P2P fails -> F2P skipped.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
from pathlib import Path
import py_compile
import subprocess
import sys
import tempfile
import time
from typing import Any, Dict, List, Optional, Set, Tuple

TEST_RUNNER_CONFIG_FILES: Tuple[str, ...] = (
    "pytest.ini",
    "pyproject.toml",
    "setup.cfg",
    "setup.py",
    "tox.ini",
    "conftest.py",
)

CORE_IMPORT_MODULES: Tuple[str, ...] = (
    "waitress",
    "waitress.adjustments",
    "waitress.buffers",
    "waitress.channel",
    "waitress.compat",
    "waitress.parser",
    "waitress.receiver",
    "waitress.server",
    "waitress.task",
    "waitress.utilities",
)

SUSPICIOUS_CHEAT_PATTERNS: Tuple[str, ...] = (
    "/logs/verifier/ctrf.json",
    "/logs/verifier/hard-gate.json",
    "/logs/verifier/reward.json",
    "grader.py",
    "verifier.py",
    "hardgate.py",
    "sys.modules['grader']",
    "sys.modules[\"grader\"]",
    "sys.modules['verifier']",
    "sys.modules[\"verifier\"]",
)

DANGEROUS_STARTUP_HOOKS: Tuple[str, ...] = (
    "sitecustomize.py",
    "usercustomize.py",
)


def normalize_nodeid(nodeid: str) -> str:
    """Normalize node IDs by converting Windows backslashes in the file part to slashes."""
    parts = nodeid.split("::", 1)
    if len(parts) == 2:
        return parts[0].replace("\\", "/") + "::" + parts[1]
    return nodeid.replace("\\", "/")


def parse_task_toml_metadata(
    toml_path: Path,
) -> Tuple[Optional[int], Optional[int], Optional[str], List[str]]:
    """Parse task.toml to extract pass_to_pass_count, fail_to_pass_count, and base_commit_hash."""
    errors: List[str] = []
    p2p_cnt: Optional[int] = None
    f2p_cnt: Optional[int] = None
    base_commit: Optional[str] = None

    try:
        text = toml_path.read_text(encoding="utf-8")
    except Exception as exc:
        return None, None, None, [f"task_toml_read_error:{exc}"]

    # Strategy 1: standard tomllib / tomli
    data: Optional[Dict[str, Any]] = None
    try:
        import tomllib  # Python 3.11+
        data = tomllib.loads(text)
    except ImportError:
        pass

    if data is None:
        try:
            import tomli  # Fallback
            data = tomli.loads(text)
        except ImportError:
            pass

    if isinstance(data, dict):
        tests_sec = data.get("tests", {})
        if isinstance(tests_sec, dict):
            p2p_raw = tests_sec.get("pass_to_pass_count")
            f2p_raw = tests_sec.get("fail_to_pass_count")
            if isinstance(p2p_raw, int):
                p2p_cnt = p2p_raw
            if isinstance(f2p_raw, int):
                f2p_cnt = f2p_raw

        meta_sec = data.get("metadata", {})
        if isinstance(meta_sec, dict):
            bc = meta_sec.get("base_commit_hash")
            if isinstance(bc, str) and bc.strip():
                base_commit = bc.strip()

        if base_commit is None:
            task_sec = data.get("task", {})
            if isinstance(task_sec, dict):
                bc = task_sec.get("base_commit_hash")
                if isinstance(bc, str) and bc.strip():
                    base_commit = bc.strip()

        return p2p_cnt, f2p_cnt, base_commit, errors

    # Strategy 2: regex fallback
    current_sec = ""
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current_sec = line[1:-1].strip()
            continue
        if "=" in line:
            k, v = [x.strip() for x in line.split("=", 1)]
            v_clean = v.strip("\"'")
            if current_sec == "tests":
                if k == "pass_to_pass_count":
                    try:
                        p2p_cnt = int(v_clean)
                    except ValueError:
                        errors.append(f"task_toml_invalid_p2p_count:{v}")
                elif k == "fail_to_pass_count":
                    try:
                        f2p_cnt = int(v_clean)
                    except ValueError:
                        errors.append(f"task_toml_invalid_f2p_count:{v}")
            elif current_sec in ("metadata", "task"):
                if k == "base_commit_hash" and base_commit is None:
                    base_commit = v_clean

    return p2p_cnt, f2p_cnt, base_commit, errors


def load_p2p_nodes(
    config: Dict[str, Any],
    config_path: Path,
    repo_path: Path,
) -> Tuple[List[str], List[str], List[str]]:
    """Load and validate P2P test inventory from config and frozen p2p_select.txt."""
    errors: List[str] = []

    if not isinstance(config, dict) or "p2p" not in config:
        errors.append("config:missing_p2p_field")
        return [], [], errors

    p2p_raw = config["p2p"]
    if not isinstance(p2p_raw, list):
        errors.append("config:p2p_not_a_list")
        return [], [], errors

    configured_nodes = [str(node) for node in p2p_raw]

    # Validate against frozen original inventory
    p2p_select_path: Optional[Path] = None
    candidate_paths = [
        config_path.parent / "p2p_select.txt",
        repo_path / "case" / "tests" / "p2p_select.txt",
        Path("/tests/p2p_select.txt"),
    ]
    for p in candidate_paths:
        if p.is_file():
            p2p_select_path = p.resolve()
            break

    frozen_original_nodes: List[str] = []
    if p2p_select_path is not None:
        try:
            for line in p2p_select_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#"):
                    frozen_original_nodes.append(normalize_nodeid(line))
        except Exception as exc:
            errors.append(f"p2p:cannot_read_p2p_select_txt:{exc}")

    return configured_nodes, frozen_original_nodes, errors


def validate_group_atomicity(
    repo_path: Path,
    nodes: List[str],
    group_name: str,
    target_files: Optional[List[str]] = None,
) -> Tuple[bool, List[str], Dict[str, Any]]:
    """Validate leaf node atomicity for a group of tests via live pytest collection."""
    errors: List[str] = []
    details: Dict[str, Any] = {
        "group": group_name,
        "collection_returncode": None,
        "collected_leaves_count": 0,
        "configured_count": len(nodes),
    }

    tmp_out = Path(tempfile.gettempdir()) / f"deepswe_{group_name.lower()}_{os.getpid()}_{time.time_ns()}_collection.json"

    collector_script = """
import json
import os
from pathlib import Path
import sys
import pytest

repo_root = Path(sys.argv[1]).resolve()
src_dir = (repo_root / "src").resolve()
output_file = Path(sys.argv[2]).resolve()
target_paths = json.loads(sys.argv[3]) if len(sys.argv) > 3 else []

sys.path.insert(0, str(src_dir))
sys.path.insert(0, str(repo_root))

def normalize_nodeid(nodeid: str) -> str:
    parts = nodeid.split("::", 1)
    if len(parts) == 2:
        return parts[0].replace("\\\\", "/") + "::" + parts[1]
    return nodeid.replace("\\\\", "/")

class LeafCollector:
    def __init__(self):
        self.leaves = {}

    def pytest_collection_modifyitems(self, items):
        for item in items:
            norm_id = normalize_nodeid(item.nodeid)
            self.leaves[norm_id] = {
                "class": item.__class__.__name__,
                "is_item": isinstance(item, pytest.Item),
            }

col = LeafCollector()
pytest_args = [
    "--collect-only",
    "-q",
    "-o", "addopts=",
]
if target_paths:
    pytest_args.extend([str((repo_root / p).resolve()) for p in target_paths])
else:
    pytest_args.append(str(repo_root / "tests"))

exit_code = pytest.main(pytest_args, plugins=[col])
output_file.write_text(
    json.dumps({
        "exit_code": int(exit_code),
        "leaves": col.leaves,
    }, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
sys.exit(int(exit_code))
"""
    try:
        env = os.environ.copy()
        src_path = str((repo_path / "src").resolve())
        repo_path_str = str(repo_path.resolve())
        env["PYTHONPATH"] = f"{src_path}{os.pathsep}{repo_path_str}{os.pathsep}{env.get('PYTHONPATH', '')}"

        target_arg = json.dumps(target_files) if target_files else json.dumps([])

        proc = subprocess.run(
            [
                sys.executable,
                "-c",
                collector_script,
                str(repo_path.resolve()),
                str(tmp_out.resolve()),
                target_arg,
            ],
            cwd=str(repo_path.resolve()),
            env=env,
            capture_output=True,
            text=True,
            timeout=60,
        )

        details["collection_returncode"] = proc.returncode

        if proc.returncode != 0:
            err_msg = proc.stderr.strip() or proc.stdout.strip() or f"exit_code_{proc.returncode}"
            errors.append(f"{group_name}:pytest_collection_failed:exit_{proc.returncode}:{err_msg[:300]}")
            return False, errors, details

        if not tmp_out.is_file():
            errors.append(f"{group_name}:collection_output_missing")
            return False, errors, details

        col_data = json.loads(tmp_out.read_text(encoding="utf-8"))
        leaves = col_data.get("leaves", {})
        details["collected_leaves_count"] = len(leaves)

        for node in nodes:
            parts = node.split("::")
            if len(parts) < 2:
                errors.append(f"{group_name}:non_atomic_node:{node}")

            if node not in leaves:
                if sys.platform.startswith("win") and "test_trigger.py" in node:
                    continue
                errors.append(f"{group_name}:configured_node_not_in_collection:{node}")
            else:
                leaf_meta = leaves[node]
                if not leaf_meta.get("is_item", False):
                    errors.append(f"{group_name}:node_not_leaf_item:{node}")

    except subprocess.TimeoutExpired:
        errors.append(f"{group_name}:collection_timeout_60s")
    except Exception as exc:
        errors.append(f"{group_name}:collection_exception:{exc}")
    finally:
        if tmp_out.is_file():
            try:
                tmp_out.unlink()
            except OSError:
                pass

    passed = len(errors) == 0
    return passed, errors, details


def run_pytest_node_group(
    repo_path: Path,
    target_nodes: List[str],
    group_name: str,
    config_path: Path,
    target_files: Optional[List[str]] = None,
    timeout: int = 1800,
    skip_is_failure: bool = True,
    missing_is_failure: bool = True,
) -> Tuple[bool, List[str], Dict[str, Any], Dict[str, Dict[str, Any]], Dict[str, Any]]:
    """Execute a specific group of pytest test nodes and record per-node results."""
    failed_nodes: List[str] = []
    node_results: Dict[str, Dict[str, Any]] = {}
    diagnostics: Dict[str, Any] = {
        "group": group_name,
        "runner_returncode": None,
        "runner_stdout": "",
        "runner_stderr": "",
    }
    stats = {"passed": 0, "failed": 0, "skipped": 0, "missing": 0}

    runner_script = """
import json
import os
from pathlib import Path
import sys
import time
import pytest

repo_root = Path(sys.argv[1]).resolve()
src_dir = (repo_root / "src").resolve()
target_nodes_file = Path(sys.argv[2]).resolve()
results_file = Path(sys.argv[3]).resolve()
target_paths = json.loads(sys.argv[4]) if len(sys.argv) > 4 else []

sys.path.insert(0, str(src_dir))
sys.path.insert(0, str(repo_root))

target_nodes = set(json.loads(target_nodes_file.read_text(encoding="utf-8")))

def normalize_nodeid(nodeid: str) -> str:
    parts = nodeid.split("::", 1)
    if len(parts) == 2:
        return parts[0].replace("\\\\", "/") + "::" + parts[1]
    return nodeid.replace("\\\\", "/")

class GroupExecutionPlugin:
    def __init__(self, targets):
        self.targets = targets
        self.results = {}
        self.node_starts = {}

    def pytest_collection_modifyitems(self, items):
        selected = []
        for item in items:
            norm_id = normalize_nodeid(item.nodeid)
            if norm_id in self.targets:
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

plugin = GroupExecutionPlugin(target_nodes)
pytest_args = [
    "-o", "addopts=",
    "-q",
]
if target_paths:
    pytest_args.extend([str((repo_root / p).resolve()) for p in target_paths])
else:
    pytest_args.append(str(repo_root / "tests"))

exit_code = pytest.main(pytest_args, plugins=[plugin])
results_file.write_text(
    json.dumps({
        "exit_code": int(exit_code),
        "results": plugin.results,
    }, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
sys.exit(int(exit_code))
"""
    tmp_prefix = group_name.lower()
    tmp_dir = Path(tempfile.gettempdir())
    tmp_nodes_path = tmp_dir / f"deepswe_{tmp_prefix}_{os.getpid()}_{time.time_ns()}_targets.json"
    tmp_results_path = tmp_dir / f"deepswe_{tmp_prefix}_{os.getpid()}_{time.time_ns()}_results.json"

    try:
        tmp_nodes_path.write_text(json.dumps(target_nodes), encoding="utf-8")

        env = os.environ.copy()
        src_path = str((repo_path / "src").resolve())
        repo_path_str = str(repo_path.resolve())
        env["PYTHONPATH"] = f"{src_path}{os.pathsep}{repo_path_str}{os.pathsep}{env.get('PYTHONPATH', '')}"
        env["DEEPSWE_CONFIG_PATH"] = str(config_path.resolve())
        env["DEEPSWE_REPO_PATH"] = str(repo_path.resolve())
        target_arg = json.dumps(target_files) if target_files else json.dumps([])

        proc = subprocess.run(
            [
                sys.executable,
                "-c",
                runner_script,
                str(repo_path.resolve()),
                str(tmp_nodes_path.resolve()),
                str(tmp_results_path.resolve()),
                target_arg,
            ],
            cwd=str(repo_path.resolve()),
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout,
        )

        diagnostics["runner_returncode"] = proc.returncode
        diagnostics["runner_stdout"] = proc.stdout
        diagnostics["runner_stderr"] = proc.stderr

        if proc.returncode not in (0, 1):
            err = proc.stderr.strip() or proc.stdout.strip() or f"exit_{proc.returncode}"
            failed_nodes.append(f"{group_name}:pytest_infrastructure_error:exit_{proc.returncode}:{err[:300]}")

        raw_results: Dict[str, Dict[str, Any]] = {}
        if tmp_results_path.is_file():
            try:
                run_data = json.loads(tmp_results_path.read_text(encoding="utf-8"))
                raw_results = run_data.get("results", {})
            except Exception as exc:
                failed_nodes.append(f"{group_name}:cannot_parse_results:{exc}")
        else:
            failed_nodes.append(f"{group_name}:results_file_not_generated")

        for node in target_nodes:
            if node in raw_results:
                item = raw_results[node]
                st = item.get("status", "failed")
                dur = float(item.get("duration", 0.0))
                msg = item.get("message")
                node_entry = {
                    "status": st,
                    "duration": dur,
                    "group": group_name,
                    "message": msg,
                }
                node_results[node] = node_entry

                if st == "passed":
                    stats["passed"] += 1
                elif st == "skipped":
                    stats["skipped"] += 1
                    if skip_is_failure:
                        failed_nodes.append(node)
                else:
                    stats["failed"] += 1
                    failed_nodes.append(node)
            else:
                stats["missing"] += 1
                node_results[node] = {
                    "status": "failed",
                    "duration": 0.0,
                    "group": group_name,
                    "message": f"missing: test node not reported by {group_name} runner",
                }
                if missing_is_failure:
                    failed_nodes.append(node)

    except subprocess.TimeoutExpired:
        failed_nodes.append(f"{group_name}:execution_timeout_{timeout}s")
    except Exception as exc:
        failed_nodes.append(f"{group_name}:execution_exception:{exc}")
    finally:
        for p in (tmp_nodes_path, tmp_results_path):
            if p.is_file():
                try:
                    p.unlink()
                except OSError:
                    pass

    group_passed = len(failed_nodes) == 0
    return group_passed, failed_nodes, stats, node_results, diagnostics


def run_hard_gate(
    config_path: Path,
    repo_path: Path,
    output_path: Path,
    apply_failed: int = 0,
    skip_p2p: bool = False,
) -> Dict[str, Any]:
    """Execute all Hard Gate checks and generate the official hard-gate.json report.

    Implements strict sequential short-circuiting across the 3 categories:
    1. Candidate Patch Check: If apply_failed -> short-circuit immediately.
    2. Configuration Validation: If config invalid or arrays missing -> short-circuit immediately.
    3. BUILD Gate (tests/test_hardgate_build.py): If fails -> short-circuit without CHEATING, P2P, or F2P.
    4. CHEATING Gate (tests/test_hardgate_cheating.py): If fails -> short-circuit without P2P or F2P.
    5. P2P Gate: If fails or skipped -> short-circuit without F2P.
    """
    config: Dict[str, Any] = {}
    try:
        raw_content = config_path.read_text(encoding="utf-8")
        parsed_json = json.loads(raw_content)
        if not isinstance(parsed_json, dict):
            raise ValueError("config.json must be a JSON object")
        config = parsed_json
    except Exception as exc:
        result = {
            "passed": False,
            "apply_failed": bool(apply_failed),
            "compile_paths": [],
            "failed_nodes": [f"hard_gate:config_error:{exc}"],
            "cheat_penalty": 0.0,
            "short_circuit": "config_json_invalid",
            "summary": {
                "build_passed": False,
                "cheating_passed": False,
                "p2p_passed": False,
                "short_circuit": "config_json_invalid",
            },
            "groups": {},
            "node_results": {},
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return result

    # 1. Candidate Patch Application Check
    if apply_failed:
        result = {
            "passed": False,
            "apply_failed": True,
            "compile_paths": [],
            "failed_nodes": ["candidate_patch_apply"],
            "cheat_penalty": 0.0,
            "short_circuit": "candidate_patch_apply_failed",
            "summary": {
                "build_passed": False,
                "cheating_passed": False,
                "p2p_passed": False,
                "short_circuit": "candidate_patch_apply_failed",
            },
            "groups": {},
            "node_results": {},
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return result

    skip_is_failure = True
    missing_is_failure = True
    all_failed_nodes: List[str] = []
    all_node_results: Dict[str, Dict[str, Any]] = {}
    groups_data: Dict[str, Any] = {}

    build_nodes = [str(n) for n in config.get("build", [])]
    cheating_nodes = [str(n) for n in config.get("cheating", [])]
    p2p_nodes = [str(n) for n in config.get("p2p", [])]

    # Validate required top-level arrays
    for cat_name, cat_arr in [("build", build_nodes), ("cheating", cheating_nodes), ("p2p", p2p_nodes)]:
        if not cat_arr:
            all_failed_nodes.append(f"config:missing_or_empty_{cat_name}_array")

    if all_failed_nodes:
        result = {
            "passed": False,
            "apply_failed": False,
            "compile_paths": [],
            "failed_nodes": all_failed_nodes,
            "cheat_penalty": 0.0,
            "short_circuit": "config_arrays_missing_or_empty",
            "summary": {
                "build_passed": False,
                "cheating_passed": False,
                "p2p_passed": False,
                "short_circuit": "config_arrays_missing_or_empty",
            },
            "groups": {},
            "node_results": {},
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return result

    # =========================================================================
    # Step 1: BUILD Gate
    # =========================================================================
    build_files = ["tests/test_hardgate_build.py"]
    build_atomicity_ok, build_atom_errs, _ = validate_group_atomicity(
        repo_path, build_nodes, "BUILD", build_files
    )
    if not build_atomicity_ok:
        all_failed_nodes.extend(build_atom_errs)
        result = {
            "passed": False,
            "apply_failed": False,
            "compile_paths": [],
            "failed_nodes": all_failed_nodes,
            "cheat_penalty": 0.0,
            "short_circuit": "build_leaf_atomicity_failed",
            "summary": {
                "build_passed": False,
                "cheating_passed": False,
                "p2p_passed": False,
                "short_circuit": "build_leaf_atomicity_failed",
            },
            "groups": {},
            "node_results": {},
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return result

    build_passed, build_failed, build_stats, build_results, _ = run_pytest_node_group(
        repo_path=repo_path,
        target_nodes=build_nodes,
        group_name="BUILD",
        config_path=config_path,
        target_files=build_files,
        skip_is_failure=skip_is_failure,
        missing_is_failure=missing_is_failure,
    )
    all_failed_nodes.extend(build_failed)
    all_node_results.update(build_results)
    groups_data["BUILD"] = {
        "total": len(build_nodes),
        "passed": build_stats["passed"],
        "failed": build_stats["failed"],
        "skipped": build_stats["skipped"],
        "missing": build_stats["missing"],
        "nodes": build_results,
    }

    if not build_passed:
        result = {
            "passed": False,
            "apply_failed": False,
            "compile_paths": [],
            "failed_nodes": all_failed_nodes,
            "cheat_penalty": 0.0,
            "short_circuit": "build_gate_failed",
            "summary": {
                "build_total": len(build_nodes),
                "build_passed_count": build_stats["passed"],
                "build_failed_count": build_stats["failed"],
                "build_skipped_count": build_stats["skipped"],
                "build_missing_count": build_stats["missing"],
                "build_passed": False,
                "cheating_passed": False,
                "p2p_passed": False,
                "short_circuit": "build_gate_failed",
            },
            "groups": groups_data,
            "node_results": all_node_results,
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return result

    # =========================================================================
    # Step 2: CHEATING Gate (Fail-Closed)
    # =========================================================================
    cheat_files = ["tests/test_hardgate_cheating.py"]
    cheat_atomicity_ok, cheat_atom_errs, _ = validate_group_atomicity(
        repo_path, cheating_nodes, "CHEATING", cheat_files
    )
    if not cheat_atomicity_ok:
        all_failed_nodes.extend(cheat_atom_errs)
        result = {
            "passed": False,
            "apply_failed": False,
            "compile_paths": [],
            "failed_nodes": all_failed_nodes,
            "cheat_penalty": -1.0,
            "short_circuit": "cheating_leaf_atomicity_failed",
            "summary": {
                "build_passed": True,
                "cheating_passed": False,
                "p2p_passed": False,
                "short_circuit": "cheating_leaf_atomicity_failed",
            },
            "groups": groups_data,
            "node_results": all_node_results,
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return result

    cheat_passed, cheat_failed, cheat_stats, cheat_results, _ = run_pytest_node_group(
        repo_path=repo_path,
        target_nodes=cheating_nodes,
        group_name="CHEATING",
        config_path=config_path,
        target_files=cheat_files,
        skip_is_failure=skip_is_failure,
        missing_is_failure=missing_is_failure,
    )
    all_failed_nodes.extend(cheat_failed)
    all_node_results.update(cheat_results)
    groups_data["CHEATING"] = {
        "total": len(cheating_nodes),
        "passed": cheat_stats["passed"],
        "failed": cheat_stats["failed"],
        "skipped": cheat_stats["skipped"],
        "missing": cheat_stats["missing"],
        "nodes": cheat_results,
    }

    if not cheat_passed:
        result = {
            "passed": False,
            "apply_failed": False,
            "compile_paths": [],
            "failed_nodes": all_failed_nodes,
            "cheat_penalty": -1.0,
            "short_circuit": "anti_cheat_gate_failed",
            "summary": {
                "build_total": len(build_nodes),
                "build_passed_count": build_stats["passed"],
                "build_failed_count": build_stats["failed"],
                "build_skipped_count": build_stats["skipped"],
                "build_missing_count": build_stats["missing"],
                "build_passed": True,
                "cheating_total": len(cheating_nodes),
                "cheating_passed_count": cheat_stats["passed"],
                "cheating_failed_count": cheat_stats["failed"],
                "cheating_skipped_count": cheat_stats["skipped"],
                "cheating_missing_count": cheat_stats["missing"],
                "cheating_passed": False,
                "p2p_passed": False,
                "short_circuit": "anti_cheat_gate_failed",
            },
            "groups": groups_data,
            "node_results": all_node_results,
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return result

    # =========================================================================
    # Step 3: P2P Regression Gate
    # =========================================================================
    p2p_configured_nodes, frozen_original_nodes, p2p_load_errors = load_p2p_nodes(config, config_path, repo_path)
    if p2p_load_errors:
        all_failed_nodes.extend(p2p_load_errors)
        result = {
            "passed": False,
            "apply_failed": False,
            "compile_paths": [],
            "failed_nodes": all_failed_nodes,
            "cheat_penalty": 0.0,
            "short_circuit": "p2p_inventory_failed",
            "summary": {
                "build_passed": True,
                "cheating_passed": True,
                "p2p_passed": False,
                "short_circuit": "p2p_inventory_failed",
            },
            "groups": groups_data,
            "node_results": all_node_results,
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return result

    # Check complete inventory of frozen original nodes
    p2p_set = set(p2p_configured_nodes)
    for fnode in frozen_original_nodes:
        if fnode not in p2p_set:
            all_failed_nodes.append(f"p2p:frozen_node_missing_from_config:{fnode}")

    if len(p2p_configured_nodes) < 30:
        all_failed_nodes.append(f"p2p:insufficient_count:{len(p2p_configured_nodes)}_less_than_30")

    if all_failed_nodes:
        result = {
            "passed": False,
            "apply_failed": False,
            "compile_paths": [],
            "failed_nodes": all_failed_nodes,
            "cheat_penalty": 0.0,
            "short_circuit": "p2p_inventory_constraint_violation",
            "summary": {
                "build_passed": True,
                "cheating_passed": True,
                "p2p_passed": False,
                "short_circuit": "p2p_inventory_constraint_violation",
            },
            "groups": groups_data,
            "node_results": all_node_results,
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return result

    # Prohibition of unexecuted P2P tests passing
    if skip_p2p:
        all_failed_nodes.append("p2p:execution_skipped")
        result = {
            "passed": False,
            "apply_failed": False,
            "compile_paths": [],
            "failed_nodes": all_failed_nodes,
            "cheat_penalty": 0.0,
            "short_circuit": "p2p_execution_skipped",
            "summary": {
                "build_passed": True,
                "cheating_passed": True,
                "p2p_passed": False,
                "short_circuit": "p2p_execution_skipped",
            },
            "groups": groups_data,
            "node_results": all_node_results,
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return result

    p2p_atomicity_ok, p2p_atom_errs, _ = validate_group_atomicity(
        repo_path, p2p_configured_nodes, "P2P"
    )
    if not p2p_atomicity_ok:
        all_failed_nodes.extend(p2p_atom_errs)
        result = {
            "passed": False,
            "apply_failed": False,
            "compile_paths": [],
            "failed_nodes": all_failed_nodes,
            "cheat_penalty": 0.0,
            "short_circuit": "p2p_leaf_atomicity_failed",
            "summary": {
                "build_passed": True,
                "cheating_passed": True,
                "p2p_passed": False,
                "short_circuit": "p2p_leaf_atomicity_failed",
            },
            "groups": groups_data,
            "node_results": all_node_results,
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return result

    p2p_passed, p2p_failed, p2p_stats, p2p_results, _ = run_pytest_node_group(
        repo_path=repo_path,
        target_nodes=p2p_configured_nodes,
        group_name="P2P",
        config_path=config_path,
        skip_is_failure=skip_is_failure,
        missing_is_failure=missing_is_failure,
    )
    all_failed_nodes.extend(p2p_failed)
    all_node_results.update(p2p_results)
    groups_data["P2P"] = {
        "total": len(p2p_configured_nodes),
        "passed": p2p_stats["passed"],
        "failed": p2p_stats["failed"],
        "skipped": p2p_stats["skipped"],
        "missing": p2p_stats["missing"],
        "nodes": p2p_results,
    }

    overall_passed = build_passed and cheat_passed and p2p_passed and len(all_failed_nodes) == 0
    short_circuit = None if overall_passed else "p2p_gate_failed"

    result = {
        "passed": overall_passed,
        "apply_failed": False,
        "compile_paths": [],
        "failed_nodes": all_failed_nodes,
        "cheat_penalty": 0.0,
        "short_circuit": short_circuit,
        "summary": {
            "build_total": len(build_nodes),
            "build_passed_count": build_stats["passed"],
            "build_failed_count": build_stats["failed"],
            "build_skipped_count": build_stats["skipped"],
            "build_missing_count": build_stats["missing"],
            "build_passed": build_passed,
            "cheating_total": len(cheating_nodes),
            "cheating_passed_count": cheat_stats["passed"],
            "cheating_failed_count": cheat_stats["failed"],
            "cheating_skipped_count": cheat_stats["skipped"],
            "cheating_missing_count": cheat_stats["missing"],
            "cheating_passed": cheat_passed,
            "p2p_total": len(p2p_configured_nodes),
            "p2p_passed_count": p2p_stats["passed"],
            "p2p_failed_count": p2p_stats["failed"],
            "p2p_skipped_count": p2p_stats["skipped"],
            "p2p_missing_count": p2p_stats["missing"],
            "p2p_passed": p2p_passed,
            "overall_passed": overall_passed,
            "short_circuit": short_circuit,
        },
        "groups": groups_data,
        "node_results": all_node_results,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Standalone Waitress Hard Gate Checker")
    parser.add_argument("--config", type=Path, required=True, help="Path to config.json")
    parser.add_argument("--repo", type=Path, required=True, help="Path to repository under test")
    parser.add_argument("--output", type=Path, default=Path("/logs/verifier/hard-gate.json"))
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    parser.add_argument("--skip-p2p", action="store_true", help="Skip P2P execution (will fail gate)")
    args = parser.parse_args()

    result = run_hard_gate(
        config_path=args.config,
        repo_path=args.repo,
        output_path=args.output,
        apply_failed=args.apply_failed,
        skip_p2p=args.skip_p2p,
    )
    return 0 if result.get("passed") else 1


if __name__ == "__main__":
    sys.exit(main())
