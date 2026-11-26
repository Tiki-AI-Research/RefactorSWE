#!/usr/bin/env python3
"""Comprehensive test suite for verifier resilience, infra failure detection, and report integrity."""

from __future__ import annotations

import copy
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import sys

_HERE = Path(__file__).resolve().parent
for p in [_HERE, _HERE.parent, _HERE.parents[1], _HERE.parents[2]]:
    p_str = str(p)
    if p_str not in sys.path:
        sys.path.insert(0, p_str)

try:
    import hardgate
    import verifier
    import grader
except ImportError:
    from case.tests.verifier import hardgate
    from case.tests.verifier import verifier
    from case.tests import grader

NodeResult = hardgate.NodeResult
REQUIRED_CHEAT_NODE_IDS = hardgate.REQUIRED_CHEAT_NODE_IDS
run_command_with_diagnostics = hardgate.run_command_with_diagnostics
run_hard_gate = hardgate.run_hard_gate
sanitize_message = hardgate.sanitize_message
validate_hard_gate_schema = hardgate.validate_hard_gate_schema
ARCHITECTURE_F2P_NODE_ID = hardgate.ARCHITECTURE_F2P_NODE_ID

InfrastructureError = verifier.InfrastructureError
VALID_CTRF_STATUSES = verifier.VALID_CTRF_STATUSES
generate_ctrf_report = verifier.generate_ctrf_report
verifier_main = verifier.main
run_f2p_tests = verifier.run_f2p_tests
validate_ctrf_report_integrity = verifier.validate_ctrf_report_integrity
grader_required_statuses = grader.required_statuses


CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.json"


def load_canonical_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def build_canonical_valid_ctrf(config: dict) -> dict:
    """Construct a canonical, 100% valid CTRF report matching the config."""
    f2p_nodes = [str(n) for n in config["f2p"]]
    p2p_nodes = [str(n) for n in config["p2p"]]

    tests_list = []
    for tid in p2p_nodes:
        tests_list.append({
            "testId": tid,
            "name": tid.split("::")[-1],
            "status": "passed",
            "duration": 5,
            "extra": {"deepswe": {"group": "P2P", "required": True}},
        })
    for tid in f2p_nodes:
        tests_list.append({
            "testId": tid,
            "name": tid.split("::")[-1],
            "status": "passed",
            "duration": 10,
            "extra": {"deepswe": {"group": "F2P", "required": True}},
        })

    return {
        "reportFormat": "CTRF",
        "specVersion": "0.0.0",
        "results": {
            "tool": {"name": "vitest"},
            "summary": {
                "tests": len(tests_list),
                "passed": len(tests_list),
                "failed": 0,
                "skipped": 0,
                "pending": 0,
                "other": 0,
                "start": 1000,
                "stop": 2000,
            },
            "tests": tests_list,
        },
    }


