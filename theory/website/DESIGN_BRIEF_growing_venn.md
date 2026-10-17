# Design brief: the growing Venn

*From the Code tool to the Design tool. Covers `Bramble Explorer.dc.html` only. Under the copy contract, Code supplies the data; build against it and send back only the `.dc.html` (plus `runtime/` if it changes).*

**Data to build against (ready now):**
- `framework-data.v2.js`: schema v2, all 20 clades and 176 cells. Generated from the Layer Map by `gen_framework_data.py`; nobody edits it by hand.
- `ui-copy.v2.js`: chrome copy with the new keys, the role glosses (`ui.roles`) and a rewritten help modal.
- `bramble-data.js`: now carries `enabled: false`.

The live site keeps loading the v1 `framework-data.js` / `ui-copy.js` until the v2 `.dc.html` lands. Code then renames the v2 files over the v1 ones, so in the design file load them under the plain names (`framework-data.js`, `ui-copy.js`). For preview, copy the v2 files in under those names.

Canon: `theory/framework/layers/Layer_Map.md`.

---

## What changed in the theory

The old Explorer drew the same four-circle, 15-region flower at all 12 clades, and each clade lit "its" new function. That model is gone.

1. **The Venn grows.** A new function is born once per **line**, not once per clade. It splits off from the center of the Venn as it stood. Every clade on a line has the same slots.
2. **There are 20 clades on four bands, not 12 on three.**
3. **Nothing is carried.** Every cell at every clade carries either its own install label or the word **owed**. A label never repeats up the line as a slate "carried" region.
4. **Functions renamed:** Modeler → **Learner**, Reviser → **Member**.
5. **The center moves by line.** It is a different cell on each line.
6. **No pair is special.** The theory has six pairs and no "adjacent" or "opposite" ones, so the two signature mini-venns have no basis.

---

## 1. The growing flower (1 / 3 / 7 / 15)

| Stage | Where | Circles | Regions | The center cell |
|---|---|---|---|---|
| 0 | Prework (below the rail, not a stop) | 1 | 1 | — |
| 1 | Genetic line, 7 clades | Effector, Regulator | 3 | **Controller** (E×R) |
| 2 | Nemetic line, 5 clades | + Learner | 7 | **Conservator** (E×R×Le) |
| 3 | Memetic line, 8 clades (symbolic + digital) | + Member | 15 | **Translator** (all four) |

