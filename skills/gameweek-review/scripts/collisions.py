#!/usr/bin/env python3
"""Own-club head-to-head exposure. Exits non-zero on 2+ class-A pairs in the XI.

Ruled 7 Sep 2026. Companion to check_squad.py, kept separate because it needs
the fixtures endpoint and answers a different question: not "is this squad
legal" but "is this squad betting against itself this week".

We hold 9 of 20 clubs across 15 players, so collisions occur in EVERY gameweek
from GW4 to GW10. A rule that banned them would fire constantly and be ignored,
which is how the transferability thesis died. So grade, never ban.

  Class A  two clean-sheet assets on opposite sides. Mutually exclusive - only
           one clean sheet can exist. Strict expected-points loss.
  Class B  our attacker against our own clean-sheet asset. An internal hedge:
           the attacker returning is exactly what kills the clean sheet.
           Marked B! when the attacking club scores above the league median AND
           the defending club concedes above it. Both rates printed; nothing
           projected (doctrine: no projection model).
  Class C  attacker against attacker. Benign, and better in a high-scoring
           game because both can return. Two strikers opposed is not a problem.
           Not reported.

DefCon accrues regardless of scoreline, so it never creates a collision.

Usage:  python3 collisions.py squad.json            # upcoming gw from squad.json
        python3 collisions.py squad.json --to 10    # horizon scan through GW10
"""
import json, sys, urllib.request

API = "https://fantasy.premierleague.com/api/bootstrap-static/"
FIX = "https://fantasy.premierleague.com/api/fixtures/"
TEAMS = {1: "ARS", 2: "AVL", 3: "BOU", 4: "BRE", 5: "BHA", 6: "CHE", 7: "COV", 8: "CRY",
         9: "EVE", 10: "FUL", 11: "HUL", 12: "IPS", 13: "LEE", 14: "LIV", 15: "MCI",
         16: "MUN", 17: "NEW", 18: "NFO", 19: "TOT", 20: "SUN"}
POS = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD"}
SRC = {"GKP": "CS", "DEF": "CS", "MID": "ATT", "FWD": "ATT"}


def get(u):
    return json.loads(urllib.request.urlopen(
        urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=45).read())


def rates(fixtures):
    gf, ga, pl = {}, {}, {}
    for f in fixtures:
        if f.get("finished") and f.get("team_h_score") is not None:
            for x, s1, s2 in ((f["team_h"], f["team_h_score"], f["team_a_score"]),
                              (f["team_a"], f["team_a_score"], f["team_h_score"])):
                gf[x] = gf.get(x, 0) + s1
                ga[x] = ga.get(x, 0) + s2
                pl[x] = pl.get(x, 0) + 1
    return gf, ga, pl


def collisions(rows, gw, fixtures):
    gf, ga, pl = rates(fixtures)
    per = lambda d, t: (d.get(t, 0) / pl[t]) if pl.get(t) else 0.0
    gfs = sorted(per(gf, k) for k in pl)
    gas = sorted(per(ga, k) for k in pl)
    mgf = gfs[len(gfs) // 2] if gfs else 0
    mga = gas[len(gas) // 2] if gas else 0

    by_club = {}
    for r in rows:
        by_club.setdefault(r["club"], []).append(r)

    out, seen = [], set()
    for f in fixtures:
        if f.get("event") != gw:
            continue
        h, a = TEAMS[f["team_h"]], TEAMS[f["team_a"]]
        if h not in by_club or a not in by_club:
            continue
        for side, opp, sid, oid in ((h, a, f["team_h"], f["team_a"]),
                                    (a, h, f["team_a"], f["team_h"])):
            for p in by_club[side]:
                for q in by_club[opp]:
                    ps, qs = SRC[p["pos"]], SRC[q["pos"]]
                    if ps == "CS" and qs == "CS":
                        cls = "A"
                    elif ps == "ATT" and qs == "CS":
                        cls = "B!" if (per(gf, sid) > mgf and per(ga, oid) > mga) else "B"
                    else:
                        continue
                    key = tuple(sorted([p["name"], q["name"]])) + (cls[0],)
                    if key in seen:
                        continue
                    seen.add(key)
                    out.append({"cls": cls, "gw": gw, "fx": h + " v " + a,
                                "a": p["name"], "ac": side, "b": q["name"], "bc": opp,
                                "xi": p["xi"] and q["xi"],
                                "gf": per(gf, sid), "ga": per(ga, oid)})
    return out


def line(c):
    where = "XI" if c["xi"] else "bench"
    if c["cls"] == "A":
        return (f"  A  GW{c['gw']} ({where}) {c['fx']}: {c['a']}({c['ac']}) and "
                f"{c['b']}({c['bc']}) both need the same clean sheet - only one can pay")
    return (f"  {c['cls']:<2} GW{c['gw']} ({where}) {c['fx']}: {c['a']}({c['ac']}) returning "
            f"kills {c['b']}({c['bc']})'s clean sheet "
            f"[{c['ac']} {c['gf']:.1f} GF/g v {c['bc']} {c['ga']:.1f} GA/g]")


def main(path, to=None):
    sq = json.load(open(path))
    gw = sq.get("gw", 1)
    by_name = {}
    for e in get(API)["elements"]:
        by_name.setdefault(e["web_name"], e)
    rows = []
    for n in sq["xi"] + sq["bench"]:
        e = by_name.get(n)
        if not e:
            print("NOT FOUND: " + n)
            sys.exit(1)
        rows.append({"name": n, "club": TEAMS[e["team"]], "pos": POS[e["element_type"]],
                     "xi": n in sq["xi"]})
    fixtures = get(FIX)
    allc = []
    for g in range(gw, (to or gw) + 1):
        allc += collisions(rows, g, fixtures)
    if not allc:
        print(f"No class-A or class-B collisions, GW{gw}" + (f"-GW{to}" if to else ""))
        return
    print("OWN-CLUB COLLISIONS (A = mutually exclusive, B = internal hedge, ! = live rates say it bites)")
    for c in allc:
        print(line(c))
    xa = [c for c in allc if c["xi"] and c["cls"] == "A" and c["gw"] == gw]
    print()
    print(f"upcoming GW{gw}: {len([c for c in allc if c['gw']==gw and c['xi']])} in the XI, "
          f"{len(xa)} of them class A")
    if len(xa) > 1:
        print("FAIL: 2+ class-A pairs in the XI - the squad is betting against itself")
        sys.exit(1)


if __name__ == "__main__":
    a = sys.argv[1:] or ["squad.json"]
    t = int(a[a.index("--to") + 1]) if "--to" in a else None
    main(a[0], t)
