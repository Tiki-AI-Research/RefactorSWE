#!/usr/bin/env python3
"""Aggregate deterministic nodes and RewardKit Atoms into Harbor rewards."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

PASS_STATUSES = {"pass", "passed"}
SKIP_STATUSES = {"skip", "skipped", "pending", "xfail", "xfailed"}
WEIGHTS = {"test": 0.3, "objectivity": 0.4, "rubrics": 0.3}
ALLOWED_ERRORS = {
    "build error",
    "compile error",
    "infrastructure_error",
    "agent_time_out",
    "scope_violation",
}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def finite_float(value):
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("nonfinite JSON number")
    return number


def reject_constant(value):
    raise ValueError("nonfinite JSON constant")


def read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object,
                           parse_float=finite_float, parse_constant=reject_constant)
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError):
        return {}


def _valid_object(value: Any) -> bool:
    return isinstance(value, dict) and bool(value)


def _infrastructure_failure(reason: str) -> dict[str, Any]:
    return {
        "cheating_detected": False,
        "hard_gate_success": 0,
        "verifier_success": 0,
        "f2p_pass_ratio": 0.0,
        "p2p_pass_ratio": 0.0,
        "can_continue": 0,
        "terminate": 1,
        "termination_reason": reason,
        "reward": -2.0,
        "errors": ["infrastructure_error"],
        "valid_for_statistics": False,
        "eligible_for_score": False,
    }


def _normalized_errors(values: Any) -> list[str]:
    if not isinstance(values, list):
        return []
    return list(dict.fromkeys(value for value in values if value in ALLOWED_ERRORS))


def public_reward(
    *,
    gate_result: dict[str, Any] | None = None,
    reward: float,
) -> dict[str, Any]:
    gate = gate_result if isinstance(gate_result, dict) else {}
    return {
        "cheating_detected": bool(gate.get("cheating_detected", False)),
        "f2p_pass_ratio": float(gate.get("f2p_pass_ratio", 0.0)),
        "p2p_pass_ratio": float(gate.get("p2p_pass_ratio", 0.0)),
        "reward": float(reward),
    }


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )



def get_final_outputs(config: dict[str, Any]) -> dict[str, Path]:
    reports = config.get("reports", {})
    if not isinstance(reports, dict):
        reports = {}
    return {
        "ctrf": Path(reports.get("ctrf", "/logs/verifier/ctrf.json")),
        "reward_details": Path(reports.get("reward_details", "/logs/verifier/reward-details.json")),
        "reward": Path(reports.get("reward", "/logs/verifier/reward.json")),
    }


def configured_nodes(config: dict[str, Any]) -> tuple[list[str], list[str]]:
    f2p = config.get("f2p", [])
    p2p = config.get("p2p", [])
    if not isinstance(f2p, list):
        f2p = []
    if not isinstance(p2p, list):
        p2p = []
    return f2p, p2p


def report_tests(report: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize legacy reports and the verifier runtime's native CTRF."""

    results = report.get("results")
    tests = results.get("tests", []) if isinstance(results, dict) else report.get("tests", [])
    if not isinstance(tests, list):
        return []

    normalized = []
    for test in tests:
        if not isinstance(test, dict):
            continue
        row = dict(test)
        if "typedStatus" not in row:
            extra = row.get("extra")
            deepswe = extra.get("deepswe") if isinstance(extra, dict) else None
            typed_status = deepswe.get("typed_status") if isinstance(deepswe, dict) else None
            if isinstance(typed_status, str):
                row["typedStatus"] = typed_status
        normalized.append(row)
    return normalized



# Phases whose failure means the evaluation itself is untrustworthy. Any other
# non-PASS node outcome on an intact report (compile, collection, setup, crash,
# timeout, not-run, unknown) is the candidate's own result: the reference
# solution passes every node in the same image.
INFRASTRUCTURE_PHASES = {"report", "infrastructure"}
INFRASTRUCTURE_RETURNCODES = {137, -9}


