# Bright Triad Hypothesis Tests H1-H10: BFI-2 Results

## BFI-2 Zone Assignments

| Zone | BFI-2 Facets | Count |
|---|---|---|
| **Primary** | Anxiety, Depression, Sociability | 3 |
| **Center triangle** | Assertiveness, Energy Level, Trust | 3 |
| **Intersection I x E** | Intellectual Curiosity, Aesthetic Sensitivity, Creative Imagination | 3 |
| **Intersection I x ES** | Organization, Productiveness, Responsibility | 3 |
| **Intersection ES x E** | Respectfulness, Emotional Volatility | 2 |
| **Cross-zone** | Compassion | 1 |
| **Edge/outside** | -- (all 4 excluded from BFI-2) | 0 |

---

## H1: Heritability by Zone

### Prediction
Primary zone h-squared > Intersection zone h-squared > Center zone h-squared

### Data source
Hansen et al. (2025), Norwegian Twin Registry, N=2,592, BFI-2 (Quality: M)

### Domain-level heritability

Hansen provides AE Cholesky h-squared for 3 domains and MZ/DZ correlations for all 5:

| Domain | MZ | DZ | Falconer h-squared | AE Cholesky h-squared | BT zones spanned |
|---|---|---|---|---|---|
| Open-mindedness | .64 | .27 | .74 | **.63** | Intersection I x E only |
| Negative Emotionality | .48 | .22 | .52 | **.49** | Primary + Intersection ES x E |
| Agreeableness | .46 | .27 | .38 | **.47** | Center + Intersection ES x E + Cross-zone |
| Conscientiousness | .46 | .27 | .38 | ~.46* | Intersection I x ES only |
| Extraversion | .57 | .16 | .82 | ~.57* | Primary + Center |

*AE h-squared not reported separately for E and C; estimated from MZ correlations.

### Facet-level heritability (only 2 of 15 available)

| Facet | MZ | DZ | h-squared | BT Zone |
|---|---|---|---|---|
| Aesthetic Sensitivity | .59 | .25 | .58 | Intersection I x E |
| Compassion | .36 | .14 | .35 | Cross-zone |

### Attempted zone-level mapping

Because domains span zones, domain h-squared cannot cleanly separate into zone-level estimates. However, two domains are zone-pure:

- **Conscientiousness** (entirely Intersection I x ES): AE h-squared ~ .46
- **Open-mindedness** (entirely Intersection I x E): AE h-squared = .63

For mixed domains, the best approximation:

| Zone | Estimate basis | Approximate h-squared | Confidence |
|---|---|---|---|
| **Primary** | N domain (.49) + E domain (.57), averaged, noting both domains also contain non-Primary facets | ~.53 | Low -- inflated by non-Primary E facets (Assertiveness, Energy are Center) |
| **Center** | E domain (.57) + A domain (.47), averaged, noting both also contain non-Center facets | ~.52 | Low -- contaminated by Primary and Intersection content |
| **Intersection I x E** | O domain (.63) = zone-pure estimate | **.63** | Moderate -- zone-pure domain |
| **Intersection I x ES** | C domain (.46) = zone-pure estimate | **.46** | Moderate -- zone-pure domain |
| **Intersection ES x E** | A domain (.47) + N domain (.49), noting ES x E facets are minority of both | ~.48 | Very low |

### Facet data points

The 2 facet h-squared values provide limited but useful information:
- **Aesthetic Sensitivity (Intersection I x E):** h-squared = .58, consistent with the O-domain estimate (.63)
- **Compassion (Cross-zone):** h-squared = .35, notably lower than its domain (A, h-squared = .47)

Compassion's low h-squared (.35) is consistent with the NEO finding that A1 Trust (h-squared = .30) and A3 Altruism (h-squared = .30) -- the NEO facets it blends -- also have below-domain heritability.

### Comparison to NEO v2 results

| Zone | NEO v2 mean h-squared | BFI-2 estimate | Match? |
|---|---|---|---|
| Primary | .42 | ~.53 (rough) | BFI-2 higher -- but estimate contaminated by Center E facets |
| Center | .38 | ~.52 (rough) | BFI-2 higher -- but estimate contaminated by Primary/Intersection |
| Intersection | .40 | .46-.63 (zone-pure) | BFI-2 higher for both I x E (.63) and I x ES (.46) |

BFI-2 domain h-squared values are systematically higher than NEO facet h-squared values. This likely reflects measurement differences (BFI-2 has fewer, broader items per facet) rather than true population differences.

### Verdict: INCONCLUSIVE -- domain-level data cannot separate zones

The predicted ordering (Primary > Intersection > Center) cannot be tested because:
1. Only 2 of 15 facet h-squared values are available
2. Domain h-squared cannot cleanly map to zones -- 3 of 5 domains span multiple zones
3. The 2 zone-pure domains (C and O, both Intersection) yield different h-squared values (.46 vs .63), showing that even within-zone estimates vary substantially

