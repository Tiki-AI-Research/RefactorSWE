# Adversarial test patches and verification points

Task: refactor-jellyfin-kodi-dialog-base-07

Base commit: 9f2823a464f4f333affba462198b289766ebb137

Scope: partial export. Some items remain unresolved.
This package contains 35 distinct patches and 35 verification points.
The export omits 0 records without a primary patch, including controls and historical revisions. It excludes 1 control or auxiliary items and leaves 1 items unresolved.
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
| [P-0001](patches/P-0001-06814cebda90.patch) | VP-0001 | Targeted regression: The server lines remain in their original order, with labels, IDs, and Wi-Fi/network types preserved. |
| [P-0002](patches/P-0002-0bb9abd31920.patch) | VP-0002 | Targeted regression: LoginManual retains the original import, XML/skin parameter construction, and modal invocation. |
| [P-0003](patches/P-0003-17f3aa9454d3.patch) | VP-0003 | Targeted regression: Manually manage the host, connections, and keepalive of the server. Maintain the original navigation. |
| [P-0004](patches/P-0004-2271bf976f68.patch) | VP-0004 | Targeted regression: After successfully connecting to the server list, the results of the first server are displayed publicly, followed by the hidden overlay being closed. |
| [P-0005](patches/P-0005-245cb9044cd3.patch) | VP-0005 | Targeted regression: The four specific windows actually reuse the common UI mechanisms listed in the problem description through the same base class, while retaining their respective connection/authentication responsibilities. |
| [P-0006](patches/P-0006-26e6cb4f1dd0.patch) | VP-0006 | Targeted regression: Manual Server Window Focused Host Field |
| [P-0007](patches/P-0007-28370b351599.patch) | VP-0007 | Targeted regression: The four-window set_args still directly assigns all the provided fields, maintaining the original state of the fields that were not provided. |
| [P-0008](patches/P-0008-2910d09e07a1.patch) | VP-0008 | Targeted regression: ServerConnect retains the original import, XML/skin parameter construction, and modal invocation. |
| [P-0009](patches/P-0009-2acb4618663c.patch) | VP-0009 | Targeted regression: After the password field is added, a default password type is set. Regular fields still require normal input. |
| [P-0010](patches/P-0010-2d343bfdd2a1.patch) | VP-0010 | Targeted regression: Close the current window without generating selection or branch flags. |
| [P-0011](patches/P-0011-37ca3b679a7a.patch) | VP-0011 | Targeted regression: The manual login button sets the manual flag first and then closes. |
| [P-0012](patches/P-0012-384bd3a7b0cf.patch) | VP-0012 | Targeted regression: Empty host submission shows the original error and does not connect. |
| [P-0013](patches/P-0013-3c96dae9d9e5.patch) | VP-0013 | Targeted regression: The four-window component continues to work with the original control ID, display area, and input prompts. |
| [P-0014](patches/P-0014-45338393c501.patch) | VP-0014 | Targeted regression: The server list Unavailable is showing an error and remains open. |
| [P-0015](patches/P-0015-54cae1a9a84c.patch) | VP-0015 | Targeted regression: Set the manual flag for the manual server button before turning it off. |
| [P-0016](patches/P-0016-58d7ddcd5f4f.patch) | VP-0016 | Targeted change: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin |
| [P-0017](patches/P-0017-6ddcf5577809.patch) | VP-0017 | Targeted regression: Log in window switches the initial focus by entering the pre-filled username |
| [P-0018](patches/P-0018-6e85b4810e36.patch) | VP-0018 | Targeted regression: Login failed, displayed as invalid_auth, and remains open. |
| [P-0019](patches/P-0019-7cf0d5b0e16e.patch) | VP-0019 | Targeted regression: The user rows are maintained in the original order, with labels, IDs, and main/default images. |
| [P-0020](patches/P-0020-7f70a7993465.patch) | VP-0020 | Targeted regression: The user list always remains the focus |
| [P-0021](patches/P-0021-86ebdc60cf21.patch) | VP-0021 | Targeted regression: Confirm selecting the original user by line ID, and disclose the result before closing. |
| [P-0022](patches/P-0022-8d24bcee4303.patch) | VP-0022 | Targeted regression: The Quick Connect button first sets the quick flag and then closes it. |
| [P-0023](patches/P-0023-916d6bc9cba7.patch) | VP-0023 | Targeted regression: UsersConnect retains the original import, XML/skin parameter construction, and modal invocation. |
| [P-0024](patches/P-0024-9885e600c525.patch) | VP-0024 | Targeted regression: After the manual connection is successful, save the first server and close it. |
| [P-0025](patches/P-0025-99f1b821e793.patch) | VP-0025 | Targeted regression: Empty username submission displays the original error without logging in. |
| [P-0026](patches/P-0026-a7162e7d0de2.patch) | VP-0026 | Targeted regression: The initial focus of the server list is determined by whether the servers field is non-empty. |
| [P-0027](patches/P-0027-b0e6e01ce864.patch) | VP-0027 | Targeted regression: Login window username, password, login and cancel maintain the original navigation structure |
| [P-0028](patches/P-0028-c8b4968c28d9.patch) | VP-0028 | Targeted regression: Maintain the existing layout and editable input in the manual host and login editing box |
| [P-0029](patches/P-0029-ca17ced941c9.patch) | VP-0029 | Targeted regression: Eliminate previous empty input errors after entering the username |
| [P-0030](patches/P-0030-cde744551d94.patch) | VP-0030 | Targeted regression: Please enter the text of the host after removing the previous empty input error. |
| [P-0031](patches/P-0031-d48198e5f781.patch) | VP-0031 | Targeted regression: Submit the username/password as originally values to the current server address. Successfully save the original user result and then close the window. |
| [P-0032](patches/P-0032-e5cb368624b3.patch) | VP-0032 | Targeted regression: Manual connection fails and shows the Unavailable prompt, remaining open. |
| [P-0033](patches/P-0033-e732f8482f3d.patch) | VP-0033 | Targeted regression: ServerManual retains the original import, XML/skin parameter construction, and modal invocation. |
| [P-0034](patches/P-0034-ef64d72678e1.patch) | VP-0034 | Targeted regression: Display target name and busy indication during server list connection call |
| [P-0035](patches/P-0035-faacee6625d7.patch) | VP-0035 | Targeted regression: Cancel button closes the current window without generating a selection or branch flag. |

