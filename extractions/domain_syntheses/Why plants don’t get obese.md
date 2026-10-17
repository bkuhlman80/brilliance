# Metabolic Budgeting Before Brains

---

## **The question the theory has to answer**

The staircase begins with a claim that sounds simple but is actually contested: **brains exist to manage metabolic budgets, and the more sophisticated the regulation, the more expensive it is to run.**

If that claim is right, it has to be true before brains exist. The multicellular organism that evolved the first nerve net must have been solving a metabolic budgeting problem that predates the nerve net. The bilaterian that evolved the first centralized brain must have been doing something that plants and fungi and protists were already doing, just in a better way. If metabolic budgeting only begins with nervous systems, then the staircase’s central claim is wrong — brains would be doing something qualitatively new rather than doing something old with better hardware.

The literature doesn’t resolve this cleanly. Sterling and Schulkin insist that allostasis — the predictive regulation they propose as the core principle of biological regulation — requires a brain. Their 2019 *Trends in Neurosciences* review is explicit: allostasis is brain-centered, it needs a hypothalamus-centered clock, it requires dopaminergic reward prediction, and it depends on hierarchical neural integration. By their definition, plants and fungi can’t do it. A jellyfish nerve net barely qualifies. A bilaterian brain is where it starts.

Friston sits at the opposite pole. The Free Energy Principle applies to any self-organizing system with a Markov blanket — which is to say, essentially every living thing, and arguably some non-living things too. Under this framework, a bacterium minimizing variational free energy is doing the same computational work as a human prefrontal cortex minimizing variational free energy, just with different substrate and different scope. Prediction all the way down. Active inference from the first cell.

Neither position is satisfying. Sterling’s brain requirement looks like gatekeeping — the mechanism is real but the definitional fence is arbitrary, and as the empirical evidence below shows, plants and slime molds do something functionally identical to allostasis using non-neural machinery. Friston’s universalism is so general that it describes everything and therefore distinguishes nothing. A rock rolling downhill can be *described* as minimizing free energy. The framework tells you which systems can be modeled that way, not which systems are actually doing computational work that matters.

The resolution requires being more precise about what metabolic budgeting actually demands at each level of sophistication.

---

## **Three criteria for allostatic regulation**

The deep research on non-neural organisms used three criteria to separate genuine allostasis from its weaker cousins:

1. **Predictive** — the organism adjusts its metabolic state *before* the need arises, based on cues that are not the need itself.  
2. **Flexible** — the prediction updates based on the organism’s own history and experience, not solely on genetically hardwired circadian or seasonal programs.  
3. **Set-point-adjusting** — the defended metabolic value itself changes as a result of the organism’s history, not just the strength of the defense.

This framework operationalizes the question that Sterling and Friston are arguing past each other about. Circadian anticipation is predictive but not flexible — a plant upregulating photosynthetic compounds before dawn is running an evolved program, not updating its own predictions from yesterday’s weather. Stress priming in plants is flexible but often not set-point-adjusting — the primed plant responds faster when drought recurs but doesn’t run a different metabolic baseline between events. Each of the three criteria dissociates from the others, and only when all three converge does the regulation qualify as functionally allostatic.

Sterling’s implicit bet is that all three criteria cluster together with brains. Friston’s implicit bet is that the criteria all exist wherever there’s a Markov blanket. The empirical evidence lands between them.

---

## **What the deep research found**

Eleven primary papers, six phenomenon categories. The result is a clear picture: **functional allostasis exists in brainless organisms, but it is rare, narrow, and shorter-lived than in animals with nervous systems.** The two cleanest cases are worth examining in detail.

### **Physarum periodic anticipation (Saigusa et al. 2008\)**

A slime mold plasmodium is exposed to three adverse-condition pulses (cold, dry air) at a constant interval. After training, when the plasmodium is placed in continuously favorable conditions, it spontaneously slows its locomotion at the time the *next* pulse would have occurred. The organism has learned a period from three training episodes, and it now runs a different baseline locomotor state at the predicted stress time than at other times. It can learn multiple periodicities simultaneously. The memory decays if unused but can be recalled by a single reminder pulse.

This meets all three criteria. Predictive: the organism adjusts its state before the predicted event, in an environment where no current cue signals the change. Flexible: the prediction is learned from only three training exposures, not hardwired by evolution. Set-point-adjusting: the baseline locomotion speed — which determines foraging rate and therefore metabolic expenditure — is temporarily reduced at predicted stress times. And critically, there is a false-alarm cost: when the predicted stressor fails to appear, the organism has wasted foraging time for nothing. That cost is the signature of genuine predictive regulation. A system that can be wrong is a system that is actually computing predictions rather than just responding to current input.

