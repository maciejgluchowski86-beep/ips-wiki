# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure changes.

## Current structure

The wiki is LaTeX-first. Source entries live in `wiki-src/entries/`, shared macros and style decisions live in `wiki-meta/`, and `wiki-src/wiki-book.tex` compiles the entries into a single readable PDF.

The first build target is the `Build wiki PDF` GitHub Actions workflow. It compiles `wiki-src/wiki-book.tex` and uploads `wiki-pdf/ips-wiki.pdf` as an artifact.

## Current entries

1. `wiki-src/entries/spin-system.tex`: baseline definition and conventions for spin systems.
2. `wiki-src/entries/ergodicity.tex`: convergence-to-equilibrium convention for ergodicity.

## Current conventions

- Every entry begins with a purpose paragraph.
- Every entry records mathematical status.
- Definitions and conventions are separated from claims.
- Project-specific claims are marked as such.
- Shared macros live in `wiki-meta/preamble.tex`.
- Durable style choices live in `wiki-meta/style-decisions.md`.

## Next likely additions

- Interacting particle system.
- Invariant measure.
- Feller property.
- Positive rates.
- Positive Rates Conjecture.
- Coupling.
- Attractiveness.
