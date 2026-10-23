# ledger.md

The record. **Append-only** — entries are never rewritten, only superseded with a
dated note. Structured data lives in the spreadsheet (`config.json` has the ID);
this file holds what needs prose.

---

## Squad

**GW1 2026/27 — COMMITTED 21 Aug 2026, before the 18:30 BST deadline.**
All values `[live]` from bootstrap-static, fetched 21 Aug 2026.

Formation 3-5-2. Cost £100.0m, ITB £0.0m. Captain Haaland, vice B.Fernandes.
No chip played.

| Slot | Player | Club | Pos | Price | Own | 25/26 pts | Starts | DefCon delivered |
|---|---|---|---|---|---|---|---|---|
| XI | Verbruggen | BHA | GKP | £4.5 | 21.6% | 130 | 38 | — |
| XI | Gabriel | ARS | DEF | £8.0 | 29.7% | 209 | 30 | +22 |
| XI | Shaw | MUN | DEF | £4.5 | 21.5% | 113 | 38 | +10 |
| XI | Tarkowski | EVE | DEF | £6.0 | 8.8% | 170 | 37 | +44 |
| XI | B.Fernandes (vc) | MUN | MID | £12.0 | 51.6% | 235 | 35 | +10 · PEN |
| XI | Ndiaye | EVE | MID | £6.0 | 16.1% | 128 | 32 | +12 · PEN |
| XI | E.Le Fée | SUN | MID | £6.0 | 10.7% | 147 | 33 | +16 |
| XI | Tzolis | ARS | MID | £6.5 | 23.7% | 0 | 0 | — |
| XI | Ampadu | LEE | MID | £5.5 | 1.5% | 134 | 35 | +38 |
| XI | Haaland (C) | MCI | FWD | £15.5 | 69.4% | 239 | 34 | — · PEN |
| XI | João Pedro | CHE | FWD | £7.5 | 64.1% | 177 | 31 | — |
| B1 | Ballard | SUN | DEF | £5.0 | 5.5% | 116 | 24 | +30 |
| B2 | F.Kadıoğlu | BHA | DEF | £4.5 | 3.0% | 118 | 34 | +4 |
| B3 | Obi | MUN | FWD | £4.5 | 1.1% | 0 | 0 | — |
| B4 | Dubravka | TOT | GKP | £4.0 | 20.2% | 96 | 35 | — |

**Whole-squad scorecard.** Raw-ownership sum (XI) 319 · DefCon delivered (XI) +152 ·
penalty takers 3 · correlated GK+DEF units in XI NONE · midweek European load 5 of
9 clubs (MCI MUN ARS SUN BHA) · bench outfield starts 58 · transferable starters
9/11 under the pre-21-Aug thesis.

**Two deliberate rule overrides, both logged.**

1. **Haaland and João Pedro forced past the transferability thesis.** Both are at
   new-manager clubs, so the thesis as written excluded them. Overridden on
   effective-ownership grounds: at 69.4% and 64.1% they are the two most-owned
   players in the game and both are ceiling assets. Doctrine §1 says EO risk
   scales with variance, so missing either concentrates rank risk far more than
   the thesis saves. See the thesis review below.
2. **Tzolis started despite failing the minutes rule (0 PL starts).** The rule
   proxies minutes certainty through Premier League history; Tzolis is an
   overseas signing with none, which is a proxy failure, not a rotation risk.
   Direct evidence overrode it: he is in the predicted Arsenal 4-3-3 as left
   winger `[live, 21 Aug]`. He takes no set pieces, so his ceiling is open play only.

**Frozen XI benchmark.** The eleven above are the control series for the
`benchmarks` tab. Never transferred, never re-picked. If frozen beats actual at
GW10, the finding is *fewer transfers, not better ones*, and the GW10 review must
say so plainly.

---

## Process errors

Full structured record: `process_errors` tab. **Ten entries logged to 21 Aug 2026.**

**Corrected 24 Aug 2026.** This section previously read "Eight logged" and carried
aggregate tables built on that count. Both were wrong. Recounted directly from the
`process_errors` tab, not from recall.

**Known defect in the tab: `n` runs 1-7, 9, 10, 11. There is no row 8.** Ten rows
exist; the highest index is 11. The gap is left in place deliberately - renumbering
an append-only log destroys the references that point at it. Do not "fix" it by
resequencing. Either row 8 was never written or it was deleted, and which of those
is true is not currently known.

The aggregate, which prose could never have produced:

| Family | Count |
|---|---|
| fast-field (club assignment, availability, transfers, calendar) | 5 |
| metric-misuse | 2 |
| process | 2 |
| role-change | 1 |

| Rule was already written in | Count |
|---|---|
| `analysis.md` (archived) | 3 |
| `data.md` (archived) | 3 |
| `operating.md` / `doctrine.md` / `README.md` (live set) | 3 |
| nowhere - a genuine gap | 1 |

| Caught by | Count |
|---|---|
| manager | 6 |
| self | 3 |
| Reddit sweep | 1 |

**Nine of ten violated a rule that already existed.** Only entry 3 had no rule behind
it. The files were never the problem. That finding drove the entire redesign:
mechanical rules moved into `check_squad.py` where they exit non-zero, and the weekly
loop moved into a skill where each step has an output that must be stated.

**The uncomfortable column is "caught by".** Manager 6, self 3, Reddit 1. The
self-caught share is better than the previously recorded "self 1" - entries 9 and 10
were both self-caught on 21 Aug and were never reflected in this file. If that ratio
has not shifted further by GW10, the redesign did not work and the GW10 review must
say so.

**Shipped 25 Aug 2026.** The redesign this section describes is now committed. `gameweek-review` became a squad-as-unit weekly loop with a proactive unowned-pool and trend scan and a forward-plan consult/update step (commit `b61177c`); `doctrine.md`, `operating.md`, `plan_gw1_gw10.md` and `squad-build` were condensed with rationale demoted to Why blocks (commit `402cd44`). doctrine §2 also gained the look-vs-act rule — see Open items. All five files were server-verified byte-exact against the reviewed checksums. Whether it worked is the GW10 caught-by ratio, not this note.

