# Michael Levin's Research Program: A Theory-Neutral Survey of Bioelectricity, Morphogenesis, and Basal Cognition

## TL;DR
- Levin's lab has produced **robust, partly replicated experimental findings** that membrane-voltage (Vmem) states and gap-junctional coupling can act as *instructive* (not merely permissive) signals shaping anatomy — ectopic eyes in *Xenopus* (Pai et al., 2012), induced limb/tail regeneration, and two-headed planaria — but the interpretive overlay that these constitute "memory," "goals," "intelligence," or "cognition" is a separable conceptual layer that critics dispute and that is *not entailed by the data*.
- The strongest empirical core is at the **tissue and whole-organism (multicellular) scale**; genuinely *single-celled eukaryote* bioelectric evidence within Levin's own program is comparatively thin and is often imported by analogy from multicellular systems or from other labs' protist-learning work (which itself has documented replication problems).
- Xenobots and Anthrobots are **real, demonstrated engineered constructs** (motile cell assemblies that move via cilia and, for Xenobots, perform "kinematic self-replication" by pushing loose cells into piles), but the labels "robot," "novel organism," and "self-replication" are contested framings, not neutral descriptions.

## Key Findings

1. **Bioelectricity as an instructive morphogenetic signal is the most established empirical pillar.** Multiple primary papers show that manipulating ion channels/pumps and gap junctions changes large-scale anatomical outcomes in structured, predictable ways — not as generic toxicity.
2. **The "pattern memory" planaria work is striking but concentrated in one lab.** The two-headed planaria that continue regenerating two heads after the perturbing agent is gone is a real, published phenomenon (Oviedo et al., 2010; Durant et al., 2017), but the "stored target morphology / memory" interpretation is interpretive, and independent replication outside the Levin group is limited.
3. **Xenobots/Anthrobots demonstrate cellular plasticity and emergent behavior**, but the demonstrated behaviors (ciliary locomotion, particle aggregation, neuron-bridging in a dish) are more modest than the popular "living robot"/"self-replication" headlines.
4. **TAME, the cognitive light cone, and multiscale competency are explicitly philosophical/theoretical frameworks**, presented by Levin as such; they are heuristics for generating experiments, not themselves empirical results.
5. **Substantive named critics exist** across philosophy of biology (Figdor, Keijzer, Jaeger/Walsh, Pigliucci) and the empirical literature (Loy et al., Mallatt et al.), with a sympathetic-but-cautious middle (Lyon, Ginsburg & Jablonka, Fábregas-Tejeda & Sims).

---

## Thread 1 — Bioelectricity as a pre-neural communication/control layer

### (a) Established empirical findings
**Scale: tissue and whole organism (frog embryo, planaria).**

- **Ectopic eye induction (Pai, Aw, Shomrat, Lemire & Levin, 2012, *Development* 139(2):313–323).** During normal *Xenopus laevis* embryogenesis a bilateral cluster of hyperpolarized cells demarcates the prospective eye field. Depolarizing the dorsal lineages produced malformed eyes; imposing an eye-like Vmem on *non-eye* cells induced, in the verbatim words of the abstract, "well-formed ectopic eyes that are morphologically and histologically similar to endogenous eyes. Remarkably, such ectopic eyes can be induced far outside the anterior neural field. A Ca2+ channel-dependent pathway transduces the Vmem signal… These data reveal a new, instructive role for [Vmem]." Ectopic eyes were induced only under the specific hyperpolarizing condition (15 mM sodium gluconate), and the signal altered eye-field transcription factors (Pax6, Rx1; Otx2 largely unchanged). What the Results actually show: a voltage change is *sufficient* to trigger organ-level patterning. **Scale: tissue/whole organism.**
- **Tail/limb regeneration via ion flux (Adams, Masi & Levin, 2007, *Development*; Tseng, Beane, Lemire, Masi & Levin, 2010, *J Neurosci* 30:13192–13200).** A transient sodium current / H⁺-pump-driven Vmem change was reported as "necessary and sufficient" to induce regeneration in otherwise non-regenerative contexts; a low-information "pump protons" stimulus triggered a self-limiting cascade rebuilding the appendage. **Scale: tissue/whole organism.**
- **Tools that make these claims tractable:** voltage-reporter dyes CC2-DMPE and DiBAC4(3), V-ATPase/H,K-ATPase manipulations, optogenetic ion-flux control in *Xenopus*, and pharmacological/genetic channel manipulation. These are genuine methodological contributions (Adams & Levin, 2012, *Cold Spring Harb Protoc*).
- **Replication/status:** The instructive role of Vmem in *Xenopus* eye/face/left-right patterning and in regeneration has been reproduced within the lab across multiple papers and modeled computationally (Pietak & Levin). The broader bioelectric-signaling field predates Levin (Borgens, Jaffe, Nuccitelli, McCaig), but the *instructive, information-bearing* framing is most strongly associated with Levin's group.

