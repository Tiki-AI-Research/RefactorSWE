# Adversarial test patches and verification points

Task: meodai-poline-20260917083155-1c6887

Base commit: c0bf44b06d549eb7bd5ecc1ac84cd3c58eb296cc

Scope: partial export. Some items remain unresolved.
This package contains 55 distinct patches and 59 verification points.
The export omits 0 records without a primary patch, including controls and historical revisions. It excludes 1 control or auxiliary items and leaves 9 items unresolved.
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
| [P-0001](patches/P-0001-018ddefd06da.patch) | VP-0001, VP-0002 | Restoring the baseline monolithic facade, keeping the idle contributor files does not constitute a substantial separation of responsibilities. Restoring the baseline monolithic facade, keeping the idle contributor files does not constitute a substantial separation of responsibilities. |
| [P-0002](patches/P-0002-0e3a3cff8a64.patch) | VP-0003 | Cancel the existing gesture for incorrect external points |
| [P-0003](patches/P-0003-11f3bf6bcc83.patch) | VP-0004 | Listener setter error: cancels the notification gesture. |
| [P-0004](patches/P-0004-152756cb9278.patch) | VP-0005, VP-0006 | Cloning attaches palette destroys reference semantics; Cloning the shared palette causes another picker to no longer retain the same reference. |
| [P-0005](patches/P-0005-15f033164b44.patch) | VP-0007 | Cancel the omission of the synchronization listener setPoline and bypass the reintegration refresh protection. |
| [P-0006](patches/P-0006-19fff4c7dc17.patch) | VP-0008 | Owner canceled the notification cleanup. |
| [P-0007](patches/P-0007-1aa80c140e39.patch) | VP-0009 | No palette returned, returning undefined instead of null. |
| [P-0008](patches/P-0008-23d1499255fa.patch) | VP-0010, VP-0011 | Disconnected Coordination Unretired Interaction Binding; Unlinked activities continue due to disconnection |
| [P-0009](patches/P-0009-29e498c90fee.patch) | VP-0012 | Skip shadow lightness gradient synchronization during attachment |
| [P-0010](patches/P-0010-2b5bc797befb.patch) | VP-0013 | Normal updateSVG error cancellation gesture |
| [P-0011](patches/P-0011-322d0f93d92d.patch) | VP-0014 | Anchor drag not captured initiated pointer |
| [P-0012](patches/P-0012-3524291e8a3b.patch) | VP-0015 | Anchor dragging changes saturation. |
| [P-0013](patches/P-0013-45af7dddc62e.patch) | VP-0016 | The coarse pointer saturation control is still displayed. |
| [P-0014](patches/P-0014-48ad717c4bf5.patch) | VP-0017 | The saturation arc does not update with current data. |
| [P-0015](patches/P-0015-4d78f9a14bc4.patch) | VP-0018 | Owner capture lost and not cleaned up |
| [P-0016](patches/P-0016-4f0d3d0fc53c.patch) | VP-0019 | Reverse Turnover Sample Order |
| [P-0017](patches/P-0017-4fc8822bb38c.patch) | VP-0020 | Configuration call generates no data change notification |
| [P-0018](patches/P-0018-509ea364056e.patch) | VP-0021 | The hit ring still lacks hover feedback. |
| [P-0019](patches/P-0019-519dd5c251aa.patch) | VP-0022 | Effective Dragging Lacks Change Notifications |
| [P-0020](patches/P-0020-60235365ad2e.patch) | VP-0023 | Listener updateSVG does not cancel gestures. |
| [P-0021](patches/P-0021-67b029fe926a.patch) | VP-0024 | Rotary startup does not show adjustment during transient state |
| [P-0022](patches/P-0022-6816c5e972d9.patch) | VP-0025 | Other pointers end/cancel/catch notification error ends current gesture |
| [P-0023](patches/P-0023-6aec16d46457.patch) | VP-0026 | Effective rotary lacks change notification. |
| [P-0024](patches/P-0024-7105c155f957.patch) | VP-0027 | After leaving the blank space, it is not possible to continue dragging new anchor points. |
| [P-0025](patches/P-0025-7d61c2019dbe.patch) | VP-0028 | Ignore interactive. |
| [P-0026](patches/P-0026-834a7db10980.patch) | VP-0029 | owner ends normally without releasing capture |
| [P-0027](patches/P-0027-8780fe17ff2e.patch) | VP-0030 | Still changing the presentation when disconnected |
| [P-0028](patches/P-0028-88dbcb2e6459.patch) | VP-0031 | Simplified Version with Excess Dots Removed |
| [P-0029](patches/P-0029-8a0fdab6c75a.patch) | VP-0032 | Even without a palette, you can still capture and obtain the owner. |
| [P-0030](patches/P-0030-8cc9a25a738f.patch) | VP-0033 | Cumulative exceeding the boundary causes reverse dead zone |
| [P-0031](patches/P-0031-8eee33487b1b.patch) | VP-0034 | Anchor radius error |
| [P-0032](patches/P-0032-930aa99473ac.patch) | VP-0035 | Reconnection not re-adopted Boolean attributes |
| [P-0033](patches/P-0033-9597fb02fff3.patch) | VP-0036 | Refresh does not update the reversed gradient. |
| [P-0034](patches/P-0034-9b7f15704733.patch) | VP-0037 | The program lacks synchronization notifications for certain operations. |
| [P-0035](patches/P-0035-9b9ccb55aab6.patch) | VP-0038 | rotary did not capture the initiating pointer |
| [P-0036](patches/P-0036-a0d6bf47cafd.patch) | VP-0039 | Targeted change: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcom |
| [P-0037](patches/P-0037-aaa5b03061e6.patch) | VP-0040 | Listener Dot Point Bypass Synchronous Reentry Cancel |
| [P-0038](patches/P-0038-ac78e62a2ef2.patch) | VP-0041 | The setter cannot dynamically close blank spaces. |
| [P-0039](patches/P-0039-aeddca940eb7.patch) | VP-0042 | Each connection requires additional installation of unmanaged interaction owners, and input repetition is effective. |
| [P-0040](patches/P-0040-b1e407b158a5.patch) | VP-0043 | Violate content box coordinate normalization |
| [P-0041](patches/P-0041-b47959c309a1.patch) | VP-0044 | Normal setter error cancels active gesture |
| [P-0042](patches/P-0042-ba442577be8a.patch) | VP-0045 | Secondary pointer preempts the current gesture |
| [P-0043](patches/P-0043-c1c61896949f.patch) | VP-0046 | Uncanceled current gesture for normal setPoline |
| [P-0044](patches/P-0044-c3fb709b65e3.patch) | VP-0047 | After adding a shared data anchor point, my updateSVG function fails to refresh properly. |
| [P-0045](patches/P-0045-c990865603c2.patch) | VP-0048 | Ignored Shift toggle in gestures |
| [P-0046](patches/P-0046-cbf535066355.patch) | VP-0049 | Lost saturation component of sample radius |
| [P-0047](patches/P-0047-cf4266da0320.patch) | VP-0050 | Attach without refreshing for a complete presentation |
| [P-0048](patches/P-0048-d9dfd59144f6.patch) | VP-0051 | Change Event Error Bubbling |
| [P-0049](patches/P-0049-db88ef117737.patch) | VP-0052 | Shift gain is used incorrectly for a week |
| [P-0050](patches/P-0050-e284e2391747.patch) | VP-0053 | The coarse pointer error enters the rotary instead of the anchor point drag. |
| [P-0051](patches/P-0051-e2e894bf7e51.patch) | VP-0054 | Discontinuous when wrapping at a rotary angle |
| [P-0052](patches/P-0052-e88b628a751f.patch) | VP-0055 | The interactive pointerdown branches are not stopped from propagating. |
| [P-0053](patches/P-0053-e88cc2b32c02.patch) | VP-0056 | The shared instance list causes the adjustment of one picker to contaminate other pickers in the transient state. |
| [P-0054](patches/P-0054-f1429369cfd0.patch) | VP-0057 | Add some returns to the correct objects, but the DOM is not synchronized. |
| [P-0055](patches/P-0055-fdc715ad0123.patch) | VP-0058, VP-0059 | Retired binding lost source and intergenerational check, can interfere with the current gesture with the same ID; Retired binding lost source and intergenerational check, can interfere with the current gesture with the same ID |

