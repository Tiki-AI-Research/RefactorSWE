# Share provenance proof construction

Post-hoc explanation and recorded-event replay duplicate proof-graph scaffolding. Give option defaults, ground validation, per-goal memoization, in-progress cycle tracking, rule-id memoization, depth handling, node construction, and content-addressed ids one shared construction component. The two entry points should supply only premise resolution: fact-store queries/closed-world checks for post-hoc mode, recorded derivation/transform events for replay. Private helpers, memo keys, and organization are yours to choose.

Keep `Explain(program, store, goal, opts)` and `BuildFromRecording(rec, store, goal, opts)` signatures and proof-list/error results. Explain retains EDB fact leaves, IDB-derived proofs, and negated-premise absence leaves, without transform nodes. Recording retains rule, let-row, and aggregate node shapes. Both reject non-ground goals with `ErrGoalNotGround` before premise resolution, return `ErrNoProof` under today's no-proof conditions, and never return partial proofs together with an error.

Public `Options.MaxProofs` defaults to 1 when zero and MaxDepth to 64 when zero, retaining their meanings/caps. Return at most MaxProofs alternatives, marking affected subproofs Partial when depth-limited rather than failing. An already-in-progress goal contributes no proof on that branch, preserving termination. Memoization stays within each call; repeated proofs of a goal within it remain identical.

Preserve every ProofNode exported field and Kind, including ID, Fact, Rule/RuleID, Bindings, Premises, GroupKey, TransformText, and Partial. Ids remain deterministic and content-addressed: equal inputs yield equal ids, and shared subderivations collapse to the same id within/across modes. Sharing rule-id memoization must not change either rule or node ids. Premise order, bindings, Partial marking, node kinds, and errors remain identical.

`EmitFacts` and `Print` keep signatures, fact schema, and tree output, including shared-subproof references and absence leaves emitting no proves fact. MemoryRecorder, engine integration, and CLI mode selection retain their APIs and tree/fact formats.

Completion requires one shared skeleton with mode-specific premise resolution, with tests for both entry points supporting unchanged identity, limits, cycles, transforms, outputs, and errors. Do not weaken or strengthen observable behavior. Add no dependencies, module/toolchain/build requirements, or public API changes. Limit edits to necessary provenance production code, tests, and direct supporting adjustments, avoiding unrelated refactors, renames, and formatting.

Work in a new branch from frozen base commit `8edad8d350b99dc08063981663f4b4a159a6b7ec` and commit the completed changes. This commit is the behavior-preservation baseline, even if `main` points elsewhere.
