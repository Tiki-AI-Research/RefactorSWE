#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=6e24ffe16f389a99de28fae3671cbd25df52d51c
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
