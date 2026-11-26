# Adversarial patches and verification points

Task: refactor-go-stellar-sdk-tx-meta-views-02
Base commit: d8c8acf5f56cae47fcf033522349565c6fc86764

This package contains 38 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-0a5574fa3486.patch)
SHA-256: 0a5574fa3486d1a01d95dcf53012486046cc2d66e58f976b7cb5f6f8bf43e61e

### VP-0001: Targeted regression: DiagnosticEvents comes from the V4 top level, and is not lost due to non-Soroban or empty operation lists.

- **requirement**: DiagnosticEvents comes from the V4 top level, and is not lost due to non-Soroban or empty operation lists.
- **mutation**: Targeted regression: DiagnosticEvents comes from the V4 top level, and is not lost due to non-Soroban or empty operation lists. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0002

[patch](patches/P-0002-0b47f8b610e3.patch)
SHA-256: 0b47f8b610e3c2170e420f4759cca9a29e0f2f74fdbc87347c00a8e1c4e534b9

### VP-0002: Targeted regression: Common operation intergeneration processing for two read entries reuse

- **requirement**: Common operation intergeneration processing for two read entries reuse
- **mutation**: Targeted regression: Common operation intergeneration processing for two read entries reuse (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0004

[patch](patches/P-0004-1b5d1dfea081.patch)
SHA-256: 1b5d1dfea0811f0e12a8271c4564ae9ba2e109d05d424aba6a76b455da2e5993

### VP-0004: Targeted regression: V3 returns its events by default or ignores the index.

- **requirement**: V3 returns its events by default or ignores the index; V4 returns nil for zero operations, and specifies a group for operations; unknown generation-related errors.
- **mutation**: Targeted regression: V3 returns its events by default or ignores the index. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0006

[patch](patches/P-0006-2136b84e8b23.patch)
SHA-256: 2136b84e8b232ee0753ef7fc226386167fe1b882c32743bbdb9dbb4d6e0590ac

### VP-0006: Targeted regression: Do not return a substitute value.

- **requirement**: Do not return a substitute value.
- **mutation**: Targeted regression: Do not return a substitute value. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0007

[patch](patches/P-0007-2d2f356a1326.patch)
SHA-256: 2d2f356a1326d0d6fc1acc474b634f59128b225fb5b1ec1520b23f586410738b

### VP-0007: Targeted regression: The production call graph and reads of generation-specific fields must show that the shared view supplies transaction-level changes.

- **requirement**: The production call relationships and inter-generation field reading proofs for transaction-level changes are provided by the common view; private names are not required.
- **mutation**: Targeted regression: The production call graph and reads of generation-specific fields must show that the shared view supplies transaction-level changes. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0008

[patch](patches/P-0008-364a5c4ab5dd.patch)
SHA-256: 364a5c4ab5ddab7705a8018a217c97a5127a191e3ed4a57184e0bfadf9d568e9

### VP-0008: Targeted regression: V0-specific errors, general unknown generation errors, and empty slices are consistent with the original early exit order.

- **requirement**: V0-specific errors, general unknown generation errors, and empty slices are consistent with the original early exit order.
- **mutation**: Targeted regression: V0-specific errors, general unknown generation errors, and empty slices are consistent with the original early exit order. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0009

[patch](patches/P-0009-3ac091fa7ea0.patch)
SHA-256: 3ac091fa7ea08185b5227d842b268768c04692a341e997e4a7bfcd5f2e421398

### VP-0009: Targeted regression: Return 0 for non-Soroban cases.

- **requirement**: Not Soroban 0; No deduction or other account charges
- **mutation**: Targeted regression: Return 0 for non-Soroban cases. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0010

[patch](patches/P-0010-4aed53e56592.patch)
SHA-256: 4aed53e56592ebd02877a9957fce01253b8f2814eb85c853b5f0bf93c17a8379

### VP-0010: Targeted regression: Preserve the converted content, ReasonFeeRefund, Transaction=t, and Ledger=&t.Ledger.

- **requirement**: Preserve the converted content, ReasonFeeRefund, Transaction=t, and Ledger=&t.Ledger.
- **mutation**: Targeted regression: Preserve the converted content, ReasonFeeRefund, Transaction=t, and Ledger=&t.Ledger. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0011

[patch](patches/P-0011-4b65826134bd.patch)
SHA-256: 4b65826134bd343161c9fdfe208cc728781f96afa0e2e60990d802252c218aa5

### VP-0011: Targeted regression: LedgerVersion<=12 and only internal errors return leading changes

- **requirement**: LedgerVersion<=12 and only leading changes are returned for internal errors; for version 13, no truncation occurs.
- **mutation**: Targeted regression: LedgerVersion<=12 and only internal errors return leading changes (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0012

[patch](patches/P-0012-4d78a6436a3b.patch)
SHA-256: 4d78a6436a3bcf1d7b79f14bdcd79de4e1ded55f7a25261d0fea00bc11fbe2af

### VP-0012: Targeted regression: Even if SorobanMeta is missing, there is still an empty group.

- **requirement**: Even if SorobanMeta is missing, there is still an empty group; no top-level transaction events
- **mutation**: Targeted regression: Even if SorobanMeta is missing, there is still an empty group. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0013

[patch](patches/P-0013-5721dc3b96df.patch)
SHA-256: 5721dc3b96df28ebb2d2b87b44d6c243d37e12f0f32b02fe979984ed7c6d3f6f

### VP-0013: Targeted regression: V4: No admin layout, map amount/muxed support, and acceptance/filter results remain unchanged. No modifications to V3 interpretation are applied.

- **requirement**: V4: No admin layout, map amount/muxed support, and acceptance/filter results remain unchanged. No modifications to V3 interpretation are applied.
- **mutation**: Targeted regression: V4: No admin layout, map amount/muxed support, and acceptance/filter results remain unchanged. No modifications to V3 interpretation are applied. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0014

[patch](patches/P-0014-57f94cf8157e.patch)
SHA-256: 57f94cf8157e3eeeda8ef1d6fe29d690c63d8b9858abc93405d052d20f61b6b0

### VP-0014: Targeted regression: The number and order of OperationEvents groups are equal to Operations. Empty operation groups and zero operation shapes are retained.

- **requirement**: The number and order of OperationEvents groups are equal to Operations. Empty operation groups and zero operation shapes are retained.
- **mutation**: Targeted regression: The number and order of OperationEvents groups are equal to Operations. Empty operation groups and zero operation shapes are retained. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0015

[patch](patches/P-0015-5e9c8b836ffb.patch)
SHA-256: 5e9c8b836ffb9a7372122ca1e693cd6759b7ce0d45e164e0b4b3916f63f39c87

### VP-0015: V0 Trading Change Error Text Deviation Compatibility Contract

- **requirement**: V0 Transaction Change Error Text Deviation Compatibility Contract (Violation of the Original Task's Behavior Requirements)
- **mutation**: V0 Trading Change Error Text Deviation Compatibility Contract
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry must be effectively rejected; an ineffective execution cannot be considered a success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0016

[patch](patches/P-0016-647d9ac11572.patch)
SHA-256: 647d9ac115723d47a5dd55bdecbdce5f079d94aee70e2f5307ad92a7a50df177

### VP-0016: Targeted regression: Contract, diagnosis, and the selection of intergenerational fields for top-level events are handled together.

- **requirement**: Contract, diagnostics, and the selection of inter-generation fields for top-level events are handled jointly; not each accessor has a complete layout distribution.
- **mutation**: Targeted regression: Contract, diagnosis, and the selection of intergenerational fields for top-level events are handled together. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0017

[patch](patches/P-0017-668c745fa8f8.patch)
SHA-256: 668c745fa8f8e67cbd78494210cd66b3572b77db9d9460b599b5eaed03706a8f

### VP-0017: Targeted regression: For a classic transaction, return nil and the error message "not a soroban transaction".

- **requirement**: Classic transaction is nil or not a soroban transaction; Soroban read operation 0 and retains the underlying result and error.
- **mutation**: Targeted regression: For a classic transaction, return nil and the error message "not a soroban transaction". (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0018

[patch](patches/P-0018-66be3638dac1.patch)
SHA-256: 66be3638dac161da0fe935ea116790f3ef13d363fa848012a20019bacd96b732

### VP-0018: Targeted regression: Downstream acquisition operations, operation quantities, and top-level events do not depend on the original version's field unpacking layout.

- **requirement**: Downstream acquisition operation events, operation quantities, and top-level events do not depend on the original version field unpacking layout; semantic distinctions are allowed to be retained.
- **mutation**: Targeted regression: Downstream acquisition operations, operation quantities, and top-level events do not depend on the original version's field unpacking layout. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0019

[patch](patches/P-0019-6a5b2503bc8e.patch)
SHA-256: 6a5b2503bc8e5a5108643df8cfa1729b6fa029371800061cb0c6d168f66f6d00

### VP-0019: Targeted regression: When starting > ending in the valid refund generation, there is a panic due to Invalid Soroban Resource Refund. No negative refund or 0 is returned.

- **requirement**: When starting > ending in the valid refund generation, there is a panic due to Invalid Soroban Resource Refund. No negative refund or 0 is returned.
- **mutation**: Targeted regression: When starting > ending in the valid refund generation, there is a panic due to Invalid Soroban Resource Refund. No negative refund or 0 is returned. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0020

[patch](patches/P-0020-78a7ade9315b.patch)
SHA-256: 78a7ade9315b12fc3b75940f7ad1a0cd844e826b545ec4ccc18ca1db345c9319

### VP-0020: Targeted regression: Support returning a non-nil empty slice or nil error when LedgerVersion is <= 12 in the current generation and there is an internal error.

- **requirement**: Support returning a non-nil empty slice and nil error when LedgerVersion is <= 12 and there are internal errors; no early leave for cases where LedgerVersion is 13.
- **mutation**: Targeted regression: Support returning a non-nil empty slice or nil error when LedgerVersion is <= 12 in the current generation and there is an internal error. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0021

[patch](patches/P-0021-80edf0df9816.patch)
SHA-256: 80edf0df98168fbb59dcbf1853ceec92136deb26932545fb808c6f4b394d28ab

### VP-0021: Targeted regression: Support returning a non-nil empty slice or nil error when the inter-generation index exceeds the recorded operations.

- **requirement**: Support returning a non-nil empty slice or nil error when the inter-generation index exceeds the recorded operations.
- **mutation**: Targeted regression: Support returning a non-nil empty slice or nil error when the inter-generation index exceeds the recorded operations. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0022

[patch](patches/P-0022-820164343466.patch)
SHA-256: 8201643434660526427868541edf18c92a2dc62dd00b5b6e91639f9a5a3a2d7b

### VP-0022: Targeted regression: V0 or unknown generation returns zero values for TransactionEvents, and there is an error with the existing unsupported TransactionMeta version.

- **requirement**: V0 or unknown generation returns zero values for TransactionEvents, and there is an error with the existing unsupported TransactionMeta version.
- **mutation**: Targeted regression: V0 or unknown generation returns zero values for TransactionEvents, and there is an error with the existing unsupported TransactionMeta version. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0023

[patch](patches/P-0023-84b9344b07ce.patch)
SHA-256: 84b9344b07cebced0f36becb3b98c3466561063bc49148ae017ba82ae9b65277

### VP-0023: Targeted regression: The feature is off by default. Once enabled through the public API, V4 reads fees and operation events by the existing rules. Non-V4 inputs return the original error.

- **requirement**: The feature is off by default. Once enabled through the public API, V4 reads fees and operation events by the existing rules. Non-V4 inputs return the original error.
- **mutation**: Targeted regression: The feature is off by default. Once enabled through the public API, V4 reads fees and operation events by the existing rules. Non-V4 inputs return the original error. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0024

[patch](patches/P-0024-f4339085fb94.patch)
SHA-256: f4339085fb9486e98ac99d6c19cb2cca065d5e788cf066188f159aa2efd772e8

### VP-0024: V3 post-trade changes are discarded

- **requirement**: V3 post-trade changes are discarded (violating the requirement of maintaining the original task behavior)
- **mutation**: V3 post-trade changes are discarded
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry must be effectively rejected; an ineffective execution cannot be considered a success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Non-target compilation/collection errors; Uncertain baseline

## P-0025

[patch](patches/P-0025-9323d0baa134.patch)
SHA-256: 9323d0baa134a648ef943bce8a0483a8d4868350ee5210cc245d4c681628e89f

### VP-0025: Targeted change: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, p

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **mutation**: Targeted changes to ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0026

[patch](patches/P-0026-96e1df8772c1.patch)
SHA-256: 96e1df8772c1acebc979e513843970d1078cba1b24bad6a88918a0f460fb4f96

### VP-0026: select operation1 with distinct balances

- **requirement**: Support various generations to return changes for specified index operations, without mixing in other operations and transaction segments.
- **mutation**: select operation1 with distinct balances (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0027

[patch](patches/P-0027-9cafd81f9504.patch)
SHA-256: 9cafd81f950460d6993de1d1c3b263955ea87c93922b161fc3f2d6dd5af70a63

### VP-0027: Targeted regression: Reason, OperationIndex, Transaction and Ledger references, as well as Pre/Post and ChangeType, correspond to the original changes.

- **requirement**: Reason, OperationIndex, Transaction and Ledger references, as well as Pre/Post and ChangeType, correspond to the original changes.
- **mutation**: Targeted regression: Reason, OperationIndex, Transaction and Ledger references, as well as Pre/Post and ChangeType, correspond to the original changes. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0028

[patch](patches/P-0028-9dfbe45051c5.patch)
SHA-256: 9dfbe45051c55f59decc15ea9afd8622ed6cc9d049393db9bfeaec17ac2f874a

### VP-0028: Targeted change: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, p

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **mutation**: Targeted changes to ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0029

[patch](patches/P-0029-00d51ff31976.patch)
SHA-256: 00d51ff3197613e17723ae25aa0c1cff0502e47eb3b5a7397482f16fbcce145f

### VP-0029: V4 Top-Level Trading Event Accessor Returns Nil

- **requirement**: The V4 top-level transaction event accessor returned nil (violating the requirements of the original task retention behavior).
- **mutation**: V4 Top-Level Trading Event Accessor Returns Nil
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry must be effectively rejected; an ineffective execution cannot be considered a success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

### VP-0030: V4 Top-Level Trading Event Accessor Returns Nil

- **requirement**: The V4 top-level transaction event accessor returned nil (violating the requirements of the original task retention behavior).
- **mutation**: V4 Top-Level Trading Event Accessor Returns Nil
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry must be effectively rejected; an ineffective execution cannot be considered a success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0030

[patch](patches/P-0030-af4eee0b7209.patch)
SHA-256: af4eee0b7209028b2d5d3646914918be8533d64b1f0925c78d9dfc3623a490eb

### VP-0031: Targeted regression: After the V1 transaction segment, comes the operation segment.

- **requirement**: V1 transaction segment followed by an operation segment; refers to before, changes based on the operation index, after; content and sequence within the segment are equal to the baseline.
- **mutation**: Targeted regression: After the V1 transaction segment, comes the operation segment. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0031

[patch](patches/P-0031-b086f9d078a7.patch)
SHA-256: b086f9d078a74add1c1958208be51816a8bee041ee1738acf9a9ed4030f60af1

### VP-0032: Targeted regression: The raw call chain is not split, bypassed, or rerouted through a new decoding view.

- **requirement**: The raw call chain is not split, bypassed, or rerouted through a new decoding view.
- **mutation**: Targeted regression: The raw call chain is not split, bypassed, or rerouted through a new decoding view. (changed files: ingest/ledger_transaction.go, ingest/transaction_events_view.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0032

[patch](patches/P-0032-b8c934cafb9a.patch)
SHA-256: b8c934cafb9acbb33f8ccec3f8764126571f6ea557d066b4658269e9fee65423

### VP-0033: Targeted regression: nil,nil

- **requirement**: Return nil,nil and preserve the original error for an unknown generation.
- **mutation**: Targeted regression: nil,nil (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0033

[patch](patches/P-0033-bd948096e132.patch)
SHA-256: bd948096e132515dcd48fad0e69a249bf6ac454a5d76dd9d7ed815db7294432c

### VP-0034: Targeted regression: Empty operation list unclear clearing diagnosis

- **requirement**: Empty operation list unclear clearing diagnosis
- **mutation**: Targeted regression: Empty operation list unclear clearing diagnosis (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0034

[patch](patches/P-0034-bfa1c74c8cc5.patch)
SHA-256: bfa1c74c8cc593c9bf12755873cfd68b14d735d589f191ee717b560ee06908c3

### VP-0035: Targeted regression: The module list did not introduce any new modules due to the refactoring.

- **requirement**: The module list did not introduce any new modules due to the refactoring.
- **mutation**: Targeted regression: The module list did not introduce any new modules due to the refactoring. (changed files: go.mod, ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0035

[patch](patches/P-0035-cb69bc9b78ac.patch)
SHA-256: cb69bc9b78ac6ca5ebfd6c28bf7909c9a04a896f5078404b9ace0622584d2431

### VP-0036: Targeted change: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, p

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **mutation**: Targeted changes to ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

### VP-0037: Targeted regression: V4: No admin layout, map amount/muxed support, and acceptance/filter results remain unchanged. No modifications to V3 interpretation are applied.

- **requirement**: V4: No admin layout, map amount/muxed support, and acceptance/filter results remain unchanged. No modifications to V3 interpretation are applied.
- **mutation**: Targeted regression: V4: No admin layout, map amount/muxed support, and acceptance/filter results remain unchanged. No modifications to V3 interpretation are applied. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0036

[patch](patches/P-0036-d2a4e808ca04.patch)
SHA-256: d2a4e808ca045d2c43d47ae09cd7c32692126d50116cf5f3ba75fa58cd93b91e

### VP-0038: Targeted change: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, p

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **mutation**: Targeted changes to ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0037

[patch](patches/P-0037-d546859bb3b9.patch)
SHA-256: d546859bb3b95c488b9c4c6cb958157704eaafb273ed62f180ea75a72da7f661

### VP-0039: Targeted regression: V0 and unknown generations' nil slices, error texts are consistent with the baseline.

- **requirement**: V0 and unknown generations' nil slices, error texts are consistent with the baseline.
- **mutation**: Targeted regression: V0 and unknown generations' nil slices, error texts are consistent with the baseline. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0039

[patch](patches/P-0039-d9f643847c25.patch)
SHA-256: d9f643847c25f24a8fad7325166603b62cbdd263b0d66e75b71f8db984bedf26

### VP-0041: Targeted regression: No further unpacking at the calculation layer

- **requirement**: No further unpacking at the calculation layer
- **mutation**: Targeted regression: No further unpacking at the calculation layer (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0040

[patch](patches/P-0040-dfb20a42f400.patch)
SHA-256: dfb20a42f400435c80b7f2ce301ace037d63229e8bf8ed10de9a09b21ead58ec

### VP-0042: Targeted regression: When the SorobanMeta is missing, it is nil.

- **requirement**: When the SorobanMeta is missing, it is nil.
- **mutation**: Targeted regression: When the SorobanMeta is missing, it is nil. (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

## P-0041

[patch](patches/P-0041-ebb9c5067dcc.patch)
SHA-256: ebb9c5067dcc267b6f8c76aa3b5fa73c9dc1a9ed05e272e634161dec321e4f96

### VP-0043: Targeted change: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, p

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **mutation**: Targeted changes to ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others (changed files: ingest/ledger_transaction.go, processors/token_transfer/contract_events.go, processors/token_transfer/token_transfer_processor.go, xdr/transaction_meta.go, among others)
- **setup**: Apply this patch to the clean baseline at d8c8acf5f56c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unrelated compilation or test collection error; No observation of the target behavior was recorded

