# **Social Defeat**

**Source manifest:** Five NotebookLM response pastes (this conversation) \+ card spec via google\_drive\_fetch. SOC doc fetch failed twice; cannot verify against existing SOC content. Brian should duplicate-check before integrating.

**Sources in this notebook:**

* Koolhaas et al. (2017) — “Social stress models in rodents” → SSM  
* Koolhaas et al. (2013) — “The resident-intruder paradigm” → RIP  
* Koolhaas et al. (2007) — “Individual Variation in Coping” → IVC  
* Lieberman & Eisenberger (2005) — “The pains of social rejection” → PSR  
* Williams & Nida (2011) — ostracism/Cyberball → OST  
* Hartgerink et al. (2015) — Cyberball meta-analysis → CYB  
* Krishnan et al. (2007) — molecular resilience/susceptibility → MRS  
* Nestler & Russo (2024) — molecular resilience update → MRU  
* Bagot et al. (2017) — ketamine transcriptional response → KTR  
* Essex et al. (2011) — early life stress HPA programming → ELS  
* Ostlund & Pérez-Edgar (2023) — two-hit model → THM  
* Milewski et al. (2022) — hierarchy plasticity → BPP  
* Hagen (2011) — evolutionary theories of depression → ETD  
* Bjorkqvist (2001) — social defeat in humans → SDH  
* Yuan et al. (2018) — zebrafish personality → ZBP  
* Toyoda (2017) — CSDS in animal science → SDS

---

## **CARDS**

---

### **Lieberman & Eisenberger (2005)**

*Structural note: This paper grounds social threat detection in the physical pain alarm system. For HPAM, it means Withdrawal’s social trigger is metabolic, not psychological — the same system that detects tissue damage detects social exclusion. This is load-bearing for the claim that Go stats have real physiological substrates.*

**SOC-LIE-PSR-01 `[MECHANISM]`**

**Claim:** The dorsal anterior cingulate cortex (dACC) responds to the subjectively distressing component of both social exclusion and physical pain. The dACC functions as a neural alarm system performing two computations: detecting a problem (conflict monitoring) and generating distress (affective alarm). The social attachment system is theorized to have piggybacked onto the pre-existing physical pain system during mammalian evolution to ensure social proximity for survival. The overlap is in the affective “hurt” component — not sensory localization, which remains modality-specific (somatosensory cortex for physical pain).

**Relevant to:** Withdrawal as Go stat, metabolic cost of threat detection, why social exclusion triggers physiological stress response, Go stats as capacity variables with real substrates

**Retrieval prompt:** “What specific evidence do Lieberman and Eisenberger cite for the dACC overlap between social and physical pain? Include the neuroimaging studies, the distinction between affective and sensory components, and the evolutionary piggybacking argument. What do they say about whether the overlap is in the alarm signal itself or in the downstream response?”

---

### **Koolhaas et al. (2017)**

*Structural note: Three distinct card-worthy findings from this paper. The controllability/predictability claim provides the mechanistic bridge between the animal social defeat literature and the existing SOC villain architecture (specifically, “the all-clear never arrives” in the Withdrawal ghosted row). The sleep/consolidation claim provides the acute-to-chronic conversion mechanism. The self-evaluation claim connects to Lewis’s shame internalization pathway.*

**SOC-KOO-SSM-01 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Controllability and predictability are the variables that determine whether a social encounter becomes a stressor. The physiological response to winning and losing a social contest is identical in magnitude; losers are distinguished by a recovery time nearly twice as long as victors. Uncontrollability is marked by a pronounced plasma adrenaline response and slow HPA/SAM recovery slope. Unpredictability is marked by the absence of anticipatory responses (no preparatory heart rate or adrenaline increase before the stimulus). The biomarker of pathological stress is the recovery profile, not the activation magnitude.

**Relevant to:** Withdrawal mechanism, villain table Withdrawal row (“the all-clear never arrives”), completion cycle resolve phase, why ghosting produces chronic activation

**Retrieval prompt:** “What specific physiological measures does Koolhaas use to distinguish controllable social challenge from uncontrollable social defeat? Include the recovery time comparison between winners and losers, the adrenaline response data, and the anticipatory response findings. What does the paper say about the role of predictability specifically — distinct from controllability?”

---

