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
  - Holder regularity
---

# L1 random-patch conjecture for the quadratic Hessian PDE

The [finite-depth patch regrouping](finite-depth-duhamel-patch-regrouping.md) is an exact signed identity, and the [deterministic self-consistent patch iteration](self-consistent-patch-iteration-for-quadratic-hessian-pde.md) converges in a small uniformly parabolic regime. It remains open whether these facts can be combined into a full infinite-depth patch-first importance sampler whose random functional is absolutely integrable. The conjecture below is deliberately separate from the two proved statements.

Two earlier obstructions have now been resolved or narrowed. Sup norms of spatially varying side profiles are insufficient, but deterministic patches with uniformly bounded spatial \(C^\alpha\) side profiles have only geometric growth in their length. On the other hand, the raw random Hessian edge does **not** inherit the same pathwise \(C^\alpha\) gain. The current open problem is therefore formulated at the level of conditional means given the patch skeleton, with the centered fluctuation field separated as the likely next obstruction.

**References.** The deterministic cancellation estimates are in [Holder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md). Spatial and parabolic Holder norms are defined in [Parabolic Holder spaces](parabolic-holder-spaces.md). Random function-space moments are defined in [Random fields in function spaces](random-fields-in-function-spaces.md), and conditional means and fluctuation fields are defined in [Conditional expectation and fluctuations of random fields](conditional-expectation-and-fluctuations-of-random-fields.md). A possible frequency-localized alternative for fluctuations is described in [Besov spaces on the torus](besov-spaces-on-the-torus.md).

## Conjecture

Consider

$$
\partial_tv
=
\frac12\partial_x^2v
+\lambda(\partial_x^2v)^2,
\qquad
v(0)=\phi
$$

on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), under the Schauder smallness hypothesis of the [self-consistent iteration theorem](self-consistent-patch-iteration-for-quadratic-hessian-pde.md).

There exists a patch-first randomization of the full Duhamel expansion with the following properties:

1. maximal consecutive left-spine Hessian events are sampled and evaluated as complete multi-event patches;
2. conditional on the patch skeleton, distinct side patches use independent auxiliary randomness, with the usual [importance-sampling compensators](importance-sampling-compensators.md);
3. the resulting infinite-depth random functional \(H_{\mathrm{patch}}(t,x)\) belongs to \(L^1\) for every \(0\leq t\leq T\); and
4. its expectation equals the deterministic solution produced by the self-consistent iteration.

The sampling law is part of the conjecture: it may be chosen to exploit the multi-event structure and need not be the edge-by-edge lifetime law used in standard derivative-weight branching.

## Audited deterministic Holder cancellation

Let

$$
K_r^{(k)}=\partial_x^{2k}P_r.
$$

Since every positive-order Hermite polynomial has Gaussian mean zero,

$$
\mathbb E[He_{2k}(Z)]=0,
$$

and therefore

$$
K_r^{(k)}f(x)
=
r^{-k}
\mathbb E\left[
He_{2k}(Z)
\bigl(f(x+\sqrt r\,Z)-f(x)\bigr)
\right].
\tag{1}
$$

If \(f\in C^\alpha\), \(0<\alpha<1\), then

$$
\lVert K_r^{(k)}f\rVert_\infty
\leq
c_{2k,\alpha}
 r^{-k+\alpha/2}[f]_{C^\alpha},
\tag{2}
$$

where

$$
c_{2k,\alpha}
=
\mathbb E\left[
|He_{2k}(Z)|\,|Z|^\alpha
\right]
\leq
\sqrt{(2k)!}
\left(\mathbb E|Z|^{2\alpha}\right)^{1/2}.
\tag{3}
$$

For \(k=1\), this gives

$$
\lVert\partial_x^2P_rf\rVert_\infty
\leq
c_{2,\alpha}
 r^{-1+\alpha/2}[f]_{C^\alpha}.
\tag{4}
$$

The heat semigroup also contracts spatial Holder norms:

$$
\lVert P_rf\rVert_{C^\alpha}
\leq
\lVert f\rVert_{C^\alpha}.
\tag{5}
$$

## Commutators and derivative clusters

Let \(M_Bg=Bg\). For every \(k\geq1\),

