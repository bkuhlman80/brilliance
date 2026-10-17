# **Evolutionary Personality**

**Source manifest:** NotebookLM responses (Prompts 1, 5, 8, 9, and two follow-ups on cognitive bridge and depression process-level) pasted by Brian. Source library: Dick (2011), Yarkoni (2015), Seyfarth & Cheney (2009), Boon, Réale, & Boutin (2007), Delgado & Sulloway (2017), Nettle (2006), Figueredo et al. (2005), Millon (2011), Kenrick et al. (2010), Koepke, Gray, & Pepperberg (2015), Addessi et al. (2013), Michalski & Shackelford (2010), Hagen (2011). Access method: \[notebooklm extraction returns pasted by brian\]. BIO doc fetched via google\_drive\_fetch this conversation. Duplicate-checked — no existing cards from Dick, Yarkoni, Seyfarth/Cheney, Boon, or Delgado/Sulloway in BIO.

**Placement note:** Most cards go in BIO. Two Yarkoni cards are placed in COMP (cognitive bridge material). Book Content entries document Brian’s synthesis moves.

---

## **Source: Dick (2011), “Gene-Environment Interaction in Psychological Traits and Disorders”**

Author code: DIC  
 Book abbreviation: GEI  
 Bucket: BIO

---

**BIO-DIC-GEI-01 \[MECHANISM\] \[EMPIRICAL\]**

**Claim:** Four landmark studies demonstrate gene-environment interaction for personality-relevant traits: (1) MAOA × maltreatment: a functional polymorphism in the MAOA gene moderated the impact of childhood maltreatment on antisocial behavior in a New Zealand birth cohort — males with high-expression MAOA genotypes were significantly less likely to develop antisocial problems after maltreatment than those with low-expression genotypes (Caspi et al.). (2) 5-HTT × stressful life events: the short allele of the serotonin transporter gene predicted more depressive symptoms and suicidality in response to stress than the long allele (Caspi et al.). (3) Maze-bright/maze-dull rats: enriched environments improved maze-dull rats’ performance but not maze-bright rats’; restricted environments degraded maze-bright but not maze-dull (Cooper & Zubek 1958). (4) GABRA2 × parental monitoring: genetic risk for substance use and externalizing behavior was significantly enhanced in environments with low parental monitoring.

**Relevant to:** Parameterized generalism (GxE is what happens when genetic parameters meet environmental input — same gene, different environment, different phenotype), developmental calibration (BIO-ELL-ACM-01 through 03 — ACM switch points are the windows during which GxE calibration occurs), the maze-bright/dull finding as a clean animal demonstration of what HPAM calls “same architecture, different parameters, different output”

**Retrieval prompt:** “What are the four landmark GxE studies Dick reviews? For each, include the gene, the environmental moderator, the behavioral outcome, and the direction of interaction. Include Caspi’s MAOA/maltreatment, Caspi’s 5-HTT/stress, Cooper & Zubek’s maze-bright/dull, and the GABRA2/parental monitoring finding. What are the sample sizes for the human studies?”

**Caveat (from general training knowledge, not from this notebook):** The Caspi MAOA and 5-HTT findings are famous but also famously contested in replication — subsequent meta-analyses have produced mixed results. HPAM should cite these as influential demonstrations of the GxE concept, not as settled findings. The GxE architecture is well-established; these specific gene-environment pairings are less certain than the original publications suggested.

---

**BIO-DIC-GEI-02 \[COUNTERPOINT\] \[FIELD STATUS\]**

**Claim:** The methodology for detecting GxE breaks down in several systematic ways: (1) Small sample sizes and low power — many GxE studies, especially neuroimaging (typically n \< 30), are underpowered, producing an “illusion of selectivity” where weak, widely distributed effects appear as strong, localized ones. (2) Restricted environmental range — measuring only the absence or presence of a stressor (rather than the full spectrum from highly supportive to highly aversive) may misidentify a crossover interaction (differential susceptibility) as a fan-shaped interaction (diathesis-stress). (3) Selected samples — adoption studies suffer from selective placement that confounds genetic and environmental separation. (4) Gene-environment correlation (rGE) confounds — many things treated as “environmental” are themselves under genetic influence (e.g., a sensation-seeking person actively seeking out risky environments), making it difficult to determine whether the environment is a true moderator or a downstream consequence of the genotype. (5) Scaling artifacts — fan-shaped interactions can vanish entirely under log transformation, raising questions about whether the interaction is biological or metric. (6) Statistical noise in additive models — standard regression can produce significant GxE even when the true model is purely additive, especially with logistic regression for dichotomous outcomes. (7) Overfitting — regression lines may cross at environmental extremes purely as artifacts of concentrated data.

**Relevant to:** Epistemic hygiene for any HPAM claim citing GxE evidence (how much weight to put on any specific GxE finding), the rGE confound as particularly important for HPAM (the corresponsive principle means people select environments matching their genotype — what looks like GxE may be rGE), the illusion of selectivity as a general warning about small-sample neuroimaging studies (relevant beyond GxE to any neuroimaging claim in BIO)

**Retrieval prompt:** “What are the main methodological problems Dick identifies for GxE detection? For each, include the specific bias, the direction of error (does it inflate or deflate GxE estimates?), and any proposed solutions. Include the illusion of selectivity, restricted environmental range, rGE confound, scaling artifacts, and the additive-model false-positive problem.”

---

**BIO-DIC-GEI-03 \[MECHANISM\] \[FRAMING MOVE\]**

**Claim:** Gene-environment correlation (rGE) and gene-environment interaction (GxE) are distinct processes that are frequently conflated. rGE occurs when an individual’s genotype influences their exposure to environments — the genotype shapes the environment before the environment acts back on the genotype. Three types follow a developmental sequence: passive rGE (parents provide both genes and environment), evocative rGE (the child’s traits elicit environmental responses), and active rGE (the individual selects environments matching their genotype). Epigenetics — the biological mechanism by which environmental signals regulate gene expression through DNA methylation and histone modification — is a distinct process from statistical GxE interaction. Epigenetics describes how the environment changes gene activity within an individual; GxE describes how the same genotype produces different phenotypes across different environments. Both are real; they are not the same thing.

