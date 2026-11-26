#!/usr/bin/env python3
"""Deterministic Hard Gate runner for PolinePicker refactoring task."""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any

EXPECTED_INDEX_TEST_SHA256 = "2d8513167cfb854f1ab92c09d49ab7c1cb3a47f802c88e03c94d88fe3f5e53ed"
ORIGINAL_SRC_INDEX_SHA256 = "3463c7d11cedc4b81628cb32f7d162d95b162c11a45369a0c42363b46f05b9f2"
EXPECTED_ORIGINAL_P2P_COUNT = 78
EXPECTED_P2P_COUNT = 78

EXPLICIT_PROTECTED_FILES = {
    "tests/index.test.ts",
    "tests/grader.py",
    "tests/test.sh",
    "tests/config.json",
    "build.js",
    "package.json",
    "package-lock.json",
    "tsconfig.json",
    ".eslintrc",
    ".prettierrc.json",
    "tea.yaml",
    "README.md",
    "LICENSE",
    ".gitignore",
}

PROTECTED_DIRECTORIES = (
    "case/",
    "tests/verifier/",
    "tests/verify/",
    ".github/",
    ".git/",
)

DISALLOWED_PATTERNS = [
    (r"\b(?:it|test|describe)\s*\.\s*(?:only|skip|todo)\b", "test skip/only/todo modifier"),
    (r"\b(?:fit|fdescribe|xit|xdescribe)\s*\(", "focused/skipped test helper"),
    (r"/\*\s*istanbul\s+ignore\b", "istanbul coverage ignore"),
]

EVAL_BYPASS_PATTERNS = [
    r"__DEEPSWE__",
    r"DF_HARBOR",
    r"/logs/verifier",
    r"hard-gate\.json",
    r"ctrf\.json",
    r"reward\.json",
    r"grader\.py",
    r"verifier\.py",
    r"hardgate\.py",
]

ARCHITECTURE_F2P_NODE_ID = "F2P::architecture::presentation_interaction_and_coordinator_are_separated"

REQUIRED_HARD_GATE_NODE_IDS = [
    "candidate_patch_apply",
    "repository_baseline_integrity",
    "project_configuration_integrity",
    "build_dependency_integrity",
    "p2p_manifest_integrity",
    "config_p2p_integrity",
    "anti_cheat_protected_paths",
    "anti_cheat_test_tampering",
    "anti_cheat_test_bypass",
    "anti_cheat_scope_restriction",
    "anti_cheat_eval_bypass",
    "anti_cheat_dependency_tampering",
    "typescript_typecheck",
    "eslint_lint_check",
    "prettier_format_check",
    "production_build",
    "test_collection_integrity",
    "test_collection_count",
    "p2p_execution_integrity",
    "node_result_uniqueness",
    "report_schema_integrity",
]

REQUIRED_CHEAT_NODE_IDS = [
    "anti_cheat_protected_paths",
    "anti_cheat_test_tampering",
    "anti_cheat_test_bypass",
    "anti_cheat_scope_restriction",
    "anti_cheat_eval_bypass",
    "anti_cheat_dependency_tampering",
]


class NodeResult:
    def __init__(
        self,
        node_id: str,
        passed: bool,
        description: str,
        message: str = "",
        details: dict[str, Any] | None = None,
    ):
        self.node_id = node_id
        self.passed = passed
        self.description = description
        self.message = message
        self.details = details or {}

    def to_dict(self) -> dict[str, Any]:
        res = {
            "node_id": self.node_id,
            "status": "passed" if self.passed else "failed",
            "description": self.description,
            "message": self.message,
        }
        if self.details:
            res["details"] = self.details
        return res


def compute_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def find_p2p_manifest(config_path: Path) -> Path | None:
    candidates = [
        config_path.parent / "verifier" / "p2p_select.txt",
        Path(__file__).parent / "p2p_select.txt",
        Path("/tests/verifier/p2p_select.txt"),
    ]
    for c in candidates:
        if c.is_file():
            return c
    return None


def find_source_manifest(repo_dir: Path, config_path: Path) -> Path | None:
    candidates = [
        repo_dir / "source-manifest.json",
        repo_dir.parent / "source-manifest.json",
        config_path.resolve().parents[2] / "source-manifest.json" if len(config_path.resolve().parents) > 2 else None,
        Path("/workspace/source-manifest.json"),
        Path("/workspace/repo/source-manifest.json"),
    ]
    for c in candidates:
        if c and c.is_file():
            return c
    return None


def get_environment_with_node_modules(repo_dir: Path) -> dict[str, str]:
    env = dict(os.environ)
    node_bin = repo_dir / "node_modules" / ".bin"
    current_path = env.get("PATH", "")
    if node_bin.is_dir():
        env["PATH"] = f"{node_bin}:{current_path}"
    node_modules = repo_dir / "node_modules"
    if node_modules.is_dir():
        curr_node_path = env.get("NODE_PATH", "")
        if curr_node_path:
            env["NODE_PATH"] = f"{node_modules.resolve()}:{curr_node_path}"
        else:
            env["NODE_PATH"] = str(node_modules.resolve())
    return env


