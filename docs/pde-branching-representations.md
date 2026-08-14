# Probabilistic representations for nonlinear PDEs

This part of the wiki studies probabilistic representations of nonlinear parabolic PDEs, with particular attention to derivative weights. The basic distinction is:

> a branching construction may be an exact **signed** Duhamel identity while failing to define an \(L^1\) random variable.

For linear equations, Feynman--Kac and backward-Kolmogorov formulas provide the model. For nonlinear equations, Duhamel's formula produces products of unknown solution values, and branching turns those products into products over descendants. If the nonlinearity contains spatial derivatives, Gaussian integration by parts, Malliavin/Bismut weights, or a differential coding system transfers derivatives to the sampled motion. These derivative weights are singular on short edges. Where cancellation occurs before the first absolute value is therefore part of the representation architecture.

The final conclusion of the programme is exact. For a finite raw marked skeleton measure

$$
\mu_\tau=R_\tau\nu_\tau
$$

and a retained sigma-field \(\sigma(\mathcal C_\tau)\), the first-moment cost which survives the coarsening is

$$
\boxed{
\|(\mathcal C_\tau)_\#\mu_\tau\|_{\mathrm{TV}}
=
\int
\left|
\mathbb E_{\nu_\tau}
[R_\tau\mid\sigma(\mathcal C_\tau)]
\right|d\nu_\tau.
}
\tag{A}
$$

Thus **cancellation before absolute values is removal of signed variation by conditional averaging**. For skeleton-preserving coarsenings, summability of the residual variations in (A) is necessary and sufficient for \(L^1\) in the corresponding conditional-barycenter class. The type of retained coordinate is not the invariant.

## Act I: coding trees show that exactness does not imply L1

The broad Nguwi--Penent--Privault setting is

$$
\partial_tu(t,x)
+
\frac12\partial_x^2u(t,x)
+
f(J_nu(t,x))
=0,
\qquad
u(T,x)=\phi(x),
$$

where

$$
J_nu=(u,u_x,\ldots,u_{x^n}).
$$

The [Nguwi--Penent--Privault coding tree](entries/npp-coding-tree.md) propagates differential codes. Repeated spatial differentiation generates arbitrarily high derivatives of the jet nonlinearity. Their [Feynman--Kac theorem](entries/npp-coding-tree-feynman-kac-theorem.md) is conditional on absolute integrability of every code-rooted functional required by the recursion.

The [repeated-Hessian obstruction](entries/repeated-hessian-obstruction-for-coding-trees.md) isolates a distinguished genealogy. For an active direction \(j\), an allowed composite code \(g^*\), and bounded measurable \(B\), define

$$
D_m(B;g,j)
=
\int_B
\left|
\partial_{z_j}^{2m}g(J_n\phi(y))
\right|dy.
$$

If

$$
\limsup_{m\to\infty}
\left(
\frac{D_m(B;g,j)}{m!}
\right)^{1/m}
=
\infty,
$$

then the raw code-rooted functional is non-\(L^1\) at every positive remaining horizon. Lifetime, mechanism-selection, and survival probabilities cancel their reciprocal compensators; the ordered branch-time simplex contributes \(1/m!\).

The converse direction is the [Gevrey-1/2 necessity theorem](entries/gevrey-half-necessity-for-coding-trees.md). Integrability of the relevant even and odd code roots forces, almost everywhere,

$$
|\partial_{z_j}^r f(J_n\phi(y))|
\leq
C_yA_y^r\Gamma(r/2+1).
$$

Thus the formal directional Taylor series is entire with at most Gaussian growth. The [finite directional radius theorem](entries/finite-directional-radius-obstruction.md) is a convenient special case.

## Representation-level dichotomy

The coding-tree obstruction is representation-specific rather than a theorem that the PDE itself has no integrable probabilistic representation. The proved [representation-level dichotomy](entries/representation-level-dichotomy.md) compares two constructions for

$$
\partial_tu+
\frac12u_{xx}
+
\eta(e^{(u_x)^4}-1)=0,
\qquad
u(T,x)=a\cos x.
$$

For

$$
0<a\leq
\frac{\operatorname{erfc}(1/\sqrt2)}{\sqrt3},
$$

the raw NPP functional is non-\(L^1\) at every positive horizon. By contrast, an explicit [HLOTW marked branching](entries/marked-branching-diffusion-for-gradient-nonlinearities.md) estimator is \(L^2\) for

$$
0<T<
\frac1{2\pi e(e-1)^2\eta^2}.
$$

