# Individual Differences in Shoaling Behavior in Fish: A Research Reconnaissance

**Compiled for:** Brian (expert researcher)
**Date:** 14 May 2026
**Scope:** Within-species, within-population individual differences in shoaling/sociability in fish. Cross-species comparisons excluded.

---

## 1. Bottom-Line Summary

**Empirically settled.** Within a single population of a given species, individual fish show statistically repeatable differences in their tendency to be near conspecifics (variously operationalized as shoaling tendency, social affiliation, sociability, or conspecific proximity preference). Across species with substantive evidence — three-spined stickleback, zebrafish, guppy, mosquitofish, *Poecilia vivipara*, *Neolamprologus pulcher*, and Eurasian perch — adjusted repeatabilities ("R" or ICC) for sociability assays typically fall in the range **R ≈ 0.20–0.55** over intervals of days to a few weeks. Time-decay is consistent: Chervet et al.'s very large *N. pulcher* dataset showed declines from R ≈ 0.83 (same-day) to R ≈ 0.19 over ~3 years.

**Plausibly inferred.** Heritability of shoaling/schooling tendency is non-zero and likely modest-to-moderate. Direct heritability estimates for the sociability component (as opposed to "schooling ability" or correlated bold-shy axis traits) are scarce. The strongest evidence comes from F2 stickleback marine × benthic crosses (Greenwood, Wark, Peichel and colleagues): they mapped *schooling ability* to chromosome 4 (linked to *Eda*) and to chromosome 21 (lateral line), but found no significant QTL for *schooling tendency*. This dissociation — that one can map *how well* fish school separately from *whether* they choose to school — is the major recurring conceptual finding.

**Genuinely contested.** (i) The sign of the boldness–sociability correlation within populations: stickleback and guppy data give negative, positive, and null estimates depending on population, sex, social housing, and assay design. (ii) Whether oxytocin/isotocin signalling is causally upstream of *individual variation* in shoaling preference (most evidence is at the gene-knockout / pharmacological level, not on naturally varying individuals). (iii) Whether arena-based dichotomous-choice assays and free-shoal observations tap the same latent trait.

**Thin or untested.** (i) Heritability of *naturally varying* sociability within an unmanipulated population (no published animal-model pedigree analysis isolates sociability per se in a wild-derived population). (ii) Long-interval (>6-month) repeatability in any species. (iii) Fitness consequences of individual sociability in the wild — frequently asserted, rarely measured with marked individuals. (iv) Whether shoaling-with-conspecifics is statistically separable from preference for moving stimuli generally at the level of individual differences.

---

## 2. Repeatability and Stability Findings (Q1, Q2)

### Q1: Variance partitioning

Most papers do not report a full variance decomposition. Where they do, a rough generalization holds: in standardized binary-choice or open-arena sociability assays of small freshwater fish, **between-individual variance accounts for roughly 25–50% of total variance**, residual (within-individual + measurement error) accounts for ~50–70%, and any context/trial-order or tank-block effects typically account for 5–15%. Bell, Hankison & Laskowski's 2009 *Animal Behaviour* meta-analysis of fish behavioural repeatability (the field benchmark, though somewhat dated for sociability specifically) gave overall fish R ≈ 0.37. Polverino et al. 2016 (lab-reared *Poecilia vivipara*, females) reports shoaling R = 0.28 — clean variance-decomposition value via GLMM. Chervet et al. 2011 (*N. pulcher*) gives R = 0.546 averaged, declining with interval. The Jolles et al. 2017 stickleback paper reports individual sociability as a moderately repeatable predictor of free-shoal swim speed and structural position; precise variance components are in their supplements.

### Q2: Measurement methods and their repeatability profile

Across published estimates, individual-level repeatability of sociability/shoaling-tendency clusters in two bands:
- **Short-interval (hours to a few days):** R ≈ 0.40–0.85.
- **Medium-interval (1–8 weeks):** R ≈ 0.20–0.55.

Method-specific generalizations:
- **Dichotomous/binary choice** (focal fish vs stimulus shoal vs empty zone): high throughput, but **strongly arena-size sensitive** (McInnes et al. 2025: peak repeatability at 30 cm arena length), body-size sensitive, and risks conflating preference for moving stimuli with preference for conspecifics.
- **Open arena with single stimulus shoal** (Wright/Krause 2006 protocol): lower density artifact, but lower R ceiling.
- **Free-swimming group observation** (Jolles, Couzin labs): captures sociability via nearest-neighbor distance metrics; R typically 0.3–0.5. Conflates active sociability with passive following.
- **Model school assays** (Wark/Greenwood/Peichel mechanical fish dummies): decouple focal fish from real-group feedback; best for genetic mapping; trade-off is ecological validity.
- **Mirror tests for sociability** (Budaev 1997; cited in Gartland et al. 2022): contested — often conflated with aggression measures.

Two further methodological findings define the field's current epistemic state:
1. **Arena size effects (McInnes et al. 2025, stickleback)** — repeatability is non-monotonic in arena size, peaking at 30 cm. Absolute sociability scores vary with arena size, so R values across labs with different geometries are not directly comparable.
2. **Social-housing carryover (Jolles, Taylor & Manica 2016, stickleback)** — fish recently housed alone produced significant boldness repeatability; socially housed fish did not. The same logic almost certainly applies to sociability assays.
3. **Diel context (Härkönen et al. 2019, Eurasian perch)** — within-individual repeatability of activity was higher at night than during day; daytime collective synchrony swamps individual variation. R is conditional on social context during measurement.

### Per-paper inventory (Q1, Q2)

1. **Wright, D., & Krause, J. (2006).** *Nat Protoc, 1*, 1828–1831. DOI: 10.1038/nprot.2006.287. — Methodological landmark. Standardized repeated-measures shoaling protocol for zebrafish; the de facto field standard. **Design:** binary-choice arena. **Verified.**

2. **Wright, Rimmer, Pritchard, Krause & Butlin (2003).** *Naturwissenschaften, 90*, 374–377. DOI: 10.1007/s00114-003-0443-2. — Four wild zebrafish populations, lab-reared. Found within- and between-population variance in shoaling exceeding measurement error. **Verified.**

3. **Greenwood, Wark, Yoshida & Peichel (2013).** *Curr Biol, 23*, 1884–1888. DOI: 10.1016/j.cub.2013.07.058. — F2 marine × benthic stickleback intercross (~270 F2 individuals reported in original methods). **Schooling ability vs schooling tendency dissociation; chr 4/21 QTL for ability.** **Verified.**

4. **Greenwood, Ardekani, McCann, Dubin, Sullivan, Bensussen, Tavaré & Peichel (2015).** *G3, 5*, 761–769. DOI: 10.1534/g3.114.016519. — Expanded F2 panel with automated tracking. Found no significant QTL for *tendency*; significant for *position/ability*. Critical null result. **Verified.**

5. **Wark, Greenwood, Taylor, Yoshida & Peichel (2011).** *PLoS ONE, 6*, e18316. DOI: 10.1371/journal.pone.0018316. — Model-school assay validation; heritable population differences between marine and freshwater sticklebacks. **Verified.**

6. **Jolles, Boogert, Sridhar, Couzin & Manica (2017).** *Curr Biol, 27*, 2862–2868. DOI: 10.1016/j.cub.2017.08.004. — Free-swimming stickleback shoals (n = ~80 individually tracked in known-personality compositions). Individual sociability negatively predicts free-shoal swim speed across contexts. **Verified.**

7. **Jolles, Taylor & Manica (2016).** *Anim Behav, 112*, 139–145. DOI: 10.1016/j.anbehav.2015.12.010. — Stickleback. Recent social housing modulates personality assay repeatability. **Verified.**

8. **Georgopoulou, King, Brown & Fürtbauer (2022).** *Behav Ecol, 33*, 47–54. DOI: 10.1093/beheco/arab108. — Stickleback shoals tested twice 24 h apart. **Design:** repeated-shoal observation. Leader/follower identity repeatable. **Verified.**