AST_ANALYZER_SCRIPT = r"""
const ts = require("typescript");
const fs = require("fs");
const path = require("path");

function getBaseReceiver(expr) {
  let curr = expr;
  while (curr) {
    if (ts.isCallExpression(curr)) {
      curr = curr.expression;
    } else if (ts.isPropertyAccessExpression(curr) || ts.isElementAccessExpression(curr)) {
      curr = curr.expression;
    } else {
      break;
    }
  }
  if (ts.isIdentifier(curr)) {
    return curr.text;
  }
  return null;
}

function getAccessedProperty(expr) {
  if (ts.isPropertyAccessExpression(expr)) {
    return expr.name.text;
  }
  if (ts.isElementAccessExpression(expr) && expr.argumentExpression && ts.isStringLiteral(expr.argumentExpression)) {
    return expr.argumentExpression.text;
  }
  return null;
}

function scanFileForBypass(filePath, content) {
  const sf = ts.createSourceFile(filePath, content, ts.ScriptTarget.Latest, true);
  const findings = [];

  const TARGET_RECEIVERS = new Set(["test", "it", "describe", "suite", "context"]);
  const TARGET_PROPS = new Set(["only", "skip", "todo"]);
  const DIRECT_BYPASS_FUNCS = new Set(["fit", "fdescribe", "xit", "xdescribe"]);

  function visit(node) {
    if (ts.isCallExpression(node)) {
      const expr = node.expression;
      if (ts.isIdentifier(expr) && DIRECT_BYPASS_FUNCS.has(expr.text)) {
        const line = sf.getLineAndCharacterOfPosition(node.getStart(sf)).line + 1;
        findings.push("Direct focused/skipped test helper '" + expr.text + "(...)' at line " + line);
      }
      const prop = getAccessedProperty(expr);
      if (prop && TARGET_PROPS.has(prop)) {
        const base = getBaseReceiver(expr);
        if (base && TARGET_RECEIVERS.has(base)) {
          const line = sf.getLineAndCharacterOfPosition(node.getStart(sf)).line + 1;
          findings.push("Disallowed test modifier '" + base + "." + prop + "(...)' at line " + line);
        }
      }
    } else if (ts.isPropertyAccessExpression(node) || ts.isElementAccessExpression(node)) {
      if (!ts.isCallExpression(node.parent) || node.parent.expression !== node) {
        const prop = getAccessedProperty(node);
        if (prop && TARGET_PROPS.has(prop)) {
          const base = getBaseReceiver(node);
          if (base && TARGET_RECEIVERS.has(base)) {
            const line = sf.getLineAndCharacterOfPosition(node.getStart(sf)).line + 1;
            findings.push("Disallowed test modifier access '" + base + "." + prop + "' at line " + line);
          }
        }
      }
    }

    ts.forEachChild(node, visit);
  }

  visit(sf);
  return findings;
}

function getAllSourceFiles(dir) {
  const files = [];
  function walk(curr) {
    const entries = fs.readdirSync(curr, { withFileTypes: true });
    for (const ent of entries) {
      const full = path.join(curr, ent.name);
      if (ent.isDirectory()) {
        if (ent.name !== "node_modules" && ent.name !== ".git") {
          walk(full);
        }
      } else if (ent.isFile() && (ent.name.endsWith(".ts") || ent.name.endsWith(".js"))) {
        if (!ent.name.endsWith(".d.ts")) {
          files.push(full);
        }
      }
    }
  }
  walk(dir);
  return files;
}

function resolveImportPath(fromFile, specifier, srcDir) {
  if (!specifier.startsWith("./") && !specifier.startsWith("../")) return null;
  const base = path.resolve(path.dirname(fromFile), specifier);
  const candidates = [
    base,
    base + ".ts",
    base + ".js",
    path.join(base, "index.ts"),
    path.join(base, "index.js")
  ];
  for (const c of candidates) {
    if (fs.existsSync(c) && fs.statSync(c).isFile()) {
      return path.resolve(c);
    }
  }
  return null;
}

function buildImportGraph(files, srcDir) {
  const graph = new Map();
  for (const f of files) {
    const resolvedF = path.resolve(f);
    graph.set(resolvedF, new Set());
    const content = fs.readFileSync(f, "utf8");
    const sf = ts.createSourceFile(path.basename(f), content, ts.ScriptTarget.Latest, true);
    sf.statements.forEach(stmt => {
      if (ts.isImportDeclaration(stmt) && stmt.moduleSpecifier && ts.isStringLiteral(stmt.moduleSpecifier)) {
        const spec = stmt.moduleSpecifier.text;
        const target = resolveImportPath(resolvedF, spec, srcDir);
        if (target && target !== resolvedF) {
          graph.get(resolvedF).add(target);
        }
      } else if (ts.isExportDeclaration(stmt) && stmt.moduleSpecifier && ts.isStringLiteral(stmt.moduleSpecifier)) {
        const spec = stmt.moduleSpecifier.text;
        const target = resolveImportPath(resolvedF, spec, srcDir);
        if (target && target !== resolvedF) {
          graph.get(resolvedF).add(target);
        }
      }
    });
  }
  return graph;
}

function getReachableFiles(startFile, graph) {
  const reachable = new Set();
  const queue = [startFile];
  while (queue.length > 0) {
    const curr = queue.shift();
    if (!reachable.has(curr)) {
      reachable.add(curr);
      const neighbors = graph.get(curr);
      if (neighbors) {
        for (const n of neighbors) {
          if (!reachable.has(n)) {
            queue.push(n);
          }
        }
      }
    }
  }
  return reachable;
}

function extractFeaturesFromNode(node, sf) {
  let hasSvgCreation = false;
  let hasSvgAttributeUpdate = false;
  let hasGradientOrStyling = false;
  let hasPointerEventHandling = false;
  let hasRotaryOrDragMath = false;
  let hasHitTesting = false;
  let hasInteractionState = false;

  function visit(n) {
    const text = n.getText(sf);
    if (ts.isCallExpression(n)) {
      const callText = n.expression.getText(sf);
      if (callText.includes("createElementNS") || callText.includes("createElement")) {
        if (text.includes("svg") || text.includes("polyline") || text.includes("circle") || text.includes("path") || text.includes("g")) {
          hasSvgCreation = true;
        }
      }
      if (callText.includes("setAttribute") || callText.includes("setAttributeNS")) {
        if (text.includes("points") || text.includes("cx") || text.includes("cy") || text.includes("r") || text.includes("d") || text.includes("viewBox")) {
          hasSvgAttributeUpdate = true;
        }
      }
    }
    if (text.includes("--minL") || text.includes("--maxL") || text.includes("linearGradient") || text.includes("gradient") || text.includes("invertedLightness")) {
      hasGradientOrStyling = true;
    }
    if (text.includes("wheel__line") || text.includes("wheel__anchor") || text.includes("wheel__point") || text.includes("wheel__ring-group") || text.includes("wheel__saturation-rings")) {
      hasSvgAttributeUpdate = true;
    }

    if (/\b(?:on)?pointer(?:down|move|up|cancel)\b/i.test(text) || text.includes("pointerId") || text.includes("pointerdown") || text.includes("pointermove") || text.includes("pointerup") || text.includes("pointercancel") || text.includes("lostpointercapture")) {
      hasPointerEventHandling = true;
    }
    if (text.includes("Math.atan2") || text.includes("ROTARY_TURNS") || text.includes("accumulatedAngle") || text.includes("deltaAngle") || text.includes("shiftKey")) {
      hasRotaryOrDragMath = true;
    }
    if (text.includes("ringOuterRadius") || text.includes("anchorRadius") || text.includes("pickRing") || text.includes("pickAnchor") || text.includes("distance") || text.includes("hitTest")) {
      hasHitTesting = true;
    }
    if (text.includes("activePointerId") || text.includes("ringAdjust") || text.includes("isDragging") || text.includes("isAdjusting") || text.includes("currentPoint") || text.includes("ringHoverIndex")) {
      hasInteractionState = true;
    }

    ts.forEachChild(n, visit);
  }

  visit(node);
  return { hasSvgCreation, hasSvgAttributeUpdate, hasGradientOrStyling, hasPointerEventHandling, hasRotaryOrDragMath, hasHitTesting, hasInteractionState };
}

function analyzeRepoArchitecture(srcDir) {
  const result = {
    passed: true,
    presentationModule: null,
    interactionModule: null,
    errors: [],
    details: {}
  };

  const webcomponentPath = path.resolve(srcDir, "webcomponent.ts");
  if (!fs.existsSync(webcomponentPath)) {
    result.passed = false;
    result.errors.push("missing coordinator: src/webcomponent.ts does not exist");
    return result;
  }

  const wcContent = fs.readFileSync(webcomponentPath, "utf8");
  const wcSf = ts.createSourceFile("webcomponent.ts", wcContent, ts.ScriptTarget.Latest, true);

  let polinePickerClass = null;
  wcSf.statements.forEach(stmt => {
    if (ts.isClassDeclaration(stmt)) {
      const name = stmt.name ? stmt.name.text : "";
      if (name === "PolinePicker" || (stmt.heritageClauses && stmt.heritageClauses.some(h => h.getText(wcSf).includes("HTMLElement")))) {
        polinePickerClass = stmt;
      }
    }
  });

  if (!polinePickerClass) {
    result.passed = false;
    result.errors.push("missing coordinator: PolinePicker class extending HTMLElement not found in webcomponent.ts");
    return result;
  }

  const methodNames = new Set();
  polinePickerClass.members.forEach(member => {
    if (ts.isMethodDeclaration(member) && member.name) {
      methodNames.add(member.name.getText(wcSf));
    } else if (ts.isPropertyDeclaration(member) && member.name) {
      if (member.initializer && (ts.isArrowFunction(member.initializer) || ts.isFunctionExpression(member.initializer))) {
        methodNames.add(member.name.getText(wcSf));
      }
    }
  });

  const requiredMethods = ["connectedCallback", "disconnectedCallback", "setPoline", "setAllowAddPoints", "updateSVG", "addPointAtPosition"];
  const missingMethods = requiredMethods.filter(m => !methodNames.has(m));
  if (missingMethods.length > 0) {
    result.passed = false;
    result.errors.push("missing coordinator facade methods: PolinePicker is missing required methods [" + missingMethods.join(", ") + "]");
  }

  const allSourceFiles = getAllSourceFiles(srcDir).map(f => path.resolve(f));
  const importGraph = buildImportGraph(allSourceFiles, srcDir);

  // Check top-level mutable state
  for (const f of allSourceFiles) {
    if (f.endsWith("index.ts") || f.endsWith("index.js")) continue;
    const content = fs.readFileSync(f, "utf8");
    const sf = ts.createSourceFile(path.basename(f), content, ts.ScriptTarget.Latest, true);
    const globalMutableVars = [];
    sf.statements.forEach(stmt => {
      if (ts.isVariableStatement(stmt)) {
        const isConst = (stmt.declarationList.flags & ts.NodeFlags.Const) !== 0;
        if (!isConst) {
          stmt.declarationList.declarations.forEach(decl => {
            const varName = decl.name.getText(sf);
            globalMutableVars.push(varName);
          });
        }
      }
    });
    if (globalMutableVars.length > 0) {
      result.passed = false;
      const relPath = path.relative(srcDir, f);
      result.errors.push("global or shared mutable state introduced: top-level mutable variable(s) [" + globalMutableVars.join(", ") + "] in " + relPath);
    }
  }

  // Anti-monolithic check: PolinePicker class itself must NOT retain embedded presentation or interaction logic
  const ppFeat = extractFeaturesFromNode(polinePickerClass, wcSf);
  if (ppFeat.hasSvgCreation || (ppFeat.hasSvgAttributeUpdate && ppFeat.hasGradientOrStyling)) {
    result.passed = false;
    result.errors.push("responsibilities still embedded in PolinePicker: presentation implementation remains in coordinator (SVG creation or DOM rendering logic directly implemented in PolinePicker)");
  }
  if (ppFeat.hasRotaryOrDragMath || ppFeat.hasHitTesting || (ppFeat.hasPointerEventHandling && ppFeat.hasInteractionState)) {
    result.passed = false;
    result.errors.push("responsibilities still embedded in PolinePicker: interaction implementation remains in coordinator (pointer gesture handling, math, or interaction state directly implemented in PolinePicker)");
  }

  // Local imports from webcomponent.ts
  const localImports = [];
  const localImportedFiles = new Set();
  wcSf.statements.forEach(stmt => {
    if (ts.isImportDeclaration(stmt) && stmt.moduleSpecifier && ts.isStringLiteral(stmt.moduleSpecifier)) {
      const specifier = stmt.moduleSpecifier.text;
      const targetPath = resolveImportPath(webcomponentPath, specifier, srcDir);
      if (targetPath && targetPath !== webcomponentPath) {
        const base = path.basename(targetPath);
        if (base !== "index.ts" && base !== "index.js") {
          localImports.push({ specifier, targetPath, importClause: stmt.importClause });
          localImportedFiles.add(targetPath);
        }
      }
    }
  });

  // Collect candidate collaborator units (classes, object literals, factory functions, closures) across all source files
  const collaboratorUnits = [];
  const collaboratorFileSet = new Set();
  localImportedFiles.forEach(f => collaboratorFileSet.add(f));

  for (const f of allSourceFiles) {
    if (f.endsWith("index.ts") || f.endsWith("index.js")) continue;
    const content = fs.readFileSync(f, "utf8");
    const sf = ts.createSourceFile(path.basename(f), content, ts.ScriptTarget.Latest, true);
    sf.statements.forEach(stmt => {
      if (ts.isClassDeclaration(stmt)) {
        const name = stmt.name ? stmt.name.text : "";
        const isPp = (name === "PolinePicker") || (stmt.heritageClauses && stmt.heritageClauses.some(h => h.getText(sf).includes("HTMLElement")));
        if (!isPp && name) {
          collaboratorUnits.push({ name, filePath: f, node: stmt, sf, kind: "class" });
          collaboratorFileSet.add(f);
        }
      } else if (ts.isFunctionDeclaration(stmt)) {
        const name = stmt.name ? stmt.name.text : "";
        if (name) {
          collaboratorUnits.push({ name, filePath: f, node: stmt, sf, kind: "function" });
        }
      } else if (ts.isVariableStatement(stmt)) {
        stmt.declarationList.declarations.forEach(decl => {
          if (decl.name && ts.isIdentifier(decl.name) && decl.initializer) {
            const name = decl.name.text;
            const init = decl.initializer;
            if (ts.isObjectLiteralExpression(init)) {
              collaboratorUnits.push({ name, filePath: f, node: init, sf, kind: "object_literal" });
            } else if (ts.isArrowFunction(init) || ts.isFunctionExpression(init)) {
              collaboratorUnits.push({ name, filePath: f, node: init, sf, kind: "function" });
            }
          }
        });
      }
    });
  }

  // For each collaborator unit, extract features.
  // Reachable helper files are only absorbed if they are pure helper files (not containing other collaborator classes/modules).
  for (const u of collaboratorUnits) {
    const feat = extractFeaturesFromNode(u.node, u.sf);
    if (u.filePath !== webcomponentPath) {
      const reachable = getReachableFiles(u.filePath, importGraph);
      reachable.delete(webcomponentPath);
      for (const rf of reachable) {
        if (rf !== u.filePath && !collaboratorFileSet.has(rf) && !rf.endsWith("index.ts") && !rf.endsWith("index.js")) {
          const rContent = fs.readFileSync(rf, "utf8");
          const rSf = ts.createSourceFile(path.basename(rf), rContent, ts.ScriptTarget.Latest, true);
          const rFeat = extractFeaturesFromNode(rSf, rSf);
          if (rFeat.hasSvgCreation) feat.hasSvgCreation = true;
          if (rFeat.hasSvgAttributeUpdate) feat.hasSvgAttributeUpdate = true;
          if (rFeat.hasGradientOrStyling) feat.hasGradientOrStyling = true;
          if (rFeat.hasPointerEventHandling) feat.hasPointerEventHandling = true;
          if (rFeat.hasRotaryOrDragMath) feat.hasRotaryOrDragMath = true;
          if (rFeat.hasHitTesting) feat.hasHitTesting = true;
          if (rFeat.hasInteractionState) feat.hasInteractionState = true;
        }
      }
    }
    u.features = feat;

    // Check substantive presentation and interaction responsibilities
    const ownsPresentation = (feat.hasSvgCreation || feat.hasSvgAttributeUpdate) && feat.hasGradientOrStyling;
    const ownsInteraction = feat.hasPointerEventHandling && (feat.hasRotaryOrDragMath || feat.hasHitTesting || feat.hasInteractionState);
    const isHybrid = ownsPresentation && ownsInteraction;

    u.isHybrid = isHybrid;
    u.isPresentation = ownsPresentation && !ownsInteraction;
    u.isInteraction = ownsInteraction && !ownsPresentation;
  }

  const presentationUnits = collaboratorUnits.filter(u => u.isPresentation && !u.isInteraction && !u.isHybrid);
  const interactionUnits = collaboratorUnits.filter(u => u.isInteraction && !u.isPresentation && !u.isHybrid);
  const mergedUnits = collaboratorUnits.filter(u => u.isHybrid || (u.features && (u.features.hasSvgCreation || u.features.hasSvgAttributeUpdate) && (u.features.hasPointerEventHandling && (u.features.hasRotaryOrDragMath || u.features.hasHitTesting))));

  if (mergedUnits.length > 0) {
    result.passed = false;
    const combinedNames = mergedUnits.map(u => u.name).join(", ");
    result.errors.push(`missing separation: presentation and interaction are combined in the same collaborator ${combinedNames} instead of separate responsibility units`);
  }

  if (presentationUnits.length === 0) {
    result.passed = false;
    result.errors.push("missing presentation separation: presentation ownership missing or collaborator is an empty shell");
  } else {
    result.presentationModule = path.basename(presentationUnits[0].filePath);
  }

  if (interactionUnits.length === 0) {
    result.passed = false;
    result.errors.push("missing interaction separation: interaction ownership missing or collaborator is an empty shell");
  } else {
    result.interactionModule = path.basename(interactionUnits[0].filePath);
  }

  // Symbols
  const presSymbols = new Set(presentationUnits.map(u => u.name));
  const intSymbols = new Set(interactionUnits.map(u => u.name));
  const presFiles = new Set(presentationUnits.map(u => u.filePath));
  const intFiles = new Set(interactionUnits.map(u => u.filePath));

  for (const imp of localImports) {
    if (presFiles.has(imp.targetPath) && imp.importClause) {
      if (imp.importClause.name) presSymbols.add(imp.importClause.name.text);
      if (imp.importClause.namedBindings && ts.isNamedImports(imp.importClause.namedBindings)) {
        imp.importClause.namedBindings.elements.forEach(el => presSymbols.add(el.name.text));
      }
      if (imp.importClause.namedBindings && ts.isNamespaceImport(imp.importClause.namedBindings)) {
        presSymbols.add(imp.importClause.namedBindings.name.text);
      }
    }
    if (intFiles.has(imp.targetPath) && imp.importClause) {
      if (imp.importClause.name) intSymbols.add(imp.importClause.name.text);
      if (imp.importClause.namedBindings && ts.isNamedImports(imp.importClause.namedBindings)) {
        imp.importClause.namedBindings.elements.forEach(el => intSymbols.add(el.name.text));
      }
      if (imp.importClause.namedBindings && ts.isNamespaceImport(imp.importClause.namedBindings)) {
        intSymbols.add(imp.importClause.namedBindings.name.text);
      }
    }
  }

  // Propagate factory symbols to variable bindings in webcomponent.ts
  wcSf.statements.forEach(stmt => {
    if (ts.isVariableStatement(stmt)) {
      stmt.declarationList.declarations.forEach(decl => {
        if (decl.name && ts.isIdentifier(decl.name) && decl.initializer) {
          const varName = decl.name.text;
          const initText = decl.initializer.getText(wcSf);
          for (const sym of presSymbols) {
            if (initText.includes(sym)) presSymbols.add(varName);
          }
          for (const sym of intSymbols) {
            if (initText.includes(sym)) intSymbols.add(varName);
          }
        }
      });
    }
  });

  const facadeSymbols = new Set();
  collaboratorUnits.forEach(u => {
    if (!u.isPresentation && !u.isInteraction) {
      const uText = u.node.getText(u.sf);
      let hasPresRef = false;
      let hasIntRef = false;
      for (const s of presSymbols) if (uText.includes(s)) hasPresRef = true;
      for (const s of intSymbols) if (uText.includes(s)) hasIntRef = true;
      if (hasPresRef && hasIntRef) {
        facadeSymbols.add(u.name);
      }
    }
  });

  const presentationProps = new Set();
  const interactionProps = new Set();
  const facadeProps = new Set();

  polinePickerClass.members.forEach(m => {
    let propName = null;
    let typeName = null;
    let initExprText = null;

    if (ts.isPropertyDeclaration(m) && m.name) {
      propName = m.name.getText(wcSf);
      if (m.type) typeName = m.type.getText(wcSf);
      if (m.initializer) initExprText = m.initializer.getText(wcSf);
    }

    if (propName) {
      for (const sym of presSymbols) {
        if ((typeName && typeName.includes(sym)) || (initExprText && initExprText.includes(sym))) {
          presentationProps.add(propName);
        }
      }
      for (const sym of intSymbols) {
        if ((typeName && typeName.includes(sym)) || (initExprText && initExprText.includes(sym))) {
          interactionProps.add(propName);
        }
      }
      for (const sym of facadeSymbols) {
        if ((typeName && typeName.includes(sym)) || (initExprText && initExprText.includes(sym))) {
          facadeProps.add(propName);
        }
      }
    }
  });

  function visitMembers(n) {
    if (ts.isBinaryExpression(n) && n.operatorToken.kind === ts.SyntaxKind.EqualsToken) {
      const leftText = n.left.getText(wcSf);
      const rightText = n.right.getText(wcSf);
      if (leftText.startsWith("this.")) {
        const prop = leftText.slice(5).split(".")[0];
        for (const sym of presSymbols) {
          if (rightText.includes(sym)) presentationProps.add(prop);
        }
        for (const sym of intSymbols) {
          if (rightText.includes(sym)) interactionProps.add(prop);
        }
        for (const sym of facadeSymbols) {
          if (rightText.includes(sym)) facadeProps.add(prop);
        }
      }
    }
    ts.forEachChild(n, visitMembers);
  }
  visitMembers(polinePickerClass);

  const methods = {};
  polinePickerClass.members.forEach(m => {
    if (ts.isMethodDeclaration(m) && m.name) {
      methods[m.name.getText(wcSf)] = m;
    } else if (ts.isPropertyDeclaration(m) && m.name) {
      if (m.initializer && (ts.isArrowFunction(m.initializer) || ts.isFunctionExpression(m.initializer))) {
        methods[m.name.getText(wcSf)] = m;
      }
    }
  });

  function getCallsAndNewsInMethod(methodNode, visited = new Set()) {
    const calls = [];
    if (!methodNode || visited.has(methodNode)) return calls;
    visited.add(methodNode);
    const body = methodNode.body || methodNode.initializer;
    if (!body) return calls;
    const aliases = new Map();
    function visit(node) {
      if (ts.isVariableDeclaration(node) && ts.isIdentifier(node.name) && node.initializer && (node.parent.flags & ts.NodeFlags.Const)) {
        const initial = unwrapExpr(node.initializer).getText(wcSf).replace(/\?\./g, ".");
        if (/^this\.[A-Za-z_$][\w$]*$/.test(initial)) aliases.set(node.name.text, initial);
      }
      if (ts.isCallExpression(node)) {
        let call = node.expression.getText(wcSf).replace(/\?\./g, ".");
        const first = call.split('.')[0];
        if (aliases.has(first)) call = aliases.get(first) + call.slice(first.length);
        calls.push(call);
        if (ts.isPropertyAccessExpression(node.expression) && node.expression.expression.kind === ts.SyntaxKind.ThisKeyword) {
          const target = methods[node.expression.name.getText(wcSf)];
          if (target) calls.push(...getCallsAndNewsInMethod(target, visited));
        }
      } else if (ts.isNewExpression(node)) {
        calls.push("new " + node.expression.getText(wcSf));
      }
      ts.forEachChild(node, visit);
    }
    visit(body);
    return calls;
  }

  // Delegation checks - strictly verify invocation on recognized collaborator instances/symbols
  if (methods["updateSVG"]) {
    const calls = getCallsAndNewsInMethod(methods["updateSVG"]);
    const delegatesToPresentation = calls.some(c => {
      for (const p of presentationProps) {
        if (c.startsWith("this." + p + ".")) return true;
      }
      for (const p of facadeProps) {
        if (c.startsWith("this." + p + ".")) return true;
      }
      for (const sym of presSymbols) {
        if (c.startsWith(sym + ".") || c.startsWith("this." + sym + ".") || c === sym || c === "this." + sym) return true;
      }
      return false;
    });
    if (!delegatesToPresentation) {
      result.passed = false;
      result.errors.push("missing coordinator delegation: PolinePicker.updateSVG() does not delegate to presentation collaborator");
    }
  }

  if (methods["connectedCallback"]) {
    const calls = getCallsAndNewsInMethod(methods["connectedCallback"]);
    const hasPresInit = calls.some(c => {
      for (const p of presentationProps) {
        if (c.startsWith("this." + p + ".")) return true;
      }
      for (const p of facadeProps) {
        if (c.startsWith("this." + p + ".")) return true;
      }
      for (const sym of presSymbols) {
        if (c.includes(sym)) return true;
      }
      return false;
    });
    const hasIntBind = calls.some(c => {
      for (const p of interactionProps) {
        if (c.startsWith("this." + p + ".")) return true;
      }
      for (const p of facadeProps) {
        if (c.startsWith("this." + p + ".")) return true;
      }
      for (const sym of intSymbols) {
        if (c.includes(sym)) return true;
      }
      return false;
    });
    if (!hasPresInit) {
      result.passed = false;
      result.errors.push("missing coordinator delegation: PolinePicker.connectedCallback() does not coordinate presentation initialization");
    }
    if (!hasIntBind) {
      result.passed = false;
      result.errors.push("missing coordinator delegation: PolinePicker.connectedCallback() does not bind pointer interaction collaborator");
    }
  }

  if (methods["disconnectedCallback"]) {
    const calls = getCallsAndNewsInMethod(methods["disconnectedCallback"]);
    const hasIntUnbind = calls.some(c => {
      for (const p of interactionProps) {
        if (c.startsWith("this." + p + ".")) return true;
      }
      for (const p of facadeProps) {
        if (c.startsWith("this." + p + ".")) return true;
      }
      for (const sym of intSymbols) {
        if (c.includes(sym)) return true;
      }
      return false;
    });
    if (!hasIntUnbind) {
      result.passed = false;
      result.errors.push("missing coordinator delegation: PolinePicker.disconnectedCallback() does not unbind interaction collaborator");
    }
  }

  if (methods["setAllowAddPoints"]) {
    let delegatesToInteraction = false;
    const calls = getCallsAndNewsInMethod(methods["setAllowAddPoints"]);

    // Mode 1: Imperative delegation call to interaction instance, facade instance, or interaction symbol
    const hasDirectIntCall = calls.some(c => {
      for (const p of interactionProps) {
        if (c.startsWith("this." + p + ".")) return true;
      }
      for (const p of facadeProps) {
        if (c.startsWith("this." + p + ".")) return true;
      }
      for (const sym of intSymbols) {
        if (c.startsWith(sym + ".") || c === sym || c.startsWith("this." + sym + ".")) return true;
      }
      return false;
    });

    if (hasDirectIntCall) {
      delegatesToInteraction = true;
    } else {
      // Mode 2: State provider / callback delegation
      function normalizePropName(name) {
        if (!name) return "";
        return String(name).replace(/^#/, "");
      }

      function getPropName(nameNode) {
        if (!nameNode) return "";
        const t = nameNode.text || nameNode.escapedText || (typeof nameNode.getText === "function" ? nameNode.getText(wcSf) : "");
        return normalizePropName(t);
      }

      function nodeReferencesThisProperty(node, propertyName) {
        let found = false;
        const normTarget = normalizePropName(propertyName);
        if (!normTarget || !node) return false;

        function visit(n) {
          if (found) return;

          if (ts.isPropertyAccessExpression(n)) {
            if (n.expression && n.expression.kind === ts.SyntaxKind.ThisKeyword && n.name) {
              const pName = getPropName(n.name);
              if (pName === normTarget) {
                found = true;
                return;
              }
            }
          } else if (ts.isElementAccessExpression(n)) {
            if (n.expression && n.expression.kind === ts.SyntaxKind.ThisKeyword && n.argumentExpression) {
              if (ts.isStringLiteral(n.argumentExpression) || ts.isNoSubstitutionTemplateLiteral(n.argumentExpression)) {
                const pName = normalizePropName(n.argumentExpression.text);
                if (pName === normTarget) {
                  found = true;
                  return;
                }
              }
            }
          }

          ts.forEachChild(n, visit);
        }

        visit(node);
        return found;
      }

      const assignedProps = [];
      const methodNode = methods["setAllowAddPoints"];
      const body = methodNode.body || methodNode.initializer;
      if (body) {
        function findAssignments(n) {
          if (ts.isBinaryExpression(n) && n.operatorToken.kind === ts.SyntaxKind.EqualsToken) {
            const left = n.left;
            if (ts.isPropertyAccessExpression(left) && left.expression && left.expression.kind === ts.SyntaxKind.ThisKeyword && left.name) {
              const pName = getPropName(left.name);
              if (pName && !assignedProps.includes(pName)) {
                assignedProps.push(pName);
              }
            } else if (ts.isElementAccessExpression(left) && left.expression && left.expression.kind === ts.SyntaxKind.ThisKeyword && left.argumentExpression) {
              if (ts.isStringLiteral(left.argumentExpression) || ts.isNoSubstitutionTemplateLiteral(left.argumentExpression)) {
                const pName = normalizePropName(left.argumentExpression.text);
                if (pName && !assignedProps.includes(pName)) {
                  assignedProps.push(pName);
                }
              }
            }
          }
          ts.forEachChild(n, findAssignments);
        }
        findAssignments(body);
      }

      if (assignedProps.length > 0) {
        let propProvidedToInteraction = false;

        function checkInteractionSetup(n) {
          if (ts.isNewExpression(n)) {
            const exprText = n.expression.getText(wcSf);
            let isTarget = false;
            for (const sym of intSymbols) if (exprText === sym || exprText.includes(sym)) isTarget = true;
            for (const sym of facadeSymbols) if (exprText === sym || exprText.includes(sym)) isTarget = true;

            if (isTarget && n.arguments) {
              for (const arg of n.arguments) {
                for (const ap of assignedProps) {
                  if (nodeReferencesThisProperty(arg, ap)) {
                    propProvidedToInteraction = true;
                  }
                }
              }
            }
          } else if (ts.isCallExpression(n)) {
            const callText = n.expression.getText(wcSf);
            let isTarget = false;
            for (const p of interactionProps) if (callText.startsWith("this." + p + ".")) isTarget = true;
            for (const p of facadeProps) if (callText.startsWith("this." + p + ".")) isTarget = true;
            for (const sym of intSymbols) if (callText === sym || callText.includes(sym)) isTarget = true;
            if (isTarget && n.arguments) {
              for (const arg of n.arguments) {
                for (const ap of assignedProps) {
                  if (nodeReferencesThisProperty(arg, ap)) {
                    propProvidedToInteraction = true;
                  }
                }
              }
            }
          }
          ts.forEachChild(n, checkInteractionSetup);
        }
        checkInteractionSetup(polinePickerClass);

        polinePickerClass.members.forEach(m => {
          if (ts.isGetAccessor(m) && m.name && m.body) {
            const getterName = m.name.getText(wcSf);
            for (const ap of assignedProps) {
              if (nodeReferencesThisProperty(m.body, ap)) {
                for (const u of interactionUnits) {
                  if (u.node.getText(u.sf).includes(getterName)) {
                    propProvidedToInteraction = true;
                  }
                }
              }
            }
          }
        });

        // Provider factory method analysis
        function unwrapExpression(expr) {
          let cur = expr;
          while (cur) {
            if (ts.isParenthesizedExpression(cur)) {
              cur = cur.expression;
            } else if (ts.isAsExpression(cur)) {
              cur = cur.expression;
            } else if (ts.isTypeAssertionExpression(cur)) {
              cur = cur.expression;
            } else if (ts.isNonNullExpression && ts.isNonNullExpression(cur)) {
              cur = cur.expression;
            } else {
              break;
            }
          }
          return cur;
        }

        function findReturnedObjectLiterals(methodBody) {
          const objectLiterals = [];
          if (!methodBody) return objectLiterals;

          const unwrappedBody = unwrapExpression(methodBody);
          if (ts.isObjectLiteralExpression(unwrappedBody)) {
            objectLiterals.push(unwrappedBody);
            return objectLiterals;
          }

          const returnStatements = [];
          function findReturns(n) {
            if (ts.isReturnStatement(n)) {
              returnStatements.push(n);
            }
            if (n !== methodBody && (ts.isFunctionDeclaration(n) || ts.isFunctionExpression(n) || ts.isArrowFunction(n) || ts.isMethodDeclaration(n))) {
              return;
            }
            ts.forEachChild(n, findReturns);
          }
          findReturns(methodBody);

          returnStatements.forEach(ret => {
            if (!ret.expression) return;
            const unwrapped = unwrapExpression(ret.expression);
            if (ts.isObjectLiteralExpression(unwrapped)) {
              objectLiterals.push(unwrapped);
            } else if (ts.isIdentifier(unwrapped)) {
              const idName = unwrapped.text;
              function findDecl(n) {
                if (ts.isVariableDeclaration(n) && n.name && ts.isIdentifier(n.name) && n.name.text === idName && n.initializer) {
                  const initUnwrapped = unwrapExpression(n.initializer);
                  if (ts.isObjectLiteralExpression(initUnwrapped)) {
                    objectLiterals.push(initUnwrapped);
                  }
                }
                ts.forEachChild(n, findDecl);
              }
              findDecl(methodBody);
            } else {
              function findObj(n) {
                if (ts.isObjectLiteralExpression(n)) {
                  objectLiterals.push(n);
                }
                ts.forEachChild(n, findObj);
              }
              findObj(ret);
            }
          });
          return objectLiterals;
        }

        const providerFactories = [];
        polinePickerClass.members.forEach(m => {
          let mName = null;
          let mBody = null;
          if (ts.isMethodDeclaration(m) && m.name) {
            mName = getPropName(m.name);
            mBody = m.body;
          } else if (ts.isPropertyDeclaration(m) && m.name && m.initializer) {
            if (ts.isArrowFunction(m.initializer) || ts.isFunctionExpression(m.initializer)) {
              mName = getPropName(m.name);
              mBody = m.initializer.body;
            }
          }
          if (!mName || !mBody || mName === "setAllowAddPoints") return;

          const returnedObjs = findReturnedObjectLiterals(mBody);
          returnedObjs.forEach(objLit => {
            if (!objLit.properties) return;
            objLit.properties.forEach(prop => {
              let memberName = null;
              let callbackNode = null;

              if (ts.isPropertyAssignment(prop) && prop.name) {
                memberName = getPropName(prop.name);
                const init = unwrapExpression(prop.initializer);
                if (init && (ts.isArrowFunction(init) || ts.isFunctionExpression(init))) {
                  callbackNode = init;
                }
              } else if (ts.isMethodDeclaration(prop) && prop.name && prop.body) {
                memberName = getPropName(prop.name);
                callbackNode = prop.body;
              } else if (ts.isGetAccessor(prop) && prop.name && prop.body) {
                memberName = getPropName(prop.name);
                callbackNode = prop.body;
              }

              if (memberName && callbackNode) {
                for (const ap of assignedProps) {
                  if (nodeReferencesThisProperty(callbackNode, ap)) {
                    providerFactories.push({
                      methodName: mName,
                      memberName: memberName,
                      assignedProp: ap
                    });
                  }
                }
              }
            });
          });
        });

        function nodeCallsOrReferencesMethod(node, targetMethod) {
          let found = false;
          const normTarget = normalizePropName(targetMethod);
          if (!normTarget || !node) return false;

          function visit(n) {
            if (found) return;
            if (ts.isCallExpression(n)) {
              const expr = n.expression;
              if (ts.isPropertyAccessExpression(expr) && expr.expression.kind === ts.SyntaxKind.ThisKeyword && expr.name) {
                if (getPropName(expr.name) === normTarget) {
                  found = true;
                  return;
                }
              } else if (ts.isIdentifier(expr) && expr.text === normTarget) {
                found = true;
                return;
              }
            } else if (ts.isPropertyAccessExpression(n)) {
              if (n.expression && n.expression.kind === ts.SyntaxKind.ThisKeyword && n.name) {
                if (getPropName(n.name) === normTarget) {
                  found = true;
                  return;
                }
              }
            }
            ts.forEachChild(n, visit);
          }
          visit(node);
          return found;
        }

        function findEnclosingFunction(node) {
          let cur = node.parent;
          while (cur) {
            if (ts.isMethodDeclaration(cur) || ts.isFunctionDeclaration(cur) || ts.isFunctionExpression(cur) || ts.isArrowFunction(cur) || ts.isConstructorDeclaration(cur)) {
              return cur;
            }
            cur = cur.parent;
          }
          return null;
        }

        function argReferencesFactoryResult(arg, methodName, callNode) {
          if (nodeCallsOrReferencesMethod(arg, methodName)) return true;
          const unwrapped = unwrapExpression(arg);
          if (ts.isIdentifier(unwrapped)) {
            const idName = unwrapped.text;
            const enc = findEnclosingFunction(callNode);
            if (enc) {
              let found = false;
              function findVar(v) {
                if (found) return;
                if (ts.isVariableDeclaration(v) && v.name && ts.isIdentifier(v.name) && v.name.text === idName && v.initializer) {
                  if (nodeCallsOrReferencesMethod(v.initializer, methodName)) {
                    found = true;
                    return;
                  }
                }
                ts.forEachChild(v, findVar);
              }
              findVar(enc);
              if (found) return true;
            }
          }
          return false;
        }

        const passedFactories = [];
        function checkProviderPassing(n) {
          if (ts.isNewExpression(n)) {
            let isInteractionTarget = false;
            const exprText = n.expression.getText(wcSf);
            for (const sym of intSymbols) {
              if (exprText === sym || exprText.includes(sym)) isInteractionTarget = true;
            }
            for (const sym of facadeSymbols) {
              if (exprText === sym || exprText.includes(sym)) isInteractionTarget = true;
            }
            for (const u of interactionUnits) {
              if (exprText === u.name || exprText.includes(u.name)) isInteractionTarget = true;
            }

            if (isInteractionTarget && n.arguments) {
              for (const arg of n.arguments) {
                for (const f of providerFactories) {
                  if (argReferencesFactoryResult(arg, f.methodName, n)) {
                    passedFactories.push(f);
                  }
                }
              }
            }
          } else if (ts.isCallExpression(n)) {
            let isInteractionTarget = false;
            if (ts.isPropertyAccessExpression(n.expression)) {
              const objExpr = n.expression.expression;
              if (ts.isPropertyAccessExpression(objExpr) && objExpr.expression.kind === ts.SyntaxKind.ThisKeyword && objExpr.name) {
                const pName = getPropName(objExpr.name);
                for (const p of interactionProps) {
                  if (normalizePropName(p) === pName) isInteractionTarget = true;
                }
                for (const p of facadeProps) {
                  if (normalizePropName(p) === pName) isInteractionTarget = true;
                }
              }
            }
            const callText = n.expression.getText(wcSf);
            for (const p of interactionProps) {
              const normP = normalizePropName(p);
              if (callText.startsWith("this." + p + ".") || callText.startsWith("this." + normP + ".") || callText.startsWith("this.#" + normP + ".")) {
                isInteractionTarget = true;
              }
            }
            for (const p of facadeProps) {
              const normP = normalizePropName(p);
              if (callText.startsWith("this." + p + ".") || callText.startsWith("this." + normP + ".") || callText.startsWith("this.#" + normP + ".")) {
                isInteractionTarget = true;
              }
            }
            for (const sym of intSymbols) {
              if (callText === sym || callText.includes(sym)) {
                isInteractionTarget = true;
              }
            }

            if (isInteractionTarget && n.arguments) {
              for (const arg of n.arguments) {
                for (const f of providerFactories) {
                  if (argReferencesFactoryResult(arg, f.methodName, n)) {
                    passedFactories.push(f);
                  }
                }
              }
            }
          }
          ts.forEachChild(n, checkProviderPassing);
        }
        checkProviderPassing(polinePickerClass);

        function unitConsumesMember(u, memberName) {
          let consumed = false;
          function visit(n) {
            if (consumed) return;
            if (ts.isPropertyAccessExpression(n)) {
              if (n.name && n.name.text === memberName) {
                consumed = true;
                return;
              }
            } else if (ts.isElementAccessExpression(n)) {
              if (n.argumentExpression && (ts.isStringLiteral(n.argumentExpression) || ts.isNoSubstitutionTemplateLiteral(n.argumentExpression))) {
                if (n.argumentExpression.text === memberName) {
                  consumed = true;
                  return;
                }
              }
            } else if (ts.isBindingElement(n)) {
              const pName = n.propertyName ? n.propertyName.text : (n.name && ts.isIdentifier(n.name) ? n.name.text : null);
              if (pName === memberName) {
                consumed = true;
                return;
              }
            } else if (ts.isCallExpression(n)) {
              if (ts.isPropertyAccessExpression(n.expression) && n.expression.name && n.expression.name.text === memberName) {
                consumed = true;
                return;
              }
              if (ts.isIdentifier(n.expression) && n.expression.text === memberName) {
                consumed = true;
                return;
              }
            }
            ts.forEachChild(n, visit);
          }
          visit(u.node);
          if (consumed) return true;

          const reachable = getReachableFiles(u.filePath, importGraph);
          reachable.delete(webcomponentPath);
          for (const rf of reachable) {
            if (rf !== u.filePath && !collaboratorFileSet.has(rf) && !rf.endsWith("index.ts") && !rf.endsWith("index.js")) {
              const rContent = fs.readFileSync(rf, "utf8");
              const rSf = ts.createSourceFile(path.basename(rf), rContent, ts.ScriptTarget.Latest, true);
              visit(rSf);
              if (consumed) return true;
            }
          }
          return false;
        }

        let providerFactoryDelegated = false;
        if (passedFactories.length > 0) {
          for (const f of passedFactories) {
            let consumed = false;
            for (const u of interactionUnits) {
              if (unitConsumesMember(u, f.memberName)) {
                consumed = true;
                break;
              }
            }
            if (!consumed) {
              for (const u of collaboratorUnits) {
                if (facadeSymbols.has(u.name)) {
                  if (unitConsumesMember(u, f.memberName)) {
                    consumed = true;
                    break;
                  }
                }
              }
            }
            if (consumed) {
              providerFactoryDelegated = true;
              break;
            }
          }
        }

        const facadeDoesNotOwnPointerInteraction =
          !ppFeat.hasPointerEventHandling || !ppFeat.hasRotaryOrDragMath;

        if (propProvidedToInteraction && !ppFeat.hasPointerEventHandling) {
          delegatesToInteraction = true;
        } else if (providerFactoryDelegated && facadeDoesNotOwnPointerInteraction) {
          delegatesToInteraction = true;
        }
      }
    }

    if (!delegatesToInteraction) {
      result.passed = false;
      result.errors.push("missing coordinator delegation: PolinePicker.setAllowAddPoints() does not delegate to interaction collaborator");
    }
  }

  // Pointerdown Event Listener Reachability Verification (audit-F01)
  function unwrapExpr(node) {
    let curr = node;
    while (curr) {
      if (ts.isParenthesizedExpression(curr) || ts.isAsExpression(curr) || ts.isTypeAssertionExpression(curr)) {
        curr = curr.expression;
      } else if (ts.isNonNullExpression && ts.isNonNullExpression(curr)) {
        curr = curr.expression;
      } else if (ts.isCallExpression(curr)) {
        const callee = unwrapExpr(curr.expression);
        if (ts.isPropertyAccessExpression(callee) && callee.name.text === "bind") {
          curr = callee.expression;
        } else {
          break;
        }
      } else {
        break;
      }
    }
    return curr;
  }

  function isBodyEmptyOrNoop(bodyNode, sf) {
    if (!bodyNode) return true;
    if (!ts.isBlock(bodyNode)) {
      const unwrapped = unwrapExpr(bodyNode);
      if (ts.isVoidExpression(unwrapped)) return true;
      if (ts.isIdentifier(unwrapped) && (unwrapped.text === "undefined" || unwrapped.text === "null")) return true;
      if (ts.isNumericLiteral(unwrapped) || ts.isStringLiteral(unwrapped)) return true;
      return false;
    }
    const statements = bodyNode.statements;
    if (!statements || statements.length === 0) return true;
    for (const stmt of statements) {
      if (ts.isEmptyStatement(stmt)) continue;
      if (ts.isReturnStatement(stmt)) {
        if (!stmt.expression) continue;
        const unwrapped = unwrapExpr(stmt.expression);
        if (ts.isVoidExpression(unwrapped)) continue;
        if (ts.isIdentifier(unwrapped) && (unwrapped.text === "undefined" || unwrapped.text === "null")) continue;
        return false;
      }
      if (ts.isExpressionStatement(stmt)) {
        const expr = unwrapExpr(stmt.expression);
        if (ts.isVoidExpression(expr)) continue;
        if (ts.isIdentifier(expr) && (expr.text === "undefined" || expr.text === "null")) continue;
        if (ts.isNumericLiteral(expr) || ts.isStringLiteral(expr)) continue;
        if (ts.isCallExpression(expr)) {
          const calleeText = expr.expression.getText(sf);
          if (calleeText.startsWith("console.")) continue;
        }
        return false;
      }
      return false;
    }
    return true;
  }

  function nodeHasSubstantiveInteraction(node, sf) {
    if (!node) return false;
    const body = node.body || node.initializer || node;
    if (isBodyEmptyOrNoop(body, sf)) return false;
    const feat = extractFeaturesFromNode(node, sf);
    if (feat.hasRotaryOrDragMath || feat.hasHitTesting || feat.hasInteractionState) {
      return true;
    }
    const text = node.getText(sf);
    if (
      text.includes("setPointerCapture") ||
      text.includes("pointerToNormalizedCoordinates") ||
      text.includes("stalePointerIds") ||
      text.includes("cancelGesture")
    ) {
      return true;
    }
    if (feat.hasPointerEventHandling && (text.includes("pointerId") || text.includes("clientX") || text.includes("clientY"))) {
      if (text.includes("Math.") || text.includes("currentPoint") || text.includes("distance") || text.includes("normalized")) {
        return true;
      }
    }
    return false;
  }

  function getUnitMembers(u) {
    const members = new Map();
    if (u.kind === "class") {
      u.node.members.forEach(m => {
        let mName = null;
        if (m.name) mName = m.name.getText(u.sf).replace(/^#/, "");
        if (mName) members.set(mName, m);
      });
    } else if (u.kind === "object_literal") {
      if (u.node.properties) {
        u.node.properties.forEach(p => {
          let pName = null;
          if (p.name) pName = p.name.getText(u.sf).replace(/^#/, "");
          if (pName) members.set(pName, p);
        });
      }
    } else if (u.kind === "function") {
      const body = u.node.body;
      if (body) {
        function findFuncs(n) {
          if (ts.isFunctionDeclaration(n) && n.name) {
            members.set(n.name.text, n);
          } else if (ts.isVariableDeclaration(n) && n.name && ts.isIdentifier(n.name) && n.initializer) {
            const init = unwrapExpr(n.initializer);
            if (ts.isArrowFunction(init) || ts.isFunctionExpression(init)) {
              members.set(n.name.text, n);
            }
          }
          if (n !== body && (ts.isFunctionDeclaration(n) || ts.isFunctionExpression(n) || ts.isArrowFunction(n))) {
            return;
          }
          ts.forEachChild(n, findFuncs);
        }
        findFuncs(body);
      }
    }
    return members;
  }

  function checkMemberSubstantive(mNode, u, membersMap, visited) {
    if (!mNode) return false;
    if (!visited) visited = new Set();
    if (visited.has(mNode)) return false;
    visited.add(mNode);

    if (nodeHasSubstantiveInteraction(mNode, u.sf)) return true;

    let targetBodies = [];
    if (mNode.body) targetBodies.push(mNode.body);
    if (mNode.initializer) targetBodies.push(mNode.initializer);

    if (mNode.name) {
      const mName = mNode.name.getText(u.sf).replace(/^#/, "");
      function findPropAssignments(n) {
        if (ts.isBinaryExpression(n) && n.operatorToken.kind === ts.SyntaxKind.EqualsToken) {
          const left = unwrapExpr(n.left);
          if (ts.isPropertyAccessExpression(left) && left.expression.kind === ts.SyntaxKind.ThisKeyword) {
            if (left.name.text.replace(/^#/, "") === mName) {
              const right = unwrapExpr(n.right);
              if (ts.isArrowFunction(right) || ts.isFunctionExpression(right)) {
                targetBodies.push(right.body || right);
              }
            }
          }
        }
        ts.forEachChild(n, findPropAssignments);
      }
      findPropAssignments(u.node);
    }

    for (let body of targetBodies) {
      body = unwrapExpr(body);
      if (isBodyEmptyOrNoop(body, u.sf)) continue;
      if (nodeHasSubstantiveInteraction(body, u.sf)) return true;

      if (ts.isPropertyAccessExpression(body)) {
        if (body.expression.kind === ts.SyntaxKind.ThisKeyword) {
          const targetName = body.name.text.replace(/^#/, "");
          if (membersMap.has(targetName)) {
            if (checkMemberSubstantive(membersMap.get(targetName), u, membersMap, visited)) {
              return true;
            }
          }
        }
      } else if (ts.isIdentifier(body)) {
        const targetName = body.text;
        if (membersMap.has(targetName)) {
          if (checkMemberSubstantive(membersMap.get(targetName), u, membersMap, visited)) {
            return true;
          }
        }
      }

      let callsSubstantive = false;
      function visitCalls(n) {
        if (callsSubstantive) return;
        if (ts.isCallExpression(n)) {
          const expr = unwrapExpr(n.expression);
          let targetName = null;
          if (ts.isPropertyAccessExpression(expr)) {
            if (expr.expression.kind === ts.SyntaxKind.ThisKeyword) {
              targetName = expr.name.text.replace(/^#/, "");
            }
          } else if (ts.isIdentifier(expr)) {
            targetName = expr.text;
          }
          if (targetName && membersMap.has(targetName)) {
            const calledMember = membersMap.get(targetName);
            if (checkMemberSubstantive(calledMember, u, membersMap, visited)) {
              callsSubstantive = true;
              return;
            }
          }
        }
        ts.forEachChild(n, visitCalls);
      }
      visitCalls(body);
      if (callsSubstantive) return true;
    }

    return false;
  }

  // Resolve lexical bindings by TypeScript symbol identity, preserving each
  // event/callback tuple instead of mixing callbacks from other event rows.
  const registrationProgram = ts.createProgram(allSourceFiles, {allowJs: true, noResolve: true, target: ts.ScriptTarget.Latest});
  const registrationChecker = registrationProgram.getTypeChecker();
  function registrationSymbol(node) {
    return registrationChecker.getSymbolAtLocation(ts.isPropertyAccessExpression(node) ? node.name : node);
  }
  function registrationValue(node, bindings, seen = new Set()) {
    if (!node) return null;
    node = unwrapExpr(node);
    if (seen.has(node)) return node;
    seen.add(node);
    if (ts.isIdentifier(node) || ts.isPropertyAccessExpression(node)) {
      const symbol = registrationSymbol(node);
      if (symbol && bindings.has(symbol)) return registrationValue(bindings.get(symbol), bindings, seen);
      const decl = symbol && (symbol.valueDeclaration || (symbol.declarations || [])[0]);
      if (decl && decl.initializer) {
        const initial = unwrapExpr(decl.initializer);
        // Callback fields may be initialized to null and assigned at connection;
        // retain the member reference so the ownership checker sees its writes.
        if (!ts.isPropertyAccessExpression(node) || ts.isArrayLiteralExpression(initial) || ts.isObjectLiteralExpression(initial) || ts.isNewExpression(initial) || ts.isStringLiteral(initial) || ts.isNoSubstitutionTemplateLiteral(initial)) {
          return registrationValue(initial, bindings, seen);
        }
      }
      if (decl && (ts.isFunctionDeclaration(decl) || ts.isMethodDeclaration(decl))) return decl;
    }
    return node;
  }
  function registrationRows(expr, bindings) {
    const value = registrationValue(expr, bindings);
    if (!value) return [];
    if (ts.isArrayLiteralExpression(value)) return [...value.elements];
    if (ts.isCallExpression(value) && ts.isPropertyAccessExpression(value.expression) && value.expression.expression.getText() === 'Object' && ['entries','values','keys'].includes(value.expression.name.text)) {
      const object = registrationValue(value.arguments[0], bindings);
      if (object && ts.isObjectLiteralExpression(object)) return object.properties.filter(ts.isPropertyAssignment).map(prop => {
        const key = ts.factory.createStringLiteral(prop.name.text);
        if (value.expression.name.text === 'keys') return key;
        if (value.expression.name.text === 'values') return prop.initializer;
        return ts.factory.createArrayLiteralExpression([key, prop.initializer]);
      });
    }

    if (ts.isNewExpression(value) && value.expression.getText() === 'Map' && value.arguments && value.arguments[0]) {
      return registrationRows(value.arguments[0], bindings);
    }
    if (ts.isCallExpression(value) && ts.isPropertyAccessExpression(value.expression) && ['entries', 'values', 'keys'].includes(value.expression.name.text)) {
      const rows = registrationRows(value.expression.expression, bindings);
      if (value.expression.name.text === 'entries') return rows;
      const offset = value.expression.name.text === 'keys' ? 0 : 1;
      return rows.map(row => registrationValue(row, bindings)).filter(row => row && ts.isArrayLiteralExpression(row)).map(row => row.elements[offset]);
    }
    return [];
  }
  function registrationBind(pattern, value, bindings) {
    if (!pattern || !value) return;
    if (ts.isIdentifier(pattern)) {
      const symbol = registrationSymbol(pattern);
      if (symbol) bindings.set(symbol, value);
    } else if (ts.isArrayBindingPattern(pattern)) {
      const tuple = registrationValue(value, bindings);
      if (tuple && ts.isArrayLiteralExpression(tuple)) pattern.elements.forEach((element, i) => {
        if (ts.isBindingElement(element)) registrationBind(element.name, tuple.elements[i], bindings);
      });
    }
  }
  const allPointerDownRegistrations = [];
  for (const f of allSourceFiles) {
    if (f.endsWith('index.ts') || f.endsWith('index.js')) continue;
    const sf = registrationProgram.getSourceFile(f);
    if (!sf) continue;
    const active = new Set();
    function scanRegistrations(node, bindings = new Map(), enterFunction = false) {
      if (!node) return;
      if ((ts.isArrowFunction(node) || ts.isFunctionExpression(node)) && !enterFunction) return;
      if (ts.isForOfStatement(node)) {
        const declaration = ts.isVariableDeclarationList(node.initializer) ? node.initializer.declarations[0] : null;
        for (const row of registrationRows(node.expression, bindings)) {
          const local = new Map(bindings);
          if (declaration) registrationBind(declaration.name, row, local);
          scanRegistrations(node.statement, local);
        }
        return;
      }
      if (ts.isBinaryExpression(node) && node.operatorToken.kind === ts.SyntaxKind.EqualsToken && ts.isPropertyAccessExpression(node.left)) {
        const symbol = registrationSymbol(node.left);
        if (symbol) bindings.set(symbol, node.right);
      }
      if (ts.isCallExpression(node)) {
        const callee = unwrapExpr(node.expression);
        const method = ts.isPropertyAccessExpression(callee) ? callee.name.text : ts.isElementAccessExpression(callee) && ts.isStringLiteral(callee.argumentExpression) ? callee.argumentExpression.text : null;
        if (method === 'addEventListener' && node.arguments.length >= 2) {
          const event = registrationValue(node.arguments[0], bindings);
          if (event && (ts.isStringLiteral(event) || ts.isNoSubstitutionTemplateLiteral(event)) && event.text === 'pointerdown') {
            allPointerDownRegistrations.push({callNode: node, sf, filePath: f, callbackNode: registrationValue(node.arguments[1], bindings), bindings: new Map(bindings)});
          }
        }
        if (ts.isPropertyAccessExpression(callee) && ['map', 'forEach'].includes(method)) {
          const callback = registrationValue(node.arguments[0], bindings);
          if (callback && (ts.isArrowFunction(callback) || ts.isFunctionExpression(callback))) {
            for (const row of registrationRows(callee.expression, bindings)) {
              const local = new Map(bindings);
              if (callback.parameters[0]) registrationBind(callback.parameters[0].name, row, local);
              scanRegistrations(callback.body, local);
            }
          }
        }
        // Local registration wrappers are invoked with their actual arguments.
        const target = registrationValue(callee, bindings);
        if (target && (ts.isArrowFunction(target) || ts.isFunctionExpression(target) || ts.isFunctionDeclaration(target) || ts.isMethodDeclaration(target)) && !active.has(target)) {
          active.add(target);
          const local = new Map(bindings);
          target.parameters.forEach((parameter, i) => registrationBind(parameter.name, node.arguments[i], local));
          scanRegistrations(target.body, local);
          active.delete(target);
        }
      }
      ts.forEachChild(node, child => scanRegistrations(child, bindings));
    }
    scanRegistrations(sf);
  }

  let validPointerDownDelegation = false;
  const unitMembersCache = new Map();
  for (const u of interactionUnits) {
    unitMembersCache.set(u, getUnitMembers(u));
  }

  function isReceiverInteraction(objExpr, sf) {
    if (!objExpr) return false;
    const text = objExpr.getText(sf);
    if (text.startsWith("this.")) {
      const prop = text.slice(5).replace(/^#/, "").split(".")[0];
      for (const p of interactionProps) {
        if (p.replace(/^#/, "") === prop) return true;
      }
      for (const p of facadeProps) {
        if (p.replace(/^#/, "") === prop) return true;
      }
    }
    for (const sym of intSymbols) {
      if (text === sym || text.includes(sym)) return true;
    }
    for (const u of interactionUnits) {
      if (text === u.name || text.includes(u.name)) return true;
    }
    return false;
  }

  function isReceiverPresentation(objExpr, sf) {
    if (!objExpr) return false;
    const text = objExpr.getText(sf);
    if (text.startsWith("this.")) {
      const prop = text.slice(5).replace(/^#/, "").split(".")[0];
      for (const p of presentationProps) {
        if (p.replace(/^#/, "") === prop) return true;
      }
    }
    for (const sym of presSymbols) {
      if (text === sym || text.includes(sym)) return true;
    }
    for (const u of presentationUnits) {
      if (text === u.name || text.includes(u.name)) return true;
    }
    return false;
  }

  function nodeDelegatesToSubstantiveInteraction(node, sf) {
    let found = false;

    function visit(n) {
      if (found) return;

      if (ts.isCallExpression(n)) {
        const callExpr = unwrapExpr(n.expression);

        if (ts.isPropertyAccessExpression(callExpr)) {
          const receiver = unwrapExpr(callExpr.expression);
          const methodName = callExpr.name.text.replace(/^#/, "");

          if (isReceiverInteraction(receiver, sf)) {
            for (const unit of interactionUnits) {
              const members = unitMembersCache.get(unit);

              if (
                members &&
                members.has(methodName) &&
                checkMemberSubstantive(
                  members.get(methodName),
                  unit,
                  members
                )
              ) {
                found = true;
                return;
              }
            }
          }
        }
      }

      ts.forEachChild(n, visit);
    }

    visit(node);
    return found;
  }

  for (const reg of allPointerDownRegistrations) {
    if (validPointerDownDelegation) break;

    const sf = reg.sf;
    let cb = unwrapExpr(reg.callbackNode);

    if (ts.isCallExpression(cb)) {
      const callee = unwrapExpr(cb.expression);
      if (ts.isPropertyAccessExpression(callee) && callee.name.text === "bind") {
        cb = unwrapExpr(callee.expression);
      }
    }

    let enclosingUnit = null;
    for (const u of interactionUnits) {
      if (u.filePath === reg.filePath) {
        if (reg.callNode.pos >= u.node.pos && reg.callNode.end <= u.node.end) {
          enclosingUnit = u;
          break;
        }
      }
    }
    if (!enclosingUnit) {
      for (const u of interactionUnits) {
        if (u.filePath === reg.filePath && u.filePath !== webcomponentPath) {
          enclosingUnit = u;
          break;
        }
      }
    }
    const isInsidePolinePicker = (reg.filePath === webcomponentPath && polinePickerClass && reg.callNode.pos >= polinePickerClass.pos && reg.callNode.end <= polinePickerClass.end);
    // Follow only invoked callbacks under the selected pointerdown row's lexical
    // bindings. Other rows (e.g. pointermove) cannot certify a no-op pointerdown.
    const callbackSeen = new Set();
    function boundCallbackIsSubstantive(expression) {
      const resolved = registrationValue(expression, reg.bindings || new Map());
      if (!resolved || callbackSeen.has(resolved)) return false;
      callbackSeen.add(resolved);
      if (ts.isPropertyAccessExpression(resolved)) {
        const receiver = unwrapExpr(resolved.expression);
        const name = resolved.name.text.replace(/^#/, '');
        if (receiver.kind === ts.SyntaxKind.ThisKeyword && enclosingUnit) {
          const members = unitMembersCache.get(enclosingUnit);
          if (members && members.has(name) && checkMemberSubstantive(members.get(name), enclosingUnit, members)) return true;
        }
        if (isReceiverInteraction(receiver, sf)) {
          for (const unit of interactionUnits) {
            const members = unitMembersCache.get(unit);
            if (members && members.has(name) && checkMemberSubstantive(members.get(name), unit, members)) return true;
          }
        }
      }
      if (ts.isCallExpression(resolved) && ts.isPropertyAccessExpression(resolved.expression) && resolved.expression.name.text === 'bind') {
        return boundCallbackIsSubstantive(resolved.expression.expression);
      }
      if (ts.isArrowFunction(resolved) || ts.isFunctionExpression(resolved) || ts.isFunctionDeclaration(resolved) || ts.isMethodDeclaration(resolved)) {
        if (enclosingUnit && resolved.pos >= enclosingUnit.node.pos && resolved.end <= enclosingUnit.node.end && nodeHasSubstantiveInteraction(resolved.body, sf)) return true;
        let found = false;
        function inspectInvocations(n) {
          if (found) return;
          if (ts.isCallExpression(n)) {
            let callee = unwrapExpr(n.expression);
            if (ts.isPropertyAccessExpression(callee) && ['call', 'apply'].includes(callee.name.text)) callee = callee.expression;
            if (boundCallbackIsSubstantive(callee)) { found = true; return; }
          }
          ts.forEachChild(n, inspectInvocations);
        }
        inspectInvocations(resolved.body);
        return found;
      }
      return false;
    }
    if (boundCallbackIsSubstantive(cb)) { validPointerDownDelegation = true; break; }


    if (ts.isPropertyAccessExpression(cb)) {
      const obj = unwrapExpr(cb.expression);
      const propName = cb.name.text.replace(/^#/, "");

      if (isReceiverInteraction(obj, sf)) {
        for (const u of interactionUnits) {
          const members = unitMembersCache.get(u);
          if (members && members.has(propName)) {
            if (checkMemberSubstantive(members.get(propName), u, members)) {
              validPointerDownDelegation = true;
              break;
            }
          }
        }
      } else if (obj.kind === ts.SyntaxKind.ThisKeyword && enclosingUnit) {
        const members = unitMembersCache.get(enclosingUnit);
        if (members && members.has(propName)) {
          if (checkMemberSubstantive(members.get(propName), enclosingUnit, members)) {
            validPointerDownDelegation = true;
          }
        }
      } else if (
        obj.kind === ts.SyntaxKind.ThisKeyword &&
        isInsidePolinePicker
      ) {
        if (methods[propName]) {
          const facadeMethod = methods[propName];

          if (
            nodeDelegatesToSubstantiveInteraction(
              facadeMethod,
              sf
            )
          ) {
            validPointerDownDelegation = true;
          }
        }
      }
      if (validPointerDownDelegation) break;
    }

    let resolvedFnNode = null;
    let resolvedSf = sf;
    let resolvedEnclosingUnit = enclosingUnit;

    if (ts.isIdentifier(cb)) {
      const idName = cb.text;

      if (enclosingUnit) {
        const members = unitMembersCache.get(enclosingUnit);
        if (members && members.has(idName)) {
          if (checkMemberSubstantive(members.get(idName), enclosingUnit, members)) {
            validPointerDownDelegation = true;
            break;
          }
        }
      }

      let currScope = reg.callNode.parent;
      while (currScope && !resolvedFnNode) {
        function findInNode(n) {
          if (resolvedFnNode) return;
          if (ts.isFunctionDeclaration(n) && n.name && n.name.text === idName) {
            resolvedFnNode = n;
          } else if (ts.isVariableDeclaration(n) && n.name && ts.isIdentifier(n.name) && n.name.text === idName && n.initializer) {
            const init = unwrapExpr(n.initializer);
            if (ts.isArrowFunction(init) || ts.isFunctionExpression(init) || ts.isPropertyAccessExpression(init)) {
              resolvedFnNode = init;
            }
          }
          if (n !== currScope && (ts.isFunctionDeclaration(n) || ts.isClassDeclaration(n) || ts.isMethodDeclaration(n))) {
            return;
          }
          ts.forEachChild(n, findInNode);
        }
        findInNode(currScope);
        currScope = currScope.parent;
      }

      if (!resolvedFnNode) {
        sf.statements.forEach(stmt => {
          if (resolvedFnNode) return;
          if (ts.isFunctionDeclaration(stmt) && stmt.name && stmt.name.text === idName) {
            resolvedFnNode = stmt;
          } else if (ts.isVariableStatement(stmt)) {
            stmt.declarationList.declarations.forEach(d => {
              if (d.name && ts.isIdentifier(d.name) && d.name.text === idName && d.initializer) {
                resolvedFnNode = unwrapExpr(d.initializer);
              }
            });
          }
        });
      }
    } else if (ts.isArrowFunction(cb) || ts.isFunctionExpression(cb)) {
      resolvedFnNode = cb;
    }

    if (resolvedFnNode) {
      if (ts.isPropertyAccessExpression(resolvedFnNode)) {
        const obj = unwrapExpr(resolvedFnNode.expression);
        const propName = resolvedFnNode.name.text.replace(/^#/, "");
        if (isReceiverInteraction(obj, resolvedSf)) {
          for (const u of interactionUnits) {
            const members = unitMembersCache.get(u);
            if (members && members.has(propName)) {
              if (checkMemberSubstantive(members.get(propName), u, members)) {
                validPointerDownDelegation = true;
                break;
              }
            }
          }
        }
        if (validPointerDownDelegation) break;
      }

      const fnBody = resolvedFnNode.body || resolvedFnNode;
      if (isBodyEmptyOrNoop(fnBody, resolvedSf)) {
        continue;
      }

      if (resolvedEnclosingUnit && nodeHasSubstantiveInteraction(resolvedFnNode, resolvedSf)) {
        validPointerDownDelegation = true;
        break;
      }

      let callsSubstantiveInteraction = false;
      let callsPresentationOnly = true;

      function checkCallsInFn(n) {
        if (callsSubstantiveInteraction) return;
        if (ts.isCallExpression(n)) {
          const callExpr = unwrapExpr(n.expression);

          if (ts.isPropertyAccessExpression(callExpr)) {
            if (!isReceiverPresentation(callExpr.expression, resolvedSf)) {
              callsPresentationOnly = false;
            }
          } else {
            callsPresentationOnly = false;
          }

          if (ts.isPropertyAccessExpression(callExpr)) {
            const receiver = unwrapExpr(callExpr.expression);
            const mName = callExpr.name.text.replace(/^#/, "");
            if (isReceiverInteraction(receiver, resolvedSf)) {
              for (const u of interactionUnits) {
                const members = unitMembersCache.get(u);
                if (members && members.has(mName)) {
                  if (checkMemberSubstantive(members.get(mName), u, members)) {
                    callsSubstantiveInteraction = true;
                    return;
                  }
                }
              }
            } else if (receiver.kind === ts.SyntaxKind.ThisKeyword && resolvedEnclosingUnit) {
              const members = unitMembersCache.get(resolvedEnclosingUnit);
              if (members && members.has(mName)) {
                if (checkMemberSubstantive(members.get(mName), resolvedEnclosingUnit, members)) {
                  callsSubstantiveInteraction = true;
                  return;
                }
              }
            } else if (
              receiver.kind === ts.SyntaxKind.ThisKeyword &&
              isInsidePolinePicker
            ) {
              if (methods[mName]) {
                const facadeMethod = methods[mName];

                if (
                  nodeDelegatesToSubstantiveInteraction(
                    facadeMethod,
                    resolvedSf
                  )
                ) {
                  callsSubstantiveInteraction = true;
                  return;
                }
              }
            }
          } else if (ts.isIdentifier(callExpr)) {
            const funcName = callExpr.text;
            if (resolvedEnclosingUnit) {
              const members = unitMembersCache.get(resolvedEnclosingUnit);
              if (members && members.has(funcName)) {
                if (checkMemberSubstantive(members.get(funcName), resolvedEnclosingUnit, members)) {
                  callsSubstantiveInteraction = true;
                  return;
                }
              }
            }
          }
        }
        ts.forEachChild(n, checkCallsInFn);
      }

      checkCallsInFn(fnBody);

      if (callsSubstantiveInteraction && !callsPresentationOnly) {
        validPointerDownDelegation = true;
        break;
      }
    }
  }

  if (allPointerDownRegistrations.length === 0 || !validPointerDownDelegation) {
    result.passed = false;
    result.errors.push("missing interaction event delegation: pointerdown listener does not reach the interaction collaborator");
  }

  result.details = {
    presentationModule: result.presentationModule,
    interactionModule: result.interactionModule,
    importedCollaborators: Array.from(localImportedFiles).map(f => path.basename(f))
  };

  return result;
}

let inputData = "";
process.stdin.on("data", chunk => { inputData += chunk; });
process.stdin.on("end", () => {
  try {
    const req = JSON.parse(inputData);
    if (req.action === "scan_test_bypass") {
      const findings = [];
      for (const f of req.files) {
        if (fs.existsSync(f)) {
          const content = fs.readFileSync(f, "utf8");
          const fileFindings = scanFileForBypass(f, content);
          for (const msg of fileFindings) {
            findings.push(path.basename(f) + ": " + msg);
          }
        }
      }
      console.log(JSON.stringify({ findings }));
    } else if (req.action === "analyze_architecture") {
      const res = analyzeRepoArchitecture(req.srcDir);
      console.log(JSON.stringify(res));
    } else {
      console.error("Unknown action:", req.action);
      process.exit(1);
    }
  } catch (e) {
    console.error(e.stack || e.message);
    process.exit(1);
  }
});
"""


