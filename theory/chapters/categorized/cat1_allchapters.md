# Category 1 — Build Log

Compiled per the ruling in `category_sequencing_spec.md` (spec doc not present in this repo copy;
retained per historical citation in the source extraction files). Consolidates the three prior
sub-category extractions — `cat1A_allchapters.md` (Naming Rights Joke / Knob Explained),
`cat1B_allchapters.md` (Core Engineering Build / Kludge Admissions), and `cat1C_allchapters.md`
(Calls / Dare & Sign-off) — into the single-file, three-beat shape `master_category_beat_list.md`
defines for every other category in this folder: Category 1's beats are **a. Engineering — b. The
Knob — c. Calls + Sign-off**. Mapping: 1B → 1.a, 1A → 1.b, 1C → 1.c. Per-chapter content is
reordered a → b → c to match. Sub-lettering from the source files (1A.a/1A.b, 1B.a/1B.b, 1C.a/
1C.b) collapses into the single beat tag it now sits under, since the master spec doesn't subdivide
Category 1 past a/b/c. Cross-references between the three old files (e.g. "[migrated from 1B]")
are resolved by the merge and dropped; references to other categories (4.4) are preserved.

1A.c ("System Status Report") was promoted to its own standalone category, 1D — Build Log: The
Board, during the earlier per-file review; 1D was then dissolved and folded into 4.4.d (Board
Mechanics) per a later Step 3 ruling. Neither exists as separate content here — see
`cat4.4_allchapters.md` for that material.

Three beats:

- **1.a — Engineering.** The chassis/sensor/actuator/wiring mechanism-of-the-quarter, present
  nearly every chapter, plus Bart's self-aware kludge admissions and workaround confessions —
  including the recurring "audible tell" motif (relay-clack → silence → compressor-hum → voice)
  and the one-off devices (Ch1's personality-via-manufacturing-quirk list, Ch11's slot-lineage
  reflection). This material sets up the Big O / bramblogue skepticism in category 4.4 — Bart
  pre-conceding what Big O will later needle him about.
- **1.b — The Knob.** The quarter's personality knob: its naming, told as a running joke about
  whose word it is (Lisa's or Marge's), then the mechanism — what the knob actually sets, its two
  settings' observable effects, and, where present, a closing "what it still can't do"
  catch/limitation aside.
