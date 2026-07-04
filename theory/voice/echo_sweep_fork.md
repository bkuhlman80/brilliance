# Echo Sweep — Tuning Fork

This fork governs the consolidated cross-chapter echo sweep: the pass that finds every
phrasing, image, beat, simile, or construction that repeats across the book and makes each
recurrence land freshly, so no two ring identical. Work it cluster by cluster, Group A
through Group F, until every cluster is closed. This is the authority for the sweep; work
from it rather than from memory or prior-conversation notes.

## The principle

Brian hates echoes, and he is right to. Any verbatim or near-verbatim call-back to wording
used somewhere else in the book — or earlier in the same chapter — is bad writing with no
offsetting value. There is no "thematic," "load-bearing," or "earned" exception that lets a
repeated *phrasing* stand. Judge every candidate cold on one question: **is this line good
prose, here, on its own?** A recurrence-frame with a graceful clause hung on it is still a
tic; the graceful clause is the disguise, not a defense.

The narrator is Cheryl — her lunches, retrospective reconstructions, closes, vignettes, and
reflections. The sweep operates on her prose. Dialogue and the character documents (Bart's
build log, Marge's "Notes on the Nth Quarter") are exempt; the Notes are handled separately
under their own strike.

## Three distinctions that do all the work

**An event may recur; its words may not.** Some things genuinely happen every quarter — Mira
keeps each new word, the vote gets called, Lisa stops the camera, Burns lifts a toast the
abstract noun won't carry. Keep the event. Write each instance from that scene's own
particulars, so the recurring event reads as a real recurring event and never as a sentence
run twice. When you de-echo a beat like this, reach into what is specific to *that* night —
the body on the bench, the shut notebook, the word being kept — and build the line out of it.

**A tell may recur; render it fresh each time.** A character is allowed a signature gesture:
Burns's chest-laugh, Marge's two-handed grip, Bart's hands going still, Lisa's palms. The
gesture recurs because the person does. But the *description* must vary, or the tell must be
established once in full and afterward referred to rather than re-defined. Never lay down the
same definition of the same tell in two places.

**Let central themes recur — in fresh dress every time.** Inherited, unchosen architecture is
the spine of the book; that theme should hit many times. The discipline is that it gets a new
expression on each hit, never the same epiphany twice. Think of a long single-theme book that
never sounds repetitive: the idea returns, the words and the image and the angle do not. This
applies to content-level echoes, not just phrases — two chapter-codas landing on the identical
realization is a repeat even when no string matches, and the fix is a genuinely different
expression, not a cut.

## Discernment — reserve "keep" for what is actually central

Do not call everything the spine. The instinct to protect a line because it is thematic, or
because it carries an emotion, or because cutting it feels like loss, is exactly the instinct
that lets echoes survive. Cut freely. Keep a recurrence only when the recurrence itself is the
substance — for example, the firewall sentence Marge walks to the same edge "eight quarters
running" and finally cannot finish: the established pattern breaking is the whole event, so the
prior instances earn their place. That is rare. Most recurrence is scaffolding wearing a theme
as a costume.

## The keeper rule

For each cluster: keep one instance and freshly render or cut every other, so no two are alike.
The keeper is usually the first occurrence the reader meets, or the one place the beat is most
load-bearing. Once the keeper is set, every later instance is rewritten from its own scene's
specifics or removed.

## How to work a cluster

1. **Re-grep from scratch.** Grep finds candidates; it does not judge. Pull every instance
   across all twelve chapters fresh, then read each one in full context before deciding
   anything. Do not trust a prior inventory; rebuild it from the live text.
2. **Pick the keeper** by the rule above, and say why.
3. **Render or cut each other instance.** Build the replacement out of what is specific to its
   scene. On surgery-level rewrites, draft the new line for Brian before committing it.
4. **Deliver exact OLD → NEW string pairs.** Verify every OLD anchor is unique in its file
   (count == 1) before delivering; check straight-vs-curly quote encoding against the actual
   file. Brian applies the pairs in the repo.
5. **Flag, don't swallow.** Name casualties, cross-chapter ripples, and any line where the fix
   touches canon or character mode. Route content-level calls and character questions to Brian
   rather than resolving them silently.

Bump the minor version per edited file; the byline carries no version token; headers never
repeat across chapters.

## What good de-echoing looks like

- *Jasmine's report opener.* "Jasmine took her beat… eleven weeks of a dog-sized thing loose
  in her kitchen" appeared near-identically two chapters running. Keep the first; rewrite the
  second from that quarter's actual content — the household teaching the machine, beginning to
  take — so the opener carries its own chapter on its back.
- *Marge sets her drink down and watches.* Three near-identical beats in one chapter, each
  doing different work, collapsed into one construction. Rewrite each to its own moment: not
  watching the cartoons but the people they portray; the beer flat and the room waiting through
  the gap; the beer untouched while she watches the machine instead of the framework. Same
  woman, three distinct sentences.
- *The camcorder-stop.* Vary the last image to the night's fact — the cold new body and the
  warm old one and the sleeping child between them; the small new talker by the shelf — so the
  recurring close never closes the same way twice.

## Working order

Run the groups in order, A through F, and clusters top-down within each group.

Start with **Group A (scaffolding)** and **Group B (the tableau)**. They carry the worst,
most mechanical repetition, and many Group C tells live inside the same paragraphs, so settling
A and B clears a good deal of C as a side effect. Group D is mostly confirmation (the Mira
refrain is already de-templated chapter by chapter; that cluster is a check that no two closes
ring alike, not a fresh rebuild). Groups E and F are a mix of paired beats, two content-level
echoes (the retirement-floor coda; the symbiosis image), and a few one-offs.

Before resolving a cluster, get the **current post-edit version** of each chapter it touches
(working copies drift from what is applied in the repo), and make sure **ch_0, ch_1, and ch_4**
are on hand — several clusters seed in those early chapters.

## The clusters

Chapter ranges show where each lands; line numbers are established per cluster against current
files at resolution time.

### A. Retrospective scaffolding
1. **The open** — "ran the order… clade → Bramble → Trellis, vote last segment… thumb to the light, red came on." [ch_7–11, some form earlier]
2. **Clade-card handoff** — "'Clade card,' Lisa said, Bart had it out of the cigar box before she finished… the voice that sold cereal" + "Now with ___." [ch_7–11]
3. **"traced the card edge the way she had all year."** [ch_8,9,10]
4. **Handoff-to-Marge** — "looked at Marge, the handoff she makes every quarter, the mechanism turning into a feeling/person." [ch_8–12; "looked at Marge" also ch_2,5]
5. **Bramble-block handoff + Jasmine-took-her-beat** — "'Bramble block, Jasmine,' the handoff she makes every quarter" + "Jasmine took her beat… (dog-sized thing loose in her kitchen)." [handoff ch_5–11; took-her-beat ch_5,6,7,8]
6. **Palm-and-palm** — "the flat one and the standing one turning against each other… making a large thing small." [ch_9,10,11]
7. **The vote** — "the parliamentary ritual he built in the third quarter… called the vote… someone in there" + recap "stood N and N" + settled "four to nothing… carried" + "All in favor / put the standing question." [ch_5,7,8,9,10,11,12]
8. **Burns-close glass-tell** — "set the beer down, the tell — in his hand, housekeeping; on the wood, he meant to spend more… the narrator knew the shape, N behind, M to come… hands flat, then up off the wood." [ch_2,8,9,10,11]
9. **"Lisa ran the close the way she ran the open"** + files-the-miracle-and-the-housekeeping-together-under-done. [ch_9,10]
10. **Burns-open** — "up before it had finished warming, his name on the science / the deep end." [ch_8,9,10,11]

### B. The roll-call tableau
11. Household-crosses-the-threshold-inside-X's-frame. [ch_9,10,11]
12. Burns's-eye-goes-once-to-the-thing-his-son-built (the good-fossil look). [ch_7,8,9,10,11]
13. Bart-always-already-there, a sensor in his hands. [ch_9,10,11,12]
14. Lisa-checked-the-charge-once / the bramble sweating its jar / her hand near the camera, not touching. [ch_8,9,10,11]
15. Marge-has-the-juice-across-the-table-before-the-girl-wants-it. [ch_10,11]

### C. Recurring physical tells (decide a policy, then render each fresh)
16. Burns's chest-laugh, "a beat early/ahead." [ch_2,8,9,10,12]
17. Marge's two-handed grip — beer held like a teacup, fingers curled, thumbs up (pays off in the ch_10 mother's-cup reveal — protect that payoff). [ch_2,5,6,7,8,9,10]
18. Marge's beer-down = careful-sentence-loading. [ch_2,9,10,11]
19. Bart's sensor/hands-go-still tell. [ch_9,11]
20. Lisa's down-the-nose laugh, spent only on a clean structure. [ch_9,10]
21. Lisa's palms-go-still when the thing's too close to turn. [ch_11 ×2]
22. Bart's single-exhale-when-it-works. [ch_5,7]
23. Bart-doesn't-look-up-when-praised. [ch_7,8]