The mechanism is coupled biochemical oscillators — calcium waves, actomyosin contraction cycles, cAMP/NADH — that become entrained to external periodic stimuli and then continue oscillating with period memory encoded in their phase relationships. No neurons. No nervous system. The regulation is implemented in the chemistry of a single giant cell.

### **Arabidopsis guard cell memory (Virlouvet and Fromm 2015\)**

A plant previously exposed to drought, then returned to well-watered conditions, does not return to baseline stomatal behavior. Its guard cells maintain partially closed stomata during the watered recovery period. Not because water is currently limited, but because the plant is running a more conservative water economy at baseline in anticipation of the next drought. The mechanism is sustained upregulation of ABA biosynthesis genes (NCED3, AAO3) specifically in guard cells, maintaining elevated ABA levels that keep stomata partly closed without any current dehydration signal.

This is not faster response when drought recurs. It is a different operating point between events. The plant has adjusted its defended value for stomatal conductance — trading photosynthetic capacity (partially closed stomata reduce CO₂ uptake) for water security. That trade-off is real and expensive. The plant grows more slowly. If drought does not recur, the plant has paid a cost for nothing.

All three criteria are met. The prediction is based on recent experience, the set point has moved, and the cost is measurable. The mechanism is transcriptional, not neural. A plant with no nervous system, no brain, no neurons of any kind is running what looks functionally identical to allostatic regulation — within a narrow physiological domain (water balance), on a short timescale (hours to days), using chromatin and gene expression as its implementation substrate.

### **The rest of the evidence**

Beyond these two cases, the landscape is more mixed. Vernalization in Arabidopsis — the epigenetic memory of winter cold that permits spring flowering — meets all three criteria formally but functions as a one-way developmental ratchet rather than ongoing regulation. Once the Polycomb machinery silences the FLC flowering repressor, the silencing doesn’t reverse in normal development. The cold duration is quantitatively integrated (more cold produces more stable silencing), so the calibration is genuine, but it’s a one-shot switch rather than an adjustable set point.

Plant stress priming broadly — the family of phenomena where prior stress exposure enhances later stress tolerance — is mostly *enhanced reactive capacity*, not predictive set-point adjustment. The plant pre-loads transcriptional machinery (stalled RNA polymerase, retained H3K4me3 histone marks) at stress-response loci, enabling faster activation when the next stress arrives. But between stresses, the plant runs the same baseline metabolism it always did. This is homeostasis with a trigger-ready defense system, not allostasis with a shifted operating point.

Bacteria show predictive behavior but without flexibility. E. coli upregulates anaerobic respiration genes when temperature rises, because in the gut, temperature increase reliably precedes oxygen depletion. This is anticipation, but it’s genetically hardwired anticipation — the temperature-oxygen correlation is encoded in the regulatory network by natural selection, not learned by the individual cell. You can evolve new anticipatory couplings in E. coli through \~850 generations of experimental selection, as Mahilkar et al. showed in 2022, but no individual bacterium learns anything. The “conditioning” is phylogenetic, not ontogenetic.

Mycorrhizal fungal networks, root-shoot allocation in plants, fungal resource trading — all of these show sophisticated homeostatic regulation with anticipatory features, but none shows experience-dependent set-point adjustment. The networks redistribute resources in response to current gradients. They don’t remember last week’s distribution and use it to predict next week’s. The regulation is real and impressive, but it’s reactive optimization, not allostatic prediction.

---

## **What this means for Sterling and Friston**

Sterling is wrong that allostasis requires a brain. Physarum and Arabidopsis guard cells prove the claim empirically — functional allostasis can be implemented in oscillatory biochemistry or in transcriptional machinery, without any nervous system at all. The three criteria that Sterling considers jointly definitive of allostasis can be met by non-neural substrate.

But Sterling is right that brains make allostasis dramatically more powerful. Physarum’s anticipation works for minutes. Arabidopsis guard cell memory works for hours to days. Neither can track more than one or two predicted variables at a time, neither can manage complex trade-offs across domains, and neither can carry memories across weeks, let alone years. Brains add scale, speed, flexibility, cross-domain integration, and temporal range. The *principle* of allostatic regulation is substrate-independent. The *implementation* of it in brains is orders of magnitude more powerful than anything available to plants or fungi or slime molds.