### (b) Levin's theoretical/interpretive framing
- Vmem patterns are described as a "bioelectric pre-pattern" that "carries information" and acts as a "master regulator" — a "build whatever normally goes here" signal. Calling a sufficient upstream physical signal an "information-bearing" or "instructive" *code* is a modeling choice. Levin further frames bioelectricity as the "cognitive glue" scaling cell-level homeostatic loops into anatomical goals (Levin, 2023, *Animal Cognition*). **Mark: interpretive.**

### (c) Open or disputed
- Whether Vmem is genuinely "instructive/information-bearing" vs. one permissive node in a complex signaling network is contested; Johannes Jaeger has argued Levin **exaggerates the significance of bioelectric fields** in development and evolution.
- **SINGLE-CELL FLAG:** Within Thread 1, essentially all the strong instructive-Vmem evidence is *multicellular* (embryonic tissue fields, gap-junction-coupled collectives). Bioelectric signaling in *individual* eukaryotic cells (resting potential influencing proliferation/differentiation) exists in the cell-biology literature, but the *instructive morphogenetic* claims depend on multicellular coupling (gap junctions, tissue-scale gradients). Single-cell bioelectric "control of pattern" is largely *extrapolated* from multicellular systems — a genuine evidential asymmetry.

---

## Thread 2 — Planaria regeneration and bioelectric "pattern memory"

### (a) Established empirical findings
**Scale: whole organism (planarian flatworms, principally *Dugesia japonica*).**

- **Gap-junction blockade → two-headed worms (Oviedo, Morokuma, Walentek et al., 2010, *Dev Biol* 339:188–199; Nogi & Levin, 2005).** Brief exposure of amputated fragments to the gap-junction blocker octanol (8-OH) or heptanol produced bipolar two-headed regenerates. **Scale: whole organism.**
- **H,K-ATPase / Vmem required for head regeneration (Beane, Morokuma, Adams & Levin, 2011, *Chem Biol* 18:77–89; Beane et al., 2013, *Development* 140:313–322).** Hyperpolarization blocked head regeneration (0-head); depolarization (e.g., ivermectin opening Cl⁻ channels with depolarizing chloride) biased toward two-head outcomes; the H,K-ATPase manipulation altered head shape.
- **Long-term, "stochastic" editing (Durant, Morokuma, Fields, Williams, Adams & Levin, 2017, *Biophysical Journal* 112:2231–2243).** This is the key paper, using a clonal strain of *D. japonica*. In the authors' verbatim words: "Temporary modulation of regenerative bioelectric dynamics in amputated trunk fragments of planaria stochastically results in a constant ratio of regenerates with two heads to regenerates with normal morphology. Remarkably, this is shown to be due not to partial penetrance of treatment, but a profound yet hidden alteration to the animals' patterning circuit." Morphologically *normal*-looking regenerates, when re-cut **in plain water with no further treatment**, again produced the same ratio of two-headed worms — a "cryptic" altered patterning state not visible in histology, gene expression, or stem-cell distribution. **Scale: whole organism.**

### (b) Levin's theoretical/interpretive framing
- The interpretation that the worm stores its "target morphology" as a rewritable bioelectric "pattern memory" — analogous to memory in a brain, editable without genomic change — is an *interpretive overlay* (Levin, 2021; Pezzulo, LaPalme, Durant & Levin, 2021, *Phil Trans R Soc B* 376:20190765, "bistability of somatic pattern memories"). The framing imports the vocabulary of memory, setpoints, and counterfactual representation. **Mark: interpretive.**

