#!/usr/bin/env python3
"""Deterministic JUnit projection and execution entry point."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote
from candidate_runtime import cleanup, prepare, protect, run_go


FIXED_GATES = (
    ("P2P-1", "test_p2p_1_public_api_and_in_place_mutation"),
    *tuple(
        (f"P2P-2-{index:02d}", f"test_p2p_2_{index:02d}_{name}")
        for index, name in (
            (1, "code_span_mapping"),
            (2, "tag_mapping"),
            (3, "inline_math_mapping"),
            (4, "emphasis_mapping"),
            (5, "strong_mapping"),
            (6, "strikethrough_mapping"),
            (7, "mark_mapping"),
            (8, "underline_mapping"),
            (9, "sub_mapping"),
            (10, "sup_mapping"),
            (11, "kbd_mapping"),
            (12, "link_mapping"),
            (13, "nested_hierarchy"),
            (14, "inline_attributes"),
            (15, "link_metadata"),
            (16, "textmark_sup"),
            (17, "textmark_sub"),
            (18, "textmark_emphasis"),
            (19, "textmark_strong"),
            (20, "textmark_mark"),
            (21, "textmark_strikethrough"),
            (22, "unsupported_textmark_noop"),
            (23, "flashcard_textmark_noop"),
            (24, "unclosed_boundary"),
        )
    ),
    *tuple(
        (f"P2P-3-{index:02d}", f"test_p2p_3_{index:02d}_{name}")
        for index, name in (
            (1, "table_math_normal"),
            (2, "table_math_export"),
            (3, "backslash_normal"),
            (4, "backslash_hybrid"),
            (5, "protyle_dom_protocol"),
            (6, "block_dom_round_trip"),
            (7, "vditor_dom_protocol"),
            (8, "vditor_round_trip"),
        )
    ),
    *tuple(
        (f"P2P-4-{index:02d}", f"test_p2p_4_{index:02d}_{name}")
        for index, name in (
            (1, "cross_tree_isolation"),
            (2, "parser_option_unchanged"),
            (3, "deterministic_result"),
        )
    ),
    *tuple(
        (f"P2P-5-{index:02d}", f"test_p2p_5_{index:02d}_{name}")
        for index, name in (
            (1, "protyle_export_md"),
            (2, "spin_block_dom"),
            (3, "md2_block_dom"),
            (4, "inline_md2_block_dom"),
            (5, "block_dom2_std_md"),
            (6, "md2_vditor_dom"),
            (7, "vditor_dom2_md"),
            (8, "inline_math"),
        )
    ),
    *tuple(
        (f"P2P-6-{index:02d}", f"test_p2p_6_{index:02d}_{name}")
        for index, name in (
            (1, "contain_text_mark_wrapper"),
            (2, "style_value_wrapper"),
            (3, "set_span_ial_wrapper"),
            (4, "set_text_mark_node_wrapper"),
        )
    ),
    ("P2P-8-001", "test_p2p_8_001_regular_flatten_semantics"),
    ("P2P-8-002", "test_p2p_8_002_hybrid_flatten_semantics"),
    ("P2P-8-003", "test_p2p_8_003_table_math_normal"),
    ("P2P-8-004", "test_p2p_8_004_table_math_export"),
    ("P2P-8-005", "test_p2p_8_005_normal_block_ref_fields"),
    ("F2P-006", "test_f2p_006_nil_regular_root"),
    ("F2P-007", "test_f2p_007_nil_hybrid_root"),
    ("P2P-8-008", "test_p2p_8_008_malformed_block_ref_id"),
    ("P2P-8-009", "test_p2p_8_009_malformed_block_ref"),
    ("P2P-8-010", "test_p2p_8_010_style_value_normalization"),
    ("F2P-011", "test_f2p_011_contain_text_mark"),
    ("F2P-012", "test_f2p_012_regular_transform_delegated"),
    ("F2P-013", "test_f2p_013_hybrid_transform_delegated"),
    ("F2P-014", "test_f2p_014_text_mark_transform_delegated"),
    ("F2P-015", "test_f2p_015_set_span_ial_delegated"),
    ("F2P-016", "test_f2p_016_contain_text_mark_delegated"),
    ("F2P-017", "test_f2p_017_set_text_mark_node_delegated"),
    ("F2P-018", "test_f2p_018_style_value_delegated"),
)
FIXED_GATES += (
    ("F2P-022", "test_f2p_022_nil_regular_tree_root"),
    ("F2P-023", "test_f2p_023_nil_hybrid_tree_root"),
    ("F2P-024", "test_f2p_024_regular_flatten_owned_by_editor"),
    ("F2P-025", "test_f2p_025_hybrid_flatten_owned_by_editor"),
    ("F2P-026", "test_f2p_026_no_parser_textmark_conversion"),
    ("F2P-027", "test_f2p_027_no_parser_style_conversion"),
    ("F2P-028", "test_f2p_028_inline_textmark_conversion_delegated"),
    ("F2P-029", "test_f2p_029_inline_image_conversion_delegated"),
)
FIXED_GATES += (
    ("P2P-9-01", "test_p2p_9_01_no_retained_invocation_state"),
    ("P2P-9-02", "test_p2p_9_02_concurrent_isolation"),
    ("P2P-9-03", "test_p2p_9_03_tag_attribute"),
    ("P2P-9-04", "test_p2p_9_04_attribute_name"),
    ("P2P-9-05", "test_p2p_9_05_attribute_value"),
    ("P2P-9-06", "test_p2p_9_06_text_mark_nil_options_plain_span"),
    ("P2P-9-07", "test_p2p_9_07_nil_options_option_free_textmark"),
)
FIXED_GATES += (
    ('F2P-030', 'test_f2p_030_stable_span_custom_attributes'),
    ('F2P-031', 'test_f2p_031_stable_paragraph_custom_attributes'),
    ('F2P-032', 'test_f2p_032_stable_heading_custom_attributes'),
    ('P2P-10-01', 'test_p2p_10_01_regular_link_reference_ast'),
    ('P2P-10-02', 'test_p2p_10_02_hybrid_link_reference_ast'),
)
P2P_SELECTION = Path(__file__).with_name("p2p_select.txt")
UNIT_NODE_PREFIX = "P2P-UNIT-"
REQUIREMENT_QUOTES = {
    "R1": "Move the coherent editor-specific transformation responsibility",
    "R2": "Existing AST mutations and serialized outputs MUST remain equivalent",
    "R3": "Nil, empty, malformed, and incomplete input MUST retain every existing safe",
    "R4": "Results MUST be deterministic and isolated to the target tree.",
    "R5": "Limit production changes to this responsibility migration",
    "R6": "Context needed by the editor layer",
    "R7": "The only required safety extensions are that regular and hybrid flattening",
}
GATE_REQUIREMENTS = {gate_id: ("R2",) for gate_id, _ in FIXED_GATES}
GATE_REQUIREMENTS.update(
    {
        "P2P-9-01": ("R6",),
        "P2P-9-02": ("R4",),
        "F2P-006": ("R7",),
        "F2P-007": ("R7",),
        "F2P-022": ("R7",),
        "F2P-023": ("R7",),
        "F2P-024": ("R1",),
        "F2P-025": ("R1",),
        "F2P-026": ("R1",),
        "F2P-027": ("R1",),
        "F2P-028": ("R1",),
        "F2P-029": ("R1",),
        "P2P-9-07": ("R3", "R6"),
        "F2P-011": ("R7",),
        "P2P-8-008": ("R3",),
        "P2P-8-009": ("R3",),
    }
)
for gate_id in (
    "P2P-6-01",
    "P2P-6-02",
    "P2P-6-03",
    "P2P-6-04",
    "F2P-012",
    "F2P-013",
    "F2P-014",
    "F2P-015",
    "F2P-016",
    "F2P-017",
    "F2P-018",
):
    GATE_REQUIREMENTS[gate_id] = ("R1", "R2")
GATE_REQUIREMENTS.update({'F2P-030': ('R4',),'F2P-031': ('R4',),'F2P-032': ('R4',)})
TEST_PATH = "tests/test_refactor.py"
TEST_PATCH = Path(__file__).with_name("test.patch")
TIMEOUT_SECONDS = 300


class ReportError(Exception):
    pass


def _install_tests(candidate_root: Path, test_patch: Path, output: Path) -> int:
    result: dict[str, object] = {
        "schema_version": "deepswe-test-install/v1",
        "installed": False,
    }
    try:
        if not test_patch.is_file() or test_patch.is_symlink():
            raise ReportError("test patch is missing or unsafe")
        completed = subprocess.run(
            [
                "git",
                "-C",
                str(candidate_root),
                "apply",
                "--binary",
                "--whitespace=nowarn",
                str(test_patch),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=120,
            check=False,
        )
        if completed.returncode != 0 or not (candidate_root / TEST_PATH).is_file():
            raise ReportError("failed to install verifier overlay: " + completed.stdout.strip())
        result["installed"] = True
    except (OSError, subprocess.TimeoutExpired, ReportError) as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
    _write_json(output, result)
    return 0 if result["installed"] is True else 1


def _selected_unit_tests() -> list[tuple[str, str, str]]:
    if not P2P_SELECTION.is_file():
        raise ReportError(f"P2P selection file is missing: {P2P_SELECTION}")
    selected: list[tuple[str, str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for raw in P2P_SELECTION.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split("::")
        if len(parts) not in {2, 3}:
            raise ReportError(f"invalid Go test selection: {raw!r}")
        package, encoded_name = parts[:2]
        test_name = unquote(encoded_name)
        tags = parts[2] if len(parts) == 3 else ""
        if not re.fullmatch(r"\./[A-Za-z0-9_./-]+", package):
            raise ReportError(f"invalid Go package in P2P selection: {raw!r}")
        if not re.fullmatch(r"Test[A-Za-z0-9_]+(?:/[^\r\n]+)?", test_name):
            raise ReportError(f"invalid Go test in P2P selection: {raw!r}")
        if tags and not re.fullmatch(r"[A-Za-z0-9_, -]+", tags):
            raise ReportError(f"invalid Go build tags in P2P selection: {raw!r}")
        item = (package, test_name, tags)
        if item in seen:
            raise ReportError(f"duplicate Go test in P2P selection: {raw!r}")
        seen.add(item)
        selected.append(item)
    if not selected:
        raise ReportError("P2P selection file is empty")
    return selected


def _all_gates() -> tuple[tuple[str, str], ...]:
    return FIXED_GATES + tuple(
        (f"{UNIT_NODE_PREFIX}{index:03d}", f"unit_{index:03d}")
        for index, _ in enumerate(_selected_unit_tests(), 1)
    )


GATES = _all_gates()


def _unit_statuses(candidate_root: Path, tmpdir: Path, log_path: Path | None = None) -> list[str]:
    selected = _selected_unit_tests()
    grouped: dict[tuple[str, str], list[tuple[int, str, str]]] = {}
    for index, (package, test_name, tags) in enumerate(selected, 1):
        grouped.setdefault((package, tags), []).append((index, test_name, tags))
    statuses = {index: "INFRA_ERROR" for index in range(1, len(selected) + 1)}
    cache = tmpdir / "go-build-cache"
    cache.mkdir(parents=True, exist_ok=True)
    overlay_dir = tmpdir / "unit-overlay"
    prepared = subprocess.run(
        ["go", "run", "./verifier_unit_adapter", str(candidate_root), str(overlay_dir)],
        cwd=candidate_root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, timeout=120, check=False,
    )
    if prepared.returncode != 0:
        raise ReportError("cannot expand trusted unit test cases: " + prepared.stdout)
    protect(overlay_dir)

    def run_group(item: tuple[tuple[str, str], list[tuple[int, str, str]]]) -> tuple[dict[int, str], str]:
        (package, tags), tests = item
        names = [name for _, name, _ in tests]
        parents = sorted({name.split("/", 1)[0] for name in names})
        expression = "^(?:" + "|".join(re.escape(name) for name in parents) + ")$"
        env = os.environ.copy()
        env["GOCACHE"] = str(cache)
        command = ["go", "test", "-json", "-vet=off", "-overlay", str(overlay_dir / "overlay.json")]
        if tags:
            command.extend(["-tags", tags])
        command.extend([package, "-run", expression, "-count=1"])
        try:
            completed = run_go(
                command,
                cwd=candidate_root,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=240,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            return ({index: "INFRA_ERROR" for index, _, _ in tests}, str(exc))
        by_name: dict[str, str] = {}
        failed_parents: set[str] = set()
        started_tests: set[str] = set()
        panic_tests: set[str] = set()
        package_failed = False
        for line in completed.stdout.splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(event, dict):
                continue
            name = event.get("Test")
            action = event.get("Action")
            if action == "run" and isinstance(name, str):
                started_tests.add(name)
            if (action == "output" and name in started_tests
                    and isinstance(event.get("Output"), str)
                    and event["Output"].startswith("panic:")):
                panic_tests.add(name)
            if action == "fail" and not name:
                package_failed = True
            if isinstance(name, str) and action == "fail":
                failed_parents.add(name)
            if name in names and action in {"pass", "fail", "skip"}:
                by_name[name] = {
                    "pass": "PASS",
                    "fail": "FAIL",
                    "skip": "INCONCLUSIVE",
                }[action]
        # A panic can abort a table-test parent before its remaining subtests
        # emit results. Attribute those interrupted cases to that failed parent,
        # not to unavailable infrastructure. Keep completed case outcomes and
        # retry other parents separately; never rerun the same crashing parent
        # indefinitely merely because its later subtests remain unreported.
        interrupted = set()
        if completed.returncode != 0 and package_failed:
            for parent in parents:
                if parent not in failed_parents or not any(
                    name == parent or name.startswith(parent + "/")
                    for name in panic_tests
                ):
                    continue
                for name in names:
                    if (name == parent or name.startswith(parent + "/")) and name not in by_name:
                        by_name[name] = "FAIL"
                        interrupted.add(name)
        result = {
            index: by_name.get(name, "INFRA_ERROR")
            for index, name, _ in tests
        }
        # A parent can fail outside any table case; preserve that failure.
        for parent in failed_parents:
            descendants = [(index, name) for index, name, _ in tests
                           if name.startswith(parent + "/")]
            if descendants and not any(by_name.get(name) == "FAIL" for _, name in descendants):
                for index, _ in descendants:
                    result[index] = "FAIL"
        if completed.returncode != 0 and all(value == "PASS" for value in result.values()):
            result = {index: "FAIL" for index, _, _ in tests}
        if completed.returncode != 0 and not by_name:
            result = {index: "INFRA_ERROR" for index, _, _ in tests}
        output = completed.stdout
        if interrupted:
            output += "\n[candidate panic interrupted cases; attributed FAIL, not individually completed: " + json.dumps(sorted(interrupted)) + "]\n"
        # A Go panic terminates the package process before later tests run.
        # Retry only the unreported cases; absent results without an observed
        # test failure remain infrastructure errors.
        remaining = [test for test in tests if test[1] not in by_name]
        if (remaining and len(remaining) < len(tests)
                and completed.returncode != 0 and "FAIL" in by_name.values()):
            retried, retry_output = run_group(((package, tags), remaining))
            result.update(retried)
            output += "\n[retrying unreported Go unit tests]\n" + retry_output
        return result, output

    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=min(2, len(grouped))) as executor:
        for result, output in executor.map(run_group, grouped.items()):
            statuses.update(result)
            if log_path is not None:
                with log_path.open("a", encoding="utf-8") as log:
                    log.write("\n[original Go unit tests]\n" + output)
    return [statuses[index] for index in range(1, len(selected) + 1)]


def _append_unit_cases(report: Path, statuses: list[str]) -> None:
    tree = ET.parse(report)
    root = tree.getroot()
    suite = root if root.tag == "testsuite" else root.find("testsuite")
    if suite is None:
        raise ReportError("JUnit report has no testsuite")
    for index, status in enumerate(statuses, 1):
        testcase = ET.SubElement(
            suite,
            "testcase",
            {"classname": "lute.original_unit_tests", "name": f"unit_{index:03d}"},
        )
        if status == "FAIL":
            ET.SubElement(testcase, "failure").text = "original Go unit test failed"
        elif status == "INCONCLUSIVE":
            ET.SubElement(testcase, "skipped")
        elif status == "INFRA_ERROR":
            ET.SubElement(testcase, "error").text = "original Go unit test could not be collected"
    tree.write(report, encoding="utf-8", xml_declaration=True)


def _integer_returncode(value: object) -> int:
    if isinstance(value, bool):
        raise ReportError("test return code must be an integer")
    try:
        return int(str(value))
    except (TypeError, ValueError) as exc:
        raise ReportError("test return code must be an integer") from exc


def project_report(report: Path, returncode: object) -> dict[str, object]:
    rc = _integer_returncode(returncode)
    if not report.is_file() or report.is_symlink() or report.stat().st_size == 0:
        raise ReportError("JUnit report is missing, symlinked, or empty")
    try:
        root = ET.parse(report).getroot()
    except (ET.ParseError, OSError) as exc:
        raise ReportError("JUnit report cannot be parsed") from exc
    if root.tag not in {"testsuite", "testsuites"}:
        raise ReportError("unexpected JUnit root element")

    rows: dict[str, list[str]] = {}
    for testcase in root.iter("testcase"):
        classname = testcase.get("classname")
        name = testcase.get("name")
        if not classname or not name:
            raise ReportError("JUnit testcase lacks classname or name")
        node = name
        if testcase.find("error") is not None:
            status = "INFRA_ERROR"
        elif testcase.find("skipped") is not None:
            status = "INCONCLUSIVE"
        elif testcase.find("failure") is not None:
            status = "FAIL"
        else:
            status = "PASS"
        rows.setdefault(node, []).append(status)

    expected_nodes = {node for _, node in GATES}
    unexpected_membership = bool(set(rows) - expected_nodes)

    observations: list[dict[str, str]] = []
    for gate_id, node in GATES:
        statuses = rows.get(node, [])
        if len(statuses) != 1:
            typed = "INFRA_ERROR"
        else:
            typed = statuses[0]
        observations.append({"id": gate_id, "typed_status": typed})

    if unexpected_membership:
        observations = [
            {"id": gate_id, "typed_status": "INFRA_ERROR"}
            for gate_id, _ in GATES
        ]

    # A non-test process error (or a nonzero exit without a failed test)
    # invalidates the execution even when a partial/stale report looks green.
    if rc not in {0, 1} or (rc == 1 and all(item["typed_status"] == "PASS" for item in observations)):
        return _infra_result()
    typed_statuses = [item["typed_status"] for item in observations]
    if "INFRA_ERROR" in typed_statuses or rc not in {0, 1}:
        overall = "INFRA_ERROR"
    elif "INCONCLUSIVE" in typed_statuses:
        overall = "INCONCLUSIVE"
    elif "FAIL" in typed_statuses:
        overall = "FAIL"
    elif rc != 0:
        overall = "INFRA_ERROR"
    else:
        overall = "PASS"
    return {"status": overall, "observations": observations}


def _emit(result: dict[str, object]) -> int:
    sys.stdout.write(json.dumps(result, separators=(",", ":"), sort_keys=False) + "\n")
    return 0


def _infra_result() -> dict[str, object]:
    return {
        "status": "INFRA_ERROR",
        "observations": [
            {"id": gate_id, "typed_status": "INFRA_ERROR"}
            for gate_id, _ in GATES
        ],
    }


def _blocked_result() -> dict[str, object]:
    return {
        "status": "FAIL",
        "observations": [
            {"id": gate_id, "typed_status": "FAIL"}
            for gate_id, _ in GATES
        ],
    }


def _run_tests(candidate_root: Path, tmpdir: Path) -> dict[str, object]:
    report_name: str | None = None
    log_path = Path(os.environ.get("VERIFIER_TEST_LOG", "/logs/verifier/test-stdout.txt"))
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        tmpdir.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            prefix="verifier-", suffix=".xml", dir=tmpdir, delete=False
        ) as handle:
            report_name = handle.name
        report = Path(report_name)
        command = [
            sys.executable,
            "-m",
            "pytest",
            "-p",
            "no:rerunfailures",
            "--rootdir=.",
            "-q",
            TEST_PATH,
            f"--junitxml={report}",
        ]
        with log_path.open("w", encoding="utf-8") as log:
            log.write("$ " + " ".join(command) + "\n")
            log.flush()
            completed = subprocess.run(
                command,
                cwd=candidate_root,
                stdout=log,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=TIMEOUT_SECONDS,
                check=False,
            )
            log.write(f"\n[pytest return code: {completed.returncode}]\n")
        _append_unit_cases(report, _unit_statuses(candidate_root, tmpdir, log_path))
        return project_report(report, completed.returncode)
    except subprocess.TimeoutExpired as exc:
        with log_path.open("a", encoding="utf-8") as log:
            log.write(f"\n[pytest timed out after {TIMEOUT_SECONDS}s: {exc}]\n")
        return _infra_result()
    except (OSError, ReportError, ET.ParseError) as exc:
        with log_path.open("a", encoding="utf-8") as log:
            log.write(f"\n[verifier error: {type(exc).__name__}: {exc}]\n")
        return _infra_result()
    finally:
        if report_name:
            try:
                Path(report_name).unlink()
            except OSError:
                pass


def _test_tmpdir() -> Path:
    value = os.environ.get("TMPDIR")
    return Path(value) if value else Path(tempfile.gettempdir())


def _write_json(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )


def _ctrf_result(result: dict[str, object]) -> dict[str, object]:
    status_map = {
        "PASS": "passed",
        "FAIL": "failed",
        "INCONCLUSIVE": "skipped",
        "INFRA_ERROR": "other",
    }
    tests = []
    for observation in result["observations"]:
        gate_id = str(observation["id"])
        typed_status = str(observation["typed_status"])
        tests.append(
            {
                "testId": gate_id,
                "name": gate_id,
                "status": status_map[typed_status],
                "extra": {"deepswe": {"group": "p2p" if gate_id.startswith("P2P-") else "f2p"}},
            }
        )
    return {
        "results": {
            "tests": tests,
            "summary": {
                "tests": len(tests),
                "passed": sum(test["status"] == "passed" for test in tests),
                "failed": sum(test["status"] == "failed" for test in tests),
                "skipped": sum(test["status"] == "skipped" for test in tests),
                "pending": sum(test["status"] == "pending" for test in tests),
                "other": sum(test["status"] == "other" for test in tests),
            },
        }
    }


def _projection_mode() -> int:
    supplied_report = os.environ.get("VERIFIER_JUNIT_REPORT")
    if not supplied_report:
        return -1
    try:
        result = project_report(
            Path(supplied_report), os.environ.get("VERIFIER_TEST_RETURNCODE")
        )
    except ReportError:
        result = _infra_result()
    return _emit(result)


def _run_hard_gate(args: argparse.Namespace, candidate_root: Path) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(Path(__file__).with_name("hardgate.py")),
            "--config",
            str(args.config),
            "--repo",
            str(candidate_root),
            "--output",
            str(args.hard_gate_output),
            "--apply-failed",
            str(args.apply_failed),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=TIMEOUT_SECONDS,
        check=False,
    )
    if completed.returncode != 0 or not args.hard_gate_output.is_file():
        raise ReportError("hard gate did not produce a report")


def _cli_mode(args: argparse.Namespace) -> int:
    try:
        candidate_root = args.repo.resolve(strict=True)
        tmpdir = _test_tmpdir().resolve(strict=False)
        if not candidate_root.is_dir():
            raise OSError("candidate repository is unavailable")
        if args.blocked_by_hard_gate:
            _write_json(args.ctrf_output, _ctrf_result(_blocked_result()))
            return 0
        if not args.skip_hard_gate:
            _run_hard_gate(args, candidate_root)
        result = _run_tests(candidate_root, tmpdir)
        _write_json(args.ctrf_output, _ctrf_result(result))
        return 0
    except (OSError, ReportError, TypeError, ValueError, subprocess.TimeoutExpired):
        result = _infra_result()
        try:
            _write_json(args.ctrf_output, _ctrf_result(result))
        except OSError:
            return 1
        return 0


def _unified_mode(args: argparse.Namespace) -> int:
    config = json.loads(args.config.read_text())
    hard = {"success": False, "infrastructure_error": True, "tests": []}
    result = _infra_result()
    try:
        repo = args.repo.resolve(strict=True)
        tmpdir = Path(tempfile.mkdtemp(prefix='lute-trusted-verifier-'))
        tmpdir.chmod(0o755)
        prepare(repo)
        args.hard_gate_output = args.hard_gate_report
        _run_hard_gate(args, repo)
        hard = json.loads(args.hard_gate_report.read_text())
        hard.update(
            success=hard.get("passed") is True,
            cheating_detected=hard.get("cheat_detected") is True,
            compile_passed=any(t["testId"] == "target_modules_compile" and t["status"] == "passed"
                               for t in hard.get("tests", [])),
            infrastructure_error=hard.get("status") == "INFRA_ERROR",
            scope_violation=any(t["testId"] == "candidate_scope_valid"
                                and t["status"] != "passed" for t in hard.get("tests", [])),
        )
        cleanup()
        if hard["success"]:
            if _install_tests(repo, TEST_PATCH, args.node_report.parent / "test-install.json"):
                raise ReportError("cannot install trusted tests")
            protect(repo)
            result = _run_tests(repo, tmpdir)
        else:
            result = _blocked_result() if not hard["infrastructure_error"] else _infra_result()
    except (OSError, ReportError, TypeError, ValueError, subprocess.TimeoutExpired) as exc:
        hard["success"] = False
        hard["infrastructure_error"] = True
        hard["error"] = str(exc)
        result = _infra_result()
    finally:
        cleanup()
    statuses = {o['id']: o['typed_status'] for o in result['observations']}
    typed = {'passed': 'PASS', 'failed': 'FAIL', 'skipped': 'INCONCLUSIVE', 'other': 'INFRA_ERROR'}
    statuses.update({t['testId']: typed.get(t['status'], 'INFRA_ERROR') for t in hard.get('tests', [])})
    plain = {v: k for k, v in typed.items()}
    nodes = [{'name': node, 'status': plain[statuses.get(node, 'INFRA_ERROR')],
              'typedStatus': statuses.get(node, 'INFRA_ERROR')}
             for node in config['f2p'] + config['p2p']]
    _write_json(args.node_report, {'tests': nodes})
    _write_json(args.hard_gate_report, hard)
    _write_json(args.verifier_report, {'success': result['status'] == 'PASS' and hard['success'],
                                     'status': result['status']})
    return _emit(result)


def _standalone_mode() -> int:
    candidate = os.environ.get("CANDIDATE_ROOT")
    if not candidate:
        return _emit(_infra_result())
    try:
        candidate_root = Path(candidate).resolve(strict=True)
        tmpdir = _test_tmpdir().resolve(strict=False)
        if not candidate_root.is_dir() or not (candidate_root / TEST_PATH).is_file():
            return _emit(_infra_result())
        return _emit(_run_tests(candidate_root, tmpdir))
    except OSError:
        return _emit(_infra_result())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path)
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--ctrf-output", type=Path)
    parser.add_argument("--hard-gate-output", type=Path)
    parser.add_argument("--node-report", type=Path)
    parser.add_argument("--hard-gate-report", type=Path)
    parser.add_argument("--verifier-report", type=Path)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    parser.add_argument("--skip-hard-gate", action="store_true")
    parser.add_argument("--blocked-by-hard-gate", action="store_true")
    parser.add_argument("--install-tests", action="store_true")
    parser.add_argument("--test-patch", type=Path)
    parser.add_argument("--install-output", type=Path)
    if len(sys.argv) == 1:
        return _projection_mode() if os.environ.get("VERIFIER_JUNIT_REPORT") else _standalone_mode()
    args = parser.parse_args()
    if args.node_report is not None:
        if not all((args.config, args.repo, args.hard_gate_report, args.verifier_report)):
            parser.error("unified mode requires config, repo and both reports")
        return _unified_mode(args)
    if args.install_tests:
        if args.repo is None or args.test_patch is None or args.install_output is None:
            parser.error("--install-tests requires --repo, --test-patch, and --install-output")
        try:
            candidate_root = args.repo.resolve(strict=True)
        except OSError:
            return 1
        return _install_tests(candidate_root, args.test_patch, args.install_output)
    if not all(
        value is not None
        for value in (args.config, args.repo, args.ctrf_output, args.hard_gate_output)
    ):
        parser.error("--config, --repo, --ctrf-output, and --hard-gate-output are required")
    return _cli_mode(args)


if __name__ == "__main__":
    raise SystemExit(main())
