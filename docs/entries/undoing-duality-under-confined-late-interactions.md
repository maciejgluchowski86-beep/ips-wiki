---
title: Undoing duality under confined late interactions
status: proved here
tags:
  - patch
  - duality
  - spin systems
  - Feynman-Kac
---

# Undoing duality under confined late interactions

Fix the [monomial duality for spin systems](monomial-duality-for-spin-systems.md), with signed dual \((A_s,\sigma_s)\), Feynman--Kac potential \(V\), and successful-interaction sigma algebra \(\cG_t\). A restriction on the [successful interactions](successful-interaction.md) during a late time interval can first be removed from the [patch representation](patch-representation-of-spin-systems.md) and then identified with the dual of a modified spin system.

## Confined late interactions

Let the dual start from \((A,+)\), where \(A\Subset\Lambda\), and write

$$
Z_t^\xi
=
\sigma_t
\exp\left(
\int_0^tV(A_s)\,ds
\right)
\chi_{A_t}(\xi),
$$

and

$$
W_t^\xi
=
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\xi,P).
$$

Thus

$$
W_t^\xi
=
\mathbb E_{(A,+)}
\left[
Z_t^\xi
\middle|
\cG_t
\right].
\tag{1}
$$

Fix \(0\le T\le t\) and \(R\subseteq\Lambda\). Define

$$
L_{T,t}^R
=
\left\{
\begin{array}{c}
\text{every successful interaction }(i,s,S)
\text{ with }T\le s<t\\
\text{satisfies }i\in R\text{ and }S\subseteq R
\end{array}
\right\}.
\tag{2}
$$

Deaths have empty target and are not successful interactions, so they are unrestricted. The event \(L_{T,t}^R\) belongs to \(\cG_t\). On this event every end patch based at a site outside \(R\) has length at least \(t-T\).

## Modified spin system

For \(Q\subseteq\Lambda\), let \(\xi^{Q,0}\) be the configuration that agrees with \(\xi\) on \(Q\) and is zero on \(Q^c\). Define

$$
c_{i,R}(\xi)
=
\begin{cases}
c_i(\xi^{R,0}),
&i\in R,
\\
c_i(\xi^{\{i\},0}),
&i\notin R.
\end{cases}
\tag{3}
$$

The modified spin-system generator is

$$
\cL_Rf(\xi)
=
\sum_{i\in\Lambda}
c_{i,R}(\xi)
\left(
f(\xi^i)-f(\xi)
\right).
\tag{4}
$$

Write \((P_s^R)_{s\ge0}\) for its semigroup. Inside \(R\), the rates are those of the original spin system with zero exterior configuration. Outside \(R\), the sites evolve independently with constant rates \(c_i^0(\mathbf0)\) and \(c_i^1(\mathbf0)\).

## Proposition

For every \(A\Subset\Lambda\), \(\xi\in\{0,1\}^\Lambda\), \(0\le T\le t\), and \(R\subseteq\Lambda\),

$$
\begin{aligned}
\mathbb E_A
\left[
W_t^\xi\ind(L_{T,t}^R)
\right]
&=
\mathbb E_{(A,+)}
\left[
Z_t^\xi\ind(L_{T,t}^R)
\right]
\\
&=
\left(
P_{t-T}^R P_T(\chi_A)
\right)(\xi).
\end{aligned}
\tag{5}
$$

Here \(\mathbb E_A\) denotes expectation over the successful-interaction skeleton, as in the patch representation, while \(\mathbb E_{(A,+)}\) denotes expectation over the full marked dual process.

The operator order in (5) is essential. The identity describes a left evolution of observables: first apply \(P_T\), then apply \(P_{t-T}^R\). A spin path run chronologically with generator \(\cL\) until time \(T\) and generator \(\cL_R\) afterward would instead have transition operator \(P_TP_{t-T}^R\), which need not agree with (5).

## Proof

We first remove the patch averaging, then identify the late confinement event as killing forbidden dual interactions, and finally split the dual evolution at time \(T\).

### Removing the patch averaging

Since \(L_{T,t}^R\in\cG_t\), equation (1) and the tower property give

