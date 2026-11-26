# Adversarial patches and verification points

Task: refactor-qbittorrent-client-split-03
Base commit: 3aec9107cd0ca50741ac4e079fd4f89c8a008968

This package contains 33 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-097856d9b304.patch)
SHA-256: 9f6cca6a398b85e91431bbde20d461d686c98c49d08cf358f70631295461db0a

### VP-0001: Targeted regression: Real Run TestAuditBanPayload

- **requirement**: Real Run TestAuditBanPayload
- **mutation**: Targeted regression: Real Run TestAuditBanPayload (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Real Run TestAuditBanPayload
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0002

[patch](patches/P-0002-828981de8852.patch)
SHA-256: aec06e0ea0c4e8574a1b8b49894150370690d15611f011a14114d857685b93be

### VP-0002: JSON torrent leech number increased by one

- **requirement**: JSON torrent leech number increased by one
- **mutation**: JSON torrent leech number increased by one
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry should generate a complete and valid rejection score; failure in execution, compilation, or collection does not count as success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0003

[patch](patches/P-0003-14e429453d16.patch)
SHA-256: f8d7238d640b9700521609778f25e9d3d57d78c9156b5028f4882e6140046cc3

### VP-0003: Targeted regression: Break an independent method or structure governed by this public contract.

- **requirement**: Break an independent method or structure governed by this public contract.
- **mutation**: Targeted regression: Break an independent method or structure governed by this public contract. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0004

[patch](patches/P-0004-15bdab87db5c.patch)
SHA-256: d8cb32b6cd875c769f511815893689a99d52baff8b2d1a5a85fed8e6344c4c19

### VP-0004: Targeted regression: Real Run TestAuditLegacyPeerFailure

- **requirement**: Real Run TestAuditLegacyPeerFailure
- **mutation**: Targeted regression: Real Run TestAuditLegacyPeerFailure (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Real Run TestAuditLegacyPeerFailure
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0005

[patch](patches/P-0005-55dfccdec650.patch)
SHA-256: e8aa05bd5baf883b2cd0ca9f660a0c438081fbf79bd6b40cce7b588d889f7d23

### VP-0005: Legacy torrent leech placeholder value error corrected to 234

- **requirement**: Legacy torrent leech placeholder value error corrected to 234
- **mutation**: Legacy torrent leech placeholder value error corrected to 234
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry should generate a complete and valid rejection score; failure in execution, compilation, or collection does not count as success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0006

[patch](patches/P-0006-31909a894d83.patch)
SHA-256: ae6a1c876aadbcb509be75b18aeef2fe2cdcc2c9b7dbe4dff9d0d107ec7be869

### VP-0006: Please change the nil response branch of the peer to return a non-nil error.

- **requirement**: Please change the nil response branch of the peer to return a non-nil error.
- **mutation**: Please change the nil response branch of the peer to return a non-nil error. (changed files: client.go, client_BitComet.go, client_integration_test.go, extended_coverage_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The actual request HTTP 204 and check TestAuditJSONPeerNil.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Unreachable nil response branch; Unrelated builds or collection failures

## P-0007

[patch](patches/P-0007-33f46dbe039d.patch)
SHA-256: a1a940af6c07a869614da1c128b5ce1316841801d6ab094f4b847d7494877421

### VP-0007: Targeted regression: Break an independent method or structure governed by this public contract.

- **requirement**: Break an independent method or structure governed by this public contract.
- **mutation**: Targeted regression: Break an independent method or structure governed by this public contract. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

### VP-0008: Targeted regression: Break an independent method or structure governed by this public contract.

- **requirement**: Break an independent method or structure governed by this public contract.
- **mutation**: Targeted regression: Break an independent method or structure governed by this public contract. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0008

[patch](patches/P-0008-475fd8ecff3f.patch)
SHA-256: bf310e162955d70e92593f53f022e6155871a6fec181a2c367fb816e703b5158

### VP-0009: Targeted regression: Break an independent method or structure governed by this public contract.

- **requirement**: Break an independent method or structure governed by this public contract.
- **mutation**: Targeted regression: Break an independent method or structure governed by this public contract. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0009

[patch](patches/P-0009-499112a77db5.patch)
SHA-256: 928f9a1e8184d39119457e87ade7d123358f1dfddd174fa90db9d2c73c37e163

### VP-0010: Targeted regression: Real Run TestAuditOwnProtocols

- **requirement**: Real Run TestAuditOwnProtocols
- **mutation**: Targeted regression: Real Run TestAuditOwnProtocols (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Real Run TestAuditOwnProtocols
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0010

[patch](patches/P-0010-d90ca6a5dd8b.patch)
SHA-256: 341310ff3ab82a3ad88228a72a3753863c542c86ac5d33227fe69cd9b54da4dd

### VP-0011: JSON torrent size increased by one byte

- **requirement**: JSON torrent size increased by one byte
- **mutation**: JSON torrent size increased by one byte
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The official entry should generate a complete and valid rejection score; failure in execution, compilation, or collection does not count as success.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0011

[patch](patches/P-0011-547b11375244.patch)
SHA-256: 62d2de78049a2af341bf4e6f95e93d19c643c24d29b5fdfc62faed09848be07c

### VP-0012: Targeted regression: Run TestAuditJSONTorrentError

- **requirement**: Run TestAuditJSONTorrentError
- **mutation**: Targeted regression: Run TestAuditJSONTorrentError (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Run TestAuditJSONTorrentError
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0012

[patch](patches/P-0012-68e34445ed65.patch)
SHA-256: fad5361db819346c630ff79af99ed2df3cbb66a9b6f132280868cb6c26bcd864

### VP-0013: Targeted regression: Realize TestAuditJSONProbe

- **requirement**: Realize TestAuditJSONProbe
- **mutation**: Targeted regression: Realize TestAuditJSONProbe (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Realize TestAuditJSONProbe
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0013

[patch](patches/P-0013-6e5b69787c80.patch)
SHA-256: d96c8253da296233a493d50d964d4eb3a3d7138db6b42cbc31a8880e7fa036c1

### VP-0014: Targeted regression: Break an independent method or structure governed by this public contract.

- **requirement**: Break an independent method or structure governed by this public contract.
- **mutation**: Targeted regression: Break an independent method or structure governed by this public contract. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0014

[patch](patches/P-0014-71647babac26.patch)
SHA-256: 2dacea285442873818beb5ee6761d6b9d65c87417b61894c59b7240ac8d221b1

### VP-0015: Targeted regression: True Run TestAuditBanResult

- **requirement**: True Run TestAuditBanResult
- **mutation**: Targeted regression: True Run TestAuditBanResult (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: True Run TestAuditBanResult
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0015

[patch](patches/P-0015-76e92d5bd764.patch)
SHA-256: 74b97eb05d1efb58729202790a1837ab3389b65c425f943484a4445c2e6f0e4e

### VP-0016: Targeted regression: Real Run TestAuditJSONPeerError

- **requirement**: Real Run TestAuditJSONPeerError
- **mutation**: Targeted regression: Real Run TestAuditJSONPeerError (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Real Run TestAuditJSONPeerError
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0016

[patch](patches/P-0016-7ddd93e7bfd0.patch)
SHA-256: aa7aff85de4570542aa6a6ab7dc7770eae997e1848319702a4415841a3e2b1fc

### VP-0017: Targeted regression: Actual TestAuditNoMatch Execution

- **requirement**: Actual TestAuditNoMatch Execution
- **mutation**: Targeted regression: Actual TestAuditNoMatch Execution (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Actual TestAuditNoMatch Execution
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0017

[patch](patches/P-0017-7f614eefa6dd.patch)
SHA-256: 5707c9c2edf9ca507af1dc52126a1399d506db613c3c838f9fede1eca9c6c849

### VP-0018: Targeted regression: Real Run TestAuditLegacyTorrentFailure

- **requirement**: Real Run TestAuditLegacyTorrentFailure
- **mutation**: Targeted regression: Real Run TestAuditLegacyTorrentFailure (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Real Run TestAuditLegacyTorrentFailure
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0018

[patch](patches/P-0018-81f1386d804a.patch)
SHA-256: 333b91e4386b89643cad3b5a099899c8b42d9c16111ff1a6494c874bb77f7e2e

### VP-0019: Targeted regression: Break an independent method or structure governed by this public contract.

- **requirement**: Break an independent method or structure governed by this public contract.
- **mutation**: Targeted regression: Break an independent method or structure governed by this public contract. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

### VP-0020: Targeted regression: Break an independent method or structure governed by this public contract.

- **requirement**: Break an independent method or structure governed by this public contract.
- **mutation**: Targeted regression: Break an independent method or structure governed by this public contract. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0019

[patch](patches/P-0019-86456a104ed4.patch)
SHA-256: aafb3f111a95b3b33b8243af46458599058be67921b6e3997077bee43ff29562

### VP-0021: Targeted regression: Break an independent method or structure governed by this public contract.

- **requirement**: Break an independent method or structure governed by this public contract.
- **mutation**: Targeted regression: Break an independent method or structure governed by this public contract. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

### VP-0022: Targeted regression: Break an independent method or structure governed by this public contract.

- **requirement**: Break an independent method or structure governed by this public contract.
- **mutation**: Targeted regression: Break an independent method or structure governed by this public contract. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0020

[patch](patches/P-0020-8a52e967ac08.patch)
SHA-256: a021e7cb66c49cfef21caa9f18e5397cc6e014a681d9e9b92e6368236abf87f4

### VP-0023: Targeted regression: Real Run TestAuditModels

- **requirement**: Real Run TestAuditModels
- **mutation**: Targeted regression: Real Run TestAuditModels (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Real Run TestAuditModels
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0021

[patch](patches/P-0021-a3e0bbdb471a.patch)
SHA-256: 8fb97c3099461e9472954c3f1bfa0c11a0883a35610520d9240b876cb72343ec

### VP-0024: Targeted regression: Realize TestAuditLegacyProbe

- **requirement**: Realize TestAuditLegacyProbe
- **mutation**: Targeted regression: Realize TestAuditLegacyProbe (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Realize TestAuditLegacyProbe
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0022

[patch](patches/P-0022-b060dae062b7.patch)
SHA-256: b1ef5631c4a5af582f1e3dac85ca5349d61621326c63c029ad1dfc2e88ed3219

### VP-0025: Targeted regression: Break an independent method or structure governed by this public contract.

- **requirement**: Break an independent method or structure governed by this public contract.
- **mutation**: Targeted regression: Break an independent method or structure governed by this public contract. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0024

[patch](patches/P-0024-b79ac48d1354.patch)
SHA-256: a9237d51f16bd912b92d3e1d34cec779ca3de887c0c3cabafd782fa3e05f1a3d

### VP-0027: Targeted regression: Real Run TestAuditJSONTorrents

- **requirement**: Real Run TestAuditJSONTorrents
- **mutation**: Targeted regression: Real Run TestAuditJSONTorrents (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Real Run TestAuditJSONTorrents
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0025

[patch](patches/P-0025-c1adc166f536.patch)
SHA-256: 9b26edd1a72f2f32e7abe9cbad3425b9f3188664da4a471608305608d1b26bfe

### VP-0028: Targeted regression: True run TestAuditForcedInstance

- **requirement**: True run TestAuditForcedInstance
- **mutation**: Targeted regression: True run TestAuditForcedInstance (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: True run TestAuditForcedInstance
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0026

[patch](patches/P-0026-cf069fe5ffd8.patch)
SHA-256: aa930e1e7b9a59187691d05f5d6f0a0b62a7def7e2d10490ee31d31f995a6922

### VP-0029: Targeted regression: Real Run TestAuditLegacyTorrents

- **requirement**: Real Run TestAuditLegacyTorrents
- **mutation**: Targeted regression: Real Run TestAuditLegacyTorrents (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Real Run TestAuditLegacyTorrents
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0027

[patch](patches/P-0027-db903e1de2b2.patch)
SHA-256: a6fdc4073a65014dbe2581679077629a88e0521abbf564ee416ffdd0261b5cd3

### VP-0030: Targeted regression: Realize TestAuditJSONPeers

- **requirement**: Realize TestAuditJSONPeers
- **mutation**: Targeted regression: Realize TestAuditJSONPeers (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Realize TestAuditJSONPeers
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0028

[patch](patches/P-0028-e1a6c084959f.patch)
SHA-256: 18c6578e9e6fb2e564ee672ce9fad07dc8c36bffa305d20803e87c383603dc74

### VP-0031: Please change the nil response branch in the list to return a non-nil error.

- **requirement**: Please change the nil response branch in the list to return a non-nil error.
- **mutation**: Please change the nil response branch in the list to return a non-nil error. (changed files: client.go, client_BitComet.go, client_integration_test.go, extended_coverage_test.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: The actual request HTTP 204 and check TestAuditJSONTorrentNil.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Unreachable nil response branch; Unrelated builds or collection failures

## P-0029

[patch](patches/P-0029-e2872c2f4f1e.patch)
SHA-256: 7170586371c5d5e60e0d8eaf0afded3d968a903332ecdc6b5fdabe584d2b9700

### VP-0032: Change the result of parsing bad% from a negative sentinel to 0.

- **requirement**: Malformed percentage inputs must return a negative value.
- **mutation**: Change the result of parsing bad% from a negative sentinel to 0. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Build or collection failed; The erroneous branch did not reach the end.

## P-0030

[patch](patches/P-0030-ea06801d17c9.patch)
SHA-256: eb75e30e1aaf8588738fee896ede3d560f93d14fd052d190da1e1780a32bfdc2

### VP-0033: Targeted regression: Realize TestAuditJSONLogin

- **requirement**: Realize TestAuditJSONLogin
- **mutation**: Targeted regression: Realize TestAuditJSONLogin (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Realize TestAuditJSONLogin
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

### VP-0034: Targeted regression: Real Run TestAuditLegacyLogin

- **requirement**: Real Run TestAuditLegacyLogin
- **mutation**: Targeted regression: Real Run TestAuditLegacyLogin (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Real Run TestAuditLegacyLogin
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

## P-0031

[patch](patches/P-0031-ea8b94113286.patch)
SHA-256: 47581bcec710aec6ab576d4673260e3efea2ef5bb99055763491d32c29511fbc

### VP-0035: Targeted regression: Error sentinel becomes 0

- **requirement**: Error sentinel becomes 0
- **mutation**: Targeted regression: Error sentinel becomes 0 (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0032

[patch](patches/P-0032-ee76156f7bd2.patch)
SHA-256: 8d04fd6d8fd0dab60a3affae3d2f33a41d2da6b58c38140f529bd8c685877efc

### VP-0036: Targeted regression: Error sentinel becomes 0

- **requirement**: Error sentinel becomes 0
- **mutation**: Targeted regression: Error sentinel becomes 0 (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0033

[patch](patches/P-0033-ef4de09ad3f3.patch)
SHA-256: c11665636c3e398cf1a681375b23827dcf1756be375cc21a96229a70170c9d72

### VP-0037: Targeted regression: Break an independent method or structure governed by this public contract.

- **requirement**: Break an independent method or structure governed by this public contract.
- **mutation**: Targeted regression: Break an independent method or structure governed by this public contract. (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Target value not reached; Build or collection failed

## P-0034

[patch](patches/P-0034-f4317da80899.patch)
SHA-256: cfdc4afa4332acb42b2a8d2c65d354f94794393ad5665d5fc83a69078f44b733

### VP-0038: Targeted regression: Realize TestAuditLegacyPeers

- **requirement**: Realize TestAuditLegacyPeers
- **mutation**: Targeted regression: Realize TestAuditLegacyPeers (changed files: client.go, client_BitComet.go, client_BitComet_Legacy.go, client_BitComet_V2.go, among others)
- **setup**: Apply this patch to the clean baseline at 3aec9107cd0c, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect. Focus: Realize TestAuditLegacyPeers
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. The patch does not apply; Irrelevant build or collection errors

