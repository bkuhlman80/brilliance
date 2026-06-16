# Task H4: Direction of Cross-Domain Genetic Loadings by Bright Triad Zone

## Data Source

Pilia et al. (2006) Supplementary Table S3 — Quality XL, weight 4
Genetic factor loadings for all 30 NEO-PI-R facets on 5 genetic factors.

## Directional Predictions

For each intersection zone, the Bright Triad model predicts cross-loadings toward
the zone's two parent factors:

| Zone | Parent 1 | Parent 2 | Predicted cross-loading directions |
|---|---|---|---|
| I x ES (C) | Intelligence | Emot. Stability | Negative N (= toward ES); Positive O (= toward I via shared parent) |
| I x E (O) | Intelligence | Extraversion | Positive E (= toward E); Positive C (= toward I via shared parent) |
| ES x E (A) | Emot. Stability | Extraversion | Negative N (= toward ES); Positive E (= toward E) |

"Intelligence" is not a Big Five factor, so the I-parent prediction is tested indirectly:
C and O should cross-load toward each other (both share the Intelligence parent).

## Per-Facet Analysis

### I x ES Zone (Conscientiousness): C1, C4, C2, C6, N5

Predicted: negative N (ES parent) + positive O (Intelligence parent)
Non-predicted: E, A loadings

| Facet | N loading | O loading | E loading | A loading | ES pred? | I pred? | Violations |
|---|---|---|---|---|---|---|---|
| C1 | **-.41** | .05 | .36 | .15 | ✓ strong | negl. | E=.36 non-predicted |
| C4 | -.25 | -.01 | .25 | -.36 | ✓ moderate | negl. | A=-.36 non-predicted |
| C2 | -.08 | **-.35** | .12 | -.02 | negl. | **✗ WRONG** | O negative = anti-Intelligence |
| C6 | **-.39** | **-.43** | .07 | .22 | ✓ strong | **✗ WRONG** | O negative = anti-Intelligence |
| N5* | [primary] | **.36** | .18 | -.31 | [is N] | ✓ moderate | A=-.31 non-predicted |

*N5: primary is N (.45); C loading (-.41) confirms BT zone assignment; O loading (.36) supports I-parent.

**I x ES Summary:**
- ES-parent prediction (negative N): **3 of 4 C facets** have meaningful negative N loadings (C1, C4, C6). C2 is negligible. → **75% hit rate** ✓
- Intelligence-parent prediction (positive O): **FAILS.** C2 (-.35) and C6 (-.43) load NEGATIVELY on O — the opposite of predicted. Only N5 (.36) is positive. → **20% hit rate** ✗
- Largest non-predicted loadings: C1→E (.36), C4→A (-.36). Both are moderate.

### I x E Zone (Openness): O2, O3, O1, O5

Predicted: positive E (E parent) + positive C (Intelligence parent)
Non-predicted: N, A loadings

| Facet | E loading | C loading | N loading | A loading | E pred? | I pred? | Violations |
|---|---|---|---|---|---|---|---|
| O2 | **.42** | .02 | .06 | .14 | ✓ strong | negl. | none |
| O3 | **.41** | .19 | .10 | .07 | ✓ strong | ✓ small | none |
| O1 | **.44** | -.18 | -.03 | -.02 | ✓ strong | ✗ wrong | C negative |
| O5 | .25 | -.03 | -.15 | .02 | ✓ moderate | negl. | N=-.15 borderline |

**I x E Summary:**
- E-parent prediction (positive E): **4 of 4** O facets load positively on E. → **100% hit rate** ✓✓
- Intelligence-parent prediction (positive C): Only O3 (.19) is positive and above threshold. O1 is -.18 (wrong direction). → **25% hit rate** ✗
- This zone is very clean: E is the dominant cross-loading for every O facet, and non-predicted loadings are negligible.

### ES x E Zone (Agreeableness): A2, A4, N2

Predicted: negative N (ES parent) + positive E (E parent)
Non-predicted: O, C loadings

