---
title: Monomial duality for spin systems
status: conditional
audit: current
tags:
  - duality
  - spin systems
  - monomials
---

# Monomial duality for spin systems

This entry records the algebraic generator calculation behind finite-set [duality](duality.md) for a [spin system](spin-system.md) in the ordinary [monomial](monomials.md) basis

$$
\chi_A(\eta)=\prod_{i\in A}\eta(i).
$$

The generator calculation below is direct. The Feynman--Kac semigroup formula is conditional on the analytic hypotheses stated below; it is not currently a verified project theorem.

## Rate coefficients

Let

$$
\cL f(\eta)=\sum_{i\in\Lambda}c_i(\eta)\left(f(\eta^i)-f(\eta)\right).
$$

Write

$$
c_i(\eta)=(1-\eta(i))c_i^0(\eta)+\eta(i)c_i^1(\eta),
$$

where $c_i^x(\eta)=c_i(\eta^{i,x})$. Assume $c_i^0$ and $c_i^1$ depend only on the finite neighbour set $N(i)$. Their monomial expansions are

$$
c_i^x(\eta)=\sum_{S\subseteq N(i)}c_i^x(S)\chi_S(\eta),
\qquad x\in\{0,1\}.
$$

Define

$$
a_i^\delta(S)=c_i^0(S),
\qquad
a_i^\beta(S)=-c_i^0(S)-c_i^1(S).
$$

Set

$$
\delta_i(S)=|a_i^\delta(S)|,
\qquad
\sigma_i^\delta(S)=\operatorname{sgn}_\pm a_i^\delta(S),
$$

and, for $S\ne\vn$,

$$
\beta_i(S)=|a_i^\beta(S)|,
\qquad
\sigma_i^\beta(S)=\operatorname{sgn}_\pm a_i^\beta(S).
$$

Use the convention $\beta_i(\vn)=0$. Signs at zero rates are arbitrary.

## Generator calculation

If $i\notin A$, then $\chi_A(\eta^i)=\chi_A(\eta)$. If $i\in A$, then

$$
c_i(\eta)\left(\chi_A(\eta^i)-\chi_A(\eta)\right)
=
c_i^0(\eta)\chi_{A\setminus\{i\}}(\eta)
-
(c_i^0(\eta)+c_i^1(\eta))\chi_A(\eta).
$$

Substituting the monomial expansions gives

$$
\cL\chi_A
=
\sum_{i\in A}\sum_{S\subseteq N(i)}
a_i^\delta(S)\chi_{(A\setminus\{i\})\cup S}
+
\sum_{i\in A}\sum_{S\subseteq N(i)}
a_i^\beta(S)\chi_{A\cup S}.
\tag{1}
$$

Equation (1) is the algebraic input for the signed additive dual.

## Conditional Feynman--Kac formula

Let $Y=(A,\sigma)$ and let $(Y_t)=(A_t,\sigma_t)$ be the [signed additive set process](signed-additive-set-process.md) with the rates and signs above. Put

$$
H(Y,\eta)=\sigma\chi_A(\eta)
$$

and

$$
V(A)=\sum_{i\in A}V_i,
\qquad
V_i=
\sum_{S\subseteq N(i)}\delta_i(S)
+
\sum_{\substack{S\subseteq N(i)\\S\ne\vn}}\beta_i(S)
+a_i^\beta(\vn).
$$

The generator identity obtained from (1) is

$$
\cL_\eta H(Y,\eta)=\cD_YH(Y,\eta)+V(A)H(Y,\eta).
\tag{2}
$$

To pass from (2) to a semigroup identity, assume for the time horizon under consideration that:

- the spin system defines the semigroup $P_t$ on the monomials in question;
- the signed dual is nonexplosive from every finite initial set used in the formula;
- the Feynman--Kac random variable below is integrable; and
- the standard generator-to-Feynman--Kac argument is justified for these two processes, including any finite-to-infinite-volume passage when $\Lambda$ is infinite.

Under these explicit hypotheses,

$$
P_t\chi_A(\eta)
=
\mathbb E_{(A,+)}\left[
\sigma_t\exp\left(\int_0^tV(A_s)\,ds\right)
\chi_{A_t}(\eta)
\right].
\tag{3}
$$

The patchwise refinement of (3) is recorded separately as the conditional [patch representation of spin systems](patch-representation-of-spin-systems.md).