Friston’s active inference framework is too permissive to distinguish these levels. Under the Free Energy Principle, a bacterium anticipating anaerobic conditions and a human planning a career change are both minimizing variational free energy — the math is the same. But the empirical evidence shows that what the bacterium is doing (genetically hardwired predictive reflex) and what the human is doing (learned, flexible, set-point-adjusting regulation) are qualitatively different at the level that matters for actual organismal behavior. The Free Energy Principle tells you the deep formal commonality. It doesn’t tell you that the bacterium cannot do within its lifetime what the human does, or why that distinction is important.

Friston himself has endorsed a version of this distinction. He explicitly separates the Free Energy Principle — which he describes as a variational principle rather than a falsifiable claim — from predictive coding, which he treats as a process theory that makes testable predictions about neural implementation. The Free Energy Principle is in the same category as “computation” or “Darwinian selection”: a mathematical framework that describes how self-organizing systems can be modeled, not a mechanism that can be falsified by experiment. Predictive coding is a candidate implementation of that framework in neural tissue, and predictive coding claims *can* be tested against data. This is Friston’s own answer to the “unification by fiat” critique raised by Litwin and Miłkowski (2020), who argue that precision-weighting does enormous theoretical work in active inference without ever being clearly operationalized at the psychological or neural level. Friston’s response is essentially: the framework isn’t supposed to be operationalized; the process theories built on top of it are. The framework is a language for describing any self-organizing system. The process theories are empirical claims about specific organisms. That distinction is exactly the one this theory needs. Active inference is the language. Allostasis is a specific claim within that language — that some organisms implement predictive regulation in a learned, flexible, set-point-adjusting way, and that the implementation has to be paid for out of the organism’s metabolic budget.

The useful move is to treat metabolic budgeting as the universal principle, active inference as the mathematical framework that describes it at every level, and allostasis as the specific implementation of metabolic budgeting that incorporates learned, flexible, set-point-adjusting prediction. Physarum’s coupled oscillators implement allostasis weakly. Plant guard cells implement it within a narrow physiological domain. Nerve nets in jellyfish and other basal metazoans probably implement it across a somewhat broader range. Brains in bilaterians implement it at scale. Human brains running language-enabled cultural transmission implement it at civilizational scale.

Each level is Hoffmann’s ratchet applied at a new scale. The molecular storm at the cellular level gets ratcheted into ordered metabolic work by protein machines that exploit thermodynamic asymmetry. Multicellular coordination gets ratcheted into directional budget allocation by hormonal and electrical signaling systems. Nervous systems ratchet sensorimotor chaos into coordinated action. Brains ratchet environmental uncertainty into predictive regulation. Simulation ratchets present-moment data into modeled futures. Language ratchets individual experience into cultural memory. Each ratchet is asymmetric — easier to click forward than backward — and each ratchet costs energy to run.

---

## **Why plants can’t get obese**

The obesity question is the cleanest way to see the difference between implementation substrates. Plants can overaccumulate starch. They can overaccumulate lipids. They can shift the starch-lipid allocation ratio under stress. They can even maintain elevated storage compounds across recovery periods. But they cannot get *obese* in the pathological sense — they cannot chronically defend an inappropriate elevated storage level in a way that compounds across time and becomes self-reinforcing.

Human obesity is allostatic overload. The brain chronically anticipates a need for higher energy reserves, recalibrates appetite upward, recalibrates insulin sensitivity downward, recalibrates metabolic rate to conserve the new higher stores, and then defends the new configuration as if it were the correct baseline. When the person tries to lose weight, the brain interprets the loss as a threat to its updated prediction and fights back. This is not a failure of homeostasis. It is homeostasis working exactly as designed — defending the current operating point — applied to an operating point that allostatic regulation moved to the wrong place.

Plants don’t have this failure mode because their regulation isn’t flexible enough to move the set point chronically in the first place. When a plant overaccumulates starch, the diurnal cycle grinds the excess down at night. When it overaccumulates lipids, β-oxidation clears them. The regulation is reactive homeostasis supplemented with genetically hardwired circadian anticipation. There is no mechanism for “the plant decides that the new higher storage level is correct and defends it.”

The absence of plant obesity is not a limitation of plants. It is a limitation of homeostatic regulation. Obesity is what flexible predictive regulation looks like when it mispredicts chronically. **You need a nervous system — or at minimum a learning-capable allostatic mechanism — to get fat in a pathological way.** The organisms that can genuinely adjust their defended metabolic values based on experience are also the organisms that can defend the wrong values for decades.

