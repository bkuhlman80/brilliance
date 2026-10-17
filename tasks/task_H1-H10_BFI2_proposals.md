# Proposed H1-H10 Tests Adapted for BFI-2 Facets (Revised with Hansen 2025)

## Rationale

The NEO-PI-R is being replaced by BFI-2 in new research. The Bright Triad model must be testable with BFI-2's 15-facet structure if it is to remain empirically relevant. BFI-2 compresses 30 NEO facets into 15, drops the Edge/outside zone entirely (all 4 outside facets excluded), and redefines some constructs. This document specifies which hypotheses are testable with available BFI-2 data, lists the data sources for each, and notes where tests are blocked.

## BFI-2 Zone Mapping

| BFI-2 Facet | NEO Primary Match | BT v2 Zone | Zone confidence |
|---|---|---|---|
| Anxiety | N1 | Primary | High |
| Depression | N3 | Primary | High |
| Sociability | E2 | Primary (E) | High |
| Assertiveness | E3 | Center triangle | High |
| Energy Level | E4 + E6 | Center triangle | High (blended) |
| Trust | A1 | Center triangle | High |
| Intellectual Curiosity | O5 | Intersection (I×E) | High |
| Aesthetic Sensitivity | O2 + O3 | Intersection (I×E) | High (blended) |
| Creative Imagination | O1 (weak match) | Intersection (I×E) | Moderate |
| Organization | C2 | Intersection (I×ES) | High |
| Productiveness | C1 + C4 + C5 | Intersection (I×ES) | High (blended) |
| Responsibility | C3 + C6 | Intersection (I×ES) | High (blended) |
| Compassion | A3 + A6 + partial A1, E1 | Mixed (Intersection + Center) | Low -- spans zones |
| Respectfulness | A2 + A4 | Intersection (ES×E) | High |
| Emotional Volatility | N2 (redefined) | Intersection (ES×E) | Moderate -- anger content unclear |

### BFI-2 Zone Summary

| Zone | BFI-2 Facets | Count | NEO coverage |
|---|---|---|---|
| **Primary** | Anxiety, Depression, Sociability | 3 | 3 of 5 primary NEO facets |
| **Center triangle** | Assertiveness, Energy Level, Trust | 3 | 3 of 6 center NEO facets (E4+E6 merged; A6 absorbed into Compassion; N5 lost) |
| **Intersection** | Intellectual Curiosity, Aesthetic Sensitivity, Creative Imagination, Organization, Productiveness, Responsibility, Respectfulness, Emotional Volatility | 8 | Covers most intersection NEO facets |
| **Cross-zone** | Compassion | 1 | Spans Intersection + Center |
| **Edge/outside** | -- | 0 | Entire zone dropped |

---

## Available BFI-2 Data Sources

| Source | N | Design | Key data | Quality |
|---|---|---|---|---|
| Hansen et al. (2025) | 2,592 | Norwegian twin registry, BFI-2 | Domain MZ/DZ, domain h² (AE Cholesky), 2 facet h² | M |
| Rammstedt et al. (2026) | 67,927 | PIAAC, 12 countries, BFI-2-S | 15 facet x literacy betas, cross-national SDs | XL |
| Rammstedt et al. (2018) | 365 | German BFI-2, Gf + Gc | 15 facet regression betas for fluid and crystallized | M |
| Danner et al. (2019) | 1,224 | German BFI-2 validation | PCA + ESEM loadings, LS betas, NEO convergent r | L |
| Soto & John (2017) | multiple | BFI-2 development | Complete factor structure, convergent validity | XL |
| Cemalcilar et al. (2021) | 1,009 | Turkish BFI-2, non-WEIRD | Domain-level outcome correlations, congruence | M |
| Ringwald et al. (2024) | 645 | Mexican-origin youth 14-23 | Facet rank-order consistency, developmental data | L |
| Zakrisson et al. (2025) | -- | Swedish BFI-2, 3 language groups | Energy Level C cross-loadings | L |

---

## Proposed Tasks

### H1-BFI2: Heritability by Zone

**Status: PARTIALLY TESTABLE -- Hansen (2025) provides domain-level h² and 2 facet h²**

