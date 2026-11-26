# Adversarial patches and verification points

Task: refactor-imageio-request-resource-01
Base commit: 319335265d293c4cf18705dbe11dcc1515702a97

This package contains 35 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-010225c94b30.patch)
SHA-256: 010225c94b30874c599ae03fbe733941f2ee4438e4bbf2d7015b8bc4c5633419

### VP-0001: Error closing borrowed handle

- **requirement**: Keep the caller's file open status
- **mutation**: Error closing borrowed handle (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0002

[patch](patches/P-0002-0b39af8457c2.patch)
SHA-256: 0b39af8457c27648764778382c07656014925efc049e329b216d99232f828407

### VP-0002: Memory resource read content corrupted

- **requirement**: get_file provides access to the original data for local, zip, memory, and caller's resources.
- **mutation**: Memory resource read content corrupted (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0003

[patch](patches/P-0003-0b58821f675f.patch)
SHA-256: 0b58821f675fb1dd9437338ad6a77012ed9136e86ffb082e51a7575298d20f8f

### VP-0003: The HTTP video backend receives modified URIs.

- **requirement**: PyAV directly passes the original URI to the backend for HTTP(S) reading.
- **mutation**: The HTTP video backend receives modified URIs. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0004

[patch](patches/P-0004-0e070d803f26.patch)
SHA-256: 0e070d803f26d5dd9b710cb1314c37977d7403648eb9f4787dd157cb8fa61e0f

### VP-0004: Add default value to necessary mode to change the signature

- **requirement**: Ensure the Request construction signature remains intact
- **mutation**: Add default value to necessary mode to change the signature (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0005

[patch](patches/P-0005-d9a2d040b5b0.patch)
SHA-256: d9a2d040b5b00e710c4ebdd3009e6b691cabccc4c64101762e749554c6d101e0

### VP-0005: Error using a default value of 1 second when HTTP missing timeout configuration is present

- **requirement**: Error in using a default value of 1 second when HTTP missing timeout is configured (violates the requirement of maintaining the original task behavior)
- **mutation**: Error using a default value of 1 second when HTTP missing timeout configuration is present
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry must be effectively rejected; an ineffective execution cannot be considered a success.
- **prerequisites**: None (clean baseline)
- **version_note**: The original audit retired this verification point. It is retained for historical reference.
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0006

[patch](patches/P-0006-2f9b47a1bbc7.patch)
SHA-256: 2f9b47a1bbc73ceaf3d74a65235ab9588416052b692536fd29b0a2a40e556aba

### VP-0006: Remove only the existing get_result declaration from the stub. Preserve runtime behavior.

- **requirement**: Continuing to expose legacy Request call surfaces with package type declaration
- **mutation**: Remove only the existing get_result declaration from the stub. Preserve runtime behavior. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0007

[patch](patches/P-0007-31088b03516e.patch)
SHA-256: 31088b03516e68450b00f8c16696b3f1ef8b3420af2fc1bc11961e0234152c2f

### VP-0007: Rejection Message Changes

- **requirement**: Rejection Branch Retention Mode Related Types and Messages
- **mutation**: Rejection Message Changes (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0008

[patch](patches/P-0008-35a3e16b4d1a.patch)
SHA-256: 35a3e16b4d1af74ae77d375156322e60cdd02eef3dca714435361cd41fe09fe1

### VP-0008: Restore the get_local_filename responsibility to the Request number branch

- **requirement**: The resource object is responsible for creating its local temporary files.
- **mutation**: Restore the get_local_filename responsibility to the Request number branch (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0009

[patch](patches/P-0009-3e3df892c37e.patch)
SHA-256: 3e3df892c37e035ee019da22584b2b836182318053c5883af22853a457a74328

### VP-0009: The standard image ZIP member was incorrectly replaced.

- **requirement**: The standard image continues to be correctly parsed in both normal and zip member formats.
- **mutation**: The standard image ZIP member was incorrectly replaced. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0010

[patch](patches/P-0010-3f4d8db58c01.patch)
SHA-256: 3f4d8db58c01bca02aba36af66ebb74dd8468096b05c798d5c3b4f81ed719969

### VP-0010: Return byte write-back additional error data

- **requirement**: Write the own output of RETURN_BYTES to the result.
- **mutation**: Return byte write-back additional error data (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0011

[patch](patches/P-0011-4829704c9461.patch)
SHA-256: 4829704c94612c157fe3baa074c41c65812f8182a3b83e232e2f371d14f91088

### VP-0011: FTP legacy constants have been changed in value, but the internal mapping remains unchanged.

- **requirement**: Legacy type constants can still be imported with unchanged values
- **mutation**: FTP legacy constants have been changed in value, but the internal mapping remains unchanged. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0012

[patch](patches/P-0012-4d73a10e37c9.patch)
SHA-256: 4d73a10e37c9626a87569e748bc1ec6c258ef03edff3a0de67ba051a58dd969f

### VP-0012: Zip-compatible tuples are converted to lists.

- **requirement**: Third parties can still read the original zip archive/member status
- **mutation**: Zip-compatible tuples are converted to lists. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0013

[patch](patches/P-0013-539a3f73d56c.patch)
SHA-256: 539a3f73d56c7dd885f7a82b0c8da15adf012197ed6995f0795d389bc6cc303f

### VP-0013: Delete missing temporary files

- **requirement**: Delete its temporary files.
- **mutation**: Delete missing temporary files (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0014

[patch](patches/P-0014-5ae933f9646b.patch)
SHA-256: 5ae933f9646b27a52c56df642707320a0370919eb1a321a2cdca0455bfc9aee2

### VP-0014: New writable kind setter

- **requirement**: New type query remains read-only
- **mutation**: New writable kind setter (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0015

[patch](patches/P-0015-624158f38ff6.patch)
SHA-256: 624158f38ff61103a0b38d8f07b99178d2dd11105ca2a03964bb97a366ea084d

### VP-0015: Reopen flow due to local stream repeated calls

- **requirement**: Reuse the acquired handle from get_file
- **mutation**: Reopen flow due to local stream repeated calls (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0016

[patch](patches/P-0016-6bc76d5020b2.patch)
SHA-256: 6bc76d5020b2416b4cc68d703e2c305244f073af91a5eb3d7e74114e4b7347d8

### VP-0016: The temporary path content will not be copied again.

- **requirement**: get_local_filename provides the original local path or a temporary path that can be used by plugins.
- **mutation**: The temporary path content will not be copied again. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0017

[patch](patches/P-0017-797dba47b47c.patch)
SHA-256: 797dba47b47c2990d348b852622404d68b135f56d6797d15f9cd5f70e6d39669

### VP-0017: Corrupt the write-back to the caller's temporary output.

- **requirement**: Finish writing the temporary output back to the original caller's file.
- **mutation**: Corrupt the write-back to the caller's temporary output. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0018

[patch](patches/P-0018-7ee8c14194fb.patch)
SHA-256: 7ee8c14194fba9e625f6e16b8bf55a52ec90092e4de34acf02e54142d6401987

### VP-0018: Make directory call sites depend on private numeric values again.

- **requirement**: Replace calls based on type judgments with common semantic queries
- **mutation**: Make directory call sites depend on private numeric values again. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0019

[patch](patches/P-0019-9342325b10ba.patch)
SHA-256: 9342325b10ba7485e426a6c8d2c341f5cf12523f036dc1213cba206f986d6a21

### VP-0019: Create temporary files in advance for resource construction

- **requirement**: Construct resource objects without generating additional I/O or temporary files in advance.
- **mutation**: Create temporary files in advance for resource construction (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0020

[patch](patches/P-0020-9a69cc0b2741.patch)
SHA-256: 9a69cc0b2741ae6ff23bbb88849ce7eb4068efdd2ad5498e6620db6c47f00cdb

### VP-0020: HTTP ignore existing environment timeout handling

- **requirement**: Normal HTTP(S) read retains the general handle and existing timeout configuration.
- **mutation**: HTTP ignore existing environment timeout handling (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0021

[patch](patches/P-0021-9f93d9f41318.patch)
SHA-256: 9f93d9f413185b1106a101062ea8b0500ee3c70b9a273618be2afd95c4815cfb

### VP-0021: Compatible with digital surface zeroing, resource mechanism unaffected

- **requirement**: Third parties can still access the original digital resource types
- **mutation**: Compatible with digital surface zeroing, resource mechanism unaffected (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0022

[patch](patches/P-0022-a84176d3eb70.patch)
SHA-256: a84176d3eb70bc0ce276e889c4bfab3c4e4c2318f5a1c85b6c77e4d50d056e2b

### VP-0022: Missing own handle closure

- **requirement**: Close the resources owned by the request.
- **mutation**: Missing own handle closure (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0023

[patch](patches/P-0023-a876d584baad.patch)
SHA-256: a876d584baad66d0ff282f27bdabfd450f966681d0f1d2852d615e478c5db93d

### VP-0023: File URI slicing is off by one.

- **requirement**: The listed URIs/object inputs continue to receive existing classification and path explanations.
- **mutation**: File URI slicing is off by one. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0024

[patch](patches/P-0024-b1d45e4b9961.patch)
SHA-256: b1d45e4b9961b031bfd02e60c101f6f2d28bd2dded22c7109cefd5fd4ac09583

### VP-0024: Standard Image Only Read/Write Error Type Change

- **requirement**: Existing read-only target write failure retains the entry and type.
- **mutation**: Standard Image Only Read/Write Error Type Change (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0025

[patch](patches/P-0025-be0ad1a9a5c9.patch)
SHA-256: be0ad1a9a5c97de76d972a5b9bdc8084b5c5ec5a963743683834b66a2e9d1fff

### VP-0025: All inquiries about false bytes are false.

- **requirement**: Public and documented type queries accurately describe existing resources
- **mutation**: All inquiries about false bytes are false. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0026

[patch](patches/P-0026-c4b0c59c5c4b.patch)
SHA-256: c4b0c59c5c4b7707d646137e75101a5945dcbf39bdbc7072f22f351f45655d96

### VP-0026: Header length error 128

- **requirement**: Firstbytes maintains lazy header reading and stream position semantics
- **mutation**: Header length error 128 (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0027

[patch](patches/P-0027-861f4fb5609b.patch)
SHA-256: 861f4fb5609bbb6d85256505ce4f2d5dffd53ce8dd1e67eda9ca60138cb71fb5

### VP-0027: The finish function returns True instead of None, but the cleanup actions are still executed.

- **requirement**: The finish function returns True instead of None, and the cleanup actions are still executed (violating the requirement to maintain the original task's behavior).
- **mutation**: The finish function returns True instead of None, but the cleanup actions are still executed.
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry must be effectively rejected; an ineffective execution cannot be considered a success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Unupdated consumers/stub

## P-0028

[patch](patches/P-0028-caec6bc89b2b.patch)
SHA-256: caec6bc89b2b099b8af8adcf44632a19375055992c36770b3c9483f0933e7320

### VP-0028: The zip file was written back after being tampered with.

- **requirement**: Finish writing the cached output back to the original zip member.
- **mutation**: The zip file was written back after being tampered with. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0029

[patch](patches/P-0029-d0bc55c0f479.patch)
SHA-256: d0bc55c0f4796e239fa9e5895960b815d1aefa787f36b434d2956a15f0bed087

### VP-0029: The raw_uri is forced to a string, destroying the original object's identity.

- **requirement**: The plugin still receives the original Request metadata.
- **mutation**: The raw_uri is forced to a string, destroying the original object's identity. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0030

[patch](patches/P-0030-d4c98f4e633f.patch)
SHA-256: d4c98f4e633fe1502673fc2b0f6892726d9ad8cb083f7629e158a7e331e26bc3

### VP-0030: The reading result will no longer be consumed.

- **requirement**: get_result maintains the return status of the consumption result.
- **mutation**: The reading result will no longer be consumed. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0031

[patch](patches/P-0031-d84d332a3cde.patch)
SHA-256: d84d332a3cdeb9415c9da3edee239c09c1497783f82ed62736160f9f1e062a7b

### VP-0031: Move only the destination write-back from the resource back into Request's numeric dispatch.

- **requirement**: The resource object is responsible for writing back to the original destination.
- **mutation**: Move only the destination write-back from the resource back into Request's numeric dispatch. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0032

[patch](patches/P-0032-e13cb2f29785.patch)
SHA-256: e13cb2f29785707392e76a5e3d710b0121f2fe77ae365fd9c5f5e1b5c89b1d2b

### VP-0032: Restore the get_file responsibility to the Request number branch

- **requirement**: Each resource object is responsible for opening a connection. The Request delegate is used to obtain the resource handle.
- **mutation**: Restore the get_file responsibility to the Request number branch (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0033

[patch](patches/P-0033-e50bcc30f9bc.patch)
SHA-256: e50bcc30f9bcb6d6a6e4b30bb76e1a5cb907ee76536d6f83f15a4b84e498b264

### VP-0033: Early rejection of explicit plugin directory processing opportunities

- **requirement**: The explicit plugin still has a chance to process the directory.
- **mutation**: Early rejection of explicit plugin directory processing opportunities (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0034

[patch](patches/P-0034-fe2f1c28cd9f.patch)
SHA-256: fe2f1c28cd9ff93eac10d6d9b9349a2a1a35481773603d7777485e4a3d3be7ed

### VP-0034: Close the cleanup code and move it back to the Request. The resources will still be written back.

- **requirement**: Release the associated handles and temporary resources of the resource object.
- **mutation**: Close the cleanup code and move it back to the Request. The resources will still be written back. (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

## P-0035

[patch](patches/P-0035-fe8ffb641be7.patch)
SHA-256: fe8ffb641be773250ff0cf6cb386c99cf54cf6e2e1aab2864f14f04fd301f96c

### VP-0035: FTP increase handle capability

- **requirement**: FTP read keeps the handle empty and does not add new resource access.
- **mutation**: FTP increase handle capability (changed files: imageio/core/__init__.py, imageio/core/imopen.py, imageio/core/request.py, imageio/core/request.pyi, among others)
- **setup**: Apply this patch to the clean baseline at 319335265d29, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not count this as an expected pass
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure failure