This benchmark establishes the first structural lesson: the moment question is determined by representation architecture, not by signed exactness alone.

## Quadratic Hessian equation and finite patches

The main representation programme concerns

$$
\partial_tv
=
\frac12v_{xx}
+
\lambda(v_{xx})^2,
\qquad
v(0)=\phi,
$$

on

$$
\mathbb T=\mathbb R/(2\pi\mathbb Z).
$$

Writing \(z=v_{xx}\) gives

$$
z(t)
=
P_t\phi''
+
\lambda\int_0^t
\partial_x^2P_{t-s}[z(s)^2]ds.
\tag{1}
$$

Finite Picard expansion produces rooted planar binary Duhamel trees. A **patch** is a maximal chain obtained by repeatedly following the left child. The [finite-depth patch theorem](entries/finite-depth-duhamel-patch-regrouping.md) proves that replacing every such chain by its complete iterated Duhamel integral is an exact finite reindexing. The [finite conditional-factorization theorem](entries/conditional-factorization-for-finite-pde-patches.md) gives the corresponding finite probabilistic statement.

The regrouping changes the unit at which an absolute value is taken. A centered Hessian edge has

$$
\partial_x^2P_rf(x)
=
\frac1r
\mathbb E\left[
He_2(Z)
\bigl(f(x+\sqrt rZ)-f(x)\bigr)
\right],
$$

so mean-zero Hermite cancellation yields

$$
\|\partial_x^2P_rf\|_\infty
\lesssim
r^{-1+\alpha/2}[f]_{C^\alpha}.
$$

The [Hölder-cancellation entry](entries/holder-cancellation-for-heat-semigroup-derivatives.md) develops the higher-order and commutator versions.

## Auxiliary deterministic theorem

The [self-consistent deterministic iteration](entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md) is useful but auxiliary. Under a uniform Schauder smallness condition, the semi-implicit iteration

$$
\partial_tz_{n+1}
=
\partial_x^2
\left[
\left(\frac12+\lambda z_n\right)z_{n+1}
\right]
$$

stays in a fixed ellipticity window and contracts in \(H^{-1}\). It gives a unique small uniformly parabolic solution and an implicit self-consistent diffusion representation.

## C-prime: complete interior averaging

Let

$$
X_{\alpha,T}
=
C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
$$

and

$$
(\mathcal Df)(t)
=
\int_0^t
\partial_x^2P_{t-s}f(s)ds.
$$

The [parabolic Hölder bound](entries/parabolic-holder-bound-for-hessian-duhamel-operator.md) gives

$$
\|\mathcal D(fg)\|_X
\leq
C_{\mathcal D}(\alpha,T)
\|f\|_X\|g\|_X.
$$

Put

$$
M=\|P_\cdot\phi''\|_X,
\qquad
 a=|\lambda|C_{\mathcal D}(\alpha,T)M.
$$

For a finite planar binary tree \(\tau\), let \(F_\tau\) be the deterministic profile obtained after all continuous branch-time, Gaussian/Hermite, Brownian, and descendant variables inside the skeleton have been averaged. Then

$$
\|F_\tau\|_X
\leq
Ma^{|\tau|}.
$$

The Catalan count gives absolute summability under

$$
\boxed{4a<1}.
\tag{2}
$$

Sampling only the discrete skeleton gives an unbiased \(L^1\) estimator. This is [Theorem C-prime](entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md).

C-prime is defined directly through deterministic Duhamel profiles, not as a conditional expectation of an unresolved infinite nonintegrable raw object.

## Four routes through the fluctuation problem

The earlier route map remains useful; the capstone theorem now identifies what each route was measuring.

1. **Fixed pathwise Hölder / same-regularity Besov.** A raw edge does not close at the same pathwise regularity. This attempts to control too fine a retained sigma-field by a pathwise norm.
2. **Decreasing Banach scale.** The [Banach-scale obstruction](entries/banach-scale-obstruction-for-raw-pde-patches.md) proves the sharp cost \(1/\delta\) per step and the lower bound
   $$
   c^n\left(\frac n\Delta\right)^n
   $$
   under a fixed total regularity budget. This is a barrier to stepwise first-moment control.
3. **Joint centered marks.** The [joint centered-mark theorem](entries/joint-centered-mark-dichotomy-for-raw-pde-patches.md) delays the absolute value across several Gaussian marks. Two marks give a genuine gain, but the all-order raw retained block has sharp scale \(C^m m!\). Signed bridge averaging reduces the bare-chain coefficient to geometric growth by coarsening the Gaussian sigma-field.
4. **Complete interior averaging.** C-prime takes the trivial interior sigma-field for each skeleton and retains only its total signed mass.

