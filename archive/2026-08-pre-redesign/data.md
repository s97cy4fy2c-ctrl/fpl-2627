<!--
ARCHIVED 20 Aug 2026. Verbatim below. Three claims have since been DISPROVEN by testing:

1. "Blocked: entry/{id}, element-summary/{id}, event/{gw}/live, leagues-classic.
   Don't retry these." -- WRONG. All four are reachable from the Composio sandbox.
   They were only ever blocked to web_fetch. Recording a tool quirk as a property of
   the API, then instructing future sessions not to retest, cost this project a week.

2. "Player list truncates at ~33 of 567" -- true of web_fetch only. The sandbox
   returns the complete 1.58MB payload.

3. "Effective ownership exists nowhere machine-readable. Screenshots only."
   -- still true in practice as of 20 Aug, but for a different reason than assumed:
   plan.livefpl.net returns 422 to ZenRows even with premium proxies.

The trust-by-field table and the funnel principle SURVIVE the redesign intact. They
were right. What failed was the Blocked section: a snapshot of one tool's limits,
written as permanent fact, with retesting explicitly discouraged.

LESSON: never write "don't retry" into a doc. Write the date and the tool it applied to.
-->

# data.md

## Staleness tagging — mandatory

Every substantive claim carries its provenance:

- **[live]** — fetched this session from the official API
- **[mirror, DD Mon]** — from the GitHub dump, with its date
- **[memory]** — not fetched. Say so explicitly and treat as a hypothesis.

If you can't tag it, don't assert it.

## Sources

**Official FPL API** — reachable via web_fetch, fully current, authoritative.
- `fantasy.premierleague.com/api/bootstrap-static/` — rules, scoring, chips, deadlines,
  clubs. **Player list truncates at ~33 of 567**, ordered by club ID, so only Arsenal is
  fully readable.
- `fantasy.premierleague.com/api/fixtures/` — all 380 fixtures with difficulty ratings.

Note: web_fetch only accepts URLs already seen in the conversation.

**GitHub mirror** — reachable from the container via bash (`raw.githubusercontent.com` is
allowlisted; `fantasy.premierleague.com` is not).
All 567 players, 20 clubs, every field. **Lagged.**

**Web search** — current on named players. Requires knowing who to ask about.

**Manager screenshots** — squad state, LiveFPL effective ownership, official price
predictor. The only route to anything client-side rendered.

## Trust by field, not by source

| Field | Trust | Note |
|---|---|---|
| Minutes, starts, xGI/90, DefCon/90 | High | Slow-moving; a week-old value is still good |
| Set-piece order | High | Changes rarely, but changes matter enormously |
| Price | **Pre-season high, in-season low** | Locked until GW1 deadline; then daily changes |
| Ownership | Low | Drifts continuously |
| Club assignment | Low | Misses recent transfers |
| Injury status / news | Low | Verify by search before acting |

Inverted trust on price is the trap: safest field pre-season, one of the worst after.

## Staleness test — run every session

Arsenal is the one club the live API renders completely. Diff mirror-Arsenal against
live-Arsenal on ownership. Match → mirror is current. Divergence → that's the lag, applied
to all 567 rows. **Report the result before using mirror data.**

Known example: on 18 Aug 2026 the mirror was dated 3 Aug and still listed Bruno Guimarães
at Newcastle, three weeks after he'd joined Arsenal.

## The funnel

Don't narrow the player pool. Narrow by *field speed*.

- **Slow fields, all 567 players** → this is what surfaces candidates.
- **Fast fields, verified per name** → only once a candidate has surfaced.

Breadth for scanning, precision for the shortlist. Never invert this.

## Blocked

`entry/{id}` (manager's team), `element-summary/{id}`, `event/{gw}/live`,
`leagues-classic/{id}/standings`. Don't retry these; they fail on a URL-permission basis,
not a rate limit.

LiveFPL and most modern FPL tools render client-side — fetching returns meta tags only.
Effective ownership by rank tier exists nowhere machine-readable. Screenshots only.

## Official price predictor

New for 2026/27, built into the FPL app, live after the GW1 deadline. Uses official
transfer data rather than inferring thresholds. Prices change around 01:30 UK, £0.1m steps,
max once per day and three times per gameweek.
