# Adversarial test patches and verification points

Task: cknd-stackprinter-20260919134409-f34e9b

Base commit: 7a07a51a806e70c273a96071c87d19289bc0c69e

Scope: partial export. Some items remain unresolved.
This package contains 70 distinct patches and 70 verification points.
The export omits 10 records without a primary patch, including controls and historical revisions. It excludes 2 control or auxiliary items and leaves 23 items unresolved.
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
| [P-0001](patches/P-0001-09d8386302de.patch) | VP-0001 | Targeted regression: Migration section provides multi-line fenced code examples for migrating from legacy to the new entry point. |
| [P-0002](patches/P-0002-0afe22dd2338.patch) | VP-0002 | Targeted regression: When stderr is not available, show returns silently before all parameter checks. |
| [P-0003](patches/P-0003-0f2d3c63f336.patch) | VP-0003 | Targeted regression: Missing or None frames are uniformly provided with precise missing frame texts. |
| [P-0004](patches/P-0004-15bb9e814f83.patch) | VP-0004 | ['(prefix + line) if line else ""', '(prefix + prefix + line) if line else ""'] |
| [P-0005](patches/P-0005-172427fb2def.patch) | VP-0005 | ['if depth >= self.depth_limit:', 'if depth > self.depth_limit:'] |
| [P-0006](patches/P-0006-1cb6d78886d9.patch) | VP-0006 | Targeted regression: Configure to carry all 14 explicit options |
| [P-0007](patches/P-0007-22334ab9fd2a.patch) | VP-0007 | Targeted regression: The undisputed mode of show_vals retains validation, and True does not preset any specifications. |
| [P-0008](patches/P-0008-22f49b91336c.patch) | VP-0008 | ['frameinfos = frameinfos[-self.config.max_frames:]', 'frameinfos = frameinfos[: |
| [P-0009](patches/P-0009-2499ca59b558.patch) | VP-0009 | Targeted regression: Non-exception stack and trace entry strictly reject unknown kwargs |
| [P-0010](patches/P-0010-292d48d3e43e.patch) | VP-0010 | ['event_str = self.event_formatter.format_event(payload)', "event_str = self.eve |
| [P-0011](patches/P-0011-29895956ad8a.patch) | VP-0011 | ['return renderer.render(etype, evalue, tb)', "return renderer.render(etype, eva |
| [P-0012](patches/P-0012-2c079635c0e4.patch) | VP-0012 | Targeted regression: Publicly disclose the budget for each stack target and retain the top N frames. |
| [P-0013](patches/P-0013-34680391a628.patch) | VP-0013 | Targeted regression: FrameFormatter receives configuration at the beginning of the process and uses ANSI styler. |
| [P-0014](patches/P-0014-37abbf021f05.patch) | VP-0014 | Targeted regression: The trace event text was returned by TraceEventFormatter. |
| [P-0015](patches/P-0015-38a55b492efd.patch) | VP-0015 | Targeted regression: The target distribution retains four legal types, including the tuple form of BaseException |
| [P-0016](patches/P-0016-418a7c5c8c48.patch) | VP-0016 | Targeted regression: After an exception is raised, close the hook by calling stop_on_exception and propagate the exception. |
| [P-0017](patches/P-0017-4a2bc2afb64d.patch) | VP-0017 | Targeted regression: with_overrides constructs a new configuration and copies lists even for fields without overrides. |
| [P-0018](patches/P-0018-4d8e7db4f628.patch) | VP-0018 | Targeted regression: prefix does not occupy wrap width |
| [P-0019](patches/P-0019-4ee5d88b0caa.patch) | VP-0019 | Targeted regression: Explicit causes are outputed in the order they occur and with precise hints. |
| [P-0020](patches/P-0020-4f2bdc7f1188.patch) | VP-0020 | ["if not (isinstance(source_lines, int) or source_lines == 'all'):", 'if False:' |
| [P-0021](patches/P-0021-4faffa68fc28.patch) | VP-0021 | Targeted regression: If a frame or traceback line number has no mapping, fall back to co_firstlineno. |
| [P-0022](patches/P-0022-5036f5f5c282.patch) | VP-0022 | Targeted regression: Explicit ANSI aliases are equivalent to the canonical palette output. |
| [P-0023](patches/P-0023-533c663e955a.patch) | VP-0023 | Targeted regression: Migration Section with Specified Title |
| [P-0024](patches/P-0024-54411d8cedab.patch) | VP-0024 | Targeted regression: Activity exception unknown. kwargs is rejected or diagnosed in debug mode. |
| [P-0025](patches/P-0025-5530b5d39112.patch) | VP-0025 | ['if tb is None:\n            return', 'if tb is None:\n            FormatConfig |
| [P-0026](patches/P-0026-59d9b4fda623.patch) | VP-0026 | Targeted regression: Perform indentation type verification and None normalization as specified. |
| [P-0027](patches/P-0027-59f9138e9e99.patch) | VP-0027 | Targeted regression: Implementation of Styler abstraction and responsibilities for plain/ANSI subclasses |
| [P-0028](patches/P-0028-5d29c08a0d01.patch) | VP-0028 | Targeted regression: The public exception entry uses the return text of ExceptionRenderer. |
| [P-0029](patches/P-0029-5e11465be422.patch) | VP-0029 | Targeted regression: Reject the reserved name config instead of exposing it as a configuration parameter. |
| [P-0030](patches/P-0030-65578f690b8c.patch) | VP-0030 | Targeted regression: The exception renderer directly outputs the existing frame, source code, values, and message layout. |
| [P-0031](patches/P-0031-66db1b5f5659.patch) | VP-0031 | Targeted regression: The general options in the matrix are accepted for the listed targets, especially source_lines_after |
| [P-0032](patches/P-0032-6aaf3f305e76.patch) | VP-0032 | Targeted regression: Chain/Group Members and Thread Stack Independent Budget |
| [P-0033](patches/P-0033-72b501de02ad.patch) | VP-0033 | source_lines based on baseline type, conditions, and precise error verification |
| [P-0034](patches/P-0034-78ed4d023f8b.patch) | VP-0034 | Targeted regression: A non-Exception BaseException instance is rejected |
| [P-0035](patches/P-0035-7970b30945cb.patch) | VP-0035 | ["if getattr(self, '_frozen', False):", 'if False:'] |
| [P-0036](patches/P-0036-7afca809a55a.patch) | VP-0036 | Targeted regression: ColorfulFrameFormatter is equivalent to ANSI configuration of FrameFormatter. |
| [P-0037](patches/P-0037-7b1f5598c253.patch) | VP-0037 | Targeted regression: show is written in three output targets without returning a formatted string. |
| [P-0038](patches/P-0038-80096d0a1283.patch) | VP-0038 | ['get_styler(self.config.style)', "get_styler('plaintext')"] |
| [P-0040](patches/P-0040-87dfa8f25bef.patch) | VP-0040 | Targeted regression: trace uses explicit style configuration events through _config. |
| [P-0041](patches/P-0041-8b9664509fdb.patch) | VP-0041 | Targeted regression: Please keep the levels of call/return events, depth_limit, and print_function as they are. |
| [P-0042](patches/P-0042-8f7fc668a6c5.patch) | VP-0042 | Targeted regression: styler exception message method application style activity |
| [P-0043](patches/P-0043-9276bf9d3919.patch) | VP-0043 | ['elif isinstance(thing, Exception) or _is_exc_info(thing):', 'elif isinstance(t |
| [P-0044](patches/P-0044-97117d00dd87.patch) | VP-0044 | Targeted regression: FrameFormatter's plaintext configuration does not generate ANSI. |
| [P-0045](patches/P-0045-9915ec64c242.patch) | VP-0045 | Targeted regression: List module/class descriptions, responsibilities, and explanations for config and compatibility. |
| [P-0046](patches/P-0046-9bb718e4c24d.patch) | VP-0046 | Targeted regression: Budget Construction/Coverage Verification Default None and Positive Int |
| [P-0047](patches/P-0047-9be3bc8241e2.patch) | VP-0047 | Targeted regression: FrameFormatter can still be called with no parameters and using keyword arguments. |
| [P-0048](patches/P-0048-9c1a73c55591.patch) | VP-0048 | Targeted regression: Public Thread Entry Delegates Thread Formatter |
| [P-0049](patches/P-0049-aff8265c425d.patch) | VP-0049 | ['return PlaintextStyler()', "return AnsiStyler('darkbg')"] |
| [P-0050](patches/P-0050-b5f9f977a168.patch) | VP-0050 | ['%r: no frames found', '%r: missing frames'] |
| [P-0051](patches/P-0051-b789f34a43b9.patch) | VP-0051 | Targeted regression: The ExceptionGroup maintains the standard library backports. |
| [P-0052](patches/P-0052-bd147b92121d.patch) | VP-0052 | Targeted regression: Explicit options override the configuration, other configurations remain unchanged. |
| [P-0053](patches/P-0053-c0ad396fff7c.patch) | VP-0053 | Targeted regression: _config only accepts FormatConfig and checks for normal target validation before proceeding. |
| [P-0054](patches/P-0054-c3fb30f2d3de.patch) | VP-0054 | Targeted regression: Prefix each listed output line exactly once and leave empty lines empty. |
| [P-0055](patches/P-0055-c52d82f5d87b.patch) | VP-0055 | Targeted regression: If there is no explicit target, select the current exception or call stack based on the exception status. |
| [P-0056](patches/P-0056-d35debf883b0.patch) | VP-0056 | Targeted regression: The marker fixes the end of the block, including when reverse or summary is enabled. |
| [P-0057](patches/P-0057-d6a4502eac89.patch) | VP-0057 | ['return list(patterns)', 'return patterns if isinstance(patterns, list) else li |
| [P-0058](patches/P-0058-d8c877225d3b.patch) | VP-0058 | Targeted regression: If internal formatting fails, propagate through the debug switch or use the diagnostic fallback. |
| [P-0059](patches/P-0059-d9de17b14eb9.patch) | VP-0059 | Targeted regression: The configuration constructor copies the three non-None suppression collections into lists owned by the instance. |
| [P-0060](patches/P-0060-db781f8c66b6.patch) | VP-0060 | ["if file == 'stderr' and sys.stderr is None:", "if file == 'stderr' and sys.std |
| [P-0061](patches/P-0061-dd436b82b08d.patch) | VP-0061 | Targeted regression: Migration guidance consists of at least three orderly steps. |
| [P-0062](patches/P-0062-e4ba31e56ed0.patch) | VP-0062 | Targeted regression: Thread formatter independently outputs the thread headline and the original indentation stack convention. |
| [P-0063](patches/P-0063-e5e9d87f6d7e.patch) | VP-0063 | Targeted regression: No traceback instances are found. Return a plain message directly according to the clear priority. |
| [P-0064](patches/P-0064-e77b4f1fae5d.patch) | VP-0064 | Targeted regression: The default prefixes and the absence of a budget will not affect the legacy output. |
| [P-0065](patches/P-0065-e7adac75722d.patch) | VP-0065 | Targeted regression: The non-exception stack target explicitly suppressed_exceptions was rejected before the delegation. |
| [P-0066](patches/P-0066-ea5893a09aa2.patch) | VP-0066 | Targeted regression: All properties are assigned after initialization, rejection is required. |
| [P-0067](patches/P-0067-ebdaadbd8e2f.patch) | VP-0067 | Targeted regression: plain Alias Resolution without ANSI Style Output |
| [P-0068](patches/P-0068-ece0a0b44b7b.patch) | VP-0068 | Targeted regression: FormatConfig(max_frames=0) must reject zero as nonpositive. |
| [P-0069](patches/P-0069-ed094e42c4d2.patch) | VP-0069 | ['return formatter.format_thread(thing)', "return formatter.format_thread(thing) |
| [P-0070](patches/P-0070-f7874f84c6fd.patch) | VP-0070 | Targeted regression: Implicit context respects cause precedence and suppress_context. |
| [P-0071](patches/P-0071-f9ad6a88a95d.patch) | VP-0071 | ['return clr_head % type_str + clr_msg % val_str', 'return type_str + val_str'] |

## P-0001

[Download patch](patches/P-0001-09d8386302de.patch)

SHA-256: 09d8386302deef30f3f2695155e77c987fa0822590bb11ded6b5c0fc2a1ad7ca

### VP-0001: Targeted regression: Migration section provides multi-line fenced code examples for migrating from legacy to the new entry point.

**Requirement**: The migration section provides multiple lines of fenced code examples for migrating from the legacy to the new entry point. Observable results: There are multiple specific migration calls within the code fencing, not just a list of class names.

**Targeted change**: Targeted regression: Migration section provides multi-line fenced code examples for migrating from legacy to the new entry point. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0002-0afe22dd2338.patch)

SHA-256: 0afe22dd23386a5fa5cfdae1a9f736735df9559e5a5c5f7269eb927c31cdf625

### VP-0002: Targeted regression: When stderr is not available, show returns silently before all parameter checks.

**Requirement**: The show function returns silently without using the default stderr, and all parameter checks are performed before the return. Observable results: returns None, no output is written, even if the config/_config is invalid.

**Targeted change**: Targeted regression: When stderr is not available, show returns silently before all parameter checks. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0003-0f2d3c63f336.patch)

SHA-256: 0f2d3c63f3366d7752f3136ff9444964ca6dc3b467ef1ab34825f852a958c9e0

### VP-0003: Targeted regression: Missing or None frames are uniformly provided with precise missing frame texts.

**Requirement**: Missing or None frames are provided with precise missing frame text; observable result: The result is %r: no frames found, non-empty stack headline.

**Targeted change**: Targeted regression: Missing or None frames are uniformly provided with precise missing frame texts. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0004-15bb9e814f83.patch)

SHA-256: 15bb9e814f837d727a3be2000cd2ca790a58bb2c641b4c99b0b5d162230cefea

### VP-0004: ['(prefix + line) if line else ""', '(prefix + prefix + line) if line else ""']

**Requirement**: Indent add a prefix to each non-empty line of all target outputs once. Empty lines do not have spaces, and the prefix is placed after wrap.

**Targeted change**: ['(prefix + line) if line else ""', '(prefix + prefix + line) if line else ""'] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0005

[Download patch](patches/P-0005-172427fb2def.patch)

SHA-256: 172427fb2def71969ec5a4cd29efabacaa6b85ca7b23edb80f01d86d6db6da8b

### VP-0005: ['if depth >= self.depth_limit:', 'if depth > self.depth_limit:']

**Requirement**: After splitting the formatter, tracing must preserve depth filtering, nested indentation, and exception propagation and hook removal under stop_on_exception.

**Targeted change**: ['if depth >= self.depth_limit:', 'if depth > self.depth_limit:'] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0006

[Download patch](patches/P-0006-1cb6d78886d9.patch)

SHA-256: 1cb6d78886d9c0919a6cf3f5109e7db7f2d7988e0f2c932b482a356cd105abed

### VP-0006: Targeted regression: Configure to carry all 14 explicit options

**Requirement**: Configuration supports all 14 explicit options; observable results: After construction, the values of each field are readable, and the new max_frames/indent default value is correct.

**Targeted change**: Targeted regression: Configure to carry all 14 explicit options (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0007-22334ab9fd2a.patch)

SHA-256: 22334ab9fd2a864f7ef40edc7090810a690e7980db1966c5bb564bce58086cd7

### VP-0007: Targeted regression: The undisputed mode of show_vals retains validation, and True does not preset any specifications.

**Requirement**: Retain validation for the five explicitly supported show_vals modes. Reject non-Boolean values outside the set. The source records True separately and does not specify required behavior for it.

**Targeted change**: Targeted regression: The undisputed mode of show_vals retains validation, and True does not preset any specifications. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0008-22f49b91336c.patch)

SHA-256: 22f49b91336c2209a82ff43d7be52a13f500cc665a8f6851abfbea611f473736

### VP-0008: ['frameinfos = frameinfos[-self.config.max_frames:]', 'frameinfos = frameinfos[:

**Requirement**: For each supported stack block, max_frames=N keeps the N innermost frames and appends exactly the specified trailing marker only when the limit is exceeded.

**Targeted change**: ['frameinfos = frameinfos[-self.config.max_frames:]', 'frameinfos = frameinfos[:self.config.max_frames]'] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0009

[Download patch](patches/P-0009-2499ca59b558.patch)

SHA-256: 2499ca59b55810103c51a617886ac2d3f35d6308dc76f988f7b1db13bc78b55f

### VP-0009: Targeted regression: Non-exception stack and trace entry strictly reject unknown kwargs

**Requirement**: The exception stack and trace entry strictly reject unknown kwargs; observable result: TypeError instead of an exception fallback.

**Targeted change**: Targeted regression: Non-exception stack and trace entry strictly reject unknown kwargs (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0010-292d48d3e43e.patch)

SHA-256: 292d48d3e43ec93f9634b6e747aede9002621441848ce8b2a4aa1db12c9b9280

### VP-0010: ['event_str = self.event_formatter.format_event(payload)', "event_str = self.eve

**Requirement**: TracePrinter/@trace will format the text of each call, return, and exception event using TraceEventFormatter.

**Targeted change**: ['event_str = self.event_formatter.format_event(payload)', "event_str = self.event_formatter.format_event(payload)\n        event_str = ''"] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0011

[Download patch](patches/P-0011-29895956ad8a.patch)

SHA-256: 29895956ad8a3b6335fdd4b013796a23d8ea8e38fc4e92e3edb0093a2e2ada80

### VP-0011: ['return renderer.render(etype, evalue, tb)', "return renderer.render(etype, eva

**Requirement**: The public exception target delegates the formatted result to ExceptionRenderer.render and returns the output directly.

**Targeted change**: ['return renderer.render(etype, evalue, tb)', "return renderer.render(etype, evalue, tb) + ''"] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0012

[Download patch](patches/P-0012-2c079635c0e4.patch)

SHA-256: 2c079635c0e4a6f0088da0af410a3c4539f6c375eb8f6ecbb73726685cc32848

### VP-0012: Targeted regression: Publicly disclose the budget for each stack target and retain the top N frames.

**Requirement**: Publish the budget for each stack target and retain the innermost N frames; observable result: explicit N coverage of_config; remove the outermost k frames, with precise markers only when frames are removed.

**Targeted change**: Targeted regression: Publicly disclose the budget for each stack target and retain the top N frames. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0013-34680391a628.patch)

SHA-256: 34680391a6281f4aaf5fc0d9013701e918c383cb617b26be419e2934ae559146

### VP-0013: Targeted regression: FrameFormatter receives configuration at the beginning of the process and uses ANSI styler.

**Requirement**: FrameFormatter receives configuration at the beginning and uses ANSI styler; observable result: the configuration was successfully constructed, and the frame output contains ANSI styles.

**Targeted change**: Targeted regression: FrameFormatter receives configuration at the beginning of the process and uses ANSI styler. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0014-37abbf021f05.patch)

SHA-256: 37abbf021f051ba98b9a1bbfa3652d703456b84cd803926ffc0865cb1ec37ae3

### VP-0014: Targeted regression: The trace event text was returned by TraceEventFormatter.

**Requirement**: The trace event text is returned by TraceEventFormatter; observable results: text emitted by call/return/exception can be attributed to formatter output, no bypassing of concatenation.

**Targeted change**: Targeted regression: The trace event text was returned by TraceEventFormatter. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0015-38a55b492efd.patch)

SHA-256: 38a55b492efd3226d0c2de9c9ed16616e29928b67f5b25e38528d38ff579b629

### VP-0015: Targeted regression: The target distribution retains four legal types, including the tuple form of BaseException

**Requirement**: The target distribution retains four legal types, including the tuple form of BaseException; observable results: legal Exceptions/tuples/frames/threads have outputs; the BaseException tuple can be formatted.

**Targeted change**: Targeted regression: The target distribution retains four legal types, including the tuple form of BaseException (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0016-418a7c5c8c48.patch)

SHA-256: 418a7c5c8c4806e3c4958815876a38020c93521fce284751a68f707c09f45f83

### VP-0016: Targeted regression: After an exception is raised, close the hook by calling stop_on_exception and propagate the exception.

**Requirement**: After an exception is raised, the hook is closed by calling stop_on_exception and the exception is propagated. Observable results: the note is visible, the hook stops/resumes, and the user's exception is not suppressed.

**Targeted change**: Targeted regression: After an exception is raised, close the hook by calling stop_on_exception and propagate the exception. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0017-4a2bc2afb64d.patch)

SHA-256: 4a2bc2afb64d9c2ccc17b89b1d9f914722521865442c8b317aedf5bd91bf0d37

### VP-0017: Targeted regression: with_overrides constructs a new configuration and copies lists even for fields without overrides.

**Requirement**: With_overrides creates a new configuration and re-creates the list of fields that have not been modified; observable result: the new object and three non-None fields have independent identities.

**Targeted change**: Targeted regression: with_overrides constructs a new configuration and copies lists even for fields without overrides. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0018-4d8e7db4f628.patch)

