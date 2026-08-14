---
title: Residual signed variation characterizes coarsened patch representations
status: proved here
tags:
  - PDE
  - patch
  - coarsening
  - total variation
  - conditional expectation
  - integrability
---

# Residual signed variation characterizes coarsened patch representations

The coarsening hierarchy is governed by an exact invariant. It is not the number or type of continuous marks which remain random. It is the **signed total variation which survives after the discarded variables have been averaged**.

For one skeleton, this surviving variation is the \(L^1\) norm of the conditional barycenter of the raw signed density. For a countable skeleton family, summability of these residual variations is both necessary and sufficient for an \(L^1\) representation in the skeleton-preserving conditional-barycenter class.

This puts the raw-faithful obstruction, the time-spine theorem, and Theorem C-prime on one scale. It also gives two counterintuitive consequences: the entire Gaussian configuration may survive on sufficiently small pieces and still be \(L^1\), while retaining only a time coordinate may fail.

The concrete quadratic-Hessian hierarchy is in [Time-spine coarsening for quadratic Hessian patches](time-spine-coarsening-for-quadratic-hessian-patches.md). The theorem below is proved here.

## Exact residual-variation identity

Let \((\Omega,\mathcal F)\) be measurable, let \(\nu\) be a finite positive measure, and let

$$
R\in L^1(\nu),
\qquad
\mu=R\nu.
\tag{1}
$$

Let

$$
\mathcal C:\Omega\to Y
$$

be measurable. Set

$$
\overline\nu=\mathcal C_\#\nu,
\qquad
\overline\mu=\mathcal C_\#\mu,
\qquad
\mathcal G=\sigma(\mathcal C).
\tag{2}
$$

Since \(\overline\mu\ll\overline\nu\), write

$$
\overline R
=
\frac{d\overline\mu}{d\overline\nu}.
$$

### Theorem

One has

$$
\boxed{
\overline R(\mathcal C(\omega))
=
\mathbb E_\nu[R\mid\mathcal G](\omega)
\quad\nu\text{-a.e.}
}
\tag{3}
$$

and consequently

$$
\boxed{
\|\mathcal C_\#\mu\|_{\mathrm{TV}}
=
\int_\Omega
\left|
\mathbb E_\nu[R\mid\sigma(\mathcal C)]
\right|d\nu.
}
\tag{4}
$$

The common quantity is the **residual signed variation** after coarsening.

### Proof

For every measurable \(B\subseteq Y\),

$$
\begin{aligned}
\int_{\mathcal C^{-1}(B)}R\,d\nu
&=
\mu(\mathcal C^{-1}(B))\\
&=
\overline\mu(B)\\
&=
\int_B\overline R\,d\overline\nu\\
&=
\int_{\mathcal C^{-1}(B)}
\overline R(\mathcal C(\omega))d\nu(\omega).
\end{aligned}
$$

The right-hand integrand is \(\mathcal G\)-measurable, proving (3). Integrating its absolute value gives (4).

Because (4) equals the total variation of the pushforward signed measure, it is independent of the choice of reference representation \(\mu=R\nu\).

## Exact L1 characterization for a skeleton family

Let \(\mathfrak T\) be countable. For each \(\tau\), let

$$
\mu_\tau=R_\tau\nu_\tau
$$

be finite signed and let

$$
\mathcal C_\tau:\Omega_\tau\to Y_\tau
$$

be a skeleton-preserving coarsening. Put

$$
V_\tau
=
\|(\mathcal C_\tau)_\#\mu_\tau\|_{\mathrm{TV}}
=
\int
\left|
\mathbb E_{\nu_\tau}
[R_\tau\mid\sigma(\mathcal C_\tau)]
\right|d\nu_\tau.
\tag{5}
$$

Choose any full-support skeleton probability \(\pi\), and conditional positive proposal \(Q_\tau\) dominating

$$
\overline\mu_\tau
=(\mathcal C_\tau)_\#\mu_\tau.
$$

The canonical estimator

$$
Y
=
\frac1{\pi(S)}
\frac{d\overline\mu_S}{dQ_S}(U)
$$

satisfies

$$
\boxed{
\mathbb E|Y|
=
\sum_{\tau\in\mathfrak T}V_\tau.
}
\tag{6}
$$

Therefore

$$
\boxed{
Y\in L^1
\quad\Longleftrightarrow\quad
\sum_\tau V_\tau<\infty.
}
\tag{7}
$$

This is genuine necessity and sufficiency, not merely an upper bound. If an estimator uses auxiliary randomness but has the same coarsened signed density as its conditional barycenter after \((S,U)\) are exposed, conditional Jensen gives

$$
\mathbb E|\widetilde Y|
\geq
\sum_\tau V_\tau.
\tag{8}
$$

The canonical estimator attains equality.

The scope is skeleton-preserving coarsening. If the skeleton label itself is forgotten, then it is another coordinate being coarsened; the invariant is still the total variation after the enlarged pushforward, but it need not equal the sum of the separate skeleton variations.

## Coarsening order

If

$$
\sigma(\mathcal C_1)
\subseteq
\sigma(\mathcal C_2),
$$

then the tower property and conditional Jensen give

$$
V_\mu(\mathcal C_1)
\leq
V_\mu(\mathcal C_2).
\tag{9}
$$

The endpoints are

$$
V_\mu(\operatorname{Id})
=
\|\mu\|_{\mathrm{TV}},
\qquad
V_\mu(\mathrm{const})
=
|\mu(\Omega)|.
\tag{10}
$$

Thus cancellation before absolute values is exactly

$$
\|\mu\|_{\mathrm{TV}}
-
V_\mu(\mathcal C).
$$

