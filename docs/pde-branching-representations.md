# Probabilistic representations for nonlinear PDEs

This part of the wiki studies probabilistic representations of nonlinear parabolic PDEs with derivative weights. Its starting point is a distinction that is easy to miss:

> a branching construction may be an exact **signed** Duhamel identity while failing to define an \(L^1\) random variable.

Derivative weights make this distinction structural. A centered Gaussian identity such as

$$
\partial_x^2P_rf(x)
=
\frac1r
\mathbb E\left[
He_2(Z)
\bigl(f(x+\sqrt rZ)-f(x)\bigr)
\right]
$$

is useful precisely because cancellation occurs before the absolute value. The programme below identifies the exact invariant behind that statement.

If a finite raw marked skeleton contribution is the signed measure

$$
\mu_\tau=R_\tau\nu_\tau,
$$

with \(\nu_\tau\) finite positive, and \(\mathcal C_\tau\) records the variables retained after coarsening, then

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

Thus **cancellation before absolute values is removal of signed variation by conditional averaging**. For skeleton-preserving coarsenings, summability of the residual variations in (A) is necessary and sufficient for \(L^1\) in the associated conditional-barycenter class. The type of retained coordinate is not the invariant.

The measure-theoretic background for (A) is contained in [Finite signed measures, pushforwards, and conditional barycenters](entries/finite-signed-measures-pushforwards-and-conditional-barycenters.md).

## Shortest self-contained path to the capstone

A reader with graduate probability and a first PDE course can reach the final theorem without leaving the wiki by following this chain.

1. [Mild formulation and branching-diffusion representation](entries/mild-formulation-and-branching-diffusion-representation.md).
2. [Branching diffusions and Duhamel trees](entries/branching-diffusions-and-duhamel-trees.md) and [Importance-sampling compensators](entries/importance-sampling-compensators.md).
3. [Finite signed measures, pushforwards, and conditional barycenters](entries/finite-signed-measures-pushforwards-and-conditional-barycenters.md).
4. [Gaussian integration by parts and automatic differentiation](entries/gaussian-integration-by-parts-and-automatic-differentiation.md), [Hermite polynomials and Gaussian chaos](entries/hermite-polynomials-and-gaussian-chaos.md), and [Hölder cancellation for heat-semigroup derivatives](entries/holder-cancellation-for-heat-semigroup-derivatives.md).
5. [Parabolic Hölder spaces](entries/parabolic-holder-spaces.md) and [Parabolic Hölder bound for the Hessian Duhamel operator](entries/parabolic-holder-bound-for-hessian-duhamel-operator.md).
6. [Finite-depth Duhamel patch regrouping](entries/finite-depth-duhamel-patch-regrouping.md) and [Conditional factorization for finite PDE patches](entries/conditional-factorization-for-finite-pde-patches.md).
7. [Skeleton-averaged \(L^1\) representation](entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md).
8. [Lacunary and Hadamard-gap trigonometric series](entries/lacunary-and-hadamard-gap-trigonometric-series.md), [Disjoint-event lower bounds for compensated branching estimators](entries/disjoint-event-lower-bounds-for-compensated-branching-estimators.md), and [Brownian confinement and heat-kernel positivity](entries/brownian-confinement-and-heat-kernel-positivity.md).
9. [Raw-barycenter \(L^1\) obstruction](entries/raw-marked-l1-obstruction-for-quadratic-hessian-pde.md).
10. [Time-spine coarsening](entries/time-spine-coarsening-for-quadratic-hessian-patches.md).
11. [Residual signed variation characterization](entries/residual-signed-variation-characterization-for-coarsened-patches.md).

The coding-tree results form Act I of the paper. They motivate why representation architecture matters, but they are not prerequisites for the proof of (A).

## Act I: exactness does not imply L1

The Nguwi--Penent--Privault setting is

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

The [Nguwi--Penent--Privault coding tree](entries/npp-coding-tree.md) propagates differential codes. Their [coding-tree Feynman--Kac theorem](entries/npp-coding-tree-feynman-kac-theorem.md) is conditional on absolute integrability of every required code-rooted functional.

The [repeated-Hessian obstruction](entries/repeated-hessian-obstruction-for-coding-trees.md) isolates a distinguished genealogy. For an active direction \(j\), an allowed composite code \(g^*\), and bounded measurable \(B\), put

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

The [Gevrey-1/2 necessity theorem](entries/gevrey-half-necessity-for-coding-trees.md) gives the converse type of statement: integrability of the relevant even and odd roots forces

$$
|\partial_{z_j}^r f(J_n\phi(y))|
\leq
C_yA_y^r\Gamma(r/2+1)
$$

