# ledger.md

The record. **Append-only** — entries are never rewritten, only superseded with a
dated note. Structured data lives in the spreadsheet (`config.json` has the ID);
this file holds what needs prose.

---

## Squad

**NOT RECORDED.** The GW1 squad is not committed here. The manager has not settled
the strategy, and recording a provisional squad as though it were decided is exactly
the kind of false certainty this redesign exists to remove.

When settled: squad table, whole-squad scorecard, and the frozen-XI benchmark that
`benchmarks` tracks against.

---

## Process errors

Full structured record: `process_errors` tab. Eight logged to 21 Aug 2026.

The aggregate, which prose could never have produced:

| Family | Count |
|---|---|
| fast-field (club assignment, availability, transfers, calendar) | 5 |
| role-change | 1 |
| metric-misuse | 1 |
| process | 1 |

| Rule was already written in | Count |
|---|---|
| `analysis.md` (archived) | 3 |
| `data.md` (archived) | 3 |
| nowhere — a genuine gap | 1 |

| Caught by | Count |
|---|---|
| manager | 6 |
| Reddit sweep | 1 |
| self | 1 |

**Six of eight violated a rule that already existed.** The files were never the
problem. That finding drove the entire redesign: mechanical rules moved into
`check_squad.py` where they exit non-zero, and the weekly loop moved into a skill
where each step has an output that must be stated.

**The uncomfortable column is "caught by".** Manager 6, self 1. If that ratio has not
shifted by GW10, the redesign did not work and the GW10 review must say so.

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
| Transferability thesis | PROVISIONAL. Falsification test GW10. 21 Aug 2026: recommended DEMOTION from hard exclusion to confidence discount — as coded it banned Haaland, and its input set was wrong. Awaiting manager confirmation |
