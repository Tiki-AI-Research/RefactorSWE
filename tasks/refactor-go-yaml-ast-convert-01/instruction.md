# Put common AST capabilities on nodes

Traversal, formatting, key extraction, and decoding repeat lists of YAML AST node kinds in separate conditional chains. A new or wrapped kind consequently needs corresponding changes in several places. Replace that duplicated dispatch knowledge with one polymorphic capability set for child enumeration, first-token lookup, and visitor acceptance. Each shipped node kind supplies its behavior once; consumers use those capabilities rather than maintaining parallel type lists.

Choose internal names, organization, and implementation freely while retaining the existing public surface and all observable results. New capabilities are additive: keep current `Node` methods and consumers compatible, and ensure every node type shipped by the module supports the added capabilities.

## Traversal and node compatibility

Keep exported entry points unchanged in name, signature, and meaning:

| Entry point | Preserved result |
| --- | --- |
| `Walk(visitor, node)` | The same depth-first visit sequence and visitor protocol. |
| `Parent(root, child)` | The same parent identity or nil. |
| `Filter(nodeType, node)` | The same `[]Node`, in the same order. |
| `FilterFile(nodeType, file)` | The same `[]Node` collected across documents. |

Preserve `Visitor` and all existing node capabilities: type identification, token access, comment get/set, column adjustment, path get/set, text rendering, YAML marshaling, and reading. Parent lookup continues binding comments to the same nodes. New internals must not remove, rename, or narrow any exported API, error value, or sentinel, or break consumers using only the current public surface.

## Decoding, formatting, and paths

Mappings, sequences, scalars, anchors, aliases, tags, merges, and nulls keep their current decoded values, error values, and error messages. Preserve the merge flag's meaning, including acceptance of sequence input only in merge contexts.

Tag-, anchor-, and alias-wrapped values retain their existing success or error outcomes, including wrapped sequences, mappings, nulls, and combined anchor/alias cases. They do not gain panics or unexpected-node-type errors through this refactor. Anchor registration retains its timing and name-to-value mapping, repeated aliases resolve identically, unresolved aliases keep their error, and depth overflow returns the same depth-limit sentinel.

All public formatting entry points remain byte-identical for every supported kind, comment placement, and block or flow style. Recursive path filtering and replacement select the same values and change the same locations; selectors with no match retain their empty result rather than becoming errors. Text extracted from anchor-, alias-, or tag-wrapped mapping keys remains the text used by path selection and replacement.

## Completion and scope

Common dispatch is supplied at node level and consumed by the affected traversal, token, formatting, key, and decoding paths. Existing traversal order, parent identity, comment binding, encoding/decoding, paths, and errors stay unchanged. Preserve linear traversal and decoding in node count without adding full passes or repeated work.

Use the existing module dependencies without adding third-party packages or changing the dependency graph. Restrict edits to necessary production code and directly accompanying tests. Leave unrelated refactoring, formatting, and documentation rewrites out.

Work on a new branch from the supplied baseline commit `edee2f91616c6d73112a13e7c0dbde72ce938877` and commit the completed changes.
