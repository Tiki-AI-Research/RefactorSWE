# Unify session module identity and resource ownership

Session persistence mixes secure file access, saved-module identity, temporary runtime registration, and imported-reference substitution across its dump and load paths. Shared temporary state and cleanup make these paths difficult to keep consistent.

Refactor that state management across `dump_module`, `load_module`, and `load_module_asdict`. Give them consistent secure path/stream handling, module identity, runtime registration, and imported-reference capture and restoration. Generate and interpret runtime module names consistently in session persistence and general module loading, retaining the `__runtime__` compatibility path. Internal helpers, classes, registries, and state representation are free to change.

## Entry points and restored state

Keep the public signatures and results:

- `dump_module(filename=None, module=None, refimported=False, **kwds)` saves the selected module, defaulting to `__main__`, to a path-like destination or writable stream and returns `None`. `refimported=True` requests reference preservation.
- `load_module(filename=None, module=None, **kwds)` accepts a path-like source or readable stream and an optional module object or name, including the existing `__runtime__` form. Updating `__main__` or a supplied module object returns `None`. For other targets without a supplied module object, including valid name-based targets, return the restored module.
- `load_module_asdict(filename=None, update=False, **kwds)` returns a separate restored module dictionary and records its source in `__session__`. It must not modify the caller's current module namespace. `update=False` starts from clean restored state; `update=True` includes the selected module's prior state before loading. Reject a `module` keyword with `TypeError`.

For a non-imported runtime session, `update=False` must restore a clean dictionary even when no prior runtime registration exists. This explicitly permits fixing the baseline `KeyError` in clean runtime dictionary restoration. With `update=True`, select prior state through the existing saved runtime registration; a missing registration must retain `KeyError` with the saved runtime key. When prior state exists, preserve its namespace and registration after restoration. Apart from the explicit clean-runtime correction, retain the existing error and cleanup contracts.

Retain `dump_session`, `load_session`, legacy argument aliases, default-path warnings, documented public error types, and their existing meanings. Preserve flags, sentinels, accepted path/stream forms, and return semantics without requiring new caller dependencies or flags.

For `refimported=True`, references currently recognized and saved by reference retain identity on restoration: module references match their `sys.modules` entries, and object references, including supported aliases, match their source-module attributes accessed through `sys.modules`. Do not expand the set of recognized imports or aliases.

## Security, cleanup, and failures

All three entry points reject symbolic-link paths with `OSError` and never read or write through them. `load_module` retains `ValueError` for a supplied module whose name or imported/runtime kind conflicts with the saved module, and `TypeError` for a non-module supplied value.

A non-imported runtime module loses its temporary `sys.modules` registration after successful loading or a failure after registration. Preserve the existing exception: if closing an internally opened stream raises, keep that close error and its cleanup effects, including an existing temporary runtime registration remaining present.

Caller-supplied writable streams remain open. Caller-supplied readable streams with `peek()` or working `tell()` and `seek()` also remain open. Other accepted readable streams keep their current lifecycle, including possible closure of bufferable streams that lack `peek()` and one or both of `tell()` and `seek()`. Attempt to close internally opened path streams after success or failure. Preserve close timing, close-failure effects, and exception ordering for every entry point.

## Scope

Remove the coupling without changing serialized state meaning, imported-reference identity, runtime compatibility, resource ownership, warnings, errors, or existing capabilities. Keep unrelated APIs, serialization, module loading, filesystem behavior, and dependencies unchanged. Limit modifications to necessary production code, relevant tests, and supporting adjustments; no particular algorithm or internal layout is required.

Work on a new branch from `main` and commit the completed changes.
