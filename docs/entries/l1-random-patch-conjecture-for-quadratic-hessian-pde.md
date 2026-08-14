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

The conjecture on this page is stronger. It asks whether one can retain the genuinely random Gaussian/Hermite and descendant marks inside the patches and still obtain an \(L^1\) unbiased estimator. That remains open.

The analytic obstruction has narrowed substantially. Deterministic Holder cancellation is sufficient after interior averaging, but direct pathwise Holder control of a raw centered Hessian edge fails. A fixed same-regularity Besov norm also fails. The new [Banach-scale obstruction](banach-scale-obstruction-for-raw-pde-patches.md) shows that simply descending through Hölder exponents does not repair the problem either: spending a regularity increment \(\delta\) costs sharply \(1/\delta\) at one edge, and any fixed total loss budget \(\Delta\) produces at least \((c n/\Delta)^n\) in a stepwise first-moment argument after \(n\) generations. C-prime shows that the interior-average part can nevertheless be summed absolutely. The remaining obstruction is the raw fluctuation around that interior average. The full fork is summarized in the [PDE branching-representations overview](../pde-branching-representations.md).

**References.** Deterministic cancellation is developed in [Holder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md) and [Parabolic Holder bound for the Hessian Duhamel operator](parabolic-holder-bound-for-hessian-duhamel-operator.md). Conditional means and fluctuations are defined in [Conditional expectation and fluctuations of random fields](conditional-expectation-and-fluctuations-of-random-fields.md). Fixed Holder and Besov norms are reviewed in [Parabolic Holder spaces](parabolic-holder-spaces.md) and [Besov spaces on the torus](besov-spaces-on-the-torus.md).

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

## Conjecture

Under the hypotheses above, there exists a patch-first randomization of the full Hessian Duhamel expansion with the following properties:

1. maximal consecutive left-spine Hessian events are sampled and evaluated as complete multi-event patches;
2. conditional on the exposed patch skeleton, distinct side patches use independent auxiliary randomness, with the usual [importance-sampling compensators](importance-sampling-compensators.md);
3. the continuous Gaussian/Hermite, branch-time, and descendant marks inside the patches are retained rather than deterministically integrated out;
4. the resulting infinite-depth random functional \(H_{\mathrm{patch}}(t,x)\) belongs to \(L^1\) for every \((t,x)\in[0,T]\times\mathbb T\); and
5. its expectation is the C-prime solution profile,
   $$
   \mathbb E[H_{\mathrm{patch}}(t,x)]
   =
   z_*(t,x).
   \tag{3}
   $$

Thus the conjecture is already meaningful on the explicit proved small-data regime (1). It may ultimately hold on a larger regime, but no such extension is part of the present claim.

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
\tag{4}
$$

Hence, for \(0<\alpha<1\),

$$
\lVert K_r^{(k)}f\rVert_\infty
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
\lVert[K_R^{(k)},M_B]g\rVert_\infty
\leq
c_{2k,\alpha}
R^{-k+\alpha/2}
[B]_{C^\alpha}\lVert g\rVert_\infty.
\tag{8}
$$

Commuting derivative blocks through a length-\(m\) patch groups the edges into consecutive clusters. A cluster of length \(\ell\) has internal time-simplex factor

$$
\frac{R^{\ell-1}}{(\ell-1)!},
$$

which leaves

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
R^{-1+\alpha/2}.
\tag{9}
$$

The singularity in (9) is integrable and the coefficient is exponentially bounded in \(\ell\). The full commutator expansion contains at most \(2^m\) terms: \(2^{m-1}\) ordered compositions of the cluster lengths, together with one additional terminal choice for the innermost cluster. This is still geometric, not factorial.

Thus deterministic patches with uniformly controlled spatial \(C^\alpha\) side profiles have geometric-in-length bounds. C-prime packages the same principle more efficiently through the bounded parabolic Hessian Duhamel operator and a Catalan tree majorant.

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
\tag{10}
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
\tag{11}
$$

Its expected sup norm has the deterministic gain:

$$
\mathbb E
\lVert\widehat K_r f(\cdot,Z)\rVert_\infty
\leq
c_{2,\alpha}r^{-1+\alpha/2}[f]_{C^\alpha}.
\tag{12}
$$

The pathwise Holder seminorm does not. One only has

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

