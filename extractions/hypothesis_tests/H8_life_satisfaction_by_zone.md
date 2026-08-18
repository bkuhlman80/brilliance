# Task H8: Center-Triangle Facets Predict Life Satisfaction More Strongly Than Peripheral Facets

## Data Sources and Weighting

| Study | Quality | Weight | Design | N | Measure | Coverage |
|---|---|---|---|---|---|---|
| Haehner et al. (2025) | L | 3 | Cross-sectional, probability sample, 3 languages | 4,492 | BFAS aspects × LS (zero-order r) | 10 aspects — 4 with specific LS values; 6 described qualitatively |
| Sun et al. (2017) | Unrated | 2 | Cross-sectional, MTurk, 2 samples | 706 | BFAS aspects × 13 WB dimensions (semipartial r) | 10 aspects — mean semipartials across all WB, partialing complementary aspect |
| Røysamb et al. (2018) | M | 2 | Twin study | 1,516 | NEO-PI-R facets × LS (zero-order r) | All 30 facets in Table 2; only 5 specific values transcribed in extractions |
| Schimmack et al. (2004) | Unrated | 1 | 4 studies, students | 136 (S1) | NEO-PI-R N+E facets × LS (zero-order r) | 12 facets (N and E domains only) |

Notes on measure types:
- Haehner reports zero-order correlations with life satisfaction (SWLS). Primary source.
- Sun reports semipartial correlations (partialing complementary aspect) averaged across 13 well-being dimensions. These are NOT zero-order LS correlations — they underestimate total association with LS specifically and remove shared within-domain variance. Used as supplementary.
- Røysamb reports zero-order r with SWLS. High-value source but full 30-facet table was not transcribed into the extraction files. Specific values cited in dissociation flag discussions.
- Schimmack reports zero-order r with SWLS. Small student sample, N and E facets only. Used for facet-level N/E coverage.

## Zone Assignments (Diagram III — consistent with H1–H7)

Primary cores (8): N1, N3, N6, N4, A1 (ES core) + E2, E1, E5 (E core)
Intersection zones (12): C1, C4, C2, C6, N5 (I×ES) + O2, O3, O1, O5 (I×E) + A2, A4, N2 (ES×E)
Center triangle (7): E3, E4, E6, A3, C3, A6, O4
Outside (3): A5, O6, C5

Aspect-to-zone mapping (from task instructions):
- ES core: Withdrawal, Volatility
- E core: Enthusiasm
- Center triangle: Assertiveness, Compassion
- I×ES zone: Industriousness, Orderliness
- I×E zone: Openness
- I edge (grouped with Edge/Outside): Intellect
- ES×E zone: Politeness

## Analysis 1: Aspect-Level (Haehner 2025, L)

### Available data

| Aspect | BT Zone | LS correlation | Source |
|---|---|---|---|
| Withdrawal | ES core | **−.51** | Haehner Table 9 |
| Volatility | ES core | **−.34** | Haehner Table 9 |
| Enthusiasm | E core | ~.35–.45 (estimated) | Haehner: "similar to Assertiveness"; domain r ≈ .30–.40 |
| Assertiveness | Center | ~.35–.45 (estimated) | Haehner: "similar to Enthusiasm" on LS |
| Compassion | Center | ~.25–.35 (estimated) | Haehner: "drives A's LS correlations"; Sun sr = .34 |
| Industriousness | I×ES | **.44** | Haehner Table 9 |
| Orderliness | I×ES | **.14** | Haehner Table 9 |
| Politeness | ES×E | **~.00** | Haehner: "near-zero on LS" |
| Openness | I×E | **~.00** | Haehner: "zero LS" (line 698) |
| Intellect | I edge | **positive** | Haehner: "positive LS" (specific value not transcribed) |

### Zone means (using |r| for strength of prediction)

