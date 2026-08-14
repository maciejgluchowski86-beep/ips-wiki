---
title: Pure-death comparison under patch positivity
status: conditional
audit: current
tags:
  - patch positivity
  - pure deaths
  - comparison
  - invariant measures
---

# Pure-death comparison under patch positivity

This page records the project pure-death comparison as a **conditional statement**. The comparison depends on the unverified patch representation and on a coefficientwise comparison of patch contributions; neither prerequisite is currently a verified project theorem.

Let $\cL$ and $\cL'$ be uniformly bounded finite-range [spin-system](spin-system.md) generators such that

$$
\cL=\cL'+\mathcal D_{\mathbf a},
$$

where

$$
\mathcal D_{\mathbf a}f(\eta)
=
\sum_{i\in\Lambda}a_i\left(f(\eta^{i,0})-f(\eta)\right),
\qquad a_i\ge0.
$$

Let $P_t$ and $P_t'$ be their semigroups.

## Required patch hypotheses

Assume all of the following for the two systems:

1. the conditional [patch representation of spin systems](patch-representation-of-spin-systems.md) is valid for the monomials under consideration;
2. the two representations use the same successful-interaction skeleton and a common centering profile $\mathbf p^\star$;
3. for every bulk patch $P$, the contribution comparison
   $$
   0\le C(P)\le C'(P)
   \tag{1}
   $$
   holds; and
4. every end contribution has the affine forms
   $$
   \begin{aligned}
   C(z,P)&=C(p_i^\star,P)+b(P)(z-p_i^\star),\\
   C'(z,P)&=C'(p_i^\star,P)+b'(P)(z-p_i^\star),
   \end{aligned}
   $$
   with
   $$
   0\le C(p_i^\star,P)\le C'(p_i^\star,P),
   \qquad
   0\le b(P)\le b'(P).
   \tag{2}
   $$

The current project patch calculations claim (1)--(2) for removal of pure deaths under the conditional patch-positivity criterion, but that claim has not completed independent verification. This page therefore takes (1)--(2) as explicit prerequisites.

## Conditional comparison

Under the hypotheses above, for every $\nu\in\mathcal M_\star$, every $A\Subset\Lambda$, and every $t\ge0$, the coefficientwise end-factor expansion in the patch representation gives

$$
\nu(P_t\chi_A)\le\nu(P_t'\chi_A).
\tag{3}
$$

The reason is purely coefficientwise once the patch representation and (1)--(2) are assumed: every centered moment of $\nu\in\mathcal M_\star$ entering the end-factor expansion is nonnegative, and each bulk or end coefficient is bounded above by its primed counterpart.

## Conditional invariant-measure comparison

If, in addition, the two systems have unique invariant measures $\pi$ and $\pi'$ and the usual Cesàro limiting argument applies, then (3) gives

$$
\pi(\chi_A)\le\pi'(\chi_A)
\qquad\text{for every }A\Subset\Lambda.
\tag{4}
$$

Equation (4) compares joint occupation moments. It does not by itself assert stochastic domination.
