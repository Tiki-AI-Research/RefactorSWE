# Adversarial patches and verification points

Task: pdoc-jinja-environment-config
Base commit: 00e18eb12ae2f06f3c245f796bfe7f6224db033a

This package contains 36 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-0349d6e07e57.patch)
SHA-256: 0349d6e07e575e32d5d058c4d1eb999770b1160835e646c053c750ff868bba11

### VP-0001: Targeted regression: Keep the public entry point for calls and HTML bytes under the given configuration

- **requirement**: Keep the public entry point for calls and HTML bytes under the given configuration
- **mutation**: Targeted regression: Keep the public entry point for calls and HTML bytes under the given configuration (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0002

[patch](patches/P-0002-0a9e9c10bc3f.patch)
SHA-256: 0a9e9c10bc3f85948f86a3e0ce9330616dbe3d1e76fe8190e396298bde28216a

### VP-0002: Targeted regression: Module cache invalidation retains the configured environment state

- **requirement**: Module cache invalidation retains the configured environment state
- **mutation**: Targeted regression: Module cache invalidation retains the configured environment state (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py, pdoc/extract.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0003

[patch](patches/P-0003-186e3004db37.patch)
SHA-256: 186e3004db375166a6694bc299844195f3a5743bca22c83699d5193d7bbabd5a

### VP-0003: The error page public entry retains calls and HTML bytes under the given configuration.

- **requirement**: Ensure that the correct implementation does not exhibit the following incorrect behaviors: The incorrect page public entry retains calls and HTML bytes under the given configuration.
- **mutation**: The error page public entry retains calls and HTML bytes under the given configuration. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0004

[patch](patches/P-0004-1bdacd645f36.patch)
SHA-256: 1bdacd645f36e55020a302b4a342169f03929e3fd51c3f5dca702f78acd819c7

### VP-0004: Another instance has its own initial build.

- **requirement**: The search index is calculated only once for the same instance and reused.
- **mutation**: Another instance has its own initial build. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0005

[patch](patches/P-0005-26540ce3d055.patch)
SHA-256: 26540ce3d055859c0c283631b612d244c9966f98b3920bac729fe58c5bba28a8

### VP-0005: Don't try to restore the original state by rewriting the entire system.

- **requirement**: Rendering and library export consume explicit configuration without relying internally on mutable configuration managed by the template.
- **mutation**: Don't try to restore the original state by rewriting the entire system. (changed files: pdoc/render.py, pdoc/web.py, pdoc/__init__.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0006

[patch](patches/P-0006-2ffec3e71ba7.patch)
SHA-256: 2ffec3e71ba7f984b42e6db142f02da48dcd8092028ec6f18061a7d84c52b066

### VP-0006: Still effective after configure

- **requirement**: The env filter added by the user remains effective in subsequent rendering.
- **mutation**: Still effective after configure (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0007

[patch](patches/P-0007-334e9ebadd02.patch)
SHA-256: 334e9ebadd029f2bdee63c13d2d19553e25dc1ab13faac04aed050ffaf6115c1

### VP-0007: Targeted regression: When searching is disabled, the public index is empty.

- **requirement**: When searching is disabled, the public index is empty.
- **mutation**: Targeted regression: When searching is disabled, the public index is empty. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0008

[patch](patches/P-0008-370a1692af0c.patch)
SHA-256: 370a1692af0c29fcff5eb383154bc823ced8a69ba64490d388016fca56565c30

### VP-0008: The new B request is the same as the baseline B.

- **requirement**: The configuration used during server creation will not be changed for the old instance after subsequent configuration changes.
- **mutation**: A new B request matches the baseline B request. The first request remains pinned to A even if it occurs after the update to B. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0009

[patch](patches/P-0009-3bb8b7dc9dbc.patch)
SHA-256: 3bb8b7dc9dbcd679930baa735899a37cc8206b02a88c020cd6535da89ccc143f

### VP-0009: The original signatures and module parameters remain valid.

- **requirement**: pdoc returns the string of the first module without an output directory.
- **mutation**: The original signatures and module parameters remain valid. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0010

[patch](patches/P-0010-4cc00d87657a.patch)
SHA-256: 4cc00d87657a4096b94b6cc414f13893632241e2cadb538565a2826d205dedeb

### VP-0010: The failed module will not be indexed. Other modules will remain, and the original warning will still appear.

- **requirement**: Search index skipped due to import failure. Module has issued a warning.
- **mutation**: The failed module will not be indexed. Other modules will remain, and the original warning will still appear. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0012

[patch](patches/P-0012-54a26a20776d.patch)
SHA-256: 54a26a20776d64e64c07af75095ac18f40078bb9e9432ba826b25eea98e80981

### VP-0012: Existing safe/Markup boundaries remain intact

- **requirement**: Template auto-escape retained.
- **mutation**: Existing safe/Markup boundaries remain intact (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0013

[patch](patches/P-0013-577d09d8e07a.patch)
SHA-256: 577d09d8e07aac1596e3327a9fa87a1f0c3e33263a2c598a47a378a0a3e4cf50

### VP-0013: Options affect the corresponding export content while preserving file bytes and artifact rules.

- **requirement**: CLI rendering options and static output branch semantics remain unchanged.
- **mutation**: Options affect the corresponding export content while preserving file bytes and artifact rules. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py, pdoc/__main__.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0015

[patch](patches/P-0015-616479866dbf.patch)
SHA-256: 616479866dbf7399fcddc2c90d11d2b1b24575fda22e61b22e8811576a277b24

### VP-0015: The repr of the same Module is the same as the baseline.

- **requirement**: The public entry of repr is reserved for calling and representing strings.
- **mutation**: The repr of the same Module is the same as the baseline. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0016

[patch](patches/P-0016-65162ad34fed.patch)
SHA-256: 65162ad34fed404241e4ae2ddb5885dc3f88a3f9c7c265241efd20f407b335df

### VP-0016: Targeted regression: The CLI defaults to opening the actual server URL. --no-browser disables the opening of the browser.

- **requirement**: The CLI defaults to opening the actual server URL. --no-browser disables this; observable results: the number of browser calls and the URL; --no-browser results in zero calls.
- **mutation**: Targeted regression: The CLI defaults to opening the actual server URL. --no-browser disables the opening of the browser. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py, pdoc/__main__.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Testing collected errors

## P-0017

[patch](patches/P-0017-66077d83098f.patch)
SHA-256: 66077d83098f973ac3c16fa81c4f8c84824ba2a60946b68971060e9a7c45e1b9

### VP-0017: configure does not lose the unmanaged key

- **requirement**: The env global added by the user remains effective in subsequent rendering.
- **mutation**: configure does not lose the unmanaged key (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0018

[patch](patches/P-0018-677c6f39f0f2.patch)
SHA-256: 677c6f39f0f2894f0f1d01dc61a685444aa53ac478596a94a834852681a2a005

### VP-0018: Targeted regression: First search build on the old server with the original A configuration

- **requirement**: The first search build on the old server retains the A configuration at the time of creation; observable result: No search has been conducted since A was created, and the first search after configure(B) still results in the baseline configuration A.
- **mutation**: Targeted regression: First search build on the old server with the original A configuration (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Testing collected errors

### VP-0019: Targeted regression: The server search response created by closing the search configuration is empty.

- **requirement**: The server search response text created by closing the search configuration is empty; observable result: The server/search.js text is '' even after opening the search through the global configure function.
- **mutation**: Targeted regression: The server search response created by closing the search configuration is empty. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Testing collected errors

## P-0019

[patch](patches/P-0019-72bf5fd69fd9.patch)
SHA-256: 72bf5fd69fd98be43702e3a04100f3509c7b1ec62bba2400c113d13cc40e40a1

### VP-0020: Targeted regression: The failures before the module try remain with the original exception boundaries.

- **requirement**: The failures before the module try remain with the original exception boundaries; observable result: mtime calculation failed and is not captured by the new unified 500 catch.
- **mutation**: Targeted regression: The failures before the module try remain with the original exception boundaries. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Testing collected errors

## P-0021

[patch](patches/P-0021-8f57140cf49f.patch)
SHA-256: 8f57140cf49f28d8c199617b3a75c768c7d364e7229f4c9f3a1e808b906bff71

### VP-0022: Targeted regression: Module cache invalidation retains the identity of the env object

- **requirement**: Module cache invalidation retains the identity of the env object
- **mutation**: Targeted regression: Module cache invalidation retains the identity of the env object (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py, pdoc/extract.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0022

[patch](patches/P-0022-9c6a6e03420c.patch)
SHA-256: 9c6a6e03420cd2d5785a91e072155a1a2b5acd9fb5bbcd04e7444d89a229b6a0

### VP-0023: The old caller does not need to consume the new carrier

- **requirement**: configure still returns None.
- **mutation**: The old caller does not need to consume the new carrier (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0023

[patch](patches/P-0023-9c8768071ec2.patch)
SHA-256: 9c8768071ec21d3b7bf881b4016735d84d5b3ef080169658c627f76142a04e9a

### VP-0024: Targeted regression: Index rendering failed, retaining exception propagation outside try.

- **requirement**: Index rendering failed, causing exception propagation outside of 'try'; observable result: Index rendering exception is propagated according to the baseline, no uniform 500 page conversion occurred.
- **mutation**: Targeted regression: Index rendering failed, retaining exception propagation outside try. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Testing collected errors

## P-0024

[patch](patches/P-0024-a90c80005924.patch)
SHA-256: a90c80005924b457ae34abe24559b901aeabc1b119a95b783623d7a6a4d84011

### VP-0025: Please keep the files in the old directories as they are.

- **requirement**: Static export with disabled search does not write search results
- **mutation**: Please keep the files in the old directories as they are. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0025

[patch](patches/P-0025-b2eb1a4a8609.patch)
SHA-256: b2eb1a4a8609ab74e5c8d7da89585da4bf2ef5cc337d1d56c568c183ff511a22

### VP-0026: None edit_url_map Treat as empty mapping

- **requirement**: Configure updates the current configuration for subsequent direct public calls. By default, calls will reset to the default values.
- **mutation**: None edit_url_map Treat as empty mapping (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0026

[patch](patches/P-0026-b8a9b0806354.patch)
SHA-256: b8a9b0806354515274eb6fcf73177fc766295163a26d8d526199e13ee149f3f1

### VP-0027: Targeted regression: Search rendering failed, keeps trying despite exceptions outside of try.

- **requirement**: Search rendering failed, causing exception propagation outside of try; observable result: search build/render exceptions propagate according to the baseline, maintaining the original order of response headers.
- **mutation**: Targeted regression: Search rendering failed, keeps trying despite exceptions outside of try. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Testing collected errors

## P-0027

[patch](patches/P-0027-b95a917da4e1.patch)
SHA-256: b95a917da4e1a4114bcba652565f126077be5b5b9eec00a7d8a71a2b9df49b7d

### VP-0028: It is not required for consumers to read the template configuration rewritten by the CLI first.

- **requirement**: CLI options are clearly defined and provided for consumer configuration
- **mutation**: It is not required for consumers to read the template configuration rewritten by the CLI first. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py, pdoc/__main__.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0028

[patch](patches/P-0028-bb906afe9fd0.patch)
SHA-256: bb906afe9fd00e995791366d8fb4aa9240dd3fa4551ec2f1feff23c43bc07616

### VP-0029: Instance configuration corresponding to the search text.

- **requirement**: Retained HTTP search entry for search response
- **mutation**: The search body reflects the instance configuration and is empty when search is disabled. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0029

[patch](patches/P-0029-c174220c3d02.patch)
SHA-256: c174220c3d02be8321c12c9305bb66708c0b68883286b9c86799c6abed06344f

### VP-0030: Original path explanation and HTML bytes of modules under fixed mtime

- **requirement**: A valid HTTP module path still returns the module page.
- **mutation**: Original path explanation and HTML bytes of modules under fixed mtime (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0030

[patch](patches/P-0030-c2860e72f744.patch)
SHA-256: c2860e72f744e7be7967acb298c9775eb37f2ea1838824ab1bbf19fa865f4dfb

### VP-0031: Original modification time string

- **requirement**: HTTP mtime request retention modification time response
- **mutation**: Original modification time string (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0031

[patch](patches/P-0031-c5e11e588775.patch)
SHA-256: c5e11e5887756c40cfd737ef720eb810e4a24959aac859be94d76250705ed77b

### VP-0032: Fixed module/templates/runtime/config/mtime to be consistent with the baseline

- **requirement**: The public entry for the module page remains callable and contains HTML bytes under the given configuration.
- **mutation**: Fixed module/templates/runtime/config/mtime to be consistent with the baseline (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0033

[patch](patches/P-0033-d31bd1333c1b.patch)
SHA-256: d31bd1333c1bb821d8517ad641214bcee5c4fae2babf504ca4cc01399f68dd90

### VP-0034: It is not advisable to expand the failure of the incorrect page into a new abnormal contract.

- **requirement**: A correct implementation should not exhibit the listed behavior: retaining the 500 error page when module import or page rendering fails.
- **mutation**: It is not advisable to expand the failure of the incorrect page into a new abnormal contract. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0034

[patch](patches/P-0034-d35c6a8b04db.patch)
SHA-256: d35c6a8b04db10c9a07f33de708dbc22eea8da71b7348f2aee3ee6f60654b203

### VP-0035: Targeted regression: Retain call and index bytes for the search public entrance under the given configuration

- **requirement**: Retain call and index bytes for the search public entrance under the given configuration
- **mutation**: Targeted regression: Retain call and index bytes for the search public entrance under the given configuration (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0035

[patch](patches/P-0035-d6b559192cf1.patch)
SHA-256: d6b559192cf1747bcfc7a0c9124badf39da9d1bd9528ed68882d58dfebfa75c0

### VP-0036: Use the instance configuration.

- **requirement**: A correct implementation should not exhibit the listed behavior: retaining the 404 error page for an unknown module request.
- **mutation**: Use the instance configuration. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0036

[patch](patches/P-0036-db062365117d.patch)
SHA-256: db062365117de649d6925c77c6aed88d6ede27125adaca1a0d7baf7ab8aa7c08

### VP-0037: HEAD No Text

- **requirement**: Both entries on the HTTP homepage are retained for index responses.
- **mutation**: HEAD No Text (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0037

[patch](patches/P-0037-e3fa737ae595.patch)
SHA-256: e3fa737ae595b27a0d94e1b055e5cd0652a3bf4a37148a5554cce18894ddf37a

### VP-0038: And the global last configuration at the time of the request.

- **requirement**: Configurations explicitly held or obtained by the server request rendering consumer instance
- **mutation**: And the global last configuration at the time of the request. (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0038

[patch](patches/P-0038-edcc775de335.patch)
SHA-256: edcc775de335d8ebe88231f2bddb7bc52679de9f1698321ec06a2768a4946706

### VP-0039: Return None

- **requirement**: pdoc static export maintains the directory output and returns None.
- **mutation**: Return None (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Test collection or environment error; The variation does not change the intended behavior.

## P-0039

[patch](patches/P-0039-fc8d660d3eec.patch)
SHA-256: fc8d660d3eecf106d00184890836678fab062ce2ac09b2e2102fdffef310a3a0

### VP-0040: Targeted regression: CLI server mode explicitly delivers this command configuration.

- **requirement**: The CLI server mode explicitly delivers this command configuration; observable results: the configuration of CLI options to the server instance is clearly defined.
- **mutation**: Targeted regression: CLI server mode explicitly delivers this command configuration. (changed files: pdoc/__init__.py, pdoc/__main__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Testing collected errors

## P-0040

[patch](patches/P-0040-fe9bf5e6c68d.patch)
SHA-256: fe9bf5e6c68d3eef07e6f04dd325465d5ac8c449b5d973a22c7aff5ad7e1e4fc

### VP-0041: Targeted regression: Search index skipped baseline RuntimeError import failed module and returned normally

- **requirement**: The search index skipped the baseline RuntimeError import failure module and returned normally; observable result: the faulty module did not enter the index, while the normal module remained, and the search response did not fail due to this import failure.
- **mutation**: Targeted regression: Search index skipped baseline RuntimeError import failed module and returned normally (changed files: pdoc/__init__.py, pdoc/render.py, pdoc/web.py)
- **setup**: Apply this patch to the clean baseline at 00e18eb12ae2, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Testing collected errors

