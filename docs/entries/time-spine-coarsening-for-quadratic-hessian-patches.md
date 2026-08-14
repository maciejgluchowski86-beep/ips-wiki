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

1. A naive patchwise Gaussian-bridge coarsening does **not** repair the fixed-datum raw obstruction. The obstruction may be realized on right-oriented combs, and every maximal-left patch of such a comb has one edge. A one-edge bridge map has no bridge coordinate to remove.
2. Retaining the ordered branch times on the root maximal-left patch while averaging the remaining continuous variables does give an \(L^1\) representation under an explicit smallness condition. The analytic patch estimate behind this statement is geometric in the patch length and requires **no smallness assumption**; smallness enters only when the finite-patch estimates are summed over all trees.

The finite patch convention is in [Finite-depth Duhamel patch regrouping](finite-depth-duhamel-patch-regrouping.md). The Hermite and commutator estimates used below are recorded in [Holder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md). The Catalan tree bound is in [Skeleton-averaged L1 representation for the quadratic Hessian PDE](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md), and the fixed-datum lower bound is in [Raw-barycenter L1 obstruction for the quadratic Hessian PDE](raw-marked-l1-obstruction-for-quadratic-hessian-pde.md).

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

and write

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
a=|\lambda|C_{\mathcal D}M.
\tag{1}
$$

For a finite planar full binary tree \(	au\), let \(F_\tau\) be its deterministic Duhamel profile. If \(|\tau|=n\), then

$$
\|F_\tau\|_X
\le
Ma^n.
\tag{2}
$$

Let \(\mu_\tau^{t,x}\) be the [canonical finite raw signed measure](canonical-raw-signed-measures-for-finite-quadratic-hessian-trees.md). Its total mass is \(F_\tau(t,x)\).

## Why patchwise Gaussian bridges miss the obstruction

A patch is a maximal chain obtained by repeatedly following the left child. A *right comb of length \(m\)* is the planar binary tree whose right child continues through exactly \(m\) internal vertices while every left child is a leaf.

Every patch of a right comb has length one: the left child of every internal vertex is already terminal. Therefore, on the right-comb family used in the raw-barycenter obstruction, the patchwise endpoint Gaussian

$$
Z_{\mathrm{end}}
=
\frac{\sum_{j=1}^{\ell}\sqrt{r_j}Z_j}
{\sqrt{r_1+\cdots+r_\ell}}
$$

reduces to \(Z_1\) because \(\ell=1\). If the unnormalized displacement is retained instead, \(Z_1\mapsto\sqrt{r_1}Z_1\) is invertible once the duration is retained. Hence patchwise bridge coarsening leaves total variation unchanged on every obstruction cylinder. For the fixed smooth datum of the raw-barycenter theorem,

$$
\sum_m
\|(\mathcal C_{\Gamma_m}^{\mathrm{bridge}})_\#\mu_m\|_{\mathrm{TV}}
=
\sum_m\|\mu_m\|_{\mathrm{TV}}
=
\infty.
\tag{3}
$$

Thus naive patchwise bridge coarsening is nonintegrable on that datum.

## Derivative clusters and the absolute-time patch bound

For \(m\ge1\), let

$$
0<s_1<\cdots<s_m<t\le T.
$$

Given \(G\in C^\alpha(\mathbb T)\) and \(b_1,\ldots,b_m\in X\), define

$$
\Xi_1=b_1(s_1)P_{s_1}G,
$$

and

$$
\Xi_r
=b_r(s_r)
\partial_x^2P_{s_r-s_{r-1}}\Xi_{r-1},
\qquad 2\le r\le m.
$$

Set

$$
I_m[b_1,\ldots,b_m;G](t,x;\mathbf s)
=
\partial_x^2P_{t-s_m}\Xi_m(x).
\tag{4}
$$

Define

$$
\mathfrak P_m(\alpha,T)
=
\sup
\frac{
\displaystyle
\sup_{t\le T,x\in\mathbb T}
\int_{0<s_1<\cdots<s_m<t}|I_m|\,d\mathbf s
}{
\|G\|_{C^\alpha}
\prod_{j=1}^m\|b_j\|_X
},
\tag{5}
$$

