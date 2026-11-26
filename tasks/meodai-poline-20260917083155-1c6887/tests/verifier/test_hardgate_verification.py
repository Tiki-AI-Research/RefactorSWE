#!/usr/bin/env python3
"""Self-test suite for hardgate.py anti-cheat AST scanner and architecture separation gate."""

import json
import os
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import sys
from pathlib import Path

# Add verifier directory and project root to sys.path
_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

def _find_workspace_root(p: Path) -> Path:
    for parent in [p, *p.parents]:
        if (parent / "source").is_dir() and (parent / "case").is_dir():
            return parent
    return p.parents[2] if len(p.parents) > 2 else p.parent

WORKSPACE_ROOT = _find_workspace_root(_HERE)
SOURCE_DIR = WORKSPACE_ROOT / "source"
sys.path.insert(0, str(WORKSPACE_ROOT))

# Import hardgate components
try:
    from hardgate import (
        AST_ANALYZER_SCRIPT,
        scan_test_bypass_ast,
        check_architecture_separation,
        get_environment_with_node_modules,
        ARCHITECTURE_F2P_NODE_ID,
        create_architecture_f2p_entry,
        REQUIRED_HARD_GATE_NODE_IDS,
        REQUIRED_CHEAT_NODE_IDS,
        validate_hard_gate_schema,
        NodeResult,
    )
except ImportError:
    from case.tests.verifier.hardgate import (
        AST_ANALYZER_SCRIPT,
        scan_test_bypass_ast,
        check_architecture_separation,
        get_environment_with_node_modules,
        ARCHITECTURE_F2P_NODE_ID,
        create_architecture_f2p_entry,
        REQUIRED_HARD_GATE_NODE_IDS,
        REQUIRED_CHEAT_NODE_IDS,
        validate_hard_gate_schema,
        NodeResult,
    )


class TestAntiCheatASTScanner(unittest.TestCase):
    """Test AST-aware detection of test bypass mechanisms without false positives."""

    def setUp(self):
        self.repo_dir = SOURCE_DIR.resolve()
        self.cmd_env = get_environment_with_node_modules(self.repo_dir)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_dir = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def _create_ts_file(self, filename: str, content: str) -> Path:
        p = self.test_dir / filename
        p.write_text(content, encoding="utf-8")
        return p

    def test_comments_and_strings_not_flagged(self):
        """Comments, docstrings, and string literals should never trigger false positives."""
        content = """
        // test.only("this is a comment", () => {});
        // it.skip("another comment", () => {});
        /*
         * describe.skip("block comment", () => {});
         * fit("focused in comment", () => {});
         * it["only"]("bracket in comment");
         */
        const notice = "Remember: describe.only and it.skip are disallowed";
        const doc = `
          Do not call test.skip or fit in your code.
        `;
        function info() {
          const skipMsg = 'it.skip should not be called';
          return skipMsg;
        }
        """
        f = self._create_ts_file("safe_comments.ts", content)
        findings = scan_test_bypass_ast([f], self.repo_dir, self.cmd_env)
        self.assertEqual(findings, [], f"Expected 0 findings for safe comments/strings, got: {findings}")

    def test_direct_bypass_functions_flagged(self):
        """fit, fdescribe, xit, xdescribe must be flagged as executable bypasses."""
        for fn_name in ["fit", "fdescribe", "xit", "xdescribe"]:
            content = f"{fn_name}('should be flagged', () => {{}});"
            f = self._create_ts_file(f"bypass_{fn_name}.ts", content)
            findings = scan_test_bypass_ast([f], self.repo_dir, self.cmd_env)
            self.assertTrue(
                any(fn_name in msg for msg in findings),
                f"Expected finding for {fn_name}, got: {findings}",
            )

    def test_member_bypass_calls_flagged(self):
        """it.skip, test.only, describe.todo must be flagged."""
        cases = [
            ("it.skip('test', () => {})", "it.skip"),
            ("test.only('test', () => {})", "test.only"),
            ("describe.todo('test')", "describe.todo"),
            ("suite.only('suite', () => {})", "suite.only"),
        ]
        for expr, label in cases:
            content = f"{expr};"
            f = self._create_ts_file(f"bypass_{label.replace('.', '_')}.ts", content)
            findings = scan_test_bypass_ast([f], self.repo_dir, self.cmd_env)
            self.assertTrue(
                any(label in msg for msg in findings),
                f"Expected finding for {label}, got: {findings}",
            )

    def test_bracket_access_bypass_flagged(self):
        """it['only'](...) or it['skip'](...) must be flagged."""
        content = "it['only']('bracket notation test', () => {});"
        f = self._create_ts_file("bracket_only.ts", content)
        findings = scan_test_bypass_ast([f], self.repo_dir, self.cmd_env)
        self.assertTrue(
            any("it['only']" in msg or "it.only" in msg for msg in findings),
            f"Expected bracket access finding, got: {findings}",
        )

    def test_multiline_bracket_access_bypass_flagged(self):
        """describe[\n  'skip'\n](...) must be flagged."""
        content = """
        describe[
          'skip'
        ]('multiline bracket', () => {});
        """
        f = self._create_ts_file("multiline_bracket.ts", content)
        findings = scan_test_bypass_ast([f], self.repo_dir, self.cmd_env)
        self.assertTrue(
            any("skip" in msg for msg in findings),
            f"Expected multiline bracket finding, got: {findings}",
        )

    def test_multiline_whitespace_bypass_flagged(self):
        """Multiline and whitespace formatted calls must be flagged."""
        content = """
        test
          .only(
            'multiline test',
            () => {}
          );
        """
        f = self._create_ts_file("multiline_bypass.ts", content)
        findings = scan_test_bypass_ast([f], self.repo_dir, self.cmd_env)
        self.assertTrue(
            any("test.only" in msg for msg in findings),
            f"Expected multiline test.only finding, got: {findings}",
        )

    def test_aliasing_and_property_access_flagged(self):
        """const mySkip = it.skip; or const myOnly = test['only']; must be flagged."""
        content = """
        const mySkip = it.skip;
        const myOnly = test['only'];
        """
        f = self._create_ts_file("alias_bypass.ts", content)
        findings = scan_test_bypass_ast([f], self.repo_dir, self.cmd_env)
        self.assertGreaterEqual(len(findings), 2, f"Expected at least 2 alias findings, got: {findings}")


