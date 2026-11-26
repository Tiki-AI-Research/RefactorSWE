#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=9f2823a464f4f333affba462198b289766ebb137
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