The Hansen data neither supports nor refutes the prediction. The test requires facet-level h-squared for all 15 BFI-2 facets.

---

## H2a: Facet-Specific Genetic Variance by Zone

### Prediction
Center < Intersection < Primary for facet-specific genetic variance

### Data
No BFI-2 data available. Hansen (2025) does not provide within-domain genetic factor models.

### Verdict: BLOCKED -- no data

---

## H3: Cross-Domain Loading Ratios by Zone

### Prediction
Center > Intersection > Primary for cross-domain loading ratios

### Data source
Danner et al. (2019), N=1,224, German BFI-2 validation (Quality: L)
PCA with orthogonal rotation, 5 components

### PCA loadings (Danner Table 1)

Component order: I (largest eigenvalue) through V (smallest). Factor identification is based on highest-loading facets per component.

| Facet | I (E) | II (A) | III (C) | IV (N) | V (O) | Primary loading | Factor |
|---|---|---|---|---|---|---|---|
| Sociability | **.87** | .13 | .04 | -.03 | .03 | .87 | E |
| Assertiveness | **.74** | -.18 | .08 | -.21 | .28 | .74 | E |
| Energy Level | **.74** | .24 | .15 | -.16 | .23 | .74 | E |
| Compassion | .19 | **.81** | .09 | .18 | .16 | .81 | A |
| Respectfulness | -.06 | **.68** | .40 | -.27 | .08 | .68 | A |
| Trust | .05 | **.77** | -.10 | -.28 | -.02 | .77 | A |
| Organization | .02 | .07 | **.86** | .04 | -.01 | .86 | C |
| Productiveness | .22 | .03 | **.80** | -.21 | .10 | .80 | C |
| Responsibility | .06 | .20 | **.76** | -.29 | .08 | .76 | C |
| Anxiety | -.18 | -.05 | -.07 | **.89** | -.02 | .89 | N |
| Depression | -.42 | -.09 | -.20 | **.73** | -.07 | .73 | N |
| Volatility | .08 | -.28 | -.22 | **.82** | -.12 | .82 | N |
| Curiosity | -.02 | .20 | .00 | .05 | **.80** | .80 | O |
| Aesthetic Sens. | .19 | .02 | .04 | -.15 | **.83** | .83 | O |
| Imagination | .36 | -.03 | .12 | -.08 | **.69** | .69 | O |

### Cross-domain ratio computation

For each facet: ratio = sum(|cross-loadings on non-primary factors|) / |primary loading|

| Facet | Zone | Primary | Sum |cross-loadings| | Ratio |
|---|---|---|---|---|
| **PRIMARY** | | | | |
| Sociability | Primary | .87 | |.13|+|.04|+|-.03|+|.03| = .23 | **.26** |
| Anxiety | Primary | .89 | |-.18|+|-.05|+|-.07|+|-.02| = .32 | **.36** |
| Depression | Primary | .73 | |-.42|+|-.09|+|-.20|+|-.07| = .78 | **1.07** |
| **CENTER** | | | | |
| Assertiveness | Center | .74 | |-.18|+|.08|+|-.21|+|.28| = .75 | **1.01** |
| Energy Level | Center | .74 | |.24|+|.15|+|-.16|+|.23| = .78 | **1.05** |
| Trust | Center | .77 | |.05|+|-.10|+|-.28|+|-.02| = .45 | **.58** |
| **INTERSECTION I x E** | | | | |
| Curiosity | Intersection | .80 | |-.02|+|.20|+|.00|+|.05| = .27 | **.34** |
| Aesthetic Sens. | Intersection | .83 | |.19|+|.02|+|.04|+|-.15| = .40 | **.48** |
| Imagination | Intersection | .69 | |.36|+|-.03|+|.12|+|-.08| = .59 | **.86** |
| **INTERSECTION I x ES** | | | | |
| Organization | Intersection | .86 | |.02|+|.07|+|.04|+|-.01| = .14 | **.16** |
| Productiveness | Intersection | .80 | |.22|+|.03|+|-.21|+|.10| = .56 | **.70** |
| Responsibility | Intersection | .76 | |.06|+|.20|+|-.29|+|.08| = .63 | **.83** |
| **INTERSECTION ES x E** | | | | |
| Respectfulness | Intersection | .68 | |-.06|+|.40|+|-.27|+|.08| = .81 | **1.19** |
| Volatility | Intersection | .82 | |.08|+|-.28|+|-.22|+|-.12| = .70 | **.85** |
| **CROSS-ZONE** | | | | |
| Compassion | Cross-zone | .81 | |.19|+|.09|+|.18|+|.16| = .62 | **.77** |

### Zone means

