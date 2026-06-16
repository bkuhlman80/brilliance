# **Proof of Concept Plan: Recoverability of Combinatorial Loading Models**  
  
*Working doc. May 2026\. Audience: Brian and future Claude in the ABHOP project.*  
  
---  
  
## **What this is**  
  
A scoped, executable plan for getting a working proof of concept for the recoverability paper before pitching the project to Butner. The PoC is cheap insurance against three failure modes: a math derivation that doesn't survive contact with simulation, a Jaccard signature that's messier than promised under realistic conditions, and a Butner pitch that gets reshaped before we know what we're recruiting for.  
  
The PoC is not the paper. It is the smallest experiment that confirms the central claims work. If it confirms them, we have a result to show Butner. If it doesn't, we've learned what we needed to learn at low cost.  
  
## **What "done" means**  
  
The PoC is done when we can demonstrate, on simulated data:  
  
* The Jaccard correlation prediction holds under stated baseline assumptions (equal loadings, unit-variance primaries, uncorrelated residuals)    
* EFA-with-rotation systematically fails to recover the combinatorial loading structure even at large sample sizes    
* A confirmatory Jaccard test discriminates the true assignment from competing assignments at modest sample sizes    
* The robustness envelope is roughly characterized — we know which deviations from baseline (loading inequality, residual correlation, finite-N noise) the test tolerates and which it doesn't  
  
These are the four results that would make the recruiting pitch concrete.  
  
## **Jon Butner**  
  
Jonathan E. Butner is a professor of psychology at the University of Utah and current chair of the department. PhD from Arizona State (2002), trained as a social psychologist with a heavy quantitative focus. Around 8,500 Google Scholar citations. His career has been spent developing dynamical-systems methods for psychological data, often in domains where standard psychometrics doesn't fit cleanly — most prominently a long-running collaboration with Cynthia Berg on couples managing type 1 diabetes.  
  
He's outside the psychometrics mainstream in useful ways. Member of the Society for Chaos Theory in Psychology and Life Sciences; his methods book *Quantitative Reasoning Under a Dynamical Social Science* (2017) is self-published; his earlier work includes Boolean XOR rings and Sierpinski-gasket topology — combinatorial-structure problems most personality researchers would never go near. The recoverability paper is built around a sparsely-loaded combinatorial factor structure that simple-structure CFA wasn't built to handle, and he has the right intuitions for that kind of object. He also has the methods chops to verify the math, the credentialed track record to buffer the credentialism friction at *Psychological Methods*, and a department chair's access to grad-student labor for implementation work.  
  
He was on Brian's dissertation committee, and Brian's read is that he likes him. The risk Brian flagged: Butner is "quirky" and "often overcomplicates things." Concretely, he'll want to dynamicize the test. He'll see the rolling window across levels and immediately think *that's a state-space evolution; let's model the configurational dynamics in phase space*. He'll see the Venn regions and think *those are attractor basins; let's characterize their topology*. None of this is wrong — it's potentially a genuinely interesting follow-up — but it would explode the scope of the static recoverability paper into something different. The two-paper sequencing in the recruiting pitch (paper 1 static, paper 2 dynamic with him leading) is designed specifically to give his dynamicizing instinct somewhere to go that doesn't reshape paper 1\.  
  
## **What's deferred to the paper proper**  
  
* The 108-item hierarchical measurement version. PoC uses the simpler 9-construct case.    
* The exploratory Jaccard search (combinatorial assignment search). PoC does confirmatory only.    
* Application to real personality data. PoC stays in simulation.    
* The R package as a polished artifact. PoC produces working code, not a documented release.    
* Comparison against Bayesian sparse factor models or Boolean matrix factorization. EFA is the one comparison we run; the others go in the paper's full Monte Carlo.  
  
Holding to this scope is itself a discipline check — every "but we should also..." that surfaces during PoC work goes on a list for the paper, not into the PoC.  
  
## **Tooling**  
  
R, in a project repo with an analyses/ directory and a results/ directory. Standard packages (lavaan, psych, MASS for multivariate normal generation, ggplot2 for diagnostic plots). RMarkdown notebooks for each analysis step, so the work is reproducible and the eventual paper has draft figures already in hand.  
  