**SOC-KOO-SSM-02 `[MECHANISM]`**

**Claim:** Disrupted sleep and memory consolidation is the specific mechanism by which acute social defeat converts into chronic pathology. Glucocorticoids and catecholamines released during defeat act on the amygdala to enhance emotional memory consolidation. Sleep is essential for qualitative reorganization and storage of these memories. Disrupted or fragmented sleep leads to re-experiencing and rumination, which functions as repeated exposure to the stressor — effectively making a single event subjectively chronic.

**Relevant to:** Acute-to-chronic conversion, masking timescale-1 to timescale-2 transition, completion cycle (resolve signal never arrives → cycle stays open → consolidation fails), why single defeat events can produce lasting Withdrawal-stat shifts

**Retrieval prompt:** “What does Koolhaas say about the specific role of sleep in the transition from acute stress to chronic pathology? Include the amygdala consolidation mechanism, the re-experiencing loop, and any evidence about sleep quality as a moderating variable. Does the paper distinguish between sleep disruption caused by the stressor and sleep disruption as an independent risk factor?”

---

**SOC-KOO-SSM-03 `[MECHANISM]`**

**Claim:** The long-term pathological consequences of social defeat depend on the organism’s cognitive evaluation of its own coping efforts during the event. If the organism evaluates its actions favorably (“I did my best given my resources”), the appraisal remains relatively positive even after a loss. If the self-evaluation is negative (“I took the wrong decisions”), it triggers a downward spiral during memory consolidation that converts the memory of a single defeat into a lasting pathological state. This self-evaluation is a continuous process during and after the event, not a one-time judgment.

**Relevant to:** Lewis’s shame internalization pathway (convergence — same mechanism at neurobiological level), Withdrawal-stat calibration, self-assessed RHP / Formidability Index, why accurate self-assessment is protective

**Retrieval prompt:** “What does Koolhaas say about the role of cognitive self-evaluation in determining long-term outcomes of social defeat? Include the ‘downward spiral’ mechanism, the specific contrast between positive and negative self-evaluation, and any evidence about when this evaluation occurs relative to the defeat event. Does the paper connect this to coping style differences?”

---

### **Koolhaas et al. (2007)**

**SOC-KOO-IVC-01 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Individual appraisal of social stressors is determined by outcome expectancy built from prior experience. Proactive individuals operate on internalized predictions of success; when a proactive organism’s positive expectancy is violated (e.g., a dominant male loses territory), the violation itself — not the defeat — is the primary pathological trigger. Reactive individuals appraise based on direct environmental input and are more flexible. The match/mismatch between coping style and environmental demands predicts vulnerability: proactive individuals are resilient in stable environments that match their predictions, vulnerable in environments that violate them; reactive individuals show the reverse pattern.

**Relevant to:** Formidability Index / self-assessed RHP, why the same social defeat produces different Withdrawal-stat consequences depending on prior expectancy structure, individual differences in Withdrawal threshold, villain table (expectancy violation as specific attack vector)

**Retrieval prompt:** “What does Koolhaas 2007 say about the relationship between coping style and outcome expectancy? Include the specific evidence for proactive individuals’ reliance on predictions versus reactive individuals’ reliance on environmental input. What does the paper say about the ‘wrong prediction’ as a stressor — how does expectancy violation compare to simple defeat in terms of pathological outcome?”

---

### **Krishnan et al. (2007) / Nestler & Russo (2024)**

*Structural note: The resilience-as-active-adaptation finding is the strongest molecular evidence that Withdrawal is a stat with a settable threshold. Resilient animals don’t fail to be damaged — they build a novel compensatory mechanism. Nestler & Russo (2024) extends and confirms the 2007 findings without altering the core claim.*

**SOC-KRI-MRS-01 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Resilience to chronic social defeat stress is not the passive absence of damage but an active set of novel molecular adaptations. Resilient mice upregulate voltage-gated potassium channels (specifically Kcnq3) in the VTA, which compensates for stress-induced hyperexcitability by restoring normal dopamine neuron firing rates. This prevents excessive activity-dependent BDNF release into the nucleus accumbens, which otherwise drives the susceptibility phenotype (social avoidance, anhedonia). The resilient state is qualitatively different from both the pre-defeat state and the susceptible state — resilient animals show elevated anxiety and sensitized CORT reactivity but maintain social interaction through active homeostatic compensation.

