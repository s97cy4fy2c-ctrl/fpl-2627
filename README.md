# fpl-2627

FPL 2026/27. Manager 50930. Objective: top 100k overall.

## Layout
- `docs/` — strategy and operating rules. `operating.md` loads every session; `doctrine.md` holds judgment; `ledger.md` is the append-only record.
- `skills/` — the mechanical rules, as executable code. `squad-build/scripts/build.py` and
  `gameweek-review/scripts/check_squad.py`. There is no `pipeline/` directory; it was
  superseded by skill scripts and both v1 and v2 were retired uncommitted.
- `data/` — baseline snapshots for staleness diffing.

## The recurring defect — hand-typed constants
`EUROPE` was once typed from memory and 5 of 9 clubs were wrong. It was moved into
`config.json["europe_2627"]` with a source and a date.

**The same defect recurred and was caught on 21 Aug 2026.** `NEW_MGR` in
`build.py` was a hand-typed set of ten clubs. It wrongly included Brentford —
Keith Andrews managed Brentford throughout 2025/26 and continues — and omitted
Ipswich. The effect was that every Brentford asset was silently banned by the
transferability thesis. Now derived from `config.json["new_managers_2627"]`.

Rule: a constant that describes the world does not live in a literal. It lives in
`config.json` with `_source` and a verification date. A rule whose data is typed
from recall is not a rule, it is a liability.

## DefCon is points DELIVERED, never a rate
`build.py` previously derived DefCon as a points residual, which silently absorbs
cards, saves and substitute appearances. It understated Tarkowski at +19 when he
delivered 44. The live API field `defensive_contribution` is a raw ACTION COUNT,
not points, and per-match data for a completed season is not on `element-summary`.
`defcon_delivered()` counts threshold-clearing matches from the finished archive.
