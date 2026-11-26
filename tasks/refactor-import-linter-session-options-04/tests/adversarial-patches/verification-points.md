# Adversarial test patches and verification points

Task: refactor-import-linter-session-options-04

Base commit: 31927f1457e3df673912cb5efb0afa6dbc37585f

Scope: adversarial patches exported after a complete inventory.
This package contains 27 distinct patches and 28 verification points.
The export omits 6 records without a primary patch, including controls and historical revisions. It excludes 6 control or auxiliary items and leaves 0 items unresolved.
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
| [P-0001](patches/P-0001-00cb23b562d0.patch) | VP-0001 | Targeted regression: Lint signatures, default values, and CLI flags are used for integration. |
| [P-0002](patches/P-0002-065e5699813d.patch) | VP-0002 | Targeted regression: The API module does not add a new lint_imports alias. |
| [P-0003](patches/P-0003-109c5c3a7070.patch) | VP-0003 | Targeted regression: Type checking for imported boolean interpretations belongs to the unified semantic owner |
| [P-0004](patches/P-0004-24ca28f8143c.patch) | VP-0004 | Targeted regression: The conversation timing configuration does not override the public flag, and the timing display does not affect the lint results. |
| [P-0005](patches/P-0005-30b745fa1ce2.patch) | VP-0005 | Targeted regression: INI loading retains single-line strings and multiple-line lists |
| [P-0006](patches/P-0006-467439898556.patch) | VP-0006 | Targeted regression: Retained unconfigured state when external package keys are missing |
| [P-0007](patches/P-0007-502e3330a132.patch) | VP-0007 | Targeted regression: Assign reading session timing options and interpreting their Boolean values to the same component. |
| [P-0008](patches/P-0008-55684fe419c8.patch) | VP-0008 | Targeted regression: The configuration API returns a normal double-key dict and a list of original contract dictionaries. |
| [P-0009](patches/P-0009-5825b2dbaa0f.patch) | VP-0009 | Targeted regression: The public signature of read_configuration remains unchanged. |
| [P-0010](patches/P-0010-5cfca8cae5d4.patch) | VP-0010 | Targeted regression: Debug mode retains the original exception propagation. |
| [P-0011](patches/P-0011-691ea9aa46c6.patch) | VP-0011 | Targeted regression: Explicit and default configuration selection paths remain unchanged |
| [P-0012](patches/P-0012-7bc454fefc24.patch) | VP-0012 | Targeted regression: When the TYPE_CHECKING import exclusion option is set to False or missing, imports within guards are still counted. |
| [P-0013](patches/P-0013-9331a81124ca.patch) | VP-0013 | Targeted regression: The forbidden check and graph builder agree on whether the same explicit external package value enables the feature. |
| [P-0014](patches/P-0014-9e7334a1e58c.patch) | VP-0014 | Targeted regression: External packages' boolean/unset interpretation is the responsibility of the unified semantics owner only. |
| [P-0015](patches/P-0015-aecad4777973.patch) | VP-0015 | Targeted regression: When the external package key is missing, forbidden treats external packages as excluded and rejects the external target through the existing error path. |
| [P-0016](patches/P-0016-ca31f5c5b5b8.patch) | VP-0016 | Targeted regression: Graph construction must honor an explicit setting that enables external packages. |
| [P-0017](patches/P-0017-d1bb572ab89d.patch) | VP-0017 | Targeted regression: The lack of configuration will continue to be exposed to the API caller via FileNotFoundError. |
| [P-0018](patches/P-0018-d36e8f5644b4.patch) | VP-0018 | Targeted regression: Configure API to not leak new type objects or introduce new boolean value conversions. |
| [P-0019](patches/P-0019-df16a6f7e62a.patch) | VP-0019, VP-0020 | Targeted regression: Return the standard singular root package before the API returns, and delete the legacy key. Targeted regression: Remove singular root package key before contract construction |
| [P-0020](patches/P-0020-df548bab105d.patch) | VP-0021 | Targeted regression: When the TYPE_CHECKING import exclusion options are enabled, imports within guards are not counted in the lint check. |
| [P-0021](patches/P-0021-dff8278f65bd.patch) | VP-0022 | Targeted regression: The contract_types configuration can still register and run the original custom contracts. |
| [P-0022](patches/P-0022-e3e823dbd600.patch) | VP-0023 | Targeted regression: Custom Contract retains the original construction protocol and obtains the standard root package by pressing the key. |
| [P-0023](patches/P-0023-e813ddcc85f8.patch) | VP-0024 | Targeted regression: The single root package has been standardized before composition. |
| [P-0024](patches/P-0024-f1c7c790097f.patch) | VP-0025 | Targeted regression: The contract returns True for approval and False for rejection. |
| [P-0025](patches/P-0025-f75a42e88fec.patch) | VP-0026 | Targeted regression: TOML Boolean continues to be stringified at the session and contract layer. |
| [P-0026](patches/P-0026-fa7a47202c3d.patch) | VP-0027 | Targeted regression: The root package reading is represented by a typed session, and the output package name list semantics are output. |
| [P-0027](patches/P-0027-fd95c93c6e0e.patch) | VP-0028 | Retain the display of errors that have been processed and False results in non-debug mode. |

