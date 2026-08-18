# **Predictive Processing and Active Inference: Empirical Reconnaissance, 2019–2026**

**The predictive processing framework has reached an inflection point where circuit-level causal evidence is arriving faster than the theory can absorb it, while active inference remains dramatically under-tested relative to its theoretical ambitions.** The strongest empirical gains since 2019 come from three fronts: mouse circuit dissections identifying specific thalamocortical mechanisms for prediction error computation (Furutachi et al. 2024, *Nature*), multilaminar primate electrophysiology revealing layer-and-frequency-specific "predictive routing" that subtly differs from canonical predictive coding (Bastos et al. 2020), and human 7T laminar fMRI showing content-specific prediction signals in deep cortical layers (Aitken et al. 2020; Kok lab). Meanwhile, the falsifiability critique has matured from philosophical hand-wringing into formal computational analysis showing testable constraints on precision-weighting (Bowman et al. 2023). Active inference's empirical track record is dominated by a single lab (Ryan Smith, Laureate Institute), exposing an enormous gap between theoretical claims and actual model-fitting to data. The neuromodulator-precision mapping (dopamine, acetylcholine, norepinephrine, serotonin) has proven substantially more complex than the clean one-to-one scheme originally proposed, with the most rigorous pharmacological test producing ambiguous cross-system effects (Iglesias et al. 2021).

---

## **SUB-AREA 1: Predictive Processing — Empirical Status**

### **The strongest tests derive from circuit and laminar methods that barely existed a decade ago**

The empirical testing of predictive processing has undergone a methodological revolution. Before 2018, most evidence came from EEG/MEG mismatch negativity paradigms and standard fMRI—methods that could show PP-*consistent* signals but couldn't distinguish predictions from adaptation or surprise from novelty. Three technologies have changed this: **7T laminar fMRI** (resolving cortical depth at sub-millimeter resolution), **multilaminar primate electrophysiology** (recording across all layers simultaneously in multiple areas), and **two-photon imaging with optogenetics in mice** (permitting causal manipulation of specific cell types during prediction). The papers below represent the field's highest-value empirical achievements using these methods.

---

**Paper 1: Furutachi, Franklin, Aldea, Mrsic-Flogel & Hofer (2024). "Cooperative thalamocortical circuit mechanism for sensory prediction errors." *Nature*, 633, 398–406. DOI: 10.1038/s41586-024-07851-w**

* **Design**: Two-photon calcium imaging with optogenetic manipulation in mice navigating virtual environments  
* **Sample**: 9+ mice across experiments; genetically targeted cell populations (VIP, SOM interneurons); no population genetic data  
* **Establishes**: A specific thalamocortical disinhibitory circuit involving the pulvinar and VIP interneurons is causally required for generating sensory prediction error signals in V1.  
* **Why care**: This is the first identification of a *causal circuit mechanism* for prediction error computation, moving the field from correlation to mechanism.

This paper represents a genuine watershed. The transition from "signals consistent with prediction error exist in cortex" to "here is the circuit that computes them, and silencing it eliminates them" is the kind of advance that restructures what questions can be asked next. The VIP-SOM disinhibitory motif cooperating with thalamic (pulvinar) input is a novel finding with immediate implications for understanding cortical computation. Critically, Furutachi et al. show that prediction errors do not encode a literal subtraction (actual minus predicted), but instead **selectively amplify stimulus-selective neurons for the unexpected input**. This favors a selective-amplification account over the error-computation account central to Rao & Ballard–style predictive coding. The cooperation between thalamic and cortical pathways also challenges purely cortical models. The head-fixed virtual-reality paradigm is a limitation for ecological validity, but the causal optogenetic design is unmatched in strength.

---

**Paper 2: Bastos, Lundqvist, Waite, Kopell & Miller (2020). "Layer and rhythm specificity for predictive routing." *PNAS*, 117(49), 31459–31469. DOI: 10.1073/pnas.2014868117**

* **Design**: Multilaminar electrophysiology across 5 cortical areas (V4, LIP, 7A, FEF, PFC) in macaques  
* **Sample**: 2 macaque monkeys; no genetic data  
* **Establishes**: Predictions are associated with alpha/beta (8–30 Hz) power in deep layers feeding back top-down, while unpredicted stimuli drive gamma (40–90 Hz) spiking in superficial layers feeding forward—across five cortical areas simultaneously.  
* **Why care**: The most comprehensive multiarea, multilaminar test of the core PP claim about directional prediction/error flow, and arguably the single strongest piece of laminar evidence for the framework.

This study tested the canonical microcircuit model's most specific prediction: that predictions and errors occupy distinct frequency bands, distinct cortical layers, and distinct directions of information flow. The simultaneous layer × frequency × directionality interaction across five areas is extremely difficult to explain with adaptation-only models. However, the "predictive routing" interpretation Bastos advances is subtly but importantly different from classical predictive coding. Rather than dedicated prediction-error neurons computing explicit subtraction, predictions act via **alpha/beta suppression of pathways carrying predicted input**. Unpredicted inputs pass forward because their pathways weren't suppressed. This reframes prediction errors as a consequence of absent suppression rather than a dedicated computation—a theoretical distinction with real empirical implications. Bastos has since developed this into the "BELIEF" framework (2025, *Trends in Cognitive Sciences*), explicitly positioning predictive routing as an alternative to Fristonian predictive coding. The N=2 is standard for primate neurophysiology but limits generalizability.

---

**Paper 3: Aitken, Menelaou, Warrington, Koolschijn, Corbin, Callaghan & Kok (2020). "Prior expectations evoke stimulus-specific activity in the deep layers of the primary visual cortex." *PLoS Biology*, 18(12), e3001023. DOI: 10.1371/journal.pbio.3001023**

* **Design**: 7T laminar fMRI in humans  
* **Sample**: \~20 participants; no genetic data  
* **Establishes**: Prior expectations about stimulus orientation evoke orientation-selective activity specifically in deep cortical layers of V1—even in the absence of bottom-up visual input.  
* **Why care**: Among the clearest demonstrations that predictions carry specific representational content and arrive at the cortical layers predicted by PP theory.

This paper from Peter Kok's group provides elegant evidence that expectations are not merely general modulatory signals but carry content-specific information (orientation selectivity) localized to the feedback-recipient layers. **Deep-layer localization** is consistent with predictions arriving via feedback connections terminating in infragranular layers. This is a non-trivial PP prediction that adaptation-based models cannot straightforwardly accommodate—adaptation predicts reduced responses to expected stimuli, not content-specific signals in deep layers during stimulus absence. The result has been replicated and extended by Haarsma et al. (2023), who additionally found that false percepts appear in middle (input) layers of V2 rather than the deep layers where predictions reside—introducing an important dissociation. The inherent limitations of laminar fMRI resolution (\~2mm cortical depth parceled into "deep," "middle," "superficial" bins with known venous-draining confounds) should be noted.

---

**Paper 4: Thomas, Haarsma, Nicholson, Yon, Kok & Press (2024). "Predictions and errors are distinctly represented across V1 layers." *Current Biology*, 34(10), R496–R498. DOI: 10.1016/j.cub.2024.04.013**

