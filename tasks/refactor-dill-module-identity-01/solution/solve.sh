#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=50d93fe52c84cdbfd81c39f5adba68f627fd330b
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
test "$(git rev-parse HEAD)" = "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
