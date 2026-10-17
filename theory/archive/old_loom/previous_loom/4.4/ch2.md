Ch 1

## The Bramblogues

Bart took the bot's slot, and he opened it the way he'd open it for the next three years, though nobody knew that yet, least of all him.

"I want to introduce somebody. Not here — in my head. Buddy of mine from school, Owen, except nobody's called him Owen since sophomore year. Big O. Like the notation — the thing you measure an algorithm's waste with — because the man could never look at a piece of code without telling you how much faster it'd run if you'd thought one more minute. He's a performance engineer at Google now, which is the most Big O thing that could happen to a person. He optimizes things that are already fast."

He picked Bramble up off the table.

"And every quarter, when I sit down to tell you what I built, I hear Big O over my shoulder asking what in God's name I was thinking. So I'll let him go first. He looks at this and says, walk me through it. I say sure — it runs on the six-degree difference between the warm floor and the cool air, skims a few thousandths of a watt out of the gap. He says where's the battery. No battery. Where's the chip. No chip. No sensors, no memory, doesn't know where it is or what it just did. He says, so what does it *do*. I say: it twitches. Few times a minute. Runs down in a week and quits till a four-year-old winds it back up. And he looks at me and says, Bart, I could build you something that does more than that out of a doorbell."

He set the bot down, gentle.

"And he's right. He could. And the answer to Big O — this quarter and every quarter — is that's not the point. Because *that* is what the first living thing was. A bag of barely. Ran on a gap it didn't make, could hardly move, forgot it existed the second the energy stopped — and barely keeping going was the entire miracle. We didn't build it efficient. We built it the way the thing actually was." He looked around the table. "I've got a name for the dumb stuff — every feature that's in there because the biology's in there and for no reason a sane engineer would sign off on. Bramble analogs. Bramblogues. That's what this slot is, every quarter: here's what we put in the thing to make it more animal and less machine, and here's Big O not believing his eyes."

Lisa pulled the bot from where Mira had set it and held it up.

"What it can do. It can persist. Hold together. Twitch when conditions are right, hold still when they're wrong. What it can't do — and there's more in the negative — it can't remember, can't model, can't model itself, can't decide, can't regulate. No battery, no sensors, no central anything, no map of where it is or what it just did. What it has is the wiring, the spring, and the gradient." She turned it over. "And the four heat-and-actuator pairs are wired straight together, no shared state, nothing coordinating them. Four little twitching modules in one shell. It isn't one thing yet."

Bart, quiet till now: "So what are we watching, when we watch it? If it's got no actions —"

Lisa thought. "Its gravity, almost. Not actions — it hasn't chosen anything. Dispositions. A pull to twitch under some conditions, to go still under others; and over weeks, in some of them, a pull to strain harder on one side, to wear a groove into themselves in a direction. Four wears its underside; five wears even. These aren't behaviors. They're the patterns the system falls into. They fall down the gradient, because things fall down." She paused. "There's a word for them in my field. Wrong word for this room. I'll bring it to the framework."

She set the bot down. "And Bramble does the least of the five. Moves least, lasts longest, keeps going after the others have run out. That's the seeded wiring — not a thing it's choosing."

Jasmine, quiet a while: "It's also why Mira likes it." Everyone looked at her. "You can hold Bramble. It doesn't lurch, doesn't spin, doesn't run out before you've decided what to do with it. It waits. Mira likes things that wait."

Bart stood for the next part; he'd been waiting on it. "The personality knob. Thought about it six months, was wrong about it for five and a half. Here's where I landed." He turned Bramble over, set it down, pointed at the crank. "There's a volume knob on it — Going. That crank's the knob."

He sat, stood back up. "It's what we thought was just the energy source. Wind it up and the volume's up and it runs; leave it a week and the volume drains down toward dead. It's the knob that decides whether the bot has a personality at all. Volume up, it does its dispositions. Volume down, it has none of them. At this clade the personality's a thing the household winds up once a week. Mira's Sunday wind-ups aren't energy management. They're the whole personality. Without Mira, there isn't one. Mira's the knob."

Marge looked up sharply. "Mira is *the knob.*"

"She's such a knob." He nudged Mira's shoulder.

Lisa, writing: "Software side — there's no software. No microcontroller, no code. A mechanical loop: the household's weekly crank is the input, the spring tension's the state, its decay's the plant, the floor-air gap's the energy, the twitch is the output. The household's in the loop. The household's what gives it a personality. Cheryl asked what a personality is; at protocell, the answer is a thing that needs a household to run it."

Bart was still up. "One more, and it's not for tonight — I just want it on tape so Cheryl can chew on it. One knob, the crank, knob one of twelve. Two at Prokaryote, then one a quarter for thirty-three months, and by the end there's twelve knobs on a body the size of a computer mouse. Where do twelve knobs *go.* It'll look like a control panel. It'll look like a cactus. Somewhere in here we run out of room. That's the twelve-knob problem. Not solving it tonight — but I think we do something architectural about it, and I don't know what yet."

Burns laughed the chest-laugh, longer than usual — because it was the kind of problem that resolves itself by being a problem, and he trusted that; because *it'll look like a cactus* was a funny thing to say; because the meeting was going well.

Ch 2

## The Effort Knob

Bart opened the bot block by handing the floor to a man who wasn't in the room. "Big O called Sunday. I told him we'd taught it to find a sunbeam, and he perked up — finding a target's a real problem, and he likes real problems. He said: four sensors, fine, when one side reads brighter you drive that way, good. But what's it do when the light's flat, when no side is clearly brighter? I said, it spins. Picks a random new heading and re-checks. He said — *random?* You don't sweep, you don't spiral, you don't even remember where you already looked? I said no. He said, quoting: *you built a robot that, the second it gets confused, gets lost on purpose.*"

He set Bramble down by Lisa's hand.

"And that's the build. Clear gradient, it runs straight at the light, smart enough. No gradient, it doesn't search — it tumbles. Random reorient, re-sample, go again, with no map of where it's been and no memory it was ever anywhere. Run, and tumble. It's how a bacterium does it, because a bacterium's got nothing to search *with* — no memory to mark where it looked, no math to plan a sweep. It can tell better-than-a-second-ago from worse, and when it's worse it rolls the dice. Half the living things on the planet navigate by rolling the dice. We wired the dice in on purpose. That's the Bramblogue this quarter — the confusion that never gets solved, only re-rolled."

He looked at Lisa. "Tell them how it actually runs, before Big O files the bug."