| Facet | N loading | E loading | O loading | C loading | ES pred? | E pred? | Violations |
|---|---|---|---|---|---|---|---|
| A2 | .08 | -.17 | .10 | .28 | ✗ wrong dir. | ✗ wrong dir. | C=.28 non-pred. |
| A4 | **-.20** | .17 | -.28 | -.01 | ✓ moderate | ✓ small | O=-.28 non-pred. |
| N2* | [primary] | -.19 | -.25 | -.01 | [is N] | ✗ wrong dir. | A=-.35 zone-confirming |

*N2: primary is N (.79); A loading (-.35) confirms BT zone assignment but isn't a parent prediction.

**ES x E Summary:**
- ES-parent prediction (negative N): A4 ✓, A2 ✗ (positive, wrong direction). → **50% hit rate** (1 of 2 A facets)
- E-parent prediction (positive E): A4 ✓ (small), A2 ✗ (negative), N2 ✗ (negative). → **33% hit rate** (1 of 3)
- A2 Straightforwardness violates BOTH parent predictions. Its largest cross-loading is on C (.28) — non-predicted.
- N2's E loading is -.19 (wrong direction for E parent).

## Aggregate Results

### By prediction type

| Prediction | Facets tested | Hit rate | Assessment |
|---|---|---|---|
| ES parent (negative N) for C facets | 4 | 75% (3/4) | ✓ Supported |
| E parent (positive E) for O facets | 4 | 100% (4/4) | ✓✓ Strongly supported |
| ES parent (negative N) for A facets | 2 | 50% (1/2) | Marginal |
| E parent (positive E) for A facets | 3 | 33% (1/3) | ✗ Not supported |
| I parent via O (positive O) for C facets | 5 | 20% (1/5) | ✗✗ Fails — 2 facets in wrong direction |
| I parent via C (positive C) for O facets | 4 | 25% (1/4) | ✗ Fails |

### By zone

| Zone | % cross-loading magnitude in predicted directions | Assessment |
|---|---|---|
| I x E (Openness) | **67%** | Partially supported — E parent works perfectly |
| I x ES (Conscientiousness) | **37%** | Not supported — ES parent works, I parent fails |
| ES x E (Agreeableness) | **19-33%** | Not supported — both parent predictions weak |
| **Overall** | **~43%** | **Not supported (<50% threshold)** |

### By parent factor

| Parent factor | Prediction | Overall hit rate | Assessment |
|---|---|---|---|
| Emotional Stability | Negative N cross-loadings | 4/6 = 67% | Moderately supported |
| Extraversion | Positive E cross-loadings | 5/7 = 71% | Supported |
| **Intelligence (indirect)** | **C↔O mutual cross-loadings** | **2/9 = 22%** | **✗✗ Fails decisively** |

## Verdict: PARTIALLY SUPPORTED — with a critical structural finding

**Overall: Not supported** by the aggregate <50% criterion.

But the failure is NOT uniform. It decomposes cleanly into two findings:

### Finding 1: Direct parent predictions WORK (✓)
When the predicted parent is a Big Five domain (ES or E), the cross-loadings largely
point in the right direction:
- C facets → low N (ES parent): 75% ✓
- O facets → E (E parent): 100% ✓✓
- A facets → low N, E: mixed (33-50%)

Averaging the ES and E parent predictions: **67% hit rate** → Partially supported.

### Finding 2: Intelligence-mediated predictions FAIL (✗)
The prediction that C and O should cross-load toward EACH OTHER (via shared Intelligence
parent) fails decisively:
- C facets loading positively on O: 20% (and 2 facets load NEGATIVELY)
- O facets loading positively on C: 25%
- Combined: **22% hit rate** ✗✗

