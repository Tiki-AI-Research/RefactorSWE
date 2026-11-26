# Step 12, round 5: configuration errors when root declarations are absent

## Snapshot audit and candidate evidence

Read-only review found exactly eight candidate-regrade node reports. All seven
hard-gate checks passed for every candidate and the solution. Each subject ran
57 nodes, with no skips or execution errors. Six candidates passed all nodes;
E7ixmyX and yQDQKCA failed only the typed-owner inventory node. The solution
passed all 57 nodes. No reward files were accessed.

The binary production patches were applied to task-local copies of base commit
`31927f1457e3df673912cb5efb0afa6dbc37585f`. Review and a runtime probe confirmed
that direct report creation from dictionary-backed user options still works for
every candidate; no deduction or additional check was introduced for that path.

An observable configuration-loading regression was reproduced in E7ixmyX and
the full-pass candidate J8t7aGq. Given either of these existing file formats:

```ini
[importlinter]
include_external_packages = true
```

```toml
[tool.importlinter]
include_external_packages = true
```

the baseline and solution raise `KeyError` from `api.read_configuration` because
neither root declaration is present. Those two candidates instead return a plain
configuration dictionary containing only the external-packages session option.
All six other candidates preserve the error. Both formats were probed separately,
so an early assertion failure in the INI case did not mask the TOML evidence.

This violates the existing requirement to preserve configuration-loading behavior
and error types, including constraint 1. It is an observed candidate regression,
not an artificial mutation or an additional requirement on the internal storage
representation. No instruction change is needed for this check.

## Minimal verifier change

The existing P2P configuration-error node still verifies `FileNotFoundError` for
a nonexistent file. It now also verifies `KeyError` for existing INI and TOML
session sections with both root declarations absent. It does not require the
exception message, an internal parser name, or a particular storage type.

Selectors, node counts, gate membership, scoring formulas, timeouts, and every
existing assertion were preserved. The patch, evaluation-file, configuration and
manifest digests and both runtime identity constants were synchronized. Both
runtime configuration loaders accepted all 57 selectors.

## Local verification

CPython 3.14.0 ran the project's dependencies installed from the frozen lockfile
with `uv sync --frozen --group dev --group nox`. Each subject used an isolated
task-local repository, restored evaluation support files from the base commit,
and applied the evaluation patch. Before and after the change, all configured
P2P and F2P selectors ran with:

```text
python -m pytest -p no:cacheprovider -q --junitxml=<local report> <all 57 selectors>
```

| Subject | Before P2P | After P2P | F2P before and after |
| --- | --- | --- | --- |
| E7ixmyX | 49/49 | 48/49 | 7/8 |
| HgsPCTC | 49/49 | 49/49 | 8/8 |
| J8t7aGq | 49/49 | 48/49 | 8/8 |
| NPwhG8b | 49/49 | 49/49 | 8/8 |
| Q8aerAQ | 49/49 | 49/49 | 8/8 |
| fkj2wQL | 49/49 | 49/49 | 8/8 |
| wAeDy4L | 49/49 | 49/49 | 8/8 |
| yQDQKCA | 49/49 | 49/49 | 7/8 |
| Baseline | 49/49 | 49/49 | 0/8 |
| Solution swprZkU | 49/49 | 49/49 | 8/8 |

There were no skipped tests, collection errors or runner errors. The new failure
in both affected candidates is `DID NOT RAISE KeyError` in the expanded P2P node.
The solution remains 57/57. Full-pass candidates decrease from six to five in
local verification; the one-to-three target remains unmet. This is local behavior
evidence, not a new grading snapshot.

Forward and reverse evaluation-patch checks passed. The fixed `tests/test.sh` and
`tests/grader.py` match their tracked templates. Instruction, task solution files,
jobs, candidates, candidate-regrade snapshots, solution snapshots and delivery
were untouched. No Harbor run was performed. Temporary task-local repositories
were removed after verification.