$$
K_R^{(k)}M_B
=
M_BK_R^{(k)}
+[K_R^{(k)},M_B],
\tag{6}
$$

and

$$
\begin{aligned}
[K_R^{(k)},M_B]g(x)
={}&R^{-k}
\mathbb E\Bigl[
He_{2k}(Z)
\bigl(B(x+\sqrt R\,Z)-B(x)\bigr)\\
&\hspace{38mm}\times g(x+\sqrt R\,Z)
\Bigr].
\end{aligned}
\tag{7}
$$

Hence

$$
\lVert[K_R^{(k)},M_B]g\rVert_\infty
\leq
c_{2k,\alpha}
R^{-k+\alpha/2}
[B]_{C^\alpha}\lVert g\rVert_\infty.
\tag{8}
$$

Repeatedly applying (6) to a length-\(m\) patch groups consecutive derivative edges into clusters whose lengths form an ordered composition

$$
m=\ell_1+\cdots+\ell_q.
\tag{9}
$$

There is one additional terminal choice: the innermost cluster either stops at the last side multiplier or commutes through it and reaches the terminal profile. Thus the \(2^{m-1}\) ordered compositions do not by themselves index every term. The full commutator expansion contains at most

$$
2^m
\tag{10}
$$

terms. This correction is only an extra factor of two at the combinatorial level and does not alter the geometric-growth conclusion.

A cluster of \(\ell\) consecutive Hessian edges has total heat time \(R\) and derivative operator \(K_R^{(\ell)}\). For fixed \(R\), the internal simplex of its \(\ell\) positive edge lengths has volume

$$
\frac{R^{\ell-1}}{(\ell-1)!}.
$$

Combining this factor with (8) leaves

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
R^{-1+\alpha/2}.
\tag{11}
$$

The singularity in (11) is integrable at zero, and

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
\leq
C_\alpha4^\ell.
\tag{12}
$$

Therefore neither the Hermite constants nor the corrected cluster combinatorics reintroduce factorial growth.

## Deterministic Holder patch bound

Fix \(0<\alpha<1\) and \(T>0\). There is a constant \(C_{\alpha,T}<\infty\) such that, if

$$
G\in C^\alpha(\mathbb T),
\qquad
\sup_{1\leq j\leq m}
\sup_{0\leq s\leq T}
\lVert b_j(s,\cdot)\rVert_{C^\alpha}
\leq M,
$$

then the complete length-\(m\) patch satisfies

$$
\sup_{0\leq t\leq T}
\lVert\mathcal P_m[b_1,\ldots,b_m;G](t)\rVert_\infty
\leq
\lVert G\rVert_{C^\alpha}
\bigl(|\lambda|C_{\alpha,T}\max\{1,M\}\bigr)^m.
\tag{13}
$$

The proof is the cluster expansion above. Each nonterminal cluster contributes one Holder increment and one integrable total-time factor \(R^{-1+\alpha/2}\); the terminal cluster is no worse. Since the cluster lengths sum to \(m\), the cluster constants multiply geometrically, and the at-most-\(2^m\) expansion count is absorbed into the same exponential constant.

This proposition is deterministic. It says nothing by itself about pathwise Holder norms of random side-patch estimators.

## The old sup-norm counterexample escapes through its Holder norm

The smooth counterexample to a side-profile \(L^\infty\) bound uses

$$
b_m(h-r,x)
=
-
\sum_{k=1}^m
\psi(N_k^2r)\cos(N_kx),
\qquad
N_k=2^kN_0,
$$

with disjoint temporal supports. Thus \(\lVert b_m\rVert_\infty\leq1\), but its Hessian Duhamel contribution grows linearly in \(m\). At the same time,

$$
[\cos(Nx)]_{C^\alpha}
\asymp N^\alpha,
$$

so

$$
\sup_s\lVert b_m(s,\cdot)\rVert_{C^\alpha}
\asymp
N_m^\alpha
\asymp
2^{\alpha m}.
\tag{14}
$$

Its parabolic Holder norm has the same scaling because the time localization is of order \(N_k^{-2}\). Thus the old counterexample does not contradict (13).

## Failure of direct pathwise random Holder control

The deterministic gain in (4) occurs only after averaging the centered Hermite mark. For one raw Hessian edge define