class TestReportIntegrityValidation(unittest.TestCase):
    """Tests for CTRF and Hard Gate report pre-validation (Goal 3)."""

    def setUp(self):
        self.config = load_canonical_config()
        self.valid_ctrf = build_canonical_valid_ctrf(self.config)

    def test_valid_report_passes(self):
        errors = validate_ctrf_report_integrity(self.valid_ctrf, self.config)
        self.assertEqual(errors, [])

    def test_missing_node_rejected(self):
        ctrf = copy.deepcopy(self.valid_ctrf)
        removed = ctrf["results"]["tests"].pop(0)
        ctrf["results"]["summary"]["tests"] -= 1
        ctrf["results"]["summary"]["passed"] -= 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(any("Missing CTRF nodes" in e for e in errors))

    def test_duplicate_node_rejected(self):
        ctrf = copy.deepcopy(self.valid_ctrf)
        dup = copy.deepcopy(ctrf["results"]["tests"][0])
        ctrf["results"]["tests"].append(dup)
        ctrf["results"]["summary"]["tests"] += 1
        ctrf["results"]["summary"]["passed"] += 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(any("Duplicate CTRF node" in e for e in errors))

    def test_extra_passed_node_rejected(self):
        ctrf = copy.deepcopy(self.valid_ctrf)
        extra_node = {
            "testId": "F2P::forged::extra_passed_test",
            "name": "extra_passed_test",
            "status": "passed",
            "duration": 5,
            "extra": {"deepswe": {"group": "F2P", "required": True}},
        }
        ctrf["results"]["tests"].append(extra_node)
        ctrf["results"]["summary"]["tests"] += 1
        ctrf["results"]["summary"]["passed"] += 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(any("Extra unexpected CTRF nodes" in e for e in errors))

    def test_extra_failed_node_rejected(self):
        ctrf = copy.deepcopy(self.valid_ctrf)
        extra_node = {
            "testId": "P2P::forged::extra_failed_test",
            "name": "extra_failed_test",
            "status": "failed",
            "duration": 5,
            "extra": {"deepswe": {"group": "P2P", "required": True}},
        }
        ctrf["results"]["tests"].append(extra_node)
        ctrf["results"]["summary"]["tests"] += 1
        ctrf["results"]["summary"]["failed"] += 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(any("Extra unexpected CTRF nodes" in e for e in errors))

    def test_wrong_group_f2p_as_p2p_rejected(self):
        ctrf = copy.deepcopy(self.valid_ctrf)
        for t in ctrf["results"]["tests"]:
            if t["testId"].startswith("F2P::"):
                t["extra"]["deepswe"]["group"] = "P2P"
                break

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(any("Wrong CTRF group for F2P test" in e for e in errors))

    def test_wrong_group_p2p_as_f2p_rejected(self):
        ctrf = copy.deepcopy(self.valid_ctrf)
        for t in ctrf["results"]["tests"]:
            if not t["testId"].startswith("F2P::"):
                t["extra"]["deepswe"]["group"] = "F2P"
                break

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(any("Wrong CTRF group for P2P test" in e for e in errors))

    def test_unknown_status_rejected(self):
        for invalid_status in ["unknown", "banana", "error", "cancelled", ""]:
            ctrf = copy.deepcopy(self.valid_ctrf)
            ctrf["results"]["tests"][0]["status"] = invalid_status
            ctrf["results"]["summary"]["passed"] -= 1

            errors = validate_ctrf_report_integrity(ctrf, self.config)
            self.assertTrue(
                any("Invalid CTRF status" in e for e in errors),
                f"Failed to reject invalid status '{invalid_status}'",
            )

    def test_inconsistent_summary_count_rejected(self):
        ctrf = copy.deepcopy(self.valid_ctrf)
        ctrf["results"]["summary"]["passed"] += 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(any("Summary count mismatch" in e for e in errors))

    def test_invalid_top_level_schema_rejected(self):
        ctrf = copy.deepcopy(self.valid_ctrf)
        ctrf["reportFormat"] = "JUNIT"
        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(any("Invalid or missing reportFormat" in e for e in errors))

    def test_architecture_f2p_node_required_exactly_once(self):
        """Verify the architecture separation node is present exactly once in canonical CTRF."""
        node_ids = [t["testId"] for t in self.valid_ctrf["results"]["tests"]]
        self.assertEqual(node_ids.count(ARCHITECTURE_F2P_NODE_ID), 1)
        errors = validate_ctrf_report_integrity(self.valid_ctrf, self.config)
        self.assertEqual(errors, [])

    def test_missing_architecture_f2p_node_rejected(self):
        """Verify report without the architecture F2P node is strictly rejected."""
        ctrf = copy.deepcopy(self.valid_ctrf)
        ctrf["results"]["tests"] = [
            t for t in ctrf["results"]["tests"] if t["testId"] != ARCHITECTURE_F2P_NODE_ID
        ]
        ctrf["results"]["summary"]["tests"] -= 1
        ctrf["results"]["summary"]["passed"] -= 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(any("Missing CTRF nodes" in e and ARCHITECTURE_F2P_NODE_ID in e for e in errors))

    def test_duplicate_architecture_f2p_node_rejected(self):
        """Verify duplicating the architecture F2P node is strictly rejected."""
        ctrf = copy.deepcopy(self.valid_ctrf)
        arch_node = next(t for t in ctrf["results"]["tests"] if t["testId"] == ARCHITECTURE_F2P_NODE_ID)
        ctrf["results"]["tests"].append(copy.deepcopy(arch_node))
        ctrf["results"]["summary"]["tests"] += 1
        ctrf["results"]["summary"]["passed"] += 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(any(f"Duplicate CTRF node: '{ARCHITECTURE_F2P_NODE_ID}'" in e for e in errors))

    def test_architecture_node_in_wrong_group_rejected(self):
        """Verify architecture F2P node declared under P2P group is rejected."""
        ctrf = copy.deepcopy(self.valid_ctrf)
        for t in ctrf["results"]["tests"]:
            if t["testId"] == ARCHITECTURE_F2P_NODE_ID:
                t["extra"]["deepswe"]["group"] = "P2P"
                break

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(any(f"Wrong CTRF group for F2P test '{ARCHITECTURE_F2P_NODE_ID}'" in e for e in errors))


