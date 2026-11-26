# Adversarial test patches and verification points

Task: cknd-stackprinter-20260915033253-107b0e

Base commit: 7a07a51a806e70c273a96071c87d19289bc0c69e

Scope: partial export. Some items remain unresolved.
This package contains 35 distinct patches and 35 verification points.
The export omits 0 records without a primary patch, including controls and historical revisions. It excludes 1 control or auxiliary items and leaves 2 items unresolved.
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
| [P-0001](patches/P-0001-0bfb764b6455.patch) | VP-0001 | The same ValueError instance appears twice in the two branches of ExceptionGroup. |
| [P-0002](patches/P-0002-0ee89bc13e6b.patch) | VP-0002 | The outer group includes the inner group and the second common exception. |
| [P-0003](patches/P-0003-0fd871542bb9.patch) | VP-0003 | Pass the same frame list to format_summary. |
| [P-0004](patches/P-0004-19b6590d3eac.patch) | VP-0004 | Pass the constructed ExceptionNode directly to sp.format, and compare it with the independent renderer by passing style=darkbg. |
| [P-0005](patches/P-0005-1df4c9acf070.patch) | VP-0005 | The group subb calls filter(True/False). The exc_value identity must be cloned anew. False is equivalent to None, and the original parent remains unchanged. |
| [P-0006](patches/P-0006-1f9175eb3b0a.patch) | VP-0006 | Group Subreal-Time secret_value |
| [P-0007](patches/P-0007-2d5183e6a371.patch) | VP-0007 | Inspect the first 8 parameters of the signature and check for no abnormal TB cases, as well as two triple groups: (None,None,None) / (TypeError,None,None) |
| [P-0008](patches/P-0008-2ebe8e5134e9.patch) | VP-0008 | The actual frame, by default outside of except, by default inside of except, exception tuple, current Thread, and illegal 42 |
| [P-0009](patches/P-0009-307dd1263cfc.patch) | VP-0009 | format_exc_info(ValueError,ValueError("entry-message"),None) |
| [P-0010](patches/P-0010-3eb804c7c311.patch) | VP-0010 | Figure n→[ValueError b→KeyError a,TypeError c] |
| [P-0011](patches/P-0011-46536ae8b86b.patch) | VP-0011 | ValueError up is the cause of RuntimeError down, and the compatibility of the positive entry should include the old standard as the direct cause. |
| [P-0012](patches/P-0012-4a0e98226778.patch) | VP-0012 | Figure n→[b→a,c], b/a/c are all normal exceptions. |
| [P-0013](patches/P-0013-5ab58cb41ced.patch) | VP-0013 | show(ValueError("stream")) specifies StringIO, with a default stderr and stderr=None. |
| [P-0014](patches/P-0014-5e51517092c8.patch) | VP-0014 | With two levels of traceback, group root, sub-exceptions, and cause ancestors, suppressed_vars=["secret.*"] |
| [P-0015](patches/P-0015-6189cfa05199.patch) | VP-0015 | RuntimeError downstream is triggered first by context ValueError upstream, and then the cause is switched. |
| [P-0016](patches/P-0016-652c998c5570.patch) | VP-0016 | Read ExceptionNode/build_exception_tree/Trac from stackprinter and stackprinter.formatting respectively. |
| [P-0017](patches/P-0017-753df23e56ec.patch) | VP-0017 | Figure n→[b→a,c], walk(postorder) should be [a,b,c,n] |
| [P-0018](patches/P-0018-763e42359138.patch) | VP-0018 | Pass KeyboardInterrupt, SystemExit, and a BaseExceptionGroup containing KeyboardInterrupt directly in separate cases. |
| [P-0019](patches/P-0019-7b4f684d306e.patch) | VP-0019 | ValueError b causes a KeyError. When filter encounters a ValueError, it clones a and reconnects it to the new b. The original chain remains unchanged. |
| [P-0020](patches/P-0020-7e15713310cb.patch) | VP-0020 | ValueError and TypeError mutually establish __context__ |
| [P-0021](patches/P-0021-8060075b4739.patch) | VP-0021 | Filter group n to its TypeError child c. The retained child's parent must point to the new group, while the original c still points to n. An all-False predicate must prune the empty group. |
| [P-0022](patches/P-0022-822b1e3d44fc.patch) | VP-0022 | Two-layer actual FrameInfo list is passed with format_stack, source_lines=0/show_vals=False |
| [P-0023](patches/P-0023-83f1cd91d1e6.patch) | VP-0023 | Group n→[b→a,c] and assign the root true frame to the group |
| [P-0024](patches/P-0024-8c4cfe34df80.patch) | VP-0024 | Group n has sub-groups b and c, b.__cause__=a, graph n→[b→a,c] |
| [P-0025](patches/P-0025-9158bfdab8e4.patch) | VP-0025 | Exceptions containing cause, plaintext has ANSI but darkbg has ANSI, text remains the same after stripping colors |
| [P-0026](patches/P-0026-9a133098a186.patch) | VP-0026 | Use a real exception frame. Configure the renderer once with style/plaintext, source_lines=3, after=0, signatures and variables disabled, truncation at 7, and wrapping at 2. |
| [P-0027](patches/P-0027-ac91bbb891fc.patch) | VP-0027 | A real two-level ValueError traceback from exc to inner |
| [P-0028](patches/P-0028-be931411dc22.patch) | VP-0028 | Explicitly construct ExceptionNode with is_cycle=True |
| [P-0029](patches/P-0029-cdc13f6ec739.patch) | VP-0029 | For branches with a cause, check each line of the prompt rail and empty rail lines for trailing spaces. |
| [P-0030](patches/P-0030-d3c4f4e65087.patch) | VP-0030 | RuntimeError.__context__=ValueError, then sets the cause of KeyError, then clears the cause and suppresses the context. |
| [P-0031](patches/P-0031-d45c3b3dd1ed.patch) | VP-0031 | The same two levels of real traceback, collect function names according to tb_next. |
| [P-0032](patches/P-0032-dba3c9a6f279.patch) | VP-0032 | Any class name Bundle(Exception) is respectively associated with list/tuple([ValueError,TypeError]), and separately tested for ordinary exceptions and those containing KeyboardInter. |
| [P-0033](patches/P-0033-dfec995fa225.patch) | VP-0033 | Figure n→[b→a,c] expects walk to default to [n,b,a,c] |
| [P-0034](patches/P-0034-fb9e52eaa3ea.patch) | VP-0034 | RuntimeError downstream is an explicit cause of ValueError upstream. The renderer must be used with reverse=True, and it must be done in the order of the current ancestors. |
| [P-0035](patches/P-0035-fc28be4f8916.patch) | VP-0035 | For true common exceptions, first check the summary True/False, then use the frame formatter to generate 51/50 line breaks to verify the original threshold of auto. |

