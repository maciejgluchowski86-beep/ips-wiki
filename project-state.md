# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure changes.

## Current structure

The wiki is article-first. Source pages live under `docs/`, and each entry is a separate Markdown page under `docs/entries/`. TeX math is rendered by the MkDocs site through MathJax. Internal links are ordinary Markdown links between pages.

The build target is the `Build wiki site` GitHub Actions workflow. It builds the MkDocs site from `docs/` and deploys through GitHub Pages when Pages is enabled for the repository.

## Current entries

1. `docs/entries/spin-system.md`: baseline definition and conventions for spin systems.
2. `docs/entries/ergodicity.md`: convergence-to-equilibrium convention for ergodicity.

## Current conventions

- Every entry begins with a purpose paragraph.
- Every entry records mathematical status.
- Definitions and conventions are separated from claims.
- Project-specific claims are marked as such.
- Cross-links use Markdown page links, not PDF section references.
- Shared notation and durable style choices live in `docs/meta/`.

## Next likely additions

- Interacting particle system.
- Invariant measure.
- Feller property.
- Positive rates.
- Positive Rates Conjecture.
- Coupling.
- Attractiveness.
