# **Brain energetics and metabolic neuroscience: a structured field reconnaissance**

The field of brain energetics is experiencing a methodological renaissance that is outpacing its theoretical frameworks. **Functional PET now achieves 3-second temporal resolution**, genetically encoded metabolic sensors enable cell-type-resolved imaging of glucose, lactate, and ATP in behaving animals, and deuterium metabolic imaging brings metabolic flux mapping to standard clinical MRI scanners. These tools have shattered several long-standing assumptions: the default mode network does not actually reduce its glucose consumption during task (it maintains high metabolism despite negative BOLD signals), neurons perform substantial glycolysis on their own (undermining the classical astrocyte-neuron lactate shuttle), and the brain's metabolic "youth" — measured by aerobic glycolysis — may be a resilience marker against Alzheimer's pathology rather than a developmental relic. Meanwhile, two sub-areas that should be mature — mitochondrial biology as a source of normal-range cognitive differences, and whole-body energy budget trade-offs involving the brain — remain strikingly underpopulated, representing genuine gaps rather than well-explored territories. The metabolic psychiatry movement has generated extraordinary clinical enthusiasm and institutional investment, but its mechanistic evidence base remains thinner than its public profile suggests, with the strongest causal data limited to schizophrenia and specific metabolic-dopamine coupling pathways.

The reconnaissance below covers seven sub-areas with roughly equal depth, flags 65+ empirical papers with full citations and commentary, and concludes with a lab-mapping section identifying where institutional momentum is concentrating. Time window: 2019–present, with select foundational papers from 2015–2018 where recent results depend on them.

---

## **1\. The metabolic cost of cognition is real but architecturally subtle**

### **State of play**

The claim that task-directed cognition costs only \~5% more than resting whole-brain metabolism — advanced by Jamadar et al. (2025, *Trends in Cognitive Sciences*) — is broadly consistent with the empirical base but requires careful qualification. That figure reflects whole-brain averages; within task-relevant circuits, local metabolic increases of **18–27%** are routinely observed via functional PET. The modest global increment reflects the brain's metabolic homeostasis strategy: increases in task-relevant regions are partially offset by decreased metabolism elsewhere. Roughly 70–80% of the brain's energy budget goes to ongoing housekeeping — maintaining resting potentials, synaptic infrastructure, and ion gradients — leaving a narrow band for cognition-specific energy demands.

Three findings have reshaped this sub-area since 2019\. First, the BOLD signal and glucose metabolism are fundamentally dissociated in the default mode network: task-induced negative BOLD responses do not correspond to metabolic decreases, meaning decades of fMRI interpretation require revision. Second, the field has moved decisively beyond glucose-centric models. Lactate is now established as mandatory for high-computational-load synaptic plasticity, while glucose suffices for lighter computation. Third, hippocampal sharp-wave ripples — a canonical memory consolidation signal — simultaneously regulate peripheral blood glucose, revealing that cognition and metabolism share neural architecture at the circuit level.

The empirical base is methodologically rich but sample-poor. Most human fPET studies run n=18–50, constrained by PET costs and radiation exposure. Large-cohort studies connecting brain metabolic phenotypes to genetic architecture are essentially absent. This is a methods-driven literature where the tools are ahead of the population-level data.

### **Key empirical papers**

**Stiernman LJ et al.** "Dissociations between glucose metabolism and blood oxygenation in the human default mode network revealed by simultaneous PET-fMRI." *PNAS*, 2021, 118(27): e2021913118. DOI: 10.1073/pnas.2021913118. Design: cross-sectional, simultaneous PET-fMRI. N=23 healthy adults. No genetic data. This paper demonstrates that task-negative BOLD responses in the DMN do not reflect decreases in glucose metabolism — DMN glucose consumption remains high during both rest and task. Edited by Marcus Raichle, it used constant-infusion \[18F\]FDG fPET during a verbal working memory task. The dissociation was specific to the posterior DMN; task-positive regions showed expected coupling. This fundamentally challenges the standard interpretation that DMN "deactivation" reflects metabolic quiescence, suggesting instead that negative BOLD may reflect neurovascular uncoupling or active, energy-demanding suppression.

**Hahn A et al.** "High-temporal resolution functional PET/MRI reveals coupling between human metabolic and hemodynamic brain response." *European Journal of Nuclear Medicine and Molecular Imaging*, 2024, 51(5): 1310–1322. DOI: 10.1007/s00259-023-06542-4. Design: methods-validation, cross-sectional. N=35 healthy volunteers. No genetic data. Achieves **3-second temporal resolution** for functional PET glucose metabolism during working memory, the highest ever reported for human brain metabolic imaging. Demonstrates that metabolic signals return to baseline within \~10 seconds of task cessation and that temporal hemodynamic-metabolic coupling in motor cortex predicts individual behavioral performance. The Vienna group's optimized bolus-plus-infusion protocol makes fPET viable for event-related designs previously restricted to fMRI.

**Hahn A et al.** "Reconfiguration of functional brain networks and metabolic cost converge during task performance." *eLife*, 2020, 9: e52443. DOI: 10.7554/eLife.52443. Design: cross-sectional, multimodal. N=22 (fPET/fMRI during Tetris); N=10 (resting state). No genetic data. Shows that the metabolic cost of cognition is concentrated at the **initial rest-to-task transition** rather than scaling linearly with difficulty. Further load increases modulate existing metabolic patterns rather than creating new demands. This directly supports the \~5% whole-brain increment claim — the metabolic "startup cost" of engaging cognition is substantial but does not scale proportionally.

**Dembitskaya Y et al.** "Lactate supply overtakes glucose when neural computational and cognitive loads scale up." *PNAS*, 2022, 119(47): e2212004119. DOI: 10.1073/pnas.2212004119. Design: **animal model** (rat), electrophysiology \+ two-photon imaging \+ behavioral \+ computational modeling. N=12–15 rats per behavioral group. No genetic data. Demonstrates that lactate is mandatory for high-demand synaptic plasticity (theta-burst LTP) while glucose suffices for lighter forms (spike-timing-dependent plasticity), and that this extends to cognitive tasks requiring high attentional loads. From Magistretti's group, this paper resolves the decades-long substrate debate by showing it is not either/or — glucose and lactate are differentially allocated depending on computational demands. The mathematical modeling predicts the switch point based on the number of postsynaptic stimulations.

**Padamsey Z et al.** "Neocortex saves energy by reducing coding precision during food scarcity." *Neuron*, 2022, 110(2): 280–296.e10. DOI: 10.1016/j.neuron.2021.10.024. Design: **animal model** (mouse), electrophysiology \+ two-photon imaging \+ behavioral. Shows that food restriction reduces AMPA receptor conductance in mouse V1, cutting synaptic ATP use by **29%**, while preserving spike rates through compensatory mechanisms — at the cost of 32% broader orientation tuning and impaired fine visual discrimination, regulated by leptin. This is the first direct demonstration that the brain trades coding precision for energy savings in mammals, with the leptin-mediated metabolic rheostat demonstrating a hormonal link between peripheral energy stores and central coding fidelity.

**Tingley D et al.** "A metabolic function of the hippocampal sharp wave-ripple." *Nature*, 2021, 597(7874): 82–86. DOI: 10.1038/s41586-021-03811-w. Design: **animal model** (rat), electrophysiology \+ optogenetics \+ continuous glucose monitoring. N=45 rats. This paradigm-shifting paper from the Buzsáki lab shows that clusters of hippocampal sharp-wave ripples reliably predict decreases in peripheral blood glucose within \~10 minutes, via the lateral septum–hypothalamus pathway, causally verified by optogenetic induction and chemogenetic silencing. A canonical cognitive activity pattern simultaneously serves a metabolic homeostatic function, establishing that cognition and metabolism are causally linked through shared neural architecture.

**Klug S et al.** "Task-evoked metabolic demands of the posteromedial default mode network are shaped by dorsal attention and frontoparietal control networks." *eLife*, 2023, 12: e84683. DOI: 10.7554/eLife.84683. Design: cross-sectional, multimodal fPET/fMRI. N=50 (Tetris task); N=23 (working memory); N=18 (simple visual/motor). Resolves an apparent contradiction: the DMN's metabolic response during task depends on which task-positive network is engaged. Simple tasks produce concordant BOLD-metabolic decreases, while cognitively complex tasks produce dissociation (negative BOLD but preserved glucose metabolism), suggesting the DMN plays an active, metabolically costly role in supporting complex cognition.

**Goyal MS et al.** "Persistent metabolic youth in the aging female brain." *PNAS*, 2019, 116(8): 3251–3255. DOI: 10.1073/pnas.1815917116. Design: cross-sectional, machine learning on PET data. N=205 adults (ages 20–82). Using multiparametric PET, demonstrates that female brains appear \~3.8 years metabolically younger than chronological age. The largest metabolic brain aging study with full multiparametric PET data, it establishes sex as a critical variable in brain energetics and suggests developmental metabolic programming influences lifelong aging trajectories.

**Jamadar SD et al.** "Metabolic and hemodynamic resting-state connectivity of the human brain." *Cerebral Cortex*, 2021, 31(6): 2855–2867. DOI: 10.1093/cercor/bhaa393. Design: methods-validation, cross-sectional. N=26 healthy adults. Establishes that fPET-derived metabolic connectivity patterns are distinct from BOLD-derived functional connectivity, with the greatest divergence in sensory networks. Metabolic connectivity captures complementary information about brain organization that cannot be inferred from fMRI alone — the empirical foundation for understanding metabolism as an independent dimension of brain architecture.

---

## **2\. The astrocyte-neuron lactate shuttle has been complicated, not resolved**

### **State of play**

The ANLS hypothesis — that glutamate uptake by astrocytes stimulates aerobic glycolysis, producing lactate shuttled to neurons as their primary fuel — has arrived at a revised, more nuanced model rather than simple confirmation or rejection after three decades.

Where consensus exists: astrocytes are more glycolytic than neurons and release lactate upon arousal and noradrenergic signaling (directly demonstrated in vivo by Zuend et al. 2020). A lactate gradient from astrocytes to neurons exists in vivo (Mächler et al. 2016). Lactate serves as both energy substrate and signaling molecule for plasticity and memory.

Where genuine controversy persists: the classical claim that neurons depend primarily on astrocyte-derived lactate and have minimal glycolytic capacity has been substantially challenged. Díaz-García et al. (2017) showed neuronal stimulation triggers direct neuronal glycolysis, not lactate uptake. Li et al. (2023) demonstrated with neuron-specific GLUT3 and PKM1 knockouts that neurons require glucose uptake and glycolysis in vivo. Dienel and Rothman have shown quantitatively that astrocytic metabolic rates, when corrected for cell volume fraction, are far higher than recognized — meaning glycogen-derived lactate likely fuels astrocytic needs rather than being shuttled to neurons.

The **emerging revised model** holds that neurons possess more metabolic flexibility than ANLS assumed, with substantial LDHA expression and direct glucose utilization. The strict metabolic compartmentalization (LDHB-only in neurons, LDHA-only in astrocytes) has been overturned by single-cell RNA sequencing. The glucose-versus-lactate reliance appears context-dependent — varying with activity intensity, cell type, brain region, age, and sex. The most compelling reconciliation comes from Dembitskaya et al. (2022): glucose suffices for lighter neural activity, but lactate becomes mandatory when computational demands scale up.

A transformative feature of this literature since \~2016 is the deployment of genetically encoded metabolic biosensors (Laconic, Peredox, SweetieTS, iLACCO, eLACCO) combined with two-photon microscopy in awake behaving animals. Both sides of the ANLS debate now use these tools, which has sharpened the empirical basis considerably. The key limitation remains that most genetically encoded sensor work is in mice.

### **Key empirical papers**

**Díaz-García CM et al.** "Neuronal Stimulation Triggers Neuronal Glycolysis and Not Lactate Uptake." *Cell Metabolism*, 2017, 26(2): 361–374.e4. DOI: 10.1016/j.cmet.2017.06.021. Design: **animal model** (mouse hippocampal slices \+ awake two-photon). Using genetically encoded biosensors (Peredox for NADH/NAD+, SweetieTS for glucose), demonstrates that neuronal metabolic responses to stimulation reflect increased direct glucose consumption, not lactate uptake. Blocking MCT-mediated lactate transport did not prevent stimulation-induced NADH transients, while glucose transporter inhibition did. This is the single most-cited empirical challenge to the classical ANLS model and launched the "neurons do their own glycolysis" line of evidence.

**Zuend M et al.** "Arousal-induced cortical activity triggers lactate release from astrocytes." *Nature Metabolism*, 2020, 2(2): 179–191. DOI: 10.1038/s42255-020-0170-4. Design: **animal model** (mouse), two-photon in vivo with glycogen synthase knockout mice. First direct in vivo demonstration that arousal-induced cortical activation triggers a fast lactate dip in astrocytes coupled with extracellular lactate surge, dependent on β-adrenergic signaling and glycogen stores. The strongest in vivo, cell-type-resolved evidence supporting the astrocyte-to-neuron lactate flux, using the same Laconic sensor technology as the ANLS-challenging papers.

**Li H et al.** "Neurons require glucose uptake and glycolysis in vivo." *Cell Reports*, 2023, 42(4): 112335\. DOI: 10.1016/j.celrep.2023.112335. Design: **animal model** \+ human iPSC neurons (conditional knockouts, hyperpolarized ¹³C MRS, behavioral testing, spatial genomics). The most comprehensive genetic test of whether neurons can survive on lactate alone — they cannot. Deleting either the neuronal glucose transporter (GLUT3) or neuronal pyruvate kinase (PKM1) causes age-dependent learning and memory deficits. Female GLUT3 knockout mice show more severe phenotypes, hinting at sex-dependent metabolic vulnerabilities. Spatial genomics revealed compensatory galactose metabolism.

**Dienel GA, Rothman DL.** "Reevaluation of Astrocyte-Neuron Energy Metabolism with Astrocyte Volume Fraction Correction." *Neurochemical Research*, 2020, 45(11): 2607–2630. DOI: 10.1007/s11064-020-03125-9. Design: computational re-analysis of 31 published studies. When astrocytic metabolic rates are corrected for cell volume fraction (\~6–15% of tissue), astrocytic glucose oxidation rates are **4–10 fold higher** than neuronal rates — challenging the "astrocytes feed hungry neurons" narrative. This deceptively simple volume-fraction correction had been overlooked and fundamentally changes the energetic bookkeeping of the ANLS hypothesis.

**Meyer DJ et al.** "The Na+/K+ pump dominates control of glycolysis in hippocampal dentate granule cells." *eLife*, 2022, 11: e81645. DOI: 10.7554/eLife.81645. Design: **animal model** (mouse hippocampal slices), two-photon biosensor imaging. From the Yellen lab, identifies the specific ATPase that drives neuronal glycolysis: the Na+/K+ pump. Neuronal firing → Na+ influx → Na+/K+ pump activation → ATP consumption → glycolysis activation. Because the pump is in the neuronal membrane, this implies glycolysis must be local to neurons rather than outsourced to astrocytes.

**Frame AK et al.** "Altered neuronal lactate dehydrogenase A expression affects cognition in a sex- and age-dependent manner." *iScience*, 2024, 27(7): 110342\. DOI: 10.1016/j.isci.2024.110342. Design: **animal model** (conditional neuronal LDHA mice, behavioral testing across ages and sexes). Neuronal LDHA — the "astrocytic" isoform according to classical ANLS — is expressed in neurons and functionally important for cognition, but with a surprise: LDHA knockout in older mice actually improves cognition, suggesting that accumulation of neuronally-produced lactate may become detrimental with aging.

**Nagai T et al.** "Lactate biosensors for spectrally and spatially multiplexed fluorescence imaging." *Nature Communications*, 2023, 14: 6598\. DOI: 10.1038/s41467-023-42230-5. Design: methods-validation. Reports eLACCO2.1 (green, extracellular) and R-iLACCO1 (red, intracellular) — a spectrally orthogonal pair enabling simultaneous imaging of extracellular and intracellular lactate dynamics for the first time. The color orthogonality also allows multiplexing with calcium sensors. This tool enables the critical experiment: simultaneously watching lactate leave astrocytes and enter neurons (or not).

**Rothman DL, Behar KL, Dienel GA.** "Mechanistic stoichiometric relationship between the rates of neurotransmission and neuronal glucose oxidation." *Journal of Neurochemistry*, 2022, 168(5): 555–591. DOI: 10.1111/jnc.15619. Design: computational modeling based on in vivo MRS flux data. The \~1:1 stoichiometry between neuronal glucose oxidation and glutamate-glutamine cycling is robust, and about half of neuronal glucose oxidation may be linked to neurotransmission localized in pre-synaptic structures. Provides the quantitative metabolic framework for why neurons must oxidize glucose locally.

---

## **3\. Mitochondrial contributions to normal-range cognitive differences remain a genuine gap**

### **State of play**

**This sub-area is genuinely thin, and that thinness is itself a significant finding.** No study has taken a large healthy cohort, measured mitochondrial function, and correlated it with psychometric cognitive ability. The space that should exist — mitochondrial efficiency as a source of normal-range cognitive individual differences — is almost entirely unoccupied.

What does exist falls into three categories. First, a vigorous emerging program of mitochondrial psychobiology centered on Martin Picard's lab at Columbia, which has established foundational tools (MitoBrainMap, Mitochondrial Health Index, MiSBIE study platform) and begun connecting mitochondrial phenotypes to behavioral variation — but primarily in animal models, disease-spectrum populations, or postmortem tissue. Second, large-cohort epidemiological studies linking peripheral blood mtDNA copy number to cognitive function, but framed as AD/dementia endophenotypes rather than normal-range variation. Third, mechanistic animal studies establishing that brain mitochondrial diversity predicts behavioral variation and that mitochondrial transcription-activity coupling drives cognitive capacity.

An investigator entering this space with a healthy human cohort, both mitochondrial phenotyping and cognitive testing, and appropriate statistical power would be publishing in a near-vacuum.

### **Key empirical papers**

**Mosharov EV et al.** "A human brain map of mitochondrial respiratory capacity and diversity." *Nature*, 2025, 641(8063): 749–758. DOI: 10.1038/s41586-025-08740-6. Design: methods-validation/atlas (single donor brain \+ \~1,870 HCP subjects for MRI regression). Grey matter has \>50% more mitochondria than white matter, and recently-evolved cortical areas have mitochondria biochemically specialized for higher energy transformation efficiency. The MRI regression model opens the door to in vivo estimation of mitochondrial phenotypes from standard neuroimaging — something that does not currently exist. Currently based on a single brain, which is a major limitation, but the lab is now profiling \~500 brains.

**Zhang Y et al.** (NHLBI TOPMed Program). "Association of Mitochondrial DNA Copy Number With Brain MRI Markers and Cognitive Function." *Neurology*, 2023, 100(18): e1930–e1943. DOI: 10.1212/WNL.0000000000207157. Design: cross-sectional and prospective meta-analysis. **N≈8,000** dementia-free participants across 9 cohorts. Genetic data present (WGS for mtDNA CN). Higher blood mtDNA copy number is significantly associated with better current and future cognitive function. Mendelian randomization did not support a causal role, suggesting mtDNA CN may be a biomarker of underlying bioenergetic health rather than a direct cause.

**Rosenberg AM et al.** "Brain mitochondrial diversity and network organization predict anxiety-like behavior in male mice." *Nature Communications*, 2023, 14: 4726\. DOI: 10.1038/s41467-023-39941-0. Design: **animal model**, cross-sectional. N=27 mice, 571 brain tissue samples across 17 regions. A cortico-striatal mitochondrial network accounts for up to **50%** of animal-to-animal behavioral differences in anxiety/stress responses — the first systematic demonstration that brain mitochondrial variation predicts individual differences in behavior at brain-wide scale.

**Trumpff C et al.** "Psychosocial experiences are associated with human brain mitochondrial biology." *PNAS*, 2024, 121(27): e2317673121. DOI: 10.1073/pnas.2317673121. Design: longitudinal antemortem assessments \+ postmortem brain proteomics. **N≈400** from ROSMAP cohort. Positive psychosocial experiences (purpose in life, social network size) associate with greater OxPhos complex I abundance in prefrontal cortex; negative experiences (neuroticism, loneliness) with lower abundance. Combined, psychosocial factors explain **18–25%** of OxPhos complex I variance. First direct evidence linking subjective human experience to mitochondrial biology in the brain. Single-nucleus RNA-seq revealed that associations are strongly cell-type-specific.

**Li W et al.** "Boosting neuronal activity-driven mitochondrial DNA transcription improves cognition in aged mice." *Science*, 2024, 386(6728): eadp6547. DOI: 10.1126/science.adp6547. Design: **animal model**, mechanistic. Neuronal excitation triggers mitochondrial DNA transcription through a novel E-TCmito pathway (via mitochondrial CaMKII and CREB); this coupling weakens with age, and restoring it rescues cognitive function in aged mice. The strongest mechanistic link yet between mitochondrial gene expression and learning/memory. Variation in E-TCmito efficiency could be a molecular source of individual cognitive differences.

**Tian R et al.** "Mitochondrial DNA copy number associated dementia risk by somatic mutations and frailty." *GeroScience*, 2024\. DOI: 10.1007/s11357-024-01355-1. Design: prospective longitudinal. **N=189,566** UK Biobank participants. Higher blood mtDNA CN associates with lower subsequent dementia risk and better cognitive performance, modified by somatic mtDNA mutations (microheteroplasmies). By far the largest single study linking a mitochondrial measure to cognitive outcomes.

### **Notable gaps as findings**

