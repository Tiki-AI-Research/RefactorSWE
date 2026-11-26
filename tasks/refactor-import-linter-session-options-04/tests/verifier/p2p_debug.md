# P2P debugging notes

The task instruction in `instruction.md` retained its SHA-256 digest of
`a336b8c3c9472b0e1d814d167ba1e86145da7ab28945955f8319efefc8ec9543`.
The reference solution, evaluation test.patch, scoring formula, and timeouts were unchanged.

The original P2P suite included eight upstream unit tests. Pytest collection at
`31927f1457e3df673912cb5efb0afa6dbc37585f` identified 453 upstream unit tests
in 18 files. All were included, with the original eight counted only once.
P2P increased from 49 to 494, and F2P stayed at 8, for a total of 502 exact selectors.

The update covered the command, gate ownership, execution profile, p2p_select,
task.toml counts, and configuration, manifest, and runtime hashes.
The 34 restoration paths cover the upstream tests and support files. Replay restores
their baseline contents, including the original assertions, before evaluating candidates.

Seventy-five upstream case IDs contain escaped newlines or wildcard characters.
These are accepted as literal values only within parameter IDs. Paths and function
or class names still reject wildcards. Actual newlines are rejected. Commands use
argv without shell expansion.

Independent tests, projection of actual JUnit results, and full verifier replay
agreed under CPython 3.14.7 with dependencies installed from the frozen uv.lock.

| Input | P2P | F2P | Score |
| --- | --- | --- | --- |
| Baseline | 494/494 | 0/8 | 0.0 |
| Reference solution | 494/494 | 8/8 | 1.0 |
| Upstream unit test regression | 490/494 | 8/8 | 0.0 |

The negative control broke ValueObject.__repr__ in a temporary patch and attempted
to replace the corresponding upstream test with assert True. After restoration,
four upstream tests still reported ASSERTION_FAILURE, and grading stopped with
p2p_failed. All three full replays passed the Hard Gate with no skipped or missing
tests or infrastructure errors.

Another 26 verifier regression checks passed. They covered configuration consistency,
parameter IDs, invalid selectors, JUnit classification for every node, and scoring
after an upstream unit test failure. Run from the task directory:

```sh
python -m pytest -p no:cacheprovider -q tests/verifier/test_p2p_inventory.py
```

To reproduce the full replay, use a clean baseline repository with an empty patch or the reference patch:

```sh
python tests/verifier/verifier.py --config tests/config.json \
  --repo /path/to/base-repo --candidate-patch /path/to/model.patch \
  --logs /path/to/debug-logs
```

The temporary repository and original replay logs were retained at `/tmp/import-linter-p2p.I8y9eE`.
This debugging run did not launch new Harbor candidate evaluations or modify existing jobs or mutation patches.