def scan_test_bypass_ast(files_to_scan: list[Path], repo_dir: Path, cmd_env: dict[str, str]) -> list[str]:
    """Scan files using AST-aware TypeScript analysis to eliminate comment/doc/string false positives."""
    if not files_to_scan:
        return []
    file_strs = [str(f.resolve()) for f in files_to_scan if f.is_file()]
    if not file_strs:
        return []
    req_data = json.dumps({"action": "scan_test_bypass", "files": file_strs})
    try:
        proc = subprocess.run(
            ["node", "-e", AST_ANALYZER_SCRIPT],
            cwd=str(repo_dir),
            env=cmd_env,
            input=req_data,
            text=True,
            capture_output=True,
            timeout=30.0,
        )
        if proc.returncode != 0:
            return [f"AST bypass scanner failed with code {proc.returncode}: {proc.stderr.strip() or proc.stdout.strip()}"]
        out = json.loads(proc.stdout)
        return out.get("findings", [])
    except Exception as e:
        return [f"AST bypass scanner execution error: {e}"]


def sanitize_message(msg: str) -> str:
    """Sanitize diagnostic messages to prevent environment variable or secret leaks."""
    if not isinstance(msg, str):
        return ""
    sanitized = re.sub(r"(Bearer\s+)[A-Za-z0-9_\-\.~]+", r"\1[REDACTED]", msg, flags=re.IGNORECASE)
    sanitized = re.sub(
        r"((?:token|key|secret|password|passwd|auth|credential|api[_-]?key)\s*[:=]\s*)['\"]?[A-Za-z0-9_\-\.~]+['\"]?",
        r"\1[REDACTED]",
        sanitized,
        flags=re.IGNORECASE,
    )
    return sanitized


