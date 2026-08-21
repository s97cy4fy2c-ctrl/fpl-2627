#!/usr/bin/env python3
"""Squad candidate generator. NOT a points projection.

Screens on fetched values under hard constraints. The objective is prior-season
total_points, which is a SCREENING HEURISTIC, not a forecast. It is blind to
penalties (a step-change in ceiling) and to bench value (auto-subs, Bench Boost).
Where this disagrees with written doctrine, doctrine wins and the disagreement
gets logged.

Usage:
  python3 build.py --gw 1
  python3 build.py --gw 8 --thesis off --exclude Watkins --max-club 2
"""
import argparse, collections, csv, io, json, sys, unicodedata, urllib.request
from collections import Counter

CFG = "https://raw.githubusercontent.com/s97cy4fy2c-ctrl/fpl-2627/main/config.json"
API = "https://fantasy.premierleague.com/api/bootstrap-static/"
TEAMS = {1: "ARS", 2: "AVL", 3: "BOU", 4: "BRE", 5: "BHA", 6: "CHE", 7: "COV", 8: "CRY",
         9: "EVE", 10: "FUL", 11: "HUL", 12: "IPS", 13: "LEE", 14: "LIV", 15: "MCI",
         16: "MUN", 17: "NEW", 18: "NFO", 19: "TOT", 20: "SUN"}
POS = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD"}
NEED = {"GKP": 2, "DEF": 5, "MID": 5, "FWD": 3}
MINXI = {"GKP": 1, "DEF": 3, "MID": 2, "FWD": 1}
MAXXI = {"GKP": 1, "DEF": 5, "MID": 5, "FWD": 3}
GOAL = {"GKP": 10, "DEF": 6, "MID": 5, "FWD": 4}
CS = {"GKP": 4, "DEF": 4, "MID": 1, "FWD": 0}
PROMOTED = {"COV", "HUL", "IPS"}
# NEW_MGR is deliberately NOT a literal. It is derived from
# config.json["new_managers_2627"], which carries a source and a date.
# The previous literal was typed from recall and was wrong: it included BRE
# (Andrews managed Brentford throughout 2025/26) and omitted IPS. Same defect
# family as the old EUROPE literal. Do not reintroduce a hand-typed set here.
NEW_MGR = set()  # populated in load() from config.json


MIRROR = ("https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/"
          "master/data/2026-27/players_raw.csv")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=60).read())


def elements():
    """Live API where reachable, mirror otherwise.

    The FPL API is reachable from the Composio sandbox but NOT from the Claude
    container, where fantasy.premierleague.com returns 403. The mirror is on
    raw.githubusercontent.com, which the container can reach. Whichever source
    is used is printed, because an undated figure is an untagged claim.
    """
    try:
        data = get(API)["elements"]
        print("[live] bootstrap-static")
        return data
    except Exception as exc:
        print(f"[mirror] live API unreachable ({type(exc).__name__}) - falling back")
        print("[mirror] WARNING: ownership and club assignment are LOW TRUST here")
        import csv, io
        raw = urllib.request.urlopen(
            urllib.request.Request(MIRROR, headers={"User-Agent": "Mozilla/5.0"}),
            timeout=90).read().decode("utf-8")
        out = []
        for r in csv.DictReader(io.StringIO(raw)):
            def num(k, default=0):
                v = r.get(k, "")
                try:
                    return type(default)(float(v))
                except (TypeError, ValueError):
                    return default
            out.append({
                "web_name": r["web_name"], "team": int(r["team"]),
                "element_type": int(r["element_type"]), "now_cost": int(r["now_cost"]),
                "selected_by_percent": r.get("selected_by_percent") or "0",
                "total_points": num("total_points"), "starts": num("starts"),
                "minutes": num("minutes"), "goals_scored": num("goals_scored"),
                "assists": num("assists"), "clean_sheets": num("clean_sheets"),
                "bonus": num("bonus"), "status": r.get("status", "a"),
                "team_join_date": r.get("team_join_date", ""),
                "penalties_order": num("penalties_order", 0) or None,
                "expected_goal_involvements_per_90":
                    r.get("expected_goal_involvements_per_90") or "0",
            })
        return out


def _key(e):
    s = f"{e.get('first_name', '')} {e.get('second_name', '')}"
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower().strip()


DC_DELIVERED = {}