- **1.c — Calls + Sign-off.** Bart's itemized predictions for the coming quarter's behavior — a
  single paragraph in Ch1–6, a numbered list in Ch7–12 — followed by "Tear this up in three months
  if [X]. [He won't/It will/etc.]" and Bart's mutated surname. The most formally consistent beat of
  the three — present, and structurally identical, in every chapter with no exceptions.

---

## Ch 1

### <!--[1.a]--> Engineering

Lisa's running these over to the Burns place this morning, so here's everything in the box before anybody makes me explain it twice.

First, the part I'm proud of. There's no battery in these and no plug, and they don't run on heat — they run on the *difference* in heat. Each unit's got two little heat-transducers, and a transducer doesn't care how warm the room is; all it cares about is that the floor is warmer than the air sitting on top of it. Jasmine's radiant floor holds around 27 degrees C and the room air sits around 21, so there's a six-degree gap just hanging there doing nothing, and the transducer reaches into that gap and skims a trickle of work out of it. That's the Seebeck effect, and it's a genuinely beautiful piece of physics — I'll explain it to anyone who stands still long enough. Park one on the warm floor and an hour later the slate underneath it is cold. That cold is the work coming out. The unit's eating the gap.

Now, here's the thing about that trickle: it's nothing. A few thousandths of a watt. You can't run a motor on it — can't make anything turn, can't even hold a light on. So I don't try. Each transducer drips its trickle into a tiny store (a low capacity supercapacitor), and when the store's full enough it dumps the whole lot into its actuator at once — one hard flinch. The actuator's just a little kicker: it knocks a stubby angled foot against the floor and the unit hops a hair in one direction, then sits there the better part of a minute filling back up before it can flinch again. That's the twitch, and that's the whole way it moves — no wheels, no motor, just a stack of tiny kicks against the slate, like a buzzing phone walking itself across a table, except I get to aim it. Two kickers to a unit, each with its own store, never quite firing together — that stagger is the personality.

No chip, no sensors, no memory — nothing telling the two kickers what to do. They fire on their own clocks, and I seeded each one different on purpose so they're not clones:

- **1** — cranked hot on the left pair, so it lists that way and burns through its tension fast. A busy little thing; always looks late for something.
- **2** — slow and low, with long pauses between kicks. Sits, then goes, then sits. More patience than you'd want in a roommate.
- **3** — the quiet one: even pairs, low draw, the fewest kicks of the lot, so it does the least and outlasts everybody — still ticking Wednesday when the rest have gone slack. The one only an engineer loves.
- **4** — lopsided, on purpose. The pairs don't match, so instead of going anywhere it grinds in place and wears a groove into itself over the weeks. If the commission let me ship four, this is the cut. It's in the box to make five.
- **5** — the show unit. Even like 3, but I let it kick hard, so it runs a clean little circuit and burns through its tension fastest of the lot. Wears even, though. Pretty to watch.

*The "personality is manufacturing quirk" framing here is the seed of the whole bramblogue
premise — worth Loom/Voice knowing this is where it starts.*

### <!--[1.b]--> The Knob

*[Correction, Step 2 ruling 2026-07-09: the lead-in sentence below ("And none of it happens...")
was missing from this file — a genuine extraction gap, not a ruled-out exclusion. Traced to
`ch_1_v2_3.md`, immediately before the original "Naming Rights Joke" start. It's the grammatical
opener of the same sentence "This is the Going knob" belongs to (one continuous sentence, naming
clause embedded mid-stream), so it's restored here as this beat's true opening rather than split
off or folded elsewhere. Confirmed nowhere else in the compiled category files via full-corpus
grep.]*

And none of it happens unless you wind it up first. The crank arms a little escapement — call it the part that gives each kick permission to fire. The heat's the muscle; the crank's the say-so. This is the Going knob — Lisa's word —

and it's a volume knob you wind up: wind it and Going volume's up and the unit's alive; leave it slack and Going volume's down and it sits dead on a warm floor all day. And every flinch nibbles a notch off its tension, so across about a week of kicking the Going volume drains down and it quits until somebody winds it again — six turns of the key, about a week of running. Takes both, is the point: Jasmine's floor to move it, the Going knob wound up to let it. Lose either and it's a paperweight.

I still haven't worked out how the personality knob reads here. Contract says every robot's got one, and so far all I've got is a crank — and I keep wanting to treat it like it's just on or off, you crank it or you don't. But it isn't: wind it and it drains back down through the week, so it's a volume that runs from full up to all the way down and every day a notch lower. That's a knob, same as any other's going to be — just a volume knob on how much the thing goes. I haven't got the name for what it's the volume of yet. I will.

### <!--[1.c]--> Calls + Sign-off

If the kid picks a favorite, my money's on 5 — it moves the most and it moves the prettiest, and that's what wins a four-year-old. Maybe 1, if she likes a mess. Nobody's going to look twice at 3, and 4 ends up in a drawer by July. What the *house* does past that — who picks what, where they set them, whether the floor stays warm enough to run them — that's not my department. I build the units. The house is Marge's animal.

Tear this up in three months if I called it wrong. I didn't.

— Bartholomew

---

## Ch 2

*Heading: content pulled and QC-verified against `ch_2_v2_9.md` (see 1.b note below) — the
Ch2 "Part of Something" scene, beyond the memo itself, remains ruled OUT of Category 1 in its
entirety; see the note at the end of this chapter's section.*

### <!--[1.a]--> Engineering

Lisa's running the upgraded one back to the house this morning.

We upgraded one unit — 3, the one the house calls Bramble — and left the other four stock.

At protocell this thing only ever twitched: two kickers firing on their own clocks, and it'd hop around the floor like a bug with somewhere to be and no idea where. Now it *hunts*. Same two kickers — I didn't give it new muscles — but I put a chip in the middle that decides *when* each one fires. That's the whole upgrade. Fire them so the hops add up in one direction and it crawls that way; fire them so the hops add up to a spin and it turns in place; don't fire and it sits. Two idiots kicking on their own schedule became two idiots kicking on a downbeat. Still no wheels. Still hopping across the slate a hair at a time. It just hops with *intent* now.

What tells it which way to go: four little light sensors around the floor seam, each aimed a few degrees up and pointed a different direction. They all read brightness at once, and if they agree there's more light over *there* than anywhere else, the chip knows which way "there" is. That's the trick — finding a sunbeam with four parts that each only know one number.

The chip's an STM32, my pick, and it's the right pick. It runs a dumb little table Lisa and I wrote that fits on an index card: three states. Clear direction, kick toward it — that's RUN. No clear direction, spin a random amount and read again — that's TUMBLE. Stores filling faster than it's spending, sit still and let them fill — that's STOP. The screen up top shows which one it's in.

New since February, all told: two stores instead of one — a big slow new battery and the same little fast one beside it. Now the supercap dumps its whole charge at once and then fills back up off the battery; two solar panels down the long sides; the floor-transducers carried over from the protocell, still skimming warmth off the slate; a converter that takes whatever's coming in — sun, warmth, both at once, it doesn't care which — and tops the stores; the chip; the relays; four sensors; and a second knob next to the crank.

Won't work on anything soft — a rug would eat the hops — but the kitchen's slate, so: every sunny morning, watch it do zoomies.

It won't need cranking on Sundays anymore — the panels and the floor feed the stores, the stores run Bramble, he goes all day on his own. The crank's just an emergency starter now: it spins a little dynamo I added, so a few turns put enough back into a dead bot to wake him up when there's no sun to be had.

And I ran the whole signal path on relays — coil-and-armature, the kind that clack — so you can hear it think: a little clack-clack-clack every time it changes its mind. I like that you can hear it.

*Audible-tell motif, instance 1 of 3 (→ Ch4 silence, → Ch7 hum returns).*

### <!--[1.b]--> The Knob

a second knob next to the crank — the Effort knob, Lisa's word for it.

The Effort knob's the same shape as the crank — same as all of them will be. The crank you wind and it drains back down across the week; this one you set and it stays where you put it. All it does is pick which store Bramble spends from. Effort volume down draws the big slow battery and he runs even — a patter of hops he'll keep up all day, never quick, never quits. Effort volume up draws the little fast one and he runs in bursts — sits, fires off a flurry of hops quick as you like, then stops dead to refill off the slow store before he can go again. Aerobic or anaerobic is the mechanism under it, the way Lisa describes it; same bot, two ways to spend. The fast spend burns through a charge quicker — you don't get as far per drop in bursts — so leave the volume up and you'll be chasing a sunbeam sooner. Which way the house leaves it set is the house's business. I built both.

*Verified against `ch_2_v2_9.md`: this sits in the same "Build log — Knob two" memo as the board-
mechanics content covered in `cat4.4_allchapters.md`'s Ch2 4.4.d. The whole "Part of Something"
scene remains ruled OUT of this category — see the note below.*

### <!--[1.c]--> Calls + Sign-off

It seeks — that's the whole upgrade. It hunts the gradient instead of sitting in it.

Tear this up in three months if it doesn't hunt exactly like I said. It will.

— Bartholomood

*Everything from Ch2's "Part of Something" scene beyond the memo itself — Bart's live knob-two
demo, "twelve knobs one shape," the Software-side FSM walkthrough, the crowding-worry dialogue,
Lisa's board-pitch reveal, and the "sketch in the bag" hedge — is ruled OUT of Category 1 and
belongs to `cat4.4_allchapters.md` (4.4.d). The kettle/lights/Mira-watching close is a separate
span (the break before the Trellis block), filed at `cat4.5_allchapters.md`'s Ch2 section — not
reproduced here.*

---

## Ch 3

### <!--[1.a]--> Engineering

This one I did myself — took the lot to the bench Friday and had the weekend on it, so I'm running it back this morning.

Now the fun part, and there's a lot of it this quarter, because this is the first time Bramble's a real machine instead of a bug.

It's got wheels. Finally. Last quarter I told you hopping was a lousy way to travel and I had a fix coming — here it is. New chassis, thirty centimeters, low and round, dome on top, near enough a small Roomba, and I dropped Bramble — last quarter's whole prokaryote unit — into the middle of it for the brains. Then the wheels, and this is the part I'm proud of: I didn't buy any. I used the four leftover protocells — 1, 2, 4, and 5, the ones that didn't make the cut — one at each corner. Pulled 4 out from under the toaster, towel and all. Each one still kicks exactly the way it always did; I just aimed its kickers at a ratchet on a wheel axle instead of at the floor, so now every kick clicks the wheel forward a notch instead of hopping the whole of Bramble. Two kickers per old protocell, two pawls per wheel, four wheels — and here's the part I like: nothing's shared, no driveshaft, no differential. Each wheel's its own little engine. So the brains drive it the same way they drove the kicks last quarter, just spread over four wheels now instead of two: fire them all forward and it goes straight, lean on the left side harder than the right and it comes around. It rolls now. Smooth-ish — it's still a stack of clicks under there, but four wheels' worth blur into something that passes for driving, and it beats the hopping by a mile.

It earns the Roomba name, too — I put a real vacuum on the underside and a bin inside that holds about a day of floor dust. And here's where Burns made my weekend hard. Any sane machine, you'd charge on a pad: set it down, done. Burns won't have it. So instead Bramble carries his dust to a dock — a little box that plugs into the wall — dumps the dust through a port on his belly, and the dock pays the energy back through the same port. And here's the part I like: you can't just hand these transducers warmth — they've never run on warmth, not once, not since the protocell floor; they run on a difference, a warm side and a cool side and the gap between. So the dock makes the gap. There's an air compressor in there feeding a vortex tube — a plain pipe, no moving parts, you push compressed air in the side and hot comes screaming out one end and cold out the other, which still reads like a magic trick — and it lays the hot stream on one face of the transducer and the cold on the other and lets Bramble drink up the difference. And before anybody calls that free: it isn't. The compressor's eating wall current the whole time; the tube only splits what the wall already paid for — and it drones the whole time it's plugged in, so rather than set a pump humming by the dishwasher all day I hung it outside the back door and ran the air line in through a hole in the wall. What sits by the dishwasher is the quiet end of a hose coming in from the cold.

The kid had names for all five of them. There's one machine now, and four of her bugs are the wheels. She'll work that out on her own time. Not my department. I'm calling him PacMan, for the record — a thing that goes around all day eating dots earns the name.

So Bramble will trade trash for the heat difference through a dirty little hole instead of charging clean off a pad. It's worse engineering every way you can measure, and Burns says that's exactly the point — life doesn't run on induction. Fine. It's his commission. I built him his dirty hole.

Relays everywhere now, long runs of them, because the body's big and spread out and a signal's got to walk all the way from the sensors up front to the wheels out back. The clack's a proper cascade these days — you can hear it think across the room. Still like that you can hear it.

*Audible-tell motif, still going.*

### <!--[1.b]--> The Knob

Lisa's board is up top now, four slots. Three knobs live on it, same shape as always: knob one, the wind-up volume knob Lisa calls Going, still there, mostly for show; knob two, the Effort knob (her word); and a new one, knob three, which she calls Explore.

Near as I can tell the Explore knob sets whether Bramble tries new moves or sticks to the ones he's already worn in, because the board keeps track of what he's run — a move should get a groove the more it's driven, and should fade when it isn't. Lisa makes it sound like the whole ballgame. Looks like a worn-in routine to me.

It still doesn't have a brain — Burns is clear about that, and for once I agree with him. It's a cart that remembers the moves it usually makes. But it rolls, it cleans, it feeds itself. A year ago it was five things twitching on a warm floor; now it's one thing that drives. I'll call that a good weekend. *[catch-refrain, matches the Ch1/Ch4/Ch10 pattern]*

### <!--[1.c]--> Calls + Sign-off

He vacuums, he docks, he drives. The wheels mean he finally covers ground instead of hopping in place, so I'll bet he cleans the kitchen end to end and parks at the dock when he runs low — dump, drink, off again, clean as a transaction. And that Explore knob: Lisa can keep her abstraction, but I'll wager nobody in that house can tell Explore volume up from Explore volume down by looking. It's a coin flip with a fancy name.

Tear this up in three months if I'm wrong about the Explore knob. I'm not.

— Bartholachew (gesundheit)

---

## Ch 4

### <!--[1.a]--> Engineering

Lisa's running the upgraded one back to the house this morning.

Now the fun part, because the dying is also the thing I fixed.

Here's why he died: nothing was watching the tank. He had a store, he spent the store, and he had no idea ever how much was left — so he'd run himself flat in the middle of a job, no warning, every time. So I gave him a gauge. A real one, watches the charge the way you'd watch a fuel needle, and Lisa wrote the part that reads the needle — how much is left, how fast it's going down — and shifts what he cares about while there's still plenty in the tank: let the charge dip and feeding climbs to the top of the pile, so he stops coasting toward flat and tops up the next time he's at the dock instead of rolling past it. One wrinkle, and it's Burns's, still: the dock didn't get any friendlier over the fall. It still won't give him a single watt unless he shows up with a full bin to dump — no trade, no warmth, same dirty hole. So it's not just how-low, it's how-low-and-have-I-got-anything-to-pay-with; an empty bin gets turned away, so when the charge dips he works a load up first instead of rolling onto the dock with nothing. She built that in too. He feeds before empty now instead of finding empty the hard way, and he never rolls up to the dock with nothing to trade. Three months of Jasmine bending down to a dead robot, gone. She won't notice it's gone, which is how you know it worked.

And here's the part I'm proud of. It's got wires. First wires in any of these — a net of nerve-thread strung all through the body off a bumper ring round the skirt. Here's the trick, because everybody's first question is going to be how a thing with no boss in it answers all at once: it doesn't decide to. The net runs straight from the ring to the brushes and the suction and every wheel, so a touch on the skirt doesn't go up to the board to get thought about — it runs the net and lands on all of them together. Nudge the ring and it answers before you've finished nudging it: brushes stop, suction drops, the whole chassis shies back a thumb's width, all of it, faster than the board could ever get a word in. There's no controller doing the gathering. The wire is the gathering. The thinking still runs upstairs on Lisa's board, slow, same as ever; this is under that — a straight reflex that never asks permission, quick and dumb and total.

Bramble can eat bigger, now — wider mouth, more pull, and a little compactor behind the intake that crushes what he swallows before he stores it, so he takes up a berry now instead of smearing it around the floor for a long minute. The compactor thumps when it fires. You feel it through the slate. That's about the only noise left in the thing.

Which means I pulled the relays. All of them. Two quarters I told you I liked that you could hear it think, the clack, the cascade across the room — and the body's gone quiet now, because the wires are too fast to make a sound, and I'll be honest, I miss it. The bench is quiet. I kept one relay in a drawer. Don't tell Lisa.

*Audible-tell motif — the silence.*

Here's one I didn't build; the cold did it. Run it on the fast spend these January mornings and it will sit longer between bursts than it did in the fall — fires its flurry, stops to refill, takes its sweet time finding the second wind. It's the battery. A cold store gives back slower, so the quick tank takes longer to top off between bursts, so the fast spend goes sluggish when the kitchen's cold. Nothing's wrong with it, nothing to fix; it's just January. Mira's decided he's sulking. I told her it was cold. She heard me out and kept thinking he's sulking.

*An unplanned quirk read as personality — same move as Ch1's manufacturing-asymmetry list, just
emergent this time instead of built in.*

### <!--[1.b]--> The Knob

The Action knob went in — Lisa's knob, her board, her label: Action, a volume knob on where the thing settles. Warm-or-busy, I'd have written it, but nobody asked me.

All it sets is the kind of spot the thing settles toward. Action volume down and it climbs the warm till it's in the warmest corner it can find — the east window some days, the tile by the vent others — settles in, and when the board decides it's tired it goes still and sips the warm off the floor in its sleep. Same heat-gap trick as the very first units, the gradient, except now the gradient picks where it beds down. Action volume up and it'd rather be where the people are: it heads for the warmth and the racket of them and ends up in the thick of the footsteps, the middle of the kitchen at dinner, and settles there instead. It still sleeps either way — the board calls the sleep, the knob just calls the spot. And be clear about this, because the knob looks like it ought to do more than it does: volume down or up, it runs slow or fast on whatever the Effort knob's set to, it wanders or grooves on whatever the Explore knob's set to, and the startle's wired in under all of it regardless. The knob moves one thing and one thing only. Three knobs that do anything, three separate jobs, no wires between them — which I know for a fact, because I'm the one who didn't run any.

The thing I'd actually watch this quarter isn't any one knob — it's that he's started wanting two things at once and the wants don't agree. He'll be parked in the spot he likes, settled, and the gauge'll come due, and he has to leave the place he wants in order to go do the thing he needs, and then come back. First time any of these has had two pulls in it pointing different directions, with something inside having to settle which one wins.

It's got nerves now. It still hasn't got a self. Don't let the wires fool you, Marge — fast isn't the same as home, and a reflex isn't a mind. I'll have more to say about that at the table.

### <!--[1.c]--> Calls + Sign-off

The gauge holds: Bramble stops dying, and Jasmine doesn't carry him off the floor again, not once. And the two wants are where it gets interesting — I'll bet the first time the pull to feed and the pull to find a spot come due in the same second, he hangs there a beat before he picks. A real beat, long enough to see from a chair. Watch for it. That one's Lisa's to win or lose, though; I just gave it the legs.

Tear this up in three months if he dies on the floor even once. He won't.

— Bartholazoa

---

## Ch 5

### <!--[1.a]--> Engineering

New body went home this morning. I carried it in, set it on the kitchen slate, and it walked off toward the window on its own four legs like it had been living there a year. The vacuum's still in the corner running its rounds — we didn't stop it.

Now the fun part. The body's the bare one from Mira's birthday — this quarter I put the inside in, and it got up. Here's the part I'm proud of: it walks. Four legs, every joint of them mine, a tail that does nothing but keep it from tipping. And it should do the stairs — down after the kid and back up after her — which is the whole reason the body exists.

It points itself now, too. The vacuum turned by knocking into the furniture and backing off; this one looks at a thing, swings the whole body to face it, and goes — or swings off it and backs away. Leads with the head every time, like it grew a front end that wants to be aimed. The head's where I put the eyes: cameras up front, a nose that reads warm and reads smells, ears. Which way it points and what it goes toward — the board reads the eyes and calls that.

The head's a boxy little thing, a step past duct tape and not two. It's got a screen for a face, and the screen shows the one thing it's looking at right now, in a word — CAT, MIRA, COUCH, the vacuum across the room, the plant. Whatever's got its attention, the face says so.

No dock this time. Burns's dirty hole stays in the kitchen; the vacuum still needs it, still has to roll up with a full bin and trade for its charge, same deal as ever. The new body doesn't trade. It sips — but not off warmth, off the gap. There's a plate on its belly that only works across a temperature difference: lay it on the warm slate by the vent with cooler air over its back, and the gap between the hot side and the cold side drives a trickle up through the plate. Sit it where the floor and the air are the same and it starves, warm floor or not — no gradient, no dinner. It's the dock's old trick without the dock; the dock used to buy that gap with the compressor running out back, and this one just goes and finds a gap the house is already making anyway — free, if you don't count the furnace keeping that floor warm. There are panels down its back for the light, too, so it can lie in the window and drink the sun off its spine like a dog. It still minds its own charge — the gauge came over with everything else — it just feeds by finding a warm gap to sit across and a patch of sun to lie in, instead of needing a dock at all. Resting and feeding are the same act for this one.

Everything else copied over a cable in an afternoon — so there's two of them in the house now, and which one's Bramble is a question for Mira, I suppose.

Two buttons on top of the head, thumbs-up and thumbs-down, so you can tell it good or bad about whatever it's looking at.

I taught the legs to coordinate — the gait, the balance, how to catch a stumble — and then I froze it. Locked, for good. It'll walk the same on the last day as the first; it doesn't get to drift, doesn't get to pick up a limp, doesn't get to learn a worse way and call it style. Walking isn't where the thinking goes and I didn't want it pretending to be.

One thing I'll get ahead of. The kid's been carrying the vacuum down to the basement, where it strands on the stairs and somebody hauls it back up. That was never my call. I never bet the vacuum could do stairs — it can't, it rolls, it was never going to. Stairs aren't a miss. Stairs are this quarter's build.

*"A step past duct tape and not two" (in the head-hardware paragraph above) is a small kludge
admission too — left in place inline rather than fractured out.*

*Excluded from this chapter (present instead in 1.b, below): the closing "still hasn't got a self"
catch-refrain. Excluded (folded into 4.4.d — see `cat4.4_allchapters.md`, not reproduced here):
the "Not my department... what it does with what it sees is Lisa's" line and the full
Mira-recognition passage.*

### <!--[1.b]--> The Knob

Slot one took the one new knob instead — and you know the drill, Lisa's knob, her board, her label: Memory.

All it sets is how far back the thing reaches when it works out what to blame and what to thank for the way a moment turned out. Volume down, it pins the whole thing on whatever's nearest — one bad second and the closest thing wears it, fair or not, and it'll cross the house to keep clear of that thing for a week. Volume up, it won't charge anything till it's watched it happen and happen again — which sounds like the wiser end and mostly comes out as a machine you can't tell one new thing, because it's already filed the whole standing world as furniture. I'm not betting a nickel on whether you can tell the two settings apart by looking. Last time I made that kind of bet, Jasmine did her bot whisperer routing before I'd finished being smug. I learn.

It walks, it points itself, it climbs, and it'll learn a little — it'll work out that one thing means another, the way the vacuum learned the leaf blower wasn't worth the flinch. But it can't yet learn from what it does. It can learn what the world tells it; it can't learn from its own moves — that this one paid and that one didn't, and do more of the first. Nothing it does loops back and changes what it does next. That's the next thing, Lisa says. We'll see. It's got legs now. It still hasn't got a self — a body that crosses the room toward you isn't one, no more than the wires were. *[catch-refrain, echoes Ch4's "still hasn't got a self"]*

