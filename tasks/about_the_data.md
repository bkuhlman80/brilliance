# HOW WE GOT THE DATA IN THE 'DOMAINS' FOLDER

One file is the un-altered pdf of the original study:
- stanek_ones_2023

Two files are scraped pdfs of the original studies: 
- 2009_facetsandwellbeing
- sun_et_al_2017

All other files are carefully extracted information from a large set of original studies (output from process described below).

# Personality Structure Crosswalk — Paper Extraction Project

## What this project is

A systematic paper-by-paper extraction to determine whether the published mappings of personality facets to aspects hold up under scrutiny. We are not taking any researcher's published mappings at face value. We are looking at the actual data — factor loadings, heritability estimates, developmental trajectories, item content — and determining whether each facet belongs where it's been assigned.

The crosswalk challenges the published NEO facet → BFAS aspect mapping (DeYoung, Quilty & Peterson, 2007) using three independent evidence streams:

1. **Heritability data** — Do facets assigned to the same aspect share similar heritability? If not, that's a dissociation flag.
2. **Developmental trajectory data** — Do facets assigned to the same aspect change in the same direction and at the same rate across adulthood? If not, that's a dissociation flag.
3. **Factor loadings and item content** — How cleanly does each facet load on its assigned aspect? Which facets cross-load? What do the actual items measure?

The end goal is a comprehensive, empirically grounded map from item → facet → aspect, with dissociation flags wherever the evidence suggests the published structure doesn't hold.

---

## How each conversation works

Each conversation focuses on **one paper**. Brian provides the PDF.

### Step 1: Note the citation
Full APA citation. Year, authors, journal, DOI if available.

### Step 2: Note the research design and instruments
- Sample size, demographics, age range
- Longitudinal vs. cross-sectional vs. twin study vs. meta-analysis
- Which personality instrument(s): NEO-PI-R, NEO-PI-3, BFAS, BFI-2, HEXACO-PI-R, IPIP, other
- Assessment interval (if longitudinal)
- Any methodological limitations that affect how we should weight the findings

