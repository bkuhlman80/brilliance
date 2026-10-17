# Task H7 (Revised): The Brilliance Composite Correlates with Intelligence More Strongly Than Any Single Big Five Domain

## Data Sources

### Primary: Stanek & Ones (2023) — XL quality, weight 4
Design: Meta-analysis of 1,325 studies, 3,543 meta-analyses, millions of individuals
Measure: Corrected phenotypic correlations (ρ̂) between personality traits and GMA
Coverage: 79 personality constructs × 97 cognitive ability constructs
This is the definitive quantification of personality-intelligence relations.
Note: Uses a hierarchical personality taxonomy (factor/aspect/facet) that partially
maps to NEO-PI-R facets but uses different labels. Mappings noted below.

### Supplementary: Nikolašević et al. (2021) — S quality, weight 1
Design: 212 twin pairs, Serbian, NEO-PI-R × Raven's APM
Measure: Genetic correlations (rG) between all 30 NEO-PI-R facets and fluid g
Coverage: All 30 facets, but S quality — noisy estimates

## Mapping Stanek & Ones Constructs to NEO-PI-R / Bright Triad

| BT zone | NEO facet | Stanek & Ones construct | Match quality |
|---|---|---|---|
| **Center** | E3 Assertiveness | Assertiveness (aspect) / Dominance (facet) | Moderate — aspect vs. facet level |
| **Center** | E4 Activity | Activity (facet) | Direct match |
| **Center** | E6 Pos. Emotions | Positive Emotionality (facet) | Good match |
| **Center** | A3 Altruism | Compassion (aspect) / Nurturance (facet) | Compassion is broader than A3 |
| **Center** | C3 Dutifulness | Dependability (facet) | Approximate |
| **Center** | A6 Tender-Mind. | Tender Mindedness (facet) | Direct match |
| **Center** | O4 Actions | Variety Seeking (facet) | Approximate |
| I×ES | Industriousness | Industriousness (aspect) | Direct match |
| I×E | Openness | Openness (factor) | Direct match |
| I×E | Intellect | Intellect (aspect) | Direct match |

## Center-Triangle Facets: GMA Correlations

### From Stanek & Ones (2023, XL)

| NEO facet | S&O construct | ρ̂ with GMA | 95% CI | Notes |
|---|---|---|---|---|
| E3 Assertiveness | Assertiveness (aspect) | -.03 | — | Near zero as an aspect |
| | Dominance (facet) | **.11** | [.10, .12] | Positive but small |
| E4 Activity | Activity | **.23** | **[.22, .24]** | **Strong — key finding** |
| E6 Pos. Emotions | Positive Emotionality | .04 | — | Near zero; sporadic relations |
| A3 Altruism | Compassion (aspect) | **.26** | **[.24, .27]** | **Strong — but aspect is broader than A3** |
| | Nurturance (facet) | .02 | — | Near zero |
| C3 Dutifulness | Dependability | **.16** | — | Moderate positive |
| A6 Tender-Mind. | Tender Mindedness | -.05 | — | Near zero / slightly negative |
| O4 Actions | Variety Seeking | ~.06 | — | Approximate, from table position |

### From Nikolašević (2021, S)

| NEO facet | rG with APM | Notes |
|---|---|---|
| E3 Assertiveness | ~.00 | Not individually reported |
| E4 Activity | ~.00 | "null" |
| E6 Pos. Emotions | +.25 | Survives FDR |
| A3 Altruism | -.03 | Near zero |
| C3 Dutifulness | ~.00-.05 | Not individually specified |
| A6 Tender-Mind. | -.21 | Negative, significant |
| O4 Actions | +.01 | Near zero |

## Benchmark: Openness Domain

| Source | Construct | ρ̂ / rG with GMA | Notes |
|---|---|---|---|
| Stanek & Ones (XL) | Openness (factor) | **.26** | [.25, .27] |
| Stanek & Ones (XL) | Intellect (aspect) | **.40** | From Table 1 position |
| Stanek & Ones (XL) | Ideas (facet) | **.28** | From Table 1 position |
| Stanek & Ones (XL) | Curiosity | ~.17 | — |
| Nikolašević (S) | O5 Ideas | **.38** (rG) | Highest of any facet |