def defcon_delivered(season="2025-26"):
    """DefCon points DELIVERED. An outcome, never a rate.

    The live API gives `defensive_contribution` as a raw ACTION COUNT and
    `defensive_contribution_per_90` as a rate. Neither is points. Per-match data
    for a COMPLETED season is not available on element-summary (its `history`
    array covers the current season only, and is empty before GW1), so this
    reads the finished per-match archive and counts matches that cleared the
    threshold: 10 for defenders, 12 for midfielders and forwards, GK excluded.

    Verified 21 Aug 2026: the old residual understated Tarkowski at +19 when he
    actually delivered 44 points, because the residual absorbs cards, saves and
    substitute appearance points.
    """
    url = ("https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/"
           f"master/data/{season}/gws/merged_gw.csv")
    th = {"DEF": 10, "MID": 12, "FWD": 12}
    hits = collections.Counter()
    raw = urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}),
        timeout=120).read().decode("utf-8")
    for r in csv.DictReader(io.StringIO(raw)):
        p = r.get("position")
        if p in th and float(r.get("defensive_contribution") or 0) >= th[p]:
            k = unicodedata.normalize("NFKD", r["name"]).encode(
                "ascii", "ignore").decode().lower().strip()
            hits[k] += 1
    return {k: v * 2 for k, v in hits.items()}


def load():
    cfg = get(CFG)
    eur = cfg["europe_2627"]
    NEW_MGR.update(cfg["new_managers_2627"]["clubs"])
    if not DC_DELIVERED:
        DC_DELIVERED.update(defcon_delivered())
    in_eu = set(eur["UCL"]) | set(eur["UEL"]) | set(eur["UECL"])
    rows = []
    for e in elements():
        if e["status"] != "a":
            continue
        pos, club = POS[e["element_type"]], TEAMS[e["team"]]
        starts, mins = e.get("starts") or 0, e.get("minutes") or 0
        # DefCon DELIVERED, by residual. An outcome, not a rate. The ratio
        # overstated lumpy players fourfold, so it is deliberately not used.
        dc = 0 if pos == "GKP" else DC_DELIVERED.get(_key(e), 0)
        new_club = (e.get("team_join_date") or "") >= "2026-06-01"
        rows.append(dict(
            name=e["web_name"], club=club, pos=pos, cost=e["now_cost"],
            own=float(e["selected_by_percent"]), pts=e["total_points"],
            starts=starts, mins=mins,
            xgi=float(e.get("expected_goal_involvements_per_90") or 0),
            pen1=1 if e.get("penalties_order") == 1 else 0,
            dc=dc, europe=club in in_eu,
            transferable=(not new_club and club not in NEW_MGR and club not in PROMOTED),
            nailed=(mins >= 1800 and starts >= 24),
        ))
    return rows


def solve(rows, gw, thesis, exempt, max_club, budget):
    try:
        import pulp
    except ImportError:
        sys.exit("pulp missing:  pip install pulp --break-system-packages")

    idx = range(len(rows))
    prob = pulp.LpProblem("squad", pulp.LpMaximize)
    s = pulp.LpVariable.dicts("s", idx, cat="Binary")
    x = pulp.LpVariable.dicts("x", idx, cat="Binary")
    prob += pulp.lpSum(rows[i]["pts"] * x[i] for i in idx)

    for i in idx:
        prob += x[i] <= s[i]
    prob += pulp.lpSum(s[i] for i in idx) == 15
    prob += pulp.lpSum(x[i] for i in idx) == 11
    prob += pulp.lpSum(rows[i]["cost"] * s[i] for i in idx) <= budget

    for pos, n in NEED.items():
        prob += pulp.lpSum(s[i] for i in idx if rows[i]["pos"] == pos) == n
        prob += pulp.lpSum(x[i] for i in idx if rows[i]["pos"] == pos) >= MINXI[pos]
        prob += pulp.lpSum(x[i] for i in idx if rows[i]["pos"] == pos) <= MAXXI[pos]

    for club in {r["club"] for r in rows}:
        prob += pulp.lpSum(s[i] for i in idx if rows[i]["club"] == club) <= max_club
        # Correlated clean-sheet risk: two defensive units from one club are ONE bet.
        prob += pulp.lpSum(x[i] for i in idx if rows[i]["club"] == club
                           and rows[i]["pos"] in ("GKP", "DEF")) <= 1

    # Minutes and role before everything else.
    prob += pulp.lpSum(x[i] for i in idx if not rows[i]["nailed"]) == 0

    # Championship data does not translate. Expires GW7.
    if gw < 7:
        prob += pulp.lpSum(x[i] for i in idx if rows[i]["club"] in PROMOTED) == 0

    # A bench that cannot auto-sub makes Bench Boost unreachable.
    prob += pulp.lpSum(s[i] for i in idx if rows[i]["starts"] < 20) <= 2

    # Transferability: same club, same manager. Decays from GW7, dropped at GW10.
    # Applies to all 15 outfield, not the 11 - bench players auto-sub into the XI.
    if thesis and gw < 10:
        for i in idx:
            if not rows[i]["transferable"] and rows[i]["name"] not in exempt:
                prob += x[i] == 0
                if rows[i]["pos"] != "GKP":
                    prob += s[i] == 0

    for name in exempt:
        if any(rows[i]["name"] == name for i in idx):
            prob += pulp.lpSum(x[i] for i in idx if rows[i]["name"] == name) == 1

    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    if pulp.LpStatus[prob.status] != "Optimal":
        sys.exit(f"INFEASIBLE ({pulp.LpStatus[prob.status]}). Relax ONE constraint and "
                 "say which. Never silently drop a rule to make it solve.")
    return [i for i in idx if s[i].value() > 0.5], [i for i in idx if x[i].value() > 0.5]


