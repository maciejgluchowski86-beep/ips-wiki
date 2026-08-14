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

The quadratic-Hessian coarsening hierarchy is governed by an exact invariant. It is not the number or type of continuous marks which remain random. It is the **signed total variation which survives after the discarded variables have been averaged**.

For one skeleton, this surviving variation is the \(L^1\) norm of the conditional barycenter of the raw signed density. For a countable skeleton family, summability of these residual variations is both necessary and sufficient for an \(L^1\) coarsened representation in the skeleton-preserving conditional-barycenter class.

This characterization explains all three previously proved points:

- identity/raw-faithful coarsening leaves all raw variation and is non-\(L^1\) for the fixed obstruction datum;
- time-spine coarsening leaves only a controlled residual variation and is \(L^1\) under its geometric smallness condition;
- constant coarsening leaves only the absolute signed mass of each skeleton and is exactly Theorem C-prime.

It also gives two less intuitive consequences. A coarsening may retain the **entire Gaussian configuration** on sufficiently small pieces of the raw state space and still have summable residual variation. Conversely, retaining only a branch-time coordinate can have infinite residual variation even when complete averaging is summable.

The result is proved here. The total-variation and pushforward terminology is consistent with [Total variation, bounded variation, and derivative singularities](total-variation-bounded-variation-and-derivative-singularities.md), while the concrete quadratic-Hessian hierarchy is in [Time-spine coarsening for quadratic Hessian patches](time-spine-coarsening-for-quadratic-hessian-patches.md).

## One signed measure and one coarsening

Let \((\Omega,\mathcal F)\) be a measurable space. Let \(\nu\) be a finite positive measure and let

$$
R\in L^1(\nu).
$$

Define the finite signed measure

$$
\mu=R\nu.
\tag{1}
$$

Let

$$
\mathcal C:\Omega\to Y
$$

be measurable into another measurable space \((Y,\mathcal Y)\). Put

$$
\overline\nu=\mathcal C_\#\nu,
\qquad
\overline\mu=\mathcal C_\#\mu,
\qquad
\mathcal G=\sigma(\mathcal C).
\tag{2}
$$

Because \(\mu\ll\nu\), one has \(\overline\mu\ll\overline\nu\). Let

$$
\overline R
=
\frac{d\overline\mu}{d\overline\nu}.
\tag{3}
$$

### Theorem: exact residual-variation identity

One has

$$
\boxed{
\overline R(\mathcal C(\omega))
=
\mathbb E_\nu[R\mid\mathcal G](\omega)
\quad\text{for }\nu\text{-a.e. }\omega,
}
\tag{4}
$$

where conditional expectation is taken with respect to the finite measure \(\nu\). Consequently

$$
\boxed{
\|\mathcal C_\#\mu\|_{\mathrm{TV}}
=
\int_\Omega
\left|
\mathbb E_\nu[R\mid\sigma(\mathcal C)]
\right|d\nu.
}
\tag{5}
$$

We call the common quantity in (5) the **residual signed variation** of \(\mu\) after the coarsening \(\mathcal C\), and write

$$
V_\mu(\mathcal C)
:=
\|\mathcal C_\#\mu\|_{\mathrm{TV}}.
\tag{6}
$$

Although the conditional-expectation formula uses a reference representation \(\mu=R\nu\), the quantity \(V_\mu(\mathcal C)\) is intrinsic because it is the total variation of the pushforward signed measure.

### Proof

For every \(B\in\mathcal Y\),

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
\overline R(\mathcal C(\omega))\,d\nu(\omega).
\end{aligned}
$$

The function \(\overline R\circ\mathcal C\) is \(\mathcal G\)-measurable, so this is precisely the defining property of the conditional expectation in (4). Therefore

$$
\begin{aligned}
\|\overline\mu\|_{\mathrm{TV}}
&=
\int_Y|\overline R|\,d\overline\nu\\
&=
\int_\Omega
|\overline R\circ\mathcal C|\,d\nu\\
&=
\int_\Omega
\left|
\mathbb E_\nu[R\mid\mathcal G]
\right|d\nu,
\end{aligned}
$$

