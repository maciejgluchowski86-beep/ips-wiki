---
title: Time-spine coarsening for quadratic Hessian patches
status: proved here
tags:
  - PDE
  - patch
  - coarsening
  - integrability
  - total variation
  - Hessian
---

# Time-spine coarsening for quadratic Hessian patches

The coarsening problem for the quadratic Hessian equation has a genuine intermediate positive regime. Complete interior averaging is not the only way to recover an integrable representation.

This entry proves two complementary statements.

1. A naive patchwise Gaussian-bridge coarsening does **not** repair the fixed-datum raw obstruction. The obstruction may be realized on right-oriented combs, and under the established convention that patches are maximal left-child chains every internal vertex of a right comb is a one-edge patch. A one-edge bridge map has no bridge coordinate to remove, so the raw comb total variation is unchanged.
2. A different coarsening is integrable. For each finite tree, retain the ordered branch times on its root maximal-left spine, and average every Gaussian/Brownian mark and every continuous variable inside the side subtrees. Under an explicit smallness condition obtained from a geometric patch estimate and the Catalan side-subtree sum, the resulting coarsened signed measures have summable total variation. Sampling them gives an unbiased \(L^1\) estimator which genuinely retains continuous branch-time randomness.

The second theorem lies strictly between the raw-faithful endpoint and Theorem C-prime at the level of retained information. It does not retain the raw Hessian Gaussian marks.

**References.** The finite patch convention is in [Finite-depth Duhamel patch regrouping](finite-depth-duhamel-patch-regrouping.md). The geometric derivative-cluster estimate is in [Holder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md) and [Joint centered-mark dichotomy for raw PDE patches](joint-centered-mark-dichotomy-for-raw-pde-patches.md). The Catalan tree bound is in [Skeleton-averaged L1 representation for the quadratic Hessian PDE](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md). The fixed-datum lower bound is in [Raw-barycenter L1 obstruction for the quadratic Hessian PDE](raw-marked-l1-obstruction-for-quadratic-hessian-pde.md). The results below are proved here.

## Setup

Fix

$$
0<\alpha<1,
\qquad
T>0,
\qquad
\lambda\in\mathbb R,
\qquad
\phi\in C^{2+\alpha}(\mathbb T),
$$

where

$$
\mathbb T=\mathbb R/(2\pi\mathbb Z).
$$

Let

$$
z(t)
=
P_t\phi''
+
\lambda\int_0^t
\partial_x^2P_{t-s}[z(s)^2]\,ds.
$$

Write

$$
X=X_{\alpha,T}
=C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
\qquad
L=P_\cdot\phi'',
\qquad
M=\|L\|_X.
$$

Let \(C_{\mathcal D}=C_{\mathcal D}(\alpha,T)\) be a valid constant in

$$
\|\mathcal D(fg)\|_X
\le
C_{\mathcal D}\|f\|_X\|g\|_X,
$$

and put

$$
a
=
|\lambda|C_{\mathcal D}M.
\tag{1}
$$

For a finite planar full binary tree \(	au\), let \(F_\tau\) be its deterministic Duhamel profile. If \(|\tau|=n\) is its number of internal vertices, then

$$
\|F_\tau\|_X
\le
Ma^n.
\tag{2}
$$

Let \(\mu_\tau^{t,x}\) be the intrinsic signed measure on the canonical raw interior-mark space of \(	au\). Its total mass is \(F_\tau(t,x)\).

## Why the naive Gaussian-bridge coarsening misses the obstruction

A patch is, by convention, a maximal chain obtained by repeatedly following the **left** child.

A *right comb of length \(m\)* is the planar binary tree whose right child continues through exactly \(m\) internal vertices, while the left child at every one of those vertices is a leaf; after the \(m\)-th vertex the right child is also a leaf.

### Lemma: right combs have only one-edge patches

Every patch of a right comb has length one.

### Proof

At every internal vertex of the right comb, the left child is a leaf. Hence the maximal chain obtained by following left children stops immediately. Every internal vertex is therefore the first and last vertex of its own maximal-left patch. Different vertices lie in different patches because every continuing internal child is a right child. \(\square\)

