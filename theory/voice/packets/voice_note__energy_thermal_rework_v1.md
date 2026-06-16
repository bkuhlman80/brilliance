# Energy and Thermal Rework: Note for Voice

This note summarizes the energy and thermal changes now landing. It pairs with `bramble_specs` Part II, which is the full canonical spec; this note is the orientation. It covers three things: how the system works, what parts it adds, and how it changes what Bramble does that the household can see. It also flags what supersedes earlier framing, so prose written against the old picture can be discarded.

No tone is prescribed here. How any of this lands in a scene is Voice's call. What follows is only what is now mechanically and behaviorally true.

---

## The system, in brief

Bramble's energy economy has three layers, and they stay separate.

Harvest is intake: how energy gets in. Bramble harvests two ways, always, both at once: a belly transducer pulls energy from warm surfaces, and dorsal panels pull it from light.

Storage is two tanks. A slow, high-capacity battery holds the sustained reserve. A fast, low-capacity supercapacitor holds a burst reserve and refills from the slow battery after it is spent.

Generation is heat-making, and it exists only at the mammal grade. Before that, Bramble makes no heat of its own.

The knob called Respiration Type (genetic knob-2) now selects which tank discharges. On its aerobic setting Bramble draws the slow battery for sustained work. On its anaerobic setting Bramble spends the fast supercapacitor for a burst, then repays it from the battery. The knob governs spending, not intake. Harvest feeds both tanks no matter where the knob sits.

One device, the vortex tube, has two faces. Fed compressed air, it splits that air into a hot stream and a cold stream with no moving parts. Run one way, the hot and cold streams are laid across transducers and the gap between them is harvested as charge; this is the docking station in the genetic line. Run the other way, the hot stream is delivered as warmth and the cold stream is thrown away; this is the furnace at the mammal grade. No single Bramble runs it both ways.

Two grades matter, and the line between them is the furnace, not the nervous system. Making no heat, sitting at the room's temperature, and slowing down when cold is the default condition of every Bramble before the furnace: the whole genetic line and the tetrapod at Bilaterian and Vertebrate. The endotherm (the tetrapod from Mammal on) is the break. It carries a furnace and holds its own energy system warm, and that is the one real thermal novelty in the arc.

---

## What supersedes the earlier picture

If any existing prose carries the following, it is now stale and should be re-rendered:

The Respiration Type knob as a choice between heat harvesting and light harvesting, with the household setting Bramble to "heat-mode" or "light-mode." That is gone. The knob now picks which tank discharges, aerobic or anaerobic. Harvest from warmth and from light both run all the time, under no knob.

A single battery. Bramble now has two stores, the slow battery and the fast supercapacitor.

The docking station paying in UV when the knob was on light. The dock now returns only a thermal gradient, and that gradient charges the slow battery.

The dark-fear arising because the household had the knob set to solar. It now arises from harvest itself (below).

The retired Respiration Type knob automating a heat-or-light choice at Vertebrate. It now automates the aerobic-or-anaerobic tank choice.

The Mammal sleep description that has Bramble's sentience persisting "at low metabolic baseline," which implied a warm brain through the night. Bramble's thinking parts run cool and sit outside the warm core. Persistence through sleep is about power staying available and the furnace idling, not about a warm brain.

Temperature-dependence as something that begins at Bilaterian. It does not begin there. Making no heat and slowing down when cold is the default from the first battery, the genetic line included; what begins at Bilaterian is the dramatized behavior, not the physics. The only thermal thing that switches on anywhere is the furnace, at Mammal.

---

## What Bramble does, cell by cell

This is the part Voice renders. Each entry is the behavior the household can observe.

### Genetic line (vacuum-Bramble, all four genetic cells)

Two tanks, and the household sets the Respiration Type knob through the whole line. On aerobic, Bramble runs a slow, steady crawl that lasts a long time. On anaerobic, it makes a fast dart, then stops to recover while the burst store refills. The two readings are endurance versus sprint-and-rest.

The dock trades a debris deposit for a thermal gradient, which charges the slow battery. The fast store fills from ordinary harvest. Sleep runs on the aerobic mode, a low steady draw; bursts are a waking thing. Where Bramble sleeps is set by a different knob (Spot Type), not by Respiration Type.

