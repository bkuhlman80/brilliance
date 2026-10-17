# Genetic Architecture Gradient: Heritability Decomposition by BRILLIANCE II Venn Zone

## Purpose

Test whether there is a gradient in genetic architecture across the BRILLIANCE II Venn diagram: Primary traits (pure C, A, E) should have more additive genetics; Center traits (impulsivity-related) should have more nonadditive/dominance genetics — because center traits require multi-system coordination, which means epistatic (gene x gene) interactions dominate.

**Prediction:** Primary A/(A+D) > Intersection A/(A+D) > Center A/(A+D)

## Data Source

**Pilia et al. (2006)** is the only study in the repo reporting both narrow-sense (A) and broad-sense (A+D) heritability for all 30 NEO-PI-R facets simultaneously. Extended pedigree design, N = 6,148, Sardinia. Quality: **XL**.

Supplementary data from:
- Luciano et al. (2005) — N = 431 families, ADE models for C facets only
- Jang et al. (1996) — N = 250 twin pairs, ACE/ADE model selection per facet
- Yamagata et al. (2006) — AE models only (no D), but provides genetic factor loadings

## Master Table: All 30 NEO-PI-R Facets

| NEO Facet | Venn Zone | A (narrow h²) | D (broad-narrow) | Broad H² | A/(A+D) | Source |
|---|---|---|---|---|---|---|
| **PRIMARY (pure C)** | | | | | | |
| C1 Competence | Primary-C | .129 | .160 | .289 | .446 | Pilia 2006 |
| C2 Order | Primary-C | .165 | .044 | .209 | .789 | Pilia 2006 |
| C3 Dutifulness | Primary-C | .089 | .145 | .234 | .380 | Pilia 2006 |
| C4 Achievement Striving | Primary-C | .093 | .092 | .185 | .503 | Pilia 2006 |
| **PRIMARY (pure A)** | | | | | | |
| A1 Trust | Primary-A | .188 | .065 | .253 | .743 | Pilia 2006 |
| A2 Straightforwardness | Primary-A | .134 | .279 | .413 | .324 | Pilia 2006 |
| A4 Compliance | Primary-A | .132 | .000 | .132 | 1.000 | Pilia 2006 |
| **PRIMARY (pure E)** | | | | | | |
| E1 Warmth | Primary-E | .186 | .000 | .186 | 1.000 | Pilia 2006 |
| E2 Gregariousness | Primary-E | .199 | .104 | .303 | .657 | Pilia 2006 |
| E6 Positive Emotions | Primary-E | .149 | .085 | .234 | .637 | Pilia 2006 |
| **INTERSECTION C x A (Neuroticism zone)** | | | | | | |
| N1 Anxiety | CxA | .140 | .173 | .313 | .447 | Pilia 2006 |
| N2 Angry Hostility | CxA | .186 | .118 | .304 | .612 | Pilia 2006 |
| N3 Depression | CxA | .202 | .193 | .395 | .511 | Pilia 2006 |
| N4 Self-Consciousness | CxA | .180 | .060 | .240 | .750 | Pilia 2006 |
| N6 Vulnerability | CxA | .117 | .102 | .219 | .534 | Pilia 2006 |
| **INTERSECTION C x E (Openness zone)** | | | | | | |
| O1 Fantasy | CxE | .206 | .069 | .275 | .749 | Pilia 2006 |
| O2 Aesthetics | CxE | .225 | .149 | .374 | .602 | Pilia 2006 |
| O3 Feelings | CxE | .127 | .110 | .237 | .536 | Pilia 2006 |
| O4 Actions | CxE | .165 | .114 | .279 | .591 | Pilia 2006 |
| O5 Ideas | CxE | .243 | .135 | .378 | .643 | Pilia 2006 |
| **INTERSECTION A x E (Dominance zone)** | | | | | | |
| E3 Assertiveness | AxE | .149 | .270 | .419 | .356 | Pilia 2006 |
| A3 Altruism | AxE | .146 | .025 | .171 | .854 | Pilia 2006 |
| A6 Tender-Mindedness | AxE | .077 | .081 | .158 | .487 | Pilia 2006 |
| **CENTER (impulsivity-related)** | | | | | | |
| N5 Impulsiveness | Center | .105 | .227 | .332 | .316 | Pilia 2006 |
| C5 Self-Discipline | Center | .123 | .240 | .363 | .339 | Pilia 2006 |
| C6 Deliberation | Center | .093 | .271 | .364 | .255 | Pilia 2006 |
| E5 Excitement-Seeking | Center | .115 | .198 | .313 | .367 | Pilia 2006 |
| E4 Activity | Center | .161 | .116 | .277 | .581 | Pilia 2006 |
| **OUTSIDE** | | | | | | |
| A5 Modesty | Outside | .122 | .128 | .250 | .488 | Pilia 2006 |
| O6 Values | Outside | .149 | .179 | .328 | .454 | Pilia 2006 |

