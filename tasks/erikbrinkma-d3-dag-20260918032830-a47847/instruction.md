## Background

In `d3-dag`, layout operators—specifically `sugiyama`, `zherebko`, and `grid`—position directed graphs by assigning geometric coordinates to nodes and routing links between them. To compute correct positions, each operator requires node dimensions, which consumers specify either as constant `[width, height]` tuples or as dynamic callback accessors that evaluate dimensions for each node.

Currently, the way node dimensions are resolved, validated, and consumed during layout execution exhibits observable inconsistencies across operators:
- **Redundant Callback Invocations**: Dynamic callback accessors are invoked repeatedly for the same node during a single layout execution across layout calculations and attached built-in tweaks, rather than being evaluated once and consistently reused across that layout run.
- **Inconsistent Validation Boundaries**: Invalid constant dimensions are rejected immediately during operator configuration in some operators, while invalid dimensions returned from callbacks are handled inconsistently—failing at differing stages or with differing checks depending on the operator invoked.
- **Divergent Error Attribution**: Error messages across operators attribute failures inconsistently; certain operators report callback failures as invalid constant dimensions, while others fail to identify which node caused the failure or whether width or height was invalid.

For downstream consumers, state-dependent or computationally heavy callbacks yield unpredictable layouts and unnecessary overhead when called multiple times per node. Establishing a unified geometry resolution and validation contract ensures deterministic layout executions, consistent error reporting, and reliable per-node dimension caching across `sugiyama`, `zherebko`, and `grid`.

## Goal

Unify node dimension resolution, validation, and per-layout reuse across `sugiyama`, `zherebko`, and `grid` under a single observable geometry input contract.

The refactored system MUST ensure that:
- Constant dimensions and callback-based dimensions adhere to identical positive-dimension semantics and validation guarantees across all three layout operators.
- During any single layout execution, a node-size callback accessor is evaluated at most once per node across layout computation and attached built-in tweaks, providing consistent dimensions to all consumers.
- Constant dimension inputs are validated immediately at the operator configuration boundary, whereas callback dimensions are validated upon per-node resolution with standardized error details identifying the affected node and invalid values.
- Existing layout coordinates, link routing points, chaining interfaces, and public APIs remain fully compatible for valid deterministic inputs.

## Public contract to preserve

The following public interfaces, function signatures, and observable contracts MUST be preserved:

- **Operator Configuration APIs**:
  - `sugiyama().nodeSize(...)` and `sugiyama().nodeSize()`
  - `zherebko().nodeSize(...)` and `zherebko().nodeSize()`
  - `grid().nodeSize(...)` and `grid().nodeSize()`
  - Setter invocations MUST accept constant dimension tuples `readonly [number, number]` or callback accessors `(node: GraphNode<NodeDatum, LinkDatum>) => readonly [number, number]`.
  - Getter invocations with no arguments MUST return the configured `NodeSize` value (either the constant tuple or the callback function).
  - Fluent builder chaining MUST preserve existing return types and TypeScript generic type inference for node and link data across operators:
    - Common methods across all three operators (`sugiyama`, `zherebko`, and `grid`): `.nodeSize(...)`, `.gap(...)`, and `.tweaks(...)`.
    - Operator-specific fluent methods:
      - `sugiyama`: `.layering(...)`, `.decross(...)`, and `.coord(...)`.
      - `zherebko`: `.rank(...)`.
      - `grid`: `.lane(...)` and `.rank(...)`.

- **Shared Layout Utilities and Types**:
  - `cachedNodeSize(nodeSize)` MUST remain available, returning a callable accessor that computes node dimensions at most once per node and validates positive dimensions over the lifetime of the returned function.
  - `splitNodeSize(nodeSize)` MUST remain available, returning independent `[xLen, yLen]` accessor functions for width and height that read from the same per-node resolved dimensions.
  - Exported types `NodeSize`, `CallableNodeSize`, `NodeLength`, `LayoutResult`, `Rankdir`, and `Operator` MUST preserve their structural contracts.

- **Built-in Tweaks**:
  - All public tweak functions (`tweakSize`, `tweakFlip`, `tweakGrid`, `tweakShape`, `tweakSugiyama`, `tweakGridHandles`, and `tweakDirection`) MUST continue to accept their documented options and function seamlessly with layouts using constant or callback node dimensions.

