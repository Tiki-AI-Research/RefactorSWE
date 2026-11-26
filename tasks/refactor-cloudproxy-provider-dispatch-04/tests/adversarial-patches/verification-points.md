# Adversarial patches and verification points

Task: refactor-cloudproxy-provider-dispatch-04
Base commit: 06f8a9d8f6f14867125b813a098243794f85d218

This package contains 20 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-0230b2a7f7ac.patch)
SHA-256: 0230b2a7f7ac2997f4ba67fcb201afbae7c511f6ab1a756c79cc60329027e3d2

### VP-0001: List Exclude Top-Level Secrets

- **requirement**: Do not use command exit values instead
- **mutation**: List Exclude Top-Level Secrets (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0002

[patch](patches/P-0002-077c718a90cd.patch)
SHA-256: 077c718a90cd0466b332a8be96c413e6cb7b18e4c81aac018337a02c44a48107

### VP-0002: DO Direct Construction Requires Continued Region

- **requirement**: Do not use command exit values instead
- **mutation**: DO Direct Construction Requires Continued Region (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0003

[patch](patches/P-0003-16744af70028.patch)
SHA-256: 16744af70028825babdcea7c65d0afe61f99638ff0d0c28d943dac6e46c29709

### VP-0003: The provider types assume their respective construction responsibilities, eliminating the condition chain of shared name literals.

- **requirement**: Do not use command exit values instead
- **mutation**: The provider types assume their respective construction responsibilities, eliminating the condition chain of shared name literals. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0006

[patch](patches/P-0006-4c4eff497140.patch)
SHA-256: 4c4eff497140cd715d9407394e967f18f8b5e0cbc3bfb3ffb65368ae67ce38ab

### VP-0006: Successful rollback with valid general configurations for unmodeled or unknown names.

- **requirement**: Do not use command exit values instead
- **mutation**: Successful rollback with valid general configurations for unmodeled or unknown names. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0007

[patch](patches/P-0007-5baaede10470.patch)
SHA-256: 5baaede10470480f983c9d36a602b27361094ccea6ef443f74ed48dfa923c164

### VP-0007: List returns all configured names, metadata, and existing model loads.

- **requirement**: Do not use command exit values instead
- **mutation**: List returns all configured names, metadata, and existing model loads. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0008

[patch](patches/P-0008-631a39a9b370.patch)
SHA-256: 631a39a9b37068626ffacf5230a8d62e1fc1b63fcda96f1db34168da9eb2f46f

### VP-0008: Explicit top-level default values are not overridden by default instances.

- **requirement**: Do not use command exit values instead
- **mutation**: Explicit top-level default values are not overridden by default instances. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0009

[patch](patches/P-0009-63c93dea2751.patch)
SHA-256: 63c93dea27515bfadc83bbe27c45cfb0dcf80a7e7b83c9450349c8463d88fd46

### VP-0009: The default policies of the provider are managed by the corresponding types. Duplicate regions/AMIs are deduplicated.

- **requirement**: Do not use command exit values instead
- **mutation**: The default policies of the provider are managed by the corresponding types. Duplicate regions/AMIs are deduplicated. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0010

[patch](patches/P-0010-73097830f477.patch)
SHA-256: 73097830f4776a2c656f729b6a18db5836f1bbb8532046e68d9cd938acfd9982

### VP-0010: Per-instance scaling accepts model instances and mappings and preserves each instance's values.

- **requirement**: Do not use command exit values instead
- **mutation**: Per-instance scaling accepts model instances and mappings and preserves each instance's values. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0011

[patch](patches/P-0011-75da76034c98.patch)
SHA-256: 75da76034c9888571eeae0e5f6caed063f7cfa0ceb89d9fd0f616c65f8a0b6a3

### VP-0011: When the AWS top-level does not have an ami, fill in the default instance ami.

- **requirement**: Do not use command exit values instead
- **mutation**: When the AWS top-level does not have an ami, fill in the default instance ami. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0012

[patch](patches/P-0012-837865922439.patch)
SHA-256: 837865922439b49b60edfa2183d40ac42598ea889372a134cfdb95971b73e4b5

### VP-0012: Existing provider and instance fields, as well as nested instance data, are retained.

- **requirement**: Do not use command exit values instead
- **mutation**: Existing provider and instance fields, as well as nested instance data, are retained. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0013

[patch](patches/P-0013-858031623101.patch)
SHA-256: 858031623101ed34ada5fef6739b7ab7bd337d35fbfa7565a2c49176cae956fd

### VP-0013: Backfill does not add keys to the top-level mapping of the caller

- **requirement**: Do not use command exit values instead
- **mutation**: Backfill does not add keys to the top-level mapping of the caller (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0014

[patch](patches/P-0014-85c7267124da.patch)
SHA-256: 85c7267124da5fec253312054a5424d9a7be84cff71db657e8d40ef52fd5023d

### VP-0014: Scale both fields while keeping the zero default values and non-negative boundaries.

- **requirement**: Do not use command exit values instead
- **mutation**: Scale both fields while keeping the zero default values and non-negative boundaries. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0016

[patch](patches/P-0016-b5c3f0c52e19.patch)
SHA-256: b5c3f0c52e192cd932871a76f813286dd7371190f21360cf5d67c1b245f52806

### VP-0016: GCP Direct Construction continues to require three original required fields.

- **requirement**: Do not use command exit values instead
- **mutation**: GCP Direct Construction continues to require three original required fields. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0018

[patch](patches/P-0018-bb6da36ff361.patch)
SHA-256: bb6da36ff3612d2eac562c527f52e1784ccd3d003088c7992b16b9b8ca7b8055

### VP-0018: List continues to call the originally public factory names, which can be overwritten.

- **requirement**: Do not use command exit values instead
- **mutation**: List continues to call the originally public factory names, which can be overwritten. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0019

[patch](patches/P-0019-d2cdfc7384e9.patch)
SHA-256: d2cdfc7384e93b8bab8d5fb6db126f6386398cf90a562bc72b141926be87c8ff

### VP-0019: AWS spot Boolean field and False default value remain unchanged

- **requirement**: Do not use command exit values instead
- **mutation**: AWS spot Boolean field and False default value remain unchanged (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0020

[patch](patches/P-0020-d6bec0b6656e.patch)
SHA-256: d6bec0b6656ea5978b535eaa01ecbf650d5eaf4d902bbd84e6dde8a52d4ee420

### VP-0020: Provider's top-level scaling compatible model instances and mappings

- **requirement**: Do not use command exit values instead
- **mutation**: Provider's top-level scaling compatible model instances and mappings (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0021

[patch](patches/P-0021-d7ef9b694ec8.patch)
SHA-256: d7ef9b694ec8adb0fe2b548cdadb2801b393f8520ea2e8669da36b73f1af928c

### VP-0021: When the DO top level lacks a region, the default instance region is populated.

- **requirement**: Do not use command exit values instead
- **mutation**: When the DO top level lacks a region, the default instance region is populated. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0022

[patch](patches/P-0022-d9ac03448a40.patch)
SHA-256: d9ac03448a404b1a53aec1cb07dfededa553b8cec53af8b1b762a9e35a0bae59

### VP-0022: Configured provider details retain the fixed response structure and value source.

- **requirement**: Do not use command exit values instead
- **mutation**: Configured provider details retain the fixed response structure and value source. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0023

[patch](patches/P-0023-da39a61f66c0.patch)
SHA-256: da39a61f66c07a5ae2dae91f1e4eaffc50a43f221b998ec8bef6f5de2f2b22b3

### VP-0023: When the AWS top-level lacks a region, the default instance region is used for fallback.

- **requirement**: Do not use command exit values instead
- **mutation**: When the AWS top-level lacks a region, the default instance region is used for fallback. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.

## P-0024

[patch](patches/P-0024-eb653e072534.patch)
SHA-256: eb653e072534d421321417efa6034b8bfe428feb6d089867f25f15c145249086

### VP-0024: No provider details configured. Keep the original 404.

- **requirement**: Do not use command exit values instead
- **mutation**: No provider details configured. Keep the original 404. (changed files: cloudproxy/main.py)
- **setup**: Apply this patch to the clean baseline at 06f8a9d8f6f1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The corresponding target test should have failed real assertions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target test was not executed and the target behavior cannot be determined.
