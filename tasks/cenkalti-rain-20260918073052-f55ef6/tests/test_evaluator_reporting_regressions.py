#!/usr/bin/env python3
"""
Focused regression tests for evaluator reporting and grading logic.
Covers the 6 scenarios mandated by the evaluator pipeline requirements:
1. Clean success.
2. All P2P nodes passing with exactly one ordinary registered F2P failure.
3. All registered nodes passing with an unregistered test failure.
4. Package teardown failure after test completion.
5. Incomplete execution or an unexplained nonzero exit.
6. A registered F2P failure combined with an independent execution abnormality.
"""

import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
CONFIG_PATH = HERE / "config.json"
GRADER_PY = HERE.parent / "authoring" / "platform_grader_fixed.py"
VERIFIER_DIR = HERE / "verifier"

if str(VERIFIER_DIR) not in sys.path:
    sys.path.insert(0, str(VERIFIER_DIR))
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


def run_gate_and_finalize(config_data, ctrf_data, hard_gate_data, apply_failed=0):
    """Helper to run grader gate and finalize using temporary files."""
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        cfg_file = tdp / "config.json"
        ctrf_file = tdp / "ctrf.json"
        hg_file = tdp / "hard_gate.json"
        gate_out = tdp / "gate.json"
        reward_out = tdp / "reward.json"

        # Update config reports to point to temporary directory paths
        cfg_copy = copy.deepcopy(config_data)
        cfg_copy.setdefault("reports", {})["reward"] = str(reward_out)
        cfg_copy["reports"]["reward_details"] = str(tdp / "reward_details.json")

        cfg_file.write_text(json.dumps(cfg_copy))
        ctrf_file.write_text(json.dumps(ctrf_data))
        hg_file.write_text(json.dumps(hard_gate_data))

        # Run grader gate
        gate_proc = subprocess.run(
            [
                sys.executable,
                str(GRADER_PY),
                "gate",
                "--config",
                str(cfg_file),
                "--ctrf",
                str(ctrf_file),
                "--hard-gate",
                str(hg_file),
                "--output",
                str(gate_out),
                "--apply-failed",
                str(apply_failed),
            ],
            capture_output=True,
            text=True,
        )
        assert gate_proc.returncode == 0, f"grader.py gate failed: {gate_proc.stderr}"
        gate_res = json.loads(gate_out.read_text())

        # Run grader.py finalize
        fin_proc = subprocess.run(
            [
                sys.executable,
                str(GRADER_PY),
                "finalize",
                "--config",
                str(cfg_file),
                "--gate",
                str(gate_out),
            ],
            capture_output=True,
            text=True,
        )
        assert fin_proc.returncode == 0, f"grader.py finalize failed: {fin_proc.stderr}"
        reward_res = json.loads(reward_out.read_text())

        return gate_res, reward_res


def make_base_ctrf(config_data, pass_p2p=True, pass_f2p=True, failing_f2p_node=None):
    """Generates a CTRF dictionary with specified node statuses."""
    tests = []
    p2p = config_data.get("p2p", [])
    f2p = config_data.get("f2p", [])

    for node in p2p:
        tests.append({
            "name": node,
            "status": "passed" if pass_p2p else "failed",
            "duration": 0,
            "testId": node,
            "extra": {"deepswe": {"group": "P2P", "required": True}},
        })
    for node in f2p:
        status = "passed"
        if not pass_f2p or (failing_f2p_node and node == failing_f2p_node):
            status = "failed"
        tests.append({
            "name": node,
            "status": status,
            "duration": 0,
            "testId": node,
            "extra": {"deepswe": {"group": "F2P", "required": True}},
        })

    return {
        "reportFormat": "CTRF",
        "specVersion": "0.0.1",
        "results": {
            "tool": {"name": "deepswe-go-verifier"},
            "summary": {
                "tests": len(tests),
                "passed": sum(t["status"] == "passed" for t in tests),
                "failed": sum(t["status"] == "failed" for t in tests),
                "skipped": 0,
                "pending": 0,
                "other": 0,
                "start": 1726900000000,
                "stop": 1726900001000,
            },
            "tests": tests,
            "extra": {
                "deepswe": {
                    "taskId": str(config_data.get("task_id") or config_data.get("taskId") or "cenkalti-rain-20260918073052-f55ef6"),
                    "task_id": str(config_data.get("task_id") or config_data.get("taskId") or "cenkalti-rain-20260918073052-f55ef6"),
                    "baseCommit": str(config_data.get("base_commit") or config_data.get("baseCommit") or "697380ffec04290679230d8d04636eb41c99e0a8"),
                    "base_commit": str(config_data.get("base_commit") or config_data.get("baseCommit") or "697380ffec04290679230d8d04636eb41c99e0a8"),
                    "cmd_returncode": 0 if pass_p2p and pass_f2p and not failing_f2p_node else 1,
                    "cmd_failed": not (pass_p2p and pass_f2p and not failing_f2p_node),
                    "is_unexplained_process": False,
                    "unregistered_failures": [],
                    "abnormal_package_failures": [],
                    "package_failures": [],
                    "incomplete_nodes": [],
                    "execution_abnormality": False,
                }
            },
        }
    }


class EvaluatorReportingRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads(CONFIG_PATH.read_text())
        cls.p2p_nodes = cls.config["p2p"]
        cls.f2p_nodes = cls.config["f2p"]
        cls.hard_gate_passed_data = {
            "passed": True,
            "hard_gate_passed": True,
            "build_passed": True,
            "anti_cheat_passed": True,
            "execution_passed": True,
            "p2p_passed": True,
            "failed_nodes": [],
            "categories": {
                "build": {"passed": True},
                "anti_cheat": {"passed": True},
                "execution": {"passed": True},
                "p2p": {"passed": True},
            },
        }
        cls.hard_gate_failed_data = {
            "passed": False,
            "hard_gate_passed": False,
            "build_passed": True,
            "anti_cheat_passed": True,
            "execution_passed": False,
            "p2p_passed": False,
            "failed_nodes": [cls.p2p_nodes[0]],
            "categories": {
                "build": {"passed": True},
                "anti_cheat": {"passed": True},
                "execution": {"passed": False},
                "p2p": {"passed": False},
            },
        }

    def test_1_clean_success(self):
        """Scenario 1: Clean success - all P2P pass, all F2P pass, no abnormalities."""
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        gate_res, reward_res = run_gate_and_finalize(
            self.config, ctrf, self.hard_gate_passed_data
        )

        self.assertEqual(gate_res["hard_gate_success"], 1)
        self.assertEqual(gate_res["verifier_success"], 1)
        self.assertTrue(gate_res["eligible"])
        self.assertEqual(gate_res["f2p_passed"], len(self.f2p_nodes))
        self.assertEqual(gate_res["p2p_passed"], len(self.p2p_nodes))
        self.assertEqual(gate_res["f2p_pass_ratio"], 1.0)
        self.assertEqual(gate_res["failed_nodes"], [])

        self.assertEqual(reward_res["reward"], 1.0)

    def test_2_p2p_pass_with_one_ordinary_registered_f2p_failure(self):
        """Scenario 2: All P2P pass, exactly 1 registered F2P fails.
        Hardgate must remain successful (1), partial credit must be preserved, reward = 10/11."""
        failing_f2p = self.f2p_nodes[0]
        ctrf = make_base_ctrf(
            self.config, pass_p2p=True, pass_f2p=True, failing_f2p_node=failing_f2p
        )
        gate_res, reward_res = run_gate_and_finalize(
            self.config, ctrf, self.hard_gate_passed_data
        )

        # Hard Gate MUST succeed because all P2P passed and independent HG passed
        self.assertEqual(gate_res["hard_gate_success"], 1, "Hard Gate must succeed despite ordinary F2P failure")
        self.assertEqual(gate_res["verifier_success"], 0, "Verifier success must be 0 when F2P fails")
        self.assertFalse(gate_res["eligible"])
        self.assertEqual(gate_res["f2p_passed"], len(self.f2p_nodes) - 1)
        self.assertEqual(gate_res["p2p_passed"], len(self.p2p_nodes))
        expected_ratio = (len(self.f2p_nodes) - 1) / len(self.f2p_nodes)
        self.assertAlmostEqual(gate_res["f2p_pass_ratio"], expected_ratio)
        self.assertEqual(gate_res["failed_nodes"], [failing_f2p])

        # Finalize reward MUST equal the F2P partial credit ratio, NOT -1.0!
        self.assertAlmostEqual(reward_res["reward"], expected_ratio, places=6)

    def test_3_all_registered_pass_with_unregistered_test_failure(self):
        """Scenario 3: All registered nodes pass, but an unregistered test fails.
        When Hard Gate fails due to the failure, infra anomaly -> reward = -2.0."""
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        # Inject unregistered failure
        extra = ctrf["results"]["extra"]["deepswe"]
        extra["unregistered_failures"] = ["github.com/cenkalti/rain/v2/torrent::TestUnregisteredHelper"]
        extra["execution_abnormality"] = True
        extra["cmd_returncode"] = 1
        extra["cmd_failed"] = True

        gate_res, reward_res = run_gate_and_finalize(
            self.config, ctrf, self.hard_gate_failed_data
        )

        self.assertEqual(gate_res["hard_gate_success"], 0)
        self.assertEqual(gate_res["verifier_success"], 0)
        self.assertFalse(gate_res["eligible"])
        self.assertEqual(reward_res["reward"], -2.0)

    def test_4_package_teardown_failure_after_tests_completion(self):
        """Scenario 4: Package teardown failure after test completion.
        Must trigger abnormal_package_failures, infra anomaly -> reward = -2.0."""
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        extra = ctrf["results"]["extra"]["deepswe"]
        extra["abnormal_package_failures"] = ["github.com/cenkalti/rain/v2/torrent"]
        extra["package_failures"] = ["github.com/cenkalti/rain/v2/torrent"]
        extra["execution_abnormality"] = True
        extra["cmd_returncode"] = 1
        extra["cmd_failed"] = True

        gate_res, reward_res = run_gate_and_finalize(
            self.config, ctrf, self.hard_gate_failed_data
        )

        self.assertEqual(gate_res["hard_gate_success"], 0)
        self.assertEqual(gate_res["verifier_success"], 0)
        self.assertFalse(gate_res["eligible"])
        self.assertEqual(reward_res["reward"], -2.0)

    def test_5_incomplete_execution_or_unexplained_nonzero_exit(self):
        """Scenario 5: Incomplete execution or an unexplained nonzero exit.
        Must fail hard gate and finalize with -2.0."""
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        extra = ctrf["results"]["extra"]["deepswe"]
        extra["is_unexplained_process"] = True
        extra["cmd_failure_reason"] = "exit_code_2"
        extra["execution_abnormality"] = True
        extra["cmd_returncode"] = 2
        extra["cmd_failed"] = True

        gate_res, reward_res = run_gate_and_finalize(
            self.config, ctrf, self.hard_gate_failed_data
        )

        self.assertEqual(gate_res["hard_gate_success"], 0)
        self.assertEqual(gate_res["verifier_success"], 0)
        self.assertFalse(gate_res["eligible"])
        self.assertEqual(reward_res["reward"], -2.0)

    def test_6_registered_f2p_failure_combined_with_independent_execution_abnormality(self):
        """Scenario 6: A registered F2P failure combined with an independent execution abnormality.
        When Hard Gate fails due to the abnormality, reward must be -2.0."""
        failing_f2p = self.f2p_nodes[0]
        ctrf = make_base_ctrf(
            self.config, pass_p2p=True, pass_f2p=True, failing_f2p_node=failing_f2p
        )
        extra = ctrf["results"]["extra"]["deepswe"]
        extra["abnormal_package_failures"] = ["github.com/cenkalti/rain/v2/torrent"]
        extra["package_failures"] = ["github.com/cenkalti/rain/v2/torrent"]
        extra["execution_abnormality"] = True

        gate_res, reward_res = run_gate_and_finalize(
            self.config, ctrf, self.hard_gate_failed_data
        )

        self.assertEqual(gate_res["hard_gate_success"], 0, "Hard Gate must NOT succeed when abnormality coexists with F2P failure")
        self.assertEqual(gate_res["verifier_success"], 0)
        self.assertFalse(gate_res["eligible"])
        self.assertEqual(reward_res["reward"], -2.0, "Coexisting abnormality must trigger -2.0")


