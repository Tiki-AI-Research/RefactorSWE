# Adversarial test patches and verification points

Task: refactor-go-yaml-ast-convert-01

Base commit: edee2f91616c6d73112a13e7c0dbde72ce938877

Scope: partial export. Some items remain unresolved.
This package contains 29 distinct patches and 29 verification points.
The export omits 0 records without a primary patch, including controls and historical revisions. It excludes 1 control or auxiliary items and leaves 4 items unresolved.
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
| [P-0001](patches/P-0001-0d76bc1753a8.patch) | VP-0001 | Traverse only skips string leaves, does not affect parsing |
| [P-0002](patches/P-0002-109aeb558eff.patch) | VP-0002 | The encoding head comment is missing, but the other comments/encodings are normal. |
| [P-0003](patches/P-0003-112a55f28d2b.patch) | VP-0003 | First alias failed to register errors, second alias also failed. |
| [P-0004](patches/P-0004-1831b5a23670.patch) | VP-0004 | If no match is found, return an error. |
| [P-0005](patches/P-0005-19ba4597c3f3.patch) | VP-0005 | List of Parallel Types Restored from Mapping and Array Containers |
| [P-0006](patches/P-0006-273874358b46.patch) | VP-0006 | New list of scalar types added for key conversion |
| [P-0007](patches/P-0007-29ac053f9462.patch) | VP-0007 | Original Formatted First Token Type Table |
| [P-0008](patches/P-0008-2c302f41b2d8.patch) | VP-0008 | Decoding Formatting Callback Receiving Error Scalar Bytes |
| [P-0009](patches/P-0009-348b01ce1cac.patch) | VP-0009 | NodeToValue/DecodeFromNode Added Full Tree Pre-Scanning |
| [P-0010](patches/P-0010-34d71a571939.patch) | VP-0010 | Recursive replacement does not change any targets |
| [P-0011](patches/P-0011-369bbbbcfe68.patch) | VP-0011 | Change the packaging key to the entire rendering text |
| [P-0012](patches/P-0012-406df0c07b09.patch) | VP-0012 | Error in packaging null into the array target. |
| [P-0013](patches/P-0013-4bc2c0f86ba2.patch) | VP-0013 | Format the output, but restore the baseline type switch. |
| [P-0014](patches/P-0014-647554ea07a2.patch) | VP-0014 | Walk adds a full tree pre-scan that does not change the user visitor output. |
| [P-0015](patches/P-0015-655ba37d9285.patch) | VP-0015 | The tag packaging mapping was rejected. |
| [P-0016](patches/P-0016-6d62b10b16fb.patch) | VP-0016 | The wrapper key is replaced at the wrong position. |
| [P-0017](patches/P-0017-815f0051337e.patch) | VP-0017 | Reverse the order of recursive matching |
| [P-0018](patches/P-0018-843ad063d585.patch) | VP-0018 | Only merge sequence branch error rejection |
| [P-0019](patches/P-0019-9713b407be86.patch) | VP-0019 | Targeted regression: Parent returns the same parent object or nil. |
| [P-0020](patches/P-0020-c2a2a7b947cd.patch) | VP-0020 | Reverse the output of Filter |
| [P-0021](patches/P-0021-c6d31c381127.patch) | VP-0021 | Integer solution decoding error, but other basic capabilities are correct. |
| [P-0022](patches/P-0022-cb78d094869e.patch) | VP-0022 | The tag packaging sequence was rejected. |
| [P-0023](patches/P-0023-cc53bbf481d6.patch) | VP-0023 | Restore the complete parallel class list in Walk |
| [P-0024](patches/P-0024-ce4f9c2b86ab.patch) | VP-0024 | Recursive filtering: no matches found, changed from empty to error |
| [P-0025](patches/P-0025-cf8c0508017e.patch) | VP-0025 | Error messages for unresolvable aliases/type changes |
| [P-0026](patches/P-0026-dd7872f3f663.patch) | VP-0026 | Non-redundant binding of anchor with the same name |
| [P-0027](patches/P-0027-de433717fa91.patch) | VP-0027 | File.String Output Prefix Added |
| [P-0028](patches/P-0028-e14cf7f87d32.patch) | VP-0028 | The depth threshold is advanced prematurely, and the sentinel has been replaced by another error. |
| [P-0029](patches/P-0029-e708fcb158f8.patch) | VP-0029 | Please only omit the second and subsequent documents. |

