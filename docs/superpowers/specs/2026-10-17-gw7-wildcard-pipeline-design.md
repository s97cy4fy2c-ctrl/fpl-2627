# GW7 Wildcard pipeline — design

- **Date:** 2026-10-17, 01:25 BST
- **Status:** draft for Ben's review
- **Entry:** 50930. Target: top 100k overall.
- **Decision:** the GW7 Wildcard squad for GW7–11. Deadline **Sat 17 Oct 2026, 11:00 BST**.

## 1. Purpose

- Pick the GW7 Wildcard squad from a **fresh, blind, multi-source, adversarial** process. It must not be built on the reasoning already done in the 16 Oct session.
- Build the minimum that serves GW7 tonight, laid out so it can later be hardened into a reusable repo pipeline (option C).

## 2. Hard constraints

1. **Deadline.**
   - Start immediately after the plan is approved.
   - Target verdict about 05:30 BST.
   - Hard fallbacks at 08:30 and 09:30 BST (§10).
2. **Blindness.**
   - No agent receives this session's conclusions: the scorecard, C1/C2′, keeper reasoning, the horizon grid, or any view on a player.
   - No agent sees the conversation or files produced before this run.
3. **Game rules are fixed:**
   - budget £99.4m, computed from selling prices
   - squad 2 GK, 5 DEF, 5 MID, 3 FWD
   - max 3 per club
   - valid XI formation
4. **Doctrine is challengeable.**
   - Every rule in repo `docs/doctrine.md` may be challenged.
   - A challenge produces a proposed amendment that Ben rules on. Nothing changes silently.
5. **Models.**
   - Haiku or Sonnet only, by the capability each job needs (§4).
   - No Opus subagents.
   - The orchestrator runs on whatever model the chat is set to.
6. **Authority.**
   - The pipeline never touches the FPL account.
   - Ben rules on the verdict. Nothing is logged to the ledger, sheet or plan until he does.

## 3. Shared store

Root: `run/gw7/` in the orchestrator's workspace.

```
run/gw7/
  status.json          stage → pending|running|done|failed, timestamps, notes
  briefs/              every dispatched brief + leak-check result
  snapshot/            Stage 0 outputs, timestamped
  research/            R1–R5 outputs
  fact/                fact_base.md, pool.csv, projections.csv, discarded.md
  builds/{x,y,z}/      squad.json, rationale.md, doctrine_breaches.md
  tribunal/            labels.json (sealed), prosecutions, rebuttals, challenge.md
  verdict/             verdict.md, repriced.json
```

- Each stage writes a `DONE` marker in `status.json` only after its outputs exist and pass their checks.
- **FPL API and Reddit access** go through the Composio sandbox. The orchestrator's container gets a 403 from the FPL API.
- **Snapshot transport** from sandbox to workspace is verified in plan step 1. If transport fails, the snapshot is pinned in the sandbox's persistent output directory and computing agents work there, against that pinned copy only.

## 4. Stages and agents

| Stage | Agent(s) | Model | Inputs | Outputs |
|---|---|---|---|---|
| 0 Snapshot | 1 | Haiku | FPL API | bootstrap, fixtures, all per-player histories, GW6 picks, transfers, selling prices; one timestamp |
| 1 Research | R1 Players | Sonnet | snapshot | `research/players.md` |
| | R2 Teams & fixtures | Sonnet | snapshot | `research/fixtures.md` |
| | R3 News | Haiku | web | `research/news.md` |
| | R4 Reddit | Sonnet | Reddit via Composio | `research/reddit.md` |
| | R5 Blogs & data sites | Haiku | web | `research/blogs.md` |
| 2 Fact base | 1 | Sonnet | research + snapshot | `fact/*` (§6) |
| 3 Builders | X ceiling, Y template-plus, Z doctrine-free | Sonnet | `fact/*` | `builds/*` |
| 4 Tribunal | 2 prosecutors (2 squads each) | Sonnet | 4 anonymised squads + `fact/*` | prosecutions |
| | 1 doctrine challenger | Sonnet | doctrine + squads + `fact/*` | `challenge.md` |
| | X, Y, Z resumed for rebuttal | Sonnet | own squad + its prosecution | rebuttals |
| | 1 C2′ defender (fresh) | Sonnet | C2′ + `fact/*` only | rebuttal |
| | 1 judge (fresh) | Sonnet | final dossiers only | `verdict.md` |
| Pre-dispatch | 1 leak checker | Haiku + script | each brief | pass/fail |
| 5 Relay | orchestrator | — | verdict | chat message + phone push |

**Total: 16 agents** (15 working agents plus the leak checker). Stages 1 and 3 run in parallel; so do the prosecutors and the challenger.

**Research claim format.** One line per claim:

`claim | subject (player/team) | source + date | tag [live|community|official] | live-checkable y/n`

**Research scope.**
- **R1:** xGI per 90, minutes, starts, DefCon delivered (threshold rule as in doctrine), set-piece orders, bonus, over/under-performance against xG/xA.
- **R2:** team attack and defence rates, opponent-adjusted runs GW7–11, home/away splits, European midweek load.
- **R3:** injuries, suspensions, press conferences, role changes.
- **R4:** r/FantasyPL, team-reveal and ownership threads, club subreddits.
- **R5:** Scout/Hub/Fix-style articles, published Wildcard drafts, top-10k ownership and EO.

