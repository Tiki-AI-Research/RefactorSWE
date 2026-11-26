# Step 12, round 4: boolean meanings independent of letter case

## Evidence and reason for contract calibration

Read-only review found exactly eight candidate-regrade node reports. All seven
hard-gate checks passed for every candidate and the solution. Each subject ran
57 nodes with no skips or execution errors. Every P2P node passed. Seven
candidates and the solution passed all eight F2P nodes; X4eX3yZ failed only
`test_typed_owner_represents_all_four_session_options`.

The production patches were decoded by applying them to isolated copies of base
commit `31927f1457e3df673912cb5efb0afa6dbc37585f`. Seven candidates use the
exact enabled strings `True` and `true` uniformly. B4q4JoL and the solution
interpret boolean strings without regard to letter case. The original instruction
explicitly allowed uniform differences in accepted spellings. Consequently,
rejecting the seven strict candidates solely through a new verifier assertion
would not have been justified under that contract. Prior rounds improved coverage
but likewise found no observable violation in those seven full-pass candidates.

This round therefore clarifies one abstract behavior in `instruction.md`: changing
only the letter case of a session boolean string preserves its meaning; any
casing of `true` enables and any casing of `false` disables. The shared-consumer
constraint now explicitly refers to that case-insensitive interpretation. This
addresses the background's fragile spelling-dependent options without prescribing
classes, helper names, storage, or implementation steps. Raw configuration payloads,
missing-option defaults, the public API and the timing flag's behavior keep their
existing requirements. This is a stricter task contract, not a previously proven
violation of the old contract.

## Minimal verifier change and reproducible behavior

The existing F2P node
`test_external_consumers_agree_on_the_actual_typed_session` retains both real
consumer calls and every existing graph/contract agreement assertion. Its inputs
now cover `TRUE`, `tRuE`, `FALSE`, and `fAlSe`. One added assertion requires the
boolean sent to graph construction to match that string's case-insensitive meaning.
False cases retain the existing configuration-error checks. No selectors, counts,
gate membership, scoring formulas, timeouts or unrelated checks were changed.

All seven strict candidates reproducibly fail on `TRUE`: both consumers are
reached, but graph construction receives `include_external_packages=False`.
The new assertion reports `assert False is ('true' == 'true')`. Under the revised
contract this is a concrete behavioral failure, rather than an AST or naming
preference. B4q4JoL and the solution pass all four inputs. The existing missing
external import assertions remain in place.

## Local verification

CPython 3.14.0 used the project's frozen dependencies, installed with
`uv sync --frozen --group dev --group nox`. For each isolated repository,
evaluation restoration paths were restored from the base, the evaluation patch
was applied, and all `config['p2p'] + config['f2p']` selectors were run with:

```text
python -m pytest -p no:cacheprovider -q --junitxml=<local report> <all 57 selectors>
```

Both the before and after checks ran every selector. No tests were skipped and
there were no collection, runner, or patch-application errors.

| Subject | Before F2P | After F2P | P2P before and after |
| --- | --- | --- | --- |
| B4q4JoL | 8/8 | 8/8 | 49/49 |
| BL5JqBu | 8/8 | 7/8 | 49/49 |
| BwqioBL | 8/8 | 7/8 | 49/49 |
| JzcXEpr | 8/8 | 7/8 | 49/49 |
| VgoYnGq | 8/8 | 7/8 | 49/49 |
| VzWEbNU | 8/8 | 7/8 | 49/49 |
| X4eX3yZ | 7/8 | 6/8 | 49/49 |
| base | 0/8 | 0/8 | 49/49 |
| nXhd734 | 8/8 | 7/8 | 49/49 |
| oracle | 8/8 | 8/8 | 49/49 |

The solution remains 57/57. Exactly one of the eight candidates passes every
configured node locally. The existing deterministic formula therefore yields a
full score for the solution and only that candidate in a subsequent replay;
this is a local verification result, not a rewritten or rerun scoring snapshot.
An additional solution check verified all 48 capitalization variants of `true`
and `false` across all three typed boolean options, with raw values preserved.

Test-patch and evaluation-file digests, configuration identity, the manifest's
instruction identity and both runtime identity constants were synchronized.
Both verifier and hardgate configuration loaders accepted all 57 selectors.
Forward and reverse test-patch application checks passed for every isolated
repository. The fixed `tests/test.sh` and `tests/grader.py` files match their
tracked versions. The historical manifest's protected-source checksum for
`tests/test.sh` was already stale relative to that unchanged template; this
unrelated metadata entry was left unchanged.

No Harbor run or reward-file operation was performed. Jobs, candidates,
candidates-regrade, solution snapshots, delivery, and task solution files were
untouched. Temporary task-local repositories were removed after validation.
