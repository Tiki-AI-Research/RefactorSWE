#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
git config user.name "DeepSWE Oracle"
git config user.email "deepswe-oracle@example.invalid"
baseline_ref=5c0959686d18ca185b81811added3cd31299569f
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --binary --check /solution/solution.patch
git apply --binary /solution/solution.patch
git add --all
git commit -m "refactor: apply gold solution"
