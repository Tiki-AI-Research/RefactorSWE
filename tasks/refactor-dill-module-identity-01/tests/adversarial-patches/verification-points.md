# Adversarial patches and verification points

Task: refactor-dill-module-identity-01
Base commit: 50d93fe52c84cdbfd81c39f5adba68f627fd330b

This package contains 44 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-036c6cbee20a.patch)
SHA-256: 036c6cbee20a5231eff378eb94ec2e7e9ed9c5b8a2dc4e448a717aca69c19f4c

### VP-0001: Targeted regression: dump saves the state of the selected module and returns None: The values and names of the selected module in the readable archive are correct, the result is normal.

- **requirement**: dump saves the state of the selected module and returns None: The values and names of the selected module in the readable archive are correct, the result is normal.
- **mutation**: Targeted regression: dump saves the state of the selected module and returns None: The values and names of the selected module in the readable archive are correct, the result is normal. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0002

[patch](patches/P-0002-03a78d97b457.patch)
SHA-256: 03a78d97b457dada7178afff2eac2e67213343a17e1f02ab72ef17d17a687738

### VP-0002: Targeted regression: Supported rules do not have any extensibility.

- **requirement**: Supported rules do not have any extensibility.
- **mutation**: Targeted regression: Supported rules do not have any extensibility. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0003

[patch](patches/P-0003-05b82eb8e503.patch)
SHA-256: 05b82eb8e5036ce3c5935b1ea1710fcc1f86e7573ff61847989807c6a6901cf2

### VP-0003: Targeted regression: dump keeps the order of close failures: Internal close errors are propagated, and when there are save errors at the same time, they are prioritized over save errors.

- **requirement**: dump keeps the order of close failures: Internal close errors are propagated, and when there are save errors at the same time, they are prioritized over save errors.
- **mutation**: Targeted regression: dump keeps the order of close failures: Internal close errors are propagated, and when there are save errors at the same time, they are prioritized over save errors. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0004

[patch](patches/P-0004-06620a4907e5.patch)
SHA-256: 06620a4907e59258a6b994b3ea71b1779616a5ffe23f1bcadc271e540b76be73

### VP-0004: Targeted regression: Session state self-reference and function globals semantics maintained: The restored module self-reference points to the restored module.

- **requirement**: Session state self-reference and function globals semantics maintained: The restored module self-reference points to the restored module; session function globals points to a dictionary of restoration targets, with the original value semantics preserved.
- **mutation**: Targeted regression: Session state self-reference and function globals semantics maintained: The restored module self-reference points to the restored module. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0005

[patch](patches/P-0005-0920a3f92987.patch)
SHA-256: 0920a3f92987159611e0e8f150dcbbc33c030a8f8335cd16a44fa4665da9408a

### VP-0005: Targeted regression: asdict(update=True) Retains the previous state that was not overwritten by the archive: The current additional entries are retained, and the saved entries are overwritten with the archive values. The original module content is not modified.

- **requirement**: asdict(update=True) Retains the previous state that was not overwritten by the archive: The current additional entries are retained, and the saved entries are overwritten with the archive values. The original module content is not modified.
- **mutation**: Targeted regression: asdict(update=True) Retains the previous state that was not overwritten by the archive: The current additional entries are retained, and the saved entries are overwritten with the archive values. The original module content is not modified. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0006

[patch](patches/P-0006-09d2a06179c7.patch)
SHA-256: 09d2a06179c703c6f3637ad38e838b8ff1b7b7ff65a4b1bc9425b96680607731

### VP-0006: Targeted regression: The caller reader that holds a peek is still open: The peek reader remains open after the call.

- **requirement**: The caller reader that holds a peek is still open: The peek reader remains open after the call.
- **mutation**: Targeted regression: The caller reader that holds a peek is still open: The peek reader remains open after the call. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0007

[patch](patches/P-0007-165d6d3a232e.patch)
SHA-256: 165d6d3a232e7fa779bb13af2666862e7b25caed1ca4d9451beb6015c776529b

### VP-0007: Targeted regression: asdict rejects symlink source: OSError

