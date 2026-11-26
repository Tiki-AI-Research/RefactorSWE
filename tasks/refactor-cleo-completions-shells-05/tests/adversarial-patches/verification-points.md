# Adversarial test patches and verification points

Task: refactor-cleo-completions-shells-05

Base commit: 8c3f1bbf82d918fc137ad40db65c446e14564aac

Scope: partial export. Some items remain unresolved.
This package contains 39 distinct patches and 40 verification points.
The export omits 0 records without a primary patch, including controls and historical revisions. It excludes 1 control or auxiliary items and leaves 3 items unresolved.
The stated expectations describe the intended checks. Actual results require a replay with the matching task baseline, tests, and environment.

To run all patches:

    bash ./run.sh /path/to/submitted-task

To reuse an existing task image:

    bash ./run.sh /path/to/submitted-task --image your-task-verifier-image

Requires Python 3.9+ and Docker. Without an explicit image, the runner builds or reuses an image based on the supplied task’s tests/Dockerfile.
Each patch runs in a separate clean container with read-only task materials. By default, results go to a new directory beside the package.
The runner replays the official task grader without a separate judge. Acceptance or rejection alone does not establish that the intended assertion ran.
Exit codes: 0 = expectations matched, 1 = expectation mismatch, 2 = incomplete run or evidence, 130 = interrupted.
Use --check-only to verify materials without running tests, or --patch P-0001 to select one patch.

