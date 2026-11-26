# Adversarial patches and verification points

Task: refactor-cattrs-dict-codegen-03
Base commit: bc34a466a878d3259d01d0169b3fb95420d7d50d

This package contains 22 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0002

[patch](patches/P-0002-0ae7bef21243.patch)
SHA-256: 0ae7bef2124370b7c078fa5d1d35a8f925c67a6407c12291a7d7634b5b11c784

### VP-0002: Change nonmapping TypeError text

- **requirement**: In detailed mode, preserve the mapping TypeError and its ClassValidationError wrapper. In fast mode, propagate the original exception without introducing a common input error.
- **mutation**: Change nonmapping TypeError text (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0003

[patch](patches/P-0003-1d6c603b7566.patch)
SHA-256: 1d6c603b7566e5ec4c3e9cbd4039ddf57954d806b4251a0a4449839030f523f9

### VP-0003: Truncate actual collected field failures

- **requirement**: The detailed mode error tree contains all failure fields; the mode source and explicit overrides are maintained, and the fast mode is not forced to be included in the detailed errors.
- **mutation**: Truncate actual collected field failures (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0004

[patch](patches/P-0004-239240404b4d.patch)
SHA-256: 239240404b4d2cde60f12a5087e0ad41b09f3f1302b20a030d00d809096c6689

### VP-0004: Lose actual extra-key set in fast error

- **requirement**: The explicit value of the forbid flag or the converter default value takes effect; False is used as a fallback. When a refusal occurs, the direct error type and extra_fields collection are retained.
- **mutation**: Lose actual extra-key set in fast error (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0005

[patch](patches/P-0005-24e449317bb7.patch)
SHA-256: 24e449317bb7269678bf2b6245ba3d52b9cb17e61a63a5f8578b10b7d84cb8af

### VP-0005: Change only public linecache default on make_dict_structure_fn

- **requirement**: Original signature, from_converter default value, linecache, and kwargs remain. The values and types received by the hook are preserved.
- **mutation**: Change only public linecache default on make_dict_structure_fn (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0006

[patch](patches/P-0006-297d84d44808.patch)
SHA-256: 297d84d448087a3b37f609f9c1251bf660f15ac822accbff408da848ade6ac17

### VP-0006: Register source with linecache disabled

- **requirement**: Generating a simple field model must not add entries to the cache.
- **mutation**: Register source with linecache disabled (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0009

[patch](patches/P-0009-406799e5d0c5.patch)
SHA-256: 406799e5d0c5c33ed0ff861bc8a6efe08996188423cbc9538da6867282854fc1

### VP-0009: Overwrite colliding source at same filename

- **requirement**: Each distinct generated result has a discoverable source without overwriting existing entries for different source code.
- **mutation**: Overwrite colliding source at same filename (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py, src/cattrs/gen/_lc.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0010

[patch](patches/P-0010-44501f80ef2d.patch)
SHA-256: 44501f80ef2d9108f402a73b25cf996f6293277269bde0022f7df82628c63269

### VP-0010: Change only public linecache default on make_dict_unstructure_fn

- **requirement**: The original signatures, linecache default values, and kwargs remain unchanged. The return value can be called as a single value entry.
- **mutation**: Change only public linecache default on make_dict_unstructure_fn (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0013

[patch](patches/P-0013-5f079cc784ab.patch)
SHA-256: 5f079cc784ab82b7543b1fd64093984db5c91212b33d70d4188f6e425af0746f

### VP-0013: Use fresh cache key for identical source

- **requirement**: Reuse an existing cache entry when equivalent configurations produce identical source code. Do not accumulate duplicate entries.
- **mutation**: Use fresh cache key for identical source (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py, src/cattrs/gen/_lc.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0015

[patch](patches/P-0015-65cdf29480a9.patch)
SHA-256: 65cdf29480a9152587b9aa91edcfbcabde5820938da80db46b3223ceb338343d

### VP-0015: Ignore converter alias default

- **requirement**: Use_alias reads from converter, BaseConverter reverts to False, explicit flag/rename takes precedence, and the constructed result is maintained.
- **mutation**: Ignore converter alias default (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0016

[patch](patches/P-0016-729a99aabea6.patch)
SHA-256: 729a99aabea614bd8c6d79eba525d823da20016d5ffa7893786d7d0afa852e22

### VP-0016: Change only public linecache default on make_dict_structure_fn_from_attrs

- **requirement**: The public signature/default values and kwargs remain unchanged. The type mapping and existing flags can still be called and returned through the structure hook.
- **mutation**: Change only public linecache default on make_dict_structure_fn_from_attrs (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0017

[patch](patches/P-0017-7375a0bcf465.patch)
SHA-256: 7375a0bcf46543b0810c78311b33ed1956cc1c8c28c03c473c27c67dd80641d8

### VP-0017: Change only public linecache default on make_dict_unstructure_fn

- **requirement**: The hook that returns the correct call shape, with the original signature, default flags, and kwargs available.
- **mutation**: Change only public linecache default on make_dict_unstructure_fn (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0018

[patch](patches/P-0018-78a920dd2149.patch)
SHA-256: 78a920dd21495e69cc9865b2d97fc87ff64e941efd732b7fbe6823f5cc5c5ff0

### VP-0018: Ignore converter preference for attribute converters

- **requirement**: The conversion results of preference settings for reading sources, backouts, and explicit field hooks are consistent with the baseline.
- **mutation**: Ignore converter preference for attribute converters (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0021

[patch](patches/P-0021-82899aadef8e.patch)
SHA-256: 82899aadef8eefa0e59087c7f74d6a55d81c49ea0a3920070c0956050b045b6f

### VP-0021: Duplicate live TypedDict __init__ responsibility while preserving all returned v

- **requirement**: The actual generation of names is handled through common responsibilities; specific function names or private identifiers are not checked.
- **mutation**: Duplicate live TypedDict __init__ responsibility while preserving all returned values (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0023

[patch](patches/P-0023-a6e0879cf53f.patch)
SHA-256: a6e0879cf53f003a2df0223f471a9611121ce27ac31039d6a605ffe262f749fa

### VP-0024: Duplicate live TypedDict wrap_field_try_except responsibility while preserving a

- **requirement**: The core common error packaging mechanism is centralized, while the processing and diagnosis of family-specific fields can be separated.
- **mutation**: Duplicate live TypedDict wrap_field_try_except responsibility while preserving all returned values (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0024

[patch](patches/P-0024-cc70a0f7cd62.patch)
SHA-256: cc70a0f7cd62986713a61487ee99a2f8ca69dac78f2ba9ebcebb826eb8feb19a

### VP-0025: Lose actual extra-key set in detailed error

- **requirement**: ClassValidationError contains the same ForbiddenExtraKeysError and an unknown set of keys.
- **mutation**: Lose actual extra-key set in detailed error (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0025

[patch](patches/P-0025-d7c05499eff7.patch)
SHA-256: d7c05499eff7edee191b5bb59d24f1b93250b40232793274c6b6802e5b51fece

### VP-0026: Change only public linecache default on make_dict_structure_fn

- **requirement**: The hook that returns the correct call shape, with the original signature, default flags, and kwargs available.
- **mutation**: Change only public linecache default on make_dict_structure_fn (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0026

[patch](patches/P-0026-d8e8cc9ff7e5.patch)
SHA-256: d8e8cc9ff7e5f234ac64c51b0a0c17f0095d96753eb6c38ba8a6cc7c61233cf6

### VP-0027: Ignore explicit omit on TypedDict unstructure

- **requirement**: The necessary keys for valid input are retained; the keys that are processed according to the baseline are omitted, and the specified keys are not included.
- **mutation**: Ignore explicit omit on TypedDict unstructure (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0027

[patch](patches/P-0027-d9845823784e.patch)
SHA-256: d9845823784e7fd4ac952c8a86a99d13f49ef8b4783dec230d42abd35e222565

### VP-0028: Targeted regression: Each path actually executes to the same shared generation boundary, from which the executable hook source code is assembled.

- **requirement**: Each path actually executes to the same shared generation boundary, which assembles the executable hook source code; it is not a unused facility or a shell.
- **mutation**: Targeted regression: Each path actually executes to the same shared generation boundary, from which the executable hook source code is assembled. (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

### VP-0029: Targeted regression: The execution of field processors and others depends on the shared mechanism.

- **requirement**: The execution of field processors and others depends on the shared mechanism.
- **mutation**: Targeted regression: The execution of field processors and others depends on the shared mechanism. (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

### VP-0030: Targeted regression: The shared generated boundary actually compiles and produces callable hooks.

- **requirement**: The shared generated boundary actually compiles and produces callable hooks.
- **mutation**: Targeted regression: The shared generated boundary actually compiles and produces callable hooks. (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

### VP-0031: Targeted regression: The common boundaries have overrides, and the data for independent fields is provided by each party.

- **requirement**: The common boundaries have overrides, and the data for independent fields is provided by each party.
- **mutation**: Targeted regression: The common boundaries have overrides, and the data for independent fields is provided by each party. (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0029

[patch](patches/P-0029-e100e4c835f8.patch)
SHA-256: e100e4c835f89dac177946be390b8c4f065df1351520a912cb03d59e9faf2a91

### VP-0033: Ignore TypedDict output rename

- **requirement**: Use the correct output and restore key names and remove the original or overridden name according to the existing rules.
- **mutation**: Ignore TypedDict output rename (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0032

[patch](patches/P-0032-ec35014b39d1.patch)
SHA-256: ec35014b39d1e59801ba1124b6d6dbe9f5b41d72d2c4e25e4543dac2eb153ae1

### VP-0036: Copy no-transform TypedDict instead of preserving identity

- **requirement**: The return value must be the same object as the input (the is comparison is True).
- **mutation**: Copy no-transform TypedDict instead of preserving identity (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0033

[patch](patches/P-0033-ec61ce83b12a.patch)
SHA-256: ec61ce83b12a855478370a2e308f64598c9344f75f856a2c2a6c8f9d5f3d2471

### VP-0037: Change only public linecache default on make_dict_unstructure_fn_from_attrs

- **requirement**: Keep the public signature/default values and kwargs. Return an available unstructure hook when an Attribute list is passed in, including the linecache option.
- **mutation**: Change only public linecache default on make_dict_unstructure_fn_from_attrs (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

## P-0036

[patch](patches/P-0036-fdfb9fd5df45.patch)
SHA-256: fdfb9fd5df458676bbdcd8929fccc4d58186659f912c1cf0980cbff685399933

### VP-0040: Change class diagnostic note text only

- **requirement**: The name/type/text of AttributeValidationNote is the same as the baseline. The diagnostic statements for class and typeddict are retained respectively.
- **mutation**: Change class diagnostic note text only (changed files: src/cattrs/gen/__init__.py, src/cattrs/gen/_shared.py, src/cattrs/gen/typeddicts.py)
- **setup**: Apply this patch to the clean baseline at bc34a466a878, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. target input branch not reached; collection/import error; missing exact nodes