## P-0001

[Download patch](patches/P-0001-00cb23b562d0.patch)

SHA-256: 00cb23b562d0afaaef179c4d3584e21c6265ede32ba916400b136c60889aae0c

### VP-0001: Targeted regression: Lint signatures, default values, and CLI flags are used for integration.

**Requirement**: The application adheres to lint signatures, default values, and CLI flags. Observable results: The seven parameters and default values are the same as the baseline. The existing CLI flags are still used, and the no_cache packaging capability and original default values are retained.

**Targeted change**: Targeted regression: Lint signatures, default values, and CLI flags are used for integration. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0002

[Download patch](patches/P-0002-065e5699813d.patch)

SHA-256: 065e5699813d6c661ef3d33df04004afd62733c36a4a518cb7bc109d6a99d1bf

### VP-0002: Targeted regression: The API module does not add a new lint_imports alias.

**Requirement**: The API module does not add a new lint_imports alias; observable result: api.lint_imports remains unchanged, and read_configuration is still publicly callable.

**Targeted change**: Targeted regression: The API module does not add a new lint_imports alias. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0003

[Download patch](patches/P-0003-109c5c3a7070.patch)

SHA-256: 109c5c3a7070ce9102c2c6a3b0c0bf0c32dd80f5079002b0b35ff0f4010b32ea

### VP-0003: Targeted regression: Type checking for imported boolean interpretations belongs to the unified semantic owner

**Requirement**: Type checking for imported boolean interpretations belongs to the unified semantic owner; observable result: there is a typed boolean semantics and a single interpretation responsibility; the composition consumer does not retain True/true private comparison.