9. **Härkönen, Alioravainen, Vainikka & Hyvärinen (2019).** *Behav Ecol, 30*, 785–791. DOI: 10.1093/beheco/arz015. — Eurasian perch, RFID tracking over 10 full diel cycles. Diel-context-dependent repeatability. **Verified.**

10. **McInnes, Fernandes, Munson, Cortese, Randalls & Killen (2025).** *Behav Ecol Sociobiol, 79*, 90. DOI: 10.1007/s00265-025-03634-z. — Stickleback. **Design:** binary-choice assay; each fish measured twice at each of four arena sizes. The most rigorous methodological audit of sociability arena design in the literature. **Verified.**

11. **Chervet, Zöttl, Schürch, Taborsky & Heg (2011).** *PLoS ONE, 6*, e27295. DOI: 10.1371/journal.pone.0027295. — *Neolamprologus pulcher*, n = 1,779. R = 0.546 averaged; same-day R = 0.83, ~3-year R = 0.19; pair-identity h² ≈ 0.15. The single largest fish behavioural-type repeatability dataset. **Verified.**

12. **Polverino, Bierbach, Killen, Uusi-Heikkilä & Arlinghaus (2016).** *Ecol Evol* (PMC5574810). — *Poecilia vivipara* females. Lab-reared cohort: boldness R = 0.37, activity R = 0.57, shoaling R = 0.28 (p = 0.006). **Verified.**

13. **Irving & Brown (2013).** *J Fish Biol, 83*, 311–325. DOI: 10.1111/jfb.12165. — Wild guppy. All three personality traits (boldness, activity, sociability) "highly repeatable" in both sexes. **Verified topic; flagged for confirmation of exact page values.**

14. **Bell, Hankison & Laskowski (2009).** *Anim Behav, 77*, 771–783. — Field-shaping meta-analysis of behavioral repeatability. Overall fish R ≈ 0.37. **Verified.**

---

## 3. Context-Dependence and Cross-Context Consistency (Q3)

### Synthesis

The dominant pattern is **context-conditional rather than context-invariant**: rank order of individual sociability tends to be moderately preserved across mild context changes (e.g., empty vs furnished arena, different times of day) but can be substantially compressed or scrambled by strong manipulations (alarm cues, predator exposure, parasite infection, dramatic shifts in group composition). Reported among-individual correlations of sociability across contexts are typically positive and significant but rarely close to 1, indicating both stable rank effects and context-specific plasticity. Cross-context studies that include sociability alongside boldness/exploration find that the cross-context preservation is *task-dependent* — sociability scored against unfamiliar conspecifics, familiar conspecifics, and heterospecifics often yields divergent individual scores.

Three specific findings worth flagging:

- **Hein et al. 2017/2018, x-ray tetra (*Pristella maxillaris*).** Alarm cues changed both individual-level interaction rules and group-level emergent properties simultaneously. Group-level focus; the paper does not report individual-by-context interaction terms for marked fish, limiting direct inference about rank order.
- **Cote et al. 2013 (*Gambusia affinis*).** Personality-dependent dispersal was *cancelled* under predation risk. Strong demonstration that the *consequences* of individual sociability are context-dependent even where the trait itself remains repeatable.
- **Demandt et al. 2021.** Parasite infection of a fraction of a shoal degraded the shoaling of uninfected fish under predator attack.

A persistent caveat: cross-context decomposition with appropriate among-individual × context interaction terms in mixed models is the analytical gold standard, but few sociability papers implement it. Most report mean-shift findings.

### Per-paper inventory (Q3)

1. **Cote, Fogarty, Tymen, Sih & Brodin (2013).** *Proc R Soc B, 280*, 20132349. DOI: 10.1098/rspb.2013.2349. **Verified.**
2. **Hein, Rosenthal, Hagstrom, Berdahl, Torney & Couzin (2018).** *Sci Adv, 4*, e1603201. DOI: 10.1126/sciadv.1603201. **Verified.**
3. **Demandt, Bierbach, Kurvers, Krause, Kurtz & Scharsack (2021).** Parasite × predator-attack shoaling. **Flagged for confirmation of exact journal/DOI.**
4. **Pearish, Hostert & Bell (2013).** *Behav Ecol Sociobiol, 67*, 1505–1513. DOI: 10.1007/s00265-013-1500-2. — Stickleback. Field-collected individuals in shoals emerged faster from refuge than solitary-caught individuals: a behavioural type × environment correlation in the natural context. **Verified.**
5. **MacGregor & Ioannou (2023).** *Ecol Evol, 13*, e10708. DOI: 10.1002/ece3.10708. — Turbidity (clear vs ~35 NTU) changed local-level shoaling interactions. **Verified.**
6. **Bevan, Gosetto, Jenkins, Barnes & Ioannou (2018).** *Anim Behav, 145*, 79–88. — Stickleback. Boldness predicts leadership; rank order preserved across some social compositions. **Verified.**
7. **Magnhagen & Bunnefeld (2009).** Personality compression in social groups (cited in Jolles et al. 2016). **Flagged for confirmation.**
8. **Webster, Ward & Hart (2007).** *Behaviour, 144*, 351–371. — Sticklebacks behave more boldly in a group than alone; cross-context preservation imperfect. **Verified.**
9. **Härkönen et al. 2019** (above) — diel-context manipulation.
10. **King, Williams & Mettke-Hofmann (2015).** — Cross-context personality measurement. **Flagged for confirmation.**

---

## 4. Heritability and Genetic Architecture (Q4)

### Synthesis

Direct heritability estimates of sociability *within* a single, unmanipulated population are exceptionally sparse. The strongest existing inferences come from:

- **Stickleback marine × benthic QTL crosses** (Peichel lab). Schooling *ability* (body alignment) is heritable and maps in part to the *Eda* locus on chromosome 4 — already famous for armor-plate evolution — and to chromosome 21 (lateral line). Schooling *tendency* did not yield significant QTL in the expanded mapping (Greenwood et al. 2015) — implying lower h², more polygenic architecture, or measurement noise overwhelming detectable additive effects.
- **Zebrafish wild × lab F2 QTL** (Wright et al. 2006). QTL for boldness on chromosomes 9 and 16 and a region on chromosome 21 plausibly linked to antipredator behaviour. Shoaling tendency itself did not yield strong QTL in that mapping panel (n = 184 F2).
- **Zebrafish three-generation pedigree** (Norton 2013-type analyses in *PLoS ONE*, DOI 10.1371/journal.pone.0068828) detected significant narrow-sense h² for boldness-axis traits and significant genetic correlations among them. They did not isolate a sociability trait per se but the architecture constrains sociability h² indirectly.
- **Ariyomo, Carter & Watt 2013** estimated h² ≈ 0.76 for boldness and h² ≈ 0.36 for aggression in zebrafish; sociability not separately estimated.
- **Lange/Hofmann/Pollux poeciliid work on genomic and transcriptomic architecture underlying schooling** (bioRxiv 2023.02.13.528353; final published version in *Nat Commun* / PMC10781616) identifies functional convergence at gene-set and transcript level. Heritability of affiliative associations ranges 0.11–0.51 across animal taxa per their meta-analytic citation.
- **Cichlid *N. pulcher* pedigree** (Chervet et al. 2011): pair-identity h² ≈ 0.15 ± 0.03 — modest.

**Evidentiary tier:** plausibly inferred that h² of sociability is non-zero and modest (rough range 0.1–0.4). Settled that schooling *ability* in sticklebacks has a Mendelian-architecture component including *Eda*. Contested whether schooling tendency itself ever maps to large-effect loci within populations.

### Per-paper inventory (Q4)

