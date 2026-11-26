#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=00e18eb12ae2f06f3c245f796bfe7f6224db033a
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check /solution/solution.patch
git apply /solution/solution.patch
