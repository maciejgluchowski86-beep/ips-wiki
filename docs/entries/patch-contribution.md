---
title: Patch contribution
status: proved here
tags:
  - signed additive set process
  - patch
  - spin systems
  - duality
---

# Patch contribution

Fix a labeled [patch](patch.md) \(P\) and write

$$
i=i(P),
\qquad
s=s(P),
\qquad
e=e(P),
\qquad
S=S(P).
$$

Let \((X_u^P)_{s\le u<e}\) be the local active indicator under the [reference patch measure](patch-consistency-event.md#reference-patch-measure). If \(\mathsf X(P)=\mathsf O\), let \(\alpha_P\in\{\delta,\beta\}\) be the kind of its initial interaction. Set

$$
\sigma_P
=
\begin{cases}
1,
& \mathsf X(P)=\mathsf I,
\\
\sigma_i^{\alpha_P}(S),
& \mathsf X(P)=\mathsf O.
\end{cases}
$$

When a patch is evaluated at \(q\in[s,e]\), use the endpoint convention

$$
X_q^P
=
\begin{cases}
X_s^P, & q=s,\\
X_{q-}^P, & q>s.
\end{cases}
$$

For a finite full patch, define

$$
F(P)
=
\sigma_P
\exp\left(
V_i\int_s^eX_u^P\,du
\right),
\qquad
C(P)
=
\mathbb E_P^{\mathrm{con}}[F(P)].
$$

For \(s\le t\le e\) and \(z\in[0,1]\), define

$$
F_t(z,P)
=
\sigma_P
\exp\left(
V_i\int_s^tX_u^P\,du
\right)
z^{X_t^P},
\qquad
C_t(z,P)
=
\mathbb E_P^{\mathrm{con}}[F_t(z,P)].
$$

If \(P\in\mathcal E_t\), write

$$
C(z,P)=C_t(z,P).
$$

For a configuration \(\xi\) and a one-density profile \(\mathbf p=(p_j)_{j\in\Lambda}\), use

$$
\begin{aligned}
F_t(\xi,P)&=F_t(\xi(i),P),
&
C_t(\xi,P)&=C_t(\xi(i),P),
&
C(\xi,P)&=C(\xi(i),P),
\\
F_t(\mathbf p,P)&=F_t(p_i,P),
&
C_t(\mathbf p,P)&=C_t(p_i,P),
&
C(\mathbf p,P)&=C(p_i,P).
\end{aligned}
$$

All conditional expectations below are understood for patches with \(\mathbb P_P(\operatorname{Con}(P))>0\).

## Dual-rate form

Define

$$
\begin{aligned}
\alpha_i
&=
\sum_{R\subseteq N(i)}\delta_i(R)
+
\sum_{\vn\ne R\subseteq N(i)}\beta_i(R),
\\
V_i&=\alpha_i+a_i^\beta(\vn),
\\
\varphi_i(\Delta)
&=
e^{-\alpha_i\Delta}
+
\delta_i(\vn)\int_0^\Delta e^{-\alpha_i w}\,dw,
\\
\psi_i(\Delta_-,\Delta_+,z)
&=
\delta_i(\vn)\int_0^{\Delta_-} e^{a_i^\beta(\vn)w}\,dw
+
z e^{a_i^\beta(\vn)\Delta_-}\varphi_i(\Delta_+).
\end{aligned}
$$

In particular,

$$
\psi_i(\Delta,z)
=
\psi_i(\Delta,0,z)
=
\delta_i(\vn)\int_0^\Delta e^{a_i^\beta(\vn)w}\,dw
+
z e^{a_i^\beta(\vn)\Delta}.
$$

For \(s\le t\le e\), put

$$
\Delta_-=t-s,
\qquad
\Delta_+=e-t,
\qquad
\Delta=e-s=\Delta_-+\Delta_+.
$$

Then

$$
C_t(z,P)
=
\begin{cases}
\dfrac{\psi_i(\Delta_-,\Delta_+,z)}{\varphi_i(\Delta)},
& \mathsf X(P)=\mathsf I,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.2em]
z e^{V_i\Delta_-},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf O),
\\[1.2em]
\dfrac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta_-,\Delta_+,z)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
& \mathsf X(P)=\mathsf O,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.5em]
\sigma_i^\beta(S)z e^{V_i\Delta_-},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf O).
\end{cases}
\tag{1}
$$

For a finite full patch, \(C(P)=C_e(1,P)\). For an end patch \(P\in\mathcal E_t\), \(C(z,P)=C_t(z,P)\) and \(\Delta_+=0\). Thus (1) contains all completed, end, and full-cut patch contributions. When \(e=\infty\), the terms \(\varphi_i(\Delta_+)\) and \(\varphi_i(\Delta)\) mean their limits at infinity.

## Spin-system rate form

In the coefficient notation of [monomial duality for spin systems](monomial-duality-for-spin-systems.md),

