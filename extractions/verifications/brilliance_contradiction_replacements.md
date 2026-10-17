# BRILLIANCE Theory: Contradiction Replacement Analysis

**Date:** 2026-03-29
**Purpose:** For each study that contradicts a BRILLIANCE claim, document whether the authors propose a replacement framework for the contradicted idea, or simply report disconfirming evidence without offering an alternative.
**Focus:** Introduction and Discussion sections of each paper.

---

## Summary Scorecard

| # | Contradiction | Replacement proposed? | Type |
|---|---|---|---|
| 1, 8 | Dopamine dominant / ADHD-ASD dopaminergic | **No** — points toward GABA but no framework | Empirical redirect |
| 2, 10 | NE as monolithic alerting | **Yes** (Grimm: dual-mode gain; Breton-Provencher: dual-function + modularity) | Explicit models |
| 3 | MD thalamus D2/GRIK4 labels | **Implicit supersession** (Lam: uncertainty decomposition replaces gain-control labels) | Conceptual evolution |
| 4 | Amygdala = threat | **No** — devastating mechanism but no named alternative | Empirical only |
| 5 | ACC = unitary node | **No** — multi-ensemble empirics, no named framework | Empirical only |
| 6 | Agreeableness = threat x orienting | **Yes** — integrated value computation via RL | Explicit mechanism |
| 7 | ASD = single imbalance | **No** — "fractionate" but no architecture proposed | Empirical demolition |
| 9 | Astrocyte omission | **No** — causal necessity shown, integration left to others | Contradicted by omission |
| 10 | ANT premise | **Yes** (Laszlovszky: Model C for ACh); **Partial** (Gustavson: HiTOP endorsed) | Mixed |
| 11 | ADHD = channel dominance | **Yes** (Feldman: drift rate); **No** (Karr: delayed maturation topology) | Mixed |
| 12 | Psychedelics dissociation | **No** — additive mechanism, no psychedelic discussion | Empirical nuance |
| 13 | Architecture intact under stress | **No** — three papers, convergent structural damage, no named replacement | Empirical convergence |

**Bottom line:** Of 13 contradictions, only 4 have explicit replacement mechanisms in the papers themselves (2, 6, 10-Laszlovszky, 11-Feldman). One more has an implicit supersession from within the same lab (3). The remaining 8 provide strong disconfirming evidence but leave the theoretical architecture-building to others.

---

## 1 & 8: Dopamine as Dominant Neuromodulator for EF / ADHD-ASD Overlap "in Dopaminergic Pathways"

**Paper:** Hatoum, A. S., et al. (2023). Genome-wide association study shows that executive functioning is influenced by GABAergic processes. *Biological Psychiatry*, 93(1), 59-70.

**Replacement proposed:** No.

Hatoum et al. provide powerful disconfirming evidence — GABA and fast synaptic transmission, not dopamine, underlie heritable individual differences in Common EF (N = 427,037) — but do not build an alternative theoretical model. They name the *what* (GABAergic pathways, E/I balance) but not the *how* (no mechanistic model of how GABA variation translates into better or worse executive control at the cognitive level).

**Key evidence against dopamine dominance:**

> "Our results suggest that genetic influences on cEF involve variation within fast ionotropic and synaptic pathways, in particular GABAergic pathways, rather than the commonly studied metabotropic and dopaminergic pathways." (Discussion, p. 67)

> "We found little evidence that dopaminergic processes genetically relate to individual differences in cEF, outside the *DRD2* gene; other monoamine (dopamine and serotonin) candidate genes were not associated with cEF despite very high power to detect previously reported associations." (Discussion, p. 67-68)

The gene-set analysis section header is explicit: "Genetic Associations With cEF Do Not Strongly Implicate Dopaminergic Pathways or Replicate Candidate Genes." COMT val/met (rs4680), the most-studied candidate gene polymorphism for EFs, was not significant at the genome-wide level.

**Closest approach to a replacement mechanism:**

> "Disruption to the excitatory/inhibitory neurotransmission balance related to GABAergic processes may explain such transdiagnostic associations with cognitive deficits, particularly EFs." (Discussion, p. 68)

