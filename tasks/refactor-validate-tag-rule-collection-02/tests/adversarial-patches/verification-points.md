# Adversarial patches and verification points

Task: refactor-validate-tag-rule-collection-02
Base commit: e6e7ae6b751ee3c3ce29eee733c5281f2718dbe0

This package contains 11 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-3504decc7a41.patch)
SHA-256: 3504decc7a41c616147aacf61ee4080f273a6ecbbd44d6eb53d47465f53df4c6

### VP-0001: Make filter rules reference a shared template so changes in one instance leak into subsequent instances.

- **requirement**: Make filter rules reference a shared template so changes in one instance leak into subsequent instances.
- **mutation**: Make filter rules reference a shared template so changes in one instance leak into subsequent instances. (changed files: cache.go, struct_rules.go, data_source.go)
- **setup**: Apply this patch to the clean baseline at e6e7ae6b751e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Actual credible targets should be rejected
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/Application/Collection Errors

## P-0002

[patch](patches/P-0002-49846ea400e0.patch)
SHA-256: 49846ea400e0a066391c00373de67af3a9f54421cc7d6b77fdb2debb440d7671

### VP-0002: Silently skip nil elements in slices/arrays, change the already guaranteed panic

- **requirement**: Silently skip nil elements in slices/arrays, change the already guaranteed panic
- **mutation**: Silently skip nil elements in slices/arrays, change the already guaranteed panic (changed files: cache.go, struct_rules.go, data_source.go)
- **setup**: Apply this patch to the clean baseline at e6e7ae6b751e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Actual credible targets should be rejected
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/Application/Collection Errors

## P-0003

[patch](patches/P-0003-74504fc734a4.patch)
SHA-256: 74504fc734a493388f3dd5494940d34e0decc2b4189d90bfd3479ad23253f689

### VP-0003: Close UpdateSource tag

- **requirement**: Close the UpdateSource tag; the tag itself being true is an explicit contract, and the getter writing back unchanged is not considered a failure reason.
- **mutation**: Close the UpdateSource tag; the tag itself being true is an explicit contract, and the getter writing back unchanged is not considered a failure reason. (changed files: cache.go, struct_rules.go, data_source.go)
- **setup**: Apply this patch to the clean baseline at e6e7ae6b751e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Actual credible targets should be rejected
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/Application/Collection Errors

## P-0004

[patch](patches/P-0004-7bac2acfd7fb.patch)
SHA-256: 7bac2acfd7fbc361d33c15b93ca8f9dc00024d3c9b614c0ee4a7ae3e8d648a38

### VP-0004: Transfer the dynamic tag parsing back to the StructData method, maintain the binding with rule output, and adhere to the principle of separation of concerns.

- **requirement**: Transfer the dynamic tag parsing back to the StructData method, maintain the binding with rule output, and adhere to the principle of separation of concerns.
- **mutation**: Transfer the dynamic tag parsing back to the StructData method, maintain the binding with rule output, and adhere to the principle of separation of concerns. (changed files: cache.go, struct_rules.go, data_source.go)
- **setup**: Apply this patch to the clean baseline at e6e7ae6b751e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Actual credible targets should be rejected
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/Application/Collection Errors

## P-0005

[patch](patches/P-0005-80cba79fc659.patch)
SHA-256: 80cba79fc659156f3be428bc5dd1f56eac2023a6d6f9951e96261d49ba9e2f13

### VP-0005: Bypass template cache for each rebuild, behavior remains consistent but violates the rule of no more than one configuration per time.

- **requirement**: Bypass template cache for each rebuild, behavior remains consistent but violates the rule of no more than one configuration per time.
- **mutation**: Bypass template cache for each rebuild, behavior remains consistent but violates the rule of no more than one configuration per time. (changed files: cache.go, struct_rules.go, data_source.go)
- **setup**: Apply this patch to the clean baseline at e6e7ae6b751e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Actual credible targets should be rejected
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/Application/Collection Errors

## P-0006

[patch](patches/P-0006-a06611aff514.patch)
SHA-256: a06611aff514a8a5fb202686da7fb7b5ff00cc48793035f810f04f9b5c4814f7

### VP-0006: Leave the fields for rules, filtering, and output unchanged.

- **requirement**: Leave the fields for rules, filtering, and output unchanged.
- **mutation**: Leave the fields for rules, filtering, and output unchanged. (changed files: cache.go, struct_rules.go, data_source.go)
- **setup**: Apply this patch to the clean baseline at e6e7ae6b751e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Actual credible targets should be rejected
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/Application/Collection Errors

## P-0007

[patch](patches/P-0007-cadd8942e10f.patch)
SHA-256: cadd8942e10fb1628062330e21a4c1a41e512ff9bbd3d2181eb1369bd09d103d

### VP-0007: Restoring the independent classification scan of the baseline, which overlaps with the metadata scan

- **requirement**: Restore the baseline's separate classification scan, duplicating the metadata scan while preserving classification behavior.
- **mutation**: Restore the baseline's separate classification scan, duplicating the metadata scan while preserving classification behavior. (changed files: cache.go, struct_rules.go, data_source.go)
- **setup**: Apply this patch to the clean baseline at e6e7ae6b751e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Actual credible targets should be rejected
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/Application/Collection Errors

## P-0008

[patch](patches/P-0008-dc9b6af92151.patch)
SHA-256: dc9b6af92151d29385cafbf6ca88ea31f63cc296fb0dea643be7be337257e4cc

### VP-0008: Discard the non-empty errors from the passed Create, other public entries remain unchanged.

- **requirement**: Discard the non-empty errors from the passed Create, other public entries remain unchanged.
- **mutation**: Discard the non-empty errors from the passed Create, other public entries remain unchanged. (changed files: cache.go, struct_rules.go, data_source.go)
- **setup**: Apply this patch to the clean baseline at e6e7ae6b751e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Actual credible targets should be rejected
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/Application/Collection Errors

## P-0009

[patch](patches/P-0009-6f690e6e4f02.patch)
SHA-256: bb9e5147b76527bf045a9fcbb464bf9b74b56e6a0595ca175da6e0723b850938

### VP-0009: Static template playback loses default values

- **requirement**: Static template playback loses default values
- **mutation**: The above directed behavior defects are injected into the struct_rules.go of the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline e6e7ae6b751ee3c3ce29eee733c5281f2718dbe0.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0010

[patch](patches/P-0010-2e55f7369083.patch)
SHA-256: 835c29de45a36376b82b643f14feecabcb885f56098b11f4224b463c5bf659d3

### VP-0010: Static template playback loses output field name mapping

- **requirement**: Static template playback loses output field name mapping
- **mutation**: The above directed behavior defects are injected into the struct_rules.go of the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline e6e7ae6b751ee3c3ce29eee733c5281f2718dbe0.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0011

[patch](patches/P-0011-7510baf29406.patch)
SHA-256: 2e166b0dd7136f6de75dea19a202463567221c042e1247d2ce69002643ea8d96

### VP-0011: Static template playback loses custom messages

- **requirement**: Static template playback loses custom messages
- **mutation**: The above directed behavior defects are injected into the struct_rules.go of the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline e6e7ae6b751ee3c3ce29eee733c5281f2718dbe0.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

