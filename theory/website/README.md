# Handoff: Explorer — Lab poles wired into the knob readout card

Target repo: **bkuhlman80/abhop-explorer** (branch `main`). Path under `trellis-site/`.

## What ships
**`trellis-site/Bramble Explorer.dc.html`** only (Design-owned). No data files in this bundle — `bramble-data.js` / `ui-copy.js` / `framework-data.js` are Code-owned; your corrected copies are the source of truth.

Changes since last ship:
- **Lab poles surfaced** in the knob readout card, reading the existing `labUp` / `labDown` / `ui.labPoles` keys (no new keys needed):
  - Meta row gains a third item: `Lab · engaged ↔ disengaged` (alongside Motivation and Board label).
  - Each Up/Down pole row shows the Lab-register word in small type under the Mira name.
- Design's local `bramble-data.js` was synced to your 7 canon fixes (Neuroticism/Curiosity swap, Lab-pole corrections) so previews here match production — nothing to pull from us on the data side.

## Needs data sync (Code-owned `framework-data.js` — no file shipped, per contract)
The Neuroticism/Curiosity swap + label corrections applied to `bramble-data.js` have NOT landed in `framework-data.js`, so the middle-panel flower disagrees with the knob card. Stale region labels (cell / slot):
- `Chronotype` → **Orienting Style**: bilaterian, vertebrate, mammal @ `tnd.explorer`
- `Experiencing Style` → **Neuroticism**: mammal, primate, band @ `tnd.anticipator`
- `Neuroticism` → **Curiosity**: band, settlement, city @ `tnd.explorer`
(Please verify the carried-cell cascade against the master table before applying — Design lists what renders stale, Code owns the canon.)

## Commit & push
```bash
git add trellis-site/Bramble\ Explorer.dc.html
git commit -m "feat(explorer): surface Lab poles in knob readout card"
git push origin main
```
Cloudflare Pages rebuilds on push (`node build.mjs` → `dist/`).
