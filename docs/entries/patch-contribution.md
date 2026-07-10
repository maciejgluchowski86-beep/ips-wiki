---
title: Patch contribution
status: definition
tags:
  - signed additive set process
  - patch
  - spin systems
  - duality
---

# Patch contribution

This entry gives the local factors \(C(P)\) and \(C(\xi,P)\) used in the [patch representation of spin systems](patch-representation-of-spin-systems.md).

Let

$$
P=\{i\}\times[s_-,s_+),
\qquad
\Delta=s_+-s_-.
$$

Let \(V_i\) be the one-site Feynman--Kac potential and let \(a_i^\beta(\vn)\) be the empty birth coefficient from [monomial duality for spin systems](monomial-duality-for-spin-systems.md). Thus

$$
V_i=\alpha_i+a_i^\beta(\vn),
$$

where

$$
\alpha_i
=
\sum_{S\subseteq N(i)}\delta_i(S)
+
\sum_{\vn\ne S\subseteq N(i)}\beta_i(S).
$$

The combination \(\alpha_i-V_i\) is therefore the already-defined quantity \(-a_i^\beta(\vn)\). Define

$$
\varphi_i(\Delta)
=
e^{-\alpha_i\Delta}
+
\delta_i(\vn)
\int_0^\Delta e^{-\alpha_i s}\,ds,
$$

and, for \(z\in\{0,1\}\),

$$
\psi_i(\Delta,z)
=
z e^{a_i^\beta(\vn)\Delta}
+
\delta_i(\vn)
\int_0^\Delta e^{a_i^\beta(\vn)s}\,ds.
$$

The formulas below are understood on patches for which the displayed denominators are positive.

## Dual-rate form

For a bulk patch with late type \(\mathsf I\),

$$
C(P)
=
\begin{cases}
\dfrac{\psi_i(\Delta,1)}{\varphi_i(\Delta)},
& \operatorname{type}_-(P)\in\{\mathsf S,\mathsf I\},\\[1.2em]
\dfrac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta,1)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
& \operatorname{type}_-(P)=\mathsf O,
\end{cases}
$$

where in the \(\mathsf O\)-initial row, \(S\) is the [initial interaction target](graphical-construction-of-signed-additive-set-process.md#poisson-interaction-sets).

For a bulk patch with late type \(\mathsf O\),

$$
C(P)
=
\begin{cases}
e^{V_i\Delta},
& \operatorname{type}_-(P)\in\{\mathsf S,\mathsf I\},\\[0.8em]
\sigma_i^\beta(S)e^{V_i\Delta},
& \operatorname{type}_-(P)=\mathsf O,
\end{cases}
$$

where in the \(\mathsf O\)-initial row, \(S\) is the initial interaction target.

For an end patch, write \(z=\xi(i)\). Then

$$
C(\xi,P)
=
\begin{cases}
\dfrac{\psi_i(\Delta,z)}{\varphi_i(\Delta)},
& \operatorname{type}_-(P)\in\{\mathsf S,\mathsf I\},\\[1.2em]
\dfrac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta,z)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
& \operatorname{type}_-(P)=\mathsf O,
\end{cases}
$$

where in the \(\mathsf O\)-initial row, \(S\) is the initial interaction target.

## Spin-system rate form

In the spin-rate notation of [monomial duality for spin systems](monomial-duality-for-spin-systems.md),

$$
a_i^\beta(\vn)=-c_i^0(\vn)-c_i^1(\vn),
$$

so

$$
V_i
=
\alpha_i-c_i^0(\vn)-c_i^1(\vn),
$$

with

$$
\alpha_i
=
\sum_{S\subseteq N(i)}|c_i^0(S)|
+
\sum_{\vn\ne S\subseteq N(i)}|c_i^0(S)+c_i^1(S)|.
$$

Thus

$$
\varphi_i(\Delta)
=
e^{-\alpha_i\Delta}
+
|c_i^0(\vn)|
\int_0^\Delta e^{-\alpha_i s}\,ds,
$$

and

$$
\psi_i(\Delta,z)
=
z e^{-(c_i^0(\vn)+c_i^1(\vn))\Delta}
+
|c_i^0(\vn)|
\int_0^\Delta e^{-(c_i^0(\vn)+c_i^1(\vn))s}\,ds.
$$

For nonempty \(S\subseteq N(i)\),

$$
\delta_i(S)\sigma_i^\delta(S)=c_i^0(S),
\qquad
\beta_i(S)\sigma_i^\beta(S)=-c_i^0(S)-c_i^1(S),
$$

and

$$
\delta_i(S)=|c_i^0(S)|,
\qquad
\beta_i(S)=|c_i^0(S)+c_i^1(S)|.
$$

Therefore the \(\mathsf O\)-initial rows become, with \(S\) the initial interaction target,

$$
C(P)
=
\frac{
c_i^0(S)-\left(c_i^0(S)+c_i^1(S)\right)\psi_i(\Delta,1)
}{
|c_i^0(S)|+|c_i^0(S)+c_i^1(S)|\varphi_i(\Delta)
}
\quad\text{if }\operatorname{type}(P)=\mathsf{OI},
$$

$$
C(P)
=
\operatorname{sgn}_\pm\left(-c_i^0(S)-c_i^1(S)\right)e^{V_i\Delta}
\quad\text{if }\operatorname{type}(P)=\mathsf{OO},
$$

and

$$
C(\xi,P)
=
\frac{
c_i^0(S)-\left(c_i^0(S)+c_i^1(S)\right)\psi_i(\Delta,\xi(i))
}{
|c_i^0(S)|+|c_i^0(S)+c_i^1(S)|\varphi_i(\Delta)
}
\quad\text{if }\operatorname{type}(P)=\mathsf{OE}.
$$

The \(\mathsf S\)- and \(\mathsf I\)-initial rows are the corresponding dual-rate formulas above with these \(\varphi_i\), \(\psi_i\), and \(V_i\).