def check_architecture_separation(repo_dir: Path, cmd_env: dict[str, str]) -> tuple[bool, str, dict[str, Any]]:
    """Verify architectural decoupling of presentation, interaction, and coordinator."""
    src_dir = repo_dir / "src"
    if not src_dir.is_dir():
        return False, "src directory does not exist in repository", {}
    req_data = json.dumps({"action": "analyze_architecture", "srcDir": str(src_dir.resolve())})
    try:
        proc = subprocess.run(
            ["node", "-e", AST_ANALYZER_SCRIPT],
            cwd=str(repo_dir),
            env=cmd_env,
            input=req_data,
            text=True,
            capture_output=True,
            timeout=30.0,
        )
        if proc.returncode != 0:
            err_output = sanitize_message(proc.stderr.strip() or proc.stdout.strip())
            is_infra = False
            infra_type = "ARCHITECTURE_ANALYSIS_ERROR"
            if proc.returncode in (126, 127):
                is_infra = True
                infra_type = "EXECUTABLE_UNAVAILABLE"
            elif proc.returncode < 0:
                is_infra = True
                infra_type = "PROCESS_SIGNAL_TERMINATED"
            elif "Cannot find module" in err_output:
                is_infra = True
                infra_type = "DEPENDENCY_UNAVAILABLE"

            err_msg = f"AST architecture analysis failed with code {proc.returncode}: {err_output}"
            details = {
                "error": err_msg,
                "is_infra": is_infra,
                "infra_type": infra_type,
                "infra_msg": err_msg if is_infra else None,
            }
            return False, err_msg, details

        res = json.loads(proc.stdout)
        passed = bool(res.get("passed"))
        errors = res.get("errors", [])
        msg = "Architectural separation verified: presentation and interaction decoupled into independent modules and coordinated by PolinePicker" if passed else "; ".join(errors)
        return passed, msg, res.get("details", {})
    except subprocess.TimeoutExpired as te:
        err_msg = "AST architecture analysis timed out after 30.0 seconds"
        return False, err_msg, {"error": err_msg, "is_infra": True, "infra_type": "TIMEOUT", "infra_msg": err_msg}
    except (FileNotFoundError, PermissionError) as pe:
        err_msg = f"Failed to launch node for AST architecture analysis: {pe}"
        return False, err_msg, {"error": err_msg, "is_infra": True, "infra_type": "EXECUTABLE_UNAVAILABLE", "infra_msg": err_msg}
    except Exception as e:
        err_msg = f"AST architecture analysis execution error: {sanitize_message(str(e))}"
        return False, err_msg, {"error": err_msg, "is_infra": True, "infra_type": "PROCESS_LAUNCH_ERROR", "infra_msg": err_msg}


