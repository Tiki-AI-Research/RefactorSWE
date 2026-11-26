## Background
The Go setup action restores a dependency cache before installation and saves it in a post step. The two flows independently rediscover the same information: each resolves the package manager configuration, asks the Go toolchain where the cache folders live, and then applies its own rules for folders missing from disk. The primary key linking both steps is derived during restore and later re-read from action state during save, so key derivation, state writes, and output writes are implicit cross-step contracts rather than one owned responsibility. This duplication lets the flows drift. Consolidate discovery, validation, key, and state handling behind one cohesive cache context that both flows consume, without changing what a user or the cache service observes.

## Goal
- Consolidate package manager resolution, cache folder discovery, on-disk existence reporting, primary key derivation, and cache state reads and writes into one cohesive cache context, removing the two parallel discovery implementations.
- Let restore obtain its cache paths and primary key from that shared context while publishing the cache hit result with the same timing and values as today.
- Let save obtain the same paths and existence information from that shared context while applying its existing early-exit decisions and log messages.
- Let the calling wiring pass the cache context once instead of rebuilding the package manager selection and repeating the discovery sequence.
- Keep the internal shape free: representation, naming, helper decomposition, and whether former standalone discovery helpers stay exposed are implementation choices.

## Public contract to preserve
- Keep the action inputs `cache` (boolean, default true) and `cache-dependency-path` (optional), and the `cache-hit` output holding the boolean hit result, with unchanged names, types, and meanings.
- Keep the cross-step state names `CACHE_KEY` and `CACHE_RESULT`, and keep the restore entry point accepting a version specification, a package manager selection, and an optional dependency file path, resolving to a completed promise with no meaningful return value.
- Keep the save entry point accepting its optional early-exit flag so the post step can terminate right after a successful save decision, and keep it resolving without failing the workflow on cache errors.
- Keep package manager resolution accepting a package manager name and yielding its dependency file pattern and cache folder command list, rejecting unknown names with the existing message.
- Keep cache folder discovery accepting that package manager information and yielding a non-empty array of folder paths, discarding failed commands, and throwing `Could not get cache folder paths.` when none resolve.
- Keep the primary key assembled in exactly this order: the literal `setup-go-`, the platform, `-`, the architecture, `-`, the Linux-only `ImageOS-` component, `go-`, the version specification, `-`, and the dependency file hash; the `ImageOS-` component appears on Linux only.
- Keep all existing user-visible error and log texts, including dependency file failures and save early-exit messages.
- Internal helpers for dependency file location, path filtering, and warning emission may be reorganized, renamed, or absorbed into the context.

## Behavior that must stay unchanged
- MUST pass the unfiltered discovered path list to the cache service on both restore and save; existence filtering MUST NOT change that list and MUST only drive the save flow's missing-path warning and its early exit when no folder exists on disk.
- MUST NOT perform local existence checks on the discovered cache folders during restore; on-disk existence reporting is a save-only concern. Dependency-file lookup and hashing during restore are unaffected.
- MUST write `CACHE_KEY` before requesting a restore, MUST write `CACHE_RESULT` only when restore returns a non-empty key, and MUST NOT write it on a miss.
- MUST output `cache-hit` false with `Cache is not found` on a miss, and true with the restored key on a hit, on both paths.
- MUST derive the primary key exactly as specified, including the Linux-only `ImageOS-` component, so restore and save agree across steps.
- MUST keep primary-key calculation free of action-reporting side effects: shared cache metadata and state access must not emit the primary-key diagnostic. Restore emits that diagnostic when consuming the calculated key, preserving its existing text and timing. Discovery command-failure diagnostics remain unchanged.
- MUST preserve every save early exit and its log text: disabled cache input, all folders missing with `There are no cache folders on the disk`, missing primary key, primary key equal to the matched key, a save returning `-1`, and a save throwing all leave the workflow successful with the existing messages.
- MUST warn about partially missing folders while still passing the complete list to the cache service, and MUST NOT skip saving because of a partial miss.
- MUST treat primary-key state retrieval as a prerequisite for restore-match metadata during save: if retrieving the primary key fails, report that failure through the existing non-fatal warning path, without reading matched-key state or calling the cache service. A secondary metadata failure must not mask the primary failure.
- MUST keep throwing `Some specified paths were not resolved, unable to cache dependencies.` when hashing yields nothing, and the existing missing dependency file error naming the workspace and supported pattern when the default dependency file is absent.

## constraints
1. Do not change action inputs, outputs, state keys, key format, user-visible messages, or what is handed to the cache service.
2. Do not remove or reduce capabilities: package manager resolution, partial-failure-tolerant discovery with its total-failure error, dependency hashing failures, and every save early exit must remain independently observable.
3. Do not add runtime dependencies or change build and packaging configuration to achieve the consolidation.
4. Do not refactor installation, version resolution, problem matchers, or path setup; keep the change centered on cache discovery, validation, key, and state responsibilities.
5. Keep internal structure and naming unconstrained; any representation is acceptable while the contract and unfiltered-path invariant hold.
6. Limit edits to the production cache code, the wiring that invokes it, and the tests or generated artifacts required by those changes; touch no unrelated files.

IMPORTANT: Please work on this in a new branch from main and commit everything when you are done.