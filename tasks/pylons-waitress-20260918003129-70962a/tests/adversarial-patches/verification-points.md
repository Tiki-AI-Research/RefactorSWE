# Adversarial patches and verification points

Task: pylons-waitress-20260918003129-70962a
Base commit: 016eea527dd4a3eb4a18d6dca4d0bfe32039e470

This package contains 39 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-00824d0a3a1f.patch)
SHA-256: 00824d0a3a1f98c2963b701ce63f50b9ac2c137eb6b628553e85c87d08f4dcab

### VP-0001: Zero buffer error delegate not closed

- **requirement**: Zero size files, buffer back to normal iteration, and close when the task is completed
- **mutation**: Zero buffer error delegate not closed (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0002

[patch](patches/P-0002-008645ab091b.patch)
SHA-256: 008645ab091bbf5e122200d489ff22b4bb9dffa37e9b022374b8b55c69690494

### VP-0002: Successful delegation leads to early closure of the buffer for tasks.

- **requirement**: Adjust the length of the non-zero file buffer and hand over the cleanup to the channel
- **mutation**: Successful delegation leads to early closure of the buffer for tasks. (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0003

[patch](patches/P-0003-06da054cc173.patch)
SHA-256: 06da054cc173e918a8085f8944791bb2715a2c3ab8b514ec3916570f35d80952

### VP-0003: Via does not use server ident

- **requirement**: The Server and Via are selected based on the last Server and ident. The preset Server is retained.
- **mutation**: Via does not use server ident (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0004

[patch](patches/P-0004-0b0dc1ce7b13.patch)
SHA-256: 0b0dc1ce7b135e3f2733824a44163cc7d0ea538f915181d80df7804f64106463

### VP-0004: ErrorTask lost error status

- **requirement**: ErrorTask maintains the metadata and body for generating error responses.
- **mutation**: ErrorTask lost error status (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0006

[patch](patches/P-0006-0f5d48fdfe13.patch)
SHA-256: 0f5d48fdfe130584f57f9612789fa7d8bdecb78399e86e45b2f33f8cc8b24c10

### VP-0006: Retain old headers during exc_info replacement

- **requirement**: Before headers are sent, exc_info replaces the metadata. Clear the old headers, accept the new status and headers, and preserve the existing update rules for other attributes.
- **mutation**: Retain old headers during exc_info replacement (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0007

[patch](patches/P-0007-0f6322acfc84.patch)
SHA-256: 0f6322acfc843043f02141bc937e8ec85a714668a5d968102f433b009b75123e

### VP-0007: Close HEAD task due to shortfall

- **requirement**: The HEAD shortform does not trigger a shortform closure or warning; a clean HEAD task returns a small amount or empty bodies without closing due to this reason, and there is no shortform warning.
- **mutation**: Close HEAD task due to shortfall (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0009

[patch](patches/P-0009-10fbaf2ba022.patch)
SHA-256: 10fbaf2ba0228076589d16939cf201a0a4a545a8d63bddb4dc72a67576bf59f1

### VP-0009: start_response does not return write.

- **requirement**: The direct method accepts metadata through an application callback and returns task.write.
- **mutation**: start_response does not return write. (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0010

[patch](patches/P-0010-122e9705e897.patch)
SHA-256: 122e9705e897a2ac66aa81fc6db79c20290a2dfae52f3a4e3106b468afb8912e

### VP-0010: Cleanup of ownership before failed delegation error transfer

- **requirement**: The task is still responsible for cleaning up after the buffer delegation failure.
- **mutation**: Cleanup of ownership before failed delegation error transfer (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0011

[patch](patches/P-0011-14155a33a57f.patch)
SHA-256: 14155a33a57f0efa41bc9516b07161bad22b2810e87dab7a10df03fd46962fa8

### VP-0011: Cross-Task Shared Error Snapshot Cache

- **requirement**: Task response status is independent, no shared variable preparation results
- **mutation**: Cross-Task Shared Error Snapshot Cache (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0012

[patch](patches/P-0012-1b0bc2367ac6.patch)
SHA-256: 1b0bc2367ac65ca65a2ad52f044e2de60220305dd3e5bf859915955febd915db

### VP-0012: Remove duplicate chunked headers

- **requirement**: If there is already a chunked, only the single chunked header will be output.
- **mutation**: Remove duplicate chunked headers (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0013

[patch](patches/P-0013-1ed3df548e37.patch)
SHA-256: 1ed3df548e373864ecf18a013c69a8c7b04df8cf4f8357d6ff706370d38759cf

### VP-0013: When configuring requirements, swallowing exceptions when propagating socket errors

- **requirement**: Socket error propagation follows the configuration and retains the closed state; OSError always sets close_on_finish; if the configuration is true, it will re-throw the exception; if it is false, it will end normally.
- **mutation**: When configuring requirements, swallowing exceptions when propagating socket errors (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Target state successfully reached
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target entry or input state has not been reached. Collecting or environmental errors

## P-0014

[patch](patches/P-0014-1f11886d669f.patch)
SHA-256: 1f11886d669feadc89287d71100958010889456a7d97d1785f12c8864618b905

### VP-0014: HTTP1.1 forces a forced close of inconvertible conflicts Connection

- **requirement**: Force the HTTP/1.1 connection to close the overlap conflict by overriding the Connection header, and remove duplicate close operations.
- **mutation**: HTTP1.1 forces a forced close of inconvertible conflicts Connection (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0017

[patch](patches/P-0017-229f491bebb4.patch)
SHA-256: 229f491bebb4a2c8b370b771f081de1301797442b6cee0e84969f2682f7bd49f

### VP-0017: Unknown request version falls back to HTTP/1.1

- **requirement**: Preparation error for constructing version backports and illegal overwriting versions; unknown request version backport 1.0, if it is overwritten as an illegal version, an AssertionError will be raised.
- **mutation**: Unknown request version falls back to HTTP/1.1 (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0018

[patch](patches/P-0018-2735341f8a3f.patch)
SHA-256: 2735341f8a3f9ad8f967b87e9d3cd8212d5d02434510caf7587cfe312f0e00e4

### VP-0018: Preset integer ordinary header not stringified

- **requirement**: Stringify ordinary preset header values without modifying the original list.
- **mutation**: Preset integer ordinary header not stringified (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0019

[patch](patches/P-0019-2ae6700e3415.patch)
SHA-256: 2ae6700e3415054bda2888b5ffc7f04b3b63221f976e75fd2bb8450bfaa109af

### VP-0019: Legacy builder adds extra CRLF

- **requirement**: The response bytes of the old build are consistent with the pure preparation; the same unsent state prepare_header_bytes is equal to the bytes returned by the build.
- **mutation**: Legacy builder adds extra CRLF (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0020

[patch](patches/P-0020-2e0420020eb8.patch)
SHA-256: 2e0420020eb84446668c4d4a816eb157a74c93655ccdef70d8bb0b312a55b6bf

### VP-0020: HTTP1.0 ignores forced close priorities

- **requirement**: HTTP/1.0 does not support close-overflow headers when keep-alive or forced close is not supported; only Connection: close, prepared close true, and old close header markers true are considered. A closed state cannot be revoked by keep-alive.
- **mutation**: HTTP1.0 ignores forced close priorities (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Target state successfully reached
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target entry or input state has not been reached. Collecting or environmental errors

## P-0025

[patch](patches/P-0025-3c43c8c2f2fe.patch)
SHA-256: 3c43c8c2f2fe26074205ec9a2ef3ad6997498f539ae3bcb166ab27a0d72ac511

### VP-0025: The forbidden state is allowed, and the CL is parsed.

- **requirement**: Prohibit body state suppression of CL and TE, and do not parse the suppressed length.
- **mutation**: The forbidden state is allowed, and the CL is parsed. (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0026

[patch](patches/P-0026-3c81d7ad14ad.patch)
SHA-256: 3c81d7ad14ad728b9afcd90f81ba57f9e62ef9b281221fb45d0a055f3fca7f9a

### VP-0026: Accepting CL without parsing integers

- **requirement**: When accepting a WSGI request, the Content-Length is parsed immediately; valid values are set as integer lengths, and non-parseable values will result in a ValueError during the acceptance phase.
- **mutation**: Accepting CL without parsing integers (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Target state successfully reached
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target entry or input state has not been reached. Collecting or environmental errors

## P-0027

[patch](patches/P-0027-3d21858cb02c.patch)
SHA-256: 3d21858cb02ca2213f3698b767c154279e6e0555775cbf475ff35ba36f741510

### VP-0027: Export object in place of PreparedResponse type

- **requirement**: Export the type and keep the zero-argument preparation entry point. Import it, call the method without arguments, and check that isinstance identifies the result as PreparedResponse.
- **mutation**: Export object in place of PreparedResponse type (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0028

[patch](patches/P-0028-3dbd9b9433f3.patch)
SHA-256: 3dbd9b9433f35f0d9cc545e89c3c3460ebb813d2128301c8080ee26303eeda50

### VP-0028: Error accepting status with CRLF

- **requirement**: WSGI rejects CR/LF metadata; ValueError occurs when the status or header name/value contains line breaks.
- **mutation**: Error accepting status with CRLF (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Target state successfully reached
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target entry or input state has not been reached. Collecting or environmental errors

## P-0029

[patch](patches/P-0029-3de12bd9702c.patch)
SHA-256: 3de12bd9702c7c8a4c71bad9b48f697b0bf63c313d859aa7ba109c2218badfe9

### VP-0029: Error allowed when no response is received

- **requirement**: If the response is not accepted, write will reject with the original error; if complete is false, raise RuntimeError with a precise message.
- **mutation**: Error allowed when no response is received (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Target state successfully reached
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target entry or input state has not been reached. Collecting or environmental errors

## P-0030

[patch](patches/P-0030-424db595493a.patch)
SHA-256: 424db595493a9cede66a801f7aaf83752899ba73c7c32b43abc13ac3d7ec83a4

### VP-0030: Do not infer single-item length

- **requirement**: Single iterators infer the body length only when there is no known length; the length of the only item reported as length 1 is established as content_length, with 0 for empty items; when there is already a length, it is not a single item, or there is no len.
- **mutation**: Do not infer single-item length (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0033

[patch](patches/P-0033-48e29e21ef35.patch)
SHA-256: 48e29e21ef3593ba86a7425a020d72add7f54a6cb4e9a15996f14851d8ace69f

### VP-0033: Ignore HTTP/1.1 request Connection close

- **requirement**: HTTP/1.1 Default persistence is consistent with explicit closing conditions; if the request is clean and has a length, no Connection is automatically added and not closed; if the request is closed or already closed, or if the allow body has no length, it is closed.
- **mutation**: Ignore HTTP/1.1 request Connection close (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0034

[patch](patches/P-0034-4dbcf5eb1afd.patch)
SHA-256: 4dbcf5eb1afdea282ba652efb1b1d272fc5bf6bbeaa538be1d57dd680636a514

### VP-0034: Chunk length-delimited preset encoding responses

- **requirement**: Responses delimited by length must not use chunking and must preserve any preset encoding. For HTTP/1.1 with a length and preset gzip, preserve gzip, set chunked=False, and emit the raw body bytes.
- **mutation**: Chunk length-delimited preset encoding responses (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0035

[patch](patches/P-0035-50d6cef3f1b4.patch)
SHA-256: 50d6cef3f1b4cf18ca7899ee074a4d0c4133a6dd10a5d7ebb2fbd568e0dd21a9

### VP-0035: Do not generate Date when final Date is empty

- **requirement**: The last Date value controls automatic generation. Preserve duplicate and empty Date fields. Append a Date based on start_time only if Date is missing or its last value is empty.
- **mutation**: Do not generate Date when final Date is empty (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0037

[patch](patches/P-0037-537824500c57.patch)
SHA-256: 537824500c573b3301154b227bd42343f2dc98a756a2652b174361995ddec541

### VP-0037: Commit sorted wire order instead of legacy header list order

- **requirement**: The old build maintains the append order of the task header list rather than the line sorting order.
- **mutation**: Commit sorted wire order instead of legacy header list order (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0040

[patch](patches/P-0040-585ff2130658.patch)
SHA-256: 585ff213065800e62d88372f39530f613256b7416faa3d853b90edf7d7437f78

### VP-0040: Block length error in lowercase hexadecimal

- **requirement**: Block-based sending and ending of final blocks conform to the original line format
- **mutation**: Block length error in lowercase hexadecimal (changed files: src/waitress/task.py, src/waitress/response.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0044

[patch](patches/P-0044-5ba9445dce6a.patch)
SHA-256: 5ba9445dce6a1af1916978c11fa7ccd1f083ee66f697536608622599a68ae86b

### VP-0044: Leak ordinary closeable iterable

- **requirement**: The regular and exceptional exit of the ordinary closable iterator will be closed once; the close call count will be 1 when the iteration is successful, failed, or a send failure occurs.
- **mutation**: Leak ordinary closeable iterable (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0046

[patch](patches/P-0046-5f2d2fe84e26.patch)
SHA-256: 5f2d2fe84e26d24b35cc8a324bd35e0fe82c45dd90bcfc2e2bdfc131e4728091

### VP-0046: Wrong repeated-acceptance exception message

- **requirement**: No duplicate acceptance with exc_info is allowed; duplicate calls will raise AssertionError and the full message provided in the problem description.
- **mutation**: Wrong repeated-acceptance exception message (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0048

[patch](patches/P-0048-6140dd8444c0.patch)
SHA-256: 6140dd8444c0de5feb48f7fa0c9ad4533304fb921ced4dcfae78f440a2b7ca50

### VP-0048: Task length overrides explicit zero header

- **requirement**: The effective length calculation follows the explicit header and correctly retains an integer 0; the explicit Content-Length covers Task.content_length, and 0 remains an integer 0 while disabling automatic chunking. The line length is consistent with the return value.
- **mutation**: Task length overrides explicit zero header (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0049

[patch](patches/P-0049-61843556da72.patch)
SHA-256: 61843556da72b5aa6795c6a823dfeb1dca312e7861111006f3fbe42eef5b706a

### VP-0049: Recreate instead of rethrowing same exception object

- **requirement**: When exc_info is thrown again, the original exception is re-thrown; the object thrown is exc_info[1], and the head is not rewritten.
- **mutation**: Recreate instead of rethrowing same exception object (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0050

[patch](patches/P-0050-639e00bd1df3.patch)
SHA-256: 639e00bd1df38bc9f68ce08382deda8416f2bb08a7b34d32304e3280420222c6

### VP-0050: Short text remains closed, only necessary warnings are skipped, and non-existent logger methods are not called.

- **requirement**: If the iteration length is insufficient, close and alert; HEAD is exempted; for non-HEAD short responses, use close_on_finish and warning. For HEAD cases, neither of these two alerts is triggered.
- **mutation**: Short text remains closed, only necessary warnings are skipped, and non-existent logger methods are not called. (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Target state successfully reached
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target entry or input state has not been reached. Collecting or environmental errors

## P-0053

[patch](patches/P-0053-66f54a999f3b.patch)
SHA-256: 66f54a999f3b3e56168601b9aaafb891d5d6b985deacb668b72abb3719d260ce

### VP-0053: ErrorTask preparation does not force closure before execute

- **requirement**: An error task must force a close under both HTTP versions, even for keep-alive requests or conflicting preset headers. Emit exactly one Connection: close.
- **mutation**: ErrorTask preparation does not force closure before execute (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0055

[patch](patches/P-0055-6d8ffef2f7e7.patch)
SHA-256: 6d8ffef2f7e73170576efd8940506eb6c03d868c1d791fb5685a3182d83c852d

### VP-0055: Accept forbidden WSGI hop-by-hop header

- **requirement**: WSGI hop-by-hop headers maintain a rejection boundary; direct Task headers are not uniformly filtered due to this.
- **mutation**: Accept forbidden WSGI hop-by-hop header (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0056

[patch](patches/P-0056-6ea7b8d814d8.patch)
SHA-256: 6ea7b8d814d86389da7ff23630cec68c90cbc5d53cd198d3d347e1f7ba8761dd

### VP-0056: HTTP1.0 error rejection for legitimate keepalive requests

- **requirement**: HTTP/1.0 Normally, there is a Keep-Alive header for length negotiation; when the negotiation is successful, the Keep-Alive header is unique, and if it is closed, it is considered false; a length of 0 is also valid.
- **mutation**: HTTP1.0 error rejection for legitimate keepalive requests (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Target state successfully reached
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target entry or input state has not been reached. Collecting or environmental errors

## P-0066

[patch](patches/P-0066-7fe56fcdb816.patch)
SHA-256: 7fe56fcdb81623faf47e9771bf7b70cd9e7ef796a9c0631dff4147f0560d6cf0

### VP-0066: Drop preset gzip coding before chunked

- **requirement**: The non-chunked preset encoding remains, and "chunked" is appended after it. After a non-length HTTP/1.1 response with gzip, two TE headers follow, with "chunked=True".
- **mutation**: Drop preset gzip coding before chunked (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0087

[patch](patches/P-0087-996aba283c48.patch)
SHA-256: 996aba283c48bd62aaa826b4e2466dbae19120cad6926c95d015865e4ace6309

### VP-0087: Task instances share mutable header list

- **requirement**: Response preparation does not introduce global or cross-task shared variable metadata; no global variable response states are written in the source code; preparation for different tasks does not contaminate header data.
- **mutation**: Task instances share mutable header list (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0115

[patch](patches/P-0115-d450f08be3d8.patch)
SHA-256: d450f08be3d8955111bc25ec58c81c41adf2f64cf7ccc84a280419690de4a17e

### VP-0115: Do not truncate excessive body bytes

- **requirement**: Respect the effective content length across successive writes. An explicit length, including 0, takes precedence. Cap the total bytes written, update content_bytes_written correctly, and use logged_write_excess to warn only once.
- **mutation**: Do not truncate excessive body bytes (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

## P-0132

[patch](patches/P-0132-eaac757e5327.patch)
SHA-256: eaac757e5327afb172210fd5610ef35b9d8855d1a2c345a164bb00fac7402fb8

### VP-0132: Allow CR/LF header-name injection

- **requirement**: CR/LF injection in WSGI causes ValueError; CR/LF in status, header name, or header value leads to ValueError
- **mutation**: Allow CR/LF header-name injection (changed files: src/waitress/__init__.py, src/waitress/response.py, src/waitress/task.py)
- **setup**: Apply this patch to the clean baseline at 016eea527dd4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: full official candidate evaluation rejects with actual node evidence.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. candidate cannot apply or pass deterministic gates; public operation not reached; evaluation incomplete or reports missing

