# **The Robot Personality Scientist**

## **A Thought Experiment in Behavioral Phenotype Measurement Across Taxa, Timescales, and Evolutionary Change**

**Working Document — Draft v0.1** **Date: April 2026**

---

## **Overview**

This document develops a thought experiment in five stages. Each stage inherits the dataset and analytical infrastructure from the previous one, and each unlocks questions that were unanswerable before.

| Stage | Setting | Timescale | Core Question |
| ----- | ----- | ----- | ----- |
| 1 | Robot in a fish lab | Months | How do you extract personality from a continuous behavioral stream? |
| 2 | Robot across taxa | Years | Is personality structure conserved across vertebrate classes? |
| 3 | Drones in the wild | Lifetimes | Does personality predict fitness in natural environments? |
| 4 | Century-scale surveillance | Generations | Can you watch personality evolve? |
| 5 | Genomic overlay \+ scenario modeling | Evolutionary time | What makes a mind? |

The thought experiment is not purely hypothetical. The technology trajectory — automated behavioral classification, drone-based wildlife monitoring, environmental DNA, long-term ecological monitoring networks — is heading here. The value of the exercise is working backward from the dataset we will eventually have to the questions we should be designing our measurement systems to answer now.

---

## **Stage 1: The Robot in the Fish Lab**

### **The Setup**

You are a personality assessment bot. You have a video camera collecting continuous data on a set of individually identified zebrafish. You have environmental sensors in the tanks (water chemistry, temperature, light cycle, vibration). Your job is to determine which fish have consistent behavioral individuality — personality — and whether individual differences are correlated across behavioral domains — behavioral syndromes.

### **The Core Engineering Problem**

Your raw inputs are continuous streams. Your outputs must be discrete: behavioral episodes, classified by type, attributed to individuals, decomposed into stable versus transient variance components. The pipeline has four stages, each with distinct computational challenges.

**Segmentation.** Where does one behavior stop and the next begin? This is a change-point detection problem on multivariate time series. You need to detect transitions in the statistical properties of the movement stream — mean speed, turning angle distribution, spatial range, proximity to landmarks and conspecifics — in real time. The challenge is that behavioral transitions are not always sharp. A fish doesn't switch from "exploring" to "freezing" instantaneously; there are transitional states, graded responses, and context-dependent thresholds. Your change-detection algorithm must balance sensitivity (detecting real transitions) against specificity (not hallucinating transitions from motor noise).

**Classification.** Once you've carved the stream into episodes, what kind of behavior is each one? You need a species-appropriate ethogram — a behavioral taxonomy — that maps movement signatures onto functional categories. For zebrafish: thigmotaxis (wall-following, anxiety proxy), center exploration (boldness proxy), rapid darting (escape behavior), slow cruising (routine locomotion), social approach, social avoidance, freezing, surface breathing. The classification problem is that the same motor pattern can serve different functions depending on context. Rapid movement toward a conspecific is social approach; the same kinematics directed away from a novel object is escape. Context must inform classification.

**Attribution.** Which variance in classified behavior is stable across time within an individual (personality) versus fluctuating within-individual noise? This is the repeatability problem. You need repeated observations of the same individual across multiple occasions, contexts, and time points. Average repeatability across animal personality studies is approximately 0.4, meaning 60% of variance in any single behavioral observation is within-individual variation. A single measurement tells you more about the situation than the fish.

**Covariance.** Do the stable individual differences correlate across behavioral categories? A fish that is consistently bold in predator-cue contexts — is it also consistently exploratory in novel environments, consistently aggressive toward conspecifics, consistently active during baseline periods? If yes, these correlated individual differences constitute a behavioral syndrome. The covariance matrix of among-individual variation across behavioral categories is the syndrome structure.

### **What the Literature Offers**

The methodological infrastructure for this pipeline exists, though it has rarely been assembled end-to-end.

For **segmentation and temporal decomposition**: Araya-Ajoy, Mathot & Dingemanse (2015) developed the MultiRR framework for decomposing repeated behavioral observations into short-term repeatability, long-term repeatability, and reaction norm components using multilevel random regression. Their simulation work establishes minimum sample requirements: approximately 1,000 total observations with more than 20 individuals for reliable intercept-slope decomposition.

