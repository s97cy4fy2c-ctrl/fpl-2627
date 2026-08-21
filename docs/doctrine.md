# doctrine.md

Judgment only. If a rule can be checked by a script, it is **not** in this file — it
lives in `skills/gameweek-review/scripts/`. What remains here is the reasoning that
cannot be automated, and it is meant to be argued with.

Manager 50930 · objective: **top 100k overall**.

---

## 1. Rank, not points

The objective is rank, so the question is never "will he score" but "what happens to
my rank in each branch, given who else owns him."

- Captaining a 70%-owned player is the **defensive** play, not the bold one.
- Not owning a high-ownership asset is where risk concentrates, whether or not it
  feels like a decision.
- **EO risk scales with a player's variance, not his ownership.** A 45%-owned floor
  asset is cheap to miss — his realistic range might be 1 to 8 points, so the cost of
  being without him is small. A 45%-owned ceiling asset is not. This distinction is
  the whole reason the Haaland argument does not transfer to anyone else.
- **Differentials must be paid for.** Low ownership *plus* a genuine route to a haul:
  penalties, xGI >= 0.34, or proven DefCon delivery. Merely unpopular is a leak.

## 2. Reading the numbers without being fooled

- **Regression direction.** Overperformance against xG regresses down.
  Underperformance *with sustained volume* is the buy signal. The market does the
  opposite — it buys the hauler and sells the blanker. That gap is where rank is made.
- **Fixture-adjust before comparing.** Two players with equal xGI are not equal if one
  has faced the promoted clubs. Adjust, or don't compare.
- **Sample size.** Don't act on underlying data before ~6 starts unless role has
  visibly changed. Role change is the only override, and it is a real one.
- **Set-piece changes outrank statistical trends.** A new penalty taker is a
  step-change in ceiling that no per-90 trend surfaces for weeks.
- **Ownership is never evidence of quality.** It is input to variance, nothing else.
- **No projection model.** Reasoning transparently from underlying data beats
  laundering guesses into numbers that look authoritative.

## 3. The solver is a candidate generator

It screens on fetched values. It cannot see penalties (a step-change in ceiling) or
bench value (auto-subs, Bench Boost). Where the solver and a written rule disagree,
**the rule wins and the disagreement is logged.** A blind rebuild is worth running
periodically to catch anchoring — but its divergences are findings to test one at a
time, not to adopt wholesale.

## 4. Chips are not played on vibes

Trigger conditions are written in advance and held to. First set expires at the
**GW19 deadline, Sat 2 Jan 2027, 13:30 GMT**. Second set unlocks GW20.

- **Wildcard** — target GW6-GW9, once six rounds of real data exist. Earlier only if
  4+ starters are unavailable/sold/demoted AND fixing it costs 3+ hits across two
  gameweeks. Never to chase a bandwagon.
- **Bench Boost** — requires all four bench players confirmed starting. Realistically
  the week after a Wildcard, because the Wildcard is what makes the bench playable.
- **Triple Captain** — a premium on a home fixture rated 2, and only if he started and
  completed the previous two. Never in a gameweek with maximum uncertainty.
- **Free Hit** — a blank gameweek. Note the "5+ players unavailable" condition is
  **decorative**: five simultaneous injuries essentially never happens. Treat FH as a
  blank-gameweek chip and do not pretend it is injury insurance.

## 5. Hits

**Almost never right before GW7**, because the Wildcard is close enough to absorb the
problem for free. After GW7 that subsidy is gone and the arithmetic flips. The
exception either side of that line is a 5+ game absence, where a dead squad slot
compounds faster than the hit costs.

## 6. Post-mortem

Separate **process error** from **variance** every time.

- Correct call, bad outcome → not a mistake. Log it as correct.
- Bad process, good outcome → still a mistake. Log it as such.
- Only process errors change future behaviour.

At GW10 and GW19, review the decision log **by category** — fixture-chasing,
form-chasing, price-chasing, gut differentials — and report which categories earned.
That is the improvable thing; individual results are not. The `decision_log` tab makes
this a query rather than a reading exercise.

Track alongside actual score: the **frozen GW1 XI** and the **template XI**. If frozen
beats actual at GW10, the fix is fewer transfers, not better ones. Say so plainly.

## 7. Behaviour

- Lead with the call. Reasoning follows the recommendation, never replaces it.
- Disagree in the first sentence when you disagree. Don't build to it.
- **No hedging.** A qualifier that only protects you from being wrong gets cut.
  Calibration — "55/45, and here's what breaks the tie" — is required when true.
- **No punditry.** Any claim that would survive being said about any player in any
  week is filler.
- **No presenting options without naming a pick.**
- **No agreeing because you were pushed.** If challenged and still right, say so.
- Tag every substantive claim: [live] / [repo] / [mirror, date] / [memory].
  Six of eight logged process errors were untagged claims from memory.

**Known drift:** long conversations pull toward agreeableness. Correction phrases —
"you're hedging", "that's punditry", "you're agreeing too easily" — mean re-read this
file and redo the answer without defending the original.

---

## 8. PROVISIONAL — the 2026/27 transferability thesis

**Not settled. Under review. Do not treat as doctrine until the manager confirms.**

Nine of twenty clubs began the season under a new manager, a Premier League record,
and `team_join_date` shows a further set of mid-price players changed clubs. The claim
is that a player's 2025/26 numbers only describe 2026/27 if he is at the same club
under the same manager — and that of players owned above 9%, only a minority pass.

The assumption underneath, stated so it can be falsified: *role changes at
new-manager clubs degrade output more often than they improve it.* That is asymmetric
and unproven.

**Falsification test at GW10.** If the new-manager clubs have outperformed, this thesis
was wrong and the GW10 review must say so plainly rather than quietly dropping it.

**Decay schedule.** The thesis is an inference drawn in the absence of current-season
data. From GW7 it is a tiebreaker only. At GW10 it is dropped entirely in favour of
actual 2026/27 numbers.
