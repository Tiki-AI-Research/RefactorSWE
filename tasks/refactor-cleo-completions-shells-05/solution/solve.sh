#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
baseline_ref=8c3f1bbf82d918fc137ad40db65c446e14564aac
git rev-parse --verify "$baseline_ref^{commit}" >/dev/null
git switch -C oracle-solution "$baseline_ref"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
