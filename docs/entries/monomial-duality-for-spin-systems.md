---
title: Monomial duality for spin systems
status: proved here
tags:
  - duality
  - spin systems
  - monomials
---

# Monomial duality for spin systems

This entry gives the finite-set dual for a [spin system](spin-system.md) in the monomial basis

$$
\chi_A(\eta)=\prod_{i\in A}\eta(i).
$$

## Rate coefficients

Let

$$
\cL f(\eta)=\sum_{i\in\Lambda}c_i(\eta)\left(f(\eta^i)-f(\eta)\right).
$$

Write

$$
c_i(\eta)=(1-\eta(i))c_i^0(\eta)+\eta(i)c_i^1(\eta),
$$

where \(c_i^x(\eta)=c_i(\eta^{i,x})\). The functions \(c_i^0\) and \(c_i^1\) depend only on \(N(i)\). Expand them as

$$
c_i^x(\eta)=\sum_{S\subseteq N(i)}c_i^x(S)\chi_S(\eta),
\qquad x\in\{0,1\}.
$$

Define signed update coefficients

$$
\delta_i(S)=c_i^0(S),
\qquad
\beta_i(S)=-c_i^0(S)-c_i^1(S).
$$

## Generator action

For \(A\Subset\Lambda\),

$$
\cL\chi_A
=
\sum_{i\in A}\sum_{S\subseteq N(i)}
\delta_i(S)\chi_{(A\setminus\{i\})\cup S}
+
\sum_{i\in A}\sum_{S\subseteq N(i)}
\beta_i(S)\chi_{A\cup S}.
$$

Thus the only dual updates are activations of subsets of neighbouring sites. The \(\delta\)-update kills the source site \(i\); the \(\beta\)-update keeps it.

The coefficient of \(\chi_A\) in \(\cL\chi_A\) is

$$
\Gamma(A)=\sum_{i\in A}\sum_{\substack{S\subseteq N(i)\\ S\subseteq A}}\beta_i(S).
$$

## Dual process

Let \((A_t,\sigma_t)\) be the [signed additive set process](signed-additive-set-process.md) with coefficients \(\delta_i(S)\) and \(\beta_i(S)\). Its duality function is

$$
H(A,\sigma,\eta)=\sigma\chi_A(\eta).
$$

The Feynman--Kac potential is

$$
V(A)=
\sum_{i\in A}\sum_{S\subseteq N(i)}|\delta_i(S)|
+
\sum_{i\in A}\sum_{\substack{S\subseteq N(i)\\ S\not\subseteq A}}|\beta_i(S)|
+
\Gamma(A).
$$

Then

$$
\cL_\eta H(A,\sigma,\eta)
=
\cD_{A,\sigma}H(A,\sigma,\eta)+V(A)H(A,\sigma,\eta),
$$

and therefore

$$
\E_\eta[\chi_A(\eta_t)]
=
\E_{A,+}\left[
\sigma_t\exp\left(\int_0^t V(A_s)\,ds\right)
\chi_{A_t}(\eta)
\right].
$$

## Calculation

If \(i\notin A\), then \(\chi_A(\eta^i)=\chi_A(\eta)\). If \(i\in A\), then

$$
c_i(\eta)\left(\chi_A(\eta^i)-\chi_A(\eta)\right)
=
c_i^0(\eta)\chi_{A\setminus\{i\}}(\eta)
-
(c_i^0(\eta)+c_i^1(\eta))\chi_A(\eta).
$$

Inserting the monomial expansions of \(c_i^0\) and \(c_i^1\) gives the displayed generator action.