## P-0001

[Download patch](patches/P-0001-06814cebda90.patch)

SHA-256: 06814cebda90608a5861e99f14dde252c61e21edcb3e3b4bda8346cc7b9e44c8

### VP-0001: Targeted regression: The server lines remain in their original order, with labels, IDs, and Wi-Fi/network types preserved.

**Requirement**: The server lines remain in their original order, with labels, IDs, and Wi-Fi/network types preserved.

**Targeted change**: Targeted regression: The server lines remain in their original order, with labels, IDs, and Wi-Fi/network types preserved. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0002

[Download patch](patches/P-0002-0bb9abd31920.patch)

SHA-256: 0bb9abd319205099c4d1593ea16a8e4f704021225a4e05a4a4293fe856e0ff03

### VP-0002: Targeted regression: LoginManual retains the original import, XML/skin parameter construction, and modal invocation.

**Requirement**: LoginManual retains the original import, XML/skin parameter construction, and modal invocation.

**Targeted change**: Targeted regression: LoginManual retains the original import, XML/skin parameter construction, and modal invocation. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0003

[Download patch](patches/P-0003-17f3aa9454d3.patch)

SHA-256: 17f3aa9454d3bfd35a6ab13a45bd08d8e37395e6def38e91ab4af38c065fa1a4

### VP-0003: Targeted regression: Manually manage the host, connections, and keepalive of the server. Maintain the original navigation.