SHA-256: 4d8e7db4f62837a740e4cf699442c3da3a40e77e207ec30e0d8bdec2eb0aef62

### VP-0018: Targeted regression: prefix does not occupy wrap width

**Requirement**: Prefix does not occupy the wrap width; observable result: The line break points of the content before and after adding the prefix are the same.

**Targeted change**: Targeted regression: prefix does not occupy wrap width (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0019-4ee5d88b0caa.patch)

SHA-256: 4ee5d88b0caadec27d25e9674803a96337edf79e284de28c37d84387ae2bcf70

### VP-0019: Targeted regression: Explicit causes are outputed in the order they occur and with precise hints.

**Requirement**: Explicit causes are output in the existing order with precise hints; observable results: causes come first, direct-causes are separated by text and line breaks.

**Targeted change**: Targeted regression: Explicit causes are outputed in the order they occur and with precise hints. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0020-4f2bdc7f1188.patch)

SHA-256: 4f2bdc7f1188437d1bc116a7e3ace41545c9633c2c8993ab5ea1a257825ffdce

### VP-0020: ["if not (isinstance(source_lines, int) or source_lines == 'all'):", 'if False:'

**Requirement**: Configure initialization and with_overrides to validate options according to the specified parameters, and generate the specified ValueError for invalid source_lines/max_frames/indent, etc.