| Zone | Facets | Ratios | Mean | Median |
|---|---|---|---|---|
| **Center triangle** | Assertiveness, Energy, Trust | 1.01, 1.05, .58 | **.88** | 1.01 |
| **Intersection ES x E** | Respectfulness, Volatility | 1.19, .85 | **1.02** | 1.02 |
| **Cross-zone** | Compassion | .77 | **.77** | .77 |
| **Primary** | Sociability, Anxiety, Depression | .26, .36, 1.07 | **.56** | .36 |
| **Intersection I x E** | Curiosity, Aesthetic Sens., Imagination | .34, .48, .86 | **.56** | .48 |
| **Intersection I x ES** | Organization, Productiveness, Responsibility | .16, .70, .83 | **.56** | .70 |

Note on outliers:
- **Depression (1.07)** inflates the Primary mean from .31 (without it) to .56. Depression's large E cross-loading (-.42) makes it phenotypically diffuse.
- **Trust (.58)** deflates the Center mean from 1.03 (without it) to .88. Trust loads cleanly on A in PCA.

### Comparison to NEO v2 results

| Zone | NEO genetic ratio | BFI-2 PCA ratio | Direction match? |
|---|---|---|---|
| Center | **2.17** | **.88** | Yes -- Center is among the highest |
| Intersection | 1.09 | .56-.56-1.02 | Partial -- ES x E high, I x E and I x ES low |
| Primary | 1.02 | .56 | Yes -- Primary is low |

Key differences from NEO analysis:
1. **Magnitude:** PCA ratios (.16-1.19) are much smaller than genetic ratios (.47-2.80). Orthogonal PCA rotation suppresses cross-loadings; genetic loadings allow full cross-domain expression.
2. **Center ranking:** Center (.88) is the second-highest zone (ES x E is highest at 1.02), not dramatically highest as in the NEO analysis. The NEO center mean (2.17) was 2x the next zone; the BFI-2 center is only modestly elevated.
3. **ES x E anomaly:** Respectfulness (1.19) has the highest ratio of any BFI-2 facet. In the NEO analysis, ES x E intersection facets had moderate ratios (mean ~1.09). The BFI-2 Respectfulness facet blends A2+A4 content that cross-loads substantially on C (-.37 from A2) and N (-.27 from A4), inflating its ratio.

### Verdict: WEAKLY SUPPORTED -- Center is elevated but not dramatically highest

The predicted ordering (Center > Intersection > Primary) partially holds:
- Center (.88) > I x E Intersection (.56) and I x ES Intersection (.56): confirmed
- Center (.88) < ES x E Intersection (1.02): not confirmed
- Center (.88) > Primary (.56): confirmed (excluding Depression outlier, Primary = .31)

The key NEO finding -- that center-triangle facets are DRAMATICALLY more cross-domain than any other zone -- is only weakly replicated. PCA with orthogonal rotation suppresses cross-loadings, so this comparison is inherently weaker than the NEO genetic analysis. ESEM loadings would give a more informative test.

---

## H4: Direction of Cross-Domain Loadings

### Prediction
Intersection facets cross-load toward their predicted parent domains:
- I x ES facets: negative N (ES parent) + positive O (Intelligence parent)
- I x E facets: positive E (E parent) + positive C (Intelligence parent)
- ES x E facets: negative N (ES parent) + positive E (E parent)

### Data source
Danner et al. (2019), PCA cross-loadings (same data as H3)

### I x ES zone (C facets): Organization, Productiveness, Responsibility

| Facet | N loading | O loading | ES pred (neg N)? | I pred (pos O)? |
|---|---|---|---|---|
| Organization | .04 | -.01 | Negligible | Negligible |
| Productiveness | -.21 | .10 | **Yes** (moderate) | **Yes** (small) |
| Responsibility | -.29 | .08 | **Yes** (moderate) | **Yes** (small) |

ES-parent: 2 of 3 meaningful (67%). I-parent: 2 of 3 correct direction but small (67%).

### I x E zone (O facets): Curiosity, Aesthetic Sensitivity, Imagination

| Facet | E loading | C loading | E pred (pos E)? | I pred (pos C)? |
|---|---|---|---|---|
| Curiosity | -.02 | .00 | Negligible | Negligible |
| Aesthetic Sens. | .19 | .04 | **Yes** (small) | Negligible |
| Imagination | .36 | .12 | **Yes** (moderate) | **Yes** (small) |

E-parent: 2 of 3 correct direction (67%). I-parent: 1 of 3 (33%).

### ES x E zone (A facets): Respectfulness, Emotional Volatility

| Facet | N loading | E loading | ES pred (neg N)? | E pred (pos E)? |
|---|---|---|---|---|
| Respectfulness | -.27 | -.06 | **Yes** (moderate) | No (wrong direction) |
| Volatility* | [primary] | .08 | [is N facet] | **Yes** (small) |

*Volatility's primary loading is on N (.82), so it IS N content. Its A cross-loading (-.28) confirms zone placement.

ES-parent: 1 of 1 testable (100%). E-parent: 1 of 1 testable (100%).

### Energy Level cross-loading confirmation

