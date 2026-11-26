# Adversarial patches and verification points

Task: ir-sim-env_param-world_param-path_param-02
Base commit: 7c086d9902694c3c56f0e4259cc01c7fe7af6693

This package contains 11 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-028caa23200c.patch)
SHA-256: 028caa23200c86133414ee244a05366f56c6e3326406cd24269e810341a75912

### VP-0001: The world module's non-parameter ordinary attributes should not be written into parameter instances.

- **requirement**: The world module's non-parameter ordinary attributes should not be written into parameter instances.
- **mutation**: The world module's non-parameter ordinary attributes should not be written into parameter instances. (changed files: irsim/config/env_param.py, irsim/config/param_storage.py, irsim/config/path_param.py, irsim/config/world_param.py, among others)
- **setup**: Apply this patch to the clean baseline at 7c086d990269, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application or collection failed

## P-0002

[patch](patches/P-0002-0db834f2e320.patch)
SHA-256: 0db834f2e320f3928425e142ae9b2db76c93a6168523e62ad82f9917fac3d95d

### VP-0002: Only install non-module delegation objects in path_param.py, and keep the getitem delegation to isolate module identity defects.

- **requirement**: The path_param exported from the configuration package should maintain existing module objects and cannot be changed to non-module delegate objects.
- **mutation**: Only install non-module delegation objects in path_param.py, and keep the getitem delegation to isolate module identity defects. (changed files: irsim/config/env_param.py, irsim/config/param_storage.py, irsim/config/path_param.py, irsim/config/world_param.py, among others)
- **setup**: Apply this patch to the clean baseline at 7c086d990269, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The value assertion of 0.0 is merely a strict sentinel, not an inevitable conclusion of the F2P partial score formula.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. getitem delegate failed; Patch application or collection failed

## P-0003

[patch](patches/P-0003-246aea72c49d.patch)
SHA-256: 246aea72c49d92aa77db71c41eb69fb28df62026cb0b37d26d7713abd56fec74

### VP-0003: After directly assigning current, the proxy should read the current alias instead of the old list.

- **requirement**: After directly assigning current, the proxy should read the current alias instead of the old list.
- **mutation**: After directly assigning current, the proxy should read the current alias instead of the old list. (changed files: irsim/config/env_param.py, irsim/config/param_storage.py, irsim/config/path_param.py, irsim/config/world_param.py, among others)
- **setup**: Apply this patch to the clean baseline at 7c086d990269, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application or collection failed

## P-0004

[patch](patches/P-0004-5d5faa9d6790.patch)
SHA-256: 5d5faa9d6790c5ce365aadc36e36c5b7873906203e47cbd998e09a05db9aaa58

### VP-0004: Please use the new lists for the indices and bind after replacing with_instances.

- **requirement**: Please use the new lists for the indices and bind after replacing with_instances.
- **mutation**: Please use the new lists for the indices and bind after replacing with_instances. (changed files: irsim/config/env_param.py, irsim/config/param_storage.py, irsim/config/path_param.py, irsim/config/world_param.py, among others)
- **setup**: Apply this patch to the clean baseline at 7c086d990269, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application or collection failed

## P-0005

[patch](patches/P-0005-69b8e0d99dbe.patch)
SHA-256: 69b8e0d99dbe2492b2409eb19afb7dafdce39dad53afcf78c623d7bb175b9aa4

### VP-0005: The path proxy reading of fig_path must reflect the current instance.

- **requirement**: The path proxy reading of fig_path must reflect the current instance.
- **mutation**: The path proxy reading of fig_path must reflect the current instance. (changed files: irsim/config/env_param.py, irsim/config/param_storage.py, irsim/config/path_param.py, irsim/config/world_param.py, among others)
- **setup**: Apply this patch to the clean baseline at 7c086d990269, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application or collection failed

## P-0006

[patch](patches/P-0006-98ea42e19e9f.patch)
SHA-256: 98ea42e19e9feaa47654a134223fffbfce8e1a340749f47e937a7564c2468523

### VP-0006: Before explicitly binding, proxy reading must use index 0 for default instance fields.

- **requirement**: Before explicitly binding, proxy reading must use index 0 for default instance fields.
- **mutation**: Before explicitly binding, proxy reading must use index 0 for default instance fields. (changed files: irsim/config/env_param.py, irsim/config/param_storage.py, irsim/config/path_param.py, irsim/config/world_param.py, among others)
- **setup**: Apply this patch to the clean baseline at 7c086d990269, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application or collection failed

## P-0007

[patch](patches/P-0007-87e93d0e8c46.patch)
SHA-256: 87e93d0e8c46511a589e6f838fd9de7407121d1609bff7fa04b48e25f5ccc59c

### VP-0007: The negative index incorrectly returned the first instance.

- **requirement**: The negative index incorrectly returned the first instance.
- **mutation**: The above targeted behavior defects are injected into the candidate implementation irsim/config/param_storage.py; the scoring tests are not modified.
- **setup**: Run the original tests/test.sh after applying the complete candidates on the clean baseline 7c086d9902694c3c56f0e4259cc01c7fe7af6693.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0008

[patch](patches/P-0008-6490040c0402.patch)
SHA-256: 6490040c0402e0ee1c1e6187386649b566ef85c6c604e49b46b87ce7a9378e9f

### VP-0008: Non-empty storage bind appended instances without replacing index zero

- **requirement**: Non-empty storage bind appended instances without replacing index zero
- **mutation**: The above targeted behavior defects are injected into the candidate implementation irsim/config/param_storage.py; the scoring tests are not modified.
- **setup**: Run the original tests/test.sh after applying the complete candidates on the clean baseline 7c086d9902694c3c56f0e4259cc01c7fe7af6693.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0009

[patch](patches/P-0009-316950b659a4.patch)
SHA-256: 316950b659a45068db95b19ea0667801aa64365f52b8b4142ef5d53bf0a0bcc1

### VP-0009: Index Zero Assignment Not Updated Current Instance Alias

- **requirement**: Index Zero Assignment Not Updated Current Instance Alias
- **mutation**: The above targeted behavior defects are injected into the candidate implementation irsim/config/param_storage.py; the scoring tests are not modified.
- **setup**: Run the original tests/test.sh after applying the complete candidates on the clean baseline 7c086d9902694c3c56f0e4259cc01c7fe7af6693.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0010

[patch](patches/P-0010-1d83ba2a7b16.patch)
SHA-256: 1d83ba2a7b160ad147c059151cd5e9312c05cd216e3df64a60521d5f807b4481

### VP-0010: Negative index assignment error message deviates from the public contract

- **requirement**: Negative index assignment error message deviates from the public contract
- **mutation**: The above targeted behavior defects are injected into the candidate implementation irsim/config/param_storage.py; the scoring tests are not modified.
- **setup**: Run the original tests/test.sh after applying the complete candidates on the clean baseline 7c086d9902694c3c56f0e4259cc01c7fe7af6693.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0011

[patch](patches/P-0011-8b107bbb01c9.patch)
SHA-256: 8b107bbb01c915b525297614ae62f28cdd0b1ebe5842360dc13aedb0192d1f5a

### VP-0011: The consumer ignores the owner parameter and always reads the global binding.

- **requirement**: The consumer ignores the owner parameter and always reads the global binding.
- **mutation**: The above targeted behavior defects are injected into the candidate implementation irsim/config/param_storage.py; the scoring tests are not modified.
- **setup**: Run the original tests/test.sh after applying the complete candidates on the clean baseline 7c086d9902694c3c56f0e4259cc01c7fe7af6693.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