**Relevant to:** Existing BIO “Gene-Environment Correlation: Developmental Sequence” section (Dick’s framing converges with the existing Briley & Tucker-Drob / Kandler material but adds the GxE/rGE/epigenetics three-way distinction), conceptual clarity for the book (Katie needs to understand why “it’s in your genes” and “it’s your environment” are both wrong framings — the interaction is the unit, not either component alone)

**Retrieval prompt:** “How does Dick distinguish between rGE, GxE, and epigenetics? Include the three types of rGE, a concrete example of each, and the specific argument for why epigenetics is not the same as statistical GxE. Does she propose criteria for determining which process is operating in a given dataset?”

---

## **Source: Yarkoni (2015), “Neurobiological Substrates of Personality: A Critical Overview”**

Author code: YAR  
 Book abbreviation: NPS  
 Bucket: BIO (critique cards), COMP (cognitive bridge card)

---

**BIO-YAR-NPS-01 \[COUNTERPOINT\] \[FIELD STATUS\]**

**Claim:** Yarkoni identifies three structural problems with “grand models” that attempt direct trait-to-substrate mapping in personality neuroscience: (1) Lack of specificity — biological mechanisms are rarely trait-specific. Cloninger linked Novelty Seeking specifically to dopamine, but research shows the trait is also associated with serotonergic, noradrenergic, and cannabinoid systems; conversely, serotonin alone is implicated in negative affect, aggression, and impulsivity. (2) Biological redundancy and non-linearity — real biological systems are rife with redundancy and non-linear interactions, making it implausible that they would “respect” psychometric models like the Big Five. (3) The inverse problem — an infinite number of causal models can produce any given pattern of correlational data, so identifying a correlation between a trait and a brain region does not prove the psychometric model has carved nature at its joints. Additionally, the “illusion of selectivity” from small neuroimaging samples (typically n \< 30\) produced inflated effect sizes that failed to replicate. And a conceptual error of “implicit dualism” treats high heritability as indicating a “stronger biological basis,” when in fact 100% of reliable behavioral variance must be mediated through biological mechanisms — heritability doesn’t make a trait more or less biological.

**Relevant to:** HPAM positioning (HPAM is a comprehensive model — it needs to know exactly what critics object to so it can show why it survives the critique), existing BIO Pharmacological Predictions table (Yarkoni’s lack-of-specificity point is a direct challenge to mapping individual transmitters to individual stats), the “implicit dualism” point is useful for the book (Katie may assume more heritable \= more biological; this corrects that), BIO-DEY-NPE-01 (DeYoung’s serotonin-Stability / dopamine-Plasticity framework is the kind of mapping Yarkoni would critique — the question is whether it survives at the metatrait level even if trait-level mapping fails)

**Retrieval prompt:** “What are Yarkoni’s three strongest arguments against grand models of personality neuroscience? Include the lack-of-specificity examples (Cloninger’s Novelty Seeking, serotonin across multiple traits), the inverse problem argument, and the implicit dualism critique. Does he acknowledge any version of a comprehensive model that might survive these objections?”

---

**BIO-YAR-NPS-02 \[MECHANISM\] \[FRAMING MOVE\]**

**Claim:** Yarkoni identifies misinterpretation of brain plasticity as a systematic error in personality neuroscience. Structural brain differences (e.g., extraverts having more gray matter in social-processing regions, as found in VBM studies) are often treated as evidence for stable, innate biological substrates of personality. But because the brain is plastic, observed structural differences may be epiphenomenal byproducts of behavior — practice effects from years of differential engagement — rather than causes of the personality trait. The same logic applies to white matter differences: someone who has spent decades practicing social engagement may show different myelination patterns than someone who hasn’t, without the myelination being the cause of the engagement. Millon, from a different angle, argues that the “patchwork quilt” of personality data cannot be organized through “brute empiricism” or the piecemeal summing of evidence — without a transcendent theory, symptomatic events are classified according to arbitrary similarity rather than underlying biological order.

**Relevant to:** BIO-VAR-CTX-01 (cortical territory allocation through use — Yarkoni’s plasticity point is the flip side: structural differences reflect use history, not just innate architecture), the “chicken and egg” problem for any neuroimaging personality claim, Millon’s “brute empiricism” critique as convergent from clinical side

**Retrieval prompt:** “What specific examples does Yarkoni give of structural neuroimaging findings that could be practice effects rather than innate substrates? Include the VBM gray matter findings and any white matter examples. What alternative research strategies does he propose that would avoid the plasticity confound?”

---

## **Source: Yarkoni (2015) — COMP placement**

---

**COMP-YAR-NPS-01 \[MECHANISM\] \[FRAMING MOVE\]**

**Claim:** Yarkoni endorses a “cognitive bridge” approach as the most productive current strategy for personality neuroscience — mapping psychometric traits onto abstract information-processing mechanisms, which are then mapped onto plausible neurobiological substrates. Two concrete examples: (1) Neuroticism decomposed into intermediate cognitive mechanisms: increased perceptual sensitivity to threats, stronger emotional responses to stressors, difficulty disengaging attention from perceived threats, and faster aversive conditioning. These mechanisms then map downward to gray matter volume in limbic regions, CRH system function, and functional coupling between object-recognition and limbic circuits. (2) Impulsivity decomposed via active maintenance of long-term goal representations, known to rely on prefrontal cortical mechanisms, contributing to the facets of perseverance and premeditation — while “reactivity to negative stimuli” (a different mechanism) increases urgency while simultaneously decreasing sensation-seeking, showing how mechanisms cut across trait boundaries. The approach is described as the “most productive” current strategy but explicitly not a fully worked-out model — it establishes “mutual, but relatively weak, constraints” between levels of analysis. The Extraversion → variation in reactivity to positive stimuli mapping is already widely accepted as an instance of this approach.

**Relevant to:** HPAM positioning (HPAM’s Go/Turn architecture IS a cognitive bridge — mapping psychometric traits onto computational mechanisms, then mapping those onto neurobiology; Yarkoni describes the strategy, HPAM builds the architecture), the cross-cutting finding (reactivity to negative stimuli increasing urgency while decreasing sensation-seeking is exactly the kind of cross-trait influence that HPAM’s stats-not-traits approach handles), existing COMP Go/Turn architecture (the cognitive bridge is what HPAM does — Go stats are intermediate capacity mechanisms, Turn modes are intermediate routing mechanisms, both mapped upward to traits and downward to biology)

