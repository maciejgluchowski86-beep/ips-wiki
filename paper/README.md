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
- In the generic theory, refer to the spin values simply as states `0` and `1`.
  Do not assign universal physical names to the two states, and do not use
  `calm` anywhere in the manuscript.
- Use `facilitating` only when it is standard and model-specific. In the KCSM
  examples, state `0` is vacant and facilitating and state `1` is occupied.
  Outside such examples, use `0` and `1` unless the model has established
  terminology.
- For Bernoulli product laws, a parameter `p` or profile `p_i` denotes the
  probability of state `1`, unless a model-specific convention is stated
  explicitly.
- The functions `c_i^0` and `c_i^1` are the restrictions of the single flip-rate
  function `c_i` according to whether the current spin is `0` or `1`. They may
  equivalently be described as the `0 -> 1` and `1 -> 0` transition rates. Do
  not call them two separate flip rates.
- `Pure deaths` are environment-independent `1 -> 0` transitions; the name
  refers to the signed dual. In generic statements, use this formulation
  rather than saying that they create a named spin state.
- In conceptual exposition, use `monotone`, `configuration monotonicity`, and
  `monotone coupling`. Use the traditional term `attractive` only in historical
  or literature discussion where that terminology itself matters.
- Use established model-specific terms when they exist: infected/healthy for
  the contact process, vacant/occupied for KCSMs, and particle/empty site for
  particle systems.
- Refer to realizations or trajectories of the graphical or dual process. Use
  remaining Poisson marks or omitted marks, rather than introducing new terms
  for unrevealed randomness.
- Reserve new terms for objects defined in the paper, such as patches and the
  successful-interaction skeleton. Use `patch-positive` as the adjective and
  `patch positivity` for the property.
- State model-specific mechanisms as such; do not attribute them to all
  non-monotone spin systems.