### D. Close & ceremony
24. **Camcorder-stop** — "Lisa let the light/tape/camera run a moment past it… and stopped it." [ch_3,6,8,9,11]
25. **Mira's closing refrain** — the kept word, "in her own voice, not the cartoon's." [ch_2,3,4,6,7,8,9,10,11] — already de-templated chapter by chapter; this is a confirm-no-two-ring-alike pass, not a rebuild.
26. **Knob-retirement ceremony + Mira's retirement line** — "the one that gets longer every quarter… Like the breathing one. And the wander one." [ch_5–11]
27. Mira-gets-there-first / understands-the-retirement-before-the-adults. [ch_5,7]
28. Mira-names-the-knobs in the treaty-signing tone. [ch_7,9,11]
29. Burns's toast where the abstract noun won't toast. [ch_8,9,10,11; deliberately broken ch_12 — leave broken]
30. Mira-asleep-against-her-mother close. [ch_6,7,8]

### E. Character moves & relational beats
31. Marge's half-step-past-the-won-point (into the part with a person under it). [ch_3,5,9,10,11]
32. Marge's dealt-≠-doomed correction, "the correction she made every time." [ch_9,10]
33. Marge's warm-low "oh, you" register, reserved for Burns and Bart. [ch_3,7,8,9,10]
34. **Shape-catches-itself formula** — "took it the way the [shape] takes everything." [ch_10 Conservator / ch_11 Planner]
35. Burns-keeping-track-of-me — "it's keeping track of me again," helpless and glad. [ch_8,9]
36. Burns-hollers-up-the-stairs / the intercom he's used twice / needs-to-be-received. [ch_8,9,11,12 — Notes-heavy]
37. Jasmine-keeps-her-counsel / not-asked / hands-quiet. [ch_7,8,9,10,11]
38. Jasmine-hand-flat-on-a-thing-to-know-it (body-knowledge register). [ch_9,10,11]
39. Bart-leaves-first / Burns-leaves-last — the post-work hour. [ch_8,9 / ch_11]