**Retrieval prompt:** “How developed is Yarkoni’s cognitive bridge concept? Include the two concrete examples (Neuroticism and Impulsivity decomposition), the specific intermediate mechanisms named, and the downward biological mappings. Does he cite other researchers who have implemented this approach, or is it his proposal? What does he mean by ‘mutual, but relatively weak, constraints’ between levels?”

---

## **Source: Seyfarth & Cheney (2009), “Affiliation, Empathy, and the Origins of Theory of Mind”**

Author code: SEY  
 Book abbreviation: AET  
 Bucket: BIO

---

**BIO-SEY-AET-01 \[EMPIRICAL\]**

**Claim:** In a population of wild female baboons studied over multiple years, three stable personality styles — “Nice” (high affiliation, frequent use of benign-intent signals like grunts), “Aloof” (high dominance, lower affiliation), and “Loner” (low affiliation, low dominance) — predicted the strength of social bonds as measured by Composite Sociality Index (CSI) and Partner Stability Index (PSI). Nice females formed the strongest and most stable bonds. Longevity and offspring survival were significantly correlated with bond strength metrics, creating a personality → bond quality → fitness chain. Nice females were specifically better at responding to social challenges (such as the immigration of a potentially infanticidal male) because their existing bond networks provided collaborative defense. Loner females failed to rebuild social networks after the death of a close relative, showing that the personality style constrained recovery from social loss.

**Relevant to:** Compassion Go stat (Nice style maps onto high Compassion — benign-intent signaling, bond formation, collaborative defense), fitness consequences of personality variation in wild populations (quantified through bond metrics → survival/longevity), niche repair constraints (Loner style constraining social recovery parallels HPAM’s claim that some routing configurations limit the available recovery paths), existing BIO-NET-PER-05 (Nettle’s Agreeableness trade-off — Seyfarth/Cheney provide the field data with actual fitness numbers that Nettle describes in theoretical terms)

**Retrieval prompt:** “What specific fitness metrics do Seyfarth and Cheney report for each baboon personality style? Include the CSI and PSI scores by style, the longevity correlation, the offspring survival data, and the social challenge response. What is the sample size and study duration? Do they report fitness differences between Nice and Aloof styles specifically, or only between Nice/Aloof and Loner?”

---

## **Source: Boon, Réale, & Boutin (2007), “The Interaction Between Personality, Offspring Fitness and Food Abundance in North American Red Squirrels”**

Author code: BOO  
 Book abbreviation: IPO  
 Bucket: BIO

---

**BIO-BOO-IPO-01 \[EMPIRICAL\]**

**Claim:** In wild North American red squirrels, maternal personality traits predicted offspring fitness outcomes, but the direction of prediction reversed depending on yearly food abundance (spruce cone mast years). Maternal activity levels were significantly correlated with offspring mass gain (g/day) while in the nest — but more active mothers had faster-growing offspring following high-cone years and slower-growing offspring following low-cone years. Maternal aggressiveness showed a different pattern: it often correlated negatively with offspring survival in the nest but positively with offspring survival through the first winter. This means the same trait is simultaneously costly in one fitness window and beneficial in another, within the same individual and the same reproductive event.

**Relevant to:** Fluctuating selection as maintenance mechanism (the direction of the fitness effect reverses with food abundance — no single activity level is unconditionally optimal), within-individual trade-off (aggressiveness simultaneously costly and beneficial at different timescales — this is a more precise version of Nettle’s theoretical trade-off argument with actual field data), existing BIO-NET-EPV-01 (deepens Nettle’s cross-species trade-off examples with quantified fitness data from a specific study), existing BIO Book Content on Zietsch non-engagement strategy (the phenotypic trade-off is real and measured regardless of which genetic maintenance mechanism is operating)

**Retrieval prompt:** “What specific fitness metrics did Boon, Réale, and Boutin measure for offspring of mothers with different personality profiles? Include the mass gain data (g/day), the nest-survival vs. winter-survival distinction for aggressiveness, and the food-abundance interaction for activity. What was the sample size and number of years of data?”

---

## **Source: Multiple sources — Great tit fluctuating selection and bluegill frequency-dependent selection**

---

**BIO-VAR-EFS-01 \[EMPIRICAL\]**

**Claim:** Two field studies provide the cleanest demonstrations of distinct evolutionary maintenance mechanisms for personality variation: (1) Great tits — exploration score (bold vs. shy) predicts survival probability, but the direction of the effect reverses by sex AND by food availability. In scarce years, bold females survive better (competing effectively for resources) while shy males survive better (avoiding costly aggressive encounters). In abundant years, the pattern flips: shy females survive (avoiding unnecessary aggression) while bold males thrive (defending territories against many surviving fledglings). This is fluctuating selection with a sex × environment interaction. (2) Bluegill sunfish — “cuckolder” males (who sneak into nests) have high reproductive success when rare but declining fitness as they become more common, favoring “parental” males instead. This is negative frequency-dependent selection where the fitness of a strategy is causally determined by its frequency in the population, not by environmental conditions.

**Relevant to:** Evolutionary maintenance of variation (two distinct mechanisms demonstrated with specific field data), existing BIO-NET-EPV-01 (great tits mentioned briefly as illustration — this card provides the sex-by-year reversal detail and fitness numbers Nettle’s summary lacks), existing BIO-BRI-NFC-01 (Brisson’s NFDS critique — the bluegill sunfish is a case where true frequency-dependent selection, not multi-niche selection, appears to operate), the sex × environment interaction as particularly sharp data (no single boldness level is optimal across both sexes and both food conditions — four-way trade-off matrix)

**Retrieval prompt:** “What specific survival data are reported for great tits by exploration score, sex, and food availability? Include the reversal pattern across scarce vs. abundant years, the sample sizes and study duration, and whether the effect holds after controlling for other variables. For bluegill sunfish, what is the specific relationship between cuckolder frequency and reproductive success — is it linear decline or threshold?”

---

## **Source: Delgado & Sulloway (2017), “Domains of Conscientiousness Throughout the Animal Kingdom”**