## P-0001

[Download patch](patches/P-0001-0bfb764b6455.patch)

SHA-256: 0bfb764b6455adc7fab4e43e47a84176b511b3cd0bde2a873bea634ea88aab71

### VP-0001: The same ValueError instance appears twice in the two branches of ExceptionGroup.

**Requirement**: Shared instances can be observed in different branches and are not incorrectly marked as cycle.

**Targeted change**: The same ValueError instance appears repeatedly in two branches of ExceptionGroup; both branches retain their identities and is_cycle is False. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0002

[Download patch](patches/P-0002-0ee89bc13e6b.patch)

SHA-256: 0ee89bc13e6bf5aecd8143e78a26a80ffd9959bf0b84541d0e822e03c97330e8

### VP-0002: The outer group includes the inner group and the second common exception.

**Requirement**: The brother branch counts from 1, specify the banner, and each nested level should have 2 spaces.

**Targeted change**: The outer group contains the inner group and the second general exception; it checks from number 1, the second branch 2, the nested 2 spaces indentation, and rail. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0003

[Download patch](patches/P-0003-0fd871542bb9.patch)

SHA-256: 0fd871542bb9f0f8b582735cdbee2bb21d87ec0142c2ca4be411a66f11ad2e3d

### VP-0003: Pass the same frame list to format_summary.