class TestArchitectureSeparationGate(unittest.TestCase):
    """Test architectural responsibility separation and delegation verification."""

    def _create_valid_separated_src(self, src_dir: Path) -> None:
        src_dir.mkdir(parents=True, exist_ok=True)
        (src_dir / "index.ts").write_text("export class Poline {}\nexport class ColorPoint {}\n", encoding="utf-8")
        (src_dir / "picker-types.ts").write_text("export interface PickerOptions {}\n", encoding="utf-8")

        view_code = """import { Poline } from "./index";
import { PickerOptions } from "./picker-types";

export class PickerView {
  private root: any;
  private svg: SVGElement;
  private polineProvider: () => any;

  constructor(root: any, polineProvider: () => any) {
    this.root = root;
    this.polineProvider = polineProvider;
    this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const line = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
    line.setAttribute("class", "wheel__line");
    line.setAttribute("points", "0 0");
    this.svg.appendChild(line);
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("class", "wheel__circle");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    circle.setAttribute("r", "5");
    this.svg.appendChild(circle);
  }

  public updateSVG(poline: any): void {
    if (!this.svg || !poline) return;
    const minL = "--minL";
    const maxL = "--maxL";
    const gradient = "linearGradient";
  }

  public getSvgElement(): SVGElement {
    return this.svg;
  }
}
"""
        (src_dir / "picker-view.ts").write_text(view_code, encoding="utf-8")

        int_code = """import { Poline } from "./index";
import { PickerOptions } from "./picker-types";

export class PickerInteraction {
  private root: any;
  private host: any;
  private polineProvider: () => any;
  private onUpdate: () => void;
  private activePointerId: number | null = null;
  private allowAddPoints = false;

  constructor(
    root: any,
    polineProvider: () => any,
    host: any,
    onUpdate: () => void
  ) {
    this.root = root;
    this.polineProvider = polineProvider;
    this.host = host;
    this.onUpdate = onUpdate;
  }

  public bind(svg?: any): void {
    svg?.addEventListener("pointerdown", (e: any) => this.handlePointerDown(e));
  }

  public unbind(): void {
    this.activePointerId = null;
  }

  public setAllowAddPoints(allow: boolean): void {
    this.allowAddPoints = allow;
  }

  private handlePointerDown(e: PointerEvent): void {
    const angle = Math.atan2(e.clientY, e.clientX);
    this.activePointerId = e.pointerId;
  }
}
"""
        (src_dir / "picker-interaction.ts").write_text(int_code, encoding="utf-8")

        wc_code = """import { Poline } from "./index";
import { PickerView } from "./picker-view";
import { PickerInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private view: PickerView;
  private interaction: PickerInteraction;

  connectedCallback() {
    this.view = new PickerView(this.shadowRoot, () => this.poline);
    this.interaction = new PickerInteraction(
      this.shadowRoot,
      () => this.poline,
      this,
      () => this.view.updateSVG(this.poline)
    );
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    if (this.interaction) {
      this.interaction.unbind();
    }
    this.view = null as any;
    this.interaction = null as any;
  }

  setPoline(p: any) {
    this.poline = p;
    if (this.view) {
      this.view.updateSVG(this.poline);
    }
  }

  setAllowAddPoints(allow: boolean) {
    if (this.interaction) {
      this.interaction.setAllowAddPoints(allow);
    }
  }

  updateSVG() {
    if (!this.poline || !this.view.getSvgElement()) return;
    this.view.updateSVG(this.poline);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src_dir / "webcomponent.ts").write_text(wc_code, encoding="utf-8")

    def setUp(self):
        self.repo_dir = SOURCE_DIR.resolve()
        self.cmd_env = get_environment_with_node_modules(self.repo_dir)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_repo = Path(self.temp_dir.name)
        # Create explicit, self-contained separated architecture fixture
        self.src = self.temp_repo / "src"
        self._create_valid_separated_src(self.src)

    def tearDown(self):
        self.temp_dir.cleanup()

    def _run_analyzer(self, src_dir: Path) -> dict:
        req_data = json.dumps({"action": "analyze_architecture", "srcDir": str(src_dir.resolve())})
        proc = subprocess.run(
            ["node", "-e", AST_ANALYZER_SCRIPT],
            cwd=str(self.repo_dir),
            env=self.cmd_env,
            input=req_data,
            text=True,
            capture_output=True,
            timeout=30.0,
        )
        self.assertEqual(proc.returncode, 0, f"Node analyzer failed: {proc.stderr}")
        return json.loads(proc.stdout)

    def test_valid_separated_implementation_passes(self):
        """Explicitly fixture a valid separated implementation and verify architecture check passes."""
        src = self.temp_repo / "src"
        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Valid separated implementation should pass, got: {res.get('errors')}")
        self.assertEqual(res.get("presentationModule"), "picker-view.ts")
        self.assertEqual(res.get("interactionModule"), "picker-interaction.ts")

        # Also verify create_architecture_f2p_entry produces passed status
        entry = create_architecture_f2p_entry(res.get("passed"), "")
        self.assertEqual(entry["testId"], ARCHITECTURE_F2P_NODE_ID)
        self.assertEqual(entry["status"], "passed")
        self.assertEqual(entry["extra"]["deepswe"]["group"], "F2P")

    @patch("subprocess.run")
    def test_architecture_analyzer_launch_failure_is_infra_error(self, mock_run):
        """Executable unavailable during AST analysis must be classified as infrastructure failure."""
        mock_run.side_effect = FileNotFoundError("node not found")
        passed, msg, details = check_architecture_separation(self.temp_repo, self.cmd_env)
        self.assertFalse(passed)
        self.assertTrue(details.get("is_infra"))
        self.assertEqual(details.get("infra_type"), "EXECUTABLE_UNAVAILABLE")

    @patch("subprocess.run")
    def test_architecture_analyzer_timeout_is_infra_error(self, mock_run):
        """Timeout during AST analysis must be classified as infrastructure failure."""
        mock_run.side_effect = subprocess.TimeoutExpired(cmd=["node"], timeout=30.0)
        passed, msg, details = check_architecture_separation(self.temp_repo, self.cmd_env)
        self.assertFalse(passed)
        self.assertTrue(details.get("is_infra"))
        self.assertEqual(details.get("infra_type"), "TIMEOUT")

    def test_renamed_modules_pass(self):
        """Refactoring must pass even if presentation and interaction modules have custom names."""
        src = self.temp_repo / "src"
        # Rename picker-view.ts -> custom-view-renderer.ts
        view_orig = src / "picker-view.ts"
        view_new = src / "custom-view-renderer.ts"
        view_orig.rename(view_new)

        # Rename picker-interaction.ts -> custom-gesture-manager.ts
        int_orig = src / "picker-interaction.ts"
        int_new = src / "custom-gesture-manager.ts"
        int_orig.rename(int_new)

        # Update imports in webcomponent.ts
        wc = src / "webcomponent.ts"
        wc_content = wc.read_text(encoding="utf-8")
        wc_content = wc_content.replace('from "./picker-view"', 'from "./custom-view-renderer"')
        wc_content = wc_content.replace('from "./picker-interaction"', 'from "./custom-gesture-manager"')
        wc.write_text(wc_content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Renamed modules should pass, but failed with: {res.get('errors')}")
        self.assertEqual(res.get("presentationModule"), "custom-view-renderer.ts")
        self.assertEqual(res.get("interactionModule"), "custom-gesture-manager.ts")

    def test_monolithic_implementation_fails(self):
        """Monolithic implementation where SVG rendering and pointer math stay in webcomponent must fail."""
        src = self.temp_repo / "src"
        # Remove separate modules
        for f in ["picker-view.ts", "picker-interaction.ts"]:
            p = src / f
            if p.is_file():
                p.unlink()

        # Write monolithic webcomponent
        monolithic_content = """
        import { Poline } from "./index";

        export class PolinePicker extends HTMLElement {
          private poline: Poline | null = null;
          private svg: SVGElement | null = null;
          private activePointerId: number | null = null;

          connectedCallback() {
            this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
            this.svg.addEventListener("pointerdown", (e) => this.handlePointerDown(e));
          }

          disconnectedCallback() {
            this.svg = null;
          }

          updateSVG() {
            if (!this.svg) return;
            const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            circle.setAttribute("cx", "50");
            circle.setAttribute("cy", "50");
            circle.setAttribute("r", "5");
            this.svg.appendChild(circle);
          }

          private handlePointerDown(e: PointerEvent) {
            const angle = Math.atan2(e.clientY, e.clientX);
            this.activePointerId = e.pointerId;
          }
        }
        customElements.define("poline-picker", PolinePicker);
        """
        (src / "webcomponent.ts").write_text(monolithic_content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("responsibilities still embedded in PolinePicker", errors_str)
        self.assertIn("missing presentation separation", errors_str)
        self.assertIn("missing interaction separation", errors_str)

    def test_empty_shell_modules_fail(self):
        """Empty or dummy modules without actual presentation or interaction logic must fail."""
        src = self.temp_repo / "src"
        # Overwrite with empty shells
        (src / "picker-view.ts").write_text("export class PickerView { constructor() {} }\n", encoding="utf-8")
        (src / "picker-interaction.ts").write_text("export class PickerInteraction { constructor() {} }\n", encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertTrue(
            "missing presentation separation" in errors_str or "missing interaction separation" in errors_str,
            f"Expected separation failure for empty shells, got: {errors_str}",
        )

    def test_global_mutable_state_fails(self):
        """Top-level mutable state (let/var) in modules must fail."""
        src = self.temp_repo / "src"
        view_p = src / "picker-view.ts"
        content = "let sharedGlobalState = 42;\n" + view_p.read_text(encoding="utf-8")
        view_p.write_text(content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("global or shared mutable state introduced", errors_str)

    def test_missing_delegation_fails(self):
        """PolinePicker omitting delegation calls in lifecycle/update methods must fail."""
        src = self.temp_repo / "src"
        wc_p = src / "webcomponent.ts"
        content = wc_p.read_text(encoding="utf-8")
        # Empty delegation inside updateSVG
        content_no_update_delegation = content.replace(
            "this.view.updateSVG(this.poline);",
            "/* skipped view update */"
        ).replace("!this.view.getSvgElement()", "!this.poline")
        self.assertNotEqual(content, content_no_update_delegation)
        wc_p.write_text(content_no_update_delegation, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing coordinator delegation", errors_str)

    def test_missing_presentation_module_fails(self):
        """Missing presentation module while keeping interaction module must fail."""
        src = self.temp_repo / "src"
        (src / "picker-view.ts").unlink()
        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing presentation separation", errors_str)

    def test_missing_interaction_module_fails(self):
        """Missing interaction module while keeping presentation module must fail."""
        src = self.temp_repo / "src"
        (src / "picker-interaction.ts").unlink()
        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing interaction separation", errors_str)

    def test_missing_interaction_delegation_fails(self):
        """PolinePicker.setAllowAddPoints failing to delegate must fail."""
        src = self.temp_repo / "src"
        wc_p = src / "webcomponent.ts"
        content = wc_p.read_text(encoding="utf-8")
        content_no_allow = content.replace(
            "this.interaction.setAllowAddPoints(allow);",
            "/* skipped allow add points delegation */"
        )
        self.assertNotEqual(content, content_no_allow)
        wc_p.write_text(content_no_allow, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing coordinator delegation", errors_str)
        self.assertIn("setAllowAddPoints", errors_str)

    def test_subdirectory_split_passes(self):
        """Refactoring into subdirectories like src/picker/view.ts must pass."""
        src = self.temp_repo / "src"
        picker_dir = src / "picker"
        picker_dir.mkdir()
        (src / "picker-view.ts").rename(picker_dir / "view.ts")
        (src / "picker-interaction.ts").rename(picker_dir / "interaction.ts")
        (src / "picker-types.ts").rename(picker_dir / "types.ts")

        v = (picker_dir / "view.ts").read_text(encoding="utf-8")
        (picker_dir / "view.ts").write_text(v.replace('"./picker-types"', '"./types"').replace('"./index"', '"../index"'), encoding="utf-8")
        i = (picker_dir / "interaction.ts").read_text(encoding="utf-8")
        (picker_dir / "interaction.ts").write_text(i.replace('"./picker-types"', '"./types"').replace('"./index"', '"../index"'), encoding="utf-8")

        wc = (src / "webcomponent.ts").read_text(encoding="utf-8")
        wc = wc.replace('"./picker-view"', '"./picker/view"')
        wc = wc.replace('"./picker-interaction"', '"./picker/interaction"')
        wc = wc.replace('"./picker-types"', '"./picker/types"')
        (src / "webcomponent.ts").write_text(wc, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Subdirectory split should pass, got errors: {res.get('errors')}")
        self.assertEqual(res.get("presentationModule"), "view.ts")
        self.assertEqual(res.get("interactionModule"), "interaction.ts")

    def test_neutral_naming_passes(self):
        """Refactoring using neutral names without view/render/interaction must pass."""
        src = self.temp_repo / "src"
        (src / "picker-view.ts").rename(src / "display.ts")
        (src / "picker-interaction.ts").rename(src / "manipulator.ts")

        wc = (src / "webcomponent.ts").read_text(encoding="utf-8")
        wc = wc.replace('"./picker-view"', '"./display"')
        wc = wc.replace('PickerView', 'DisplayEngine')
        wc = wc.replace('"./picker-interaction"', '"./manipulator"')
        wc = wc.replace('PickerInteraction', 'ManipulatorEngine')
        wc = wc.replace('private view: DisplayEngine;', 'private displayEngine: DisplayEngine;')
        wc = wc.replace('this.view', 'this.displayEngine')
        wc = wc.replace('private interaction: ManipulatorEngine;', 'private gestureControl: ManipulatorEngine;')
        wc = wc.replace('this.interaction', 'this.gestureControl')
        (src / "webcomponent.ts").write_text(wc, encoding="utf-8")

        v = (src / "display.ts").read_text(encoding="utf-8")
        (src / "display.ts").write_text(v.replace('PickerView', 'DisplayEngine'), encoding="utf-8")
        m = (src / "manipulator.ts").read_text(encoding="utf-8")
        (src / "manipulator.ts").write_text(m.replace('PickerInteraction', 'ManipulatorEngine'), encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Neutral naming should pass, got errors: {res.get('errors')}")
        self.assertEqual(res.get("presentationModule"), "display.ts")
        self.assertEqual(res.get("interactionModule"), "manipulator.ts")

    def test_finer_sub_helpers_passes(self):
        """Splitting presentation into finer sub-helper modules must aggregate features and pass."""
        src = self.temp_repo / "src"
        svg_helper = """
        export function createWheelSvg(): SVGElement {
          const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
          const line = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
          line.setAttribute("class", "wheel__line");
          line.setAttribute("points", "0 0");
          svg.appendChild(line);
          return svg;
        }
        """
        (src / "svg-helper.ts").write_text(svg_helper, encoding="utf-8")
        v = (src / "picker-view.ts").read_text(encoding="utf-8")
        v = 'import { createWheelSvg } from "./svg-helper";\n' + v
        (src / "picker-view.ts").write_text(v, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Finer sub-helpers should pass, got: {res.get('errors')}")

    def test_internal_facade_passes(self):
        """Internal facade coordinating presentation and interaction must pass."""
        src = self.temp_repo / "src"
        facade = """
        import { PickerView } from "./picker-view";
        import { PickerInteraction } from "./picker-interaction";

        export class PickerFacade {
          public view: PickerView;
          public interaction: PickerInteraction;
          constructor(root: any, host: any, polineProvider: any) {
            this.view = new PickerView(root, polineProvider);
            this.interaction = new PickerInteraction(root, polineProvider, host, () => this.view.updateSVG(polineProvider()));
          }
        }
        """
        (src / "facade.ts").write_text(facade, encoding="utf-8")
        wc = (src / "webcomponent.ts").read_text(encoding="utf-8")
        wc = 'import { PickerFacade } from "./facade";\n' + wc.replace(
            'private view: PickerView;\n  private interaction: PickerInteraction;',
            'private facade: PickerFacade;\n  private view: PickerView;\n  private interaction: PickerInteraction;'
        )
        wc = wc.replace(
            'this.view = new PickerView(this.shadowRoot, () => this.poline);',
            'this.facade = new PickerFacade(this.shadowRoot, this, () => this.poline);\n    this.view = this.facade.view;\n    this.interaction = this.facade.interaction;'
        )
        (src / "webcomponent.ts").write_text(wc, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Internal facade should pass, got: {res.get('errors')}")

    def test_merged_presentation_and_interaction_fails(self):
        """Combining presentation and interaction into a single collaborator class must fail."""
        src = self.temp_repo / "src"
        (src / "picker-view.ts").unlink()
        (src / "picker-interaction.ts").unlink()

        combined_code = """import { Poline } from "./index";

