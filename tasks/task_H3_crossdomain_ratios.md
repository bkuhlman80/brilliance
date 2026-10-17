# Task H3: Cross-Domain Genetic Loading Ratios by Bright Triad Zone

## Reference
See `bright_triad_reference.md` for the model description and zone assignments.

## Hypothesis
Center-triangle facets have the highest cross-domain genetic loading ratios, primary-core facets have the lowest, and intersection-zone facets fall in between. E3 Assertiveness should have the single highest ratio of any facet.

## Prediction
Mean cross-domain ratio: Center triangle > Intersection zones > Primary cores

## What is a cross-domain loading ratio?
When genetic factor analyses of personality extract five genetic factors corresponding to the Big Five, each facet loads on its "home" domain factor and may also cross-load on other domain factors. The cross-domain ratio captures how genetically diffuse a facet is:

**Cross-domain ratio = (sum of absolute cross-domain genetic loadings) / (absolute primary-domain genetic loading)**

A ratio near 0 means the facet is genetically "pure" — all its genetic variance is in one domain. A ratio above 1.0 means cross-domain loadings collectively exceed the home-domain loading.

## Data needed
Genetic factor loadings for NEO-PI-R facets on all five domain-level genetic factors. These come from multivariate genetic analyses that extract genetic Big Five factors and report how each facet loads on each factor. Cross-cultural replications (same analysis run in multiple countries) are especially valuable.

For each facet, you need:
- The genetic loading on its assigned domain factor (the "primary" loading)
- The genetic loadings on the other four domain factors (the "cross-loadings")
- Ideally, these loadings across multiple samples/countries

## Analysis
1. For each facet with available data, compute the cross-domain ratio.
2. Assign each facet to its Bright Triad zone.
3. Compute zone means and ranges.
4. Identify which individual facet has the highest ratio.
5. Compare against prediction.

## Output
- Per-facet table: facet, primary loading, cross-loadings, ratio, zone assignment
- Zone means and ranges for the ratio
- Identification of the most genetically diffuse facet
- Verdict: Supported / Partially supported / Not supported / Untestable
- Data coverage note: how many facets have full five-factor genetic loading data?
- Caveats (especially: if loadings vary across countries, report the range and note which country's data you used)