I write the code, you run it, we iterate on results in conversation. Where I'm uncertain about an implementation choice, I flag it explicitly rather than committing silently.  
  
---  
  
## **Sequenced analyses**  
  
Each step has a defined output and a decision point. If a step fails, we stop and reassess before continuing.  
  
### **Step 1: Derive the Jaccard prediction formally**  
  
Output: a written derivation, in markdown with LaTeX math, of the predicted correlation between two indicators $X$ and $Y$ loading on subsets $S\_X$ and $S\_Y$ of the latent primaries, under three baseline assumptions: equal loadings $\\lambda$ across all indicator-primary pairs, unit-variance independent primaries, and uncorrelated residuals.  
  
Expected result: $\\text{cor}(X, Y) \= \\lambda^2 |S\_X \\cap S\_Y| / \\sqrt{(\\lambda^2 |S\_X| \+ \\sigma\_X^2)(\\lambda^2 |S\_Y| \+ \\sigma\_Y^2)}$, which under standardization simplifies to a function of $|S\_X \\cap S\_Y|$, $|S\_X|$, $|S\_Y|$.  
  
**Decision point:** Does the formula come out as expected? If yes, proceed. If the derivation produces something more complicated than the clean Jaccard form, we need to decide whether the more complex prediction is still a sharp diagnostic or whether the project's central claim needs softening.  
  
### **Step 2: Build the data generator and verify the prediction**  
  