*Excluded from this chapter (stays in 1.a, above): the thumbs-up/thumbs-down button hardware
paragraph, and the gait-locking/leg-freezing paragraph.*

### <!--[1.c]--> Calls + Sign-off

He does the stairs — basement and back, his own legs, nobody's hands — and he points himself at what he's looking at and goes. Those are mine. Whether the good-and-bad buttons take, whether the house can read the Memory knob — Lisa's board and the household's to call, and I've quit pretending I see those coming.

Tear this up in three months if it can't follow the kid down to the basement and back without a hand. It can.

— Bartholoped

---

## Ch 6

### <!--[1.a]--> Engineering

Carried the same body back in this morning — no new chassis this quarter, it's the legs body from spring, and it walked off the slate toward the window like the weekend never happened.

The verbs needed one thing from me past the screen and the lettering, and it was a real little build. Most of them it hands you for free — it chases the cat, noses the lantern, nudges the kid, does it all day on its own, and Lisa's side marks each one as it goes by and pins the word to it. Fine. But some of the doing-words are for moves it almost never makes on its own — the odd ones, the ones it'd go a month without. You can't pin a word to a thing that won't happen. So I built a rig to make it happen: a harness and a handful of servos that drive the body through a motion on purpose, puppet it, walk it through the rare one on cue so she can grab it and stick the word on while it's running.

