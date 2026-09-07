# plan_gw1_gw10.md

Forward plan for manager 50930, written 21 Aug 2026 before the GW1 deadline — so later
decisions are checked against a pre-committed position, not reconstructed after.

**Everything here is a trigger, not a prediction.** A trigger has a condition and an
action. Condition unmet → action doesn't fire, however the gameweek felt.

**A default, not a cage.** Written before a ball was kicked; the data ages badly.
Strong new evidence should change it — via the amendment rule below.

---

## STANDING PLAN - as at 7 Sep 2026, after GW3

**Read this first.** Everything below it is the pre-committed 21 Aug record plus dated
amendments. The originals stay in place because the GW10 falsification test needs
them; this block is what is actually live. Where the two conflict, this block wins and
the superseded line is quoted in the 7 Sep amendment at the foot of the file.

**Where we are** `[live, 7 Sep]`. 204 pts, overall rank 1,885,177. Objective top 100k.
Frozen-XI control 197, so the entire 7-point lead over doing nothing is the GW3 Triple
Captain; the Gross-for-Ndiaye transfer is -2 to date. Two FTs, 0.5 ITB, squad 99.3.

**Chips.** Triple Captain SPENT (GW3). Remaining in set one: Wildcard, Free Hit, Bench
Boost, all expiring at the **GW19 deadline, 2 Jan 2027**. Verified `[live, 7 Sep]`:
every gameweek GW4-GW19 is a full ten-fixture round and the fixture list has zero
unassigned fixtures, so **no blank exists before that expiry**. Chips are now governed
by doctrine s4 as a stopping rule, not by trigger conditions.

**The wildcard's brief has changed.** It was "six rounds of real data, then tidy up".
The real brief is now three named structural faults `[live, 7 Sep]`:

1. **DefCon has not arrived.** The squad was built on +152 delivered in 25/26. Across
   GW1-3 the XI has delivered **8 points**. Ampadu, the 1.1%-owned differential bought
   purely on DefCon, sits on 13/10/11 actions against a threshold of 12 with 0.00 xG.
2. **Two dead squad slots.** Obi and Dubravka, 0 minutes each across three gameweeks.
   This is also why Bench Boost is currently unplayable.
3. **Collision load.** Nine clubs across fifteen players produces a collision in every
   gameweek GW4-GW10, including a class A at GW5 (Verbruggen/Gabriel) and a class A at
   GW8 (Gabriel/Tarkowski - our two largest DefCon assets, mutually exclusive).

**Live decision points, in order.**

| When | Decision | State |
|---|---|---|
| GW4, Sat 12 Sep 13:30 BST | Hold vs Free Hit | **OPEN.** Lean Hold ~55/45. Tie-breaker pre-stated: if Thu/Fri team news puts 2+ of the XI in doubt, Free Hit becomes the pick |
| GW5 vs GW6 | Free Hit GW5 then Wildcard GW6, or Wildcard GW6 and Free Hit later | **50/50.** Settle with GW4 results in hand. GW5 is the more compromised week (XI FDR 3.18, class-A collision, European load begins) |
| ~GW15 | Free Hit backstop | If unplayed, play it on the best remaining week. Expiry beats optimisation |
| GW6-9 | Wildcard | Brief is the three faults above, not a tidy-up. Must design out the GW8 class A and build a playable bench for the Bench Boost |
| GW10 | Hard sunset | Unchanged. Re-derive from real data |

**European load starts GW5**, not GW1. CL/EL league phases 15-17 Sep. Six starters
affected: Gabriel, Tzolis (ARS), Shaw, B.Fernandes (MUN), Haaland (MCI), E.Le Fee
(SUN). Verbruggen and Gross (BHA, UECL) not until ~Oct. FDR is blind to all of it.

**Watchlist lives in the spreadsheet tab, not here.** Refreshed 7 Sep; the 21 Aug table
below is superseded in full.

