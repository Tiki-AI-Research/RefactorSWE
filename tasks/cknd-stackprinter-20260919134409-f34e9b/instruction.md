# Refactor stackprinter: Decouple Configuration, Formatting, Styling, and Tracing

## Goal

Refactor the `stackprinter` package to decompose its monolithic exception and stack formatting pipelines into clean, cohesive, and testable architectural components, strictly preserving existing public APIs, observable output formats, and error-handling semantics (except for the required changes listed in the table below).

The refactored design must introduce:
1. Centralized configuration management with validation and immutability (`stackprinter.config.FormatConfig`).
2. A polymorphic styling hierarchy (`stackprinter.styling.Styler`, `PlaintextStyler`, `AnsiStyler`, `get_styler`).
3. An isolated exception renderer (`stackprinter.formatting.ExceptionRenderer`).
4. An isolated thread stack formatter (`stackprinter.formatting.ThreadStackFormatter`).
5. An isolated execution trace event formatter (`stackprinter.tracing.TraceEventFormatter`).
6. A backward-compatible, private internal parameter routing mechanism (`_config`), keeping the public API surface clean.
7. A refactoring manifest (`REFACTORING.md`) documenting architectural responsibilities, migration paths, and component boundaries.

### Workflows and Acceptance Boundaries

1. **Workflow A: Structural Refactoring (Preserving Existing Behavior)**:
   - Decompose monolithic formatting and inspection logic into isolated, cohesive components (`FormatConfig`, `Styler`, `PlaintextStyler`, `AnsiStyler`, `ExceptionRenderer`, `ThreadStackFormatter`, `TraceEventFormatter`).
   - Maintain 100% byte-for-byte and semantic parity with pre-refactor baseline formatting across all standard exception, frame, thread, and trace outputs when default or legacy options are used.

2. **Workflow B: Deliberate Functional Extensions and New Behaviors**:
   - Implement intentional extensions including palette aliases, deterministic missing-frame text, extended option acceptance, frame budget truncation (`max_frames`), line prefix indentation (`indent`), and private configuration routing (`_config`).

3. **Workflow C: Compatibility, Exceptions, and Early Return Precedence**:
   - Baseline error semantics: invalid target types, unknown kwargs, or illegal option combinations preserve baseline rejection rules (e.g. `BaseException` instance targets raise `ValueError`; unknown kwargs on frame/thread/current-stack targets are rejected).
   - Traceback-free exception targets: targets where `exc.__traceback__ is None` unconditionally return plain text `"<Type>: <msg>"` directly without validating ordinary formatting options (unknown kwargs, styling options, and option values) or applying ANSI styles. The reserved `config=` rejection and the `_config` type check still run first; see "Validation order".
   - Silent stderr: invoking `show(exc)` with default `'stderr'` when `sys.stderr is None` returns `None` silently before checking parameters.

### Requirement Groups and Acceptance Boundaries

| Requirement ID | Workflow | Acceptance boundary |
| :---: | :---: | :--- |
| A1 | Workflow A | `FormatConfig` encapsulates every formatting option listed in Architectural Requirements |
| A2 | Workflow A | Public exception entry points delegate to `ExceptionRenderer` and return its rendered output directly |
| A3 | Workflow A | Public thread entry points delegate to `ThreadStackFormatter` and return its formatted output directly |
| A4 | Workflow A | Tracing facilities delegate event formatting to `TraceEventFormatter` |
| A5 | Workflow A | `FrameFormatter` accepts and applies `FormatConfig` and renders frames through the active `Styler` |
| A6 | Workflow A | `REFACTORING.md` documents 7 architectural classes, responsibilities, and migration steps |
| B1 | Workflow B | `get_styler('dark')` renders identical ANSI output to `get_styler('darkbg')`; same for `'light'`→`'lightbg'`, `True`→`'color'` |
| B2 | Workflow B | Stylers satisfy `format_exception_message` and ANSI frame styling contracts |
| B3 | Workflow B | Threads with missing frame mappings deterministically return `"%r: no frames found" % thread` |
| B4 | Workflow B | `max_frames=N` truncates stack blocks to innermost `N` frames with trailing marker `    ... (<k> frames omitted)` |
| B5 | Workflow B | `indent=str` prefixes every non-empty formatted line across all targets |
| B6 | Workflow B | Public entry points accept private configuration instances, with explicit kwargs overriding configuration values |
| C1 | Workflow C | Exception target without traceback returns `"<Type>: <msg>"` before ordinary formatting-option validation; the reserved `config=` rejection and the `_config` type check still take precedence |
| C2 | Workflow C | `show(exc)` with default `'stderr'` and `sys.stderr is None` silently returns `None` before parameter checking |
| C3 | Workflow C | Non-`Exception` `BaseException` instance targets raise `ValueError`; unknown kwargs and illegal options are rejected |

