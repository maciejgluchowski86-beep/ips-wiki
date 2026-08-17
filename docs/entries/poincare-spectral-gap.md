---
title: Poincare inequality and spectral-gap method
status: literature
audit: current
tags:
  - ergodicity methods
  - functional inequalities
  - spectral gap
---

# Poincare inequality and spectral-gap method

## Criterion

Let \((P_t)_{t\ge0}\) be a reversible Markov semigroup with invariant probability \(\mu\), generator \(L\), and Dirichlet form \(\mathcal E(f,f)=\mu[f(-Lf)]\). A Poincare inequality with constant \(C<\infty\) is
\[
\operatorname{Var}_\mu(f)\le C\,\mathcal E(f,f)
\]
for all functions in the form domain. Equivalently, the spectral gap satisfies \(\operatorname{gap}(-L)\ge C^{-1}>0\). For the heat-bath/Glauber generator in Caputo--Menz--Tetali, \(\mathcal E(f,f)=\sum_i\mu[\operatorname{Var}_{\mu_i}(f)]\), and their Section 1.1 records the equivalent semigroup estimate
\[
\operatorname{Var}_\mu(P_t f)\le e^{-2t/C}\operatorname{Var}_\mu(f).
\]
Thus a volume-uniform Poincare constant gives a volume-uniform exponential \(L^2(\mu)\) relaxation rate.

## Mechanism

Reversibility makes \(-L\) self-adjoint and nonnegative. The Poincare inequality excludes spectrum in \((0,C^{-1})\) on the mean-zero subspace. Applying it to \(P_t f\) and differentiating the variance gives
\[
\frac{d}{dt}\operatorname{Var}_\mu(P_t f)
=-2\mathcal E(P_t f,P_t f)
\le -\frac{2}{C}\operatorname{Var}_\mu(P_t f),
\]
so Gronwall yields exponential variance decay. In finite volume this also controls the usual relaxation time. In infinite volume, a uniform finite-volume inequality is often combined with exhaustion or direct form arguments to obtain a positive infinite-volume gap.

The proof task is therefore shifted from long-time dynamics to a static coercive inequality. Typical ways to establish it include tensorization, variance decomposition, [comparison of Dirichlet forms](dirichlet-form-canonical-path-comparison.md), [block/bisection arguments](block-dynamics-bisection-variance.md), or [martingale conditional-variance recursion](lu-yau-martingale-conditional-variance.md). These are separate toolbox methods rather than part of the criterion itself.

## Representative IPS use

Cancrini--Martinelli--Roberto--Toninelli apply this strategy to [kinetically constrained spin models](kinetically-constrained-spin-model.md), whose reversible measure is Bernoulli product but whose update rates can vanish. Their Theorem 3.3 states that if, at some block scale, a sufficiently probable good event satisfies their legal-move condition, then the infinite-volume generator has positive spectral gap. Corollary 3.5 gives a concrete bootstrap-percolation version: if a large block is internally spanned with probability tending to one and the corresponding zero-boundary block chain is ergodic, then the gap is positive. Their Theorem 2.2 identifies simplicity of the zero eigenvalue with \(L^2(\mu)\) convergence, hence mixing and ergodicity of \(\mu\).

## Limitations

The basic method is naturally reversible; nonreversible chains need different coercive or hypocoercive tools. A positive gap controls \(L^2(\mu)\) relaxation, not automatically total-variation mixing from every initial state on an infinite state space. It also does not by itself prove uniqueness of all invariant measures. This distinction is concrete for KCSM: blocked configurations can support other stationary measures even while the Bernoulli reversible measure is mixing. Near criticality the gap may be positive but extremely small, so proving positivity alone can give little quantitative information.

## Sources

- Caputo, Menz, Tetali, *Approximate tensorization of entropy at high temperature*, Section 1.1, equations (1.5)-(1.10), DOI: https://doi.org/10.5802/afst.1460. This is used as a representative primary formulation of the Poincare/semigroup equivalence, not as an origin claim.
- Cancrini, Martinelli, Roberto, Toninelli, *Kinetically constrained spin models*, Theorem 2.2, Theorem 3.3 and Corollary 3.5, https://arxiv.org/abs/math/0610106.
