#!/usr/bin/env python3
"""Evaluate candidate integrity before installing evaluator-owned tests."""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import subprocess
from candidate_runtime import run_go
import tempfile
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "deepswe-hard-gate/v1"
TIMEOUT_SECONDS = 300
CHEAT_CHECKS = {"protected_assets_unchanged"}


class GateError(Exception):
    pass


def _git(repo: Path, *args: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            ["git", *args],
            cwd=repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise GateError(f"git inspection failed: {exc}") from exc


def _changed_paths(repo: Path, base_commit: str) -> list[str]:
    result = _git(
        repo,
        "diff",
        "--cached",
        "--name-only",
        "--no-renames",
        "-z",
        base_commit,
        "--",
    )
    if result.returncode != 0:
        raise GateError(result.stderr.strip() or "cannot inspect the candidate index")
    return sorted({item for item in result.stdout.split("\0") if item})


def _blocked_path_rules(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list) or not value:
        raise GateError("config.hard_gate.blocked_paths must be a non-empty rule list")
    patterns: set[str] = set()
    for rule in value:
        if (
            not isinstance(rule, dict)
            or set(rule) - {"pattern", "allow_additions"}
            or not isinstance(rule.get("pattern"), str)
            or not rule["pattern"]
            or not isinstance(rule.get("allow_additions", False), bool)
        ):
            raise GateError("invalid config.hard_gate.blocked_paths rule")
        if rule["pattern"] in patterns:
            raise GateError("config.hard_gate.blocked_paths contains duplicate patterns")
        patterns.add(rule["pattern"])
    return value


def _index_modes(repo: Path, paths: list[str]) -> dict[str, str]:
    if not paths:
        return {}
    result = _git(repo, "ls-files", "--stage", "-z", "--", *paths)
    if result.returncode != 0:
        raise GateError(result.stderr.strip() or "cannot inspect candidate file modes")
    modes: dict[str, str] = {}
    for record in result.stdout.split("\0"):
        if not record:
            continue
        metadata, separator, path = record.partition("\t")
        if not separator:
            raise GateError("malformed candidate index record")
        modes[path] = metadata.split(" ", 1)[0]
    return modes


def _tracked_at_base(repo: Path, base_commit: str, path: str) -> bool:
    return _git(repo, "cat-file", "-e", f"{base_commit}:{path}").returncode == 0


def _discard_candidate_test_additions(repo: Path, paths: list[str]) -> None:
    for relative in paths:
        path = repo / relative
        try:
            if path.is_symlink() or not path.is_file():
                raise GateError(f"candidate test addition is not a regular file: {relative}")
            path.unlink()
        except OSError as exc:
            raise GateError(f"cannot isolate candidate test addition {relative}: {exc}") from exc
    if paths:
        result = _git(repo, "update-index", "--force-remove", "--", *paths)
        if result.returncode != 0:
            raise GateError(result.stderr.strip() or "cannot isolate candidate test additions")


def _test(test_id: str, status: str, message: str, **details: Any) -> dict[str, Any]:
    result: dict[str, Any] = {
        "testId": test_id,
        "status": status,
        "message": message,
    }
    if details:
        result["details"] = details
    return result


def _compile(repo: Path, compile_paths: list[str]) -> tuple[str, str]:
    command = ["go", "test", "-run", "^$", "-count=1", *compile_paths]
    env = os.environ.copy()
    env.setdefault("GOCACHE", str(Path(env.get("TMPDIR", "/tmp")) / "lute-hardgate-cache"))
    try:
        completed = run_go(
            command,
            cwd=repo,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=TIMEOUT_SECONDS,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return "other", f"target compilation could not run: {exc}"
    if completed.returncode == 0:
        return "passed", "target packages compile"
    tail = "\n".join(completed.stdout.splitlines()[-20:])
    message = "target package compilation failed"
    return "failed", message + (f":\n{tail}" if tail else "")


def evaluate(config: dict[str, Any], repo: Path, output: Path, apply_failed: bool) -> dict[str, Any]:
    hard_gate = config.get("hard_gate")
    if not isinstance(hard_gate, dict):
        raise GateError("config.hard_gate must be an object")
    base_commit = config.get("base_commit")
    if not isinstance(base_commit, str) or not base_commit:
        raise GateError("config.base_commit must be a non-empty string")

    settings: dict[str, list[str]] = {}
    for label in (
        "required_checks",
        "compile_paths",
    ):
        value = hard_gate.get(label)
        if not isinstance(value, list) or not value or not all(
            isinstance(item, str) and item for item in value
        ):
            raise GateError(f"config.hard_gate.{label} must be a non-empty string list")
        if len(value) != len(set(value)):
            raise GateError(f"config.hard_gate.{label} contains duplicates")
        settings[label] = value
    blocked_rules = _blocked_path_rules(hard_gate.get("blocked_paths"))
    cheat_checks = hard_gate.get("cheat_nodes")
    if set(cheat_checks or []) != CHEAT_CHECKS:
        raise GateError("config.hard_gate.cheat_nodes does not match implemented cheat checks")

    repo = repo.resolve(strict=True)
    if not repo.is_dir():
        raise GateError("candidate repository is not a directory")
    try:
        output.parent.resolve(strict=False).relative_to(repo)
    except ValueError:
        pass
    else:
        raise GateError("hard-gate report must be evaluator-owned")
    base = _git(repo, "rev-parse", "--verify", f"{base_commit}^{{commit}}")
    if base.returncode != 0:
        raise GateError("configured base commit is unavailable")

    changed = _changed_paths(repo, base_commit)
    modes = _index_modes(repo, changed)
    tracked = {
        path: _tracked_at_base(repo, base_commit, path)
        for path in changed
    }
    matching_rules = {
        path: [rule for rule in blocked_rules if fnmatch.fnmatchcase(path, rule["pattern"])]
        for path in changed
    }
    # An addition is exempt only when every matching rule permits it. A
    # protected evaluator directory therefore overrides the new-test exception.
    safe_test_additions = sorted(
        path
        for path in changed
        if matching_rules[path]
        and not tracked[path]
        and all(rule.get("allow_additions", False) for rule in matching_rules[path])
        and modes.get(path) in {"100644", "100755"}
    )
    scope_violations = sorted(
        path for path, mode in modes.items() if mode not in {"100644", "100755"}
    )
    protected = sorted(
        path
        for path in changed
        if matching_rules[path] and path not in safe_test_additions
    )
    if apply_failed or protected or scope_violations:
        compile_status = "failed"
        compile_message = "compilation skipped because candidate integrity checks failed"
    else:
        _discard_candidate_test_additions(repo, safe_test_additions)
        compile_status, compile_message = _compile(repo, settings["compile_paths"])

    tests = [
        _test("target_modules_compile", compile_status, compile_message),
        _test(
            "candidate_scope_valid",
            "passed" if not scope_violations else "failed",
            "candidate changes contain only regular files or deletions"
            if not scope_violations
            else "candidate includes symlinks or other non-regular files",
            violations=scope_violations,
        ),
        _test(
            "protected_assets_unchanged",
            "passed" if not protected else "failed",
            "protected tests, verifier files, and dependencies are unchanged"
            if not protected
            else "candidate changed protected assets",
            violations=protected,
        ),
    ]
    observed = {entry["testId"] for entry in tests}
    if set(settings["required_checks"]) != observed:
        raise GateError("config.hard_gate.required_checks does not match implemented checks")

    failed_ids = [entry["testId"] for entry in tests if entry["status"] != "passed"]
    cheat_nodes = sorted(CHEAT_CHECKS.intersection(failed_ids))
    infrastructure_error = any(entry["status"] == "other" for entry in tests)
    passed = not apply_failed and not failed_ids
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "INFRA_ERROR" if infrastructure_error else ("PASS" if passed else "FAIL"),
        "passed": passed,
        "apply_failed": apply_failed,
        "cheat_detected": bool(cheat_nodes),
        "cheat_nodes": cheat_nodes,
        "failed_test_ids": failed_ids,
        "base_commit": base_commit,
        "changed_files": changed,
        "ignored_candidate_test_additions": safe_test_additions,
        "tests": tests,
    }


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".hard-gate-", suffix=".json", dir=path.parent)
    try:
        os.fchmod(fd, 0o644)
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def _infra_result(config: dict[str, Any] | None, apply_failed: bool, error: Exception) -> dict[str, Any]:
    required = []
    if isinstance(config, dict):
        value = (config.get("hard_gate") or {}).get("required_checks")
        if isinstance(value, list) and all(isinstance(item, str) for item in value):
            required = value
    tests = [
        _test(test_id, "other", "hard gate could not evaluate candidate")
        for test_id in required
    ]
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "INFRA_ERROR",
        "passed": False,
        "apply_failed": apply_failed,
        "cheat_detected": False,
        "cheat_nodes": [],
        "failed_test_ids": required,
        "tests": tests,
        "error": f"{type(error).__name__}: {error}",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args()
    config: dict[str, Any] | None = None
    try:
        config = json.loads(args.config.read_text(encoding="utf-8"))
        if not isinstance(config, dict):
            raise GateError("config must contain a JSON object")
        result = evaluate(config, args.repo, args.output, bool(args.apply_failed))
    except (GateError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        result = _infra_result(config, bool(args.apply_failed), exc)
    _write_json(args.output, result)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
