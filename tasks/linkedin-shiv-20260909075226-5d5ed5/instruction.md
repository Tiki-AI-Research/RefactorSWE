# Refactor CLI Build Orchestration, Cache Materialization, and Runtime Dispatch

## Background
`shiv` packages Python applications into standalone zipapps and manages their unpacking and execution at runtime. Currently, three core responsibilities suffer from tight coupling:

1. CLI build orchestration in `shiv.cli`: Option validation, dependency staging, build metadata assembly, and final zipapp emission are intertwined within a single linear procedure. Because build preparation is not isolated from archive generation, build preparation cannot be driven or evaluated as a distinct stage prior to archive emission.
2. Runtime cache materialization in `shiv.bootstrap`: Cache directory evaluation, synchronization across concurrent processes, extraction of archived dependencies, permission restoration, bytecode compilation, and cache directory placement are intermixed procedurally in module-level helpers. The materialization workflow lacks a dedicated lifecycle responsibility boundary.
3. Runtime execution dispatch across `shiv.bootstrap` and `shiv.bootstrap.interpreter`: Selecting the runtime target, evaluating preamble execution, invoking configured entry points or console scripts, and falling back to Python interpreter modes are directly coupled with process execution and environment mutation. Execution intent cannot be formulated or evaluated separately from immediate invocation.

These areas need structural refactoring to establish clean separation of concerns while preserving all existing CLI behavior, environment variable contracts, and zipapp runtime semantics.

## Goal
Restructure the build orchestration, cache materialization, and runtime dispatch logic into explicit architectural boundaries:

1. CLI Build Orchestration (Split Phase): Separate build preparation from archive emission into two distinct, sequential phases. The preparation phase must handle dependency collection, staging, and build metadata setup, producing an explicit intermediate representation of the build. The emission phase must consume that intermediate representation to write the final executable zipapp archive.
2. Cache Materialization Lifecycle (Extract Class): Encapsulate the end-to-end cache materialization lifecycle into a dedicated responsibility boundary rather than procedural forwarding functions. This component must manage cache path evaluation, materialization synchronization, extraction of packaged site-packages, file permission restoration, optional bytecode compilation, and final cache directory placement.
3. Runtime Execution Dispatch (Function <-> Command): Decouple runtime target selection from target execution. Evaluating configuration, preamble requirements, entry points, and interpreter fallback options must produce an independently representable execution request, separating the decision of what to execute from the concrete execution and handoff steps.

## Public contract to preserve
The following external interfaces and configurations must remain strictly backward-compatible:

1. CLI Command-Line Interface:
   - All supported CLI options, arguments, flags (such as entry-point configuration, output target, python interpreter specification, site-packages overrides, preamble scripts, and pass-through pip arguments after `--`), defaults, argument parsing semantics, and exit codes must remain fully compatible.
   - The CLI acceptance, help text, persisted configuration, and runtime target dispatch behavior must remain fully preserved across all combinations of entry-point flags: when `--entry-point` is supplied alone, when `--console-script` is supplied alone, when both are supplied, and when neither is supplied (allowing fallback to interpreter execution). Preserve the historical help wording “entry point takes precedence” as help text. At runtime, when both fields are configured, the console script is selected; an entry point alone selects the callable. These are distinct historical behaviors and must not be reconciled by changing either surface.
   - Existing CLI failure behavior must remain compatible, including existing failure conditions, error messages, output streams, and exit behavior for scenarios such as missing dependency inputs, missing output paths, disallowed pip arguments, and unresolved console scripts. No new errors or failure conditions may be introduced.
2. Runtime Environment Variables:
   - `SHIV_ROOT`: Overrides the base cache directory used for extracting zipapp dependencies.
   - `SHIV_FORCE_EXTRACT`: Forces re-extraction of bundled dependencies when resolving to a true value according to existing boolean resolution semantics.
   - `SHIV_INTERPRETER`: Overrides the configured application entry point, forcing interpreter handling instead.
   - All other existing SHIV_* settings and their boolean/value resolution, metadata defaults, and environment scrubbing remain compatible; the three variables above are examples, not an exhaustive list.
3. Archive Output Properties:
   - Generated zipapps must retain their configured shebang lines, executable file permissions, exposed build metadata, compression behavior, and runtime compatibility.
