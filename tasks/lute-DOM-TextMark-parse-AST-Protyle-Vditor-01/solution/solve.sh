#!/usr/bin/env bash
set -euo pipefail

cd /workspace/repo
git config user.name "DeepSWE Oracle"
git config user.email "deepswe-oracle@example.invalid"
git apply --check --binary /solution/solution.patch
git apply --binary /solution/solution.patch
git add --all
git commit -m "refactor: apply gold solution"
