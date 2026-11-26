# Adversarial patches and verification points

Task: refactor-mermaid-ascii-layout-direction-03
Base commit: 5f00e3d9ac9fc96a19859d502333e35b87d2ffea

This package contains 34 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-02f4a1a536b3.patch)
SHA-256: 02f4a1a536b30549ce6f2910f74830429a079d3f42e64b45cb06c2adc260d0cb

### VP-0001: Targeted change: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pk

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **mutation**: Targeted changes to pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Determine whether the public error is rejected or whether a legitimate alternative is accepted.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0002

[patch](patches/P-0002-0508ab5a6794.patch)
SHA-256: 0508ab5a6794310dbd68d8f4f0d048088c289b2a9e709de93d2a0d7786de43ac

### VP-0002: Double horizontal coordinate increments and collision steps, preserving the other abstractions and entry points.

- **requirement**: Double horizontal coordinate increments and collision steps, preserving the other abstractions and entry points.
- **mutation**: Double horizontal coordinate increments and collision steps, preserving the other abstractions and entry points. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0003

[patch](patches/P-0003-0647ad32db8c.patch)
SHA-256: 0647ad32db8c9401a6fa1861772fb849177d5080e09b0f66e1b31851ae5374ab

### VP-0003: NewConfig ignores the passed TD