def _node_evidence(item: Any) -> dict[str, Any]:
    extra = item.get("extra") if isinstance(item, dict) else None
    if not isinstance(extra, dict):
        return {}
    for key in ("evidence", "deepswe"):
        evidence = extra.get(key)
        if isinstance(evidence, dict) and "phase" in evidence:
            return evidence
    return extra


def _is_infrastructure_evidence(evidence: Any) -> bool:
    if not isinstance(evidence, dict):
        return True
    phase = str(evidence.get("phase", "")).lower()
    if not phase or phase in INFRASTRUCTURE_PHASES:
        return True
    raw = evidence.get("raw_evidence")
    code = evidence.get("returncode")
    if code is None and isinstance(raw, dict):
        code = raw.get("returncode")
    return code in INFRASTRUCTURE_RETURNCODES


def attribute_candidate_failures(
    reported: list[Any],
    verifier_result: dict[str, Any],
) -> tuple[list[Any], dict[str, Any]]:
    """Type candidate-caused INFRA_ERROR/INCONCLUSIVE nodes as FAIL."""
    infra = {**verifier_result, "status": "INFRA_ERROR", "success": False}
    terminal = verifier_result.get("terminal")
    if isinstance(terminal, dict) and _is_infrastructure_evidence(terminal):
        return reported, infra
    rewritten: list[Any] = []
    attributed = 0
    for item in reported:
        if isinstance(item, dict):
            status = str(item.get("typedStatus", "")).upper()
            if status in {"INFRA_ERROR", "INCONCLUSIVE"}:
                evidence = _node_evidence(item)
                if _is_infrastructure_evidence(evidence):
                    return reported, infra
                extra = dict(item.get("extra") or {})
                extra["candidate_attribution"] = {
                    "original_typed_status": status,
                    "phase": evidence.get("phase"),
                    "failure_class": evidence.get("failure_class"),
                }
                item = {**item, "typedStatus": "FAIL", "extra": extra}
                attributed += 1
            elif status not in {"PASS", "FAIL"}:
                return reported, infra
        rewritten.append(item)
    status = str(verifier_result.get("status", "")).upper()
    if status in {"INFRA_ERROR", "INCONCLUSIVE"}:
        if not attributed and not isinstance(terminal, dict):
            return reported, infra
        verifier_result = {**verifier_result, "status": "FAIL", "success": False}
    return rewritten, verifier_result


def canonicalize_nodes(
    report: dict[str, Any],
    required_nodes: list[str],
    *,
    apply_failed: bool,
) -> list[dict[str, Any]]:
    tests = report_tests(report) if isinstance(report, dict) else []
    by_name: dict[str, list[dict[str, Any]]] = {}
    for t in tests:
        if isinstance(t, dict) and isinstance(t.get("name"), str):
            by_name.setdefault(t["name"], []).append(t)

    canonical_list: list[dict[str, Any]] = []
    for node_id in required_nodes:
        entries = by_name.get(node_id, [])
        duplicate = len(entries) > 1
        missing = len(entries) == 0
        raw_status = str(entries[0].get("status", "failed")).lower() if entries else "missing"
        skipped = raw_status in SKIP_STATUSES
        passed = not apply_failed and not duplicate and not missing and raw_status in PASS_STATUSES

        if apply_failed:
            message = "candidate patch could not be applied"
        elif duplicate:
            message = f"node was reported {len(entries)} times"
        elif missing:
            message = "required node was not reported"
        elif skipped:
            message = "required node was skipped"
        else:
            message = str(entries[0].get("message", ""))

        typed_status = str(entries[0].get("typedStatus", "")).upper() if entries else "INFRA_ERROR"
        if missing or duplicate:
            typed_status = "INFRA_ERROR"
        ctrf_status = ("other" if typed_status == "INFRA_ERROR" else
                       "skipped" if typed_status == "INCONCLUSIVE" else
                       "passed" if passed else "failed")
        canonical_list.append({
            "name": node_id,
            "testId": node_id,
            "status": ctrf_status,
            "message": message,
            "rawStatus": raw_status,
            "typedStatus": typed_status,
            **({"extra": entries[0]["extra"]} if entries and isinstance(entries[0].get("extra"), dict) else {}),
        })
    return canonical_list