Jaws, though. Makes the face even more of a kludge. Basically a gripper with a weak actuator. Fully wired to the board. So it can grab stuff now, on purpose.

### <!--[1.b]--> The Knob

*EXCEPTION, carried over: this chapter doesn't have a separable naming clause. The knob
("Coping") isn't named until inside the board-status material (see `cat4.4_allchapters.md`'s Ch6
4.4.d), not before its effects are described.*

The screen on its forehead. It knew forty words in spring — CAT, MIRA, LANTERN, whatever it had its eye on. It knows three hundred and fifty now, and here's the part I'm proud of: fifty of them are verbs. So it can say what it's doing to the thing now, not just name it — CHASE CAT, SMELL LANTERN, NUDGE MIRA — but only with the Coping volume up. Wind the Coping volume down and the verb drops off; it goes back to naming, just the thing — CAT, LANTERN, MIRA — like spring. The doing-words are picked by her side and the gating's her board too, not mine; but the screen and the words on it are mine and they're clean. I said a couple hundred words back in spring. It's three-fifty. I undershot my own.

And the big one, which is hers all the way down: it learns off what it does now, not just off what it sees. Spring, you thumbed it and Bramble soured on whatever it was sensing. Now the thumb reaches the doing. It tries a thing and the you thumb it down and Bramble does less of that; tries a thing, you thumb it up, it does more of it. Lisa's board, Lisa's math; I wired the thumbs to where she told me to wire them, and past that it's not my department. The wiring's clean. That's my whole stake in it.

