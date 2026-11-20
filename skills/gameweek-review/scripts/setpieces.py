#!/usr/bin/env python3
"""Set-piece snapshot and diff (doctrine s2 / D5, ruled 20 Nov 2026).

D5 says set-piece changes outrank statistical trends. Until now nothing measured
them: data/baseline_snapshot_20260803.csv has no set-piece columns. This script
snapshots the live *_order fields for every player with a role, and diffs that
against the previous snapshot. Run it every week at gameweek-review step 3.

Usage (Composio sandbox, where the FPL API is reachable):
    python3 setpieces.py --out setpieces_YYYYMMDD.csv --baseline <path or raw URL>
Commit the new snapshot to data/ so next week has a baseline.
"""
import csv, io, json, sys, urllib.request

API = "https://fantasy.premierleague.com/api/bootstrap-static/"
FIELDS = (("pen", "penalties_order"), ("cor", "corners_and_indirect_freekicks_order"),
          ("dfk", "direct_freekicks_order"))
COLS = ["id", "web_name", "club"] + [k for k, _ in FIELDS]


def snapshot(elements, teams):
    rows = []
    for e in elements:
        vals = {k: e.get(f) for k, f in FIELDS}
        if not any(vals.values()):
            continue
        r = {"id": str(e["id"]), "web_name": e["web_name"], "club": teams[e["team"]]}
        r.update({k: str(v) if v else "" for k, v in vals.items()})
        rows.append(r)
    return rows


def diff(old, new):
    o = {r["id"]: r for r in old}
    n = {r["id"]: r for r in new}
    out = []
    for i in sorted(set(o) | set(n), key=lambda x: int(x)):
        a, b = o.get(i, {}), n.get(i, {})
        name = (b or a)["web_name"]
        club = (b or a)["club"]
        moved = a and b and a["club"] != b["club"]
        parts = [f"{k} {a.get(k) or '-'} -> {b.get(k) or '-'}"
                 for k, _ in FIELDS if (a.get(k) or "") != (b.get(k) or "")]
        if moved:
            parts.append(f"club {a['club']} -> {b['club']}")
        if parts:
            out.append(f"{name} ({club}): " + ", ".join(parts))
    return out


def _read(src):
    if src.startswith("http"):
        txt = urllib.request.urlopen(urllib.request.Request(
            src, headers={"User-Agent": "Mozilla/5.0"}), timeout=45).read().decode()
    else:
        txt = open(src, encoding="utf-8").read()
    return list(csv.DictReader(io.StringIO(txt)))


def main(argv):
    out = argv[argv.index("--out") + 1] if "--out" in argv else None
    base = argv[argv.index("--baseline") + 1] if "--baseline" in argv else None
    bs = json.loads(urllib.request.urlopen(urllib.request.Request(
        API, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read())
    rows = snapshot(bs["elements"], {t["id"]: t["short_name"] for t in bs["teams"]})
    if out:
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLS)
            w.writeheader()
            w.writerows(rows)
        print(f"[live] snapshot: {len(rows)} players with a set-piece role -> {out}")
    if base:
        ch = diff(_read(base), rows)
        print("SET-PIECE CHANGES vs baseline:" if ch else "Set pieces: no change vs baseline")
        for c in ch:
            print("  " + c)


if __name__ == "__main__":
    main(sys.argv[1:])
