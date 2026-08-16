---
title: Monomial Feynman-Kac duality for spin systems
status: proved here
audit: current
tags:
  - duality
  - spin systems
  - monomials
  - Feynman-Kac
---

# Monomial Feynman-Kac duality for spin systems

This entry records the signed monomial dual used in the canonical paper *Patch representations and convergence for facilitated spin systems*. The generator calculation and the infinite-volume Feynman-Kac formula are proved there.

Let

$$
\cL f(\eta)=\sum_{i\in\Lambda}c_i(\eta)\bigl(f(\eta^i)-f(\eta)\bigr)
$$

be a uniformly bounded finite-range [spin system](spin-system.md). Write

$$
c_i(\eta)=(1-\eta(i))c_i^0(\eta)+\eta(i)c_i^1(\eta),
$$

where each $c_i^x$ depends only on the finite neighbour set $N(i)$, and expand

$$
c_i^x(\eta)=\sum_{S\subseteq N(i)}c_i^x(S)\chi_S(\eta),
\qquad x\in\{0,1\}.
$$

For the ordinary [monomials](monomials.md)

$$
\chi_A(\eta)=\prod_{i\in A}\eta(i),
$$

set

$$
a_i^\delta(S)=c_i^0(S),
\qquad
a_i^\beta(S)=-c_i^0(S)-c_i^1(S).
$$

Define the signed-dual rates and signs by

$$
\delta_i(S)=|a_i^\delta(S)|,
\qquad
\sigma_i^\delta(S)=\operatorname{sgn}_\pm a_i^\delta(S),
$$

and, for $S\ne\vn$,

$$
\beta_i(S)=|a_i^\beta(S)|,
\qquad
\sigma_i^\beta(S)=\operatorname{sgn}_\pm a_i^\beta(S),
$$

with $\beta_i(\vn)=0$. The corresponding [signed additive set process](signed-additive-set-process.md) has generator $\cD$.

## Generator identity

For $Y=(A,\sigma)$ define

$$
H(Y,\eta)=\sigma\chi_A(\eta).
$$

Put

$$
V(A)=\sum_{i\in A}V_i,
$$

where

$$
V_i=
\sum_{S\subseteq N(i)}\delta_i(S)
+
\sum_{\substack{S\subseteq N(i)\\S\ne\vn}}\beta_i(S)
+a_i^\beta(\vn).
$$

Then

$$
\cL_\eta H(Y,\eta)
=
\cD_YH(Y,\eta)+V(A)H(Y,\eta).
\tag{1}
$$

The underlying monomial calculation is

$$
\cL\chi_A
=
\sum_{i\in A}\sum_{S\subseteq N(i)}
a_i^\delta(S)\chi_{(A\setminus\{i\})\cup S}
+
\sum_{i\in A}\sum_{S\subseteq N(i)}
a_i^\beta(S)\chi_{A\cup S}.
$$

## Feynman-Kac formula

Write $\mathbb P_A$ and $\mathbb E_A$ for the signed set process started from $(A,+)$. Then for every $A\Subset\Lambda$, $t\ge0$, and $\eta\in\{0,1\}^\Lambda$,

$$
P_t\chi_A(\eta)
=
\mathbb E_A\left[
\sigma_t
\exp\left(\int_0^tV(A_s)\,ds\right)
\chi_{A_t}(\eta)
\right].
\tag{2}
$$

Uniform boundedness and finite range imply nonexplosion of the dual from finite initial sets; the paper proves (2) by finite-volume approximation and the required Feynman-Kac domination.

The [successful-interaction](successful-interaction.md) skeleton retains only the nonempty-target interactions that act on this dual. Conditioning on that skeleton and averaging the omitted marks gives the [patch representation](patch-representation-of-spin-systems.md).