No study of mitochondrial biology and psychometric intelligence in healthy young adults exists. No twin/family studies of mitochondrial phenotypes and cognition have been conducted despite the unique maternal inheritance of mtDNA. No in vivo human brain mitochondrial measurement exists yet. No well-powered mtDNA haplogroup-cognition studies in healthy populations have been published despite the availability of mtDNA genotyping in existing biobanks.

---

## **4\. Whole-body energy budgets and brain metabolism: a thin but promising frontier**

### **State of play**

**This sub-area is genuinely thin at the direct intersection of its core questions.** The constrained total energy expenditure model (Pontzer) and the expensive brain hypothesis (Aiello and Wheeler) are powerful evolutionary frameworks that should be connected to brain metabolic allocation — but almost no one has empirically tested that specific connection. No study has combined doubly-labeled water measures of total energy expenditure with simultaneous brain metabolic imaging in the same individuals. The Pontzer lab discusses organ-level allocation in general terms but has not published direct empirical tests of brain energy allocation within the constrained model. The Kuzawa lab has generated the strongest empirical work connecting brain energetics to body composition trade-offs during development, but this work relies on aggregate or cross-sectional data.

The most provocative finding comes from an unexpected source: artificially selected high-BMR mice did not develop larger brains but showed superior learning and enhanced hippocampal LTP (Goncerzewicz et al. 2022), suggesting that energy may be allocated to brain function (synapse quality, plasticity) rather than brain size. This finding implies the field should pivot from brain size to brain metabolic efficiency as the key variable.

### **Key empirical papers**

**Pontzer H et al.** (IAEA DLW Consortium). "Daily energy expenditure through the human life course." *Science*, 2021, 373(6556): 808–812. DOI: 10.1126/science.abe5017. Design: cross-sectional mega-analysis. **N=6,421** individuals (ages 8 days to 95 years, 29 countries). Defines four distinct metabolic life stages. Brain and liver are identified as driving elevated tissue-specific metabolic rates in early life. The definitive lifespan energy expenditure map against which brain-specific energetics must be understood. The finding that observed basal expenditure exceeds organ-based estimates by \~30% in early life represents exactly where brain metabolic variation should be investigated.

**Kuzawa CW, Blair C.** "A hypothesis linking the energy demand of the brain to obesity risk." *PNAS*, 2019, 116(27): 13266–13275. DOI: 10.1073/pnas.1816908116. Design: computational synthesis with quantitative modeling. Establishes a formal framework proposing that individual variation in childhood brain energy expenditure (peaking at **66% of RMR** at \~age 5\) could explain variation in the timing of adiposity rebound and subsequent obesity risk. Critically notes that BMI-elevating genetic variants are disproportionately expressed in the brain, suggesting a genetic architecture for brain-body energy trade-offs.

**Blair C, Kuzawa CW, Willoughby MT.** "The development of executive function in early childhood is inversely related to change in body mass index." *Developmental Science*, 2020, 23(1): e12860. DOI: 10.1111/desc.12860. Design: longitudinal. **N=1,292** children (ages 2–5). Within-individual gains in executive function are inversely related to BMI changes — the best available within-individual test of the brain-body energy trade-off during the critical period when brain energy demands peak. Effect size is modest, and the inference chain is indirect (EF change is a proxy for brain energetics), but the large sample and longitudinal design are strengths.

**Aronoff JE et al.** "Why do humans undergo an adiposity rebound?" *International Journal of Obesity*, 2022, 46(5): 1044–1050. DOI: 10.1038/s41366-022-01065-8. Design: cross-sectional, MRI-based 4D flow. N=82 healthy individuals (ages 0–60). First study comparing developmental trajectories of brain metabolism (via MRI-derived total cerebral blood flow) and BMI in the same individuals, finding inverse trajectories with peak TCBF at age 5.6 (close to BMI nadir at 4.9 years). A proof-of-concept that non-invasive MRI can proxy brain energy expenditure.

**Vandekar SN et al.** "Sex differences in estimated brain metabolism in relation to body growth through adolescence." *Journal of Cerebral Blood Flow and Metabolism*, 2019, 39(3): 524–535. DOI: 10.1177/0271678X17737692. Design: cross-sectional. **N=922** individuals (ages 8–21) from the Philadelphia Neurodevelopmental Cohort. The largest sample demonstrating the brain-body metabolic inverse relationship through adolescence, extending it to sex differences for the first time: females achieve maximum body growth \~2 years earlier with correspondingly earlier stabilization of brain metabolism.

**Urlacher SS et al.** "Constraint and trade-offs regulate energy expenditure during childhood." *Science Advances*, 2019, 5(12): eaax1065. DOI: 10.1126/sciadv.aax1065. Design: cross-sectional field study with doubly-labeled water. N=44 Shuar children \+ US/UK comparisons. First empirical demonstration of constrained TEE in children: Shuar children in a high-activity, high-pathogen population burn the same total daily calories as US/UK children despite being \~25% more physically active. Trade-offs are between immune function and growth, but brain energy allocation is explicitly noted as the major unexplored component.

**Goncerzewicz A et al.** "Brain size, gut size and cognitive abilities: the energy trade-offs tested in artificial selection experiment." *Proceedings of the Royal Society B*, 2022, 289(1972): 20212747\. DOI: 10.1098/rspb.2021.2747. Design: **animal model** — experimental evolution (\~70 generations of artificial selection in mice). High-BMR mice had larger guts and visceral organs but NOT larger brains. However, they showed superior learning and enhanced hippocampal LTP. This dissociation between organ size and cognitive function suggests the expensive brain hypothesis may need revision — energy may be allocated to brain function rather than brain size.

---

## **5\. Metabolic psychiatry has more institutional momentum than mechanistic proof**

### **State of play**

The metabolic theory of mental illness occupies an interesting epistemic position. **The enthusiasm substantially outpaces the causal mechanistic evidence, but the circumstantial case is genuinely strong and growing.** What exists: robust epidemiological data showing metabolic abnormalities precede psychiatric onset by years (Perry et al. 2021); consistent MRS evidence of bioenergetic deficits in psychotic disorders; emerging genetic and Mendelian randomization evidence that metabolic genes have causal effects on psychiatric risk; and a compelling dopamine-metabolism coupling story in schizophrenia. What is missing: large-scale prospective brain imaging studies tracking metabolic changes before psychiatric onset; definitive causal directionality in most human studies; and any substantial psychiatric-specific basic science on ketogenic diet mechanisms (most is borrowed from epilepsy literature).

This is not a fringe position — it publishes in *JAMA Psychiatry*, *Molecular Psychiatry*, and *Nature Mental Health*, and the May 2024 Ernst Strüngmann Forum produced a landmark book (*Metabolic Neuropsychiatry*, Springer 2025\) authored by \~39 experts. But it is still a hypothesis-rich, proof-poor field. The strongest causal evidence is for specific disorder-metabolic pathway pairs (insulin resistance → psychosis; bioenergetic deficits → schizophrenia) rather than a unified metabolic theory of all mental illness.

Palmer's *Brain Energy* theory is integrative and stimulating but relies primarily on reinterpreting other investigators' empirical work through a metabolic lens. The Baszucki Group has invested $60M+ philanthropically, funding \~20 clinical trials, but mechanistic research is still catching up.

### **Key empirical papers**

**Perry BI et al.** "Longitudinal Trends in Childhood Insulin Levels and Body Mass Index and Associations With Risks of Psychosis and Depression in Young Adults." *JAMA Psychiatry*, 2021, 78(4): 416–425. DOI: 10.1001/jamapsychiatry.2020.4180. Design: longitudinal (ALSPAC birth cohort). N=5,790 (FI data), 10,463 (BMI data). Persistently high fasting insulin levels from age 9 are associated with psychosis at age 24 (**aOR 3.22**). The strongest temporal-precedence evidence that metabolic dysfunction is upstream of psychosis, directly challenging the view that metabolic problems are merely consequences of illness or medication. Growth mixture modeling reveals disorder-specific trajectories: insulin → psychosis; puberty-onset BMI increase → depression.

**Wu Q et al.** "Prefrontal cortical dopamine deficit may cause impaired glucose metabolism in schizophrenia." *Translational Psychiatry*, 2024, 14: 76\. DOI: 10.1038/s41398-024-02800-7. Design: multi-design — cross-sectional human (**N=704** drug-naïve first-episode psychosis), prospective TMS intervention (N=57), and **animal model** (optogenetic/chemogenetic). One of the few studies providing a complete translational bridge: human association, human intervention, and animal causal mechanism connecting prefrontal dopamine deficiency to metabolic dysfunction. Optogenetic suppression of VTA→mPFC dopamine projection is sufficient to produce glucose intolerance in mice.

**Sauerzopf U et al.** "Disrupted relationship between blood glucose and brain dopamine D2/3 receptor binding in patients with first-episode schizophrenia." *NeuroImage: Clinical*, 2021, 32: 102813\. DOI: 10.1016/j.nicl.2021.102813. Design: cross-sectional dual-PET imaging. N=19 controls, 25 unmedicated first-episode schizophrenia. The normal positive correlation between blood glucose and brain D2/3 receptor binding is disrupted in drug-naïve first-episode schizophrenia, particularly in the VTA. Direct neuroimaging evidence that dopamine-glucose metabolic coupling is fundamentally broken in early psychosis, independent of medication.

**Lu Y et al.** "Genetic insights into the role of mitochondria-related genes in mental disorders." *Journal of Affective Disorders*, 2025, 380: 685–695. DOI: 10.1016/j.jad.2025.03.116. Design: computational (SMR \+ multi-omics). GWAS summary statistics for 7 psychiatric disorders; 1,136 mitochondria-related genes. Identifies specific genes with multi-omics causal evidence: RMDN1 for ADHD, ETFA and MMAB increasing schizophrenia risk, ACADVL and PPA2 decreasing it. Importantly, null findings for bipolar, MDD, anxiety, ASD, and PTSD constrain the "mitochondrial dysfunction causes all mental illness" claim, suggesting specificity for schizophrenia and ADHD.

**Gilchrist L et al.** "Evaluating metabolome-wide causal effects on risk for psychiatric and neurodegenerative disorders." *BMC Medicine*, 2025, 23(1): 326\. DOI: 10.1186/s12916-025-04129-4. Design: computational (MR \+ colocalization). \~1,000 plasma metabolites; GWAS for 8 disorders. Identifies 85 causal metabolite-disorder associations; sphingolipid metabolism specifically implicated in psychiatric risk; **29 metabolite-disorder pairs colocalize at the FADS gene cluster** on chromosome 11 involving linoleic/arachidonic acid lipids. No single metabolite had causal effects on both a psychiatric and a neurodegenerative disease, arguing against a single "metabolic dysfunction → all brain disease" narrative.

**Aslanoglou D et al.** "Dopamine regulates pancreatic glucagon and insulin secretion via adrenergic and dopaminergic receptors." *Translational Psychiatry*, 2021, 11: 59\. DOI: 10.1038/s41398-020-01171-z. Design: mechanistic cell biology / **animal model**. Pancreatic alpha and beta cells synthesize dopamine endogenously; dopamine regulates both insulin and glucagon secretion via D2-like receptors AND adrenergic receptors, establishing a bidirectional signaling pathway between dopaminergic and metabolic systems. From Freyberg's lab, this provides the molecular basis for why D2-blocking antipsychotics cause metabolic dysfunction.

**Bhattacharyya U et al.** "Circulating Blood-Based Proteins in Psychopathology and Cognition: A Mendelian Randomization Study." *JAMA Psychiatry*, 2025, 82(5): 481–491. DOI: 10.1001/jamapsychiatry.2025.0033. Design: computational (proteomic MR). 2,923–4,719 proteins per 34,557–35,559 individuals; SCZ 67K cases/93K controls; MDD 167K/508K. Identifies 113 Bonferroni-corrected protein-disorder associations (46 novel); immune-related proteins show pleiotropic effects across psychiatric and cognitive phenotypes. The largest proteomic MR study of psychiatric disorders to date.

---

## **6\. Developmental and aging brain metabolism reveals a coherent arc from aerobic glycolysis to ketone rescue**

### **State of play**

Brain metabolism follows a dramatic lifespan trajectory. Aerobic glycolysis peaks in childhood when synaptic growth rates are highest, accounts for 10–12% of adult brain glucose consumption, and declines progressively to near-zero by age 60\. This trajectory is not merely a curiosity — it appears mechanistically linked to developmental plasticity, sex differences in brain aging, resilience against Alzheimer's pathology, and the ability to use alternative fuel sources.

The Goyal lab at Washington University has produced the most coherent body of work, establishing that aerobic glycolysis is a signature of developmental neoteny that correlates with transcriptional programs for synapse formation. Females retain more metabolically "youthful" brain profiles across the entire adult lifespan. In aging, the critical finding is not that glucose metabolism simply declines, but that **ketone body utilization capacity is preserved** even as glucose uptake fails — the Cunnane lab's dual-tracer PET work demonstrated this is true even in Alzheimer's disease.

Large longitudinal cohorts (ABCD, UK Biobank) are beginning to be used for brain metabolic studies, but mostly via MRI-derived proxies rather than direct metabolic imaging. Direct PET-based developmental trajectories remain limited to cross-sectional designs and moderate samples. The NAD+ decline story in aging brain is mechanistically compelling, with restoration of NAD+ through precursor supplementation shown to rescue myelination capacity and cognitive function in aged animal models.

### **Key empirical papers**

**Goyal MS et al.** "Loss of brain aerobic glycolysis in normal human aging." *Cell Metabolism*, 2017, 26(2): 353–360.e3. DOI: 10.1016/j.cmet.2017.07.010. Design: cross-sectional (PET). N≈200 cognitively normal adults (ages 20–82). Foundational paper showing that age-related decreases in brain glucose uptake exceed those of oxygen use, resulting in progressive AG loss. Brain regions with highest AG in young adults (medial frontal cortex, precuneus) show the most rapid age-related AG loss — regions that also show the highest transcriptional neoteny (r \= −0.87). Included here despite 2017 date because it initiated the entire AG-resilience research program.

**Goyal MS et al.** "Brain aerobic glycolysis and resilience in Alzheimer disease." *PNAS*, 2023, 120(7): e2212256120. DOI: 10.1073/pnas.2212256120. Design: cross-sectional with longitudinal elements. N=285, 313 PET sessions. Cognitive impairment is associated with loss of youthful AG patterns, but amyloid-positive yet cognitively unimpaired individuals actually preserve youthful AG — even higher than amyloid-negative controls. This reframes aerobic glycolysis from developmental relic to marker of cognitive resilience.

**Mujica-Parodi LR et al.** "Diet modulates brain network stability, a biomarker for brain aging, in young adults." *PNAS*, 2020, 117(11): 6170–6177. DOI: 10.1073/pnas.1913042117. Design: large-scale fMRI lifespan datasets (total N=928) \+ targeted experiments in younger adults using 7T fMRI. Brain network destabilization correlates with age and accelerates with insulin resistance, with effects emerging at \~47 years. In younger adults, brain networks were destabilized by glucose and **stabilized by ketones** within 30 minutes, regardless of whether ketosis was achieved through diet or exogenous ketone ester. Ketones increase Gibbs free energy for ATP by 27% compared to glucose. First direct experimental evidence that switching brain fuel source can reverse a functional biomarker of aging. Note: some authors have financial interests in ketone ester products.

**Cunnane SC et al.** "Can Ketones Help Rescue Brain Fuel Supply in Later Life?" *Frontiers in Molecular Neuroscience*, 2016, 9: 53\. DOI: 10.3389/fnmol.2016.00053. Design: dual-tracer PET (¹⁸F-FDG \+ ¹¹C-acetoacetate). Demonstrates that brain ketone uptake remains normal in AD and MCI even where glucose uptake is impaired, and that interventions raising peripheral ketone levels directly increase brain ketone utilization. Pioneering dual-tracer evidence establishing the preserved ketone utilization pathway.

**Li W et al.** "Boosting neuronal activity-driven mitochondrial DNA transcription improves cognition in aged mice." *Science*, 2024, 386(6728): eadp6547. DOI: 10.1126/science.adp6547. Design: **animal model**, mechanistic. Neuronal excitation triggers mtDNA transcription through a novel E-TCmito pathway; this coupling weakens with age, and restoring it rescues cognitive function. Provides a direct molecular mechanism by which mitochondrial transcription efficiency could determine cognitive capacity, with the age-dependent weakening explaining individual variation in cognitive aging rate.

**Ma X-R et al.** "Restoring nuclear entry of Sirtuin 2 in oligodendrocyte progenitor cells promotes remyelination during ageing." *Nature Communications*, 2022, 13: 1225\. DOI: 10.1038/s41467-022-28844-1. Design: **animal model** (mouse). In aging OPCs, nuclear entry of SIRT2 is impaired and NAD+ levels are reduced. Supplementation with β-NMN rescued SIRT2 nuclear entry, restored OPC differentiation, and promoted remyelination. Demonstrates that age-related NAD+ decline directly impairs myelination capacity and this can be reversed — a concrete example of metabolic intervention rejuvenating brain repair.

**Kolbeinsson A et al.** "Accelerated MRI-predicted brain ageing and its associations with cardiometabolic and brain disorders." *Scientific Reports*, 2020, 10: 19940\. DOI: 10.1038/s41598-020-76518-z. Design: cross-sectional, UK Biobank. **N\>37,000**. Accelerated brain aging is significantly associated with type 1 and type 2 diabetes, elevated BMI, and poorer cognitive function across \>1,410 phenome-wide traits. Large-scale population evidence that systemic metabolic health is tightly coupled to brain aging rates.

**Sanchez-Roman I et al.** "Molecular markers of DNA repair and brain metabolism correlate with cognition in centenarians." *GeroScience*, 2022, 44(1): 103–125. DOI: 10.1007/s11357-021-00502-2. Design: cross-sectional. N=120 Danish centenarians. NAD+/NADH levels in plasma positively correlate with cognitive capacity; mitochondrial respiration is surprisingly well preserved compared to young adults. First direct human evidence linking NAD+ levels to cognitive preservation at extreme old age.

---

## **7\. New methods are enabling questions that could not be asked five years ago**

### **State of play**

The methodological landscape spans five transformative fronts. **Genetically encoded metabolic sensors** (GRAB-ATP, iGlucoSnFR2, Laconic, PercevalHR, eLACCO/iLACCO) now enable two-photon imaging of glucose, lactate, and ATP at subcellular resolution in behaving animals. **Functional PET** via continuous FDG infusion has improved temporal resolution from \~30 minutes to 3 seconds and, on hybrid PET/MR scanners, enables concurrent measurement of glucose metabolism and BOLD activity. **Deuterium metabolic imaging** maps the metabolic fate of glucose noninvasively using oral deuterium-labeled glucose on standard clinical MRI scanners — the most scalable technique for human metabolic flux imaging. **Hyperpolarized ¹³C MRI** has been translated to human brain and provides real-time enzymatic flux measurements (pyruvate→lactate, pyruvate→bicarbonate). **Single-cell spatial metabolomics** via MALDI-MSI can profile \>100 metabolites per cell in tissue sections. Together, these span temporal scales from sub-seconds to hours and spatial scales from subcellular to whole-brain.

### **Key empirical papers**

**Wu Z et al.** "A sensitive GRAB sensor for detecting extracellular ATP in vitro and in vivo." *Neuron*, 2022, 110(5): 770–782.e5. DOI: 10.1016/j.neuron.2021.11.027. Design: methods-validation / **animal model** (mouse, zebrafish). From the Yulong Li lab (Peking University). The first genetically encoded sensor with nanomolar ATP affinity and \>700% ΔF/F₀ dynamic range, enabling direct visualization of ATP release at individual astrocytes during neuroinflammation. The GRAB platform architecture is extensible — the same lab has produced sensors for dopamine, norepinephrine, serotonin, and adenosine.

**Díaz-García CM et al.** "Quantitative in vivo imaging of neuronal glucose concentrations with a genetically encoded fluorescence lifetime sensor." *Journal of Biological Chemistry*, 2019, 294(45): 17135–17148. DOI: 10.1074/jbc.RA119.009906. Design: methods-validation / **animal model**. First demonstration of calibrated, quantitative glucose concentrations in living brain using fluorescence lifetime imaging (FLIM). Found intracellular glucose in hippocampal neurons is \~20% of extracellular concentration — a fundamental parameter for metabolic modeling. FLIM-based sensing is immune to photobleaching and expression level confounds, making it the gold standard for quantitative metabolite imaging.

**De Feyter HM et al.** "Deuterium metabolic imaging (DMI) for MRI-based 3D mapping of metabolism in vivo." *Science Advances*, 2018, 4(8): eaat7314. DOI: 10.1126/sciadv.aat7314. Design: methods-validation / human \+ **animal**. The foundational DMI paper, demonstrating that MR imaging of deuterium-labeled substrates can noninvasively map the metabolic fate of glucose in human brain, distinguishing where carbon goes — glycolysis (lactate) vs. oxidative metabolism (glutamate/glutamine). Requires only a simple ²H RF coil added to existing 3T scanners and oral administration of inexpensive, non-radioactive deuterium-labeled glucose, making it scalable far beyond PET.

**Hendriks AD et al.** "Deuterium metabolic imaging (DMI) of the human brain in vivo at 7T." *Magnetic Resonance in Medicine*, 2023, 89(3): 912–921. DOI: 10.1002/mrm.29498. Design: methods-validation / human. First full-brain volume DMI at 7T, leveraging supra-linear sensitivity gain to achieve well-resolved metabolite maps with complete volume coverage.