## Zone-Level Averages

| Zone | N facets | Mean A/(A+D) | SD | Range | Mean A | Mean D |
|---|---|---|---|---|---|---|
| **Primary** (combined) | 10 | **.648** | .239 | .324–1.000 | .146 | .097 |
| -- Primary-E | 3 | .765 | .201 | .637–1.000 | .178 | .063 |
| -- Primary-A | 3 | .689 | .342 | .324–1.000 | .151 | .115 |
| -- Primary-C | 4 | .530 | .179 | .380–.789 | .119 | .110 |
| **Intersection** (combined) | 13 | **.590** | .136 | .356–.854 | .166 | .123 |
| -- CxA (N zone) | 5 | .571 | .118 | .447–.750 | .165 | .129 |
| -- CxE (O zone) | 5 | .624 | .082 | .536–.749 | .193 | .115 |
| -- AxE (Dom zone) | 3 | .566 | .260 | .356–.854 | .124 | .125 |
| **Center** | 5 | **.372** | .124 | .255–.581 | .119 | .210 |
| **Outside** | 2 | .471 | .024 | .454–.488 | .136 | .154 |

## Does the Gradient Hold?

**Prediction:** Primary > Intersection > Center

**Actual:** Primary (.648) > Intersection (.590) > Outside (.471) > Center (.372)

### YES. The gradient holds, and the effect is substantial.

Key numbers:
- Primary-to-Center spread: **.276** (meaningful given within-zone SDs of .12–.24)
- Center facets average **63% nonadditive** genetic variance (A/(A+D) = .372)
- Primary facets average only **35% nonadditive** genetic variance (A/(A+D) = .648)
- The effect is driven particularly by 4 of 5 Center facets having A/(A+D) < .37:
  - C6 Deliberation: **.255**
  - N5 Impulsiveness: **.316**
  - C5 Self-Discipline: **.339**
  - E5 Excitement-Seeking: **.367**
  - E4 Activity (outlier): .581

This contrasts sharply with the BRILLIANCE I H1 test (total heritability by zone), which found negligible spread (.02). The A/(A+D) decomposition reveals structure that total heritability conceals.

## Confirmatory and Contradictory Evidence

### Luciano et al. (2005) — C facets only, N = 431 families

| Facet | A | D | A/(A+D) | Zone |
|---|---|---|---|---|
| C1 Competence | .00 | .37 | .000 | Primary-C |
| C2 Order | .11 | .07 | .611 | Primary-C |
| C3 Dutifulness | .15 | .24 | .385 | Primary-C |
| C4 Achievement Striving | .00 | .28 | .000 | Primary-C |
| C5 Self-Discipline | .00 | .49 | .000 | Center |
| C6 Deliberation | .24 | .10 | .706 | Center |

**Mixed.** C5 confirms the Center prediction (all dominance), but C1 and C4 (Primary) also show all dominance, and C6 contradicts (mostly additive). However, Luciano's CIs encompass zero for all facets except C5 — very low power (91 MZ pairs) vs. Pilia's N = 6,148.

