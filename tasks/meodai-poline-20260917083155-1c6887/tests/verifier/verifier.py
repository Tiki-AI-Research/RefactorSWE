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
from typing import Any

# Import run_hard_gate and related helpers from hardgate.py
sys.path.insert(0, str(Path(__file__).parent))
try:
    from hardgate import (
        run_hard_gate,
        validate_hard_gate_schema,
        get_environment_with_node_modules,
        sanitize_message,
        REQUIRED_CHEAT_NODE_IDS,
        ARCHITECTURE_F2P_NODE_ID,
        create_architecture_f2p_entry,
    )
except ImportError:
    from case.tests.verifier.hardgate import (
        run_hard_gate,
        validate_hard_gate_schema,
        get_environment_with_node_modules,
        sanitize_message,
        REQUIRED_CHEAT_NODE_IDS,
        ARCHITECTURE_F2P_NODE_ID,
        create_architecture_f2p_entry,
    )


class InfrastructureError(Exception):
    """Exception raised when verifier encounters an infrastructure, toolchain, or system failure."""

    def __init__(
        self,
        error_type: str,
        message: str,
        details: dict[str, Any] | None = None,
    ):
        super().__init__(message)
        self.error_type = error_type
        self.message = message
        self.details = details or {}


VALID_CTRF_STATUSES = {"passed", "failed", "skipped", "pending", "other"}