### (c) Open or disputed
- **Replication concentration:** The modern bioelectric two-headed "pattern memory" program traces overwhelmingly to the Levin lab and collaborators (Oviedo 2010; Beane 2011/2013; Durant 2017; Pezzulo 2019/2021). Older external precedent exists (Marsh & Beams, 1947/1952, on electric fields and planarian polarity), but independent modern replication of the *bioelectric pattern-memory* claim is limited. Levin himself notes there is "only one known strain of planaria that permanently propagates an unusual anatomy."
- **Penetrance/interpretation:** The gap-junction-blocker effects are *stochastic* (a minority fraction become two-headed). Levin interprets the constant ratio as evidence of a hidden stored memory with perceptual-style bistability; a skeptic can argue the data under-determine "memory" vs. an altered but non-cognitive dynamical attractor.
- **SINGLE-CELL FLAG:** This entire thread is *whole-organism/tissue*; it bears on single-celled eukaryotes only by analogy, not directly.

---

## Thread 3 — Xenobots and Anthrobots (engineered constructs)

### (a) Established empirical findings
**Scale: engineered construct (multicellular assemblies).**

- **Xenobots v1 (Kriegman, Blackiston, Levin & Bongard, 2020, *PNAS* 117(4):1853–1859).** Cell source: *Xenopus laevis* embryonic cells (skin/epidermal + cardiac muscle). An evolutionary algorithm (run at UVM) searched in silico for body shapes producing locomotion; Blackiston manually sculpted skin + contractile cardiac tissue into the designs. The cardiac tissue's spontaneous contractions drove locomotion; simulated and physical trajectories matched closely. **Scale: engineered construct.**
- **Xenobots v2 (Blackiston, Lederer, Kriegman, Garnier, Bongard & Levin, 2021, *Science Robotics* 6(52):eabf1571).** Made from whole *Xenopus* animal-cap explants; cells reorganized cilia to the outer surface and achieved coordinated **ciliary locomotion** (rather than cardiac actuation). Demonstrated behaviors: locomotion, traversal of mazes, collective behavior, and limited self-repair. The paper itself states "the xenobots reported to date have no known mechanism of sensor-motor coordination."
- **Kinematic self-replication (Kriegman, Blackiston, Levin & Bongard, 2021, *PNAS* 118(49):e2112672118).** C-shaped (Pac-Man) xenobots, swirling via cilia, pushed loose dissociated stem cells into piles; those piles compacted and matured into new motile xenobots (each copy taking roughly five days under optimal conditions, per NPR's reporting of the team). AI-designed semitoroidal shapes produced offspring ~149% larger in diameter than spheroid offspring, extending replication from a maximum of two rounds (wild-type spheroids) to three or four rounds. The process halts without added cells. **Scale: engineered construct.**
- **Anthrobots (Gumuskaya, Srivastava, Cooper, Lesser, Semegran, Garnier & Levin, 2023, *Advanced Science* 11(4):2303575, "Motile Living Biobots Self-Construct from Adult Human Somatic Progenitor Seed Cells").** Cell source: **adult human tracheal/airway epithelial cells**, no genetic modification. Single cells grown in 3D scaffolding formed organoids; a special bath induced cilia to face outward, producing self-assembled motile "biobots." Per the abstract, these are "a spheroid-shaped multicellular biological robot (biobot) platform with diameters ranging from 30 to 500 microns… motility patterns ranging from tight loops to straight lines and speeds ranging from 5–50 microns s⁻¹," and (per Tufts Now/*Scientific American*) they survive roughly 45–60 days before biodegrading. Movement type correlated with ciliary distribution (circlers, wigglers, etc.), and Anthrobots could fuse into "superbots." In a 2D assay, superbots placed across a scratch "wound" in a layer of cultured human neurons were associated with substantial neurite regrowth bridging the gap; neurons did not regrow where Anthrobots were absent; inert materials (starch, silicone) had no such effect. **Scale: engineered construct; neuron assay is tissue-level in vitro.**

### (b) Levin's theoretical/interpretive framing
- "Robot," "reconfigurable organism," "novel organism/life form," "kinematic self-replication," and "biobot" are *interpretive labels*. Levin frames xenobots as evidence of latent morphological/behavioral plasticity ("the genome is not a strict blueprint") and as "a new kind of organism." On replication, Levin explicitly says "nobody's claiming that the xenobots sat around agonizing over how they were going to make copies." **Mark: interpretive.**

### (c) Open or disputed
- **"Self-replication" framing contested.** The constructs do not grow and shed offspring; they push *pre-existing* loose cells into piles that become new constructs, and the process halts after ≤2–4 rounds without intervention. Even sympathetic insiders are cautious: Jamie Davies (Edinburgh; a Levin co-author on synthetic morphology) told *Scientific American* (Nov 2023) that "by and large, the *Xenopus* embryo community who know these cells could not really see what the fuss was about." (The phrase "somewhat random pieces of human tissue that look superficially like microorganisms" is the magazine author's paraphrase of the skeptical view, not Davies's verbatim words.)
- **Neuron-bridging mechanism unknown** ("the exact mechanism behind how Anthrobots stimulate neuron growth remains unclear"); the therapeutic vision (Astonishing Labs funding) is prospective, not demonstrated in vivo.
- **SINGLE-CELL FLAG:** These are *constructs built from many cells*; the "self-construct" claim is about multicellular self-assembly, not single-cell cognition.

---

## Thread 4 — Basal cognition, TAME, and multiscale competency

### (a) Established empirical findings
- The empirically grounded part is the *competency* phenomenology already described: regulative development, regeneration to a target morphology from scrambled/partial starting conditions, and the *Xenopus*/planaria manipulations. These show goal-*directed-looking* robustness. **Scale: tissue/whole organism/construct.**
- Single-cell "learning" results that Levin invokes (e.g., *Physarum* maze/habituation, ciliate conditioning, *Lacrymaria* hunting) come **largely from other labs** (Dussutour, Boussard, Nakagaki; Marshall lab on *Lacrymaria*/*Stentor*) and are themselves empirically contested (see critics).

### (b) Levin's theoretical/interpretive framing
- **TAME — Technological Approach to Mind Everywhere (Levin, 2022, *Frontiers in Systems Neuroscience* 16:768201; arXiv:2201.10346).** Explicitly a *Perspective/framework*, not a data paper. Core tenets: a continuum of cognitive capacities (no bright line between "true cognition" and "just physics"); no privileged material substrate; cognition defined functionally (learning, problem-solving, goal-directedness, scaled appropriately to each system).
- **Cognitive light cone:** the boundary in space and time of the largest goal a system can pursue — a schematic of "goal space" (illustrated by the brainless ciliate *Lacrymaria* navigating to meet metabolic needs).
- **Multiscale competency architecture (MCA):** nested layers of homeostatic agents, each a substrate for the layer above (Fields & Levin, 2020, *BioEssays*; Levin, 2023, *Cell Mol Life Sci* 80:142, "Darwin's agential materials").
- **Levin–Watson collaboration (Watson & Levin, 2023, *Collective Intelligence* 2(2); Watson, Levin & Buckley, 2022, *Front Ecol Evol*).** Argues development and evolution are themselves "collective intelligence"/cognitive architectures regardless of substrate.
- **Friston/Pezzulo connections:** active-inference / free-energy and Markov-blanket formalisms (Kuchling, Friston, Georgiev & Levin, 2019, *Physics of Life Reviews*; Fields et al., 2023, active inference). All explicitly theoretical. **Mark: philosophical/theoretical framework.**

### (c) Open or disputed
- Whether the cognitive vocabulary has *predictive* value beyond redescription is the central dispute (below). Levin's defense ("teleophobia" — the claim that *under*-attributing agency is as costly an error as *over*-attributing it; the engineering "proof is in the pudding") is itself a contested philosophical stance, not a neutral methodology.

---

## Critics and Skeptics (substantive)

This section presents the strongest skeptical case alongside Levin's framing and deliberately does **not** harmonize them.

### Conceptual critics (philosophy of biology / mind)
- **Massimo Pigliucci** (CUNY), "Nope, It Isn't 'Cognition All the Way Down'" (essay responding to Levin & Dennett's 2020 *Aeon* piece; **flagged: non-peer-reviewed blog essay**). Argument: Levin & Dennett illegitimately collapse Dennett's own *intentional stance* (treating X *as if* it had goals — a predictive heuristic) into a literal claim that cells *have* goals/cognition, stretching "cognition" until it loses content.
- **Carrie Figdor** (Iowa), *Biology & Philosophy* 37(6):52 (2022) and a chapter in *Philosophy of Plant Cognition* (2024). Objects to the "freewheeling use of functional ascriptions" that neglects the *evolutionary individuation* of biological characters (Character-Species Separation; Character-Phenotype Separation): cognitive functions co-evolve with their substrate-dependent realizers, so cross-clade ascription "erases lineage-specific histories." NUANCE: her 2018 book *Pieces of Mind* defends "Literalism" (taking scientists' psychological predicates literally), so she is *not* a blanket anthropomorphism-skeptic — her objection is specifically to *unparsimonious cross-clade extension*.
- **Fred Keijzer** (Groningen) and colleagues — "Making decisions does not suffice for minimal cognition" (*Adaptive Behavior* 11(4):266–269, 2003) and van Duijn, Keijzer & Franken, "Principles of minimal cognition: casting cognition as sensorimotor coordination" (*Adaptive Behavior* 14(2):157–170, 2006). Position: *adaptive behavior is not automatically cognition*; the lower bound of cognition should be drawn at **sensorimotor coordination** mediated by a dedicated regulatory (proto-nervous) infrastructure. Keijzer's verbatim worry: "From an embodied perspective perception-action provides the key feature for anything cognitive… The problem is that we hardly have any good criteria on this count, just intuitions." (Keijzer later co-published with Lyon/Levin, so this is "draw the line rigorously," not blanket rejection.)
- **Johannes Jaeger, Denis Walsh, John Vervaeke et al.**, "Naturalizing relevance realization: why agency and cognition are fundamentally not computational" (*Frontiers in Psychology* 15:1362658, 2024). Argument: organismic agency/cognition are *not computational*; algorithmic/free-energy frameworks (Levin, Friston) "ignore the difference in organization between a living and non-living system." Grounded in the autopoiesis/organizational tradition.
- **Daniel Nicholson** ("Organisms ≠ Machines," *Stud Hist Phil Biol Biomed Sci* 44:669–678, 2013; *Everything Flows*, OUP, 2018). Processual critique that organisms are dynamically stable flows, not designed machines — a "simpler dynamical-systems framing is available" counterweight (target is mechanism, not cognition per se).
- The classic "mark of the cognitive requires representation/intentionality" camp (Adams & Aizawa) supplies the bar that Levin's own recent rebuttal (Chis-Ciure & Levin, 2025, *Synthese*) concedes the critics press: that proponents are "equivocating on terms like 'learning,' 'memory,' or 'decision-making'… relying on a terminological loosening or metaphorical extension rather than demonstrating genuine cognitive processes" (which would require intentionality, intensionality, and the possibility of *mis*representation).

### Empirical skeptics
- **Loy et al. (2021), *J Exp Psychol: Animal Learning & Cognition* 47(3):234–251.** Review concluding associative learning shows "clear limitations and at least partial lack of replicability" in unicellular organisms (*E. coli*, *Paramecium*, *Physarum*) — directly relevant to the single-cell "learning" Levin invokes.
- **Gershman, Balbi, Gallistel & Gunawardena (2021), *eLife* 10:e61907, "Reconsidering the evidence for learning in single cells."** Sympathetic in aim but documents that historical single-cell learning claims were "non-reproducible or subject to more acceptable interpretations," and that the foundational Gelber *Paramecium* results failed to rule out confounds.
- **Mallatt, Blatt, Draguhn, Robinson & Taiz (2021), "Debunking a myth: plant consciousness," *Protoplasma* 258:459–476.** Argues aneural "cognition/consciousness" claims start from a false dichotomy, "confusingly redefine accepted cognitive terms," fail the burden of proof for extraordinary claims, and ignore more parsimonious explanations. Represents the "nervous-system-required" pole (Feinberg & Mallatt).

### Sympathetic but methodologically cautious
- **Pamela Lyon**, "Of what is 'minimal cognition' the half-baked version?" (*Adaptive Behavior* 28(6):407–424, 2020). A founder of basal cognition who nonetheless warns that loose qualifiers ("minimal," "proto") smuggle in confusion and that synthetic/toy instantiations should not be mistaken for the real function.
- **Ginsburg & Jablonka**, *The Evolution of the Sensitive Soul* (MIT Press, 2019). Propose Unlimited Associative Learning as a *demanding* transition marker — evolutionary continuity, but a high bar for where genuine cognition/consciousness begins.
- **Fábregas-Tejeda & Sims (2025), *History and Philosophy of the Life Sciences* 47(1):10.** Defends basal cognition by analogy to Evo-Devo while attaching "cautionary notes that should not be disregarded." A constructive middle that also catalogs the skeptics (Figdor; Loy et al.; Mallatt et al.).

---

## Researcher / Lab Map

**Levin lab and core collaborators**
- **Michael Levin** — PI, Allen Discovery Center at Tufts; Vannevar Bush Professor of Biology; also Wyss Institute (Harvard).
- **Douglas Blackiston** — microsurgeon/biologist; built xenobots and ran the anthrobot/neuron assays.
- **Gizem Gumuskaya** — Tufts/Wyss PhD (architecture background); lead author on Anthrobots.
- **Josh Bongard** (UVM) & **Sam Kriegman** (then UVM; later Northwestern) — computer scientists/roboticists; evolutionary-algorithm design of xenobots.
- **Fallon Durant, Junji Morokuma, Wendy Beane, Néstor Oviedo, Maya Emmons-Bell, Vaibhav Pai, Dany Spencer Adams** — key experimental authors on planaria/*Xenopus* bioelectricity.
- **Christopher Fields** — theory co-author (scale-free biology, active inference).
- **Richard Watson** (Southampton) — evolution-as-collective-intelligence collaborator.
- **Giovanni Pezzulo** — active-inference / pattern-memory bistability collaborator.
- **Karl Friston** connection — via active-inference/free-energy formalisms (Kuchling et al.; Fields et al.).
- **Daniel Dennett** (d. 2024) — philosophical collaborator ("Cognition all the way down," *Aeon* 2020).
- **Jamie Davies** (Edinburgh) — synthetic-morphology co-author; sympathetic but publicly cautious about some claims.

**Named critics / cautious voices**
- Conceptual: Carrie Figdor, Fred Keijzer & Marc van Duijn, Johannes Jaeger / Denis Walsh / John Vervaeke, Daniel Nicholson, Massimo Pigliucci (essay); representation-camp: Adams & Aizawa.
- Empirical: Loy et al.; Samuel Gershman & Jeremy Gunawardena; Jon Mallatt & Lincoln Taiz (plant-consciousness debunking).
- Sympathetic-cautious: Pamela Lyon; Simona Ginsburg & Eva Jablonka; Matthew Sims & Alejandro Fábregas-Tejeda.

---

## Recommendations (for the user's synthesis)

1. **Treat Thread 1 (instructive Vmem) and Thread 2 (planaria) as the empirical backbone**, but cite the *primary* papers (Pai 2012; Beane 2011; Durant 2017; Oviedo 2010) and report what the Results show, not abstract spin. The benchmark that would most strengthen them: *independent, non-Levin-lab replication* of the planaria pattern-memory cryptic-phenotype result. Until then, keep "pattern memory" tagged as interpretive.
2. **Keep the epistemic layers separate in your own writing.** The data ("voltage manipulation changes anatomy") are robust; the gloss ("the tissue remembers its goal") is a framework choice. Both can be reported without endorsing the second.
3. **For single-cell claims, lean on non-Levin primary sources** (Dussutour/Boussard *Physarum*; Marshall lab *Lacrymaria*/*Stentor*) and explicitly flag the replication concerns (Loy et al. 2021; Gershman et al. 2021). Do not let multicellular results stand in for single-cell cognition.
4. **Present xenobots/anthrobots as demonstrated constructs with contested labels.** "Kinematic self-replication" is accurate as a *defined technical term* but misleading if read as biological reproduction; cite the quantitative specifics (30–500 µm diameters, 5–50 µm/s, ≤2–4 replication rounds, ~5-day cycle, 45–60-day lifespan).
5. **Give critics their own voice with citations**, especially Figdor (evolutionary individuation), Keijzer (sensorimotor lower bound), and Jaeger/Walsh (non-computational agency), plus the empirical replication skeptics. The central live question is *predictive value vs. redescription*.
6. **Threshold that would change the assessment:** if the agential framework generates a *novel, risky, confirmed prediction* that a mechanistic/dynamical account demonstrably could not, the "merely redescriptive" charge weakens substantially. Levin's team argues the regeneration/limb experiments already meet this bar; critics dispute it. Watch for such predictions, ideally pre-registered and externally replicated.

## Caveats
- Several widely circulated claims rest on **popular-science or interview sources** (Quanta, Scientific American, IEEE Pulse/EMBS, NPR, Tufts Now press releases, podcasts). These are flagged in-text; the load-bearing citations are the peer-reviewed papers (PNAS, Science Robotics, Advanced Science, Development, Biophysical Journal).
- The **Pigliucci critique is a blog essay**, not peer-reviewed; it is included because it is a clearly attributable, substantive objection from a named philosopher of science. Its decisive wording should be verified against the original before quotation.
- **Replication asymmetry:** the bioelectric pattern-memory and instructive-Vmem claims are disproportionately from one lab. This is a structural feature of the literature — not by itself evidence against the claims, but it bears on confidence.
- **Single-cell evidence is the thinnest part of the program** relative to its rhetorical prominence; the genuinely single-celled eukaryote results Levin cites are largely external and partly contested.
- This survey reflects sources available as of the research date (May 2026); some 2024–2026 items (e.g., Chis-Ciure & Levin, *Synthese*) are recent and their reception is still developing.

## References (APA 7th edition, primary papers cited)

Adams, D. S., Masi, A., & Levin, M. (2007). H+ pump-dependent changes in membrane voltage are an early mechanism necessary and sufficient to induce *Xenopus* tail regeneration. *Development, 134*(7), 1323–1335.

Beane, W. S., Morokuma, J., Adams, D. S., & Levin, M. (2011). A chemical genetics approach reveals H,K-ATPase-mediated membrane voltage is required for planarian head regeneration. *Chemistry & Biology, 18*(1), 77–89.

Beane, W. S., Morokuma, J., Lemire, J. M., & Levin, M. (2013). Bioelectric signaling regulates head and organ size during planarian regeneration. *Development, 140*(2), 313–322.

Blackiston, D., Lederer, E., Kriegman, S., Garnier, S., Bongard, J., & Levin, M. (2021). A cellular platform for the development of synthetic living machines. *Science Robotics, 6*(52), eabf1571.

Durant, F., Morokuma, J., Fields, C., Williams, K., Adams, D. S., & Levin, M. (2017). Long-term, stochastic editing of regenerative anatomy via targeting endogenous bioelectric gradients. *Biophysical Journal, 112*(10), 2231–2243.

Fields, C., & Levin, M. (2020). Scale-free biology: Integrating evolutionary and developmental thinking. *BioEssays, 42*(8), 1900228.

Figdor, C. (2022). What could cognition be, if not human cognition? Individuating cognitive abilities in the light of evolution. *Biology & Philosophy, 37*(6), 52.

Gershman, S. J., Balbi, P. E., Gallistel, C. R., & Gunawardena, J. (2021). Reconsidering the evidence for learning in single cells. *eLife, 10*, e61907.

Ginsburg, S., & Jablonka, E. (2019). *The evolution of the sensitive soul: Learning and the origins of consciousness.* MIT Press.

Gumuskaya, G., Srivastava, P., Cooper, B. G., Lesser, H., Semegran, B., Garnier, S., & Levin, M. (2023). Motile living biobots self-construct from adult human somatic progenitor seed cells. *Advanced Science, 11*(4), 2303575.

Jaeger, J., Riedl, A., Djedovic, A., Vervaeke, J., & Walsh, D. (2024). Naturalizing relevance realization: Why agency and cognition are fundamentally not computational. *Frontiers in Psychology, 15*, 1362658.

Keijzer, F. A. (2003). Making decisions does not suffice for minimal cognition. *Adaptive Behavior, 11*(4), 266–269.

Kriegman, S., Blackiston, D., Levin, M., & Bongard, J. (2020). A scalable pipeline for designing reconfigurable organisms. *Proceedings of the National Academy of Sciences, 117*(4), 1853–1859.

Kriegman, S., Blackiston, D., Levin, M., & Bongard, J. (2021). Kinematic self-replication in reconfigurable organisms. *Proceedings of the National Academy of Sciences, 118*(49), e2112672118.

Kuchling, F., Friston, K., Georgiev, G., & Levin, M. (2019). Morphogenesis as Bayesian inference: A variational approach to pattern formation and control in complex biological systems. *Physics of Life Reviews, 33*, 88–108.

Levin, M. (2022). Technological approach to mind everywhere: An experimentally-grounded framework for understanding diverse bodies and minds. *Frontiers in Systems Neuroscience, 16*, 768201.

Levin, M. (2023). Darwin's agential materials: Evolutionary implications of multiscale competency in developmental biology. *Cellular and Molecular Life Sciences, 80*(6), 142.

Levin, M., & Dennett, D. C. (2020, October 13). Cognition all the way down. *Aeon.*

Loy, I., Carnero-Sierra, S., Acebes, F., Muñiz-Moreno, J., Muñiz-Diez, C., & Sánchez-González, J. C. (2021). Where association ends. A review of associative learning in invertebrates, plants and protista. *Journal of Experimental Psychology: Animal Learning and Cognition, 47*(3), 234–251.

Lyon, P. (2020). Of what is "minimal cognition" the half-baked version? *Adaptive Behavior, 28*(6), 407–424.

Mallatt, J., Blatt, M. R., Draguhn, A., Robinson, D. G., & Taiz, L. (2021). Debunking a myth: Plant consciousness. *Protoplasma, 258*(3), 459–476.

Nicholson, D. J. (2013). Organisms ≠ machines. *Studies in History and Philosophy of Biological and Biomedical Sciences, 44*(4), 669–678.

Oviedo, N. J., Morokuma, J., Walentek, P., Kema, I. P., Gu, M. B., Ahn, J. M., Hwang, J. S., Gojobori, T., & Levin, M. (2010). Long-range neural and gap junction protein-mediated cues control polarity during planarian regeneration. *Developmental Biology, 339*(1), 188–199.

Pai, V. P., Aw, S., Shomrat, T., Lemire, J. M., & Levin, M. (2012). Transmembrane voltage potential controls embryonic eye patterning in *Xenopus laevis*. *Development, 139*(2), 313–323.

Pezzulo, G., LaPalme, J., Durant, F., & Levin, M. (2021). Bistability of somatic pattern memories: Stochastic outcomes in bioelectric circuits underlying regeneration. *Philosophical Transactions of the Royal Society B, 376*(1821), 20190765.

Tseng, A. S., Beane, W. S., Lemire, J. M., Masi, A., & Levin, M. (2010). Induction of vertebrate regeneration by a transient sodium current. *Journal of Neuroscience, 30*(39), 13192–13200.

van Duijn, M., Keijzer, F., & Franken, D. (2006). Principles of minimal cognition: Casting cognition as sensorimotor coordination. *Adaptive Behavior, 14*(2), 157–170.

Watson, R., & Levin, M. (2023). The collective intelligence of evolution and development. *Collective Intelligence, 2*(2).

Fábregas-Tejeda, A., & Sims, M. (2025). On the prospects of basal cognition research becoming fully evolutionary: Promising avenues and cautionary notes. *History and Philosophy of the Life Sciences, 47*(1), 10.