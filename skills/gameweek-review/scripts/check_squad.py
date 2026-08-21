#!/usr/bin/env python3
"""Squad legality and rule compliance. Exits non-zero on any violation.

This file exists because writing rules in markdown and hoping produced an
eight-item error log. Every check below was previously a sentence someone skipped.

Usage:  python3 check_squad.py squad.json
        {"xi": [...11 web_names...], "bench": [...4...], "captain": "...", "gw": 5}
"""
import json, sys, urllib.request
from collections import Counter

CFG = "https://raw.githubusercontent.com/s97cy4fy2c-ctrl/fpl-2627/main/config.json"
API = "https://fantasy.premierleague.com/api/bootstrap-static/"
TEAMS = {1:"ARS",2:"AVL",3:"BOU",4:"BRE",5:"BHA",6:"CHE",7:"COV",8:"CRY",9:"EVE",10:"FUL",
         11:"HUL",12:"IPS",13:"LEE",14:"LIV",15:"MCI",16:"MUN",17:"NEW",18:"NFO",19:"TOT",20:"SUN"}
POS = {1:"GKP",2:"DEF",3:"MID",4:"FWD"}
NEED = {"GKP":2,"DEF":5,"MID":5,"FWD":3}
MINXI = {"GKP":1,"DEF":3,"MID":2,"FWD":1}


def get(u):
    return json.loads(urllib.request.urlopen(
        urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=45).read())


def main(path):
    sq = json.load(open(path))
    gw = sq.get("gw", 1)
    eur = get(CFG)["europe_2627"]
    in_europe = set(eur["UCL"]) | set(eur["UEL"]) | set(eur["UECL"])

    by_name = {}
    for e in get(API)["elements"]:
        by_name.setdefault(e["web_name"], []).append(e)

    fails, warns, rows = [], [], []
    for n in sq["xi"] + sq["bench"]:
        c = by_name.get(n)
        if not c:
            fails.append(f"NOT FOUND: {n} - renamed, sold, or left the league")
            continue
        if len(c) > 1:
            warns.append(f"AMBIGUOUS: {n} matches {len(c)} - {[TEAMS[x['team']] for x in c]}")
        e = c[0]
        rows.append({"name": n, "club": TEAMS[e["team"]], "pos": POS[e["element_type"]],
                     "price": e["now_cost"] / 10, "status": e["status"],
                     "chance": e.get("chance_of_playing_next_round"),
                     "news": (e.get("news") or "")[:70], "xi": n in sq["xi"]})
    if fails:
        print(chr(10).join(fails))
        sys.exit(1)

    cost = sum(r["price"] for r in rows)
    if cost > 100.0:
        fails.append(f"BUDGET: GBP {cost:.1f}m exceeds 100.0m")
    pc = Counter(r["pos"] for r in rows)
    for p, n in NEED.items():
        if pc[p] != n:
            fails.append(f"SHAPE: {pc[p]} {p}, need {n}")
    cc = Counter(r["club"] for r in rows)
    for club, n in cc.items():
        if n > 3:
            fails.append(f"CLUB LIMIT: {n} from {club}")

    xi = [r for r in rows if r["xi"]]
    xc = Counter(r["pos"] for r in xi)
    for p, m in MINXI.items():
        if xc[p] < m:
            fails.append(f"FORMATION: {xc[p]} {p} in XI, need >= {m}")
    if len(xi) != 11:
        fails.append(f"XI has {len(xi)} players")
    if sq.get("captain") not in [r["name"] for r in xi]:
        fails.append(f"CAPTAIN {sq.get('captain')} is not in the XI")

    for r in rows:
        if r["status"] != "a":
            tgt = fails if r["xi"] else warns
            tgt.append(f"UNAVAILABLE{' (XI)' if r['xi'] else ' (bench)'}: "
                       f"{r['name']} status={r['status']} {r['news']}")
        elif r["chance"] is not None and r["chance"] < 100:
            warns.append(f"DOUBTFUL: {r['name']} {r['chance']}% - {r['news']}")

    dcl = [r["club"] for r in xi if r["pos"] in ("GKP", "DEF")]
    for club, n in Counter(dcl).items():
        if n > 1:
            warns.append(f"CORRELATED DEFENCE: {n} starting GK/DEF from {club} - one bet, not {n}")

    if gw < 7:
        for r in xi:
            if r["club"] in ("COV", "HUL", "IPS"):
                fails.append(f"PROMOTED CLUB: {r['name']} ({r['club']}) starting before GW7")

    eu = [r for r in xi if r["club"] in in_europe]
    if eu:
        warns.append(f"MIDWEEK LOAD: {len(eu)}/11 starters in Europe - "
                     + ", ".join(f"{r['name']}({r['club']})" for r in eu))

    print(f"cost GBP {cost:.1f}m | shape {dict(pc)} | max/club {max(cc.values())} | XI {dict(xc)}")
    print(f"clubs: {dict(cc)}")
    print()
    if warns:
        print("WARNINGS (judgment required):")
        for w in warns:
            print("  ~", w)
        print()
    if fails:
        print("FAILURES (must fix):")
        for f in fails:
            print("  X", f)
        sys.exit(1)
    print("All hard rules pass.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "squad.json")
