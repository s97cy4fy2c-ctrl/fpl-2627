#!/usr/bin/env bash
# Session bootstrap. Run FIRST in any new session.
#
#   curl -sfL https://raw.githubusercontent.com/s97cy4fy2c-ctrl/fpl-2627/main/bootstrap.sh -o bs.sh && bash bs.sh
#
# NOTE: the container default shell is dash, so `bash <(curl ...)` does NOT work.
# NOTE: api.github.com is rate limited to 60 req/hr PER IP and the container IP is
#       shared, so that budget is usually already spent. This script therefore uses
#       ONLY raw.githubusercontent.com, which is CDN-served and not rate limited.
#       MANIFEST is committed to the repo and regenerated whenever files change.

set -euo pipefail
RAW="https://raw.githubusercontent.com/s97cy4fy2c-ctrl/fpl-2627/main"
DEST="${1:-/home/claude/fpl}"

mkdir -p "$DEST" && cd "$DEST"
curl -sfL "$RAW/MANIFEST" -o MANIFEST

n=0
while read -r p; do
  [ -z "$p" ] && continue
  mkdir -p "$(dirname "$p")"
  if curl -sfL "$RAW/$p" -o "$p"; then n=$((n+1)); else echo "FAILED: $p"; fi
done < MANIFEST

echo "pulled $n of $(grep -c . MANIFEST) files"
echo
echo "Read docs/ before acting. If MANIFEST is stale, regenerate it - do not hand-edit."