## P-0001

[Download patch](patches/P-0001-018ddefd06da.patch)

SHA-256: 018ddefd06da7fd3a6d2a3970fe6ccab890e5c5a4bc97a2121d2c83c9ecc1097

### VP-0001: Restoring the baseline monolithic facade, keeping the idle contributor files does not constitute a substantial separation of responsibilities.

**Requirement**: The presenter has actual control over SVG construction, visual synchronization, styles, and their states.

**Targeted change**: Restoring the baseline monolithic facade, keeping the idle contributor files does not constitute a substantial separation of responsibilities. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The implementation of facade is not fully preserved, and the acceptance does not follow grammar or file name rules.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

### VP-0002: Restoring the baseline monolithic facade, keeping the idle contributor files does not constitute a substantial separation of responsibilities.

**Requirement**: The actual state of the interaction collaborator, including hits, inputs, gestures, and movement/rotation.

**Targeted change**: Restoring the baseline monolithic facade, keeping the idle contributor files does not constitute a substantial separation of responsibilities. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The facade does not retain the complete interaction process.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0002

[Download patch](patches/P-0002-0e3a3cff8a64.patch)

SHA-256: 0e3a3cff8a64f24b85035b2c97658e6d91900a4dfff23238a677bc309f8d38c2

### VP-0003: Cancel the existing gesture for incorrect external points