with the supremum over nonzero inputs, and

$$
K_{\mathrm{time}}(\alpha,T)
=
\sup_{m\ge1}
\mathfrak P_m(\alpha,T)^{1/m}.
\tag{6}
$$

### Proposition: explicit absolute-time derivative-cluster bound

Define

$$
H_\alpha
=
\left(\mathbb E|Z|^{2\alpha}\right)^{1/2},
\qquad
D_{\alpha,T}
=
\frac{2T^{\alpha/2}}{\alpha},
\qquad
A_{\alpha,T}=H_\alpha D_{\alpha,T},
\tag{7}
$$

and

$$
K_{\mathrm{cl}}(\alpha,T)
=
4\max\{1+A_{\alpha,T},\,2A_{\alpha,T}\}.
\tag{8}
$$

Then, for every \(m\ge1\),

$$
\boxed{
\begin{aligned}
&\sup_{t\le T,x\in\mathbb T}
\int_{0<s_1<\cdots<s_m<t}
|I_m[b_1,\ldots,b_m;G](t,x;\mathbf s)|\,d\mathbf s\\
&\qquad\le
2A_{\alpha,T}4^m(1+A_{\alpha,T})^{m-1}
\|G\|_{C^\alpha}
\prod_{j=1}^m\|b_j\|_X\\
&\qquad\le
K_{\mathrm{cl}}(\alpha,T)^m
\|G\|_{C^\alpha}
\prod_{j=1}^m\|b_j\|_X.
\end{aligned}
}
\tag{9}
$$

Consequently

$$
K_{\mathrm{time}}(\alpha,T)
\le
K_{\mathrm{cl}}(\alpha,T)
<\infty.
\tag{10}
$$

This proposition is purely analytic. It contains no smallness condition on \(\lambda\), \(\phi\), or any nonlinear solution norm.

### Proof

Write

$$
K_r^{(k)}=\partial_x^{2k}P_r,
\qquad
M_Bf=Bf,
$$

and

$$
c_{2k,\alpha}
=
\mathbb E[|He_{2k}(Z)|\,|Z|^\alpha].
$$

The standard Hermite cancellation and multiplication-commutator bounds are

$$
\|K_R^{(k)}f\|_\infty
\le
c_{2k,\alpha}R^{-k+\alpha/2}[f]_{C^\alpha},
\tag{11}
$$

and

$$
\|[K_R^{(k)},M_B]f\|_\infty
\le
c_{2k,\alpha}R^{-k+\alpha/2}
[B]_{C^\alpha}\|f\|_\infty.
\tag{12}
$$

Set \(s_{m+1}=t\) and

$$
r_j=s_{j+1}-s_j,
\qquad 1\le j\le m.
$$

Then \(r_j>0\), \(\sum_jr_j<t\), and

$$
s_1=t-\sum_{j=1}^m r_j.
$$

The change of variables from \((s_1,\ldots,s_m)\) to \((r_1,\ldots,r_m)\) has unit Jacobian. In particular, the initial heat interval is **not** an extra integration variable. With \(B_j=b_j(s_j,\cdot)\),

$$
I_m
=
K_{r_m}^{(1)}M_{B_m}
K_{r_{m-1}}^{(1)}M_{B_{m-1}}
\cdots
K_{r_1}^{(1)}M_{B_1}P_{s_1}G.
\tag{13}
$$

Expand repeatedly with

$$
K_R^{(k)}M_B
=
M_BK_R^{(k)}+[K_R^{(k)},M_B].
\tag{14}
$$

Passing a multiplier joins the current derivative block to the next Hessian edge because

$$
K_R^{(k)}K_r^{(1)}=K_{R+r}^{(k+1)}.
$$

Taking the commutator terminates the current derivative cluster. Thus every term partitions the \(m\) derivative edges into consecutive clusters. A term with \(q\) clusters has \(q-1\) cluster boundaries among the first \(m-1\) multipliers, and the innermost multiplier has two terminal choices: the last cluster may end in its commutator or pass through it and reach \(P_{s_1}G\). Hence the exact number of \(q\)-cluster terms is