### F. Narrator conceit, reflections, images
40. Cheryl's room-pick confession — "I pick the room for the other person without examining why." [ch_5,6,7,11]
41. "The truest thing was on the tape and not in the room." [ch_9,10,11]
42. "I've watched the tape more times than the work required." [ch_8,9,10,12]
43. Cheryl-now-on-the-near-side-of-the-lens / watched-on-tape-never-in-the-flesh. [mostly ch_12]
44. Screen-honesty — "the glass was always honest / the screen told on it." [ch_9,10,11]
45. "The room went quiet… the wonder on the floor and not on the wall." [ch_11; check others]
46. Mira "kept everything / keeps them sorted." [ch_5,7,8]
47. Mira's "let it come" (Door One — recognition one-directional). [ch_9,10,11]
48. Trellis-bramble — woody, leafless, "holds the shape it was built to hold," nothing flowered. [ch_7,8,11,12]
49. **Retirement-floor coda thesis** (a retired drive = the unchosen, unfelt floor of the self) — content echo; give each a genuinely fresh expression rather than cutting either. [ch_8,10]
50. **Symbiosis image** (a cell takes in a stranger and keeps it / two things become a third) — image recurs; confirm each use does new work, and vary the rendering where it does. [ch_3,7,11,12]

## Closing a cluster

A cluster is closed when every instance has been read in current context, the keeper is set,
each other instance is freshly rendered or cut with a verified OLD → NEW pair, and any casualty
or ripple has been flagged to Brian. Move to the next cluster in order. The sweep is done when
all fifty are closed and a final re-grep surfaces no new repetition.
