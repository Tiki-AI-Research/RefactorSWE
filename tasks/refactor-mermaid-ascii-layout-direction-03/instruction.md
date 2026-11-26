## Background
The graph layout pipeline represents its layout axis as a bare string ("LR" or "TD") and decides direction-dependent behavior through repeated string comparisons spread across parsing, layout, edge routing and fan-out handling (nineteen explicit direction checks today). Consequently the parser vocabulary, the stored representation and the layout rules are unnecessarily entangled: the meaning of a direction is implicit in scattered conditionals, and every direction-sensitive rule must be found and kept in sync by hand. The refactor should remove that coupling by letting the layout direction itself answer direction-dependent questions, while users keep the same Mermaid inputs, the same public API and exactly the same drawings.

## Goal
- Replace the string direction type code used by the graph layout pipeline with a layout-direction abstraction that carries direction-dependent behavior, so layout code no longer branches on literal "LR"/"TD" comparisons.
- Move every direction-dependent decision behind that abstraction while keeping each axis's present outcome: self-reference start and end directions, backwards-edge detection, preferred and alternative route selection, grid stepping and coordinate growth, parallel directions for repeated edges, and fan-out branch handling.
- Keep a single mapping point for direction: the Mermaid declaration is translated once into the direction abstraction (LR and RL to the horizontal axis, TD, TB and BT to the vertical axis, no direction to the vertical axis), and no other component reinterprets direction strings.
- Preserve the public surface and observable behavior: accepted inputs, rendered output, defaults, errors and the configuration contract must not change.
- Leave the mechanism open: whether the abstraction is a value type, an interface with per-axis implementations or another construct is the implementer's choice; no particular design pattern or file organization is required.

## Public contract to preserve
- `diagram.Config.GraphDirection` remains a public `string` field whose accepted values are exactly `"LR"` and `"TD"`; `Config.Validate()` must keep rejecting any other value with a `ConfigError` that names the `GraphDirection` field.
- `NewConfig(useAscii bool, graphDirection, styleType string) (*Config, error)`, `NewCLIConfig(...) (*Config, error)`, `NewWebConfig(...) (*Config, error)` and `NewTestConfig(useAscii bool, styleType string) *Config` keep their parameter lists and existing `"LR"` defaults.
- `graph.Parse(mermaid, styleType string)` keeps returning `(*Properties, error)`; `(*Properties).Apply(config *diagram.Config)` and `Draw(properties *Properties) string` keep their signatures and remain the supported parse, configure and render entry points.
- `render.RenderDiagram(input string, config *diagram.Config) (string, error)` and `render.RenderDiagramWithStatus(input string, config *diagram.Config) (string, WidthStatus, error)` keep their signatures and results, including width-status reporting.
- The stored representation of a parsed direction and the internal helpers that consume it may change freely; only the observable mapping and layout outcomes listed below are binding.

## Behavior that must stay unchanged
- Rendered diagrams MUST remain byte-for-byte identical for every accepted input on both axes, including node and box placement, edge paths and arrowheads, labels, subgraph output and coordinate overlays.
- Direction parsing MUST keep defaulting to the vertical axis, MUST keep mapping LR and RL to the horizontal axis without reversal, MUST keep mapping TD, TB and BT to the vertical axis without reversal, MUST remain case-sensitive, and MUST still return the existing `unsupported graph direction` error, whose supported-direction list remains `TD, TB, BT, LR, RL`.
- Self-referencing edges, backwards edges, repeated and bidirectional edges including their parallel routing, and fan-out branch labels MUST keep their existing per-axis start and end directions, paths and label placement; fan-out special handling MUST continue to apply only to vertical layouts that have no subgraphs.
- Layout MUST stay deterministic: the same input and configuration produce identical output, and the existing ordering of nodes and edges MUST NOT change.
- Invalid declarations MUST keep returning their current errors instead of panicking: unsupported graph type, extra tokens after the direction, and unknown direction; a declaration without a direction MUST NOT become an error.
- Configuration validation MUST NOT regress: values outside `"LR"` and `"TD"` are still rejected by the existing field-scoped error, and valid default configurations still succeed.
- The layout axis MUST continue to come from the Mermaid declaration; rendering MUST NOT begin requiring or honoring a new direction source, flag or parameter.

## constraints
1. Keep this a behavior-preserving refactor: no observable change to rendered output, parsed direction semantics, defaults or error behavior.
2. Do not remove, rename, narrow or change the contract of any public API, configuration field, CLI flag, default value or public error; do not add required parameters, flags, environment variables or configuration inputs.
3. Do not add third-party dependencies or expand existing ones, and do not move direction handling into a new module or package boundary.
4. Do not make unrelated changes such as drive-by renames, formatting churn, or edits to other diagram pipelines or unrelated layout features.
5. Confine edits to the graph layout pipeline, its direction-dependent helpers, the declaration-to-direction mapping and the matching test and support adjustments; every changed line must serve the direction abstraction.

IMPORTANT: Please work on this in a new branch from main and commit everything when you are done.