#!/usr/bin/env python3
"""Deterministic hard-gate, P2P, and F2P reward aggregator."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def finite_score(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, int | float):
        raise ValueError(f"{label} must be numeric")
    score = float(value)
    if not math.isfinite(score) or not 0 <= score <= 1:
        raise ValueError(f"{label} must be in [0,1]")
    return score


def required_statuses(config: dict[str, Any], ctrf: dict[str, Any]) -> dict[str, str]:
    expected = {
        **{str(node): "F2P" for node in config["f2p"]},
        **{str(node): "P2P" for node in config["p2p"]},
    }
    actual: dict[str, str] = {}
    for entry in ctrf["results"]["tests"]:
        test_id = str(entry["testId"])
        if test_id in actual:
            raise ValueError(f"duplicate CTRF node: {test_id}")
        group = ((entry.get("extra") or {}).get("deepswe") or {}).get("group")
        if test_id in expected and group != expected[test_id]:
            raise ValueError(f"wrong CTRF group for {test_id}: {group}")
        actual[test_id] = str(entry["status"])
    missing = sorted(set(expected) - set(actual))
    if missing:
        raise ValueError(f"missing CTRF nodes: {missing}")
    return {node: actual[node] for node in expected}


def node_results(config: dict[str, Any], statuses: dict[str, str]) -> list[dict[str, str]]:
    groups = {
        **{str(node): "F2P" for node in config["f2p"]},
        **{str(node): "P2P" for node in config["p2p"]},
    }
    return [
        {"testId": node, "group": groups[node], "status": statuses[node]}
        for node in groups
    ]


def gate(args: argparse.Namespace) -> int:
    config = read_json(args.config)
    ctrf = read_json(args.ctrf)
    hard_gate = read_json(args.hard_gate)
    hard_gate_passed = hard_gate.get("passed") is True and not bool(args.apply_failed)
    if not hard_gate_passed:
        f2p_nodes = {str(node) for node in config["f2p"]}
        for entry in ctrf["results"]["tests"]:
            if str(entry.get("testId")) in f2p_nodes:
                entry["status"] = "failed"
                entry["message"] = "candidate failed deterministic hard gate"
        statuses = ("passed", "failed", "skipped", "pending", "other")
        tests = ctrf["results"]["tests"]
        summary = ctrf["results"].get("summary")
        if isinstance(summary, dict):
            summary["tests"] = len(tests)
            summary.update(
                {status: sum(item.get("status") == status for item in tests) for status in statuses}
            )
        write_json(args.ctrf, ctrf)
    statuses = required_statuses(config, ctrf)
    f2p = [str(node) for node in config["f2p"]]
    p2p = [str(node) for node in config["p2p"]]
    f2p_passed = sum(statuses[node] == "passed" for node in f2p)
    p2p_passed = sum(statuses[node] == "passed" for node in p2p)
    f2p_complete = bool(f2p) and f2p_passed == len(f2p)
    p2p_complete = p2p_passed == len(p2p)
    result = {
        "hard_gate_success": int(hard_gate_passed and p2p_complete),
        "verifier_success": int(hard_gate_passed and f2p_complete and p2p_complete),
        "f2p_passed": f2p_passed,
        "f2p_total": len(f2p),
        "f2p_pass_ratio": f2p_passed / len(f2p) if f2p else 0.0,
        "p2p_passed": p2p_passed,
        "p2p_total": len(p2p),
        "p2p_pass_ratio": p2p_passed / len(p2p) if p2p else 1.0,
        "eligible": hard_gate_passed and p2p_complete and f2p_complete,
        "apply_failed": bool(args.apply_failed),
        "failed_nodes": sorted(node for node, status in statuses.items() if status != "passed"),
        "nodes": node_results(config, statuses),
    }
    write_json(args.output, result)
    return 0


def finalize(args: argparse.Namespace) -> int:
    config = read_json(args.config)
    gate_result = read_json(args.gate)
    success = gate_result.get("eligible") is True
    hard_gate_passed = gate_result.get("hard_gate_success") == 1
    reward = finite_score(gate_result.get("f2p_pass_ratio"), "gate.f2p_pass_ratio") if hard_gate_passed else -1.0
    components = {
        "hard_gate": {"score": float(gate_result.get("hard_gate_success", 0)), "weight": 0.0},
        "p2p": {"score": finite_score(gate_result.get("p2p_pass_ratio"), "gate.p2p_pass_ratio"), "weight": 0.0},
        "f2p": {"score": finite_score(gate_result.get("f2p_pass_ratio"), "gate.f2p_pass_ratio"), "weight": 1.0},
    }
    public_reward = {"reward": reward, "f2p": components["f2p"]["score"], "p2p": components["p2p"]["score"]}
    details = {
        "schema_version": "deepswe-reward-details/v1",
        "reward_mode": config.get("reward_mode", "VERIFIER_ONLY"),
        "status": "passed" if success else "candidate_failed",
        "evaluation_valid": True,
        "evaluation_success": success,
        "scoring_executed": False,
        "skip_reason": None if success else "deterministic_gate_failed",
        "policy": "deterministic_verifier_only",
        "policy_version": "3",
        "components": components,
        "reward": reward,
        "gate": gate_result,
        "verifier_success": int(success),
        "hard_gate_success": int(gate_result.get("hard_gate_success") == 1),
        "f2p_passed": gate_result.get("f2p_passed", 0),
        "f2p_total": gate_result.get("f2p_total", 0),
        "f2p_pass_ratio": gate_result.get("f2p_pass_ratio", 0.0),
        "p2p_passed": gate_result.get("p2p_passed", 0),
        "p2p_total": gate_result.get("p2p_total", 0),
        "p2p_pass_ratio": gate_result.get("p2p_pass_ratio", 0.0),
        "failed_nodes": gate_result.get("failed_nodes") or [],
        "nodes": gate_result.get("nodes") or [],
        "apply_failed": gate_result.get("apply_failed") is True,
        "hard_gate": {
            "passed": gate_result.get("hard_gate_success") == 1,
            "failed_test_ids": gate_result.get("failed_nodes") or [],
        },
    }
    reports = config["reports"]
    write_json(Path(reports["reward"]), public_reward)
    write_json(Path(reports["reward_details"]), details)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    gate_parser = subparsers.add_parser("gate")
    gate_parser.add_argument("--config", type=Path, required=True)
    gate_parser.add_argument("--ctrf", type=Path, required=True)
    gate_parser.add_argument("--hard-gate", type=Path, required=True)
    gate_parser.add_argument("--output", type=Path, required=True)
    gate_parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    gate_parser.set_defaults(handler=gate)

    finalize_parser = subparsers.add_parser("finalize")
    finalize_parser.add_argument("--config", type=Path, required=True)
    finalize_parser.add_argument("--gate", type=Path, required=True)
    finalize_parser.set_defaults(handler=finalize)

    args = parser.parse_args()
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