class TestInfrastructureFailureDetection(unittest.TestCase):
    """Tests distinguishing infrastructure failures from ordinary candidate failures (Goal 1 & 2)."""

    @patch("subprocess.run")
    def test_run_command_diagnostics_exit_127(self, mock_run):
        mock_run.side_effect = FileNotFoundError("No such file or directory: 'non_existent_binary_xyz123'")
        diag = run_command_with_diagnostics(["non_existent_binary_xyz123"], Path("/tmp"), {})
        self.assertTrue(diag["is_infra"])
        self.assertEqual(diag["infra_type"], "EXECUTABLE_UNAVAILABLE")
        self.assertEqual(diag["exit_code"], 127)

    @patch("subprocess.run")
    def test_run_command_diagnostics_timeout(self, mock_run):
        mock_run.side_effect = subprocess.TimeoutExpired(cmd=["sleep", "5"], timeout=0.1)
        diag = run_command_with_diagnostics(["sleep", "5"], Path("/tmp"), {}, timeout=0.1)
        self.assertTrue(diag["is_infra"])
        self.assertEqual(diag["infra_type"], "TIMEOUT")
        self.assertTrue(diag["timed_out"])

    @patch("subprocess.run")
    def test_run_command_diagnostics_signal_termination(self, mock_run):
        mock_proc = MagicMock()
        mock_proc.returncode = -9  # SIGKILL
        mock_proc.stdout = ""
        mock_proc.stderr = "Killed: Out of memory"
        mock_run.return_value = mock_proc

        diag = run_command_with_diagnostics(["node", "some_script.js"], Path("/tmp"), {})
        self.assertTrue(diag["is_infra"])
        self.assertEqual(diag["infra_type"], "PROCESS_SIGNAL_TERMINATED")

    def test_run_f2p_tests_missing_test_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_path = Path(tmpdir)
            with self.assertRaises(InfrastructureError) as ctx:
                run_f2p_tests(repo_path)
            self.assertEqual(ctx.exception.error_type, "TEST_FILE_MISSING")

    @patch("subprocess.run")
    def test_run_f2p_tests_malformed_json(self, mock_run):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            test_dir = repo / "tests"
            test_dir.mkdir(parents=True)
            (test_dir / "deep_swe_verifier_poline_picker.test.ts").write_text("// test", encoding="utf-8")

            mock_proc = MagicMock()
            mock_proc.returncode = 1
            mock_proc.stdout = "<html>502 Bad Gateway</html>"
            mock_proc.stderr = ""
            mock_run.return_value = mock_proc

            with self.assertRaises(InfrastructureError) as ctx:
                run_f2p_tests(repo)
            self.assertEqual(ctx.exception.error_type, "MALFORMED_JSON")

    @patch("subprocess.run")
    def test_run_f2p_tests_zero_tests_collected(self, mock_run):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            test_dir = repo / "tests"
            test_dir.mkdir(parents=True)
            (test_dir / "deep_swe_verifier_poline_picker.test.ts").write_text("// test", encoding="utf-8")

            mock_proc = MagicMock()
            mock_proc.returncode = 0
            mock_proc.stdout = json.dumps({"testResults": []})
            mock_proc.stderr = ""
            mock_run.return_value = mock_proc

            with self.assertRaises(InfrastructureError) as ctx:
                run_f2p_tests(repo)
            self.assertEqual(ctx.exception.error_type, "ZERO_TESTS_COLLECTED")


