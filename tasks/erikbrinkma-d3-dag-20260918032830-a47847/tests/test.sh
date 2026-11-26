#!/bin/bash
set -Eeuo pipefail

LOGS=/logs/verifier
REPORTS="$LOGS/reports"
MODEL_PATCH=/logs/artifacts/model.patch
REPO=/workspace/repo
CONFIG=/tests/config.json
CTRF_REPORT="$LOGS/ctrf.json"
HARD_GATE_REPORT="$LOGS/hard-gate.json"
GATE_REWARD="$LOGS/gate-reward.json"
REWARD_DETAILS="$LOGS/reward-details.json"
REWARD="$LOGS/reward.json"

# The runtime image does not guarantee TMPDIR; hidden Go tests use it for their build cache.
export TMPDIR="${TMPDIR:-/tmp}"

mkdir -p "$REPORTS"
rm -f "$CTRF_REPORT" "$REWARD" "$REWARD_DETAILS" "$LOGS/reward.txt" "$LOGS/infrastructure-error.json" \
  "$HARD_GATE_REPORT" "$GATE_REWARD"

infrastructure_failure() {
  status=$?
  trap - ERR
  rm -f "$REWARD" "$REWARD_DETAILS"
  printf '%s\n' -2 > "$LOGS/reward.txt"
  printf '%s\n' '{"reward": -2}' > "$REWARD"
  printf '{"status":"INFRA_ERROR","reward":-2,"exit_code":%s}\n' "$status" > "$LOGS/infrastructure-error.json"
  exit "$status"
}
trap infrastructure_failure ERR

# Create the empty reports consumed by grader.py before its gate phase reads them.
mkdir -p "$LOGS"
: > "$CTRF_REPORT"
: > "$HARD_GATE_REPORT"

# Apply the candidate patch when it is valid.
apply_failed=0
if [ ! -f "$MODEL_PATCH" ]; then
  apply_failed=1
elif [ -s "$MODEL_PATCH" ]; then
  git -C "$REPO" update-index --refresh
  if git -C "$REPO" apply --check --binary "$MODEL_PATCH" >/dev/null 2>&1; then
    git -C "$REPO" apply --index --binary "$MODEL_PATCH" >/dev/null 2>&1
  else
    apply_failed=1
  fi
fi

git -C "$REPO" apply --whitespace=nowarn /tests/verifier/test.patch

python3 /tests/verifier/verifier.py \
  --config "$CONFIG" \
  --repo "$REPO" \
  --ctrf-output "$CTRF_REPORT" \
  --hard-gate-output "$HARD_GATE_REPORT" \
  --apply-failed "$apply_failed"

python3 /tests/grader.py gate \
  --config "$CONFIG" \
  --ctrf "$CTRF_REPORT" \
  --hard-gate "$HARD_GATE_REPORT" \
  --output "$GATE_REWARD" \
  --apply-failed "$apply_failed"

python3 /tests/grader.py finalize \
  --config "$CONFIG" \
  --gate "$GATE_REWARD"

test -f "$CTRF_REPORT"
test -f "$REWARD"
test -f "$REWARD_DETAILS"
test ! -e "$LOGS/reward.txt"
trap - ERR
exit 0
