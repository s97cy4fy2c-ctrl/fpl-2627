# GW10 review — 20 Nov 2026

Manager 50930. Objective top 100k. Rank after GW10: 147,450 [live].
Status: **RULED 20 Nov 2026, 12:48 GMT.** The manager accepted all 18 recommendations in section 4, including the review's D9 wording over the challenger's. GW11 itself is OPEN (section 5).

Method: one live pull (Composio sandbox, 20 Nov). Two blind auditors, then a blind doctrine challenger. Each saw the evidence, not the session's reasoning. Working files: `audit1.md`, `audit2.md`, `challenge.md`.

---

## 1. Verdicts

| Test (where it was set) | Result | Verdict |
|---|---|---|
| Frozen GW1 XI v actual (doctrine s6) | Frozen 559-577, actual 692 (683 without the TC) [live] | **Transfers earned.** "Fewer transfers" does not fire |
| Template XI (doctrine s6) | 615 under a proposed rule [live, A1] | Actual +77. The rule flatters the template |
| Transferability thesis (s8) | Prior-to-current Spearman: new-manager clubs 0.33 v 0.44; 90% CI of the gap [-0.39, +0.18]. Top quartile: 0.75 v 0.63 [live] | **Not supported. Retire it** |
| Overrides honestly counted (s8) | 4 named; 4 of 4 buys at new-manager clubs overridden; 0 of 37 rejections cite it [A2] | Honest bookkeeping. The rule never bit |
| Look-vs-act gate (s2) | Mostly honest. Retrofitted twice: GW5 Calvert-Lewin, and the GW11 draft [A2] | **Leaks under pressure.** Needs an instrument (N1) |
| Caught-by ratio (ledger) | Self 3/10 → 10/26 [sheet + n=27-29] | Turned on paper. **Every costly error was still caught by you** |
| Plan amendments (plan) | 8 earned, 8 not, 1 unknown [A2] | **Fudged.** External causes honoured; judgment calls mislabelled or silent |
| GW7 pipeline (first outing) | Wildcard 15 out-scored the old 15 by +91 over GW7-10 [live, A1] | Build B, close-out D. Nothing it raised was ruled or committed |

## 2. What earned and what didn't [live, A1]

- **Transfers, 4-GW window:** role-change +28 (Groß). Fixture +21 (2 moves). Injury-forced +22 (3 moves; +5 counting only the weeks held). GW9 JP → Jackson +20 (unlogged). No transfer lost over its window. No hits.
- **Rejections by reason type:** hard rule 1-3 (all three losses were the BHA GK+DEF bar). Constraint claims 0-2. EO judgments 3-0. Sequencing / FT value 7-0.
- **Overrides:** Kadıoğlu ×3 +15 (xGC favoured him each time; the review was wrong). Armband GW4 −4. Calvert-Lewin GW5 −8 (the review caved under pushback). Belloumi over Tavernier GW7 −15. Net −4.
- **Captaincy:** Haaland 9/10 and most-captained 10/10. The armband was rarely the gap.
- **Churn:** Mbeumo sold on the Wildcard, bought back next week. One FT spent undoing it.

## 3. Process failures found

| n | What | Caught by |
|---|---|---|
| 27 | GW10 deadline missed. The calendar date was wrong; live was Fri 6 Nov 18:30 UTC | Manager |
| 28 | GW19 expiry wrong in five places (doctrine s4; plan ×3; ledger). Live: **Fri 1 Jan 2027 18:30 UTC** | Self |
| 29 | GW11 review amended `plan_gw1_gw10.md` after its sunset. It cited the expired s8 rule as a sell reason | Manager |
| 30 | No ledger ruling for GW9 or GW10. GW9 JP → Jackson unrecorded | Auditor |
| 31 | GW11 draft sold Mbeumo on a window split (0.84 → 0.50 → 0.36) driven by one GW2 match (1.97 xGI). GW3-10 is flat at 0.41 | Auditor (verified [live]) |
| 32 | The GW11 datapack fed "0.77 at GW6" to the blind builder. Its "0.26 over GW7-10" was wrong (true 0.44). Blindness breached again (n=23 family) | Self |

Record gaps: three transfers missing from `decision_log`. Benchmarks tab stops at GW4. Five promised GW5 rejection rows never written. 19 of 25 due rejection rows ungraded. Watchlist last checked 7 Sep. Pipeline code never committed. Ledger caught-by arithmetic off by one since n=15.

## 4. Rulings — all RULED as recommended, 20 Nov 2026

Challenger's verdict first; the review's where it differs. Code changes pending: collisions.py class A to warn; an N1 script; a weekly `*_order` snapshot.

