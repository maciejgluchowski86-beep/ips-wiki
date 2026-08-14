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

The quadratic Hessian route has several proved layers below the full random-patch problem. Finite Duhamel trees regroup exactly into patches; the deterministic semi-implicit iteration converges in a small uniformly parabolic regime; and, under an explicit Catalan smallness condition, [Theorem C-prime](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md) gives an unbiased \(L^1\) estimator after **all continuous randomness inside each decorated skeleton has been averaged out**.

The conjecture on this page is stronger. It asks whether one can retain the genuinely random Gaussian/Hermite, branch-time, and descendant marks inside the patches and still obtain an \(L^1\) unbiased estimator. That remains open.

The negative information is now substantial. Fixed pathwise Hölder and fixed same-regularity Besov norms fail. The [Banach-scale obstruction](banach-scale-obstruction-for-raw-pde-patches.md) rules out every stepwise first-moment Hölder-scale proof with a bounded cumulative regularity loss. The [joint centered-mark dichotomy](joint-centered-mark-dichotomy-for-raw-pde-patches.md) shows that postponing the first absolute value across an entire block really does evade that stepwise theorem, but creates a new split: if all Gaussian marks are retained, the optimal uniform block norm is factorial in the block length; if the internal Gaussian bridge marks are signedly averaged first, the coefficient becomes geometric, but the resulting representation is only partially random and no longer satisfies the literal retention clause of this conjecture.

Thus no settled theorem currently proves or disproves C. The accumulated barriers constrain what either outcome would have to look like. The [PDE branching-representations overview](../pde-branching-representations.md) gives the section-level map.

**References.** Deterministic cancellation is developed in [Hölder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md) and [Parabolic Hölder bound for the Hessian Duhamel operator](parabolic-holder-bound-for-hessian-duhamel-operator.md). Conditional means and fluctuations are defined in [Conditional expectation and fluctuations of random fields](conditional-expectation-and-fluctuations-of-random-fields.md). Hölder and Besov spaces are reviewed in [Parabolic Hölder spaces](parabolic-holder-spaces.md) and [Besov spaces on the torus](besov-spaces-on-the-torus.md).

## Concrete open problem

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

Let

$$
X_{\alpha,T}=C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
\qquad
M=\|P_\cdot\phi''\|_{X_{\alpha,T}},
$$

and let \(C_{\mathcal D}(\alpha,T)\) be the operator constant from the [Hessian Duhamel bound](parabolic-holder-bound-for-hessian-duhamel-operator.md). Assume the explicit C-prime smallness condition

$$
4|\lambda|C_{\mathcal D}(\alpha,T)M<1.
\tag{1}
$$

Under (1), Theorem C-prime constructs the unique small fixed point \(z_*\in X_{\alpha,T}\) of

$$
z_*(t)
=
P_t\phi''
+
\lambda\int_0^t
\partial_x^2P_{t-s}[z_*(s)^2]\,ds
\tag{2}
$$

inside its Catalan fixed-point ball, together with an unbiased skeleton-only \(L^1\) estimator.

## Conjecture C

Under the hypotheses above, there exists a patch-first randomization of the full Hessian Duhamel expansion with the following properties:

1. maximal consecutive left-spine Hessian events are sampled and evaluated as complete multi-event patches;
2. conditional on the exposed patch skeleton, distinct side patches use independent auxiliary randomness, with the usual [importance-sampling compensators](importance-sampling-compensators.md);
3. the continuous Gaussian/Hermite, branch-time, and descendant marks inside the patches are **retained as random variables rather than deterministically integrated out**;
4. the resulting infinite-depth random functional \(H_{\mathrm{patch}}(t,x)\) belongs to \(L^1\) for every \((t,x)\in[0,T]\times\mathbb T\); and
5. its expectation is the C-prime solution profile,
   $$
   \mathbb E[H_{\mathrm{patch}}(t,x)]
   =
   z_*(t,x).
   \tag{3}
   $$

The retention clause in item 3 is part of the conjecture, not optional terminology. A representation that integrates out some or all of those continuous interior variables can be useful and can be unbiased, but it is a different statement. In particular, Theorem C-prime and the bridge-averaged branch below do not prove C.