$$
\widehat K_r f(x,Z)
=
\frac{He_2(Z)}{r}
\left[
 f(x+\sqrt r\,Z)-f(x)
\right].
\tag{15}
$$

Its pathwise sup norm has the expected gain:

$$
\mathbb E
\lVert\widehat K_r f(\cdot,Z)\rVert_\infty
\leq
c_{2,\alpha}
 r^{-1+\alpha/2}[f]_{C^\alpha}.
\tag{16}
$$

However, for the pathwise Holder seminorm one only gets

$$
[\widehat K_r f(\cdot,Z)]_{C^\alpha}
\leq
\frac{2|He_2(Z)|}{r}
[f]_{C^\alpha}.
\tag{17}
$$

There is no uniform factor \(r^{\alpha/2}\) missing from (17). Indeed, translation is not small in operator norm on the \(C^\alpha\) unit ball. For

$$
f_N(x)=N^{-\alpha}\cos(Nx),
$$

one has \(\lVert f_N\rVert_{C^\alpha}\asymp1\). Choosing \(N\asymp r^{-1/2}\) and restricting \(Z\) to a fixed interval on which both \(|He_2(Z)|\) and \(|\sin(N\sqrt r Z/2)|\) are bounded below gives

$$
\mathbb E
[\widehat K_r f_N(\cdot,Z)]_{C^\alpha}
\geq
c_\alpha r^{-1}.
\tag{18}
$$

Thus a direct recursive estimate in

$$
L^p(\Omega;C^\alpha)
$$

for the raw edge fields cannot reproduce the deterministic Holder gain. The naive pathwise random-Holder route is ruled out.

## Conditional expectation restores the deterministic cancellation

Let \(\mathcal G\) contain the exposed patch skeleton, the edge length \(r\), and the input field \(f\), but not the centered Gaussian mark \(Z\). Then

$$
\mathbb E\left[
\widehat K_r f(\cdot,Z)
\,\middle|\,
\mathcal G
\right]
=
K_rf.
\tag{19}
$$

More generally, if the input field is itself a descendant random field that is conditionally independent of the fresh Gaussian edge mark given \(\mathcal G\), then linearity and conditional independence replace \(f\) in (19) by its conditional mean.

At finite patch depth, distinct side patches are conditionally independent given the patch skeleton. Consequently, whenever the products are integrable,

$$
\mathbb E\left[
\prod_PY_P
\,\middle|\,
\mathcal G
\right]
=
\prod_P
m_P,
\qquad
m_P:=\mathbb E[Y_P\mid\mathcal G].
\tag{20}
$$

This is exactly the level at which the deterministic Holder cluster estimate can act: the signed Gaussian and descendant randomness are averaged before the function-space norm is applied.

## Current formulation of the open problem

The main regularity object is now the family of conditional mean side fields

$$
m_P
=
\mathbb E[Y_P\mid\mathcal G_P],
\tag{21}
$$

where \(\mathcal G_P\) is the appropriate exposed patch-skeleton sigma-field. A route to C would need recursive bounds, uniform in the relevant birth time and position, that keep these conditional means in a spatial Holder or comparable deterministic regularity class so that (13) can be iterated through the genealogy.

This is not enough for \(L^1\) by itself. Write the raw side field as

$$
Y_P=m_P+R_P,
\qquad
R_P:=Y_P-m_P,
\qquad
\mathbb E[R_P\mid\mathcal G_P]=0.
\tag{22}
$$

The field \(R_P\) is the *conditional fluctuation term*. It is the likely next obstruction: the conditional mean may be regular by cancellation while the raw estimator still has large absolute moments. A proof of C must therefore combine conditional-mean regularity with enough conditional moment or weaker function-space control of the fluctuations to justify the infinite-depth \(L^1\) limit.

A pathwise parabolic Holder norm is not currently the preferred target for \(R_P\): the genealogy may jump with the horizon, and even one fixed-time centered Hessian edge fails to gain in pathwise spatial \(C^\alpha\). Integrated time norms, scale-localized Besov norms, or another cancellation-adapted fluctuation norm remain possible.

The conjecture remains open. Neither the deterministic geometric patch estimate nor the conditional factorization identity proves absolute integrability of the infinite random patch functional.