| # | Rule | Recommend | Wording (short form) |
|---|---|---|---|
| R1 | **Dates** | ADOPT | Dates are data. Read `events[].deadline_time` live each session. No doc types a date. Fix s4 now |
| R2 | **N1 volume trend** (new) | ADOPT | Fixed window: last 6 starts v earlier. Drop the largest match and recompute; if the change halves, no trend. Minutes first |
| R3 | **D3 cause gate** | AMEND | Causes: this player's role, his set pieces, or a trend that passes N1. Team xG is not a cause. A manager change is not a cause |
| R4 | **D10 / s8 transferability** | DROP | Retired 20 Nov. Only a visible role change counts |
| R5 | **D13 GK+DEF bar** | AMEND to scorecard axis | 0-3 when it fired. Start the pair when each beats his alternative on fixture-adjusted xGC. Script warns |
| R6 | **D9 chips** | AMEND — **differs** | Challenger: Bench Boost in the first qualifying GW. **Mine:** target GW14 (best bench fixtures); fire if all four bench are status a and started both previous games; GW16+ fallback. Free Hit: GW15 candidate, decided at the GW14 review. Plan both now |
| R7 | **D11 collisions** | AMEND | Class A is a hedge, not a dead slot (a 0-0 pays both). Warn, don't fail |
| R8 | **D7 projections** | AMEND | A model may screen. Its numbers never enter a scorecard, decision line or captaincy call |
| R9 | **D1 differentials** | AMEND | xGI >= 0.34 measured by N1 |
| R10 | **Recording** | ADOPT | No transfer, chip or armband change without a ledger line before the deadline |
| R11 | **Amendment grounds** | ADOPT | Closed list: availability, role, set piece, real club transfer, live fixture-grid change. Anything else logged as "judgment" |
| R12 | **Community provenance** | ADOPT | A ruling that cites a [community] point is a process error |
| R13 | **Armband lock** (open since 17 Sep) | ADOPT | Change needs a named cause written before the deadline |
| R14 | **Template XI** | ADOPT A1's rule | 11 most-owned at that round, legal formation, most-captained as captain. Score from GW11 |
| R15 | D2, D4, D5, D6, D8, FT-banking bar | KEEP | D5 needs weekly `*_order` snapshots in code |
| R16 | D12, D14, D15 | KEEP, re-test GW19 | Tests named in `challenge.md` |
| R17 | Plan file | CLOSE `plan_gw1_gw10.md`; open `docs/plan_rolling.md` | Stops n=29 recurring |
| R18 | Project prompt | You edit it | Points at archived files. Point it at `operating.md` + `doctrine.md` |

## 5. Does it change GW11? Yes.

**Revised pick: Hold. Bank to 3 FTs. Bench Mbeumo for Liverpool away.** Supersedes the earlier "Mbeumo → McGinn". **OPEN:** the manager is not yet sure. The alternative, Mbeumo → McGinn, is a legal fixture-chasing move under the new rules. Flip trigger: official Villa team news confirming McGinn starts centrally with Manzambi out.

- The sell case had three legs. N1 kills the volume leg: change −0.03 once GW2 is dropped [live]. R3/R4 kill the manager leg. Only the fixture remains (LIV away).
- A fixture is a lineup reason this week, not a transfer reason. Bench him.
- McGinn passes N1 (+0.26) but fails its first line: minutes per start fell from 87 to 66 (45, 65, 86, 70) [live]. Role first. Re-test after GW11.
- FT-sequencing calls went 7-0 [A1]. With a Bench Boost bench to build by GW14, the third FT has a use.
- Case against: AVL's run (2,2,3,2) beats MUN's (4,3,3,2) [live]. McGinn's per-match xGI GW3-10 is 0.49 v Mbeumo's 0.40. If McGinn starts 90 in GW11, this costs a few points. 55/45 for Hold.

**XI (4-3-3):** Trafford; De Cuyper, Van Hecke, Silva, Calafiori; Groß, Rogers, Rudoni; Haaland (C), N.Jackson (VC), Barry.
**Bench:** Leno; 1 Mbeumo, 2 Hall, 3 Belloumi.
- Calafiori at NEW: Arsenal concede 0.5 GA/g; 3 clean sheets in his last 4 starts [live].
- Mbeumo at LIV: Liverpool concede 1.0 GA/g [live]. The bench call rests on the fixture alone (R12).
- `check_squad.py` and `collisions.py` exit 0. One XI class B (Rogers v Trafford), accepted.
- Captaincy unchanged: Haaland 78.8% owned [live]; shield, not bet.

## 6. Rolling plan, GW11-14 (committed as `docs/plan_rolling.md`)

- **GW11: OPEN.** Review pick Hold, 3 FTs to GW12.
- **GW12:** Re-run N1 and role checks on Mbeumo (Pochettino's first XI) and McGinn (minutes). Belloumi out if not fit. Start building the Bench Boost bench.
- **GW13 (midweek, 1-3 Dec):** Bench must be four players with status a who started GW12 and GW13.
- **GW14: Bench Boost target.** 8 of 15 at FDR 2 [live].
- **GW15: Free Hit candidate.** Worst XI week in the window (FDR sum 37 [live]). Decide at the GW14 review.
- **Rogers:** passes the hold under N1 for now. Re-test before CHE's LIV (H) GW14 and MCI (a) GW15.
- **Chip expiry:** the GW19 deadline, read live from `events[].deadline_time` (R1).