**Grist JT et al.** "Quantifying normal human brain metabolism using hyperpolarized \[1-¹³C\]pyruvate and magnetic resonance imaging." *NeuroImage*, 2019, 189: 171–179. DOI: 10.1016/j.neuroimage.2019.01.027. Design: methods-validation / human. First quantitative measurement of both glycolytic and oxidative pyruvate metabolism in normal human brain using hyperpolarized ¹³C MRI. The pyruvate→lactate rate constant (kPL) reflects cytosolic LDH activity; pyruvate→bicarbonate (kPB) reflects mitochondrial PDH. These are fundamentally different metabolic axes from what FDG-PET measures. A 2024 consensus paper (Larson et al., *MRM* 91: 2204–2228) has now standardized methods across 13 sites.

**Hahn A et al.** "High-temporal resolution functional PET/MRI reveals coupling between human metabolic and hemodynamic brain response." *European Journal of Nuclear Medicine and Molecular Imaging*, 2024, 51(5): 1310–1322. DOI: 10.1007/s00259-023-06542-4. (Also listed in Sub-area 1.) The highest temporal resolution for human brain glucose metabolic imaging at **3 seconds**, making fPET viable for event-related paradigms.

**Jamadar SD et al.** "Radiotracer administration for high temporal resolution positron emission tomography of the human brain: application to FDG-fPET." *Journal of Visualized Experiments*, 2019, (152): e60259. DOI: 10.3791/60259. Design: methods-validation / human. The methods cookbook for fPET — detailed protocols for constant infusion and bolus+infusion approaches with video demonstration. Lowers the barrier to entry by providing reproducible step-by-step instructions.

**Zürcher NR, Hahn A et al.** "Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep." *Nature Communications*, 2025, 16\. DOI: 10.1038/s41467-025-64414-x. Design: methods-application / human. Concurrent EEG, fPET, and fMRI during wakefulness-to-NREM transition. Reveals that a \~0.02 Hz sensorimotor network remains metabolically active during NREM sleep while the default mode network is metabolically suppressed. The state of the art in multimodal brain metabolic imaging.

**Rappez L et al.** "SpaceM reveals metabolic states of single cells." *Nature Methods*, 2021, 18(7): 799–805. DOI: 10.1038/s41592-021-01198-0. Design: methods-validation / computational \+ cell culture. Establishes the first accessible method for in situ single-cell metabolomics combining fluorescence microscopy with MALDI-MSI, profiling \>100 metabolites per cell at \>1,000 cells per hour. Directly applicable to neural tissue sections for profiling astrocyte vs. neuron vs. microglia metabolomes.

**iGlucoSnFR2** (Bhatt et al., *Science Advances*, 2025; DOI: 10.1126/sciadv.adz3889). Design: methods-validation / **animal model**. Second-generation glucose sensor significantly outperforming the original, calibratable to report absolute extracellular glucose concentrations in awake mice. Makes it possible to track glucose fluctuations at the single-cell level in living brain during behavior.

---

## **Lab and researcher mapping: where institutional momentum is concentrating**

### **Established leaders and what makes their work distinctive**

**Manu Goyal and Marcus Raichle** (Washington University, St. Louis) have produced the most coherent body of work in this field through their aerobic glycolysis research program. Goyal's multiparametric PET studies (n=205–285) are the largest available, and the AG-as-resilience-biomarker finding is being taken up across the AD and aging communities. Raichle's conceptual contributions (default mode network, resting metabolism) provided the intellectual foundation; Goyal has extended it into developmental neoteny, sex differences, and Alzheimer's resilience.

**Pierre Magistretti** (KAUST/Collège de France) originated the ANLS hypothesis and continues to produce high-impact empirical work. His group's 2022 PNAS paper demonstrating load-dependent substrate switching represents the most compelling reconciliation in the ANLS debate. His influence extends across computational neuroscience and synaptic plasticity.

**Gary Yellen** (Harvard Medical School) has fundamentally reshaped the ANLS debate through genetically encoded biosensor development and elegant experimental design. His lab's demonstration that neurons perform their own glycolysis (Díaz-García et al. 2017\) is the most-cited empirical challenge to the classical shuttle model. The FLIM-based quantitative glucose sensor represents the gold standard for in vivo metabolite measurement.

**Gerald Dienel and Douglas Rothman** (Yale) provide the quantitative rigor that keeps the ANLS debate honest. Their volume-fraction correction and stoichiometric analyses have forced the field to reconsider fundamental assumptions about astrocyte-neuron metabolic compartmentalization.

**Martin Picard** (Columbia) has created an entirely new sub-field — mitochondrial psychobiology — and built the infrastructure (MitoBrainMap, MiSBIE, Mitochondrial Health Index) that will define the next decade of work connecting mitochondrial biology to brain function and behavior. Inaugural recipient of the $1.5M Baszucki Prize in Science (March 2024). PI/MPI on 7 NIH R01s with a team of 15–20 scientists.

**Rupert Lanzenberger and Andreas Hahn** (Medical University of Vienna) are the technical leaders of functional PET. Their 3-second temporal resolution represents the state of the art, and their systematic characterization of metabolic-hemodynamic dissociations has changed how the default mode network is understood.

**Sharna Jamadar** (Monash University) has established metabolic connectivity as a distinct concept and demonstrated that fPET metabolic connectivity has greater predictive utility for age and cognition than fMRI functional connectivity. Selected as OHBM 2025 Keynote Speaker. Over $12M AUD in competitive funding.

**Stephen Cunnane** (Université de Sherbrooke) pioneered dual-tracer PET (FDG \+ ¹¹C-acetoacetate) and demonstrated that brain ketone uptake is preserved in Alzheimer's disease — the mechanistic foundation for ketone-based neurotherapeutics.

**Christopher Kuzawa** (Northwestern) and **Clancy Blair** (CU Denver) have developed the most sophisticated theoretical and empirical framework connecting brain energetics to body composition trade-offs during development, though their work needs direct metabolic imaging to advance beyond proxy measures.

**Bruno Weber** (ETH Zurich) and **L. Felipe Barros** (CECs, Chile) are central to the astrocyte metabolism and ANLS literature. Weber's lab deployed the Laconic sensor for in vivo two-photon lactate imaging; Barros has described the metabolic recruitment mechanisms by which active neurons harvest resources from surrounding astrocytes.

### **Rising stars doing cross-disciplinary work**

**Caroline Trumpff** (Columbia) co-leads the ROSMAP mind-mitochondria work and cell-free mtDNA as a stress biomarker, bridging molecular biology, psychiatry, and aging research.

**Benjamin Perry** (Cambridge) provides the critical epidemiological temporal precedence evidence that metabolic dysfunction precedes psychiatric onset — the foundational data for the metabolic psychiatry argument.

**Carlos Díaz-García** (post-Yellen lab) has moved the field from qualitative to quantitative metabolite imaging through FLIM-based genetically encoded sensors.

**Hendrikus De Feyter and Robin de Graaf** (Yale) invented deuterium metabolic imaging, arguably the most scalable new technique in the field.

**Zijing Wu and Yulong Li** (Peking University) have developed the GRAB sensor platform for ATP, dopamine, norepinephrine, and other molecules — creating an ecosystem for multi-analyte metabolic imaging that is being adopted worldwide.

**Zachary Freyberg** (University of Pittsburgh) provides the most innovative basic science connecting dopamine and metabolism through pancreatic islet biology, bridging pharmacology and metabolic neuroscience.

**Margaret Hahn** (University of Toronto/CAMH) is arguably the strongest empirical researcher in the metabolism-psychosis space, with work specifically targeting drug-naïve first-episode psychosis to disentangle intrinsic from iatrogenic metabolic dysfunction.

### **New centers, major grants, and convergence zones**

The **Ernst Strüngmann Forum** (May 2024, Frankfurt) convened \~39 experts and produced *Metabolic Neuropsychiatry* (Springer, 2025), co-edited by Dost Öngür and Judith Ford — the landmark publication marking this field's formal crystallization as a discipline.

The **Metabolic and Mental Health Program at McLean Hospital** (Harvard), funded by a $3M donation, combines research, education, and clinical practice under Chris Palmer. Öngür holds a **NIMH P50 Center Grant** for biological research in psychotic disorders with active grants through 2028\.

The **UK Hub for Metabolic Psychiatry** at the University of Edinburgh, led by Daniel Smith and Iain Campbell, launched September 2024 as part of a multi-million-pound UKRI Mental Health Platform with 100+ researchers.

The **MiSBIE Platform** at Columbia (Picard lab) hosted a December 2025 symposium with 620+ registrants, signaling growing community interest in mind-mitochondria research.

**Ana Cristina Andreazza** (University of Toronto) holds a Tier II Canada Research Chair and the Thomas C. Zachos Chair in Mitochondrial Research, and founded the **Mitochondrial Innovation Initiative (Mito2i)**, bridging neuropsychiatry and regenerative medicine.

The **Baszucki Group** (founded by Roblox CEO David Baszucki and Jan Ellison Baszucki) is the primary philanthropic driver: the $1.5M Baszucki Prize in Science, Metabolic Psychiatry Scholar Awards ($150K each, 6 awarded October 2025), Fresh Start Awards ($10K each), and Metabolic Mind nonprofit. They have invested **$60M+** and fund \~20 clinical trials.

### **Where the next generation is being trained**

The densest training pipelines are at **Columbia** (Picard lab, mitochondrial psychobiology), **Harvard/McLean** (Öngür/Du for MRS and bioenergetics in psychosis; Palmer for metabolic psychiatry), **Vienna** (Lanzenberger/Hahn for fPET/fMRI methodology), **Yale** (Rothman/de Graaf for MRS, DMI, and quantitative metabolic modeling), **Monash** (Jamadar for fPET methodology and metabolic connectivity), and **Harvard Medical School** (Yellen lab for genetically encoded sensor development). The **Peking University** neuroscience program (Yulong Li) is the leading center for GRAB sensor development. **Sherbrooke** (Cunnane) trains researchers in dual-tracer PET for ketone metabolism. **ETH Zurich** (Weber) trains in two-photon metabolite imaging. The **University of Toronto/CAMH** (Hahn, Andreazza) is emerging as a center for metabolic psychiatry research with strong clinical integration.

---

## **Cross-cutting observations and intelligence summary**

**The tools are ahead of the theory.** Functional PET, genetically encoded sensors, and deuterium metabolic imaging have opened measurement windows that the field has not yet fully exploited. The most conspicuous gap is the absence of large-cohort studies connecting brain metabolic phenotypes to genetic architecture — none of the fPET studies exceed n=50 for human participants, and no study has combined genome-wide data with direct brain metabolic imaging.

**Two sub-areas are genuine gaps, not mature fields.** Mitochondrial biology as a source of normal-range cognitive individual differences, and whole-body energy budget trade-offs involving the brain, are both startlingly underpopulated. An investigator entering either space with proper phenotyping, adequate sample sizes, and appropriate statistical power would face minimal competition.

**The ANLS debate has been productively complicated.** The binary framing (neurons use lactate vs. neurons use glucose) has given way to a context-dependent model where substrate reliance varies with computational demand, cell type, brain region, age, and sex. This is a genuine advance, not just fence-sitting — the reconciliation papers (especially Dembitskaya et al. 2022\) generate testable predictions.

**Metabolic psychiatry is institutionally real but mechanistically early.** The Strüngmann Forum, Baszucki funding, McLean program, and Edinburgh Hub signal that this is now a recognized field with institutional backing. But the strongest mechanistic evidence is concentrated in schizophrenia and specific dopamine-metabolism pathways; the broader claim that metabolic dysfunction causes psychiatric illness across diagnoses remains more aspiration than established fact.

**Sex differences are emerging as a major theme.** Female brains retain more metabolically youthful profiles across the lifespan (Goyal 2019), female mice show more severe phenotypes from neuronal glucose transporter knockout (Li et al. 2023), and neuronal LDHA knockout effects are sex- and age-dependent (Frame et al. 2024). This convergence across independent research programs suggests sex-specific brain metabolic biology is a real phenomenon deserving systematic investigation.

**The animal-to-human translation gap is the field's central challenge.** The most mechanistically compelling work (genetically encoded sensors, cell-type knockouts, optogenetics) is in mice. The human work has scale (UK Biobank, TOPMed) but crude metabolic measures (peripheral mtDNA copy number, MRI-derived proxies). The techniques that could bridge this gap — DMI, hyperpolarized ¹³C, fPET — are still in methods-validation stages for most applications. The field needs large-sample human studies using these newer techniques to mature from proof-of-concept to population-level discovery.

# **Metabolic Psychiatry (Palmer et al.)**

**Date:** 2026-03-10 **Source manifest:**

* \[NotebookLM responses, pasted in conversation\] 7 right-sized prompts \+ NotebookLM-recommended prompts from a notebook containing: Palmer *Brain Energy* chapters 1-21 (2022), Sethi (2022) ketogenic therapy review, Tang (2026) brain insulin resistance review, Cavaleri (2026) metabolomics biomarkers, Allen (2018) mitochondria and depression, Laurent (2025) keto case study, Ede (2026) Delphi consensus, plus supporting clinical and metabolic psychiatry sources (38 total).  
* \[google\_drive\_fetch: full doc\] BIO research doc loaded, duplicate-checked.  
* \[just-completed Pontzer constrained energy model extraction\] for convergence mapping.

**Duplicate check results:** Zero existing Palmer cards (BIO-PAL-\*). Palmer exists as: (1) bullets in Metabolic Harshness section ("Mental disorders are metabolic disorders of the brain"), (2) Immune System BC ("Palmer has the Vitality right. He has nothing else."), (3) BC-CEM-07 from Pontzer extraction ("Palmer is right about Vitality — confirmed, not qualified"). All mitochondrial mechanism cards below are new territory.

**Author codes and book abbreviations:**

* PAL \= Palmer; BRE \= Brain Energy  
* TAN \= Tang; BIR \= Brain Insulin Resistance  
* ALL \= Allen, Josh; MMD \= Mitochondria Mood Depression  
* VAR-MPY \= various authors, Metabolic Psychiatry (multi-source claims)

**Placement:** BIO doc, new subsection within or after existing Metabolic Harshness section. Title: "Metabolic Psychiatry: The Mitochondrial Level of the Energy Budget."

---

## **MITOCHONDRIAL EFFICIENCY AS INDEPENDENT VARIABLE**

---

### **BIO-VAR-MPY-01 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Within the brain's allocated energy share, the efficiency of mitochondrial ATP production matters independently of energy supply. In conditions like type 2 diabetes and obesity, cells have surplus fuel (high blood glucose) but remain energy-deprived because mitochondrial dysfunction or insulin resistance prevents conversion to usable ATP. A single resting neuron requires approximately 4.7 billion ATP molecules per second. If mitochondria are inefficient — whether through impaired oxidative phosphorylation, accumulated damage from ROS, or failure of maintenance processes like mitophagy — the brain can have adequate caloric allocation and still be functionally energy-starved. The "paradox of supply vs. use" demonstrates that caloric allocation (Pontzer's constrained model) and conversion efficiency (Palmer's mitochondrial model) are independent variables: you can have plenty of fuel and a broken engine, or a good engine and insufficient fuel, and the functional outcome — cognitive and psychiatric degradation — looks the same from both.

**Relevant to:** Vitality architecture (adds a third component: ceiling × allocation × efficiency), BIO-GEA-OOM-02 neural efficiency (Geary's finding that intelligent individuals consume LESS glucose converges — efficiency is the variable, not supply), individual variation in Vitality (two people with identical allocation can differ in functional output because their mitochondria convert fuel at different rates), existing Metabolic Harshness section (the fuel metaphor — "fuel cut with ethanol" — is the Palmer version of the efficiency problem)

**Retrieval prompt:** "What evidence exists that mitochondrial efficiency varies independently of energy supply? Include the type 2 diabetes paradox (surplus glucose, energy-starved cells), the 4.7 billion ATP/second neuron figure, and any studies showing psychiatric symptoms in metabolically well-supplied but mitochondrially impaired individuals."

---

### **BIO-VAR-MPY-02 `[EMPIRICAL] [MECHANISM]`**

**Claim:** Mitochondrial efficiency is both heritable and trainable. Heritable: mitochondria possess 37 genes in their own DNA, and approximately 1,500 additional genes in the nuclear genome are dedicated to mitochondrial maintenance. Mutations in these genes directly influence behavior, cognition, and stress responses. Epigenetic factors (including micro-RNAs) can be transmitted from parents to children, passing metabolic vulnerabilities across generations. Trainable: exercise is a primary driver of mitochondrial biogenesis (growing new mitochondria) and mitophagy (clearing damaged ones) in both muscle and brain. Ketogenic metabolic therapy upregulates biogenesis and provides ketones as a more efficient fuel source — ketones produce more ATP than glucose for the same amount of oxygen consumed. Light therapy and thyroid hormones can also increase mitochondrial activity and repair. The trainability finding means mitochondrial efficiency is not a fixed ceiling — it responds to environmental input throughout life, unlike the developmental allocation ratios that lock during childhood (Pontzer/Shuar data).

**Relevant to:** Vitality as partly modifiable (ceiling and allocation may be relatively fixed in adulthood; efficiency remains plastic), BIO-VAR-CEM-12 resistance training exception (resistance training expands the metabolic ceiling; exercise also improves mitochondrial efficiency — two different mechanisms by which exercise changes the energy landscape), existing Pharmacological Predictions table (keto as metabolic intervention rather than pharmacological one — different entry point, same target), SALMON benchmarking (Vitality measurement needs to be sensitive to efficiency, not just allocation)

**Retrieval prompt:** "What evidence exists for heritability of mitochondrial function? Include the 37 mtDNA genes, the \~1,500 nuclear genes, and the epigenetic transmission findings. What evidence exists for trainability? Include exercise-driven biogenesis studies (brain-specific, not just muscle), the ketone vs. glucose efficiency comparison, and any RCT data on mitochondrial function improvement."

---

## **HYPOTHALAMUS-MITOCHONDRIA FEEDBACK LOOP**

---

### **BIO-VAR-MPY-03 `[MECHANISM] [EMPIRICAL]`**

**Claim:** The hypothalamus depends on its own mitochondrial health to perform its metabolic allocation role, and when hypothalamic mitochondria are impaired, the allocation system itself degrades. The ventromedial hypothalamus uses mitochondrial fission and ROS levels as the precise signals to regulate systemic glucose. Sleep deprivation specifically targets and impairs mitochondrial function in the hypothalamus (demonstrated in mice). High-fat diet triggers hypothalamic inflammation before it appears anywhere else in the body, and chronic overnutrition triggers interactions between neurons and glial cells that make initially reversible metabolic shifts permanent. Chronic stress diverts energy toward fight-or-flight and away from cellular maintenance; high cortisol inhibits autophagy and mitophagy in the brain, preventing the hypothalamus from repairing its own energy-producing machinery. The result is a vicious cycle: impaired hypothalamic mitochondria → poor glucose regulation and insulin resistance → HPA axis dysregulation and sustained high cortisol → cortisol inhibits mitochondrial repair → further hypothalamic impairment. Behavioral manifestations include overeating, weight gain, anhedonia, anxiety, and "despair-like" behaviors. Mental symptoms are described as the "canary in the coal mine" — the first warning signs of a degrading hypothalamic allocation system.

**Relevant to:** BC-08 Brain's Conflict of Interest (the brain is both the allocator and the organ whose degradation degrades the allocation — this card adds: the degradation operates through the brain's own mitochondria, creating a specific feedback loop), BIO-VAR-CEM-01 hypothalamic enforcement mechanism (this card adds: the enforcement mechanism can itself break down, and the breakdown is self-reinforcing), BIO-VAR-LPR-02 hypothalamic inflammation timeline (convergent: LPR-02 documents inflammation at day 1 of high-fat diet; this card adds the mitochondrial mechanism underneath), existing "Precision-Weighting Trap" BC-EA-06 (convergent: the allocator accommodating its own degradation as the new baseline)

**Retrieval prompt:** "What evidence exists for hypothalamic mitochondrial impairment degrading allocation quality? Include the VMH mitochondrial fission/ROS signaling mechanism, the sleep deprivation mouse study (brain regions affected, timeline), the high-fat diet hypothalamic inflammation precedence finding, and the cortisol-mitophagy inhibition pathway. What behavioral outcomes have been measured when hypothalamic mitochondria are experimentally impaired?"

---

## **DEGRADATION SEQUENCE**

---

### **BIO-VAR-MPY-04 `[MECHANISM]`**

**Claim:** When mitochondria are impaired, their functions degrade in a predictable sequence based on metabolic priority. (1) Maintenance ("housekeeping") degrades first — approximately one-third of a brain cell's energy goes toward maintenance, and under stress the cell puts these functions on hold to prioritize immediate survival. This leads to accumulation of debris (beta-amyloid, tau proteins) and defects in myelin coating. (2) The "off switch" fails next — because it takes energy to apply neural inhibition (ion pumping and calcium regulation), an energy deficit manifests as hyperexcitability before it leads to underactivity. Cells fire when they shouldn't. (3) Energy production collapses — the cell can no longer sustain normal neurotransmission. This sequence predicts a specific psychiatric trajectory: anxiety, mania, seizures, and racing thoughts (hyperexcitability from failed inhibition) appear before depression, fatigue, brain fog, and cognitive impairment (underactivity from energy collapse), which appear before premature brain aging, cell shrinkage, and permanent function loss (maintenance failure accumulated over time).

