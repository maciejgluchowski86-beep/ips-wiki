---
method_id: dirichlet-form-canonical-path-comparison
title: Dirichlet-form and canonical-path comparison
category: functional-inequality
targets:
  - spectral-gap
  - mixing
model_scope: Finite reversible spin, particle, and Glauber-type chains that can be compared to a reference chain
source_status: primary-checked
primary_source: Persi Diaconis and Laurent Saloff-Coste, Comparison theorems for reversible Markov chains, Annals of Applied Probability 3(3) (1993), 696-730.
primary_pinpoint: Section 2B, Theorem 2.1, pp. 698-699; Section 2C, Theorem 2.3 for multicommodity flows
primary_url: https://doi.org/10.1214/AOAP/1177005359
application_source: Persi Diaconis and Laurent Saloff-Coste, Comparison theorems for reversible Markov chains, Annals of Applied Probability 3(3) (1993), 696-730.
application_pinpoint: Section 3, especially Theorem 3.1 and Theorem 3.2 on the exclusion process
application_url: https://doi.org/10.1214/AOAP/1177005359
wiki_candidate: yes
---

# Dirichlet-form and canonical-path comparison

## Criterion

Let \(P\) be a reversible chain of interest and \(\widetilde P\) a reversible reference chain on the same finite state space. For every reference transition \((x,y)\) with \(\widetilde P(x,y)>0\), choose a path \(\gamma_{xy}\) made of allowed \(P\)-edges. Diaconis--Saloff-Coste Theorem 2.1 bounds the reference Dirichlet form by
\[
\widetilde{\mathcal E}(f,f)\le A\,\mathcal E(f,f),
\]
where a canonical-path congestion constant is
\[
A=\max_{e=(z,w)}\frac{1}{\pi(z)P(z,w)}
\sum_{(x,y):e\in\gamma_{xy}}
|\gamma_{xy}|\,\widetilde\pi(x)\widetilde P(x,y).
\]
When the two chains have the same stationary law, the variational characterization immediately gives
\[
\operatorname{gap}(P)\ge A^{-1}\operatorname{gap}(\widetilde P).
\]
Their Theorem 2.3 replaces one chosen path by a multicommodity flow, allowing the comparison demand to be split among many paths and reducing congestion.

## Mechanism

Write each reference increment as a telescoping sum along its path,
\[
f(x)-f(y)=\sum_{e\in\gamma_{xy}}\nabla_e f.
\]
Cauchy--Schwarz bounds its square by the path length times the sum of squared edge gradients. Summing over reference transitions and reversing the order of summation produces the maximal load on any target edge, normalized by that edge's stationary conductance \(\pi(z)P(z,w)\). The comparison therefore converts a difficult global relaxation question into routing reference transitions through legal moves of the target dynamics.

This viewpoint is especially useful when the reference chain has a known gap but makes nonlocal moves, whereas the chain of interest has local or constrained moves. The same architecture can compare generators directly: if one proves \(\widetilde{\mathcal E}\le A\mathcal E\) by any argument, canonical paths are no longer needed explicitly.

## Representative IPS use

Diaconis--Saloff-Coste apply the method to finite symmetric exclusion. The target chain moves a particle only to a neighboring empty site of an underlying graph. The reference chain is the Bernoulli--Laplace diffusion, which can move a particle to an arbitrary empty site and has explicitly known eigenvalues. In Section 3 they route a Bernoulli--Laplace move along graph paths and use the comparison constant to control the exclusion spectrum. Theorem 3.1 gives eigenvalue bounds in terms of the underlying graph comparison geometry, and Theorem 3.2 gives a multicommodity-flow version for the second eigenvalue. This is a direct interacting-particle application of canonical-path Dirichlet comparison.

## Limitations

The basic theorem is finite-state and reversible. A poor path choice can create enormous congestion even when the true gap is large; finding good flows may be the main problem. The method requires the target move graph to connect every reference transition through legal paths, so hard kinetic constraints or disconnected ergodic components can make the comparison unusable. A gap comparison does not automatically transfer a sharp log-Sobolev constant, and spectral-gap bounds may lose important density or system-size powers. For infinite-volume IPS one still needs a uniform finite-volume estimate plus a legitimate passage to the limit.

## Sources

- Diaconis, Saloff-Coste, *Comparison theorems for reversible Markov chains*, Theorem 2.1, pp. 698-699, and Theorem 2.3, pp. 704-705, https://doi.org/10.1214/AOAP/1177005359.
- Same paper, Section 3, Theorems 3.1 and 3.2, for the finite exclusion-process application.
