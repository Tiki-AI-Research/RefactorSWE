## Background

The generic parsing package currently owns editor-specific syntax-tree and DOM normalization logic. This mixes core Markdown parsing with representation details used by the editor. It also makes the parser responsible for transformations that belong to the editor layer.

## Goal

- Move editor-specific transformation logic out of the generic parsing implementation. Treat the existing editor-facing transformations as one coherent responsibility, rather than moving only the obvious entry points.
- The editor-owned component MUST implement the transformations. The parsing package MUST delegate them without implementing or duplicating their conversion logic.
- Keep dependencies explicit and acyclic. Context needed by the editor layer must be supplied per invocation; do not use mutable global state or hidden execution context.
- The design of new internal types, helper functions, callbacks, and source files is left to the implementation.

## Public contract to preserve

- Preserve existing exported entry points in the parsing package and all high-level Markdown, editor DOM, and export pipelines. Existing callers MUST NOT require migration.
- Public signatures, return values, in-place mutation behavior, parser options, and downstream protocols MUST remain compatible.

## Behavior that must stay unchanged

- Existing AST mutations and serialized outputs MUST remain equivalent for normal rendering, editor rendering, and export modes across all supported inline and DOM constructs.
- For nil, empty, malformed, and incomplete input, every existing safe fallback MUST remain in place without new panics or partial mutation. In particular, nil parser options MUST remain valid on branches that do not use those options.
- The only required safety extensions are that regular and hybrid flattening of a nil root MUST be no-ops, and text-mark membership on a nil node MUST be false. These are explicit exceptions to preserving baseline panic behavior.
- Results MUST be deterministic and isolated to the target tree. Equivalent calls MUST NOT depend on retained mutable state or change unrelated document structures.

## constraints

- Limit production changes to this responsibility migration and the compatibility wiring it requires. Do not change unrelated grammar, external protocols, or dependency versions.
- Do not remove supported behavior to simplify the refactor.
- Do not modify, bypass, or disable existing tests. New tests may be added outside evaluator-owned directories.