**Relevant to:** Low-Vitality behavioral signature (the degradation sequence predicts that anxiety/agitation should appear BEFORE depression/withdrawal — the system gets loud before it gets quiet), Goblin Mode (may not be the first sign of budget trouble — irritability and racing thoughts may come first), masking timescale mapping (maintenance failure maps onto chronic allostatic damage; off-switch failure maps onto acute cognitive taxation; energy collapse maps onto identity-level erosion — though the temporal ordering is different from the masking sequence), existing BIO-ABR-CFC-01 C factor (the C factor is what this degradation sequence looks like at the population level)

**Retrieval prompt:** "What evidence exists for the specific ordering of mitochondrial functional degradation? Include the one-third maintenance energy estimate, the hyperexcitability-before-underactivity prediction, the beta-amyloid/tau accumulation mechanism, and any clinical data confirming the anxiety-before-depression temporal sequence."

---

## **CONVERGENCE PATHWAYS**

---

### **BIO-VAR-MPY-05 `[MECHANISM]`**

**Claim:** Palmer's common pathway claim — that all major contributing causes of mental illness converge on mitochondrial dysfunction — has uneven evidence across six pathways. (1) Inflammation: STRONG/EXPERIMENTAL. Interferon directly inhibits three specific mitochondrial genes and suppresses ATP production in brain cells. Chronic inflammation creates a vicious cycle where ROS damage mtDNA, further impairing mitochondria. (2) Hormonal disruption: STRONG/EXPERIMENTAL. Chronic cortisol inhibits autophagy and mitophagy, prevents mitochondrial repair. Brain insulin resistance impairs the PI3K/Akt/mTOR pathway essential for mitochondrial biogenesis. Estrogen decline (menopause) correlates with malformed, donut-shaped mitochondria and declining brain energy metabolism. Animal studies show genetic removal of insulin receptors causes mitochondrial dysfunction and subsequent anxiety/depressive behaviors. (3) Sleep deprivation: STRONG IN ANIMAL MODELS. Melatonin during sleep stimulates mitophagy to clear defective mitochondria. Deprivation prevents this maintenance. Mouse studies show long-term sleep restriction directly damages mitochondria in hypothalamus and frontal cortex. (4) Substance use: DIRECT EXPERIMENTAL. Alcohol processing enzymes are located on or inside mitochondria; excess intake causes swelling, ATP loss, lethal ROS. THC binds CB1 receptors on mitochondrial membranes, acutely slowing function (Nature-published). (5) Gut dysfunction: EMERGING/PARTLY INFERRED. Butyrate (microbially produced) fuels mitochondria and regulates their efficiency — experimentally proven in animals. Leaky gut allows toxins triggering systemic inflammation that damages mitochondria. Human gut-mental-health intervention field described as "in its infancy." (6) Childhood adversity: THEORETICAL/CORRELATIONAL. Trauma induces chronic stress that diverts resources from maintenance. Epigenetic changes (micro-RNA) can be passed intergenerationally, "programming" offspring mitochondria for vulnerability. The ACE-mental-illness correlation is among the strongest in psychiatry, but proving the mitochondrial mechanism in humans relies on theoretical integration rather than direct demonstration.

**Relevant to:** The convergence funnel (if the evidence holds, HPAM has a single mechanistic explanation for why everything that degrades Vitality — inflammation, poor sleep, stress, substances, gut dysfunction, adversity — produces similar behavioral outcomes despite different entry points), existing BIO Immune System section (inflammation pathway is the best-evidenced; converges with existing cytokine-specific behavioral profiles), existing BIO-SUD-GFM-01 and microbiome material (gut pathway is weakest; the existing BIO microbiome cards provide the mechanism detail Palmer lacks), existing BIO-SAP-ZEB series (cortisol pathway converges — Sapolsky provides the behavioral downstream; Palmer provides the mitochondrial mechanism underneath)

**Retrieval prompt:** "For each of the six convergence pathways, what is the strongest single study demonstrating mitochondrial impairment as the mechanism? Include the interferon gene inhibition study, the insulin receptor knockout behavioral study, the mouse sleep deprivation mitochondrial damage study, the THC CB1 receptor study (journal and year), and the butyrate mitochondrial efficiency study. For adversity, what is the strongest theoretical argument rather than direct evidence?"

---

## **INTERFERON AS CAUSAL PROOF**

---

### **BIO-PAL-BRE-01 `[EMPIRICAL] [MECHANISM]`**

**Claim:** Interferon treatment — administered medically for cancer or serious infections — provides a direct, experimentally observed causal link between suppressed mitochondrial function and the immediate onset of psychiatric symptoms. Interferon directly inhibits three specific mitochondrial genes and suppresses ATP production in brain cells. Shortly after treatment begins, patients experience depression, fatigue, irritability, anxiety, insomnia, manic symptoms, psychotic symptoms, hallucinations, suicidal behavior, and delirium. This single drug can produce every symptom known to psychiatry. The argument for a common pathway: if one drug targeting one organelle (mitochondria) produces the full spectrum of psychiatric symptoms, then the organelle is plausibly the convergence point for all contributing causes. Which specific symptom manifests depends on the individual's pre-existing neuronal vulnerabilities — their "weakest link" in the metabolic chain. The interferon data moves the evidence from correlation to causation: healthcare professionals observe psychiatric symptoms appearing as a direct consequence of a drug known to suppress mitochondrial function.

**Relevant to:** Strongest single piece of evidence for the mitochondrial common pathway (one drug → full-spectrum symptoms via one target), existing BIO Immune System section (interferon is an inflammatory cytokine — the Capuron two-factor dissociation already in BIO documents the temporal sequence of interferon effects; this card documents Palmer's use of it as proof-of-concept), the "weakest link" individual variation (why the same metabolic insult produces different symptoms in different people — converges with selective neuronal vulnerability), BC-CEM-07 Palmer confirmation (the interferon data is the strongest empirical support for Palmer's general principle)

**Retrieval prompt:** "What specific studies does Palmer cite for the interferon-psychiatric symptom link? Include which cancers/infections interferon is used for, the timeline from drug administration to symptom onset, the specific mitochondrial genes inhibited, and whether the symptoms resolve when interferon is discontinued."

---

## **ADAPTIVE VS. DISORDER THRESHOLD**

---

### **BIO-PAL-BRE-02 `[MECHANISM] [FRAMING MOVE]`**

**Claim:** Palmer distinguishes adaptive mental states from true metabolic disorders using three criteria: context-appropriateness (are the symptoms provoked by circumstances that would challenge anyone?), duration relative to the provoking context (do they persist after the situation resolves?), and the state of cellular maintenance (has the metabolic diversion lasted long enough to produce accumulated damage?). In an adaptive stress response, mitochondria mobilize resources effectively — the brain's "headlights and wipers" turn on in a storm. In a disorder, mitochondrial impairment prevents neurons from turning both on and off appropriately, regardless of the external environment — the car's systems malfunction in good weather. The gray zone between adaptive stress and disorder is explained through accumulated maintenance failure: a normal stress response diverts resources from housekeeping (autophagy, mitophagy). If this diversion is prolonged, cells develop maintenance problems — damaged parts accumulate, toxic proteins build up — and the adaptive response fails, turning a temporary state into a persistent metabolic disorder. Supporting sources add complexity: a specific threshold of mitochondrial complex dysfunction may need to be reached before homeostasis fails entirely; a "BIR-positive" subtype (Brain Insulin Resistance) of depression/anxiety may be mechanistically distinct from non-metabolic versions; and chronic overnutrition can trigger neuron-glial interactions that make initially reversible processes permanent.

**Relevant to:** HPAM's Goblin Mode vs. disorder distinction (Palmer's criteria map: Goblin Mode \= adaptive diversion, context-appropriate, recoverable with rest; disorder \= maintenance failure, context-inappropriate, self-sustaining), the three masking timescales (acute taxation \= adaptive diversion still recoverable; chronic damage \= maintenance failure accumulating; identity erosion \= the maintenance machinery itself has degraded, making the original state irrecoverable), BIR subtype (relevant to SALMON: some people presenting with depression may have a metabolically distinct condition requiring different intervention), existing BC-EA-03 "The Referee Goes Deaf Before the Subsystem Expands" (convergent: maintenance failure begins before the disorder is clinically visible)

**Retrieval prompt:** "What specific metabolic criteria does Palmer use to distinguish adaptive stress from disorder? Include the 'three cars' analogy criteria, the maintenance failure mechanism (autophagy diversion timeline), and the BIR subtype finding. What does Palmer say about whether a disorder caused by prolonged adaptive diversion is reversible or permanent?"

---

## **DIRECTIONALITY**

---

### **BIO-VAR-MPY-06 `[EMPIRICAL]`**

**Claim:** The strongest evidence that metabolic dysfunction precedes psychiatric symptom onset comes from four lines: (1) Medication-naïve first episodes: patients diagnosed with first-episode schizophrenia — before any medication that might cause weight gain or time for lifestyle degradation — already show disrupted insulin and glucose metabolism in the brain. (2) Longitudinal childhood data: a study following 15,000 children found that persistently high insulin levels at age 9 predicted a fivefold increased risk for a "psychosis at-risk mental state" and a threefold increased risk for bipolar or schizophrenia diagnosis by age 24\. (3) Interferon induction: psychiatric symptoms appear directly following administration of a known mitochondrial inhibitor (see BIO-PAL-BRE-01). (4) Cancer depressive prodromes: some patients experience clinical depression months before a pancreatic cancer diagnosis, suggesting systemic metabolic changes drive brain dysfunction before the patient is aware of the illness. Intervention evidence: restoring a specific mitochondrial protein (MFN2) in the brain immediately stops anxiety and depression-like behaviors in animal models. The ketogenic diet, which provides alternative fuel bypassing glucose metabolism blocks, produced metabolic syndrome remission in 100% of participants in a Stanford pilot of bipolar/schizophrenia patients, correlated with significant psychiatric improvement. However, the sources explicitly acknowledge bidirectional causation as the more accurate picture — depression causes sedentary behavior and poor sleep, which damage mitochondria, which worsen depression. The most effective clinical intervention point is argued to be the metabolic system, as restoring brain energy allows psychological and social systems to stabilize.

**Relevant to:** The causal argument for Palmer's framework (strongest for inflammation/interferon, moderate for insulin/first-episode, suggestive for childhood longitudinal), the bidirectionality acknowledgment (HPAM should present the vicious cycle, not one-directional causation), the childhood insulin finding (convergent with BIO-ELL-ACM developmental calibration — metabolic dysfunction during the calibration window predicts psychiatric outcomes decades later), existing BC-CEM-03 forecasting system (the hypothalamus as prediction system — early metabolic dysfunction may set the prediction model's parameters toward pathology)

**Retrieval prompt:** "What specific studies establish that metabolic dysfunction precedes psychiatric onset? Include the medication-naïve first-episode data (sample size, specific metabolic measures), the 15,000-child longitudinal study (insulin measure, follow-up duration, risk ratios), the MFN2 animal experiment, and the Stanford keto pilot (sample size, outcomes, follow-up). What does Palmer say about how to adjudicate between metabolic-first and symptom-first explanations?"

---

## **SELECTIVE NEURONAL VULNERABILITY**

---

### **BIO-VAR-MPY-07 `[MECHANISM]`**

**Claim:** Mitochondrial impairment does not affect all brain regions equally. The brain as a whole is uniquely susceptible to oxidative stress — consuming 20% of the body's energy while being lipid-rich (a primary target for oxidative damage), having low antioxidant defenses, and storing almost no energy reserves. Within this already-vulnerable organ, specific neurons are selectively targeted based on their size, location, neurotransmitter type, and metabolic demand. Larger neurons with higher energy demands are more prone to oxidative damage. Dopaminergic neurons are particularly susceptible because dopamine has a natural tendency toward auto-oxidation, creating high oxidative load within those cells. Different brain regions have varying sensitivity thresholds — a specific threshold of mitochondrial dysfunction must be reached before a cell loses homeostasis. Neurons living closer to this threshold are more likely to "crash" under additional stress. The "weakest link" principle: an individual's biological blueprint and past environmental exposures determine which neural networks fail first when energy supply is compromised, producing the specific symptom profile rather than uniform degradation.

**Relevant to:** Why the same metabolic insult produces different psychiatric presentations in different people (the "weakest link" is individually determined by genetics and developmental history), BIO-ABR-CFC-01 C factor (the C factor documents that cognitive dysfunction is universal across disorders; selective vulnerability explains why the specific PATTERN of dysfunction differs), dopaminergic vulnerability (converges with existing BIO-SAP-ZEB-01 and ZEB-03 — dopamine neurons are metabolically fragile, which is why Enthusiasm and Industriousness are the Go stats most vulnerable to chronic stress), existing BIO-VAR-CEM-02 triage hierarchy (under constrained TEE, the brain is protected as a whole, but WITHIN the brain, vulnerability is selective — not all neurons are equally protected)

**Retrieval prompt:** "What evidence exists for selective neuronal vulnerability to mitochondrial impairment? Include the brain's general susceptibility factors (lipid content, low antioxidants, no storage), the large-neuron vulnerability finding, the dopamine auto-oxidation mechanism, and any studies identifying which brain regions or cell types fail first under energy constraint."

---

## **LIMITATIONS AND BOUNDARIES**

---

### **BIO-VAR-MPY-08 `[COUNTERPOINT]`**

**Claim:** The metabolic psychiatry model has several identified weaknesses. (1) The bidirectionality problem remains the weakest link: causes lead to consequences that become causes, and proving metabolic precedence requires ruling out reverse causation in complex feedback loops. (2) Much evidence relies on peripheral biomarkers (blood, urine) as imperfect proxies for the metabolic state of specific microscopic neural circuits — an acknowledged uncertainty. (3) Even individuals with the same rare genetic mitochondrial mutation manifest widely different symptoms, suggesting energy production alone cannot account for the diversity of psychiatric presentations. (4) Antidepressant data is contradictory: some studies show antidepressants improve mitochondrial function, others show no effect, and some show they potentiate dysfunction depending on dosage and cell type. (5) A "mitochondrial cocktail" of 20+ vitamins and nutrients (CoQ10, NAC, B-vitamins) showed no difference from placebo in 180 bipolar patients — a direct metabolic intervention that failed. (6) Anti-inflammatory interventions (omega-3s, vitamin E, ibuprofen) for depression and schizophrenia have been "disappointing at best." (7) A 2017 meta-analysis of 2,500 participants found no antidepressant effects of exercise and no significant effect on quality of life — a counterexample to the theory that increasing metabolic activity always improves symptoms. (8) Palmer acknowledges that in acute drug-induced states, mitochondria may be "dysregulated" rather than "dysfunctional," and concedes it is "unfair" to call them dysfunctional when they are simply responding to a hostile chemical environment. (9) Keto intervention evidence has selection bias (uniquely motivated participants) not yet resolved by RCTs.