**Targeted change**: ["if not (isinstance(source_lines, int) or source_lines == 'all'):", 'if False:'] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0021

[Download patch](patches/P-0021-4faffa68fc28.patch)

SHA-256: 4faffa68fc2840c599788a57d2855a2bf709f9a63f4202ca4b0da66b604c819b

### VP-0021: Targeted regression: If a frame or traceback line number has no mapping, fall back to co_firstlineno.

**Requirement**: No mapping of frame/traceback line numbers back to co_firstlineno; observable results: output of valid frame positions, no failure due to None line numbers.

**Targeted change**: Targeted regression: If a frame or traceback line number has no mapping, fall back to co_firstlineno. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/extraction.py, among others)

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

[Download patch](patches/P-0022-5036f5f5c282.patch)

SHA-256: 5036f5f5c282b497eb9fda30fd199e036fe3a09a510c11914a379353848fdee6

### VP-0022: Targeted regression: Explicit ANSI aliases are equivalent to the canonical palette output.

**Requirement**: Explicit ANSI aliases match their canonical palettes byte for byte. Compare dark with darkbg, light with lightbg, and True with color. All produce ANSI output.

**Targeted change**: Targeted regression: Explicit ANSI aliases are equivalent to the canonical palette output. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0023-533c663e955a.patch)

