# Adversarial patches and verification points

Task: refactor-notesmd-cli-note-operation-04
Base commit: 58830c82327b8b34f8e5d52e5a3a7cfa0ad0ab5a

This package contains 33 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-0095237bb967.patch)
SHA-256: 0095237bb9672714f75456a2f771a0ec5f65e83f56b839d640882ffa0c953d75

### VP-0001: Mask the original parsing or read error.

- **requirement**: Mask the original parsing or read error.
- **mutation**: Mask the original parsing or read error. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0002

[patch](patches/P-0002-06570bdf82ae.patch)
SHA-256: 06570bdf82aed07deb78b9504b2b56a0c508671133c36d98f54e7bb130bbc416

### VP-0002: Format adds an extra newline.

- **requirement**: Format adds an extra newline.
- **mutation**: Format adds an extra newline. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0003

[patch](patches/P-0003-0b5f2a73ce2d.patch)
SHA-256: 0b5f2a73ce2ddd04639ba6350cacfbe34146cc923c9cd67cde027b39287fd65b

### VP-0003: No longer deleting existing keys

- **requirement**: No longer deleting existing keys
- **mutation**: No longer deleting existing keys (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0004

[patch](patches/P-0004-0ca2bec0b568.patch)
SHA-256: 0ca2bec0b5688a53b77f861e85456e4fcecea077e196ca5ff1d3729c820a9044

### VP-0004: Let the second serialization/layout implementation be removed

- **requirement**: Let the second serialization/layout implementation be removed
- **mutation**: Let the second serialization/layout implementation be removed (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0006

[patch](patches/P-0006-16c76c8bea6c.patch)
SHA-256: 16c76c8bea6c721c88e1edcbf0788fbd75764fac02c024b501ee513bd6ca8259

### VP-0006: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13.

- **requirement**: The F1P assertion failed and resulted in 12/13; a valid closure should be accepted.
- **mutation**: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not pass if the outer exit is 0
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Inconsistent patch hash; The actual testing collection or running environment is not completed.

### VP-0007: The selected boolean value will be placed back in the edit path for distribution.

- **requirement**: The selected boolean value will be placed back in the edit path for distribution.
- **mutation**: The selected boolean value will be placed back in the edit path for distribution. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0007

[patch](patches/P-0007-2274abe5dfae.patch)
SHA-256: 2274abe5dfae056bb2d7817a98d27ce99dd1d282da559f66d9c5380f53a50683

### VP-0008: Move loaded content to package global instead of operation context

- **requirement**: Move loaded content to package global instead of operation context
- **mutation**: Move loaded content to package global instead of operation context (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0008

[patch](patches/P-0008-35131c097070.patch)
SHA-256: 35131c0970702a9c950530e6e46122cd2f6d19363e3c52ec5ceb145948c4870c

### VP-0009: No frontmatter error in print.

- **requirement**: No frontmatter error in print.
- **mutation**: No frontmatter error in print. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0010

[patch](patches/P-0010-3d6e49740b73.patch)
SHA-256: 3d6e49740b730cf269f44dad8e64c463444213b919b72f5db79a1e5fb68ba73d

### VP-0011: edit duplicate writing

- **requirement**: edit duplicate writing
- **mutation**: edit duplicate writing (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0011

[patch](patches/P-0011-46b8e1fd017d.patch)
SHA-256: 46b8e1fd017dcb08fcec7f1e338fbc5a6083eae5f482a1bb7e004160182cb8d0

### VP-0012: Change the single note command to a two-parameter version.

- **requirement**: Change the single note command to a two-parameter version.
- **mutation**: Change the single note command to a two-parameter version. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go, cmd/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0012

[patch](patches/P-0012-494c60245d8d.patch)
SHA-256: 494c60245d8d185683750ae6b59af6b4e01194798bf00cbd8d131deaf7250090

### VP-0013: No operation returns before the name/path/read is performed.

- **requirement**: No operation returns before the name/path/read is performed.
- **mutation**: No operation returns before the name/path/read is performed. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0013

[patch](patches/P-0013-4ac56eef6d7f.patch)
SHA-256: 4ac56eef6d7f25f147be322131309ab9328257956c35caff904748ac0c48b550

### VP-0014: delete duplicate writes

- **requirement**: delete duplicate writes
- **mutation**: delete duplicate writes (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0015

[patch](patches/P-0015-57f7df039f1a.patch)
SHA-256: 57f7df039f1a52105c76306d88ad364d1cfec9736b10c918a04e69d01d33da0e

### VP-0016: print swallows the parse error.

- **requirement**: print swallows the parse error.
- **mutation**: print swallows the parse error. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0016

[patch](patches/P-0016-59f5a3ee07a3.patch)
SHA-256: 59f5a3ee07a326c2c5f6ecad144da98b273862d309d834d4ab2a2e9aafd9f565

### VP-0017: Parse lost text

- **requirement**: Parse lost text
- **mutation**: Parse lost text (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0017

[patch](patches/P-0017-6338591b397f.patch)
SHA-256: 6338591b397f4d89783fe82cd783ad27f78aa8a589e99203f3d1f84328c8a1e4

### VP-0018: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13.

- **requirement**: The F1P assertion failed and resulted in 12/13; a valid closure should be accepted.
- **mutation**: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not pass if the outer exit is 0
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Inconsistent patch hash; The actual testing collection or running environment is not completed.

### VP-0019: Delete the final key to clear all, not just the leading newline

- **requirement**: Delete the final key to clear all, not just the leading newline
- **mutation**: Delete the final key to clear all, not just the leading newline (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0018

[patch](patches/P-0018-672ba169211e.patch)
SHA-256: 672ba169211ecc799adef6661d0b92befcdf29f6a2943265f73e9dce89b13ab7

### VP-0020: Turning an empty sequence into an empty string element

- **requirement**: Turning an empty sequence into an empty string element
- **mutation**: Turning an empty sequence into an empty string element (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0019

[patch](patches/P-0019-684c0dd05373.patch)
SHA-256: 684c0dd05373d9d47f2b9b6cf90cae9b1b249afdb41f7e99ed5906e526fe314d

### VP-0021: Incorrectly convert numeric-looking text to a number. Use 123, the example specified in the task.

- **requirement**: Incorrectly convert numeric-looking text to a number. Use 123, the example specified in the task.
- **mutation**: Incorrectly convert numeric-looking text to a number. Use 123, the example specified in the task. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0020

[patch](patches/P-0020-6ed88ef98bbf.patch)
SHA-256: 6ed88ef98bbf1cf70b0a00bffca3b162d8b8a45f0c498c729971d61ca44ea057

### VP-0022: false false

- **requirement**: false false
- **mutation**: false false (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0021

[patch](patches/P-0021-86ae17518bb3.patch)
SHA-256: 86ae17518bb385d39c98d002f2712b107e5eefc1b23d43e2daa2e96f4c7f6119

### VP-0023: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13.

- **requirement**: The F1P assertion failed and resulted in 12/13; a valid closure should be accepted.
- **mutation**: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not pass if the outer exit is 0
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Inconsistent patch hash; The actual testing collection or running environment is not completed.

### VP-0024: delete swallowed write error and returned success

- **requirement**: delete swallowed write error and returned success
- **mutation**: delete swallowed write error and returned success (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0022

[patch](patches/P-0022-915faa0ac2a2.patch)
SHA-256: 915faa0ac2a239e5b9129c3df53cbbdda67b80488d3b9498baef3839112916c4

### VP-0025: Create new frontmatter and lose the main text.

- **requirement**: Create new frontmatter and lose the main text.
- **mutation**: Create new frontmatter and lose the main text. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0023

[patch](patches/P-0023-9d4e89a9ada9.patch)
SHA-256: 9d4e89a9ada9a99b283562f45b7f10b14debe7c781395091ce3451281cda4c54

### VP-0026: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13.

- **requirement**: The F1P assertion failed and resulted in 12/13; a valid closure should be accepted.
- **mutation**: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not pass if the outer exit is 0
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Inconsistent patch hash; The actual testing collection or running environment is not completed.

### VP-0027: Incorrectly treat a non-nil empty map as missing frontmatter.

- **requirement**: Incorrectly treat a non-nil empty map as missing frontmatter.
- **mutation**: Incorrectly treat a non-nil empty map as missing frontmatter. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0024

[patch](patches/P-0024-9e1408a26ab8.patch)
SHA-256: 9e1408a26ab8ca5edf79bdad3f4b6d3402d5ee1ede15699c09b95897f549f6c3

### VP-0028: Rebuild Layout with additional empty lines

- **requirement**: Rebuild Layout with additional empty lines
- **mutation**: Rebuild Layout with additional empty lines (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0025

[patch](patches/P-0025-140916758118.patch)
SHA-256: 1409167581183aee0e36c60b1aae2f490052359c8e24d9a38e15f8e65ddf4e4d

### VP-0029: Error in using the deletion prefix for the edit success message

- **requirement**: Error in using the deletion prefix for the edit success message
- **mutation**: Error in using the deletion prefix for the edit success message
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry should generate a complete and valid rejection score; failure in execution, compilation, or collection does not count as success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Inconsistent patch hash; The actual testing collection or running environment is not completed.

### VP-0030: Error in using the deletion prefix for the edit success message

- **requirement**: Error in using the deletion prefix for the edit success message
- **mutation**: Error in using the deletion prefix for the edit success message
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry should generate a complete and valid rejection score; failure in execution, compilation, or collection does not count as success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The ownership or ability of the context is missing. The shared transformation is broken

## P-0026

[patch](patches/P-0026-a9c1fe73b9c9.patch)
SHA-256: a9c1fe73b9c96d1854f9b0abe8c1d59bd8d7cb1241198b194116893c2a8c4e95

### VP-0031: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13.

- **requirement**: The F1P assertion failed and resulted in 12/13; a valid closure should be accepted.
- **mutation**: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not pass if the outer exit is 0
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Inconsistent patch hash; The actual testing collection or running environment is not completed.

### VP-0032: HasFrontmatter no longer calls TrimSpace on the first line.

- **requirement**: HasFrontmatter no longer calls TrimSpace on the first line.
- **mutation**: HasFrontmatter no longer calls TrimSpace on the first line. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0027

[patch](patches/P-0027-aa9171bce4d4.patch)
SHA-256: aa9171bce4d431c890190d0cbbc77007a6a48f31a1c6fd5a54e7cd081b6a4f56

### VP-0033: delete Swallow True Parsing Error

- **requirement**: delete Swallow True Parsing Error
- **mutation**: delete Swallow True Parsing Error (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0028

[patch](patches/P-0028-af021ba49595.patch)
SHA-256: af021ba49595ba31d67892c9c860b1b7aada2735a22d3410e735c69149d62f0d

### VP-0034: Print Leak Body

- **requirement**: Print Leak Body
- **mutation**: Print Leak Body (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0030

[patch](patches/P-0030-b8619e1ad1fe.patch)
SHA-256: b8619e1ad1fe566e0598c805d93c06b27a1b1e194c5eeb6aba6d566091c77518

### VP-0036: Mask the original parsing or read error.

- **requirement**: Mask the original parsing or read error.
- **mutation**: Mask the original parsing or read error. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0032

[patch](patches/P-0032-c4dd0cb4c48b.patch)
SHA-256: c4dd0cb4c48be50ba524ed6b8810ebf210e2fd955ed99170326c87174c0c5c86

### VP-0038: edit swallowed the error and returned success.

- **requirement**: edit swallowed the error and returned success.
- **mutation**: edit swallowed the error and returned success. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0033

[patch](patches/P-0033-cbd5633cbd87.patch)
SHA-256: cbd5633cbd87b272315a2c758859195671d558d3b244e6d46f6c6155a2c8aa28

### VP-0039: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13.

- **requirement**: The F1P assertion failed and resulted in 12/13; a valid closure should be accepted.
- **mutation**: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not pass if the outer exit is 0
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Inconsistent patch hash; The actual testing collection or running environment is not completed.

### VP-0040: edit swallow real parsing error

- **requirement**: edit swallow real parsing error
- **mutation**: edit swallow real parsing error (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0034

[patch](patches/P-0034-df47fcc07da3.patch)
SHA-256: df47fcc07da32a4736072f734cdbfa0ce75bd5b275a6827afe4ef9da05bc6179

### VP-0041: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13.

- **requirement**: The F1P assertion failed and resulted in 12/13; a valid closure should be accepted.
- **mutation**: Targeted regression: The appropriate 1 F2P assertion failed and got 12/13. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go, cmd/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Do not pass if the outer exit is 0
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Inconsistent patch hash; The actual testing collection or running environment is not completed.

### VP-0042: edit flag error binding print variable, keep the short name of the flag

- **requirement**: edit flag error binding print variable, keep the short name of the flag
- **mutation**: edit flag error binding print variable, keep the short name of the flag (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go, cmd/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0035

[patch](patches/P-0035-e31e51ee0a1d.patch)
SHA-256: e31e51ee0a1d920e6d1a3c6d1793524956d6d15a8e6e4e2cd78df96fbc8c64fa

### VP-0043: Make edit override print

- **requirement**: Make edit override print
- **mutation**: Make edit override print (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0036

[patch](patches/P-0036-e843ee465616.patch)
SHA-256: e843ee465616afd6e08e698706c503331d22c9749cf68462de5d9346552a3882

### VP-0044: SetKey replaces the entire map, discarding the remaining keys.

- **requirement**: SetKey replaces the entire map, discarding the remaining keys.
- **mutation**: SetKey replaces the entire map, discarding the remaining keys. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0037

[patch](patches/P-0037-ebb7ec5a475c.patch)
SHA-256: ebb7ec5a475cb4f448592587bce2e83080aaf222132b7d2686e986e43fdea00e

### VP-0045: List elements without surrounding spaces

- **requirement**: List elements without surrounding spaces
- **mutation**: List elements without surrounding spaces (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

## P-0038

[patch](patches/P-0038-f7eb5d4c4ceb.patch)
SHA-256: f7eb5d4c4ceb5552eda1b27c5a1586bbb995fc972029e7fd0613fe5cd659b105

### VP-0046: Mask the original parsing or read error.

- **requirement**: Mask the original parsing or read error.
- **mutation**: Mask the original parsing or read error. (changed files: pkg/actions/frontmatter.go, pkg/frontmatter/frontmatter.go)
- **setup**: Apply this patch to the clean baseline at 58830c82327b, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The faulty implementation must fail at least one relevant test or violate an API type contract
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target fails only because of an unrelated compilation, dependency, or test collection error