The long-comb lower bound in the raw-barycenter obstruction may be realized on these right combs. The quadratic product is symmetric in its two children, so choosing the continuing child to be the right child does not change the signed comb calculation: the side leaf still carries frequency \(1\), the distinguished terminal leaf carries the frequency \(N_m\), and the same successive multipliers \(N_m+1,\ldots,N_m+m\) appear.

Define the *naive patchwise Gaussian-bridge coarsening* to act separately on every maximal-left patch: for a patch with durations \(r_1,\ldots,r_\ell\) and Gaussian increments \(Z_1,\ldots,Z_\ell\), retain the endpoint Gaussian coordinate

$$
Z_{\mathrm{end}}
=
\frac{\sum_{j=1}^\ell\sqrt{r_j}Z_j}
{\sqrt{r_1+\cdots+r_\ell}}
$$

and forget the \(\ell-1\) orthogonal bridge coordinates, while leaving the other raw coordinates unchanged.

For \(\ell=1\),

$$
Z_{\mathrm{end}}=Z_1.
$$

Thus the bridge map is literally the identity on the Gaussian coordinate of a one-edge patch. If one uses the unnormalised endpoint displacement instead, the map \(Z_1\mapsto\sqrt{r_1}Z_1\) is invertible once the retained duration \(r_1\) is known, so total variation is again unchanged.

### Corollary: patchwise bridge coarsening is nonintegrable on the fixed datum

Let \(\phi_\varepsilon\) be the single smooth datum from the raw-barycenter obstruction. On the right-comb cylinders \(\Gamma_m\), naive patchwise Gaussian-bridge coarsening leaves the intrinsic signed measure unchanged up to an invertible coordinate change. Consequently

$$
\|(\mathcal C_{\Gamma_m}^{\mathrm{bridge}})_\#\mu_m\|_{\mathrm{TV}}
=
\|\mu_m\|_{\mathrm{TV}},
$$

and therefore

$$
\sum_m
\|(\mathcal C_{\Gamma_m}^{\mathrm{bridge}})_\#\mu_m\|_{\mathrm{TV}}
=
\infty.
\tag{3}
$$

Hence the naive patchwise bridge scheme does not give an \(L^1\) representation for that fixed smooth datum.

This failure is combinatorial rather than quantitative: the obstruction genealogy never presents the bridge map with a patch containing two Gaussian edges.

## Absolute time integral of one deterministic patch

For \(m\ge1\), let

$$
0<s_1<\cdots<s_m<t\le T.
$$

Given \(G\in C^\alpha(\mathbb T)\) and side profiles \(b_1,\ldots,b_m\in X\), define

$$
\Xi_1
=
b_1(s_1)P_{s_1}G,
$$

and, for \(2\le r\le m\),

$$
\Xi_r
=
b_r(s_r)
\partial_x^2P_{s_r-s_{r-1}}\Xi_{r-1}.
$$

Write

$$
I_m[b_1,\ldots,b_m;G](t,x;\mathbf s)
=
\partial_x^2P_{t-s_m}\Xi_m(x).
\tag{4}
$$

Thus the complete deterministic patch contribution is

$$
\lambda^m
\int_{0<s_1<\cdots<s_m<t}
I_m(t,x;\mathbf s)\,d\mathbf s.
$$

Define the normalized absolute-time constant

$$
\mathfrak P_m(\alpha,T)
=
\sup
\frac{
\displaystyle
\sup_{0\le t\le T}\sup_{x\in\mathbb T}
\int_{0<s_1<\cdots<s_m<t}
|I_m(t,x;\mathbf s)|\,d\mathbf s
}{
\|G\|_{C^\alpha}
\prod_{j=1}^m\|b_j\|_X
},
\tag{5}
$$

where the supremum is over nonzero \(G,b_1,\ldots,b_m\). Finally set

$$
K_{\mathrm{time}}(\alpha,T)
=
\sup_{m\ge1}
\mathfrak P_m(\alpha,T)^{1/m}.
\tag{6}
$$

### Proposition: the time-spine patch constant is finite

For every \(0<\alpha<1\) and \(T>0\),

$$
K_{\mathrm{time}}(\alpha,T)<\infty.
\tag{7}
$$

### Proof

