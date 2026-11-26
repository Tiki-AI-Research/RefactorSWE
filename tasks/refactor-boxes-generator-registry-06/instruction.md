# Use one generator catalog for discovery and grouping

Generator consumers currently scan the package independently. Discovery changes shared package state, grouping appends to global UI-group collections, and one consumer captures its generators at import time. Repeated queries can therefore accumulate group entries or keep a stale view.

Provide one cached catalog with complete, web-interface, and UI-group views. Group construction must be idempotent: repeated listing, lookup, web catalog, gallery, or server construction cannot add another copy of a generator. Remove permanent discovery-time mutation of shared package state, and route the CLI listing, web-generator snapshot, webserver catalog, and gallery through the catalog rather than independent scans. Keep extension-path reachability, including later discovery in the same process.

## Existing discovery and presentation interfaces

Preserve these no-argument entry points and mapping meanings:

| Entry point | Result |
| --- | --- |
| `getAllBoxGenerators()` | Fully qualified `module.ClassName` keys mapped to generator classes. |
| `getAllGeneratorModules()` | Module short names mapped to imported module objects. |

`BOXES_GENERATOR_PATH` remains a colon-separated list of additional discovery directories. Extension generators use the same key scheme as bundled generators; a later discovery call must still reach them without losing any bundled generator.

Keep the importable ordered `ui_groups` and `ui_groups_by_name` definitions. `UIGroup` retains its `name`, `title`, `description`, `image`, `generators`, and existing thumbnail/image properties. Group order and descriptions stay unchanged. Unknown declared group names fall back to `Misc`, and generators within each group remain sorted by generator name.

The `--list` output still begins with `Available generators:`, then prints each group title, its description when present, and generator entries in the existing format ` *  {name:<15} - {description}`. Preserve the complete current output format, with each generator listed once, including exactly one `HolePattern` entry.

The webserver object keeps `boxes`, `groups`, and `groups_by_name`. Its view includes only generators with `webinterface` enabled, and the gallery contains one entry per generator. Do not change any bundled generator or its web-interface and UI-group classifications.

## Completion and scope

Consecutive `getAllBoxGenerators()` calls return identical full bundled key sets: 195 generators in this checkout. Repeated listing or webserver construction does not grow group lists, and one catalog still exposes all 182 web-interface generators. An extension directory containing one extra generator yields 196 total, retains all bundled generators, and remains reachable by later discovery calls in that process.

Shared caching must satisfy these reachability requirements rather than permanently freezing discovery before an extension can be seen. The organization of scanning, caching, grouping, and private helpers is free, provided the public entry points, signatures, return shapes, flags, and presentation remain compatible.

Use existing dependencies and retain extension-path syntax and discovery semantics apart from removing shared package/group-state writes. Limit changes to necessary production code, tests, and directly supporting adjustments. Leave packaging metadata, unrelated import-time behavior, documentation, code, and formatting alone.

Work on a new branch from `main` and commit the completed changes.
