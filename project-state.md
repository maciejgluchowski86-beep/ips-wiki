# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure changes.

## Current structure

The wiki is article-first and public-facing. Source pages live under `docs/`, and each entry is a separate Markdown page under `docs/entries/`. TeX math is rendered by the MkDocs site through MathJax. Internal links are ordinary Markdown links between pages.

The build target is the `Build wiki site` GitHub Actions workflow. It builds the MkDocs site from `docs/` and deploys through GitHub Pages after every push to `main`.

## Current core entries

1. `docs/entries/lattice-and-graph.md`: lattice notation \(\Lambda\), neighbourhoods \(N(i)\), enlarged neighbourhoods \(N_*(i)\), reachability, orientation, and graph descriptions.
2. `docs/entries/polynomial-growth-lattice.md`: graph distance, balls, and \((k,D)\)-polynomial growth.
3. `docs/entries/local-functions.md`: finite-dependence observables and their role in generators.
4. `docs/entries/monomials.md`: monomials \(\chi_A\) and algebraic identities.
5. `docs/entries/interacting-particle-system.md`: general product-space Markov process on \(\mathcal S^\Lambda\) with local updates.
6. `docs/entries/spin-system.md`: two-state single-site flip system, generator, and semigroup/kernel notation.
7. `docs/entries/pure-noise-spin-system.md`: independent Bernoulli refresh spin system and pure-noise perturbations.
8. `docs/entries/oriented-spin-system.md`: spin systems on oriented lattices, with orientation defined by reachability through \(N(i)\).
9. `docs/entries/ergodicity.md`: IPS-specific distinction between unique invariant measure, ergodicity, and uniform exponential ergodicity.

## Current duality entries

1. `docs/entries/duality.md`: concise operator and Feynman--Kac duality definition.
2. `docs/entries/theta-monomials.md`: \(\chi_A^\theta\), barred theta monomials, basis property, and algebraic identities.
3. `docs/entries/monomial-duality-for-spin-systems.md`: monomial duality for spin systems via a signed additive set process and Feynman--Kac potential.
4. `docs/entries/patch-factorization.md`: product decomposition of patch laws conditional on successful interactions.
5. `docs/entries/patch-contribution.md`: explicit bulk and end patch contribution formulas in dual-rate form and spin-rate form.
6. `docs/entries/patch-positivity-property.md`: coefficient criterion guaranteeing nonnegative bulk patch contributions.
7. `docs/entries/patch-representation-of-spin-systems.md`: representation theorem expressing \(P_t\chi_A\) as an expectation over products of patch contributions.
8. `docs/entries/duality-noise-lemma.md`: perturbation lemma for Markov noise acting diagonally with non-positive eigenvalue on the duality function.

## Current signed additive set process entries

1. `docs/entries/signed-additive-set-process.md`: finite-subset process with sign coordinate, deaths, splits, and births.
2. `docs/entries/graphical-construction-of-signed-additive-set-process.md`: Poisson interaction construction of the signed additive set process.
3. `docs/entries/successful-interaction.md`: nonempty-target successful-interaction skeletons and the sigma algebra revealing them.
4. `docs/entries/patch.md`: one-site spacetime intervals cut by successful touches, classified by boundary type, with bulk patches \(\mathcal B_T\) and end patches \(\mathcal E_T\).
5. `docs/entries/patch-consistency-event.md`: local patch measure, consistency event, and conditioned patch measure.

## Current KCSM entries

1. `docs/entries/bernoulli-refresh-operator.md`: Bernoulli product measure and one-site refresh operator.
2. `docs/entries/update-family.md`: update rules and induced constraints.
3. `docs/entries/kinetically-constrained-spin-model.md`: general KCSM generator.
4. `docs/entries/soft-kcsm.md`: KCSM with hard constraints softened by unconstrained updates.
5. `docs/entries/legal-update.md`: legal clock rings and legal paths.
6. `docs/entries/fa-1f-model.md`: FA-1f on an arbitrary lattice.
7. `docs/entries/east-model.md`: East model as FA-1f on an oriented lattice using \(N(i)\).
8. `docs/entries/monomial-duality-for-fa-1f.md`: systematic dual rates, signs, and Feynman--Kac weights for hard/soft FA-1f with optional pure-death perturbation.
9. `docs/entries/patch-contributions-for-fa-1f.md`: hard FA-1f patch contributions with explicit bulk and end formulas.
10. `docs/entries/patch-positivity-for-fa-1f.md`: verification that FA-1f has patch positivity and characterization of pure-noise perturbations preserving it.
11. `docs/entries/kcsm-relaxation-and-mixing.md`: relaxation time, mixing time, and precutoff terminology.
12. `docs/entries/kcsm-out-of-equilibrium.md`: general out-of-equilibrium setup.
13. `docs/entries/fa-1f-out-of-equilibrium.md`: theorem records for known FA-1f out-of-equilibrium convergence results.
14. `docs/entries/east-out-of-equilibrium.md`: theorem records for known East out-of-equilibrium convergence results.

## Current conventions

- Public pages should not contain private strategy, raw scratch work, personal information, credentials, copyrighted source text, or unpublished claims without proof status.
- Entries should be mathematical articles, not commentary about the wiki.
- Cross-links should usually be Wikipedia-style inline links through relevant words or phrases.
- Do not use top-level "Related pages" lists on ordinary entries.
- Use `\(...\)` for inline math and `$$...$$` for display math.
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

- Invariant measure.
- Feller property.
- Positive rates.
- Positive Rates Conjecture.
- Coupling.
- Attractiveness.
- Bootstrap percolation.
- Blocked configuration.
