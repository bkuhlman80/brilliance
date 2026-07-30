# Computational and Robotic Models of First-Language Acquisition: A Literature Review (2023–2026 emphasis)

## TL;DR
- No computational or robotic system has demonstrated end-to-end acquisition of a first language from realistic child input across phonology, morphology, syntax, and grounded semantics together; the strongest recent results are narrow successes (grounded word–referent mapping from one child's headcam, U-shaped past-tense curves, child-matching acquisition *order* for three syntactic phenomena) coupled with robust failures (hierarchical generalization, out-of-distribution grounding, sample efficiency 3–4 orders of magnitude worse than children).
- The field splits into two goals that are routinely conflated: (i) modeling *how humans acquire* language and (ii) *engineering data-efficient ML*; the BabyLM Challenge explicitly serves both, and most "success" headlines concern (ii) while the cognitive claims (i) remain contested.
- The most live 2023–2026 debates — whether child-directed speech actually helps, whether embodiment is necessary, whether LMs refute the poverty-of-the-stimulus argument, and whether LMs distinguish possible from impossible languages — are genuinely unresolved, and several are older debates (past-tense, nativism vs. empiricism) recurring with new tools.

## Key Findings

**Consensus (broadly agreed):**
- Children are exposed to fewer than 100 million word tokens by about age 13 (the BabyLM organizers cite Gilkerson et al. 2017 for this estimate), while modern language models are typically trained on three to four orders of magnitude more data and still underperform humans on many evaluations. This data-efficiency gap is the field's organizing fact (BabyLM organizers; Warstadt et al. 2023; Hu et al. 2024).
- Disembodied text LMs reproduce many morphological/syntactic phenomena (subject–verb agreement, filler–gap, U-shaped past tense) but the way they acquire language diverges substantially from children.
- Word–referent mapping (one slice of word learning) is learnable by a generic neural net from one child's naturalistic audiovisual input (Vong et al. 2024, *Science*) — but only partially, and it stalls badly on out-of-distribution generalization.

**Contested:**
- Whether child-directed speech is better training data than other text (Feng/Goodman/Frank 2024; Padovani et al. 2025 say no consistent benefit).
- Whether embodiment/grounding changes acquisition or merely adds a perceptual channel.
- Whether LMs' success undercuts the poverty-of-the-stimulus argument (Lan/Chemla/Katzir vs. Piantadosi; Kallini et al.).

**Individual assertions (not consensus):**
- Steven Piantadosi (2024, "Modern Language Models Refute Chomsky's Approach to Language," in *From Fieldwork to Linguistic Theory*, Language Science Press) argues that modern ML "has subverted and bypassed the theoretical framework of Chomsky's generative approach," and that "large language models have attained remarkable success at discovering grammar without using any of the methods that some in linguistics insisted were necessary."
- Claims that embodiment is "instrumental" for human-like intelligence (Cangelosi & Schlesinger).

## Details

### A. Theories under test, and which developmental behaviors are being modeled

**Distinguish the two goals up front.** The BabyLM Challenge organizers (Warstadt, Choshen, Cotterell, Linzen, Williams, Hu, Mueller, Wilcox, Zhuang, Ross, and colleagues; institutions span NYU, ETH Zürich, MIT, IBM, Meta AI, Northeastern, Georgetown, Boston University) explicitly list three goals: building cognitively/developmentally plausible models, optimizing pretraining pipelines before scaling, and democratizing LM research. Goals 1 (explaining humans) and 2–3 (engineering) coexist in the same competition, which is exactly why "BabyLM success" is ambiguous: a model can win the competition (engineering) while telling us little about children (cognition).

**Theories and lineages being instantiated:**
- *Connectionist vs. symbolic/dual-route (past tense).* The Rumelhart & McClelland (1986) single-route connectionist model vs. Pinker & Prince (1988) / Pinker & Ullman dual-route is the founding debate. Modern revisitations: Kirov & Cotterell (2018) showed encoder–decoder RNNs reach near-ceiling accuracy and produce human-like overregularization errors (*throwed*), overcoming the original Pinker–Prince objections; but Corkery et al. (2019, German plurals) and McCurdy et al. found encoder–decoders fail as cognitive models where there is "no majority" default. Haga et al. (2024, Findings of ACL) "Modeling Overregularization in Children with Small Language Models" found child-like U-shaped curves for *certain* verbs but the *preferences for types of overregularization did not match children* — a precise partial match (right curve shape, wrong error distribution).
- *Usage-based / construction grammar* (Tomasello lineage) is instantiated in Bayesian construction learners (Alishahi & Stevenson) and in BabyLM curriculum work.
- *Cross-situational / statistical word learning* (Yu & Smith; Frank, Goodman & Tenenbaum Bayesian model) is instantiated in Fazly, Alishahi & Stevenson (2010) and in CVCL (Vong et al. 2024).
- *Distributional learning / poverty-of-stimulus tests* (Linzen lineage): subject–verb agreement (Linzen, Dupoux & Goldberg 2016), targeted syntactic evaluation (Marvin & Linzen 2018), hierarchical generalization (Yedetore et al. 2023).

**Specific developmental behaviors researchers try to reproduce (beyond overregularization):**
- *Vocabulary spurt and fast-mapping*: targeted by cross-situational models (Fazly et al.); CVCL does word–referent mapping but does not claim a spurt.
- *Age/order of acquisition*: Chang & Bergen (2022, TACL) extracted "ages of acquisition" for 600+ CDI words in LSTMs/BERT/GPT-2 — found concreteness, word length, and lexical-class effects *pointedly different* from children, and models rely *far more on frequency* than children do (a cognition-goal study with a negative result). Evanson, Lakretz & King (2023, Findings of ACL, pp. 12205–12218, DOI 10.18653/v1/2023.findings-acl.773) trained **48 GPT-2 models** from scratch (WikiText103) and compared them to 54 children aged 18 months–6 years; they report that "probes tend to be learned in the same order by all agents with R = 0.743, p < 0.001, disproving the null hypothesis." For the three directly comparable syntactic phenomena, models matched the child order — subject–verb agreement in simple sentences → in questions → across (object) relative clauses — in **46 of 48 seeds**. Crucially, they flag that for the hardest stage the models reach above-chance accuracy via *heuristics rather than syntactic rules* (the incongruent-case probes are not learned above chance), and that the predictors of order do not always track linguistic difficulty.
- *Shape of error trajectories (U-shaped learning)*: Haga et al. 2024; Evanson et al. report a dip-then-rise on a group of BLiMP phenomena.
- *Individual variation*: largely NOT modeled. Frank's Wordbank program documents that "kids take a lot of different routes to language," and the variation across children is a target the models have not addressed.

### B. Embodiment and grounding

**The case that grounding/embodiment helps or matters:**
- The developmental-robotics lineage (Cangelosi, Metta and the iCub platform; Asada; the IEEE ICDL / IEEE TCDS community; Tani; Steels) holds, per Cangelosi & Schlesinger, that the physical body is instrumental for human-like intelligence. iCub work (Marocco, Cangelosi, Fischer, Belpaeme 2010; Stramandinoli, Marocco & Cangelosi 2012) grounds action words in sensorimotor interaction; Tani's group (Science Robotics 2024) shows compositional generalization of verb–noun combinations improving with task variation in a real robot.
- Vong, Wang, Orhan & Lake (2024, *Science*, DOI 10.1126/science.adi1374) is the strongest grounding-from-realistic-input result. CVCL (Child's View for Contrastive Learning) was trained on SAYCam-S — "600,000 video frames paired with 37,500 transcribed utterances (extracted from 61 hours of video)" over the child's life from 6 to 25 months, which "only captures about 1% of the child's waking hours." It reached **61.6%** four-alternative classification accuracy on in-distribution concepts (vs. 26.7% for a co-occurrence-lesioned control and 66.7% for web-scale CLIP).
- Developmental psychology (Smith & Gasser, "six lessons from babies") and the symbol-grounding tradition (Harnad 1990) argue text-only meaning is parasitic on prior human grounding (recent restatements: Harnad 2024; "epistemic parasitism").

**The case that embodiment does NOT (clearly) matter, or that text suffices:**
- Blind children acquire language largely without issue (noted by the BabyLM organizers), showing visual grounding is not necessary.
- The BabyLM *multimodal* track has repeatedly FAILED: no submission beat the text+image baselines in 2024, and the multimodal/vision track remained hard in 2025. Adding vision did not buy data efficiency.
- The morphology/syntax phenomena that text LMs reproduce (agreement, filler–gap, past tense) are reproduced *without any grounding at all*, so for those phenomena grounding is demonstrably not required.
- CVCL itself replaces acoustic input with idealized transcripts and learns from still frames, not embodied action; its authors list embodiment as a missing ingredient, not a demonstrated one.

**Where embodied robots stall:** unsupervised grammar learning from real, colloquial user utterances; scaling beyond small lexicons; the survey literature ("Survey on frontiers of language and robotics," Tani/Asada-adjacent) notes most problems remain unsolved and that robots learn small grounded lexicons but not rich grammar. Grounding interacts with morphology/syntax asymmetrically: grounding helps concrete nouns most, verbs and function/abstract words least — exactly the categories where disembodied models also struggle.

### C. Social and interactive input

- *Child-directed speech (CDS) as training data — contested and trending negative.* Feng, Goodman & Frank (2024, EMNLP) "Is Child-Directed Speech Effective Training Data for Language Models?" and Padovani, Jumelet, Matusevych & Bisazza (2025, EMNLP) "Child-Directed Language Does Not Consistently Boost Syntax Learning in Language Models" (across English, French, German) both find CDS does not consistently beat other text for grammar. A 2026 follow-up argues CDS facilitates *production, not comprehension*. This partially contradicts the developmental-linguistics prior (Ferguson; the assumption that CDS is specially helpful).
- *Interaction/feedback.* The BabyLM 2025 INTERACTION track (teacher–student) found teacher interaction *can* yield high-quality models, and interaction-track submissions beat baselines (a winning entry used RL-based interaction; Martins et al. 2025). But Padovani et al. (2025, "Dialogue Is Not Enough to Make a Communicative BabyLM (But Neither Is Developmentally Inspired Reinforcement Learning)") found dialogue and RL insufficient. For 2026, the standalone Interaction and Multimodal tracks were *removed* and folded into the strict tracks.
- *Human evidence is itself contested.* Whether corrective feedback/recasts drive developmental change is disputed in acquisition research (the "no negative evidence" problem; the past-tense-without-feedback modeling lineage). The modeling work cannot settle what the human evidence has not.

### D. The negative space (priority inventory)

**Convincingly reproduced (with caveats):**
- Subject–verb agreement, including across some intervening material (Linzen et al. 2016; Marvin & Linzen 2018) — though accuracy degrades with attractors.
- Filler–gap dependencies (Wilcox et al.).
- Regular/irregular past tense with near-ceiling accuracy and human-like overregularization errors in the modern encoder–decoder revisitation (Kirov & Cotterell 2018).
- Word–referent mapping from naturalistic single-child input, in-distribution (Vong et al. 2024, 61.6%).
- Systematic acquisition *order* across syntactic phenomena, consistent across seeds (R=0.743) and partially matching children (Evanson et al. 2023).

**Stubbornly resisted:**
- *Hierarchical generalization for yes/no questions.* Yedetore, Linzen, Frank & McCoy (2023, ACL) "How poor is the stimulus?" trained LSTMs and Transformers on CHILDES-scale child-directed speech: both generalized using linear/word-identity heuristics, NOT hierarchical rules — suggesting children's word-input alone may not contain enough hierarchical cues for a learner without a hierarchical bias. A clean negative result for the empiricist position at child-realistic scale.
- *Out-of-distribution visual grounding.* CVCL drops to 34.7% on the Konkle out-of-distribution object set; referent localization is inconsistent across categories (e.g., reliable for "ball"/"car," misaligned for "cat"/"paper"), and the contrastive objective produced errors such as associating "hand" with sand.
- *Data efficiency*: no model closes the 3–4 order-of-magnitude gap.
- *Verbs and abstract words*; *temporally extended/embodied meanings* (CVCL learns from still frames, which its authors note "likely affect[s] the learnability of verbs and other abstract words").
- *Individual variation* and *multiple developmental routes*.

**Partial matches (precise mismatch):**
- Past tense: right U-shape for some verbs, wrong distribution of overregularization types (Haga et al. 2024).
- Word age-of-acquisition: models show the slower-learning-in-longer-utterances effect like children, but frequency dominates and concreteness/length/lexical-class effects run differently (Chang & Bergen 2022).
- German plurals: encoder–decoders fail to reproduce the human default where there is no statistical majority (Corkery et al. 2019; McCurdy et al.).

### E. Live debates (2023–present)

1. **Does CDS help LMs learn grammar?** Live and empirically resolvable. Feng/Goodman/Frank and Padovani et al. (no consistent benefit) vs. the developmental prior and curriculum-learning advocates (Mueller & Linzen 2023 found CDS-first curricula impart hierarchical bias). Mostly empirical; partly about evaluation choice (production vs. comprehension; which benchmark).

2. **Poverty of the stimulus / nativism vs. empiricism.** Genuinely live but partly a framing dispute and partly an *old* debate in new clothing. Lan, Chemla & Katzir (2024, *Linguistic Inquiry*, DOI 10.1162/ling_a_00533) argue networks trained on natural corpora FAIL on certain dependencies but succeed when input is enriched — *supporting* the argument from the poverty of the stimulus. Piantadosi (2024) argues LMs refute Chomsky. On the critical side, Kodner, Payne & Heinz (2023, arXiv:2308.03228, "Why Linguistics Will Thrive in the 21st Century") reply that "humans achieve their capacity for language after exposure to several orders of magnitude less data," and that the implications of LLMs for understanding the cognitive mechanisms of language "are like the implications of airplanes for understanding how birds fly"; Katzir (2023) presses the opacity and data-scale objections. Strongest pro-empiricist point: LMs demonstrably acquire structure-dependent phenomena from data alone. Strongest pro-nativist point: they do so from vastly more data, often via heuristics, and fail at child-realistic scale (Yedetore et al.).

3. **Can LMs distinguish possible from impossible languages?** Live. Kallini, Papadimitriou, Futrell, Mahowald & Potts (2024, ACL, Best Paper Award; pp. 14691–14714) built 15 synthetic impossible languages (shuffle, reverse, and count-based "hop" rules) and report that "GPT-2 struggles to learn impossible languages when compared to English as a control, challenging the core claim" that LLMs are indifferent to possibility — interpreted as an inductive bias aligned with human language. Critics: Hunter (2024, *Computational Linguistics*) "Kallini et al. (2024) do not compare impossible languages with constituency-based ones"; and Leivada et al. (2025) and a separate "Biasless Language Models Learn Unnaturally" line find LMs sometimes *prefer* impossible variants, undermining the strong reading. Futrell & Mahowald (2025, BBS target article, "How Linguistics Learned to Stop Worrying and Love the Language Models") frames the constructive position. Empirically resolvable in principle but currently methodologically contested.

4. **Do children and LMs follow similar learning stages?** Evanson et al. (2023) say partially yes (order matches for three phenomena, R=0.743 across seeds) but with divergences (heuristics, plural-verb bias). Chang & Bergen say the predictors of acquisition differ. Live, empirical.

5. **Is grounding solved/needed?** See B. Live, partly framing (definitions of "grounding"); the multimodal track's repeated failure is the key empirical datapoint.

### F. Forward-looking methods (each paired with its critique)

- *Multimodal / vision-grounded BabyLMs (CVCL successors; BabyVLM; lexicon-level contrastive grounding).* Promising route to word learning. Critique: no multimodal submission has beaten text baselines on language benchmarks; out-of-distribution generalization is weak; transcripts ≠ speech. To count as established: a multimodal model must beat strong text-only baselines on grammatical and word-learning benchmarks at child scale.
- *Self-supervised speech / learning without linguistic priors (Dupoux lineage; Zero Resource Speech Challenge; BabySLM benchmark; Lavechin, Cristia et al.).* Promising for phonetic acquisition from raw audio. Critique: Lavechin et al. (2023) found statistical-learning models of early phonetic acquisition *struggle with real child-centered audio*; the realistic-scale acoustic problem remains largely unsolved (Dupoux's 2018 *Cognition* roadmap for "reverse-engineering the infant language-learner" still open).
- *Interaction/teacher–student and RL (BabyLM 2025).* Promising: teacher interaction yielded strong models. Critique: "Dialogue Is Not Enough" — gains may reflect distillation from a large teacher (which has itself seen trillions of words), undercutting the developmental-plausibility claim.
- *Curriculum learning (age-ordered CDS; cross-linguistic, Salhan et al. 2024).* Popular — the most common BabyLM approach across all three years. Critique: it was rarely the actual winner; benefits are inconsistent.
- *New architectures/objectives (GPT-BERT hybrid; diffusion LMs; mixture-of-experts; LTG-BERT).* These, not cognitive insights, produced the actual BabyLM wins (e.g., GPT-BERT in 2024; a diffusion LM, a mixture-of-experts model, and an RL interaction approach in 2025) — itself a deflationary finding for the cognitive-modeling goal.
- *Developmental robotics with foundation models (LLM-on-robot; Alter3; vision-language-action models).* Promising for grounded action-language. Critique: symbol grounding "circumvented, not solved" (these models inherit grounding from human text); hallucination; small grounded lexicons.

## Recommendations
- **For a realistic depiction of an artificial agent learning a first language from scratch:** depict narrow, uneven competence — good word–object mapping for concrete nouns, plausible morphological overregularization curves, emerging agreement, but failure at hierarchical syntax from realistic input, weak out-of-distribution grounding, and gross data inefficiency. Do NOT depict smooth, child-like, stage-wise mastery across all levels; that has not been demonstrated.
- **Attribute positions, don't harmonize:** if the depiction touches the nativism debate, present Lan/Chemla/Katzir and Kodner/Payne/Heinz alongside Piantadosi and Futrell/Mahowald as live disagreement, not a settled verdict.
- **Benchmarks that would change the depiction:** (i) a multimodal/embodied model beating text-only baselines on grammar at ≤100M words; (ii) hierarchical generalization emerging from child-scale CDS without a built-in bias; (iii) closing the data-efficiency gap by even one order of magnitude with developmentally plausible input; (iv) reproducing individual variation. Until these are met, treat "embodiment helps" and "machine resembles child" claims as unproven.

## Caveats
- Several key 2025–2026 sources are arXiv preprints (Padovani et al.; BabyBabelLM; the acoustic-modeling review; the impossible-languages replies); peer-reviewed anchors include Vong et al. (*Science*), Kallini et al. (ACL), Yedetore et al. (ACL), Haga et al. (Findings of ACL), Feng et al. (EMNLP), Lan et al. (*Linguistic Inquiry*), Hunter (*Computational Linguistics*), Chang & Bergen (TACL). Preprint status is flagged inline where it matters.
- Abstracts compress findings; where possible I verified against Results sections (Evanson R=0.743 and 46/48 seeds; CVCL 61.6% in-distribution / 34.7% out-of-distribution; Yedetore heuristic generalization; Haga partial U-shape with mismatched error types).
- "Acquisition order matches children" rests on only three directly comparable syntactic phenomena (Evanson et al.) and should not be over-generalized; the same paper shows the matched accuracy is partly heuristic.
- The Piantadosi piece is widely cited from a 2023 preprint (lingbuzz/007180) and appeared in an edited volume dated 2024; cite the venue accordingly.

## The clearest current limits — what no model or robot has yet shown
No system has acquired a first language from human-scale, naturalistic, multimodal input the way a child does. Specifically, none has: (1) integrated phonology + morphology + syntax + grounded semantics in one agent learning from realistic input; (2) achieved child-like data efficiency; (3) shown hierarchical syntactic generalization from child-scale child-directed speech without a built-in structural bias (Yedetore et al. is the key negative result); (4) demonstrated robust out-of-distribution grounding of word meaning (CVCL 34.7%); (5) learned verbs and abstract words from embodied experience at scale; or (6) reproduced the individual variation and multiple developmental routes children show. The robust positive results are narrow (word–referent mapping, agreement, past-tense curves, acquisition order for a few phenomena), and the most reliable cross-cutting finding remains the large, unexplained data-efficiency gap between children and machines.