The route history is therefore not superseded. It is reinterpreted as a sequence of attempts to reduce the residual conditional \(L^1\) norm in (A).

## Fixed-datum raw-faithful obstruction

The [raw-barycenter obstruction](entries/raw-marked-l1-obstruction-for-quadratic-hessian-pde.md) removes the generation-dependent-frequency caveat of the earlier barriers.

Choose

$$
N_m=K^m,
\qquad
b_m=(m!)^{-1/2},
$$

and put every frequency into one smooth Hessian datum

$$
g_\varepsilon(x)
=
\varepsilon
\left[
\cos x+
\sum_{m\ge m_0}b_m\cos(N_mx)
\right].
$$

The obstruction may be realized on **right-oriented combs**. Restricting each of the \(m\) Hessian durations to

$$
N_m^{-2}
\leq r_j\leq
\frac h{4m}
$$

gives one logarithmic factor per raw centered edge and

$$
\|\mu_m\|_{\mathrm{TV}}
\gtrsim
\varepsilon(C|\lambda|\varepsilon)^m
\frac{m^m}{\sqrt{m!}}.
\tag{3}
$$

The disjoint comb subseries diverges. If an estimator must retain this canonical raw signed contribution as its conditional barycenter, conditional Jensen gives infinite first moment for every positive proposal. The datum can be scaled into the C-prime regime, yielding the clean same-data contrast:

> complete interior averaging is \(L^1\), while raw-faithful retention is not.

## Exact coarsening characterization

The capstone result is [Residual signed variation characterizes coarsened patch representations](entries/residual-signed-variation-characterization-for-coarsened-patches.md).

For one skeleton, write

$$
\mu_\tau=R_\tau\nu_\tau,
$$

with \(\nu_\tau\) finite positive. For a measurable skeleton-preserving coarsening \(\mathcal C_\tau\),