This is the most informative result. The Bright Triad model posits Intelligence as a
shared parent of both C and O. If this were correct, C and O facets should share genetic
variance — their facets should cross-load on each other's genetic factors. They do not.
Instead:
- C2 Order loads -.35 on O (genetically, orderly people are LESS open)
- C6 Deliberation loads -.43 on O (genetically, deliberate people are LESS open)
- O1 Fantasy loads -.18 on C (genetically, imaginative people are LESS conscientious)
- O5 Ideas loads -.03 on C (negligible)

The C↔O genetic relationship is NEGATIVE or absent, not positive. This is the opposite
of what a shared Intelligence parent would produce.

## Specific Facet Violations

**A2 Straightforwardness** is the cleanest model violation. It sits in the ES×E zone
(predicted: negative N, positive E), but its cross-loadings are:
- N: +.08 (wrong direction)
- E: -.17 (wrong direction)
- C: .28 (non-predicted, and the LARGEST cross-loading)
A2 violates both parent predictions and cross-loads primarily on a non-parent domain.

**C2 Order and C6 Deliberation** violate the Intelligence-parent prediction. Both have
large negative O loadings (-.35 and -.43), meaning they are genetically ANTI-open.
Conceptually, these facets involve careful constraint and rule-following — the
psychological opposite of openness to experience. The genetic data confirm this
opposition. The Bright Triad model treats this opposition as paradoxical (both C and O
should share an Intelligence parent), but the genetic architecture says C and O are
partially antagonistic, not allied.

**N2 Angry Hostility** loads -.19 on E (wrong direction for the E parent of the A zone).
Anger/hostility is anti-social, which genetically manifests as low E — directly counter
to the prediction that A-zone facets should share E genetics.

## What the Pattern Reveals

The results suggest that ES (Emotional Stability) and E (Extraversion) function as
genuine genetic parents of the intersection domains, consistent with the Bright Triad
model. But Intelligence does NOT function as a detectable genetic parent shared between
C and O. At the genetic level:

- C's cross-domain loadings point toward low-N (ES parent ✓) and scattered E/A
- O's cross-domain loadings point toward E (E parent ✓) and NOT toward C
- C and O are genetically independent or mildly antagonistic

This is consistent with the Pilia S2 genetic cluster data: C facets cluster together
(Cluster 17), O facets cluster together (Cluster 15), and these two clusters do NOT
overlap. The only genetic bridge between C and O is through the E-N mega-cluster
(Cluster 18), not through any direct C↔O link.

## Cross-Cultural Note

Yamagata (2006, XL/L) three-country data confirms the key patterns:
- N5's C cross-loading: -.53/-.33/-.52 (replicates in 3 countries)
- N6's C cross-loading: -.37/-.34/-.57 (replicates)
- E4's C cross-loading: .48/.53/.54 (replicates)
- N2's A cross-loading: -.32/-.41/-.60 (replicates, strengthens east)
- All O facets' E cross-loadings: consistent positive direction

The direct parent predictions that work in Pilia also replicate cross-culturally.

## Caveats

1. **Intelligence is latent.** The Bright Triad's Intelligence factor is not directly
   measured by any Big Five genetic factor. The C↔O bridge test is an indirect proxy.
   Intelligence might influence C and O through mechanisms not captured by genetic
   factor loadings (e.g., gene-environment correlation, epistasis).

2. **Procrustes rotation.** The genetic loadings are rotated toward the Big Five phenotypic
   structure. This may suppress unexpected cross-loadings. However, it should affect all
   zones equally, not selectively suppress C↔O loadings.

3. **Small ES×E zone.** Only 3 facets (A2, A4, N2) — low power to assess.

4. **Threshold effects.** Using |.15| as the meaningful threshold is somewhat arbitrary.
   Relaxing to |.10| wouldn't change the pattern substantially.

5. **The C↔O failure could reflect measurement.** NEO-PI-R C items emphasize behavioral
   regulation (orderliness, self-discipline) while O items emphasize aesthetic/cognitive
   openness. The item content may PREVENT detection of a shared Intelligence factor
   that exists at a deeper level. This is unfalsifiable from the current data but
   worth noting.
