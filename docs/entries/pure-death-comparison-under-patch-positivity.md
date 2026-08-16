---
title: Pure-death comparison under patch positivity
status: proved here
audit: current
tags:
  - patch positivity
  - pure deaths
  - comparison
  - invariant measures
---

# Pure-death comparison under patch positivity

Let $\cL$ and $\cL'$ be spin-system generators with semigroups $P_t$ and $P_t'$. Suppose $\cL$ is [patch positive](patch-positivity-property.md) and

$$
\cL f(\eta)
=
\cL'f(\eta)
+
\sum_{i\in\Lambda}d_i
\bigl(f(\eta^{i,0})-f(\eta)\bigr),
\qquad d_i\ge0.
\tag{1}
$$

Thus $\cL'$ is obtained by removing an environment-independent mechanism creating the facilitating state $0$.

## Corollary

The generator $\cL'$ is patch positive with the same [patch threshold profile](patch-critical-density.md) $\mathbf p^\star$. For every $\mu\in\mathcal M_*$, every $A\Subset\Lambda$, and every $t\ge0$,

$$
(\mu P_t)(\chi_A)
\le
(\mu P_t')(\chi_A).
\tag{2}
$$

This is a comparison of joint occupation moments, not a stochastic-domination assertion.

## Patch comparison

The two systems have the same dual interaction rates, successful-interaction skeleton, and reference patch laws. Only the Feynman-Kac potential changes. The contribution formulas give

$$
0\le C(P)\le C'(P)
$$

for every full patch. For an end patch based at $i$,

$$
0\le C(p_i^\star,P)\le C'(p_i^\star,P),
$$

and the slope of the affine end contribution also increases.

Expanding the end factors around $\mathbf p^\star$ expresses each skeleton weight as a nonnegative linear combination of centered moments of $\mu\in\mathcal M_*$. The primed coefficient of every term dominates the unprimed one, so the [patch representation](patch-representation-of-spin-systems.md) gives (2) skeleton by skeleton and hence after expectation.

If the two systems have unique invariant measures $\pi$ and $\pi'$, the Cesaro argument gives

$$
\pi(\chi_A)\le\pi'(\chi_A)
$$

for every finite $A$.