* **Design**: 7T laminar fMRI  
* **Sample**: \~20 participants; no genetic data  
* **Establishes**: Simultaneous dissociation of prediction and error signals across cortical depth in V1 within a single experiment—predictions in deep layers, prediction errors in superficial layers.  
* **Why care**: The first human study to simultaneously contrast expected vs. unexpected stimuli within the same cortical column, directly testing PP's most specific architectural claim.

This extends the Aitken et al. (2020) finding by demonstrating the complementary pattern: predictions and errors occupy different layers within the same experimental paradigm and same voxels. The simultaneous dissociation is important because prior work either showed expectation effects alone or error effects alone. The gradient-echo BOLD signal's venous draining problem means deep-layer effects can bleed into superficial-layer measurements, complicating clean dissociation. Replication with VASO-based acquisition methods (which have superior laminar specificity but lower SNR) would substantially strengthen the conclusion. Despite limitations, this study and the Aitken et al. work together form the most direct human evidence for layer-specific prediction/error segregation.

---

**Paper 5: Jordan & Keller (2020). "Opposing influence of top-down and bottom-up input on excitatory layer 2/3 neurons in mouse primary visual cortex." *Neuron*, 108(6), 1194–1205. DOI: 10.1016/j.neuron.2020.09.033**

* **Design**: Two-photon calcium imaging with optogenetic manipulations in transgenic mice  
* **Sample**: Multiple mice; Cre-driver lines for cell-type access; no population genetic data  
* **Establishes**: Layer 2/3 neurons in V1 can be functionally classified into "positive prediction error" (PPE) and "negative prediction error" (NPE) populations receiving opposing combinations of top-down motor and bottom-up visual input.  
* **Why care**: The strongest evidence for functionally distinct prediction error neuron subtypes—a core requirement of predictive coding that had been postulated but never demonstrated at the cellular level.