**Updated 25 Aug 2026.** Entry 12 logged to the tab — a process error from this session, self-caught: two structural decisions were mis-filed into the `decision_log` tab and moved to this file. Count is now eleven; the aggregates above are as of 21 Aug and exclude it. Deltas: family process 2→3, caught-by self 3→4, rule-lived-in live-set (now incl. `ledger.md`) 3→4. Self-caught share moves 3/10 → 4/11.

**Updated 3 Sep 2026.** Entry n=13 logged — twelve rows now, highest index 13. A GW3 pre-deadline staleness miss: the review ran on the session-open bootstrap fetch and missed Ndiaye's deadline-day Everton→Man City transfer; caught by manager. Deltas from the 21 Aug aggregate: family fast-field 5→6, caught-by manager 6→7. Self-caught share moves 4/11 → 4/12 — the wrong direction; if the ratio has not improved by GW10 the redesign did not work and the GW10 review says so. Fix: gameweek-review step 2 hardened to verify current club for all 15 on deadline day (committed 3 Sep 2026).

**Updated 3 Sep 2026 (2).** Entry n=14 logged — thirteen rows now, highest index 14. Ran the GW3 review from the stale mounted skill snapshot (`/mnt/skills`, 9-step) instead of the repo version (10-step, commit b61177c), and so skipped the cold-trend surface (step 2), the proactive pool scan (step 5), and the forward-plan update (step 10). Consequence: Shaw's cold trend went unflagged and Le Fée's was surfaced by the manager, not proactively; the forward plan was left stale on four Ndiaye lines. No decision changed — the skipped steps were re-run and none cleared the bar. Caught by manager. Deltas: family process 3→4; caught-by manager 7→8; self-caught share 4/12 → 4/13 — again the wrong direction. Fix: operating.md now requires reading loop skills from the repo, not the mount; plan_gw1_gw10.md amended by dated append.

---

## Decision log

Structured record: `decision_log` tab. Empty until GW1 resolves — deliberately.
Seeding it with retro-fitted rationales would poison the first category review.

One row per transfer: gameweek, in, out, cost, category, rationale, rejected
alternative, then points for both over the following four gameweeks, delta, verdict.
Categories are the four from the post-mortem doctrine — fixture-chasing,
form-chasing, price-chasing, gut-differential — plus injury-forced and role-change,
which the season will produce whether planned for or not.

**Corrected 25 Aug 2026.** The `decision_log` tab is transfer decisions only — its point-delta columns and category vocabulary assume an in/out pair — so structural, doctrine and process decisions are recorded in this file's prose, not the tab. Two such rows were briefly appended on 25 Aug and removed the same day (`process_errors` n=12). 'Empty until GW1 resolves' above refers to *transfer* rows; the tab also carries the GW1 `initial-build` seed as the squad baseline.

---

## Benchmarks

Structured record: `benchmarks` tab. Populated from
`https://fantasy.premierleague.com/api/entry/50930/history/`, which is reachable
from the Composio sandbox — so this fills itself rather than being typed in.

Three series: actual, frozen GW1 XI, template XI. The frozen XI is the control. If it
beats actual at GW10, the fix is fewer transfers, not better ones.

---

## Open items

| Item | Status |
|---|---|
| LiveFPL effective ownership | UNRESOLVED. ZenRows gets 422 even with premium proxy. Retry post-deadline when EO data exists. Screenshots remain the fallback |
| `squad-build` skill | BUILT and committed 21 Aug 2026 at `skills/squad-build/`. Was previously installed locally but absent from the repo, so MANIFEST never served it |
| Pipeline in repo | CLOSED 21 Aug 2026. No `pipeline/` directory exists; README no longer claims one. Mechanical rules live in `skills/*/scripts/` |
| Transferability thesis | **CLOSED as an open item 21 Aug 2026 — RULED, not pending.** Demoted from hard exclusion to a confidence discount by manager ruling at the GW1 deadline. `doctrine.md` §8 is the record. This row previously read "Awaiting manager confirmation", which contradicted doctrine; corrected 24 Aug 2026. The GW10 falsification test remains open and is tracked in `plan_gw1_gw10.md`, not here |
| Look-vs-act rule | RULED 25 Aug 2026, committed to `doctrine.md` §2. Form is a trigger to look, never a reason to act; act only on a named cause — role, set-piece, or volume over ~6 starts. Pre-GW6 only role and set-piece are actionable. Falsifiable at GW10 alongside the transferability thesis; grade whether the cause-gate was applied honestly. |


---

## Gameweek rulings

Non-transfer weekly decisions — Hold, captaincy, XI shape, bench order. The
`decision_log` tab is transfer rows only; recording a Hold there would poison the
GW10 category review, so these live here as dated prose. Append-only.

### GW2 — RULED 25 Aug 2026. Deadline Thu 28 Aug, 18:30 BST.

**Hold. 0 transfers. Bank the FT.** Captain Haaland, vice B.Fernandes.

XI unchanged, 3-5-2 [live 25 Aug]: Verbruggen; Gabriel, Shaw, Tarkowski; B.Fernandes,
Ndiaye, Tzolis, E.Le Fee, Ampadu; Haaland (C), Joao Pedro.
Bench order: 1 Ballard, 2 Kadioglu, 3 Obi. Reserve GK Dubravka.

**Why hold.** No role, set-piece, or availability change in the XI [live]. One GW is
not a sample; before ~6 starts only role and set-piece override [repo, doctrine 2].
A banked FT is worth ~one future move; no GW2 upgrade beats it. The wildcard window
(GW6-9) is the free fix; hits are almost never right before GW7 [repo].