| Patch | Verification points | Subject |
| --- | --- | --- |
| [P-0001](patches/P-0001-069fee35f456.patch) | VP-0001 | Fish format responsibility shifted to command internal helper |
| [P-0002](patches/P-0002-0ece136ed362.patch) | VP-0002 | The disabled command has been incorporated. |
| [P-0003](patches/P-0003-10b38e1c8aae.patch) | VP-0003 | Alias is no longer unique |
| [P-0004](patches/P-0004-2d5850ddc19b.patch) | VP-0004 | The required parameter metadata is incorrect. |
| [P-0005](patches/P-0005-3092697320d2.patch) | VP-0005 | Targeted regression: Three shells use the same parsing responsibility, without duplicating the path and name calculations three times. |
| [P-0006](patches/P-0006-3914ba5c30cd.patch) | VP-0006 | Creation of files |
| [P-0007](patches/P-0007-46b67daf87b2.patch) | VP-0007 | Fish single quotes do not escape |
| [P-0008](patches/P-0008-4f30f3d5cc0b.patch) | VP-0008 | Targeted regression: Ordered aliases are prepared for sharing. The differences in effects between Bash/Zsh/Fish do not lead to the replication of common preparations. |
| [P-0009](patches/P-0009-590635fb75da.patch) | VP-0009 | The unnamed command was included, but it has been given a safe display name to avoid a cascading TypeError. |
| [P-0010](patches/P-0010-5b954877f74c.patch) | VP-0010 | bash format responsibility moved back to command internal helper |
| [P-0011](patches/P-0011-62670d018788.patch) | VP-0011 | Reverse two-level option sorting |
| [P-0012](patches/P-0012-62b6f287e099.patch) | VP-0012 | Change the command name but retain its lookup alias so the initial lookup succeeds. |
| [P-0013](patches/P-0013-656ef7e581a1.patch) | VP-0013 | Change the text in the fish template blanks. |
| [P-0014](patches/P-0014-69099282ef01.patch) | VP-0014 | Reverse Command Order |
| [P-0015](patches/P-0015-6c76d3cde939.patch) | VP-0015 | Emit an additional explanation on success. |
| [P-0016](patches/P-0016-6cc110c72d73.patch) | VP-0016 | Before the error: |
| [P-0017](patches/P-0017-75a2cf0196be.patch) | VP-0017 | Change the blank text in the bash template |
| [P-0018](patches/P-0018-77d8a11a506e.patch) | VP-0018 | Zsh colon not escaping |
| [P-0019](patches/P-0019-78a987983d55.patch) | VP-0019 | Omit support for shell messages |
| [P-0020](patches/P-0020-7951928c7a07.patch) | VP-0020 | Remove duplicate aliases |
| [P-0021](patches/P-0021-7a569f79eadc.patch) | VP-0021 | Bash colon options do not need to be escaped |
| [P-0022](patches/P-0022-7fdc792132e3.patch) | VP-0022 | Remove space-based command references in Bash/Zsh |
| [P-0023](patches/P-0023-84a37aced3a8.patch) | VP-0023 | Bypass realpath |
| [P-0025](patches/P-0025-a9c9895f6246.patch) | VP-0025 | Introducing additional application name state modifications |
| [P-0026](patches/P-0026-ade91a644daa.patch) | VP-0026, VP-0027 | Bypass Traversal Initialization; Bypass lazy materialization |
| [P-0027](patches/P-0027-b232f8c1c286.patch) | VP-0028 | command helper handles generating data traversal |
| [P-0028](patches/P-0028-bad929a18fb7.patch) | VP-0029 | Fish namespace changed to Ye name space |
| [P-0029](patches/P-0029-bd9e715283fa.patch) | VP-0030 | Ignore the end part of the environment path and use bash by default |
| [P-0030](patches/P-0030-c363ba9861f1.patch) | VP-0031 | Environment Coverage Explicit Shell |
| [P-0031](patches/P-0031-c4f018bec0f9.patch) | VP-0032 | Targeted regression: The success command returned 0, indicating that the application exited with a successful status. |
| [P-0032](patches/P-0032-ccb9a9e5cdbb.patch) | VP-0033 | Targeted regression: The responsibility for filling in the common template is replaced by three substitutions, without specifying the template position or private method names. |
| [P-0033](patches/P-0033-d180f88d69ed.patch) | VP-0034 | Hidden commands have been incorporated |
| [P-0034](patches/P-0034-d8ddf84db7a9.patch) | VP-0035 | Default Bash Realpath Registration Vulnerability |
| [P-0035](patches/P-0035-dc2bf0b1112e.patch) | VP-0036 | Targeted regression: Define the naming rules in one place and have the shell generators consume the result. |
| [P-0036](patches/P-0036-de69a725be98.patch) | VP-0037 | zsh format: Responsibility shifted back to the command internal helper |
| [P-0037](patches/P-0037-e8bc3996999e.patch) | VP-0038 | Targeted regression: RuntimeError |
| [P-0038](patches/P-0038-e932b5fb3069.patch) | VP-0039 | Function hash truncation length error |
| [P-0039](patches/P-0039-f51b06035834.patch) | VP-0040 | Targeted regression: The sorting and filtering operations are defined by the same responsibility, and the shell processes them in its own format. |
| [P-0040](patches/P-0040-f84b745526b6.patch) | VP-0041 | Change the whitespace in the zsh template text |

## P-0001

[Download patch](patches/P-0001-069fee35f456.patch)

SHA-256: 069fee35f4564c8a6e2afa4fab5c65445f727c4c76282242fe00369aadd0cc90

### VP-0001: Fish format responsibility shifted to command internal helper

**Requirement**: Fish format generation is carried out by external commands; replacing this responsibility does not require changes to Bash/Zsh or orchestration.

