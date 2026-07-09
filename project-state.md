# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure changes.

## Current structure

The wiki is article-first and public-facing. Source pages live under `docs/`, and each entry is a separate Markdown page under `docs/entries/`. TeX math is rendered by the MkDocs site through MathJax. Internal links are ordinary Markdown links between pages.

The build target is the `Build wiki site` GitHub Actions workflow. It builds the MkDocs site from `docs/` and deploys through GitHub Pages after every push to `main`.

## Current core entries

1. `docs/entries/lattice-and-graph.md`: lattice notation \(\Lambda\), neighbourhoods \(N(i)\), enlarged neighbourhoods \(N_*(i)\), and graph descriptions.
2. `docs/entries/local-functions.md`: finite-dependence observables and their role in generators.
3. `docs/entries/monomials.md`: monomials \(\chi_A\) and algebraic identities.
4. `docs/entries/interacting-particle-system.md`: general product-space Markov process on \(\mathcal S^\Lambda\) with local updates.
5. `docs/entries/spin-system.md`: two-state single-site flip system, generator, and semigroup/kernel notation.
6. `docs/entries/oriented-spin-system.md`: spin systems on directed acyclic lattices.
7. `docs/entries/ergodicity.md`: IPS-specific distinction between unique invariant measure, ergodicity, and uniform exponential ergodicity.

## Current KCSM entries

1. `docs/entries/bernoulli-refresh-operator.md`: Bernoulli product measure and one-site refresh operator.
2. `docs/entries/update-family.md`: update rules and induced constraints.
3. `docs/entries/kinetically-constrained-spin-model.md`: general KCSM generator.
4. `docs/entries/legal-update.md`: legal clock rings and legal paths.
5. `docs/entries/fa-1f-model.md`: FA-1f on an arbitrary lattice.
6. `docs/entries/east-model.md`: East model on an oriented lattice.
7. `docs/entries/kcsm-relaxation-and-mixing.md`: relaxation time, mixing time, and precutoff terminology.
8. `docs/entries/kcsm-out-of-equilibrium.md`: general out-of-equilibrium setup.
9. `docs/entries/fa-1f-out-of-equilibrium.md`: known FA-1f out-of-equilibrium results.
10. `docs/entries/east-out-of-equilibrium.md`: known East out-of-equilibrium results.

## Current conventions

- Public pages should not contain private strategy, raw scratch work, personal information, credentials, copyrighted source text, or unpublished claims without proof status.
- Entries should be mathematical articles, not commentary about the wiki.
- Cross-links should usually be Wikipedia-style inline links through relevant words or phrases.
- Do not use top-level "Related pages" lists on ordinary entries.
- Use `\(...\)` for inline math and `$$...$$` for display math.
- Use unambiguous subset notation: non-strict, strict, and finite-subset commands are distinct; the bare ambiguous subset command is forbidden by CI.
- Use \(\Lambda\) for the lattice and \(\mathcal S\) for the single-site state space.
- A graph is an alternative description of neighbourhoods on \(\Lambda\).
- \(N(i)\) does not contain \(i\), while \(N_*(i)=N(i)\cup\{i\}\) does.
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
