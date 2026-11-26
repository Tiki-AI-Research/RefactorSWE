# Adversarial patches and verification points

Task: refactor-boxes-generator-registry-06
Base commit: d23a70c4912258407161243ed50e06f126d3fca8

This package contains 33 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-05827277ad52.patch)
SHA-256: 05827277ad5268fdcf8c89e7eb2e15d658d339028b04af270477af2ede369290

### VP-0001: Duplicate generator does not increase the number of group members

- **requirement**: No additional copies of the group member names sequence were found before and after the repeated search.
- **mutation**: Duplicate generator detection does not increase the number of group members; fix the target mapping: restrict to the correct target statement after def generators_by_name() -> dict[str, type[boxes.Boxes]]: (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0002

[patch](patches/P-0002-0f767226e35e.patch)
SHA-256: 0f767226e35e4a9e5d484851928262dbee2107216672c4964fbcb69753a42978

### VP-0002: The shared class discovery cache must allow later discovery of extensions in the same process.

- **requirement**: First take the directory and then provide an extension generator. Subsequent checks show that the value is 196, while the original 195 keys are all retained.
- **mutation**: The shared class discovery cache must allow later discovery of extensions in the same process. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0003

[patch](patches/P-0003-1e1d74e59889.patch)
SHA-256: 1e1d74e598896477cef4a8e413d60d8df9e666691f0a052b91cd8e2c5a712553

### VP-0003: Both complete, Web, and grouped views share a reusable discovery cache.

- **requirement**: The structure or call observation proves that each view shares the discovery source and cache reuse, without restricting the directory API name.
- **mutation**: Both complete, Web, and grouped views share a reusable discovery cache. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0004

[patch](patches/P-0004-1e7b77b45804.patch)
SHA-256: 1e7b77b45804a019a15758c246354e9d465fb23f6b27e473034d3ede389d63db

### VP-0004: The gallery items come from shared directory views.

- **requirement**: The data traversed by the gallery can be traced back to the directory view, allowing indirect access through server properties' attributes'
- **mutation**: The gallery items come from shared directory views. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0005

[patch](patches/P-0005-1ecc8fce2bd1.patch)
SHA-256: 1ecc8fce2bd129d0181459980baa55089ac3479a87937b48ae43e3023537766e

### VP-0005: The generator finds no way to leave the package path unchanged permanently

- **requirement**: Set the additional directory and call the __path__ content of the preceding and following packages; the content does not increase permanently due to the discovery of extensions.
- **mutation**: The generator finds no way to leave the package path unchanged permanently (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0006

[patch](patches/P-0006-30fff6bd06ee.patch)
SHA-256: 30fff6bd06ee7f6fbb4da6672e0f33db53d9a86001279e6555592e19d091dd68

### VP-0006: The module discovery function reads additional directories separated by colons.

- **requirement**: Each additional directory module is mapped to an import object by its short name, and the bundled modules are not lost.'
- **mutation**: The module discovery function reads additional directories separated by colons. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0007

[patch](patches/P-0007-3859639339d5.patch)
SHA-256: 3859639339d5f23863cb6e7758c3f0170bb7641db68b13b5ee10d4aaf4a1704e

### VP-0007: Team members remain sorted by generator name

- **requirement**: "Each group of generator name sequences conforms to the baseline sorting rules"
- **mutation**: Team members remain sorted by generator name (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0008

[patch](patches/P-0008-3b58c11da5c6.patch)
SHA-256: 3b58c11da5c62e4880f49029edfa12bc2a6f0500cb74cbecbaf56b6f9e7e2336

### VP-0008: Avoid repeated visits to the gallery to prevent group growth.

- **requirement**: Before and after accessing the gallery, the group member sequence does not accumulate copies, including duplicate access to existing HTML caches
- **mutation**: Avoid repeated visits to the gallery to prevent group growth. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0009

[patch](patches/P-0009-4061a09eb1de.patch)
SHA-256: 4061a09eb1de7eb78bc8e7a04370f47ffaec5b876023717eff6bd8195be14453

### VP-0009: Module discovery preserves the zero-argument mapping from short names to imported modules.

- **requirement**: The module shortname key corresponds to the same ModuleType object and baseline module range as the module shortname.
- **mutation**: Module discovery preserves the zero-argument mapping from short names to imported modules. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0010

[patch](patches/P-0010-4417531decb6.patch)
SHA-256: 4417531decb64f633f69930e0f08d11aa8fec919a97d1ae5c94db0da7dc4147c

### VP-0010: The bundled generator ontology and Web/UI group classification remain unchanged.

- **requirement**: The patch does not modify the generator ontology. The webinterface/ui_group of the class is consistent with the frozen baseline. The organization of the directory packages is checked separately according to the directory obligations.
- **mutation**: The bundled generator ontology and Web/UI group classification remain unchanged. (changed files: boxes/generators/__init__.py, boxes/generators/abox.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0011

[patch](patches/P-0011-56329dc05c48.patch)
SHA-256: 56329dc05c4868a1566d12f2b47e40a9034c5b8d177046278f263a475686cbfb

### VP-0011: The generator snapshot consumption retrieves the Web generator from the shared directory.

- **requirement**: The data source for snapshot/consumption search is the web view directory. It does not exist when permanently importing the source.
- **mutation**: The generator snapshot consumption retrieves the Web generator from the shared directory. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0013

[patch](patches/P-0013-58a661d72d9a.patch)
SHA-256: 58a661d72d9a0a8128e85e0813e64f5c4f1a234a1993d205374a431c247744a9

### VP-0013: Repeatedly obtaining the Web directory does not increase the number of group members

- **requirement**: Repeated retrieval of Web views does not result in cumulative additional copies of group members
- **mutation**: Repeatedly obtaining the Web directory does not increase the number of group members (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0014

[patch](patches/P-0014-63c3fb428310.patch)
SHA-256: 63c3fb4283100e541d468e6978e93f3c6425546faa42cc16b3f1bbdbd0a8e86b

### VP-0014: The server only exposes all enabled Web generators.

- **requirement**: The server name collection and group members comply with Web subset 182, no prohibited classes are mixed in
- **mutation**: The server only exposes all enabled Web generators. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0015

[patch](patches/P-0015-6471000009f7.patch)
SHA-256: 6471000009f74cc5a552b7f6e57e742c063028203f0d1e5ff1f84cd3c25ee436

### VP-0015: CLI generator entries are unique, and there is exactly one HolePattern.

- **requirement**: Both the single and consecutive lists should be one line per person, and the HolePattern count should be 1
- **mutation**: CLI generator entries are unique, and there is exactly one HolePattern. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0016

[patch](patches/P-0016-666f9ff01ed9.patch)
SHA-256: 666f9ff01ed91994c54ee4b1ec59b3a9ed3f3e5b6f3a61290f7747a57149a59f

### VP-0016: UIGroup retains field and image property semantics.

- **requirement**: Existing fields are available, and the default title matches the baseline with/without image attribute values.
- **mutation**: UIGroup retains field and image property semantics. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0017

[patch](patches/P-0017-692f35ab7f54.patch)
SHA-256: 692f35ab7f54cac4b7e02e8e60d79b0f911bda52cce588c623da087254c0f7d5

### VP-0017: The server build obtains the generator and groups through the shared directory.

- **requirement**: Use directory views for constructing data flows, no longer having the link to discover independently and add global groups.'
- **mutation**: The server construction obtains the generator and groups through the shared directory; fixed the target mapping: the correct target statement is limited to after class BServer:. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0018

[patch](patches/P-0018-7a9097b33aaf.patch)
SHA-256: 7a9097b33aaf1fd5cf249a494ed5d91bf2333a4cebc6faf1a5026909c1937c0d

### VP-0018: Unknown declaration group name falls back to Misc

- **requirement**: Normally discovered and declared as an unknown group name appears in Misc
- **mutation**: Unknown declaration group name falls back to Misc (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0019

[patch](patches/P-0019-7e7a84193759.patch)
SHA-256: 7e7a841937594a89a3f3747ffdce00799017074c4c7b3d6ea87131c7deed731a

### VP-0019: Keep the CLI list in its complete output format.

- **requirement**: ['Output Prefix, Group Title Description, Blank Line, Name Width, Description Processing, ANSI and Correct Baseline First List Consistency']
- **mutation**: Keep the CLI list in its complete output format. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0020

[patch](patches/P-0020-8a5a1fa85554.patch)
SHA-256: 8a5a1fa8555476150c85873536d4d65c3846a74e050ce756f683474f6c915cd7

### VP-0020: Duplicate generator does not increase the number of group members

- **requirement**: No additional copies of the group member names sequence were found before and after the repeated search.
- **mutation**: Duplicate generator detection does not increase the number of group members; fix the target mapping: restrict to the correct target statement after def generators_by_name() -> dict[str, type[boxes.Boxes]]: (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **version_note**: The original audit retired this verification point. It is retained for historical reference.
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0021

[patch](patches/P-0021-9264914f89cb.patch)
SHA-256: 9264914f89cb7f9213caccc79e2acd273b4883ddda51ba32108ec6326e714542

### VP-0021: Continuously constructing servers does not increase or contaminate Web group members

- **requirement**: The set of Web group names for the new and old servers is unique. The CLI results are still consistent with the respective Web generator sets.
- **mutation**: Continuously constructing servers does not increase or contaminate Web group members (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0022

[patch](patches/P-0022-93da70111951.patch)
SHA-256: 93da70111951248ed6e9bfbfc9599335e58f896a32cd2803a096d1cd8985004f

### VP-0022: CLI list retrieves data from the shared directory

- **requirement**: CLI data extraction/grouping data stream arrives at directory, independent scanning sources are eliminated
- **mutation**: CLI list retrieves data from the shared directory; fix in target mapping: restrict to the correct target statements after def generators_by_name() -> dict[str, type[boxes.Boxes]]: (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **version_note**: The original audit retired this verification point. It is retained for historical reference.
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0023

[patch](patches/P-0023-a5d5dc1c9f30.patch)
SHA-256: a5d5dc1c9f307d47db1d8421e4c93fa44d823924b93620888f311f13f03f8087

### VP-0023: Module discovery does not permanently modify the package path

- **requirement**: Set the additional directory and call the __path__ content of the preceding and following packages; the content does not increase permanently due to the discovery of extensions.
- **mutation**: Module discovery does not permanently modify the package path (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0024

[patch](patches/P-0024-a86c2040661a.patch)
SHA-256: a86c2040661aca1d823461d841208e0a089c6b12e7729277bf2a23e28608ff15

### VP-0024: The shared module discovery cache permits later discovery of extension modules in the same process.

- **requirement**: ['Table of Contents has additional extensions after use. Subsequent modules can be mapped to extended ModuleType. The bundled modules are retained.'
- **mutation**: The shared module discovery cache permits later discovery of extension modules in the same process. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0025

[patch](patches/P-0025-ad3269805e88.patch)
SHA-256: ad3269805e8872bd6e2321a76a9413e5b4d7f2a4a6e0afee28b7c6247ab63363

### VP-0025: Table of Contents Web View retains all 182 enabled generators

- **requirement**: The bundled Web name set corresponds to the enabled categories, totaling 182. The disabled classes are excluded, but the complete directory is still retained.
- **mutation**: Table of Contents Web View retains all 182 enabled generators (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0026

[patch](patches/P-0026-b4978ebc2430.patch)
SHA-256: b4978ebc24307b6b816882b88abe82ac83e2c7d41b5f9ec7f23478b9b90d130d

### VP-0026: Group definitions remain importable, with their existing order and metadata.

- **requirement**: Group name order, title, description, image base name and baseline are consistent. The corresponding groups can be accessed by name mapping.
- **mutation**: Group definitions remain importable, with their existing order and metadata. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0027

[patch](patches/P-0027-b752358069b2.patch)
SHA-256: b752358069b28b17fdd771615161dbf56bea330a0fedf3d96bc8357bfae0f228

### VP-0027: The complete generator found no parameter-less classes and continuous bundled key sets.

- **requirement**: The complete set of keys returned consecutively is the same as the baseline, which is 195. The value corresponds to the corresponding class. The alias keys formed by the scanning module are retained.
- **mutation**: The complete generator found no parameterless class mappings and continuous bundled key sets; fixed the target mapping: limited to the correct target statements after def getAllBoxGenerators() (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0028

[patch](patches/P-0028-cc0a7b1c395e.patch)
SHA-256: cc0a7b1c395effeca0f82718e3bf000668e590ce15b8a8720ce9161123b00eeb

### VP-0028: The server maintains the existing construction parameters and object attribute states.

- **requirement**: Available for both construction calls, boxes is a mapping from names to classes, and groups are ordered and can be queried by groups_by_name.
- **mutation**: The server maintains the existing construction parameters and object attribute states. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0029

[patch](patches/P-0029-cc366b024182.patch)
SHA-256: cc366b0241822795f6a0b10ccd5f09408d5685c995c05ee0b5acdb70b51aeada

### VP-0029: Discovering to read the additional directories separated by colons

- **requirement**: Accessible from various additional directory classes in the public colon syntax, with keys using the same module plus class name scheme. The bundled keys are not lost.
- **mutation**: Discovering to read the additional directories separated by colons (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0030

[patch](patches/P-0030-cdad364be975.patch)
SHA-256: cdad364be9758cab0c203875de050b8bf6bca4730fb7af11f46fdd7a20548b10

### VP-0030: Independent snapshot branch: The directory and server remain at 182, and the public GENERATOR snapshot has deleted ABox.

- **requirement**: The bundled Web name set corresponds to the enabled categories, totaling 182. The disabled classes are excluded, but the complete directory is still retained.
- **mutation**: Independent snapshot branch: The directory and server remain at 182, and the public GENERATOR snapshot has deleted ABox. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0031

[patch](patches/P-0031-e686bdf5a298.patch)
SHA-256: e686bdf5a298968f31aff2824fedf3f96fc1338a22af0a2ec4acb50b0c8d36e1

### VP-0031: Continuous CLI groups or lists do not increase the number of group members

- **requirement**: Repeated operations must not accumulate duplicate members in any group's name sequence.
- **mutation**: Continuous CLI groups or lists do not increase the number of group members (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0032

[patch](patches/P-0032-f0e1652c68dd.patch)
SHA-256: f0e1652c68ddf8d1e628ec1295c52a1f964b566908db3f4fa5d0f14933a128dd

### VP-0032: The server build obtains the generator and groups through the shared directory.

- **requirement**: Use directory views for constructing data flows, no longer having the link to discover independently and add global groups.'
- **mutation**: The server construction obtains the generator and groups through the shared directory; fixed the target mapping: the correct target statement is limited to after class BServer:. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0033

[patch](patches/P-0033-f9a9253c2220.patch)
SHA-256: f9a9253c2220298dd3aba015254b24d9076cc1cdf5a55686dac59c9492566c68

### VP-0033: CLI list retrieves data from the shared directory

- **requirement**: CLI data extraction/grouping data stream arrives at directory, independent scanning sources are eliminated
- **mutation**: CLI list retrieves data from the shared directory; fix in target mapping: restrict to the correct target statements after def generators_by_name() -> dict[str, type[boxes.Boxes]]: (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

## P-0034

[patch](patches/P-0034-fa3acd5af916.patch)
SHA-256: fa3acd5af91676b56e2283170c6f92a3ddf3d9e1cd1f92209041b58015da19a2

### VP-0034: Each Web generator in the gallery has exactly one entry.

- **requirement**: 'HTML Generator Entry Name Set Equal to Web Server Set, Count 1, Also Has an Entry Without Images'
- **mutation**: Each Web generator in the gallery has exactly one entry. (changed files: boxes/generators/__init__.py, boxes/scripts/boxes_generator.py, boxes/scripts/boxes_main.py, boxes/scripts/boxesserver.py, among others)
- **setup**: Apply this patch to the clean baseline at d23a70c49122, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out.

