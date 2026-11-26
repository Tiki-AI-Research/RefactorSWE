# Adversarial patches and verification points

Task: spr-git-commit-id-05
Base commit: 0767a458e50fa1f7ae203b73e50298ab201c80bb

This package contains 11 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-7ae16f002622.patch)
SHA-256: 7ae16f0026220bc10c0558166ce67ead799aeeda003ada39e5ac07a84433861a

### VP-0001: GraphQL parsing error rejecting empty identifiers

- **requirement**: GraphQL parsing error rejecting empty identifiers
- **mutation**: The above directed behavior defects are injected into the candidate implementation in git/commitid.go; the scoring tests are not modified.
- **setup**: Apply the complete candidate after running the original tests/test.sh on the clean baseline 0767a458e50fa1f7ae203b73e50298ab201c80bb.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0002

[patch](patches/P-0002-3e7d552f9617.patch)
SHA-256: 3e7d552f9617848901557d571d87747dec5bf2e60203f0f69a2c77d833971872

### VP-0002: Local commit-id error, truncated to seven digits

- **requirement**: Local commit-id error, truncated to seven digits
- **mutation**: The above directed behavior defects are injected into the candidate implementation in git/commitid.go; the scoring tests are not modified.
- **setup**: Apply the complete candidate after running the original tests/test.sh on the clean baseline 0767a458e50fa1f7ae203b73e50298ab201c80bb.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0003

[patch](patches/P-0003-4fd0b5898534.patch)
SHA-256: 4fd0b5898534daf0ef471759c059ced9883487e6cb14006dfa7e4e882e471b0e

### VP-0003: Local commit-id error acceptance in uppercase hexadecimal

- **requirement**: Local commit-id error acceptance in uppercase hexadecimal
- **mutation**: The above directed behavior defects are injected into the candidate implementation in git/commitid.go; the scoring tests are not modified.
- **setup**: Apply the complete candidate after running the original tests/test.sh on the clean baseline 0767a458e50fa1f7ae203b73e50298ab201c80bb.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0004

[patch](patches/P-0004-30f81cbeb6b5.patch)
SHA-256: 30f81cbeb6b51b1faa6665f970e1a5b65897bbc76af5eced756466cee8476a78

### VP-0004: Local commit-id rejects the valid blanks after a colon.

- **requirement**: Local commit-id rejects the valid blanks after a colon.
- **mutation**: The above directed behavior defects are injected into the candidate implementation in git/commitid.go; the scoring tests are not modified.
- **setup**: Apply the complete candidate after running the original tests/test.sh on the clean baseline 0767a458e50fa1f7ae203b73e50298ab201c80bb.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0005

[patch](patches/P-0005-4569a42c2be1.patch)
SHA-256: 4569a42c2be181cdcbbbe01e490116b9f5a22f469c1bfe2fc6839b434b4ba1f4

### VP-0005: Local commit-id error rejection eight-digit identifier text

- **requirement**: Local commit-id error rejection eight-digit identifier text
- **mutation**: The above directed behavior defects are injected into the candidate implementation in git/commitid.go; the scoring tests are not modified.
- **setup**: Apply the complete candidate after running the original tests/test.sh on the clean baseline 0767a458e50fa1f7ae203b73e50298ab201c80bb.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0006

[patch](patches/P-0006-3a58da366855.patch)
SHA-256: 3a58da3668557cb9b9857c3b8bec03f4a04455c3d240dc380b838995c9325c27

### VP-0006: The GraphQL identifier has been incorrectly removed of leading and trailing spaces.

- **requirement**: The GraphQL identifier has been incorrectly removed of leading and trailing spaces.
- **mutation**: The above directed behavior defects are injected into the candidate implementation in git/commitid.go; the scoring tests are not modified.
- **setup**: Apply the complete candidate after running the original tests/test.sh on the clean baseline 0767a458e50fa1f7ae203b73e50298ab201c80bb.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0007

[patch](patches/P-0007-61fa3a0dc7c6.patch)
SHA-256: 61fa3a0dc7c6a4f63333054181afdd9ddaea7175bd2063c7bc6748bbe2ccabaa

### VP-0007: GraphQL identifier error includes the text after the second colon

- **requirement**: GraphQL identifier error includes the text after the second colon
- **mutation**: The above directed behavior defects are injected into the candidate implementation in git/commitid.go; the scoring tests are not modified.
- **setup**: Apply the complete candidate after running the original tests/test.sh on the clean baseline 0767a458e50fa1f7ae203b73e50298ab201c80bb.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0008

[patch](patches/P-0008-2ec9fb1d818e.patch)
SHA-256: 2ec9fb1d818e5797fcbc302ca93dd196be0c06a0652233270aa2a88f8e3f7017

### VP-0008: GraphQL consumer error: strict resolver call

- **requirement**: GraphQL consumer error: strict resolver call
- **mutation**: The above targeted behavior defects are only injected into the candidate implementation in github/githubclient/client.go; the scoring tests are not modified.
- **setup**: Apply the complete candidate after running the original tests/test.sh on the clean baseline 0767a458e50fa1f7ae203b73e50298ab201c80bb.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0009

[patch](patches/P-0009-5184e301ebad.patch)
SHA-256: 5184e301ebad38ca2287fa383526449d6fa1fbe16459795c5ee4a5db54404391

### VP-0009: commit-id formatting error with space insertion

- **requirement**: commit-id formatting error with space insertion
- **mutation**: The above directed behavior defects are injected into the candidate implementation in git/commitid.go; the scoring tests are not modified.
- **setup**: Apply the complete candidate after running the original tests/test.sh on the clean baseline 0767a458e50fa1f7ae203b73e50298ab201c80bb.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0010

[patch](patches/P-0010-3846a384defc.patch)
SHA-256: 3846a384defcebf177fe4766aaeada95e6272e30ccf666d0613f3ffe2be1c19d

### VP-0010: Single-line commit loss requires additional line breaks.

- **requirement**: Single-line commit loss requires additional line breaks.
- **mutation**: The above targeted behavior defects are injected into the cmd/reword/main.go of the candidate implementation; the scoring tests are not modified.
- **setup**: Apply the complete candidate after running the original tests/test.sh on the clean baseline 0767a458e50fa1f7ae203b73e50298ab201c80bb.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0011

[patch](patches/P-0011-9934b9c89503.patch)
SHA-256: 9934b9c89503ce9c5e7304848d09d41b87c5f684b6c91d73110101f1d4b6b16a

### VP-0011: Memory Git Proxy lost identification line indentation

- **requirement**: Memory Git Proxy lost identification line indentation
- **mutation**: The above directed behavior defects are injected into the candidate implementation's git/mockgit/mockgit.go; the scoring tests are not modified.
- **setup**: Apply the complete candidate after running the original tests/test.sh on the clean baseline 0767a458e50fa1f7ae203b73e50298ab201c80bb.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

