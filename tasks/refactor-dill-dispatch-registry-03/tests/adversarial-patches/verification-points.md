# Adversarial patches and verification points

Task: refactor-dill-dispatch-registry-03
Base commit: 50d93fe52c84cdbfd81c39f5adba68f627fd330b

This package contains 13 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-06060ad9fe60.patch)
SHA-256: 06060ad9fe60e888759f4194752df2517acb6bf2636ea29186504e1d40d5927a

### VP-0001: Cancel the additional overall coverage of the old standard snapshot, disrupt external replacement

- **requirement**: Undo must preserve external handlers assigned directly in the standard table, particularly replacements for the original standard types.
- **mutation**: Cancel the additional overall coverage of the old standard snapshot, disrupt external replacement (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0002

[patch](patches/P-0002-08402f803a0e.patch)
SHA-256: 08402f803a0ef4052c10ac657d823a4c473eb1b1e9fa28c27d734b4c0ae8e18d

### VP-0002: Public key iteration is empty

- **requirement**: It is still possible to iterate the currently registered dispatch when it is made public.
- **mutation**: Public key iteration is empty; actual items and storage are retained. (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0005

[patch](patches/P-0005-355318f5e69f.patch)
SHA-256: 355318f5e69f69dbe2de9ceb98b4bbfa035d2dc1ecd45c7eb03dc1d739eed1b2

### VP-0005: Pickle is completed with registration, but an error is returned, resulting in True.

- **requirement**: If the pickle registration is successful, return None.
- **mutation**: Pickle is completed with registration, but an error is returned, resulting in True. (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0006

[patch](patches/P-0006-37cea0641c3b.patch)
SHA-256: 37cea0641c3bacc00cebc676fbb42bb3f4f104f810b4742e15d9e2e7d7cc61b8

### VP-0006: Return to the independent module snapshot and perform module-level writes.

- **requirement**: The same registry has the status of registered and standard integration/restoration, exposes path delegation, and has no independent extension status owner.
- **mutation**: Restore path to independent module snapshot and module-level write; other registry paths remain unchanged (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0008

[patch](patches/P-0008-3a75c9afd014.patch)
SHA-256: 3a75c9afd014303fd0ac61201d256cf9dcca1cb388757fab98b94ac6c884fd3b

### VP-0008: Cancel the deletion of the original standard type without restoring the original function.

- **requirement**: Restore the original standard type that was not overwritten by the dill own handler to its pre-expansion state.
- **mutation**: Cancel the deletion of the original standard type without restoring the original function. (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0009

[patch](patches/P-0009-449e5815f658.patch)
SHA-256: 449e5815f658967ef6e7bb27d70708b98b9b73cd3aa06dcd419cf719b6dd73b3

### VP-0009: dumps returns a new format prefix, breaking the standard data format

- **requirement**: The serialization data results and format of the existing serializer remain compatible.
- **mutation**: dumps returns a new format prefix, breaking the standard data format (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0011

[patch](patches/P-0011-6ff43c578167.patch)
SHA-256: 6ff43c578167f80b5f554206a6628c3242c89a64881502c8da6e24e752b5726b

### VP-0011: Error swallowed by serializer ValueError

- **requirement**: If the serializer has any exceptions that do not support object behavior, they should be left unchanged.
- **mutation**: Error swallowed by serializer ValueError (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0012

[patch](patches/P-0012-79481dca6080.patch)
SHA-256: 79481dca60809720c0b2b35d2253f3a98b6d5a805209fd828e1e4024ea9ce2fc

### VP-0012: extend returns True for both error conditions

- **requirement**: extend returns None in both directions
- **mutation**: extend returns True for both error conditions (changed files: dill/_dill.py, dill/__init__.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0013

[patch](patches/P-0013-83f27d7a703e.patch)
SHA-256: 83f27d7a703ec329c6628360e8a1d8ffc4a821deae2967ffef978e3845da56dd

### VP-0013: The meta-class fallback returns an error for the existing handler, maintaining a successful lookup.

- **requirement**: Public dispatch retains compatibility with type lookup
- **mutation**: The meta-class fallback returns an error for the existing handler, maintaining a successful lookup. (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0014

[patch](patches/P-0014-87ef8519e3a1.patch)
SHA-256: 87ef8519e3a18932553ae6b27367d8e509dcf5a610a511050b224b091ef5b198

### VP-0014: Cancel only processes the original standard types, leaving the newly added dill own handler behind.

- **requirement**: Remove the dill own handler that does not exist in the original standard table.
- **mutation**: Cancel only processes the original standard types, leaving the newly added dill own handler behind. (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0016

[patch](patches/P-0016-9e890743b261.patch)
SHA-256: 9e890743b2612a876d1f24967f55f36d54900b676ba5064cb4c3ff0530702c32

### VP-0016: External decorator returns None but is correctly registered

- **requirement**: The decorator returned by register is the original serializer passed in.
- **mutation**: External decorator returns None but is correctly registered (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0017

[patch](patches/P-0017-a07fecd456e5.patch)
SHA-256: a07fecd456e518b6cdb43e4b8913f6b2aa7e4363fa578d85c525f0de9822f100

### VP-0017: Integrated additional replacement standard C Pickler entry

- **requirement**: The integrated write dispatch target is defined as a standard pure Python pickler mapping.
- **mutation**: Integrated additional replacement standard C Pickler entry (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0022

[patch](patches/P-0022-fe45b1826613.patch)
SHA-256: fe45b1826613baf4258e33a7b2560f10c5d6656285be1ad837991220768ef4fa

### VP-0022: First normal recovery, subsequent recoveries were mistakenly skipped

- **requirement**: Re-enabling undo recovery and external protection rules does not drift.
- **mutation**: First normal recovery, subsequent recoveries were mistakenly skipped (changed files: dill/_dill.py)
- **setup**: Apply this patch to the clean baseline at 50d93fe52c84, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

