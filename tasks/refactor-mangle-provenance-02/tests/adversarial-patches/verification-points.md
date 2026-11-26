# Adversarial patches and verification points

Task: refactor-mangle-provenance-02
Base commit: 8edad8d350b99dc08063981663f4b4a159a6b7ec

This package contains 25 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-0bb45b9fd027.patch)
SHA-256: 0bb45b9fd027693974c179727a48f4c43baaf17aeafd00b172a2342239e3c8f8

### VP-0001: simple error acceptance transforms the result as an EDB

- **requirement**: The IDB goal with only transform derivation is still nil, ErrNoProof, and does not have KindLetRow/KindDoAggregate.
- **mutation**: simple error acceptance transforms the result as an EDB (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0002

[patch](patches/P-0002-0d8f237beef1.patch)
SHA-256: 0d8f237beef1bb2b41c93861425ce02fc2d88e945838b8876c69d24c54b1fea1

### VP-0002: EDB Content Identity Salt Change

- **requirement**: For the same input, the EDB, absence, derived, partial, and RuleID strings match the original implementation and remain stable across repeated construction.
- **mutation**: EDB Content Identity Salt Change (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0003

[patch](patches/P-0003-0e71139c01f8.patch)
SHA-256: 0e71139c01f8a63d97f9d53c12a231fa5d806a6c9d6973ac1857df7ce9a61839

### VP-0003: Zero MaxProofs errors, default value 2

- **requirement**: In multiple alternatives, MaxProofs=0 is equivalent to 1.
- **mutation**: Zero MaxProofs errors, default value 2 (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

### VP-0004: Zero MaxProofs errors, default value 2

- **requirement**: In multiple valid events, MaxProofs=0 is equivalent to 1.
- **mutation**: Zero MaxProofs errors, default value 2 (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0004

[patch](patches/P-0004-12518da4e00e.patch)
SHA-256: 12518da4e00e8e7ce2798dce3dfdf812e60033d089175add464783146da6656d

### VP-0005: Replay Lost Store Leaf Retrocession

- **requirement**: If there are no events and the fact is in the store, then it is KindEDB; if the fact is missing, then there is no proof.
- **mutation**: Replay Lost Store Leaf Retrocession (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0005

[patch](patches/P-0005-2e02577bfe8d.patch)
SHA-256: 2e02577bfe8d1b3bf185ec0c4a5f35b224bf7995a0c3abbd0cce14df8ad9af27

### VP-0006: Zero MaxDepth error default 63

- **requirement**: The truncation position and Partial value for MaxDepth=0 and 64 are the same.
- **mutation**: Zero MaxDepth error default 63 (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

### VP-0007: Zero MaxDepth error default 63

- **requirement**: The truncation position and Partial value for MaxDepth=0 and 64 are the same.
- **mutation**: Zero MaxDepth error default 63 (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0006

[patch](patches/P-0006-590fb144b06f.patch)
SHA-256: 590fb144b06f092a03ec0afcff7d4373205aab3289c555aac8e53b0d922e5924

### VP-0008: Deep truncation leaf node error removal Partial marker

- **requirement**: When the depth limit is reached, a proof of partial must be returned.
- **mutation**: The shared constructor buildPartialLeaf sets Partial to false.
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The original official tests should reject the candidate in a valid run. An invalid run does not count.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Public Behavior Differences; compile/collect/apply error

## P-0007

[patch](patches/P-0007-413b97d18b76.patch)
SHA-256: 413b97d18b76814e2e6b496256141dd9956d383555bc144965475595f1bb5976

### VP-0009: The absence of errors proves

- **requirement**: An absence_leaf and a reference from the parent premise exist, but there is no proves entry for that absence ID.
- **mutation**: The absence of errors proves (changed files: provenance/provenance.go, provenance/recorder.go, provenance/facts.go, provenance/provenance_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0008

[patch](patches/P-0008-4efc757d4d78.patch)
SHA-256: 4efc757d4d78a79b089571e9a41946078d504977cd91869ff889aa659b26704b

### VP-0010: Explicit MaxProofs upper limit increased by one

- **requirement**: When there are more alternatives than the upper limit
- **mutation**: Explicit MaxProofs upper limit increased by one (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

### VP-0011: Explicit MaxProofs upper limit increased by one

- **requirement**: When recording multiple alternatives, the number should not exceed the limit, and the order of event selection remains unchanged.
- **mutation**: Explicit MaxProofs upper limit increased by one (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0009

[patch](patches/P-0009-56b608c501ca.patch)
SHA-256: 56b608c501caefcddcaf28b33b6805319c154e2591d111fd8c4d11e04b0d4760

### VP-0012: Disable in-progress short-circuit, continue termination with depth limit

- **requirement**: Re-entering the same branch of an in-progress goal does not contribute to the proof; loops with a base case still terminate and retain the original result.
- **mutation**: Disable in-progress short-circuit, continue termination with depth limit (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

### VP-0013: Disable in-progress short-circuit, continue termination with depth limit

- **requirement**: The repeated targets of the loop events return null; the parent events are processed according to the original Partial/rollback rules and terminated.
- **mutation**: Disable in-progress short-circuit, continue termination with depth limit (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0010

[patch](patches/P-0010-60e4ba7ee813.patch)
SHA-256: 60e4ba7ee8134aa51271d7a31393b2996fd0b337836caceefb6f4f5138fafce7

### VP-0014: Targeted regression: Share an ID across subderivations with the same rule, fact, and ordered child proofs.

- **requirement**: Subderivations with the same rule, fact, and ordered child proofs share an ID. The two modes may select different alternatives.
- **mutation**: Targeted regression: Share an ID across subderivations with the same rule, fact, and ordered child proofs. (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0011

[patch](patches/P-0011-7b042a422956.patch)
SHA-256: 7b042a4229567d071d24dd992a89e6bb86fb23745cee2887c76f79944c2eeb24

### VP-0015: EDB errors are marked as absence

- **requirement**: The EDB goal's Fact, KindEDB, and ID match the baseline.
- **mutation**: EDB errors are marked as absence (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0012

[patch](patches/P-0012-7b50ead405a3.patch)
SHA-256: 7b50ead405a36a6b0012e31107048300be504a217fdf4f7a1c303eb452d57db2

### VP-0016: Behaviorally equivalent but violates the structure goal of being only premises

- **requirement**: The pattern side retains the analysis of post-hoc queries/absence or recording rule/let/do, and the shared construction layer does not reimplement the second set of pattern schedules; there are no restrictions on naming, the number of helpers, or the file layout.
- **mutation**: Behaviorally equivalent but violates the structure goal of being only premises (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0013

[patch](patches/P-0013-7c1414d5a2db.patch)
SHA-256: 7c1414d5a2db98ac01d54ce3a0e3cc5d1c7fb90b5a8fb782432c413209504b9c

### VP-0017: Targeted regression: EventLet's KindLetRow, TransformText, premises, Rule/RuleID, and Partial are related to the baseline.

- **requirement**: EventLet's KindLetRow, TransformText, premises, Rule/RuleID, and Partial are the same as the baseline.
- **mutation**: Targeted regression: EventLet's KindLetRow, TransformText, premises, Rule/RuleID, and Partial are the same as the baseline. (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0014

[patch](patches/P-0014-82425e32625a.patch)
SHA-256: 82425e32625ac4394cd058a3ea0393d7ea836b1c452d2cfed10a1b270351cf8f

### VP-0018: Memo errors are elevated to process global, resulting in outdated cross-call results

- **requirement**: The sub-proofs for the same repeated goal are consistent; the changes in the store can be seen in the next call.
- **mutation**: Memo errors are elevated to process global, resulting in outdated cross-call results (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

### VP-0019: Memo errors are elevated to process global, resulting in outdated cross-call results

- **requirement**: The sub-proofs for the same repeated goal are consistent; the next call can see newly recorded events or store states.
- **mutation**: Memo errors are elevated to process global, resulting in outdated cross-call results (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0015

[patch](patches/P-0015-84ed4b5ed0f4.patch)
SHA-256: 84ed4b5ed0f4ae12f32b7f1dd82a0e78500031d5dd32d0d99d82274b59192b4f

### VP-0020: Targeted regression: All satisfied positive premise/Eq/Ineq rules generate the same KindDerived, Rule/RuleID, Bindings, and ordered Premi.

- **requirement**: Both satisfying positive premise/Eq/Ineq rules generate the same KindDerived, Rule/RuleID, Bindings, and ordered premises.
- **mutation**: Targeted regression: Both satisfying positive premise/Eq/Ineq rules generate the same KindDerived, Rule/RuleID, Bindings, and ordered premises. (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0016

[patch](patches/P-0016-870ce5466754.patch)
SHA-256: 870ce54667545f6794972b2c3c4f51f9e4268bd5b85baaeee875566e0715af0c

### VP-0021: EventRule playback loses bindings

- **requirement**: EventRule generates the same KindDerived, rule, bindings, ordered premises, and original Partial.
- **mutation**: EventRule playback loses bindings (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0017

[patch](patches/P-0017-892e98ec068d.patch)
SHA-256: 892e98ec068d9905d46c2fa4b58d3f572784e657ea42a4a6e5b4183191b0aacf

### VP-0022: absence error marked as EDB

- **requirement**: When the fact is absent, it is denoted as KindAbsence; when it exists, there is no proof for that branch.
- **mutation**: absence error marked as EDB (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0018

[patch](patches/P-0018-8adbb8130efa.patch)
SHA-256: 8adbb8130efaa50e67a580576290a4237514bb7bbe1f3d2dda888b1232d4dc57

### VP-0023: fact schema premise index increment by one

- **requirement**: fact schema premise index increment by one
- **mutation**: fact schema premise index increment by one (changed files: provenance/provenance.go, provenance/recorder.go, provenance/facts.go, provenance/provenance_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0019

[patch](patches/P-0019-90b57a95c88b.patch)
SHA-256: 90b57a95c88b551f167f9115778aefb7d09ae1202df6849eee5b63a5e523bd0c

### VP-0024: Depth cut in one layer ahead

- **requirement**: Do not replace "error" with "error"
- **mutation**: Depth cut in one layer ahead (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

### VP-0025: Depth cut in one layer ahead

- **requirement**: No behavioral fixes to be done
- **mutation**: Depth cut in one layer ahead (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0020

[patch](patches/P-0020-9d4e6b8ad337.patch)
SHA-256: 9d4e6b8ad337e2ccf663313fad6c93648d056bf8ed37894f035d2b287fc90638

### VP-0026: No proof errors were swallowed.

- **requirement**: nil, ErrNoProof, without partial proofs when not available
- **mutation**: No proof errors were swallowed. (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

### VP-0027: No proof errors were swallowed.

- **requirement**: When neither the event nor the store rollback can generate a proof, the result is nil, ErrNoProof, without any partial proofs.
- **mutation**: No proof errors were swallowed. (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0021

[patch](patches/P-0021-b92d9d0c8010.patch)
SHA-256: b92d9d0c8010c54560805c0bc9c595fbe0f1e763786412af8716e2398f0db6eb

### VP-0028: Restored two independent recursive construction skeletons

- **requirement**: Structural review can identify common construction layers; both patterns no longer retain complete recursive skeletons separately.
- **mutation**: Restored two independent recursive construction skeletons (changed files: provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0022

[patch](patches/P-0022-c34eb89332e0.patch)
SHA-256: c34eb89332e0fd844d5506d5fa1c8f862d2612c0e21cdc3cdc1d73a70e5cc0f0

### VP-0029: Shared ruleID content identity salt variation

- **requirement**: The EDB, rule, let, aggregate, partial, and RuleID strings for the same recording input remain the same as the original implementation, ensuring stable reconstruction.
- **mutation**: Shared ruleID content identity salt variation (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0023

[patch](patches/P-0023-cf966236b964.patch)
SHA-256: cf966236b964376d31b8bd8471fcadddc0be32f9c65fbaa6ace2cde9f69669fe

### VP-0030: Partial tree output label changes

- **requirement**: The expected differences for aggregate printing tests should remain unresolved under PF02, and should not be overwritten with hidden materials.
- **mutation**: Partial tree output label changes (changed files: provenance/provenance.go, provenance/recorder.go, provenance/facts.go, provenance/provenance_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0024

[patch](patches/P-0024-d26bd8e4da1e.patch)
SHA-256: d26bd8e4da1eee4705d4dcc569735d9157162a45636fb4407ecfaa20b69025c0

### VP-0031: Shared subproof repeated expansion

- **requirement**: The sub-proof with the same ID is only fully expanded for the first time. Subsequent outputs will retain the original ... see ID text.
- **mutation**: Shared subproof repeated expansion (changed files: provenance/provenance.go, provenance/recorder.go, provenance/facts.go, provenance/provenance_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

## P-0025

[patch](patches/P-0025-d28e33a942cb.patch)
SHA-256: d28e33a942cbefd8becbb60612f1b35841ed787167fdff617101ac414d46135b

### VP-0032: Targeted regression: EventDo's KindDoAggregate, GroupKey, TransformText, sorted by ID input proofs, and Partial

- **requirement**: EventDo's KindDoAggregate, GroupKey, TransformText, sorted by ID input proofs, and Partial are the same as the baseline.
- **mutation**: Targeted regression: EventDo's KindDoAggregate, GroupKey, TransformText, sorted by ID input proofs, and Partial are the same as the baseline. (changed files: provenance/provenance.go, provenance/recorder.go, provenance/provenance_test.go, provenance/recorder_test.go)
- **setup**: Apply this patch to the clean baseline at 8edad8d350b9, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation/collection/application failed

