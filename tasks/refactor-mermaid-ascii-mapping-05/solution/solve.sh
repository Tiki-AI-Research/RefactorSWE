#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=5f00e3d9ac9fc96a19859d502333e35b87d2ffea
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
