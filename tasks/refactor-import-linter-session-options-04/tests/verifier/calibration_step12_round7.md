# Step 12, round 7: shared mappings passed to public contract constructors

## Snapshot review and reproducible omission

Read-only review found exactly eight candidate-regrade node reports. All seven
hard-gate checks passed for every candidate and the solution. Seven candidates
and solution dEby95G passed all 57 nodes; SkSPr2u failed only the typed-owner
inventory F2P node. No reward files were accessed.

The binary patches were applied to isolated task-local copies of base commit
`31927f1457e3df673912cb5efb0afa6dbc37585f`. Evaluation paths and the four
configured restoration paths were restored before applying the evaluation patch.
Candidate changes to supporting contract fixtures were retained. Running all
configured selectors reproduced the snapshot outcomes.

The round 6 test exercises sharing through the CLI, which supplies the new typed
mapping. It does not exercise integrators constructing custom contracts with an
ordinary dictionary through the public `Contract` constructor. Three full-pass
candidates copy that dictionary independently at each construction. Both the
baseline and solution preserve sharing on this public path.

An independent runtime probe constructed two instances of a custom `Contract`
subclass with the same plain session dictionary. The first check added an entry,
updated it from `pending` to `ready`, and deleted a temporary entry. The second
check asserted that the updated value and deletion were visible. Results:

* 9XJLv82, HMAAdhg and wzGrBsZ: assertion failure; the subscriber still contained
  the original temporary entry and had no published state.
* Baseline, solution dEby95G and the other five candidates: success.

This is a public extension regression under the existing requirements to keep
custom contracts unchanged and preserve session mapping edits between contracts.
The constructor still accepts ordinary dictionaries; requiring callers to create
a new internal type would reduce that capability. The check asserts observable
sharing, without requiring a class name, dictionary subclass or object identity.
No instruction change is necessary.

## Minimal task-side change

The existing custom-contract P2P node retains every earlier assertion, including
the real CLI scenario. Eighteen lines additionally construct a publisher and a
subscriber with one plain dictionary, run the publisher's public check hook,
assert that the subscriber sees the update and deletion, and run its check hook.
The visibility assertion uses `get` before the subscriber hook so missing state
produces an assertion failure rather than an uncaught `KeyError`.

No selector, test count, gate membership, scoring formula or timeout changed.
The evaluation-file, test-patch, config and manifest digests and both runtime
identity constants were synchronized. Both runtime configuration loaders accepted
all 57 selectors. `instruction.md` stayed byte-for-byte unchanged, with SHA-256
`a336b8c3c9472b0e1d814d167ba1e86145da7ab28945955f8319efefc8ec9543`.

## Local verification

CPython 3.14.0 used project dependencies installed from the frozen lockfile with
`uv sync --frozen --offline --python <3.14 interpreter> --group dev --group nox`.
The dependency cache and all temporary repositories were task-local. Each subject
used its own production source through `PYTHONPATH` and ran the complete configured
P2P and F2P selection before and after the change:

```text
python -m pytest -p no:cacheprovider -q --junitxml=<local report> <all 57 selectors>
```

| Subject | Before P2P | After P2P | F2P before and after |
| --- | --- | --- | --- |
| 9XJLv82 | 49/49 | 48/49 | 8/8 |
| HMAAdhg | 49/49 | 48/49 | 8/8 |
| LMbPwfj | 49/49 | 49/49 | 8/8 |
| MnsPNWn | 49/49 | 49/49 | 8/8 |
| S6U7pyP | 49/49 | 49/49 | 8/8 |
| SkSPr2u | 49/49 | 49/49 | 7/8 |
| oQKLuwH | 49/49 | 49/49 | 8/8 |
| wzGrBsZ | 49/49 | 48/49 | 8/8 |
| Baseline | 49/49 | 49/49 | 0/8 |
| Solution dEby95G | 49/49 | 49/49 | 8/8 |

All runs executed 57 tests with no skips, collection errors or execution errors.
The verifier's strict JUnit evidence resolver classified the three new failures
as FAIL, and classified every solution node as PASS. The solution remains
eligible for 1.0 under the unchanged scoring contract. The local full-pass
candidate count drops from seven to four, so the one-to-three distribution target
is still unmet. These are local test results, not a new grading snapshot.

Forward and reverse evaluation-patch checks passed. The fixed `tests/test.sh` and
`tests/grader.py` match their tracked templates. Task solution files, jobs,
candidates, candidate-regrade snapshots, solution snapshots and delivery were
untouched. No Harbor run was performed. Temporary repositories and cache copies
were removed after verification.
