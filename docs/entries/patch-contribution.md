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

This entry defines and computes the local factors used in the [patch representation of spin systems](patch-representation-of-spin-systems.md). The unaveraged factors are \(F(P)\) and \(F_t(\xi,P)\). Completed patches have contributions \(C(P)\), finite-horizon end patches have contributions \(C(\xi,P)\), and full patches cut by the evaluation time have contributions \(C_t(\xi,P)\).

Fix a labeled [patch](patch.md) \(P\) and write

$$
i=i(P),
\qquad
s=s(P),
\qquad
e=e(P),
\qquad
S=S(P),
\qquad
\Delta=e-s.
$$

Let \((X_u^P)_{s\le u<e}\) be the local active indicator under the [reference patch measure](patch-consistency-event.md#reference-patch-measure). If \(\mathsf X(P)=\mathsf O\), let \(\alpha_P\in\{\delta,\beta\}\) be the kind of the initial outgoing interaction in \(\Sigma_P\). Define its sign contribution by

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

Here \(\sigma_i^{\alpha_P}(S)=\sigma_i^\delta(S)\) when \(\alpha_P=\delta\), and \(\sigma_i^{\alpha_P}(S)=\sigma_i^\beta(S)\) when \(\alpha_P=\beta\).

When a patch is evaluated at a time \(v\) with \(s\le v\le e\), use the endpoint convention

$$
X_v^P
=
\begin{cases}
X_s^P, & v=s,\\
X_{v-}^P, & v>s.
\end{cases}
$$

Thus a zero-length patch is evaluated in the state created by its initial interaction.

Let \(V_i\) be the one-site Feynman--Kac potential and let \(a_i^\beta(\vn)\) be the empty birth coefficient from [monomial duality for spin systems](monomial-duality-for-spin-systems.md). Set

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
\varphi_i(u)
&=
e^{-\alpha_i u}
+
\delta_i(\vn)
\int_0^u e^{-\alpha_i v}\,dv,
\\
\psi_i(u,z)
&=
z e^{a_i^\beta(\vn)u}
+
\delta_i(\vn)
\int_0^u e^{a_i^\beta(\vn)v}\,dv,
\qquad z\in[0,1].
\end{aligned}
$$

The cancellation

$$
V_i-\alpha_i=a_i^\beta(\vn)
$$

will be used below. All conditional expectations are understood for patches with \(\mathbb P_P(\operatorname{Con}(P))>0\).

## Unaveraged patch factors

For a finite full patch, define

$$
F(P)
=
\sigma_P
\exp\left(
V_i\int_s^e X_u^P\,du
\right).
$$

When \(s\le t\le e\), define, for \(z\in[0,1]\),

$$
F_t(z,P)
=
\sigma_P
\exp\left(
V_i\int_s^t X_u^P\,du
\right)
z^{X_t^P}.
$$

For a configuration \(\xi\) and a one-density profile \(\mathbf p=(p_j)_{j\in\Lambda}\), write

$$
F_t(\xi,P)=F_t(\xi(i),P),
\qquad
F_t(\mathbf p,P)=F_t(p_i,P).
$$

## Dual-rate form

### Completed patches

Let \(P\) be a finite full patch, equivalently a patch with \(\mathsf Y(P)\in\{\mathsf I,\mathsf O\}\). Its contribution is

$$
C(P)
=
\mathbb E_P^{\mathrm{con}}[F(P)].
$$

It is given explicitly by

$$
C(P)
=
\begin{cases}
\dfrac{\psi_i(\Delta,1)}{\varphi_i(\Delta)},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf I),
\\[1.2em]
e^{V_i\Delta},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf O),
\\[1.2em]
\dfrac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta,1)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf I),
\\[1.4em]
\sigma_i^\beta(S)e^{V_i\Delta},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf O).
\end{cases}
\tag{1}
$$

### Affine extension for end patches

Let \(P\in\mathcal E_t\). Then \(e(P)=t\) and \(\mathsf Y(P)=\mathsf E\). For \(z\in[0,1]\), define

$$
C(z,P)
=
\mathbb E_P^{\mathrm{con}}[F_t(z,P)].
$$

with the convention \(z^0=1\). For a configuration \(\xi\) and a one-density profile \(\mathbf p=(p_j)_{j\in\Lambda}\), write

$$
C(\xi,P)=C(\xi(i),P),
\qquad
C(\mathbf p,P)=C(p_i,P).
$$

The explicit formulas are

$$
C(z,P)
=
\begin{cases}
\dfrac{\psi_i(\Delta,z)}{\varphi_i(\Delta)},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf E),
\\[1.2em]
\dfrac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta,z)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf E).
\end{cases}
\tag{2}
$$

Thus the end contribution is affine in \(z\). The [patch critical density](patch-critical-density.md) is the smallest one-density profile for which all the factors \(C(\mathbf p,P)\) are nonnegative.

