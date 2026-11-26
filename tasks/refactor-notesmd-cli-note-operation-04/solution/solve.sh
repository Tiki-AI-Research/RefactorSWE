#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
git config user.name "DeepSWE Oracle"
git config user.email "deepswe-oracle@example.invalid"
baseline_ref=58830c82327b8b34f8e5d52e5a3a7cfa0ad0ab5a
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
git add --all
git commit -m "refactor: apply gold solution"