the \(C^\alpha\) norm stays of order one while the expected pathwise seminorm in (13) is of order \(r^{-1}\) on a Gaussian event of fixed positive probability. Hence no uniform \(r^{\alpha/2}\) gain holds in the operator norm of the raw edge on \(C^\alpha\).

The same high-frequency mechanism rules out a fixed same-regularity Besov repair. On a fixed Besov space \(B^s_{p,q}\), the translation difference \(f(\cdot+h)-f\) is not uniformly small on the unit ball as \(h\to0\): a frequency packet at scale \(|h|^{-1}\) keeps the operator norm bounded below. Thus neither a fixed Holder space nor a fixed same-regularity Besov space closes the raw edge recursion.

## Decreasing exponents do not repair the stepwise first-moment argument

One might try to spend a small amount of regularity at each generation. Put \(\beta=\alpha-\delta\). The translation estimate

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

After integration over one edge, this costs order \(1/\delta\). The [Banach-scale obstruction theorem](banach-scale-obstruction-for-raw-pde-patches.md) proves that this cost is sharp. More precisely, if

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

The uniform budget \(\delta_k=\Delta/n\) minimizes this product; a geometric or other nonuniform budget is worse. Preserving the chronological time simplex does not restore an \(n!\) gain: the corresponding Dirichlet integral contains \(\prod_k\Gamma(\delta_k/2)\), which has the same \(\prod_k\delta_k^{-1}\) singularity.

Thus the bare Nash--Moser-style idea of repairing the fluctuation problem only by descending through a fixed total Hölder regularity budget fails. This statement is deliberately scoped. The theorem does **not** exclude every genuine Nash--Moser smoothing scheme: a smoothing/telescoping construction that retains frequency information and compensates smoothing errors is outside the stepwise uniform first-moment architecture.

The lower bound also does not imply divergence of the raw estimator. The one-edge test that saturates the \(1/\delta\) cost uses frequency

$$
N\asymp e^{c/\delta}.
$$

Under the optimal depth-\(n\) budget \(\delta\asymp\Delta/n\), the saturating frequency therefore grows like \(e^{cn/\Delta}\). The test datum changes with the generation/depth. No fixed smooth terminal datum is shown to realize these worst-case operator norms at all depths, so (15) is a barrier to a proof architecture, not a counterexample to conjecture C.

## What C-prime settles

The [skeleton-averaged theorem](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md) never takes a pathwise function-space norm inside a patch. For a finite decorated skeleton \(S\), all continuous branch-time and Gaussian/Hermite variables are integrated first, producing a deterministic profile \(F_S\). These profiles lie in the parabolic Holder space \(X_{\alpha,T}\) and satisfy an absolutely summable Catalan majorant under (1). Sampling only \(S\) therefore gives an unbiased \(L^1\) estimator.

This should not be phrased by first writing \(\mathbb E[H\mid S]\) for the unresolved raw infinite-patch functional: a measure-theoretic conditional expectation requires \(H\in L^1\), which is exactly what is unknown. At finite integrable cutoffs the conditional-expectation language is legitimate, and the limit is the deterministic interior-averaged profile \(F_S\).

The theorem proves that the **interior-average part of the construction closes and is absolutely summable**. That part is no longer the open problem.

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
\tag{16}
$$

C-prime controls the first term after passing to the interior-averaged limit. Conjecture C asks for the full raw functional, so it still requires control of the centered fluctuation \(R_S\).

The current negative information is now layered:

- a fixed pathwise Holder norm fails at one centered Hessian edge;
- a fixed same-regularity Besov norm has the same high-frequency translation obstruction;
- lowering the Hölder exponent at every edge with any fixed total regularity budget gives the sharp supergeometric barrier \((c n/\Delta)^n\) for every stepwise first-moment Banach-scale argument.

These results do not show that \(R_S\) itself has infinite absolute expectation for a fixed smooth datum. They show instead that a successful proof must preserve more structure before taking absolute values. Candidate escape mechanisms include retaining frequency together with genealogy, using a multiscale martingale or square-function structure, or allowing cancellation across several centered Gaussian/Hermite marks before taking a first-moment norm. None of these routes is currently proved.

The conjecture remains open. C-prime gives an \(L^1\) unbiased estimator only after the interior patch fluctuations have been averaged away.
