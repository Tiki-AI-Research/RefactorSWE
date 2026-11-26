#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=d23a70c4912258407161243ed50e06f126d3fca8
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