Finding neurons that combine motor predictions with visual input in opposing ways (PPE: excited when visual exceeds predicted; NPE: excited when predicted exceeds visual) is precisely what the Rao & Ballard model requires. Subsequent work (O'Toole et al. 2023\) showed these populations have **distinct molecular markers**, raising the prospect of genetically accessing prediction error neurons for causal manipulation—a genuinely new experimental capability. The Muzzu & Saleem (2021) challenge that these patterns reflect feature selectivity rather than prediction error computation remains unresolved, though the Keller lab's rebuttal (Vasilevskaya et al. 2023\) showed experience-dependent enhancement that simple feature selectivity cannot explain. This debate represents exactly the kind of empirical falsification attempt that critics say PP needs more of.

---

**Paper 6: Caucheteux, Gramfort & King (2023). "Evidence of a predictive coding hierarchy in the human brain listening to speech." *Nature Human Behaviour*, 7(3), 430–441. DOI: 10.1038/s41562-022-01516-2**

* **Design**: Computational modeling (encoding models using GPT-2 language model) \+ fMRI  
* **Sample**: **304 participants** (Narratives dataset); no genetic data  
* **Establishes**: The human brain makes hierarchical predictions spanning up to 8 words ahead during speech processing, with lower cortical areas predicting syntactic features and higher areas predicting semantic content.  
* **Why care**: With N=304, one of the largest neuroimaging studies to test PP predictions, leveraging modern deep learning to quantify hierarchical prediction across cortical areas.

This paper represents a genuinely new paradigm: using transformer-based language models as quantitative encoding models of brain activity. The syntactic-semantic factorization across cortical hierarchy is compelling—lower temporal regions predict syntax while prefrontal regions predict semantics, matching PP's hierarchical organization. The massive sample size provides exceptional statistical power rarely seen in neuroimaging. However, a significant caveat: the study uses representational similarity between GPT-2 layers and cortical areas rather than direct neural measurement of prediction signals. The "predictions" are inferred from model fit, not observed as actual neural prediction or error signals. This makes the evidence correlational and compatible with non-predictive-coding accounts of hierarchical language processing. It is an important bridge paper between deep learning and PP neuroscience, but not a strong test of PP-specific claims.

---

### **The falsifiability critique has become more rigorous, and PP proponents are responding**

**Paper 7: Bowman, Collins, Nayak & Cruse (2023). "Is predictive coding falsifiable?" *Neuroscience & Biobehavioral Reviews*, 154, 105404\. DOI: 10.1016/j.neubiorev.2023.105404**

* **Design**: Formal computational analysis with simulations  
* **Sample**: N/A (computational); code available on OSF  
* **Establishes**: While precision-weighting can rescue PP from "contra-predictive" data (where expected stimuli produce larger responses), this rescue has testable consequences: increased precision also reduces latency and increases frequency, providing falsifiable constraints.  
* **Why care**: The most rigorous formal treatment of the falsifiability problem, providing concrete criteria for when PP's precision escape route is and isn't legitimate.

The falsifiability question is the elephant in the PP room. Bowman et al. address it head-on with admirable rigor. The key insight is that precision-weighting—the most commonly used post-hoc adjustment to save PP from contradictory data—produces **correlated signatures** (latency reduction \+ frequency increase) that constrain when it can legitimately be invoked. This provides the field a falsifiability "playbook." However, it only addresses one escape route. PP has many other degrees of freedom (hierarchical level, timescale, active inference switching) that this analysis doesn't cover. The formal demonstration using a canonical predictive coding model makes the argument precise rather than merely philosophical—a significant methodological contribution.

---

**Paper 8: Walsh, McGovern, Clark & O'Connell (2020). "Evaluating the neurophysiological evidence for predictive processing as a model of perception." *Annals of the New York Academy of Sciences*, 1464(1), 242–268. DOI: 10.1111/nyas.14321**

* **Design**: Systematic review of neurophysiological evidence (\~200 studies)  
* **Sample**: N/A (review)  
* **Establishes**: Despite PP's influence, the evidence base is thinner than proponents suggest—many phenomena cited as PP evidence (repetition suppression, mismatch negativity) can be accommodated by feedforward \+ adaptation models.  
* **Why care**: The most cited and influential critical evaluation of PP's empirical status from a sympathetic but rigorous perspective.

Walsh et al. systematically decompose PP into testable hypotheses—expectation suppression, top-down origin of suppression, functionally distinct error/prediction populations, hierarchical specificity—and find each either mixed or compatible with simpler alternatives. Their key methodological insight is that the recording technique used (EEG, fMRI, single-unit, calcium imaging) determines which PP-consistent results will be found, explaining many contradictory findings across studies. This review established the benchmark against which subsequent laminar and circuit work has been evaluated. The field has partially responded to it: the Aitken, Thomas, and Furutachi papers directly address Walsh et al.'s demand for fine-grained neural evidence.

---

**Paper 9: Litwin & Miłkowski (2020). "Unification by fiat: Arrested development of predictive processing." *Cognitive Science*, 44(7), e12867. DOI: 10.1111/cogs.12867**

* **Design**: Philosophical analysis  
* **Sample**: N/A  
* **Establishes**: PP functions more as a research tradition than a testable theory, with unclear empirical commitments and multiple incompatible versions—its "precision" concept lacks clear neural operationalization, enabling post-hoc accommodation.  
* **Why care**: The most influential philosophical critique arguing that PP's problems are structural rather than merely empirical.

The distinction between "generalized PP" (which they argue is unfalsifiable) and "hierarchical PP" (which constrains implementations) is analytically useful. Their point about "precision" is particularly sharp: the mathematical term does crucial theoretical work but lacks clear psychological or neural operationalization, allowing post-hoc invocation. The follow-up (Litwin & Miłkowski 2022, *Synthese*, "Testable or bust") provides a more nuanced taxonomy distinguishing frameworks, theories, and models within PP. The emerging resolution in the field appears to be that PP-as-framework may resist falsification (like "computation" or "Darwinian selection"), but specific PP models are testable—a position Friston himself endorses when he says the Free Energy Principle is a variational principle (not falsifiable), while predictive coding is a process theory (falsifiable).

---

**Paper 10: Muzzu & Saleem (2021). "Feature selectivity can explain mismatch signals in mouse visual cortex." *Cell Reports*, 37(1), 109772\. DOI: 10.1016/j.celrep.2021.109772**

* **Design**: Two-photon calcium imaging in mouse V1  
* **Sample**: Multiple mice; no genetic data  
* **Establishes**: "Mismatch signals" previously interpreted as prediction errors can be explained by the convergence of visual feature selectivity (speed tuning) and locomotion-related gain, without invoking prediction error computation.  
* **Why care**: The most prominent empirical challenge to PP interpretation of visuomotor mismatch signals, demonstrating that simpler explanations for canonical PP evidence remain viable.

This paper generated a vigorous scientific exchange: Vasilevskaya et al. (2023, *Cell Reports*) from the Keller lab responded showing that visuomotor coupling experience greatly enhances mismatch responses in a manner that locomotion gain alone cannot explain. Muzzu & Saleem responded in turn. The resolution appears to be that feature selectivity contributes to but does not fully explain mismatch responses. **This is the kind of productive empirical debate** that the field needs more of—the back-and-forth between PP-consistent and non-PP interpretations of the same data, with each side forced to make more specific predictions.

---

**Paper 11: Haarsma, Kok, Press & Yon (2023). "Expectation cues and false percepts generate stimulus-specific activity in distinct layers of the early visual cortex." *Journal of Neuroscience*, 43(41), 6898–6907. DOI: 10.1523/JNEUROSCI.0544-23.2023**

* **Design**: 7T laminar fMRI \+ online behavioral sample  
* **Sample**: \~20 (fMRI) \+ N=100 (behavioral); no genetic data  
* **Establishes**: Prediction signals appear in deep layers (replicating Aitken et al. 2020), but high-confidence false percepts appear in middle input layers of V2—suggesting feedforward-like spontaneous activity contributes to hallucinations independently of top-down predictions.  
* **Why care**: Challenges the simplistic PP account that hallucinations arise purely from excessive top-down predictions, revealing a feedforward component.

The dissociation between prediction signals (deep layers) and false-percept signals (middle/input layers) is theoretically provocative. Standard PP accounts of hallucinations emphasize overly strong priors overwhelming weak sensory evidence. But the middle-layer signal for false percepts corresponds to feedforward input layers, suggesting **spontaneous stimulus-like activity** can generate false percepts independently of top-down predictions. This is a potential embarrassment for strict PP accounts of hallucination, or at least forces a more nuanced model where both top-down and bottom-up noise contribute to perceptual errors.

---

### **Where PP stands: the honest assessment**

No crucial experiment exists. No single finding has been confirmed that could not be explained by alternative frameworks. The Bastos et al. (2020) results come closest—the simultaneous layer × frequency × direction pattern is difficult (but perhaps not impossible) to generate from adaptation-based or surprise-coding models. The Aitken et al. (2020) finding of content-specific predictions in deep layers during stimulus absence is also resistant to simple adaptation accounts but could potentially be explained by working memory. The field remains in a state where PP is well-supported at the circuit level but not uniquely supported—the canonical microcircuit model is generating productive experiments, but no single observation decisively favors PP over all alternatives. The most important recent development is that Bastos himself—the first author on the most-cited predictive coding neural architecture paper (Bastos et al. 2012, *Neuron*, \~3,000 citations)—is now proposing "predictive routing" as a refinement that differs from Friston-style predictive coding in important ways, particularly in framing errors as absent suppression rather than explicit computation.

---

## **SUB-AREA 2: Active Inference — Uptake and Operationalization**

### **The theory-to-data ratio remains the field's central problem**

Active inference is genuinely being adopted beyond Friston's UCL group, but the gap between theoretical ambition and empirical delivery is enormous. A systematic review by Hodson, Mehta & Smith (2024) found that most published active inference papers are theoretical or simulation-based; the subset that actually fits models to empirical human data is small and dominated by a single laboratory. The honest accounting: for every paper fitting active inference to real data, there are approximately **15–20 theoretical papers** claiming the framework explains some phenomenon.

---

**Paper 1: Hodson, Mehta & Smith (2024). "The empirical status of predictive coding and active inference." *Neuroscience & Biobehavioral Reviews*, 157, 105473\. DOI: 10.1016/j.neubiorev.2023.105473**

* **Design**: Systematic review  
* **Sample**: N/A (review)  
* **Establishes**: Active inference models explain behavioral data reasonably well when fit, but have almost never been formally compared to non-Bayesian or model-free reinforcement learning alternatives—the critical missing step.  
* **Why care**: The honest reckoning paper. Anyone entering this literature should read it first because it maps exactly where evidence is strong, where it's suggestive, and where it's absent.

Written by Ryan Smith—the most prolific empirical active inference modeler outside the Friston orbit—this review's candor is its main contribution. It identifies a fundamental asymmetry: active inference has been used primarily as a modeling tool (fitting to data) rather than as a theory being tested (competitive model comparison). The paper implicitly reveals that the community has spent far more energy on theoretical elaboration than on the slow, unglamorous work of showing that active inference models fit data *better* than established alternatives. This is the paper that calibrates expectations.

---

**Paper 2: Smith, Friston & Whyte (2022). "A step-by-step tutorial on active inference and its application to empirical data." *Journal of Mathematical Psychology*, 107, 102632\. DOI: 10.1016/j.jmp.2021.102632**

* **Design**: Methodological tutorial with MATLAB code  
* **Sample**: Simulated demonstrations; no genetic data  
* **Establishes**: The first comprehensive, accessible tutorial for building, simulating, and fitting active inference POMDP models to behavioral data with working code.  
* **Why care**: This paper is the on-ramp—the publication that made active inference empirically accessible to non-specialists. Its **\~313 citations** indicate it actually changed practice.

Before this paper, fitting active inference models required deep SPM/MATLAB expertise or direct collaboration with Friston's group. Smith et al. democratized the pipeline: build a generative model of a task, simulate, fit to choice data via variational Bayes, interpret parameters. The complete code templates made it possible for a computational psychology graduate student to implement active inference without a sabbatical at UCL. This is infrastructure work whose importance is easily underestimated—it is the single most impactful paper for actual adoption of the framework.

---

**Paper 3: Smith et al. (2020). "A Bayesian computational model reveals a failure to adapt interoceptive precision estimates across depression, anxiety, eating, and substance use disorders." *PLoS Computational Biology*, 16(12), e1008484. DOI: 10.1371/journal.pcbi.1008484**

* **Design**: Cross-sectional computational psychiatry; Bayesian model fit to heartbeat tapping task  
* **Sample**: **N=434** (52 healthy controls, 382 psychiatric patients); no genetic data  
* **Establishes**: Selective dysfunction in adaptive interoceptive precision across psychiatric conditions—patients show reduced interoceptive precision, not altered prior beliefs.  
* **Why care**: The single best example of active inference operationalized as a computational phenotyping tool in clinical populations, producing clinically meaningful parameter differences.

This paper represents what active inference can look like when it works. A formal generative model of heartbeat perception fit to a large transdiagnostic sample produces a specific mechanistic finding: **low sensory precision, not hyperprecise priors**. The precision parameter captures something clinically meaningful—the degree to which patients fail to upweight bodily signals under perturbation. The finding was replicated (Smith et al. 2024, *Biological Psychology*). An honest boundary: the interoception model is simpler than full active inference POMDP machinery. It uses Bayesian precision estimation without the full policy-selection apparatus, which means it demonstrates Bayesian modeling of precision, not active inference per se.

---

**Paper 4: Marković, Stojić, Schwöbel & Kiebel (2021). "An empirical evaluation of active inference in multi-armed bandits." *Neural Networks*, 144, 229–246. DOI: 10.1016/j.neunet.2021.08.018**

* **Design**: Computational benchmarking; active inference vs. Bayesian UCB and optimistic Thompson sampling  
* **Sample**: Simulation-based; no genetic data  
* **Establishes**: Active inference outperforms established bandit algorithms in non-stationary (switching) environments but is less efficient in stationary settings.  
* **Why care**: The first rigorous head-to-head comparison of active inference against established alternatives, identifying specific conditions where active inference adds value.

From **TU Dresden** (Kiebel's group)—not UCL—this demonstrates genuine independent adoption. The key result is nuanced: active inference's information-seeking exploration gives it an edge in volatile environments but is less efficient when simpler algorithms suffice. This is exactly the kind of finding that helps calibrate when active inference adds value over alternatives. Code is available on GitHub, and the JAX implementation shows adoption of modern scientific computing. The limitation is that the comparison is simulation-only rather than fit to human behavioral data, but the formal model comparison methodology is rigorous and represents what the Hodson review says the field needs.

---

**Paper 5: Heins, Millidge, Da Costa, Mann, Friston & Couzin (2024). "Collective behavior from surprise minimization." *PNAS*, 121(17), e2320239121. DOI: 10.1073/pnas.2320239121**

* **Design**: Agent-based computational modeling  
* **Sample**: Simulation only; no genetic data  
* **Establishes**: Classical collective behavior phenomena (cohesion, milling, directed motion) emerge naturally from active inference agents without explicit behavioral rules.  
* **Why care**: Active inference's highest-profile 2024 achievement, demonstrating the framework's ability to unify collective behavior under a single principle and connecting it to a major field beyond neuroscience.

From Heins (Max Planck/VERSES) and Couzin's group in Konstanz, this extends active inference into animal collective behavior. The theoretical contribution is showing that "social forces" (the dominant paradigm) emerge as a special case of prediction error minimization. The paper provides testable predictions about how individual beliefs determine collective accuracy, which could be validated against fish schooling data. However, it does not fit parameters to empirical data from actual animal groups—it remains in the "proof-of-concept simulation" category. The connection to ecology and animal behavior represents a genuine expansion of the framework's empirical reach.

---

**Paper 6: Heins, Millidge, Demekas, Klein, Friston, Couzin & Tschantz (2022). "pymdp: A Python library for active inference in discrete state spaces." *Journal of Open Source Software*, 7(73), 4098\. DOI: 10.21105/joss.04098**

* **Design**: Software paper  
* **Sample**: N/A  
* **Establishes**: The first open-source Python package for active inference with POMDPs, replacing the MATLAB-only SPM/DEM bottleneck.  
* **Why care**: Software infrastructure determines adoption. pymdp was the critical step in making active inference accessible outside the MATLAB/SPM ecosystem.

The shift from MATLAB (license-required, opaque SPM codebase) to Python (open-source, interoperable with ML ecosystem) was transformative for the field. pymdp provides modular routines for state estimation, policy selection, and learning. The recent JAX backend enables GPU acceleration and automatic differentiation, critical for scaling. Developed primarily at Max Planck (Heins) and Sussex (Tschantz), with **539+ GitHub stars**. pymdp is now the de facto entry point for anyone entering active inference without MATLAB expertise. However, it was originally designed for simulation, not parameter estimation from empirical data—a gap that the Julia implementation addresses.

---

**Paper 7: Nehrer, Laursen, Heins, Friston, Mathys & Waade (2025). "Introducing ActiveInference.jl: A Julia Library for Simulation and Parameter Estimation with Active Inference Models." *Entropy*, 27(1), 62\. DOI: 10.3390/e27010062**

* **Design**: Software paper with parameter recovery demonstration  
* **Sample**: Simulated parameter recovery; no genetic data  
* **Establishes**: A Julia implementation integrating with ActionModels.jl and Turing.jl, enabling active inference model fitting to empirical data using MCMC—something pymdp initially lacked.  
* **Why care**: Specifically addresses the gap between simulation (what most active inference software does) and parameter estimation from empirical data (what computational psychiatry needs).

From **Aarhus University** (Mathys's Interacting Minds Centre), this represents genuine institutional spread. The integration with Turing.jl for Bayesian inference embeds active inference within a broader computational modeling ecosystem. The paper explicitly identifies the limitation of existing tools: "they do not usually allow for fitting models to empirically observed data, which is a fundamental method used in cognitive modelling." This Julia package fills exactly that gap.

---

**Paper 8: Çatal, Verbelen, Van de Maele, Dhoedt & Safron (2021). "Robot navigation as hierarchical active inference." *Neural Networks*, 142, 192–204. DOI: 10.1016/j.neunet.2021.05.010**

* **Design**: Robotics implementation; hierarchical generative model for SLAM on a real robot  
* **Sample**: N/A (robotic experiments)  
* **Establishes**: Navigation concepts (path integration, localization, mapping) emerge from active inference under a hierarchical generative model, demonstrated on a physical robot.  
* **Why care**: The best demonstration that active inference can move from simulation to physical implementation, and it comes from a lab (Ghent University–imec) entirely independent of the Friston group.

This is genuinely independent work—no Friston co-authorship. The model draws explicit parallels with hippocampal representations (place cells, grid cells), giving the robotics implementation neuroscientific motivation. The group has continued building on this (de Tinguy et al. 2024/2025), showing the approach scales to ROS2 environments. The limitation is that performance comparison against state-of-the-art SLAM algorithms (ORB-SLAM3, etc.) is limited, making it hard to assess whether active inference adds engineering value beyond conceptual elegance.

---

**Paper 9: Schwartenbeck, Passecker, Hauser, FitzGerald, Kronbichler & Friston (2019). "Computational mechanisms of curiosity and goal-directed exploration." *eLife*, 8, e41703. DOI: 10.7554/eLife.41703**

* **Design**: Computational theory with simulation demonstrations  
* **Sample**: Simulation only; no genetic data  
* **Establishes**: Two distinct exploration mechanisms derived from expected free energy—"hidden state exploration" (active inference) and "model parameter exploration" (active learning)—with separable behavioral signatures.  
* **Why care**: Made active inference's treatment of curiosity and exploration rigorous, providing concrete testable predictions about exploratory behavior.

The decomposition of epistemic value into two components with different behavioral predictions is a genuine theoretical innovation. One drives agents toward unambiguous observations (to resolve state uncertainty), the other drives them toward uncertain outcomes (to learn model parameters). These predictions are concrete and testable. This paper is simulation-only but has been followed by empirical model-fitting work (Smith et al. 2025\) that tests these predictions against human choice data.

---

### **Where active inference stands: the honest assessment**

The empirical track record is dominated by **Ryan Smith's Laureate Institute** group. Outside that lab, empirical model-fitting to human behavioral data is extremely rare. Papers that actually fit active inference models to empirical human data and estimate parameters number approximately **15–30 total** as of 2025\. Papers with formal model comparison between active inference and reinforcement learning alternatives number **fewer than 10**. No genuinely surprising, novel prediction has been confirmed that couldn't have been anticipated from other frameworks. Active inference has so far primarily re-derived known results within a more unified framework rather than generating risky novel predictions. The framework's strength is its generality; its weakness is that generality purchases explanatory breadth at the cost of predictive specificity.

---

## **SUB-AREA 3: Precision Weighting and Neuromodulation**

### **The clean one-to-one mapping has fractured under pharmacological testing**

The theoretical elegance of the neuromodulator-precision mapping—acetylcholine signals sensory precision, dopamine signals reward prediction precision, norepinephrine signals environmental volatility, serotonin signals prior precision—has not survived contact with empirical pharmacology in its simple form. The most rigorous pharmacological tests reveal **substantial cross-system effects** that complicate the neat assignment. The field's strongest empirical anchors are: dopamine mediates cortical precision-weighting of unsigned prediction errors (Haarsma et al. 2021), norepinephrine underpins volatility-sensitive learning and pupil-indexed updating (Lawson et al. 2021), and serotonergic psychedelics disrupt prediction error processing consistent with REBUS (Duerler et al. 2022; Girn et al. 2022). Genetic evidence connecting neuromodulatory gene variants to precision weighting is nearly nonexistent.

---

**Paper 1: Haarsma, Fletcher, Griffin, Taverne, Ziauddeen, Spencer, Miller, Katthagen, Goodyer, Diederen & Murray (2021). "Precision weighting of cortical unsigned prediction error signals benefits learning, is mediated by dopamine, and is impaired in psychosis." *Molecular Psychiatry*, 26(9), 5320–5333. DOI: 10.1038/s41380-020-0803-8**

* **Design**: Two studies: (1) Pharmacological fMRI (bromocriptine/sulpiride/placebo, double-blind between-subjects); (2) Case-control fMRI (first-episode psychosis, at-risk mental state, controls)  
* **Sample**: Study 1: N=59 healthy volunteers; Study 2: N=74 (20 FEP, 24 ARMS, 30 HC); no genetic data  
* **Establishes**: Precision-weighted unsigned prediction errors are encoded in superior frontal cortex, modulated by dopamine (disrupted by sulpiride D2 antagonism), and impaired in early psychosis.  
* **Why care**: The single most important paper linking "dopamine controls precision" to actual pharmacological and clinical data with formal computational modeling.

This study is methodologically exemplary. The computational modeling separately estimates precision-weighted signed and unsigned prediction errors, and the fMRI analysis localizes unsigned PE precision-weighting to bilateral superior frontal gyri and dorsal ACC—**not the striatum**, which is significant because it positions dopaminergic precision control as a cortical phenomenon. Sulpiride (D2 antagonist) disrupted precision weighting while bromocriptine (D2 agonist) did not produce clear effects, suggesting a more nuanced dopaminergic mechanism than simple gain modulation. The psychosis sample showed impaired precision weighting correlating dimensionally with schizotypy scores, establishing a continuous clinical relationship.

---

**Paper 2: Iglesias, Kasper, Harrison, Manka, Mathys & Stephan (2021). "Cholinergic and dopaminergic effects on prediction error and uncertainty responses during sensory associative learning." *NeuroImage*, 226, 117590\. DOI: 10.1016/j.neuroimage.2020.117590**

* **Design**: Two between-subjects double-blind placebo-controlled pharmacological fMRI studies using antagonists (amisulpride \+ biperiden) and enhancers (levodopa \+ galantamine); HGF modeling  
* **Sample**: \~120 healthy participants total; exploratory COMT and ChAT genotyping (underpowered)  
* **Establishes**: Replicates the basic DA-midbrain/ACh-basal-forebrain hierarchy for prediction errors, BUT the pharmacological manipulations did NOT produce the predicted clean dissociation—substantial cross-system effects emerged.  
* **Why care**: The most rigorous pharmacological test of the DA/ACh hierarchy hypothesis, and its ambiguous result demonstrates the mapping is far more complex than initially theorized.

This is the essential follow-up to the foundational Iglesias et al. (2013, *Neuron*) paper. The authors attempted the obvious next step: pharmacologically manipulating dopaminergic and cholinergic systems to test causal roles. The failure to find a clean dichotomy is genuinely informative. **Galantamine** (cholinesterase inhibitor) enhanced low-level PE responses in dopaminergic midbrain—not in cholinergic regions as predicted. **Biperiden** (muscarinic antagonist) enhanced low-level PEs and attenuated high-level PE activity. The cross-talk is the finding. The exploratory COMT/ChAT genotype analyses were underpowered but represent a rare attempt to integrate genetic variation into this framework. The authors are admirably transparent about pharmacological fMRI confounds (vascular effects, dose-response uncertainty).

---

**Paper 3: Lawson, Bisby, Nord, Burgess & Rees (2021). "The computational, pharmacological, and physiological determinants of sensory learning under uncertainty." *Current Biology*, 31(1), 163–172. DOI: 10.1016/j.cub.2020.10.043**

* **Design**: Between-subjects double-blind placebo-controlled (propranolol 40mg vs. placebo) with pupillometry and HGF modeling  
* **Sample**: N=40 (20 per group); no genetic data  
* **Establishes**: Propranolol (β-adrenergic antagonist) reduced learning rates, increased dominance of prior expectations over sensory evidence under uncertainty, and eliminated phasic pupil encoding of prediction errors and volatility.  
* **Why care**: First direct pharmacological evidence that noradrenaline underpins behavioral and computational responses to uncertainty, directly testing PP's assignment of NE to volatility signaling.

This study integrates pharmacological, computational, and physiological (pupillometric) levels in a way that exemplifies what precision-weighting research should look like. By blocking norepinephrine with propranolol, Lawson showed that learning about volatility was reduced and pupil size no longer tracked precision-weighted PEs—**exactly as PP predicts**. The link to cardiovascular physiology (baseline systolic BP predicting volatility estimates) connects interoceptive signals to hierarchical inference. This builds on Lawson et al. (2017, *Nature Neuroscience*), which showed adults with autism overestimate environmental volatility with aberrant pupil responses, creating a coherent research program: computational models → clinical phenotype → pharmacological mechanism → physiological readout.

---

**Paper 4: Diaconescu, Mathys, Weber, Daunizeau, Kasper, Lomakina, Fehr & Stephan (2017). "Hierarchical prediction errors in midbrain and septum during social learning." *Social Cognitive and Affective Neuroscience*, 12(4), 618–634. DOI: 10.1093/scan/nsw171**

* **Design**: Two independent fMRI studies of social learning with HGF modeling and COMT genotyping  
* **Sample**: N=82 across two samples; **COMT Val158Met genotyping included**  
* **Establishes**: The DA-midbrain/ACh-septum hierarchy generalizes to social learning, and COMT genotype modulates striatal encoding of precision-weighted social prediction errors (Met/Met \> Val carriers).  
* **Why care**: The only published paper directly connecting genetic variation in a neuromodulatory gene to individual differences in precision-weighted prediction error encoding within the PP framework.

Three crucial contributions: the DA/ACh architecture generalizes from sensory to social learning; COMT variation modulates precision-weighted PE encoding; and the finding replicates across independent samples. The **COMT result** (Met/Met homozygotes, who have higher cortical dopamine, showing enhanced striatal PE responses) is the closest thing the field has to genetic evidence for the neuromodulator-precision mapping. The genetic analysis was exploratory and underpowered for genome-wide approaches—replication with larger samples and polygenic scores is needed. This remains a lonely finding; no subsequent large-scale genetic study of precision weighting has been published.

---

**Paper 5: Powers, Mathys & Corlett (2017). "Pavlovian conditioning–induced hallucinations result from overweighting of perceptual priors." *Science*, 357(6351), 596–600. DOI: 10.1126/science.aan3458**

* **Design**: Pavlovian conditioning with fMRI and HGF modeling; 2×2 design (voice-hearers vs. non-voice-hearers × treatment-seekers vs. non-treatment-seekers)  
* **Sample**: \~60 participants across 4 groups; no genetic data  
* **Establishes**: Conditioned hallucinations result from overweighting of perceptual priors, and computational modeling can distinguish pathological from non-pathological voice-hearing based on precision parameters.  
* **Why care**: The landmark demonstration that aberrant precision weighting can induce and explain hallucinations, providing the most elegant experimental validation of the PP account of psychosis.

A tour de force of experimental design. By creating new perceptual priors through Pavlovian conditioning and measuring how different populations update beliefs about sensory evidence, Powers et al. showed that voice-hearers have **higher prior precision relative to sensory precision**. Crucially, treatment-seekers (psychosis patients) could be distinguished from non-treatment-seekers (psychics who hear voices without distress) by pattern of computational parameters and neural signatures. The fMRI identified anterior insula, auditory cortex, and cerebellum as mediating circuitry. This paper has spawned a productive research program connecting precision weighting to glutamate levels and semantic priors.

---

**Paper 6: Duerler, Brem, Fraga-González, Neef, Allen, Zeidman, Stämpfli, Vollenweider & Preller (2022). "Psilocybin induces aberrant prediction error processing of tactile mismatch responses—a simultaneous EEG-fMRI study." *Cerebral Cortex*, 32(1), 186–196. DOI: 10.1093/cercor/bhab202**

* **Design**: Double-blind, placebo-controlled, within-subjects, simultaneous EEG-fMRI during somatosensory oddball under psilocybin  
* **Sample**: N=22 healthy volunteers; no genetic data  
* **Establishes**: Psilocybin reduces tactile mismatch negativity and decreases differential BOLD activation to deviant vs. standard stimuli in frontal cortex and cerebellum.  
* **Why care**: The most direct empirical test of the REBUS model's prediction that psychedelics alter precision-weighted prediction errors.

This provides direct evidence that 5-HT2A agonism disrupts the brain's distinction between expected and unexpected sensory inputs—exactly as REBUS predicts. The simultaneous EEG-fMRI captured both temporal (MMN reduction) and spatial (frontal BOLD reduction) signatures. Subjective disembodiment and experience of unity correlated with MMN amplitude changes, linking the computational disruption to psychedelic phenomenology. A significant limitation: no formal precision-weighting model (HGF, DCM) was applied—the study uses MMN as a proxy for prediction error without decomposing it into precision and error components. Future work should apply computational modeling to determine whether psilocybin specifically alters the *precision* of PEs versus the PEs themselves.

---

**Paper 7: Girn, Roseman, Bernhardt, Smallwood, Carhart-Harris & Spreng (2022). "Serotonergic psychedelic drugs LSD and psilocybin reduce the hierarchical differentiation of unimodal and transmodal cortex." *NeuroImage*, 256, 119220\. DOI: 10.1016/j.neuroimage.2022.119220**

* **Design**: Re-analysis of two pharmacological resting-state fMRI datasets using gradient-mapping connectivity analyses  
* **Sample**: LSD: N=15 (within-subjects); Psilocybin: N=9 (within-subjects); no genetic data  
* **Establishes**: Both LSD and psilocybin cause contraction (flattening) of the principal gradient of cortical functional connectivity—the hierarchy from unimodal to transmodal cortex.  
* **Why care**: The most direct neuroimaging test of REBUS's central prediction that psychedelics flatten cortical hierarchy, using a quantitative measure of hierarchical functional organization.

The flattening effect means unimodal (sensory) regions become more functionally connected with transmodal (association) regions, consistent with increased cross-talk and dedifferentiation. The replication across LSD and psilocybin (and subsequently DMT; Timmermann et al. 2023\) strengthens the finding. However, sample sizes are small, these are re-analyses of existing datasets, and the study cannot determine whether hierarchy flattening *causes* altered subjective experience or merely accompanies it. The "synthetic surprise" alternative (Pérez-González et al. 2024\) challenges whether psilocybin relaxes priors or instead increases bottom-up surprise—a distinction the gradient-mapping approach cannot resolve.

---

**Paper 8: Lawson, Mathys & Rees (2017). "Adults with autism overestimate the volatility of the sensory environment." *Nature Neuroscience*, 20(9), 1293–1299. DOI: 10.1038/nn.4615**

* **Design**: Probabilistic associative learning with pupillometry and HGF modeling; case-control  
* **Sample**: N=49 (24 ASD, 25 controls); no genetic data  
* **Establishes**: Adults with ASD overestimate environmental volatility, leading to reduced surprise to unexpected events, with aberrant pupillometric responses suggesting heightened phasic noradrenergic signaling.  
* **Why care**: The landmark empirical demonstration of the "aberrant precision" account of autism, directly linking computational modeling of precision-weighted learning to NE-indexed physiological signals.

The key insight is counterintuitive: rather than simply having "weaker priors" (the Pellicano & Burr 2012 hypo-prior hypothesis), individuals with ASD **overestimate how volatile the environment is**—which means their priors are continually overridden, producing a sensory-dominated processing style via precision mechanism. Elevated volatility estimates reduce the precision of predictions, thereby upweighting sensory evidence. The pupillometry data showing ASD participants' pupils didn't track surprise normally but correlated with model-estimated volatility suggests a specific disruption in NE-mediated precision adjustment. This paper directly motivated the propranolol study (Lawson et al. 2021), creating a coherent pharmacological-computational research program.

---

**Paper 9: Carhart-Harris & Friston (2019). "REBUS and the anarchic brain: Toward a unified model of the brain action of psychedelics." *Pharmacological Reviews*, 71(3), 316–344. DOI: 10.1124/pr.118.017160**

* **Design**: Theoretical/review  
* **Sample**: N/A  
* **Establishes**: Psychedelics work by relaxing high-level priors via 5-HT2A agonism, sensitizing the system to bottom-up prediction errors—producing increased neural entropy and altered consciousness.  
* **Why care**: While theoretical, this generated the specific testable predictions now being empirically evaluated; understanding it is prerequisite for interpreting the empirical literature.

REBUS's testable predictions and their empirical status: (1) Increased neural entropy—**supported** by Lempel-Ziv complexity measures, though McCulloch et al. 2023 found mixed results. (2) Flattened cortical hierarchy—**supported** by Girn et al. 2022\. (3) Reduced top-down connectivity—**supported** by traveling wave analyses (Alamia et al. 2020; Timmermann et al. 2023). (4) Altered prediction error processing—**supported** by Duerler et al. 2022\. (5) Dose-dependent belief revision—**partially supported**. However, the "synthetic surprise" alternative and enhanced imaginative suggestibility under psychedelics (which implies *strengthened* top-down control) challenge the model. REBUS remains productive but faces mounting complexity.

---

**Paper 10: Iglesias, Mathys, Brodersen, Kasper, Piccirelli, den Ouden & Stephan (2013). "Hierarchical prediction errors in midbrain and basal forebrain during sensory learning." *Neuron*, 80(2), 519–530. DOI: 10.1016/j.neuron.2013.09.032**

* **Design**: Two independent fMRI studies with HGF computational modeling  
* **Sample**: N=118 across three samples; no genetic data  
* **Establishes**: Low-level precision-weighted PEs about stimulus outcomes activate dopaminergic VTA/SN, while high-level precision-weighted PEs about stimulus contingencies (volatility) activate cholinergic basal forebrain—replicated across independent samples.  
* **Why care**: The foundational empirical paper for the entire neuromodulator-precision hierarchy literature; every subsequent study in this area references it.

Though published before the 2019 window, inclusion is essential for understanding the field. The methodological rigor—replication, stringent FWE correction, anatomically defined ROIs—set a gold standard that subsequent work has tried to match. The HGF framework developed by Mathys became the dominant computational tool for this literature. The critical limitation is that fMRI BOLD in midbrain and basal forebrain cannot definitively identify dopaminergic or cholinergic neurons (these regions contain glutamatergic and GABAergic neurons), motivating the pharmacological follow-up (Iglesias et al. 2021\) that found the mapping to be more complex than the original clean dissociation suggested.

---

### **The neuromodulator-precision mapping: where it stands**

* **Dopamine → precision of unsigned PEs**: Strongest evidence (Haarsma et al. 2021), but localized to cortical sites rather than subcortical  
* **Acetylcholine → volatility/higher-level PEs**: Observational fMRI support (Iglesias 2013; Diaconescu 2017\) but pharmacological test was ambiguous (Iglesias 2021 found cross-system effects)  
* **Norepinephrine → volatility/uncertainty**: Directly supported by propranolol (Lawson 2021\) and pupillometry work  
* **Serotonin → prior precision**: Indirectly supported via REBUS tests (Girn 2022; Duerler 2022\) but mechanism (relaxed priors vs. enhanced surprise) is debated  
* **Genetic evidence**: Nearly nonexistent—only COMT (Diaconescu 2017), exploratory and underpowered  
* **Circuit-level thalamic evidence**: Largely theoretical with indirect animal support; no human study has directly tested thalamic gating as precision within a formal PP computational framework

---

## **Lab and Researcher Mapping**

### **Theorists primarily elaborating the framework**

**Karl Friston** (UCL Wellcome Centre / VERSES AI) remains the gravitational center. Now also Chief Scientist at VERSES AI, creating industry pull on the field. His theoretical output continues at extraordinary volume, but his most impactful recent role may be as a co-author enabling others' empirical work rather than generating it directly.

**Andy Clark** (University of Sussex) made PP accessible through *Surfing Uncertainty* (2015) and *The Experience Machine* (2023). Philosophical architect more than empiricist; his contribution is conceptual framing.

**Jakob Hohwy** (Monash University) provides the "skull-bound" philosophical interpretation of PP. Currently engaged in adversarial consciousness science (PP vs. IIT) through the Templeton ARC initiative.

**Thomas Parr** (Oxford, Nuffield Dept. of Clinical Neurosciences) is transitioning from Friston trainee to independent PI. Co-authored the *Active Inference* textbook (MIT Press, 2022). \~11,700 citations. Clinical academic role connecting theory to neurology.

**Lancelot Da Costa** (VERSES AI / ELLIS Institute) won Best Maths PhD Thesis Prize 2025 (Imperial College). Mathematical foundations of active inference and Bayesian mechanics. Interned with Yoshua Bengio at Mila in 2024\. Rising star in the mathematical formalization space.

**Maxwell Ramstead** (Noumenal Labs; formerly VERSES) bridges philosophy, physics, and AI industry. PhD at McGill; extensive Friston collaboration. "Bayesian mechanics" and multiscale active inference.

### **Empiricists designing decisive experiments**

**Peter Kok** (UCL, Prediction & Perception Lab) is arguably the field's most important empirical tester right now. Won 2024 CNS Young Investigator Award. Trained with Floris de Lange (Donders); postdoc with Turk-Browne (Yale/Princeton). Uses **7T laminar fMRI** to test layer-specific PP predictions. Recent: "Communication of perceptual predictions from the hippocampus to the deep layers of the parahippocampal cortex" (*Science Advances*, 2025).

**André Bastos** (Vanderbilt University) won 2025 CNS Young Investigator Award. Trained with Pascal Fries (ESI Frankfurt), Earl Miller (MIT), Nancy Kopell (Boston University). His "canonical microcircuits for predictive coding" (Neuron 2012, \~3,000 citations) launched the field's neural architecture. Now his own work challenges vanilla predictive coding with **"predictive routing"** and the "BELIEF" framework—making him both the field's most important empiricist and a constructive internal critic.

**Georg Keller** (Friedrich Miescher Institute, Basel) is the most important circuit-level empiricist. Discovered visuomotor prediction errors in mouse V1 at the single-neuron level. His lab (with Mrsic-Flogel) identified PPE and NPE neuron populations, defined the VIP-SOM disinhibitory circuit for prediction errors, and published the Furutachi et al. (2024) *Nature* paper. Arguably producing the strongest mechanistic evidence for PP.

**Floris de Lange** (Radboud/Donders Institute) is an established leader in expectation effects on visual cortex. Trained Peter Kok and Hanneke den Ouden. The Donders Institute is a major PP empirical hub.

**Ryan Smith** (Laureate Institute for Brain Research, Tulsa) is the dominant empirical active-inference modeler outside UCL. Responsible for the vast majority of published active inference model-fitting studies. The step-by-step tutorial (2022, \~313 citations) made active inference accessible. Computational psychiatry of interoception, decision-making, and transdiagnostic precision.

**Rebecca Lawson** (University of Cambridge) established the "aberrant precision" account of autism (*Nature Neuroscience*, 2017). Trained at UCL with Friston and Rees; postdoc with Hohwy. Coherent research program connecting computational models → clinical phenotypes → pharmacological mechanisms.

**Ryszard Auksztulewicz** (Maastricht University) won an **ERC Consolidator Grant** for the MemPred project disentangling memory from prediction in neural populations. Trained at Humboldt Berlin, postdocs with Friston (UCL), Nobre (Oxford), and Melloni (MPI Frankfurt).

**Lars Muckli** (University of Glasgow) with **Lucy Petro** pioneered layer-specific fMRI of cortical feedback. Demonstrated that non-stimulated V1 regions carry contextual/predictive information.

**Christoph Mathys** (Aarhus University) created the **Hierarchical Gaussian Filter (HGF)**—one of the most widely used computational models for testing PP predictions in behavior. Now also building ActiveInference.jl. The Interacting Minds Centre at Aarhus is an emerging cluster.

### **Tool-builders making frameworks testable**

**Conor Heins** (now NIDA/NIH; formerly Max Planck/VERSES) is lead developer of **pymdp**, the most important open-source active inference library (539+ GitHub stars). Also first author on collective behavior from surprise minimization (*PNAS*, 2024).

**Alexander Tschantz** (Sussex → VERSES) co-developed pymdp and deep active inference methods. Bridges active inference to reinforcement learning.

**Bert de Vries** (Eindhoven University of Technology) develops **RxInfer.jl**, a Julia package for reactive Bayesian inference using factor graphs—a message-passing approach to active inference at scale.

**Beren Millidge** (independent researcher) co-developed pymdp, maintains the influential FEP\_Active\_Inference\_Papers GitHub repository, and authored "Predictive coding approximates backprop along arbitrary computation graphs"—an important AI bridge paper.

**Pablo Lanillos** (Donders Institute / CSIC Madrid) leads active inference robotics implementations, including body perception on humanoid robots and torque control.

### **Critics providing productive challenges**

**Mark Sprevak** (University of Edinburgh) authored a major 4-part series "Predictive coding I–IV" (*Philosophy Compass*, 2024)—the most thorough philosophical analysis distinguishing PP's actual commitments from conflated claims. Essential reading for anyone trying to understand what PP does and does not predict.

**Jeffrey Bowers** (University of Bristol) co-authored the landmark "Bayesian just-so stories" critique (2012) and the formal falsifiability analysis with Bowman et al. (2023). The most persistent empirical critic.

**Paweł Litwin & Marcin Miłkowski** (Warsaw) authored "Unification by fiat" (*Cognitive Science*, 2020\) and "Testable or bust" (*Synthese*, 2022)—the most analytically rigorous philosophical critique of PP's theoretical structure.

**Kevin Walsh** and Redmond O'Connell (Trinity College Dublin) produced the most influential empirical evaluation of PP's neurophysiological evidence (*NYAS*, 2020), establishing the benchmark for what counts as strong evidence.

### **Institutional clusters and training lineages**

The field's institutional geography centers on **six major clusters**. UCL's Wellcome Centre remains the epicenter, though its influence now flows primarily through alumni: Parr → Oxford, Da Costa → VERSES/ELLIS, Sajid → Harvard, Lawson → Cambridge, Schwartenbeck → MPI Tübingen, Auksztulewicz → Maastricht. The **Donders Institute** (Radboud) is the leading empirical hub for PP in perception, anchored by de Lange and now Lanillos. **Sussex** bridges PP to consciousness science (Seth) and mathematical formalization (Buckley). **Vanderbilt** (Bastos) is building the strongest NHP electrophysiology program for predictive routing. **Aarhus** (Mathys) is emerging as a computational psychiatry cluster. **Laureate Institute** (Smith) houses the dominant active inference model-fitting operation.

The Friston training tree is extensive: virtually every major empirical researcher in this space has either trained at UCL, collaborated directly with Friston, or used tools (SPM, HGF) developed by his close collaborators. Truly independent adoption (no Friston co-authorship) is rarer than the field's breadth might suggest. The Ghent robotics group (Çatal/Verbelen), TU Dresden (Marković/Kiebel), and the Stephan group at ETH Zurich (Iglesias, Mathys before moving to Aarhus) represent the clearest examples of genuinely independent empirical programs.

A notable emerging trend: **industry pull** is attracting theorists away from academic empirical work. VERSES AI (now partly dissolved, with researchers moving to Noumenal Labs and elsewhere) employed Friston, Da Costa, Heins, Verbelen, and Ramstead at various points. Whether this accelerates or retards empirical progress remains to be seen.

### **Key software ecosystem**

| Tool | Language | Lead developers | Primary use |
| ----- | ----- | ----- | ----- |
| **SPM/DEM** | MATLAB | Friston lab (UCL) | Original active inference; requires license |
| **pymdp** | Python/JAX | Heins, Tschantz, Millidge | Open-source POMDP simulation; growing |
| **ActiveInference.jl** | Julia | Nehrer, Waade, Mathys (Aarhus) | Model fitting to empirical data via MCMC |
| **RxInfer.jl** | Julia | Bagaev, de Vries (Eindhoven) | Reactive Bayesian inference; scalable |
| **PyHGF** | Python | Mathys group | Hierarchical Gaussian Filter for PP |

---

## **Conclusion**

The predictive processing research program is healthier than its critics suggest but weaker than its proponents claim. The genuine advances since 2019 are concentrated in **circuit-level causal mechanisms** (Furutachi et al. 2024; Jordan & Keller 2020), **laminar-resolution human neuroimaging** (Kok lab's 7T work), and **multiarea primate electrophysiology** (Bastos et al. 2020)—technologies that can finally test PP's most specific neural predictions. These have partially confirmed the framework's core architecture while simultaneously revealing that the reality is more nuanced than canonical models assumed: prediction errors appear to involve selective amplification rather than literal subtraction, and "predictive routing" via frequency-band suppression may be more accurate than dedicated error-computing neurons.

Active inference faces a credibility gap that the community itself acknowledges. The theoretical machinery is impressive but has not been subjected to competitive empirical testing at anything approaching the scale required to justify its grand unificatory claims. The field needs **50 more papers like Smith et al. (2020)**—fitting models to real clinical data and comparing them formally to alternatives—before active inference's empirical status matches its theoretical ambitions.

The precision-neuromodulation mapping remains the framework's most clinically productive arm, generating real computational psychiatry findings in psychosis, autism, and the psychedelic state. But the clean one-to-one mapping has not survived pharmacological testing, and the near-total absence of genetic evidence represents a major untapped opportunity. The researcher who first conducts a well-powered GWAS-informed study of precision weighting—connecting polygenic scores for dopaminergic, cholinergic, or noradrenergic function to individual differences in HGF-estimated precision parameters—will produce one of the most cited papers in this literature.