## Other Notable Personality–GMA Correlations (Stanek & Ones, XL)

| Construct | ρ̂ with GMA | BT zone | Significance for H7 |
|---|---|---|---|
| Industriousness (aspect) | **.32** | I×ES | Higher than any center-triangle facet |
| Compassion (aspect) | **.26** | Overlaps center | Equals Openness; but aspect includes non-center facets |
| Activity (facet) | **.23** | Center | Strongest center-triangle signal |
| Dependability (facet) | **.16** | Center (approx.) | Moderate |
| Dominance (facet) | .11 | Center (approx.) | Small |
| Neuroticism (factor) | -.08 | ES core | Small negative |
| Extraversion (factor) | -.02 | E core | Near zero |

## Composite Estimation

### Method 1: Simple average of center-triangle GMA correlations (Stanek & Ones, XL)

Using best-available mappings for each center-triangle facet:

| Facet | ρ̂ used | Construct used |
|---|---|---|
| E3 | .11 | Dominance (facet-level, more specific than aspect) |
| E4 | .23 | Activity |
| E6 | .04 | Positive Emotionality |
| A3 | .02 | Nurturance (facet-level for A3 specifically) |
| C3 | .16 | Dependability |
| A6 | -.05 | Tender Mindedness |
| O4 | .06 | Variety Seeking (estimated) |

**Simple average: (.11 + .23 + .04 + .02 + .16 + (-.05) + .06) / 7 = .081**

### Method 2: Using Compassion aspect (.26) as proxy for A3

If we use the Compassion aspect (.26) instead of the Nurturance facet (.02):

**Average: (.11 + .23 + .04 + .26 + .16 + (-.05) + .06) / 7 = .116**

### Method 3: Best-case composite (only facets with positive GMA relations)

Taking only the positive-signal center facets (E4, C3, Dominance):

**Average of E4 (.23), C3 (.16), Dominance (.11) = .167**

This still falls below Openness (.26).

## Comparison

| Composite / Domain | ρ̂ with GMA | Source |
|---|---|---|
| **Openness** | **.26** | Stanek & Ones, XL |
| **Intellect (aspect)** | **.40** | Stanek & Ones, XL |
| Industriousness (aspect) | .32 | Stanek & Ones, XL |
| Compassion (aspect) | .26 | Stanek & Ones, XL |
| **Center triangle composite** | **.08-.12** | Computed from S&O |
| Center best-case (E4+C3+Dom) | .17 | Computed from S&O |

## Verdict: NOT SUPPORTED

The center-triangle composite (.08-.12) falls well below the Openness benchmark (.26).
Even the best-case selection of positive center-triangle facets (.17) does not reach
the Openness domain correlation.

The intelligence signal in personality is concentrated in:
1. **Intellect aspect** (.40) — I×E zone
2. **Industriousness aspect** (.32) — I×ES zone
3. **Openness domain** (.26) — I×E zone
4. **Compassion aspect** (.26) — overlaps center but broader than center
5. **E4 Activity** (.23) — center triangle

The Bright Triad model correctly identifies that intelligence-related variance exists
beyond Openness (Activity at .23, Industriousness at .32, Compassion at .26). But this
variance is concentrated in INTERSECTION ZONES (I×ES and I×E), not in the center
triangle.

## What the Stanek & Ones Data Reveal for the Bright Triad Model

### Intelligence signal by BT zone (estimated from S&O)

| Zone | Strongest GMA signal | ρ̂ | Interpretation |
|---|---|---|---|
| I×E (Openness) | Intellect aspect | .40 | Strongest zone for intelligence |
| I×ES (Conscientiousness) | Industriousness aspect | .32 | Second strongest |
| Center triangle | Activity facet | .23 | Third — one standout, rest near zero |
| ES×E (Agreeableness) | Compassion aspect | .26 | Strong — but driven by non-center content |
| Primary cores | — | ~.00 | No intelligence signal |