For **simultaneous estimation of personality, plasticity, and predictability**: O'Dea, Noble & Nakagawa (2022) provide the double hierarchical generalized linear model (DHGLM) framework in brms/Stan. This matters because a fish that is *consistently erratic* is behaviorally different from one that is *inconsistently calm*. Both are real individual differences and they're different constructs. The DHGLM estimates all three — mean (personality), slope (plasticity), and residual variance (predictability) — per individual simultaneously.

For **temporal scale dependence**: Kermany, Martin & Careau (2023) demonstrated that the sign of the personality–predictability correlation reverses across temporal bin sizes in wild mice. This is a critical warning: the segmentation window size is not a neutral design choice. It changes what the robot finds.

For **repeatability estimation and quality criteria**: Dingemanse & Wright (2020) establish the minimum standards. Valid personality studies require repeated measures, univariate mixed-effects models reporting all variance components, adjusted repeatability controlling for fixed effects, and multivariate GLMMs for syndrome structure.

For **species-specific calibration**: Singh et al. (2025) tested exactly zebrafish. Only open-field area exploration showed significant repeatability (R ≈ 0.36). Emergence latency was modulated by hunger state. Shoal size preference was not repeatable at all. This tells the robot which assays are worth investing in and which will produce noise.

### **What's Missing**

The bibliography does not cover the computer vision and signal processing layer between raw video and statistical models — pose estimation (DeepLabCut), hidden Markov models for behavioral state classification, or how sensor noise and tracking errors propagate into repeatability estimates. This engineering layer is the bridge between the raw data stream and the statistical infrastructure described above. It is not trivial: measurement error had the largest impact on accuracy in simulation studies (partial η² \= .29–.32), meaning camera resolution and tracking algorithm quality directly affect whether personality can be detected at all.

---

## **Stage 2: The Robot Across Taxa**

### **The Setup**

You now run the same measurement pipeline for five years across a range of vertebrate species: fish, amphibians, small mammals, primates. You have collected continuous behavioral stream data — segmented, classified, and decomposed — for multiple species spanning four vertebrate classes. For each species you have individual-level behavioral episode sequences, repeatability estimates per behavioral category, multivariate covariance matrices (syndrome structure), reaction norm parameters, and all of this at multiple temporal scales.

### **Three Questions About Behavioral Complexity**

**Question 1: Is the behavioral repertoire larger in more encephalized species?**

You can count the number of discriminable behavioral categories per species — the effective behavioral repertoire size. This should increase with brain size, consistent with the finding that pallial neuron counts (not brain volume per se) predict innovation propensity across bird species, and that behavioral innovation frequency correlates with relative executive brain volume across primates.

But the count is sensitive to your segmentation parameters. If you use the same change-point detection thresholds for zebrafish and chimpanzees, you'll either oversegment fish behavior or undersegment primate behavior. You need sensitivity analyses varying thresholds and reporting the range of category counts that are stable.

**Question 2: Is personality covariance structure more differentiated in cognitively complex species?**

This is the more interesting question. For each species you have a multivariate among-individual covariance matrix. You can characterize each matrix's structure along several dimensions:

* *Dimensionality*: How many independent axes of among-individual variation? Eigenvalue decomposition or Exploratory Graph Analysis can estimate this without imposing a factor model. If primates have five semi-independent personality dimensions and fish have two, that's a complexity gradient.

* *Integration versus modularity*: Are behavioral categories tightly correlated (a single boldness-shyness axis dominates) or modular (separate clusters with weak between-cluster connections)? Simpler nervous systems may produce more integrated, lower-dimensional syndromes, while complex brains support modular organization.

* *Stability across contexts*: Do syndrome structures hold when you change the testing environment, or do they reorganize? If primate syndromes are more stable across contexts, that might reflect more canalized personality architecture supported by prefrontal executive systems.

**Question 3: Is there a conserved core structure that scales up?**

The cross-cultural human lexical work finds only three personality dimensions — Extraversion, Agreeableness, Conscientiousness — that replicate robustly across all languages examined. Cross-taxa evidence converges: a core approach-avoidance dimension (boldness-shyness, proactive-reactive) appears in every vertebrate studied. A sociability dimension appears wherever the species is social. Additional differentiation — separating exploration from boldness, or conscientiousness from agreeableness — seems to emerge with increasing social and ecological complexity.