which proves (5).

## Coarsening order and exact amount of cancellation

If \(\mathcal C_1\) is coarser than \(\mathcal C_2\), meaning

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
\tag{7}
$$

Thus more averaging can only remove signed variation.

The two endpoints are exact:

- if \(\mathcal C=\operatorname{Id}\), then
  $$
  V_\mu(\operatorname{Id})
  =
  \int|R|d\nu
  =
  \|\mu\|_{\mathrm{TV}};
  \tag{8}
  $$
- if \(\mathcal C\) is constant, then
  $$
  V_\mu(\mathcal C)
  =
  \left|\int R\,d\nu\right|
  =
  |\mu(\Omega)|.
  \tag{9}
  $$

Hence the amount of cancellation created before the absolute value is exactly

$$
\|\mu\|_{\mathrm{TV}}
-
V_\mu(\mathcal C)
=
\int|R|d\nu
-
\int
\left|
\mathbb E_\nu[R\mid\sigma(\mathcal C)]
\right|d\nu.
\tag{10}
$$

No reference to Gaussian, time, or descendant coordinates appears in (5)--(10).

## Countably many skeletons: an exact L1 criterion

Let \(\mathfrak T\) be countable. For every \(\tau\in\mathfrak T\), let

$$
\mu_\tau=R_\tau\nu_\tau
$$

be a finite signed measure on \(\Omega_\tau\), with \(\nu_\tau\) finite positive and \(R_\tau\in L^1(\nu_\tau)\). Let

$$
\mathcal C_\tau:\Omega_\tau\to Y_\tau
$$

be a measurable skeleton-preserving coarsening and set

$$
\overline\mu_\tau
=
(\mathcal C_\tau)_\#\mu_\tau.
\tag{11}
$$

For a full-support skeleton law \(\pi\), and positive proposal probabilities \(Q_\tau\) dominating \(\overline\mu_\tau\), the canonical coarsened estimator is

$$
Y
=
\frac1{\pi(S)}
\frac{d\overline\mu_S}{dQ_S}(U),
\qquad
S\sim\pi,
\quad
U\mid\{S=\tau\}\sim Q_\tau.
\tag{12}
$$

Then

$$
\boxed{
\mathbb E|Y|
=
\sum_{\tau\in\mathfrak T}
V_{\mu_\tau}(\mathcal C_\tau)
=
\sum_{\tau\in\mathfrak T}
\int
\left|
\mathbb E_{\nu_\tau}
[R_\tau\mid\sigma(\mathcal C_\tau)]
\right|d\nu_\tau.
}
\tag{13}
$$

Consequently

$$
\boxed{
Y\in L^1
\quad\Longleftrightarrow\quad
\sum_{\tau\in\mathfrak T}
V_{\mu_\tau}(\mathcal C_\tau)<\infty.
}
\tag{14}
$$

This is both necessity and sufficiency for the canonical coarsened sampler.

More generally, suppose an estimator \(\widetilde Y\) uses arbitrary auxiliary randomness but, after the skeleton and coarsened state are exposed, has the canonical coarsened signed density as its conditional barycenter. Conditional Jensen gives

$$
\mathbb E|\widetilde Y|
\geq
\sum_\tau
V_{\mu_\tau}(\mathcal C_\tau).
\tag{15}
$$

The canonical estimator (12) attains equality. Therefore the right side of (13) is the **minimum possible first moment in the conditional-barycenter class attached to the fixed coarsening scheme**. This is the exact necessity-and-sufficiency statement.

The scope is important. Formula (13) treats the skeleton label as retained. If one also identifies states belonging to different skeletons, then the skeleton itself has been further coarsened and the relevant invariant is the total variation after that larger pushforward. There is no contradiction: residual signed variation remains the invariant, but the state space being conditioned on has changed.

