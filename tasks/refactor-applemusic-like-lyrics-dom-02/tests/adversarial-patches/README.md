# Adversarial patch replay

Task: `refactor-applemusic-like-lyrics-dom-02`  
Base commit: `5c0959686d18ca185b81811added3cd31299569f`

Patches are numbered `P-0001`–`P-0024` in ascending order of their original IDs. Verification points are numbered `VP-0001`–`VP-0048`. The historical old/new ID mapping is not included in this package. Patch contents and SHA-256 hashes are unchanged; renumbering did not rerun the tests.

## Requirements

Use Bash, Python 3.9 or later, and a running Docker daemon. The task container targets `linux/amd64`; each patch runs with 4 CPUs and 8,192 MiB of memory.

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
