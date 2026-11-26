#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=0767a458e50fa1f7ae203b73e50298ab201c80bb
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check /solution/solution.patch
git apply /solution/solution.patch
git add --all
