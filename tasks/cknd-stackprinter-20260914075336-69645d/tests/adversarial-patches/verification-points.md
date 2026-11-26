# Adversarial patches and verification points

Task: cknd-stackprinter-20260914075336-69645d
Base commit: 7a07a51a806e70c273a96071c87d19289bc0c69e

This package contains 11 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0002

[patch](patches/P-0002-124120a7020c.patch)
SHA-256: 124120a7020cabd022396987f4dacf0bddf53a8ef811691baef8d89d7f963731

### VP-0002: Targeted change: Standard and IPython exception hooks can still be restored when the sink fails. The remove_excepthook continues to maintain its existing semantics.

- **requirement**: Standard and IPython exception hooks can still be restored when the sink fails. The remove_excepthook continues to maintain its existing semantics.
- **mutation**: Targeted change: Standard and IPython exception hooks can still be restored when the sink fails. The remove_excepthook continues to maintain its existing semantics. (changed files: stackprinter/__init__.py, stackprinter/formatting.py, stackprinter/frame_formatting.py, stackprinter/frame_preparation.py, among others)
- **setup**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior did not actually occur.

## P-0003

[patch](patches/P-0003-440575218013.patch)
SHA-256: 4405752180138190e9955aca039c22fb554a7e44158cc16d9c6a280eac9a9895

### VP-0003: Targeted change: Exception singleton, cause/context chain, and summary are identical byte by byte to plaintext when formatted in plain format, without adding any ANSI characters.

- **requirement**: Exception singleton, cause/context chain, and summary are identical byte by byte to plaintext when formatted in plain format, without adding any ANSI characters.
- **mutation**: Targeted change: Exception singleton, cause/context chain, and summary are identical byte by byte to plaintext when formatted in plain format, without adding any ANSI characters. (changed files: stackprinter/__init__.py, stackprinter/formatting.py, stackprinter/frame_formatting.py, stackprinter/frame_preparation.py, among others)
- **setup**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior did not actually occur.

## P-0006

[patch](patches/P-0006-5a902c76916a.patch)
SHA-256: 5a902c76916a4b8143599336b8dc8ba17b1ab5960869a7f6edef57655357db2e

### VP-0006: Targeted change: After manual enabling, a sink exception occurred. Calling disable to restore the previous state of this layer, including nested manual activations.

- **requirement**: After manual enabling, a sink exception occurred. Calling disable to restore the previous state of this layer, including nested manual activations.
- **mutation**: Targeted change: After manual enabling, a sink exception occurred. Calling disable to restore the previous state of this layer, including nested manual activations. (changed files: stackprinter/__init__.py, stackprinter/formatting.py, stackprinter/frame_formatting.py, stackprinter/frame_preparation.py, among others)
- **setup**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior did not actually occur.

## P-0007

[patch](patches/P-0007-5ccab0d702a3.patch)
SHA-256: 5ccab0d702a3a7b30efad6d433fc262be909f2a7b66a76efbe51702a5152629b

### VP-0007: Targeted change: format_thread retains the original sequence content and type after successful, failed, and duplicate calls of list/tuple suppressed_paths.

- **requirement**: format_thread retains the original sequence content and type after successful, failed, and duplicate calls of list/tuple suppressed_paths.
- **mutation**: Targeted change: format_thread retains the original sequence content and type after successful, failed, and duplicate calls of list/tuple suppressed_paths. (changed files: stackprinter/__init__.py, stackprinter/formatting.py, stackprinter/frame_formatting.py, stackprinter/frame_preparation.py, among others)
- **setup**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior did not actually occur.

## P-0008

[patch](patches/P-0008-8e7cd4b3a750.patch)
SHA-256: 8e7cd4b3a7503bdcbba4b3685df5da86501e1aa13e54f19364f98caba5b6b92c

### VP-0008: Targeted change: After all activations are completed, do not prevent the recycling of the originally unreachable application objects by saving exceptions or frames.

- **requirement**: After all activations are completed, do not prevent the recycling of the originally unreachable application objects by saving exceptions or frames.
- **mutation**: Targeted change: After all activations are completed, do not prevent the recycling of the originally unreachable application objects by saving exceptions or frames. (changed files: stackprinter/__init__.py, stackprinter/formatting.py, stackprinter/frame_formatting.py, stackprinter/frame_preparation.py, among others)
- **setup**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior did not actually occur.