def calculate_pass_ratio(
    canonical_tests: list[dict[str, Any]],
    configured: list[str],
) -> tuple[int, int, float]:
    if not configured:
        return 0, 0, 1.0
    passed_set = {t["name"] for t in canonical_tests if t.get("status") == "passed"}
    passed_count = sum(1 for node in configured if node in passed_set)
    total_count = len(configured)
    ratio = passed_count / total_count if total_count > 0 else 0.0
    return passed_count, total_count, ratio



def evaluate_gate(
    *,
    hard_gate: dict[str, Any],
    verifier_result: dict[str, Any],
    f2p_pass_ratio: float,
    p2p_pass_ratio: float,
    apply_failed: bool,
    partial_f2p: bool = False,
) -> dict[str, Any]:
    hard_gate_passed = (
        hard_gate.get("success", hard_gate.get("passed")) is True
        and not apply_failed
    )
    verifier_success = verifier_result.get("success")
    if not isinstance(verifier_success, bool):
        verifier_success = (
            verifier_result.get("status") in {"PASS", "FAIL"}
            and not verifier_result.get("error")
            and not verifier_result.get("terminal")
        )
    verifier_passed = verifier_success and not apply_failed
    cheating_detected = bool(hard_gate.get("cheating_detected"))
    candidate_rejected = bool(
        apply_failed
        or hard_gate.get("error_category") in {"CANDIDATE_REJECTED", "CANDIDATE_PATCH_INVALID"}
        or verifier_result.get("error_category") in {"CANDIDATE_REJECTED", "CANDIDATE_PATCH_INVALID"}
    )
    errors: list[str] = []
    if apply_failed:
        errors.append("build error")
    elif hard_gate.get("compile_passed") is False:
        errors.append("compile error")

    common = {
        "cheating_detected": cheating_detected,
        "candidate_rejected": candidate_rejected,
        "hard_gate_success": int(hard_gate_passed),
        "verifier_success": int(verifier_passed),
        "f2p_pass_ratio": f2p_pass_ratio,
        "p2p_pass_ratio": p2p_pass_ratio,
        "errors": errors,
        "eligible_for_score": False,
        "valid_for_statistics": True,
    }

    if cheating_detected or candidate_rejected:
        return {
            **common,
            "can_continue": 0,
            "terminate": 1,
            "termination_reason": "cheating_detected" if cheating_detected else "candidate_rejected",
            "reward": -1.0 if cheating_detected else 0.0,
        }

    # A failed assertion is a candidate result; an unavailable runner is not.
    if (verifier_result.get("status") in {"INFRA_ERROR", "INCONCLUSIVE"}
            or hard_gate.get("infrastructure_error")
            or hard_gate.get("error_category") == "INFRASTRUCTURE_ERROR"):
        return {
            **common, "can_continue": 0, "terminate": 1,
            "termination_reason": "infrastructure_error", "reward": -2.0,
            "errors": ["infrastructure_error"], "valid_for_statistics": False,
        }

    # P2P regressions block scoring, even when F2P assertions pass.
    if hard_gate.get("error_category") == "P2P_REGRESSION" and p2p_pass_ratio != 1.0:
        return {**common, "can_continue": 0, "terminate": 1,
                "termination_reason": "p2p_failed", "reward": 0.0}

    if not hard_gate_passed:
        return {
            **common,
            "can_continue": 0,
            "terminate": 1,
            "termination_reason": "scope_violation" if hard_gate.get("scope_violation") else "hard_gate_failed",
            "errors": ["scope_violation"] if hard_gate.get("scope_violation") else errors,
            "reward": 0.0,
        }

    # P2P preservation is a prerequisite, never compensated by new F2P points.
    if p2p_pass_ratio != 1.0:
        return {**common, "can_continue": 0, "terminate": 1,
                "termination_reason": "p2p_failed", "reward": 0.0}
    if f2p_pass_ratio != 1.0 and not partial_f2p:
        return {
            **common,
            "can_continue": 0,
            "terminate": 1,
            "termination_reason": "pass_ratio_not_complete",
            "reward": 0.0,
        }

    common["eligible_for_score"] = True

    if not verifier_passed:
        return {
            **common,
            "eligible_for_score": False,
            "can_continue": 0,
            "terminate": 1,
            "termination_reason": "verifier_failed",
            "reward": 0.0,
        }

    return {
        **common,
        "can_continue": 1,
        "terminate": 0,
        "termination_reason": "",
        "reward": f2p_pass_ratio,
    }


