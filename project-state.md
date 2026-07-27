# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure changes.

## Current structure

The wiki is article-first and public-facing. Source pages live under `docs/`, and each entry is a separate Markdown page under `docs/entries/`. TeX math is rendered by the MkDocs site through MathJax. Internal links are ordinary Markdown links between pages.

The build target is the `Build wiki site` GitHub Actions workflow. It builds the MkDocs site from `docs/` and deploys through GitHub Pages after every push to `main`.

The paper template lives under `paper/`. The repository-level
`main.tex` is the Overleaf main file and loads `paper/main.tex`. The
paper body contains the agreed section and subsection order.
Introduction Sections 1.1--1.3 are now a prose draft. They present the
calm--facilitating tendency and noisy loss-of-memory problem, distinguish
interaction strength from persistence, and introduce patches as the mechanism
which recovers a centered-moment order from the signed dual. The introduction
does not use the KCSM \(0\)--\(1\) convention; that notation is postponed to
the setup. The abstract, Section 1.4 onward, and the appendices remain short
drafting notes with links to source wiki entries. No title, formal statement,
or proof has yet been fixed. Shared macros and theorem environments live in
`paper/preamble.tex`.

## Current core entries

1. `docs/entries/lattice-and-graph.md`: lattice notation \(\Lambda\), neighbourhoods \(N(i)\), enlarged neighbourhoods \(N_*(i)\), reachability, orientation, and graph descriptions.
2. `docs/entries/polynomial-growth-lattice.md`: graph distance, balls, and \((k,D)\)-polynomial growth.
3. `docs/entries/local-functions.md`: finite-dependence observables and their role in generators.
4. `docs/entries/monomials.md`: monomials \(\chi_A\) and algebraic identities.
5. `docs/entries/bernoulli-product-measure.md`: homogeneous and inhomogeneous Bernoulli product measures, monomial moments, and coordinatewise stochastic order.
6. `docs/entries/interacting-particle-system.md`: general product-space Markov process on \(\mathcal S^\Lambda\) with local updates.
7. `docs/entries/spin-system.md`: two-state single-site flip system, generator, and semigroup/kernel notation.
8. `docs/entries/pure-noise-spin-system.md`: independent Bernoulli refresh spin system and pure-noise perturbations.
9. `docs/entries/oriented-spin-system.md`: spin systems on oriented lattices, with orientation defined by reachability through \(N(i)\).
10. `docs/entries/invariant-measure.md`: invariant measures and the Krylov--Bogoliubov existence theorem inside a preserved weakly closed convex class.
11. `docs/entries/ergodicity.md`: IPS-specific distinction between unique invariant measure, ergodicity, and uniform exponential ergodicity.

## Current duality entries

1. `docs/entries/duality.md`: concise operator and Feynman--Kac duality definition.
2. `docs/entries/monomial-duality-for-spin-systems.md`: monomial duality for spin systems via a signed additive set process and Feynman--Kac potential.
3. `docs/entries/duality-noise-lemma.md`: perturbation lemma for Markov noise acting diagonally with non-positive eigenvalue on the duality function.

## Current signed additive set process entries

1. `docs/entries/signed-additive-set-process.md`: finite-subset process with sign coordinate, deaths, splits, and births.
2. `docs/entries/graphical-construction-of-signed-additive-set-process.md`: Poisson interaction construction of the signed additive set process.
3. `docs/entries/successful-interaction.md`: finite-horizon and full nonempty-target successful-interaction skeletons.

## Current patch entries

1. `docs/entries/patch.md`: full one-site spacetime intervals cut by successful touches and their finite-horizon truncations.
2. `docs/entries/interaction-cone.md`: sites reached from the initial dual set by successful interactions.
3. `docs/entries/patch-consistency-event.md`: local patch measure, consistency event, and conditioned patch measure.
4. `docs/entries/patch-factorization.md`: finite-horizon product decomposition of patch laws conditional on \(\cG_T\), proved by Poisson disintegration and chronological reconstruction of the successful skeleton.
5. `docs/entries/patch-contribution.md`: one full-patch contribution definition covering finite and infinite lifetimes, together with explicit cut and end formulas in dual-rate form and spin-rate form.
6. `docs/entries/patch-positivity-property.md`: coefficient criterion guaranteeing nonnegative bulk patch contributions.
7. `docs/entries/patch-critical-density.md`: minimal one-density profile making every affine end-patch contribution nonnegative.
8. `docs/entries/high-density-measure.md`: centered-moment definitions of the high-density class \(\mathcal M_\star\) and lower convergence class \(\mathcal M_-\), with product-profile characterizations.
9. `docs/entries/patch-representation-of-spin-systems.md`: finite-horizon bulk-and-end representation of \(P_t\chi_A\), including the centered end-factor expansion for general initial laws.
10. `docs/entries/undoing-duality-under-confined-interactions.md`: successful interactions confined on an arbitrary dual interval represented by a modified spin-system semigroup, with initial-interval and late-interval specializations.
11. `docs/entries/finite-propagation-for-zero-boundary-restrictions.md`: exponentially accurate approximation of local observables by zero-boundary restrictions on linearly growing balls.
12. `docs/entries/exponential-relaxation-under-confined-late-interactions.md`: exponential convergence of a late-confined term under uniform zero-boundary mixing.
13. `docs/entries/monomial-monotonicity-for-high-density-measures.md`: centered-moment semigroup order, preservation of \(\mathcal M_\star\), and product-profile corollaries.
14. `docs/entries/pure-death-comparison-under-patch-positivity.md`: monomial comparison on all of \(\mathcal M_\star\) after removing an environment-independent pure-death component, with a corollary for unique invariant measures.
15. `docs/entries/common-invariant-limit-under-uniform-pure-deaths.md`: common invariant limit, uniformly over \(\mathcal M_-\), proved by initial-cone confinement, ordinary zero-boundary finite propagation, and patch relaxation under a uniform pure-death component.

