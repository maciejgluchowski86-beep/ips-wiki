# Literature note

## Target

One-dimensional biased annihilating branching process (BABP), finite nonempty initial particle set, convergence to Bernoulli equilibrium for every branching parameter `lambda>0`.

Use

$$
q=\frac{\lambda}{1+\lambda},
\qquad
p=\frac1{1+\lambda}
$$

for particle/vacancy density versus the canonical patch-paper convention.

## Current state of the art

### Neuhauser--Sudbury (1993)

Claudia Neuhauser and Aidan Sudbury, *The biased annihilating branching process*, Advances in Applied Probability 25 (1993), 24--38.

The paper establishes the basic stationary-law structure and formulates the spreading picture for BABP. It is foundational background for the finite-seed problem.

### Mountford (1993) and Sudbury (1999)

The finite-seed convergence theorem was known for `lambda>1/3`; Sudbury's 1999 paper

Aidan Sudbury, *Hunting submartingales in the jumping voter model and the biased annihilating branching process*, Advances in Applied Probability 31 (1999), 839--854,

improves the range to

$$
\lambda>0.0347.
$$

The exact origin of this numerical threshold is the first research bottleneck and must be reconstructed rather than treated as a black box.

### Martinelli--Shapira--Toninelli (2025)

Fabio Martinelli, Assaf Shapira, Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461 (2025), Section 5.

Relevant items:

- Theorem 5.2: exponential ergodicity of the double-flipping process (DFP) for every `lambda>0`, uniformly over initial configurations for local observables.
- Equation (5.2): BABP self-duality.
- Equation (5.3): BABP--DFP quasi-duality.
- Remark 5.3: decay of the finite-test self-duality observable implies BABP convergence to equilibrium.
- Application 1: BABP from any finite nonempty initial set has linear particle-number growth for every `lambda>0`.
- Remark 5.4: finite-seed convergence is recorded as known only for `lambda>0.0347`.
- Application 2 / Remark 5.5: exponential convergence from Bernoulli and certain inhomogeneous product initial laws for every `lambda>0`.

The fact that the authors prove Theorem 5.2 yet still record the finite-seed gap is important negative evidence: quasi-duality does not trivially close the problem.

### Lloyd--Sudbury and Sudbury (1997)

The quasi-duality/thinning algebra and qualitative convergence results for translation-invariant initial laws are relevant background. Student B should trace the exact interface rather than assume the 2025 presentation is the only usable formulation.

## Canonical project source

The principal's canonical paper `paper/`, *Patch representations and convergence for facilitated spin systems*.

Relevant locations:

- `paper/sections/applications.tex`, BABP subsection: patch positivity, patch threshold `p`, existing convergence results, and explicit statement that finite-seed convergence remains open in part of the parameter range.
- `paper/sections/discussion.tex`: finite nonempty BABP seeds are listed among the hard-model convergence problems not covered by the uniform-pure-death theorem.

The patch paper is authoritative for project-specific patch statements. It is not evidence that a patch-only proof of the finite-seed theorem exists.

## Successor check

At programme initialization on 2026-08-15, a targeted web search found no later theorem removing the `0.0347` finite-seed threshold. Before any novelty claim, Student B should search later citations, alternate terminology, and related branching/coalescing systems more systematically.
