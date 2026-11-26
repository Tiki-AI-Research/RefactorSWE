#!/bin/bash
set -Eeuo pipefail

LOGS=/logs/verifier
REPORTS="$LOGS/reports"
MODEL_PATCH=/logs/artifacts/model.patch
REPO=/workspace/repo

NODE_REPORT="$REPORTS/nodes.json"
HARD_GATE_REPORT="$LOGS/hard-gate.json"
VERIFIER_REPORT="$LOGS/verifier-result.json"
GATE_REWARD="$LOGS/gate-reward.json"

OBJECTIVE_SCRIPT=/tests/graded/objectivity.py
OBJECTIVE_EVIDENCE="$LOGS/objective-evidence.json"

JUDGE_DIR=/tests/graded
JUDGE_PROMPT="$JUDGE_DIR/judge-prompt.md"
JUDGE_OUTPUT="$LOGS/judge"
JUDGE_REWARD="$JUDGE_OUTPUT/reward.json"

CTRF_REPORT="$LOGS/ctrf.json"
REWARD_DETAILS="$LOGS/reward-details.json"
REWARD="$LOGS/reward.json"
AGENT_TIME_OUT="$LOGS/agent-time-out"

mkdir -p "$REPORTS"
rm -f \
  "$CTRF_REPORT" \
  "$REWARD" \
  "$REWARD_DETAILS" \
  "$NODE_REPORT" \
  "$HARD_GATE_REPORT" \
  "$VERIFIER_REPORT" \
  "$GATE_REWARD" \
  "$OBJECTIVE_EVIDENCE" \
  "$AGENT_TIME_OUT" \
  "$LOGS/rewardkit-judge-stdout.txt" \
  "$LOGS/rewardkit-judge-stderr.txt"

rm -rf -- "$JUDGE_OUTPUT"

infrastructure_failure() {
  status=$?
  trap - ERR
  if [ ! -f "$REWARD" ]; then
    printf '%s\n' '{"cheating_detected":false,"f2p_pass_ratio":0.0,"p2p_pass_ratio":0.0,"reward":0.0}' > "$REWARD"
    printf '%s\n' '{"termination_reason":"test_script_failure","errors":["infrastructure_error"],"valid_for_statistics":false,"eligible_for_score":false}' > "$REWARD_DETAILS"
  fi
  exit "$status"
}
trap infrastructure_failure ERR

apply_failed=0
if [ ! -f "$MODEL_PATCH" ]; then
  apply_failed=1
elif [ -s "$MODEL_PATCH" ]; then
  git -C "$REPO" update-index --refresh
  if git -C "$REPO" apply --check --binary "$MODEL_PATCH" \
      > /dev/null 2>&1; then
    git -C "$REPO" apply --index --binary "$MODEL_PATCH" \
      > /dev/null 2>&1
  else
    apply_failed=1
  fi
fi

python3 /tests/verifier/verifier.py \
  --config /tests/config.json \
  --repo "$REPO" \
  --node-report "$NODE_REPORT" \
  --hard-gate-report "$HARD_GATE_REPORT" \
  --verifier-report "$VERIFIER_REPORT" \
  --apply-failed "$apply_failed" \
  > "$LOGS/verifier.json" 2>&1 || true

python3 /tests/grader.py grade \
  --config /tests/config.json \
  --report "$NODE_REPORT" \
  --logs "$LOGS" \
  --apply-failed "$apply_failed" \
  --hard-gate "$HARD_GATE_REPORT" \
  --verifier-result "$VERIFIER_REPORT" \
  --reward-output "$GATE_REWARD" \
  > /dev/null 2>&1

hard_gate_status=$(
  python3 -c '
import json, sys
from pathlib import Path

value = json.loads(Path(sys.argv[1]).read_text()).get("hard_gate_success")
if isinstance(value, bool) or value not in (0, 1):
    raise SystemExit("hard_gate_success must be 0 or 1")
print(value)
' "$GATE_REWARD"
)