**XI assessed as a shape, not inherited.** Two forwards are the only startable
attackers (Obi 0 mins), so any legal shape is X-Y-2 [live]. 3-5-2 ranked above 4-4-2:
starting Ballard for Ampadu is a floor wash — Ballard's GW1 DefCon (9) missed the DEF
threshold (10) while Ampadu's (13) cleared MID — and breaks a balanced shape for
nothing. No correlated GK+DEF unit in the XI. Everton appears twice (Tarkowski clean
sheet, Ndiaye attack) through different point sources, so it is not one bet.

**Rejected transfer.** Reactive Shaw->De Cuyper (De Cuyper 17 pts GW1): form off one
game; would create a BHA GK+DEF correlation with Verbruggen; De Cuyper GW2 is CHE(A)4
vs Shaw IPS(H)2. Loses on every moved axis.

**Captaincy in EO terms.** Haaland ~68.7% owned, most-captained in GW1 [live].
Captaining the ~69% ceiling asset is the defensive play; the risk is in not holding
the armband there [repo, doctrine 1]. CRY(A) fdr3 — not a TC spot. TC target stays
GW3 COV(H)2 if Haaland starts and completes GW2.

**Logged, not acted.** MUN 0-2 at Hull [live] dents the "United easy opening pair"
FDR inference behind three United picks. One GW, no role change -> not grounds [repo].
Re-tested at GW10.

**Forward intent: unchanged.** The Tzolis->E.Anderson exit did not fire — Tzolis
started and returned; its window closes after GW2. Obi stays a wildcard fix. Kadioglu
doubtful (75%, UECL 2nd leg 27 Aug) is bench cover; injury protocol = no action, and
if he is ruled out nothing changes (already behind Ballard, Obi last).


### GW3 — RULED 3 Sep 2026. Deadline Fri 4 Sep, 18:30 BST.

**1 transfer: Ndiaye OUT -> Groß IN. Bank 2nd FT (1 used, 1 banked). Chip: TRIPLE CAPTAIN on Haaland.** Captain Haaland (TC x3), vice B.Fernandes. XI unchanged 3-5-2. Bench: 1 Ballard, 2 Kadıoğlu, 3 Obi; reserve GK Dubravka.

**Why the transfer.** Ndiaye transferred Everton->Man City on the deadline-day window (closed 1 Sep) [live]. A transfer is a hard amendment ground — act immediately [repo, doctrine 2]. His Everton record now describes a club he left; role at City unverified (rotation + UCL midweek load from GW5); and he ceased to be a penalty taker (Everton pen1 -> City pen None), which alone drops the squad from 3 pen takers to 2.

**Why Groß over Sangaré.** The replacement brief is Ndiaye's profile — attacking mid on penalties — not a DefCon floor. Ampadu already carries the mid floor (+38 delivered), so a second pure-floor mid (Sangaré, DefCon delivered 2/2) is redundant. Groß is Brighton's penalty taker, order 1 [live] — a set-piece role, which outranks statistical trends and needs no six-start sample — restoring the third pen taker (Bruno, Haaland, Groß). Bought the durable pen role, NOT the 13-point two-game haul (form spike, ignored [repo, doctrine 2]). Cost: Brighton 2->3 in the 15 (2 in XI — Verbruggen off clean sheets, Groß off attack, different point sources, not one bet; Verbruggen+Groß is GK+MID, not the banned GK+DEF pair). Brighton UECL playoff done 20/27 Aug; league phase ~Oct, inside/after the WC window; Groß nailed 90/90 [live]. Ndiaye £6.0 -> Groß £5.5, +£0.5 ITB.

**Rejected.** Sangaré (BRE, DefCon delivered 2/2, zero correlation) — redundant floor vs Ampadu, runs only 2 pen takers. Stach (LEE) — 2nd Leeds. Hold-and-bench Ndiaye — carries an unverified City starter in the XI and reintroduces the Ballard-for-mid floor wash.

**Triple Captain — FIRED.** Haaland: home fixture rated 2 (COV), started and completed the previous two (90'/90'), fit, no UCL load before GW5 [live, repo]. Earliest clean TC spot per the plan; GW5+ carries midweek load. Rejected holding the chip for a speculative later double — none is visible in the live grid [live].

**Holds.** Tzolis — two early subs (75', 45') but still starting; no confirmed role change, not actionable pre-GW6. Hold with a GW3 trip-wire: a third early sub or a benching = act; the wildcard (GW6-9) resolves it. Le Fée — output poor (5 pts, form 2.5) but nailed (79'/89'), set-piece role intact (primary corners), xGI rising 0.03->0.54; form is a trigger to look, not a cause to act [repo, doctrine 2]. His trigger is the GW4-5 Sunderland wall (ARS H4, MCI A5); pre-named exit there on the banked FT. Hold GW3 (BRE away, fdr3), move GW4.

**Process error n=13.** This GW3 review was built on the session-open bootstrap fetch and missed Ndiaye's deadline-day move; caught by manager. Caught-by ratio -> manager 7 / self 4. Fix committed this session: gameweek-review step 2 now verifies current club for all 15 on deadline day. See process_errors n=13.

### Plan amendment — 3 Sep 2026

Recorded in prose, not the `decision_log` tab (transfer rows only, per n=12). `plan_gw1_gw10.md` amended by dated append: Ndiaye's EVE→MCI transfer supersedes four 21-Aug lines (European load, GW7-8 Everton pressure point, Everton-wall route, set-piece takers). Set-piece takers now B.Fernandes, Haaland, Groß; Everton exposure is Tarkowski only; Groß (BHA) carries UECL load ~Oct. Originals preserved. The plan's "How" step still says to log amendments in `decision_log`, which conflicts with the n=12 discipline — flagged in the plan append for GW10 reconciliation.


### 7 Sep 2026 - structural rulings (post-GW3, pre-GW4)

Manager rulings, recorded in prose per the n=12 tab discipline. Not `decision_log` rows.