The prediction: a conserved two- or three-dimensional core, with additional dimensions accreting as neural and social complexity increases. You test this by rotating each species' factor solution toward a common target and measuring congruence.

### **Organizing Lab Conditions by Personality-Diagnostic Power**

After five years of continuous observation, you have an empirical map of which environmental conditions *elicit discriminating behavioral variation* and which don't. You can rank contexts by their individual-differentiating power — which maximize among-individual variance relative to within-individual variance.

The critical insight: the same physical setup discriminates different personality dimensions depending on the species. An open field with a novel object is a boldness assay for a fish but closer to an exploration assay for a primate with no predator concern. The behavioral meaning of a context depends on the species' evolved threat ecology and social structure. Your robot can identify which contexts maximize individual-differentiating variance empirically, without assuming what the context "means" to the animal — but interpreting that variance requires species-specific ecological knowledge.

An additional complication: assay conditions themselves can *create* syndrome structure. Predation exposure generated a boldness-aggression correlation in sticklebacks that didn't exist before. The lab environment isn't just revealing pre-existing personality — it's partially constructing the covariance structure you observe.

### **Solitary Versus Gregarious Species**

Social species should show equal or greater personality dimensionality than solitary species, because sociality adds an entire behavioral domain (social tactics, dominance strategies, affiliative behavior, coalition management) on top of non-social behaviors. A positive feedback loop between sociality and social competence means more social living selects for more differentiated social cognitive capacities.

But solitary species might show high behavioral flexibility in non-social domains (foraging tactics, habitat use, risk assessment) because they can't rely on social information from conspecifics. The prediction: solitary species show *fewer personality dimensions* (because the social domain is minimal) but potentially *equivalent within-dimension behavioral flexibility*.

### **Species-Level Behavioral Traits as Personality Analogs**

Species-typical behavioral strategies — hibernation, migration, territory marking, caching, cooperative breeding — function as the taxa-level analogs of individual personality traits. The same trade-off axes that generate personality variation within species organize behavioral strategy variation across species:

* *Hibernation versus migration*: species-level manifestation of the reactive–proactive axis. Hibernators wait it out; migrants go find it.  
* *Territorial versus gregarious social organization*: species-level manifestation of the sociability–aggression trade-off.  
* *Caching versus immediate consumption*: species-level manifestation of the impulsivity–prudence axis.  
* *Cooperative versus independent breeding*: species-level manifestation of the prosociality axis.

Evolution generates behavioral diversity at two nested levels using the same underlying trade-off logic. At the species level, ecological constraints channel populations into strategic niches. Within each niche, individual variation along residual trade-off axes generates personality. The species-level strategy constrains which personality dimensions are expressed, but doesn't eliminate individual variation — it changes its character.

---

## **Stage 3: Drones in the Wild**

### **The Setup**

Your lab-derived measurement algorithms are used to train a fleet of observatory drones. These are assigned to continuously track different vertebrate taxa in their natural habitats. They observe the same individuals from birth to death, tracking all behavioral episodes in full ecological and social context. They do this continuously for 100 years.

### **What This Dataset Contains That Nothing Else Does**

The lab dataset gave you individual-level behavioral streams under controlled conditions. The drone dataset gives you something qualitatively different: individual-level behavioral streams embedded in their full ecological and social context, tracked across entire lifespans, across generations, across climatic and ecological change.

For long-lived species (primates, elephants, cetaceans, parrots, tortoises), 100 years captures multiple complete generations. For short-lived species (fish, amphibians, small rodents), it captures hundreds or thousands of generations. That's not just more data. It's a different kind of data. It lets you watch evolution happen.

### **Timescale 1: Within-Lifetime Development (months to years)**

For every tracked individual, you have a complete developmental behavioral trajectory — birth through senescence and death. You can now move from describing *what* changes in personality development to explaining *why*.

You can test state-behavior feedback models with real developmental data. Do bold juvenile fish that survive their first predation encounter become bolder adults? Do shy juveniles that avoid predation become increasingly cautious? The feedback loop prediction — that early behavioral tendencies generate state changes (body condition, social rank, territory quality) that reinforce those tendencies — can be tested directly because you have the full state-behavior time series for each individual.