---

## Architectural Requirements

1. **Configuration Centralization (`stackprinter.config`)**:
   - Establish `stackprinter.config.FormatConfig` as an immutable (or property-guarded) configuration container. After initialization, any attribute assignment (including writing to non-existent fields and to any internal attributes used to implement immutability) must raise `AttributeError`.
   - Encapsulate all formatting options: `style`, `source_lines`, `source_lines_after`, `show_signature`, `show_vals`, `truncate_vals`, `line_wrap`, `suppressed_paths`, `suppressed_vars`, `suppressed_exceptions`, `reverse`, `add_summary`, `max_frames`, and `indent`.
   - Validate options on initialization: when validation fails, raise `ValueError` with message `source_lines must be an integer or 'all', was %r` where `%r` is the original supplied value. Do not add any extra range checks (including `>= 0`), preserving baseline validation conditions; `show_vals` must be one of its supported modes or boolean/None.
   - Store `suppressed_paths`, `suppressed_vars`, and `suppressed_exceptions` as `list` objects: each non-`None` value supplied by the caller is copied into a new `list` owned by that `FormatConfig` instance. `None` values remain `None`. Do not convert these collections to tuples or any other sequence type, and do not retain the caller's original collection object.
   - `FormatConfig.with_overrides(**kwargs) -> FormatConfig` must return a new instance. Every `list`-typed collection field on the returned instance must be an independent copy: for each of `suppressed_paths`, `suppressed_vars`, and `suppressed_exceptions`, `new_cfg.<field> is not old_cfg.<field>` must hold whenever both fields are non-`None`, even when the two lists have equal contents.

2. **Polymorphic Styling Hierarchy (`stackprinter.styling`)**:
   - Define an abstract `Styler` base class exposing styling methods for headings, line numbers, variable values, source code, and exception messages.
   - Implement `PlaintextStyler(Styler)`: outputs pure uncolored text strictly devoid of ANSI escape codes (`[`).
   - Implement `AnsiStyler(Styler)`: outputs ANSI color-coded text across supported color palettes (`darkbg`, `darkbg2`, `darkbg3`, `lightbg`, `lightbg2`, `lightbg3`, `color`).
   - Implement `get_styler(style, ...)` resolving style names and aliases to `Styler` instances:
     - Plain-text aliases: `'plaintext'`, `'plain'`, `'none'`, `None`, `False`, `''` map to `PlaintextStyler`.
     - ANSI aliases: `'dark'` maps to `'darkbg'`, `'light'` maps to `'lightbg'`, and `True` maps to `'color'`.
   - Stylers must implement `format_exception_message(cls, exc, tb)` returning the formatted exception message string according to the active style.

3. **Exception Rendering Decomposition (`stackprinter.formatting`)**:
   - Establish `stackprinter.formatting.ExceptionRenderer(cfg)` taking a `FormatConfig` instance and exposing `render(cls, exc, tb) -> str` to format exception chains, frame blocks, and summary headers.
   - Public exception entry points must obtain exception output by delegating to `ExceptionRenderer.render(...)`.
   - *Architecture Rationale*: This delegation relationship is a core architectural deliverable of this task, establishing a single source of truth for exception chain traversal and frame block assembly, and eliminating redundant formatting paths across exception entry points.

4. **Thread Stack Formatting Decomposition (`stackprinter.formatting`)**:
   - Establish `stackprinter.formatting.ThreadStackFormatter(cfg)` taking a `FormatConfig` instance and exposing `format_thread(thread) -> str` to format thread inspection frames.
   - Public thread entry points must obtain thread output by delegating to `ThreadStackFormatter.format_thread(...)`.
   - *Architecture Rationale*: This delegation ensures that thread inspection, thread name extraction, and thread stack indentation are centralized in a single testable formatter, decoupling thread-specific logic from generic formatting entry points.

5. **Internal Parameter Routing vs. Public API Protection**:
   - Public entry points accept `_config`; for routing rules, merging behavior, and error handling, see the "Entry points, options, and error handling" section.
   - The public entry points must NOT expose `config` as a public parameter name; passing `config=` to any public entry point must raise `TypeError` across all states and targets.
   - Routable entry points include `stackprinter.format`, `stackprinter.show`, `format_current_stack`, `show_current_stack`, `format_current_exception`, `show_current_exception`, `TracePrinter`, and `trace`.

