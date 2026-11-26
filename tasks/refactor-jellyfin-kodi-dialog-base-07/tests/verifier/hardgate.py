#!/usr/bin/env python3
"""Pipeline-owned verifier runtime. Generated from frozen execution inputs."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

EXPECTED_BASE = '9f2823a464f4f333affba462198b289766ebb137'
EXPECTED_CONFIG_SHA256 = '2d52a918e2bacf5165d37b397d511e0321466d4ad643f328e835650fce7262cd'
EXPECTED_RUNTIME_VERSION = 'deepswe-verifier-runtime/v4'
EXPECTED_CONFIG_SCHEMA = 'deepswe-verifier-config/v4'
EXPECTED_REPORTS = {'hardgate': '/logs/verifier/hard-gate.json', 'verifier': '/logs/verifier/evidence/verifier.json', 'reward': '/logs/verifier/reward.json', 'reward_text': '/logs/verifier/reward.txt', 'ctrf': '/logs/verifier/ctrf.json', 'reward_details': '/logs/verifier/reward-details.json', 'gate_reward': '/logs/verifier/gate-reward.json'}
STRICT_ASSERTIONS = True
STATUS_ORDER = ("INFRA_ERROR", "INCONCLUSIVE", "FAIL", "PASS")
CANONICAL = {
    "repository": "/workspace/repo",
    "candidate_patch": "/logs/artifacts/model.patch",
    "test_patch": "/tests/verifier/test.patch",
    "p2p_select": "/tests/verifier/p2p_select.txt",
    "hardgate": "/tests/verifier/hardgate.py",
    "verifier": "/tests/verifier/verifier.py",
}


def regular(path):
    path = Path(path)
    if any(parent.is_symlink() for parent in (path, *path.parents)) or not path.is_file():
        raise ValueError("expected regular file: " + str(path))
    return path


def digest(path):
    return hashlib.sha256(regular(path).read_bytes()).hexdigest()


def emit(payload):
    print(json.dumps(payload, sort_keys=True))


def selector_parts(selector, paths):
    if not isinstance(selector, str) or selector != selector.strip():
        raise ValueError("invalid selector")
    if any(not c.isprintable() or c in "*?\\" for c in selector):
        raise ValueError("selectors must be exact")
    parts = selector.split("::")
    if len(parts) < 2 or any(not part for part in parts) or parts[0] not in paths:
        raise ValueError("selector is outside declared test paths")
    # Parameter brackets are literal parts of the exact terminal JUnit name.
    if any("[" in part or "]" in part for part in parts[:-1]):
        raise ValueError("invalid selector path or class")
    leaf = parts[-1]
    if ("[" in leaf or "]" in leaf) and not re.fullmatch(r"[^\[\]]+\[.*\]", leaf):
        raise ValueError("invalid parameter selector")
    return parts[0], leaf


def load_config(path):
    path = regular(path)
    actual_digest = digest(path)
    if actual_digest != EXPECTED_CONFIG_SHA256:
        raise ValueError(
            "frozen config identity mismatch: " + str(path)
            + " expected " + EXPECTED_CONFIG_SHA256 + ", got " + actual_digest
        )
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("schema_version") != EXPECTED_CONFIG_SCHEMA:
        raise ValueError("invalid config schema")
    declared_runtime = value.get("runtime_version", None if STRICT_ASSERTIONS else EXPECTED_RUNTIME_VERSION)
    if declared_runtime != EXPECTED_RUNTIME_VERSION:
        raise ValueError("config/runtime version mismatch")
    if value.get("junit_assertion_adapter") not in (None, "pytest"):
        raise ValueError("invalid JUnit assertion adapter")
    if value.get("base_commit") != EXPECTED_BASE or not re.fullmatch(r"[0-9a-f]{40,64}", EXPECTED_BASE):
        raise ValueError("invalid frozen base commit")
    if any(value.get(key) != expected for key, expected in CANONICAL.items()):
        raise ValueError("invalid canonical runtime paths")
    if value.get("reports") != EXPECTED_REPORTS:
        raise ValueError("invalid canonical report paths")
    if value.get("scoring") != EXPECTED_SCORING:
        raise ValueError("invalid scoring contract")
    command = value.get("command")
    if not isinstance(command, list) or not command or not all(isinstance(x, str) and x for x in command):
        raise ValueError("invalid argv command")
    if not any("{report}" in part for part in command):
        raise ValueError("command must emit a fresh report")
    timeout = value.get("timeout_seconds")
    if type(timeout) not in (int, float) or not 0 < timeout <= 900:
        raise ValueError("invalid timeout")
    if "node_command" in value:
        node_command = value["node_command"]
        if not isinstance(node_command, list) or not node_command or not all(isinstance(part, str) and part for part in node_command):
            raise ValueError("invalid node argv command")
        if not all(any(token in part for part in node_command) for token in ("{selector}", "{report}")):
            raise ValueError("node command requires selector and report placeholders")
        if type(value.get("node_timeout_seconds")) not in (int, float) or not 0 < value["node_timeout_seconds"] <= timeout:
            raise ValueError("invalid node timeout")
    paths = value.get("test_paths")
    if not isinstance(paths, list) or not paths or not all(isinstance(p, str) and p for p in paths):
        raise ValueError("invalid test paths")
    if len(paths) != len(set(paths)):
        raise ValueError("duplicate test paths")
    restoration = value.get("restoration_paths", [])
    if (
        not isinstance(restoration, list) or not all(isinstance(name, str) and name for name in restoration)
        or len(restoration) != len(set(restoration)) or set(restoration).intersection(paths)
    ):
        raise ValueError("invalid restoration paths")
    if type(value.get("require_exec", False)) is not bool:
        raise ValueError("require_exec must be a boolean")
    declared_paths = set(paths) | set(restoration)
    for name in [*paths, *restoration]:
        p = PurePosixPath(name)
        if p.is_absolute() or p.as_posix() != name or "\\" in name or any(part.startswith(".") for part in p.parts):
            raise ValueError("unsafe test path")
        leaf = p.name.lower()
        if not (
            any(part.lower() in {"test", "tests", "__tests__"} for part in p.parts[:-1])
            or leaf.startswith("test_") or "_test." in leaf or ".test." in leaf or ".spec." in leaf
        ):
            raise ValueError("evaluation path is outside test scope")
    files = value.get("evaluation_files")
    if "evaluation_files" in value and (
        not isinstance(files, dict) or set(files) != set(paths)
        or any(not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{64}", sha) for sha in files.values())
    ):
        raise ValueError("invalid frozen evaluation file inventory")
    selections = {}
    names = {}
    gates = value.get("gates")
    if not isinstance(gates, list) or not gates or not all(isinstance(gate, dict) for gate in gates):
        raise ValueError("missing or invalid gates")
    expected_tests = {
        name for gate in gates for name in gate.get("tests", []) if isinstance(name, str)
    }
    for kind, key in (("P2P", "p2p"), ("F2P", "f2p")):
        rows = value.get(key)
        if not isinstance(rows, list) or not rows:
            raise ValueError("both selector inventories must be nonempty")
        for selector in rows:
            selector_parts(selector, declared_paths if kind == "P2P" else set(paths))
            name = selector_test_id(selector, expected_tests)
            if selector in selections or name in names:
                raise ValueError("selectors and JUnit names must be unique")
            selections[selector] = (kind, name)
            names[name] = kind
    gates = value.get("gates")
    if not isinstance(gates, list) or not gates:
        raise ValueError("missing gates")
    owners = {}
    identifiers = set()
    for gate in gates:
        if not isinstance(gate, dict) or gate.get("kind") not in ("P2P", "F2P"):
            raise ValueError("invalid gate")
        identifier = gate.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in identifiers:
            raise ValueError("invalid gate id")
        identifiers.add(identifier)
        tests = gate.get("tests")
        if not isinstance(tests, list) or not tests:
            raise ValueError("missing gate tests")
        for name in tests:
            if not isinstance(name, str) or name in owners or names.get(name) != gate["kind"]:
                raise ValueError("gate selector ownership mismatch")
            owners[name] = identifier
    if set(owners) != set(names):
        raise ValueError("gates do not exactly cover selectors")
    validate_selector_independence(selections, value.get("node_relations", []))
    integrity = value.get("integrity")
    if not isinstance(integrity, dict) or any(
        not isinstance(integrity.get(key), str) or not re.fullmatch(r"[0-9a-f]{64}", integrity[key])
        for key in ("test_patch_sha256", "p2p_select_sha256")
    ):
        raise ValueError("invalid asset digests")
    profile = value.get("execution_profile")
    preparation = normalize_execution_preparation(value.get("execution_preparation"), node_command=bool(value.get("node_command")))
    if (
        not isinstance(profile, dict)
        or profile.get("schema_version") != "grader-verifier-execution-profile/v1"
        or type(profile.get("feasible")) is not bool
        or not isinstance(profile.get("shards"), list)
        or not profile["shards"]
    ):
        raise ValueError("invalid execution profile")
    profile_order = profile.get("selector_order")
    expected_order = [
        *({"selector": selector, "role": "P2P"} for selector in value["p2p"]),
        *({"selector": selector, "role": "F2P"} for selector in value["f2p"]),
    ]
    shard_selectors = [
        selector
        for shard in profile["shards"]
        if isinstance(shard, dict)
        and isinstance(shard.get("selectors"), list)
        and type(shard.get("timeout_seconds")) in (int, float)
        and shard["timeout_seconds"] > 0
        for selector in shard["selectors"]
    ]
    if profile_order != expected_order or shard_selectors != list(selections):
        raise ValueError("execution profile does not exactly cover frozen selectors")
    if profile.get("execution_preparation") != preparation:
        raise ValueError("execution profile preparation differs from the authoritative config")
    if not profile["feasible"] or profile.get("terminal_reason") is not None:
        raise ValueError("RESOURCE_BUDGET_EXHAUSTED")
    return value, selections


def selector_test_id(selector: str, expected_tests: Iterable[str]) -> str:
    """Prefer a full node identity while preserving unambiguous legacy names.

    Syntax and path ownership remain selector_parts' responsibility. A full
    selector and its legacy leaf cannot both own the same executed node.
    """

    expected = set(expected_tests)
    leaf = selector.rsplit("::", 1)[-1]
    matches = {candidate for candidate in (selector, leaf) if candidate in expected}
    if len(matches) != 1:
        raise ValueError(f"selector must have exactly one declared test identity: {selector}")
    return matches.pop()


def normalize_execution_preparation(value: object, *, node_command: bool) -> dict | None:
    """Validate explicit, selector-independent setup/compile declarations."""

    import math

    if value is None:
        return None
    if (not node_command or not isinstance(value, dict)
            or value.get("schema_version") != "grader-verifier-execution-preparation/v1"
            or set(value) - {"schema_version", "setup", "compile"}
            or not set(value).intersection({"setup", "compile"})):
        raise ValueError("execution_preparation requires explicit node_command and a supported preparation schema")
    normalized = {"schema_version": value["schema_version"]}
    for phase in ("setup", "compile"):
        if phase not in value:
            continue
        declaration = value[phase]
        if not isinstance(declaration, dict) or set(declaration) != {"command", "timeout_seconds"}:
            raise ValueError("execution_preparation phase requires command and timeout_seconds")
        command, timeout = declaration["command"], declaration["timeout_seconds"]
        if (not isinstance(command, list) or not command
                or not all(isinstance(part, str) and part for part in command)
                or any(token in part for part in command for token in ("{selector}", "{report}"))):
            raise ValueError("execution_preparation command must be selector-independent nonempty argv")
        if type(timeout) not in (int, float) or not math.isfinite(timeout) or not 0 < timeout <= 900:
            raise ValueError("execution_preparation timeout_seconds must be finite and within (0, 900]")
        normalized[phase] = {"command": list(command), "timeout_seconds": float(timeout)}
    return normalized


def _classify_junit_outcome(outcome, *, strict_assertions=False, junit_assertion_adapter=None):
    """Map one raw JUnit outcome to the canonical node evidence taxonomy."""

    if outcome is None:
        return "PASS", "test", "NONE"
    tag = outcome.tag
    if tag == "skipped":
        return "INCONCLUSIVE", "not-run", "NOT_RUN"
    declared_phase = outcome.get("phase")
    phase_failures = {"setup": "SETUP_ERROR", "compile": "COMPILE_ERROR", "collection": "COLLECTION_ERROR"}
    if declared_phase in phase_failures:
        return "INFRA_ERROR", declared_phase, phase_failures[declared_phase]
    outcome_type = outcome.get("type", "").lower()
    assertion_type = outcome_type.replace("::", ".").rsplit(".", 1)[-1]
    if tag == "failure" and assertion_type in {
        "assertionerror", "assertionfailure", "assertionfailederror", "assertionexception",
        "comparisonfailure", "expectationnotmeterror", "expectationfailure", "asserterror",
    }:
        # A real assertion may discuss a timeout, fixture or compiler result.
        # Its message is not structured evidence of an operational phase.
        return "FAIL", "assertion", "ASSERTION_FAILURE"
    if tag == "failure" and not outcome_type and junit_assertion_adapter == "pytest":
        # The declared producer supplies pytest's structured assertion message.
        # Neither argv inspection nor arbitrary traceback keywords opt into this.
        message = outcome.get("message", "").strip()
        if (message == "AssertionError" or message.startswith("AssertionError:")
                or message.startswith("Failed:")
                or message.startswith("assert ") or message.startswith("assert\t")):
            return "FAIL", "assertion", "ASSERTION_FAILURE"
    detail = " ".join((
        outcome.get("type", ""), outcome.get("message", ""), outcome.text or "",
    )).lower().replace("_", " ").replace("-", " ")
    classifications = (
        (("syntaxerror", "syntax error", "compile error", "compilation error", "compiler error", "javac"),
         "compile", "COMPILE_ERROR"),
        (("collectionerror", "collection error", "during collection", "collect error",
          "importerror while importing", "no tests collected"),
         "collection", "COLLECTION_ERROR"),
        (("pytest.setup", "setup error", "setup failure", "failed on setup", "set up",
          "beforeeach", "beforeall", "before each", "before all", "fixture"),
         "setup", "SETUP_ERROR"),
        (("timeout", "timed out", "deadline exceeded", "deadline exhausted"),
         "process", "TIMEOUT"),
        (("runner exit error", "process crash", "segmentation fault", "segfault",
          "signal ", "killed", "aborted", "core dumped"),
         "process", "PROCESS_CRASH"),
        (("report error", "junit report", "no regular junit", "missing report",
          "invalid report", "report parse"),
         "report", "REPORT_ERROR"),
        (("runner template unresolved", "execution error", "permission denied",
          "environment invalid", "infrastructure error", "infra error"),
         "infrastructure", "INFRA_ERROR"),
    )
    for tokens, phase, failure_class in classifications:
        if any(token in detail for token in tokens):
            return "INFRA_ERROR", phase, failure_class
    if tag == "failure" and not outcome_type and not strict_assertions:
        # Explicit v2 compatibility for legacy JUnit producers without type.
        # Unknown nonempty exception names never establish assertion failure.
        return "FAIL", "assertion", "ASSERTION_FAILURE"
    return "INCONCLUSIVE", "unknown", "UNKNOWN_FAILURE"


def resolve_junit_evidence(
    document, selections, report_reference="junit.xml", *,
    strict_assertions=False, junit_assertion_adapter=None,
):
    """Bind raw JUnit cases to exact selectors and preserve failure semantics.

    ``selections`` maps exact selector to ``(role, JUnit identity)``.  Raw
    report references are retained for diagnosis but are intentionally not
    part of semantic parity comparison.
    """

    if type(strict_assertions) is not bool or junit_assertion_adapter not in (None, "pytest"):
        raise ValueError("invalid JUnit assertion interpretation policy")
    if document.tag not in {"testsuite", "testsuites"}:
        raise ValueError("unrecognized JUnit report root")
    if not isinstance(selections, dict) or not selections:
        raise ValueError("JUnit evidence requires selector mappings")
    expected = {}
    for selector, value in selections.items():
        if (
            not isinstance(selector, str)
            or not isinstance(value, (tuple, list))
            or len(value) != 2
            or not all(isinstance(item, str) and item for item in value)
        ):
            raise ValueError("invalid JUnit selector mapping")
        role, identity = value
        if identity in expected:
            raise ValueError("JUnit identities must be uniquely owned")
        expected[identity] = (selector, role)

    def matches_identity(node, identity):
        name = node.get("name")
        if "::" not in identity:
            return name == identity
        path, qualified = identity.split("::", 1)
        scope, _, leaf = qualified.rpartition("::")
        if name not in {identity, qualified, leaf}:
            return False
        file = node.get("file", "").removeprefix("./")
        classname = node.get("classname", "")
        module = path.rsplit(".", 1)[0].replace("/", ".")
        module_class = module + ("." + scope.replace("::", ".") if scope else "")
        if file and file != path and not (file.startswith("/") and file.endswith("/" + path)):
            return False
        allowed_classes = {module_class, scope.replace("::", ".") if scope else module}
        if name != identity and classname and scope and classname not in allowed_classes:
            return False
        if name != identity and classname and not scope and classname.startswith(module.rpartition(".")[0] + ".") and classname not in allowed_classes:
            return False
        # Custom runners, including Go coverage scripts, often put the source path in classname.
        # In that case classname supplies the file path. The name must still match exactly.
        if (name == identity or classname == path
                or (file and (not scope or classname or name == qualified))
                or classname == module_class):
            return True
        return None

    rows = []
    observed = set()
    cases = list(document.iter("testcase"))
    for node in cases:
        name = node.get("name")
        if not name:
            raise ValueError("missing JUnit test name")
        matches = {identity for identity in expected if matches_identity(node, identity) is True}
        if len(matches) != 1:
            raise ValueError("JUnit testcase identity is missing, extra or ambiguous: " + name)
        identity = matches.pop()
        if identity in observed:
            raise ValueError("duplicate JUnit testcase identity: " + identity)
        observed.add(identity)
        outcomes = [child for child in node if child.tag in {"error", "skipped", "failure"}]
        if len(outcomes) > 1:
            raise ValueError("conflicting or duplicate JUnit outcomes")
        outcome = outcomes[0] if outcomes else None
        typed_status, phase, failure_class = _classify_junit_outcome(
            outcome, strict_assertions=strict_assertions,
            junit_assertion_adapter=junit_assertion_adapter,
        )
        selector, role = expected[identity]
        rows.append({
            "schema_version": "grader-verifier-node-evidence/v1",
            "selector": selector,
            "role": role,
            "typed_status": typed_status,
            "phase": phase,
            "failure_class": failure_class,
            "raw_evidence": {
                "report": report_reference,
                "testcase": {
                    "file": node.get("file", ""),
                    "classname": node.get("classname", ""),
                    "name": name,
                },
                "outcome": None if outcome is None else {
                    "tag": outcome.tag,
                    "type": outcome.get("type", ""),
                    "message": outcome.get("message", ""),
                    "text": outcome.text or "",
                },
                **({"junit_assertion_adapter": junit_assertion_adapter}
                   if junit_assertion_adapter is not None else {}),
            },
        })
    if not rows or observed != set(expected):
        raise ValueError("JUnit observations do not exactly match declared tests (missing/extra tests)")
    for node in cases:
        for attribute in ("parent", "alias_of"):
            related = node.get(attribute)
            if not related:
                continue
            matches = [matches_identity(candidate, related) for candidate in cases]
            if related in expected or any(match is True for match in matches):
                raise ValueError("overlapping JUnit execution identities: " + related)
            if any(match is None for match in matches):
                raise ValueError("ambiguous JUnit relationship identity: " + related)
    for suite in document.iter():
        if suite.tag not in {"testsuite", "testsuites"}:
            continue
        suite_cases = list(suite.iter("testcase"))
        if suite.get("tests") is not None and int(suite.get("tests")) != len(suite_cases):
            raise ValueError("JUnit suite test counter disagrees with testcases")
        for attr, tag in (("errors", "error"), ("failures", "failure"), ("skipped", "skipped")):
            if suite.get(attr) is not None and int(suite.get(attr)) != sum(case.find(tag) is not None for case in suite_cases):
                raise ValueError("JUnit suite counters disagree with testcase results")
        if any(child.tag in {"error", "failure", "skipped"} for child in suite):
            raise ValueError("JUnit suite reported an execution error")
    return rows


def resolve_junit_observations(
    document, expected_tests, *, strict_assertions=False, junit_assertion_adapter=None,
):
    """Compatibility projection of canonical evidence to typed observations."""

    rows = resolve_junit_evidence(
        document,
        {identity: ("UNSPECIFIED", identity) for identity in expected_tests},
        strict_assertions=strict_assertions,
        junit_assertion_adapter=junit_assertion_adapter,
    )
    return {row["selector"]: row["typed_status"] for row in rows}


def validate_node_relations(rows):
    """Validate explicit runner identities without interpreting name delimiters."""

    if not isinstance(rows, (list, tuple)):
        raise ValueError("node_relations must be an array")
    result = []
    seen = set()
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"kind", "node", "related"}:
            raise ValueError("node_relations require kind, node and related")
        kind, node, related = row["kind"], row["node"], row["related"]
        if kind not in ("parent", "alias") or any(
            not isinstance(value, str) or value != value.strip() or "::" not in value
            or not all(value.split("::")) for value in (node, related)
        ) or node == related:
            raise ValueError("invalid node relation identity")
        endpoints = tuple(sorted((node, related))) if kind == "alias" else (node, related)
        key = (kind, *endpoints)
        if key in seen:
            raise ValueError("duplicate node relation")
        seen.add(key)
        result.append(dict(row))
    return tuple(result)


def validate_selector_independence(selectors, node_relations=()):
    """Only evidenced parent/alias relationships establish overlapping owners."""

    selected = set(selectors)
    edges = {}
    for row in validate_node_relations(node_relations):
        edges.setdefault(row["node"], set()).add(row["related"])
        if row["kind"] == "alias":
            edges.setdefault(row["related"], set()).add(row["node"])
    for node in selected:
        pending, visited = list(edges.get(node, ())), {node}
        while pending:
            related = pending.pop()
            if related in visited:
                continue
            if related in selected:
                raise ValueError("overlapping parent and child or alias selectors: " + node)
            visited.add(related)
            pending.extend(edges.get(related, ()))


EXPECTED_SCORING = {'p2p_requires_all': True, 'formula': 'f2p_fraction if p2p_all_passed else 0.0', 'candidate_rejection_reward': -1.0, 'infrastructure_reward': -2.0, 'reward_text': 'error_only'}

def main():
    checks = []
    category = "INFRASTRUCTURE_ERROR"
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--config", default=os.environ.get("HARDGATE_CONFIG", "/tests/config.json"))
        args = parser.parse_args()
        config, _ = load_config(args.config)
        checks.append("frozen-config")
        for variable, name, key in (
            ("HARDGATE_TEST_PATCH", "test_patch", "test_patch_sha256"),
            ("HARDGATE_P2P_SELECT", "p2p_select", "p2p_select_sha256"),
        ):
            path = regular(os.environ.get(variable, config[name]))
            if digest(path) != config["integrity"][key]:
                raise ValueError("frozen asset digest mismatch: " + name)
            checks.append(key)
        text = regular(os.environ.get("HARDGATE_P2P_SELECT", config["p2p_select"])).read_text()
        if not text.endswith("\n") or text.splitlines() != config["p2p"]:
            raise ValueError("P2P inventory mismatch")
        checks.append("p2p-inventory")
        category = "CANDIDATE_REJECTED"
        repository = Path(os.environ.get("CANDIDATE_ROOT", config["repository"]))
        if repository.is_symlink() or not repository.is_dir() or repository.resolve() != Path.cwd().resolve():
            raise ValueError("invalid candidate root")
        for arguments, expected, label in (
            (["rev-parse", "--show-toplevel"], str(repository.resolve()), "candidate-root"),
            (["rev-parse", "--verify", config["base_commit"] + "^{commit}"], EXPECTED_BASE, "base-commit"),
        ):
            value = subprocess.run(["git", "--no-optional-locks", *arguments], cwd=repository,
                                   capture_output=True, text=True, check=True)
            if value.stdout.strip() != expected:
                raise ValueError("candidate Git identity mismatch")
            checks.append(label)
        candidate = regular(os.environ.get("HARDGATE_CANDIDATE_PATCH", config["candidate_patch"]))
        if "candidate_patch_sha256" in config["integrity"] and digest(candidate) != config["integrity"]["candidate_patch_sha256"]:
            raise ValueError("candidate patch digest mismatch")
        checks.append("candidate-patch")
        emit({"status": "PASS", "passed": True, "checks": checks})
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        if isinstance(exc, (OSError, subprocess.TimeoutExpired)):
            category = "INFRASTRUCTURE_ERROR"
        emit({"status": "FAIL", "passed": False, "checks": checks, "error_category": category, "error": str(exc)})
        return 1


if __name__ == "__main__":
    sys.exit(main())