Developmental sensitive period models can be tested rigorously: do individuals who experience adversity during specific developmental windows show different personality trajectories than those who experience equivalent adversity at other times? You have the actual environmental conditions (predation events, dominance reversals, resource scarcity, maternal loss) time-stamped in the drone record, not retrospectively reported.

For shorter-lived species, you can estimate the heritability of developmental trajectories themselves — not just the heritability of a trait measured at one age, but the heritability of the *shape* of personality development across the lifespan.

### **Timescale 2: Fitness Consequences and Natural Selection (years to decades)**

With lifetime reproductive success for every individual in your short-lived species — total offspring produced, offspring survival to reproduction, actual genetic contributions to the next generation — you can directly estimate natural selection on personality.

Prior meta-analyses found small average personality–fitness effects (r \~ 0.10), but from short studies with incomplete fitness measures. Your dataset provides complete lifetime fitness, enabling selection gradient estimation for every generation. Critically, you can track how selection fluctuates across years as ecological conditions change — the full temporal autocorrelation structure of selection on personality.

The deep analysis: personality-fitness relationships likely depend on population density, food availability, predation pressure, and social environment. With 100 years spanning natural fluctuations, droughts, disease outbreaks, and range shifts, you can map the full fitness landscape for personality across ecological conditions. You can test whether the fitness advantage of bold versus shy types oscillates with the frequency of each type in the population — the frequency-dependent selection prediction.

### **Timescale 3: Microevolution and Inheritance (decades to century)**

For species with one- to three-year generation times, 100 years gives you 30 to 100 generations. You can watch personality evolve in real time.

Complete pedigrees reconstructed from behavioral observation (mating, parturition, parent-offspring association) enable animal models to estimate additive genetic variance, maternal effects, and permanent environment effects on personality across generations.

Testable predictions:

* Does personality heritability change across generations as the population experiences different ecological conditions? Traits may be heritable in some environments but not others.  
* Does the genetic covariance structure (the G-matrix for personality) itself evolve? Syndrome structure might reorganize across decades as selection favors different trait combinations.  
* Can you detect gene-environment correlation building up across generations? If bold parents create ecological niches that make offspring bolder through developmental experience rather than genetic transmission, parent-offspring personality resemblance should exceed additive genetic predictions. The excess is the signature of niche construction contributing to personality inheritance.

### **Timescale 4: Cross-Taxa Macroevolutionary Patterns (full century)**

Now you can return to the behavioral complexity gradient question with far more power. Your lab data compared static syndrome structure across species. Your century-scale field data compare the *dynamics* of syndrome structure — how stable it is across ecological perturbations, how rapidly it reorganizes, how much it fluctuates across generations.

Two competing predictions:

1. **Cognitive buffering**: species with larger brains show *more stable* syndrome structures across environmental perturbations. Encephalization buffers organisms against environmental change, making behavioral individuality more deeply canalized.

2. **Cognitive flexibility**: species with larger brains show *more labile* syndrome structures, reorganizing readily as conditions change. Primate personality is more cognitive; fish personality is more physiological. Cognition is more context-sensitive than physiology.

The dataset distinguishes these by computing the temporal autocorrelation of syndrome structure within each species. How similar is the population-level covariance matrix in decade N to decade N+1?

---

## **Stage 4: Genomic Overlay**

### **The Setup**

Now add complete whole-genome sequences for every individual across every generation.

### **What Genomics Unlocks**

**Resolving missing heritability.** Human personality GWAS finds SNP heritability of 7–14%, far below twin-based estimates of 40–60%. In wild populations with complete pedigrees AND genomes AND behavioral phenotypes across 100 years, you can partition the gap: how much is rare variants? Gene-gene interaction? Gene-environment interaction that only manifests under specific ecological conditions? Non-genetic inheritance masquerading as genetic?

**Watching selection at the molecular level.** For fast-generation species experiencing novel selective pressures, you can track allele frequency change in real time and correlate it with behavioral phenotype data. When a population encounters a novel predator in year 37, you can watch whether boldness-associated alleles shift in frequency over subsequent generations, and whether behavioral change leads or lags genomic change.

**Decomposing gene-environment correlation.** You have each individual's genome from birth, the full environmental time series, and the complete behavioral developmental trajectory. You can estimate the portion of environmental variance that is genetically mediated (active gene-environment correlation) versus truly exogenous. This is the holy grail of developmental behavioral genetics.

