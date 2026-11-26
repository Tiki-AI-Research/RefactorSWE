# Adversarial patches and verification points

Task: labeler-match-dimensions-03
Base commit: 98ce1450c7908643084f7487327dfa4f4bf8a367

This package contains 30 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-0db0f285448e.patch)
SHA-256: 0db0f285448e2f93989bcc0d1ce96b6277006616fea9158c01a6b90951675e1b

### VP-0001: Clear the output for the newly added label.

- **requirement**: The new-labels still output the newly added tags in the final collection; the names remain new-labels, and the content is a comma-separated list of newly added tags in the existing order, subject to the truncation constraint of the original 100 tags.
- **mutation**: Clear the output for the newly added label. (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The content is the new labels joined by commas in their original order, subject to the existing 100-label limit. The run must be valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0002

[patch](patches/P-0002-1bcee98f5c84.patch)
SHA-256: 1bcee98f5c843ce312ba1ae0f055f8025541580d182bdfab6bb8df42182c3083

### VP-0002: Targeted regression: Preserve all-globs-to-any-file matching for the file dimension.

- **requirement**: Keep the file dimension in the all-globs-to-any-file format; it is required that all globs are satisfied in the same file, and it cannot be replaced by separate matches in different files.
- **mutation**: Targeted regression: Preserve all-globs-to-any-file matching for the file dimension. (changed files: src/changedFiles.ts, src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: It cannot be replaced with separate matches in different files; it is not an ineffective execution.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0003

[patch](patches/P-0003-1c574f53eb6b.patch)
SHA-256: 1c574f53eb6bb3e76735622584116a6c3f01d303c02e601ecfae39ff2eea786f

### VP-0003: Disable Synchronized Removal for Configured Tags

- **requirement**: sync-labels only synchronize the configured tags and remove the invalid tags in the existing way; the retained and removed sets under the enabled/disabled state of sync, as well as the directed removeLabels/addLabels calls
- **mutation**: Disable Synchronized Removal for Configured Tags (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: And the directed calls to removeLabels/addLabels; not invalid executions.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0004

[patch](patches/P-0004-2200d3b9e842.patch)
SHA-256: 2200d3b9e842c90cc12f97e49c754eeb16c3ec629898f14d28987d96d93ce764

### VP-0004: Error rejection when the new file tag equals the limit

- **requirement**: Changed-files-labels-limit applies to all new file types with a limit. If the limit is exceeded, no new file type labels will be added. If it equals the limit, existing labels will not be counted, and branch labels will continue to be applied.
- **mutation**: Error rejection when the new file tag equals the limit (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Equal is allowed. Tags are not counted. Branch tags continue to be applied; it is not an invalid execution.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0005

[patch](patches/P-0005-2279548da790.patch)
SHA-256: 2279548da790ad8592c26ef8bd5d99e55490fb43328057ac6fb90546a9041735

### VP-0005: Targeted regression: File dimensions should be kept in the any-glob-to-all-files format.

- **requirement**: Keep the file dimension in the 'any-glob-to-all-files' mode; it is necessary for the same glob to match all files, and scattered coverage cannot be used instead.
- **mutation**: Targeted regression: File dimensions should be kept in the any-glob-to-all-files format. (changed files: src/changedFiles.ts, src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: It cannot be replaced with scattered coverage; it is not an ineffective execution.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0006

[patch](patches/P-0006-244e0a2399df.patch)
SHA-256: 244e0a2399df68a08a24edc5eaa07f1eb022787f40f9d44137b3f3898ae91f57

### VP-0006: any incorrectly uses the all strategy.

- **requirement**: any returns true if any participating dimensions are successful, otherwise false; the boolean result of the success of the current entry and subsequent entries
- **mutation**: any incorrectly uses the all strategy. (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The run is valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0007

[patch](patches/P-0007-3133d595f405.patch)
SHA-256: 3133d595f40555dfce697a640e1c6490cd85cdeb6b5b28d087ffda630c5c552f

### VP-0007: The head dimension incorrectly uses the base ref.

- **requirement**: The head-branch still performs regular matching on the corresponding quantifiers for the head ref; when the base/head names are different and there are multiple regular expressions, the result follows the same matching rules as the head.
- **mutation**: The head dimension incorrectly uses the base ref. (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The results are consistent with the rules for matching the head; it is not an invalid execution.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0008

[patch](patches/P-0008-411030032b3e.patch)
SHA-256: 411030032b3eb5f1e52bba8900b00877a8459152f7fe01b0da1ef98c6a4e9030

### VP-0008: Targeted regression: File dimensions should be retained in the "any-glob-to-any-file" format.

- **requirement**: File dimension retains the any-glob-to-any-file pattern. This pattern is successful when a certain glob matches a certain file, and fails when there is no match.
- **mutation**: Targeted regression: File dimensions should be retained in the "any-glob-to-any-file" format. (changed files: src/changedFiles.ts, src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Failure when no matches found; Not an invalid execution
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0009

[patch](patches/P-0009-4535e2bfd9a7.patch)
SHA-256: 4535e2bfd9a7d12a6cf429fb910374f375c10d857e5aef1ad74d4aeedf0258aa

### VP-0009: Copy quantity operators, each entrance calls different copies

- **requirement**: Both quantifiers share a semantic and orchestration contract. Verify the actual call graph and ownership of the quantifier logic, including the absence of duplicate orchestration.
- **mutation**: Copy quantity operators, each entrance calls different copies; behavior remains the same but structure is incorrect (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The run is valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0010

[patch](patches/P-0010-48e5a13b2726.patch)
SHA-256: 48e5a13b272648e22d08c679dd97b4caba23e5d0647f8cca0d759ee4f6078077

### VP-0010: When the max threshold is reached, the error is skipped.

- **requirement**: Skip file-based labels above max-files-changed. Continue processing branch-only labels. At the threshold, process normally. Above it, neither add nor remove file-based labels, even when sync=true.
- **mutation**: When the max threshold is reached, the error is skipped. (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The file class remains unchanged if it exceeds the limit; even if sync=true is set, the pure branch still matches; it is not considered an invalid execution.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0011

[patch](patches/P-0011-4b95b8d0d94f.patch)
SHA-256: 4b95b8d0d94fc19646435b4e544f5bd366b4bcf9c4be236f4daaca19946d2c56

### VP-0011: Targeted regression: Preserve all-globs-to-all-files matching for the file dimension.

- **requirement**: Preserve all-globs-to-all-files matching. Every glob must match every file. A single mismatch fails the check.
- **mutation**: Targeted regression: Preserve all-globs-to-all-files matching for the file dimension. (changed files: src/changedFiles.ts, src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A mismatch means failure; not an invalid execution
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0012

[patch](patches/P-0012-51a246c9a015.patch)
SHA-256: 51a246c9a015e18475e905d6ddb256a8cbe2e22ae181be196d41fed5f372a1ce

### VP-0012: Reverse the output order of the four modes

- **requirement**: The keys and values of the four file modes are normalized, and the order of entries is maintained; the order of fields in the four camelCase modes, the results of string conversion to arrays, and the output arrays are also preserved.
- **mutation**: Reverse the output order of the four modes (changed files: src/changedFiles.ts, src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The run is valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0013

[patch](patches/P-0013-52a26804039d.patch)
SHA-256: 52a26804039d2b8951c6d852c2b667be79424c83fd5496e83aa5ed09dc418e66

### VP-0013: Reverse Dimension Evaluation and Debug Order

- **requirement**: Evaluate dimensions in the order of base, files, head, and maintain the debug sequence; no subsequent dimension calls or logs will be performed if any or all of the debug sequences fail.
- **mutation**: Reverse Dimension Evaluation and Debug Order (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Any success or no subsequent dimension calls and logs; not an invalid execution.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0014

[patch](patches/P-0014-53c3340c2367.patch)
SHA-256: 53c3340c2367a3b05e1b32f021902a7765f7d50416ae2eb9fdce8cbe105bd25b

### VP-0014: all empty block errors return true

- **requirement**: Return false for all empty blocks or completely empty entry blocks; the all result of [] and [] is false.
- **mutation**: all empty block errors return true (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The run is valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0015

[patch](patches/P-0015-12af1d77d8a0.patch)
SHA-256: 12af1d77d8a0247d6f5d9b411e93a037fbe0be89002e28ff11f0130e4a02c5f0

### VP-0015: The any quantifier returns true when no matches are found.

- **requirement**: The any quantifier returns true when no matches are found.
- **mutation**: The above targeted behavior defects are injected into the src/labeler.ts of the candidate implementation; the scoring test is not modified.
- **setup**: Apply the complete candidates after running the original tests/test.sh on the clean baseline 98ce1450c7908643084f7487327dfa4f4bf8a367.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The formal test should produce a valid score and reject the candidate; failure in compilation, application, collection, or invalid reports cannot be considered a success.
- **prerequisites**: None (Complete candidate from a clean baseline application)
- **version_note**: 2026-11-14 Add negative examples as required by users; change the positive examples that pass to negative ones; the verification result is subject to actual measurement results.
- **invalid_if**: The patch does not apply; Build or test collection failed; Running timeout or incomplete test nodes; The scoring report is invalid.

## P-0016

[patch](patches/P-0016-6d5acd64de3f.patch)
SHA-256: 6d5acd64de3f9edc15713f17133c79f19567003f6727f30d503e87c1e0d2d9e5

### VP-0016: Clear final tag output

- **requirement**: all-labels will still be output as the final set of planned tags; the name remains all-labels, including the existing retained tags and new tags added. The expired items are removed, and they are connected in the original order with the original truncation rules preserved.
- **mutation**: Clear final tag output (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Keep valid existing and new labels, drop stale ones, join them in the established order, and apply the original truncation rule. The run must be valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0017

[patch](patches/P-0017-6f39e6773ddc.patch)
SHA-256: 6f39e6773ddcfc0aa0b5210bb741439fc0b18c249efcff7e080d7fbed99af4bb

### VP-0017: The shared driver has three hardcoded registration items. The extended DIMENSIONS are no longer automatically connected.

- **requirement**: The three dimensions use a clear common access contract, so there is no need to modify the two quantities separately for extended dimensions; the declaration of the dimension set and the points of access modification are not limited to internal naming, files, or delegation forms.
- **mutation**: The shared driver has three hardcoded registration items. The extended DIMENSIONS are no longer automatically connected. (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: No restrictions on internal naming, file or delegation formats; it does not result in invalid execution.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0018

[patch](patches/P-0018-7237b011b24f.patch)
SHA-256: 7237b011b24f32380edbb7d129a829a8e3b5a426afe78d91631a1d59a6b3a6e0

### VP-0018: The unknown file key is no longer rejected

- **requirement**: The changed-files internal unknown keys continue to throw existing errors; The error type and the message content and order of the unknown keys.
- **mutation**: The unknown file key is no longer rejected (changed files: src/changedFiles.ts, src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The run is valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0019

[patch](patches/P-0019-773fd60a77e3.patch)
SHA-256: 773fd60a77e33c155a6180f4d3606ad09b9bf451490e551096fdab8f8f743119

### VP-0019: all misuse of any strategy

- **requirement**: all requires all participating dimensions and non-empty entries to be successful; if there is one failed dimension, it is false; if both are successful and there are empty entries, it is true.
- **mutation**: all misuse of any strategy (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: True when everything is successful and no empty entries are generated; otherwise false.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0020

[patch](patches/P-0020-81698cca6f34.patch)
SHA-256: 81698cca6f342d0325edfdcc4f1e63b3e69f911c47bde1f27656ee8e85647244

### VP-0020: The base dimension is incorrectly referenced by the head ref.

- **requirement**: The base-branch still performs regular matching on the corresponding quantifiers for the base ref; when the base/head names are different and there are multiple regular expressions, the result follows the same matching rules as the base.
- **mutation**: The base dimension is incorrectly referenced by the head ref. (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The results match the base matching rules; it is not an invalid execution.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0021

[patch](patches/P-0021-9db50b99dbb4.patch)
SHA-256: 9db50b99dbb44af0a4dcd38265156d0269add1b9475e644385163643a08205b3

### VP-0021: Discard dot option

- **requirement**: The shared orchestration still passes dots and changes the result of the regular glob pair for the leading dot file; the same *.txt and.foo.txt return false/true respectively when dot=false/true.
- **mutation**: Discard dot option (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The run is valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0022

[patch](patches/P-0022-ac5face5639c.patch)
SHA-256: ac5face5639c876d7298d8f94bb74a91b3ef58ef3bcca11c33225441c9975a6a

### VP-0022: any empty block error returns true

- **requirement**: Return false for any empty block or fully empty entry block; the any of [] and [] returns false.
- **mutation**: any empty block error returns true (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The run is valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0023

[patch](patches/P-0023-aca66b863c40.patch)
SHA-256: aca66b863c40b18797930ad2540747c2f24f27a3e1c3b35f87acc2a115ab4a67

### VP-0023: When both exist, skip all.

- **requirement**: Combine all and any within one configuration using AND in their original evaluation order. Either block failing makes the result false. A failed all block short-circuits any.
- **mutation**: When both exist, skip all. (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: all failed, not evaluated any; not invalid execution
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0024

[patch](patches/P-0024-afcc37248051.patch)
SHA-256: afcc37248051b14ee9a88459824c3c685e8ee473196fb44f8994169deaeabe6b

### VP-0024: Branch string error normalized to empty array

- **requirement**: The normalized objects of branch strings/arrays and combined entries remain equal; the normalized baseBranch/headBranch/changedFiles fields, arrays, and existing undefined fields
- **mutation**: Branch string error normalized to empty array (changed files: src/labeler.ts, src/branch.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The run is valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0025

[patch](patches/P-0025-b95f9ff9923f.patch)
SHA-256: b95f9ff9923fd4328dc204a67a33fd2e01ae62f4c36c0921813b5b20408636d4

### VP-0025: Remove the pre-condition for all empty files

- **requirement**: The all changed-files dimension fails if there is an empty file list; if the boolean is false and the file mode has not been evaluated, the debug for no files is located at the same position.
- **mutation**: Remove the pre-condition for all empty files (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The debug for no files is located in the same position; it is not an invalid execution.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0026

[patch](patches/P-0026-c16a789b93c2.patch)
SHA-256: c16a789b93c20bcbbfeb38067f5c0a3972e3c1a47f650885c694de808872f0d1

### VP-0026: Change existing shape error message

- **requirement**: The correct implementation should not have the following incorrect behaviors: changed-files non-object elements continue to trigger existing shape errors; the correct implementation should not have the following errors: changed-files:[42], etc., which include rejected input errors and messages, should not be extended to an arbitrary input robustness matrix.
- **mutation**: Change existing shape error message (changed files: src/changedFiles.ts, src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: [42] Existing Error and message responses for rejecting input are not extended to an arbitrary input robustness matrix; it is not an invalid execution.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0027

[patch](patches/P-0027-cabc6e5b16d2.patch)
SHA-256: cabc6e5b16d2f03c8ce1ff871471d30f6f81c9c9ecbbab18efcafea095863393

### VP-0027: Throw exception due to missing PR context error.

- **requirement**: Missing corresponding branch context results in dimension failure without making mistakes; return false when there is no PR or corresponding reference, without causing exceptions due to premature construction of regular expressions.
- **mutation**: Throw exception due to missing PR context error. (changed files: src/labeler.ts, src/branch.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Eager regex construction must not raise an exception. The run must be valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0028

[patch](patches/P-0028-cc50c2817f39.patch)
SHA-256: cc50c2817f39a06a9d4364c1ad2b3cd5c6a71a39a4be7d0d036c74fe9e6714e2

### VP-0028: Make the shorthand a separate AND configuration instead of merging it into the existing any configuration.

- **requirement**: The grouping and priority of explicit quantifiers and abbreviated dimensions are maintained. For the same configuration, equal Map and MatchConfig lists are generated. Abbreviations are merged into the same position, and top-level options do not become labels.
- **mutation**: Make the shorthand a separate AND configuration instead of merging it into the existing any configuration. (changed files: src/labeler.ts, src/api/get-label-configs.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Merge the shorthand into the same any position. Top-level options must not become labels. The run must be valid.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0029

[patch](patches/P-0029-ce0b6f5dd7c2.patch)
SHA-256: ce0b6f5dd7c2a7a821bbccb8e1c4c6ce06eee69eadf3407af52ebace098aac02

### VP-0029: Only the first item in the configuration list is checked.

- **requirement**: The configuration list is combined by AND. Empty lists and empty configuration object boundaries are retained. If one item fails, the result is false; if all succeed, the result is true. [] represents true, and [] represents false.
- **mutation**: Only the first item in the configuration list is checked. (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: True for all cases, [] means true, [] means false; not invalid execution
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

## P-0031

[patch](patches/P-0031-f6d2a6de495f.patch)
SHA-256: f6d2a6de495f4f5c54052380045649276d78e9b27ccb9d7d6ff469fe353e7d8c

### VP-0031: Missing dimensions treated as array error

- **requirement**: Determine participation dimensions based on existing configuration field values, maintaining the difference between empty arrays and undefined values; single-branch normalization objects will not mistakenly evaluate the other undefined branch; empty array dimensions will not be considered missing due to having a length of 0.
- **mutation**: Missing dimensions treated as array error (changed files: src/labeler.ts)
- **setup**: Apply this patch to the clean baseline at 98ce1450c790, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Empty arrays are not considered missing if their length is zero; it is not an invalid execution.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public target not reached; No errors occurred. Trustworthy test import or collection failed

