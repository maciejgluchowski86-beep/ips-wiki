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

Let $\mathcal L$ and $\mathcal L'$ be spin-system generators with semigroups $P_t$ and $P_t'$. Suppose $\mathcal L$ is [patch positive](patch-positivity-property.md) and

$$
\mathcal L f(\eta)
=
\mathcal L'f(\eta)
+
\sum_{i\in\Lambda}d_i
\bigl(f(\eta^{i,0})-f(\eta)\bigr),
\qquad d_i\ge0.
\tag{1}
$$

Thus $\mathcal L'$ is obtained by removing an environment-independent mechanism that creates the facilitating state $0$ in the spin system, equivalently a pure-death mechanism in the signed dual.

## Corollary

The generator $\mathcal L'$ is patch positive with the same [patch threshold profile](patch-critical-density.md) $\mathbf p^\star$. For every $\mu\in\mathcal M_*$, every $A\Subset\Lambda$, and every $t\ge0$,

$$
(\mu P_t)(\chi_A)
\le
(\mu P_t')(\chi_A).
\tag{2}
$$

This is a comparison of joint occupation moments, not a stochastic-domination assertion.

## Proof: patch positivity of the comparison generator

Only the empty-neighbour calm-to-facilitating coefficient changes. For $\mathcal L'$, the coefficient $c_i^1(\varnothing)$ is replaced by

$$
c_i^{\prime\,1}(\varnothing)=c_i^1(\varnothing)-d_i.
$$

All nonempty-target coefficients are unchanged. Therefore the first patch-positivity inequality

$$
c_i^0(S)+c_i^1(S)\le0
$$

is unchanged.

Suppose first that the new empty-neighbour sum

$$
c_i^0(\varnothing)+c_i^1(\varnothing)-d_i
$$

is positive. The second patch-positivity expression for $\mathcal L'$ is

$$
\bigl(c_i^1(\varnothing)-d_i\bigr)c_i^0(S)
-
c_i^0(\varnothing)c_i^1(S).
\tag{3}
$$

If $c_i^0(S)\le0$, subtracting $d_i c_i^0(S)$ makes (3) at least as large as the original nonnegative determinant

$$
c_i^1(\varnothing)c_i^0(S)-c_i^0(\varnothing)c_i^1(S).
$$

If $c_i^0(S)>0$, the first coefficient inequality forces $c_i^1(S)<0$. Both terms in (3) are then nonnegative. Thus the second coefficient criterion holds for $\mathcal L'$.

Suppose instead that the new empty-neighbour sum vanishes. The residual rate function $c_i^{\prime\,1}$ is nonnegative, has zero constant coefficient, and has nonpositive nonconstant coefficients by the local-rate monotonicity consequence of patch positivity. Hence $c_i^{\prime\,1}\equiv0$. The first coefficient inequality gives $c_i^0(S)\le0$ for every nonempty $S$, while $c_i^0(\varnothing)=0$ and $c_i^0\ge0$, so $c_i^0\equiv0$. Thus the degenerate $r_i'=0$ clause of the patch-positivity criterion also holds.

Therefore $\mathcal L'$ is patch positive. Its nonempty multilinear coefficients are unchanged, so the coefficient formula for the threshold profile gives the same $\mathbf p^\star$.

## Proof: comparison of patch contributions

The two systems have the same dual interaction rates, the same successful-interaction skeleton, and the same reference and consistent patch laws. Only the Feynman-Kac potential changes. Equivalently, the function $\varphi_i$ is unchanged, while

$$
\psi_i'(\Delta,z)
=
c_i^0(\varnothing)
\int_0^\Delta e^{-\left(r_i-d_i\right)u}\,du
+
z e^{-\left(r_i-d_i\right)\Delta},
\tag{4}
$$

where

$$
r_i=c_i^0(\varnothing)+c_i^1(\varnothing).
$$

For $z\in[0,1]$, removing pure deaths slows the relaxation away from the active state and gives

$$
\psi_i'(\Delta,z)\ge\psi_i(\Delta,z).
\tag{5}
$$

Its slope in $z$ also increases:

$$
\partial_z\psi_i'(\Delta,z)
=e^{-(r_i-d_i)\Delta}
\ge
e^{-r_i\Delta}
=
\partial_z\psi_i(\Delta,z).
\tag{6}
$$

Substituting (5)-(6) into the [patch contribution formulas](patch-contribution.md), using patch positivity for both systems, yields

$$
0\le C(P)\le C'(P)
\tag{7}
$$

for every full patch. If $P$ is an end patch based at $i$, then

$$
0\le C(p_i^\star,P)
\le
C'(p_i^\star,P),
\tag{8}
$$

and, with

$$
\kappa(P)=\partial_z C(z,P),
\qquad
\kappa'(P)=\partial_z C'(z,P),
$$

one has

$$
0\le\kappa(P)\le\kappa'(P).
\tag{9}
$$

## Proof of the semigroup comparison

For a fixed successful-interaction skeleton, expand the end-factor average around $\mathbf p^\star$:

$$
\begin{aligned}
&\mu\left(
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right)\\
&\quad=
\sum_{\mathcal Q\subseteq\mathcal E_t}
\mu\left(
\chi^*_{\{i(P):P\in\mathcal Q\}}
\right)
\prod_{P\in\mathcal Q}\kappa(P)
\prod_{P\in\mathcal E_t\setminus\mathcal Q}
C(p_{i(P)}^\star,P).
\end{aligned}
\tag{10}
$$

If $\mu\in\mathcal M_*$, every centered moment in (10) is nonnegative. By (8)-(9), each summand is bounded above by the corresponding primed summand. By (7), the product of bulk contributions is also bounded by its primed counterpart. Hence, skeleton by skeleton, the complete weight appearing in the [patch representation](patch-representation-of-spin-systems.md) for $\mathcal L$ is bounded by the corresponding weight for $\mathcal L'$. Taking expectation over the skeleton proves (2).

## Invariant-measure comparison

Suppose in addition that the two systems have unique invariant probability measures $\pi$ and $\pi'$. Then

$$
\pi(\chi_A)\le\pi'(\chi_A)
\qquad
(A\Subset\Lambda).
\tag{11}
$$

### Proof

Apply (2) with the all-one product law $\mu_{\mathbf1}\in\mathcal M_*$ and average over $t\in[0,T]$. Every subsequential weak limit of either family of Cesaro averages is invariant. Uniqueness identifies the limits as $\pi$ and $\pi'$. Passing to the limit in the monomial inequality gives (11).