**Relevant to:** Withdrawal as Go stat with settable threshold, active molecular resilience vs. absence of damage, asymptotic competency framing (resilient state \= qualitatively new \= “training again” not “restored”), Go-stat substrates

**Retrieval prompt:** “What specific molecular mechanisms does Krishnan et al. identify in resilient versus susceptible mice? Include the K+ channel data, VTA firing rates, BDNF signaling in the NAc, and the behavioral profile of resilient animals (what symptoms they do and don’t show). Does the paper address whether resilience is trait-like or induced by the defeat experience itself?”

---

### **Bagot et al. (2017)**

**SOC-BAG-KTR-01 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Ketamine’s therapeutic effect in socially defeated mice involves two concurrent molecular operations: (1) reversing susceptibility-associated transcriptional changes in PFC and NAc (normalizing disrupted gene expression including Dusp1, Arc, Htr1b), and (2) inducing resilience-specific gene expression profiles not seen in controls, particularly in PFC (including the hub gene Zfp189, enriched in signal transduction and protein kinase regulation). Both operations are detected at 24 hours post-dose in treatment responders and appear concurrent rather than sequential. Both operations are best understood as restoring and enhancing the capacity of regulatory systems — the PFC contribution is executive capacity to maintain emotional homeostasis, not selection of a different behavioral strategy.

**Relevant to:** Two Go-level recovery operations (restore \+ harden), Withdrawal-stat restoration mechanism, why recovery ≠ returning to baseline, Go capacity as prerequisite for downstream behavioral change

**Retrieval prompt:** “What specific transcriptional changes does Bagot identify in ketamine responders versus non-responders? Include the PFC and NAc regional specificity, the comparison between ketamine and imipramine, the Zfp189 hub gene finding, and the distinction between reversing susceptibility and inducing resilience. Does the paper address the timecourse — do both operations happen simultaneously?”

---

### **Williams & Nida (2011) / Hartgerink et al. (2015)**

**SOC-WIL-OST-01 `[MECHANISM] [FRAMING MOVE]`**

**Claim:** Williams’ temporal need-threat model distinguishes three qualitatively different stages of response to social exclusion. The reflexive stage (seconds to minutes) threatens belonging, self-esteem, control, and meaningful existence simultaneously and indiscriminately; even minimal exclusion (Cyberball) produces this effect. The reflective stage involves appraisal and coping — if reinclusion seems possible, belonging and self-esteem drive prosocial repair behavior; if reinclusion seems unlikely, control and meaningful existence drive antisocial assertion. The resignation stage (weeks to months of chronic exclusion) involves complete depletion of coping resources, producing alienation, helplessness, depression, and “social death” where the message of insignificance is internalized. These three stages are qualitatively distinct, not quantitatively. Hartgerink et al.’s meta-analysis confirms the reflexive effect is large but decreases over the session as coping engages.

**Relevant to:** Vitality-level phenomenology (not Withdrawal-level mechanism), masking timescales (reflexive \= timescale-1 acute taxation, reflective \= coping under reduced Vitality, resignation \= timescale-3 identity erosion), niche constriction at social-exclusion scale

**Retrieval prompt:** “What does Williams say about the specific behavioral differences between the reflexive, reflective, and resignation stages? Include the Cyberball evidence for the reflexive stage, the reinclusion-possible vs. reinclusion-unlikely distinction in the reflective stage, and the specific symptoms of the resignation stage. What does Williams say about what distinguishes resignation from depression?”

---

### **Essex et al. (2011)**

**SOC-ESS-ELS-01 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Early life stress (specifically maternal depression and family-expressed anger) programs the HPA axis through a combination of resetting the homeostatic set-point (trait-like basal cortisol levels) and altering receptor sensitivity to episodic challenges. The programming manifests as either sustained hyper-arousal or hypo-arousal depending on ELS type, and persists after the stressor is removed. These alterations are described as “molecular scars” (e.g., DNA methylation) established early and remaining stable into adolescence. The long-term signature is a delayed recovery trajectory of HPA axis response — the same biomarker Koolhaas identifies for uncontrollable stress.

