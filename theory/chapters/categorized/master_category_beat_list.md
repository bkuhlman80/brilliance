# Master Category & Beat List

## THE RULE: every beat gets a tag, in every chapter, no exceptions

For every chapter, and for every beat letter listed under a category in the Category detail table
below (when that category is present in the chapter at all — see Absence), there must be a tag
on the page for that beat. No letter is ever silently missing. This holds regardless of why the
letter has no scene of its own:

- **Present** — the beat has its own bounded content. Tag is dated, at the point the content begins.
- **Folded** — the beat's material exists but never separated into its own scene; it reads as part
  of a neighboring beat's prose. Tag is bare (no date), placed at the point the beat's material
  would begin within the neighboring text.
- **Absent** — there is no material for the beat anywhere in the chapter. Tag is bare (no date), at
  the beat's position in the sequence.

Folded and absent both get the same bare-tag format — the tag does not need to say which one it
is. What the tag guarantees, in both cases, is that the letter is accounted for. A missing tag is
never correct. If you can't tell whether a beat is folded or absent, tag it bare anyway and flag
the uncertainty — but the tag goes in either way.

**Verification check:** for a chapter to be considered complete under this spec, grepping the file
for every `<!--[N.letter]` combination implied by the Category detail table (for every category
present that chapter) must return at least one match. Zero matches for any expected letter is a
defect, full stop.

**A bare category tag sitting alone, with no beat tags at all, is itself a defect** — not a
formatting nuance to leave for later. An absent category must show its *category* tag plus *every
one* of its beat tags, concatenated (see Header format below). If you find `<!--[4.6]-->` on its
own line with no `<!--[4.6.a]-->` / `<!--[4.6.b]-->` beside it, that chapter has not actually been
tagged for that category yet — fix it as part of the same pass, don't just reformat around it.

---

## Header format

**Category boundary — split across three lines, not one:**

