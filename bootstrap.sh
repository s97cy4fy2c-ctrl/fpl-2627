#!/usr/bin/env bash
# Session bootstrap. Run this FIRST in any new session.
#
# raw.githubusercontent.com and api.github.com are both on the container's
# network allowlist, so this needs no auth, no MCP call and no file upload.
#
#   bash <(curl -sfL https://raw.githubusercontent.com/s97cy4fy2c-ctrl/fpl-2627/main/bootstrap.sh)

set -euo pipefail
REPO="s97cy4fy2c-ctrl/fpl-2627"
RAW="https://raw.githubusercontent.com/${REPO}/main"
API="https://api.github.com/repos/${REPO}"
DEST="${1:-/home/claude/fpl}"

mkdir -p "$DEST" && cd "$DEST"

# Discover every tracked file rather than hardcoding a list, so new files
# are picked up automatically and a rename never silently drops one.
curl -sfL "${API}/git/trees/main?recursive=1" \
  | python3 -c "import json,sys; [print(b['path']) for b in json.load(sys.stdin)['tree'] if b['type']=='blob']" \
  > .manifest

while read -r p; do
  mkdir -p "$(dirname "$p")"
  curl -sfL "${RAW}/${p}" -o "$p"
done < .manifest

echo "pulled $(wc -l < .manifest) files from ${REPO}"
echo
echo "HEAD: $(curl -sfL "${API}/commits/main" | python3 -c "import json,sys; c=json.load(sys.stdin); print(c['sha'][:7], c['commit']['message'].splitlines()[0], '--', c['commit']['author']['date'])")"
echo
echo "Read docs/commitments.md before doing anything. The weekly loop is section 7."