---

## Amending this plan

**Change it when the world changed. Not when the result was bad.** That is the whole
test: did new *information* arrive, or did the last gameweek just hurt.

**Grounds — any one is enough:**

| Evidence | Why it beats the plan |
|---|---|
| **Role change** | Position, starting place, gained or lost. Doctrine's only override on sample size. Act immediately. |
| **Set-piece change** | New penalty or corner taker. Step-change in ceiling. Act same week. |
| **Transfer, in or out** | Prior numbers describe a different club. Through 31 Aug, again in January. |
| **Availability** | Injury, suspension, announced absence. Follow the injury protocol. |
| **~6 starts of 2026/27 data** | Real numbers beat pre-season inference. From GW10 they replace it entirely. |
| **DefCon delivered diverging** | Delivered, never a rate. A defender's floor is his whole case. |
| **Fixture / calendar change** | Postponements, cup progression, blanks, doubles. Re-pull `/api/fixtures/`; don't trust the grid past ~GW4. |
| **A pressure point failing to bite** | The four below are FDR inferences. If a wall doesn't materialise, say so and drop it. |

**Not grounds:**

- One bad gameweek, or one good one.
- Form, hauls or blanks with no role change behind them.
- Ownership moving on its own. Input to variance, not evidence of quality.
- Community noise. The GW1 Reddit sweep was low-signal; one call was wrong.
- Regret about a pick already made. Correct call, bad outcome, is not a mistake.

**How — three steps, all required:**

1. Name the evidence and tag it [live] / [repo] / [mirror, date].
2. Name the trigger it overrides, quoting the line it replaces.
3. Log it in `decision_log` as `plan-amendment`, and edit this file with a dated
   append. Never silently rewrite — the superseded version is the evidence.

Pre-commitment only works if breaking it is visible. At GW10, count the amendments: if
most earned, the plan was too rigid; if most didn't, it was being fudged.

**Nothing here overrides `doctrine.md`.** On conflict, doctrine wins and the
disagreement is logged.

**Hard sunset: GW10.** Re-derive the whole plan from actual 2026/27 data. Do not extend
by inertia. After GW10 the plan changes mode: no longer a fixed GW1-GW10 baseline, it
becomes a **rolling ~3-4 GW horizon** that `skills/gameweek-review` consults before
each pick (step 6) and amends after (step 10), under this same amendment rule. The
horizon matches the transfer bar; fixtures past ~4 GW out stay fiction and get
re-pulled as rounds resolve.

---

## Fixture grid, GW1-GW10

`[live]` from `/api/fixtures/`, fetched 21 Aug 2026. FDR as published; crude, and blind
to European load, so read it with the midweek section below.

