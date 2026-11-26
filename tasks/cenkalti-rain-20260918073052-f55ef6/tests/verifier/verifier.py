#!/usr/bin/env python3
"""Task-specific F2P/P2P verifier entrypoint."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path


P2P: list[str] = []
F2P: list[str] = []


def parse_go_test_events(
    stdout: str,
    stderr: str,
    returncode: int,
    config: dict,
    hg_data: dict,
    start_time: int | None = None,
    stop_time: int | None = None,
) -> dict:
    P2P = [str(node) for node in config.get("p2p", [])]
    F2P = [str(node) for node in config.get("f2p", [])]
    all_registered_nodes = P2P + F2P

    node_to_target = {}
    node_group = {}
    for node in P2P:
        node_group[node] = "P2P"
        parts = node.split("::")
        if len(parts) == 2:
            rel_file, test_name = parts
            if rel_file.startswith("github.com/cenkalti/rain/v2"):
                pkg = rel_file
            else:
                rel_dir = os.path.dirname(rel_file)
                pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")
            node_to_target[node] = (pkg, test_name)
    for node in F2P:
        node_group[node] = "F2P"
        parts = node.split("::")
        if len(parts) == 2:
            rel_file, test_name = parts
            if rel_file.startswith("github.com/cenkalti/rain/v2"):
                pkg = rel_file
            else:
                rel_dir = os.path.dirname(rel_file)
                pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")
            node_to_target[node] = (pkg, test_name)

    pkg_status: dict[str, str] = {}
    pkg_errors: dict[str, list[str]] = {}
    started_pkgs: set[str] = set()
    started_tests: set[tuple[str, str]] = set()
    test_status: dict[tuple[str, str], str] = {}
    test_duration: dict[tuple[str, str], float] = {}
    test_messages: dict[tuple[str, str], list[str]] = {}
    duplicate_terminal_tests: set[tuple[str, str]] = set()
    conflicting_tests: set[tuple[str, str]] = set()
    duplicate_terminal_pkgs: set[str] = set()
    conflicting_pkgs: set[str] = set()

    for line in stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except Exception:
            continue

        action = event.get("Action")
        pkg = event.get("Package")
        test = event.get("Test")
        if not pkg:
            continue

        if test:
            key = (pkg, test)
            if action == "run":
                started_tests.add(key)
            elif action in ("pass", "fail", "skip"):
                if key in test_status:
                    old_action = test_status[key]
                    if old_action != action:
                        conflicting_tests.add(key)
                    else:
                        duplicate_terminal_tests.add(key)
                    if old_action == "fail":
                        action = "fail"
                test_status[key] = action
                if "Elapsed" in event:
                    test_duration[key] = float(event["Elapsed"])
            elif action == "output" and "Output" in event:
                test_messages.setdefault(key, []).append(event["Output"])
        else:
            if action == "start":
                started_pkgs.add(pkg)
            elif action in ("pass", "fail", "skip"):
                if pkg in pkg_status:
                    old_action = pkg_status[pkg]
                    if old_action != action:
                        conflicting_pkgs.add(pkg)
                    else:
                        duplicate_terminal_pkgs.add(pkg)
                    if old_action == "fail":
                        action = "fail"
                pkg_status[pkg] = action
            elif action == "output" and "Output" in event:
                pkg_errors.setdefault(pkg, []).append(event["Output"])

    # Check command-level failure: non-zero return code MUST fail verification
    cmd_failed = returncode != 0
    cmd_failure_reason = ""
    if cmd_failed:
        cmd_err_sample = (stderr or "").strip()
        if not cmd_err_sample:
            # Check package-level errors
            all_errs = [
                "".join(errs)
                for errs in pkg_errors.values()
                if "".join(errs).strip()
            ]
            cmd_err_sample = "; ".join(all_errs)[:500] if all_errs else "no output"
        cmd_failure_reason = (
            f"go test command failed with exit code {returncode}: {cmd_err_sample[:200]}"
        )

    # Evaluate status for each registered node
    hg_p2p_info = hg_data.get("categories", {}).get("p2p", {})
    hg_p2p_passed = hg_data.get("p2p_passed", False) or hg_p2p_info.get("passed", False) or hg_data.get("passed", False)
    hg_passed_p2p_nodes = set(
        hg_p2p_info.get("details", {}).get("passed_p2p_nodes", [])
        or hg_data.get("passed_nodes", [])
    )

    if start_time is None:
        start_time = int(time.time() * 1000)
    if stop_time is None:
        stop_time = int(time.time() * 1000)

    ctrf_tests = []
    summary_counts = {
        "tests": 0,
        "passed": 0,
        "failed": 0,
        "skipped": 0,
        "pending": 0,
        "other": 0,
        "start": start_time,
        "stop": stop_time,
    }

    for node in all_registered_nodes:
        group = node_group.get(node, "UNKNOWN")
        pkg, test_name = node_to_target.get(node, ("", ""))
        key = (pkg, test_name)

        status = "failed"
        message = ""
        duration = 0

        if not pkg or not test_name:
            status = "failed"
            message = f"Invalid node identifier format: {node}"
        elif key in conflicting_tests:
            status = "failed"
            message = f"Conflicting terminal results observed for node: {node}"
            if key in test_duration:
                duration = int(test_duration[key] * 1000)
        elif key in duplicate_terminal_tests:
            status = "failed"
            message = f"Duplicate terminal result observed for node: {node}"
            if key in test_duration:
                duration = int(test_duration[key] * 1000)
        elif key in test_status:
            action = test_status[key]
            duration = int(test_duration.get(key, 0.0) * 1000)
            if action == "pass":
                pkg_has_failing_test = any(
                    k[0] == pkg and test_status.get(k) == "fail" for k in test_status
                )
                if pkg_status.get(pkg) == "fail" and not pkg_has_failing_test:
                    status = "failed"
                    pkg_out = "".join(pkg_errors.get(pkg, []))
                    message = (
                        f"Package {pkg} failed abnormally after tests completed "
                        f"(TestMain or teardown failure): {pkg_out[:500]}"
                    )
                else:
                    status = "passed"
            elif action == "skip":
                status = "skipped"
                message = "".join(test_messages.get(key, []))
            else:
                status = "failed"
                message = "".join(test_messages.get(key, []))
        elif group == "P2P" and hg_p2p_passed and node in hg_passed_p2p_nodes:
            status = "passed"
            message = "Independently verified by Hard Gate P2P execution"
        elif pkg_status.get(pkg) == "fail":
            status = "failed"
            pkg_out = "".join(pkg_errors.get(pkg, []))
            message = f"Package {pkg} failed before test completed: {pkg_out[:500]}"
        elif cmd_failed:
            status = "failed"
            message = f"Test node was not executed due to command failure: {cmd_failure_reason}"
        else:
            status = "failed"
            message = f"Test node was not observed during test execution: {node}"

        summary_counts["tests"] += 1
        summary_counts[status] = summary_counts.get(status, 0) + 1

        ctrf_entry = {
            "name": node,
            "status": status,
            "duration": int(duration),
            "testId": node,
            "extra": {
                "deepswe": {
                    "group": group,
                    "required": True,
                }
            },
        }
        if message:
            ctrf_entry["message"] = message[:2000]
        ctrf_tests.append(ctrf_entry)

    # Collect unregistered test failures and package failures for execution-level diagnostics
    registered_keys = {node_to_target[node] for node in all_registered_nodes if node in node_to_target}
    unregistered_failures = [
        f"{pkg}::{test}"
        for (pkg, test), status in test_status.items()
        if status == "fail" and (pkg, test) not in registered_keys
    ]
    registered_failures = [
        node
        for node in all_registered_nodes
        if test_status.get(node_to_target.get(node, ("", ""))) == "fail"
    ]

    # Detect abnormal package failures (e.g. teardown panics, TestMain failures, build crashes)
    abnormal_package_failures = []
    for pkg, status in pkg_status.items():
        if status == "fail":
            pkg_tests_failed = any(
                k[0] == pkg and s == "fail" for k, s in test_status.items()
            )
            pkg_out = "".join(pkg_errors.get(pkg, []))
            has_abnormal_output = any(
                sig in pkg_out for sig in ("panic:", "fatal error:", "SIGSEGV", "SIGBUS", "goleak:", "[build failed]", "WARNING: DATA RACE")
            )
            if not pkg_tests_failed or has_abnormal_output:
                abnormal_package_failures.append(pkg)

    # Incomplete execution check: registered nodes that were not observed with terminal outcome
    incomplete_nodes = [
        node
        for node in all_registered_nodes
        if node_to_target.get(node) not in test_status
        and not (node_group.get(node) == "P2P" and hg_p2p_passed and node in hg_passed_p2p_nodes)
    ]

    # Incomplete execution check: any started test or package (registered or unregistered) without terminal outcome
    unterminated_tests = [
        f"{pkg}::{test}"
        for (pkg, test) in sorted(started_tests)
        if (pkg, test) not in test_status
    ]
    unterminated_packages = [
        pkg
        for pkg in sorted(started_pkgs)
        if pkg not in pkg_status
    ]

    is_unexplained_process = False
    if returncode != 0:
        if returncode != 1:
            is_unexplained_process = True
        elif not registered_failures and not unregistered_failures and not abnormal_package_failures:
            is_unexplained_process = True

    execution_abnormality = bool(
        unregistered_failures
        or abnormal_package_failures
        or incomplete_nodes
        or unterminated_tests
        or unterminated_packages
        or is_unexplained_process
        or conflicting_tests
        or duplicate_terminal_tests
        or conflicting_pkgs
        or duplicate_terminal_pkgs
    )

    task_id = str(config.get("task_id") or config.get("taskId") or "")
    base_commit = str(config.get("base_commit") or config.get("baseCommit") or "")
    reward_mode = str(config.get("reward_mode") or config.get("rewardMode") or "VERIFIER_ONLY")
    reward_policy = str(config.get("reward_policy") or config.get("rewardPolicy") or "deterministic_verifier_only")
    suite = str(config.get("suite") or "")

    return {
        "reportFormat": "CTRF",
        "specVersion": "0.0.1",
        "results": {
            "tool": {"name": "deepswe-go-verifier"},
            "summary": summary_counts,
            "tests": ctrf_tests,
            "extra": {
                "deepswe": {
                    "taskId": task_id,
                    "task_id": task_id,
                    "baseCommit": base_commit,
                    "base_commit": base_commit,
                    "rewardMode": reward_mode,
                    "reward_mode": reward_mode,
                    "rewardPolicy": reward_policy,
                    "reward_policy": reward_policy,
                    "suite": suite,
                    "cmd_returncode": returncode,
                    "cmd_failed": cmd_failed,
                    "cmd_failure_reason": cmd_failure_reason,
                    "is_unexplained_process": is_unexplained_process,
                    "unregistered_failures": unregistered_failures,
                    "abnormal_package_failures": abnormal_package_failures,
                    "package_failures": abnormal_package_failures,
                    "incomplete_nodes": incomplete_nodes,
                    "unterminated_tests": unterminated_tests,
                    "unterminated_packages": unterminated_packages,
                    "conflicting_tests": [f"{pkg}::{t}" for (pkg, t) in sorted(conflicting_tests)],
                    "duplicate_terminal_tests": [f"{pkg}::{t}" for (pkg, t) in sorted(duplicate_terminal_tests)],
                    "conflicting_pkgs": sorted(conflicting_pkgs),
                    "duplicate_terminal_pkgs": sorted(duplicate_terminal_pkgs),
                    "execution_abnormality": execution_abnormality,
                }
            },
        }
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--ctrf-output", type=Path, required=True)
    parser.add_argument("--hard-gate-output", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args(argv)

    config = json.loads(args.config.read_text(encoding="utf-8"))

    global P2P, F2P
    P2P = [str(node) for node in config.get("p2p", [])]
    F2P = [str(node) for node in config.get("f2p", [])]
    all_registered_nodes = P2P + F2P
    if not all_registered_nodes:
        raise SystemExit("Error: Empty test selection configured. At least one test node must be registered.")

    node_group = {n: "P2P" for n in P2P}
    node_group.update({n: "F2P" for n in F2P})

    # 1. Execute hardgate.py (stale pre-existing output must not substitute for current execution)
    if args.hard_gate_output.exists():
        try:
            args.hard_gate_output.unlink()
        except OSError:
            pass

    hardgate_script = Path(__file__).parent / "hardgate.py"
    cmd_hardgate = [
        sys.executable,
        str(hardgate_script),
        "--config",
        str(args.config),
        "--repo",
        str(args.repo),
        "--output",
        str(args.hard_gate_output),
        "--apply-failed",
        str(args.apply_failed),
    ]
    try:
        hg_proc = subprocess.run(cmd_hardgate, capture_output=True, text=True)
    except Exception as e:
        raise SystemExit(f"Infrastructure failure: failed to invoke hardgate.py: {e}")

    if hg_proc.returncode != 0:
        raise SystemExit(
            f"Infrastructure failure: hardgate.py exited with non-zero code {hg_proc.returncode}. "
            f"Stderr: {hg_proc.stderr}"
        )

    if not args.hard_gate_output.exists():
        raise SystemExit(
            f"Infrastructure failure: hardgate.py did not produce expected output at {args.hard_gate_output}"
        )

    try:
        hg_data = json.loads(args.hard_gate_output.read_text(encoding="utf-8"))
    except Exception as e:
        raise SystemExit(
            f"Infrastructure failure: hardgate output is not valid JSON ({e})"
        )

    # 2. Check Hard Gate outcome
    if not hg_data.get("passed", False):
        failed_gate_nodes = hg_data.get("failed_nodes", [])
        gate_msg = f"Hard gate failed: {', '.join(failed_gate_nodes)}"

        diagnostics = config.get("diagnostics", {})
        if "verifier" in diagnostics:
            try:
                diag_path = Path(diagnostics["verifier"])
                diag_path.parent.mkdir(parents=True, exist_ok=True)
                diag_payload = {
                    "phase": "hard_gate",
                    "command": cmd_hardgate,
                    "passed": False,
                    "failed_nodes": failed_gate_nodes,
                }
                diag_path.write_text(
                    json.dumps(diag_payload, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
            except Exception:
                pass

        ctrf_tests = []
        for node in all_registered_nodes:
            ctrf_tests.append(
                {
                    "name": node,
                    "status": "failed",
                    "duration": 0,
                    "testId": node,
                    "message": gate_msg,
                    "extra": {
                        "deepswe": {
                            "group": node_group[node],
                            "required": True,
                        }
                    },
                }
            )

        now_ts = int(time.time() * 1000)
        task_id = str(config.get("task_id") or config.get("taskId") or "")
        base_commit = str(config.get("base_commit") or config.get("baseCommit") or "")
        reward_mode = str(config.get("reward_mode") or config.get("rewardMode") or "VERIFIER_ONLY")
        reward_policy = str(config.get("reward_policy") or config.get("rewardPolicy") or "deterministic_verifier_only")
        suite = str(config.get("suite") or "")
        ctrf_report = {
            "reportFormat": "CTRF",
            "specVersion": "0.0.1",
            "results": {
                "tool": {"name": "deepswe-go-verifier"},
                "summary": {
                    "tests": len(ctrf_tests),
                    "passed": 0,
                    "failed": len(ctrf_tests),
                    "skipped": 0,
                    "pending": 0,
                    "other": 0,
                    "start": now_ts,
                    "stop": now_ts,
                },
                "tests": ctrf_tests,
                "extra": {
                    "deepswe": {
                        "taskId": task_id,
                        "task_id": task_id,
                        "baseCommit": base_commit,
                        "base_commit": base_commit,
                        "rewardMode": reward_mode,
                        "reward_mode": reward_mode,
                        "rewardPolicy": reward_policy,
                        "reward_policy": reward_policy,
                        "suite": suite,
                        "hard_gate_passed": False,
                        "failed_gate_nodes": failed_gate_nodes,
                    }
                },
            },
        }
        args.ctrf_output.parent.mkdir(parents=True, exist_ok=True)
        args.ctrf_output.write_text(
            json.dumps(ctrf_report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return 0

    # 3. Execute Go test suite
    test_start_ts = int(time.time() * 1000)
    test_cmd = ["go", "test", "-race", "-count=1", "-json", "./..."]
    timeout_sec = int(config.get("timeout_sec", 600))
    try:
        test_proc = subprocess.run(
            test_cmd,
            cwd=args.repo,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
        )
        test_stop_ts = int(time.time() * 1000)
        test_stdout = test_proc.stdout
        test_stderr = test_proc.stderr
        test_rc = test_proc.returncode
    except subprocess.TimeoutExpired as e:
        test_stop_ts = int(time.time() * 1000)
        test_stdout = (e.stdout or "") if isinstance(e.stdout, str) else (e.stdout or b"").decode("utf-8", errors="replace")
        test_stderr = ((e.stderr or "") if isinstance(e.stderr, str) else (e.stderr or b"").decode("utf-8", errors="replace")) + f"\nTest execution timed out after {timeout_sec}s"
        test_rc = 124

    diagnostics = config.get("diagnostics", {})
    if "verifier" in diagnostics:
        try:
            diag_path = Path(diagnostics["verifier"])
            diag_path.parent.mkdir(parents=True, exist_ok=True)
            diag_payload = {
                "phase": "go_test",
                "command": test_cmd,
                "returncode": test_rc,
                "stdout": test_stdout[:5000],
                "stderr": test_stderr[:5000],
            }
            diag_path.write_text(
                json.dumps(diag_payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        except Exception:
            pass

    # 4. Parse test results
    ctrf_report = parse_go_test_events(
        stdout=test_stdout,
        stderr=test_stderr,
        returncode=test_rc,
        config=config,
        hg_data=hg_data,
        start_time=test_start_ts,
        stop_time=test_stop_ts,
    )

    # 5. Propagate execution abnormalities to the Hardgate report contract
    extra = ctrf_report.get("results", {}).get("extra", {}).get("deepswe", {})
    execution_abnormality = extra.get("execution_abnormality", False)

    if execution_abnormality:
        # Construct explicit execution diagnostics and failure identifiers
        abnormality_failures = []
        for uf in extra.get("unregistered_failures", []):
            abnormality_failures.append(f"unregistered_failure:{uf}")

        for apf in extra.get("abnormal_package_failures", []):
            abnormality_failures.append(f"abnormal_package_failure:{apf}")

        for inc in extra.get("incomplete_nodes", []):
            abnormality_failures.append(f"incomplete_node:{inc}")

        for ut in extra.get("unterminated_tests", []):
            abnormality_failures.append(f"unterminated_test:{ut}")

        for up in extra.get("unterminated_packages", []):
            abnormality_failures.append(f"unterminated_package:{up}")

        for ct in extra.get("conflicting_tests", []):
            abnormality_failures.append(f"conflicting_test:{ct}")

        for dt in extra.get("duplicate_terminal_tests", []):
            abnormality_failures.append(f"duplicate_terminal_test:{dt}")

        for cp in extra.get("conflicting_pkgs", []):
            abnormality_failures.append(f"conflicting_package:{cp}")

        for dp in extra.get("duplicate_terminal_pkgs", []):
            abnormality_failures.append(f"duplicate_terminal_package:{dp}")

        if extra.get("is_unexplained_process"):
            ret = extra.get("cmd_returncode", test_rc)
            abnormality_failures.append(f"unexplained_process_failure:exit_code_{ret}")

        if not abnormality_failures:
            abnormality_failures.append("execution_abnormality")

        # Invalidate Hardgate report while preserving original build, anti-cheat, and P2P evidence
        hg_data["passed"] = False
        hg_data["execution_passed"] = False

        existing_failed = hg_data.get("failed_nodes", [])
        hg_data["failed_nodes"] = list(dict.fromkeys(existing_failed + abnormality_failures))

        hg_data.setdefault("categories", {})
        hg_data["categories"]["execution"] = {
            "passed": False,
            "failed_nodes": abnormality_failures,
            "details": {
                "cmd_returncode": test_rc,
                "cmd_failed": test_rc != 0,
                "diagnostics": {
                    "unregistered_failures": extra.get("unregistered_failures", []),
                    "abnormal_package_failures": extra.get("abnormal_package_failures", []),
                    "incomplete_nodes": extra.get("incomplete_nodes", []),
                    "unterminated_tests": extra.get("unterminated_tests", []),
                    "unterminated_packages": extra.get("unterminated_packages", []),
                    "conflicting_tests": extra.get("conflicting_tests", []),
                    "duplicate_terminal_tests": extra.get("duplicate_terminal_tests", []),
                    "conflicting_pkgs": extra.get("conflicting_pkgs", []),
                    "duplicate_terminal_pkgs": extra.get("duplicate_terminal_pkgs", []),
                    "is_unexplained_process": extra.get("is_unexplained_process", False),
                },
            },
        }
        hg_data.setdefault("summary", {})
        hg_data["summary"]["execution"] = "FAILED"

        args.hard_gate_output.write_text(
            json.dumps(hg_data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    else:
        # Complete execution without abnormality: Hardgate remains valid
        hg_data["execution_passed"] = True
        hg_data.setdefault("categories", {})
        hg_data["categories"]["execution"] = {
            "passed": True,
            "failed_nodes": [],
            "details": {
                "cmd_returncode": test_rc,
                "cmd_failed": test_rc != 0,
            },
        }
        hg_data.setdefault("summary", {})
        hg_data["summary"]["execution"] = "PASSED"
        args.hard_gate_output.write_text(
            json.dumps(hg_data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    args.ctrf_output.parent.mkdir(parents=True, exist_ok=True)
    args.ctrf_output.write_text(
        json.dumps(ctrf_report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