Hansen et al. (2025) is the first BFI-2 twin study. It provides:

**Domain-level MZ/DZ twin correlations:**
| Domain | MZ | DZ | Falconer h² (2*(MZ-DZ)) |
|---|---|---|---|
| Extraversion | .57 | .16 | .82 |
| Negative Emotionality | .48 | .22 | .52 |
| Agreeableness | .46 | .27 | .38 |
| Conscientiousness | .46 | .27 | .38 |
| Open-mindedness | .64 | .27 | .74 |

**Domain-level AE Cholesky heritability:**
- Open-mindedness h² = .63
- Negative Emotionality h² = .49
- Agreeableness h² = .47

(E and C AE h² not separately reported but derivable from MZ/DZ)

**Facet-level h² (only 2 of 15 modeled):**
- O2 Aesthetic Sensitivity: MZ = .59, DZ = .25, h² = .58
- A1 Compassion: MZ = .36, DZ = .14, h² = .35

**Mapping domains to BT zones -- the fundamental problem:**

BFI-2 domains do not map cleanly to BT zones because each domain contains facets from multiple zones:
- Extraversion contains Primary (Sociability), Center (Assertiveness, Energy Level)
- Negative Emotionality contains Primary (Anxiety, Depression) and Intersection (Emotional Volatility)
- Agreeableness contains Center (Trust), Intersection (Respectfulness), Cross-zone (Compassion)
- Conscientiousness is entirely Intersection (Organization, Productiveness, Responsibility)
- Open-mindedness is entirely Intersection (Intellectual Curiosity, Aesthetic Sensitivity, Creative Imagination)

Only C and O domains are zone-pure (both entirely Intersection). E, N, and A mix Primary, Center, and Intersection content.

**Prediction:** Primary zone h² > Intersection zone h² > Center zone h²

**What Hansen enables:**
1. Rough zone-level estimates using domain h² as proxy (acknowledging domains span zones)
2. Two facet-level data points: Aesthetic Sensitivity (Intersection I×E, h² = .58) and Compassion (Cross-zone, h² = .35)
3. Comparison to NEO-based v2 zone means (Primary .42, Intersection .40, Center .38)

**What remains blocked:** Facet-level h² for 13 of 15 BFI-2 facets. Without these, zone means cannot be computed cleanly.

---

### H2a-BFI2: Facet-Specific Genetic Variance by Zone

**Status: BLOCKED -- requires within-domain genetic factor analysis of BFI-2**

Hansen (2025) does not provide within-domain genetic factor models (i.e., genetic variance decomposition into domain-shared and facet-specific components). This would require multivariate Cholesky or independent pathway models at the facet level.

**Prediction (from NEO mapping):** BFI-2 center facets (Assertiveness, Energy Level, Trust) should have the LEAST specific variance if center content is captured by multiple domain factors. However, the NEO-based result REVERSED this prediction -- center facets had the MOST residual h² (.282).

**What to look for:** Any BFI-2 study with multivariate genetic modeling at the facet level.

---

### H3-BFI2: Cross-Domain Loading Ratios by Zone

**Status: TESTABLE with phenotypic data (Danner 2019)**

**Task:** For each BFI-2 facet, compute the cross-domain loading ratio (sum of absolute cross-loadings / primary loading) from Danner (2019) PCA or ESEM loadings. Compare zone means.

**Available data:**
- Danner et al. (2019): PCA (orthogonal, 5 components) and ESEM loadings for all 15 BFI-2 facets
- Zakrisson et al. (2025): ESEM loadings across 3 Swiss language groups (German, French, Italian)
- Soto & John (2017): US BFI-2 factor structure

**Prediction:** Center-triangle BFI-2 facets (Assertiveness, Energy Level, Trust) should have the highest cross-domain loading ratios, replicating the NEO-based H3 finding (Center 2.17 >> Intersection 1.09 > Primary 1.02).

**Limitation:** Phenotypic cross-loadings (from PCA/ESEM) are NOT genetic cross-loadings. The NEO-based H3 used GENETIC loadings from Pilia (2006, XL). PCA with orthogonal rotation suppresses cross-loadings; ESEM allows them but they are still phenotypic. Expect smaller zone differences than the NEO genetic analysis.