f2p_complete=$(
  python3 -c '
import json, sys
from pathlib import Path

value = json.loads(Path(sys.argv[1]).read_text()).get("f2p_pass_ratio")
if isinstance(value, bool) or not isinstance(value, (int, float)):
    raise SystemExit("f2p_pass_ratio must be numeric")
if not 0 <= value <= 1:
    raise SystemExit("f2p_pass_ratio must be in [0, 1]")
print(int(value == 1.0))
' "$GATE_REWARD"
)

reward_mode=$(
  python3 -c '
import json, sys
from pathlib import Path

value = json.loads(Path(sys.argv[1]).read_text()).get("reward_mode", "")
print(value if isinstance(value, str) else "")
' /tests/config.json
)

if [ "$reward_mode" != "VERIFIER_ONLY" ] \
  && [ "$apply_failed" -eq 0 ] \
  && [ "$hard_gate_status" -eq 1 ] \
  && [ "$f2p_complete" -eq 1 ]; then
  /usr/local/bin/python3 "$OBJECTIVE_SCRIPT" \
    --repo "$REPO" \
    --output "$OBJECTIVE_EVIDENCE" \
    > "$LOGS/objectivity.json" 2>&1

  mkdir -p "$JUDGE_OUTPUT"

  # RewardKit launches Codex directly, so it does not inherit Harbor's
  # provider overrides. Codex ignores OPENAI_BASE_URL unless a custom
  # provider is selected explicitly.
  CODEX_HOME="$LOGS/codex-home"
  rm -rf -- "$CODEX_HOME"
  mkdir -p "$CODEX_HOME"
  if [ -n "${OPENAI_BASE_URL:-}" ]; then
    case "$OPENAI_BASE_URL" in
      *'"'*|*'\'*|*$'\n'*|*$'\r'*)
        printf '%s\n' "OPENAI_BASE_URL contains characters unsafe for Codex TOML configuration" \
          > "$LOGS/codex-config-error.txt"
        ;;
      *)
        cat > "$CODEX_HOME/config.toml" <<EOF
model_provider = "rewardkit_proxy"

[model_providers.rewardkit_proxy]
name = "RewardKit proxy"
base_url = "$OPENAI_BASE_URL"
env_key = "OPENAI_API_KEY"
wire_api = "responses"
supports_websockets = false
EOF
        ;;
    esac
  fi

  judge_status=0
  env \
    CODEX_HOME="$CODEX_HOME" \
    OPENAI_API_KEY="${OPENAI_API_KEY:-}" \
    OPENAI_BASE_URL="${OPENAI_BASE_URL:-}" \
    REWARDKIT_JUDGE="${REWARDKIT_JUDGE:-codex}" \
    REWARDKIT_MODEL="${REWARDKIT_MODEL:-gpt-5.5}" \
    MLRUN_OBJECTIVE_EVIDENCE_PATH="$OBJECTIVE_EVIDENCE" \
    timeout --signal=TERM --kill-after=3600s 36000s \
      /usr/local/bin/rewardkit "$JUDGE_DIR" \
        --workspace "$REPO" \
        --output "$JUDGE_REWARD" \
        --max-concurrent-programmatic 1 \
        --max-concurrent-llm 1 \
        --max-concurrent-agent 1 \
        > "$LOGS/rewardkit-judge-stdout.txt" 2>&1 || judge_status=$?
  if [ "$judge_status" -eq 124 ] || [ "$judge_status" -eq 137 ]; then
    : > "$AGENT_TIME_OUT"
  fi
fi

python3 /tests/grader.py finalize \
  --config /tests/config.json \
  --prompt "$JUDGE_PROMPT" \
  --logs "$LOGS" \
  --rewardkit-output "$JUDGE_REWARD" \
  --rewardkit-details "$JUDGE_OUTPUT/reward-details.json" \
  --objective-evidence "$OBJECTIVE_EVIDENCE" \
  --agent-time-out "$AGENT_TIME_OUT" \
  > "$LOGS/finalize.json" 2>&1

trap - ERR
exit 0