- **requirement**: NewConfig ignores the passed TD
- **mutation**: NewConfig ignores the passed TD (changed files: pkg/diagram/config.go, pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0005

[patch](patches/P-0005-11374057c8c0.patch)
SHA-256: 11374057c8c00480d2022894a598d40f3d17a566c3521a4eead0f3910324d1c2

### VP-0005: Discontinue parallel connection direction of duplicate edges

- **requirement**: Discontinue parallel connection direction of duplicate edges
- **mutation**: Discontinue parallel connection direction of duplicate edges (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0006

[patch](patches/P-0006-1a5bc240697a.patch)
SHA-256: 1a5bc240697a87d46dfdc32cde16833d25e7282ad212438c89fc6e3e5283e94e

### VP-0006: Draw returns one extra space at the end of the byte.

- **requirement**: Draw returns one extra space at the end of the byte.
- **mutation**: Draw returns one extra space at the end of the byte. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0007

[patch](patches/P-0007-1d48c9ee2e08.patch)
SHA-256: 1d48c9ee2e08d1c0d852b07b1143cef9e1917e5aa322af0b66fd2e8684d7b874

### VP-0007: Only drawing ignores Unicode selection

- **requirement**: Only drawing ignores Unicode selection
- **mutation**: Only drawing ignores Unicode selection (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0008

[patch](patches/P-0008-2b07c5d874c4.patch)
SHA-256: 2b07c5d874c4264f43ff038aefdd662dd1cf5ef1abcb677ea66fb00cc57205b0

### VP-0008: Change only the four directions of the horizontal self-loop.

- **requirement**: Change only the four directions of the horizontal self-loop.
- **mutation**: Change only the four directions of the horizontal self-loop. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0009

[patch](patches/P-0009-2dcbe56f863c.patch)
SHA-256: 2dcbe56f863c62317f8d808c156ddc76d73c99e590a6ef4410d312f85a87e430

### VP-0009: Change only the preferred and fallback routes for a downward edge pointing right in horizontal layout.

- **requirement**: Change only the preferred and fallback routes for a downward edge pointing right in horizontal layout.
- **mutation**: Change only the preferred and fallback routes for a downward edge pointing right in horizontal layout. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0010

[patch](patches/P-0010-2f39ad4c8315.patch)
SHA-256: 2f39ad4c8315137d74df2e02655e8219270900fb363eb4fe2e24a37f461b16dc

### VP-0010: Disabling configured coordinate overrides

- **requirement**: Disabling configured coordinate overrides
- **mutation**: Disabling configured coordinate overrides (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0011

[patch](patches/P-0011-31e914a3683a.patch)
SHA-256: 31e914a3683afa41aed5a064d06a9bc63a609bdf24984740eea29c8473725259

### VP-0011: Repeat the call with a space added at the end of every even iteration. The actual input sequence is uncertain.

- **requirement**: Repeat the call with a space added at the end of every even iteration. The actual input sequence is uncertain.
- **mutation**: Repeat the call with a space added at the end of every even iteration. The actual input sequence is uncertain. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0012

[patch](patches/P-0012-33e762dc8b7e.patch)
SHA-256: 33e762dc8b7efe9215af4d225367501f4f6fef83757821ba3689579590125311

### VP-0012: Map RL to the vertical axis

- **requirement**: Map RL to the vertical axis
- **mutation**: Map RL to the vertical axis (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0013

[patch](patches/P-0013-360c9afa69d1.patch)
SHA-256: 360c9afa69d1905642292b87e17772ffdfa637174cf137b3eb9f4ce81f92c360

### VP-0013: Deduct explicit bidirectional edge labels

- **requirement**: Deduct explicit bidirectional edge labels
- **mutation**: Deduct explicit bidirectional edge labels (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0014

[patch](patches/P-0014-3c80f1d33ef2.patch)
SHA-256: 3c80f1d33ef2eae61953422db6dc39be50d8138b08f71ccb0a73827c1eae029e

### VP-0014: Change only the bytes returned by RenderDiagram.

- **requirement**: Change only the bytes returned by RenderDiagram.
- **mutation**: Change only the bytes returned by RenderDiagram. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0015

[patch](patches/P-0015-3df8728c059c.patch)
SHA-256: 3df8728c059c513087f5185248d2169e96b8c3594d60026300c70067d440b1df

### VP-0015: Change only the connection side of a leftward back edge in horizontal layout.

- **requirement**: Change only the connection side of a leftward back edge in horizontal layout.
- **mutation**: Change only the connection side of a leftward back edge in horizontal layout. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0016

[patch](patches/P-0016-40374363c70f.patch)
SHA-256: 40374363c70fd9ef35be07c7c13ccc8c99fc8d90072865fc8d7611c7aece4ecc

### VP-0016: Change only the Width column of the width state.

- **requirement**: Change only the Width column of the width state.
- **mutation**: Change only the Width column of the width state. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0017

[patch](patches/P-0017-4975fa1acd7b.patch)
SHA-256: 4975fa1acd7b398f8ea094f86ebb0f40897d45436ae23287d1abd5c9f3446066

### VP-0017: The declaration words for re-mapping at the point of actual parsing and layout transmission are the same, but the single-point mapping is violated.

- **requirement**: The declaration words for re-mapping at the point of actual parsing and layout transmission are the same, but the single-point mapping is violated.
- **mutation**: The declaration words for re-mapping at the point of actual parsing and layout transmission are the same, but the single-point mapping is violated. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0018

[patch](patches/P-0018-6119b2da63d5.patch)
SHA-256: 6119b2da63d5b7a8b7eb924771cca1653f4ceb0060c9fbefd6e7ff48434c8a92

### VP-0018: Change only the default direction in DefaultConfig.

- **requirement**: Change only the default direction in DefaultConfig.
- **mutation**: Change only the default direction in DefaultConfig. (changed files: pkg/diagram/config.go, pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0019

[patch](patches/P-0019-65d470f43b44.patch)
SHA-256: 65d470f43b44e4af3f31d35304c2188dca6bc541df5035e60531adc4af8995a3

### VP-0019: Targeted change: pkg/diagram/config.go, pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: pkg/diagram/config.go, pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, among others)
- **mutation**: Targeted changes to pkg/diagram/config.go, pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, among others (changed files: pkg/diagram/config.go, pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Determine whether the public error is rejected or whether a legitimate alternative is accepted.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0020

[patch](patches/P-0020-690dcb841c4c.patch)
SHA-256: 690dcb841c4cf1ed8899fc7a7b4c62776032499da075e177433e487eb51386cd

### VP-0020: Only the original qualified vertical axis fan-out is allowed.

- **requirement**: Only the original qualified vertical axis fan-out is allowed.
- **mutation**: Only the original qualified vertical axis fan-out is allowed. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0021

[patch](patches/P-0021-6e7d04a7a8a5.patch)
SHA-256: 6e7d04a7a8a5eb2d3976cc363fba662a94da1c7dd671ff4665596bb6ee55cc47

### VP-0021: Only Apply ignores the passed horizontal spacing

- **requirement**: Only Apply ignores the passed horizontal spacing
- **mutation**: Only Apply ignores the passed horizontal spacing (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0022

[patch](patches/P-0022-76f996b7114d.patch)
SHA-256: 76f996b7114d590f65a05fb6a320d11af6531c81a3ced306514ce9ee174a0122

### VP-0022: Targeted change: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pk

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **mutation**: Targeted changes to pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Determine whether the public error is rejected or whether a legitimate alternative is accepted.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0023

[patch](patches/P-0023-785db53a1775.patch)
SHA-256: 785db53a177509d161b963b720e971a36c90837be42dc057a3371849bd7fbd1c

### VP-0023: Only change the default Test direction

- **requirement**: Only change the default Test direction
- **mutation**: Only change the default Test direction (changed files: pkg/diagram/config.go, pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0024

[patch](patches/P-0024-858937fd30ab.patch)
SHA-256: 858937fd30abe8ed2db23735f3eacee02252e735d9561ac563237f810c62f739

### VP-0024: Discarding the separation of horizontal outer roots and edge subgraph roots

- **requirement**: Discarding the separation of horizontal outer roots and edge subgraph roots
- **mutation**: Discarding the separation of horizontal outer roots and edge subgraph roots (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0025

[patch](patches/P-0025-86480bcf9a21.patch)
SHA-256: 86480bcf9a21b571c52f4df0a1b10bdf24ccaaeb194be6397706e6ae56655e5d

### VP-0025: Change only the error message for an extra token.

- **requirement**: Change only the error message for an extra token.
- **mutation**: Change only the error message for an extra token. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0026

[patch](patches/P-0026-8b68af101798.patch)
SHA-256: 8b68af101798b4d585b13a542b45e7ccdb0ec717bd8fa1d78152e07d82a50f82

### VP-0026: Please only assign fields that are in the wrong direction to the correct category.

- **requirement**: Please only assign fields that are in the wrong direction to the correct category.
- **mutation**: Please only assign fields that are in the wrong direction to the correct category. (changed files: pkg/diagram/config.go, pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0027

[patch](patches/P-0027-a44f90a30709.patch)
SHA-256: a44f90a30709e6f3fded2e70d57133aab84eca4265793bc6efe2c09ee4ea9013

### VP-0027: Keep the original string axis and scattered consumers. The image stays the same, but the structural requirement is unmet.

- **requirement**: Keep the original string axis and scattered consumers. The image stays the same, but the structural requirement is unmet.
- **mutation**: Keep the original string axis and scattered consumers. The image stays the same, but the structural requirement is unmet. (changed files: pkg/graph/direction.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0028

[patch](patches/P-0028-7ff789184d20.patch)
SHA-256: 7ff789184d20863baaada6d729d24b7429d328d2420a3d79a4510693391007d5

### VP-0028: Correct the error in the first parallel path on the repeated horizontal side.

- **requirement**: Correct the error in the first parallel path on the repeated horizontal side.
- **mutation**: Correct the error in the first parallel path on the repeated horizontal side.
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry should generate a complete and valid rejection score; failure in execution, compilation, or collection does not count as success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0029

[patch](patches/P-0029-b026b4c461fe.patch)
SHA-256: b026b4c461fe6402e29a1e2f39f330e1c4ad51ef58bbe97bcc502b49bb39a74b

### VP-0029: NewCLIConfig ignores the passed TD.

- **requirement**: NewCLIConfig ignores the passed TD.
- **mutation**: NewCLIConfig ignores the passed TD. (changed files: pkg/diagram/config.go, pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0030

[patch](patches/P-0030-c46cae91c99d.patch)
SHA-256: c46cae91c99d3f7496b8c712dec4de5d06fbc30630e3270ac161e3a10a41f6fd

### VP-0030: Change the support list in "Direction Error"

- **requirement**: Change the support list in "Direction Error"
- **mutation**: Change the support list in "Direction Error" (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0031

[patch](patches/P-0031-d76279659d69.patch)
SHA-256: d76279659d69568d8c20f70c540ddcb51b3ea45e2a644008162fc1d873fe5729

### VP-0031: Change only the default axis when the direction is omitted.

- **requirement**: Change only the default axis when the direction is omitted.
- **mutation**: Change only the default axis when the direction is omitted. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0032

[patch](patches/P-0032-dc68e163b2f9.patch)
SHA-256: dc68e163b2f9b51404f1c261f098ec95341f749cd0fa0ee890d0ffd26b3c01cf

### VP-0032: Apply incorrectly covers the declaration axis in the wrong configuration direction

- **requirement**: Apply incorrectly covers the declaration axis in the wrong configuration direction
- **mutation**: Apply incorrectly covers the declaration axis in the wrong configuration direction (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0033

[patch](patches/P-0033-f3a65d36519c.patch)
SHA-256: f3a65d36519c17d8bb33f8f718efc5b94231caeed47853233c3d495d5773b03e

### VP-0033: Map only BT to the horizontal axis.

- **requirement**: Map only BT to the horizontal axis.
- **mutation**: Map only BT to the horizontal axis. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0034

[patch](patches/P-0034-f896a820828b.patch)
SHA-256: f896a820828bb8f41e2b888c856ff4791f6a3a22cbfcb63067fc33b7ec776a20

### VP-0034: Only error messages that do not support types are changed.

- **requirement**: Only error messages that do not support types are changed.
- **mutation**: Only error messages that do not support types are changed. (changed files: pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, pkg/graph/graph.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

## P-0035

[patch](patches/P-0035-f91ea9ea640f.patch)
SHA-256: f91ea9ea640f4b2b4b43c035f62995cd5232562ac0358ed197bce22a0e439a16

### VP-0035: Only Web Direction Default Changed

- **requirement**: Only Web Direction Default Changed
- **mutation**: Only Web Direction Default Changed (changed files: pkg/diagram/config.go, pkg/graph/direction.go, pkg/graph/mapping_edge.go, pkg/graph/parse_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The target was never reached or the change had no effect; Patch application, build, or test collection error; The original output or identity binding is incomplete

