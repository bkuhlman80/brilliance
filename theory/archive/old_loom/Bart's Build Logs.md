# Bart's Build Logs
---

## Chapter 1 — Five units, out the door
*Bart, hardware. Filed February 12, 2031, for the team.*

Lisa's running these over to the Burns place this morning, so here's everything in the box before anybody makes me explain it twice.

Here's the part I'm proud of. There's no battery in these and no plug, and they don't run on heat — they run on the *difference* in heat. Each unit's got two little heat-transducers, and a transducer doesn't care how warm the room is; all it cares about is that the floor is warmer than the air sitting on top of it. Jasmine's radiant floor holds around 27 degrees and the room air sits around 21, so there's a six-degree gap just hanging there doing nothing, and the transducer reaches into that gap and skims a trickle of work out of it. That's the Seebeck effect, and it's a genuinely beautiful piece of physics — I'll explain it to anyone who stands still long enough. Park one on the warm floor and an hour later the slate underneath it is cold. That cold is the work coming out. The unit's eating the gap.

Now, here's the thing about that trickle: it's nothing. A few thousandths of a watt. You can't run a motor on it — can't make anything turn, can't even hold a light on. So I don't try. Each transducer drips its trickle into a tiny store, and when the store's full enough it dumps the whole lot into its actuator at once — one hard flinch. The actuator's just a little kicker: it knocks a stubby angled foot against the floor and the unit hops a hair in one direction, then sits there the better part of a minute filling back up before it can flinch again. That's the twitch, and that's the whole way it moves — no wheels, no motor, just a stack of tiny kicks against the slate, like a buzzing phone walking itself across a table, except I get to aim it. Two kickers to a unit, each with its own store, never quite firing together — that stagger is the personality.

And none of it happens unless you crank it first. The crank arms a little escapement — call it the part that gives each kick permission to fire. The heat's the muscle; the crank's the say-so. Leave one uncranked and it'll sit dead on a warm floor all day. And every flinch nibbles a notch off the crank's tension, so after about a week of kicking it goes slack and quits until somebody cranks it again — six turns of the key, about a week of running. Takes both, is the point: Jasmine's floor to move it, a crank to let it. Lose either and it's a paperweight.

No chip, no sensors, no memory — nothing telling the two kickers what to do. They fire on their own clocks, and I seeded each one different on purpose so they're not clones:

- **1** — cranked hot on the left pair, so it lists that way and burns through its tension fast. A busy little thing; always looks late for something.
- **2** — slow and low, with long pauses between kicks. Sits, then goes, then sits. More patience than you'd want in a roommate.
- **3** — the quiet one: even pairs, low draw, the fewest kicks of the lot, so it does the least and outlasts everybody — still ticking Wednesday when the rest have gone slack. The one only an engineer loves.
- **4** — lopsided, on purpose. The pairs don't match, so instead of going anywhere it grinds in place and wears a groove into itself over the weeks. If the contest let me ship four, this is the cut. It's in the box to make five.
- **5** — the show unit. Even like 3, but I let it kick hard, so it runs a clean little circuit and burns through its tension fastest of the lot. Wears even, though. Pretty to watch.

Calls. If the kid picks a favorite, my money's on 5 — it moves the most and it moves the prettiest, and that's what wins a four-year-old. Maybe 1, if she likes a mess. Nobody's going to look twice at 3, and 4 ends up in a drawer by July. What the *house* does past that — who picks what, where they set them, whether the floor stays warm enough to run them — that's not my department. I build the units. The house is Marge's animal.

I still haven't found where the personality knob goes. Contract says every robot's got one, and so far all I've got is a crank — and a crank's just on or off, you crank it or you don't. There's a dial somewhere in this thing's future and I haven't found its shape yet. I will.

Tear this up in three months if I called it wrong. I didn't.

— Bartholomew

---

## Chapter 2 — Knob two, one unit up
*Bart, hardware. Filed June 2, 2031, for the team.*

Lisa's running the upgraded one back to the house this morning. Scorecard first, now that I've got a quarter on the books.

