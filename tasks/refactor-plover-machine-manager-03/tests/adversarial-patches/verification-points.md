# Adversarial patches and verification points

Task: refactor-plover-machine-manager-03
Base commit: e87c4ef2982fcdeea587d2e612dff829fd331386

This package contains 34 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-13f29811bfbf.patch)
SHA-256: 13f29811bfbf3a48e848f8285cec3f7cc6430496167e096a1c9b61bf8b39299b

### VP-0001: Shutdown only stops non-thread plugins, while the actual ThreadedStenotypeBase continues to capture events.

- **requirement**: Shutdown only stops non-thread plugins, while the real ThreadedStenotypeBase continues to capture; real input is fixed.
- **mutation**: Shutdown only stops non-thread plugins, while the real ThreadedStenotypeBase continues to capture; real input is fixed. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0002

[patch](patches/P-0002-1b05e6c917e7.patch)
SHA-256: 1b05e6c917e7fceb9214521170936457d0b3ca5ef972fa55918231af499c787a

### VP-0002: The actual state is stored and migrated back to the engine. The public report remains unchanged.

- **requirement**: The actual state is stored and migrated back to the engine. The public report remains unchanged.
- **mutation**: The actual state is stored and migrated back to the engine. The public report remains unchanged. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0003

[patch](patches/P-0003-1ea8bd2e0fa6.patch)
SHA-256: 1ea8bd2e0fa6c35245539f240e10630649fe574e6b92d53a692f4d117e710c2d

### VP-0003: shutdown stops but does not release the instance