| Zone | Aspects | |r| values | Mean |r| |
|---|---|---|---|
| ES core (Primary) | Withdrawal, Volatility | .51, .34 | **.43** |
| E core (Primary) | Enthusiasm | ~.40 (est.) | **~.40** |
| **Primary cores combined** | All three above | .51, .34, ~.40 | **~.42** |
| Center triangle | Assertiveness, Compassion | ~.40, ~.30 (est.) | **~.35** |
| Intersection: I×ES | Industriousness, Orderliness | .44, .14 | **.29** |
| Intersection: I×E | Openness | ~.00 | **~.00** |
| Intersection: ES×E | Politeness | ~.00 | **~.00** |
| **Intersection combined** | All three sub-zones | .44, .14, ~.00, ~.00 | **~.15** |
| Edge/outside | Intellect | positive (~.15–.25 est.) | **~.20** |

### Predicted vs. actual ordering

Prediction: Center triangle ≥ Intersection zones > Primary cores > Edge/outside

Actual (aspect-level): **Primary cores (~.42) > Center triangle (~.35) > Edge/outside (~.20) > Intersection (~.15)**

- ✗ Center triangle highest: NOT SUPPORTED. Primary cores are highest.
- ✗ Primary cores lowest (of the first three groups): NOT SUPPORTED. Primary cores are highest.
- ✓ Edge/outside low: SUPPORTED (but only one aspect in this zone).
- Partial: Center > Intersection: SUPPORTED (~.35 > ~.15).

**Critical caveat:** The ES core dominance is driven by Withdrawal (−.51) — which is essentially Depression + Anxiety content. The strong LS prediction of these facets is well-established and reflects definitional overlap (depressed people are dissatisfied with life). This is not a structural finding — it's a content-criterion overlap.

## Analysis 2: Facet-Level (Schimmack 2004 + Røysamb 2018)

Limited to N and E facets (12 of 30), plus scattered values for C1, N5, E5.

### Data table

| Facet | BT Zone | r with LS | Source | Notes |
|---|---|---|---|---|
| **PRIMARY CORES** | | | | |
| N1 Anxiety | ES core | −.22 | Schimmack T1 | Røysamb: selected as top predictor |
| N3 Depression | ES core | −.52 | Schimmack T1 | Strongest single predictor |
| N4 Self-Consciousness | ES core | −.35 | Schimmack T1 | |
| N6 Vulnerability | ES core | −.31 | Schimmack T1 | |
| A1 Trust | ES core | ~.20 | Estimated from domain r and pattern | No specific value in extractions |
| E2 Gregariousness | E core | .26 | Schimmack T1 | |
| E1 Warmth | E core | .27 | Schimmack T1 | |
| E5 Excitement-Seeking | E core | .05 | Røysamb | Schimmack: −.03. Near zero in both. |
| **I×ES ZONE** | | | | |
| C1 Competence | I×ES | .30 | Røysamb | Røysamb: "exceeds C domain (.28)" |
| N5 Impulsiveness | I×ES | −.14 | Røysamb | Schimmack: −.19. Weakest N facet. |
| C4 Ach. Striving | I×ES | ~.20 | Estimated from C domain (.28) | |
| C2 Order | I×ES | — | No data | |
| C6 Deliberation | I×ES | — | No data | |
| **I×E ZONE** | | | | |
| O2, O3, O1, O5 | I×E | — | No facet-level data | Domain r ≈ .05–.15 typical |
| **ES×E ZONE** | | | | |
| N2 Angry Hostility | ES×E | −.34 | Schimmack T1 | |
| A2, A4 | ES×E | — | No facet-level data | |
| **CENTER TRIANGLE** | | | | |
| E3 Assertiveness | Center | .21 | Schimmack T1 | Røysamb: in .13–.30 range |
| E4 Activity | Center | .23 | Schimmack T1 | Røysamb: selected as top predictor |
| E6 Positive Emotions | Center | .40 | Schimmack T1 | Røysamb: .30. Strongest E facet. |
| A3 Altruism | Center | — | No data | |
| C3 Dutifulness | Center | — | No data | |
| A6 Tender-Mindedness | Center | — | No data | |
| O4 Actions | Center | — | No data | |
| **OUTSIDE** | | | | |
| A5 Modesty | Outside | — | No data | |
| O6 Values | Outside | — | No data | |
| C5 Self-Discipline | Outside | — | No data | |