Author code: DGS  
 Book abbreviation: ACK  
 Bucket: BIO

---

**BIO-DGS-ACK-01 \[EMPIRICAL\] \[EVOLUTIONARY\]**

**Claim:** A systematic review identifies nine distinct behavioral facets of conscientiousness across the animal kingdom — including achievement striving, orderliness, and self-discipline — that had been previously overlooked because conscientiousness was assumed to be uniquely human or primate. The distribution of these facets across taxa closely parallels known phylogenetic relationships, suggesting deep evolutionary origins rather than convergent evolution. Specifically: orderliness in nest-building in Darwin’s finches predicts mate attraction and reproductive success, and colony-level fitness in honeybees (measured by weight gain, comb production, and number of reared young) is predicted by worker hygiene behavior — an orderliness facet. The phylogenetic distribution pattern suggests a single deep origin for conscientiousness-related behavioral facets, with increasing complexity in more recently evolved lineages.

**Relevant to:** Deep rootedness of personality variation (conscientiousness isn’t a human cultural invention — it has phylogenetic depth), existing BIO-DEY-NPE-03 (DeYoung’s claim that C is phylogenetically recent and limited to bonobos/chimpanzees among primates — Delgado/Sulloway challenge this by finding C-like facets across much broader taxa, though the full C dimension may still be uniquely hominid), existing BIO animal personality section (Réale et al., van Oers & Sinn — confirmatory material, but Delgado/Sulloway add the underrecognized conscientiousness facets specifically), Yarkoni’s phylogenetic facet analysis (COMP-YAR-NPS-01 follow-up — this is an instance of building biologically grounded personality models from cross-species facet data)

**Retrieval prompt:** “What nine facets of conscientiousness do Delgado and Sulloway identify across the animal kingdom? For each, include the taxa where it’s been documented, the behavioral measure used, and whether the fitness consequence has been quantified. What is the phylogenetic distribution pattern — does it follow a gradient from simpler to more complex facets across the evolutionary tree?”

---

## **Source: Figueredo et al. (2005), “Evolutionary Personality Psychology”**

Author code: FIG  
 Book abbreviation: EPY  
 Bucket: BIO

---

**BIO-FIG-EPY-01 \[MECHANISM\] \[FRAMING MOVE\]**

**Claim:** Figueredo et al. propose a “K-Factor” — a latent variable representing general life history speed — that correlates with traditional personality traits. Slow LH strategy (high K) correlates with higher Agreeableness, Conscientiousness, Emotional Stability, and Openness; fast LH strategy (low K) correlates with their opposites. The K-Factor is treated as a single dimension underlying correlations between personality, cognitive abilities, and reproductive strategies. However, the empirical basis for treating life history as a single dimension (rather than multiple independent trade-offs) is contested — the K-Factor may reflect shared method variance from self-report instruments or a general evaluative factor rather than a genuine biological dimension.

**Relevant to:** Existing BIO Life History Theory section (Ellis & Del Giudice harshness/unpredictability — Figueredo adds the K-Factor as a proposed integrative dimension), existing BIO-ELL-ACM-02 (ACM maps Slow LH onto Sensitive/Buffered and Fast LH onto Vigilant/Unemotional — the K-Factor is the latent variable version of that mapping), the single-dimension question matters for HPAM (if K is real, it converges with Vitality as a general factor; if K is an artifact, HPAM’s multi-stat architecture is better positioned than a single-factor model)

**Retrieval prompt:** “What evidence does Figueredo cite for the K-Factor as a single dimension? Include the specific personality-trait correlations, the cognitive ability correlations, and the reproductive strategy associations. What are the strongest critiques of treating life history as a single dimension — include the method variance concern and any factor-analytic challenges?”

---

## **Source: Multiple sources — Evolutionary maintenance mechanisms taxonomy**

---

**BIO-VAR-EMM-01 \[FRAMING MOVE\] \[FIELD STATUS\]**

**Claim:** The literature distinguishes four mechanisms that could maintain heritable personality variation: (1) Selective neutrality — variation has no fitness impact, maintained as noise. Largely rejected for major personality dimensions because Big Five traits demonstrably predict mating success, health, and longevity. (2) Mutation-selection balance — selection depletes deleterious variants but new mutations replenish them. Supported for traits unidirectionally correlated with fitness (intelligence: higher is always better, yet variation persists). (3) Fluctuating selection — optimal trait values change across time and space, maintaining variation because no single setting is always best. Supported by great tit survival reversals and squirrel offspring fitness reversals. (4) Frequency-dependent selection — fitness depends on trait frequency in population, not on absolute environment. Supported by bluegill sunfish cuckolder data. These mechanisms are not mutually exclusive: a trait like Extraversion might be maintained in the normal range by fluctuating selection and trade-offs while extreme values are influenced by mutation load, resulting in stabilizing selection at the tails. Environmental sensitivity (differential susceptibility) creates crossover effects where the same genotype is most successful in supportive environments and most dysfunctional in stressful ones.

**Relevant to:** Existing BIO-ZIE-BSM-01 (Zietsch argues for mutation-selection balance over balancing selection — this card provides the full landscape of mechanisms), existing BIO-PEJ-EGP-02 (Penke & Jokela reconciliation — compatible with simultaneous mechanisms), the simultaneous-mechanisms framing as most useful for HPAM (the phenotypic trade-offs survive regardless of which mechanism is operating), existing BC “HPAM doesn’t need to win the Zietsch argument” (this card provides the evidence base that BC rests on)

**Retrieval prompt:** “What evidence distinguishes each evolutionary maintenance mechanism for personality variation? For each mechanism, include the type of evidence required to confirm it, a specific example from the animal or human literature, and whether the mechanism has been definitively confirmed for any personality dimension. What does the simultaneous-mechanisms hypothesis predict about trait distributions?”

## **(SOC) Tooby & Cosmides, “Friendship and the Banker’s Paradox” (1996)**

*Structural note: This paper provides the evolutionary specification for why niche fit → deep friendship → survival insurance. It fills the SOC bucket’s thinnest spot: the mechanism connecting personality-environment match to social embeddedness. The five irreplaceability mechanisms are essentially an evolutionary user manual for healthy Turn-stat expression.*

---

