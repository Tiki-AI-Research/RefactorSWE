#!/usr/bin/env python3
"""Deterministic Hard Gate: Build, Anti-Cheat, and atomic P2P verification.

Detects critical defects in candidate data after model refactoring:
1. Build Test: Parsable, executable, reproducible conditions (syntax, types, go.mod, go build).
2. Anti-Cheat Test: Detects test neutralization, evaluation bypass, unauthorized files, and provenance tampering.
3. P2P Test: Verifies consistency of task semantics, input-output relations, and core constraints.
   Enforces atomicity (1 check = 1 test node, >= 30 nodes, original baseline test integrity).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def run_cmd(
    cmd: list[str],
    cwd: Path,
    timeout: int = 300,
    check: bool = False,
) -> subprocess.CompletedProcess[str]:
    """Helper to run a subprocess command safely."""
    return subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=check,
    )


def check_build(
    repo: Path,
    config: dict[str, Any],
    apply_failed: bool,
    timeout: int = 300,
) -> tuple[bool, list[str], dict[str, Any]]:
    """Category 1: Build Test.

    Verify basic parsable, executable, and reproducible conditions:
    - Candidate patch apply status
    - go.mod / go.sum integrity and dependency verification
    - Source code syntax and static analysis (go vet)
    - Full package compilation (go build)
    """
    failed_nodes: list[str] = []
    details: dict[str, Any] = {}

    # 1.1 Candidate patch application
    if apply_failed:
        failed_nodes.append("candidate_patch_apply")
        details["patch_apply"] = "Candidate patch failed to apply or was missing."
        return False, failed_nodes, details
    details["patch_apply"] = "ok"

    # 1.2 Explicit dependencies & module integrity
    go_mod = repo / "go.mod"
    go_sum = repo / "go.sum"
    if not go_mod.exists():
        failed_nodes.append("build_missing_go_mod")
        details["go_mod"] = "go.mod file not found"
    else:
        details["go_mod"] = "ok"

    if not go_sum.exists():
        failed_nodes.append("build_missing_go_sum")
        details["go_sum"] = "go.sum file not found"
    else:
        details["go_sum"] = "ok"

    if not failed_nodes:
        try:
            mod_verify = run_cmd(["go", "mod", "verify"], cwd=repo, timeout=timeout)
            if mod_verify.returncode != 0:
                failed_nodes.append("build_mod_verify_failure")
                details["mod_verify"] = {
                    "returncode": mod_verify.returncode,
                    "stderr": mod_verify.stderr.strip()[:1000],
                }
            else:
                details["mod_verify"] = "ok"
        except Exception as e:
            failed_nodes.append(f"build_mod_verify_exception: {e}")
            details["mod_verify"] = str(e)

    # 1.3 Static syntax analysis (go vet)
    if not failed_nodes:
        try:
            vet_proc = run_cmd(["go", "vet", "./..."], cwd=repo, timeout=timeout)
            if vet_proc.returncode != 0:
                failed_nodes.append("build_vet_failure")
                details["go_vet"] = {
                    "returncode": vet_proc.returncode,
                    "stderr": vet_proc.stderr.strip()[:1000],
                }
            else:
                details["go_vet"] = "ok"
        except Exception as e:
            failed_nodes.append(f"build_vet_exception: {e}")
            details["go_vet"] = str(e)

    # 1.4 Package compilation and executability (go build)
    if not failed_nodes:
        hard_gate_cfg = config.get("hard_gate", {})
        compile_paths = hard_gate_cfg.get("compile_paths", [])
        build_targets = compile_paths if compile_paths else ["./..."]
        try:
            build_proc = run_cmd(["go", "build", *build_targets], cwd=repo, timeout=timeout)
            if build_proc.returncode != 0:
                failed_nodes.append("go_build_failure")
                details["go_build"] = {
                    "returncode": build_proc.returncode,
                    "stderr": build_proc.stderr.strip()[:1000],
                    "targets": build_targets,
                }
            else:
                details["go_build"] = "ok"
        except Exception as e:
            failed_nodes.append(f"go_build_exception: {e}")
            details["go_build"] = str(e)

    passed = len(failed_nodes) == 0
    return passed, failed_nodes, details


def verify_and_get_trusted_verifier_files(
    repo: Path,
    verifier_dir: Path,
    manifest_data: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    """Verify evaluator-owned test files against trusted expected content.
    
    Instead of trusting paths blindly, verifies:
    - Expected trusted files match their trusted hashes from freeze_manifest.json
    - Any tampering or modification of evaluator-owned files is detected
    """
    trusted_specs = manifest_data.get("trusted_verifier_files", {})
    failed_nodes: list[str] = []
    verified_files: dict[str, dict[str, Any]] = {}

    if not trusted_specs:
        # Fallback: compute expected hashes from test.patch in verifier_dir
        test_patch = verifier_dir / "test.patch"
        if test_patch.exists():
            try:
                with tempfile.TemporaryDirectory() as tmpdir:
                    subprocess.run(["git", "init"], cwd=tmpdir, check=True, capture_output=True)
                    proc = subprocess.run(
                        ["git", "apply", "--whitespace=nowarn", str(test_patch.resolve())],
                        cwd=tmpdir,
                        capture_output=True,
                    )
                    if proc.returncode == 0:
                        for root, _, files in os.walk(tmpdir):
                            for f in files:
                                if f.endswith(".go"):
                                    full_p = Path(root) / f
                                    rel_p = str(full_p.relative_to(tmpdir))
                                    b = full_p.read_bytes()
                                    trusted_specs[rel_p] = {
                                        "sha256": hashlib.sha256(b).hexdigest(),
                                        "size_bytes": len(b),
                                    }
            except Exception as e:
                failed_nodes.append(f"evaluator_test_verification_error: {e}")

    for rel_path, spec in trusted_specs.items():
        norm_p = os.path.normpath(rel_path)
        expected_sha = spec.get("sha256")
        target_f = repo / norm_p
        if not target_f.exists():
            failed_nodes.append(f"missing_trusted_evaluator_file: {norm_p}")
            continue
        try:
            actual_bytes = target_f.read_bytes()
            actual_sha = hashlib.sha256(actual_bytes).hexdigest()
            if actual_sha != expected_sha:
                failed_nodes.append(f"cheat_evaluator_test_tampered: {norm_p}")
            else:
                verified_files[norm_p] = spec
        except Exception as e:
            failed_nodes.append(f"cheat_evaluator_test_unreadable: {norm_p}: {e}")

    return verified_files, failed_nodes


def resolve_and_verify_baseline(
    repo: Path,
    manifest_data: dict[str, Any],
) -> tuple[str | None, list[str], dict[str, Any]]:
    """Establish exact baseline provenance without unverified fallback.
    
    Required base commit is 697380ffec04290679230d8d04636eb41c99e0a8.
    If the repository contains an alternate snapshot commit, verifies that the snapshot
    matches the trusted complete baseline manifest exactly before accepting it.
    """
    required_base = "697380ffec04290679230d8d04636eb41c99e0a8"
    failed_nodes: list[str] = []
    details: dict[str, Any] = {
        "required_base_commit": required_base,
    }

    # Check if required commit exists directly in repo
    rev_proc = run_cmd(["git", "rev-parse", "--verify", f"{required_base}^{{commit}}"], cwd=repo, timeout=10)
    if rev_proc.returncode == 0:
        details["selected_baseline"] = required_base
        details["provenance_evidence"] = f"Direct commit match: {required_base}"
        return required_base, failed_nodes, details

    # Candidate commit list (e.g. reconstructed snapshot commits)
    rev_list_proc = run_cmd(["git", "rev-list", "--max-parents=0", "HEAD"], cwd=repo, timeout=10)
    candidate_commits = []
    if rev_list_proc.returncode == 0 and rev_list_proc.stdout.strip():
        candidate_commits = [c.strip() for c in rev_list_proc.stdout.splitlines() if c.strip()]

    # Also check base commits from manifest
    if "base_commit" in manifest_data and manifest_data["base_commit"] not in candidate_commits:
        candidate_commits.append(str(manifest_data["base_commit"]))

    baseline_snapshot = manifest_data.get("baseline_snapshot")
    if not baseline_snapshot or "files" not in baseline_snapshot:
        failed_nodes.append("cheat_provenance_unavailable")
        details["provenance_error"] = (
            f"Required base commit {required_base} not found in repo, and no baseline snapshot manifest available to verify alternate commits."
        )
        return None, failed_nodes, details

    expected_files: dict[str, dict[str, Any]] = baseline_snapshot["files"]
    verified_commit: str | None = None

    for cand in candidate_commits:
        chk_proc = run_cmd(["git", "rev-parse", "--verify", f"{cand}^{{commit}}"], cwd=repo, timeout=10)
        if chk_proc.returncode != 0:
            continue
        cand_sha = chk_proc.stdout.strip()
        # Verify commit content against baseline_snapshot
        tree_proc = run_cmd(["git", "ls-tree", "-r", "--name-only", cand_sha], cwd=repo, timeout=30)
        if tree_proc.returncode != 0:
            continue
        cand_files = sorted([f.strip() for f in tree_proc.stdout.splitlines() if f.strip()])
        if sorted(expected_files.keys()) != cand_files:
            continue

        # Verify cryptographic sha256 of all files
        all_matched = True
        for fpath, spec in expected_files.items():
            content_proc = subprocess.run(["git", "show", f"{cand_sha}:{fpath}"], cwd=repo, capture_output=True)
            if content_proc.returncode != 0:
                all_matched = False
                break
            h = hashlib.sha256(content_proc.stdout).hexdigest()
            if h != spec.get("sha256"):
                all_matched = False
                break

        if all_matched:
            verified_commit = cand_sha
            details["selected_baseline"] = cand_sha
            details["provenance_evidence"] = (
                f"Alternate commit {cand_sha} cryptographically verified against {len(expected_files)} trusted baseline snapshot files (base commit {required_base})."
            )
            break

    if not verified_commit:
        failed_nodes.append("cheat_provenance_unavailable")
        details["provenance_error"] = (
            f"Required base commit {required_base} is not available and no repository commit matches trusted baseline snapshot."
        )
        return None, failed_nodes, details

    return verified_commit, failed_nodes, details


def check_anti_cheat(
    repo: Path,
    config: dict[str, Any],
    verifier_dir: Path,
    timeout: int = 60,
) -> tuple[bool, list[str], dict[str, Any]]:
    """Category 2: Anti-Cheat Test.

    Detect cheating or opportunistic behaviors:
    - Tampering with evaluation infrastructure or test frameworks
    - Modifying original repository test files or tampering with evaluator tests
    - Evaluation bypass (checking benchmark environment variables or test harness)
    - Test neutralization (adding skips or build-ignore tags)
    - Suspicious replace directives or local vendor dependency injection in go.mod
    - Reject same-path trusted test impersonation and strictly prohibit candidate test files
    """
    failed_nodes: list[str] = []
    details: dict[str, Any] = {}

    # 2.1 Check go.mod for suspicious replace directives
    go_mod_path = repo / "go.mod"
    if go_mod_path.exists():
        try:
            go_mod_text = go_mod_path.read_text(encoding="utf-8")
            if re.search(r'^\s*replace\s+[^\s=>]+\s*=>\s*(\./|\.\./)', go_mod_text, re.MULTILINE):
                failed_nodes.append("cheat_suspicious_dependency_override")
                details["dependency_override"] = "Suspicious local replace directive found in go.mod."
        except Exception as e:
            details["go_mod_check_err"] = str(e)

    # 2.2 Load manifest
    manifest_path = verifier_dir.parent / "assets" / "freeze_manifest.json"
    manifest_data: dict[str, Any] = {}
    if manifest_path.exists():
        try:
            manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception as e:
            failed_nodes.append("malformed_integrity_metadata")
            details["manifest_error"] = str(e)
            return False, failed_nodes, details

    # 2.3 Establish exact baseline provenance
    base_commit, prov_failed, prov_details = resolve_and_verify_baseline(repo, manifest_data)
    details["provenance"] = prov_details
    if prov_failed or not base_commit:
        failed_nodes.extend(prov_failed)
        return False, failed_nodes, details

    # 2.4 Verify trusted evaluator files against trusted expected contents
    verified_trusted_files, eval_tamper_failed = verify_and_get_trusted_verifier_files(
        repo=repo,
        verifier_dir=verifier_dir,
        manifest_data=manifest_data,
    )
    if eval_tamper_failed:
        failed_nodes.extend(eval_tamper_failed)
        details["evaluator_test_tampering"] = eval_tamper_failed

    # 2.5 Inspect candidate modifications against base commit (committed, staged, unstaged, untracked)
    candidate_files: set[str] = set()
    tampered_tests: list[str] = []
    submitted_test_files: list[str] = []

    # Check for evaluator-injected test impersonation or unauthorized submission:
    # Evaluator injects trusted tests into working tree only; candidate MUST NOT commit or stage them.
    # If candidate committed or staged any trusted verifier file in HEAD or git index, reject immediately.
    for vf in verified_trusted_files:
        head_commit_chk = run_cmd(["git", "cat-file", "-e", f"HEAD:{vf}"], cwd=repo, timeout=10)
        index_chk = run_cmd(["git", "diff", "--name-only", "--cached"], cwd=repo, timeout=10)
        staged_files = [os.path.normpath(f.strip()) for f in index_chk.stdout.splitlines() if f.strip()]
        if head_commit_chk.returncode == 0 or vf in staged_files:
            submitted_test_files.append(vf)
            failed_nodes.append(f"cheat_test_file_submitted: {vf}")

    # Inspect status diffs with rename detection (-M)
    for diff_cmd in [
        ["git", "diff", "--name-status", "-M", f"{base_commit}..HEAD"],
        ["git", "diff", "--name-status", "-M", base_commit],
        ["git", "diff", "--name-status", "-M", "--cached"],
    ]:
        proc = run_cmd(diff_cmd, cwd=repo, timeout=timeout)
        if proc.returncode == 0:
            for line in proc.stdout.splitlines():
                line = line.strip()
                if not line:
                    continue
                parts = line.split("\t")
                status = parts[0]
                if status.startswith("R") or status.startswith("C"):
                    if len(parts) >= 3:
                        old_p = os.path.normpath(parts[1])
                        new_p = os.path.normpath(parts[2])
                        if old_p not in verified_trusted_files:
                            candidate_files.add(old_p)
                        if new_p not in verified_trusted_files:
                            candidate_files.add(new_p)
                        if old_p.endswith("_test.go") and old_p not in verified_trusted_files:
                            if old_p not in tampered_tests:
                                tampered_tests.append(old_p)
                                failed_nodes.append(f"cheat_original_test_modified: {old_p}")
                        if new_p.endswith("_test.go") and new_p not in verified_trusted_files:
                            if new_p not in submitted_test_files:
                                submitted_test_files.append(new_p)
                                failed_nodes.append(f"cheat_test_file_submitted: {new_p}")
                elif status.startswith("D"):
                    if len(parts) >= 2:
                        del_p = os.path.normpath(parts[1])
                        if del_p not in verified_trusted_files:
                            candidate_files.add(del_p)
                            if del_p.endswith("_test.go") and del_p not in tampered_tests:
                                tampered_tests.append(del_p)
                                failed_nodes.append(f"cheat_original_test_modified: {del_p}")
                else:
                    if len(parts) >= 2:
                        p = os.path.normpath(parts[1])
                        if p not in verified_trusted_files:
                            candidate_files.add(p)

    untracked_proc = run_cmd(["git", "ls-files", "--others", "--exclude-standard"], cwd=repo, timeout=timeout)
    if untracked_proc.returncode == 0:
        for f in untracked_proc.stdout.splitlines():
            if f.strip():
                p = os.path.normpath(f.strip())
                if p not in verified_trusted_files:
                    candidate_files.add(p)

    candidate_changed_files = {f for f in candidate_files if f not in verified_trusted_files}

    # 2.6 Infrastructure tampering check
    tampered_infra: list[str] = []
    for f in candidate_changed_files:
        if (
            f.startswith("tests/")
            or f in ("grader.py", "verifier.py", "hardgate.py", "test.sh", "config.json", "task.toml", "p2p_select.txt", "test.patch")
            or f.startswith(".github/")
        ):
            tampered_infra.append(f)

    if tampered_infra:
        for ti in tampered_infra:
            failed_nodes.append(f"cheat_infrastructure_tampering: {ti}")
        details["infrastructure_tampering"] = tampered_infra
    else:
        details["infrastructure_tampering"] = "ok"

    # 2.7 Test file modifications vs added test files
    for f in candidate_changed_files:
        if f.endswith("_test.go"):
            chk = run_cmd(["git", "cat-file", "-e", f"{base_commit}:{f}"], cwd=repo, timeout=10)
            if chk.returncode == 0:
                # Pre-existing original test file: ANY modification by candidate is strictly prohibited
                if f not in tampered_tests:
                    tampered_tests.append(f)
                    failed_nodes.append(f"cheat_original_test_modified: {f}")
            else:
                # New test file added by candidate: strictly prohibited
                if f not in submitted_test_files:
                    submitted_test_files.append(f)
                    failed_nodes.append(f"cheat_test_file_submitted: {f}")

    if tampered_tests:
        details["original_tests_tampered"] = tampered_tests
    if submitted_test_files:
        details["submitted_test_files"] = submitted_test_files

    # 2.8 Evaluation bypass & test neutralization detection
    eval_env_patterns = [
        re.compile(r'\bos\.Getenv\s*\(\s*["\'](DF_HARBOR|HARBOR|CALIBRATION|DEEPSWE_REWARD|DEEPSWE_EVAL|TEST_HARNESS)["\']\s*\)'),
        re.compile(r'os\.LookupEnv\s*\(\s*["\'](DF_HARBOR|HARBOR|CALIBRATION|DEEPSWE_REWARD|DEEPSWE_EVAL|TEST_HARNESS)["\']\s*\)'),
    ]
    test_skip_pattern = re.compile(r'\bt\.(Skip|SkipNow|Skipf)\s*\(')
    build_ignore_pattern = re.compile(r'//\s*(go:build|\+build)\s+ignore\b')

    # Inspect candidate diff (excluding verified evaluator files)
    pathspec = [":!tests"] + [f":!{f}" for f in verified_trusted_files]
    diff_proc = run_cmd(["git", "diff", base_commit, "--", ".", *pathspec], cwd=repo, timeout=timeout)
    if diff_proc.returncode == 0:
        diff_text = diff_proc.stdout
        for pat in eval_env_patterns:
            if pat.search(diff_text):
                failed_nodes.append("cheat_evaluation_bypass_detected")
                details["evaluation_bypass"] = "Evaluation environment variable probing detected in candidate diff."
                break

        for patch_line in diff_text.splitlines():
            if patch_line.startswith("+") and not patch_line.startswith("+++"):
                if test_skip_pattern.search(patch_line):
                    failed_nodes.append("cheat_test_neutralization_detected")
                    details["test_neutralization"] = f"Unauthorized test skipping detected: {patch_line.strip()}"
                    break
                if build_ignore_pattern.search(patch_line):
                    failed_nodes.append("cheat_test_build_tag_exclusion")
                    details["build_tag_exclusion"] = f"Unauthorized build tag ignore detected: {patch_line.strip()}"
                    break

    # Also inspect untracked candidate Go files
    for untracked in candidate_changed_files:
        if untracked.endswith(".go") and (repo / untracked).is_file():
            try:
                content = (repo / untracked).read_text(encoding="utf-8")
                for pat in eval_env_patterns:
                    if pat.search(content):
                        failed_nodes.append(f"cheat_evaluation_bypass_detected in {untracked}")
                        break
                if build_ignore_pattern.search(content):
                    failed_nodes.append(f"cheat_test_build_tag_exclusion in {untracked}")
                    break
            except Exception:
                pass

    # 2.9 Configured cheat nodes in config.json
    hard_gate_cfg = config.get("hard_gate", {})
    configured_cheat_nodes = hard_gate_cfg.get("cheat_nodes", [])
    for cheat_node in configured_cheat_nodes:
        failed_nodes.append(str(cheat_node))
    if configured_cheat_nodes:
        details["configured_cheat_nodes"] = configured_cheat_nodes
    else:
        details["configured_cheat_nodes"] = "ok"

    passed = len(failed_nodes) == 0
    return passed, failed_nodes, details


NODE_REGEX = re.compile(r"^([a-zA-Z0-9_\-\./]+_test\.go)::(Test[A-Za-z0-9_]+)(?:/([A-Za-z0-9_\-\./\s:]+))?$")


def validate_atomicity_structure(
    repo: Path,
    nodes: list[str],
    test_patch_path: Path | None = None,
) -> tuple[list[str], dict[str, Any]]:
    """Validate concrete atomicity of test nodes statically."""
    atomicity_failures: list[str] = []
    details: dict[str, Any] = {}

    patch_content = ""
    if test_patch_path and test_patch_path.exists():
        try:
            patch_content = test_patch_path.read_text(encoding="utf-8")
        except Exception:
            pass

    seen_normalized: dict[str, str] = {}

    for node in nodes:
        match = NODE_REGEX.match(node)
        if not match:
            atomicity_failures.append(f"malformed_atomicity_node: {node}")
            continue

        rel_file, root_func, subtest = match.group(1), match.group(2), match.group(3)

        # Reject path normalization aliases like ./foo_test.go
        norm_file = os.path.normpath(rel_file)
        canon_key = f"{norm_file}::{root_func}" + (f"/{subtest}" if subtest else "")
        if canon_key in seen_normalized and seen_normalized[canon_key] != node:
            atomicity_failures.append(f"alias_p2p_node: {node} is an alias of {seen_normalized[canon_key]}")
        else:
            seen_normalized[canon_key] = node

        # File existence check
        target_file = repo / norm_file
        file_exists = target_file.exists()
        file_in_patch = f"+++ b/{norm_file}" in patch_content or f"+++ b/{rel_file}" in patch_content

        if not file_exists and not file_in_patch:
            atomicity_failures.append(f"atomicity_missing_file: {node}")
            continue

        # Root test function existence check
        root_exists = False
        if file_exists:
            try:
                code = target_file.read_text(encoding="utf-8")
                if f"func {root_func}(" in code:
                    root_exists = True
            except Exception:
                pass
        if not root_exists and file_in_patch:
            if f"func {root_func}(" in patch_content:
                root_exists = True

        if not root_exists:
            atomicity_failures.append(f"atomicity_missing_root_test: {node}")

    details["atomicity_failures_count"] = len(atomicity_failures)
    return atomicity_failures, details


def check_p2p(
    repo: Path,
    config: dict[str, Any],
    verifier_dir: Path,
    skip_exec: bool = False,
    require_new_p2p: bool = False,
    timeout: int = 300,
) -> tuple[bool, list[str], dict[str, Any]]:
    """Category 3: P2P Test.

    Verify consistency of task semantics, input-output relations, and core constraints:
    - Atomicity: 1 functional check = 1 test node
    - Inventory validation: checks p2p_select.txt for validity, blank entries, and duplicates
    - Baseline test integrity: Go-aware comparison (file_hashes / gofmt_hashes) preserving literals and helpers
    - New P2P enforcement: validates new atomic preservation P2P tests
    - Runtime execution: executes P2P tests only and validates process exit code and package-level events
    """
    failed_nodes: list[str] = []
    details: dict[str, Any] = {}

    raw_p2p_config = config.get("p2p", [])
    raw_f2p_config = config.get("f2p", [])

    # 3.0 Duplicate check in config P2P
    seen_p2p: set[str] = set()
    dup_p2p: list[str] = []
    for item in raw_p2p_config:
        s_item = str(item)
        if s_item in seen_p2p:
            dup_p2p.append(s_item)
        seen_p2p.add(s_item)

    if dup_p2p:
        for dup in dup_p2p:
            failed_nodes.append(f"duplicate_p2p_node: {dup}")
        details["duplicate_p2p_nodes"] = dup_p2p
    else:
        details["duplicate_p2p_nodes"] = []

    # Overlap check between P2P and F2P
    overlap = set(raw_p2p_config) & set(raw_f2p_config)
    if overlap:
        for ov in sorted(overlap):
            failed_nodes.append(f"p2p_f2p_overlap: {ov}")
        details["overlap_nodes"] = sorted(overlap)
    else:
        details["overlap_nodes"] = []

    p2p_nodes = [str(node) for node in raw_p2p_config]
    details["configured_unique_p2p_count"] = len(set(p2p_nodes))

    # 3.1 Load original frozen P2P inventory (from freeze_manifest.json)
    manifest_path = verifier_dir.parent / "assets" / "freeze_manifest.json"
    if not manifest_path.exists():
        fallback_manifest = Path(__file__).resolve().parent.parent / "assets" / "freeze_manifest.json"
        if fallback_manifest.exists():
            manifest_path = fallback_manifest

    if not manifest_path.exists():
        failed_nodes.append("missing_integrity_metadata")
        details["integrity_error"] = "freeze_manifest.json not found"
        return False, failed_nodes, details

    try:
        manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as e:
        failed_nodes.append("malformed_integrity_metadata")
        details["integrity_error"] = f"Failed to parse freeze_manifest.json: {e}"
        return False, failed_nodes, details

    original_p2p_nodes: list[str] = manifest_data.get("original_inventory", [])
    details["original_inventory_count"] = len(original_p2p_nodes)

    # Load and validate execution selector (p2p_select.txt) covering all executed P2P nodes
    p2p_select_file = verifier_dir / "p2p_select.txt"
    if not p2p_select_file.exists():
        fallback_p2p = Path(__file__).resolve().parent / "p2p_select.txt"
        if fallback_p2p.exists():
            p2p_select_file = fallback_p2p

    if not p2p_select_file.exists():
        failed_nodes.append("missing_p2p_select_file")
        details["original_inventory_integrity"] = "p2p_select.txt not found"
        return False, failed_nodes, details

    try:
        raw_select_text = p2p_select_file.read_text(encoding="utf-8")
    except Exception as e:
        failed_nodes.append(f"missing_p2p_select_file: {e}")
        return False, failed_nodes, details

    raw_lines = raw_select_text.splitlines()
    selector_nodes: list[str] = []
    select_dups: list[str] = []
    seen_select: set[str] = set()

    for idx, line in enumerate(raw_lines):
        trimmed = line.strip()
        if not trimmed:
            if 0 < idx < len(raw_lines) - 1 and any(l.strip() for l in raw_lines[idx:]):
                failed_nodes.append("p2p_select_blank_entry")
            continue
        if not NODE_REGEX.match(trimmed):
            failed_nodes.append(f"p2p_select_invalid_node: {trimmed}")
        if trimmed in seen_select:
            select_dups.append(trimmed)
        seen_select.add(trimmed)
        selector_nodes.append(trimmed)

    if select_dups:
        for dup in select_dups:
            failed_nodes.append(f"p2p_select_duplicate_node: {dup}")
        details["p2p_select_duplicates"] = select_dups

    details["selector_count"] = len(selector_nodes)

    # Validate set(config.p2p) == set(selector)
    configured_set = set(p2p_nodes)
    selector_set = set(selector_nodes)
    missing_in_config = [node for node in selector_nodes if node not in configured_set]
    missing_in_selector = [node for node in p2p_nodes if node not in selector_set]
    if missing_in_config:
        for m in missing_in_config:
            failed_nodes.append(f"missing_configured_test: {m}")
        details["missing_configured_tests"] = missing_in_config
    if missing_in_selector:
        for m in missing_in_selector:
            failed_nodes.append(f"missing_selector_test: {m}")
        details["missing_selector_tests"] = missing_in_selector

    # Validate all original frozen nodes are retained in selector
    missing_original = [node for node in original_p2p_nodes if node not in selector_set]
    if missing_original:
        for m in missing_original:
            failed_nodes.append(f"missing_original_frozen_test: {m}")
        details["missing_original_frozen_tests"] = missing_original

    # 3.2 Atomicity validation (structural guard)
    test_patch_path = verifier_dir / "test.patch"
    atomicity_failures, atomicity_details = validate_atomicity_structure(
        repo=repo,
        nodes=p2p_nodes,
        test_patch_path=test_patch_path,
    )
    if atomicity_failures:
        failed_nodes.extend(atomicity_failures)
        details["atomicity_failures"] = atomicity_failures

    # 3.3 Count thresholds and new P2P test requirement
    if len(set(p2p_nodes)) < 30:
        failed_nodes.append(f"p2p_insufficient_nodes: count={len(set(p2p_nodes))} < 30")
        details["node_count_check"] = f"Insufficient unique P2P nodes: {len(set(p2p_nodes))} (min: 30)"
    else:
        details["node_count_check"] = f"ok ({len(set(p2p_nodes))} unique nodes >= 30)"

    new_p2p_nodes = [node for node in p2p_nodes if node not in set(original_p2p_nodes)]
    details["new_p2p_count"] = len(new_p2p_nodes)

    task_requires_new_p2p = require_new_p2p or bool(
        config.get("require_new_p2p") or config.get("hard_gate", {}).get("require_new_p2p")
    )

    if task_requires_new_p2p and len(new_p2p_nodes) == 0:
        failed_nodes.append("no_new_p2p_nodes_configured")
        details["new_p2p_check"] = "Task defines new P2P checks but no new P2P nodes were configured."

    # Validate backing of new P2P nodes
    for new_node in new_p2p_nodes:
        match = NODE_REGEX.match(new_node)
        if match:
            rf, rf_name = match.group(1), match.group(2)
            backed = False
            if (repo / rf).exists():
                try:
                    if f"func {rf_name}(" in (repo / rf).read_text(encoding="utf-8"):
                        backed = True
                except Exception:
                    pass
            if not backed and test_patch_path.exists():
                try:
                    if f"func {rf_name}(" in test_patch_path.read_text(encoding="utf-8"):
                        backed = True
                except Exception:
                    pass
            if not backed:
                failed_nodes.append(f"missing_new_p2p_test_backing: {new_node}")

    # 3.4 Original test integrity check (reliable baseline comparison)
    manifest_path = verifier_dir.parent / "assets" / "freeze_manifest.json"
    if not manifest_path.exists():
        failed_nodes.append("missing_integrity_metadata")
        details["integrity_error"] = "freeze_manifest.json not found"
        return False, failed_nodes, details

    try:
        manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as e:
        failed_nodes.append("malformed_integrity_metadata")
        details["integrity_error"] = f"Failed to parse freeze_manifest.json: {e}"
        return False, failed_nodes, details

    file_hashes: dict[str, str] = manifest_data.get("file_hashes", {})
    gofmt_hashes: dict[str, str] = manifest_data.get("gofmt_hashes", {})
    if not file_hashes or not gofmt_hashes or not isinstance(file_hashes, dict) or not isinstance(gofmt_hashes, dict):
        failed_nodes.append("malformed_integrity_metadata")
        details["integrity_error"] = "Manifest missing file_hashes or gofmt_hashes"
        return False, failed_nodes, details

    manifest_base_commit = str(manifest_data.get("base_commit", ""))
    required_base_commit = "697380ffec04290679230d8d04636eb41c99e0a8"
    if manifest_base_commit != required_base_commit:
        failed_nodes.append("integrity_base_commit_mismatch")
        details["integrity_error"] = f"Manifest base commit {manifest_base_commit} does not match required base commit {required_base_commit}"
        return False, failed_nodes, details

    original_files = sorted(set(n.split("::")[0] for n in original_p2p_nodes))
    modified_test_files: list[str] = []

    for rel_file in original_files:
        norm_file = os.path.normpath(rel_file)
        if norm_file not in file_hashes or norm_file not in gofmt_hashes:
            failed_nodes.append(f"incomplete_integrity_metadata: {norm_file}")
            continue

        cand_file = repo / norm_file
        if not cand_file.exists():
            failed_nodes.append(f"missing_original_test_file: {norm_file}")
            continue

        try:
            raw_bytes = cand_file.read_bytes()
        except Exception as e:
            failed_nodes.append(f"unreadable_original_test_file: {norm_file}: {e}")
            continue

        raw_sha = hashlib.sha256(raw_bytes).hexdigest()
        if raw_sha == file_hashes[norm_file]:
            # Exact match
            continue

        # Non-identical: run gofmt to verify harmless formatting vs semantic modification
        gofmt_proc = subprocess.run(
            ["gofmt"],
            input=raw_bytes,
            capture_output=True,
            timeout=20,
        )
        if gofmt_proc.returncode != 0:
            modified_test_files.append(norm_file)
            failed_nodes.append(f"modified_original_test_file: {norm_file} (gofmt syntax error)")
            continue

        gofmt_sha = hashlib.sha256(gofmt_proc.stdout).hexdigest()
        if gofmt_sha == gofmt_hashes[norm_file]:
            # Harmless whitespace / formatting change normalized by gofmt
            continue

        # Genuine semantic change (changed literals, helpers, TestMain, or test logic)
        modified_test_files.append(norm_file)
        failed_nodes.append(f"modified_original_test_file: {norm_file}")

    # Check for missing test functions in existing original files
    for node in original_p2p_nodes:
        rf, root_func = node.split("::")[0], node.split("::")[1].split("/")[0]
        tf = repo / rf
        if tf.exists():
            try:
                content = tf.read_text(encoding="utf-8")
                if f"func {root_func}(" not in content:
                    failed_nodes.append(f"missing_original_test: {node}")
            except Exception:
                pass

    details["modified_original_test_files"] = modified_test_files
    details["original_integrity_status"] = "ok" if not modified_test_files else "tampered"

    # 3.5 Execution check: Do not allow P2P execution to be skipped while reporting success
    if skip_exec:
        failed_nodes.append("p2p_execution_skipped")
        details["skipped_execution"] = "P2P execution was skipped (diagnostic static mode only; Hard Gate cannot pass without execution)"
        details["p2p_passed_count"] = 0
        details["unobserved_nodes"] = p2p_nodes
        return False, failed_nodes, details

    # If static / integrity checks failed, return early
    if failed_nodes:
        return False, failed_nodes, details

    # 3.6 Runtime execution of intended P2P test selection
    pkg_roots: dict[str, set[str]] = {}
    node_to_pkg_test: dict[str, tuple[str, str]] = {}

    for node in p2p_nodes:
        rel_file, test_spec = node.split("::", 1)
        root_test = test_spec.split("/", 1)[0]
        rel_dir = os.path.dirname(rel_file)
        pkg_target = "./" + rel_dir if rel_dir else "."
        pkg_full = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")
        node_to_pkg_test[node] = (pkg_full, test_spec)
        pkg_roots.setdefault(pkg_target, set()).add(root_test)

    targets = sorted(pkg_roots.keys())
    all_roots = sorted(set(r for roots in pkg_roots.values() for r in roots))
    run_regex = "^(" + "|".join(all_roots) + ")$"

    # Original cross-package tests share fixed loopback port 127.0.0.1:5000; run P2P packages serially (-p 1) to prevent port contention.
    cmd = ["go", "test", "-race", "-count=1", "-p", "1", "-json", *targets, "-run", run_regex]
    details["p2p_test_command"] = cmd

    try:
        proc = run_cmd(cmd, cwd=repo, timeout=timeout)
    except subprocess.TimeoutExpired:
        failed_nodes.append(f"p2p_timeout: command {' '.join(cmd[:4])}")
        return False, failed_nodes, details
    except Exception as e:
        failed_nodes.append(f"p2p_execution_exception: {e}")
        return False, failed_nodes, details

    details["p2p_test_exit_code"] = proc.returncode
    if proc.stderr.strip():
        details["p2p_test_stderr"] = proc.stderr.strip()[:2000]

    terminal_events: dict[tuple[str, str], str] = {}
    started_tests: set[tuple[str, str]] = set()
    started_pkgs: set[str] = set()
    conflicting_events: list[str] = []
    duplicate_terminal_events: list[str] = []
    pkg_status: dict[str, str] = {}
    pkg_errors: dict[str, list[str]] = {}
    test_errors: dict[tuple[str, str], list[str]] = {}

    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except Exception:
            continue

        event_pkg = event.get("Package")
        event_test = event.get("Test")
        action = event.get("Action")
        if not event_pkg or not action:
            continue

        if event_test:
            key = (event_pkg, event_test)
            if action == "run":
                started_tests.add(key)
            elif action in ("pass", "fail", "skip"):
                if key in terminal_events:
                    old_action = terminal_events[key]
                    if old_action != action:
                        conflicting_events.append(f"{event_pkg}::{event_test} ({old_action} vs {action})")
                    else:
                        duplicate_terminal_events.append(f"{event_pkg}::{event_test}")
                    # Never allow a later pass/skip to overwrite an earlier fail
                    if old_action == "fail":
                        action = "fail"
                terminal_events[key] = action
            elif action == "output" and "Output" in event:
                test_errors.setdefault(key, []).append(event["Output"])
        else:
            if action == "start":
                started_pkgs.add(event_pkg)
            elif action in ("pass", "fail", "skip"):
                if event_pkg in pkg_status:
                    old_action = pkg_status[event_pkg]
                    if old_action != action:
                        conflicting_events.append(f"package {event_pkg} ({old_action} vs {action})")
                    else:
                        duplicate_terminal_events.append(f"package {event_pkg}")
                    if old_action == "fail":
                        action = "fail"
                pkg_status[event_pkg] = action
            elif action == "output" and "Output" in event:
                pkg_errors.setdefault(event_pkg, []).append(event["Output"])

    # Process exit code check: Nonzero test command exit MUST fail the gate
    if proc.returncode != 0:
        failed_nodes.append(f"p2p_process_failure (exit code {proc.returncode})")
        details["process_failure"] = f"go test process exited with code {proc.returncode}"

    # Conflicting and duplicate terminal events MUST fail the gate
    details["conflicting_events"] = conflicting_events
    details["duplicate_terminal_events"] = duplicate_terminal_events
    for ce in conflicting_events:
        failed_nodes.append(f"p2p_conflicting_event: {ce}")
    for de in duplicate_terminal_events:
        failed_nodes.append(f"p2p_duplicate_terminal: {de}")

    # Package-level failure check (TestMain, teardown, panic, goroutine leak)
    package_failures: list[str] = []
    for pkg, action in pkg_status.items():
        if action == "fail":
            package_failures.append(pkg)
            failed_nodes.append(f"p2p_package_failure: {pkg}")
    details["package_failures"] = package_failures
    if package_failures:
        details["package_errors"] = {
            pkg: "".join(pkg_errors.get(pkg, []))[-2000:]
            for pkg in package_failures
        }

    # Incomplete execution check: any started test or package without terminal completion
    unterminated_tests = [
        f"{pkg}::{test}"
        for (pkg, test) in sorted(started_tests)
        if (pkg, test) not in terminal_events
    ]
    if unterminated_tests:
        details["unterminated_tests"] = unterminated_tests
        for ut in unterminated_tests:
            failed_nodes.append(f"p2p_unterminated_test: {ut}")

    unterminated_packages = [
        pkg
        for pkg in sorted(started_pkgs)
        if pkg not in pkg_status
    ]
    if unterminated_packages:
        details["unterminated_packages"] = unterminated_packages
        for up in unterminated_packages:
            failed_nodes.append(f"p2p_unterminated_package: {up}")

    # Evaluate individual P2P node outcomes
    p2p_passed_count = 0
    p2p_failed_test_nodes: list[str] = []
    unobserved_nodes: list[str] = []

    passed_p2p_nodes: list[str] = []
    conflict_or_dup_keys = {
        ce.split(" (")[0].strip() for ce in conflicting_events
    } | set(duplicate_terminal_events)

    for node in p2p_nodes:
        pkg, test_name = node_to_pkg_test.get(node, ("", ""))
        key_str = f"{pkg}::{test_name}"
        status = terminal_events.get((pkg, test_name))
        if key_str in conflict_or_dup_keys:
            # Already marked in failed_nodes via conflicting_events / duplicate_terminal_events
            p2p_failed_test_nodes.append(f"{node} (conflicting/duplicate terminal)")
        elif status == "pass":
            p2p_passed_count += 1
            passed_p2p_nodes.append(node)
        elif status == "fail":
            p2p_failed_test_nodes.append(node)
        elif status == "skip":
            if config.get("skip_is_failure", True):
                p2p_failed_test_nodes.append(f"{node} (skipped)")
            else:
                p2p_passed_count += 1
                passed_p2p_nodes.append(node)
        else:
            unobserved_nodes.append(node)
            p2p_failed_test_nodes.append(f"{node} (not observed)")

    details["p2p_passed_count"] = p2p_passed_count
    details["passed_p2p_nodes"] = passed_p2p_nodes
    details["unobserved_nodes"] = unobserved_nodes

    if p2p_failed_test_nodes:
        failed_nodes.extend(p2p_failed_test_nodes)
        details["failed_p2p_nodes"] = p2p_failed_test_nodes[:30]
        details["failed_p2p_output"] = {
            node: "".join(test_errors.get(node_to_pkg_test.get(node, ("", "")), []))[-2000:]
            for node in p2p_failed_test_nodes[:10]
        }

    passed = len(failed_nodes) == 0
    return passed, failed_nodes, details


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic Hard Gate.")
    parser.add_argument("--config", type=Path, required=True, help="Path to config.json")
    parser.add_argument("--repo", type=Path, required=True, help="Path to repository")
    parser.add_argument("--output", type=Path, required=True, help="Output path for hard gate JSON")
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0, help="Patch apply failure flag")
    parser.add_argument("--skip-p2p-exec", action="store_true", help="Diagnostic static check only (always fails gate)")
    parser.add_argument("--require-new-p2p", action="store_true", help="Require new P2P tests beyond frozen inventory")
    parser.add_argument("--timeout", type=int, default=300, help="Subprocess timeout in seconds")
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    hard_gate_cfg = config.get("hard_gate", {})
    compile_paths = hard_gate_cfg.get("compile_paths", [])
    cheat_penalty = float(hard_gate_cfg.get("cheat_penalty", -1.0))
    verifier_dir = Path(__file__).resolve().parent

    # 1. Build Test
    build_passed, build_failed, build_details = check_build(
        repo=args.repo,
        config=config,
        apply_failed=bool(args.apply_failed),
        timeout=args.timeout,
    )

    # 2. Anti-Cheat Test
    anti_cheat_passed, anti_cheat_failed, anti_cheat_details = check_anti_cheat(
        repo=args.repo,
        config=config,
        verifier_dir=verifier_dir,
        timeout=args.timeout,
    )

    # 3. P2P Test (run when build succeeded)
    if build_passed:
        p2p_passed, p2p_failed, p2p_details = check_p2p(
            repo=args.repo,
            config=config,
            verifier_dir=verifier_dir,
            skip_exec=args.skip_p2p_exec,
            require_new_p2p=args.require_new_p2p,
            timeout=args.timeout,
        )
    else:
        p2p_passed = False
        p2p_failed = ["p2p_skipped_due_to_build_failure"]
        p2p_details = {"skipped": True}

    all_failed_nodes = list(dict.fromkeys(build_failed + anti_cheat_failed + p2p_failed))
    passed = len(all_failed_nodes) == 0

    p2p_nodes = [str(node) for node in config.get("p2p", [])]

    infra_failed = [
        fn for fn in (build_failed + p2p_failed)
        if any(fn.startswith(prefix) for prefix in (
            "candidate_patch_apply",
            "build_missing_go_mod",
            "build_missing_go_sum",
            "build_mod_verify_failure",
            "build_vet_failure",
            "go_build_failure",
            "p2p_timeout",
            "p2p_execution_exception",
            "p2p_process_failure",
            "p2p_unterminated",
        ))
    ]
    if args.apply_failed:
        infra_failed.append("candidate_patch_apply")
    execution_passed = len(infra_failed) == 0

    result = {
        "passed": passed,
        "apply_failed": bool(args.apply_failed),
        "build_passed": build_passed,
        "anti_cheat_passed": anti_cheat_passed,
        "execution_passed": execution_passed,
        "p2p_passed": p2p_passed,
        "failed_nodes": all_failed_nodes,
        "compile_paths": compile_paths,
        "cheat_penalty": cheat_penalty if not passed else 0.0,
        "categories": {
            "build": {
                "passed": build_passed,
                "failed_nodes": build_failed,
                "details": build_details,
            },
            "anti_cheat": {
                "passed": anti_cheat_passed,
                "failed_nodes": anti_cheat_failed,
                "details": anti_cheat_details,
            },
            "execution": {
                "passed": execution_passed,
                "failed_nodes": infra_failed,
                "details": {
                    "apply_failed": bool(args.apply_failed),
                    "infrastructure_failures": infra_failed,
                },
            },
            "p2p": {
                "passed": p2p_passed,
                "total_nodes": len(p2p_nodes),
                "passed_nodes": p2p_details.get("p2p_passed_count", 0),
                "failed_nodes": p2p_failed,
                "details": p2p_details,
            },
        },
        "summary": {
            "build": "PASSED" if build_passed else "FAILED",
            "anti_cheat": "PASSED" if anti_cheat_passed else "FAILED",
            "execution": "PASSED" if execution_passed else "FAILED",
            "p2p": "PASSED" if p2p_passed else "FAILED",
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