### Zone means (|r|, facet-level, available data only)

| Zone | Available facets | |r| values | Mean |r| | N (of total) |
|---|---|---|---|---|
| Primary cores (ES) | N1, N3, N4, N6, (A1 est.) | .22, .52, .35, .31, (~.20) | **.32** | 5 of 5 |
| Primary cores (E) | E2, E1, E5 | .26, .27, .05 | **.19** | 3 of 3 |
| **Primary combined** | 8 facets | | **.27** | 8 of 8 |
| I×ES (intersection) | C1, N5, (C4 est.) | .30, .14, (~.20) | **.21** | 3 of 5 |
| ES×E (intersection) | N2 | .34 | **.34** | 1 of 3 |
| I×E (intersection) | — | — | **no data** | 0 of 4 |
| Center triangle | E3, E4, E6 | .21, .23, .40 | **.28** | 3 of 7 |
| Outside | — | — | **no data** | 0 of 3 |

### Predicted vs. actual (facet-level, partial data)

Prediction: Center triangle ≥ Intersection zones > Primary cores > Edge/outside

Actual: ES×E (.34) > ES core (.32) > Center (.28) > Primary combined (.27) > I×ES (.21) > E core (.19)

The center triangle (.28) is NOT higher than the primary cores (.27). Essentially equal.

## Analysis 3: What Drives the Signal — Specific Facets

The four strongest individual facet predictors (from Røysamb regression, β > .10):
1. N3 Depression: −.52 (ES core)
2. E6 Positive Emotions: .40 (Center triangle)
3. N4 Self-Consciousness: −.35 (ES core)
4. N1 Anxiety: −.22 (ES core)

The Røysamb Cholesky decomposition found that within each domain, a single genetic factor captured ALL the genetic prediction of LS. The second facet's unique genetic variance added nothing. This means the LS signal in personality is genetically concentrated, not distributed across many facets.

The two strongest aspect-level predictors (Haehner 2025):
1. Withdrawal: −.51 (ES core)
2. Industriousness: .44 (I×ES zone)

The strongest LS prediction comes from Emotional Stability (reversed N) and Industriousness — both primary-core or intersection-zone content. NOT from the center triangle.

### The E6 exception

E6 Positive Emotions is the one center-triangle facet with a strong LS signal (.30–.40). It is consistently the strongest E facet predictor across all studies. Schimmack's key finding is that Depression and Positive Emotions are "necessary and sufficient to predict life satisfaction from personality traits."

This means one center facet (E6) is a strong predictor, but the center triangle as a GROUP does not concentrate the LS signal. The signal in E6 may reflect its role as a positive-affect facet rather than its "Brilliance" status.

### The Industriousness finding

Industriousness (I×ES zone) is the strongest positive predictor at the aspect level — mean sr = .55 across WB variables (Sun 2017), r = .44 with LS (Haehner 2025). This is an intersection-zone aspect, not center triangle. Industriousness's LS signal is LARGER than any center-triangle estimate.

## Verdict: NOT SUPPORTED

The predicted ordering (Center triangle ≥ Intersection zones > Primary cores > Edge/outside) is not observed in any analysis.

The actual pattern across both analyses is:

**Primary cores (ES) > Center triangle ≈ Intersection (I×ES) > Edge/Outside ≈ Intersection (I×E, ES×E)**

### Specific predictions tested:

| Prediction | Result | |
|---|---|---|
| Center triangle is the strongest zone | ✗ Primary cores (ES core) are strongest | |
| Center ≥ Intersection | ✗ Partially supported — center (.28-.35) > I×E and ES×E zones (~.00), but center < I×ES (.29-.44) | |
| Primary cores are weaker than center | ✗ Primary cores (.27-.42) ≥ Center (.28-.35) | |
| Edge/outside is weakest | ✓ Consistent — E5 (.05), Openness (~.00), Politeness (~.00) are all near-zero | |

## What the Data Reveal for the Bright Triad Model

### 1. The LS signal is concentrated in the ES core and I×ES zone

