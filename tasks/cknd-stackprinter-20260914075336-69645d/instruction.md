## Background

Stackprinter combines caller-owned formatting options, traceback presentation, and mutable tracing activation state. Internal suppression rules currently modify caller configuration, style interpretation differs across rendering paths, and a tracer stores state that belongs to individual activations. Refactor these responsibility boundaries so rendering configuration remains owned by its caller and each activation owns its lifecycle, while retaining the public diagnostic capabilities.

## Goal

- Separate caller configuration from internal rendering options, and reusable tracer configuration from per-activation state. Rendering MUST leave caller configuration and installed trace hooks untouched; one activation MUST NOT overwrite another activation's saved predecessor or lifecycle state. These boundaries are defined by observable ownership, side effects, and lifecycle behavior; internal structure, inheritance, and delegation are unrestricted.
- For format_thread() and the IPython hook installed by set_excepthook(), passing suppressed_paths as a list or tuple MUST NOT modify or mutate the caller's original sequence. Successful calls and formatting failures MUST leave it intact; repeated calls MUST NOT accumulate internal patterns.
- Sink failures mean exceptions from streams used by show() or the standard Python excepthook, or from TracePrinter's print_function. Caller configuration MUST remain intact. format_thread() returns text without writing to a sink; the IPython hook returns a one-element list of formatted text. Consumption of these returned values is outside the library's lifecycle obligations.
- The style name plain MUST be a full, identical alias for plaintext across every diagnostic formatting entry point, including single exception formatting, chained exceptions (explicit __cause__ and implicit __context__), summaries (format_summary()), format(), and show() (both return values and written stream content). Both style names MUST produce identical text and MUST NOT add ANSI styling; escape sequences already present in user content MUST remain unchanged.
- Nested with contexts, nested enable() calls, and recursive decorator calls MUST each save and restore the immediately preceding trace hook on normal exit or exception. Calling disable() on an inactive TracePrinter MUST be a silent no-op.
- If an exception raised inside an inner activation is caught while an outer activation remains active, the outer trace hook MUST remain installed until that outer activation exits. Context and decorator activations MUST restore their immediate predecessor before a sink exception reaches the caller.
- After a sink exception in a manual enable() activation, restoration MUST occur when the caller invokes disable(), including for nested activations. Sink failure MUST NOT replace or uninstall exception hooks; remove_excepthook() retains its existing restoration behavior.
- With stop_on_exception=True, a fresh explicit raise MUST stop the current activation even if it reuses an exception object previously caught from an inner activation. This applies both within called functions and directly in the already-running frame that entered the context or enabled tracing.
- Propagation of the original inner exception MUST preserve the outer activation. Completed activations MUST NOT retain otherwise unreachable application objects through saved exceptions or frames.

## Public contract to preserve

Preserve the following public interfaces, parameter names, default values, return types, and documented behaviors:
- stackprinter.format(thing=None, **kwargs): accepts exception objects, sys.exc_info() tuples, frame objects, and thread objects; returns formatted string.
- stackprinter.show(thing=None, file='stderr', **kwargs): prints formatted output to the specified stream ('stderr', 'stdout', or file-like object) and returns None.
- stackprinter.format_current_stack(**kwargs) and stackprinter.format_current_exception(**kwargs): return formatted strings for the current stack or handled exception.
- stackprinter.show_current_stack(**kwargs) and stackprinter.show_current_exception(file=sys.stderr, **kwargs): write the current stack or handled exception and return None.
- stackprinter.formatting.format_stack(frames, style='plaintext', source_lines=5, show_signature=True, show_vals='like_source', truncate_vals=500, line_wrap=60, reverse=False, suppressed_paths=None, suppressed_vars=[]): returns formatted stack string.
- stackprinter.formatting.format_summary(frames, style='plaintext', source_lines=1, reverse=False, **kwargs): returns formatted summary string.
- stackprinter.formatting.format_stack_from_frame(fr, add_summary=False, **kwargs): returns formatted stack string.
- stackprinter.formatting.format_exc_info(etype, evalue, tb, style='plaintext', add_summary='auto', reverse=False, suppressed_exceptions=[KeyboardInterrupt], suppressed_vars=[], **kwargs): returns formatted exception traceback string.
- stackprinter.format_thread(thread, add_summary=False, **kwargs): returns formatted thread traceback string.
- stackprinter.set_excepthook(**kwargs) and stackprinter.remove_excepthook(): install and restore the system or IPython excepthook and return None.
- stackprinter.formatting.get_formatter(style, **kwargs): returns FrameFormatter or ColorfulFrameFormatter. Omitting style raises TypeError.
- stackprinter.tracing.TracePrinter(suppressed_paths=[], depth_limit=20, print_function=print, stop_on_exception=True, **formatter_kwargs): preserves existing default constructor behavior (calling without arguments raises TypeError because get_formatter() requires style), context manager methods (__enter__, __exit__), and activation methods (enable(force=False, current_depth=None), disable()).
- stackprinter.tracing.trace(*args, suppressed_paths=[], **formatter_kwargs): decorator supporting function wrapping and parameter pass-through.
- FrameFormatter and ColorfulFrameFormatter classes under stackprinter.frame_formatting; ColorfulFrameFormatter remains a subclass of FrameFormatter.
- Preserve existing `ValueError` behavior for unsupported format inputs, wrong-length exception tuples, and three-item tuples whose exception type/value fields are invalid; preserve valid traceback objects and `tb=None`. Do not promise one exception type for a malformed non-None traceback slot, whose failure depends on the downstream traversal path. Preserve existing `TypeError` behavior for omitted required style arguments.

## Behavior that must stay unchanged

Except for the changes specified in Goal, all existing behavior MUST remain unchanged.

- MUST NOT alter existing source code inspection, variable extraction, value truncation, line wrapping, reverse ordering, or exception chaining formatting logic for existing valid styles ('plaintext', 'darkbg', 'lightbg', etc.) except for recognizing 'plain' as an alias for 'plaintext'.
- MUST NOT change the existing constructor parameter requirements or default exception behavior of TracePrinter(); instantiating TracePrinter() without keyword arguments or without specifying style MUST raise TypeError exactly as in the baseline.
- MUST NOT mutate caller-supplied collections or arguments passed to public functions.
- MUST preserve the default exception-handling and traceback formatting output for calls that do not exercise the refactored behaviors.
- MUST maintain existing excepthook replacement and restoration semantics for both standard Python and IPython environments.
- MUST preserve existing trace-hook conflict behavior: `enable(force=False)` rejects an unrelated installed hook without replacing it, while a forced activation restores that hook when disabled.
- MUST keep existing internal suppression patterns effective in rendered output and preserve their existing ordering relative to caller-specified patterns.

## constraints

- All production code changes MUST be strictly confined to the stackprinter/ directory. No files outside stackprinter/ may be added, modified, or removed.
- MUST NOT introduce any new runtime dependencies.
- MUST NOT install a process-wide trace hook at module import time.
- The internal implementation, module organization, and helper function design for normalization and tracing management may be freely structured by the author.