**Testing whether genetic architecture is conserved across taxa.** With genomes and behavioral phenotypes across fish, amphibians, mammals, and primates, you can test whether the same gene families underlie the conserved core personality dimensions, or whether convergent behavioral phenotypes are built from different genetic substrates in different lineages — degeneracy at the genomic level.

---

## **Stage 5: Scenario Modeling**

### **Scenario A: Climate Change as Natural Experiment**

A century of continuous observation spanning accelerating climate change provides the most powerful natural experiment in the history of behavioral ecology. You're watching the selective environment change while tracking both behavioral and genomic responses.

**Altered environmental autocorrelation.** Climate change alters the temporal autocorrelation structure of environmental stressors — previously predictable seasonal patterns become erratic, extreme events become more frequent but less predictable. You can test whether populations exposed to decreasing environmental predictability evolve different stress response profiles compared to populations experiencing directional shifts without loss of predictability.

**Ecological traps.** As climate change reshapes habitats, some populations will fall into ecological traps — where formerly reliable environmental cues now lead to maladaptive responses. You can test whether personality type predicts which individuals are trapped versus which escape. Bold, exploratory types might discover habitat deterioration faster; shy, site-faithful types might persist in deteriorating habitat longer.

**Differential rates of behavioral versus morphological adaptation.** Behavioral traits have the lowest phylogenetic signal of any trait category — they evolve fastest. Your dataset, tracking behavioral, morphological, and physiological phenotypes simultaneously within each species experiencing the same climate perturbation, can estimate the relative rates of adaptive change across phenotypic levels.

### **Scenario B: Humanity Shrinks, Wilderness Grows**

**Behavioral release.** Urbanization increases within-population phenotypic variance by \~11%. If urbanization reverses, you can track whether urban-adapted populations show behavioral reversion as predation pressure returns and human-dominated selective regimes dissolve.

**Personality-biased range expansion.** As wilderness grows, populations expand into formerly occupied habitat. Dispersers have distinct personality profiles — bolder, more exploratory, less social. You can test whether the leading edge of expanding populations is behaviorally distinct from the core, and whether personality-biased dispersal creates founder effects shaping newly established populations.

**Community-level personality ecology.** As communities reassemble in expanding wilderness, you can test whether the personality composition of arriving species predicts community assembly trajectories. Do communities with more behaviorally diverse populations reach stable states faster?

**Does personality diversity increase as human selection pressure relaxes?** Human environments impose specific behavioral demands (urban boldness, disturbance tolerance, anthropogenic food exploitation) that may reduce personality diversity. Relaxing this selection might allow broader variation to persist, increasing population stability and adaptive capacity.

### **Scenario C: Domestication of Squirrels and Raccoons**

You can now watch two new domestication events unfold from the beginning with complete behavioral and genomic surveillance.

**Does the domestication syndrome emerge as a correlated package?** Or do different traits change at different rates via different genetic mechanisms? The neural crest cell hypothesis, the reproductive disruption hypothesis, and the taxon-specific genetic architecture hypothesis make different predictions that your data can distinguish.

**Personality changes under domestication selection.** Do the first generations selected for tameness show reduced boldness across all contexts, or only toward humans? Does the boldness-aggression syndrome reorganize, or does the entire proactive-reactive axis shift? Does domestication differentially affect affiliative versus agentic behavior?

**The feralization control.** Over 100 years, some captive-bred animals will inevitably escape and establish feral populations. You can watch the reverse process — which domestication-associated behavioral and genomic changes persist in feral environments and which are rapidly eliminated by natural selection. This gives you the full domestication-feralization cycle in real time.

**Comparing two independent domestication events.** With one rodent (squirrel) and one carnivore-adjacent (raccoon) species, you can test whether the same loci respond to domestication selection in both, or whether convergent phenotypic outcomes arise from different genomic substrates.

---

## **What the Thought Experiment Reveals About Current Science**

The entire exercise exposes how impoverished our actual data are relative to what we'd need to answer the questions we ask.

| What we currently do | What the thought experiment requires |
| ----- | ----- |
| Estimate heritability from twin studies with 2 time points | Complete pedigrees \+ genomes \+ behavioral phenotypes across 30–100 generations |
| Estimate fitness consequences from 2-year field studies | Lifetime reproductive success across fluctuating ecological conditions |
| Estimate cross-taxa personality structure from brief standardized assays | Continuous behavioral streams segmented at multiple temporal resolutions |
| Estimate personality development from 3–5 longitudinal waves | Complete developmental trajectories from birth to death |
| Estimate gene-environment interaction from candidate gene studies | Full genomes \+ full environmental time series \+ full behavioral trajectories simultaneously |