This is a single sentence, not a developed framework.

**Nuance on dopamine's remaining role:**
- DRD2 survives as a genome-wide significant hit, though with much smaller effect sizes than previously reported.
- Dopaminergic gene sets reached nominal significance but showed "the weakest evidence for association among hypothesized pathways."
- The claim is specifically that dopamine is not the primary molecular substrate of *heritable individual differences* in common EF. Dopamine could still matter for within-person EF modulation (pharmacological effects, task-state dynamics) without being the major source of between-person genetic variance.
- The theoretical distinction is between slow neuromodulatory processes (dopamine, serotonin) and fast ionotropic/synaptic processes (GABA, glutamate/NMDA). The latter are genetically more important for cEF.

---

## 2 & 10 (partial): NE as Monolithic "Alerting" System

Three papers, progressively stronger on replacement.

### Ghosh & Maunsell (2024)

**Paper:** Ghosh, S., & Maunsell, J. H. R. (2024). LC norepinephrine contributes to visual-spatial attention. *Neuron*, 112, 2231-2240.

**Replacement proposed:** Partial — adds spatially selective perceptual sensitivity as a distinct LC function; invokes the existing GANE model.

LC-NE selectively enhances perceptual sensitivity to attended stimuli in a hemisphere-specific way — not broadcast arousal. Optogenetic activation of LC improves perceptual d' only contralaterally.

> "We have shown that NE neuromodulation selectively contributes to the perceptual sensitivity of behaviorally relevant stimuli, a crucial neuronal signature of selective attention." (Discussion)

> "Collectively, the results identify a distinct causal contribution of NE activity in mediating task-relevant selective sensory processing distinct from attention orienting and nonselective arousal." (Discussion)

They invoke the **GANE model** (Glutamate Amplifies Noradrenergic Effects): high glutamate release in response to the attended stimulus creates a localized NE hotspot via positive feedback between glutamate and NE release. Alerting/arousal is acknowledged as a real function of LC-NE but shown to be *separable from* the selective attention function. Intertrial LC spike rates did not differ by attentional hemifield — "contrary to what would have been predicted by hemisphere-specific arousal."

### Grimm et al. (2024)

**Paper:** Grimm, C., et al. (2024). Tonic and burst-like LC stimulation distinctly shift network activity. *Nature Neuroscience*, 27, 2167-2177.

**Replacement proposed:** Yes — LC-NA as a **"dynamic gain controller along a cortical hierarchy."**

Same LC nucleus, same stimulation intensity, but tonic vs. burst firing produce qualitatively different brain-wide network reconfigurations:

> "Our findings suggest that tonic and burst-like LC firing could act as dynamic gain controllers along this hierarchical axis, dynamically reassigning the brain's resources according to situational demands." (Discussion)

> "Burst-like firing -- typically related to salient stimuli that require sensory reorientation -- preferentially activates 'lower-level' sensory processing, whereas tonic firing -- related to sustained attention and task engagement -- activates 'higher regions' tasked with more complex and abstract information processing." (Discussion)

Alerting is not discarded but **reframed as one mode** within a dual-mode system. Burst-like firing maps onto alertness/reorienting; tonic firing maps onto sustained attention and transmodal recruitment. Even the burst/alerting mode does not produce uniform global arousal — it specifically recruits sensory cortex while having different effects on transmodal regions. The system is a **mode switch** that reconfigures which parts of the cortical hierarchy are activated, not a dial between low and high arousal.

### Breton-Provencher et al. (2022)

**Paper:** Breton-Provencher, V., et al. (2022). Spatiotemporal dynamics of noradrenaline during learned behaviour. *Nature*, 606, 732-738.

**Replacement proposed:** Yes — LC-NA performs **two concurrently encoded functions** (task execution and reinforcement encoding) via **modular, spatially targeted outputs.**

> "Here, using a learned behaviour dependent on LC-NA activity, we demonstrate two concurrently encoded functions for the LC-NA system: task execution and performance optimization." (Discussion)

> "LC-NA neurons form distinct groups with respect to encoding of action execution and positive reinforcement, whereas the negative reinforcement signal is globally encoded in LC-NA neurons." (Discussion)