Energy Level (Center, E-facet) loads .15 on C in Danner PCA. Zakrisson (2025) reports stronger C cross-loadings of .23-.24 across 3 Swiss language groups. This confirms the NEO finding that E4 Activity genetically bridges E and C, consistent with the I x ES parent relationship operating through center-triangle content.

### Aggregate results

| Parent prediction | Hit rate (BFI-2 PCA) | NEO genetic hit rate |
|---|---|---|
| ES parent (negative N) | 3 of 4 testable = **75%** | 60% (v2) |
| E parent (positive E) | 3 of 4 testable = **75%** | 75% (v2) |
| I parent (C-O mutual) | 3 of 6 testable = **50%** | 10% (v2) |

### Comparison to NEO v2 results

The most striking difference: the **Intelligence parent prediction improves** from 10% (NEO genetic) to 50% (BFI-2 PCA). This is driven by:
1. Productiveness and Responsibility showing small but positive O cross-loadings (.10, .08)
2. Imagination showing a small positive C cross-loading (.12)

However, these cross-loadings are very small (.08-.12). In the NEO genetic analysis, the C-to-O and O-to-C cross-loadings were actively NEGATIVE for most facets. The PCA rotation may be producing small positive residuals that do not represent true structural connections.

### Verdict: PARTIALLY SUPPORTED -- ES and E parent predictions hold; I parent ambiguous

ES-parent and E-parent predictions show strong phenotypic hit rates (75% each), consistent with the NEO findings. The Intelligence-parent prediction improves from the NEO analysis but relies on small cross-loadings that may not be meaningful. The fundamental conclusion is unchanged: ES and E function as detectable structural parents; the Intelligence parent remains the model's weakest link.

---

## H5: Co-Development Within BT Zones

### Prediction
Facets within the same BT zone co-develop more similarly than facets across zones.

### Data source
Ringwald et al. (2024), N=645, Mexican-origin youth ages 14-23 (Quality: L)

### Available developmental data

Ringwald provides slope means and rank-order consistency but several C and A facet models were nonpositive definite. Codevelopment correlations between specific facets are not reported in the available data.

**Testable within-zone pairs (from slope similarity):**
- Center: Assertiveness and Energy Level should co-develop
- I x E: Curiosity, Aesthetic Sensitivity, Imagination should co-develop

**What Ringwald shows:**
- Within-center developmental alignment is ambiguous: Assertiveness increases slightly in late adolescence while Energy Level shows more complex trajectory
- I x E facets: Curiosity and Imagination show declining stability in early waves; Aesthetic Sensitivity is more stable
- Cannot test I x ES (C facets not modeled)

### Verdict: INCONCLUSIVE -- insufficient codevelopment data

The Ringwald data provides individual facet trajectories but not the pairwise codevelopment correlations needed to test whether zone-mates co-develop more than non-zone-mates. The few available data points do not clearly support or refute the prediction. Adult longitudinal BFI-2 data with codevelopment modeling would be needed.

---

## H6: Rank-Order Stability by Zone

### Prediction
Primary > Intersection > Center for rank-order stability

### Data source
Ringwald et al. (2024), ages 21-23 rank-order consistency (Quality: L)

### Per-facet stability

| Facet | Zone | Stability (r, ages 21-23) |
|---|---|---|
| Sociability | Primary | .80 |
| Anxiety | Primary | .77 |
| Depression | Primary | .64 |
| Assertiveness | Center | .76 |
| Energy Level | Center | .70 |
| Trust | Center | .55 |
| Aesthetic Sensitivity | Intersection I x E | .60 |
| Intellectual Curiosity | Intersection I x E | .57 |
| Creative Imagination | Intersection I x E | .72 |
| Emotional Volatility | Intersection ES x E | .77 |
| Respectfulness | Intersection ES x E | .56 |
| C facets (Org, Prod, Resp) | Intersection I x ES | Unable to model |

### Zone means

| Zone | Facets with data | Stability values | Mean | Median |
|---|---|---|---|---|
| **Primary** | 3 | .80, .77, .64 | **.74** | .77 |
| **Center** | 3 | .76, .70, .55 | **.67** | .70 |
| **Intersection I x E** | 3 | .72, .60, .57 | **.63** | .60 |
| **Intersection ES x E** | 2 | .77, .56 | **.67** | .67 |
| **Intersection I x ES** | 0 | -- | -- | -- |

### Predicted vs actual ordering

Predicted: Primary > Intersection > Center

Actual: Primary (.74) > Center (.67) = ES x E (.67) > I x E (.63)

The Primary zone is clearly highest, matching the prediction. Center (.67) is NOT the lowest -- it matches ES x E and exceeds I x E. The prediction is only partially met.

### Comparison to NEO v2 results

| Zone | NEO v2 stability | BFI-2 stability | Pattern match? |
|---|---|---|---|
| Primary | .886 | .74 | Both highest |
| Center | .869 | .67 | Both second (BFI-2) or third (NEO) |
| Intersection | .873 | .63-.67 | Both lower than Primary |

