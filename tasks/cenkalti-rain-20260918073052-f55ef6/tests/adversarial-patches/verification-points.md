# Adversarial patches and verification points

Task: cenkalti-rain-20260918073052-f55ef6
Base commit: 697380ffec04290679230d8d04636eb41c99e0a8

This package contains 11 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-88f32fd08de4.patch)
SHA-256: 88f32fd08de4a28126fd0ef9c7fafb48bf23c8d25f743a22dbbe6d60edf918c0

### VP-0001: No RPC close budget reserved with a 100ms safety margin

- **requirement**: No RPC close budget reserved with a 100ms safety margin
- **mutation**: The above-mentioned directed behavior defects are injected into the torrent/session.go in the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline 697380ffec04290679230d8d04636eb41c99e0a8.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0002

[patch](patches/P-0002-7bc04d2595b2.patch)
SHA-256: 7bc04d2595b243545818b9b25d2d8dc3b3042b4a95caeeb17f2a85a09cc7f1d7

### VP-0002: The RPC service does not wait for ongoing requests when it is shut down.

- **requirement**: When the session is closed, the RPC service should wait within the graceful shutdown window until all ongoing requests are completed before exiting.
- **mutation**: The complete implementation is the same as the reference implementation. Only the logic for stopping the RPC service, which currently has if active > 0, is changed to if false && active > 0. This allows skipping the waiting for ongoing requests. (changed files: torrent/session_rpc_server.go, among others)
- **setup**: Apply this patch (full implementation) on the clean baseline (commit 697380ffec04), and then run the tests/test.sh provided with the task for official scoring.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: There are ongoing RPC requests when closing.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0004

[patch](patches/P-0004-37ea9d13495b.patch)
SHA-256: 37ea9d13495b604f1d88f3516e25c4e0d6b0d8f1690616a93b1f52eaa2619099

### VP-0005: RPC internal budget error has been expanded to a timeout of 250ms

- **requirement**: RPC internal budget error has been expanded to a timeout of 250ms
- **mutation**: The above-mentioned directed behavior defects are injected into the torrent/session.go in the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline 697380ffec04290679230d8d04636eb41c99e0a8.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0005

[patch](patches/P-0005-74eb47062c53.patch)
SHA-256: 74eb47062c5358b85aca0fb107c31ce96530509093415a4d39db4bae46299aa0

### VP-0006: Total closing budget for the activity torrent does not reserve a safety margin.

- **requirement**: Total closing budget for the activity torrent does not reserve a safety margin.
- **mutation**: The above-mentioned directed behavior defects are injected into the torrent/session.go in the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline 697380ffec04290679230d8d04636eb41c99e0a8.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0006

[patch](patches/P-0006-a2cba9ef3c12.patch)
SHA-256: a2cba9ef3c12f3d4f1de33032ca5f4a635c1a025d6260fd33f4076f6a6c38bdc

### VP-0007: Error in using the long overall shutdown budget when no active torrents

- **requirement**: Error in using the long overall shutdown budget when no active torrents
- **mutation**: The above-mentioned directed behavior defects are injected into the torrent/session.go in the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline 697380ffec04290679230d8d04636eb41c99e0a8.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0007

[patch](patches/P-0007-b4c7e2c86cf3.patch)
SHA-256: b4c7e2c86cf34f7c71b5af5f3ee2c9db4200a517e8faedc9257ca8f2f0642540

### VP-0008: Error occurred when clearing the RPC deadline when querying the activity deadline.

- **requirement**: Error occurred when clearing the RPC deadline when querying the activity deadline.
- **mutation**: The above-mentioned directed behavior defects are injected into the torrent/session.go in the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline 697380ffec04290679230d8d04636eb41c99e0a8.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0008

[patch](patches/P-0008-2c6c1a331d7b.patch)
SHA-256: 2c6c1a331d7b0b7f4ea9752db6a72aa3bef024e78d566b4e2cd1d8a10e5c4def

### VP-0009: Close the deadline error report at the current time.

- **requirement**: Close the deadline error report at the current time.
- **mutation**: The above-mentioned directed behavior defects are injected into the torrent/session.go in the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline 697380ffec04290679230d8d04636eb41c99e0a8.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0009

[patch](patches/P-0009-534a86dbbe14.patch)
SHA-256: 534a86dbbe14731d97a115ee4dff89973a1455a6e28b8a35a1492a5d2651c162

### VP-0010: Ignore timer closure injection boundaries

- **requirement**: Ignore timer closure injection boundaries
- **mutation**: The above-mentioned directed behavior defects are injected into the torrent/session.go in the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline 697380ffec04290679230d8d04636eb41c99e0a8.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0010

[patch](patches/P-0010-3b4cbbd6be36.patch)
SHA-256: 3b4cbbd6be3617476f586065c291e9eb54cf6b327e742296579f262c22131e61

### VP-0011: worker completed boundary early report successfully

- **requirement**: worker completed boundary early report successfully
- **mutation**: The above-mentioned directed behavior defects are injected into the torrent/session.go in the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline 697380ffec04290679230d8d04636eb41c99e0a8.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0011

[patch](patches/P-0011-c2324dc0e344.patch)
SHA-256: c2324dc0e344c7bd5ab5e9924fa5d2a0e94ee73bf927b487110b66500a26990b

### VP-0012: Repetitive closing of lost cached errors

- **requirement**: Repetitive closing of lost cached errors
- **mutation**: The above-mentioned directed behavior defects are injected into the torrent/session.go in the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline 697380ffec04290679230d8d04636eb41c99e0a8.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0012

[patch](patches/P-0012-bcb73e11dda6.patch)
SHA-256: bcb73e11dda6607d57988e779cf6aea9a645970300b8de8f72468909d2b3a60c

### VP-0013: RPC Close Budget Safety Margin Error Reduced to 50ms

- **requirement**: RPC Close Budget Safety Margin Error Reduced to 50ms
- **mutation**: The above-mentioned directed behavior defects are injected into the torrent/session.go in the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline 697380ffec04290679230d8d04636eb41c99e0a8.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

