# Adversarial patches and verification points

Task: refactor-mermaid-ascii-mapping-05
Base commit: 5f00e3d9ac9fc96a19859d502333e35b87d2ffea

This package contains 21 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-048c036fe5f8.patch)
SHA-256: 048c036fe5f8844070c11c02666feeb3fa8444536a3993006b03b035e0122c1c

### VP-0001: Targeted changes to pkg/graph/graph.go, pkg/graph/mapping.go

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **mutation**: Targeted changes to pkg/graph/graph.go, pkg/graph/mapping.go (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0002

[patch](patches/P-0002-24be0ba5d009.patch)
SHA-256: 24be0ba5d0097a737640e03a699444d1664eef9fee50643dd2f46c74f5e30d43

### VP-0002: Targeted regression: Ensure the fanout order corresponds to the branch logic.

- **requirement**: Ensure the fanout order corresponds to the branch logic.
- **mutation**: Targeted regression: Ensure the fanout order corresponds to the branch logic. (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0003

[patch](patches/P-0003-cbc4a2868fc4.patch)
SHA-256: cbc4a2868fc43c90c452b2b0d39405311b306b0da1c1cc624cd4af1b791b27b6

### VP-0003: The grid spacing of the external root node is doubled incorrectly.

- **requirement**: Maintain the existing layout spacing and output bytes of the independent external root.
- **mutation**: The root placement step size is changed from 4 to 8, restoring the original untriggered startDir modification.
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The original tests reject the candidate because the layout bytes differ. An invalid run does not count.
- **prerequisites**: None (clean baseline)
- **version_note**: The original audit retired this verification point. It is retained for historical reference.
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0004

[patch](patches/P-0004-3576106db715.patch)
SHA-256: 3576106db7157920086835dc9c0d96b50233315d440bffe3543956fca9a36cb5

### VP-0004: Targeted regression: Preserve the translation caused by negative subgraph bounds.

- **requirement**: Preserve the translation caused by negative subgraph bounds.
- **mutation**: Targeted regression: Preserve the translation caused by negative subgraph bounds. (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0005

[patch](patches/P-0005-622ff43ab79e.patch)
SHA-256: 622ff43ab79ef2b1b4844bfe1621c37198172e71a73303e79f3288277f90fbe7

### VP-0005: Targeted regression: Subgraph offset responsibilities are independent

- **requirement**: Subgraph offset responsibilities are independent
- **mutation**: Targeted regression: Subgraph offset responsibilities are independent (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0006

[patch](patches/P-0006-647e5f12ffab.patch)
SHA-256: 647e5f12ffab686c5a306c3dd37286855538e56ce34b0acb1664240827aa20db

### VP-0006: Targeted regression: Responsibility for calculating and updating line height/column width is clearly defined.

- **requirement**: Responsibility for calculating and updating line height/column width is clearly defined.
- **mutation**: Targeted regression: Responsibility for calculating and updating line height/column width is clearly defined. (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0007

[patch](patches/P-0007-6e62977b7529.patch)
SHA-256: 6e62977b75291b0170c856b215f5f0b27f4a3742bc2ea1af1f51b834b6a00734

### VP-0007: Targeted regression: The mapping entry is only for short, dependent, and orderly arrangement of dependencies.

- **requirement**: The mapping entry is only for short, dependent, and orderly arrangement of dependencies.
- **mutation**: Targeted regression: The mapping entry is only for short, dependent, and orderly arrangement of dependencies. (changed files: pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0008

[patch](patches/P-0008-7b07eda820fc.patch)
SHA-256: 7b07eda820fccf63c2f169f458dd68775d7eed1d132d954462de88d25ad13c67

### VP-0008: Targeted regression: The fanout layout is cohesive, and state dependencies are explicitly stated.

- **requirement**: The fanout layout is cohesive, and state dependencies are explicitly stated.
- **mutation**: Targeted regression: The fanout layout is cohesive, and state dependencies are explicitly stated. (changed files: pkg/graph/fanout.go, pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0009

[patch](patches/P-0009-83aabc0d8b75.patch)
SHA-256: 83aabc0d8b75007901a5d23a258342a9854e42325906b7a8780c1d43123df076

### VP-0009: Targeted regression: The LR mixed root is one layer behind the subgraph root; otherwise, the roots are unified.

- **requirement**: The LR mixed root is one layer behind the subgraph root; otherwise, the roots are unified.
- **mutation**: Targeted regression: The LR mixed root is one layer behind the subgraph root; otherwise, the roots are unified. (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0010

[patch](patches/P-0010-8caf5dc3092d.patch)
SHA-256: 8caf5dc3092debb3e41c87f219a72e653d30da5ea2b04d858130b63ed7c6408d

### VP-0010: Targeted regression: Tag line selection and dimension/clean space adjustment responsibility cohesion

- **requirement**: Tag line selection and dimension/clean space adjustment responsibility cohesion
- **mutation**: Targeted regression: Tag line selection and dimension/clean space adjustment responsibility cohesion (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0011

[patch](patches/P-0011-91c064c6e912.patch)
SHA-256: 91c064c6e912673b5eb9117993c8821bacece90063ad1636fb37e7d3425b6f94

### VP-0011: Targeted regression: Subgraph bounding box responsibilities are independent

- **requirement**: Subgraph bounding box responsibilities are independent
- **mutation**: Targeted regression: Subgraph bounding box responsibilities are independent (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0012

[patch](patches/P-0012-932a371b5ae9.patch)
SHA-256: 932a371b5ae95422cdbf6b76279dd984f0ceab82d5d1c3f78fc3f9e799983c76

### VP-0012: Targeted regression: The placeholder conflict advances along the existing placement direction to the empty space.

- **requirement**: The placeholder conflict advances along the existing placement direction to the empty space.
- **mutation**: Targeted regression: The placeholder conflict advances along the existing placement direction to the empty space. (changed files: pkg/graph/graph.go, pkg/graph/mapping.go, pkg/graph/mapping_node.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0013

[patch](patches/P-0013-a8655f29514c.patch)
SHA-256: a8655f29514c2c0fa958d7ccdf2af0c4d20283d190c7b677acd7ac67d8c58398

### VP-0013: Targeted changes to pkg/graph/graph.go, pkg/graph/mapping.go

- **requirement**: Preserve existing behavior in the files changed by the patch (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **mutation**: Targeted changes to pkg/graph/graph.go, pkg/graph/mapping.go (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0014

[patch](patches/P-0014-b634e7ec1d71.patch)
SHA-256: b634e7ec1d71843ca4e33532a63821afcb307f9f1d203c82f3a5340948dfc4be

### VP-0014: Targeted regression: Assign responsibility for edge routing traversal and path state explicitly.

- **requirement**: Assign responsibility for edge routing traversal and path state explicitly.
- **mutation**: Targeted regression: Assign responsibility for edge routing traversal and path state explicitly. (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0015

[patch](patches/P-0015-b9802e200810.patch)
SHA-256: b9802e2008103fd330da635e3528db20563a740c32d8cf32f2a40894f0d56cc9

### VP-0015: Targeted regression: Normal graphic output bytes, spaces, dimensions, and labels remain unchanged.

- **requirement**: Normal graphic output bytes, spaces, dimensions, and labels remain unchanged.
- **mutation**: Targeted regression: Normal graphic output bytes, spaces, dimensions, and labels remain unchanged. (changed files: pkg/graph/graph.go, pkg/graph/mapping.go, pkg/graph/mapping_node.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0016

[patch](patches/P-0016-be6b3b48eff9.patch)
SHA-256: be6b3b48eff97d76203757b79529db19970b189333bca06fba9f79ffeebde70c

### VP-0016: Targeted regression: Subgraph bounding box geometry remains intact

- **requirement**: Subgraph bounding box geometry remains intact
- **mutation**: Targeted regression: Subgraph bounding box geometry remains intact (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0017

[patch](patches/P-0017-2c2b14f8ef4e.patch)
SHA-256: 2c2b14f8ef4ec197a7747a980686e1c44b79a7314dd16a48bf47faa5473eb81a

### VP-0017: The spacing between child nodes has increased from four spaces to eight spaces.

- **requirement**: The spacing between child nodes has increased from four spaces to eight spaces.
- **mutation**: The spacing between child nodes has increased from four spaces to eight spaces.
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry should generate a complete and valid rejection score; failure in execution, compilation, or collection does not count as success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0018

[patch](patches/P-0018-cb8d6f219fb6.patch)
SHA-256: cb8d6f219fb6f4cff70e0d85dbd81f7e89360fbc14eb46e9093353b27620f3e9

### VP-0018: Targeted regression: Root discovery logic and state independence cohesion

- **requirement**: Root discovery logic and state independence cohesion
- **mutation**: Targeted regression: Root discovery logic and state independence cohesion (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0019

[patch](patches/P-0019-d222f630dc54.patch)
SHA-256: d222f630dc54b51a5b8f995d52ba400ce2faf0119cb8b2bb80154961c0046973

### VP-0019: Targeted regression: Coordinate coverage map character retention

- **requirement**: Coordinate coverage map character retention
- **mutation**: Targeted regression: Coordinate coverage map character retention (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0020

[patch](patches/P-0020-e2ab4a692a83.patch)
SHA-256: e2ab4a692a83d41200ea1388138046b450f27d06e83ece6d6d0fd1c31694f19a

### VP-0020: Targeted regression: Edge label rows and alignment remain unchanged.

- **requirement**: Edge label rows and alignment remain unchanged.
- **mutation**: Targeted regression: Edge label rows and alignment remain unchanged. (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

## P-0021

[patch](patches/P-0021-eb6f4d3952ff.patch)
SHA-256: eb6f4d3952ff8a5575b5f53c437f8e0e565e5b7982937b2c5fc449c406d0ad4d

### VP-0021: Targeted regression: The root separation judgment and grouping have clear responsibilities and boundaries.

- **requirement**: The root separation judgment and grouping have clear responsibilities and boundaries.
- **mutation**: Targeted regression: The root separation judgment and grouping have clear responsibilities and boundaries. (changed files: pkg/graph/graph.go, pkg/graph/mapping.go)
- **setup**: Apply this patch to the clean baseline at 5f00e3d9ac9f, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: A valid named-map cannot be rejected solely due to shape issues.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Compilation or collection failed; Treat private dead fields as public errors

