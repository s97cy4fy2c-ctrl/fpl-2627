#!/usr/bin/env python3
"""N1 volume trend (doctrine s2, ruled 20 Nov 2026). Decides cause v variance.

Exists because the GW11 draft sold Mbeumo on a 4/3/3 window split that one GW2
match (1.97 xGI) produced (process error n=31). The split was picked after the
numbers were seen. N1 fixes the window and tests for a single-match outlier.

  1. Per-start series, in order. Starts only.
  2. Minutes first. Falling minutes per start -> a ROLE question, not volume.
  3. Fixed window: last 6 starts v all earlier starts.
  4. Fewer than 6 recent or 4 earlier starts -> LOOK (no trend).
  5. Drop the single largest match and recompute. If the change shrinks by
     more than half (or flips sign) -> VARIANCE.
  6. Otherwise -> CAUSE. Both rates are printed.

"Falling minutes" = recent minutes per start more than 10 below earlier.
Materiality: a change smaller than 20% of the earlier rate is no trend (VARIANCE),
whatever the outlier test says. Added 20 Nov 2026 after the first live run read
Barry's -0.06 on 0.86 as CAUSE. Both 10 and 20% are arguable; change them by
ruling, not in passing.

Usage (Composio sandbox, where the FPL API is reachable):
    python3 n1.py Mbeumo McGinn                # xGI per 90
    python3 n1.py Hall Silva --metric defcon   # DefCon points delivered per 90
"""
import json, sys, urllib.request

RECENT, EARLIER, MIN_DROP, MIN_SHIFT = 6, 4, 10, 0.20
API = "https://fantasy.premierleague.com/api/"
DEFCON = {2: 10, 3: 12, 4: 12}  # element_type -> threshold (config.json defcon_2627)


def _rate(s):
    m = sum(x[0] for x in s)
    return sum(x[1] for x in s) / m * 90 if m else 0.0


def n1(starts):
    """starts: list of (minutes, value) for each start, oldest first."""
    rec, ear = starts[-RECENT:], starts[:-RECENT]
    out = {"n_recent": len(rec), "n_earlier": len(ear)}
    if len(rec) < RECENT or len(ear) < EARLIER:
        out["verdict"] = "look"
        return out
    mr = sum(x[0] for x in rec) / len(rec)
    me = sum(x[0] for x in ear) / len(ear)
    out.update(mins_recent=mr, mins_earlier=me,
               rate_recent=_rate(rec), rate_earlier=_rate(ear))
    out["change"] = out["rate_recent"] - out["rate_earlier"]
    k = max(range(len(starts)), key=lambda i: starts[i][1])
    drec = [x for i, x in enumerate(starts) if i != k and i >= len(starts) - RECENT]
    dear = [x for i, x in enumerate(starts) if i != k and i < len(starts) - RECENT]
    out["dropped_index"] = k
    out["change_dropped"] = _rate(drec) - _rate(dear) if dear and drec else 0.0
    small = abs(out["change"]) < max(MIN_SHIFT * out["rate_earlier"], 1e-9)
    if mr < me - MIN_DROP:
        out["verdict"] = "role"
    elif small or (abs(out["change_dropped"]) < abs(out["change"]) / 2
          or out["change_dropped"] * out["change"] < 0):
        out["verdict"] = "variance"
    else:
        out["verdict"] = "cause"
    return out


def _get(p):
    req = urllib.request.Request(API + p, headers={"User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=45).read())


def series(element, history, metric):
    out = []
    for h in history:
        if not h.get("starts"):
            continue
        if metric == "defcon":
            t = DEFCON.get(element["element_type"])
            v = 2 if t and h.get("defensive_contribution", 0) >= t else 0
        else:
            v = float(h["expected_goal_involvements"])
        out.append((h["minutes"], v))
    return out


def main(argv):
    metric = "defcon" if "--metric" in argv and argv[argv.index("--metric") + 1] == "defcon" else "xgi"
    names = [a for a in argv if not a.startswith("--") and a not in ("xgi", "defcon")]
    els = {e["web_name"]: e for e in _get("bootstrap-static/")["elements"]}
    for n in names:
        e = els.get(n)
        if not e:
            print(f"NOT FOUND: {n}")
            continue
        r = n1(series(e, _get(f"element-summary/{e['id']}/")["history"], metric))
        if r["verdict"] == "look":
            print(f"{n}: LOOK - {r['n_recent']} recent / {r['n_earlier']} earlier starts, no trend")
            continue
        print(f"{n} [{metric}/90]: earlier {r['rate_earlier']:.2f} ({r['n_earlier']} starts) -> "
              f"last {RECENT} {r['rate_recent']:.2f}; change {r['change']:+.2f}, "
              f"without largest match {r['change_dropped']:+.2f}; "
              f"mins/start {r['mins_earlier']:.0f} -> {r['mins_recent']:.0f} => {r['verdict'].upper()}")


if __name__ == "__main__":
    main(sys.argv[1:])
