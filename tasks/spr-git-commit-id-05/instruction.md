# Background & Problem
The `commit-id` protocol is currently duplicated across four call sites: local commit-log parsing, GitHub GraphQL message-body matching, the reword editor helper that appends identifiers, and the in-memory git test double that fabricates log output. Each site has its own line prefix check, identifier shape, and formatting logic. The parsers also differ in what they accept:
- Local commit-log parsing enforces an eight-character lowercase hexadecimal identifier and permits optional whitespace following the prefix colon.
- GitHub GraphQL matching accepts any raw token following the prefix without hexadecimal validation or whitespace stripping.

With protocol rules spread across modules, updates require the same edits in several places, and the implementations can drift apart.

# Goals & Solutions
Consolidate `commit-id` parsing and formatting in a single shared, exported API in the `git` package:
- Centralize protocol constants, line prefix recognition, and identifier validation in `git`.
- Route local commit-log parsing and GitHub GraphQL matching through this shared capability while strictly preserving what each path accepts.
- Route the reword editor helper through the shared formatting capability, keeping emitted text byte-for-byte identical.
- Remove redundant protocol checks across consuming packages so future protocol changes require updating only the central capability.

# Scenarios & Behavior
### Scenario 1: Local Commit-Log Parsing
- **Current problem**: Custom line scanning and local regex/string trimming duplicate prefix matching and identifier validation.
- **Resolution**: Use the shared `git` capability. Preserve exact parsing rules: recognize `commit-id:` preceded by optional whitespace, permit optional whitespace after the colon, extract the first eight lowercase hexadecimal characters, and ignore any subsequent characters on the line. Retain stack ordering (bottom-of-stack first), invalidation of the full log when any identifier is missing, without returning partial commits, and the panic diagnostic following failed reword retries.

### Scenario 2: GitHub GraphQL Message-Body Matching
- **Current problem**: Ad-hoc string slicing parses message bodies independently from local git log routines.
- **Resolution**: Route message scanning through the shared capability while keeping its relaxed parsing rules: capture verbatim whatever string follows the first colon up to the next colon or newline, without enforcing hex validation or whitespace rules. Retain branch matching, pull-request ordering, and field population for `CommitHash`, `Subject`, and `Body`. Preserve the existing empty-result behavior: return a non-nil empty pull-request slice when the local stack is empty or the GraphQL nodes pointer is nil; when the local stack is non-empty and the nodes pointer is non-nil but no pull request matches, return a nil pull-request slice.

### Scenario 3: Reword Editor Helper
- **Current problem**: Hardcoded string concatenation appends protocol lines directly in the helper script.
- **Resolution**: Use the shared formatting capability to build the appended line. Retain editor-helper semantics: append `commit-id:<8-lowercase-hex>` on its own line only to non-empty messages lacking an identifier, preserve the trailing newline on single-line messages, leave existing or empty files untouched, and rewrite only relevant rebase-todo `pick` lines to `reword`.

### Scenario 4: In-Memory Git Test Double
- **Current problem**: The test double independently formats commit messages and log outputs.
- **Resolution**: Emit log lines using the shared protocol definitions, keeping fabricated log output byte-identical, including tab indentation and surrounding blank lines.

# Public Contract to Preserve
Exported types, signatures, and fields must remain unchanged:
- `git.Commit`: Retain public fields `CommitID`, `CommitHash`, `Subject`, `Body`, and `WIP` with identical types, zero values, and semantics.
- `git.GetLocalCommitStack`: Retain signature `(cfg *config.Config, gitcmd GitInterface) []Commit`, returning unmerged commits bottom-of-stack first.
- `git.GetLocalTopCommit`: Retain signature and return the top unmerged commit, or `nil` for an empty stack.
- `git.BranchNameRegex`: Retain signature `(branchPrefix string)` matching `<prefix>/<branch>/<8-hex-id>` with the identifier in the second capture group.
- `github.GetInfo`: Retain signature `(ctx context.Context, gitcmd git.GitInterface) *github.GitHubInfo`, returning pull requests with `FromBranch`, `ToBranch`, `Commit`, `Commits`, and `MergeStatus` populated as before.
- **New Shared Capability**: Must be exported from package `git` to support external callers, while internal helper names and file layouts remain flexible.

# Invariable Behavior
- **Local Parsing Fidelity**: Preserve extraction of 40-character commit hashes, subject/body trimming, and the `WIP` prefix flag. Reject partial logs when any commit lacks an identifier; preserve the diagnostic panic on unresolved rewords.
- **GraphQL Parser Tolerance**: Do not apply the stricter eight-hex rule or whitespace stripping to GraphQL message bodies; preserve field mappings for `CommitHash`, `Subject`, and `Body`.
- **Reword Helper Mechanics**: Append lines only when non-comment content exists and no `commit-id:` line is present. Preserve the extra newline for single-line inputs and maintain rebase-todo line transformations.
- **Test Double Compatibility**: Maintain byte-identical output formatting for tab-indented subject/identifier lines and spacing.

# Constraints
1. The `commit-id` wire format MUST NOT change: retain the `commit-id:` prefix, eight-lowercase-hex format for generated identifiers, line placement, and exact emitted text.
2. The two parsing paths MUST maintain their distinct tolerances; the shared capability must not impose strict log rules on GraphQL bodies or loose GraphQL rules on commit logs.
3. Do not remove, rename, or narrow existing public capabilities, and do not introduce new module dependencies, CLI commands, or configuration options.
4. Restrict code modifications strictly to the production code and tests necessary for this consolidation, without unrelated refactoring or formatting changes.
5. Work on this in a new branch from main and commit everything when you are done.