**Relevant to:** Go-stat baseline calibration by developmental environment, Abdi’s open calibration windows, epigenetic persistence vs. Go trainability (sets starting conditions for asymptotic curve, doesn’t cap the curve), convergence with Koolhaas recovery-profile biomarker

**Retrieval prompt:** “What specific measures does Essex use to track HPA axis changes from childhood to adolescence? Include the cortisol data, the distinction between maternal depression and family anger as different types of ELS, and the evidence for persistence after stressor removal. Does the paper address whether the programming is reversible?”

---

### **Ostlund & Pérez-Edgar (2023)**

**SOC-OPE-THM-01 `[MECHANISM] [FRAMING MOVE]`**

**Claim:** A two-hit model explains the transition from temperamental behavioral inhibition (BI) to anxiety disorder. The first hit (gestation/infancy) tunes attentional and affective systems toward hypervigilance, creating the BI phenotype. The second hit (adolescence) is a genuinely new calibration event, not activation of dormancy — adolescence involves neural reorganization and pubertal maturation that reopens a window of plasticity for stress-mediated system recalibration. The second hit uniquely taxes BI-linked vulnerabilities because it demands navigation of novel social roles and complex peer relationships. Childhood social stressors do not tax the same circuits in the same qualitatively distinct manner. The probability of developing anxiety via the BI pathway is specifically heightened when the second hit arrives during the adolescent window.

**Relevant to:** Abdi’s calibration windows, developmental sensitive periods, adolescence as genuine second calibration window (connects to existing BIO/COMP adolescent sensitive-period cards), why Abdi’s current social environment is high-leverage, two-hit architecture for Go-stat programming

**Retrieval prompt:** “What does Ostlund & Pérez-Edgar say about why adolescence specifically — rather than childhood or adulthood — is the critical period for the second hit? Include the neural reorganization evidence, the pubertal maturation argument, and the specific claim that childhood stressors are qualitatively different. Does the paper predict anything about what happens if the second hit is delayed past adolescence?”

---

### **Milewski et al. (2022)**

*Structural note: Four cards from this source. Milewski provides the only material in this notebook about the standing costs of social position — as opposed to the costs of losing or acquiring position. The hierarchy-maintenance findings connect the defeat literature (what happens when you lose) to the niche constriction framework (what happens when you stay).*

**SOC-MIL-BPP-01 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Maintaining dominant rank is a continuous metabolic expenditure, not a one-time acquisition cost. Dominant animals pay ongoing costs through aggression, territorial defense, and status signaling — including energetically expensive honest signals like major urinary proteins (MUPs) in mice, which require increased food and water intake to sustain. Dominance maintenance becomes cheaper once hierarchies stabilize (aggression peaks during formation, shifts to affiliation afterward). However, organisms in contested or unstable hierarchies pay significantly higher physiological costs, including chronic hypercortisolemia and increased risk of cardiovascular pathology, regardless of whether they are dominant or subordinate.

**Relevant to:** Go stats as capacity variables with real metabolic costs, contested vs. stable environments as a variable in Go-stat expenditure, why unstable social environments are more metabolically expensive at every rank

**Retrieval prompt:** “What specific evidence does Milewski cite for the metabolic cost of dominance maintenance? Include the MUP data, the aggression-to-affiliation shift in stable hierarchies, and the glucocorticoid comparison between stable and unstable hierarchies. Does the paper quantify the difference in cost between stable and contested rank?”

---

**SOC-MIL-BPP-02 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Subordinate animals exhibit significantly delayed HPA axis and SAM recovery after social conflict compared to dominant animals — the same biomarker Koolhaas (2017) identifies for uncontrollable stress. This means sustained subordination is functionally equivalent to repeated social defeat without a recovery window: each daily interaction produces the slow-recovery profile, and the next interaction arrives before recovery is complete. This convergence with the acute-defeat literature suggests subordination and defeat operate through the same mechanism at different timescales — episodic for defeat, continuous for subordination.

**Relevant to:** Withdrawal mechanism (convergence with Koolhaas SSM-01), chronic vs. acute social stress, masking timescale-2 (allostatic damage from sustained subordination), completion cycle (recovery signal never arrives because the next stressor arrives first)

**Retrieval prompt:** “What does Milewski say about the physiological recovery profiles of dominant versus subordinate animals after social conflict? Include the HPA and SAM recovery data, and any evidence about whether subordinates ever fully recover between interactions. Does the paper discuss the cumulative effect of incomplete recovery?”

