# Adversarial patches and verification points

Task: linkedin-shiv-20260909075226-5d5ed5
Base commit: ff542cbe75ea832df3a989d07c7fdf5214f727fa

This package contains 45 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-11655f1fc3b6.patch)
SHA-256: 11655f1fc3b60ae5c3e7e06793ac5cce68963ac224f303dbc2e4f3ae7cbda0f8

### VP-0001: Archive files remain in executable mode.

- **requirement**: The stat function in POSIX environments has user/group/other execution bits.
- **mutation**: Archive files remain in executable mode. (changed files: src/shiv/cli.py, src/shiv/builder.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0002

[patch](patches/P-0002-129257b99532.patch)
SHA-256: 129257b99532d72073a623305301f98ff604fecb4dd161f1448fcc3fcfba9e90

### VP-0002: First and forced materialization of correct unpacked bundled dependencies

- **requirement**: The archived site-packages members appear in the cache. Force overwrites of modified content.
- **mutation**: First and forced materialization of the correct unpacked bundled dependencies; ignore force override (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0003

[patch](patches/P-0003-17c3ce44b77f.patch)
SHA-256: 17c3ce44b77f7804b878d0a10517f0922157a20af757b7f10a285828835235d7

### VP-0003: Compiler -m Mode maintains module execution

- **requirement**: run_module(__main__) and the argv of the module name/ subsequent parameters, the stream, and the exit status
- **mutation**: Compiler -m mode retains module execution; -m does not have a __main__ execution name (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0004

[patch](patches/P-0004-188c6a61bf56.patch)
SHA-256: 188c6a61bf56bf6d2d14183d78bb04a2e8ae56938c51e803ed847a36e9a4c927

### VP-0004: The existing options and default parsing/tunneling contracts remain unchanged.

- **requirement**: Options names/aliases/defaults, help/version, and UNPROCESSED pip parameter parsing remain unchanged.
- **mutation**: Keep the existing options and default parsing/typing contracts; disrupt the variable-length pip parameter parsing. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0005

[patch](patches/P-0005-24b5b59817ba.patch)
SHA-256: 24b5b59817baeb2c818c4d55b857b14729eb4ba1d733be7933987b870f390a94

### VP-0005: Keep the shebang configuration

- **requirement**: If the target start byte is the same as the specified or default shebang, an extended error is retained.
- **mutation**: Keep the shebang configuration; ignore custom shebang settings. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0006

[patch](patches/P-0006-28b7712d1337.patch)
SHA-256: 28b7712d1337c60bb32cb6477ff22c75c258de2c54a7d46155320c1f251c870e

### VP-0006: The existing site-packages are still being collected and entering the final archive.

- **requirement**: Individual or duplicate directory sources and their order/path resolution, file dependency content
- **mutation**: Existing site-packages are still being collected and entering the final archive; existing dependency paths are not being collected. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0007

[patch](patches/P-0007-30ef54c4fd6f.patch)
SHA-256: 30ef54c4fd6fe1635379905d6f06bb461026f4df21b666c39a8e6f3f2522f164

### VP-0007: Prepare pip input in a temporary directory, preserving the original arguments and the rules for merging an existing directory.

- **requirement**: The target/args passed to install, the staged content, and the original directory are not modified by pip.
- **mutation**: The pip input is prepared in the temporary directory and maintains the original parameters and existing directories; the passed-through pip parameters are discarded. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0008

[patch](patches/P-0008-3fbc327ed649.patch)
SHA-256: 3fbc327ed649dd5b5bb7aaf4562e8b35b3896ca549f14c41e318d61a1255640a

### VP-0008: Archive and retain the runnable startup structure

- **requirement**: The file site-packages/_bootstrap/environment.json/__main__.py exists and can start the dependency environment as originally intended.
- **mutation**: Archive and retain the runnable startup structure; can generate a zip file, but the startup structure cannot run. (changed files: src/shiv/cli.py, src/shiv/builder.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0009

[patch](patches/P-0009-437b2098f8f3.patch)
SHA-256: 437b2098f8f3f52d38f8d20b5edb2bd19b652be2abd8b1aa1a012db2534a3b21

### VP-0009: Prepare independently to return results containing staged inputs and resolved config.

- **requirement**: Returned results and staged paths are present, initial Environment fields are set, target not written; preamble staging is still available for subsequent emission.
- **mutation**: Prepare independently to return results containing staged inputs and resolved config; write the target before preparation. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0010

[patch](patches/P-0010-494ced07f374.patch)
SHA-256: 494ced07f374ed0c5f5701ab90ac911bb9cdd56d07a5e57a2b0a40c6fb7ccd1e

### VP-0010: Select to return requests that have been checked and have executable behavior. Three types of executions maintain latency.

- **requirement**: The return request is checkable and executable; no calls to application/interpreter/preamble have occurred before returning.
- **mutation**: Select to return requests that have executable behavior. Three types of executions maintain latency; immediate execution of callables upon selection. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0012

[patch](patches/P-0012-5f262e5a2081.patch)
SHA-256: 5f262e5a2081a85549d3b98b98f31373f2cc6c977a6486693ce9f8676e7db0ba

### VP-0012: Generate the final cache path evaluation for bootstrap delegation to the lifecycle.

- **requirement**: The lifecycle is responsible for path resolution and providing the location for producing site-packages. The bootstrap does not calculate the final target outside the boundaries.
- **mutation**: Produce the bootstrap delegation final cache path evaluation for the lifecycle; produce the bootstrap evaluation outside the boundary for the final target. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0014

[patch](patches/P-0014-746c0b01da35.patch)
SHA-256: 746c0b01da353f9a47b006f20c79ee368bdbd06bd5fa3189f71b7f2d7977ff66

### VP-0014: Compression Selection Retention

- **requirement**: Zip entries compression type matches the configured ZIP_DEFLATED/ZIP_STORED.
- **mutation**: Keep compression options as is; reverse compression configuration (changed files: src/shiv/cli.py, src/shiv/builder.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0015

[patch](patches/P-0015-7a74c61a4922.patch)
SHA-256: 7a74c61a4922716af9562489e5eb79ce5b0625433d3b44c15b2c7966b241128e

### VP-0015: Explainer -c mode retains the content and parameter execution

- **requirement**: Check execution results, sys.argv with -c and the additional arguments, original main-module fields, streams, exit status, and parsing errors.
- **mutation**: Explainer -c mode preserves the content and parameters; -c discards the subsequent argv (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0016

[patch](patches/P-0016-7bb66c6dc788.patch)
SHA-256: 7bb66c6dc788c7a0f44e406fe7ac086fc6de2601dc4117c0c847de4607c681f9

### VP-0016: If the independent console-script cannot be parsed, an error has already occurred.

- **requirement**: Both metadata and bin have NO_ENTRY_POINT, stream, and exit; there is no error rejection when there is bin.
- **mutation**: When the independent console-script cannot be parsed, an error has already occurred; changing the unparsed console-script error remains unchanged. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0017

[patch](patches/P-0017-7c768e89969b.patch)
SHA-256: 7c768e89969b5c68237850d6e0df6c9f0607258674859e72939b3d0ed11b728a

### VP-0017: force Boolean parsing and default fallback retained

- **requirement**: Yes/T/1 and false value parsing, always_write_cache defaults to rollback
- **mutation**: force: Boolean parsing and default fallback are retained; force treats a non-empty string of false as true. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/environment.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0018

[patch](patches/P-0018-7fffa0e0e482.patch)
SHA-256: 7fffa0e0e482a5a69454f1d957610acdb415fefc240f15ceedcd627185463017

### VP-0018: The configuration of the four entry flags is persisted.

- **requirement**: The entry_point/script field in environment.json; independent console-script metadata parsing or bin fallback is maintained.
- **mutation**: The configuration of the four entry flags is persisted; the double-flag archive loses the script field. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0019

[patch](patches/P-0019-816373a7da45.patch)
SHA-256: 816373a7da4577928ad74a6551d985a62ed57fec85894ca7bf22831fff1cf5a7

### VP-0019: Cache root override and naming rules remain unchanged

- **requirement**: Final path of SHIV_ROOT/metadata/default, $variables, and expanduser, archive basename/build_id name
- **mutation**: Cache root override and naming rules remain; cache names are lost with build_id (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0020

[patch](patches/P-0020-83e95a5574f7.patch)
SHA-256: 83e95a5574f7de06a98d38cafca3678c020dbb27d6fe1abb8ab8cccff4cb9c86

### VP-0020: console-script Executes the target according to the existing path. Select 'script' for two fields.

- **requirement**: The behavior of site-packages/bin/script run_path(__main__), the original argv/stream, and the exit status are described in two fields. These fields do not involve the callable function.
- **mutation**: console-script: The target is executed according to the existing path. Select 'script' for two fields; if there is an error with two fields, select 'callable'. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0021

[patch](patches/P-0021-841e66c4a70f.patch)
SHA-256: 841e66c4a70f30e1c68100b7ade93f375150c092ccfd4c8f6916467144ad2729

### VP-0021: Ignore explicit workers configuration, fixed workers=1

- **requirement**: Compilation occurs only when requested. The quiet/workers argument and invalid integer backtracking are retained.
- **mutation**: Ignore the explicit workers configuration, fix it to workers=1; narrow down the original workers0 instrument confusion (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0022

[patch](patches/P-0022-8c013b7748f0.patch)
SHA-256: 8c013b7748f01691d240bc023b14be05ac4ae3522fed1e29cb1977db956aae3e

### VP-0022: Keep the interaction mode when there are no targets or parameters.

- **requirement**: code.interact is called and retains the dependent environment and standard flow.
- **mutation**: Keep the interaction mode when there are no targets or parameters; the interaction entry does not call interact. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0023

[patch](patches/P-0023-9494801231f1.patch)
SHA-256: 9494801231f16d736eed405618b3e8834706f8175d53f9c01be9f5993e51c57e

### VP-0023: preamble is executed in the context and precedes the main objective.

- **requirement**: Preserve the Python-injected archive, env, and site_packages values or the non-Python subprocess behavior, the preamble, and the order of application and interpreter events.
- **mutation**: Preamble is executed in the context of the existing setup and precedes the main objective; Preamble context archive error (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0024

[patch](patches/P-0024-9c26b17825a6.patch)
SHA-256: 9c26b17825a67d1703680e568c36b97680548ce56c4dd462c5de7fe52c4ba4c5

### VP-0024: Explainer script path pattern remains read-only and executable

- **requirement**: Script execution, script path argv/__file__, original error text, and stream/exit
- **mutation**: The interpreter script path mode remains read-only and executable; script __file__ error (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0025

[patch](patches/P-0025-9f412bf4038b.patch)
SHA-256: 9f412bf4038b3c212748c349ae4a05cb33106402f6e0d6d7dacb573fded672ff

### VP-0025: Effective cache hit and non-force, no materialized side effects.

- **requirement**: Do not call archive.extract, chmod, or compile. Preserve the existing cache contents.
- **mutation**: Effective cache hit and no force, no materialized side effects; cache hit still retrieves the modified permission. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0026

[patch](patches/P-0026-a65beadb0eb4.patch)
SHA-256: a65beadb0eb4749975f0c844d65ad4a3b9ab821513123ccbbd77b690016cb7ab

### VP-0026: The lifecycle actually coordinates the materialized process, not just idling or overall forwarding.

- **requirement**: The lifecycle is responsible for actually carrying out and coordinating each step; focused helpers can collaborate.
- **mutation**: The lifecycle actually coordinates the materialized process, not just idling or overall forwarding; the lifecycle's overall forwarding returns to the procedural monolith. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0027

[patch](patches/P-0027-a718cacf86f6.patch)
SHA-256: a718cacf86f649d1aa83fce750c6caf50a48d1380570c97309763aeb455b5c6b

### VP-0027: SHIV_INTERPRETER replaces the application with a non-empty string

- **requirement**: Non-empty 0/False: Still select the interpreter; empty string/Default: Select according to the original application; Not str_bool
- **mutation**: A nonempty SHIV_INTERPRETER string overrides the application setting. Parse a nonempty interpreter value of false as a Boolean. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/environment.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0028

[patch](patches/P-0028-a8dd75c08fef.patch)
SHA-256: a8dd75c08fefdb7a45c7014fb7fafbf4976a52be1c8e43e668284c929d3e2594

### VP-0028: The permissions to unpack the file have been restored.

- **requirement**: The selected file uses the stat mode match external_attr, but the executable script can still be executed.
- **mutation**: The archive permissions to unpack the file have been restored; unpacking permissions were lost. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0029

[patch](patches/P-0029-bb4c0a5509f3.patch)
SHA-256: bb4c0a5509f327ccca4351f0e5e9e27c59f16e8db4da5b02559be750bfe1deb9

### VP-0029: Compatible with active lifecycle of extraction helper calls

- **requirement**: The original signature is available. The actual reach of the lifecycle for the helper call path is as follows:
- **mutation**: Compatible with extraction helper calling active lifecycle; compatible with helper bypassing the lifecycle (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0030

[patch](patches/P-0030-bd49df9328f4.patch)
SHA-256: bd49df9328f44b3f2792e5fdb92abb324730723b8bb8836b694ccbd49e749d4a

### VP-0030: Existing failures with disabled pip parameters remain intact.

- **requirement**: DISALLOWED_ARGS corresponds to the reason for the error, stream, and exit. No new disabling rules have been added.
- **mutation**: Existing failures remain due to the prohibition of certain pip parameters; incorrect changes to prohibited parameters. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0031

[patch](patches/P-0031-c407f90826b8.patch)
SHA-256: c407f90826b8182baa3139e0240a0213301e9124d9d36eed0189c74cac94132a

### VP-0031: Existing failures with dependencies but no output paths remain unchanged.

- **requirement**: Preserve the original NO_OUTFILE text, output stream, and exit status.
- **mutation**: Existing failures with dependencies remain unchanged; changes that affect output paths are incorrect. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0032

[patch](patches/P-0032-c4307336b0ac.patch)
SHA-256: c4307336b0acc03f0da5704d6f603f398223765ef6a719d4d58667c2ba64a338

### VP-0032: Prepare failure: target missing or original content remains

- **requirement**: After failure, emission was not called. The missing target remains missing, or the bytes of the existing target remain unchanged.
- **mutation**: Preparation failure: target is missing or the original content remains; pip preparation failure destroys the target. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0033

[patch](patches/P-0033-c55083392714.patch)
SHA-256: c550833927146e67fdfb47bf975ae8c8aeb2f6b859f2684460ecac5fb1172f1c

### VP-0033: The callable target executes according to the existing import/call and handoff semantics.

- **requirement**: callable: Call, original argv/stream, propagation of return value to exit, entry_point: Independent configuration selection of callable
- **mutation**: The callable target executes according to the existing import/call and handoff semantics; the return value of the callable does not propagate. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0034

[patch](patches/P-0034-c6fd78bdad9f.patch)
SHA-256: c6fd78bdad9f7006848aee6e515be3052f2e551441b9cc02fe6702312e7d541a

### VP-0034: The help text still says the entry point takes precedence.

- **requirement**: --entry-point's historical priority help text remains unchanged
- **mutation**: Help still claims that the entry point takes precedence; removes the text about the priority of historical help. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0035

[patch](patches/P-0035-ca319b39bbd7.patch)
SHA-256: ca319b39bbd7d30e38e6c88d37b8ae2b216e5652e680d72e68ae1a3df31cbfe2

### VP-0035: Ignore explicit workers configuration, fixed workers=1

- **requirement**: Compilation occurs only when requested. The quiet/workers argument and invalid integer backtracking are retained.
- **mutation**: Ignore the explicit workers configuration, fix it to workers=1; narrow down the original workers0 instrument confusion (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0036

[patch](patches/P-0036-cfa3e50acbaf.patch)
SHA-256: cfa3e50acbaf81ae5690edd283f9947c99b061506c7edc4a164652ff8d0d6429

### VP-0036: The real bootstrap consumes the returned data after selection is returned.

- **requirement**: The behavior returned by the producer path call/consumer selector, without bypassing the request and directly running another target
- **mutation**: The real bootstrap consumes the returned behavior after selection is returned; the production path loses the return request and directly interprets the interpreter. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0037

[patch](patches/P-0037-d6b562005b39.patch)
SHA-256: d6b562005b39e78ebbd9dd481f6d01c37495f624e8ba0788277000b05e556071

### VP-0037: All four entry flags have been accepted

- **requirement**: The build acceptance status remains unchanged, no new rejection rules are added.
- **mutation**: Both of the four entry flags are accepted; adding a second flag results in rejection. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0038

[patch](patches/P-0038-de6f5c50efb5.patch)
SHA-256: de6f5c50efb57d299d4cc77ab35ceffeb6fcd6bab4f3a091f1da7fa0e4e73e44

### VP-0038: Replace and position the final directory after materialization completes.

- **requirement**: The deletion of the old directory during the force operation, the order of the temporary directory move, and the final location of the site-packages are maintained.
- **mutation**: Replace and position the final directory after materialization. The faulty placement introduces an extra directory level. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0039

[patch](patches/P-0039-e093509d3ffd.patch)
SHA-256: e093509d3ffd43619ca0fe3d6388af67777bd4658b884c8b7cbccb93fa503267

### VP-0039: Archived metadata is still readable for consumers

- **requirement**: environment.json field and shiv-info text/JSON output remain unchanged.
- **mutation**: The archived metadata is still readable for consumers; the shiv-info JSON lacks the archived metadata. (changed files: src/shiv/info.py, src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0040

[patch](patches/P-0040-e1ab535aa1df.patch)
SHA-256: e1ab535aa1dff3651ce245dd586d2a07fec805bf8d4605ed55151a07ec4b3832

### VP-0040: Actual emission consumption preparation return result

- **requirement**: Prepare return values to flow into emission in the production call path, without rerunning the entire preparation or bypassing the results.
- **mutation**: The real emission consumption preparation returns the result; emission coverage preparation returns the configuration. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0041

[patch](patches/P-0041-e3740b000a82.patch)
SHA-256: e3740b000a8296e0a8fc06fc6e110b34bc52aa254de445164e3dc9efdb291174

### VP-0041: Default content identity and explicit build_id are correctly persisted.

- **requirement**: environment.json.build_id should be consistent with the baseline content/relative name hash or user ID.
- **mutation**: The default content identity and explicit build_id are correctly persisted; the default content identity is a constant. (changed files: src/shiv/cli.py, src/shiv/builder.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0042

[patch](patches/P-0042-e5b8b191d839.patch)
SHA-256: e5b8b191d83973e216c4539f4b5fa10154db718ae5f7595b5db5f5046905e25e

### VP-0042: Interpreter - Mode maintains standard input execution

- **requirement**: The content of stdin is executed, along with the - and additional parameters, streams, and exit.
- **mutation**: Interpreter - The mode preserves the execution of standard input; the content of stdin is not executed (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0043

[patch](patches/P-0043-eaa990262e5f.patch)
SHA-256: eaa990262e5ffe0f70468af5e18bf58ee15c1a35891ea313ef44b33f3cef092a

### VP-0043: Target Environment Coverage Priority Maintenance

- **requirement**: The values of ENTRY_POINT/MODULE/metadata and CONSOLE_SCRIPT/metadata are rolled back, and the final goal remains unchanged.
- **mutation**: The priority of the target environment coverage is maintained; MODULE errors take precedence over ENTRY_POINT. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/environment.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0044

[patch](patches/P-0044-ee61eb4a0846.patch)
SHA-256: ee61eb4a084683bc87cd4e6d3b3d8010335d9ee2b38a0ffc79f474ac7b585c58

### VP-0044: SHIV_INTERPRETER replaces the application with a non-empty string

- **requirement**: Non-empty 0/False: Still select the interpreter; empty string/Default: Select according to the original application; Not str_bool
- **mutation**: A nonempty SHIV_INTERPRETER string overrides the application setting. Parse a nonempty interpreter value of false as a Boolean. (changed files: src/shiv/bootstrap/__init__.py, src/shiv/bootstrap/environment.py, src/shiv/bootstrap/interpreter.py, src/shiv/cli.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0045

[patch](patches/P-0045-f35a82c3663b.patch)
SHA-256: f35a82c3663bc0c137ce1146f56a012095cd8210ea666713e4bcc8ad500f1670

### VP-0045: Use handoff to clean up the original three entry environment variables.

- **requirement**: The three variables are deleted at the start of the callable/script, while other environments are retained; the interpreter still retains the original uncleaned semantics.
- **mutation**: Apply handoff to clean up the original three entry environment variables; handoff fails to clean up MODULE. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0046

[patch](patches/P-0046-f9bb22ba3c2a.patch)
SHA-256: f9bb22ba3c2a74784e97468f7b0ab4223a89e2400eecffd0ad21c6530f694695

### VP-0046: Existing failures remain unchanged without any dependent inputs.

- **requirement**: Preserve the original NO_PIP_ARGS_OR_SITE_PACKAGES text, output stream, and exit status.
- **mutation**: Existing failures remain unchanged; no errors occur in changes. (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

## P-0047

[patch](patches/P-0047-fdf3a4f55cfe.patch)
SHA-256: fdf3a4f55cfe8dcf6cd9b8988365f1235be2126f820657ae416f9fd907f36753

### VP-0047: Cache contention, serialization, and synchronous synchronization

- **requirement**: The extraction/placement of the same cache does not overlap. Recheck after locking to prevent duplicate damage.
- **mutation**: Cache contention is atomically serialized; POSIX locks are not actually synchronized (changed files: src/shiv/cli.py, src/shiv/bootstrap/interpreter.py, src/shiv/bootstrap/filelock.py, src/shiv/bootstrap/__init__.py)
- **setup**: Apply this patch to the clean baseline at ff542cbe75ea, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Patch application, test collection, or infrastructure error

