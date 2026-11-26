#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
git config user.name "DeepSWE Oracle"
git config user.email "deepswe-oracle@example.invalid"
baseline_ref="${ENVPIPE_BASE_COMMIT:-HEAD}"
git rev-parse --verify "${baseline_ref}^{commit}" >/dev/null 2>&1
git switch -C oracle-solution "$baseline_ref"
git apply --check /solution/solution.patch
git apply /solution/solution.patch
git add --all
git commit -m "refactor: apply gold solution"
