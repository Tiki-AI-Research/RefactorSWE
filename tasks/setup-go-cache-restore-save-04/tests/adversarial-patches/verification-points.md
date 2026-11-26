# Adversarial test patches and verification points

Task: setup-go-cache-restore-save-04

Base commit: fba3fb4ead8c8e09a06f1d32ae5436e5818eff15

Scope: partial export. Some items remain unresolved.
This package contains 34 distinct patches and 35 verification points.
The export omits 0 records without a primary patch, including controls and historical revisions. It excludes 1 control or auxiliary items and leaves 39 items unresolved.
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
| [P-0001](patches/P-0001-0cb7946d79a3.patch) | VP-0001 | The workspace's real go.mod exists, omitting the dependency path. |
| [P-0002](patches/P-0002-1c16bca7fce6.patch) | VP-0002 | RUNNER_OS=Linux, ImageOS=audit-image, Version 1.13.1, Hash hash-value |
| [P-0003](patches/P-0003-1d87639fc317.patch) | VP-0003, VP-0004 | The save section directory is missing. Missing partial path in save section |
| [P-0004](patches/P-0004-1e39ac6b6f47.patch) | VP-0005 | cache=false |
| [P-0005](patches/P-0005-3448422bd68a.patch) | VP-0006 | Pass explicit, **/go.sum, and a/go.sum followed by a newline and b/go.mod, in that order. |
| [P-0006](patches/P-0006-378bf4e2ceec.patch) | VP-0007 | Use a valid state-primary that differs from state-matched, with one existing directory. |
| [P-0007](patches/P-0007-38e8254bd408.patch) | VP-0008 | cache=true, state-primary differs from state-matched, and one directory is missing. |
| [P-0008](patches/P-0008-3b6f215adf0f.patch) | VP-0009 | Both CACHE_KEY and CACHE_RESULT equal state-primary. |
| [P-0009](patches/P-0009-3fc7a73d669a.patch) | VP-0010 | Run(true) - Normal save |
| [P-0010](patches/P-0010-43e733f2baff.patch) | VP-0011 | Independent analysis of unknown-audit |
| [P-0011](patches/P-0011-60b1ee14f944.patch) | VP-0012 | cache=true and both directories are missing |
| [P-0012](patches/P-0012-62e16d07d939.patch) | VP-0013 | The service returned an empty string. |
| [P-0013](patches/P-0013-70c5db87c3a4.patch) | VP-0014 | Discover one existing directory and one missing directory. |
| [P-0014](patches/P-0014-795a284d89c9.patch) | VP-0015 | The service returns returned-key. |
| [P-0015](patches/P-0015-79f5fba9a105.patch) | VP-0016 | Exercise three cache/feature combinations in main: disabled, enabled but unavailable, and enabled and available. |
| [P-0016](patches/P-0016-88231a3de52c.patch) | VP-0017 | restore hit |
| [P-0017](patches/P-0017-8f8c1e8ca828.patch) | VP-0018 | Save the default package manager and identify one existing and one missing directory. |
| [P-0018](patches/P-0018-91197552b621.patch) | VP-0019 | The context is created twice for the same call when restoring. |
| [P-0019](patches/P-0019-93ebcafd1493.patch) | VP-0020 | main enabled cache and restore encountered an error |
| [P-0020](patches/P-0020-966b2c2f9fdc.patch) | VP-0021 | Targeted regression: Could not get cache folder paths. No empty array was successfully returned. |
| [P-0021](patches/P-0021-a5c7f02130ec.patch) | VP-0022 | restore explicit dependency path |
| [P-0022](patches/P-0022-a5ec75696d67.patch) | VP-0023 | After restore is successful, save reads the existing state. |
| [P-0023](patches/P-0023-af4ddb11fc1f.patch) | VP-0024 | restore first creates the correct context, then discovers another path and requests services using the second path. |
| [P-0024](patches/P-0024-b575f373e8fe.patch) | VP-0025 | First empty, second successful |
| [P-0025](patches/P-0025-bdb69d00923c.patch) | VP-0026 | The service returned an empty string. |
| [P-0026](patches/P-0026-c3053584c6f3.patch) | VP-0027 | cache=true with an empty CACHE_KEY |
| [P-0027](patches/P-0027-c6f1d01bdc39.patch) | VP-0028 | The service returns returned-key. |
| [P-0028](patches/P-0028-cc7bc4ddeb1e.patch) | VP-0029 | The three-parameter restore returns a non-empty returned-key. |
| [P-0029](patches/P-0029-e7577de07630.patch) | VP-0030 | Independent analysis of default, returning go.mod and GOMODCACHE/GOCACHE in order |
| [P-0030](patches/P-0030-e980d1a83bc2.patch) | VP-0031 | RUNNER_OS=Windows, ImageOS=audit-image |
| [P-0031](patches/P-0031-ebe93d9471a8.patch) | VP-0032 | The explicit path hashFiles returns an empty string. |
| [P-0032](patches/P-0032-ed2a21008997.patch) | VP-0033 | Save Service Throws Audit Save Failure |
| [P-0033](patches/P-0033-f256ea80aec9.patch) | VP-0034 | Delete test workspace/go.mod, omit the path |
| [P-0034](patches/P-0034-fbaa3e90fae5.patch) | VP-0035 | Save service returns -1 |

