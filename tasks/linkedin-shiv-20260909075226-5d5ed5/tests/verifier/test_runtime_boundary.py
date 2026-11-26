"""Calibrate the E3 witness against the production selection boundary.

These controls exercise the existing five interpreter modes without requiring
the compatibility executor to introduce another selection boundary.
"""

import pathlib
import tempfile
import types
import unittest
from unittest.mock import patch


def load_harness():
    patch_text = pathlib.Path(__file__).with_name("test.patch").read_text()
    section = patch_text.split(
        "diff --git a/test/test_f2p_behavior.py b/test/test_f2p_behavior.py\n", 1
    )[1].split("diff --git ", 1)[0]
    source = "\n".join(
        line[1:] for line in section.splitlines()
        if line.startswith("+") and not line.startswith("+++")
    )
    module = types.ModuleType("runtime_boundary_harness")
    exec(compile(source, str(pathlib.Path(__file__).with_name("test.patch")), "exec"), module.__dict__)
    return module


class TestRuntimeBoundary(unittest.TestCase):
    def setUp(self):
        self.harness = load_harness()

    def check_modes(self, boundary, expected, snapshot_expected=None, preamble_expected=None):
        with tempfile.TemporaryDirectory() as tmp:
            repo = pathlib.Path(tmp)
            source = repo / "src" / "shiv" / "bootstrap"
            source.mkdir(parents=True)
            shiv = types.ModuleType("shiv")
            bootstrap = types.ModuleType("shiv.bootstrap")
            interpreter = types.ModuleType("shiv.bootstrap.interpreter")
            environment = types.ModuleType("shiv.bootstrap.environment")
            shiv.bootstrap = bootstrap
            bootstrap.interpreter = interpreter
            bootstrap.site = types.SimpleNamespace(addsitedir=lambda *args: None)
            bootstrap.current_zipfile = lambda: None

            class Environment(types.SimpleNamespace):
                def to_json(self):
                    return "{}"

                @staticmethod
                def from_json(value):
                    raise AssertionError("the harness must supply runtime metadata")

            environment.Environment = Environment
            interpreter_source = '''
import code
import runpy
import sys
from pathlib import Path

def execute_content(name, content, argv0=None):
    raise AssertionError("the harness must observe content execution")

def execute_interpreter():
    args = sys.argv[1:]
    if not args:
        code.interact()
    elif args[0] == "-c":
        content = args[1]
        sys.argv = ["-c", *args[2:]]
        execute_content("-c <cmd>", content, argv0="-c")
    elif args[0] == "-m":
        sys.argv = args[1:]
        runpy.run_module(args[1], run_name="__main__")
    else:
        content = sys.stdin.read() if args[0] == "-" else Path(args[0]).read_text()
        sys.argv = args
        execute_content(args[0], content)
'''
            exec(compile(interpreter_source, str(source / "interpreter.py"), "exec"), interpreter.__dict__)
            bootstrap.__dict__.update(Environment=Environment, interpreter=interpreter)
            bootstrap_source = '''
class Request:
    def execute(self):
        interpreter.execute_interpreter()

def formulate():
    EAGER
    return Request()

def bootstrap():
    with current_zipfile() as archive:
        env = Environment.from_json(archive.read("environment.json"))
    request = formulate()
    EXECUTE
'''.replace(
                "EAGER", "interpreter.execute_interpreter()" if boundary == "eager" else "pass"
            ).replace(
                "EXECUTE", "request.execute()" if boundary != "unused" else "interpreter.execute_interpreter()"
            )
            if boundary == "eager":
                # The target ran during formulation; later consumption does no work.
                bootstrap_source = bootstrap_source.replace(
                    "        interpreter.execute_interpreter()", "        pass", 1
                )
            if boundary == "absent":
                bootstrap_source = bootstrap_source.replace(
                    "request = formulate()\n    request.execute()", "interpreter.execute_interpreter()"
                )
            if boundary in ("snapshot", "late_validation"):
                bootstrap_source = bootstrap_source.replace(
                    "class Request:\n    def execute(self):\n",
                    "class Request:\n"
                    "    def __init__(self):\n"
                    "        self.argv = list(interpreter.sys.argv)\n"
                    "    def execute(self):\n"
                    "        interpreter.sys.argv = list(self.argv)\n",
                )
                if boundary == "snapshot":
                    bootstrap_source = bootstrap_source.replace(
                        "        self.argv = list(interpreter.sys.argv)\n",
                        "        self.argv = list(interpreter.sys.argv)\n"
                        "        if len(self.argv) > 1 and self.argv[1] in ('-c', '-m'):\n"
                        "            self.argv[2]\n",
                    )
            if boundary in ("preamble_snapshot", "preamble_ambient"):
                preamble_source = '''
class PreambleRequest:
    def __init__(self, env, site_packages):
        self.env = env
        self.site_packages = site_packages
        self.archive = interpreter.sys.argv[0]

    def execute(self):
        interpreter.runpy.run_path(
            str(self.site_packages / "bin" / "pre.py"),
            init_globals={
                "archive": ARCHIVE,
                "env": self.env,
                "site_packages": self.site_packages,
            },
            run_name="__main__",
        )

def select_preamble(env, site_packages):
    return PreambleRequest(env, site_packages)

'''.replace(
                    "ARCHIVE",
                    "self.archive" if boundary == "preamble_snapshot" else "interpreter.sys.argv[0]",
                )
                bootstrap_source = preamble_source + bootstrap_source.replace(
                    "    request = formulate()",
                    "    if env.preamble:\n"
                    "        site_packages = interpreter.Path(env.root) / 'app.pyz_probe' / 'site-packages'\n"
                    "        preamble = select_preamble(env, site_packages)\n"
                    "        preamble.execute()\n"
                    "    request = formulate()",
                )
            exec(compile(bootstrap_source, str(source / "__init__.py"), "exec"), bootstrap.__dict__)
            modules = {
                "shiv": shiv, "shiv.bootstrap": bootstrap,
                "shiv.bootstrap.interpreter": interpreter,
                "shiv.bootstrap.environment": environment,
            }
            with patch.dict("sys.modules", modules), patch.object(
                self.harness.sys, "path", list(self.harness.sys.path)
            ), patch.object(
                self.harness, "__file__", str(repo / "test" / "test_f2p_behavior.py"), create=True
            ):
                for mode in ("interp_c", "interp_m", "interp_script", "interp_stdin", "interp_interactive"):
                    with self.subTest(boundary=boundary, mode=mode):
                        self.assertEqual(
                            self.harness.run_e3_witness_case(repo, mode, repo / mode), expected
                        )
                if snapshot_expected is True:
                    self.harness.test_interpreter_primary_request_preserves_selected_arguments(repo / "snapshot")
                elif snapshot_expected is False:
                    reason = "missing operand" if boundary == "late_validation" else "dependent on ambient argv"
                    with self.assertRaisesRegex(AssertionError, reason):
                        self.harness.test_interpreter_primary_request_preserves_selected_arguments(repo / "snapshot")
                if preamble_expected is True:
                    self.harness.test_preamble_request_preserves_selected_archive_context(repo / "preamble")
                elif preamble_expected is False:
                    with self.assertRaisesRegex(AssertionError, "archive context.*ambient argv"):
                        self.harness.test_preamble_request_preserves_selected_archive_context(repo / "preamble")

    def test_production_request_with_procedural_compatibility_executor(self):
        self.check_modes("deferred", True)

    def test_eager_selection_still_fails(self):
        self.check_modes("eager", False)

    def test_unused_request_still_fails(self):
        self.check_modes("unused", False)

    def test_missing_request_still_fails(self):
        self.check_modes("absent", False)

    def test_primary_request_captures_arguments_with_procedural_executor(self):
        self.check_modes("snapshot", True, snapshot_expected=True)

    def test_primary_request_reselects_from_live_arguments_fails(self):
        self.check_modes("deferred", True, snapshot_expected=False)

    def test_incomplete_request_returned_before_operand_validation_fails(self):
        self.check_modes("late_validation", True, snapshot_expected=False)

    def test_preamble_request_captures_archive_with_procedural_primary_executor(self):
        self.check_modes("preamble_snapshot", True, preamble_expected=True)

    def test_preamble_request_reads_ambient_archive_fails(self):
        self.check_modes("preamble_ambient", True, preamble_expected=False)


if __name__ == "__main__":
    unittest.main()
