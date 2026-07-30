// ─────────────────────────────────────────────────────────────────────────
// Trellis Framework — UI CHROME COPY
// OWNED BY THE CODE TOOL. This file is all the interface wording (labels,
// headings, button text, help modal). The Design tool reads every string from
// here and hardcodes none, so copy edits here never collide with design edits
// in "Bramble Explorer.dc.html".
//   • Content prose (per-clade / per-region body text)  → framework-data.js
//   • UI chrome copy (everything below)                  → THIS FILE
// Keys are consumed as {{ ui.<key> }} holes in the design file — renaming a key
// requires a matching change there, so coordinate schema changes.
// ─────────────────────────────────────────────────────────────────────────
window.BRAMBLE_UI = {
  // masthead
  brandLine1: "Trellis",
  brandLine2: "Framework",

  // left rail + header
  ladder: "Ladder",
  trellisFn: "TRELLIS FUNCTION",

  // labels toggle + its explainer
  labelsHeading: "LABELS",
  formLabel: "Form",
  functionLabel: "Function",
  blurbPre: "Switch the flower's labels between this clade's own ",
  blurbForm: "form",
  blurbMid: "\u00A0— which climbs and changes at every level — and the universal ",
  blurbFunction: "function",
  blurbPost: " roles, which stay the same at each rung of the trellis.",

  // legend — region types
  modulesHeading: "MENTAL MODULES",
  motivation: "Motivation",
  tendency: "Tendency",
  capacity: "Capacity",
  breakthrough: "Breakthrough",
  signature: "Signature",

  // legend — cybernetic systems
  systemsHeading: "CYBERNETIC SYSTEMS",
  effector: "Effector",
  regulator: "Regulator",
  modeler: "Modeler",
  reviser: "Reviser",

  // specimen viewfinder
  noSpecimen: "NO SPECIMEN ON FILE",
  awaitingCapture: "AWAITING FIELD CAPTURE",
  rec: "REC",

  // right panel section labels
  backTo: "Back to",
  virtuousCycle: "THE VIRTUOUS CYCLE",
  draftProse: "DRAFT PROSE",
  functionsInPlay: "FUNCTIONS IN PLAY",
  scienceLinks: "SCIENCE LINKS",

  // mobile horizontal rail
  mobileOlder: "◀ OLDER",
  mobileRailTitle: "DEEP-TIME RAIL",
  mobileNewer: "NEWER ▶",

  // help modal
  helpTitle: "HOW TO READ THE TRELLIS",
  helpIntroDesktop: "A field guide to one personality's deep history — from the first cell to the modern self — read as a trellis of inherited functions.",
  helpIntroMobile: "A field guide to one personality's deep history, read as a trellis of inherited functions.",
  helpRailH: "THE RAIL",
  helpRailPD: "Twelve clades, oldest at the base climbing to newest. Click any to travel its lineage; the three tinted bands are the genetic, neuronal, and symbolic inheritance lines.",
  helpRailPM: "Twelve clades, oldest at the base to newest. Tap any to travel its lineage; the tinted bands are the genetic, neuronal, and symbolic lines.",
  helpFlowerH: "THE FLOWER",
  helpFlowerPD: "The four functions — Effector, Regulator, Modeler, Reviser — and the regions they combine into. Click any node to open its panel.",
  helpFlowerPM: "The four functions — Effector, Regulator, Modeler, Reviser — and the regions they combine into. Tap any node to open its panel.",
  helpTrellisFnH: "THE TRELLIS FUNCTION",
  helpTrellisFnPD: "Each clade adds one new function, shown in color; functions carried from older clades stay slate.",
  helpTrellisFnPM: "Each clade adds one new function, shown in color; carried functions stay slate.",
  helpRegionsH: "REGION TYPES",
  helpRegionsPD: "Motivation (solid), Tendency (soft ellipse), Capacity (dashed), Breakthrough (the lit center), and Signature (the two opposite-pair venns).",
  helpRegionsPM: "Motivation (solid), Tendency (soft ellipse), Capacity (dashed), Breakthrough (lit center), Signature (the opposite-pair venns).",
  helpFormFnH: "FORM / FUNCTION",
  helpFormFnPD: "Toggle labels between this clade's specific names and the universal cybernetic roles.",
  helpFormFnPM: "Toggle labels between this clade's specific names and the universal cybernetic roles.",
};