- **Genetic:** two overlapping circles. Their lens is the lit center.
- **Nemetic:** a standard three-circle Venn. The triple region is the lit center, and the three lenses are the pairs Controller, Anticipator and Connector.
- **Memetic:** a **true four-set Venn**, meaning four congruent ellipses rotated around a common center (Venn's own construction), so that all 15 regions exist in one figure. The current cross layout (`ELL`) cannot do this: E∩Le-only and R∩Me-only have no region of their own. That gap is why the signature lanes existed. With a true four-set Venn, two of the six pairs have to sit across the middle. **Which two is arbitrary and means nothing**, so pick the one that reads best and don't style those two differently.
- **Line transitions:** when the reader steps across a line boundary (Metazoa→Eumetazoa, Primate→Band), the new circle should be seen **growing out of the center**: it emerges from the old center region and swings out to its place. Within a line, stepping between clades changes the labels only, never the geometry.
- **Lit state:** the old `cell.newSlot` per-clade lighting is gone. Light `cell.center`, the clade's center region; it holds the clade's breakthrough. At a line's founding clade (`cell.founds` is set), give the newborn circle its function color. At later clades on the same line, how much of that color it keeps is your call, but don't let it read as "new at this clade".
- **Colors:** keep `FC`/`BRIGHT`, remapped: Effector red, Regulator blue, **Learner** yellow (was Modeler), **Member** green (was Reviser).

## 2. The rail: 20 clades on four bands

Index 0 is the oldest clade.

| Band | Clades |
|---|---|
| **Genetic** (brown) | RNA World · Ribocyte · Progenote · LUCA · Prokaryote · Eukaryote · Metazoa |
| **Nemetic** (blue; was "neuronal") | Eumetazoa · Bilaterian · Vertebrate · Mammal · Primate |
| **Memetic, symbolic** (purple) | Band · Settlement · City · Empire |
| **Memetic, digital** (new tint) | Computer · Network · Model · Agent |

- Symbolic and digital are both **memetic** and share the 15-slot Venn. Group them under one memetic bracket with two sub-bands. The digital founding is a change of medium, not a birth, so no new circle appears at Computer.
- `y = 700 - i*58` assumes 12 rungs. Fit 20 rungs by tightening the spacing or letting the rail scroll, whichever you prefer. The mobile horizontal rail just gets longer.
- **The trellis rods should start where each function is born.** The woody trunk below RNA World *is* the prework, a single process. At RNA World it splits into the Effector and Regulator rods. The Learner rod starts at Eumetazoa and the Member rod at Band. Today all four rods run the full height. The existing soil bed and trunk are a natural home for the prework; one caption line is enough there ("Prework: chemistry that keeps itself going, with no store").
- **Archaeon is retired as a clade.** Archaea now sit inside Prokaryote. Eumetazoa moves from the genetic band to found the nemetic one. LUCA was groundwork and is now a clade.
- **Unruled clades:** all four digital clades carry `ruled: false`. Their labels are placeholders, and the map says a reader takes nothing from them. Draw their Venn, but render the labels as clearly provisional (muted, plus an "UNRULED" stamp or similar). They must not look like results.

## 3. Per-line centers

Light the region named by `cell.center`, never a hardcoded slot. The center label is the clade's breakthrough. In Function mode it shows the center's role name (Controller / Conservator / Translator). In the left-panel meta, append the slot count, e.g. `NEMETIC LINE · CLADE 09 · 7-SLOT VENN`.

## 4. Settings, owed and claimants

A region carries one of three kinds of content:

- **An install label** (the normal case).
- **Settings.** A setting is a dial on that cell's loop, not a separate operation. Examples: Bilaterian Effector = Locomotion + Impetus, Temperament, Inhibition; Primate center = Self-Model + Standing, Sociometer, Affiliation. Show the install as the region label. Show settings in the right panel as a small list under their own heading (`ui.settings`). In the flower itself, at most a small mark showing that settings exist; the 15-slot regions are too small for more. Some cells have up to five settings.
- **Owed.** The install is still to be found (`owed: true`, `label: null`). This is real, frequent content: 6 of 15 at Settlement, 7 at City. Render it as a deliberate empty state, such as an outlined or hatched region with *owed* in italics, and keep it clickable. The panel explains it in one line (`ui.owedExplainer`). Don't hide owed regions, and don't style them like errors.
- **Claimants.** No cell has claimants right now, but the schema allows a `claimants: []` list (rival labels a session still has to choose between). If present, show the incumbent and say "+N claimants". Low priority.

## 5. Remove

- **The signature mini-venns:** the `withSig` lanes, `mini()`, `crest`, `sig.*` slot handling, and the **Signature** legend entry with `pickSignature`.
- The legend's region types. **Motivation / Tendency / Capacity / Breakthrough** become **Single / Pair / Triple / Center** (`ui.single`, `ui.pair`, `ui.triple`, `ui.center`). The old Motivation labels such as Persistence, Impetus and Mastery are now *settings*, not single-slot types.
- `NEWFN_TO_TND`, `SLOT_FN`, the sticker logic tied to `newSlot`, and `INSTALL = {effector:[0,4,8],…}`. These encode "one new function per clade × 12 clades".
- **The "THE VIRTUOUS CYCLE" panel section.** Replace it with **THE LINE TEST** (`cell.lineTest`). Each line has one test: genetic, survival and reproduction under finite carrying capacity; nemetic, the outcome of expressed behavior; memetic, uptake.

## 6. The Bramble panel: hide it for this release

The knob board maps 12 knobs onto 12 clade indices through `INSTALL`. With 20 clades and per-line births it would show wrong knobs. Gate the Ancestor/Bramble toggle on `window.BRAMBLE_UNIT.enabled === true`. Code will ship `enabled: false` until the book side settles how knobs map to the growing Venn. Keep the panel code itself; just don't show the toggle.

## 7. Specimens

New ids with no art yet: `rnaworld`, `ribocyte`, `progenote`, `luca`, `metazoa`, `computer`, `network`, `model`, `agent`. Until art arrives, use the existing "NO SPECIMEN ON FILE / AWAITING FIELD CAPTURE" fallback. Drop `archaeon` from `SPECIMEN`. Keep the map's exact shape (`id: 'public/specimens/<id>.<ext>'`). `build_site.py` rewrites those paths, and Code will update its guard counts.

---

## Data contract: `framework-data.js` schema v2

```js
window.BRAMBLE_FRAMEWORK = {
  schema: 2,
  functions: [            // the circles, in birth order
    { id: "effector",  born: null },        // the prework renamed; present from RNA World
    { id: "regulator", born: "rnaworld" },
    { id: "learner",   born: "eumetazoa" },
    { id: "member",    born: "band" }
  ],
  lines: [
    { id: "genetic",  slots: 3,  center: "p.controller",  test: "…" },
    { id: "nemetic",  slots: 7,  center: "t.conservator", test: "…" },
    { id: "symbolic", slots: 15, center: "c.translator",  test: "…", group: "memetic" },
    { id: "digital",  slots: 15, center: "c.translator",  test: "…", group: "memetic" }
  ],
  regionSlots: [          // all 15; fns = the circles the region lies inside
    { id: "s.effector",    type: "single", fns: ["effector"] },
    { id: "s.regulator",   type: "single", fns: ["regulator"] },
    { id: "s.learner",     type: "single", fns: ["learner"] },
    { id: "s.member",      type: "single", fns: ["member"] },
    { id: "p.controller",  type: "pair",   fns: ["effector","regulator"] },
    { id: "p.anticipator", type: "pair",   fns: ["regulator","learner"] },
    { id: "p.connector",   type: "pair",   fns: ["effector","learner"] },
    { id: "p.adapter",     type: "pair",   fns: ["learner","member"] },
    { id: "p.operator",    type: "pair",   fns: ["regulator","member"] },
    { id: "p.starter",     type: "pair",   fns: ["effector","member"] },
    { id: "t.conservator", type: "triple", fns: ["effector","regulator","learner"] }, // no Member
    { id: "t.herald",      type: "triple", fns: ["effector","regulator","member"] },  // no Learner
    { id: "t.counselor",   type: "triple", fns: ["regulator","learner","member"] },   // no Effector
    { id: "t.tester",      type: "triple", fns: ["effector","learner","member"] },    // no Regulator
    { id: "c.translator",  type: "center", fns: ["effector","regulator","learner","member"] }
  ],
  cells: [
    {
      id: "bilaterian", index: 8, name: "Bilaterian", line: "nemetic",
      date: "~550 MYA", era: "…", coincidingEvent: "…",
      founds: null,               // function id born here, e.g. "learner" at eumetazoa
      center: "t.conservator",    // same as the line's; repeated so the renderer reads one field
      ruled: true,                // false at the four digital clades
      clade: "…prose…",
      regions: {                  // only the slots that exist on this line
        "s.effector": { label: "Locomotion", owed: false,
                        settings: ["Impetus", "Temperament", "Inhibition"],
                        claimants: [], panel: { title, body, links: [...] } },
        "s.learner":  { label: "Potentiation", owed: false, settings: [], panel: {...} },
        "p.anticipator": { label: "Expectation", ... },
        // an owed cell:
        // "p.anticipator": { label: null, owed: true, settings: [], panel: { title: "Anticipator", body: "…" } }
      }
    }
  ]
};
```

Rules the renderer can rely on:

- A slot exists at a clade **if and only if** its id is a key in `cell.regions`. Draw only the circles whose `functions[].born` index is at or below the current clade.
- `label` is null exactly when `owed` is true.
- Function mode shows the role name derived from the slot id (`p.controller` → "Controller"). The role glosses stay in your `ROLES` table; Code will send the new gloss wording as `ui-copy.js` keys.

## New `ui-copy.js` keys (shipped in `ui-copy.v2.js`)

Also added: `roles.<id>.{name,gloss}` for all 15 roles, `genetic`, `symbolic`, `lineSuffix`, `cladeWord`, `settingsExplainer`, `claimants`, `founds`, `references`.

`single`, `pair`, `triple`, `center`, `settings`, `owed`, `owedExplainer`, `unruled`, `unruledExplainer`, `lineTest`, `prework`, `preworkCaption`, `learner`, `member`, `memetic`, `nemetic`, `digital`, `slotsSuffix` ("-SLOT VENN"). Removed: `modeler`, `reviser`, `motivation`, `tendency`, `capacity`, `breakthrough`, `signature` and `virtuousCycle`. The help-modal strings are rewritten. If a layout needs a string that isn't on this list, ask for the key. Don't hardcode it.

## Done looks like

- Stepping RNA World → Agent shows the flower at 3, then 7, then 15 regions. A circle grows out of the center at Eumetazoa and again at Band, and nowhere else.
- The lit center is the Controller lens on the genetic band, the triple region on the nemetic band, and the four-way center on the memetic band.
- Owed regions are visibly empty and clickable. Settings appear in the panel. The digital clades read as unruled.
- There are no signature lanes. The legend reads Single / Pair / Triple / Center plus four function chips. Desktop and mobile both work.
