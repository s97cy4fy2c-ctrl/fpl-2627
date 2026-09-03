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