No named coordinate appears in this formula.

## Explicit Gaussian counterexample

For \(n\geq1\), let

$$
\Omega_n=\mathbb R^n,
\qquad
\nu_n=\gamma_n,
$$

where \(\gamma_n\) is standard Gaussian measure, and set

$$
R_n(z)
=
2^{-n}+\operatorname{sgn}(z_1).
\tag{11}
$$

Then

$$
\mu_n(\Omega_n)=2^{-n},
\qquad
\|\mu_n\|_{\mathrm{TV}}=1.
$$

Hence constant coarsening is summable and identity retention is not.

Choose a symmetric slab

$$
A_n
=
\{z:|z_1|\leq\delta_n\}
$$

with

$$
\gamma_n(A_n)=2^{-n},
$$

and define

$$
\mathcal C_n(z)
=
\begin{cases}
(1,z),&z\in A_n,\\
(0,*),&z\notin A_n.
\end{cases}
\tag{12}
$$

On \(A_n\) the **entire Gaussian vector** survives. Symmetry gives zero signed contribution from \(\operatorname{sgn}(z_1)\) separately on \(A_n\) and \(A_n^c\), so

$$
\begin{aligned}
V_n
&=
\int_{A_n}|R_n|d\gamma_n
+|\mu_n(A_n^c)|\\
&=
2^{-n}+2^{-n}(1-2^{-n})\\
&<2^{1-n}.
\end{aligned}
\tag{13}
$$

Thus

$$
\sum_nV_n<\infty
$$

even though every Gaussian coordinate is retained exactly on a nonnull piece of every state space.

## Explicit time-only counterexample

Let

$$
\Omega_n=(0,1)\times\mathbb R^n,
\qquad
\nu_n=dt\otimes\gamma_n,
$$

and define

$$
R_n(t,z)
=
2^{-n}+h(t),
$$

where

$$
h(t)
=
\begin{cases}
1,&0<t<1/2,\\
-1,&1/2<t<1.
\end{cases}
$$

Again

$$
\mu_n(\Omega_n)=2^{-n},
$$

so complete averaging is summable. Now retain only time,

$$
\mathcal C_n(t,z)=t.
$$

All Gaussian variables disappear, but

$$
\mathbb E[R_n\mid t]
=
2^{-n}+h(t),
$$

so

$$
V_n
=
\int_0^1|2^{-n}+h(t)|dt
=1.
\tag{14}
$$

Therefore

$$
\sum_nV_n=\infty.
$$

Retaining only an apparently harmless time variable is not safe unless the residual sign variation visible through time is controlled.

## Sparse full-state retention for the quadratic-Hessian patches

Fix one observation point \((t,x)\) in the C-prime regime. Then

$$
\sum_\tau|F_\tau(t,x)|<\infty.
\tag{15}
$$

Every finite non-leaf raw patch measure \(\mu_\tau^{t,x}\) is absolutely continuous with respect to a reference law containing continuous Gaussian/time coordinates, hence its total-variation measure is nonatomic. Choose positive summable \(\varepsilon_\tau\), and for each nonzero non-leaf measure choose \(A_\tau\) with

$$
0<
|\mu_\tau^{t,x}|(A_\tau)
\leq
\varepsilon_\tau.
$$

Retain the entire raw state on \(A_\tau\) and collapse \(A_\tau^c\). Then

$$
\begin{aligned}
V_\tau
&=
|\mu_\tau^{t,x}|(A_\tau)
+|\mu_\tau^{t,x}(A_\tau^c)|\\
&\leq
|F_\tau(t,x)|+2\varepsilon_\tau.
\end{aligned}
\tag{16}
$$

Thus

$$
\sum_\tau V_\tau<\infty.
\tag{17}
$$

At every fixed target in the C-prime regime, there are therefore nonconstant \(L^1\) coarsenings which retain the complete raw Gaussian configuration on small nonnull pieces. This closes the **fixed-target existential relaxation** of Conjecture C. It does not by itself construct one target-uniform coarsening architecture valid simultaneously for every \((t,x)\); that stronger formulation remains open.

## Sanity check: the three known quadratic-Hessian points

The characterization reproduces all three previously proved results.

- **Raw-faithful / identity.** Conditional expectation onto the full raw sigma-field is \(R_\tau\), so the residual variation is the full raw total variation. The right-comb fixed-datum theorem gives a divergent subseries.
- **Time-spine.** Conditional expectation onto the retained root-spine times is exactly the deterministic time-spine density. The [time-spine theorem](time-spine-coarsening-for-quadratic-hessian-patches.md) proves summability under
  $$
  4a<1,
  \qquad
  bC(a)<1.
  $$
- **C-prime / constant.** The residual variation is \(|F_\tau(t,x)|\), whose sum is finite throughout the Catalan regime.

No point in the existing hierarchy conflicts with the characterization. They are three different values of the same invariant.

## What remains open

The fixed-target skeleton-preserving integrability problem is characterized exactly. Natural remaining questions are stronger:

1. construct a non-sparse coarsening with a fixed geometric description which is \(L^1\) throughout the full C-prime regime;
2. construct one target-uniform coarsening architecture with quantitative function-space control;
3. optimize residual variation under a prescribed retained sigma-field or computational budget;
4. find natural Gaussian coarsenings beyond the failed patchwise bridge construction;
5. formulate cross-skeleton coarsenings where the skeleton label itself may be averaged.

The conceptual endpoint is exact: **cancellation before absolute values is removal of signed variation by conditional averaging, and \(L^1\) is equivalent to summability of the variation which survives.**
