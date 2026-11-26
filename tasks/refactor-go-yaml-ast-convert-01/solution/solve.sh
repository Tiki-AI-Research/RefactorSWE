#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=edee2f91616c6d73112a13e7c0dbde72ce938877
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