Pre-movement NE release is spatially targeted to motor regions (task execution); negative reinforcement/punishment produces broad neuromodulation (performance optimization). Single LC neurons sort into functionally distinct clusters with different cortical targets.

Arousal is explicitly dismissed as an explanation: "we measured the effect on behavioural performance as a function of pupil constriction and found no clear relationship, suggesting that the effects of LC-NA activity on task execution are independent of changes in arousal levels."

---

## 3: MD Thalamus "D2 for Signal Amplification, GRIK4 for Noise Filtering"

### Mukherjee et al. (2021)

**Paper:** Mukherjee, A., et al. (2021). Thalamic circuits for independent control of prefrontal signal and noise. *Nature*, 600, 100-104.

**Replacement proposed:** N/A — this paper *is* the two-cell-type model; it establishes rather than replaces the framework.

MD contains two genetically distinct projection neuron populations:
- **MD_D2** neurons target VIP+ interneurons in PFC and amplify prefrontal signals when task inputs are sparse (low signal).
- **MD_GRIK4** neurons target PV+ interneurons in PFC and suppress prefrontal noise when inputs are dense but conflicting (high noise).

> "These different neural signals are carried by two genetically distinct thalamic projections." (Discussion, p. 103)

### Lam et al. (2025)

**Paper:** Lam, N. H., et al. (2025). Prefrontal transthalamic uncertainty processing drives flexible switching. *Nature*, 637, 127-136.

**Replacement proposed:** Implicit supersession, not explicit rejection.

Same lab (Halassa), overlapping authors, four years later. Moves to an entirely different level of description:

- **From cell-type identity to functional selectivity:** Mukherjee defined MD populations by genetic markers (D2 vs. GRIK4). Lam defines them by what task variable they encode (conflict vs. context). The genetic labels disappear.
- **From gain control to uncertainty decomposition:** Mukherjee framed MD as performing signal amplification and noise suppression. Lam frames MD as decomposing mixed cortical representations into separated uncertainty estimates (cueing uncertainty vs. rule uncertainty).
- **From single-area modulation to inter-areal routing:** Mukherjee studied MD's effect on a single cortical area. Lam adds ACC and shows MD serves as a relay in an ACC → MD → PFC transthalamic pathway — "enabling cortico-cortical communication through a low-dimensional bottleneck."

> "A major conclusion from our work is that in contrast to frontal cortical areas, the MD thalamus shows a low-dimensional and demixed representation of task variables... the notion that the thalamus may demix cortical task variables is novel and has multiple implications on how cognitive tasks are neurally implemented." (Discussion, p. 9)

The underlying cell types likely still exist, but the functional labels ("signal amplification" and "noise filtering") have been superseded by "uncertainty decomposition" and "transthalamic routing."

---

## 4: Amygdala Assigned to ES/Alerting/Threat-Sensitivity

**Paper:** Li, H., et al. (2022). Neurotensin orchestrates valence assignment in the amygdala. *Nature*, 608, 586-592.

**Replacement proposed:** No.

The authors never name or critique a "threat-detector" model. They take the BLA's dual-valence nature as established background and pose a mechanistic question: how do the same BLA neurons get routed toward reward vs. punishment? Answer: neurotensin (NT) from PVT acts as a concentration-dependent gate — high NT promotes reward encoding, low/decreased NT promotes punishment encoding.

> "During associative learning, the basolateral complex of the amygdala (BLA) forms associations with positive or negative outcomes." (Introduction, p. 1)

The BLA is presented as a *dual-valence associative learning structure* from the opening sentence — not a threat detector. Fear conditioning appears as one of two symmetric assays throughout, not as the amygdala's defining function.

Key implicit challenges to "threat structure" framing:
- The **same neurons** can encode either valence, depending on neuropeptide context.
- NT knockout doesn't just impair fear responses — it abolishes the preference for *active* behavioral strategies in both reward and punishment contexts.
- Dopamine "codes for 'absolute value'" (necessary for both reward and punishment learning), while NT is the signal that determines *which* valence is encoded.

The empirical ammunition is extremely strong, but the theoretical bridge from mechanism to framework is left for others.

