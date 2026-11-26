#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=3aec9107cd0ca50741ac4e079fd4f89c8a008968
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
