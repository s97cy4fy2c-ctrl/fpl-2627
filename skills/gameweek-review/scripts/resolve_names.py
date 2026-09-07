#!/usr/bin/env python3
"""Resolve player names in community text against the live roster.

Built 7 Sep 2026 after an LLM summariser, given 49k characters of r/FantasyPL
comments, invented "Jude Bellingham" for Joao Pedro, "Kasper Palmer" for Cole
Palmer, and placed Wirtz at Leicester and Mbeumo at Brentford. The fetch was
never the problem. The defect was asking a language model to do entity
resolution when a lookup table does it exactly.

Two modes, and the order matters:

  tag   <file>   Resolve names BEFORE summarising. Every match is rewritten as
                 `web_name[club]` so the model reads resolved entities instead
                 of guessing them.
  check <file>   Verify AFTER summarising. Any capitalised token that looks
                 like a player name and resolves to nothing is reported. A
                 digest that fails check is not usable.

Variants are DERIVED from bootstrap-static, never hand-typed - README rule: a
constant that describes the world does not live in a literal. The only hand
written part is the nickname map in config.json["player_aliases"], which carries
a source and a date, and covers what derivation cannot reach (JP, Bruno, TAA).
"""
import json, re, sys, unicodedata, urllib.request

API = "https://fantasy.premierleague.com/api/bootstrap-static/"
CFG = "https://raw.githubusercontent.com/s97cy4fy2c-ctrl/fpl-2627/main/config.json"
TEAMS = {1: "ARS", 2: "AVL", 3: "BOU", 4: "BRE", 5: "BHA", 6: "CHE", 7: "COV", 8: "CRY",
         9: "EVE", 10: "FUL", 11: "HUL", 12: "IPS", 13: "LEE", 14: "LIV", 15: "MCI",
         16: "MUN", 17: "NEW", 18: "NFO", 19: "TOT", 20: "SUN"}

# Words that look like names but are not. Kept short on purpose - a long
# stopword list hides real misses.
NOISE = {"FPL", "GW", "TC", "WC", "BB", "FH", "EO", "XI", "VC", "DGW", "BGW",
         "Premier", "League", "Gameweek", "Wildcard", "Free", "Hit", "Bench",
         "Boost", "Triple", "Captain", "Chelsea", "Arsenal", "Liverpool",
         "City", "United", "Spurs", "Brighton", "Everton", "Newcastle", "Leeds",
         "Hull", "Fulham", "Palace", "Villa", "Forest", "Brentford", "Sunderland",
         "Coventry", "Ipswich", "Bournemouth", "Reddit", "Opta", "Saturday",
         "Sunday", "Monday", "Friday", "Thursday", "I", "The", "My", "But", "If"}


def get(u):
    return json.loads(urllib.request.urlopen(
        urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=45).read())


def strip_marks(s):
    for a, b in (("\u00df", "ss"), ("\u00f8", "o"), ("\u00d8", "O"), ("\u0111", "d"),
                 ("\u0110", "D"), ("\u0142", "l"), ("\u0141", "L"),
                 ("\u00e6", "ae"), ("\u00c6", "AE"), ("\u0131", "i"), ("\u0130", "I")):
        s = s.replace(a, b)
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def build_index():
    """name variant (lowercased) -> (web_name, club). Derived, not typed."""
    idx, clash = {}, set()

    def add(k, val):
        k = k.strip().lower()
        if len(k) < 3 or k in NOISE:
            return
        if k in idx and idx[k] != val:
            clash.add(k)
        else:
            idx[k] = val

    for e in get(API)["elements"]:
        val = (e["web_name"], TEAMS[e["team"]])
        first, second, web = e["first_name"], e["second_name"], e["web_name"]
        forms = {web, second, f"{first} {second}", f"{first[:1]}.{second}",
                 f"{first[:1]} {second}", second.split()[-1] if second.split() else second}
        for f in list(forms):
            forms.add(strip_marks(f))
        for f in forms:
            add(f, val)
    for k in clash:                       # ambiguous surnames resolve to nothing
        idx.pop(k, None)
    try:
        for alias, web in (get(CFG).get("player_aliases", {}) or {}).items():
            if alias.startswith("_"):
                continue
            for k, v in list(idx.items()):
                if v[0] == web:
                    idx[alias.lower()] = v
                    break
    except Exception as ex:
        print(f"WARN: player_aliases unavailable ({ex}) - derived variants only", file=sys.stderr)
    return idx, clash


TOKEN = re.compile(r"\b([A-Z][\w'\u00c0-\u024f-]+(?:\s+[A-Z][\w'\u00c0-\u024f-]+)?)\b")


def tag(text, idx):
    def sub(m):
        hit = idx.get(m.group(1).lower())
        return f"{hit[0]}[{hit[1]}]" if hit else m.group(1)
    return TOKEN.sub(sub, text)


def check(text, idx):
    bad = []
    for m in TOKEN.finditer(text):
        t = m.group(1)
        if t in NOISE or t.split()[0] in NOISE:
            continue
        if t.lower() in idx:
            continue
        if " " in t or t.istitle():
            bad.append(t)
    seen, out = set(), []
    for b in bad:
        if b.lower() not in seen:
            seen.add(b.lower())
            out.append(b)
    return out


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    text = open(sys.argv[2]).read() if len(sys.argv) > 2 else sys.stdin.read()
    index, ambiguous = build_index()
    if mode == "tag":
        print(tag(text, index))
    else:
        miss = check(text, index)
        print(f"index: {len(index)} variants, {len(ambiguous)} ambiguous surnames dropped")
        if miss:
            print(f"UNRESOLVED ({len(miss)}) - drop these from the digest, do not report them:")
            for m in miss:
                print("  ?", m)
            sys.exit(1)
        print("All name-like tokens resolve to the live roster.")