---

## 5: ACC as Unitary SN/Alerting Node

**Paper:** Zhang, M., et al. (2024). Cortical regulation of helping behaviour towards others in pain. *Nature*, 626, 136-144.

**Replacement proposed:** No.

The authors never mention "salience network" or any unitary ACC theory. Their contribution is empirical: ACC contains **separable neural ensembles** for categorically different prosocial responses.

- Allolicking-activated and allogrooming-activated neurons are "largely non-overlapping" (~15-17% overlap).
- ACC differentiates input states (local pain vs. general stress) AND maps them to different outputs via separable population codes.
- ACC plays a **causal regulatory role** (DREADDs/optogenetics), not just detection.

> "Here our data demonstrate a distinct role of the ACC in regulating both targeted allolicking and general allogrooming towards others in pain, beyond the initial perception of others' state." (Discussion, p. 8)

Their summary schematic (Fig. 5r) depicts ACC as containing two parallel processing streams — local-pain-to-targeted-helping and general-stress-to-comforting — but this is presented as an empirical conclusion, not as a named competing model.

---

## 6: Agreeableness Mechanism — "Detect Social Signals (E) and Weight Them as Urgent/Threatening (ES)"

**Paper:** Rhoads, S. A., et al. (2025). Neurocomputational basis of learning when choices simultaneously affect both oneself and others. *Nature Communications*, 16, 9350.

**Replacement proposed:** Yes — **integrated value computation via reinforcement learning.**

This is the strongest replacement of the set. The mechanism:

- People maintain a **single expected value (Q) per choice** that integrates both self-relevant and other-relevant outcome information.
- This value is updated **asymmetrically** through four distinct learning rates: self x other x positive x negative prediction errors.
- Prosocial individuals weight other-relevant prediction errors more heavily; antisocial individuals (high psychopathy) show blunted learning rates for other-relevant PEs.
- The whole system runs on standard reward-prediction-error machinery in ventral striatum, sgACC, pgACC, amygdala, and anterior insula.

> "People integrate self- and other-relevant information during learning to guide future prosocial behaviors, suggesting that the brain combines self- and other-regarding information into a common valuation signal, rather than maintaining entirely separate valuation systems." (Discussion, p. 7-8)

The integrated model was tested *against* a "value simulation" model (separate value functions for self and other) and won decisively across all samples and model comparison metrics.

Threat-sensitivity plays no role as a separate mechanism. Valence asymmetry (positive vs. negative PEs) is the closest analogue, but it is embedded within reward learning, not a separate channel. The ventral striatum, not a threat-detection circuit, is the core engine.

---

## 7: ASD as Single "Alerting Dominates" Imbalance

**Paper:** Warrier, V., et al. (2019). Social and non-social autism symptoms and trait domains are genetically dissociable. *Communications Biology*, 2, 328.

**Replacement proposed:** No.

The authors forcefully argue unitary models are inadequate but stop at the empirical demonstration. Polygenic scores for systemizing predict restricted/repetitive behaviors but show *zero* association with ADOS-G social/communication scores — a clean within-person genetic dissociation.

> "Our results confirm the need to rethink our understanding of autism as existing along a single dimension." (Discussion, p. 7)

They endorse the "fractionable autism triad" concept (Happe & Ronald, 2008) as confirmed and extended by their molecular-genetic evidence. They note the dissociability may explain why autism GWAS have identified fewer loci than comparably-powered psychiatric GWAS — signal attenuation from lumping genetically distinct phenotypes. Different domains also have different psychiatric comorbidity profiles: social traits share genetics with schizophrenia and depression; systemizing/non-social traits do not.

No replacement architecture is proposed. The what-comes-next is left to future work.

---

## 9: Astrocyte Omission from Circuit Architecture

**Paper:** Mederos, S., et al. (2021). GABAergic signaling to astrocytes in the prefrontal cortex sustains goal-directed behaviors. *Nature Neuroscience*, 24, 82-92.

**Replacement proposed:** No — causal necessity demonstrated, but theoretical integration left to others.

