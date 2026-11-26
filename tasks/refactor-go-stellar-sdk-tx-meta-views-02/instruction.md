## Background
Transaction metadata is versioned, and its version is currently re-inspected independently in many places: transaction-level change assembly, per-operation change lookup, contract, diagnostic and transaction event extraction, and soroban fee-refund accounting each branch on the metadata generation on their own. This duplicates domain knowledge across callers and layers, mixes generation dispatch with unrelated responsibilities, and makes every metadata-generation adjustment a cross-cutting change in which paths can silently drift apart. The per-generation differences should be consolidated behind one internal view so each supported generation is described once, while the capabilities and observable results consumers rely on today remain exactly as they are.

## Goal
- Replace the scattered generation conditionals around decoded transaction metadata with one internal view whose per-generation handling owns the differences in changes, operation changes, events and fee-refund inputs.
- Keep every supported generation's observable results identical, including ordering, grouping, absence versus error outcomes, and refund values.
- Remove the need for downstream event consumers to re-derive metadata layout from the raw version field, while leaving their generation-specific event interpretation unchanged.
- Achieve this without adding new dependencies or reversing the existing dependency direction between packages.

## Public contract to preserve
- Change assembly: `LedgerTransaction.GetChanges() ([]Change, error)` and `LedgerTransaction.GetOperationChanges(operationIndex uint32) ([]Change, error)` keep their signatures, parameters, ordering and empty/error outcomes.
- Events: `LedgerTransaction.GetTransactionEvents() (TransactionEvents, error)` keeps its signature, and the exported `TransactionEvents` value keeps its three fields: top-level transaction events, per-operation contract-event groups, and diagnostic events.
- Event accessors: `GetContractEvents() ([]xdr.ContractEvent, error)`, `GetContractEventsForOperation(opIndex uint32) ([]xdr.ContractEvent, error)` and `GetDiagnosticEvents() ([]xdr.DiagnosticEvent, error)` on the transaction type, plus the equivalent exported accessors on `xdr.TransactionMeta` returning `[]ContractEvent`, `[]DiagnosticEvent` and `[]TransactionEvent`, keep their signatures, per-generation outcomes and unsupported-generation errors.
- Fee refunds: `SorobanResourceFeeRefund() int64` and `GetPostApplyFeeChanges() []Change` keep their signatures and value and classification semantics.
- Unified-events flag: the token-transfer event processor keeps its exported option that enables reading from the unified event stream; with that option enabled generation-4 metadata remains the only accepted generation and other generations still fail with an error.
- Internal helpers, including per-generation wrappers, the consolidated view and any dispatch helpers, are free to be introduced, renamed, replaced or removed; only the exported capabilities and behaviors above are contractual.

## Behavior that must stay unchanged
- `GetChanges` MUST preserve per-generation composition and order: generation 1 returns transaction-wide changes followed by operation changes; generations 2 and 3 return leading transaction changes, then operation changes in index order, then trailing transaction changes; generation 4 keeps that shape with its own per-operation change representation.
- When a transaction failed with an internal error on ledger version 12 or lower, `GetChanges` MUST return only the leading transaction changes, and `GetOperationChanges` MUST return an empty change set with no error.
- `GetOperationChanges` MUST return an empty result without error for an index beyond the recorded operations, and MUST return an empty result with the existing error for unsupported generations, including generation 0.
- `GetTransactionEvents` MUST return no events for generations 1 and 2; for generation 3 it MUST return events only for a soroban transaction, as a single operation group at index 0 plus diagnostic events; for generation 4 it MUST populate top-level transaction events, one operation group per recorded operation in order, and top-level diagnostic events.
- The metadata-level event accessors MUST keep their absent-event outcomes: nothing for generations 1 and 2, and for transaction events also generation 3; nothing when a generation-3 soroban metadata section is missing; and nothing for generation-4 metadata with an empty operation list rather than an index failure; unknown generations MUST produce the existing unsupported-generation error.
- `SorobanResourceFeeRefund` MUST return zero for non-soroban transactions, MUST derive the refund from the trailing transaction changes followed by post-apply fee changes, and MUST NOT return a value for a soroban transaction whose metadata generation is neither 3 nor 4.
- Returned change values MUST keep their existing classification and associations (reason, operation index, transaction and ledger references), and exported result shapes MUST NOT change.
- Generation-3 and generation-4 contract-event interpretation in the token-transfer event pipeline MUST remain distinct, with each generation's acceptance rules and error outcomes preserved.
- The unified-events path MUST accept exactly generation-4 metadata and MUST fail with an error for any other generation.

## constraints
1. No behavior drift: results, ordering, grouping, and error or panic outcomes must remain identical for every supported generation, and no capability may be removed or reduced.
2. No dependency expansion: introduce no new module dependency and no dependency from a lower-level data package onto an ingest or processing package; the consolidated handling must be usable at the level where both the metadata accessors and the transaction readers can reach it.
3. No unrelated changes: do not rename, reshape or repurpose exported APIs, result types, error values or flags beyond what the consolidation strictly requires.
4. The existing raw-view event walk that already centralizes generation dispatch in one place is out of scope; it must not be split, bypassed or rerouted through the consolidated view.
5. Scope: restrict edits to the production code, tests and supporting adjustments necessary to consolidate generation dispatch for decoded metadata, and exclude unrelated refactors, cleanups or reorganizations.

IMPORTANT: Please work on this in a new branch from main and commit everything when you are done.