### Full patches cut by the evaluation time

Let \(P\in\mathcal C_t\), so that

$$
s\le t<e.
$$

For \(z\in[0,1]\), define the contribution conditioned on the full patch by

$$
C_t(z,P)
=
\mathbb E_P^{\mathrm{con}}[F_t(z,P)].
$$

For a configuration \(\xi\) and a one-density profile \(\mathbf p\), write

$$
C_t(\xi,P)=C_t(\xi(i),P),
\qquad
C_t(\mathbf p,P)=C_t(p_i,P).
$$

Put

$$
\ell=t-s,
\qquad
r=e-t,
\qquad
\Delta=e-s.
$$

Then

$$
C_t(z,P)
=
\begin{cases}
\dfrac{
\delta_i(\vn)\displaystyle\int_0^\ell
e^{a_i^\beta(\vn)u}\,du
+
z e^{a_i^\beta(\vn)\ell}\varphi_i(r)
}{
\varphi_i(\Delta)
},
& \mathsf X(P)=\mathsf I,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.5em]
z e^{V_i\ell},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf O),
\\[1.2em]
\dfrac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)
\left[
\delta_i(\vn)\displaystyle\int_0^\ell
e^{a_i^\beta(\vn)u}\,du
+
z e^{a_i^\beta(\vn)\ell}\varphi_i(r)
\right]
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
& \mathsf X(P)=\mathsf O,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.8em]
\sigma_i^\beta(S)z e^{V_i\ell},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf O).
\end{cases}
\tag{3}
$$

When \(e=\infty\), the occurrences of \(\varphi_i(r)\) and \(\varphi_i(\Delta)\) in (3) mean their limits at infinity. Notice that \(C_t(z,P)\) uses the full consistent law \(\mathbb P_P^{\mathrm{con}}\), whereas \(C(z,P^{(t)})\) uses \(\mathbb P_{P^{(t)}}^{\mathrm{con}}\). They need not be equal: the former also conditions on the actual terminal time and terminal label of the full patch.

## Calculation

Suppose first that the patch starts active. If its terminal label is \(\mathsf I\) or \(\mathsf E\), consistency occurs either when no outgoing interaction occurs before the end of the patch, or when the first outgoing interaction is a pure death. Consequently,

$$
\mathbb P_P(\operatorname{Con}(P))
=
e^{-\alpha_i\Delta}
+
\delta_i(\vn)\int_0^\Delta e^{-\alpha_i u}\,du
=
\varphi_i(\Delta).
\tag{4}
$$

For a finite-horizon end patch, splitting according to whether the pure death occurs before time \(u=\Delta\) gives

$$
\begin{aligned}
&\mathbb E_P\left[
\ind(\operatorname{Con}(P))
\exp\left(
V_i\int_s^eX_u^P\,du
\right)
z^{X_e^P}
\right]
\\
&\qquad=
z e^{(V_i-\alpha_i)\Delta}
+
\delta_i(\vn)
\int_0^\Delta e^{(V_i-\alpha_i)u}\,du
\\
&\qquad=
z e^{a_i^\beta(\vn)\Delta}
+
\delta_i(\vn)
\int_0^\Delta e^{a_i^\beta(\vn)u}\,du
\\
&\qquad=
\psi_i(\Delta,z).
\end{aligned}
\tag{5}
$$

For a full patch cut at \(t\), the same decomposition gives

$$
\begin{aligned}
&\mathbb E_P\left[
\ind(\operatorname{Con}(P))
\exp\left(
V_i\int_s^tX_u^P\,du
\right)
z^{X_t^P}
\right]
\\
&\qquad=
\delta_i(\vn)
\int_0^\ell e^{(V_i-\alpha_i)u}\,du
+
z e^{(V_i-\alpha_i)\ell}
\left[
e^{-\alpha_i r}
+
\delta_i(\vn)\int_0^r e^{-\alpha_i u}\,du
\right]
\\
&\qquad=
\delta_i(\vn)
\int_0^\ell e^{a_i^\beta(\vn)u}\,du
+
z e^{a_i^\beta(\vn)\ell}\varphi_i(r).
\end{aligned}
\tag{6}
$$

Dividing (5) or (6) by (4) gives the \(\mathsf I\)-initial rows with terminal label \(\mathsf I\) or \(\mathsf E\).

If the patch starts with an outgoing interaction of target \(S\), then under \(\mathbb P_P\) its initial kind is split or birth with probabilities proportional to \(\delta_i(S)\) and \(\beta_i(S)\). A split makes the source inactive immediately, while a birth leaves it active. Therefore, for terminal label \(\mathsf I\) or \(\mathsf E\),

$$
\mathbb P_P(\operatorname{Con}(P))
=
\frac{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
}{
\delta_i(S)+\beta_i(S)
}.
\tag{7}
$$