| Club | GW1 | GW2 | GW3 | GW4 | GW5 | GW6 | GW7 | GW8 | GW9 | GW10 | SUM |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **MCI** | BOU(H) 3 | CRY(A) 3 | COV(H) 2 | MUN(A) 4 | SUN(H) 2 | LIV(A) 4 | IPS(H) 2 | AVL(A) 4 | BHA(H) 2 | NFO(A) 3 | 29 |
| **MUN** | HUL(A) 2 | IPS(H) 2 | EVE(A) 3 | MCI(H) 4 | FUL(A) 3 | TOT(H) 3 | LEE(A) 3 | BOU(H) 3 | CHE(A) 4 | AVL(H) 3 | 30 |
| **ARS** | COV(H) 2 | AVL(A) 4 | CHE(H) 4 | SUN(A) 3 | BHA(A) 3 | LEE(H) 2 | NFO(A) 3 | EVE(H) 3 | LIV(A) 4 | HUL(H) 2 | 30 |
| **EVE** | CRY(H) 3 | BOU(A) 3 | MUN(H) 4 | TOT(A) 3 | IPS(H) 2 | HUL(A) 2 | CHE(H) 4 | ARS(A) 5 | NEW(A) 3 | COV(H) 2 | 31 |
| **SUN** | IPS(A) 2 | FUL(H) 2 | BRE(A) 3 | ARS(H) 4 | MCI(A) 5 | BHA(H) 2 | BOU(A) 3 | LEE(H) 2 | COV(A) 2 | CHE(H) 4 | 29 |
| **LEE** | NFO(A) 3 | BRE(H) 3 | BHA(A) 3 | NEW(H) 2 | CRY(H) 3 | ARS(A) 5 | MUN(H) 4 | SUN(A) 3 | BOU(A) 3 | TOT(H) 3 | 32 |
| **CHE** | FUL(A) 3 | BHA(H) 2 | ARS(A) 5 | HUL(H) 2 | BRE(A) 3 | BOU(H) 3 | EVE(A) 3 | TOT(H) 3 | MUN(H) 4 | SUN(A) 3 | 31 |
| **BHA** | AVL(H) 3 | CHE(A) 4 | LEE(H) 2 | COV(A) 2 | ARS(H) 4 | SUN(A) 3 | CRY(H) 3 | LIV(A) 4 | MCI(A) 5 | BRE(H) 3 | 33 |
| **TOT** | BRE(A) 3 | NEW(H) 2 | NFO(A) 3 | EVE(H) 3 | AVL(H) 3 | MUN(A) 4 | COV(H) 2 | CHE(A) 4 | CRY(H) 3 | LEE(A) 3 | 30 |

## Midweek European load

In Europe: **MCI MUN ARS** (UCL), **SUN** (UEL), **BHA** (UECL). Not: EVE CHE LEE TOT —
so Tarkowski, Ndiaye, João Pedro, Ampadu and Dubravka carry no midweek rotation risk
all season.

- **Brighton play a UECL playoff 20 and 27 Aug**, between GW1 and GW2. Verbruggen
  rotates rarely; **Kadıoğlu is the exposed one**.
- **CL/EL league phases begin from GW5 (15-17 Sep).** Before then the European clubs are
  effectively domestic-only — treat MCI/MUN/ARS/SUN rotation risk as near-zero until
  GW5, re-check weekly after.

## Pressure points the grid identifies

Four places this squad gets harder, derived not guessed:

1. **GW4-5, Sunderland.** After GW1-2 (2, 2): ARS(H) 4, MCI(A) 5. Le Fée and Ballard
   blunt at once — two of fifteen, same club. First pressure point, and it lands
   *before* the wildcard window.
2. **GW7-8, Everton.** CHE(H) 4 then ARS(A) 5. Tarkowski and Ndiaye together; Tarkowski
   is the squad's largest DefCon source.
3. **GW2-3, Arsenal.** GW1 COV(H) 2 is the round's best fixture, then AVL(A) 4 and
   CHE(H) 4. Gabriel and Tzolis front-loaded on one week.
4. **GW9, Man Utd.** CHE(A) 4, with MCI(H) 4 already at GW4. Bruno priced to survive
   both; Shaw is the one to re-check.

Man Utd's GW1-2 (HUL away, IPS home) is the league's easiest opening pair — the reason
three of the fifteen are United.

## Chip triggers — pre-committed

Bench Boost and Triple Captain are available **from GW1** `[live]`; Wildcard and Free
Hit unlock at **GW2**. The first set expires at the GW19 deadline, Sat 2 Jan 2027,
13:30 GMT. Second set unlocks GW20.

