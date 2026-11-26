# Running the adversarial patches

Task: `refactor-mermaid-ascii-mapping-05`  
Base commit: `5f00e3d9ac9fc96a19859d502333e35b87d2ffea`

## Requirements

Use Bash, Python 3.9 or later, and a running Docker daemon. Each patch runs in a `linux/amd64` container with 4 CPUs and 8192 MiB of memory.

Unpack the complete task and this package locally. For example, name the package directory `adversarial`.

```text
delivery/
├── task/
│   ├── task.toml
│   └── tests/          # Keep the entire directory, including the Dockerfile, configuration, and verifier.
└── adversarial/
    ├── README.md
    ├── run.sh
    ├── manifest.json
    ├── verification-points.md
    └── patches/
```

The directory names `task/` and `adversarial/` are examples. Pass the task directory as the first argument. The runner reads the patches and index relative to `run.sh` and checks the task and patch hashes before execution. Use the task revision that matches this package.

For patches based on the reference solution, keep `solution/solution.patch` in the task directory. Its hash is recorded in `manifest.runner.reference_patch`. The runner reads the reference patch from the supplied task.

## Run

Run the following commands from the example `delivery/` directory.

Check that the task and patches match.

```bash
bash ./adversarial/run.sh ./task --check-only
```

This check verifies the materials without building an image or running tests. To run all patches:

```bash
bash ./adversarial/run.sh ./task
```

Without `--image`, the runner looks for a matching local image and builds one from `task/tests/Dockerfile` if needed. The first build requires access to the task's base image registry, source repository, and dependency sources. Later runs can reuse the local image.

The task Dockerfile specifies the source repository, pinned commit, dependencies, and container paths. The runner checks the clean baseline at `/workspace/repo` and invokes `/tests/test.sh`. Each candidate runs independently and writes results outside the package.

For an incremental patch based on the reference solution, the runner applies the reference patch and increment in an isolated container, generates the complete candidate diff against the clean baseline, restores the baseline, and invokes the task grader. Replay preserves the supplied patch bytes. Failure to apply either patch produces `APPLY_FAILED` and leaves target coverage unconfirmed.

To reuse a matching local image, pass its name or ID.

```bash
bash ./adversarial/run.sh ./task --image task-verifier:local
```

The specified image must exist and contain the matching baseline. Passing `--image` disables automatic builds. Replace the example image name with your own.

To run a single patch and choose the results directory:

```bash
bash ./adversarial/run.sh ./task --patch P-0001 --out ./results
```

Pass a new directory outside both the task and this package to `--out`. By default, the runner creates `<package>-results-<timestamp>-<random-id>/` beside the package. Absolute paths work from any directory. Quote paths containing spaces. See `bash ./adversarial/run.sh --help` for other options.

## Results

- `summary.json` lists all candidate scores and compares them with the stated expectations.
- `P-xxxx/result.json` records one candidate's result, failed nodes, and verification-point mapping.
- `P-xxxx/console.log` and `P-xxxx/logs/` contain execution output and official grading reports. Some reports may be missing after an incomplete run.
- `build.log` contains the image build output when the run triggered a build.

`ACCEPTED` and `REJECTED` record the task grader's decision. Acceptance of a faulty candidate expected to fail counts as an expectation mismatch. With `target_assertion_confirmed=null`, target assertion coverage has not been independently verified. The grading decision alone does not establish coverage. See [verification-points.md](verification-points.md) for each patch's intended check.

| Exit code | Meaning |
| --- | --- |
| 0 | All selected candidates match their stated grading expectations |
| 1 | At least one expectation mismatch. Inspect the reports for details. |
| 2 | Build, execution, material verification, or incomplete report error |
| 130 | Run interrupted |

For material mismatches, check the task version in the error message. For build failures, inspect `build.log` in the results directory and check access to dependency sources. Use a new output directory for each run.
