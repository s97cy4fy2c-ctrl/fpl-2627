# method.md

Manager ID 50930. Objective: top 100k overall.

## Pre-deadline sequence

Run in order, every gameweek. Don't skip steps because the week looks quiet.

1. **Run the script.** `fetch_fpl.py` — full roster, staleness check reported first.
2. **State the lag** before using any mirror-derived number.
3. **Availability sweep** across the squad and anything on the watchlist. Live-verify by
   search for any name where the mirror flag matters to a decision.
4. **Set-piece diff** against the stored baseline. Changes here outrank most statistical
   shifts — report them unprompted.
5. **Fixture context**, next three and next six.
6. **Options at three risk levels** — safe / balanced / aggressive — each with reasoning
   and the case against.
7. **Name your pick** and why. Tiers are the options; the recommendation is still required.
8. **Captaincy in effective-ownership terms**, not raw projection.
9. **One line for the decision log**, including the rejected alternative.

## Effective ownership

The objective is rank, so the question is never "will he score" but "what happens to my
rank in each branch, given who else owns him."

- Captaining a 70%-owned player is the **defensive** play, not the bold one.
- Not owning a high-ownership asset is where risk concentrates, whether or not it feels
  like a decision.
- Differentials are only worth it where the variance is *paid for* — a low-owned player
  with a genuine route to a haul, not merely an unpopular one.

## Post-mortem

Separate **process error** from **variance** every time.

- Correct call, bad outcome → not a mistake. Log it as correct.
- Bad process, good outcome → still a mistake. Log it as such.
- Only process errors should change future behaviour.

At GW10 and GW19, review the decision log by *category* — fixture-chasing, form-chasing,
price-chasing, gut differentials — and report which categories earned. That's the
improvable thing; individual results aren't.

## Benchmarks

Track alongside actual score: the **frozen GW1 XI** (no transfers all season) and the
**template XI**. If frozen beats actual by GW10, the fix is fewer transfers, not better
ones. Say so plainly if it happens.

## Weekly input from the manager

Ask for this, in this format, at the start of each check-in:

```
GW__ | Bank £__ | FTs __ | Chips left: WC FH TC BB
XI: (formation)
Bench: 1. 2. 3. 4.
Captain / Vice:
Changes since last week + any hits
```

Screenshots of Pick Team and Transfers are faster and preferred. Low-effort fallback:
bank, free transfers, current captain.

**Conditional asks only when they'd change a decision:** LiveFPL effective ownership when
a call is close; official in-app price predictor when a move is price-sensitive;
availability changes when they occur. Never a standing ask for community chatter.

## Chip discipline

Trigger conditions get written in advance, in `commitments.md`, and are held to. Chips are
not played on vibes. First set expires at the **GW19 deadline, Sat 2 Jan 2027, 13:30 GMT**.
Wildcard and Free Hit are unavailable in GW1.