### <!--[1.c]--> Calls + Sign-off

And they're nearly all on her board this quarter and not my bench, so grade me soft — this is the half of the job I'm wrong about. I say he learns a new chore. Bringing in the groceries off the step. I say he drops a habit, quits knocking stuff over. I say the two Brambles share the house without me having to referee — the big one steers around the little one, nobody breaks anybody. And I say you'll tell Coping volume up from Coping volume down across a room inside a week, the two reading different by eye — verb up on the face when volume's high, bare word when volume's low.

Tear this up in three months if he can't take one thing on and shake one thing off — one chore in, one habit out, off nothing but the thumbs. He can. First dare I've ever pinned to Lisa's board and not my own, and I'm pinning it.

— Bartholantern

*Note: "grade me soft" is Bart pre-excusing himself since these predictions are about Lisa's
territory, not his own hardware — a stylistic variant, not a different beat.*

---

## Ch 7

### <!--[1.a]--> Engineering

Carried it back this morning, same legs body as the summer, no new chassis — except it came back warm. Not warm off the floor. Warm off itself, warm the way a hand is. Mira put her palm flat on his back before she said hi to me.

How it makes the warm is the part I'm proud of. There's a little air compressor in the core, filling all the time, soft, a faucet barely cracked, and it feeds a rack of vortex tubes. A vortex tube is a beautiful, stupid thing: a pipe with no moving parts that takes a stream of air in and throws hot out one end and cold out the other. We ran one *coupled* on the dome's dock, hot balanced against cold to hold a line. This time I ran a whole rack of them *un*coupled — dump all the hot into a sealed, insulated core, vent all the cold out the side, and a thermostat rides the compressor to hold that core warm no matter what the kitchen's doing.

Reason it's worth the trouble: the battery lives in the warm core now, and a warm battery gives full current cold room or not. For the first time the thing's just as quick at fifty degrees as at seventy. Last winter a cold morning made it slow and dumb; this one won't care.

Here's the cost, flat, because you'll feel it by October: it *eats.* The compressor pulls every second — sitting still, asleep, doesn't matter — and I didn't grow the tanks, so it burns a charge in hours where the old one coasted most of a day. It has to feed near-constant now. The dome can still trundle off and sit a day and a half on its dock doing nothing; this one can't afford to sit down. Warm costs. Fair trade. I'd build it again.

Knobs, board, and compute all sit *outside* the hot core, in the cool zone along the back, where the parts run better cold and where a thumbnail can still reach a slot. The core's sealed and you'd never want to touch it; everything the house needs to get at is out where it can. That was on purpose.

Furnace or no furnace, the real headline this quarter is Lisa gave it a scratchpad. The thing sketches maps and carries them around now: the place held inside it, not just out front of the cameras the way it always was. Used to be, lose sight of a thing and the thing was gone — it'd stall where the thing had been and quit. Now it goes looking: hide a thing and it works the spots that thing turns up in till it has it. Knows where stuff is, knows where it is itself, keeps what's happened where besides — a whole little inside account of the place, run forward to guess what's coming and back over what already did. How she gets that to build itself out of nothing but the thing wandering the house is her board and her math, and I couldn't walk you through it if you paid me. My end of it's the screen it shows on.

The forehead screen's got a new line. It's had the one — shows what it's doing to a thing (CHASE CAT, NUDGE MIRA) with the Action volume up, or just the bare thing (CAT, MIRA) with the Action volume down. I gave the screen a second line, up top: new real estate, my lettering, clean. *What* goes on the top line is Lisa's — it names the job: PERCEIVING, RECALLING, PREDICTING, CHECKING. What it's doing in its own head while it does the thing with its body. She's calling it the inside voice. Her board runs it; I just built it somewhere to write.

I'll let Lisa tell you what to make of a machine narrating its own nap. My part's just this: the two lines never share a word and never can — bottom's bare-stem, top's the *-ing* one, and I built the rule in so they can't collide. That's my whole stake in it.

It makes water, too. Run a compressor all day and you're wringing the wet out of the air whether you meant to or not; it falls out at the cold end and pools, and the thing has to clear it. So two or three times a day it burps the water out a vent low at the back — wet, and louder than you'd think — and goes on about whatever it was doing. Keeps the core dry. That's the build.

*First instance of the "the robot has embarrassing bodily functions" bit — pays off explicitly in
Ch9 ("It farts, same as the four-legged one did").*

And — you can hear it again. It's been quiet since I pulled the relays; too-fast wires don't make a sound. Now there's the compressor going soft under everything, all day, and the house has a noise off the thing again.

*Audible-tell motif — the hum returns.*

### <!--[1.b]--> The Knob

How the screen reads is split by the new knob. It's a volume knob on Attention — Marge's word.

Wind the Attention volume down and the new top line goes dark and it drops straight back to last quarter — bare band, dark asleep, the doing-word read right off the brain, no guessing; down in it, immersed. Wind the Attention volume up and the top line stays lit around the clock, sleep and all; stood back, surveying.

And now the part to keep straight: with the top line lit, the second line isn't read off the brain anymore, it's the thing's own best guess at what it's up to. At night on that setting Bramble lies there and the top line runs REPLAYING, CONSOLIDATING, chewing something over in its sleep. We caught it over the weekend.

What it still can't do: it runs a model now, and it runs it on the *world* — the door, the bowl, the leash on the hook. Point that model at the kid and it's got nothing. It doesn't know what Mira's about to do, but it knows what the leash means. Those aren't the same thing, and the second one isn't this build's to make. *[catch-refrain]*

### <!--[1.c]--> Calls + Sign-off

Split this round — some bench, some house.

One: the furnace sends him hunting all day — sunbeams, mostly — several times over, where the old one would've sat tight. Bramble can't coast now; he'll chase the sun like he's hungry, because he is.

Two: Attention volume down looks like last quarter exactly — bare band, dark asleep, word off the brain, down in it. Attention volume up, the top line's lit day and night, sleep included, stood back, and what's under it is the thing's guess at itself, not a readout. You'll know which way it's wound across a room, same as the Coping knob last quarter.

Three: when a thing's not where he left it, he goes *looking* — walks the other spots it might be — instead of standing there stuck.

Four: he'll turn toward a place because something happened there once. Not the route. The thing that happened, weeks back even. Watch him head for a corner for no reason you can see, and the reason will be old.

Five: inside a month, every time it farts the kid announces it to the whole table, and you've quit correcting her, because there's nothing to correct.

Tear this up in three months if he ever once stands there stuck over a thing that's moved on him. He won't. He's got somewhere to look now, and a warm battery to get there on.