## Explicit example: the entire Gaussian configuration may survive

The type of retained variable does not determine integrability. Here is an explicit family in which the raw variation is not summable, yet a coarsening which sometimes retains the **entire Gaussian vector** is summable.

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
\tag{16}
$$

Then

$$
\mu_n(\Omega_n)=2^{-n},
\qquad
\|\mu_n\|_{\mathrm{TV}}=1.
\tag{17}
$$

Thus complete averaging is summable,

$$
\sum_n|\mu_n(\Omega_n)|=1,
$$

while identity retention is not,

$$
\sum_n\|\mu_n\|_{\mathrm{TV}}=\infty.
$$

Choose \(\delta_n>0\) so that

$$
\gamma_n\{z:|z_1|\leq\delta_n\}=2^{-n},
$$

and write this symmetric slab as \(A_n\). Define

$$
\mathcal C_n(z)
=
\begin{cases}
(1,z),&z\in A_n,\\
(0,*),&z\notin A_n.
\end{cases}
\tag{18}
$$

On \(A_n\), the whole vector \(z=(z_1,\ldots,z_n)\) is retained exactly. Outside \(A_n\), every Gaussian coordinate is forgotten.

Because \(A_n\) is symmetric in \(z_1\),

$$
\int_{A_n}\operatorname{sgn}(z_1)d\gamma_n
=
\int_{A_n^c}\operatorname{sgn}(z_1)d\gamma_n
=0.
$$

Hence

$$
\begin{aligned}
V_{\mu_n}(\mathcal C_n)
&=
\int_{A_n}|R_n|d\gamma_n
+
|\mu_n(A_n^c)|\\
&=
2^{-n}
+2^{-n}(1-2^{-n})\\
&<
2^{1-n}.
\end{aligned}
\tag{19}
$$

Therefore

$$
\sum_nV_{\mu_n}(\mathcal C_n)<\infty.
\tag{20}
$$

The entire Gaussian configuration survives on a nonnull piece for every \(n\), yet the family is \(L^1\). The reason is not that the Gaussian marks became harmless; it is that only a summable amount of their signed variation survives.

### Sparse full-state retention in the C-prime regime

The same construction is available abstractly for the quadratic-Hessian patch measures. Fix an observation point \((t,x)\) in the C-prime regime, so

$$
\sum_\tau|F_\tau(t,x)|<\infty.
\tag{21}
$$

Every finite non-leaf raw patch measure \(\mu_\tau^{t,x}\) is absolutely continuous with respect to a reference law containing continuous Gaussian coordinates, so its total-variation measure is nonatomic on those coordinates. Let \((\varepsilon_\tau)_\tau\) be positive and summable. Choose measurable sets \(A_\tau\) with

$$
0<
|\mu_\tau^{t,x}|(A_\tau)
\leq
\varepsilon_\tau
$$

whenever the raw measure is nonzero, and define \(\mathcal C_\tau\) to retain the entire raw state on \(A_\tau\) and collapse \(A_\tau^c\) to one point. Then

$$
\begin{aligned}
V_{\mu_\tau^{t,x}}(\mathcal C_\tau)
&=
|\mu_\tau^{t,x}|(A_\tau)
+
|\mu_\tau^{t,x}(A_\tau^c)|\\
&\leq
|F_\tau(t,x)|
+2\varepsilon_\tau.
\end{aligned}
\tag{22}
$$

Summing gives

$$
\sum_\tau
V_{\mu_\tau^{t,x}}(\mathcal C_\tau)<\infty.
\tag{23}
$$

Thus, at every fixed observation point in the C-prime regime, there are nonconstant \(L^1\) coarsenings which retain the complete raw Gaussian configuration on small nonnull pieces of mark space. This resolves the literal existential version of Conjecture C; what remains open is the construction of natural, non-sparse, target-uniform coarsenings with useful retained information.

## Explicit example: retaining only time can fail

