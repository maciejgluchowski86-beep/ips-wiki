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

This entry gives the local factors \(C(P)\) and \(C(\xi,P)\) used in the [patch representation of spin systems](patch-representation-of-spin-systems.md). A finite full patch has a contribution \(C(P)\), while a patch truncated at a time horizon has a terminal contribution depending on the configuration or its one-density profile. The [patch positivity property](patch-positivity-property.md) gives a coefficient criterion under which all finite-patch factors are nonnegative, while the [patch critical density](patch-critical-density.md) determines when the affine terminal factors are nonnegative.

Let

$$
P=\{i\}\times[s_-,s_+),
\qquad
\Delta=s_+-s_-.
$$

Let \(V_i\) be the one-site Feynman--Kac potential and let \(a_i^\beta(\vn)\) be the empty birth coefficient from [monomial duality for spin systems](monomial-duality-for-spin-systems.md). Define

$$
\begin{aligned}
\alpha_i
&=
\sum_{S\subseteq N(i)}\delta_i(S)
+
\sum_{\vn\ne S\subseteq N(i)}\beta_i(S),
\\
V_i&=\alpha_i+a_i^\beta(\vn),
\\
\varphi_i(\Delta)
&=
e^{-\alpha_i\Delta}
+
\delta_i(\vn)
\int_0^\Delta e^{-\alpha_i s}\,ds,
\\
\psi_i(\Delta,z)
&=
z e^{a_i^\beta(\vn)\Delta}
+
\delta_i(\vn)
\int_0^\Delta e^{a_i^\beta(\vn)s}\,ds,
\qquad z\in\{0,1\}.
\end{aligned}
$$

The identity \(\alpha_i-V_i=-a_i^\beta(\vn)\) is the cancellation used in the definition of \(\psi_i\). The formulas below are understood on patches for which the displayed denominators are positive. In the \(\mathsf O\)-initial rows, \(S\) is the [initial interaction target](graphical-construction-of-signed-additive-set-process.md#poisson-interaction-sets).

## Dual-rate form

For a bulk patch \(P\in\mathcal B_T\), the contribution is

$$
C(P)
=
\begin{cases}
\dfrac{\psi_i(\Delta,1)}{\varphi_i(\Delta)},
& \operatorname{type}(P)\in\{\mathsf{SI},\mathsf{II}\},\\[1.2em]
e^{V_i\Delta},
& \operatorname{type}(P)\in\{\mathsf{SO},\mathsf{IO}\},\\[1.2em]
\dfrac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta,1)
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
& \operatorname{type}(P)=\mathsf{OI},\\[1.4em]
\sigma_i^\beta(S)e^{V_i\Delta},
& \operatorname{type}(P)=\mathsf{OO}.
\end{cases}
$$

For an end patch \(P\in\mathcal E_T\), the contribution is

$$
C(\xi,P)
=
\begin{cases}
\dfrac{\psi_i(\Delta,\xi(i))}{\varphi_i(\Delta)},
& \operatorname{type}(P)\in\{\mathsf{SE},\mathsf{IE}\},\\[1.2em]
\dfrac{
\delta_i(S)\sigma_i^\delta(S)
+
\beta_i(S)\sigma_i^\beta(S)\psi_i(\Delta,\xi(i))
}{
\delta_i(S)+\beta_i(S)\varphi_i(\Delta)
},
& \operatorname{type}(P)=\mathsf{OE}.
\end{cases}
$$

## Affine extension for end patches

Let \(P\in\mathcal E_T\) be an end patch based at \(i\). Its contribution depends on the terminal configuration only through \(\xi(i)\), and is affine in that variable. For \(p\in[0,1]\), define

$$
C^p(P)
=
(1-p)C(0,P)+pC(1,P).
$$

Equivalently, \(C^p(P)\) is obtained from the end-patch formula by replacing \(\xi(i)\) with \(p\). For a one-density profile \(\mathbf p=(p_i)_{i\in\Lambda}\), write

$$
C^{\mathbf p}(P)=C^{p_i}(P)
$$

when \(P\) is based at \(i\). The [patch critical density](patch-critical-density.md) is the smallest profile for which these affine end contributions are nonnegative.

## Contributions of full patches

Let \(\mathcal P\) be the full patch family from the [patch](patch.md) entry. If \(P\in\mathcal P\) is finite, its contribution \(C(P)\) is the corresponding bulk contribution in the dual-rate display above.

Suppose that \(P=\{i\}\times[s,\infty)\) is infinite. When the terminal contributions of its truncations have a common finite limit independent of the terminal density, define

$$
C(P)
=
\lim_{T\to\infty}C^p(P^{(T)}).
$$

This definition applies almost surely to the infinite patches occurring under the uniform pure-death assumption used in [monomial convergence under uniform pure deaths](monomial-convergence-under-uniform-pure-deaths.md). Indeed,

$$
c_i^1(\xi)\ge\varepsilon>0
\qquad\text{for every }\xi
$$

implies

$$
c_i^0(\vn)+c_i^1(\vn)\ge\varepsilon.
$$

In the end-patch formulas before the consistency normalization is cancelled against the skeleton weight, all dependence on \(p\) is carried by

$$
p\,e^{-(c_i^0(\vn)+c_i^1(\vn))\Delta},
$$

so it disappears as \(\Delta\to\infty\). The same conclusion holds for the normalized contribution whenever the infinite patch has positive skeleton weight; zero-weight exceptional patches do not affect the representation. The remaining limit is the same for every \(p\in[0,1]\). Under patch positivity it is nonnegative.

## Spin-system rate form

In the spin-rate notation of [monomial duality for spin systems](monomial-duality-for-spin-systems.md), the quantities in the preceding display are

$$
\begin{aligned}
a_i^\beta(\vn)&=-c_i^0(\vn)-c_i^1(\vn),
\\
\alpha_i
&=
\sum_{S\subseteq N(i)}|c_i^0(S)|
+
\sum_{\vn\ne S\subseteq N(i)}|c_i^0(S)+c_i^1(S)|,
\\
V_i&=\alpha_i-c_i^0(\vn)-c_i^1(\vn),
\\
\varphi_i(\Delta)
&=
e^{-\alpha_i\Delta}
+
|c_i^0(\vn)|
\int_0^\Delta e^{-\alpha_i s}\,ds,
\\
\psi_i(\Delta,z)
&=
z e^{-(c_i^0(\vn)+c_i^1(\vn))\Delta}
+
|c_i^0(\vn)|
\int_0^\Delta e^{-(c_i^0(\vn)+c_i^1(\vn))s}\,ds.
\end{aligned}
$$

For nonempty \(S\subseteq N(i)\), the signed rates appearing in the \(\mathsf O\)-initial rows are

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

Substituting these identities into the two contribution displays gives the spin-system rate form.
