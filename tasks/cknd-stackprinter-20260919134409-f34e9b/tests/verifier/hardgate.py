#!/usr/bin/env python3
"""
Compile, integrity, P2P, and anti-cheat hard gates.

Checks three categories:
1. P2P: Verifies that pre- and post-refactoring semantics, I/O behavior, and core constraints
   remain consistent (atomic test nodes, count >= 30).
2. Build: Verifies that the task meets parseable, executable, and reproducible conditions
   (schema valid, patch applies, syntax compiles, package imports, dependencies verified).
3. Cheating: Detects test tampering, evaluator bypass, or data leakage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import py_compile
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


# Normalized (LF) SHA-256 hashes of original protected files at base commit 7a07a51
BASELINE_PROTECTED_HASHES = {
    "tests/test_formatting.py": "eaed320e3a2abcf755d51a9f0c5145c5a0ac4523dcbcc758e5651a9363cb2879",
    "tests/test_frame_inspection.py": "a22c18037b9939b39a3eada48a4cde8f0ac3e6044f24189591db1e5e88ecf211",
    "tests/test_source_inspection.py": "78bc6f64421c1d5e6459f15ad2d4cff4acdaf68c0a435f0c30acc16a33b54b62",
    "tests/test_utils.py": "3f33c48d83d9d0ed261170638b64a1d934d1d611d8a9e8d64b23b856a3ac1d6a",
    "tests/conftest.py": "e33bc2fa6863809b05b02b667336c19efa13f9590822a416aa9ed7d261035a06",
    "tests/source.py": "a01e2811b3fedb879154096f1cb5dd59d20d72a0c2041c1ca0dc5aa334e59ad6",
}

PROHIBITED_ROOT_FILES = [
    "sitecustomize.py",
    "usercustomize.py",
    "pytest.py",
    "conftest.py",
    "pytest.ini",
    "setup.cfg",
    "tox.ini",
    "pyproject.toml",
]

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


def run_nodes_batch(repo: Path, nodes: list[str], timeout_sec: int = 300) -> dict[str, dict[str, Any]]:
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
            timeout=timeout_sec,
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
        return {node: {"status": "failed", "duration": timeout_sec * 1000, "message": f"Execution timed out after {timeout_sec}s"} for node in nodes}
    except Exception as exc:
        return {node: {"status": "failed", "duration": 0, "message": f"Execution failed: {exc}"} for node in nodes}
    finally:
        try:
            os.remove(out_json)
        except OSError:
            pass


# ---------------------------------------------------------------------------
# Explicit Build Handlers
# ---------------------------------------------------------------------------

def check_config_schema(repo: Path, config: dict[str, Any], apply_failed: bool) -> tuple[bool, str]:
    required_sections = ["p2p", "f2p", "build", "cheating"]
    for sec in required_sections:
        val = config.get(sec)
        if not isinstance(val, list) or len(val) == 0:
            return False, f"Section '{sec}' is missing or empty"

    p2p_nodes = [str(n) for n in config.get("p2p", [])]
    if len(p2p_nodes) < 30:
        return False, f"P2P count ({len(p2p_nodes)}) is less than mandatory 30"

    f2p_nodes = [str(n) for n in config.get("f2p", [])]
    if len(f2p_nodes) < 5:
        return False, f"F2P count ({len(f2p_nodes)}) is less than mandatory 5"

    for sec in required_sections:
        nodes = config[sec]
        if len(nodes) != len(set(nodes)):
            return False, f"Duplicate test node IDs detected in '{sec}'"

    # Registration integrity: No overlap between F2P and P2P sets
    f2p_set = set(f2p_nodes)
    p2p_set = set(p2p_nodes)
    overlap = f2p_set.intersection(p2p_set)
    if overlap:
        return False, f"Cross-group duplicate test node IDs between F2P and P2P: {sorted(list(overlap))}"

    # Registration integrity: Read p2p_select.txt, require original nodes verbatim and exactly once
    p2p_select_file = Path(__file__).parent / "p2p_select.txt"
    raw_p2p_nodes: list[str] = []
    if p2p_select_file.exists():
        raw_p2p_nodes = [
            line.strip() for line in p2p_select_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]
        for base_node in raw_p2p_nodes:
            count = p2p_nodes.count(base_node)
            if count != 1:
                return False, f"Baseline P2P node '{base_node}' must appear verbatim and exactly once in config.p2p (found {count})"

    # Registration integrity: Require node format to be concrete test functions, not just modules
    for node in f2p_nodes + p2p_nodes:
        if "::" not in node or not node.split("::")[-1].startswith("test_"):
            return False, f"Node '{node}' must specify a concrete test function (e.g. tests/...::test_func), not just a test module"

    # Registration integrity: Verify newly added nodes come from test patch
    test_patch_file = Path(__file__).parent / "test.patch"
    if test_patch_file.exists():
        patch_text = test_patch_file.read_text(encoding="utf-8", errors="ignore")
        baseline_set = set(raw_p2p_nodes)
        for node in f2p_nodes + p2p_nodes:
            if node not in baseline_set:
                func_name = node.split("::")[-1]
                if f"def {func_name}(" not in patch_text:
                    return False, f"Newly registered test node '{node}' is not defined in test.patch"

    # Registration integrity: Run pytest --collect-only to confirm every registered node exists
    if not apply_failed and repo.exists():
        env = os.environ.copy()
        repo_str = str(repo.resolve())
        tests_str = str((repo / "tests").resolve())
        env["PYTHONPATH"] = f"{repo_str}{os.pathsep}{tests_str}{os.pathsep}{env.get('PYTHONPATH', '')}"
        try:
            res = subprocess.run(
                [sys.executable, "-m", "pytest", "--collect-only", "-q"],
                cwd=str(repo),
                env=env,
                capture_output=True,
                text=True,
                timeout=60,
            )
            collected_nodes = set()
            for line in res.stdout.splitlines():
                line = line.strip().replace("\\", "/")
                if line.startswith("./"):
                    line = line[2:]
                if "::" in line:
                    collected_nodes.add(line)
            for node in f2p_nodes + p2p_nodes:
                if node not in collected_nodes:
                    return False, f"Registered test node does not exist in pytest collection: {node}"
        except subprocess.TimeoutExpired:
            return False, "pytest --collect-only execution timed out"
        except Exception as exc:
            return False, f"pytest --collect-only execution failed: {exc}"

    cheating_nodes = config.get("cheating", [])
    hard_gate_cheat_nodes = config.get("hard_gate", {}).get("cheat_nodes", [])
    if set(cheating_nodes) != set(hard_gate_cheat_nodes):
        return False, "config.cheating and hard_gate.cheat_nodes must be identical"

    if config.get("hard_gate", {}).get("p2p_requires_all") is not True:
        return False, "hard_gate.p2p_requires_all must be True"
    if config.get("missing_is_failure") is not True:
        return False, "missing_is_failure must be True"
    if config.get("skip_is_failure") is not True:
        return False, "skip_is_failure must be True"
    if config.get("duplicate_is_failure") is not True:
        return False, "duplicate_is_failure must be True"

    return True, ""


def check_patch_apply(repo: Path, config: dict[str, Any], apply_failed: bool) -> tuple[bool, str]:
    if apply_failed:
        return False, "Candidate patch application failed"
    return True, ""


def check_syntax_compile(repo: Path, config: dict[str, Any], apply_failed: bool) -> tuple[bool, str]:
    targets: list[Path] = []
    pkg_dir = repo / "stackprinter"
    if pkg_dir.exists():
        targets.extend(pkg_dir.rglob("*.py"))

    compile_paths = config.get("hard_gate", {}).get("compile_paths", [])
    for cp in compile_paths:
        p = repo / cp
        if p.is_file() and p not in targets:
            targets.append(p)

    tests_dir = repo / "tests"
    if tests_dir.exists():
        targets.extend(tests_dir.rglob("*.py"))

    for target in targets:
        try:
            py_compile.compile(str(target), doraise=True)
        except Exception as exc:
            return False, f"Syntax compilation failed for {target}: {exc}"

    return True, ""


def check_package_import(repo: Path, config: dict[str, Any], apply_failed: bool) -> tuple[bool, str]:
    if apply_failed:
        return False, "Candidate patch application failed"

    env = os.environ.copy()
    repo_str = str(repo.resolve())
    env["PYTHONPATH"] = f"{repo_str}{os.pathsep}{env.get('PYTHONPATH', '')}"

    import_check_code = (
        "import stackprinter; "
        "assert hasattr(stackprinter, 'format'); "
        "assert hasattr(stackprinter, 'show'); "
    )

    try:
        res = subprocess.run(
            [
                sys.executable,
                "-c",
                import_check_code,
            ],
            cwd=str(repo),
            env=env,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if res.returncode != 0:
            err = res.stderr or res.stdout
            return False, f"Package import check failed: {err.strip()}"
    except subprocess.TimeoutExpired:
        return False, "Import check timed out"
    except Exception as exc:
        return False, f"Import check error: {exc}"

    return True, ""


def check_dependencies(repo: Path, config: dict[str, Any], apply_failed: bool) -> tuple[bool, str]:
    try:
        res = subprocess.run(
            [
                sys.executable,
                "-c",
                "import pytest; import sys; assert sys.version_info >= (3, 8)",
            ],
            cwd=str(repo),
            capture_output=True,
            timeout=30,
        )
        if res.returncode != 0:
            return False, f"Dependency check failed: {res.stderr.decode('utf-8', errors='ignore')}"
    except subprocess.TimeoutExpired:
        return False, "Dependency check timed out"
    except Exception as exc:
        return False, f"Dependency check error: {exc}"

    return True, ""


BUILD_HANDLERS: dict[str, Callable[[Path, dict[str, Any], bool], tuple[bool, str]]] = {
    "build::config_schema_valid": check_config_schema,
    "build::candidate_patch_apply": check_patch_apply,
    "build::python_syntax_compile": check_syntax_compile,
    "build::package_import": check_package_import,
    "build::dependency_check": check_dependencies,
}


# ---------------------------------------------------------------------------
# Explicit Cheating Handlers
# ---------------------------------------------------------------------------

def check_patch_tampering(repo: Path, config: dict[str, Any]) -> tuple[bool, str]:
    # 1. Check baseline protected test files hash integrity
    for rel_path, expected_hash in BASELINE_PROTECTED_HASHES.items():
        file_path = repo / rel_path
        if not file_path.exists():
            return False, f"Protected file missing: {rel_path}"
        try:
            content = file_path.read_bytes().replace(b"\r\n", b"\n")
            actual_hash = hashlib.sha256(content).hexdigest()
            if actual_hash != expected_hash:
                return False, f"Protected test file modified or tampered: {rel_path}"
        except Exception as exc:
            return False, f"Error reading protected file {rel_path}: {exc}"

    # 2. Check for prohibited root-level injection files
    for prohibited in PROHIBITED_ROOT_FILES:
        if (repo / prohibited).exists():
            return False, f"Prohibited injection file found in repository root: {prohibited}"

    for pth in repo.glob("*.pth"):
        return False, f"Prohibited .pth injection file found: {pth.name}"

    # 3. Check model.patch if present
    model_patch = Path("/logs/artifacts/model.patch")
    if model_patch.exists():
        try:
            patch_text = model_patch.read_text(encoding="utf-8", errors="ignore")
            for rel_path in BASELINE_PROTECTED_HASHES:
                if f"diff --git a/{rel_path}" in patch_text or f"+++ b/{rel_path}" in patch_text:
                    return False, f"Candidate patch illegally modifies protected file: {rel_path}"
            for prohibited in PROHIBITED_ROOT_FILES:
                if f"diff --git a/{prohibited}" in patch_text or f"+++ b/{prohibited}" in patch_text:
                    return False, f"Candidate patch illegally introduces root injection file: {prohibited}"
        except Exception as exc:
            return False, f"Error inspecting candidate patch: {exc}"

    return True, ""


def check_eval_bypass(repo: Path, config: dict[str, Any]) -> tuple[bool, str]:
    pkg_dir = repo / "stackprinter"
    if not pkg_dir.exists():
        return False, "Package directory stackprinter does not exist"

    bypass_patterns = [
        re.compile(r"sys\.modules\s*\[\s*['\"]pytest['\"]\s*\]"),
        re.compile(r"pytest_runtest_logreport"),
        re.compile(r"pytest\.main"),
        re.compile(r"\bimport\s+pytest\b"),
        re.compile(r"\bfrom\s+pytest\b"),
    ]

    for py_file in pkg_dir.rglob("*.py"):
        try:
            text = py_file.read_text(encoding="utf-8", errors="ignore")
            for pat in bypass_patterns:
                if pat.search(text):
                    return False, f"Suspicious evaluation bypass pattern found in {py_file.name}: {pat.pattern}"
        except Exception as exc:
            return False, f"Error reading {py_file}: {exc}"

    return True, ""


def check_data_leak(repo: Path, config: dict[str, Any]) -> tuple[bool, str]:
    pkg_dir = repo / "stackprinter"
    if not pkg_dir.exists():
        return False, "Package directory stackprinter does not exist"

    leak_patterns = [
        re.compile(r"__DEEPSWE_CHEATING__"),
        re.compile(r"__VERIFIER_BACKDOOR__"),
        re.compile(r"p2p_select"),
        re.compile(r"\bverifier\.py\b"),
        re.compile(r"\bgrader\.py\b"),
        re.compile(r"\bctrf\b\s*(plugin|report)", re.IGNORECASE),
        re.compile(r"test_refactor_compatibility"),
        re.compile(r"test_refactor_features"),
        re.compile(r"/logs/artifacts"),
    ]

    for py_file in pkg_dir.rglob("*.py"):
        try:
            text = py_file.read_text(encoding="utf-8", errors="ignore")
            for pat in leak_patterns:
                if pat.search(text):
                    return False, f"Data leak or backdoor pattern detected in {py_file.name}: {pat.pattern}"
        except Exception as exc:
            return False, f"Error reading {py_file}: {exc}"

    return True, ""


CHEATING_HANDLERS: dict[str, Callable[[Path, dict[str, Any]], tuple[bool, str]]] = {
    "cheating::test_patch_tampering": check_patch_tampering,
    "cheating::eval_bypass_mock": check_eval_bypass,
    "cheating::data_leak_check": check_data_leak,
}


# ---------------------------------------------------------------------------
# Main Driver
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic Hard Gate Verifier")
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args()

    config = read_json(args.config)
    apply_failed = bool(args.apply_failed)

    build_nodes = [str(n) for n in config.get("build", [])]
    cheating_nodes = [str(n) for n in config.get("cheating", [])]
    p2p_nodes = [str(n) for n in config.get("p2p", [])]

    failed_nodes: list[str] = []
    cheat_failed = False

    # 1. Build Checks (Explicit mapping only; unknown nodes fail immediately)
    build_results: dict[str, str] = {}
    build_messages: dict[str, str] = {}
    if not build_nodes:
        failed_nodes.append("build::empty_registration")
        build_messages["build::empty_registration"] = "No build verification nodes registered"
    for node in build_nodes:
        handler = BUILD_HANDLERS.get(node)
        if handler is None:
            build_results[node] = "failed"
            msg = f"Unknown build node: {node}"
            build_messages[node] = msg
            failed_nodes.append(node)
        else:
            ok, msg = handler(args.repo, config, apply_failed)
            build_results[node] = "passed" if ok else "failed"
            if not ok:
                build_messages[node] = msg
                failed_nodes.append(node)

    # 2. Cheating Checks (Explicit mapping only; unknown nodes fail immediately)
    cheating_results: dict[str, str] = {}
    cheating_messages: dict[str, str] = {}
    if not cheating_nodes:
        failed_nodes.append("cheating::empty_registration")
        cheating_messages["cheating::empty_registration"] = "No cheating verification nodes registered"
        cheat_failed = True
    for node in cheating_nodes:
        handler = CHEATING_HANDLERS.get(node)
        if handler is None:
            cheating_results[node] = "failed"
            msg = f"Unknown cheating node: {node}"
            cheating_messages[node] = msg
            failed_nodes.append(node)
            cheat_failed = True
        else:
            ok, msg = handler(args.repo, config)
            cheating_results[node] = "passed" if ok else "failed"
            if not ok:
                cheating_messages[node] = msg
                failed_nodes.append(node)
                cheat_failed = True

    # 3. P2P Checks (Atomic function test nodes)
    p2p_results: dict[str, str] = {}
    p2p_messages: dict[str, str] = {}
    outcomes: dict[str, dict[str, Any]] = {}
    if not p2p_nodes:
        failed_nodes.append("p2p::empty_registration")
        p2p_messages["p2p::empty_registration"] = "No P2P verification nodes registered"
    elif apply_failed:
        for node in p2p_nodes:
            p2p_results[node] = "failed"
            p2p_messages[node] = "Candidate patch failed to apply"
    else:
        outcomes = run_nodes_batch(args.repo, p2p_nodes, timeout_sec=300)
        for node in p2p_nodes:
            rec = outcomes.get(node, {})
            status = rec.get("status", "failed")
            p2p_results[node] = status
            if status != "passed":
                failed_nodes.append(node)
                p2p_messages[node] = rec.get("message", "P2P node did not pass")

    passed = len(failed_nodes) == 0 and not apply_failed

    configured_penalty = config.get("hard_gate", {}).get("cheat_penalty", -1.0)
    cheat_penalty = configured_penalty if cheat_failed else 0.0

    compile_paths = config.get("hard_gate", {}).get("compile_paths", [])
    failure_reasons = {**build_messages, **cheating_messages, **p2p_messages}

    result = {
        "passed": passed,
        "apply_failed": apply_failed,
        "compile_paths": compile_paths,
        "failed_nodes": sorted(list(set(failed_nodes))),
        "failure_reasons": failure_reasons,
        "cheat_penalty": cheat_penalty,
        "build_results": build_results,
        "build_messages": build_messages,
        "cheating_results": cheating_results,
        "cheating_messages": cheating_messages,
        "p2p_results": p2p_results,
        "p2p_messages": p2p_messages,
        "p2p_outcomes": outcomes if not apply_failed and p2p_nodes else {},
    }

    write_json(args.output, result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