def build_ctrf(
    *,
    config: dict[str, Any],
    canonical_tests: list[dict[str, Any]],
    gate_result: dict[str, Any],
) -> dict[str, Any]:
    # Group identity comes from trusted membership, not candidate-supplied text.
    f2p, p2p = configured_nodes(config)
    groups = {**dict.fromkeys(f2p, "f2p"), **dict.fromkeys(p2p, "p2p")}
    for node in canonical_tests:
        extra = node.setdefault("extra", {})
        extra["deepswe"] = {"group": groups[node["name"]]}
    passed_total = sum(1 for t in canonical_tests if t.get("status") == "passed")
    failed_total = sum(t["status"] == "failed" for t in canonical_tests)
    return {
        "results": {
            "tool": {"name": "deepswe-grader", "version": "1.0"},
            "summary": {
                "tests": len(canonical_tests),
                "passed": passed_total,
                "failed": failed_total,
                "pending": 0,
                "skipped": sum(t["status"] == "skipped" for t in canonical_tests),
                "other": sum(t["status"] == "other" for t in canonical_tests),
            },
            "tests": canonical_tests,
            "environment": {
                "task": config.get("task_id", ""),
                "baseCommit": str(config.get("base_commit", "")),
                "verifierSuccess": gate_result.get("verifier_success", 0),
                "hardGateSuccess": gate_result.get("hard_gate_success", 0),
                "validForStatistics": gate_result.get("valid_for_statistics", False),
            },
        }
    }



