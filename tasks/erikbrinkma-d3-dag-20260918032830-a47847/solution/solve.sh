#!/bin/bash
set -euo pipefail

TARGET_DIR="${1:-/workspace/repo}"
cd "$TARGET_DIR"

REQUIRED_BASE="67d5447722eff38482a5bc5b5eed5f4229d2f80b"

# 1. Verify required base commit exists
if ! git cat-file -e "$REQUIRED_BASE^{commit}" 2>/dev/null; then
  echo "Error: Required base commit $REQUIRED_BASE is unavailable in repository $TARGET_DIR" >&2
  exit 1
fi

# 2. Create genuinely new branch without resetting existing branch
BRANCH_NAME="feature/solution"
if git show-ref --verify --quiet "refs/heads/$BRANCH_NAME"; then
  echo "Error: Branch $BRANCH_NAME already exists; cannot create genuinely new branch without resetting" >&2
  exit 1
fi

if ! git checkout -b "$BRANCH_NAME" "$REQUIRED_BASE"; then
  echo "Error: Failed to create new branch $BRANCH_NAME from base commit $REQUIRED_BASE" >&2
  exit 1
fi

# 3. Locate and apply patch file
PATCH_PATH="${2:-/solution/solution.patch}"
if [[ ! -f "$PATCH_PATH" ]]; then
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  if [[ -f "$SCRIPT_DIR/solution.patch" ]]; then
    PATCH_PATH="$SCRIPT_DIR/solution.patch"
  else
    echo "Error: Solution patch file not found at $PATCH_PATH" >&2
    exit 1
  fi
fi

if ! git apply --whitespace=nowarn "$PATCH_PATH"; then
  echo "Error: Failed to apply solution patch from $PATCH_PATH" >&2
  exit 1
fi

# 4. Stage and commit
if ! git add -A; then
  echo "Error: Failed to stage modified files" >&2
  exit 1
fi

if ! git -c user.name="oracle" -c user.email="oracle@local" commit --no-verify -m "Unify node dimension resolution and validation across layout operators"; then
  echo "Error: Failed to create solution commit" >&2
  exit 1
fi

# 5. Verify parent commit is exactly the required base
PARENT_COMMIT=$(git rev-parse HEAD^)
if [[ "$PARENT_COMMIT" != "$REQUIRED_BASE"* ]]; then
  echo "Error: Resulting commit parent mismatch. Expected parent $REQUIRED_BASE but found $PARENT_COMMIT" >&2
  exit 1
fi

# 6. Verify working tree is clean
TREE_STATUS=$(git status --porcelain)
if [[ -n "$TREE_STATUS" ]]; then
  echo "Error: Working tree is not clean after solution commit:" >&2
  echo "$TREE_STATUS" >&2
  exit 1
fi

RESULT_COMMIT=$(git rev-parse HEAD)
echo "Verified clean working tree and parent commit. Solution commit successfully created: $RESULT_COMMIT on branch $BRANCH_NAME"