1. **Greenwood, Wark, Yoshida & Peichel 2013** (above).
2. **Greenwood et al. 2015** (above).
3. **Wark, Greenwood, Taylor, Yoshida & Peichel 2011** (above).
4. **Wright, Nakamichi, Krause & Butlin (2006).** *Behav Genet, 36*, 271–284. DOI: 10.1007/s10519-005-9029-4. — Zebrafish wild × lab F2 (n = 184). **Verified.**
5. **Norton (and colleagues), PLoS ONE 2013, 10.1371/journal.pone.0068828.** "Quantitative Genetic Architecture of the Bold-Shy Continuum in Zebrafish." Three-generation pedigree; significant narrow-sense h² for component bold-shy traits and significant genetic correlations. **Verified DOI; flagged for confirmation of exact author list.**
6. **Ariyomo, T. O., Carter, M., & Watt, P. J. (2013).** *Behav Genet, 43*. — Zebrafish boldness h² ≈ 0.76, aggression h² ≈ 0.36. **Flagged for exact volume/page.**
7. **Chervet et al. 2011** (above).
8. **Edenbrow, M., & Croft, D. P. (2013).** Mangrove killifish (*Kryptolebias marmoratus*) — self-fertilizing isogenic lines used to decompose genetic vs environmental contributions to personality. **Verified topic; DOI flagged.**
9. **Laine, V. N., et al. (2014).** Nine-spined stickleback (*Pungitius pungitius*) QTL for behavioural/morphological traits. **Flagged.**
10. **Greenwood, Mills, Wark, Archambeault & Peichel (2016).** *Mol Ecol*. — Demonstrated *Eda* allele effects on schooling. **Flagged for exact DOI.**
11. **Lange/Hofmann/Pollux poeciliid functional convergence paper** (PMC10781616). **Verified.**

---

## 5. Developmental Factors (Q5)

### Synthesis

Three developmental variables have the most-cited evidence for shaping individual sociability:

1. **Social isolation during early life.** McCann & Matthews 1974 showed lifelong isolation impairs species-typical shoaling in zebrafish. Dreosti et al. 2015 traced ontogeny of shoaling-preference development in larval zebrafish. The implication is that adult individual differences in sociability are partly the legacy of early social experience.
2. **Recent social context (carryover).** Jolles et al. 2016 (stickleback) demonstrates that even *adult* recent housing alters subsequent personality assay repeatability. Developmental-style effects do not need to occur in early life.
3. **Predator exposure during rearing.** Trinidadian guppy populations diverging in predation regime show robust differences in adult shoaling, but the within-population developmental effect on individual rank order is less well documented. Most "predation regime" papers compare populations rather than manipulating rearing within a population.

**Evidentiary tier:** settled that early social isolation degrades shoaling. Plausibly inferred that rearing density modulates adult sociability mean and variance. Thin for parental effects, food-predictability rearing, and predator-exposure history within a single population.

### Per-paper inventory (Q5)

1. **McCann & Matthews (1974).** *Dev Psychobiol, 7*, 159–163. **Verified.**
2. **Moretz, Martins & Robison (2007).** *Exp Biol Fishes, 80*, 91–101. **Verified.**
3. **Dreosti, Lopes, Kampff & Wilson (2015).** *Front Neural Circuits, 9*, 39. DOI: 10.3389/fncir.2015.00039. **Verified.**
4. **Hinz & de Polavieja (2017).** Ontogeny of shoaling preferences. **Flagged for exact DOI; widely cited.**
5. **Buske & Gerlai (2012).** *Dev Psychobiol, 54*, 28–35. DOI: 10.1002/dev.20571. **Verified.**
6. **Jolles, Taylor & Manica 2016** (above).
7. **Edenbrow & Croft 2013** (above).
8. **Krause, J., et al. (2000).** *Biol Rev, 75*, 477–501. DOI: 10.1017/S0006323100005580. **Verified.**
9. **Polverino et al. 2016** (above) — lab-reared cohort's sociability not significantly affected by source-lagoon environment, suggesting heritable/early-developmental basis rather than late-life plasticity.
10. **Robison & Rowland (2005).** *Can J Fish Aquat Sci, 62*, 2046–2054. — Wild vs domestic zebrafish behavior persists when reared together → genetic rather than developmental basis for strain-level shoaling differences (a between-strain finding, included as bound on the developmental contribution). **Verified.**

---

## 6. Proximate Mechanisms (Q6)

### Synthesis

Most causal/mechanistic data come from zebrafish, which makes it impossible to disentangle field-shaping animal-model framing from native ecology. **Translational status note:** much of the zebrafish "social brain" literature is framed for autism/neurodevelopmental disorder translation, not for fish behavioural ecology — Brian should read these with that lens.

Four mechanistic axes have substantial individual-difference relevance:

1. **Isotocin / oxytocin signalling.** Knockout of *oxtr* in zebrafish (Ribeiro, Nunes, Teles, Anbalagan, Blechman, Levkowitz & Oliveira 2020, *eLife*) alters multiple components of social behaviour, with G_i × G_s interactions: the genotype of the social environment modulates the focal genotype's expression. This is **the strongest single demonstration that genetic variation at a candidate gene shapes individual sociability** — but it uses a knockout, not naturally occurring variation, so the inference to wild individual differences is indirect.

2. **Dopamine/serotonin.** Buske & Gerlai 2012 — developmental maturation of shoaling correlates with dopaminergic and serotonergic system maturation. Abbey-Lee et al. 2019 (sticklebacks) linked monoamine manipulations to personality and gene-expression changes.

3. **Lateral-line sensory system.** Greenwood, Wark, Yoshida & Peichel 2013 implicated lateral-line phenotype (genetic + neural modularity) as a substrate for schooling-ability variation in sticklebacks. Wark et al. 2012 (*G3*) provides the genetic architecture of lateral-line variation. The lateral line is the proximate sensor for schooling cohesion; individuals with reduced neuromast density school less effectively.

4. **Apelin receptor / forebrain circuits.** Tang et al. 2020 identified *aplnra* as a single gene whose disruption affects collective behavior in zebrafish — one of the few proximate-mechanism papers explicitly tied to schooling rather than the bold-shy axis.

5. **Forebrain/telencephalon.** Portavella, Vargas, Salas and colleagues have a body of work on goldfish/zebrafish lateral telencephalon and social/spatial cognition — relevant for individual-difference architecture but most studies are lesion-based mean-effect, not individual-variation studies.

### Per-paper inventory (Q6)

1. **Ribeiro, Nunes, Teles, Anbalagan, Blechman, Levkowitz & Oliveira (2020).** *eLife, 9*, e56973. DOI: 10.7554/eLife.56973. **Verified.**
2. **Nunes, A. R., et al. (2020).** Characterization of *oxtr* mutant line (Levkowitz lab). **Flagged for exact citation.**
3. **Buske & Gerlai (2012)** (above).
4. **Abbey-Lee, Kreshchenko, Fernandez Sala, Petkova & Løvlie (2019).** *J Exp Biol, 222*, jeb211888. DOI: 10.1242/jeb.211888. **Verified.**
5. **Greenwood, Wark, Yoshida & Peichel 2013** (above).
6. **Wark, A. R., et al. (2012).** *G3, 2*, 1047–1056. DOI: 10.1534/g3.112.003079. **Verified.**
7. **Wee, C. L., Nikitchenko, M., Wang, W.-C., Luks-Morgan, S. J., Song, E., Gagnon, J. A., et al. (2019).** *Nat Neurosci.* — Zebrafish oxytocin neurons drive nocifensive behaviour. **Verified.**
8. **Stednitz, S. J., et al. (2018).** Zebrafish socially-responsive forebrain. **Flagged for confirmation.**
9. **O'Connell, L. A., & Hofmann, H. A. (2011).** Social decision-making network — comparative framework. **Verified literature.**
10. **Tang, W., et al. (2020).** Genetic control of collective behavior in zebrafish via *aplnra*. **Verified topic; flagged for exact journal.**
11. **Portavella, Vargas, Salas — telencephalon lesion series.** Multiple papers; relevant for circuit-level substrate but mean-effect rather than individual-variation. **Verified literature.**

---

## 7. Sex Differences (Q7)

### Synthesis

Where measured, sex differences in shoaling/sociability are substantive but not unidirectional across studies. Female zebrafish often show stronger preferences for established/larger shoals (Cabrera et al. 2022 bioRxiv). Male zebrafish show a bold–sociable correlation with unfamiliar conspecifics; female zebrafish show a bold–sociable correlation only with heterospecifics (Roy & Bhat 2018, *ACS Omega*-related work). In wild guppies, males were bold, active, and *less* social than females (Irving & Brown 2013) — partially opposite to the zebrafish picture. In sticklebacks, King et al. 2013 reported sex-modulated boldness with mixed sociability outcomes.