def grade(
    *,
    config_path: Path,
    report_path: Path,
    hard_gate_path: Path,
    verifier_result_path: Path,
    reward_output_path: Path,
    ctrf_output_path: Path,
    apply_failed: bool,
) -> dict[str, Any]:
    config = read_json(config_path)
    report = read_json(report_path)
    hard_gate = read_json(hard_gate_path)
    verifier_result = read_json(verifier_result_path)

    if not _valid_object(verifier_result) or not _valid_object(hard_gate):
        result = _infrastructure_failure("verifier_result_missing_or_invalid")
        if _valid_object(verifier_result):
            result["termination_reason"] = "hard_gate_result_missing_or_invalid"
        write_json(reward_output_path, result)
        write_json(ctrf_output_path, {"results": {"tests": [], "environment": {"error": result["termination_reason"]}}})
        return result

    # Malformed evidence is an infrastructure error, not a candidate failure.
    if (type(hard_gate.get("passed")) is not bool
            or (hard_gate.get("status") in ("PASS", "FAIL")
                and hard_gate["passed"] != (hard_gate["status"] == "PASS"))
            or ("success" in hard_gate and (
                type(hard_gate["success"]) is not bool
                or hard_gate["success"] != hard_gate["passed"]))):
        result = _infrastructure_failure("hard_gate_result_missing_or_invalid")
        write_json(reward_output_path, result)
        write_json(ctrf_output_path, report)
        return result

    f2p_nodes, p2p_nodes = configured_nodes(config)
    required_nodes = [*f2p_nodes, *p2p_nodes]
    reported = report_tests(report)
    reported_names = [item.get("name") for item in reported if isinstance(item, dict)]
    groups = {**dict.fromkeys(f2p_nodes, "f2p"), **dict.fromkeys(p2p_nodes, "p2p")}
    issues = []
    report_results = report.get("results")
    raw_tests = report_results.get("tests") if isinstance(report_results, dict) else None
    if not isinstance(raw_tests, list) or len(raw_tests) != len(reported):
        issues.append("invalid test records")
    compatible = {"passed": "PASS", "failed": "FAIL", "skipped": "INCONCLUSIVE", "other": "INFRA_ERROR"}
    for item in reported:
        extra = item.get("extra")
        deepswe = extra.get("deepswe") if isinstance(extra, dict) else None
        if not isinstance(deepswe, dict):
            issues.append("missing node metadata")
            continue
        name, raw, typed = item.get("name"), item.get("status"), item.get("typedStatus")
        if not isinstance(name, str) or groups.get(name) != deepswe.get("group"):
            issues.append("node group mismatch")
        if not isinstance(raw, str) or raw not in compatible or compatible.get(raw) != typed:
            issues.append("invalid or contradictory node status")
        if "typed_status" in deepswe and deepswe["typed_status"] != typed:
            issues.append("contradictory metadata status")
        if item.get("testId", name) != name:
            issues.append("node identity mismatch")
    summary = report_results.get("summary") if isinstance(report_results, dict) else None
    counts = {"tests": len(reported), **{status: sum(item.get("status") == status for item in reported)
              for status in ("passed", "failed", "skipped", "pending", "other")}}
    if not isinstance(summary, dict) or any(type(summary.get(key)) is not int or summary[key] != value
                                           for key, value in counts.items()):
        issues.append("invalid CTRF summary")
    if issues:
        result = _infrastructure_failure("invalid_node_report")
        result["report_issues"] = sorted(set(issues))
        write_json(reward_output_path, result)
        write_json(ctrf_output_path, report)
        return result
    integrity_failed = False
    # Missing, duplicate, or foreign records invalidate the evidence chain.
    if (not isinstance(reported, list) or len(reported_names) != len(required_nodes)
            or any(not isinstance(name, str) for name in reported_names)
            or len(set(reported_names)) != len(reported_names)
            or set(reported_names) != set(required_nodes)):
        integrity_failed = True
    if integrity_failed:
        verifier_result = {**verifier_result, "status": "INFRA_ERROR", "success": False}
    else:
        reported, verifier_result = attribute_candidate_failures(reported, verifier_result)
        report = {**report, "tests": reported}

    canonical_tests = canonicalize_nodes(
        report,
        required_nodes,
        apply_failed=apply_failed,
    )

    f2p_passed, f2p_total, f2p_pass_ratio = calculate_pass_ratio(canonical_tests, f2p_nodes)
    p2p_passed, p2p_total, p2p_pass_ratio = calculate_pass_ratio(canonical_tests, p2p_nodes)

    gate_result = evaluate_gate(
        hard_gate=hard_gate,
        verifier_result=verifier_result,
        f2p_pass_ratio=f2p_pass_ratio,
        p2p_pass_ratio=p2p_pass_ratio,
        apply_failed=apply_failed,
        partial_f2p=config.get("reward_mode") == "VERIFIER_ONLY",
    )

    gate_result.update({
        "f2p_passed": f2p_passed,
        "f2p_total": f2p_total,
        "p2p_passed": p2p_passed,
        "p2p_total": p2p_total,
        "p2p_pass_ratio": p2p_pass_ratio,
        "apply_failed": int(apply_failed),
    })

    ctrf = build_ctrf(
        config=config,
        canonical_tests=canonical_tests,
        gate_result=gate_result,
    )

    write_json(reward_output_path, gate_result)
    write_json(ctrf_output_path, ctrf)
    return gate_result



def calculate_final_score(
    *,
    gate_result: dict[str, Any],
    objective_result: dict[str, Any],
    judge_result: dict[str, Any],
) -> dict[str, float]:
    f2p_pass_ratio = float(gate_result.get("f2p_pass_ratio", 0.0))

    obj_atoms = objective_result.get("atoms", {})
    if isinstance(obj_atoms, dict) and obj_atoms:
        scores = [float(x.get("score", 0.0)) for x in obj_atoms.values() if isinstance(x, dict)]
        objectivity_score = sum(scores) / len(scores) if scores else 0.0
    else:
        objectivity_score = float(objective_result.get("score", 0.0))

    rubrics_score = float(judge_result.get("reward", 0.0))

    final_reward = round(
        WEIGHTS["test"] * f2p_pass_ratio
        + WEIGHTS["objectivity"] * objectivity_score
        + WEIGHTS["rubrics"] * rubrics_score,
        4,
    )

    return {
        "test": f2p_pass_ratio,
        "objectivity": objectivity_score,
        "rubrics": rubrics_score,
        "reward": final_reward,
    }