**Targeted change**: Fish format responsibility shifted to command internal helper (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0002

[Download patch](patches/P-0002-0ece136ed362.patch)

SHA-256: 0ece136ed362477885b00db71e3641d57169935d534eaba6d92079e4c3c3e93c

### VP-0002: The disabled command has been incorporated.

**Requirement**: Corresponding commands and their options - Normal generation entries - Absent

**Targeted change**: The disabled command has been incorporated. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0003

[Download patch](patches/P-0003-10b38e1c8aae.patch)

SHA-256: 10b38e1c8aae99070f2d210e7a9b32bebd1189dbb06bc5dbb6328b4b48d2a383

### VP-0003: Alias is no longer unique

**Requirement**: After parsing, the alias is converted into an ordered value list; an empty list is returned when there are no options.

**Targeted change**: Alias is no longer repeatable; leave it empty by default to keep it executable. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0004

[Download patch](patches/P-0004-2d5850ddc19b.patch)

SHA-256: 2d5850ddc19b0f3e94a9ab4d2d1a2b4c13ef3f0dcef7f544cf22c731a8ec8496

### VP-0004: The required parameter metadata is incorrect.

**Requirement**: Define the parameter as optional. Both omission and an explicit value must bind as they did at the original entry point.

**Targeted change**: The required parameter metadata is incorrect; the initialize method maintains an omitted environment behavior to avoid cascading issues. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0005

[Download patch](patches/P-0005-3092697320d2.patch)

SHA-256: 3092697320d21e65d2701f1bb8c8b93e8dfb7d4d8ee1d0fcb82b2871529c3be2

### VP-0005: Targeted regression: Three shells use the same parsing responsibility, without duplicating the path and name calculations three times.

**Requirement**: Three shells use the same parsing responsibility, without duplicating the path and name calculations three times.

**Targeted change**: Targeted regression: Three shells use the same parsing responsibility, without duplicating the path and name calculations three times. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0006

[Download patch](patches/P-0006-3914ba5c30cd.patch)

SHA-256: 3914ba5c30cda3503f3f7626852e0563d4c0e0447a52886b92ab6288c5d01a5f

### VP-0006: Creation of files

**Requirement**: Generation must not create, delete, or change files.

**Targeted change**: Creation of files (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0007

[Download patch](patches/P-0007-46b67daf87b2.patch)

SHA-256: 46b67daf87b21dc43bbc06a6364a74a7fcc69fa4bf6e5de53af563b675a3b483

### VP-0007: Fish single quotes do not escape

**Requirement**: Clean up the description of the complete line and consistent with the baseline for single quote escaping.

**Targeted change**: Fish single quotes do not escape (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0008

[Download patch](patches/P-0008-4f30f3d5cc0b.patch)

SHA-256: 4f30f3d5cc0b4830b4f6dd9151756d2f32b9fb0025d24814042fcd25e4fdaf74

### VP-0008: Targeted regression: Ordered aliases are prepared for sharing. The differences in effects between Bash/Zsh/Fish do not lead to the replication of common preparations.

**Requirement**: Ordered aliases are prepared for sharing. The differences in effects between Bash/Zsh/Fish do not lead to the replication of common preparations.

**Targeted change**: Targeted regression: Ordered aliases are prepared for sharing. The differences in effects between Bash/Zsh/Fish do not lead to the replication of common preparations. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0009

[Download patch](patches/P-0009-590635fb75da.patch)

SHA-256: 590635fb75dafd59b9ab7dc7e48f8421c6046b9bfb639613170988f7577cd6a9

### VP-0009: The unnamed command was included, but it has been given a safe display name to avoid a cascading TypeError.

**Requirement**: Unnamed entries are absent, and the reordering/splitting of names does not introduce any anomalies.

**Targeted change**: The unnamed command was included, but it has been given a safe display name to avoid a cascading TypeError. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0010

[Download patch](patches/P-0010-5b954877f74c.patch)

SHA-256: 5b954877f74c7f91def1e079059192f6d1ed56efb26c0a26e2a7d06982e84819

### VP-0010: bash format responsibility moved back to command internal helper

**Requirement**: Bash format generation is handled by external commands; this responsibility does not need to be changed in Zsh/Fish or the workflow.

**Targeted change**: bash format responsibility moved back to command internal helper (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0011

[Download patch](patches/P-0011-62670d018788.patch)

SHA-256: 62670d018788e83d67bb88d9f57bed76349e135f1048af819218edb50da876e2

### VP-0011: Reverse two-level option sorting

**Requirement**: Both two-level options are sorted by name, in the same order as the baseline.

**Targeted change**: Reverse two-level option sorting (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0012

[Download patch](patches/P-0012-62b6f287e099.patch)

SHA-256: 62b6f287e09974690e691bb5ed8bc6f09bf42b58971c043507886ac262d4ae47

### VP-0012: Change the command name but retain its lookup alias so the initial lookup succeeds.

**Requirement**: Found the command named completions

**Targeted change**: Change the command name but retain its lookup alias so the initial lookup succeeds. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0013

[Download patch](patches/P-0013-656ef7e581a1.patch)

SHA-256: 656ef7e581a19bf4abec3a62472cba255c2aae51a12d3a4586aac3616ec639a8

### VP-0013: Change the text in the fish template blanks.

**Requirement**: The entire Fish script matches character by character with the publicly available baseline input, including template replacements and the last line of the input.

**Targeted change**: Change the text in the fish template blanks. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0014

[Download patch](patches/P-0014-69099282ef01.patch)

SHA-256: 69099282ef012b73fafe45ff9fd5efe77627bba8902b6618558b95e4de8234c9

### VP-0014: Reverse Command Order

**Requirement**: Sort entries by their existing names, without switching to registration order or adding deduplication.

**Targeted change**: Reverse Command Order (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0015

[Download patch](patches/P-0015-6c76d3cde939.patch)

SHA-256: 6c76d3cde93913b8c42654a42323133c0d6faca6b61ccc5383e0e44ee67b6df1

### VP-0015: Emit an additional explanation on success.

**Requirement**: Normal output is script text with existing line breaks. Error stream is empty, with no additional explanations.

**Targeted change**: Emit an additional explanation on success. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0016

[Download patch](patches/P-0016-6cc110c72d73.patch)

SHA-256: 6cc110c72d731dbb946b9020bcded732ec5a7bb8db34b9e4f7a82cfaa0e58f7f

### VP-0016: Before the error:

**Requirement**: Standard output is empty. No partial output is emitted before the error.

**Targeted change**: Before the error: (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0017

[Download patch](patches/P-0017-75a2cf0196be.patch)

SHA-256: 75a2cf0196bebac340efadbac6770b4479cc10b912cb77bdbca5e3d70e24582b

### VP-0017: Change the blank text in the bash template

**Requirement**: The complete Bash script checks character by character against the input public baseline, including template replacements and a final line break.

**Targeted change**: Change the blank text in the bash template (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0018

[Download patch](patches/P-0018-77d8a11a506e.patch)

SHA-256: 77d8a11a506e5125e66af469a89e2c9417edf2a670872a19803c56da41c827f5

### VP-0018: Zsh colon not escaping

**Requirement**: The describe text, colon handling, and unformatted output match the baseline.

**Targeted change**: Zsh colon not escaping (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0019

[Download patch](patches/P-0019-78a987983d55.patch)

SHA-256: 78a987983d55e554257a5b19bdf0124fa7655df75dc1f1594effbc87fbf71dc4

### VP-0019: Omit support for shell messages

**Requirement**: The ValueError message contains bash, zsh, fish

**Targeted change**: Omit support for shell messages (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0020

[Download patch](patches/P-0020-7951928c7a07.patch)

SHA-256: 7951928c7a07b18b2542af697d22713b39e14d888b18c29cdad381b46daccbf4

### VP-0020: Remove duplicate aliases

**Requirement**: In Bash/Zsh, two duplicate registered lines are retained with their order preserved; in Fish, the output is not affected by aliases.

**Targeted change**: Remove duplicate aliases (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0021

[Download patch](patches/P-0021-7a569f79eadc.patch)

SHA-256: 7a569f79eadc455bbc1a0eecb912029978e8cf6cce9acbd6dbdb74a8b1d7e11e

### VP-0021: Bash colon options do not need to be escaped

**Requirement**: The characters in the corresponding local option match the baseline without extending escaping to global options.

**Targeted change**: Bash colon options do not need to be escaped (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0022

[Download patch](patches/P-0022-7fdc792132e3.patch)

SHA-256: 7fdc792132e3e4d8aad5bb7207a233e1df2a3470e204e77753ff4b7e14193424

### VP-0022: Remove space-based command references in Bash/Zsh

**Requirement**: Quote command names containing spaces in both the list and case entries as in the baseline. Preserve names containing colons.

**Targeted change**: Remove space-based command references in Bash/Zsh (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0023

[Download patch](patches/P-0023-84a37aced3a8.patch)

SHA-256: 84a37aced3a8ad151488fd2980365dfb63f7d007cbe6d21c20b0707f0a20a903

### VP-0023: Bypass realpath

**Requirement**: Script identity fields match the baseline. Preserve input precedence, package-name fallback, and the results of realpath and basename.

**Targeted change**: Bypass realpath (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0025

[Download patch](patches/P-0025-a9c9895f6246.patch)

SHA-256: a9c9895f62464aa7d532e0648b662be9c19924eaf4b8a58a733dbc220223fc24

### VP-0025: Introducing additional application name state modifications

**Requirement**: In addition to existing initialization, definition preparation, and traversal loading, registration mapping, command properties/options, and loader configuration remain unchanged.

**Targeted change**: Introducing additional application name state modifications (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0026

[Download patch](patches/P-0026-ade91a644daa.patch)

SHA-256: ade91a644daa676c8037dd170c3e11cb3186f5b6ddcb1d887e736574038ee132

### VP-0026: Bypass Traversal Initialization

**Requirement**: Existing initialization markers and default command registrations occur once, and are not extracted or bypassed.

**Targeted change**: Bypass Traversal Initialization (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

### VP-0027: Bypass lazy materialization

**Requirement**: The required command instance is registered with the existing loader. Subsequent traversal will reuse the registered instance, ensuring consistent loading timing.

**Targeted change**: Bypass lazy materialization (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0027

[Download patch](patches/P-0027-b232f8c1c286.patch)

SHA-256: b232f8c1c286ef934f58f464c228dce420be1e1ecb9bbc6b6b064c299fd551d0

### VP-0028: command helper handles generating data traversal

**Requirement**: The command and its own helpers no longer have the responsibility of generating data preparation, traversing, and concatenating various shell formats.

**Targeted change**: command helper handles generating data traversal (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0028

[Download patch](patches/P-0028-bad929a18fb7.patch)

SHA-256: bad929a18fb7daea695927f63a51c29312cb292afd7f2975a56cff6ffdde5758

### VP-0029: Fish namespace changed to Ye name space

**Requirement**: namespace, leaf command, seen-subcommand conditions, and cmds_names are consistent with the baseline.

**Targeted change**: Fish namespace changed to Ye name space (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0029

[Download patch](patches/P-0029-bd9e715283fa.patch)

SHA-256: bd9e715283fa67c9913f331b71ae463806558f5bed14595172f7e885ba316f70

### VP-0030: Ignore the end part of the environment path and use bash by default

**Requirement**: Choose Zsh for responsibility generation, no path overall matching or default guessing

**Targeted change**: Ignore the end part of the environment path and use bash by default (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0030

[Download patch](patches/P-0030-c363ba9861f1.patch)

SHA-256: c363ba9861f17608add76d96d69c1abcc3b94934aa6255c0ad261d63c22760c6

### VP-0031: Environment Coverage Explicit Shell

**Requirement**: Select Bash Generation Responsibility and Write Bash Script

**Targeted change**: Environment Coverage Explicit Shell (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0031

[Download patch](patches/P-0031-c4f018bec0f9.patch)

SHA-256: c4f018bec0f9634bb80df805a842d6110e9405bd27ee957e42783072a10a70ea

### VP-0032: Targeted regression: The success command returned 0, indicating that the application exited with a successful status.

**Requirement**: The success command returned 0, indicating that the application exited with a successful status.

**Targeted change**: Targeted regression: The success command returned 0, indicating that the application exited with a successful status. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0032

[Download patch](patches/P-0032-ccb9a9e5cdbb.patch)

SHA-256: ccb9a9e5cdbb8f5be39bb319dd2fa5692535c6db1dc541cd057623095a8edec6

### VP-0033: Targeted regression: The responsibility for filling in the common template is replaced by three substitutions, without specifying the template position or private method names.

**Requirement**: The responsibility for filling in the common template is replaced by three substitutions, without specifying the template position or private method names.

**Targeted change**: Targeted regression: The responsibility for filling in the common template is replaced by three substitutions, without specifying the template position or private method names. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0033

[Download patch](patches/P-0033-d180f88d69ed.patch)

SHA-256: d180f88d69edd66a5f8fc3bfa2c6d3e9b41c323dbe8ff3dd4abc55b2ce97dfd6

### VP-0034: Hidden commands have been incorporated

**Requirement**: Corresponding commands and their options - Normal generation entries - Absent

**Targeted change**: Hidden commands have been incorporated (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0034

[Download patch](patches/P-0034-d8ddf84db7a9.patch)

SHA-256: d8ddf84db7a94ee23cd65ffa5dcb0fc2466eeb84367536fa171a69552a72136f

### VP-0035: Default Bash Realpath Registration Vulnerability

**Requirement**: The output of basename/realpath in Bash, the existing functions in Zsh, and script_name in Fish are consistent with the baseline.

**Targeted change**: Default Bash Realpath Registration Vulnerability (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0035

[Download patch](patches/P-0035-dc2bf0b1112e.patch)

SHA-256: dc2bf0b1112eb9eef1b6b572fb7e167d6a4b8800a1b250504be5e77abf77c1e6

### VP-0036: Targeted regression: Define the naming rules in one place and have the shell generators consume the result.

**Requirement**: Define the naming rules in one place and have the shell generators consume the result.

**Targeted change**: Targeted regression: Define the naming rules in one place and have the shell generators consume the result. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0036

[Download patch](patches/P-0036-de69a725be98.patch)

SHA-256: de69a725be98b7f95e8b4471693c1489c0688f4f97ae21b3f518488cf3a855dd

### VP-0037: zsh format: Responsibility shifted back to the command internal helper

**Requirement**: Zsh format generation is handled by external commands; replacing this responsibility does not require modifying Bash/Fish or the configuration.

**Targeted change**: zsh format: Responsibility shifted back to the command internal helper (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0037

[Download patch](patches/P-0037-e8bc3996999e.patch)

SHA-256: e8bc3996999e226602ee3b96c6b8e535182921fb0175400d908543391202819c

### VP-0038: Targeted regression: RuntimeError

**Requirement**: RuntimeError; Root path differences are disclosed as exceptions for acceptance

**Targeted change**: Targeted regression: RuntimeError (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0038

[Download patch](patches/P-0038-e932b5fb3069.patch)

SHA-256: e932b5fb30697d6422abf356d49824c9ea61a3170fa30e3a0d776eae951560d2

### VP-0039: Function hash truncation length error

**Requirement**: Functions with the same script name and path should be consistent with the baseline. It cannot be proven solely by fixed mock function names.

**Targeted change**: Function hash truncation length error (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0039

[Download patch](patches/P-0039-f51b06035834.patch)

SHA-256: f51b060358341b6f66ae8d7cf7e82619d31feed92c7def9360d1cb2dadc798aa

### VP-0040: Targeted regression: The sorting and filtering operations are defined by the same responsibility, and the shell processes them in its own format.

**Requirement**: The sorting and filtering common traversal is defined by the same responsibility, and the shells consume them in their respective formats; necessary namespace queries are retained.

**Targeted change**: Targeted regression: The sorting and filtering operations are defined by the same responsibility, and the shell processes them in its own format. (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error

## P-0040

[Download patch](patches/P-0040-f84b745526b6.patch)

SHA-256: f84b745526b640074870b87efac45fdb5ba2f19f2be456483effe15e7e46f1d7

### VP-0041: Change the whitespace in the zsh template text

**Requirement**: The complete Zsh script matches character by character with the input public baseline, including template replacements and a final line break.

**Targeted change**: Change the whitespace in the zsh template text (changed files: src/cleo/commands/completions/__init__.py, src/cleo/commands/completions/base.py, src/cleo/commands/completions/bash.py, src/cleo/commands/completions/fish.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 8c3f1bbf82d9, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: This outcome does not establish experimental failure

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- git apply failed
- Import or test collection error