The conjecture is already meaningful on the explicit proved small-data regime (1). It may ultimately hold on a larger regime, but no such extension is part of the present claim.

## Deterministic Hölder cancellation is no longer the obstruction

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
\tag{4}
$$

Hence, for \(0<\alpha<1\),

$$
\|K_r^{(k)}f\|_\infty
\leq
c_{2k,\alpha}
r^{-k+\alpha/2}[f]_{C^\alpha},
\tag{5}
$$

where

$$
c_{2k,\alpha}
=
\mathbb E\left[|He_{2k}(Z)|\,|Z|^\alpha\right]
\leq
\sqrt{(2k)!}
\left(\mathbb E|Z|^{2\alpha}\right)^{1/2}.
\tag{6}
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
\tag{7}
$$

so

$$
\|[K_R^{(k)},M_B]g\|_\infty
\leq
c_{2k,\alpha}
R^{-k+\alpha/2}
[B]_{C^\alpha}\|g\|_\infty.
\tag{8}
$$

Commuting derivative blocks through a length-\(m\) deterministic patch groups the edges into consecutive clusters. A cluster of length \(\ell\) has internal time-simplex factor

$$
\frac{R^{\ell-1}}{(\ell-1)!},
$$

which leaves

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
R^{-1+\alpha/2}.
\tag{9}
$$

The singularity is integrable and the coefficient is exponentially bounded in \(\ell\). The full commutator expansion contains at most \(2^m\) terms: \(2^{m-1}\) ordered compositions of the cluster lengths, together with one additional terminal choice for the innermost cluster. Thus deterministic patches with uniformly controlled spatial \(C^\alpha\) side profiles have geometric-in-length bounds.

Theorem C-prime packages the same cancellation through the bounded parabolic Hessian Duhamel operator and a Catalan majorant. Consequently deterministic Hölder/Hermite growth is not the current obstruction.

## The old sup-norm counterexample does not survive Hölder control

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
[\cos(Nx)]_{C^\alpha}\asymp N^\alpha,
$$

so

$$
\sup_s\|b_m(s,\cdot)\|_{C^\alpha}
\asymp 2^{\alpha m}.
\tag{10}
$$

The counterexample therefore escapes through its regularity norm and does not contradict deterministic Hölder closure.

## Route 1: direct pathwise random Hölder and Besov control fails

For one raw centered Hessian edge define

$$
\widehat K_r f(x,Z)
=
\frac{He_2(Z)}r
\left[
f(x+\sqrt rZ)-f(x)
\right].
\tag{11}
$$

Its expected sup norm has the deterministic gain:

$$
\mathbb E
\|\widehat K_r f(\cdot,Z)\|_\infty
\leq
c_{2,\alpha}r^{-1+\alpha/2}[f]_{C^\alpha}.
\tag{12}
$$

The pathwise Hölder seminorm does not. One only has

$$
[\widehat K_r f(\cdot,Z)]_{C^\alpha}
\leq
\frac{2|He_2(Z)|}{r}[f]_{C^\alpha}.
\tag{13}
$$

This loss is genuine. For

$$
f_N(x)=N^{-\alpha}\cos(Nx),
\qquad
N\asymp r^{-1/2},
$$

the \(C^\alpha\) norm stays of order one while the expected pathwise seminorm is of order \(r^{-1}\) on a Gaussian event of fixed positive probability. Hence no uniform \(r^{\alpha/2}\) gain holds in the operator norm of the raw edge on \(C^\alpha\).

A fixed same-regularity Besov norm has the same obstruction: the translation difference \(f(\cdot+h)-f\) is not uniformly small on the unit ball at frequencies of order \(|h|^{-1}\). Thus retaining the raw mark while taking a fixed pathwise Hölder or same-regularity Besov norm does not close the recursion.

## Route 2: decreasing exponents do not repair a stepwise first-moment proof

One may try to spend a small amount of regularity at each generation. Put \(\beta=\alpha-\delta\). The translation estimate

$$
[\tau_hf-f]_{C^\beta}
\lesssim
|h|^\delta[f]_{C^\alpha}
$$

gives

$$
\mathbb E
[\widehat K_r f]_{C^\beta}
\lesssim
r^{-1+\delta/2}[f]_{C^\alpha}.
\tag{14}
$$

