#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=7fe290e7fc72c5ef548949608272e7613c7800c2
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
