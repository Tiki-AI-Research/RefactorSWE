# Step 12, round 1: external consumer agreement

The instruction requires every consumer to interpret the same raw value uniformly.
It permits accepting or rejecting additional boolean spellings, provided graph
building and forbidden contracts agree. Therefore strict spelling implementations
must not fail merely because they reject mixed-case values.

The eight candidate snapshots contain 49 P2P and eight F2P nodes each. All
hard-gates and P2P nodes passed. The only failed F2P node was
`test_typed_owner_represents_all_four_session_options` in JQbZiPv. All eleven
gate observations passed for the other seven candidates and the solution;
JQbZiPv failed only F2P-CORE-OWNERSHIP. No runner/application failure was reported.

| Subject | Snapshot F2P | Snapshot P2P | Local F2P after change | Local P2P after change |
| --- | --- | --- | --- | --- |
| 9x4kPuc | 8/8 | 49/49 | 8/8 | 49/49 |
| JQbZiPv | 7/8 | 49/49 | 7/8 | 49/49 |
| YBFQuqK | 8/8 | 49/49 | 8/8 | 49/49 |
| aVt8o6t | 8/8 | 49/49 | 8/8 | 49/49 |
| dgTGFow | 8/8 | 49/49 | 8/8 | 49/49 |
| kLApdNJ | 8/8 | 49/49 | 8/8 | 49/49 |
| uNtWivX | 8/8 | 49/49 | 8/8 | 49/49 |
| zu3tMw6 | 8/8 | 49/49 | 8/8 | 49/49 |
| Solution N9RYQqA | 8/8 | 49/49 | 8/8 | 49/49 |

## Reproduced blind spot

An intentionally faulty control was constructed in an isolated copy of the
solution, leaving the forbidden consumer's case-insensitive interpretation intact.
At module scope in `application/use_cases.py`, add:

```python
_GRAPH_ENABLED_SPELLINGS = ("True", "true", "TRUE")
```

Replace the graph consumer's reading of `include_external_packages` with:

```python
include_external_packages = (
    user_options.session_options.get("include_external_packages") in _GRAPH_ENABLED_SPELLINGS
    if "include_external_packages" in user_options.session_options else None
)
```

This control passed all 57 old selectors, including the ownership checks. With
`tRuE`, however, graph building omitted externals while the forbidden consumer
accepted them: the report showed zero dependencies and a KEPT contract. The
expanded node failed with `Forbidden accepted externals omitted by graph building`.
The control is a mutation experiment, not an observed defect in a candidate patch.

## Minimal calibration and validation

The existing `test_external_consumers_agree_on_the_actual_typed_session` now runs
the same real-consumer assertions for `TRUE` and `tRuE`, using separate directories
and monkeypatch contexts. It retains the legal uniformly-disabled outcome. No
selector, scoring weight, gate, or P2P requirement was added or removed. The test
file, patch, configuration and manifest hashes were synchronized; both verifier
and hardgate configuration loaders accepted the updated assets.

Local pytest ran every configured selector against isolated copies of the base,
solution, all eight candidate patches, and the control using CPython 3.14.0 and
the frozen project dependencies. The base remained 49 P2P passes/eight F2P failures;
the solution passed 57/57; the control changed from 57/57 to 56/57. The candidate
outcomes are listed above. The final test patch also passed reverse-application
validation. No Harbor evaluation or reward-file operation was performed.

Seven candidates still pass every scoring node. This round improves observable
contract coverage but does not achieve the requested one-to-three-full-pass target.
Further reductions require evidence of another real contract violation; the
different uniformly-applied spelling policies do not supply that evidence.