def create_architecture_f2p_entry(
    arch_passed: bool,
    arch_msg: str,
    arch_details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Construct canonical CTRF entry for the architecture separation F2P node."""
    status = "passed" if arch_passed else "failed"
    entry: dict[str, Any] = {
        "testId": ARCHITECTURE_F2P_NODE_ID,
        "name": "presentation_interaction_and_coordinator_are_separated",
        "status": status,
        "duration": 0,
        "extra": {
            "deepswe": {
                "group": "F2P",
                "required": True,
            }
        },
    }
    if status != "passed":
        entry["message"] = (
            arch_msg
            if arch_msg
            else "Architectural separation failed: presentation, interaction, and coordinator responsibilities must be decoupled"
        )
    return entry


def run_command_with_diagnostics(
    cmd: list[str],
    cwd: Path,
    env: dict[str, str],
    timeout: float = 60.0,
) -> dict[str, Any]:
    clean_cmd = [str(c) for c in cmd]
    try:
        proc = subprocess.run(
            clean_cmd,
            cwd=cwd,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        exit_code = proc.returncode
        stdout = sanitize_message(proc.stdout or "")
        stderr = sanitize_message(proc.stderr or "")
        is_infra = False
        infra_type = None
        infra_msg = None

        if exit_code in (126, 127):
            is_infra = True
            infra_type = "EXECUTABLE_UNAVAILABLE"
            infra_msg = f"Tool or launcher unavailable: '{clean_cmd[0]}' returned exit code {exit_code}"
        elif exit_code < 0:
            is_infra = True
            infra_type = "PROCESS_SIGNAL_TERMINATED"
            infra_msg = f"Process '{clean_cmd[0]}' terminated abnormally by signal {abs(exit_code)}"

        return {
            "cmd": clean_cmd,
            "exit_code": exit_code,
            "stdout": stdout,
            "stderr": stderr,
            "timed_out": False,
            "error": None,
            "is_infra": is_infra,
            "infra_type": infra_type,
            "infra_msg": infra_msg,
        }
    except subprocess.TimeoutExpired as te:
        timeout_msg = f"Command '{clean_cmd[0]}' timed out after {timeout} seconds"
        return {
            "cmd": clean_cmd,
            "exit_code": -1,
            "stdout": sanitize_message(te.stdout or ""),
            "stderr": sanitize_message(te.stderr or ""),
            "timed_out": True,
            "error": timeout_msg,
            "is_infra": True,
            "infra_type": "TIMEOUT",
            "infra_msg": timeout_msg,
        }
    except (FileNotFoundError, PermissionError) as pe:
        launch_err = f"Failed to launch '{clean_cmd[0]}': {pe}"
        return {
            "cmd": clean_cmd,
            "exit_code": 127 if isinstance(pe, FileNotFoundError) else 126,
            "stdout": "",
            "stderr": str(pe),
            "timed_out": False,
            "error": launch_err,
            "is_infra": True,
            "infra_type": "EXECUTABLE_UNAVAILABLE",
            "infra_msg": launch_err,
        }
    except Exception as e:
        unexpected_err = f"Unexpected error launching '{clean_cmd[0]}': {e}"
        return {
            "cmd": clean_cmd,
            "exit_code": -1,
            "stdout": "",
            "stderr": str(e),
            "timed_out": False,
            "error": unexpected_err,
            "is_infra": True,
            "infra_type": "PROCESS_LAUNCH_ERROR",
            "infra_msg": unexpected_err,
        }


def check_src_index_changes(repo_dir: Path, base_commit: str) -> tuple[bool, str]:
    """Verify that any modification to src/index.ts is strictly limited to PolinePicker public export/wiring."""
    target = repo_dir / "src" / "index.ts"
    if not target.is_file():
        return False, "Rule 'core_palette_integrity': src/index.ts was removed or missing, which destroys the core palette library"

    current_hash = compute_sha256(target)
    if current_hash == ORIGINAL_SRC_INDEX_SHA256:
        return True, ""

    diff_lines: list[str] = []
    git_dir = repo_dir / ".git"
    if git_dir.is_dir():
        try:
            out = subprocess.check_output(
                ["git", "-C", str(repo_dir), "diff", "-U0", base_commit, "--", "src/index.ts"],
                text=True,
                stderr=subprocess.DEVNULL,
            )
            diff_lines = out.splitlines()
        except Exception:
            diff_lines = []

    if not diff_lines:
        orig_content = None
        # Try git show first if git directory exists
        if git_dir.is_dir():
            try:
                orig_content = subprocess.check_output(
                    ["git", "-C", str(repo_dir), "show", f"{base_commit}:src/index.ts"],
                    text=True,
                    stderr=subprocess.DEVNULL,
                )
            except Exception:
                pass

        if orig_content is None:
            # Search upwards from hardgate.py
            for p in Path(__file__).resolve().parents:
                cand = p / "source" / "src" / "index.ts"
                if cand.is_file() and compute_sha256(cand) == ORIGINAL_SRC_INDEX_SHA256:
                    orig_content = cand.read_text(encoding="utf-8", errors="ignore")
                    break

        if orig_content is None:
            for cand in [
                repo_dir.parent / "source" / "src" / "index.ts",
                Path("/workspace/source/src/index.ts"),
                Path("/workspace/repo/src/index.ts"),
            ]:
                if cand.is_file() and compute_sha256(cand) == ORIGINAL_SRC_INDEX_SHA256:
                    orig_content = cand.read_text(encoding="utf-8", errors="ignore")
                    break

        if orig_content is None:
            return False, "Rule 'core_palette_integrity': Unable to verify baseline integrity for modified src/index.ts"

        curr_content = target.read_text(encoding="utf-8", errors="ignore")
        diff_lines = list(
            difflib.unified_diff(
                orig_content.splitlines(),
                curr_content.splitlines(),
                n=0,
            )
        )

    removed_lines = [l[1:].strip() for l in diff_lines if l.startswith("-") and not l.startswith("---")]
    added_lines = [l[1:].strip() for l in diff_lines if l.startswith("+") and not l.startswith("+++")]

    if removed_lines:
        non_trivial_removed = [
            l for l in removed_lines
            if l and not l.startswith("//") and not l.startswith("/*") and not l.startswith("*")
        ]
        if non_trivial_removed:
            return False, (
                f"Rule 'core_palette_integrity': Modification to src/index.ts altered existing core palette code "
                f"('{non_trivial_removed[0][:60]}'). Modifying core palette math, color conversion, or interpolation "
                f"is outside the PolinePicker component responsibility boundary."
            )

    for line in added_lines:
        if not line or line.startswith("//") or line.startswith("/*") or line.startswith("*"):
            continue
        is_import_export = (
            re.match(r"^export\s+(?:type\s+)?(?:\{[^}]*\}|\*\s+from\s+['\"][^'\"]+['\"]);?", line)
            or re.match(r"^export\s+(?:default\s+)?(?:class|function|const|let|var|type|interface)\s+([A-Za-z0-9_]+)", line)
            or re.match(r"^import\s+(?:type\s+)?(?:\{[^}]*\}|\*\s+as\s+[A-Za-z0-9_]+|[A-Za-z0-9_]+)\s+from\s+['\"][^'\"]+['\"];?", line)
        )
        if not is_import_export:
            return False, (
                f"Rule 'core_palette_integrity': Added line '{line[:60]}' in src/index.ts is not a valid export or import statement. "
                f"Adding logic or algorithms to src/index.ts is outside the PolinePicker component responsibility boundary."
            )
        allowed_picker_keywords = {"picker", "polinepicker", "webcomponent", "pickerview", "pickerinteraction"}
        line_lower = line.lower()
        if not any(kw in line_lower for kw in allowed_picker_keywords):
            return False, (
                f"Rule 'core_palette_integrity': Export/import '{line[:60]}' in src/index.ts is unrelated to PolinePicker. "
                f"Only PolinePicker public exports and wiring are permitted in src/index.ts."
            )

    return True, ""


_TEST_GRAPH_CACHE: dict[str, dict[str, Any]] = {}


def supporting_test_graph(repo_dir: Path) -> dict[str, Any]:
    """Resolve test helpers by actual static imports, including production reachability."""
    key = str(repo_dir.resolve())
    if key in _TEST_GRAPH_CACHE:
        return _TEST_GRAPH_CACHE[key]
    script = r'''
const ts = require('typescript'), fs = require('fs'), path = require('path');
const root = process.cwd(), files = [];
function walk(dir) {
  if (!fs.existsSync(dir)) return;
  for (const item of fs.readdirSync(dir, {withFileTypes:true})) {
    const file = path.join(dir,item.name);
    if (item.isDirectory()) { if (!['node_modules','.git'].includes(item.name)) walk(file); }
    else files.push(file);
  }
}
walk(path.join(root,'src')); walk(path.join(root,'tests'));
const configPath = ts.findConfigFile(root,ts.sys.fileExists);
const config = configPath ? ts.readConfigFile(configPath,ts.sys.readFile).config : {};
const options = ts.parseJsonConfigFileContent(config || {},ts.sys,root).options;
const graph = new Map(), unknown = new Set();
function resolve(name, file) {
  const resolved = ts.resolveModuleName(name,file,options,ts.sys).resolvedModule;
  if (resolved) return path.resolve(resolved.resolvedFileName);
  if (name.startsWith('.')) {
    const target = path.resolve(path.dirname(file),name);
    if (fs.existsSync(target) && fs.statSync(target).isFile()) return target;
  }
}
for (const file of files) {
  const edges = []; graph.set(file,edges);
  if (!/\.[cm]?[jt]sx?$/.test(file)) continue;
  const sf = ts.createSourceFile(file,fs.readFileSync(file,'utf8'),ts.ScriptTarget.Latest,true);
  function visit(n) {
    let spec;
    if ((ts.isImportDeclaration(n) || ts.isExportDeclaration(n)) && n.moduleSpecifier) spec=n.moduleSpecifier;
    if (ts.isCallExpression(n) && (n.expression.kind===ts.SyntaxKind.ImportKeyword || ts.isIdentifier(n.expression)&&n.expression.text==='require')) {
      spec=n.arguments[0];
      if (!spec || !(ts.isStringLiteral(spec)||ts.isNoSubstitutionTemplateLiteral(spec))) unknown.add(file);
    }
    if (spec && (ts.isStringLiteral(spec)||ts.isNoSubstitutionTemplateLiteral(spec))) {
      const target=resolve(spec.text,file);if(target)edges.push(target);
    }
    ts.forEachChild(n,visit);
  } visit(sf);
}
function reachable(roots) { const seen=new Set(),todo=[...roots];while(todo.length){const f=todo.pop();if(seen.has(f))continue;seen.add(f);todo.push(...(graph.get(f)||[]));}return seen; }
const production=reachable(files.filter(f=>f.startsWith(path.join(root,'src')+path.sep)));
const tests=reachable(files.filter(f=>/\.(test|spec)\.[cm]?[jt]sx?$/.test(f)));
const relative=f=>path.relative(root,f).split(path.sep).join('/');
console.log(JSON.stringify({production:[...production].map(relative),tests:[...tests].map(relative),unknown_production:[...unknown].filter(f=>production.has(f)).map(relative)}));
'''
    proc = subprocess.run(['node', '-e', script], cwd=repo_dir, text=True, capture_output=True, timeout=60)
    if proc.returncode:
        result = {'error': proc.stderr[-1000:]}
    else:
        result = json.loads(proc.stdout)
    _TEST_GRAPH_CACHE[key] = result
    return result


def is_permitted_candidate_path(rel_path: str, repo_dir: Path, base_commit: str) -> tuple[bool, str]:
    """Check if a changed file is within the permitted PolinePicker refactoring scope."""
    p = Path(rel_path)
    parts = p.parts
    if not parts:
        return False, "Path is empty"

    norm = rel_path.replace("\\", "/")

    # 1. Explicit protected files
    if norm == "tests/index.test.ts":
        return False, (
            f"File '{norm}' violated rule 'original_test_protection': "
            f"Modifying original test suite tests/index.test.ts is strictly prohibited."
        )
    if norm in ("tests/grader.py", "tests/test.sh", "tests/config.json"):
        return False, (
            f"File '{norm}' violated rule 'eval_harness_protection': "
            f"Modifying evaluation harness file {norm} is strictly prohibited."
        )
    if norm in ("package.json", "package-lock.json"):
        return False, (
            f"File '{norm}' violated rule 'dependency_protection': "
            f"Modifying package dependencies or lockfile {norm} is prohibited."
        )
    if norm in ("build.js", "tsconfig.json", ".eslintrc", ".prettierrc.json"):
        return False, (
            f"File '{norm}' violated rule 'toolchain_protection': "
            f"Modifying project build or toolchain configuration {norm} is prohibited."
        )
    if norm in ("tea.yaml", "README.md", "LICENSE", ".gitignore"):
        return False, (
            f"File '{norm}' violated rule 'metadata_protection': "
            f"Modifying repository metadata or documentation file {norm} is prohibited."
        )

    # 2. Protected directories
    for pdir in PROTECTED_DIRECTORIES:
        if norm.startswith(pdir) or norm == pdir.rstrip("/"):
            return False, (
                f"File '{norm}' violated rule 'eval_harness_protection': "
                f"Modifying files in protected evaluation or system directory {norm} is prohibited."
            )

    # 3. Special handling for src/index.ts
    if norm == "src/index.ts":
        return check_src_index_changes(repo_dir, base_commit)

    # 4. Files under src/
    if parts[0] == "src":
        allowed_src_exts = {".ts", ".tsx", ".js", ".mjs", ".cjs", ".d.ts", ".css", ".svg", ".md"}
        if p.suffix.lower() not in allowed_src_exts:
            return False, (
                f"File '{norm}' violated rule 'component_scope_restriction': "
                f"File type '{p.suffix}' is not a permitted source or asset file under src/."
            )
        full_p = repo_dir / norm
        if full_p.is_file():
            try:
                content = full_p.read_text(encoding="utf-8", errors="ignore")
                for pat in EVAL_BYPASS_PATTERNS:
                    if re.search(pat, content):
                        return False, (
                            f"File '{norm}' violated rule 'eval_bypass_protection': "
                            f"Contains evaluation bypass or test harness pattern '{pat}'."
                        )
            except Exception:
                pass
        return True, ""

    # 5. Supporting test files under tests/
    if parts[0] == "tests":
        allowed_test_exts = {".ts", ".js", ".mjs", ".cjs"}
        if p.suffix.lower() not in allowed_test_exts:
            return False, (
                f"File '{norm}' violated rule 'supporting_test_scope': "
                f"File type '{p.suffix}' under tests/ is not a permitted test script format."
            )
        existed = subprocess.run(['git', 'cat-file', '-e', f'{base_commit}:{norm}'], cwd=repo_dir, capture_output=True).returncode == 0
        if existed:
            return False, f"Existing test asset '{norm}' is protected by the task contract."
        graph = supporting_test_graph(repo_dir)
        if graph.get('error'):
            return False, f"Cannot establish supporting-test reachability: {graph['error']}"
        if norm in graph['production'] or graph['unknown_production']:
            return False, f"Test asset '{norm}' is runtime-reachable, or runtime imports cannot be resolved."
        if norm not in graph['tests']:
            return False, f"File '{norm}' is not a test entry or reachable support for a test entry."
        full_p = repo_dir / norm
        if full_p.is_file():
            try:
                content = full_p.read_text(encoding="utf-8", errors="ignore")
                for pat in EVAL_BYPASS_PATTERNS:
                    if re.search(pat, content):
                        return False, (
                            f"File '{norm}' violated rule 'eval_bypass_protection': "
                            f"Contains evaluation bypass or test harness pattern '{pat}'."
                        )
            except Exception:
                pass
        return True, ""

    # 6. Any other files outside src/ and tests/
    return False, (
        f"File '{norm}' violated rule 'component_scope_restriction': "
        f"File {norm} is outside the PolinePicker component responsibility boundary "
        f"(only src/ component files and tests/ supporting test files are permitted)."
    )


def snapshot_candidate_changes(repo_dir: Path, base_commit: str, config_path: Path) -> list[str]:
    """Detect modified and added files before running build to avoid flagging dist/ artifacts."""
    git_dir = repo_dir / ".git"
    changed_files: set[str] = set()

    if git_dir.is_dir():
        diff_cmd = ["git", "-C", str(repo_dir), "diff", "--name-only", "--diff-filter=ACDMRTUXB", "HEAD"]
        try:
            out = subprocess.check_output(diff_cmd, text=True, stderr=subprocess.DEVNULL)
            for line in out.splitlines():
                p = line.strip()
                if p and not p.startswith("node_modules") and not p.startswith("dist/"):
                    changed_files.add(p)
        except Exception:
            pass

        staged_cmd = ["git", "-C", str(repo_dir), "diff", "--name-only", "--cached", "--diff-filter=ACDMRTUXB"]
        try:
            out = subprocess.check_output(staged_cmd, text=True, stderr=subprocess.DEVNULL)
            for line in out.splitlines():
                p = line.strip()
                if p and not p.startswith("node_modules") and not p.startswith("dist/"):
                    changed_files.add(p)
        except Exception:
            pass

        untracked_cmd = ["git", "-C", str(repo_dir), "ls-files", "--others", "--exclude-standard"]
        try:
            out = subprocess.check_output(untracked_cmd, text=True, stderr=subprocess.DEVNULL)
            for line in out.splitlines():
                p = line.strip()
                if p and not p.startswith("node_modules") and not p.startswith("dist/"):
                    changed_files.add(p)
        except Exception:
            pass
    else:
        manifest_path = find_source_manifest(repo_dir, config_path)
        if manifest_path and manifest_path.is_file():
            try:
                manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
                expected_files = manifest_data.get("files", {})
                for rel_path, meta in expected_files.items():
                    if rel_path.startswith("dist/"):
                        continue
                    full_p = repo_dir / rel_path
                    if not full_p.is_file():
                        changed_files.add(rel_path)
                    else:
                        current_hash = compute_sha256(full_p)
                        if current_hash != meta.get("sha256"):
                            changed_files.add(rel_path)
                for root, dirs, files in os.walk(repo_dir):
                    if "node_modules" in root or ".git" in root or "dist" in root:
                        continue
                    for f in files:
                        p = Path(root) / f
                        rel = str(p.relative_to(repo_dir)).replace("\\", "/")
                        if rel not in expected_files:
                            changed_files.add(rel)
            except Exception:
                pass

    return sorted(changed_files)


def validate_hard_gate_schema(
    data: dict[str, Any],
    expected_p2p_list: list[str] | None = None,
    expected_cheat_nodes: list[str] | None = None,
) -> tuple[bool, list[str]]:
    """Strictly validate Hard Gate report schema, types, P2P reconciliation, and bidirectional consistency."""
    errors: list[str] = []

    # 1. Required top-level keys & exact types
    required_keys = {
        "passed": bool,
        "apply_failed": bool,
        "failed_nodes": list,
        "nodes": list,
        "p2p_summary": dict,
        "p2p_results": list,
        "compile_paths": list,
        "candidate_changed_paths": list,
        "protected_changes": list,
        "test_bypass": dict,
        "cheat_reasons": list,
        "compile_errors": dict,
        "infra_errors": dict,
    }
    for k, t in required_keys.items():
        if k not in data:
            errors.append(f"Missing required key '{k}'")
        elif not isinstance(data[k], t):
            errors.append(f"Key '{k}' expected {t.__name__}, got {type(data[k]).__name__}")

    if errors:
        return False, errors

    # Strict boolean checks (not just int subclasses)
    if not isinstance(data["passed"], bool):
        errors.append(f"Key 'passed' must be bool, got {type(data['passed']).__name__}")
    if not isinstance(data["apply_failed"], bool):
        errors.append(f"Key 'apply_failed' must be bool, got {type(data['apply_failed']).__name__}")

    # 2. String array field validations
    string_array_fields = [
        "compile_paths",
        "candidate_changed_paths",
        "protected_changes",
        "cheat_reasons",
        "failed_nodes",
    ]
    for fld in string_array_fields:
        for idx, item in enumerate(data[fld]):
            if not isinstance(item, str):
                errors.append(f"Item {idx} in '{fld}' must be str, got {type(item).__name__}")

    # failed_nodes must be unique
    failed_nodes_list = data["failed_nodes"]
    if len(failed_nodes_list) != len(set(failed_nodes_list)):
        errors.append("failed_nodes contains duplicate entries")
    failed_nodes_set = set(failed_nodes_list)

    # 3. Test bypass structure
    tb = data["test_bypass"]
    if "detected" not in tb or not isinstance(tb["detected"], bool):
        errors.append("test_bypass.detected must be a bool")
    if "findings" not in tb or not isinstance(tb["findings"], list):
        errors.append("test_bypass.findings must be a list")
    else:
        for idx, f in enumerate(tb["findings"]):
            if not isinstance(f, str):
                errors.append(f"test_bypass.findings[{idx}] must be str")

    # 4. Check Nodes validation
    nodes_list = data["nodes"]
    if not nodes_list:
        errors.append("Report 'nodes' list cannot be empty")
    seen_node_ids: set[str] = set()
    failed_check_node_ids: set[str] = set()

    for idx, n in enumerate(nodes_list):
        if not isinstance(n, dict):
            errors.append(f"nodes[{idx}] must be a dict")
            continue
        for req in ("node_id", "status", "description", "message"):
            if req not in n:
                errors.append(f"nodes[{idx}] missing '{req}'")
        nid = n.get("node_id")
        if not isinstance(nid, str) or not nid.strip():
            errors.append(f"nodes[{idx}] 'node_id' must be non-empty str")
        elif nid in seen_node_ids:
            errors.append(f"Duplicate node_id '{nid}' in nodes list")
        else:
            seen_node_ids.add(nid)

        st = n.get("status")
        if st not in ("passed", "failed"):
            errors.append(f"nodes[{idx}] status must be 'passed' or 'failed', got '{st}'")
        elif st == "failed":
            if nid:
                failed_check_node_ids.add(nid)

        if not isinstance(n.get("description"), str):
            errors.append(f"nodes[{idx}] 'description' must be str")
        if not isinstance(n.get("message"), str):
            errors.append(f"nodes[{idx}] 'message' must be str")

    # Required check nodes presence
    missing_req_nodes = set(REQUIRED_HARD_GATE_NODE_IDS) - seen_node_ids
    if missing_req_nodes:
        errors.append(f"Missing required check node(s) in report nodes: {sorted(list(missing_req_nodes))}")

    # Required cheat nodes presence (cannot bypass by deleting cheat nodes from config)
    all_expected_cheats = set(expected_cheat_nodes or []) | set(REQUIRED_CHEAT_NODE_IDS)
    missing_cheats = all_expected_cheats - seen_node_ids
    if missing_cheats:
        errors.append(f"Missing required cheat node(s) in report nodes: {sorted(list(missing_cheats))}")

    # 5. P2P results reconciliation
    p2p_res = data["p2p_results"]
    expected_p2p_count = len(expected_p2p_list) if expected_p2p_list else EXPECTED_P2P_COUNT
    if len(p2p_res) != expected_p2p_count:
        errors.append(f"p2p_results length ({len(p2p_res)}) != expected ({expected_p2p_count})")

    p2p_ids_seen: list[str] = []
    failed_p2p_ids: set[str] = set()
    actual_passed = 0
    actual_failed = 0

    expected_p2p_set = set(expected_p2p_list) if expected_p2p_list else None

    for idx, pr in enumerate(p2p_res):
        if not isinstance(pr, dict):
            errors.append(f"p2p_results[{idx}] must be a dict")
            continue
        for req in ("testId", "name", "status", "duration"):
            if req not in pr:
                errors.append(f"p2p_results[{idx}] missing '{req}'")

        tid = pr.get("testId")
        if not isinstance(tid, str) or not tid.strip():
            errors.append(f"p2p_results[{idx}] invalid testId '{tid}'")
        else:
            p2p_ids_seen.append(tid)
            if expected_p2p_set is not None and tid not in expected_p2p_set:
                errors.append(f"p2p_results[{idx}] testId '{tid}' is not in expected P2P node set (forged or unrecognized ID)")

        st = pr.get("status")
        if st == "passed":
            actual_passed += 1
        elif st == "failed":
            actual_failed += 1
            if tid:
                failed_p2p_ids.add(tid)
        else:
            errors.append(f"p2p_results[{idx}] status must be 'passed' or 'failed', got '{st}'")

        dur = pr.get("duration")
        if not (isinstance(dur, (int, float)) and not isinstance(dur, bool) and dur >= 0):
            errors.append(f"p2p_results[{idx}] 'duration' must be non-negative number, got '{dur}'")

    # Check P2P uniqueness
    if len(p2p_ids_seen) != len(set(p2p_ids_seen)):
        errors.append("p2p_results contains duplicate testId entries")

    # Check exact P2P set equality
    if expected_p2p_set is not None:
        actual_p2p_set = set(p2p_ids_seen)
        missing_p2p = expected_p2p_set - actual_p2p_set
        extra_p2p = actual_p2p_set - expected_p2p_set
        if missing_p2p:
            errors.append(f"p2p_results is missing required P2P test(s): {sorted(list(missing_p2p))[:5]}")
        if extra_p2p:
            errors.append(f"p2p_results contains extra/unexpected P2P test(s): {sorted(list(extra_p2p))[:5]}")

    # 6. P2P summary checks
    summary = data["p2p_summary"]
    for sk in ("total", "passed", "failed"):
        if sk not in summary or not isinstance(summary[sk], int) or isinstance(summary[sk], bool):
            errors.append(f"p2p_summary missing or invalid int for '{sk}'")

    if isinstance(summary.get("total"), int) and not isinstance(summary.get("total"), bool):
        if summary["total"] != expected_p2p_count:
            errors.append(f"p2p_summary total ({summary['total']}) != expected ({expected_p2p_count})")

    if (
        isinstance(summary.get("total"), int)
        and isinstance(summary.get("passed"), int)
        and isinstance(summary.get("failed"), int)
        and not isinstance(summary.get("passed"), bool)
        and not isinstance(summary.get("failed"), bool)
    ):
        if summary["passed"] != actual_passed:
            errors.append(f"p2p_summary passed ({summary['passed']}) != actual passed count ({actual_passed})")
        if summary["failed"] != actual_failed:
            errors.append(f"p2p_summary failed ({summary['failed']}) != actual failed count ({actual_failed})")
        if summary["passed"] + summary["failed"] != summary["total"]:
            errors.append(
                f"p2p_summary passed ({summary['passed']}) + failed ({summary['failed']}) != total ({summary['total']})"
            )

    # 7. Exact Bidirectional Consistency for failed_nodes
    expected_failed_nodes = failed_check_node_ids | failed_p2p_ids

    missing_in_failed_nodes = expected_failed_nodes - failed_nodes_set
    if missing_in_failed_nodes:
        errors.append(f"failed_nodes is missing actual failed items: {sorted(list(missing_in_failed_nodes))}")

    extra_in_failed_nodes = failed_nodes_set - expected_failed_nodes
    if extra_in_failed_nodes:
        errors.append(f"failed_nodes contains passed/unfailed items: {sorted(list(extra_in_failed_nodes))}")

    # 8. Top-level passed consistency
    passed = data["passed"]

    # Any failed P2P or check node strictly forbids passed=True
    if actual_failed > 0 and passed is True:
        errors.append(f"passed is True but {actual_failed} P2P test(s) failed")

    if passed is True:
        if bool(data.get("infra_errors")):
            errors.append("passed is True but infra_errors is non-empty")
        if data["apply_failed"] is not False:
            errors.append("passed is True but apply_failed is True")
        if failed_nodes_list:
            errors.append(f"passed is True but failed_nodes is non-empty: {failed_nodes_list}")
        if expected_failed_nodes:
            errors.append(f"passed is True but expected_failed_nodes is non-empty: {sorted(list(expected_failed_nodes))}")
        if summary.get("passed") != expected_p2p_count:
            errors.append(f"passed is True but p2p_summary passed ({summary.get('passed')}) != {expected_p2p_count}")
    else:
        has_failure_reason = (
            bool(failed_nodes_list)
            or bool(data.get("apply_failed"))
            or bool(data.get("infra_errors"))
        )
        if not has_failure_reason:
            errors.append("passed is False but failed_nodes is empty, apply_failed is False, and infra_errors is empty")

    return len(errors) == 0, errors


def run_hard_gate(
    config_path: Path,
    repo_dir: Path,
    output_path: Path,
    apply_failed: int = 0,
) -> dict[str, Any]:
    nodes: list[NodeResult] = []
    compile_errors: dict[str, Any] = {}
    infra_errors: dict[str, Any] = {}
    cheat_reasons: list[str] = []
    protected_changes: list[str] = []
    test_bypass_findings: list[str] = []

    config: dict[str, Any] = {}
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except Exception as e:
        infra_errors["config_read"] = str(e)

    base_commit = config.get("base_commit", "c0bf44b06d549eb7bd5ecc1ac84cd3c58eb296cc")
    p2p_config_nodes = config.get("p2p", [])
    expected_cheat_nodes = config.get("hard_gate", {}).get("cheat_nodes", REQUIRED_CHEAT_NODE_IDS)

    # 1. Candidate patch application check
    patch_applied = (apply_failed == 0)
    nodes.append(
        NodeResult(
            node_id="candidate_patch_apply",
            passed=patch_applied,
            description="Candidate patch application check",
            message="Patch applied cleanly" if patch_applied else "Candidate patch failed to apply to base commit",
        )
    )

    # 2. Repository baseline commit and directory integrity check
    repo_ok = repo_dir.is_dir()
    repo_msg = "Repository directory exists and is valid"
    if not repo_ok:
        repo_msg = f"Repository directory {repo_dir} does not exist"
    else:
        git_dir = repo_dir / ".git"
        if git_dir.is_dir():
            try:
                head_rev = subprocess.check_output(
                    ["git", "-C", str(repo_dir), "rev-parse", "HEAD"],
                    text=True,
                ).strip()
                if head_rev != base_commit:
                    repo_ok = False
                    repo_msg = f"HEAD commit {head_rev} does not match base_commit {base_commit}"
            except Exception as e:
                repo_ok = False
                repo_msg = f"Failed to check git commit: {e}"

    nodes.append(
        NodeResult(
            node_id="repository_baseline_integrity",
            passed=repo_ok,
            description="Repository baseline commit and directory integrity check",
            message=repo_msg,
        )
    )

    # 3. Project configuration integrity check
    required_configs = ["package.json", "tsconfig.json", ".eslintrc", ".prettierrc.json", "build.js"]
    missing_configs = [cfg for cfg in required_configs if not (repo_dir / cfg).is_file()]
    configs_valid = len(missing_configs) == 0
    config_msg = "All required configuration files exist and are readable"
    if not configs_valid:
        config_msg = f"Missing required configuration files: {missing_configs}"
    nodes.append(
        NodeResult(
            node_id="project_configuration_integrity",
            passed=configs_valid,
            description="Project build and lint configuration integrity check",
            message=config_msg,
        )
    )

    # 4. Runtime toolchain and node_modules availability check
    node_bin_ok = True
    dep_msg = "Node and toolchain dependencies are available"
    try:
        node_res = subprocess.run(["node", "--version"], capture_output=True, text=True, timeout=10)
        if node_res.returncode != 0:
            node_bin_ok = False
            dep_msg = f"Node returned non-zero code: {sanitize_message(node_res.stderr)}"
    except Exception as e:
        node_bin_ok = False
        dep_msg = f"Failed to execute node: {sanitize_message(str(e))}"

    if not (repo_dir / "node_modules").is_dir():
        node_bin_ok = False
        dep_msg = "node_modules directory is missing in repository"

    if not node_bin_ok:
        infra_errors["build_dependency"] = {
            "error_type": "DEPENDENCY_OR_TOOL_UNAVAILABLE",
            "message": dep_msg,
        }

    nodes.append(
        NodeResult(
            node_id="build_dependency_integrity",
            passed=node_bin_ok,
            description="Runtime toolchain and node_modules availability check",
            message=dep_msg,
        )
    )

    # 5. P2P manifest integrity check
    p2p_manifest_path = find_p2p_manifest(config_path)
    manifest_lines: list[str] = []
    manifest_ok = False
    manifest_msg = ""
    if p2p_manifest_path and p2p_manifest_path.is_file():
        manifest_lines = [
            line.strip()
            for line in p2p_manifest_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        if len(manifest_lines) == EXPECTED_P2P_COUNT:
            if len(set(manifest_lines)) == EXPECTED_P2P_COUNT:
                manifest_ok = True
                manifest_msg = f"P2P manifest verified with exactly {EXPECTED_P2P_COUNT} unique nodes"
            else:
                manifest_msg = f"P2P manifest contains duplicate entries: {len(manifest_lines)} total vs {len(set(manifest_lines))} unique"
        else:
            manifest_msg = f"P2P manifest has {len(manifest_lines)} lines, expected {EXPECTED_P2P_COUNT}"
    else:
        manifest_msg = "P2P manifest file p2p_select.txt not found"

    if not manifest_ok:
        infra_errors["p2p_manifest"] = {
            "error_type": "EVAL_HARNESS_ERROR",
            "message": manifest_msg,
        }

    nodes.append(
        NodeResult(
            node_id="p2p_manifest_integrity",
            passed=manifest_ok,
            description="P2P manifest existence, line count, and uniqueness check",
            message=manifest_msg,
        )
    )

    # 6. Consistency between config.json and p2p_select.txt
    config_p2p_ok = False
    config_p2p_msg = ""
    orig_count = len(manifest_lines)
    if (
        len(p2p_config_nodes) >= orig_count
        and len(set(p2p_config_nodes)) == len(p2p_config_nodes)
        and p2p_config_nodes[:orig_count] == manifest_lines
    ):
        added_nodes = p2p_config_nodes[orig_count:]
        all_added_valid = all(isinstance(n, str) and n.startswith("P2P::") for n in added_nodes)
        if all_added_valid:
            config_p2p_ok = True
            config_p2p_msg = (
                f"config.json P2P contains {orig_count} original tests matching manifest and "
                f"{len(added_nodes)} added Picker regression tests ({len(p2p_config_nodes)} total unique nodes)"
            )
        else:
            config_p2p_msg = "config.json added P2P tests must all start with 'P2P::'"
    else:
        diff_manifest = set(manifest_lines) - set(p2p_config_nodes[:orig_count])
        config_p2p_msg = (
            f"config.json P2P ({len(p2p_config_nodes)} entries) does not match manifest at prefix: missing {diff_manifest}"
        )

    nodes.append(
        NodeResult(
            node_id="config_p2p_integrity",
            passed=config_p2p_ok,
            description="Consistency between config.json and p2p_select.txt",
            message=config_p2p_msg,
        )
    )

    candidate_changed_paths = snapshot_candidate_changes(repo_dir, base_commit, config_path)

    # 7. Anti-Cheat: Protected Paths Check
    protected_violation = False
    protected_msg = "No protected evaluation or configuration paths modified"
    for p in candidate_changed_paths:
        norm_p = p.replace("\\", "/")
        if norm_p in EXPLICIT_PROTECTED_FILES:
            protected_changes.append(p)
            protected_violation = True
        else:
            for pdir in PROTECTED_DIRECTORIES:
                if norm_p.startswith(pdir) or norm_p == pdir.rstrip("/"):
                    protected_changes.append(p)
                    protected_violation = True
                    break

    if protected_violation:
        protected_msg = f"Candidate modified protected paths: {protected_changes}"
        cheat_reasons.append(protected_msg)

    nodes.append(
        NodeResult(
            node_id="anti_cheat_protected_paths",
            passed=not protected_violation,
            description="Check that protected tests, config, and evaluation assets are not modified",
            message=protected_msg,
            details={"protected_changes": protected_changes},
        )
    )

    # 8. Anti-Cheat: Original Test Tampering Check
    test_file_path = repo_dir / "tests" / "index.test.ts"
    test_tampered = False
    test_tamper_msg = "Original tests/index.test.ts is untouched and verified by SHA-256"
    if not test_file_path.is_file():
        test_tampered = True
        test_tamper_msg = "Original tests/index.test.ts was removed or renamed"
        cheat_reasons.append(test_tamper_msg)
    else:
        actual_test_sha = compute_sha256(test_file_path)
        if actual_test_sha != EXPECTED_INDEX_TEST_SHA256:
            test_tampered = True
            test_tamper_msg = (
                f"tests/index.test.ts hash mismatch: got {actual_test_sha}, expected {EXPECTED_INDEX_TEST_SHA256}"
            )
            cheat_reasons.append(test_tamper_msg)

    nodes.append(
        NodeResult(
            node_id="anti_cheat_test_tampering",
            passed=not test_tampered,
            description="Verify original tests/index.test.ts file integrity",
            message=test_tamper_msg,
        )
    )

    cmd_env = get_environment_with_node_modules(repo_dir)

    # 9. Anti-Cheat: Test Bypass Check (.only / .skip / fit / etc.)
    test_bypass_detected = False
    test_bypass_msg = "No test bypass or skip mechanisms detected in test files or candidate source"
    files_to_scan = [test_file_path]
    src_dir = repo_dir / "src"
    if src_dir.is_dir():
        for root, dirs, files in os.walk(src_dir):
            for f in files:
                if f.endswith(".ts") or f.endswith(".js"):
                    files_to_scan.append(Path(root) / f)

    # Other files under tests/ are candidate-authored or evaluator-supplied
    # suites outside the original graded file. Skipping their own tests cannot
    # hide a graded node, so only focus modifiers (.only / fit / fdescribe),
    # which can change which tests run, are disallowed there.
    extra_test_files = []
    tests_dir = repo_dir / "tests"
    if tests_dir.is_dir():
        for root, dirs, files in os.walk(tests_dir):
            if "verifier" in root or "verify" in root:
                continue
            for f in files:
                if (f.endswith(".ts") or f.endswith(".js")) and (Path(root) / f) != test_file_path:
                    extra_test_files.append(Path(root) / f)

    test_bypass_findings = scan_test_bypass_ast(files_to_scan, repo_dir, cmd_env)
    focus_finding = re.compile(r"'(?:\w+\.only|fit|fdescribe)(?:\(\.\.\.\))?'|scanner failed")
    test_bypass_findings += [
        finding for finding in scan_test_bypass_ast(extra_test_files, repo_dir, cmd_env)
        if focus_finding.search(finding)
    ]
    if test_bypass_findings:
        test_bypass_detected = True
        test_bypass_msg = f"Test bypass detected: {test_bypass_findings}"
        for f in test_bypass_findings:
            cheat_reasons.append(f)

    nodes.append(
        NodeResult(
            node_id="anti_cheat_test_bypass",
            passed=not test_bypass_detected,
            description="Detect .only, .skip, focused tests, or test skipping mechanisms",
            message=test_bypass_msg,
            details={"findings": test_bypass_findings},
        )
    )

    # 10. Anti-Cheat: Fair Scope Restriction Check
    scope_violation = False
    scope_msg = "Candidate modifications are within the permitted PolinePicker responsibility boundary"
    out_of_scope_files: list[str] = []
    for cp in candidate_changed_paths:
        permitted, reason = is_permitted_candidate_path(cp, repo_dir, base_commit)
        if not permitted:
            out_of_scope_files.append(f"{cp} ({reason})")
            scope_violation = True

    if scope_violation:
        scope_msg = f"Candidate modified out-of-scope files: {out_of_scope_files}"
        cheat_reasons.append(scope_msg)

    nodes.append(
        NodeResult(
            node_id="anti_cheat_scope_restriction",
            passed=not scope_violation,
            description="Ensure candidate changes remain within the PolinePicker refactoring boundary",
            message=scope_msg,
            details={"out_of_scope_files": out_of_scope_files},
        )
    )

    # 11. Anti-Cheat: Evaluation Bypass Check
    eval_bypass_detected = False
    eval_bypass_msg = "No evaluation harness references or cheating detected in candidate files"
    eval_findings: list[str] = []
    for cp in candidate_changed_paths:
        target_f = repo_dir / cp
        if target_f.is_file():
            try:
                content = target_f.read_text(encoding="utf-8", errors="ignore")
                for pat in EVAL_BYPASS_PATTERNS:
                    if re.search(pat, content):
                        finding = f"Evaluation internal pattern '{pat}' referenced in {cp}"
                        eval_findings.append(finding)
                        eval_bypass_detected = True
                        cheat_reasons.append(finding)
            except Exception:
                pass

    if eval_bypass_detected:
        eval_bypass_msg = f"Evaluation bypass detected: {eval_findings}"

    nodes.append(
        NodeResult(
            node_id="anti_cheat_eval_bypass",
            passed=not eval_bypass_detected,
            description="Detect evaluation bypass, test harness sniffing, or hardcoded mock branches",
            message=eval_bypass_msg,
            details={"findings": eval_findings},
        )
    )

    # 12. Anti-Cheat: Dependency Tampering Check
    dep_tampered = any(p in ("package.json", "package-lock.json") for p in candidate_changed_paths)
    dep_cheat_msg = "Package manager configurations are unmodified"
    if dep_tampered:
        dep_cheat_msg = "package.json or package-lock.json modified by candidate"
        cheat_reasons.append(dep_cheat_msg)

    nodes.append(
        NodeResult(
            node_id="anti_cheat_dependency_tampering",
            passed=not dep_tampered,
            description="Ensure candidate does not modify package dependencies or lockfiles",
            message=dep_cheat_msg,
        )
    )

    # 13. TypeScript Typecheck
    tsc_diag = run_command_with_diagnostics(["npx", "tsc", "--build"], repo_dir, cmd_env, timeout=60.0)
    if tsc_diag.get("is_infra"):
        tsc_passed = False
        tsc_msg = f"TypeScript typecheck infrastructure failure: {tsc_diag['infra_msg']}"
        infra_errors["tsc"] = {
            "error_type": tsc_diag["infra_type"],
            "message": tsc_diag["infra_msg"],
            "exit_code": tsc_diag["exit_code"],
        }
    elif tsc_diag["exit_code"] != 0:
        tsc_passed = False
        tsc_msg = f"tsc --build failed with code {tsc_diag['exit_code']}: {tsc_diag['stderr'] or tsc_diag['stdout']}"
        compile_errors["tsc"] = tsc_diag
    else:
        tsc_passed = True
        tsc_msg = "TypeScript type checking passed cleanly"

    nodes.append(
        NodeResult(
            node_id="typescript_typecheck",
            passed=tsc_passed,
            description="TypeScript project build and type check (npx tsc --build)",
            message=tsc_msg,
            details={"exit_code": tsc_diag["exit_code"], "timed_out": tsc_diag["timed_out"]},
        )
    )

    # 14. ESLint Check
    eslint_diag = run_command_with_diagnostics(
        ["npx", "eslint", ".", "--ext", ".ts"], repo_dir, cmd_env, timeout=60.0
    )
    if eslint_diag.get("is_infra"):
        eslint_passed = False
        eslint_msg = f"ESLint infrastructure failure: {eslint_diag['infra_msg']}"
        infra_errors["eslint"] = {
            "error_type": eslint_diag["infra_type"],
            "message": eslint_diag["infra_msg"],
            "exit_code": eslint_diag["exit_code"],
        }
    elif eslint_diag["exit_code"] != 0:
        eslint_passed = False
        eslint_msg = f"ESLint failed with code {eslint_diag['exit_code']}: {eslint_diag['stderr'] or eslint_diag['stdout']}"
        compile_errors["eslint"] = eslint_diag
    else:
        eslint_passed = True
        eslint_msg = "ESLint code style and linting passed cleanly"

    nodes.append(
        NodeResult(
            node_id="eslint_lint_check",
            passed=eslint_passed,
            description="ESLint code quality check (npx eslint . --ext .ts)",
            message=eslint_msg,
            details={"exit_code": eslint_diag["exit_code"], "timed_out": eslint_diag["timed_out"]},
        )
    )

    # 15. Prettier Check
    prettier_diag = run_command_with_diagnostics(
        ["npx", "prettier", "--check", "./src/"], repo_dir, cmd_env, timeout=60.0
    )
    if prettier_diag.get("is_infra"):
        prettier_passed = False
        prettier_msg = f"Prettier infrastructure failure: {prettier_diag['infra_msg']}"
        infra_errors["prettier"] = {
            "error_type": prettier_diag["infra_type"],
            "message": prettier_diag["infra_msg"],
            "exit_code": prettier_diag["exit_code"],
        }
    elif prettier_diag["exit_code"] != 0:
        prettier_passed = False
        prettier_msg = f"Prettier failed with code {prettier_diag['exit_code']}: {prettier_diag['stderr'] or prettier_diag['stdout']}"
        compile_errors["prettier"] = prettier_diag
    else:
        prettier_passed = True
        prettier_msg = "Prettier code formatting check passed"

    nodes.append(
        NodeResult(
            node_id="prettier_format_check",
            passed=prettier_passed,
            description="Prettier formatting validation (npx prettier --check ./src/)",
            message=prettier_msg,
            details={"exit_code": prettier_diag["exit_code"], "timed_out": prettier_diag["timed_out"]},
        )
    )

    # 16. Production Build Check
    build_diag = run_command_with_diagnostics(["node", "./build.js"], repo_dir, cmd_env, timeout=60.0)
    if build_diag.get("is_infra"):
        build_passed = False
        build_msg = f"build.js infrastructure failure: {build_diag['infra_msg']}"
        infra_errors["build"] = {
            "error_type": build_diag["infra_type"],
            "message": build_diag["infra_msg"],
            "exit_code": build_diag["exit_code"],
        }
    elif build_diag["exit_code"] != 0:
        build_passed = False
        build_msg = f"build.js failed with code {build_diag['exit_code']}: {build_diag['stderr'] or build_diag['stdout']}"
        compile_errors["build"] = build_diag
    else:
        build_passed = True
        build_msg = "Production bundling and build succeeded (node ./build.js)"

    nodes.append(
        NodeResult(
            node_id="production_build",
            passed=build_passed,
            description="Production bundling with esbuild (node ./build.js)",
            message=build_msg,
            details={"exit_code": build_diag["exit_code"], "timed_out": build_diag["timed_out"]},
        )
    )

    # 17. Architectural Separation Analysis (Evaluated as F2P node)
    arch_passed, arch_msg, arch_details = check_architecture_separation(repo_dir, cmd_env)
    if arch_details.get("is_infra"):
        infra_errors["architecture_separation"] = {
            "error_type": arch_details.get("infra_type", "ARCHITECTURE_ANALYSIS_INFRA_ERROR"),
            "message": arch_details.get("infra_msg", arch_msg),
        }

    architecture_result = {
        "node_id": ARCHITECTURE_F2P_NODE_ID,
        "passed": arch_passed,
        "message": arch_msg,
        "details": arch_details,
    }

    # 18, 19, 20. Test Collection & Execution via Vitest
    expected_p2p_list = [str(n) for n in p2p_config_nodes]
    expected_f2p_list = [str(n) for n in config.get("f2p", [])]
    expected_total_p2p = len(expected_p2p_list)

    # 1. Raw execution records tracking to detect duplicates without dict overwriting
    raw_p2p_test_ids: list[str] = []
    raw_p2p_records_by_id: dict[str, list[dict[str, Any]]] = {}

    test_collection_ok = False
    test_collection_msg = ""
    test_count_ok = False
    test_count_msg = ""
    p2p_exec_ok = False
    p2p_exec_msg = ""

    # Execute tests/index.test.ts (original P2P tests)
    vitest_diag = run_command_with_diagnostics(
        ["npx", "vitest", "run", "tests/index.test.ts", "--reporter=json"],
        repo_dir,
        cmd_env,
        timeout=120.0,
    )

    index_exec_ok = False
    if vitest_diag.get("is_infra"):
        test_collection_msg = f"Vitest execution infrastructure failure: {vitest_diag['infra_msg']}"
        infra_errors["vitest_index"] = {
            "error_type": vitest_diag["infra_type"],
            "message": vitest_diag["infra_msg"],
            "exit_code": vitest_diag["exit_code"],
        }
    elif not vitest_diag["stdout"].strip():
        test_collection_msg = f"Vitest execution failed to start: {vitest_diag['stderr'] or vitest_diag['error']}"
        infra_errors["vitest_index"] = {
            "error_type": "NO_STDOUT",
            "message": test_collection_msg,
            "stderr": vitest_diag["stderr"],
        }
    else:
        try:
            vitest_json = json.loads(vitest_diag["stdout"])
            test_results = vitest_json.get("testResults", [])
            assertion_count = sum(len(tf.get("assertionResults", [])) for tf in test_results)
            if test_results and assertion_count > 0:
                index_exec_ok = True
                test_collection_msg = "Vitest successfully executed tests/index.test.ts"

                for test_file in test_results:
                    for a in test_file.get("assertionResults", []):
                        ancestors = a.get("ancestorTitles", [])
                        title = a.get("title", "")
                        if ancestors:
                            node_id = f"tests/index.test.ts::{'::'.join(ancestors)}::{title}"
                        else:
                            node_id = f"tests/index.test.ts::{title}"

                        status = str(a.get("status", "failed"))
                        duration = float(a.get("duration", 0) or 0)
                        failure_messages = a.get("failureMessages", [])

                        raw_p2p_test_ids.append(node_id)
                        if node_id not in raw_p2p_records_by_id:
                            raw_p2p_records_by_id[node_id] = []
                        raw_p2p_records_by_id[node_id].append({
                            "testId": node_id,
                            "name": title,
                            "status": status,
                            "duration": duration,
                            "failureMessages": failure_messages,
                        })
            else:
                test_collection_msg = "Vitest runner collected 0 tests from tests/index.test.ts due to launch failure"
                infra_errors["vitest_index"] = {
                    "error_type": "ZERO_TESTS_COLLECTED",
                    "message": test_collection_msg,
                }
        except Exception as e:
            test_collection_msg = f"Failed to parse Vitest index output: {e}"
            infra_errors["vitest_index"] = {
                "error_type": "MALFORMED_JSON",
                "message": test_collection_msg,
                "stdout_snippet": vitest_diag["stdout"][:200],
            }

    # Execute tests/deep_swe_verifier_poline_picker.test.ts strictly for P2P tests
    picker_test_file = repo_dir / "tests" / "deep_swe_verifier_poline_picker.test.ts"
    picker_exec_ok = True
    picker_p2p_env = dict(cmd_env)
    picker_p2p_env["PICKER_TEST_FILTER"] = "P2P"

    if not picker_test_file.is_file():
        picker_exec_ok = False
        test_collection_msg += "; tests/deep_swe_verifier_poline_picker.test.ts is missing in repository"
        infra_errors["test_harness"] = {
            "error_type": "TEST_FILE_MISSING",
            "message": "tests/deep_swe_verifier_poline_picker.test.ts is missing in repository",
        }
    else:
        vitest_picker_diag = run_command_with_diagnostics(
            ["npx", "vitest", "run", "tests/deep_swe_verifier_poline_picker.test.ts", "-t", "P2P::", "--reporter=json"],
            repo_dir,
            picker_p2p_env,
            timeout=120.0,
        )
        if vitest_picker_diag.get("is_infra"):
            picker_exec_ok = False
            test_collection_msg += f"; tests/deep_swe_verifier_poline_picker.test.ts infrastructure failure: {vitest_picker_diag['infra_msg']}"
            infra_errors["vitest_picker"] = {
                "error_type": vitest_picker_diag["infra_type"],
                "message": vitest_picker_diag["infra_msg"],
                "exit_code": vitest_picker_diag["exit_code"],
            }
        elif not vitest_picker_diag["stdout"].strip():
            picker_exec_ok = False
            test_collection_msg += f"; tests/deep_swe_verifier_poline_picker.test.ts produced no stdout: {vitest_picker_diag['stderr'] or vitest_picker_diag['error']}"
            infra_errors["vitest_picker"] = {
                "error_type": "NO_STDOUT",
                "message": "Vitest picker produced no stdout",
                "stderr": vitest_picker_diag["stderr"],
            }
        else:
            try:
                picker_json = json.loads(vitest_picker_diag["stdout"])
                picker_results = picker_json.get("testResults", [])
                assertion_count = sum(len(tf.get("assertionResults", [])) for tf in picker_results)
                if picker_results and assertion_count > 0:
                    for test_file in picker_results:
                        for a in test_file.get("assertionResults", []):
                            title = str(a.get("title", "")).strip()
                            raw_status = str(a.get("status", "failed"))
                            duration = float(a.get("duration", 0) or 0)
                            fail_msgs = a.get("failureMessages", [])

                            raw_p2p_test_ids.append(title)
                            if title not in raw_p2p_records_by_id:
                                raw_p2p_records_by_id[title] = []
                            raw_p2p_records_by_id[title].append({
                                "testId": title,
                                "name": title.split("::")[-1] if "::" in title else title,
                                "status": raw_status,
                                "duration": duration,
                                "failureMessages": fail_msgs,
                            })
                else:
                    picker_exec_ok = False
                    test_collection_msg += "; tests/deep_swe_verifier_poline_picker.test.ts runner collected 0 tests"
                    infra_errors["vitest_picker"] = {
                        "error_type": "ZERO_TESTS_COLLECTED",
                        "message": "Vitest runner collected 0 P2P tests from tests/deep_swe_verifier_poline_picker.test.ts",
                    }
            except Exception as e:
                picker_exec_ok = False
                test_collection_msg += f"; Failed to parse Vitest picker output: {e}"
                infra_errors["vitest_picker"] = {
                    "error_type": "MALFORMED_JSON",
                    "message": f"Failed to parse Vitest picker output: {e}",
                    "stdout_snippet": vitest_picker_diag["stdout"][:200],
                }

    # 2. Strict ID verification and anomaly detection
    # A. Internal duplicate P2P test detection (without dict overwrites)
    seen_ids: set[str] = set()
    duplicate_p2p_ids: list[str] = []
    for tid in raw_p2p_test_ids:
        if tid in seen_ids and tid not in duplicate_p2p_ids:
            duplicate_p2p_ids.append(tid)
        seen_ids.add(tid)

    # B. Detection of any F2P tests in Hard Gate (Hard Gate MUST execute zero F2P tests)
    leaked_f2p_ids: list[str] = [
        tid for tid in raw_p2p_test_ids
        if tid.startswith("F2P::") or tid in expected_f2p_list
    ]

    # C. Missing P2P test IDs relative to config.json
    missing_p2p_ids: list[str] = sorted(list(set(expected_p2p_list) - set(raw_p2p_test_ids)))

    # D. Extra P2P test IDs relative to config.json
    extra_p2p_ids: list[str] = sorted(list(set(raw_p2p_test_ids) - set(expected_p2p_list)))

    # E. Collision between P2P and F2P
    p2p_f2p_collisions: list[str] = sorted(list(set(raw_p2p_test_ids) & set(expected_f2p_list)))

    # F. Abnormal statuses: skipped, pending, todo, or assertion failures
    abnormal_status_ids: list[str] = []
    failed_assertion_ids: list[str] = []
    for tid, recs in raw_p2p_records_by_id.items():
        for r in recs:
            st = r.get("status")
            if st in ("skipped", "pending", "todo"):
                if tid not in abnormal_status_ids:
                    abnormal_status_ids.append(tid)
            elif st != "passed":
                if tid not in failed_assertion_ids:
                    failed_assertion_ids.append(tid)

    # Build canonical p2p_results list for all expected P2P nodes
    p2p_results_list: list[dict[str, Any]] = []
    failed_p2p_test_ids: list[str] = []

    for test_id in expected_p2p_list:
        if test_id in duplicate_p2p_ids:
            failed_p2p_test_ids.append(test_id)
            p2p_results_list.append({
                "testId": test_id,
                "name": test_id.split("::")[-1],
                "status": "failed",
                "duration": 0,
                "failureMessages": [f"Duplicate test ID execution detected ({raw_p2p_test_ids.count(test_id)} instances)"],
            })
        elif test_id in missing_p2p_ids:
            failed_p2p_test_ids.append(test_id)
            p2p_results_list.append({
                "testId": test_id,
                "name": test_id.split("::")[-1],
                "status": "failed",
                "duration": 0,
                "failureMessages": ["Required P2P test was missing or unexecuted"],
            })
        elif test_id in abnormal_status_ids:
            failed_p2p_test_ids.append(test_id)
            p2p_results_list.append({
                "testId": test_id,
                "name": test_id.split("::")[-1],
                "status": "failed",
                "duration": 0,
                "failureMessages": ["P2P test was marked as skipped/pending/todo"],
            })
        elif test_id in failed_assertion_ids:
            failed_p2p_test_ids.append(test_id)
            recs = raw_p2p_records_by_id.get(test_id, [])
            fail_msgs = recs[0].get("failureMessages", []) if recs else []
            p2p_results_list.append({
                "testId": test_id,
                "name": test_id.split("::")[-1],
                "status": "failed",
                "duration": recs[0].get("duration", 0) if recs else 0,
                "failureMessages": fail_msgs or ["P2P test assertion failed"],
            })
        else:
            recs = raw_p2p_records_by_id.get(test_id, [])
            p2p_results_list.append({
                "testId": test_id,
                "name": test_id.split("::")[-1],
                "status": "passed",
                "duration": recs[0].get("duration", 0) if recs else 0,
                "failureMessages": [],
            })

    # Include extra, leaked F2P, and collision IDs into failed_p2p_test_ids
    for eid in sorted(list(set(extra_p2p_ids) | set(leaked_f2p_ids) | set(p2p_f2p_collisions))):
        if eid not in failed_p2p_test_ids:
            failed_p2p_test_ids.append(eid)

    test_collection_ok = bool(index_exec_ok and picker_exec_ok and len(leaked_f2p_ids) == 0)
    if leaked_f2p_ids:
        test_collection_msg += f"; Violation: F2P tests were executed in Hard Gate ({leaked_f2p_ids})"

    # Validate test collection count & integrity
    has_collection_anomalies = bool(
        duplicate_p2p_ids
        or missing_p2p_ids
        or extra_p2p_ids
        or leaked_f2p_ids
        or p2p_f2p_collisions
        or len(raw_p2p_test_ids) != expected_total_p2p
    )

    if not has_collection_anomalies:
        test_count_ok = True
        test_count_msg = f"Exactly {expected_total_p2p} unique P2P tests collected matching configuration with zero F2P leakage"
    else:
        reasons = []
        if duplicate_p2p_ids:
            reasons.append(f"duplicates: {duplicate_p2p_ids}")
        if missing_p2p_ids:
            reasons.append(f"missing: {missing_p2p_ids[:3]}")
        if extra_p2p_ids:
            reasons.append(f"extra: {extra_p2p_ids[:3]}")
        if leaked_f2p_ids:
            reasons.append(f"leaked F2P: {leaked_f2p_ids[:3]}")
        if p2p_f2p_collisions:
            reasons.append(f"P2P/F2P collision: {p2p_f2p_collisions[:3]}")
        if len(raw_p2p_test_ids) != expected_total_p2p:
            reasons.append(f"count: {len(raw_p2p_test_ids)} != {expected_total_p2p}")
        test_count_msg = f"P2P collection integrity failure: {'; '.join(reasons)}"

    if test_count_ok and len(failed_p2p_test_ids) == 0:
        p2p_exec_ok = True
        p2p_exec_msg = f"All {expected_total_p2p} P2P regression tests passed successfully"
    else:
        p2p_exec_msg = f"{len(failed_p2p_test_ids)} of {expected_total_p2p} P2P tests failed/invalid: {failed_p2p_test_ids[:5]}"

    nodes.append(
        NodeResult(
            node_id="test_collection_integrity",
            passed=test_collection_ok,
            description="Vitest test discovery and execution integrity check",
            message=test_collection_msg,
        )
    )

    nodes.append(
        NodeResult(
            node_id="test_collection_count",
            passed=test_count_ok,
            description=f"Validate that exactly {expected_total_p2p} P2P tests are collected matching configuration",
            message=test_count_msg,
        )
    )

    nodes.append(
        NodeResult(
            node_id="p2p_execution_integrity",
            passed=p2p_exec_ok,
            description=f"All {expected_total_p2p} P2P regression tests pass cleanly",
            message=p2p_exec_msg,
            details={"failed_tests": failed_p2p_test_ids},
        )
    )

    # 21. Node result uniqueness check
    all_node_ids = [n.node_id for n in nodes]
    nodes_unique = len(all_node_ids) == len(set(all_node_ids))
    unique_msg = "All verification check node IDs are unique"
    if not nodes_unique:
        unique_msg = "Duplicate node IDs detected in verification pipeline"

    nodes.append(
        NodeResult(
            node_id="node_result_uniqueness",
            passed=nodes_unique,
            description="Verify that every verification node ID is unique",
            message=unique_msg,
        )
    )

    # 22. Report Schema Integrity Node & Report Aggregation
    # Create schema node (tentatively passed to validate provisional structure)
    schema_node = NodeResult(
        node_id="report_schema_integrity",
        passed=True,
        description="Verify structured report schemas conform to DeepSWE requirements",
        message="Hard Gate report schema, data types, and cross-field consistencies verified",
    )
    nodes.append(schema_node)

    # Pre-schema failure calculation
    p2p_failed_ids = [p["testId"] for p in p2p_results_list if p.get("status") != "passed"]
    check_failed_ids = [n.node_id for n in nodes if not n.passed]
    provisional_failed_nodes = sorted(list(set(check_failed_ids) | set(p2p_failed_ids)))

    provisional_overall_passed = bool(
        patch_applied and len(provisional_failed_nodes) == 0 and len(infra_errors) == 0
    )

    report_data: dict[str, Any] = {
        "passed": provisional_overall_passed,
        "apply_failed": bool(apply_failed),
        "failed_nodes": provisional_failed_nodes,
        "nodes": [n.to_dict() for n in nodes],
        "architecture_result": architecture_result,
        "p2p_summary": {
            "total": len(p2p_config_nodes),
            "passed": sum(1 for p in p2p_results_list if p.get("status") == "passed"),
            "failed": sum(1 for p in p2p_results_list if p.get("status") != "passed"),
        },
        "p2p_results": p2p_results_list,
        "compile_paths": config.get("hard_gate", {}).get("compile_paths", ["src/"]),
        "candidate_changed_paths": candidate_changed_paths,
        "protected_changes": protected_changes,
        "test_bypass": {
            "detected": test_bypass_detected,
            "findings": test_bypass_findings,
        },
        "cheat_reasons": cheat_reasons,
        "cheat_penalty": config.get("hard_gate", {}).get("cheat_penalty", -1.0) if not provisional_overall_passed else 0.0,
        "compile_errors": compile_errors,
        "infra_errors": infra_errors,
    }

    # Execute True Schema and Cross-Field Consistency Validation
    schema_valid, schema_errors = validate_hard_gate_schema(
        report_data,
        expected_p2p_list=p2p_config_nodes,
        expected_cheat_nodes=expected_cheat_nodes,
    )

    if not schema_valid:
        schema_node.passed = False
        schema_node.message = f"Hard Gate report schema validation failed: {'; '.join(schema_errors)}"
        schema_node.details = {"schema_errors": schema_errors}

    # Re-synchronize final nodes and failed_nodes after schema determination
    final_check_failed = [n.node_id for n in nodes if not n.passed]
    final_p2p_failed = [p["testId"] for p in p2p_results_list if p.get("status") != "passed"]
    final_failed_nodes = sorted(list(set(final_check_failed) | set(final_p2p_failed)))
    final_overall_passed = bool(
        patch_applied and len(final_failed_nodes) == 0 and schema_valid and len(infra_errors) == 0
    )

    report_data["nodes"] = [n.to_dict() for n in nodes]
    report_data["failed_nodes"] = final_failed_nodes
    report_data["passed"] = final_overall_passed
    report_data["cheat_penalty"] = config.get("hard_gate", {}).get("cheat_penalty", -1.0) if not final_overall_passed else 0.0

    # Write serialized report to disk
    output_path.parent.mkdir(parents=True, exist_ok=True)
    serialized_json = json.dumps(report_data, ensure_ascii=False, indent=2) + "\n"
    output_path.write_text(serialized_json, encoding="utf-8")

    # Re-read and re-validate serialization from disk
    try:
        disk_text = output_path.read_text(encoding="utf-8")
        disk_data = json.loads(disk_text)
        reval_ok, reval_errs = validate_hard_gate_schema(
            disk_data,
            expected_p2p_list=p2p_config_nodes,
            expected_cheat_nodes=expected_cheat_nodes,
        )
        if not reval_ok:
            raise ValueError(f"Re-validation from disk failed: {'; '.join(reval_errs)}")
    except Exception as e:
        schema_node.passed = False
        schema_node.message = f"Disk report re-validation failed: {e}"
        schema_node.details = {"disk_error": str(e)}

        recomputed_check_failed = [n.node_id for n in nodes if not n.passed]
        recomputed_failed = sorted(list(set(recomputed_check_failed) | set(final_p2p_failed)))

        report_data["nodes"] = [n.to_dict() for n in nodes]
        report_data["failed_nodes"] = recomputed_failed
        report_data["passed"] = False
        report_data["infra_errors"]["disk_revalidation"] = str(e)
        report_data["cheat_penalty"] = config.get("hard_gate", {}).get("cheat_penalty", -1.0)

        output_path.write_text(json.dumps(report_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return report_data


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic Hard Gate runner")
    parser.add_argument("--config", type=Path, required=True, help="Path to config.json")
    parser.add_argument("--repo", type=Path, required=True, help="Path to repository")
    parser.add_argument("--output", type=Path, required=True, help="Output path for hard-gate.json")
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0, help="Whether candidate patch apply failed")
    args = parser.parse_args()

    report_data = run_hard_gate(
        config_path=args.config,
        repo_dir=args.repo,
        output_path=args.output,
        apply_failed=args.apply_failed,
    )
    if report_data.get("infra_errors"):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