The specific pathway: PV interneuron GABA → astrocyte GABA_B receptor → Ca²⁺ → glutamate release → mGluR1 activation at GABAergic terminals → enhanced IPSCs onto pyramidal cells.

> "While neurons have been associated with encoding task-specific responses, astrocytes have been largely ignored for high-demand computation tasks." (Discussion)

Critically, **boosting PV interneuron activity directly (via ChR2) was not sufficient to rescue the cognitive deficits** caused by astrocyte GABA_B receptor ablation. The neuronal pathway alone cannot compensate for the loss of the astrocytic pathway. Removing GABA_B receptors from astrocytes alone — leaving all neurons genetically unaltered — causes "widespread collapse in the neural coding critical for working memory and decision-making."

The authors describe astrocytes as "cellular checkpoints for tuning the signal-to-noise ratio" but do not propose a revised theoretical architecture for EF circuits with astrocytes included. The "contradicted by omission" label is apt: the omission is of a cell type whose absence causes collapse of the very computations the theory claims to explain.

---

## 10: ANT x Personality Predictions — Premise Contradicted

### Laszlovszky et al. (2020)

**Paper:** Laszlovszky, T., et al. (2020). Distinct synchronization, cortical coupling and behavioral function of two basal forebrain cholinergic neuron types. *Nature Neuroscience*, 23, 992-1003.

**Replacement proposed:** Yes — **Model C** (a hybrid of prior competing models).

They test three models of cholinergic heterogeneity:
- Model A ("different types"): Different BFCN types underlie phasic vs. tonic effects.
- Model B ("different modes"): Same neurons, different firing modes control temporal dynamics.
- **Model C (their proposal):** Two cell types (BFCN_BURST and BFCN_REG) *plus* state-dependent mode-switching within the bursting type.

> "Our result suggests a third, more complex scenario underlying tonic and phasic cholinergic effects. We propose that there are two basal forebrain cholinergic cell types... While BFCN_BURST and BFCN_REG are two separate cell types, the firing mode seems crucial to regulating slow and fast cholinergic modulation." (Discussion, p. 9)

Key functional dissociation:
- BFCN_BURST predicts response *occurrence* (arousal/engagement) — analogous to alerting.
- BFCN_REG predicts response *accuracy* (selective detection) — overlapping with orienting or executive functions.
- The two types are anatomically segregated along the anterior-posterior axis, meaning different cortical regions receive different cholinergic "messages."

Implication: ACh cannot be cleanly assigned to "orienting." The cholinergic system internally contains functionally distinct subsystems that cut across what the ANT framework distributes across separate neuromodulator systems.

### Gustavson et al. (2024)

**Paper:** Gustavson, D. E., et al. (2024). Executive function and impulsivity predict distinct genetic variance in internalizing problems, externalizing problems, thought disorders, and compulsive disorders. *Clinical Psychological Science*, 12(5), 865-881.

**Replacement proposed:** Partial — empirical demolition of the unified construct; HiTOP endorsed as the appropriate framework.

Task-based EF and questionnaire-based impulsivity are genetically near-unrelated (rg = 0.13). Urgency-specific impulsivity is completely uncorrelated with EF (rg = 0.00). Despite both being called "attention/self-regulation," they predict *different* psychopathology spectra: EF most strongly predicts thought disorders; impulsivity most strongly predicts externalizing.

> "Executive function and impulsivity may simply reflect separable domains of self-control." (Introduction, p. 3)

They directly critique RDoC's classification of EF and impulsivity within one "cognitive control" system: "because these measures clearly capture different sets of genetic risk factors that are relevant to psychopathology and related traits, it will be important to further explore both domains."

For the ANT specifically: the "executive attention" component (operationalized with conflict tasks) captures something genetically unrelated to the self-regulation difficulties that drive clinical impairment in ADHD and externalizing psychopathology.

---

## 11: ADHD as "Orienting Dominates, Alerting Can't Sustain Access"

### Feldman & Huang-Pollock (2021)

**Paper:** Feldman, J. S., & Huang-Pollock, C. (2021). Slow drift rate predicts ADHD symptomology over and above executive dysfunction. *Child Neuropsychology*, 27(6), 834-855.

