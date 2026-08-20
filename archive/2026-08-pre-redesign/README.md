# archive/2026-08-pre-redesign

The four original operating documents, frozen 20 Aug 2026, immediately before the
structural redesign. **These are not live.** Nothing here should be followed.

They exist for one reason: the redesign has to be visible as a diff. Without a
baseline there is no record of what was dropped or why.

## What was actually wrong with them

Not the content. Five of the seven process errors logged in `commitments.md`
were violations of rules **written in these files and ignored**:

| Rule, and where it was written | What happened anyway |
|---|---|
| `analysis.md` — report DefCon as clearing frequency, not a raw average | The pipeline computed the raw average; it was quoted as a points estimate |
| `analysis.md` — fixture ratings ignore European commitments | European qualification was typed from memory; 5 of 9 clubs wrong |
| `analysis.md` — role is the first filter | Applied to Anderson, not to Szoboszlai |
| `data.md` — price is locked until the GW1 deadline | Contradicted from a misread API field |
| `data.md` — club assignment and news are low-trust, verify by search | Digne, Konsa, Watkins and Cash all missed |

The diagnosis is structural, not editorial. **Prose does not execute.** These
files were simultaneously reference material and operating procedure, and only
the reference half ever worked.

The redesign moves every mechanical rule into code, where it passes or fails
loudly, and leaves markdown holding only the judgment that cannot be codified.
Most of the sentences below survive that move. They just move.
