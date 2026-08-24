# ledger.md

The record. **Append-only** — entries are never rewritten, only superseded with a
dated note. Structured data lives in the spreadsheet (`config.json` has the ID);
this file holds what needs prose.

---

## Squad

**GW1 2026/27 — COMMITTED 21 Aug 2026, before the 18:30 BST deadline.**
All values `[live]` from bootstrap-static, fetched 21 Aug 2026.

Formation 3-5-2. Cost £100.0m, ITB £0.0m. Captain Haaland, vice B.Fernandes.
No chip played.

| Slot | Player | Club | Pos | Price | Own | 25/26 pts | Starts | DefCon delivered |
|---|---|---|---|---|---|---|---|---|
| XI | Verbruggen | BHA | GKP | £4.5 | 21.6% | 130 | 38 | — |
| XI | Gabriel | ARS | DEF | £8.0 | 29.7% | 209 | 30 | +22 |
| XI | Shaw | MUN | DEF | £4.5 | 21.5% | 113 | 38 | +10 |
| XI | Tarkowski | EVE | DEF | £6.0 | 8.8% | 170 | 37 | +44 |
| XI | B.Fernandes (vc) | MUN | MID | £12.0 | 51.6% | 235 | 35 | +10 · PEN |
| XI | Ndiaye | EVE | MID | £6.0 | 16.1% | 128 | 32 | +12 · PEN |
| XI | E.Le Fée | SUN | MID | £6.0 | 10.7% | 147 | 33 | +16 |
| XI | Tzolis | ARS | MID | £6.5 | 23.7% | 0 | 0 | — |
| XI | Ampadu | LEE | MID | £5.5 | 1.5% | 134 | 35 | +38 |
| XI | Haaland (C) | MCI | FWD | £15.5 | 69.4% | 239 | 34 | — · PEN |
| XI | João Pedro | CHE | FWD | £7.5 | 64.1% | 177 | 31 | — |
| B1 | Ballard | SUN | DEF | £5.0 | 5.5% | 116 | 24 | +30 |
| B2 | F.Kadıoğlu | BHA | DEF | £4.5 | 3.0% | 118 | 34 | +4 |
| B3 | Obi | MUN | FWD | £4.5 | 1.1% | 0 | 0 | — |
| B4 | Dubravka | TOT | GKP | £4.0 | 20.2% | 96 | 35 | — |

**Whole-squad scorecard.** Raw-ownership sum (XI) 319 · DefCon delivered (XI) +152 ·
penalty takers 3 · correlated GK+DEF units in XI NONE · midweek European load 5 of
9 clubs (MCI MUN ARS SUN BHA) · bench outfield starts 58 · transferable starters
9/11 under the pre-21-Aug thesis.

**Two deliberate rule overrides, both logged.**

1. **Haaland and João Pedro forced past the transferability thesis.** Both are at
   new-manager clubs, so the thesis as written excluded them. Overridden on
   effective-ownership grounds: at 69.4% and 64.1% they are the two most-owned
   players in the game and both are ceiling assets. Doctrine §1 says EO risk
   scales with variance, so missing either concentrates rank risk far more than
   the thesis saves. See the thesis review below.
2. **Tzolis started despite failing the minutes rule (0 PL starts).** The rule
   proxies minutes certainty through Premier League history; Tzolis is an
   overseas signing with none, which is a proxy failure, not a rotation risk.
   Direct evidence overrode it: he is in the predicted Arsenal 4-3-3 as left
   winger `[live, 21 Aug]`. He takes no set pieces, so his ceiling is open play only.

**Frozen XI benchmark.** The eleven above are the control series for the
`benchmarks` tab. Never transferred, never re-picked. If frozen beats actual at
GW10, the finding is *fewer transfers, not better ones*, and the GW10 review must
say so plainly.

---

## Process errors

Full structured record: `process_errors` tab. **Ten entries logged to 21 Aug 2026.**

**Corrected 24 Aug 2026.** This section previously read "Eight logged" and carried
aggregate tables built on that count. Both were wrong. Recounted directly from the
`process_errors` tab, not from recall.

**Known defect in the tab: `n` runs 1-7, 9, 10, 11. There is no row 8.** Ten rows
exist; the highest index is 11. The gap is left in place deliberately - renumbering
an append-only log destroys the references that point at it. Do not "fix" it by
resequencing. Either row 8 was never written or it was deleted, and which of those
is true is not currently known.

The aggregate, which prose could never have produced:

| Family | Count |
|---|---|
| fast-field (club assignment, availability, transfers, calendar) | 5 |
| metric-misuse | 2 |
| process | 2 |
| role-change | 1 |

| Rule was already written in | Count |
|---|---|
| `analysis.md` (archived) | 3 |
| `data.md` (archived) | 3 |
| `operating.md` / `doctrine.md` / `README.md` (live set) | 3 |
| nowhere - a genuine gap | 1 |

| Caught by | Count |
|---|---|
| manager | 6 |
| self | 3 |
| Reddit sweep | 1 |

**Nine of ten violated a rule that already existed.** Only entry 3 had no rule behind
it. The files were never the problem. That finding drove the entire redesign:
mechanical rules moved into `check_squad.py` where they exit non-zero, and the weekly
loop moved into a skill where each step has an output that must be stated.

**The uncomfortable column is "caught by".** Manager 6, self 3, Reddit 1. The
self-caught share is better than the previously recorded "self 1" - entries 9 and 10
were both self-caught on 21 Aug and were never reflected in this file. If that ratio
has not shifted further by GW10, the redesign did not work and the GW10 review must
say so.

---

## Decision log

Structured record: `decision_log` tab. Empty until GW1 resolves — deliberately.
Seeding it with retro-fitted rationales would poison the first category review.

One row per transfer: gameweek, in, out, cost, category, rationale, rejected
alternative, then points for both over the following four gameweeks, delta, verdict.
Categories are the four from the post-mortem doctrine — fixture-chasing,
form-chasing, price-chasing, gut-differential — plus injury-forced and role-change,
which the season will produce whether planned for or not.

---

## Benchmarks

Structured record: `benchmarks` tab. Populated from
`https://fantasy.premierleague.com/api/entry/50930/history/`, which is reachable
from the Composio sandbox — so this fills itself rather than being typed in.

Three series: actual, frozen GW1 XI, template XI. The frozen XI is the control. If it
beats actual at GW10, the fix is fewer transfers, not better ones.

---

## Open items

| Item | Status |
|---|---|
| LiveFPL effective ownership | UNRESOLVED. ZenRows gets 422 even with premium proxy. Retry post-deadline when EO data exists. Screenshots remain the fallback |
| `squad-build` skill | BUILT and committed 21 Aug 2026 at `skills/squad-build/`. Was previously installed locally but absent from the repo, so MANIFEST never served it |
| Pipeline in repo | CLOSED 21 Aug 2026. No `pipeline/` directory exists; README no longer claims one. Mechanical rules live in `skills/*/scripts/` |
| Transferability thesis | **CLOSED as an open item 21 Aug 2026 — RULED, not pending.** Demoted from hard exclusion to a confidence discount by manager ruling at the GW1 deadline. `doctrine.md` §8 is the record. This row previously read "Awaiting manager confirmation", which contradicted doctrine; corrected 24 Aug 2026. The GW10 falsification test remains open and is tracked in `plan_gw1_gw10.md`, not here |