Last quarter's calls. The bodies were five for five — every unit did exactly what I tuned it to do, which is the part of this job I'm never wrong about. The rest didn't go my way. I said the kid would pick 5; she picked 3. In my defense, 5 still moves the most — it just turns out moving the most isn't what wins a four-year-old, which is a kid problem, not a 5 problem. I said nobody would look twice at 3, and then the kid looks at it, names it, the project gets named after it, and it's the one we just upgraded — so, fine, somebody looked twice. I said 4 would be in a drawer by July; it's under the toaster in a folded towel, which is a drawer with a blanket, so I'm calling that close enough. And the personality knob I couldn't find last quarter turned out to be the crank the whole time — the say-so I'd written off as on or off. The house is the knob, technically: the kid cranks it, the kid's the dial. I don't love that. It's right.

Now the fun part. We upgraded one unit — 3, the one the house calls Bramble — and left the other four stock.

At protocell this thing only ever twitched: two kickers firing on their own clocks, and it'd hop around the floor like a bug with somewhere to be and no idea where. Now it *hunts*. Same two kickers — I didn't give it new muscles — but I put a chip in the middle that decides *when* each one fires. That's the whole upgrade. Fire them so the hops add up in one direction and it crawls that way; fire them so the hops add up to a spin and it turns in place; don't fire and it sits. Two idiots kicking on their own schedule became two idiots kicking on a downbeat. Still no wheels. Still hopping across the slate a hair at a time. It just hops with *intent* now.

What tells it which way to go: four little light sensors around the floor seam, each aimed a few degrees up and pointed a different direction. They all read brightness at once, and if they agree there's more light over *there* than anywhere else, the chip knows which way "there" is. That's the trick — finding a sunbeam with four parts that each only know one number.

The chip's an STM32, my pick, and it's the right pick. It runs a dumb little table Lisa and I wrote that fits on an index card: three states. Clear direction, kick toward it — that's RUN. No clear direction, spin a random amount and read again — that's TUMBLE. Battery filling faster than it's spending, sit still and let it fill — that's STOP. The screen up top shows which one it's in. And I ran the whole signal path on relays — coil-and-armature, the kind that clack — so you can hear it think: a little clack-clack-clack every time it changes its mind. I like that you can hear it.