**1. Wider-context sweep - RULED.** The weekly loop takes no input from forums, blogs
or expert sites. `plan_gw1_gw10.md` lists community noise under *Not grounds*, and
`operating.md` flags the token cost of one Reddit search. That removed an entire input
class because a single early sweep was low-signal. The sweep returns as **step 5b**,
under a new provenance tag **`[community, date]`**: a hypothesis to test, never
evidence, barred from any scorecard, decision-log line or plan amendment until
confirmed independently against live data. Committed to `operating.md` and the skill.

**2. Own-club collisions - RULED.** Doctrine s9. The grade turns on point source, not
position: two clean-sheet assets opposed is class A (mutually exclusive); our attacker
against our own clean-sheet asset is class B (an internal hedge); attacker against
attacker is class C and benign, and better in a free-scoring fixture. DefCon never
collides. Class B is graded on live GF/GA rates, marked `B!` when both sides clear the
league median. Mechanical part in `skills/gameweek-review/scripts/collisions.py`,
exits non-zero on 2+ class-A in the XI. Collisions are a scorecard axis and are scored
across the next ~4 GWs on any transfer, not just the upcoming one.

Live at ruling `[live, 7 Sep]`: we hold 9 of 20 clubs, so collisions occur in every
gameweek GW4-GW10. GW4 has 0 class A and 2 class B in the XI (Haaland/Shaw is `B!`).
**GW5 has a class A in the XI (Verbruggen/Gabriel). GW8 has Gabriel/Tarkowski - our two
largest DefCon assets, mutually exclusive, inside the wildcard window.**

**3. Chips as a stopping rule - RULED.** Doctrine s4 rewritten. Verified `[live, 7 Sep]`:
every gameweek GW4-GW19 is a full ten-fixture round and the season fixture list has
zero unassigned fixtures, so **no blank exists before the first set expires on 2 Jan
2027**. The old Free Hit rule ("a blank gameweek. Nothing else") therefore guaranteed
the chip expired unused. A chip with a hard expiry and no blank in its window has no
option value. Fixture-targeting is now the Free Hit's primary use; a blank remains
valid but is no longer the only trigger; backstop ~GW15. Bench Boost is currently
unplayable (Obi and Dubravka on 0 minutes) and must be either made reachable on the
Wildcard or written off deliberately. Falsifiable: if a blank emerges before GW19 the
finding was wrong and the next review says so.

**4. Name resolution - BUILT.** `resolve_names.py`. Variants derived from the live
roster; nicknames only in `config.json["player_aliases"]`, sourced and dated. Tag
before summarising, check after; an unresolved name is dropped, not reported.

### Process errors - updated 7 Sep 2026

Entry **n=15** logged: argued against a GW4 Free Hit on the false ground that it would
mean not owning Haaland. A Free Hit imposes no such constraint. The alternative had
been unbanned in the same session precisely for having been defeated by assertion, and
was then defeated by assertion again. Family metric-misuse 2->3; caught-by manager
8->9. Self-caught share 4/14 -> **4/15**, the wrong direction for the third consecutive
entry. If that ratio has not turned by GW10 the redesign did not work and the GW10
review says so plainly.

Standing gap, not yet fixed: `check_squad.py` and `collisions.py` validate the option
we propose. Nothing validates the reasons we reject the ones we don't. n=15 lived
there.

### GW4 - OPEN, not ruled (as of 7 Sep 2026)

Deadline Sat 12 Sep, 13:30 BST. Manager is reviewing again closer to the deadline;
this entry records the state, not a decision.

Current lean: **Hold, 2 FTs banked, captain Haaland, vice moved B.Fernandes ->
Joao Pedro.** Called at ~55/45 over a GW4 Free Hit after the n=15 correction, on three
grounds: the XI already holds four of the six fixtures rated 2; a Free Hit fixes
nothing structural; and GW5 and GW8 are more compromised weeks. Pre-stated tie-breaker:
**if Thursday or Friday team news puts 2+ of the XI in doubt after the international
break, the Free Hit becomes the pick.**

Chip sequence beyond GW4 is 50/50 between "Free Hit GW5, Wildcard GW6" and "Wildcard
GW6, Free Hit later", to be settled with GW4 results in hand. Prior lean of 60/40 for
the latter rested partly on the n=15 error and has been withdrawn.


### 7 Sep 2026 (2) - validating rejections - RULED

The gap: every check we owned validated the option being chosen. Nothing held the
reasons for discarding the others to the same standard. Four cases, one shape - an
option removed by a claim that never faced the evidence bar the supporting claims face:
the blanket Free Hit ban (asserted, never argued); "a Free Hit means not owning
Haaland" (n=15, a constraint that does not exist); the Szoboszlai sale (a role read
tagged nowhere and never re-verified until its own trigger forced it, and wrong); and
Hull's defence, excluded silently by the promoted-club rule with no record of the cost.

Three fixes, adopted together. A fourth was considered and declined.

**A. Provenance is symmetric.** `operating.md`. A claim that REMOVES an option carries a
tag like any other, and a claim that an option is impossible, illegal, unaffordable or
constrained must be **[live]-verified before it is used to reject**. Near-zero cost,
and it covers the factual subclass where three of the four cases sat.

**B. Steelman gate, scoped.** Skill step 10b. On chip and wildcard decisions only, state
the strongest case FOR the top-ranked rejected option and what would have to be true for
it to win. Scoped deliberately: applied to every rejected transfer it becomes ceremony,
and ceremony gets skipped. This is the one that would have caught the Free Hit ban.

**C. `rejections` tab.** One row per rejected option: reason, reason_type, provenance,
would_win_if, graded_at, verdict. Graded at GW10 and GW19 **by reason_type** alongside
the decision log by category (`doctrine.md` s6). Prevention is not the point -
countability is, and that is what turned `process_errors` from a list into the thing
that drove the redesign.

