# Separate shell completion rendering from the command

The `completions` command mixes shell selection with three parallel renderers that repeat application traversal, naming, alias assembly, and template substitution. Give each shell's generation behavior a cohesive, independently replaceable responsibility outside the command. Define the shell-independent work once: script path/name resolution, completion function naming, aliases, command and option traversal, and template filling. The command should only resolve and validate the shell, select its generator, write the result, and return success. Internal dispatch keys, helpers, templates, and module layout are yours to choose.

Keep the command registered as `completions`, with the optional positional `shell` argument and repeatable value-taking `--alias` option unchanged. Support `bash`, `zsh`, and `fish`. An explicit shell takes precedence; otherwise use only the final path component of `SHELL`. An absent or empty usable shell raises `RuntimeError` rather than choosing a default. An unsupported shell raises `ValueError` naming all three supported shells and emits no script output.

For the same application, command set, and script-name inputs, each generated script must remain character-for-character identical, including whitespace, completion function names, aliases, and placeholder substitutions. Preserve traversal ordering and inclusion: skip hidden, disabled, and unnamed commands; retain namespaced-command quoting and namespace handling, and option sorting and escaping. Repeated aliases keep their current effect; omitting the option does not alter the output.

Successful generation writes only to the command output stream, exits with status 0, and makes no filesystem changes. Preserve the existing application initialization and lazy-command materialization performed by command traversal, without introducing additional application-state mutations.

Completion requires shell behavior to be separate from command orchestration and common work to replace the three copies, with focused tests supporting the preserved scripts, inputs, resolution order, and failures. Do not add dependencies, configuration, or caching/lazy evaluation that changes script production. Limit edits to generation, selection, directly relevant tests, and small supporting changes such as template relocation; leave unrelated commands, application wiring, and shared formatting untouched.

Work in a new branch from `main` and commit the completed changes.