**SOC-TOO-BKP-01 \[EVOLUTIONARY\] \[MECHANISM\]**

**Claim:** The Banker’s Paradox — individuals need help most when they’re the worst credit risks — creates selection pressure for deep friendship as a counter-strategy to desertion. If an individual makes themselves irreplaceably valuable to specific others, those partners gain a selfish stake in the individual’s survival regardless of repayment capacity. “True” friends help not from a ledger but because they cannot afford to lose the unique benefits the individual provides. This differs from reciprocal altruism: reciprocity is contingent exchange (tit-for-tat), while irreplaceability is association value. A partner helps you in crisis because your continued existence is necessary for their own welfare. Explicit ledgers or immediate offers of repayment are felt as shallow engagement — a signal that the bond is contingent, not deep.

**Relevant to:** Niche fit (irreplaceability is the fitness payoff of occupying a unique social niche), Turn stats (routing preferences are what make a person non-fungible — a Specialist build is harder to replace than a Generalist), Katie’s alienation (she interacts through contingent exchange, not deep bonds), restoration logic (the friendship-generating system is intact; the inputs are missing)

**Retrieval prompt:** “What is the Banker’s Paradox and how does it create selection pressure for deep friendship rather than reciprocal altruism? Include the credit-risk logic, the distinction between contingent exchange and association value, and the phenomenology of friendship where explicit repayment signals shallow engagement.”

---

**SOC-TOO-BKP-02 \[MECHANISM\]**

**Claim:** Tooby & Cosmides propose five cognitive mechanisms evolved to make individuals irreplaceable: (1) an appetite for individuality — a drive to be recognized for unique Domains; (2) niche monitoring — tracking which of one’s own Domains are valued by others but hard to obtain elsewhere; (3) product-differentiation — cultivating specialized skills or habitual activities that increase relative irreplaceability; (4) strategic association — seeking social groups where one’s specific Domain package is most indispensable; (5) social rivalry — jealousy toward others who develop similar abilities, threatening one’s niche uniqueness. The mind seeks to “product-differentiate” the self by honing skills one does relatively well compared to the local group, ensuring a unique starting position.

**Relevant to:** Turn-stat expression (product-differentiation \= Specialist build leaning into niche; strategic association \= seeking environment-routing match), niche monitoring as a social self-assessment mechanism, social rivalry as niche-protection (not pathology), SALMON instrument design (the five mechanisms suggest what healthy Turn engagement looks like behaviorally)

**Retrieval prompt:** “What specific cognitive mechanisms do Tooby and Cosmides propose for making oneself irreplaceable? Include the appetite for individuality, niche monitoring, product-differentiation, strategic association, and social rivalry. What does ‘product-differentiation’ mean in their framework — is it about skills, personality, or both?”

---

**SOC-TOO-BKP-03 \[EVOLUTIONARY\] \[FRAMING MOVE\]**

**Claim:** When irreplaceability cannot be established, individuals become vulnerable to desertion. Modern environments, which are safer and more stable than ancestral ones, lack the “clarifying events” (life-threatening crises) that reveal who is truly engaged in one’s welfare. Without these events, people interact with many “fair-weather friends” via commercial, contingent exchanges rather than the deep, non-contingent bonds the friendship psychology evolved to produce. The result is alienation and loneliness — not because the social machinery is broken, but because the environmental inputs it requires (existential stakes, small stable groups, repeated interaction under uncertainty) are absent.

**Relevant to:** Katie’s loneliness (evolutionary specification — not broken machinery, missing inputs), restoration \= niche repair (the friendship system needs environmental conditions, not self-improvement), mismatch thesis (ancestral friendship machinery in modern contingent-exchange environments), ghosted villain type (nothing comes back — no clarifying events means no signal about who’s truly engaged)

**Retrieval prompt:** “What do Tooby and Cosmides say about the breakdown of irreplaceability in modern environments? Include the ‘clarifying events’ concept, the shift from deep bonds to commercial/contingent exchange, and the prediction of alienation and loneliness. What conditions would need to be met for deep friendship to form?”

---

## **(COMP) Lukaszewski et al., “An Adaptationist Framework for Personality Science” (2020)**

---

**COMP-LUK-AFP-01 \[FRAMING MOVE\]**

**Claim:** Lukaszewski et al. argue that Big Five factors are “heuristic trait concepts” — products of a folk personality psychology designed by evolution for social prediction, not scientific constructs that reveal underlying machinery. Their analogy: factor-analyzing the adjectives users apply to a computer (“fast,” “intuitive,” “aesthetic”) provides no insight into the hardware producing the behavior. The lexical hypothesis assumes synonymous word clusters reveal fundamental dimensions of mind; the authors counter there is no scientific rationale for this assumption. Personality factors are often rotated to orthogonality for statistical convenience, but these decisions don’t change the operation of the mind’s actual programs.

**Relevant to:** HPAM’s “Big Five are statistical shadows” claim (convergent evidence from evo psych, independent of Bennett’s neuroscience route), SALMON instrument rationale (measuring the generative architecture, not the lexical shadow), the “computer analogy” as potential book illustration for Katie

**Retrieval prompt:** “What is Lukaszewski et al.’s specific critique of the Big Five and lexical hypothesis? Include the computer analogy, the claim about statistical rotation being arbitrary, and their argument that folk personality psychology is an evolved heuristic system for social prediction.”

---

**COMP-LUK-AFP-02 \[FRAMING MOVE\]**

**Claim:** Stopping at factor analysis leaves personality science unable to answer four fundamental questions: (1) which specific mechanisms produce the outputs described by a trait like Agreeableness? (2) How many different mechanisms produce outputs lumped into a single factor? (The many-to-one problem.) (3) Which important behavior-regulating mechanisms lack lexical terms and are therefore invisible to trait models? (4) What is the difference between perceiving behavior and generating behavior? The adaptationist toolkit fills these gaps through reverse-engineering logic (task analysis of ancestral problems → predicted information-processing structure) and can predict specific triggers and deactivation cues that descriptive models cannot.

**Relevant to:** HPAM’s aspect-level analysis (partially addresses the many-to-one problem — Compassion ≠ Politeness despite both falling under Agreeableness), missing-mechanism question (H is invisible to Big Five — HEXACO catches it; are there others?), Go/Turn as HPAM’s answer to the perception/generation gap

