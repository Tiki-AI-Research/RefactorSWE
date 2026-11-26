"""Regression checks for the task's P2P inventory and literal pytest IDs.

Run with ``python -m pytest tests/verifier/test_p2p_inventory.py`` using an
interpreter with pytest installed. These test the verifier, not the candidate.
"""

import importlib.util
from pathlib import Path
import tomllib
import xml.etree.ElementTree as ET

import pytest


PACKAGE = Path(__file__).resolve().parent.parent


@pytest.fixture(params=("hardgate", "verifier"))
def runtime(request):
    spec = importlib.util.spec_from_file_location(
        request.param, PACKAGE / "verifier" / f"{request.param}.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_authenticated_inventory_is_synchronized(runtime):
    config, selections = runtime.load_config(PACKAGE / "config.json")
    manifest = runtime.load_release_manifest()
    task = tomllib.loads((PACKAGE.parent / "task.toml").read_text())
    assert len(config["p2p"]) == manifest["p2p_count"] == task["tests"]["pass_to_pass_count"]
    assert len(config["f2p"]) == manifest["f2p_count"] == task["tests"]["fail_to_pass_count"]
    assert (PACKAGE / "verifier" / "p2p_select.txt").read_text().splitlines() == config["p2p"]
    assert config["command"][config["command"].index("{report}") + 1:] == list(selections)

    original = manifest["original_unit_suite"]
    unit_nodes = [node for node in config["p2p"] if node.startswith("tests/unit/")]
    assert original["base_commit"] == config["base_commit"]
    assert len(unit_nodes) == original["count"] == 453
    assert {node.split("::", 1)[0] for node in unit_nodes} == set(original["files"])
    assert set(original["files"]) <= set(config["restoration_paths"])
    assert {"tests/helpers/contracts.py", "tests/adapters/building.py"} <= set(
        config["restoration_paths"]
    )
    assert not set(config["p2p"]) & set(config["f2p"])


@pytest.mark.parametrize("payload", (r"\n [importlinter] foo=True", "mypackage.*", "a?b"))
def test_parameter_payloads_are_literal(runtime, payload):
    selector = f"tests/unit/example.py::TestExample::test_value[{payload}]"
    assert runtime.selector_parts(selector, {"tests/unit/example.py"}) == (
        "tests/unit/example.py", f"test_value[{payload}]"
    )


@pytest.mark.parametrize("selector", (
    "tests/unit/example.py::test_*",
    "tests/unit/*.py::test_value[ok]",
    r"tests/unit/example.py::test_\value[ok]",
    "tests/unit/example.py::test_value[unclosed*",
    "tests/unit/example.py::test_value[actual\nnewline]",
    "tests/unit/example.py::test_value[actual\ttab]",
    "tests/unit/example.py::Test[parameter]::test_value",
    "tests/outside.py::test_value[ok]",
))
def test_nonexact_or_undeclared_selectors_are_rejected(runtime, selector):
    with pytest.raises(ValueError):
        runtime.selector_parts(selector, {"tests/unit/example.py"})


def test_all_original_parameter_ids_bind_to_junit(runtime):
    config, selections = runtime.load_config(PACKAGE / "config.json")
    suite = ET.Element("testsuite", tests=str(len(selections)))
    for selector in selections:
        path, qualified = selector.split("::", 1)
        scope, _, name = qualified.rpartition("::")
        classname = path.removesuffix(".py").replace("/", ".")
        if scope:
            classname += "." + scope.replace("::", ".")
        ET.SubElement(suite, "testcase", classname=classname, name=name)
    rows = runtime.resolve_junit_evidence(
        suite, selections, strict_assertions=True, junit_assertion_adapter="pytest"
    )
    assert len(rows) == len(selections)
    assert all(row["typed_status"] == "PASS" for row in rows)

    # An original unit regression must reach the all-P2P-pass gate as a failure.
    victim = next(node for node in suite if node.get("classname", "").startswith("tests.unit."))
    ET.SubElement(victim, "failure", message="assert actual == expected")
    rows = runtime.resolve_junit_evidence(
        suite, selections, strict_assertions=True, junit_assertion_adapter="pytest"
    )
    failures = [row for row in rows if row["typed_status"] != "PASS"]
    assert len(failures) == 1
    assert failures[0]["role"] == "P2P"
    assert failures[0]["typed_status"] == "FAIL"
    assert failures[0]["selector"].startswith("tests/unit/")

    spec = importlib.util.spec_from_file_location("grader", PACKAGE / "grader.py")
    grader = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(grader)
    outcome = grader.evaluate_gate(
        hard_gate={"success": True},
        verifier_result={"success": True, "status": "FAIL"},
        f2p_pass_ratio=1.0,
        p2p_pass_ratio=(len(config["p2p"]) - 1) / len(config["p2p"]),
        apply_failed=False,
    )
    assert outcome["reward"] == 0.0
    assert outcome["termination_reason"] == "p2p_failed"
