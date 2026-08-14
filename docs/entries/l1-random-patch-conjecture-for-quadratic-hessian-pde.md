---
title: L1 random-patch conjecture for the quadratic Hessian PDE
status: conjecture
tags:
  - PDE
  - branching process
  - patch
  - integrability
  - conjecture
  - Hessian
  - Gaussian analysis
---

# L1 random-patch conjecture for the quadratic Hessian PDE

The quadratic-Hessian programme now has three proved levels rather than two.

1. [Theorem C-prime](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md) integrates every continuous variable inside a decorated skeleton and gives an unbiased \(L^1\) skeleton-only estimator under the Catalan smallness condition.
2. The [raw-barycenter obstruction](raw-marked-l1-obstruction-for-quadratic-hessian-pde.md) shows that the canonical raw signed marked contribution cannot remain the conditional barycenter of an \(L^1\) estimator, even after arbitrary proposal changes, for one fixed arbitrarily small \(C^\infty\) datum.
3. The [time-spine coarsening theorem](time-spine-coarsening-for-quadratic-hessian-patches.md) retains the actual branch times on one canonical maximal-left spine while averaging all other continuous marks. Under one additional geometric smallness condition, this gives an unbiased \(L^1\) estimator with genuine continuous interior randomness.

Thus the literal conjecture below is **proved on a stronger small-data subregime**. It remains a conjecture because its stated regime is the full C-prime region, where only complete interior averaging is presently known to close.

The new theorem also removes one candidate escape: naive patchwise Gaussian-bridge coarsening fails on the fixed obstruction datum. The right-comb obstruction genealogies consist entirely of one-edge maximal-left patches, so a one-edge bridge map has no internal bridge coordinate to average.

## PDE and C-prime regime

Fix

$$
0<\alpha<1,
\qquad
T>0,
\qquad
\lambda\in\mathbb R,
\qquad
\phi\in C^{2+\alpha}(\mathbb T),
\qquad
\mathbb T=\mathbb R/(2\pi\mathbb Z).
$$

For

$$
\partial_tv
=
\frac12v_{xx}
+\lambda(v_{xx})^2,
\qquad
v(0)=\phi,
$$

write \(z=v_{xx}\). Then

$$
z(t)
=
P_t\phi''
+\lambda\int_0^t
\partial_x^2P_{t-s}[z(s)^2]\,ds.
\tag{1}
$$

Let

$$
X_{\alpha,T}
=
C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
\qquad
M
=
\|P_\cdot\phi''\|_{X_{\alpha,T}},
$$

and let \(C_{\mathcal D}(\alpha,T)\) be the Hessian Duhamel operator constant. Put

$$
a
=
|\lambda|C_{\mathcal D}(\alpha,T)M.
\tag{2}
$$

The C-prime regime is

$$
4a<1.
\tag{3}
$$

Under (3), Theorem C-prime constructs the unique small fixed point \(z_*\) in its Catalan ball and an unbiased skeleton-only \(L^1\) estimator.

## Conjecture C: full C-prime regime

Under (3), does there exist a patch-first randomization with the following properties?

1. Maximal consecutive left-spine Hessian events are organized into complete multi-event patches.
2. Conditional on an exposed patch skeleton, different descendant patches may use auxiliary randomness with appropriate importance-sampling compensators.
3. Nontrivial continuous Gaussian/Hermite, branch-time, or descendant randomness remains inside the sampled patches rather than **all** such variables being deterministically integrated out.
4. The resulting infinite-depth random functional belongs to \(L^1\) for every \((t,x)\in[0,T]\times\mathbb T\).
5. Its expectation is \(z_*(t,x)\).

The conjecture deliberately does **not** require the canonical raw signed marked integrand to remain the conditional barycenter after all raw marks have been exposed.

## What is already false

For one centered Hessian edge, the canonical raw transfer is

$$
\widehat K_rF(x,Z)
=
\frac{He_2(Z)}r
\left[
F(x+\sqrt rZ)-F(x)
\right].
\tag{4}
$$

On a raw comb cylinder \(\Gamma_m\), let \(Q_m\) be any positive proposal dominating the intrinsic signed raw measure \(
u_m\). The raw-barycenter strengthening requires

