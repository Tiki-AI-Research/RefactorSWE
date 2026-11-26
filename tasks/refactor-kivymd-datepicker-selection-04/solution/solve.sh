#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=4a2617ea24e13ef2540c37edb95a54ef02e78707
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