- **requirement**: shutdown stops but does not release the instance
- **mutation**: shutdown stops but does not release the instance (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0004

[patch](patches/P-0004-30e300ed415f.patch)
SHA-256: 30e300ed415f8282fd6fad8cc2a015979986d3ea5483b6c4450078761838de2b

### VP-0004: Construct Lost Exclusive Options

- **requirement**: Construct Lost Exclusive Options
- **mutation**: Construct Lost Exclusive Options (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0005

[patch](patches/P-0005-35eb2b1533a4.patch)
SHA-256: 35eb2b1533a484643525401c83fa3de171c8031943cfc8078f27b19edbf311f5

### VP-0005: Reuse the path and pass None to the plugin.

- **requirement**: Reuse the path and pass None to the plugin; fix the actual input.
- **mutation**: Reuse the path and pass None to the plugin; fix the actual input. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0006

[patch](patches/P-0006-3f94718b9a6c.patch)
SHA-256: 3f94718b9a6ca711632399b63c093902f78aeec3eb55b03a91a5b576e97a4beb

### VP-0006: State bypassing the engine thread

- **requirement**: State bypassing the engine thread
- **mutation**: State bypassing the engine thread (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0007

[patch](patches/P-0007-4a4d0ce2360a.patch)
SHA-256: 4a4d0ce2360af05d6a1ab59bc7b55441ad14d8dee038e0610c2443d9693bc142

### VP-0007: reset Skip Dictionary Reloading

- **requirement**: reset Skip Dictionary Reloading
- **mutation**: reset Skip Dictionary Reloading (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0008

[patch](patches/P-0008-4a7963a4b0db.patch)
SHA-256: 4a7963a4b0dbaadf001cb00913a71362b46cdc07d25ad5cca6a1aa114a70f4e6

### VP-0008: Independent reload does not load the disk

- **requirement**: Independent reload does not load the disk
- **mutation**: Independent reload does not load the disk (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0009

[patch](patches/P-0009-4c5c43792b71.patch)
SHA-256: 4c5c43792b7184e1ae41d01a5937f1e9ca4f1b1819e596096c444cea0c91c3fe

### VP-0009: The non-none keymap is applied only once but later than capture.

- **requirement**: The non-none keymap is applied only once but later than capture; real input is fixed.
- **mutation**: The non-none keymap is applied only once but later than capture; real input is fixed. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0010

[patch](patches/P-0010-4dd18677477c.patch)
SHA-256: 4dd18677477c3180d4139e2a229c8dbf02c842ca77a88c79ebb3da04bbd277a4

### VP-0010: Configuration events have lost their actual application differences.

- **requirement**: Configuration events have lost their actual application differences.
- **mutation**: Configuration events have lost their actual application differences. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0011

[patch](patches/P-0011-5c19328314d4.patch)
SHA-256: 5c19328314d4c366c3e0789f978da082dec9ad6bb416e1cb869a4c16393493ee

### VP-0011: The output property repeats an additional event. Normal state/suppression is maintained.

- **requirement**: The output property repeats an event additionally. The normal state/suppression remains; the real input is fixed.
- **mutation**: The output property repeats an event additionally. The normal state/suppression remains; the real input is fixed. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0012

[patch](patches/P-0012-5d184d121990.patch)
SHA-256: 5d184d1219908dbf3a36c64e4af68bb4139ea123e6a1ec14a6b4e9f449f41985

### VP-0012: A redundant request emits a duplicate output event.

- **requirement**: A redundant request emits a duplicate output event.
- **mutation**: A redundant request emits a duplicate output event. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0013

[patch](patches/P-0013-5f8fa313294f.patch)
SHA-256: 5f8fa313294fa97b10e470df8e2eea0f1d68510ccbb9fa104a0af26eb40d4d2e

### VP-0013: The non-none keymap is applied only once but later than capture.

- **requirement**: The non-none keymap is applied only once but later than capture; real input is fixed.
- **mutation**: The non-none keymap is applied only once but later than capture; real input is fixed. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0014

[patch](patches/P-0014-63d962dae0c5.patch)
SHA-256: 63d962dae0c5ae0d328f52af06f276f89940cccfd8ba00d3cdda1126ce30574d

### VP-0014: Shutdown only stops non-thread plugins, while the actual ThreadedStenotypeBase continues to capture events.

- **requirement**: Shutdown only stops non-thread plugins, while the real ThreadedStenotypeBase continues to capture; real input is fixed.
- **mutation**: Shutdown only stops non-thread plugins, while the real ThreadedStenotypeBase continues to capture; real input is fixed. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0015

[patch](patches/P-0015-65d462e98847.patch)
SHA-256: 65d462e98847ab8aaf491ac65aa4a4a7b7c9058874eb5f3224260c6a69338e8f

### VP-0015: The stroke callback is moved after capture, and still registered once.

- **requirement**: Move the stroke callback after capture, still register once; fix the real input issue
- **mutation**: Move the stroke callback after capture, still register once; fix the real input issue (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0016

[patch](patches/P-0016-6682214fe4df.patch)
SHA-256: 6682214fe4dfc441d8ddc713e5d4c0c654abd665484ff5e2b84a4350cda05344

### VP-0016: The disabled output is still suppressed.

- **requirement**: The disabled output is still suppressed.
- **mutation**: The disabled output is still suppressed. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0017

[patch](patches/P-0017-76bb18eea699.patch)
SHA-256: 76bb18eea699db19ba6ec1d0ff695f1dc9f93f81f8b5d008ff0012d7b2e6c1e0

### VP-0017: Changes in options do not result in reconstruction.

- **requirement**: Changes in options do not result in reconstruction.
- **mutation**: Changes in options do not result in reconstruction. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0018

[patch](patches/P-0018-780514ebc738.patch)
SHA-256: 780514ebc7388370cb9d4301070c7ddb7f823e0a9b36be1e6b6a98b3762e8367

### VP-0018: keymap-only forced reconstruction

- **requirement**: keymap-only forced reconstruction
- **mutation**: keymap-only forced reconstruction (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0019

[patch](patches/P-0019-7f2504009c0b.patch)
SHA-256: 7f2504009c0b7e0e0bb6a77074d96d173f42379a3f4196160f02cec35a9cdbf1

### VP-0019: reset increases disk loading

- **requirement**: reset increases disk loading; real input repair
- **mutation**: reset increases disk loading; real input repair (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0020

[patch](patches/P-0020-92de987a446f.patch)
SHA-256: 92de987a446fe161a33deef1b3c91ddd639b72007820c768f91fd0d7952a3e7f

### VP-0020: The reuse path skips a non-None keymap.

- **requirement**: The reuse path skips a non-None keymap.
- **mutation**: The reuse path skips a non-None keymap. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0021

[patch](patches/P-0021-9543c55d2e08.patch)
SHA-256: 9543c55d2e08f9ada6c9f8d7fcbf4ea481854d684a5ad51fa4a7dc2a89c1cc3c

### VP-0021: Restoration Command Stroke Omission Post-event Suppression

- **requirement**: Restoration Command Stroke Omission Post-event Suppression
- **mutation**: Restoration Command Stroke Omission Post-event Suppression (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0022

[patch](patches/P-0022-95979cb9f0f3.patch)
SHA-256: 95979cb9f0f381122127eb09137ede2a7610d324294afce300cec724b32c70ae

### VP-0022: The engine directly holds live instances, with specialized ownership being broken

- **requirement**: The engine directly holds live instances, with specialized ownership being broken
- **mutation**: The engine directly holds live instances, with specialized ownership being broken (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0023

[patch](patches/P-0023-a5d975aa74a7.patch)
SHA-256: a5d975aa74a7d52567e0a3fc1ab4e95e0b5336d33a8348c086af332236c11726

### VP-0023: Synthesis successful before asynchronous ready

- **requirement**: Synthesis successful before asynchronous ready
- **mutation**: Synthesis successful before asynchronous ready (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0024

[patch](patches/P-0024-d906fb7c47ad.patch)
SHA-256: d906fb7c47ad3472f63fa995d5f2258576f4601d2d8ae1ac8211ba2f5cacef13

### VP-0024: First machine report incorrectly reported a stopped status

- **requirement**: First machine report incorrectly reported a stopped status
- **mutation**: First machine report incorrectly reported a stopped status
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry should generate a complete and valid rejection score; failure in execution, compilation, or collection does not count as success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0025

[patch](patches/P-0025-b82b1b63b170.patch)
SHA-256: b82b1b63b1703a36876961edadbc2de8247b5a4179e72a1e3d0f942596868894

### VP-0025: Start reconstruction, pass None to the plugin.

- **requirement**: Start reconstruction, pass None to the plugin.
- **mutation**: Start reconstruction, pass None to the plugin. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0026

[patch](patches/P-0026-c49d57dbb579.patch)
SHA-256: c49d57dbb57997a1ed637d1ace1aa8b788fb48ffa626d4dd237337247c4f436b

### VP-0026: The output property repeats an additional event. Normal state/suppression is maintained.

- **requirement**: The output property repeats an event additionally. The normal state/suppression remains; the real input is fixed.
- **mutation**: The output property repeats an event additionally. The normal state/suppression remains; the real input is fixed. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0027

[patch](patches/P-0027-c7969bfc3e6c.patch)
SHA-256: c7969bfc3e6c9dec6a65c48ca2e9a2d992f7a2f49678dffe722b76c5946439db

### VP-0027: Replace the error report with connected.

- **requirement**: Replace the error report with connected.
- **mutation**: Replace the error report with connected. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0028

[patch](patches/P-0028-d0f9b08f51b4.patch)
SHA-256: d0f9b08f51b4dfa28d3f65c4416f8489e9c4eff42e984f437d33be40fc0274d1

### VP-0028: Status cache error ignored, disconnected

- **requirement**: Status cache error ignored, disconnected
- **mutation**: Status cache error ignored, disconnected (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0029

[patch](patches/P-0029-d605589e6d00.patch)
SHA-256: d605589e6d00fff96b3a12b568a5541f9db23ad827df3010138d5f2db13cac9a

### VP-0029: toggle does not flip.

- **requirement**: toggle does not flip.
- **mutation**: toggle does not flip. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0030

[patch](patches/P-0030-e4e2ec0b3717.patch)
SHA-256: e4e2ec0b37178224f021e4e6d04c8accfe583e111d1b88663925d1832a1f60ef

### VP-0030: Move keymap actual call back to engine

- **requirement**: Move keymap actual call back to engine
- **mutation**: Move keymap actual call back to engine (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0031

[patch](patches/P-0031-e9955750ee21.patch)
SHA-256: e9955750ee2136830ec748a8dc7dddbd5cc4b16ff362b299edfc4d7791f66863

### VP-0031: The stroke callback is moved after capture, and still registered once.

- **requirement**: Move the stroke callback after capture, still register once; fix the real input issue
- **mutation**: Move the stroke callback after capture, still register once; fix the real input issue (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0032

[patch](patches/P-0032-f09cf3668a33.patch)
SHA-256: f09cf3668a33a9b58f03e64deaf787dcf2851ac180ea339b545869ee0d2a8516

### VP-0032: Reverse the order of stroke logging and translation.

- **requirement**: Reverse the order of stroke logging and translation.
- **mutation**: Reverse the order of stroke logging and translation. (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0033

[patch](patches/P-0033-f11367346c3e.patch)
SHA-256: f11367346c3ee8d4ca442116610c2a85cf8a537f9cbc40b356b31f221d93d945

### VP-0033: set_output reverse setting

- **requirement**: set_output reverse setting
- **mutation**: set_output reverse setting (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

## P-0034

[patch](patches/P-0034-fe0695c558b5.patch)
SHA-256: fe0695c558b57d610eff7e1299b9297153e04649a5b1d0fdfefe5e0e54e8457e

### VP-0034: Cancel forced reconnection with the same configuration

- **requirement**: Cancel forced reconnection with the same configuration
- **mutation**: Cancel forced reconnection with the same configuration (changed files: plover/engine.py, plover/machine/manager.py, test/test_engine.py)
- **setup**: Apply this patch to the clean baseline at e87c4ef2982f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application fails