| Chip | Trigger | Notes |
|---|---|---|
| **Wildcard** | Target **GW6-GW9**, once six rounds of real data exist. Fire earlier only if 4+ starters are unavailable/sold/demoted AND fixing it costs 3+ hits across two gameweeks. | GW7-8 is the natural landing spot: clears the Everton wall, lands after the thesis decays to a tiebreaker (GW7) and just before it drops (GW10). Never to chase a bandwagon. |
| **Bench Boost** | Requires **all four** bench players confirmed starting. **Currently unreachable** — Obi has 0 minutes. | Realistically the week after the Wildcard, which makes the bench playable. Don't bring it forward by buying bench value with a free transfer — that pays twice. |
| **Triple Captain** | A premium on a **home fixture rated 2**, and only if he started and completed the previous two. | Haaland rating-2 home fixtures: **GW3 COV, GW5 SUN, GW7 IPS, GW9 BHA**. GW3 is the earliest that satisfies started-and-completed. GW5 on carries midweek UCL load; GW3 doesn't. |
| **Free Hit** | A **blank gameweek**. Nothing else. | The "5+ unavailable" condition is decorative. Blanks emerge from cup progression; re-derive from `/api/fixtures/` as rounds resolve rather than storing a list. |

## Hits

**Almost never right before GW7** — the Wildcard absorbs the problem for free; after
GW7 the arithmetic flips. Exception either side: a **5+ game absence**, where a dead
slot compounds faster than the hit costs.

## Agile routes — pre-named exits

Each row is a named contingency so the decision isn't invented under time pressure.
**None fire on form alone.** Not exhaustive — it covers what was foreseeable on 21 Aug;
new evidence can add or retire rows (see *Amending this plan*).

| If this happens | Then do this | Funded by |
|---|---|---|
| **Tzolis benched or subbed early GW1-2** | The squad's only unverified role. Exit to a nailed £6.0-6.5m mid. First call **E.Anderson (MCI, £6.5m, 52 DefCon delivered, 37 starts)** — straight price swap. | Straight swap |
| **Obi still 0 minutes at the Wildcard** | Don't fix him on a free transfer. Fix him **on the Wildcard**, where the £1.0m upgrade to a playing forward (Barry EVE £5.5m / Georginio BHA £5.5m) is free. | Wildcard |
| **João Pedro's role changes under Alonso** | Bought on EO, not pre-season output. If ownership falls below ~40% the EO case is gone; re-argue from scratch, don't defend. | Re-derive |
| **Sunderland wall GW4-5 bites** | Le Fée and Ballard swing together. Move **one**, not both — moving both turns a fixture problem into a shape problem. Move Le Fée; Ballard is cheap bench cover. | 1 FT |
| **Everton wall GW7-8** | Inside the Wildcard window. **No hits** — let the Wildcard solve Tarkowski and Ndiaye together. | Wildcard |
| **Haaland injured or rotated** | Largest correlated exposure (69.4% owned, captain). No like-for-like at £15.5m. Don't chase — take the field's hit and re-plan on the Wildcard. | — |
| **A set-piece taker changes in the 15** | Set-piece changes outrank statistical trends. Report unprompted, act same week. Current takers: B.Fernandes, Ndiaye, Haaland. Tzolis takes none. | 1 FT |
| **Any starter out 5+ games** | Transfer immediately, hit or not, either side of GW7. | Hit if needed |

## Watchlist — entry conditions, not names to admire

| Player | Why | Entry condition |
|---|---|---|
| **E.Anderson (MCI, £6.5m)** | 52 DefCon delivered — joint-highest in the game; 37 starts | Confirm his deep role survived the move under Maresca. Two starts in the same role. |
| **Rice (ARS, £7.5m)** | 28 DefCon delivered, 35 starts, 18.3% owned | Only if a midfield slot opens; £1.0m more than Tzolis |
| **Mbeumo (MUN, £8.0m)** | 37.0% owned — largest remaining EO hole in the squad | If ownership climbs above ~45% the hole becomes a rank liability regardless of output |
| **Szoboszlai (LIV, £7.0m)** | 41.7% owned, 36 starts, 20 DefCon delivered | Sold in a prior session on a role-change read under Iraola, **unverified against 2026/27 minutes**. Recheck at GW3, don't re-enter before |
| **Calafiori (ARS, £5.5m)** | Most popular defender among last season's top-10k drafts | Fails the minutes rule at 22 starts. Enter only on 5 consecutive starts |
| **Barry (EVE) / Georginio (BHA), £5.5m** | Playing forwards for the Obi slot | Wildcard only |

