# Separate graph-mapping responsibilities

The mapping phase interleaves root discovery, root separation, grid reservation/sizing, fanout layout, edge paths/labels, coordinate conversion, and subgraph bounds/offsets through implicit mutable state. Give these responsibilities dedicated cohesive units with explicit state ownership so they can be understood and verified independently. Keep the mapping entry point a short ordered orchestration rather than a container of layout logic. Private units, state holders, and call organization are yours to choose.

Preserve `graph.Parse(mermaid string, styleType string) (*Properties, error)`, `graph.Draw(*Properties) string`, all exported identifiers/signatures, and `Properties.ShowCoords`. CLI stdin/file input and stdout output retain `--file/-f`, `--coords/-c`, `--ascii/-a`, `--paddingX/-x`, `--paddingY/-y`, `--borderPadding/-p`, `--verbose/-v`, and `--max-width`, with current defaults and meaning. Invalid parse/CLI inputs still produce errors, diagnostics, and nonzero exits rather than partial/truncated diagrams.

Every supported diagram must retain output bytes, spacing, dimensions, and labels, including checked-in ASCII, extended-character, multibyte, subgraph, top-down, and fanout references. Coordinate overlay grids, node boxes, and annotations remain character-identical for equal inputs/flags.

Keep observable mapping order: roots, external/subgraph separation, level reservation, column/row sizing, fanout, edge-path/label-line determination, grid-to-drawing conversion, then subgraph bounds and offsets. In LR layouts mixing external roots with subgraph roots that have edges, retain the one-level subgraph-root offset; without that mix, treat roots uniformly. Occupied requested coordinates advance to the next free slot in the same direction without overlaps or missing nodes. Edge routing, fanout order, label lines, and subgraph bounds/offsets remain unchanged for every input.

Completion requires explicit separated responsibilities and ordered orchestration, supported by the existing suite and minimal relevant tests/support. Add no dependencies, module requirements, flags, or public entries. Restrict production changes to mapping; do not alter parser/render stages outside it, expected outputs, unrelated code, names, or formatting.

Work in a new branch from `main` and commit the completed changes.