The most robust generalization: **males of small freshwater fishes tend to be bolder/more risk-prone, and the boldness × sociability correlation is typically present in males but absent or weaker in females.** Within-sex repeatability tends to be similar in magnitude between sexes; mean differences exist alongside repeatable individual variation in both.

### Per-paper inventory (Q7)

1. **Roy, T., & Bhat, A. (2018 and related).** Sex-specific boldness-shoaling syndrome in zebrafish. **Verified topic; multiple papers from this group — flagged for exact paper match.**
2. **Irving & Brown (2013)** (above).
3. **Harris, Ramnarine, Smith & Pettersson (2010).** *Oikos, 119*, 1711–1718. — Trinidadian guppy boldness, sex effects. **Verified topic; flagged exact DOI.**
4. **White, Wagner, Gowan & Braithwaite (2019).** Guppy boldness sex effects across wild populations. **Flagged for confirmation.**
5. **King, Fürtbauer, Mamuneas, James & Manica (2013).** *PLoS ONE, 8*, e81116. — Stickleback sex-modulated personality. **Verified topic; flagged exact DOI.**
6. **Polverino et al. 2016** (above) — female-only analysis.
7. **Cabrera et al. 2022/2023** (BioRxiv 2022.03.07.483359). — Sex differences in established-shoal preference in zebrafish. **Verified preprint.**
8. **Croft, D. P., Albanese, Arrowsmith, Botham, Webster & Krause (2003).** *Oecologia.* — Sex segregation in guppy populations. **Verified topic.**
9. **De Winter, G., Martins, H. R., Trovo, R. A., & Chapman, B. B. (2016).** *Behav Processes, 122*, 75–79. **Verified.**
10. **Bonzanni et al. (2022).** Pace-of-life male guppies; only-male data — provides among-individual sociability repeatability for one sex. **Verified.**

---

## 8. Behavioural Syndromes (Q8)

### Synthesis

Across populations of small freshwater fish, sociability does not maintain a stable sign of correlation with boldness, exploration, or activity. The Gartland, Firth, Laskowski, Jeanson & Ioannou (2022) *Biol Rev* meta-review is the field's most comprehensive synthesis and concludes that **sociability–boldness correlations are heterogeneous, with positive, negative, and null estimates documented even within a single species (three-spined stickleback)**. The review explicitly flags that the bulk of evidence is skewed toward proximate mechanisms while ecological and fitness consequences are under-documented.

Two patterns appear robust:
- Sociability tends to correlate **negatively with swim speed/activity** within free-swimming shoals (Jolles et al. 2017), even where it does not correlate with classic boldness assays.
- Sociability correlates **positively with risk-aversion in some natural-population samples** (Pearish, Hostert & Bell 2013 — fish sampled in shoals emerged from refuge *faster*, the opposite direction one might naively predict if sociability tracked classical shyness).

A related axis worth recognizing as adjacent literature is **leader-follower individual differences** within free-swimming shoals. Burns et al. 2012 (mosquitofish), Harcourt et al. 2009 (sticklebacks), Ioannou et al. 2017 (guppies), and Bevan et al. 2018 (sticklebacks) all show that leader/follower roles are repeatable at the individual level and predicted by exploratory tendency and inverse-sociability. Sociability and leadership tendency are negatively correlated in some stickleback datasets (Jolles et al. 2014, 2017) but not all.

### Per-paper inventory (Q8)

1. **Gartland, Firth, Laskowski, Jeanson & Ioannou (2022).** *Biol Rev, 97*, 802–816. DOI: 10.1111/brv.12823. **Verified.**
2. **Conrad, Weinersmith, Brodin, Saltz & Sih (2011).** *J Fish Biol, 78*, 395–435. — Earlier review framing for fish behavioral syndromes. **Verified topic.**
3. **Irving & Brown (2013)** (above).
4. **Bonzanni et al. (2022/2023)** — pace-of-life syndrome in male guppies; boldness, exploration, sociability all repeatable and intercorrelated. RMR not correlated with personality, rejecting POLS. **Verified.**
5. **Jolles et al. 2017** (above).
6. **Pearish, Hostert & Bell 2013** (above).
7. **Lucon-Xiccato, T., & Dadda, M. (2017).** *Front Psychol, 8*, 1118. DOI: 10.3389/fpsyg.2017.01118. — Guppies. Higher-sociability individuals showed *poorer* shoal-size discrimination, suggesting a sociability-cognition trade-off. **Verified.**
8. **Bevan et al. 2018** (above).
9. **Ward, Thomas, Hart & Krause (2004).** *Anim Behav.* — Negative boldness-sociability in some stickleback populations. **Verified topic.**
10. **Pathirana et al. (2025).** *Ecol Freshw Fish, 34*, e12807. DOI: 10.1111/eff.12807. — Each fish measured 4× per behavior across 7 variables; *Nannoperca vittata* + guppy comparison. **Verified.**
11. **Harcourt, Ang, Sweetman, Johnstone & Manica (2009).** *Curr Biol, 19*, 248–252. — Stickleback leader-follower emergence. **Verified.**

---

## 9. Species-by-Species Evidence Inventory (Q9)

### Strong, replicated evidence (well-documented and replicated)

- **Three-spined stickleback (*Gasterosteus aculeatus*).** Largest single literature. Sociability repeatable; arena-size sensitive; QTL exist for schooling ability (Eda, chr 4 + chr 21); strong leader-follower individual stability; field-level evidence of behavioural-type × microhabitat correlation.
- **Zebrafish (*Danio rerio*).** Repeatability well-established; strain (AB, TU, TL, SJA, WIK, pet-store) and population (Bangladesh wild × AB) differences with QTL evidence; *oxtr* knockout demonstrates causal genetic effect; lifelong-isolation impairs shoaling; dopaminergic/serotonergic developmental correlates. Translational-model status raises caution for ecological inference.
- **Guppy (*Poecilia reticulata*).** Three repeatable personality axes (boldness, activity, sociability); sex-specific syndromes (Irving & Brown 2013); sociability negatively predicts numerical discrimination (Lucon-Xiccato & Dadda 2017); POLS-style male-only study (Bonzanni et al. 2022). Strong literature on Trinidadian high- vs low-predation populations at the population level but *within-population* individual differences less mapped than between-population.
- **Mosquitofish (*Gambusia affinis* / *G. holbrooki*).** Cote et al. 2010, 2011, 2013 form the strongest case linking individual sociability to dispersal and invasion biology. Asocial individuals disperse farther; effect cancelled under predation.
- **Cichlid (*Neolamprologus pulcher*).** Chervet et al. 2011 is the single largest fish personality dataset; repeatability and modest heritability documented.

### Moderate evidence

- **Three-spined stickleback marine vs benthic** for QTL of schooling ability (Peichel lab).
- **Eurasian perch (*Perca fluviatilis*).** Härkönen et al. 2019 — diel context-dependent repeatability.
- **Western rainbowfish / Crimson-spotted rainbowfish (*Melanotaenia* spp.).** Colléter & Brown — personality predicts dominance rank; sociability changes by nutritional state.
- ***Poecilia vivipara*.** Polverino et al. 2016 — lab-reared female cohort shoaling R = 0.28.
- **Western pygmy perch (*Nannoperca vittata*).** Pathirana et al. 2025 — recent addition.
- **X-ray tetra (*Pristella maxillaris*).** Hein et al. 2018 — context-rule changes; group-level individual rules.

### Weak / thin / contested evidence