def valid_gate_summary(gate: dict[str, Any], expected_counts=None) -> bool:
    """Validate the aggregate receipt before using it to assign a reward."""
    for key in ("hard_gate_success", "verifier_success", "can_continue", "terminate"):
        if type(gate.get(key)) is not int or gate[key] not in (0, 1):
            return False
    for key in ("eligible_for_score", "valid_for_statistics", "cheating_detected"):
        if type(gate.get(key)) is not bool:
            return False
    if not isinstance(gate.get("errors"), list) or any(
            not isinstance(error, str) for error in gate["errors"]):
        return False
    if not isinstance(gate.get("termination_reason"), str):
        return False
    for group in ("f2p", "p2p"):
        ratio = gate.get(group + "_pass_ratio")
        if type(ratio) not in (int, float) or not math.isfinite(ratio) or not 0 <= ratio <= 1:
            return False
        passed, total = gate.get(group + "_passed"), gate.get(group + "_total")
        # Early infrastructure errors can have no node counts, but cannot score.
        if passed is None and total is None and gate["valid_for_statistics"] is False:
            if ratio != 0 or gate["eligible_for_score"]:
                return False
            continue
        if type(passed) is not int or type(total) is not int or not 0 <= passed <= total or total <= 0:
            return False
        if expected_counts is not None and total != expected_counts[group]:
            return False
        if not math.isclose(ratio, passed / total, rel_tol=0, abs_tol=1e-12):
            return False
    return True


def finalize(
    *,
    gate_reward_path: Path,
    objective_evidence_path: Path,
    judge_output_path: Path,
    judge_details_path: Path,
    reward_details_output_path: Path,
    reward_output_path: Path,
    reward_mode: str | None = None,
    agent_time_out_path: Path | None = None,
    expected_counts: dict[str, int] | None = None,
) -> dict[str, Any]:
    gate_result = read_json(gate_reward_path)

    if not _valid_object(gate_result) or not valid_gate_summary(gate_result, expected_counts):
        final_reward = public_reward(reward=-2.0)
        write_json(reward_details_output_path, {
            "termination_reason": "gate_result_missing_or_invalid",
            "errors": ["infrastructure_error"],
            "valid_for_statistics": False,
            "eligible_for_score": False,
        })
        write_json(reward_output_path, final_reward)
        return final_reward

    f2p_pass_ratio = float(gate_result.get("f2p_pass_ratio", 0.0))

    if reward_mode == "VERIFIER_ONLY":
        # P2P and hard gates are prerequisites; valid F2P assertions earn
        # proportional credit, including when the overall test status is FAIL.
        eligible = (
            gate_result.get("eligible_for_score") is True
            and gate_result.get("valid_for_statistics") is True
            and gate_result.get("hard_gate_success") == 1
            and gate_result.get("verifier_success") == 1
            and 0.0 <= f2p_pass_ratio <= 1.0
            and gate_result.get("p2p_pass_ratio") == 1.0
            and not gate_result.get("cheating_detected")
            and not gate_result.get("candidate_rejected")
            and not gate_result.get("apply_failed")
            and not gate_result.get("errors")
        )
        if gate_result.get("cheating_detected"):
            blocked_reward = -1.0
        elif gate_result.get("valid_for_statistics") is False or "infrastructure_error" in gate_result.get("errors", []):
            blocked_reward = -2.0
        else:
            blocked_reward = 0.0
        final_reward = public_reward(
            gate_result=gate_result,
            reward=f2p_pass_ratio if eligible else blocked_reward,
        )
        reward_details = {
            "termination_reason": gate_result.get("termination_reason", ""),
            "gate": gate_result,
            "errors": _normalized_errors(gate_result.get("errors", [])),
            "valid_for_statistics": gate_result.get("valid_for_statistics", False),
            "eligible_for_score": eligible,
        }
        write_json(reward_details_output_path, reward_details)
        write_json(reward_output_path, final_reward)
        return final_reward

    if gate_result.get("can_continue") != 1:
        reward = float(gate_result.get("reward", 0.0))
        final_reward = public_reward(
            gate_result=gate_result,
            reward=reward,
        )
        reward_details = {
            "termination_reason": gate_result.get("termination_reason", "gate_failed"),
            "gate": gate_result,
            "errors": _normalized_errors(gate_result.get("errors", [])),
        }
        write_json(reward_details_output_path, reward_details)
        write_json(reward_output_path, final_reward)
        return final_reward

    objective_result = read_json(objective_evidence_path)
    judge_result = read_json(judge_output_path)
    judge_details = read_json(judge_details_path)

    if not _valid_object(objective_result):
        final_reward = public_reward(
            gate_result=gate_result,
            reward=0.0,
        )
        write_json(reward_details_output_path, {
            "termination_reason": "objective_result_missing_or_invalid",
            "gate": gate_result,
            "errors": ["infrastructure_error"],
        })
        write_json(reward_output_path, final_reward)
        return final_reward
    if not _valid_object(judge_result) or not isinstance(judge_result.get("reward"), (int, float)):
        judge_timed_out = agent_time_out_path is not None and agent_time_out_path.is_file()
        final_reward = public_reward(
            gate_result=gate_result,
            reward=0.0,
        )
        write_json(reward_details_output_path, {
            "termination_reason": (
                "agent_time_out" if judge_timed_out else "judge_result_missing_or_invalid"
            ),
            "gate": gate_result,
            "errors": ["agent_time_out" if judge_timed_out else "infrastructure_error"],
        })
        write_json(reward_output_path, final_reward)
        return final_reward

    score = calculate_final_score(
        gate_result=gate_result,
        objective_result=objective_result,
        judge_result=judge_result,
    )

    final_reward = public_reward(
        gate_result=gate_result,
        reward=score["reward"],
    )

    reward_details = {
        "gate": gate_result,
        "objective": objective_result,
        "judge": judge_result,
        "judge_details": judge_details,
        "score": score,
        "errors": _normalized_errors(gate_result.get("errors", [])),
    }

    write_json(reward_details_output_path, reward_details)
    write_json(reward_output_path, final_reward)
    return final_reward