$$
\frac{d(\mathcal C_\tau)_\#\mu_\tau}
{d(\mathcal C_\tau)_\#\nu_\tau}
(\mathcal C_\tau(\omega))
=
\mathbb E_{\nu_\tau}
[R_\tau\mid\sigma(\mathcal C_\tau)](\omega).
$$

Therefore (A) holds. If \(\mathcal C_1\) is coarser than \(\mathcal C_2\), the tower property and conditional Jensen imply

$$
V_\tau(\mathcal C_1)
\leq
V_\tau(\mathcal C_2).
$$

Identity gives full raw total variation; constant coarsening gives \(|F_\tau(t,x)|\).

For a countable skeleton family, the canonical coarsened importance sampler satisfies

$$
\mathbb E|Y|
=
\sum_\tau
V_\tau(\mathcal C_\tau).
\tag{4}
$$

Thus

$$
Y\in L^1
\quad\Longleftrightarrow\quad
\sum_\tau V_\tau(\mathcal C_\tau)<\infty.
\tag{5}
$$

Conditional Jensen proves that no auxiliary estimator with the same coarsened conditional barycenter can have a smaller first moment; the canonical Radon--Nikodym estimator attains equality.

The theorem is exact for the skeleton-preserving class used in the manuscript. If the skeleton label itself is also coarsened, then the same principle applies to the larger pushforward state, but the per-skeleton sum need not remain the correct formula.

## Gaussian survival is not the invariant

Two explicit examples make the characterization nontrivial.

First, there are Gaussian families with raw variation \(1\) on every level but total signed mass \(2^{-n}\). One may retain the **entire Gaussian vector** on a symmetric slab of Gaussian probability \(2^{-n}\) and collapse the complement. The residual variation is then less than \(2^{1-n}\), hence summable. Full Gaussian information may therefore survive on small pieces without obstructing \(L^1\).

Second, there are families with total signed mass \(2^{-n}\) but conditional signed density

$$
2^{-n}+h(t),
\qquad
h(t)=\pm1
$$

when only a one-dimensional time coordinate is retained. The residual variation is exactly \(1\) on every level. All Gaussian variables have been averaged away, yet the representation is non-\(L^1\).

Hence ``Gaussian retained'' and ``time retained'' are not mathematical categories for integrability. The retained sigma-field matters only through the signed variation visible through it.

## Sparse full-state retention at a fixed target

The exact theorem gives another useful consequence. Fix \((t,x)\) in the C-prime regime. Since

$$
\sum_\tau|F_\tau(t,x)|<\infty,
$$

and each finite non-leaf raw patch total-variation measure is nonatomic on its continuous coordinates, choose nonnull sets \(A_\tau\) with summably small raw variation. Retain the **entire raw state** on \(A_\tau\) and collapse \(A_\tau^c\). Then

$$
V_\tau
\leq
|F_\tau(t,x)|
+2|\mu_\tau^{t,x}|(A_\tau),
$$

so the residual variations are summable.

Thus the fixed-target existential question for nonconstant retained randomness is closed throughout the full C-prime regime. This does **not** automatically produce one target-uniform architecture valid simultaneously for every \((t,x)\).

## Structured hierarchy as a sanity check

The three previously proved structured points sit exactly where the characterization predicts.

### Raw-faithful / identity

Identity retains the full raw sigma-field, hence

$$
V_\tau(\operatorname{Id})
=
\|\mu_\tau\|_{\mathrm{TV}}.
$$

The right-comb subseries diverges for the fixed smooth datum.

### Time-spine coarsening

The [time-spine theorem](entries/time-spine-coarsening-for-quadratic-hessian-patches.md) retains the actual ordered branch times on one root maximal-left patch and averages all Gaussian/Brownian marks and all continuous variables in the attached side subtrees.

Let

$$
b=|\lambda|K_{\mathrm{time}}(\alpha,T)M,
$$

and

$$
C(a)
=
\frac{1-\sqrt{1-4a}}{2a},
\qquad C(0)=1.
$$

If

$$
4a<1,
\qquad
bC(a)<1,
\tag{6}
$$

then

$$
\sum_\tau
V_\tau(\mathcal C_\tau^{\mathrm{time}})
\leq
\frac{M}{1-bC(a)}
<\infty.
$$

The retained time vector affects the estimator nontrivially.

### C-prime / constant

Constant coarsening gives

$$
V_\tau(\mathrm{const})
=|F_\tau(t,x)|,
$$

summable under the full Catalan condition \(4a<1\).

There is no inconsistency among the three results: they are three different values of the same invariant.

## Why naive patchwise Gaussian bridges still fail

Patches are maximal **left-child** chains. The obstruction can be realized on right combs, where every left child is terminal and every continuing internal child is right. Hence every maximal-left patch on the obstruction genealogy has one edge.

A one-edge Gaussian bridge map has no bridge coordinate to remove. It generates the same retained Gaussian sigma-field as identity, up to an invertible coordinate change. The divergent residual variation (3) therefore survives unchanged. Genuine multi-edge patches still benefit locally from bridge averaging; the obstruction family simply never presents one.

## What remains open

The [random-patch conjecture](entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md) is now best read as a **target-uniform structured** problem. The fixed-target existential relaxation is solved by sparse full-state retention. The time-spine theorem gives one target-uniform structured architecture on the stronger regime (6).

Natural remaining problems are:

1. find a non-sparse geometrically defined coarsening which works throughout the full C-prime regime;
2. obtain one target-uniform architecture with function-space rather than pointwise total-variation control;
3. optimize residual variation under information or computational constraints;
4. construct natural Gaussian coarsenings beyond the failed patchwise bridge map;
5. formulate cross-skeleton coarsenings in which the skeleton label itself may be averaged.

## Reading map

### Foundations

- [Heat-reference fully nonlinear terminal PDE](entries/heat-reference-fully-nonlinear-pde.md)
- [Mild formulation and branching-diffusion representation](entries/mild-formulation-and-branching-diffusion-representation.md)
- [Feynman--Kac formula for linear parabolic equations](entries/feynman-kac-formula-for-linear-parabolic-equations.md)
- [Branching diffusions and Duhamel trees](entries/branching-diffusions-and-duhamel-trees.md)
- [Age-dependent branching and finite-horizon nonexplosion](entries/age-dependent-branching-and-nonexplosion.md)
- [Importance-sampling compensators](entries/importance-sampling-compensators.md)
- [Disjoint-event lower bounds for compensated branching estimators](entries/disjoint-event-lower-bounds-for-compensated-branching-estimators.md)
- [Uniform integrability and passage to expectations](entries/uniform-integrability-and-passage-to-expectations.md)
- [Gaussian integration by parts and automatic differentiation](entries/gaussian-integration-by-parts-and-automatic-differentiation.md)
- [Malliavin and Bismut automatic differentiation](entries/malliavin-and-bismut-automatic-differentiation.md)
- [Hermite polynomials and Gaussian chaos](entries/hermite-polynomials-and-gaussian-chaos.md)
- [Brownian confinement and heat-kernel positivity](entries/brownian-confinement-and-heat-kernel-positivity.md)
- [Lacunary and Hadamard-gap trigonometric series](entries/lacunary-and-hadamard-gap-trigonometric-series.md)
- [Total variation, bounded variation, and derivative singularities](entries/total-variation-bounded-variation-and-derivative-singularities.md)
- [Tonelli, Markov, and Borel--Cantelli](entries/tonelli-markov-and-borel-cantelli.md)

### Parabolic regularity and function spaces

- [Hölder cancellation for heat-semigroup derivatives](entries/holder-cancellation-for-heat-semigroup-derivatives.md)
- [Parabolic Hölder spaces](entries/parabolic-holder-spaces.md)
- [Parabolic Hölder bound for the Hessian Duhamel operator](entries/parabolic-holder-bound-for-hessian-duhamel-operator.md)
- [Random fields in function spaces](entries/random-fields-in-function-spaces.md)
- [Conditional expectation and fluctuations of random fields](entries/conditional-expectation-and-fluctuations-of-random-fields.md)
- [Besov spaces on the torus](entries/besov-spaces-on-the-torus.md)
- [Parabolic maximum principle and Schauder estimates](entries/parabolic-maximum-principle-and-schauder-estimates.md)
- [Interior Hölder estimates for parabolic equations](entries/interior-holder-estimates-for-parabolic-equations.md)
- [Aronson and Nash Gaussian bounds](entries/aronson-nash-gaussian-bounds.md)
- [\(H^{-1}\) energy method](entries/h-minus-one-energy-method.md)
- [Weak parabolic solutions on the torus](entries/weak-parabolic-solutions-on-the-torus.md)
- [Itô diffusions and backward Kolmogorov representation](entries/ito-diffusions-and-backward-kolmogorov-representation.md)

### Branching constructions and coding-tree results

- [Marked branching diffusion for gradient nonlinearities](entries/marked-branching-diffusion-for-gradient-nonlinearities.md)
- [Antithetic and ghost branching schemes](entries/antithetic-and-ghost-branching-schemes.md)
- [Nguwi--Penent--Privault coding tree](entries/npp-coding-tree.md)
- [Nguwi--Penent--Privault coding-tree Feynman--Kac theorem](entries/npp-coding-tree-feynman-kac-theorem.md)
- [Directional jet radius](entries/directional-jet-radius.md)
- [Repeated-Hessian obstruction for coding trees](entries/repeated-hessian-obstruction-for-coding-trees.md)
- [Finite directional radius obstruction](entries/finite-directional-radius-obstruction.md)
- [Gevrey-1/2 necessity for coding trees](entries/gevrey-half-necessity-for-coding-trees.md)
- [Integrable regime of the coding tree](entries/integrable-regime-of-coding-tree.md)
- [Dichotomy benchmark](entries/dichotomy-benchmark.md)
- [Representation-level dichotomy](entries/representation-level-dichotomy.md)

### Quadratic-Hessian patch route

- [Finite-depth Duhamel patch regrouping](entries/finite-depth-duhamel-patch-regrouping.md)
- [Conditional factorization for finite PDE patches](entries/conditional-factorization-for-finite-pde-patches.md)
- [Self-consistent patch iteration for the quadratic Hessian PDE](entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md)
- [Skeleton-averaged \(L^1\) representation for the quadratic Hessian PDE](entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md)
- [Banach-scale obstruction for raw PDE patches](entries/banach-scale-obstruction-for-raw-pde-patches.md)
- [Joint centered-mark dichotomy for raw PDE patches](entries/joint-centered-mark-dichotomy-for-raw-pde-patches.md)
- [Raw-barycenter \(L^1\) obstruction for the quadratic Hessian PDE](entries/raw-marked-l1-obstruction-for-quadratic-hessian-pde.md)
- [Time-spine coarsening for quadratic Hessian patches](entries/time-spine-coarsening-for-quadratic-hessian-patches.md)
- [Residual signed variation characterization](entries/residual-signed-variation-characterization-for-coarsened-patches.md)
- [\(L^1\) random-patch conjecture for the quadratic Hessian PDE](entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md)

The [reference list](meta/references.md) collects the literature cited throughout these pages.
