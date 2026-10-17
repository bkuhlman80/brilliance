Ch 1

## Build log — Five units, out the door
*Bart, hardware. Filed February 12, 2031, for the team.*

Lisa's running these over to the Burns place this morning, so here's everything in the box before anybody makes me explain it twice.

First, the part I'm proud of. There's no battery in these and no plug, and they don't run on heat — they run on the *difference* in heat. Each unit's got two little heat-transducers, and a transducer doesn't care how warm the room is; all it cares about is that the floor is warmer than the air sitting on top of it. Jasmine's radiant floor holds around 27 degrees C and the room air sits around 21, so there's a six-degree gap just hanging there doing nothing, and the transducer reaches into that gap and skims a trickle of work out of it. That's the Seebeck effect, and it's a genuinely beautiful piece of physics — I'll explain it to anyone who stands still long enough. Park one on the warm floor and an hour later the slate underneath it is cold. That cold is the work coming out. The unit's eating the gap.

Now, here's the thing about that trickle: it's nothing. A few thousandths of a watt. You can't run a motor on it — can't make anything turn, can't even hold a light on. So I don't try. Each transducer drips its trickle into a tiny store (a low capacity supercapacitor), and when the store's full enough it dumps the whole lot into its actuator at once — one hard flinch. The actuator's just a little kicker: it knocks a stubby angled foot against the floor and the unit hops a hair in one direction, then sits there the better part of a minute filling back up before it can flinch again. That's the twitch, and that's the whole way it moves — no wheels, no motor, just a stack of tiny kicks against the slate, like a buzzing phone walking itself across a table, except I get to aim it. Two kickers to a unit, each with its own store, never quite firing together — that stagger is the personality.

No chip, no sensors, no memory — nothing telling the two kickers what to do. They fire on their own clocks, and I seeded each one different on purpose so they're not clones:

- **1** — cranked hot on the left pair, so it lists that way and burns through its tension fast. A busy little thing; always looks late for something.
- **2** — slow and low, with long pauses between kicks. Sits, then goes, then sits. More patience than you'd want in a roommate.
- **3** — the quiet one: even pairs, low draw, the fewest kicks of the lot, so it does the least and outlasts everybody — still ticking Wednesday when the rest have gone slack. The one only an engineer loves.
- **4** — lopsided, on purpose. The pairs don't match, so instead of going anywhere it grinds in place and wears a groove into itself over the weeks. If the commission let me ship four, this is the cut. It's in the box to make five.
- **5** — the show unit. Even like 3, but I let it kick hard, so it runs a clean little circuit and burns through its tension fastest of the lot. Wears even, though. Pretty to watch.

Ch 2

## Build log — Knob two, one unit up
*Bart, hardware. Filed June 2, 2031, for the team.*

Lisa's running the upgraded one back to the house this morning.

We upgraded one unit — 3, the one the house calls Bramble — and left the other four stock.

At protocell this thing only ever twitched: two kickers firing on their own clocks, and it'd hop around the floor like a bug with somewhere to be and no idea where. Now it *hunts*. Same two kickers — I didn't give it new muscles — but I put a chip in the middle that decides *when* each one fires. That's the whole upgrade. Fire them so the hops add up in one direction and it crawls that way; fire them so the hops add up to a spin and it turns in place; don't fire and it sits. Two idiots kicking on their own schedule became two idiots kicking on a downbeat. Still no wheels. Still hopping across the slate a hair at a time. It just hops with *intent* now.

What tells it which way to go: four little light sensors around the floor seam, each aimed a few degrees up and pointed a different direction. They all read brightness at once, and if they agree there's more light over *there* than anywhere else, the chip knows which way "there" is. That's the trick — finding a sunbeam with four parts that each only know one number.

The chip's an STM32, my pick, and it's the right pick. It runs a dumb little table Lisa and I wrote that fits on an index card: three states. Clear direction, kick toward it — that's RUN. No clear direction, spin a random amount and read again — that's TUMBLE. Stores filling faster than it's spending, sit still and let them fill — that's STOP. The screen up top shows which one it's in. And I ran the whole signal path on relays — coil-and-armature, the kind that clack — so you can hear it think: a little clack-clack-clack every time it changes its mind. I like that you can hear it.

New since February, all told: two stores instead of one — a big slow new battery and the same little fast one beside it. Now the supercap dumps its whole charge at once and then fills back up off the battery; two solar panels down the long sides; the floor-transducers carried over from the protocell, still skimming warmth off the slate; a converter that takes whatever's coming in — sun, warmth, both at once, it doesn't care which — and tops the stores; the chip; the relays; four sensors; and a second knob next to the crank — the Effort knob, Lisa's word for it.

