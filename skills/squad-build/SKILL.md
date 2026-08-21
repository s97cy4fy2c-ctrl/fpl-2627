---
name: squad-build
description: Build or rebuild a full 15-man FPL squad for manager 50930 under every hard constraint — budget, formation, club limits, minutes certainty, promoted-club exclusion, correlated defensive risk and transferability — then score it as a whole squad and name a pick. Use this whenever the user asks to build a squad, plan or fire a wildcard, rebuild from scratch, do a blind rebuild, restructure the team, check what a squad would look like without a given player, or asks "what should my team be" — even if they don't say "build". Also use when a player must be excluded after a transfer rumour, when comparing template-safe against aggressive shapes, and before any deadline where the whole squad is in question.
---

# Squad build

Generates squad candidates for manager 50930. Objective: top 100k overall.

**The solver is a candidate generator, not a recommendation.** It screens on
prior-season points, which cannot see penalties (a step-change in ceiling) or bench
value (auto-subs, Bench Boost). Its output is the start of the analysis, never the
end of it.

## Run it

```bash
python3 scripts/build.py --gw 1
python3 scripts/build.py --gw 8 --exclude Watkins,Konsa --max-club 2
python3 scripts/build.py --gw 12 --thesis off
```

Requires `pulp` (`pip install pulp --break-system-packages`).

The script prints `[live]` or `[mirror]` as its first line. **State which.** The FPL
API is reachable from the Composio sandbox but returns 403 from the Claude container,
where the mirror is the fallback — and mirror ownership and club assignment are
low-trust fields.

| Flag | Use |
|---|---|
| `--gw N` | Drives the rules that expire: promoted-club at GW7, transferability at GW10 |
| `--exclude` | Players removed entirely. **Run the rumour sweep first** while the window is open |
| `--exempt` | Forces a player in and waives transferability for him. Justify every use |
| `--max-club` | Lower than 3 buys wildcard flexibility |
| `--thesis off` | Disables transferability. Use from GW10, or to test what it costs |

## What the script enforces, so you don't have to remember

Budget, 2/5/5/3, valid formation, max per club, minutes certainty (1800+ minutes and
24+ starts to start), promoted-club exclusion before GW7, no two starting GK/DEF from
one club, at most two squad players below 20 starts, and transferability across all
15 outfield rather than just the 11.

If it says **INFEASIBLE**, relax exactly one constraint and say which one. Never
quietly drop a rule to make it solve.

## What the script cannot see — this is your job

- **Penalties.** A taker is a step-change in ceiling no points total captures.
- **Bench value.** Bench points don't enter the objective, so the solver will happily
  buy a dead bench and make Bench Boost unreachable.
- **Effective ownership.** It reports an ownership sum, which is not EO. Risk scales
  with a player's *variance*, not his ownership: a 45%-owned floor asset is cheap to
  miss, a 45%-owned ceiling asset is not.
- **Fixture swing and midweek load.** It reports European load; it does not weigh it.
- **Transfer rumours.** A player with agreed terms elsewhere is worth nothing, and no
  statistic will tell you.

## Method

1. Run it. State `[live]` or `[mirror]`.
2. Run it again with a materially different constraint — `--thesis off`, a lower
   `--max-club`, an exclusion. Two candidates beat one.
3. Compare on the scorecard, not on the player list.
4. **Name a pick and give the case against it.** A menu without a recommendation is
   avoidance.
5. Where you override the solver, say so and say why. Log the disagreement.

## Whole-squad scorecard

Judge candidates on these, never on individual names:

transferable starters · DefCon delivered · penalty takers · correlated defensive
units · midweek European load · bench outfield starts · ownership sum · cost and ITB

**A locally correct swap that degrades the shape is still a mistake.** Three sequential
individually-sensible changes once produced a floor-heavy squad carrying unpaid
differential risk. Rescore the whole thing after every change.

## Output

Lead with the pick. Then the scorecard comparison, the case against, and one
decision-log line naming the rejected alternative.