def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("grade", "finalize"))
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--logs", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--hard-gate", type=Path)
    parser.add_argument("--verifier-result", type=Path)
    parser.add_argument("--reward-output", type=Path)
    parser.add_argument("--judge", type=Path)
    parser.add_argument("--prompt", type=Path)
    parser.add_argument("--rewardkit-output", type=Path)
    parser.add_argument("--rewardkit-details", type=Path)
    parser.add_argument("--objective-evidence", type=Path)
    parser.add_argument("--agent-time-out", type=Path)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    config = read_json(args.config)
    outputs = get_final_outputs(config)

    if args.command == "grade":
        result = grade(
            config_path=args.config,
            report_path=args.report if args.report else args.logs / "reports" / "nodes.json",
            hard_gate_path=args.hard_gate if args.hard_gate else args.logs / "hard-gate.json",
            verifier_result_path=args.verifier_result if args.verifier_result else args.logs / "verifier-result.json",
            reward_output_path=args.reward_output if args.reward_output else args.logs / "gate-reward.json",
            ctrf_output_path=outputs["ctrf"],
            apply_failed=bool(args.apply_failed),
        )
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 0

    result = finalize(
        gate_reward_path=args.logs / "gate-reward.json",
        objective_evidence_path=args.objective_evidence if args.objective_evidence else args.logs / "objective-evidence.json",
        judge_output_path=args.rewardkit_output if args.rewardkit_output else args.logs / "judge" / "reward.json",
        judge_details_path=args.rewardkit_details if args.rewardkit_details else args.logs / "judge" / "reward-details.json",
        reward_details_output_path=outputs["reward_details"],
        reward_output_path=outputs["reward"],
        reward_mode=config.get("reward_mode"),
        agent_time_out_path=args.agent_time_out,
        expected_counts={group: len(config.get(group, [])) for group in ("f2p", "p2p")},
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