**Enhancement:** Zakrisson (2025) Energy Level cross-loads on C (.23-.24) across all 3 Swiss language groups -- confirming the NEO-based finding that E4 Activity genetically bridges E and C. Computing cross-domain ratios across multiple language groups adds a within-instrument cross-cultural stability test.

---

### H4-BFI2: Direction of Cross-Domain Loadings

**Status: TESTABLE with phenotypic data (Danner 2019)**

**Task:** Using PCA/ESEM loading matrices, test whether intersection BFI-2 facets cross-load toward their predicted parent domains:
- I×ES facets (Organization, Productiveness, Responsibility): Should cross-load negatively on N (ES parent) and positively on O (I parent)
- I×E facets (Intellectual Curiosity, Aesthetic Sensitivity, Creative Imagination): Should cross-load positively on E (E parent) and positively on C (I parent)
- ES×E facets (Respectfulness, Emotional Volatility): Should cross-load negatively on N (ES parent) and positively on E (E parent)

**Available data:**
- Danner (2019): PCA and ESEM cross-loadings
- Zakrisson (2025): Energy Level C cross-loadings (.23-.24) across 3 language groups

**Key question for BT model:** Does the Intelligence parent prediction hold phenotypically? The NEO genetic data showed only 10% hit rate for I-parent cross-loadings. Phenotypic data may be different.

---

### H5-BFI2: Facets Co-Develop Within BT Zones

**Status: PARTIALLY TESTABLE with Ringwald (2024)**

Ringwald provides BFI-2 facet trajectories (ages 14-23) and codevelopment data, though many facet models were nonpositive definite.

**Task:** Using Ringwald's growth parameters, test whether BFI-2 facets within the same BT zone co-develop more than facets across zones.

**Test cases:**
1. Do Assertiveness and Energy Level (both center) co-develop more than Assertiveness and Sociability (center vs primary)?
2. Do the three C facets (Organization, Productiveness, Responsibility -- all I×ES) co-develop more than C facets with O facets (I×E)?

**Available data:** Ringwald (2024, L quality)

**Limitation:** Youth sample (14-23) with instrument switches (BFI to BFI-2). Adult BFI-2 longitudinal data would be far more informative. Several C and A facets could not be modeled.

---

### H6-BFI2: Rank-Order Stability by Zone

**Status: PARTIALLY TESTABLE with Ringwald (2024)**

**Task:** Compute zone means for BFI-2 facet rank-order stability using Ringwald's ages 21-23 values.

**Available data (Ringwald 2024, ages 21-23):**
| Facet | Zone | Stability (r) |
|---|---|---|
| Sociability | Primary | .80 |
| Anxiety | Primary | .77 |
| Depression | Primary | .64 |
| Assertiveness | Center | .76 |
| Energy Level | Center | .70 |
| Trust | Center | .55 |
| Aesthetic Sensitivity | Intersection I×E | .60 |
| Curiosity | Intersection I×E | .57 |
| Imagination | Intersection I×E | .72 |
| Respectfulness | Intersection ES×E | .56 |
| Emotional Volatility | Intersection ES×E | .77 |
| C facets | Intersection I×ES | Unable to model |

**Prediction:** Primary > Intersection > Center

**Limitation:** Youth sample only (ages 14-23). Many C facets couldn't be modeled. Adult BFI-2 stability data would be critical.

---

### H7-BFI2: Brilliance Composite vs Openness for Intelligence

**Status: TESTABLE -- two studies provide direct data**

**Task:** Compare BFI-2 center-triangle facet composite with Openness benchmark for intelligence prediction.

**Available data:**
1. **Rammstedt et al. (2026)** -- N=67,927, 12 countries, BFI-2-S x PIAAC literacy (XL quality)
   - All 15 BFI-2 facet betas available
   - Cross-national SDs for stability analysis
2. **Rammstedt et al. (2018)** -- N=365, German BFI-2 x Gf + Gc (M quality)
   - All 15 facet betas for both fluid and crystallized intelligence

**Prediction:** Center-triangle composite > Openness domain for intelligence prediction.

---

