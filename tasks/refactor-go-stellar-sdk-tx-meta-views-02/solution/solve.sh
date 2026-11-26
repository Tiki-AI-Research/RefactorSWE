#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=d8c8acf5f56cae47fcf033522349565c6fc86764
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
