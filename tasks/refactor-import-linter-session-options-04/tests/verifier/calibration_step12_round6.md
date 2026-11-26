# Step 12, round 6: custom contracts exchange session metadata

## Review and reason for contract calibration

Read-only audit found exactly eight candidate-regrade node reports. Every
hard-gate passed. Five candidates and the solution passed all 57 nodes.
6oeGMF6 failed the missing-roots P2P check, HCp842D failed that check and the
typed-owner F2P check, and bQUYSv4 failed only the typed-owner check. No reward
files were accessed.

All binary candidate patches and the solution snapshot patch were applied to
task-local copies of base commit
`31927f1457e3df673912cb5efb0afa6dbc37585f`. The existing 57 selectors reproduced
the snapshot outcomes. Additional exploration ran the original configuration
reading, functional linting and contract unit tests: all 243 tests passed in
the baseline, solution and each of the five full-pass candidates. Inspection
found no further spelling/default/root-reading violation that would justify
rejecting those candidates under the previously explicit read-by-key contract.

A different public behavior is reproducibly distinguishable: custom contracts
can exchange metadata through their session mapping. The baseline and solution
support additions, updates and deletions visible to a subsequent contract.
CrZmdZX instead supplies a read-only mapping, and p8PbsWm gives each contract
a separate dictionary. The earlier instruction permitted different storage
types and required only readable key access, so this round explicitly calibrates
the contract rather than treating those storage choices alone as an old violation.

One abstract bullet was added to `instruction.md`: custom hooks can add, update
and delete entries by key, and those changes are visible to later contracts in
the same lint session. It describes an observable extension capability already
supported by the baseline and solution, without specifying a class, helper,
file, object identity, storage type or implementation procedure.

## Reproducible scenario and minimal verifier change

The existing custom-contract P2P node retains all its root-reading and
construction-hook assertions. It additionally lints a configuration containing
two custom contracts, in declaration order. The first adds a metadata entry,
updates its value, and deletes an existing temporary entry. The second reads
the updated value and verifies the deletion. Both return kept checks. This
uses actual configuration loading, graph construction, custom-type registration,
the public CLI wrapper and its success status.

An independent debug-mode probe produced these concrete failures:

* CrZmdZX: `TypeError: 'SessionOptions' object does not support item assignment`.
* p8PbsWm, 6oeGMF6 and bQUYSv4: `KeyError: 'contract_state'` in the later contract.
* The baseline, solution and remaining four candidates passed the probe.

The installed check uses the ordinary CLI error channel, then asserts its
success status. The failing candidates return 1 instead of 0. These are
assertion failures classified as FAIL by the verifier, not collection errors,
uncaught test errors or inconclusive evidence.

No selector, node count, gate, scoring formula, timeout or existing assertion
was removed or changed. Evaluation-file, patch, config, manifest and runtime
identity digests were synchronized; the instruction digest was also updated.

## Local verification

CPython 3.14.0 used dependencies installed from the frozen lockfile with
`uv sync --frozen --offline --python 3.14 --group dev --group nox`. Each subject
ran all `config['p2p'] + config['f2p']` selectors before and after the change:

```text
python -m pytest -p no:cacheprovider -q --junitxml=<local report> <57 selectors>
```

| Subject | Before P2P | After P2P | F2P before and after |
| --- | --- | --- | --- |
| 6oeGMF6 | 48/49 | 47/49 | 8/8 |
| BLs78AM | 49/49 | 49/49 | 8/8 |
| BxcVN2v | 49/49 | 49/49 | 8/8 |
| CrZmdZX | 49/49 | 48/49 | 8/8 |
| HCp842D | 48/49 | 48/49 | 7/8 |
| bQUYSv4 | 49/49 | 48/49 | 7/8 |
| e3b7n6X | 49/49 | 49/49 | 8/8 |
| p8PbsWm | 49/49 | 48/49 | 8/8 |
| Baseline | 49/49 | 49/49 | 0/8 |
| Solution mSdRjrP | 49/49 | 49/49 | 8/8 |

Every run executed all 57 nodes, without skips or test errors. Both runtime
configuration loaders accepted the updated package. The verifier projected
the actual JUnit reports as PASS for the solution and exactly three candidates
(BLs78AM, BxcVN2v and e3b7n6X), and as FAIL for the other subjects. Under the
unchanged scoring contract, the local solution remains eligible for 1.0 and
exactly three of the eight candidates remain eligible for 1.0. This is local
verification evidence, not a new grading snapshot.

Reverse evaluation-patch checks passed in all ten repositories; forward
application also passed on restored evaluation paths. The fixed `tests/test.sh`
matches its tracked template; `tests/grader.py` remains absent and unchanged.
No Harbor run was performed. Task solution files, jobs, candidates,
candidate-regrade snapshots, solution snapshots and delivery were untouched.
Temporary task-local repositories were removed after validation.