Write each Hessian transfer as \(K_r^{(1)}=\partial_x^2P_r\). At fixed branch times, the integrand (4) is a product of \(m\) Hessian heat operators interlaced with the spatial multiplication operators \(M_{b_j(s_j)}\), followed by the initial heat lift \(P_{s_1}G\).

Use repeatedly

$$
K_R^{(k)}M_B
=
M_BK_R^{(k)}
+
[K_R^{(k)},M_B].
\tag{8}
$$

Every resulting term partitions the \(m\) Hessian edges into consecutive derivative clusters. A cluster of length \(\ell\) either reaches the initial profile \(G\), where mean-zero Hermite cancellation gives one \(C^\alpha\) increment, or ends at a commutator with a multiplier, where the same increment is supplied by that multiplier. The standard bounds give, for a cluster of total duration \(R\),

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
R^{-1+\alpha/2}
\tag{9}
$$

after integrating the internal subdivision of \(R\). Moreover

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
\le
C_\alpha4^\ell.
\tag{10}
$$

If a term has \(q\) clusters, the remaining cluster durations \(R_1,\ldots,R_q\) lie in a simplex with total at most \(T\). Their absolute integral is

$$
\int_{R_i>0,\,\sum_iR_i<T}
\prod_{i=1}^qR_i^{-1+\alpha/2}\,d\mathbf R
=
T^{q\alpha/2}
\frac{\Gamma(\alpha/2)^q}
{\Gamma(1+q\alpha/2)}
\le
D_{\alpha,T}^q
\tag{11}
$$

for a finite \(D_{\alpha,T}\). There are at most \(2^m\) cluster/commutator terms. The heat semigroup is contractive on \(C^\alpha\), and every multiplier contributes at most its \(X\)-norm. Combining (9)--(11) therefore gives

$$
\sup_{t,x}
\int_{\Delta_m(t)}
|I_m(t,x;\mathbf s)|\,d\mathbf s
\le
K_{\alpha,T}^m
\|G\|_{C^\alpha}
\prod_{j=1}^m\|b_j\|_X
$$

for a finite \(K_{\alpha,T}\) independent of \(m\). This proves (7). \(\square\)

The definition (6) uses the optimal geometric base; any explicit geometric constant obtained from the preceding proof is a valid upper bound for \(K_{\mathrm{time}}\).

## Time-spine coarsening

Every non-leaf planar binary tree has a unique root maximal-left patch. Suppose its length is \(m\ge1\). Along this patch, let the successive right subtrees be

$$
\sigma_1,\ldots,\sigma_m.
$$

The final left child is a leaf. This gives a bijective decomposition

$$
\tau
\longleftrightarrow
(m;\sigma_1,\ldots,\sigma_m),
\qquad
|\tau|
=
m+\sum_{j=1}^m|\sigma_j|.
\tag{12}
$$

Define \(\mathcal C_\tau^{\mathrm{time}}\) as follows.

- Retain the ordered branch times \(0<s_1<\cdots<s_m<t\) of the root maximal-left patch.
- Average all Gaussian/Hermite and Brownian marks on that patch.
- Average every continuous mark, including all branch times, inside each side subtree \(\sigma_j\).

At finite depth, conditional factorization shows that the pushforward signed measure on the retained time simplex has density

$$
\lambda^m
I_m[F_{\sigma_1},\ldots,F_{\sigma_m};\phi''](t,x;\mathbf s)\,d\mathbf s.
\tag{13}
$$

Thus this coarsening is defined directly from a finite signed measure; no conditional expectation of an unresolved infinite random functional is used.

For the leaf tree, the coarsened measure is the point mass of mass \(L(t,x)\).

## Theorem: an intermediate L1 representation with retained time randomness

Let

$$
C(a)
=
\sum_{n=0}^\infty C_na^n
=
\frac{1-\sqrt{1-4a}}{2a},
\qquad 0\le a<\frac14,
\tag{14}
$$

with \(C(0)=1\), and put

$$
b
=
|\lambda|K_{\mathrm{time}}(\alpha,T)M.
\tag{15}
$$

Assume

$$
4a<1,
\qquad
bC(a)<1.
\tag{16}
$$

Then, for every \((t,x)\in[0,T]\times\mathbb T\),