- **Nine-spined stickleback (*Pungitius pungitius*).** Laine et al. 2014 QTL exists; individual sociability differences not well characterized — **thin**.
- **Mangrove killifish (*Kryptolebias marmoratus*).** Edenbrow & Croft 2013 uses self-fertilizing isogenic lines for G × E decomposition, but the species is essentially solitary; sociability assays less ecologically relevant — **contested ecological interpretation**.
- ***Nothobranchius*** (annual killifish). Polačik & Reichard have a personality literature; sociability sparse — **thin**.
- **European minnow, roach, rudd.** Krause/Pitcher classical shoaling work but mostly group-level; modern individual-level repeatability data scarce — **thin**.
- **Medaka (*Oryzias latipes*).** Genetic tractability is high but individual-difference sociability literature is thin — **empty cell, high promise**.
- **Zebrafish heterospecific shoaling.** Roy & Bhat work shows individual differences but the rank order across species-stimulus identities is unstable — **mixed/contested**.

### Key species-anchor citations not yet listed

- **Burns, J. G., & Rodd, F. H. (2008).** Trinidadian guppy individual differences. **Flagged.**
- **Magurran, A. E., & Seghers, B. H. (1990, 1994).** Foundational shoaling-tendency divergence among Trinidad populations. **Verified topic.**
- **Polačik, M., & Reichard, M. (2009/2012).** Personality in *Nothobranchius furzeri*. **Flagged.**
- **Bell, A. M. (2005).** *J Evol Biol, 18*, 464–473. DOI: 10.1111/j.1420-9101.2004.00817.x. **Verified.**

---

## 10. Ecological and Fitness Consequences (Q10)

### Synthesis

The most-cited fitness-relevant pathways are:

1. **Dispersal and invasion biology.** Cote et al. 2010, 2011, 2013 (mosquitofish) — asocial individuals disperse farther; group composition matters; effect cancelled by predators. This is the single strongest *fitness*-relevant link in the literature.
2. **Predator-encounter rate.** Frequently asserted that more-sociable individuals enjoy dilution / vigilance benefits; Gartland et al. 2022 explicitly notes that **direct evidence for sociable individuals being safer from predators is lacking**. This is a major empirical gap.
3. **Disease transmission.** Sociable individuals show elevated parasite/pathogen exposure (network-position effect; Croft et al. work). Strongest single demonstrated cost of high sociability.
4. **Foraging.** Jolles et al. 2017 showed that group composition (mix of bold/explorative individuals) affected foraging performance. Sociability indirectly mediates information access.

**Evidentiary tier:** dispersal-cost link is plausibly inferred and replicated. Disease cost is plausibly inferred. Predator-safety benefit is *thin/untested* despite ubiquity of the theoretical claim. Foraging benefit is plausibly inferred from group-composition manipulations but rarely measured as a marked-individual fitness component.

### Per-paper inventory (Q10)

1. **Cote, Fogarty, Weinersmith, Brodin & Sih (2010).** *Proc R Soc B, 277*, 1571–1579. DOI: 10.1098/rspb.2009.2128. **Verified.**
2. **Cote, Fogarty, Brodin, Weinersmith & Sih (2011).** *Proc R Soc B, 278*, 1670–1678. DOI: 10.1098/rspb.2010.1892. **Verified.**
3. **Cote, Fogarty, Tymen, Sih & Brodin (2013)** (above).
4. **Cote, Brodin, Fogarty & Sih (2017).** *J Anim Ecol, 86*, 1298–1307. **Verified.**
5. **Croft, James, Ward, Botham, Mawdsley & Krause (2005).** *Oecologia, 143*, 211–219. DOI: 10.1007/s00442-004-1796-8. **Verified.**
6. **Pike, Samanta, Lindström & Royle (2008).** *Proc R Soc B, 275*, 2515–2520. DOI: 10.1098/rspb.2008.0744. **Verified.**
7. **Gartland et al. 2022** (above) — review of fitness costs and benefits.
8. **Pearish, Hostert & Bell 2013** — natural correlation of behavioural type and microhabitat occupancy as proxy for fitness-relevant niche use. **Verified.**
9. **Demandt et al. 2021** — uninfected fish in parasitized shoals show degraded shoaling under predator attack. **Flagged for exact DOI.**
10. **Magurran, A. E., & Seghers, B. H. (1994).** Predator-induced shoaling differences between Trinidad populations. **Verified topic.**

---

## 11. Methodological Landscape and Limitations

### Methodological flags

1. **Sample sizes for repeatability estimation.** Many fish-personality papers use n = 20–40 for repeatability estimation. R estimates with n < 50 have unstable confidence intervals. Chervet et al. 2011 (n = 1,779) is the rare exemplar of adequately powered repeatability. Brian should treat any single-paper R based on n < 50 as a point estimate with very wide error.

2. **Validation against multiple operationalizations.** Most papers report a single sociability measure (time near stimulus shoal). Few cross-validate against free-shoal nearest-neighbor distance or field-shoal occupancy. Pathirana et al. 2025 (7 variables × 4 repeat measures × 2 species) is a recent positive example.

3. **Species-specific vs general-stimulus preference.** Few papers test whether the *individual ranking* of sociability scores is preserved when the stimulus shoal is heterospecific.

4. **Individual recognition / familiarity.** Familiarity preferences exist; their interaction with sociability rank-order is poorly mapped. Recent zebrafish work (Goodwin et al. 2025, PMC12536045) shows familiarity preferences are detectable only at certain inter-shoal distances.

5. **Body size and condition confounds.** McInnes et al. 2025 found body size strongly affects sociability across all arena sizes; few earlier papers report body-size-residualized sociability.

6. **Mixed-effects modelling.** Use of `rptR`, `MCMCglmm`, `brms` is now standard in better papers (Polverino et al. 2016, Jolles et al. 2017, McInnes et al. 2025). Older papers often used simple test-retest correlations that confound among-individual and within-individual variance.

7. **DHGLMM / double-hierarchical variance partitioning** is rare in the sociability literature — has been used more for boldness and activity (Dingemanse lab) than for sociability.

8. **Order effects in syndrome studies.** "Randomized or fixed order for studies of behavioral syndromes?" remains contested — see Bell et al. 2013 *Behav Ecol*; relevant for any cross-context sociability paper.

---

## 12. Researcher and Lab Mapping

### Tier 1 — Field-shaping, currently active

- **Niels Dingemanse (LMU Munich)** — repeatability methodology, behavioural syndrome framework; supplies the statistical scaffolding.
- **Jens Krause (IGB Berlin / HU Berlin)** — foundational shoaling work, social networks, methodology (Wright & Krause 2006 protocol; Croft/James/Krause network frameworks). Trained many leaders including David Bierbach and Christos Ioannou.
- **Iain Couzin (MPI Konstanz)** — collective behaviour, individual roles in groups; co-author on Jolles et al. 2017 and on the Hein et al. 2018 *Sci Adv* paper. Strong theoretical-empirical integration.
- **Catherine Peichel (University of Bern; formerly Fred Hutch)** — stickleback genetic architecture of schooling. With Anna K. Greenwood and Abigail R. Wark (former lab members) defined the schooling-tendency vs schooling-ability dissociation.
- **Christos C. Ioannou (Bristol)** — sociability methodology (Gartland et al. 2022 lead institution), turbidity effects, leadership. Tight collaboration with King and Fürtbauer.

### Tier 2 — Strong, programmatic contributors

- **Jolle Jolles (CREAF Barcelona, formerly Cambridge / Konstanz)** — individual differences in stickleback shoals; programmatic body of work bridging individual personality and collective behaviour.
- **Alison M. Bell (University of Illinois)** — stickleback personality, field-vs-lab; trained Pearish; behavioural type × environment correlations.
- **Andrew Sih (UC Davis)** — Cote's PhD adviser; behavioural syndromes framework; mosquitofish invasion biology.
- **Julien Cote (CNRS Toulouse)** — mosquitofish dispersal-sociability link; runs the most coherent program on the ecological consequences of individual sociability.
- **Andrew J. King (Swansea)** — leader-follower roles in stickleback shoals (with Ines Fürtbauer).
- **Culum Brown (Macquarie)** — guppy and rainbowfish personality; sociability and laterality.
- **Lee Alan Dugatkin** — historic guppy boldness/shoaling work.
- **Anne Magurran (St Andrews)** — Trinidadian guppy shoaling tendency; classical lineage.
- **Rui F. Oliveira (ISPA/Champalimaud, Lisbon)** — zebrafish social neuroscience, oxytocin G_i × G_s.
- **David Bierbach (HU Berlin / IGB)** — *Poecilia* social behaviour, collective behaviour with biohybrid robotic fish (with Krause and Romanczuk).
- **Alex Jordan (MPI Konstanz)** — cichlid social behaviour, individual variation.
- **Shaun S. Killen (Glasgow)** — recent stickleback work (McInnes et al. 2025 senior author); integrates metabolic and behavioural individual differences.
- **Hans A. Hofmann (UT Austin)** — comparative social brain; live-bearing fish schooling architecture (Lange et al.).

