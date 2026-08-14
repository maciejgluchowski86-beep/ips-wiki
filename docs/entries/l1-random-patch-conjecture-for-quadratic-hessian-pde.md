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

The quadratic Hessian route now has three proved layers below the full random-patch problem. Finite Duhamel trees regroup exactly into patches; the deterministic semi-implicit iteration converges in a small uniformly parabolic regime; and, under an explicit Catalan smallness condition, the new [skeleton-averaged representation](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md) gives an unbiased \(L^1\) estimator after **all continuous randomness inside each decorated skeleton has been averaged out**.

The conjecture on this page is stronger. It asks whether one can retain the genuinely random Gaussian/Hermite and descendant marks inside the patches and still obtain an \(L^1\) unbiased estimator. That remains open.

The analytic obstruction has therefore narrowed again. Deterministic Holder cancellation is sufficient after interior averaging, but direct pathwise Holder control of a raw centered Hessian edge fails. The skeleton-averaged theorem shows that the conditional-mean part can be summed absolutely. The remaining obstruction is the raw fluctuation around that interior average.

**References.** Deterministic cancellation is developed in [Holder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md) and [Parabolic Holder bound for the Hessian Duhamel operator](parabolic-holder-bound-for-hessian-duhamel-operator.md). Conditional means and fluctuations are defined in [Conditional expectation and fluctuations of random fields](conditional-expectation-and-fluctuations-of-random-fields.md). Fixed Holder and Besov norms are reviewed in [Parabolic Holder spaces](parabolic-holder-spaces.md) and [Besov spaces on the torus](besov-spaces-on-the-torus.md).

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

on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), in a sufficiently small smooth-data regime.

There exists a patch-first randomization of the full Duhamel expansion with the following properties:

1. maximal consecutive left-spine Hessian events are sampled and evaluated as complete multi-event patches;
2. conditional on the exposed patch skeleton, distinct side patches use independent auxiliary randomness, with the usual [importance-sampling compensators](importance-sampling-compensators.md);
3. the resulting infinite-depth random functional \(H_{\mathrm{patch}}(t,x)\) belongs to \(L^1\) for every finite horizon; and
4. its expectation equals the deterministic solution.

Unlike the skeleton-averaged theorem, the conjectural estimator retains random continuous marks inside the patches.

## Deterministic Holder cancellation is no longer the obstruction

Let

$$
K_r^{(k)}=\partial_x^{2k}P_r.
$$

Hermite centering gives

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

Hence, for \(0<\alpha<1\),

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
\mathbb E\left[|He_{2k}(Z)|\,|Z|^\alpha\right]
\leq
\sqrt{(2k)!}
\left(\mathbb E|Z|^{2\alpha}\right)^{1/2}.
\tag{3}
$$

For multiplication by a spatial profile \(B\),

$$
[K_R^{(k)},M_B]g(x)
=
R^{-k}
\mathbb E\Bigl[
He_{2k}(Z)
\bigl(B(x+\sqrt RZ)-B(x)\bigr)
 g(x+\sqrt RZ)
\Bigr],
\tag{4}
$$

so

$$
\lVert[K_R^{(k)},M_B]g\rVert_\infty
\leq
c_{2k,\alpha}
R^{-k+\alpha/2}
[B]_{C^\alpha}\lVert g\rVert_\infty.
\tag{5}
$$

Commuting derivative blocks through a length-\(m\) patch groups the edges into consecutive clusters. A cluster of length \(\ell\) has internal time-simplex factor

$$
\frac{R^{\ell-1}}{(\ell-1)!},
$$

which leaves

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
R^{-1+\alpha/2}.
\tag{6}
$$

The singularity in (6) is integrable and the coefficient is exponentially bounded in \(\ell\). The full commutator expansion contains at most \(2^m\) terms: \(2^{m-1}\) ordered compositions of the cluster lengths, together with one additional terminal choice for the innermost cluster. This is still geometric, not factorial.

Thus deterministic patches with uniformly controlled spatial \(C^\alpha\) side profiles have geometric-in-length bounds. The skeleton-averaged theorem packages the same principle more efficiently through the bounded parabolic Hessian Duhamel operator and a Catalan tree majorant.

## The old sup-norm counterexample does not survive Holder control

The smooth counterexample to an \(L^\infty\)-only side-profile estimate uses packets

$$
b_m(h-r,x)
=
-
\sum_{k=1}^m
\psi(N_k^2r)\cos(N_kx),
\qquad
N_k=2^kN_0,
$$