Seeded with fourteen rejections that were **recorded in writing at the time**, from
`decision_log`, `ledger.md` and the watchlist - not reconstructed, which would repeat the
error the empty decision_log was protecting against. Three already read badly and are
marked as such rather than left flattering: Shaw->De Cuyper (21 pts to 7), Sangare over
Ampadu (2/3 delivered to 1/3), and Szoboszlai (wrong, confirmed).

**D. Mechanical feasibility checker - DECLINED for now.** A script confirming a rejected
option really is infeasible when we claim infeasibility would catch n=15 exactly, but
most rejections are not feasibility claims. Over-engineering off a single instance.
Revisit if a second feasibility error appears.

**Stated limit.** None of these reliably catches a subtly wrong judgment. Had n=15 read
"the Free Hit's fixture gain is too small to justify the chip" - a claim, tagged,
verifiable in form - and simply been wrong about the magnitude, all three fixes pass it
through. The aim is to make the factual subclass mechanical and the judgment subclass
countable at GW10. The rest still depends on the manager reading carefully, which is
what caught n=15.

### GW4 - RULED at the deadline (12 Sep), recorded 17 Sep 2026

Recorded after GW4 finished, on manager instruction. The ruling was not committed at the
deadline, and the post-mortem nearly graded the wrong decision because of it (n=17).

**Transfers - 2 FTs, no hit, no chip.** B.Fernandes (sold 12.0) -> Palmer (9.7). E.Le Fée
(sold 5.8) -> Rogers (7.6). Both made ~00:10 UTC 12 Sep [live]. ITB 1.0 after. The manager
raised the pair on a value argument. The review endorsed it on fixtures and structure, not
value. `decision_log` carries both rows.

**Recommended at the deadline** [12 Sep review, held twice]. Captain Haaland, vice João Pedro.
XI 3-5-2: Verbruggen; Gabriel, Ballard, Tarkowski; Palmer, Rogers, Groß, Tzolis, Ampadu;
Haaland, João Pedro. Bench: 1 Kadıoğlu, 2 Shaw, 3 Obi. Shaw benched on a 75% flag -
`check_squad.py` exits 1 with him in the XI.

**Fielded** [live]. The same XI with **Kadıoğlu for Ballard**. Captain **Palmer**, vice
Haaland. Bench: 1 Ballard, 2 Shaw, 3 Obi. Reserve GK Dubravka.

**Two manager overrides. Neither was written down before the deadline.**

1. **Kadıoğlu over Ballard.** It puts the Brighton GK+DEF pair (Verbruggen + Kadıoğlu) in
   the XI, which the squad rules bar [repo]. Result: Kadıoğlu 6, Ballard 0 (conceded 2,
   yellow). BHA won 5-0 at COV, so the correlated bet paid both legs.
2. **Armband: Haaland -> João Pedro -> Palmer.** The manager pushed for Palmer. The review
   held Haaland twice. The manager moved it to João Pedro, then to Palmer at the last
   minute. No new information existed: Chelsea kicked off 90 minutes after the deadline
   [live]. Result: Palmer 5, Haaland 9, João Pedro 12.

**Result** [live]. 97 points against an average of 69. GW rank 349,614. Overall rank
1,885,177 -> 702,711. Bench 0.

| Team | Captain | DEF | GW4 |
|---|---|---|---|
| Recommended | Haaland | Ballard | 95 |
| Manager's first override | João Pedro | Kadıoğlu | 104 |
| Fielded | Palmer | Kadıoğlu | 97 |

Manager overrides net +2 against the recommendation: Kadıoğlu +6, armband -4. The final
switch cost 7 against the João Pedro armband.

**Post-mortem - process v variance** (doctrine s6).

- **Transfers: process sound, outcome ahead, verdict at GW7.** 13 v 2 in GW4. Palmer v Bruno
  is level on underlying (0.38 v 0.36 xGI), so +3 is noise. Rogers v Le Fée is 0.23 v 1.44
  xGI, and Le Fée missed a penalty (-2). The +8 is mostly finishing variance.
- **Armband: bad process, bad outcome.** The review's call held on underlying inside the
  match: Haaland 0.88 xGI, Palmer 0.38, João Pedro 0.33 [live]. Two changes, no new cause.
  The João Pedro armband would have gained 3, and that would have been variance too. The
  error is the unrecorded override, not the 4 points.
- **Kadıoğlu: the review's rejection was the weaker read.** It adjusted Brighton's defence
  (5.71 xGC in 3) but not Coventry's attack: 0 goals from 2.88 xG in GW1-3 [live]. Ballard
  faced Arsenal (4.98 xG). Doctrine s2 says fixture-adjust before comparing. Graded WRONG in
  `rejections`. The override still broke a written rule and was not recorded. One clean
  sheet does not make the pair safe.
- **Groß for Ndiaye (GW3): +16 in GW4** (17 v 1). Top scorer of the week [live]. Bought for
  the pen role, not form.

**Frozen XI.** 68 in GW4, 265 in total. Actual 301, so +36 [live]. GW3 +7: TC +9, Groß v
Ndiaye -2. GW4 +29: Groß +16, Rogers +8, Kadıoğlu v Shaw +6, Palmer v Bruno +3, armband -4.
`benchmarks` rows GW3 and GW4 written 17 Sep. The template XI still has no construction rule.

**Set pieces.** No change in the 15. Pen takers are now Haaland, Groß, Palmer - still three
[live]. DefCon delivered in GW4: Gabriel +2, Ampadu +2.

**Rejected** (`rejections` tab): Hold, S2 Palmer-only, S3 Palmer + Barry (excluded by the
argued Barry fence, not outscored; Barry 2 in GW4), Free Hit GW4, Palmer (C), Kadıoğlu start.
João Pedro (C) was not recorded as a rejection at the time, so it is not seeded.

**Forward intent.** See the 17 Sep append in `plan_gw1_gw10.md`.

**Supersedes** the "GW4 - OPEN, not ruled (as of 7 Sep 2026)" entry above.

### Process errors - updated 17 Sep 2026