This is not a rhetorical point. It is the strongest argument for why metabolic budgeting belongs at the beginning of the staircase rather than somewhere later. The entire arc of the book — from bilaterian gamification of life tasks, through endotherm simulation, through ape social strategy, through human symbolic transmission — is the progressive sophistication of allostatic regulation. At each step the organism gains more flexibility, more predictive range, more capacity to update its own defended values. At each step it also gains more capacity to defend the wrong values for longer.

Plants can’t get obese because plants can’t carry their predictions across enough context. Humans can get obese because humans can carry predictions across decades of symbolic environment. The same capacity that makes personality possible makes personality pathology possible. This is what metabolic budgeting means when you run it on a more powerful substrate.

---

## **The Set Point × Free Lunch mirror pair**

The multicellularity theory needs to establish all of this in a way that the reader carries forward into every subsequent theory. The way to do it is through the Set Point × Free Lunch mirror pair — two fallacies that fight each other and that together define the healthy middle where real metabolic budgeting lives.

**Set Point fallacy:** The organism defends a fixed value. Change is impossible or only temporary. The thermostat metaphor rules. Stability is the default; deviation is the exception. This is classical homeostatic thinking, and it fails for any organism capable of allostatic regulation — which, the evidence now shows, includes even non-neural organisms in narrow domains.

**Free Lunch fallacy:** Regulation is free. The organism can predict, adjust, and recalibrate without paying any metabolic cost. Cognitive and regulatory work don’t draw on the same energy budget as physical work. Sustained self-regulation is a matter of willpower, not of metabolic expenditure. This is the Ghost’s supply chain, and it fails for any organism whose allostatic machinery is actually running — which is to say, any organism that does prediction at all.

The two fallacies are mirror images. Set Point says the organism is rigid; Free Lunch says the organism is fluid. Set Point says change is impossible; Free Lunch says change is costless. Neither is right. The truth — the allostatic truth — is that **change is possible but expensive.**

Every predictive adjustment draws on the metabolic budget. Every maintained deviation from baseline costs energy to sustain. The organism runs on a finite budget, and the budget is what forces the trade-offs that shape every decision the organism makes. When the trade-offs work, you get a healthy allostatic system that predicts well and pays reasonable costs. When the trade-offs break down, you get allostatic overload — chronic mispredictions compounding into pathologies that defend the wrong values for decades.

This is the foundation the staircase needs. Once the reader has understood it, every subsequent level of the staircase is a refinement of the same lesson. Bilaterians gamify life tasks by paying predictive costs that reactive homeostasis wouldn’t. Vertebrates use reinforcement learning to update their predictions at further cost. Endotherms invest in simulation, which is radically more expensive than reactive control. Apes pay coordination costs to run recursive social models. Humans pay the extraordinary cost of running symbolic transmission across generations. Each level is a better implementation of the same fundamental problem: predict, adjust, pay.

And each level inherits the same failure mode. The predictive system that produces Conscientiousness at its best also produces rigidity and compulsion at its worst. The social modeling that produces Agreeableness at its best also produces exploitability and boundary failure at its worst. The symbolic transmission that produces shared culture at its best also produces generational pathology at its worst. In every case, the pathology is allostatic overload — the system defending the wrong values because its predictions went chronically wrong, or because the environment shifted and the system hasn’t paid the reset cost.

---

## **Why this theory is load-bearing for the whole book**

If the reader doesn’t come out of the multicellularity theory with Set Point × Free Lunch corrected, the rest of the book will not work.

Without the correction, the reader will enter the bilaterian theory thinking the nervous system is *commanding* the body rather than *coordinating its metabolic budget*. That reading will install a homunculus at every subsequent level. The reader will treat gamification of life tasks as the fish’s agency, rather than as a sophisticated implementation of metabolic budgeting. The reader will treat endotherm simulation as planning done by a controller, rather than as an expensive investment in predictive capacity. The reader will treat ape mentalizing as a separate cognitive module rather than as the same architecture applied at higher recursive depth. The reader will treat human symbolic transmission as culture-on-top-of-biology rather than as metabolic budgeting running on a radically new substrate.