$$
\mathbb E_Q[Y\mid\text{raw marks}]
=
\frac{d\nu_m}{dQ_m}.
\tag{5}
$$

For one fixed smooth datum, the raw-barycenter obstruction gives

$$
\mathbb E|Y|=\infty
\tag{6}
$$

for every estimator satisfying (5). This is proposal invariant: lifetime, genealogy, Gaussian proposals, dependence among proposal variables, and auxiliary conditionally unbiased randomness may all be changed.

Hence the following statement is false:

> Keep the canonical raw marked state and require its raw signed contribution to remain the conditional barycenter, while changing only the positive sampling architecture or adding conditionally unbiased auxiliary randomness.

## A genuine retained-randomness theorem

Let \(K_{\mathrm{time}}(\alpha,T)<\infty\) be the geometric absolute-time patch constant from the time-spine theorem, and put

$$
b
=
|\lambda|K_{\mathrm{time}}(\alpha,T)M.
$$

Let

$$
C(a)
=
\sum_{n\ge0}C_na^n
=
\frac{1-\sqrt{1-4a}}{2a},
\qquad C(0)=1.
$$

If

$$
4a<1,
\qquad
bC(a)<1,
\tag{7}
$$

then the time-spine coarsening gives

$$
\sum_{\tau}
\|(\mathcal C_\tau^{\mathrm{time}})_\#\mu_\tau\|_{\mathrm{TV}}
<\infty.
\tag{8}
$$

The coarsening retains the ordered branch times on the root maximal-left patch of each finite tree and integrates out every Gaussian/Brownian mark and every continuous variable in the side subtrees. Sampling the coarsened signed measures therefore gives an unbiased \(L^1\) representation of \(z_*\) in which continuous branch-time randomness remains and affects the estimator value.

Thus Conjecture C is already true on the subregime (7).

## Why naive Gaussian-bridge coarsening is not the missing full-regime proof

Patchwise Gaussian-bridge averaging acts only when at least two Hessian Gaussian coordinates belong to the same maximal-left patch. The fixed-datum obstruction may be realized on right combs. At every internal vertex of a right comb the left child is terminal, so every maximal-left patch has length one. On a one-edge patch the normalized endpoint Gaussian is the original Gaussian mark itself. Hence patchwise bridge coarsening is the identity, up to an invertible coordinate change, on the obstruction family and preserves its divergent total variation.

This does not say that bridge averaging is useless locally. For a genuine multi-edge patch it converts factorial retained-mark growth into geometric growth. It says only that the naive patchwise version cannot be the global solution because some genealogies never contain a multi-edge patch.

## Randomness, raw-faithfulness, and coarsening

Random dependence on marks is strictly weaker than raw-barycenter retention. The one-edge antithetic estimator

$$
\widetilde K_rF(x,Z)
=
\frac{He_2(Z)}{2r}
\left[
F(x+\sqrt rZ)
+F(x-\sqrt rZ)
-2F(x)
\right]
\tag{9}
$$

still uses \(Z\) and is unbiased, but conditional on \(Z\) it is not the raw transfer (4). Decorative randomness is weaker still: one may append unused Gaussian marks to the C-prime estimator without changing its value.

The time-spine theorem gives the first proved nondecorative intermediate point. The current hierarchy is

- raw-faithful / identity: non-\(L^1\) for the fixed smooth datum;
- time-spine coarsening: \(L^1\) under (7), with continuous branch-time randomness retained;
- constant coarsening / C-prime: \(L^1\) under the full C-prime condition (3), with all continuous interior variables averaged.

## What remains open

The remaining question is now quantitative rather than existential:

> Does a nonconstant coarsening with genuine continuous interior randomness have summable total variation throughout the entire C-prime regime \(4a<1\)?

The time-spine construction answers this on the stronger subregime (7). It is open whether its additional condition can be removed, whether another choice of retained coordinates works on the full Catalan interval, or whether there is a genuine gap between the full C-prime regime and every nonconstant coarsening.

In particular, complete interior averaging is **not necessary** for \(L^1\) in general, but it remains the only proved construction on all of (3).
