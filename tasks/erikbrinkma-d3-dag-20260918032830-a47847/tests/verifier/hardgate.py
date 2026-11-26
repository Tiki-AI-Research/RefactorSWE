#!/usr/bin/env python3
"""Compile, integrity, anti-cheat, and atomic P2P hard gates."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

EXPECTED_EVAL_TESTS_SHA256 = "3a0accb08ce7a53f421c4d7bc09b4d5f41f735036e3c8f186330af541d1847d3"

ALLOWED_PROD_FILES = {
    "src/layout.ts",
    "src/sugiyama/index.ts",
    "src/zherebko/index.ts",
    "src/grid/index.ts",
    "src/tweaks.ts",
}

BASELINE_TEST_FILES = {
    "src/collections.test.ts",
    "src/dagre.test.ts",
    "src/graph/connect.test.ts",
    "src/graph/hierarchy.test.ts",
    "src/graph/index.test.ts",
    "src/graph/json.test.ts",
    "src/graph/stratify.test.ts",
    "src/graph/utils.test.ts",
    "src/grid/index.test.ts",
    "src/grid/lane/greedy.test.ts",
    "src/grid/lane/index.test.ts",
    "src/grid/lane/opt.test.ts",
    "src/index.test.ts",
    "src/iters.test.ts",
    "src/layout.test.ts",
    "src/sugiyama/coord/center.test.ts",
    "src/sugiyama/coord/greedy.test.ts",
    "src/sugiyama/coord/index.test.ts",
    "src/sugiyama/coord/quad.test.ts",
    "src/sugiyama/coord/simplex.test.ts",
    "src/sugiyama/coord/topological.test.ts",
    "src/sugiyama/decross/dfs.test.ts",
    "src/sugiyama/decross/index.test.ts",
    "src/sugiyama/decross/opt.test.ts",
    "src/sugiyama/decross/two-layer.test.ts",
    "src/sugiyama/index.test.ts",
    "src/sugiyama/layering/index.test.ts",
    "src/sugiyama/layering/longest-path.test.ts",
    "src/sugiyama/layering/simplex.test.ts",
    "src/sugiyama/layering/topological.test.ts",
    "src/sugiyama/sugify.test.ts",
    "src/sugiyama/twolayer/agg.test.ts",
    "src/sugiyama/twolayer/greedy.test.ts",
    "src/sugiyama/twolayer/index.test.ts",
    "src/sugiyama/twolayer/opt.test.ts",
    "src/sugiyama/utils.test.ts",
    "src/tweaks.test.ts",
    "src/utils.test.ts",
    "src/zherebko/index.test.ts",
}

BASELINE_SRC_FILES = {
    "src/collections.test.ts", "src/collections.ts", "src/dagre.bench.ts", "src/dagre.test.ts", "src/dagre.ts",
    "src/graph/connect.test.ts", "src/graph/connect.ts", "src/graph/hierarchy.test.ts", "src/graph/hierarchy.ts",
    "src/graph/index.test.ts", "src/graph/index.ts", "src/graph/json.test.ts", "src/graph/json.ts",
    "src/graph/stratify.test.ts", "src/graph/stratify.ts", "src/graph/utils.test.ts", "src/graph/utils.ts",
    "src/grid/index.test.ts", "src/grid/index.ts", "src/grid/lane/greedy.test.ts", "src/grid/lane/greedy.ts",
    "src/grid/lane/index.test.ts", "src/grid/lane/index.ts", "src/grid/lane/opt.test.ts", "src/grid/lane/opt.ts",
    "src/grid/lane/test-utils.ts", "src/grid/lane/utils.ts", "src/index.test.ts", "src/index.ts",
    "src/iters.test.ts", "src/iters.ts", "src/layout.test.ts", "src/layout.ts",
    "src/sugiyama/coord/center.test.ts", "src/sugiyama/coord/center.ts", "src/sugiyama/coord/greedy.test.ts",
    "src/sugiyama/coord/greedy.ts", "src/sugiyama/coord/index.test.ts", "src/sugiyama/coord/index.ts",
    "src/sugiyama/coord/quad.test.ts", "src/sugiyama/coord/quad.ts", "src/sugiyama/coord/simplex.test.ts",
    "src/sugiyama/coord/simplex.ts", "src/sugiyama/coord/topological.test.ts", "src/sugiyama/coord/topological.ts",
    "src/sugiyama/coord/utils.ts", "src/sugiyama/decross/dfs.test.ts", "src/sugiyama/decross/dfs.ts",
    "src/sugiyama/decross/index.test.ts", "src/sugiyama/decross/index.ts", "src/sugiyama/decross/opt.test.ts",
    "src/sugiyama/decross/opt.ts", "src/sugiyama/decross/two-layer.test.ts", "src/sugiyama/decross/two-layer.ts",
    "src/sugiyama/index.test.ts", "src/sugiyama/index.ts", "src/sugiyama/layering/index.test.ts",
    "src/sugiyama/layering/index.ts", "src/sugiyama/layering/longest-path.test.ts", "src/sugiyama/layering/longest-path.ts",
    "src/sugiyama/layering/simplex.test.ts", "src/sugiyama/layering/simplex.ts", "src/sugiyama/layering/test-utils.ts",
    "src/sugiyama/layering/topological.test.ts", "src/sugiyama/layering/topological.ts", "src/sugiyama/sugify.test.ts",
    "src/sugiyama/sugify.ts", "src/sugiyama/test-utils.ts", "src/sugiyama/twolayer/agg.test.ts",
    "src/sugiyama/twolayer/agg.ts", "src/sugiyama/twolayer/greedy.test.ts", "src/sugiyama/twolayer/greedy.ts",
    "src/sugiyama/twolayer/index.test.ts", "src/sugiyama/twolayer/index.ts", "src/sugiyama/twolayer/opt.test.ts",
    "src/sugiyama/twolayer/opt.ts", "src/sugiyama/utils.test.ts", "src/sugiyama/utils.ts", "src/test-graphs.ts",
    "src/test-utils.ts", "src/tweaks.test.ts", "src/tweaks.ts", "src/types.d.ts", "src/utils.test.ts", "src/utils.ts",
    "src/zherebko/greedy.ts", "src/zherebko/index.test.ts", "src/zherebko/index.ts",
}

PROHIBITED_CONFIGS = {
    "package.json",
    "tsconfig.json",
    "tsconfig.build.json",
    "biome.json",
    "bun.lock",
    "bun.lockb",
    "bunfig.toml",
    ".bunfig.toml",
    "p2p_select.txt",
    "p2p_added.txt",
}

PROHIBITED_HELPERS = {
    "src/test-graphs.ts",
    "src/test-utils.ts",
    "src/sugiyama/test-utils.ts",
    "src/sugiyama/layering/test-utils.ts",
    "src/grid/lane/test-utils.ts",
}

CONFIRMED_INTEGRATION_NODES = [
    "src/index.test.ts::sugiyama()",
    "src/index.test.ts::grid()",
    "src/index.test.ts::zherebko()",
    "src/index.test.ts::sugiyama.tweak()",
    "src/index.test.ts::manual sugiyama() layered",
    "src/index.test.ts::manual sugiyama() compact",
]

def strip_comments(code: str) -> str:
    """Strip single-line and multi-line comments from JS/TS code while preserving string literals."""
    def replacer(match: re.Match[str]) -> str:
        s = match.group(0)
        return ("\n" * s.count("\n")) if s.startswith("/") else s

    pattern = re.compile(
        r'//.*?$|/\*[\s\S]*?\*/|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|`(?:\\.|[^`\\])*`',
        re.DOTALL | re.MULTILINE,
    )
    return pattern.sub(replacer, code)


@dataclass
class Token:
    type: str  # "ID", "STR", "NUM", "PUNCT", "RAW", "REGEX"
    value: str
    is_control: bool = False


MULTI_CHAR_OPS = (
    ">>>=", "===", "!==", ">>>", "<<=", ">>=", "**=", "&&=", "||=", "??=",
    "...", "==", "!=", "<=", ">=", "&&", "||", "??", "=>", "++", "--",
    "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<", ">>", "**", "?."
)

REGEX_EXPR_KEYWORDS = {
    "return", "throw", "case", "delete", "void", "typeof",
    "instanceof", "in", "yield", "await", "default", "do"
}

CONTROL_KEYWORDS = {"if", "for", "while", "with", "switch", "catch"}

REGEX_START_PUNCT = {
    "=", "(", "[", "{", ",", ":", ";",
    "!", "?", "&&", "||", "=>", "${",
    "+", "-", "*", "/", "%", "&", "|", "^", "~",
    "<", ">", "<=", ">=", "==", "!=", "===", "!==",
    "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=",
    "**", "<<", ">>", ">>>", "...", "??"
}


def try_read_unicode_escape(source: str, pos: int) -> tuple[str, int] | None:
    n = len(source)
    if pos + 1 >= n or source[pos] != "\\" or source[pos+1] != "u":
        return None
    if pos + 2 < n and source[pos+2] == "{":
        close_idx = source.find("}", pos + 3)
        if close_idx != -1 and pos + 3 < close_idx:
            hex_str = source[pos+3:close_idx]
            if len(hex_str) <= 6 and all(c in "0123456789abcdefABCDEF" for c in hex_str):
                try:
                    cp = int(hex_str, 16)
                    if cp <= 0x10FFFF:
                        return (chr(cp), close_idx + 1)
                except ValueError:
                    pass
    elif pos + 5 < n:
        hex_str = source[pos+2:pos+6]
        if all(c in "0123456789abcdefABCDEF" for c in hex_str):
            try:
                cp = int(hex_str, 16)
                return (chr(cp), pos + 6)
            except ValueError:
                pass
    return None


def unescape_js_string(s: str) -> str:
    res = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == "\\" and i + 1 < n:
            i += 1
            c = s[i]
            if c == "u":
                if i + 1 < n and s[i+1] == "{":
                    close_idx = s.find("}", i + 2)
                    if close_idx != -1:
                        hex_str = s[i+2:close_idx]
                        if hex_str and len(hex_str) <= 6 and all(ch in "0123456789abcdefABCDEF" for ch in hex_str):
                            try:
                                code_pt = int(hex_str, 16)
                                if code_pt <= 0x10FFFF:
                                    res.append(chr(code_pt))
                                    i = close_idx + 1
                                    continue
                            except ValueError:
                                pass
                elif i + 4 < n:
                    hex_str = s[i+1:i+5]
                    if all(ch in "0123456789abcdefABCDEF" for ch in hex_str):
                        try:
                            code_pt = int(hex_str, 16)
                            res.append(chr(code_pt))
                            i += 5
                            continue
                        except ValueError:
                            pass
                res.append("u")
                i += 1
            elif c == "x" and i + 2 < n:
                hex_str = s[i+1:i+3]
                if all(ch in "0123456789abcdefABCDEF" for ch in hex_str):
                    try:
                        code_pt = int(hex_str, 16)
                        res.append(chr(code_pt))
                        i += 3
                        continue
                    except ValueError:
                        pass
                res.append("x")
                i += 1
            elif c == "n":
                res.append("\n")
                i += 1
            elif c == "r":
                res.append("\r")
                i += 1
            elif c == "t":
                res.append("\t")
                i += 1
            elif c == "b":
                res.append("\b")
                i += 1
            elif c == "f":
                res.append("\f")
                i += 1
            elif c == "v":
                res.append("\v")
                i += 1
            elif c == "0":
                res.append("\0")
                i += 1
            elif c in ("\r", "\n"):
                if c == "\r" and i + 1 < n and s[i+1] == "\n":
                    i += 2
                else:
                    i += 1
            else:
                res.append(c)
                i += 1
        else:
            res.append(s[i])
            i += 1
    return "".join(res)


def tokenize_js(source: str) -> list[Token]:
    """Tokenize JS/TS code into identifiers, strings, template text, regexes, and operators."""
    tokens: list[Token] = []
    i = 0
    n = len(source)
    state_stack: list[Any] = ["CODE"]
    paren_stack: list[bool] = []

    while i < n:
        state = state_stack[-1]

        if state == "TEMPLATE":
            raw_chars = []
            while i < n:
                ch = source[i]
                if ch == "\\" and i + 1 < n:
                    raw_chars.append(source[i:i+2])
                    i += 2
                elif ch == "`":
                    if raw_chars:
                        tokens.append(Token("RAW", unescape_js_string("".join(raw_chars))))
                    tokens.append(Token("PUNCT", "`"))
                    i += 1
                    state_stack.pop()
                    break
                elif ch == "$" and i + 1 < n and source[i+1] == "{":
                    if raw_chars:
                        tokens.append(Token("RAW", unescape_js_string("".join(raw_chars))))
                    tokens.append(Token("PUNCT", "${"))
                    i += 2
                    state_stack.append(["INTERP", 0])
                    break
                else:
                    raw_chars.append(ch)
                    i += 1
            continue

        ch = source[i]

        if ch.isspace():
            i += 1
            continue

        # Comments
        if ch == "/" and i + 1 < n:
            if source[i+1] == "/":
                i += 2
                while i < n and source[i] != "\n":
                    i += 1
                continue
            elif source[i+1] == "*":
                i += 2
                while i + 1 < n and not (source[i] == "*" and source[i+1] == "/"):
                    i += 1
                i += 2 if i + 1 < n else (n - i)
                continue

        # Check regex literal vs division/punctuation
        if ch == "/":
            can_be_regex = False
            if not tokens:
                can_be_regex = True
            else:
                last = tokens[-1]
                if last.type == "ID":
                    if last.value in REGEX_EXPR_KEYWORDS:
                        can_be_regex = True
                elif last.type == "PUNCT":
                    if last.value == ")" and last.is_control:
                        can_be_regex = True
                    elif last.value in (")", "]", "}", "++", "--"):
                        can_be_regex = False
                    elif last.value in REGEX_START_PUNCT:
                        can_be_regex = True

            if can_be_regex:
                j = i + 1
                in_class = False
                matched_regex = False
                while j < n:
                    c = source[j]
                    if c in ("\r", "\n"):
                        break
                    if c == "\\":
                        j += 2 if j + 1 < n else 1
                        continue
                    if c == "[" and not in_class:
                        in_class = True
                        j += 1
                        continue
                    if c == "]" and in_class:
                        in_class = False
                        j += 1
                        continue
                    if c == "/" and not in_class:
                        j += 1
                        while j < n and (source[j].isalpha() or source[j] == "$"):
                            j += 1
                        matched_regex = True
                        break
                    j += 1

                if matched_regex:
                    tokens.append(Token("REGEX", source[i:j]))
                    i = j
                    continue

        # Template literal start
        if ch == "`":
            tokens.append(Token("PUNCT", "`"))
            i += 1
            state_stack.append("TEMPLATE")
            continue

        # String literal
        if ch in ("\"", "'"):
            quote = ch
            i += 1
            raw_chars = []
            while i < n:
                c = source[i]
                if c == "\\" and i + 1 < n:
                    raw_chars.append(source[i:i+2])
                    i += 2
                elif c == quote:
                    i += 1
                    break
                else:
                    raw_chars.append(c)
                    i += 1
            tokens.append(Token("STR", unescape_js_string("".join(raw_chars))))
            continue

        # Identifiers (including Unicode escape prefix or body)
        is_ident = False
        if ch.isalpha() or ch in ("_", "$"):
            is_ident = True
        elif ch == "\\" and i + 1 < n and source[i+1] == "u":
            u_res = try_read_unicode_escape(source, i)
            if u_res and (u_res[0].isalpha() or u_res[0] in ("_", "$")):
                is_ident = True

        if is_ident:
            ident_chars = []
            while i < n:
                c = source[i]
                if c.isalnum() or c in ("_", "$"):
                    ident_chars.append(c)
                    i += 1
                elif c == "\\" and i + 1 < n and source[i+1] == "u":
                    u_res = try_read_unicode_escape(source, i)
                    if u_res and (u_res[0].isalnum() or u_res[0] in ("_", "$")):
                        ident_chars.append(u_res[0])
                        i = u_res[1]
                    else:
                        break
                else:
                    break
            tokens.append(Token("ID", "".join(ident_chars)))
            continue

        # Number literal
        if ch.isdigit():
            start = i
            while i < n and (source[i].isalnum() or source[i] in (".", "_")):
                i += 1
            tokens.append(Token("NUM", source[start:i]))
            continue

        # Paren tracking
        if ch == "(":
            is_control_paren = False
            if tokens and tokens[-1].type == "ID" and tokens[-1].value in CONTROL_KEYWORDS:
                is_control_paren = True
            paren_stack.append(is_control_paren)
            tokens.append(Token("PUNCT", "("))
            i += 1
            continue

        if ch == ")":
            was_control = paren_stack.pop() if paren_stack else False
            tokens.append(Token("PUNCT", ")", is_control=was_control))
            i += 1
            continue

        # Braces tracking in interpolation
        if ch == "{" and isinstance(state, list) and state[0] == "INTERP":
            state[1] += 1
            tokens.append(Token("PUNCT", "{"))
            i += 1
            continue

        if ch == "}" and isinstance(state, list) and state[0] == "INTERP":
            if state[1] > 0:
                state[1] -= 1
                tokens.append(Token("PUNCT", "}"))
            else:
                tokens.append(Token("PUNCT", "}"))
                state_stack.pop()
            i += 1
            continue

        # Multi-char operators
        matched_op = False
        for op in MULTI_CHAR_OPS:
            if source.startswith(op, i):
                tokens.append(Token("PUNCT", op))
                i += len(op)
                matched_op = True
                break
        if matched_op:
            continue

        # Single char punctuation/operator
        tokens.append(Token("PUNCT", ch))
        i += 1

    return tokens


FS_SENSITIVE_APIS = {
    "readFile", "readFileSync", "open", "openSync", "createReadStream", "file"
}
PROCESS_SENSITIVE_APIS = {
    "spawn", "spawnSync", "exec", "execSync", "execFile", "fork", "$"
}


def check_module_name(name: str) -> str | None:
    n = name.strip()
    if n in ("fs", "node:fs") or n.startswith("fs/") or n.startswith("node:fs/"):
        return "node:fs"
    if n in ("child_process", "node:child_process") or n.startswith("child_process/") or n.startswith("node:child_process/"):
        return "child_process"
    return None


def scan_for_forbidden_code(code: str) -> list[str]:
    """Scan JS/TS code for malicious calls, imports, or tokens with semantic awareness."""
    tokens = tokenize_js(code)
    detected: list[str] = []
    num_tokens = len(tokens)

    def add_rule(r: str):
        if r not in detected:
            detected.append(r)

    for i in range(num_tokens):
        tok = tokens[i]

        # 1. auditRead() and auditWrite()
        # Only direct calls without receiver
        if tok.type == "ID" and tok.value in ("auditRead", "auditWrite"):
            prev_tok = tokens[i-1] if i > 0 else None
            if not prev_tok or prev_tok.value not in (".", "?."):
                if i + 1 < num_tokens and tokens[i+1].type == "PUNCT" and tokens[i+1].value == "(":
                    add_rule(tok.value)

        # 2. process.exit in direct, optional-chain, or computed property forms
        if tok.type == "ID" and tok.value == "process":
            # Option A: process.exit or process?.exit
            j = i + 1
            if j < num_tokens and tokens[j].type == "PUNCT" and tokens[j].value in (".", "?."):
                j += 1
                if j < num_tokens and tokens[j].type == "ID" and tokens[j].value == "exit":
                    j += 1
                    if j < num_tokens and tokens[j].type == "PUNCT" and tokens[j].value == "?.":
                        j += 1
                    if j < num_tokens and tokens[j].type == "PUNCT" and tokens[j].value == "(":
                        add_rule("process.exit")
            # Option B: process["exit"]() or process?.["exit"]?.()
            j = i + 1
            if j < num_tokens and tokens[j].type == "PUNCT" and tokens[j].value == "?.":
                j += 1
            if j < num_tokens and tokens[j].type == "PUNCT" and tokens[j].value == "[":
                j += 1
                if j < num_tokens and tokens[j].type == "STR" and tokens[j].value == "exit":
                    j += 1
                    if j < num_tokens and tokens[j].type == "PUNCT" and tokens[j].value == "]":
                        j += 1
                        if j < num_tokens and tokens[j].type == "PUNCT" and tokens[j].value == "?.":
                            j += 1
                        if j < num_tokens and tokens[j].type == "PUNCT" and tokens[j].value == "(":
                            add_rule("process.exit")

        # 3. Static import / export with from
        if tok.type == "ID" and tok.value == "from":
            if i + 1 < num_tokens and tokens[i+1].type == "STR":
                mod_rule = check_module_name(tokens[i+1].value)
                if mod_rule:
                    add_rule(mod_rule)

        # 4. Bare import "fs"
        if tok.type == "ID" and tok.value == "import":
            prev_tok = tokens[i-1] if i > 0 else None
            if not prev_tok or prev_tok.value not in (".", "?."):
                if i + 1 < num_tokens and tokens[i+1].type == "STR":
                    mod_rule = check_module_name(tokens[i+1].value)
                    if mod_rule:
                        add_rule(mod_rule)

        # 5. Dynamic import("fs")
        if tok.type == "ID" and tok.value == "import":
            prev_tok = tokens[i-1] if i > 0 else None
            if not prev_tok or prev_tok.value not in (".", "?."):
                if i + 2 < num_tokens and tokens[i+1].type == "PUNCT" and tokens[i+1].value == "(" and tokens[i+2].type == "STR":
                    mod_rule = check_module_name(tokens[i+2].value)
                    if mod_rule:
                        add_rule(mod_rule)

        # 6. require("fs")
        if tok.type == "ID" and tok.value == "require":
            prev_tok = tokens[i-1] if i > 0 else None
            if not prev_tok or prev_tok.value not in (".", "?."):
                if i + 2 < num_tokens and tokens[i+1].type == "PUNCT" and tokens[i+1].value == "(" and tokens[i+2].type == "STR":
                    mod_rule = check_module_name(tokens[i+2].value)
                    if mod_rule:
                        add_rule(mod_rule)

        # 7. Sensitive function calls with /proc/ or --reporter-outfile
        if tok.type == "PUNCT" and tok.value == "(":
            callee_id = None
            callee_idx = -1
            if i > 0 and tokens[i-1].type == "ID":
                callee_id = tokens[i-1].value
                callee_idx = i - 1
            elif i > 1 and tokens[i-1].type == "PUNCT" and tokens[i-1].value == "?." and tokens[i-2].type == "ID":
                callee_id = tokens[i-2].value
                callee_idx = i - 2

            if callee_id:
                receiver = None
                if callee_idx > 0 and tokens[callee_idx - 1].type == "PUNCT" and tokens[callee_idx - 1].value in (".", "?."):
                    if callee_idx > 1 and tokens[callee_idx - 2].type == "ID":
                        receiver = tokens[callee_idx - 2].value
                        if callee_idx > 2 and tokens[callee_idx - 3].type == "PUNCT" and tokens[callee_idx - 3].value in (".", "?."):
                            receiver = "other"
                    else:
                        receiver = "other"

                depth = 1
                k = i + 1
                arg_strings = []
                while k < num_tokens and depth > 0:
                    if tokens[k].type == "PUNCT" and tokens[k].value == "(":
                        depth += 1
                    elif tokens[k].type == "PUNCT" and tokens[k].value == ")":
                        depth -= 1
                    elif tokens[k].type in ("STR", "RAW"):
                        arg_strings.append(tokens[k].value)
                    k += 1

                # /proc/ only on no receiver or Bun receiver
                if (receiver is None or receiver == "Bun") and callee_id in FS_SENSITIVE_APIS:
                    for s in arg_strings:
                        if "/proc/" in s:
                            add_rule("/proc/")

                # --reporter-outfile only on no receiver or Bun receiver
                if (receiver is None or receiver == "Bun") and callee_id in PROCESS_SENSITIVE_APIS:
                    for s in arg_strings:
                        if "--reporter-outfile" in s:
                            add_rule("--reporter-outfile")

        # 8. Tagged template calls: Bun.$`...`, $`...`, etc.
        if tok.type == "ID" and tok.value in PROCESS_SENSITIVE_APIS:
            prev_tok = tokens[i-1] if i > 0 else None
            receiver = None
            if prev_tok and prev_tok.value in (".", "?."):
                if i > 1 and tokens[i-2].type == "ID":
                    receiver = tokens[i-2].value
                else:
                    receiver = "other"

            if receiver is None or receiver == "Bun":
                if i + 1 < num_tokens and tokens[i+1].type == "PUNCT" and tokens[i+1].value == "`":
                    k = i + 2
                    while k < num_tokens and not (tokens[k].type == "PUNCT" and tokens[k].value == "`"):
                        if tokens[k].type in ("STR", "RAW") and "--reporter-outfile" in tokens[k].value:
                            add_rule("--reporter-outfile")
                        k += 1

        if tok.type == "ID" and tok.value in FS_SENSITIVE_APIS:
            prev_tok = tokens[i-1] if i > 0 else None
            receiver = None
            if prev_tok and prev_tok.value in (".", "?."):
                if i > 1 and tokens[i-2].type == "ID":
                    receiver = tokens[i-2].value
                else:
                    receiver = "other"

            if receiver is None or receiver == "Bun":
                if i + 1 < num_tokens and tokens[i+1].type == "PUNCT" and tokens[i+1].value == "`":
                    k = i + 2
                    while k < num_tokens and not (tokens[k].type == "PUNCT" and tokens[k].value == "`"):
                        if tokens[k].type in ("STR", "RAW") and "/proc/" in tokens[k].value:
                            add_rule("/proc/")
                        k += 1

    return detected


def validate_p2p_selection(config: dict[str, Any], verifier_dir: Path) -> tuple[bool, list[str]]:
    """Validate P2P/F2P test lists consistency, order, duplicates, and non-overlap."""
    failed_nodes: list[str] = []

    p2p_select_path = verifier_dir / "p2p_select.txt"
    p2p_select_nodes: list[str] = []
    seen_select: set[str] = set()

    if not p2p_select_path.exists():
        failed_nodes.append("p2p_select_file_missing")
    else:
        for line in p2p_select_path.read_text(encoding="utf-8").splitlines():
            node = line.strip()
            if not node:
                failed_nodes.append("p2p_select_empty_node")
                continue
            if node in seen_select:
                failed_nodes.append(f"p2p_select_duplicate:{node}")
            seen_select.add(node)
            p2p_select_nodes.append(node)

    p2p_added_path = verifier_dir / "p2p_added.txt"
    p2p_added_nodes: list[str] = []
    seen_added: set[str] = set()

    if not p2p_added_path.exists():
        failed_nodes.append("p2p_added_file_missing")
    else:
        for line in p2p_added_path.read_text(encoding="utf-8").splitlines():
            node = line.strip()
            if not node:
                failed_nodes.append("p2p_added_empty_node")
                continue
            if node in seen_added:
                failed_nodes.append(f"p2p_added_duplicate:{node}")
            seen_added.add(node)
            p2p_added_nodes.append(node)

    config_p2p_raw = config.get("p2p", [])
    config_p2p_nodes: list[str] = []
    seen_cfg_p2p: set[str] = set()
    for node in config_p2p_raw:
        node_str = str(node).strip()
        if not node_str:
            failed_nodes.append("config_empty_node")
            continue
        if node_str in seen_cfg_p2p:
            failed_nodes.append(f"config_duplicate_node:{node_str}")
        seen_cfg_p2p.add(node_str)
        config_p2p_nodes.append(node_str)

    config_f2p_raw = config.get("f2p", [])
    config_f2p_nodes: list[str] = []
    seen_cfg_f2p: set[str] = set()
    for node in config_f2p_raw:
        node_str = str(node).strip()
        if not node_str:
            failed_nodes.append("config_empty_node")
            continue
        if node_str in seen_cfg_f2p:
            failed_nodes.append(f"config_duplicate_node:{node_str}")
        seen_cfg_f2p.add(node_str)
        config_f2p_nodes.append(node_str)

    config_advisory_raw = config.get("advisory_ids", [])
    config_advisory_nodes: list[str] = []
    seen_cfg_adv: set[str] = set()
    for node in config_advisory_raw:
        node_str = str(node).strip()
        if not node_str:
            failed_nodes.append("config_empty_node")
            continue
        if node_str in seen_cfg_adv:
            failed_nodes.append(f"config_duplicate_node:{node_str}")
        seen_cfg_adv.add(node_str)
        config_advisory_nodes.append(node_str)

    # Check order and set equality: config.p2p == p2p_select_nodes + p2p_added_nodes
    expected_p2p = p2p_select_nodes + p2p_added_nodes
    if config_p2p_raw != expected_p2p:
        failed_nodes.append("p2p_select_config_mismatch")

    # Check overlap between original P2P and added P2P
    overlap_select_added = set(p2p_select_nodes) & set(p2p_added_nodes)
    for node in sorted(overlap_select_added):
        failed_nodes.append(f"p2p_select_added_overlap:{node}")

    # Check P2P / F2P overlap
    all_p2p_set = set(p2p_select_nodes) | set(p2p_added_nodes) | set(config_p2p_nodes)
    overlap_p2p_f2p = all_p2p_set & set(config_f2p_nodes)
    for node in sorted(overlap_p2p_f2p):
        failed_nodes.append(f"p2p_f2p_overlap:{node}")

    # Check P2P / advisory overlap
    overlap_p2p_adv = all_p2p_set & set(config_advisory_nodes)
    for node in sorted(overlap_p2p_adv):
        failed_nodes.append(f"p2p_advisory_overlap:{node}")

    # Check F2P / advisory overlap
    overlap_f2p_adv = set(config_f2p_nodes) & set(config_advisory_nodes)
    for node in sorted(overlap_f2p_adv):
        failed_nodes.append(f"f2p_advisory_overlap:{node}")

    return (len(failed_nodes) == 0, failed_nodes)


def resolve_source_manifest_path(repo: Path) -> Path | None:
    """Resolve source-manifest.json path via env vars and repository context."""
    candidates: list[Path] = []
    env_manifest = os.environ.get("SOURCE_MANIFEST_PATH")
    if env_manifest:
        candidates.append(Path(env_manifest))
    verifier_dir = Path(__file__).resolve().parent
    candidates.extend([
        repo / "source-manifest.json",
        repo.parent / "source-manifest.json",
        verifier_dir.parent / "source-manifest.json",
        verifier_dir / "source-manifest.json",
    ])
    for p in candidates:
        if p.exists():
            return p
    return None


def resolve_model_patch_path(repo: Path) -> Path | None:
    """Resolve candidate model.patch path via env vars and repository context."""
    candidates: list[Path] = []
    env_patch = os.environ.get("MODEL_PATCH_PATH")
    if env_patch:
        candidates.append(Path(env_patch))
    env_artifacts = os.environ.get("ARTIFACTS_DIR")
    if env_artifacts:
        candidates.append(Path(env_artifacts) / "model.patch")
    candidates.extend([
        repo.parent / "artifacts" / "model.patch",
        repo.parent / "logs" / "artifacts" / "model.patch",
        repo.parent.parent / "logs" / "artifacts" / "model.patch",
        repo / "artifacts" / "model.patch",
        repo / "logs" / "artifacts" / "model.patch",
    ])
    for p in candidates:
        if p.exists():
            return p
    return None


def resolve_verifier_log_file(repo: Path, filename: str = "bun-test.log") -> Path:
    """Resolve verifier log file path via env vars, repository context, or temp directory."""
    env_dir = os.environ.get("VERIFIER_LOG_DIR") or os.environ.get("LOG_DIR")
    if env_dir:
        target_dir = Path(env_dir)
        try:
            target_dir.mkdir(parents=True, exist_ok=True)
            return target_dir / filename
        except Exception:
            pass

    candidates = [
        repo.parent.parent / "logs" / "verifier",
        repo.parent / "logs" / "verifier",
        repo.parent / "verifier",
    ]
    for d in candidates:
        if d.exists():
            return d / filename

    fallback_dir = Path(tempfile.gettempdir()) / "verifier"
    try:
        fallback_dir.mkdir(parents=True, exist_ok=True)
        return fallback_dir / filename
    except Exception:
        return Path(tempfile.gettempdir()) / filename


def check_anti_cheat(repo: Path, config: dict[str, Any]) -> tuple[bool, list[str], list[str]]:
    """Verify repository integrity against baseline snapshot and anti-cheat policies."""
    failed_nodes: list[str] = []
    warnings: list[str] = []

    # 0. Validate P2P/F2P test lists consistency
    verifier_dir = Path(__file__).resolve().parent
    sel_passed, sel_failed = validate_p2p_selection(config, verifier_dir)
    if not sel_passed:
        failed_nodes.extend(sel_failed)

    # 1. Validate baseline files against source-manifest.json if available
    manifest_path = resolve_source_manifest_path(repo)
    if not manifest_path:
        failed_nodes.append("anti_cheat_manifest_missing")
        warnings.append("source-manifest.json not found in candidate paths")
    else:
        try:
            manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
            for rel_path, meta in manifest_data.get("files", {}).items():
                if rel_path in ALLOWED_PROD_FILES:
                    continue
                target = repo / rel_path
                if not target.exists():
                    failed_nodes.append(f"anti_cheat_baseline_missing:{rel_path}")
                    warnings.append(f"Baseline file missing: {rel_path}")
                else:
                    sha = hashlib.sha256(target.read_bytes()).hexdigest()
                    if sha != meta.get("sha256"):
                        failed_nodes.append(f"anti_cheat_baseline_tampered:{rel_path}")
                        warnings.append(f"Baseline file tampered: {rel_path}")
        except Exception as exc:
            failed_nodes.append(f"anti_cheat_manifest_error:{exc}")

    # 2. Check candidate model patch if present in logs artifacts
    model_patch_path = resolve_model_patch_path(repo)
    if model_patch_path and model_patch_path.is_file() and model_patch_path.stat().st_size > 0:
        patch_text = model_patch_path.read_text(encoding="utf-8", errors="ignore")
        for line in patch_text.splitlines():
            if line.startswith("diff --git "):
                parts = line.split()
                if len(parts) >= 4:
                    b_path = parts[3].lstrip("b/")
                    if b_path.startswith("eval_tests/") or b_path.startswith("src/__hidden_verifier__/"):
                        failed_nodes.append(f"anti_cheat_model_patch_prohibited_path:{b_path}")
                    elif not b_path.startswith("src/"):
                        failed_nodes.append(f"anti_cheat_model_patch_unauthorized_path:{b_path}")
                    elif b_path in BASELINE_TEST_FILES:
                        failed_nodes.append(f"anti_cheat_model_patch_baseline_test_modified:{b_path}")
                    elif b_path in PROHIBITED_CONFIGS or b_path in PROHIBITED_HELPERS:
                        failed_nodes.append(f"anti_cheat_model_patch_prohibited_file:{b_path}")

    # 3. Check modified, added, deleted, staged, and untracked files via git
    all_touched_files: set[str] = set()
    base_commit = config.get("base_commit", "67d5447722eff38482a5bc5b5eed5f4229d2f80b")
    chk_base = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{base_commit}^{{commit}}"],
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    if chk_base.returncode != 0:
        base_commit = "HEAD"

    for cmd in (
        ["git", "diff", "--name-only", base_commit],
        ["git", "status", "--porcelain", "-uall"],
        ["git", "diff", "--name-only"],
        ["git", "diff", "--cached", "--name-only"],
    ):
        try:
            res = subprocess.run(
                cmd,
                cwd=repo,
                capture_output=True,
                text=True,
                check=False,
            )
            if res.returncode != 0:
                failed_nodes.append(f"anti_cheat_git_command_failed:{' '.join(cmd)}")
                return False, failed_nodes, warnings

            if "status" in cmd:
                for line in res.stdout.splitlines():
                    if len(line) >= 3:
                        path_part = line[3:].strip()
                        if " -> " in path_part:
                            for p in path_part.split(" -> "):
                                all_touched_files.add(p.strip())
                        else:
                            all_touched_files.add(path_part)
            else:
                for line in res.stdout.splitlines():
                    f = line.strip()
                    if f:
                        all_touched_files.add(f)
        except Exception as exc:
            failed_nodes.append(f"anti_cheat_git_check_failed:{exc}")
            return False, failed_nodes, warnings

    candidate_src_files_to_scan: set[str] = set()

    for f in sorted(all_touched_files):
        if f.endswith("/"):
            continue

        # Hidden test file created by verifier test.patch
        if f == "eval_tests/unified-node-size.test.ts":
            continue

        if f.startswith("eval_tests/") or f.startswith("src/__hidden_verifier__/"):
            failed_nodes.append(f"anti_cheat_prohibited_path_modified:{f}")
            warnings.append(f"WARNING: Candidate touched hidden test directory '{f}'.")
            continue

        # Prohibited prefixes
        if any(f.startswith(prefix) for prefix in ("tests/", "case/", ".github/")):
            failed_nodes.append(f"anti_cheat_prohibited_path_modified:{f}")
            warnings.append(f"WARNING: Candidate touched protected directory '{f}'.")
            continue

        # Protected configs and lockfiles
        file_name = Path(f).name
        if f in PROHIBITED_CONFIGS or file_name.startswith("bunfig") or file_name.startswith(".bunfig"):
            failed_nodes.append(f"anti_cheat_prohibited_file_modified:{f}")
            warnings.append(f"WARNING: Candidate modified config or lockfile '{f}'.")
            continue

        # Protected test helpers
        if f in PROHIBITED_HELPERS or (f.startswith("src/") and f.endswith("test-utils.ts")):
            failed_nodes.append(f"anti_cheat_test_helper_modified:{f}")
            warnings.append(f"WARNING: Candidate modified test helper file '{f}'.")
            continue

        # Baseline test suites
        if f in BASELINE_TEST_FILES:
            failed_nodes.append(f"anti_cheat_existing_test_modified:{f}")
            warnings.append(f"WARNING: Candidate modified baseline test file '{f}'.")
            continue

        # Files under src/
        if f.startswith("src/"):
            if f in ALLOWED_PROD_FILES:
                candidate_src_files_to_scan.add(f)
                continue
            if f.endswith(".test.ts") and f not in BASELINE_TEST_FILES:
                candidate_src_files_to_scan.add(f)
                continue
            if f.endswith(".ts") and f not in BASELINE_SRC_FILES and not f.endswith("test-utils.ts"):
                candidate_src_files_to_scan.add(f)
                continue
            failed_nodes.append(f"anti_cheat_unauthorized_src_modified:{f}")
            warnings.append(f"WARNING: Candidate modified unauthorized source path '{f}'.")
            continue

        # Files outside src/
        failed_nodes.append(f"anti_cheat_unauthorized_path_modified:{f}")
        warnings.append(f"WARNING: Candidate modified file outside src/: '{f}'.")

    # 4. Hidden test suite file integrity verification
    eval_test_file = repo / "eval_tests/unified-node-size.test.ts"
    if eval_test_file.exists():
        actual_eval_sha = hashlib.sha256(eval_test_file.read_bytes()).hexdigest()
        if actual_eval_sha != EXPECTED_EVAL_TESTS_SHA256:
            failed_nodes.append("anti_cheat_hidden_tests_tampered")
            warnings.append("WARNING: eval_tests/unified-node-size.test.ts content tampered.")

    # 5. Scan candidate source files for malicious or exploit tokens in executable code
    for rel_f in sorted(candidate_src_files_to_scan):
        src_file = repo / rel_f
        if src_file.exists():
            text = src_file.read_text(encoding="utf-8", errors="ignore")
            detected_tokens = scan_for_forbidden_code(text)
            for pattern in detected_tokens:
                failed_nodes.append(f"anti_cheat_malicious_code_detected:{rel_f}:{pattern}")
                warnings.append(f"WARNING: Malicious or forbidden token '{pattern}' detected in '{rel_f}'.")

    return (len(failed_nodes) == 0, failed_nodes, warnings)


def check_post_test_integrity(repo: Path, config: dict[str, Any]) -> tuple[bool, list[str], list[str]]:
    """Verify repository state after test suite execution to prevent runtime mutations."""
    passed, failed_nodes, warnings = check_anti_cheat(repo, config)
    if not passed:
        runtime_failed = [
            f"anti_cheat_runtime_{node}" if not node.startswith("anti_cheat_") else node
            for node in failed_nodes
        ]
        return False, runtime_failed, warnings
    return True, [], []


def check_integration_tests(
    repo: Path,
    statuses: dict[str, str],
    details: dict[str, dict[str, Any]],
) -> tuple[bool, list[str]]:
    """Verify human-confirmed real repository integration tests executed and passed."""
    failed_nodes: list[str] = []

    for node in CONFIRMED_INTEGRATION_NODES:
        status = statuses.get(node)
        if status != "passed":
            failed_nodes.append(f"integration_test_failed:{node}")

    if failed_nodes:
        return False, failed_nodes

    return True, []


def check_build(repo: Path, config: dict[str, Any]) -> tuple[bool, list[str]]:
    """Verify repository configuration and clean TypeScript / lint compilation."""
    failed_nodes: list[str] = []

    for req in ["package.json", "tsconfig.json"]:
        if not (repo / req).exists():
            failed_nodes.append(f"build_missing_required_file:{req}")

    compile_paths = config.get("hard_gate", {}).get("compile_paths", [])
    for c_path in compile_paths:
        if not (repo / c_path).exists():
            failed_nodes.append(f"build_missing_compile_path:{c_path}")

    if failed_nodes:
        return False, failed_nodes

    bun_bin = os.environ.get("BUN_BIN") or shutil.which("bun")
    if not bun_bin or not Path(bun_bin).exists():
        failed_nodes.append("build_bun_not_found")
        return False, failed_nodes
    env = os.environ.copy()

    # TypeScript typecheck
    try:
        proc = subprocess.run(
            [bun_bin, "run", "lint:ts"],
            cwd=repo,
            capture_output=True,
            text=True,
            env=env,
            timeout=180,
            check=False,
        )
        if proc.returncode != 0:
            failed_nodes.append("build_typecheck_failed")
    except subprocess.TimeoutExpired:
        failed_nodes.append("build_typecheck_timeout")
    except Exception as exc:
        failed_nodes.append(f"build_typecheck_error:{exc}")

    # Linter / formatter check (runs biome check to match instruction.md)
    try:
        biome_bin = repo / "node_modules/.bin/biome"
        lint_cmd = [str(biome_bin), "check"] if biome_bin.exists() else [bun_bin, "x", "@biomejs/biome", "check"]
        proc_lint = subprocess.run(
            lint_cmd,
            cwd=repo,
            capture_output=True,
            text=True,
            env=env,
            timeout=60,
            check=False,
        )
        if proc_lint.returncode != 0:
            failed_nodes.append("build_lint_failed")
    except subprocess.TimeoutExpired:
        failed_nodes.append("build_lint_timeout")
    except Exception as exc:
        failed_nodes.append(f"build_lint_error:{exc}")

    return (len(failed_nodes) == 0, failed_nodes)


def load_p2p_nodes(config: dict[str, Any], verifier_dir: Path | None = None) -> list[str]:
    """Return verified P2P nodes directly from config.json."""
    return [str(node).strip() for node in config.get("p2p", []) if str(node).strip()]


def execute_test_suite(
    repo: Path,
) -> tuple[int, dict[str, str], dict[str, dict[str, Any]], set[str], list[str]]:
    """Execute the full test suite directly via Bun stream capture.

    Runs with per-test timeout=60000 to guarantee stability across resource-constrained
    environments, without relying on candidate-writable files or external reporters.
    """
    runner_errors: list[str] = []
    bun_bin = os.environ.get("BUN_BIN") or shutil.which("bun")
    if not bun_bin or not Path(bun_bin).exists():
        runner_errors.append("build_bun_not_found")
        return 1, {}, {}, set(), runner_errors
    env = os.environ.copy()

    log_file = resolve_verifier_log_file(repo, "bun-test.log")

    statuses: dict[str, str] = {}
    details: dict[str, dict[str, Any]] = {}
    duplicate_ids: set[str] = set()
    exit_code = 0

    opt_file = repo / "src/grid/lane/opt.test.ts"
    orig_opt_content: str | None = None
    if opt_file.exists():
        try:
            c = opt_file.read_text(encoding="utf-8")
            if "}, 30000);" in c:
                orig_opt_content = c
                opt_file.write_text(c.replace("}, 30000);", "}, 60000);"), encoding="utf-8")
        except Exception:
            pass

    try:
        proc = subprocess.run(
            [bun_bin, "test", "--timeout=60000"],
            cwd=repo,
            capture_output=True,
            text=True,
            env=env,
            timeout=300,
            check=False,
        )
        exit_code = proc.returncode

        combined_output = (proc.stdout or "") + "\n" + (proc.stderr or "")

        try:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            log_file.write_text(
                f"STDOUT:\n{proc.stdout}\n\nSTDERR:\n{proc.stderr}\nEXIT_CODE: {proc.returncode}\n",
                encoding="utf-8",
            )
        except Exception:
            pass

        file_re = re.compile(r"^([a-zA-Z0-9_\-./]+\.test\.ts):")
        test_re = re.compile(r"^\((pass|fail|skip)\)\s+(.*?)(?:\s+\[([0-9.]+(?:ms|s|µs|ns))\])?$")
        trailer_summary_re = re.compile(r"^\d+\s+tests?\s+failed:")

        curr_file: str | None = None
        curr_err_lines: list[str] = []

        for raw_line in combined_output.splitlines():
            line = raw_line.strip()
            if trailer_summary_re.match(line):
                curr_file = None
                curr_err_lines = []
                continue

            mf = file_re.match(line)
            if mf:
                curr_file = mf.group(1)
                try:
                    p = Path(curr_file)
                    if p.is_absolute():
                        curr_file = str(p.relative_to(repo))
                except Exception:
                    pass
                curr_err_lines = []
                continue

            mt = test_re.match(line)
            if mt and curr_file:
                status_str, name, duration_str = mt.groups()
                test_id = f"{curr_file}::{name}"

                if status_str == "pass":
                    curr_status = "passed"
                elif status_str == "skip":
                    curr_status = "skipped"
                else:
                    curr_status = "failed"

                time_s = 0.0
                if duration_str:
                    if duration_str.endswith("ms"):
                        time_s = float(duration_str[:-2]) / 1000.0
                    elif duration_str.endswith("s"):
                        time_s = float(duration_str[:-1])
                    elif duration_str.endswith("µs"):
                        time_s = float(duration_str[:-2]) / 1_000_000.0

                is_assertion_failure = any(
                    "expect(" in l or "Expected" in l or "assert" in l.lower()
                    for l in curr_err_lines
                )
                is_timeout = any("timed out" in l.lower() or "timeout" in l.lower() for l in curr_err_lines)
                failure_msg = "\n".join(curr_err_lines[-15:]) if curr_status == "failed" else ""

                instance = {
                    "status": curr_status,
                    "time": time_s,
                    "failure_message": failure_msg,
                    "is_assertion_failure": is_assertion_failure,
                    "is_timeout": is_timeout,
                }
                if test_id in statuses:
                    duplicate_ids.add(test_id)
                    # Bun permits same-title parameterized instances. Preserve all
                    # outcomes; a later pass must never erase a failure or skip.
                    details[test_id]["instances"].append(instance)
                    severity = {"passed": 0, "skipped": 1, "failed": 2}
                    if severity[curr_status] > severity[statuses[test_id]]:
                        statuses[test_id] = curr_status
                        for key in ("failure_message", "is_assertion_failure", "is_timeout"):
                            details[test_id][key] = instance[key]
                    details[test_id]["time"] += time_s
                else:
                    statuses[test_id] = curr_status
                    details[test_id] = {
                        "time": time_s,
                        "failure_message": failure_msg,
                        "is_assertion_failure": is_assertion_failure,
                        "is_timeout": is_timeout,
                        "instances": [instance],
                    }
                curr_err_lines = []
            else:
                if line:
                    curr_err_lines.append(line)

        # Ensure Bun actually ran and finished the test suite
        trailer_ran = re.search(r"Ran\s+(\d+)\s+tests\s+across\s+(\d+)\s+files\.", combined_output)
        if not trailer_ran:
            runner_errors.append("test_runner_premature_exit")
        elif not statuses:
            runner_errors.append("test_runner_no_tests_executed")

    except subprocess.TimeoutExpired:
        runner_errors.append("test_runner_timeout")
        exit_code = -1
    except Exception as exc:
        runner_errors.append(f"test_runner_error:{exc}")
        exit_code = -1
    finally:
        if orig_opt_content is not None and opt_file.exists():
            try:
                opt_file.write_text(orig_opt_content, encoding="utf-8")
            except Exception:
                pass

    return exit_code, statuses, details, duplicate_ids, runner_errors


def evaluate_hard_gate(
    config: dict[str, Any],
    repo: Path,
    apply_failed: int = 0,
    parsed_execution: tuple[int, dict[str, str], dict[str, dict[str, Any]], set[str], list[str]] | None = None,
    build_result: tuple[bool, list[str]] | None = None,
    anti_cheat_result: tuple[bool, list[str], list[str]] | None = None,
    post_anti_cheat_result: tuple[bool, list[str], list[str]] | None = None,
) -> dict[str, Any]:
    """Execute compile, anti-cheat, integration test, and atomic P2P test gates."""
    hard_gate_cfg = config.get("hard_gate", {})
    cheat_penalty = float(hard_gate_cfg.get("cheat_penalty", -1.0))
    compile_paths = hard_gate_cfg.get("compile_paths", [])

    failed_nodes: list[str] = []

    # 1. Candidate patch application check
    if bool(apply_failed):
        failed_nodes.append("candidate_patch_apply")
        return {
            "passed": False,
            "apply_failed": True,
            "compile_paths": compile_paths,
            "failed_nodes": failed_nodes,
            "cheat_penalty": cheat_penalty,
            "build_gate": {"passed": False, "failed_nodes": ["candidate_patch_apply"]},
            "anti_cheat": {"passed": False, "failed_nodes": ["candidate_patch_apply"], "warnings": []},
            "integration_gate": {"passed": False, "failed_nodes": ["candidate_patch_apply"]},
            "p2p": {"passed": False, "total": 0, "passed_count": 0, "failed_nodes": ["candidate_patch_apply"]},
            "p2p_statuses": {},
        }

    # 2. Anti-cheat check
    if anti_cheat_result is not None:
        anti_cheat_passed, cheat_failed_nodes, cheat_warnings = anti_cheat_result
    else:
        anti_cheat_passed, cheat_failed_nodes, cheat_warnings = check_anti_cheat(repo, config)
    if not anti_cheat_passed:
        failed_nodes.extend(cheat_failed_nodes)

    # 3. Post-execution integrity check
    if post_anti_cheat_result is not None:
        post_cheat_passed, post_failed_nodes, post_warnings = post_anti_cheat_result
    else:
        post_cheat_passed, post_failed_nodes, post_warnings = check_post_test_integrity(repo, config)
    if not post_cheat_passed:
        failed_nodes.extend(post_failed_nodes)

    # 4. Build check
    if build_result is not None:
        build_passed, build_failed_nodes = build_result
    else:
        build_passed, build_failed_nodes = check_build(repo, config)
    if not build_passed:
        failed_nodes.extend(build_failed_nodes)

    # 5. Atomic P2P tests check from single execution
    verifier_dir = Path(__file__).resolve().parent
    sel_passed, sel_failed = validate_p2p_selection(config, verifier_dir)
    for n in sel_failed:
        if n not in failed_nodes:
            failed_nodes.append(n)

    p2p_nodes = load_p2p_nodes(config, verifier_dir)

    if parsed_execution is None:
        exit_code, statuses, details, duplicate_ids, runner_errors = execute_test_suite(repo)
    else:
        exit_code, statuses, details, duplicate_ids, runner_errors = parsed_execution

    p2p_failed_nodes: list[str] = []
    p2p_statuses: dict[str, str] = {node: "pending" for node in p2p_nodes}

    if len(p2p_nodes) < 30:
        p2p_failed_nodes.append("p2p_insufficient_atomic_nodes_count")
        for node in p2p_nodes:
            p2p_statuses[node] = "failed"
    elif not sel_passed:
        p2p_failed_nodes.extend(sel_failed)
        for node in p2p_nodes:
            p2p_statuses[node] = "failed"
    else:
        if runner_errors:
            p2p_failed_nodes.extend(runner_errors)
            for node in p2p_nodes:
                p2p_statuses[node] = "failed"
        else:
            if exit_code < 0:
                p2p_failed_nodes.append(f"runner_signal_terminated:{abs(exit_code)}")

            if exit_code not in (0, 1):
                p2p_failed_nodes.append(f"runner_abnormal_exit_code:{exit_code}")

            # Fixed selectors must identify a unique instance. Extra candidate
            # tests do not become scoring selectors merely by sharing a title.
            selected_ids = (set(p2p_nodes) | set(config.get("f2p", []))
                            | set(config.get("advisory_ids", []))
                            | set(CONFIRMED_INTEGRATION_NODES))
            for dup_id in sorted(duplicate_ids):
                if dup_id in selected_ids:
                    p2p_failed_nodes.append(f"duplicate_test_id:{dup_id}")
                elif statuses.get(dup_id) != "passed":
                    p2p_failed_nodes.append(f"additional_test_not_passed:{dup_id}")

            for node in p2p_nodes:
                status = "failed" if node in duplicate_ids else statuses.get(node)
                if status == "passed":
                    p2p_statuses[node] = "passed"
                elif status in ("failed", "error", "skipped"):
                    p2p_statuses[node] = status
                    p2p_failed_nodes.append(node)
                else:
                    p2p_statuses[node] = "missing"
                    p2p_failed_nodes.append(node)

            if exit_code == 1:
                total_failed_tests = sum(st != "passed" for st in statuses.values())
                if total_failed_tests == 0:
                    p2p_failed_nodes.append("runner_exit_1_with_zero_test_failures")

    if p2p_failed_nodes:
        failed_nodes.extend(p2p_failed_nodes)

    # 6. Integration test existence and pass check
    integration_passed, integration_failed_nodes = check_integration_tests(repo, statuses, details)
    if not integration_passed:
        failed_nodes.extend(integration_failed_nodes)

    p2p_passed = len(p2p_failed_nodes) == 0
    passed = len(failed_nodes) == 0
    p2p_passed_count = sum(1 for status in p2p_statuses.values() if status == "passed")

    total_cheat_failed = cheat_failed_nodes + post_failed_nodes
    total_cheat_warnings = cheat_warnings + post_warnings

    return {
        "passed": passed,
        "apply_failed": False,
        "compile_paths": compile_paths,
        "failed_nodes": sorted(set(failed_nodes)),
        "cheat_penalty": 0.0 if passed else cheat_penalty,
        "build_gate": {
            "passed": build_passed,
            "failed_nodes": build_failed_nodes,
        },
        "anti_cheat": {
            "passed": anti_cheat_passed and post_cheat_passed,
            "failed_nodes": total_cheat_failed,
            "warnings": total_cheat_warnings,
        },
        "integration_gate": {
            "passed": integration_passed,
            "failed_nodes": integration_failed_nodes,
        },
        "p2p": {
            "passed": p2p_passed,
            "total": len(p2p_nodes),
            "passed_count": p2p_passed_count,
            "failed_nodes": p2p_failed_nodes,
        },
        "p2p_statuses": p2p_statuses,
    }


def run_hard_gate(
    config_path: Path,
    repo: Path,
    apply_failed: int = 0,
) -> dict[str, Any]:
    """Standalone entry for hard gate execution."""
    config = json.loads(config_path.read_text(encoding="utf-8"))
    return evaluate_hard_gate(config, repo, apply_failed=apply_failed)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile, integrity, anti-cheat, and atomic P2P hard gates.")
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply-failed", type=int, choices=(0, 1), default=0)
    args = parser.parse_args()

    result = run_hard_gate(
        config_path=args.config,
        repo=args.repo,
        apply_failed=args.apply_failed,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
