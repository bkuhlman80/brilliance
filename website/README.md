# Trellis Framework website

Deployed to `trellis-framework.pages.dev` via `wrangler` (not git). The live
bundle is assembled by `build_site.py` into `site/`, then pushed.

## Two-tool copy contract (read before editing anything here)

This site is worked on by two tools with a hard division of labor. The whole
point of the split is to stop copy drift, where one tool's handoff silently
overwrites the other's words. Obey the ownership table and the drift never
happens.

### Who owns what

| File | Owner | Contains |
|------|-------|----------|
| `framework-data.js` | **Code tool** | all cell/region prose — body text, virtuous-cycle, badges, statuses, per-cell slot labels |
| `ui-copy.js` | **Code tool** | all chrome microcopy — wordmark, section headers (LABELS, TRELLIS FUNCTION, MENTAL MODULES, THE VIRTUOUS CYCLE, DRAFT PROSE), button labels, the settings paragraph |
| `Bramble Explorer.dc.html` | **Design tool** | structure, layout, styling, look & feel. Reads every string from the data files; **hardcodes none** |
| `build_site.py` | **Code tool** | build; copies both data files into `site/` |
| `runtime/` (support.js, icons, manifest) | Design / shared | ships in the Design handoff when changed |

### The two rules that enforce it

1. **The Code tool never opens `Bramble Explorer.dc.html`.** All words it needs
   to change live in `framework-data.js` or `ui-copy.js`.
2. **The Design tool never ships `framework-data.js` or `ui-copy.js`.** Its
   handoff is the `.dc.html` alone (plus `runtime/` if it changed). The Code
   tool integrates by taking *only* the `.dc.html`, then runs `build_site.py`
   and deploys. Because build + deploy belong to the Code tool, a stale data
   file in a Design bundle physically cannot reach production.

Merges are always "take both files," never "overwrite."

### Schema changes (the one coordination point)

Design owns the *shape*; the Code tool owns the *words that fill it*. If a design
change adds a new slot, cell, region, or chrome label, Design cannot ship the
data for it. Instead the handoff note says **"needs new key `X`"** and the Code
tool adds `X` to the appropriate data file. Never resolve this by having Design
ship a data file.

### Deploy flow

```
Design hands off Bramble Explorer.dc.html (+ runtime/ if changed)
  → Code tool drops in that one file, touches nothing else
  → python3 build_site.py
  → wrangler pages deploy website/site --project-name trellis-framework --branch main
```
