# Consolidate frontmatter note operations

Give note identity and already-loaded contents one operation abstraction exposing print, edit, and delete. Replace overlapping parameter bundles and boolean dispatch inside individual operation paths, and centralize content transformation shared by key setting/deletion. Keep command-level selection flags and precedence; private operation shape, handlers, and helpers are yours to choose without requiring new public API.

Keep frontmatter/fm with exactly one note argument and print/-p, edit/-e, delete/-d, key/-k, value, and vault/-v flags. `actions.Frontmatter` retains vault-manager/note-manager/FrontmatterParams inputs and `(string,error)`; params retain note, selections, key, and value. The pkg/frontmatter Parse/Format/HasFrontmatter/SetKey/DeleteKey functions and Delimiter/NoFrontmatterError/InvalidFrontmatterError stay exported with current signatures and effects.

Resolve the default vault name, vault path, and note contents before returning `no operation specified: use --print, --edit, or --delete`. Multiple flags retain print→edit→delete priority. Resolution, read, parse, and write failures propagate rather than being masked by operation errors.

Print returns only formatted YAML, never the body, without writing; absent/empty frontmatter is empty success, malformed frontmatter an error. Edit rejects empty key with `--key is required for edit operation` and empty value with `--value is required for edit operation`, without writing. Delete rejects empty key with `--key is required for delete operation` and missing frontmatter or a parsed nil frontmatter map with `note does not contain frontmatter`, without writing. Preserve the existing nonnil empty-map case: deletion succeeds, returns the body with one leading newline removed, and the action writes it once. Successful edit/delete writes exactly once via the note manager and retains success text beginning `Updated frontmatter key`/`Deleted frontmatter key`, naming key and note.

Key setting creates delimiters if needed and preserves the body. Preserve boolean conversion of true/false, bracketed comma-separated sequences, empty sequence for empty brackets, and strings otherwise. Deletion preserves remaining keys/body; removing the final key returns only the body with its leading newline removed. Reconstruct unchanged bytes with opening delimiter, YAML, closing delimiter, then body. Keep formatting, error precedence, wording, and write effects.

Completion requires owned operation context, explicit capabilities, and one content transformation implementation, with directly affected tests/documentation. Add no dependencies or unrelated commands/flags/features. Limit production changes to frontmatter consolidation and direct support, without unrelated refactoring.

Work in a new branch from `main` and commit the completed changes.
