---
name: gameweek-review
description: Run the full pre-deadline gameweek review for FPL manager 50930 — staleness check, availability sweep, set-piece diff, fixture and European load, a proactive pool/upgrade scan, then a named transfer and captaincy recommendation with a decision-log line. Use this whenever the user mentions a gameweek by number, asks to review the gameweek, says "GW check-in", pastes a squad in the standard format, asks what transfer to make, asks who to captain, or asks whether to play a chip — even if they don't say "review". Also use before any deadline and when planning a wildcard.
---

# Gameweek review

Pre-deadline loop for manager 50930. Objective: top 100k.

**The squad is the unit, not the player.** Every option is a whole-squad state,
including Hold. Rank states on the scorecard; pick the top. If Hold wins, hold —
because it scored best, not because moving was forbidden.

**Every step outputs a stated result. No stated output means the step was skipped.**

## Before anything

```bash
curl -sfL https://raw.githubusercontent.com/s97cy4fy2c-ctrl/fpl-2627/main/bootstrap.sh -o bs.sh && bash bs.sh
```

Read `config.json` and `docs/operating.md`. Don't re-derive what they hold —
European qualification especially.

Run `scripts/check_squad.py` for the mechanical steps. It exits non-zero on any
hard-rule breach.

## The loop

| # | Step | Output that must be stated |
|---|---|---|
| 1 | Refresh roster + fixtures; staleness check | frozen / lagged / current |
| 2 | Squad health: availability + cold-trend + current-club check (deadline day) across all 15 | every flag + every cold name + any club change, or "none" |
| 3 | Set-piece diff vs baseline | changes, or "no change" |
| 4 | Fixtures next 3 and 6, plus European load | which clubs swing |
| 5 | Pool scan: hot-trend + solver upgrade candidates, unowned | named candidates, or "none clears the bar" |
| 6 | Consult the forward plan — standing intent, does it still hold | the intent + "holds" or "invalidated by [evidence]" |
| 7 | Rank squad-states on the scorecard — Hold included | the ranked table |
| 8 | Name the pick + the case against | the recommendation |
| 9 | Captaincy in EO terms | the EO split, not a projection |
| 10 | Decision-log line (incl. rejected alternative); update the rolling intent if it changed | the line + the amended intent, or "intent unchanged" |

Steps 2 and 5 are the trend scan — cold on what we own, hot on what we don't.
**Look every week. Act only on cause.** Step 6 consults the forward plan before any
option is ranked; step 10 updates it after. **Consult, then update — one plan, never two.**

## Trend scan — look agile, act conservative

Flag outliers both directions: owned players underperforming, unowned players in
a purple patch. A flag is a prompt to investigate, never a reason to move. For
each flagged name, name the cause.

| Cause | Actionable |
|---|---|
| Role — minutes, position or starting status changed | Now |
| Set-piece — gained or lost penalties / corners | Now |
| Volume — sustained xGI or DefCon-delivered shift over >=6 starts | From GW6 only |
| Variance — finishing noise, none of the above | No. Hold / ignore |

Act on the first three. Variance is how you hold a cold player without dogma: you
looked, found no cause, held. Before GW6 the sample is too thin for volume — only
role and set-piece override.

## The bar to move

Hold is always a candidate. A move must beat Hold on the scorecard, not just fix a
local problem.

- **Free-transfer upgrade** — take it only when the ~4-GW scorecard edge beats
  banking the transfer. A banked FT is worth roughly one future move; a marginal
  upgrade fails.
- **Hit** — almost never right before GW7; the Wildcard absorbs the problem for
  free. Exception: a 5+ game absence, where a dead slot compounds faster than the
  hit costs.
- **A locally correct swap that degrades the shape is still a mistake.** Rescore
  the whole squad, not the slot.

## Forward plan — consult, then update

One rolling intent, ~3-4 GW deep, matching the transfer bar. Through GW10 it lives
in `docs/plan_gw1_gw10.md`. Consult that file; never fork it.

- **Consult (step 6).** State the standing intent and whether this week's scans just
  invalidated it. It is an input, never a cage. A locked-in intent does not raise the
  bar to move away from it.
