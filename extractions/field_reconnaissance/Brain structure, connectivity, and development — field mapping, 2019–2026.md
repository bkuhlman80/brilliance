# **Brain structure, connectivity, and development — field mapping, 2019–2026**

**The field is in a phase transition.** Three capabilities that did not exist five years ago — whole-brain connectomics at synapse resolution, single-cell transcriptomic atlases of the entire human brain, and spatial transcriptomics preserving tissue architecture — have converged between 2023 and 2025, generating a cascade of discoveries that force revision of textbook neuroscience. The most consequential cluster is the October 2023 BICCN *Science* special issue (\>3,000 human brain cell types catalogued), the October 2024 FlyWire papers (first complete adult brain connectome), and the April 2025 MICrONS papers (largest mammalian functional connectome). Below each sub-area, individual differences in brain wiring remain the critical unsolved problem: synapse-level connectomics operates at n=1, population-level imaging genetics operates at millimeter resolution, and nothing yet bridges these scales.

This report covers **31 papers across 9 sub-areas**, with verified DOIs, design metadata, and analytical commentary on each.

---

## **1\. Connectomics is delivering wiring rules, not yet individual differences**

The field's flagship datasets — the complete *Drosophila* brain (FlyWire), the 1 mm³ mouse visual cortex (MICrONS), and the 1 mm³ human temporal cortex fragment (Shapson-Coe et al.) — are all **single-specimen reconstructions**. They reveal species-typical organizational principles with extraordinary precision but structurally cannot address inter-individual wiring variation. The Human Connectome Project (n≈1,200) does reveal heritable individual differences in macroscale functional connectivity, but operates at millimeter resolution. **No empirical paper bridges synapse-level connectomics with population-level variation.** This is the field's next grand challenge.

### **Paper 1.1 — First graph-theoretic characterization of a complete brain**

