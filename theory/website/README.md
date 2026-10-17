# Trellis Framework website

The Explorer at **trellis-framework.pages.dev**, a Cloudflare Pages project called `trellis-framework`.

## Who owns what

Two tools build this site. The split between them stops their copies drifting apart.

| File | Owner | Holds |
|---|---|---|
| `Bramble Explorer.dc.html` | Design tool | Look and feel. Reads every string from the data files and hardcodes none. |
| `framework-data.js` | Code tool | Clades, cell labels, panel prose, science links |
| `ui-copy.js` | Code tool | Interface wording: legend, panel headings, help modal |
| `bramble-data.js` | Code tool | The Bramble (Unit 03) panel |
| `runtime/` | Code tool | `support.js` (the dc-runtime), icons, `_redirects` |

Rules:

- The Code tool never edits the `.dc.html`.
- When a Design handoff arrives, take **only** the `.dc.html` (plus `runtime/` if it changed). Never copy in the bundle's data files. Doing that once reverted Impetus→Boldness (commit `e939769`).
- If a design needs a new string, the Code tool adds the key to a data file. Design never ships data to supply it.

## Where the words come from

The labels come from the theory, at `theory/framework/layers/Layer_Map.md`. `gen_framework_data.py` parses the Layer Map into `framework-data.v2.js` and checks the slot rules. Edit the Layer Map and regenerate; don't hand-edit the output.

```bash
python3 theory/website/gen_framework_data.py
```

## Migration in progress: the growing Venn

The theory moved from a fixed four-circle Venn at 12 clades to a Venn that grows (3, then 7, then 15 slots) across 20 clades. [DESIGN_BRIEF_growing_venn.md](DESIGN_BRIEF_growing_venn.md) is the handoff to the Design tool and specifies the v2 data schema.

Until the v2 `.dc.html` lands, the live site keeps loading the v1 `framework-data.js` and `ui-copy.js`. When it lands:

1. Rename `framework-data.v2.js` → `framework-data.js` and `ui-copy.v2.js` → `ui-copy.js`.
2. Update the `SPECIMEN` path rewrite in `build_site.py` and its guard counts, to match the new design file.
3. Build, check desktop and mobile locally, then deploy.

## Build and deploy

```bash
python3 theory/website/build_site.py
```

```bash
wrangler pages deploy theory/website/site --project-name trellis-framework --branch main
```

The deploy is a direct upload. The site is **not** connected to git, so pushing a commit changes nothing live. `build_site.py` writes the upload bundle to `site/`. To preview locally, serve `site/` (launch.json has a `trellis-site` config on port 8899).

Specimen images: full-size originals live in `specimen/`, web-optimized `.jpg`s in `specimens_web/`.