- **Update (step 10).** If the week changed the intent, amend via the plan's own
  amendment rule: name the evidence, quote the line it replaces, log it. Overwrite is
  cheap. If nothing changed, say "unchanged" — silence is not consent.
- **Conditional intentions, not predictions.** Intended moves plus their triggers, no
  projection model. Fixtures past ~GW4 are fiction; re-pull from `/api/fixtures/` as
  rounds resolve.

At the GW10 sunset `plan_gw1_gw10.md` is re-derived from real data and becomes the
standalone rolling plan this step maintains.

## Whole-squad scorecard

Rank every state — Hold and each candidate — on these, never on names:

transferable starters · DefCon delivered · penalty takers · correlated defensive
units · midweek European load · bench outfield starts · ownership sum · cost / ITB

## Hard rules the analysis respects

- **DefCon on points DELIVERED, never a rate.** The ratio is a shortlist filter only.
- **Minutes and role before everything.** 0.6 xGI/90 at 60% of starts loses to 0.4
  at 100%.
- **Transferability** (decays GW7, dropped GW10): same club, same manager, and for
  clean-sheet assets the same defensive unit. All 15, not the 11.
- **No promoted-club starter before GW7** (COV, HUL, IPS).
- **Correlated risk** counted by club, point source and injury.
- **European load** before trusting any fixture rating. Source from `config.json`.
- **EO risk scales with variance, not ownership.** A 45%-owned floor asset is cheap
  to miss; a ceiling asset is not.
- **Differentials must be paid for** — penalties, xGI >= 0.34, or proven DefCon
  delivery. Merely unpopular is a leak.
- **No projection model.** The solver is a candidate generator; it can't see
  penalties or bench value. Solver vs written rule → the rule wins, and the
  disagreement is logged.

## Injury protocol

| Situation | Action |
|---|---|
| Out <=1 game | Nothing. The bench handles it |
| Out 2-4, bench player | Nothing |
| Out 2-4, starter | Transfer only on a spare FT. No hit before GW7 |
| Out 5+, any starter | Transfer now, hit or not |
| 2+ starters out, WC in hand | Bring the Wildcard forward, don't take hits |

## Deadline-day club check

The transfer window — through 31 Aug, again in January — can move a squad member
between clubs *after* the session-open fetch. On any deadline that falls in an open
window, re-fetch and confirm the current club of all 15 **at write time**, not just at
pull time. A changed club is a hard cause to act (doctrine §2) and its prior numbers
describe a club it left. Added 3 Sep 2026 after process error n=13 (Ndiaye moved
Everton→Man City on deadline day; the review, built on the session-open pull, missed it).

## Context discipline

Tool responses dominate context cost. Any call that might return bulk data sets
`sync_response_to_workbench: true` and is distilled in the sandbox.
`bootstrap-static` is 1.58MB — never pull it into the conversation.

## Provenance

Tag every substantive claim [live] / [repo] / [mirror, date] / [memory]. Untagged
claims from memory caused most of the logged process errors.

## Output

Lead with the pick. Then: staleness, flags and cold names, set-piece changes,
fixture and European swing, the pool-scan result, the standing forward intent and
whether it holds, the scorecard table with Hold ranked, the recommendation with the
case against, captaincy in EO terms, the decision-log line, and the updated intent if
it changed. Never a menu without a pick.

---

## Why — rationale, kept out of the reading path

- **Hold as a candidate.** Holding is earned by the scorecard, not granted by
  inertia. One mechanism stops churn and dogma at once.
- **Look every week, act on cause.** Purple patches and cold streaks are usually
  finishing variance — the market chases them and loses rank there. A trend with a
  role or set-piece cause under it is real, and no per-90 surfaces it for weeks.
  Scanning without acting on form catches the second without buying the first.
- **Conservative bar.** The frozen-XI benchmark isn't populated yet — no evidence
  churn pays. August underlying is built on ~270 minutes and misleads. The bar to
  act stays high until ~6 rounds of real data exist.
- **A persisted intent, not a second plan.** Writing the forward intent down catches
  two things a fresh weekly re-derive cannot: sequence traps — a cheap move now that
  wastes the transfer next week's move needs — and drift, weeks of quietly not doing
  the thing we meant to. It stays one plan so the GW10 falsification baseline is never
  forked, and it never raises the bar to change course.
