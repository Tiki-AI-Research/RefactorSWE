#!/bin/bash
set -euo pipefail
TARGET_DIR="${1:-/workspace/repo}"
if [ ! -d "$TARGET_DIR" ] && [ -d "/app" ]; then
    TARGET_DIR="/app"
fi
cd "$TARGET_DIR"
PATCH_FILE="${2:-/solution/solution.patch}"
if [ ! -f "$PATCH_FILE" ]; then
    # Fallback to local relative location if running locally
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    if [ -f "$SCRIPT_DIR/solution.patch" ]; then
        PATCH_FILE="$SCRIPT_DIR/solution.patch"
    fi
fi
git apply --whitespace=nowarn "$PATCH_FILE"
git checkout -b feature/solution 2>/dev/null || true