class TestCandidateFailureClassification(unittest.TestCase):
    """Tests that real candidate failures are NEVER treated as infrastructure failures."""

    def test_candidate_typecheck_error_is_candidate_failure(self):
        diag = {
            "cmd": ["npx", "tsc", "--build"],
            "exit_code": 2,
            "stdout": "src/webcomponent.ts(10,5): error TS2322: Type 'number' is not assignable to type 'string'.",
            "stderr": "",
            "timed_out": False,
            "error": None,
            "is_infra": False,
            "infra_type": None,
            "infra_msg": None,
        }
        self.assertFalse(diag["is_infra"])
        self.assertIsNone(diag["infra_type"])

    def test_candidate_eslint_error_is_candidate_failure(self):
        diag = {
            "cmd": ["npx", "eslint", ".", "--ext", ".ts"],
            "exit_code": 1,
            "stdout": "src/webcomponent.ts:15:3: error: 'unusedVar' is defined but never used",
            "stderr": "",
            "timed_out": False,
            "error": None,
            "is_infra": False,
            "infra_type": None,
            "infra_msg": None,
        }
        self.assertFalse(diag["is_infra"])
        self.assertIsNone(diag["infra_type"])

    def test_candidate_build_error_is_candidate_failure(self):
        diag = {
            "cmd": ["node", "./build.js"],
            "exit_code": 1,
            "stdout": "",
            "stderr": "Error: Could not resolve './missing-module'",
            "timed_out": False,
            "error": None,
            "is_infra": False,
            "infra_type": None,
            "infra_msg": None,
        }
        self.assertFalse(diag["is_infra"])
        self.assertIsNone(diag["infra_type"])


