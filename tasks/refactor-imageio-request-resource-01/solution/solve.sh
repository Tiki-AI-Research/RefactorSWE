#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
git config user.name "DeepSWE Oracle"
git config user.email "deepswe-oracle@example.invalid"
baseline_ref=319335265d293c4cf18705dbe11dcc1515702a97
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
git add --all
git commit -m "refactor: apply gold solution"