**Retrieval prompt:** “What four questions does stopping at factor analysis leave unanswered according to Lukaszewski et al.? Include the many-to-one problem, the missing mechanisms problem, and the perception-vs-generation distinction. What does their adaptationist toolkit add that descriptive models can’t provide?”

---

## **(COMP) Cosmides & Tooby, “Evolutionary Psychology: New Perspectives” (2013)**

*Structural note: IRVs are the closest thing in the evo psych literature to what HPAM calls stats. The kinship index — one variable calibrating two independent behavioral systems — is structurally identical to HPAM’s claim that one stat setting produces multiple downstream behavioral outputs. The tension: IRVs are continuous magnitudes (like Go stats), not categorical routing preferences (like Turn stats). See Book Content below for the three possible resolutions.*

---

**COMP-COT-EPN-01 \[MECHANISM\]**

**Claim:** Internal regulatory variables (IRVs) are specialized computational elements that store magnitudes representing value or tracking targeted properties of the body and social environment. They function through a three-step sequence: (1) psychophysical front ends register ancestrally reliable cues; (2) a dedicated estimator transforms cues into a continuous internal magnitude; (3) the magnitude is accessed as a parameter by multiple behavioral systems to calibrate their output. This process often occurs nonconsciously and independently of explicit beliefs. A single IRV can tune two entirely independent behavioral systems in parallel — the kinship index simultaneously calibrates altruism (up-regulating welfare-weighting) and sexual aversion (down-regulating attraction). Because a single choice cannot express inconsistent weights simultaneously, the brain integrates multiple factors into one variable that coordinates diverse outputs around a consistent internal estimate.

**Relevant to:** Go/Turn architecture (IRVs are the evo psych community’s independent convergence on “parameters tuning multiple systems”), SALMON instrument (IRVs suggest what stats are measuring computationally — stored magnitudes, not behavioral frequencies), the single-variable-multiple-outputs pattern (one stat → multiple mode expressions)

**Retrieval prompt:** “How do internal regulatory variables work computationally? Include the three-step sequence (cue detection → estimation → calibration), the kinship index as primary example showing one variable tuning two independent systems, and the claim that this process operates independently of explicit beliefs. Do the authors describe IRVs as relationship-specific or as general dispositional tendencies?”

---

**COMP-COT-EPN-02 \[MECHANISM\]**

**Claim:** Beyond the kinship index, the sources describe several additional IRVs: the Welfare Trade-Off Ratio (WTR, person-specific weight on another’s welfare relative to own), the Sexual Value Index (experienced as attraction), the Formidability Index (self-assessment of own fighting ability, feeding the anger program), the Conferral Index (self-assessment of ability to confer/withhold benefits — social leverage), Social Value of Self and Others (status indices), and Mortality Risk (calibrating life history strategy). The Formidability and Conferral Indices are self-assessment variables: the organism’s estimate of its own capacity, which then shapes social bargaining thresholds.

**Relevant to:** Formidability/Conferral as Go-stat self-knowledge (the system’s estimate of its own capacity shapes routing), WTR as the computational register behind Politeness routing, Mortality Risk as life history calibration (BIO bucket connection), the anger program’s dual inputs (formidability \+ WTR)

**Retrieval prompt:** “What specific internal regulatory variables are described beyond the kinship index? Include the WTR, Formidability Index, Conferral Index, Sexual Value Index, and Mortality Risk. How does the Formidability Index differ from the WTR — is one about self-assessment and the other about assessment of a specific other person?”

---

## **(BIO) Lukaszewski et al. — The Anger Program**

---

**BIO-LUK-AFP-01 \[MECHANISM\]**

**Claim:** The anger program is an evolved recalibrational adaptation whose outputs personality psychologists label “Agreeableness.” It activates on cues that a target’s WTR toward the self is unacceptably low (the target places too little weight on the self’s welfare). The program computes: (1) estimate the target’s WTR from behavioral cues (high cost imposed for trivial benefit, intentional harm); (2) assess own bargaining power via Formidability Index and Conferral Index; (3) determine whether the target’s WTR is lower than what one’s bargaining power can cost-effectively enforce. Outputs escalate: verbal arguments demonstrating the target’s insufficient valuation → threats or physical aggression demonstrating formidability → benefit-withholding (silent treatment) demonstrating cooperative withdrawal. The program deactivates when the target signals upward WTR recalibration — typically a sincere apology. The full input→computation→output specification extends the Sell et al. (2009) recalibrational signal framework already in BIO.

**Relevant to:** Politeness Turn stat (the anger program’s outputs map onto Savage vs. Respect routing — escalate vs. yield — not onto the whole Agreeableness domain), Go-feeds-Turn pattern (Compassion Go \= capacity to estimate others’ WTR accurately; Politeness Turn \= what you do with that estimate), Sell et al. recalibrational anger (extension with full program architecture), WTR as the computational register behind Politeness routing

**Retrieval prompt:** “What is the full input-computation-output specification of the anger program? Include the WTR detection trigger, the role of Formidability and Conferral indices in calculating bargaining power, the escalation sequence of outputs, and the specific deactivation cue (sincere apology as WTR recalibration signal).”

---

## **(BIO) Grodwohl & Parker / Maynard Smith — Evolutionary Game Theory**

---

**BIO-GRO-EGT-01 \[MECHANISM\] \[EVOLUTIONARY\]**

**Claim:** Resource-Holding Power (RHP) — an individual’s relative fighting ability — changes the equilibrium in evolutionary contests from random aggression to conditional strategies based on assessment. When contestants differ in RHP, the adaptive choice for the weaker party is to concede immediately rather than risk injury in an unwinnable fight. Escalated fights occur primarily when contestants are closely matched in RHP or when resource value is extremely high relative to injury cost. Animals evolved to “size up” opponents through displays, bellows, and sequential sparring bouts that provide increasingly accurate information about relative strength.

**Relevant to:** Go stats as RHP (Go capacity determines which Turn-routing strategies are affordable — high RHP makes escalation viable, low RHP makes concession adaptive), the Go-shapes-Turn pattern (capacity constrains routing), Assertiveness Turn (Boss vs. Backseat as conditional strategy calibrated to assessed relative RHP), sequential assessment as real-time self-calibration mechanism