### Key insight: The I-parent prediction works for INTERSECTION zones

The Bright Triad model predicts that C (I×ES) and O (I×E) share an Intelligence parent.
The Stanek & Ones data show that both Industriousness (.32) and Openness (.26) have
strong GMA correlations — the two strongest domain/aspect-level signals in the entire
personality taxonomy. This is consistent with Intelligence functioning as a shared
parent of C and O, even though the C↔O genetic bridge failed in H4.

The difference from H4: Stanek & Ones measures PHENOTYPIC correlations with an
EXTERNAL criterion (GMA). H4 tested genetic CROSS-LOADINGS between personality
domains. Intelligence may relate to both C and O phenotypically through different
mechanisms (investment for O, executive function for C) without producing genetic
cross-loadings between them.

### E4 Activity is a genuine Intelligence marker

E4 Activity's .23 correlation with GMA is one of the strongest facet-level signals
outside the O domain. The text explicitly notes: "individuals who are energetic and
active score higher on knowledge measures, regardless of the area." This is consistent
with E4's center-triangle placement and its genetic C-loading from H3 — E4 bridges
E and C, and both its genetic architecture and its intelligence correlation support this.

### The center triangle is NOT where Intelligence concentrates

Despite containing E4 (.23), the center triangle also contains facets with near-zero
or negative intelligence relations (Positive Emotionality .04, Tender Mindedness -.05,
Nurturance .02, Variety Seeking .06). These dilute the composite.

The intelligence signal sits in the INTERSECTION zones (I×ES and I×E), not in their
triple overlap. This is the opposite of the Bright Triad prediction for H7, but it's
actually consistent with a different reading of the model: if Intelligence is a
"parent" that contributes to C and O, then the Intelligence variance should be visible
in those intersection zones, not necessarily in the center.

## Updated Assessment Including Both Data Sources

| Source | Quality | Center triangle GMA | Openness GMA | Verdict |
|---|---|---|---|---|
| Stanek & Ones (2023) | XL (weight 4) | .08-.12 (phenotypic) | .26 (phenotypic) | Not supported |
| Nikolašević (2021) | S (weight 1) | ~.01 (genetic) | ~.13 (genetic) | Not supported |
| **Weighted** | | | | **Not supported** |

Both sources agree: the center triangle does not concentrate intelligence variance.
The XL-quality phenotypic data confirms and strengthens the S-quality genetic finding.

## Caveats

1. **Construct mapping.** Stanek & Ones use their own personality taxonomy, not the
   NEO-PI-R directly. The mappings (E4→Activity, A3→Compassion/Nurturance, C3→Dependability)
   are approximate. Some center-triangle facets may not have clean equivalents.

2. **Composite vs. optimal composite.** A simple average treats all facets equally.
   An optimally weighted composite might perform better — but the near-zero correlations
   for most center facets (E6, A6, O4) limit what weighting can achieve.

3. **Phenotypic vs. genetic.** Stanek & Ones reports phenotypic ρ̂, not genetic rG.
   The Bright Triad model might predict genetic rather than phenotypic intelligence
   relations for the center triangle. However, both the phenotypic (XL) and genetic (S)
   data tell the same story.

4. **The "Intelligence" in Bright Triad may not equal GMA.** If the model's Intelligence
   factor is broader than cognitive ability (e.g., including social intelligence,
   creative capacity, adaptive flexibility), GMA may underrepresent it.

5. **Compassion's .26 is promising but ambiguous.** The Compassion ASPECT correlates
   .26 with GMA — as high as Openness. A3 Altruism is one component of Compassion,
   and A3 is a center-triangle facet. But the Compassion aspect also includes A1 Trust
   (ES core in BT) and A6 Tender-Mindedness (center but GMA-negative). The .26 may
   be carried by A1 Trust or by the aggregate, not by A3 specifically. Nurturance
   (.02) — the closest facet-level proxy for A3 — suggests A3's own contribution is
   minimal.
