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
OBJECTIVE_EVIDENCE="$LOGS/objective-evidence.json"
JUDGE_OUTPUT="$LOGS/judge"
JUDGE_REWARD="$JUDGE_OUTPUT/reward.json"
REWARD_DETAILS="$LOGS/reward-details.json"
REWARD="$LOGS/reward.json"

mkdir -p "$REPORTS"
rm -f "$CTRF_REPORT" "$REWARD" "$REWARD_DETAILS" "$LOGS/reward.txt" \
  "$HARD_GATE_REPORT" "$GATE_REWARD" "$OBJECTIVE_EVIDENCE"
rm -rf -- "$JUDGE_OUTPUT"

infrastructure_failure() {
  status=$?
  trap - ERR
  rm -f "$REWARD" "$REWARD_DETAILS"
  printf '%s\n' -1 > "$LOGS/reward.txt"
  exit "$status"
}
trap infrastructure_failure ERR

# Create the empty reports consumed by grader.py before its gate phase reads them.
mkdir -p "$LOGS"
: > "$CTRF_REPORT"
: > "$HARD_GATE_REPORT"

reward_mode=$(python3 -c '
import json, sys
value = json.load(open(sys.argv[1], encoding="utf-8")).get("reward_mode", "FULL_REWARD")
if value not in {"FULL_REWARD", "VERIFIER_ONLY"}:
    raise SystemExit(f"unsupported reward_mode: {value}")
print(value)
' "$CONFIG")
if [ "$reward_mode" = "VERIFIER_ONLY" ]; then
  unset CODEX_API_KEY OPENAI_API_KEY OPENAI_BASE_URL OPENAI_API_BASE \
    GRADER_API_KEY GRADER_MODEL GRADER_REASONING_EFFORT REWARDKIT_REASONING_EFFORT
fi

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

# Candidate-authored tests are allowed by the original task. Evaluate against
# the frozen regression suite instead of rejecting legitimate test additions.
# The original candidate patch remains unchanged in /logs/artifacts/model.patch.
git -C "$REPO" restore --source=7a07a51a806e70c273a96071c87d19289bc0c69e --worktree -- \
  tests/conftest.py tests/source.py tests/test_formatting.py \
  tests/test_frame_inspection.py tests/test_source_inspection.py tests/test_utils.py

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

eligible_for_judge=$(python3 -c '
import json, sys
value = json.load(open(sys.argv[1], encoding="utf-8")).get("eligible_for_judge")
print(int(value is True))
' "$GATE_REWARD")

if [ "$reward_mode" = "FULL_REWARD" ]; then
  python3 /tests/graded/objectivity.py \
    --repo "$REPO" \
    --output "$OBJECTIVE_EVIDENCE"
  if [ "${DF_HARBOR_CALIBRATION:-0}" != "1" ] && [ "$eligible_for_judge" -eq 1 ]; then
    mkdir -p "$JUDGE_OUTPUT"
    timeout --signal=TERM --kill-after=30s 3600s \
      /usr/local/bin/rewardkit /tests/graded \
        --workspace "$REPO" \
        --output "$JUDGE_REWARD" \
        --max-concurrent-programmatic 1 \
        --max-concurrent-llm 1 \
        --max-concurrent-agent 1
  fi
fi

python3 /tests/grader.py finalize \
  --config "$CONFIG" \
  --gate "$GATE_REWARD" \
  --objective "$OBJECTIVE_EVIDENCE" \
  --judge "$JUDGE_REWARD"

test -f "$CTRF_REPORT"
test -f "$REWARD"
test -f "$REWARD_DETAILS"
test ! -e "$LOGS/reward.txt"
trap - ERR
exit 0
