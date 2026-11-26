# Step 12, round 2: roots available during custom Contract construction

The instruction explicitly requires single-root normalization before contracts are
constructed and requires custom contract types to keep reading roots by key.
`Contract.__init__` invokes the public `validate()` hook. A custom type can therefore
read its session roots there, before `check()` runs.

## Snapshot audit and candidate review

Read-only audit of all eight candidate-regrade snapshots and the solution found:

* All seven hard-gate checks passed: frozen-config, test_patch_sha256,
  p2p_select_sha256, p2p-inventory, candidate-root, base-commit, candidate-patch.
* Every individual node in P2P-1 through P2P-8 and P2P-CORE-COMPATIBILITY passed
  (49 P2P nodes per subject).
* Every node in F2P-EXTERNAL-AGREEMENT passed (five per subject).
* F2P-CORE-OWNERSHIP passed for seven candidates and the solution. XgnChzn failed
  only `test_typed_owner_represents_all_four_session_options`; its other two
  ownership nodes passed. No runner or patch-application error was reported.

Review of the decoded production patches found all candidates normalize roots
before the custom contract receives them. The dict-backed, Mapping-backed and
raw-mapping representations all support the specified key access. The different
uniform boolean spelling policies are permitted by the instruction. Neither an
immutable mapping nor rejection of mixed-case spellings supplies evidence for an
additional deduction.

## Reproduced verifier blind spot

The existing custom-contract P2P node read `root_packages` only during `check()`.
It could not observe normalization performed after construction had completed.
In an isolated copy of the solution, a faulty control changed `_build_report`:

```python
# Immediately before contract_class(...):
construction_options = SessionOptions(user_options.session_options)
construction_options["root_package"] = construction_options.pop("root_packages")[0]

# Pass session_options=construction_options to contract_class(...).

# Immediately after construction, before checking:
construction_options["root_packages"] = user_options.session_options.root_packages
construction_options.pop("root_package")
```

This control passed all 57 existing selectors. It supplies only the singular key
during construction, violating the explicit timing/key-access contract, then
restores the normalized mapping before the old assertion can observe it. This is
a mutation experiment, not a defect observed in a candidate patch.

## Minimal calibration and validation

The existing `SessionOptionsRecordingContract` now reads and records roots in
`validate()`, asserting the roots are a list and the singular key is absent. Its
existing test verifies that this construction hook ran. The original assertions
during `check()` remain. This is a ten-line expansion of the existing P2P-7 node;
selectors, gate membership, scoring weights and counts remain unchanged.

Local pytest executed every configured selector with CPython 3.14.0 and the
project's frozen dependencies. No tests were skipped. The faulty control changed
from 57/57 to 56/57, failing only the enhanced custom-contract test with missing
`root_packages` in the construction hook.

| Subject | Snapshot F2P | Snapshot P2P | Updated F2P | Updated P2P |
| --- | --- | --- | --- | --- |
| 8Gzoasf | 8/8 | 49/49 | 8/8 | 49/49 |
| BSgfWDo | 8/8 | 49/49 | 8/8 | 49/49 |
| EyphEnz | 8/8 | 49/49 | 8/8 | 49/49 |
| RbbXw9b | 8/8 | 49/49 | 8/8 | 49/49 |
| UQWP8qj | 8/8 | 49/49 | 8/8 | 49/49 |
| XgnChzn | 7/8 | 49/49 | 7/8 | 49/49 |
| h6ksktv | 8/8 | 49/49 | 8/8 | 49/49 |
| jt42G2S | 8/8 | 49/49 | 8/8 | 49/49 |
| Solution MBozpw9 | 8/8 | 49/49 | 8/8 | 49/49 |
| Baseline | — | — | 0/8 | 49/49 |

The test patch, evaluation-file hashes, configuration and manifest identities were
synchronized. Both runtime configuration loaders accepted all 57 selectors; the
final test patch passed reverse-application validation. `instruction.md`, the
fixed test/grader templates and all snapshot/delivery directories were untouched.
No Harbor evaluation or reward-file operation was performed.

Seven candidates still pass every node. The one-to-three-full-pass target remains
unmet; the evidence supports improved coverage, not arbitrary candidate rejection.