The Effort knob's the same shape as the crank — same as all of them will be. The crank you wind and it drains back down across the week; this one you set and it stays where you put it. All it does is pick which store Bramble spends from. Effort volume down draws the big slow battery and he runs even — a patter of hops he'll keep up all day, never quick, never quits. Effort volume up draws the little fast one and he runs in bursts — sits, fires off a flurry of hops quick as you like, then stops dead to refill off the slow store before he can go again. Aerobic or anaerobic is the mechanism under it, the way Lisa describes it; same bot, two ways to spend. The fast spend burns through a charge quicker — you don't get as far per drop in bursts — so leave the volume up and you'll be chasing a sunbeam sooner. Which way the house leaves it set is the house's business. I built both.

Won't work on anything soft — a rug would eat the hops — but the kitchen's slate, so: every sunny morning, watch it do zoomies.

It won't need cranking on Sundays anymore — the panels and the floor feed the stores, the stores run Bramble, he goes all day on his own. The crank's just an emergency starter now: it spins a little dynamo I added, so a few turns put enough back into a dead bot to wake him up when there's no sun to be had.

Ch 3

## Build log — Five into one
*Bart, hardware. Filed September 1, 2031, for the team.*

This one I did myself — took the lot to the bench Friday and had the weekend on it, so I'm running it back this morning.

Now the fun part, and there's a lot of it this quarter, because this is the first time Bramble's a real machine instead of a bug.

It's got wheels. Finally. Last quarter I told you hopping was a lousy way to travel and I had a fix coming — here it is. New chassis, thirty centimeters, low and round, dome on top, near enough a small Roomba, and I dropped Bramble — last quarter's whole prokaryote unit — into the middle of it for the brains. Then the wheels, and this is the part I'm proud of: I didn't buy any. I used the four leftover protocells — 1, 2, 4, and 5, the ones that didn't make the cut — one at each corner. Pulled 4 out from under the toaster, towel and all. Each one still kicks exactly the way it always did; I just aimed its kickers at a ratchet on a wheel axle instead of at the floor, so now every kick clicks the wheel forward a notch instead of hopping the whole of Bramble. Two kickers per old protocell, two pawls per wheel, four wheels — and here's the part I like: nothing's shared, no driveshaft, no differential. Each wheel's its own little engine. So the brains drive it the same way they drove the kicks last quarter, just spread over four wheels now instead of two: fire them all forward and it goes straight, lean on the left side harder than the right and it comes around. It rolls now. Smooth-ish — it's still a stack of clicks under there, but four wheels' worth blur into something that passes for driving, and it beats the hopping by a mile.

The kid had names for all five of them. There's one machine now, and four of her bugs are the wheels. She'll work that out on her own time. Not my department. I'm calling him PacMan, for the record — a thing that goes around all day eating dots earns the name.

It earns the Roomba name, too — I put a real vacuum on the underside and a bin inside that holds about a day of floor dust. And here's where Burns made my weekend hard. Any sane machine, you'd charge on a pad: set it down, done. Burns won't have it. So instead Bramble carries his dust to a dock — a little box that plugs into the wall — dumps the dust through a port on his belly, and the dock pays the energy back through the same port. And here's the part I like: you can't just hand these transducers warmth — they've never run on warmth, not once, not since the protocell floor; they run on a difference, a warm side and a cool side and the gap between. So the dock makes the gap. There's an air compressor in there feeding a vortex tube — a plain pipe, no moving parts, you push compressed air in the side and hot comes screaming out one end and cold out the other, which still reads like a magic trick — and it lays the hot stream on one face of the transducer and the cold on the other and lets Bramble drink up the difference. And before anybody calls that free: it isn't. The compressor's eating wall current the whole time; the tube only splits what the wall already paid for — and it drones the whole time it's plugged in, so rather than set a pump humming by the dishwasher all day I hung it outside the back door and ran the air line in through a hole in the wall. What sits by the dishwasher is the quiet end of a hose coming in from the cold. 

So Bramble will trade trash for the heat difference through a dirty little hole instead of charging clean off a pad. It's worse engineering every way you can measure, and Burns says that's exactly the point — life doesn't run on induction. Fine. It's his commission. I built him his dirty hole.

Relays everywhere now, long runs of them, because the body's big and spread out and a signal's got to walk all the way from the sensors up front to the wheels out back. The clack's a proper cascade these days — you can hear it think across the room. Still like that you can hear it.

It still doesn't have a brain — Burns is clear about that, and for once I agree with him. It's a cart that remembers the moves it usually makes. But it rolls, it cleans, it feeds itself. A year ago it was five things twitching on a warm floor; now it's one thing that drives. I'll call that a good weekend.
