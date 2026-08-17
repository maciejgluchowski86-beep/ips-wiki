---
method_id: lu-yau-martingale-conditional-variance
title: Lu-Yau martingale and conditional-variance recursion
category: functional-inequality
targets:
  - spectral-gap
  - log-sobolev
  - convergence
model_scope: Conservative Glauber/Kawasaki and Ginzburg-Landau type spin systems with canonical constraints
source_status: primary-checked
primary_source: Claudio Landim, Gustavo Panizo, and Horng-Tzer Yau, Spectral gap and logarithmic Sobolev inequality for unbounded conservative spin systems, Annales de l'Institut Henri Poincare Probabilites et Statistiques 38 (2002), 739-777.
primary_pinpoint: Section 3, especially Step 2 variance decomposition and equations (3.1)-(3.6); Theorem 2.1; Section 4 for the entropy analogue proving Theorem 2.2
primary_url: https://doi.org/10.1016/S0246-0203(02)01108-1
application_source: Sheng Lin Lu and Horng-Tzer Yau, Spectral gap and logarithmic Sobolev inequality for Kawasaki and Glauber dynamics, Communications in Mathematical Physics 156 (1993), 399-433.
application_pinpoint: Main spectral-gap and logarithmic-Sobolev theorems; Landim-Panizo-Yau explicitly identify this article as introducing the martingale approach
application_url: https://doi.org/10.1007/BF02098489
wiki_candidate: yes
---

# Lu-Yau martingale and conditional-variance recursion

## Criterion

The Lu--Yau martingale method proves coercive inequalities by revealing coordinates, particles, or blocks one at a time and recursively controlling the variance or entropy of the conditional expectation. In the conservative setting of Landim--Panizo--Yau, let \(\nu_{L,M}\) be the canonical measure on \(L\) spins with fixed total mass \(M\), and let \(W(L)\) denote the worst inverse spectral-gap constant. Their Section 3 begins from the exact conditional-variance decomposition

\[
\operatorname{Var}_{\nu_{L,M}}(f)
=
\nu_{L,M}\!\left[\operatorname{Var}(f\mid \eta_L)\right]
+
\operatorname{Var}_{\nu_{L,M}}\!\left(\nu_{L,M}[f\mid\eta_L]\right).
\]

The first term is controlled by the \((L-1)\)-site induction hypothesis. The second is reduced to derivatives or exchanges of the one-coordinate conditional expectation and then estimated using equivalence-of-ensembles/local-limit information. This produces a recursion for \(W(L)\), ultimately yielding \(W(L)\le C L^2\), i.e. a spectral gap at least of order \(L^{-2}\). Section 4 performs the corresponding conditional-entropy recursion for the logarithmic Sobolev constant.

## Mechanism

Conservation destroys naive tensorization: after conditioning on one spin, the other spins remain coupled through the fixed total mass. The martingale decomposition isolates this dependence in a single conditional-expectation term. The proof then asks a sharper question than a block decomposition: how sensitive is
\(\nu[f\mid\eta_L]\) to changing the revealed coordinate? For conservative models this sensitivity can be rewritten in terms of exchange gradients of \(f\), plus covariance errors coming from the canonical constraint.

The method becomes recursive because the conditional law of the unrevealed coordinates is again a smaller canonical ensemble. A local central limit theorem, equivalence of ensembles, and large-deviation estimates bound the covariance errors uniformly in the conserved mass. Once those errors are small enough at large scale, the recursion closes with the diffusive \(L^2\) order. The entropy version uses the same filtration but replaces variance decomposition by conditional entropy and needs stronger moment estimates.

This differs from the overlapping-block bisection method: bisection recursively cuts physical regions and pays overlap errors, while Lu--Yau recursion follows a filtration/conditional expectation and exploits the algebra of the conserved quantity.

## Representative IPS use

Lu and Yau introduced the martingale approach for Kawasaki and Glauber dynamics. Landim--Panizo--Yau give a particularly explicit conservative-spin implementation for reversible Ginzburg--Landau dynamics whose single-site potential is a bounded perturbation of a Gaussian. Their Theorems 2.1 and 2.2 establish spectral-gap and logarithmic-Sobolev constants of diffusive order \(L^{-2}\), uniformly in the conserved mean. Such estimates imply quantitative relaxation on the canonical sector and are key inputs in hydrodynamic-limit arguments for conservative IPS.

## Limitations

The recursion is not automatic from conditioning alone. One needs uniform control of the conditional law as the conserved quantity varies, typically through equivalence of ensembles, local central limit estimates, covariance bounds, or a related one-block theorem. Near phase coexistence or for heavy-tailed/nonconvex canonical measures these ingredients can fail. The method is especially natural for a single additive conservation law; several conserved quantities or hard constraints can make the conditional sensitivity substantially harder. A spectral gap on a canonical sector also does not by itself compare different conserved sectors or imply uniqueness of an unconstrained infinite-volume invariant law.

## Sources

- Landim, Panizo, Yau, *Spectral gap and logarithmic Sobolev inequality for unbounded conservative spin systems*, Theorem 2.1 and Section 3, especially Step 2 and equations (3.1)--(3.6); Section 4 and Theorem 2.2 for LSI, https://doi.org/10.1016/S0246-0203(02)01108-1.
- Lu, Yau, *Spectral gap and logarithmic Sobolev inequality for Kawasaki and Glauber dynamics*, Communications in Mathematical Physics 156 (1993), 399--433, https://doi.org/10.1007/BF02098489. Landim--Panizo--Yau explicitly cite this as the introduction of the martingale approach.