$$
\boxed{
\sum_{\tau\in\mathfrak T}
\|(\mathcal C_\tau^{\mathrm{time}})_\#\mu_\tau^{t,x}\|_{\mathrm{TV}}
\le
\frac{M}{1-bC(a)}
<\infty.
}
\tag{17}
$$

Consequently the canonical importance sampler for the coarsened measures is an unbiased \(L^1\) representation of the same solution \(z_*\) as Theorem C-prime. It retains the actual ordered branch times of the root maximal-left spine as continuous random variables.

### Proof

Let \(	au\leftrightarrow(m;\sigma_1,\ldots,\sigma_m)\) be the decomposition (12). By (13), the definition of \(K_{\mathrm{time}}\), and \(\|\phi''\|_{C^\alpha}\le M\),

$$
\begin{aligned}
\|(\mathcal C_\tau^{\mathrm{time}})_\#\mu_\tau^{t,x}\|_{\mathrm{TV}}
&\le
|\lambda|^m
K_{\mathrm{time}}^m
M
\prod_{j=1}^m\|F_{\sigma_j}\|_X\\
&\le
M b^m
\prod_{j=1}^m a^{|\sigma_j|},
\end{aligned}
\tag{18}
$$

where the second line uses (2).

Sum first over the \(m\) side subtrees. Since

$$
\sum_{\sigma\in\mathfrak T}a^{|\sigma|}
=
C(a),
$$

we obtain

$$
\begin{aligned}
\sum_{\tau\in\mathfrak T}
\|(\mathcal C_\tau^{\mathrm{time}})_\#\mu_\tau^{t,x}\|_{\mathrm{TV}}
&\le
M
+
M\sum_{m=1}^\infty
[bC(a)]^m\\
&=
\frac{M}{1-bC(a)}.
\end{aligned}
$$

This proves (17).

The total mass of every coarsened measure is \(F_\tau(t,x)\). Condition \(4a<1\) gives absolute convergence of \(\sum_\tau F_\tau=z_*\). Sampling a skeleton with any full-support mass function and then sampling the retained time vector from any positive proposal dominating its coarsened signed measure therefore gives an unbiased estimator. Equation (17) gives its finite first moment. \(\square\)

## Exact form of the additional smallness condition

Let

$$
\theta
=
\frac{K_{\mathrm{time}}(\alpha,T)}
{C_{\mathcal D}(\alpha,T)}.
$$

When \(a>0\), one has \(b=\theta a\), and

$$
aC(a)
=
\frac{1-\sqrt{1-4a}}2.
$$

Thus the second inequality in (16) is exactly

$$
\boxed{
\frac\theta2
\left(1-\sqrt{1-4a}\right)<1.
}
\tag{19}
$$

If \(	heta\le2\), this is automatic under \(4a<1\). If \(	heta>2\), it is equivalent to

$$
a
<
\frac{\theta-1}{\theta^2}.
\tag{20}
$$

Hence the time-spine theorem requires the C-prime condition together with one explicit additional geometric-series condition. Whether this is numerically stricter throughout the C-prime interval depends on the chosen valid constants \(K_{\mathrm{time}}\) and \(C_{\mathcal D}\); no universal numerical strengthening is asserted.

## The coarsening hierarchy is nontrivial

The three proved levels are now:

1. **Raw-faithful / identity.** For the fixed smooth datum of the raw-barycenter theorem, the canonical raw measures have nonsummable total variation. Naive patchwise bridge coarsening also fails because the obstruction uses one-edge patches.
2. **Time-spine coarsening.** Under (16), one root-spine time vector remains random and the total-variation sum is finite.
3. **Complete interior averaging / C-prime.** Under \(4a<1\), every continuous interior mark is integrated out and the skeleton-only estimator is \(L^1\).

The middle level is not decorative. For example, for the one-vertex tree and datum \(\phi''(x)=\cos x\), the retained-time density at \(x=0\) is proportional to

$$
\partial_x^2P_{t-s}
[(P_s\cos)^2](0)
=
-2e^{-2t+s},
$$

which depends nontrivially on \(s\). The sampled branch time therefore affects the estimator value.

This theorem shows that the correct structural dichotomy is not “raw randomness versus no randomness.” Averaging enough continuous marks to move signed mass between raw states is necessary for the fixed-datum obstruction, but complete averaging is not necessary for \(L^1\) in the stronger small-data regime (16).
