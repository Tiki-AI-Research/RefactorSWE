# Adversarial patches and verification points

Task: refactor-fynedesk-frame-interaction-03
Base commit: 7bc2c75eda3aeff73b18450fe32a656bc4af27c4

This package contains 32 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-02c0210c80ae.patch)
SHA-256: 02c0210c80aea045895450eb08556f1395d1815d94270d5a2487c7353512ab0f

### VP-0001: Zero displacement still enters the queue

- **requirement**: The tests should catch zero displacement being enqueued.
- **mutation**: Enqueue even zero displacement. The test must distinguish no visible movement from no queue write. (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0002

[patch](patches/P-0002-043ef614461d.patch)
SHA-256: 043ef614461d5014a35818976abf750a652c5dc7e5e500fb2d69a80c35068cee

### VP-0002: Move to the same target, retain hover and drawing callback

- **requirement**: The changes affect the existing behaviors, which should be tested for: handling target movement with callbacks, maintaining hover and drawing.
- **mutation**: Move to the same target, retain hover and drawing callback (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0003

[patch](patches/P-0003-08c0af3a9f44.patch)
SHA-256: 08c0af3a9f4457d00fb9551d1690617e4ef1bdb762451902cafb7898f2ce9394

### VP-0003: Omit the refresh after a change.

- **requirement**: The tests should catch a missing refresh after a change.
- **mutation**: Omit the refresh after a change. (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0004

[patch](patches/P-0004-1c74176599d0.patch)
SHA-256: 1c74176599d023672b5da3b0d281fccedd9598c6c11a819f575fe572931d1379

### VP-0004: Double-click to assign click

- **requirement**: The tests should catch the regression where a double click is dispatched as a single click.
- **mutation**: Double-click to assign click (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0005

[patch](patches/P-0005-25573bb4f2d3.patch)
SHA-256: 25573bb4f2d332e65aa58477217cffeba589f66730c1baf18f423e1d2b2a1ce3

### VP-0005: move request force=true

- **requirement**: The existing behavior affected by this change should be tested and constrained: move request force=true
- **mutation**: move request force=true (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0006

[patch](patches/P-0006-2abd921236f2.patch)
SHA-256: 2abd921236f25e9d96cfc66fcd849edb5a5be3023549ba7372c4502b47f2f99e

### VP-0006: Extend the existing deadline from 300ms to 600ms

- **requirement**: The existing behaviors affected by this change should be tested and constrained: extending the existing deadline from 300ms to 600ms.
- **mutation**: Extend the existing deadline from 300ms to 600ms (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0007

[patch](patches/P-0007-2cd72fce1b15.patch)
SHA-256: 2cd72fce1b15b0ea9b9d6c6d372b8f792ababbf360940bf89985e590efe842ab

### VP-0007: release does not clear ignore

- **requirement**: The existing behaviors affected by this change should be tested for constraints: release does not clear the ignored items.
- **mutation**: release does not clear ignore (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0008

[patch](patches/P-0008-369836022b05.patch)
SHA-256: 369836022b055a2300655e10297159f38bfd80e6971c8517c3bbffd5dab3daa6

### VP-0008: Targeted change: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **mutation**: Targeted changes to internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0009

[patch](patches/P-0009-3f8fcb61890f.patch)
SHA-256: 3f8fcb61890fdb2119e9c04af732b5f63ea20b6c2297654b97c762b93c131230

### VP-0009: Ignore full screen/ignore protection

- **requirement**: The existing behaviors affected by this change should be tested and constrained: remove full-screen/ignored protection
- **mutation**: Ignore full screen/ignore protection (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0010

[patch](patches/P-0010-5ecbad75884b.patch)
SHA-256: 5ecbad75884b84fa3c71fdec1d4e86b31f604e6b345088deed1fd531fc2e28ec

### VP-0010: Mouse movement notification reversed x/y forwarding coordinates

- **requirement**: The X11 mouse motion must be forwarded with the same x/y coordinates in the original order.
- **mutation**: Mouse movement notification reversed x/y forwarding coordinates
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal testing resulted in a valid rejection, the behavior assertion or routing contract check failed; failure to build or execute does not count as success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0011

[patch](patches/P-0011-589fc8d95fee.patch)
SHA-256: 589fc8d95feef6d296ecf2e9ad3bcb83ff0a27c93f284c080e837ae1508b1246

### VP-0011: Replace the actual mouseX decision-dependent logic with the frame, and keep the dead fields to ensure that the rest of the code can still be compiled.

- **requirement**: The changes affect the existing behavior, which should be tested and constrained: the actual mouseX decision should be placed back in the frame, and dead fields should be retained to ensure that the rest of the code can be compiled.
- **mutation**: Replace the actual mouseX decision-dependent logic with the frame, and keep the dead fields to ensure that the rest of the code can still be compiled. (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0012

[patch](patches/P-0012-66ab625cdbfe.patch)
SHA-256: 66ab625cdbfea845ceea39aecf7dcc41bf0e0e8a9121da32fb74c2667bb72618

### VP-0012: The TitleHeight equal sign boundary is missing in the baseline acceptance.

- **requirement**: The existing behaviors affected by this change should be tested for constraints: The TitleHeight equal sign boundary accepted by the baseline is lost.
- **mutation**: The TitleHeight equal sign boundary is missing in the baseline acceptance. (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0013

[patch](patches/P-0013-728482365e64.patch)
SHA-256: 728482365e64e6f2a45dd2adbb057166cd20aff12121107c141e4b3d1c75252b

### VP-0013: Write the property to child.

- **requirement**: The existing behaviors affected by this change should be tested and constrained: Attributes are written to child.
- **mutation**: Write the property to child. (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0014

[patch](patches/P-0014-732dba2ee77c.patch)
SHA-256: 732dba2ee77c40d21e17773b848119fe0d41e03611d15459071fb1d68faf8ade

### VP-0014: Omit the ending "raise".

- **requirement**: The existing behaviors affected by this change should be tested and constrained: omitting the final raise.
- **mutation**: Omit the ending "raise". (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0015

[patch](patches/P-0015-7842d1abb26c.patch)
SHA-256: 7842d1abb26c4b4c4d78690bc6ea7a1064106c4e66806d76524979a515ad73e7

### VP-0015: Replace the actual use of pixmap with frame, and keep the decorative dead fields.

- **requirement**: The existing behavior affected by this change should be tested and constrained: replace the actual usage of pixmap with frame, and retain the decorated dead fields.
- **mutation**: Replace the actual use of pixmap with frame, and keep the decorative dead fields. (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0016

[patch](patches/P-0016-8326159cd34e.patch)
SHA-256: 8326159cd34e8998ff03552f7bfead090ad9fd2fc2f94547207845ed5879e24d

### VP-0016: Omit unfocused activations

- **requirement**: The existing behaviors affected by this change should be tested and constrained: omitting unfocused activations
- **mutation**: Omit unfocused activations (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0017

[patch](patches/P-0017-8f5d8bf63a6c.patch)
SHA-256: 8f5d8bf63a6cac88510ca9a63b3195248b739ad155b0f68ba03fa3cf6b95ada1

### VP-0017: Click to Unassign Expired

- **requirement**: The tests should catch the regression where an expired single click is never dispatched.
- **mutation**: Click to Unassign Expired (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0018

[patch](patches/P-0018-91e4ab9bfbee.patch)
SHA-256: 91e4ab9bfbeefde74a6cce223743a7558ca74e2122098fae9c6dd44b368a9d62

### VP-0018: The classification function is missing the scaling flag.

- **requirement**: The existing behaviors affected by this change should be tested for constraints: The classification function loses its scaling flag.
- **mutation**: The classification function is missing the scaling flag. (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0019

[patch](patches/P-0019-979a2091a060.patch)
SHA-256: 979a2091a060eb74886abfb485d4741ebbff654c2bebcc8bd231d52070030f52

### VP-0019: Lost scaling cursor search

- **requirement**: The existing behaviors affected by this change should be tested and constrained: Lost zoom cursor search
- **mutation**: Lost scaling cursor search (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0020

[patch](patches/P-0020-9e620477febe.patch)
SHA-256: 9e620477febe5e9a16d7165fcc53c1e1af2fe9111f1c7fe80bcb0ffa508c92b4

### VP-0020: Do not save the matched ignored items.

- **requirement**: The existing behaviors affected by this change should be tested and constrained: do not save those that are ignored.
- **mutation**: Do not save the matched ignored items. (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0021

[patch](patches/P-0021-aa25cdd3a7d8.patch)
SHA-256: aa25cdd3a7d87baf6813bcd42c155fadfc239a025d19520cf6e3a463de0a150c

### VP-0021: Eliminate reliance on complete pure unit tests for delivery; maintain production behavior

- **requirement**: The existing behaviors affected by this change should be tested and constrained: Remove all pure unit tests for reference solutions, keep production behavior intact.
- **mutation**: Eliminate reliance on complete pure unit tests for delivery; maintain production behavior (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0022

[patch](patches/P-0022-b27acd2aa99b.patch)
SHA-256: b27acd2aa99bdcd21e2ea9d77f4281a135607a6599889b0b7d4dce9be5d1353a

### VP-0022: Allow non-primary entries

- **requirement**: The existing behaviors affected by this change should be tested and constrained: non-primary keys are allowed to enter.
- **mutation**: Allow non-primary entries (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0023

[patch](patches/P-0023-c6e2f78f46a8.patch)
SHA-256: c6e2f78f46a8891670c8be926a10bb12089a0f4af46bc9b1658e91ace5214130

### VP-0023: Negative width and height incorrectly set to 1

- **requirement**: The tests should catch an incorrect clamp to 1 for either negative dimension.
- **mutation**: Incorrectly clamp a negative width or height to 1. Inspect the enqueued value before decoration applies its minimum size. (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0024

[patch](patches/P-0024-d0d84aba8370.patch)
SHA-256: d0d84aba8370f88525f931ec56fea70ad79b88bb7d005af76a010eb51ca54a5d

### VP-0024: Replace old save coordinates with current event coordinates.

- **requirement**: The existing behaviors affected by this change should be tested and constrained: use the current event coordinates instead of the old saved coordinates.
- **mutation**: Replace old save coordinates with current event coordinates. (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0025

[patch](patches/P-0025-d1042e109728.patch)
SHA-256: d1042e1097287379e0d823e1ef1f65c99f0879e503a383a79b98b0a010e27371

### VP-0025: Targeted change: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **mutation**: Targeted changes to internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0026

[patch](patches/P-0026-d3f925600647.patch)
SHA-256: d3f92560064750eeec22c1e4f0becd7d453c6d8596a4af7fc85cd5c9226b2242

### VP-0026: Target cursor closing error

- **requirement**: The existing behaviors affected by this change should be tested for: incorrect closing of the target cursor.
- **mutation**: Target cursor closing error (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0027

[patch](patches/P-0027-d5c5c3e89dfd.patch)
SHA-256: d5c5c3e89dfdbb21e376a43ab00575b82bc8970b99d8bfa74e83aa97e89e36e2

### VP-0027: The title center has lost its movement mode.

- **requirement**: The existing behaviors affected by this change should be tested and constrained: The title center loses the movement mode.
- **mutation**: The title center has lost its movement mode. (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0028

[patch](patches/P-0028-d8b67b712a96.patch)
SHA-256: d8b67b712a967379ac4c6019989f19f0406d8a5897f362a32c7a4560d239c0cc

### VP-0028: Remove full-screen early return

- **requirement**: The existing behaviors affected by this change should be tested and constrained: remove full-screen early return.
- **mutation**: Remove full-screen early return (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0029

[patch](patches/P-0029-deb45278755b.patch)
SHA-256: deb45278755bebaafca4be6d9db7ddc5b2a1ee5d991ae91b436dd183ca4d471f

### VP-0029: Targeted change: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **mutation**: Targeted changes to internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0030

[patch](patches/P-0030-df1b725bd929.patch)
SHA-256: df1b725bd929b04e6bf25df666b7cbbe474c1cd57928e9528b6e77a38ae9e7ca

### VP-0030: Strict threshold changed to include equal signs

- **requirement**: The existing behaviors affected by this change should be tested and constrained: strict threshold changed to include equal signs.
- **mutation**: Strict threshold changed to include equal signs (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0031

[patch](patches/P-0031-e4ab637734c5.patch)
SHA-256: e4ab637734c53770c1cc63e4c281a2c6e49a11f6e8779a304f76eff399026b6c

### VP-0031: Targeted change: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **mutation**: Targeted changes to internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

## P-0032

[patch](patches/P-0032-ff0e39518406.patch)
SHA-256: ff0e39518406dcbbae90f8aa7a03c07be155f285612170610681c7820cfc6ec1

### VP-0032: Bypass the controlled POS reading interface, with behavior equivalent but structural violation

- **requirement**: The changes affect the existing behavior, which should be tested for: bypassing the controlled pos read interface, with behavior equivalent but structural violations.
- **mutation**: Bypass the controlled POS reading interface, with behavior equivalent but structural violation (changed files: internal/x11/win/client.go, internal/x11/win/decoration.go, internal/x11/win/frame.go, internal/x11/win/interaction.go, among others)
- **setup**: Apply this patch to the clean baseline at 7bc2c75eda3a, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior or assertion was never reached

