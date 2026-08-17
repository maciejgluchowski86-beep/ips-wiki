# Student G Assignment 005 handoff

## Status

Assignment 005 is complete. Five genuinely distinct coupling/graphical entries were staged under `research/active/ergodicity-methods-toolbox/entries/`, one substantive entry per commit. The sixth target, regeneration of an actual disagreement front between two coupled copies, did not survive a bounded primary-source search, and the fallback search did not produce a source-supported substitute satisfying the programme's concrete-interacting-process gate without duplicating an already-live interface. I therefore did **not** manufacture a sixth entry.

No file under `docs/` and no `mkdocs.yml` file was edited.

## Entries and commits

1. `coupling-independence-coarse-grained-comparison.md` — `dfd0aa0115f9b6ba6fb914f45c26c252ee4e4d9a`.
2. `sticky-coupling-mckean-vlasov.md` — `098e1453cf66099d1ef567fd79a88896fe8866db`.
3. `componentwise-reflection-uniform-mean-field.md` — `7203bff7d8c8471371708033545856552aa2af83`.
4. `survival-conditioned-renewal-multitype-contact.md` — `4fbcbe3a1d2a8668318d832eb65113d350850be6`.
5. `environment-seen-second-class-particle.md` — `8f76a8b24a105f2cbee1f2b46e82646edd2aace6`.

## Taxonomy decisions

### Coupling independence is not spectral independence or block/path coupling

Chen--Feng Definition 7 requires an **actual coupling of two pinned conditional Gibbs laws** whose expected weighted Hamming discrepancy is bounded by the weight of the changed pin. Their Theorem 9 uses that coupling object to compare the original high-degree Glauber chain with pinned lower-degree subproblems. The paper notes that coupling independence implies spectral independence, but the coarse-grained comparison theorem uses more than the spectral radius of an influence matrix. It is also distinct from ordinary path coupling, which contracts neighboring dynamic configurations, and from the live block-coupling page, which changes the update itself to a joint block resampling.

### Sticky coupling has a law-dependent sticky distance process

Durmus--Eberle--Guillin--Schuh reduce the McKean--Vlasov coupling to a one-dimensional nonlinear distance process whose diffusion coefficient vanishes at zero and whose drift contains the current noncoupling probability. Zero is therefore a **sticky state**, not merely the endpoint of a successful meeting. The resulting concave transportation cost yields exponential Wasserstein contraction and a uniform-in-time propagation-of-chaos estimate. This differs from the live synchronous weighted-`W_1` contraction, Hairer's absolutely-continuous binding construction, and reflection coupling with a nonsticky coupling time.

### Componentwise reflection is load-bearing because the estimate is uniform in particle number

Liu--Wu--Zhang reflect the noise for each coordinate pair separately and use a Poisson-designed one-particle cost. The mean-field factor `1/(N-1)` cancels the number of cross-interaction errors, producing an exponential transportation contraction with constants independent of `N`. This is not Wang's live infinite-dimensional reflection mechanism: Wang's difficulty is singular Hilbert-space reflection and its regularization, whereas here the reflection is finite-dimensional coordinate by coordinate and the hard point is closing the interacting `N`-particle estimate uniformly in `N`. It is also distinct from sticky coupling because there is no nonlinear sticky scalar comparison process.

### Survival-conditioned ancestor renewal is distinct from block restart plus dual intersection

Mountford--Barrios Pantoja--Valesin Proposition 4.4 constructs, conditional on survival, a random space-time point with a free selective infection path, an independent fresh graphical future of the survival-conditioned law, and exponential moments for its time and displacement. Section 5 builds these renewal-type times from the ancestor process. Repeated renewals plus steering estimates yield linear takeover of the weaker type and Theorem 1.2 complete convergence. This differs from the live Ruibo Ma two-level contact page, where restartable coarse blocks are combined with a separate backward flea dual and a forward/backward intersection argument.

### Moving with a second-class particle creates a stationary ergodic environment

Martin--Sly--Zhang start TASEP from one second-class particle in an otherwise Bernoulli-`rho` background and prove that the configuration viewed from the second-class particle converges to an explicit non-product stationary law. They then prove time ergodicity of the stationary moving-frame process. The marker is deliberately retained. This is not the live product-shock/random-walk page: there a specially chosen shock family is exactly closed under the coupled generator and the marker itself is an autonomous random walk; here convergence of the **surrounding moving-frame environment** is the theorem.

## Source qualifications

### Coupling independence

Primary checked source: Xiaoyu Chen and Weiming Feng, *Rapid Mixing via Coupling Independence for Spin Systems with Unbounded Degree*, APPROX/RANDOM 2025, LIPIcs 353, Article 68, DOI `10.4230/LIPIcs.APPROX/RANDOM.2025.68`. Checked pinpoints: Definition 7; Theorem 9 and Sections 2.1--2.2; Theorem 1 for list-colouring and Theorem 5 for hard core. The entry keeps the conclusion at finite-volume Glauber relaxation/mixing and does not infer infinite-volume uniqueness.

### Sticky coupling

Primary checked source: Alain Durmus, Andreas Eberle, Arnaud Guillin and Katharina Schuh, *Sticky nonlinear SDEs and convergence of McKean--Vlasov equations without confinement*, Stochastics and Partial Differential Equations: Analysis and Computations 12 (2024), 1855--1906, DOI `10.1007/s40072-023-00315-8`. Checked pinpoints: Theorems 1--2, Theorem 7, Theorem 8, and Section 5. The particle application is weak mean-field interaction; the theorem is not claimed in phase-coexistence regimes.

