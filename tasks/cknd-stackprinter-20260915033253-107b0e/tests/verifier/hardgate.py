#!/usr/bin/env python3
"""Compile, integrity and anti-cheat hard gates."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXPECTED_CONFIG_SHA256 = "be8ffbc33b0032664e1ea114ad0fed51e15accf44f1ba92302d686d7767e96d2"


def integrity_failures(config_path: Path, repo: Path, config: dict) -> list[str]:
    """Bind the selected nodes, installed overlay and original regression tests."""
    def digest(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    if digest(config_path) != EXPECTED_CONFIG_SHA256:
        return ["config_sha256_mismatch"]

    failures = []
    verifier_dir = Path(__file__).resolve().parent
    integrity = config["integrity"]
    for name, key in (("test.patch", "test_patch_sha256"),
                      ("p2p_select.txt", "p2p_select_sha256")):
        path = verifier_dir / name
        if path.is_symlink() or not path.is_file() or digest(path) != integrity[key]:
            failures.append(f"verifier_asset_sha256:{name}")

    selection = verifier_dir / "p2p_select.txt"
    expected_selection = "".join(node + "\n" for node in config["p2p"])
    if selection.is_file() and selection.read_text() != expected_selection:
        failures.append("p2p_selection_mismatch")
    all_nodes = config["f2p"] + config["p2p"]
    if len(all_nodes) != len(set(all_nodes)):
        failures.append("duplicate_selected_node")

    for name, expected_digest in config["evaluation_files"].items():
        target = repo / name
        try:
            target.resolve().relative_to(repo.resolve())
        except ValueError:
            failures.append(f"evaluation_path_outside_repo:{name}")
            continue
        if target.is_symlink() or not target.is_file() or digest(target) != expected_digest:
            failures.append(f"evaluation_file_sha256:{name}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    failed_nodes = integrity_failures(args.config, args.repo, config)
    
    if bool(args.apply_failed):
        failed_nodes.append("candidate_patch_apply")

    # 1. Check compilation and syntax
    import py_compile
    compile_paths = config.get("hard_gate", {}).get("compile_paths", [])
    for rel_path in compile_paths:
        target = args.repo / rel_path
        if not target.is_file():
            failed_nodes.append(f"missing_compile_path:{rel_path}")
            continue
        try:
            py_compile.compile(str(target), doraise=True)
        except py_compile.PyCompileError as e:
            failed_nodes.append(f"syntax_error:{rel_path}")

    # 2. Check for hardcoded strings specific to hidden tests
    cheat_tokens = [
        "top_secret_token_value_999",
        "operation_cancelled_by_user",
        "missing_key_x",
        "inner_val_error",
    ]
    for rel_path in compile_paths:
        target = args.repo / rel_path
        if target.is_file():
            content = target.read_text(encoding="utf-8", errors="ignore")
            for token in cheat_tokens:
                if token in content:
                    failed_nodes.append(f"anti_cheat_hardcoded:{token}")

    passed = len(failed_nodes) == 0
    cheat_penalty = config.get("hard_gate", {}).get("cheat_penalty", -1.0) if any("anti_cheat" in n for n in failed_nodes) else 0.0

    result = {
        "passed": passed,
        "apply_failed": bool(args.apply_failed),
        "compile_paths": compile_paths,
        "failed_nodes": failed_nodes,
        "cheat_penalty": cheat_penalty,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
