# Share dimension evaluation between label quantifiers

Label matching repeats the same three dimension branches in both `any` and `all`. Each quantifier also decides how those dimensions are evaluated, so adding a dimension requires parallel changes and makes evaluation order and empty-input behavior harder to follow.

Define the quantifier semantics once and let each optional dimension use one common evaluation contract. Make the supported dimension set explicit and extensible, so a new dimension does not require editing both quantifiers. Preserve configuration normalization and determine whether a dimension is present from its configuration key, as today. Internal names, modules, types, and dispatch mechanisms are yours to choose.

## Configuration and matching

Keep the existing `any` and `all` arrays. Each entry may combine `base-branch`, `changed-files`, and `head-branch`; branch patterns still accept strings or arrays and normalize to arrays. The changed-files modes remain `any-glob-to-any-file`, `any-glob-to-all-files`, `all-globs-to-any-file`, and `all-globs-to-all-files`. Their string values normalize to one-element arrays, unknown changed-files keys are rejected, and invalid shapes retain their current errors. At other normalization levels, unknown keys continue to be ignored wherever they are ignored today. The same valid input produces equal match objects, with unchanged `any`/`all` meaning and precedence.

The matching entry point still takes changed-file paths, parsed match configurations, and `dot`, and returns a boolean. Preserve these quantifier boundaries:

- `any` passes when some non-empty entry has a matching present dimension. An empty block, a block of empty entries, or no matching present dimension returns false.
- `all` passes only when every non-empty entry and every present dimension matches. An empty block, a block of empty entries, or any failing present dimension returns false.
- If a configuration has both blocks, both must pass. Every configuration in the list must match for the overall result to be true.

Within an entry, evaluate base branch, then changed files, then head branch, retaining short-circuiting and debug-output order. A present changed-files dimension in an `all` block returns false for an empty file list before evaluating file patterns. Missing branch context makes that dimension fail without throwing.

## Action behavior and scope

`dot` keeps controlling leading-dot files: a plain glob does not match them when disabled and does when enabled. Preserve `sync-labels`, `max-files-changed`, and `changed-files-labels-limit`, together with the names and contents of `new-labels` and `all-labels`. When the changed-file count exceeds the maximum, branch-only labels still apply; labels using non-empty changed-files patterns are skipped or preserved according to the existing `sync-labels` behavior. Keep label removal and changed-file label limits unchanged.

The work is complete when matching orchestration shares the quantifier and dimension contract without changing accepted payloads, normalization results, matching outcomes, debug ordering, label application, or any public name or result shape. Retain both quantifiers, all three dimensions, and all four changed-files modes.

Limit edits to necessary matching orchestration, dimension adapters, minimum public type or constant exposure for dimension keys, corresponding tests, and directly required documentation. Add no runtime dependencies, broaden no action permissions, and do not change external protocols or packaging. Leave workflows, build and release files untouched unless strictly required by this refactor; avoid unrelated renames, formatting, or behavior changes.

Work on a new branch from `main` and commit the completed changes.