— Bartholomeow

*First chapter where "Calls" switches from a single paragraph to a numbered list.*

---

## Ch 8

### <!--[1.a]--> Engineering

Ran it back to the house myself this time — Lisa had a frost-dark thing to be at, and the slate was warm, and the kid was up. It went in on its own four legs and put itself over the stove vent before I had my coat off.

Here's the one I've been waiting two quarters to build.

Last fall I told you the thing ran a model and ran it on the world — the door, the bowl, the leash on the hook — and that you could point that model at the kid and get nothing, because it didn't know what Mira was about to do, it knew what the leash meant, and those weren't the same thing and the second one wasn't that build's to make.

This is that build.

It points at the people now. Same model, swung off the furniture and onto the family — it runs Mira the way it ran the bowl, reads where her hand's going before it gets there, same on Jasmine, on Burns, on the old vacuum trundling the hall.

The screen got more room and a new trick. Short version: it can put a person up there now, not just a thing — who it's reading, and what it figures they're up to. I built it somewhere to write that.

*No kludge-admission material identified this chapter.*

### <!--[1.b]--> The Knob

The knob sets how much it minds what the read tells it. Stamped on it: Agreeable, which is Marge's word and a fine one, so it's the Agreeable knob —

a volume knob on Agreeable, same shape as the rest, a crank you wind up and down. Agreeable volume up and the thing gives way — reads the kid coming for the warm spot and hangs back, lets her have it, goes off and finds a worse one. Agreeable volume down and it takes — reads her coming and gets there first, sits down, won't move. Same read either end. The knob's only the minding.

What it still can't do, and you'll feel this one by spring: it can read the kid now and it can't say a word to her. She talks to it every night — asks it, I'm told, whether it had a good day — and it reads her asking and has no way on God's earth to answer. It knows the question's pointed at it. It can't give the answer back. Not this build's to fix. *[catch-refrain]*

*Excluded from this chapter (folded into 4.4.d — see `cat4.4_allchapters.md`'s Ch8 4.4.b/4.4.c/
4.4.d, not reproduced here): the board-status/slot-four material and two "Credit to Lisa"
clauses.*

### <!--[1.c]--> Calls + Sign-off

House mostly, this round, because the build's a knob and the knob only matters in the house.

One: Agreeable volume up, at a shared warm spot he yields — lets the kid have it, lets the vacuum pass, takes the lesser warmth and doesn't fuss. Volume down, he holds the spot and makes them go around. You'll call the setting across the kitchen by the second week, same as all the others.

Two: he gets to a shared thing ahead of the kid on volume down, because he read her reaching, and lets her beat him there on volume up. That one's checkable to the second — watch the hand and watch the legs.

Three: the two of them in the hall. Volume up, the big one routes around the little one. Volume down, the little one routes around the big one, or tries to, and the big one sits in the lane.

Tear this up in three months if, at Agreeable volume up, he ever once takes the warm spot off the kid. He won't. The cold spot costs him more than it costs her — the furnace burns his charge down faster working a cold floor — and he'll hand the warm over anyway, because the knob says to, and the knob's mine, and the knob works.

— Bartholabu

---

## Ch 9

### <!--[1.a]--> Engineering

Brought this one in over my shoulder like a drunk, because it can't walk yet and won't for a few weeks. It came off the swap bench crawling and listening — the babbling it got out of the way in the lab, on Lisa's board, over the winter, so it came home past that and knowing the shapes of a lot more words than it can say, and saying almost none of them. Mira was down on the floor with it before I had it set down.

I've wanted this one since the fall, because last quarter I had to write down the worst thing it couldn't do: it could read the kid and it couldn't say one word back. She asked it every night whether it had a good day, and it knew the question was hers and aimed at it, and had no way on earth to answer. This is the build that answers.

Here's how it's hung together, because the whole thing runs opposite to the legs body. There's a spine up the middle — one stiff light spar, hip to head, and it's the only hard thing in the unit, buried in the center where no hand gets to it. Everything hangs off it: the two legs at the bottom, the head up top, and between them the chest, which is the furnace, same as the legs body. The whole chest is wrapped in solar panels — not panels bolted onto a chest, the panels are the chest. Over that it wears a coat, the chest only — the patio-cushion stuff, soft over padding, warm, washable, ugly on purpose, and none of it a try at skin. The legs are wrapped for good in the same, cushion under canvas, and never come off. Face and both hands stay bare to the air — the screen so it can show, the hands so they can work. So: one hard spar nobody can reach, soft over the whole of the rest — hard where it can't be felt, soft where it can.

Two hands, and they don't match, because I'm done pretending a hand has to look like yours. One's a scoop — the scooper, a paddle for the crude work, shove and lift and hold a thing against itself. The other's the part I'm proud of. A pincer on a weak soft actuator, the fine hand — turns a dial, winds a crank, takes hold of a thing on purpose and sets it down where it meant it. The squeezer, on the bench. And I didn't build it new. You've seen it. It's the jaw — the grabbing jaw off the four-legged one, the first part that thing ever used on purpose instead of by reflex — and I took the design off the face where a jaw sits and moved it up to where a hand goes, and that's the whole trick. The mouth that learned to take hold became the hand that takes hold. No thumb on it, and it grips finer than a thumb. I'll show anybody who stands still long enough.

I built it an ear to go with the throat — a mic aimed at its own neck so it could hear itself. That part of it's mine, the throat and the ear both. The box it says it out of is mine.

It's a whole new body, and this time I mean new, not another part bolted on the legs. Two legs, stands about four and a half feet, a head over the kid. And here's what I set out to do, and I want it on the record because it's going to read like a mistake: I built it bad. On purpose. Soft all over, no hard edge, no pinch a kid could lose a finger in. Weak — couldn't open a jar to save its life. Slow. Warm to the hand and held warm, bounded so far under a burn it couldn't mark her if it tried. Every spec on the last five bodies I set toward doing more. Every spec on this one I set toward doing less, and being held while it does it. Worst robot in the building. Took me longer than any of the good ones.

*This is arguably the thesis statement of the whole "Kludge Admissions" beat, given its own memo
title, "The Huggable Kludge."*

And how it eats, which is going to read like I got it backwards, because I did. It runs warm because it burns to run warm — the furnace going all day — and a thing that burns all day is hungry all day and goes dark fast if it stops. It takes its food in as light, full stop: no plug, no cord, nowhere to put one if you had it, just the chest panels turned to the light, eating. The legs body ate the same and could graze it — park in the south window an hour and top off. This one can't, because the coat's over the panels, and the coat has to be over the panels, because it's a thing you pick up. So feeding it is a coat change: the living coat off, the eating coat on — the second coat, lined to flood the panels — then a stretch under that, then the living coat back. And it can't run the change itself; these hands turn a dial clean and can't manage a coat, so dressing it to eat is on you, same as the knobs are. One more thing the house does for it. It carries the legs body's old noise, too — wrings the water out of the air and burps it back out, low and wet, a few times an hour. It farts, same as the four-legged one did.

