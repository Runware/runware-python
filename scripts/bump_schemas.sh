#!/usr/bin/env bash
# Pin SCHEMAS_VERSION to the current latest schemas release and regenerate
# task_map.py. No argument needed — fetches `/releases/latest/schema-map.json`,
# reads its embedded `version` field, and pins that.
#
# Usage:
#   ./scripts/bump_schemas.sh             # bumps + commits
#   ./scripts/bump_schemas.sh --no-commit # bumps + stages, you commit yourself

set -euo pipefail

COMMIT=1
for arg in "$@"; do
  case "$arg" in
    --no-commit) COMMIT=0 ;;
    *) echo "error: unknown flag '$arg'" >&2; exit 2 ;;
  esac
done

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION_FILE="$ROOT/runware/_schemas_version.py"
SCHEMAS_URL="https://schemas.runware.ai/releases/latest/schema-map.json"

if [ ! -f "$VERSION_FILE" ]; then
  echo "error: $VERSION_FILE not found" >&2
  exit 1
fi

echo "Resolving latest from $SCHEMAS_URL …"
VERSION=$(curl -fsSL "$SCHEMAS_URL" | python3 -c \
  "import sys, json; d = json.load(sys.stdin); v = d.get('version'); sys.exit(1) if not v or v == 'dev' else print(v)" \
  || true)

if [ -z "$VERSION" ]; then
  echo "error: could not read .version from the latest bundle." >&2
  echo "       the schemas service may not yet embed a version field." >&2
  exit 1
fi

CURRENT=$(grep -oE 'SCHEMAS_VERSION = "[^"]*"' "$VERSION_FILE" | sed 's/SCHEMAS_VERSION = "\(.*\)"/\1/')
if [ "$CURRENT" = "$VERSION" ]; then
  echo "Already pinned to $VERSION — nothing to bump."
  exit 0
fi

echo "Bumping $CURRENT → $VERSION"

# Cross-platform sed -i (BSD/macOS vs GNU): write to a tmp file and move.
TMP="$(mktemp)"
sed "s|SCHEMAS_VERSION = .*|SCHEMAS_VERSION = \"$VERSION\"|" \
  "$VERSION_FILE" > "$TMP"
mv "$TMP" "$VERSION_FILE"

cd "$ROOT"
uv run python scripts/generate_types.py

git add runware/_schemas_version.py runware/types/task_map.py

if [ "$COMMIT" -eq 1 ]; then
  git commit -m "chore: bump schemas to $VERSION"
  echo
  echo "Committed: chore: bump schemas to $VERSION"
else
  echo
  echo "Staged (not committed):"
  echo "  runware/_schemas_version.py"
  echo "  runware/types/task_map.py"
  echo
  echo "Next: \`git commit -m 'chore: bump schemas to $VERSION'\`"
fi
