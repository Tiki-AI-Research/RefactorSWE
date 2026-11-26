#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
git config user.name "DeepSWE Oracle"
git config user.email "deepswe-oracle@example.invalid"
baseline_ref=98ce1450c7908643084f7487327dfa4f4bf8a367
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check /solution/solution.patch
git apply /solution/solution.patch
git add --all
git commit -m "refactor: apply gold solution"