After integration over one edge, this costs order \(1/\delta\). The Banach-scale theorem proves that the cost is sharp. If

$$
\alpha_0>\alpha_1>\cdots>\alpha_n,
\qquad
\delta_k=\alpha_{k-1}-\alpha_k,
\qquad
\sum_{k=1}^n\delta_k\leq\Delta,
$$

then any proof that takes a first-moment Hölder norm after every centered edge and bounds each edge uniformly over the current Banach-space unit ball necessarily incurs

$$
\prod_{k=1}^n\frac{c}{\delta_k}
\geq
c^n\left(\frac n\Delta\right)^n.
\tag{15}
$$

The uniform budget \(\delta_k=\Delta/n\) minimizes this product; geometric and other nonuniform budgets are worse. Preserving the chronological time simplex does not restore an \(n!\) gain.

This is a proof-architecture barrier, not a disproof of C. The one-edge test saturating the \(1/\delta\) cost uses frequency

$$
N\asymp e^{c/\delta}.
$$

At depth \(n\), the worst-case frequency therefore changes with \(n\). No fixed smooth terminal datum is shown to realize these operator norms at all depths.

The theorem rules out the bare loss-of-derivatives budget by itself. It does not exclude every genuine Nash--Moser smoothing/telescoping scheme, because a frequency-aware correction mechanism falls outside its stepwise uniform-norm hypothesis.

## Route 3: conditioning all interiors gives C-prime, not raw C

The [skeleton-averaged theorem](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md) never takes a pathwise function-space norm inside a patch. For a finite decorated skeleton \(S\), all continuous branch-time, Gaussian/Hermite, and descendant variables are integrated first, producing a deterministic profile \(F_S\). These profiles lie in \(X_{\alpha,T}\) and satisfy an absolutely summable Catalan majorant under (1). Sampling only \(S\) therefore gives an unbiased \(L^1\) estimator.

This must not be phrased by first writing \(\mathbb E[H\mid S]\) for the unresolved raw infinite-patch functional: a measure-theoretic conditional expectation requires \(H\in L^1\), which is exactly what is unknown. At finite integrable cutoffs the conditional-expectation language is legitimate, and the limit is the deterministic interior-averaged profile \(F_S\).

Thus C-prime establishes the integrable side of the tradeoff only after giving up all continuous interior randomness. It is strictly weaker than C.

## Route 4: joint centered marks replace the derivative ladder by a factorial barrier

The [joint centered-mark theorem](joint-centered-mark-dichotomy-for-raw-pde-patches.md) tests the most direct way to postpone absolute values while keeping several centered Gaussian marks together.

For positive durations \(r_1,\ldots,r_m\), independent \(Z_1,\ldots,Z_m\), and \(h_j=\sqrt{r_j}Z_j\), the retained centered bare block is

$$
\widehat{\mathcal K}_{\mathbf r}^{\mathrm{raw}}f
=
\left(
\prod_{j=1}^m\frac{He_2(Z_j)}{r_j}
\right)
\Delta_{h_m}\cdots\Delta_{h_1}f.
\tag{16}
$$

The two-mark block has a genuine same-input-regularity estimate after the joint contribution is formed:

$$
\int_{r_1+r_2<T}
\mathbb E
\left\|
\widehat{\mathcal K}_{(r_1,r_2)}^{\mathrm{raw}}f
\right\|_\infty
\,dr_1dr_2
\leq
C_{\alpha,T}[f]_{C^\alpha}.
\tag{17}
$$

No intermediate Hölder norm and no regularity-loss parameter is used. This genuinely escapes the hypothesis of the Banach-scale barrier, which requires a first-moment Banach norm after every centered edge.

At arbitrary block length, however, the optimal uniform retained-mark block norm satisfies

$$
c_{\alpha,T}^m m!
\leq
\mathfrak R_m(\alpha,T)
\leq
C_{\alpha,T}^m m!.
\tag{18}
$$

Thus full Gaussian mark retention replaces the descending regularity ladder by factorial block growth. The lower bound again uses an \(m\)-dependent frequency,

$$
N_m\asymp\sqrt{m/T}\,e^{m/\alpha},
$$