### H8-BFI2: Center-Triangle Predicts Life Satisfaction

**Status: TESTABLE -- Danner (2019)**

**Task:** Compare BFI-2 zone means for life satisfaction prediction.

**Available data:**
- Danner et al. (2019): N=1,224, German BFI-2, all 15 facet regression betas for LS (L quality)
- Cemalcilar et al. (2021): Turkish sample, domain-level LS associations (M quality, supplementary)

**Prediction:** Center composite > Intersection > Primary for LS prediction.

---

### H9-BFI2: Excluded Facets Show Weakest Biological Signatures

**Status: REFRAMED -- BFI-2 exclusion IS the test**

BFI-2 excluded exactly the 4 NEO facets that the BT v2 model assigns to Edge/outside: A5 Modesty, O6 Values, E5 Excitement-Seeking, and O4 Actions. This 4-for-4 convergence between psychometric exclusion criteria and BT biological exclusion criteria is itself a finding.

**Task (reframed):** Document the convergence between BFI-2 exclusions and BT outside-zone assignments. Test whether BFI-2's reduced item set loses criterion prediction for outcomes those facets uniquely predict.

**Available data:** The exclusion convergence is already established. No additional BFI-2-specific data needed for the primary test. For the secondary test (criterion loss), studies comparing BFI-2 vs NEO-PI-R criterion prediction would be needed.

---

### H10-BFI2: Cross-National Stability by Zone

**Status: TESTABLE with Rammstedt (2026)**

**Task:** Compute cross-national SD of personality-ability betas for each BFI-2 zone using Rammstedt (2026) 12-country data.

**Available data:**
- Rammstedt et al. (2026): All 15 facet betas with cross-national SDs (XL quality)
- Cemalcilar et al. (2021): Turkish BFI-2 factor structure congruence coefficients (M quality)

**Prediction:** Primary zone should have the lowest cross-national variability (most stable).

**Note:** This tests cross-national stability of personality-ability RELATIONSHIPS, not genetic loading stability. The NEO-based H10 tested genetic loading stability (VCC, Yamagata cross-country loadings). These are different constructs.

---

## Summary: What BFI-2 Can and Cannot Test

| Hypothesis | NEO Verdict (v2) | BFI-2 Testable? | Key data source | Key change from prior proposal |
|---|---|---|---|---|
| H1 (Heritability) | Not supported | **Partially** -- Hansen domain h² + 2 facet h² | Hansen (2025, M) | Upgraded from BLOCKED -- Hansen provides first BFI-2 twin data |
| H2a (Specific variance) | Not supported (reversed) | **No** -- no within-domain genetic factor analysis | -- | Unchanged |
| H3 (Cross-domain ratios) | Strongly supported | **Partially** -- phenotypic ESEM only | Danner (2019, L) | Unchanged |
| H4 (Loading directions) | Partially supported | **Partially** -- phenotypic only | Danner (2019, L) | Unchanged |
| H5 (Co-development) | Weakly supported | **Partially** -- Ringwald youth data | Ringwald (2024, L) | Unchanged |
| H6 (Stability) | Weakly supported | **Partially** -- Ringwald youth only | Ringwald (2024, L) | Unchanged |
| H7 (Intelligence) | Not supported | **Yes** -- two studies | Rammstedt (2026, XL) | Unchanged |
| H8 (Life satisfaction) | Not supported | **Yes** -- Danner (2019) | Danner (2019, L) | Unchanged |
| H9 (Outside signatures) | Moderately supported | **Reframed** -- BFI-2 exclusion = test | Exclusion convergence | Unchanged |
| H10 (Cross-cultural) | Partially supported | **Partially** -- criterion stability | Rammstedt (2026, XL) | Unchanged |

### The critical gap: BFI-2 genetic architecture

Hansen (2025) partially unlocks H1 but only at the domain level (plus 2 facets). **H1, H2a, H3 (genetic), and H4 (genetic)** all require facet-level multivariate genetic modeling using BFI-2. A BFI-2 twin study with full facet-level Cholesky decomposition would unlock all four hypotheses and determine whether the NEO-based findings -- especially H3's dramatically high center-triangle genetic diffuseness -- replicate with a modern instrument.
