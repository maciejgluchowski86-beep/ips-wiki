---
method_id: large-set-conductance-warm-start
title: Large-set conductance and warm-start mixing
category: functional-inequality
targets:
  - mixing
  - convergence
model_scope: Finite reversible spin-system chains where an isoperimetric bound is available for sets of non-negligible stationary mass, even if tiny bottlenecks destroy a uniform spectral gap
source_status: primary-checked
primary_source: Ahmed El Alaoui, Ronen Eldan, Reza Gheissari, Arianna Piana, Fast relaxation of the random field Ising dynamics, Annals of Probability 54 (2026), 99-136.
primary_pinpoint: Section 3.3.1, equations (3.17)-(3.18) and Lemma 3.5 for large-set conductance to warm-start mixing; Theorems 1.2 and 1.4 for the RFIM application
primary_url: https://doi.org/10.1214/24-AOP1743
application_source: Ahmed El Alaoui, Ronen Eldan, Reza Gheissari, Arianna Piana, Fast relaxation of the random field Ising dynamics, Annals of Probability 54 (2026), 99-136.
application_pinpoint: Theorem 1.2, Theorem 1.4, and Section 3.3 polynomial relaxation and sampling under weak spatial mixing
application_url: https://arxiv.org/abs/2311.06171
wiki_candidate: yes
---

# Large-set conductance and warm-start mixing

## Criterion

For a finite reversible Markov chain with stationary law \(\pi\), write

\[
Q(S,S^c)=\sum_{x\in S,y\in S^c}\pi(x)P(x,y)
\]

for the stationary flow across a cut. A full Cheeger inequality asks for a linear lower bound on this flow uniformly over all sets of mass at most \(1/2\). A weaker but still useful criterion is **large-set expansion**. El Alaoui--Eldan--Gheissari--Piana consider bounds of the form

\[
\pi(S)(1-\pi(S))
\le A\,Q(S,S^c)^{1/p},
\qquad p\ge1,
\tag{C}
\]

for every \(S\). Equation (3.17) arises by applying their weak Poincare inequality to indicator functions, and the paper explicitly interprets it as a conductance bound most effective for sets whose stationary mass is not extremely small.

Lemma 3.5 shows that if `(C)` holds and the initial law \(\pi_0\) is an \(M\)-warm start,

\[
\sup_S\frac{\pi_0(S)}{\pi(S)}\le M,
\]

then the discrete-time chain satisfies a polynomial total-variation bound of the form

\[
d_{\mathrm{TV}}(\pi_k,\pi)
\le
M\left(\frac{A^{2p}\log k}{k}\right)^{1/(2p-1)}
\]

(up to the normalization of the transition kernel used in the lemma). Thus isoperimetry restricted to large sets can still prove quantitative mixing from warm starts even when no useful uniform spectral gap is available.

## Mechanism

The proof uses the Lovasz--Simonovits profile of a Markov chain. Conductance controls how quickly probability mass can remain concentrated on a set. Under a full Cheeger bound this yields exponential decay and a spectral-gap estimate. Under `(C)`, the expansion deteriorates as the target set becomes small; the corresponding profile recursion is nonlinear and gives polynomial decay instead.

Warmness is what prevents the initial law from hiding excessive mass in the tiny sets where the weak conductance estimate is least informative. One tracks the maximal excess mass that the evolving distribution can place on a set of stationary measure \(x\), uses the flow bound to force flattening of this profile, and iterates. The result is an isoperimetric route to mixing that remains meaningful in disordered systems with rare deep traps.

## Representative IPS use

The primary application is single-site heat-bath Glauber dynamics for the ferromagnetic random-field Ising model on finite subsets of \(\mathbb Z^d\). Under weak spatial mixing in expectation over the random field, Theorem 1.2 proves a weak Poincare inequality and algebraic variance relaxation with high probability over the disorder.

Applying that inequality to indicators gives the large-set conductance estimate `(C)`. Section 3.3.1 and Lemma 3.5 then turn it into polynomial mixing from warm starts. Theorem 1.4 exploits this in a sampling construction: grow the domain one vertex at a time, initialize the next Glauber chain from the previous approximate sample plus one new spin, verify that this is uniformly warm, and run long enough for the large-set conductance bound to mix it. Iterating produces a polynomial-time approximate RFIM sampler under WSM on the required cube-like intermediate domains.

## Limitations

Large-set conductance is weaker than a positive Cheeger constant. It may coexist with extremely small bottlenecks supported on tiny stationary sets, so it need not imply a positive spectral gap or worst-case rapid mixing. The warm-start hypothesis is essential to the stated mixing conclusion; an adversarial cold start may begin inside precisely such a rare trap.

The RFIM theorem is quenched-probabilistic: the conductance/weak-Poincare conclusions hold with high probability over the random field under spatial-mixing assumptions in expectation. The sampling theorem also requires WSM on a controlled family of intermediate cube-like domains, not merely the final box.

This method is distinct from canonical paths. Canonical paths prove a global Dirichlet-form comparison by routing every transition demand and controlling congestion. Large-set conductance works directly with cut flow in the chain's own state graph and can deliberately ignore poor expansion of very small sets. It is also distinct from the Dobrushin--Shlosman page: spatial mixing is one way the RFIM source obtains the weak Poincare inequality, while this page isolates the later **isoperimetric-to-dynamical** step.

## Sources

- El Alaoui, Eldan, Gheissari, Piana, *Fast relaxation of the random field Ising dynamics*, Theorems 1.2 and 1.4; Section 3.3.1, equations (3.17)--(3.18) and Lemma 3.5, https://doi.org/10.1214/24-AOP1743.
- Open primary version: https://arxiv.org/abs/2311.06171.