## 5. Blindness controls

1. **Fixed brief template.** Slots only:
   - role
   - input paths
   - doctrine pasted verbatim from the repo
   - game rules
   - output schema
   - tooling notes

   No free text from the orchestrator beyond the one-line role.
2. **Leak check, before every dispatch.**
   - (a) A script fails the brief if it contains any bootstrap `web_name` or second name, "C1", "C2", "scorecard" or "incumbent".
   - (b) Haiku reads the brief for steering emphasis.
   - On failure, the brief is rewritten and rechecked.
3. **Budget without ownership signal.**
   - The price table given to builders replaces the current price of the 15 GW6 players with their selling price.
   - Ownership is not marked anywhere.
4. **Isolation.** Builders don't see each other's squads.
5. **Anonymised contest.**
   - The three builds plus C2′ get shuffled letters A–D.
   - The mapping is sealed in `labels.json`, read only by the orchestrator.
   - All squads use an identical format, with rationales stripped before prosecution.
   - C2′ is rebutted by a fresh defender, so it isn't the only squad without a defence.
6. **Tooling note, not reasoning.** Builders are told that the repo `build.py` solver uses full-season thresholds that fail mid-season, and that it needs `pulp==2.9.0`.

## 6. Fact base and shared yardstick

`fact/` contains:
- `fact_base.md`: verified claims, merged.
- `pool.csv`: about 60–80 candidates with verified fields.
- `discarded.md`: claims the live data contradicts, each with its reason.
- `projections.csv`: one transparent per-player, per-GW projection for GW7–11. Every assumption is written in the file. Components:
  - minutes probability
  - xGI per 90 × opponent softness
  - clean-sheet probability, from team xGC × opponent attack
  - DefCon rate
  - bonus rate

Every squad is scored on `projections.csv`. Builders may argue against it, but the judge uses it.

## 7. Doctrine challenge

- **Rule list.** Doctrine rules are numbered from repo `docs/doctrine.md` at brief-build time.
- **Measured cost.** Doctrine's cost is the gap between builder Z and the best of X and Y on the yardstick.
- **The challenger, per rule:**
  - expected points the rule cost, with evidence
  - the risk the rule protects against
  - keep, amend or drop, with proposed wording
- **The defence.** X and Y defend doctrine in their rebuttals.

## 8. Judge

**Scorecard, GW7–11:**

| # | Axis | Measured as |
|---|---|---|
| 1 | Expected points | Best projected XI each week, summed |
| 2 | Minutes security | Starts, flags, rotation risk |
| 3 | Rank leverage | Expected points weighted by (1 − ownership) |
| 4 | Collisions | Class-A clashes in the XI across the horizon |
| 5 | Flexibility | Bank, price-fall exposure, slots likely to need moving by GW11 |
| 6 | Bench | Bench expected points |
| 7 | GW12–14 swing | Tiebreak only |
| — | Doctrine breaches | Listed, not scored |

**Required output:**
- winner, runner-up and best fully compliant squad
- case against the winner
- sensitivities ("the verdict flips if X")
- recommended rulings on each doctrine challenge

**Re-price.** Before the judge scores, all four squads are re-priced against a fresh API pull and re-checked for budget.

## 9. Ruling rule

- If the winner breaks doctrine, Ben rules on each rule it breaks before 11:00.
- If he rejects a rule change or doesn't rule in time, the best fully compliant squad is the pick.

## 10. Failure handling and resumability

| Failure | Response |
|---|---|
| Snapshot API failure | Retry with backoff, then **hard stop and alert**. No stale data. |
| R1 or R2 fails | One rerun, then stop and alert |
| R3, R4 or R5 fails | Continue. The gap is named in the verdict. |
| Illegal squad | `check_squad.py` rejects it. One fix attempt, then the squad is dropped. |
| Leak check fails | Rewrite and recheck |
| Reddit 429 | Backoff. Partial coverage noted. |
| Any stage fails | Resume from the last `DONE` stage. Never restart from scratch. |

- **Check-ins.** Scheduled check-ins into this session about every 45 minutes. Each checks `status.json`, retries failed stages and continues.
- **08:30 BST, no verdict:** the judge rules on the squads that exist.
- **09:30 BST, nothing usable:** the pipeline has failed and C2′ stands as the verified-legal fallback. C2′ appears in no brief before Stage 4.
- **Alerts.** The verdict, or a failure message saying what broke and what is needed, goes to the chat and to Ben's phone.

## 11. Success criteria

- A verdict delivered by about 06:00 BST, naming:
  - winner, runner-up and best compliant squad
  - case against the winner
  - doctrine rulings to make
- Every squad legal after re-pricing.
- Every claim in the verdict tagged and traceable to a file in `run/gw7/`.
- The leak-check log shows every brief passed.

## 12. Out of scope tonight (hardening to B later)

- Turning the briefs and stages into a repo skill
- Reusable config across gameweeks
- Ledger and sheet logging, which happens after Ben rules, under the existing rules
