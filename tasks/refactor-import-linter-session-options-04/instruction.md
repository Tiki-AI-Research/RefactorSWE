## Background
Import Linter's session-level configuration reaches the application as an untyped mapping of raw values, and several consumers independently re-interpret the same entries. Some sites accept only the exact strings "True" and "true", while others lower-case the raw value before comparing, so the same configuration item is explained differently in different places and consumers can disagree about whether an option is enabled. This duplicated, implicit interpretation makes session options fragile, particularly for values that do not match the exact spellings each site happens to expect. The work below removes that duplication by giving session options a single typed, semantic owner, while preserving every capability that users, integrators, and custom contract types rely on.

## Goal
- Give session-level options a typed representation that owns the reading and boolean normalization of the root-packages, external-packages, type-checking-imports, and timing options, so no consumer needs to know how raw configuration values are stored.
- Replace the scattered per-consumer value comparisons with that one shared interpretation, so graph building and contract checks can never disagree about whether a session option is enabled.
- Preserve the externally observable behaviour of configuration loading, linting results, and the public API while eliminating the duplicated parsing logic.
- Keep custom contract types working unchanged: they receive session options and read at least the root-packages entry by key.

## Public contract to preserve
- `importlinter.api.read_configuration(config_filename: str | None = None) -> dict` MUST keep returning a plain dictionary with exactly two keys: `"session_options"` (a dictionary of the string values read from the top-level configuration) and `"contracts_options"` (a list of dictionaries, each keyed by `"name"`, `"type"`, and any contract-specific options). A single `root_package` entry is still normalized into a single-item `root_packages` list, and a missing configuration file still raises `FileNotFoundError`.
- The linting entry point that the CLI invokes, `importlinter.application.use_cases.lint_imports(config_filename, limit_to_contracts, cache_dir, is_debug_mode, show_timings, no_logo, verbose) -> bool`, MUST keep those parameters, their existing defaults and flags, and its boolean result: `True` when linting passes and `False` when it does not. No `lint_imports` alias may be added to `importlinter.api`, which MUST continue to expose `read_configuration` as its public Python function.
- The public `Contract` base class, which custom contract types subclass, MUST keep receiving session options as a mapping that can be read by key for at least the root-packages entry, without requiring custom contract types to change.
- Custom contract hooks MUST be able to add, update, and delete session entries by key. Those changes MUST remain visible to later contracts checked in the same lint session, so custom types can exchange session metadata through the mapping.
- Internal details may change freely: the in-memory storage type for session options, the per-option parsing helpers, and the equality behaviour of the user-options container are not part of the public contract.

## Behavior that must stay unchanged
- Session boolean strings MUST be interpreted case-insensitively: every letter-case spelling of `true` MUST mean enabled, and every letter-case spelling of `false` MUST mean disabled. Changing only the letter case MUST NOT change the option's meaning. All consumers MUST derive the same boolean for the same raw value; in particular, the decision to include external packages when building the graph and the forbidden contract's check that externals were included MUST never disagree.
- When the external-packages option is absent, it MUST remain unset, deferring to the graph builder's default rather than becoming an explicit false, and forbidden contracts MUST treat that case as externals not having been included.
- The type-checking-imports option set to `True` or `true` MUST still exclude imports made inside `if TYPE_CHECKING:` guards, while `False` or an absent option MUST still include them, leaving overall lint results unchanged.
- Configuration loading MUST keep producing the same raw values: INI options remain strings, and TOML booleans are still stringified to `True` or `False` before option interpretation.
- `read_configuration` MUST NOT expose the new typed object or convert any value to a boolean; its returned structure and string payloads MUST stay as they are today.
- Normalizing a single `root_package` into `root_packages` MUST still happen before the graph is built and before contracts are constructed, and the legacy singular key MUST NOT be passed through.
- Session options that do not currently affect behaviour, such as timing display, which is driven by the public flag, MUST NOT start affecting output or results as a side effect of this change.
- Failures MUST still surface through existing channels: a missing configuration file as `FileNotFoundError` from `read_configuration`, and linting errors as a `False` result from the CLI lint entry point unless debug mode is enabled.

## constraints
1. Do not change any public signature, return shape, flag, default, or error type; no public capability may be deleted, renamed, or reduced.
2. Do not change the raw values produced by configuration loading or TOML boolean stringification, and do not add, remove, or rename configuration keys.
3. The unified, case-insensitive interpretation must be shared by every consumer; no consumer may retain a private rule.
4. Do not add runtime dependencies, and do not perform unrelated refactors, renames, or behaviour changes outside the session-option interpretation.
5. Limit changes to the production code, tests, and supporting adjustments strictly necessary to converge session-option parsing on the typed representation.

IMPORTANT: Please work on this in a new branch from main and commit everything when you are done.
