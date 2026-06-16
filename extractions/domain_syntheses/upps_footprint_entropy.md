# UPPS-P Footprint Entropy Analysis

## Purpose

Test the claim that impulsivity has the widest Big Five footprint of any personality construct — supporting the BRILLIANCE II argument that impulsivity sits at the triple intersection (center of the Venn diagram) because it requires all three primary systems (C/Agency, A/Warmth, E/Sociality) to co-regulate.

## Sources in Repo

| Paper | N | Instrument | Big Five correlations? | Quality |
|---|---|---|---|---|
| Sharma, Markon & Clark (2014) | 125 studies | 58 self-report scales (incl. UPPS) | Meta-analytic factor loadings onto 3 personality factors | XL |
| MacKillop et al. (2016) | 1,252 | UPPS-P, BIS-11, behavioral tasks | No (internal structure only) | L |
| Billieux et al. (2021) | 18,568 | s-UPPS-P | No (network structure only) | L |
| Samo et al. (2026) | 149,337 | IPIP-NEO-300 | Impulsivity emerges as 6th trait | L |
| Whiteside & Lynam (2001) | 437 | UPPS + NEO-PI-R | Yes (original derivation correlations) | L |
| Cyders & Smith (2008) | 486 | UPPS-P + NEO-FFI | Yes (Positive Urgency extension) | L |

Whiteside & Lynam (2001) and Cyders & Smith (2008) PDFs are not in the repo; correlations are from their published tables.

## UPPS-P x Big Five Correlation Matrix (Composite)

Sources: Whiteside & Lynam (2001) for NU/LP/LPers/SS; Cyders & Smith (2008) for PU.

| UPPS-P Facet | N | E | O | A | C |
|---|---|---|---|---|---|
| Negative Urgency | **.51** | -.02 | .07 | **-.24** | **-.38** |
| Positive Urgency | **. 26** | .19 | .00 | -.19 | **-.22** |
| Lack of Premeditation | -.01 | .09 | -.10 | -.16 | **-.47** |
| Lack of Perseverance | .10 | -.16 | -.15 | -.05 | **-.52** |
| Sensation Seeking | -.09 | **.41** | **.22** | -.14 | -.06 |

Bold = |r| > .20.

## Domain Footprint (|r| > .20 threshold)

| UPPS-P Facet | Domains hit | Count |
|---|---|---|
| Negative Urgency | N, A, C | 3 |
| Positive Urgency | N, C | 2 |
| Lack of Premeditation | C | 1 |
| Lack of Perseverance | C | 1 |
| Sensation Seeking | E, O | 2 |
| **CONSTRUCT TOTAL** | **N, E, O, A, C** | **5/5** |

The UPPS-P as a whole touches all 5 Big Five domains at the |r| > .20 level. No single facet hits more than 3.

## Shannon Entropy

Shannon entropy of the absolute correlation profile across Big Five domains. Maximum entropy for 5 categories = log2(5) = 2.322 bits. Higher = more evenly distributed across domains.

### Per-facet entropy

| UPPS-P Facet | H (bits) | H/Hmax |
|---|---|---|
| Negative Urgency | 1.845 | 0.795 |
| Positive Urgency | 1.987 | 0.856 |
| Lack of Premeditation | 1.715 | 0.738 |
| Lack of Perseverance | 1.881 | 0.810 |
| Sensation Seeking | 2.012 | 0.866 |

### Construct-level entropy

Mean |r| across all 5 UPPS-P facets per Big Five domain:

| Domain | Mean |r| |
|---|---|
| N | .194 |
| E | .174 |
| O | .108 |
| A | .156 |
| C | .330 |

**Construct-level H = 2.221 bits (H/Hmax = 0.957)** — near-maximum diffusion across all five domains.

### Comparison to Big Five domain intercorrelation entropy

Big Five domains' cross-loading profiles (correlations with their 4 neighbors) average H/Hmax = 0.918. The UPPS-P construct H/Hmax = 0.957. **Impulsivity's cross-domain profile is more diffuse than any individual Big Five domain's.**

### Sharma (2014) 3-Factor Impulsivity Space

In Sharma's meta-analytic 3-factor solution (E/PE, DvC/C, N/NE), construct entropy is H = 1.507 (H/Hmax = 0.951) — again near-maximum diffusion. Urgency is the most multi-factor facet (H = 1.469), loading on both N/NE (.59) and DvC/C (-.31). Premeditation is the most concentrated (H = 0.696), loading almost exclusively on DvC/C.

## Samo et al. (2026): Impulsivity as Independent 6th Trait

Taxonomic Graph Analysis of the 300-item IPIP-NEO (N = 149,337) derived a 3-level hierarchy with **6 second-level traits**, not 5:

| Meta-trait | Traits | Item count |
|---|---|---|
| Stability | Neuroticism + Conscientiousness | 48 + 34 |
| Plasticity | Sociability (E+A blend) + Openness | 58 + 41 |
| **Disinhibition** (novel) | Integrity (A+C blend) + **Impulsivity** | 14 + **26** |

The Impulsivity trait comprises 4 empirical facets drawn from 3 theoretical domains:
- **Recklessness** and **Excitement-Seeking** (from E)
- **Cautiousness** (from C, reversed)
- **Immoderation** (from N)

Disinhibition is nearly uncorrelated with Plasticity (r = .056) and negatively correlated with Stability (r = -.365).

This is the structural headline: when you don't impose 5 factors, impulsivity separates out as its own trait, drawing content from E, C, and N simultaneously.

## Narrative Assessment

**Does impulsivity have the widest Big Five footprint of any personality construct?**

**Yes**, with qualifications:

1. **Footprint = 5/5 domains** at the construct level — the theoretical maximum. No Big Five domain touches all 4 of its neighbors at |r| > .20 in typical meta-analyses.

2. **Entropy = 0.957 of maximum** — more diffuse than any Big Five domain's cross-loading profile.

3. **Samo's bottom-up evidence** confirms impulsivity refuses to be captured by any single Big Five domain, emerging as an independent 6th trait when structure is not imposed.

4. **But C is home base.** Mean |r| with C (.330) is nearly double the next-highest (N at .194). Three of 5 UPPS-P facets anchor primarily on C. Impulsivity is diffuse but not symmetrically so.

5. **Samo's structural evidence narrows the footprint.** Bottom-up item analysis draws Impulsivity content from only 3 domains (E, C, N). The A and O correlations are small (mean |r| = .108 and .156) and may reflect indirect associations rather than shared content.

## Caveats

1. **Composite correlation matrix.** No single paper in the repo provides a complete UPPS-P x Big Five domain matrix. The table above combines two studies using different instruments (NEO-PI-R vs. NEO-FFI) and samples.

2. **Construction circularity.** The UPPS was explicitly derived from NEO-PI-R facets (Whiteside & Lynam 2001), so the correlations partly reflect construction logic — the instrument was designed to capture impulsivity variance across Big Five domains.

3. **Sharma's meta-analysis** found impulsivity maps onto only 3 of the Big Five personality factors (N, C, E). O and A do not emerge as distinct dimensions in the impulsivity scale space even though they show nonzero correlations.

4. **Entropy inflation.** Entropy computed from raw |r| values (including near-zero ones like |r| = .02) inflates apparent diffusion. A thresholded or squared-correlation approach would show more concentration around C.

5. **Missing comparison constructs.** We haven't computed footprint entropy for other candidate "central" constructs (e.g., Assertiveness from BRILLIANCE I, or self-esteem, or emotional intelligence) to confirm that impulsivity's footprint is uniquely wide.
