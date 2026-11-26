# Adversarial test patches and verification points

Task: sveltejs-devalue-20260917060608-25e4d1

Base commit: a3d30d94c8fd9cfca4b774814ff9d5bfade5010c

Scope: adversarial patches exported after a complete inventory.
This package contains 41 distinct patches and 42 verification points.
The export omits 0 records without a primary patch, including controls and historical revisions. It excludes 1 control or auxiliary items and leaves 0 items unresolved.
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
| [P-0001](patches/P-0001-03ced3890542.patch) | VP-0001 | Convert ordinary array holes into undefined properties |
| [P-0002](patches/P-0002-044f66cd57e9.patch) | VP-0002, VP-0003 | Illegal score reference was accepted; Invalid sub-value reference in nested valid sparse metadata was accepted |
| [P-0003](patches/P-0003-05a8fdcd8c4f.patch) | VP-0004 | The sparse length verification is omitted, resulting in a native RangeError. |
| [P-0004](patches/P-0004-11c69e2973a9.patch) | VP-0005 | The custom reviver receives the original index instead of rebuilding the value. |
| [P-0005](patches/P-0005-1b176b22ade1.patch) | VP-0006 | All hydration definitions have been re-grouped into a single closure called unflatten. |
| [P-0006](patches/P-0006-1c3a9140799a.patch) | VP-0007 | Construct the sparse array one element too long while preserving its indices and back-references. |
| [P-0007](patches/P-0007-1d7ca8eadc62.patch) | VP-0008 | The reviver misidentified the target and was disguised as something else. |
| [P-0008](patches/P-0008-2fa15af74bed.patch) | VP-0009 | Expanding the operation coverage results in the loss of inherited members |
| [P-0009](patches/P-0009-39721dfa4328.patch) | VP-0010 | Non-string buffer encoding retains old errors and violates explicit exceptions. |
| [P-0010](patches/P-0010-49add41f782f.patch) | VP-0011 | Incorrectly replace a plain object's back-reference with an empty object. |
| [P-0011](patches/P-0011-4fdbd57b8f2d.patch) | VP-0012 | The built-in Date dispatch occurs before the named reviver |
| [P-0012](patches/P-0012-5869f2582ead.patch) | VP-0013 | The current table length verification failed before cache reuse |
| [P-0013](patches/P-0013-7458ea9c06a9.patch) | VP-0014 | The packaging of null is silently accepted, and the native TypeError disappears. |
| [P-0014](patches/P-0014-7a75af96d703.patch) | VP-0015 | Require consumers to supply the internal context. |
| [P-0015](patches/P-0015-7f530a77f5ae.patch) | VP-0016 | The operation misidentified the identity and was wrapped up. |
| [P-0016](patches/P-0016-806668d99716.patch) | VP-0017 | Null-prototype container incorrectly uses the plain object constructor |
| [P-0017](patches/P-0017-82405f4d25d2.patch) | VP-0018 | Unified security errors for common objects proto |
| [P-0018](patches/P-0018-857e170b766c.patch) | VP-0019 | null-prototype object proto has inconsistent security errors |
| [P-0019](patches/P-0019-8e6562752c12.patch) | VP-0020 | view Dispatch Direct Inception Opaque Buffer Handle |
| [P-0020](patches/P-0020-920f42561699.patch) | VP-0021 | The object filling uses the ambient current context, and the callback reentrancy contaminates subsequent sibling references. |
| [P-0021](patches/P-0021-929dc8349592.patch) | VP-0022 | Delete the custom loop path that has already parsed the payload |
| [P-0022](patches/P-0022-94ff45a95579.patch) | VP-0023 | The excessive base64 string verification changes the compatible behavior of the actual Node decoder. |
| [P-0023](patches/P-0023-98cb60cfb3c7.patch) | VP-0024 | Share the parsed cache across calls. |
| [P-0024](patches/P-0024-99853347b592.patch) | VP-0025 | hydration added a real third-party runtime import and call |
| [P-0025](patches/P-0025-99b04134d706.patch) | VP-0026 | The raw custom payload was incorrectly replaced with undefined. |
| [P-0026](patches/P-0026-a5e9495e8e99.patch) | VP-0027 | Targeted regression: Production modifications are limited to parsing/hydration. |
| [P-0027](patches/P-0027-a8f11587b5ec.patch) | VP-0028 | JSON syntax error types and messages are unified and packaged. |
| [P-0028](patches/P-0028-b00e29116061.patch) | VP-0029 | Omitted sparse index verification, incorrect writing of negative attribute |
| [P-0029](patches/P-0029-b959b040d455.patch) | VP-0030 | The view constructor RangeError is uniformly packaged. |
| [P-0030](patches/P-0030-bca0276d11cd.patch) | VP-0031 | Only allow the release of illegal empty tables |
| [P-0031](patches/P-0031-bd59e361e7b5.patch) | VP-0032 | View illegal buffer index error message drift |
| [P-0032](patches/P-0032-bd8055438753.patch) | VP-0033 | Map creates a new Map by referencing an incorrect value |
| [P-0033](patches/P-0033-bef7c2b3a4fe.patch) | VP-0034 | Empty array replaced for ordinary array self-reference error |
| [P-0034](patches/P-0034-cd9ba1aafb07.patch) | VP-0035 | Remove custom revivers from each caller of owner and store them in a module-level mutable WeakMap |
| [P-0035](patches/P-0035-cdf5bdc3dc79.patch) | VP-0036 | parse loses the second parameter, but the third parameter operation is still correct. |
| [P-0036](patches/P-0036-dc5ed21a25f4.patch) | VP-0037 | The custom loop encountered an error during processing. |
| [P-0037](patches/P-0037-e77cfea3739f.patch) | VP-0038 | Unknown tag errors are collectively packaged |
| [P-0038](patches/P-0038-eaaf0375c423.patch) | VP-0039 | Six categories of distribution responsibilities are merged into one helper, maintaining sufficient utility helpers to meet the needs of pure counting. |
| [P-0039](patches/P-0039-f0c42872c04d.patch) | VP-0040 | Even adding comments violates the boundaries. |
| [P-0040](patches/P-0040-f3baae70c5f5.patch) | VP-0041 | Omitted the final sparse review; subsequent reviver modifications have handled bypassing boundaries of the index. |
| [P-0041](patches/P-0041-fdffa2eb40f1.patch) | VP-0042 | Create a new Set from Set member errors |

