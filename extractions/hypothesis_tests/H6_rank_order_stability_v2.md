# Task H6 (v2): Developmental Rank-Order Stability by Bright Triad Zone

## Status change: UNTESTABLE → TESTABLE

The previous H6 analysis was flagged as "largely untestable" because the corpus lacked numerical per-facet rank-order stability estimates. The Brandt et al. (2023) supplementary appendix (Tables S13–S17) provides exactly the missing data: **latent 4-year retest correlations for all 30 NEO-PI-R facets**, estimated via local structural equation modeling (LSEM) with scalar measurement invariance across ages 35–80 in the Seattle Longitudinal Study (N = 1,667).

---

## Data Source

**Brandt et al. (2023), quality rating: L (Strong)**
- 4-wave longitudinal design (2001–2012), 11-year span
- Latent retest correlations via LSEM with joint estimation procedure
- Scalar invariance established for all 30 facets
- 4-year interval (Wave 01–05) used as primary stability metric
- Ages 35–80 (adult stability — ideal for testing inherent facet stability)

**Supplementary: Ringwald et al. (2024), quality rating: L**
- 5-wave longitudinal (ages 14–23), N = 645
- BFI/BFI-2 facets (15 facets, 3 per domain — NOT NEO-PI-R)
- Rank-order consistency across 2–3 year intervals
- Cannot be directly integrated but provides convergent/divergent evidence

---

## Extracted Data: 4-Year Latent Retest Correlations (Brandt Tables S13–S17)

All values are M(r) from the 01–05 interval (approximately 4 years, 2001–2005).

### Neuroticism facets (Table S13)

| Facet | M(r) | SD(r) | Range | V2 Zone |
|---|---|---|---|---|
| N1 Anxiety | .865 | .037 | .811–.970 | Primary core |
| N2 Angry Hostility | .824 | .020 | .776–.849 | Intersection (ES×E) |
| N3 Depression | .815 | .011 | .796–.842 | Primary core |
| N4 Self-Consciousness | .906 | .039 | .867–.987 | Primary core |
| N5 Impulsiveness | .851 | .039 | .796–.907 | Center triangle |
| N6 Vulnerability | .900 | .012 | .872–.916 | Primary core |

### Extraversion facets (Table S14)

| Facet | M(r) | SD(r) | Range | V2 Zone |
|---|---|---|---|---|
| E1 Warmth | .881 | .016 | .866–.923 | Intersection (ES×E) |
| E2 Gregariousness | .943 | .003 | .939–.950 | Primary core (E) |
| E3 Assertiveness | .933 | .018 | .908–.985 | Center triangle |
| E4 Activity | .893 | .039 | .831–.942 | Center triangle |
| E5 Excitement Seeking | .894 | .031 | .827–.938 | Edge/outside |
| E6 Positive Emotions | .861 | .017 | .813–.877 | Center triangle |

### Openness facets (Table S15)

| Facet | M(r) | SD(r) | Range | V2 Zone |
|---|---|---|---|---|
| O1 Fantasy | .897 | .033 | .867–.992 | Intersection (I×E) |
| O2 Aesthetics | .894 | .071 | .801–1.026 | Intersection (I×E) |
| O3 Feelings | .905 | .016 | .869–.921 | Intersection (I×E) |
| O4 Actions | 1.011† | .031 | .953–1.060 | Edge/outside |
| O5 Ideas | .919 | .020 | .892–.945 | Intersection (I×E) |
| O6 Values | .892 | .025 | .830–.913 | Edge/outside |

†O4 Actions: latent retest r > 1.0 is a known artifact of latent variable estimation (over-identification in LSEM). Treated cautiously in zone means.

### Agreeableness facets (Table S16)

| Facet | M(r) | SD(r) | Range | V2 Zone |
|---|---|---|---|---|
| A1 Trust | .779 | .037 | .680–.814 | Center triangle |
| A2 Straightforwardness | .831 | .019 | .802–.862 | Intersection (ES×E) |
| A3 Altruism | .862 | .030 | .794–.894 | Intersection (ES×E) |
| A4 Compliance | .846 | .027 | .783–.875 | Intersection (ES×E) |
| A5 Modesty | .908 | .016 | .889–.948 | Edge/outside |
| A6 Tender-Mindedness | .894 | .027 | .862–.963 | Center triangle |

### Conscientiousness facets (Table S17)

| Facet | M(r) | SD(r) | Range | V2 Zone |
|---|---|---|---|---|
| C1 Competence | .861 | .026 | .800–.901 | Intersection (I×ES) |
| C2 Order | .883 | .028 | .844–.928 | Intersection (I×ES) |
| C3 Dutifulness | .859 | .031 | .826–.940 | Intersection (I×ES) |
| C4 Achievement Striving | .937 | .030 | .883–.978 | Intersection (I×ES) |
| C5 Self-Discipline | .848 | .040 | .773–.903 | Intersection (I×ES) |
| C6 Deliberation | .851 | .042 | .766–.919 | Intersection (I×ES) |

---

## V2 Zone Assignments