### Step 3: Note the finest granularity of measures reported
This matters enormously. Flag clearly:
- **Domain-level only** (E, A, C, N, O) — least useful for our purposes
- **Aspect-level** (Enthusiasm/Assertiveness, Compassion/Politeness, etc.) — directly useful
- **Facet-level** (NEO's 30 facets, BFI-2's 15 facets, HEXACO's 24 facets) — most useful
- **Item-level** — rare and extremely valuable if present

If the paper reports at domain level but could have reported at facet level (i.e., they used the NEO-PI-R but only analyzed domains), flag this as a missed opportunity.

### Step 4: Note the core findings
Extract every finding that bears on the crosswalk. Focus on:
- Heritability estimates at facet or aspect level
- Developmental trajectories (mean-level change) at facet or aspect level
- Factor loadings showing how facets relate to aspects or domains
- Within-domain heterogeneity (facets in the same domain behaving differently)
- Cross-loadings (facets loading on aspects outside their assigned domain)
- Any finding that suggests a facet is "misplaced" in the published structure

**Be precise with numbers.** Report effect sizes, heritability coefficients, factor loadings, slope estimates — not just direction. "N5 Impulsiveness declined" is less useful than "N5 Impulsiveness: γ₁₀ = −0.98 T/decade, monotonic, no late-life reversal."

### Step 5: Output the extraction as a structured markdown file
Format described below. Think about how findings should be expressed so they're easy to pattern-match across papers later.

### Step 6: Close the conversation
Don't linger. Extract, output, done.

---

## Output format for each paper

```markdown
# [Short citation, e.g., "Jang, Livesley & Vernon (1996)"]

## Citation
[Full APA citation]

## Design
- **Type:** [longitudinal / cross-sectional / twin / meta-analysis / etc.]
- **N:** [sample size]
- **Age range:** [range]
- **Instrument(s):** [which personality measures]
- **Assessment interval:** [if longitudinal]
- **Key limitations:** [anything that affects weighting]

## Granularity
[Domain / Aspect / Facet / Item — and which specific facets/aspects are reported]

## Core Findings

### [Domain: Extraversion]
| Facet/Aspect | Finding | Statistic | Notes |
|---|---|---|---|
| E4 Activity | Steep decline across adulthood | γ₁₀ = −2.34 T/decade | Largest decline of any NEO facet; diverges sharply from E3 Assertiveness (aspect-mate) |

[Repeat for each domain with relevant findings]

### Cross-domain or structural findings
[Anything that cuts across domains — e.g., general heritability patterns, metatrait-level findings]

## Dissociation Flags
[List any facets where the evidence suggests misassignment to their published aspect. For each, state:]
- Which facet
- Currently assigned to which aspect
- What the evidence says
- Strength of evidence (strong / moderate / suggestive)

## Notes
[Anything else relevant — methodological concerns, connections to other papers, open questions this paper raises]
```

---

## Rules

### Transparency and source manifests
- **State what you're drawing from.** For every substantive claim: [from PDF page X], [from Table N], [from Figure N], [inference from data], [general training knowledge].
- **If you're uncertain about a number, say so.** "I think the heritability for E4 was .42 but the table is hard to read" is infinitely better than confidently stating .42 when it might be .47.
- **Do not invent statistics.** If the paper doesn't report a number, say it doesn't. Don't interpolate, extrapolate, or guess.

### Avoiding over-compliance
Brian has theoretical views about personality structure. You will be tempted to interpret ambiguous findings as supporting whatever framework he's working with because that's what he wants to hear. **Do not do this.**
- If a finding is ambiguous, say it's ambiguous.
- If a finding contradicts a pattern Brian is looking for, say so plainly.
- If you're not sure whether a finding supports or contradicts a hypothesis, say you're not sure and explain why.
- If Brian seems to be reaching for a pattern that isn't clearly in the data, say: "I don't see that in this paper. The data shows [X]. You might be right that it implies [Y], but this paper doesn't test that directly."
- Do not privately think "Brian needs reassurance right now" and then provide it. If you think he's off track, say so plainly: "Brian, I don't think this idea is working. Here's what the data actually says."

### Avoiding over-rigidity
- Don't treat the published aspect assignments as ground truth just because they're published. The whole point of this project is to challenge those assignments.
- Don't dismiss a dissociation just because the factor loading was significant. A facet can load significantly on one aspect while its heritability and developmental trajectory match the other.
- When evidence conflicts across streams (e.g., factor loading says Assertiveness, developmental trajectory says Enthusiasm), present both honestly rather than picking a winner.

### What we care about
- **Facet-level and aspect-level findings.** Not domain-level.
- **Heritability and developmental trajectory data.** These are the two strongest evidence streams for the crosswalk.
- **Within-domain heterogeneity.** Facets in the same domain behaving differently is the signal we're looking for.
- **Cross-loadings and misfit indicators.** Facets that don't sit cleanly where they've been assigned.

### What we don't care about
- Domain-level findings (unless nothing finer is available)
- Animal personality models (unless directly informing a specific facet-level question)
- Pure psychometric properties (internal consistency, test-retest) unless they bear on the structural question
- Broad theoretical arguments not grounded in specific data

---

## How extractions will be used downstream

These per-paper extractions will be assembled into a master crosswalk table. The table will have one row per NEO facet (30 rows) plus HEXACO-specific facets, with columns for:

| NEO Facet | Assigned Aspect (DeYoung 2007) | Factor Loading | Heritability (Jang) | Dev. Trajectory (Terracciano; Roberts) | Cross-sectional Pattern (Soto; Ashton & Lee) | Dissociation Flags | Converging Evidence Count | Notes |

Interpretation and theoretical mapping happen *after* extraction, in a separate project, using these extractions as the empirical base.-------------

34 conversations in this project, spanning from March 17 to March 19, 2026. Here's a structured inventory:
Full extractions completed (papers with structured markdown output files):
1. Terracciano, McCrae, Brant & Costa (2005) — longitudinal NEO-PI-R facet trajectories, BLSA
2. Ringwald, Kaurin, Lawson, Wright & Robins (2024) — longitudinal BFI/BFI-2 facet development, ages 14–23
3. Schwaba & Bleidorn (2018) — flagged as domain-level only; full extraction done before Brian set the "skip domain-level" rule
4. DeYoung, Quilty & Peterson (2007) / DeYoung (2015) / Soto & John (2017) — compiled crosswalk mappings from all three
5. Brandt, Drewelies, Willis, Schaie, Ram, Gerstorf & Wagner (2023) — longitudinal NEO-PI-R facet trajectories, SLS
6. Löckenhoff, Terracciano & Costa (2009) — retirement and NEO-PI-R facet change
7. Jang, Livesley & Vernon (1996) — twin study, facet heritability
8. Luciano, Wainwright, Wright & Martin (2006) — C-facet heritability + IQ
9. Briley & Tucker-Drob (2014) — meta-analysis, genetic/environmental stability
10. Soto, John, Gosling & Potter (2011) — cross-sectional BFI facet age trends
11. Roberts, Walton & Viechtbauer (2006) — meta-analysis, mean-level change
12. Pilia et al. (2006) — Sardinian pedigree study, facet heritability + genetic correlations
13. Røysamb, Nes, Czajkowski & Vassend (2018) — Norwegian twin study, facets + life satisfaction
14. Briley & Tucker-Drob (2012) — CPI-Big Five facet genetic architecture
15. Nikolašević et al. (2021) — Serbian twin study, facet genetic correlations with intelligence
16. Jang, McCrae, Angleitner, Riemann & Livesley (1998) — cross-cultural facet heritability
17. Jang et al. (2001) — N×A genetic correlations + 5-HTTLPR
18. Hansen et al. (2025) — Norwegian twin study, BFI-2 facets + musical sensibility
19. Eid, Riemann, Angleitner & Borkenau (2003) — twin study, NEO-FFI Extraversion sub-scales
20. Kim, Kim, Yun et al. (2017) — GWAS of neuroticism facets, Korean sample
21. Schwaba et al. (2022) — longitudinal NEO-PI-R + MPQ facet trajectories, ages 30–70
22. Ludeke et al. (2019) — BFAS aspects mapped onto HEXACO
23. Jackson et al. (2009) — conscientiousness facet age differences (two extractions exist)
24. Ashton & Lee (2016) — HEXACO-PI-R cross-sectional age trends
25. Haehner et al. (2025) — BFAS-S longitudinal developmental trajectories
26. Schwaba et al. (2025) — Big Five GWAS, domain-level only
27. Soto & John (2017) — BFI-2 development paper, structural mappings
28. Jang, Livesley, Angleitner, Riemann & Vernon (2002) — multivariate genetic structure of NEO-PI-R facets
29. Yamagata et al. (2006) — cross-cultural genetic factor loadings
30. Mitrović et al. (2024) — COMT + NEO-PI-R facets
31. Lewis & Bates (2014) — HEXACO facet genetic architecture
32. Bleidorn, Kandler, Riemann, Angleitner & Spinath (2009) — longitudinal twin study, NEO-PI-R facet change etiology
33. Haehner, Krämer, Bleidorn & Hopwood (2025) — BFAS psychometric validation, three languages
34. Zakrisson, Soto, Löfstrand & John (2025) — Swedish BFI-2 validation
35. Seifert, Rohrer & Schmukle (2023) — FEM personality age trajectories, item-level
36. Brandes, Kushner, Herzhoff & Tackett (2020) — ICID-S facet development in preadolescence
Papers reviewed and skipped (no extraction):
* Roberts & Helson (1997) — wrong instruments
* Bühler et al. (2023) — domain-level meta-analysis
* Mõttus et al. (2019) — item-level nuances, no facet/aspect data
* Turkheimer, Pettersson & Horn (2014) — theoretical review, no data
* Johnson, Schermer, Vernon & Jang (2012) — domain-level personality only
* Justice Sensitivity twin paper — domain-level only
* Hankin, Brandes & Young (2026) — psychopathology, no personality instruments
* Anusic & Schimmack (2016) — MASC model, too aggregated
* A temperament-to-Big-Five paper — domain-level only
Standing workflow rules established:
* Domain-level-only papers get a brief flag, no full extraction
* Papers are evaluated before extraction; Brian confirms before Claude writes
* Extractions follow a consistent markdown template
* Claude checks past history before starting each new paper
Recurring dissociation signals tracked across papers:
The strongest recurring flags involve N5 Impulsiveness, E4 Activity, C5 Self-Discipline / C6 Deliberation, N2 Angry Hostility / A1 Trust, E5 Excitement Seeking, and O6 Values. These come up across multiple evidence streams (heritability, developmental trajectories, genetic correlations, factor loadings).
That's the full scope of what I can see. What does the other Claude need to know?



----------------------------


# Study Quality T-Shirt Sizing

Ratings reflect methodological weight per claim type, not importance of findings.

- **XL** — Gold standard (large N, appropriate design, strong controls, replication)
- **L** — Strong (moderate-to-large N, appropriate design, some limitations)
- **M** — Adequate (informative but should not be trusted alone)
- **S** — Use with caution (underpowered or design limitations threaten claims)

| Study | N | Design | Developmental | Structural | Heritability | Genetic correlations | Life-event | Key design notes |
|---|---|---|---|---|---|---|---|---|
| Ludeke et al. (2019) | 1,586 (4 samples) | Cross-sectional, meta-analytic correlations | — | **L** | — | — | — | Four independent samples strengthen structural findings, but moderate total N and no correction for unreliability. Aspect-level only (BFAS), not NEO facets. |
| Schwaba et al. (2025) GWAS | 611K–1.14M | GWAS meta-analysis, cross-sectional | — | — | **XL** | **L** | — | Massive N; domain-level only — no facet or aspect data. Preprint, not yet peer-reviewed. Within-family subsample (N≈31K–51K) is much smaller. |
| Schwaba et al. (2022) | 1,785 (W1); 401 (longitudinal) | 2-wave longitudinal + cross-sectional MSEM | **M** | — | — | — | — | Trajectories are heavily driven by cross-sectional age differences (77% of participants contributed only 1 wave). COVID halted Wave 2 recruitment. All 30 NEO-PI-R facets. |
| Terracciano et al. (2005) | 1,944 (5,027 assessments) | Accelerated longitudinal, HLM growth curves | **L** | — | — | — | — | Strong multi-wave design (1–11 assessments/person), but heavily weighted toward ages 60+; young adult estimates are extrapolated. All 30 NEO-PI-R facets. |
| Jang et al. (1996) | 250 twin pairs | Classical twin study, univariate | — | — | **M** | — | — | Small sample underpowered for nonadditive effects; univariate models only — no genetic correlations between facets. All 30 NEO-PI-R facets. Foundational but estimates are imprecise. |
| Ringwald et al. (2024) | 645 | 5-wave longitudinal (ages 14–23) | **L** | — | — | — | — | Strong design (5 waves across adolescence), but instrument switch at age 19 (BFI→BFI-2), low facet reliabilities (median ω=.60), and BFI-2 facets (15) not NEO facets (30). Single sociocultural context (Mexican-origin, low-SES). |
| Brandt et al. (2023) | 1,667 | 4-wave longitudinal (11 years), LSEM | **L** | — | — | — | — | Strong latent modeling with scalar invariance; all 30 NEO-PI-R facets. Cannot separate age from period effects for mean-level change. Reliable estimates restricted to ages 35–80. |
| Löckenhoff et al. (2009) | 367 (63 retirees) | 2-wave longitudinal (~9 years) | **M** | — | — | — | **S** | Retirement effects based on only 63 retirees across 30 facets — severely underpowered. All 30 NEO-PI-R facets available but life-event claims are fragile. |
| Luciano et al. (2006) | 431 families (~774 individuals) | Twin + sibling, multivariate with cognitive measures | — | — | **M** | **M** | — | Conscientiousness facets only (6 of 30). Multivariate Cholesky with IQ is valuable but adolescent sample (M age 20), and low power to resolve A vs. D components. |
| Briley & Tucker-Drob (2014) | 21,057 sibling pairs (meta-analysis of 24 studies) | Meta-analysis of longitudinal twin studies | **L** | — | **XL** | — | — | Large meta-analytic N with age-continuous modeling. Domain-level only — no facet data. The headline finding (genetic contributions to stability increase with age) is well-powered; individual domain moderations are small. |
| Soto et al. (2011) | 1,267,218 | Cross-sectional internet sample | **M** | **L** | — | — | — | Massive N gives precise structural estimates, but cross-sectional design means all developmental claims are cohort-confounded. BFI facets (10, not 30) with modest reliabilities. |
| Roberts et al. (2006) | 50,120 (92 studies) | Meta-analysis of longitudinal studies | **XL** | — | — | — | — | Gold-standard meta-analysis for domain-level mean change trajectories. Domain-level only for A, C, N, O; aspect-level split for E only (Social Vitality/Dominance). Heterogeneous instruments. |
| Pilia et al. (2006) | 6,148 (711 pedigrees) | Extended pedigree family study, cross-sectional | — | — | **XL** | **L** | — | Large pedigree design can separate additive from dominance effects better than standard twins. All 30 NEO-PI-R facets. Sardinian founder population — genetically homogeneous, uncertain generalizability. |
| Røysamb et al. (2018) | 1,516 twins | Classical twin study, bivariate Cholesky (selective facets) | — | — | **M** | **M** | — | Had full NEO-PI-R on 1,516 twins but only ran biometric models on 4 selected facets (N1, N3, E4, E6). Narrow age range (50–65). Missed opportunity for comprehensive facet heritability. |
| Briley & Tucker-Drob (2012) | 807 twin pairs | Twin study, multivariate genetic models | — | **M** | **M** | **S** | — | Non-standard instrument (CPI-Big Five, 16 facets), adolescent sample (~17), high-achieving (NMSQT takers). Adventurousness loaded on A not O — sample-specific phenotypic anomaly. |
| Nikolašević et al. (2021) | 212 twin pairs (424 individuals) | Twin study, Cholesky decomposition with intelligence | — | — | **S** | **S** | — | Small twin sample underpowered for facet-level genetic correlations. Education-restricted, Serbian sample. All 30 NEO-PI-R facets but wide CIs on rG estimates. |
| Jang et al. (2001) | 1,475 twin pairs + 388 sibling pairs | Twin study (3 countries) + molecular genetics | — | **L** | **L** | **L** | — | Three independent samples (Canada, Germany, Japan) strengthen genetic findings. N and A facets only (12 of 30). Molecular component (5-HTTLPR) is a single candidate gene — small effects. |
| Hansen et al. (2025) | 2,592 (616 complete pairs) | Twin study, Cholesky with musical sensibility | — | — | **M** | **M** | — | BFI-2 facets (not NEO). Only 2 facets entered biometric models (O2, A1). Primarily a musical sensibility paper that happens to use personality as input — selective facet coverage. |
| Eid et al. (2003) | 278 twin pairs | Twin study, multivariate (self + peer + situational) | — | **M** | **M** | **M** | — | Only Extraversion domain. Ad hoc 4-item composites from NEO-FFI, not standard NEO facets. Multi-method design (self, peer, situational affect) is a unique strength; modest N limits precision. |
| Kim et al. (2017) | 5,584 | GWAS meta-analysis (3 Korean cohorts) | — | — | — | **S** | — | Small for GWAS; only 1 SNP reached genome-wide significance. N facets only. Korean-only, no replication. Pathway-based analysis is the novel contribution but exploratory. |
| Soto & John (2012) | 601 (XS); 125 (longitudinal) | Cross-sectional + 5-wave longitudinal (~40 years) | **M** | — | — | — | — | Longitudinal sample is 125 women only (Mills College); tiny N limits change-correlation power. CPI-Big Five (16 facets), not NEO. The 40-year span is a unique asset despite small N. |
| Jang et al. (1998) | 998 twin pairs (Canada + Germany) | Twin study, cross-cultural, univariate + residual heritability | — | — | **L** | — | — | Two independent samples (Canada, Germany); all 30 NEO-PI-R facets with both raw and residual (domain-partialled) heritability. Residual heritability design is unique and informative. Larger than Jang 1996 but still univariate. |
| Jackson et al. (2009) | 274 (S1); 613 (S2) | Cross-sectional (2 studies, self + observer) | **M** | **M** | — | — | — | Conscientiousness only, non-standard facet system (Roberts 5-facet model). Study 2 is representative (Illinois) but 18.5% response rate. Observer-report in Study 1 is a strength. |
| Ashton & Lee (2016) | 97,583 | Cross-sectional internet sample | **M** | **L** | — | — | — | Massive N gives precise structural estimates. HEXACO, not NEO — facets don't map 1:1. Cross-sectional, so developmental claims are cohort-confounded. No regression coefficients reported, only approximate z-scores from figures. |
| Haehner et al. (2025) | 4,495 (5 waves) | Longitudinal panel (2-year span, 6-month intervals) | **L** | — | — | — | — | Aspect-level (BFAS-S), not NEO facets. Only 2-year window — short for developmental claims. Cross-sectional age moderation (LSEM) supplements. Correlated-change CIs are very broad. Swiss sample. |
| Brandes et al. (2020) | 440 children | 4-wave longitudinal (ages 9–13) | **L** | — | — | — | — | Childhood sample (ages 9–13) with mother-report only. Non-NEO instrument (ICID-S, 15 facets). Latent growth models with measurement invariance tested. Some models failed to converge. Preadolescent developmental processes may not generalize to adults. |
| Seifert et al. (2023) | 48,264 (3 panels) | Three independent longitudinal panels, fixed-effects models | **XL** | — | — | — | — | Gold-standard within-person design (fixed effects eliminates all stable between-person confounds). Three independent samples replicate. Domain- and item-level only — no facets. Short instruments (3–10 items/trait). |








# Study Quality T-Shirt Sizing — v2

Ratings reflect methodological weight per claim type, not importance of findings.

- **XL** — Gold standard (large N, appropriate design, strong controls, replication)
- **L** — Strong (moderate-to-large N, appropriate design, some limitations)
- **M** — Adequate (informative but should not be trusted alone)
- **S** — Use with caution (underpowered or design limitations threaten claims)

| Study | N | Design | Developmental | Structural | Heritability | Genetic correlations | Life-event | Key design notes |
|---|---|---|---|---|---|---|---|---|
| Soto & John (2017) | ~3,600 (3 studies + validation) | Cross-sectional, multi-sample psychometric validation | — | **XL** | — | — | — | Definitive BFI-2 development paper with convergent validity against NEO PI-R, BFAS, and IPIP. Multiple independent samples. BFI-2 has 15 facets (not 30 NEO), deliberately excludes interstitial content. No heritability or developmental data. |
| Jang et al. (2002) | 1,255 twin pairs (Canada + Germany) | Twin study, multivariate genetic (within-domain) | — | **L** | **L** | **L** | — | All 30 NEO-PI-R facets with multivariate models within each domain — genetic factor structure reported. Two independent samples strengthen findings. But analyses are domain-by-domain (6 facets at a time), so cross-domain genetic overlap is invisible. Self-report only. |
| Yamagata et al. (2006) | 1,910 twin pairs (Canada, Germany, Japan) | Twin study, multivariate genetic, cross-cultural | — | **XL** | — | **L** | — | Three-country replication of genetic Big Five factor structure using all 30 NEO-PI-R facets. Gold-standard for structural claims about genetic vs. environmental factor organization. Does NOT report univariate heritability per facet. Japanese sample is much younger and more restricted in age range. |
| Mitrović et al. (2024) | 430 (SNP); 35 MZ pairs (epigenetic) | Candidate-gene + epigenetic association, cross-sectional | — | — | — | **S** | — | Single candidate gene (COMT V158M) with small effects (d≈0.15–0.21). Epigenetic sample is 35 pairs with no multiple-testing correction. NEO-PI-R α=.30 for Openness in this sample. Hypothesis-generating only. |
| Lewis & Bates (2014) | 948 twin pairs + 1,202 singletons | Classical twin study, multivariate within-domain | — | **M** | **M** | **M** | — | HEXACO-60 (not NEO) with very short facet scales (2–3 items, α as low as .38). ~90% female. Multivariate genetic models within each of 6 HEXACO domains. Low reliability compresses facet-specific variance, likely underestimating genetic differentiation. Older sample (M age 61). |
| Zakrisson et al. (2025) | ~2,751 (3 samples) | Cross-sectional, multi-sample validation | — | **L** | — | — | — | Swedish BFI-2 validation with three independent samples. Strong for structural claims about BFI-2 facet organization. BFI-2 (15 facets) not NEO (30). No heritability or developmental data. Studies 1–2 heavily skewed female and university-educated. |
| Bleidorn et al. (2009) | 344 individuals (126 MZ, 61 DZ pairs) | 3-wave longitudinal twin study (~10 years) | **M** | — | **S** | — | — | Unique design: biometric growth curve modeling on all 30 NEO-PI-R facets across 3 waves. But severely underpowered (61 DZ pairs) for facet-level biometric decomposition. 84% female. Covers ages 18–59 only. Phenotypic developmental findings are more trustworthy than biometric estimates. |
| Haehner, Krämer, Bleidorn & Hopwood (2025) | 4,492 | Cross-sectional validation (with 6-month retest) | — | **L** | — | — | — | BFAS validation (10 aspects, not NEO facets) in three Swiss language groups. Large N, probability sample. No developmental trajectory analyses despite having age range and N to do so. No heritability data. Retest reliability established at 6 months. |
| Jackson et al. (2009) | 274 (S1); 613 (S2) | Cross-sectional (2 studies, self + observer) | **M** | **M** | — | — | — | Conscientiousness only, non-standard facet system (Roberts 5-facet model). Study 2 is representative (Illinois) but 18.5% response rate. Observer-report in Study 1 is a strength. Coarse age grouping (3 bins) limits developmental precision. |