def scorecard(rows, squad, xi_idx):
    squad_rows = [rows[i] for i in squad]
    xi = [rows[i] for i in xi_idx]
    bench = [r for r in squad_rows if r not in xi]
    cost = sum(r["cost"] for r in squad_rows) / 10
    defclubs = [r["club"] for r in xi if r["pos"] in ("GKP", "DEF")]
    dupes = [c for c, v in Counter(defclubs).items() if v > 1]

    print(f"\nCOST £{cost:.1f}m | ITB £{100 - cost:.1f}m | "
          f"max/club {max(Counter(r['club'] for r in squad_rows).values())}")
    print(f"XI shape {dict(Counter(r['pos'] for r in xi))} | "
          f"XI ownership sum {sum(r['own'] for r in xi):.0f}")
    print(f"transferable starters       {sum(r['transferable'] for r in xi)}/11")
    print(f"DefCon delivered (XI)       {sum(r['dc'] for r in xi):+.0f}")
    print(f"penalty takers in XI        {sum(r['pen1'] for r in xi)}")
    print(f"XI GK+DEF clubs {defclubs} -> correlated {dupes or 'NONE'}")
    print(f"midweek European load       {sum(r['europe'] for r in xi)}/11")
    print(f"bench outfield starts       {sum(r['starts'] for r in bench if r['pos'] != 'GKP')}")
    print()
    order = ("GKP", "DEF", "MID", "FWD")
    for label, group in (("XI", xi), ("BENCH", bench)):
        for r in sorted(group, key=lambda z: order.index(z["pos"])):
            print(f"  {label:<5} {r['name']:<16}{r['club']:<5}{r['pos']:<5}"
                  f"£{r['cost'] / 10:<6.1f}{r['own']:>5.1f}%{r['pts']:>5}pts"
                  f"{r['starts']:>3}st  xgi {r['xgi']:.2f}  dc {r['dc']:+.0f}"
                  f"{'  PEN' if r['pen1'] else ''}{'  EUR' if r['europe'] else ''}")
    print("\nThis is a CANDIDATE, not a recommendation. The objective cannot see")
    print("penalties or bench value. Check against doctrine before proposing it.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gw", type=int, default=1)
    ap.add_argument("--thesis", default="transferable", help="'transferable' or 'off'")
    ap.add_argument("--exempt", default="", help="comma-sep names exempt from transferability")
    ap.add_argument("--exclude", default="", help="comma-sep names removed entirely (rumour sweep)")
    ap.add_argument("--max-club", type=int, default=3)
    ap.add_argument("--budget", type=int, default=1000)
    args = ap.parse_args()

    rows = load()
    drop = {n.strip() for n in args.exclude.split(",") if n.strip()}
    if drop:
        before = len(rows)
        rows = [r for r in rows if r["name"] not in drop]
        print(f"excluded {before - len(rows)} rows: {sorted(drop)}")
    exempt = {n.strip() for n in args.exempt.split(",") if n.strip()}
    squad, xi = solve(rows, args.gw, args.thesis == "transferable",
                      exempt, args.max_club, args.budget)
    scorecard(rows, squad, xi)


if __name__ == "__main__":
    main()