**Lin A, Yang R, Dorkenwald S, Matsliah A, Sterling AR, Schlegel P, et al.** Network statistics of the whole-brain connectome of *Drosophila*. *Nature* 634, 153–165 (2024). DOI: [10.1038/s41586-024-07968-y](https://doi.org/10.1038/s41586-024-07968-y) ✅ Verified

* **Design:** Computational analysis of complete connectome (single-specimen whole-brain EM reconstruction)  
* **Sample:** N=1 brain; 139,255 neurons, 54.5 million synapses. No genetic data; neurotransmitter predictions included.  
* **What's new:** The fly brain exhibits rich-club organization with \~30% of neurons participating — strikingly high compared to mammalian mesoscale estimates (\<15%). Two- and three-node circuit motif prevalence depends on neurotransmitter identity, meaning the wiring diagram alone misses essential circuit logic.  
* **Why it matters:** First complete graph-theoretic characterization of any adult brain at synapse resolution; establishes the template against which all future connectomes (zebrafish, mouse) will be analyzed.

The finding that motif strength is non-random with respect to excitation/inhibition is a genuine advance — it reveals that connectomics without transmitter labels misses an essential organizational layer. The **30% rich-club participation rate** raises the question of whether mammalian estimates are underestimates due to resolution limits or whether invertebrate brains are genuinely more interconnected proportionally.

### **Paper 1.2 — "Like-to-like" as a universal cortical wiring rule**

**Ding Z, Fahey PG, Papadopoulos S, Wang EY, Celii B, et al.** Functional connectomics reveals general wiring rule in mouse visual cortex. *Nature* 640, 459–469 (2025). DOI: [10.1038/s41586-025-08840-3](https://doi.org/10.1038/s41586-025-08840-3) ✅ Verified

* **Design:** Computational analysis of combined functional imaging \+ EM connectome (MICrONS dataset)  
* **Sample:** N=1 mouse; \~75,000 neurons functionally imaged, co-registered with EM reconstruction of \>200,000 cells and 0.5 billion synapses. No genetic data.  
* **What's new:** "Like-to-like" connectivity — neurons with similar visual response properties preferentially forming synapses — is a universal rule operating across all cortical layers and across brain areas, including feedback connections.  
* **Why it matters:** Transforms "like-to-like" from a local curiosity (previously shown only in layer 2/3 of V1) into a candidate universal wiring law, validated with a digital twin model.

The finding that feedback connections follow the same rule as feedforward is **genuinely surprising**, because feedback has long been theorized to carry top-down prediction signals that would not necessarily follow bottom-up tuning. Feature similarity, not just retinotopic proximity, drives connectivity. Limitation: n=1 mouse, one cortical area family.

### **Paper 1.3 — Inhibitory "motif groups" overturn the blanket-inhibition model**

**Schneider-Mizell CM, Bodor AL, Brittain D, Buchanan J, et al.** Inhibitory specificity from a connectomic census of mouse visual cortex. *Nature* 640, 448–458 (2025). DOI: [10.1038/s41586-024-07780-8](https://doi.org/10.1038/s41586-024-07780-8) ✅ Verified

* **Design:** Computational analysis of complete inhibitory wiring from EM connectome (MICrONS dataset)  
* **Sample:** N=1 mouse; 1,352 densely segmented neurons, \>70,000 inhibitory synapses. Transcriptomic cell-type correspondence via Patch-seq.  
* **What's new:** Cortical inhibition is organized into "motif groups" — diverse sets of inhibitory neurons that collectively target both perisomatic and dendritic compartments of the same excitatory subpopulation — plus a class of disinhibitory specialist interneurons selectively targeting basket cells.  
* **Why it matters:** Overturns the textbook view of cortical inhibition as a spatially diffuse "blanket" and replaces it with a precise, cell-type-specific targeting architecture.

The **motif group concept** — coordination of diverse interneuron types to simultaneously modulate output-gating (perisomatic) and input-gating (dendritic) of the same excitatory population — was essentially invisible to previous methods. Classical anatomical categories remain useful at connectomic scale, but the data reveal substantial within-class heterogeneity.

---

## **2\. Cell-type discoveries rewrite the human brain's parts list**

The October 2023 *Science* special issue from the BRAIN Initiative Cell Census Network (BICCN) represents the single most consequential publication event in this space. Four papers form a complementary set: whole-brain reference (Siletti), spatial context for cortical areas (Jorstad/Close), evolutionary context (Jorstad/Song), and population-level variation (Johansen). Together they establish that the adult human brain contains **\>3,000 transcriptomically distinct cell types**, organized into \~24 conserved cortical subclasses with area-specific proportional variation.

### **Paper 2.1 — \>3,000 cell types across the whole human brain**

**Siletti K, Hodge R, Mossi Albiach A, Lee KW, et al.** Transcriptomic diversity of cell types across the adult human brain. *Science* 382(6667), eadd7046 (2023). DOI: [10.1126/science.add7046](https://doi.org/10.1126/science.add7046) ✅ Verified

* **Design:** Large-scale snRNA-seq atlas with RNAScope validation  
* **Sample:** 3 postmortem donors; \>3 million nuclei from \~100 dissections spanning forebrain, midbrain, hindbrain. No genetic data.  
* **What's new:** Identifies 461 clusters organized into 30 superclusters and 3,313 subclusters — far greater cellular diversity than previously appreciated, particularly in non-cortical regions.  
* **Why it matters:** The foundational reference atlas for all subsequent human brain cell-type research, analogous to what the Human Genome Project was for genomics.

Three discoveries force revision of classical understanding: (1) **"Splatter neurons"** — a novel, broadly distributed supercluster with no clear classical counterpart; (2) midbrain and hindbrain neurons showed unexpectedly high diversity defined by combinatorial neuropeptide expression, far exceeding cortical diversity; (3) astrocytes and OPCs split along telencephalic/non-telencephalic divides, challenging the view of glial populations as homogeneous.

### **Paper 2.2 — Molecular basis for Brodmann-style area distinctions**

**Jorstad NL, Close J, Johansen N, et al.** Transcriptomic cytoarchitecture reveals principles of human neocortex organization. *Science* 382(6667), eadf6812 (2023). DOI: [10.1126/science.adf6812](https://doi.org/10.1126/science.adf6812) ✅ Verified

* **Design:** Multi-area snRNA-seq \+ MERFISH spatial transcriptomics across 8 cortical areas  
* **Sample:** \>1.1 million nuclei via snRNA-seq; MERFISH spatial validation. \~3–7 postmortem donors.  
* **What's new:** Creates the first molecularly defined, spatially resolved cytoarchitectonic map — showing 24 shared cell subclasses with systematically varying proportions, providing a transcriptomic basis for classical area distinctions.  
* **Why it matters:** Bridges classical neuroanatomy (Brodmann) with molecular cell typing, proving cortical area differences reflect quantitative variation in shared types rather than distinct cell populations.

V1 emerged as strikingly distinct: **dramatically altered excitatory:inhibitory ratio**, expanded L4 IT population, and specialized LAMP5 LHX6 inhibitory neurons with atypical laminar distribution. Even glial cells showed area-specific organization — a finding that challenges the notion that glial heterogeneity is merely a response to local neuronal milieu.

### **Paper 2.3 — What makes the human cortex molecularly distinct**

**Jorstad NL, Song JHT, Exposito-Alonso D, et al.** Comparative transcriptomics reveals human-specific cortical features. *Science* 382(6667), eade9516 (2023). DOI: [10.1126/science.ade9516](https://doi.org/10.1126/science.ade9516) ✅ Verified

* **Design:** Comparative snRNA-seq of middle temporal gyrus across 5 primate species (human, chimpanzee, gorilla, rhesus macaque, marmoset) with spatial validation  
* **Sample:** \>570,000 nuclei total across 5 species; multiple individuals per species.  
* **What's new:** Glial gene expression has diverged faster than neuronal expression across species; neuronal expression has diverged faster on the human lineage than any other; only a few hundred human-specific differentially expressed genes define human cortical distinctiveness — enriched near human accelerated regions (HARs).  
* **Why it matters:** First single-cell-resolution molecular answer to "what makes the human cortex different" — and the answer is surprisingly minimal at the cellular level: **regulatory evolution, not structural protein changes**.

The paradox of minimal cellular novelty is provocative: great apes share highly similar cell-type composition. The finding that **microglia and astrocytes showed more-divergent expression across species than neurons** aligns with glial regional specialization findings and raises questions about whether glial evolution has been an underappreciated driver of human cognitive specialization.

### **Paper 2.4 — Population-level cell-type variation in the human brain**

**Johansen N, Somasundaram S, Travaglini KJ, et al.** Interindividual variation in human cortical cell type abundance and expression. *Science* 382(6667), eadf2359 (2023). DOI: [10.1126/science.adf2359](https://doi.org/10.1126/science.adf2359) ✅ Verified

* **Design:** Large-cohort snRNA-seq with whole-genome sequencing (WGS) and eQTL analysis  
* **Sample:** 75 neurosurgical donors; \~400,000 nuclei; 125 cell types. **Genetic data: Yes** (paired WGS).  
* **What's new:** Cellular composition is remarkably conserved across individuals, but substantial interindividual variation exists in cell-type abundances and gene expression — particularly in **deep-layer glutamatergic neurons and microglia** — with genomic variants significantly associated with cell-type-specific expression.  
* **Why it matters:** Establishes the population-level baseline for distinguishing disease-associated changes from normal human variation, essential for interpreting GWAS signals at cell-type resolution.

That deep-layer excitatory neurons and microglia harbor the most interindividual variation converges with Jorstad/Song's finding that these populations show the fastest evolutionary divergence — suggesting the most evolutionarily dynamic cell populations are also the most variable within the human population. Age, sex, ancestry, and disease state explained only a minority of observed variance, leaving a large fraction unexplained.

---

## **3\. Revised structural anatomy concentrates in meningeal and molecular domains**

This sub-area is modestly productive but genuinely active. The strongest contributions come from meningeal/perivascular anatomy (genuinely novel structural discoveries), cytoarchitectonic atlas revision (systematic replacement of Brodmann), and receptor architectonics (molecular-level cortical organization as a new axis). **Thalamic parcellation** has seen primarily higher-resolution confirmations, not new subdivisions. **New white matter tracts** meeting the "forces revision" threshold are largely absent post-2019.

### **Paper 3.1 — Julich-Brain replaces Brodmann with 248+ probabilistic areas**

**Amunts K, Mohlberg H, Bludau S, Zilles K.** Julich-Brain: A 3D probabilistic atlas of the human brain's cytoarchitecture. *Science* 369(6506), 988–992 (2020). DOI: [10.1126/science.abb4588](https://doi.org/10.1126/science.abb4588) ✅ Verified

* **Design:** Large-scale observer-independent cytoarchitectonic mapping with 3D probabilistic registration  
* **Sample:** 10 postmortem brains (\~7,000+ histological sections each). No genetic data.  
* **What's new:** First whole-brain 3D probabilistic cytoarchitectonic atlas with \~248 areas — substantially exceeding and revising Brodmann's 43-area map with statistically validated borders.  
* **Why it matters:** Replaces the century-old Brodmann map as the standard reference and accounts for interindividual variability through probabilistic mapping — something missing from all prior maps.

Many classical Brodmann areas (e.g., BA19, BA39) are formally demonstrated to be heterogeneous composites of multiple distinct areas. The atlas is dynamically expanding; e.g., Bludau et al. (2022) added four previously unrecognized parahippocampal areas. Julich-Brain functions as a **living revision of neuroanatomy** via the EBRAINS infrastructure.

### **Paper 3.2 — Receptor architecture as an independent axis of cortical organization**

**Froudist-Walsh S, Xu T, Niu M, Rapan L, et al.** Gradients of neurotransmitter receptor expression in the macaque cortex. *Nature Neuroscience* 26(7), 1281–1294 (2023). DOI: [10.1038/s41593-023-01351-2](https://doi.org/10.1038/s41593-023-01351-2) ✅ Verified

* **Design:** Quantitative receptor autoradiography (14 receptor types, 109 areas) integrated with connectivity, gene expression, and fMRI  
* **Sample:** Macaque cortex (postmortem tissue). Integrated with Allen Brain Atlas transcriptomic data. No genetic association data.  
* **What's new:** A principal gradient of receptor density per neuron aligns with cortical hierarchy (sensory→association); a second gradient driven by **serotonin 5-HT₁A receptors** distinguishes anterior cingulate/default mode/salience networks.  
* **Why it matters:** Demonstrates that the molecular architecture of the cortex is a systematic organizational principle independent of cytoarchitecture — the "traffic light map" of cortical organization necessary to move beyond purely connectomic models.

This is a capstone from the Zilles/Palomero-Gallagher receptor architectonics program. The discovery that a single principal component captures cortical hierarchy at the receptor level is a genuine conceptual advance — it means any complete parcellation model must incorporate molecular identity alongside structural and connectivity measures.

### **Paper 3.3 — Discovery of arachnoid cuff exit points connecting dura to brain**

**Smyth LCD, Xu D, Okar SV, Dykstra T, Rustenhoven J, et al.** Identification of direct connections between the dura and the brain. *Nature* 627(8002), 165–173 (2024). DOI: [10.1038/s41586-023-06993-7](https://doi.org/10.1038/s41586-023-06993-7) ✅ Verified

* **Design:** Multimodal discovery study: snRNA-seq, transgenic mouse models, two-photon imaging, EM, fluorescent tracers, human contrast-enhanced MRI  
* **Sample:** Mouse (multiple transgenic lines) \+ human (gadolinium-enhanced MRI). No genome-wide genetic data.  
* **What's new:** Discovery of "arachnoid cuff exit (ACE) points" — previously unknown openings in the arachnoid barrier at bridging veins that permit CSF drainage, molecular exchange, and immune cell trafficking between subarachnoid space and dura mater.  
* **Why it matters:** Overturns the textbook model of the arachnoid barrier as sealed, revealing a structural route for brain waste clearance and immune surveillance with direct implications for neurodegeneration.

This is the cleanest "forces revision" paper in the set: it identifies a previously unknown structural feature, characterizes it molecularly, demonstrates function in vivo, and confirms existence in humans with MRI. ACE points provide a concrete anatomical mechanism for how CSF exits the subarachnoid space to reach dural lymphatic vessels — a question the field had struggled to explain since the meningeal lymphatics rediscovery (Louveau et al. 2015).

### **Paper 3.4 — The SLYM controversy: a proposed fourth meningeal membrane**

**Møllgård K, Beinlich FRM, Kusk P, et al.** A mesothelium divides the subarachnoid space into functional compartments. *Science* 379(6627), 84–88 (2023). DOI: [10.1126/science.adc8810](https://doi.org/10.1126/science.adc8810) ✅ Verified

* **Design:** Discovery study: Prox1-eGFP transgenic mice, two-photon imaging, immunohistochemistry, human postmortem confirmation  
* **Sample:** Multiple transgenic mouse lines; human postmortem tissue. No genetic data.  
* **What's new:** Claims the existence of a fourth meningeal layer — the subarachnoid lymphatic-like membrane (SLYM) — that compartmentalizes the subarachnoid space and hosts myeloid immune cells.  
* **Why it matters:** If validated, SLYM would be the first new meningeal layer added to textbooks in centuries.

⚠️ **This paper is highly controversial.** Multiple groups (Siegenthaler, Betsholtz) challenged the findings, arguing SLYM is the inner sublayer of the arachnoid, not a separate membrane (Pietilä et al., *Neuron*, 2023; Mapunda et al., *Nat Commun*, 2023). The Nedergaard/Møllgård group published rebuttals. **The field has not reached consensus.** Included because it represents a genuine attempt at anatomical revision in a top-tier journal, but readers should evaluate critically.

---

## **4\. Developmental neurobiology enters the spatial multi-omic era**

This sub-area has seen transformative progress driven by spatial transcriptomics and multi-omic profiling of developing human tissue. The picture that emerges: cortical area identity is established far earlier than classical histology suggested, an **epigenetic barrier** governs the protracted timeline of human neuronal maturation, and a previously unknown tripotential progenitor challenges the textbook separation of neuronal and glial lineages.

### **Paper 4.1 — Laminar identity visible months before cytoarchitectural layers form**

**Qian X, Coleman K, Jiang S, et al.** Spatial transcriptomics reveals human cortical layer and area specification. *Nature* 644, 153–163 (2025). DOI: [10.1038/s41586-025-09010-1](https://doi.org/10.1038/s41586-025-09010-1) ✅ Verified

* **Design:** Cross-sectional spatial transcriptomics (MERFISH) on postmortem human fetal brain  
* **Sample:** \>18 million cells across 8 cortical areas and 7 developmental time points (GW 16–21+). No genetic data.  
* **What's new:** Six-layer laminar structure is molecularly identifiable \~3 months before classical cytoarchitectural layers emerge, and cortical area specification proceeds via two modes — continuous gradients across most areas but a **discrete, sharp binary boundary between V1 and V2** as early as GW 20\.  
* **Why it matters:** Overturns the assumption that mid-gestation arealization involves only gradient-like transitions, suggesting at least some boundaries emerge through discrete transcriptional switches.

The V1–V2 sharp boundary finding directly challenges the dominant "protomap" model of purely graded areal specification. Early upregulation of synaptogenesis programs in V1-specific layer 4 neurons hints at area-specific developmental timing differences that connect to the broader literature on heterochronic maturation (including Xie et al. 2023).

### **Paper 4.2 — An epigenetic clock explains why human neurons mature so slowly**

**Ciceri G, Baggiolini A, Cho HS, et al.** An epigenetic barrier sets the timing of human neuronal maturation. *Nature* 626, 881–890 (2024). DOI: [10.1038/s41586-023-06984-8](https://doi.org/10.1038/s41586-023-06984-8) ✅ Verified

* **Design:** Experimental in vitro (hPSC-derived cortical neurons): scRNA-seq, ATAC-seq, CUT\&Tag, electrophysiology, loss-of-function experiments  
* **Sample:** Multiple hPSC lines; time-course across months of maturation. No population genetic data.  
* **What's new:** Identifies histone methyltransferases **EZH2, EHMT1/EHMT2, and DOT1L** as an epigenetic barrier that holds maturation programs in a "poised" state; this clock is set before neurogenesis and gradually released post-mitotically.  
* **Why it matters:** First concrete molecular mechanism explaining why human neurons take months to years to mature vs. days in mouse — a fundamental question with implications for understanding neoteny, critical periods, and neurodevelopmental disorder vulnerability windows.

The conceptual shift: the maturation clock is **set at the progenitor stage**, not intrinsic to the post-mitotic neuron itself. This directly complements Xie et al. 2023's findings on protracted PFC development — region-specific differences in epigenetic barrier strength could explain why PFC neurons mature more slowly than sensory cortex neurons. The potential to pharmacologically manipulate maturation timing has major implications for stem cell therapy.

### **Paper 4.3 — The most comprehensive developmental atlas: prenatal through adulthood**

**Velmeshev D, Perez Y, Yan Z, et al.** Single-cell analysis of prenatal and postnatal human cortical development. *Science* 382(6667), eadf0834 (2023). DOI: [10.1126/science.adf0834](https://doi.org/10.1126/science.adf0834) ✅ Verified

* **Design:** Cross-sectional snRNA-seq \+ snATAC-seq atlas spanning second trimester through adulthood  
* **Sample:** \>700,000 nuclei from 169 samples, 106 donors. Intersected with GWAS data for schizophrenia, ASD, MDD, bipolar. **Genetic data: Yes** (GWAS integration).  
* **What's new:** Captures the full molecular progression of cortical lineages across the entire human developmental arc, revealing burst transcriptional events and **female-enriched lineage programs disproportionately enriched for autism risk factors**.  
* **Why it matters:** Most comprehensive single-cell developmental atlas in temporal span (106 donors, prenatal through adult), with chromatin accessibility data directly linked to disease genetics.

The female-enriched programs with autism risk enrichment provide a molecular basis for the long-observed male-to-female ASD ratio. Different maturation rates across excitatory neuron subtypes — upper-layer neurons maturing most slowly — complement both Xie et al. 2023 and Ciceri et al. 2024\.

### **Paper 4.4 — Tripotential progenitors challenge the textbook lineage model**

**Wang L, Wang C, Moriano JA, et al.** Molecular and cellular dynamics of the developing human neocortex. *Nature* 647, 169–178 (2025). DOI: [10.1038/s41586-024-08351-7](https://doi.org/10.1038/s41586-024-08351-7) ✅ Verified

* **Design:** Multi-omic atlas (paired snATAC-seq \+ snRNA-seq, spatial transcriptomics, lineage tracing) of human neocortex, first trimester through adolescence  
* **Sample:** 232,328 nuclei from 27 specimens; integrated with GWAS data for ASD and schizophrenia. **Genetic data: Yes.**  
* **What's new:** Identifies a previously unknown **tripotential intermediate progenitor cell (Tri-IPC)** that locally generates GABAergic interneurons, OPCs, and astrocytes — resolving the neurogenesis-to-gliogenesis transition and finding that glioblastoma cells transcriptomically resemble Tri-IPCs.  
* **Why it matters:** Fundamentally revises the canonical model of separate progenitor pools for neurons and glia, with immediate implications for both developmental biology and neuro-oncology.

The Tri-IPC discovery challenges the textbook view that cortical GABAergic interneurons are exclusively of ventral origin. The glioblastoma connection — cancer cells resembling developmental Tri-IPCs — is a translational bridge. PFC vs. V1 comparisons across development provide the regulatory architecture underlying regional timing differences.

---

## **5\. Adolescent development gains a unifying axis and loses a simple narrative**

The "adolescent pruning" story is getting substantially more complex. Four findings reshape the picture: development proceeds along a hierarchical sensorimotor-to-association axis governed by myelination (Sydnor), cortical thinning reflects oligodendrocyte maturation more than synaptic pruning (Genc), adolescence involves active compartment-specific **spine creation** alongside pruning (Egashira), and the molecular machinery of pruning (IGSF11) connects to transdiagnostic psychiatric risk (Xie).

### **Paper 5.1 — The S-A axis as a unifying developmental framework**

**Sydnor VJ, Larsen B, Seidlitz J, et al.** Intrinsic activity development unfolds along a sensorimotor–association cortical axis in youth. *Nature Neuroscience* 26(4), 638–649 (2023). DOI: [10.1038/s41593-023-01282-y](https://doi.org/10.1038/s41593-023-01282-y) ✅ Verified

* **Design:** Large cross-sectional developmental neuroimaging (resting-state fMRI \+ T1w/T2w myelin mapping)  
* **Sample:** n=1,033 youths aged 8–23 (Philadelphia Neurodevelopmental Cohort). **Genetic data: No**, but integrates Allen Human Brain Atlas gene expression.  
* **What's new:** Refinement of intrinsic cortical activity proceeds heterochronously along a hierarchical **sensorimotor-to-association (S-A) axis**, with activity amplitude declines coupled to intracortical myelin maturation, and environmental influences structured by this same axis.  
* **Why it matters:** First unified evidence that a single hierarchical axis governs spatiotemporal patterning of functional maturation, myelination, and environmental sensitivity during adolescence.

The coupling between intrinsic activity declines and myelin maturation suggests **myelination actively constrains plasticity** — not merely a passive structural event. Environmental effects maximally structured along the S-A axis during adolescence demonstrate that late-maturing association cortices represent a window of both vulnerability and opportunity.

### **Paper 5.2 — Cortical thinning is myelination, not just pruning**

**Genc S, Ball G, Chamberland M, et al.** MRI signatures of cortical microstructure in human development align with oligodendrocyte cell-type expression. *Nature Communications* 16, 3317 (2025). DOI: [10.1038/s41467-025-58604-w](https://doi.org/10.1038/s41467-025-58604-w) ✅ Verified

* **Design:** Cross-sectional developmental ultra-strong gradient diffusion MRI (300 mT/m Connectom scanner) \+ biophysical modeling \+ transcriptomic alignment  
* **Sample:** \~50–100 participants (constrained by scanner rarity). **Genetic data: No**, but integrates PsychENCODE and Allen Human Brain Atlas.  
* **What's new:** Developmental increases in cortical neurite density and soma radius reductions align specifically with **oligodendrocyte — not astrocyte** — gene expression patterns, supporting intracortical myelination as the dominant driver of observed cortical thinning.  
* **Why it matters:** Decomposes what "cortical thinning" actually means at the cellular level, changing interpretation of decades of volumetric MRI findings.

By applying SANDI biophysical models to ultra-strong gradient data, the authors disentangle neurite from soma contributions. Cross-reference with PsychENCODE shows an oligodendrocyte-to-astrocyte expression ratio shift around age 20 in sensorimotor cortex (later in association cortex) — directly supporting the S-A axis model.

### **Paper 5.3 — Adolescent spine hotspots challenge the pruning-only model**

**Egashira R, Ke M-T, Nakagawa-Tamagawa N, et al.** Dendritic compartment-specific spine formation in layer 5 neurons underlies cortical circuit maturation during adolescence. *Science Advances* 12(3), eadw8458 (2026). DOI: [10.1126/sciadv.adw8458](https://doi.org/10.1126/sciadv.adw8458) ✅ Verified

* **Design:** Mouse super-resolution imaging \+ schizophrenia-associated gene knockouts (Setd1a, Hivep2, Grin1)  
* **Sample:** Small n (labor-intensive super-resolution spine mapping). **Genetic data: Yes** (schizophrenia gene manipulation).  
* **What's new:** The adolescent brain simultaneously creates high-density **"hotspots" of dendritic spines** in specific compartments of Layer 5 extratelencephalic-projecting neuron apical dendrites — and schizophrenia-associated mutations selectively impair this spine *formation*, not pruning.  
* **Why it matters:** Directly challenges the decades-old "adolescent synaptic pruning" hypothesis by demonstrating that adolescence involves compartment-specific construction alongside elimination.

**Paradigm-shifting** for developmental neuroscience. The hotspots localize to the calcium spike initiation zone of L5 ET neurons — a cellular substrate for top-down computations emerging during adolescence. Schizophrenia gene mutations (Setd1a, Hivep2, Grin1) selectively impaired adolescent formation while leaving early postnatal development intact, pointing to an adolescence-specific vulnerability window. Mouse study; translation to primates remains open but L5 ET circuitry is conserved.

### **Paper 5.4 — IGSF11 connects pruning machinery to transdiagnostic psychiatric risk**

**Xie C, Xiang S, Shen C, et al.** A shared neural basis underlying psychiatric comorbidity. *Nature Medicine* 29, 1232–1242 (2023). DOI: [10.1038/s41591-023-02317-4](https://doi.org/10.1038/s41591-023-02317-4) ✅ Verified

* **Design:** Multi-cohort cross-sectional neuroimaging \+ genetic analysis \+ replication  
* **Sample:** Discovery: IMAGEN (\~2,000 adolescents, longitudinal imaging \+ GWAS). Replication: ABCD (n=1,799). **Genetic data: Yes.**  
* **What's new:** Identifies a transdiagnostic "neuropsychopathological factor" — disrupted frontal connectivity genetically anchored to **IGSF11**, a gene directly implicated in synaptic pruning.  
* **Why it matters:** First human imaging-genetics bridge between pruning biology and transdiagnostic risk, connecting molecular machinery to a measurable brain phenotype predicting psychiatric comorbidity.

The frontal concentration aligns with late PFC maturation. Effect sizes are small, typical of psychiatric genetics. Pairs with Egashira et al. — one identifies genetic risk at the population level, the other reveals the cellular mechanism that may be disrupted.

---

## **6\. Glia emerge as active circuit participants, not passive support**

All three major glial types now have causal evidence for roles in information processing — oligodendrocytes as plasticity gatekeepers, astrocytes as ensemble-forming circuit participants, and microglia as bidirectional synapse regulators. This represents a fundamental expansion of the cellular basis of cognition beyond neurons alone.

### **Paper 6.1 — Myelination actively closes critical periods**

**Xin W, Kaneko M, Roth RH, et al.** Oligodendrocytes and myelin limit neuronal plasticity in visual cortex. *Nature* 633(8031), 856–863 (2024). DOI: [10.1038/s41586-024-07853-8](https://doi.org/10.1038/s41586-024-07853-8) ✅ Verified

* **Design:** Genetic loss-of-function (conditional Myrf deletion from OPCs during adolescence) \+ in vivo imaging \+ monocular deprivation  
* **Sample:** Mice, 4–8+ per condition. No human genetic data.  
* **What's new:** Blocking oligodendrocyte differentiation during adolescence keeps adult visual cortex in a juvenile-like state of heightened plasticity — enhanced monocular deprivation response, elevated spine turnover, reduced inhibitory transmission.  
* **Why it matters:** Most direct evidence that **myelination actively constrains circuit plasticity**, reframing oligodendrocytes as developmental gatekeepers that close critical periods.

Dissociates oligodendrocyte function from mere conduction velocity: myelin loss affects dendritic spine dynamics and inhibitory circuit maturation. Profound implications for understanding why disorders of myelination timing produce lasting circuit consequences. Links directly to Sydnor et al.'s S-A axis framework and Genc et al.'s cortical thinning findings.

### **Paper 6.2 — Astrocytes form task-specific ensembles that drive behavior**

**Serra I, Martín-Monteagudo C, Sánchez Romero J, et al.** Astrocyte ensembles manipulated with AstroLight tune cue-motivated behavior. *Nature Neuroscience* 28(3), 616–626 (2025). DOI: [10.1038/s41593-025-01870-0](https://doi.org/10.1038/s41593-025-01870-0) ✅ Verified

* **Design:** Novel tool development (AstroLight: light \+ Ca²⁺-dependent gene expression) \+ fiber photometry \+ optogenetic/chemogenetic manipulation \+ operant conditioning  
* **Sample:** Mice, \~6–12 animals per condition. No genetic data.  
* **What's new:** Astrocytes in the nucleus accumbens form **functionally specialized ensembles** recruited during cue-reward learning; manipulation of tagged ensembles is sufficient to bias reward-seeking behavior.  
* **Why it matters:** First demonstration that astrocytes organize into task-specific functional ensembles causally contributing to motivated decision-making — demolishing the assumption of astrocyte functional homogeneity.

AstroLight is itself a significant methodological advance: it translates Ca²⁺ signals into gene expression, enabling activity-dependent labeling analogous to c-Fos tagging for neurons. The finding that reactivation biases port choice suggests astrocyte ensembles carry information about specific reward contingencies. A companion 2025 paper (Williamson et al.) demonstrated similar principles in hippocampal fear conditioning, suggesting this is a **general organizational principle**.

### **Paper 6.3 — Microglia drive forgetting through complement-dependent synapse elimination**

**Wang C, Yue H, Hu Z, et al.** Microglia mediate forgetting via complement-dependent synaptic elimination. *Science* 367(6478), 688–694 (2020). DOI: [10.1126/science.aaz2288](https://doi.org/10.1126/science.aaz2288) ✅ Verified

* **Design:** Microglial depletion, complement manipulation, engram-cell-specific interventions, contextual fear conditioning  
* **Sample:** Mice (multiple lines), 4–5+ per condition. No genetic data.  
* **What's new:** Microglia actively engulf synaptic components between memory engram cells in a **complement (C1q)-dependent** manner, and this process is necessary for natural forgetting of remote memories.  
* **Why it matters:** Reconceptualizes forgetting as an active, microglia-driven biological process — the same complement-dependent machinery used during development is repurposed throughout life.

The CD55 expression experiment is particularly powerful: expressing complement inhibitor specifically in engram cells prevents forgetting, demonstrating synapse specificity. Reframes individual differences in forgetting rates as potentially reflecting variation in microglial activity or complement signaling.

### **Paper 6.4 — Microglia promote plasticity by clearing extracellular matrix**

**Nguyen PT, Dorman LC, Pan S, et al.** Microglial remodeling of the extracellular matrix promotes synapse plasticity. *Cell* 182(2), 388–403 (2020). DOI: [10.1016/j.cell.2020.05.050](https://doi.org/10.1016/j.cell.2020.05.050) ✅ Verified

* **Design:** Conditional deletion of IL-33 and its receptor, dendritic spine imaging, fear conditioning, enriched environment, IL-33 gain-of-function in aged mice  
* **Sample:** Mice (conditional knockout lines, young and aged). No human genetic data.  
* **What's new:** Neurons express IL-33 in an experience-dependent manner, signaling microglia to phagocytose **extracellular matrix proteins** surrounding synapses; this pathway is required for spine plasticity and declines with aging.  
* **Why it matters:** Reveals that microglia promote (not just eliminate) synaptic connections by clearing the physical ECM barrier — providing a non-neuronal explanation for why plasticity declines with age.

Shifts the microglial narrative from "pruners" to **"sculptors" that create permissive conditions for new synapses**. Combined with Wang et al. 2020, reveals that microglia simultaneously promote new connections (via ECM clearance) and eliminate old ones (via complement), establishing microglia as bidirectional regulators of circuit remodeling. The aging dimension — IL-33 decline with age, gain-of-function rescue — suggests a candidate mechanism for age-related cognitive decline.

---

## **7\. New methods are making the previously invisible visible**

Four tools represent genuine capability discontinuities, not incremental improvements: whole-brain spatial transcriptomics (MERFISH), the first nanoscale human brain connectome, light-microscopy-based connectomics that breaks the EM monopoly, and expansion microscopy validated for clinical human specimens.

### **Paper 7.1 — Whole-brain MERFISH atlas: every cell type, every location**

**Zhang M, Pan X, Jung W, et al.** Molecularly defined and spatially resolved cell atlas of the whole mouse brain. *Nature* 624, 343–354 (2023). DOI: [10.1038/s41586-023-06808-9](https://doi.org/10.1038/s41586-023-06808-9) ✅ Verified

* **Design:** Methods-validation / resource (MERFISH imaging \+ scRNA-seq integration, whole mouse brain)  
* **Sample:** \~10 million cells; \>1,100 genes imaged; \>5,000 transcriptionally distinct clusters. Mouse.  
* **What's new:** Simultaneous whole-brain mapping of cell identity and spatial location at single-cell resolution, enabling discovery of spatial modules, cell-type gradients, and prediction of cell-cell interactions.  
* **Why it matters:** The reference atlas that BICCN and spatial neuroscience now builds upon — replaces region-by-region patchwork with a unified, queryable molecular-spatial map.

First whole-brain-scale application of spatial transcriptomics at single-cell resolution — a capability that **did not exist five years ago**. Registration to the Allen CCF creates an open community resource; any researcher can query cell-type composition of any brain region via the Allen Brain Cell Atlas platform.

### **Paper 7.2 — First nanoscale 3D reconstruction of human brain tissue**

**Shapson-Coe A, Januszewski M, Berger DR, et al.** A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science* 384(6696), eadk4858 (2024). DOI: [10.1126/science.adk4858](https://doi.org/10.1126/science.adk4858) ✅ Verified

* **Design:** Methods-validation / resource (EM reconstruction \+ AI segmentation)  
* **Sample:** 1 mm³ human temporal cortex; \~57,000 cells, \~150 million synapses, 1.4 petabytes. Human (surgical epilepsy tissue).  
* **What's new:** Any researcher can now explore a cubic millimeter of human brain at every synapse, axon, and glial cell. Revealed rare but extremely powerful axonal inputs (\~50 synapses per connection) and confirmed a **2:1 glia-to-neuron ratio** in human cortex.  
* **Why it matters:** The only existing nanoscale 3D reconstruction of human brain tissue at this scale; freely available dataset and Neuroglancer tools have already catalyzed \>200 citations.

The discovery of rare **multi-synaptic connections** (\~50 synapses from single axons to single targets) challenges simple models of cortical computation and suggests previously invisible "privileged" connectivity channels. Key limitation: single epilepsy-patient sample.

### **Paper 7.3 — LICONN breaks the electron microscopy monopoly on connectomics**

**Tavakoli MR, Lyudchik J, Januszewski M, et al.** Light-microscopy-based connectomic reconstruction of mammalian brain tissue. *Nature* 642, 398–410 (2025). DOI: [10.1038/s41586-025-08985-1](https://doi.org/10.1038/s41586-025-08985-1) ✅ Verified

* **Design:** Methods-validation (expansion microscopy \+ deep-learning segmentation \+ synaptic connectivity analysis)  
* **Sample:** Mouse somatosensory cortex (\~10⁶ μm³ native tissue). \~16× hydrogel expansion achieving \<20 nm effective resolution.  
* **What's new:** Dense, synapse-level connectomic reconstruction achievable with **standard light microscopy** rather than EM — and molecular identity of synaptic proteins can be directly overlaid on the same reconstruction.  
* **Why it matters:** Breaks the EM monopoly by achieving comparable resolution with far simpler hardware while adding molecular labeling that EM fundamentally cannot do — could democratize connectomics.

This may represent the **single most significant methodological advance in connectomics in the past decade**. Molecular labeling alongside structural connectivity opens entirely new paradigms — asking how specific molecular subtypes of synapses are distributed within a circuit. Current limitation: demonstrated at \~10⁶ μm³ scale; needs substantial scaling.

### **Paper 7.4 — Expansion microscopy for clinical human brain specimens**

**Valdes PA, Yu CJ, Aronson J, et al.** Improved immunostaining of nanostructures and cells in human brain specimens through expansion-mediated protein decrowding. *Science Translational Medicine* 16(732), eabo0049 (2024). DOI: [10.1126/scitranslmed.abo0049](https://doi.org/10.1126/scitranslmed.abo0049) ✅ Verified

* **Design:** Methods-validation (dExPath on human clinical specimens including FFPE tissue)  
* **Sample:** Human tissue: healthy brain, gliomas, Alzheimer's, Parkinson's — including archival paraffin-embedded specimens. \~4× expansion, up to 16 simultaneous biomarkers.  
* **What's new:** Nanoscale, multiplexed protein imaging on standard clinical brain pathology specimens using ordinary confocal microscopes — including formalin-fixed paraffin-embedded archives.  
* **Why it matters:** First expansion microscopy method validated for routine clinical human brain specimens, bridging basic neuroscience tool development and clinical neuropathology.

Unlike most expansion microscopy working in mouse models, dExPath tackles human clinical challenges: paraffin embedding, formalin fixation, lipofuscin autofluorescence. The Boyden lab's progression from basic ExM (2015) to this clinical-grade protocol represents a mature translational pipeline.

---

## **8\. New phenotypes connect genetic architecture to brain wiring**

The strongest new phenotypes are structural connectome genetics — two independent GWAS papers establish that white matter connectivity topology is genetically tractable and biologically distinct from previously studied brain metrics. A discovery of massive silent synapse reservoirs in adult cortex overturns assumptions about fixed adult connectivity. The first GWAS of glymphatic activity establishes brain waste clearance as a heritable phenotype. **A notable gap: no papers yet connect structural brain genetics to truly faceted cognitive phenotypes** (e.g., specific executive functions, theory of mind). The field remains tilted toward broad phenotypes.

### **Paper 8.1 — Silent synapses on filopodia: a hidden plasticity reservoir in adults**

**Vardalaki D, Chung K, Harnett MT.** Filopodia are a structural substrate for silent synapses in adult neocortex. *Nature* 612(7939), 323–327 (2022). DOI: [10.1038/s41586-022-05483-6](https://doi.org/10.1038/s41586-022-05483-6) ✅ Verified

* **Design:** Mouse electrophysiology \+ super-resolution expansion microscopy (eMAP)  
* **Sample:** 2,234 synapses from layer 5 pyramidal neurons; \~10+ mice per experiment. No genetic data.  
* **What's new:** \~25–30% of all synapses in adult mouse neocortex are functionally **silent synapses on dendritic filopodia** — structures 10× more abundant than appreciated and thought to exist only during development.  
* **Why it matters:** Overturns the dominant model of largely fixed adult cortical connectivity, demonstrating a massive latent plasticity substrate that may explain how adult brains form new memories without disrupting existing ones.

**Paradigm-shifting.** Filopodia — previously dismissed as developmental relics — form the physical basis for a dual-plasticity system: silent synapses on filopodia are easily recruited via Hebbian mechanisms while mature synapses remain stable. Validates theoretical frameworks for complementary learning systems at the synaptic level.

### **Paper 8.2 — First GWAS of the white matter connectome reveals prenatal genetic signals**

**Sha Z, Schijven D, Fisher SE, Francks C.** Genetic architecture of the white matter connectome of the human brain. *Science Advances* 9(7), eadd2870 (2023). DOI: [10.1126/sciadv.add2870](https://doi.org/10.1126/sciadv.add2870) ✅ Verified

* **Design:** Population-based cross-sectional GWAS using tractography-based structural connectivity  
* **Sample:** N=30,810 UK Biobank adults. Full GWAS. **Genetic data: Yes.**  
* **What's new:** Identified **325 genetic loci** (80% novel — never associated with any brain metric) enriched for neurogenesis, neural migration, and axon guidance, with predominantly prenatal brain expression.  
* **Why it matters:** Moves imaging genetics from regional volumes to network topology, revealing that genes shaping adult structural connectivity are predominantly active prenatally.

The key advance is phenotypic: structural connectivity captures something biologically distinct from tract-averaged FA or cortical thickness, confirmed by 69% novel loci. Language-network analysis identified **31 loci** associated with left-hemisphere language connectivity. Tractography noise is a limitation, but genetic enrichment for axon guidance genes provides biological validation.

### **Paper 8.3 — Distinct spatial signatures of genetic risk in the structural connectome**

**Wainberg M, Forde NJ, Mansour S, et al.** Genetic architecture of the structural connectome. *Nature Communications* 15, 1962 (2024). DOI: [10.1038/s41467-024-46023-2](https://doi.org/10.1038/s41467-024-46023-2) ✅ Verified

* **Design:** Population-based cross-sectional GWAS of 206 structural connectivity measures  
* **Sample:** N=26,333 UK Biobank. Full GWAS. **Genetic data: Yes.**  
* **What's new:** Identified four distinct spatial patterns of genetic association (corticothalamic, interhemispheric, combined, diffuse), implicating myelination and neurite guidance genes; polygenic scores for **specific psychiatric disorders show distinct spatial wiring signatures**.  
* **Why it matters:** Shows that genetic disposition to different disorders manifests through distinct structural connectivity profiles — moving beyond "brain structure is heritable."

The four-pattern spatial taxonomy and the finding that schizophrenia PGS associates with particular inter-regional connections rather than global connectivity are novel contributions. Together with Sha et al., establishes structural connectivity as a genetically informative phenotype class.

### **Paper 8.4 — First GWAS of brain glymphatic activity**

**Huang S-Y, Ge Y-J, Ren P, et al.** Genome-wide association study unravels mechanisms of brain glymphatic activity. *Nature Communications* 16, 626 (2025). DOI: [10.1038/s41467-024-55706-9](https://doi.org/10.1038/s41467-024-55706-9) ✅ Verified

* **Design:** Multi-cohort GWAS with replication \+ cross-lifespan validation  
* **Sample:** Discovery: N=31,021 (UK Biobank). Replication: N=3,730. Lifespan validation: ABCD (N=4,307), IMAGEN (N=1,589), HCP (N=219). **Genetic data: Yes** throughout.  
* **What's new:** First GWAS of the ALPS index (proxy for glymphatic clearance), identifying **17 genome-wide significant loci** with shared genetic architecture with ventricular volumes and CSF tau levels, and concordant effects from childhood to old age.  
* **Why it matters:** Establishes glymphatic function as a heritable, genetically tractable phenotype sharing overlap with Alzheimer's-relevant biomarkers — a new axis for neurodegeneration genetics.

Treating the ALPS index as a GWAS phenotype indexes a physiological process rather than static structure. The cross-lifespan validation is unusually strong: the 2p23.3 locus shows concordant effects from **ages 9 to 82**. ALPS-index validity remains debated, but genetic enrichment for relevant pathways lends credibility.

---

## **9\. Lab and researcher mapping**

### **Established leaders reshaping the field**

**H. Sebastian Seung (Princeton)** — Co-led both the first complete adult brain connectome (FlyWire, *Drosophila*) and the largest mammalian functional connectome (MICrONS). His CAVE infrastructure is the backbone for collaborative connectomics worldwide. *Papers: 1.1, 1.2, 1.3.*

**Ed S. Lein (Allen Institute for Brain Science)** — Principal architect of the BICCN human brain cell atlas effort. Led the coordinated atlas publications establishing the reference taxonomy for brain cell types. *Papers: 2.1, 2.2, 2.3, 2.4.*

**Sten Linnarsson (Karolinska Institutet)** — Led the most comprehensive human brain cell atlas (\>3 million nuclei, \>3,000 types). Also produced the first comprehensive first-trimester developing human brain atlas (Braun et al., *Science* 2023). *Paper: 2.1.*

**Arnold Kriegstein (UCSF)** — Continues defining how human-specific progenitor types generate the expanded cortex. His trainees — Nowakowski, Bhaduri, Pollen — now lead labs producing independent high-impact work. *Papers: 4.3, 4.4.*

**Christopher A. Walsh (Harvard/BCH)** — 2022 Kavli Prize laureate. Published the groundbreaking spatial transcriptomics study of human fetal cortical specification. Pioneered single-neuron whole-genome sequencing revealing somatic mosaicism. *Paper: 4.1.*

**Lorenz Studer (Memorial Sloan Kettering)** — Breakthrough discovery of the epigenetic maturation clock. Generates the field's most sophisticated directed differentiation protocols. *Paper: 4.2.*

**Katrin Amunts (Forschungszentrum Jülich)** — Leading the BigBrain and Julich-Brain projects providing the highest-resolution 3D cytoarchitectonic reference for the human brain. *Paper: 3.1.*

**Theodore Satterthwaite (Penn, PennLINC)** — The sensorimotor-association axis framework has become the dominant model for understanding human cortical maturation. Leads a major neuroimaging methods hub. *Paper: 5.1.*

**Jeff Lichtman (Harvard)** — Published the first nanoscale map of human cerebral cortex. Collaborating with Google on AI-assisted segmentation. *Paper: 7.2.*

**Xiaowei Zhuang (Harvard/HHMI)** — Inventor of MERFISH; the technology is now critical infrastructure for BRAIN Initiative Cell Census efforts. *Paper: 7.1.*

**Edward Boyden (MIT)** — Expansion microscopy pipeline from basic ExM to clinical-grade human tissue protocols (dExPath). *Paper: 7.4.*

**Moritz Helmstaedter (MPI Brain Research, Frankfurt)** — Not represented in the paper list but an essential figure: published the first connectomic reconstruction of a defined cortical column in mouse barrel cortex (2024), developed RoboEM reducing annotation costs 400-fold. Leibniz Prize recipient. **Should be on the radar.**

**Jonathan Kipnis (Washington University → Stanford)** — Pioneered ACE points discovery connecting peripheral immune surveillance to brain structural organization. *Paper: 3.3.*

### **Rising stars producing outsized impact**

**Sven Dorkenwald (MIT McGovern, incoming faculty)** — Led the technical effort producing the first complete adult brain connectome (*Drosophila*). Developed CAVE, the critical infrastructure for collaborative petascale connectomics. Won the 2024 Larry Katz Memorial Lectureship. Perhaps the single most impactful rising star in connectomics. *Papers: 1.1, 1.2, 1.3.*

**Tomasz Nowakowski (UCSF)** — Lineage-resolved atlas of developing human cortex (*Nature* 2025), spatiotemporal dynamics of the developing thalamus (*Science* 2023), thalamocortical organoid models. Updated Rakic's Radial Unit model with the Supragranular Cortex Expansion Hypothesis. Lab established \~2017; CZI BioHub Investigator, Allen Institute Next Gen Leader.

**Aparna Bhaduri (UCLA)** — Created the first meta-atlas of the developing human cortex identifying specification modules (*Nat Neurosci* 2023). Bridges developmental neuroscience and glioblastoma biology. Lab opened 2021; McKnight Neurobiology of Brain Disorders Award 2024\.

**Vicky Sydnor (Pittsburgh, transitioning to faculty)** — First-authored the landmark S-A axis study. Named among The Transmitter's Rising Stars 2025\. *Paper: 5.1.*

**Longzhi Tan (Stanford)** — 2024 McKnight Scholar. Developed a "biochemical microscope" for 3D DNA structure at unprecedented resolution, studying how chromatin folding shapes brain development. **Not in the paper list — should be tracked.**

### **Key consortia and collaborative efforts**

* **FlyWire Consortium (Princeton, MRC LMB Cambridge):** First complete connectome of an adult brain. Published October 2024 in *Nature* (12+ papers). Data at flywire.ai/codex. Now extending to male fly brain and ventral nerve cord.  
* **MICrONS (Allen Institute, Baylor, Princeton):** Largest mammalian functional connectome. Published April 2025 in *Nature* (10 papers). Open access at microns-explorer.org.  
* **BICCN/BICAN (Allen Institute, Karolinska, Salk, UCSD):** Published the most comprehensive multimodal human brain cell atlas (21+ papers, *Science* October 2023). Now transitioning to BICAN for even larger-scale efforts.  
* **BRAIN CONNECTS (Allen Institute):** Goal: scale EM connectomics to the entire mouse brain (\~500× the MICrONS volume). Active development.  
* **Human Brain Project / EBRAINS (FZ Jülich):** BigBrain and Julich-Brain cytoarchitectonic atlases at cellular resolution; integrated multi-scale atlas infrastructure.

### **Geographic hubs**

Princeton (connectomics), Allen Institute Seattle (cell types \+ connectomics), UCSF (development, glia), Harvard/BCH (development \+ methods), Karolinska Institutet (cell atlases), MPI Frankfurt (cortical connectomics), FZ Jülich (structural anatomy), Penn (adolescent brain), MIT (neurotechnology \+ dendritic computation). A notable training pipeline: the **Kriegstein lab** (UCSF) has spawned Nowakowski, Bhaduri, and Pollen; the **Seung lab** has produced Dorkenwald.

---

## **Conclusion: where the field is actually heading**

The most consequential momentum is concentrating in three areas. First, **cell-type-resolved developmental neuroscience** — the convergence of spatial transcriptomics, multi-omic profiling, and large donor cohorts is producing the first mechanistic understanding of how human brain regions acquire their identities, with the Tri-IPC discovery and epigenetic maturation clock representing genuine paradigm shifts. Second, **connectomics is transitioning from mapping to mechanism** — the MICrONS "like-to-like" finding and inhibitory motif groups show that synapse-level wiring rules can now be extracted from connectomic data, but the field's celebrated datasets structurally cannot address individual differences because they are all n=1. This is the most important unsolved problem in connectomics. Third, **glial biology has crossed the threshold from supporting role to causal circuit participant** — myelination closing critical periods, astrocyte ensembles driving behavior, microglia executing both forgetting and plasticity promotion through distinct molecular pathways.

Two sub-areas are thinner than expected. Revised structural anatomy beyond meningeal discoveries is largely confirmatory — thalamic parcellation and white matter tract discovery have not produced post-2019 findings that clearly force textbook revision. And despite impressive GWAS of brain structural connectivity, **no paper yet connects genetic architecture to truly faceted cognitive phenotypes** (specific executive functions, theory of mind, temporal discounting); the field remains dominated by broad phenotypes.

The clearest cross-cutting theme is that **myelination has been promoted from passive insulation to active developmental regulator** — visible in Sydnor's S-A axis, Genc's oligodendrocyte-expression alignment, Xin's critical period gating, and the emerging recognition that "cortical thinning" during adolescence reflects oligodendrocyte maturation more than synaptic pruning. This convergence across independently pursued sub-areas suggests a genuine reorientation of developmental neuroscience around myelination biology.

