#!/usr/bin/env python3
"""Build the deployable Trellis Framework site from the design-canvas source.

Reads `Bramble Explorer.dc.html` (the Claude Design export), applies the
deploy transformations, and assembles the upload bundle in `site/`:

  index.html          — the .dc.html + responsive wrapper + web specimen paths
  support.js          — dc-runtime (vendored in runtime/)
  framework-data.js   — data file (source of truth for labels/prose)
  favicon/og assets   — vendored in runtime/
  public/specimens_web/*.jpg

Deploy with:
  wrangler pages deploy website/site --project-name trellis-framework --branch main
"""

import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "Bramble Explorer.dc.html"
RUNTIME = HERE / "runtime"
OUT = HERE / "site"

RESPONSIVE_STYLE = """<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style id="bx-responsive">
  html, body { margin:0; background:#1b1813; }
  body { overflow-x:hidden; }
  #bx-canvas { padding:0 !important; gap:0 !important; background:#1b1813 !important; width:auto !important; min-width:0 !important; min-height:100dvh !important; }
  /* hide the design-canvas frame labels */
  #bx-desktop > div:first-child, #bx-mobile > div:first-child { display:none !important; }
  /* one layout per device — desktop on wide screens, mobile on phones */
  @media (min-width:821px) {
    #bx-mobile { display:none !important; }
    #bx-desktop-frame { width:100vw !important; height:100dvh !important; box-shadow:none !important; }
  }
  @media (max-width:820px) {
    #bx-desktop { display:none !important; }
    #bx-mobile-frame { width:100vw !important; height:100dvh !important; box-shadow:none !important; }
  }
</style>"""

# (needle, replacement, expected occurrence count)
EDITS = [
    # viewport meta -> viewport-fit + injected responsive style block
    ('<meta name="viewport" content="width=device-width, initial-scale=1">',
     RESPONSIVE_STYLE, 1),
    # anchor ids for the responsive CSS
    ('<div style="min-width:100%; min-height:100vh; width:max-content;',
     '<div id="bx-canvas" style="min-width:100%; min-height:100vh; width:max-content;', 1),
    ('DESKTOP ==================== -->\n  <div style="flex:none;">',
     'DESKTOP ==================== -->\n  <div id="bx-desktop" style="flex:none;">', 1),
    ('MOBILE ==================== -->\n  <div style="flex:none;">',
     'MOBILE ==================== -->\n  <div id="bx-mobile" style="flex:none;">', 1),
    ('<div data-screen-label="Explorer — Desktop"',
     '<div id="bx-desktop-frame" data-screen-label="Explorer — Desktop"', 1),
    ('<div data-screen-label="Explorer — Mobile"',
     '<div id="bx-mobile-frame" data-screen-label="Explorer — Mobile"', 1),
]


def build() -> None:
    html = SRC.read_text(encoding="utf-8")

    for needle, replacement, expected in EDITS:
        n = html.count(needle)
        if n != expected:
            sys.exit(f"ABORT: expected {expected} occurrence(s) of {needle[:60]!r}, found {n} — "
                     "the design file changed shape; update build_site.py.")
        html = html.replace(needle, replacement)

    # specimen images: design-canvas paths -> web-optimized jpgs
    start = html.index("const SPECIMEN = {")
    end = html.index("};", start)
    block = html[start:end]
    fixed = block.replace("public/specimens/", "public/specimens_web/").replace(".png'", ".jpg'")
    html = html[:start] + fixed + html[end:]

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / "index.html").write_text(html, encoding="utf-8")
    for name in ("support.js", "favicon-32.png", "apple-touch-icon.png", "og-image.png", "_redirects"):
        shutil.copy2(RUNTIME / name, OUT / name)
    shutil.copy2(HERE / "framework-data.js", OUT / "framework-data.js")

    spec_out = OUT / "public" / "specimens_web"
    spec_out.mkdir(parents=True)
    jpgs = sorted((HERE / "specimens_web").glob("*.jpg"))
    if len(jpgs) != 12:
        sys.exit(f"ABORT: expected 12 specimen jpgs, found {len(jpgs)}")
    for jpg in jpgs:
        shutil.copy2(jpg, spec_out / jpg.name)

    total = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file())
    print(f"built {OUT} — {sum(1 for f in OUT.rglob('*') if f.is_file())} files, {total/1024:.0f} KiB")


if __name__ == "__main__":
    build()
