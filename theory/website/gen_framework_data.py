#!/usr/bin/env python3
"""Generate framework-data.v2.js (schema v2, the growing Venn) from the Layer Map.

Source of truth: theory/framework/layers/Layer_Map.md. The labels, owed cells,
settings, dates and clade prose all come from it. Panel bodies are the Layer
Map sentences that name each label, pulled out automatically, so every panel is
marked draft. Science links from the v1 data file are kept wherever the same
label sits at the same clade.

    python3 theory/website/gen_framework_data.py          # writes framework-data.v2.js
    python3 theory/website/gen_framework_data.py --check  # parse and validate only
    python3 theory/website/gen_framework_data.py --out ../trellis-site/explorer/framework-data.v2.js

Schema and renderer rules: DESIGN_BRIEF_growing_venn.md.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LAYER_MAP = HERE.parent / "framework" / "layers" / "Layer_Map.md"
V1_DATA = HERE / "framework-data.js"
OUT = HERE / "framework-data.v2.js"

# ---------------------------------------------------------------- structure

FUNCTIONS = [
    {"id": "effector", "born": None},
    {"id": "regulator", "born": "rnaworld"},
    {"id": "learner", "born": "eumetazoa"},
    {"id": "member", "born": "band"},
]

LINE_TESTS = {
    "genetic": "Survival and reproduction under finite carrying capacity.",
    "nemetic": "The outcome of expressed behavior: a route kept by being re-met, scored inside the unit from where scoring installs.",
    "symbolic": "Uptake: taken up and retold.",
    "digital": "Uptake: in the digital medium, run and kept.",
}

LINES = [
    {"id": "genetic", "slots": 3, "center": "p.controller", "store": "gene", "group": None},
    {"id": "nemetic", "slots": 7, "center": "t.conservator", "store": "neme", "group": None},
    {"id": "symbolic", "slots": 15, "center": "c.translator", "store": "meme", "group": "memetic"},
    {"id": "digital", "slots": 15, "center": "c.translator", "store": "meme", "group": "memetic"},
]
for ln in LINES:
    ln["test"] = LINE_TESTS[ln["id"]]
LINE_BY_ID = {ln["id"]: ln for ln in LINES}

REGION_SLOTS = [
    ("s.effector", "single", ["effector"]),
    ("s.regulator", "single", ["regulator"]),
    ("s.learner", "single", ["learner"]),
    ("s.member", "single", ["member"]),
    ("p.controller", "pair", ["effector", "regulator"]),
    ("p.anticipator", "pair", ["regulator", "learner"]),
    ("p.connector", "pair", ["effector", "learner"]),
    ("p.adapter", "pair", ["learner", "member"]),
    ("p.operator", "pair", ["regulator", "member"]),
    ("p.starter", "pair", ["effector", "member"]),
    ("t.conservator", "triple", ["effector", "regulator", "learner"]),
    ("t.herald", "triple", ["effector", "regulator", "member"]),
    ("t.counselor", "triple", ["regulator", "learner", "member"]),
    ("t.tester", "triple", ["effector", "learner", "member"]),
    ("c.translator", "center", ["effector", "regulator", "learner", "member"]),
]
SLOT_BY_ROLE = {sid.split(".")[1]: sid for sid, _, _ in REGION_SLOTS}

# Layer Map heading -> (id, line). Order here is rail order, oldest first.
CLADES = [
    ("RNA World", "rnaworld", "genetic"),
    ("Ribocyte", "ribocyte", "genetic"),
    ("Progenote", "progenote", "genetic"),
    ("LUCA", "luca", "genetic"),
    ("Prokaryote", "prokaryote", "genetic"),
    ("Eukaryote", "eukaryote", "genetic"),
    ("Metazoa", "metazoa", "genetic"),
    ("Eumetazoa", "eumetazoa", "nemetic"),
    ("Bilaterian", "bilaterian", "nemetic"),
    ("Vertebrate", "vertebrate", "nemetic"),
    ("Mammal", "mammal", "nemetic"),
    ("Primate", "primate", "nemetic"),
    ("Band-Human", "band", "symbolic"),
    ("Settlement-Human", "settlement", "symbolic"),
    ("City-Human", "city", "symbolic"),
    ("Empire-Human", "empire", "symbolic"),
    ("Computer", "computer", "digital"),
    ("Network", "network", "digital"),
    ("Model", "model", "digital"),
    ("Agent", "agent", "digital"),
]
FOUNDS = {"rnaworld": "regulator", "eumetazoa": "learner", "band": "member"}

# Era-table row name -> clade id (the table pluralizes some names).
ERA_NAMES = {
    "RNA World": "rnaworld", "Ribocyte": "ribocyte", "Progenote": "progenote", "LUCA": "luca",
    "Prokaryotes": "prokaryote", "Eukaryotes": "eukaryote", "Metazoa": "metazoa",
    "Eumetazoa": "eumetazoa", "Bilaterians": "bilaterian", "Vertebrates": "vertebrate",
    "Mammals": "mammal", "Primates": "primate", "Bands": "band", "Settlements": "settlement",
    "Cities": "city", "Empires": "empire",
}

# "What each clade name covers" bullet lead -> clade id.
COVER_NAMES = {
    "RNA World": "rnaworld", "Ribocyte": "ribocyte", "Progenote": "progenote", "LUCA": "luca",
    "Prokaryote": "prokaryote", "Eukaryote": "eukaryote", "Metazoa": "metazoa",
    "Eumetazoa": "eumetazoa", "Bilaterian": "bilaterian", "Mammal": "mammal",
    "Band": "band", "Settlement": "settlement", "City": "city", "Empire": "empire",
}

# Rail dot colors for clades the v1 file never had, tinted by band.
NEW_COLORS = {
    "rnaworld": "#9c7a4e", "ribocyte": "#a5834f", "progenote": "#ad8c55", "luca": "#b5955b",
    "metazoa": "#8e6c45", "computer": "#4f8f86", "network": "#4a8a9a",
    "model": "#4f7fa8", "agent": "#5b74b0",
}

# ---------------------------------------------------------------- parsing helpers

ABBREV = re.compile(r"(?:\bal|\bvs|\be\.g|\bi\.e|\b[A-Z]|\bc|\bca|\bSt|\bDr|\bp)$")


def strip_md(text):
    return re.sub(r"\*+", "", text).strip()


def sentences(text):
    """Split prose into sentences without breaking on 'et al.' or initials."""
    out, start = [], 0
    for m in re.finditer(r"[.!?](?=\s+[A-Z(\"'])", text):
        head = text[start:m.start()]
        if ABBREV.search(head.rstrip()):
            continue
        out.append(text[start:m.end()].strip())
        start = m.end()
    tail = text[start:].strip()
    if tail:
        out.append(tail)
    return out


def split_layer(raw):
    """'Locomotion · Impetus (setting) · Temperament (setting)' -> label, settings, claimants."""
    raw = raw.replace("†", "").strip()
    if raw.lower() == "owed":
        return None, [], []
    parts = [p.strip() for p in raw.split("·") if p.strip()]
    label, settings, claimants = None, [], []
    for p in parts:
        if p.endswith("(setting)"):
            settings.append(p[: -len("(setting)")].strip())
        elif label is None:
            label = p
        else:
            claimants.append(p)
    return label, settings, claimants


def mentions(sentence, name):
    """Whole-word, case-sensitive match that is not the head of a longer hyphenated label."""
    return re.search(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", sentence) is not None


def section(md, title):
    m = re.search(r"^## " + re.escape(title) + r"\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    if not m:
        sys.exit(f"Layer Map: section '## {title}' not found")
    return m.group(1)


def parse_eras(md):
    eras = {}
    for row in section(md, "Eras and coinciding events").splitlines():
        cols = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cols) == 4 and cols[0] in ERA_NAMES:
            eras[ERA_NAMES[cols[0]]] = {"date": cols[1], "era": cols[2], "coincidingEvent": cols[3]}
    return eras


def parse_covers(md):
    covers = {}
    for line in section(md, "What each clade name covers").splitlines():
        if not line.startswith("- "):
            continue
        for m in re.finditer(r"\*\*(.+?)\*\* names (.+?)(?=\s\*\*|$)", line):
            if m.group(1) in COVER_NAMES:
                covers[COVER_NAMES[m.group(1)]] = strip_md(m.group(1) + " names " + m.group(2))
    return covers


def parse_clades(md):
    venn = section(md, "The Venn at each clade")
    digital_note = None
    m = re.search(r"### Memetic line, digital medium.*?\n\s*\n\*(.+?)\*\s*\n", venn, re.S)
    if m:
        digital_note = strip_md(m.group(1))
    blocks = {}
    for m in re.finditer(r"^#### (.+?)\s*$(.*?)(?=^#### |^### |\Z)", venn, re.M | re.S):
        name, body = m.group(1).strip(), m.group(2)
        rows = {}
        for row in body.splitlines():
            cols = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cols) != 2 or cols[0] in ("Position", "") or set(cols[0]) <= set("-"):
                continue
            role = cols[0].split(",")[0].strip().lower()
            rows[role] = cols[1]
        para = ""
        pm = re.search(r"^\*References:(.+?)\*\s*$", body, re.M | re.S)
        if pm:
            para = pm.group(1).strip()
        blocks[name] = {"rows": rows, "para": para}
    return blocks, digital_note


def split_references(para):
    """'A 1986; B on C. Prose…' -> ('A 1986; B on C.', [prose sentences])."""
    sents = sentences(strip_md(para))
    if not sents:
        return None, []
    refs, prose = sents[0], sents[1:]
    if refs.rstrip(".") == "No external anchor":
        refs = None
    return refs, prose


def load_v1():
    """The v1 data file, for colors, carried-over links and the two clade blurbs the Layer Map lacks."""
    if not V1_DATA.exists():
        return {}
    js = V1_DATA.read_text()
    if "regionSlots" not in js or '"schema":2' in js.replace(" ", ""):
        return {}
    payload = js[js.index("=") + 1:].strip().rstrip(";")
    try:
        data = json.loads(payload)
    except json.JSONDecodeError:
        node = subprocess.run(
            ["node", "-e", f"global.window={{}};require({json.dumps(str(V1_DATA))});"
                           "process.stdout.write(JSON.stringify(window.BRAMBLE_FRAMEWORK))"],
            capture_output=True, text=True, check=True)
        data = json.loads(node.stdout)
    return {c["id"]: c for c in data.get("cells", [])}


# ---------------------------------------------------------------- build

def build():
    md = LAYER_MAP.read_text()
    eras = parse_eras(md)
    covers = parse_covers(md)
    blocks, digital_note = parse_clades(md)
    v1 = load_v1()

    cells = []
    for index, (heading, cid, line) in enumerate(CLADES):
        if heading not in blocks:
            sys.exit(f"Layer Map: no '#### {heading}' table")
        blk = blocks[heading]
        ln = LINE_BY_ID[line]
        refs, prose = split_references(blk["para"])
        old = v1.get(cid, {})
        old_links = {}
        for reg in (old.get("regions") or {}).values():
            if reg.get("label") and reg.get("panel", {}).get("links"):
                old_links[reg["label"]] = reg["panel"]["links"]

        regions = {}
        for role, raw in blk["rows"].items():
            if role not in SLOT_BY_ROLE:
                sys.exit(f"{heading}: unknown position '{role}'")
            sid = SLOT_BY_ROLE[role]
            label, settings, claimants = split_layer(raw)
            role_name = role.capitalize()
            if label:
                # the label by name, then in lower case ("a firing threshold"), then the role's own sentences
                body = ([s for s in prose if mentions(s, label)]
                        or [s for s in prose if mentions(s.lower(), label.lower())]
                        or [s for s in prose if mentions(s, "The " + role_name)])[:3]
                title = label
            else:
                body = [s for s in prose if mentions(s, role_name) and "owed" in s][:2]
                title = role_name
            regions[sid] = {
                "label": label,
                "owed": label is None,
                "settings": settings,
                "claimants": claimants,
                "panel": {
                    "title": title,
                    "body": " ".join(body) or None,
                    "links": old_links.get(label, []) if label else [],
                    "status": "draft",
                },
            }

        era = eras.get(cid, {})
        clade_prose = covers.get(cid) or (old.get("clade") or "").replace("[DRAFT]", "").strip() or None
        cells.append({
            "id": cid,
            "index": index,
            "name": heading,
            "line": line,
            "date": era.get("date"),
            "era": era.get("era"),
            "coincidingEvent": era.get("coincidingEvent"),
            "founds": FOUNDS.get(cid),
            "center": ln["center"],
            "ruled": line != "digital",
            "color": old.get("color") or NEW_COLORS[cid],
            "clade": clade_prose,
            "note": digital_note if line == "digital" else None,
            "references": refs,
            "lineTest": ln["test"],
            "proseStatus": "draft",
            "regions": regions,
        })

    return {
        "schema": 2,
        "source": "theory/framework/layers/Layer_Map.md",
        "functions": FUNCTIONS,
        "lines": LINES,
        "regionSlots": [{"id": i, "type": t, "fns": f} for i, t, f in REGION_SLOTS],
        "cells": cells,
    }


def validate(data):
    """The renderer rules the brief promises Design."""
    errors = []
    born_at = {f["id"]: (-1 if f["born"] is None else next(c["index"] for c in data["cells"] if c["id"] == f["born"]))
               for f in data["functions"]}
    slot_fns = {s["id"]: s["fns"] for s in data["regionSlots"]}
    total = 0
    for c in data["cells"]:
        ln = LINE_BY_ID[c["line"]]
        live = {f for f, i in born_at.items() if i <= c["index"]}
        expect = {sid for sid, fns in slot_fns.items() if set(fns) <= live}
        if set(c["regions"]) != expect:
            errors.append(f"{c['id']}: slots {sorted(c['regions'])} != circles {sorted(live)}")
        if len(c["regions"]) != ln["slots"]:
            errors.append(f"{c['id']}: {len(c['regions'])} slots, line wants {ln['slots']}")
        if c["center"] not in c["regions"]:
            errors.append(f"{c['id']}: center {c['center']} missing")
        for sid, r in c["regions"].items():
            if (r["label"] is None) != r["owed"]:
                errors.append(f"{c['id']} {sid}: label/owed disagree")
        total += len(c["regions"])
    if total != 176:
        errors.append(f"{total} cells in all, Layer Map says 176")
    return errors


def main():
    data = build()
    errors = validate(data)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    owed = sum(r["owed"] for c in data["cells"] for r in c["regions"].values())
    empty = sum(1 for c in data["cells"] for r in c["regions"].values() if not r["owed"] and not r["panel"]["body"])
    print(f"{len(data['cells'])} clades, 176 cells, {owed} owed, {empty} labelled cells with no panel body")
    if "--check" in sys.argv:
        return
    header = (
        "// Trellis Framework: content data, schema v2 (the growing Venn).\n"
        "// GENERATED by gen_framework_data.py from theory/framework/layers/Layer_Map.md.\n"
        "// Owned by the Code tool. Edit the Layer Map and regenerate; do not hand-edit.\n"
        "// Schema and renderer rules: DESIGN_BRIEF_growing_venn.md.\n"
    )
    out = Path(sys.argv[sys.argv.index("--out") + 1]).resolve() if "--out" in sys.argv else OUT
    out.write_text(header + "window.BRAMBLE_FRAMEWORK = " + json.dumps(data, indent=1, ensure_ascii=False) + ";\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