**n=16, self-caught (11 Sep).** The watchlist `Palmer` row carried Alex Palmer's (IPS GK)
price and ownership. The `notes` column is shifted against the other columns on at least
five rows. New family label: name-resolution. Palmer row corrected and closed 17 Sep. The
notes shift is NOT repaired - which note belongs to which row is unknown. Open item.

**n=17, caught by manager (17 Sep).** In the post-GW4 review's second pass, withdrew a
correct finding - the recommendation was Haaland and Ballard, held twice per the retrievable
record - on an unverified recollection, and rebuilt the review on it. Doctrine s7: no
agreeing because pushed. An earlier draft n=17 ("called the 11:32 call final") was proposed
in the same thread and withdrawn. It was never written. Fix: when the record and a
recollection conflict, hold the record, state the conflict, and ask. Commit the GW ruling at
the deadline, so a post-mortem never depends on chat retrieval.

Deltas since n=15: family process 4->5, name-resolution 0->1. Caught-by self 4->5, manager
9->10. Self-caught share 4/15 -> **5/17**. Still the wrong direction into GW10.

### 17 Sep 2026 - open items from the GW4 post-mortem

Filed open. None is ruled.

| Item | Status |
|---|---|
| Armband lock | PROPOSED. The armband stays at the last recorded call. A change needs a named cause (availability or confirmed news) and a one-line reason written before the deadline, so GW10 can count overrides as doctrine s8 does. Awaiting ruling |
| GK+DEF pair: warn or fail | CONFLICT. `operating.md` lists it as a coded cap. `check_squad.py` only warns. The GW4 XI started the pair. Reconcile at GW10 |
| Template XI | NO RULE. `benchmarks.template_xi_pts` is blank for all four rows. Without a construction rule GW10 has one benchmark, not two |
| Watchlist notes shift | OPEN (n=16). Rebuild row by row |
| Set-piece baseline | GAP (found 11 Sep). `baseline_snapshot_20260803.csv` has no set-piece columns, so review step 3 cannot diff against data |
| Mirror note in `config.json` | STALE (found 11 Sep). It says frozen at 3 Aug; the mirror had 616 rows on 11 Sep |

### GW5 - RULED before the deadline (18 Sep 2026, ~17:15 BST)

Committed before the 18:30 BST deadline, per the n=17 fix. Post-deadline items are listed at the foot.

**Transfer - 1 FT, no hit, no chip.** João Pedro (CHE) -> Calvert-Lewin (LEE, 6.0). Made in-app [screenshot, 17:04 BST]. The public transfers endpoint shows nothing for GW5 pre-deadline [live]. Verify against the GW5 picks after the deadline.

**Cause: availability.** FPL flag 75%, unchanged since 16 Sep [live]. ESPN reported a knee injury, about 3.5 weeks out, and withdrawal from Brazil's squad [press, 18 Sep]. Alonso said nobody was ruled out before Friday's session [press, 17 Sep]. Called ~80% to miss GW5, with GW6 at risk. Injury protocol: starter out 2-4, spare FT.

**Replacement - the review moved during the session.**
1. First pick Barry (EVE, pen 1, IPS home), on an unadjusted xGI/90 comparison.
2. Manager challenged Barry's blanks. Per-match xG showed volume in every match (2.98 xG, 1 goal) [live]. Fixture-adjusted, Calvert-Lewin's output was level. Barry held 55/45 on EO only.
3. Manager leaned Calvert-Lewin on form. Team data backed him: CRY xGC 2.04/g v IPS 1.69/g; LEE xG 1.66/g v EVE 1.22/g [live]. The review moved to Calvert-Lewin, 55/45.
Logged rationale is the underlying team data. Manager's stated reason was form. GW10 should grade it as the logged rationale, and note the stated one.

**Captain Haaland, vice Palmer.** Matches the recommendation. Haaland 73.2% owned [live]. Tier EO not measurable pre-deadline.

**Recommended XI.** Verbruggen; Gabriel, Tarkowski, Ballard; Palmer, Rogers, Groß, Tzolis, Ampadu; Haaland, Calvert-Lewin. Bench: Dubravka; 1 Kadıoğlu, 2 Shaw, 3 Obi. `check_squad.py` and `collisions.py` both pass [live].

**Fielded XI** [screenshot, 17:04 BST]. The same, with **Kadıoğlu for Ballard**. Bench: Dubravka; 1 Ballard, 2 Shaw, 3 Obi.

**Manager override - Kadıoğlu over Ballard. Written before the deadline.**
- Effect: `collisions.py` exits 1, with two class-A pairs in the XI (Verbruggen-Gabriel, Kadıoğlu-Gabriel). `check_squad.py` warns on the BHA GK+DEF pair [live].
- Manager's reason, stated before the deadline: form over everything else; the better player for the better team; Arsenal and City are both tough opponents, so there is not much in it.
- Review's counter [live, GW1-4]: BHA xGC 7.04 v SUN 5.84. Kadıoğlu 8 pts and 0/3 DefCon delivered; Ballard 12 pts and 2/4. ARS 6.87 xG v MCI 7.94, so the clean-sheet odds are level and Ballard's DefCon route decides it. Called ~60/40 Ballard, low stakes.
- Grade on process v variance (doctrine s6), not the GW5 result alone. This is the second consecutive Kadıoğlu-over-Ballard override. GW4's was graded right on a fixture-adjust.

**Chips - none.** Free Hit held: the tie-breaker (2+ of the XI flagged) stood at 1 [live]. Wildcard GW6 stands, deadline Sat 10 Oct 11:00 BST [live]. No PL fixture 22 Sep - 9 Oct [live].

