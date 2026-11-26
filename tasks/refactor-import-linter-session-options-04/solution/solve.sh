#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
git config user.name "DeepSWE Oracle"
git config user.email "deepswe-oracle@example.invalid"
baseline_ref=31927f1457e3df673912cb5efb0afa6dbc37585f
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
