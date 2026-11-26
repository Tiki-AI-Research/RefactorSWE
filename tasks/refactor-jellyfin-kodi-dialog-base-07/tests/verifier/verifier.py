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
import math
import shutil
import signal
import tempfile
import xml.etree.ElementTree as ET

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
    if digest(path) != EXPECTED_CONFIG_SHA256:
        raise ValueError("frozen config identity mismatch")
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

def bundle_root():
    if os.environ.get("VERIFIER_PACKAGE_ROOT"):
        return Path(os.environ["VERIFIER_PACKAGE_ROOT"])
    own = Path(__file__).resolve().parent
    return own.parent if own.name == "verifier" else own


def asset(root, name):
    nested = root / "verifier" / name
    return nested if nested.is_file() else root / name

class CandidatePatchError(ValueError):
    """A supplied candidate patch cannot be replayed safely."""

    category = "CANDIDATE_PATCH_INVALID"


def candidate_patch(supplied):
    try:
        return regular(supplied).resolve()
    except (OSError, ValueError) as exc:
        raise CandidatePatchError("candidate patch is missing or unsafe: " + str(exc)) from exc


def apply_candidate_patch(repository, patch):
    if patch.stat().st_size == 0:
        return patch
    try:
        subprocess.run(
            ["git", "apply", "--check", "--whitespace=nowarn", str(patch)],
            cwd=repository, capture_output=True, check=True,
        )
        subprocess.run(
            ["git", "apply", "--whitespace=nowarn", str(patch)],
            cwd=repository, capture_output=True, check=True,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        detail = getattr(exc, "stderr", b"")
        if isinstance(detail, bytes):
            detail = detail.decode("utf-8", errors="replace").strip()
        raise CandidatePatchError("candidate patch cannot be applied" + (": " + detail if detail else "")) from exc
    return patch


def write_json(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def copy_candidate(repository, destination, revision=None):
    # Clone Git metadata independently, then overlay the exact current worktree.
    # This supports .git pointer files while preserving dirty/deleted input files.
    cloned = subprocess.run(
        ["git", "clone", "--no-hardlinks", "--quiet", str(repository), str(destination)],
        capture_output=True, text=True,
    )
    if cloned.returncode:
        raise ValueError("candidate repository clone failed: " + cloned.stderr.strip())
    if revision is not None:
        subprocess.run(
            ["git", "checkout", "--quiet", "--detach", "--force", revision],
            cwd=destination, capture_output=True, check=True,
        )
        return
    for child in destination.iterdir():
        if child.name != ".git":
            if child.is_dir() and not child.is_symlink():
                shutil.rmtree(child)
            else:
                child.unlink()
    for child in repository.iterdir():
        if child.name == ".git":
            continue
        target = destination / child.name
        if child.is_symlink():
            target.symlink_to(child.readlink())
        elif child.is_dir():
            shutil.copytree(child, target, symlinks=True)
        else:
            shutil.copy2(child, target)


def worktree_identity(path):
    # Source links are Git semantics; published control files remain regular.
    if path.is_symlink():
        return "symlink:" + os.readlink(path)
    return digest(path)

def canonical_json(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False)


def report_path(logs, name):
    logs = Path(logs).absolute()
    target = logs / name
    if any(path.is_symlink() for path in (target, *target.parents)):
        raise ValueError("report path must not traverse symlinks")
    return target


def read_json(path):
    value = json.loads(regular(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("expected report object")
    return value


def output_path(supplied, logs, name):
    expected = report_path(logs, name)
    if Path(supplied).absolute() != expected:
        raise ValueError("report output differs from the current execution root")
    return expected


def runtime_report_payloads(
    result, gate, hard_gate_success, apply_failed, reward, *, runtime_version,
):
    """Project portable diagnostics without creating a second scoring policy."""

    nodes = result["tests"]
    components = {}
    for role in ("p2p", "f2p"):
        selected = [node for node in nodes if node["role"] == role.upper()]
        passed = sum(node["typed_status"] == "PASS" for node in selected)
        components[role] = {
            "passed": passed, "total": len(selected),
            "score": passed / len(selected) if selected else 0.0,
        }
    p2p, f2p = components["p2p"], components["f2p"]
    p2p_success = bool(p2p["total"] and p2p["passed"] == p2p["total"])
    evaluation_valid = bool(
        hard_gate_success and not apply_failed and p2p["total"] and f2p["total"]
        and result["status"] in ("PASS", "FAIL") and not result.get("error")
        and not result.get("terminal")
        and all(node["typed_status"] in ("PASS", "FAIL") for node in nodes)
    )
    details = {
        "schema_version": "deepswe-reward-details/v1", "runtime_version": runtime_version,
        "hard_gate_success": bool(hard_gate_success), "p2p_success": p2p_success,
        "evaluation_valid": evaluation_valid,
        "evaluation_success": bool(evaluation_valid and p2p_success and f2p["passed"] == f2p["total"]),
        "apply_failed": bool(apply_failed), "reward": reward, "components": components,
        "nodes": nodes, "gates": result["observations"], "hard_gate": gate,
        "status": result["status"],
        "reason_code": (result.get("error_category") or (result.get("terminal") or {}).get("failure_class")
                        or ("COMPLETED" if evaluation_valid else "EVALUATION_INCOMPLETE")),
    }
    for key in ("terminal", "error", "error_category"):
        if key in result:
            details[key] = result[key]
    tests = []
    for node in nodes:
        status = ("passed" if node["typed_status"] == "PASS" else
                  "failed" if node["typed_status"] == "FAIL" else
                  "skipped" if node["failure_class"] == "NOT_RUN" else "other")
        tests.append({
            "name": node["selector"], "testId": node["selector"], "status": status,
            "extra": {"deepswe": {"group": node["role"], **{
                key: node[key] for key in ("typed_status", "phase", "failure_class", "raw_evidence")
            }}},
        })
    statuses = [test["status"] for test in tests]
    ctrf = {"results": {
        "tool": {"name": "deepswe-verifier"}, "tests": tests,
        "summary": {"tests": len(tests), **{
            key: statuses.count(key) for key in ("passed", "failed", "skipped", "pending", "other")
        }},
    }}
    return ctrf, details


def run_process(command, cwd, timeout, stdout=None, stderr=None, env=None):
    process = subprocess.Popen(
        command, cwd=cwd, env=env, stdout=stdout, stderr=stderr,
        start_new_session=os.name == "posix",
    )
    try:
        return process.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        if os.name == "posix":
            os.killpg(process.pid, signal.SIGKILL)
        else:
            process.kill()
        process.wait()
        raise

def aggregate(statuses):
    return next(status for status in STATUS_ORDER if status in statuses)


def project(config, selections, report, returncode):
    terminal = None
    try:
        root = ET.parse(regular(report)).getroot()
        tests = resolve_junit_evidence(
            root, selections, str(report), strict_assertions=STRICT_ASSERTIONS,
            junit_assertion_adapter=config.get("junit_assertion_adapter"),
        )
        by_selector = {row["selector"]: row for row in tests}
        observations = {
            name: by_selector[selector]["typed_status"]
            for selector, (_kind, name) in selections.items()
        }
        if returncode not in (0, 1) and not STRICT_ASSERTIONS:
            raise ValueError("test execution returned an abnormal exit code")
        failed = any(status != "PASS" for status in observations.values())
        error = None
        if returncode is not None and returncode not in (0, 1):
            error = "test execution returned an abnormal exit code"
            terminal = {"typed_status": "INFRA_ERROR", "phase": "process",
                        "failure_class": "PROCESS_CRASH", "returncode": returncode, "error": error}
        elif (returncode == 0 and "FAIL" in observations.values()) or (returncode == 1 and not failed):
            if not STRICT_ASSERTIONS:
                raise ValueError("JUnit and test exit code disagree")
            error = "JUnit and test exit code disagree"
            terminal = {"typed_status": "INFRA_ERROR", "phase": "report",
                        "failure_class": "REPORT_ERROR", "returncode": returncode, "error": error}
    except (OSError, ValueError, ET.ParseError) as exc:
        failure_class = "PROCESS_CRASH" if STRICT_ASSERTIONS and type(returncode) is int and returncode not in (0, 1) else "REPORT_ERROR"
        failure_phase = "process" if failure_class == "PROCESS_CRASH" else "report"
        observations = {name: "INFRA_ERROR" for _kind, name in selections.values()}
        tests = [
            {
                "schema_version": "grader-verifier-node-evidence/v1",
                "selector": selector, "role": role, "typed_status": "INFRA_ERROR",
                "phase": failure_phase, "failure_class": failure_class,
                "raw_evidence": {"report": str(report), "error": str(exc),
                                 **({"returncode": returncode} if STRICT_ASSERTIONS else {})},
            }
            for selector, (role, _name) in selections.items()
        ]
        error = str(exc)
        if STRICT_ASSERTIONS:
            terminal = {"typed_status": "INFRA_ERROR", "phase": failure_phase,
                        "failure_class": failure_class, "returncode": returncode, "error": error}
    payload = {
        "status": "INFRA_ERROR" if terminal else aggregate(set(observations.values())),
        "observations": [
            {"id": gate["id"], "kind": gate["kind"],
             "typed_status": aggregate({observations[name] for name in gate["tests"]})}
            for gate in config["gates"]
        ],
        "tests": [{**row, "kind": row["role"]} for row in tests],
    }
    if error:
        payload["error"] = error
    if terminal:
        payload["terminal"] = terminal
    return payload


def restore_evaluation_files(
    repository: Path, base_commit: str, paths: tuple[str, ...],
    *, restoration_paths: tuple[str, ...] = (),
) -> None:
    """Restore authority only in a private execution copy before test.patch.

    Restore exactly the declared test and support files from frozen Git blobs.
    Additional restoration paths are immutable support assets or explicit absent
    paths to clear; only paths may enter test.patch. No language or directory
    discovery expands this authority. Files outside the declaration stay intact.
    Source symlinks elsewhere remain unchanged; evaluation ancestors must be
    ordinary directories, because following a Candidate link is unsafe.
    This self-contained function is also embedded in the published grader.
    """

    import subprocess
    from pathlib import Path, PurePosixPath

    def run_git(*arguments: str, data: bytes | None = None) -> bytes:
        result = subprocess.run(
            ["git", "--no-optional-locks", "--literal-pathspecs", *arguments],
            cwd=repository, input=data, capture_output=True, check=False,
        )
        if result.returncode:
            raise ValueError(result.stderr.decode("utf-8", errors="replace").strip())
        return result.stdout

    if repository.is_symlink() or not repository.is_dir():
        raise ValueError("unsafe private evaluation repository")
    if len(paths) != len(set(paths)) or len(restoration_paths) != len(set(restoration_paths)):
        raise ValueError("duplicate evaluation paths")
    selected = set(paths) | set(restoration_paths)
    if not selected:
        raise ValueError("no evaluation paths declared")
    for name in selected:
        relative = PurePosixPath(name)
        if (
            not name or relative.is_absolute() or ".." in relative.parts
            or any(part.startswith(".") for part in relative.parts)
            or "\\" in name or relative.as_posix() != name
        ):
            raise ValueError(f"unsafe evaluation path: {name}")
        leaf = relative.name.lower()
        if not (
            any(part.lower() in {"test", "tests", "__tests__"} for part in relative.parts[:-1])
            or leaf.startswith("test_") or "_test." in leaf
            or ".test." in leaf or ".spec." in leaf
        ):
            raise ValueError(f"evaluation path is outside test scope: {name}")
    tree = run_git("ls-tree", "--full-tree", "-z", base_commit, "--", *sorted(selected))
    blobs: dict[str, tuple[str, bytes]] = {}
    for record in tree.split(b"\0"):
        if not record:
            continue
        header, raw_name = record.split(b"\t", 1)
        mode, kind, object_id = header.decode("ascii").split()
        name = raw_name.decode("utf-8")
        if name not in selected or mode not in {"100644", "100755"} or kind != "blob":
            raise ValueError(f"frozen evaluation path is not a regular Git file: {name}")
        content = run_git("cat-file", "blob", object_id)
        if run_git("hash-object", "--stdin", data=content).decode().strip() != object_id:
            raise ValueError(f"frozen evaluation blob identity differs: {name}")
        blobs[name] = (mode, content)
    # Check the entire path set before replacing any evaluation file.
    for name in sorted(selected):
        target = repository / name
        for parent in target.parents:
            if parent == repository:
                break
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                raise ValueError(f"unsafe evaluation ancestor: {name}")
        if target.exists() and not target.is_file() and not target.is_symlink():
            raise ValueError(f"evaluation path conflicts with a directory: {name}")
    for name in sorted(selected):
        target = repository / name
        if target.exists() or target.is_symlink():
            target.unlink()
        if name in blobs:
            mode, content = blobs[name]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
            target.chmod(0o755 if mode == "100755" else 0o644)




import contextlib

class ReplayEnvironmentError(ValueError):
    """Pre-execution filesystem contract failure (not a runner test failure)."""

@contextlib.contextmanager
def replay_environment(repository, evidence, report=None, environment=None, temporary_root=None, executable_root=None, require_exec=False):
    """Check real process permissions and isolate all temporary runner writes."""

    import os
    from pathlib import Path
    import subprocess
    import tempfile

    if type(require_exec) is not bool:
        raise ReplayEnvironmentError("require_exec must be a boolean")

    def directory(value, label, *, create=False):
        path = Path(value)
        if not path.is_absolute():
            raise ReplayEnvironmentError(label + " must be an absolute directory")
        if any(parent.is_symlink() for parent in (path, *path.parents)):
            raise ReplayEnvironmentError(label + " must not use symlink directories")
        if create:
            try:
                path.mkdir(parents=True, exist_ok=True)
            except OSError as exc:
                raise ReplayEnvironmentError(label + " cannot be created by the execution user") from exc
        if not path.is_dir():
            raise ReplayEnvironmentError(label + " is not a directory")
        # os.access and host-side mode checks do not prove that the image's
        # configured uid can write a bind mount. Exercise a real write here.
        try:
            with tempfile.TemporaryFile(dir=path) as probe:
                probe.write(b"verifier environment preflight\n")
                probe.flush()
        except OSError as exc:
            raise ReplayEnvironmentError(label + " is not writable by the execution user") from exc
        return path.resolve()

    repository = directory(repository, "repository working directory")
    evidence = directory(evidence, "evidence directory")
    if report is not None:
        report = Path(report)
        if not report.is_absolute() or ".." in report.parts:
            raise ReplayEnvironmentError("report must be an absolute path inside evidence directory")
        if not report.is_relative_to(evidence) or report == evidence:
            raise ReplayEnvironmentError("report is outside evidence directory")
        if any(parent.is_symlink() for parent in (report, *report.parents)):
            raise ReplayEnvironmentError("report must not use symlink paths")
        if report.exists() and not report.is_file():
            raise ReplayEnvironmentError("report must be a regular file")
        directory(report.parent, "report parent directory", create=True)
        if report.exists():
            try:
                with report.open("ab"):
                    pass
            except OSError as exc:
                raise ReplayEnvironmentError("report is not writable by the execution user") from exc
    execution_env = {**os.environ, **(environment or {})}
    with contextlib.ExitStack() as cleanup:
        try:
            temporary_root = temporary_root or execution_env.get("TMPDIR") or tempfile.gettempdir()
            temporary_root = directory(temporary_root, "temporary root directory")
            temporary = cleanup.enter_context(
                tempfile.TemporaryDirectory(prefix="verifier-execution-", dir=temporary_root)
            )
        except OSError as exc:
            raise ReplayEnvironmentError("cannot create isolated temporary directory") from exc
        execution_env.update(TMPDIR=temporary, TMP=temporary, TEMP=temporary)
        # Temporary data may be noexec; declared generated executables use a
        # separate directory, with tool-specific variables mapped by the runner.
        executable_root = directory(
            executable_root or execution_env.get("VERIFIER_EXEC_DIR") or evidence,
            "executable root directory",
        )
        try:
            executable = cleanup.enter_context(
                tempfile.TemporaryDirectory(prefix="verifier-executable-", dir=executable_root)
            )
            requires_exec = require_exec or execution_env.get("VERIFIER_REQUIRE_EXEC") == "1"
            if requires_exec:
                probe = Path(executable) / "probe"
                probe.write_bytes(b"#!/bin/sh\nexit 0\n")
                probe.chmod(0o700)
                try:
                    checked = subprocess.run([str(probe)], capture_output=True, timeout=5, check=False)
                    if checked.returncode:
                        raise ReplayEnvironmentError("executable directory probe failed")
                finally:
                    probe.unlink()
        except (OSError, subprocess.SubprocessError) as exc:
            raise ReplayEnvironmentError("executable directory does not permit execution") from exc
        execution_env.update(VERIFIER_EXEC_DIR=executable)
        yield execution_env

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

def _preparation_manifest(directory):
    """Bind all input/artifact bytes, modes and in-root source links."""

    import hashlib
    from pathlib import Path

    directory = Path(directory)
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError("preparation directory is unavailable or unsafe")
    manifest = {}
    for path in sorted(directory.rglob("*")):
        name = path.relative_to(directory)
        if path.is_symlink():
            if not path.resolve().is_relative_to(directory.resolve()):
                raise ValueError("preparation input/artifact link escapes its frozen root")
            manifest[name.as_posix()] = ["symlink", str(path.readlink())]
        elif path.is_file():
            manifest[name.as_posix()] = [
                hashlib.sha256(path.read_bytes()).hexdigest(), path.stat().st_mode & 0o777,
            ]
        elif not path.is_dir():
            raise ValueError("preparation input/artifact has an unsupported file type")
    return manifest

def _preparation_inputs(repository, environment, declaration, command, timeout, total_timeout, shards):
    """Describe frozen preparation inputs without recording environment secrets."""

    import hashlib
    import json
    from pathlib import Path
    import sys

    def fingerprint(value):
        return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

    controls = {}
    for key in ("VERIFIER_CONFIG", "VERIFIER_P2P_SELECT"):
        if not environment.get(key):
            continue
        path = Path(environment[key])
        if any(parent.is_symlink() for parent in (path, *path.parents)) or not path.is_file():
            raise ValueError("preparation frozen control input is unavailable or unsafe")
        controls[key] = [hashlib.sha256(path.read_bytes()).hexdigest(), path.stat().st_mode & 0o777]
    return {
        "repository": str(Path(repository).resolve()),
        "repository_sha256": fingerprint(_preparation_manifest(repository)),
        "controls": controls, "environment_sha256": fingerprint(dict(environment)),
        "preparation": declaration, "node_command": list(command),
        "node_timeout_seconds": timeout, "total_timeout_seconds": total_timeout,
        "shards": shards, "python": sys.version,
    }

def _prepare_node_execution(declaration, command, repository, timeout, environment, total_timeout, shards, deadline, logs):
    """Prepare once in this execution context; never load an earlier receipt."""

    import hashlib
    import json
    import os
    from pathlib import Path
    import re
    import signal
    import subprocess
    import sys
    import tempfile
    import time

    record = {"schema_version": "grader-verifier-preparation-execution/v1", "status": "RUNNING", "phases": []}
    execution_env = dict(environment)
    phase = "setup"
    try:
        executable = Path(environment.get("VERIFIER_EXEC_DIR", ""))
        if (not executable.is_absolute() or not executable.is_dir()
                or any(parent.is_symlink() for parent in (executable, *executable.parents))
                or executable.resolve().is_relative_to(Path(repository).resolve())):
            raise ValueError("preparation requires an isolated executable scratch directory outside the worktree")
        inputs = _preparation_inputs(repository, environment, declaration, command, timeout, total_timeout, shards)
        record["inputs"] = inputs
        record["fingerprint"] = hashlib.sha256(json.dumps(inputs, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        artifacts = Path(tempfile.mkdtemp(prefix="verifier-preparation-", dir=executable))
        execution_env["VERIFIER_PREPARATION_DIR"] = str(artifacts)
        record["artifacts_directory"] = str(artifacts)
        logs = Path(logs)
        logs.mkdir()
        replacements = {
            "{repository}": str(repository), "{workspace}": str(repository), "{python}": sys.executable,
            "{config}": environment.get("VERIFIER_CONFIG", ""),
            "{p2p_select}": environment.get("VERIFIER_P2P_SELECT", ""),
        }
        template = re.compile("|".join(re.escape(token) for token in replacements))
        for phase in ("setup", "compile"):
            if phase not in declaration:
                continue
            step = declaration[phase]
            missing = {match.group(0) for part in step["command"] for match in template.finditer(part)
                       if not str(replacements[match.group(0)])}
            if missing:
                raise ValueError("RUNNER_TEMPLATE_UNRESOLVED: preparation input template is unavailable")
            argv = [template.sub(lambda match: str(replacements[match.group(0)]), part) for part in step["command"]]
            started = time.monotonic()
            process_deadline = started + step["timeout_seconds"]
            if deadline is not None:
                process_deadline = min(process_deadline, deadline)
            if process_deadline <= started:
                record.update(status="NOT_RUN", phase="not-run", failure_class="NOT_RUN",
                              error="replay deadline exhausted before preparation launch")
                return execution_env, record
            observed = {"phase": phase, "command": argv, "status": "RUNNING"}
            record["phases"].append(observed)
            with (logs / (phase + ".stdout.log")).open("w") as stdout, (logs / (phase + ".stderr.log")).open("w") as stderr:
                if process_deadline <= time.monotonic():
                    observed["status"] = "NOT_RUN"
                    record.update(status="NOT_RUN", phase="not-run", failure_class="NOT_RUN",
                                  error="preparation deadline exhausted while opening launch logs")
                    return execution_env, record
                process = subprocess.Popen(argv, cwd=artifacts, env=execution_env, stdout=stdout, stderr=stderr,
                                           start_new_session=os.name == "posix")
                remaining = max(0.0, process_deadline - time.monotonic())
                observed["timeout_seconds"] = remaining
                try:
                    code = process.wait(timeout=remaining)
                except subprocess.TimeoutExpired:
                    try:
                        if os.name == "posix":
                            os.killpg(process.pid, signal.SIGKILL)
                        else:
                            process.kill()
                    except ProcessLookupError:
                        pass
                    process.wait()
                    observed["status"] = "TIMEOUT"
                    record.update(status="TIMEOUT", phase="process", failure_class="TIMEOUT",
                                  error="preparation process exceeded its remaining deadline")
                    return execution_env, record
            observed.update(status="COMPLETED", returncode=code)
            if code != 0:
                record.update(status="FAILED", phase=phase, failure_class=phase.upper() + "_ERROR",
                              error=phase + " error: preparation process exited " + str(code))
                return execution_env, record
            if _preparation_inputs(repository, environment, declaration, command, timeout, total_timeout, shards) != inputs:
                raise ValueError("preparation modified frozen production, test or control inputs")
        record.update(status="COMPLETED", artifacts=_preparation_manifest(artifacts))
    except (OSError, ValueError) as exc:
        record.update(status="INFRA_ERROR", phase="infrastructure", failure_class="INFRA_ERROR", error=str(exc))
    return execution_env, record

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

def run_node_commands(
    command, selections, repository, report, timeout, environment,
    total_timeout=None, shards=None,
):
    """Run exact nodes independently; aggregate real cases and execution errors."""

    import copy
    import json
    import os
    from pathlib import Path
    import re
    import signal
    import subprocess
    import sys
    import tempfile
    import time
    import xml.etree.ElementTree as ET

    declaration = None
    assertion_policy = {"strict_assertions": False, "junit_assertion_adapter": None}
    if environment.get("VERIFIER_CONFIG"):
        configuration = json.loads(Path(environment["VERIFIER_CONFIG"]).read_text())
        assertion_policy.update(
            strict_assertions=configuration.get("runtime_version") == "deepswe-verifier-runtime/v4",
            junit_assertion_adapter=configuration.get("junit_assertion_adapter"),
        )
        if assertion_policy["junit_assertion_adapter"] not in (None, "pytest"):
            raise ValueError("unsupported junit_assertion_adapter")
        declaration = normalize_execution_preparation(configuration.get("execution_preparation"), node_command=bool(command))
    report = Path(report)
    root = report.parent / "node-executions"
    root.mkdir(exist_ok=False)
    document = ET.Element("testsuites")
    normalized = {
        selector: tuple(value) if isinstance(value, (tuple, list)) else ("UNSPECIFIED", value)
        for selector, value in selections.items()
    }
    if shards is None:
        shards = [{
            "id": "shard-001", "selectors": list(normalized),
            "timeout_seconds": total_timeout or max(timeout, timeout * len(normalized)),
        }]
    if not isinstance(shards, list) or not shards:
        raise ValueError("execution shards must be a nonempty array")
    execution_order = []
    for shard in shards:
        if (
            not isinstance(shard, dict)
            or not isinstance(shard.get("id"), str)
            or not isinstance(shard.get("selectors"), list)
            or type(shard.get("timeout_seconds")) not in (int, float)
            or shard["timeout_seconds"] <= 0
        ):
            raise ValueError("execution shard has an invalid shape")
        for selector in shard["selectors"]:
            if selector not in normalized:
                raise ValueError("execution shard contains an unknown selector")
            role, identity = normalized[selector]
            execution_order.append(
                (selector, role, identity, shard["id"], float(shard["timeout_seconds"]))
            )
    if [row[0] for row in execution_order] != list(normalized):
        raise ValueError("execution shards must exactly preserve frozen selector order")
    records = [
        {"selector": selector, "role": role, "node": identity, "shard": shard_id,
         "command": [], "status": "NOT_RUN", "returncode": None}
        for selector, role, identity, shard_id, _ in execution_order
    ]
    failed = False
    task_deadline = time.monotonic() + total_timeout if total_timeout is not None else None
    current_shard = None
    shard_deadline = None

    preparation = None
    preparation_environment = dict(environment)

    def persist():
        payload = {"nodes": records, "assertion_policy": assertion_policy}
        if preparation is not None:
            payload["execution_preparation"] = preparation
        for path, content in (
            (report, ET.tostring(document, encoding="utf-8", xml_declaration=True)),
            (root / "result.json", (json.dumps(payload, indent=2) + "\n").encode()),
        ):
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".node-write-", delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(content)
            try:
                temporary.replace(path)
            finally:
                temporary.unlink(missing_ok=True)

    persist()
    if declaration is not None:
        environment, preparation = _prepare_node_execution(
            declaration, command, repository, timeout, environment, total_timeout, shards,
            task_deadline, root / "preparation",
        )
        if preparation["status"] != "COMPLETED":
            for record in records:
                suite = ET.SubElement(document, "testsuite", name=record["selector"])
                node = ET.SubElement(suite, "testcase", name=record["node"])
                record.update(error=preparation["error"], launched=False,
                              blocked_by={"phase": preparation["phase"], "failure_class": preparation["failure_class"]})
                if preparation["status"] == "NOT_RUN":
                    ET.SubElement(node, "skipped", message=preparation["error"])
                else:
                    record["status"] = "PREPARATION_ERROR"
                    ET.SubElement(node, "error", type=preparation["failure_class"], message=preparation["error"])
            evidence = resolve_junit_evidence(document, normalized, report.name, **assertion_policy)
            for record, row in zip(records, evidence):
                record["node_evidence"] = row
            persist()
            return 1
        persist()
    for index, (selector, role, identity, shard_id, shard_timeout) in enumerate(execution_order, start=1):
        if shard_id != current_shard:
            current_shard = shard_id
            shard_deadline = time.monotonic() + shard_timeout
        directory = root / f"node-{index:04d}"
        directory.mkdir()
        node_report = directory / "junit.xml"
        replacements = {
            "{selector}": selector, "{report}": str(node_report), "{repository}": repository,
            "{workspace}": repository, "{python}": sys.executable,
            "{config}": environment.get("VERIFIER_CONFIG", ""),
            "{p2p_select}": environment.get("VERIFIER_P2P_SELECT", ""),
        }
        template = re.compile("|".join(re.escape(token) for token in replacements))
        used = {
            match.group(0)
            for part in command
            for match in template.finditer(part)
        }
        missing = sorted(token for token in used if not str(replacements[token]))
        argv = [
            template.sub(lambda match: str(replacements[match.group(0)]), part)
            for part in command
        ]
        record = records[index - 1]
        record["command"] = argv
        if missing:
            error_type = "RUNNER_TEMPLATE_UNRESOLVED"
            message = "required command template values are unavailable: " + ", ".join(missing)
            record.update(status=error_type, error=message)
            suite = ET.SubElement(document, "testsuite", name=selector)
            node = ET.SubElement(suite, "testcase", name=identity)
            ET.SubElement(node, "error", type=error_type, message=message)
            failed = True
            persist()
            continue
        if preparation is not None:
            try:
                if (_preparation_manifest(preparation["artifacts_directory"]) != preparation["artifacts"]
                        or _preparation_inputs(repository, preparation_environment, declaration, command, timeout,
                                               total_timeout, shards) != preparation["inputs"]):
                    raise ValueError("infrastructure error: preparation reuse invalidated by frozen input/artifact drift")
            except (OSError, ValueError) as exc:
                record.update(status="EXECUTION_ERROR", error=str(exc), launched=False)
                suite = ET.SubElement(document, "testsuite", name=selector)
                node = ET.SubElement(suite, "testcase", name=identity)
                ET.SubElement(node, "error", type="EXECUTION_ERROR", message=str(exc))
                failed = True
                persist()
                continue
        remaining = shard_deadline - time.monotonic() if shard_deadline is not None else timeout
        if task_deadline is not None:
            remaining = min(remaining, task_deadline - time.monotonic())
        if remaining <= 0:
            record["error"] = "overall replay deadline exhausted before node launch"
            failed = True
            suite = ET.SubElement(document, "testsuite", name=selector)
            node = ET.SubElement(suite, "testcase", name=identity)
            ET.SubElement(node, "skipped", message=record["error"])
            persist()
            continue
        record["status"] = "RUNNING"
        persist()
        error_type = None
        message = None
        with (directory / "stdout.log").open("w") as stdout, (directory / "stderr.log").open("w") as stderr:
            try:
                # Check again after checkpoint/log I/O, and use an absolute
                # deadline so process startup cannot refresh a stale budget.
                launch_started = time.monotonic()
                process_deadline = launch_started + timeout
                if shard_deadline is not None:
                    process_deadline = min(process_deadline, shard_deadline)
                if task_deadline is not None:
                    process_deadline = min(process_deadline, task_deadline)
                if process_deadline <= launch_started:
                    record.update(
                        status="NOT_RUN",
                        error="replay deadline exhausted while preparing node launch",
                    )
                else:
                    process = subprocess.Popen(argv, cwd=repository, env=environment, stdout=stdout, stderr=stderr,
                                               start_new_session=os.name == "posix")
                    wait_timeout = max(0.0, process_deadline - time.monotonic())
                    record["timeout_seconds"] = wait_timeout
                    try:
                        record["returncode"] = process.wait(timeout=wait_timeout)
                        record["status"] = "COMPLETED"
                    except subprocess.TimeoutExpired:
                        try:
                            if os.name == "posix":
                                os.killpg(process.pid, signal.SIGKILL)
                            else:
                                process.kill()
                        except ProcessLookupError:
                            pass
                        process.wait()
                        record["status"] = error_type = "TIMEOUT"
                        message = f"node process exceeded {wait_timeout:g}s remaining execution budget"
            except OSError as exc:
                record["status"] = error_type = "EXECUTION_ERROR"
                message = str(exc)
        cases = []
        if not error_type and record["status"] != "NOT_RUN":
            try:
                if node_report.is_symlink() or not node_report.is_file():
                    raise ValueError("node produced no regular JUnit report")
                node_document = ET.parse(node_report).getroot()
                evidence = resolve_junit_evidence(
                    node_document, {selector: (role, identity)},
                    "node-executions/node-%04d/junit.xml" % index,
                    **assertion_policy,
                )
                observation = evidence[0]["typed_status"]
                if record["returncode"] not in {0, 1}:
                    error_type = "RUNNER_EXIT_ERROR"
                    raise ValueError(f"node process exited abnormally: exit {record['returncode']}")
                nonpass = observation != "PASS"
                if record["returncode"] == 1 and not nonpass or record["returncode"] == 0 and observation == "FAIL":
                    raise ValueError("node exit code conflicts with JUnit result")
                cases = [copy.deepcopy(node) for node in node_document.iter("testcase")]
                record["observation"] = observation
                record["node_evidence"] = evidence[0]
                failed = failed or nonpass
            except (OSError, ValueError, ET.ParseError) as exc:
                error_type = error_type or "REPORT_ERROR"
                message = str(exc)
        suite = ET.SubElement(document, "testsuite", name=selector)
        if record["status"] == "NOT_RUN":
            failed = True
            node = ET.SubElement(suite, "testcase", name=identity)
            ET.SubElement(node, "skipped", message=record["error"])
        elif error_type:
            failed = True
            record.update(status=error_type, error=message)
            # This is an observed process failure for a node we actually
            # launched, never an invented assertion or a not-run PASS/FAIL.
            node = ET.SubElement(suite, "testcase", name=identity)
            ET.SubElement(node, "error", type=error_type, message=message or error_type)
        else:
            suite.extend(cases)
        persist()
    return int(failed)

def read_node_execution_evidence(report, *, expected_assertion_policy=None, expected_selectors=None):
    """Keep completed observations even when a global deadline leaves gaps."""

    import json
    from pathlib import Path
    import xml.etree.ElementTree as ET

    root = Path(report).parent / "node-executions"
    records_path = root / "result.json"

    def report_failure(error):
        return {
            "status": "INFRA_ERROR", "error": error,
            "terminal": {
                "typed_status": "INFRA_ERROR", "phase": "report", "failure_class": "REPORT_ERROR",
                "error": error, "raw_evidence": {"report": "node-executions/result.json"},
            },
        }

    if root.is_symlink() or records_path.is_symlink() or not records_path.is_file():
        return report_failure("missing or unsafe required node ledger") if expected_assertion_policy is not None else {}
    try:
        payload = json.loads(records_path.read_text(encoding="utf-8"))
        assertion_policy = payload.get("assertion_policy", {"strict_assertions": False, "junit_assertion_adapter": None})
        valid_policy = (isinstance(assertion_policy, dict)
                and set(assertion_policy) == {"strict_assertions", "junit_assertion_adapter"}
                and type(assertion_policy["strict_assertions"]) is bool
                and assertion_policy["junit_assertion_adapter"] in (None, "pytest"))
        policy_error = None
        if expected_assertion_policy is not None:
            if (not isinstance(expected_assertion_policy, dict)
                    or set(expected_assertion_policy) != {"strict_assertions", "junit_assertion_adapter"}
                    or type(expected_assertion_policy["strict_assertions"]) is not bool
                    or expected_assertion_policy["junit_assertion_adapter"] not in (None, "pytest")):
                raise ValueError("invalid expected JUnit assertion policy")
            if not valid_policy or payload.get("assertion_policy") != expected_assertion_policy:
                policy_error = "node ledger assertion policy disagrees with the frozen runtime config"
            assertion_policy = expected_assertion_policy
        elif not valid_policy:
            raise ValueError("invalid frozen JUnit assertion policy")
        records = payload["nodes"]
        if not isinstance(records, list):
            raise ValueError("node ledger records must be an array")
        if expected_assertion_policy is not None:
            if (not records or any(not isinstance(record, dict)
                    or any(not isinstance(record.get(key), str) or not record[key]
                           for key in ("selector", "node", "role", "status"))
                    or (record.get("status") == "COMPLETED" and type(record.get("returncode")) is not int)
                    for record in records)
                    or len({record["selector"] for record in records}) != len(records)):
                raise ValueError("required node ledger has missing or duplicate node records")
            if expected_selectors is not None and {record["selector"] for record in records} != set(expected_selectors):
                raise ValueError("node ledger disagrees with the frozen exact selector inventory")
        partial = {}
        evidence = []
        missing = []
        blocked_evidence = {}
        if not policy_error and any(record.get("status") == "PREPARATION_ERROR" for record in records):
            aggregate = Path(report)
            if aggregate.is_symlink() or not aggregate.is_file():
                raise ValueError("preparation failure produced no regular aggregate report")
            selections = {record["selector"]: (record["role"], record["node"]) for record in records}
            blocked_evidence = {
                row["selector"]: row for row in resolve_junit_evidence(
                    ET.parse(aggregate).getroot(), selections, aggregate.name,
                    **assertion_policy,
                )
            }
        for index, record in enumerate(records, start=1):
            identity = record.get("node")
            if not isinstance(identity, str):
                continue
            if policy_error:
                missing.append(identity)
                evidence.append({
                    "schema_version": "grader-verifier-node-evidence/v1",
                    "selector": record.get("selector", identity), "role": record.get("role", "UNSPECIFIED"),
                    "typed_status": "INFRA_ERROR", "phase": "report", "failure_class": "REPORT_ERROR",
                    "raw_evidence": {
                        "report": "node-executions/result.json", "error": policy_error,
                        "expected_assertion_policy": expected_assertion_policy,
                        "observed_assertion_policy": payload.get("assertion_policy"),
                    },
                })
            elif record.get("status") in {"NOT_RUN", "RUNNING"}:
                missing.append(identity)
                evidence.append({
                    "schema_version": "grader-verifier-node-evidence/v1",
                    "selector": record.get("selector", identity),
                    "role": record.get("role", "UNSPECIFIED"),
                    "typed_status": "INCONCLUSIVE", "phase": "not-run",
                    "failure_class": "NOT_RUN",
                    "raw_evidence": {"report": "node-executions/result.json", "status": record.get("status")},
                })
            elif record.get("status") == "PREPARATION_ERROR":
                missing.append(identity)
                row = blocked_evidence.get(record.get("selector"))
                if isinstance(row, dict) and row == record.get("node_evidence"):
                    evidence.append(row)
            elif record.get("status") == "COMPLETED" and record.get("returncode") in {0, 1}:
                node_report = root / f"node-{index:04d}" / "junit.xml"
                try:
                    if node_report.is_symlink() or not node_report.is_file():
                        raise ValueError("completed node has no regular JUnit report")
                    row = resolve_junit_evidence(
                        ET.parse(node_report).getroot(),
                        {record.get("selector", identity): (record.get("role", "UNSPECIFIED"), identity)},
                        "node-executions/node-%04d/junit.xml" % index,
                        **assertion_policy,
                    )[0]
                    if (record.get("observation") != row["typed_status"]
                            or record["returncode"] == 0 and row["typed_status"] == "FAIL"
                            or record["returncode"] == 1 and row["typed_status"] == "PASS"):
                        raise ValueError("completed node observation/exit conflicts with real JUnit")
                    cached = record.get("node_evidence")
                    if cached is not None and cached != row:
                        raise ValueError("completed node canonical evidence conflicts with real JUnit")
                except (OSError, ValueError, ET.ParseError) as exc:
                    missing.append(identity)
                    evidence.append({
                        "schema_version": "grader-verifier-node-evidence/v1",
                        "selector": record.get("selector", identity), "role": record.get("role", "UNSPECIFIED"),
                        "typed_status": "INFRA_ERROR", "phase": "report", "failure_class": "REPORT_ERROR",
                        "raw_evidence": {"report": "node-executions/result.json", "error": str(exc),
                                         "junit_report": "node-executions/node-%04d/junit.xml" % index},
                    })
                else:
                    partial[identity] = row["typed_status"]
                    evidence.append(row)
            elif isinstance(record.get("selector"), str):
                if expected_assertion_policy is not None:
                    missing.append(identity)
                failure_class = {
                    "TIMEOUT": "TIMEOUT", "REPORT_ERROR": "REPORT_ERROR",
                    "RUNNER_EXIT_ERROR": "PROCESS_CRASH",
                }.get(record.get("status"), "INFRA_ERROR")
                phase = {
                    "TIMEOUT": "process", "REPORT_ERROR": "report",
                    "RUNNER_EXIT_ERROR": "process",
                }.get(record.get("status"), "infrastructure")
                evidence.append({
                    "schema_version": "grader-verifier-node-evidence/v1",
                    "selector": record["selector"], "role": record.get("role", "UNSPECIFIED"),
                    "typed_status": "INFRA_ERROR", "phase": phase,
                    "failure_class": failure_class,
                    "raw_evidence": {"report": "node-executions/result.json", "status": record.get("status")},
                })
        result = {"partial_observations": partial, "partial_node_evidence": evidence,
                  "missing_nodes": missing, "node_execution": records}
        if "execution_preparation" in payload:
            result["execution_preparation"] = payload["execution_preparation"]
        if expected_assertion_policy is not None and (policy_error or missing):
            result.update(report_failure(policy_error or "required node ledger has uncompleted or untrusted nodes"))
        return result
    except (OSError, ValueError, KeyError, TypeError, AttributeError, ET.ParseError) as exc:
        return report_failure(str(exc)) if expected_assertion_policy is not None else {}



PARITY_FIELDS = ('role', 'typed_status', 'phase', 'failure_class')

def _evidence_index(rows: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
    if not isinstance(rows, list):
        raise ValueError("node evidence must be an array")
    indexed = {}
    for row in rows:
        if not isinstance(row, dict) or row.get("schema_version") != "grader-verifier-node-evidence/v1":
            raise ValueError("node evidence has an invalid schema")
        selector = row.get("selector")
        if not isinstance(selector, str) or not selector or selector in indexed:
            raise ValueError("node evidence selectors must be unique non-empty strings")
        projected = {field: row.get(field) for field in PARITY_FIELDS}
        if not all(isinstance(value, str) and value for value in projected.values()):
            raise ValueError("node evidence parity fields must be non-empty strings")
        indexed[selector] = projected
    return indexed


def compare_node_evidence(
    independent: list[dict[str, Any]],
    published: list[dict[str, Any]],
    *,
    evaluation_digest: str | None = None,
) -> dict[str, Any]:
    """Compare semantic fields while leaving each side's raw evidence intact."""

    left = _evidence_index(independent)
    right = _evidence_index(published)
    mismatches = [
        {"selector": selector, "independent": left.get(selector), "published": right.get(selector)}
        for selector in sorted(set(left) | set(right))
        if left.get(selector) != right.get(selector)
    ]
    result: dict[str, Any] = {
        "schema_version": "grader-verifier-evidence-parity/v1",
        "status": "MISMATCH" if mismatches else "PASS",
        "fields": ["selector", *PARITY_FIELDS],
        "mismatches": mismatches,
    }
    if evaluation_digest is not None:
        result["evaluation_digest"] = evaluation_digest
    return result


def not_run(config, selections, error):
    return {
        "status": "INCONCLUSIVE",
        "tests": [{"schema_version": "grader-verifier-node-evidence/v1", "selector": selector,
                   "role": role, "kind": role, "typed_status": "INCONCLUSIVE", "phase": "not-run",
                   "failure_class": "NOT_RUN", "raw_evidence": {"error": error, "execution_started": False}}
                  for selector, (role, _) in selections.items()],
        "observations": [{"id": gate["id"], "kind": gate["kind"], "typed_status": "INCONCLUSIVE"}
                         for gate in config["gates"]],
    }


def evaluate_patch_input(config_path, repository, supplied_patch, logs, *, apply_failed=False):
    config, selections = load_config(config_path)
    root = bundle_root()
    logs = report_path(logs, "")
    logs.mkdir(parents=True, exist_ok=True)
    report_path(logs, "evidence").mkdir(exist_ok=True)
    gate = {"status": "NOT_RUN", "passed": False, "checks": [], "error_category": "INFRASTRUCTURE_ERROR"}
    result = not_run(config, selections, "execution not started")
    observed = None
    report = None
    tests_started = False
    code = None
    phase = "infrastructure"
    try:
        repository = Path(repository)
        if repository.is_symlink() or not repository.is_dir():
            raise CandidatePatchError("invalid candidate root")
        repository = repository.resolve()
        test_patch, p2p_select = regular(asset(root, "test.patch")), regular(asset(root, "p2p_select.txt"))
        environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "CANDIDATE_ROOT": str(repository),
                       "HARDGATE_CONFIG": str(config_path), "HARDGATE_TEST_PATCH": str(test_patch),
                       "HARDGATE_P2P_SELECT": str(p2p_select), "HARDGATE_CANDIDATE_PATCH": str(supplied_patch)}
        with report_path(logs, "hardgate.stdout.log").open("w") as stdout, report_path(logs, "hardgate.stderr.log").open("w") as stderr:
            gate_code = run_process([sys.executable, str(regular(asset(root, "hardgate.py")))], repository, 30, stdout, stderr, environment)
        phase = "report"
        gate = read_json(report_path(logs, "hardgate.stdout.log"))
        if (type(gate.get("passed")) is not bool or gate.get("status") not in ("PASS", "FAIL")
                or gate["passed"] != (gate["status"] == "PASS") or gate_code != (0 if gate["passed"] else 1)
                or not isinstance(gate.get("checks"), list) or not gate["checks"]):
            raise ValueError("invalid Hard Gate execution report")
        gate["returncode"] = gate_code
        if not gate["passed"]:
            if gate.get("error_category") == "CANDIDATE_REJECTED":
                raise CandidatePatchError(gate.get("error", "candidate rejected"))
            raise ValueError(gate.get("error", "Hard Gate infrastructure error"))
        phase = "infrastructure"
        if apply_failed:
            raise CandidatePatchError("candidate apply rejected by caller")
        submitted = candidate_patch(supplied_patch)
        with tempfile.TemporaryDirectory(prefix="working-", dir=logs) as temporary:
            working = Path(temporary) / "repository"
            copy_candidate(repository, working, config["base_commit"])
            if submitted.stat().st_size:
                try:
                    subprocess.run(["git", "apply", "--check", "--binary", "--whitespace=nowarn", str(submitted)],
                                   cwd=working, capture_output=True, check=True)
                    subprocess.run(["git", "apply", "--binary", "--whitespace=nowarn", str(submitted)],
                                   cwd=working, capture_output=True, check=True)
                except subprocess.CalledProcessError as exc:
                    raise CandidatePatchError("candidate patch cannot be applied") from exc
            for name in (*config["test_paths"], *config.get("restoration_paths", ())):
                target = working / name
                for parent in target.parents:
                    if parent == working:
                        break
                    if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                        raise CandidatePatchError("unsafe evaluation ancestor: " + name)
                if target.exists() and not target.is_file() and not target.is_symlink():
                    raise CandidatePatchError("evaluation path conflicts with a directory: " + name)
            restore_evaluation_files(working, config["base_commit"], tuple(config["test_paths"]),
                                     restoration_paths=tuple(config.get("restoration_paths", ())))
            if test_patch.stat().st_size:
                subprocess.run(["git", "apply", "--binary", "--whitespace=nowarn", str(test_patch)],
                               cwd=working, capture_output=True, check=True)
            for name, expected in config.get("evaluation_files", {}).items():
                if digest(working / name) != expected:
                    raise ValueError("replayed evaluation file identity differs: " + name)
            frozen = {path.relative_to(working).as_posix(): (worktree_identity(path), path.lstat().st_mode)
                      for path in working.rglob("*") if (path.is_file() or path.is_symlink())
                      and ".git" not in path.relative_to(working).parts}
            report = Path(tempfile.mkdtemp(prefix="report-", dir=logs)) / "junit.xml"
            replacements = {"{report}": str(report), "{repository}": str(working), "{workspace}": str(working),
                            "{python}": sys.executable, "{config}": str(config_path), "{p2p_select}": str(p2p_select.resolve())}
            command = []
            for part in config["command"]:
                for placeholder, value in replacements.items():
                    part = part.replace(placeholder, value)
                command.append(part)
            with replay_environment(working, logs, report=report,
                    environment={"PYTHONPATH": str(working), "PYTHONDONTWRITEBYTECODE": "1"},
                    require_exec=config.get("require_exec", False)) as execution_env:
                with report_path(logs, "tests.stdout.log").open("w") as stdout, report_path(logs, "tests.stderr.log").open("w") as stderr:
                    tests_started = True
                    phase = "process"
                    if config.get("node_command"):
                        execution_env.update(VERIFIER_CONFIG=str(config_path), VERIFIER_P2P_SELECT=str(p2p_select.resolve()))
                        profile = config["execution_profile"]
                        code = run_node_commands(config["node_command"], selections, str(working), str(report),
                            config["node_timeout_seconds"], execution_env, profile["per_subject_timeout_seconds"], profile["shards"])
                    else:
                        code = run_process(command, working, config["timeout_seconds"], stdout, stderr, execution_env)
            phase = "report"
            observed = project(config, selections, report, code)
            for name, expected in frozen.items():
                path = working / name
                if (worktree_identity(path), path.lstat().st_mode) != expected:
                    raise ValueError("test command modified frozen worktree files")
            result = observed
            if config.get("node_command"):
                metadata = read_node_execution_evidence(report, expected_assertion_policy={"strict_assertions": True,
                    "junit_assertion_adapter": config.get("junit_assertion_adapter")}, expected_selectors=list(selections))
                if not metadata.get("terminal") and compare_node_evidence(result["tests"], metadata.get("partial_node_evidence"))["status"] != "PASS":
                    raise ValueError("node ledger conflicts with the real aggregate JUnit evidence")
                if result.get("status") in {"INFRA_ERROR", "TIMEOUT"} and (result.get("error") or result.get("terminal")):
                    metadata = {key: value for key, value in metadata.items() if key not in {"status", "error", "terminal"}}
                result.update(metadata)
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        if observed is None and tests_started and report is not None:
            observed = project(config, selections, report, code)
        result = dict(observed) if observed is not None else not_run(config, selections, str(exc))
        result["error"] = str(exc)
        if isinstance(exc, CandidatePatchError):
            result.update(status="INCONCLUSIVE", error_category="CANDIDATE_PATCH_INVALID", apply_failed=True)
            if gate["status"] == "NOT_RUN":
                gate.update(status="FAIL", error_category="CANDIDATE_REJECTED", error=str(exc))
        else:
            result.update(status="INFRA_ERROR", error_category="REPLAY_ENVIRONMENT_INVALID" if isinstance(exc, ReplayEnvironmentError) else "INFRASTRUCTURE_ERROR")
            terminal = {"typed_status": "INFRA_ERROR", "phase": phase,
                        "failure_class": "REPORT_ERROR" if phase == "report" else "INFRA_ERROR", "error": str(exc)}
            if isinstance(exc, subprocess.TimeoutExpired):
                terminal.update(phase="process", failure_class="TIMEOUT", timeout_seconds=exc.timeout)
                for node in result["tests"]:
                    if node["failure_class"] == "REPORT_ERROR":
                        node.update(phase="process", failure_class="TIMEOUT")
                        node["raw_evidence"]["process"] = {"failure_class": "TIMEOUT", "timeout_seconds": exc.timeout}
            result["terminal"] = (observed or {}).get("terminal") or terminal
    write_json(report_path(logs, "evidence/verifier.json"), result)
    write_json(report_path(logs, "hard-gate.json"), gate)
    ctrf, _ = runtime_report_payloads(result, gate, gate["passed"], result.get("apply_failed", False), 0.0, runtime_version=EXPECTED_RUNTIME_VERSION)
    write_json(report_path(logs, "ctrf.json"), ctrf)
    return result


def write_template_reports(result, logs, node_report, hard_gate_report, verifier_report):
    """Adapt replay evidence to the fixed grading entry point without rescoring it."""
    gate = read_json(report_path(logs, "hard-gate.json"))
    nodes = [{
        "name": node["selector"],
        "status": "passed" if node["typed_status"] == "PASS" else "failed",
        "typedStatus": node["typed_status"],
        "message": node["failure_class"],
        "extra": node,
    } for node in result["tests"]]
    write_json(node_report, {"tests": nodes})
    write_json(hard_gate_report, {
        **gate,
        "success": gate.get("passed") is True,
        "infrastructure_error": gate.get("error_category") == "INFRASTRUCTURE_ERROR",
    })
    write_json(verifier_report, {**result, "success": result["status"] == "PASS"})


def main():
    root = bundle_root()
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=os.environ.get("VERIFIER_CONFIG", str(root / "config.json")))
    parser.add_argument("--report", default=os.environ.get("VERIFIER_JUNIT_REPORT"))
    parser.add_argument("--returncode", type=int, default=os.environ.get("VERIFIER_TEST_RETURNCODE", "2"))
    parser.add_argument("--repo", default=os.environ.get("CANDIDATE_ROOT", "/workspace/repo"))
    parser.add_argument("--candidate-patch", default=os.environ.get("HARDGATE_CANDIDATE_PATCH", "/logs/artifacts/model.patch"))
    parser.add_argument("--logs", default=os.environ.get("GRADER_LOGS", "/logs/verifier"))
    parser.add_argument("--ctrf-output")
    parser.add_argument("--hard-gate-output")
    parser.add_argument("--node-report")
    parser.add_argument("--hard-gate-report")
    parser.add_argument("--verifier-report")
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args()
    try:
        config_path = regular(args.config).resolve()
        config, selections = load_config(config_path)
        if args.report:
            if args.ctrf_output or args.hard_gate_output:
                raise ValueError("projection and execution arguments are mutually exclusive")
            result = project(config, selections, args.report, args.returncode)
            emit(result)
            return 0 if result["status"] == "PASS" else 1
        if args.ctrf_output:
            output_path(args.ctrf_output, args.logs, "ctrf.json")
        if args.hard_gate_output:
            output_path(args.hard_gate_output, args.logs, "hard-gate.json")
        template_outputs = (args.node_report, args.hard_gate_report, args.verifier_report)
        if any(template_outputs):
            if not all(template_outputs) or args.report:
                raise ValueError("template execution requires all three report outputs")
            for supplied, name in zip(template_outputs, (
                    "reports/nodes.json", "hard-gate.json", "verifier-result.json")):
                output_path(supplied, args.logs, name)
        result = evaluate_patch_input(config_path, args.repo, args.candidate_patch, args.logs, apply_failed=bool(args.apply_failed))
        if all(template_outputs):
            write_template_reports(result, args.logs, *template_outputs)
        emit(result)
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        emit({"status": "INFRA_ERROR", "error": str(exc)})
        return 2


if __name__ == "__main__":
    sys.exit(main())
