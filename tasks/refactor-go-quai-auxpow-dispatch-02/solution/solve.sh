#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=208b67554a9078086c8de7c9ab0a9b5af2d9d567
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