## P-0001

[Download patch](patches/P-0001-0d76bc1753a8.patch)

SHA-256: 0d76bc1753a8651e68c095250d660e6c8b4a9de395211ca31f58bce59012d1c9

### VP-0001: Traverse only skips string leaves, does not affect parsing

**Requirement**: Traverse only skips string leaves, does not affect parsing

**Targeted change**: Traverse only skips string leaves, does not affect parsing (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0002

[Download patch](patches/P-0002-109aeb558eff.patch)

SHA-256: 109aeb558eff4515ab982bff6679580973ffed78c10d8be146f4def044c310a5

### VP-0002: The encoding head comment is missing, but the other comments/encodings are normal.

**Requirement**: The encoding head comment is missing, but the other comments/encodings are normal.

**Targeted change**: The encoding head comment is missing, but the other comments/encodings are normal. (changed files: ast/ast.go, decode.go, encode.go, internal/format/format.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0003

[Download patch](patches/P-0003-112a55f28d2b.patch)

SHA-256: 112a55f28d2bbc7a6ee44dc71d9627f9503aef878e369479705646c1fce871e2

### VP-0003: First alias failed to register errors, second alias also failed.

**Requirement**: Duplicate alias resolution

**Targeted change**: First alias failed to register errors, second alias also failed. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0004

[Download patch](patches/P-0004-1831b5a23670.patch)

SHA-256: 1831b5a236707015af38a0e27f8ab772f83cd47282b6a9d2ed311a9cac346c6d

### VP-0004: If no match is found, return an error.

**Requirement**: Recursive replacement with no matches leaves the input unchanged and introduces no error.

**Targeted change**: If no match is found, return an error. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0005

[Download patch](patches/P-0005-19ba4597c3f3.patch)

SHA-256: 19ba4597c3f37d27cfae33e48110ede5094ea32834db3d4e3fcda4684e45917d

### VP-0005: List of Parallel Types Restored from Mapping and Array Containers

**Requirement**: List of Parallel Types Restored from Mapping and Array Containers

**Targeted change**: List of Parallel Types Restored from Mapping and Array Containers (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0006

[Download patch](patches/P-0006-273874358b46.patch)

SHA-256: 273874358b4612423d430997bda7591ad57e2518010169b4bae9137035efd5b5

### VP-0006: New list of scalar types added for key conversion

**Requirement**: New list of scalar types added for key conversion

**Targeted change**: New list of scalar types added for key conversion (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0007

[Download patch](patches/P-0007-29ac053f9462.patch)

SHA-256: 29ac053f94625788422e0794bb7cc7d0f4d45f031d4b87f8a401bf490cf3ee2b

### VP-0007: Original Formatted First Token Type Table

**Requirement**: The capabilities of the first token are provided by each delivered Node and are used by the token/formatted path.

**Targeted change**: Original Formatted First Token Type Table (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0008

[Download patch](patches/P-0008-2c302f41b2d8.patch)

SHA-256: 2c302f41b2d8bbf8c191a811a3f21bb383f5c4955ce505f81cba010421f13541

### VP-0008: Decoding Formatting Callback Receiving Error Scalar Bytes

**Requirement**: The decoding formatted callback continues to receive the original YAML bytes.

**Targeted change**: Decoding Formatting Callback Receiving Error Scalar Bytes (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0009

[Download patch](patches/P-0009-348b01ce1cac.patch)

SHA-256: 348b01ce1cacdc157db5e01fa404c0ff2742b6529579591c5daba55b10949e45

### VP-0009: NodeToValue/DecodeFromNode Added Full Tree Pre-Scanning

**Requirement**: Decoding capabilities do not increase the total tree pass or result in redundant work.

**Targeted change**: NodeToValue/DecodeFromNode Added Full Tree Pre-Scanning (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0010

[Download patch](patches/P-0010-34d71a571939.patch)

SHA-256: 34d71a571939bdd7f8551971ea4863fe57e2dda65f0f6ed091b625418b07537c

### VP-0010: Recursive replacement does not change any targets

**Requirement**: Recursive path replacement modifies the same position

**Targeted change**: Recursive replacement does not change any targets (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0011

[Download patch](patches/P-0011-369bbbbcfe68.patch)

SHA-256: 369bbbbcfe68e36e10a70eb8a23561515e689fcfa0b3469a86a03a2c9f672408

### VP-0011: Change the packaging key to the entire rendering text

**Requirement**: Wrap Key Extraction Continues with the Same Selection Result

**Targeted change**: Change the packaging key to the entire rendering text (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0012

[Download patch](patches/P-0012-406df0c07b09.patch)

SHA-256: 406df0c07b09f16a5bbe34ddfe9d825792d8e72c2d2d13c4774acaa903429292

### VP-0012: Error in packaging null into the array target.

**Requirement**: Wrap null to maintain the results of existing containers

**Targeted change**: Error in packaging null into the array target. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0013

[Download patch](patches/P-0013-4bc2c0f86ba2.patch)

SHA-256: 4bc2c0f86ba2fd3ab915d82f5563a5a6c3f7c91e311380142aa552b8cda97363

### VP-0013: Format the output, but restore the baseline type switch.

**Requirement**: Each delivered Node supports the visitor's acceptance ability, and the formatting of the types is distributed using common capabilities.

**Targeted change**: Format the output, but restore the baseline type switch. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0014

[Download patch](patches/P-0014-647554ea07a2.patch)

SHA-256: 647554ea07a238df60b5c81b1d964515d98e9a400de93bec8a5260badd1d508d

### VP-0014: Walk adds a full tree pre-scan that does not change the user visitor output.

**Requirement**: Traverse without increasing the total number of passes or doing repetitive work, while maintaining the original linear scale.

**Targeted change**: Walk adds a full tree pre-scan that does not change the user visitor output. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0015

[Download patch](patches/P-0015-655ba37d9285.patch)

SHA-256: 655ba37d9285a9ffddb1339152f95a0158f6a532e1971da215f8af10069f67e7

### VP-0015: The tag packaging mapping was rejected.

**Requirement**: The packaging mapping retains the original success or error results.

**Targeted change**: The tag packaging mapping was rejected. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0016

[Download patch](patches/P-0016-6d62b10b16fb.patch)

SHA-256: 6d62b10b16fb7de5e79d7ca1b27521c4a81199c740372a105f58fc096be86072

### VP-0016: The wrapper key is replaced at the wrong position.

**Requirement**: Packaging key extraction continues with the same replacement locations

**Targeted change**: The wrapper key is replaced at the wrong position. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0017

[Download patch](patches/P-0017-815f0051337e.patch)

SHA-256: 815f0051337e1ab1ed151f02cf93d4c672ae235c3d5449972e5848e3228ee131

### VP-0017: Reverse the order of recursive matching

**Requirement**: Recursive path filtering returns the same values and order

**Targeted change**: Reverse the order of recursive matching (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0018

[Download patch](patches/P-0018-843ad063d585.patch)

SHA-256: 843ad063d5850e3193295af6c5063af0e952cc865fdb93d872453cf3c9f453d6

### VP-0018: Only merge sequence branch error rejection

**Requirement**: merge context allows sequences to be treated as a set of mappings, non-merge context maintains rejection

**Targeted change**: Only merge sequence branch error rejection (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0019

[Download patch](patches/P-0019-9713b407be86.patch)

SHA-256: 9713b407be865a95ea693995631b782a70e6092f47960a736ed9609910f3c1e4

### VP-0019: Targeted regression: Parent returns the same parent object or nil.

**Requirement**: Parent returns the same parent object or nil.

**Targeted change**: Targeted regression: Parent returns the same parent object or nil. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0020

[Download patch](patches/P-0020-c2a2a7b947cd.patch)

SHA-256: c2a2a7b947cda326c72b855e7b92eb59cbb8b7bb8b314dfa983478f1eae73975

### VP-0020: Reverse the output of Filter

**Requirement**: Reverse the output of Filter

**Targeted change**: Reverse the output of Filter (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0021

[Download patch](patches/P-0021-c6d31c381127.patch)

SHA-256: c6d31c381127c8e4bb77a8ff7f23df0086dbcc08a5d9656cf31cf6d15f9e4dbe

### VP-0021: Integer solution decoding error, but other basic capabilities are correct.

**Requirement**: Normal mapping, sequence, scalar, and tag decoding retained values and errors

**Targeted change**: Integer solution decoding error, but other basic capabilities are correct. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0022

[Download patch](patches/P-0022-cb78d094869e.patch)

SHA-256: cb78d094869e5e1d0aaf5e9df2c9d77db4013a5884258d9247bf2548da6fba80

### VP-0022: The tag packaging sequence was rejected.

**Requirement**: The packaging sequence retains the original success or error results.

**Targeted change**: The tag packaging sequence was rejected. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0023

[Download patch](patches/P-0023-cc53bbf481d6.patch)

SHA-256: cc53bbf481d6fdc8961eaca6dbcf46d42d838be1bb6b426730dcedc18ff8463a

### VP-0023: Restore the complete parallel class list in Walk

**Requirement**: The consumer uses this ability

**Targeted change**: Restored complete list of parallel abilities in Walk; other abilities still exist (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0024

[Download patch](patches/P-0024-ce4f9c2b86ab.patch)

SHA-256: ce4f9c2b86ab17083418fcb7d6fad231a4021c125425c44b8c6643535b68aea9

### VP-0024: Recursive filtering: no matches found, changed from empty to error

**Requirement**: Recursive filtering with no matches returns an empty result without introducing an error.

**Targeted change**: Recursive filtering: no matches found, changed from empty to error (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0025

[Download patch](patches/P-0025-cf8c0508017e.patch)

SHA-256: cf8c0508017e2845336f059f7f187c2b39b35a330aa456b4f505a902491d8d81

### VP-0025: Error messages for unresolvable aliases/type changes

**Requirement**: Unresolved aliases remain as errors.

**Targeted change**: Error messages for unresolvable aliases/type changes (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0026

[Download patch](patches/P-0026-dd7872f3f663.patch)

SHA-256: dd7872f3f6638d09dfbde0e9830f276de38fe30945031a9472a73f9bb4abb96a

### VP-0026: Non-redundant binding of anchor with the same name

**Requirement**: Maintain the timing of anchor name registration and re-binding

**Targeted change**: Non-redundant binding of anchor with the same name (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0027

[Download patch](patches/P-0027-de433717fa91.patch)

SHA-256: de433717fa918a505dd7e568e64a8fbacbbf260050cb7674f1e6d17ea6aa1726

### VP-0027: File.String Output Prefix Added

**Requirement**: File.String Output Prefix Added

**Targeted change**: File.String Output Prefix Added (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0028

[Download patch](patches/P-0028-e14cf7f87d32.patch)

SHA-256: e14cf7f87d326d1aa75602bb194c294f6ee74a6203c25065ac9f7d61058174d0

### VP-0028: The depth threshold is advanced prematurely, and the sentinel has been replaced by another error.

**Requirement**: Deep limit exceeded remains the same sentinel

**Targeted change**: The depth threshold is advanced prematurely, and the sentinel has been replaced by another error. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors

## P-0029

[Download patch](patches/P-0029-e708fcb158f8.patch)

SHA-256: e708fcb158f8375137f2cc3df717abce97b87de8b837be66488c9bced84ec049

### VP-0029: Please only omit the second and subsequent documents.

**Requirement**: FilterFile maintains cross-document consistency.

**Targeted change**: Please only omit the second and subsequent documents. (changed files: ast/ast.go, decode.go, internal/format/format.go, parser/parser.go, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at edee2f91616c, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Collection or infrastructure errors
