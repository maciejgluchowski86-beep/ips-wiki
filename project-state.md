# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure changes.

## Current structure

The wiki is article-first and public-facing. Source pages live under `docs/`, and each entry is a separate Markdown page under `docs/entries/`. TeX math is rendered by the MkDocs site through MathJax. Internal links are ordinary Markdown links between pages.

The build target is the `Build wiki site` GitHub Actions workflow. It builds the MkDocs site from `docs/` and deploys through GitHub Pages after every push to `main`.

## Current core entries

1. `docs/entries/lattice-and-graph.md`: site spaces as graphs or lattice neighbourhood systems.
2. `docs/entries/local-functions.md`: finite-dependence observables and their role in generators.
3. `docs/entries/interacting-particle-system.md`: general product-space Markov process with local updates.
4. `docs/entries/spin-system.md`: two-state single-site flip system.
5. `docs/entries/ergodicity.md`: convergence-to-equilibrium notion and local-function formulation.

## Current conventions

- Public pages should not contain private strategy, raw scratch work, personal information, credentials, copyrighted source text, or unpublished claims without proof status.
- Entries should be mathematical articles, not commentary about the wiki.
- Cross-links should usually be Wikipedia-style inline links through relevant words or phrases.
- Do not use top-level "Related pages" lists on ordinary entries.
- Use `\(...\)` for inline math and `$$...$$` for display math.
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
