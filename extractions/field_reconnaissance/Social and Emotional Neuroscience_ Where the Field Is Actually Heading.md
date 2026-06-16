# **Social and Emotional Neuroscience: Where the Field Is Actually Heading**

The dominant momentum in social and emotional neuroscience is **computational decomposition** — breaking apart monolithic constructs like empathy, social cognition, and prosocial behavior into formally specified, individually measurable computational parameters. This shift, well underway since roughly 2019, has changed what counts as a "phenotype" in social neuroscience from a questionnaire score or an fMRI blob to a set of latent model parameters extracted from structured behavioral tasks. Simultaneously, circuit neuroscience in animal models has shattered the one-region-one-function view of social-emotional brain organization, revealing neuropeptide-gated, projection-specific, and cell-type-specific mechanisms that operate far below the resolution of human neuroimaging. The genetic architecture of social-emotional traits remains the weakest link: **no major new GWAS of a specific social-cognitive phenotype has been published since 2018**, and current polygenic scores for empathy or social cognition explain functionally zero variance. The critical bottleneck is not genotyping power — it is that large genotyped cohorts lack the fine-grained social-cognitive phenotyping that computational modeling now makes possible. The field's near-future trajectory is therefore clear: scaling computational phenotyping to biobank-sized samples, while integrating circuit-level insights from animal work through translational paradigms.

What follows covers five sub-areas with 12 papers total, each selected for novelty, influence, and the specific contribution it makes to the field's direction. A standalone lab-mapping section closes the report.

---

## **1\. New phenotypes: social cognition is being computationally decomposed**

The most consequential shift in this sub-area is the move from measuring social cognition through self-report scales or accuracy scores toward extracting **individual-level computational parameters** from structured social learning tasks. "Empathy" or "theory of mind" as measured by a single score is being replaced by multi-dimensional vectors of parameters — learning rates, precision terms, reference points — that describe *how* a person processes social information, not just how well.

### **Paper 1**

**Rhoads, S. A., Gan, L., Berluti, K., O'Connell, K., Cutler, J., Lockwood, P. L., & Marsh, A. A. (2025). Neurocomputational basis of learning when choices simultaneously affect both oneself and others. *Nature Communications*, 16, 9350\.** DOI: [10.1038/s41467-025-64424-9](https://doi.org/10.1038/s41467-025-64424-9)

* **Design:** Computational \+ neuroimaging (3 pre-registered behavioral studies \+ 1 fMRI study)  
* **Sample:** N \> 200 across behavioral studies; \~30–40 in fMRI component. No genetic data.  
* **What it establishes:** A **four-dimensional computational phenotype** of prosocial/antisocial learning, decomposed along target (self vs. other) × valence (positive vs. negative). Individuals have distinct, asymmetric learning rates for self-positive, self-negative, other-positive, and other-negative prediction errors — and these are neurally dissociable.  
* **Why it matters:** Before this work, "prosociality" was measured as one number. Now it can be decomposed into four independent computational dimensions, each with its own neural signature and its own relationship to trait measures like psychopathic meanness. This creates measurable individual-difference parameters suitable for scaling to genetic studies.

This paper builds directly on Lockwood et al.'s (2016, PNAS) foundational finding that people learn differently for self-benefiting versus other-benefiting outcomes. The key advance is that real-world prosocial and antisocial decisions almost always involve **joint outcomes** — helping someone costs you, harming someone benefits you. Rhoads et al. built a task that captures all four cells of this matrix and fitted computational models to show that an integrated value framework (where self and other outcomes combine with asymmetric weights) outperforms a simulation model (where people imagine what others want). The integrated model resolves a longstanding debate in the field by demonstrating that prosocial behavior operates through direct value computation, not perspective-taking simulation. Ventral striatum, subgenual ACC, insula, and amygdala each encoded distinct components of the 2×2 structure.

### **Paper 2**

