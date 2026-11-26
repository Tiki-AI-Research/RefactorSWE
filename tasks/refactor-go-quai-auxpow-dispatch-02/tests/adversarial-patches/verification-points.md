# Adversarial patches and verification points

Task: refactor-go-quai-auxpow-dispatch-02
Base commit: 208b67554a9078086c8de7c9ab0a9b5af2d9d567

This package contains 28 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-06d42c6cc51a.patch)
SHA-256: 06d42c6cc51a4667aff33f9737b3a2659d3e9420d93b7385637f835348acba6f

### VP-0001: Unknown transaction hash returns non-zero

- **requirement**: Other identifiers transaction hash is zero
- **mutation**: Unknown transaction hash returns non-zero (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0002

[patch](patches/P-0002-1b1451d46b0d.patch)
SHA-256: 1b1451d46b0de960f3653b2dfc7cc3043fe28ab1498a8cf3a0024166dfae3ae2

### VP-0002: Targeted regression: JSON header decoding uses a unified chain mapping and delegates the existing headers Deserialize

- **requirement**: JSON header decoding uses a unified chain mapping and delegates the existing headers Deserialize
- **mutation**: Targeted regression: JSON header decoding uses a unified chain mapping and delegates the existing headers Deserialize (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0003

[patch](patches/P-0003-26548b2ef0a9.patch)
SHA-256: 26548b2ef0a9ab9765cbb71d621fb4a87e7ef786881973b0104c78551f3abeb4

### VP-0003: JSON will be submitted with the ID only after successful decoding. Keep the correct chain of options.

- **requirement**: JSON header decoding failed and still records the input identifier.
- **mutation**: JSON will be submitted with the ID only after successful decoding. Keep the correct chain of options. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0004

[patch](patches/P-0004-26895b262d1b.patch)
SHA-256: 26895b262d1b8d9b1d221c099c110144d781d59e1835bfb91765aaa1bce2e6eb

### VP-0004: Add new export aliases to maintain behavior during runtime.

- **requirement**: The refactoring is carried out with existing header abstractions as the seams, without establishing parallel dispatch type hierarchies or adding new common types/APIs.
- **mutation**: Add new export aliases to maintain behavior during runtime. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0005

[patch](patches/P-0005-07594c4150be.patch)
SHA-256: 07594c4150be96e86ffa967fd1ca67c4dd8410d5d7e314a9eb66b116519d1f4b

### VP-0005: Scrypt construction error increases the bits parameter

- **requirement**: The Scrypt construction must ensure that the incoming block header is exactly consistent in bits and bytes.
- **mutation**: Scrypt construction error increases the bits parameter
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal testing resulted in a valid rejection, the behavior assertion or routing contract check failed; failure to build or execute does not count as success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0006

[patch](patches/P-0006-520c74c6f3cb.patch)
SHA-256: 520c74c6f3cbe4f5d7f18b7826afb64b02223b4847853fa11d4aee6bc6c16a9e

### VP-0006: The ID is submitted only after the protobuf header is successfully decoded. The selection chain is still taken from this input.

- **requirement**: Even after a Protobuf error, this input identifier is still recorded.
- **mutation**: The ID is submitted only after the protobuf header is successfully decoded. The selection chain is still taken from this input. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0007

[patch](patches/P-0007-5c68efa47272.patch)
SHA-256: 5c68efa47272fd7b6b0d9ec1cc03087c762c24d771d53887cd3e3db36cd952a2

### VP-0007: Transaction hash error, reverse natural byte order

- **requirement**: Four support identifiers maintain a natural order for the original transaction bytes, with double SHA256.
- **mutation**: Transaction hash error, reverse natural byte order (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0008

[patch](patches/P-0008-64d20fd6e56a.patch)
SHA-256: 64d20fd6e56a5be6fd1c5af2ef85ca91da1aec7137040efaefc0151d3e23027d

### VP-0008: Targeted regression: Use the common chain mapping for construction. The chain type supplies default fields without repeating the initialization choice for four chains.

- **requirement**: Use the common chain mapping for construction. The chain type supplies default fields without repeating the initialization choice for four chains.
- **mutation**: Targeted regression: Use the common chain mapping for construction. The chain type supplies default fields without repeating the initialization choice for four chains. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0009

[patch](patches/P-0009-6c45b784742b.patch)
SHA-256: 6c45b784742bbcc89c30258edffb7f5fd3dc6cb26e9cc030fca1b5839068b357

### VP-0009: Nil protobuf input cleared receiver

- **requirement**: nil protobuf is returned when input is nil, and the entire receiver is retained.
- **mutation**: Nil protobuf input cleared receiver (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0010

[patch](patches/P-0010-6ddb7ba4153d.patch)
SHA-256: 6ddb7ba4153d7af73f52e38e354a65b0403d91776517ec80a15944c195e919c2

### VP-0010: Targeted regression: Dispatch transaction hashing through a common entry point to the existing chain-specific header implementation.

- **requirement**: Dispatch transaction hashing through a common entry point to the existing chain-specific header implementation.
- **mutation**: Targeted regression: Dispatch transaction hashing through a common entry point to the existing chain-specific header implementation. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0011

[patch](patches/P-0011-74ae90ba48b5.patch)
SHA-256: 74ae90ba48b58934299e81c34d9ec59dbdb08b9a46ec222fc13ce48c279c9393

### VP-0011: BTC registration construction ignores the provided nonce

- **requirement**: Constructors for all four supported chains preserve supplied fields and chain defaults.
- **mutation**: BTC registration construction ignores the provided nonce (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0012

[patch](patches/P-0012-7a148ab1639a.patch)
SHA-256: 7a148ab1639a518ac54a028465d319314abb49916b5497d40ed3313bdbe50763

### VP-0012: Unknown JSON returned, indicating an error instead of successful completion.

- **requirement**: The unknown powId does not set the header on a zero-value receiver and successfully fills in other valid fields.
- **mutation**: Unknown JSON returned, indicating an error instead of successful completion. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0013

[patch](patches/P-0013-7d04fcda7258.patch)
SHA-256: 7d04fcda7258d683e093076513c583a237e1045a34a3360f305a6873fc2e9145

### VP-0013: protobuf encoding lost transaction

- **requirement**: Four-chain protobuf AuxPow encoding/decoding retains the first byte and payload.
- **mutation**: protobuf encoding lost transaction (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0014

[patch](patches/P-0014-8d9b071454f8.patch)
SHA-256: 8d9b071454f8eecdaebe65bab89ffbb22e20a9226e90ec138dac2f221ceb20d0

### VP-0014: Clear existing headers whenprotobuf short header errors occur

- **requirement**: protobuf header errors do not replace old headers or overwrite subsequent payloads.
- **mutation**: Clear existing headers whenprotobuf short header errors occur (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0015

[patch](patches/P-0015-90ffdfcf02fb.patch)
SHA-256: 90ffdfcf02fbfbdcff0554f8189480092870546cb8354c7294ea55ca8890cbd9

### VP-0015: Targeted regression: Protobuf header decoding uses a unified chain mapping and delegates the existing headers to Deserialize.

- **requirement**: Protobuf header decoding uses a unified chain mapping and delegates the existing headers to Deserialize.
- **mutation**: Targeted regression: Protobuf header decoding uses a unified chain mapping and delegates the existing headers to Deserialize. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0016

[patch](patches/P-0016-94e3351c386e.patch)
SHA-256: 94e3351c386e8be16553699145c96f0a91c450896f6d914133166818f9459236

### VP-0016: JSON successfully decoded, clearing the transaction.

- **requirement**: Valid JSON for all four chains preserves the six fields and round-trips the header bytes.
- **mutation**: JSON successfully decoded, clearing the transaction. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0017

[patch](patches/P-0017-969e4d2fc737.patch)
SHA-256: 969e4d2fc737419752d76bd23026b7bf3a5459e4991b2ce56bb1d70a35a6e096

### VP-0017: Do not construct returning an empty wrapper instead of nil.

- **requirement**: The auxiliary header does not support identifier construction, returning nil.
- **mutation**: Do not construct returning an empty wrapper instead of nil. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0018

[patch](patches/P-0018-a3afc2fbb993.patch)
SHA-256: a3afc2fbb993d97df0237dde884460c9cd5f56173b4c5511b3d0ea04dbe158f9

### VP-0018: JSON header error replaced with general error, still does not panic

- **requirement**: Support chain short head serialization error without panic
- **mutation**: JSON header error replaced with general error, still does not panic (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0019

[patch](patches/P-0019-aab0d8842b8f.patch)
SHA-256: aab0d8842b8fc4af52b172693f0d251ba21c741880672de8323895626a203ee9

### VP-0019: BTC valid field accessor returns an error value

- **requirement**: Keep the original header layout for Serialize, Deserialize, and field access.
- **mutation**: BTC valid field accessor returns an error value (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0020

[patch](patches/P-0020-b12aee7d8092.patch)
SHA-256: b12aee7d80928847eaab523e6675241af81d2e507e7aa2f3f52f4105c51add06

### VP-0020: Theprotobuf short header error has been replaced by a general error.

- **requirement**: Support the propagation of protobuf short header errors in chains without panicking.
- **mutation**: Theprotobuf short header error has been replaced by a general error. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0021

[patch](patches/P-0021-ba5e3b5768e7.patch)
SHA-256: ba5e3b5768e74a2874f5fdac193e77b5bcbf6d42cc18e6a26c6a8affdcc9b84e

### VP-0021: Block Hash Byte Order Reversal

- **requirement**: BlockHash retains the chain algorithm and byte order. An empty inner value returns zero.
- **mutation**: Block Hash Byte Order Reversal (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0022

[patch](patches/P-0022-be4daa8f380c.patch)
SHA-256: be4daa8f380ccfe649a2ad7ae9606c8a7a3bd6f59d17e1a0e1faf33cdbbf8e5f

### VP-0022: Seal Hash Byte Order Reverse

- **requirement**: SealHash maintains the input boundaries, byte order, and other chain zero values of KAWPOW.
- **mutation**: Seal Hash Byte Order Reverse (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0023

[patch](patches/P-0023-d5ecb93aa564.patch)
SHA-256: d5ecb93aa56493b9a8ecafd502bd22c4d981e2d16986ff6e7198d1412c17b60d

### VP-0023: JSON should verify the header in advance of powId.

- **requirement**: Multiple illegal JSON cases occurred, including errors in outer decoding, required field decoding, and header decoding.
- **mutation**: JSON should verify the header in advance of powId. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0024

[patch](patches/P-0024-ddd5ea867767.patch)
SHA-256: ddd5ea8677679b65d9162f3837c1aafef8f73c002ab9e6ad3f2c796adb83693f

### VP-0024: Unknown JSON Clearing Reusable Receiver Old Head

- **requirement**: Unknown powId retains the old header on the reclaimer and updates other valid fields
- **mutation**: Unknown JSON Clearing Reusable Receiver Old Head (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0025

[patch](patches/P-0025-e364969ca62a.patch)
SHA-256: e364969ca62af966b9719914441a1c4e1471ec19b82bf3559bc172ef5609481a

### VP-0025: Unknown protobuf returns different error texts

- **requirement**: The unknown protobuf ChainId returns an explicit error.
- **mutation**: Unknown protobuf returns different error texts (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0026

[patch](patches/P-0026-f591658af816.patch)
SHA-256: f591658af81630c96f097fa0111864df5b397d2de559122cde8a549d18bab615

### VP-0026: Copying and sharing inner causes subsequent modifications to overwrite the original object.

- **requirement**: Copy preserves the header fields and isolates subsequent changes to the copy.
- **mutation**: Copying and sharing inner causes subsequent modifications to overwrite the original object. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0027

[patch](patches/P-0027-fda962f57853.patch)
SHA-256: fda962f57853b88927935bc521d361c55f6835919565d5cfeb93bcb6bcd89ef1

### VP-0027: The PoW hash incorrectly uses the block hash

- **requirement**: PowHash retains the outputs of each chain, returns zero for an empty inner part.
- **mutation**: The PoW hash incorrectly uses the block hash (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

## P-0028

[patch](patches/P-0028-fedd6d84c198.patch)
SHA-256: fedd6d84c198c31f5b47eeb97c940de7f57716632e5bbb2d1e20f9ad4fdb739f

### VP-0028: When a JSON header error occurs, the existing headers are cleared, and the payload remains intact.

- **requirement**: JSON header errors do not replace old headers or overwrite subsequent payloads.
- **mutation**: When a JSON header error occurs, the existing headers are cleared, and the payload remains intact. (changed files: core/types/auxpow.go, core/types/auxpow_test.go, core/types/bch.go, core/types/btc.go, among others)
- **setup**: Apply this patch to the clean baseline at 208b67554a90, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch cannot be applied. Not reached the target input state

