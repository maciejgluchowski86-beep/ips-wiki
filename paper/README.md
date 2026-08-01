# Paper source

This directory contains the canonical paper manuscript. The repository-level
`main.tex` is the Overleaf main file and loads `paper/main.tex`. The
repository-level `ejpecp.cls` is the EJP/ECP class used by the manuscript.

The paper is organized around three principal results. After the introduction
and setup, Theorems A--C state, respectively, the patch representation; the
coefficient criterion, patch threshold formula, and centered-moment
comparisons; and the common invariant-limit theorem. Their proofs follow in
that order. The model examples and discussion come after the proof of the
convergence theorem, followed by three appendices.

Shared packages, theorem environments, and notation are in
`paper/preamble.tex`; references are in `paper/references.bib`.

From the repository root, compile locally with:

```bash
latexmk -pdf main.tex
```

## Language conventions

- Use standard IPS and KCSM terminology, and prefer the wording of the
  author's earlier papers when several terms are available.
- A spin system already has two states and single-site flips; do not call it a
  binary spin system.
- Refer to realizations or trajectories of the graphical or dual process. Use
  remaining Poisson marks or omitted marks, rather than introducing new terms
  for unrevealed randomness.
- Use `facilitating` and `calm` for interpretation in the abstract,
  introduction, and conceptual discussion. `Facilitating` is standard KCSM
  terminology; `calm` is descriptive rather than a literature term or a new
  technical notion. In the formal setup and calculations, use the convention
  that the facilitating state is `0` and the calm state is `1`.
- Use established model-specific terms (infected/healthy, vacant/occupied,
  particle/empty site) in the examples. Do not derive new formal terminology
  from the word `calm`.
- Reserve new terms for objects defined in the paper, such as patches and the
  successful-interaction skeleton. Avoid unnecessary adjectives and adverbs.
- State model-specific mechanisms as such; do not attribute them to all
  non-attractive spin systems.
