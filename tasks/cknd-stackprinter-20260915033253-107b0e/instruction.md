# Refactor Traceback Formatting Engine to Structured Exception Tree Pipeline

## Background

In `stackprinter`, traceback formatting in `formatting.py` is centered around `format_exc_info()`, which currently functions as a monolithic procedural routine. It tightly couples multiple disparate responsibilities:
- Traversing exception causality chains (`__cause__`, `__context__`, and `__suppress_context__`).
- Performing AST and frame inspections via `extraction.get_info()`.
- Formatting individual stack frames and variable assignments.
- Generating chain transition hints and applying ANSI color templates.
- Appending trailing summary blocks.

This tight coupling introduces critical architectural and functional limitations:
1. **Lack of Intermediate Representation (IR)**: Traceback inspection does not produce a structured data model. Callers and downstream consumers cannot programmatically inspect, query, or transform the exception tree prior to string serialization.
2. **Missing `ExceptionGroup` Support**: Since Python 3.11 introduced `ExceptionGroup` and `BaseExceptionGroup`, `stackprinter` has bypassed tree formatting entirely by falling back to standard library `traceback.format_exception`. Consequently, rich formatting features—including frame variable values, semantic highlighting, source context, and variable censorship (`suppressed_vars`)—are lost for all grouped exceptions.
3. **Vulnerability to Circular References**: Dynamic modifications to exception chains (e.g. `e1.__context__ = e2; e2.__context__ = e1`) result in uncontrolled recursion and `RecursionError` crashes during formatting.
4. **API Inconsistencies**: Passing a naked `BaseException` instance (e.g., `KeyboardInterrupt` or a custom `BaseExceptionGroup`) directly to `stackprinter.format()` causes a `ValueError` because the entrypoint strictly checks `isinstance(thing, Exception)`.

## Expected Behavior

Refactor the formatting engine into a decoupled, two-phase pipeline:
1. **Structural Analysis Phase**: Construct a structured, cycle-safe exception tree representation (`ExceptionNode` and `build_exception_tree`).
2. **Rendering Phase**: Format the exception tree via a dedicated, modular renderer (`TracebackRenderer`).

---

### 1. Structured Exception Data Model (`ExceptionNode`)

Define an `ExceptionNode` class in `stackprinter.formatting` (and export it from `stackprinter.formatting` as well as `stackprinter`) to represent a single exception in an exception graph/tree.

#### Public Attributes:
- `exc_type`: `type[BaseException]` - The exception class.
- `exc_value`: `BaseException | None` - The exception instance.
- `traceback`: `types.TracebackType | None` - The traceback object associated with this exception.
- `frames`: `list[FrameInfo]` - Ordered list of `FrameInfo` namedtuples extracted from `traceback` (from caller to innermost raise site) using `stackprinter.extraction.get_info`. If `traceback` is `None` or has no frames, this must be an empty list `[]`.
- `chain_type`: `str | None` - The causal relation to the upstream exception:
  - `'cause'`: If explicitly caused by `__cause__` (`raise ... from ...`).
  - `'context'`: If implicitly caused by `__context__` (and not suppressed by `__suppress_context__`).
  - `'group_sub'`: If this node is a child exception of an enclosing `ExceptionGroup`.
  - `None`: For the root exception or an unchained exception.
- `parent`: `ExceptionNode | None` - The enclosing parent node (for a sub-exception inside an `ExceptionGroup`, or the child exception in a causal chain that caused this node to be visited; `None` for the root exception).
- `chain_parent`: `ExceptionNode | None` - The upstream causal cause/context node that led to this exception, or `None` if there is no causal ancestor.
- `sub_exceptions`: `list[ExceptionNode]` - If this node represents an `ExceptionGroup` (or `BaseExceptionGroup`), this list contains the `ExceptionNode` for each child exception in `exc_value.exceptions`. For standard exceptions, this must be an empty list `[]`.
- `is_group`: `bool` - `True` if `exc_value` is an instance of `BaseExceptionGroup` (or has an `.exceptions` sequence); `False` otherwise.
- `is_cycle`: `bool` - `True` if a circular reference was detected when traversing this exception along its active ancestor path; `False` otherwise.

#### Public IR Methods & Properties:
- `depth`: `int` (property)
  - Returns the nesting depth of this node from the root exception in the tree hierarchy (the root node has `depth = 0`, and any child or upstream causal node has `depth = parent.depth + 1`).
- `leaves`: `list[ExceptionNode]` (property)
  - Returns an ordered list of all leaf exception nodes (concrete non-group nodes where `is_group is False` and `sub_exceptions` is empty) in preorder traversal order.
- `walk(self, order: str = 'preorder') -> Iterator[ExceptionNode]`:
  - Traverses and yields all reachable nodes in the tree/subgraph without infinite recursion on cycles. Supports `order='preorder'` (node first, then upstream `chain_parent`, then `sub_exceptions`) and `order='postorder'` (upstream `chain_parent`, `sub_exceptions`, then node).
- `find(self, exc_type: type) -> list[ExceptionNode]`:
  - Returns all nodes in traversal order whose `exc_type` is a subclass of `exc_type`.
