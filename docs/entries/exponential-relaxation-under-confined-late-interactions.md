---
title: Exponential relaxation under confined late interactions
status: proved here
tags:
  - patch
  - ergodicity
  - spin systems
  - convergence to equilibrium
---

# Exponential relaxation under confined late interactions

The modified spin system from [undoing duality under confined late interactions](undoing-duality-under-confined-late-interactions.md) is the product of a zero-boundary process on \(R\) and independent two-state chains on \(R^c\). Exponential mixing of these components therefore gives exponential convergence of the confined patch term.

## Assumptions

For \(R\Subset\Lambda\), let \(\cL_R^0\) be the zero-boundary restriction of the original spin system to \(R\). Assume that \(\cL_R^0\) has a unique invariant measure \(\nu_R\), and that it admits a coupling with its stationary process satisfying

$$
\sup_{\eta\in\{0,1\}^R}
\mathbb P
\left(
\eta_s\ne\widetilde\eta_s
\right)
\le
C_1e^{-\gamma_1s},
\tag{1}
$$

where \(C_1<\infty\) and \(\gamma_1>0\) are independent of \(R\).

Set

$$
\gamma_2
=
\inf_{i\in\Lambda}
\inf_{x\in\{0,1\}}
c_i^x(\mathbf0),
\qquad
\gamma
=
\min(\gamma_1,\gamma_2),
$$

and assume \(\gamma_2>0\). For \(i\notin R\), put

$$
q_i
=
\frac{c_i^0(\mathbf0)}
{c_i^0(\mathbf0)+c_i^1(\mathbf0)}.
$$

The modified generator \(\cL_R\) has invariant measure

$$
\mu_R
=
\nu_R
\otimes
\bigotimes_{i\notin R}\operatorname{Ber}(q_i).
\tag{2}
$$

Assume that the product coupling of the process on \(R\) and the exterior one-site chains satisfies

$$
\sup_{\xi\in\{0,1\}^\Lambda}
\mathbb P
\left(
\xi_s^R\ne\widetilde\xi_s^R
\right)
\le
C_R e^{-\gamma s}
\tag{3}
$$

for some \(C_R<\infty\). Here \(\widetilde\xi_s^R\) is stationary with law \(\mu_R\). In finite volume, (3) follows directly from (1) and the independent one-site couplings outside \(R\). On an infinite lattice, (3) is the corresponding uniform product-coupling assumption.

## Lemma

For every \(A\Subset\Lambda\), \(T<\infty\), \(R\Subset\Lambda\), and \(t\ge T\),

$$
\sup_{\xi\in\{0,1\}^\Lambda}
\left|
\mathbb E_A
\left[
W_t^\xi\ind(L_{T,t}^R)
\right]
-
\mu_R\left(P_T(\chi_A)\right)
\right|
\le
C_R e^{-\gamma(t-T)}.
\tag{4}
$$

In particular, the limit is the same for every initial configuration \(\xi\), and the constant in the estimate does not depend on \(T\).

## Proof

Set \(s=t-T\) and \(g=P_T(\chi_A)\). The confined-interaction representation gives

$$
\mathbb E_A
\left[
W_t^\xi\ind(L_{T,t}^R)
\right]
=
P_s^R g(\xi).
\tag{5}
$$

Couple the modified process started from \(\xi\) with its stationary version as in (3). Since \(0\le g\le1\),

$$
\begin{aligned}
\left|
P_s^R g(\xi)-\mu_R(g)
\right|
&\le
\mathbb P
\left(
\xi_s^R\ne\widetilde\xi_s^R
\right)
\\
&\le
C_Re^{-\gamma s}.
\end{aligned}
$$

Substituting \(s=t-T\) and \(g=P_T(\chi_A)\) proves (4).