with disjoint time supports. Their sup norms remain bounded while the Hessian Duhamel contribution grows with \(m\). But

$$
[\cos(Nx)]_{C^\alpha}
\asymp N^\alpha,
$$

so

$$
\sup_s\lVert b_m(s,\cdot)\rVert_{C^\alpha}
\asymp
2^{\alpha m}.
\tag{7}
$$

The counterexample therefore escapes through its regularity norm and does not contradict deterministic Holder closure.

## Failure of direct pathwise random Holder control

For one raw centered Hessian edge define

$$
\widehat K_r f(x,Z)
=
\frac{He_2(Z)}r
\left[
f(x+\sqrt rZ)-f(x)
\right].
\tag{8}
$$

Its expected sup norm has the deterministic gain:

$$
\mathbb E
\lVert\widehat K_r f(\cdot,Z)\rVert_\infty
\leq
c_{2,\alpha}r^{-1+\alpha/2}[f]_{C^\alpha}.
\tag{9}
$$

The pathwise Holder seminorm does not. One only has

$$
[\widehat K_r f(\cdot,Z)]_{C^\alpha}
\leq
\frac{2|He_2(Z)|}{r}[f]_{C^\alpha}.
\tag{10}
$$

This loss is genuine. For

$$
f_N(x)=N^{-\alpha}\cos(Nx),
\qquad
N\asymp r^{-1/2},
$$

the \(C^\alpha\) norm stays of order one while the expected pathwise seminorm in (10) is of order \(r^{-1}\) on a Gaussian event of fixed positive probability. Hence no uniform \(r^{\alpha/2}\) gain holds in the operator norm of the raw edge on \(C^\alpha\).

Lowering the regularity exponent gives a translation gain but loses regularity at every edge. Iterating that estimate therefore creates a descending regularity ladder rather than a fixed function space.

The same high-frequency mechanism rules out a fixed same-regularity Besov repair. On a fixed Besov space \(B^s_{p,q}\), the translation difference \(f(\cdot+h)-f\) is not uniformly small on the unit ball as \(h\to0\): a frequency packet at scale \(|h|^{-1}\) keeps the operator norm bounded below. Passing from \(B^s_{p,q}\) to a lower exponent can recover a power of \(|h|\), but again spends regularity. Thus neither a fixed Holder space nor a fixed same-regularity Besov space closes the raw edge recursion.

## What C-prime settles

The [skeleton-averaged theorem](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md) never takes a pathwise function-space norm inside a patch. For a finite decorated skeleton \(S\), all continuous branch-time and Gaussian/Hermite variables are integrated first, producing a deterministic profile \(F_S\). These profiles lie in the parabolic Holder space

$$
X_{\alpha,T}
=
C^{\alpha/2,\alpha}([0,T]\times\mathbb T)
$$

and satisfy an absolutely summable Catalan majorant under an explicit smallness condition. Sampling only \(S\) therefore gives an unbiased \(L^1\) estimator.

This should not be phrased by first writing \(\mathbb E[H\mid S]\) for the unresolved raw infinite-patch functional: a measure-theoretic conditional expectation requires \(H\in L^1\), which is exactly what is unknown. At finite integrable cutoffs the conditional-expectation language is legitimate, and the limit is the deterministic interior-averaged profile \(F_S\).

The theorem proves that the **conditional-mean / interior-average part of the construction closes and is absolutely summable**. That part is no longer the open problem.

## Remaining obstruction: the raw fluctuation

For a finite cutoff where ordinary conditional expectation is defined, write

$$
H
=
\mathbb E[H\mid S]
+
R_S,
\qquad
\mathbb E[R_S\mid S]=0.
\tag{11}
$$

C-prime controls the first term after passing to the interior-averaged limit. Conjecture C asks for the full raw functional, so it still requires control of the centered fluctuation \(R_S\).

The current obstruction is precise: the \(L^1\) amplitude of the fluctuation cannot be propagated through the next Hessian edge by putting the raw field in one fixed Holder space, and the same high-frequency translation mechanism defeats a fixed same-regularity Besov norm. The fluctuation is centered, but absolute values erase that cancellation before the next edge can use it.

A proof of C must therefore exploit additional structure beyond a fixed pathwise regularity norm: for example a multiscale conditional cancellation, a martingale or square-function structure, a norm that records both scale and genealogy, or another way of postponing absolute values across several random edges. None of these is currently proved.

The conjecture remains open. C-prime gives an \(L^1\) unbiased estimator only after the interior patch fluctuations have been averaged away.