The multicellularity theory isn’t a preliminary section the reader can skim. It’s the spine. Everything the staircase is trying to show depends on the reader understanding that brains didn’t start anything new — they made an old thing dramatically better, and the old thing was metabolic budgeting under constraint. The Set Point × Free Lunch mirror pair is how you lock that understanding in place, because it forces the reader to hold both sides of the truth simultaneously. Change is possible. Change is expensive. Neither alone.

Once that’s in place, every trap correction at every subsequent level of the staircase is doing the same work — pulling the reader back from picking one side when the answer is always both. The Determinism Fallacy at the bilaterian level is Set Point thinking applied to genetic inheritance. The Homuncular Fallacy at the human level is Free Lunch thinking applied to symbolic agency. The Authenticity Fallacy at the ape level is Free Lunch thinking applied to personal identity. In every case, the reader is tempted to grant the organism either too much rigidity or too much freedom, and the correction is always the same: the organism is doing allostatic regulation, which is flexible but costly, and every instance of the fallacy is a failure to hold both truths at once.

The reader who has understood the multicellularity theory correctly will be ready to encounter every subsequent fallacy with the right instinct already loaded. The reader who hasn’t will keep installing homunculi, keep treating trait scores as verdicts, keep treating environments as cages, and keep missing the central point that personality is an energy allocation within a constrained landscape that runs on a budget the organism doesn’t control and can’t inspect.

That’s why this theory is where the book begins. Not because multicellularity is chronologically first. Because metabolic budgeting is the principle everything else in the book is an elaboration of, and the reader needs to meet it before they meet any of its implementations.

---

## **Reading list for this theory**

**Foundational:**

* Peter Hoffmann, *Life’s Ratchet: How Molecular Machines Extract Order from Chaos* (2012). The molecular-storm-to-ordered-work argument that underwrites everything above.  
* Peter Sterling and Joseph Eyer, “Allostasis: A New Paradigm to Explain Arousal Pathology” (1988). The original allostasis paper.  
* Peter Sterling, “Allostasis: A Model of Predictive Regulation” (2012, *Physiology and Behavior*). The update.  
* Peter Sterling and Joseph Schulkin, “Allostasis: A Brain-Centered, Predictive Mode of Physiological Regulation” (2019, *Trends in Neurosciences*). The brain-centric version that this theory needs to push back against.

**Friston and active inference:**

* Karl Friston, “The Free-Energy Principle: A Unified Brain Theory?” (2010, *Nature Reviews Neuroscience*). The framework.  
* Paco Calvo and Karl Friston, “Predicting Green: Really Radical (Plant) Predictive Processing” (2017, *Journal of the Royal Society Interface*). The Bayesian plant hypothesis.  
* Karl Friston, “A free energy principle for a particular physics” (2019). Friston’s own statement that the FEP is a variational principle rather than a process theory, and that predictive coding is the testable implementation layer.  
* Litwin and Miłkowski, “Unification by fiat: Arrested development of predictive processing” (2020, *Cognitive Science*). The sharpest philosophical critique of active inference as currently formulated — specifically on the problem that “precision” does enormous theoretical work without clear operationalization. Useful as the independent philosophical version of the empirical point this theory makes.

**Allostasis in non-neural organisms:**

* T. Saigusa, A. Tero, T. Nakagaki, Y. Kuramoto, “Amoebae Anticipate Periodic Events” (2008, *Physical Review Letters*). The Physarum paper.  
* L. Virlouvet and M. Fromm, “Physiological and transcriptional memory in guard cells during repetitive dehydration stress” (2015, *New Phytologist*). The plant guard cell paper.  
* I. Tagkopoulos, Y.-C. Liu, S. Tavazoie, “Predictive Behavior Within Microbial Genetic Networks” (2008, *Science*). Bacterial anticipation.  
* A. Mitchell et al., “Adaptive prediction of environmental changes by microorganisms” (2009, *Nature*). More bacterial anticipation.  
* M. Bäurle and colleagues, “Priming and memory of stress responses in organisms lacking a nervous system” (2016, *Biological Reviews*). The most comprehensive review.

**Barrett and interoceptive budgeting:**

* Lisa Feldman Barrett, *How Emotions Are Made* (2017). The constructed-emotion argument and the body-budget framing.  
* Lisa Feldman Barrett, *Seven and a Half Lessons About the Brain* (2020). The shorter version of the body budget argument.

**Background on homeostasis vs. allostasis:**

* Jay Schulkin, *Rethinking Homeostasis: Allostatic Regulation in Physiology and Pathophysiology* (2003).  
* Bruce McEwen and colleagues on allostatic load — various papers from the 1990s and 2000s.