## Transferability — RULED 21 Aug 2026

**Demoted to a confidence discount.** Manager's ruling at the GW1 deadline.
`doctrine.md` §8 is the record; read it there. Short version: a player at a
new-manager club is not banned but needs independent role confirmation — pre-season
minutes, set-piece duty, or a predicted XI. Every override is named in writing, so
they can be counted at GW10. Decay schedule and the GW10 falsification test unchanged.

## What to check first, every gameweek

Run `skills/gameweek-review`. Its ten steps each have a stated output. In this window,
the three that matter most:

1. **Availability across all 15** — Tzolis and Obi have no PL baseline.
2. **Set-piece diff** — three penalty takers is the ceiling; losing one is a
   step-change no per-90 surfaces for weeks.
3. **European load from GW5** — five of nine clubs affected, and FDR is blind to it.

---

## Amendments

Dated appends that supersede lines above; the originals stay in place as the pre-committed record (see *Amending this plan*).

### 3 Sep 2026 — Ndiaye transferred Everton → Man City (GW3)

Ndiaye moved EVE→MCI on the deadline-day window (closed 1 Sep) `[live]`, and was transferred out for Groß (BHA £5.5) at the GW3 deadline. `ledger.md` carries the GW3 ruling; the `decision_log` tab carries the transfer row. This supersedes four lines written 21 Aug, when Ndiaye was an Everton asset:

- **Midweek European load** — Ndiaye is no longer rotation-risk-free: at Man City he carries UCL load from GW5. His replacement **Groß (BHA)** carries **UECL** load once the league phase begins ~Oct — inside the wildcard window, so no action, but not risk-free either.
- **Pressure point 2 (GW7-8 Everton)** and the **Everton-wall agile route** — now **Tarkowski only**; Everton exposure in the 15 is a single asset.
- **Set-piece takers** — now **B.Fernandes, Haaland, Groß** (Groß is Brighton's penalty taker, order 1 `[live]`), keeping the squad at three pen takers after Ndiaye's pen duty left with him.

**Logging note.** The *Amending this plan* steps say to log a plan-amendment in `decision_log`. That conflicts with the tab discipline ruled after process error n=12 — `decision_log` is transfer rows only; structural and plan decisions go to `ledger.md` prose. This amendment is in `ledger.md`, not the tab. Reconcile the conflicting instruction at the GW10 sunset.


### 7 Sep 2026 - post-GW3 amendment

Grounds: **~6 starts of 2026/27 data** is not yet reached, but three other listed
grounds are - *fixture / calendar change*, *a pressure point failing to bite*, and
*DefCon delivered diverging*. Plus two doctrine rulings made the same day. Evidence
is `[live, 7 Sep]` from the FPL API unless tagged otherwise.

**1. Chip triggers - superseded.** Replaces, in the chip table:

> **Free Hit** | A **blank gameweek**. Nothing else. | The "5+ unavailable" condition
> is decorative.

Every gameweek GW4-GW19 is a full ten-fixture round; the season fixture list has zero
unassigned fixtures. No blank exists before the 2 Jan expiry, so that trigger
guaranteed the chip expired unused. Fixture-targeting is now the primary use, upside
led; a blank stays valid but is no longer the only trigger; backstop ~GW15. Full
reasoning in doctrine s4. Also superseded: **Triple Captain** row - SPENT at GW3 on
Haaland v Coventry, returned 27 (9 x3), i.e. +9 over a normal captain against a field
where 1.79m managers played the same chip the same week. **Bench Boost** row - the
note "currently unreachable" is upgraded to a decision: made reachable on the Wildcard,
or written off deliberately by ~GW15. Not left to expire by drift.

**2. Pressure point 1 (GW4-5 Sunderland) - route RETIRED, not deferred.** Replaces:

> **Sunderland wall GW4-5 bites** | ... Move **Le Fee**; Ballard is cheap bench cover.
> | 1 FT

The wall condition was met (SUN ARS(H)4, MCI(A)5) and the action was still withheld,
because the route assumed a better-fixtured replacement existed at the price and none
does: every candidate at or below 6.4 sums 10-11 over GW4-6 against Sunderland's 11.
The fixture edge exists over two gameweeks and vanishes over three. Le Fee returns to
the general wildcard pool. Recorded because this is the plan's own "a pressure point
failing to bite" ground, and the GW10 count of amendments should show it.

**3. Two new pressure points the 21 Aug FDR analysis could not see.** The four listed
were derived from the fixture grid alone, which is blind to both:

- **GW5 - the European cliff plus a class-A collision.** Six starters take on midweek
  load for the first time, and Verbruggen and Gabriel need the same clean sheet in
  BHA v ARS. XI FDR 3.18, the worst in the GW4-GW9 window.
- **GW8 - ARS v EVE, class A.** Gabriel and Tarkowski, our two largest DefCon sources,
  mutually exclusive. Inside the wildcard window, so the wildcard should design it out
  rather than the week being survived.

**4. Agile routes - status.** Tzolis exit: window closed after GW2 and the GW3
trip-wire (a third early sub or a benching) did not fire - he played 90 and returned 5.
Route CLOSED, he is a normal wildcard candidate. Obi route: STANDS, wildcard only.
Haaland route: STANDS. Set-piece takers: amended 3 Sep, now B.Fernandes, Haaland, Gross.

**5. Watchlist section - superseded in full** by the `watchlist` tab, refreshed 7 Sep.
Two findings from that refresh belong here rather than in a cell:

- **Szoboszlai's sale was an error, now confirmed.** His trigger was "recheck at GW3".
  Rechecked: 90/90/90 and he is Liverpool's penalty taker, order 1. The role-change
  read that sold him was wrong, and at 39.3% owned it is an EO hole as well as a
  points one. Re-entry on the wildcard, never on a hit.
- **The Mbeumo trigger is retired.** It read "if ownership climbs above ~45%".
  Ownership has gone 37% -> 26%; over 500,000 managers sold him before GW3. A
  one-directional trigger on a two-directional quantity is not a trigger.

**6. Hull, recorded so GW10 can grade it.** The promoted-club rule (no COV/HUL/IPS
starter before GW7) excluded the best value block of the season so far - Tzolakis,
Ajayi, Egan and Giles at 4.0-4.6 for 20-26 points each. The rule is probably still
right: Hull have three clean sheets from three against 5.05 xGC. But the exclusion was
silent, and a rule that costs something without recording the cost cannot be graded.
Both names are now on the watchlist tab, blocked with the reason attached.

**7. Fixture grid - re-verified 7 Sep.** GW4-GW9 matches the 21 Aug grid exactly. No
postponements, no rescheduling. The "fixtures past ~GW4 are fiction" warning has not
yet bitten; re-pull each week regardless.

**8. Loop changes that affect what this plan consults.** The review is now ten steps
plus **5b, a wider-context sweep** (forums, blogs, expert sites) under the new
`[community, date]` tag - hypotheses only, never evidence, barred from any scorecard or
amendment until confirmed live. And `collisions.py` now runs alongside `check_squad.py`.
The "What to check first" list below should be read as four items, not three: add
**own-club collisions across the next ~4 gameweeks**.

**Logging note, unchanged from 3 Sep.** The *Amending this plan* steps still say to log
plan-amendments in `decision_log`, which conflicts with the n=12 discipline. This
amendment is in `ledger.md` and this file, not the tab. Still flagged for GW10.