The converse intuition is also false. A coarsening can forget every Gaussian coordinate and retain only a one-dimensional time variable while leaving a nonsummable amount of sign variation.

For \(n\geq1\), take

$$
\Omega_n=(0,1)\times\mathbb R^n,
\qquad
\nu_n=dt\otimes\gamma_n,
$$

and set

$$
R_n(t,z)
=
2^{-n}+h(t),
\tag{24}
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

so constant coarsening has summable total variation. Now retain only time,

$$
\mathcal C_n(t,z)=t.
\tag{25}
$$

All Gaussian coordinates are averaged out, but

$$
\mathbb E_{\nu_n}[R_n\mid t]
=
2^{-n}+h(t).
$$

Since \(2^{-n}<1\),

$$
V_{\mu_n}(\mathcal C_n)
=
\int_0^1|2^{-n}+h(t)|dt
=1.
\tag{26}
$$

Hence

$$
\sum_nV_{\mu_n}(\mathcal C_n)=\infty.
\tag{27}
$$

Nothing singular is being retained except the branch-time coordinate. The failure is entirely the residual sign variation visible as a function of that time.

## Sanity check: the three quadratic-Hessian points

The exact characterization places the known constructions exactly where the previous theorems put them.

### Raw-faithful / identity

For identity coarsening,

$$
\mathbb E[R_\tau\mid\sigma(\operatorname{Id})]
=R_\tau,
$$

so the residual variation is the full raw total variation. The fixed-datum right-comb theorem gives a divergent subseries. Hence the characterization predicts non-\(L^1\), exactly as proved in [Raw-barycenter L1 obstruction for the quadratic Hessian PDE](raw-marked-l1-obstruction-for-quadratic-hessian-pde.md).

### Time-spine coarsening

For the time-spine map, the conditional barycenter given the retained root-spine times is precisely the deterministic patch density obtained after averaging the Gaussian/Brownian marks and the side-subtree interiors. The [time-spine theorem](time-spine-coarsening-for-quadratic-hessian-patches.md) proves that the sum of the corresponding residual variations is finite under

$$
4a<1,
\qquad
bC(a)<1.
$$

Hence the characterization predicts \(L^1\), exactly as already proved.

### Constant coarsening / C-prime

For the constant map,

$$
V_{\mu_\tau}(\mathcal C_\tau)
=|\mu_\tau(\Omega_\tau)|
=|F_\tau(t,x)|.
$$

Theorem C-prime proves

$$
\sum_\tau|F_\tau(t,x)|<\infty
$$

throughout the Catalan regime. Again the characterization gives exactly the known answer.

There is therefore no conflict among the three levels. They are three different values of the same invariant.

## What remains open

The exact characterization closes the existential question for arbitrary skeleton-preserving coarsenings at a fixed observation point, but it does not make every representation question trivial. Natural remaining problems include:

1. **Structured full-regime coarsening.** Find a non-sparse coarsening with a fixed geometric description, rather than a set chosen only to make residual variation small, which is \(L^1\) throughout the C-prime regime.
2. **Target-uniform schemes.** Construct one coarsening architecture which works uniformly in \((t,x)\), with quantitative control in a function-space norm rather than pointwise selection of small sets.
3. **Information-constrained optimization.** Given a prescribed retained sigma-field or a computational budget, minimize
   $$
   \int
   |\mathbb E[R_\tau\mid\mathcal G_\tau]|d\nu_\tau
   $$
   over admissible coarsenings.
4. **Natural Gaussian intermediates.** Naive patchwise bridge coarsening fails on one-edge obstruction patches, but more global Gaussian coarsenings or couplings may still have controlled residual variation.
5. **Cross-skeleton cancellation.** If the skeleton label itself may be coarsened, the correct invariant remains residual total variation after the enlarged pushforward, but the interaction with the infinite skeleton series requires a separate formulation.

The conceptual endpoint is nevertheless exact: **cancellation before absolute values is precisely the removal of signed variation by conditional averaging, and integrability is equivalent to summability of the variation which remains.**