## P-0011

[patch](patches/P-0011-ab5361d68408.patch)
SHA-256: ab5361d684085329dd7f39915de7d80e82578d7d03ff4d6cb852ae4115f65b27

### VP-0011: Targeted change: In plain style, format must return and show must write the same text as plaintext.

- **requirement**: In plain style, format must return and show must write the same text as plaintext.
- **mutation**: Targeted change: In plain style, format must return and show must write the same text as plaintext. (changed files: stackprinter/__init__.py)
- **setup**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior did not actually occur.

## P-0012

[patch](patches/P-0012-af3b90c38229.patch)
SHA-256: af3b90c3822968c376e5a86342d6042dfd69124ac0f6d162e3f8d89da2db2e19

### VP-0012: Targeted change: The recursive decorator call is independently restored for each call, closely following the predecessor.

- **requirement**: The recursive decorator call is independently restored for each call, closely following the predecessor.
- **mutation**: Targeted change: The recursive decorator call is independently restored for each call, closely following the predecessor. (changed files: stackprinter/__init__.py, stackprinter/formatting.py, stackprinter/frame_formatting.py, stackprinter/frame_preparation.py, among others)
- **setup**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior did not actually occur.

## P-0013

[patch](patches/P-0013-b09c4679c04b.patch)
SHA-256: b09c4679c04b4d4a0d732ebaad6e219c625fc132a13b38d66e41128f125069b8

### VP-0013: Targeted change: When an internal activation exception is caught by the outer layer, the outer layer's trace hook is still installed when it exits.

- **requirement**: When an internal activation exception is caught by the outer layer, the outer layer's trace hook is still installed when it exits.
- **mutation**: Targeted change: When an internal activation exception is caught by the outer layer, the outer layer's trace hook is still installed when it exits. (changed files: stackprinter/__init__.py, stackprinter/formatting.py, stackprinter/frame_formatting.py, stackprinter/frame_preparation.py, among others)
- **setup**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior did not actually occur.

## P-0014

[patch](patches/P-0014-e18a29ab7507.patch)
SHA-256: e18a29ab7507f44428d2b29d49827a759c7da3e63d5293572024492278fe8ceb

### VP-0014: Targeted change: When the function fresh raise the same exception object that has been captured in the inner layer, stop_on_exception=True will stop the current execution.

- **requirement**: When the function fresh raise the same exception object that has been captured in the inner layer, stop_on_exception=True will stop the current execution.
- **mutation**: Targeted change: When the function fresh raise the same exception object that has been captured in the inner layer, stop_on_exception=True will stop the current execution. (changed files: stackprinter/__init__.py, stackprinter/formatting.py, stackprinter/frame_formatting.py, stackprinter/frame_preparation.py, among others)
- **setup**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior did not actually occur.

## P-0015

[patch](patches/P-0015-e606254f9700.patch)
SHA-256: e606254f97007ca9bc238b847d78362009619282edb11f052e6933529c29e019

### VP-0015: Targeted change: When the same exception object is raised within the running frame where context/enable is entered, the current activation stops.

- **requirement**: When the same exception object is raised within the running frame where context/enable is entered, the current activation stops.
- **mutation**: Targeted change: When the same exception object is raised within the running frame where context/enable is entered, the current activation stops. (changed files: stackprinter/__init__.py, stackprinter/formatting.py, stackprinter/frame_formatting.py, stackprinter/frame_preparation.py, among others)
- **setup**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior did not actually occur.

## P-0016

[patch](patches/P-0016-fd11b35a2f64.patch)
SHA-256: fd11b35a2f642124ac39aab471812a35604761eae9ec909b02246f6535a68709

### VP-0016: Targeted change: Restore the currently active predecessor before the sink exception reaches the caller in the decorator context.

- **requirement**: Restore the currently active predecessor before the sink exception reaches the caller in the decorator context.
- **mutation**: Targeted change: Restore the currently active predecessor before the sink exception reaches the caller in the decorator context. (changed files: stackprinter/__init__.py, stackprinter/formatting.py, stackprinter/frame_formatting.py, stackprinter/frame_preparation.py, among others)
- **setup**: Apply this patch to the clean baseline at 7a07a51a806e, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target behavior did not actually occur.