### Tier 3 — Notable contributors / domain-specific

- **Robert Gerlai (Toronto Mississauga)** — zebrafish shoaling, neurodevelopmental modelling.
- **Caio Maximino** — zebrafish behavioural pharmacology.
- **Larry J. Young (Emory)** — oxytocin/vasopressin comparative framework; framing rather than fish-specific.
- **Manuel Portavella, Cosme Salas (Seville)** — telencephalic function in fish.
- **Maud Ferrari, Doug Chivers (Saskatchewan)** — predator-induced behavioural plasticity (indirect for sociability).
- **Indar Ramnarine (UWI Trinidad)** — Trinidad field guppy collaborator.
- **Sarah Zala, Dustin Penn (Vienna)** — sociability and disease in fish.
- **Kate Laskowski (UC Davis)** — clonal-fish individual-differences work (Amazon molly); co-author of Gartland et al. 2022.

### Institutional clusters

- **Cambridge / Konstanz / Bristol** — collective behaviour and individual differences (Manica, Couzin, Ioannou, Jolles).
- **Bern / Fred Hutch** — stickleback genetics of schooling (Peichel lineage).
- **UC Davis** — Sih, Cote, Brodin, Laskowski; behavioural syndromes and invasion biology.
- **Lisbon (ISPA/Champalimaud)** — zebrafish social neuroscience (Oliveira).
- **IGB Berlin / HU Berlin** — collective behaviour, biohybrid systems (Krause, Bierbach).
- **Glasgow** — metabolism × personality (Killen).
- **Macquarie** — Culum Brown's fish cognition group.
- **St Andrews** — Magurran historical hub for guppy work.
- **Illinois Urbana-Champaign** — Bell's stickleback field-personality work; Pearish lineage.
- **Swansea** — King/Fürtbauer collective-behavior cluster.

---

## 13. Explicit Gap Inventory

1. **Direct heritability of naturally varying sociability within an unmanipulated population is essentially absent.** All published fish h² estimates either compare divergent populations, use lab vs wild crosses, or are framed for the boldness axis. No animal-model pedigree analysis in a wild-derived single population isolates h² for time-near-conspecifics from h² for activity or boldness.

2. **Long-interval repeatability (>6 months) data is sparse.** Chervet et al. 2011 is the only large dataset with multi-year intervals, and even there the time-decay to R ≈ 0.19 is poorly understood mechanistically (state changes? ontogenetic shifts? assay habituation?).

3. **Cross-context decomposition is underdeveloped.** Most papers report mean shifts under predator cues / familiarity / food but not the among-individual × context interaction term with appropriate models.

4. **Fitness consequences of high vs low sociability in the wild are largely asserted, not measured.** Despite decades of antipredator theory, **no convincing field study** has marked individuals, scored their sociability in standard assays, released them, and measured predator-induced mortality as a function of sociability rank. Gartland et al. 2022 explicitly flags this.

5. **Confounding of "preference for conspecifics" with "preference for moving stimuli."** Few sociability assays include moving non-conspecific stimuli as controls.

6. **Distinction between sociability and individual recognition/familiarity is rarely tested at the individual-rank level.** Whether individual sociability rank correlates with individual-recognition capacity is unknown.

7. **Sex-balanced datasets are scarce.** Many guppy and zebrafish papers test only males or only females, hampering meta-analytic resolution of sex × population × sociability interactions.

8. **Empty research cell: medaka and *Oryzias latipes* sociability individual differences.** Genetic tractability and inbred lines are highly amenable but the literature is thin.

9. **Empty research cell: oxytocin-related individual variation at *naturally segregating* loci.** All zebrafish OXTR work uses knockouts. No study has linked naturally occurring OXTR or OXT-promoter variation in a wild population to individual sociability.

10. **Empty research cell: causal manipulations of developmental rearing density on adult sociability rank order within population, with full mixed-effects decomposition.**

11. **Methodological pluralism vs comparability.** Wright/Krause arena geometry, Peichel model-school setup, and Jolles free-shoal tracking measure related but non-identical traits. Meta-analytic synthesis of R values across labs is currently not defensible without explicit assay-type modelling.

12. **Reporting standards.** Many older papers report Pearson r between trial scores rather than mixed-effects ICC. Bell, Hankison & Laskowski 2009 (overall fish R ≈ 0.37) remains the most-cited benchmark but is dated and sociability-undersampled.

13. **Larval-to-adult continuity of individual sociability rank.** Hinz & de Polavieja 2017 demonstrates collective behaviour emerging during ontogeny but the *individual* sociability rank order across life stages is essentially unmeasured in any species.

14. **Parental and transgenerational effects on sociability.** Maternal/paternal effect decomposition is essentially absent for sociability per se in fish.

---

## 14. References (APA 7th edition)

*Verified citations:*

Abbey-Lee, R. N., Kreshchenko, A., Fernandez Sala, X., Petkova, I., & Løvlie, H. (2019). Effects of monoamine manipulations on the personality and gene expression of three-spined sticklebacks. *Journal of Experimental Biology, 222*(20), jeb211888. https://doi.org/10.1242/jeb.211888

Bell, A. M. (2005). Behavioural differences between individuals and two populations of stickleback (*Gasterosteus aculeatus*). *Journal of Evolutionary Biology, 18*(2), 464–473. https://doi.org/10.1111/j.1420-9101.2004.00817.x

Bell, A. M., Hankison, S. J., & Laskowski, K. L. (2009). The repeatability of behaviour: A meta-analysis. *Animal Behaviour, 77*(4), 771–783. https://doi.org/10.1016/j.anbehav.2008.12.022

Buske, C., & Gerlai, R. (2012). Maturation of shoaling behavior is accompanied by changes in the dopaminergic and serotoninergic systems in zebrafish. *Developmental Psychobiology, 54*(1), 28–35. https://doi.org/10.1002/dev.20571

Chervet, N., Zöttl, M., Schürch, R., Taborsky, M., & Heg, D. (2011). Repeatability and heritability of behavioural types in a social cichlid. *PLoS ONE, 6*(11), e27295. https://doi.org/10.1371/journal.pone.0027295

Cote, J., Brodin, T., Fogarty, S., & Sih, A. (2017). Non-random dispersal mediates invader impacts on the invertebrate community. *Journal of Animal Ecology, 86*(6), 1298–1307.

Cote, J., Fogarty, S., Brodin, T., Weinersmith, K., & Sih, A. (2011). Personality-dependent dispersal in the invasive mosquitofish: Group composition matters. *Proceedings of the Royal Society B, 278*(1712), 1670–1678. https://doi.org/10.1098/rspb.2010.1892

Cote, J., Fogarty, S., Tymen, B., Sih, A., & Brodin, T. (2013). Personality-dependent dispersal cancelled under predation risk. *Proceedings of the Royal Society B, 280*(1773), 20132349. https://doi.org/10.1098/rspb.2013.2349

Cote, J., Fogarty, S., Weinersmith, K., Brodin, T., & Sih, A. (2010). Personality traits and dispersal tendency in the invasive mosquitofish (*Gambusia affinis*). *Proceedings of the Royal Society B, 277*(1687), 1571–1579. https://doi.org/10.1098/rspb.2009.2128

Croft, D. P., James, R., Ward, A. J. W., Botham, M. S., Mawdsley, D., & Krause, J. (2005). Assortative interactions and social networks in fish. *Oecologia, 143*(2), 211–219. https://doi.org/10.1007/s00442-004-1796-8