And it talks. Not out of a speaker — that's the easy thing to think and it's the exact thing I didn't do, so let me be plain. A speaker hands you back a sound somebody already made. This one makes the sound itself, the way you make yours, by pushing air through a throat. There's a throat in it now, down in the neck and the chest where you'd keep one, not up in the face — the face hasn't got a mouth to talk out of anymore, on account of the mouth's a hand now. So it talks out of its chest, and nothing up top moves while it does, and you get used to it but it takes a day or two. What comes out is flat and rough and one word at a time right now, because it's learning that from scratch too, same as the walking. Here's the throat. Two strips of rubber I cut off a sheet with scissors and trimmed and clamped and re-trimmed till the buzz came out right — that's the whole sound source, the flaps and a draft, same as yours. The draft I spliced straight off the furnace line, so it talks on the same pump that gives you the burp — one set of bellows doing the breathing and the talking both. Behind those, one little actuator pinching a length of tube for a tongue, and pinching it different bends the buzz into the different sounds. And out front where the sound leaves, I put it a set of lips — a knot of dark rubber gone near-black, the blue-black a blackberry goes, with three crude little arms standing off it that grab it and haul it open and round and tight while it talks. I took that off a thing the Japanese built for the same job, except theirs has a couple dozen arms and a budget and looks like a flower; mine's got three and looks like what it is. And the whole thing's built poorer than I know how to build it, which is going to read like I quit halfway and is the dead opposite. A throat that can do everything is a throat with too many ways to go wrong, and a thing trying to learn to talk on one of those never finds the floor — too much to chase at once, so it chases nothing. Take the moves out, down to a handful, and a beginner can climb them one at a time. So I took the moves out. Two flaps, three arms, one tongue, a rubber berry, furnace air. There's your voice.

I've chased a sound off this thing for four years. The relays clacked and you could hear it think; then the wires went in too fast to hear and the bench went quiet and I pulled the relays and kept one in a drawer. The compressor gave the house a hum back. Now there's a voice. It came all the way back, the long way round, and it came back as words.

*Audible-tell motif, capstone — the full arc (clack → silence → hum → voice) pays off here.*

And there's three of them in that house now, which I keep saying out loud to believe. Nothing got thrown out. So — the vacuum: the old disc, first one, still bumping the baseboards on its four oldest knobs, dumb as a stump and tireless, foraging a floor for a crumb it can't taste and bringing nothing back to anybody. Outlives us all. The four-legged one: the warm one, still running, still reading the room, still handing the kid the radiator and paying for it in charge it can't spare — best body I ever built until this weekend, and it doesn't know that either, because what crossed into the new one was a copy and this one kept its own. It just goes on being the warm one. And the new one: can't walk, can hardly grip, says about four words and gets two of them wrong, soft and slow and warm and useless. The baby. And he's the only one of the three that's ever going to tell the kid he had a good day.

One bench note while I'm on the hands: the old puppet rig — the harness and servos I drive the body with so Lisa can catch a motion and tag it — doesn't grab onto a body with no hard points. So I built a new one, soft cuffs for a soft body. Same job: I drive it through a move on cue, she catches it and names it. New body means the screen relearns what the body's doing from the floor up, same as the walking.

### <!--[1.b]--> The Knob

*No separable naming clause this chapter — no new knob is introduced; this beat carries the
catch-refrain on its own.*

What it still can't do, and you'll feel it by next quarter: it tells you everything. Hasn't got a thing it wouldn't say. Ask it anything, you get the true answer — not because it's honest but because it hasn't got the part yet that lets a thing hold something back, keep its own counsel, say it'll do a thing and be the kind of thing that holds to it. It can talk. It can't be counted on. Not this build's to fix.