**Open - awaiting manager ruling.**
- n=18 candidate, self-caught. `config.json` `first_midweek_load` says the league phase starts 15-17 Sep, "i.e. GW5". UCL MD1 was 8 Sep (Porto 0-2 Man City) [press, ESPN]. Another hand-typed constant.
- n=19 candidate, caught by manager. An unadjusted per-90 comparison (Barry v Calvert-Lewin), and a rejection reason (Leeds' six-GW run) that the GW6 Wildcard voids. No decision changed.
- Armband lock: still PROPOSED.
- Project prompt still names the archived behaviour/method/data/analysis.md as operating instructions. n=14 family. Update it to operating.md and doctrine.md.

**Post-deadline, not yet done.** `decision_log` row; `rejections` rows (Hold, Barry, Free Hit GW5, Wildcard GW5, Ballard start); plan append; transfer verification.

### GW6 - RULED before the deadline (10 Oct 2026, ~10:50 BST)

**Context.** Session opened ~20 minutes before the deadline. No GW6 moves had been made. Rank 264,742 after GW5 [live]. 1 FT, ITB 2.6 [live]. Set-one chips left: Wildcard, Free Hit, Bench Boost [live].

**Process.** The first pass was API-only. The manager asked for the full sweep. The 10-step loop was then run from the live repo `SKILL.md`. Done: staleness (current), squad health, fixtures GW6-11, pool scan, r/FantasyPL sweep, plan consult, scorecard, captaincy EO. Not run: `check_squad.py`, `collisions.py`, OneFPL, FPL Copilot. Set-piece diff not possible: `data/baseline_snapshot_20260803.csv` has no set-piece columns.

**Transfer.** Tzolis -> Mbeumo, free transfer. Ground: availability. Tzolis hamstring, expected back 24 Oct [live]. Mbeumo: best xGI/90 of fit mids <=8.9 (0.77), 450 of 450 mins, pen order 2, TOT (H) FDR 2 [live]. Hold ranked second. The one-week gain is close to the value of a banked FT. Mbeumo is re-argued from scratch on the Wildcard. Man United's GW6-11 run is bottom-six [live].

**Wildcard deferred, GW6 -> GW7.** The ground is process, not evidence. The squad-build checks could not run in the time left. That is not a listed amendment ground. The manager accepted it. Plan amended under the same date.

**Free Hit.** Not fired. No blank or double in GW6 [live].

**Captaincy.** Haaland (C), Groß (VC). Haaland 74.3% owned [live]. City team news says he is fine [community, 9 Oct].

**Lineup - manager override, stated before the deadline.**
- Review: start Shaw, bench Kadıoğlu. Verbruggen + Kadıoğlu is the barred BHA GK+DEF pair (doctrine).
- Manager started Kadıoğlu over Shaw. Reason: trusts Kadıoğlu's form more.
- Review's counter: form alone is a trigger to look, not to act. Shaw has TOT (H) FDR 2; Kadıoğlu has SUN (a) [live]. Shaw carries real minutes risk: 0 mins GW4, 83 GW5 [live].
- Third consecutive Kadıoğlu override (GW4, GW5, GW6). GW4's was graded WRONG for the review. Grade on process v variance, not the GW6 result alone.

**Collision, accepted.** ARS v LEE in GW6: Gabriel against Calvert-Lewin and Ampadu. Present under every option. Not graded by script.

**Community flags, not acted on.** Palmer: bookmaker Chelsea goals dipped ~0.1 on deadline morning; some read it as a start doubt [community, 10 Oct]. FPL flag clean [live].

**Written this session.** `rejections` rows 22-27 (Hold, Wildcard GW6, Free Hit GW6, Kadıoğlu start, Ødegaard, Groß (C)). Plan amendment, 10 Oct.

**Post-deadline, not yet done.** Transfer verification: the GW6 transfer was not visible in `entry/50930/transfers/` at 09:50 UTC [live]. The `decision_log` row waits for it. GW5 backlog still open: `decision_log` row (João Pedro -> Calvert-Lewin), GW5 `rejections` rows, GW5 plan append [live, sheet read 09:50 UTC].


## 17 Oct 2026 - GW7 Wildcard ruling

**Ruling.** Wildcard played GW7, deadline Sat 17 Oct 11:00 BST. Manager confirmed 10:00 BST.

**Squad (15).** GK Trafford, Leno. DEF Calafiori, De Cuyper, Hall, Van Hecke, Silva. MID Saka, Groß, Rogers, Belloumi, Rudoni. FWD Haaland, João Pedro, Barry. Cost £98.1m on selling prices, ITB £1.4m [live]. Kept: Groß, Rogers, Haaland.

**GW7 XI.** Trafford; Calafiori, De Cuyper, Hall, Van Hecke; Saka, Groß, Rogers, Belloumi; Haaland (C), João Pedro. Saka (VC). Bench: Leno, Barry, Silva, Rudoni.

**How it was built.** A blind, multi-agent adversarial pipeline. Spec `docs/superpowers/specs/2026-10-17-gw7-wildcard-pipeline-design.md` (commit 05417b6).
- Snapshot 01:33 BST, 436/436 histories [live]. Budget 995 after overnight price moves (Groß, Haaland +0.1, Mbeumo -0.1).
- Research x5 (players, fixtures, news, Reddit, blogs). Fact base checked every community claim; 51 discarded.
- Three blind builders (ceiling, template-plus, doctrine-free). The 16 Oct pick (C2') entered anonymised.
- Two prosecutors, a doctrine challenger, four rebuttals, a fresh judge.
- Verdict: winner squad A (builder X), runner-up C (doctrine-free), D (template) third, C2' last on points, leverage and bench.

**Manager deviations from the verdict, stated before the deadline.**
- Built his own blend: template core (Calafiori, De Cuyper, Groß, João Pedro, Rogers) plus Saka, Haaland.
- Raya -> Trafford taken on review advice (Raya + Calafiori = one D13 slot for £12.0m).
- Tavernier over Rudoni reversed on review advice (Rudoni 0.53 xGI/90 without best game v 0.35; pen 1 v 3).
- Calafiori started over Silva (manager). Review agreed: Calafiori is not a pure floor asset.
- **Belloumi kept and started over Barry - manager override.** Review: 3 goals from 0.69 xG GW4-6, minutes 59/82/26, pen 2; GW7 proj 3.09 v Barry 4.59 [live, model]. Manager: benched in GW6 then scored; expects him to start again. Supporting point: Hull manager said Gelhardt lacks rhythm [community, 15 Oct]. Sell trigger: benched again in GW7 = named cause (D3).

**Scores on the shared yardstick, GW7-11 [live, model].** Final squad 282.3 xPts, leverage 189.6, bench 68.0. Squad A 284.6 / 208.1 / 75.1. The gap is the leverage cost of the template core.

**Doctrine challenge.** Judge accepted amendments to D2, D5, D9, D11 (class A is not a collision), D12, D14, D15; amended D1 and D7 differently; kept D10 to its GW10 expiry. **None ruled.** Filed open for the GW10 review. D7 ('no projection model') was challenged by the pipeline's own design; the yardstick is recorded as a screen, gaps under ~5 xPts are ties.

**Known gaps.** No 13-17 Oct source for MCI, IPS; no Coventry subreddit; one full published draft; no top-10k EO. Price table leaked ownership of 5 players to agents (process_errors n=23). Account usage limit paused the run 03:45-06:21 BST; no work lost.

**Written this session.** decision_log GW7 row. rejections rows (squad A, D', C2', Belloumi->Ndoye/Tavernier, Barry start). process_errors n=20-23. Plan amendment 17 Oct. Not yet done: final code review of pipeline tools; commit of pipeline tools to `pipelines/wildcard/`; post-deadline verification of picks via `entry/50930/event/7/picks/`.


## 23 Oct 2026 - GW8 ruling

**Ruled 15:53 BST, before the 18:30 deadline** [live]. 1 FT (confirmed by the manager), ITB £1.4m [live].

**GW7 verified** [live, `entry/50930/event/7/picks/`]. Wildcard played. Picks match the 17 Oct ruling. 62 pts v average 59. Overall rank 298,350 -> 473,792. Bench 22 (Silva 8, Leno 6, Rudoni 6, Barry 2). Belloumi played 90, so his sell trigger did not fire. Belloumi v Barry override: 2 v 2.

**Transfer - 1 FT, no hit.** Saka (ARS, sells £9.6) -> Mbeumo (MUN, £7.9). ITB £3.1m after. Made in-app by the manager. Verify against the GW8 picks after the deadline.

**Cause: availability.** Saka came off at 10' at Bayern on 21 Oct with a quad injury [community, 22 Oct]. FPL flag went from 50% (22 Oct) to `i`, 0%, "unknown return date" (23 Oct) [live]. Arteta, 23 Oct: a second MRI, "a lot of fluid", "struggling to walk without pain... not good signs", no timeline [community, 23 Oct]. Called ~85-90% to miss GW9. Injury protocol: starter out 2-4, spare FT.

**Why now, not after the scan.** The 22 Oct rule said "unknown -> hold". Withdrawn. Both routes give the same two moves over GW8-9 (process error n=25). Holding gains only if Saka is fit by GW9. Selling now banks Mbeumo's GW8 and Saka's full sale price before the drop: 492k managers sold him this GW [live].

**Why Mbeumo.** 630/630 mins, 0.70 xGI/90, the best affordable mid on volume. Pen 2 [live]. The manager doubted him on United's form, the press and the Como defeat in the UCL. Review: no Mbeumo-specific cause. MUN 1.43 GF/g v BOU 1.29 [live]. Tavernier rated ~40/60: minutes 74/72/78, pen 3, and a third player in BOU v LEE in the Bench Boost week. The manager chose Mbeumo.

**Chip - Bench Boost moved GW8 -> GW9.** Manager ruling, 22 Oct. Grounds: availability (Saka) and the doctrine s4 stopping rule. The GW9 bench fixtures are stronger and no European midweek precedes GW9 [live]. Plan amended.

**Captain Haaland, vice João Pedro.** Haaland 76.9% owned [live], so captaining him is the defensive play. Tier EO not measurable.

**XI, 4-4-2.** Trafford; Calafiori, De Cuyper, Hall, Silva; Mbeumo, Groß, Rogers, Rudoni; Haaland (C), João Pedro (VC). Bench: Leno; 1 Barry, 2 Van Hecke, 3 Belloumi.
- Silva for Van Hecke: DefCon delivered 5/7 v 3/7. It also removes two class-B pairs (Chelsea attackers v Van Hecke).
- Rudoni for Belloumi: pen 1, 0.58 v 0.28 xGI/90, FUL (H) v BRE (H).
- `check_squad.py` and `collisions.py` both exit 0. Repo scripts run against the live API. One class B! in the XI: Mbeumo v Silva (MUN v BOU). Accepted.

**Rejected** (`rejections`): Bench Boost GW8; hold Saka until the scan; Tavernier; Cherki; Ødegaard; Belloumi start.

### Process errors - updated 23 Oct 2026

**n=24, caught by manager.** The 22 Oct review stated 2 FTs for GW8, "derived" from a claim that a Wildcard keeps the FT. That was a rule asserted from memory and wrong; the manager confirmed 1. Not used to reject anything. Corrected before use.

**n=25, self-caught.** On 22 Oct the review argued that holding the FT gave GW9 two moves while selling Saka left one. Both routes give two moves over GW8-9, because the Saka fix uses a GW9 FT either way. This false reason held off the sell-now option for a day. It is the n=15 shape: a rejection reason that never faced the arithmetic. Corrected before the deadline. No cost.

**n=26, self-caught.** The Skill tool again loaded the stale `/mnt/skills` 9-step snapshot (n=14 repeat). Caught and switched to the repo 10-step version. The mount is outside our control; the `operating.md` rule held.

Deltas: caught-by self +2, manager +1.

**Still open.** The project prompt still names the archived behaviour/method/data/analysis.md as operating instructions (open since GW5). The set-piece baseline still has no set-piece columns.