### Jang et al. (1996) — Model selection approach

Facets where ADE model was selected (A = 0, D estimated): N2, E1, **E3**, **E5**, O2, O5, A4, A6. Several are Intersection or Center zone members (E3, E5), consistent with those zones having more nonadditive genetics. But only 250 pairs — extremely low power to distinguish A from D.

## Genetic Correlation Data Relevant to Impulsivity

### N5 Impulsiveness is the most genetically diffuse facet in the corpus (Yamagata 2006, XL)

| Country | N loading | C loading | Cross-domain ratio |
|---|---|---|---|
| Canada | .45 | -.53 | 2.80 |
| Germany | .37 | -.33 | — |
| Japan | .51 | -.52 | — |

N5 genetically loads more on C than on N in 2/3 countries. 66–85% facet-specific genetic variance within N (Jang 2002).

### Other cross-domain genetic bridges at the Center

- E4 Activity: genetic C cross-loading of .48–.54 across three countries (Yamagata 2006)
- E3 Assertiveness: genetically spans four domains simultaneously (E, low-N, low-A, C)
- C4 within-C facet-specific variance (41–43%) is shared with E4 (rG = .775, Jang 2002)

### Not in the repo

- rG between N5 and E5 (both genetically orphaned, both excluded from BFI-2)
- Gustavson et al. (2023) EF vs. impulsivity GWAS (rg = .13)
- Miller & Gizer (2024) GenomicSEM impulsivity factors
- Full 30x30 genetic correlation matrix at the facet level

## Caveats

### 1. Design confound (CRITICAL)

Pilia 2006 is an extended pedigree, not a classical twin study. The dominance component in pedigree models is **confounded with shared sibling environment**. Pilia's authors explicitly note these two models are statistically indistinguishable. If the D component is actually shared environment, the gradient would reflect environmental sharing rather than genetic architecture. However, shared environment is typically near zero for personality in twin studies, making this less likely.

### 2. Single study

The gradient rests entirely on Pilia 2006. Luciano 2005 partially contradicts (for C facets specifically), albeit with far less power. No other study in the repo provides simultaneous A and D estimates for all 30 facets.

### 3. ACE vs. ADE models

Yamagata 2006 (the highest-quality genetic study in the repo) uses AE models only — no dominance estimated. Their genetic factor loadings are informative for structure but cannot test the A/(A+D) prediction. Jang 1996 uses binary ACE/ADE model selection, making continuous A/(A+D) extraction impossible.

### 4. Internal variability

The Primary zone has considerable variability (SD = .239): A2 Straightforwardness (.324) and C3 Dutifulness (.380) look more like Center facets, while E1 Warmth (1.000) and A4 Compliance (1.000) are at ceiling.

### 5. E4 Activity outlier

E4 is the only Center facet with A/(A+D) above .50 (.581). Excluding it drops the Center mean to .319, strengthening the gradient. E4's zone assignment is somewhat forced — its genetics pull strongly toward C (cross-loading .48–.54) and it may be better classified as an Intersection facet.

## Ambiguous Zone Assignments

| Facet | Assigned | Issue |
|---|---|---|
| E4 Activity | Center | A/(A+D) = .581, inconsistent with other Center facets. Genetic profile is more CxE Intersection. |
| A2 Straightforwardness | Primary-A | A/(A+D) = .324 is the lowest of any Primary facet. High D (.279). Does not behave like a "pure A" facet. |
| C3 Dutifulness | Primary-C | A/(A+D) = .380 is very low for Primary. Was in Center in some earlier zone assignments. |
| A3 Altruism | AxE Intersection | A/(A+D) = .854 is very high for Intersection. Genetically diffuse but mostly additive. |
| N4 Self-Consciousness | CxA Intersection | A/(A+D) = .750 is unusually high for Intersection. |
| O4 Actions | CxE Intersection | Zone assignment is arbitrary; O4 is cross-culturally unstable. |
