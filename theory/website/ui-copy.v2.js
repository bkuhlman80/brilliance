// ─────────────────────────────────────────────────────────────────────────
// Trellis Framework — UI CHROME COPY, schema v2 (the growing Venn)
// OWNED BY THE CODE TOOL. This file is all the interface wording (labels,
// headings, button text, help modal). The Design tool reads every string from
// here and hardcodes none, so copy edits here never collide with design edits
// in "Bramble Explorer.dc.html".
//   • Content prose (per-clade / per-region body text)  → framework-data.v2.js
//   • UI chrome copy (everything below)                  → THIS FILE
// Keys are consumed as {{ ui.<key> }} holes in the design file — renaming a key
// requires a matching change there, so coordinate schema changes.
// Schema and renderer rules: DESIGN_BRIEF_growing_venn.md.
// ─────────────────────────────────────────────────────────────────────────
window.BRAMBLE_UI = {
  // masthead
  brandLine1: "Trellis",
  brandLine2: "Framework",

  // left rail + header
  ladder: "Ladder",
  trellisFn: "TRELLIS FUNCTION",
  slotsSuffix: "-SLOT VENN",
  lineSuffix: " LINE",
  cladeWord: "CLADE",

  // rail bands
  genetic: "Genetic",
  nemetic: "Nemetic",
  memetic: "Memetic",
  symbolic: "Symbolic",
  digital: "Digital",
  prework: "Prework",
  preworkCaption: "Chemistry that keeps itself going, with no store: a Venn of one circle.",

  // labels toggle + its explainer
  labelsHeading: "LABELS",
  formLabel: "Form",
  functionLabel: "Function",
  blurbPre: "Switch the flower's labels between this clade's own ",
  blurbForm: "form",
  blurbMid: " — what installed in each cell at this clade — and the universal ",
  blurbFunction: "function",
  blurbPost: " roles, which name the same cell on every line.",

  // legend — region types
  modulesHeading: "REGIONS",
  single: "Single",
  pair: "Pair",
  triple: "Triple",
  center: "Center",

  // legend — functions
  systemsHeading: "FUNCTIONS",
  effector: "Effector",
  regulator: "Regulator",
  learner: "Learner",
  member: "Member",

  // role names and glosses (Function mode, tooltips, panel headers)
  roles: {
    effector:    { name: "Effector",    gloss: "does; holds nothing" },
    regulator:   { name: "Regulator",   gloss: "holds a value the unit can be wrong about" },
    learner:     { name: "Learner",     gloss: "keeps a store rewritten by what was met" },
    member:      { name: "Member",      gloss: "renders into a code others take up" },
    controller:  { name: "Controller",  gloss: "acts against a held value; nothing rewritten" },
    anticipator: { name: "Anticipator", gloss: "a held value the unit's own outcomes revise" },
    connector:   { name: "Connector",   gloss: "acts with a store tuned by what its acts met" },
    adapter:     { name: "Adapter",     gloss: "a store rewritten by what it is told" },
    operator:    { name: "Operator",    gloss: "a held value rendered so others hold the unit to it" },
    starter:     { name: "Starter",     gloss: "emits into a shared code" },
    conservator: { name: "Conservator", gloss: "acts, scores and revises, with no exit to others" },
    herald:      { name: "Herald",      gloss: "a held value enacted and told; the store unrevised" },
    counselor:   { name: "Counselor",   gloss: "candidates rehearsed against a held value before any is voiced" },
    tester:      { name: "Tester",      gloss: "tried in the code and revised by what comes back" },
    translator:  { name: "Translator",  gloss: "the loop that closes through other members" },
  },

  // cell states
  settings: "SETTINGS",
  settingsExplainer: "A setting is a dial on this cell's loop: how much, how readily or how strongly it runs, not a separate operation.",
  owed: "owed",
  owedExplainer: "Owed: the install in this cell is still to be found. No evidence at this clade reads at this composition yet.",
  claimants: "claimants",
  unruled: "UNRULED",
  unruledExplainer: "This clade has not been ruled. Its labels are placeholders kept so the Venn is drawn; take nothing from them.",
  founds: "Born here",

  // specimen viewfinder
  noSpecimen: "NO SPECIMEN ON FILE",
  awaitingCapture: "AWAITING FIELD CAPTURE",
  rec: "REC",

  // right panel section labels
  backTo: "Back to",
  lineTest: "THE LINE TEST",
  draftProse: "DRAFT PROSE",
  functionsInPlay: "FUNCTIONS IN PLAY",
  scienceLinks: "SCIENCE LINKS",
  references: "REFERENCES",

  // mobile horizontal rail
  mobileOlder: "◀ OLDER",
  mobileRailTitle: "DEEP-TIME RAIL",
  mobileNewer: "NEWER ▶",

  // help modal
  helpTitle: "HOW TO READ THE TRELLIS",
  helpIntroDesktop: "A field guide to deep history — from self-sustaining chemistry to the digital agent — read as a Venn that grows a circle each time a new kind of memory appears.",
  helpIntroMobile: "A field guide to deep history, read as a Venn that grows a circle with each new kind of memory.",
  helpRailH: "THE RAIL",
  helpRailPD: "Twenty clades, oldest at the base climbing to newest. Click any to visit it. The bands are the genetic, nemetic and memetic lines; the memetic line runs first in the symbolic medium, then in the digital.",
  helpRailPM: "Twenty clades, oldest at the base to newest. Tap any to visit it. The bands are the genetic, nemetic and memetic lines, the last in two media.",
  helpFlowerH: "THE FLOWER",
  helpFlowerPD: "The Venn grows: two circles on the genetic line, three on the nemetic, four on the memetic. Each region is a cell, and each cell holds what installed there at this clade, or is owed. Click any region to open its panel.",
  helpFlowerPM: "Two circles on the genetic line, three on the nemetic, four on the memetic. Tap any region to open its panel.",
  helpTrellisFnH: "THE TRELLIS FUNCTION",
  helpTrellisFnPD: "A new function is born once per line, at its founding clade — the Regulator at RNA World, the Learner at Eumetazoa, the Member at Band — splitting off from the center of the Venn as it stood.",
  helpTrellisFnPM: "A new function is born once per line, splitting off from the center: the Regulator at RNA World, the Learner at Eumetazoa, the Member at Band.",
  helpRegionsH: "REGION TYPES",
  helpRegionsPD: "Singles, pairs, triples and the center. The lit center is the clade's breakthrough: the Controller on the genetic line, the Conservator on the nemetic, the Translator on the memetic.",
  helpRegionsPM: "Singles, pairs, triples and the lit center, the clade's breakthrough.",
  helpFormFnH: "FORM / FUNCTION",
  helpFormFnPD: "Toggle labels between this clade's specific names and the universal roles.",
  helpFormFnPM: "Toggle labels between this clade's specific names and the universal roles.",

  // Four Corners (the growing pyramid, served at /four-corners/)
  fourCorners: "Four Corners",
  fourCornersBlurb: "Why 3, then 7, then 15: the four functions as the corners of a pyramid that grows a dimension per line.",
  fourCornersHref: "/four-corners/",
  fourCornersBack: "Back to the Explorer",
  helpFourCornersH: "FOUR CORNERS",
  helpFourCornersPD: "The slot counts are not a convention. Four functions are the corners of a pyramid: a point, then a line, a triangle, a solid. Its corners, edges, faces and interior are the fifteen slots. Open Four Corners to watch it grow.",
  helpFourCornersPM: "Four functions are the corners of a pyramid; its corners, edges, faces and interior are the fifteen slots. Open Four Corners to watch it grow.",
};