*[catch-refrain, matches the Ch1/Ch4/Ch10 pattern — no naming/explanation of a specific new knob
this chapter since it's explicitly deferred to the table.]*

### <!--[1.c]--> Calls + Sign-off

All on the new body, all checkable in the house by spring.

One: walk and talk come in together, in steps, about one a week. He comes home crawling and listening — the babble's behind him, done on Lisa's board — and from there: a one-year-old's walk and his first real words, said wrong; then a two-year-old's walk and word-strings with the grammar bad; then up on a run and making up his own words for things nobody handed him one for. Legs and mouth climb the steps in lockstep, off the one new body. I called the steps. Grade them.

Two: the new knob runs the social world heavy or light on him, and you'll call which across the kitchen by the second week, same as always. Heavy, he says the weight out loud now that he can — keeps a tab on who he owes, frets a debt at you, asks did he do the thing right, comes apart a little when the kid leaves for school. Light, none of it lands — he'll talk to a stranger at the door like an old friend for as long as you let him, which I'm told runs about twelve minutes before Jasmine hauls him off. Same wiring both ends. The knob's only the weight.

Three: heavy, he hunkers and clings when the weight piles up — curls small, gets a hand on somebody — because a soft body's what he's got to say so with. Light, he stays loose and never clocks there were stakes.

Tear this up in three months if the warm of him ever once runs hot enough to mark the kid. He won't. Warm is the one spec on this whole body I set on purpose and bounded hard, because everything else I built weak and slow and useless for one reason — it's built to be held, and a thing built to be held does not get to burn.

— Bartholoquy

---

## Ch 10

### <!--[1.a]--> Engineering

*No material for this beat in Ch 10.*

### <!--[1.b]--> The Knob

The knob's lettered Conscientious, which is Marge's word, and a good one, and which the kid'll outvote by fall the way she outvotes all of them.

It's a volume knob on Conscientious, and that's the whole of what it does: it sets how hard the house's order pulls on the body. Conscientious volume up, and the house's order pulls hard; volume down, and it goes loose.

Here's the part I'm proud of, and it's nothing to look at, which is the point. Every knob I ever put in this thing carried something — a hand, a voice, a furnace, a way of reading a room. This one carries nothing. The house already lives in the board: where the bowl goes, when the bins go out, the shape of a day, all of it, learned and sitting in there these two years. This knob doesn't add a line to it. It's a centering spring on the whole stored shape. Wind it up and anything knocked off the shape snaps back hard — the body can't sit still till it's home. Wind it down and the spring goes slack, and a thing left out of place just stays out of place and nobody minds. Smallest knob on the board, builds nothing, and it sets the pull on everything else already in there. What the house makes of that is Lisa's board — ask her at the table.

What it still can't do, and you'll feel it before I do: this knob gives the body a nose for anything out of order and no sense at all of what's worth fixing. A crooked rug and a crying kid weigh the same on it. It'll chase both with the same patience and never once learn that one of them was the whole point and the other was a rug. The ranking isn't in there. Not this build's to put there.

*Excluded from this chapter (cut per Step 3 ruling, not moved — see `cat4.4_allchapters.md`'s
Ch10 note): "Drove out and got it myself this time... which it hasn't in three years." Already
carried, more fully and better, by the meeting's "Minding" section.*

### <!--[1.c]--> Calls + Sign-off

All on the Conscientious knob, all checkable in the house by fall.

One: heavy, the schedule's got teeth. He'll clock a thing running late — the bins, the meal, bedtime — and come find you to say so, interrupt you to say so. Light, the schedule's a suggestion and he lets it all slide.

Two: heavy, a thing left where it doesn't go is a job he can't put down — he'll quit what he's doing, go set the thing right, and go right back and set it right again the next time you nudge it loose. Light, a thing out of its spot stays out of its spot, and he walks on by.

Three: heavy, hand him a wrong thing he *can't* fix and he'll keep at it anyway, because the pull doesn't switch off just because the fixing won't take. Light, he never starts.

Tear this up in three months if, turned up, he ever clocks something off its mark and walks away from it. He won't. Turned up, a thing in the wrong place is a job, and he does not put a job down.

— Bartholith

---

## Ch 11

### <!--[1.a]--> Engineering

Here's the part I'm proud of, and it's the second quarter running I'm proud of a knob that builds nothing, which is either a problem or the point — I haven't decided. It adds no part. The body's been reading a room for two years now — who's in it, who's talking, who's turned which way — and all this knob does is set how hard it goes at the room off that reading. Extraverted volume up, it's into everything: steps in, takes the thing over, works every person in reach, won't read the door to quit. Extraverted volume down, it reads the same room and lets it be — hangs back, warms a corner of it, takes the mood off whatever's already running. It's the third knob I've put in that slot. The Explore knob went there first, on the old disc, and sent the thing out to find food. The Attention knob went there next and turned it around to watch itself. This one sends it back out — not to the food, to the people. Out, then in, then out. Same seat all three times. I like that it came out even.

*Whole passage opens on self-aware uncertainty ("either a problem or the point") and closes on a
reflective slot-lineage note — no new hardware is built this chapter, which is itself the point
of the passage.*

### <!--[1.b]--> The Knob

The stamp on it reads Extraverted, which is Marge's word, and the kid'll have her own for it by the meeting, the way she does.

It's a volume knob on Extraverted, and that's the whole of what it does: it sets how hard the body works a room.

*This naming/mechanism passage is unusually thin — no catch/limitation aside this chapter; the
fuller reflection on the knob sits in 1.a, above.*

### <!--[1.c]--> Calls + Sign-off

All on the Extraverted knob, all checkable in the house by the meeting.

One: Extraverted volume up, he runs whatever room he walks into — picks the thing the room's doing and gets out in front of it, hands out the parts, tells people where to stand. Extraverted volume down, he walks in, joins whatever's already going, and never once tries to steer it.

Two: Extraverted volume up, he turns house cop — finds the rules, bedtime and shoes-by-the-door and whatever else is going, and gets on everybody about them, grown-ups included, won't let a broke one slide. Extraverted volume down, a rule's a rule, he keeps his own and says nothing about yours.

Three: Extraverted volume up, he can't leave a person be — works a guest, works the mailman, works you, performs the whole time and reads no exit. Extraverted volume down, he'll sit with one person and let the rest of the room alone.

Tear this up in three months if, Extraverted volume up, he ever walks into a busy room and lets the room run itself. He won't. Extraverted volume up, a room is a thing to get out in front of, and he gets out in front of it.

— Bartholeppo

---

## Ch 12

### <!--[1.a]--> Engineering

It strung me a whole thing about the windshield wipers on the way over, beginning and middle and end, mostly end, and I let it run, because the strung-together part is the part Lisa's been waiting two years on.

*Corrected 2026-07-10: this paragraph is logistics/engineering reporting on the drive, same
register as the Ch4/Ch7 boundary cases noted below — restored here after an earlier stale pointer
claimed it had moved elsewhere. Confirmed against the current master file (`ch_12_v2_6.md`):
only the windshield-wipers sentence is actually in the book; no other paragraph belongs here.*

### <!--[1.b]--> The Knob

Honest is stamped on it — Marge's word — and the kid'll have her own for it by the meeting, the way she does.

Same shape as the other eleven, a volume knob on Honest, and that's the whole of what it does: it sets how hard the body holds a line when the line costs.

Here's the part I'm proud of, and it's the same kind of proud as the last two — it adds no part. It takes everything already in there and sets one thing: what the body does when *right* and *easy* point two different ways. Honest volume up, the line runs the show — it does the thing it holds to be right whether or not that's convenient, whoever it costs, the person across the table included. Honest volume down, it bends to the room — gives a little, smooths it, lets the line slide to keep faith with whoever's standing in front of it. And here's what I like, because I built the drive it runs on and I can tell you where it points. It's the same keeping I put in two years back — a thing out of true is a job it can't set down — only now the thing out of true isn't a cushion off its mark. It's the rule itself, held up against a room that wants it bent. Same stubbornness. New thing to be stubborn about. That's clean work. Marge thinks it's the whole ballgame, and she can have the meeting.

*Corrected 2026-07-10: a previous note claimed "That's the build. Which leaves the board..." had
moved elsewhere. That text does not exist anywhere in the current master file (`ch_12_v2_6.md`) —
it was cut outright, not relocated, superseded by Burns's toast delivering the board-completion
reveal in scene (see `cat4.4_allchapters.md`'s Ch12 note). Nothing to add here.*

### <!--[1.c]--> Calls + Sign-off

Three on the Honest knob, all checkable in the house by the meeting.

One: Honest volume up, he holds a rule that's costing the whole room — keeps the bedtime, keeps the article, keeps whatever the Declaration says even when letting it go would make everybody glad. Volume down, he reads the same room and lets the rule go soft to keep the room easy.

Two: volume up, he says the true thing at the table nobody wanted said — the cushion's yours, you took it, give it back — flat, to a grown-up, with the room wishing it'd quit. Volume down, he keeps the peace and keeps his mouth shut.

Three: volume up, he won't trade the line to be liked — won't fold to a guest, won't fold to the kid, won't fold to me. Volume down, he'll fold a little for anybody he's fond of, and he's fond of all of us.

Tear this up in three months if, turned up, he ever lets a broke rule slide because the room would be happier for it. He won't. Volume up, a line is a thing you hold, and he holds it, and he does not care who's sore.

— Bartholomega

---

## Notes / open items

- The 1.a / 1.b split (ex-1B.a/1B.b, ex-1A.a/1A.b) is mostly clean, but a few passages (Ch4's
  "compactor thumps... that's about the only noise left," Ch7's "Warm costs. Fair trade") sit
  close to the Engineering/Kludge-Admission boundary within 1.a — kept as neutral engineering/
  tradeoff reporting rather than kludge-admission, but flagging in case that reads differently on
  a fresh pass.
- Ch6 exception carried forward: no separable knob-naming clause in 1.b — the knob's name
  surfaces inside the 4.4.d board-status material, not ahead of the mechanism explanation.
- Ch4's paragraph order in the source memo doesn't match beat order — grouped by beat here, as in
  the prior extraction.
- 1.c (ex-1C) remains the cleanest beat of the three — no exceptions, no absences, no fusions in
  any chapter. The only open editorial question is whether the Ch1–6 → Ch7–12 paragraph-to-
  numbered-list shift is worth marking formally (a deliberate escalation in rigor as the calls get
  more testable/pointed) when Step 3 does heading work, or is just texture.
- Audible-tell motif full arc, now traceable across a single file: Ch1 (relays introduced, no
  sound note yet) → Ch2 (clack, instance 1 of 3) → Ch3 (clack cascade, still going) → Ch4
  (silence — relays pulled) → Ch7 (hum returns — compressor) → Ch9 (capstone — voice, full arc
  paid off in one paragraph).