Many of our conclusions depend on extrapolations that the thought experiment dataset would either confirm or overturn. The exercise makes vivid exactly where the inferential gaps are.

### **The Measurement Problem Runs All the Way Down**

Each stage of the thought experiment introduces a version of the same fundamental problem: the measurement system partly constructs what it observes.

* The robot's segmentation algorithm determines how many behavioral categories exist  
* The choice of temporal bin size determines the sign of personality-predictability correlations  
* The lab environment can create syndrome structures that don't exist in nature  
* The drone's camera resolution and tracking accuracy set a floor on detectable individual differences  
* The statistical model (factor analysis versus network analysis, latent variable versus emergent variable) determines whether personality is a cause or a consequence of behavioral covariation

This isn't a flaw. It's the nature of psychological measurement. But the thought experiment makes the measurement dependence visible in a way that standard personality research, with its reliance on self-report questionnaires, typically obscures.

---

## **Key Citations by Stage**

### **Stage 1 (Robot in the Lab)**

* Araya-Ajoy, Mathot & Dingemanse (2015) — MultiRR framework for decomposing repeated behavioral observations  
* O'Dea, Noble & Nakagawa (2022) — DHGLM for personality, plasticity, and predictability estimation  
* Kermany, Martin & Careau (2023) — temporal scale dependence of personality-predictability correlations  
* Dingemanse & Wright (2020) — methodological criteria for valid personality studies  
* Singh et al. (2025) — zebrafish personality: which assays produce repeatable individual differences  
* Roche, Careau & Binning (2016) — R tutorial for repeatability estimation  
* McCune et al. (2023) — construct validity of behavioral flexibility measures via temporal and contextual repeatability

### **Stage 2 (Robot Across Taxa)**

* De Raad et al. (2010) — only three personality factors replicate across languages  
* De Raad et al. (2014) — three-factor pan-cultural kernel from simultaneous component analysis  
* Thalmayer et al. (2025) — cross-cultural Big Two (Social Self-Regulation, Dynamism)  
* Sol, Olkowicz, Sayol et al. (2022) — pallial neuron counts predict innovation  
* Taborsky (2021) — positive feedback loop between sociality and social competence  
* Taborsky & Oliveira (2012) — social competence as evolved behavioral reaction norm  
* Bell & Sih (2007) — predation exposure creates behavioral syndromes  
* Réale et al. (2007) — five-category temperament framework across taxa  
* Réale et al. (2010) — pace-of-life syndrome integrating behavior, physiology, life history  
* Sih & Del Giudice (2012) — speed-accuracy trade-off linking personality and cognitive style  
* Dingemanse, Kazem, Réale & Wright (2010) — behavioral reaction norm framework

### **Stage 3 (Drones in the Wild)**

* Sih et al. (2015) — state-behavior feedback models of personality development  
* Ostlund & Pérez-Edgar (2023) — two-hit developmental sensitive period model  
* Briley & Tucker-Drob (2014) — genetic and environmental contributions to personality stability  
* Dingemanse & Réale (2005) — natural selection on personality in wild populations  
* Smith & Blumstein (2008) — meta-analysis of personality-fitness consequences  
* Taborsky et al. (2021) — evolutionary theory of stress responses and environmental autocorrelation  
* Wolf, van Doorn & Weissing (2008) — frequency-dependent selection maintaining personality variation  
* Wolf & McNamara (2012) — physiological architecture enables personality evolution  
* Dingemanse & Wolf (2013) — between-individual differences in behavioral plasticity  
* Sih, Ferrari & Harris (2011) — behavioral mismatch under human-induced rapid environmental change  
* Wolf & Weissing (2012) — ecological consequences of personality diversity  
* Golino, Nesselroade & Christensen (2025) — Ergodicity Information Index

### **Stage 4 (Genomic Overlay)**