$$
\begin{aligned}
\mathbb E_A
\left[
W_t^\xi\ind(L_{T,t}^R)
\right]
&=
\mathbb E_{(A,+)}
\left[
\mathbb E_{(A,+)}
\left[
Z_t^\xi
\middle|
\cG_t
\right]
\ind(L_{T,t}^R)
\right]
\\
&=
\mathbb E_{(A,+)}
\left[
Z_t^\xi\ind(L_{T,t}^R)
\right].
\end{aligned}
\tag{6}
$$

This proves the first equality in (5). It remains to return the restricted dual expectation to the spin side.

### The late killed dual

Retain every death interaction. Among the nonempty-target interactions, retain only those with source in \(R\) and target contained in \(R\). Their rates are

$$
\delta_{i,R}(S)
=
\ind\left(
S=\vn
\text{ or }
\left(i\in R\text{ and }S\subseteq R\right)
\right)\delta_i(S),
$$

and

$$
\beta_{i,R}(S)
=
\ind\left(i\in R\text{ and }S\subseteq R\right)\beta_i(S).
\tag{7}
$$

Let \(\cD_R\) be the generator formed from these retained interactions. If the active set is \(B\), the total rate of forbidden successful interactions is

$$
\kappa_R(B)
=
\sum_{i\in B}
\sum_{\substack{\vn\ne S\subseteq N(i)\\
i\notin R\text{ or }S\nsubseteq R}}
\left(
\delta_i(S)+\beta_i(S)
\right).
\tag{8}
$$

During \([T,t)\), the indicator \(\ind(L_{T,t}^R)\) becomes zero at the first forbidden successful interaction. Hence the dual process relevant to the restricted expectation has generator

$$
\cD_R-\kappa_R,
$$

where the second term is killing. After including the original Feynman--Kac potential, its operator is

$$
\cD_R+V-\kappa_R.
\tag{9}
$$

By the coefficient formulas in the monomial duality, the rates in (3) leave every empty-target coefficient unchanged and delete precisely the nonempty-target coefficients whose source or target is not contained in \(R\). Thus the signed dual generator of \(\cL_R\) is \(\cD_R\), and its potential is

$$
V_R(B)
=
V(B)-\kappa_R(B).
\tag{10}
$$

Therefore

$$
(\cL_R)_\xi H(Y,\xi)
=
(\cD_R)_YH(Y,\xi)
+
V_R(B)H(Y,\xi),
\qquad
Y=(B,\sigma).
\tag{11}
$$

Equations (9)--(11) identify the late killed dual with the ordinary Feynman--Kac dual of \(\cL_R\).

### Splitting at time \(T\)

Set \(s=t-T\). Conditional on \(Y_T=(A_T,\sigma_T)\), the post-\(T\) killed evolution and the Feynman--Kac duality for \(\cL_R\) give

$$
\begin{aligned}
&\mathbb E
\left[
\sigma_t
\exp\left(
\int_T^tV(A_u)\,du
\right)
\chi_{A_t}(\xi)
\ind(L_{T,t}^R)
\middle|
Y_T
\right]
\\
&\hspace{5em}=
\sigma_T
\left(
P_s^R(\chi_{A_T})
\right)(\xi).
\end{aligned}
\tag{12}
$$

Multiplying by the weight accumulated before \(T\) and taking expectation yields

$$
\begin{aligned}
\mathbb E_{(A,+)}
\left[
Z_t^\xi\ind(L_{T,t}^R)
\right]
=
\mathbb E_{(A,+)}
\left[
\sigma_T
\exp\left(
\int_0^TV(A_u)\,du
\right)
\left(
P_s^R(\chi_{A_T})
\right)(\xi)
\right].
\end{aligned}
\tag{13}
$$

The original duality at time \(T\) is the equality of functions

$$
P_T(\chi_A)
=
\mathbb E_{(A,+)}
\left[
\sigma_T
\exp\left(
\int_0^TV(A_u)\,du
\right)
\chi_{A_T}
\right].
\tag{14}
$$

Apply the linear operator \(P_s^R\) to (14) and evaluate at \(\xi\). The right-hand side becomes the expectation in (13), so

$$
\mathbb E_{(A,+)}
\left[
Z_t^\xi\ind(L_{T,t}^R)
\right]
=
\left(
P_s^RP_T(\chi_A)
\right)(\xi).
$$

Since \(s=t-T\), this proves the second equality in (5).
