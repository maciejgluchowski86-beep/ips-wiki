---
title: Undoing duality under confined interactions
status: proved here
tags:
  - patch
  - duality
  - spin systems
  - Feynman-Kac
---

# Undoing duality under confined interactions

Restricting the [successful interactions](successful-interaction.md) of the signed dual during a time interval is equivalent to replacing the spin system by a zero-boundary modification during the corresponding semigroup interval. This converts a weighted dual confinement estimate into an ordinary spin-system estimate.

Fix the [monomial duality for spin systems](monomial-duality-for-spin-systems.md), with signed dual \((A_r,\sigma_r)\), Feynman--Kac potential \(V\), and successful-interaction sigma algebra \(\cG_t\). Let the dual start from \((A,+)\), where \(A\Subset\Lambda\), and write

$$
Z_t^\xi
=
\sigma_t\exp\left(\int_0^tV(A_r)\,dr\right)\chi_{A_t}(\xi)
$$

and

$$
W_t^\xi
=
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C(\xi,P).
$$

The [patch representation](patch-representation-of-spin-systems.md) gives

$$
W_t^\xi=\mathbb E_{(A,+)}\left[Z_t^\xi\mid\cG_t\right].
\tag{1}
$$

## Confined interactions

Fix \(0\le s\le u\le t\) and \(R\subseteq\Lambda\). Define

$$
E_{s,u}^R
=
\left\{
\text{every ordinary successful interaction }(i,r,S)\text{ with }s<r\le u
\text{ satisfies }i\in R\text{ and }S\subseteq R
\right\}.
\tag{2}
$$

Deaths have empty target and are not successful interactions, so they are unrestricted. The event \(E_{s,u}^R\) belongs to \(\cG_t\). Write

$$
E_T^R=E_{0,T}^R.
$$

If \(A\subseteq R\), then

$$
E_T^R=\{\mathbf{Cone}_T\subseteq R\},
\tag{3}
$$

where \(\mathbf{Cone}_T\) is the [interaction cone](interaction-cone.md). The event of no successful interaction in \((s,u]\) is

$$
L_{s,u}=E_{s,u}^{\vn}.
$$

## Modified and zero-boundary systems

For \(Q\subseteq\Lambda\), let \(\xi^{Q,0}\) agree with \(\xi\) on \(Q\) and vanish on \(Q^c\). Define

$$
c_{i,R}(\xi)
=
\begin{cases}
c_i(\xi^{R,0}), & i\in R,\\
c_i(\xi^{\{i\},0}), & i\notin R.
\end{cases}
\tag{4}
$$

Let \(\cL_R\) be the spin-system generator with rates \(c_{i,R}\), and write \(P_t^R\) for its semigroup. Inside \(R\), this is the original spin system with zero boundary condition. Outside \(R\), the sites evolve independently with constant rates \(c_i^0(\mathbf0)\) and \(c_i^1(\mathbf0)\).

For \(R\Subset\Lambda\), the zero-boundary generator on \(R\) is

$$
\cL^{R,0}f(\xi)
=
\sum_{i\in R}c_i(\xi^{R,0})\bigl(f(\xi^i)-f(\xi)\bigr),
\tag{5}
$$

and its semigroup is denoted by \(P_t^{R,0}\). If \(f\) depends only on the spins in \(R\), then

$$
P_t^Rf=P_t^{R,0}f.
\tag{6}
$$

## Proposition

For every \(A\Subset\Lambda\), \(\xi\in\{0,1\}^\Lambda\), \(0\le s\le u\le t\), and \(R\subseteq\Lambda\),

$$
\mathbb E_A\left[W_t^\xi\ind(E_{s,u}^R)\right]
=
\mathbb E_{(A,+)}\left[Z_t^\xi\ind(E_{s,u}^R)\right]
=
\left(P_{t-u}P_{u-s}^RP_s\chi_A\right)(\xi).
\tag{7}
$$

In particular, if \(A\subseteq R\), then confinement during the initial dual interval gives

$$
\mathbb E_A\left[W_t^\xi\ind(E_T^R)\right]
=
\left(P_{t-T}P_T^{R,0}\chi_A\right)(\xi),
\tag{8}
$$

whereas confinement during the final dual interval gives

$$
\mathbb E_A\left[W_t^\xi\ind(E_{T,t}^R)\right]
=
\left(P_{t-T}^RP_T\chi_A\right)(\xi).
\tag{9}
$$

The operator order reflects the direction of the dual calculation: later dual intervals act farther to the left.

## Proof

Since \(E_{s,u}^R\in\cG_t\), equation (1) and the tower property give the first equality in (7).

To identify the restricted dual expectation, retain every empty-target death interaction. For \(S\ne\vn\), retain a split or birth interaction only when \(i\in R\) and \(S\subseteq R\). Thus

$$
\delta_{i,R}(S)=\ind\bigl(S=\vn\text{ or }(i\in R,\ S\subseteq R)\bigr)\delta_i(S),
\qquad
\beta_{i,R}(S)=\ind(i\in R,\ S\subseteq R)\beta_i(S).
\tag{10}
$$

If the active set is \(B\), the rate of forbidden successful interactions is

$$
\kappa_R(B)
=
\sum_{i\in B}
\sum_{\substack{\vn\ne S\subseteq N(i)\\i\notin R\text{ or }S\nsubseteq R}}
\bigl(\delta_i(S)+\beta_i(S)\bigr).
\tag{11}
$$

On the interval \((s,u]\), the indicator of \(E_{s,u}^R\) kills the dual at the first forbidden successful interaction. The corresponding Feynman--Kac operator is therefore

$$
\cD_R+V-\kappa_R.
\tag{12}
$$

The monomial coefficients of the rates in (4) retain every empty-target coefficient and precisely the nonempty-target coefficients with source and target in \(R\). Hence \(\cD_R\) is the signed dual generator of \(\cL_R\), and its potential is \(V_R=V-\kappa_R\). Thus (12) is the ordinary Feynman--Kac dual operator of \(\cL_R\).

Apply the original duality on \([0,s]\), the modified duality on \([s,u]\), and the original duality on \([u,t]\). Successive dual intervals act from right to left on observables, giving

$$
\mathbb E_{(A,+)}\left[Z_t^\xi\ind(E_{s,u}^R)\right]
=
\left(P_{t-u}P_{u-s}^RP_s\chi_A\right)(\xi).
$$

This proves (7). If \(s=0\), \(u=T\), and \(A\subseteq R\), then (6) gives (8). Taking \(s=T\) and \(u=t\) gives (9).
