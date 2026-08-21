---
name: gameweek-review
description: Run the full pre-deadline gameweek review for FPL manager 50930 — staleness check, availability sweep, set-piece diff, fixture and European load, then a named transfer and captaincy recommendation with a decision-log line. Use this whenever the user mentions a gameweek by number, asks to review the gameweek, says "GW check-in", pastes a squad in the standard format, asks what transfer to make, asks who to captain, or asks whether to play a chip — even if they don't say "review". Also use before any deadline and when planning a wildcard.
---

# Gameweek review

The pre-deadline loop for FPL manager 50930. Objective: top 100k overall.

**Every step below has an OUTPUT that must be stated aloud. A step with no stated
output did not happen.** This is not ceremony — six of eight logged process errors
were rules that already existed and were skipped.

## Before anything

```bash
curl -sfL https://raw.githubusercontent.com/s97cy4fy2c-ctrl/fpl-2627/main/bootstrap.sh -o bs.sh && bash bs.sh
```

Read `config.json` and `docs/operating.md`. Do not re-derive what they contain —
in particular the European qualification block, which was previously wrong because
it was typed from memory.

## The loop

| # | Step | Output that must be stated |
|---|---|---|
| 1 | Pull roster + fixtures; staleness check | frozen / lagged / current |
| 2 | Availability sweep across all 15 | every flag, or "none" |
| 3 | Set-piece diff vs baseline | changes, or "no change" |
| 4 | Fixtures next 3 and next 6, **plus European load** | which clubs swing |
| 5 | Rumour sweep — **only while the window is open** | names cleared / amber |
| 6 | Options at three risk levels, then **name the pick** | the recommendation |
| 7 | Captaincy in effective-ownership terms | the EO split, not a projection |
| 8 | Whole-squad rescore | the deltas vs last week |
| 9 | One decision-log line, incl. the rejected alternative | the line |

Run `scripts/check_squad.py` for steps 1-4 rather than eyeballing them. It exits
non-zero on any hard-rule violation.

## Hard rules the analysis must respect

- **DefCon on points DELIVERED, never a rate.** Two players averaging exactly 1.00x
  threshold delivered 7 and 28 points. The ratio is a shortlist filter only.
- **Minutes and role before everything.** 0.6 xGI/90 at 60% of starts loses to 0.4
  at 100%.
- **Transferability** (decays from GW7, drop at GW10): same club, same manager, and
  for clean-sheet assets the same *defensive unit*. Applies to all 15, not the 11 —
  bench players auto-sub into the XI.
- **No promoted-club starter before GW7** (COV, HUL, IPS).
- **Correlated risk counted three ways**: by club, by point source, by injury.
- **European load** before trusting any fixture rating. Source from `config.json`.
- **EO risk scales with variance, not ownership.** A 45%-owned floor asset is cheap
  to miss; a 45%-owned ceiling asset is not.
- **Differentials must be paid for** — penalties, xGI >= 0.34, or proven DefCon
  delivery. Merely unpopular is a leak.
- **No projection model.** A solver is a candidate generator. It cannot see penalties
  or bench value. Where solver and written rule disagree, the rule wins and the
  disagreement is logged.

## Injury protocol

| Situation | Action |
|---|---|
| Out <= 1 game | Nothing. The bench handles it |
| Out 2-4, bench player | Nothing |
| Out 2-4, starter | Transfer only if an FT is spare. **No hit before GW7** |
| Out 5+, any starter | Transfer immediately, hit or not |
| 2+ starters out, WC in hand | Bring the Wildcard forward rather than take hits |

## Context discipline

Tool responses dominate context cost. Any call that might return bulk data sets
`sync_response_to_workbench: true` and is distilled in the sandbox.
`bootstrap-static` is 1.58MB — never pull it into the conversation.

## Output format

Lead with the call. Then: staleness verdict, flags, set-piece changes, fixture and
European swing, the recommendation with the case against it, captaincy in EO terms,
and the decision-log line. Do not present options without naming a pick.
