# plan_gw1_gw10.md

Forward plan for manager 50930. Written 21 Aug 2026, before the GW1 deadline,
so that later decisions are checked against a pre-committed position rather than
reconstructed after the fact.

**Everything here is a trigger, not a prediction.** A trigger has a condition and
an action. If a condition is not met, the action does not fire — regardless of how
the gameweek felt.

**This plan is a default, not a cage.** It is written from data available on
21 Aug 2026, before a single ball was kicked. That data will age badly. Strong new
evidence should change it. The amendment rule below is how.

---

## Amending this plan

**Change it when the world changed. Not when the result was bad.**

That is the whole test. A plan that survives every outcome is dogma. A plan that
folds after every red arrow is noise. The line between them is whether new
*information* arrived, not whether the last gameweek hurt.

**Grounds to amend — any one is enough:**

| Evidence | Why it beats the plan |
|---|---|
| **Role change** | A player moved position, lost his starting place, or gained one. Doctrine's only override on sample size. Act immediately. |
| **Set-piece change** | A new penalty or corner taker. A step-change in ceiling no per-90 trend surfaces for weeks. Outranks statistical trends. Act same week. |
| **Transfer, in or out** | Prior numbers describe a different club. Applies through 31 Aug and again in January. |
| **Availability** | Injury, suspension, an announced absence. Follow the injury protocol, not this plan. |
| **~6 starts of 2026/27 underlying data** | Real numbers beat pre-season inference. From GW10 they replace it entirely. |
| **DefCon delivered diverging from last season** | Delivered, never a rate. A defender's floor is his whole case; if it has gone, so has the pick. |
| **Fixture or calendar change** | Postponements, cup progression, blanks and doubles. Re-pull from `/api/fixtures/`; do not trust the grid above after ~GW4. |
| **A pressure point failing to bite** | The four below are inferences from FDR. If a wall does not materialise, say so and drop it. |

**Not grounds to amend:**

- One bad gameweek. One good one.
- Form, hauls or blanks with no role change behind them. The market buys the hauler
  and sells the blanker; that gap is where rank is made.
- Ownership moving, on its own. Ownership is input to variance, not evidence of quality.
- Community noise. The GW1 Reddit sweep was low-signal and one of its calls was wrong.
- Regret about a pick already made. Correct call, bad outcome, is not a mistake.

**How to amend — three steps, all required:**

1. **Name the evidence** and tag it `[live]` / `[repo]` / `[mirror, date]`.
2. **Name the trigger it overrides**, quoting the line it replaces.
3. **Log it** in `decision_log` with category `plan-amendment`, and edit this file.
   Append the change with a date. Do not silently rewrite — the superseded version
   is the evidence.

**Why step 3 matters.** Pre-commitment only works if breaking it is visible. An
uncounted amendment is indistinguishable from having had no plan. At GW10, count
the amendments and ask whether they earned. If most did, this plan was too rigid.
If most did not, it was being fudged.

**Nothing here overrides `doctrine.md`.** Where this plan and doctrine disagree,
doctrine wins and the disagreement gets logged.

**Hard sunset: GW10.** Re-derive the whole plan from actual 2026/27 data. Do not
extend it by inertia.

---

## Fixture grid, GW1-GW10

`[live]` from `/api/fixtures/`, fetched 21 Aug 2026. FDR as published; crude, and
blind to European load, so read it with the midweek section below.

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

In Europe: **MCI MUN ARS** (UCL), **SUN** (UEL), **BHA** (UECL). Not in Europe:
EVE CHE LEE TOT — so Tarkowski, Ndiaye, João Pedro, Ampadu and Dubravka carry no
midweek rotation risk all season.

- **Brighton play a UECL playoff 20 and 27 Aug** — i.e. between GW1 and GW2.
  Verbruggen is a goalkeeper and rotates rarely; **Kadıoğlu is the exposed one**.
- **CL/EL league phases begin 15-17 Sep, i.e. from GW5.** Before GW5 the European
  clubs are effectively domestic-only. Rotation risk on MCI, MUN, ARS and SUN
  assets should be treated as near-zero until then and re-checked weekly after.

## Pressure points the grid identifies

These are the four places this squad gets harder, derived, not guessed:

1. **GW4-GW5, Sunderland.** After GW1-2 (2, 2) they get ARS(H) 4 then MCI(A) 5.
   Le Fée and Ballard both blunt at once — two of fifteen, same club, same swing.
   This is the **first** pressure point and it lands *before* the wildcard window.
2. **GW7-GW8, Everton.** CHE(H) 4 then ARS(A) 5. Tarkowski and Ndiaye together —
   again a paired swing, and Tarkowski is the single largest DefCon source in the squad.
3. **GW2-GW3, Arsenal.** GW1 COV(H) 2 is the best fixture in the round, then AVL(A) 4
   and CHE(H) 4 immediately. Gabriel and Tzolis are front-loaded on one week.
4. **GW9, Manchester United.** CHE(A) 4, with MCI(H) 4 already at GW4. Bruno is
   priced to survive both; Shaw is the one to re-check.

Manchester United's GW1-GW2 (HUL away, IPS home) is the easiest opening pair in
the league and is the reason three of the fifteen are United.

## Chip triggers — pre-committed

Bench Boost and Triple Captain are available **from GW1** `[live]`; Wildcard and
Free Hit unlock at **GW2**. The first set expires at the GW19 deadline,
Sat 2 Jan 2027, 13:30 GMT. Second set unlocks GW20.