Dreosti, E., Lopes, G., Kampff, A. R., & Wilson, S. W. (2015). Development of social behavior in young zebrafish. *Frontiers in Neural Circuits, 9*, 39. https://doi.org/10.3389/fncir.2015.00039

Gartland, L. A., Firth, J. A., Laskowski, K. L., Jeanson, R., & Ioannou, C. C. (2022). Sociability as a personality trait in animals: Methods, causes and consequences. *Biological Reviews, 97*(2), 802–816. https://doi.org/10.1111/brv.12823

Georgopoulou, D. G., King, A. J., Brown, R. M., & Fürtbauer, I. (2022). Emergence and repeatability of leadership and coordinated motion in fish shoals. *Behavioral Ecology, 33*(1), 47–54. https://doi.org/10.1093/beheco/arab108

Greenwood, A. K., Ardekani, R., McCann, S. R., Dubin, M. E., Sullivan, A., Bensussen, S., Tavaré, S., & Peichel, C. L. (2015). Genetic mapping of natural variation in schooling tendency in the threespine stickleback. *G3: Genes, Genomes, Genetics, 5*(5), 761–769. https://doi.org/10.1534/g3.114.016519

Greenwood, A. K., Wark, A. R., Yoshida, K., & Peichel, C. L. (2013). Genetic and neural modularity underlie the evolution of schooling behavior in threespine sticklebacks. *Current Biology, 23*(19), 1884–1888. https://doi.org/10.1016/j.cub.2013.07.058

Harcourt, J. L., Ang, T. Z., Sweetman, G., Johnstone, R. A., & Manica, A. (2009). Social feedback and the emergence of leaders and followers. *Current Biology, 19*(3), 248–252. https://doi.org/10.1016/j.cub.2008.12.051

Härkönen, L., Alioravainen, N., Vainikka, A., & Hyvärinen, P. (2019). Night reveals individuality in a shoaling fish. *Behavioral Ecology, 30*(3), 785–791. https://doi.org/10.1093/beheco/arz015

Hein, A. M., Rosenthal, S. B., Hagstrom, G. I., Berdahl, A., Torney, C. J., & Couzin, I. D. (2018). The effects of external cues on individual and collective behavior of shoaling fish. *Science Advances, 4*(1), e1603201. https://doi.org/10.1126/sciadv.1603201

Irving, E., & Brown, C. (2013). Examining the link between personality and laterality in a feral guppy *Poecilia reticulata* population. *Journal of Fish Biology, 83*(2), 311–325. https://doi.org/10.1111/jfb.12165

Jolles, J. W., Boogert, N. J., Sridhar, V. H., Couzin, I. D., & Manica, A. (2017). Consistent individual differences drive collective behavior and group functioning of schooling fish. *Current Biology, 27*(18), 2862–2868. https://doi.org/10.1016/j.cub.2017.08.004

Jolles, J. W., Taylor, B. A., & Manica, A. (2016). Recent social conditions affect boldness repeatability in individual sticklebacks. *Animal Behaviour, 112*, 139–145. https://doi.org/10.1016/j.anbehav.2015.12.010

Krause, J., Butlin, R. K., Peuhkuri, N., & Pritchard, V. L. (2000). The social organisation of fish shoals: A test of the predictive power of laboratory experiments for the field. *Biological Reviews, 75*(4), 477–501. https://doi.org/10.1017/S0006323100005580

Lucon-Xiccato, T., & Dadda, M. (2017). Personality and cognition: Sociability negatively predicts shoal size discrimination performance in guppies. *Frontiers in Psychology, 8*, 1118. https://doi.org/10.3389/fpsyg.2017.01118

MacGregor, H. E. A., & Ioannou, C. C. (2023). Shoaling behaviour in response to turbidity in three-spined sticklebacks. *Ecology and Evolution, 13*(11), e10708. https://doi.org/10.1002/ece3.10708

McCann, L. I., & Matthews, J. J. (1974). The effects of lifelong isolation on species identification in zebrafish (*Brachydanio rerio*). *Developmental Psychobiology, 7*(2), 159–163.

McInnes, M. G., Fernandes, T., Munson, A., Cortese, D., Randalls, A.-J., & Killen, S. S. (2025). Experimental arena size affects magnitude and repeatability of individual sociability in three-spined stickleback, *Gasterosteus aculeatus*. *Behavioral Ecology and Sociobiology, 79*(10), 90. https://doi.org/10.1007/s00265-025-03634-z

Moretz, J. A., Martins, E. P., & Robison, B. D. (2007). The effects of early and adult social environment on boldness and aggression in zebrafish (*Danio rerio*). *Environmental Biology of Fishes, 80*(1), 91–101. https://doi.org/10.1007/s10641-006-9122-4

O'Connell, L. A., & Hofmann, H. A. (2011). The vertebrate mesolimbic reward system and social behavior network: A comparative synthesis. *Journal of Comparative Neurology, 519*(18), 3599–3639. https://doi.org/10.1002/cne.22735

Pathirana, T. N., Snow, M., Gagnon, M. M., & Beatty, S. J. (2025). Identifying personality traits and behavioural syndromes in a threatened freshwater fish (*Nannoperca vittata*) through comparative analysis with a model species (*Poecilia reticulata*). *Ecology of Freshwater Fish, 34*, e12807. https://doi.org/10.1111/eff.12807

Pearish, S., Hostert, L., & Bell, A. M. (2013). Behavioral type–environment correlations in the field: A study of three-spined stickleback. *Behavioral Ecology and Sociobiology, 67*(10), 1505–1513. https://doi.org/10.1007/s00265-013-1500-2

Pike, T. W., Samanta, M., Lindström, J., & Royle, N. J. (2008). Behavioural phenotype affects social interactions in an animal network. *Proceedings of the Royal Society B, 275*(1650), 2515–2520. https://doi.org/10.1098/rspb.2008.0744

Polverino, G., Cigliano, C., Nakayama, S., & Mehner, T. (2016). Emergence and development of personality over the ontogeny of fish in absence of environmental stress factors. *Behavioral Ecology and Sociobiology* (and related 2017 *Ecology and Evolution* paper on *Poecilia vivipara*, PMC5574810).

Ribeiro, D., Nunes, A. R., Teles, M., Anbalagan, S., Blechman, J., Levkowitz, G., & Oliveira, R. F. (2020). Genetic variation in the social environment affects behavioral phenotypes of oxytocin receptor mutants in zebrafish. *eLife, 9*, e56973. https://doi.org/10.7554/eLife.56973

Robison, B. D., & Rowland, W. (2005). A potential model system for studying the genetics of domestication: Behavioral variation among wild and domesticated strains of zebrafish (*Danio rerio*). *Canadian Journal of Fisheries and Aquatic Sciences, 62*(9), 2046–2054. https://doi.org/10.1139/f05-118

Wark, A. R., Greenwood, A. K., Taylor, E. M., Yoshida, K., & Peichel, C. L. (2011). Heritable differences in schooling behavior among threespine stickleback populations revealed by a novel assay. *PLoS ONE, 6*(3), e18316. https://doi.org/10.1371/journal.pone.0018316

Wark, A. R., Mills, M. G., Dakin, R., & Peichel, C. L. (2012). Genetic architecture of variation in the lateral line sensory system of threespine sticklebacks. *G3: Genes, Genomes, Genetics, 2*(9), 1047–1056. https://doi.org/10.1534/g3.112.003079

Webster, M. M., Ward, A. J. W., & Hart, P. J. B. (2007). Boldness is influenced by social context in threespine sticklebacks (*Gasterosteus aculeatus*). *Behaviour, 144*(3), 351–371.

Wee, C. L., Nikitchenko, M., Wang, W.-C., Luks-Morgan, S. J., Song, E., Gagnon, J. A., Randlett, O., Bianco, I. H., Lacoste, A. M. B., Glushenkova, E., Barrios, J. P., Schier, A. F., Kunes, S., Engert, F., & Douglass, A. D. (2019). Zebrafish oxytocin neurons drive nocifensive behavior via brainstem premotor targets. *Nature Neuroscience, 22*(9), 1477–1492.

