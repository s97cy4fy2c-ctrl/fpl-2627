# fpl-2627

FPL 2026/27. Manager 50930. Objective: top 100k overall.

## Layout
- `docs/` — strategy and operating rules. `commitments.md` is the live one.
- `pipeline/` — `fetch_fpl_v2.py` is current. v1 kept only to show what changed and why.
- `data/` — baseline snapshots for staleness diffing.

## Why v2 replaced v1
v1 computed `dc_vs_threshold` as avg/90 over threshold — the exact quantity
`docs/analysis.md` warns against. Two players reading 1.00 delivered 7 and 28
points. v2 reports DefCon points *delivered*, adds a `transferable` flag from
`team_join_date`, pulls fixtures instead of hand-transcribing them, and detects
a frozen mirror rather than merely a lagged one.

## Known defect — do not paper over
`EUROPE` in `fetch_fpl_v2.py` was typed from memory and is wrong. It includes
Chelsea (no European football this season) and omits Aston Villa, Bournemouth,
Crystal Palace and Brighton.

Verified 20 Aug 2026 — UCL: ARS MCI MUN AVL LIV · UEL: BOU SUN CRY · UECL: BHA.

Do not fix by editing the literal. Derive it, with a source and a date attached.
A rule whose data is typed from recall is not a rule, it is a liability.
