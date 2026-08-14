---
title: Monomial monotonicity for high-density measures
status: conditional
audit: current
tags:
  - patch positivity
  - high-density measure
  - centered moments
  - monotonicity
---

# Monomial monotonicity for high-density measures

This page isolates the coefficient conditions actually used by the project monotonicity argument. It does not import the unverified [patch positivity property](patch-positivity-property.md) as an established premise.

Fix a profile $\mathbf p^\star=(p_i^\star)_{i\in\Lambda}\in[0,1]^\Lambda$ and the centered monomials from [high-density measure](high-density-measure.md),

$$
\chi_A^\star(\eta)=\prod_{i\in A}(\eta(i)-p_i^\star).
$$

## Explicit coefficient hypotheses

Use the coefficient notation from [monomial duality for spin systems](monomial-duality-for-spin-systems.md). For $S\subseteq N(i)$ define

$$
d_i(S)
=
c_i^0(S)-p_i^\star\left(c_i^0(S)+c_i^1(S)\right),
$$

and for $S\ne\vn$ define

$$
b_i(S)=-c_i^0(S)-c_i^1(S).
$$

Assume explicitly that

$$
d_i(S)\ge0
\qquad\text{for every }i\text{ and }S\subseteq N(i),
\tag{1}
$$

and

$$
b_i(S)\ge0
\qquad\text{for every }i\text{ and }\vn\ne S\subseteq N(i).
\tag{2}
$$

These are the sign inequalities required below. No assertion is made here that the current patch-positivity or critical-density calculations imply (1)--(2).

## Finite-to-infinite-volume hypothesis

Assume the spin system is defined in infinite volume and admits finite-volume approximations $P_t^{\Lambda_n}$ along an exhaustion $\Lambda_n\uparrow\Lambda$ such that, for every finite $A$ and fixed $t\ge0$,

$$
\left\|P_t^{\Lambda_n}\chi_A^\star-P_t\chi_A^\star\right\|_\infty
\longrightarrow0.
\tag{3}
$$

The finite-volume generators are required to have the same local coefficient identities (1)--(2) on the sites relevant to $\chi_A^\star$ once $n$ is large. This is the precise approximation assumption used to transfer coefficient positivity to infinite volume.

## Conditional monotonicity statement

Under (1)--(3), if probability measures $\nu_0,\nu_1$ satisfy

$$
\nu_0(\chi_B^\star)\le\nu_1(\chi_B^\star)
\qquad\text{for every }B\Subset\Lambda,
\tag{4}
$$

then the current generator argument gives

$$
\nu_0(P_t\chi_A^\star)\le\nu_1(P_t\chi_A^\star)
\tag{5}
$$

for every finite $A$ and $t\ge0$. Since

$$
\chi_A
=
\sum_{B\subseteq A}
\left(\prod_{i\in A\setminus B}p_i^\star\right)\chi_B^\star,
$$

the same hypotheses give

$$
\nu_0(P_t\chi_A)\le\nu_1(P_t\chi_A).
\tag{6}
$$

The finite-volume calculation underlying (5) is

$$
\cL\chi_A^\star
=
\sum_{i\in A}
\left[
-r_i\chi_A^\star
+
\sum_{S\subseteq N(i)}d_i(S)\chi_S\chi_{A\setminus\{i\}}^\star
+
\sum_{\vn\ne S\subseteq N(i)}b_i(S)\chi_S\chi_A^\star
\right],
$$

where $r_i=c_i^0(\vn)+c_i^1(\vn)$, together with the algebraic identity

$$
\chi_S\chi_B^\star
=
\left(\prod_{j\in S\cap B}(1-p_j^\star)\right)
\sum_{R\subseteq S}
\left(\prod_{j\in S\setminus R}p_j^\star\right)
\chi_{R\cup(B\setminus S)}^\star.
$$

Under (1)--(2), all off-diagonal coefficients in the finite centered-monomial system are nonnegative. The infinite-volume conclusion remains conditional on the approximation hypothesis (3).
