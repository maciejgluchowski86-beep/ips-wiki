---
title: Monomial duality for spin systems
status: proved here
tags:
  - duality
  - spin systems
  - monomials
---

# Monomial duality for spin systems

This entry gives the finite-set [duality](duality.md) for a [spin system](spin-system.md) in the ordinary [monomial](monomials.md) basis

$$
\chi_A(\eta)=\prod_{i\in A}\eta(i).
$$

The dual process is a [signed additive set process](signed-additive-set-process.md). Variants with deformed basis functions use the same algebraic philosophy as [theta monomials](theta-monomials.md), while perturbative comparison arguments can use the [duality noise lemma](duality-noise-lemma.md). The patchwise refinement of this formula is separated into [patch factorization](patch-factorization.md), [patch contribution](patch-contribution.md), and the [patch representation of spin systems](patch-representation-of-spin-systems.md).

## Rate coefficients

Let

$$
\cL f(\eta)=\sum_{i\in\Lambda}c_i(\eta)\left(f(\eta^i)-f(\eta)\right).
$$

Write

$$
c_i(\eta)=(1-\eta(i))c_i^0(\eta)+\eta(i)c_i^1(\eta),
$$

where \(c_i^x(\eta)=c_i(\eta^{i,x})\). The functions \(c_i^0\) and \(c_i^1\) depend only on the neighbour set \(N(i)\) from the [lattice and graph](lattice-and-graph.md) convention. Their monomial expansions are

$$
c_i^x(\eta)=\sum_{S\subseteq N(i)}c_i^x(S)\chi_S(\eta),
\qquad x\in\{0,1\}.
$$

Define the signed coefficients

$$
a_i^\delta(S)=c_i^0(S),
\qquad
a_i^\beta(S)=-c_i^0(S)-c_i^1(S).
$$

The associated nonnegative death and split rates and signs are

$$
\delta_i(S)=|a_i^\delta(S)|,
\qquad
\sigma_i^\delta(S)=\operatorname{sgn}_\pm a_i^\delta(S).
$$

For births use the convention \(\beta_i(\vn)=0\). For \(S\ne\vn\), set

$$
\beta_i(S)=|a_i^\beta(S)|,
\qquad
\sigma_i^\beta(S)=\operatorname{sgn}_\pm a_i^\beta(S).
$$

Here \(\operatorname{sgn}_\pm x\) is \(+\) for \(x>0\) and \(-\) for \(x<0\). Signs at zero rates are arbitrary.

## Generator action

For \(A\Subset\Lambda\),

$$
\cL\chi_A
=
\sum_{i\in A}\sum_{S\subseteq N(i)}
a_i^\delta(S)\chi_{(A\setminus\{i\})\cup S}
+
\sum_{i\in A}\sum_{S\subseteq N(i)}
a_i^\beta(S)\chi_{A\cup S}.
$$

Thus the only dual updates are activations of subsets of neighbouring sites. The \(\delta\)-update is a death when \(S=\vn\) and a split when \(S\ne\vn\). The \(\beta\)-update is a birth when \(S\ne\vn\). The empty birth term is not a dual update and is absorbed into the Feynman--Kac potential.

## Dual process

Let \(Y=(A,\sigma)\), and let \((Y_t)=(A_t,\sigma_t)\) be the signed additive set process with rates \(\delta_i(S)\), \(\beta_i(S)\), signs \(\sigma_i^\delta(S)\), \(\sigma_i^\beta(S)\), and update maps \(D_{i,S}\), \(B_{i,S}\). Its duality function is

$$
H(Y,\eta)=\sigma\chi_A(\eta),
$$

where the sign \(\sigma\in\{+,-\}\) acts on the real number \(\chi_A(\eta)\).

The Feynman--Kac potential depends only on \(A\). Write

$$
V(A)=\sum_{i\in A}V_i,
\qquad
V_i=
\sum_{S\subseteq N(i)}\delta_i(S)
+
\sum_{\substack{S\subseteq N(i)\\ S\ne\vn}}\beta_i(S)
+a_i^\beta(\vn).
$$

The generator of the dual process acts on the first coordinate of \(H\) by

$$
\begin{aligned}
\cD H(Y,\eta)
={}&
\sum_{i\in A}\sum_{S\subseteq N(i)}\delta_i(S)
\left(H(D_{i,S}Y,\eta)-H(Y,\eta)\right)\\
&+
\sum_{i\in A}\sum_{\substack{S\subseteq N(i)\\ S\ne\vn}}\beta_i(S)
\left(H(B_{i,S}Y,\eta)-H(Y,\eta)\right).
\end{aligned}
$$

The resulting Feynman--Kac duality identity is

$$
\cL_\eta H(Y,\eta)
=
\cD H(Y,\eta)+V(A)H(Y,\eta),
$$

so

$$
\E_\eta[\chi_A(\eta_t)]
=
\E_{(A,+)}\left[
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