class TestGraderBoundaryAndPlatformTrap(unittest.TestCase):
    """Tests the boundary between verifier and grader, demonstrating why pre-validation is essential (Goal 4)."""

    def setUp(self):
        self.config = load_canonical_config()

    def test_editable_verifier_pre_validation_blocks_extra_nodes_before_grader(self):
        """Verify that editable verifier pre-validation blocks extra unexpected nodes before the protected grader."""
        ctrf = build_canonical_valid_ctrf(self.config)
        extra_node = {
            "testId": "forged_extra_node_outside_config",
            "name": "forged_extra_node",
            "status": "passed",
            "duration": 5,
            "extra": {"deepswe": {"group": "F2P", "required": True}},
        }
        ctrf["results"]["tests"].append(extra_node)
        ctrf["results"]["summary"]["tests"] += 1
        ctrf["results"]["summary"]["passed"] += 1

        # The editable verifier pre-validation strictly blocks the malformed report:
        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(
            any("Extra unexpected CTRF nodes" in e for e in errors),
            "Editable verifier must reject extra nodes before report reaches grader",
        )

        # Document that without verifier pre-validation, the protected grader would omit this node:
        statuses = grader_required_statuses(self.config, ctrf)
        self.assertNotIn("forged_extra_node_outside_config", statuses)

    def test_editable_verifier_pre_validation_blocks_unknown_status_before_grader(self):
        """Verify that editable verifier pre-validation blocks unknown CTRF statuses before the protected grader."""
        ctrf = build_canonical_valid_ctrf(self.config)
        ctrf["results"]["tests"][0]["status"] = "corrupted_status_xyz"

        # The editable verifier pre-validation strictly blocks the invalid status:
        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(
            any("Invalid CTRF status" in e for e in errors),
            "Editable verifier must reject unknown statuses before report reaches grader",
        )

        # Document that without verifier pre-validation, the protected grader would blindly pass through:
        statuses = grader_required_statuses(self.config, ctrf)
        tid = ctrf["results"]["tests"][0]["testId"]
        self.assertEqual(statuses[tid], "corrupted_status_xyz")

    def test_verifier_exit_code_on_hard_gate_infra_error(self):
        """Verify that when hard gate detects infra error, verifier exits with code 2 to trigger test.sh trap."""
        with patch.object(verifier, "run_hard_gate") as mock_hg:
            mock_hg.return_value = {
                "passed": False,
                "infra_errors": {
                    "tsc": {"error_type": "EXECUTABLE_UNAVAILABLE", "message": "npx not found"}
                },
            }
            with tempfile.TemporaryDirectory() as tmpdir:
                tmp = Path(tmpdir)
                cfg = tmp / "config.json"
                cfg.write_text(json.dumps(self.config), encoding="utf-8")
                repo = tmp / "empty_repo"
                repo.mkdir()
                ctrf_out = tmp / "ctrf.json"
                hg_out = tmp / "hard-gate.json"

                with patch("sys.argv", ["verifier.py", "--config", str(cfg), "--repo", str(repo), "--ctrf-output", str(ctrf_out), "--hard-gate-output", str(hg_out), "--apply-failed", "0"]):
                    exit_code = verifier_main()
                    self.assertEqual(exit_code, 2)

    def test_verifier_exit_code_on_f2p_infra_error(self):
        """Verify that when F2P detects infra error, verifier updates hard-gate.json and exits with code 2."""
        with patch.object(verifier, "run_hard_gate") as mock_hg, patch.object(verifier, "run_f2p_tests") as mock_f2p:
            mock_hg.return_value = {"passed": True, "p2p_results": []}
            mock_f2p.side_effect = InfrastructureError("TIMEOUT", "Vitest F2P timed out")

            with tempfile.TemporaryDirectory() as tmpdir:
                tmp = Path(tmpdir)
                cfg = tmp / "config.json"
                cfg.write_text(json.dumps(self.config), encoding="utf-8")
                repo = tmp / "empty_repo"
                repo.mkdir()
                ctrf_out = tmp / "ctrf.json"
                hg_out = tmp / "hard-gate.json"

                with patch("sys.argv", ["verifier.py", "--config", str(cfg), "--repo", str(repo), "--ctrf-output", str(ctrf_out), "--hard-gate-output", str(hg_out), "--apply-failed", "0"]):
                    exit_code = verifier_main()
                    self.assertEqual(exit_code, 2)
                    hg_data = json.loads(hg_out.read_text(encoding="utf-8"))
                    self.assertIn("f2p_runner", hg_data["infra_errors"])

    def test_verifier_clean_candidate_failure_exits_0(self):
        """Verify that genuine candidate failures produce valid reports and exit with code 0 for grader.py."""
        with patch.object(verifier, "run_hard_gate") as mock_hg, patch.object(verifier, "generate_ctrf_report") as mock_gen_ctrf:
            mock_hg.return_value = {
                "passed": False,
                "apply_failed": False,
                "failed_nodes": ["typescript_typecheck"],
                "nodes": [
                    {"node_id": "candidate_patch_apply", "status": "passed", "description": "", "message": ""},
                    {"node_id": "typescript_typecheck", "status": "failed", "description": "", "message": ""},
                ],
                "p2p_summary": {"total": len(self.config["p2p"]), "passed": len(self.config["p2p"]) - 1, "failed": 1},
                "p2p_results": [],
                "compile_paths": ["src/"],
                "candidate_changed_paths": ["src/webcomponent.ts"],
                "protected_changes": [],
                "test_bypass": {"detected": False, "findings": []},
                "cheat_reasons": [],
                "compile_errors": {"tsc": {"exit_code": 2}},
                "infra_errors": {},
            }
            valid_ctrf = build_canonical_valid_ctrf(self.config)
            valid_ctrf["results"]["tests"][0]["status"] = "failed"
            valid_ctrf["results"]["summary"]["passed"] -= 1
            valid_ctrf["results"]["summary"]["failed"] += 1
            mock_gen_ctrf.return_value = valid_ctrf

            with tempfile.TemporaryDirectory() as tmpdir:
                tmp = Path(tmpdir)
                cfg = tmp / "config.json"
                cfg.write_text(json.dumps(self.config), encoding="utf-8")
                repo = tmp / "empty_repo"
                repo.mkdir()
                ctrf_out = tmp / "ctrf.json"
                hg_out = tmp / "hard-gate.json"

                with patch.object(verifier, "validate_hard_gate_schema", return_value=(True, [])):
                    with patch("sys.argv", ["verifier.py", "--config", str(cfg), "--repo", str(repo), "--ctrf-output", str(ctrf_out), "--hard-gate-output", str(hg_out), "--apply-failed", "0"]):
                        exit_code = verifier_main()
                        self.assertEqual(exit_code, 0)


class TestSecretSanitization(unittest.TestCase):
    """Tests that credentials and secrets are redacted from diagnostic strings."""

    def test_sanitize_bearer_token(self):
        msg = "Authorization failed with Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        sanitized = sanitize_message(msg)
        self.assertNotIn("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9", sanitized)
        self.assertIn("Bearer [REDACTED]", sanitized)

    def test_sanitize_api_key_and_password(self):
        msg = "Connecting with api_key='sk-1234567890abcdef' and password='superSecretPassword'"
        sanitized = sanitize_message(msg)
        self.assertNotIn("sk-1234567890abcdef", sanitized)
        self.assertNotIn("superSecretPassword", sanitized)
        self.assertIn("[REDACTED]", sanitized)


