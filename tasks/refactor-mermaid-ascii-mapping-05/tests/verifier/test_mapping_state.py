from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


VERIFIER_ROOT = Path(__file__).resolve().parent
TESTS_ROOT = VERIFIER_ROOT.parent
STRUCTURE_PATH = "pkg/graph/f2p_mapping_structure_test.go"
SHARED_STATE = "TestF2PMappingEntryPointSharesDedicatedMappingState"
LEVEL_STATE = "TestF2PLevelReservationStateOwnedByDedicatedType"
LOCAL_STATE = "TestF2PMappingEntryPointOwnsNoCollectionState"
ORCHESTRATION = "TestF2PMappingEntryPointIsShortOrchestration"
DELEGATION = "TestF2PMappingEntryPointDelegatesLowLevelPrimitives"
LAYOUT_LOOPS = "TestF2PMappingEntryPointHasNoLayoutLoops"
SELECTED_TESTS = (SHARED_STATE, LEVEL_STATE, LOCAL_STATE, ORCHESTRATION, DELEGATION, LAYOUT_LOOPS)


def overlay_files():
    files = {}
    path = None
    old_remaining = new_remaining = 0
    for line in (VERIFIER_ROOT / "test.patch").read_text().splitlines(keepends=True):
        if line.startswith("diff --git "):
            if old_remaining or new_remaining:
                raise AssertionError("incomplete patch hunk")
            path = line.rstrip().split(" b/", 1)[1]
            files[path] = []
        elif line.startswith("@@ "):
            if old_remaining or new_remaining:
                raise AssertionError("incomplete patch hunk")
            match = re.fullmatch(r"@@ -\d+(?:,(\d+))? \+\d+(?:,(\d+))? @@.*\n?", line)
            if match is None:
                raise AssertionError("invalid patch hunk")
            old_remaining = int(match.group(1) or 1)
            new_remaining = int(match.group(2) or 1)
        elif line.startswith(("+++ ", "--- ", "index ", "new file mode ")):
            continue
        elif line.startswith(("+", "-", " ")):
            if not old_remaining and not new_remaining:
                raise AssertionError("patch content exceeds declared hunk counts")
            if line[0] in "- ":
                old_remaining -= 1
            if line[0] in "+ ":
                new_remaining -= 1
                files[path].append(line[1:])
            if old_remaining < 0 or new_remaining < 0:
                raise AssertionError("patch content exceeds declared hunk counts")
        elif line.strip() and not line.startswith("\\ No newline"):
            raise AssertionError("unexpected patch content")
    if old_remaining or new_remaining:
        raise AssertionError("incomplete patch hunk")
    return {name: "".join(lines) for name, lines in files.items()}


class MappingStateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.go = shutil.which("go")
        if cls.go is None:
            raise RuntimeError("Go is required for mapping-state regression tests")
        cls.overlay = overlay_files()
        cls.temporary = tempfile.TemporaryDirectory(prefix=".mapping-state-", dir=VERIFIER_ROOT)
        cls.addClassCleanup(cls.temporary.cleanup)
        cls.root = Path(cls.temporary.name)
        cls.environment = {
            "PATH": str(Path(cls.go).parent) + ":/usr/bin:/bin",
            "HOME": str(cls.root),
            "TMPDIR": str(cls.root),
            "GOCACHE": str(cls.root / "cache"),
            "GOPATH": str(cls.root / "gopath"),
            "GO111MODULE": "off",
            "GOWORK": "off",
            "GOPROXY": "off",
            "GOTOOLCHAIN": "local",
            "CGO_ENABLED": "0",
        }

    def check_fixture(self, source, failures=()):
        with tempfile.TemporaryDirectory(prefix="fixture-", dir=self.root) as directory:
            fixture = Path(directory)
            (fixture / "mapping_structure_test.go").write_text(self.overlay[STRUCTURE_PATH])
            (fixture / "mapping.go").write_text("package graph\n" + source)
            command = [
                self.go, "test", "-json", "-vet=off", "-count=1", "-run",
                "^(" + "|".join(SELECTED_TESTS) + ")$", ".",
            ]
            process = subprocess.run(
                command, cwd=fixture, env=self.environment,
                capture_output=True, text=True, timeout=180,
            )
            observations = {}
            output = []
            for line in process.stdout.splitlines():
                event = json.loads(line)
                if "Output" in event:
                    output.append(event["Output"])
                if event.get("Test") in SELECTED_TESTS and event["Action"] in {"pass", "fail"}:
                    observations[event["Test"]] = event["Action"]
            expected = {name: "fail" if name in failures else "pass" for name in SELECTED_TESTS}
            diagnostics = "".join(output) + process.stderr
            self.assertEqual(observations, expected, diagnostics)
            self.assertEqual(process.returncode, int(bool(failures)), diagnostics)

    @staticmethod
    def named_map_fixture(initializer="state := newState()", reserve="state[0]++", extra="", body=None):
        if body is None:
            body = initializer + "\nstate.reserve()\nstate.size()"
        return "\n".join([
            "type graph struct{}",
            "type reservationState map[int]int",
            "func newState() reservationState { return make(reservationState) }",
            "func (state reservationState) reserve() { " + reserve + " }",
            "func (state reservationState) size() { _ = state[0] }",
            extra,
            "func (owner *graph) createMapping() {\n" + body + "\n}",
        ])

    def test_named_map_initializers(self):
        for initializer in (
            "state := newState()",
            "state := make(reservationState)",
            "state := reservationState{}",
            "var state reservationState = newState()",
            "var state = newState()",
        ):
            with self.subTest(initializer=initializer):
                self.check_fixture(self.named_map_fixture(initializer=initializer))

    def test_named_map_alias(self):
        source = self.named_map_fixture().replace(
            "type reservationState map[int]int",
            "type reservationState map[int]int\ntype reservationAlias = reservationState",
        ).replace("func newState() reservationState", "func newState() reservationAlias")
        self.check_fixture(source)

    def test_named_map_parameter(self):
        source = self.named_map_fixture(body="state := newState()\nreserve(state)\nsize(state)")
        source = source.replace("func (state reservationState) reserve()", "func reserve(state reservationState)")
        source = source.replace("func (state reservationState) size()", "func size(state reservationState)")
        self.check_fixture(source)

    def test_pointer_to_named_map(self):
        source = self.named_map_fixture(initializer="state := &reservationState{}")
        source = source.replace("(state reservationState)", "(state *reservationState)")
        source = source.replace("state[0]", "(*state)[0]")
        self.check_fixture(source)

    def test_named_map_local_alias_writes(self):
        for reserve in (
            "levels := state; levels[0]++",
            "var levels = state; levels[0]++",
            "levels := state; next := levels; next[0]++",
            "var levels reservationState; levels = state; levels[0]++",
            "levels := (state); (levels[0]) = levels[0] + 1",
            "levels := state; levels, state = make(reservationState), levels; state[0]++",
            "levels := state; { levels := make(reservationState); _ = levels }; levels[0]++",
        ):
            with self.subTest(reserve=reserve):
                self.check_fixture(self.named_map_fixture(reserve=reserve))

    def test_parenthesized_named_map_writes(self):
        for reserve in ("(state[0])++", "(state)[0] = 1", "((state[0])) += 1"):
            with self.subTest(reserve=reserve):
                self.check_fixture(self.named_map_fixture(reserve=reserve))

    def test_rebound_or_shadowed_alias_does_not_own_shared_map(self):
        for reserve in (
            "levels := state; levels = make(reservationState); levels[0]++",
            "levels := state; { levels := make(reservationState); levels[0]++ }; _ = levels",
            "state = make(reservationState); state[0]++",
            "levels := state; levels, state = make(reservationState), levels; levels[0]++",
        ):
            with self.subTest(reserve=reserve):
                self.check_fixture(self.named_map_fixture(reserve=reserve), failures=(LEVEL_STATE,))

    def test_struct_owner_remains_accepted(self):
        for field_type in ("map[int]int", "reservationState"):
            with self.subTest(field_type=field_type):
                source = self.named_map_fixture().replace(
                    "func newState() reservationState { return make(reservationState) }",
                    "type mappingState struct { levels " + field_type + " }\n"
                    "func newState() *mappingState { return &mappingState{levels: make(" + field_type + ")} }",
                ).replace("(state reservationState)", "(state *mappingState)")
                source = source.replace("state[0]++", "state.levels[0] = state.levels[0] + 1")
                self.check_fixture(source.replace("_ = state[0]", "_ = state.levels[0]"))

    def test_unshared_state_is_rejected(self):
        self.check_fixture(
            self.named_map_fixture(body="state := newState()\nstate.reserve()"),
            failures=(SHARED_STATE,),
        )

    def test_unowned_collection_is_rejected(self):
        source = self.named_map_fixture(body="state := make(map[int]int)\nreserve(state)\nsize(state)")
        source = source.replace("func (state reservationState) reserve()", "func reserve(state map[int]int)")
        source = source.replace("func (state reservationState) size()", "func size(state map[int]int)")
        self.check_fixture(source, failures=(SHARED_STATE, LEVEL_STATE, LOCAL_STATE))

    def test_unused_or_unreachable_owner_is_rejected(self):
        for reserve, extra in (
            ("_ = state[0]", ""),
            ("other := make(map[int]int); other[0] = 1; _ = state[0]", ""),
            ("{ state := make(map[int]int); state[0] = 1 }; _ = state[0]", ""),
            ("_ = state[0]", "func (state reservationState) unused() { state[0]++ }"),
        ):
            with self.subTest(reserve=reserve, extra=extra):
                self.check_fixture(self.named_map_fixture(reserve=reserve, extra=extra), failures=(LEVEL_STATE,))

    def test_local_reservation_does_not_satisfy_struct_owner(self):
        source = self.named_map_fixture().replace(
            "func newState() reservationState { return make(reservationState) }",
            "type mappingState struct { levels map[int]int }\n"
            "func newState() *mappingState { return &mappingState{levels: make(map[int]int)} }",
        ).replace("(state reservationState)", "(state *mappingState)")
        source = source.replace("state[0]++", "levels := make(map[int]int); levels[0]++")
        source = source.replace("_ = state[0]", "_ = state.levels[0]")
        self.check_fixture(source, failures=(LEVEL_STATE,))

    def test_inline_layout_is_still_rejected(self):
        source = self.named_map_fixture(
            body="state := newState()\nstate.reserve()\nstate.size()\nreserveSpotInGrid()",
            extra="func reserveSpotInGrid() {}",
        )
        self.check_fixture(source, failures=(DELEGATION,))

    def test_long_orchestration_is_still_rejected(self):
        body = "state := newState()\nstate.reserve()\n" + "state.size()\n" * 41
        self.check_fixture(self.named_map_fixture(body=body), failures=(ORCHESTRATION,))

    def test_layout_loop_is_still_rejected(self):
        body = "state := newState()\nfor level := 0; level < 2; level++ { state.reserve() }\nstate.size()"
        self.check_fixture(self.named_map_fixture(body=body), failures=(LAYOUT_LOOPS,))

    def test_graph_alias_is_not_a_dedicated_owner(self):
        source = "\n".join([
            "type graph struct { levels map[int]int }",
            "type graphAlias = graph",
            "func newState() *graphAlias { return &graphAlias{levels: make(map[int]int)} }",
            "func (owner *graph) reserve() { owner.levels[0] = 1 }",
            "func (owner *graph) size() { _ = owner.levels[0] }",
            "func (owner *graph) createMapping() { state := newState(); state.reserve(); state.size() }",
        ])
        self.check_fixture(source, failures=(SHARED_STATE, LEVEL_STATE))

    def test_package_integrity_and_selector_membership(self):
        config_path = TESTS_ROOT / "config.json"
        config = json.loads(config_path.read_text())
        for name, path in (
            ("test_patch_sha256", VERIFIER_ROOT / "test.patch"),
            ("p2p_select_sha256", VERIFIER_ROOT / "p2p_select.txt"),
        ):
            self.assertEqual(config["integrity"][name], hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertEqual((VERIFIER_ROOT / "p2p_select.txt").read_text(), "\n".join(config["p2p"]) + "\n")
        config_hash = hashlib.sha256(config_path.read_bytes()).hexdigest()
        for name in ("verifier.py", "hardgate.py"):
            contents = (VERIFIER_ROOT / name).read_text()
            self.assertRegex(contents, r"EXPECTED_CONFIG_SHA256 = ['\"]" + config_hash + r"['\"]")
        for selector in config["f2p"] + config["p2p"]:
            path, testcase = selector.split("::", 1)
            if path in self.overlay and path.endswith("_test.go"):
                self.assertRegex(self.overlay[path], r"(?m)^func " + re.escape(testcase.split("/", 1)[0]) + r"\(")

    def test_replayed_evaluation_file_identity(self):
        config = json.loads((TESTS_ROOT / "config.json").read_text())
        git = shutil.which("git")
        self.assertIsNotNone(git, "Git is required for evaluation-file integrity tests")
        with tempfile.TemporaryDirectory(prefix="overlay-", dir=self.root) as directory:
            process = subprocess.run(
                [git, "-c", "core.symlinks=false", "apply", "--binary", "--whitespace=nowarn",
                 str(VERIFIER_ROOT / "test.patch")],
                cwd=directory, env={**self.environment, "GIT_CEILING_DIRECTORIES": str(self.root)},
                capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(process.returncode, 0, process.stderr)
            for name, expected_hash in config["evaluation_files"].items():
                with self.subTest(path=name):
                    target = Path(directory) / name
                    self.assertTrue(target.is_file())
                    self.assertFalse(target.is_symlink())
                    self.assertEqual(hashlib.sha256(target.read_bytes()).hexdigest(), expected_hash)


if __name__ == "__main__":
    unittest.main(verbosity=2)