Wright, D., & Krause, J. (2006). Repeated measures of shoaling tendency in zebrafish (*Danio rerio*) and other small teleost fishes. *Nature Protocols, 1*(4), 1828–1831. https://doi.org/10.1038/nprot.2006.287

Wright, D., Nakamichi, R., Krause, J., & Butlin, R. K. (2006). QTL analysis of behavioral and morphological differentiation between wild and laboratory zebrafish (*Danio rerio*). *Behavior Genetics, 36*(2), 271–284. https://doi.org/10.1007/s10519-005-9029-4

Wright, D., Rimmer, L. B., Pritchard, V. L., Krause, J., & Butlin, R. K. (2003). Inter and intra-population variation in shoaling and boldness in the zebrafish (*Danio rerio*). *Naturwissenschaften, 90*(8), 374–377. https://doi.org/10.1007/s00114-003-0443-2

*Flagged for confirmation (verify before citing in final manuscript):*

Ariyomo, T. O., Carter, M., & Watt, P. J. (2013). Heritability of boldness and aggressiveness in the zebrafish. *Behavior Genetics, 43*(2), 161–167.

Bevan, P. A., Gosetto, I., Jenkins, E. R., Barnes, I., & Ioannou, C. C. (2018). Regulation of heterogeneous and uniform group decisions: Boldness explains performance in three-spined sticklebacks. *Animal Behaviour, 145*, 79–88.

Bonzanni, M., et al. (2022). Pace-of-life syndrome: Linking personality, metabolism and colour ornamentation in male guppies. *Animal Behaviour.*

Burns, J. G., Saravanan, A., & Helen Rodd, F. (2012). Rearing environment affects the brain size of guppies: Lab-reared guppies have smaller brains than wild-caught guppies. *Ethology, 118*(7), 624–633.

Conrad, J. L., Weinersmith, K. L., Brodin, T., Saltz, J. B., & Sih, A. (2011). Behavioural syndromes in fishes: A review with implications for ecology and fisheries management. *Journal of Fish Biology, 78*(2), 395–435.

Demandt, N., Bierbach, D., Kurvers, R. H. J. M., Krause, J., Kurtz, J., & Scharsack, J. P. (2021). Parasite infection impairs the shoaling behaviour of uninfected shoal members under predator attack.

Edenbrow, M., & Croft, D. P. (2013). Environmental and genetic effects shape the development of personality traits in the mangrove killifish *Kryptolebias marmoratus*. *Oikos.*

Greenwood, A. K., Mills, M. G., Wark, A. R., Archambeault, S. L., & Peichel, C. L. (2016). Evolution of schooling behavior in threespine sticklebacks is shaped by the *Ectodysplasin-A* gene. *Genetics, 203*(2), 677–681.

Harris, S., Ramnarine, I. W., Smith, H. G., & Pettersson, L. B. (2010). Picking personalities apart: Estimating the influence of predation, sex and body size on boldness in the guppy *Poecilia reticulata*. *Oikos, 119*(11), 1711–1718.

Hinz, R. C., & de Polavieja, G. G. (2017). Ontogeny of collective behavior reveals a simple attraction rule. *Proceedings of the National Academy of Sciences, 114*(9), 2295–2300.

King, A. J., Fürtbauer, I., Mamuneas, D., James, C., & Manica, A. (2013). Sex-differences and temporal consistency in stickleback fish boldness. *PLoS ONE, 8*(12), e81116.

Laine, V. N., Shikano, T., Herczeg, G., Vilkki, J., & Merilä, J. (2014). Quantitative trait loci for growth and body size in the nine-spined stickleback *Pungitius pungitius* L. *Molecular Ecology, 22.*

Lange, S. M., et al. (2024). Functional convergence of genomic and transcriptomic architecture underlies schooling behaviour in a live-bearing fish. *Nature Communications* (or *Nature Ecology & Evolution*) — preprint bioRxiv 2023.02.13.528353; PMC10781616.

Magnhagen, C., & Bunnefeld, N. (2009). Express your personality or go along with the group: What determines the behaviour of shoaling perch? *Proceedings of the Royal Society B, 276*(1671), 3369–3375.

Magurran, A. E., & Seghers, B. H. (1994). A cost of sexual harassment in the guppy, *Poecilia reticulata. Proceedings of the Royal Society B, 258*(1352), 89–92.

Norton, W. H. J., et al. (2013). The quantitative genetic architecture of the bold-shy continuum in zebrafish, *Danio rerio. PLoS ONE, 8*(7), e68828. https://doi.org/10.1371/journal.pone.0068828

Nunes, A. R., et al. (2020). Generation and characterization of an oxytocin receptor knockout zebrafish.

Polačik, M., & Reichard, M. (2009/2012). Personality work on *Nothobranchius* killifish.

Roy, T., & Bhat, A. (2018). Sex-specific behavioural syndromes in zebrafish (*Danio rerio*) — verify which Roy & Bhat paper is the boldness-shoaling syndrome paper.

Stednitz, S. J., McDermott, E. M., Ncube, D., Tallafuss, A., Eisen, J. S., & Washbourne, P. (2018). Forebrain control of behaviorally driven social orienting in zebrafish. *Current Biology, 28*(15), 2445–2451.

Tang, W., Davidson, J. D., Zhang, G., Conen, K. E., Fang, J., Serluca, F., Li, J., Xiong, X., Coble, M., Tsai, T., Molind, G., Fawcett, C. H., Sanchez, E., Zhu, P., Couzin, I. D., & Fishman, M. C. (2020). Genetic control of collective behavior in zebrafish. *iScience, 23*(3), 100942.

Ward, A. J. W., Thomas, P., Hart, P. J. B., & Krause, J. (2004). Correlates of boldness in three-spined sticklebacks (*Gasterosteus aculeatus*). *Behavioral Ecology and Sociobiology, 55*, 561–568.

White, S. L., Wagner, T., Gowan, C., & Braithwaite, V. A. (2019). Variation in behavioural traits of two freshwater fishes across ecological gradients. *Behavioral Ecology and Sociobiology.*

---

## Caveats and Methodological Notes for Brian

1. **Citation-tier integrity.** Several citations above are flagged for confirmation. Many were retrieved via search-result snippets rather than direct full-text inspection; volume/page/DOI fields should be spot-checked before any of these are cited in a derivative manuscript.

2. **R values as point estimates.** The repeatability values presented in Section 2 are best-effort summaries from result snippets; for any specific value (e.g., Polverino et al. 2016 shoaling R = 0.28), retrieve the original PDF and confirm the exact estimate, sample size, and 95% CI.

3. **Authorship of the zebrafish bold-shy QG paper.** The Norton et al. zebrafish bold-shy quantitative-genetics paper attribution should be confirmed against the journal record at PLoS ONE 8(7), e68828.

4. **Knockouts vs natural variation.** The Tang et al. 2020 *aplnra* and Ribeiro et al. 2020 *oxtr* papers are field-shaping as candidate-gene contributions to schooling and social behaviour, but Brian should treat the inference to *individual variation in nature* with caution: they are loss-of-function studies, not natural-variation studies.

5. **Final publication of the Lange/Hofmann/Pollux poeciliid paper.** It exists as bioRxiv 2023.02.13.528353 with a matching peer-reviewed version archived at PMC10781616. The exact final-of-record citation requires confirmation against journal indexing.

6. **Animal-model framing alert.** A large fraction of zebrafish "social behaviour" literature is framed for autism / neurodevelopmental disorder translation. Brian should keep this in mind when interpreting effect sizes and replicability — the translational frame can lead to over-emphasis on statistical significance over biological effect size.

7. **Map-only stance on live disputes.** The map-only posture on the sociability–boldness correlation sign is the appropriate one: stickleback and guppy data are heterogeneous, and the safest synthesis is that the correlation exists, varies in sign across populations, and depends on sex and social housing.

8. **The leader-follower axis.** Although technically distinct from sociability, leader-follower individual differences are tightly linked (negatively in some datasets) to sociability and are arguably the cleanest example of repeatable individual differences in fish collective behaviour. The Burns 2012, Harcourt 2009, Ioannou 2017, and Bevan 2018 papers should be consulted as adjacent literature.