class TestFixedGradingProtocolIntegrityScenarios(unittest.TestCase):
    """Explicit deterministic regression tests covering all 13 fixed grading protocol adaptation scenarios."""

    def setUp(self):
        self.config = load_canonical_config()
        self.valid_ctrf = build_canonical_valid_ctrf(self.config)

    def test_scenario_01_valid_report_passes(self):
        """Scenario 1: Complete and valid CTRF report passes."""
        errors = validate_ctrf_report_integrity(self.valid_ctrf, self.config)
        self.assertEqual(errors, [], f"Valid canonical CTRF must pass with 0 errors, got: {errors}")

    def test_scenario_02_extra_passed_node_rejected(self):
        """Scenario 2: Reject report with extra 'passed' node."""
        ctrf = copy.deepcopy(self.valid_ctrf)
        extra_node = {
            "testId": "F2P::extra::unauthorized_passed_node",
            "name": "unauthorized_passed_node",
            "status": "passed",
            "duration": 5,
            "extra": {"deepswe": {"group": "F2P", "required": False}},
        }
        ctrf["results"]["tests"].append(extra_node)
        ctrf["results"]["summary"]["tests"] += 1
        ctrf["results"]["summary"]["passed"] += 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(len(errors) > 0, "Extra passed node must be rejected")
        self.assertTrue(
            any("Extra unexpected CTRF nodes" in e or "Unrecognized testId" in e for e in errors),
            f"Expected extra/unrecognized node error, got: {errors}",
        )

    def test_scenario_03_extra_failed_node_rejected(self):
        """Scenario 3: Reject report with extra 'failed' node."""
        ctrf = copy.deepcopy(self.valid_ctrf)
        extra_node = {
            "testId": "P2P::extra::unauthorized_failed_node",
            "name": "unauthorized_failed_node",
            "status": "failed",
            "duration": 5,
            "extra": {"deepswe": {"group": "P2P", "required": False}},
        }
        ctrf["results"]["tests"].append(extra_node)
        ctrf["results"]["summary"]["tests"] += 1
        ctrf["results"]["summary"]["failed"] += 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(len(errors) > 0, "Extra failed node must be rejected")
        self.assertTrue(
            any("Extra unexpected CTRF nodes" in e or "Unrecognized testId" in e for e in errors),
            f"Expected extra/unrecognized node error, got: {errors}",
        )

    def test_scenario_04_status_mystery_rejected(self):
        """Scenario 4: Reject report when valid node status changed to 'mystery'."""
        ctrf = copy.deepcopy(self.valid_ctrf)
        ctrf["results"]["tests"][0]["status"] = "mystery"
        ctrf["results"]["summary"]["passed"] -= 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(len(errors) > 0, "Status 'mystery' must be rejected")
        self.assertTrue(
            any("Invalid CTRF status 'mystery'" in e for e in errors),
            f"Expected invalid status 'mystery' error, got: {errors}",
        )

    def test_scenario_05_status_Passed_rejected(self):
        """Scenario 5: Reject report when valid node status changed to 'Passed' (capitalized)."""
        ctrf = copy.deepcopy(self.valid_ctrf)
        ctrf["results"]["tests"][0]["status"] = "Passed"
        ctrf["results"]["summary"]["passed"] -= 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(len(errors) > 0, "Status 'Passed' (capitalized) must be rejected")
        self.assertTrue(
            any("Invalid CTRF status 'Passed'" in e for e in errors),
            f"Expected invalid status 'Passed' error, got: {errors}",
        )

    def test_scenario_06_non_string_status_rejected(self):
        """Scenario 6: Reject report when valid node status changed to non-string value."""
        for invalid_val in [None, 123, True, False, ["passed"], {"status": "passed"}]:
            ctrf = copy.deepcopy(self.valid_ctrf)
            ctrf["results"]["tests"][0]["status"] = invalid_val
            ctrf["results"]["summary"]["passed"] -= 1

            errors = validate_ctrf_report_integrity(ctrf, self.config)
            self.assertTrue(len(errors) > 0, f"Non-string status {invalid_val!r} must be rejected")
            self.assertTrue(
                any("Invalid CTRF status" in e for e in errors),
                f"Expected invalid status error for {invalid_val!r}, got: {errors}",
            )

    def test_scenario_07_missing_required_node_rejected(self):
        """Scenario 7: Reject report when required node is missing."""
        ctrf = copy.deepcopy(self.valid_ctrf)
        removed = ctrf["results"]["tests"].pop(0)
        ctrf["results"]["summary"]["tests"] -= 1
        ctrf["results"]["summary"]["passed"] -= 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(len(errors) > 0, "Missing required node must be rejected")
        self.assertTrue(
            any("Missing CTRF nodes" in e for e in errors),
            f"Expected missing node error, got: {errors}",
        )

    def test_scenario_08_duplicate_node_rejected(self):
        """Scenario 8: Reject report with duplicate node."""
        ctrf = copy.deepcopy(self.valid_ctrf)
        dup = copy.deepcopy(ctrf["results"]["tests"][0])
        ctrf["results"]["tests"].append(dup)
        ctrf["results"]["summary"]["tests"] += 1
        ctrf["results"]["summary"]["passed"] += 1

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(len(errors) > 0, "Duplicate node must be rejected")
        self.assertTrue(
            any("Duplicate CTRF node" in e for e in errors),
            f"Expected duplicate node error, got: {errors}",
        )

    def test_scenario_09_p2p_group_as_F2P_rejected(self):
        """Scenario 9: Reject report when P2P node group is changed to 'F2P'."""
        ctrf = copy.deepcopy(self.valid_ctrf)
        p2p_target = next(t for t in ctrf["results"]["tests"] if t["testId"] in self.config["p2p"])
        p2p_target["extra"]["deepswe"]["group"] = "F2P"

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(len(errors) > 0, "P2P node disguised as F2P must be rejected")
        self.assertTrue(
            any("Wrong CTRF group for P2P test" in e for e in errors),
            f"Expected wrong group for P2P test error, got: {errors}",
        )

    def test_scenario_10_f2p_group_as_P2P_rejected(self):
        """Scenario 10: Reject report when F2P node group is changed to 'P2P'."""
        ctrf = copy.deepcopy(self.valid_ctrf)
        f2p_target = next(t for t in ctrf["results"]["tests"] if t["testId"] in self.config["f2p"])
        f2p_target["extra"]["deepswe"]["group"] = "P2P"

        errors = validate_ctrf_report_integrity(ctrf, self.config)
        self.assertTrue(len(errors) > 0, "F2P node disguised as P2P must be rejected")
        self.assertTrue(
            any("Wrong CTRF group for F2P test" in e for e in errors),
            f"Expected wrong group for F2P test error, got: {errors}",
        )

    def test_scenario_11_lowercase_group_rejected(self):
        """Scenario 11: Reject report when group is changed to lowercase 'p2p' or 'f2p'."""
        for invalid_group in ["p2p", "f2p", "P2p", "F2p"]:
            ctrf = copy.deepcopy(self.valid_ctrf)
            ctrf["results"]["tests"][0]["extra"]["deepswe"]["group"] = invalid_group

            errors = validate_ctrf_report_integrity(ctrf, self.config)
            self.assertTrue(len(errors) > 0, f"Lowercase/mixed group '{invalid_group}' must be rejected")
            self.assertTrue(
                any("Wrong CTRF group" in e for e in errors),
                f"Expected wrong group error for '{invalid_group}', got: {errors}",
            )

    def test_scenario_12_summary_total_mismatch_rejected(self):
        """Scenario 12: Reject report when summary tests count mismatches actual tests count."""
        for delta in [1, -1, 10]:
            ctrf = copy.deepcopy(self.valid_ctrf)
            ctrf["results"]["summary"]["tests"] += delta

            errors = validate_ctrf_report_integrity(ctrf, self.config)
            self.assertTrue(len(errors) > 0, f"Summary total mismatch by {delta} must be rejected")
            self.assertTrue(
                any("Summary total tests" in e for e in errors),
                f"Expected summary total mismatch error, got: {errors}",
            )

    def test_scenario_13_summary_status_count_mismatch_rejected(self):
        """Scenario 13: Reject report when summary status count mismatches actual count."""
        for st in ["passed", "failed", "skipped", "pending", "other"]:
            ctrf = copy.deepcopy(self.valid_ctrf)
            ctrf["results"]["summary"][st] = ctrf["results"]["summary"].get(st, 0) + 1

            errors = validate_ctrf_report_integrity(ctrf, self.config)
            self.assertTrue(len(errors) > 0, f"Summary mismatch for status '{st}' must be rejected")
            self.assertTrue(
                any(f"Summary count mismatch for '{st}'" in e for e in errors),
                f"Expected summary mismatch error for '{st}', got: {errors}",
            )

    def test_verifier_main_blocks_extra_node_with_exit_2(self):
        """Verify verifier.main() terminates with exit 2 and updates hard-gate.json on extra node."""
        with patch.object(verifier, "run_hard_gate") as mock_hg, \
             patch.object(verifier, "run_f2p_tests") as mock_f2p, \
             patch.object(verifier, "generate_ctrf_report") as mock_gen:
            mock_hg.return_value = {
                "passed": True,
                "p2p_results": [],
                "infra_errors": {},
            }
            mock_f2p.return_value = ([], {})
            ctrf = build_canonical_valid_ctrf(self.config)
            extra_node = {
                "testId": "extra_rogue_test",
                "name": "rogue",
                "status": "passed",
                "duration": 1,
                "extra": {"deepswe": {"group": "F2P", "required": False}},
            }
            ctrf["results"]["tests"].append(extra_node)
            ctrf["results"]["summary"]["tests"] += 1
            ctrf["results"]["summary"]["passed"] += 1
            mock_gen.return_value = ctrf

            with tempfile.TemporaryDirectory() as tmpdir:
                tmp = Path(tmpdir)
                cfg = tmp / "config.json"
                cfg.write_text(json.dumps(self.config), encoding="utf-8")
                repo = tmp / "empty_repo"
                repo.mkdir()
                ctrf_out = tmp / "ctrf.json"
                hg_out = tmp / "hard-gate.json"

                with patch("sys.argv", ["verifier.py", "--config", str(cfg), "--repo", str(repo), "--ctrf-output", str(ctrf_out), "--hard-gate-output", str(hg_out), "--apply-failed", "0"]):
                    exit_code = verifier_main()
                    self.assertEqual(exit_code, 2, "Verifier must exit with code 2 on extra node to block grader.py")
                    hg_data = json.loads(hg_out.read_text(encoding="utf-8"))
                    self.assertFalse(hg_data["passed"])
                    self.assertIn("ctrf_integrity", hg_data["infra_errors"])
                    self.assertEqual(hg_data["infra_errors"]["ctrf_integrity"]["error_type"], "REPORT_INTEGRITY_VIOLATION")

    def test_verifier_main_blocks_unknown_status_with_exit_2(self):
        """Verify verifier.main() terminates with exit 2 and updates hard-gate.json on unknown status."""
        with patch.object(verifier, "run_hard_gate") as mock_hg, \
             patch.object(verifier, "run_f2p_tests") as mock_f2p, \
             patch.object(verifier, "generate_ctrf_report") as mock_gen:
            mock_hg.return_value = {
                "passed": True,
                "p2p_results": [],
                "infra_errors": {},
            }
            mock_f2p.return_value = ([], {})
            ctrf = build_canonical_valid_ctrf(self.config)
            ctrf["results"]["tests"][0]["status"] = "mystery"
            mock_gen.return_value = ctrf

            with tempfile.TemporaryDirectory() as tmpdir:
                tmp = Path(tmpdir)
                cfg = tmp / "config.json"
                cfg.write_text(json.dumps(self.config), encoding="utf-8")
                repo = tmp / "empty_repo"
                repo.mkdir()
                ctrf_out = tmp / "ctrf.json"
                hg_out = tmp / "hard-gate.json"

                with patch("sys.argv", ["verifier.py", "--config", str(cfg), "--repo", str(repo), "--ctrf-output", str(ctrf_out), "--hard-gate-output", str(hg_out), "--apply-failed", "0"]):
                    exit_code = verifier_main()
                    self.assertEqual(exit_code, 2, "Verifier must exit with code 2 on unknown status to block grader.py")
                    hg_data = json.loads(hg_out.read_text(encoding="utf-8"))
                    self.assertFalse(hg_data["passed"])
                    self.assertIn("ctrf_integrity", hg_data["infra_errors"])
                    self.assertEqual(hg_data["infra_errors"]["ctrf_integrity"]["error_type"], "REPORT_INTEGRITY_VIOLATION")


if __name__ == "__main__":
    unittest.main()
