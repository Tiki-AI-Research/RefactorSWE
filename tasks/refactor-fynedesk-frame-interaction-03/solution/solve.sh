#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=7bc2c75eda3aeff73b18450fe32a656bc4af27c4
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