1. Hidden category tag alone on its own line: `<!--[N]-->`
2. Visible title on the next line, no date, no tag inline: `## Title`
3. A visible italicized subtitle line right under the title, with no blank line before it — and
   its content depends on the category type:
   - **Category 1 (Build Log):** the in-universe memo byline, e.g. `*Bart, hardware. Filed
     February 12, 2031, for the team.*`
   - **Category 2 (Cheryl's Lunch):** date only, prose style — `*July 27, 2031*` — matching the
     Category 1 byline's date format (Month DD, YYYY), not the ISO style used at Category 5.
   - **Categories 4.1–4.15 (the retrospective meeting):** a date and clock time, e.g.
     `*2031-05-15 4:45pm*` — and the time advances category to category across the evening
     (4:45pm → 5:20pm → 5:32pm → 6:18pm → 6:43pm → 7:01pm → 7:16pm → 7:45pm → 7:59pm → 8:08pm →
     8:12pm in Ch1). Each category slot gets its own specific clock time, tracking the meeting's
     real-time progression — not just one shared date for the whole meeting. Gaps are weighted by
     how the section actually plays (a monologue-heavy slot runs longer in real time than its line
     count suggests), not divided evenly — Ch1's 4.3 (Deep Time) is deliberately the single longest
     slot in the chapter, since that's the section the room jokes about running over
     ("land the plane").
     **Building the progression for a new chapter:** search the chapter's own prose for hard
     anchors before inventing anything — an explicit stopwatch/duration line (Ch2's deep-time ran
     21:15, Ch3's ran 19:00 — both used as the fixed gap for that slot), a stated clock time
     ("It was six twenty," Ch2's 4.7), or a comparative cue ("six had come and gone," Ch3's 4.11).
     Anchor the progression to those, then distribute the remaining gaps by scene weight for
     everything else. If two anchors in the text contradict each other (Ch2's 4.7 has both "six
     twenty" and a claim that the dusk-triggered lot lights — which don't fire until past eight in
     August — had already clicked on), don't silently resolve it in favor of one; flag the
     contradiction and let Brian rule on which detail is wrong.
   - **Category 3 (Household Vignettes):** no subtitle line at all — dates live at the beat level
     instead (see below).
4. Then a blank line, then the first beat tag.

**Beat tags carry no date at all.** Just `<!--[N.letter]-->`, bare. Letters run a, b, c… in fixed
order; a letter appearing out of that order is a violation unless it's a deliberate recurrence.
Content follows the beat tag directly — no blank line, no date — **except category 3**, where each
vignette's beat tag is followed (no blank line) by a short visible date, `*February 12*`, then a
blank line, then content. That's the one place a date shows on the page.

**Whole-category absence loses its title and collapses onto one line.** No `##`, no subtitle —
just every tag for that category (the category tag plus all its beat tags) concatenated with zero
spaces on a single line: `<!--[2]--><!--[2.a]--><!--[2.b]--><!--[2.c]--><!--[2.d]-->`. A run of
consecutive absent categories stacks the same way, one per line, no blank line between them. A
standalone no-beat category that's absent (4.7, 4.14) just gets its own bare tag alone on a line.

**Consecutive absent beats within an otherwise-present category also collapse onto one line** —
e.g. `<!--[4.8.b]--><!--[4.8.c]-->` when both are missing back to back. A single trailing absent
beat just gets its own line.

**A horizontal rule (`---`) precedes every titled category** — including the very first one, right
after the chapter's own title block — but never precedes an absent (title-less) category. If
several absent categories run together, the `---` appears once, right before the next titled one.

- **Standalone single-content categories** (4.7, 4.14): same category-boundary format as any other
  category when present, but no internal beat letter — content runs directly under the subtitle
  line.
- **Visible titles are never the spine label.** The `## Title` line is reader-facing and must never
  just restate the category's name from the spine (never `## Pitch / Reveal`, never `## Retrospective:
  Bart Grills Mira` used verbatim as the visible title of that category's chapter instance — that
  wording lives only in the spine table below, for our internal bookkeeping). Each chapter invents its
  own title for the slot: clever, specific to what actually happens in that instance of the category,
  and meant to intrigue the reader rather than label the mechanism. ("Guess How" for a chapter's Pitch/
  Reveal slot is the model — it's a title about the scene on the page, not the category underneath it.)
- **No provenance in the chapter files.** Migration notes, correction notes, "formerly X" labels,
  and dated rulings don't belong on the page — only current state and the rule that currently
  governs it. (This master doc is the one exception: its own spine list below keeps "formerly"
  annotations for now, since another process depends on them.)
- **Bart's Build Log sign-off is a running joke, not a typo.** "Bartholomew" (Ch1), "Bartholomood"
  (Ch2), "Bartholachew" (Ch3) — each chapter gets its own variant. Don't flag it, don't "fix" it
  back to Bartholomew.
- **Every beat gets a tag.** See THE RULE at the top of this doc — it governs Absence too, and
  supersedes any narrower reading of the bullet above.

---

## The chapter spine — 18 stops, fixed order

1. **1** — Build Log
2. **3** — Household Vignettes
3. **2** — Cheryl's Lunch
4. **4.1** — Retrospective: Arrival Choreography
5. **4.2** — Retrospective: Clade Block
6. **4.3** — Retrospective: Burns's Deep-Time
7. **4.4** — Retrospective: Bot Block
8. **4.5** — Retrospective: Bart Grills Mira (beats a–c only; formerly 4.5.a–c, with 4.5.d split off)
9. **4.6** — Retrospective: Pitch / Reveal (formerly beats 4.11.a–b)
10. **4.7** — The Break (mid-meeting pause; formerly beat 4.5.d)
11. **4.8** — Retrospective: Jasmine's Report (formerly 4.6)
12. **4.9** — Retrospective: Lisa's Trellis (formerly 4.7)
13. **4.10** — Retrospective: The Sentience Vote (formerly 4.9)
14. **4.11** — Retrospective: Marge's Fallacy (formerly 4.8)
15. **4.12** — Retrospective: WORM-to-___ Slideshow
16. **4.13** — Retrospective: Burns's Verb-Toast Close (formerly 4.10)
17. **4.14** — Logistics (formerly beat 4.11.c)
18. **4.15** — Solo Coda (formerly 5)

Categories never move relative to each other. Any category can be entirely absent in a given
chapter (marked with a bare tag at its spine position) without the sequence reordering around it.

---

## Category detail

| Stop | Category | Name                                    | Beats (fixed order)                                          |
|------|----------|-----------------------------------------|--------------------------------------------------------------|
| 1    | 1        | Build Log                               | a. Engineering — b. The Knob — c. Calls + Sign-off           |
| 2    | 2        | Cheryl's Lunch                          | a. Scene Setting — [b. Dialogue & Character / c. Cheryl's Self-Narration, interwoven, no fixed order] — d. Drive Home Coda |
| 3    | 3        | Household Vignettes                     | [a. Bramblation / b. Bramble + Chill — c. Bramblearning, interwoven, no fixed order] (vignette dates must still run chronologically, whatever letter order they carry) |
| 4    | 4.1      | Retrospective: Arrival Choreography     | a. Choreography — b. Cheryl Review — c. Ambition Statement   |
| 5    | 4.2      | Retrospective: Clade Block              | a. Tarot Card — b. Breakthrough — c. Heuristics              |
| 6    | 4.3      | Retrospective: Burns's Deep-Time        | a. Ritual Framing — b. The Deep-Time Monologue — c. Landing  |
| 7    | 4.4      | Retrospective: Bot Block                | a. Owen's Critique — b. Bart's Answer — c. The Demo — d. Board Mechanics |
| 8    | 4.5      | Retrospective: Bart Grills Mira         | a. Ritual Opening — b. The Calls — c. Tally & Coda           |
| 9    | 4.6      | Retrospective: Pitch / Reveal           | a. Pitch — b. Retirement                                     |
| 10   | 4.7      | The Break                               | *(no internal beats)*                                        |
| 11   | 4.8      | Retrospective: Jasmine's Report         | a. The Household Report — b. The Kitchen vs. Bench — c. Mira's Turn |
| 12   | 4.9      | Retrospective: Lisa's Trellis           | a. Vocabulary Mode — b. Motivation & Signature Naming — c. Board Geometry |
| 13   | 4.10     | Retrospective: The Sentience Vote       | [a. The Count / b. The Reasoning, interwoven, no fixed order] — c. The Uncounted, fixed last |
| 14   | 4.11     | Retrospective: Marge's Fallacy          | a. Naming the Fallacy — b. Testing It — c. The Turn          |
| 15   | 4.12     | Retrospective: WORM-to-___ Slideshow    | a. The Ladder — b. The Tell                                  |
| 16   | 4.13     | Retrospective: Burns's Verb-Toast Close | a. The Tell, The Deep-Time — b. The Turn, The Verb-Hunt — c. The Toast, The Round, The Reach |
| 17   | 4.14     | Logistics                               | *(no internal beats)*                                        |
| 18   | 4.15     | Solo Coda                               | a. The Drive — b. The Private Ritual — c. The Narrator's Frame |

---