**Requirement**: Compact variable-frame output with preservation of source_lines/reverse semantics; no unauthorized requests for unconfirmed top-level aliases

**Targeted change**: Pass the same frame list to format_summary. The compact output includes the source line containing raise, and reverse=True changes the frame order. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0004

[Download patch](patches/P-0004-19b6590d3eac.patch)

SHA-256: 19b6590d3eac0f8c9e18181135fd7dfbc6769420cb48aad77125d3d5cf1608a2

### VP-0004: Pass the constructed ExceptionNode directly to sp.format, and compare it with the independent renderer by passing style=darkbg.

**Requirement**: format(node,**kwargs) Returns the corresponding IR string and applies the parameters.

**Targeted change**: Pass the constructed ExceptionNode directly to sp.format, and compare it with the independent renderer by passing style=darkbg. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0005

[Download patch](patches/P-0005-1df4c9acf070.patch)

SHA-256: 1df4c9acf0704b115527ec5d8986c1f592655a7eebfce77ffb37f2ac69582416

### VP-0005: The group subb calls filter(True/False). The exc_value identity must be cloned anew. False is equivalent to None, and the original parent remains unchanged.

**Requirement**: The true and false predicates correspond to new objects/None, while the original tree and parent remain unchanged.

**Targeted change**: The group subb calls filter(True/False). The exc_value identity must be cloned anew. False is equivalent to None, and the original parent remains unchanged. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0006

[Download patch](patches/P-0006-1f9175eb3b0a.patch)

SHA-256: 1f9175eb3b0af1202ffc7f393b3dd22a944b2c3ba91616430e657388bb4cca57

### VP-0006: Group Subreal-Time secret_value

**Requirement**: The source code/variables in the sub-items are displayed, line wrapping is truncated, and settings follow the parent renderer.

**Targeted change**: Group sub-real frames with secret_value; show_vals=False/source_lines=0. Assignment should not be displayed/code source. Values should not be disclosed when suppressed_vars are also included. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0007

[Download patch](patches/P-0007-2d5183e6a371.patch)

SHA-256: 2d5183e6a37171f1e63d46a41740ae53bd50b50b976bf08e0787efd973d9b6ce

### VP-0007: Inspect the first 8 parameters of the signature and check for no abnormal TB cases, as well as two triple groups: (None,None,None) / (TypeError,None,None)

**Requirement**: The original parameters/default can be used; standard exceptions and the public None tuple/value output remain the same as the baseline.