**Relevant to:** Honest framing for HPAM (the model has real critics and real failures — the book should use Palmer for the general principle while acknowledging these boundaries), the mitochondrial cocktail failure (direct metabolic supplementation doesn't work — the system needs reorganization, not ingredients), the exercise paradox (exercise helps mental health in some studies and not others — may depend on whether the individual's depression is metabolically driven or not, converging with the BIR subtype finding), existing BIO-ZIE-BSM-01 rhetorical parallel (same structure: the critique challenges the mechanism while the phenotypic finding survives — Palmer's general principle holds even where his specific mechanism claims are contested)

**Retrieval prompt:** "What specific counterexamples and limitations do Palmer and the other sources acknowledge? Include the mitochondrial cocktail study (sample size, intervention, result), the exercise meta-analysis (author, sample size, finding), the contradictory antidepressant data (which studies show positive vs. negative effects), and the peripheral biomarker limitation. Does Palmer address why direct mitochondrial supplementation fails while dietary intervention (keto) succeeds?"

---

## **CONVERGENT CITATION NOTES (for existing cards and Book Content)**

---

### **Note for existing Metabolic Harshness section (Palmer bullets)**

**Upgrade to formal card reference:** BIO-PAL-BRE-01 and BIO-PAL-BRE-02 now formalize Palmer's contribution with specific mechanism claims, evidence, and boundary conditions. The existing bullets ("Mental disorders are metabolic disorders of the brain / Mitochondrial dysfunction reduces available brain energy") can remain as summary but should reference the cards for specificity. The existing fuel metaphor ("fuel cut with ethanol in an engine not designed for it") is Palmer's efficiency argument in narrative form — now supported by the 4.7 billion ATP/second figure and the type 2 diabetes paradox.

---

### **Note for existing "Palmer's Brain Energy Contribution, Precisely Bounded" BC**

**Update with mitochondrial specificity:** The existing BC says "Palmer has the Vitality right. He has nothing else." BC-CEM-07 (Pontzer extraction) upgraded this to "confirmed, not qualified." The current Palmer extraction adds: Palmer's mitochondrial mechanism provides a THIRD variable for Vitality (efficiency alongside ceiling and allocation), the hypothalamus-mitochondria feedback loop explains how chronic stress permanently degrades the allocator, and the degradation sequence predicts a specific psychiatric trajectory. The "nothing else" assessment should be revised to: "Palmer has Vitality right, including the mitochondrial efficiency layer. His common-pathway claim is strong for inflammation and hormonal disruption, moderate for sleep and substances, weak for gut and adversity. His specific treatment claims (keto) are proof-of-concept, not established. The immune-specific routing that HPAM documents (cytokine-specific behavioral profiles) remains beyond Palmer's framework."

---

### **Note for BIO-VAR-CEM-01 (hypothalamic enforcement mechanism)**

**Add mitochondrial substrate:** The existing card documents how the hypothalamus enforces the energy constraint (leptin, glucose, gut signals → triage hierarchy). BIO-VAR-MPY-03 adds: the enforcement mechanism itself depends on hypothalamic mitochondrial health. The VMH uses mitochondrial fission and ROS as the actual regulatory signals. When these mitochondria are impaired, the enforcement degrades — the manager's own office is burning down.

---

### **Note for BC-08 (Brain's Conflict of Interest)**

**Add mitochondrial feedback loop:** BC-08 says the brain is both referee and biggest spender. The constrained TEE notes (already flagged in Pontzer extraction) sharpen this to zero-sum. The Palmer extraction adds the feedback loop mechanism: the referee's judgment quality depends on its own mitochondrial health, which is degraded by the same stressors (cortisol, inflammation, poor sleep) that the referee is supposed to manage. The conflict of interest isn't just structural — it's metabolically self-reinforcing.

---

### **Note for existing BIO Immune System section (Capuron two-factor dissociation)**

**Add interferon mitochondrial mechanism:** The existing Immune System BC documents that interferon produces a two-factor dissociation (fatigue/neurovegetative at weeks 1-2 via dopamine, mood/cognitive at weeks 8-12 via serotonin). BIO-PAL-BRE-01 adds Palmer's use of the same finding as proof-of-concept for the mitochondrial common pathway — one drug targeting mitochondria → full-spectrum psychiatric symptoms. The two framings are complementary: the Immune System BC documents the specificity (different timelines, different transmitters); Palmer documents the generality (all symptoms trace back to one organelle).

---

### **Note for BIO-GEA-OOM-02 (Neural efficiency)**

**Add mitochondrial mechanism:** Geary documents that intelligent individuals consume LESS glucose during complex tasks. The Palmer extraction provides the mechanism underneath: mitochondrial efficiency determines how much ATP you get per unit of allocated fuel. Geary's neural efficiency may be partly (or largely) mitochondrial efficiency — the brain that wastes less glucose may be the brain with healthier, more efficient mitochondria, not just better inhibitory control. This doesn't replace Geary's inhibitory-control explanation but adds a subcellular layer.

---

### **Note for BIO-VAR-CEM-05 (Individual variation in ceiling)**

**Add efficiency as third variable:** The Pontzer card documents two sources of Vitality variation: ceiling differences and allocation differences. BIO-VAR-MPY-01 adds a third: mitochondrial efficiency differences. At the same body size, with the same allocation ratio, two people can differ in functional brain energy because their mitochondria convert fuel at different rates. SALMON's eventual Vitality measure would need sensitivity to all three.

---

### **Note for existing three masking timescales BC**

**Add degradation sequence mapping:** BIO-VAR-MPY-04's degradation sequence (maintenance → off-switch → energy) provides a mitochondrial-level mapping that partially converges with and partially complicates the masking timescales. Convergence: the temporal ordering (fast adjustments → medium adjustments → slow/permanent adjustments) is the same in both frameworks. Complication: the mitochondrial sequence predicts hyperexcitability (anxiety, agitation) as the FIRST sign of degradation, while the masking framework predicts cognitive taxation (depletion) as the first sign. These may not conflict — hyperexcitability IS a form of cognitive taxation (the system is running loud and inefficiently). But the book should address why low-Vitality states can present as either agitated or depleted, depending on where in the degradation sequence the person is.

# **Constrained Energy Model (Pontzer et al.)**

**Date:** 2026-03-10 **Source manifest:**

* \[NotebookLM responses, pasted in conversation\] 7 round-1 prompts \+ 8 round-2 prompts from a notebook containing: Pontzer *Burn* (2021), Pontzer (2016) "Constrained Total Energy Expenditure," Pontzer (2012) "Hunter-gatherer energetics," Hall (2021) "Energy compensation: Biggest Loser reinterpreted," Dolan (2023) "Energy constraint: endurance athletes," Gonzalez (2023) "Perspective: additive or constrained?", Galanes (2025) "Rethinking Endurance Training."  
* \[google\_drive\_fetch: full doc\] BIO research doc loaded, duplicate-checked.

**Duplicate check results:** Zero existing Pontzer cards or constrained energy model content. Existing material this connects to: BC-04 (Priority Matrix), BC-05 (κ-rule/DEB), BC-08 (Brain's Conflict of Interest), BC-10 (T-Shirt Sizing — explicitly deferred to a future notebook; this IS that notebook), BIO-VAR-MCA-08 (sleep as reallocation), BIO-NOR-TBB-05 (exercise mental health data), BIO-GEA-OOM-02 (neural efficiency), Metabolic Harshness section (Palmer/Hall/Belluz). Convergent citation notes for each below.

**Author codes and book abbreviations:**

* PON \= Pontzer; BRN \= *Burn*; CTE \= Constrained Total Energy (2016 paper); HGE \= Hunter-Gatherer Energetics (2012 paper)  
* HAK \= Hall, Kevin; ECM \= Energy Compensation Metabolic (2021 reinterpretation paper)  
* DOL \= Dolan; ECE \= Energy Constraint Endurance (2023)  
* GON \= Gonzalez; PCA \= Perspective Constrained Additive (2023)  
* VAR-CEM \= various authors, Constrained Energy Model (multi-source claims)

**Placement:** BIO doc, new section after existing Metabolic Allocation material. Title: "Constrained Energy Expenditure: The Evolutionary Logic of Vitality."

---

# **BIO \- CARDS**

---

## **CORE MODEL**

---

### **BIO-PON-CTE-01 `[EMPIRICAL] [MECHANISM]`**

**Claim:** In an analysis of 332 adults across five diverse populations (ranging from subsistence farmers to sedentary urbanites), total daily energy expenditure (TEE) does not scale linearly with physical activity. Instead, TEE plateaus at higher activity levels. Individuals in the most active populations do not burn significantly more total calories per day than those in moderately active populations after adjusting for body size and composition. The body maintains TEE within a relatively narrow range by compensating for increased physical activity through reductions in energy allocated to other physiological processes. This "constrained" model of energy expenditure contrasts with the "additive" model (where every calorie of activity adds directly to TEE) and implies that the body operates on an energy budget with a ceiling rather than an open-ended demand-response system.

**Relevant to:** Vitality as budget share (the ceiling constrains total available energy; personality-relevant computation is one budget line item), all existing metabolic allocation material (provides the evolutionary logic for WHY the budget is fixed), BC-04 Priority Matrix (triage operates under this ceiling), BC-05 κ-rule (DEB's preset allocation ratios divide THIS constrained total)

**Retrieval prompt:** "What does Pontzer (2016) report about the relationship between physical activity level and total daily energy expenditure across five populations? Include the sample size, the populations studied, the statistical model used to distinguish additive from constrained, and whether the plateau is absolute or gradual."

---

### **BIO-PON-HGE-01 `[EMPIRICAL]`**

**Claim:** Hadza hunter-gatherers in Tanzania, who walk miles daily foraging and perform sustained physical labor, have total daily energy expenditure statistically indistinguishable from sedentary Westerners after controlling for body size and composition. This finding holds despite Hadza physical activity levels being roughly ten times higher than Western norms. The Hadza are weight-stable throughout their lives — they are not in energy deficit. The implication is that the Hadza body reallocates energy from other physiological systems (immune activity, reproductive hormones, stress reactivity) to fund high physical activity, maintaining the same total energy ceiling as people who barely move.

**Relevant to:** The strongest single finding for the constrained model (weight-stable population with massive activity difference and identical TEE — rules out deficit-driven compensation as the sole explanation), existing BIO Metabolic Harshness section (the Hadza data is the evolutionary counterpoint to the UPF/sedentary Western environment), person-environment fit (same total budget, radically different allocation \= different phenotype from same species)

**Retrieval prompt:** "What does Pontzer (2012) report about Hadza vs. Western TEE? Include the body-size adjustment method, the specific physical activity measures (walking distance, foraging hours), and the statistical comparison of adjusted TEE. Are the Hadza weight-stable, and what is the evidence for that?"

---

### **BIO-VAR-CEM-01 `[MECHANISM]`**

**Claim:** The body enforces the energy constraint through the hypothalamus, which integrates blood-borne signals (leptin from fat cells, glucose levels) and neural signals from taste buds, stomach, and small intestine. When expenditure pressure increases, the hypothalamus initiates a hierarchy of functional preservation: suppressing "luxury" systems (reproduction, chronic inflammation, stress reactivity, non-exercise activity) to protect immediate survival functions. Enforcement operates through combined hormonal and neural channels — thyroid hormone regulation controls metabolic intensity, reproductive hormone suppression saves calories, and the brain manufactures the sensation of fatigue to shut down activity before physiological damage occurs. The hypothalamus is not just a sensor but an active allocator that picks "winners and losers" within the constrained budget.

**Relevant to:** BC-08 Brain's Conflict of Interest (the hypothalamus is the budget manager AND part of the brain that benefits from the budget — sharpens the existing claim), BIO-VAR-MCA-01 (extends: the EAS three-axis model describes the governance network; this card describes the constraint the network operates under), BIO-PET-SBR-01 (convergent: the selfish brain's brain-pull mechanism operates within the constrained total, not in addition to it)

**Retrieval prompt:** "What specific detection and enforcement mechanisms does the literature describe for how the hypothalamus maintains the energy constraint? Include the input signals (leptin, glucose, gut hormones), the output pathways (thyroid, reproductive, neural fatigue), and any evidence for the sequence in which systems are suppressed."

---

## **TRIAGE AND FAILURE**

---

### **BIO-VAR-CEM-02 `[MECHANISM]`**

**Claim:** When sustained physical activity demands a larger share of the energy budget, the body suppresses systems in a consistent hierarchy: (1) Reproductive function is cut first — testosterone, estrogen, and progesterone decrease; at extreme workloads, women stop ovulating and men show crashed sperm count and libido. (2) Immune activity is reduced — chronic inflammation is suppressed (healthy in moderation, pathological when pushed further, resulting in increased illness frequency and delayed healing). (3) Stress reactivity is muted — adrenaline and cortisol responses are dampened. (4) Non-exercise activity (NEAT) may be unconsciously reduced — less fidgeting, less standing. The brain is rigorously protected throughout — starvation victims lose spleen and liver mass while the brain maintains its mass. The brain is described as a "high-maintenance prima donna" that consumes approximately 300 kcal/day (20% of adult BMR) despite weighing under three pounds.

**Relevant to:** Masking cost specificity (the triage hierarchy answers "what gets defunded when you mask?" — reproduction and immune surveillance are the first budget lines to lose share), BC-04 Priority Matrix (converges and extends: BC-04 says different crises rotate the triage order; this card says within the activity-demand crisis, the order is reproduction → immune → stress → NEAT, with brain protected), existing BIO Immune System section (immune suppression under high activity is the same mechanism as immune override of brain priority in reverse — when activity demands dominate, immune gets cut; when immune demands dominate, activity gets cut)

**Retrieval prompt:** "What specific evidence exists for the triage ordering? Include the reproductive suppression data (which hormones, at what activity level), the immune suppression findings (infection rates in athletes), the stress reactivity muting, and the brain mass preservation data from starvation victims. Does the ordering vary between individuals?"

---

### **BIO-VAR-CEM-03 `[EMPIRICAL] [MECHANISM]`**

**Claim:** The triage hierarchy is not universal but is shaped by evolutionary life history strategy. Short-lived species like mice prioritize reproduction above all else — during starvation, they maintain testicles even while the spleen (immune function) atrophies. Long-lived species like humans prioritize somatic maintenance and survival, suppressing reproduction during lean times. In children, the "broken" system during energy pressure is often physical growth — if brain or immune demands increase, the body slows growth to protect those higher-priority investments. The Shuar (indigenous Ecuadorian population) provide the clearest human evidence: children facing high pathogen loads show BMRs approximately 20% higher than industrialized peers due to immune activity, and the energy is taken from growth, resulting in shorter adult stature. These trade-offs become permanent features of adult physiology regardless of later environmental changes.

**Relevant to:** BIO-ELL-ACM-01 through 03 (convergent: ACM developmental switch points describe WHEN calibration happens; the Shuar data shows the metabolic MECHANISM — the allocation ratio that gets set during the window), existing heritability trajectory section (the Shuar finding is the metabolic version of developmental canalization via epigenetic programming — BIO-VAR-MCA-06), BIO-ELL-DSE-01 (orchid/dandelion sensitivity — the Shuar children's allocation response is what high biological sensitivity to context looks like metabolically)

**Retrieval prompt:** "What specific evidence exists for species differences in triage ordering? Include the mouse testicle/spleen finding, the human growth-suppression data, and the Shuar BMR and stature data. How permanent are the Shuar allocation ratios — what evidence exists that they persist after environmental change?"

---

### **BIO-VAR-CEM-04 `[EMPIRICAL]`**

**Claim:** The alimentary limit — the maximum rate at which the human gut can absorb calories — sets the absolute ceiling for sustainable energy expenditure at approximately 2.5 times basal metabolic rate. For a typical adult, this translates to roughly 4,000-5,000 kcal/day. When expenditure exceeds this limit (Tour de France cyclists reaching 3.5-4.5× BMR, Arctic trekkers, Race Across USA runners), the body enters negative energy balance and begins consuming its own fat and muscle tissue because it literally cannot eat fast enough to keep up. This limit has been observed across diverse scenarios including extreme endurance events and pregnancy — third-trimester mothers reach the same metabolic boundary as ultra-endurance athletes, leading researchers to describe pregnancy as "the ultimate ultramarathon." The alimentary limit is the hard floor that explains why the constrained model's ceiling exists: no species can persist long-term spending more energy than its gut can replace.

**Relevant to:** BC-10 T-Shirt Sizing (explicitly flags "the one number that surfaced: immune activation can consume 25-55% of BMR" and defers magnitudes to a future notebook — THIS is that data), the Expensive Animal (the alimentary limit puts a hard number on the maximum metabolic budget any human can sustain), pregnancy as metabolic extreme (useful for the book — connects to the life history material)

**Retrieval prompt:** "What is the evidence for the 2.5× BMR alimentary limit? Include the Tour de France data, the Arctic trekking data, the Race Across USA data, and the pregnancy finding. Is the 2.5× figure a hard ceiling or a range, and does it vary between individuals?"

---

## **INDIVIDUAL VARIATION**

---

### **BIO-VAR-CEM-05 `[EMPIRICAL]`**

**Claim:** At the same body size and composition, individuals vary in total daily energy expenditure by 300 kcal/day typically and up to 500 kcal/day at extremes. The variation has two sources: (1) Ceiling differences — the total budget size is set by genetics, body size, and organ mass. Fat-free mass is the single strongest determinant of metabolic rate because lean tissues are far more metabolically active than fat. Individual variation in the relative sizes of expensive organs (liver and brain each consume \~20% of BMR despite small mass) creates "fast" or "slow" metabolisms. Over 900 gene variants associated with obesity are primarily active in the brain, influencing hypothalamic management of the budget. (2) Allocation differences — once the total is set, the body dynamically reallocates across systems based on demand. People in high-pathogen environments (Tsimane, Shuar) show BMRs 200-350 kcal/day higher than industrialized populations because their immune systems are chronically active, claiming a larger share of the fixed budget.

**Relevant to:** Vitality has two components (ceiling size AND allocation ratio — this matters for SALMON because measuring Vitality means measuring both), BIO-GEA-OOM-02 neural efficiency (individual variation in efficiency \= variation in mileage per unit of fixed budget), BIO-HAL-FOO-02 (900+ gene variants acting in brain — convergent: same finding, food context vs. energy context)

**Retrieval prompt:** "What evidence distinguishes individual variation in total budget size from variation in budget allocation? Include the 300-500 kcal range, the organ-mass contribution to BMR variation, the 900 gene variants finding, and the Tsimane/Shuar immune burden data."

---

## **LIFESPAN AND DEVELOPMENT**

---

### **BIO-VAR-CEM-06 `[EMPIRICAL] [MECHANISM]`**

**Claim:** The metabolic ceiling changes across the lifespan in both absolute terms and metabolic intensity. Size-adjusted ceiling peaks in early childhood at approximately 35 kcal per pound per day, declines through adolescence, and flattens in the early twenties at approximately 15 kcal per pound per day. A further decline occurs in aging, partly driven by body composition changes (metabolically active muscle replaced by quieter fat tissue). Allocation priorities shift fundamentally at each stage: in children aged 3-7, the brain consumes over 60% of BMR, and this demand is so high it physically slows growth in the rest of the body. At puberty, the hypothalamus shifts priorities from growth to reproduction, including body composition changes and hormonal investment. In aging, the budget focuses on somatic maintenance with declining efficiency. The childhood-to-adulthood ceiling drop represents the engine running progressively cooler — not less total energy for the bigger organism, but less energy per unit of tissue.

**Relevant to:** Developmental calibration architecture (converges with all existing ACM, heritability trajectory, sensitive period material — adds the metabolic ceiling trajectory underneath), BIO-BLM-SCP-01 (social brain maturation timelines — the 60% brain BMR in early childhood is the metabolic cost of the neural development Blakemore documents structurally), the V-acquisition period (the pubertal budget shift is the metabolic underpinning of the pubertal recalibration window)

**Retrieval prompt:** "What data exist for size-adjusted metabolic intensity across the lifespan? Include the 35 kcal/lb childhood figure, the 15 kcal/lb adult figure, the 60% BMR brain consumption in ages 3-7, and any evidence about whether the aging decline is reversible or inevitable."

---

### **BIO-VAR-CEM-07 `[EMPIRICAL] [MECHANISM]`**

**Claim:** Childhood and adolescence serve as critical developmental windows where metabolic allocation ratios are calibrated based on environmental cues. It is hypothesized that the ratio of food availability to physical activity during development provides the signal that determines an individual's TEE set point for adulthood. In the Shuar, children aged 5-12 show \~20% higher BMR than industrialized peers due to chronic immune demand, and this high immune allocation steals energy from growth. These trade-offs — prioritizing immune function over height — become permanent features of adult physiology regardless of later environmental changes. The mechanism is described as the hypothalamus integrating environmental signals to set metabolic targets, with every individual inheriting the same basic biological variables (leptin, ghrelin, etc.) but early-life experiences determining the precise thresholds at which these signals trigger responses. The calibration is characterized as one-way: once allocation ratios are established in childhood, they persist even if the individual later moves to a pathogen-free environment.

**Relevant to:** BIO-ELL-ACM-01 (direct convergence: ACM's developmental switch points \= the windows during which these metabolic ratios are configured), BIO-VAR-MCA-06 (convergent: thrifty phenotype and glucocorticoid receptor methylation as molecular mechanisms for permanent allocation locking), BIO-SUD-GFM-01 (microbial sensitive period for HPA calibration — another system where early window closure permanently sets allocation), existing heritability trajectory section (genetic stability reaches unity by \~30, but the metabolic allocation ratios may lock earlier)

**Retrieval prompt:** "What evidence exists for the permanence of developmental metabolic calibration? Include the Shuar data (BMR comparison, growth impact, adult stature), the hypothesis about food:activity ratio as calibration signal, and any evidence about whether allocation ratios have EVER been observed to change in adulthood after early calibration."

---

## **HERITABILITY**

---

### **BIO-VAR-CEM-08 `[EMPIRICAL] [MECHANISM]`**

**Claim:** Metabolic heritability encompasses both the total budget size and the hypothalamic management logic that allocates it. The total budget (ceiling) is largely set by genetics, body size, and organ mass. The management logic (allocation algorithms) is shaped by over 900 gene variants primarily active in the brain, which build the "algorithms" determining when to prioritize movement, when to trigger hunger, and when to suppress luxury systems. Genetic inheritance and developmental calibration interact: genetics sets the framework and potential ranges, while early-life environment tunes the inherited algorithms — determining the precise thresholds at which leptin, ghrelin, and other signals trigger responses. A "genetic set point" adaptive for a hunter-gatherer environment can produce dysregulation in a modern environment when the reward system's sensitivity to fat and sugar, previously advantageous, becomes an "obesity trap" amid engineered hyperpalatable foods.

**Relevant to:** Go stat baselines (you inherit both a metabolic ceiling and a rulebook for dividing it — Go stats operate on whatever allocation the combination produces), existing heritability trajectory section (adds metabolic heritability as a third dimension alongside behavioral genetics and temperament), BIO-HAL-FOO-02 (convergent: the 900+ gene variants acting in brain are the same finding in the food/obesity context — should be cross-referenced, not duplicated)

**Retrieval prompt:** "What evidence distinguishes heritable ceiling from heritable allocation logic? Include the 900 gene variants finding, the specific hypothalamic algorithms described, and any twin or family study data on metabolic rate heritability. What is the evidence for gene-environment mismatch in modern food environments?"

---

## **SLEEP**

---

### **BIO-VAR-CEM-09 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Under the constrained energy model, sleep functions as both a scheduled maintenance window and an active compensation mechanism. Sleeping metabolic rate (SMR) often decreases to offset increased daytime physical activity — in some exercise intervention studies, the compensation in SMR was significantly greater than compensation in basal metabolic rate. The body maintains the constrained total by "squashing" peaks of resting expenditure throughout the day and night to fund movement costs. Migratory birds and extreme endurance athletes do not show the massive increases in total annual expenditure their activity would predict, partly because of this nighttime compensation — running the "engine" cooler during sleep. When sleep is restricted or misaligned with the internal clock, total daily energy expenditure can actually decrease (not increase), suggesting that without the structured reset period, the body's ability to maintain metabolic throughput is impaired. Sleep restriction leads to a "fit but fragile" state where short-term performance is maintained but illness risk, hormonal stagnation, and overtraining vulnerability increase because the restoration budget was cut.

**Relevant to:** BIO-VAR-MCA-08 (extends: existing card describes sleep as diurnal reallocation; this adds the SMR compensation mechanism, the circadian squashing, and the sleep-restriction TEE-decrease finding), masking costs (sleep restriction cuts the restoration budget — the same budget that repairs whatever damage masking accumulated during the day), Vitality replenishment (sleep is not just "rest" but the window where the allocation is actively reset — skip it and the next day starts with a degraded budget)

**Retrieval prompt:** "What specific evidence exists for SMR compensation during exercise interventions? Include the comparison of SMR vs. BMR compensation magnitude, the circadian squashing mechanism, and the sleep-restriction TEE-decrease finding. Is SMR compensation proportional to activity increase, or does it plateau?"

---

## **COMPENSATION TIME COURSE**

---

### **BIO-VAR-CEM-10 `[EMPIRICAL] [MECHANISM]`**

**Claim:** Metabolic compensation is not immediate — there is a lag period followed by system-specific reallocation on different schedules. In the Race Across the USA (140-day, 3,000-mile run), runners averaged 6,200 kcal/day in week 1 — exactly what additive prediction would expect. By the end, TEE had dropped 20% despite constant workload, with BMR unchanged, suggesting savings came from other activity-related or circadian components. Full acclimation to a new exercise regimen takes 3-5 months for TEE to pull back toward the constrained target. System-specific timelines: thyroid hormone production can decrease within days under severe energy pressure. BMR and SMR compensation becomes significant only after approximately 15 weeks of sustained activity. Reproductive hormone suppression takes months to years — in male endurance runners, testosterone levels continue dropping over the first two years of training, reaching a suppressed stable point only after five years. In animal models, spleen (immune function) is sacrificed immediately during energy restriction, while reproductive organs are protected longer.

**Relevant to:** Three masking timescales (the compensation time course provides metabolic analogs: acute taxation ≈ thyroid-speed adjustment in days; chronic allostatic damage ≈ BMR/immune adjustment over weeks to months; identity-level erosion ≈ reproductive/permanent calibration over years), the early "fit but fragile" phase (before compensation engages, the organism is in high-throughput mode with no budget cuts — performance is high but risk is elevated), BIO-ELL-ACM-03 (asymmetric profile shifts — downregulation takes time, and different physiological channels respond on different schedules)

**Retrieval prompt:** "What specific data exist for the Race Across USA compensation timeline? Include week 1 TEE, final TEE, the 20% reduction figure, which components of expenditure did and did not change, and the 3-5 month acclimation estimate. What is the evidence for the 15-week BMR threshold and the 5-year testosterone stabilization? Include sample sizes and study designs."

---

## **FATIGUE**

---

### **BIO-VAR-CEM-11 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Mental fatigue is not a result of substrate depletion — it is a regulatory signal manufactured by the brain to protect the organism from overuse and manage the constrained energy budget. Studies of elite athletes show that even at the point of felt exhaustion and collapse, they still have fuel on board — circulating glucose, fatty acids, and ATP in muscles all present. The brain integrates metabolic by-products, body temperature, perceived difficulty, and the expected remaining workload, then generates the sensation of exhaustion to shut the body down neurally before actual physiological damage or fuel depletion occurs. This sensation is manufactured deep in the brain beneath conscious awareness and can be triggered by mental strain even when physical reserves are full. Although the caloric cost of thinking is negligible (\~4 kcal/hour increase), mental fatigue directly reduces physical endurance and performance. The brain can be rigorously protected calorically (maintaining mass and baseline metabolic rate even during starvation) while still being functionally degraded by its own regulatory signals — suppressing behavioral drives for sex, social interaction, and mental persistence to focus on maintenance and immediate survival.

**Relevant to:** Acute masking timescale (reframes: the "cognitive taxation" of masking isn't substrate running out — it's the hypothalamus pulling the plug on non-essential expression as a regulatory decision), Goblin Mode mechanism (the brain isn't depleted, it's reallocating — the person who can't socialize after work hasn't run out of social fuel; their manager decided socializing isn't getting funded right now), BC-08 Brain's Conflict of Interest (the brain manufactures the sensation that stops activity to protect itself — it's the referee calling the game to preserve its own operations)

**Retrieval prompt:** "What specific studies demonstrate that fatigue occurs with fuel still available? Include the elite athlete collapse data, the specific substrates still present at exhaustion, and the evidence that the brain manufactures fatigue as a regulatory signal rather than detecting fuel depletion. What is the 4 kcal/hour finding from, and how does mental fatigue reduce physical performance if the cost isn't caloric?"

---

## **RESISTANCE TRAINING EXCEPTION**

---

### **BIO-VAR-CEM-12 `[COUNTERPOINT] [EMPIRICAL]`**

**Claim:** Resistance training produces "negative compensation" — both total daily energy expenditure and basal metabolic rate increase more than predicted by the exercise cost plus new muscle mass. This violates the constrained model. Several explanations: (1) Muscle repair and protein synthesis after resistance training require high metabolic investment, effectively raising the background "idling" cost of the organism. (2) Fat-free mass is the primary determinant of BMR, and each kg of FFM added typically increases BMR by \~20 kcal/day — resistance training may physically expand the metabolic ceiling rather than forcing reallocation within it. (3) Resistance training may not trigger the same hypothalamic "cost-cutting" algorithms as endurance activity, perhaps because it is intermittent and non-endurance-patterned — less indicative of the sustained foraging demands that shaped evolutionary energy constraint. (4) Resistance training is frequently paired with caloric surplus, which may signal the hypothalamus that the budget is flexible enough to permit expansion. The exception reveals a boundary condition: the constrained model applies most reliably to sustained aerobic exercise; resistance training may follow additive or super-additive logic. Confirming this consistently would break the model's claim to universality.

**Relevant to:** The ceiling CAN expand under specific conditions (this is architecturally important — not everything about energy is zero-sum reallocation), desirable difficulty for Go stats (if resistance training builds expensive tissue that permanently raises BMR, is there a Go-stat equivalent that builds expensive neural capacity?), BIO-VAR-MCA-05 (insulin resistance as allocation tool — resistance training may bypass the allocation system entirely by building new infrastructure rather than competing within existing allocation)

**Retrieval prompt:** "What specific studies show negative compensation from resistance training? Include the TEE and BMR data, the comparison to aerobic exercise, and whether the negative compensation persists long-term or is limited to the post-exercise recovery window. What evidence distinguishes the signaling environment of resistance vs. endurance training?"

---

## **CRITIQUE AND BOUNDARIES**

---

### **BIO-GON-PCA-01 `[COUNTERPOINT]`**

**Claim:** Gonzalez (2023) argues the constrained model has potential statistical and methodological limitations. The observed TEE "plateau" may be an artifact of regression dilution or spurious correlations — a single linear model often fits the data as well as the piecewise change-point model Pontzer proposes. Much evidence relies on hip-mounted accelerometry, which is poor at capturing non-ambulatory activity (cycling, swimming, load-carrying); if "missing" energy was actually unmeasured activity, the case for physiological constraint weakens. The trigger for compensation remains ambiguous — whether it is physical activity itself or the resulting energy deficit. If compensation is purely a starvation response, the constrained model may be a restatement of existing energy balance theory rather than a new metabolic principle. The strongest evidence against hard constraint would be a long-term RCT showing 1:1 additive TEE increase during energy balance (no weight loss), which has not been conducted. The true human response likely falls between purely additive and purely constrained, with compensation degree influenced by energy balance and exercise modality.

**Relevant to:** HPAM needs the allocation architecture, not the exact curve shape (the reallocation logic holds whether the ceiling is perfectly rigid or merely strongly constrained), the activity-vs-deficit debate (the chronicity-detection resolution below addresses this), honest framing for the book (the constrained model has legitimate critics and the book should use "strongly constrained" rather than "perfectly rigid"), existing BIO-ZIE-BSM-01 (same rhetorical structure: the critique challenges the mechanism while the phenotypic finding survives)

**Retrieval prompt:** "What specific statistical critiques does Gonzalez (2023) raise? Include the regression dilution argument, the single-linear-model comparison, the accelerometry limitation, and the energy balance moderation evidence. What experimental design does he propose as the definitive test?"

---

### **BIO-VAR-CEM-13 `[EMPIRICAL]`**

**Claim:** Adipose tissue functions as both an adaptive buffer against scarcity and a factor that degrades the system's total metabolic capacity. Humans evolved to carry significantly more fat (23-41%) than other great apes (9-23%) to support faster metabolic rates and energy-hungry brains. Fat is exceptionally energy-dense (255 kcal/oz) but metabolically quiet (\~2 kcal/lb/day versus \~6 kcal/lb/day for muscle). As body composition shifts from muscle to fat, overall metabolic intensity decreases. The hypothalamus monitors fat stores via leptin and treats them as both available reserves (leptin drop triggers starvation response) and settled baseline (after weight loss, the hypothalamus targets the pre-loss weight indefinitely, treating the previously heavier state as the baseline to defend). In modern environments, highly palatable processed foods can overwhelm hypothalamic algorithms, causing the manager to settle on a progressively higher fat baseline that persists even when it harms total capacity.

**Relevant to:** BIO-HAL-FOO-03 (convergent: leptin as "overall amplification" of satiety signals — same finding, different framing), BIO-VAR-LPR-01/02/03 (convergent: leptin resistance mechanism is the molecular detail for how the hypothalamus goes deaf to its own fat-monitoring system), existing Metabolic Harshness section (adipose dual role adds biological mechanism to the food environment narrative)

**Retrieval prompt:** "What evidence distinguishes fat-as-buffer from fat-as-pathology? Include the human vs. ape fat percentage comparison, the kcal density, the metabolic activity comparison with muscle, and the leptin-as-monitor mechanism. What is the evidence that the hypothalamus defends a higher set point after weight gain — include the long-term weight loss studies."

# **Warm-Blooded Brains**

**Source manifest:**

* \[NotebookLM responses, pasted in conversation\] Two structured extractions from a notebook containing: Yu (2014), Yu et al. (2014), Girard et al. (2023), Castelfranco & Hartline (2016), Yu et al. (2012), Neuroscience News summary of PNAS (2025).  
* \[conversation context\] Bennett NotebookLM summary on bird intelligence and warm-bloodedness.  
* \[google\_drive\_fetch: full doc\] BIO research doc — loaded this conversation, confirmed zero existing coverage of endothermy, avian cognition, or temperature-dependent neural computation.

**Duplicate check results:** No existing cards or Book Content in BIO on this topic. The COMP doc discusses Bennett's breakthrough stack but does not address the B3-simulation mammal-only boundary or the avian independent evolution of simulation capacity.

---

### **BIO-YUG-TMP-01 `[MECHANISM] [EMPIRICAL]`**

**Claim:** A constant warm body temperature (34–40°C) is required for reliable neural signal propagation across multi-layered cortical circuits. In computational Hodgkin-Huxley models, a temperature variance of just 5°C caused spike timing jitter to increase from 2ms to over 8ms and response reliability to drop from above 0.7 to below 0.3. The stable thermal environment of endotherms functions as a "firewall" protecting precise signaling from environmental fluctuations. Both mammals (36–37°C) and birds (39–40°C) maintain their body temperatures within the range that maximizes neural coding reliability. Without this stability, signals cannot propagate accurately through the deep, multi-layered architectures that complex cognition requires.

**Relevant to:** Bennett's simulation breakthrough (simulation requires multi-layered circuits that depend on spike timing precision), warm-bloodedness as prerequisite for B3-simulation (not just enhancement), avian independent evolution of simulation (birds evolved the same thermal prerequisite independently), Go as metabolically expensive (maintaining the firewall is itself energy-demanding)

**Retrieval prompt:** "What does Yu (2014) show about the relationship between temperature stability and neural coding reliability? Include the specific jitter and reliability numbers at different temperature variances, the optimal temperature range, and the 'firewall' metaphor. Does the study distinguish between warm temperature and stable temperature as separate contributions?"

---

### **BIO-YUG-TMP-02 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Warm body temperatures (37–42°C) maximize the energy efficiency of individual action potentials by accelerating sodium channel inactivation and reducing wasteful overlap between Na+ and K+ currents. At mammalian body temperature, Na+ entry is reduced to 1.3–1.41 times the theoretical minimum, compared to approximately 4 times the minimum in cold-water ectotherms like squid. Action potentials are 4 to 10 times more energy-efficient at 37°C than at 18°C. This efficiency is described as a "limiting factor in brain architecture" — without it, the metabolic cost of firing would constrain the brain to sparse codes incapable of supporting complex computation.

**Relevant to:** Go as metabolically expensive (efficiency per spike enables capacity for more spikes), Vitality as metabolic gestalt (total cognitive capacity \= efficiency × supply), the brain's 20%-of-body-energy budget (this is the mechanism that makes that budget viable)

**Retrieval prompt:** "What does Yu et al. (2012) show about the relationship between temperature and action potential energy efficiency? Include the Na+ entry ratios at different temperatures, the comparison to squid, and the argument about energy efficiency as a limiting factor for brain architecture. What happens to firing rates above 35°C?"

---

### **BIO-YUG-BSE-01 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Endothermic brains are 5 to 50 times heavier than ectothermic brains of comparable body mass, with the gap widening in larger animals (20–40× in large species). Temperature-regulated metabolism is described as the "most critical factor" for brain enlargement, but endothermy alone is not sufficient: non-neuronal glial cells provide necessary mechanical/trophic support and myelination for long-range communication. Glia are energetically inexpensive (costing only a few percent of what neurons do) but occupy substantial brain volume. Per-neuron metabolic cost is quantified at 2.51 × 10⁻¹⁰ watts for endotherms versus 0.563 × 10⁻¹⁰ watts for ectotherms — endotherm neurons are individually more expensive, but endothermy provides a higher total energy supply that more than compensates. Brain enlargement coincided independently with the development of endothermy in both mammals and birds.

**Relevant to:** Cross-taxon convergence (same thermal prerequisite, independent evolution in mammals and birds — strongest evidence for computational generalism over modularity), Go budget as metabolic supply (total brain energy \= neurons × cost-per-neuron; supply determines ceiling), glial infrastructure as hidden cost of capacity (cheap per unit but massive in volume)

**Retrieval prompt:** "What does Yu et al. (2014) show about brain size differences between endotherms and ectotherms? Include the 5–50× range, the per-neuron metabolic cost comparison, and the specific role of glia. How do they model total brain energy as a function of neuron count and per-neuron cost?"

---

### **BIO-GIR-MEM-01 `[EMPIRICAL]`**

**Claim:** Biological memory formation requires approximately 10mJ per bit of information — 6 to 7 orders of magnitude more energy-expensive than modern computer hardware (SSDs at \~0.5 nJ/bit). Storing a simple association (estimated at \~10 bits) costs roughly 100mJ. Persistent Long-Term Memory (LTM) is specifically disabled under low-energy conditions to favor survival. In fruit flies, forming a single associative memory reduced lifespan by 20% under starvation conditions. Less persistent memory forms (Anaesthesia Resistant Memory) are metabolically cheaper, suggesting a hierarchy of memory persistence scaled to energy availability.

**Relevant to:** Go as metabolically expensive (this is the quantitative anchor — 10mJ/bit gives a literal energy price for learning), masking as metabolic cost (if memory formation is this expensive, then the monitoring/simulation/inhibition operations of masking are drawing from the same finite budget), adaptive disabling under depletion (the brain shuts down expensive operations when energy drops — directly parallels Goblin Mode as forced triage), the memory persistence hierarchy as a Go-allocation model (system invests in durable storage only when budget permits)

**Retrieval prompt:** "What does Girard et al. (2023) estimate as the energy cost of biological memory formation? Include the mJ/bit figure, the comparison to computer hardware, the starvation-lifespan finding in Drosophila, and the distinction between persistent LTM and cheaper memory forms. Do they discuss whether the cost estimate transfers to mammalian systems?"

**Sourcing note:** Primary data from Drosophila (ectotherm). Authors note similar adaptive regulation in mammals but do not provide mammalian energy cost estimates. The 10mJ/bit figure is best treated as order-of-magnitude anchor, not precise cross-species claim.

---

### **BIO-CAS-NCS-01 `[MECHANISM] [EVOLUTIONARY]`**

**Claim:** Myelin evolved independently at least four times across animal taxa (vertebrates, earthworms, and two distinct crustacean groups). Myelinated fibers can reach conduction speeds above 200 m/s, enabling what the authors describe as "more computational sophistication in a given time interval." Myelin reduces the number of ions that must be pumped during signal transmission, decreasing activity costs — but carries high infrastructure costs for manufacturing and maintaining lipid-rich membranes. The evolution of rapid conduction follows a trajectory from slow chemical diffusion in single-celled organisms through core-conductor giant axons to saltatory conduction in myelinated fibers. Natural variation in conduction rates and path distances between individuals affects precision in temporal discrimination.

**Relevant to:** Bennett's breakthrough stack (conduction speed as prerequisite for simulation — running mental models faster than real-time requires fast internal signaling), computational generalism (myelin evolving independently 4× demonstrates convergent solution to a universal computational constraint), individual differences in Go capacity (variation in myelination \= variation in processing speed \= variation in how much computation fits in a time window)

**Retrieval prompt:** "What does Castelfranco and Hartline (2016) say about the independent evolution of myelin? Include the four taxa, the speed comparison (myelinated vs. unmyelinated), the 'computational sophistication in a given time interval' claim, and the infrastructure cost argument."

---

### **BIO-VAR-END-01 `[EMPIRICAL] [EVOLUTIONARY]`**

**Claim:** A global phylogenetic study (reported in PNAS, 2025\) found that endothermy provided the stable energy flow necessary to fuel large brains, and that parental investment — specifically, producing larger, well-fed offspring — was a critical additional factor enabling lineages to develop high brain-to-body ratios. Brains cannot shut down during hunger or sleep; they require constant energy flow. Species and lineages facing periods of energy loss have smaller brains. Human brain evolution succeeded partly because human infants are provisioned for years, creating the sustained energetic conditions for large brain development.

**Relevant to:** Parental investment as developmental supply-side for Go capacity (initial "startup capital"), life history theory connection (extended provisioning \= slow strategy prerequisite for high Go), Gen Z metabolic mismatch (if early provisioning sets the Go ceiling, then developmental nutrition matters for lifetime capacity)

**Retrieval prompt:** "What does the 2025 PNAS study find about the relationship between endothermy, parental investment, and brain size evolution? Include the number of species analyzed, the two key factors identified, and the specific claim about human infant provisioning."

**Source:** Song, Z., Schuppli, C., Drobniak, S. M., Heldstab, S. A., Griesser, M., & van Schaik, C. P. (2025). Parental investment and body temperature explain encephalization in vertebrates. *PNAS*, 122(45), e2506145122. n \= 2,600 species. Open access CC BY. DOI: 10.1073/pnas.2506145122.

# **Metabolic Allocation**

**Source manifest:** NotebookLM extraction (8 prompts), Card Spec (google\_drive\_fetch). BIO doc and Expensive Animal doc failed fetch — no duplicate-check performed. Brian confirmed prior cards integrated.

**Attribution note:** Many claims in this notebook emerge from synthesis across the source collection. Where a claim is clearly attributable to a single framework or author, I’ve assigned accordingly. Where it synthesizes across multiple notebook sources, I’ve used VAR. Brian should verify all author codes against actual source authorship.

---

## **Selfish Brain / Selfish Immune System Framework**

*Structural note: The Peters “Selfish Brain” and Straub “Selfish Immune System” frameworks together provide the core arbitration logic for HPAM’s metabolic allocation model. The brain and immune system are the two organs that can unilaterally override normal allocation — and they use the same tool (insulin resistance) to do it. This is the biological grounding for Vitality as a contested resource, not a freely available one.*

**BIO-PET-SBR-01 `[MECHANISM]`**

**Claim:** The brain self-regulates its energy supply with the highest priority in the organism. When neuronal ATP drops (detected in the ventromedial hypothalamus), the brain activates a “brain-pull” via the sympathoadrenal system and HPA axis, suppressing pancreatic insulin secretion (Cerebral Insulin Suppression / CIS). This locks insulin-dependent tissues (muscle, fat) out of glucose uptake, leaving circulating glucose available for the brain’s insulin-independent transporters. The brain uses the body’s stress systems as tools to allocate energy to itself.

**Relevant to:** Vitality as contested resource, brain’s metabolic privilege, Go stats as metabolically expensive capacities, the Expensive Animal (Move 2 — everything costs)

**Retrieval prompt:** “What does Peters say about the specific mechanism of cerebral insulin suppression? Include the VMH detection threshold, the sympathoadrenal pathway, and how insulin suppression mechanistically locks out peripheral tissues.”

---

**BIO-STR-EMA-01 `[MECHANISM] [FRAMING MOVE]`**

**Claim:** Energy allocation in organisms follows a hierarchy governed by “wise selfishness” versus “foolish selfishness.” Wise selfishness is a transient prioritization strategy — a tissue takes more than its share to meet an acute threat, then subsides, benefiting the whole organism. Foolish selfishness is a tissue pursuing narrow self-interest that harms the whole organism — it does not subside when the threat passes. Tumors and chronically expanding adipose tissue exhibit foolish selfishness. The distinction is not structural origin but whether the tissue’s increased demand remains coupled to systemic regulation.

**Relevant to:** Substitution ratchet (signal substitution → capacity atrophy → preference capture), masking costs as metabolic, pathological entrenchment, attractor dynamics (wise \= reversible pitchfork, foolish \= irreversible saddle-node)

**Retrieval prompt:** “What does Straub say about the specific criteria separating wise from foolish selfishness? Include examples of each, and whether any tissue can transition from wise to foolish over time.”

---

**BIO-STR-EMA-02 `[MECHANISM] [EMPIRICAL]`**

**Claim:** During severe immune challenges, the immune system moves to the top of the organism’s energy hierarchy, overriding the brain’s default priority. The immune system is non-insulin-dependent for glucose uptake, so it benefits from the same insulin resistance mechanism the brain uses. Mild immune activation (non-febrile respiratory infection) increases resting metabolic rate by 8–14%. Severe immune challenges (sepsis, major burns) increase energy demands 25–55% above baseline. The organism exhibits “sickness behavior” — lethargy, withdrawal, failure to concentrate, anorexia — which is not a byproduct of illness but an active motivational program that reorganizes priorities to conserve energy for immune function.

**Relevant to:** Vitality depletion during illness, Withdrawal as Go stat (sickness behavior looks like Withdrawal activation), the Expensive Animal (Move 2), why chronic illness reshapes personality

**Retrieval prompt:** “What is the direct human evidence for immune override of brain metabolic priority? Include the RMR measurement studies, the sickness behavior mechanism, and the specific conditions under which immune priority exceeds brain priority.”

---

**BIO-STR-EMA-03 `[EMPIRICAL] [COUNTERPOINT]`**

**Claim:** Alzheimer’s disease patients frequently exhibit high core body temperature (indicating systemic inflammation) alongside low brain metabolism and temperature. This pattern is consistent with chronic immune override of brain metabolic priority — the body remains inflamed while the brain has been deprioritized. Animal studies of torpor show “Alzheimer-anatomy” (tau phosphorylation) during hibernation that reverses upon waking, suggesting the metabolic state may drive the pathology rather than vice versa. However, the causal claim — that chronic immune activation causes neurodegeneration by deprioritizing the brain — is a theoretical inference from the “selfish immune system” framework, not established consensus.

**Relevant to:** Aging as defunding vs. breakdown, long-term consequences of immune-brain competition, attractor dynamics (saddle-node — can the brain’s original state be restored?)

**Retrieval prompt:** “What is the specific evidence linking chronic inflammation to reduced brain metabolism in AD? Include the torpor/hibernation-anatomy parallel, the metabolically-induced hibernation hypothesis, and where the authors acknowledge this is inference rather than direct observation.”

---

## **Allocation Mechanisms and Triage**

**BIO-VAR-MCA-01 `[MECHANISM]`**

**Claim:** The organism’s energy triage is coordinated by the Energy Allocation System (EAS), operating through three interlocking endocrine axes: HPA (stress — cortisol mobilizes substrates and suppresses lower-priority functions), HPT (metabolism/pacing — thyroid hormones set metabolic rate), and HPG (reproduction/growth — sex steroids and growth hormone govern anabolic investment). These axes function as a coordinated governance network, not independent systems. Cortisol actively suppresses the HPG and HPT axes to defund growth and metabolic pacing during stress.

**Relevant to:** The Expensive Animal (Move 2), Vitality’s biological substrate, how personality change gets funded or defunded, three-axis model as “budget committee”

**Retrieval prompt:** “What does the EAS model say about how the three axes coordinate? Include the specific suppression pathways (cortisol suppressing HPG and HPT), and whether the axes ever conflict with each other rather than coordinating.”

---

**BIO-VAR-MCA-02 `[MECHANISM]`**

**Claim:** Baseline cortisol levels scale predictably with mass-specific metabolic rate across mammals, indicating that cortisol’s primary role is managing daily energy flux — not exclusively emergency response. Acutely, cortisol mobilizes glucose and lipids for brain-pull. Chronically, the same mechanism becomes entrenched and maladaptive. This is one mechanism operating at different timescales, not two different mechanisms sharing a molecule. The “emergency” and “reallocation” framings describe the same function observed at different durations.

**Relevant to:** Cortisol as allocation signal (not just stress signal), masking costs as chronic cortisol, attractor dynamics (chronic activation \= basin deepening), the Expensive Animal

**Retrieval prompt:** “What is the evidence that baseline cortisol scales with metabolic rate? Include the species-comparative data and the argument for cortisol as a metabolic pacing hormone rather than purely a stress hormone.”

---

**BIO-VAR-MCA-03 `[MECHANISM]`**

**Claim:** When cortisol activation becomes chronic, the reallocation logic does not vanish — it becomes entrenched and degrades through a specific sequence: (1) Growth, maintenance, and repair (GMR) are starved, producing subclinical Exposure-Related Malnutrition even when nutrient intake is adequate. (2) Anabolic resistance develops — muscle protein synthesis stops responding to nutrients because energy is being triaged for survival. (3) Metabolic rigidity sets in — the organism loses fuel-switching flexibility. (4) HPA axis exhaustion — flattened diurnal rhythms, impaired mobilization capacity. (5) Mitochondrial allostatic load — ROS overload, fragmentation, mitophagy failure, accelerated epigenetic aging.

**Relevant to:** Masking costs (chronic allostatic degradation), attractor dynamics (entrenched patterns cannibalize escape capacity), Vitality depletion cascade, aging trajectory, the Expensive Animal

**Retrieval prompt:** “What is the evidence for each stage in the chronic cortisol degradation sequence? Include the ERM mechanism, anabolic resistance studies, metabolic rigidity definition, HPA exhaustion markers, and mitochondrial allostatic load.”

---

**BIO-VAR-MCA-04 `[MECHANISM] [FRAMING MOVE]`**

**Claim:** The organism’s triage order is not a fixed hierarchy but a priority matrix indexed by threat type. During chronic resource scarcity (famine), construction is cut first — growth and reproduction are suppressed to preserve somatic maintenance. During acute or chronic stress, maintenance is cut first — DNA repair, immune surveillance, neurogenesis, and autophagy are suppressed to fund the stress response. The same organism with the same budget will sacrifice different functions depending on what kind of crisis it faces. Fixed priorities (brain/heart always funded) form the constants; everything else is context-dependent.

**Relevant to:** Why personality change is harder under stress (maintenance of current personality competes with stress response), the Expensive Animal (Move 2), triage as framework for understanding phenotypic change costs

**Retrieval prompt:** “What specific evidence supports the claim that scarcity and stress produce different triage orders? Include the famine data (construction cut first) and the stress data (maintenance cut first), and any cases where both hit simultaneously.”

---

**BIO-VAR-MCA-05 `[MECHANISM]`**

**Claim:** Insulin resistance functions as an allocation tool, not merely a disease state. Because the brain and immune system use insulin-independent glucose transporters, inducing IR in peripheral tissues (muscle, fat) creates hyperglycemia that preferentially feeds insulin-independent organs. In acute settings this is adaptive (“wise selfishness”). In chronic settings the same mechanism becomes pathological — peripheral tissues are permanently locked out, fat accumulates, and the organism loses metabolic flexibility. The transition from tool to trap is a function of duration, not a change in mechanism.

**Relevant to:** Substitution ratchet (tool → trap), attractor dynamics (pitchfork → saddle-node), the Expensive Animal, metabolic syndrome reframe

**Retrieval prompt:** “What is the mechanistic pathway by which IR shunts glucose to brain and immune system? Include the transporter types (GLUT1 vs. GLUT4), and the evidence for when acute IR transitions to chronic metabolic dysfunction.”

---

## **Tumor and Adipose Hijacking**

**BIO-VAR-ONC-01 `[MECHANISM]`**

**Claim:** Tumors subvert normal energy allocation through multiple mechanisms: they hijack adjacent adipocytes, forcing them to “brown” and release metabolites (lactate, fatty acids) to feed the tumor; they redirect blood supply through VEGF-mediated angiogenesis triggered by hypoxia; and they exploit the Warburg effect to outcompete normal cells for glucose by running aerobic glycolysis (less efficient per molecule, but faster throughput). Tumors can also reprogram liver function before metastasis, decreasing albumin synthesis and the urea cycle to free amino acids for tumor growth. In extreme cases they induce cachexia — metabolic wasting of distant organs.

**Relevant to:** Foolish selfishness (pathological hijacking), the Expensive Animal (hijacking metaphor for personality entrenchment), attractor dynamics (tumor as autonomous attractor that cannibalizes system resources)

**Retrieval prompt:** “What are the specific mechanisms by which tumors reprogram host metabolism? Include the adipocyte browning, VEGF/angiogenesis, Warburg effect, liver reprogramming, and cachexia pathways.”

---

**BIO-VAR-ONC-02 `[MECHANISM]`**

**Claim:** Hypertrophied adipose tissue transitions from metabolic participant to metabolic hijacker when it outgrows its blood supply. The resulting hypoxia triggers chronic inflammation, which drives further metabolic dysregulation in a self-reinforcing cycle. Expanding fat deposits broadcast endocrine signals (leptin, adipokines, inflammatory cytokines) that shift systemic allocation in their favor. This is structurally parallel to tumor behavior — both involve a tissue that has decoupled from normal systemic regulation and begun redirecting resources to sustain its own growth — but the adipose pathway is slower and uses endocrine lobbying rather than angiogenic hijacking.

**Relevant to:** Foolish selfishness (adipose version), the adipose tissue analogy from attractor dynamics session (fat as endocrine organ that lobbies for resources), the Expensive Animal, obesity as metabolic entrenchment

**Retrieval prompt:** “What specific endocrine signals do hypertrophied adipose deposits use to shift allocation? Include the hypoxia-inflammation cycle, the cytokine profile, and the comparison to tumor metabolic behavior.”

---

## **Life History and Trade-Off Theory**

**BIO-AIW-ETH-01 `[EVOLUTIONARY] [COUNTERPOINT]`**

**Claim:** The Expensive Tissue Hypothesis proposes that brain expansion during human evolution was funded by a compensatory reduction in gut size — an organ-level trade-off within a finite energy budget. The brain and gut are both metabolically expensive, and their combined cost must be sustained by total energy intake. However, intraspecific studies have failed to replicate this trade-off at the individual level, suggesting the relationship may be a species-level evolutionary pattern rather than a constraint operating within individual organisms.

**Relevant to:** The Expensive Animal (foundational claim — organ budgets compete), Go stats as metabolically expensive (brain operations cost real energy), whether personality trade-offs operate at population or individual level

**Retrieval prompt:** “What is the original evidence for the expensive tissue hypothesis, and what are the specific intraspecific studies that challenge it? Include the Aiello & Wheeler data and the counterevidence.”

---

**BIO-KIR-DSM-01 `[EVOLUTIONARY] [FRAMING MOVE]`**

**Claim:** The Disposable Soma theory proposes that organisms strategically underinvest in somatic maintenance to maximize early-life reproductive success. Late-life survival is not an accident of wear — it is the downstream consequence of an allocation decision that favored reproduction over repair. The organism may actively endorse breakdown of muscle tissue to mobilize amino acids for immune activation or wound repair, effectively defunding a long-term asset to solve an immediate crisis.

**Relevant to:** Aging as strategic defunding, the Expensive Animal (Move 2), attractor dynamics (deep attractors deplete maintenance budget), Vitality decline with age

**Retrieval prompt:** “What does Kirkwood argue about the specific mechanism by which soma is ‘disposed’? Include the amino acid mobilization from muscle, the relationship between reproductive investment and somatic decay, and any evidence for the allocation being actively regulated versus passively drifting.”

---

**BIO-AUL-CPL-01 `[FRAMING MOVE]`**

**Claim:** The costs and limits of phenotypic plasticity are often confused or may describe the same phenomena differently. A “cost” of plasticity is a fitness reduction for being plastic versus fixed in a given environment. A “limit” is a boundary on what the plastic response can achieve. But a change the organism cannot afford (cost) is also a change it cannot make (limit), suggesting these may not be genuinely distinct categories. Clarifying this distinction matters for understanding why some phenotypic changes are merely expensive while others are impossible regardless of available resources.

**Relevant to:** The Expensive Animal (cost vs. limit of personality change), hard limits on Go stats vs. expensive-but-achievable changes, why some personality changes fail despite high Vitality

**Retrieval prompt:** “What does Auld argue about the specific cases where costs and limits collapse into the same thing? Include the examples and whether the authors propose criteria for distinguishing them when they don’t collapse.”

---

**BIO-GAR-TRD-01 `[MECHANISM] [FRAMING MOVE]`**

**Claim:** Biological trade-offs exist as complex networks rather than simple binary relationships. Garland et al. identify six general categories of trade-offs: allocation constraints, functional conflicts, shared biochemical pathways, and three others. Path analysis and network simulations demonstrate that a change in one trait can propagate through the trade-off network to affect traits that appear unrelated. This means the cost of a phenotypic change cannot be assessed by looking at the changed trait alone — the network effects must be included.

**Relevant to:** The Expensive Animal (why personality change has costs that seem disproportionate), stat interactions in HPAM (changing one stat affects others via network), Go stats as shared capacity pool

**Retrieval prompt:** “What are Garland’s six categories of trade-offs, and what do the network simulations show about how changes propagate? Include the path analysis methodology and the specific finding about indirect trade-off effects.”

---

## **Dynamic Energy Budget and Developmental Locking**

**BIO-KOO-DEB-01 `[MECHANISM]`**

**Claim:** Dynamic Energy Budget theory models energy allocation using a “kappa-rule” where a fixed fraction (κ) of utilized energy goes to somatic maintenance and growth, with the remainder (1−κ) going to maturation and reproduction. κ is treated as a species-specific parameter (e.g., \~0.65 for blue mussel). Somatic maintenance has absolute priority within the κ fraction — if energy is insufficient for maintenance, the organism shrinks structural volume before it stops maintaining what remains. The organism is not negotiating the split in real time under standard conditions; it follows a preset ratio.

**Relevant to:** The Expensive Animal (quantitative allocation model), Vitality as the κ fraction for personality maintenance, Go stats as somatic maintenance equivalents

**Retrieval prompt:** “What does DEB theory say about the conditions under which κ deviates from its species-typical value? Include the mussel parameterization, the priority rule for maintenance, and the ‘shrinking’ mechanism when maintenance can’t be funded.”

---

**BIO-VAR-MCA-06 `[MECHANISM] [EVOLUTIONARY]`**

**Claim:** While DEB theory treats κ as stable, broader life history models show allocation ratios shift with condition. Acute shifts are facultative and reversible — lizards only trade off wound healing for reproduction when food is scarce; restore resources and the trade-off disappears. However, shifts during developmental critical windows canalize permanently via epigenetic programming. The “thrifty phenotype” hypothesis: patterns of fetal/infant growth permanently shape metabolic capacity (nephron number, insulin secretion). Early-life stress causes lasting epigenetic changes (glucocorticoid receptor methylation), locking in high stress reactivity and altered allocation set-points for life.

**Relevant to:** Abdi’s two-hit developmental model, calibration windows, developmental canalization, the Expensive Animal (permanent vs. reversible allocation shifts), why early environment has outsized personality effects

**Retrieval prompt:** “What is the specific evidence for developmental locking of allocation ratios? Include the thrifty phenotype data, the glucocorticoid receptor methylation studies, and the lizard wound-healing reversibility experiment.”

---

## **Maintenance, Construction, and Aging**

**BIO-VAR-MCA-07 `[MECHANISM]`**

**Claim:** DEB theory distinguishes “construction costs” (building biomolecules — proteins, lipids) from “operating costs” (running processes — ion pumping, locomotion). However, the boundary is blurry because many maintenance functions are continuous construction: protein turnover and cellular repair require constant synthesis of new biomolecules. Maintaining an existing phenotype requires ongoing construction. Despite this blurriness at the cellular level, the organism’s budget treats them as distinct categories with different priority rules — maintenance before construction during scarcity, construction before maintenance during acute stress.

**Relevant to:** Attractor dynamics (maintenance costs vs. escape costs), the Expensive Animal (maintaining personality costs energy even when nothing is changing), Vitality as fuel for both maintenance and change

**Retrieval prompt:** “What does DEB theory say about the quantitative difference between construction and operating costs? Include specific examples of maintenance-as-construction (protein turnover rates), and whether the organism can distinguish them in real time.”

---

**BIO-VAR-MCA-08 `[MECHANISM]`**

**Claim:** Sleep functions as diurnal energy reallocation. Wakefulness prioritizes thermoregulation and sensory processing. NREM sleep reallocates energy toward immunity, protein synthesis, and cellular repair. This is not merely “rest” — it is a scheduled maintenance window where the organism shifts budget from operating costs to construction/repair costs that cannot be funded while the sensory and locomotor systems are running.

**Relevant to:** The Expensive Animal (maintenance has a schedule, not just a budget), sleep deprivation as Vitality depletion, why inadequate sleep degrades personality expression

**Retrieval prompt:** “What is the specific energetic evidence that NREM sleep reallocates resources? Include the metabolic rate data during sleep stages, the protein synthesis timing data, and the immune function scheduling.”

---

**BIO-VAR-MCA-09 `[EMPIRICAL]`**

**Claim:** Under calorie restriction, the brain is relatively spared while body mass decreases — the brain experiences only minor mass/energy changes compared to major changes in the body. CR induces autophagy (cellular self-digestion that clears damaged molecules and organelles), effectively extending healthspan by shifting resources from growth to maintenance. This demonstrates that the organism can extend tissue lifespan if it redirects budget to maintenance — the machinery for maintenance persists even when it is normally deprioritized.

**Relevant to:** The Expensive Animal (brain’s metabolic privilege), aging as defunding (reversible if caught early), Vitality reallocation through lifestyle change

**Retrieval prompt:** “What specific brain regions or functions are preserved under CR, and which body systems lose mass first? Include the autophagy mechanism, the caloric threshold for autophagy induction, and the lifespan extension data.”

---

**BIO-VAR-AGE-01 `[MECHANISM] [EVOLUTIONARY]`**

**Claim:** Aging begins as strategic trade-off (disposable soma — underinvesting in repair to fund reproduction) but transitions to involuntary breakdown when allostatic overload depletes the organism’s energetic reserve. The Proteome Cost Minimization theory identifies a point of no return: when supplied energy can no longer satisfy the increasing maintenance costs of an aging proteome, the organism enters proteome collapse — misfolded proteins accumulate, and diseases like memory loss follow. Chronic stress accelerates this by making the organism “more mouse-like” — triggering hypermetabolism that burns through reserve capacity faster.

**Relevant to:** Aging trajectory in the Expensive Animal, the Expensive Animal (threshold between trade-off and breakdown), attractor dynamics (saddle-node — original configuration ceases to exist), Vitality decline with age

**Retrieval prompt:** “What is the specific evidence for the proteome cost minimization threshold? Include the energetic accounting (how much maintenance costs increase with age), the ‘mouse-like hypermetabolism’ finding, and whether the point of no return can be predicted before it’s reached.”

---

## **Reductive Evolution**

**BIO-DSO-MDB-01 `[EVOLUTIONARY] [MECHANISM]`**

**Claim:** Bacteria frequently lose biosynthetic genes when the environment reliably provides essential metabolites, rendering them dependent on their environment (auxotrophy). Experimental evolution with *E. coli* and *Acinetobacter baylyi* shows this “reductive evolution” is driven by natural selection for metabolic efficiency, not just genetic drift — organisms that dismantle unused infrastructure gain a competitive advantage by saving the metabolic cost of maintaining it. This is an organism actively choosing to trade capacity for efficiency, and it becomes a trap when the environment changes and the dismantled infrastructure is needed again.

**Relevant to:** The Expensive Animal (infrastructure dismantling), “easy-locked” environments in HPAM (reliable external provision → internal capacity atrophy), substitution ratchet (capacity atrophy stage), niche constriction

**Retrieval prompt:** “What does D’Souza show about the fitness advantage of gene loss versus the vulnerability it creates? Include the experimental evolution data, the metabolic cost savings measured, and the conditions under which auxotrophy becomes fatal.”

---

Entrenched Subsystems Corrupt the Referee — Catalogue Cards

**Source manifest:** NotebookLM extraction (6 primary prompts \+ 3 follow-up prompts) from a notebook containing \~33 sources across addiction neurobiology, cancer cachexia, obesity/leptin resistance, and computational/interoceptive models. Access method: \[notebooklm responses pasted in conversation\]. Card Spec loaded via google\_drive\_fetch. BIO doc loaded via google\_drive\_fetch — duplicate-checked.

**Duplicate check results:** BIO already covers wanting/liking (BIO-NOR-TBB-01/02), prediction error → attractor states (TBB-03/04/05), selfish brain (BIO-PET-SBR-01), wise/foolish selfishness (BIO-STR-EMA-01), tumor/adipose hijacking descriptively (BIO-VAR-ONC-01/02), and IR as allocation tool (BIO-VAR-MCA-05). None of the cards below duplicate existing content. Where convergence exists, a note on the existing card is flagged rather than a new card drafted.

---

## **LEPTIN RESISTANCE — INPUT DEGRADATION**

*Structural note: The leptin resistance sequence is the cleanest biological model of how a subsystem corrupts its regulator’s inputs. The one-day inflammation finding and the clamping experiment together establish that the referee starts going deaf before the subsystem has fully expanded, and that it’s the volume of the signal — not the dietary environment alone — that breaks the receiver. This is the biological template for HPAM’s personality entrenchment argument: a deep attractor doesn’t just consume resources, it degrades the system’s ability to detect that it’s consuming too much.*

---

### **BIO-VAR-LPR-01 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Leptin signaling contains an inherent self-silencing mechanism. When leptin binds its receptor, it activates STAT3, which transcribes SOCS3 as a negative feedback loop. Under chronic hyperleptinemia, SOCS3 expression becomes persistent and physically blocks the JAK2-STAT3 signaling pathway — the receptor’s own downstream product shuts down the receptor. PTP1B provides a second brake: localized in the endoplasmic reticulum, it dephosphorylates JAK2 to attenuate signaling. Critically, hyperleptinemia is *required* for resistance to develop: in experiments where plasma leptin was clamped to lean levels, animals remained leptin-sensitive despite becoming obese on a high-fat diet, demonstrating that dietary fat alone does not block the signal — the volume of leptin exposure is what breaks the receiver.

**Relevant to:** Referee corruption mechanism (input degradation — the subsystem’s growth produces the signal volume that degrades the referee’s sensitivity), substitution ratchet (signal substitution phase — the tissue’s normal feedback signal becomes the instrument of its own deafening), the Expensive Animal (Move 2 — the cost of carrying excess adipose includes degrading the system that would detect the excess)

**Retrieval prompt:** “What do the sources say about the specific molecular sequence by which SOCS3 and PTP1B block leptin signaling? Include the STAT3 transcription loop, the JAK2 dephosphorylation by PTP1B, and the leptin-clamping experiment that demonstrates hyperleptinemia is required for resistance.”

---

### **BIO-VAR-LPR-02 `[EMPIRICAL] [MECHANISM]`**

**Claim:** Hypothalamic inflammation precedes obesity and operates through the same intracellular machinery as leptin resistance. Activation of the IKKβ-NF-κB inflammatory pathway in the hypothalamus is detectable after only one day of high-fat diet exposure. SOCS3 upregulation in the arcuate nucleus follows within one week — before measurable obesity has developed. Saturated fatty acids trigger this cascade by activating TLR4 on hypothalamic microglia, which produce proinflammatory cytokines (TNF-α, IL-1β, IL-6). ER stress functions as a bidirectional bridge: NF-κB activation promotes ER stress, and ER stress promotes NF-κB activation, creating a self-sustaining positive feedback loop. Artificial activation of the IKKβ-NF-κB pathway is sufficient to impair leptin signaling and promote weight gain; conversely, inhibiting hypothalamic inflammation can reverse diet-induced leptin resistance.

**Relevant to:** Temporal sequence of referee corruption (the referee starts going deaf before the subsystem has fully expanded — inflammation at day 1, SOCS3 at week 1, obesity later), ER stress as self-sustaining loop (once established, the inflammation-resistance cycle maintains itself even if the original dietary trigger is reduced), the Expensive Animal (the organism’s own defensive inflammatory response becomes the mechanism of its regulatory capture)

**Retrieval prompt:** “What do the sources say about the timeline of hypothalamic inflammation relative to obesity onset? Include the one-day IKKβ-NF-κB finding, the one-week SOCS3 finding, and the ER stress bidirectional loop. What is the evidence that inhibiting hypothalamic inflammation reverses leptin resistance — include the specific pathway targeted and the outcome measures.”

---

### **BIO-VAR-LPR-03 `[EMPIRICAL]`**

**Claim:** The brain actively defends a corrupted metabolic set point for years after the corruption is removed. One year after weight loss, circulating levels of leptin, ghrelin, peptide YY, CCK, amylin, and other appetite mediators have not returned to pre-obese baselines — maintaining constant hormonal pressure to regain weight. In a follow-up of “Biggest Loser” participants, metabolic adaptation (the slowing of resting metabolic rate beyond what body composition change would predict) persisted and actually increased in magnitude six years after initial weight loss, despite significant weight regain. The brain treats the previously obese state as the baseline it must return to, interpreting weight loss as a starvation emergency requiring correction.

**Relevant to:** Why self-rescue from deep attractors is structurally hard (the referee doesn’t just fail to detect the problem — it actively fights the correction), the Expensive Animal (the organism funds the defense of a state that harms it), attractor dynamics (the corrupted set point has become the new stable equilibrium — recovery requires building a new basin, not returning to the old one), substitution ratchet terminal phase (preference capture — the system now prefers the corrupted state)

**Retrieval prompt:** “What specific hormonal changes persist one year after weight loss? Include the direction and magnitude of change for each appetite mediator. What does the Biggest Loser follow-up show about the six-year trajectory of metabolic adaptation — did metabolic rate recover partially, hold steady, or worsen? What is the sample size and attrition rate?”

---

## **ADDICTION — INTERNAL CO-OPTATION**

*Structural note: The addiction cards below cover three aspects of internal co-optation that are NOT in existing BIO coverage. BIO-NOR-TBB-01/02 cover wanting/liking dissociation from Nord’s perspective. What’s new here: (1) the anatomical migration from goal-directed to compulsive circuitry, (2) the metaplasticity concept (single exposure changes learning rules, not behavior), and (3) incubation of craving and the D1/D2 asymmetry. These are complementary to Nord, not duplicative.*

---

### **BIO-VAR-ACR-01 `[MECHANISM] [EMPIRICAL]`**

**Claim:** Behavioral control migrates through three anatomically distinct stages as a pattern becomes entrenched. Goal-directed stage: the ventral striatum (nucleus accumbens shell and core) encodes action-outcome associations, regulated by the prelimbic cortex and posterior dorsomedial striatum. Habitual stage: control shifts to the dorsolateral striatum and infralimbic cortex, encoding stimulus-response associations where environmental cues trigger behavior automatically, independent of the reward’s current value. Compulsive stage: control is entrenched in the DLS while the extended amygdala drives behavior through negative reinforcement; prefrontal cortex and anterior cingulate cortex become hypoactive, effectively uncoupling the evaluative system from behavioral execution. Goal-directed and habitual systems initially operate in parallel and compete for control; the evaluative system is functionally lost when the PFC/ACC can no longer exert top-down inhibition — producing “behavioral crystallization” where the behavior persists despite clear aversive outcomes. This migration is not unique to drug addiction: it occurs in pathological gambling, compulsive eating, punding in Parkinson’s patients, and is the same circuitry used for normal skill automaticity.

**Relevant to:** Referee bypass (at the compulsive stage, the evaluation system isn’t just biased — it’s been structurally disconnected from the behavior it’s supposed to evaluate), the Expensive Animal (the brain’s standard architecture for making behavior efficient is what makes it capturable), attractor dynamics (the migration from ventral to dorsal is the neural implementation of basin deepening), masking architecture (the habitual stage is behavior running without evaluative consultation — structurally parallel to overlearned social performance)

**Retrieval prompt:** “What do the sources say about the specific brain regions involved at each stage of the migration from goal-directed to compulsive behavior? Include the prelimbic/infralimbic cortex distinction, the DMS-to-DLS shift, the extended amygdala recruitment, and the PFC/ACC uncoupling. What is the evidence that this migration occurs in non-drug contexts — include punding, gambling, and binge eating data?”

---

### **BIO-VAR-ACR-02 `[MECHANISM] [EMPIRICAL]`**

**Claim:** A single drug exposure induces NMDA receptor-dependent long-term potentiation of excitatory transmission onto VTA dopamine neurons within hours, measured by an increased AMPA:NMDA ratio and insertion of calcium-permeable GluA2-lacking AMPA receptors. This initial VTA rewriting does not encode addiction — it is “metaplasticity”: it changes the rules for future learning, making it easier to induce persistent changes downstream in the nucleus accumbens. VTA changes are transient (reverting within 5-10 days), but NAc changes are persistent or permanent — including selective potentiation of D1-expressing MSNs (the “go” pathway), chronic reduction of D2 receptor density, and increased dendritic spine density that makes neurons hyperreactive to drug cues. The VTA gate resets; the NAc prison doesn’t. NAc changes are contingent on prior VTA plasticity — blocking VTA changes prevents the downstream rewrite.

**Relevant to:** Metaplasticity as vulnerability creation (the first exposure doesn’t create the prison, it unlocks the door — HPAM parallel: a single significant experience in a personality domain may not create an entrenched pattern but may change how easily future experiences entrench), D1/D2 asymmetry (the evaluation circuit is physically restructured to say “go” louder and “no-go” quieter), the Expensive Animal (the brain’s efficiency mechanisms — synaptic plasticity, dendritic remodeling — are what get exploited)

**Retrieval prompt:** “What do the sources say about the timeline and reversibility of synaptic changes at the VTA versus the NAc? Include the AMPA:NMDA ratio data, the GluA2-lacking receptor insertion, the D1/D2 MSN differential, the dendritic spine density finding, and the experiment showing that blocking VTA changes prevents NAc adaptation.”

---

### **BIO-VAR-ACR-03 `[EMPIRICAL]`**

**Claim:** Relapse vulnerability does not decrease monotonically during abstinence — it increases during the first month, a phenomenon called “incubation of craving.” The mechanism: surface expression of GluA2-lacking AMPA receptors in the NAc mediates this incubation effect, meaning the synaptic substrate of wanting is actively remodeling during abstinence in a direction that increases drug-seeking. Neural sensitization persists for months or years, keeping the brain hyperreactive to drug-associated cues even after withdrawal symptoms have resolved. Recovery from addiction is not circuitry reversal: sustained abstinence is associated with increased functional connectivity between left dlPFC and nucleus accumbens — a workaround where a strengthened prefrontal “brake” continuously overrides intact, sensitized subcortical circuitry. The compulsive architecture stays; the organism builds an inhibitory bypass, not a repair.

**Relevant to:** Recovery-as-workaround (the entrenched circuitry is not dismantled but held in check — structurally parallel to HPAM’s masking: the routing persists, a different system suppresses its expression), incubation of craving as counterintuitive prediction (willpower narratives assume vulnerability decreases with time; the biology says the opposite during early abstinence), masking costs (active inhibition of sensitized circuitry is metabolically expensive — the “recovered addict” is paying ongoing masking costs), the Expensive Animal (escape from a deep attractor requires building new infrastructure, not restoring old — saddle-node, not pitchfork)

**Retrieval prompt:** “What do the sources say about the incubation of craving mechanism? Include the GluA2-lacking AMPA receptor data, the timeline of increasing vulnerability during abstinence, and the dlPFC-NAc connectivity finding in sustained recovery. Is there evidence for a time horizon after which incubation reverses?”

---

### **BIO-ROB-IST-01 `[MECHANISM] [FRAMING MOVE]`**

**Claim:** Robinson’s 2025 update to incentive-sensitization theory reports that wanting/liking dissociation extends well beyond drug contexts. Non-drug evidence includes: pathological gambling, hypersexuality, compulsive shopping, and Internet use (hyperreactive cue-triggered dopamine release without corresponding pleasure increase); binge eating in obesity (heightened wanting for palatable food without enhanced liking); Dopamine Dysregulation Syndrome in Parkinson’s patients (compulsive pursuit of medication or hobbies they don’t enjoy); a novel salt appetite state where an unliked intense salt cue is instantly “wanted” before the salt is ever retasted; and an amygdala stimulation paradigm where rats intensely “want” to approach an electrified shock rod they visibly dislike. Approximately 90% of the NAc generates intense wanting when stimulated, but only \~10% (the “hedonic hotspot”) can enhance liking. A “firewall” between motivation and cached hedonic values protects the integrity of learned reward predictions but makes the system unable to detect that a pursuit is no longer rewarding once sensitization has occurred.

**Relevant to:** Wanting/liking dissociation as a general corruption mechanism (not addiction-specific — any entrenched behavioral pattern can produce wanting without liking), the firewall concept (the brain’s architecture for protecting learning integrity is what prevents self-correction — same design-feature-as-vulnerability logic as the robust-yet-fragile principle), existing BIO-NOR-TBB-01/02 (Robinson is the original source; Nord extended it — Robinson’s 2025 update adds the non-drug evidence and the firewall concept that Nord doesn’t cover), the Expensive Animal (the organism pursues something intensely without finding it rewarding — this is the phenomenology of personality entrenchment)

**Retrieval prompt:** “What does Robinson (2025) say about the non-drug evidence for incentive sensitization? Include the salt appetite experiment, the shock rod paradigm, the Parkinson’s DDS data, and the 90%/10% NAc wanting/liking ratio. What is the ‘firewall’ between motivation and cached values, and how does it prevent the organism from detecting that a pursuit is no longer rewarding?”

---

## **CACHEXIA — SOURCE FALSIFICATION**

*Structural note: The existing BIO-VAR-ONC-01/02 describe tumor hijacking descriptively (Warburg, VEGF, cachexia mentioned, adipose endocrine lobbying). What’s new below: the specific pathways by which falsified metabolic data reaches the brain, the LIF/JAK-STAT mimicry of leptin signaling, and the dual answer on whether the referee is reading false reports or has been compromised itself (both).*

---

### **BIO-VAR-CXS-01 `[MECHANISM]`**

**Claim:** Tumor-derived signals reach the hypothalamus through at least five distinct pathways: (1) Direct access via “brain windows” — the mediobasal hypothalamus and median eminence lack a complete blood-brain barrier, allowing circulating cytokines to reach the arcuate nucleus directly. (2) BBB crossing — cytokines like IL-6 can cross the intact BBB, and cachexia itself is associated with BBB disruptions that increase permeability. (3) Vagal afferent signaling — peripheral cytokines signal to the nucleus tractus solitarii via the vagus nerve, which relays to the hypothalamus. (4) Vascular activation — cytokines bind to BBB endothelial cells, stimulating production of secondary mediators (PGE2, NO) within the brain. (5) Gut-brain axis — increased gut permeability in cachexia allows LPS into circulation, synergizing with tumor factors to exacerbate hypothalamic inflammation.

**Relevant to:** Source falsification mechanism (the tumor has five independent channels for getting falsified data to the referee — redundancy makes the corruption robust against blocking any single pathway), the Expensive Animal (the brain’s design features that enable rapid metabolic sensing — brain windows, vagal afferents — are the same features that make it vulnerable to false reports), BIO-VAR-ONC-01 (extends: existing card describes what tumors take; this card describes how the falsified reports reach the decision-maker)

**Retrieval prompt:** “What do the sources say about the relative importance of each pathway for delivering tumor signals to the hypothalamus? Is there evidence that blocking one pathway (e.g., vagotomy) shifts the tumor to rely more heavily on others? Which pathway carries the most volume of falsified signaling?”

---

### **BIO-VAR-CXS-02 `[MECHANISM]`**

**Claim:** The brain in cachexia is both reading false reports AND suffering compromised judgment. False reports: members of the IL-6 family (particularly LIF) activate the JAK/STAT signaling pathway — the same pathway leptin uses for satiety signaling. The hypothalamus responds as if the body is in positive energy balance, suppressing appetite even as the patient wastes. This is molecular mimicry: the tumor speaks the same biochemical language as the satiety system, making the signal indistinguishable from genuine data. Compromised judgment: the brain develops ghrelin resistance (failing to respond to elevated hunger signals), CRH feedback failure (hypothalamic CRH remains elevated despite high systemic glucocorticoids, indicating the internal feedback loop is broken), and under the EPIC model, limbic predictions about body state become decoupled from actual visceral signals — the brain may ignore emergency signals to minimize prediction error within its own pathological model.

**Relevant to:** The dual corruption (the referee is simultaneously receiving falsified inputs AND its own judgment has been compromised — this is worse than either alone), LIF/JAK-STAT mimicry (the strongest specific mechanism for source falsification — the tumor literally hijacks the molecular language of a legitimate signaling system), EPIC model corruption (convergent with COMP interoceptive prediction material — the brain accommodates the pathological state as the new expected baseline), existing BIO-VAR-ONC-01 (extends: adds the brain-side corruption that ONC-01 doesn’t cover)

**Retrieval prompt:** “What do the sources say about the LIF/JAK-STAT mimicry mechanism specifically? Include which cytokines activate this pathway, how closely the signaling matches endogenous leptin, and whether blocking JAK/STAT in the hypothalamus reverses cachexia-related appetite suppression. What is the evidence for ghrelin resistance and CRH feedback failure — include the specific hormonal measurements?”

---

### **BIO-VAR-CXS-03 `[MECHANISM] [EVOLUTIONARY]`**

**Claim:** GDF15 and similar tumor-derived factors exploit a legitimate, evolutionarily conserved danger-response system rather than creating a novel signaling channel. GDF15 acts through a specific neuroreceptor (GFRAL) and co-receptor (RET) that are part of a discrete neural circuit modulating the hypothalamic-pituitary neuroendocrine response to both physical and psychosocial stress. The neuroimmune circuit engaged by cachexia cytokines is hypothesized to be adaptive during acute illness — conserving energy by dampening motivation and inducing sickness behavior. The pathology arises from persistent engagement of what should be a transient system. Some factors like Lipocalin-2 (LCN2) bypass standard physiological pathways entirely, directly activating the melanocortin 4 receptor (MC4R) to override normal hunger signals.

**Relevant to:** Wise-to-foolish selfishness transition (acute sickness behavior is wise selfishness — the immune system temporarily overrides appetite for good reasons; tumor hijacking of the same system is foolish selfishness — the signal persists because the tumor maintains it), the Expensive Animal (the organism’s own defense systems become the instruments of its capture), BIO-STR-EMA-02 (convergent — sickness behavior as active motivational program; CXS-03 adds the tumor exploitation of that program)

**Retrieval prompt:** “What do the sources say about the GFRAL/RET receptor system for GDF15? Include the neural circuit it feeds into, the evidence that this system responds to non-tumor stress, and the LCN2/MC4R bypass pathway. Is there evidence that blocking GDF15 signaling reverses cachexia in animal models or clinical trials?”

---

## **INTEROCEPTIVE PREDICTION — THE COMPUTATIONAL BRIDGE**

---

### **COMP-VAR-IPM-01 `[MECHANISM]`**

**Claim:** Under the EPIC (Embodied Predictive Interoception Coding) model, chronically distorted interoceptive inputs cause the brain’s predictive model to accommodate the pathological state as a new expected baseline — an “allostatic state” where the system maintains apparent stability at a pathological operating level. The brain resists updating in the short term by reducing precision-weighting (attention) given to prediction errors that contradict its model, effectively silencing reports of bodily distress. If the distortion persists, the model recalibrates: the drug-addicted brain treats the drugged state as “normal,” the obese brain treats the higher weight as baseline, the cachectic brain accommodates the wasting. The brain’s defensive mechanism against noisy data — reducing precision on unreliable signals — becomes the vulnerability that allows it to ignore genuine distress signals. Agranular visceromotor cortices are architecturally less sensitive to prediction-error signals than sensory cortical regions, meaning the interoceptive prediction system is *built* to be less responsive to bottom-up correction than other cortical systems.

**Relevant to:** Why self-rescue from deep attractors is computationally hard (the brain’s model-updating architecture is biased toward accommodating pathological inputs rather than rejecting them), attractor dynamics (the allostatic state IS the deep attractor — the prediction system maintains it by silencing the signals that would destabilize it), masking (the brain’s ability to suppress prediction errors is the same mechanism that maintains overlearned social performance — the mask persists because the system treats it as expected), V calibration (V is hosted in the predictive model; if the model accommodates corruption, V becomes complicit in maintaining the corrupted state)

**Retrieval prompt:** “What does the EPIC model say about the specific mechanism by which precision-weighting is reduced for interoceptive prediction errors? Include the agranular visceromotor cortex finding, the self-fulfilling prophecy framing, and the distinction between the model resisting update vs. the model accommodating distortion. Is there evidence for a timeline — how quickly does accommodation occur?”

---

### **COMP-VAR-IPM-02 `[MECHANISM]`**

**Claim:** When the body attempts to correct toward health, the brain’s corrupted predictive model interprets the resulting signal change as a deviation from its (pathological) expected state. It responds by issuing “allostatic predictions” that actively drive autonomic and behavioral systems to return the body to the corrupted state. The system further protects itself through salience misattribution: updates from pathological cues (drug triggers, tumor-mimicked satiety signals, adipose endocrine lobbying) are over-weighted, while updates from negative feedback or corrective signals are down-weighted. Even when PFC-mediated error detection is intact, hypoactive executive function may prevent the generation of a corrective behavioral response — the referee detects the discrepancy but lacks the authority to act on it. The failure cascades across three levels: sensory input (noisy or falsified data), update rule (precision-weighting favors the pathological prior), and corrective response (PFC too depleted or uncoupled to override).

**Relevant to:** Why self-correction fails at three levels (not just “the brain doesn’t notice” but a cascade: bad data → biased updating → broken corrective response), salience misattribution (the same mechanism behind wanting/liking dissociation — Robinson’s firewall — operates at the model-update level), the Expensive Animal (the organism actively defends the state that harms it, not through stupidity but through the logic of its own predictive architecture), existing COMP-VAR-AGP series (aging positivity effect — same precision-weighting mechanism operating in a different domain)

**Retrieval prompt:** “What do the sources say about the three failure levels in the predictive model’s self-correction? Include the sensory input degradation evidence, the precision-weighting bias evidence, and the PFC hypoactivity/uncoupling evidence. Is the salience misattribution finding specific to addiction, or has it been demonstrated in obesity and cachexia as well?”

---

## **ROBUST YET FRAGILE — THE GENERAL PRINCIPLE**

---

### **BIO-VAR-RYF-01 `[MECHANISM] [FRAMING MOVE]`**

**Claim:** The brain’s centralized role in metabolic regulation exhibits the “Highly Optimized Tolerance” (HOT) pattern: the same architectural features that make it resilient to common perturbations make it catastrophically vulnerable to rare, specific attacks. The brain windows (MBH, ME) that enable rapid metabolic sensing also allow tumor-derived factors to bypass the BBB. The reward circuitry optimized by evolution to stamp in survival-critical rewards is uniquely vulnerable to concentrated psychostimulants. The homeostatic appetite system is heavily weighted toward defending against energy deficit (evolutionarily common), making it asymmetrically fragile to chronic caloric surplus (historically rare). The neuroimmune circuit adaptive during acute illness becomes pathological under persistent tumor engagement. In each case, robustness to one class of metabolic challenge (acute starvation, short-term infection, natural reinforcers) comes at the cost of fragility to another class (chronic surplus, slow-growing tumors, concentrated drugs).

**Relevant to:** The general principle underlying all three corruption mechanisms (input degradation, internal co-optation, source falsification are all exploitations of design features that are normally adaptive), the Expensive Animal (the brain isn’t poorly designed — it’s optimally designed for ancestral conditions and therefore fragile to novel ones), Bennett bet (centralized regulation via general-purpose circuitry creates a single point of failure that modular systems would avoid — but the efficiency gains of centralization are what made complex cognition possible), why personality entrenchment is structurally predicted (any centralized evaluation system with the architecture described here WILL be vulnerable to capture by its largest clients)

**Retrieval prompt:** “What do the sources say about the HOT (Highly Optimized Tolerance) pattern in biological regulation? Include the specific examples of robustness/fragility trade-offs across the three corruption domains. Is there a formal systems-theory source for the HOT concept, or is it described informally?”

---

## **CONVERGENT CITATION NOTES (for existing cards)**

---

### **Note for BIO-NOR-TBB-01/02 (wanting/liking dissociation)**

**Add convergent source:** Robinson (2025) 30-year update to incentive-sensitization theory. Robinson is the original source; Nord extended. Robinson’s 2025 update adds: non-drug evidence (salt appetite, shock rod, gambling, punding, binge eating), the 90%/10% NAc wanting/liking ratio, and the “firewall” concept between motivation and cached hedonic values. The firewall is architecturally important for HPAM — it explains why entrenched patterns resist re-evaluation even when the organism cognitively “knows” the pursuit isn’t rewarding.

---

### **Note for BIO-NOR-TBB-04 (attractor states / prediction error gating)**

**Add convergent mechanism:** The EPIC model’s precision-weighting failure (COMP-VAR-IPM-01) provides the computational mechanism underneath Nord’s attractor-state gating. Nord describes the phenomenon (positive errors discounted, negative errors amplified). The EPIC model describes the mechanism (agranular visceromotor cortices are architecturally less sensitive to prediction error, and the brain actively reduces precision on signals that contradict its model). Together they explain why attractor states resist disruption at both the neural and computational levels.

---

### **Note for BIO-VAR-ONC-01 (tumor hijacking)**

**Add referee-corruption framing:** Existing card describes what tumors take (Warburg, VEGF, cachexia). BIO-VAR-CXS-01/02/03 now document how falsified reports reach the referee and corrupt its judgment. The existing card is the resource-theft story. The new cards are the regulatory-capture story. Both are needed — theft describes the cost, capture describes why the cost persists.

---

### **Note for BIO-VAR-ONC-02 (adipose hijacking)**

**Add leptin resistance mechanism:** Existing card describes adipose endocrine lobbying and hypoxia-inflammation cycle. BIO-VAR-LPR-01/02/03 now document the specific molecular sequence by which the lobbying works: SOCS3/PTP1B upregulation → receptor deafening → ER stress bridge → self-sustaining loop → defense of corrupted set point. The existing card is the strategy. The new cards are the mechanism.

---

### **Note for BIO-STR-EMA-01 (wise/foolish selfishness)**

**Add temporal specificity:** BIO-VAR-LPR-02 shows the wise-to-foolish transition begins before the subsystem has fully expanded — hypothalamic inflammation at day 1, SOCS3 at week 1, obesity later. This sharpens the existing card: the transition isn’t gradual and proportional to subsystem growth. The deafening starts almost immediately.

---

### **Note for BC-08 (The Brain’s Conflict of Interest)**

**Add three corruption mechanisms:** BC-08 establishes the structural conflict (brain is both referee and biggest spender). The new extraction documents three specific mechanisms by which entrenched subsystems exploit this conflict: input degradation (leptin resistance), internal co-optation (dopaminergic hijacking), and source falsification (cachexia signaling). BC-08 is the setup. The three corruption mechanisms are the payoff.

