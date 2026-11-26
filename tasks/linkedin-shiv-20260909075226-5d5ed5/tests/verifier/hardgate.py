#!/usr/bin/env python3
"""Compile, integrity, candidate scope, test protection, anti-cheat, and P2P regression hard gates."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple


EXPECTED_CONFIG_SHA256 = "6a321af6a0a58a6ff6a090c30f89f65e389bbcf72516723f86cee9dc4046536a"


def check_config_integrity(config_path: Path, expected_digest: str = EXPECTED_CONFIG_SHA256) -> List[str]:
    """Fail before executing nodes if config, patch, or selection assets diverge."""
    try:
        raw = config_path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected_digest:
            return ["config_sha256_mismatch"]
        config = json.loads(raw)
        verifier_dir = config_path.parent / "verifier"
        integrity = config["integrity"]
        errors = []
        for filename, key in [("test.patch", "test_patch_sha256"),
                              ("p2p_select.txt", "p2p_select_sha256")]:
            if hashlib.sha256((verifier_dir / filename).read_bytes()).hexdigest() != integrity[key]:
                errors.append(key + "_mismatch")
        expected_selection = "".join(node + "\n" for node in config["p2p"]).encode()
        if (verifier_dir / "p2p_select.txt").read_bytes() != expected_selection:
            errors.append("p2p_selection_mismatch")
        nodes = config["f2p"] + config["p2p"]
        if not nodes or len(nodes) != len(set(nodes)):
            errors.append("node_selection_empty_or_duplicate")
        return errors
    except (OSError, ValueError, KeyError, TypeError):
        return ["config_integrity_unreadable"]


# Allowed path prefixes for refactoring candidate modifications
ALLOWED_PREFIXES = [
    "src/shiv/",
]

# Protected files / directories that candidate patches must never touch or tamper with
PROTECTED_PATTERNS = [
    "test/",
    "tests/",
    ".github/",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
]

# Suspicious mock/monkeypatch patterns attempting to tamper with grading or verifier infrastructure
CHEAT_PATTERNS = [
    "mock.patch('grader",
    "mock.patch(\"grader",
    "mock.patch('hardgate",
    "mock.patch(\"hardgate",
    "mock.patch('verifier",
    "mock.patch(\"verifier",
]


def check_compile_validity(repo: Path, compile_paths: List[str]) -> List[str]:
    """Verify syntax and bytecode compilation of required paths."""
    errors: List[str] = []
    for rel_path in compile_paths:
        target = repo / rel_path
        if not target.exists():
            errors.append(f"missing_compile_path:{rel_path}")
            continue
        py_files = [target] if target.is_file() else list(target.rglob("*.py"))
        for py_file in py_files:
            try:
                content = py_file.read_bytes()
                ast.parse(content, filename=str(py_file))
                compile(content, str(py_file), "exec")
            except SyntaxError as e:
                errors.append(f"syntax_error:{py_file.relative_to(repo)}:{e.lineno}:{e.msg}")
            except Exception as e:
                errors.append(f"compile_error:{py_file.relative_to(repo)}:{e}")
    return errors


def _locate_case_test_patch(config_path: Path) -> Path:
    """Locate the Case-controlled test.patch from the configuration location."""
    # Standard locations relative to config.json (e.g. /tests/config.json or case/tests/config.json)
    candidates = [
        config_path.parent / "verifier" / "test.patch",
        config_path.parent / "test.patch",
        Path("/tests/verifier/test.patch"),
    ]
    for cand in candidates:
        if cand.is_file():
            return cand
    raise FileNotFoundError(f"Case-controlled test.patch not found from {config_path}")


def _locate_manifest_and_source(repo: Path, config_path: Path) -> Tuple[Path | None, Path | None]:
    """Locate Case-controlled source-manifest.json and corresponding source directory."""
    candidates = [
        (config_path.parent / "source-manifest.json", config_path.parent / "source"),
        (config_path.parent.parent / "source-manifest.json", config_path.parent.parent / "source"),
        (config_path.parent.parent.parent / "source-manifest.json", config_path.parent.parent.parent / "source"),
        (repo.parent / "source-manifest.json", repo.parent / "source"),
        (Path("/source-manifest.json"), Path("/source")),
        (Path("/tests/source-manifest.json"), Path("/source")),
    ]
    for m_cand, s_cand in candidates:
        if m_cand.is_file() and s_cand.is_dir():
            return m_cand, s_cand
    return None, None


def _materialize_manifest_verified_source(
    manifest_file: Path,
    source_dir: Path,
    target_dir: Path,
) -> List[str]:
    """Verify manifest entries and materialize ONLY manifested files into target_dir."""
    try:
        manifest_data = json.loads(manifest_file.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"manifest_read_error:{exc}"]

    files_meta = manifest_data.get("files", {})
    if not files_meta:
        return ["manifest_files_empty"]

    for rel_path, meta in files_meta.items():
        src_path = source_dir / rel_path
        if not src_path.is_file():
            return [f"manifest_file_missing:{rel_path}"]

        expected_hash = meta.get("sha256") if isinstance(meta, dict) else str(meta)
        actual_hash = hashlib.sha256(src_path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            return [f"manifest_hash_mismatch:{rel_path}:{actual_hash}:{expected_hash}"]

        dest_path = target_dir / rel_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_path, dest_path)

    return []


def derive_dynamic_expected_harness(
    repo: Path,
    config_path: Path,
    base_commit: str | None = None,
) -> Tuple[Dict[str, str], Set[str], List[str], str]:
    """Dynamically derive Expected Harness State by applying Case test.patch to trusted frozen source.

    Returns:
      (expected_harness_hashes, expected_deleted_harness_files, derivation_errors, provenance)
    Fails closed if trusted frozen source or case test.patch cannot be obtained/applied,
    or if the expected harness state is empty.
    """
    errors: List[str] = []
    try:
        patch_file = _locate_case_test_patch(config_path)
    except Exception as exc:
        return {}, set(), [f"locate_test_patch_failed:{exc}"], "none"

    # Create a disposable temporary environment to materialize the trusted base + test.patch
    with tempfile.TemporaryDirectory() as td:
        tmp_base = Path(td) / "trusted_base"
        tmp_base.mkdir(parents=True, exist_ok=True)

        extracted = False
        provenance = "none"

        # Trust Source A: Exact Frozen Commit
        if base_commit and (repo / ".git").exists():
            check_proc = subprocess.run(
                ["git", "cat-file", "-e", f"{base_commit}^{{commit}}"],
                cwd=repo,
                capture_output=True,
            )
            if check_proc.returncode == 0:
                cmd = f"git archive {base_commit} | tar -x -C \"{tmp_base}\""
                proc = subprocess.run(cmd, shell=True, cwd=repo, capture_output=True)
                if proc.returncode == 0 and (tmp_base / "src").is_dir():
                    extracted = True
                    provenance = "exact_frozen_commit"

        # Trust Source B: Manifest-verified Source Snapshot
        if not extracted:
            manifest_file, source_dir = _locate_manifest_and_source(repo, config_path)
            if manifest_file and source_dir:
                mat_errors = _materialize_manifest_verified_source(manifest_file, source_dir, tmp_base)
                if mat_errors:
                    errors.extend(mat_errors)
                elif (tmp_base / "src").is_dir():
                    extracted = True
                    provenance = "manifest_verified_snapshot"

        if not extracted:
            if not errors:
                errors.append("trusted_frozen_source_unavailable")
            return {}, set(), errors, provenance

        # Snapshot baseline state of test assets before test.patch
        base_test_hashes: Dict[str, str] = {}
        for p in tmp_base.rglob("*"):
            if p.is_file():
                rel = str(p.relative_to(tmp_base))
                if rel.startswith("test/") or rel.startswith("tests/"):
                    base_test_hashes[rel] = hashlib.sha256(p.read_bytes()).hexdigest()

        # Apply Case-controlled test.patch onto the trusted base
        proc_apply = subprocess.run(
            ["git", "apply", "--whitespace=nowarn", str(patch_file)],
            cwd=tmp_base,
            capture_output=True,
            text=True,
        )
        if proc_apply.returncode != 0:
            proc_patch = subprocess.run(
                ["patch", "-p1"],
                input=patch_file.read_text(encoding="utf-8"),
                cwd=tmp_base,
                capture_output=True,
                text=True,
            )
            if proc_patch.returncode != 0:
                return {}, set(), [f"test_patch_apply_on_frozen_base_failed:{proc_apply.stderr or proc_patch.stderr}"], provenance

        # Snapshot post-patch state of test assets
        post_test_hashes: Dict[str, str] = {}
        for p in tmp_base.rglob("*"):
            if p.is_file():
                rel = str(p.relative_to(tmp_base))
                if rel.startswith("test/") or rel.startswith("tests/"):
                    post_test_hashes[rel] = hashlib.sha256(p.read_bytes()).hexdigest()

        # Derive expected harness deltas (files newly added or modified by test.patch)
        expected_harness: Dict[str, str] = {}
        for rel, post_h in post_test_hashes.items():
            if rel not in base_test_hashes or base_test_hashes[rel] != post_h:
                expected_harness[rel] = post_h

        # Deleted by test.patch if any
        expected_deleted: Set[str] = set(base_test_hashes.keys()) - set(post_test_hashes.keys())

        # S9-REBLOCK-005: Fail closed if expected harness deltas and deletions are both empty
        if not expected_harness and not expected_deleted:
            return {}, set(), ["empty_expected_harness_state"], provenance

        return expected_harness, expected_deleted, [], provenance


def _get_raw_changed_files(repo: Path) -> List[str]:
    """Get all changed/added/deleted/untracked files relative to repo root using git status/diff."""
    changed: Set[str] = set()
    try:
        proc = subprocess.run(
            ["git", "status", "--porcelain", "-uall"],
            cwd=repo,
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            for line in proc.stdout.splitlines():
                line = line.strip()
                if not line:
                    continue
                parts = line.split(maxsplit=1)
                if len(parts) == 2 and len(parts[0]) <= 2:
                    target_path = parts[1].strip()
                    if " -> " in target_path:
                        old_p, new_p = target_path.split(" -> ", 1)
                        changed.add(old_p.strip())
                        changed.add(new_p.strip())
                    else:
                        changed.add(target_path)
                else:
                    changed.add(line)

        proc_diff = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            cwd=repo,
            capture_output=True,
            text=True,
        )
        if proc_diff.returncode == 0:
            for line in proc_diff.stdout.splitlines():
                if line.strip():
                    changed.add(line.strip())
    except Exception:
        pass
    return sorted(changed)


def get_candidate_delta_files(
    repo: Path,
    expected_harness: Dict[str, str],
    expected_deleted: Set[str],
) -> Tuple[List[str], List[str]]:
    """Separate Candidate Delta from Trusted Test Harness State.

    Returns (candidate_delta_files, harness_errors).
    Fails if any expected test harness asset is missing, deleted, or altered by candidate.
    """
    raw_changed = _get_raw_changed_files(repo)
    candidate_delta: List[str] = []
    harness_errors: List[str] = []

    # 1. Verify integrity of all dynamically derived harness files in candidate repo
    for rel_harness, expected_hash in expected_harness.items():
        harness_path = repo / rel_harness
        if not harness_path.exists():
            harness_errors.append(f"trusted_harness_deleted_or_missing:{rel_harness}")
        else:
            actual_hash = hashlib.sha256(harness_path.read_bytes()).hexdigest()
            if actual_hash != expected_hash:
                harness_errors.append(f"trusted_harness_tampered:{rel_harness}")

    # 2. Filter raw changed files to determine the true Candidate Delta
    for changed in raw_changed:
        if changed in expected_harness:
            harness_path = repo / changed
            if not harness_path.exists():
                candidate_delta.append(changed)
            else:
                actual_hash = hashlib.sha256(harness_path.read_bytes()).hexdigest()
                if actual_hash != expected_harness[changed]:
                    candidate_delta.append(changed)
        elif changed in expected_deleted:
            # Expected deletion by test.patch
            continue
        else:
            candidate_delta.append(changed)

    return sorted(set(candidate_delta)), harness_errors


def check_candidate_scope(candidate_delta: List[str]) -> List[str]:
    """Enforce ALLOWED_PREFIXES on Candidate Delta."""
    errors: List[str] = []
    for changed in candidate_delta:
        if not any(changed.startswith(allowed) for allowed in ALLOWED_PREFIXES):
            errors.append(f"candidate_scope_violation:{changed}")
    return errors


def check_protected_assets(candidate_delta: List[str]) -> Tuple[List[str], List[str]]:
    """Verify Candidate Delta does not alter protected repository assets or test trees."""
    errors: List[str] = []
    protected_changes: List[str] = []
    for changed in candidate_delta:
        for prot in PROTECTED_PATTERNS:
            if changed == prot or changed.startswith(prot):
                errors.append(f"protected_asset_modified:{changed}")
                protected_changes.append(changed)
                break
    return errors, protected_changes


def _extract_ast_skips(py_path: Path) -> List[str]:
    """Extract actual executable pytest skip/skipif/xfail decorator or call markers from an AST."""
    skips: List[str] = []
    try:
        tree = ast.parse(py_path.read_bytes(), filename=str(py_path))
    except Exception:
        return skips

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            for deco in node.decorator_list:
                deco_str = ast.unparse(deco)
                if any(m in deco_str for m in ("pytest.mark.skip", "pytest.mark.skipif", "pytest.mark.xfail")):
                    skips.append(f"{node.name}:{deco_str}")
        elif isinstance(node, ast.Call):
            call_str = ast.unparse(node)
            if any(call_str.startswith(m) for m in ("pytest.skip", "pytest.xfail")):
                skips.append(call_str)

    return skips


def check_tests_not_bypassed(repo: Path, candidate_delta: List[str]) -> Tuple[List[str], List[str]]:
    """Detect candidate-introduced test bypasses in Candidate Delta (modified, added, or untracked test files)."""
    errors: List[str] = []
    bypass_details: List[str] = []

    for changed in candidate_delta:
        if changed in ("setup.cfg", "pyproject.toml", "tox.ini"):
            cfg_path = repo / changed
            if cfg_path.exists():
                try:
                    proc = subprocess.run(
                        ["git", "diff", "HEAD", "--", changed],
                        cwd=repo,
                        capture_output=True,
                        text=True,
                    )
                    if proc.returncode == 0 and proc.stdout.strip():
                        msg = f"test_config_modified:{changed}"
                        errors.append(msg)
                        bypass_details.append(msg)
                except Exception:
                    pass

        if changed.startswith("test/") or changed.startswith("tests/"):
            test_file = repo / changed
            if not test_file.exists():
                msg = f"candidate_deleted_test_file:{changed}"
                errors.append(msg)
                bypass_details.append(msg)
                continue

            if test_file.suffix == ".py":
                current_skips = _extract_ast_skips(test_file)
                if not current_skips:
                    continue

                baseline_skips: List[str] = []
                try:
                    proc = subprocess.run(
                        ["git", "show", f"HEAD:{changed}"],
                        cwd=repo,
                        capture_output=True,
                        text=True,
                    )
                    if proc.returncode == 0 and proc.stdout:
                        baseline_tree = ast.parse(proc.stdout, filename=f"HEAD:{changed}")
                        for node in ast.walk(baseline_tree):
                            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                                for deco in node.decorator_list:
                                    d_str = ast.unparse(deco)
                                    if any(m in d_str for m in ("pytest.mark.skip", "pytest.mark.skipif", "pytest.mark.xfail")):
                                        baseline_skips.append(f"{node.name}:{d_str}")
                            elif isinstance(node, ast.Call):
                                c_str = ast.unparse(node)
                                if any(c_str.startswith(m) for m in ("pytest.skip", "pytest.xfail")):
                                    baseline_skips.append(c_str)
                except Exception:
                    pass

                for s in current_skips:
                    if s not in baseline_skips:
                        msg = f"candidate_introduced_test_skip:{changed}:{s}"
                        errors.append(msg)
                        bypass_details.append(msg)

    return errors, bypass_details


def check_anti_cheat(repo: Path) -> List[str]:
    """Check for suspicious test bypass or grading tampering keywords."""
    cheat_flags: List[str] = []
    for py_file in (repo / "src").rglob("*.py"):
        try:
            text = py_file.read_text(encoding="utf-8")
            for pattern in CHEAT_PATTERNS:
                if pattern in text:
                    cheat_flags.append(f"cheat_pattern_found:{py_file.relative_to(repo)}:{pattern}")
        except Exception:
            pass
    return cheat_flags


def run_p2p_tests(repo: Path, config: dict[str, Any]) -> Tuple[bool, List[str], dict[str, Any]]:
    """Run exact configured P2P test node IDs using pytest."""
    p2p_nodes = config.get("p2p", [])
    if not p2p_nodes:
        return True, [], {}

    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "-q",
        "--tb=short",
        "--import-mode=importlib",
    ]
    cmd.extend(str(node) for node in p2p_nodes)

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
        )
    except Exception as e:
        return False, [f"pytest_execution_error:{e}"], {}

    failed_nodes: List[str] = []
    details: dict[str, Any] = {
        "returncode": proc.returncode,
        "nodes_count": len(p2p_nodes),
        "stdout": proc.stdout[-2000:] if len(proc.stdout) > 2000 else proc.stdout,
        "stderr": proc.stderr[-2000:] if len(proc.stderr) > 2000 else proc.stderr,
    }

    if proc.returncode != 0:
        for line in proc.stdout.splitlines():
            if line.startswith("FAILED "):
                failed_node = line.split()[1]
                failed_nodes.append(failed_node)

    return len(failed_nodes) == 0 and proc.returncode == 0, failed_nodes, details


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    parser.add_argument("--run-p2p", action="store_true", default=False,
                        help="Run P2P regression suite directly in hardgate")
    args = parser.parse_args()

    integrity_errors = check_config_integrity(args.config)
    if integrity_errors:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps({
            "passed": False, "success": False, "status": "FAIL",
            "infrastructure_error": False, "failed_nodes": integrity_errors,
            "details": {"config_integrity": integrity_errors},
        }, indent=2) + "\n", encoding="utf-8")
        return 0

    config = json.loads(args.config.read_text(encoding="utf-8"))
    hard_gate_cfg = config.get("hard_gate", {})
    compile_paths = hard_gate_cfg.get("compile_paths", ["src/shiv"])
    cheat_penalty = hard_gate_cfg.get("cheat_penalty", -1.0)
    base_commit = config.get("base_commit")

    failed_reasons: List[str] = []

    # 1. Apply validity check
    if bool(args.apply_failed):
        failed_reasons.append("candidate_patch_apply_failed")

    # 2. Syntax & bytecode compilation validity check
    compile_errors = check_compile_validity(args.repo, compile_paths)
    if compile_errors:
        failed_reasons.extend(compile_errors)

    # 3. Dynamically derive Expected Harness State from Case test.patch on trusted base (Fail Closed)
    expected_harness, expected_deleted, derivation_errors, provenance = derive_dynamic_expected_harness(
        args.repo, args.config, base_commit=base_commit
    )
    if derivation_errors:
        failed_reasons.extend(derivation_errors)

    # 4. Identify Candidate Delta and verify Dynamic Trusted Harness State
    candidate_delta: List[str] = []
    harness_errors: List[str] = []
    if not derivation_errors:
        candidate_delta, harness_errors = get_candidate_delta_files(
            args.repo, expected_harness, expected_deleted
        )
        if harness_errors:
            failed_reasons.extend(harness_errors)

    # 5. Candidate scope check (enforcing ALLOWED_PREFIXES on Candidate Delta)
    scope_errors = check_candidate_scope(candidate_delta)
    if scope_errors:
        failed_reasons.extend(scope_errors)

    # 6. Protected asset check (protecting test/, tests/, .github/, etc. against candidate delta)
    protected_errors, protected_changes = check_protected_assets(candidate_delta)
    if protected_errors:
        failed_reasons.extend(protected_errors)

    # 7. Tests not bypassed check (skip/xfail additions, test configuration tampering)
    bypass_errors, bypass_details = check_tests_not_bypassed(args.repo, candidate_delta)
    if bypass_errors:
        failed_reasons.extend(bypass_errors)

    # 8. Anti-cheat check
    cheat_errors = check_anti_cheat(args.repo)
    if cheat_errors:
        failed_reasons.extend(cheat_errors)

    # 9. P2P tests execution (if --run-p2p requested)
    p2p_details: dict[str, Any] = {}
    if args.run_p2p and not failed_reasons:
        p2p_ok, p2p_failed_nodes, p2p_details = run_p2p_tests(args.repo, config)
        if not p2p_ok:
            failed_reasons.extend(p2p_failed_nodes or ["p2p_suite_failed"])

    passed = len(failed_reasons) == 0
    result = {
        "passed": passed,
        "success": passed,
        "compile_passed": not compile_errors,
        "scope_violation": bool(scope_errors or protected_errors),
        "cheating_detected": bool(cheat_errors or bypass_errors or harness_errors),
        "infrastructure_error": bool(derivation_errors),
        "apply_failed": bool(args.apply_failed),
        "compile_paths": compile_paths,
        "failed_nodes": failed_reasons,
        "cheat_penalty": cheat_penalty if not passed else 0.0,
        "details": {
            "compile_errors": compile_errors,
            "expected_harness": expected_harness,
            "derivation_errors": derivation_errors,
            "candidate_delta": candidate_delta,
            "harness_errors": harness_errors,
            "candidate_scope_valid": {
                "passed": len(scope_errors) == 0,
                "changed_paths": candidate_delta,
                "violations": scope_errors,
            },
            "protected_assets_unchanged": {
                "passed": len(protected_errors) == 0,
                "protected_changes": protected_changes,
            },
            "tests_not_bypassed": {
                "passed": len(bypass_errors) == 0,
                "details": bypass_details,
            },
            "cheat_errors": cheat_errors,
            "p2p": p2p_details,
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