**Requirement**: Manually manage the host, connections, and keepalive of the server. Maintain the original navigation.

**Targeted change**: Targeted regression: Manually manage the host, connections, and keepalive of the server. Maintain the original navigation. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0004

[Download patch](patches/P-0004-2271bf976f68.patch)

SHA-256: 2271bf976f682405359c8b49c98a68bb6a721da1561e91f31d7b37d0157d13b8

### VP-0004: Targeted regression: After successfully connecting to the server list, the results of the first server are displayed publicly, followed by the hidden overlay being closed.

**Requirement**: After successfully connecting to the server list, the results of the first server are displayed publicly, followed by the hidden overlay being closed.

**Targeted change**: Targeted regression: After successfully connecting to the server list, the results of the first server are displayed publicly, followed by the hidden overlay being closed. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0005

[Download patch](patches/P-0005-245cb9044cd3.patch)

SHA-256: 245cb9044cd3b1f8a389179503a93bd8aa05bb953d8ffbb9ae658d2218dc6df0

### VP-0005: Targeted regression: The four specific windows actually reuse the common UI mechanisms listed in the problem description through the same base class, while retaining their respective connection/authentication responsibilities.

**Requirement**: The four specific windows actually reuse the common UI mechanisms listed in the problem description through the same base class, while retaining their respective connection/authentication responsibilities.

**Targeted change**: Targeted regression: The four specific windows actually reuse the common UI mechanisms listed in the problem description through the same base class, while retaining their respective connection/authentication responsibilities. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0006

[Download patch](patches/P-0006-26e6cb4f1dd0.patch)

SHA-256: 26e6cb4f1dd0cba5662de1cba84f987101884be76f7cc0dc46d8bd3aa08dd309

### VP-0006: Targeted regression: Manual Server Window Focused Host Field

**Requirement**: Manual Server Window Focused Host Field

