#!/usr/bin/env python3
"""DeepSWE v2 gate and final reward aggregator."""

from __future__ import annotations

import argparse
import json
import math
import os
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
        **{str(node): "f2p" for node in config["f2p"]},
        **{str(node): "p2p" for node in config["p2p"]},
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
        "f2p_pass_ratio": f2p_passed / len(f2p) if f2p else 0.0,
        "p2p_pass_ratio": p2p_passed / len(p2p) if p2p else 1.0,
        "eligible_for_judge": hard_gate_passed and p2p_complete and f2p_complete,
        "apply_failed": bool(args.apply_failed),
        "failed_nodes": sorted(node for node, status in statuses.items() if status != "passed"),
    }
    write_json(args.output, result)
    return 0


def _judge_score(path: Path) -> float:
    value = read_json(path)
    for key in ("reward", "score", "rubrics"):
        if key in value:
            return finite_score(value[key], f"judge.{key}")
    raise ValueError("judge output must contain reward, score, or rubrics")


def finalize(args: argparse.Namespace) -> int:
    config = read_json(args.config)
    gate_result = read_json(args.gate)
    calibration = os.environ.get("DF_HARBOR_CALIBRATION") == "1"
    reward_mode = config.get("reward_mode", "FULL_REWARD")
    if reward_mode not in {"FULL_REWARD", "VERIFIER_ONLY"}:
        raise ValueError(f"unsupported reward_mode: {reward_mode}")
    eligible = gate_result.get("eligible_for_judge") is True
    test_score = finite_score(gate_result.get("f2p_pass_ratio"), "gate.f2p_pass_ratio")

    if calibration:
        rubrics_score = 0.0
        reward = 1.0 if eligible else 0.0
        weights = {"test": 1.0, "objectivity": 0.0, "rubrics": 0.0}
        scoring_executed = False
        skip_reason = "calibration"
        if reward_mode == "VERIFIER_ONLY":
            policy = "deterministic_verifier_only"
            components = {"test": {"score": reward, "weight": 1.0}}
            public_reward = {"reward": reward, "test": reward}
        else:
            objective = read_json(args.objective)
            objective_score = finite_score(objective.get("score"), "objectivity.score")
            policy = config["final_reward"]["policy"]
            components = {
                "test": {"score": test_score, "weight": 1.0},
                "objectivity": {"score": objective_score, "weight": 0.0},
                "rubrics": {"score": rubrics_score, "weight": 0.0},
            }
            public_reward = {
                "test": test_score,
                "objectivity": objective_score,
                "rubrics": rubrics_score,
                "reward": reward,
            }
    elif reward_mode == "VERIFIER_ONLY":
        reward = 1.0 if eligible else 0.0
        scoring_executed = False
        skip_reason = "verifier_only"
        policy = "deterministic_verifier_only"
        components = {"test": {"score": reward, "weight": 1.0}}
        public_reward = {"reward": reward, "test": reward}
    elif eligible:
        objective = read_json(args.objective)
        objective_score = finite_score(objective.get("score"), "objectivity.score")
        rubrics_score = _judge_score(args.judge)
        weights = config["final_reward"]["weights"]
        reward = sum(
            score * finite_score(weights[name], f"weights.{name}")
            for name, score in {
                "test": test_score,
                "objectivity": objective_score,
                "rubrics": rubrics_score,
            }.items()
        )
        reward = min(1.0, max(0.0, reward))
        scoring_executed = True
        skip_reason = None
        policy = config["final_reward"]["policy"]
        components = {
            "test": {"score": test_score, "weight": float(weights["test"])},
            "objectivity": {"score": objective_score, "weight": float(weights["objectivity"])},
            "rubrics": {"score": rubrics_score, "weight": float(weights["rubrics"])},
        }
        public_reward = {
            "test": test_score,
            "objectivity": objective_score,
            "rubrics": rubrics_score,
            "reward": reward,
        }
    else:
        objective = read_json(args.objective)
        objective_score = finite_score(objective.get("score"), "objectivity.score")
        rubrics_score = 0.0
        weights = config["final_reward"]["weights"]
        reward = 0.0
        scoring_executed = False
        skip_reason = "deterministic_gate_failed"
        policy = config["final_reward"]["policy"]
        components = {
            "test": {"score": test_score, "weight": float(weights["test"])},
            "objectivity": {"score": objective_score, "weight": float(weights["objectivity"])},
            "rubrics": {"score": rubrics_score, "weight": float(weights["rubrics"])},
        }
        public_reward = {
            "test": test_score,
            "objectivity": objective_score,
            "rubrics": rubrics_score,
            "reward": reward,
        }

    success = eligible
    details = {
        "schema_version": "deepswe-reward-details/v1",
        "reward_mode": reward_mode,
        "status": "passed" if success else "candidate_failed",
        "evaluation_valid": True,
        "evaluation_success": success,
        "scoring_executed": scoring_executed,
        "skip_reason": skip_reason,
        "policy": policy,
        "policy_version": "2",
        "components": components,
        "reward": reward,
        "apply_failed": gate_result.get("apply_failed") is True,
        "hard_gate": {
            "passed": gate_result.get("hard_gate_success") == 1,
            "failed_test_ids": gate_result.get("failed_nodes") or [],
        },
    }
    reports = config["reports"]
    rubric_evidence = args.judge.parent / "rubrics.json"
    if reward_mode == "FULL_REWARD" and scoring_executed and rubric_evidence.is_file():
        details["components"]["rubrics"]["items"] = read_json(rubric_evidence).get("items", [])
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
    finalize_parser.add_argument("--objective", type=Path, required=True)
    finalize_parser.add_argument("--judge", type=Path, required=True)
    finalize_parser.set_defaults(handler=finalize)

    args = parser.parse_args()
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
