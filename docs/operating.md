# operating.md

How this project runs. Deliberately short — the one file that loads every session.
Anything longer lives behind a skill or script and loads on demand.

---

## Session start

```
curl -sfL https://raw.githubusercontent.com/s97cy4fy2c-ctrl/fpl-2627/main/bootstrap.sh -o bs.sh && bash bs.sh
```

Then read `config.json` — sheet ID, schemed API endpoints, verified European
qualification. Don't re-derive what's in there.

---

## Access routes — verified 20 Aug 2026

| Route | Reaches | Notes |
|---|---|---|
| **Composio sandbox** | **Full FPL API** incl. `entry/`, `element-summary/`, `event/live` | PRIMARY. Free, unlimited, complete 1.58MB bootstrap |
| Container bash | `raw.githubusercontent.com` only | `api.github.com` is 60/hr per SHARED IP — treat as unavailable |
| web_fetch | URLs already in context | Schemed URLs in repo files qualify; bare hostnames don't |
| Composio reddit | search + comments | Direct fetch is SITE_BLOCKED. Works for team news |
| Composio zenrows | — | `plan.livefpl.net` returns 422 even with premium proxy. UNRESOLVED |

**Never write "don't retry" into a doc.** The old `data.md` declared four endpoints
permanently blocked and told future sessions not to retest. All four work. That
sentence cost a week. Write the date and the tool it applied to instead.

---

## Context discipline

Tool responses dominate context cost, not standing files. One Reddit search returned
21,778 tokens — double the entire project-file baseline.

1. **Any bulk-data call sets `sync_response_to_workbench: true`,** then distils in the
   sandbox. Never pull a payload in to look at it.
2. **Compute where the data lives.** `bootstrap-static` is 1.58MB. Print aggregates,
   never dataframes.
3. **Data files don't belong in project files.** The repo serves them on demand.
4. **Procedure belongs in skills.** A project file loads whether relevant or not; a
   skill body loads only when triggered, and its scripts run without entering context.

---

## Provenance — mandatory

Every substantive claim carries its source:

- **[live]** — fetched this session
- **[repo]** — a committed file, with its verification date
- **[mirror, DD Mon]** — the GitHub dump, with its date
- **[memory]** — not fetched. Say so, treat as hypothesis.

If you can't tag it, don't assert it. Most logged process errors were untagged claims
from memory. Where a raw API field and documented behaviour disagree, the
documentation wins until the field is understood (`price_change_deadlines` lists
calculation windows, not price changes).

---

## Mechanical vs judgment

The governing failure of the first design: rules lived in prose, and prose doesn't
execute. Most process errors violated a rule already written down.

| In **code** — passes or fails loudly | In **`doctrine.md`** — needs judgment |
|---|---|
| minutes and starts thresholds | transferability + its GW10 falsification |
| promoted-club exclusion before GW7 | chip triggers |
| club correlation caps (GK+DEF, 2×DEF) | what makes a differential *paid for* |
| transferability: club + manager + defensive unit | effective-ownership reasoning |
| DefCon as points DELIVERED, never a rate | when to override the solver |
| European load | form-as-trigger vs cause-to-act |
| staleness and set-piece diffing | tone, pushback, naming the pick |
| squad legality (£100.0m, 2/5/5/3, max 3/club) | |

If a rule can be checked, something that fails must check it.

---

## Files

- `config.json` — IDs, endpoints, verified season data. Read first.
- `docs/operating.md` — this file.
- `docs/doctrine.md` — judgment only. Short and arguable.
- `docs/ledger.md` — squad, decisions, process errors. Append-only.
- `docs/plan_gw1_gw10.md` — pre-committed triggers, named exits, watchlist. Through
  GW10 it is the forward plan the weekly loop consults and amends; at the GW10 sunset
  it is re-derived and becomes the rolling ~3-4 GW plan.
- `skills/` — the mechanical rules, as code, plus the gameweek-review and squad-build
  loops. Load on trigger. **Read the skill body from the repo — the mounted `/mnt/skills` copy is an unsynced snapshot and lagged the 10-step redesign by a full loop version (process error n=14); the repo is authoritative.**
- `archive/2026-08-pre-redesign/` — the four original docs, verbatim. Not live.

The spreadsheet holds `decision_log`, `benchmarks`, `process_errors`, `watchlist`.
ID in `config.json`.