$$
2\binom{m-1}{q-1}.
\tag{15}
$$

Consider a cluster of length \(\ell\) and total derivative duration \(R\). For fixed \(R\), the simplex of its \(\ell\) positive edge durations has volume

$$
\frac{R^{\ell-1}}{(\ell-1)!}.
$$

If the cluster ends at a multiplier, apply (12). If the innermost cluster reaches \(G\), apply (11) and

$$
[P_{s_1}G]_{C^\alpha}\le [G]_{C^\alpha}.
$$

After the internal subdivision is integrated, the cluster contributes at most

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
R^{-1+\alpha/2}.
\tag{16}
$$

Every multiplier appears exactly once and costs at most \(\|b_j\|_X\).

By Cauchy--Schwarz and Hermite orthogonality,

$$
c_{2\ell,\alpha}
\le
H_\alpha\sqrt{(2\ell)!}.
$$

Furthermore,

$$
\frac{\sqrt{(2\ell)!}}{(\ell-1)!}
=
\ell\sqrt{\binom{2\ell}{\ell}}
\le
\ell2^\ell
\le
4^\ell.
$$

Therefore

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
\le
H_\alpha4^\ell.
\tag{17}
$$

For a \(q\)-cluster term, the cluster lengths sum to \(m\), so (17) contributes \(H_\alpha^q4^m\). If the cluster totals are \(R_1,\ldots,R_q\), then

$$
\int_{\substack{R_i>0\\\sum_iR_i<t}}
\prod_{i=1}^qR_i^{-1+\alpha/2}\,d\mathbf R
\le
\prod_{i=1}^q
\int_0^T R^{-1+\alpha/2}\,dR
=
D_{\alpha,T}^q.
\tag{18}
$$

Hence each \(q\)-cluster term is bounded by

$$
4^mA_{\alpha,T}^q
\|G\|_{C^\alpha}
\prod_{j=1}^m\|b_j\|_X.
$$

Summing (15) over \(q\) gives

$$
\begin{aligned}
\mathfrak P_m(\alpha,T)
&\le
2\,4^m
\sum_{q=1}^m
\binom{m-1}{q-1}A_{\alpha,T}^q\\
&=
2A_{\alpha,T}4^m(1+A_{\alpha,T})^{m-1}.
\end{aligned}
$$

If \(A_{\alpha,T}\le1\), this is at most \([4(1+A_{\alpha,T})]^m\); if \(A_{\alpha,T}\ge1\), it is at most \((8A_{\alpha,T})^m\). Equations (8)--(10) follow. \(\square\)

## Time-spine coarsening and the representation corollary

Every non-leaf planar binary tree has a unique root maximal-left patch. If its length is \(m\ge1\), let \(\sigma_1,\ldots,\sigma_m\) be its successive right subtrees. Then

$$
\tau
\longleftrightarrow
(m;\sigma_1,\ldots,\sigma_m),
\qquad
|\tau|
=m+\sum_{j=1}^m|\sigma_j|.
\tag{19}
$$

The time-spine rule retains the ordered branch times \(0<s_1<\cdots<s_m<t\) of this root patch, averages every Gaussian/Hermite and Brownian mark on that patch, and averages every continuous mark inside the side subtrees. The pushforward signed measure on the retained time simplex has density

$$
\lambda^m
I_m[F_{\sigma_1},\ldots,F_{\sigma_m};\phi'']
(t,x;\mathbf s)\,d\mathbf s.
\tag{20}
$$

### Corollary: target-uniform time-spine L1 representation

Let

$$
C(a)
=
\sum_{n=0}^\infty C_na^n
=
\frac{1-\sqrt{1-4a}}{2a},
\qquad C(0)=1,
$$

and put

$$
b
=
|\lambda|K_{\mathrm{time}}(\alpha,T)M.
\tag{21}
$$

Assume

$$
\boxed{
4a<1,
\qquad
bC(a)<1.
}
\tag{22}
$$

Then the same time-spine coarsening rule works for every \((t,x)\in[0,T]\times\mathbb T\), and