| Zone | Facets | Count |
|---|---|---|
| **Primary cores** | N1, N3, N6, N4, E2 | 5 |
| **Intersection zones** | C1, C4, C3, C2, C5, C6, O2, O3, O1, O5, A2, A3, A4, N2, E1 | 15 |
| **Center triangle** | E3, E4, E6, A1, A6, N5 | 6 |
| **Edge / outside** | O4, O6, A5, E5 | 4 |

---

## Zone Mean Comparison

### H6 Prediction: Primary cores > Intersection zones > Center triangle

| Zone | n | Mean r | SD | Min | Max | Range |
|---|---|---|---|---|---|---|
| **Primary cores** | 5 | **.886** | .047 | .815 | .943 | .128 |
| **Intersection** | 15 | **.873** | .033 | .824 | .937 | .113 |
| **Center triangle** | 6 | **.869** | .053 | .779 | .933 | .154 |
| Edge/outside | 4 | **.926**† | .056 | .892 | 1.011 | .119 |

†Edge/outside inflated by O4 Actions (1.011). Excluding O4: mean = .898, SD = .009.

### Primary computation

- Primary cores: (.865 + .815 + .900 + .906 + .943) / 5 = **4.429 / 5 = .886**
- Intersection: (.861 + .937 + .859 + .883 + .848 + .851 + .894 + .905 + .897 + .919 + .831 + .862 + .846 + .824 + .881) / 15 = **13.098 / 15 = .873**
- Center triangle: (.933 + .893 + .861 + .779 + .894 + .851) / 6 = **5.211 / 6 = .869**
- Edge/outside: (1.011 + .892 + .908 + .894) / 4 = **3.705 / 4 = .926**

### Result

**The zone ordering matches the prediction: Primary (.886) > Intersection (.873) > Center (.869)**

But the differences are small:
- Primary vs Intersection: .886 − .873 = **.013**
- Intersection vs Center: .873 − .869 = **.004**
- Primary vs Center: .886 − .869 = **.017**

Cohen's d (Primary vs Center): d ≈ (.886 − .869) / .049 = **0.35** (small effect)

Within-zone variance substantially exceeds between-zone variance. The within-zone range for primary cores (.128) is 7.5× larger than the primary-vs-center mean difference (.017).

---

## Individual Facet Analysis

### Most stable facets (top 5, excluding O4 artifact)

| Rank | Facet | r | V2 Zone |
|---|---|---|---|
| 1 | E2 Gregariousness | .943 | Primary core |
| 2 | C4 Achievement Striving | .937 | Intersection |
| 3 | E3 Assertiveness | .933 | Center triangle |
| 4 | O5 Ideas | .919 | Intersection |
| 5 | A5 Modesty | .908 | Edge/outside |

### Least stable facets (bottom 5)

| Rank | Facet | r | V2 Zone |
|---|---|---|---|
| 26 | C5 Self-Discipline | .848 | Intersection |
| 27 | A4 Compliance | .846 | Intersection |
| 28 | A2 Straightforwardness | .831 | Intersection |
| 29 | N2 Angry Hostility | .824 | Intersection |
| 30 | N3 Depression | .815 | Primary core |

### Key observations

1. **E2 Gregariousness (.943) — the most stable facet — is a primary core.** This is the strongest individual-level evidence for the prediction.

2. **E3 Assertiveness (.933) — the third most stable — is center triangle.** This facet is supposedly the most genetically diffuse (loads on 4 domains), yet it has near-top-rank stability. E3 alone nearly equals E2 and exceeds 4 of 5 primary-core facets.

3. **N3 Depression (.815) — the least stable facet — is a primary core.** This pulls the primary-core mean down substantially. Without N3, primary mean = .904.

4. **A1 Trust (.779) is the single biggest outlier.** It is the only center-triangle facet below .850 and the lowest stability across all 30 facets. Without A1, center mean = (.933 + .893 + .861 + .894 + .851) / 5 = .886 — **identical to the primary-core mean.**

5. **C4 Achievement Striving (.937) — an intersection facet — exceeds 4 of 5 primary cores.** The intersection zone contains both very stable (C4, O5) and relatively unstable (N2, A2) facets.

6. **Edge/outside facets are unexpectedly stable (.898 excluding O4).** A5 Modesty (.908) is more stable than most intersection and center facets, despite being "outside all circles."

---

## Supplementary Evidence: Ringwald et al. (2024)

Ringwald reports BFI/BFI-2 facet-level rank-order consistency across 2–3 year intervals in Mexican-origin youth (ages 14–23, N = 645). The instrument uses 3 facets per domain (not 6), so direct integration is not possible. Approximate NEO-PI-R mappings:

| BFI-2 Facet | ~NEO Equivalent | r (ages 21–23) | V2 Zone of NEO equivalent |
|---|---|---|---|
| Sociability | E2 Gregariousness | .80 | Primary core |
| Assertiveness | E3 Assertiveness | .76 | Center triangle |
| Energy | E4 Activity | .70 | Center triangle |
| Aesthetic Sensitivity | O2 Aesthetics | .60 | Intersection |
| Intellectual Curiosity | O5 Ideas | .57 | Intersection |
| Creative Imagination | O1 Fantasy | .72 | Intersection |
| Respectfulness | A2 Straightforwardness | .56 | Intersection |
| Anxiety | N1 Anxiety | .77 | Primary core |
| Depression | N3 Depression | .64 | Primary core |
| Emotional Volatility | N2 Angry Hostility | .77 | Intersection |
| Conscientiousness (domain) | — | .60 | — |

