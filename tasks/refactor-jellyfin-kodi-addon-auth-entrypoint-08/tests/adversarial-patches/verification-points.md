# Adversarial patches and verification points

Task: refactor-jellyfin-kodi-addon-auth-entrypoint-08
Base commit: 9f2823a464f4f333affba462198b289766ebb137

This package contains 38 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-08df3809d109.patch)
SHA-256: 08df3809d1098f061373cf513e810b6fa18f452e48ec559bae7487da6798f29e

### VP-0001: Server name is injected, and the value for None is missing

- **requirement**: Server name is injected, and the value for None is missing
- **mutation**: Server name is injected, and the value for None is missing (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0002

[patch](patches/P-0002-1af07dbb2381.patch)
SHA-256: 1af07dbb2381c5d2eba7d8cf65c9f919d100113d66349d8f8ac50b2f115e977c

### VP-0002: Targeted regression: Normalize the local path separator.

- **requirement**: Normalize the local path separator.
- **mutation**: Targeted regression: Normalize the local path separator. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0003

[patch](patches/P-0003-1ba4005f4a26.patch)
SHA-256: 1ba4005f4a26ffc82f4e173135166ca753aa4f27a6e572339b1d01c0189ea882

### VP-0003: Reuse data when configuration remains unchanged, without reading each item separately

- **requirement**: Reuse data when configuration remains unchanged, without reading each item separately
- **mutation**: Reuse data when configuration remains unchanged, without reading each item separately (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0004

[patch](patches/P-0004-205cf3b280d8.patch)
SHA-256: 205cf3b280d8a9d03069a353fef417595de4f4700aea98c46e2fe94f41234293

### VP-0004: Targeted regression: If the explicit path is not provided, use item.Path.

- **requirement**: If the explicit path is not provided, use item.Path.
- **mutation**: Targeted regression: If the explicit path is not provided, use item.Path. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0005

[patch](patches/P-0005-259ee94194b2.patch)
SHA-256: 259ee94194b2d0084857798beea3fffc4f970642794e80a638be9d0ccd07b638

### VP-0005: Narrow change in jellyfin_kodi/jellyfin/configuration.py

- **requirement**: Retain the same loading value for the already configured addon in cache reuse.
- **mutation**: Narrow change in jellyfin_kodi/jellyfin/configuration.py (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0006

[patch](patches/P-0006-2f87cdde6832.patch)
SHA-256: 2f87cdde6832eb98b66f3fa000ae70bb3ffd06d5c6f62cea767a9294e1e4f489

### VP-0006: Server address injection with a missing value of None

- **requirement**: Server address injection with a missing value of None
- **mutation**: Server address injection with a missing value of None (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0007

[patch](patches/P-0007-3e5d8379d15f.patch)
SHA-256: 3e5d8379d15fcedac767ff4706eebcd68bfdfcd2d9976e55328d07a812d6e68b

### VP-0007: The optional artwork server continues to affect the image URLs.

- **requirement**: The optional artwork server continues to affect the image URLs.
- **mutation**: The optional artwork server continues to affect the image URLs. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0008

[patch](patches/P-0008-4483c0c7cdef.patch)
SHA-256: 4483c0c7cdeff18f1a85bacd105fe433442c98ae8cb1c34debed44acdedf2815

### VP-0008: Narrow change in jellyfin_kodi/objects/actions.py

- **requirement**: Actions retains the explicitly passed clients and existing construction shapes.
- **mutation**: Narrow change in jellyfin_kodi/objects/actions.py (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0009

[patch](patches/P-0009-4e4614c3bef0.patch)
SHA-256: 4e4614c3bef0ae9c970f3d69dc365034f1be25a7afc1670c2bf5b19ebe4fc0d8

### VP-0009: Injecting access token with missing value being None

- **requirement**: Injecting access token with missing value being None
- **mutation**: Injecting access token with missing value being None (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0010

[patch](patches/P-0010-517ef2a3f5ea.patch)
SHA-256: 517ef2a3f5ea4a35c7ace89267c83a8588f99eb43f82cd3f0ea39226a2f06438

### VP-0010: The existing accessor is still available for connection, path setting, and log calls.

- **requirement**: The existing accessor is still available for connection, path setting, and log calls.
- **mutation**: The existing accessor is still available for connection, path setting, and log calls. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0011

[patch](patches/P-0011-5181139179d0.patch)
SHA-256: 5181139179d0cbd84ee0d941b6175dd0bdcecb549aabea357d343983903167c6

### VP-0011: Preserve the existing result for paths that match no mapping.

- **requirement**: Preserve the existing result for paths that match no mapping.
- **mutation**: Preserve the existing result for paths that match no mapping. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0012

[patch](patches/P-0012-53e87a5123cc.patch)
SHA-256: 53e87a5123cc39eccf89a9b33f9913ed70ebeeea12f1b305bd4d2801d050f159

### VP-0012: Targeted regression: If the path is empty or missing, return an empty string.

- **requirement**: If the path is empty or missing, return an empty string.
- **mutation**: Targeted regression: If the path is empty or missing, return an empty string. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0013

[patch](patches/P-0013-61efbe0861c6.patch)
SHA-256: 61efbe0861c666c3c807e4a3a3ffc684c15eab5875cebf29663054ccb1ce4a54

### VP-0013: Configuration path mapping error: swapping the source path with the target path.

- **requirement**: Configuration path mapping error: swapping the source path with the target path (violating the original task's behavior requirements)
- **mutation**: Configuration path mapping error: swapping the source path with the target path.
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry must be effectively rejected; an ineffective execution cannot be considered a success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

### VP-0014: Configuration path mapping error: swapping the source path with the target path.

- **requirement**: Configuration path mapping error: swapping the source path with the target path (violating the original task's behavior requirements)
- **mutation**: Configuration path mapping error: swapping the source path with the target path.
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry must be effectively rejected; an ineffective execution cannot be considered a success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0014

[patch](patches/P-0014-64f2860f1db3.patch)
SHA-256: 64f2860f1db36688e9b62994b31ef07aa8be50465527778ec2d5ca4c8f152ca8

### VP-0015: Load and standardize to the communication layer configuration/credentials responsibility. Existing accessor delegates/multiple uses of it.

- **requirement**: Load and standardize to the communication layer configuration/credentials responsibility. Existing accessor delegates/multiple uses of it.
- **mutation**: Load and standardize to the communication layer configuration/credentials responsibility. Existing accessor delegates/multiple uses of it. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0015

[patch](patches/P-0015-681b4df901e5.patch)
SHA-256: 681b4df901e542ee9bb973e2282d48569ad5ccbe11d261c8c317d2d14d08b8b4

### VP-0016: File opening failed and propagated to higher levels.

- **requirement**: File opening failed and propagated to higher levels.
- **mutation**: File opening failed and propagated to higher levels. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0017

[patch](patches/P-0017-6f3d4b497884.patch)
SHA-256: 6f3d4b4978844ccc4063c3e5ee18b4d8a56207affd433d6a0c4326fefa528e5c

### VP-0018: Targeted regression: dvd container path suffix

- **requirement**: dvd container path suffix
- **mutation**: Targeted regression: dvd container path suffix (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0018

[patch](patches/P-0018-7066feca9112.patch)
SHA-256: 7066feca9112a74a58851d99cd714333827a8252d912e777f1d74a4f02c36c28

### VP-0019: Targeted regression: The mapping keys are still replaced according to the existing substrings in the path.

- **requirement**: The mapping keys are still replaced according to the existing substrings in the path.
- **mutation**: Targeted regression: The mapping keys are still replaced according to the existing substrings in the path. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0019

[patch](patches/P-0019-76ff3a325e3f.patch)
SHA-256: 76ff3a325e3f324b0fa01b802fbb334a9eac734c6cd6da82d42096acfd9fcc54

### VP-0020: Targeted regression: UNC path is continued to smb path

- **requirement**: UNC path is continued to smb path
- **mutation**: Targeted regression: UNC path is continued to smb path (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0020

[patch](patches/P-0020-7fb1ec70ed99.patch)
SHA-256: 7fb1ec70ed99ff0ba59f60f983718c0ed59143115684910cc8de598cfd590e3c

### VP-0021: item helper uses the first loaded server paths; an empty map is returned when not available.

- **requirement**: item helper uses the first loaded server paths; an empty map is returned when not available.
- **mutation**: item helper uses the first loaded server paths; an empty map is returned when not available. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0021

[patch](patches/P-0021-7076ee713116.patch)
SHA-256: 7076ee7131166929a53f332d2e2038741e8655b59943418a5675a33b1d2b2a30

### VP-0022: Action loading failed. Clear the existing auth.server rollback values.

- **requirement**: Action loading failed. Clearing existing auth.server rollback values (violating the original task's behavior requirement).
- **mutation**: Action loading failed. Clear the existing auth.server rollback values.
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry must be effectively rejected; an ineffective execution cannot be considered a success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0022

[patch](patches/P-0022-8f638706c470.patch)
SHA-256: 8f638706c4707b69521fd9517713591314fb88ab06cb2cde6ef5b3618cffada5

### VP-0023: The first storage record contains an injected parsed request server client.

- **requirement**: The first storage record contains an injected parsed request server client.
- **mutation**: The first storage record contains an injected parsed request server client. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0023

[patch](patches/P-0023-911a40b986ed.patch)
SHA-256: 911a40b986ed4399f9253fd3b1b985003535fcdc3a360c0fb670985520c10bf0

### VP-0024: Actions can be constructed without a client, either with no parameters or only a server ID. They are injected first and then read from the server.

- **requirement**: Actions can be constructed without a client, either with no parameters or only a server ID. They are injected first and then read from the server.
- **mutation**: Actions can be constructed without a client, either with no parameters or only a server ID. They are injected first and then read from the server. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0024

[patch](patches/P-0024-9afc04fa5fb9.patch)
SHA-256: 9afc04fa5fb9398be15dcd737fb496ab7d2b3b65b41c09b05a604735b743ed93

### VP-0025: Context listitem explicitly requested, storing two records

- **requirement**: Context listitem Explicitly requested, stores two records; Only error parsing default, checks target identity and four values
- **mutation**: Context listitem Explicitly requested, stores two records; Only error parsing default, checks target identity and four values (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0025

[patch](patches/P-0025-9afeb7d233ec.patch)
SHA-256: 9afeb7d233ecb142dd03decd47382027939abb58136a9ce11e938bc1e1af2a26

### VP-0026: Warning: Loading input port failed/No server available. Continue with default settings.

- **requirement**: Warning: Loading input port failed/No server available. Continue with default settings.
- **mutation**: Warning: Loading input port failed/No server available. Continue with default settings. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0026

[patch](patches/P-0026-9bee6bdadd2e.patch)
SHA-256: 9bee6bdadd2ed8719a699b40387bdde4c8a55e7747d6a473382c0b312972823f

### VP-0027: Preserve the replacement output for paths that already match.

- **requirement**: Preserve the replacement output for paths that already match.
- **mutation**: Preserve the replacement output for paths that already match. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0027

[patch](patches/P-0027-ac0154ba13ca.patch)
SHA-256: ac0154ba13ca7f0beda6d7214711d66d8367c2c8668d8b44f3a7616eff10e944

### VP-0028: item helper retains one or two parameters for construction

- **requirement**: item helper retains one or two parameters for construction
- **mutation**: item helper retains one or two parameters for construction (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0028

[patch](patches/P-0028-acfd58730df6.patch)
SHA-256: acfd58730df697af8d8102bd6c040932245b0837f71e4bb0fc3879bfb1210854

### VP-0029: The missing Servers are still normalized to an empty list.

- **requirement**: The missing Servers are still normalized to an empty list.
- **mutation**: The missing Servers are still normalized to an empty list. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0029

[patch](patches/P-0029-adff7524325b.patch)
SHA-256: adff7524325bc832945a4a39d6cb34473aee5de127f65a684170662d077063b5

### VP-0030: Narrow change in jellyfin_kodi/jellyfin/configuration.py

- **requirement**: The cached configuration loaded cannot be skipped for subsequent client injection.
- **mutation**: Narrow change in jellyfin_kodi/jellyfin/configuration.py (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0030

[patch](patches/P-0030-b27792ef6ec4.patch)
SHA-256: b27792ef6ec434b8814690f2ef4b6a132e1732db74bf1893feb19c14a6c93848

### VP-0031: Narrow change in jellyfin_kodi/database/__init__.py

- **requirement**: The old address normalization for the storage accessor continues to be effective.
- **mutation**: Narrow change in jellyfin_kodi/database/__init__.py (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0031

[patch](patches/P-0031-b3dbf4bf9edb.patch)
SHA-256: b3dbf4bf9edb3196fb16995d935d7569b4b1239b627a1f9412003eaf98e2bc61

### VP-0032: Injecting user id and missing values as None

- **requirement**: Injecting user id and missing values as None
- **mutation**: Injecting user id and missing values as None (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0032

[patch](patches/P-0032-bea3d72d1a48.patch)
SHA-256: bea3d72d1a485b32b70d87fd446fa6fceb0b1c3ef591953d6fd58f43c5b5be5e

### VP-0033: Three authentication paths share a single credential injection entry point

- **requirement**: Three authentication paths share a single credential injection entry point
- **mutation**: Three authentication paths share a single credential injection entry point (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0033

[patch](patches/P-0033-cb3b468ad426.patch)
SHA-256: cb3b468ad42678ddb4936d8f62e40a3630960479cb61d4ae9e65eca1ecac931a

### VP-0034: File opened successfully without a server, with no warnings. Proceed.

- **requirement**: File opened successfully without a server, with no warnings. Proceed.
- **mutation**: File opened successfully without a server, with no warnings. Proceed. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0034

[patch](patches/P-0034-ccfcdaf27dd3.patch)
SHA-256: ccfcdaf27dd3698288ccbc2ae18d4c9910c1ef4c9e32a08c1c19bd29f59627be

### VP-0035: Targeted regression: bluray container path suffix

- **requirement**: bluray container path suffix
- **mutation**: Targeted regression: bluray container path suffix (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0035

[patch](patches/P-0035-da01354162a4.patch)
SHA-256: da01354162a4692a05fe1616561f8c9f201b4754c73d6f83799cc3a3fe25fc6c

### VP-0036: Completed injection before the first authentication request

- **requirement**: Completed injection before the first authentication request
- **mutation**: Completed injection before the first authentication request (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0036

[patch](patches/P-0036-defadbc71fe2.patch)
SHA-256: defadbc71fe22b7b35d5228eb96a0573639052563c8732684e52c303c14cfd20

### VP-0037: Targeted regression: Preserve the step that converts the protocol to lowercase.

- **requirement**: Preserve the step that converts the protocol to lowercase.
- **mutation**: Targeted regression: Preserve the step that converts the protocol to lowercase. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: narrow wrong candidate reaches same target and fails that assertion
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target not reached; patch apply/import/collection fails; candidate rejected before target tests; not all 61 actual nodes evaluated

## P-0038

[patch](patches/P-0038-e3e014dbade1.patch)
SHA-256: e3e014dbade1e985014e77a5078e66c275ae3b8cb23b41dcd867c486e7bb0144

### VP-0039: The first record lacks address but has valid values for the other four fields and paths.

- **requirement**: The first record lacks address but has valid values for the other four fields and paths. All three authentication entry points construct successfully, and auth.server must be None.
- **mutation**: The first record lacks address but has valid values for the other four fields and paths. All three authentication entry points construct successfully, and auth.server must be None. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0039

[patch](patches/P-0039-ef77cf95b36d.patch)
SHA-256: ef77cf95b36d0a65f99c71d763d2f60c2411f314b26c21b6f560eb3cf5af5973

### VP-0040: Two independent clients (default/requested), storing two records. Events are explicitly requested.

- **requirement**: Two independent clients (default/requested), storing two records. Events are explicitly requested; only default for incorrect parsing is allowed, and the target default client cannot be written.
- **mutation**: Two independent clients (default/requested), storing two records. Events are explicitly requested; only default for incorrect parsing is allowed, and the target default client cannot be written. (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

## P-0040

[patch](patches/P-0040-f297712f7302.patch)
SHA-256: f297712f73023482dba38fbfb463aed3c1ef8bdcb57130299c00887cd7f97146

### VP-0041: Complete injection before the broadcast input's first authentication request

- **requirement**: Complete injection before the broadcast input's first authentication request
- **mutation**: Complete injection before the broadcast input's first authentication request (changed files: jellyfin_kodi/database/__init__.py, jellyfin_kodi/entrypoint/context.py, jellyfin_kodi/entrypoint/default.py, jellyfin_kodi/helper/api.py, among others)
- **setup**: Apply this patch to the clean baseline at 9f2823a464f4, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Target State/Call Not Actually Reached; Application or test collection failed