**Replacement proposed:** Yes — **slow drift rate** (evidence accumulation efficiency).

When drift rate and traditional EF metrics are entered simultaneously, drift rate continues to predict ADHD (beta = -.441, p = .030) while EF drops to nonsignificance (beta = -.090, p = .642). EF adds nothing once drift rate is accounted for.

> "The DM and the drift rate parameter offer a hitherto absent method of explaining cognitive deficits in ADHD in a clear, consistent, and mechanistically specific way." (Discussion)

> "The disappearance of an association between ADHD and the latent EF metric factor suggest that slow drift rate is both a more parsimonious and psychologically meaningful explanation for cognitive dysfunction in the disorder." (Conclusion)

The deficit is domain-general and task-nonspecific — slow drift rate across perceptual discrimination AND mental rotation tasks. This implicitly undermines channel-dominance models: the core deficit is at a lower computational level (evidence accumulation efficiency) that would produce deficits across any task requiring speeded decisions regardless of which attention network is engaged. The authors also explicitly critique the "homunculus" framing of executive control.

### Karr et al. (2023)

**Paper:** Karr, J. E., et al. (2023). A network analysis of executive functions in children and adolescents with and without ADHD. *Child Psychiatry and Human Development*, 55(6), 1600-1610.

**Replacement proposed:** No single mechanism — a structural/organizational account aligned with **delayed maturation.**

Children with ADHD showed trivially small performance deficits (d = 0.05-0.11) but different inter-ability relationships: shifting has less centrality, inhibition serves as the integrating hub — a pattern that mirrors younger typically developing children.

> "The current findings indicate that ADHD is associated with different relationships between executive functions rather than an overall reduction in executive function test performances." (Discussion)

> "Children with ADHD may experience delays in cortical development, most prominently in prefrontal regions, which could explain why their network, with lower shifting centrality, reflects a comparably less mature network structure." (Discussion)

They propose EFs as a **dynamic system** of interactive abilities: "If executive functions reflect a dynamic system, it may be why ADHD, which involves frontoparietal dysfunction, is characterized by intraindividual variability, but does not always involve a reduction in performances on executive function tests." The ADHD network is not "broken" or "imbalanced" — it looks like a younger version of the same system.

---

## 12: Psychedelics — "Self-Model Is Primary Target, EF Somewhat Disrupted"

**Paper:** Haarsma, J., et al. (2023). Expectation cues and false percepts generate stimulus-specific activity in distinct layers of early visual cortex. *Journal of Neuroscience*, 43(41), 6898-6907.

**Replacement proposed:** No.

The authors explicitly state their findings "should not be taken as evidence against the theory that top-down perceptual expectations can play an important part in generating hallucinations." Their contribution is additive: false percepts arise in **middle (feedforward/input) cortical layers**, not deep (prediction/feedback) layers.

> "The core finding here -- that orientation-specific activity in the middle layers of V2 can lead participants to perceive a grating that was not actually presented -- has important implications for the field of hallucination research... it suggests that false percepts can arise through activity in the input layers in the absence of top-down stimulus templates." (Discussion, p. 7954)

They cite **"circular inference" / runaway overcounting models** (Deneve & Jardri, 2016) as consistent — weak sensory signals trigger perceptual hypotheses that get counted as evidence in ascending loops without requiring top-down initiation.

They distinguish between expectations about stimulus *presence* vs. stimulus *content*, suggesting these may operate through different neural processes. They speculate that for expectation-induced hallucinations, "feedback signals may need to override activity in the middle input layers."

**The paper contains zero discussion of psychedelics.** The clinical implications are limited to schizophrenia, Charles Bonnet syndrome, and Parkinson's disease. The connection to psychedelic effects on cognition must be constructed externally.

---

## 13: "Workspace Closure" (Withdrawal) as Pure Dynamics, Architecture Intact

Three papers, convergent evidence, no named replacement frameworks.

### Van der Meulen et al. (2022)

**Paper:** Van der Meulen, M., et al. (2022). Association between use of systemic and inhaled glucocorticoids and changes in brain volume and white matter microstructure. *BMJ Open*, 12, e062446.

