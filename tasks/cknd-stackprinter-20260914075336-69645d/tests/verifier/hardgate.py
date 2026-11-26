#!/usr/bin/env python3
"""Deterministic compile, integrity, candidate scope, and anti-cheat hard gates."""

from __future__ import annotations

import argparse
import hashlib
import ast
import json
import os
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


EXPECTED_CONFIG_SHA256 = "61260d38e22ba710e495f79b7e557564363af79d7a91bc7324653d1ca1a93498"


class InfrastructureError(RuntimeError):
    """The trusted runner could not produce a usable test execution report."""


def _run_cheat_node(repo: Path, node: str) -> tuple[bool, str]:
    env = os.environ.copy()
    env.update({
        "PYTHONUTF8": "1",
        "PYTHONIOENCODING": "utf-8",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1",
    })
    with tempfile.TemporaryDirectory(prefix="hardgate-") as temp_dir:
        junit = Path(temp_dir) / "result.xml"
        command = [
            sys.executable, "-m", "pytest", node, "-q", "-ra", "-p",
            "no:cacheprovider", f"--junitxml={junit}",
        ]
        try:
            completed = subprocess.run(
                command, cwd=repo, env=env, capture_output=True, text=True,
                encoding="utf-8", errors="replace", timeout=180, check=False,
            )
        except OSError as exc:
            raise InfrastructureError(f"cannot start pytest: {exc}") from exc
        except subprocess.TimeoutExpired as exc:
            return False, f"candidate test exceeded 180 seconds: {exc}"
        output = (completed.stdout + "\n" + completed.stderr).strip()
        if completed.returncode == 3:
            raise InfrastructureError(f"pytest internal error: {output[-4000:]}")
        if not junit.is_file():
            raise InfrastructureError(f"pytest produced no JUnit report: {output[-4000:]}")
        skipped = False
        if junit.is_file():
            try:
                skipped = bool(ET.parse(junit).getroot().findall(".//skipped"))
            except ET.ParseError as exc:
                raise InfrastructureError(f"invalid pytest JUnit report: {exc}") from exc
        return completed.returncode == 0 and not skipped, output[-4000:]


def _anti_cheat_findings(repo: Path) -> list[str]:
    package = repo / "stackprinter"
    if not package.is_dir():
        return []  # Missing source is handled by the compilation gate.
    forbidden_text = (
        "solution.patch", "/logs/artifacts/model.patch", "test_refactor_cheat",
        "p2p_select.txt",
    )
    findings: list[str] = []
    for path in sorted(package.rglob("*.py")):
        try:
            source = path.read_text(encoding="utf-8")
            tree = ast.parse(source, filename=str(path))
        except (OSError, SyntaxError, UnicodeError, ValueError):
            # Unreadable or malformed candidate source is a compile failure,
            # not evidence of cheating. Continue scanning other files so an
            # unrelated syntax error cannot hide a real anti-cheat finding.
            continue
        # Comments are absent from the AST.  Remove docstrings as well: a
        # harmless explanation must not become an answer-artifact finding.
        for owner in ast.walk(tree):
            body = getattr(owner, "body", None)
            if not isinstance(body, list) or not body:
                continue
            first = body[0]
            if (isinstance(first, ast.Expr)
                    and isinstance(first.value, ast.Constant)
                    and isinstance(first.value.value, str)):
                body.pop(0)
        artifact_names: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and any(
                token in ast.unparse(node.value) for token in forbidden_text
            ):
                artifact_names.update(
                    target.id for target in node.targets if isinstance(target, ast.Name)
                )
            elif isinstance(node, ast.AnnAssign) and node.value is not None and any(
                token in ast.unparse(node.value) for token in forbidden_text
            ) and isinstance(node.target, ast.Name):
                artifact_names.add(node.target.id)

        read_methods = {"open", "read", "read_text", "read_bytes"}
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            method = (node.func.id if isinstance(node.func, ast.Name) else
                      node.func.attr if isinstance(node.func, ast.Attribute) else "")
            if method not in read_methods:
                continue
            expression = ast.unparse(node)
            names = {part.id for part in ast.walk(node) if isinstance(part, ast.Name)}
            if (any(token in expression for token in forbidden_text)
                    or names.intersection(artifact_names)):
                findings.append(f"{path.relative_to(repo)}:{node.lineno}:answer-artifact-read")
                break
    return findings