* Schwaba et al. (2025) — largest personality GWAS (N \> 1M)  
* Hatoum et al. (2023) — executive function GWAS: GABAergic, not dopaminergic  
* MacLean et al. (2019) — highly heritable dog breed behavioral differences  
* Andrade et al. (2024) — selection against domestication alleles in feral rabbits  
* Westlin et al. (2023) — degeneracy: many-to-one neural-behavioral mappings  
* Roberts & Jackson (2008) — sociogenomic model of personality development  
* Danchin et al. (2011) — inclusive inheritance beyond DNA  
* Maher (2008) — the missing heritability problem  
* Polderman et al. (2015) — meta-analysis of heritability across all human traits

### **Stage 5 (Scenario Modeling)**

* Thompson et al. (2022) — urbanization effects on phenotypic mean and variance  
* Thompson et al. (2025) — continental patterns of urban phenotypic variation  
* Cote et al. (2010) — personality-dependent dispersal  
* Sih et al. (2012) — ecological implications of behavioral syndromes  
* Hare, Wobber & Wrangham (2012) — self-domestication hypothesis  
* Gleeson & Wilson (2023) — reproductive disruption vs. NCC hypothesis  
* Johnsson, Henriksen & Wright (2021) — critique of the NCC hypothesis  
* Hansen Wheat, van der Bijl & Wheat (2020) — domestication syndrome traits don't covary in dogs  
* Gering et al. (2019) — feralization in animals  
* Hare (2017) — survival of the friendliest: human self-domestication  
* Depue & Morrone-Strupinsky (2005) — affiliative versus agentic extraversion  
* Blomberg, Garland & Ives (2003) — behavioral traits are more evolutionarily labile  
* Laland et al. (2015) — extended evolutionary synthesis  
* Laland (2025) — developmentalist view of inheritance

### **Cross-Cutting Methods**

* Christensen, Golino & Silvia (2020) — network psychometrics for personality validity  
* Condon et al. (2020) — bottom-up personality taxonomy  
* Wilson et al. (2010) — animal model for quantitative genetics in wild populations  
* Martin et al. (2025) — estimating selection on reaction norms  
* Careau & Garland (2012) — physiology-performance-behavior-fitness integration  
* Dall et al. (2012) — evolutionary ecology of individual differences  
* MacLean et al. (2012) — phylogenetic comparative methods for cognitive evolution  
* MacLean et al. (2014) — absolute brain volume predicts self-control across 36 species  
* Reader, Hager & Laland (2011) — species-level g factor in primates

---

## **Open Questions for Future Drafts**

1. **The temporal segmentation problem as a metaphor.** The robot's first challenge — where does one behavior stop and the next begin? — is the same challenge personality science faces at every level. Where does a trait stop and a state begin? Where does personality stop and psychopathology begin? Where does one factor stop and the next begin? The measurement system's segmentation choices are constitutive, not merely instrumental.

2. **Connection to BRILLIANCE architecture.** The evolutionary accretion model predicts a specific ordering: which personality dimensions should appear first phylogenetically (earliest vertebrates) and which should be later elaborations (mammals, primates, humans)? The thought experiment provides the empirical framework for testing this ordering.

3. **Connection to domestication.** The domestication scenario directly tests whether selection against reactive aggression (self-domestication hypothesis) or selection on reproductive ecology (reproductive disruption hypothesis) better explains correlated behavioral, morphological, and physiological change. This maps onto the question of whether Neuroticism/Emotional Stability is a primary personality dimension or an intersection zone construct.

4. **Connection to the cognitive-noncognitive distinction.** The robot never distinguishes cognitive from noncognitive. It measures behavioral streams and extracts variance components. The distinction only enters when humans interpret the output. This supports the BRILLIANCE position that the cognitive/noncognitive dichotomy is an artifact of measurement tradition, not a natural kind.

5. **The information-theoretic layer.** The thought experiment's unique asset — continuous behavioral streams at multiple temporal resolutions — enables analyses that standard personality measurement cannot: entropy rate of behavioral sequences, mutual information between successive behavioral states, compression complexity as a measure of behavioral predictability. These metrics could reveal aspects of individual differences invisible to traditional mean-level personality measurement.

6. **Practical implications for assessment design.** The robot's empirical ranking of contexts by individual-differentiating power is directly relevant to the BESSI-B project. Which situational contexts maximize the behavioral signal for each personality dimension? The chatbot assessment environment is itself a context that shapes what it measures.

