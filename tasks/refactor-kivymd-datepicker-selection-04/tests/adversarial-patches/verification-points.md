# Adversarial patches and verification points

Task: refactor-kivymd-datepicker-selection-04
Base commit: 4a2617ea24e13ef2540c37edb95a54ef02e78707

This package contains 31 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-0f4d3371723e.patch)
SHA-256: 0f4d3371723eb054ac514cea2c162b9fb501e596de241234549b3ff889aee2e1

### VP-0001: toggle only opens, does not close

- **requirement**: Ensure that the correct implementation does not exhibit the following incorrect behaviors: toggle only opens, not closes.
- **mutation**: toggle only opens, does not close (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0002

[patch](patches/P-0002-1242bf331a51.patch)
SHA-256: 1242bf331a51b7489d082aa80f3e37ccbc0fde0880926cad3dca064664c74cf9

### VP-0002: Change only the default min_year from 1914 to 1915.

- **requirement**: Change only the default min_year from 1914 to 1915.
- **mutation**: Change only the default min_year from 1914 to 1915. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached

## P-0003

[patch](patches/P-0003-1401949d92db.patch)
SHA-256: 1401949d92dbc6acbcdd11f94dd5e0ac345f3e7a27522ac1aebe4f01d07204ae

### VP-0003: Calendar update loses visible date

- **requirement**: Ensure that the calendar update retains the visible date.
- **mutation**: Calendar update loses visible date (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0004

[patch](patches/P-0004-1c227b3289b3.patch)
SHA-256: 1c227b3289b3b9ccfbae70091ac59bd2475670c6c9beb2f660d0081c7c0e2b70

### VP-0004: One valid touch will be applied repeatedly and distributed twice

- **requirement**: Ensure that correct implementations do not involve the following incorrect behaviors: applying the same action twice due to a single valid touch.
- **mutation**: One valid touch will be applied repeatedly and distributed twice (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0011

[patch](patches/P-0011-39b28e627383.patch)
SHA-256: 39b28e6273835641c28fe48aa0c3b7af53368f360fb5f4832fd0e096b41db5d0

### VP-0011: Generate only months 1 through 11, omitting December.

- **requirement**: Generate only months 1 through 11, omitting December.
- **mutation**: Generate only months 1 through 11, omitting December. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached

## P-0012

[patch](patches/P-0012-3a963a153043.patch)
SHA-256: 3a963a15304352415a3803b6380bab11460658d8cbdea269d2cf354a05fec2fa

### VP-0012: The year list contains an error with the upper limit.

- **requirement**: Please ensure that the following incorrect behaviors do not occur: errors in the list of years, including the upper limit.
- **mutation**: The year list contains an error with the upper limit. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0013

[patch](patches/P-0013-41cd371d0f33.patch)
SHA-256: 41cd371d0f33bebecc6cab09f458fee14abc3ab0be13eee8ee6dae933e19ea45

### VP-0013: Copy the entire month callback/recovery method to the modal, keeping the common upstream wrapper.

- **requirement**: Please ensure that the following incorrect behaviors do not occur: copying the entire month callback/restoration method to the modal, and retaining the common upstream wrapper.
- **mutation**: Copy the entire month callback/recovery method to the modal, keeping the common upstream wrapper. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0014

[patch](patches/P-0014-42bc386b4922.patch)
SHA-256: 42bc386b49220975ff453c7b1e18ef3385506d610e4823e6d3634a2b0de97cdb

### VP-0014: picker date string separator changed

- **requirement**: Ensure that the date string separator used by the picker does not change.
- **mutation**: picker date string separator changed (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0015

[patch](patches/P-0015-4a9f1ac3f7fb.patch)
SHA-256: 4a9f1ac3f7fb7a5a96c17b7c2bb5ec3007dd045527a0d0064cbbd4604193771c

### VP-0015: List scaling error after docking is closed

- **requirement**: Ensure that the list scaling does not occur after the docking is closed.
- **mutation**: List scaling error after docking is closed (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0017

[patch](patches/P-0017-51f504015c14.patch)
SHA-256: 51f504015c143fe1c1651784fe444cef42f826a47d7322f78af3ed3fc8fc4c79

### VP-0017: Date range error elimination deadline

- **requirement**: Ensure that the following incorrect behaviors do not occur: incorrect date range exclusion at the end.
- **mutation**: Date range error elimination deadline (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0018

[patch](patches/P-0018-561184d0df98.patch)
SHA-256: 561184d0df9806953e58b68487c08ddbf725ae1a49e8a8fe45593e254fa9bdff

### VP-0018: Modal close pre-setting zoom error

- **requirement**: Ensure that the pre-setting of zoom does not occur after the modal is closed.
- **mutation**: Modal close pre-setting zoom error (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0020

[patch](patches/P-0020-5ea438868dee.patch)
SHA-256: 5ea438868dee27c674a9b9b4393d8c65066a1797d4db9e0efec3fa1919cb4e8d

### VP-0020: Declarative list date name key-value missing

- **requirement**: Ensure that the following incorrect behaviors do not occur: Loss of declarative list date name key-value pairs.
- **mutation**: Declarative list date name key-value missing (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0022

[patch](patches/P-0022-67460ee261f9.patch)
SHA-256: 67460ee261f97c6ffe557e56885dfc1db0507de2950037f94be007328d6061c7

### VP-0022: Directly show error progression memory switch, the first subsequent menu event should still be displayed but actually closed.

- **requirement**: Directly show error progression memory switch, the first subsequent menu event should still be displayed but actually closed.
- **mutation**: Directly show error progression memory switch, the first subsequent menu event should still be displayed but actually closed. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached

## P-0027

[patch](patches/P-0027-764467693d53.patch)
SHA-256: 764467693d53aa5681ad118828881f387cb8e56ad74ec2c7f25e61104e0b8803

### VP-0027: Allow years to exceed the upper limit by one year

- **requirement**: The year arrow must not move one year beyond the upper limit.
- **mutation**: Allow years to exceed the upper limit by one year (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0030

[patch](patches/P-0030-7ec5bccd9901.patch)
SHA-256: 7ec5bccd99018c50a804b40ee735197acc98500bf61699928373f9a337ef129a

### VP-0030: month payload as a string

- **requirement**: Ensure that the correct implementation does not exhibit the following incorrect behaviors: month payload should be converted into a string.
- **mutation**: month payload as a string (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0031

[patch](patches/P-0031-88a9a61c1aa6.patch)
SHA-256: 88a9a61c1aa621ba727ffa6344500cf79ac2cb66d4143ef2771182263b1e1325

### VP-0031: The modal touch path is directly copied from update_calendar and on_select_year. It maintains the correct date/event results and the selected items are written back.

- **requirement**: The modal touch path is directly copied from update_calendar and on_select_year. It maintains the correct date/event results and the selected items are written back.
- **mutation**: The modal touch path is directly copied from update_calendar and on_select_year. It maintains the correct date/event results and the selected items are written back. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached

## P-0033

[patch](patches/P-0033-8bd0d0f5e2c7.patch)
SHA-256: 8bd0d0f5e2c737e0681b88a6bd615a40be7f4573efd384d85aedcf393a1e6a89

### VP-0033: The imported name is no longer available as a valid picker type.

- **requirement**: Ensure that the following incorrect behaviors do not occur: The original imported name is no longer available for the picker type.
- **mutation**: The imported name is no longer available as a valid picker type. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0035

[patch](patches/P-0035-90cae709f7ae.patch)
SHA-256: 90cae709f7ae8e6767eee98b3f7ebcbd1b3d314d1c414a1a7351d250c66967ab

### VP-0035: Modal menu width reduction error 1dp

- **requirement**: Ensure that the following incorrect behaviors do not occur: Modal menu width reduction error 1dp
- **mutation**: Modal menu width reduction error 1dp (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0040

[patch](patches/P-0040-9f4980ab99d1.patch)
SHA-256: 9f4980ab99d1d4d0f0165a164d5cfc1c26ca146d0eac1b2e2db0892c518c444d

### VP-0040: Copy the entire line and write it back to the modal line for implementation.

- **requirement**: Do not duplicate the entire row-selection write-back implementation in modal rows.
- **mutation**: Copy the entire line and write it back to the modal line for implementation. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0043

[patch](patches/P-0043-ad34add281dd.patch)
SHA-256: ad34add281dd28cb6adffc964b509ddc9ad234e8232336c82fdb3eb72e89fa7d

### VP-0043: next error step two months

- **requirement**: The following incorrect behaviors should not occur: next error step for two months
- **mutation**: next error step two months (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0044

[patch](patches/P-0044-b810c4b40998.patch)
SHA-256: b810c4b40998bd1437d5a7973849c3dee1c931ea0e9ff952eac6b7b912ae28e3

### VP-0044: Retain public upstream wrappers

- **requirement**: Ensure that the following incorrect behaviors do not occur: retaining public upstream wrappers
- **mutation**: Retain public upstream wrappers (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0047

[patch](patches/P-0047-beb0ca204a10.patch)
SHA-256: beb0ca204a10702ca5f0f574c21c5deda544b7972a8c0a27e26e846b89594e82

### VP-0047: Please correct the error in the docked selection label and display the year and month.

- **requirement**: Please correct the error in the docked selection label and display the year and month.
- **mutation**: Please correct the error in the docked selection label and display the year and month. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached

## P-0048

[patch](patches/P-0048-c094d3d8d774.patch)
SHA-256: c094d3d8d774aafe5eb540b22dee2bf3a44e5c7aaef76675c1376dffff2b5c6d

### VP-0048: Month row incorrectly uses the selected year instead of the displayed year

- **requirement**: Ensure that the following incorrect behaviors do not occur: incorrect use of the selected year instead of the displayed year in the month row.
- **mutation**: Month row incorrectly uses the selected year instead of the displayed year (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0049

[patch](patches/P-0049-c0d15bd6b8bb.patch)
SHA-256: c0d15bd6b8bbb97e0edad568a4dd1e649038bb8d501294a3a8c7ea4b7b7b6044

### VP-0049: Year Row Error Application Next Year

- **requirement**: Please ensure that the following incorrect behaviors do not occur: year row error applies to the next year.
- **mutation**: Year Row Error Application Next Year (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0050

[patch](patches/P-0050-c36ca387a77e.patch)
SHA-256: c36ca387a77e9e612ae7003d4a32c60469433fc61fa29cb4dcb6cb8ee7a3730c

### VP-0050: The fade-out has been reduced from 0.2 seconds to 0.01 seconds.

- **requirement**: The following incorrect behaviors should not occur: the fade-out time should be shortened from 0.2 seconds to 0.01 seconds.
- **mutation**: The fade-out has been reduced from 0.2 seconds to 0.01 seconds. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0051

[patch](patches/P-0051-c9074cae53c8.patch)
SHA-256: c9074cae53c8c82731a2b9072114039a12731b8dea2b5b23885e507eab89463a

### VP-0051: Refresh Error Distribution Selection Event

- **requirement**: Ensure that the correct implementation avoids the following incorrect behaviors: directly refreshing error-prone selection events.
- **mutation**: Refresh Error Distribution Selection Event (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0052

[patch](patches/P-0052-ccc6fcd450c1.patch)
SHA-256: ccc6fcd450c1dfa4e5fe0044e637d8d481dd2c0cc85bcb022231a2a08dfc2e2b

### VP-0052: The base variadic handler still accepts parameters, but it incorrectly modifies the picker, violating the no-op rule.

- **requirement**: The base variadic handler still accepts parameters, but it incorrectly modifies the picker, violating the no-op rule.
- **mutation**: The base variadic handler still accepts parameters, but it incorrectly modifies the picker, violating the no-op rule. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached

## P-0054

[patch](patches/P-0054-d1f72be0e6eb.patch)
SHA-256: d1f72be0e6eb7d89c86d8aacada64df0bce5419cdbe270cd66c1468d9bdab059

### VP-0054: Stopping menu height deduction error 1dp

- **requirement**: A correct implementation must not subtract the wrong 1dp from the docked menu height.
- **mutation**: Stopping menu height deduction error 1dp (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0055

[patch](patches/P-0055-e2004b6a6df2.patch)
SHA-256: e2004b6a6df2c8ed3c9b517525dcc152f8de0ece88c3d8e25ae5aca75711c47f

### VP-0055: When the picker is opened, the scrim is not displayed.

- **requirement**: The input picker must show the scrim when opened.
- **mutation**: When the picker is opened, the scrim is not displayed. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0060

[patch](patches/P-0060-ef1408e49000.patch)
SHA-256: ef1408e490009362b191557fde495856c72ea6230f9bce29db8b956d866febf3

### VP-0060: KV Right Arrow Wrong Route Prev

- **requirement**: A correct implementation must not route the KV right arrow to prev.
- **mutation**: KV Right Arrow Wrong Route Prev (changed files: kivymd/uix/pickers/datepicker/datepicker.py, kivymd/uix/pickers/datepicker/datepicker.kv)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion

## P-0061

[patch](patches/P-0061-f17949e9e0ad.patch)
SHA-256: f17949e9e0adf8ba736a67c673e07f72476c73a4a4c657e045941463cc1503e2

### VP-0061: Do not write back list data for selected lines.

- **requirement**: Ensure that the following incorrect behaviors do not occur: do not write back list data while selecting lines.
- **mutation**: Do not write back list data for selected lines. (changed files: kivymd/uix/pickers/datepicker/datepicker.py)
- **setup**: Apply this patch to the clean baseline at 4a2617ea24e1, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached; Uncompleted collection/execution and no reaching of target assertion
