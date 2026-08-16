---
title: Patch threshold profile
status: proved here
audit: current
tags:
  - patch
  - patch positivity
  - threshold profile
  - spin systems
---

# Patch threshold profile

For a patch-positive spin system, the **patch threshold profile**

$$
\mathbf p^\star=(p_i^\star)_{i\in\Lambda}
$$

records the calm-state density above which every end-patch contribution is nonnegative. It is not an ergodicity threshold or a phase-transition critical density.

## Definition

For each site $i$,

$$
p_i^\star
=
\inf\left\{
p\in[0,1]:
C(p,P)\ge0
\text{ for every end patch based at }i
\right\}.
\tag{1}
$$

Incoming end patches are nonnegative for every $p\in[0,1]$. The restriction comes from outgoing end patches.

## Coefficient formula

Under [patch positivity](patch-positivity-property.md),

$$
p_i^\star
=
\max\left\{
0,
\sup_{\substack{
\vn\ne S\subseteq N(i)\\
c_i^0(S)+c_i^1(S)<0
}}
\frac{c_i^0(S)}{c_i^0(S)+c_i^1(S)}
\right\}.
\tag{2}
$$

If the index set in the supremum is empty, the supremum contributes no positive restriction. At a site with $c_i^0(\vn)+c_i^1(\vn)=0$, patch positivity forces $c_i\equiv0$ and hence $p_i^\star=0$.

## Empty-neighbour bound

If

$$
r_i=c_i^0(\vn)+c_i^1(\vn)>0,
$$

then

$$
p_i^\star
\le
\frac{c_i^0(\vn)}{c_i^0(\vn)+c_i^1(\vn)}.
\tag{3}
$$

Indeed, for every nonempty $S$ with $c_i^0(S)+c_i^1(S)<0$, the determinant inequality in the patch-positivity criterion is equivalent to the corresponding ratio in (2) being at most the right-hand side of (3).

The profile $\mathbf p^\star$ is the centering profile for the [centered-moment cones](high-density-measure.md).