New since February, all told: a battery (not the cells I wanted; you don't always get the cells you wanted), two solar panels down the long sides, a converter to keep the battery topped, the chip, the relays, four sensors, and a second knob next to the crank — heat or light, pick what it eats.

Calls. It seeks — that's the whole upgrade. It hunts the gradient instead of sitting in it.

The shove is the one I want on record. It crawls toward the light, and the other four don't crawl anywhere — they sit where they're set. And nothing in the table tells it the others are even there; they're not sensors, it can't feel them, far as the chip knows the floor's empty. So when a stock unit's parked in the beam it wants, the upgraded one just keeps hopping into it. It's not strong — one kicker-hop is nothing — but it never quits, and the stock one's got no drive to push back with, so on the slick slate, half a foot at a time over a morning, the stock one ends up out of the sun and mine ends up in it. Won't work on anything soft — a rug would eat the hops — but the kitchen's slate, so: every sunny morning, clean as you like. That one's my favorite. It does exactly what it's built to.

On the light setting it won't need cranking on Sundays anymore — panels feed the battery, battery runs the unit, it goes all day on its own. The crank's just an emergency starter now: it spins a little dynamo I added, so a few turns put enough charge in a dead battery to wake it up when there's no sun to be had. Off the leash.

It's getting crowded down there, though — two knobs now, plus a screen, panels, a converter, sensors round the seam, and I've still got ten knobs to find room for. And hopping's a lousy way to travel: it gets where it's going, but it lurches the whole way. I've got a fix in mind for next quarter.

Tear this up in three months if it doesn't hunt exactly like I said. It will.

— Bartholomood

---

## Chapter 3 — Five into one
*Bart, hardware. Filed September 1, 2031, for the team.*

This one I did myself — took the lot to the bench Friday and had the weekend on it, so I'm running it back this morning. Scorecard first.

Last quarter's calls, and I'll take the whole board again. I said it would seek, and it seeks. I said it would hunt the gradient instead of sitting in it, and it does. I said on the light setting it would run off the panels and not need a Sunday crank, and it hasn't. And I put the shove on record — drives into a stock unit sitting in the sun, leans on it half a foot at a time across a morning, ends up in the beam itself — and that's what it's done every sunny morning since June. Called it dead on. Marge tells me it started some kind of conversation at their dinner table. Couldn't tell you. I wired the shove; it shoves.

Now the fun part, and there's a lot of it this quarter, because this is the first time the thing's a real machine instead of a bug.

It's got wheels. Finally. Last quarter I told you hopping was a lousy way to travel and I had a fix coming — here it is. New chassis, thirty centimeters, low and round, dome on top, near enough a small Roomba, and I dropped the whole prokaryote unit into the middle of it for the brains. Then the wheels, and this is the part I'm proud of: I didn't buy any. I used the four leftover protocells — 1, 2, 4, and 5, the ones that didn't make the cut — one at each corner. Pulled 4 out from under the toaster, towel and all. Each one still kicks exactly the way it always did; I just aimed its kickers at a ratchet on a wheel axle instead of at the floor, so now every kick clicks the wheel forward a notch instead of hopping the whole unit. Two kickers per old protocell, two pawls per wheel, four wheels — and here's the part I like: nothing's shared, no driveshaft, no differential. Each wheel's its own little engine. So the brains drive it the same way they drove the kicks last quarter, just spread over four wheels now instead of two: fire them all forward and it goes straight, lean on the left side harder than the right and it comes around. It rolls now. Smooth-ish — it's still a stack of clicks under there, but four wheels' worth blur into something that passes for driving, and it beats the hopping by a mile.

The kid had names for all five of them. There's one machine now, and four of her bugs are the wheels. She'll work that out on her own time. Not my department.

It earns the Roomba name, too — I put a real vacuum on the underside and a bin inside that holds about a day of floor dust. And here's where Burns made my weekend hard. Any sane machine, you'd charge on a pad: set it down, done. Burns won't have it. So instead the thing carries its dust to a dock — a little box that plugs into the wall — dumps the dust through a port on its belly, and the dock feeds energy back through the same port, heat or UV, for the transducers to drink. It trades trash for warmth through a dirty little hole instead of charging clean off a pad. It's worse engineering every way you can measure, and Burns says that's exactly the point — life doesn't run on induction. Fine. It's his contest. I built him his dirty hole.

There's a board up top now, four slots, and it's Lisa's — her algorithm, her department. Three knobs live on it: the crank (knob one, still there, mostly for show), heat-or-light (knob two), and a new one, knob three, which she calls explore-or-exploit. Near as I can tell it sets whether the thing wanders and tries new routes or sticks to the ones it's already worn in, because the board keeps track of where it's been — a path gets a groove the more it's driven, and fades when it isn't. Lisa makes it sound like the whole ballgame. Looks like a worn path to me. Three slots filled, one open, nine knobs still to squeeze in after that. I'm going to need a bigger board by spring.

Relays everywhere now, long runs of them, because the body's big and spread out and a signal's got to walk all the way from the sensors up front to the wheels out back. The clack's a proper cascade these days — you can hear it think across the room. Still like that you can hear it.

Calls. It vacuums, it docks, it drives. The wheels mean it finally covers ground instead of hopping in place, so I'll bet it cleans the kitchen end to end and parks at the dock when it runs low — dump, drink, off again, clean as a transaction. And that explore-or-exploit knob: Lisa can keep her abstraction, but I'll wager nobody in that house can tell the two settings apart by looking. It's a coin flip with a fancy name.

It still doesn't have a brain — Burns is clear about that, and for once I agree with him. It's a cart that remembers which way it usually goes. But it rolls, it cleans, it feeds itself. A year ago it was five things twitching on a warm floor; now it's one thing that drives. I'll call that a good weekend.

Tear this up in three months if I'm wrong about the explore-or-exploit knob. I'm not.

— Bartholachew (gesundheit)

---

## Chapter 4 — Knob four, the wires go in
*Bart, hardware. Filed December 1, 2031, for the team.*

Lisa's running the upgraded one back to the house this morning. Scorecard first, and this quarter I don't get to take the board.

Last quarter's calls. I said it vacuums, it docks, it drives, and it does all three — take those. Then I bet it would park at the dock when it ran low: dump, drink, off again, clean as a transaction. It did not. It docked when it happened to bump the dock with a full bin, and the rest of the time it ran flat out until it ran flat, and sat there dead in the middle of the floor until somebody picked it up. All fall. Jasmine's been carrying it back to its dock like a stunned bird since September. I called a transaction; I built a thing that dies on the tile by lunch. That's the miss, and it's a real one.

And I staked the dare on the explore-or-exploit knob — said nobody in that house could tell the two settings apart, dared you to tear the page up if I was wrong. I'm not going to claim it. You can't watch how a thing likes to wander when it's face-down on the kitchen floor four days out of five. The question never got a fair morning. Ask Marge whether anybody felt the difference; the house is her animal. I'll only say the test was rigged by the dying, and the dying was on me, so the dare's a wash.

Now the fun part, because the dying is also the thing I fixed.

Here's why it died: nothing was watching the tank. It had a store and it spent the store and it had no idea, ever, how much was left — so it'd commit to a crossing it couldn't finish and quit halfway, no warning, every time. So I gave it a gauge. A real one, watches the charge the way you'd watch a fuel needle, and Lisa wrote the part that reads the needle and does the arithmetic — how far to the dock, what that costs, what's left in the tank — and peels the unit off whatever it's doing while it's still got the legs to get home. It feeds before empty now instead of finding empty the hard way. Three months of Jasmine bending down to a dead robot, gone. She won't notice it's gone, which is how you know it worked.

And here's the part I'm proud of. It's got wires. First wires in any of these — a little net of nerve-thread strung through the body off a bumper ring round the skirt, so a touch goes straight to the whole of it at once. Brush the ring and it answers before you've finished brushing it: brushes stop, suction drops, the whole chassis shies back a thumb's width, all of it, faster than anything it's ever done. No thinking in it. The thinking still runs upstairs on the chip; this is under that — a reflex, quick and dumb and total.

Which means I pulled the relays. All of them. Two quarters I told you I liked that you could hear it think, the clack, the cascade across the room — and the body's gone quiet now, because the wires are too fast to make a sound, and I'll be honest, I miss it. The bench is quiet. I kept one relay in a drawer. Don't tell Lisa.

It eats bigger, too — wider mouth, more pull, and a little compactor behind the intake that crushes what it swallows before it stores it, so it takes a penny now instead of shoving it around the floor for a week. The compactor thumps when it fires. You feel it through the slate. That's about the only noise left in the thing.

Knob four went in — Lisa's knob, her board, her label: comfy or active, it says on the dial. Warm-or-busy, I'd have written, but nobody asked me. Set it warm and it goes and finds the hottest spot it can — the east window, the tile by the vent — and once it's there it decides on its own it's tired, goes still, and sips the warm off the floor in its sleep. Same heat-gap trick as the very first units, the gradient, except now it picks the spot and picks the nap. Set it busy and it parks itself where the floor's buzzing with footsteps and won't sleep at all — and that's the new thing worth watching, because in busy it still has to feed, and it can't sleep to do it, so it has to tear itself off the spot it wants, go dock, and come back. First time the unit's ever wanted two things it can't both have and had to choose between them. I just built the wanting. What it does caught in the middle is going to be the show.

That's slot four, by the way. The last one. The board I've been bellyaching about since June is full — four knobs down, eight to go, and nowhere on God's earth to put them. I said I'd need a bigger board by spring; spring's the deadline now, not the worry. Something gives next quarter or I'm soldering knobs to the kid's lunchbox.

It's got nerves now. It still hasn't got a self. Don't let the wires fool you — fast isn't the same as home, and a reflex isn't a mind. I'll have more to say about that at the table.

Calls. The gauge holds: it stops dying, and Jasmine never carries it off the floor again. And the busy setting is where it gets interesting — I'll bet the first time the gauge and the spot-wanting pull hard against each other, the thing hangs a second before it picks. A real second, long enough to see from a chair. Watch for it.

Tear this up in three months if it dies on the floor even once. It won't.

— Bartholazoa

---