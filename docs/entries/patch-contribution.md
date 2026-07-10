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

Write \(v_i\) for the site potential of the signed dual, and set

$$
\alpha_i
=
\sum_{S\subseteq N(i)}\delta_i(S)
+
\sum_{\vn\ne S\subseteq N(i)}\beta_i(S).
$$

Define

$$
\phi_i(\Delta)
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
z e^{-(\alpha_i-v_i)\Delta}
+
\delta_i(\vn)
\int_0^\Delta e^{-(\alpha_i-v_i)s}\,ds.
$$

The formulas below are understood on patches for which the displayed denominators are positive.

## Dual-rate form

If the early type is \(\mathsf S\) or \(\mathsf I\), then

$$
C(P)=
\begin{cases}
\dfrac{\psi_i(\Delta,1)}{\phi_i(\Delta)},
& \operatorname{type}(P)\in\{\mathsf{SI},\mathsf{II}\},\\[1.2em]
e^{v_i\Delta},
& \operatorname{type}(P)\in\{\mathsf{SO},\mathsf{IO}\}.
\end{cases}
$$

If the early type is \(\mathsf O\), let \(S_-(P)\) be the target set in the initial skeleton. Then

$$
C(P)=
\begin{cases}
\dfrac{
\delta_i(S_-(P))\sigma_i^\delta(S_-(P))
+
\beta_i(S_-(P))\sigma_i^\beta(S_-(P))\psi_i(\Delta,1)
}{
\delta_i(S_-(P))+eta_i(S_-(P))\phi_i(\Delta)
},
& \operatorname{type}(P)=\mathsf{OI},\\[1.4em]
\sigma_i^\beta(S_-(P))e^{v_i\Delta},
& \operatorname{type}(P)=\mathsf{OO}.
\end{cases}
$$

For an end patch, write \(z=\xi(i)\). If the early type is \(\mathsf S\) or \(\mathsf I\), then

$$
C(\xi,P)
=
\frac{\psi_i(\Delta,z)}{\phi_i(\Delta)}.
$$

If the early type is \(\mathsf O\), then

$$
C(\xi,P)
=
\frac{
\delta_i(S_-(P))\sigma_i^\delta(S_-(P))
+
\beta_i(S_-(P))\sigma_i^\beta(S_-(P))\psi_i(\Delta,z)
}{
\delta_i(S_-(P))+eta_i(S_-(P))\phi_i(\Delta)
}.
$$

## Spin-system rate form

Let \(c_i^0(S)\) and \(c_i^1(S)\) be the monomial coefficients used in [monomial duality for spin systems](monomial-duality-for-spin-systems.md). Set

$$
a_i(S)=c_i^0(S),
\qquad
b_i(S)=-c_i^0(S)-c_i^1(S).
$$

Then

$$
\delta_i(S)=|a_i(S)|,
\qquad
\sigma_i^\delta(S)=\operatorname{sgn}_\pm a_i(S),
$$

and, for \(S\ne\vn\),

$$
\beta_i(S)=|b_i(S)|,
\qquad
\sigma_i^\beta(S)=\operatorname{sgn}_\pm b_i(S).
$$

Moreover

$$
\alpha_i
=
\sum_{S\subseteq N(i)}|c_i^0(S)|
+
\sum_{\vn\ne S\subseteq N(i)}|c_i^0(S)+c_i^1(S)|,
$$

and

$$
v_i
=
\alpha_i-c_i^0(\vn)-c_i^1(\vn).
$$

Therefore

$$
\phi_i(\Delta)
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
z e^{-(\alpha_i-v_i)\Delta}
+
|c_i^0(\vn)|
\int_0^\Delta e^{-(\alpha_i-v_i)s}\,ds.
$$

The only rows involving nonempty \(S_-(P)\) become, for \(S=S_-(P)\),

$$
C_{\mathsf{OI}}(P)
=
\frac{
c_i^0(S)-\left(c_i^0(S)+c_i^1(S)\right)\psi_i(\Delta,1)
}{
|c_i^0(S)|+|c_i^0(S)+c_i^1(S)|\phi_i(\Delta)
},
$$

$$
C_{\mathsf{OO}}(P)
=
\operatorname{sgn}_\pm\left(-c_i^0(S)-c_i^1(S)\right)e^{v_i\Delta},
$$

and

$$
C_{\mathsf{OE}}(\xi,P)
=
\frac{
c_i^0(S)-\left(c_i^0(S)+c_i^1(S)\right)\psi_i(\Delta,\xi(i))
}{
|c_i^0(S)|+|c_i^0(S)+c_i^1(S)|\phi_i(\Delta)
}.
$$

The remaining rows are the same formulas from the dual-rate form with the displayed \(\phi_i\), \(\psi_i\), and \(v_i\).
