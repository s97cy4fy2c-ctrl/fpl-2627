---
name: squad-build
description: Build or rebuild a full 15-man FPL squad for manager 50930 under every hard constraint — budget, formation, club limits, minutes certainty, promoted-club exclusion, correlated defensive risk and transferability — then score it as a whole squad and name a pick. Use this whenever the user asks to build a squad, plan or fire a wildcard, rebuild from scratch, do a blind rebuild, restructure the team, check what a squad would look like without a given player, or asks "what should my team be" — even if they don't say "build". Also use when a player must be excluded after a transfer rumour, when comparing template-safe against aggressive shapes, and before any deadline where the whole squad is in question.
---

# Squad build

Generates 15-man squad candidates for manager 50930. Objective: top 100k.

**The solver is a candidate generator, not a recommendation.** It screens on
prior-season points — blind to penalties and bench value. Its output starts the
analysis, never ends it.

## Run it

```bash
python3 scripts/build.py --gw 1
python3 scripts/build.py --gw 8 --exclude Watkins,Konsa --max-club 2
python3 scripts/build.py --gw 12 --thesis off
```

Requires `pulp` (`pip install pulp --break-system-packages`).

First line prints `[live]` or `[mirror]`. **State which.** The API is reachable from
the Composio sandbox, 403 from the container where the mirror is the fallback — and
mirror ownership and club assignment are low-trust.

| Flag | Use |
|---|---|
| `--gw N` | Drives the expiring rules: promoted-club at GW7, transferability at GW10 |
| `--exclude` | Players removed entirely. Run the rumour sweep first while the window is open |
| `--exempt` | Forces a player in, waives transferability for him. Justify every use |
| `--max-club` | Below 3 buys wildcard flexibility |
| `--thesis off` | Disables transferability. Use from GW10, or to test what it costs |

## What it enforces — so you don't have to remember

Budget, 2/5/5/3, valid formation, max per club, minutes certainty (1800+ minutes and
24+ starts), promoted-club exclusion before GW7, no two starting GK/DEF from one club,
at most two squad players below 20 starts, transferability across all 15.

**INFEASIBLE** → relax exactly one constraint and say which. Never quietly drop a rule
to make it solve.

## What it can't see — your job

- **Penalties.** A taker is a step-change in ceiling no points total captures.
- **Bench value.** Bench points don't enter the objective; the solver will buy a dead
  bench and make Bench Boost unreachable.
- **Effective ownership.** It reports an ownership sum. Risk scales with *variance*: a
  45%-owned floor asset is cheap to miss, a ceiling asset is not.
- **Fixture swing and midweek load.** It reports European load; it doesn't weigh it.
- **Transfer rumours.** A player with agreed terms elsewhere is worth nothing, and no
  statistic tells you.

## Method

1. Run it. State `[live]` or `[mirror]`.
2. Run again with a materially different constraint — `--thesis off`, a lower
   `--max-club`, an exclusion. Two candidates beat one.
3. Compare on the scorecard, not the player list.
4. Name a pick and give the case against. A menu without a recommendation is avoidance.
5. Where you override the solver, say why. Log the disagreement.

## Whole-squad scorecard

Judge candidates on these, never on names:

transferable starters · DefCon delivered · penalty takers · correlated defensive
units · midweek European load · bench outfield starts · ownership sum · cost / ITB

## Output

Lead with the pick. Then the scorecard comparison, the case against, and one
decision-log line naming the rejected alternative.

---

## Why — rationale, kept out of the reading path

- **Two candidates, not one.** A single solve anchors you to its objective. A second
  run under a different constraint exposes what the first was blind to.
- **Score the shape, not the slot.** Three sequential individually-sensible changes
  once produced a floor-heavy squad carrying unpaid differential risk. A locally
  correct swap that degrades the shape is still a mistake — rescore the whole thing
  after every change.