## P-0001

[Download patch](patches/P-0001-03ced3890542.patch)

SHA-256: 03ced389054276c3cd7382b09d799dd9303f65af1daa781fe2c6f6311893c766

### VP-0001: Convert ordinary array holes into undefined properties

**Requirement**: Legal primitive sentinels and ordinary array holes retain their respective meanings.

**Targeted change**: Convert ordinary array holes into undefined properties (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0002

[Download patch](patches/P-0002-044f66cd57e9.patch)

SHA-256: 044f66cd57e9786224964a38d1da912b582ba69cafc35ec01da8cdfa163bda36

### VP-0002: Illegal score reference was accepted

**Requirement**: Illegal payload references are uniformly rejected.

**Targeted change**: Illegal score reference was accepted (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

### VP-0003: Invalid sub-value reference in nested valid sparse metadata was accepted

**Requirement**: Invalid sub-value reference in nested valid sparse metadata was accepted

**Targeted change**: Invalid sub-value reference in nested valid sparse metadata was accepted (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0003

[Download patch](patches/P-0003-05a8fdcd8c4f.patch)

SHA-256: 05a8fdcd8c4ff99fcbd751cd2f8cf70648af3a985d02ea504b70bbbabb423236

### VP-0004: The sparse length verification is omitted, resulting in a native RangeError.

**Requirement**: Sparse declaration length maintains numerical boundary verification

**Targeted change**: The sparse length verification is omitted, resulting in a native RangeError. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0004

[Download patch](patches/P-0004-11c69e2973a9.patch)

SHA-256: 11c69e2973a973945f19aca4a39b0f99bd05b7bfbc29136a29ec4e3f9a5c4911

### VP-0005: The custom reviver receives the original index instead of rebuilding the value.

**Requirement**: The reviver correctly handles table references in the payload.

**Targeted change**: The custom reviver receives the original index instead of rebuilding the value. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0005

[Download patch](patches/P-0005-1b176b22ade1.patch)

SHA-256: 1b176b22ade1b0d979e9a70d5f6223d4f9ca0a9a5aec94ffb3925a48b297a6e8

### VP-0006: All hydration definitions have been re-grouped into a single closure called unflatten.

**Requirement**: Parse/unflatten: Delegates the hydration responsibilities; unflatten: No nested hydration definitions exist within.

**Targeted change**: All hydration definitions have been re-grouped into a single closure called unflatten. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0006

[Download patch](patches/P-0006-1c3a9140799a.patch)

SHA-256: 1c3a9140799a431fe6f441ce8a0ac8d370be3212d5623342c0de6f63119c79a0

### VP-0007: Construct the sparse array one element too long while preserving its indices and back-references.

**Requirement**: Sparse arrays maintain the declaration length, padding index, and reference graph.

**Targeted change**: Construct the sparse array one element too long while preserving its indices and back-references. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0007

[Download patch](patches/P-0007-1d7ca8eadc62.patch)

SHA-256: 1d7ca8eadc6277fdd1a4535f8ea91ace9b2b985bd8c60ed0a5b49696572494c2

### VP-0008: The reviver misidentified the target and was disguised as something else.

**Requirement**: reviver is spreading things incorrectly

**Targeted change**: The reviver misidentified the target and was disguised as something else. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0008

[Download patch](patches/P-0008-2fa15af74bed.patch)

SHA-256: 2fa15af74bed42f3dccd6677c451108eabe49839aff1716a1890ad76bb4a2d7a

### VP-0009: Expanding the operation coverage results in the loss of inherited members

**Requirement**: Each call to operation will continue to be merged according to the default rules.

**Targeted change**: Expanding the operation coverage results in the loss of inherited members (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0009

[Download patch](patches/P-0009-39721dfa4328.patch)

SHA-256: 39721dfa43288fe5342af752c645bd10c3db2806839ed90ad197a4de3318451a

### VP-0010: Non-string buffer encoding retains old errors and violates explicit exceptions.

**Requirement**: Built-in ArrayBuffer is missing or non-string encoding is rejected

**Targeted change**: Non-string buffer encoding retains old errors and violates explicit exceptions. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0010

[Download patch](patches/P-0010-49add41f782f.patch)

SHA-256: 49add41f782fd8ff97e7a0e60334edd3a62fa0c91ba23b03f43fb25c6866e1e5

### VP-0011: Incorrectly replace a plain object's back-reference with an empty object.

**Requirement**: Keep common objects and objects with circular references as shared.

**Targeted change**: Incorrectly replace a plain object's back-reference with an empty object. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0011

[Download patch](patches/P-0011-4fdbd57b8f2d.patch)

SHA-256: 4fdbd57b8f2d86468da271f47ec92cfa094fed600101e6da7d81eb64b9a3a71e

### VP-0012: The built-in Date dispatch occurs before the named reviver

**Requirement**: Custom Reviver continues to be distributed before the built-in tag

**Targeted change**: The built-in Date dispatch occurs before the named reviver (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0012

[Download patch](patches/P-0012-5869f2582ead.patch)

SHA-256: 5869f2582ead836633d80857407852bb0b834ce3c85908f85e59bd73574cc5dc

### VP-0013: The current table length verification failed before cache reuse

**Requirement**: After collapsing, the parsed index is still reused.

**Targeted change**: The current table length verification failed before cache reuse (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0013

[Download patch](patches/P-0013-7458ea9c06a9.patch)

SHA-256: 7458ea9c06a93466ae883efd1e38f72d8025628db2dc49324bc6f6c3e82c7a91

### VP-0014: The packaging of null is silently accepted, and the native TypeError disappears.

**Requirement**: Object is null, retain native TypeError

**Targeted change**: The packaging of null is silently accepted, and the native TypeError disappears. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0014

[Download patch](patches/P-0014-7a75af96d703.patch)

SHA-256: 7a75af96d703128d6fff0d268e194f6fea31f4d453ad6fbca3dc855d8195177a

### VP-0015: Require consumers to supply the internal context.

**Requirement**: Internal reorganization does not become a mandatory interface for consumers

**Targeted change**: Require consumers to supply the internal context. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0015

[Download patch](patches/P-0015-7f530a77f5ae.patch)

SHA-256: 7f530a77f5aeaf5d7ca0f63e5c34cf047181ae776ce5654144b1ed80b8869dd1

### VP-0016: The operation misidentified the identity and was wrapped up.

**Requirement**: Operation callback error maintains object identity

**Targeted change**: The operation misidentified the identity and was wrapped up. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0016

[Download patch](patches/P-0016-806668d99716.patch)

SHA-256: 806668d99716327a85f6daa264493b27bf72fa4fe773dda1120daab5aec1d5f5

### VP-0017: Null-prototype container incorrectly uses the plain object constructor

**Requirement**: The null-prototype object retains its prototype and reference graph.

**Targeted change**: Null-prototype container incorrectly uses the plain object constructor (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0017

[Download patch](patches/P-0017-82405f4d25d2.patch)

SHA-256: 82405f4d25d26bbcb70ad40b4d6821a1b11eff4cf9adeee4e2bcbf383807d3e6

### VP-0018: Unified security errors for common objects proto

**Requirement**: Rejecting ordinary objects containing __proto__

**Targeted change**: Unified security errors for common objects proto (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0018

[Download patch](patches/P-0018-857e170b766c.patch)

SHA-256: 857e170b766cfa34ba6713e9df9266311ad98a89f9186255aed6e7c8fe55e513

### VP-0019: null-prototype object proto has inconsistent security errors

**Requirement**: The null-prototype object rejects objects with __proto__

**Targeted change**: null-prototype object proto has inconsistent security errors (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0019

[Download patch](patches/P-0019-8e6562752c12.patch)

SHA-256: 8e6562752c126af310837e97cdef2028d82898bf6b442122cab6e4c045e82e7d

### VP-0020: view Dispatch Direct Inception Opaque Buffer Handle

**Requirement**: Opaque construction handles can be passed through operations/reviver.

**Targeted change**: view Dispatch Direct Inception Opaque Buffer Handle (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0020

[Download patch](patches/P-0020-920f42561699.patch)

SHA-256: 920f42561699f3879874e86c0ee03428abaf4384b1c7698a4a2d1d5201c853e6

### VP-0021: The object filling uses the ambient current context, and the callback reentrancy contaminates subsequent sibling references.

**Requirement**: Callback reentrancy does not contaminate the outer hydration

**Targeted change**: The object filling uses the ambient current context, and the callback reentrancy contaminates subsequent sibling references. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0021

[Download patch](patches/P-0021-929dc8349592.patch)

SHA-256: 929dc83495928fd9aa8842048508e8d0fbb9e6a76e88491f299a8d499b6ac05c

### VP-0022: Delete the custom loop path that has already parsed the payload

**Requirement**: Parsed payload reused, legitimate custom loops are not rejected incorrectly

**Targeted change**: Delete the custom loop path that has already parsed the payload (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0022

[Download patch](patches/P-0022-94ff45a95579.patch)

SHA-256: 94ff45a95579a24972a766d301bc9c2888845125bbd04298f474604245854932

### VP-0023: The excessive base64 string verification changes the compatible behavior of the actual Node decoder.

**Requirement**: String ArrayBuffer decoding is not wrapped in new input errors.

**Targeted change**: The excessive base64 string verification changes the compatible behavior of the actual Node decoder. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0023

[Download patch](patches/P-0023-98cb60cfb3c7.patch)

SHA-256: 98cb60cfb3c7670412b2b32dd1ec57e5fd7769816133465b823c48a3d30387d7

### VP-0024: Share the parsed cache across calls.

**Requirement**: Independent calls do not contaminate configurations or caches.

**Targeted change**: Share the parsed cache across calls. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0024

[Download patch](patches/P-0024-99853347b592.patch)

SHA-256: 99853347b592f4096b8d19d711d9442a5c9ece4519388222f35784506819902b

### VP-0025: hydration added a real third-party runtime import and call

**Requirement**: Reconstruction does not add any external dependencies.

**Targeted change**: hydration added a real third-party runtime import and call (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0025

[Download patch](patches/P-0025-99b04134d706.patch)

SHA-256: 99b04134d7060581264ebc1f8a265b7ccad0f31d7162affd3f8e1cc3b47ba313

### VP-0026: The raw custom payload was incorrectly replaced with undefined.

**Requirement**: reviver correctly processes the raw tag payload

**Targeted change**: The raw custom payload was incorrectly replaced with undefined. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0026

[Download patch](patches/P-0026-a5e9495e8e99.patch)

SHA-256: a5e9495e8e990e57f0bd18e849a4e639ff99d83ad8ea9b5fe5fdca6fd17093c0

### VP-0027: Targeted regression: Production modifications are limited to parsing/hydration.

**Requirement**: Production modifications are limited to parsing/hydration.

**Targeted change**: Targeted regression: Production modifications are limited to parsing/hydration. (changed files: src/parse.js, src/stringify.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0027

[Download patch](patches/P-0027-a8f11587b5ec.patch)

SHA-256: a8f11587b5ec5c80f0b7431e629f68971283f2f584f0349fce9dc8621e14a3ec

### VP-0028: JSON syntax error types and messages are unified and packaged.

**Requirement**: JSON syntax errors remain unchanged.

**Targeted change**: JSON syntax error types and messages are unified and packaged. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0028

[Download patch](patches/P-0028-b00e29116061.patch)

SHA-256: b00e29116061323f4746213c253f5affba773dcf07033b4b7c742f48f3fa3e17

### VP-0029: Omitted sparse index verification, incorrect writing of negative attribute

**Requirement**: Sparse filling index maintains numerical and declaration length boundary checking

**Targeted change**: Omitted sparse index verification, incorrect writing of negative attribute (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0029

[Download patch](patches/P-0029-b959b040d455.patch)

SHA-256: b959b040d4555c94458c0c3a6c4e930d56787f6fda39977591f99e0aedc1d1bf

### VP-0030: The view constructor RangeError is uniformly packaged.

**Requirement**: view Constructor Native Error Pass-through

**Targeted change**: The view constructor RangeError is uniformly packaged. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0030

[Download patch](patches/P-0030-bca0276d11cd.patch)

SHA-256: bca0276d11cdd4048f20d14d8ca7d154f91054ab79ae193b84f1d374ff4ee44f

### VP-0031: Only allow the release of illegal empty tables

**Requirement**: unflatten retains the table/sentinel input contract and illegal top-level rejection

**Targeted change**: Only allow the release of valid tables; valid tables and sentinels are kept. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0031

[Download patch](patches/P-0031-bd59e361e7b5.patch)

SHA-256: bd59e361e7b588802d1f94f6ec3a2a11361d89262a0a9d90a0f3d9e9fd3a4ecb

### VP-0032: View illegal buffer index error message drift

**Requirement**: The illegal backing-buffer declaration for the built-in view was rejected.

**Targeted change**: View illegal buffer index error message drift (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0032

[Download patch](patches/P-0032-bd8055438753.patch)

SHA-256: bd80554387532d7e183d4200b67fc4e56aa8ab9644a2b5019e6afc81c0363cc2

### VP-0033: Map creates a new Map by referencing an incorrect value

**Requirement**: Map maintains key-value references and loop identities

**Targeted change**: Map creates a new Map by referencing an incorrect value (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0033

[Download patch](patches/P-0033-bef7c2b3a4fe.patch)

SHA-256: bef7c2b3a4fe72aee82a2cbd9cfe14fbf32e111ca5bd219f9953682ebdc19fcf

### VP-0034: Empty array replaced for ordinary array self-reference error

**Requirement**: Keeping common arrays with shared and circular reference identities

**Targeted change**: Empty array replaced for ordinary array self-reference error (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0034

[Download patch](patches/P-0034-cd9ba1aafb07.patch)

SHA-256: cd9ba1aafb075e9d3026c518e7abb272c45af67a9348a1fa7be1f62237c6cdcb

### VP-0035: Remove custom revivers from each caller of owner and store them in a module-level mutable WeakMap

**Requirement**: Explicitly, each call to owner has five types of hydration states.

**Targeted change**: Remove custom revivers from each caller of owner and store them in a module-level mutable WeakMap (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0035

[Download patch](patches/P-0035-cdf5bdc3dc79.patch)

SHA-256: cdf5bdc3dc7969fbd573c190a9f346a8a9616e193329981c1edfb214901b7699

### VP-0036: parse loses the second parameter, but the third parameter operation is still correct.

**Requirement**: parse retains the string entry and passes it as a parameter to revivers/options.

**Targeted change**: parse loses the second parameter, but the third parameter operation is still correct. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0036

[Download patch](patches/P-0036-dc5ed21a25f4.patch)

SHA-256: dc5ed21a25f41eb88c7eb62dba233de965a4229a848145d98ffe330518acbca3

### VP-0037: The custom loop encountered an error during processing.

**Requirement**: The unresolvable custom loop was rejected by the dedicated error.

**Targeted change**: The custom loop encountered an error during processing. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0037

[Download patch](patches/P-0037-e77cfea3739f.patch)

SHA-256: e77cfea3739f49ab5f4f0f4e49da2113b99b64408e028639f9f48b787b69cc2a

### VP-0038: Unknown tag errors are collectively packaged

**Requirement**: Unknown tag remains as the original error.

**Targeted change**: Unknown tag errors are collectively packaged (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0038

[Download patch](patches/P-0038-eaaf0375c423.patch)

SHA-256: eaaf0375c423262f919fd9e944938cc69fcc01d39c98c3ecf046488aea930bdc

### VP-0039: Six categories of distribution responsibilities are merged into one helper, maintaining sufficient utility helpers to meet the needs of pure counting.

**Requirement**: Separate the six groups of responsibilities into at least six reachable, nonempty routines.

**Targeted change**: Six categories of distribution responsibilities are merged into one helper, maintaining sufficient utility helpers to meet the needs of pure counting. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0039

[Download patch](patches/P-0039-f0c42872c04d.patch)

SHA-256: f0c42872c04d0fa6d3cc1b6906244f6dc9905d9a5789af7a3cc595f4482a0375

### VP-0040: Even adding comments violates the boundaries.

**Requirement**: Existing test files remain frozen

**Targeted change**: Even adding comments violates the boundaries. (changed files: src/parse.js, test/index.test.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0040

[Download patch](patches/P-0040-f3baae70c5f5.patch)

SHA-256: f3baae70c5f5961544b96c0f3cc3e9182e5c215379a965c64e8462a28cb7763a

### VP-0041: Omitted the final sparse review; subsequent reviver modifications have handled bypassing boundaries of the index.

**Requirement**: Reviver cannot bypass the sparse verification when modifying the table.

**Targeted change**: Omitted the final sparse review; subsequent reviver modifications have handled bypassing boundaries of the index. (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0041

[Download patch](patches/P-0041-fdffa2eb40f1.patch)

SHA-256: fdffa2eb40f172b146a6c62fd8d9db6c0a33bd70df2d24383a1cc6f29096ff96

### VP-0042: Create a new Set from Set member errors

**Requirement**: Maintain member references and loop identities

**Targeted change**: Create a new Set from Set member errors (changed files: src/parse.js)

**Entry point and initial state**: Apply this patch to the clean baseline at a3d30d94c8fd, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
