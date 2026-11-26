#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=fba3fb4ead8c8e09a06f1d32ae5436e5818eff15
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check /solution/solution.patch
git apply /solution/solution.patch
npm run build
