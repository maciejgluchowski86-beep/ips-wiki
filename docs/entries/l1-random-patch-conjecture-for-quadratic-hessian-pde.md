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

A previous obstruction showed that side-profile sup norms cannot control a spatially varying Hessian patch. That obstruction does **not** survive under a uniform positive spatial Holder bound. The audited deterministic estimate below shows that Holder cancellation changes the analytic problem: for deterministic side profiles with uniformly bounded \(C^\alpha\) norms, complete patches grow at most geometrically in their length. The unresolved issue is now recursive regularity and moment control for the *random* side-patch fields.

**References.** The Holder cancellation estimates are recorded in [Holder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md). Parabolic Holder norms are defined in [Parabolic Holder spaces](parabolic-holder-spaces.md). The conjecture and counterexample concern the patch construction developed in this project.

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

## Audited Holder cancellation

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

For \(k=1\), (2) is the short-edge improvement

$$
\lVert\partial_x^2P_rf\rVert_\infty
\leq
c_{2,\alpha}
 r^{-1+\alpha/2}[f]_{C^\alpha}.
\tag{4}
$$

The gain \(r^{\alpha/2}\) is exactly the gain obtained by subtracting the constant \(f(x)\) against the centered Hermite weight.

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

and the commutator has the exact increment representation

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

Apply (6) successively along a complete length-\(m\) patch. At each multiplier there are two choices: commute the current derivative block through the multiplier, thereby extending the block by the next Hessian edge, or stop the block by taking the commutator. Thus the resulting terms are indexed by ordered compositions

$$
m=\ell_1+\cdots+\ell_q.
\tag{9}
$$

A cluster of \(\ell\) consecutive Hessian edges has total heat time \(R\) and derivative operator \(K_R^{(\ell)}\). For fixed \(R\), the internal simplex of its \(\ell\) positive edge lengths has volume

$$
\frac{R^{\ell-1}}{(\ell-1)!}.
$$

Combining this factor with (8) leaves

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
R^{-1+\alpha/2}.
\tag{10}
$$

The singularity in (10) is integrable at zero. Moreover, by (3),

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
\leq
C_\alpha4^\ell.
\tag{11}
$$

The number of ordered compositions of \(m\) is \(2^{m-1}\). Thus neither the Hermite constants nor the cluster combinatorics reintroduce factorial growth.

The terminal cluster can be commuted all the way to the initial heat transfer. Its internal simplex gives an even better factor: after applying (2) to the terminal profile, the remaining total-time factor is of order \(R^{\alpha/2}/\ell!\), rather than \(R^{-1+\alpha/2}/(\ell-1)!\).

## Proposition: deterministic Holder patch bound

Fix \(0<\alpha<1\) and \(T>0\). There is a constant \(C_{\alpha,T}<\infty\) such that the complete length-\(m\) patch contribution \(\mathcal P_m\) from [Finite-depth Duhamel patch regrouping](finite-depth-duhamel-patch-regrouping.md) satisfies the following bound.

If

$$
G\in C^\alpha(\mathbb T)
$$

and the side profiles obey

$$
\sup_{1\leq j\leq m}
\sup_{0\leq s\leq T}
\lVert b_j(s,\cdot)\rVert_{C^\alpha}
\leq M,
\tag{12}
$$

then

$$
\sup_{0\leq t\leq T}
\lVert\mathcal P_m[b_1,\ldots,b_m;G](t)\rVert_\infty
\leq
\lVert G\rVert_{C^\alpha}
\bigl(|\lambda|C_{\alpha,T}\max\{1,M\}\bigr)^m.
\tag{13}
$$

### Proof

Expand the patch by repeated use of (6). Every term corresponds to a composition (9). Multipliers passed without a commutator contribute only their sup norms. Each nonterminal cluster ends at one commutator and contributes one spatial Holder seminorm together with the integrable time factor (10). The terminal cluster either ends at a commutator, leaving a heat-semigroup contraction on \(G\), or reaches \(G\) and uses the terminal Holder gain described above.

For a nonterminal cluster, integrating \(R^{-1+\alpha/2}\) over \((0,T]\) costs at most \(2T^{\alpha/2}/\alpha\). By (11), the remaining length-dependent coefficient is bounded by a fixed exponential in the cluster length. The terminal-cluster coefficient has the same property. Since the cluster lengths sum to \(m\), products of the cluster coefficients are bounded by \(C_{\alpha,T}^m\). Finally, there are at most \(2^{m-1}\) compositions. Absorbing this factor and the \(C^\alpha\) bounds of the multipliers into a larger value of \(C_{\alpha,T}\) gives (13).

The proposition is deterministic. It does not estimate the Holder norms of the random side-patch fields generated by a branching construction.

## Why the sup-norm counterexample does not contradict the Holder bound

For \(h>0\), define

$$
(\mathcal K_h b)(x)
=
\int_0^h
\partial_x^2P_r[b(h-r,\cdot)](x)\,dr.
\tag{14}
$$

The smooth high-frequency counterexample is built from time-frequency packets

$$
b_m(h-r,x)
=
-
\sum_{k=1}^m
\psi(N_k^2r)\cos(N_kx),
\qquad
N_k=2^kN_0,
\tag{15}
$$

with \(\psi\in C_c^\infty((1,2))\). The temporal supports are disjoint, so

$$
\lVert b_m\rVert_\infty\leq1,
$$

while

$$
(\mathcal K_hb_m)(0)
=
m\int_1^2\psi(q)e^{-q/2}\,dq
\longrightarrow\infty.
\tag{16}
$$

However,

$$
[\cos(Nx)]_{C^\alpha}
\asymp N^\alpha.
\tag{17}
$$

At a time when the highest-frequency packet in (15) is active, (17) gives

$$
\sup_s[b_m(s,\cdot)]_{C^\alpha}
\geq
c_{\alpha,\psi}N_m^\alpha.
$$

Conversely, summing the Holder bounds of the finitely many packets gives an upper bound of the same order. Hence

$$
\sup_s\lVert b_m(s,\cdot)\rVert_{C^\alpha}
\asymp
N_m^\alpha
\asymp
2^{\alpha m}.
\tag{18}
$$

The full parabolic \(C^{\alpha/2,\alpha}\) norm has the same scaling because the time localization occurs at scale \(N_k^{-2}\); see [Parabolic Holder spaces](parabolic-holder-spaces.md). Thus the counterexample escapes the Holder estimate precisely by making its regularity norm diverge.

## The obstruction has changed character

The deterministic estimate (13) removes the earlier factorial/Hermite obstruction for patches whose side profiles have uniformly controlled spatial Holder norms. The open problem is therefore no longer to tame a deterministic factorial growth produced by consecutive Hessian transfers. It is to control the *random regularity* of the side patches strongly enough that the geometric deterministic majorant can be averaged recursively.

A sufficient route would be a recursive moment estimate for random side fields in a norm such as

$$
L^p\bigl(\Omega;L^\infty([0,T];C^\alpha(\mathbb T))\bigr),
$$

or in a suitable parabolic Holder or Besov-type space. Which norm is natural is itself part of the problem.

Full pathwise parabolic Holder regularity should not be assumed automatically. In a naive common-randomness coupling across the horizon variable, the realized branching topology can change when a sampled lifetime crosses the observation horizon, producing time discontinuities of the raw estimator. The commutator argument above only needs spatial \(C^\alpha\) control at the sampled branch times. An averaged, integrated, or Besov regularity norm may therefore be more appropriate than a pathwise \(C^{\alpha/2,\alpha}\) norm.

The conjecture remains open until such random function-space estimates are proved and shown to be summable over the patch genealogy.