**Replacement proposed:** No.

Glucocorticoid exposure is associated with widespread white matter microstructural degradation — reduced fractional anisotropy (FA) and increased mean diffusivity (MD), both markers of microstructural *architecture*. The mechanism runs through oligodendrocyte damage:

> "Glucocorticoids have important impact on white matter, and non-neuronal cells such as oligodendrocytes are very sensitive to glucocorticoids. Animal studies have shown that glucocorticoid exposure inhibits proliferation of oligodendrocyte progenitor cells... and induce changes in the expression of myelin basic protein." (Discussion)

**On reversibility:** In Cushing disease patients, "some of these effects were detected even after ten years of biochemical remission." Evidence for recovery is mixed and incomplete.

### Horchar & Wohleb (2019)

**Paper:** Horchar, M. J., & Wohleb, E. S. (2019). Glucocorticoid receptor antagonism prevents microglia-mediated dendritic spine loss in PFC after chronic stress. *Brain, Behavior, and Immunity*, 81, 329-340.

**Replacement proposed:** No named framework, but they articulate a full mechanistic cascade.

The pathway: chronic stress → glucocorticoid receptor activation → neuronal CSF1 upregulation → microglial activation and morphological change → complement pathway (C1q/C3/CD11b) activation → **phagocytic engulfment of synaptic elements** → dendritic spine loss → PFC dysfunction.

> "GFP+ inclusions co-localized with the lysosomal marker CD68, indicating that these neuronal elements are phagocytosed by resident microglia." (Results)

This is the most vivid demonstration: microglia literally eat PFC pyramidal neuron dendritic spines. The architecture is not "intact" — it is being physically dismantled by immune cells.

They explicitly frame a shift from viewing stress effects as cell-internal "software" changes to an intercellular remodeling process: prior studies "attributed these chronic stress-induced molecular and cellular adaptations to intrinsic, cell-autonomous mechanisms... In contrast, seminal studies have uncovered dynamic interactions between neurons and microglia that modulate neuroplasticity."

**On reversibility:** RU486 administered concurrently *prevents* the damage, but they do not test whether established damage can be reversed. Spine phagocytosis occurs within 15 min - 2 hours based on ex vivo imaging. Once spines are phagocytosed and digested, they must be rebuilt de novo.

### Feng et al. (2025)

**Paper:** Feng, Y., et al. (2025). Association between allostatic load and accelerated white matter brain aging. *American Journal of Epidemiology*, 194(8), 2376-2384.

**Replacement proposed:** No — uses McEwen's existing allostatic load model as theoretical scaffold.

Allostatic load accelerates biological aging of white matter across all 39 measured tracts. Mendelian randomization supports a *causal* relationship: 0.33 years of additional white matter aging per allostatic load unit.

> "Chronic stress precipitates a cascade of endocrine disruptions, causing sustained elevation of cortisol -- a glucocorticoid linked to deleterious effects on cerebral architecture and functionality, manifesting as compromised white matter integrity." (Discussion)

> "Structural changes in white matter can compromise its fundamental role in facilitating signal transmission between brain regions, hence indicating the changes in white matter may be a mediator between chronic stress and cognitive function and emotion regulation." (Discussion)

**On reversibility:** The framing is starkly preventive. The paper references "irreversible brain damage" and frames its purpose as enabling early intervention *before* permanent structural damage occurs.

### Cross-paper synthesis (Contradiction 13)

All three papers converge: chronic stress does not leave brain architecture intact. Structural damage operates at multiple scales:

- **Cellular/synaptic level** (Horchar & Wohleb): Microglia physically phagocytose dendritic spines on PFC pyramidal neurons.
- **White matter microstructure** (Van der Meulen): Glucocorticoids damage oligodendrocytes, disrupt myelination, reduce FA.
- **Whole-brain aging** (Feng): Cumulative stress causally accelerates biological aging of white matter across all measured tracts.

Reversibility evidence is sobering: Van der Meulen shows effects persisting a decade after glucocorticoid normalization; Horchar & Wohleb show prevention is possible but do not demonstrate reversal of established damage; Feng explicitly references "irreversible brain damage."