6. **Refactoring Trajectory Record**:
   - Produce a refactoring trajectory record / manifest in the repository, such as `REFACTORING.md` (including a fenced code example in its migration section), documenting the responsibilities of `stackprinter.config`, `stackprinter.styling`, `stackprinter.formatting`, `stackprinter.frame_formatting`, and `stackprinter.tracing`.
   - The manifest must name all 7 core architectural classes: `FormatConfig`, `Styler`, `PlaintextStyler`, `AnsiStyler`, `ExceptionRenderer`, `ThreadStackFormatter`, and `TraceEventFormatter`.
   - Simply listing class names without descriptions is insufficient: each required class must include a responsibility description (in the same paragraph or table row).
   - Document `_config`, backward compatibility, and a progressive migration path.
   - The manifest must contain a section titled `Migration Capabilities & Integration Guidance` (case-insensitive) outlining caller migration guidance with an ordered list of at least 3 migration steps. The migration guidance must include at least one concrete multi-line code example (wrapped in Markdown code fences ```) demonstrating how to migrate from legacy calls to the new entry point.
   - *Architecture Rationale*: The structured manifest section titles and component definitions act as machine-verifiable architectural anchors for downstream tools, automated test fixtures, and team integration verification.

7. **Tracing Decomposition (`stackprinter.tracing`)**:
   - Establish `stackprinter.tracing.TraceEventFormatter(cfg)` taking a `FormatConfig` instance and exposing `format_event(event) -> str`, which produces the emitted text for a single trace event (call events, return events, and the exception trace note); the event payload shape is an internal implementation detail.
   - `TracePrinter` (and therefore `@trace`) must obtain every emitted event string by delegating to a `TraceEventFormatter` instance; the same instance may be reused for the lifetime of the printer.
   - `TracePrinter` and `trace` must accept the private `_config` keyword argument described in item 5 and use it to build both the event formatter and the `Styler`; the public `style` option continues to behave as before.
   - Observable event text, hierarchical indentation, `depth_limit` filtering, `print_function` usage, and `stop_on_exception` behaviour must remain unchanged.
   - *Architecture Rationale*: Delegating event formatting to `TraceEventFormatter` decouples execution tracing hooks and stack depth inspection from text formatting and ANSI styling, ensuring consistent event styling across the trace lifecycle.

8. **Frame Formatter Configuration and Styling (`stackprinter.frame_formatting`)**:
   - `stackprinter.frame_formatting.FrameFormatter` must accept an optional `FormatConfig` instance as its first positional constructor argument (`FrameFormatter(cfg)`), must keep accepting its existing keyword options, and must render frames through the `Styler` taken from that configuration.
   - `FrameFormatter(FormatConfig(style='darkbg'))(frame, lineno=None)` must produce ANSI output, `FrameFormatter(FormatConfig(style='plaintext'))(frame, lineno=None)` must produce output containing no ANSI escape sequences, and `FrameFormatter()(frame, lineno=None)` must keep working.
   - `ColorfulFrameFormatter` must remain available as the ANSI-configured counterpart and must produce the same text as `FrameFormatter(FormatConfig(style=<ansi style>))`.

9. **Stack Frame Budget (`max_frames`)**:
   - `FormatConfig` gains `max_frames` (default `None`). Valid values are `None` or an `int` `>= 1`; any other value raises
     `ValueError` with the exact message `max_frames must be a positive integer or None, was %r` (`%r` is the original value),
     both on initialization and from `with_overrides`.
   - `max_frames` is a public keyword option for exception, frame, thread, current-stack and current-exception targets, and is
     therefore also accepted by `show`, `show_current_stack` and `show_current_exception`. Like every other option it is routed
     through `_config`, and an explicitly passed keyword argument overrides the value carried by `_config`.
   - When `max_frames` is an integer `N`, each rendered stack block keeps only the innermost `N` frames and replaces the dropped
     outermost frames with exactly one marker line, emitted as the **final line** of that rendered block
       (i.e. after that block's exception message line, when the block has one):
     `    ... (<k> frames omitted)` where `<k>` is the number of dropped frames (four leading spaces, exact wording).
   - Budgets are per stack block: every exception in a chain and every thread stack has its own budget of `N`. ExceptionGroup targets use the standard-library fallback described in "Behavior to preserve" item 3 and are exempt from `max_frames`; their member frames are not individually budgeted.
   - When a block has at most `N` frames, no marker line is emitted.
   - The marker is not affected by `reverse` or `add_summary`: it is always the last line of its own block, after the block's exception message line if present.
   - `TracePrinter` and `trace` are unaffected; `depth_limit` continues to control tracing depth only.

10. **Line Prefix Indentation (`indent`)**:
    - `FormatConfig` accepts `indent`, a `str` with default `''`. `None` is normalized to `''`. Any other type raises `ValueError` with the exact message `indent must be a string, was %r`, where `%r` is the supplied value; `FormatConfig(...)` and every entry point that accepts `indent=` explicitly must raise that error for invalid values on frame, thread, current-stack, current-exception and tracing targets.
    - Every non-empty line of the rendered output is prefixed exactly once with `indent`. Empty lines stay empty and must not carry trailing whitespace.
    - The prefix applies to exception output (including chained causes, context hints, summaries, the `---- (full traceback ...) ----` separator, and frame-budget omission lines), single-frame output, thread output (including the headline and the `"%r: no frames found" % thread` boundary line), current-stack output, `show()` / `show_current_stack()` / `show_current_exception()` output, and every line emitted by `TracePrinter` / `@trace`, including the depth connector lines.
    - Exactly one prefix per line. An entry point delegating to `ExceptionRenderer`, `ThreadStackFormatter`, `FrameFormatter` or `TraceEventFormatter` must not double the prefix. `ExceptionRenderer(config).render(...)` must equal `stackprinter.format(exc, _config=config)` and `ThreadStackFormatter(config).format_thread(thread)` must equal `stackprinter.format(thread, _config=config)` for the same config.
    - `line_wrap` keeps its current meaning and applies to the line content; the prefix is prepended after wrapping and does not count toward the wrap width.
    - With the default `indent=''`, every existing output stays byte-identical.

---

## Required behavior changes relative to the pre-refactor baseline

The refactored implementation introduces several deliberate behavioral improvements and extensions over the pre-refactor baseline. Each item below takes precedence over any general statement regarding preserving historical error semantics or output formats:

| Affected input / Area | Baseline observable behavior | Required post-refactor behavior | Precedence / Compatibility rule |
| :--- | :--- | :--- | :--- |
| Style aliases: `'dark'`, `'light'`, `True` | `AttributeError: module 'stackprinter.colorschemes' has no attribute 'dark'` | `'dark'` maps to `'darkbg'`, `'light'` maps to `'lightbg'`, `True` maps to `'color'`, producing normal ANSI output | Precedes strict error preservation; alias resolution required across all stylers |
| Style aliases: `None`, `False`, `''`, `'none'` | `TypeError: attribute name must be string` or `AttributeError` | Render clean plaintext output with no ANSI escape sequences | Precedes strict error preservation; canonical plaintext fallback required |
| Thread with no frame mapping (ident absent, maps to `None`, unstarted, or dead) | Emits empty stack `"<MockThread(...)>

    "` | Returns `"%r: no frames found" % thread` deterministically | Precedes strict output format preservation; consistent missing-frame text required |
| Configuration routing: `_config=` passed to public entry points | Returns diagnostic fallback on exceptions; rejected on frame/thread targets | See the "Entry points, options, and error handling" section | Precedes baseline parameter rejection; internal configuration routing required |
| Extended option acceptance: `source_lines_after` on frame, thread, or current stack targets | Raises `TypeError: unexpected keyword argument 'source_lines_after'` | Accepted across exception, frame, thread, and current stack targets; default `1` | Precedes baseline keyword set restrictions; uniform multi-line inspection required |
| Single compiled regex: `suppressed_vars=re.compile(...)` / `suppressed_paths=re.compile(...)` | Raises `TypeError: 're.Pattern' object is not iterable` | Accepted as a valid single-pattern suppression specification | Precedes baseline type restrictions; single pattern convenience required |
| Target without traceback: exception instance without traceback + unknown kwargs | Returns `"Type: msg"` without validating unknown kwargs (baseline unvalidated behavior) | Preserves baseline behavior: returns `"Type: msg"` directly without validating unknown kwargs; the reserved `config=` rejection and the `_config` type check still apply first | Preserves baseline non-validation for unknown kwargs only; the `_config` type contract is enforced before this early return |
| Target without traceback: exception instance without traceback (`exc.__traceback__ is None`) with styling options | Applies ANSI escape sequences when an ANSI style (such as `style='darkbg'`) is specified | Unconditionally returns plain text `"<exception class name>: <message>"` (e.g. `'ValueError: x'`) without ANSI escape sequences | Takes precedence over styling contracts; an exception object without a traceback unconditionally returns plain text `"<Type>: <msg>"` without applying styles |
| Silent stderr: `show(exc)` with default `'stderr'` and `sys.stderr is None` | Returns `None` silently before checking parameters | Preserves baseline behavior: returns `None` silently without checking kwargs | Preserves baseline non-validation when output destination is unavailable |
| `BaseException` instance target: `format(KeyboardInterrupt(...))` / `format(SystemExit(...))` | Raises `ValueError` rejecting `BaseException` instances that are not `Exception` subclasses | Raises `ValueError` rejecting `BaseException` instances; `sys.exc_info()` tuple remains accepted | Baseline semantic clarification: instance target requires `Exception` subclass |
| Stack length: `max_frames=N` | No such option; passing it raises `TypeError: unexpected keyword argument 'max_frames'` | Truncates each stack block to its innermost `N` frames and appends `    ... (<k> frames omitted)` | Precedes baseline keyword-set restrictions; applies uniformly to exception, frame, thread and current-stack targets |

---

## Public contract to preserve

- Public entry points remain available with unchanged names and import locations: `stackprinter.format`, `stackprinter.show`, `format_current_stack`, `show_current_stack`, `format_current_exception`, `show_current_exception`, `set_excepthook`, `remove_excepthook`, `TracePrinter`, and `trace`.
- Function signatures and accepted keyword arguments remain fully compatible across all public entry points.
- Target types: `stackprinter.format()` continues to accept an exception instance (must be a subclass of `Exception`), a `sys.exc_info()` tuple `(type, value, tb)`, a frame (`types.FrameType`), or a thread (`threading.Thread`). Passing an instance of `BaseException` that is not an `Exception` subclass (e.g. `KeyboardInterrupt`, `SystemExit`) directly as the target must raise `ValueError`. The `sys.exc_info()` tuple form `(type, value, tb)` continues to accept and format `BaseException` (such as `KeyboardInterrupt`).
- Calling `stackprinter.format()` or `stackprinter.show()` without an explicit target continues to resolve the currently handled exception inside an `except` block or the calling stack frame outside exception handling.
- `stackprinter.show()` continues to accept `'stderr'`, `'stdout'`, or any file-like object exposing a `write()` method.
- When `show()` is invoked with default `'stderr'` in environments where `sys.stderr` is `None`, the non-crashing silent return behavior remains intact.
- The style option must support the complete alias set documented under `stackprinter.styling`: plain-text aliases produce no ANSI escapes, ANSI styles produce ANSI output, and shorthand aliases resolve to the equivalent canonical style.
- All public formatting keyword options retain their established meanings and defaults:
  - `source_lines`: integer count (e.g. `0`, `1`, `5`) or `'all'`.
  - `source_lines_after`: integer count of source lines shown after the highlighted line; default `1`.
  - `show_signature`: boolean controlling inclusion of function headers.
  - `show_vals`: `'like_source'`, `'line'`, `'all'`, `None`, or `False`.
  - `truncate_vals`: when `truncate_vals=n`, truncate only when the representation length is strictly greater than `n + 3` (lengths exactly `n + 1`, `n + 2`, and `n + 3` are not truncated). When truncating, take the first `n` characters, strip trailing whitespace (`rstrip`), and append `...`; setting `n=0` or `False` completely disables truncation. For example, `truncate("abcd efghijk", 5)` returns `"abcd..."` (not `"abcd ..."`).
  - `line_wrap`: integer column threshold, or `0`/`False` to disable wrapping.
  - `suppressed_paths`: iterable collection (`list`, `tuple`, `set`) of string patterns or compiled regular expressions, a single string pattern, a single compiled regular expression, or `None`.
  - `suppressed_vars`: iterable collection (`list`, `tuple`, `set`) of string patterns or compiled regular expressions, a single string pattern, a single compiled regular expression, or `None`.
  - `suppressed_exceptions`: collection of exception classes (defaulting to `[KeyboardInterrupt]`). `suppressed_exceptions=None` means no exception suppression (verbose rendering of every exception type), while omitting the option keeps the default `[KeyboardInterrupt]`.
  - `reverse`: boolean controlling frame and summary ordering.
  - `add_summary`: boolean or `'auto'` appending a compact traceback summary.
  - `max_frames`: integer count `>= 1` or `None` (default `None`) truncating each stack block to its innermost frames, encapsulated within `FormatConfig`.
  - `indent`: string prefix prepended to every non-empty output line (default `''`).

---

## Entry points, options, and error handling

This section serves as the single authoritative reference for entry point parameter routing, option acceptance, and error handling rules across all targets.

### Option Acceptance Matrix

| Entry Point / Target | `source_lines` | `source_lines_after` | `show_signature` | `show_vals` | `truncate_vals` | `line_wrap` | `suppressed_paths` | `suppressed_vars` | `suppressed_exceptions` | `reverse` | `add_summary` | `max_frames` | `style` | `_config` | `config` | Unknown kwargs | indent |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `format(exc)` / `show(exc)` | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | **TypeError** | Debug-dependent | Accepted |
| `format(frame)` / `show(frame)` | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | **TypeError** | Accepted | Accepted | Accepted | Accepted | Accepted | **TypeError** | **TypeError** | Accepted |
| `format(thread)` / `show(thread)` | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | **TypeError** | Accepted | Accepted | Accepted | Accepted | Accepted | **TypeError** | **TypeError** | Accepted |
| `format_thread(thread, ...)` | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | **TypeError** | Accepted | Accepted | Accepted | Accepted | Accepted | **TypeError** | **TypeError** | Accepted |
| `format_current_stack` / `show_current_stack` | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | **TypeError** | Accepted | Accepted | Accepted | Accepted | Accepted | **TypeError** | **TypeError** | Accepted |
| `format_current_exception` / `show_current_exception` | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | **TypeError** | Debug-dependent | Accepted |
| `TracePrinter` / `@trace` | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | - | Accepted | Accepted | **TypeError** | **TypeError** | Accepted |
| `set_excepthook` | - | - | - | - | - | - | - | - | - | - | - | - | - | Ignored (baseline **kwargs) | **TypeError** | Ignored (baseline **kwargs) | - |
| `remove_excepthook` | - | - | - | - | - | - | - | - | - | - | - | - | - | **TypeError** | **TypeError** | **TypeError** | - |
| `FrameFormatter.__init__` | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted (positional only) | **TypeError** | **TypeError** | Accepted |
| `FormatConfig.__init__` | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | Accepted | N/A | **TypeError** | **TypeError** | Accepted |

### `_config` Routing and Merging Rules

- **Type Constraint**: The private `_config` parameter accepts ONLY instances of `FormatConfig`. Non-`FormatConfig` arguments are rejected across all participating entry points (see Validation order below).
- **Precedence & Merging**: `_config` provides the baseline formatting configuration. Any explicit keyword arguments passed to the entry point override the corresponding settings in `_config` (equivalent to calling `_config.with_overrides(**kwargs)`). Options not explicitly passed retain their settings from `_config`.
- **Scope**: Private `_config` routing applies to all public entry points except `set_excepthook` and `remove_excepthook`. Tracing facilities (`TracePrinter` and `trace`) accept `_config` to initialize the event formatter and styler.

### Unknown Keyword Arguments and Target-Specific Restrictions

- **Reserved Parameter `config`**: Passing `config=` to any public entry point or constructor raises `TypeError` (see Validation order below).
- **Target-Specific Restrictions**: Frame, thread, and current-stack targets reject `suppressed_exceptions` with `TypeError`, even when `_config` is supplied. This also applies to the module-level `stackprinter.format_thread(thread, ...)` entry point, which must reject `suppressed_exceptions` with `TypeError` before delegating to its formatter. `stackprinter.formatting.format_stack(frames, ...)` is an internal helper, not a public top-level API; it also rejects `suppressed_exceptions` with `TypeError`.
- **Unknown Keyword Handling**: Frame, thread, current-stack, and tracing targets strictly reject unlisted keyword arguments. Exception targets with an active traceback evaluate unknown keyword arguments according to active debug settings.

### Validation order

Formatting and display entry points process targets and options according to the following strict evaluation order:

0. **Reserved Parameter and Private Configuration Type** (highest precedence: evaluated before target dispatch, ordinary option validation, and the traceback-free early return below, regardless of whether the target has a traceback and regardless of debug mode):
   - Passing `config=` to any public entry point or constructor raises `TypeError`. The only path that does not inspect `config=` is the `show()` silent-stderr return in step 1, which validates no formatting parameter at all.
   - Passing a `_config` argument that is not an instance of `FormatConfig` raises `TypeError` at every entry point that participates in `_config` routing, including when the exception target has `__traceback__ is None`, and before any plain-text early return is produced.
1. **Pre-Validation Early Returns**:
   - Invoking `show(exc)` with default `'stderr'` when `sys.stderr is None` silently returns `None` without validating any formatting parameter, including `config=` and `_config` (baseline behavior).
   - Formatting an exception instance where `__traceback__ is None` unconditionally returns uncolored plain text `"<Type>: <msg>"` (e.g. 'ValueError: msg') without validating ordinary formatting options (unknown keyword arguments, styling options, and option values) or applying ANSI styles. The `config=` rejection and the `_config` type check in step 0 still run before this return.
2. **Target Dispatch and Target-Specific Option Validation**:
   - Frame, thread, and current-stack targets reject `suppressed_exceptions` (`TypeError`); along with tracing targets, they reject unknown keyword arguments (`TypeError`).
   - Passing a `BaseException` instance that is not an `Exception` subclass directly as the target raises `ValueError`. For an exception target with an active traceback, passing unknown keyword arguments triggers `TypeError` in debug mode or diagnostic fallback when unset.
3. **`_config` Merging and Option Value Validation**:
   - Merging explicit keyword arguments over `_config` is equivalent to calling `_config.with_overrides(**kwargs)`.
   - Invalid option values for `source_lines`, `show_vals`, `max_frames`, or `indent` raise `ValueError` during this stage.
4. **Renderer Delegation**:
   - Exception targets delegate to `ExceptionRenderer.render`, thread targets to `ThreadStackFormatter.format_thread`, frame targets to `FrameFormatter`, and tracing targets to `TraceEventFormatter.format_event`. Entry points return the output directly.
5. **Formatting Failure Fallback**:
   - Applies only to exception targets with an active traceback: if `PY_STACKPRINTER_DEBUG` is set, internal formatting exceptions propagate to the caller; if unset, returns diagnostic fallback text starting with `"Stackprinter failed"`.
---

## Behavior to preserve except where listed above

1. **Exception Traceback and Frame Rendering**: Formatting an exception preserves the sequential order of traceback frames, source code context surrounding executed lines, execution arrow markers (`-->`), function header listings, frame headline headers (`File "...", line ..., in ...`), exception type name, exception message, and visible variable assignments with their formatting and indentation.
2. **Exception Chaining and Context Precedence**: When formatting an exception with an explicit cause (`__cause__`), the cause traceback precedes the main exception, separated by `"

The above exception was the direct cause of the following exception:

"`. When explicit cause is absent and implicit context (`__context__`) exists with `__suppress_context__=False`, context precedes the exception with `"

While handling the above exception, another exception occurred:

"`. When `__suppress_context__=True`, implicit context remains completely suppressed.
3. **ExceptionGroup Compatibility Handling**: When formatting an exception type named `'ExceptionGroup'` (such as Python 3.11+ `ExceptionGroup`), the library preserves its existing fallback compatibility behavior by returning standard `traceback.format_exception()` output without performing custom frame decomposition or raising errors.
4. **Plain-Text and ANSI Output Styling**: Plain-text formatting (`style='plaintext'` or `'plain'`, as well as shorthand aliases `'none'`, `None`, `False`, `''` - relative to baseline these aliases are new, see required changes table) contains no ANSI escape sequences (`[...]`), producing uncolored text suitable for logging. Supported ANSI styles (`'darkbg'`, `'darkbg2'`, `'darkbg3'`, `'lightbg'`, `'lightbg2'`, `'lightbg3'`, and `'color'`, as well as aliases `'dark'`, `'light'`, `True` - relative to baseline these aliases are new, see required changes table) apply their respective color and formatting escape codes to frame headlines, line numbers, executed line markers, code tokens, variable assignments, exception types, exception messages, and chain hints, preserving the underlying text hierarchy, file references, and variable data without altering non-styling content.
5. **Consistent Formatting Option Semantics Across Targets**: Common frame-formatting options (`source_lines`, `source_lines_after`, `show_signature`, `show_vals`, `truncate_vals`, `line_wrap`, `suppressed_vars`, and user-specified `suppressed_paths`) apply consistent formatting rules to individual stack frames whether formatting an exception, an explicit frame, the current call stack, or a running thread, while preserving target-specific conventions (such as thread-specific indentation, automatic threading path suppression, and thread-specific summary defaults).
6. **Reverse Ordering Semantics**: Specifying `reverse=True` inverts the frame sequence across stack, summary, and exception rendering so that the innermost (most recent) frame appears first and outer frames follow. In exception formatting with a summary enabled, the exception type and message are displayed at the very beginning, followed by the summary listing (with reversed frames), the separator header (`---- (full traceback below) ----

`), and the full traceback stack placed below.
7. **Variable, Path, and Exception Suppression**: Variables matching `suppressed_vars` patterns are masked with `'*****'` without triggering property evaluation or dynamic attribute side effects. Frames matching `suppressed_paths` are rendered in compact form (fewer source lines on first occurrence, and collapsed detail without variable values on deeper calls). Both `suppressed_paths` and `suppressed_vars` accept an iterable collection (`list`, `tuple`, `set`) of string patterns or compiled regular expressions, a single string pattern, a single compiled regular expression (single compiled regex is new relative to baseline, see required changes table), or `None` to disable suppression. Exceptions matching `suppressed_exceptions` (defaulting to `[KeyboardInterrupt]`) retain their existing reduced-detail summary behavior rather than emitting full verbose frame blocks.
8. **Thread Stack Formatting and Missing Frame Boundaries**: Formatting an active `threading.Thread` instance renders the thread representation (`%r % thread`) followed by an indented representation of its call stack with `threading.py` paths suppressed by default. If the thread ident is absent from `sys._current_frames()` or has no accessible frame, the output deterministically returns `"%r: no frames found" % thread` (relative to baseline this boundary text is new, see required changes table).
   For thread delegation, entry point routing, and return value details, see the "Entry points, options, and error handling" section.
9. **Source Context Granularity**: `source_lines=0`, `source_lines=1`, positive multi-line values, and `'all'` preserve their existing source-context semantics: `source_lines=0` omits the source code listing entirely (with variable display governed by `show_vals`); `source_lines=1` restricts the core source context to the executed line while continuing to incorporate function headers or surrounding context according to active formatting options; positive multi-line values `n > 1` expand the context window around the executed line; and `'all'` displays the entire enclosing scope of the frame.
10. **Value Truncation and Line Wrapping**: When `truncate_vals=n`, truncate only when the representation length is strictly greater than `n + 3` (lengths exactly `n + 1`, `n + 2`, and `n + 3` are not truncated). When truncating, take the first `n` characters, strip trailing whitespace (`rstrip`), and append `...`; setting `n=0` or `False` completely disables truncation. For example, `truncate("abcd efghijk", 5)` returns `"abcd..."` (not `"abcd ..."`). Lines exceeding `line_wrap` characters are wrapped with proper indentation; setting `line_wrap=0` or `line_wrap=False` disables wrapping completely.
11. **Python 3.12+ Unmapped Line Number Resilience**: Frames or traceback entries where `tb_lineno` or `f_lineno` is `None` (such as instruction points with no line mapping in Python 3.12+) are formatted safely by falling back to `co_firstlineno` without raising exceptions.
    `stackprinter.frame_formatting.FrameFormatter` must remain importable and callable as `FrameFormatter()(frame, lineno=None)`.
12. **Exception Formatting Error Fallback and Debug Mode**:
    Internal formatting errors and debug mode behavior follow the rules defined in the "Entry points, options, and error handling" section above.
13. **Tracing Behavior and Trace Events**: Executing code within a `TracePrinter` context manager or under the `@trace` decorator emits call and return events to `print_function` within `depth_limit` with hierarchical indentation. When an exception occurs within traced code, an exception trace note is emitted, and if `stop_on_exception=True`, the trace hook is disabled upon processing the exception event, preserving existing observable event emission and exception propagation.
14. **Deterministic Structural Layout and Ordering**: Repeated formatting calls with the same input target and options preserve the existing deterministic textual layout, frame hierarchy, and line ordering. For dynamic runtime targets such as live frames or running threads, formatting reflects state at the moment of inspection without altering or caching target state.

---

## constraints

- All refactored code must run on standard Python 3.8+ without introducing new external third-party dependencies.
- Maintain full backward compatibility with existing tests; all pre-existing tests in the test suite must pass without modification.
- Do not modify any pre-existing tests or existing test support files in the repository.
- Do not introduce root-level configuration or injection files: do not create `pytest.ini`, `setup.cfg`, `tox.ini`, `pyproject.toml`, root-level test configuration files, `sitecustomize.py`, `usercustomize.py`, `pytest.py`, or any `.pth` files in the repository root.
- Production code under `stackprinter/` must remain pure and free from test framework or evaluation dependencies: do not import `pytest` inside `stackprinter/`. The following strings must not appear anywhere in production code: `test_refactor_features`, `test_refactor_compatibility`, `verifier.py`, `grader.py`, `/logs/artifacts`, `__VERIFIER_BACKDOOR__`. Ordinary English words (e.g. verifier, grader appearing as ordinary nouns in comments or docstrings) do not constitute a violation.
- Do not remove, rename, or alter the signature of any existing public API function or class in `stackprinter`.

IMPORTANT: Create a new branch from the task's base commit `7a07a51a806e70c273a96071c87d19289bc0c69e` and commit all task changes, including new files, when you are done.