**Convergent patterns:**
- Sociability/E2 is the most stable facet (both studies) ✓
- Assertiveness/E3 is highly stable (both studies) — but E3 is center triangle, not primary
- Depression/N3 is among the least stable (both studies) — but N3 is primary core

**Divergent patterns:**
- In Ringwald (youth, ages 14–23), all stability values are much lower (.26–.81) than Brandt (adults, .779–.943), consistent with the well-established finding that stability increases with age
- The facet-level rank ordering is roughly preserved across developmental periods

---

## Schwaba et al. (2022): No Rank-Order Stability Data

Schwaba (2022) reports mean-level change trajectories and comaturation correlations (r_co-dev), NOT rank-order stability coefficients. Within-domain comaturation correlations (N mean = .33, C mean = .31, A mean = .21, E mean = .15, O mean = .15) reflect codevelopment, not individual-difference stability. These data were already used in H5 and are not applicable to H6.

---

## Limitations

1. **Single study.** The zone comparison rests entirely on one study (Brandt, SLS). No weighted averaging across studies is possible for the NEO-PI-R facet-level estimates. The Ringwald data uses a different instrument and cannot be directly integrated.

2. **Age restriction.** Brandt covers ages 35–80 only. Stability in younger adults may differ. The Ringwald data (ages 14–23) shows much lower overall stability and partially different facet rank ordering.

3. **Small zone n.** With 5, 15, 6, and 4 facets per zone, the zone means are not robust. A single outlier (A1 Trust = .779 or N3 Depression = .815) can shift a zone mean substantially.

4. **O4 artifact.** O4 Actions has a latent stability > 1.0 (an estimation artifact), inflating the edge/outside mean.

5. **LSEM averaging.** The M(r) values are means across age-based LSEM focal points (every 3 years, ages 35–80). Stability varies with age — some facets show age-moderated stability (N4 Self-Consciousness ranges .867–.987; E3 Assertiveness ranges .908–.985). Zone differences might differ at specific ages.

6. **No formal statistical test.** With only 30 facets across 4 zones, a formal ANOVA would have very low power. The analysis is descriptive.

---

## Verdict: WEAKLY SUPPORTED

**The monotonic ordering matches the prediction: Primary (.886) > Intersection (.873) > Center (.869).**

However, the support is weak because:

1. **Trivial effect sizes.** The primary-vs-center difference (.017) is dwarfed by within-zone variability (SD ≈ .05). Cohen's d ≈ 0.35 (small) with n = 5 and n = 6.

2. **Two outlier facets drive the pattern.** A1 Trust (.779) depresses the center mean, and E2 Gregariousness (.943) elevates the primary mean. Remove either, and the zone difference shrinks to near zero. Remove both, and center ≈ primary.

3. **Counter-examples within the data.** E3 Assertiveness (center, .933) is more stable than 4 of 5 primary-core facets. C4 Achievement Striving (intersection, .937) exceeds all primaries except E2. N3 Depression (primary, .815) is the second-least-stable facet overall.

4. **Edge/outside facets are the most stable zone** (.898 excl. O4, or .926 incl. O4), which the theory doesn't predict. If "biological primaries" should be most resistant to environmental perturbation, genetically isolated edge facets should NOT be more stable than primaries.

5. **Single-study limitation.** The pattern rests on one dataset.

### Comparison to domain-level fallback (from v1)

The v1 analysis could only note that N (primary-dominated) had "uniformly high stability" qualitatively. The v2 quantitative analysis confirms this is directionally correct but reveals that the effect is trivial in magnitude and driven by individual facets rather than a systematic zone-level pattern.

### What the data actually suggests

The strongest predictor of facet stability is not zone membership but **measurement properties and construct breadth**. Facets with narrow, well-defined behavioral referents (E2 Gregariousness, C4 Achievement Striving, E3 Assertiveness) tend to be more stable regardless of zone. Facets tapping diffuse or mood-laden content (N3 Depression, A1 Trust, N2 Angry Hostility) tend to be less stable. This psychometric explanation is more parsimonious than the Bright Triad zone account.

---

## Summary Statistics

| Comparison | Difference | Cohen's d | Direction |
|---|---|---|---|
| Primary vs Intersection | +.013 | ~0.32 | ✓ Predicted |
| Primary vs Center | +.017 | ~0.35 | ✓ Predicted |
| Intersection vs Center | +.004 | ~0.09 | ✓ Predicted (trivial) |
| Primary vs Edge/outside | −.012 | — | ✗ Not predicted |

**Overall verdict: WEAKLY SUPPORTED — monotonic ordering present, effect sizes trivial, driven by 2 outlier facets, and contradicted by edge/outside zone being most stable.**