- **Execution Contract**:
  - Invoking any configured layout operator with an input graph (`operator(graph)`) MUST return a `LayoutResult` object containing `{ width: number, height: number }` reflecting the overall layout dimensions.

## Behavior that must stay unchanged

### 1. Per-Layout Dimension Evaluation and Accessor Lifecycle
- During any single execution of `operator(graph)` on `sugiyama`, `zherebko`, or `grid`, the configured `nodeSize` callback accessor MUST be evaluated at most once for each node in the graph. The final layout coordinates and layout bounds for any given node MUST NOT depend on subsequent callback invocations or return values.
- Direct invocation of `cachedNodeSize(nodeSize)`: Calling the returned accessor directly caches dimensions per node for the lifetime of that accessor instance; evaluating it multiple times for the same node calls the underlying callback on the first invocation and returns cached dimensions on subsequent calls. If the callback throws or returns invalid dimensions, that failure MUST also be cached for subsequent invocations on that node.
- Passing an accessor to layout operators: Passing an accessor (whether wrapped with `cachedNodeSize` or a raw callback) to `sugiyama`, `zherebko`, or `grid` scopes evaluation to each layout execution. During each layout run, the underlying callback is evaluated at most once per node.
- Sequential executions of the same operator: Sequential executions (`op(graph); op(graph);`) are independent; the operator does not retain cached node dimensions across distinct runs and evaluates the callback anew in each separate execution.
- Executions across different operators: Different operators (or different instances of the same operator) do not share or reuse evaluated dimensions across runs; each operator run evaluates the callback independently.
- Nested and reentrant layout executions: When a layout execution triggers another layout execution (e.g. inside a callback or tweak), the inner and outer executions MUST remain completely isolated without cross-contaminating cached dimensions or invocation counts.
- Evaluating accessors from `splitNodeSize(nodeSize)`: Evaluating either `xLen(node)` or `yLen(node)` first resolves the node's dimensions; subsequently calling the other length accessor for that same node returns its dimension without invoking the callback again. Direct usage of `splitNodeSize` on constant values or non-validating callbacks (such as `splitNodeSize([0, 1])`) MUST NOT throw during splitting or evaluation, preserving existing baseline behavior.
- Single mutable tuple protection: When a callback reuses a single mutable array instance across invocations, the layout operator and `splitNodeSize` MUST capture dimensions defensively so that subsequent mutations of that tuple do not corrupt previously resolved dimensions.
- Nested `cachedNodeSize` wrapping: Wrapping an already cached accessor or constant tuple in multiple `cachedNodeSize` calls (`cachedNodeSize(cachedNodeSize(...))`) is supported and transparent: nested wrappers preserve the underlying dimensions and adhere to the same at-most-once evaluation guarantee.

### 2. Built-in Tweaks and Empty Graph Boundaries
- When a layout operator configured with `.nodeSize(callback)` has attached built-in tweaks via `.tweaks([...])`—specifically `tweakShape(callback)`, `tweakSugiyama(callback)`, or `tweakGridHandles(callback, ...)`—that receive the identical callback reference, the layout operator and those tweaks together MUST evaluate that callback at most once per node in a single execution.
  - The at-most-once evaluation guarantee strictly covers:
    1. Node-size resolution managed directly by the operator;
    2. Built-in tweaks that share execution context with the operator when passed the identity-equal callback reference.
  - Custom tweaks: If a custom tweak directly invokes a `nodeSize` callback, the invocation count is managed solely by the custom tweak itself and does not enjoy the operator's shared caching guarantee.
  - Custom tweaks MUST NOT depend on unexposed internal execution contexts.
- If a tweak receives a distinct callback function reference from the operator's `.nodeSize(...)` callback, each callback function reference MUST be evaluated independently according to its own usage, without sharing or interfering with the other's invocation count.
- Standalone tweak invocations: Calling tweaks outside a layout operator re-evaluates node dimensions for the provided graph without stale caching.
- When an empty graph (a graph with zero nodes) is passed to `sugiyama`, `zherebko`, or `grid`:
  1. The operator itself and built-in tweaks that use the operator-managed execution context will not invoke the `nodeSize` callback (invocation count is exactly 0).
  2. The layout operator first generates an initial layout result `{ width: 0, height: 0 }`.
  3. The first tweak receives this initial `{ width: 0, height: 0 }`.
  4. Each subsequent tweak receives the return value of the preceding tweak.
  5. The final layout result equals the return value of the last tweak.
  6. If a custom tweak directly invokes a callback, its invocation count is managed independently according to the custom tweak rules above, and does not fall under the operator's zero-invocation guarantee.