## Current KCSM entries

1. `docs/entries/bernoulli-refresh-operator.md`: Bernoulli product measure and one-site refresh operator.
2. `docs/entries/update-family.md`: update rules and induced constraints.
3. `docs/entries/kinetically-constrained-spin-model.md`: general KCSM generator.
4. `docs/entries/soft-kcsm.md`: KCSM with hard constraints softened by unconstrained updates.
5. `docs/entries/legal-update.md`: legal clock rings and legal paths.
6. `docs/entries/fa-1f-model.md`: FA-1f on an arbitrary lattice.
7. `docs/entries/east-model.md`: East model as FA-1f on an oriented lattice using \(N(i)\).
8. `docs/entries/babp-model.md`: BABP as the additive-rate analogue of FA-1f, including the classical particle convention.
9. `docs/entries/monomial-duality-for-fa-1f.md`: systematic dual rates, signs, and Feynman--Kac weights for hard/soft FA-1f with optional pure-death perturbation.
10. `docs/entries/patch-contributions-for-fa-1f.md`: hard FA-1f patch contributions with unified full-patch, cut, and end formulas.
11. `docs/entries/patch-positivity-for-fa-1f.md`: verification that FA-1f has patch positivity and characterization of pure-noise perturbations preserving it.
12. `docs/entries/patch-critical-density-for-fa-1f.md`: identification of the FA-1f patch critical density with its equilibrium one-density.
13. `docs/entries/monomial-duality-for-babp.md`: singleton-target dual rates, signs, and Feynman--Kac weights for BABP.
14. `docs/entries/patch-contributions-for-babp.md`: BABP full-patch, cut, and end contribution formulas.
15. `docs/entries/patch-positivity-for-babp.md`: verification of BABP patch positivity and characterization of pure-noise perturbations preserving it.
16. `docs/entries/patch-critical-density-for-babp.md`: identification of the BABP patch critical density with its equilibrium one-density.
17. `docs/entries/kcsm-relaxation-and-mixing.md`: relaxation time, mixing time, and precutoff terminology.
18. `docs/entries/kcsm-out-of-equilibrium.md`: general out-of-equilibrium setup.
19. `docs/entries/fa-1f-out-of-equilibrium.md`: theorem records for known FA-1f out-of-equilibrium convergence results.
20. `docs/entries/east-out-of-equilibrium.md`: theorem records for known East out-of-equilibrium convergence results.
21. `docs/entries/babp-out-of-equilibrium.md`: known BABP long-time results and the high-density centered-moment comparison.

## Current conventions

- Public pages should not contain private strategy, raw scratch work, personal information, credentials, copyrighted source text, or unpublished claims without proof status.
- Entries should be mathematical articles, not commentary about the wiki.
- Cross-links should usually be Wikipedia-style inline links through relevant words and phrases.
- Do not use top-level "Related pages" lists on ordinary entries.
- Use \(...\) for inline math and $$...$$ for display math.
- Subset notation is a style convention, not a build constraint: prefer distinct notation for non-strict, strict, and finite subsets in polished entries.
- Use \(\Lambda\) for the lattice and \(\mathcal S\) for the single-site state space.
- A graph is an alternative description of neighbourhoods on \(\Lambda\).
- \(N(i)\) does not contain \(i\), while \(N_*(i)=N(i)\cup\{i\}\) does.
- Orientation uses only \(N(i)\): \(i\to j\) means there is a chain from \(i\) to \(j\) following neighbour sets; oriented means reachability is antisymmetric.
- Do not introduce predecessor/successor notation for orientation unless a later page genuinely needs it.
- For KCSM, \(0\) is the facilitating state, \(q\) is the density of zeros, and \(p=1-q\).
- Spin system means two-state single-site flip system.
- IPS is the broader class allowing larger single-site spaces and more general local update maps.
- Shared notation and durable style choices live in `docs/meta/`.

## Next likely additions

- Feller property.
- Positive rates.
- Positive Rates Conjecture.
- Coupling.
- Attractiveness.
- Bootstrap percolation.
- Blocked configuration.