**Schurr, R., Reznik, D., Hillman, H., Bhui, R., & Gershman, S. J. (2024). Dynamic computational phenotyping of human cognition. *Nature Human Behaviour*, 8(5), 917–931.** DOI: [10.1038/s41562-024-01814-x](https://doi.org/10.1038/s41562-024-01814-x)

* **Design:** Longitudinal / methods-validation (12-week intensive study, 7 cognitive tasks measured weekly, concurrent mood/affect tracking)  
* **Sample:** \~50–100 participants (justified by \~84+ data points per person). No genetic data; weekly affective state measures.  
* **What it establishes:** Computational phenotype parameters are not fixed traits — they **fluctuate systematically with affective state**. The paper provides a hierarchical Bayesian framework to separate random noise, practice effects, and mood-driven state effects on model parameters.  
* **Why it matters:** Every computational phenotyping study in social neuroscience assumes parameters reflect stable individual differences. This paper shows that assumption is wrong, and provides the statistical machinery to fix it.

The implications for social-emotional neuroscience are direct and serious. If learning rate or precision parameters shift with mood (which this paper demonstrates), then any single-session extraction of a "social computational phenotype" captures an unknowable mixture of trait and state. The field's recurring problem of poor test-retest reliability for computational parameters is reframed: **low ICC values are not evidence that computational phenotyping fails — they are evidence that it captures real, structured variability including affective modulation.** The practical consequence is that future social-cognitive phenotyping must become longitudinal and mood-aware. Gershman's lab, one of the most influential in computational cognitive science, has effectively issued a methodological mandate for the entire field.

### **Paper 3**

**Frolichs, K. M. M., Rosenblau, G., & Korn, C. W. (2022). Incorporating social knowledge structures into computational models. *Nature Communications*, 13, 6205\.** DOI: [10.1038/s41467-022-33418-2](https://doi.org/10.1038/s41467-022-33418-2)

* **Design:** Computational / methods-validation (5 behavioral experiments)  
* **Sample:** Total N ≈ 150–200 across 5 experiments. No genetic data.  
* **What it establishes:** Two novel formalized constructs — **"granularity"** (how fine-grained one's model of personality trait structure is during social learning) and **"reference points"** (implicit prototypes against which new individuals are compared) — that can be extracted as tunable parameters from social learning tasks.  
* **Why it matters:** Prior computational models of social learning treated it as equivalent to non-social reward learning. This paper shows that people bring hierarchically organized prior knowledge to social encounters, and that individual variation in how they deploy this knowledge constitutes a new measurable phenotype dimension.

The paper extends standard Rescorla-Wagner learning models with social knowledge structure parameters, creating a class of hybrid models that outperform standard reinforcement learning. The "granularity" parameter is particularly promising as a clinical marker: individuals who learn about others at a coarse level (Big-5 factors) versus a fine level (individual trait correlations) may differ systematically in social-cognitive strategy, with plausible relevance to autism and personality disorders.

---

## **2\. Measurement breakthroughs are concentrated in computational modeling**

The strongest measurement advances are in **generative computational modeling** of social inference and emotion attribution. Hyperscanning has produced its first prospective predictive validity result, but remains methodologically immature relative to computational approaches. Digital phenotyping of social behavior via smartphones is still at the feasibility stage.

### **Paper 4**

**Houlihan, S. D., Kleiman-Weiner, M., Hewitt, L. B., Tenenbaum, J. B., & Saxe, R. (2023). Emotion prediction as computation over a generative theory of mind. *Philosophical Transactions of the Royal Society A*, 381(2251), 20220047\.** DOI: [10.1098/rsta.2022.0047](https://doi.org/10.1098/rsta.2022.0047)

* **Design:** Computational \+ empirical validation (multiple behavioral experiments)  
* **Sample:** N \= 554 observers contributing 1,108 judgments. No genetic data.  
* **What it establishes:** A fully generative computational model that **predicts the specific emotions observers will attribute to others** across 20 distinct emotion categories in complex social situations, matching human quantitative predictions without requiring intermediate human ratings.  
* **Why it matters:** For the first time, emotion attribution can be formally decomposed into interpretable computational components (inferred beliefs, inferred preferences, computed appraisals, emotion concept mappings), making previously intractable questions — *why* do people predict someone will feel guilt rather than shame? — formally testable.

This model integrates three modules: Bayesian inverse planning (inferring beliefs and preferences, including social preferences for equity and reputation), computed appraisals, and learned emotion concept functions. The "situation-computable" nature of the model — it operates over the same information given to human observers, with no human-rated appraisal inputs — is the critical advance over prior appraisal theory work, which always required a human in the loop. The model adjusts to personalizing information about social actors, capturing how context modulates emotion attribution. Code and data are openly available (OSF: https://osf.io/yhwqn). This won the 2023 Best Dissertation in Affective Science Award.

### **Paper 5**

**Barnby, J. M., Bell, V., Deeley, Q., Mehta, M. A., & Moutoussis, M. (2024). D2/D3 dopamine supports the precision of mental state inferences and self-relevance of joint social outcomes. *Nature Mental Health*, 2(5), 562–573.** DOI: [10.1038/s44220-024-00220-6](https://doi.org/10.1038/s44220-024-00220-6)

* **Design:** Double-blind, placebo-controlled, within-subject pharmacological manipulation \+ computational modeling (methods-validation)  
* **Sample:** Small n (within-subject pharmacological design; standard for drug studies). No genetic data.  
* **What it establishes:** A computational model of intentional attribution in social games is **pharmacologically validated** — haloperidol (D2/D3 antagonist) selectively alters specific model parameters (belief precision, learning rate, self-relevance) in interpretable and dissociable ways.  
* **Why it matters:** This is the first demonstration that computational social inference models are sensitive to neurotransmitter manipulation, opening the door to using these models as biomarkers and connecting social cognition to neuropharmacology at the mechanistic level.

Previous work linking dopamine to social cognition used aggregate behavioral measures that could not distinguish which computational process was affected. Barnby et al. show that haloperidol specifically enhanced belief flexibility (increased the impact of partner behavior on inferences) and increased learning from recent encounters while reducing self-relevance. This selective parameter-level sensitivity means the model can serve as an assay for dopaminergic contributions to social cognition, with direct relevance for understanding paranoia and psychosis where social inference goes awry.

### **Paper 6**

**Mayo, O., Molcho-Fisher, Y., Avnor, Y., & Shamay-Tsoory, S. (2025). Interbrain synchrony and its potential role in modulating the impact of traumatic events. *Translational Psychiatry*, 16(1), 30\.** DOI: [10.1038/s41398-025-03770-0](https://doi.org/10.1038/s41398-025-03770-0)

* **Design:** Prospective longitudinal (hyperscanning data collected *before* real-world trauma; outcomes assessed afterward)  
* **Sample:** N \= 98 participants from prior fNIRS hyperscanning study. No genetic data.  
* **What it establishes:** Pre-existing interbrain synchrony during naturalistic conversation **prospectively predicts resilience** to real-world trauma (the October 7, 2023 attack in Israel), with greater spontaneous IBS associated with weaker trauma exposure–symptom associations.  
* **Why it matters:** This is the first hyperscanning result with prospective, real-world predictive validity, demonstrating that interbrain synchrony is not just a laboratory curiosity but a trait-like marker of social adaptation capacity with consequential mental health implications.

The hyperscanning literature has been plagued by small samples, irreplicable effects, and unclear real-world significance. This paper breaks through that impasse by leveraging a natural experiment: participants had been scanned during free conversation with a stranger before the October 7 attack, and the attack provided a uniform traumatic exposure against which IBS could be tested as a moderator. The prospective design rules out the possibility that trauma altered synchrony patterns. The effect was strongest in left pre-motor cortex (observation-execution system), consistent with action-perception coupling accounts of social resonance.

---

## **3\. Circuit specificity has overturned the one-region-one-function model**

This is the sub-area with the most unambiguous progress. Work in rodent models using optogenetics, calcium imaging, CRISPR, and genetically encoded sensors has demonstrated that **social and emotional processing is organized at the level of specific projections, neuropeptides, and cell types** — not brain regions. A landmark human single-neuron recording study confirms that this specificity extends to human social inference.

### **Paper 7**

**Li, H., Namburi, P., Olson, J. M., ... & Tye, K. M. (2022). Neurotensin orchestrates valence assignment in the amygdala. *Nature*, 608(7923), 586–592.** DOI: [10.1038/s41586-022-04964-y](https://doi.org/10.1038/s41586-022-04964-y)

* **Design:** Rodent (mouse); optogenetics, genetically encoded calcium and neurotensin sensors, CRISPR-mediated projection-specific gene knockout, fiber photometry  
* **Sample:** Multiple mouse cohorts, n \= 5–15 per experimental group across many manipulations. Genetic data: extensive (Cre-dependent viral targeting, CRISPR knockout of Nts gene in specific projections, GRAB-NT sensor).  
* **What it establishes:** A single neuropeptide — **neurotensin, released from a specific paraventricular thalamus→basolateral amygdala projection** — acts as a concentration-dependent switch for valence assignment. The same anatomical projection gates opposite behavioral outcomes (reward learning vs. punishment learning) depending on neurotensin concentration.  
* **Why it matters:** This directly demolishes "the amygdala does fear" by showing that whether individual BLA neurons encode reward or punishment depends on a neuropeptide signal from a specific thalamic input, not on a fixed regional identity.

The paper solves a fundamental timing puzzle: how does the amygdala route valence information correctly when synaptic plasticity operates on sub-second timescales but cue-outcome associations span seconds? The answer — neurotensin extends the temporal window of plasticity in a valence-specific manner — is a mechanism that no approach less specific than projection-targeted neuropeptide manipulation could reveal. CRISPR knockout of Nts specifically in PVT→BLA (leaving systemic neurotensin intact) blunted BLA dynamics and attenuated emotionally driven behavior for both positive and negative outcomes, confirming necessity. This is molecular-circuit specificity at its finest.

### **Paper 8**

**Zhang, M., Wu, Y. E., Jiang, M., & Hong, W. (2024). Cortical regulation of helping behaviour towards others in pain. *Nature*, 626(7997), 136–144.** DOI: [10.1038/s41586-023-06973-x](https://doi.org/10.1038/s41586-023-06973-x)

* **Design:** Rodent (mouse); microendoscopic calcium imaging at single-neuron resolution, optogenetics, chemogenetics  
* **Sample:** Multiple mouse cohorts across experiments. Genetic data: Cre-dependent viral constructs, cell-type-specific ACC manipulations.  
* **What it establishes:** Distinct population codes within the anterior cingulate cortex encode **targeted helping** (licking a conspecific's injury site) versus **general prosocial behavior** (allogrooming in response to emotional distress) — the same region implements categorically different prosocial responses through separable neural ensembles.  
* **Why it matters:** Decades of human fMRI have treated the ACC as a unitary "empathy region." This paper shows that the ACC distinguishes *type of prosocial response* at the single-neuron level, a specificity invisible to all prior methods. It also establishes a mouse model for studying prosocial helping, previously thought to require primate-level cognition.

The study used microendoscopic imaging to record individual ACC neurons during naturalistic social interactions, demonstrating that the population code for targeted helping is separable from general allogrooming. Optogenetic and chemogenetic manipulations confirmed bidirectional causality. This finding has direct implications for how we interpret human ACC activations during empathy tasks — they likely reflect a mixture of representationally distinct prosocial computations that are averaged together in BOLD signal.

### **Paper 9**

**Cao, R., Dubois, J., Mamelak, A. N., Adolphs, R., Wang, S., & Rutishauser, U. (2024). Domain-specific representation of social inference by neurons in the human amygdala and hippocampus. *Science Advances*, 10(49), eado6166.** DOI: [10.1126/sciadv.ado6166](https://doi.org/10.1126/sciadv.ado6166)

* **Design:** Human single-neuron recordings from neurosurgical epilepsy patients; depth electrode microelectrode recordings from medial temporal lobe and medial frontal cortex  
* **Sample:** 10–20 neurosurgical patients (standard and appropriate for intracranial recording). No genetic data.  
* **What it establishes:** Social inference in the human medial temporal lobe is **domain-specific at the single-neuron level** — separate neuronal subsets encode face-based versus hand-based social inference, and inference type is entangled with stimulus category specifically within the social domain.  
* **Why it matters:** This directly challenges the fMRI-derived view that "theory of mind" is a unitary, domain-general computation. At single-neuron resolution, what looks like a general "social inference" activation decomposes into categorically distinct computations. This paper is the closest existing bridge between rodent circuit work and human social cognitive neuroscience.

The architecture revealed is elegant: stimulus category itself (face vs. hand vs. scene) is represented in a task-general manner, but inference type becomes entangled with category specifically for social stimuli. This means the brain separates "what am I looking at" from "what inference am I making" — and the coupling of these two is a specifically social phenomenon. For conditions like autism, where social inference may be selectively impaired, this suggests that the deficit could be in the coupling mechanism rather than in inference or perception per se.

---

## **4\. Genetic architecture remains the field's weakest link**

This sub-area is **genuinely thin**, and this thinness is itself a major finding. No major new GWAS of empathy, emotion recognition, or theory of mind has been published since the Warrier and Baron-Cohen studies of 2017–2018. The bottleneck is not genotyping power — UK Biobank has **500,000** genotyped participants, 23andMe over a million — but that these cohorts lack fine-grained social-cognitive phenotyping. SNP-heritability for social-emotional traits sits at **3–11%**, and current polygenic scores explain approximately **0.01%** of variance in target phenotypes.

### **Paper 10**

**Bralten, J., Mota, N. R., Klemann, C. J. H. M., ... & Poelmans, G. (2021). Genetic underpinnings of sociability in the general population. *Neuropsychopharmacology*, 46(9), 1627–1634.** DOI: [10.1038/s41386-021-01044-z](https://doi.org/10.1038/s41386-021-01044-z)

* **Design:** GWAS with genetic correlation and polygenic risk score analyses  
* **Sample:** N \= 342,461 from UK Biobank, European ancestry, imputed to \~13 million SNPs. Genetic data: UK Biobank Axiom array.  
* **What it establishes:** The largest GWAS of a social-behavioral phenotype, identifying **18 genome-wide significant loci** for sociability (a composite of loneliness, social interaction frequency, social embarrassment, social activities). SNP-heritability is **6%**. Notable hits include *DRD2* (dopamine D2 receptor), *ARNTL* (circadian rhythm), and *ELAVL2* (neural RNA-binding protein).  
* **Why it matters:** It demonstrates that population variation in social engagement is highly polygenic with very small individual effects, genetically correlated with depression (rg \= 0.68) and autism (rg \= 0.27), but *not* with bipolar disorder or Alzheimer's — suggesting specificity in how social-behavioral genetic architecture maps onto psychopathology.

The *DRD2* finding is notable because it survived exclusion of all participants with psychiatric diagnoses, suggesting it reflects normative social functioning variation rather than clinical confounding. However, the phenotype is a relatively crude self-report composite about social engagement *frequency and preference* — not social-cognitive *ability*. The absence of tissue expression enrichment (including brain) limits biological interpretation. This paper illustrates both the promise and the ceiling of GWAS on social phenotypes constructed from existing biobank questionnaire items.

### **Paper 11**

**Warrier, V., Toro, R., Won, H., ... Baron-Cohen, S. (2019). Social and non-social autism symptoms and trait domains are genetically dissociable. *Communications Biology*, 2, 328\.** DOI: [10.1038/s42003-019-0558-4](https://doi.org/10.1038/s42003-019-0558-4)

* **Design:** GWAS of systemising \+ genetic correlation analyses with social traits \+ polygenic score analyses in clinical autism samples  
* **Sample:** GWAS N \= 51,564 from 23andMe; cross-referenced with EQ GWAS (N \= 46,861), Eyes Test GWAS (N \= 89,553), autism GWAS (N \= 46,350); PRS validation in \~5,000 autistic individuals from iPSYCH/PGC. Genetic data: Illumina arrays.  
* **What it establishes:** The social and non-social domains of autism have **distinct genetic architectures** — polygenic scores for systemising predict restricted/repetitive behaviors in autistic individuals but do *not* predict social difficulties. Empathy and mentalizing share minimal genetic overlap with systemising.  
* **Why it matters:** This provides molecular genetic evidence for the "fractionable autism" hypothesis and argues that future GWAS should target specific social-cognitive subphenotypes rather than treating social cognition as unitary.

The genetic correlation profiles diverge strikingly: systemising correlates positively with educational attainment and autism but has no overlap with empathy/mentalizing genetic variants, which instead correlate with anorexia and openness. This is important architectural information: it means that whatever genes influence empathy and mentalizing, they are not the same genes driving the cognitive/systemising dimension of autism. For the field's trajectory, this paper suggests that progress in social-emotional genetics requires moving away from omnibus diagnoses toward specific, faceted phenotypes — exactly the phenotypes that computational approaches (Papers 1–3) are now making measurable.

---

## **5\. Developmental trajectories are being mapped in two major cohorts**

Longitudinal social-emotional neuroimaging is concentrated in two programs: the **L-CID twin study** (Leiden/Erasmus, \~500 twins, ages 7–13, multiple fMRI waves) and the **ABCD Study** (21 US sites, \~11,878 youth, ages 9–10 onward, biannual imaging). Both have genetic data. The L-CID provides twin heritability decomposition; ABCD provides genome-wide genotyping at scale. However, most ABCD longitudinal papers focus on substance use or general psychopathology — social-emotional questions are an emerging frontier rather than an established one.

### **Paper 12**

**Van der Meulen, M., Dobbelaar, S., van Drunen, L., ... & Crone, E. A. (2023). Transitioning from childhood into adolescence: A comprehensive longitudinal behavioral and neuroimaging study on prosocial behavior and social inclusion. *NeuroImage*, 284, 120445\.** DOI: [10.1016/j.neuroimage.2023.120445](https://doi.org/10.1016/j.neuroimage.2023.120445)

* **Design:** Longitudinal, three-wave, ages 7–13. L-CID twin study.  
* **Sample:** N \= 512 at Wave 1, N \= 456 at Wave 2, N \= 336 at Wave 3\. MZ/DZ twin design enabling heritability estimation. Genetic decomposition available through twin design.  
* **What it establishes:** Prosocial compensating behavior increases linearly from ages 7 to 13, but its neural substrate reorganizes nonlinearly — ventral striatum shows a developmental peak while TPJ increases linearly, and **co-developmental coupling between brain and behavior** shifts the reward signature of prosocial acts as behavioral tendencies crystallize.  
* **Why it matters:** This is the most methodologically rigorous longitudinal fMRI study of prosocial development, revealing that different nodes of the social brain mature on different schedules and that their coordination with behavior follows complex, non-additive trajectories.

The Prosocial Cyberball paradigm allows simultaneous measurement of prosocial compensation, social inclusion processing, and reactive aggression. The quadratic trajectory in empathy-related brain responses (peaking in late childhood before declining) is noteworthy — it suggests a sensitive window for empathy-related neural plasticity that closes as adolescence begins. The twin design enables future genetic decomposition of these trajectories, and companion L-CID papers have already shown significant heritability for aggression-related neural responses (Achterberg et al., 2018).

### **Paper 13 (bonus — included for cohort coverage)**

**Brieant, A. E., Sisk, L. M., & Gee, D. G. (2021). Associations among negative life events, changes in cortico-limbic connectivity, and psychopathology in the ABCD Study. *Developmental Cognitive Neuroscience*, 52, 101022\.** DOI: [10.1016/j.dcn.2021.101022](https://doi.org/10.1016/j.dcn.2021.101022)

* **Design:** Longitudinal, two-wave (ages \~9–10 to 11–12), structural equation modeling of mediation pathways. ABCD Study.  
* **Sample:** N \= 4,006 youth. Genetic data available in ABCD cohort (Smokescreen array, TOPMed imputation on \~11,000 participants) though not used in this paper directly.  
* **What it establishes:** Negative life events predict **accelerated maturation** of cingulo-opercular–amygdala functional connectivity — youth exposed to more adversity show faster shifts toward adult-like negative connectivity patterns, supporting the stress acceleration hypothesis.  
* **Why it matters:** This demonstrates that adversity changes the developmental *tempo* of cortico-limbic circuit maturation, not just its endpoint — a finding with implications for sensitive period biology and the timing of social-emotional interventions. The ABCD cohort's genotype data enables immediate follow-up for gene-by-adversity analyses on these exact neural pathways.

The stress acceleration finding is consequential: more "mature" connectivity was associated with lower concurrent internalizing symptoms, suggesting the acceleration may be a short-term adaptive response. Whether this early maturation carries costs later in development (by closing sensitive periods prematurely) is a testable prediction that ABCD's ongoing longitudinal follow-up can address.

---

## **Lab and researcher mapping: who is building bridges**

This section identifies researchers and labs whose work appears across multiple sub-areas or across disciplinary boundaries. These are the bridge-builders whose programs connect otherwise siloed literatures.

### **Tier 1: Cross-disciplinary bridge-builders**

**Patricia Lockwood** (Social Decision Neuroscience Lab, University of Birmingham) Appears in: Phenotyping (Paper 1, via Rhoads who builds on her foundational 2016 PNAS work), Computational social neuroscience. Lockwood's 2016 demonstration that self-other learning rates differ launched the computational prosocial phenotyping program. Her lab now spans reinforcement learning, prosocial behavior, aging, and clinical applications. She is the central node connecting computational modeling to prosocial behavior research. Cited by geneticists (her phenotypes are candidates for future GWAS), developmental scientists, and clinical researchers.

**Rebecca Saxe & Joshua Tenenbaum** (MIT, Social Cognitive Neuroscience Lab \+ Computational Cognitive Science Lab) Appear in: Measurement (Paper 4). Their collaboration producing the generative theory-of-mind emotion prediction model represents a convergence of social neuroscience and machine learning that is being cited across cognitive science, affective computing, and AI alignment. Saxe's earlier fMRI work on the TPJ is being superseded by her lab's computational turn. Tenenbaum's probabilistic programming framework for social reasoning has become the dominant formal language for social inference modeling.

**Kay Tye** (Salk Institute / HHMI) Appears in: Circuits (Paper 7). Tye's lab is the dominant force in affective circuit neuroscience, with work spanning valence coding, loneliness, social reward, and neuropeptide mechanisms. Her work is cited by behavioral geneticists (her circuit findings suggest candidate pathways for genetic studies), developmental scientists, and computational neuroscientists. The neurotensin-valence finding has implications far beyond emotion — it changes how the field thinks about amygdala function generally.

**Varun Warrier & Simon Baron-Cohen** (Autism Research Centre, University of Cambridge) Appear in: Genetics (Papers 10, 11, and connected to Wendt et al. 2022). This team conducted essentially all existing GWAS of empathy and social-cognitive phenotypes (EQ, Eyes Test, systemising). Warrier is the most prolific first author in the social-emotional genetics space. Their work demonstrating genetic dissociability of social versus non-social autism traits has been cited by developmental psychologists, clinical researchers, and behavioral geneticists. The Cambridge ARC remains the only lab systematically running molecular genetic studies on social-cognitive phenotypes.

**Eveline Crone** (Brain and Development Research Center, Leiden University / Erasmus University Rotterdam) Appears in: Development (Papers 12, and L-CID cohort underlying Paper 13-area work via Achterberg, Mulder, Dobbelaar). Crone directs the L-CID twin study, which is the richest source of multi-wave longitudinal fMRI data on social-emotional development worldwide. Her program spans prosocial behavior, social rejection, self-evaluation, and parenting effects on brain development — all within a twin design enabling heritability estimation. L-CID is the closest thing the field has to a "social-emotional ABCD" with genetic decomposition.

### **Tier 2: Emerging influential programs**

**Weizhe Hong** (UCLA, Departments of Biological Chemistry, Neurobiology, & Bioengineering) Appears in: Circuits (Paper 8). Hong received the SfN Young Investigator Award and Society for Social Neuroscience Early Career Award. His lab uses cellular-resolution imaging and circuit manipulation to study prosocial behavior in mice, establishing animal models for behaviors previously thought to require primate cognition. His work is creating translation pipelines between rodent and human social neuroscience.

**Ueli Rutishauser & Ralph Adolphs** (Cedars-Sinai / Caltech) Appear in: Circuits (Paper 9). This collaboration maintains one of the world's few programs recording single neurons in the human brain during social-cognitive tasks. Their domain-specificity finding directly challenges the fMRI-based consensus about how social inference is neurally implemented. Rutishauser's technical expertise in human electrophysiology combined with Adolphs' longstanding program on the social brain makes this a unique translation point between animal and human circuit neuroscience.

**Samuel Gershman** (Computational Cognitive Neuroscience Lab, Harvard → Weizmann Institute) Appears in: Phenotyping (Paper 2). Gershman's move into dynamic phenotyping methodology has implications across every sub-area — his framework applies directly to social-cognitive computational phenotyping, developmental trajectory modeling, and genetic phenotype definition. Though not primarily a social neuroscientist, his methodological contributions are reshaping how the field measures individual differences.

**Joseph Barnby** (Royal Holloway / Social Computation and Cognitive Representation Lab) Appears in: Measurement (Paper 5). Barnby's program connecting computational social inference models to neuropharmacology and clinical paranoia is an emerging bridge between social cognition, computational psychiatry, and psychopharmacology. His framework for formalizing social representation to explain psychiatric symptoms (developed with Peter Dayan and Vaughan Bell) is gaining traction across disciplines.

**Dylan Gee** (CANDLab, Yale University) Appears in: Development (Paper 13). Gee's program on sensitive periods in cortico-limbic development, particularly the stress acceleration hypothesis, bridges developmental neuroscience, clinical psychology, and adversity research. Her use of ABCD data positions her lab to integrate genetic and environmental influences on social-emotional circuit development at scale.

**Simone Shamay-Tsoory** (University of Haifa) Appears in: Measurement (Paper 6). A longstanding leader in empathy and social neuroscience research, Shamay-Tsoory's lab produced the first prospectively validated hyperscanning result, demonstrating real-world predictive power for interbrain synchrony. Her work spans empathy, social touch, envy/schadenfreude, and cannabinoid effects on social cognition.

### **Notable cross-referencing patterns**

The most consequential intellectual traffic runs along three corridors. First, **computational modeling → phenotyping → genetics**: the constructs being formalized by Lockwood, Korn, Rhoads, and Saxe/Tenenbaum are exactly the phenotypes that Warrier, Bralten, and the genetics community need — but they have not yet been scaled to genotyped samples. This is the field's most important gap. Second, **rodent circuits → human single-neuron recording → human neuroimaging**: the Tye and Hong labs provide molecular-circuit mechanisms, the Rutishauser/Adolphs program tests whether these principles hold at the single-neuron level in humans, and the developmental neuroimaging programs (Crone, Gee) map the broader network-level manifestations. Third, **computation → pharmacology → clinical application**: Barnby's pharmacological validation of computational social inference models creates a bridge from formal models to interventional psychiatry.

The field's trajectory is toward closing these gaps: scaling computational phenotypes to large genotyped samples, establishing cross-species translation for circuit mechanisms, and connecting formalized social inference to neurotransmitter systems and developmental change. The infrastructure exists — ABCD, L-CID, UK Biobank, computational modeling frameworks — but integration across these levels remains the core unsolved problem.