### 3. Constant and Callback Input Validation
- Constant dimensions and callback-returned dimensions MUST enforce symmetrical positive-dimension semantics and identical structural guarantees:
  - Both width and height MUST be finite numbers strictly greater than zero (`width > 0` and `height > 0`).
  - Inputs that are `null`, `undefined`, non-array values (other than callable functions in `.nodeSize(...)`), or arrays whose length is not 2 MUST be rejected with an `Error`.
- For constant dimensions passed to `.nodeSize(...)` on `sugiyama`, `zherebko`, or `grid`, or to `cachedNodeSize(...)`:
  - If the input is not a 2-tuple (e.g. `null`, `undefined`, a non-array primitive or object, or an array whose length is not 2), or contains zero, negative numbers, `NaN`, `Infinity`, `-Infinity`, BigInt, Symbol, or non-numeric values, the input MUST be rejected immediately with an `Error` during configuration.
- For dynamic callback accessors during layout execution:
  - If the callback returns a value that is not a 2-tuple (e.g. `null`, `undefined`, a non-array primitive or object, or an array whose length is not 2), or returns a 2-tuple containing zero, negative numbers, `NaN`, `Infinity`, `-Infinity`, BigInt, Symbol, or non-numeric values, the layout operator MUST throw an `Error` during layout execution when resolving that node.
- Valid constant dimension tuples and valid callback dimension results MUST be preserved exactly without truncation, rounding, or modification during layout computation.

### 4. Standardized Error Format and Context Attribution
- Errors resulting from invalid dimensions or callback evaluation failures MUST format their error message using a fixed key-value structure with exact keys in the following order:
  `category=<category>; node=<node>; width=<width>; height=<height>`
  (followed by `; returned=<returned>` when an input or return value cannot be decomposed into a 2-tuple, and followed by `; legacy=<legacy message>`).

- The `category` value MUST be strictly one of the following exact string tokens:
  - `constant-node-size`: when constant dimensions passed to `.nodeSize(...)` or `cachedNodeSize(...)` fail validation.
  - `invalid-callback-node-size`: when a callback accessor returns a non-tuple, malformed value, or non-positive dimension values.
  - `node-size-callback-threw`: when a callback accessor throws an exception during evaluation.

- The `node` value MUST be formatted as follows:
  - For `invalid-callback-node-size` and `node-size-callback-threw`:
    - If `node.data` is of primitive type (`string`, `number`, `boolean`, `null`, or `undefined`), the value MUST be `String(node.data)`.
    - For all other `node.data` types (e.g. `bigint`, objects, functions, or symbols; specifically `bigint` `node.data` belongs to the placeholder branch), the value MUST be the exact placeholder string `"<node data unavailable>"`.
  - For `constant-node-size` where no node is involved, the value MUST be the exact placeholder string `"N/A"`.

- The `width` and `height` values MUST be formatted as follows:
  - When the input is a 2-element array `[w, h]`:
    - If an element is a finite number, it MUST be formatted using `String(value)`.
    - If an element is a non-finite number, it MUST be `"NaN"`, `"Infinity"`, or `"-Infinity"`.
    - If an element is `null`, it MUST be `"null"`.
    - If an element is `undefined`, it MUST be `"undefined"`.
    - If an element is a `symbol`, it MUST be `String(value)`.
    - For any other primitive value (e.g. `string`, `boolean`, `bigint`), it MUST be `String(value)`.
    - For object or function elements, it MUST be `"<type: " + typeof value + ">"` (e.g. `"<type: object>"`).
  - When the input is NOT a 2-element array (e.g. `null`, `undefined`, a non-array value, or an array whose length is not 2), `width` and `height` MUST both be set to `"<unavailable>"`, and an additional key `returned=<returned>` MUST be appended to the message.

