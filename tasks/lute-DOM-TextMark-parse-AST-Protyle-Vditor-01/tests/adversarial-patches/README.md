# Adversarial patch replay

Task: `lute-DOM-TextMark-parse-AST-Protyle-Vditor-01`  
Base commit: `8928f1866da3269aed613288afb3554985df94e1`

This package retains 59 patches and 112 verification points selected from the archived run of 2026-10-22. Each selected candidate had a recorded result of `REJECTED` and `reward=0`. Patch and verification-point IDs were renumbered consecutively. The source refers to `renumbering.json` for the old/new IDs and result hashes, but that file was not supplied. Selection and renumbering did not rerun the tests.

The runner was rebound on 2026-10-23 to the supplied task version: 2,953 P2P and 18 F2P checks. The source refers to `task-binding.json` for the binding changes and old/new file hashes, but that file was not supplied either. The 59 historical rejections used an older verifier; replay is required to establish results under the current version. Use `--check-only` to check the supplied materials before replay.

## Requirements

Use Bash, Python 3.9 or later, and a running Docker daemon. The task container targets `linux/amd64`; each patch runs with 2 CPUs and 4,096 MiB of memory.

Keep the full task and this package together. For example:

```text
delivery/
├── task/
│   ├── task.toml
│   └── tests/          # Keep the full directory, including Dockerfile, config, and verifier
└── adversarial/
    ├── README.md
    ├── run.sh
    ├── manifest.json
    ├── verification-points.md
    └── patches/
```

These directory names are examples. Pass the task directory as the first argument. Patches and their index are always read relative to `run.sh`. The runner checks task and patch hashes, so use the task version that matches this package.

For an incremental patch that starts from the reference solution, keep `solution/solution.patch` in the task directory. Its hash is recorded in `manifest.runner.reference_patch`. The runner reads it from the supplied task; it is not copied into this adversarial package.

## Run

From the example `delivery/` directory, check the materials first:

```bash
bash ./adversarial/run.sh ./task --check-only
```

This checks the files without building an image or running tests. To replay all patches:

```bash
bash ./adversarial/run.sh ./task
```

Without `--image`, the runner checks its local image cache and builds from `task/tests/Dockerfile` if needed. The first build requires access to the task's declared image registries, source repository, and dependency sources. Later runs can reuse the image.

Source checkout, pinned commit, dependencies, and container paths follow the task Dockerfile. The runner checks the clean base at `/workspace/repo`, then invokes `/tests/test.sh`. Each patch runs separately, and results are written outside the package.

For a patch on top of the reference solution, the runner applies the reference patch and the original increment inside an isolated container. It collects the complete candidate diff against the clean base, restores that base, and passes the candidate to the task's official grader. The delivered patch bytes remain unchanged. Failure to apply either patch is recorded as `APPLY_FAILED` and does not establish that the target check ran.

To use a matching image already on this machine:

```bash
bash ./adversarial/run.sh ./task --image task-verifier:local
```

The image must exist and contain the matching base. An explicit `--image` disables automatic image building. Replace the example image name with your own.

To run one patch and choose an output directory:

```bash
bash ./adversarial/run.sh ./task --patch P-0001 --out ./results
```

`--out` must name a directory that does not yet exist and is outside both the task and package directories. If omitted, the runner creates `<package>-results-<timestamp>-<random-id>/` beside the package. Absolute paths also work; quote paths containing spaces. Run `bash ./adversarial/run.sh --help` for other options.

## Results

- `summary.json`: scores for all selected candidates and their agreement with the stated expectations.
- `P-xxxx/result.json`: one candidate's result, failed nodes, and verification-point mapping.
- `P-xxxx/console.log` and `P-xxxx/logs/`: execution output and official grading reports. Some reports may be absent if execution did not finish.
- `build.log`: image-build output, when the run triggered a build.

`ACCEPTED` means the task grader accepted the candidate; `REJECTED` means it rejected the candidate. Accepting a faulty candidate that is expected to be rejected counts as an expectation mismatch. `target_assertion_confirmed=null` means assertion coverage has not been independently certified. Acceptance or rejection alone does not prove that the intended assertion was reached. See [verification-points.md](verification-points.md) for each patch's intent.

| Exit code | Meaning |
| --- | --- |
| 0 | Selected candidates match their stated grading expectations |
| 1 | At least one expectation mismatch; inspect the reports |
| 2 | Build, execution, material-check, or incomplete-report error |
| 130 | Interrupted |

For material mismatches, check the task version named in the error. For build failures, inspect `build.log` and access to dependency sources. Use a new output directory for each replay.