Output: an R function `generate_abhop_data(n, lambda, residual_var)` that produces a $n \\times 9$ data matrix from the true generating model. Specifically: 4 latent primaries (independent standard normal), 9 indicators corresponding to the 4 ring-adjacent pairs, 4 triples, and 1 quadruple of the Primate Venn (excluding the 4 singles, which the framework holds aren't directly measurable).  
  
Verification: compute the empirical correlation matrix from a large sample ($n \= 50000$) and compare entry-by-entry to the Step 1 prediction. Plot predicted vs observed as a scatter — should fall on a straight line through the origin.  
  
**Decision point:** Does the empirical correlation matrix match the prediction at large $N$? If yes, the data generator is correct and the formula is right. If not, either the generator has a bug or the formula has an error — diagnose before continuing.  
  
### **Step 3: Demonstrate EFA failure**  
  
Output: results from running EFA on simulated data at $N \\in {200, 500, 1000, 2000}$, each replicated 100 times. Extract 4 factors with varimax rotation. Report the loading matrix and the proportion of replications in which the factors are interpretable as the four latent primaries.  
  
Operational definition of "interpretable as primaries": for each replication, compute the best alignment between estimated factors and true primaries (via Procrustes rotation), then check whether each estimated factor has its highest loadings on indicators that include the corresponding true primary. Score the proportion of replications where this holds for all 4 factors simultaneously.  
  
Expected result: low success rate at all sample sizes. EFA finds factors that are blends of the true primaries, weighted by which Venn regions are most heavily represented in the indicator set.  
  
**Decision point:** Does EFA fail as predicted? If yes, we have the negative result the paper needs. If EFA partially recovers the structure, the methods contribution is weakened — we'd need to characterize the partial recovery and rethink whether the paper's central claim ("standard methods can't find this") holds.  
  
### **Step 4: Implement and test the confirmatory Jaccard test**  
  
Output: an R function `jaccard_test(cor_matrix, assignment, n_obs)` that returns a fit statistic and p-value for the hypothesis that the observed correlation matrix is generated by the specified Jaccard-structured assignment.  
  
Implementation approach: compute the predicted correlation matrix from the assignment, compute the residual matrix (observed minus predicted), summarize the residuals into a single fit statistic (probably mean squared residual or $\\chi^2$-style statistic with sample size weighting), generate the null distribution by permuting the assignment of indicators to subsets and recomputing the fit statistic for each permutation.  
  
Tests:  
  
* Run on simulated data from the true model. Should detect Jaccard structure with high power at $N \= 500$.    
* Run on simulated data from a non-Jaccard alternative (e.g., simple-structure 4-factor model with the 9 indicators randomly assigned to factors). Should reject Jaccard structure with high power at $N \= 500$.    
* Run with the wrong assignment (true Jaccard structure exists but the test is given an incorrect mapping of indicators to subsets). Should reject the wrong assignment.  
  
**Decision point:** Does the test discriminate true from non-Jaccard data? Does it discriminate the correct from incorrect assignments? If yes, the diagnostic works as designed. If not, the test statistic or null distribution needs rethinking.  
  
### **Step 5: Characterize the robustness envelope**  
  
Output: a small grid of simulations varying:  
  
* Loading inequality: replace constant $\\lambda$ with $\\lambda\_{ij} \\sim \\text{Uniform}(\\lambda \- \\delta, \\lambda \+ \\delta)$ for $\\delta \\in {0, 0.05, 0.1, 0.2}$    
* Residual correlation: replace independent residuals with method-factor structure (single method factor with loadings of varying magnitude)    
* Sample size: $N \\in {200, 500, 1000}$  
  
Report the test's true-positive rate (detection power on true Jaccard data) and false-positive rate (rejection of correct assignment when only deviations are present, not non-Jaccard alternatives) across this grid.  
  
Expected result: the test tolerates moderate loading inequality and moderate method-factor structure, breaks at large deviations. We learn where the boundary is.  
  
**Decision point:** Is the robustness envelope wide enough to apply to realistic personality data? If yes, the PoC is done — we have everything Butner needs to see. If the envelope is narrow, we need to reformulate the test (probably with explicit modeling of method factors and free loadings) before pitching.  
  
---  
  
## **What we tell Butner when this is done**  
  
A short pitch document — two pages — with:  
  
* The framework's combinatorial Venn architecture, summarized    
* The recoverability problem (why standard methods don't work)    
* The Jaccard diagnostic and its derivation    
* The PoC results: EFA fails, confirmatory test works, robustness envelope is \[whatever we found\]    
* The proposed paper structure and what's left to do (full Monte Carlo, exploratory search, package development, real-data application)    
* The two-paper sequencing (static recoverability paper first, dynamic configurational-evolution paper second, with him leading the second)  
  
The pitch document and the working notebooks together. He gets to see code that runs, results that hold up, and a scoped invitation rather than a vague proposal.  
  
---  
  
## **Risks and what they would mean**  
  
**Risk 1: The Jaccard formula doesn't simplify cleanly.** If Step 1's derivation produces a formula that depends on multiple loading-magnitude parameters in a non-cancellable way, the diagnostic isn't as sharp as advertised. The paper still works methodologically — the recoverability problem remains real — but the headline "geometric correlation prediction" framing weakens. We'd reframe around hierarchical CFA fit comparison rather than the standalone diagnostic.  
  
**Risk 2: EFA partially recovers the structure.** If certain Venn configurations produce loading patterns that EFA can decompose into something close to the true primaries, the methods paper's central claim ("standard methods can't find this") gets fuzzy. We'd need to characterize when EFA succeeds versus fails and reframe the paper as "here's the boundary of EFA recoverability for combinatorial loading models" — still publishable, less interesting.  
  
**Risk 3: The confirmatory test has insufficient power at realistic N.** If we need $N \> 5000$ to discriminate Jaccard from competitors reliably, the test isn't useful for personality data, which typically tops out around $N \= 1000-3000$ in single-sample studies. We'd need to incorporate auxiliary information — facet-level structure, theoretical priors on subsets — to get power up at smaller N.  
  
**Risk 4: The robustness envelope is too narrow.** If even mild loading inequality or modest method-factor structure breaks the test, real personality data will defeat it. This is the most likely failure mode and the one we should plan to address head-on. Probably means the paper needs to formalize the test as a hierarchical CFA fit comparison rather than as a residual-based diagnostic on the raw correlation matrix.  
  
In all four cases, we learn the failure cheaply, before recruiting Butner, and we can decide whether to reformulate or to drop the project. That's the entire point of doing PoC first.  