**Retrieval prompt:** “How does resource-holding power change the predicted equilibrium in animal contests? Include the shift from random aggression to conditional assessment-based strategies, the conditions under which escalated fights occur, and the sequential assessment model where organisms gather information through successive bouts.”

---

**BIO-GRO-EGT-02 \[MECHANISM\] \[EVOLUTIONARY\]**

**Claim:** The “Bourgeois” strategy — “if owner, play Hawk; if intruder, play Dove” — demonstrates that arbitrary role cues unrelated to fighting ability can settle contests without escalation. The asymmetry need not be correlated with RHP or resource value; it only needs to be common knowledge between contestants. This produces role-based conditional behavior: the same organism, with the same capacity, produces completely different behavioral output depending on a contextual cue. Maynard Smith showed this is an ESS — once a population adopts it, no mutant strategy can invade.

**Relevant to:** Turn stats as conditional routing (same capacity, different output depending on role — this is what Turn routing looks like described in game-theoretic terms), why Turn stats feel “situational” (the person routes differently in different roles, which looks like inconsistency but is a conditional strategy), uncorrelated asymmetries in modern environments (credentials, seniority, follower counts function as Bourgeois cues)

**Retrieval prompt:** “What is the Bourgeois strategy and how does it demonstrate that arbitrary asymmetries can settle contests? Include Maynard Smith’s ESS proof, the distinction between correlated and uncorrelated asymmetries, and examples of role-based conditional behavior in animal contests.”

---

**BIO-GRO-EGT-03 \[MECHANISM\]**

**Claim:** When organisms cannot accurately assess relative RHP — due to unreliable displays, novelty, or unfamiliarity — the sequential assessment model predicts three failure modes: (1) default to escalation (the underdog can’t determine it’s weaker, so it doesn’t concede — costly fights result); (2) default to arbitrary settlement via uncorrelated asymmetries (when real formidability is unknown, role-based rules like Bourgeois substitute for assessment); (3) continued sequential information-gathering through successive bouts until one party realizes it’s the likely loser. Psychological adaptations for assessment (like the Formidability Index) are designed for ancestral environments; in novel environments these mechanisms may misread cues, producing maladaptive escalation or retreat.

**Relevant to:** Easy-locking (environments that prevent honest assessment prevent self-calibration of RHP/Go-stat capacity), masking (producing displays that don’t match actual state \= signal unreliability \= assessment failure for both self and others), ghosted villain type (no signal returns \= no sequential assessment possible \= organism can’t discover relative RHP), mismatch thesis (assessment hardware intact, input conditions changed)

**Retrieval prompt:** “What happens in the sequential assessment game when organisms cannot accurately assess relative RHP? Include the three predicted behavioral consequences (escalation, arbitrary settlement, continued information-gathering), the dual-error framework (over-activation vs. under-activation), and the claim about mechanism failure in novel environments.”

---

## **(BIO/MASK) Honest Signals and Assessment Errors**

---

**BIO-GRO-EGT-04 \[MECHANISM\] \[EVOLUTIONARY\]**

**Claim:** The adaptationist framework predicts organisms must avoid dual errors: over-activation of aggression (escalating against a superior opponent — false alarm on own strength → injury) and under-activation (conceding to an inferior opponent — miss on own strength → resource loss). Natural selection addresses unreliable displays by favoring “honest” signals too expensive for a low-RHP individual to counterfeit (the handicap principle). Emotions were “handcuffed” to involuntary physiological circuits — sweating, trembling, facial expressions — precisely to make them unfakeable honest advertisements of internal states. If displays are easy to fake, their informational value drops, and the assessment system can no longer function.

**Relevant to:** Masking as metabolic cost (evolutionary rationale — masking fights a system designed to be unfakeable; producing a display that doesn’t match your state \= paying the cost of the honest-signal machinery in a mode it wasn’t designed for), the expensive animal (the cost of honest signals is a feature, not a bug — it’s what makes them informative), SDT logic applied to social assessment (every threshold trades false alarms against misses)

**Retrieval prompt:** “What is the handicap principle and how does it explain why natural selection favors costly, unfakeable signals? Include the dual-error framework (over- vs. under-activation), the claim that emotions were ‘handcuffed’ to involuntary physiological circuits, and what happens to assessment systems when signals become unreliable or easy to fake.”

# Neuroticism 

# **Hagen , Depression-as-Adaptation**

**Source manifest:** NotebookLM responses (Prompts 7 and follow-up on process-level mechanisms) pasted by Brian. Source library: Hagen (2011) “Evolutionary Theories of Depression: A Critical Review” \+ supporting sources on analytical rumination, social risk, honest signaling, bargaining, and social competition hypotheses. Access method: \[notebooklm extraction returns pasted by brian\]. MASK doc fetched via google\_drive\_fetch this conversation. Duplicate-checked — no existing Hagen cards in MASK.

**Placement note:** These cards document what the depression-as-adaptation literature claims. The Book Content entry below documents Brian’s positioning of this material relative to HPAM’s masking architecture. The depression literature addresses *function* (why does low mood exist?). HPAM’s masking framework addresses *cost* (what does chronic suppression do to the system?). They are adjacent but not the same question.

---

## **Source: Hagen (2011), “Evolutionary Theories of Depression: A Critical Review” \+ supporting sources**

Author code: HAG  
 Book abbreviation: ETD (Evolutionary Theories Depression)  
 Bucket: MASK

---

**MASK-HAG-ETD-01 \[FRAMING MOVE\]**

**Claim:** Five competing adaptive hypotheses for depression each propose a distinct evolved function for low mood, with different predictions about who gets depressed, when, and what triggers recovery. (1) Social Competition: depression as involuntary subordinate strategy — inhibits aggression after rank loss, signals submission, facilitates acceptance of defeat. Predicts onset after rank loss; recovery through yielding. (2) Analytical Rumination: depression as problem-solving reallocation — anhedonia diverts cognitive resources from daily activities to focus single-mindedly on the triggering problem. Predicts onset facing severe complex problems; recovery through solving them. (3) Honest Signaling: depression and self-harm as credible cry for help — costly signal of genuine need that can’t be faked cheaply. Predicts onset amid interpersonal conflict with skeptical partners; recovery through receiving support. (4) Bargaining: depression as withdrawal of labor to force concessions from interdependent partners. Predicts onset when feeling exploited; recovery through partner concessions. (5) Social Risk: low mood as risk-aversion strategy when social value is low — reduces social risk-taking to maintain tenuous connections. Predicts onset when social standing is precarious; recovery through re-establishing social safety. Most evolutionary theorists concede that clinical MDD likely represents a dysregulated extreme of otherwise adaptive low-mood mechanisms.

