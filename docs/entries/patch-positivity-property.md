---
title: Patch positivity property
status: proved here
tags:
  - duality
  - spin systems
  - patch
  - positivity
---

# Patch positivity property

The patch positivity property is a coefficient criterion ensuring that every bulk patch contribution in the [patch representation of spin systems](patch-representation-of-spin-systems.md) is nonnegative. Together with the [patch critical density](patch-critical-density.md), it separates bulk positivity from the density threshold needed for nonnegative end contributions. It is expressed in the spin-rate notation of [monomial duality for spin systems](monomial-duality-for-spin-systems.md), and uses the bulk rows of the [patch contribution](patch-contribution.md) formula.

## Criterion

All bulk patch contributions at source site \(i\) are nonnegative for every patch length and every initial interaction target if and only if, for every nonempty \(S\subseteq N(i)\),

$$
\begin{cases}
c_i^0(S)+c_i^1(S)\le0,
\qquad
c_i^1(\vn)c_i^0(S)-c_i^0(\vn)c_i^1(S)\ge0,
& c_i^0(\vn)+c_i^1(\vn)>0,\\[0.6em]
c_i^0(S)+c_i^1(S)\le0,
\qquad
c_i^1(S)\le0,
& c_i^0(\vn)+c_i^1(\vn)=0.
\end{cases}
$$

The second line is the degenerate case: since \(c_i^0(\vn)\) and \(c_i^1(\vn)\) are nonnegative rates, \(c_i^0(\vn)+c_i^1(\vn)=0\) is equivalent to \(c_i(\mathbf 0)=0\) and \(c_i(\mathbf 0^{i,1})=0\). This case is usually peripheral because both empty-neighbour flip rates vanish.

## Proof

The bulk patch formula has four rows. For \(\operatorname{type}(P)\in\{\mathsf{SI},\mathsf{II}\}\),

$$
C(P)=\frac{\psi_i(\Delta,1)}{\varphi_i(\Delta)}.
$$

Here \(\varphi_i(\Delta)>0\), and \(\psi_i(\Delta,1)\ge0\) because \(c_i^0(\vn)\) and \(c_i^1(\vn)\) are nonnegative rates. Hence these rows are nonnegative without any extra condition.

For \(\operatorname{type}(P)\in\{\mathsf{SO},\mathsf{IO}\}\),

$$
C(P)=e^{V_i\Delta}>0.
$$

For \(\operatorname{type}(P)=\mathsf{OO}\), the initial interaction target is a nonempty set \(S\subseteq N(i)\), and the contribution is

$$
C(P)=\sigma_i^\beta(S)e^{V_i\Delta}.
$$

Since

$$
\beta_i(S)\sigma_i^\beta(S)=-c_i^0(S)-c_i^1(S),
$$

this row is nonnegative exactly when

$$
c_i^0(S)+c_i^1(S)\le0.
$$

It remains to check \(\operatorname{type}(P)=\mathsf{OI}\). Its denominator is positive on patches where the displayed formula applies, and its numerator is

$$
c_i^0(S)-\left(c_i^0(S)+c_i^1(S)\right)\psi_i(\Delta,1).
$$

Under the \(\mathsf{OO}\) condition, the coefficient of \(\psi_i(\Delta,1)\) in this numerator is nonnegative. If \(c_i^0(\vn)+c_i^1(\vn)>0\), then

$$
\psi_i(\Delta,1)
=
\frac{c_i^0(\vn)}{c_i^0(\vn)+c_i^1(\vn)}
+
\frac{c_i^1(\vn)}{c_i^0(\vn)+c_i^1(\vn)}
e^{-\left(c_i^0(\vn)+c_i^1(\vn)\right)\Delta}.
$$

Thus the numerator is nonnegative for all \(\Delta\ge0\) if and only if it is nonnegative at the limiting value of \(\psi_i(\Delta,1)\), namely

$$
c_i^0(S)-\left(c_i^0(S)+c_i^1(S)\right)
\frac{c_i^0(\vn)}{c_i^0(\vn)+c_i^1(\vn)}\ge0.
$$

Multiplying by the positive denominator gives

$$
c_i^1(\vn)c_i^0(S)-c_i^0(\vn)c_i^1(S)\ge0.
$$

If \(c_i^0(\vn)+c_i^1(\vn)=0\), then \(\psi_i(\Delta,1)=1\), and the \(\mathsf{OI}\) numerator is

$$
c_i^0(S)-\left(c_i^0(S)+c_i^1(S)\right)=-c_i^1(S).
$$

Therefore the \(\mathsf{OI}\) row is nonnegative in the degenerate case exactly when \(c_i^1(S)\le0\). This completes the systematic check of all bulk patch types.