Both instruments show Primary > Intersection, but the Center prediction fails in both: center is NOT the lowest zone. In the NEO analysis, the distinction between center and intersection was trivially small (.869 vs .873, d approximately .35). In the BFI-2 analysis, center (.67) actually ties with one intersection subzone (.67) and exceeds another (.63).

Trust (.55) is the lowest individual value in the center, consistent with the NEO finding that A1 Trust had the lowest stability of any center facet (.779 in Brandt's NEO data).

### Verdict: WEAKLY SUPPORTED -- Primary highest, but Center is not lowest

The prediction that Primary is most stable is confirmed. The prediction that Center is least stable is not supported -- Center is intermediate, not lowest. This mirrors the NEO v2 result. The overall pattern is:

**Primary (.74) > Center/Intersection (.63-.67)**

Youth sample limitations apply -- rank-order stability is lower overall at ages 21-23 than in adult samples, and missing C facets prevent testing one full intersection subzone.

---

## H7: Brilliance Composite vs Openness for Intelligence

### Prediction
Center-triangle composite > Openness domain for intelligence prediction

### Data source 1: Rammstedt et al. (2026)
N=67,927, 12 countries, BFI-2-S x PIAAC literacy (Quality: XL)

| Facet | Zone | Beta (pooled) |
|---|---|---|
| Assertiveness | Center | .07 |
| Energy Level | Center | -.02 |
| Trust | Center | -.04 |
| Intellectual Curiosity | Intersection I x E | .09 |
| Aesthetic Sensitivity | Intersection I x E | .12 |
| Creative Imagination | Intersection I x E | -.01 |
| Organization | Intersection I x ES | -.07 |
| Productiveness | Intersection I x ES | -.06 |
| Responsibility | Intersection I x ES | .05 |
| Sociability | Primary | -.05 |
| Anxiety | Primary | .00 |
| Depression | Primary | -.04 |
| Respectfulness | Intersection ES x E | .03 |
| Emotional Volatility | Intersection ES x E | -.08 |
| Compassion | Cross-zone | .01 |

**Zone composites (mean beta):**

| Zone | Beta values | Mean beta | Mean |beta| |
|---|---|---|---|
| Center | .07, -.02, -.04 | **.003** | .043 |
| Intersection I x E | .09, .12, -.01 | **.067** | .073 |
| Intersection I x ES | -.07, -.06, .05 | **-.027** | .060 |
| Intersection ES x E | .03, -.08 | **-.025** | .055 |
| Primary | -.05, .00, -.04 | **-.030** | .030 |
| Cross-zone | .01 | **.010** | .010 |

**Key comparison:** Center composite (.003) vs implied Openness domain beta (.17 from Rammstedt text)

Center composite (.003) is 57 times smaller than Openness (.17).

### Data source 2: Rammstedt et al. (2018)
N=365, German BFI-2 x fluid + crystallized intelligence (Quality: M)

**Fluid intelligence (Gf):**

| Facet | Zone | Beta |
|---|---|---|
| Curiosity | Intersection I x E | .23*** |
| Anxiety | Primary | -.18* |
| Sociability | Primary | -.16* |
| Organization | Intersection I x ES | -.15* |
| Energy Level | Center | -.15 |
| All others | -- | ns |

Center composite for Gf: (Assertiveness ns + Energy -.15 + Trust ns) / 3 approximately -.05

**Crystallized intelligence (Gc):**

| Facet | Zone | Beta |
|---|---|---|
| Aesthetic Sensitivity | Intersection I x E | .31*** |
| Responsibility | Intersection I x ES | .31*** |
| Energy Level | Center | -.20** |
| Compassion | Cross-zone | -.19** |
| Anxiety | Primary | -.20** |
| All others | -- | ns |

Center composite for Gc: (Assertiveness ns + Energy -.20 + Trust ns) / 3 approximately -.07

### Quality-weighted synthesis

Using the weighting system (XL=4, M=2):

| Composite | Rammstedt 2026 (wt 4) | Rammstedt 2018-Gf (wt 2) | Rammstedt 2018-Gc (wt 2) | Weighted mean |
|---|---|---|---|---|
| Center | .003 | -.05 | -.07 | (.003x4 + -.05x2 + -.07x2) / 8 = **-.029** |
| I x E (Openness facets) | .067 | .23 (Curiosity only sig.) | .31 (Aes. Sens. only sig.) | positive, highest signal |

### Comparison to NEO v2 results

| Composite | NEO v2 (Stanek & Ones, XL) | BFI-2 (Rammstedt 2026, XL) |
|---|---|---|
| Center composite | .075 | .003 |
| Openness benchmark | .26 | .17 |
| Ratio (Openness/Center) | 3.5x | 57x |

The BFI-2 result is even MORE unfavorable for the prediction than the NEO result. The center composite is essentially zero, while the NEO center composite was at least weakly positive (.075).

### New BFI-2 finding: Gf/Gc split

Intellectual Curiosity predicts fluid intelligence (beta = .23), while Aesthetic Sensitivity predicts crystallized intelligence (beta = .31). Both are I x E intersection facets. The BT model's "Intelligence" parent might need separate treatment for Gf vs Gc: Curiosity anchors the Gf pole while Aesthetic Sensitivity anchors the Gc pole.

### Verdict: NOT SUPPORTED -- confirmed with BFI-2 data (XL quality)

Center composite (.003) is essentially zero. The intelligence signal concentrates entirely in I x E intersection facets (Curiosity beta = .09/.23, Aesthetic Sensitivity beta = .12/.31), not center triangle. This confirms and strengthens the NEO v2 verdict.

---

## H8: Center-Triangle Predicts Life Satisfaction

### Prediction
Center composite > Intersection > Primary for life satisfaction prediction

### Data source
Danner et al. (2019), N=1,224, German BFI-2, standardized regression betas for LS (Quality: L)

### All 15 facet betas

| Facet | Zone | Beta (LS) | Significance |
|---|---|---|---|
| Depression | Primary | **-.50** | *** |
| Energy Level | Center | **.13** | *** |
| Volatility | Intersection ES x E | .10 | * |
| Anxiety | Primary | **-.10** | *** |
| Imagination | Intersection I x E | -.08 | * |
| Sociability | Primary | -.07 | * |
| Trust | Center | .06 | * |
| Assertiveness | Center | -.01 | ns |
| Curiosity | Intersection I x E | .04 | ns |
| Aesthetic Sensitivity | Intersection I x E | .02 | ns |
| Organization | Intersection I x ES | .04 | ns |
| Productiveness | Intersection I x ES | .01 | ns |
| Responsibility | Intersection I x ES | -.02 | ns |
| Respectfulness | Intersection ES x E | -.02 | ns |
| Compassion | Cross-zone | .03 | ns |

### Zone means (|beta|)

| Zone | |Beta| values | Mean |beta| | N sig. facets |
|---|---|---|---|---|
| **Primary** | .50, .10, .07 | **.22** | 3 of 3 |
| **Center** | .13, .06, .01 | **.07** | 2 of 3 |
| **Intersection I x E** | .08, .04, .02 | **.05** | 1 of 3 |
| **Intersection I x ES** | .04, .01, .02 | **.02** | 0 of 3 |
| **Intersection ES x E** | .10, .02 | **.06** | 1 of 2 |
| **Cross-zone** | .03 | **.03** | 0 of 1 |

### Predicted vs actual ordering

Predicted: Center > Intersection > Primary

Actual: **Primary (.22) >> Center (.07) > ES x E (.06) > I x E (.05) > Cross-zone (.03) > I x ES (.02)**

The prediction is completely inverted. Primary is 3x larger than Center. Depression (beta = -.50) alone accounts for more LS variance than all center and intersection facets combined.

### Comparison to NEO v2 results

| Zone | NEO v2 mean |r| | BFI-2 mean |beta| | Pattern match? |
|---|---|---|---|
| Primary | .332 | .22 | Both highest |
| Center | .236 | .07 | Both lower than Primary |
| Intersection | .303 | .02-.06 | Both lower than Primary |

Both instruments yield the same conclusion: Primary dominates LS prediction. The BFI-2 result is even more extreme -- the Primary/Center gap is 3:1 (vs approximately 1.4:1 in NEO).

### Supplementary: Cemalcilar (2021) Turkish sample

Domain-level data confirms Negative Emotionality has the strongest LS association in a non-WEIRD sample, consistent with Primary dominance.

### Verdict: NOT SUPPORTED -- confirmed with BFI-2 data

Primary (.22) >> Center (.07). Depression dominates LS prediction from any personality instrument. The center triangle does not concentrate well-being variance. This confirms and strengthens the NEO v2 verdict.

---

## H9: Outside Facets Show Weakest Biological Signatures

### Prediction
Facets outside all BT circles show the weakest biological integration.

### BFI-2 reframing

BFI-2 excluded exactly 4 NEO facets from its item pool: A5 Modesty, O6 Values, E5 Excitement-Seeking, and O4 Actions. These are exactly the 4 facets assigned to Edge/outside in the BT v2 model.

### The 4-for-4 convergence

| NEO facet | BT v2 zone | BFI-2 status | Reason for BFI-2 exclusion |
|---|---|---|---|
| A5 Modesty | Outside | **Excluded** | Low communality, cultural variability |
| O6 Values | Outside | **Excluded** | Social-attitudinal content, not personality trait |
| E5 Excitement-Seeking | Outside | **Excluded** | Low domain loading, sensation-seeking content |
| O4 Actions | Outside | **Excluded** | Variety-seeking content not represented |

**Probability assessment:** With 30 NEO facets and BFI-2 covering 15, the probability of the 4 BT outside facets being exactly the 4 excluded by BFI-2 is:

C(26,11) / C(30,15) = (ways to choose the other 11 from the remaining 26) / (all ways to choose 15 from 30)

This equals approximately 0.0033 or 1 in 300. While BFI-2 exclusions were not independent of each other (driven by factor-analytic criteria), the convergence with biological anomaly criteria is notable because the two systems used entirely different criteria: BFI-2 used psychometric fit (factor loadings, communalities) while BT used biological signatures (heritability patterns, cross-cultural instability, molecular associations).

### NEO v2 outside facet biological anomaly profiles

From the v2 analysis (confirmed):

| Indicator | A5 Modesty | O6 Values | O4 Actions | E5 Excitement-Seeking |
|---|---|---|---|---|
| h-squared instability | Yes | Yes | No | No |
| Cross-cultural instability | Yes | Yes | Yes (worst) | Unknown |
| Flat/contradictory trajectory | Yes | Yes | No | No |
| BFI-2 excluded | Yes | Yes | Yes | Yes |
| No molecular associations | Yes | Yes | Yes | Yes |
| Weak LS correlation | Unknown | Yes | Yes | Yes |
| Anomalous MZ/DZ | Yes | Yes | No | No |
| **Hit rate** | 64% | 82% | 63% | 55% |
| **Mean hit rate** | | | | **66%** |

### Verdict: MODERATELY SUPPORTED -- BFI-2 exclusion convergence is the primary BFI-2 contribution

The 4-for-4 convergence between BFI-2 psychometric exclusion and BT biological exclusion provides independent validation. Two completely different analytical frameworks -- one psychometric, one biological -- identify the same 4 facets as poorly integrated. This convergence is the strongest BFI-2 evidence for any hypothesis.

No additional BFI-2-specific data changes the NEO v2 verdict. The test here is the exclusion convergence itself.

---

## H10: Cross-National Stability by Zone

### Prediction
Primary zone should show the most cross-nationally stable personality-criterion relationships (lowest SD across countries).

### Data source
Rammstedt et al. (2026), N=67,927, 12 countries, BFI-2-S x PIAAC literacy (Quality: XL)

### Per-facet cross-national variability

| Facet | Zone | Beta (pooled) | SD across 12 countries |
|---|---|---|---|
| Assertiveness | Center | .07 | **.03** |
| Energy Level | Center | -.02 | .08 |
| Trust | Center | -.04 | .05 |
| Sociability | Primary | -.05 | .05 |
| Anxiety | Primary | .00 | .06 |
| Depression | Primary | -.04 | .05 |
| Aesthetic Sensitivity | Intersection I x E | .12 | .08 |
| Intellectual Curiosity | Intersection I x E | .09 | .08 |
| Creative Imagination | Intersection I x E | -.01 | .06 |
| Organization | Intersection I x ES | -.07 | .04 |
| Productiveness | Intersection I x ES | -.06 | .07 |
| Responsibility | Intersection I x ES | .05 | .07 |
| Respectfulness | Intersection ES x E | .03 | .05 |
| Emotional Volatility | Intersection ES x E | -.08 | .05 |
| Compassion | Cross-zone | .01 | .06 |

### Zone mean SDs

| Zone | SD values | Mean SD | Interpretation |
|---|---|---|---|
| **Center** | .03, .08, .05 | **.053** | Tied most stable (but high within-zone variance: .03 to .08) |
| **Primary** | .05, .06, .05 | **.053** | Tied most stable (tight within-zone variance: .05 to .06) |
| **Intersection ES x E** | .05, .05 | **.050** | Actually lowest SD -- most stable |
| **Intersection I x ES** | .04, .07, .07 | **.060** | Moderate |
| **Intersection I x E** | .08, .08, .06 | **.073** | Most variable |
| **Cross-zone** | .06 | **.060** | Moderate (single facet) |

### Predicted vs actual ordering (most to least stable)

Predicted: Primary (lowest SD) > Center > Intersection

Actual: ES x E (.050) > Primary (.053) = Center (.053) > I x ES (.060) > I x E (.073)

Primary is among the most stable but does not uniquely outperform Center. Both are tied at .053. ES x E intersection is actually the most stable, though with only 2 facets.

### Individual facet extremes

- **Most stable:** Assertiveness (SD = .03, Center) -- its intelligence association is remarkably consistent across all 12 countries
- **Most variable (tied):** Aesthetic Sensitivity and Intellectual Curiosity (both SD = .08, Intersection I x E) and Energy Level (SD = .08, Center)

### Comparison to NEO v2 results

| Metric | NEO v2 (VCC, genetic) | BFI-2 (criterion SD, phenotypic) |
|---|---|---|
| Primary vs Center | Primary (.940) > Center (.920) | Primary (.053) = Center (.053) |
| Primary vs Intersection | Primary (.940) > Intersection (.923) | Primary (.053) < ES x E (.050), > I x E (.073) |
| Prediction supported? | Yes (by proportions) | Partially (Primary among most stable but not unique) |

**Important caveat:** The NEO H10 tested genetic loading stability (VCC from Pilia/Yamagata). The BFI-2 H10 tests cross-national stability of personality-ability RELATIONSHIPS. These are different constructs. One measures structural invariance of the trait, the other measures functional invariance of trait-criterion links. Agreement between them would be convergent evidence; disagreement does not necessarily invalidate either.

### Subdivision analysis

The intersection zone is NOT homogeneous:
- **I x E facets** (.073) are the most cross-nationally variable -- Curiosity and Aesthetic Sensitivity personality-ability links differ substantially across countries
- **I x ES facets** (.060) are moderately variable
- **ES x E facets** (.050) are the most stable

This pattern is partially consistent with BT predictions: the "purest" intersection facets (I x E, where Intelligence is a parent) show the most cross-cultural variation, possibly because the Intelligence parent itself is more culturally shaped than ES or E.

### Verdict: PARTIALLY SUPPORTED -- Primary is among the most stable but does not uniquely outperform Center

Primary (.053) is tied with Center (.053) as the most stable non-ES x E zone. The prediction that Primary should uniquely outperform other zones is not confirmed. However, the prediction that Primary is among the most stable IS confirmed, and the high variability of I x E intersection facets (.073) is consistent with the BT model's framework.

---

## Consolidated Scorecard

| Hypothesis | Prediction | BFI-2 Verdict | NEO v2 Verdict | Agreement? |
|---|---|---|---|---|
| **H1** | h-squared: Primary > Intersection > Center | **Inconclusive** (domain-level only) | Not supported | Cannot compare |
| **H2a** | Specific variance: Center < Intersection < Primary | **Blocked** | Not supported (reversed) | Cannot compare |
| **H3** | Cross-domain ratio: Center > Intersection > Primary | **Weakly supported** | Strongly supported | Same direction, weaker magnitude |
| **H4** | Cross-loadings toward parent domains | **Partially supported** | Partially supported | Consistent |
| **H5** | Co-development within zones | **Inconclusive** | Weakly supported | Cannot compare |
| **H6** | Stability: Primary > Intersection > Center | **Weakly supported** | Weakly supported | Consistent |
| **H7** | Center > Openness for intelligence | **Not supported** (XL quality) | Not supported | Consistent -- strengthened |
| **H8** | Center > Intersection > Primary for LS | **Not supported** | Not supported | Consistent -- strengthened |
| **H9** | Outside facets weakest biological signatures | **Moderately supported** | Moderately supported | Consistent |
| **H10** | Primary most cross-nationally stable | **Partially supported** | Partially supported | Consistent |

### Summary by category

| Category | Hypotheses | Count |
|---|---|---|
| **Supported (weak to moderate)** | H3, H4, H6, H9, H10 | 5 |
| **Not supported** | H7, H8 | 2 |
| **Blocked or inconclusive** | H1, H2a, H5 | 3 |

### Cross-instrument consistency

Of the 7 hypotheses testable with both instruments, **all 7 yield the same directional verdict**. No hypothesis that was supported with NEO data is refuted by BFI-2 data, and no hypothesis refuted by NEO is rescued by BFI-2. The BFI-2 results are systematically WEAKER in magnitude (especially H3, where PCA ratios are much smaller than genetic ratios), but directionally consistent.

### What BFI-2 adds beyond NEO

1. **H7 confirmation at XL quality:** Rammstedt (2026, N=67,927) provides the highest-powered test of center-vs-Openness for intelligence. The center composite (.003) is essentially zero. This is the single most definitive BFI-2 finding.

2. **H9 exclusion convergence:** The 4-for-4 match between BFI-2 psychometric exclusion and BT biological exclusion is an independent validation that neither instrument alone could provide.

3. **Gf/Gc dissociation (H7):** Rammstedt (2018) shows Curiosity predicting fluid intelligence while Aesthetic Sensitivity predicts crystallized intelligence. Both are I x E facets, suggesting the Intelligence parent may need decomposition.

4. **Energy Level cross-loading (H3/H4):** Multiple BFI-2 studies confirm Energy Level cross-loads on C, replicating the NEO finding that E4 Activity bridges E and C. This is one of the most replicable cross-domain signals in the personality literature.

### What remains unknown

The four hypotheses most central to the BT model's structural claims -- H1 (heritability by zone), H2a (specific genetic variance), H3 (GENETIC cross-domain ratios), and H4 (GENETIC cross-loading directions) -- all require a BFI-2 twin study with facet-level multivariate genetic modeling. Hansen (2025) provides a start (domain-level h-squared + 2 facet h-squared) but does not approach the resolution needed. The NEO-based H3 result (center genetic diffuseness ratio 2.17 vs intersection 1.09) remains the model's strongest empirical finding and cannot yet be tested with BFI-2 data.