for almost every \(y\). Hence the formal directional Taylor series is entire with at most Gaussian growth.

The [representation-level dichotomy](entries/representation-level-dichotomy.md) shows that this is a property of the representation architecture, not merely the PDE. For

$$
\partial_tu+
\frac12u_{xx}
+
\eta(e^{(u_x)^4}-1)=0,
\qquad
u(T,x)=a\cos x,
$$

the raw NPP functional is non-\(L^1\) at every positive horizon for the stated amplitude range, while an explicit [HLOTW marked branching](entries/marked-branching-diffusion-for-gradient-nonlinearities.md) estimator is \(L^2\) for

$$
0<T<
\frac1{2\pi e(e-1)^2\eta^2}.
$$

## Quadratic Hessian equation

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

on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). With \(z=v_{xx}\),

$$
z(t)
=
P_t\phi''
+
\lambda\int_0^t
\partial_x^2P_{t-s}[z(s)^2]ds.
\tag{1}
$$

Finite Picard expansion produces rooted planar binary Duhamel trees. A **patch** is a maximal chain obtained by repeatedly following the left child. The [finite-depth patch theorem](entries/finite-depth-duhamel-patch-regrouping.md) proves that replacing each such chain by its complete iterated Duhamel integral is an exact finite reindexing. The [finite conditional-factorization theorem](entries/conditional-factorization-for-finite-pde-patches.md) gives the corresponding finite probabilistic statement.

The [self-consistent deterministic iteration](entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md) is auxiliary. Its smallness condition is

$$
|\lambda|C_{\mathrm{Sch}}(\alpha,T)
\|\phi\|_{C^{2+\alpha}}
\leq\frac18.
$$

It gives a classical solution and uniqueness only in the class \(|\lambda v_{xx}|\le1/8\). This condition and uniqueness class are distinct from the C-prime assumptions below.

## C-prime: complete interior averaging

Let

$$
X=X_{\alpha,T}
=C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
$$

and

$$
(\mathcal Df)(t)
=
\int_0^t
\partial_x^2P_{t-s}f(s)ds.
$$

The [Hessian Duhamel estimate](entries/parabolic-holder-bound-for-hessian-duhamel-operator.md) gives

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

For a finite tree \(\tau\), let \(F_\tau\) be the deterministic profile obtained after every continuous variable inside that skeleton has been averaged. Then

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

Sampling only the discrete skeleton gives an unbiased \(L^1\) estimator for every \((t,x)\). This is [Theorem C-prime](entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md).

The deterministic and C-prime solutions are identified only when both smallness conditions hold **and** the C-prime profile itself satisfies \(|\lambda z_*|\le1/8\).

## Four routes through the fluctuation problem

The route map remains useful because the capstone identifies what each route was implicitly controlling.

1. **Fixed pathwise Hölder / same-regularity Besov.** A raw edge does not close at the same pathwise regularity.
2. **Decreasing Banach scale.** The [Banach-scale obstruction](entries/banach-scale-obstruction-for-raw-pde-patches.md) gives the sharp \(1/\delta\) one-edge cost and an unavoidable \((cn/\Delta)^n\) stepwise majorant under a fixed total regularity budget. This is a proof-architecture barrier, not a fixed-datum divergence theorem.
3. **Joint centered marks.** The [joint centered-mark theorem](entries/joint-centered-mark-dichotomy-for-raw-pde-patches.md) delays the first absolute value across several Gaussian marks. Retaining all canonical marks gives sharp factorial block growth; signed bridge averaging gives geometric growth on genuine multi-edge blocks by passing to a coarser Gaussian sigma-field.
4. **Complete interior averaging.** C-prime takes the trivial interior sigma-field for each skeleton and retains only its total signed mass.

These are different attempts to reduce the residual conditional \(L^1\) norm in (A).

## Fixed-datum raw-faithful obstruction

The [raw-barycenter obstruction](entries/raw-marked-l1-obstruction-for-quadratic-hessian-pde.md) removes the generation-dependent-frequency caveat. Choose

$$
N_m=K^m,
\qquad
b_m=(m!)^{-1/2},
$$

and place all these modes in one smooth Hessian datum. On right-oriented combs,

$$
\|\mu_m\|_{\mathrm{TV}}
\gtrsim
\varepsilon(C|\lambda|\varepsilon)^m
\frac{m^m}{\sqrt{m!}},
\tag{3}
$$

so a disjoint comb subseries diverges.

