// ============================================================================
// BRAMBLE — Unit 03 panel content  (Code owns this file; Design reads it)
// The far-right panel's "Bramble" view is driven entirely from here.
// Canon source: bramble_specs_v1_4.md (Parts II–IV). Copy is editable prose;
// the Explorer re-renders live. Do not add logic here — data only.
// ----------------------------------------------------------------------------
//  knobs   — the 12 knobs, keyed by install order 1..12. knob-N is the same
//            cybernetic function across all three lines (1=Effector, 2=Regulator,
//            3=Modeler, 4=Reviser, repeating). At any clade the board carries the
//            most-recent generation of each function; the Explorer picks them.
//            up = derived pole (newer layer, expressive); down = primordial pole
//            (ancestor showing through, suppressive). mira = the sticker names.
//  cells   — per clade: chassis build line + face-screen readout.
//            face.mode 'none'        → no screen fitted (pre-board builds)
//            face.always             → shows regardless of the new knob
//            face.gated + up/down    → up shows when the clade's NEW knob is up;
//                                      down is the fall-through to the layer below
//  ui      — chrome strings for the Bramble view.
// ============================================================================
window.BRAMBLE_UNIT = {
  unitLabel: 'UNIT 03',

  chassis: { genetic: 'Vacuum chassis', neuronal: 'Tetrapod chassis', symbolic: 'Humanoid chassis' },

  ui: {
    unitLabel: 'UNIT 03',
    view: 'View', ancestor: 'Ancestor', bramble: 'Bramble',
    intro: 'Unit 03 — the lab re-bodies it at every clade so you can watch a personality get built one system at a time. The household sets the knobs; the unit cannot set its own.',
    faceHeading: 'Face-screen',
    faceNote: 'An involuntary readout — Bramble cannot author or suppress it. It grows one layer per neuronal cell; a knob turned down lets its layer eclipse and the screen falls through to the layer beneath.',
    systemsHeading: 'Installed systems',
    knobsHeading: 'Disposition knobs',
    knobsSub: 'Two poles each: up = the newer layer, down = the ancestor showing through. Turn one to see what changes.',
    newTag: 'New', heldTag: 'Held',
    faceLive: '\u25CF Live', faceOff: '\u25CB Dark', faceNone: 'No screen',
    labPoles: 'Lab', miraPoles: 'Mira', motivation: 'Motivation', clinical: 'Board label',
    upTag: 'Up', downTag: 'Down',
    // face effect notes shown in the knob readout
    faceNewNote: 'This is the newly-installed system — the face-screen listens to this knob. Up powers its readout layer; down lets the screen fall through to the layer beneath.',
    faceHeldNote: 'Carried from an earlier clade. The knob still turns, but the face-screen no longer depends on it.',
    faceSymbolicNote: 'This build adds no display layer — the screen carries the Primate readout on automatic. The knob still shapes behavior.',
    // retired-system line templates ({new}=new proper name, {old}=old proper name, {mira}=old mira pair)
    retiredTmpl: '{new} replaces {old} ({mira}) at this build \u2014 the old loop folds to firmware and runs itself.',
    retiredFirst: 'First install of the {fn} system \u2014 nothing to retire yet.',
    asciiTag: 'ASCII', readoutTag: 'Readout',
    asciiNote: 'From City-Human, Bramble can draw on its own screen. The drawn channel is voluntary — and, like speech, the dishonest-capable one.',
  },

  // ---- the twelve knobs (up = derived / expressive · down = primordial / suppressive) ----
  knobs: {
    '1':  { fn: 'effector',  cell: 'prokaryote', name: 'Going',    motivation: 'Persistence',   clinical: 'Extension Type', crank: true,
            labUp: 'wound', labDown: 'unwound', miraUp: '—', miraDown: '—',
            up: 'Wound — the unit runs its tendencies: kickers out, grab, retract.', down: 'Unwound — it goes still (\u201Cthe forever kind of sleep\u201D).' },
    '2':  { fn: 'regulator', cell: 'archaeon',   name: 'Working',  motivation: 'Thrift',        clinical: 'Dependency Type',
            labUp: 'obligate', labDown: 'free-living', miraUp: '—', miraDown: '—',
            up: 'Draws through the dock — trades its sweepings for a gradient it cannot make alone.', down: 'Gathers with its own surfaces — dearer per joule, free to range.' },
    '3':  { fn: 'modeler',   cell: 'eukaryote',  name: 'Getting',  motivation: 'Interiority',   clinical: 'Pruning Type',
            labUp: 'active', labDown: 'passive', miraUp: '—', miraDown: '—',
            up: 'Clears hard — sequences that stop earning their keep are torn out, and the worn grooves left standing run clean.', down: 'Lets them lie — unused sequences decay on their own schedule, and old paths linger.' },
    '4':  { fn: 'reviser',   cell: 'eumetazoa',  name: 'Resting',  motivation: 'Excitability',  clinical: 'Home Type',
            labUp: 'loud', labDown: 'quiet', miraUp: 'Busy', miraDown: 'Warm',
            up: 'Settles in the thick of bodies — the middle of the kitchen at dinner.', down: 'Follows the thermal gradient to the warmest corner it can reach.' },
    '5':  { fn: 'effector',  cell: 'bilaterian', name: 'Choosing', motivation: 'Impetus',       clinical: 'Orienting Style',
            labUp: 'engaged', labDown: 'disengaged', miraUp: 'Learn', miraDown: 'Turn',
            up: 'Catches the freshest percept to the OBJECT band — associates off a single coincidence.', down: 'The recency layer goes dormant; home-seeking shows through and it catches nothing.' },
    '6':  { fn: 'regulator', cell: 'vertebrate', name: 'Coping',   motivation: 'Mastery',       clinical: 'Coping Style',
            labUp: 'reactive', labDown: 'proactive', miraUp: 'Little', miraDown: 'Beast',
            up: 'Hangs back and waits to be sure — the VERB + OBJECT layer runs.', down: 'Leans hard at anything that might pay — the action layer falls dormant.' },
    '7':  { fn: 'modeler',   cell: 'mammal',     name: 'Risking',  motivation: 'Autonomy',      clinical: 'Neuroticism',
            labUp: 'reflective', labDown: 'autonomous', miraUp: 'Buster', miraDown: 'Believer',
            up: 'Goes and checks whether the fear is real — forecasts an OUTCOME for the act.', down: 'Already sure it is — takes the standing read at face value, no forecast.' },
    '8':  { fn: 'reviser',   cell: 'primate',    name: 'Helping',  motivation: 'Affiliation',   clinical: 'Agreeableness',
            labUp: 'agreeable', labDown: 'selfish', miraUp: 'Respect', miraDown: 'Savage',
            up: 'Weights other minds — models what they forecast (the PERSON columns).', down: 'Out for its own — the other-mind columns fall away.' },
    '9':  { fn: 'effector',  cell: 'band',       name: 'Hunting',  motivation: 'Commitment',    clinical: 'Curiosity',
            labUp: 'focused', labDown: 'curious', miraUp: 'Deep', miraDown: 'Wide',
            up: 'Locks onto the one exchange that moves its standing and holds there.', down: 'Scatters across whatever exchange is novel — nothing held past its shine.' },
    '10': { fn: 'regulator', cell: 'settlement', name: 'Tracking', motivation: 'Stability',     clinical: 'Conscientiousness',
            labUp: 'orderly', labDown: 'kludgy', miraUp: 'Preppy', miraDown: 'Messy',
            up: 'The stored norms feel load-bearing — it flags the trash fifteen minutes late.', down: 'The schedule feels optional — a suggestion, not a law.' },
    '11': { fn: 'modeler',   cell: 'city',       name: 'Leading',  motivation: 'Representation', clinical: 'Extraversion',
            labUp: 'assertive', labDown: 'passive', miraUp: 'Boss', miraDown: 'Vibe',
            up: 'Steps up and runs the room — surfaces the written law and enforces it.', down: 'Hangs back — warms the room and carries the mood rather than leading it.' },
    '12': { fn: 'reviser',   cell: 'empire',     name: 'Living',   motivation: 'Universality',  clinical: 'Integrity',
            labUp: 'candid', labDown: 'canned', miraUp: 'Real', miraDown: 'Flex',
            up: 'The principle enters action regardless of local expedience.', down: 'Bends to the situation to protect the relationship.' },
  },

  // ---- per-clade chassis build + face-screen readout ----
  cells: {
    prokaryote: { build: 'A wind-up cell: crank-armed battery, finite-state machine, four canted solar panels. The organ it sees with is the organ it eats with, and it hunts the warm spot and holds there.',
      face: { always: true, kind: 'status', word: 'STOP', set: ['RUN', 'TUMBLE', 'STOP'], caption: 'Movement panel' } },
    archaeon:   { build: 'The dock arrives — an outboard partner trading a thermal gradient for a debris deposit; neither side is complete alone. Aboard, nothing new: idle draw falls, the margin widens, and the household learns its budget.',
      face: { always: true, kind: 'status', word: 'STOP', set: ['RUN', 'TUMBLE', 'STOP'], caption: 'Movement panel' } },
    eukaryote:  { build: 'A Roomba-class vacuum. It docks to feed and re-runs worn foraging grooves off a use-weighted board — it remembers, it does not yet learn.',
      face: { always: true, kind: 'status', word: 'STORED', set: ['STORED', 'EMPTY'], caption: 'Carry panel' } },
    eumetazoa:  { build: 'A soft radial vacuum with the first nervous tissue. It forecasts the energy gap and sleeps in a chosen spot before it strands.',
      face: { gated: true, capUp: 'Arousal panel', capDown: 'Fell through \u2192 carry panel',
        up: { kind: 'status', word: 'AWAKE', set: ['STARTLED', 'AWAKE', 'SLEEPING'] },
        down: { kind: 'status', word: 'STORED', set: ['STORED', 'EMPTY'] } } },
    bilaterian: { build: 'A tetrapod that grew a front — a centralized brain, monoamine affect, a head that turns to face you first.',
      face: { gated: true, capUp: 'OBJECT band', capDown: 'Fell through \u2192 arousal',
        up: { kind: 'lines', lines: ['MIRA'] },
        down: { kind: 'status', word: 'AWAKE', set: ['STARTLED', 'AWAKE', 'SLEEPING'] } } },
    vertebrate: { build: 'A four-limbed tetrapod with a jaw that does things on purpose — basal-ganglia reward learning, procedural memory.',
      face: { gated: true, capUp: 'VERB + OBJECT', capDown: 'Fell through \u2192 OBJECT',
        up: { kind: 'lines', lines: ['CHASE CAT'] },
        down: { kind: 'lines', lines: ['CAT'] } } },
    mammal:     { build: 'The endotherm that dreams: an insulated furnace core, a generative model it runs offline, episodic memory.',
      face: { gated: true, capUp: 'VERB + OBJECT = OUTCOME', capDown: 'Fell through \u2192 no forecast',
        up: { kind: 'lines', lines: ['CHASE CAT = LOST'] },
        down: { kind: 'lines', lines: ['CHASE CAT'] } } },
    primate:    { build: 'A mentalizing tetrapod — it tracks coalitions and keeps a social ledger of other minds.',
      face: { gated: true, capUp: 'PERSON columns', capDown: 'Fell through \u2192 self only',
        up: { kind: 'persons', persons: [['MIRA', 'OPEN DOOR', 'SAFE'], ['BRAMBLE', 'CHASE CAT', 'LOST']] },
        down: { kind: 'lines', lines: ['CHASE CAT = LOST'] } } },
    band:       { build: 'A 54-inch humanoid learning to walk and to speak. Its face cannot lie; its words can.',
      face: { always: true, kind: 'persons', caption: 'PERSON columns (carried)',
        persons: [['MIRA', 'CARRY UNIT', 'SAFE'], ['UNIT', 'SAY YES', 'GAINED']] } },
    settlement: { build: 'A humanoid that plans past today — it stores against winter and keeps a household schedule.',
      face: { always: true, kind: 'persons', caption: 'PERSON columns (carried)',
        persons: [['SELF', 'STORE GRAIN', 'GAINED'], ['MIRA', 'WAIT WINTER', 'SAFE']] } },
    city:       { build: 'A humanoid that writes things down; the marks outlive their author. It can now draw on its own screen.',
      face: { always: true, kind: 'persons', caption: 'PERSON columns', canAscii: true,
        persons: [['MIRA', 'READ LAW', 'GAINED'], ['UNIT', 'FLAG DEBT', 'SAFE']],
        ascii: ' .----------.\n | III OWED |\n |  LEDGER  |\n \'----------\'' } },
    empire:     { build: 'A humanoid that sticks up for someone not in the room — stranger-to-stranger trust.',
      face: { always: true, kind: 'persons', caption: 'PERSON columns (carried)',
        persons: [['STRANGER', 'KEEP WORD', 'SAFE'], ['UNIT', 'TRUST FAR', 'GAINED']] } },
  },
};