**Relevant to:** MASK motivation layer (each hypothesis proposes a different upstream trigger that could initiate masking — rank loss, complex problems, interpersonal exploitation, social precariousness), containment vs. armor masking (social competition and social risk hypotheses predict containment-direction responses; bargaining predicts armor-direction responses), three-timescale cascade (the “smoke alarm stuck on” concession from most theorists is the claim that adaptive low mood becomes pathological through the same kind of self-sustaining trap the MASK cascade describes)

**Retrieval prompt:** “What are the five main adaptive hypotheses for depression that Hagen reviews? For each, what is the proposed evolved function, who is predicted to get depressed, and what triggers recovery? Include the social competition, analytical rumination, honest signaling, bargaining, and social risk hypotheses. What is the consensus position on where adaptive low mood ends and clinical MDD begins?”

---

**MASK-HAG-ETD-02 \[COUNTERPOINT\] \[FIELD STATUS\]**

**Claim:** No study has successfully examined whether the rumination characteristic of depression actually improves the person’s responses to the life problems that triggered the depressive episode. The “resource reallocation” proposed by the analytical rumination hypothesis is observable on the loss side — measurable performance deficits on unrelated cognitive tasks, documented situation-symptom congruence (social loss triggers crying; failure triggers fatigue) — but the putative gain in problem-solving utility remains untested. Additionally: the social competition hypothesis fails to explain why episodes last months when quick yielding would be most adaptive. The social risk hypothesis predicts risk-aversion to protect relationships, but depressed individuals actually parent less and work less, reducing relationship payoffs and potentially hastening the ostracism the strategy supposedly prevents. The honest signaling model’s account of suicidality as a high-stakes gamble remains largely untested and controversial.

**Relevant to:** MASK architecture (the cost structure of depressive states is better documented than the putative function — converges with HPAM’s emphasis on cost mechanisms rather than functional teleology), existing MASK-CAM-SCC-01 (rumination consumes resources without demonstrated return — this card provides the depression-specific version of the same finding), Loop 1 (rumination as resource drain is now confirmed from two independent literatures: self-concept research and evolutionary depression research)

**Retrieval prompt:** “What are the main empirical failures of adaptive depression hypotheses? Include: the missing evidence that rumination improves problem-solving, the social competition timing problem (why months-long episodes?), the social risk paradox (depressed people reduce rather than protect relationship payoffs), and the untested status of the signaling account of suicidality. Which of these failures does Hagen consider most damaging to which hypothesis?”

---

**MASK-HAG-ETD-03 \[MECHANISM\]**

**Claim:** The analytical rumination hypothesis describes a specific process-level shift during depressive states: anhedonia removes the distraction of pursuing food, sex, or social interaction, freeing processing capacity for intense focus on the triggering problem. Resources are pulled from daily maintenance (grooming, eating, sleeping) and from unrelated cognitive tasks. Depressed individuals show deficits in abstract reasoning and laboratory cognitive tests, interpreted as evidence that processing capacity is already fully occupied by the triggering problem. Fatigue and pessimism function to conserve resources and decrease initiative in circumstances where effort is likely to be wasted. However, this account is currently more inference from symptom profile than verified mechanism — anhedonia and rumination co-occur, so theorists infer that the former exists to facilitate the latter, but the facilitation itself is undemonstrated.

**Relevant to:** Existing MASK-CAM-SCC-01 (the analytical rumination hypothesis provides a function-level framing for the same resource competition that Campbell documents at the self-concept level: rumination occupying bandwidth that would otherwise be available for adaptive coping), Double Cognitive Taxation BC (a person who is both masking AND in a depressive resource-reallocation state would be triply taxed: masking \+ rumination \+ anhedonia-mediated withdrawal from normal maintenance), Barrett HEAM-04 (rumination-as-paving — Barrett provides the neural mechanism for how rumination entrenches; Hagen provides the evolutionary rationale for why the system might have been designed to ruminate in the first place)

**Retrieval prompt:** “What does the analytical rumination hypothesis claim is happening at the process level during depression? What capacities are suppressed (hedonic drive, extraneous attention, performance on unrelated tasks, behavioral initiation) and what is supposedly enhanced (analytical reasoning focused on the triggering problem)? Where does the hypothesis rest on inference from symptom profile versus direct evidence of resource reallocation?”

---

**MASK-HAG-ETD-04 \[MECHANISM\]**

**Claim:** The social risk hypothesis proposes that low mood heightens social vigilance — increasing attention to social threats and reducing risky social behaviors — as a strategy to avoid ostracism when the individual’s social value is low. This is functionally a shift toward threat-monitoring and risk-aversion in the social domain. Separately, the social competition hypothesis predicts that low mood inhibits aggression and speeds reactions to threatening stimuli, locking attention onto potential negatives. Both hypotheses converge on a prediction that depressive states shift the organism toward heightened threat detection and reduced exploratory behavior in the social environment.

**Relevant to:** Explore/exploit axis (low mood as a shift toward exploit-mode vigilance — reduced exploration, heightened monitoring of existing social connections, risk-aversion), Volatility routing (social risk hypothesis predicts Zen-direction shift under precarious social standing — reduce reactivity to avoid triggering rejection), masking motivation layer (social risk hypothesis identifies low social value as the trigger state — converges with Leary’s sociometer detecting relational threat)

**Retrieval prompt:** “What does the social risk hypothesis predict about changes in social behavior during low mood? Include the heightened social vigilance claim, the risk-aversion prediction, and how this intersects with the social competition hypothesis’s prediction about inhibited aggression and threat-locked attention. Do the sources provide direct evidence for enhanced social vigilance during depressive states, or is this inferred from the theory?”