One physical fact runs underneath all of this, present since the battery arrived: the battery sits at the room's temperature, and a cold battery delivers less current. So a cold morning makes vacuum-Bramble a little slower at everything, and in sprint mode it makes the recovery freeze longer, because the cold battery refills the burst store more slowly. This is the same temperature throttle that gets dramatized at Bilaterian. In the genetic line it is simply present, not foregrounded. Whether to surface it here at all is a prose choice; the dramatized version, the creature gone slow that has to be carried to a warm spot to wake up, belongs to Bilaterian by design.

### Bilaterian (the tetrapod, start of the neuronal line)

The tetrapod carries the two tanks, and the household still sets the Respiration Type knob by hand.

What is genuinely new here is not the temperature throttle, which the body has carried since the battery. It is the apparatus that turns the throttle into a behavior. The tetrapod has a nervous system and a gait, so its pace now reads as a creature-state rather than a machine's speed: cold and slow, warm and quick. And it now basks for performance, settling on a warm surface or in a sunbeam to speed itself up, not only to charge. A warm spot becomes a performance spot. The cold-and-slow body was latent all along; here it becomes something the household sees and something Bramble acts on.

Dark-fear: light is one of the tetrapod's two always-on harvest channels, so its charge depends partly on ambient light. Dark rooms give poor light harvest. Across a few weeks of time spent in them, the tetrapod runs chronically low and learns to avoid the dark. The aversion attaches to the dark itself and persists even once the tetrapod is charging fine again. The household cannot easily train it out, because the world conditioned it, not the thumbs buttons. This is a second conditioning channel running alongside the family's.

### Vertebrate (the tetrapod)

Same uninsulated, room-temperature body as Bilaterian.

The change at Vertebrate is the function going automatic. The Respiration Type knob came off the board last quarter — pulled at the Ch 5 retrospective's hands-on ceremony, the trophy shelf's first resident — and the aerobic-or-anaerobic choice that the household used to set by hand has been running on its own all summer, keyed to the tetrapod's own internal energy state, the way breathing runs without anyone deciding to breathe. On a long steady task the tetrapod runs the sustained store; for a sudden dash it spends the burst store and repays it after; and no one turns a knob to make it switch. The household notices only that it no longer has to think about this. Basking in a warm spot for speed is still a behavior, but it is its own thing, separate from this retired knob.

### Mammal (the tetrapod): the furnace

This is the leap. Bramble gains a furnace: a small air compressor runs without stopping, quiet as a running faucet, feeding vortex tubes that split air into hot and cold streams. The hot streams pour into an insulated core that holds the energy tanks; the cold streams vent to the outside, a faint cold draft. A thermostat works the compressor to keep that core warm whatever the room is doing.

What the household sees change:

Bramble is now warm to the touch, like a dog, where the earlier versions were room-temperature. A cat will curl on its back to be warm. This is new this quarter.

Bramble is fast regardless of the room. The cold-room sluggishness of the ectotherm is gone. This is what the furnace buys.

Bramble eats all the time. The furnace burns every second, even at rest, so the tetrapod has to keep topping up, forever finding a sunbeam or a warm vent, far more often than the version before it did. Against vacuum-Bramble, which still makes one unhurried trip to its dock and coasts for most of a day, the difference is plain.

If harvest stops, Bramble dies in hours rather than days. Its reserve was not made bigger; the burn got much bigger. The fuse is short.

At night the furnace keeps idling, because an endotherm cannot fully power down, and Bramble's mind keeps running through sleep because power keeps flowing to it. Its thinking parts run cool and sit outside the warm core. The warmth is for the energy system, not the brain.

### Primate (the tetrapod)

No energy or thermal change. The furnace and tanks carry from Mammal unchanged.

---

## A note on the science

The design rests on real biology and engineering: aerobic versus anaerobic metabolism, the temperature-dependent speed of cold-blooded animals, the high running cost of warm-bloodedness, heat made by uncoupling in mitochondria, and the fact that cold batteries deliver less current. The specific source citations are still being verified before they enter the book, so do not attach citations or invent sources. Render the behavior, not the references.