Withdrawal (-.51), Depression (-.52), and Industriousness (.44) dominate LS prediction. In the Bright Triad model, these map to the Emotional Stability primary and the Intelligence × Emotional Stability intersection — not to the center triangle.

### 2. The center triangle has ONE strong member (E6) and many weak ones

E6 Positive Emotions (.30-.40) is genuinely strong. E3 (.21) and E4 (.23) are moderate. The remaining center facets (A3, C3, A6, O4) have no individual LS data but their aspects (Compassion ~.30, Orderliness .14) suggest they are mixed.

### 3. The prediction fails because "Brilliance" doesn't integrate into a LS-predictive composite

The Bright Triad model predicts that the center triangle represents integrated mental phenotype functioning. If true, these facets should collectively predict LS better than any single zone. They don't — because the center-triangle facets are psychologically heterogeneous. E6 (cheerfulness) predicts LS for affect-related reasons. E3 (assertiveness) and E4 (activity) predict weakly. A3, A6, O4 likely predict weakly or not at all. There is no emergent "integration" signal.

### 4. The ES core dominance is partly artifactual

Withdrawal/Depression's strong LS correlation reflects partial content overlap: depressed people evaluate their lives negatively. This is almost definitional rather than structurally informative. The Industriousness signal (.44) is more structurally interesting — it suggests that goal-directed engagement (I×ES content) predicts satisfaction through achievement and mastery, not through affect.

### 5. An alternative reading that partially supports the model

If we exclude the ES core (on grounds of content-criterion overlap) and focus on the POSITIVE predictors:
- Center triangle: E6 (.40), E3 (.21), E4 (.23) → mean .28
- I×ES zone: C1 (.30), Industriousness (.44) → strong
- E core: E1 (.27), E2 (.26) → mean .27
- Edge/outside: E5 (.05) → weak

In this framing, the center and intersection zones are comparable, and both exceed the E core and Edge/outside. This is a weaker version of the prediction: center ≈ intersection > primary cores (E only) > outside. But it requires dropping the ES core entirely, which is a post-hoc move.

## Comparison with H7 (Brilliance × Intelligence)

H7 found that the intelligence signal is concentrated in the intersection zones (Intellect .40, Industriousness .32), not the center triangle (.08-.12 composite). H8 finds the same pattern for life satisfaction: the signal is concentrated in the ES core and I×ES zone, not the center triangle.

Both H7 and H8 converge on the same structural conclusion: **the "Brilliance" triple intersection does not concentrate criterion-relevant variance. The criterion variance sits in the intersection zones and primary cores.**

## Caveats

1. **Incomplete facet-level data.** Only 15 of 30 facets have specific LS values. The remaining 15 (all O facets, most A facets, most C facets) are estimated from domain/aspect data. The center triangle is particularly undersampled — only 3 of 7 facets have direct LS data.

2. **Aspect-to-zone mapping is approximate.** Each aspect contains facets from multiple BT zones (e.g., Assertiveness includes E3 center + E4 center + E5 outside). Aspect-level data cannot cleanly distinguish zone effects.

3. **Schimmack is small and unrated.** N = 136 students. Used as supplementary for facet-level coverage only.

4. **Haehner LS values are incomplete.** Only 4 of 10 aspects have specific LS correlations transcribed (Withdrawal, Volatility, Industriousness, Orderliness). The other 6 are described qualitatively. The full Haehner Table 9 would strengthen the analysis.

5. **Sun semipartials ≠ zero-order LS.** Sun's mean semipartial correlations (partialing complementary aspect, averaged across 13 WB dimensions) systematically differ from zero-order LS correlations. They were used only where Haehner values were unavailable.

6. **The ES core dominance may reflect measurement confounding.** Depression items and life satisfaction items share negative-evaluation content. The genetic evidence (Røysamb: personality-related genetics = 20% of LS variance) confirms there IS a genuine personality→LS pathway, but the phenotypic correlations likely overestimate it for Depression/Withdrawal specifically.

7. **N and E facets dominate the available data.** The facet-level analysis is heavily weighted toward N and E facets because these are the only domains with complete coverage. If O, A, and C facets showed different zone patterns, the conclusion could change.
