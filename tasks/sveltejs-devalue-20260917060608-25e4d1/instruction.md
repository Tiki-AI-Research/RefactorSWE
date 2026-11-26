# Refactor Deserialization State and Dispatch Handling

## Problem
Deserialization must preserve its existing public behavior and reject the malformed inputs listed under "Safety compatibility exceptions" with the exact errors specified there. The evaluated contract includes both observable behavior and the structural acceptance requirements described in this document: the public API, identity and topology preservation, custom reviver lifecycle and cycle detection, the safety exceptions, the preserved legacy errors, and the required separation of per-call hydration state from tag/container dispatch. The task remains a refactoring task: reorganizing parsing and hydration for maintainability is required, while names, helper boundaries, and module layout remain free to the implementer as long as the structural acceptance requirements are met.

## API Contract
- `unflatten`: Accepts a flattened payload array along with optional custom revivers or parser options, and returns the reconstructed JavaScript value.
- `parse`: Accepts a serialized payload string along with optional custom revivers or parser options, and returns the reconstructed JavaScript value.
- Internal helper routines, deserialization state handling, and dispatch logic may be freely introduced, refactored, or encapsulated, provided no internal implementation details leak into the public interface.

## Behavior
- **MUST preserve cyclic reference identities and duplicate reference equality**: Reconstructed containers (such as plain objects, regular arrays, sparse arrays, sets, and maps), circular references, duplicate references, and self-referential structures MUST retain exact reference equality and topology upon reconstruction.
- **MUST maintain custom reviver lifecycle and cycle detection**: Custom revivers MUST correctly process both raw values and serialized payload entries. When resolving previously deserialized references, revivers MUST reuse the resolved reference instance; when encountering an unresolved cyclical dependency during custom reviver execution, deserialization MUST throw an Error with the message `Invalid circular reference`.
- **MUST enforce sparse array and payload safety constraints**: Deserialization of sparse array payloads MUST reject invalid declared lengths and out-of-bounds indices exceeding numerical limits. Payloads containing forbidden property keys such as `__proto__`, invalid typed array or ArrayBuffer declarations, or malformed payload indices MUST be rejected by throwing an Error with the message `Invalid input`.

## Structural acceptance requirements
- Hydration MUST use an explicit per-call state owner, such as a context object, state object, class instance, or factory-created state container. That owner MUST hold the payload table, resolved-reference cache, custom revivers, parser operations, and circular-reference tracking for a single parse/unflatten call.
- `parse` and `unflatten` MUST delegate hydration work instead of keeping all state tracking, reference resolution, tag dispatch, sparse-array handling, and container population inside one monolithic closure. `unflatten` MUST NOT define nested hydration functions or closures inside its body; hydration must be delegated through the per-call state owner and independently reachable routines or methods.
- Built-in tag handling, sparse-array validation/population, regular array/object population, Set/Map population, null-prototype object population, and custom reviver handling MUST be separated across at least six non-empty helper routines or methods that are reachable from `unflatten`. The exact helper names and module placement are free, but these responsibilities must be mechanically separable in the implementation.
- The change scope MUST stay limited to parsing and hydration production code. The repository's existing test files remain frozen; compatibility exceptions are validated by independent contract tests rather than by modifying upstream tests.

## Safety compatibility exceptions
The following changes intentionally take priority over legacy invalid-input behavior. Each MUST throw an ordinary `Error` whose message is exactly `Invalid input`:

1. A `__proto__` property in a plain-object or null-prototype-object payload, including nested occurrences.
2. A typed-array/DataView payload whose buffer reference is missing, is not a valid table index, or does not refer to an `ArrayBuffer`-tagged payload.
3. An `ArrayBuffer`-tagged payload whose encoding is missing or is not a string.
4. A payload reference that is nonnumeric, nonintegral, nonfinite, negative other than a supported primitive sentinel, or outside the available table and resolved cache. This includes fractional references that previously produced `undefined`. Array holes and primitive sentinels retain their existing supported meanings.

5. Boundary combinations that mix malformed references with nested containers or sparse-array metadata MUST be rejected with `Invalid input`; valid primitive sentinels and array holes remain accepted.

6. A custom reviver MUST NOT be able to bypass sparse-array declared-length or index validation by mutating the payload table during hydration. The final result MUST still reject an index outside the declared length with `Invalid input`.

## Preserved legacy errors
The following behavior is outside the safety exceptions and MUST remain unchanged:

- `unflatten([["Object", 1], null])` MUST continue to throw the native `TypeError` produced by the existing implementation. It MUST NOT be silently accepted or normalized to `Invalid input`.
- Native errors from view constructors, including a misaligned typed-array offset, MUST be propagated unchanged.
- Errors thrown by custom operation callbacks MUST preserve their original error object and type.
- Unknown tags, custom revivers, decoding string encodings, and JSON syntax errors MUST retain their existing error behavior.

Custom revivers and operations MUST retain their precedence and may use opaque handles. In particular, implementations MUST NOT wrap every exception in a generic input error.

Already resolved references MUST still be reused if a custom reviver shortens the input table; this does not make an unresolved invalid reference valid.

The original repository test files remain frozen. Safety changes may be checked with independent contract tests; any legacy assertions that conflict with an explicitly listed safety exception are documented as compatibility exceptions rather than by modifying repository tests.

## Constraints
1. Except for the explicitly listed safety changes, no behavioral drift or public API degradation is permitted across standard, circular, or custom-revived payloads.
2. Independent and reentrant deserialization calls MUST NOT interfere with one another. Implementations MUST NOT introduce shared mutable deserialization state, ambient call contexts, or external dependencies.
3. Modifications MUST be strictly limited to the parsing and hydration logic; the repository's existing test files are frozen.
4. All existing error types, error messages, and rejection behaviors outside the explicitly listed safety changes MUST remain identical.
5. Internal reorganization MUST NOT alter observable deserialization output, reference graphs, or cyclical identity guarantees.