so (18) is not a fixed-datum non-\(L^1\) theorem.

There is a sharply different branch if the internal Gaussian bridge coordinates are signedly averaged before the absolute value. For a bare derivative chain, if

$$
Y=\sum_{j=1}^m\sqrt{r_j}Z_j,
\qquad
R=\sum_{j=1}^m r_j,
\qquad
Z=Y/\sqrt R,
$$

then

$$
\mathbb E\left[
\left.
\prod_{j=1}^m\frac{He_2(Z_j)}{r_j}
\right|Y
\right]
=
\frac{He_{2m}(Z)}{R^m}.
\tag{19}
$$

The fixed-\(R\) time simplex contributes \(R^{m-1}/(m-1)!\), so the Hölder coefficient is bounded by

$$
C_{\alpha,T}
\frac{\sqrt{(2m)!}}{(m-1)!}
\leq
C_{\alpha,T}4^m.
\tag{20}
$$

For spatially varying patches, the exact one-Hermite collapse is replaced by the already proved commutator/cluster decomposition, which also has geometric-in-length growth under uniform spatial Hölder control of the side profiles.

The favorable branch (19)--(20) is **not C in disguise**. It integrates out \(m-1\) Gaussian bridge coordinates. An endpoint Gaussian remains random, but the original continuous interior marks are no longer all retained, violating item 3 of the conjecture. It is a partially averaged representation between raw C and the completely interior-averaged C-prime estimator.

## The four-route map

The fluctuation problem has now been attacked in four structurally different ways, and each has isolated a different boundary.

1. **Fixed pathwise Hölder/Besov control:** keeps the raw marks, but same-space first-moment regularity fails already at one centered edge.
2. **Decreasing Banach scale:** keeps the raw marks and spends regularity, but the sharp one-edge \(1/\delta\) cost forces at least \((c n/\Delta)^n\) in every stepwise first-moment loss-budget proof.
3. **Condition all patch interiors:** gives absolute summability and an unbiased \(L^1\) estimator by C-prime, but removes the continuous interior marks completely.
4. **Joint centered blocks:** genuinely avoids the stepwise derivative-loss hypothesis; retaining all Gaussian marks gives sharp factorial \(m!\) block growth, while signed bridge averaging restores geometric growth only by removing part of the Gaussian interior randomness.

These routes repeatedly expose the same tradeoff: the currently controlled constructions have either favorable absolute moments or full continuous interior randomness, but not both. This is evidence about the difficulty of C, not a theorem that C is false.

## Current status: proof and disproof criteria

Conjecture C remains open. The current research direction is to test whether the conjecture itself may be false, rather than continuing to search only for another uniform first-moment proof architecture. No disproof is recorded here.

A genuine **disproof** must overcome the caveat shared by the Banach-scale and retained-block lower bounds: their worst-case frequencies depend on the generation or block length. It would need, for example, one fixed smooth datum for which the actual raw patch estimator has infinite absolute expectation, or another argument that yields non-\(L^1\) without changing the datum with depth.

A genuine **proof** must evade all four settled routes without averaging away the marks required by item 3. It would have to preserve additional structure before taking absolute values: frequency together with genealogy, correlations between distinct patches, a martingale or square-function mechanism, or multi-mark cancellation that remains available while the marks themselves stay random.

Either outcome would change the status of this page. Until such a result is audited, the status remains `conjecture`.

## Conditional-mean decomposition and the remaining raw fluctuation

At a finite cutoff where ordinary conditional expectation is defined, one may write

$$
H
=
\mathbb E[H\mid S]
+
R_S,
\qquad
\mathbb E[R_S\mid S]=0.
\tag{21}
$$

C-prime controls the first term after passing to the deterministic interior-averaged limit. C asks for the full raw functional, so the centered fluctuation \(R_S\) remains the object whose absolute moments must ultimately be understood.

The settled results do not prove that \(R_S\) has infinite absolute expectation for a fixed smooth datum. They show instead that four natural ways of discarding structure before the first absolute moment are insufficient. The present open problem is therefore no longer merely “find a better Hölder norm”; it is to determine whether the required full-randomness \(L^1\) representation exists at all.