def run_f2p_tests(
    repo_dir: Path,
    timeout: float = 120.0,
) -> tuple[list[str], dict[str, list[dict[str, Any]]]]:
    """Execute F2P tests via Vitest and collect raw results with full test ID tracking."""
    cmd_env = get_environment_with_node_modules(repo_dir)
    cmd_env["PICKER_TEST_FILTER"] = "F2P"
    test_file = repo_dir / "tests" / "deep_swe_verifier_poline_picker.test.ts"
    if not test_file.is_file():
        raise InfrastructureError(
            "TEST_FILE_MISSING",
            f"F2P test file {test_file} does not exist in repository",
        )

    cmd = ["npx", "vitest", "run", "tests/deep_swe_verifier_poline_picker.test.ts", "-t", "F2P::", "--reporter=json"]
    try:
        proc = subprocess.run(
            cmd,
            cwd=repo_dir,
            env=cmd_env,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as te:
        raise InfrastructureError(
            "TIMEOUT",
            f"Vitest F2P execution timed out after {timeout} seconds",
            {"timeout": timeout},
        ) from te
    except (FileNotFoundError, PermissionError) as pe:
        raise InfrastructureError(
            "EXECUTABLE_UNAVAILABLE",
            f"Failed to launch Vitest F2P runner: {pe}",
            {"error": str(pe)},
        ) from pe
    except Exception as e:
        raise InfrastructureError(
            "PROCESS_LAUNCH_ERROR",
            f"Failed to execute Vitest F2P tests: {e}",
            {"error": str(e)},
        ) from e

    if proc.returncode in (126, 127):
        raise InfrastructureError(
            "EXECUTABLE_UNAVAILABLE",
            f"Vitest F2P runner unavailable (exit code {proc.returncode})",
            {"exit_code": proc.returncode, "stderr": sanitize_message(proc.stderr)},
        )
    if proc.returncode < 0:
        raise InfrastructureError(
            "PROCESS_SIGNAL_TERMINATED",
            f"Vitest F2P runner terminated abnormally by signal {abs(proc.returncode)}",
            {"signal": abs(proc.returncode)},
        )

    stdout = proc.stdout.strip()
    if not stdout:
        raise InfrastructureError(
            "NO_STDOUT",
            f"Vitest exited with code {proc.returncode} but produced no JSON output on stdout. Stderr: {sanitize_message(proc.stderr)}",
            {"exit_code": proc.returncode, "stderr": sanitize_message(proc.stderr)},
        )

    try:
        vitest_json = json.loads(stdout)
    except Exception as e:
        raise InfrastructureError(
            "MALFORMED_JSON",
            f"Failed to parse Vitest JSON output: {e}. Raw stdout: {sanitize_message(stdout[:300])}",
            {"stdout_snippet": sanitize_message(stdout[:300])},
        ) from e

    raw_f2p_ids: list[str] = []
    raw_f2p_records_by_id: dict[str, list[dict[str, Any]]] = {}

    test_results = vitest_json.get("testResults", [])
    for test_file_res in test_results:
        for a in test_file_res.get("assertionResults", []):
            test_id = str(a.get("title", "")).strip()
            raw_status = str(a.get("status", "failed"))
            duration = float(a.get("duration", 0) or 0)
            fail_msgs = a.get("failureMessages", [])

            raw_f2p_ids.append(test_id)
            if test_id not in raw_f2p_records_by_id:
                raw_f2p_records_by_id[test_id] = []
            raw_f2p_records_by_id[test_id].append({
                "testId": test_id,
                "name": test_id.split("::")[-1] if "::" in test_id else test_id,
                "status": raw_status,
                "duration": duration,
                "failureMessages": fail_msgs,
            })

    if len(raw_f2p_ids) == 0:
        raise InfrastructureError(
            "ZERO_TESTS_COLLECTED",
            "Vitest F2P runner collected 0 tests due to launch or runner configuration failure",
        )

    return raw_f2p_ids, raw_f2p_records_by_id


def validate_ctrf_report_integrity(
    ctrf: dict[str, Any],
    config: dict[str, Any],
) -> list[str]:
    """Strictly validate CTRF report schema, types, node set equality, groups, statuses, and summary consistency."""
    errors: list[str] = []

    if not isinstance(ctrf, dict):
        return ["CTRF root must be a dict"]

    if ctrf.get("reportFormat") != "CTRF":
        errors.append(f"Invalid or missing reportFormat: expected 'CTRF', got {ctrf.get('reportFormat')!r}")

    if not isinstance(ctrf.get("specVersion"), str):
        errors.append("Missing or invalid specVersion (must be string)")

    results = ctrf.get("results")
    if not isinstance(results, dict):
        return errors + ["Missing or invalid results object"]

    tool = results.get("tool")
    if not isinstance(tool, dict) or not isinstance(tool.get("name"), str) or not tool["name"].strip():
        errors.append("Missing or invalid results.tool.name")

    summary = results.get("summary")
    if not isinstance(summary, dict):
        errors.append("Missing or invalid results.summary object")

    tests = results.get("tests")
    if not isinstance(tests, list):
        errors.append("Missing or invalid results.tests list")
        return errors

    if not isinstance(config, dict):
        return errors + ["Config must be a dict"]

    raw_f2p = config.get("f2p")
    raw_p2p = config.get("p2p")
    if not isinstance(raw_f2p, list) or not isinstance(raw_p2p, list):
        return errors + ["Config missing required 'f2p' or 'p2p' list"]

    expected_f2p = [str(n) for n in raw_f2p]
    expected_p2p = [str(n) for n in raw_p2p]
    expected_f2p_set = set(expected_f2p)
    expected_p2p_set = set(expected_p2p)
    expected_all_set = expected_f2p_set | expected_p2p_set

    actual_ids: list[str] = []
    seen_ids: set[str] = set()
    status_counts: dict[str, int] = {st: 0 for st in VALID_CTRF_STATUSES}

    for idx, t in enumerate(tests):
        if not isinstance(t, dict):
            errors.append(f"tests[{idx}] must be a dict")
            continue

        tid = t.get("testId")
        if not isinstance(tid, str) or not tid.strip():
            errors.append(f"tests[{idx}] missing or invalid testId")
            continue

        if tid in seen_ids:
            errors.append(f"Duplicate CTRF node: '{tid}'")
        seen_ids.add(tid)
        actual_ids.append(tid)

        name = t.get("name")
        if not isinstance(name, str):
            errors.append(f"tests[{idx}] ('{tid}') missing or invalid name")

        dur = t.get("duration")
        if not isinstance(dur, (int, float)) or isinstance(dur, bool) or dur < 0:
            errors.append(f"tests[{idx}] ('{tid}') duration must be non-negative number, got {dur!r}")

        st = t.get("status")
        if not isinstance(st, str) or st not in VALID_CTRF_STATUSES:
            errors.append(
                f"Invalid CTRF status {st!r} for test '{tid}'; must be one of {sorted(VALID_CTRF_STATUSES)}"
            )
        else:
            status_counts[st] += 1

        # Group verification
        extra = t.get("extra")
        if not isinstance(extra, dict):
            errors.append(f"tests[{idx}] ('{tid}') missing or invalid 'extra' object")
            deepswe = None
        else:
            deepswe = extra.get("deepswe")
            if not isinstance(deepswe, dict):
                errors.append(f"tests[{idx}] ('{tid}') missing or invalid 'extra.deepswe' object")

        group = deepswe.get("group") if isinstance(deepswe, dict) else None
        if not isinstance(group, str) or group not in {"P2P", "F2P"}:
            errors.append(f"Wrong CTRF group for test '{tid}': expected 'P2P' or 'F2P', got {group!r}")
        elif tid in expected_f2p_set and group != "F2P":
            errors.append(f"Wrong CTRF group for F2P test '{tid}': expected 'F2P', got '{group}'")
        elif tid in expected_p2p_set and group != "P2P":
            errors.append(f"Wrong CTRF group for P2P test '{tid}': expected 'P2P', got '{group}'")
        elif tid not in expected_all_set:
            errors.append(f"Unrecognized testId '{tid}' does not belong to configured F2P or P2P nodes")

    actual_set = set(actual_ids)
    missing = sorted(expected_all_set - actual_set)
    extra = sorted(actual_set - expected_all_set)

    if missing:
        errors.append(f"Missing CTRF nodes ({len(missing)}): {missing[:5]}")
    if extra:
        errors.append(f"Extra unexpected CTRF nodes ({len(extra)}): {extra[:5]}")
    if len(actual_ids) != len(expected_all_set):
        errors.append(f"Total test count mismatch: expected {len(expected_all_set)}, got {len(actual_ids)}")

    # Summary consistency
    if isinstance(summary, dict):
        total_declared = summary.get("tests")
        if not isinstance(total_declared, int) or isinstance(total_declared, bool) or total_declared != len(tests):
            errors.append(f"Summary total tests ({total_declared}) does not match actual tests count ({len(tests)})")

        for st in VALID_CTRF_STATUSES:
            if st in summary:
                declared = summary[st]
                actual = status_counts[st]
                if not isinstance(declared, int) or isinstance(declared, bool) or declared != actual:
                    errors.append(f"Summary count mismatch for '{st}': declared {declared}, actual {actual}")

    return errors


def generate_ctrf_report(
    config: dict[str, Any],
    hard_gate_result: dict[str, Any],
    f2p_execution_data: tuple[list[str], dict[str, list[dict[str, Any]]]] | None,
    ctrf_output_path: Path,
    hard_gate_passed: bool,
) -> dict[str, Any]:
    p2p_nodes = [str(n) for n in config.get("p2p", [])]
    f2p_nodes = [str(n) for n in config.get("f2p", [])]

    # Map P2P results from hard gate
    p2p_results_by_id: dict[str, dict[str, Any]] = {
        r["testId"]: r for r in hard_gate_result.get("p2p_results", [])
    }

    tests_list: list[dict[str, Any]] = []

    # 1. P2P nodes (ordered as declared in config)
    for test_id in p2p_nodes:
        if test_id in p2p_results_by_id:
            res = p2p_results_by_id[test_id]
            status = res.get("status") if "status" in res else "failed"
            duration = float(res.get("duration", 0) or 0)
            entry: dict[str, Any] = {
                "testId": test_id,
                "name": test_id.split("::")[-1],
                "status": status,
                "duration": duration,
                "extra": {
                    "deepswe": {
                        "group": "P2P",
                        "required": True,
                    }
                },
            }
            if status != "passed":
                fail_msgs = res.get("failureMessages", [])
                entry["message"] = (
                    fail_msgs[0] if fail_msgs else "P2P test assertion failed"
                )
            tests_list.append(entry)
        else:
            tests_list.append({
                "testId": test_id,
                "name": test_id.split("::")[-1],
                "status": "failed",
                "duration": 0,
                "message": "P2P test was not executed due to prior verification failure",
                "extra": {
                    "deepswe": {
                        "group": "P2P",
                        "required": True,
                    }
                },
            })

    # Include any extra P2P test results that were executed
    executed_p2p_ids = [str(r.get("testId")) for r in hard_gate_result.get("p2p_results", [])]
    extra_p2p_ids = [tid for tid in executed_p2p_ids if tid not in p2p_nodes]
    for test_id in extra_p2p_ids:
        res = p2p_results_by_id.get(test_id, {})
        status = res.get("status") if "status" in res else "failed"
        tests_list.append({
            "testId": test_id,
            "name": test_id.split("::")[-1],
            "status": status,
            "duration": float(res.get("duration", 0) or 0),
            "extra": {
                "deepswe": {
                    "group": "P2P",
                    "required": False,
                }
            },
        })

    # 2. Strict F2P Validation & Assembly
    raw_f2p_ids: list[str] = []
    raw_f2p_records_by_id: dict[str, list[dict[str, Any]]] = {}
    duplicate_f2p_ids: list[str] = []
    missing_f2p_ids: list[str] = []
    extra_f2p_ids: list[str] = []
    p2p_collision_ids: list[str] = []
    abnormal_f2p_ids: list[str] = []

    if hard_gate_passed and f2p_execution_data is not None:
        raw_f2p_ids = list(f2p_execution_data[0])
        raw_f2p_records_by_id = {k: list(v) for k, v in f2p_execution_data[1].items()}

        # Merge architecture analysis result from hard_gate_result into F2P records
        arch_res = hard_gate_result.get("architecture_result")
        if arch_res and isinstance(arch_res, dict):
            arch_id = arch_res.get("node_id", ARCHITECTURE_F2P_NODE_ID)
            if arch_id not in raw_f2p_records_by_id:
                raw_f2p_ids.append(arch_id)
                arch_passed = bool(arch_res.get("passed"))
                arch_msg = str(arch_res.get("message", ""))
                raw_f2p_records_by_id[arch_id] = [{
                    "testId": arch_id,
                    "name": arch_id.split("::")[-1] if "::" in arch_id else arch_id,
                    "status": "passed" if arch_passed else "failed",
                    "duration": 0,
                    "failureMessages": [] if arch_passed else ([arch_msg] if arch_msg else ["Architecture separation assertion failed"]),
                }]

        # Detect internal duplicate F2P test executions
        seen_f2p: set[str] = set()
        for tid in raw_f2p_ids:
            if tid in seen_f2p and tid not in duplicate_f2p_ids:
                duplicate_f2p_ids.append(tid)
            seen_f2p.add(tid)

        # Detect collision between P2P and F2P
        p2p_collision_ids = sorted(list(set(raw_f2p_ids) & set(p2p_nodes)))

        # Detect missing F2P IDs relative to config
        missing_f2p_ids = sorted(list(set(f2p_nodes) - set(raw_f2p_ids)))

        # Detect extra F2P IDs relative to config
        extra_f2p_ids = sorted(list(set(raw_f2p_ids) - set(f2p_nodes)))

        # Detect abnormal statuses (todo, etc.)
        for tid, recs in raw_f2p_records_by_id.items():
            for r in recs:
                if r.get("status") in ("todo",):
                    if tid not in abnormal_f2p_ids:
                        abnormal_f2p_ids.append(tid)

    # Assemble configured F2P nodes in exact config order
    for test_id in f2p_nodes:
        if not hard_gate_passed:
            # Short-circuit: Hardgate failed, F2P tests were never run
            tests_list.append({
                "testId": test_id,
                "name": test_id.split("::")[-1] if "::" in test_id else test_id,
                "status": "failed",
                "duration": 0,
                "message": "F2P verification skipped due to Hard Gate failure",
                "extra": {
                    "deepswe": {
                        "group": "F2P",
                        "required": True,
                    }
                },
            })
        elif test_id in duplicate_f2p_ids:
            tests_list.append({
                "testId": test_id,
                "name": test_id.split("::")[-1] if "::" in test_id else test_id,
                "status": "failed",
                "duration": 0,
                "message": f"Duplicate F2P test ID execution detected ({raw_f2p_ids.count(test_id)} instances)",
                "extra": {
                    "deepswe": {
                        "group": "F2P",
                        "required": True,
                    }
                },
            })
        elif test_id in missing_f2p_ids:
            tests_list.append({
                "testId": test_id,
                "name": test_id.split("::")[-1] if "::" in test_id else test_id,
                "status": "failed",
                "duration": 0,
                "message": "F2P test node was not collected or executed",
                "extra": {
                    "deepswe": {
                        "group": "F2P",
                        "required": True,
                    }
                },
            })
        elif test_id in abnormal_f2p_ids:
            tests_list.append({
                "testId": test_id,
                "name": test_id.split("::")[-1] if "::" in test_id else test_id,
                "status": "failed",
                "duration": 0,
                "message": "F2P test was marked as todo",
                "extra": {
                    "deepswe": {
                        "group": "F2P",
                        "required": True,
                    }
                },
            })
        elif p2p_collision_ids:
            tests_list.append({
                "testId": test_id,
                "name": test_id.split("::")[-1] if "::" in test_id else test_id,
                "status": "failed",
                "duration": 0,
                "message": f"Test ID collision between P2P and F2P: {p2p_collision_ids}",
                "extra": {
                    "deepswe": {
                        "group": "F2P",
                        "required": True,
                    }
                },
            })
        else:
            recs = raw_f2p_records_by_id.get(test_id, [])
            rec = recs[0] if recs else {}
            status = rec.get("status") if (rec and "status" in rec) else "failed"
            duration = float(rec.get("duration", 0) or 0)
            fail_msgs = rec.get("failureMessages", [])

            entry = {
                "testId": test_id,
                "name": test_id.split("::")[-1] if "::" in test_id else test_id,
                "status": status,
                "duration": duration,
                "extra": {
                    "deepswe": {
                        "group": "F2P",
                        "required": True,
                    }
                },
            }
            if status != "passed":
                entry["message"] = (
                    fail_msgs[0] if fail_msgs else "F2P behavior assertion failed"
                )
            tests_list.append(entry)

    # Append any extra F2P nodes collected during execution
    for test_id in extra_f2p_ids:
        recs = raw_f2p_records_by_id.get(test_id, [])
        rec = recs[0] if recs else {}
        status = rec.get("status") if (rec and "status" in rec) else "failed"
        duration = float(rec.get("duration", 0) or 0)
        fail_msgs = rec.get("failureMessages", [])
        entry = {
            "testId": test_id,
            "name": test_id.split("::")[-1] if "::" in test_id else test_id,
            "status": status,
            "duration": duration,
            "extra": {
                "deepswe": {
                    "group": "F2P",
                    "required": False,
                }
            },
        }
        if status != "passed":
            entry["message"] = (
                fail_msgs[0] if fail_msgs else "Unrecognized extra F2P test"
            )
        tests_list.append(entry)

    for test in tests_list:
        try:
            test["duration"] = max(
                0,
                int(round(float(test.get("duration", 0) or 0))),
            )
        except (TypeError, ValueError, OverflowError):
            test["duration"] = 0

    status_summary = {st: sum(1 for t in tests_list if t.get("status") == st) for st in VALID_CTRF_STATUSES}

    stop_ms = int(time.time() * 1000)
    total_duration_ms = max(
        0,
        int(sum(float(test.get("duration", 0) or 0) for test in tests_list)),
    )
    start_ms = max(0, stop_ms - total_duration_ms)

    ctrf = {
        "reportFormat": "CTRF",
        "specVersion": "0.0.0",
        "results": {
            "tool": {
                "name": "vitest",
            },
            "summary": {
                "tests": len(tests_list),
                "passed": status_summary["passed"],
                "failed": status_summary["failed"],
                "skipped": status_summary["skipped"],
                "pending": status_summary["pending"],
                "other": status_summary["other"],
                "start": start_ms,
                "stop": stop_ms,
            },
            "tests": tests_list,
            "environment": {
                "osPlatform": sys.platform,
                "extra": {
                    "python": sys.version,
                },
            },
            "extra": {
                "deepswe": {
                    "taskId": config.get("task_id", ""),
                    "baseCommit": config.get("base_commit", ""),
                },
            },
        },
    }

    ctrf_output_path.parent.mkdir(parents=True, exist_ok=True)
    ctrf_output_path.write_text(json.dumps(ctrf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return ctrf


def main() -> int:
    parser = argparse.ArgumentParser(description="DeepSWE task verifier entrypoint")
    parser.add_argument("--config", type=Path, required=True, help="Path to config.json")
    parser.add_argument("--repo", type=Path, required=True, help="Path to repository")
    parser.add_argument("--ctrf-output", type=Path, required=True, help="Path for ctrf.json")
    parser.add_argument("--hard-gate-output", type=Path, required=True, help="Path for hard-gate.json")
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0, help="Patch application status")
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))

    # 1. Execute Hard Gate checks (strictly P2P tests only)
    try:
        hard_gate_result = run_hard_gate(
            config_path=args.config,
            repo_dir=args.repo,
            output_path=args.hard_gate_output,
            apply_failed=args.apply_failed,
        )
    except Exception as e:
        err_msg = f"Hard gate execution encountered unhandled exception: {e}"
        print(sanitize_message(err_msg), file=sys.stderr)
        try:
            hg_fail_report = {
                "passed": False,
                "apply_failed": bool(args.apply_failed),
                "failed_nodes": ["hard_gate_crash"],
                "nodes": [],
                "infra_errors": {
                    "hard_gate_crash": {
                        "error_type": "INTERNAL_VERIFIER_EXCEPTION",
                        "message": sanitize_message(str(e)),
                    }
                },
            }
            args.hard_gate_output.parent.mkdir(parents=True, exist_ok=True)
            args.hard_gate_output.write_text(
                json.dumps(hg_fail_report, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        except Exception:
            pass
        return 2

    # Check for infrastructure failures in hard gate
    if hard_gate_result.get("infra_errors"):
        infra_msg = (
            f"Deterministic Hard Gate identified infrastructure failure(s): "
            f"{list(hard_gate_result['infra_errors'].keys())}"
        )
        print(sanitize_message(infra_msg), file=sys.stderr)
        return 2

    hard_gate_passed = bool(hard_gate_result.get("passed")) and (args.apply_failed == 0)

    # 2. Execute F2P tests strictly and independently only if Hard Gate passed (short-circuit otherwise)
    f2p_execution_data: tuple[list[str], dict[str, list[dict[str, Any]]]] | None = None
    if hard_gate_passed:
        try:
            f2p_execution_data = run_f2p_tests(repo_dir=args.repo)
        except InfrastructureError as ie:
            infra_msg = f"F2P test execution infrastructure failure ({ie.error_type}): {ie.message}"
            print(sanitize_message(infra_msg), file=sys.stderr)
            hard_gate_result["passed"] = False
            if "infra_errors" not in hard_gate_result or not isinstance(hard_gate_result["infra_errors"], dict):
                hard_gate_result["infra_errors"] = {}
            hard_gate_result["infra_errors"]["f2p_runner"] = {
                "error_type": ie.error_type,
                "message": sanitize_message(ie.message),
                "details": ie.details,
            }
            args.hard_gate_output.write_text(
                json.dumps(hard_gate_result, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            return 2
        except Exception as e:
            infra_msg = f"F2P test execution unhandled exception: {e}"
            print(sanitize_message(infra_msg), file=sys.stderr)
            hard_gate_result["passed"] = False
            if "infra_errors" not in hard_gate_result or not isinstance(hard_gate_result["infra_errors"], dict):
                hard_gate_result["infra_errors"] = {}
            hard_gate_result["infra_errors"]["f2p_runner"] = {
                "error_type": "INTERNAL_VERIFIER_EXCEPTION",
                "message": sanitize_message(str(e)),
            }
            args.hard_gate_output.write_text(
                json.dumps(hard_gate_result, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            return 2

    # 3. Generate CTRF report reflecting both P2P and F2P statuses
    try:
        ctrf = generate_ctrf_report(
            config=config,
            hard_gate_result=hard_gate_result,
            f2p_execution_data=f2p_execution_data,
            ctrf_output_path=args.ctrf_output,
            hard_gate_passed=hard_gate_passed,
        )
    except Exception as e:
        infra_msg = f"Failed to generate CTRF report: {e}"
        print(sanitize_message(infra_msg), file=sys.stderr)
        hard_gate_result["passed"] = False
        if "infra_errors" not in hard_gate_result or not isinstance(hard_gate_result["infra_errors"], dict):
            hard_gate_result["infra_errors"] = {}
        hard_gate_result["infra_errors"]["ctrf_generation"] = {
            "error_type": "REPORT_CREATION_FAILURE",
            "message": sanitize_message(str(e)),
        }
        args.hard_gate_output.write_text(
            json.dumps(hard_gate_result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return 2

    # 4. Pre-validate CTRF report integrity before handing over to grader.py
    ctrf_errors = validate_ctrf_report_integrity(ctrf, config)
    if ctrf_errors:
        err_msg = f"CTRF report integrity validation failed: {'; '.join(ctrf_errors)}"
        print(sanitize_message(err_msg), file=sys.stderr)
        hard_gate_result["passed"] = False
        if "infra_errors" not in hard_gate_result or not isinstance(hard_gate_result["infra_errors"], dict):
            hard_gate_result["infra_errors"] = {}
        hard_gate_result["infra_errors"]["ctrf_integrity"] = {
            "error_type": "REPORT_INTEGRITY_VIOLATION",
            "errors": ctrf_errors,
        }
        args.hard_gate_output.write_text(
            json.dumps(hard_gate_result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return 2

    # 5. Pre-validate Hard Gate report schema integrity
    hg_valid, hg_errors = validate_hard_gate_schema(
        hard_gate_result,
        expected_p2p_list=config.get("p2p", []),
        expected_cheat_nodes=config.get("hard_gate", {}).get("cheat_nodes", REQUIRED_CHEAT_NODE_IDS),
    )
    if not hg_valid:
        err_msg = f"Hard Gate report schema integrity validation failed: {'; '.join(hg_errors)}"
        print(sanitize_message(err_msg), file=sys.stderr)
        hard_gate_result["passed"] = False
        if "infra_errors" not in hard_gate_result or not isinstance(hard_gate_result["infra_errors"], dict):
            hard_gate_result["infra_errors"] = {}
        hard_gate_result["infra_errors"]["hard_gate_schema"] = {
            "error_type": "REPORT_SCHEMA_VIOLATION",
            "errors": hg_errors,
        }
        args.hard_gate_output.write_text(
            json.dumps(hard_gate_result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return 2

    # Evaluation pipeline completed cleanly (candidate results are deterministically recorded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