**Targeted change**: Targeted regression: Manual Server Window Focused Host Field (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0007

[Download patch](patches/P-0007-28370b351599.patch)

SHA-256: 28370b351599c25ee8e7f20765b2549c8c0b818378623ce6376b30fe3aab9f46

### VP-0007: Targeted regression: The four-window set_args still directly assigns all the provided fields, maintaining the original state of the fields that were not provided.

**Requirement**: The four-window set_args still directly assigns all the provided fields, maintaining the original state of the fields that were not provided.

**Targeted change**: Targeted regression: The four-window set_args still directly assigns all the provided fields, maintaining the original state of the fields that were not provided. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0008

[Download patch](patches/P-0008-2910d09e07a1.patch)

SHA-256: 2910d09e07a1982f810e67c3b793e67e2b1d566c926bf26e9835cdb0411aac28

### VP-0008: Targeted regression: ServerConnect retains the original import, XML/skin parameter construction, and modal invocation.

**Requirement**: ServerConnect retains the original import, XML/skin parameter construction, and modal invocation.

**Targeted change**: Targeted regression: ServerConnect retains the original import, XML/skin parameter construction, and modal invocation. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0009

[Download patch](patches/P-0009-2acb4618663c.patch)

SHA-256: 2acb4618663c85923e35e3ccaad9b886b10aa3809de0077458f9a0d4d82609fd

### VP-0009: Targeted regression: After the password field is added, a default password type is set. Regular fields still require normal input.

**Requirement**: After the password field is added, a default password type is set. Regular fields still require normal input.

**Targeted change**: Targeted regression: After the password field is added, a default password type is set. Regular fields still require normal input. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0010

[Download patch](patches/P-0010-2d343bfdd2a1.patch)

SHA-256: 2d343bfdd2a1c534819cfca3dfaec8507fbccd5b26d35964199c1d9c3b48ed8e

### VP-0010: Targeted regression: Close the current window without generating selection or branch flags.

**Requirement**: Close the current window without generating selection or branch flags.

**Targeted change**: Targeted regression: Close the current window without generating selection or branch flags. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0011

[Download patch](patches/P-0011-37ca3b679a7a.patch)

SHA-256: 37ca3b679a7ad2c9c4dbe747f9c87dc47d8e4d850e581f5811ba86d7d4b652bd

### VP-0011: Targeted regression: The manual login button sets the manual flag first and then closes.

**Requirement**: The manual login button sets the manual flag first and then closes.

**Targeted change**: Targeted regression: The manual login button sets the manual flag first and then closes. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0012

[Download patch](patches/P-0012-384bd3a7b0cf.patch)

SHA-256: 384bd3a7b0cf098ecc2a9295eafe98ee65060acbefa3f95aa3ff377511de0ec8

### VP-0012: Targeted regression: Empty host submission shows the original error and does not connect.

**Requirement**: Empty host submission shows the original error and does not connect.

**Targeted change**: Targeted regression: Empty host submission shows the original error and does not connect. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0013

[Download patch](patches/P-0013-3c96dae9d9e5.patch)

SHA-256: 3c96dae9d9e5cde96befb48a1b9ec1072b4efe3e9b17f13d8ac639a303c08a7d

### VP-0013: Targeted regression: The four-window component continues to work with the original control ID, display area, and input prompts.

**Requirement**: The four-window component continues to work with the original control ID, display area, and input prompts.

**Targeted change**: Targeted regression: The four-window component continues to work with the original control ID, display area, and input prompts. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0014

[Download patch](patches/P-0014-45338393c501.patch)

SHA-256: 45338393c501b7d98c0a58994e42a978542a3bbdc6503cab86bc1db17af200ff

### VP-0014: Targeted regression: The server list Unavailable is showing an error and remains open.

**Requirement**: The server list Unavailable is showing an error and remains open.

**Targeted change**: Targeted regression: The server list Unavailable is showing an error and remains open. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0015

[Download patch](patches/P-0015-54cae1a9a84c.patch)

SHA-256: 54cae1a9a84c4ed356195ae142027dec47848ac5afdb5e5caf47004c501b8e11

### VP-0015: Targeted regression: Set the manual flag for the manual server button before turning it off.

**Requirement**: Set the manual flag for the manual server button before turning it off.

**Targeted change**: Targeted regression: Set the manual flag for the manual server button before turning it off. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0016

[Download patch](patches/P-0016-58d7ddcd5f4f.patch)

SHA-256: 58d7ddcd5f4f8e7e275270230a7209529224a0dbadf161501d1ad7841c372029

### VP-0016: Targeted change: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin

**Requirement**: Preserve existing behavior in the files changed by the patch (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Targeted change**: Targeted changes to jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0017

[Download patch](patches/P-0017-6ddcf5577809.patch)

SHA-256: 6ddcf55778099077cd6e25ca4fb282ed3b0d14dffc798aadd091bbb480b74cec

### VP-0017: Targeted regression: Log in window switches the initial focus by entering the pre-filled username

**Requirement**: Log in window switches the initial focus by entering the pre-filled username

**Targeted change**: Targeted regression: Log in window switches the initial focus by entering the pre-filled username (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0018

[Download patch](patches/P-0018-6e85b4810e36.patch)

SHA-256: 6e85b4810e36d832414fc6f5bae77b8bee922f6b66eac4d89785d9f2152d1eec

### VP-0018: Targeted regression: Login failed, displayed as invalid_auth, and remains open.

**Requirement**: Login failed, displayed as invalid_auth, and remains open.

**Targeted change**: Targeted regression: Login failed, displayed as invalid_auth, and remains open. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0019

[Download patch](patches/P-0019-7cf0d5b0e16e.patch)

SHA-256: 7cf0d5b0e16eedaacdc4a218721b3c20c50377b61373e337ac717332c4c33d67

### VP-0019: Targeted regression: The user rows are maintained in the original order, with labels, IDs, and main/default images.

**Requirement**: The user rows are maintained in the original order, with labels, IDs, and main/default images.

**Targeted change**: Targeted regression: The user rows are maintained in the original order, with labels, IDs, and main/default images. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0020

[Download patch](patches/P-0020-7f70a7993465.patch)

SHA-256: 7f70a7993465285223277f9deefbe7001665dd9b261d424fd4729678b0206e69

### VP-0020: Targeted regression: The user list always remains the focus

**Requirement**: The user list always remains the focus

**Targeted change**: Targeted regression: The user list always remains the focus (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0021

[Download patch](patches/P-0021-86ebdc60cf21.patch)

SHA-256: 86ebdc60cf215c572aab7268b684a51c713a7c90ac40dd7b7cf1e875fe800bb6

### VP-0021: Targeted regression: Confirm selecting the original user by line ID, and disclose the result before closing.

**Requirement**: Confirm selecting the original user by line ID, and disclose the result before closing.

**Targeted change**: Targeted regression: Confirm selecting the original user by line ID, and disclose the result before closing. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0022

[Download patch](patches/P-0022-8d24bcee4303.patch)

SHA-256: 8d24bcee4303eac95424ac4bc14e59bdd7939d89ccbedcebdfe2e05137f936f1

### VP-0022: Targeted regression: The Quick Connect button first sets the quick flag and then closes it.

**Requirement**: The Quick Connect button first sets the quick flag and then closes it.

**Targeted change**: Targeted regression: The Quick Connect button first sets the quick flag and then closes it. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0023

[Download patch](patches/P-0023-916d6bc9cba7.patch)

SHA-256: 916d6bc9cba7091ff7d30e0e5490c936ff3ec9d8e44797ddd934769fca8aa104

### VP-0023: Targeted regression: UsersConnect retains the original import, XML/skin parameter construction, and modal invocation.

**Requirement**: UsersConnect retains the original import, XML/skin parameter construction, and modal invocation.

**Targeted change**: Targeted regression: UsersConnect retains the original import, XML/skin parameter construction, and modal invocation. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0024

[Download patch](patches/P-0024-9885e600c525.patch)

SHA-256: 9885e600c5259cce1863a1b7094f93aec61fb4df7c98dcc5a1f4bd855f99301f

### VP-0024: Targeted regression: After the manual connection is successful, save the first server and close it.

**Requirement**: After the manual connection is successful, save the first server and close it.

**Targeted change**: Targeted regression: After the manual connection is successful, save the first server and close it. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0025

[Download patch](patches/P-0025-99f1b821e793.patch)

SHA-256: 99f1b821e793e80ec6c41159373a436e1f8f40825d7cce74740ef3dcb6eb19e5

### VP-0025: Targeted regression: Empty username submission displays the original error without logging in.

**Requirement**: Empty username submission displays the original error without logging in.

**Targeted change**: Targeted regression: Empty username submission displays the original error without logging in. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0026

[Download patch](patches/P-0026-a7162e7d0de2.patch)

SHA-256: a7162e7d0de284690807c8eedf95801521e3e4ccc54b22963bd616feac006b8c

### VP-0026: Targeted regression: The initial focus of the server list is determined by whether the servers field is non-empty.

**Requirement**: The initial focus of the server list is determined by whether the servers field is non-empty.

**Targeted change**: Targeted regression: The initial focus of the server list is determined by whether the servers field is non-empty. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0027

[Download patch](patches/P-0027-b0e6e01ce864.patch)

SHA-256: b0e6e01ce864d9abaf24c20215669d6e6f35f4a9935f97a92c5e4465fa0174e7

### VP-0027: Targeted regression: Login window username, password, login and cancel maintain the original navigation structure

**Requirement**: Login window username, password, login and cancel maintain the original navigation structure

**Targeted change**: Targeted regression: Login window username, password, login and cancel maintain the original navigation structure (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0028

[Download patch](patches/P-0028-c8b4968c28d9.patch)

SHA-256: c8b4968c28d916a1462b3bfc0f1ed4c7df3640aaeb520fd1d38ac8508deb02c1

### VP-0028: Targeted regression: Maintain the existing layout and editable input in the manual host and login editing box

**Requirement**: Maintain the existing layout and editable input in the manual host and login editing box

**Targeted change**: Targeted regression: Maintain the existing layout and editable input in the manual host and login editing box (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0029

[Download patch](patches/P-0029-ca17ced941c9.patch)

SHA-256: ca17ced941c949e5c1a4e787ac16099a09c0ad6a4980b3c9db9ebaf71984e090

### VP-0029: Targeted regression: Eliminate previous empty input errors after entering the username

**Requirement**: Eliminate previous empty input errors after entering the username

**Targeted change**: Targeted regression: Eliminate previous empty input errors after entering the username (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0030

[Download patch](patches/P-0030-cde744551d94.patch)

SHA-256: cde744551d94efd08e86c616c6b0ae56024aed7c6a64000929ed180b03e85887

### VP-0030: Targeted regression: Please enter the text of the host after removing the previous empty input error.

**Requirement**: Please enter the text of the host after removing the previous empty input error.

**Targeted change**: Targeted regression: Please enter the text of the host after removing the previous empty input error. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0031

[Download patch](patches/P-0031-d48198e5f781.patch)

SHA-256: d48198e5f781fa991cd1b5e2f47dc9d8300dd405669ed63d64a7d5ba51bd28b2

### VP-0031: Targeted regression: Submit the username/password as originally values to the current server address. Successfully save the original user result and then close the window.

**Requirement**: Submit the username/password as originally values to the current server address. Successfully save the original user result and then close the window.

**Targeted change**: Targeted regression: Submit the username/password as originally values to the current server address. Successfully save the original user result and then close the window. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0032

[Download patch](patches/P-0032-e5cb368624b3.patch)

SHA-256: e5cb368624b344a7843caf95a7d478a5cb3f21b630dd0ca9de82bd89651f90b2

### VP-0032: Targeted regression: Manual connection fails and shows the Unavailable prompt, remaining open.

**Requirement**: Manual connection fails and shows the Unavailable prompt, remaining open.

**Targeted change**: Targeted regression: Manual connection fails and shows the Unavailable prompt, remaining open. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0033

[Download patch](patches/P-0033-e732f8482f3d.patch)

SHA-256: e732f8482f3dc92b32b53268fca512dbce04cd02036678e38d296991a294a427

### VP-0033: Targeted regression: ServerManual retains the original import, XML/skin parameter construction, and modal invocation.

**Requirement**: ServerManual retains the original import, XML/skin parameter construction, and modal invocation.

**Targeted change**: Targeted regression: ServerManual retains the original import, XML/skin parameter construction, and modal invocation. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0034

[Download patch](patches/P-0034-ef64d72678e1.patch)

SHA-256: ef64d72678e163ae3ce0ff9d5be189d4142ca4fb1148508eb09c5363455854ae

### VP-0034: Targeted regression: Display target name and busy indication during server list connection call

**Requirement**: Display target name and busy indication during server list connection call

**Targeted change**: Targeted regression: Display target name and busy indication during server list connection call (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error

## P-0035

[Download patch](patches/P-0035-faacee6625d7.patch)

SHA-256: faacee6625d7aa25fc71a954bd91c99ae255da5d4fa70acab7dc945e700815e8

### VP-0035: Targeted regression: Cancel button closes the current window without generating a selection or branch flag.

**Requirement**: Cancel button closes the current window without generating a selection or branch flag.

**Targeted change**: Targeted regression: Cancel button closes the current window without generating a selection or branch flag. (changed files: jellyfin_kodi/dialogs/base.py, jellyfin_kodi/dialogs/loginmanual.py, jellyfin_kodi/dialogs/serverconnect.py, jellyfin_kodi/dialogs/servermanual.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The failure must come from an actual assertion

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection, import, or environment error
