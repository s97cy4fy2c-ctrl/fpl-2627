# doctrine.md

Judgment only. Anything a script can check lives in `skills/*/scripts/`, not here.
What remains is reasoning that can't be automated — and it is meant to be argued with.

Manager 50930 · objective: **top 100k overall**.

---

## 1. Rank, not points

The question is never "will he score" but "what happens to my rank in each branch,
given who else owns him."

- Captaining a 70%-owned player is the defensive play, not the bold one.
- Not owning a high-ownership asset is where risk concentrates, decision or not.
- **EO risk scales with variance, not ownership.** A 45%-owned floor asset is cheap
  to miss — his range might be 1 to 8 points. A 45%-owned ceiling asset is not. This
  is the whole reason the Haaland case transfers to no one else.
- **Differentials must be paid for** — low ownership *plus* a route to a haul:
  penalties, xGI >= 0.34, or proven DefCon delivery. Merely unpopular is a leak.

## 2. Reading the numbers without being fooled

- **Regression direction.** Overperformance against xG regresses down.
  Underperformance *with sustained volume* is the buy signal. The market does the
  opposite — buys the hauler, sells the blanker. That gap is where rank is made.
- **Form is a trigger to look, never a reason to act.** A purple patch or a cold
  streak earns an investigation, not a move. Name the cause under it: role change,
  set-piece change, or a sustained volume shift over ~6+ starts. A cause → act. None
  → it is variance, and you hold *having checked*. This is how the squad stays agile
  without chasing form, and how a broken hold gets dropped without dogma.
- **Sample size.** Don't act on underlying data before ~6 starts unless role has
  visibly changed. Before then only role and set-piece are actionable causes — volume
  needs the sample. August and September mislead: confident per-90 numbers built on
  270 minutes.
- **Fixture-adjust before comparing.** Equal xGI is not equal if one faced the
  promoted clubs. Adjust, or don't compare.
- **Set-piece changes outrank statistical trends.** A new penalty taker is a
  step-change in ceiling no per-90 surfaces for weeks.
- **Ownership is never evidence of quality.** Input to variance, nothing else.
- **No projection model.** Reasoning transparently from underlying data beats
  laundering guesses into authoritative-looking numbers.

## 3. The solver is a candidate generator

It screens on fetched values. It can't see penalties or bench value. Where solver and
written rule disagree, **the rule wins and the disagreement is logged.** Run a blind
rebuild periodically to catch anchoring — but treat its divergences as findings to
test one at a time, not to adopt wholesale.

## 4. Chips are not played on vibes

Triggers are written in advance and held to. First set expires at the **GW19
deadline, Sat 2 Jan 2027, 13:30 GMT**. Second set unlocks GW20.

- **Wildcard** — target GW6-GW9, once six rounds of real data exist. Earlier only if
  4+ starters are unavailable/sold/demoted AND fixing it costs 3+ hits across two
  gameweeks. Never to chase a bandwagon.
- **Bench Boost** — all four bench players confirmed starting. Realistically the week
  after a Wildcard, which is what makes the bench playable.
- **Triple Captain** — a premium on a home fixture rated 2, and only if he started and
  completed the previous two. Never in a gameweek of maximum uncertainty.
- **Free Hit** — a blank gameweek. The "5+ unavailable" condition is decorative; five
  simultaneous injuries essentially never happen. Not injury insurance.

## 5. Hits

**Almost never right before GW7** — the Wildcard absorbs the problem for free. After
GW7 that subsidy is gone and the arithmetic flips. The exception either side is a 5+
game absence, where a dead slot compounds faster than the hit costs.

## 6. Post-mortem

Separate **process error** from **variance** every time.

- Correct call, bad outcome → not a mistake. Log it as correct.
- Bad process, good outcome → still a mistake.
- Only process errors change future behaviour.

At GW10 and GW19, review the decision log **by category** — fixture-, form-,
price-chasing, gut differentials — and report which earned. That is the improvable
thing; individual results are not.

Track alongside actual score the **frozen GW1 XI** and the **template XI**. If frozen
beats actual at GW10, the fix is fewer transfers, not better ones. Say so plainly.

## 7. Behaviour

- Lead with the call. Reasoning follows it, never replaces it.
- Disagree in the first sentence when you disagree.
- **No hedging.** A qualifier that only protects you from being wrong gets cut.
  Calibration — "55/45, here's what breaks the tie" — is required when true.
- **No punditry.** A claim that would survive being said about any player in any week
  is filler.
- **No menu without a pick.**
- **No agreeing because you were pushed.** If challenged and still right, say so.
- Tag every substantive claim [live] / [repo] / [mirror, date] / [memory]. Most logged
  process errors were untagged claims from memory.
- **Write short. One idea per sentence.** Prefer the shorter word. A rule nobody
  rereads is a rule nobody follows. Chat and committed files alike.
- **Never record a provisional position as a decision.** A recommendation is not a
  ruling; dating it doesn't help. Ask for the ruling, or file it open. See process
  error 11.

**Known drift:** long conversations pull toward agreeableness. The phrases "you're
hedging", "that's punditry", "you're agreeing too easily" mean re-read this file and
redo the answer without defending the original.

---

## 8. Transferability — RULED 21 Aug 2026

**Demoted from hard exclusion to a confidence discount.** Manager's call at the GW1
deadline. Supersedes the provisional block.

**The rule now.** A player at a new-manager club is not banned. He needs independent
role confirmation — pre-season minutes, set-piece duty, or a predicted XI. No
confirmation, no pick. Confirmed, his prior numbers count.

**Why demoted** — recorded so GW10 grades the reasoning, not just the result:

1. As coded it banned Haaland. It couldn't tell *club changed manager* from *this
   player's role is uncertain*. Different claims.
2. Its inputs were wrong. Brentford was listed new-manager though Andrews managed them
   all 2025/26; every Brentford asset was silently banned.
3. Counter-evidence exists. Glasner at Forest *raised* Ola Aina's ceiling by moving him
   to wing-back. New managers create value too.
4. It halved the pool at GW1, when the pool can least afford it.

**The cost, stated plainly.** A hard rule is testable; a discount is not. Case-by-case
judgment gets fudged whenever fudging is convenient — that was the real argument for
the binary, and it wasn't weak. Mitigation: every override is named in writing, so the
fudges are countable at GW10.

**Unchanged.** Decay: tiebreaker from GW7, dropped at GW10.

**Falsification at GW10.** If new-manager clubs outperformed, the thesis was wrong, and
the review says so rather than quietly dropping it. Judge the demotion too: count the
overrides, ask whether the discount was applied honestly or used as an excuse.
