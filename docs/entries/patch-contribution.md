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

This entry defines the local contribution of a [patch](patch.md) in the monomial [duality](monomial-duality-for-spin-systems.md) representation of a [spin system](spin-system.md). Bulk patches have contribution \(C(P)\). End patches have contribution \(C(\xi,P)\), because they also see the terminal configuration \(\xi\).

Throughout, signs are identified with the numbers \(\pm1\). Fix a patch

$$
P=\{i\}\times[s,t),
\qquad
\nu=t-s.
$$

Assume the signed additive set process comes with the site potential

$$
V(A)=\sum_{i\in A}V_i.
$$

For the source site \(i\), set

$$
d_i=\delta_i(\vn),
\qquad
\varepsilon_i=\sigma_i^\delta(\vn),
$$

and

$$
r_i=
\sum_{S\ne\vn}\left(\delta_i(S)+\beta_i(S)\right),
\qquad
\lambda_i=d_i+r_i.
$$

Here \(d_i\) is the death rate, while \(r_i\) is the total rate of nonempty-target outgoing interactions from an active source. Define

$$
\Phi_i(u)=\int_0^u e^{(V_i-\lambda_i)a}\,da,
$$

and

$$
p_i(u)
=
e^{-\lambda_i u}+d_i\int_0^u e^{-\lambda_i a}\,da.
$$

The quantity \(p_i(u)\) is the probability that, starting active, no forbidden nonempty-target outgoing interaction occurs before time \(u\), allowing a death before \(u\). The corresponding signed Feynman--Kac numerators are

$$
n_i(u)
=
e^{(V_i-\lambda_i)u}+d_i\varepsilon_i\Phi_i(u),
$$

and, for an end patch,

$$
n_i^\xi(u)
=
\xi(i)e^{(V_i-\lambda_i)u}+d_i\varepsilon_i\Phi_i(u).
$$

Thus, for a patch that starts active without an outgoing initial sign,

$$
A_i(u)=\frac{n_i(u)}{p_i(u)},
\qquad
E_i^\xi(u)=\frac{n_i^\xi(u)}{p_i(u)},
\qquad
O_i(u)=e^{V_i u}.
$$

The term \(A_i(u)\) is used for terminal type \(\mathsf I\), \(E_i^\xi(u)\) for terminal type \(\mathsf E\), and \(O_i(u)\) for terminal type \(\mathsf O\). The last formula follows because terminal type \(\mathsf O\) forces the patch to stay active until the terminal outgoing boundary.

## Outgoing initial boundary

If \(\operatorname{type}_-(P)=\mathsf O\), write \(S_-(P)\) for the target set in the initial skeleton \((i,s,S_-(P))\). Conditional on this skeleton, the initial outgoing interaction is a birth with probability

$$
\pi_i^\beta(S)
=
\frac{\beta_i(S)}{\delta_i(S)+\beta_i(S)},
$$

and a split with probability

$$
\pi_i^\delta(S)
=
\frac{\delta_i(S)}{\delta_i(S)+\beta_i(S)}.
$$

The birth sign is \(\sigma_i^\beta(S)\), and the split sign is \(\sigma_i^\delta(S)\). For \(S=S_-(P)\), define

$$
A_i^S(u)
=
\frac{
\pi_i^\beta(S)\sigma_i^\beta(S)n_i(u)
+
\pi_i^\delta(S)\sigma_i^\delta(S)
}{
\pi_i^\beta(S)p_i(u)+\pi_i^\delta(S)
},
$$

and

$$
E_i^{S,\xi}(u)
=
\frac{
\pi_i^\beta(S)\sigma_i^\beta(S)n_i^\xi(u)
+
\pi_i^\delta(S)\sigma_i^\delta(S)
}{
\pi_i^\beta(S)p_i(u)+\pi_i^\delta(S)
}.
$$

For terminal type \(\mathsf O\), consistency forces the initial outgoing interaction to be a birth, so

$$
O_i^S(u)=\sigma_i^\beta(S)e^{V_i u}.
$$

These expressions are understood on skeletons for which the displayed denominators are positive.

## Contribution functions

For a bulk patch \(P\in\mathcal B_T\), define

$$
C(P)=
\begin{cases}
A_i(\nu),
& \operatorname{type}_-(P)\in\{\mathsf S,\mathsf I\},\ \operatorname{type}_+(P)=\mathsf I,\\
O_i(\nu),
& \operatorname{type}_-(P)\in\{\mathsf S,\mathsf I\},\ \operatorname{type}_+(P)=\mathsf O,\\
A_i^{S_-(P)}(\nu),
& \operatorname{type}_-(P)=\mathsf O,\ \operatorname{type}_+(P)=\mathsf I,\\
O_i^{S_-(P)}(\nu),
& \operatorname{type}_-(P)=\mathsf O,\ \operatorname{type}_+(P)=\mathsf O.
\end{cases}
$$

For an end patch \(P\in\mathcal E_T\), define

$$
C(\xi,P)=
\begin{cases}
E_i^\xi(\nu),
& \operatorname{type}_-(P)\in\{\mathsf S,\mathsf I\},\\
E_i^{S_-(P),\xi}(\nu),
& \operatorname{type}_-(P)=\mathsf O.
\end{cases}
$$

Equivalently, \(C(P)\) and \(C(\xi,P)\) are the conditional expectations of the local sign and Feynman--Kac weight under \(\mathbb P_P^{\operatorname{cons}}\), with the additional terminal factor \(\xi(i)\) exactly when the end patch is active at time \(T\).

## Spin-system rate form

For a spin system in the monomial basis, write

$$
c_i^x(\eta)=\sum_{S\subseteq N(i)}c_i^x(S)\chi_S(\eta),
\qquad x\in\{0,1\}.
$$

The dual rates, signs, and site potential are

$$
d_i=|c_i^0(\vn)|,
\qquad
\varepsilon_i=\operatorname{sgn}_\pm c_i^0(\vn),
$$

$$
r_i=
\sum_{S\ne\vn}
\left(
|c_i^0(S)|+|c_i^0(S)+c_i^1(S)|
\right),
$$

and

$$
V_i=
\sum_{S\subseteq N(i)}|c_i^0(S)|
+
\sum_{S\ne\vn}|c_i^0(S)+c_i^1(S)|
-c_i^0(\vn)-c_i^1(\vn).
$$

For \(S\ne\vn\),

$$
\pi_i^\delta(S)
=
\frac{|c_i^0(S)|}{|c_i^0(S)|+|c_i^0(S)+c_i^1(S)|},
$$

$$
\pi_i^\beta(S)
=
\frac{|c_i^0(S)+c_i^1(S)|}{|c_i^0(S)|+|c_i^0(S)+c_i^1(S)|},
$$

with signs

$$
\sigma_i^\delta(S)=\operatorname{sgn}_\pm c_i^0(S),
\qquad
\sigma_i^\beta(S)=\operatorname{sgn}_\pm\left(-c_i^0(S)-c_i^1(S)\right).
$$

Substituting these quantities into the formulas above gives the patch contributions directly in terms of the spin-system rate coefficients \(c_i^0(S)\) and \(c_i^1(S)\).
