# operating.md

How this project runs. Deliberately short — this is the one file that loads every
session. Everything longer lives behind a skill or a script and loads on demand.

---

## Session start

```
curl -sfL https://raw.githubusercontent.com/s97cy4fy2c-ctrl/fpl-2627/main/bootstrap.sh -o bs.sh && bash bs.sh
```

Then read `config.json`. It holds the sheet ID, the schemed API endpoints and the
verified European qualification data. Do not re-derive what is already in there.

---

## Access routes — verified 20 Aug 2026

| Route | Reaches | Notes |
|---|---|---|
| **Composio sandbox** | **Full FPL API** incl. `entry/`, `element-summary/`, `event/live` | PRIMARY. Free, unlimited, complete 1.58MB bootstrap |
| Container bash | `raw.githubusercontent.com` only | `api.github.com` is 60/hr per SHARED IP — treat as unavailable |
| web_fetch | URLs already in context | Schemed URLs in repo files qualify; bare hostnames do not |
| Composio reddit | search + comments | Direct fetch is SITE_BLOCKED. Works for team news and community research |
| Composio zenrows | — | `plan.livefpl.net` returns 422 even with premium proxy. UNRESOLVED |

**Never write "don't retry" into a doc.** The old `data.md` declared four endpoints
permanently blocked and told future sessions not to retest. All four work. That
single sentence cost a week. Write the date and the tool it applied to instead.

---

## Context discipline

Tool responses dominate context cost, not standing files. One Reddit search
returned 21,778 tokens — roughly double the entire project-file baseline.

1. **Any tool call that might return bulk data sets `sync_response_to_workbench: true`,
   then distils in the sandbox.** Never pull a payload into the conversation to look
   at it.
2. **Compute where the data lives.** `bootstrap-static` is 1.58MB. Summarise it in the
   sandbox or container; print aggregates, never dataframes.
3. **Data files do not belong in project files.** The repo serves them on demand. A CSV
   sitting in project context costs ~4,000 tokens per session to be read by pandas.
4. **Procedure belongs in skills, not project files.** A project file loads whether or
   not it is relevant; a skill's body loads only when triggered, and its scripts can
   execute without entering context at all.

---

## Provenance — mandatory

Every substantive claim carries its source:

- **[live]** — fetched this session
- **[repo]** — from a committed file, with the verification date it carries
- **[mirror, DD Mon]** — from the GitHub dump, with its date
- **[memory]** — not fetched. Say so, and treat as a hypothesis.

If you can't tag it, don't assert it. Six of eight logged process errors were
untagged claims from memory presented as fact.

**Where a raw API field and a documented behaviour disagree, the documentation wins
until the field is understood.** `price_change_deadlines` lists calculation windows,
not price changes.

---

## Mechanical vs judgment

The governing failure of the first design was that rules lived in prose, and prose
does not execute. Six of eight process errors violated a rule that was already
written down.

| Goes in **code** — passes or fails loudly | Goes in **`doctrine.md`** — needs judgment |
|---|---|
| minutes and starts thresholds | the transferability thesis + its GW10 falsification |
| promoted-club exclusion before GW7 | chip triggers |
| club correlation caps (GK+DEF, 2×DEF) | what makes a differential *paid for* |
| transferability: club + manager + defensive unit | effective-ownership reasoning |
| DefCon as points DELIVERED, never a rate | when to override the solver |
| European load | tone, pushback, naming the pick |
| staleness and set-piece diffing | |
| squad legality (£100.0m, 2/5/5/3, max 3/club) | |

If a rule can be checked, it must be checked by something that fails. Writing it in
markdown and hoping is what produced the eight-item error log.

---

## Files

- `config.json` — IDs, endpoints, verified season data. Read first.
- `docs/operating.md` — this file.
- `docs/doctrine.md` — judgment only. Short and arguable.
- `docs/ledger.md` — squad, decisions, process errors. Append-only.
- `pipeline/` — the mechanical rules, as code.
- `archive/2026-08-pre-redesign/` — the four original docs, verbatim. Not live.

The spreadsheet holds `decision_log`, `benchmarks`, `process_errors` and `watchlist`.
ID is in `config.json`.