4. Runtime Compatibility Entry Points:
   - Existing callable entry points for directly invoking interpreter handling must remain importable from their original public module locations. Calling them must execute the selected invocation and preserve argument handling, errors, standard streams, and exit-code propagation.

## Behavior that must stay unchanged
1. Build Preparation and Archive Emission:
   - Dependency preparation (pip installation into a transient environment or copying an existing site-packages directory) and initial build metadata setup must finish before archive emission begins. The default build_id is computed while site-packages are written into the archive, and is then persisted in environment.json; it need not exist before archive creation starts.
   - A failure during build preparation must halt the workflow, must not proceed to archive emission, and must not create or overwrite the target archive as part of that failed attempt.
2. Cache Materialization Semantics:
   - When a target cache directory already exists and `SHIV_FORCE_EXTRACT` does not resolve to true, extraction, permission adjustments, and compilation must be bypassed.
   - Competing processes attempting to materialize the same cache must be serialized to avoid corrupted extractions.
   - Forced extractions and initial materializations must continue to unpack archived site-packages, restore preserved file permissions, conditionally compile bytecode when requested, and update the cache directory following existing semantics.
3. Runtime Execution and Handoff Semantics:
   - Any configured preamble script must run prior to primary application or interpreter target execution. Runtime target overrides changed by a Python preamble must affect the primary target according to their existing semantics; in particular, a nonempty `SHIV_INTERPRETER` value forces interpreter handling, including values such as `false` and `0`, while an unset or empty value does not.
   - Direct callable entry points, console scripts, interpreter execution modes (`-c`, `-m`, script paths, standard input, and interactive sessions), and application handoffs must preserve their existing execution behavior, exit code propagation, argument handling, standard streams, and environment scrubbing where applicable.

## constraints
1. No Behavioral Regressions:
   - Do not alter CLI option names, default values, or error exit codes.
   - Do not break existing metadata exposure, build identity, archive executability, or runtime compatibility contracts.
2. Refactoring Boundary Requirements:
   - Build preparation and emission must have an explicit handoff: a preparation result containing the staged inputs and resolved build configuration can be obtained before archive writing; emission must consume that result. A preparation failure must leave the output absent or unchanged. No particular class or function name is required.
   - Cache materialization must have an active lifecycle boundary used by both the compatibility extraction helper and production bootstrap. It must evaluate the cache path and coordinate synchronization, extraction, permissions, optional compilation, and placement. Cooperating objects and focused helpers may implement these steps and receive paths from the lifecycle. An unused class or a wrapper that sends the complete workflow back to the old procedural monolith does not establish this boundary. Production bootstrap must delegate cache path evaluation to this boundary rather than compute the final cache target outside it.
   - Runtime selection must return an inspectable execution request before target execution. Selection must leave application, interpreter, and preamble execution deferred; the returned request must be used by the real runtime path. The request may expose executable behavior (for example an execute/run method or a callable), or contain data consumed by a separate executor. In either design, execution must consume the returned request after selection returns; merely constructing an unused request does not establish this boundary. Preamble execution must still precede the selected primary target. No particular class or selector name is required.
   - For command-string and module interpreter execution, the primary target request must retain the selected mode and arguments: changing the ambient process argument vector after primary selection returns must not change the target or arguments executed from that request. Primary selection may occur after a preamble so that the preamble's runtime configuration changes still take effect. No particular request representation is required.
   - A selected Python preamble request must retain its invocation context: changing the ambient process argument vector after preamble selection returns must not change the archive identifier supplied to that preamble. Its site-packages context and runtime environment object must remain available, and the environment must retain its existing mutability and override behavior.
   - A primary interpreter request must represent a complete invocation. If the required command-content or module-name operand is omitted, primary selection must raise the existing missing-operand error before returning an execution request. Validation must not execute the primary target; configured preambles retain their existing ordering before primary selection.
3. Implementation and Scope Constraints:
   - Do not introduce new external runtime dependencies.
   - Do not introduce additional refactoring targets beyond CLI build orchestration, cache materialization lifecycle, and runtime execution dispatch.
   - Candidate changes must be limited to `src/shiv/**`.
   - Candidate must not create, modify, rename, or delete tests or testing configuration. Existing tests and test configuration may be read and executed for validation.

IMPORTANT: Please work on this in a new branch from main and commit everything when you are done.