## P-0001

[Download patch](patches/P-0001-0cb7946d79a3.patch)

SHA-256: 0cb7946d79a37b41f58b1489a6a86f3b6b15685032ee068e96e265d40d8f620f

### VP-0001: The workspace's real go.mod exists, omitting the dependency path.

**Requirement**: The actual parameter of hashFiles is workspace/go.mod.

**Targeted change**: The workspace's real go.mod exists, omitting the dependency path. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0002

[Download patch](patches/P-0002-1c16bca7fce6.patch)

SHA-256: 1c16bca7fce66c43403a9953b41f1d7b06d72361fe4b34bbcb6b4fc535d11321

### VP-0002: RUNNER_OS=Linux, ImageOS=audit-image, Version 1.13.1, Hash hash-value

**Requirement**: CACHE_KEY and restore key comply with setup-go-<platform>-<arch>-<ImageOS>-go-<version>-<hash>

**Targeted change**: RUNNER_OS=Linux, ImageOS=audit-image, Version 1.13.1, Hash hash-value (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0003

[Download patch](patches/P-0003-1d87639fc317.patch)

SHA-256: 1d87639fc3179f83f210be21541d5e07b7ac0f410bade18ed21cda6b72518e95

### VP-0003: The save section directory is missing.

**Requirement**: The existence result is provided independently within the context of responsibility. Save consumes this result.

**Targeted change**: The save section's directory is missing; move the existence check to the save entry, still passing the full path. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

### VP-0004: Missing partial path in save section

**Requirement**: Obtain the save paths and missing-path report from the context, without a second implementation of the preparation logic.

**Targeted change**: The path for "save" is missing; "save" directly uses existsSync to handle the existence result of the consumption context. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0004

[Download patch](patches/P-0004-1e39ac6b6f47.patch)

SHA-256: 1e39ac6b6f471c8809b30d1889b8e1d70c667635d3684391184295ac54831ac2

### VP-0005: cache=false

**Requirement**: No findings/saveCache/warning/setFailed/process.exit

**Targeted change**: cache=false (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0005

[Download patch](patches/P-0005-3448422bd68a.patch)

SHA-256: 3448422bd68aa47a0fe9da2b77fad1145b79c1f113777e8021c856f10eac8439

### VP-0006: Pass explicit, **/go.sum, and a/go.sum followed by a newline and b/go.mod, in that order.

**Requirement**: The actual parameter of hashFiles is equal to the input, which has not been changed to the default file.

**Targeted change**: Pass explicit, **/go.sum, and a/go.sum followed by a newline and b/go.mod, in that order. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0006

[Download patch](patches/P-0006-378bf4e2ceec.patch)

SHA-256: 378bf4e2ceec0f4b85cce1a9966f656d05e1eaf8669926beacb56f7424ff82ad

### VP-0007: Use a valid state-primary that differs from state-matched, with one existing directory.

**Requirement**: Save the full path of saveCache and the actual parameter of CACHE_KEY. The cache is saved with the key: <key>. Do not recalculate the dependency hash.

**Targeted change**: Use a valid state-primary that differs from state-matched, with one existing directory. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0007

[Download patch](patches/P-0007-38e8254bd408.patch)

SHA-256: 38e8254bd4087452c21039f841caddd0089a8f6ee58fd35efa0acebfbc120ee6

### VP-0008: cache=true, state-primary differs from state-matched, and one directory is missing.

**Requirement**: The existing [warning] info contains missing directories; the service obtains the complete path under valid primary keys.

**Targeted change**: cache=true, state-primary differs from state-matched, and one directory is missing. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0008

[Download patch](patches/P-0008-3b6f215adf0f.patch)

SHA-256: 3b6f215adf0f300a96a75d260f2cfc0ee1ee375d7897d0960e5fa26819d09151

### VP-0009: Both CACHE_KEY and CACHE_RESULT equal state-primary.

**Requirement**: Cache hit occurred on the primary key <key>, not saving cache. No saveCache

**Targeted change**: Both CACHE_KEY and CACHE_RESULT equal state-primary. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0009

[Download patch](patches/P-0009-3fc7a73d669a.patch)

SHA-256: 3fc7a73d669a53ac53c46cae0c719fc850067043b47b0ecac21c2224233f1618

### VP-0010: Run(true) - Normal save

**Requirement**: After enabling the normal decision for caching, true triggers exit(0), and the flag is naturally completed; the error catch path does not enter this exit.

**Targeted change**: Run(true) - Normal save (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0010

[Download patch](patches/P-0010-43e733f2baff.patch)

SHA-256: 43e733f2baff8e989d8b5ad47e17e77bffefcabe54e6587ff72944fa6ebe0c0c

### VP-0011: Independent analysis of unknown-audit

**Requirement**: Existing Error Texts with Given Names

**Targeted change**: Independent analysis of unknown-audit (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts, src/cache-utils.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0011

[Download patch](patches/P-0011-60b1ee14f944.patch)

SHA-256: 60b1ee14f944ca03710fdb8d1280ec075f27aeaa9aae26de1e0d85d71131319d

### VP-0012: cache=true and both directories are missing

**Requirement**: There are no cache folders on the disk, saveCache has not been called.

**Targeted change**: cache=true and both directories are missing (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0012

[Download patch](patches/P-0012-62e16d07d939.patch)

SHA-256: 62e16d07d939346f029a0b330f748ee7783ea5614c5eed6b24ad99af4e7ef1a1

### VP-0013: The service returned an empty string.

**Requirement**: cache-hit=false and Cache is not found, baseline repetition false, write order maintained

**Targeted change**: The service returned an empty string. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0013

[Download patch](patches/P-0013-70c5db87c3a4.patch)

SHA-256: 70c5db87c3a447a3dfba529b696912b5ae01ab80b93d5ffd7f0838b05d15df5c

### VP-0014: Discover one existing directory and one missing directory.

**Requirement**: The service path array is equal to the discovered result, even if the directory does not exist yet.

**Targeted change**: Discover one existing directory and one missing directory. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0014

[Download patch](patches/P-0014-795a284d89c9.patch)

SHA-256: 795a284d89c9b7490ed19fe15b677360611daca3a379a8be9797ee34bcb3b8d3

### VP-0015: The service returns returned-key.

**Requirement**: The values and names written by the state remain unchanged.

**Targeted change**: The service returns returned-key. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0015

[Download patch](patches/P-0015-79f5fba9a105.patch)

SHA-256: 79f5fba9a105c33903b1856e08b64faf1de91abdaceef1a6432760f0d20467a7

### VP-0016: Exercise three cache/feature combinations in main: disabled, enabled but unavailable, and enabled and available.

**Requirement**: No restore call when disabled or unavailable; call only when enabled and available.

**Targeted change**: Exercise three cache/feature combinations in main: disabled, enabled but unavailable, and enabled and available. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts, src/main.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0016

[Download patch](patches/P-0016-88231a3de52c.patch)

SHA-256: 88231a3de52cb03a4c3a6c94c7683fca469cebb3706eb813602a4fd4135aadd6

### VP-0017: restore hit

**Requirement**: saveState(CACHE_KEY, primaryKey) call sequence precedes the service request

**Targeted change**: restore hit (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0017

[Download patch](patches/P-0017-8f8c1e8ca828.patch)

SHA-256: 8f8c1e8ca8285ca1f437c050a620beeee4ef95dafb13f4de6c27e7f817293530

### VP-0018: Save the default package manager and identify one existing and one missing directory.

**Requirement**: Structural inspection: It was found that the sequence is owned by the same implementation; neither process implements the sequence separately.

**Targeted change**: The save default package manager found one existing and one missing directory; only the found sequences were moved back to the save entry, and the other results remained the same. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0018

[Download patch](patches/P-0018-91197552b621.patch)

SHA-256: 91197552b62183793d74fdf7b08fa7554cc2ffa5bcf41ea409c424dd031b110d

### VP-0019: The context is created twice for the same call when restoring.

**Requirement**: A single execution flow must not reconstruct package manager selection or discovery twice. The interpretation of counts across processes remains unresolved.

**Targeted change**: restore context created twice in the same call; observe the number of occurrences in each process (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0019

[Download patch](patches/P-0019-93ebcafd1493.patch)

SHA-256: 93ebcafd1493311089e26c4f5139ee3cd0bacfa2d9bb4ba925b4ad6206fe4c25

### VP-0020: main enabled cache and restore encountered an error

**Requirement**: Restore cache failed: <message>. The cache error did not cause setFailed. The subsequent action output is still completed.

**Targeted change**: main enabled cache and restore encountered an error (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts, src/main.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0020

[Download patch](patches/P-0020-966b2c2f9fdc.patch)

SHA-256: 966b2c2f9fdcea5fd808e1254e33fe0e0e61aa8ca61f4aa5b938574b4e6869d7

### VP-0021: Targeted regression: Could not get cache folder paths. No empty array was successfully returned.

**Requirement**: Could not get cache folder paths. No empty array was successfully returned.

**Targeted change**: Targeted regression: Could not get cache folder paths. No empty array was successfully returned. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts, src/cache-utils.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0021

[Download patch](patches/P-0021-a5c7f02130ec.patch)

SHA-256: a5c7f02130ec7b68202be816dfad4085a291b39bc023e94d4132f2ca3172e7c7

### VP-0022: restore explicit dependency path

**Requirement**: In the primary key generation responsibility, there is no second set of keys derived for restore.

**Targeted change**: restore explicitly depends on the path; derive the key back to the restore entry, maintaining the key format and error text (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0022

[Download patch](patches/P-0022-a5ec75696d67.patch)

SHA-256: a5ec75696d676b90d93c79e008fb68f7d8896b2e4b964e7292291cd3f4987161

### VP-0023: After restore is successful, save reads the existing state.

**Requirement**: The responsibility for accessing CACHE_KEY/CACHE_RESULT has been moved to the context, and the step value has been passed through the original state.

**Targeted change**: After restore is successful, save reads the existing state; only write CACHE_KEY back to the restore entry. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0023

[Download patch](patches/P-0023-af4ddb11fc1f.patch)

SHA-256: af4ddb11fc1f27494d130048bdf103993f31fc0b4fa7516ae6e6aac90ba12ff7

### VP-0024: restore first creates the correct context, then discovers another path and requests services using the second path.

**Requirement**: Use the restore paths supplied by the shared context without rebuilding the path chain independently.

**Targeted change**: restore first creates the correct context, then discovers another path and requests services using the second path. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0024

[Download patch](patches/P-0024-b575f373e8fe.patch)

SHA-256: b575f373e8fe2c45d37140913d3e439e8a098bc89fce91909f44225fb1d9bdd1

### VP-0025: First empty, second successful

**Requirement**: Non-empty successful array, order and values, and failure command error messages; do not throw errors if paths still exist.

**Targeted change**: First empty, second successful (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts, src/cache-utils.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0025

[Download patch](patches/P-0025-bdb69d00923c.patch)

SHA-256: bdb69d00923c51e1c2c5312f05f6e7fe84af9854d7d8588fa17e4d03d77f6a62

### VP-0026: The service returned an empty string.

**Requirement**: No matching key state written

**Targeted change**: The service returned an empty string. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0026

[Download patch](patches/P-0026-c3053584c6f3.patch)

SHA-256: c3053584c6f35c5a807ef7990de2be6e1b7c4636867edab4af676734a5548cfe

### VP-0027: cache=true with an empty CACHE_KEY

**Requirement**: Emit "Primary key was not generated. Please check the log messages above for more errors or information" without calling saveCache.

**Targeted change**: cache=true with an empty CACHE_KEY (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0027

[Download patch](patches/P-0027-c6f1d01bdc39.patch)

SHA-256: c6f1d01bdc399cf8426e08ce614efeef8a3ab76fc288c5d1f3710be8787f8135

### VP-0028: The service returns returned-key.

**Requirement**: After the service returns, emit cache-hit=true followed by "Cache restored from key: <key>" in that order.

**Targeted change**: The service returns returned-key. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0028

[Download patch](patches/P-0028-cc7bc4ddeb1e.patch)

SHA-256: cc7bc4ddeb1ec70bf70b3df412d5f3a56fcfd028792a003531b34abb63810944

### VP-0029: The three-parameter restore returns a non-empty returned-key.

**Requirement**: The resolved value is undefined in some cases, but the optional path can still be omitted.

**Targeted change**: The three-parameter restore returns a non-empty returned-key. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0029

[Download patch](patches/P-0029-e7577de07630.patch)

SHA-256: e7577de07630eebed4185b37b3f967c8934b6f8fb1bdf27b023d8f324ed1ad81

### VP-0030: Independent analysis of default, returning go.mod and GOMODCACHE/GOCACHE in order

**Requirement**: go.mod and the two Go cache commands in order

**Targeted change**: Independent analysis of default, returning go.mod and GOMODCACHE/GOCACHE in order (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts, src/package-managers.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0030

[Download patch](patches/P-0030-e980d1a83bc2.patch)

SHA-256: e980d1a83bc2a1063e780b8aca7ed36bf31c4211d08d8bf5c1e78c73bb7f6625

### VP-0031: RUNNER_OS=Windows, ImageOS=audit-image

**Requirement**: CACHE_KEY and restore key comply with setup-go-<platform>-<arch>-go-<version>-<hash>.

**Targeted change**: RUNNER_OS=Windows, ImageOS=audit-image (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0031

[Download patch](patches/P-0031-ebe93d9471a8.patch)

SHA-256: ebe93d9471a89d69f93862a47dd61199f504f9c5cdc74541632c51cc69af7f62

### VP-0032: The explicit path hashFiles returns an empty string.

**Requirement**: Some specified paths were not resolved, unable to cache dependencies. No primary key write/restore request

**Targeted change**: The explicit path hashFiles returns an empty string. (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0032

[Download patch](patches/P-0032-ed2a21008997.patch)

SHA-256: ed2a2100899717ddfd182a5b044992f22da5a42c329cc4447d033f0b1b764d3d

### VP-0033: Save Service Throws Audit Save Failure

**Requirement**: The run is normal, resolve, and the original error message is displayed. No setFailed occurs, and a successful save is output.

**Targeted change**: Save Service Throws Audit Save Failure (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0033

[Download patch](patches/P-0033-f256ea80aec9.patch)

SHA-256: f256ea80aec9e596c516299d3dc63fc99e53e8d27cff4d9f235abae59aeaa4ec

### VP-0034: Delete test workspace/go.mod, omit the path

**Requirement**: The Dependencies file is not found in <workspace>. Supported file pattern: <pattern>; No restore request.

**Targeted change**: Delete test workspace/go.mod, omit the path (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed

## P-0034

[Download patch](patches/P-0034-fbaa3e90fae5.patch)

SHA-256: fbaa3e90fae5819bfef4df8c763b8c4ef012654c376ad8fba959c659b41fb564

### VP-0035: Save service returns -1

**Requirement**: Cache was not saved for the key: <key>, no success message or setFailed

**Targeted change**: Save service returns -1 (changed files: src/cache-context.ts, src/cache-restore.ts, src/cache-save.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at fba3fb4ead8c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or testing failed
