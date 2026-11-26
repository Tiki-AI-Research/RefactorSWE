# Step 12, round 3: preserve positional and keyword lint calls

The instruction explicitly preserves the public signature and capabilities of
`application.use_cases.lint_imports(config_filename, limit_to_contracts, cache_dir,
is_debug_mode, show_timings, no_logo, verbose) -> bool`. All seven base parameters
accept both positional and keyword arguments. Restricting their calling convention
would reduce that public capability even if their names and defaults stayed intact.

## Snapshot audit

There are exactly eight candidate-regrade node reports. All seven hard-gate checks
passed for every candidate and the solution: frozen-config, test_patch_sha256,
p2p_select_sha256, p2p-inventory, candidate-root, base-commit and candidate-patch.

All individual nodes in P2P-1 (4), P2P-2 (3), P2P-3 (9), P2P-4 (11), P2P-5 (3),
P2P-6 (7), P2P-7 (3), P2P-8 (3) and P2P-CORE-COMPATIBILITY (6) passed for every
subject. All five F2P-EXTERNAL-AGREEMENT nodes passed. F2P-CORE-OWNERSHIP passed
3/3 except xHQjdQP, which failed only `test_typed_owner_represents_all_four_session_options`
and passed its other two nodes. No patch-application or runner errors occurred.

Decoded candidate production patches retain the lint calling convention. Their
uniformly applied differences in accepted boolean spellings do not justify a
penalty. No new observable violation was found in the seven full-pass candidates.

## Reproduced blind spot and minimal change

In an isolated copy of the solution, insert `*,` immediately after
`def lint_imports(`, making its seven parameters keyword-only. This faulty control
passes all 57 old scoring selectors, including the existing signature test:
that test checks names and defaults but omits parameter kinds. With configuration
initialized, the existing positional call

```python
lint_imports("/does-not-exist.ini", (), None, False, False, True, False)
```

returns `False` in the solution through the normal missing-file error channel;
the faulty control instead raises `TypeError` before entering the function.
This is a mutation experiment, not an observed candidate defect.

The existing `test_lint_imports_public_signature_is_unchanged` now additionally
asserts `inspect.Parameter.POSITIONAL_OR_KEYWORD` for all seven parameters.
This four-line addition strengthens P2P-3. Selectors, counts, gate membership,
weights, execution configuration and existing checks remain unchanged.

## Local validation

All configured selectors ran with CPython 3.14.0 and the project dependencies
installed from its frozen lockfile. Evaluation restoration paths were restored
from the base commit. There were no skipped tests or test execution errors.

| Subject | Updated F2P | Updated P2P |
| --- | --- | --- |
| DSre88z | 8/8 | 49/49 |
| EVKFgKA | 8/8 | 49/49 |
| LF6GZuY | 8/8 | 49/49 |
| WporpR2 | 8/8 | 49/49 |
| iHt8etJ | 8/8 | 49/49 |
| kVdgPDu | 8/8 | 49/49 |
| xHQjdQP | 7/8 | 49/49 |
| zKy679U | 8/8 | 49/49 |
| Solution sQmjarK | 8/8 | 49/49 |
| Baseline | 0/8 | 49/49 |
| Faulty keyword-only control | 8/8 | 48/49 |

The control changed from 57/57 to 56/57, failing only the expanded signature node.
The solution stayed at 57/57. The baseline stayed at 49 P2P passes/eight F2P
failures. Candidate node outcomes remained identical to their snapshots.

Test-patch, evaluation-file, configuration and release-manifest hashes were
synchronized; both verifier and hardgate loaders accepted all 57 selectors.
The updated patch passed forward and reverse application checks in every
isolated repository. No Harbor run or reward-file operation was performed.
Instruction, fixed templates, snapshot directories, delivery and the solution
files were untouched in this round; temporary repositories were removed.

Seven candidates still pass every scoring node. The requested one-to-three target
remains unmet; rejecting otherwise compliant candidates would lack behavioral evidence.
