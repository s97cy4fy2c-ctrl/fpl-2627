# analysis.md

How to read the numbers without being fooled by them.

## Sample size

State sample size alongside any per-90 figure. Three gameweeks of xG is noise.

**Don't act on underlying data before ~6 starts** unless role has visibly changed. August
and September are the danger zone: the pipeline produces confident-looking per-90 numbers
built on 270 minutes, and they will mislead.

Pre-season figures for new signings are near-worthless. Championship stats for promoted
clubs don't translate cleanly — this is the least reliable data in the file, and it applies
to Coventry, Hull and Ipswich this season.

## Fixture-adjust before comparing

Two players with equal xGI are not equal if one has faced Hull, Coventry and Ipswich.
Never compare raw output across different fixture runs. Adjust, or don't compare.

## Regression direction

- Overperformance against xG regresses **down**.
- Underperformance against xG **with sustained volume** is the buy signal.

The market does the opposite — it buys the hauler and sells the blanker. That gap is where
rank is made.

## Role is the first filter

No amount of underlying quality survives being benched. Minutes certainty comes before
every other consideration, not as a footnote to it. A 0.6 xGI/90 player starting 60% of
matches is usually worse than a 0.4 player starting all of them.

## Set-piece changes outrank statistical trends

A player taking penalties is a step-change in ceiling that no per-90 trend will surface for
weeks. Diff against the stored baseline every week and report changes unprompted.

## Ownership is not a quality signal

High ownership tells you what happens to rank in each branch. It says nothing about whether
the player is good. Never use it as evidence for a pick — only as input to variance.

## Correlated risk

Clean sheet potential is a **team** property, not a player property. Two defenders from the
same side are one bet, not two, and it cuts both ways. Same for a defender-plus-goalkeeper
pairing. Count correlated exposure explicitly when assessing a squad.

## Defensive contribution

2 points, and from 2026/27 it applies to **forwards as well as defenders and midfielders**
(goalkeepers excluded). Thresholds: 10 defensive actions for defenders, 12 for midfielders
and forwards. Report DefCon per 90 as a *rate of clearing the threshold*, not as a raw
average — the average conceals how often it actually converts.

BPS was reworked this season: clearances, blocks and interceptions now score 1 BPS per 3
actions rather than per 2. This slightly devalues stopper centre-backs relative to
attacking full-backs and defensive midfielders for bonus purposes. DefCon points themselves
are unchanged.

## Calendar structure

- FPL's own difficulty ratings are crude. They ignore European commitments, midweek load
  and rotation risk. Treat as a starting point.
- Teams rated 2 both home and away this season: **Coventry, Hull, Ipswich**. Returns and
  clean sheets concentrate against these.
- **AFCON** is a January planning problem that catches people out annually. Flag affected
  players well before the window, not during it.
- Blanks and doubles emerge from cup progression. Don't store a list — it'll be wrong by
  December. Re-derive from the fixtures endpoint as rounds resolve.

## No projection model

Do not build or present an expected-points model. Reasoning transparently from underlying
data is better than laundering guesses into numbers that look authoritative. If a figure
can't be traced to a fetched value or a stated assumption, don't produce it.