SHA-256: 533c663e955ae847749b065f6a20bd31760b7404c63728d215d5a17db71ef6a5

### VP-0023: Targeted regression: Migration Section with Specified Title

**Requirement**: Migration Section has a specified title; Observable Results: There is a Migration Capabilities & Integration Guidance title that is case-insensitive.

**Targeted change**: Targeted regression: Migration Section with Specified Title (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0024-54411d8cedab.patch)

SHA-256: 54411d8cedab6df2e0074a0b5c5d26b55b7f220f7ec3e9520b3dfaa853cc0582

### VP-0024: Targeted regression: Activity exception unknown. kwargs is rejected or diagnosed in debug mode.

**Requirement**: Activity exception unknown.kwargs Rejected or diagnosed in debug mode; observable result: TypeError when debug is set; diagnostic fallback when not set.

**Targeted change**: Targeted regression: Activity exception unknown. kwargs is rejected or diagnosed in debug mode. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0025-5530b5d39112.patch)

SHA-256: 5530b5d39112a4c474d37c5e625239aeb5ad73bb3e2508acaf225a928d11505f

### VP-0025: ['if tb is None:\n            return', 'if tb is None:\n            FormatConfig

**Requirement**: No traceback exception occurred before the normal format option validation, resulting in an empty style <Type>: <msg>. However, the configuration rejection and configuration type checking are retained.