For an end patch, the corresponding signed numerator is

$$
\begin{aligned}
&\mathbb E_P\left[
\ind(\operatorname{Con}(P))
\sigma_P
\exp\left(
V_i\int_s^eX_u^P\,du
\right)
z^{X_e^P}
\right]
\\
&\qquad=
\frac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta,z)
}{
\delta_i(S)+\beta_i(S)
}.
\end{aligned}
\tag{8}
$$

For a full patch cut at \(t\), it is

$$
\begin{aligned}
&\mathbb E_P\left[
\ind(\operatorname{Con}(P))
\sigma_P
\exp\left(
V_i\int_s^tX_u^P\,du
\right)
z^{X_t^P}
\right]
\\
&\qquad=
\frac{1}{\delta_i(S)+\beta_i(S)}
\Bigg\{
\delta_i(S)\sigma_i^\delta(S)
\\
&\qquad\qquad+
\beta_i(S)\sigma_i^\beta(S)
\left[
\delta_i(\vn)
\int_0^\ell e^{a_i^\beta(\vn)u}\,du
+
z e^{a_i^\beta(\vn)\ell}\varphi_i(r)
\right]
\Bigg\}.
\end{aligned}
\tag{9}
$$

Dividing (8) or (9) by (7) gives the corresponding \(\mathsf O\)-initial rows.

Finally, if \(\mathsf Y(P)=\mathsf O\), consistency forces the source to stay active throughout the patch. If \(\mathsf X(P)=\mathsf O\), it also forces \(\alpha_P=\beta\). Hence

$$
\begin{aligned}
\mathbb E_P^{\mathrm{con}}\left[
\exp\left(V_i\int_s^eX_u^P\,du\right)
\right]
&=e^{V_i\Delta},
\\
\mathbb E_P^{\mathrm{con}}\left[
\exp\left(V_i\int_s^tX_u^P\,du\right)
z^{X_t^P}
\right]
&=z e^{V_i\ell},
\\
\mathbb E_P^{\mathrm{con}}[\sigma_P]
&=
\begin{cases}
1,&\mathsf X(P)=\mathsf I,\\
\sigma_i^\beta(S),&\mathsf X(P)=\mathsf O.
\end{cases}
\end{aligned}
\tag{10}
$$

This proves (1)--(3).

## Contributions of full patches

Suppose that \(P\) is an infinite full patch. Whenever \(C_t(z,P)\) has a common finite limit independent of \(z\in[0,1]\), define

$$
C(P)
=
\lim_{t\to\infty}C_t(z,P).
$$

Under the uniform pure-death assumption used in [the common invariant-limit theorem](common-invariant-limit-under-uniform-pure-deaths.md),

$$
c_i^1(\xi)\ge\varepsilon>0
\qquad
\text{for every }\xi
$$

implies

$$
a_i^\beta(\vn)
=
-c_i^0(\vn)-c_i^1(\vn)
\le-\varepsilon.
$$

Every dependence on \(z\) in (3) is therefore multiplied by

$$
e^{a_i^\beta(\vn)(t-s)},
$$

which converges to zero exponentially. Thus the limiting contribution is well defined for every infinite patch carrying positive consistent probability. Quantitative comparison estimates for these limits belong to the proof of the common invariant-limit theorem.

## Spin-system rate form

In the spin-rate notation of [monomial duality for spin systems](monomial-duality-for-spin-systems.md),

$$
\begin{aligned}
a_i^\beta(\vn)&=-c_i^0(\vn)-c_i^1(\vn),
\\
\alpha_i
&=
\sum_{R\subseteq N(i)}|c_i^0(R)|
+
\sum_{\vn\ne R\subseteq N(i)}|c_i^0(R)+c_i^1(R)|,
\\
V_i&=\alpha_i-c_i^0(\vn)-c_i^1(\vn),
\\
\varphi_i(u)
&=
e^{-\alpha_i u}
+
|c_i^0(\vn)|
\int_0^u e^{-\alpha_i v}\,dv,
\\
\psi_i(u,z)
&=
z e^{-(c_i^0(\vn)+c_i^1(\vn))u}
+
|c_i^0(\vn)|
\int_0^u e^{-(c_i^0(\vn)+c_i^1(\vn))v}\,dv.
\end{aligned}
$$

For every nonempty \(S\subseteq N(i)\),

$$
\begin{aligned}
\delta_i(S)\sigma_i^\delta(S)&=c_i^0(S),
&
\delta_i(S)&=|c_i^0(S)|,
\\
\beta_i(S)\sigma_i^\beta(S)&=-c_i^0(S)-c_i^1(S),
&
\beta_i(S)&=|c_i^0(S)+c_i^1(S)|.
\end{aligned}
$$

Substituting these identities into (1)--(3) gives the spin-system rate form of every patch contribution.