- `filter(self, predicate: Callable[[ExceptionNode], bool]) -> ExceptionNode | None`:
  - Recursively filters the tree according to `predicate(node)`, returning a newly constructed, pruned tree without mutating the original tree.
  - For standard exceptions, returns a new clone if retained, or `None` if pruned.
  - For `ExceptionGroup` nodes, recursively filters children in `sub_exceptions`. If all children are pruned and `predicate(self)` is `False`, the group is pruned (`None`). If any children remain, returns a new group node containing the retained children with updated `parent` pointers. Any `chain_parent` is also recursively filtered.

---

### 2. Exception Tree Builder (`build_exception_tree`)

Implement `build_exception_tree(etype, evalue, tb, suppressed_vars=None) -> ExceptionNode` in `stackprinter.formatting`:
- **Causality & Group Traversal**:
  - Recursively parse exception relationships following standard Python exception chaining (`__cause__` with `chain_type='cause'`, and unsuppressed `__context__` with `chain_type='context'`).
  - For `ExceptionGroup` (or `BaseExceptionGroup`) instances, recursively parse each child exception in `.exceptions` with `chain_type='group_sub'`.
  - Maintain bidirectional links between nodes: set `parent` on children and upstream causal nodes, and set `chain_parent` on nodes that were caused by an upstream exception.
- **DAG vs. Cycle Detection**:
  - Distinguish between legitimate directed acyclic graph (DAG) reuse and active circular references.
  - Exception instances shared across distinct branches (such as multi-task aggregations) must be supported without being marked as cyclic.
  - A node is marked with `is_cycle=True` only when an exception instance is encountered that already exists along the current active ancestor chain. Truncate further traversal upon encountering a cycle to prevent infinite recursion.
- **Frame Extraction**:
  - Extract frames for all tracebacks using `stackprinter.extraction.get_info(tb, suppressed_vars=suppressed_vars)`.

---

### 3. Dedicated Renderer Pipeline (`TracebackRenderer`)

Implement `TracebackRenderer` in `stackprinter.formatting` to encapsulate traceback serialization:
- **Renderer Configuration**:
  - `TracebackRenderer` must accept the formatting parameters supported by `stackprinter` (such as `style`, `source_lines`, `source_lines_after`, `show_signature`, `show_vals`, `truncate_vals`, `line_wrap`, `reverse`, `suppressed_paths`, `suppressed_vars`, `suppressed_exceptions`, and `add_summary`), storing them as renderer settings.
- **`render(self, node: ExceptionNode) -> str`**:
  - Formats an `ExceptionNode` tree into the complete output string.
  - **Causal Chains**:
    - Format causal ancestors (`chain_parent`) separated by the standard Python exception chaining banners (for explicit causes and context exceptions).
    - When `reverse=True`, reverse the causal chain output order so the current exception is output first followed by its causal ancestors.
    - If `node.is_cycle` is `True`, output an informative cycle indicator banner instead of recursing indefinitely.
  - **`ExceptionGroup` Branch Rail Rendering**:
    - Render the `ExceptionGroup`'s frames and message, followed by each sub-exception branch.
    - Each branch must start with a 1-based numbered separator banner (`+---------------- {index} ----------------`), indented by 2 spaces per nesting depth level.
    - All lines of a sub-exception branch (including any nested causal chain frames, banners, and child lines) must be prefixed with vertical rails (`| ` indented to the current branch depth; empty lines must not have trailing whitespace after the rail).
    - Sub-branches must inherit all formatting options (`style`, `source_lines`, `suppressed_vars`, etc.).
  - **Styling and Summaries**:
    - Apply existing styling rules and color schemes consistently across frames and banners.
    - Append the trailing summary block when `add_summary` is active (`True` or `'auto'`).

---

### 4. Integration and Backward Compatibility

- **`format_exc_info()`**:
  Refactor `format_exc_info(etype, evalue, tb, ...)` to construct an `ExceptionNode` via `build_exception_tree` and serialize it with `TracebackRenderer`. Its public signature, default parameters, and output for standard single exceptions and existing causal chains must remain completely backward compatible.
- **Top-Level `format()`**:
  Update `stackprinter.format(thing=None, **kwargs)`:
  - If `thing` is an `ExceptionNode`, directly format it via `TracebackRenderer(**kwargs).render(thing)`.
  - Accept any `BaseException` instance (such as `KeyboardInterrupt`, `SystemExit`, or `BaseExceptionGroup`), passing it cleanly into the new formatting pipeline without raising `ValueError`.
- **Module Exports**:
  Export `ExceptionNode`, `build_exception_tree`, and `TracebackRenderer` from `stackprinter.formatting` and `stackprinter`.

## Compatibility and Scope

- All existing public functions and parameters must remain supported:
  - `stackprinter.format()`
  - `stackprinter.show()`
  - `stackprinter.format_exc_info()`
  - `stackprinter.format_stack()`
  - `stackprinter.format_summary()`
- All existing tests in `tests/test_formatting.py`, `tests/test_frame_inspection.py`, `tests/test_source_inspection.py`, and `tests/test_utils.py` must pass without regressions.
- `FrameFormatter`, `extraction.get_info()`, and `colorschemes` internal implementations must not be broken or altered in incompatible ways.

IMPORTANT: Create a new branch from the task's base commit `7a07a51a806e70c273a96071c87d19289bc0c69e` and commit all task changes, including new files, when you are done.