**Targeted change**: ['if tb is None:\n            return', 'if tb is None:\n            FormatConfig(**kwargs)\n            return'] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0026

[Download patch](patches/P-0026-59d9b4fda623.patch)

SHA-256: 59d9b4fda6231d43b3026dd5ffa8c5404fe53f8f21fad4e5c44a891a6695d111

### VP-0026: Targeted regression: Perform indentation type verification and None normalization as specified.

**Requirement**: Indent type validation and None normalization are performed according to regulations; observable result: None is an empty string; an exact ValueError is raised for illegal types, and no validation is performed early.

**Targeted change**: Targeted regression: Perform indentation type verification and None normalization as specified. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0027-59f9138e9e99.patch)

SHA-256: 59f9138e9e99c290754e89d62969962d82932dd6ae3c19008df29298d03d657d

### VP-0027: Targeted regression: Implementation of Styler abstraction and responsibilities for plain/ANSI subclasses

**Requirement**: Implementing Styler abstractions and handling plain/ANSI subclass responsibilities; observable results: inheritance/abstraction relationships, source code, values, line numbers, and message styling capabilities.

**Targeted change**: Targeted regression: Implementation of Styler abstraction and responsibilities for plain/ANSI subclasses (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0028-5d29c08a0d01.patch)

SHA-256: 5d29c08a0d0163d9d88aefe50885e81b087751cf90a3e0df1470f7304f37d8b0

### VP-0028: Targeted regression: The public exception entry uses the return text of ExceptionRenderer.

**Requirement**: The public exception entry uses the text returned by ExceptionRenderer; observable results: the delegated call is observable; the format result or show output is the renderer output.

**Targeted change**: Targeted regression: The public exception entry uses the return text of ExceptionRenderer. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0029-5e11465be422.patch)

SHA-256: 5e11465be4228a382f7e01c72bc673e829a5e01246ee08e5745c77537bac91ef

### VP-0029: Targeted regression: Reject the reserved name config instead of exposing it as a configuration parameter.

**Requirement**: The config retains the name of the parameter, which is set to "reject" rather than "public" configuration parameters; observable results: TypeError, show suppresses the stderr output, except for silent paths.

**Targeted change**: Targeted regression: Reject the reserved name config instead of exposing it as a configuration parameter. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0030-65578f690b8c.patch)

SHA-256: 65578f690b8cfaa5957f6c159824df8d8680022243d1acb3b555bce383ba4b50

### VP-0030: Targeted regression: The exception renderer directly outputs the existing frame, source code, values, and message layout.

**Requirement**: The abnormal renderer directly outputs the existing frame, source code, values, and message layout; observable results: stable abnormal input/output includes the existing headline, arrow, frame order, values, and messages.

**Targeted change**: Targeted regression: The exception renderer directly outputs the existing frame, source code, values, and message layout. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0031-66db1b5f5659.patch)

SHA-256: 66db1b5f56593324eaffe6f8d58ad68d6e73e6f25d71ff924cfdc9787ea8229e

### VP-0031: Targeted regression: The general options in the matrix are accepted for the listed targets, especially source_lines_after

**Requirement**: The general options in the matrix are accepted for the listed targets, especially source_lines_after; observable result: The explicit parameters are not rejected by mistake, and source_lines_after actually changes the post-source context and defaults to 1.

**Targeted change**: Targeted regression: The general options in the matrix are accepted for the listed targets, especially source_lines_after (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0032-6aaf3f305e76.patch)

SHA-256: 6aaf3f305e766b4fc80be232b96bf2014dc048df40a8ba4381dcde69d2926a2a

### VP-0032: Targeted regression: Chain/Group Members and Thread Stack Independent Budget

**Requirement**: Chain/team members and thread stacks have independent counting budgets; observable results: each block has a maximum of N frames and an independent k, without using a shared total count

**Targeted change**: Targeted regression: Chain/Group Members and Thread Stack Independent Budget (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0033-72b501de02ad.patch)

SHA-256: 72b501de02addfae5d7629873d87159740bf5b1dc30b8ad16b2ee9982263e2be

### VP-0033: source_lines based on baseline type, conditions, and precise error verification

**Requirement**: Check source_lines against the baseline type rules and exact error behavior. Invalid types raise the original ValueError. Do not introduce a nonnegative-value restriction.

**Targeted change**: source_lines based on baseline type, conditions, and precise error verification (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0034-78ed4d023f8b.patch)

SHA-256: 78ed4d023f8bedde7e1570a1567133efdf945dcd18f8bd538b63ea7148149a9f

### VP-0034: Targeted regression: A non-Exception BaseException instance is rejected

**Requirement**: A non-Exception BaseException instance was rejected; observable result: ValueError was thrown, not formatted as a regular Exception.