- **requirement**: asdict rejects symlink. Source: OSError; the linked target is not readable as a recovery dictionary.
- **mutation**: Targeted regression: asdict rejects symlink source: OSError (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0008

[patch](patches/P-0008-219d8d9c1e47.patch)
SHA-256: 219d8d9c1e4719bd9719bfbea7156cd568d7bcae30dc7e825b95ec2c651a9cb0

### VP-0008: Targeted regression: dump keeps the caller writable stream open: The save operation is successful or failed, but the original caller stream is not closed upon entry.

- **requirement**: dump keeps the caller writable stream open: The save operation is successful or failed, but the original caller stream is not closed upon entry.
- **mutation**: Targeted regression: dump keeps the caller writable stream open: The save operation is successful or failed, but the original caller stream is not closed upon entry. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0009

[patch](patches/P-0009-2de20aabaa35.patch)
SHA-256: 2de20aabaa35e8ca4529e1b6f5208b8d1451214f8f15c48634c6df510ee4eaff

### VP-0009: Targeted regression: asdict remains open with a peeked caller reader: remains open after the received peek reader call

- **requirement**: asdict remains open with a peeked caller reader: remains open after the received peek reader call
- **mutation**: Targeted regression: asdict remains open with a peeked caller reader: remains open after the received peek reader call (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0010

[patch](patches/P-0010-2e5f0af17c5d.patch)
SHA-256: 2e5f0af17c5d3f7fe55b727910500c588ac8b3d841186509b599708a37213fa5

### VP-0010: Targeted regression: Failed to load after registration for runtime; temporary registration is also revoked. If there is an exception during registration and close is successful, the original exception is propagated. The temporary sys.modules item does not exist.

- **requirement**: Failed to load after registration for runtime; temporary registration is also revoked. If there is an exception during registration and close is successful, the original exception is propagated. The temporary sys.modules item does not exist.
- **mutation**: Targeted regression: Failed to load after registration for runtime; temporary registration is also revoked. If there is an exception during registration and close is successful, the original exception is propagated. The temporary sys.modules item does not exist. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0011

[patch](patches/P-0011-2f03f7520510.patch)
SHA-256: 2f03f752051074fc4707d9f7d994408da425434b46e1b8aa1aebe83ae37e5491

### VP-0011: Targeted regression: Maintain normal upstream behavior

- **requirement**: Maintain normal upstream behavior
- **mutation**: Targeted regression: Maintain normal upstream behavior (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0012

[patch](patches/P-0012-36d832a28bc8.patch)
SHA-256: 36d832a28bc8418e49b3f6f94e6eab642bcc75efd7421fcf7e2acc6bff42011a

### VP-0012: Targeted regression: Maintain normal upstream behavior

- **requirement**: Maintain normal upstream behavior
- **mutation**: Targeted regression: Maintain normal upstream behavior (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0013

[patch](patches/P-0013-39f10741cc8e.patch)
SHA-256: 39f10741cc8e9bcc8324e7ecdf0e43f6e9f82b60dbb287be44becad568c55951

### VP-0013: Targeted regression: Maintain normal upstream behavior

- **requirement**: Maintain normal upstream behavior
- **mutation**: Targeted regression: Maintain normal upstream behavior (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0014

[patch](patches/P-0014-3f688b2f6eb1.patch)
SHA-256: 3f688b2f6eb187afbc60f456886566f8fddf2921303d6616b15647175812ebad

### VP-0014: Targeted regression: Maintain normal upstream behavior

- **requirement**: Maintain normal upstream behavior
- **mutation**: Targeted regression: Maintain normal upstream behavior (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0015

[patch](patches/P-0015-40321a437eee.patch)
SHA-256: 40321a437eeeb26953a5dda6fea75f67fbe95583db50bf5763814342900f99cb

### VP-0015: Targeted regression: Loads the legal target return module for other explicit module instances: the module whose return value, specified by the legal name, is the correct name and status.

- **requirement**: Loads the legal target return module for other explicit module instances: the module whose return value, specified by the legal name, is the correct name and status.
- **mutation**: Targeted regression: Loads the legal target return module for other explicit module instances: the module whose return value, specified by the legal name, is the correct name and status. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0016

[patch](patches/P-0016-4723d6e5f992.patch)
SHA-256: 4723d6e5f99225a467dedff41085ee39083f1191085655c25f4a1c217f2952ed

### VP-0016: Targeted regression: load refuses to load symlink source: OSError

- **requirement**: load rejects symlink source: OSError; linked target not read as session state
- **mutation**: Targeted regression: load refuses to load symlink source: OSError (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0017

[patch](patches/P-0017-485b8d336f5d.patch)
SHA-256: 485b8d336f5d7f29ac2399efac5a2a124b9724282ed80fb9e3d54b45eb1e8165

### VP-0017: Targeted regression: Restoring the source attribute of the object is sys.modules[source].

- **requirement**: Restoring the source attribute of the object is sys.modules[source].
- **mutation**: Targeted regression: Restoring the source attribute of the object is sys.modules[source]. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0018

[patch](patches/P-0018-49c1273c6fbb.patch)
SHA-256: 49c1273c6fbbff0d5fed38b2af5aefcc30f879e1a611a789548e5269b0969845

### VP-0018: Targeted regression: Session state self-reference and function globals semantics maintained: The restored module self-reference points to the restored module.

- **requirement**: Session state self-reference and function globals semantics maintained: The restored module self-reference points to the restored module; session function globals points to a dictionary of restoration targets, with the original value semantics preserved.
- **mutation**: Targeted regression: Session state self-reference and function globals semantics maintained: The restored module self-reference points to the restored module. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0019

[patch](patches/P-0019-51918355a88e.patch)
SHA-256: 51918355a88e5b4d0c840823d39728aef89a4f6f95e9b3bb7c8f5970365672d1

### VP-0019: Targeted regression: load remains active; tell/seek is functional; caller reader opens: none; peek and tell/seek are functional.

- **requirement**: load remains active for the caller of tell/seek. reader is open: none. peek and tell/seek are functional for the caller. The reader remains open after the call.
- **mutation**: Targeted regression: load remains active for the caller of tell/seek. reader is open: none. peek and tell/seek are functional for the caller. The reader remains open after the call. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0020

[patch](patches/P-0020-57a9614dbf61.patch)
SHA-256: 57a9614dbf61d28ad2e7717d4a935b0028ee80763db3607a64f81479fa6d74a6

### VP-0020: Targeted regression: asdict maintains the effects of close failures and module replacement: close errors take precedence over loading errors, and the restoration/removal of original sys.modules items occurs after close.

- **requirement**: asdict maintains the effects of close failures and module replacement: close errors take precedence over loading errors. The restoration/revocation of original sys.modules items after close does not occur.
- **mutation**: Targeted regression: asdict maintains the effects of close failures and module replacement: close errors take precedence over loading errors. The restoration/revocation of original sys.modules items after close does not occur. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0021

[patch](patches/P-0021-58d0ad09fc86.patch)
SHA-256: 58d0ad09fc86e3bef38f12ada779362bf7261b70858a4cb373e68094209ea02d

### VP-0021: Targeted regression: Maintain normal upstream behavior

- **requirement**: Maintain normal upstream behavior
- **mutation**: Targeted regression: Maintain normal upstream behavior (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0022

[patch](patches/P-0022-778e3dbae00d.patch)
SHA-256: 778e3dbae00deef4322092c94a546bb2eb80934a4dea207a6ac97377b5c42fc9

### VP-0022: Targeted regression: asdict returns an independent recovery dictionary: returns a dict and is not the same object as the original module dictionary.

- **requirement**: asdict returns an independent recovery dictionary: returns a dict and is not the same object as the original module dictionary; the runtime archive range is subject to unresolved explanations.
- **mutation**: Targeted regression: asdict returns an independent recovery dictionary: returns a dict and is not the same object as the original module dictionary. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0023

[patch](patches/P-0023-7b69e35388b1.patch)
SHA-256: 7b69e35388b1ded1619dcd12d59769b023d81e6a4096e9d8e5e50257d7d98d89

### VP-0023: Targeted regression: Load maintains the existing lifecycle of other accepted readers: It can buffer and has a peek/position interface that mirrors the underlying closure effect of the baseline.

- **requirement**: Load maintains the existing lifecycle of other accepted readers: It can be buffered, and the underlying closure effect of readers with peek/position interfaces is consistent with the baseline; does not change to never closing.
- **mutation**: Targeted regression: Load maintains the existing lifecycle of other accepted readers: It can buffer and has a peek/position interface that mirrors the underlying closure effect of the baseline. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

### VP-0024: Targeted regression: asdict maintains the existing lifecycle of other accepted readers: It can buffer and has a peek/position interface, and the underlying closure effect of the reader is consistent with the baseline.

- **requirement**: asdict maintains the existing lifecycle of other accepted readers: It can buffer and has a peek/position interface, and the underlying closure effect of the reader is consistent with the baseline.
- **mutation**: Targeted regression: asdict maintains the existing lifecycle of other accepted readers: It can buffer and has a peek/position interface, and the underlying closure effect of the reader is consistent with the baseline. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0024

[patch](patches/P-0024-80ee8a556323.patch)
SHA-256: 80ee8a556323da3a360df3afdce2707638c30d8d6e9e399ce40d1496da05f1f6

### VP-0025: Targeted regression: load rejects non-module supplied values: valid archived and non-module values trigger TypeError

- **requirement**: load rejects non-module supplied values: valid archived and non-module values trigger TypeError
- **mutation**: Targeted regression: load rejects non-module supplied values: valid archived and non-module values trigger TypeError (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0025

[patch](patches/P-0025-8342c24a0dd8.patch)
SHA-256: 8342c24a0dd88978d44266c007e507aa1c2c221f55f3238f7ae69e3d2c2c17e8

### VP-0026: Targeted regression: Supported aliases can restore identity by reference: The alias attribute is the original name attribute of sys.modules[source].

- **requirement**: Supported aliases can restore identity by reference: The alias attribute is the original name attribute of sys.modules[source].
- **mutation**: Targeted regression: Supported aliases can restore identity by reference: The alias attribute is the original name attribute of sys.modules[source]. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0026

[patch](patches/P-0026-8b036a56983b.patch)
SHA-256: 8b036a56983b42c9e3589a49e7dc4c4cfdee2957694f40e3dd9ce8620424c237

### VP-0027: Targeted regression: Maintain normal upstream behavior

- **requirement**: Maintain normal upstream behavior
- **mutation**: Targeted regression: Maintain normal upstream behavior (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0027

[patch](patches/P-0027-9117c963442b.patch)
SHA-256: 9117c963442b119508f00d9930aa68db6a8981de45ea9c10a7e76f440e1ac77c

### VP-0028: Targeted regression: Load updates __main__ or an explicit module instance and returns None: The state of the specified instance is restored and the result is None.

- **requirement**: Load updates __main__ or explicit module instances and returns None: The state of the specified instance is restored and the result is None; the instance identity remains unchanged.
- **mutation**: Targeted regression: Load updates __main__ or an explicit module instance and returns None: The state of the specified instance is restored and the result is None. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0028

[patch](patches/P-0028-985701e54154.patch)
SHA-256: 985701e541541b867c26bd1f7aa68654c1369514ef004161113a7b41d3d77356

### VP-0029: Targeted regression: asdict remains with the caller of tell/seek. The reader is turned on: no peek, and tell/seek works.

- **requirement**: asdict remains open with the caller reader for tell/seek; no peek, and the caller reader remains open after the call.
- **mutation**: Targeted regression: asdict remains open with the caller reader for tell/seek; no peek, and the caller reader remains open after the call. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0029

[patch](patches/P-0029-9a13ff794edf.patch)
SHA-256: 9a13ff794edfea34aed1072a98cc36f5e5ce15e98e1f6526601e04e116b8a7eb

### VP-0030: Targeted regression: asdict records the source: the value returned by __session__ follows the semantics of str(filename).

- **requirement**: asdict records the source: the value returned by __session__ follows the semantics of str(filename).
- **mutation**: Targeted regression: asdict records the source: the value returned by __session__ follows the semantics of str(filename). (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0030

[patch](patches/P-0030-9e35aee67c0a.patch)
SHA-256: 9e35aee67c0a82e9c07ee1fa3b6e75e94c98a5c09be23913e5461f941ab20be0

### VP-0031: Targeted regression: Load keeps close failure and runtime residual exceptions: Close errors take precedence over loading errors. Cleanup and reference restoration after close do not execute. Registered r

- **requirement**: Load failed with close failure and remaining exceptions in runtime: Close errors take precedence over loading errors. Cleanup and reference restoration after close do not execute. Remaining registered runtime items remain.
- **mutation**: Targeted regression: Load failed with close failure and remaining exceptions in runtime: Close errors take precedence over loading errors. Cleanup and reference restoration after close do not execute. Remaining registered runtime items remain. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0031

[patch](patches/P-0031-a17881175ef0.patch)
SHA-256: a17881175ef0f3e18464bc56fe43dae389fd3728b1e5c321424d2e54d33562bd

### VP-0032: Targeted regression: Maintain normal upstream behavior

- **requirement**: Maintain normal upstream behavior
- **mutation**: Targeted regression: Maintain normal upstream behavior (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0032

[patch](patches/P-0032-a4814a2f885f.patch)
SHA-256: a4814a2f885fa4ac55108fe4238b22a2ff3a155dcc5b6f926ad96d7a6cfba9ae

### VP-0033: Targeted regression: Maintain normal upstream behavior

- **requirement**: Maintain normal upstream behavior
- **mutation**: Targeted regression: Maintain normal upstream behavior (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0033

[patch](patches/P-0033-b3100a880efa.patch)
SHA-256: b3100a880efac15266c4c6afa2679b191e5e02182c5371fd716821f9dfffb25c

### VP-0034: Targeted regression: Load updates __main__ or an explicit module instance and returns None: The state of the specified instance is restored and the result is None.

- **requirement**: Load updates __main__ or explicit module instances and returns None: The state of the specified instance is restored and the result is None; the instance identity remains unchanged.
- **mutation**: Targeted regression: Load updates __main__ or an explicit module instance and returns None: The state of the specified instance is restored and the result is None. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0034

[patch](patches/P-0034-bd0842fa6314.patch)
SHA-256: bd0842fa631406a1951f64130fd2da4e75ffadef01eb6d5bdf3b1cdc1791f358

### VP-0035: Targeted regression: asdict Rejects the "module" keyword: Triggers a TypeError before source reading when the "module" keyword is included.

- **requirement**: asdict Rejects the "module" keyword: Triggers a TypeError before source reading when the "module" keyword is included.
- **mutation**: Targeted regression: asdict Rejects the "module" keyword: Triggers a TypeError before source reading when the "module" keyword is included. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0035

[patch](patches/P-0035-c32c58a4dd51.patch)
SHA-256: c32c58a4dd51f25e0606eef05ef44504857386259632a225e5b5f8129eddc502

### VP-0036: Targeted regression: asdict maintains the current module namespace of the caller: the content of the original module dictionary remains the same before and after calling. The registration identity of the original module is restored upon completion.

- **requirement**: asdict maintains the current module namespace of the caller: the content of the original module dictionary remains the same before and after calling. The registration identity of the original module is restored upon completion.
- **mutation**: Targeted regression: asdict maintains the current module namespace of the caller: the content of the original module dictionary remains the same before and after calling. The registration identity of the original module is restored upon completion. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0036

[patch](patches/P-0036-c3d8b9677a12.patch)
SHA-256: c3d8b9677a1251be07928f5766846dc588885a114c296bc0ed4a435b5a82468f

### VP-0037: Targeted regression: load rejected: imported/runtime type mismatch: valid archive and conflicting type module object triggered ValueError

- **requirement**: load rejected: imported/runtime type mismatch: valid archive and conflicting type module object triggered ValueError
- **mutation**: Targeted regression: load rejected: imported/runtime type mismatch: valid archive and conflicting type module object triggered ValueError (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0037

[patch](patches/P-0037-d4ba08370f74.patch)
SHA-256: d4ba08370f7458d804d9c5a8648fc03a55bed5e9fcf28024f947ed6622830885

### VP-0038: Targeted regression: dump rejects symlink target: OSError

- **requirement**: dump rejects symlink target: OSError; the target bytes were not written to or truncated
- **mutation**: Targeted regression: dump rejects symlink target: OSError (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0038

[patch](patches/P-0038-d6e780ecec21.patch)
SHA-256: d6e780ecec21bafe0acb994edca5769712b63b8974482bae94acd47435bfd9db

### VP-0039: Targeted regression: load rejects explicit module name mismatch: valid archives and modules with different names trigger ValueError.

- **requirement**: load rejects explicit module name mismatch: valid archives and modules with different names trigger ValueError.
- **mutation**: Targeted regression: load rejects explicit module name mismatch: valid archives and modules with different names trigger ValueError. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0039

[patch](patches/P-0039-df1ca57e0024.patch)
SHA-256: df1ca57e002498ca047f12fb2d3773502f061ae2e5c35b0d523d50fbacf26156

### VP-0040: Targeted regression: Maintain normal upstream behavior

- **requirement**: Maintain normal upstream behavior
- **mutation**: Targeted regression: Maintain normal upstream behavior (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0040

[patch](patches/P-0040-e435d975f7a3.patch)
SHA-256: e435d975f7a34f30ae99f030253e9b94d9af00aff2955374523457208bc9bb70

### VP-0041: Targeted regression: Path/stream acquisition and resource ownership responsibility actual reorganization: The review of the production source code shows substantial organizational changes in state management, and the ownership rules for the three entrances are coordinated.

- **requirement**: Path/stream acquisition and resource ownership responsibility actual reorganization: The review of the production source code shows substantial organizational changes in state management, and the ownership rules for the three entrances are coordinated; no acceptance is made based on the name or quantity of helpers.
- **mutation**: Targeted regression: Path/stream acquisition and resource ownership responsibility actual reorganization: The review of the production source code shows substantial organizational changes in state management, and the ownership rules for the three entrances are coordinated. (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

### VP-0042: Targeted regression: The generation and interpretation of the runtime module identity are consistent: the runtime name in the archive, loading and parsing, and the recovery of __name__ correspond to the compatibility rules.

- **requirement**: The generation and interpretation of the runtime module identity are consistent: the names in the archive for runtime, loading, parsing, and restoring __name__ correspond to compatible rules; the production and consumption responsibilities in the source code are coordinated, with no independent drift in interpretation.
- **mutation**: Targeted regression: The generation and interpretation of the runtime module identity are consistent: the runtime name in the archive, loading and parsing, and the recovery of __name__ correspond to the compatibility rules. (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

### VP-0043: Targeted regression: Imported reference capture and recovery state responsibility actual reorganization: Producing code with coordinated capture/recovery data flow and substantial responsibility reorganization, not just changing format or adding unused code

- **requirement**: Imported reference capture and recovery state responsibility actual reorganization: Producing code with coordinated capture/recovery data flow and substantial responsibility reorganization, not just changing format or adding unused code
- **mutation**: Targeted regression: Imported reference capture and recovery state responsibility actual reorganization: Producing code with coordinated capture/recovery data flow and substantial responsibility reorganization, not just changing format or adding unused code (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0041

[patch](patches/P-0041-e57f5a66c16e.patch)
SHA-256: e57f5a66c16e4e69388d799be3b88b2d4977f902a0d1777eff16a87d18390ce7

### VP-0044: Targeted regression: After successful runtime loading, temporary registration is revoked: When returning normally, __runtime__.<name> does not exist in the temporary sys.modules items.

- **requirement**: After successful runtime loading, temporary registration is revoked: When returning normally, __runtime__.<name> does not exist in the temporary sys.modules items.
- **mutation**: Targeted regression: After successful runtime loading, temporary registration is revoked: When returning normally, __runtime__.<name> does not exist in the temporary sys.modules items. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0042

[patch](patches/P-0042-e68b66af0e23.patch)
SHA-256: e68b66af0e23a93b3b44236e97e75ec7445223b71aa2a67922b903e7432cbc82

### VP-0045: Targeted regression: Restoring module attribute is sys.modules in the corresponding module.

- **requirement**: Restoring module attribute is sys.modules in the corresponding module.
- **mutation**: Targeted regression: Restoring module attribute is sys.modules in the corresponding module. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0043

[patch](patches/P-0043-f51c0c38ae00.patch)
SHA-256: f51c0c38ae000eea56ba38e6dfb3861ed7d218cdc1ed32ae35eeb495cad15327

### VP-0046: Targeted regression: asdict(update=False) does not incorporate the current additional state: Newly added entries that have not been saved are not included in the restored dictionary, allowing the saved state to be recovered.

- **requirement**: asdict(update=False) does not incorporate the current additional state: Newly added entries that have not been saved are not included in the restored dictionary, allowing the saved state to be recovered.
- **mutation**: Targeted regression: asdict(update=False) does not incorporate the current additional state: Newly added entries that have not been saved are not included in the restored dictionary, allowing the saved state to be recovered. (changed files: dill/session.py, dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not reclassify this outcome as a blocked experiment
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

## P-0044

[patch](patches/P-0044-51699acc672f.patch)
SHA-256: 51699acc672fbd5c70bef75bfa9b89bf279fda884de92febc344da3d16afecc4

### VP-0047: runtime update=True: Error in creating an empty module when it already exists during registration.

- **requirement**: update=True is missing to throw a KeyError with the saved key when saving the runtime registration.
- **mutation**: Change the query from missing registration to creating a new module, allowing errors to be recovered; restore the identity of references that were not triggered for the old candidates.
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The original test must effectively fail: A KeyError was thrown when the runtime registration was missing, which is not allowed according to the contract.
- **prerequisites**: None (clean baseline)
- **version_note**: The original audit retired this verification point. It is retained for historical reference.
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application failed; The original target field is missing

