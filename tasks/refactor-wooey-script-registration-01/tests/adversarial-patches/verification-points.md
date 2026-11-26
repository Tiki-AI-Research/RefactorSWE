# Adversarial patches and verification points

Task: refactor-wooey-script-registration-01
Base commit: 6e24ffe16f389a99de28fae3671cbd25df52d51c

This package contains 22 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-0294abf2ef1c.patch)
SHA-256: 0294abf2ef1c9e7d7aa48605346a7dc477ac2dec7e76586366f05b9f3420d394

### VP-0001: The uploaded file was also incorrectly marked as output.

- **requirement**: Ensure that the following incorrect behaviors do not occur: uploading files is also incorrectly marked as output.
- **mutation**: The uploaded file was also incorrectly marked as output. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0002

[patch](patches/P-0002-131b05531c9d.patch)
SHA-256: 131b05531c9d8ecffcbdbaf640742462c4f9654f71e169acecab7645c7a048e7

### VP-0002: Repeat error values, keep the rest of the repeated states unchanged

- **requirement**: Ensure that the following incorrect behaviors do not occur: repeated changes of incorrect values, and maintaining other repeated states.
- **mutation**: Repeat error values, keep the rest of the repeated states unchanged (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0003

[patch](patches/P-0003-17a60be3b52f.patch)
SHA-256: 17a60be3b52fbbc637c1d043b57f43a0b96cf57bc69fc27993dfff35dc183a2b

### VP-0003: Clones new primary keys without reusing the original parameter identity

- **requirement**: Ensure that the correct implementation does not involve cloning a new primary key without reusing the original parameter identity.
- **mutation**: Clones new primary keys without reusing the original parameter identity (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0004

[patch](patches/P-0004-1b563e971194.patch)
SHA-256: 1b563e97119467568ca85f04d50ce7b35acbfe027545ca46b5f9b132c2e7b9c3

### VP-0004: When the historical checksums are repeated, select the first one instead of the last one in the baseline.

- **requirement**: Ensure that the following incorrect behaviors do not occur: When the historical checksums are duplicate, select the first one instead of the last one in the baseline.
- **mutation**: When the historical checksums are repeated, select the first one instead of the last one in the baseline. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0005

[patch](patches/P-0005-3c270a8da043.patch)
SHA-256: 3c270a8da043760ce1ce4f818507a10ed2f79510e2162bba01320badc2f617f6

### VP-0005: The first iteration of the new script starts from version 2.

- **requirement**: The first version of a new script must not start at iteration 2.
- **mutation**: The first iteration of the new script starts from version 2. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0006

[patch](patches/P-0006-43c6a30b293f.patch)
SHA-256: 43c6a30b293f99fe043a9917722b7d6910ed418c032ffd5003d7bc64c9e509aa

### VP-0006: Put the original logic in a long private routine and make the public entry point a wrapper, leaving the responsibilities undivided.

- **requirement**: A long private routine containing the original logic and a thin public wrapper do not divide the responsibilities.
- **mutation**: Put the original logic in a long private routine and make the public entry point a wrapper, leaving the responsibilities undivided. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0007

[patch](patches/P-0007-526e50fb4b74.patch)
SHA-256: 526e50fb4b74eadef6ace7c330a3c5507cc56a1d5813c52a8e009c43747153f8

### VP-0007: Re-link all historical parameters of the same script to the new version, including parameters that have been deleted.

- **requirement**: It is not allowed to perform the following incorrect behaviors: re-link all historical parameters of the same script to the new version, including parameters that have been deleted.
- **mutation**: Re-link all historical parameters of the same script to the new version, including parameters that have been deleted. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0008

[patch](patches/P-0008-5d2a903ae227.patch)
SHA-256: 5d2a903ae227bca0e87508f3ae0291e795432a2e9cd678b4b7a5c6a58911f9e0

### VP-0008: Ignore false default selection options

- **requirement**: Ensure that the correct implementation does not exhibit the following incorrect behaviors: ignoring false default selection options.
- **mutation**: Ignore false default selection options (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0009

[patch](patches/P-0009-5db759653278.patch)
SHA-256: 5db7596532781ed3b9f03bb6837f0b4dbf736bbe8a190b9a91b0e5def9de13f4

### VP-0009: Change the parameter sequence number to increase by 2 in each step.

- **requirement**: Ensure that the following incorrect behaviors do not occur: The parameter number should increase by 2 in each step.
- **mutation**: Change the parameter sequence number to increase by 2 in each step. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0010

[patch](patches/P-0010-7a7024863fdc.patch)
SHA-256: 7a7024863fdc99393dd420b383d8f64bb422bb53fb27b9a97acef554bf19a387

### VP-0010: The successfully mapped error values are no longer None.

- **requirement**: The following incorrect behaviors should not occur: The successfully mapped error values will no longer be None.
- **mutation**: The successfully mapped error values are no longer None. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0011

[patch](patches/P-0011-7d31993c74cd.patch)
SHA-256: 7d31993c74cdcc1968d01bf9990131d606c44bfaf99dde9d0aeb58cd8c84dfc7

### VP-0011: Targeted changes to wooey/backend/utils.py

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: wooey/backend/utils.py)
- **mutation**: Targeted changes to wooey/backend/utils.py (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0012

[patch](patches/P-0012-80b9f97d440a.patch)
SHA-256: 80b9f97d440a9ec89e61a9f3b253d15396cd837629c4daa9e44e038ecdf22760

### VP-0012: Successfully saved the version without checking the content checksum

- **requirement**: Ensure that the correct implementation does not result in the following incorrect behaviors: successful version saved without checking the content checksum.
- **mutation**: Successfully saved the version without checking the content checksum (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0013

[patch](patches/P-0013-81acd576fda8.patch)
SHA-256: 81acd576fda8bc1f9e960cc8b89b882092c1207fd74514e8076322cdd7d9aa4c

### VP-0013: Only existing records have successful mapping of error value changes. Synchronization is still completed.

- **requirement**: The following incorrect behaviors should not occur: Only the recorded mode successfully maps the error value change, and the call still completes the synchronization.
- **mutation**: Only existing records have successful mapping of error value changes. Synchronization is still completed. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0014

[patch](patches/P-0014-84830fa1a4d1.patch)
SHA-256: 84830fa1a4d17fb4ede45820152b8bda94d51e98b0108b662a359d40edb37470

### VP-0014: Targeted changes to wooey/backend/utils.py

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: wooey/backend/utils.py)
- **mutation**: Targeted changes to wooey/backend/utils.py (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0015

[patch](patches/P-0015-8ed8c11859fc.patch)
SHA-256: 8ed8c11859fcabbd84347225c9cdf7bc93afefc804a14faf855bd2765bdcd48e

### VP-0015: The multi-value parameter choice_limit is fixed at 1.

- **requirement**: Do not hardcode choice_limit to 1 for a multivalue argument.
- **mutation**: The multi-value parameter choice_limit is fixed at 1. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0016

[patch](patches/P-0016-92d651bf097b.patch)
SHA-256: 92d651bf097b2f2ed182f815eb11343cd1b8769dcd55f6b499f3c4120c6128f1

### VP-0016: Change the default value of the six parameters ignore_bad_imports

- **requirement**: Ensure that the following incorrect behaviors do not occur: Changing the default values of the six parameters ignore_bad_imports
- **mutation**: Change the default value of the six parameters ignore_bad_imports (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0017

[patch](patches/P-0017-abd1553cc823.patch)
SHA-256: abd1553cc823676e7200fe8def222513a5fe38ddd84eccad7b20450f50a58fcd

### VP-0017: The new declaration version is not reset to iteration 1.

- **requirement**: A newly declared version must reset the iteration to 1.
- **mutation**: The new declaration version is not reset to iteration 1. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0018

[patch](patches/P-0018-b68f01444ae5.patch)
SHA-256: b68f01444ae5defb3fa19d34676f9bd4735b0dee97997a4a5812a1ccaae2c5ef

### VP-0018: Discard explicit schema default values

- **requirement**: Ensure that the correct implementation does not exhibit the following incorrect behaviors: Discarding explicit schema default values
- **mutation**: Discard explicit schema default values (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0021

[patch](patches/P-0021-c38e92fa335a.patch)
SHA-256: c38e92fa335a158e430ddaef19657e3aebbdde6862949468a574f0a584318dc9

### VP-0021: Max Iteration Plus 2 for the Same Declaration Version

- **requirement**: The maximum iteration for the same declared version must not increase by 2.
- **mutation**: Max Iteration Plus 2 for the Same Declaration Version (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0023

[patch](patches/P-0023-cef5437053ce.patch)
SHA-256: cef5437053ce9241d16c1eac5da222aca3519eb0a1e86232ed3f338eccddbf1b

### VP-0023: After successful registration, if the source files in the storage configuration are accidentally deleted, keep a local parsing copy.

- **requirement**: Ensure that the following incorrect behaviors do not occur: After successful registration, accidentally delete the source files in the storage configuration, and retain the local parsing copies.
- **mutation**: After successful registration, if the source files in the storage configuration are accidentally deleted, keep a local parsing copy. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0025

[patch](patches/P-0025-e1223af99950.patch)
SHA-256: e1223af99950190a472951f851189e2b1757b9bafe5fdd5a532701946f34e992

### VP-0025: All fields in the parameter form should be replaced with CharField.

- **requirement**: Ensure that the following incorrect behaviors do not occur: All parameter form field are changed to CharField.
- **mutation**: All fields in the parameter form should be replaced with CharField. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

## P-0026

[patch](patches/P-0026-efac92e96656.patch)
SHA-256: efac92e9665655ee40e7e5c769b2f83288af755ddc95c58af295fcd6bcda41e9

### VP-0026: Please set all required fields to False.

- **requirement**: Please ensure that the following incorrect behaviors do not occur: all required values are set to False.
- **mutation**: Please set all required fields to False. (changed files: wooey/backend/utils.py)
- **setup**: Apply this patch to the clean baseline at 6e24ffe16f38, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target input did not arrive. Upstream import/collection errors