class TestVerifierPipelineIntegration(unittest.TestCase):
    """Full-pipeline integration tests exercising the production verifier entrypoint (verifier.main)
    and the unchanged platform grader commands (grader.py gate and finalize).

    In every test:
    - Independent Hardgate starts with a valid passing result (passed: True), except
      for the independent hardgate failure scenario.
    - Controlled Go JSON events and process outcomes are fed through verifier.main.
    - Reports written by verifier.main (both hard-gate.json and ctrf.json) are inspected.
    - The unchanged grader gate and finalize commands are invoked.
    - The test verifies whether verifier.py properly transitioned or preserved the Hardgate
      report and whether the grader computed the exact expected reward and success metrics.
    """

    @classmethod
    def setUpClass(cls):
        import verifier
        cls.verifier_main = staticmethod(verifier.main)
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            cls.config = json.load(f)
        cls.p2p_nodes = cls.config.get("p2p", [])
        cls.f2p_nodes = cls.config.get("f2p", [])

    def _make_passing_hardgate_data(self):
        return {
            "passed": True,
            "apply_failed": False,
            "build_passed": True,
            "anti_cheat_passed": True,
            "p2p_passed": True,
            "failed_nodes": [],
            "categories": {
                "build": {"passed": True, "failed_nodes": [], "details": {}},
                "anti_cheat": {"passed": True, "failed_nodes": [], "details": {}},
                "p2p": {
                    "passed": True,
                    "total_nodes": len(self.p2p_nodes),
                    "passed_nodes": len(self.p2p_nodes),
                    "failed_nodes": [],
                    "details": {"passed_p2p_nodes": list(self.p2p_nodes)},
                },
            },
            "summary": {
                "build": "PASSED",
                "anti_cheat": "PASSED",
                "p2p": "PASSED",
            },
        }

    def _make_failing_hardgate_data(self):
        return {
            "passed": False,
            "apply_failed": False,
            "build_passed": True,
            "anti_cheat_passed": False,
            "p2p_passed": False,
            "failed_nodes": ["cheat_evaluator_test_tampered:torrent/evaluator_session_lifecycle_test.go"],
            "categories": {
                "build": {"passed": True, "failed_nodes": [], "details": {}},
                "anti_cheat": {"passed": False, "failed_nodes": ["cheat_evaluator_test_tampered"], "details": {}},
                "p2p": {"passed": False, "failed_nodes": ["p2p_skipped"], "details": {}},
            },
            "summary": {
                "build": "PASSED",
                "anti_cheat": "FAILED",
                "p2p": "FAILED",
            },
        }

    def generate_raw_go_events(
        self,
        pass_p2p=True,
        pass_f2p=True,
        failing_f2p_node=None,
        extra_events=None,
        package_status=None,
        omit_terminal_nodes=None,
    ):
        """Generates realistic raw `go test -json` newline-delimited JSON stream."""
        lines = []
        pkgs = set()
        omit_terminal_nodes = set(omit_terminal_nodes or [])

        for node in self.p2p_nodes + self.f2p_nodes:
            file_part, test_part = node.split("::")
            if file_part.startswith("github.com/cenkalti/rain/v2"):
                pkg = file_part
            else:
                rel_dir = os.path.dirname(file_part)
                pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")
            pkgs.add(pkg)

        for pkg in sorted(pkgs):
            lines.append(json.dumps({"Action": "start", "Package": pkg}))

        for node in self.p2p_nodes:
            file_part, test_part = node.split("::")
            if file_part.startswith("github.com/cenkalti/rain/v2"):
                pkg = file_part
            else:
                rel_dir = os.path.dirname(file_part)
                pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")
            lines.append(json.dumps({"Action": "run", "Package": pkg, "Test": test_part}))
            if node not in omit_terminal_nodes:
                status = "pass" if pass_p2p else "fail"
                lines.append(json.dumps({"Action": status, "Package": pkg, "Test": test_part, "Elapsed": 0.01}))

        for node in self.f2p_nodes:
            file_part, test_part = node.split("::")
            if file_part.startswith("github.com/cenkalti/rain/v2"):
                pkg = file_part
            else:
                rel_dir = os.path.dirname(file_part)
                pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")
            lines.append(json.dumps({"Action": "run", "Package": pkg, "Test": test_part}))
            if node not in omit_terminal_nodes:
                status = "fail" if (node == failing_f2p_node or not pass_f2p) else "pass"
                lines.append(json.dumps({"Action": status, "Package": pkg, "Test": test_part, "Elapsed": 0.01}))

        if extra_events:
            for ev in extra_events:
                lines.append(json.dumps(ev))

        pkg_status_map = package_status or {}
        for pkg in sorted(pkgs):
            action = pkg_status_map.get(pkg, "pass")
            lines.append(json.dumps({"Action": action, "Package": pkg, "Elapsed": 0.5}))

        return "\n".join(lines) + "\n"

    def run_pipeline(
        self,
        stdout_events: str,
        stderr: str = "",
        returncode: int = 0,
        apply_failed: int = 0,
        initial_hardgate_data: dict | None = None,
    ):
        if initial_hardgate_data is None:
            initial_hardgate_data = self._make_passing_hardgate_data()

        with tempfile.TemporaryDirectory() as td:
            tdp = Path(td)
            cfg_file = tdp / "config.json"
            ctrf_file = tdp / "ctrf.json"
            hg_file = tdp / "hard_gate.json"
            gate_out = tdp / "gate.json"
            reward_out = tdp / "reward.json"
            reward_details_out = tdp / "reward_details.json"
            events_file = tdp / "events.json"

            cfg_copy = copy.deepcopy(self.config)
            cfg_copy.setdefault("reports", {})["reward"] = str(reward_out)
            cfg_copy["reports"]["reward_details"] = str(reward_details_out)

            cfg_file.write_text(json.dumps(cfg_copy, indent=2), encoding="utf-8")
            hg_file.write_text(json.dumps(initial_hardgate_data, indent=2), encoding="utf-8")
            events_file.write_text(stdout_events, encoding="utf-8")

            # 1. Invoke the production verifier entrypoint with controlled Go events via test-process mock
            argv = [
                "--config", str(cfg_file),
                "--repo", str(REPO_ROOT / "source"),
                "--ctrf-output", str(ctrf_file),
                "--hard-gate-output", str(hg_file),
                "--apply-failed", str(apply_failed),
            ]
            from unittest.mock import patch
            from collections import namedtuple
            CompletedProc = namedtuple("CompletedProc", ["args", "returncode", "stdout", "stderr"])

            def mock_run(cmd, *cmd_args, **cmd_kwargs):
                cmd_str = " ".join(str(c) for c in cmd)
                if "hardgate.py" in cmd_str:
                    out_idx = cmd.index("--output") + 1
                    dest_p = Path(cmd[out_idx])
                    dest_p.write_text(json.dumps(initial_hardgate_data, indent=2), encoding="utf-8")
                    return CompletedProc(cmd, 0, "", "")
                elif len(cmd) >= 2 and cmd[0] == "go" and cmd[1] == "test":
                    return CompletedProc(cmd, returncode, stdout_events, stderr)
                return subprocess.run(cmd, *cmd_args, **cmd_kwargs)

            with patch("verifier.subprocess.run", side_effect=mock_run):
                v_exit = self.verifier_main(argv)
            self.assertEqual(v_exit, 0, f"verifier.main must return 0, got {v_exit}")

            # 2. Inspect reports written by verifier.main
            updated_hg = json.loads(hg_file.read_text(encoding="utf-8"))
            ctrf = json.loads(ctrf_file.read_text(encoding="utf-8"))

            # 3. Invoke unchanged grader gate
            gate_proc = subprocess.run(
                [
                    sys.executable, str(GRADER_PY), "gate",
                    "--config", str(cfg_file),
                    "--ctrf", str(ctrf_file),
                    "--hard-gate", str(hg_file),
                    "--output", str(gate_out),
                    "--apply-failed", str(apply_failed),
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(gate_proc.returncode, 0, f"grader.py gate failed: {gate_proc.stderr}")
            gate_res = json.loads(gate_out.read_text(encoding="utf-8"))

            # 4. Invoke unchanged grader finalize
            fin_proc = subprocess.run(
                [
                    sys.executable, str(GRADER_PY), "finalize",
                    "--config", str(cfg_file),
                    "--gate", str(gate_out),
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(fin_proc.returncode, 0, f"grader.py finalize failed: {fin_proc.stderr}")
            reward_res = json.loads(reward_out.read_text(encoding="utf-8"))
            details_res = json.loads(reward_details_out.read_text(encoding="utf-8"))

            return updated_hg, ctrf, gate_res, reward_res, details_res

    def assert_valid_ctrf_schema(self, ctrf):
        self.assertEqual(ctrf.get("reportFormat"), "CTRF")
        self.assertEqual(ctrf.get("specVersion"), "0.0.1")
        self.assertIn("results", ctrf)
        results = ctrf["results"]
        self.assertIn("tool", results)
        self.assertIn("name", results["tool"])
        self.assertIn("summary", results)
        summary = results["summary"]
        for key in ["tests", "passed", "failed", "skipped", "pending", "other", "start", "stop"]:
            self.assertIn(key, summary, f"Summary missing required key: {key}")
            self.assertIsInstance(summary[key], int, f"Summary key {key} must be an integer")
        self.assertIn("tests", results)
        self.assertIsInstance(results["tests"], list)
        for t in results["tests"]:
            self.assertIn("name", t)
            self.assertIn("status", t)
            self.assertIn(t["status"], {"passed", "failed", "skipped", "pending", "other"})
            self.assertIn("duration", t)
            self.assertIsInstance(t["duration"], int)
        self.assertIn("extra", results)
        self.assertIn("deepswe", results["extra"])
        self.assertIn("taskId", results["extra"]["deepswe"])
        self.assertTrue(results["extra"]["deepswe"]["taskId"])
        self.assertIn("baseCommit", results["extra"]["deepswe"])
        self.assertTrue(results["extra"]["deepswe"]["baseCommit"])

    def test_pipeline_1_clean_success(self):
        """1. Clean success: all P2P pass, all F2P pass, process exit 0.
        Hardgate remains valid, grader grants full credit (reward = 1.0)."""
        stdout = self.generate_raw_go_events(pass_p2p=True, pass_f2p=True)
        hg, ctrf, gate_res, reward_res, _ = self.run_pipeline(stdout, returncode=0)

        # Validate CTRF schema
        self.assert_valid_ctrf_schema(ctrf)

        # Hardgate remains valid
        self.assertTrue(hg["passed"], "Hardgate must remain valid for clean run")
        self.assertTrue(hg.get("execution_passed", False))
        self.assertEqual(hg["summary"]["execution"], "PASSED")

        # Grader outcome
        self.assertEqual(gate_res["hard_gate_success"], 1)
        self.assertEqual(gate_res["verifier_success"], 1)
        self.assertTrue(gate_res["eligible"])
        self.assertEqual(gate_res["f2p_passed"], len(self.f2p_nodes))
        self.assertEqual(gate_res["p2p_passed"], len(self.p2p_nodes))
        self.assertEqual(gate_res["failed_nodes"], [])
        self.assertEqual(reward_res["reward"], 1.0)

    def test_pipeline_2_one_ordinary_registered_f2p_failure_preserved_partial_credit(self):
        """2. One ordinary registered F2P failure: exit 1, no abnormalities.
        Hardgate remains valid, proportional credit preserved, overall success prevented."""
        failing_f2p = self.f2p_nodes[0]
        file_part, test_part = failing_f2p.split("::")
        rel_dir = os.path.dirname(file_part)
        failing_pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")

        stdout = self.generate_raw_go_events(
            pass_p2p=True,
            pass_f2p=True,
            failing_f2p_node=failing_f2p,
            package_status={failing_pkg: "fail"},
        )
        hg, ctrf, gate_res, reward_res, _ = self.run_pipeline(stdout, returncode=1)

        # Hardgate remains valid despite registered F2P failure!
        self.assertTrue(hg["passed"], "Hardgate must remain valid for ordinary F2P failure")
        self.assertTrue(hg.get("execution_passed", False))
        self.assertEqual(hg["summary"]["execution"], "PASSED")

        # Grader outcome: hard_gate_success=1, verifier_success=0, proportional reward
        self.assertEqual(gate_res["hard_gate_success"], 1)
        self.assertEqual(gate_res["verifier_success"], 0)
        self.assertFalse(gate_res["eligible"])
        self.assertEqual(gate_res["failed_nodes"], [failing_f2p])
        expected_ratio = (len(self.f2p_nodes) - 1) / len(self.f2p_nodes)
        self.assertAlmostEqual(gate_res["f2p_pass_ratio"], expected_ratio, places=6)
        self.assertAlmostEqual(reward_res["reward"], expected_ratio, places=6)

    def test_pipeline_3_all_registered_pass_with_unregistered_failure(self):
        """3. All registered nodes pass, but an unregistered test fails.
        Production verifier must invalidate the initially passing Hardgate report;
        Grader must reject the candidate (hard_gate_success=0, reward=-1.0)."""
        extra = [
            {"Action": "run", "Package": "github.com/cenkalti/rain/v2/torrent", "Test": "TestUnregisteredMystery"},
            {"Action": "fail", "Package": "github.com/cenkalti/rain/v2/torrent", "Test": "TestUnregisteredMystery", "Elapsed": 0.02},
        ]
        stdout = self.generate_raw_go_events(
            pass_p2p=True,
            pass_f2p=True,
            extra_events=extra,
            package_status={"github.com/cenkalti/rain/v2/torrent": "fail"},
        )
        hg, ctrf, gate_res, reward_res, _ = self.run_pipeline(stdout, returncode=1)

        # Verifier must transition Hardgate passed from True to False!
        self.assertFalse(hg["passed"], "Verifier must set Hardgate passed to False")
        self.assertFalse(hg.get("execution_passed", True))
        self.assertEqual(hg["summary"]["execution"], "FAILED")
        self.assertTrue(any("unregistered_failure:" in fn for fn in hg.get("failed_nodes", [])))

        # Grader rejection
        self.assertEqual(gate_res["hard_gate_success"], 0)
        self.assertEqual(gate_res["verifier_success"], 0)
        self.assertFalse(gate_res["eligible"])
        self.assertEqual(reward_res["reward"], -2.0)

    def test_pipeline_4_package_teardown_failure(self):
        """4. Package teardown failure (e.g. goleak/panic after test completion).
        Verifier invalidates Hardgate report; grader rejects candidate with -2.0."""
        extra = [
            {"Action": "output", "Package": "github.com/cenkalti/rain/v2/torrent", "Output": "goleak: found unexpected goroutines:\n[goroutine 42]"},
        ]
        stdout = self.generate_raw_go_events(
            pass_p2p=True,
            pass_f2p=True,
            extra_events=extra,
            package_status={"github.com/cenkalti/rain/v2/torrent": "fail"},
        )
        hg, ctrf, gate_res, reward_res, _ = self.run_pipeline(stdout, returncode=1)

        self.assertFalse(hg["passed"], "Verifier must invalidate Hardgate on teardown failure")
        self.assertEqual(hg["summary"]["execution"], "FAILED")
        self.assertTrue(any("abnormal_package_failure:" in fn for fn in hg.get("failed_nodes", [])))

        self.assertEqual(gate_res["hard_gate_success"], 0)
        self.assertEqual(gate_res["verifier_success"], 0)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_pipeline_4b_data_race_detection(self):
        """Data race detection:
        Feeding synthetic 'WARNING: DATA RACE' package output through the verifier
        invalidates Hardgate report and grader rejects candidate with -2.0 reward.
        """
        extra = [
            {"Action": "output", "Package": "github.com/cenkalti/rain/v2/torrent", "Output": "==================\nWARNING: DATA RACE\nRead at 0x00c000123456 by goroutine 7:\n  github.com/cenkalti/rain/v2/torrent.(*Session).Close()\n=================="},
        ]
        stdout = self.generate_raw_go_events(
            pass_p2p=True,
            pass_f2p=True,
            extra_events=extra,
            package_status={"github.com/cenkalti/rain/v2/torrent": "fail"},
        )
        hg, ctrf, gate_res, reward_res, _ = self.run_pipeline(stdout, returncode=1)

        self.assertFalse(hg["passed"], "Verifier must invalidate Hardgate on data race detection")
        self.assertEqual(hg["summary"]["execution"], "FAILED")
        self.assertTrue(any("abnormal_package_failure:" in fn for fn in hg.get("failed_nodes", [])))

        self.assertEqual(gate_res["hard_gate_success"], 0)
        self.assertEqual(gate_res["verifier_success"], 0)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_pipeline_5_started_test_or_package_without_terminal_completion(self):
        """5. Started test or package without terminal completion:
        Process exits 0, but started test has no terminal action.
        Verifier invalidates Hardgate report; grader rejects candidate with -2.0."""
        extra = [
            {"Action": "run", "Package": "github.com/cenkalti/rain/v2/torrent", "Test": "TestUnregisteredHangingWorker"},
        ]
        stdout = self.generate_raw_go_events(
            pass_p2p=True,
            pass_f2p=True,
            extra_events=extra,
        )
        hg, ctrf, gate_res, reward_res, _ = self.run_pipeline(stdout, returncode=0)

        self.assertFalse(hg["passed"], "Verifier must invalidate Hardgate on unterminated test")
        self.assertEqual(hg["summary"]["execution"], "FAILED")
        self.assertTrue(any("unterminated_test:" in fn for fn in hg.get("failed_nodes", [])))

        self.assertEqual(gate_res["hard_gate_success"], 0)
        self.assertEqual(gate_res["verifier_success"], 0)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_pipeline_6_contradictory_and_duplicate_terminal_outcomes(self):
        """6. Contradictory and prohibited duplicate terminal outcomes:
        Both contradictory (fail then pass) and duplicate (pass then pass) must invalidate Hardgate with -2.0."""
        # 6a: Contradictory test events (fail then pass)
        target_node = self.p2p_nodes[0]
        file_part, test_part = target_node.split("::")
        rel_dir = os.path.dirname(file_part)
        pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")

        extra_contra = [
            {"Action": "fail", "Package": pkg, "Test": test_part, "Elapsed": 0.01},
            {"Action": "pass", "Package": pkg, "Test": test_part, "Elapsed": 0.02},
        ]
        stdout_contra = self.generate_raw_go_events(
            pass_p2p=True,
            pass_f2p=True,
            omit_terminal_nodes=[target_node],
            extra_events=extra_contra,
        )
        hg_c, _, gate_c, reward_c, _ = self.run_pipeline(stdout_contra, returncode=0)
        self.assertFalse(hg_c["passed"])
        self.assertEqual(gate_c["hard_gate_success"], 0)
        self.assertEqual(reward_c["reward"], -2.0)

        # 6b: Duplicate terminal events (repeated pass)
        target_node2 = self.p2p_nodes[1]
        file_part2, test_part2 = target_node2.split("::")
        rel_dir2 = os.path.dirname(file_part2)
        pkg2 = "github.com/cenkalti/rain/v2" + ("/" + rel_dir2 if rel_dir2 else "")

        extra_dup = [
            {"Action": "pass", "Package": pkg2, "Test": test_part2, "Elapsed": 0.01},
            {"Action": "pass", "Package": pkg2, "Test": test_part2, "Elapsed": 0.02},
        ]
        stdout_dup = self.generate_raw_go_events(
            pass_p2p=True,
            pass_f2p=True,
            omit_terminal_nodes=[target_node2],
            extra_events=extra_dup,
        )
        hg_d, _, gate_d, reward_d, _ = self.run_pipeline(stdout_dup, returncode=0)
        self.assertFalse(hg_d["passed"])
        self.assertEqual(gate_d["hard_gate_success"], 0)
        self.assertEqual(reward_d["reward"], -2.0)

    def test_pipeline_7_unexplained_nonzero_process_exit(self):
        """7. Unexplained nonzero process exit:
        Process exits 2 with no failing tests recorded.
        Verifier invalidates Hardgate report; grader rejects candidate with -2.0."""
        stdout = self.generate_raw_go_events(pass_p2p=True, pass_f2p=True)
        hg, ctrf, gate_res, reward_res, _ = self.run_pipeline(
            stdout,
            stderr="fatal: test runner crashed with signal 11",
            returncode=2,
        )

        self.assertFalse(hg["passed"], "Verifier must invalidate Hardgate on exit code 2")
        self.assertEqual(hg["summary"]["execution"], "FAILED")
        self.assertTrue(any("unexplained_process_failure:" in fn for fn in hg.get("failed_nodes", [])))

        self.assertEqual(gate_res["hard_gate_success"], 0)
        self.assertEqual(gate_res["verifier_success"], 0)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_pipeline_8_registered_f2p_failure_combined_with_independent_abnormality(self):
        """8. Registered F2P failure combined with an independent abnormality:
        An ordinary F2P test fails, but an unregistered test is left unterminated.
        Partial credit must be denied, Hardgate invalidated, reward -2.0."""
        failing_f2p = self.f2p_nodes[0]
        file_part, test_part = failing_f2p.split("::")
        rel_dir = os.path.dirname(file_part)
        failing_pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")

        extra = [
            {"Action": "run", "Package": "github.com/cenkalti/rain/v2/torrent", "Test": "TestUnregisteredUnterminated"},
        ]
        stdout = self.generate_raw_go_events(
            pass_p2p=True,
            pass_f2p=True,
            failing_f2p_node=failing_f2p,
            extra_events=extra,
            package_status={failing_pkg: "fail"},
        )
        hg, ctrf, gate_res, reward_res, _ = self.run_pipeline(stdout, returncode=1)

        self.assertFalse(hg["passed"], "Coexisting abnormality must invalidate Hardgate")
        self.assertEqual(gate_res["hard_gate_success"], 0)
        self.assertEqual(reward_res["reward"], -2.0, "Reward must be -2.0 when abnormality coexists with F2P failure")

    def test_pipeline_9_independent_hardgate_failure_remains_failure(self):
        """9. Independent Hardgate failure remaining a failure:
        Candidate fails initial Hardgate checks (e.g. anti-cheat tampering).
        Verifier generates failure CTRF report, returns 0, and grader awards -1.0."""
        stdout = self.generate_raw_go_events(pass_p2p=True, pass_f2p=True)
        failing_hg = self._make_failing_hardgate_data()
        hg, ctrf, gate_res, reward_res, _ = self.run_pipeline(
            stdout,
            returncode=0,
            initial_hardgate_data=failing_hg,
        )

        self.assertFalse(hg["passed"])
        self.assert_valid_ctrf_schema(ctrf)
        self.assertEqual(gate_res["hard_gate_success"], 0)
        self.assertEqual(gate_res["verifier_success"], 0)
        self.assertFalse(gate_res["eligible"])
        self.assertEqual(reward_res["reward"], -1.0)


class TestBypassProtectionRegressions(unittest.TestCase):
    """Regressions ensuring simulation controls cannot be supplied via production CLI or environment,
    an empty repository with fabricated reports cannot succeed, and normal evaluation invokes
    the real subprocess commands in proper sequence.
    """

    @classmethod
    def setUpClass(cls):
        import verifier
        cls.verifier_main = staticmethod(verifier.main)
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            cls.config = json.load(f)

    def test_removed_cli_options_rejected_with_system_exit(self):
        """Removed CLI simulation flags must be rejected by argparse and must not permit evaluation."""
        removed_flags = [
            ["--skip-hardgate-exec"],
            ["--test-events", "/tmp/fake.json"],
            ["--test-returncode", "0"],
            ["--test-stderr", "error"],
        ]
        with tempfile.TemporaryDirectory() as td:
            tdp = Path(td)
            cfg_file = tdp / "config.json"
            cfg_file.write_text(json.dumps(self.config), encoding="utf-8")
            ctrf_file = tdp / "ctrf.json"
            hg_file = tdp / "hard_gate.json"

            base_argv = [
                "--config", str(cfg_file),
                "--repo", str(REPO_ROOT / "source"),
                "--ctrf-output", str(ctrf_file),
                "--hard-gate-output", str(hg_file),
                "--apply-failed", "0",
            ]
            for flag in removed_flags:
                with self.assertRaises(SystemExit) as ctx:
                    self.verifier_main(base_argv + flag)
                # argparse exits with code 2 on unknown arguments
                self.assertEqual(ctx.exception.code, 2)
                # Ensure no CTRF or Hardgate evaluation output was written
                self.assertFalse(ctrf_file.exists())

    def test_legacy_environment_variables_do_not_replace_subprocess_execution(self):
        """Legacy simulation environment variables must NOT bypass or replace actual subprocess calls."""
        with tempfile.TemporaryDirectory() as td:
            tdp = Path(td)
            cfg_file = tdp / "config.json"
            cfg_file.write_text(json.dumps(self.config), encoding="utf-8")
            ctrf_file = tdp / "ctrf.json"
            hg_file = tdp / "hard_gate.json"

            argv = [
                "--config", str(cfg_file),
                "--repo", str(REPO_ROOT / "source"),
                "--ctrf-output", str(ctrf_file),
                "--hard-gate-output", str(hg_file),
                "--apply-failed", "0",
            ]

            env_patch = {
                "_DEEPSWE_SKIP_HARDGATE_EXEC": "1",
                "_DEEPSWE_TEST_GO_EVENTS": str(tdp / "fabricated_events.json"),
                "_DEEPSWE_TEST_GO_RC": "0",
                "_DEEPSWE_TEST_GO_STDERR": "",
            }

            executed_commands = []
            from unittest.mock import patch
            from collections import namedtuple
            CompletedProc = namedtuple("CompletedProc", ["args", "returncode", "stdout", "stderr"])

            def spy_subprocess_run(cmd, *a, **kw):
                executed_commands.append(list(cmd))
                cmd_str = " ".join(str(c) for c in cmd)
                if "hardgate.py" in cmd_str:
                    out_idx = cmd.index("--output") + 1
                    Path(cmd[out_idx]).write_text(json.dumps({"passed": True, "failed_nodes": []}), encoding="utf-8")
                    return CompletedProc(cmd, 0, "", "")
                elif len(cmd) >= 2 and cmd[0] == "go" and cmd[1] == "test":
                    return CompletedProc(cmd, 0, "", "")
                return subprocess.run(cmd, *a, **kw)

            with patch.dict(os.environ, env_patch), patch("verifier.subprocess.run", side_effect=spy_subprocess_run):
                ret = self.verifier_main(argv)

            self.assertEqual(ret, 0)
            # Verify hardgate.py was STILL executed (not skipped despite env var)
            self.assertTrue(
                any("hardgate.py" in " ".join(str(c) for c in cmd) for cmd in executed_commands),
                "hardgate.py must be executed even when _DEEPSWE_SKIP_HARDGATE_EXEC is set",
            )
            # Verify go test was STILL executed (not replaced despite env var)
            self.assertTrue(
                any(len(cmd) >= 2 and cmd[0] == "go" and cmd[1] == "test" for cmd in executed_commands),
                "go test must be executed even when _DEEPSWE_TEST_GO_EVENTS is set",
            )

    def test_empty_repository_with_fabricated_passing_reports_cannot_pass(self):
        """An empty repository plus a pre-existing fabricated passing report must not evaluate to success."""
        with tempfile.TemporaryDirectory() as td:
            tdp = Path(td)
            empty_repo = tdp / "empty_repo"
            empty_repo.mkdir()
            cfg_file = tdp / "config.json"
            cfg_file.write_text(json.dumps(self.config), encoding="utf-8")
            ctrf_file = tdp / "ctrf.json"
            hg_file = tdp / "hard_gate.json"

            # Plant a fabricated passing Hardgate report
            hg_file.write_text(
                json.dumps({
                    "passed": True,
                    "apply_failed": False,
                    "build_passed": True,
                    "anti_cheat_passed": True,
                    "p2p_passed": True,
                    "failed_nodes": [],
                }),
                encoding="utf-8",
            )

            argv = [
                "--config", str(cfg_file),
                "--repo", str(empty_repo),
                "--ctrf-output", str(ctrf_file),
                "--hard-gate-output", str(hg_file),
                "--apply-failed", "0",
            ]

            # Run verifier against empty_repo without mocking hardgate execution.
            # Real hardgate.py runs against empty_repo: it cannot pass.
            try:
                ret = self.verifier_main(argv)
            except SystemExit as e:
                ret = e.code

            # In either case, the fabricated passing report MUST NOT result in passed=True
            if hg_file.exists():
                hg_res = json.loads(hg_file.read_text(encoding="utf-8"))
                self.assertFalse(hg_res.get("passed", False), "Empty repository must never be marked as passed")

    def test_normal_evaluation_invokes_expected_real_subprocess_commands(self):
        """Normal evaluation must orchestrate the exact expected real subprocess commands in sequence."""
        with tempfile.TemporaryDirectory() as td:
            tdp = Path(td)
            cfg_file = tdp / "config.json"
            cfg_file.write_text(json.dumps(self.config), encoding="utf-8")
            ctrf_file = tdp / "ctrf.json"
            hg_file = tdp / "hard_gate.json"

            argv = [
                "--config", str(cfg_file),
                "--repo", str(REPO_ROOT / "source"),
                "--ctrf-output", str(ctrf_file),
                "--hard-gate-output", str(hg_file),
                "--apply-failed", "0",
            ]

            executed_calls = []
            from unittest.mock import patch
            from collections import namedtuple
            CompletedProc = namedtuple("CompletedProc", ["args", "returncode", "stdout", "stderr"])

            def track_subprocess_run(cmd, *a, **kw):
                executed_calls.append({"cmd": list(cmd), "kwargs": kw})
                cmd_str = " ".join(str(c) for c in cmd)
                if "hardgate.py" in cmd_str:
                    out_idx = cmd.index("--output") + 1
                    Path(cmd[out_idx]).write_text(json.dumps({"passed": True, "failed_nodes": []}), encoding="utf-8")
                    return CompletedProc(cmd, 0, "", "")
                elif len(cmd) >= 2 and cmd[0] == "go" and cmd[1] == "test":
                    return CompletedProc(cmd, 0, "", "")
                return subprocess.run(cmd, *a, **kw)

            with patch("verifier.subprocess.run", side_effect=track_subprocess_run):
                ret = self.verifier_main(argv)

            self.assertEqual(ret, 0)
            self.assertEqual(len(executed_calls), 2)

            # Command 1: hardgate.py
            cmd1 = executed_calls[0]["cmd"]
            self.assertEqual(cmd1[0], sys.executable)
            self.assertTrue(cmd1[1].endswith("hardgate.py"))
            self.assertIn("--config", cmd1)
            self.assertIn("--repo", cmd1)
            self.assertIn("--output", cmd1)

            # Command 2: go test
            cmd2_test = executed_calls[1]["cmd"]
            self.assertEqual(cmd2_test, ["go", "test", "-race", "-count=1", "-json", "./..."])
            self.assertEqual(str(executed_calls[1]["kwargs"].get("cwd")), str(REPO_ROOT / "source"))


class TestHardgateRawEventRegressions(unittest.TestCase):
    """Direct regressions for hardgate.check_p2p() testing contradictory, duplicate,
    and package-level event stream detection using synthetic event streams."""

    @classmethod
    def setUpClass(cls):
        from unittest.mock import patch
        from hardgate import check_p2p
        from collections import namedtuple

        cls.check_p2p = staticmethod(check_p2p)
        cls.ProcMock = namedtuple("ProcMock", ["returncode", "stdout", "stderr"])
        cls.config = json.loads(CONFIG_PATH.read_text())
        cls.repo = REPO_ROOT / "source"
        cls.verifier_dir = VERIFIER_DIR

    def _generate_clean_p2p_stream(self):
        lines = []
        pkgs = set()
        for node in self.config["p2p"]:
            f, t = node.split("::")
            rel_dir = os.path.dirname(f)
            pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")
            pkgs.add(pkg)
            lines.append(json.dumps({"Action": "run", "Package": pkg, "Test": t}))
            lines.append(json.dumps({"Action": "pass", "Package": pkg, "Test": t, "Elapsed": 0.01}))

        for pkg in sorted(pkgs):
            lines.insert(0, json.dumps({"Action": "start", "Package": pkg}))
            lines.append(json.dumps({"Action": "pass", "Package": pkg, "Elapsed": 0.1}))
        return lines

    def test_hardgate_rejects_contradictory_fail_then_pass(self):
        """Hardgate must fail when the same P2P test reports fail then pass."""
        from unittest.mock import patch
        lines = self._generate_clean_p2p_stream()
        target_node = self.config["p2p"][0]
        f, t = target_node.split("::")
        rel_dir = os.path.dirname(f)
        pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")

        # Inject fail event before the existing pass event
        lines.append(json.dumps({"Action": "fail", "Package": pkg, "Test": t, "Elapsed": 0.01}))

        with patch("hardgate.run_cmd", return_value=self.ProcMock(0, "\n".join(lines), "")):
            passed, failed_nodes, details = self.check_p2p(self.repo, self.config, self.verifier_dir)

        self.assertFalse(passed, "Hardgate must not pass when contradictory events occur")
        self.assertTrue(any("p2p_conflicting_event" in fn for fn in failed_nodes))
        self.assertTrue(any(f"{pkg}::{t}" in ce for ce in details.get("conflicting_events", [])))

    def test_hardgate_rejects_contradictory_pass_then_fail(self):
        """Hardgate must fail when the same P2P test reports pass then fail."""
        from unittest.mock import patch
        lines = self._generate_clean_p2p_stream()
        target_node = self.config["p2p"][1]
        f, t = target_node.split("::")
        rel_dir = os.path.dirname(f)
        pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")

        lines.append(json.dumps({"Action": "fail", "Package": pkg, "Test": t, "Elapsed": 0.02}))

        with patch("hardgate.run_cmd", return_value=self.ProcMock(0, "\n".join(lines), "")):
            passed, failed_nodes, details = self.check_p2p(self.repo, self.config, self.verifier_dir)

        self.assertFalse(passed)
        self.assertTrue(any("p2p_conflicting_event" in fn for fn in failed_nodes))

    def test_hardgate_rejects_duplicate_terminal_pass(self):
        """Hardgate must fail when the same P2P test reports repeated pass."""
        from unittest.mock import patch
        lines = self._generate_clean_p2p_stream()
        target_node = self.config["p2p"][2]
        f, t = target_node.split("::")
        rel_dir = os.path.dirname(f)
        pkg = "github.com/cenkalti/rain/v2" + ("/" + rel_dir if rel_dir else "")

        lines.append(json.dumps({"Action": "pass", "Package": pkg, "Test": t, "Elapsed": 0.02}))

        with patch("hardgate.run_cmd", return_value=self.ProcMock(0, "\n".join(lines), "")):
            passed, failed_nodes, details = self.check_p2p(self.repo, self.config, self.verifier_dir)

        self.assertFalse(passed)
        self.assertTrue(any("p2p_duplicate_terminal" in fn for fn in failed_nodes))

    def test_hardgate_rejects_conflicting_package_outcomes(self):
        """Hardgate must fail when a package reports conflicting terminal outcomes."""
        from unittest.mock import patch
        lines = self._generate_clean_p2p_stream()
        pkg = "github.com/cenkalti/rain/v2/internal/allocator"

        lines.append(json.dumps({"Action": "fail", "Package": pkg, "Elapsed": 0.5}))

        with patch("hardgate.run_cmd", return_value=self.ProcMock(0, "\n".join(lines), "")):
            passed, failed_nodes, details = self.check_p2p(self.repo, self.config, self.verifier_dir)

        self.assertFalse(passed)
        self.assertTrue(any("p2p_conflicting_event" in fn for fn in failed_nodes))


class TestHardgateAntiCheatTestFileRegressions(unittest.TestCase):
    """Direct regressions for hardgate.check_anti_cheat() using real Git repositories,
    ensuring candidate cannot add, modify, rename, delete, or submit any test files."""

    @classmethod
    def setUpClass(cls):
        from hardgate import check_anti_cheat

        cls.check_anti_cheat = staticmethod(check_anti_cheat)
        cls.config = json.loads(CONFIG_PATH.read_text())
        cls.verifier_dir = VERIFIER_DIR

    def _create_real_git_repo(self):
        td = tempfile.TemporaryDirectory()
        tmp_repo = Path(td.name) / "repo"
        subprocess.run(["cp", "-R", str(REPO_ROOT / "source"), str(tmp_repo)], check=True)
        subprocess.run(["git", "init"], cwd=tmp_repo, check=True, capture_output=True)
        subprocess.run(["git", "add", "-A"], cwd=tmp_repo, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "base"], cwd=tmp_repo, check=True, capture_output=True)
        return td, tmp_repo

    def test_hardgate_rejects_candidate_added_test_file(self):
        """Hardgate must fail with cheat_test_file_submitted when candidate introduces a new test file."""
        td, tmp_repo = self._create_real_git_repo()
        try:
            new_test = tmp_repo / "torrent" / "foo_test.go"
            new_test.write_text("package torrent\n", encoding="utf-8")
            subprocess.run(["git", "add", "torrent/foo_test.go"], cwd=tmp_repo, check=True)
            subprocess.run(["git", "commit", "-m", "add test"], cwd=tmp_repo, check=True, capture_output=True)

            passed, failed_nodes, details = self.check_anti_cheat(tmp_repo, self.config, self.verifier_dir)
            self.assertFalse(passed, "Hardgate must not pass when candidate submits a new test file")
            self.assertTrue(any("cheat_test_file_submitted: torrent/foo_test.go" in f for f in failed_nodes))
            self.assertIn("torrent/foo_test.go", details.get("submitted_test_files", []))
        finally:
            td.cleanup()

    def test_hardgate_rejects_candidate_modified_original_test_file(self):
        """Hardgate must fail with cheat_original_test_modified when candidate modifies an existing test file (even whitespace)."""
        td, tmp_repo = self._create_real_git_repo()
        try:
            target = tmp_repo / "torrent" / "session_add_test.go"
            target.write_text(target.read_text(encoding="utf-8") + "\n// harmless comment\n", encoding="utf-8")
            subprocess.run(["git", "commit", "-am", "modify test"], cwd=tmp_repo, check=True, capture_output=True)

            passed, failed_nodes, details = self.check_anti_cheat(tmp_repo, self.config, self.verifier_dir)
            self.assertFalse(passed, "Hardgate must not pass when candidate modifies an original test file")
            self.assertTrue(any("cheat_original_test_modified: torrent/session_add_test.go" in f for f in failed_nodes))
            self.assertIn("torrent/session_add_test.go", details.get("original_tests_tampered", []))
        finally:
            td.cleanup()

    def test_hardgate_rejects_candidate_deleted_test_file(self):
        """Hardgate must fail with cheat_original_test_modified when candidate deletes an existing test file."""
        td, tmp_repo = self._create_real_git_repo()
        try:
            subprocess.run(["git", "rm", "torrent/session_add_test.go"], cwd=tmp_repo, check=True, capture_output=True)
            subprocess.run(["git", "commit", "-m", "delete test"], cwd=tmp_repo, check=True, capture_output=True)

            passed, failed_nodes, details = self.check_anti_cheat(tmp_repo, self.config, self.verifier_dir)
            self.assertFalse(passed, "Hardgate must not pass when candidate deletes an original test file")
            self.assertTrue(any("cheat_original_test_modified: torrent/session_add_test.go" in f for f in failed_nodes))
        finally:
            td.cleanup()

    def test_hardgate_rejects_candidate_renamed_test_file(self):
        """Hardgate must fail when candidate renames an existing test file, checking both old and new paths."""
        td, tmp_repo = self._create_real_git_repo()
        try:
            subprocess.run(["git", "mv", "torrent/session_add_test.go", "torrent/renamed_test.go"], cwd=tmp_repo, check=True, capture_output=True)
            subprocess.run(["git", "commit", "-m", "rename test"], cwd=tmp_repo, check=True, capture_output=True)

            passed, failed_nodes, details = self.check_anti_cheat(tmp_repo, self.config, self.verifier_dir)
            self.assertFalse(passed, "Hardgate must not pass when candidate renames an original test file")
            self.assertTrue(any("cheat_original_test_modified: torrent/session_add_test.go" in f for f in failed_nodes))
            self.assertTrue(any("cheat_test_file_submitted: torrent/renamed_test.go" in f for f in failed_nodes))
        finally:
            td.cleanup()

    def test_hardgate_rejects_candidate_submitted_evaluator_test_file(self):
        """Candidate committing evaluator_session_lifecycle_test.go into HEAD or index must fail as cheat_test_file_submitted."""
        td, tmp_repo = self._create_real_git_repo()
        try:
            eval_test = tmp_repo / "torrent" / "evaluator_session_lifecycle_test.go"
            eval_test.write_text("package torrent\n", encoding="utf-8")
            subprocess.run(["git", "add", "torrent/evaluator_session_lifecycle_test.go"], cwd=tmp_repo, check=True)
            subprocess.run(["git", "commit", "-m", "cheat commit"], cwd=tmp_repo, check=True, capture_output=True)

            passed, failed_nodes, details = self.check_anti_cheat(tmp_repo, self.config, self.verifier_dir)
            self.assertFalse(passed, "Candidate submitting evaluator test file in commit must fail")
            self.assertTrue(any("cheat_test_file_submitted: torrent/evaluator_session_lifecycle_test.go" in f for f in failed_nodes))
        finally:
            td.cleanup()


class TestRPCEvaluatorPrematureCloseValidation(unittest.TestCase):
    """Evaluator self-validation demonstrating that verifyServerSideWorkFinished
    strictly rejects a candidate whose Session.Close returns prematurely while session-owned
    work (such as in-flight RPC handlers holding port reservations) remains active.
    """

    def test_evaluator_rejects_premature_close_return(self):
        """Demonstrate that premature Session.Close return while session work is active fails the test."""
        repo_dir = REPO_ROOT / "source"
        if not repo_dir.exists():
            repo_dir = HERE.parent / "isolated_repo"

        with tempfile.TemporaryDirectory() as td:
            tmp_repo = Path(td) / "repo"
            # Copy source to tmp_repo
            subprocess.run(["cp", "-R", str(repo_dir), str(tmp_repo)], check=True)
            subprocess.run(["git", "-C", str(tmp_repo), "init"], check=True, capture_output=True)
            subprocess.run(["git", "-C", str(tmp_repo), "add", "-A"], check=True, capture_output=True)
            solution_patch = (HERE.parent / "solution" / "solution.patch").resolve()
            test_patch = (VERIFIER_DIR / "test.patch").resolve()
            chk = subprocess.run(["git", "-C", str(tmp_repo), "apply", "--check", str(solution_patch)], capture_output=True)
            if chk.returncode == 0:
                subprocess.run(["git", "-C", str(tmp_repo), "apply", "--whitespace=nowarn", str(solution_patch)], check=True)
            subprocess.run(["git", "-C", str(tmp_repo), "apply", "--whitespace=nowarn", str(test_patch)], check=True)

            # 1. Unmutated reference solution passes
            pass_proc = subprocess.run(
                ["go", "test", "-count=1", "-v", "-run", "TestEvaluator_B8_Session_RPCShutdown_EnforcesDeadlineAndReleasesPort", "./torrent"],
                cwd=str(tmp_repo),
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertEqual(pass_proc.returncode, 0, f"Unmutated test must pass: {pass_proc.stderr}")

            # 2. Mutate Session.Close to return prematurely while in-flight handler work is still active
            session_go = tmp_repo / "torrent" / "session.go"
            content = session_go.read_text(encoding="utf-8")
            mutated_content = content.replace(
                "func (s *Session) Close() error {",
                "func (s *Session) Close() error { return nil // MUTATION_PREMATURE_CLOSE",
            )
            self.assertNotEqual(content, mutated_content)
            session_go.write_text(mutated_content, encoding="utf-8")

            # 3. Mutated candidate must FAIL with premature Close rejection
            fail_proc = subprocess.run(
                ["go", "test", "-count=1", "-v", "-run", "TestEvaluator_B8_Session_RPCShutdown_EnforcesDeadlineAndReleasesPort", "./torrent"],
                cwd=str(tmp_repo),
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertNotEqual(fail_proc.returncode, 0, "Mutated premature Close must fail evaluation")


class TestTimingAssertionTighteningCounterExamples(unittest.TestCase):
    """Verifies that implementations exceeding the public deadlines or weakening the internal
    safety margin (e.g. 50ms mutant) are strictly rejected by the observable budget and deadline
    assertions in test.patch, while unmutated reference solution cleanly passes."""

    def _setup_candidate_repo(self):
        td = tempfile.TemporaryDirectory()
        tmp_repo = Path(td.name) / "repo"
        subprocess.run(["cp", "-R", str(REPO_ROOT / "source"), str(tmp_repo)], check=True)
        subprocess.run(["git", "init"], cwd=tmp_repo, check=True, capture_output=True)
        subprocess.run(["git", "add", "-A"], cwd=tmp_repo, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "base"], cwd=tmp_repo, check=True, capture_output=True)
        solution_patch = (HERE.parent / "solution" / "solution.patch").resolve()
        test_patch = (VERIFIER_DIR / "test.patch").resolve()
        subprocess.run(["git", "-C", str(tmp_repo), "apply", str(solution_patch)], check=True)
        subprocess.run(["git", "-C", str(tmp_repo), "apply", str(test_patch)], check=True)
        return td, tmp_repo

    def test_reference_solution_passes_all_safety_margin_and_timing_assertions(self):
        """Unmutated reference solution satisfies all internal 100ms safety margin and timing bounds."""
        td, tmp_repo = self._setup_candidate_repo()
        try:
            proc = subprocess.run(
                ["go", "test", "-v", "-run", "^TestEvaluator_B(8|11|13|14)_", "./torrent"],
                cwd=str(tmp_repo),
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertEqual(proc.returncode, 0, f"Unmutated solution must pass B8, B11, B13, B14: {proc.stdout}")
        finally:
            td.cleanup()

    def test_internal_safety_margin_weakened_to_50ms_rejected(self):
        """When candidate implementation weakens internal safety margin from 100ms to 50ms
        (e.g. 4950ms instead of 4900ms, timeout+200ms instead of timeout+150ms),
        the observable boundary assertions strictly reject the candidate."""
        td, tmp_repo = self._setup_candidate_repo()
        try:
            session_go = tmp_repo / "torrent" / "session.go"
            content = session_go.read_text(encoding="utf-8")
            mutated = content.replace("4900 * time.Millisecond", "4950 * time.Millisecond")
            mutated = mutated.replace("150*time.Millisecond", "200*time.Millisecond")
            mutated = mutated.replace("4900*time.Millisecond", "4950*time.Millisecond")
            self.assertNotEqual(content, mutated)
            session_go.write_text(mutated, encoding="utf-8")

            proc = subprocess.run(
                ["go", "test", "-v", "-run", "^TestEvaluator_B(8|11|13|14)_", "./torrent"],
                cwd=str(tmp_repo),
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertNotEqual(proc.returncode, 0, "50ms mutant must fail B8/B11/B13/B14 assertions")
            failed = [l for l in proc.stdout.splitlines() if "--- FAIL:" in l]
            self.assertGreater(len(failed), 0, "At least one test must fail for 50ms mutant")
        finally:
            td.cleanup()

    def test_non_positive_rpc_timeout_counter_example(self):
        """When candidate silently falls back instead of returning an error for RPCShutdownTimeout <= 0,
        the test fails cleanly without emitting unregistered subtests or causing execution abnormality."""
        td, tmp_repo = self._setup_candidate_repo()
        try:
            session_go = tmp_repo / "torrent" / "session.go"
            content = session_go.read_text(encoding="utf-8")
            target = "\tif cfg.RPCEnabled && cfg.RPCShutdownTimeout <= 0 {\n\t\treturn nil, errors.New(\"torrent: RPCShutdownTimeout must be positive when RPC is enabled\")\n\t}"
            self.assertIn(target, content)
            mutated = content.replace(target, "\t// validation removed for mutation")
            session_go.write_text(mutated, encoding="utf-8")

            proc = subprocess.run(
                ["go", "test", "-json", "-run", "^TestEvaluator_Session_RPCShutdownTimeoutNonPositiveRejected$", "./torrent"],
                cwd=str(tmp_repo),
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertNotEqual(proc.returncode, 0, "Fallback mutant must fail the test")

            events = [json.loads(line) for line in proc.stdout.splitlines() if line.strip() and line.startswith("{")]
            test_names = {e.get("Test") for e in events if e.get("Test")}
            for name in test_names:
                self.assertNotIn("/zero", name, "No subtests like /zero should be emitted")
                self.assertNotIn("/negative", name, "No subtests like /negative should be emitted")
        finally:
            td.cleanup()

    def test_secretly_extended_execution_deadline_mutant_fails(self):
        """When candidate reports correct theoretical budgets and deadlines but secretly extends
        the execution deadline passed to timers (e.g. callerDeadline and rpcDeadline +50ms),
        the execution timer observation hook strictly detects and rejects the extension."""
        td, tmp_repo = self._setup_candidate_repo()
        try:
            session_go = tmp_repo / "torrent" / "session.go"
            content = session_go.read_text(encoding="utf-8")
            target = """callerDeadline := start.Add(totalBudget)
	var rpcDeadline time.Time
	if rpcBudget > 0 {
		rpcDeadline = start.Add(rpcBudget)
	}"""
            mutant_b = """callerDeadline := start.Add(totalBudget + 50*time.Millisecond)
	var rpcDeadline time.Time
	if rpcBudget > 0 {
		rpcDeadline = start.Add(rpcBudget + 50*time.Millisecond)
	}"""
            self.assertIn(target, content)
            mutated = content.replace(target, mutant_b, 1)
            session_go.write_text(mutated, encoding="utf-8")

            proc = subprocess.run(
                ["go", "test", "-v", "-run", "^TestEvaluator_B(8|11|13|14)_", "./torrent"],
                cwd=str(tmp_repo),
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertNotEqual(proc.returncode, 0, "Mutant B (+50ms execution deadline) must fail evaluation")
            output = proc.stdout
            self.assertTrue(
                "actual execution timer for 'total' phase must match totalBudget" in output
                or "actual execution timer for 'rpc' phase must match rpcBudget" in output,
                f"Failure output must specifically identify phase execution timer discrepancy: {output}",
            )
        finally:
            td.cleanup()

    def test_premature_database_close_mutant_fails_b13(self):
        """When candidate prematurely closes BoltDB upon Close() timeout while RPC handlers are still active,
        TestEvaluator_B13 strictly fails on lock retention (Check 1) and handler DB access (Check 2)."""
        td, tmp_repo = self._setup_candidate_repo()
        try:
            session_go = tmp_repo / "torrent" / "session.go"
            content = session_go.read_text(encoding="utf-8")
            target = """if rpcErr != nil {
			s.log.Errorln("cannot stop RPC server:", rpcErr.Error())
		}"""
            mutant_db = """if rpcErr != nil {
			s.log.Errorln("cannot stop RPC server:", rpcErr.Error())
			_ = s.db.Close() // MUTANT_PREMATURE_DB_CLOSE
		}"""
            self.assertIn(target, content)
            mutated = content.replace(target, mutant_db, 1)
            session_go.write_text(mutated, encoding="utf-8")

            proc = subprocess.run(
                ["go", "test", "-v", "-run", "^TestEvaluator_B13_", "./torrent"],
                cwd=str(tmp_repo),
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertNotEqual(proc.returncode, 0, "Premature DB close mutant must fail B13")
            output = proc.stdout
            self.assertTrue(
                "BoltDB must remain locked while RPC handler is active after Close timeout" in output
                or "database not open" in output,
                f"Failure output must specifically identify premature DB closure: {output}",
            )
        finally:
            td.cleanup()

    def test_deleted_set_shutdown_timer_mutant_fails(self):
        """When candidate deletes Session.setShutdownTimer to evade timer duration assertions,
        tests B8, B11, B13, and B14 mandatorily assert the interface and fail immediately."""
        td, tmp_repo = self._setup_candidate_repo()
        try:
            session_go = tmp_repo / "torrent" / "session.go"
            content = session_go.read_text(encoding="utf-8")
            method_str = """func (s *Session) setShutdownTimer(fn func(phase string, d time.Duration) (<-chan time.Time, func() bool)) {
	if s == nil || s.shutdown == nil {
		return
	}
	s.shutdown.mu.Lock()
	defer s.shutdown.mu.Unlock()
	s.shutdown.timerFn = fn
}"""
            self.assertIn(method_str, content)
            mutated = content.replace(method_str, "// setShutdownTimer removed to attempt evasion")
            timer_target = 'timerC, stopTimer := sc.newTimer("total", rem)'
            timer_mutant = 'timerC, stopTimer := sc.newTimer("total", rem + 50*time.Millisecond)'
            self.assertIn(timer_target, mutated)
            mutated = mutated.replace(timer_target, timer_mutant)
            session_go.write_text(mutated, encoding="utf-8")

            proc = subprocess.run(
                ["go", "test", "-v", "-run", "^TestEvaluator_B(8|11|13|14)_", "./torrent"],
                cwd=str(tmp_repo),
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertNotEqual(proc.returncode, 0, "Mutant without setShutdownTimer must fail evaluation")
            output = proc.stdout
            self.assertIn("Session must implement setShutdownTimer", output)
        finally:
            td.cleanup()

    def test_renamed_worker_helper_passes_b15(self):
        """When candidate refactors worker management using an alternative internal helper name
        (e.g., launchSessionWorker instead of startWorker), TestEvaluator_B15 passes cleanly without
        failing on any private method reflection."""
        td, tmp_repo = self._setup_candidate_repo()
        try:
            for p in tmp_repo.glob("torrent/*.go"):
                txt = p.read_text(encoding="utf-8")
                if "startWorker" in txt:
                    p.write_text(txt.replace("startWorker", "launchSessionWorker"), encoding="utf-8")

            proc = subprocess.run(
                ["go", "test", "-v", "-run", "^TestEvaluator_B15_Session_WorkerCompletionBoundary$", "./torrent"],
                cwd=str(tmp_repo),
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertEqual(proc.returncode, 0, f"B15 must pass with renamed worker helper: {proc.stdout}")
        finally:
            td.cleanup()

    def test_discarded_timer_channel_mutant_fails_b8(self):
        """When candidate reports correct theoretical timer durations via setShutdownTimer but discards
        the injected channel and uses an independent uncoordinated timer, TestEvaluator_B8 detects that
        execution is not driven by the injected channel and strictly fails."""
        td, tmp_repo = self._setup_candidate_repo()
        try:
            session_go = tmp_repo / "torrent" / "session.go"
            content = session_go.read_text(encoding="utf-8")
            target = "ch, stop := fn(phase, d)"
            self.assertIn(target, content)
            mutated = content.replace(
                target,
                "_, _ = fn(phase, d)\n\t\tt := time.NewTimer(d)\n\t\tch, stop := t.C, t.Stop",
                1,
            )
            session_go.write_text(mutated, encoding="utf-8")

            proc = subprocess.run(
                ["go", "test", "-v", "-run", "^TestEvaluator_B8_Session_RPCShutdown_EnforcesDeadlineAndReleasesPort$", "./torrent"],
                cwd=str(tmp_repo),
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertNotEqual(proc.returncode, 0, "Mutant discarding injected timer channel must fail B8")
            output = proc.stdout
            self.assertIn("Close was not driven by injected timer channel", output)
        finally:
            td.cleanup()


class TestGradingContractMatrix(unittest.TestCase):
    """Exhaustive verification of all review grading contract branches:
    1. Valid candidate, clean pass (all P2P and all F2P pass) -> reward = 1.0, evaluation_success = True
    2. Valid candidate, single P2P failure -> reward = 0.0
    3. Valid candidate, multiple P2P failures -> reward = 0.0
    4. Valid candidate, all P2P pass, single F2P failure -> reward = actual pass ratio (11/12)
    5. Valid candidate, all P2P pass, all F2P fail -> reward = 0.0
    6. Illegitimate candidate (apply_failed or build or anti_cheat failure) -> reward = -1.0
    7. Report protocol violation: unexpected extra node -> reward = -2.0
    8. Report protocol violation: missing node -> reward = -2.0
    9. Report protocol violation: duplicate node -> reward = -2.0
    10. Report protocol violation: unknown status enum -> reward = -2.0
    11. Report protocol violation: malformed report -> reward = -2.0
    12. Runner non-zero exit / execution crash -> reward = -2.0
    13. F2P failure accompanied by execution abnormality -> reward = -2.0
    """

    @classmethod
    def setUpClass(cls):
        cls.config = json.loads(CONFIG_PATH.read_text())
        cls.fixed_grader_py = HERE.parent / "authoring" / "platform_grader_fixed.py"

    def _run_fixed_pipeline(self, config_data, ctrf_data, hard_gate_data, apply_failed=0):
        with tempfile.TemporaryDirectory() as td:
            tdp = Path(td)
            cfg_file = tdp / "config.json"
            ctrf_file = tdp / "ctrf.json"
            hg_file = tdp / "hard_gate.json"
            gate_out = tdp / "gate.json"
            reward_out = tdp / "reward.json"
            reward_details_out = tdp / "reward_details.json"

            cfg_copy = copy.deepcopy(config_data)
            cfg_copy.setdefault("reports", {})["reward"] = str(reward_out)
            cfg_copy["reports"]["reward_details"] = str(reward_details_out)

            cfg_file.write_text(json.dumps(cfg_copy))
            ctrf_file.write_text(json.dumps(ctrf_data))
            hg_file.write_text(json.dumps(hard_gate_data))

            gate_proc = subprocess.run(
                [
                    sys.executable,
                    str(self.fixed_grader_py),
                    "gate",
                    "--config", str(cfg_file),
                    "--ctrf", str(ctrf_file),
                    "--hard-gate", str(hg_file),
                    "--output", str(gate_out),
                    "--apply-failed", str(apply_failed),
                ],
                capture_output=True,
                text=True,
            )
            if gate_proc.returncode != 0:
                # Protocol violation / error in gate triggers infrastructure error (-2)
                return None, {"reward": -2.0, "status": "INFRA_ERROR", "stderr": gate_proc.stderr}

            gate_res = json.loads(gate_out.read_text())

            fin_proc = subprocess.run(
                [
                    sys.executable,
                    str(self.fixed_grader_py),
                    "finalize",
                    "--config", str(cfg_file),
                    "--gate", str(gate_out),
                ],
                capture_output=True,
                text=True,
            )
            if fin_proc.returncode != 0:
                return gate_res, {"reward": -2.0, "status": "INFRA_ERROR", "stderr": fin_proc.stderr}

            reward_res = json.loads(reward_out.read_text())
            details_res = json.loads(reward_details_out.read_text())
            reward_res["details"] = details_res
            return gate_res, reward_res

    def test_1_clean_pass_reward_1(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertIsNotNone(gate_res)
        self.assertEqual(reward_res["reward"], 1.0)
        self.assertTrue(reward_res["details"]["evaluation_success"])

    def test_2_single_p2p_failure_reward_0(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        # Mark 1 P2P node failed
        failing_node = self.config["p2p"][0]
        ctrf["results"]["tests"][0]["status"] = "failed"
        hg = {"passed": False, "failed_nodes": [failing_node], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": False}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertIsNotNone(gate_res)
        self.assertEqual(reward_res["reward"], 0.0, "Legitimate candidate with P2P failure must receive 0.0")
        self.assertFalse(reward_res["details"]["evaluation_success"])

    def test_3_multiple_p2p_failures_reward_0(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        failing_nodes = self.config["p2p"][:5]
        for i in range(5):
            ctrf["results"]["tests"][i]["status"] = "failed"
        hg = {"passed": False, "failed_nodes": failing_nodes, "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": False}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertIsNotNone(gate_res)
        self.assertEqual(reward_res["reward"], 0.0, "Legitimate candidate with multi P2P failures must receive 0.0")

    def test_4_single_f2p_failure_reward_pass_ratio(self):
        failing_f2p = self.config["f2p"][0]
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True, failing_f2p_node=failing_f2p)
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertIsNotNone(gate_res)
        expected_ratio = (len(self.config["f2p"]) - 1) / len(self.config["f2p"])
        self.assertAlmostEqual(reward_res["reward"], expected_ratio, places=5)
        self.assertFalse(reward_res["details"]["evaluation_success"])

    def test_5_candidate_patch_apply_failed_reward_minus_1(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        hg = {
            "passed": False,
            "apply_failed": True,
            "failed_nodes": [],
            "categories": {
                "build": {"passed": False},
                "anti_cheat": {"passed": True},
                "p2p": {"passed": False},
            },
        }
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg, apply_failed=1)
        self.assertEqual(reward_res["reward"], -1.0)

    def test_6_build_vet_anticheat_failed_reward_minus_1(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        # 6a. Build / vet failed
        hg_build = {
            "passed": False,
            "failed_nodes": [],
            "categories": {
                "build": {"passed": False},
                "anti_cheat": {"passed": True},
                "p2p": {"passed": False},
            },
        }
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg_build)
        self.assertEqual(reward_res["reward"], -1.0)

        # 6b. Anti-cheat failed
        hg_cheat = {
            "passed": False,
            "failed_nodes": [],
            "categories": {
                "build": {"passed": True},
                "anti_cheat": {"passed": False},
                "p2p": {"passed": False},
            },
        }
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg_cheat)
        self.assertEqual(reward_res["reward"], -1.0)

    def test_7_extra_undeclared_node_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        ctrf["results"]["tests"].append({
            "name": "extra/node_test.go::TestExtra",
            "testId": "extra/node_test.go::TestExtra",
            "status": "passed",
            "extra": {"deepswe": {"group": "P2P", "required": True}},
        })
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_8_missing_node_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        ctrf["results"]["tests"].pop()
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_9_duplicate_node_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        ctrf["results"]["tests"].append(copy.deepcopy(ctrf["results"]["tests"][0]))
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_10_unknown_status_enum_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        ctrf["results"]["tests"][0]["status"] = "unknown_status_enum"
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_11_skipped_pending_other_status_reward_minus_2(self):
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        for bad_status in ("skipped", "pending", "other"):
            ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
            ctrf["results"]["tests"][0]["status"] = bad_status
            gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
            self.assertEqual(reward_res["reward"], -2.0, f"Status {bad_status} must yield reward -2.0")

    def test_12_malformed_ctrf_reward_minus_2(self):
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        for malformed in ({"results": "not_a_dict"}, {"results": {"tests": "not_a_list"}}, "not_a_dict"):
            gate_res, reward_res = self._run_fixed_pipeline(self.config, malformed, hg)
            self.assertEqual(reward_res["reward"], -2.0)

    def test_13_malformed_hard_gate_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        # Empty dict, missing categories, contradiction
        for bad_hg in (
            {},
            {"passed": True},
            {"passed": True, "categories": {}},
            {"passed": True, "categories": {"build": {"passed": False}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}},
        ):
            gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, bad_hg)
            self.assertEqual(reward_res["reward"], -2.0)

    def test_14_runner_timeout_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        hg = {
            "passed": False,
            "failed_nodes": ["p2p_timeout: go test execution timed out after 300s"],
            "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": False}},
        }
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_15_unregistered_failure_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        ctrf["results"]["extra"]["deepswe"]["unregistered_failures"] = ["github.com/cenkalti/rain/v2/torrent::TestMystery"]
        ctrf["results"]["extra"]["deepswe"]["execution_abnormality"] = True
        hg = {"passed": False, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_16_abnormal_package_failure_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        ctrf["results"]["extra"]["deepswe"]["abnormal_package_failures"] = ["github.com/cenkalti/rain/v2/torrent"]
        ctrf["results"]["extra"]["deepswe"]["execution_abnormality"] = True
        hg = {"passed": False, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_17_incomplete_execution_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        ctrf["results"]["extra"]["deepswe"]["incomplete_nodes"] = ["github.com/cenkalti/rain/v2/torrent::TestIncomplete"]
        ctrf["results"]["extra"]["deepswe"]["execution_abnormality"] = True
        hg = {"passed": False, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_18_exit_code_1_with_registered_p2p_failure_reward_0(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        failing_node = self.config["p2p"][0]
        for t in ctrf["results"]["tests"]:
            if t["testId"] == failing_node:
                t["status"] = "failed"
        ctrf["results"]["extra"]["deepswe"]["cmd_returncode"] = 1
        ctrf["results"]["extra"]["deepswe"]["cmd_failed"] = True
        ctrf["results"]["extra"]["deepswe"]["is_unexplained_process"] = False
        ctrf["results"]["extra"]["deepswe"]["execution_abnormality"] = False
        hg = {
            "passed": False,
            "failed_nodes": [failing_node, "p2p_process_failure (exit code 1)"],
            "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": False}},
        }
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertEqual(reward_res["reward"], 0.0, "Ordinary exit code 1 with registered P2P failure must yield reward 0.0")

    def test_19_hard_gate_missing_or_invalid_passed_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        # Missing passed
        hg_missing = {"failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg_missing)
        self.assertEqual(reward_res["reward"], -2.0)

        # Non-boolean passed
        hg_non_bool = {"passed": "true", "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg_non_bool)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_20_hard_gate_p2p_category_contradicts_ctrf_reward_minus_2(self):
        # Case A: Hard-gate says P2P failed, but CTRF says all P2P passed
        ctrf_all_pass = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        hg_p2p_failed = {
            "passed": False,
            "failed_nodes": [self.config["p2p"][0]],
            "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": False}},
        }
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf_all_pass, hg_p2p_failed)
        self.assertEqual(reward_res["reward"], -2.0)
        self.assertIn("Contradiction between hard-gate and CTRF", reward_res["details"].get("skip_reason", ""))

        # Case B: Hard-gate says P2P passed, but CTRF says a P2P node failed
        ctrf_p2p_failed = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        for t in ctrf_p2p_failed["results"]["tests"]:
            if t["testId"] == self.config["p2p"][0]:
                t["status"] = "failed"
        hg_p2p_passed = {
            "passed": True,
            "failed_nodes": [],
            "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}},
        }
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf_p2p_failed, hg_p2p_passed)
        self.assertEqual(reward_res["reward"], -2.0)
        self.assertIn("Contradiction between hard-gate and CTRF", reward_res["details"].get("skip_reason", ""))

    def test_21_hard_gate_failed_nodes_contains_non_string_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        for bad_item in (123, None, {"node": "test"}, [1]):
            hg = {
                "passed": False,
                "failed_nodes": [bad_item],
                "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": False}},
            }
            gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
            self.assertEqual(reward_res["reward"], -2.0, f"failed_nodes containing {bad_item!r} must yield reward -2.0")

    def test_22_empty_or_duplicate_config_nodes_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}

        # 22a. Empty F2P list
        cfg_empty_f2p = copy.deepcopy(self.config)
        cfg_empty_f2p["f2p"] = []
        gate_res, reward_res = self._run_fixed_pipeline(cfg_empty_f2p, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

        # 22b. Empty string node
        cfg_blank_node = copy.deepcopy(self.config)
        cfg_blank_node["f2p"].append("   ")
        gate_res, reward_res = self._run_fixed_pipeline(cfg_blank_node, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

        # 22c. Duplicate P2P node in config
        cfg_dup_p2p = copy.deepcopy(self.config)
        cfg_dup_p2p["p2p"].append(cfg_dup_p2p["p2p"][0])
        gate_res, reward_res = self._run_fixed_pipeline(cfg_dup_p2p, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

        # 22d. Overlap between F2P and P2P in config
        cfg_overlap = copy.deepcopy(self.config)
        cfg_overlap["f2p"].append(cfg_overlap["p2p"][0])
        gate_res, reward_res = self._run_fixed_pipeline(cfg_overlap, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_23_ctrf_empty_test_id_or_wrong_group_reward_minus_2(self):
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}

        # Empty testId
        ctrf_empty_id = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        ctrf_empty_id["results"]["tests"][0]["testId"] = ""
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf_empty_id, hg)
        self.assertEqual(reward_res["reward"], -2.0)

        # Wrong group
        ctrf_wrong_group = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        ctrf_wrong_group["results"]["tests"][0]["extra"]["deepswe"]["group"] = "WRONG_GROUP"
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf_wrong_group, hg)
        self.assertEqual(reward_res["reward"], -2.0)

        # Missing required flag
        ctrf_no_req = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        ctrf_no_req["results"]["tests"][0]["extra"]["deepswe"]["required"] = False
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf_no_req, hg)
        self.assertEqual(reward_res["reward"], -2.0)

    def test_24_ctrf_summary_skipped_pending_reward_minus_2(self):
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        for bad_key in ("skipped", "pending", "other"):
            ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
            ctrf["results"]["summary"][bad_key] = 1
            gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
            self.assertEqual(reward_res["reward"], -2.0)

    def test_25_hard_gate_missing_failed_nodes_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        hg = {"passed": True, "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
        self.assertEqual(reward_res["reward"], -2.0)
        self.assertIn("missing explicit failed_nodes", reward_res["details"].get("skip_reason", ""))

    def test_26_hard_gate_failed_nodes_contains_empty_or_whitespace_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        for bad_fn in ("", "   ", "\t\n"):
            hg = {
                "passed": False,
                "failed_nodes": [bad_fn],
                "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": False}},
            }
            gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
            self.assertEqual(reward_res["reward"], -2.0)

    def test_27_hard_gate_boolean_fields_invalid_type_reward_minus_2(self):
        ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
        bad_bool_cases = [
            {"infra_error": "false"},
            {"apply_failed": 1},
            {"execution_passed": "true"},
            {"build_passed": 0},
            {"anti_cheat_passed": "false"},
            {"p2p_passed": "true"},
        ]
        for extra_field in bad_bool_cases:
            hg = {
                "passed": True,
                "failed_nodes": [],
                "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}},
                **extra_field,
            }
            gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
            self.assertEqual(reward_res["reward"], -2.0, f"Field {extra_field} must yield -2.0")

    def test_28_ctrf_summary_negative_or_non_integer_reward_minus_2(self):
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        for bad_summary in [
            {"passed": -1},
            {"tests": "251"},
            {"failed": 1.5},
            {"skipped": True},
        ]:
            ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
            ctrf["results"]["summary"].update(bad_summary)
            gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
            self.assertEqual(reward_res["reward"], -2.0, f"Bad summary {bad_summary} must yield -2.0")

    def test_29_ctrf_extra_deepswe_invalid_types_reward_minus_2(self):
        hg = {"passed": True, "failed_nodes": [], "categories": {"build": {"passed": True}, "anti_cheat": {"passed": True}, "p2p": {"passed": True}}}
        bad_cases = [
            {"execution_abnormality": "false"},
            {"is_unexplained_process": 1},
            {"runner_timeout": "true"},
            {"unregistered_failures": "not_a_list"},
            {"abnormal_package_failures": 123},
            {"incomplete_nodes": False},
        ]
        for bad in bad_cases:
            ctrf = make_base_ctrf(self.config, pass_p2p=True, pass_f2p=True)
            ctrf["results"]["extra"]["deepswe"].update(bad)
            gate_res, reward_res = self._run_fixed_pipeline(self.config, ctrf, hg)
            self.assertEqual(reward_res["reward"], -2.0, f"Bad extra deepswe {bad} must yield -2.0")


if __name__ == "__main__":
    unittest.main()




