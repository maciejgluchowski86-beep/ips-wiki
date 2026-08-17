---
method_id: disagreement-percolation-gibbs-uniqueness
title: Disagreement percolation for Gibbs uniqueness
category: spatial-mixing
targets:
  - uniqueness
model_scope: Finite or countably infinite locally finite spin/Markov fields with boundary-condition couplings dominated by independent site percolation
source_status: primary-checked
primary_source: J. van den Berg and C. Maes, Disagreement percolation in the study of Markov fields, Annals of Probability 22 (1994), 749-763
primary_pinpoint: Theorem 1 and Corollaries 1-2, pp. 752-755; proof of Theorem 1 and Corollaries 1-2, pp. 759-762
primary_url: https://doi.org/10.1214/aop/1176988728
application_source: J. van den Berg and C. Maes, Disagreement percolation in the study of Markov fields, Annals of Probability 22 (1994), 749-763
application_pinpoint: Example 1, p. 756, hard-core lattice gas
application_url: https://doi.org/10.1214/aop/1176988728
wiki_candidate: yes
---

# Disagreement percolation for Gibbs uniqueness

## Criterion

Let $\gamma$ be a single-site specification on a locally finite graph. For each vertex $i$, define a worst-case boundary sensitivity $p_i$ by maximizing the total-variation distance between the single-site conditional laws at $i$ over admissible exterior configurations. Van den Berg and Maes construct, for two finite-volume Gibbs fields with different boundary conditions, a coupling whose disagreement indicator is dominated by an independent Bernoulli field with site-open probabilities $(p_i)$.

The crucial geometric property is that every interior disagreement must be connected by a path of disagreements to the boundary where the two boundary conditions differ. Consequently, for an event $E$ depending on a finite set $A$,

\[
|\gamma_\Lambda(E\mid\eta)-\gamma_\Lambda(E\mid\eta')|
\leq
\mathbb P_{(p_i)}\bigl(A\longleftrightarrow\partial\Lambda\bigr).
\]

Corollary 2 gives the infinite-volume uniqueness criterion

\[
\mathbb P_{(p_i)}(\text{there exists an infinite open path})=0
\quad\Longrightarrow\quad
\text{at most one Gibbs measure}.
\]

In particular, if $\sup_i p_i<p_c(G)$ for independent site percolation on the underlying graph, uniqueness follows.

## Mechanism

The coupling is built sequentially using optimal single-site couplings. At each newly exposed vertex, the probability that the two spins disagree is at most the corresponding $p_i$. These disagreement indicators can therefore be coupled below an independent Bernoulli percolation field.

Optimal coupling alone is not enough. The Markov-field property supplies the second key fact: if a site has no neighboring disagreement among the already exposed sites and is not adjacent to a boundary disagreement, the two conditional distributions at that site coincide, so the optimal coupling makes the spins agree almost surely. Hence a disagreement observed deep inside the volume forces an entire connected disagreement path back to the boundary.

Subcritical percolation then removes boundary influence at large distances. If two infinite-volume Gibbs measures existed, apply the finite-volume boundary estimate to a fixed local event while sending the boundary to infinity. The probability of an open path from the event to that receding boundary tends to zero when there is no infinite Bernoulli cluster, forcing the two Gibbs measures to agree on every local event.

This differs from Dobrushin's sum-of-influences criterion. It retains the geometry of influence propagation: many individually possible disagreements are harmless if they cannot form a long connected path.

## Representative IPS use

The hard-core lattice gas is a binary constrained spin field. Van den Berg--Maes compute in Example 1 that the disagreement parameter is $p=a/(1+a)$, where $a$ is the activity. Their percolation criterion gives uniqueness whenever

\[
\frac{a}{1+a}<p_c,
\qquad\text{equivalently}\qquad
a<\frac{p_c}{1-p_c}.
\]

The paper emphasizes that this geometric criterion can improve on the single-site Dobrushin bound for hard-core and strongly repulsive systems on low-dimensional graphs, while the opposite can occur for ferromagnetic Ising models.

## Limitations

This checked theorem is a **static Gibbs uniqueness method**. It does not by itself give convergence of Glauber dynamics, coupling time, or a spectral gap. Dynamical arguments that dominate space-time disagreements by a subcritical contact or oriented-percolation process are closely related but constitute a distinct method.

The criterion can also be conservative because $p_i$ is a worst-case single-site sensitivity and the dominating field is independent. If these maxima are large, independent percolation may survive although the true dependent disagreement set does not. The method needs useful geometric information about the percolation threshold of the underlying graph. As the source notes, for ferromagnetic Ising systems the Dobrushin criterion can outperform disagreement percolation because changing one remote boundary spin has much less effect than the unconstrained worst-case boundary comparison defining $p_i$.

## Sources

Primary source: J. van den Berg and C. Maes, *Disagreement percolation in the study of Markov fields*, Annals of Probability 22 (1994), 749-763, Theorem 1 and Corollaries 1-2, with proofs on pp. 759-762. https://doi.org/10.1214/aop/1176988728

A stable author-institution copy of the paper is available through CWI: https://ir.cwi.nl/pub/1472