| Chip | Trigger | Notes |
|---|---|---|
| **Wildcard** | Target **GW6-GW9**, once six rounds of real data exist. Fire earlier only if 4+ starters are unavailable/sold/demoted AND fixing it costs 3+ hits across two gameweeks. | GW7-8 is the natural landing spot: it clears the Everton wall and lands after the transferability thesis has decayed to a tiebreaker (GW7) and just before it is dropped entirely (GW10). Never to chase a bandwagon. |
| **Bench Boost** | Requires **all four** bench players confirmed starting. **Currently unreachable** — Obi has 0 minutes. | Realistically the week after the Wildcard, because the Wildcard is what makes the bench playable. Do not bring it forward by buying bench value with a free transfer; that is paying twice. |
| **Triple Captain** | A premium on a **home fixture rated 2**, and only if he started and completed the previous two. | Haaland's rating-2 home fixtures in this window: **GW3 COV(H), GW5 SUN(H), GW7 IPS(H), GW9 BHA(H)**. GW3 is the earliest that can satisfy the started-and-completed condition. GW5 onward carries midweek UCL load; GW3 does not. |
| **Free Hit** | A **blank gameweek**. Nothing else. | The "5+ players unavailable" condition is decorative — five simultaneous injuries essentially never happens. Do not treat FH as injury insurance. Blanks emerge from cup progression; re-derive from `/api/fixtures/` as rounds resolve rather than storing a list. |

## Hits

**Almost never right before GW7** — the Wildcard is close enough to absorb the
problem for free. After GW7 that subsidy is gone and the arithmetic flips. The
exception either side of that line is a **5+ game absence**, where a dead squad
slot compounds faster than the hit costs.

## Agile routes — pre-named exits

Each row is a named contingency so the decision is not invented under time pressure.
**None of these fire on form alone.** This list is not exhaustive — it covers what
was foreseeable on 21 Aug. New evidence can add rows or retire them; see *Amending
this plan*.

| If this happens | Then do this | Funded by |
|---|---|---|
| **Tzolis benched or subbed early in GW1-2** | He is the squad's only unverified role. Exit to a nailed £6.0-6.5m midfielder. First call **E.Anderson (MCI, £6.5m, 52 DefCon delivered, 37 starts)** — straight price swap, no downgrade needed. | Straight swap |
| **Obi still 0 minutes at the Wildcard** | Do not fix him with a free transfer. Fix him **on the Wildcard**, where the £1.0m upgrade to a playing forward (Barry EVE £5.5m / Georginio BHA £5.5m) is free. | Wildcard |
| **João Pedro's role changes under Alonso** | He was bought on effective ownership, not on pre-season output. If his ownership falls below ~40% the EO case that justified him has gone and the pick must be re-argued from scratch, not defended. | Re-derive |
| **Sunderland wall at GW4-5 bites** | Le Fée and Ballard swing together. Move **one**, not both — moving both converts a fixture problem into a squad-shape problem. Le Fée is the one to move; Ballard is bench cover and cheap. | 1 FT |
| **Everton wall at GW7-8** | Lands inside the Wildcard window. **Do not pay hits for it** — let the Wildcard solve Tarkowski and Ndiaye together. | Wildcard |
| **Haaland injured or rotated** | The single largest correlated exposure in the squad (69.4% owned, captain). There is no like-for-like at £15.5m. Do not chase — take the field's hit alongside everyone else and re-plan on the Wildcard. | — |
| **A set-piece taker changes anywhere in the 15** | Set-piece changes outrank statistical trends. Report unprompted and act same week. Squad currently has 3 penalty takers: B.Fernandes, Ndiaye, Haaland. Tzolis takes none. | 1 FT |
| **Any starter out 5+ games** | Transfer immediately, hit or not, on either side of GW7. | Hit if needed |

## Watchlist — entry conditions, not names to admire

| Player | Why | Entry condition |
|---|---|---|
| **E.Anderson (MCI, £6.5m)** | 52 DefCon delivered — joint-highest in the game; 37 starts | Confirm his deep role survived the move from Forest under Maresca. Two starts in the same role. |
| **Rice (ARS, £7.5m)** | 28 DefCon delivered, 35 starts, 18.3% owned | Only if a midfield slot opens; £1.0m more than Tzolis |
| **Mbeumo (MUN, £8.0m)** | 37.0% owned — largest remaining EO hole in the squad | If ownership climbs above ~45% the hole becomes a rank liability regardless of his output |
| **Szoboszlai (LIV, £7.0m)** | 41.7% owned, 36 starts, 20 DefCon delivered | Was sold in a prior session on a role-change read under Iraola. That read is **unverified against 2026/27 minutes** — recheck at GW3, do not re-enter before |
| **Calafiori (ARS, £5.5m)** | Most popular defender among last season's top-10k drafts by 10+ points | Fails the minutes rule at 22 starts. Enter only if he clears 5 consecutive starts |
| **Barry (EVE) / Georginio (BHA), £5.5m** | Playing forwards for the Obi slot | Wildcard only |

## Transferability — RULED 21 Aug 2026

**Demoted to a confidence discount.** Manager's ruling, taken at the GW1 deadline.
`doctrine.md` §8 is the record; read it there.

Short version: a player at a new-manager club is not banned. He needs independent
role confirmation — pre-season minutes, set-piece duty, or a predicted XI. Every
override still gets named in writing, so they can be counted at GW10.

Decay schedule and the GW10 falsification test are unchanged.

## What to check first, every gameweek

Run `skills/gameweek-review`. Its nine steps each have an output that must be stated
aloud. In this window, the three that matter most:

1. **Availability across all 15** — Tzolis and Obi are the two with no PL baseline.
2. **Set-piece diff** — three penalty takers is the squad's ceiling; losing one is
   a step-change no per-90 trend will surface for weeks.
3. **European load from GW5** — five of nine clubs are affected, and FDR is blind to it.