The theorem applies to **raw-faithful** schemes: after the canonical raw state is exposed, the canonical signed contribution must remain the estimator's conditional barycenter. It does **not** quantify over all unbiased estimators. Within that class, changing lifetime, genealogy, or Gaussian proposals, allowing dependencies between proposal variables, or adding auxiliary conditionally unbiased randomness cannot improve the first moment.

The datum can be scaled into the C-prime regime. Thus the same small smooth datum has an \(L^1\) C-prime representation and no raw-faithful \(L^1\) representation.

## Exact coarsening characterization

The capstone is [Residual signed variation characterizes coarsened patch representations](entries/residual-signed-variation-characterization-for-coarsened-patches.md). Formula (A) is the one-skeleton identity.

If the countable skeleton label is retained, the canonical coarsened importance sampler satisfies

$$
\mathbb E|Y|
=
\sum_\tau V_\tau(\mathcal C_\tau),
\tag{4}
$$

and therefore

$$
Y\in L^1
\quad\Longleftrightarrow\quad
\sum_\tau V_\tau(\mathcal C_\tau)<\infty.
\tag{5}
$$

Conditional Jensen proves that this sum is also the minimum first moment among all auxiliary estimators with the same coarsened conditional barycenter. If the skeleton label itself is coarsened, the same signed-measure principle applies after enlarging the raw state to include the skeleton label, but the separate sum in (4) need not remain the invariant.

Two examples show why the theorem is not a statement about Gaussian randomness.

- The entire Gaussian vector may be retained on small nonnull pieces while the residual variations remain summable.
- Retaining only a one-dimensional time coordinate may leave residual variation equal to one at every level, even after every Gaussian coordinate has been averaged out.

Only the signed variation visible through the retained sigma-field matters.

### Fixed-target sparse retention

At each fixed \((t,x)\) in the C-prime regime, one can retain the entire raw state on suitably small nonnull sets and collapse their complements. This gives a nonconstant \(L^1\) coarsening throughout the full C-prime regime. The construction may depend on \((t,x)\), so it does **not** give one target-uniform architecture.

### Structured time-spine representation

The [time-spine theorem](entries/time-spine-coarsening-for-quadratic-hessian-patches.md) gives one fixed geometric rule for every target: retain the ordered branch times on the root maximal-left patch and average every Gaussian/Brownian mark there together with all continuous variables in the side subtrees.

Let

$$
b=|\lambda|K_{\mathrm{time}}(\alpha,T)M,
\qquad
C(a)=\frac{1-\sqrt{1-4a}}{2a},
\quad C(0)=1.
$$

If

$$
\boxed{
4a<1,
\qquad
bC(a)<1,
}
\tag{6}
$$

then

$$
\sum_\tau
V_\tau(\mathcal C_\tau^{\mathrm{time}})
\leq
\frac{M}{1-bC(a)}
<\infty
$$

uniformly in the target. The branch-time vector affects the estimator nontrivially. The extra condition may be stronger than C-prime; its exact strength depends on \(K_{\mathrm{time}}/C_{\mathcal D}\).

### Why naive patchwise Gaussian bridges fail

The fixed-datum obstruction can be realized on right combs. Under the maximal-left-spine convention every patch of a right comb has one edge. A one-edge bridge map has no internal bridge coordinate to remove, so it generates the same retained sigma-field as identity, up to an invertible coordinate change. The divergent residual variation therefore survives unchanged.

## What remains open

The [random-patch conjecture](entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md) is now a **structured target-uniform** problem. The arbitrary fixed-target existence question is solved. Natural remaining problems are:

1. a non-sparse geometrically defined coarsening throughout the full C-prime regime;
2. a target-uniform structured representation on that full regime with function-space control;
3. optimization of residual variation under information or computational constraints;
4. natural Gaussian coarsenings beyond the failed patchwise bridge map;
5. cross-skeleton coarsenings in which the skeleton label itself may be averaged.

## Full reading map

### Foundations

- [Heat-reference fully nonlinear terminal PDE](entries/heat-reference-fully-nonlinear-pde.md)
- [Mild formulation and branching-diffusion representation](entries/mild-formulation-and-branching-diffusion-representation.md)
- [Feynman--Kac formula for linear parabolic equations](entries/feynman-kac-formula-for-linear-parabolic-equations.md)
- [Branching diffusions and Duhamel trees](entries/branching-diffusions-and-duhamel-trees.md)
- [Age-dependent branching and finite-horizon nonexplosion](entries/age-dependent-branching-and-nonexplosion.md)
- [Importance-sampling compensators](entries/importance-sampling-compensators.md)
- [Finite signed measures, pushforwards, and conditional barycenters](entries/finite-signed-measures-pushforwards-and-conditional-barycenters.md)
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