---

**SOC-MIL-BPP-03 `[MECHANISM] [FRAMING MOVE]`**

**Claim:** The subordinate phenotype is adaptive in the short term: inhibiting the Core Aggression Circuit and adopting submissive postures avoids injury; increased social vigilance enables identification of opportunistic mating; reproductive suppression (HPG axis downregulation) redirects energy into somatic growth, potentially preparing for future rank challenge. The adaptive value reverses gradually through allostatic load — the HPA axis makes progressively wider swings around its set-point to maintain stability through change, and the cumulative metabolic cost of these adjustments eventually exceeds the survival benefit. There is no discrete tipping point; costs accumulate monotonically while the organism’s capacity to change its situation deteriorates because subordination suppresses the very systems (aggression, exploration) needed to exit.

**Relevant to:** Niche constriction (real goods purchased: survival, injury avoidance; capabilities lost: aggression, exploration; trade-off deteriorates without visible threshold), substitution ratchet (structural parallel — the system uses degraded versions of the organism’s own architecture), allostatic load as masking timescale-2

**Retrieval prompt:** “What specific adaptive benefits does Milewski identify for the subordinate phenotype? Include the Core Aggression Circuit inhibition, the sneaky mating evidence, and the somatic growth redirection. What does the paper say about the timeline over which adaptive subordination becomes maladaptive — is there a threshold or is it gradual? Does the paper discuss whether the organism can detect the transition?”

---

**SOC-MIL-BPP-04 `[MECHANISM] [EVOLUTIONARY]`**

**Claim:** Subordinate organisms redirect energy from reproduction into somatic growth and social vigilance as a survival strategy, with the implicit temporal bet that current restraint enables future challenge for higher rank. This energy redirection is functionally equivalent to Withdrawal operating adaptively — the system prioritizes threat detection and conservation over engagement and output. Pathology begins not when the strategy is adopted but when the “later” never arrives: chronic subordination erodes the capacity (aggression circuits, exploratory behavior, HPG axis) that would be required to execute the deferred challenge, trapping the organism in a phenotype that was designed to be temporary.

**Relevant to:** Withdrawal as Go stat (not pure pathology — functional at appropriate levels), Nettle’s trade-off logic for Neuroticism (convergence: selection maintains non-zero Withdrawal because volatile ecologies reward vigilant phenotype; cost \= burnout in stable environments), asymptotic competency framing (subordinate who successfully redirects into growth is training; one stuck in chronic subordination has stopped training)

**Retrieval prompt:** “What does Milewski say about the temporal structure of the subordinate strategy — is there evidence that organisms ‘plan’ to challenge later, or is the somatic growth an automatic byproduct of reproductive suppression? Does the paper discuss cases where the subordinate phenotype successfully transitions back to dominance — what enables the transition and what prevents it?”

---

### **Hagen (2011)**

**SOC-HAG-ETD-01 `[EVOLUTIONARY] [FIELD STATUS]`**

**Claim:** Three evolutionary theories frame Major Depressive Disorder as functional rather than purely pathological: the social competition hypothesis (depression as involuntary subordinate strategy), the analytical rumination hypothesis (anhedonia as functional single-minded focus — suppresses normal activities to divert cognitive resources toward analyzing the triggering social problem), and the credible signaling hypothesis (suicidality as costly “cry for help” that demonstrates genuine need through high-risk gamble). These are best understood as describing different facets of one condition responding to different types of adversity (situation-symptom congruence), not as competing accounts. However, there is currently no empirical evidence that depressive symptoms themselves successfully produce the life improvements any of these theories predict. Most evolutionary scholars still categorize severe clinical presentations as system failures where healthy mechanisms become dysregulated.

**Relevant to:** Withdrawal as functional Go stat vs. Withdrawal pathology boundary, evolutionary justification for non-zero Withdrawal, limitations of purely adaptationist framing of depression

**Retrieval prompt:** “What specific evidence does Hagen cite for and against each evolutionary theory of depression? Include the situation-symptom congruence hypothesis, the evidence gap regarding whether symptoms produce improvements, and Hagen’s own assessment of which theory is best supported. Does the paper distinguish between mild/moderate depression (potentially functional) and severe MDD (potentially system failure)?”