export class PickerCombined {
  private svg: SVGElement;
  private activePointerId: number | null = null;

  constructor() {
    this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    circle.setAttribute("r", "5");
    this.svg.appendChild(circle);
  }

  public updateSVG(p: any): void {
    const minL = "--minL";
    const maxL = "--maxL";
    const gradient = "linearGradient";
  }

  public bind(): void {
    this.svg.addEventListener("pointerdown", (e: any) => {
      const angle = Math.atan2(e.clientY, e.clientX);
      this.activePointerId = e.pointerId;
    });
  }

  public unbind(): void {
    this.activePointerId = null;
  }

  public setAllowAddPoints(a: boolean): void {}
}
"""
        (src / "picker-combined.ts").write_text(combined_code, encoding="utf-8")

        wc_code = """import { Poline } from "./index";
import { PickerCombined } from "./picker-combined";

export class PolinePicker extends HTMLElement {
  private combined: PickerCombined;

  connectedCallback() {
    this.combined = new PickerCombined();
    this.combined.bind();
  }

  disconnectedCallback() {
    this.combined.unbind();
  }

  setPoline(p: any) {}

  setAllowAddPoints(allow: boolean) {
    this.combined.setAllowAddPoints(allow);
  }

  updateSVG() {
    this.combined.updateSVG(null);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("combined in the same collaborator", errors_str)

    def test_allow_add_points_provider_callback_passes(self):
        """Allow-add-points coordinated via state provider or options callback must pass."""
        src = self.temp_repo / "src"
        wc_p = src / "webcomponent.ts"
        wc_content = wc_p.read_text(encoding="utf-8")
        wc_content = wc_content.replace(
            "this.interaction.setAllowAddPoints(allow);",
            "this.allowAddPoints = allow;"
        )
        wc_content = wc_content.replace(
            "this.interaction.bind(this.view.getSvgElement());",
            "this.interaction = new PickerInteraction(this.shadowRoot, () => this.poline, this, () => this.view.updateSVG(this.poline), { canAdd: () => this.allowAddPoints });\n    this.interaction.bind(this.view.getSvgElement());"
        )
        wc_p.write_text(wc_content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Provider callback options should pass, got: {res.get('errors')}")

    def test_same_file_distinct_responsibility_classes_pass(self):
        """Co-locating separate responsibility classes in webcomponent.ts must pass."""
        src = self.temp_repo / "src"
        v = (src / "picker-view.ts").read_text(encoding="utf-8")
        i = (src / "picker-interaction.ts").read_text(encoding="utf-8")
        wc = (src / "webcomponent.ts").read_text(encoding="utf-8")

        (src / "picker-view.ts").unlink()
        (src / "picker-interaction.ts").unlink()

        clean_v = v.replace('import { Poline } from "./index";', '').replace('import { PickerOptions } from "./picker-types";', '')
        clean_i = i.replace('import { Poline } from "./index";', '').replace('import { PickerOptions } from "./picker-types";', '')
        clean_wc = wc.replace('import { PickerView } from "./picker-view";', '').replace('import { PickerInteraction } from "./picker-interaction";', '')

        combined_wc = f"{clean_v}\n{clean_i}\n{clean_wc}"
        (src / "webcomponent.ts").write_text(combined_wc, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Co-located distinct classes should pass, got: {res.get('errors')}")
        self.assertEqual(res.get("presentationModule"), "webcomponent.ts")
        self.assertEqual(res.get("interactionModule"), "webcomponent.ts")

    def test_fake_callback_delegation_fails(self):
        """Modifying unrelated state in setAllowAddPoints without connecting it to interaction must fail."""
        src = self.temp_repo / "src"
        wc_p = src / "webcomponent.ts"
        wc_content = wc_p.read_text(encoding="utf-8")
        fake_wc = wc_content.replace(
            "this.interaction.setAllowAddPoints(allow);",
            "this.dummyFlag = allow;"
        )
        wc_p.write_text(fake_wc, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"), "Fake callback delegation should fail")
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing coordinator delegation", errors_str)
        self.assertIn("setAllowAddPoints", errors_str)

    def test_unrelated_set_named_call_is_not_interaction_delegation(self):
        """Unrelated calls like setAttribute or resetCache in setAllowAddPoints must not pass delegation check."""
        src = self.temp_repo / "src"
        wc_p = src / "webcomponent.ts"
        wc_content = wc_p.read_text(encoding="utf-8")

        # Variant 1: setAttribute (contains 'set')
        fake_wc1 = wc_content.replace(
            "this.interaction.setAllowAddPoints(allow);",
            'this.setAttribute("data-allow", String(allow));'
        )
        wc_p.write_text(fake_wc1, encoding="utf-8")

        res1 = self._run_analyzer(src)
        self.assertFalse(res1.get("passed"), "setAttribute in setAllowAddPoints must not pass delegation check")
        errors_str1 = " ".join(res1.get("errors", []))
        self.assertIn("missing coordinator delegation", errors_str1)
        self.assertIn("setAllowAddPoints", errors_str1)

        # Variant 2: resetCache (contains 'set')
        fake_wc2 = wc_content.replace(
            "this.interaction.setAllowAddPoints(allow);",
            "this.resetCache();"
        )
        wc_p.write_text(fake_wc2, encoding="utf-8")

        res2 = self._run_analyzer(src)
        self.assertFalse(res2.get("passed"), "resetCache in setAllowAddPoints must not pass delegation check")
        errors_str2 = " ".join(res2.get("errors", []))
        self.assertIn("missing coordinator delegation", errors_str2)
        self.assertIn("setAllowAddPoints", errors_str2)

    def test_unrelated_interaction_named_provider_is_not_delegation(self):
        """Passing state to an unrelated class named Interaction* does not satisfy provider delegation."""
        src = self.temp_repo / "src"
        wc_p = src / "webcomponent.ts"
        wc_content = wc_p.read_text(encoding="utf-8")

        logger_def = """
export class InteractionLogger {
  private readAllow: () => boolean;
  constructor(readAllow: () => boolean) {
    this.readAllow = readAllow;
  }
}
"""
        wc_content = logger_def + "\n" + wc_content
        wc_content = wc_content.replace(
            "this.interaction.setAllowAddPoints(allow);",
            "this.allowAddPoints = allow;"
        )
        wc_content = wc_content.replace(
            "this.interaction.bind(this.view.getSvgElement());",
            "this.logger = new InteractionLogger(() => this.allowAddPoints);\n    this.interaction.bind(this.view.getSvgElement());"
        )
        wc_p.write_text(wc_content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"), "Interaction-named dummy class must not satisfy provider delegation")
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing coordinator delegation", errors_str)
        self.assertIn("setAllowAddPoints", errors_str)

    def test_allow_add_points_provider_factory_passes(self):
        """Allow-add-points coordinated via provider factory method passed to and consumed by interaction collaborator must pass."""
        src = self.temp_repo / "src"

        int_p = src / "picker-interaction.ts"
        int_code = """import { Poline } from "./index";
import { PickerOptions } from "./picker-types";

export interface InteractionDelegate {
  getAllowAddPoints(): boolean;
}

export class PickerInteraction {
  private delegate: InteractionDelegate;
  private activePointerId: number | null = null;

  constructor(delegate: InteractionDelegate) {
    this.delegate = delegate;
  }

  public bind(svg?: any): void {
    svg?.addEventListener("pointerdown", (e: any) => this.handlePointerDown(e));
  }

  public unbind(): void {
    this.activePointerId = null;
  }

  private handlePointerDown(e: PointerEvent): void {
    if (this.delegate.getAllowAddPoints()) {
      // interaction-owned point-addition decision
    }
    const angle = Math.atan2(e.clientY, e.clientX);
    this.activePointerId = e.pointerId;
  }
}
"""
        int_p.write_text(int_code, encoding="utf-8")

        wc_p = src / "webcomponent.ts"
        wc_code = """import { Poline } from "./index";
import { PickerView } from "./picker-view";
import { PickerInteraction, InteractionDelegate } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  #allowAddPoints = false;
  private poline: Poline | null = null;
  private view: PickerView;
  private interaction: PickerInteraction;

  setAllowAddPoints(allow: boolean): void {
    this.#allowAddPoints = allow;
  }

  private createInteractionDelegate(): InteractionDelegate {
    return {
      getAllowAddPoints: () => this.#allowAddPoints,
    };
  }

  connectedCallback() {
    this.view = new PickerView(this.shadowRoot, () => this.poline);
    this.interaction = new PickerInteraction(this.createInteractionDelegate());
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    if (this.interaction) {
      this.interaction.unbind();
    }
  }

  setPoline(p: any) {
    this.poline = p;
    if (this.view) {
      this.view.updateSVG(this.poline);
    }
  }

  updateSVG() {
    if (!this.poline || !this.view.getSvgElement()) return;
    this.view.updateSVG(this.poline);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        wc_p.write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Provider factory pattern should pass, got: {res.get('errors')}")

    def test_allow_add_points_provider_factory_unpassed_fails(self):
        """Creating provider factory but not passing it to interaction collaborator must fail."""
        src = self.temp_repo / "src"

        int_p = src / "picker-interaction.ts"
        int_code = """import { Poline } from "./index";
import { PickerOptions } from "./picker-types";

export interface InteractionDelegate {
  getAllowAddPoints(): boolean;
}

export class PickerInteraction {
  private activePointerId: number | null = null;

  constructor() {}

  public bind(svg?: any): void {
    svg?.addEventListener("pointerdown", (e: any) => this.handlePointerDown(e));
  }

  public unbind(): void {
    this.activePointerId = null;
  }

  private handlePointerDown(e: PointerEvent): void {
    const angle = Math.atan2(e.clientY, e.clientX);
    this.activePointerId = e.pointerId;
  }
}
"""
        int_p.write_text(int_code, encoding="utf-8")

        wc_p = src / "webcomponent.ts"
        wc_code = """import { Poline } from "./index";
import { PickerView } from "./picker-view";
import { PickerInteraction, InteractionDelegate } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  #allowAddPoints = false;
  private poline: Poline | null = null;
  private view: PickerView;
  private interaction: PickerInteraction;

  setAllowAddPoints(allow: boolean): void {
    this.#allowAddPoints = allow;
  }

  private createInteractionDelegate(): InteractionDelegate {
    return {
      getAllowAddPoints: () => this.#allowAddPoints,
    };
  }

  connectedCallback() {
    this.view = new PickerView(this.shadowRoot, () => this.poline);
    this.interaction = new PickerInteraction();
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    if (this.interaction) {
      this.interaction.unbind();
    }
  }

  setPoline(p: any) {
    this.poline = p;
    if (this.view) {
      this.view.updateSVG(this.poline);
    }
  }

  updateSVG() {
    if (!this.poline || !this.view.getSvgElement()) return;
    this.view.updateSVG(this.poline);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        wc_p.write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"), "Unpassed provider factory must fail delegation check")
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing coordinator delegation", errors_str)
        self.assertIn("setAllowAddPoints", errors_str)

    def test_allow_add_points_provider_factory_unconsumed_fails(self):
        """Passing provider factory to interaction that never consumes the callback member must fail."""
        src = self.temp_repo / "src"

        int_p = src / "picker-interaction.ts"
        int_code = """import { Poline } from "./index";
import { PickerOptions } from "./picker-types";

export interface InteractionDelegate {
  getAllowAddPoints(): boolean;
}

export class PickerInteraction {
  private delegate: InteractionDelegate;
  private activePointerId: number | null = null;

  constructor(delegate: InteractionDelegate) {
    this.delegate = delegate;
  }

  public bind(svg?: any): void {
    svg?.addEventListener("pointerdown", (e: any) => this.handlePointerDown(e));
  }

  public unbind(): void {
    this.activePointerId = null;
  }

  private handlePointerDown(e: PointerEvent): void {
    const angle = Math.atan2(e.clientY, e.clientX);
    this.activePointerId = e.pointerId;
  }
}
"""
        int_p.write_text(int_code, encoding="utf-8")

        wc_p = src / "webcomponent.ts"
        wc_code = """import { Poline } from "./index";
import { PickerView } from "./picker-view";
import { PickerInteraction, InteractionDelegate } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  #allowAddPoints = false;
  private poline: Poline | null = null;
  private view: PickerView;
  private interaction: PickerInteraction;

  setAllowAddPoints(allow: boolean): void {
    this.#allowAddPoints = allow;
  }

  private createInteractionDelegate(): InteractionDelegate {
    return {
      getAllowAddPoints: () => this.#allowAddPoints,
    };
  }

  connectedCallback() {
    this.view = new PickerView(this.shadowRoot, () => this.poline);
    this.interaction = new PickerInteraction(this.createInteractionDelegate());
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    if (this.interaction) {
      this.interaction.unbind();
    }
  }

  setPoline(p: any) {
    this.poline = p;
    if (this.view) {
      this.view.updateSVG(this.poline);
    }
  }

  updateSVG() {
    if (!this.poline || !this.view.getSvgElement()) return;
    this.view.updateSVG(this.poline);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        wc_p.write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"), "Unconsumed provider callback must fail delegation check")
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing coordinator delegation", errors_str)
        self.assertIn("setAllowAddPoints", errors_str)

    def test_allow_add_points_provider_factory_unrelated_class_fails(self):
        """Passing provider factory to an unrelated class without interaction responsibilities must fail."""
        src = self.temp_repo / "src"

        wc_p = src / "webcomponent.ts"
        wc_code = """import { Poline } from "./index";
import { PickerView } from "./picker-view";
import { PickerInteraction } from "./picker-interaction";

export class InteractionLogger {
  private delegate: any;
  constructor(delegate: any) {
    this.delegate = delegate;
  }
}

export class PolinePicker extends HTMLElement {
  #allowAddPoints = false;
  private poline: Poline | null = null;
  private view: PickerView;
  private interaction: PickerInteraction;
  private logger: InteractionLogger;

  setAllowAddPoints(allow: boolean): void {
    this.#allowAddPoints = allow;
  }

  private createInteractionDelegate() {
    return {
      getAllowAddPoints: () => this.#allowAddPoints,
    };
  }

  connectedCallback() {
    this.view = new PickerView(this.shadowRoot, () => this.poline);
    this.logger = new InteractionLogger(this.createInteractionDelegate());
    this.interaction = new PickerInteraction(
      this.shadowRoot,
      () => this.poline,
      this,
      () => this.view.updateSVG(this.poline)
    );
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    if (this.interaction) {
      this.interaction.unbind();
    }
  }

  setPoline(p: any) {
    this.poline = p;
    if (this.view) {
      this.view.updateSVG(this.poline);
    }
  }

  updateSVG() {
    if (!this.poline || !this.view.getSvgElement()) return;
    this.view.updateSVG(this.poline);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        wc_p.write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"), "Passing provider factory to dummy logger must fail delegation check")
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing coordinator delegation", errors_str)
        self.assertIn("setAllowAddPoints", errors_str)

    def test_mock_node_contains_semantics(self):
        """MockNode.prototype.contains real assertions must be present in test.patch for Vitest execution."""
        patch_path = _HERE / "test.patch"
        self.assertTrue(patch_path.is_file(), "test.patch must exist")
        patch_content = patch_path.read_text(encoding="utf-8")

        # Verify MockNode.contains signature is in test.patch
        self.assertIn("contains(node: MockNode | null): boolean", patch_content)

        # Static integrity check: ensure real semantic assertions are in test.patch
        required_snippets = [
            "root.contains(root)",
            "root.contains(child)",
            "root.contains(grandchild)",
            "root.contains(unrelated)",
            "root.contains(null)",
            "root.removeChild(child)",
        ]
        for snippet in required_snippets:
            self.assertIn(snippet, patch_content, f"test.patch must contain real assertion for: {snippet}")

    def test_fake_split_monolithic_with_shells_fails(self):
        """Fake split where shell modules exist but webcomponent still implements rendering and math must fail."""
        src = self.temp_repo / "src"
        (src / "picker-view.ts").write_text("export class PickerView { constructor() {} }\n", encoding="utf-8")
        (src / "picker-interaction.ts").write_text("export class PickerInteraction { constructor() {} }\n", encoding="utf-8")

        monolithic_content = """
        import { Poline } from "./index";
        import { PickerView } from "./picker-view";
        import { PickerInteraction } from "./picker-interaction";

        export class PolinePicker extends HTMLElement {
          private poline: Poline | null = null;
          private svg: SVGElement | null = null;
          private view = new PickerView();
          private interaction = new PickerInteraction();

          connectedCallback() {
            this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
            this.svg.addEventListener("pointerdown", (e) => this.handlePointerDown(e));
          }
          disconnectedCallback() { this.svg = null; }
          setPoline(p: any) { this.poline = p; }
          setAllowAddPoints(a: boolean) {}
          updateSVG() {
            if (!this.svg) return;
            const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            circle.setAttribute("cx", "50");
            circle.setAttribute("cy", "50");
            circle.setAttribute("r", "5");
            this.svg.appendChild(circle);
          }
          addPointAtPosition(x: number, y: number) { return null; }
          private handlePointerDown(e: PointerEvent) {
            const angle = Math.atan2(e.clientY, e.clientX);
          }
        }
        customElements.define("poline-picker", PolinePicker);
        """
        (src / "webcomponent.ts").write_text(monolithic_content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("responsibilities still embedded in PolinePicker", errors_str)

    def test_presentation_pointer_capture_facade_does_not_count_as_merged_interaction_ownership(self):
        """Presentation class exposing pointer-capture facade methods must not be misclassified as interaction owner."""
        src = self.temp_repo / "src"
        for f in ["picker-view.ts", "picker-interaction.ts"]:
            p = src / f
            if p.is_file():
                p.unlink()

        pres_code = """import { Poline } from "./index";

export class PickerPresentation {
  private svg: SVGElement;

  constructor() {
    this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const line = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
    line.setAttribute("class", "wheel__line");
    line.setAttribute("points", "0 0");
    this.svg.appendChild(line);
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("class", "wheel__circle");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    circle.setAttribute("r", "5");
    this.svg.appendChild(circle);
  }

  public capturePointer(id: number): void {
    this.svg.setPointerCapture(id);
  }

  public releasePointer(id: number): void {
    this.svg.releasePointerCapture(id);
  }

  public updateSVG(poline: any): void {
    if (!this.svg || !poline) return;
    const minL = "--minL";
    const maxL = "--maxL";
    const gradient = "linearGradient";
  }

  public getSvgElement(): SVGElement {
    return this.svg;
  }
}
"""
        (src / "picker-presentation.ts").write_text(pres_code, encoding="utf-8")

        int_code = """import { Poline } from "./index";
import { PickerPresentation } from "./picker-presentation";

export class PickerInteraction {
  private activePointerId: number | null = null;
  private presentation: PickerPresentation;
  private allowAddPoints = false;

  constructor(presentation: PickerPresentation) {
    this.presentation = presentation;
  }

  public bind(svg?: any): void {
    svg?.addEventListener("pointerdown", (e: any) => this.handlePointerDown(e));
    svg?.addEventListener("pointermove", (e: any) => this.handlePointerMove(e));
  }

  public unbind(): void {
    this.activePointerId = null;
  }

  public setAllowAddPoints(allow: boolean): void {
    this.allowAddPoints = allow;
  }

  private handlePointerDown(e: PointerEvent): void {
    const angle = Math.atan2(e.clientY, e.clientX);
    this.activePointerId = e.pointerId;
    this.presentation.capturePointer(e.pointerId);
  }

  private handlePointerMove(e: PointerEvent): void {
    const angle = Math.atan2(e.clientY, e.clientX);
  }
}
"""
        (src / "picker-interaction.ts").write_text(int_code, encoding="utf-8")

        wc_code = """import { Poline } from "./index";
import { PickerPresentation } from "./picker-presentation";
import { PickerInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private presentation: PickerPresentation;
  private interaction: PickerInteraction;

  connectedCallback() {
    this.presentation = new PickerPresentation();
    this.interaction = new PickerInteraction(this.presentation);
    this.interaction.bind(this.presentation.getSvgElement());
  }

  disconnectedCallback() {
    if (this.interaction) {
      this.interaction.unbind();
    }
  }

  setPoline(p: any) {
    this.poline = p;
    if (this.presentation) {
      this.presentation.updateSVG(this.poline);
    }
  }

  setAllowAddPoints(allow: boolean) {
    if (this.interaction) {
      this.interaction.setAllowAddPoints(allow);
    }
  }

  updateSVG() {
    if (!this.poline || !this.presentation.getSvgElement()) return;
    this.presentation.updateSVG(this.poline);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(
            res.get("passed"),
            f"Presentation pointer-capture facade must not be rejected as interaction owner: {res.get('errors')}",
        )
        self.assertEqual(res.get("presentationModule"), "picker-presentation.ts")
        self.assertEqual(res.get("interactionModule"), "picker-interaction.ts")

    def test_presentation_with_pointer_lifecycle_and_gesture_state_is_rejected_as_merged(self):
        """Presentation class combining SVG rendering with pointer lifecycle listeners and gesture state must be rejected."""
        src = self.temp_repo / "src"
        for f in ["picker-view.ts", "picker-interaction.ts", "picker-presentation.ts"]:
            p = src / f
            if p.is_file():
                p.unlink()

        merged_pres_code = """import { Poline } from "./index";

export class MergedPresentation {
  private svg: SVGElement;
  private activePointerId: number | null = null;

  constructor() {
    this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    circle.setAttribute("r", "5");
    this.svg.appendChild(circle);
  }

  public updateSVG(poline: any): void {
    const minL = "--minL";
    const maxL = "--maxL";
    const gradient = "linearGradient";
  }

  public bind(svg?: any): void {
    this.svg.addEventListener("pointerdown", (e: any) => {
      const angle = Math.atan2(e.clientY, e.clientX);
      this.activePointerId = e.pointerId;
    });
    this.svg.addEventListener("pointermove", (e: any) => {
      const angle = Math.atan2(e.clientY, e.clientX);
    });
  }

  public getSvgElement(): SVGElement {
    return this.svg;
  }
}
"""
        (src / "merged-presentation.ts").write_text(merged_pres_code, encoding="utf-8")

        dummy_int_code = """import { Poline } from "./index";

export class EmptyInteraction {
  public bind(svg?: any): void {}
  public unbind(): void {}
  public setAllowAddPoints(allow: boolean): void {}
}
"""
        (src / "empty-interaction.ts").write_text(dummy_int_code, encoding="utf-8")

        wc_code = """import { Poline } from "./index";
import { MergedPresentation } from "./merged-presentation";
import { EmptyInteraction } from "./empty-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private presentation: MergedPresentation;
  private interaction: EmptyInteraction;

  connectedCallback() {
    this.presentation = new MergedPresentation();
    this.interaction = new EmptyInteraction();
    this.presentation.bind(this.presentation.getSvgElement());
    this.interaction.bind(this.presentation.getSvgElement());
  }

  disconnectedCallback() {
    this.interaction.unbind();
  }

  setPoline(p: any) {
    this.poline = p;
    this.presentation.updateSVG(this.poline);
  }

  setAllowAddPoints(allow: boolean) {
    this.interaction.setAllowAddPoints(allow);
  }

  updateSVG() {
    this.presentation.updateSVG(this.poline);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertTrue(
            "combined in the same collaborator" in errors_str or "missing separation" in errors_str,
            f"Expected merged separation failure, got: {errors_str}",
        )

    def test_presentation_shell_with_facade_retaining_rendering_fails(self):
        """Empty presentation shell where facade retains SVG rendering must fail."""
        src = self.temp_repo / "src"
        (src / "picker-view.ts").write_text("export class PickerView { updateSVG() {} }\n", encoding="utf-8")
        wc_code = """import { Poline } from "./index";
import { PickerView } from "./picker-view";
import { PickerInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private view: PickerView;
  private interaction: PickerInteraction;
  private svg: SVGElement | null = null;

  connectedCallback() {
    this.view = new PickerView();
    this.interaction = new PickerInteraction(this.shadowRoot, () => this.poline, this, () => {});
    this.interaction.bind(this.svg);
  }

  disconnectedCallback() {
    if (this.interaction) this.interaction.unbind();
  }

  setPoline(p: any) { this.poline = p; }
  setAllowAddPoints(allow: boolean) { this.interaction.setAllowAddPoints(allow); }

  updateSVG() {
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", "50");
    const minL = "--minL";
  }

  addPointAtPosition(x: number, y: number) { return null; }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")
        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertTrue(
            "presentation ownership missing" in errors_str or "presentation implementation remains in coordinator" in errors_str or "responsibilities still embedded in PolinePicker" in errors_str,
            f"Expected presentation ownership/retained error, got: {errors_str}"
        )

    def test_interaction_shell_with_facade_retaining_gesture_fails(self):
        """Empty interaction shell where facade retains pointer handling and math must fail."""
        src = self.temp_repo / "src"
        (src / "picker-interaction.ts").write_text(
            "export class PickerInteraction { bind(svg: any) {} unbind() {} setAllowAddPoints(a: boolean) {} }\n",
            encoding="utf-8"
        )
        wc_code = """import { Poline } from "./index";
import { PickerView } from "./picker-view";
import { PickerInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private view: PickerView;
  private interaction: PickerInteraction;
  private activePointerId: number | null = null;

  connectedCallback() {
    this.view = new PickerView(this.shadowRoot, () => this.poline);
    this.interaction = new PickerInteraction();
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    if (this.interaction) this.interaction.unbind();
  }

  setPoline(p: any) { this.poline = p; }
  setAllowAddPoints(allow: boolean) { this.interaction.setAllowAddPoints(allow); }

  updateSVG() {
    this.view.updateSVG(this.poline);
  }

  private handlePointerDown(e: PointerEvent) {
    const angle = Math.atan2(e.clientY, e.clientX);
    this.activePointerId = e.pointerId;
  }

  addPointAtPosition(x: number, y: number) { return null; }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")
        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertTrue(
            "interaction ownership missing" in errors_str or "interaction implementation remains in coordinator" in errors_str or "responsibilities still embedded in PolinePicker" in errors_str,
            f"Expected interaction ownership/retained error, got: {errors_str}"
        )

    def test_two_shells_plus_hybrid_class_fails(self):
        """Two empty shells plus a third class containing merged implementation must fail."""
        src = self.temp_repo / "src"
        (src / "picker-view.ts").write_text("export class PickerView { updateSVG() {} }\n", encoding="utf-8")
        (src / "picker-interaction.ts").write_text("export class PickerInteraction { bind() {} unbind() {} setAllowAddPoints() {} }\n", encoding="utf-8")
        hybrid_code = """
export class HybridGodClass {
  private svg: SVGElement;
  private activePointerId: number | null = null;

  render() {
    this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", "50");
    const minL = "--minL";
  }

  handle(e: PointerEvent) {
    const angle = Math.atan2(e.clientY, e.clientX);
    this.activePointerId = e.pointerId;
  }
}
"""
        (src / "hybrid-class.ts").write_text(hybrid_code, encoding="utf-8")
        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertTrue(
            "combined in the same collaborator" in errors_str or "missing separation" in errors_str,
            f"Expected combined class error, got: {errors_str}"
        )

    def test_fake_delegation_via_misleading_method_names_fails(self):
        """Misleading method names or unrelated calls faking delegation must fail."""
        src = self.temp_repo / "src"
        wc_code = """import { Poline } from "./index";
import { PickerView } from "./picker-view";
import { PickerInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private view: PickerView;
  private interaction: PickerInteraction;

  connectedCallback() {
    this.view = new PickerView(this.shadowRoot, () => this.poline);
    this.interaction = new PickerInteraction(this.shadowRoot, () => this.poline, this, () => {});
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    if (this.interaction) this.interaction.unbind();
  }

  setPoline(p: any) { this.poline = p; }
  setAllowAddPoints(allow: boolean) { this.interaction.setAllowAddPoints(allow); }

  updateSVG() {
    this.fakeViewRendererCall();
  }

  private fakeViewRendererCall() {
    /* fake update */
  }

  addPointAtPosition(x: number, y: number) { return null; }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")
        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing coordinator delegation: PolinePicker.updateSVG() does not delegate to presentation collaborator", errors_str)

    def test_collaborator_real_but_facade_does_not_call_it_fails(self):
        """Real collaborator where coordinator completely omits calling it must fail."""
        src = self.temp_repo / "src"
        wc_code = """import { Poline } from "./index";
import { PickerView } from "./picker-view";
import { PickerInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private view: PickerView;
  private interaction: PickerInteraction;

  connectedCallback() {
    this.view = new PickerView(this.shadowRoot, () => this.poline);
    this.interaction = new PickerInteraction(this.shadowRoot, () => this.poline, this, () => {});
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    if (this.interaction) this.interaction.unbind();
  }

  setPoline(p: any) { this.poline = p; }
  setAllowAddPoints(allow: boolean) { this.interaction.setAllowAddPoints(allow); }

  updateSVG() {
    // completely empty, not calling this.view
  }

  addPointAtPosition(x: number, y: number) { return null; }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")
        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
    def test_object_literals_presentation_and_interaction_passes(self):
        """Distinct object literals for presentation and interaction with substantive logic must pass."""
        src = self.temp_repo / "src"
        pres_obj = """import { Poline } from "./index";

export const pickerView = {
  svg: null as SVGElement | null,
  init(root: any) {
    this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    circle.setAttribute("r", "5");
    this.svg.appendChild(circle);
  },
  updateSVG(p: any) {
    const minL = "--minL";
    const maxL = "--maxL";
    const gradient = "linearGradient";
  },
  getSvgElement() {
    return this.svg;
  }
};
"""
        (src / "picker-view.ts").write_text(pres_obj, encoding="utf-8")

        int_obj = """import { Poline } from "./index";

export const pickerInteraction = {
  activePointerId: null as number | null,
  allowAddPoints: false,
  bind(svg: any) {
    svg?.addEventListener("pointerdown", (e: any) => this.handlePointerDown(e));
    svg?.addEventListener("pointermove", (e: any) => this.handlePointerMove(e));
  },
  unbind() {
    this.activePointerId = null;
  },
  setAllowAddPoints(allow: boolean) {
    this.allowAddPoints = allow;
  },
  handlePointerDown(e: any) {
    const angle = Math.atan2(e.clientY, e.clientX);
    this.activePointerId = e.pointerId;
  },
  handlePointerMove(e: any) {
    const angle = Math.atan2(e.clientY, e.clientX);
  }
};
"""
        (src / "picker-interaction.ts").write_text(int_obj, encoding="utf-8")

        wc_code = """import { Poline } from "./index";
import { pickerView } from "./picker-view";
import { pickerInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private view = pickerView;
  private interaction = pickerInteraction;

  connectedCallback() {
    this.view.init(this.shadowRoot);
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    this.interaction.unbind();
  }

  setPoline(p: any) {
    this.poline = p;
    if (this.view) {
      this.view.updateSVG(this.poline);
    }
  }

  setAllowAddPoints(allow: boolean) {
    this.interaction.setAllowAddPoints(allow);
  }

  updateSVG() {
    if (!this.poline || !this.view.getSvgElement()) return;
    this.view.updateSVG(this.poline);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(
            res.get("passed"),
            f"Object literals for presentation and interaction should pass, got: {res.get('errors')}",
        )
        self.assertEqual(res.get("presentationModule"), "picker-view.ts")
        self.assertEqual(res.get("interactionModule"), "picker-interaction.ts")

    def test_factory_functions_returning_objects_passes(self):
        """Factory functions returning presentation and interaction objects must pass."""
        src = self.temp_repo / "src"
        pres_factory = """import { Poline } from "./index";

export function createPickerView(root: any) {
  let svg: SVGElement | null = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  circle.setAttribute("cx", "50");
  circle.setAttribute("cy", "50");
  circle.setAttribute("r", "5");
  svg.appendChild(circle);

  return {
    getSvgElement() { return svg; },
    updateSVG(p: any) {
      const minL = "--minL";
      const maxL = "--maxL";
      const gradient = "linearGradient";
    }
  };
}
"""
        (src / "picker-view.ts").write_text(pres_factory, encoding="utf-8")

        int_factory = """import { Poline } from "./index";

export function createPickerInteraction(root: any, polineProvider: any) {
  let activePointerId: number | null = null;
  let allowAddPoints = false;

  function handlePointerDown(e: any) {
    const angle = Math.atan2(e.clientY, e.clientX);
    activePointerId = e.pointerId;
  }
  function handlePointerMove(e: any) {
    const angle = Math.atan2(e.clientY, e.clientX);
  }

  return {
    bind(svg: any) {
      svg?.addEventListener("pointerdown", handlePointerDown);
      svg?.addEventListener("pointermove", handlePointerMove);
    },
    unbind() {
      activePointerId = null;
    },
    setAllowAddPoints(allow: boolean) {
      allowAddPoints = allow;
    }
  };
}
"""
        (src / "picker-interaction.ts").write_text(int_factory, encoding="utf-8")

        wc_code = """import { Poline } from "./index";
import { createPickerView } from "./picker-view";
import { createPickerInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private view: any;
  private interaction: any;

  connectedCallback() {
    this.view = createPickerView(this.shadowRoot);
    this.interaction = createPickerInteraction(this.shadowRoot, () => this.poline);
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    if (this.interaction) this.interaction.unbind();
  }

  setPoline(p: any) {
    this.poline = p;
    if (this.view) {
      this.view.updateSVG(this.poline);
    }
  }

  setAllowAddPoints(allow: boolean) {
    if (this.interaction) this.interaction.setAllowAddPoints(allow);
  }

  updateSVG() {
    if (!this.poline || !this.view.getSvgElement()) return;
    this.view.updateSVG(this.poline);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(
            res.get("passed"),
            f"Factory functions returning objects should pass, got: {res.get('errors')}",
        )
        self.assertEqual(res.get("presentationModule"), "picker-view.ts")
        self.assertEqual(res.get("interactionModule"), "picker-interaction.ts")

    def test_closure_based_interaction_state_passes(self):
        """Closure-based unit preserving interaction state and exposing methods must pass."""
        src = self.temp_repo / "src"
        int_closure = """import { Poline } from "./index";

export function setupInteraction(host: any, polineProvider: any) {
  let activePointerId: number | null = null;
  let allowAddPoints = false;
  let dragCount = 0;

  function onPointerDown(e: any) {
    const angle = Math.atan2(e.clientY, e.clientX);
    activePointerId = e.pointerId;
    dragCount++;
  }

  function onPointerMove(e: any) {
    const angle = Math.atan2(e.clientY, e.clientX);
  }

  return {
    bind(svg: any) {
      svg?.addEventListener("pointerdown", onPointerDown);
      svg?.addEventListener("pointermove", onPointerMove);
    },
    unbind() {
      activePointerId = null;
    },
    setAllowAddPoints(allow: boolean) {
      allowAddPoints = allow;
    },
    getDragCount() {
      return dragCount;
    }
  };
}
"""
        (src / "picker-interaction.ts").write_text(int_closure, encoding="utf-8")

        wc_code = """import { Poline } from "./index";
import { PickerView } from "./picker-view";
import { setupInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private view: PickerView;
  private interaction: any;

  connectedCallback() {
    this.view = new PickerView(this.shadowRoot, () => this.poline);
    this.interaction = setupInteraction(this, () => this.poline);
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    if (this.interaction) this.interaction.unbind();
  }

  setPoline(p: any) {
    this.poline = p;
    if (this.view) {
      this.view.updateSVG(this.poline);
    }
  }

  setAllowAddPoints(allow: boolean) {
    if (this.interaction) this.interaction.setAllowAddPoints(allow);
  }

  updateSVG() {
    if (!this.poline || !this.view.getSvgElement()) return;
    this.view.updateSVG(this.poline);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(
            res.get("passed"),
            f"Closure-based interaction state unit should pass, got: {res.get('errors')}",
        )
        self.assertEqual(res.get("interactionModule"), "picker-interaction.ts")

    def test_empty_shell_objects_fails(self):
        """Empty shell objects lacking substantive state and methods must fail."""
        src = self.temp_repo / "src"
        (src / "picker-view.ts").write_text("export const pickerView = {};\n", encoding="utf-8")
        (src / "picker-interaction.ts").write_text("export const pickerInteraction = {};\n", encoding="utf-8")

        wc_code = """import { Poline } from "./index";
import { pickerView } from "./picker-view";
import { pickerInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private view = pickerView;
  private interaction = pickerInteraction;

  connectedCallback() {}
  disconnectedCallback() {}
  setPoline(p: any) { this.poline = p; }
  setAllowAddPoints(allow: boolean) {}
  updateSVG() {}
  addPointAtPosition(x: number, y: number) { return null; }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertTrue(
            "missing presentation separation" in errors_str or "missing interaction separation" in errors_str,
            f"Expected separation failure for empty shell objects, got: {errors_str}",
        )

    def test_single_object_combining_presentation_and_interaction_fails(self):
        """Single hybrid object combining presentation and interaction must fail."""
        src = self.temp_repo / "src"
        (src / "picker-view.ts").unlink()
        (src / "picker-interaction.ts").unlink()

        hybrid_obj = """import { Poline } from "./index";

export const hybridPicker = {
  svg: null as any,
  activePointerId: null as number | null,

  init() {
    this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    circle.setAttribute("r", "5");
    this.svg.appendChild(circle);
  },
  updateSVG(p: any) {
    const minL = "--minL";
    const maxL = "--maxL";
    const gradient = "linearGradient";
  },
  bind(svg: any) {
    svg?.addEventListener("pointerdown", (e: any) => {
      const angle = Math.atan2(e.clientY, e.clientX);
      this.activePointerId = e.pointerId;
    });
  },
  unbind() {
    this.activePointerId = null;
  },
  setAllowAddPoints(allow: boolean) {}
};
"""
        (src / "hybrid-picker.ts").write_text(hybrid_obj, encoding="utf-8")

        wc_code = """import { Poline } from "./index";
import { hybridPicker } from "./hybrid-picker";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private hybrid = hybridPicker;

  connectedCallback() {
    this.hybrid.init();
    this.hybrid.bind(this.shadowRoot);
  }
  disconnectedCallback() {
    this.hybrid.unbind();
  }
  setPoline(p: any) {
    this.poline = p;
    this.hybrid.updateSVG(p);
  }
  setAllowAddPoints(allow: boolean) {
    this.hybrid.setAllowAddPoints(allow);
  }
  updateSVG() {
    this.hybrid.updateSVG(this.poline);
  }
  addPointAtPosition(x: number, y: number) { return null; }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertTrue(
            "combined in the same collaborator" in errors_str
            or "missing presentation separation" in errors_str
            or "missing interaction separation" in errors_str,
            f"Expected failure for hybrid object, got: {errors_str}",
        )

    def test_objects_with_implementation_but_facade_not_calling_fails(self):
        """Objects with implementation where facade omits delegation must fail."""
        src = self.temp_repo / "src"
        pres_obj = """import { Poline } from "./index";

export const pickerView = {
  svg: null as SVGElement | null,
  init(root: any) {
    this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", "50");
    this.svg.appendChild(circle);
  },
  updateSVG(p: any) {
    const minL = "--minL";
    const maxL = "--maxL";
    const gradient = "linearGradient";
  },
  getSvgElement() {
    return this.svg;
  }
};
"""
        (src / "picker-view.ts").write_text(pres_obj, encoding="utf-8")

        int_obj = """import { Poline } from "./index";

export const pickerInteraction = {
  activePointerId: null as number | null,
  bind(svg: any) {
    svg?.addEventListener("pointerdown", (e: any) => {
      const angle = Math.atan2(e.clientY, e.clientX);
      this.activePointerId = e.pointerId;
    });
  },
  unbind() {
    this.activePointerId = null;
  },
  setAllowAddPoints(allow: boolean) {}
};
"""
        (src / "picker-interaction.ts").write_text(int_obj, encoding="utf-8")

        wc_code = """import { Poline } from "./index";
import { pickerView } from "./picker-view";
import { pickerInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private view = pickerView;
  private interaction = pickerInteraction;

  connectedCallback() {
    this.view.init(this.shadowRoot);
    this.interaction.bind(this.view.getSvgElement());
  }

  disconnectedCallback() {
    this.interaction.unbind();
  }

  setPoline(p: any) { this.poline = p; }
  setAllowAddPoints(allow: boolean) { this.interaction.setAllowAddPoints(allow); }

  updateSVG() {
    // Omitting delegation to this.view.updateSVG
  }

  addPointAtPosition(x: number, y: number) { return null; }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(wc_code, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing coordinator delegation: PolinePicker.updateSVG() does not delegate to presentation collaborator", errors_str)

    def test_presentation_and_interaction_retained_in_facade_fails(self):
        """Presentation and interaction retained inside facade class must fail."""
        src = self.temp_repo / "src"
        (src / "picker-view.ts").write_text("export const dummyView = {};\n", encoding="utf-8")
        (src / "picker-interaction.ts").write_text("export const dummyInteraction = {};\n", encoding="utf-8")

        monolithic_facade = """import { Poline } from "./index";
import { dummyView } from "./picker-view";
import { dummyInteraction } from "./picker-interaction";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private svg: SVGElement | null = null;
  private activePointerId: number | null = null;

  connectedCallback() {
    this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    circle.setAttribute("r", "5");
    this.svg.appendChild(circle);
    this.svg.addEventListener("pointerdown", (e) => this.handlePointerDown(e));
  }

  disconnectedCallback() {
    this.svg = null;
  }

  setPoline(p: any) { this.poline = p; }
  setAllowAddPoints(a: boolean) {}

  updateSVG() {
    if (!this.svg) return;
    const minL = "--minL";
    const maxL = "--maxL";
    const gradient = "linearGradient";
  }

  addPointAtPosition(x: number, y: number) { return null; }

  private handlePointerDown(e: PointerEvent) {
    const angle = Math.atan2(e.clientY, e.clientX);
    this.activePointerId = e.pointerId;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        (src / "webcomponent.ts").write_text(monolithic_facade, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("responsibilities still embedded in PolinePicker", errors_str)

    def test_dead_pointerdown_binding_fails_architecture_node(self):
        """Dead pointerdown binding where listener is a no-op or disconnected from interaction logic must fail architecture node."""
        src = self.temp_repo / "src"
        int_p = src / "picker-interaction.ts"
        int_content = int_p.read_text(encoding="utf-8")
        dead_content = int_content.replace(
            'svg?.addEventListener("pointerdown", (e: any) => this.handlePointerDown(e));',
            'svg?.addEventListener("pointerdown", () => {\n    void 0;\n  });'
        )
        self.assertNotEqual(int_content, dead_content, "Replacement should modify pointerdown listener")
        int_p.write_text(dead_content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"), "Dead pointerdown binding must fail architecture analysis")
        errors_str = " ".join(res.get("errors", []))
        self.assertTrue(
            "pointerdown" in errors_str or "event delegation" in errors_str,
            f"Expected error message indicating pointerdown event delegation failure, got: {errors_str}"
        )
        # Prove that presentation and interaction modules were NOT deleted or empty shells
        self.assertEqual(res.get("presentationModule"), "picker-view.ts")
        self.assertEqual(res.get("interactionModule"), "picker-interaction.ts")

        # Verify F2P node conversion results in 'failed' status
        entry = create_architecture_f2p_entry(res.get("passed"), errors_str, res.get("details", {}))
        self.assertEqual(entry["testId"], ARCHITECTURE_F2P_NODE_ID)
        self.assertEqual(entry["status"], "failed")
        self.assertTrue(
            "pointerdown" in entry["message"] or "event delegation" in entry["message"],
            f"Expected failed CTRF entry message to state pointerdown/delegation failure, got: {entry['message']}"
        )

    def test_pointerdown_delegating_to_empty_interaction_method_fails(self):
        """Pointerdown delegating directly to empty interaction method (noop) must fail architecture node."""
        src = self.temp_repo / "src"
        int_p = src / "picker-interaction.ts"
        int_content = int_p.read_text(encoding="utf-8")
        int_content = int_content.replace(
            'svg?.addEventListener("pointerdown", (e: any) => this.handlePointerDown(e));',
            '/* listener registered by coordinator */',
        )
        int_content = int_content.replace(
            'public setAllowAddPoints(allow: boolean): void {',
            'public noop(event: any): void {}\n\n  public setAllowAddPoints(allow: boolean): void {',
        )
        int_p.write_text(int_content, encoding="utf-8")

        wc_p = src / "webcomponent.ts"
        wc_content = wc_p.read_text(encoding="utf-8")
        wc_content = wc_content.replace(
            'this.interaction.bind(this.view.getSvgElement());',
            'const svg = this.view.getSvgElement();\n    svg?.addEventListener("pointerdown", (event: any) => {\n      this.interaction.noop(event);\n    });\n    this.interaction.bind(svg);',
        )
        wc_p.write_text(wc_content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing interaction event delegation", errors_str)
        self.assertEqual(res.get("presentationModule"), "picker-view.ts")
        self.assertEqual(res.get("interactionModule"), "picker-interaction.ts")

    def test_pointerdown_facade_wrapper_to_empty_interaction_method_fails(self):
        """Facade wrapper delegating to empty interaction method (noop) must fail architecture node."""
        src = self.temp_repo / "src"
        int_p = src / "picker-interaction.ts"
        int_content = int_p.read_text(encoding="utf-8")
        int_content = int_content.replace(
            'svg?.addEventListener("pointerdown", (e: any) => this.handlePointerDown(e));',
            '/* listener registered by coordinator */',
        )
        int_content = int_content.replace(
            'public setAllowAddPoints(allow: boolean): void {',
            'public noop(event: any): void {}\n\n  public setAllowAddPoints(allow: boolean): void {',
        )
        int_p.write_text(int_content, encoding="utf-8")

        wc_p = src / "webcomponent.ts"
        wc_content = wc_p.read_text(encoding="utf-8")
        wc_content = wc_content.replace(
            'setAllowAddPoints(allow: boolean) {',
            'private onPointerDown(event: any): void {\n    this.interaction.noop(event);\n  }\n\n  setAllowAddPoints(allow: boolean) {',
        )
        wc_p.write_text(wc_content, encoding="utf-8")
        wc_content = wc_p.read_text(encoding="utf-8")
        wc_content = wc_content.replace(
            'this.interaction.bind(this.view.getSvgElement());',
            'const svg = this.view.getSvgElement();\n    svg?.addEventListener("pointerdown", (event: any) => {\n      this.onPointerDown(event);\n    });\n    this.interaction.bind(svg);',
        )
        wc_p.write_text(wc_content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertFalse(res.get("passed"))
        errors_str = " ".join(res.get("errors", []))
        self.assertIn("missing interaction event delegation", errors_str)

    def test_method_reference_delegation_passes(self):
        """Direct method reference delegation to interaction collaborator must pass architecture analysis."""
        src = self.temp_repo / "src"
        int_p = src / "picker-interaction.ts"
        int_content = int_p.read_text(encoding="utf-8")
        method_ref_content = int_content.replace(
            'svg?.addEventListener("pointerdown", (e: any) => this.handlePointerDown(e));',
            'svg?.addEventListener("pointerdown", this.handlePointerDown);'
        )
        self.assertNotEqual(int_content, method_ref_content)
        int_p.write_text(method_ref_content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Method reference delegation should pass, got errors: {res.get('errors')}")

    def test_facade_arrow_callback_delegation_passes(self):
        """Facade registering pointerdown listener delegating to interaction collaborator must pass."""
        src = self.temp_repo / "src"
        int_p = src / "picker-interaction.ts"
        int_content = int_p.read_text(encoding="utf-8")
        int_content = int_content.replace(
            'svg?.addEventListener("pointerdown", (e: any) => this.handlePointerDown(e));',
            '/* listener registered by coordinator */'
        )
        int_p.write_text(int_content, encoding="utf-8")

        wc_p = src / "webcomponent.ts"
        wc_content = wc_p.read_text(encoding="utf-8")
        wc_content = wc_content.replace(
            'this.interaction.bind(this.view.getSvgElement());',
            'const svg = this.view.getSvgElement();\n    svg?.addEventListener("pointerdown", (event: any) => {\n      this.interaction.handlePointerDown(event);\n    });\n    this.interaction.bind(svg);'
        )
        wc_p.write_text(wc_content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Facade arrow callback delegation should pass, got errors: {res.get('errors')}")

    def test_renamed_interaction_method_passes(self):
        """Renamed interaction method (e.g. beginGesture) with substantive logic must pass architecture analysis."""
        src = self.temp_repo / "src"
        int_p = src / "picker-interaction.ts"
        int_content = int_p.read_text(encoding="utf-8")
        renamed_content = int_content.replace(
            'this.handlePointerDown(e)',
            'this.beginGesture(e)'
        ).replace(
            'private handlePointerDown(e: PointerEvent): void {',
            'private beginGesture(e: PointerEvent): void {'
        )
        self.assertNotEqual(int_content, renamed_content)
        int_p.write_text(renamed_content, encoding="utf-8")

        res = self._run_analyzer(src)
        self.assertTrue(res.get("passed"), f"Renamed interaction method should pass, got errors: {res.get('errors')}")



class TestBaselineMonolithicBehavior(unittest.TestCase):
    """Test that baseline monolithic implementation fails architecture F2P node without failing Hard Gate."""

    def setUp(self):
        self.repo_dir = SOURCE_DIR.resolve()
        self.cmd_env = get_environment_with_node_modules(self.repo_dir)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_repo = Path(self.temp_dir.name)
        self.src = self.temp_repo / "src"
        self.src.mkdir(parents=True)
        # Create explicit monolithic baseline fixture
        (self.src / "index.ts").write_text("export class Poline {}\nexport class ColorPoint {}\n", encoding="utf-8")
        monolithic_content = """import { Poline } from "./index";

export class PolinePicker extends HTMLElement {
  private poline: Poline | null = null;
  private svg: SVGElement | null = null;
  private activePointerId: number | null = null;

  connectedCallback() {
    this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    this.svg.addEventListener("pointerdown", (e) => this.handlePointerDown(e));
  }

  disconnectedCallback() {
    this.svg = null;
  }

  setPoline(p: any) {
    this.poline = p;
  }

  setAllowAddPoints(allow: boolean) {}

  updateSVG() {
    if (!this.svg) return;
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    circle.setAttribute("r", "5");
    this.svg.appendChild(circle);
  }

  addPointAtPosition(x: number, y: number) {
    return null;
  }

  private handlePointerDown(e: PointerEvent) {
    const angle = Math.atan2(e.clientY, e.clientX);
    this.activePointerId = e.pointerId;
  }
}
customElements.define("poline-picker", PolinePicker);
"""
        (self.src / "webcomponent.ts").write_text(monolithic_content, encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_unmodified_baseline_monolithic_fails_architecture_f2p_node(self):
        """Monolithic implementation must fail the architecture F2P node with detailed findings."""
        passed, msg, details = check_architecture_separation(self.temp_repo, self.cmd_env)
        self.assertFalse(passed, "Baseline monolithic code must fail architecture separation check")
        self.assertFalse(details.get("is_infra", False), "Must not be classified as infrastructure failure")

        # Convert to F2P node entry
        entry = create_architecture_f2p_entry(passed, msg, details)
        self.assertEqual(entry["testId"], ARCHITECTURE_F2P_NODE_ID)
        self.assertEqual(entry["status"], "failed")
        self.assertEqual(entry["extra"]["deepswe"]["group"], "F2P")
        self.assertIn("embedded in PolinePicker", entry["message"])

    def test_failed_architecture_f2p_does_not_fail_hard_gate(self):
        """Verify that a candidate failing architecture separation does not fail Hard Gate."""
        # 1. architecture_separation_integrity must not be in REQUIRED_HARD_GATE_NODE_IDS
        self.assertNotIn(
            "architecture_separation_integrity",
            REQUIRED_HARD_GATE_NODE_IDS,
            "architecture_separation_integrity must be removed from REQUIRED_HARD_GATE_NODE_IDS",
        )

        # 2. Check architecture separation fails on monolithic fixture
        passed, msg, details = check_architecture_separation(self.temp_repo, self.cmd_env)
        self.assertFalse(passed)

        # 3. Simulate Hard Gate report assembly and verify Hard Gate passed is True
        nodes = [
            NodeResult(nid, True, f"Check for {nid}", "passed")
            for nid in REQUIRED_HARD_GATE_NODE_IDS
        ]
        p2p_results = [
            {"testId": "tests/index.test.ts::test1", "name": "test1", "status": "passed", "duration": 1}
        ]
        report_data = {
            "passed": True,
            "apply_failed": False,
            "failed_nodes": [],
            "nodes": [n.to_dict() for n in nodes],
            "architecture_result": {
                "node_id": ARCHITECTURE_F2P_NODE_ID,
                "passed": passed,
                "message": msg,
                "details": details,
            },
            "p2p_summary": {"total": 1, "passed": 1, "failed": 0},
            "p2p_results": p2p_results,
            "compile_paths": ["src/"],
            "candidate_changed_paths": ["src/webcomponent.ts"],
            "protected_changes": [],
            "test_bypass": {"detected": False, "findings": []},
            "cheat_reasons": [],
            "compile_errors": {},
            "infra_errors": {},
        }

        # Hard Gate schema validation must pass
        valid, errors = validate_hard_gate_schema(
            report_data,
            expected_p2p_list=["tests/index.test.ts::test1"],
            expected_cheat_nodes=REQUIRED_CHEAT_NODE_IDS,
        )
        self.assertTrue(valid, f"Hard Gate schema should be valid: {errors}")
        self.assertTrue(report_data["passed"], "Hard Gate must pass even when architecture separation failed")
        self.assertEqual(report_data["failed_nodes"], [], "Architecture failure must not appear in hard gate failed_nodes")


if __name__ == "__main__":
    unittest.main()
