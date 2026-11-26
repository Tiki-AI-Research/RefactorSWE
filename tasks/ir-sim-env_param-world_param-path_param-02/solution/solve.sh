#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=7c086d9902694c3c56f0e4259cc01c7fe7af6693
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check /solution/solution.patch
git apply /solution/solution.patch
git add -A -- .
git -c user.name="Oracle Solution" -c user.email="oracle@example.invalid" \
    commit -m "Extract shared parameter storage and resolution"
