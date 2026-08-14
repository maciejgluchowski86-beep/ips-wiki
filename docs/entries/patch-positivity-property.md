---
title: Patch positivity property
status: conditional
audit: current
tags:
  - duality
  - spin systems
  - patch
  - positivity
---

# Patch positivity property

This page records the project coefficient criterion for nonnegativity of bulk patch contributions. It is **conditional on the closed-form contribution identities** in [patch contribution](patch-contribution.md), which have not completed the current independent verification protocol.

## Conditional criterion

Assume the contribution formulas on the patch-contribution page are correct. Then all bulk patch contributions at source site $i$ are nonnegative for every patch length and every initial interaction target if and only if, for every nonempty $S\subseteq N(i)$,

$$
\begin{cases}
c_i^0(S)+c_i^1(S)\le0,
\qquad
c_i^1(\vn)c_i^0(S)-c_i^0(\vn)c_i^1(S)\ge0,
&c_i^0(\vn)+c_i^1(\vn)>0,\\[0.6em]
c_i^0(S)+c_i^1(S)\le0,
\qquad
c_i^1(S)\le0,
&c_i^0(\vn)+c_i^1(\vn)=0.
\end{cases}
\tag{1}
$$

The second line is the degenerate case. Since $c_i^0(\vn)$ and $c_i^1(\vn)$ are nonnegative rates, $c_i^0(\vn)+c_i^1(\vn)=0$ means that both empty-neighbour flip rates vanish.

## Dependence on the contribution identities

Under the current formulas, the $\mathsf{II}$ and $\mathsf{IO}$ bulk rows are automatically nonnegative. The $\mathsf{OO}$ row gives

$$
c_i^0(S)+c_i^1(S)\le0.
$$

For the $\mathsf{OI}$ row, the current formula has numerator

$$
c_i^0(S)-\left(c_i^0(S)+c_i^1(S)\right)\psi_i(\Delta,1).
$$

Using the current empty-neighbour relaxation formula for $\psi_i$ yields the determinant condition in the first line of (1), or $c_i^1(S)\le0$ in the degenerate case. Because this derivation depends on the unaudited contribution formulas, (1) remains conditional.

The [patch critical density](patch-critical-density.md), [patch representation of spin systems](patch-representation-of-spin-systems.md), and later comparison pages must therefore name this prerequisite explicitly rather than treat patch positivity as a verified theorem.
