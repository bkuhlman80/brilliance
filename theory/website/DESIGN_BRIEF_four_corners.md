# Design brief: Four Corners

*From the Code tool to the Design tool. Covers `Four Corners.dc.html`, a second artboard beside `Bramble Explorer.dc.html`, and the one place the Explorer should link to it. Under the copy contract, Code supplies the strings; build against them and send back only the `.dc.html` files (plus `runtime/` if an export's runtime changes).*

**What is already in place:**
- `Four Corners.dc.html` in the website folder, served at `/four-corners/`. It is the export of the Four Corners canvas, the file the Design tool edits.
- `runtime/four-corners/`: the dc-runtime that export ships with (`support.js` plus `vendor/react.js` and `vendor/react-dom.js`). It is newer than the Explorer's `support.js` and the two are not interchangeable; each page keeps its own.
- `build_site.py` builds both routes. The Explorer's build is unchanged.
- `ui-copy.js` and `ui-copy.v2.js` carry the new keys listed at the end, for the cross-links and a help-modal section.

Canon for the figure: the growing-Venn treatment in `theory/framework/core/`.

---

## What Four Corners is

The theory's central visual metaphor for the growing Venn. It answers the question the Explorer's flower cannot: why there are 3, then 7, then 15 slots, and why no pair is special.

**A function is a corner. Every birth opens a dimension.** The four functions are the corners of a pyramid, and the slots are its faces of every dimension:

| Stage | Figure | Corners | Edges | Faces | Solid | Slots | The whole, which is the center |
|---|---|---|---|---|---|---|---|
| 0 | a point | 1 | 0 | 0 | 0 | 1 | Process |
| 1 · genetic | a line | 2 | 1 | 0 | 0 | 3 | Body |
| 2 · nemetic | a triangle | 3 | 3 | 1 | 0 | 7 | Workspace |
| 3 · memetic | a pyramid (tetrahedron) | 4 | 6 | 4 | 1 | 15 | Translator |

- Singles are corners, pairs are edges, triples are the triangular faces, the center is the solid interior.
- Each new corner **rises out of the center of the figure as it stands** and lifts the figure into a new dimension. Point, line, plane, space. This is "the newborn function splits off from the center," drawn literally.
- When a corner rises past the old whole, the old whole becomes a boundary face of a bigger whole and is renamed for what it keeps doing: Process becomes Effector, Body becomes Controller, Workspace becomes Conservator.
- Nothing older is lost: the line is still an edge of the triangle, the triangle is still a face of the pyramid.
- The figure is fully symmetric. The six pairs are six identical edges; nothing is inner, outer, adjacent or opposite. This is the geometric fact behind the brief's rule that no pair is special.
- The empty subset has no geometry, so there is no "nothing" corner to explain away.

The page has four parts: the figure (a drawn canvas: orbit by drag, hover or tap a name), a stage control (Rise button, Back, a scrubber that freezes mid-rise), the reading column (stage title, stage text, counts, the slot list with the newborns and the renamed one marked), and a hover card for any slot (name, composition, kind of face, the line it was born on, its old name if it was ever the whole).

Function colors are the Explorer's: Effector red, Regulator blue, Learner yellow, Member green. Edges are gradients between their two corners; faces are tinted blends of their three.

## How the Design tool works on it

- **Treat the Four Corners canvas as the source of truth** and `Four Corners.dc.html` as its export. A handoff is the exported artboard renamed to `Four Corners.dc.html`. Keep the two `vendor/` script lines in its head; the site build relies on them. If the export's runtime changes, the new `support.js` and `vendor/` go in `runtime/four-corners/`, never in `runtime/`.
- **The figure is code, not markup.** The pyramid is drawn on a `<canvas>` by the artboard's logic class. The properties panel can restyle the frame around it; it cannot drag a corner or edit a name in the figure. Don't try to rebuild it as placed elements. The geometry is the theory, and hand-nudging it would make the picture lie.
- **Tweaks:** a dark/light switch (dark is the site look and the default) and the four function colors. Keep the function colors in step with the Explorer's `FC` / `BRIGHT` map; if one changes there, change it here.
- **Copy:** Four Corners is the one named exception to the rule that Design ships no words. Its stage texts and headline live in the artboard as literal copy, editable in place, because they are the theory's argument and will be revised against the figure. If the wording stabilizes, Code moves it to a `four-corners-copy.js` and the page reads it as holes like the Explorer does. Until then, edit the words on the canvas and hand off the file.
- **Layout:** it is a PAGE (fluid root, `expand: fill`), 1280×760 in the frame, and it stacks to one column at phone width: figure, controls, then the reading column. Keep it fluid; the site shows it at any width.
- **Don't verify by rebuilding the site.** Code builds and deploys. Send the file.

## Integrating with the Explorer

Two links and one help section, all from existing keys. No new strings in the design file.

1. **A link from the Explorer to Four Corners**, in the masthead or beside the help button, reading `{{ ui.fourCorners }}` and pointing at `{{ ui.fourCornersHref }}` (`/four-corners/`). Use a real `<a href>` with the site's link styling; it opens the page in the same tab. `{{ ui.fourCornersBlurb }}` is a one-line tooltip or caption if there is room. Put it on both the desktop and the mobile frame.
2. **A section in the help modal**, after THE TRELLIS FUNCTION and before REGION TYPES: heading `{{ ui.helpFourCornersH }}`, body `{{ ui.helpFourCornersPD }}` on desktop and `{{ ui.helpFourCornersPM }}` on mobile, in the same styling as the other sections.
3. **A way back from Four Corners.** The page currently has no site chrome. Add a small masthead line above the figure, in the site's monospace eyebrow style: the brand on the left, and on the right a link reading "Back to the Explorer" pointing at `/`. This is the one string the page hardcodes for now, under the copy exception above; it matches `ui.fourCornersBack` so it can be swapped for the hole later.

## The relation to the flower: keep both

The flower stays the reading surface. It shows 176 cells, one clade at a time, with their installs, settings and owed states. Four Corners is the explainer: why those cells exist in those numbers. The two should link to each other and should not try to do each other's job. In particular, the Explorer's line transitions (the new circle growing out of the center at Eumetazoa and at Band) are the flower's own version of the rise; let them rhyme with Four Corners in timing and feel, but don't put a pyramid inside the flower.

This is the Code tool's recommendation, not a ruling. If the author decides the pyramid should replace the flower as the Explorer's figure, that is a new brief.

## Not in scope

- No per-clade content in Four Corners. It shows functions and slots, not installs. If a reader wants Locomotion or Potentiation they go to the Explorer.
- No Bramble panel, no specimen art, no rail.
- No signature lanes or any other construct the growing-Venn brief retires.

## New `ui-copy.js` keys (shipped in both `ui-copy.js` and `ui-copy.v2.js`)

`fourCorners`, `fourCornersBlurb`, `fourCornersHref`, `fourCornersBack`, `helpFourCornersH`, `helpFourCornersPD`, `helpFourCornersPM`.

If a layout needs a string that isn't on this list, ask for the key. Don't hardcode it.

## Done looks like

- `/` has a visible way to reach Four Corners on desktop and mobile, and its help modal explains in one section what the page is for.
- `/four-corners/` has a way back to the Explorer and otherwise looks like the same site: same ground, same cream, same amber links, same function colors as the flower.
- Stepping Point → Space on Four Corners shows a point, a line, a triangle and a pyramid, each corner rising out of the center of the figure before it, with the center label always on top and the corner labels always visible.
