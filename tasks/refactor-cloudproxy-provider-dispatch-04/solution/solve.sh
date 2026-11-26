#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=06f8a9d8f6f14867125b813a098243794f85d218
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