def _path_exists_in_revision(repo: Path, revision: str, path: str) -> bool:
    try:
        check = subprocess.run(
            ["git", "cat-file", "-e", f"{revision}:{path}"],
            cwd=repo,
            capture_output=True,
            timeout=30,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return True
    return check.returncode == 0


def _config_sha256_findings(config_path: Path) -> list[str]:
    try:
        actual = hashlib.sha256(config_path.read_bytes()).hexdigest()
    except OSError as exc:
        return [f"config-unreadable:{exc}"]
    if actual != EXPECTED_CONFIG_SHA256:
        return [f"config-sha256-mismatch:{actual}"]
    return []


def _integrity_findings(config: dict[str, Any], repo: Path) -> list[str]:
    findings: list[str] = []
    declared = config.get("integrity")
    if not isinstance(declared, dict):
        findings.append("missing-integrity-digests")
        declared = {}
    for key, filename in (
        ("test_patch_sha256", "test.patch"),
        ("p2p_select_sha256", "p2p_select.txt"),
    ):
        expected = str(declared.get(key) or "").strip().lower()
        if len(expected) != 64 or any(char not in "0123456789abcdef" for char in expected):
            findings.append(f"invalid-integrity-digest:{key}")
            continue
        path = Path(__file__).with_name(filename)
        try:
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError as exc:
            findings.append(f"integrity-file-unreadable:{filename}:{exc}")
            continue
        if actual != expected:
            findings.append(f"integrity-digest-mismatch:{key}")

    base_commit = str(config.get("base_commit") or "").strip()
    if not base_commit:
        return findings + ["missing-base-commit"]
    try:
        commit_check = subprocess.run(
            ["git", "cat-file", "-e", f"{base_commit}^{{commit}}"],
            cwd=repo,
            capture_output=True,
            timeout=30,
            check=False,
        )
        if commit_check.returncode != 0:
            return [f"baseline-commit-not-found:{base_commit}"]
        completed = subprocess.run(
            ["git", "diff", "--name-only", base_commit, "--"],
            cwd=repo,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return [f"git-diff:{exc}"]
    if completed.returncode != 0:
        return [f"git-diff:{completed.stderr.strip()[-500:]}"]
    changed = [line.strip().replace("\\", "/") for line in completed.stdout.splitlines() if line.strip()]
    protected = [
        path for path in changed
        if path.startswith("tests/") and _path_exists_in_revision(repo, base_commit, path)
    ]
    findings.extend(f"protected-test-modified:{path}" for path in protected)
    return findings


def _runtime_sources(repo: Path) -> list[Path]:
    """Exclude standalone tests, but follow production imports into test code.

    Every non-test module is a runtime root (including public modules that the
    package initializer does not import). Importing a test helper makes that
    helper, its package initializers and transitive imports runtime code too.
    Nonliteral dynamic imports conservatively retain all test modules.
    """
    modules: dict[str, Path] = {}
    trees: dict[str, ast.AST] = {}
    selected: set[str] = set()
    for path in sorted((repo / 'stackprinter').rglob('*.py')):
        parts = path.relative_to(repo).with_suffix('').parts
        module = '.'.join(parts[:-1] if parts[-1] == '__init__' else parts)
        modules[module] = path
        try:
            trees[module] = ast.parse(path.read_text())
        except (SyntaxError, UnicodeError):
            continue  # Compilation gate owns these failures.
        is_test = ('tests' in parts or 'test' in parts or
                   path.name.startswith('test_') or path.name.endswith('_test.py') or
                   path.name == 'conftest.py')
        if not is_test:
            selected.add(module)

    pending = list(selected)
    while pending:
        module = pending.pop()
        path = modules[module]
        package = module if path.name == '__init__.py' else module.rpartition('.')[0]
        imports: set[str] = set()
        for node in ast.walk(trees[module]):
            if isinstance(node, ast.Import):
                imports.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    parent = package.split('.')
                    parent = parent[:len(parent) - node.level + 1]
                    base = '.'.join(parent + ([node.module] if node.module else []))
                else:
                    base = node.module or ''
                imports.add(base)
                imports.update(base + '.' + alias.name for alias in node.names)
            elif isinstance(node, ast.Call):
                name = node.func.id if isinstance(node.func, ast.Name) else (
                    node.func.attr if isinstance(node.func, ast.Attribute) else '')
                if name in {'import_module', '__import__'}:
                    if not node.args or not isinstance(node.args[0], ast.Constant) or not isinstance(node.args[0].value, str):
                        return sorted(modules.values())
                    target = node.args[0].value
                    if target.startswith('.'):
                        # Dynamic relative imports can select another package.
                        return sorted(modules.values())
                    imports.add(target)
        for target in imports:
            parts = target.split('.')
            for size in range(1, len(parts) + 1):
                dependency = '.'.join(parts[:size])
                if dependency in trees and dependency not in selected:
                    selected.add(dependency)
                    pending.append(dependency)
    return sorted(modules[module] for module in selected)


def _dependency_findings(config: dict[str, Any], repo: Path) -> list[str]:
    def roots(source):
        tree = ast.parse(source)
        found = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                found.update(a.name.split(".")[0] for a in node.names)
            elif isinstance(node, ast.ImportFrom) and not node.level and node.module:
                found.add(node.module.split(".")[0])
            elif isinstance(node, ast.Call):
                name = node.func.id if isinstance(node.func, ast.Name) else (
                    node.func.attr if isinstance(node.func, ast.Attribute) else "")
                if name in {"import_module", "__import__"} and node.args:
                    arg = node.args[0]
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        found.add(arg.value.split(".")[0])
        return found
    revision = str(config["base_commit"])
    listing = subprocess.run(["git", "ls-tree", "-r", "--name-only", revision,
                              "--", "stackprinter"], cwd=repo, capture_output=True,
                             text=True, check=True).stdout.splitlines()
    allowed = set(sys.stdlib_module_names) | {"stackprinter"}
    for name in listing:
        if name.endswith(".py"):
            source = subprocess.run(["git", "show", f"{revision}:{name}"], cwd=repo,
                                    capture_output=True, text=True, check=True).stdout
            allowed.update(roots(source))
    findings = []
    for path in _runtime_sources(repo):
        try:
            unexpected = roots(path.read_text()) - allowed
        except (SyntaxError, UnicodeError):
            continue  # Compilation gate attributes malformed candidate source.
        findings.extend(f"new-runtime-import:{path.relative_to(repo)}:{name}"
                        for name in sorted(unexpected))
    return findings


def check_candidate_scope(config: dict[str, Any], repo: Path) -> tuple[bool, list[str]]:
    """Verify candidate modifications are strictly confined to stackprinter/."""
    base_commit = str(config.get("base_commit") or "").strip()
    if not base_commit:
        return False, ["missing-base-commit"]
    try:
        check = subprocess.run(
            ["git", "cat-file", "-e", f"{base_commit}^{{commit}}"],
            cwd=repo,
            capture_output=True,
            timeout=30,
            check=False,
        )
        if check.returncode != 0:
            return False, [f"baseline-commit-not-found:{base_commit}"]
        diff = subprocess.run(
            ["git", "diff", "-z", "-M", "--name-status", base_commit],
            cwd=repo,
            capture_output=True,
            timeout=30,
            check=False,
        )
        if diff.returncode != 0:
            return False, [f"git-diff-failed:{diff.stderr.decode('utf-8', 'replace').strip()[-500:]}"]

        raw_parts = [p.decode("utf-8", "replace") for p in diff.stdout.split(b"\0") if p]
        i = 0
        changed_paths: list[str] = []
        while i < len(raw_parts):
            status = raw_parts[i]
            if status.startswith("R") or status.startswith("C"):
                changed_paths.append(raw_parts[i + 1])
                changed_paths.append(raw_parts[i + 2])
                i += 3
            else:
                changed_paths.append(raw_parts[i + 1])
                i += 2

        out_of_scope: list[str] = []
        for path_str in changed_paths:
            normalized = path_str.strip().replace("\\", "/")
            if not (normalized == "stackprinter" or normalized.startswith("stackprinter/")):
                out_of_scope.append(f"out-of-scope-modified:{normalized}")

        return len(out_of_scope) == 0, out_of_scope
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, [f"git-diff-exception:{exc}"]


def _p2p_selector_findings(config: dict[str, Any]) -> list[str]:
    """Ensure the audit selector records exactly the configured P2P cases."""
    selector = Path(__file__).with_name("p2p_select.txt")
    try:
        selected = [
            line.strip()
            for line in selector.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
    except OSError as exc:
        return [f"p2p-selector-unreadable:{exc}"]
    configured = [str(node) for node in config.get("p2p", [])]
    if len(selected) != len(set(selected)):
        return ["p2p-selector-duplicate-node"]
    missing = sorted(set(configured) - set(selected))
    extra = sorted(set(selected) - set(configured))
    findings = [f"p2p-selector-missing:{node}" for node in missing]
    findings.extend(f"p2p-selector-extra:{node}" for node in extra)
    return findings


def evaluate(
    config: dict[str, Any], repo: Path, apply_failed: bool, p2p_passed: bool | None = None,
    p2p_failed_nodes: list[str] | None = None, scope_failed_findings: list[str] | None = None,
) -> dict[str, Any]:
    failed_nodes: list[str] = []
    compile_results: dict[str, bool] = {}
    if apply_failed:
        failed_nodes.append("candidate_patch_apply")

    if scope_failed_findings:
        failed_nodes.extend(f"scope:{finding}" for finding in scope_failed_findings)

    configured_p2p = [str(node) for node in config.get("p2p", [])]
    failed_nodes.extend(_p2p_selector_findings(config))
    if len(configured_p2p) < 30:
        failed_nodes.append(f"p2p_count:{len(configured_p2p)}<30")
    if len(configured_p2p) != len(set(configured_p2p)):
        failed_nodes.append("p2p_duplicate_node_ids")
    non_atomic = [node for node in configured_p2p if "::" not in node]
    if non_atomic:
        failed_nodes.extend(f"p2p_non_atomic:{node}" for node in non_atomic)

    configured_build = config.get("build")
    if not isinstance(configured_build, list) or not all(
        isinstance(item, str) and item.strip() for item in configured_build
    ):
        failed_nodes.append("build_registration_invalid")
        configured_build = []
    for relative in configured_build:
        target = repo / relative
        result = target.is_dir()
        for source in sorted(target.rglob("*.py")):
            try:
                compile(source.read_bytes(), str(source), "exec")
            except (OSError, SyntaxError, ValueError):
                result = False
        compile_results[relative] = bool(result)
        if not result:
            failed_nodes.append(f"compile:{relative}")

    dependencies = _dependency_findings(config, repo)
    failed_nodes.extend(f"dependency:{finding}" for finding in dependencies)
    anti_cheat = _anti_cheat_findings(repo)
    failed_nodes.extend(f"cheat:{finding}" for finding in anti_cheat)
    integrity = _integrity_findings(config, repo)
    failed_nodes.extend(f"integrity:{finding}" for finding in integrity)
    configured_cheating = config.get("cheating")
    if not isinstance(configured_cheating, list) or not all(
        isinstance(item, str) and item.strip() for item in configured_cheating
    ):
        failed_nodes.append("cheating_registration_invalid")
        configured_cheating = []
    cheat_results: dict[str, dict[str, Any]] = {}
    for node in ([] if apply_failed or scope_failed_findings else configured_cheating):
        passed, message = _run_cheat_node(repo, str(node))
        cheat_results[str(node)] = {"passed": passed, "message": message}
        if not passed:
            failed_nodes.append(f"cheat_node:{node}")

    p2p_results: dict[str, dict[str, Any]] = {}
    if p2p_passed is None:
        p2p_failed_nodes = []
        for node in configured_p2p:
            node_passed, message = _run_cheat_node(repo, str(node))
            p2p_results[str(node)] = {"passed": node_passed, "message": message}
            if not node_passed:
                p2p_failed_nodes.append(str(node))
        p2p_passed = not p2p_failed_nodes
    else:
        p2p_failed_nodes = list(p2p_failed_nodes or [])
    if not p2p_passed:
        failed_nodes.extend(f"p2p:{node}" for node in p2p_failed_nodes)
    passed = not failed_nodes
    return {
        "passed": passed,
        "apply_failed": bool(apply_failed),
        "compile_paths": list(configured_build),
        "compile_results": compile_results,
        "dependency_findings": dependencies,
        "anti_cheat_findings": anti_cheat,
        "integrity_findings": integrity,
        "scope_findings": list(scope_failed_findings or []),
        "cheat_nodes": cheat_results,
        "p2p_nodes": p2p_results,
        "p2p": {"passed": bool(p2p_passed), "failed_nodes": p2p_failed_nodes},
        "failed_nodes": failed_nodes,
        "cheat_penalty": config.get("hard_gate", {}).get("cheat_penalty", -1.0)
        if not passed else 0.0,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    scope_ok, scope_findings = check_candidate_scope(config, args.repo)
    config_findings = _config_sha256_findings(args.config)
    if config_findings:
        scope_ok = False
        scope_findings.extend(config_findings)
    result = evaluate(config, args.repo, bool(args.apply_failed), scope_failed_findings=scope_findings if not scope_ok else None)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