### Componentwise reflection

Primary checked source: Wei Liu, Liming Wu and Chaoen Zhang, *Long-time behaviors of mean-field interacting particle systems related to McKean-Vlasov equations*, Communications in Mathematical Physics 387 (2021), DOI `10.1007/s00220-021-04198-5`, inspected via arXiv `2007.09462`. Checked pinpoints: Theorem 2.5, Section 3.1 and equation (3.3), Theorem 2.9, and Examples 2.13--2.14. The conclusion is Wasserstein contraction and long-time propagation of chaos, not total-variation coalescence.

### Survival-conditioned contact renewal

Primary checked source: Thomas Mountford, Pedro Luis Barrios Pantoja and Daniel Valesin, *The asymmetric multitype contact process*, Stochastic Processes and their Applications 129 (2019), 2783--2820, DOI `10.1016/j.spa.2018.08.006`, arXiv `1803.01533`. Checked pinpoints: Theorems 1.1--1.2; Proposition 4.4; Section 5, *Ancestor process and renewal-type random times*; Proposition 3.2 for steering. The renewal lemma is one load-bearing part of the complete-convergence proof, not a standalone implication by itself.

### Environment viewed from a second-class particle

Primary checked source: James B. Martin, Allan Sly and Lingfu Zhang, *Convergence of the Environment Seen from Geodesics in Exponential Last-Passage Percolation*, Journal of the European Mathematical Society 27 (2025), 877--970, DOI `10.4171/jems/1594`, arXiv `2106.05242`. Checked pinpoints: Theorem 1.7, Section 2.3, Section 4, and Proposition 5.3. The entry concerns convergence and ergodicity of the **moving-frame** TASEP environment and does not claim laboratory-frame global mixing.

## Disagreement-front regeneration: bounded negative search

I did **not** find a clean primary theorem satisfying target 6: two coupled copies whose actual disagreement boundary has regeneration times and whose renewal structure proves agreement or an interface long-time theorem. The targeted search repeatedly returned one of three already-live or deliberately separate objects:

- a physical propagating reaction front;
- a competition interface between species/phases;
- a retained second-class discrepancy/shock marker without a regeneration sequence for the coupled-copy disagreement front.

This is a bounded negative literature result, not a claim that no such theorem exists. A future search should be reopened only with a concrete source lead or terminology that changes the search space.

## Rejected fallback candidates

Two fallback families were inspected and deliberately **not** turned into entries.

### Another finite-dual successful coupling

The symmetric inclusion process and later multilayer exclusion/inclusion work provide clean successful couplings of finite dual particle systems, but their load-bearing theorem is the same interface as the already-live `successful-coupling-finite-dual-particles.md`: duality turns invariant transforms into bounded harmonic functions and successful coupling makes those functions constant on fixed-particle-number sectors. A different model is not enough to justify a duplicate method page.

### Quasi-successful coupling of infinite particle systems

Blank--Pirogov, *On Quasi-successful Couplings of Markov Processes*, Problems of Information Transmission 43 (2007), 316--330, DOI `10.1134/S0032946007040059`, arXiv `math/0610118`, is mathematically distinct and was inspected in detail. Theorem 5.1 shows that vanishing density of discrepancies, possibly after a bounded spatial shift, gives uniqueness among translation-invariant invariant laws in a fixed invariant sector. Theorem 5.2 shows that local coupling in probability on every finite cylinder, again allowing a bounded shift, yields weak convergence within the translation-invariant class. Lemma 6.4 gives the same-density limit-point consequence for locally interacting particle systems.

However, the paper explicitly states that construction of couplings satisfying these hypotheses for **specific particle-system models** is deferred to separate work. Under the toolbox rule that generic coupling theory needs a concrete interacting-process application, this source does not by itself clear the entry gate. I therefore did not use it merely to fill the sixth slot. If a later primary source supplies a concrete model where the quasi-successful/local-after-shift coupling is actually verified and load-bearing, this would be a plausible distinct future page.

## Further uncovered graphical/coupling families

The wave leaves several potentially distinct interfaces for later source-led work:

- a genuine **disagreement-front regeneration** theorem for two coupled copies remains uncovered;
- **quasi-successful/local-after-shift coupling** becomes viable if a concrete IPS verification is located;
- environments seen from **multiple second-class particles or finite discrepancy clouds**, where the moving-frame invariant law is not reducible to the one-marker TASEP theorem;
- **essential hitting times with subadditive shape/large-deviation control** as a standalone contact-process method, separate from their use as one ingredient inside complete convergence;
- non-mean-field **sticky or hybrid reflection/synchronous couplings** for spatially interacting particle systems;
- coupling-independence analogues where the coarse comparison is used for an infinite-volume uniqueness or relaxation theorem rather than only finite-volume Glauber mixing.

The closed generic searches from earlier waves remain closed: generic boundary-uniform dynamic projective coupling and generic common/basic graphical coupling should not be repeated absent named new evidence.

## Mechanical validation

All five staged entries were written against the current `entry-template.md` and committed separately. `validate_entries.py` remains the principal/orchestrator's structural check and is not treated here as mathematical or source verification.
