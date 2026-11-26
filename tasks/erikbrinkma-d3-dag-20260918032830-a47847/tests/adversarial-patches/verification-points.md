# Adversarial patches and verification points

Task: erikbrinkma-d3-dag-20260918032830-a47847
Base commit: 67d5447722eff38482a5bc5b5eed5f4229d2f80b

This package contains 42 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-007bc37006dc.patch)
SHA-256: 007bc37006dcf9d7b01a58cfd29b67c577bbc9d72d12115056bee840f870dd27

### VP-0001: tweakSugiyama upgraded the standalone cache to the tweak function lifespan

- **requirement**: Independent tweakSugiyama repeatedly calls the reread current size function; tweakSugiyama upgrades the standalone cache to the lifetime of the tweak function.
- **mutation**: tweakSugiyama upgraded the standalone cache to the tweak function lifespan (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0002

[patch](patches/P-0002-07668737d117.patch)
SHA-256: 07668737d1170918261126ff9b496b08877c5672861cfdf7dbc85e55c041e353

### VP-0002: zherebko valid input link.points horizontal coordinate shifted by 0.125

- **requirement**: zherebko's valid deterministic size link routing does not revert; zherebko's valid input link.points x-axis undergoes a 0.125 drift
- **mutation**: zherebko valid input link.points horizontal coordinate shifted by 0.125 (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0003

[patch](patches/P-0003-0a5d3ca3f134.patch)
SHA-256: 0a5d3ca3f134063e511caa39e44d6959b7a97d9a3798f31fd295bcff7c341986

### VP-0003: The cachedNodeSize does not save the failure results.

- **requirement**: The cachedNodeSize does not save the failure results.
- **mutation**: The cachedNodeSize does not save the failure results. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0004

[patch](patches/P-0004-0e0d876abc46.patch)
SHA-256: 0e0d876abc46ae79016c574e1825bdb2ce657e18827c5187c2e1ac773df593c6

### VP-0004: Initial width of empty diagram is incorrect, it is 1.

- **requirement**: The empty image is initialized with zero boundaries and passed to the first tweak; the initial width of the empty image is set to 1.
- **mutation**: Initial width of empty diagram is incorrect, it is 1. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0005

[patch](patches/P-0005-0e4d37a7b50d.patch)
SHA-256: 0e4d37a7b50db94f7117f68479c4b6b3ed6920bcf856033ca19f4bc22f53bc21

### VP-0005: Corrected the setter for grid to modify the old builder configuration.

- **requirement**: grid retains the valid nodeSize constant/callback setter; errors in the grid's setter may modify the old builder configuration.
- **mutation**: Corrected the setter for grid to modify the old builder configuration. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0006

[patch](patches/P-0006-0f8fce5f589e.patch)
SHA-256: 0f8fce5f589e06cc427633237c87f460a81192d58aade1ff89f0dcd2c54a0bad

### VP-0006: zherebko valid input LayoutResult.width has a drift of 0.125

- **requirement**: zherebko ensures accurate and deterministic input maintains layout boundaries; zherebko's valid input LayoutResult.width experiences a 0.125 drift
- **mutation**: zherebko valid input LayoutResult.width has a drift of 0.125 (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0007

[patch](patches/P-0007-0fa9a723c7c0.patch)
SHA-256: 0fa9a723c7c09e4a2e5774b446c6d151b6a21f5ea124c02ba8b9ec90445d5b31

### VP-0007: zherebko valid input node.x experienced a 0.125 drift

- **requirement**: zherebko valid input node.x experienced a 0.125 drift
- **mutation**: zherebko valid input node.x experienced a 0.125 drift (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0009

[patch](patches/P-0009-37ee52053217.patch)
SHA-256: 37ee5205321788c6bb0b507bae23f8671d0cc9a9792e045d9a38c7adff22735a

### VP-0009: Error in dimension element format, additional question marks, violating the specified String output.

- **requirement**: Invalid binary size, width/height is safely formatted by element type; elements with incorrect sizes are appended with a question mark, violating the specified String output format.
- **mutation**: Error in dimension element format, additional question marks, violating the specified String output. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0010

[patch](patches/P-0010-396b88902aa0.patch)
SHA-256: 396b88902aa0f4ab72aa9cfa66349f65b6838de946f38bd282a73d7909c8a0aa

### VP-0010: Add positive size verification for non-verified splitNodeSize.

- **requirement**: splitNodeSize uses the semantic of a non-verified numerical tuple directly; enforce a positive size verification for non-verified splitNodeSize.
- **mutation**: Add positive size verification for non-verified splitNodeSize. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0011

[patch](patches/P-0011-3c2753e2c219.patch)
SHA-256: 3c2753e2c219036572102f5788efb543002a488b85cd5272145838569368bcca

### VP-0011: Invalid callback returns are misattributed to constant errors.

- **requirement**: Invalid callback returns are classified using a separate category, with a unified field order and specified old keywords; invalid callback returns are misclassified as constant errors.
- **mutation**: Invalid callback returns are misattributed to constant errors. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0012

[patch](patches/P-0012-4132034e7306.patch)
SHA-256: 4132034e7306b08680e2fe01042f97f284031b2c8e1c8ad9d7af5ee005337cec

### VP-0012: The returned array has an incorrect label for size.

- **requirement**: The non-tuple size error results in the unavailability of dimensions and the returned summary; the error in the returned label of the non-binary array is size.
- **mutation**: The returned array has an incorrect label for size. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0013

[patch](patches/P-0013-4f00b352ebe8.patch)
SHA-256: 4f00b352ebe8bfd5fbefc3d2d70a5246e9ca18faa8790be245461527ed3b1bf4

### VP-0013: splitNodeSize width and height reading failed to save snapshot, repeated evaluation

- **requirement**: splitNodeSize width and height reading failed to save snapshot, repeated evaluation
- **mutation**: splitNodeSize width and height reading failed to save snapshot, repeated evaluation (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0014

[patch](patches/P-0014-4fe982d4f014.patch)
SHA-256: 4fe982d4f01499e24d40d0bc4b329b94e72828d7b56c544db5a3b4834c5912ef

### VP-0014: Elevate layout context errors to the builder lifecycle for cross-execution reuse and caching.

- **requirement**: When the same layout is running continuously, the dimensions are re-parse, including cases where the cachedNodeSize is passed in. Each layout context error is raised to the lifetime of the builder, allowing for cross-execution reuse of the cached data.
- **mutation**: Elevate layout context errors to the builder lifecycle for cross-execution reuse and caching. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0015

[patch](patches/P-0015-52855f289f98.patch)
SHA-256: 52855f289f984a49bd06fd1d938cf88e441a755907f106da13f8d3fa7d5cb86e

### VP-0015: Grid's valid input LayoutResult.width has a drift of 0.125

- **requirement**: The grid maintains layout boundaries with valid deterministic input; the width of the LayoutResult with valid input changes by 0.125.
- **mutation**: Grid's valid input LayoutResult.width has a drift of 0.125 (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0016

[patch](patches/P-0016-55b770efa51d.patch)
SHA-256: 55b770efa51dda7607709b7a462b18db029312d8f44df75b88211c258a006da0

### VP-0016: The custom tweak resets the input zero boundary, losing the previous return value.

- **requirement**: The empty diagram still transmits the return results of each tweak in order; each custom tweak resets the input zero boundary, and the previous return is lost.
- **mutation**: The custom tweak resets the input zero boundary, losing the previous return value. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0017

[patch](patches/P-0017-561ed2986daf.patch)
SHA-256: 561ed2986daf7afe892f502bd4f451646aa0f066a0bd98c6428678330a2f6ee1

### VP-0017: Sugiyama's valid input node.x experiences a 0.125 drift.

- **requirement**: Sugiyama's valid input node.x experiences a 0.125 drift.
- **mutation**: Sugiyama's valid input node.x experiences a 0.125 drift. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0018

[patch](patches/P-0018-5985aef5c595.patch)
SHA-256: 5985aef5c595ee76c76ac260416264ba3743186d21a24513b7ddbf53a31b1522

### VP-0018: Basic node.data misuse of non-displayable placeholders

- **requirement**: Callback failure: The node field distinguishes between base data that can be directly displayed and placeholder branches; incorrect use of placeholders in base node.data makes it impossible to display the placeholder.
- **mutation**: Basic node.data misuse of non-displayable placeholders (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0020

[patch](patches/P-0020-5ece2883cd12.patch)
SHA-256: 5ece2883cd126741541997aeb80b497aaec81d13817900906cafb81847c32afc

### VP-0020: sugiyama removes the zero-parameter getter ability

- **requirement**: sugiyama retains the zero-parameter nodeSize getter; sugiyama removes the zero-parameter getter functionality.
- **mutation**: sugiyama removes the zero-parameter getter ability (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0021

[patch](patches/P-0021-6fb5c70da798.patch)
SHA-256: 6fb5c70da798279da3c416ea16368f1b1f21b6e760ea5f003856eda24355ecef

### VP-0021: Nested cachedNodeSize error unpacking and directly returning the original callback, causing transparent caching to be broken

- **requirement**: Nested cachedNodeSize error unpacking and directly returning the original callback, causing transparent caching to be broken
- **mutation**: Nested cachedNodeSize error unpacking and directly returning the original callback, causing transparent caching to be broken (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0022

[patch](patches/P-0022-70a667e3fa3b.patch)
SHA-256: 70a667e3fa3bc9c0d7f50622da501af7d21acdc90fec89dde3211bacdce763fc

### VP-0022: The built-in tweakSugiyama bypasses the layout context and creates a separate cache for the same callback.

- **requirement**: tweakSugiyama reuse this layout size when using the same callback; built-in tweakSugiyama bypasses the layout context and creates a new cache for the same callback
- **mutation**: The built-in tweakSugiyama bypasses the layout context and creates a separate cache for the same callback. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0023

[patch](patches/P-0023-782f4898bf26.patch)
SHA-256: 782f4898bf26885d52d342a731b72befe9e9c0712105621716a82117b185e8f7

### VP-0023: Make all contexts share a global Map so that independent layouts affect one another.

- **requirement**: Make all contexts share a global Map so that independent layouts affect one another.
- **mutation**: Make all contexts share a global Map so that independent layouts affect one another. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

### VP-0024: Sharing a global Map across contexts lets nested and outer layout calls contaminate each other's caches.

- **requirement**: Callback fixture restores common ux/uy, excluding internal layout geometric side effects
- **mutation**: Sharing a global Map across contexts lets nested and outer layout calls contaminate each other's caches. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0024

[patch](patches/P-0024-7e1dbe4c6908.patch)
SHA-256: 7e1dbe4c6908bda4d4d063a94f639e9a34ba44424a414a8387655b1f5fb7ace9

### VP-0025: The built-in tweakShape bypasses the layout context and creates a separate cache for the same callback.

- **requirement**: tweakShape reuses the initial layout dimensions when using the same callback as the layout identity; built-in tweakShape bypasses the layout context to create a separate cache for the same callback.
- **mutation**: The built-in tweakShape bypasses the layout context and creates a separate cache for the same callback. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0025

[patch](patches/P-0025-7eef1326ac04.patch)
SHA-256: 7eef1326ac043fa049ddda8967832ea579acb55588bbbd5cfb70c94716850fab

### VP-0026: splitNodeSize retains the reference to the shared array, does not save snapshots of the two axes.

- **requirement**: splitNodeSize retains the reference to the shared array, does not save snapshots of the two axes.
- **mutation**: splitNodeSize retains the reference to the shared array, does not save snapshots of the two axes. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0026

[patch](patches/P-0026-837991c6e681.patch)
SHA-256: 837991c6e68172433584d3ff34f558dd7a90da116eb783046e584a53cf979119

### VP-0027: tweakGridHandles has upgraded the standalone cache to the lifetime of the tweak function.

- **requirement**: Independent calls to tweakGridHandles repeatedly reload the current size; tweakGridHandles upgrades the standalone cache to the lifetime of the tweak function.
- **mutation**: tweakGridHandles has upgraded the standalone cache to the lifetime of the tweak function. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0027

[patch](patches/P-0027-85da0f5e2e14.patch)
SHA-256: 85da0f5e2e14e0d1baedd95e52a2a1b49a3ed1bd72da40d532553af3e139f769

### VP-0028: tweakShape has upgraded the standalone cache to the tweak function lifespan.

- **requirement**: The independent tweakShape continuously calls the reread current size function; the tweakShape improves the standalone cache to the lifetime of the tweak function.
- **mutation**: tweakShape has upgraded the standalone cache to the tweak function lifespan. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0028

[patch](patches/P-0028-860d261a2d64.patch)
SHA-256: 860d261a2d64348ff80a3a720eb81fa2c197d98ed10f16d6a58439185dec7037

### VP-0029: Targeted regression: Infinity did not reject due to invalid callbacks

- **requirement**: Infinity did not reject due to invalid callbacks
- **mutation**: Targeted regression: Infinity did not reject due to invalid callbacks (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

### VP-0030: Targeted regression: Infinity did not reject due to invalid callbacks

- **requirement**: Infinity did not reject due to invalid callbacks
- **mutation**: Targeted regression: Infinity did not reject due to invalid callbacks (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

### VP-0031: Targeted regression: Infinity did not reject due to invalid callbacks

- **requirement**: Infinity did not reject due to invalid callbacks
- **mutation**: Targeted regression: Infinity did not reject due to invalid callbacks (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0029

[patch](patches/P-0029-927eb325d293.patch)
SHA-256: 927eb325d293ece24877b33bd5253be924d6336f0c65998ef2844274059d3bb8

### VP-0032: Empty image path error evaluation nodeSize callback, violation of zero-occurrence guarantee

- **requirement**: Empty layout and built-in size tweaks do not evaluate size callback; empty image path evaluates nodeSize callback incorrectly, violating the zero-occurrence guarantee.
- **mutation**: Empty image path error evaluation nodeSize callback, violation of zero-occurrence guarantee (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0030

[patch](patches/P-0030-98c17bf63023.patch)
SHA-256: 98c17bf6302315f301640b82c24715fa0cfb0c63b77b027f4b4ccf01d78beb7b

### VP-0033: Targeted regression: Geometric reading of the same initial dimensions

- **requirement**: Geometric reading of the same initial dimensions; the layout context is executed once more in case of a cache miss, and the underlying callback is called additionally.
- **mutation**: Targeted regression: Geometric reading of the same initial dimensions (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

### VP-0034: Targeted regression: The layout context executes an additional underlying callback when a cache miss occurs.

- **requirement**: The layout context executes an additional underlying callback when a cache miss occurs.
- **mutation**: Targeted regression: The layout context executes an additional underlying callback when a cache miss occurs. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

### VP-0035: Targeted regression: The layout context executes an additional underlying callback when a cache miss occurs.

- **requirement**: The layout context executes an additional underlying callback when a cache miss occurs.
- **mutation**: Targeted regression: The layout context executes an additional underlying callback when a cache miss occurs. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0031

[patch](patches/P-0031-9b76fc6c8c17.patch)
SHA-256: 9b76fc6c8c17ac924c41353e813df58afe304206694f5a09b83978c42181f602

### VP-0036: Sugiyama's valid input link.points' horizontal coordinate shifts by 0.125

- **requirement**: Sugiyama's valid deterministic size link routing does not revert; Sugiyama's valid input link.points x-axis undergoes a 0.125 drift.
- **mutation**: Sugiyama's valid input link.points' horizontal coordinate shifts by 0.125 (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0032

[patch](patches/P-0032-9cdb632054b2.patch)
SHA-256: 9cdb632054b2cbc411f1bca4610e01389b27323614adc09dfbcf427f652b1a44

### VP-0037: Directly cachedNodeSize does not save successful results.

- **requirement**: Directly cachedNodeSize does not save successful results.
- **mutation**: Directly cachedNodeSize does not save successful results. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0033

[patch](patches/P-0033-a8e7f499d6b9.patch)
SHA-256: a8e7f499d6b952d2b36af4b6dafec38b8d56320aefffb8a5b5ba4558121b4f4b

### VP-0038: Context does not distinguish between callback identities, errors are reused from the first accessor.

- **requirement**: The size tweak and layout have different callback references that are evaluated independently; the context does not distinguish between callback identities, and errors are reused from the first accessor.
- **mutation**: Context does not distinguish between callback identities, errors are reused from the first accessor. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0034

[patch](patches/P-0034-adfca9f58bc7.patch)
SHA-256: adfca9f58bc7e7cc86331a09a9fcda554e2070720985b3a56a508f1496e94516

### VP-0039: The sugiyama setter incorrectly modifies the old builder's configuration.

- **requirement**: sugiyama retains the valid nodeSize constant/callback setter; sugiyama's setter incorrectly modifies the old builder configuration.
- **mutation**: The sugiyama setter incorrectly modifies the old builder's configuration. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0035

[patch](patches/P-0035-b54c8fd8f146.patch)
SHA-256: b54c8fd8f1461c493a88adaec35bf742e997c7c53da999afc6c141a6b88f702f

### VP-0040: NaN is accepted at the configuration boundaries.

- **requirement**: The constant size of sugiyama is verified at the setter boundary for a binary array and two positive finite numbers; NaN is accepted at the configuration boundary.
- **mutation**: NaN is accepted at the configuration boundaries. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

### VP-0041: Targeted regression: The constant size of zherebko is verified within the setter boundary.

- **requirement**: The constant size of zherebko is verified within the setter boundary; Infinity is accepted at the configuration boundary.
- **mutation**: Targeted regression: The constant size of zherebko is verified within the setter boundary. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

### VP-0042: Targeted regression: The grid constant size will undergo the same validation within the setter boundary.

- **requirement**: The grid constant size undergoes the same validation at the setter boundary; Infinity is accepted at the configuration boundary.
- **mutation**: Targeted regression: The grid constant size will undergo the same validation within the setter boundary. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

### VP-0043: Targeted regression: The cachedNodeSize constant input undergoes the same validation when constructing the accessor.

- **requirement**: The cachedNodeSize constant is validated in the same manner when it is input into the constructor; Infinity is accepted at the configuration boundary.
- **mutation**: Targeted regression: The cachedNodeSize constant input undergoes the same validation when constructing the accessor. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0036

[patch](patches/P-0036-cde355a9acdb.patch)
SHA-256: cde355a9acdb08f9607e0d99113a98889dc85757342ea28fe833c6b68f0e04cc

### VP-0044: The built-in tweakGridHandles bypasses the layout context and creates a new cache for the same callback.

- **requirement**: tweakGridHandles reuses the layout dimensions when the same callback is used; the built-in tweakGridHandles bypasses the layout context and creates a cache for the same callback.
- **mutation**: The built-in tweakGridHandles bypasses the layout context and creates a new cache for the same callback. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0037

[patch](patches/P-0037-d0f077f07890.patch)
SHA-256: d0f077f078909f4a24c5e9baa2dde5b3e0e1f098336006c77d10e98e8116656a

### VP-0045: The grid's valid input link.points' horizontal coordinate shifted by 0.125

- **requirement**: The grid has a valid and deterministic size for link routing; the grid input link.points' x-axis values shift by 0.125.
- **mutation**: The grid's valid input link.points' horizontal coordinate shifted by 0.125 (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0038

[patch](patches/P-0038-d631b68e8041.patch)
SHA-256: d631b68e80416578b86a79abaaa018e0ee082c156eaac0577f03706b7d90c3c2

### VP-0046: zherebko removes the zero-parameter getter capability

- **requirement**: zherebko retains the zero-parameter nodeSize getter; zherebko removes the zero-parameter getter functionality.
- **mutation**: zherebko removes the zero-parameter getter capability (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0039

[patch](patches/P-0039-dfbba6dd299a.patch)
SHA-256: dfbba6dd299a7bd95600ab2e94732f49ba41d15a8f28b720f34b154ecd6550a2

### VP-0047: The valid input of grid has a drift of 0.125 in node.x.

- **requirement**: The valid input of grid has a drift of 0.125 in node.x.
- **mutation**: The valid input of grid has a drift of 0.125 in node.x. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0040

[patch](patches/P-0040-e51e3db325a9.patch)
SHA-256: e51e3db325a9086ee9f8b76694d1fee4a172b797c172c18ca76affa2dabdeccb

### VP-0048: Grid removes the zero-parameter getter capability.

- **requirement**: grid retains the zero-parameter nodeSize getter; grid removes the zero-parameter getter capability.
- **mutation**: Grid removes the zero-parameter getter capability. (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0041

[patch](patches/P-0041-ec1a21f16252.patch)
SHA-256: ec1a21f16252a8f2ebb5d9ddf376cd9c2269836f026fb6eb73d6458eaa76a75d

### VP-0049: Packaging exception converted the original cause error to a string

- **requirement**: The packaging callback exception retains the original cause as the exception; the packaging exception converts the original cause error into a string.
- **mutation**: Packaging exception converted the original cause error to a string (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0042

[patch](patches/P-0042-ed48abae0913.patch)
SHA-256: ed48abae0913daea6c1e5478cdeb36789b947d1176eec963b18da8ad5123af6d

### VP-0050: Sugiyama's valid input LayoutResult.width has a drift of 0.125

- **requirement**: Sugiyama's effective deterministic input maintains layout boundaries; Sugiyama's effective input results in a 0.125 drift in LayoutResult.width
- **mutation**: Sugiyama's valid input LayoutResult.width has a drift of 0.125 (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0043

[patch](patches/P-0043-f3092103345a.patch)
SHA-256: f3092103345a45002adaa95f43ec0082146b7bdb03e0e407bf359c97945605bb

### VP-0051: Wrong packaging, additional prohibited legacy fields

- **requirement**: When the callback throws an error, the wrapped message must contain only the specified four fields. An additional prohibited legacy field should be added in case of an error.
- **mutation**: Wrong packaging, additional prohibited legacy fields (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

## P-0044

[patch](patches/P-0044-fad6eac7d5dd.patch)
SHA-256: fad6eac7d5ddec5a97f7c6cd57ee6284e1587866210f23f22d2dcd450439dc27

### VP-0052: zherebko's setter incorrectly modifies the old builder configuration

- **requirement**: zherebko retains the valid nodeSize constant/callback setter; errors in zherebko's setter may modify the old builder configuration.
- **mutation**: zherebko's setter incorrectly modifies the old builder configuration (changed files: src/layout.ts, src/tweaks.ts, src/sugiyama/index.ts, src/zherebko/index.ts, among others)
- **setup**: Apply this patch to the clean baseline at 67d5447722ef, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails; Only a syntax, import, or tooling error occurs