$$
\begin{aligned}
\alpha_i
&=
\sum_{R\subseteq N(i)}|c_i^0(R)|
+
\sum_{\vn\ne R\subseteq N(i)}|c_i^0(R)+c_i^1(R)|,
\\
V_i
&=
\alpha_i-c_i^0(\vn)-c_i^1(\vn),
\\
\varphi_i(\Delta)
&=
e^{-\alpha_i\Delta}
+
|c_i^0(\vn)|\int_0^\Delta e^{-\alpha_i w}\,dw,
\\
\psi_i(\Delta_-,\Delta_+,z)
&=
|c_i^0(\vn)|
\int_0^{\Delta_-} e^{-(c_i^0(\vn)+c_i^1(\vn))w}\,dw
\\
&\qquad+
z e^{-(c_i^0(\vn)+c_i^1(\vn))\Delta_-}\varphi_i(\Delta_+).
\end{aligned}
$$

With \(\Delta_-,\Delta_+,\Delta\) as above,

$$
C_t(z,P)
=
\begin{cases}
\dfrac{\psi_i(\Delta_-,\Delta_+,z)}{\varphi_i(\Delta)},
& \mathsf X(P)=\mathsf I,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.2em]
z e^{V_i\Delta_-},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf O),
\\[1.2em]
\dfrac{
c_i^0(S)
-
(c_i^0(S)+c_i^1(S))\psi_i(\Delta_-,\Delta_+,z)
}{
|c_i^0(S)|
+
|c_i^0(S)+c_i^1(S)|\varphi_i(\Delta)
},
& \mathsf X(P)=\mathsf O,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.5em]
\operatorname{sgn}_\pm\bigl(-c_i^0(S)-c_i^1(S)\bigr)
z e^{V_i\Delta_-},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf O).
\end{cases}
\tag{2}
$$

Again, \(C(P)=C_e(1,P)\) for a finite full patch and \(C(z,P)=C_t(z,P)\) for \(P\in\mathcal E_t\).

## Calculation

Suppose first that the patch starts active and \(\mathsf Y(P)\in\{\mathsf I,\mathsf E\}\). Consistency occurs either when no outgoing interaction occurs before time \(e\), or when the first outgoing interaction is a pure death. Hence

$$
\mathbb P_P(\operatorname{Con}(P))
=
e^{-\alpha_i\Delta}
+
\delta_i(\vn)\int_0^\Delta e^{-\alpha_i w}\,dw
=
\varphi_i(\Delta).
\tag{3}
$$

Splitting according to whether the pure death occurs before or after time \(t\) gives

$$
\begin{aligned}
\mathbb E_P\left[
\ind(\operatorname{Con}(P))
\exp\left(
V_i\int_s^tX_u^P\,du
\right)
z^{X_t^P}
\right]
&=
\delta_i(\vn)
\int_0^{\Delta_-} e^{(V_i-\alpha_i)w}\,dw
\\
&\quad+
z e^{(V_i-\alpha_i)\Delta_-}
\left[
e^{-\alpha_i\Delta_+}
+
\delta_i(\vn)\int_0^{\Delta_+} e^{-\alpha_i w}\,dw
\right]
\\
&=
\delta_i(\vn)
\int_0^{\Delta_-} e^{a_i^\beta(\vn)w}\,dw
+
z e^{a_i^\beta(\vn)\Delta_-}\varphi_i(\Delta_+)
\\
&=
\psi_i(\Delta_-,\Delta_+,z).
\end{aligned}
\tag{4}
$$

Dividing (4) by (3) gives the first row of (1).

Suppose next that \(\mathsf X(P)=\mathsf O\) and \(\mathsf Y(P)\in\{\mathsf I,\mathsf E\}\). The initial interaction is a split or birth with probabilities proportional to \(\delta_i(S)\) and \(\beta_i(S)\). A split makes the source inactive immediately, while a birth leaves it active. Therefore

$$
\mathbb P_P(\operatorname{Con}(P))
=
\frac{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
}{
\delta_i(S)+\beta_i(S)
},
\tag{5}
$$

and

$$
\mathbb E_P\left[
\ind(\operatorname{Con}(P))F_t(z,P)
\right]
=
\frac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta_-,\Delta_+,z)
}{
\delta_i(S)+\beta_i(S)
}.
\tag{6}
$$

Dividing (6) by (5) gives the third row of (1).

Finally, if \(\mathsf Y(P)=\mathsf O\), consistency forces the source to remain active throughout the patch. If also \(\mathsf X(P)=\mathsf O\), it forces \(\alpha_P=\beta\). Consequently,

$$
C_t(z,P)
=
\begin{cases}
z e^{V_i\Delta_-},
& \mathsf X(P)=\mathsf I,
\\
\sigma_i^\beta(S)z e^{V_i\Delta_-},
& \mathsf X(P)=\mathsf O,
\end{cases}
$$

which gives the second and fourth rows of (1).

The identities

$$
\begin{aligned}
\delta_i(S)\sigma_i^\delta(S)&=c_i^0(S),
&
\delta_i(S)&=|c_i^0(S)|,
\\
\beta_i(S)\sigma_i^\beta(S)&=-c_i^0(S)-c_i^1(S),
&
\beta_i(S)&=|c_i^0(S)+c_i^1(S)|
\end{aligned}
$$

transform (1) into (2).