**Targeted change**: Targeted regression: Type checking for imported boolean interpretations belongs to the unified semantic owner (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0004

[Download patch](patches/P-0004-24ca28f8143c.patch)

SHA-256: 24ca28f8143c09668fec75055d53d3fe621bdfe238791db5cbf49bd89dfc99d8

### VP-0004: Targeted regression: The conversation timing configuration does not override the public flag, and the timing display does not affect the lint results.

**Requirement**: The conversation timing configuration does not override the public flag. The timing display does not change the lint results. Observed results: When the public flag is False, configuring it to True still does not display the timing. When the public flag is True, the timing is still displayed, and the lint pass/fail values remain unchanged.

**Targeted change**: Targeted regression: The conversation timing configuration does not override the public flag, and the timing display does not affect the lint results. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0005

[Download patch](patches/P-0005-30b745fa1ce2.patch)

SHA-256: 30b745fa1ce2da61326cb34ff8bf4b1ca9c1d7fd989ab8da7a0426b4eba56c70

### VP-0005: Targeted regression: INI loading retains single-line strings and multiple-line lists

**Requirement**: INI loading retains single-line strings and multiple-line lists; observed results: INI boolean strings and multiple-line root_packages/contract_types/contract items lists are consistent with the baseline; no new or deleted keys were added.

**Targeted change**: Targeted regression: INI loading retains single-line strings and multiple-line lists (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0006

[Download patch](patches/P-0006-467439898556.patch)

SHA-256: 467439898556232885617d7cfecbd1332f7790f7e0b2571a62e7076f1b5316d8

### VP-0006: Targeted regression: Retained unconfigured state when external package keys are missing

**Requirement**: When the external package key is missing, the composition retains the unset state; observable result: the missing key remains None/unset, explicitly False, and the default selection of the diagram builder is retained; it is not mandatory to omit kwarg for this private shape.

**Targeted change**: Targeted regression: Retained unconfigured state when external package keys are missing (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0007

[Download patch](patches/P-0007-502e3330a132.patch)

SHA-256: 502e3330a1324d77c49e9c081a734eb6dc1e852993868259b9df6e275a7bdb1d

### VP-0007: Targeted regression: Assign reading session timing options and interpreting their Boolean values to the same component.

**Requirement**: The reading and boolean interpretation of the timing conversation option are attributed to the unified semantic owner; observable result: the type semantics of show_timings can be located, with shared interpretation responsibility; there is no requirement to configure the timing impact output, and the deletion of the idle private helper itself is not considered a sufficient implementation.

**Targeted change**: Targeted regression: Assign reading session timing options and interpreting their Boolean values to the same component. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0008

[Download patch](patches/P-0008-55684fe419c8.patch)

SHA-256: 55684fe419c8c3da8991b9e60b6fd675583a56eb465d2b0267c7894a8ded5db5

### VP-0008: Targeted regression: The configuration API returns a normal double-key dict and a list of original contract dictionaries.

**Requirement**: The configuration API returns a normal double-key dict along with the original contract dictionary list; observable results: type(result) is dict, and the keys are exactly session_options/contracts_options. The session is a dict, and the contracts are a list of dicts with no original fields lost.

**Targeted change**: Targeted regression: The configuration API returns a normal double-key dict and a list of original contract dictionaries. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0009

[Download patch](patches/P-0009-5825b2dbaa0f.patch)

SHA-256: 5825b2dbaa0f9c4332bda442d947a4d3ace1bf071d30d513dbb9773c0c071a4f

### VP-0009: Targeted regression: The public signature of read_configuration remains unchanged.

**Requirement**: The public signature of read_configuration remains unchanged; observable results: config_filename: str | None = None and dict return convention. The original calling method can be used.

**Targeted change**: Targeted regression: The public signature of read_configuration remains unchanged. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0010

[Download patch](patches/P-0010-5cfca8cae5d4.patch)

SHA-256: 5cfca8cae5d4193cba2d4bd5edec4a5ea7bf19c34953a4295b04cf9567f69412

### VP-0010: Targeted regression: Debug mode retains the original exception propagation.

**Requirement**: The original exception propagation is retained in debug mode; observable results: when is_debug_mode=True and there are errors in the original capture range such as reading configurations, the original exception will be thrown instead of being suppressed when is_debug_mode=False.

**Targeted change**: Targeted regression: Debug mode retains the original exception propagation. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0011

[Download patch](patches/P-0011-691ea9aa46c6.patch)

SHA-256: 691ea9aa46c621fea8f8bdb2767a40024e8a035114cdb50cf3575fd267ba5190

### VP-0011: Targeted regression: Explicit and default configuration selection paths remain unchanged

**Requirement**: The explicit and default configuration selection paths remain unchanged; observable results: TOML is selected for .toml files, other paths are selected as INI, and no changes are made to the order of existing files and readers; no changes in position or new selection strategies are introduced.

**Targeted change**: Targeted regression: Explicit and default configuration selection paths remain unchanged (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0012

[Download patch](patches/P-0012-7bc454fefc24.patch)

SHA-256: 7bc454fefc249bdcc87c1065187431d7a625001d951cbc88a31f19e408c438fb

### VP-0012: Targeted regression: When the TYPE_CHECKING import exclusion option is set to False or missing, imports within guards are still counted.

**Requirement**: When the TYPE_CHECKING import exclusion option is set to False or missing, imports within guards are still counted; observable result: When False or missing, related imports are retained, and related contracts are judged based on the baseline; missing values cannot be changed to exclusion.

**Targeted change**: Targeted regression: When the TYPE_CHECKING import exclusion option is set to False or missing, imports within guards are still counted. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0013

[Download patch](patches/P-0013-9331a81124ca.patch)

SHA-256: 9331a81124ca6ac88d93fb213e5c6b8bdff6dbfa6275ce84d008965edab85d31

### VP-0013: Targeted regression: The forbidden check and graph builder agree on whether the same explicit external package value enables the feature.

**Requirement**: The judgment of enabling the same explicit external package value for forbidden and composition is consistent; observable result: Both True/true are considered to include it; original TRUE and other publicly displayed discrepancies have the same true value, which can be uniformly accepted or rejected, without retaining the split judgment.

**Targeted change**: Targeted regression: The forbidden check and graph builder agree on whether the same explicit external package value enables the feature. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0014

[Download patch](patches/P-0014-9e7334a1e58c.patch)

SHA-256: 9e7334a1e58cfd4db3346ec99cbd33bba525ac132eb2d5767957660d306e5711

### VP-0014: Targeted regression: External packages' boolean/unset interpretation is the responsibility of the unified semantics owner only.

**Requirement**: The boolean/unset interpretation of external packages is the responsibility of the unified semantic owner; observable results: typeable bool/unset semantics can be located, with a shared interpretation source; consumers do not have their own original string comparisons.

**Targeted change**: Targeted regression: External packages' boolean/unset interpretation is the responsibility of the unified semantics owner only. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0015

[Download patch](patches/P-0015-aecad4777973.patch)

SHA-256: aecad4777973ae0fece7d922aea0c3985176b6cb8b63dc4c5f209339449933b9

### VP-0015: Targeted regression: When the external package key is missing, forbidden treats external packages as excluded and rejects the external target through the existing error path.

**Requirement**: When the external package key is missing, it is considered not included and the external target is rejected according to the original process. Observable result: the external enablement judgment is False. When an external forbidden target is included, it triggers existing validation errors and corresponding lint failures.

**Targeted change**: Targeted regression: When the external package key is missing, forbidden treats external packages as excluded and rejects the external target through the existing error path. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0016

[Download patch](patches/P-0016-ca31f5c5b5b8.patch)

SHA-256: ca31f5c5b5b84f178fe987889a851678f464b9668914a2f6d6a49c5e06ce80d0

### VP-0016: Targeted regression: Graph construction must honor an explicit setting that enables external packages.

**Requirement**: When include_external_packages is True or true, enable the graph construction parameter and inspect the resulting graph for external imports.

**Targeted change**: Targeted regression: Graph construction must honor an explicit setting that enables external packages. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0017

[Download patch](patches/P-0017-d1bb572ab89d.patch)

SHA-256: d1bb572ab89d8d68c9403bb16060e2f08ed2f7d5f54eed17edc75f7b79cdafdd

### VP-0017: Targeted regression: The lack of configuration will continue to be exposed to the API caller via FileNotFoundError.

**Requirement**: The lack of configuration will continue to be exposed to the API caller as FileNotFoundError; observable result: explicitly missing files or no configuration provided will result in a FileNotFoundError, without returning an empty configuration or False.

**Targeted change**: Targeted regression: The lack of configuration will continue to be exposed to the API caller via FileNotFoundError. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0018

[Download patch](patches/P-0018-d36e8f5644b4.patch)

SHA-256: d36e8f5644b483c3f690bac24fc7e823cc143bfe268e6200abad944397441b63

### VP-0018: Targeted regression: Configure API to not leak new type objects or introduce new boolean value conversions.

**Requirement**: The configuration API does not reveal new type objects or introduce additional boolean value conversions. Observable results: After using type objects internally, the session_options are still exposed as a raw dict. The boolean option strings remain intact, and existing lists/digits are not altered in any way.

**Targeted change**: Targeted regression: Configure API to not leak new type objects or introduce new boolean value conversions. (changed files: src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0019

[Download patch](patches/P-0019-df16a6f7e62a.patch)

SHA-256: df16a6f7e62ad76b78878ac8aacd0287a9756258c06753d6e50516deda6cbd97

### VP-0019: Targeted regression: Return the standard singular root package before the API returns, and delete the legacy key.

**Requirement**: Normalize the singular root package and remove the legacy key before returning from the API. root_package=one becomes root_packages=[one] with no root_package key. Preserve existing multi-root packages.

**Targeted change**: Targeted regression: Return the standard singular root package before the API returns, and delete the legacy key. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

### VP-0020: Targeted regression: Remove singular root package key before contract construction

**Requirement**: Remove the singular root package key before contract construction; observable result: the received mapping contains root_packages=[one] and does not contain root_package, and cannot only rely on temporary specifications in composition calls.

**Targeted change**: Targeted regression: Remove singular root package key before contract construction (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0020

[Download patch](patches/P-0020-df548bab105d.patch)

SHA-256: df548bab105d6752faa62f0ecc4d0dca03dc1a97084fc999a22a4a8babf57447

### VP-0021: Targeted regression: When the TYPE_CHECKING import exclusion options are enabled, imports within guards are not counted in the lint check.

**Requirement**: When the TYPE_CHECKING import exclusion option is enabled, imports within guards are not counted in the lint check. Observable result: If True/true, the diagram does not contain imports within guards, and contracts triggered only by that edge are kept with the original pass result.

**Targeted change**: Targeted regression: When the TYPE_CHECKING import exclusion options are enabled, imports within guards are not counted in the lint check. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0021

[Download patch](patches/P-0021-dff8278f65bd.patch)

SHA-256: dff8278f65bd7e730bd08174f8cca1a6148d603799a4b5a57c2b4ce9ed7993a6

### VP-0022: Targeted regression: The contract_types configuration can still register and run the original custom contracts.

**Requirement**: The contract_types configuration still allows for the registration and operation of original custom contracts. Observable results: The declared payload is not lost. Existing names: The class path can still import, register, instantiate, and inspect Contract subclasses.

**Targeted change**: Targeted regression: The contract_types configuration can still register and run the original custom contracts. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0022

[Download patch](patches/P-0022-e3e823dbd600.patch)

SHA-256: e3e823dbd6005e7512df800da261befb077dc284fc77109dc339dd1388ac9e98

### VP-0023: Targeted regression: Custom Contract retains the original construction protocol and obtains the standard root package by pressing the key.

**Requirement**: The custom Contract retains the original construction protocol and obtains the standard root package by pressing a key; observable result: The atomic class does not need to be migrated, and it is possible to read self.session_options[root_packages] to obtain a list of package names; the call to name/session_options/contract_options remains unchanged.

**Targeted change**: Targeted regression: Custom Contract retains the original construction protocol and obtains the standard root package by pressing the key. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0023

[Download patch](patches/P-0023-e813ddcc85f8.patch)

SHA-256: e813ddcc85f8539629231bfdf321440a8230e2c4133b798426e6a88d6c719dd6

### VP-0024: Targeted regression: The single root package has been standardized before composition.

**Requirement**: The single root package has been standardized before composition; observable result: the single configuration enables the diagram builder to obtain root_package_names=[one], while multiple root packages remain with their list contents and order intact.

**Targeted change**: Targeted regression: The single root package has been standardized before composition. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0024

[Download patch](patches/P-0024-f1c7c790097f.patch)

SHA-256: f1c7c790097f4a0c882e41a2f64855d2c238a8fb48a09fddb31377673a6c6a6b

### VP-0025: Targeted regression: The contract returns True for approval and False for rejection.

**Requirement**: The contract returns True and False respectively for approval and rejection; observable result: whether the application is successful/failed is a bool value, and the CLI packaging remains 0/1; other objects do not return the same truthiness.

**Targeted change**: Targeted regression: The contract returns True for approval and False for rejection. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0025

[Download patch](patches/P-0025-f75a42e88fec.patch)

SHA-256: f75a42e88fece518d53aeefd0305235aa444612b76f22b8b8b50d6bf4f37bcd3

### VP-0026: Targeted regression: TOML Boolean continues to be stringified at the session and contract layer.

**Requirement**: TOML Boolean continues to be stringified at the session and contract level; observable results: true/false is now represented as True/False strings at both levels, arrays/numbers remain intact, and contracts remain as independent lists.

**Targeted change**: Targeted regression: TOML Boolean continues to be stringified at the session and contract layer. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0026

[Download patch](patches/P-0026-fa7a47202c3d.patch)

SHA-256: fa7a47202c3de3a8693cab01a462c91c61bd289b9780b9b2d7747bbdcb5e4c02

### VP-0027: Targeted regression: The root package reading is represented by a typed session, and the output package name list semantics are output.

**Requirement**: The root package reading is represented by a typed session, outputting a list of package names with semantic meaning; observable results: type declarations and actual root package reading responsibilities are concentrated; the list of package names remains unchanged; there is no requirement for fixed class names, property names, or file locations.

**Targeted change**: Targeted regression: The root package reading is represented by a typed session, and the output package name list semantics are output. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid

## P-0027

[Download patch](patches/P-0027-fd95c93c6e0e.patch)

SHA-256: fd95c93c6e0e65aeeba6f8fff2cfb8d4c13306a3d059edf93fe6bc9ed0f90a10

### VP-0028: Retain the display of errors that have been processed and False results in non-debug mode.

**Requirement**: Ensure that the correct implementation does not exhibit the following incorrect behaviors: Displaying and returning False for errors that have already been processed in non-debug mode; Observable results: Errors are created in configurations, registrations, or reports, and are displayed and returned as False through existing presentation channels, without the error content being rewritten due to typification.

**Targeted change**: Retain the display of errors that have been processed and False results in non-debug mode. (changed files: src/importlinter/api.py, src/importlinter/application/use_cases.py, src/importlinter/application/user_options.py, src/importlinter/contracts/forbidden.py)

**Entry point and initial state**: Apply this patch to the clean baseline at 31927f1457e3, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- Test collection/execution/report invalid