- In `returned=<returned>`:
  - If the value is an array whose length is not 2, `returned` MUST be `"[length: " + value.length + "]"`.
  - If the value is `null`, `returned` MUST be `"null"`.
  - If the value is `undefined`, `returned` MUST be `"undefined"`.
  - For all other non-array values, `returned` MUST be `"<type: " + typeof value + ">"` (for example, `"<type: number>"`, `"<type: string>"`, `"<type: object>"`).

- Legacy error compatibility:
  - To maintain compatibility with callers and tests expecting legacy error text, a legacy suffix `; legacy=<legacy message>` MUST be appended to `constant-node-size` and `invalid-callback-node-size` errors:
    - For `constant-node-size`, the legacy message MUST include the phrase `"must be positive"` or `"all node sizes must be positive"`.
    - For `invalid-callback-node-size`, the legacy message MUST include the phrase `"all node sizes must be positive"`.
  - For `node-size-callback-threw`:
    - The wrapper `Error` message MUST ONLY contain the four fields `category`, `node`, `width`, and `height`:
      `category=node-size-callback-threw; node=<node>; width=<unavailable>; height=<unavailable>`
    - A legacy suffix (`; legacy=...`) MUST NOT be appended under any circumstances (even if the raw thrown exception message contains phrases like `"all node sizes must be positive"`).
    - The wrapper `Error` MUST preserve the original thrown exception on its `cause` property (`error.cause`).

- The three layout operators (`sugiyama`, `zherebko`, and `grid`) MUST expose equivalent error semantics and consistent validation messaging for equivalent invalid dimension inputs.

## constraints

1. Changes MUST be strictly confined to unifying node dimension validation, resolution, and per-layout reuse:
   - **Allowed modification paths**:
     - `src/layout.ts`
     - `src/sugiyama/index.ts`
     - `src/zherebko/index.ts`
     - `src/grid/index.ts`
     - `src/tweaks.ts`
     - New internal helper modules under `src/` directly required for unified dimension resolution.
     - Any newly created independent test files under `src/` (e.g., `src/*.test.ts`) created to verify dimension resolution.
   - **Prohibited modification paths**:
     - Any existing test files (`src/**/*.test.ts` present in the baseline repository, including `src/layout.test.ts`, `src/sugiyama/index.test.ts`, `src/zherebko/index.test.ts`, `src/grid/index.test.ts`, etc.). Modifying existing test files is strictly prohibited; evaluation will fail if existing test files are altered.
     - Any other existing source files under `src/` not in the allowed modification paths (including `src/graph/**`, `src/dagre.ts`, `src/collections.ts`, `src/iters.ts`, `src/index.ts`, and sub-operator modules under `src/sugiyama/**` other than `src/sugiyama/index.ts`, `src/grid/lane/**`, etc.).
     - Protected test utilities and helpers (`src/test-graphs.ts`, `src/test-utils.ts`, `src/**/test-utils.ts`).
     - Build and runtime configurations (`package.json`, `tsconfig*.json`, `biome.json`, `bunfig*.toml`, `bun.lock*`).
     - Evaluation suites and platform directories (`tests/`, `case/`, `.github/`).
2. The refactoring MUST NOT alter graph data structures, graph mutation behaviors, graph query utilities, or dagre interoperability helpers.
3. Cyclic graph handling is outside the scope of this refactoring; existing dag/cycle validation remains unchanged.
4. The refactoring MUST NOT rename, remove, or change the signatures of existing public methods, types, or exported functions on `sugiyama`, `zherebko`, `grid`, or `./layout.js`.
5. Layout calculations for valid graphs with constant dimensions or deterministic callback dimensions MUST NOT exhibit any geometric drift or coordinate regression.
6. Sequential layout executions and nested layout executions MUST NOT contaminate each other or leak cached dimensions between distinct layout runs.
7. The solution MUST NOT introduce new external runtime dependencies or modify package configuration files.
8. TypeScript generic type inference for node and link data across operator builder chains MUST remain intact.
9. The implementation MUST NOT swallow callback exceptions or weaken existing dimension validation checks.
10. All changes MUST satisfy existing project quality standards, ensuring both `bun run lint:ts` (or `tsc`) and `bun run lint:es` (or `biome check`) pass without errors.

IMPORTANT: Create a new branch from the task's base commit `67d5447722eff38482a5bc5b5eed5f4229d2f80b` and commit all task changes, including new files, when you are done.