**Targeted change**: Inspect the first 8 parameters of the signature and check for no abnormal TB cases, as well as two triple groups: (None,None,None) / (TypeError,None,None) (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0008

[Download patch](patches/P-0008-2ebe8e5134e9.patch)

SHA-256: 2ebe8e5134e91b9e2e23c76abd8d1194b53ed11667ead604c7a110fbf813c97e

### VP-0008: The actual frame, by default outside of except, by default inside of except, exception tuple, current Thread, and illegal 42

**Requirement**: Except for parameters within the `except` block, the exception tuple, and frame/thread, the corresponding content is still returned. The original type error path has not changed unexpectedly.

**Targeted change**: The actual frame, by default outside of except, by default inside of except, exception tuple, current Thread, and illegal 42; check the corresponding entry/exception behavior. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0009

[Download patch](patches/P-0009-307dd1263cfc.patch)

SHA-256: 307dd1263cfc3345374fd446c72a968c0d74067a8771fbf4eb94ad9318ca2d27

### VP-0009: format_exc_info(ValueError,ValueError("entry-message"),None)

**Requirement**: TracebackRenderer then serializes the result. Adding names around the original monolithic implementation does not meet the requirement.

**Targeted change**: Call format_exc_info(ValueError,ValueError("entry-message"),None). Only the group route retains the pipeline. Verify in the source that the name is not a valid builder alias. (changed files: stackprinter/__init__.py, stackprinter/formatting.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0010

[Download patch](patches/P-0010-3eb804c7c311.patch)

SHA-256: 3eb804c7c311fc8644aa187a049ddfda556a66dcacc4cb4e50b3b22b2336c955

### VP-0010: Figure n→[ValueError b→KeyError a,TypeError c]

**Requirement**: Figure n→[ValueError b→KeyError a,TypeError c]; find(LookupError)=[a]，find(Exception) remains in order

**Targeted change**: Figure n→[ValueError b→KeyError a,TypeError c]; find(LookupError)=[a]，find(Exception) remains in order (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0011

[Download patch](patches/P-0011-46536ae8b86b.patch)

SHA-256: 46536ae8b86b1763f1896fd7a4446118c9335b38584669fc78b59b538df7a847

### VP-0011: ValueError up is the cause of RuntimeError down, and the compatibility of the positive entry should include the old standard as the direct cause.

**Requirement**: Regular causal text remains consistent with the baseline; the order with reverse=True must be reported alongside the baseline and new renderer terms. Disputes not resolved shall not be resolved unilaterally.

**Targeted change**: ValueError up is the cause of RuntimeError down. The compatibility of the forward entry should include the old standard as the direct cause. Reverse conflicts are only disclosed without strong judgment. The additional signature changes of the wrapper are not used to prove this goal. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0012

[Download patch](patches/P-0012-4a0e98226778.patch)

SHA-256: 4a0e982267786c0ccd303c3fbaa862210b67dc7fd354e141844e153fa7bccf5f

### VP-0012: Figure n→[b→a,c], b/a/c are all normal exceptions.

**Requirement**: The list is not a group, and sub_exceptions is empty.

**Targeted change**: Figure n→[b,a,c], both b/a/c are normal exceptions; leaves must be [b,a,c] (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0013

[Download patch](patches/P-0013-5ab58cb41ced.patch)

SHA-256: 5ab58cb41ced43071c70d87ebf218b8b0ec8277c37df1971a15b938c16bd43a5

### VP-0013: show(ValueError("stream")) specifies StringIO, with a default stderr and stderr=None.

**Requirement**: The format of the specified stream output is retained, with the default semantics of stderr and silent behavior when it does not exist.

**Targeted change**: show(ValueError("stream")) Specifies StringIO, with a default stderr and stderr=None; checks for writing to the stream and handling of missing streams. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0014

[Download patch](patches/P-0014-5e51517092c8.patch)

SHA-256: 5e51517092c83aacbd4427adc747e09d33c0f25f3f696eba58d4261d2f832384

### VP-0014: With two levels of traceback, group root, sub-exceptions, and cause ancestors, suppressed_vars=["secret.*"]

**Requirement**: The get_info of the root, causal ancestor, and group sub-items receives the masking settings, and the matching variables maintain the masking access semantics as before the review.

**Targeted change**: Group root with two levels of traceback, sub-exceptions and cause ancestors, suppressed_vars=["secret.*"]; spy recorded at least 6 occurrences of get_info with consistent parameters each time. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0015

[Download patch](patches/P-0015-6189cfa05199.patch)

SHA-256: 6189cfa05199546479a9bbe49d372b52ebd00a134eb477d84e4a6c2471fdcb5e

### VP-0015: RuntimeError downstream is triggered first by context ValueError upstream, and then the cause is switched.

**Requirement**: Use correct prompts for cause/context and connect the corresponding exception sections.

**Targeted change**: RuntimeError downstream is triggered first by context ValueError upstream, and then the cause is switched. Check the corresponding standard prompts, no error cause prompt, and the order before and after. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0016

[Download patch](patches/P-0016-652c998c5570.patch)

SHA-256: 652c998c5570e3939eb4962cb17a3fcd48a3dc7be888c29db4fe922a8c8267f9

### VP-0016: Read ExceptionNode/build_exception_tree/Trac from stackprinter and stackprinter.formatting respectively.

**Requirement**: ExceptionNode, build_exception_tree, TracebackRenderer are all available public objects.

**Targeted change**: Read ExceptionNode/build_exception_tree/TracebackRenderer from both stackprinter and stackprinter.formatting and check the callable functions. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0017

[Download patch](patches/P-0017-753df23e56ec.patch)

SHA-256: 753df23e56ec747425a08e635358a5ae8cd1e961e8f44af56c8fce1f314f3ee5

### VP-0017: Figure n→[b→a,c], walk(postorder) should be [a,b,c,n]

**Requirement**: posterior results of chain_parent, sub_exceptions, and node

**Targeted change**: Figure n→[b→a,c], walk(postorder) should be [a,b,c,n] (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0018

[Download patch](patches/P-0018-763e42359138.patch)

SHA-256: 763e423591383db9189e73c1d59cb42b5c96a559d633c758065d0af59374d897

### VP-0018: Pass KeyboardInterrupt, SystemExit, and a BaseExceptionGroup containing KeyboardInterrupt directly in separate cases.

**Requirement**: Dispatch KeyboardInterrupt, SystemExit, and BaseExceptionGroup through the new pipeline without raising ValueError because of their types.

**Targeted change**: Pass KeyboardInterrupt, SystemExit, and a BaseExceptionGroup containing KeyboardInterrupt directly in separate cases. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0019

[Download patch](patches/P-0019-7b4f684d306e.patch)

SHA-256: 7b4f684d306e7b19d836e047798a31bb566aacca1bb55425b6d35fefb4815ff1

### VP-0019: ValueError b causes a KeyError. When filter encounters a ValueError, it clones a and reconnects it to the new b. The original chain remains unchanged.

**Requirement**: chain_parent is recursively filtered, the source tree remains unchanged; no additional requirements are added for undeclared ancestor promotion rules.

**Targeted change**: ValueError b causes a KeyError. When filter encounters a ValueError, it clones a and reconnects it to the new b. The original chain remains unchanged. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0020

[Download patch](patches/P-0020-7e15713310cb.patch)

SHA-256: 7e15713310cbdaf0e69ebfbe4c0c30535d759dcd59e75601018dade7fa02eba2

### VP-0020: ValueError and TypeError mutually establish __context__

**Requirement**: The construction of the two abnormal context loops has terminated; no further expansion is necessary.

**Targeted change**: Set the ValueError and TypeError as each other's __context__. On the second visit, check is_cycle and stop expanding the chain. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0021

[Download patch](patches/P-0021-8060075b4739.patch)

SHA-256: 8060075b4739e195181bbe3ad121ffd1ff88d48679f6f0705c90d18ab82cbe30

### VP-0021: Filter group n to its TypeError child c. The retained child's parent must point to the new group, while the original c still points to n. An all-False predicate must prune the empty group.

**Requirement**: If neither the group nor its subgroups match, return None.

**Targeted change**: Filter group n to its TypeError child c. The retained child's parent must point to the new group, while the original c still points to n. An all-False predicate must prune the empty group. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0022

[Download patch](patches/P-0022-822b1e3d44fc.patch)

SHA-256: 822b1e3d44fc667b2530ce61defa5d5b40d7751891ab3715c0f3fb0abb234864

### VP-0022: Two-layer actual FrameInfo list is passed with format_stack, source_lines=0/show_vals=False

**Requirement**: Frame sequences, existing configurations, and reverse are still formatted according to the baseline; do not request unconfirmed top-level aliases without permission.

**Targeted change**: Two-layer actual FrameInfo list, pass format_stack, source_lines=0/show_vals=False; reverse=True. The inner should be before exc. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0023

[Download patch](patches/P-0023-83f1cd91d1e6.patch)

SHA-256: 83f1cd91d1e661b006f47dc64aa72f8ef4e8cafb4aba10a640d81bc88dfb9c96

### VP-0023: Group n→[b→a,c] and assign the root true frame to the group

**Requirement**: Group head and traceback exist, followed by an ordered branch

**Targeted change**: Group n→[b→a,c] and assign the root frame to the group; check if the root frame is visible, and ensure that the own message is before all sub-items while maintaining the sub-order. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0024

[Download patch](patches/P-0024-8c4cfe34df80.patch)

SHA-256: 8c4cfe34df8058fe5d588ac46c95c7276d3ce8fb9db44e87d89f70983d403d17

### VP-0024: Group n has sub-groups b and c, b.__cause__=a, graph n→[b→a,c]

**Requirement**: Both the sub-items and the causal ancestors are 1 deeper than the parent.

**Targeted change**: Group n has sub-groups b and c, b.__cause__=a, graph n→[b→a,c]; check that n, b, a, c.depth are 0, 1, 2, 1. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0025

[Download patch](patches/P-0025-9158bfdab8e4.patch)

SHA-256: 9158bfdab8e4a4daa570bf187e91fcc57b29853e2763aaf4acdaded2789f31ac

### VP-0025: Exceptions containing cause, plaintext has ANSI but darkbg has ANSI, text remains the same after stripping colors

**Requirement**: Plaintext and existing color schemes follow the original rules for frames/errors/alerts.

**Targeted change**: Exceptions containing cause, plaintext has ANSI but darkbg has ANSI, text remains the same after stripping colors (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0026

[Download patch](patches/P-0026-9a133098a186.patch)

SHA-256: 9a133098a186505751eb7fb20bb270e3147a8befc5029b3cad822c222f800b33

### VP-0026: Use a real exception frame. Configure the renderer once with style/plaintext, source_lines=3, after=0, signatures and variables disabled, truncation at 7, and wrapping at 2.

**Requirement**: List of available parameters, effective when rendered, resulting in a complete string; including renderer's source_lines_after

**Targeted change**: Use a real exception frame. Configure the renderer once with style/plaintext, source_lines=3, after=0, signatures and variables disabled, truncation at 7, wrapping at 25, reverse order, masking, and summary=False. Use a spy to check the actual format_stack arguments. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0027

[Download patch](patches/P-0027-ac91bbb891fc.patch)

SHA-256: ac91bbb891fc3e2b490299a5eb8ab88cb90b1d98e8a1f0cd3e9a8fdc78b54ac8

### VP-0027: A real two-level ValueError traceback from exc to inner

**Requirement**: Return an ExceptionNode whose exc_type, exc_value, and traceback match the inputs, including permitted None values.

**Targeted change**: exc→inner two layers of actual ValueError traceback; check the type/value/tb identity, and also pass in (TypeError, None, None) (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0028

[Download patch](patches/P-0028-be931411dc22.patch)

SHA-256: be931411dc220233fdaf9290de04fded9f24069bd2e9a3e4c09d67ff895ead97

### VP-0028: Explicitly construct ExceptionNode with is_cycle=True

**Requirement**: No specific wording is required.

**Targeted change**: Explicitly construct an ExceptionNode with is_cycle=True; the output must have the semantics of cycle/recursion/loop. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0029

[Download patch](patches/P-0029-cdc13f6ec739.patch)

SHA-256: cdc13f6ec7390c23e4a684afe1b9d6a19e6010f403fd453d302c3bab9cd28388

### VP-0029: For branches with a cause, check each line of the prompt rail and empty rail lines for trailing spaces.

**Requirement**: Within the group, frames, causal prompts, and nested sublines all have the correct vertical line hierarchy. There are no blanks after the rail.

**Targeted change**: For branches with a cause, check each line of the prompt rail and empty rail lines for trailing spaces. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0030

[Download patch](patches/P-0030-d3c4f4e65087.patch)

SHA-256: d3c4f4e6508775ccf4aa88bab4fc4fcbe992bad437ed51d08f62ccba66140bfc

### VP-0030: RuntimeError.__context__=ValueError, then sets the cause of KeyError, then clears the cause and suppresses the context.

**Requirement**: Cause takes precedence, suppress takes effect, chain_parent refers to the ancestor; the storage direction of chain_type remains ambiguous and is not used as a unique label assertion.

**Targeted change**: RuntimeError.__context__=ValueError, then sets the cause of KeyError, then clears the cause and suppresses the context; checks the ancestor value, reverse parent, priority, and suppression (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0031

[Download patch](patches/P-0031-d45c3b3dd1ed.patch)

SHA-256: d45c3b3dd1ed6709cdb3fa3eb666af91566f878dbd520b3906b61476ee9a27b3

### VP-0031: The same two levels of real traceback, collect function names according to tb_next.

**Requirement**: Frames is an ordered list of FrameInfo. When tb=None, it is []

**Targeted change**: Use the same real two-frame traceback, collect function names via tb_next, and compare them with FrameInfo.function. Also test tb=None. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0032

[Download patch](patches/P-0032-dba3c9a6f279.patch)

SHA-256: dba3c9a6f27970ae4634c07bf77ff9c8df347a7ce7e466b8a4fc86dfd337a2dc

### VP-0032: Any class name Bundle(Exception) is respectively associated with list/tuple([ValueError,TypeError]), and separately tested for ordinary exceptions and those containing KeyboardInter.

**Requirement**: BaseExceptionGroup/Valid exceptions sequence is marked as a group; sub-items correspond to the original sequence, parent refers to the group, and chain_type=group_sub. Normal exceptions sub_exceptions=[]

**Targeted change**: Give an arbitrarily named Bundle(Exception) a list and then a tuple containing ValueError and TypeError. Also test an ordinary exception and a BaseExceptionGroup containing KeyboardInterrupt. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0033

[Download patch](patches/P-0033-dfec995fa225.patch)

SHA-256: dfec995fa225adc67076614454004efbf9fa97a1ffd515c511ef4990e5b287ca

### VP-0033: Figure n→[b→a,c] expects walk to default to [n,b,a,c]

**Requirement**: Preorder results of node, chain_parent, sub_exceptions; finite tree traversal due to loop truncation

**Targeted change**: Figure n→[b→a,c] expects walk to default to [n,b,a,c] (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0034

[Download patch](patches/P-0034-fb9e52eaa3ea.patch)

SHA-256: fb9e52eaa3ea2193eefd3d6ea108f49528a38f4b232504b1aa415f68e005ce16

### VP-0034: RuntimeError downstream is an explicit cause of ValueError upstream. The renderer must be used with reverse=True, and it must be done in the order of the current ancestors.

**Requirement**: The independent renderer outputs the current exception followed by the ancestor; the scope controversy for compatible entrances is retained, and this assertion is not used to replace C045.

**Targeted change**: RuntimeError downstream is an explicit cause of ValueError upstream. The renderer must be used with reverse=True, and it must be done in the order of the current ancestors. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0035

[Download patch](patches/P-0035-fc28be4f8916.patch)

SHA-256: fc28be4f8916780077d58869d1a5178f0079a4bc8c024e6478ad473ae52a3fce

### VP-0035: For true common exceptions, first check the summary True/False, then use the frame formatter to generate 51/50 line breaks to verify the original threshold of auto.

**Requirement**: Compatible entry auto has more than 50 conditions; the precise summary layout of the unspecified group is not considered as the only assertion.

**Targeted change**: For true common exceptions, first check the summary True/False, then use the frame formatter to generate 51/50 line breaks to verify the original threshold of auto. (changed files: stackprinter/formatting.py, stackprinter/__init__.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
