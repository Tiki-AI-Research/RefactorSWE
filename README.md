# RefactorSWE

RefactorSWE is a benchmark for measuring how well coding agents refactor code while preserving existing behavior. It includes 40 tasks from 35 open-source repositories across Python, Go, TypeScript, and JavaScript.

[Run tasks](#quick-start) · [Directory structure](#directory-structure) · [Leaderboard](#2-leaderboard) · [Task design](#3-task-design) · [Evaluation method](#4-evaluation-method) · [Results by task](#6-results-by-task) · [Error analysis](#7-error-analysis) · [Full report](https://tikiai.co/benchmarks/refactor-swe)

## Quick start

Install Harbor with `uv` on a host with Docker Engine, Docker Compose v2, and access to the task and verifier images listed in each task’s `task.toml`.

```bash
uv tool install --python 3.12 'harbor==0.24.0'
```

1. From the directory containing this README, choose a task. To check the environment with the supplied reference solution, run the Oracle agent.

   ```bash
   TASK_DIR="tasks/meodai-poline-20260917083155-1c6887"
   harbor run -p "$TASK_DIR" -a oracle -e docker -k 1 -n 1 -o jobs
   ```

2. To evaluate a model, set its credentials and replace `<model-id>` with the model ID from your API provider.

   ```bash
   export OPENAI_API_KEY="YOUR_API_KEY"
   export OPENAI_BASE_URL="https://api.openai.com/v1"
   harbor run -p "$TASK_DIR" -a mini-swe-agent -m "openai/<model-id>" -e docker -k 1 -n 1 -o jobs
   ```

3. Open `jobs/<job>/<trial>/result.json` for the run status and `verifier/reward.json` inside the trial for its score. To run all 40 tasks four times each, use `-p tasks -k 4` in the model command.

## Directory structure

```text
benchmark/
├── README.md
├── LICENSE                      # Apache-2.0 for project-authored material
├── PROVENANCE.md                # Upstream repositories and pinned revisions
├── THIRD_PARTY_NOTICES.md       # Third-party materials and patch notices
└── tasks/
    └── <task>/
        ├── instruction.md       # Requirements shown to the agent
        ├── task.toml            # Pinned revision, category, images, and execution settings
        ├── environment/         # Dockerfile for the agent workspace
        ├── solution/            # Reference patch and Oracle entry point
        └── tests/               # Verifier, test configuration, and replay patches

```

## 1. Overview

Each task starts at a pinned commit and specifies which code should own a responsibility, which callers should use it, and which behaviors must hold after the change. The collection includes 20 Python tasks, 14 Go tasks, five TypeScript tasks, and one JavaScript task.

| Item | Count |
| --- | ---: |
| Refactoring tasks | 40 |
| Upstream repositories | 35 |
| Model and harness configurations | 13 |
| Runs per task per configuration | 4 |
| Total runs | 2,080 |
| Fully successful runs | 733 (35.2%) |

## 2. Leaderboard

Each configuration ran 160 times. **pass@1** is the share of runs that earned full reward. **pass@4** is the share of the 40 tasks solved at least once in four attempts. **pass^4** is the share solved in all four attempts. 

| Model · effort | Harness | pass@1 | pass@4 | pass^4 | Avg. steps | Tokens per task (M) | Est. USD per task | Tasks passed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude-opus-5-5 · xhigh | claude-code | 51.9% | 77.5% | 22.5% | 49.7 | 22.79 | 19.02 | 31 / 40 |
| gpt-6.1-sol · xhigh | codex | 45.0% | 60.0% | 30.0% | 35.1 | 7.76 | 2.76 | 24 / 40 |
| hy4 · high | mini-swe-agent | 41.9% | 72.5% | 15.0% | 57.6 | 20.66 | 1.15 | 29 / 40 |
| kimi-k3.1-pro · high | mini-swe-agent | 41.9% | 60.0% | 25.0% | 28.9 | 4.79 | 2.27 | 24 / 40 |
| qwen4-max · xhigh | mini-swe-agent | 41.3% | 65.0% | 20.0% | 69.3 | 24.58 | 3.93 | 26 / 40 |
| muse-wonder · xhigh | mini-swe-agent | 38.1% | 65.0% | 12.5% | 60.3 | 19.64 | 16.91 | 26 / 40 |
| mimo-v2.6-pro · high | mini-swe-agent | 37.5% | 60.0% | 15.0% | 53.5 | 20.18 | 0.71 | 24 / 40 |
| gemini-4-argon · xhigh | mini-swe-agent | 34.4% | 42.5% | 25.0% | 54.2 | 24.30 | 11.83 | 17 / 40 |
| deepseek-v4-1-flash-261017 · xhigh | mini-swe-agent | 33.8% | 72.5% | 7.5% | 64.3 | 20.45 | 0.51 | 29 / 40 |
| MiniMax-M3.1-Flash · xhigh | mini-swe-agent | 30.6% | 52.5% | 10.0% | 83.7 | 34.29 | 0.81 | 21 / 40 |
| glm-5.3 · high | mini-swe-agent | 26.3% | 47.5% | 2.5% | 84.6 | 24.21 | 7.61 | 19 / 40 |
| grok-4.7 · xhigh | mini-swe-agent | 20.6% | 42.5% | 7.5% | 60.8 | 20.78 | 13.15 | 17 / 40 |
| doubao-seed-2-1-pro · high | mini-swe-agent | 15.0% | 30.0% | 5.0% | 82.1 | 18.00 | 4.47 | 12 / 40 |

## 3. Task design

| Refactoring objective | Tasks | Example |
| --- | ---: | --- |
| Extract shared logic | 11 | Several graph layouts validate and cache node dimensions. The task asks them to share this work. |
| Separate responsibilities | 10 | Split SVG rendering and pointer interaction into components coordinated by the public color picker. |
| Reorganize state and data | 8 | Give generator discovery and grouping a single cached catalog. |
| Introduce a common interface or dispatch mechanism | 7 | Give YAML syntax tree nodes a common interface for traversal and visitor dispatch. |
| Manage resource lifecycles | 4 | Coordinate concurrent shutdown calls so they share one cleanup operation. |

The agent receives a repository at a fixed commit and an instruction describing the requested change. The instruction sets the boundaries of the refactor, including existing behavior that callers rely on and any exceptions the task explicitly asks the agent to correct.

Consider what happens when a user drags a color anchor in Poline and the application replaces the palette before the drag ends. The replacement invalidates the gesture. A later pointer event from that drag must leave both palettes untouched and must not emit another change event. The task also requires a distinct component to own pointer interaction. The agent can implement that component as a class, an object, or a closure. Both the ownership decision and its consequences for users are part of the task.

## 4. Evaluation method

The verifier applies the candidate patch and checks the task’s build, evaluation integrity, and regression requirements. **Pass-to-pass (P2P)** checks cover behavior that already works at the base commit and should still work after the change. **Fail-to-pass (F2P)** checks target requirements that fail at the base commit and pass with the reference solution. A candidate earns a leaderboard pass when it clears the task’s required gates and receives a final reward of 1.

For example, one archived Poline attempt passed all 102 regression checks and 21 of the 26 refactor checks. Its recorded reward was 0.8077. Preserving existing behavior earned the attempt a clean regression result, while the five outstanding refactor checks kept it from a full pass.

## 5. Quality assurance

The pinned baseline and reference solution establish the expected test outcomes. P2P checks should pass on both revisions. F2P checks should fail on the baseline and pass with the reference solution. Each task’s `tests/adversarial-patches/` directory contains replay material for checking the verifier against candidate patches.

## 6. Results by task

Each task links to its package. F2P and P2P are the configured check counts. The patch column counts archived adversarial patches. Best model pass@1 is the highest full-pass rate among the 13 configurations for that task. A value of 75% means one configuration passed three of its four attempts and none passed all four.

### Module boundaries and responsibility separation (10 tasks)

| Task | Difficulty | F2P / P2P | Adversarial patches | Best model pass@1 |
| --- | --- | --- | --- | --- |
| [Tree-based traceback rendering](./tasks/cknd-stackprinter-20260915033253-107b0e/) | Very High | 53 / 13 | 35 | 100.0% |
| [Stackprinter formatting pipeline decomposition](./tasks/cknd-stackprinter-20260919134409-f34e9b/) | Very High | 76 / 82 | 70 | 100.0% |
| [Shiv zipapp build and runtime stages](./tasks/linkedin-shiv-20260909075226-5d5ed5/) | Very High | 8 / 100 | 45 | 100.0% |
| [PolinePicker rendering and gesture handling](./tasks/meodai-poline-20260917083155-1c6887/) | Very High | 26 / 102 | 55 | 100.0% |
| [Independent admin HTTP handlers](./tasks/refactor-ehco-server-handlers-04/) | Very High | 13 / 27 | 26 | 75.0% |
| [X11 frame rendering and input handling](./tasks/refactor-fynedesk-frame-interaction-03/) | Very High | 20 / 26 | 32 | 100.0% |
| [Editor-specific syntax tree transformations](./tasks/lute-DOM-TextMark-parse-AST-Protyle-Vditor-01/) | Medium / High | 21 / 2955 | 59 | 0.0% |
| [Graph mapping stages and state ownership](./tasks/refactor-mermaid-ascii-mapping-05/) | Medium / High | 11 / 49 | 21 | 100.0% |
| [Script registration stages](./tasks/refactor-wooey-script-registration-01/) | Very High | 15 / 28 | 22 | 100.0% |
| [Struct tag rule collection](./tasks/refactor-validate-tag-rule-collection-02/) | Very High | 25 / 748 | 11 | 25.0% |

### Shared extraction and deduplication (11 tasks)

| Task | Difficulty | F2P / P2P | Adversarial patches | Best model pass@1 |
| --- | --- | --- | --- | --- |
| [Shared node sizing across graph layouts](./tasks/erikbrinkma-d3-dag-20260918032830-a47847/) | Very High | 202 / 707 | 42 | 100.0% |
| [Common evaluator for label matching rules](./tasks/labeler-match-dimensions-03/) | Medium / High | 17 / 66 | 30 | 100.0% |
| [Shared code generation for dictionary hooks](./tasks/refactor-cattrs-dict-codegen-03/) | Medium / High | 11 / 165 | 22 | 75.0% |
| [Stored connection settings and credential injection](./tasks/refactor-jellyfin-kodi-addon-auth-entrypoint-08/) | Medium / High | 18 / 50 | 38 | 100.0% |
| [Common base for connection dialogs](./tasks/refactor-jellyfin-kodi-dialog-base-07/) | Very High | 15 / 49 | 35 | 75.0% |
| [Shared date picker selection logic](./tasks/refactor-kivymd-datepicker-selection-04/) | Medium / High | 8 / 18 | 31 | 100.0% |
| [Shared provenance proof builder](./tasks/refactor-mangle-provenance-02/) | Medium / High | 15 / 38 | 25 | 100.0% |
| [Unified frontmatter editing operations](./tasks/refactor-notesmd-cli-note-operation-04/) | Medium / High | 12 / 85 | 33 | 100.0% |
| [Shared cache context for Go dependencies](./tasks/setup-go-cache-restore-save-04/) | Medium / High | 18 / 64 | 34 | 100.0% |
| [Git commit ID parsing and formatting](./tasks/spr-git-commit-id-05/) | Medium / High | 25 / 225 | 11 | 100.0% |
| [Shared simulation parameter store](./tasks/ir-sim-env_param-world_param-path_param-02/) | Medium / High | 31 / 1029 | 11 | 100.0% |

### State and data-structure refactoring (8 tasks)

| Task | Difficulty | F2P / P2P | Adversarial patches | Best model pass@1 |
| --- | --- | --- | --- | --- |
| [Formatting options and tracer state ownership](./tasks/cknd-stackprinter-20260914075336-69645d/) | Medium / High | 33 / 98 | 11 | 50.0% |
| [Per-instance Jinja rendering configuration](./tasks/pdoc-jinja-environment-config/) | Medium / High | 27 / 417 | 36 | 75.0% |
| [Lyric group ownership and indexing](./tasks/refactor-applemusic-like-lyrics-dom-02/) | Very High | 56 / 424 | 24 | 0.0% |
| [Cached generator catalog](./tasks/refactor-boxes-generator-registry-06/) | Very High | 20 / 25 | 33 | 100.0% |
| [Serializer dispatch registry](./tasks/refactor-dill-dispatch-registry-03/) | Medium / High | 8 / 36 | 13 | 100.0% |
| [Module identity in session persistence](./tasks/refactor-dill-module-identity-01/) | Very High | 14 / 71 | 44 | 75.0% |
| [Typed session configuration](./tasks/refactor-import-linter-session-options-04/) | Medium / High | 9 / 494 | 27 | 100.0% |
| [Hydration state and deserialization dispatch](./tasks/sveltejs-devalue-20260917060608-25e4d1/) | Very High | 25 / 816 | 41 | 25.0% |

### Lifecycle and Resource Management (4 tasks)

| Task | Difficulty | F2P / P2P | Adversarial patches | Best model pass@1 |
| --- | --- | --- | --- | --- |
| [Rain session shutdown coordination](./tasks/cenkalti-rain-20260918073052-f55ef6/) | Very High | 21 / 240 | 11 | 100.0% |
| [WSGI response preparation and lifecycle](./tasks/pylons-waitress-20260918003129-70962a/) | Medium / High | 35 / 748 | 39 | 100.0% |
| [Resource lifecycle in ImageIO requests](./tasks/refactor-imageio-request-resource-01/) | Medium / High | 24 / 63 | 35 | 100.0% |
| [Steno machine lifecycle management](./tasks/refactor-plover-machine-manager-03/) | Medium / High | 19 / 23 | 34 | 100.0% |

### Strategy Dispatch and Extensibility (7 tasks)

| Task | Difficulty | F2P / P2P | Adversarial patches | Best model pass@1 |
| --- | --- | --- | --- | --- |
| [Shell-specific completion renderers](./tasks/refactor-cleo-completions-shells-05/) | Medium / High | 17 / 14 | 39 | 50.0% |
| [Provider-owned configuration defaults](./tasks/refactor-cloudproxy-provider-dispatch-04/) | Very High | 13 / 32 | 20 | 50.0% |
| [Auxiliary proof-of-work dispatch](./tasks/refactor-go-quai-auxpow-dispatch-02/) | Medium / High | 12 / 25 | 28 | 100.0% |
| [Version-independent transaction metadata access](./tasks/refactor-go-stellar-sdk-tx-meta-views-02/) | Very High | 11 / 38 | 38 | 100.0% |
| [Polymorphic YAML syntax tree traversal](./tasks/refactor-go-yaml-ast-convert-01/) | Very High | 22 / 71 | 29 | 50.0% |
| [Direction-aware graph layout](./tasks/refactor-mermaid-ascii-layout-direction-03/) | Medium / High | 13 / 30 | 34 | 100.0% |
| [Protocol-specific BitComet clients](./tasks/refactor-qbittorrent-client-split-03/) | Very High | 13 / 23 | 33 | 100.0% |

## 7. Error analysis

Of the 2,080 runs, 733 earned full reward and 1,347 fell short. The following examples from the archived evaluation illustrate three ways an apparently complete refactor can still fail.

| Task | Observed failure |
| --- | --- |
| Shiv cache materialization | The runtime received the dependency directory for a later cache selection instead of the directory used during materialization. |
| Boxes generator registry | The implementation reused the catalog object but scanned the modules again on warm queries. Alternating full and module views produced 567 additional scan records. |
| pdoc rendering configuration | Search-template rendering still read settings from shared Jinja globals, allowing one server’s configuration to affect another. |



## 8. References

- The pass@k estimator is described in [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374).
- The repeated-success metric pass^k is described in [τ-bench](https://arxiv.org/abs/2406.12045).

## License

RefactorSWE's original documentation, task instructions, configuration, standalone verifier code, and replay tooling are available under the [Apache License, Version 2.0](./LICENSE), to the extent the project has authority to license them.

Third-party material, including upstream code reproduced or modified in reference, verifier, and replay patches, remains subject to its applicable license terms. See [PROVENANCE.md](./PROVENANCE.md) for pinned upstream revisions and image references and [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md) for patch scope and links to upstream licenses and attribution notices.
