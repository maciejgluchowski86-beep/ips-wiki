---
title: Residual signed variation under coarsening
status: standard fact
audit: current
tags:
  - signed measure
  - coarsening
  - total variation
  - conditional expectation
  - integrability
---

# Residual signed variation under coarsening

Pushing a finite signed measure through a measurable coarsening averages the signed density over the information that is discarded. The total variation that remains is exactly the \(L^1\) norm of that conditional average.

## Pushforward identity

Let \((\Omega,\mathcal F)\) be a measurable space, let \(\nu\) be a finite positive measure, and let
\[
R\in L^1(\nu),
\qquad
\mu=R\nu.
\tag{1}
\]
Let
\[
\mathcal C:\Omega\to Y
\]
be measurable, and set
\[
\overline\nu=\mathcal C_\#\nu,
\qquad
\overline\mu=\mathcal C_\#\mu,
\qquad
\mathcal G=\sigma(\mathcal C).
\tag{2}
\]
Since \(\overline\mu\ll\overline\nu\), let
\[
\overline R=\frac{d\overline\mu}{d\overline\nu}.
\]
Then
\[
\overline R(\mathcal C(\omega))
=
\mathbb E_\nu[R\mid\mathcal G](\omega)
\qquad
\nu\text{-a.e.},
\tag{3}
\]
and therefore
\[
\boxed{
\|\mathcal C_\#\mu\|_{\mathrm{TV}}
=
\int_\Omega
\left|
\mathbb E_\nu[R\mid\sigma(\mathcal C)]
\right|\,d\nu.
}
\tag{4}
\]

For every measurable \(B\subseteq Y\),
\[
\begin{aligned}
\int_{\mathcal C^{-1}(B)}R\,d\nu
&=\mu(\mathcal C^{-1}(B))\\
&=\overline\mu(B)\\
&=\int_B\overline R\,d\overline\nu\\
&=\int_{\mathcal C^{-1}(B)}
\overline R(\mathcal C(\omega))\,d\nu(\omega).
\end{aligned}
\]
The pullback \(\overline R\circ\mathcal C\) is \(\mathcal G\)-measurable, proving (3). Integrating its absolute value gives (4).

The right side of (4) is independent of the particular positive reference representation \(\mu=R\nu\), because it equals the total-variation norm of the pushforward signed measure.

## Monotonicity under further coarsening

Suppose two coarsenings satisfy
\[
\sigma(\mathcal C_1)\subseteq\sigma(\mathcal C_2).
\]
By the tower property,
\[
\mathbb E[R\mid\sigma(\mathcal C_1)]
=
\mathbb E[
\mathbb E[R\mid\sigma(\mathcal C_2)]
\mid
\sigma(\mathcal C_1)].
\]
Conditional Jensen therefore gives
\[
\int
\left|
\mathbb E[R\mid\sigma(\mathcal C_1)]
\right|d\nu
\le
\int
\left|
\mathbb E[R\mid\sigma(\mathcal C_2)]
\right|d\nu.
\tag{5}
\]
Thus forgetting more information cannot increase the surviving signed variation. At the endpoints,
\[
\|\operatorname{Id}_\#\mu\|_{\mathrm{TV}}
=
\|\mu\|_{\mathrm{TV}},
\qquad
\|\operatorname{const}_\#\mu\|_{\mathrm{TV}}
=
|\mu(\Omega)|.
\tag{6}
\]

## Countable-family calculation

Let \(\mathfrak T\) be countable. For each \(\tau\in\mathfrak T\), let
\[
\mu_\tau=R_\tau\nu_\tau
\]
be a finite signed measure and let
\[
\mathcal C_\tau:\Omega_\tau\to Y_\tau
\]
be measurable. Write
\[
\overline\mu_\tau
=
(\mathcal C_\tau)_\#\mu_\tau,
\qquad
V_\tau
=
\|\overline\mu_\tau\|_{\mathrm{TV}}.
\tag{7}
\]

Choose a probability mass function \(\pi\) with \(\pi(\tau)>0\) for every \(\tau\), and for each \(\tau\) choose a probability measure \(Q_\tau\) dominating \(\overline\mu_\tau\). Sample
\[
S\sim\pi,
\qquad
U\mid\{S=\tau\}\sim Q_\tau,
\]
and define
\[
Y
=
\frac1{\pi(S)}
\frac{d\overline\mu_S}{dQ_S}(U).
\tag{8}
\]
Then Tonelli's theorem gives
\[
\boxed{
\mathbb E|Y|
=
\sum_{\tau\in\mathfrak T}V_\tau.
}
\tag{9}
\]
Indeed,
\[
\begin{aligned}
\mathbb E|Y|
&=
\sum_\tau
\pi(\tau)
\int
\frac1{\pi(\tau)}
\left|
\frac{d\overline\mu_\tau}{dQ_\tau}
\right|dQ_\tau\\
&=
\sum_\tau
\|\overline\mu_\tau\|_{\mathrm{TV}}.
\end{aligned}
\]
Consequently,
\[
Y\in L^1
\quad\Longleftrightarrow\quad
\sum_\tau V_\tau<\infty.
\tag{10}
\]

If another estimator \(\widetilde Y\) uses extra randomness but satisfies
\[
\mathbb E[\widetilde Y\mid S,U]=Y,
\]
then conditional Jensen yields
\[
\mathbb E|\widetilde Y|
\ge
\mathbb E|Y|
=
\sum_\tau V_\tau.
\tag{11}
\]
Thus, once the retained information and conditional barycenter are fixed, auxiliary conditionally unbiased randomness cannot lower the first absolute moment below the residual total variation.

These identities are measure-theoretic. They do not depend on a particular PDE, branching architecture, or choice of retained coordinates.