**Requirement**: An ordinary external point addition preserves the existing drag or rotary interaction.

**Targeted change**: Cancel the existing gesture for incorrect external points (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The original gesture still retains the capture and transient states, and the subsequent movement continues to update the original target.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0003

[Download patch](patches/P-0003-11f3bf6bcc83.patch)

SHA-256: 11f3bf6bcc83675aa781880850598613afb6554fd8258a55db1e52e392e1367f

### VP-0004: Listener setter error: cancels the notification gesture.

**Requirement**: The "setAllowAddPoints" method within the change listener still retains the gesture for issuing notifications.

**Targeted change**: Listener setter error: cancels the notification gesture. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Capture and transient states are not mistakenly canceled by a general reentrancy protection

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0004

[Download patch](patches/P-0004-152756cb9278.patch)

SHA-256: 152756cb9278df4950d7c498f41bfef259a805775842793f5455d5aa9c4e91fa

### VP-0005: Cloning attaches palette destroys reference semantics

**Requirement**: setPoline retains the palette reference provided by the caller.

**Targeted change**: Cloning attaches palette destroys reference semantics (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not clone or replace the references.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

### VP-0006: Cloning the shared palette causes another picker to no longer retain the same reference.

**Requirement**: Poline retains the original references and shared data but does not automatically update the presentation or notifications for other pickers.

**Targeted change**: Cloning the shared palette causes another picker to no longer retain the same reference. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The DOM, notifications, gestures, captures, and temporary state of the other picker are independent and not cloned or denied to share objects.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0005

[Download patch](patches/P-0005-15f033164b44.patch)

SHA-256: 15f033164b4447abc6cb0a2ceb8acc0996eaa2fd7266eb1af548e0fec0c22b8e

### VP-0007: Cancel the omission of the synchronization listener setPoline and bypass the reintegration refresh protection.

**Requirement**: The gesture that triggers notifications is disabled by setPoline within the change listener, and cannot be revived from the outer layer.

**Targeted change**: Cancel the omission of the synchronization listener setPoline and bypass the reintegration refresh protection. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Subsequent old inputs have no data or have no notification effect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0006

[Download patch](patches/P-0006-19fff4c7dc17.patch)

SHA-256: 19fff4c7dc170f55efd8eb2b860f0f2468fc6bd430448d26c36a7a273a345ba5

### VP-0008: Owner canceled the notification cleanup.

**Requirement**: The owner pointercancel invalidates the gesture and cleans up the resources.

**Targeted change**: Owner canceled the notification cleanup. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Subsequent changes to the old event will not modify the palette, notify anyone, or restore the state.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0007

[Download patch](patches/P-0007-1aa80c140e39.patch)

SHA-256: 1aa80c140e39d2389e51fe58bffe2da3e52d94c6e48330ab30b13ba0df90d4fc

### VP-0009: No palette returned, returning undefined instead of null.

**Requirement**: When there is no palette, the program returns null with some security measures.

**Targeted change**: No palette returned, returning undefined instead of null. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0008

[Download patch](patches/P-0008-23d1499255fa.patch)

SHA-256: 23d1499255fa77da8c72259e764e57db015ba41444ffb9fed20b379d1536c5c8

### VP-0010: Disconnected Coordination Unretired Interaction Binding

**Requirement**: The facade continues to coordinate the public API, palette, and connection/disconnection.

**Targeted change**: Disconnected Coordination Unretired Interaction Binding (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

### VP-0011: Unlinked activities continue due to disconnection

**Requirement**: disconnectedCallback makes the active gesture ineffective.

**Targeted change**: Unlinked activities continue due to disconnection (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Invalid old input. After reconnection, new gestures are available.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0009

[Download patch](patches/P-0009-29e498c90fee.patch)

SHA-256: 29e498c90fee7812f65fb64cccbeabede97601a8be11d1a0c6ad36b83ecc5dd2

### VP-0012: Skip shadow lightness gradient synchronization during attachment

**Requirement**: Synchronize shadow lightness gradient when attaching the palette

**Targeted change**: Skip shadow lightness gradient synchronization during attachment (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0010

[Download patch](patches/P-0010-2b5bc797befb.patch)

SHA-256: 2b5bc797befb5adf039d940269ad3872baa710bd1cbfb45d9c41523bb849c451

### VP-0013: Normal updateSVG error cancellation gesture

**Requirement**: Normal updateSVG retains active gestures.

**Targeted change**: Normal updateSVG error cancellation gesture (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Subsequent movements continue to be updated normally, and the call itself does not notify.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0011

[Download patch](patches/P-0011-322d0f93d92d.patch)

SHA-256: 322d0f93d92d278bcc77a4497307eda8c2fcfddd9c2bbf2d98883c5e8f63fb35

### VP-0014: Anchor drag not captured initiated pointer

**Requirement**: Accepting Anchor Drag Capture Initiation Pointer

**Targeted change**: Anchor drag not captured initiated pointer (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0012

[Download patch](patches/P-0012-3524291e8a3b.patch)

SHA-256: 3524291e8a3b3bebb2161d7996b90e77dd0291cc092b147f6e2dcb32efdc5fa4

### VP-0015: Anchor dragging changes saturation.

**Requirement**: Anchor dragging updates coordinates and derived colors, but does not change saturation.

**Targeted change**: Anchor dragging changes saturation. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: z/color[1] remains the same as before dragging.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0013

[Download patch](patches/P-0013-45af7dddc62e.patch)

SHA-256: 45af7dddc62ecec8f2050dac4d5b4cfeecf0f1eae2665389068701d6e0dc3e36

### VP-0016: The coarse pointer saturation control is still displayed.

**Requirement**: Hide the saturation control for coarse pointers.

**Targeted change**: The coarse pointer saturation control is still displayed. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Should not be revealed due to repainting

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0014

[Download patch](patches/P-0014-48ad717c4bf5.patch)

SHA-256: 48ad717c4bf53c6844e2a270d03920179f0327ba6cf466994f3311de48cc6ccb

### VP-0017: The saturation arc does not update with current data.

**Requirement**: The saturation control updates with the current anchor point and saturation.

**Targeted change**: The saturation arc does not update with current data. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Preserve behavior near zero and for a full circle.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0015

[Download patch](patches/P-0015-4d78f9a14bc4.patch)

SHA-256: 4d78f9a14bc4ac771fe7e79742992e6e447abb8afc37eb49b91f70a68a4292c2

### VP-0018: Owner capture lost and not cleaned up

**Requirement**: The owner lost the capture, causing the gesture to become ineffective and clearing it up.

**Targeted change**: Owner capture lost and not cleaned up (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The old movement is invalid and cannot be re-captured or notified.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0016

[Download patch](patches/P-0016-4f0d3d0fc53c.patch)

SHA-256: 4f0d3d0fc53cded41d626f0ba8e9f65d713ac79f8cead0d5fd5c6a6e9713aa6a

### VP-0019: Reverse Turnover Sample Order

**Requirement**: The complete use of flat samples in the order and projection of the polyline

**Targeted change**: Reverse Turnover Sample Order (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Accept Geometric Equivalency SVG Format

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0017

[Download patch](patches/P-0017-4fc8822bb38c.patch)

SHA-256: 4fc8822bb38c5cd09d05aac2882466945acd99561db4cdd448c745f684b5024b

### VP-0020: Configuration call generates no data change notification

**Requirement**: Activities that do not involve actual data changes remain notified and silent.

**Targeted change**: Configuration call generates no data change notification (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Reentrant configuration must not emit a separate notification or erase the outer change event already in progress. Calling the update function alone does not establish a change.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0018

[Download patch](patches/P-0018-509ea364056e.patch)

SHA-256: 509ea364056e76bf6a6b4f94fd5b4d9af2744a474e5108c4065a8703f37be660

### VP-0021: The hit ring still lacks hover feedback.

**Requirement**: Fine Pointer Ring Hovering for Corresponding Feedback

**Targeted change**: The hit ring still lacks hover feedback. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Host ring-hover and control highlights are correct, with no residue after removal.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0019

[Download patch](patches/P-0019-519dd5c251aa.patch)

SHA-256: 519dd5c251aa0c6906ada85acaaf08f2ce7e549feaa4f3395c4dc32f5a7f5d6e

### VP-0022: Effective Dragging Lacks Change Notifications

**Requirement**: Notification of changes in the current palette for effective anchor point dragging distribution

**Targeted change**: Effective Dragging Lacks Change Notifications (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0020

[Download patch](patches/P-0020-60235365ad2e.patch)

SHA-256: 60235365ad2ea8728b718f5fc38a5168af3488c251b488fc03077262e64a2468

### VP-0023: Listener updateSVG does not cancel gestures.

**Requirement**: Changed the activity gesture for canceling notifications in the updateSVG within the change listener.

**Targeted change**: Listener updateSVG does not cancel gestures. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The old input will no longer be changed or notified.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0021

[Download patch](patches/P-0021-67b029fe926a.patch)

SHA-256: 67b029fe926a5717712e19772322e1b5030693322e6529b82c506d898c6422f1

### VP-0024: Rotary startup does not show adjustment during transient state

**Requirement**: Press the fine pointer ring to start the rotary function and display the adjustment transient state.

**Targeted change**: Rotary startup does not show adjustment during transient state (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: ring-adjusting and corresponding ring presentation are effective.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0022

[Download patch](patches/P-0022-6816c5e972d9.patch)

SHA-256: 6816c5e972d987b39a2c4ecdfcccbf2160de9e3666c62eef2b8ac8440fbf18b5

### VP-0025: Other pointers end/cancel/catch notification error ends current gesture

**Requirement**: End/cancellation/capture notifications for other pointers do not terminate valid gestures

**Targeted change**: Other pointers end/cancel/catch notification error ends current gesture (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The subsequent owner movement is still valid

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0023

[Download patch](patches/P-0023-6aec16d46457.patch)

SHA-256: 6aec16d464572e81ef5ce4270984085d860e437d0d2fdd1ed38bdf064f77d16f

### VP-0026: Effective rotary lacks change notification.

**Requirement**: Effective rotary adjustment distribution change notification for the current palette.

**Targeted change**: Effective rotary lacks change notification. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0024

[Download patch](patches/P-0024-7105c155f957.patch)

SHA-256: 7105c155f957481e9f0b97952ea53d123ce508c6c5ca0881d5399b936446b6ec

### VP-0027: After leaving the blank space, it is not possible to continue dragging new anchor points.

**Requirement**: After adding a point in empty space, the current pointer can continue dragging the new anchor.

**Targeted change**: After leaving the blank space, it is not possible to continue dragging new anchor points. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Stop moving after completion; maintain the baseline main process and comply with the current pointer ownership.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0025

[Download patch](patches/P-0025-7d61c2019dbe.patch)

SHA-256: 7d61c2019dbeb3c43e08a109f3fd591a875d56f88faf8b3c1ba9110808b9c92b

### VP-0028: Ignore interactive.

**Requirement**: In non-interactive connections, no input is processed, and the pointerdown event continues to fire. Reconnection uses the current properties.

**Targeted change**: Unconditional installation and listening through the facade (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: No captures, no changes in data/classes/events; ancestor receives down; properties are sampled based on existence.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0026

[Download patch](patches/P-0026-834a7db10980.patch)

SHA-256: 834a7db10980ede149605fc21e5c55389a873cc77836d45a65c418224ef83418

### VP-0029: owner ends normally without releasing capture

**Requirement**: The owner releases the capture and exits the gesture normally.

**Targeted change**: owner ends normally without releasing capture (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Continue to not change the data of the old move, and new gestures can be established.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0027

[Download patch](patches/P-0027-8780fe17ff2e.patch)

SHA-256: 8780fe17ff2ed16143362ea71a494dc6554553f76024150255114da711ff7e2d

### VP-0030: Still changing the presentation when disconnected

**Requirement**: Unusable updateSVG security null operation in presented state

**Targeted change**: Still changing the presentation when disconnected (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: It is not possible to prove everything with just one state.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0028

[Download patch](patches/P-0028-88dbcb2e6459.patch)

SHA-256: 88dbcb2e6459d37dd38d70591e6333abdf193d307959a343b3234467d9834f3f

### VP-0031: Simplified Version with Excess Dots Removed

**Requirement**: Refresh after palette reduction to remove unnecessary visual elements

**Targeted change**: Simplified Version with Excess Dots Removed (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0029

[Download patch](patches/P-0029-8a0fdab6c75a.patch)

SHA-256: 8a0fdab6c75aed4b262425aca4ac6502b1e489c5ff0a5c3b20d6d486d192bb04

### VP-0032: Even without a palette, you can still capture and obtain the owner.

**Requirement**: Pointer input without a palette does not change the interaction state.

**Targeted change**: Even without a palette, you can still capture and obtain the owner. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Interactive down propagation still follows separate rules

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0030

[Download patch](patches/P-0030-8cc9a25a738f.patch)

SHA-256: 8cc9a25a738f200d5633573e9fa864028612a4aa0446f0b11e174a08a4b111e6

### VP-0033: Cumulative exceeding the boundary causes reverse dead zone

**Requirement**: Saturation boundary immediate response

**Targeted change**: Cumulative exceeding the boundary causes reverse dead zone (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Reverse input causes the saturation to change within the interval

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0031

[Download patch](patches/P-0031-8eee33487b1b.patch)

SHA-256: 8eee33487b1be5318d6c8f86c9a784cbd06adc8d5622ff624a153aa3f7b5804b

### VP-0034: Anchor radius error

**Requirement**: The anchor points retain the semantics of projection, radius, and color.

**Targeted change**: Anchor radius error (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0032

[Download patch](patches/P-0032-930aa99473ac.patch)

SHA-256: 930aa99473acad4e4b28714267c84d0d9f777dc2be92d6ace384dc2824c2eaff

### VP-0035: Reconnection not re-adopted Boolean attributes

**Requirement**: Reconnect and adopt the allow-add-points boolean attribute with some additional strategies.

**Targeted change**: Reconnection not re-adopted Boolean attributes (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The boolean properties containing false text remain enabled.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0033

[Download patch](patches/P-0033-9597fb02fff3.patch)

SHA-256: 9597fb02fff3294821ae190a6698065ec291c920f572e82ec2fb4894737d3963

### VP-0036: Refresh does not update the reversed gradient.

**Requirement**: After an external change to brightness inversion, updateSVG synchronizes the gradient.

**Targeted change**: Refresh does not update the reversed gradient. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The shadow gradient variable corresponds to the current inverted state.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0034

[Download patch](patches/P-0034-9b7f15704733.patch)

SHA-256: 9b7f15704733ba4c2463f1c2e046f46ae699f4d348404d4b56b185f1b05bb749

### VP-0037: The program lacks synchronization notifications for certain operations.

**Requirement**: Add Point Operation Synchronous Distribution: Notification of Changes in New Points

**Targeted change**: The program lacks synchronization notifications for certain operations. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Normal program with additional points, returns before the listener has executed

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0035

[Download patch](patches/P-0035-9b9ccb55aab6.patch)

SHA-256: 9b9ccb55aab6a3acf3b9040b03d7d47b5e7acb310ea22734c165314f2557624b

### VP-0038: rotary did not capture the initiating pointer

**Requirement**: Accepting the detailed pointer rotary capture initiating pointer

**Targeted change**: rotary did not capture the initiating pointer (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0036

[Download patch](patches/P-0036-a0d6bf47cafd.patch)

SHA-256: a0d6bf47cafdc2677fe428f9140302d70e2b0a011e6ddca89b1a07d38e76bedf

### VP-0039: Targeted change: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcom

**Requirement**: Preserve existing behavior in the files changed by the patch (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Targeted change**: Targeted changes to src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The old generation binding has no side effects; it does not require the generation property to be public.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0037

[Download patch](patches/P-0037-aaa5b03061e6.patch)

SHA-256: aaa5b03061e61d7cf9871fbb25789145431dd9aef7bada6cfcdf6d680e7687d5

### VP-0040: Listener Dot Point Bypass Synchronous Reentry Cancel

**Requirement**: Change listener with additional points for reentrancy, refresh, cancellation, and notification gesture

**Targeted change**: Listener Dot Point Bypass Synchronous Reentry Cancel (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The outer call must not restore stale state. After one controlled reentry, the old move has no effect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0038

[Download patch](patches/P-0038-ac78e62a2ef2.patch)

SHA-256: ac78e62a2ef23b995affc7836b2f4aa6370d61939ce91afab9744691650c4cb0

### VP-0041: The setter cannot dynamically close blank spaces.

**Requirement**: The blank dot strategy is activated and deactivated immediately by the setter at the current connection.

**Targeted change**: The setter cannot dynamically close blank spaces. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Disabled, no additional changes, no need to reconnect

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0039

[Download patch](patches/P-0039-aeddca940eb7.patch)

SHA-256: aeddca940eb7914d248013b22ecb84c37313e1a45945dc8ab78898aca04e6c66

### VP-0042: Each connection requires additional installation of unmanaged interaction owners, and input repetition is effective.

**Requirement**: Only one current interaction binding is valid after repeated connections.

**Targeted change**: Each connection requires additional installation of unmanaged interaction owners, and input repetition is effective. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: New connections can start, move, and end gestures properly.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0040

[Download patch](patches/P-0040-b1e407b158a5.patch)

SHA-256: b1e407b158a59b82eb992d323a333da12bbcba9e9d85c5b2f1c1b318ffdbf43a

### VP-0043: Violate content box coordinate normalization

**Requirement**: The program uses SVG for certain elements, with local CSS for pixels and respective width and height normalization.

**Targeted change**: Violate content box coordinate normalization (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The out-of-bounds values are not pre-clipped by the picker, and ultimately follow the Poline clipping configuration; no specific value for size backtracking is mandatory according to the requirements.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0041

[Download patch](patches/P-0041-b47959c309a1.patch)

SHA-256: b47959c309a1520cf3cd99ea0aed0f68e8d6c65e3dac747ad6f84e1326e4c9f6

### VP-0044: Normal setter error cancels active gesture

**Requirement**: Retain the normal setAllowAddPoints to keep the active gesture.

**Targeted change**: Normal setter error cancels active gesture (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The subsequent owner movement continues to be effective and can be completed normally; the call itself has no events.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0042

[Download patch](patches/P-0042-ba442577be8a.patch)

SHA-256: ba442577be8a857f781ac95b19543b04648cf692efec56d3c40388fec8db985f

### VP-0045: Secondary pointer preempts the current gesture

**Requirement**: Secondary pointers cannot override or update the current gesture.

**Targeted change**: Secondary pointer preempts the current gesture (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Secondary pointers do not capture, do not update the palette

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0043

[Download patch](patches/P-0043-c1c61896949f.patch)

SHA-256: c1c61896949f98d30eeba89d6d49f57f01d800e237292f5d26799b5754712d59

### VP-0046: Uncanceled current gesture for normal setPoline

**Requirement**: The regular setPoline deactivates the active gesture whether it is with an existing object or a new object.

**Targeted change**: Uncanceled current gesture for normal setPoline (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The old palette cannot be changed anymore, and no notifications will be sent. New gestures can then be enabled.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0044

[Download patch](patches/P-0044-c3fb709b65e3.patch)

SHA-256: c3fb709b65e3a6efedb6e325278a030e6090a7bd85dbf4a54a530b786e0676ca

### VP-0047: After adding a shared data anchor point, my updateSVG function fails to refresh properly.

**Requirement**: Another picker in the shared palette reflects the shared changes after its own refresh.

**Targeted change**: After adding a shared data anchor point, my updateSVG function fails to refresh properly. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Refreshing itself does not trigger a poline-change, and does not use it to share the interaction state.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0045

[Download patch](patches/P-0045-c990865603c2.patch)

SHA-256: c990865603c25df1092fe89c6f001632013b89bc9a17b463d7969ae4de9f03c8

### VP-0048: Ignored Shift toggle in gestures

**Requirement**: Changing Shift in gestures only affects the sensitivity of subsequent angle movements.

**Targeted change**: Ignored Shift toggle in gestures (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The subsequent movement will not reverse, and the increment will adopt a new sensitivity.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0046

[Download patch](patches/P-0046-cbf535066355.patch)

SHA-256: cbf5350663558c011cf73adc8c565c3f9bf42510ee8cd735948c7beb2ae8be36

### VP-0049: Lost saturation component of sample radius

**Requirement**: The sampling points retain the projection, radius, and HSL color semantics.

**Targeted change**: Lost saturation component of sample radius (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0047

[Download patch](patches/P-0047-cf4266da0320.patch)

SHA-256: cf4266da0320e4974439d83a9ffb23d94eb87968b48bf18609a7df944ae3732b

### VP-0050: Attach without refreshing for a complete presentation

**Requirement**: setPoline immediately refreshes the complete presentation of the attached palette during the connection.

**Targeted change**: Attach without refreshing for a complete presentation (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The line segments, anchor points, samples, and rings correspond to the new data.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0048

[Download patch](patches/P-0048-d9dfd59144f6.patch)

SHA-256: d9dfd59144f6d964cc308dd364f8095f8c4f107f0881968aed5a4681ad07a9f3

### VP-0051: Change Event Error Bubbling

**Requirement**: Synchronize and maintain the type, detail, and flag of change events

**Targeted change**: Change Event Error Bubbling (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: CustomEvent.detail.poline is the current object, and bubbles/cancelable/composed are all false.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0049

[Download patch](patches/P-0049-db88ef117737.patch)

SHA-256: db88ef117737081461bbadd188aacc239c0bd3b96212f4e05918a3261eaaac9b

### VP-0052: Shift gain is used incorrectly for a week

**Requirement**: Normal adjustment and Shift adjustment adopt ranges of 1 week and 2.5 weeks respectively.

**Targeted change**: Shift gain is used incorrectly for a week (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Shift is 1/2.5.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0050

[Download patch](patches/P-0050-e284e2391747.patch)

SHA-256: e284e2391747b6efdee052ea2aa1c3b9976057dc75b03efa2e27bf4ae4090bc1

### VP-0053: The coarse pointer error enters the rotary instead of the anchor point drag.

**Requirement**: Using a coarse pointer to drag an anchor without initiating the rotary function

**Targeted change**: The coarse pointer error enters the rotary instead of the anchor point drag. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Saturation is not adjusted according to rotary input, no rotary transient state.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0051

[Download patch](patches/P-0051-e2e894bf7e51.patch)

SHA-256: e2e894bf7e519e6e32ba81fd2c178621f22afdc8112911e9498ae8837c4f8da4

### VP-0054: Discontinuous when wrapping at a rotary angle

**Requirement**: Rotational crossing angle wrapping boundary maintaining continuity

**Targeted change**: Discontinuous when wrapping at a rotary angle (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: No near-integer jump

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0052

[Download patch](patches/P-0052-e88b628a751f.patch)

SHA-256: e88b628a751f53641365eadba50b66921e927d2b6cc4367769bd455c8560ebfd

### VP-0055: The interactive pointerdown branches are not stopped from propagating.

**Requirement**: The pointerdown on the interactive surface indicates that all branches have stopped propagating.

**Targeted change**: The interactive pointerdown branches are not stopped from propagating. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Ancestors don't receive these downs

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0053

[Download patch](patches/P-0053-e88cc2b32c02.patch)

SHA-256: e88cc2b32c02082036130e47d1dde4c35a2deb42da6e1e171b40b31a4b95ecc7

### VP-0056: The shared instance list causes the adjustment of one picker to contaminate other pickers in the transient state.

**Requirement**: Maintain the state of pickers with different palettes independently from data

**Targeted change**: The shared instance list causes the adjustment of one picker to contaminate other pickers in the transient state. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: No new shared variable interactions added.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0054

[Download patch](patches/P-0054-f1429369cfd0.patch)

SHA-256: f1429369cfd052b837d8e3d92280b5fcd00e73e96f94070090254e30219ea2f6

### VP-0057: Add some returns to the correct objects, but the DOM is not synchronized.

**Requirement**: The program adds a new anchor point with a return statement, and it presents it synchronously.

**Targeted change**: Add some returns to the correct objects, but the DOM is not synchronized. (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The returned object is the newly added ColorPoint, and the current presentation reflects the newly added point.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

## P-0055

[Download patch](patches/P-0055-fdc715ad0123.patch)

SHA-256: fdc715ad012392b11413d445e7b4e9a37d972ce34776b71bafcc3c2634063062

### VP-0058: Retired binding lost source and intergenerational check, can interfere with the current gesture with the same ID

**Requirement**: The old surface input cannot be obtained or interferes with the current interaction.

**Targeted change**: Retired binding lost source and intergenerational check, can interfere with the current gesture with the same ID (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not change the data or classes, emit events, end the current gesture, or release its pointer capture.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails

### VP-0059: Retired binding lost source and intergenerational check, can interfere with the current gesture with the same ID

**Requirement**: Cross-presentation reuse of pointerId still distinguishes between old sources and new gestures

**Targeted change**: Retired binding lost source and intergenerational check, can interfere with the current gesture with the same ID (changed files: src/picker-interaction.ts, src/picker-types.ts, src/picker-view.ts, src/webcomponent.ts)

**Entry point and initial state**: Apply this patch to the clean baseline at c0bf44b06d54, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not release the capture or change the current temporary state.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Patch application or test collection fails
