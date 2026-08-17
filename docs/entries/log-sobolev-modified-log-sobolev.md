---
title: Logarithmic Sobolev and modified logarithmic Sobolev methods
status: literature
audit: current
tags:
  - ergodicity methods
  - functional inequalities
  - logarithmic Sobolev inequality
---

# Logarithmic Sobolev and modified logarithmic Sobolev methods

## Criterion

For a reversible heat-bath chain with invariant law \(\mu\), Caputo--Menz--Tetali distinguish two entropy inequalities. Their classical log-Sobolev inequality is
\[
\operatorname{Ent}_\mu(f)\le C\sum_i\mu\!\left[\operatorname{Var}_{\mu_i}(\sqrt f)\right],\qquad f\ge0,
\]
whereas their modified log-Sobolev inequality (mLSI) is
\[
\operatorname{Ent}_\mu(f)\le C\sum_i\mu\!\left[\operatorname{Cov}_{\mu_i}(f,\log f)\right].
\]
The conclusions are different: classical LSI is equivalent to hypercontractivity of the heat-bath semigroup, while mLSI is equivalent to exponential entropy decay
\[
\operatorname{Ent}_\mu(P_t f)\le e^{-t/C}\operatorname{Ent}_\mu(f).
\]
They also record \(LS(C)\Rightarrow MLS(C/4)\Rightarrow P(C/2)\). Thus either inequality is stronger than a bare [spectral-gap estimate](poincare-spectral-gap.md), but mLSI is the one directly matched to relative-entropy dissipation.

## Mechanism

For a density \(f\) with respect to \(\mu\), entropy dissipation along the reversible semigroup is the entropy-production functional appearing on the right of mLSI. The inequality closes the differential inequality \(d\operatorname{Ent}_\mu(P_t f)/dt\le-C^{-1}\operatorname{Ent}_\mu(P_t f)\). Classical LSI instead controls the Dirichlet form of \(\sqrt f\); Gross's semigroup argument converts it into hypercontractive \(L^p\to L^q\) bounds and, through standard implications, also yields mLSI and Poincare estimates.

A major proof device is [entropy factorization](block-factorization-entropy.md). Caputo--Menz--Tetali define approximate tensorization
\[
\operatorname{Ent}_\mu(f)\le C\sum_i\mu[\operatorname{Ent}_{\mu_i}(f)].
\]
Their Proposition 1.1 shows that this immediately implies both Poincare and mLSI with the same constant. Theorem 2.1 and Corollary 2.3 give weak-dependence criteria under which the tensorization constant is dimension-free.

## Representative IPS use

For finite-spin Gibbs systems, Stroock--Zegarlinski give a canonical [spatial-to-functional application](dobrushin-shlosman-spatial-to-dynamical.md): their Theorem 1.2 identifies the Dobrushin--Shlosman mixing condition with a uniform logarithmic Sobolev inequality for the finite-range lattice system, and Theorems 3.2 and 3.6 connect these conditions to a uniform rate of convergence of the associated Glauber dynamics. This is stronger information than uniqueness of the Gibbs state alone.

Caputo--Menz--Tetali give a more explicit high-temperature weak-dependence route. Corollary 2.3 proves approximate tensorization under the quantitative condition \(q<2/3\) in their notation, and Section 2.2 specializes it to Ising/Potts systems on graphs, yielding dimension-free mLSI and Poincare constants in a Dobrushin-type regime.

## Limitations

Classical LSI and mLSI should not be treated as interchangeable labels: hypercontractivity and entropy decay are different semigroup properties, and constants convert nontrivially. These inequalities are usually proved under reversibility and substantial spatial mixing/high-temperature hypotheses. Uniform LSI can fail near phase coexistence even when finite-volume chains remain irreducible. Approximate-tensorization criteria based on worst-case conditional influences can be far from the true one-phase region. Finally, entropy decay for densities absolutely continuous with respect to \(\mu\) does not by itself resolve convergence from singular infinite-volume initial configurations.

## Sources

- Caputo, Menz, Tetali, *Approximate tensorization of entropy at high temperature*, Section 1.1, Proposition 1.1, Theorem 2.1, Corollary 2.3 and Section 2.2, https://doi.org/10.5802/afst.1460.
- Stroock, Zegarlinski, *The equivalence of the logarithmic Sobolev inequality and the Dobrushin-Shlosman mixing condition*, Theorem 1.2 and Theorems 3.2, 3.6, https://doi.org/10.1007/BF02101094.