**Targeted change**: Targeted regression: A non-Exception BaseException instance is rejected (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

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

[Download patch](patches/P-0035-7970b30945cb.patch)

SHA-256: 7970b30945cb619a54f49bdbd2e7566c9f29c4682a738fb1bfe6b4071a63711a

### VP-0035: ["if getattr(self, '_frozen', False):", 'if False:']

**Requirement**: The FormatConfig encapsulates the format options listed in the problem description. After construction, any property assignment will raise an AttributeError.

**Targeted change**: ["if getattr(self, '_frozen', False):", 'if False:'] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0036

[Download patch](patches/P-0036-7afca809a55a.patch)

SHA-256: 7afca809a55a647756f53fbf3c0214cfda3e4a57a4a27d171d5b5a96a2806647

### VP-0036: Targeted regression: ColorfulFrameFormatter is equivalent to ANSI configuration of FrameFormatter.

**Requirement**: ColorfulFrameFormatter is equivalent to ANSI configuration FrameFormatter; observable result: the same text is returned for the same frame and style.

**Targeted change**: Targeted regression: ColorfulFrameFormatter is equivalent to ANSI configuration of FrameFormatter. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0037

[Download patch](patches/P-0037-7b1f5598c253.patch)

SHA-256: 7b1f5598c2537d123d3b6b5d7d0f7555335caaeb7b4e22e64910ae0f4b1b805e

### VP-0037: Targeted regression: show is written in three output targets without returning a formatted string.

**Requirement**: show is written in three categories of output targets without returning a formatted string; observable results: the content of write is formatted text with print line breaks; returns None.

**Targeted change**: Targeted regression: show is written in three output targets without returning a formatted string. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0038

[Download patch](patches/P-0038-80096d0a1283.patch)

SHA-256: 80096d0a1283c6a2d80f0c5000d13789854012869f7a38f9426446a1fc556097

### VP-0038: ['get_styler(self.config.style)', "get_styler('plaintext')"]

**Requirement**: FrameFormatter accepts FormatConfig and generates frame outputs based on the active Styler, while retaining calls without configuration.

**Targeted change**: ['get_styler(self.config.style)', "get_styler('plaintext')"] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0040

[Download patch](patches/P-0040-87dfa8f25bef.patch)

SHA-256: 87dfa8f25bef53a55d206b219e6cdb6df115cf3ca8efe27d63fc150a4d06bb23

### VP-0040: Targeted regression: trace uses explicit style configuration events through _config.

**Requirement**: trace uses explicit style configuration events through _config.

**Targeted change**: Targeted regression: trace uses explicit style configuration events through _config. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0041

[Download patch](patches/P-0041-8b9664509fdb.patch)

SHA-256: 8b9664509fdb3c257a55c58d135aec57eb9226a3ec7e6c6752c10a12d1496e94

### VP-0041: Targeted regression: Please keep the levels of call/return events, depth_limit, and print_function as they are.

**Requirement**: Preserve nesting, depth_limit, and print_function for call/return events. Compare the nested event sequence, connector lines, and depth filtering. max_frames must not replace depth_limit.

**Targeted change**: Targeted regression: Please keep the levels of call/return events, depth_limit, and print_function as they are. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0042

[Download patch](patches/P-0042-8f7fc668a6c5.patch)

SHA-256: 8f7fc668a6c560042aad350fc6030bf1643ae795763b0021def8396494ee9b35

### VP-0042: Targeted regression: styler exception message method application style activity

**Requirement**: styler exception message method application style; observable results: returns str and the plain/ANSI message matches the selected style

**Targeted change**: Targeted regression: styler exception message method application style activity (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0043

[Download patch](patches/P-0043-9276bf9d3919.patch)

SHA-256: 9276bf9d3919b7fd54b73f56ce0460855b3f2a52d5a1fb5ee07b2623a84b6714

### VP-0043: ['elif isinstance(thing, Exception) or _is_exc_info(thing):', 'elif isinstance(t

**Requirement**: A non-Exception BaseException instance threw a ValueError, rejecting the target and specific unknown parameters according to the contract.

**Targeted change**: ['elif isinstance(thing, Exception) or _is_exc_info(thing):', 'elif isinstance(thing, BaseException) or _is_exc_info(thing):'] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0044

[Download patch](patches/P-0044-97117d00dd87.patch)

SHA-256: 97117d00dd87e5ab48d0b9cb70b5153239afba10b3b9bdb133712e70e52b7d43

### VP-0044: Targeted regression: FrameFormatter's plaintext configuration does not generate ANSI.

**Requirement**: The plaintext configuration of FrameFormatter does not produce ANSI; observable result: the frame output does not contain ESC[

**Targeted change**: Targeted regression: FrameFormatter's plaintext configuration does not generate ANSI. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0045

[Download patch](patches/P-0045-9915ec64c242.patch)

SHA-256: 9915ec64c242d6c77616308915bc7b9e77b5a1f1a757940ed49856111ada5457

### VP-0045: Targeted regression: List module/class descriptions, responsibilities, and explanations for config and compatibility.

**Requirement**: List module/class descriptions, responsibilities, and explanations for config and compatibility; observable results: seven core classes, with each module having a specific responsibility, not just a list of names.

**Targeted change**: Targeted regression: List module/class descriptions, responsibilities, and explanations for config and compatibility. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0046

[Download patch](patches/P-0046-9bb718e4c24d.patch)

SHA-256: 9bb718e4c24d26cd15f9c2010909334e112646c2ac002f8061c76aa02817b2a2

### VP-0046: Targeted regression: Budget Construction/Coverage Verification Default None and Positive Int

**Requirement**: Budget construction/coverage verification defaults to None and a positive integer; observable results: invalid values with the exact ValueError and corresponding messages, including None and positive integers.

**Targeted change**: Targeted regression: Budget Construction/Coverage Verification Default None and Positive Int (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0047

[Download patch](patches/P-0047-9be3bc8241e2.patch)

SHA-256: 9be3bc8241e237dd4e8d6ffa0aa92f479ea6141142fadfd5676acc4f4266ba27

### VP-0047: Targeted regression: FrameFormatter can still be called with no parameters and using keyword arguments.

**Requirement**: FrameFormatter can still be called with no parameters and without keywords. Observed results: The old form returns the existing frame text, without the need to pass configuration. The old position parameters are retained separately.

**Targeted change**: Targeted regression: FrameFormatter can still be called with no parameters and using keyword arguments. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0048

[Download patch](patches/P-0048-9c1a73c55591.patch)

SHA-256: 9c1a73c55591a77b39ecb34de3242d12130976acd79a1450bd064396a7570df7

### VP-0048: Targeted regression: Public Thread Entry Delegates Thread Formatter

**Requirement**: Public thread entry delegate set contains the thread formatter; observable results: format and direct formatter results are the same; show outputs the same results.

**Targeted change**: Targeted regression: Public Thread Entry Delegates Thread Formatter (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0049

[Download patch](patches/P-0049-aff8265c425d.patch)

SHA-256: aff8265c425d5b58ad26426c9311129c5e918420e3d2a6e42810eab880579c10

### VP-0049: ['return PlaintextStyler()', "return AnsiStyler('darkbg')"]

**Requirement**: Plain-text aliases produce output without ANSI escapes. The dark, light, and True aliases each match their specified ANSI style.

**Targeted change**: ['return PlaintextStyler()', "return AnsiStyler('darkbg')"] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0050

[Download patch](patches/P-0050-b5f9f977a168.patch)

SHA-256: b5f9f977a1680740122b790490f4b4d83fd3917cdb6551a6c684d569d6b9e190

### VP-0050: ['%r: no frames found', '%r: missing frames']

**Requirement**: When the thread has no frame mapping, it outputs accurate and deterministic frame missing text.

**Targeted change**: ['%r: no frames found', '%r: missing frames'] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0051

[Download patch](patches/P-0051-b789f34a43b9.patch)

SHA-256: b789f34a43b985f3905df784a57972a8c616378f41be55ba412c321f2b6ce861

### VP-0051: Targeted regression: The ExceptionGroup maintains the standard library backports.

**Requirement**: The ExceptionGroup maintains the standard library backends; observable result: the output is equal to the standard traceback.format_exception result, without additional error decomposition.

**Targeted change**: Targeted regression: The ExceptionGroup maintains the standard library backports. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0052

[Download patch](patches/P-0052-bd147b92121d.patch)

SHA-256: bd147b92121db19c071a7a1baec43091818607ae3e05fd3843a052623ae708b4

### VP-0052: Targeted regression: Explicit options override the configuration, other configurations remain unchanged.

**Requirement**: Explicit options override matching configuration fields. Fields without an override continue to use their configured values.

**Targeted change**: Targeted regression: Explicit options override the configuration, other configurations remain unchanged. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0053

[Download patch](patches/P-0053-c0ad396fff7c.patch)

SHA-256: c0ad396fff7c69ad9fa8977609571c5f6298ee7624fc0cacc2b3c71ea1a2a219

### VP-0053: Targeted regression: _config only accepts FormatConfig and checks for normal target validation before proceeding.

**Requirement**: _config only accepts FormatConfig and checks before performing normal target validation; observable results: non-instance TypeError, including instance paths without a traceback; show silently ignores exceptions.

**Targeted change**: Targeted regression: _config only accepts FormatConfig and checks for normal target validation before proceeding. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0054

[Download patch](patches/P-0054-c3fb30f2d3de.patch)

SHA-256: c3fb30f2d3dee437e8c313e6339579f5978dfe7238a99205711a819c5d446b93

### VP-0054: Targeted regression: Prefix each listed output line exactly once and leave empty lines empty.

**Requirement**: All listed output lines will have a prefix added to them. Empty lines will remain empty. Observers can observe the following: direct/indirect results are equal. Frames, markers, summaries, and trace connections are all processed according to non-empty rules.

**Targeted change**: Targeted regression: Prefix each listed output line exactly once and leave empty lines empty. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0055

[Download patch](patches/P-0055-c52d82f5d87b.patch)

SHA-256: c52d82f5d87bfc846de47b6e94ae1d639e6ba2a52c04328f4791ecae679e4b0c

### VP-0055: Targeted regression: If there is no explicit target, select the current exception or call stack based on the exception status.

**Requirement**: If there is no explicit target, select the current exception or call stack based on the exception status; observable result: the current exception is within the except block, and the caller stack is outside the except block.

**Targeted change**: Targeted regression: If there is no explicit target, select the current exception or call stack based on the exception status. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0056

[Download patch](patches/P-0056-d35debf883b0.patch)

SHA-256: d35debf883b02676ef2a44263216de58e1b626622766cb2283c9ac90e8bd8d6c

### VP-0056: Targeted regression: The marker fixes the end of the block, including when reverse or summary is enabled.

**Requirement**: The marker fixes the end of the block, including when reverse or summary is enabled; observable results: the marker is located after the message and at the end of the entire block, not moved to the beginning due to reverse sorting.

**Targeted change**: Targeted regression: The marker fixes the end of the block, including when reverse or summary is enabled. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0057

[Download patch](patches/P-0057-d6a4502eac89.patch)

SHA-256: d6a4502eac89842b957f317584578c5b7f97b25acb68e836c8c9327575db5b45

### VP-0057: ['return list(patterns)', 'return patterns if isinstance(patterns, list) else li

**Requirement**: The suppression collection holds independent list copies, overriding the list fields copied from the configuration.

**Targeted change**: ['return list(patterns)', 'return patterns if isinstance(patterns, list) else list(patterns)'] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0058

[Download patch](patches/P-0058-d8c877225d3b.patch)

SHA-256: d8c877225d3b22a3103c360b98b9426dcadd32cd3ea89438e43c60898c4f4b9a

### VP-0058: Targeted regression: If internal formatting fails, propagate through the debug switch or use the diagnostic fallback.

**Requirement**: Internal formatting failed. Propagate with the debug switch or use the diagnostic fallback. Observable result: Propagate if the environment variable exists; return "Stackprinter failed" prefix and the original traceback if not set.

**Targeted change**: Targeted regression: If internal formatting fails, propagate through the debug switch or use the diagnostic fallback. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0059

[Download patch](patches/P-0059-d9de17b14eb9.patch)

SHA-256: d9de17b14eb91670e0fafc9c91012f8add6c6d53b06ef2a2ab5ab8add1331fa6

### VP-0059: Targeted regression: The configuration constructor copies the three non-None suppression collections into lists owned by the instance.

**Requirement**: Configure the construction to copy three non-null sets as a self-owned list; observable results: values are equal, type is list, identity is not equal; None remains unchanged.

**Targeted change**: Targeted regression: The configuration constructor copies the three non-None suppression collections into lists owned by the instance. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0060

[Download patch](patches/P-0060-db781f8c66b6.patch)

SHA-256: db781f8c66b617d179e02973b31e2101b3f383498392855f5846f2b84f7f3152

### VP-0060: ["if file == 'stderr' and sys.stderr is None:", "if file == 'stderr' and sys.std

**Requirement**: When show lacks the default stderr, it returns None and does not validate any format parameters.

**Targeted change**: ["if file == 'stderr' and sys.stderr is None:", "if file == 'stderr' and sys.stderr is None and not kwargs:"] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0061

[Download patch](patches/P-0061-dd436b82b08d.patch)

SHA-256: dd436b82b08dcbb7f84fce3e8d098658e37829d70f2bee5e457142ed276c2429

### VP-0061: Targeted regression: Migration guidance consists of at least three orderly steps.

**Requirement**: The migration guide consists of at least three orderly steps; observable results: at least three ordered list steps describe the progressive migration.

**Targeted change**: Targeted regression: Migration guidance consists of at least three orderly steps. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0062

[Download patch](patches/P-0062-e4ba31e56ed0.patch)

SHA-256: e4ba31e56ed05f002ff52a81ca04e18b19ab333eaf0f427d6f4cf7cc07b651a2

### VP-0062: Targeted regression: Thread formatter independently outputs the thread headline and the original indentation stack convention.

**Requirement**: The thread formatter independently outputs the thread headline and the original indentation stack convention; observable results: thread repr, stack indentation, default threading path suppression, and the summary is retained by default.

**Targeted change**: Targeted regression: Thread formatter independently outputs the thread headline and the original indentation stack convention. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0063

[Download patch](patches/P-0063-e5e9d87f6d7e.patch)

SHA-256: e5e9d87f6d7ef87c02244b1bd1004c25641ea50a0c0780a09fd3088d17b0cbf2

### VP-0063: Targeted regression: No traceback instances are found. Return a plain message directly according to the clear priority.

**Requirement**: If there is no traceback, a plain message is returned directly according to the specified priority. Observable results: ordinary invalid options and ANSI are not effective. Names and _config types are still checked first. Silent stderr has exceptions.

**Targeted change**: Targeted regression: No traceback instances are found. Return a plain message directly according to the clear priority. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0064

[Download patch](patches/P-0064-e77b4f1fae5d.patch)

SHA-256: e77b4f1fae5db47eb7761a37d926cd85de5fa6508612063f426e01da6716fc83

### VP-0064: Targeted regression: The default prefixes and the absence of a budget will not affect the legacy output.

**Requirement**: The default prefix and no budget will not change the legacy output; observable result: The stable input is byte-by-byte consistent with the baseline, and each target is compared separately.

**Targeted change**: Targeted regression: The default prefixes and the absence of a budget will not affect the legacy output. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0065

[Download patch](patches/P-0065-e7adac75722d.patch)

SHA-256: e7adac75722d9b5ff6d46e6d178dc7a6888f647f51acb06b9c93f50d3f05a51e

### VP-0065: Targeted regression: The non-exception stack target explicitly suppressed_exceptions was rejected before the delegation.

**Requirement**: The non-exception stack target explicitly suppressed_exceptions was rejected before the delegation; observable result: a TypeError occurred with or without_config, and the formatter was not called.

**Targeted change**: Targeted regression: The non-exception stack target explicitly suppressed_exceptions was rejected before the delegation. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0066

[Download patch](patches/P-0066-ea5893a09aa2.patch)

SHA-256: ea5893a09aa204da22882e7fca7c27264e24231ce27718112c7e6a46c3d8de64

### VP-0066: Targeted regression: All properties are assigned after initialization, rejection is required.

**Requirement**: After initialization, all property assignments are rejected; observable result: existing, new, and protected property assignments throw AttributeError.

**Targeted change**: Targeted regression: All properties are assigned after initialization, rejection is required. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0067

[Download patch](patches/P-0067-ebdaadbd8e2f.patch)

SHA-256: ebdaadbd8e2fe1d4c5edf99efcfe5564b2d92bc0912b2a24fb97ccbe19d0626b

### VP-0067: Targeted regression: plain Alias Resolution without ANSI Style Output

**Requirement**: All explicitly listed plain aliases produce plain text without ANSI styling or an ESC[ sequence.

**Targeted change**: Targeted regression: plain Alias Resolution without ANSI Style Output (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0068

[Download patch](patches/P-0068-ece0a0b44b7b.patch)

SHA-256: ece0a0b44b7b1208bc345dcd38dc02c9f48a7c42825f6eda8cb89fc7af2caf31

### VP-0068: Targeted regression: FormatConfig(max_frames=0) must reject zero as nonpositive.

**Requirement**: FormatConfig(max_frames=0) must reject zero as nonpositive.

**Targeted change**: Targeted regression: FormatConfig(max_frames=0) must reject zero as nonpositive. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- candidate patch did not apply
- collection or infrastructure failure
- failure unrelated to max_frames=0

## P-0069

[Download patch](patches/P-0069-ed094e42c4d2.patch)

SHA-256: ed094e42c4d2da5d0391be3f89a9a84187ef372ce787ac993e5241cec89ca314

### VP-0069: ['return formatter.format_thread(thing)', "return formatter.format_thread(thing)

**Requirement**: The public thread formats the target delegate ThreadStackFormatter.format_thread and directly returns the formatted output.

**Targeted change**: ['return formatter.format_thread(thing)', "return formatter.format_thread(thing) + ''"] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed

## P-0070

[Download patch](patches/P-0070-f7874f84c6fd.patch)

SHA-256: f7874f84c6fd053e83574e776a4fae2cd8a6c90e648550e8252f890bde5c02ef

### VP-0070: Targeted regression: Implicit context respects cause precedence and suppress_context.

**Requirement**: Implicit context respects cause precedence and suppress_context. An unsuppressed context uses the exact handling message. With from None, the context is absent.

**Targeted change**: Targeted regression: Implicit context respects cause precedence and suppress_context. (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.

## P-0071

[Download patch](patches/P-0071-f9ad6a88a95d.patch)

SHA-256: f9ad6a88a95df7f8640f06018046fa49c2c629c000a7fbed3ef6a2a8f32b0f1d

### VP-0071: ['return clr_head % type_str + clr_msg % val_str', 'return type_str + val_str']

**Requirement**: PlaintextStyler and AnsiStyler use corresponding styles to output exception messages.

**Targeted change**: ['return clr_head % type_str + clr_msg % val_str', 'return type_str + val_str'] (changed files: REFACTORING.md, stackprinter/__init__.py, stackprinter/config.py, stackprinter/formatting.py, among others)

**Entry point and initial state**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.

**Expected outcome**: Reject the faulty candidate

**Expected result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.

**Patch starting point**: Clean baseline

**Prerequisites**: None (clean baseline)

**Conditions that invalidate the check**: 

- The patch does not apply to the task baseline (APPLY_FAILED).
- The task image fails to build or the container environment fails (ENV_ERROR).
- The tests produce no case-level report, fail to finish, or time out.
- The target input did not actually arrive.
- pytest import or collection failed