$$
\boxed{
\sum_{\tau\in\mathfrak T}
\|(\mathcal C_\tau^{\mathrm{time}})_\#
\mu_\tau^{t,x}\|_{\mathrm{TV}}
\le
\frac{M}{1-bC(a)}
<\infty.
}
\tag{23}
$$

Consequently its canonical importance sampler is an unbiased \(L^1\) representation of the C-prime solution \(z_*(t,x)\) for every target. The ordered branch-time vector is retained and is nondecorative. No Gaussian/Hermite or Brownian mark is retained by this rule.

### Proof

For \(	au\leftrightarrow(m;\sigma_1,\ldots,\sigma_m)\), the density (20), the definition of \(K_{\mathrm{time}}\), and (2) give

$$
\begin{aligned}
\|(\mathcal C_\tau^{\mathrm{time}})_\#\mu_\tau^{t,x}\|_{\mathrm{TV}}
&\le
|\lambda|^mK_{\mathrm{time}}^mM
\prod_{j=1}^m\|F_{\sigma_j}\|_X\\
&\le
Mb^m\prod_{j=1}^ma^{|\sigma_j|}.
\end{aligned}
\tag{24}
$$

Since

$$
\sum_{\sigma\in\mathfrak T}a^{|\sigma|}=C(a),
$$

summing independently over the side subtrees gives

$$
\sum_{\tau\in\mathfrak T}
\|(\mathcal C_\tau^{\mathrm{time}})_\#\mu_\tau^{t,x}\|_{\mathrm{TV}}
\le
M+M\sum_{m\ge1}[bC(a)]^m
=
\frac{M}{1-bC(a)}.
$$

Condition \(4a<1\) also gives the absolutely convergent C-prime sum of the total masses \(F_\tau(t,x)\), so the residual-variation theorem gives the unbiased \(L^1\) representation.

For nondecorativity, take the one-vertex tree and \(\phi''(x)=\cos x\). At \(x=0\), the retained-time density contains

$$
\partial_x^2P_{t-s}[(P_s\cos)^2](0)
=
-2e^{-2t+s},
$$

which depends nontrivially on \(s\). \(\square\)

The separation between the proposition and the corollary is load-bearing: the derivative-cluster bound is an unconditional analytic estimate, whereas (22) is needed only to sum the finite-patch bounds over the infinite tree family.

## Exact form of the additional smallness condition

Let

$$
\theta
=
\frac{K_{\mathrm{time}}(\alpha,T)}
{C_{\mathcal D}(\alpha,T)}.
$$

When \(a>0\), \(b=\theta a\), and

$$
aC(a)
=
\frac{1-\sqrt{1-4a}}2.
$$

Thus the second condition in (22) is

$$
\boxed{
\frac\theta2
\left(1-\sqrt{1-4a}\right)<1.
}
\tag{25}
$$

If \(	heta\le2\), this is automatic under \(4a<1\). If \(	heta>2\), it is equivalent to

$$
a<\frac{\theta-1}{\theta^2}.
\tag{26}
$$

Hence the time-spine representation requires the C-prime condition together with one explicit additional geometric-series condition. Whether it is numerically stricter throughout the C-prime interval depends on the chosen valid constants \(K_{\mathrm{time}}\) and \(C_{\mathcal D}\).

## The structured hierarchy

The three proved levels are:

1. **Raw-faithful / identity.** For the fixed smooth datum of the raw-barycenter theorem, the canonical raw measures have nonsummable total variation. Naive patchwise bridge coarsening also fails because the obstruction uses one-edge patches.
2. **Time-spine coarsening.** Under (22), the root-spine branch-time vector remains random and the total-variation sum is finite uniformly in the target.
3. **Complete interior averaging / C-prime.** Under \(4a<1\), every continuous interior mark is integrated out and the skeleton-only estimator is \(L^1\).

Thus the correct structural dichotomy is not “raw randomness versus no randomness.” Enough averaging to move signed mass between canonical raw states is necessary for the fixed-datum raw obstruction, but complete averaging is not necessary in the stronger small-data regime (22).
