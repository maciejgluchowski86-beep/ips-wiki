# Probabilistic representations for nonlinear PDEs

This part of the wiki studies probabilistic representations of nonlinear parabolic PDEs, with a particular focus on branching constructions and on the absolute-moment problems created by derivative weights. The basic question is simple to state:

> Can the solution of a nonlinear PDE be written as the expectation of an explicitly sampled random object whose absolute moments are finite?

For linear equations, the answer is the classical Feynman--Kac or backward-Kolmogorov formula. For nonlinear equations, Duhamel's formula produces products of unknown solution values. Branching processes turn those products into products over descendants. If the nonlinearity contains derivatives of the solution, one also needs a mechanism for transferring derivatives onto the random motion: Gaussian integration by parts, Malliavin/Bismut weights, or a differential coding system.

The central issue in this wiki is that **signed exactness is much easier than absolute integrability**. A random tree can reproduce the correct Duhamel recursion after expectation and nevertheless fail to belong to \(L^1\). Much of the programme below is about locating that failure and then reorganizing the expansion so that cancellations occur before absolute values are taken.

## The reference PDE and the first Duhamel expansion

The broad Nguwi--Penent--Privault setting is the [heat-reference terminal PDE](entries/heat-reference-fully-nonlinear-pde.md)

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
J_nu=(u,u_x,\ldots,u_{x^n})
$$

is the finite spatial jet. The [mild formulation](entries/mild-formulation-and-branching-diffusion-representation.md) keeps the heat semigroup exact and writes the nonlinear term as a time integral. Repeated substitution produces deterministic [Duhamel trees](entries/branching-diffusions-and-duhamel-trees.md). Randomizing the integration times and offspring choices gives a branching representation; the reciprocal proposal probabilities are [importance-sampling compensators](entries/importance-sampling-compensators.md).

The linear model behind this construction is the [Feynman--Kac formula](entries/feynman-kac-formula-for-linear-parabolic-equations.md). The nonlinear tree should be viewed as an attempt to retain the same philosophy after products and derivatives have entered the equation.

## Why probabilistic representations are useful

A probabilistic formula can serve several different purposes. It can identify a PDE solution with an expectation, provide a Monte Carlo method that does not require a spatial grid, or expose structural information that is difficult to see from the PDE alone. These uses require different levels of control. A formal first-branch identity is enough to check algebraic exactness, but Monte Carlo requires at least \(L^1\), and quantitative simulation usually needs higher moments.

This distinction is why the wiki keeps separate entries for [nonexplosion of the branching genealogy](entries/age-dependent-branching-and-nonexplosion.md), [uniform integrability and passage to expectations](entries/uniform-integrability-and-passage-to-expectations.md), and the compensator identities. A tree can be finite almost surely and still have infinite absolute expectation.

## Two branching mechanisms

The [Nguwi--Penent--Privault coding tree](entries/npp-coding-tree.md) propagates differential *codes*. Applying the total spatial derivative and the [multivariate Faà di Bruno formula](entries/spatial-jets-total-derivative-and-faa-di-bruno.md) creates new codes recursively, so arbitrarily high jet derivatives of the nonlinearity appear along the tree. The corresponding [NPP Feynman--Kac theorem](entries/npp-coding-tree-feynman-kac-theorem.md) is conditional: it assumes the multiplicative tree functional is absolutely integrable for every code needed by the recursion.

The [Henry-Labordère--Oudjane--Tan--Touzi--Warin marked branching construction](entries/marked-branching-diffusion-for-gradient-nonlinearities.md) has a different architecture. It expands a polynomial or countable monomial driver in \((u,Du)\), branches according to those monomials, and transfers first derivatives through automatic-differentiation weights. The constant-diffusion case follows from [Gaussian integration by parts](entries/gaussian-integration-by-parts-and-automatic-differentiation.md); variable diffusions lead to [Malliavin/Bismut weights](entries/malliavin-and-bismut-automatic-differentiation.md). These weights are singular on short edges, so the lifetime density must be chosen together with the moment estimate.

The [antithetic and ghost branching schemes](entries/antithetic-and-ghost-branching-schemes.md) are related variance/cancellation devices. They become important again below because they show that “the marks remain random” is weaker than “the canonical raw integrand remains the conditional barycenter.”

## The negative coding-tree chain

The first project-level result is the [repeated-Hessian obstruction](entries/repeated-hessian-obstruction-for-coding-trees.md). Suppose a jet direction \(j\) is active at the terminal datum, \(\phi^{(j+1)}\not\equiv0\), and let \(g^*\) be an allowed composite NPP code. Define

$$
D_m(B;g,j)
=
\int_B
\left|
\partial_{z_j}^{2m}g(J_n\phi(y))
\right|\,dy.
$$

If for some bounded measurable \(B\)

$$
\limsup_{m\to\infty}
\left(
\frac{D_m(B;g,j)}{m!}
\right)^{1/m}
=
\infty,
$$

then the \(g^*\)-rooted raw NPP functional has infinite absolute expectation at every positive remaining horizon. The proof isolates a repeated Hessian genealogy. Lifetime, offspring, and survival probabilities cancel their reciprocal compensators, so the only combinatorial cost is the ordered-time simplex \(1/m!\). The derivative growth therefore remains visible in the absolute expectation.

Two consequences sharpen the obstruction. The [finite directional radius theorem](entries/finite-directional-radius-obstruction.md) shows that finite directional Taylor radius on a set of positive measure already forces failure of the all-code \(L^1\) hypothesis. The [Gevrey-1/2 necessity theorem](entries/gevrey-half-necessity-for-coding-trees.md) gives the converse style of information: if the relevant code-rooted trees are integrable, then the terminal directional derivatives must satisfy

$$
|\partial_{z_j}^r f(J_n\phi(y))|
\leq
C_yA_y^r\Gamma(r/2+1)
$$

for almost every \(y\). Thus the formal directional Taylor series must be entire with at most Gaussian growth. The [directional jet radius entry](entries/directional-jet-radius.md) contains the analytic terminology behind these statements. The [integrable-regime note](entries/integrable-regime-of-coding-tree.md) records that the NPP theorem is not vacuous; the obstruction is structural, not a statement that every coding tree diverges.

## A representation-level dichotomy

The obstruction is not merely a reflection of a difficult PDE. The [dichotomy benchmark](entries/dichotomy-benchmark.md) and the proved [representation-level dichotomy](entries/representation-level-dichotomy.md) compare two branching constructions for the same equation

$$
\partial_tu+
\frac12u_{xx}
+
\eta\left(e^{(u_x)^4}-1\right)=0,
\qquad
u(T,x)=a\cos x.
$$

For

$$
0<a\leq
\frac{\operatorname{erfc}(1/\sqrt2)}{\sqrt3},
$$

the raw NPP functional rooted at both \(f^*\) and the identity code is non-\(L^1\) at every positive horizon. By contrast, an explicit HLOTW construction has finite second moment when

$$
0<T<
\frac1{2\pi e(e-1)^2\eta^2}.
$$

The HLOTW expectation is identified with a continuous viscosity solution. The comparison is deliberately **representation-level**: it says that two exact branching architectures attached to the same PDE can have radically different absolute-moment behavior. The [viscosity-solution entry](entries/viscosity-solutions.md) states the solution concept and the role of comparison/uniqueness.

## Patch regrouping: average before taking absolute values

The project-level patch route is developed for the quadratic Hessian equation on the torus,

$$
\partial_tv
=
\frac12v_{xx}
+
\lambda(v_{xx})^2,
\qquad
v(0)=\phi,
$$

with \(z=v_{xx}\). Then

$$
z(t)
=
P_t\phi''
+
\lambda
\int_0^t
\partial_x^2P_{t-s}[z(s)^2]\,ds.
\tag{1}
$$

A naive edge-by-edge randomization applies a centered Hessian weight at every derivative edge. That is exactly where short-edge absolute moments become dangerous. The central alternative is to regroup **consecutive Hessian events first** and delay absolute values until more of the signed local structure has been combined.

The [finite-depth Duhamel patch theorem](entries/finite-depth-duhamel-patch-regrouping.md) is purely algebraic: every finite planar binary tree decomposes uniquely into maximal left-child chains, and replacing each chain by its complete multi-event Duhamel integral changes no signed term. The [finite conditional-factorization theorem](entries/conditional-factorization-for-finite-pde-patches.md) gives the probabilistic version: expose the patch genealogy and times but leave the centered Gaussian marks unexposed, so independent side patches factor after conditional expectation.

The analytic reason this helps is [Hermite cancellation](entries/hermite-polynomials-and-gaussian-chaos.md). For \(0<\alpha<1\),

$$
\partial_x^2P_rf(x)
=
\frac1r
\mathbb E\left[
He_2(Z)
\bigl(f(x+\sqrt r Z)-f(x)\bigr)
\right],
$$

and therefore

$$
\|\partial_x^2P_rf\|_\infty
\lesssim
r^{-1+\alpha/2}[f]_{C^\alpha}.
$$

The [Hölder-cancellation entry](entries/holder-cancellation-for-heat-semigroup-derivatives.md) develops this estimate and its higher-order/commutator forms. The relevant function spaces are introduced in [Parabolic Hölder spaces](entries/parabolic-holder-spaces.md), while [Besov spaces](entries/besov-spaces-on-the-torus.md) record a frequency-localized alternative.

## The deterministic theorem and Theorem C-prime

There are two different positive theorems and they should not be conflated.

The [self-consistent deterministic theorem](entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md) uses the semi-implicit iteration

$$
\partial_tz_{n+1}
=
\partial_x^2
\left[
\left(\frac12+\lambda z_n\right)z_{n+1}
\right],
\qquad
z_{n+1}(0)=\phi''.
$$

With a uniform Schauder constant \(C_{\mathrm{Sch}}(\alpha,T)\), the condition

$$
|\lambda|C_{\mathrm{Sch}}(\alpha,T)
\|\phi\|_{C^{2+\alpha}}
\leq
\frac18
$$

keeps the iteration coefficient in \([3/8,5/8]\), gives an \(H^{-1}\) contraction with ratio at most \(1/3\), and produces the unique small uniformly parabolic solution.

The stronger representation statement is [Theorem C-prime: the skeleton-averaged \(L^1\) representation](entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md). Define

$$
(\mathcal Df)(t)
=
\int_0^t
\partial_x^2P_{t-s}f(s)\,ds,
$$

and

$$
X_{\alpha,T}
=
C^{\alpha/2,\alpha}([0,T]\times\mathbb T).
$$

If

$$
M=\|P_\cdot\phi''\|_{X_{\alpha,T}}
$$

and

$$
4|\lambda|C_{\mathcal D}(\alpha,T)M<1,
\tag{2}
$$

then the deterministic profiles attached to finite decorated binary skeletons satisfy a Catalan majorant and

$$
\sum_S\|F_S\|_{X_{\alpha,T}}<\infty.
$$

Sampling a discrete skeleton \(S\) with any full-support mass function \(\pi\) and returning

$$
\widehat z(t,x)=\frac{F_S(t,x)}{\pi(S)}
$$

gives an unbiased \(L^1\) estimator. All branch-time and Gaussian/Hermite variables inside \(S\) have been integrated out before the skeleton is sampled.

## The quadratic-Hessian endpoint is now a three-way split

The earlier fork “average the interiors or retain the raw marks” was useful but is no longer precise enough.

**Complete interior averaging.** Theorem C-prime integrates every continuous interior variable first. Under (2), this is proved unbiased and \(L^1\).

**Canonical raw-barycenter retention.** The new [raw-barycenter obstruction](entries/raw-marked-l1-obstruction-for-quadratic-hessian-pde.md) proves that this endpoint is impossible in \(L^1\) for one fixed arbitrarily small smooth datum. The theorem allows arbitrary lifetime, genealogy, and Gaussian proposals, arbitrary dependence among them, and auxiliary conditionally unbiased randomness. What it forbids is moving signed mass between distinct canonical raw marked states: after the raw marks are exposed, the canonical raw signed contribution must remain the estimator's conditional barycenter.

**Non-barycentric retained randomness.** This is the surviving content of [Conjecture C](entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md). An estimator may still sample and use continuous interior marks while changing the raw conditional barycenter through antithetic pairing, partial averaging, control variates across marked states, coupled samples, or another signed reorganization. No full infinite-depth \(L^1\) construction of this kind is currently proved, and the raw-barycenter theorem does not rule one out.

This distinction matters. “The marks remain random” does not imply “the canonical raw integrand is their conditional mean.” For example, the antithetic Hessian transfer

$$
\frac{He_2(Z)}{2r}
\left[
F(x+\sqrt rZ)+F(x-\sqrt rZ)-2F(x)
\right]
$$

still uses the random mark \(Z\) and is unbiased by Gaussian symmetry, but it is not the canonical one-sided raw transfer conditional on \(Z\). It therefore lies outside the negative theorem.

## Four routes through the fluctuation problem

The four audited routes remain useful because each isolated a different failure mechanism.

**1. Fixed pathwise Hölder or same-regularity Besov control.** A single centered Hessian edge has the desired expected sup-norm gain, but its pathwise \(C^\alpha\) seminorm does not. A fixed same-regularity Besov norm has the same high-frequency translation obstruction. This rules out a fixed pathwise regularity space for the raw recursion.

**2. Decreasing Banach scale.** The [Banach-scale obstruction](entries/banach-scale-obstruction-for-raw-pde-patches.md) quantifies the cost of spending regularity. If generation \(k\) is measured in \(C^{\alpha_k}\) and \(\delta_k=\alpha_{k-1}-\alpha_k\), the sharp one-edge first-moment cost is order \(1/\delta_k\). Under any fixed total budget \(\sum_k\delta_k\leq\Delta\), a stepwise first-moment proof incurs at least

$$
c^n\prod_{k=1}^n\delta_k^{-1}
\geq
c^n\left(\frac n\Delta\right)^n.
$$

The uniform budget is optimal; nonuniform budgets are worse. This is a barrier to the stepwise first-moment Banach-scale architecture, not by itself a nonintegrability theorem.

**3. Condition all patch interiors.** Theorem C-prime integrates the continuous variables inside each finite skeleton before the skeleton is sampled. This gives an absolutely summable, unbiased \(L^1\) representation, but the continuous interior marks are gone.

**4. Joint centered marks.** The [joint centered-mark theorem](entries/joint-centered-mark-dichotomy-for-raw-pde-patches.md) does not take a norm after every centered edge. Already at two marks there is a finite joint estimate with no intermediate regularity loss, so this route genuinely escapes route 2. At length \(m\), however, retaining all canonical Gaussian marks gives the sharp uniform block scale

$$
c_{\alpha,T}^m m!
\leq
\mathfrak R_m(\alpha,T)
\leq
C_{\alpha,T}^m m!.
$$

If instead the internal Gaussian bridge coordinates are signedly averaged before the absolute value, the bare chain collapses to one \(He_{2m}\) endpoint weight and the factorial reduces to geometric growth. With spatial multipliers, the commutator/cluster expansion gives the corresponding deterministic geometric estimate. The favorable branch has altered the raw marked state by averaging bridge coordinates.

### Fixed-datum closure of route 4

The old route-2 and route-4 lower bounds had a shared caveat: their optimizing frequency changed with the depth. The raw-barycenter theorem removes that caveat.

Choose

$$
N_m=K^m,
\qquad
b_m=(m!)^{-1/2},
$$

and put all these modes into one smooth Hessian terminal datum

$$
g_\varepsilon(x)
=
\varepsilon
\left[
\cos x+
\sum_{m\ge m_0}b_m\cos(N_mx)
\right].
$$

For every fixed derivative order \(k\),

$$
\sum_m b_mN_m^k<\infty,
$$

so this is one \(C^\infty\) function. On the length-\(m\) long comb, terminal Fourier projections isolate the side frequency \(1\) and the distinguished frequency \(N_m\). Restricting every Hessian duration to

$$
N_m^{-2}
\le r_j\le
\frac{h}{4m}
$$

produces one factor

$$
\int_{N_m^{-2}}^{h/(4m)}
\frac{dr}{r}
\asymp m
$$

at each of the \(m\) retained centered edges. The rectangle lies inside the duration simplex, so there is no compensating \(1/m!\). The resulting intrinsic total variation obeys

$$
\|\nu_m\|_{\mathrm{TV}}
\gtrsim
\varepsilon(C|\lambda|\varepsilon)^m
\frac{m^m}{\sqrt{m!}},
$$

which is not summable. Conditional Jensen then transfers this divergence to every estimator whose conditional barycenter is the raw signed comb contribution.

This is the first fixed-datum non-\(L^1\) theorem in the quadratic-Hessian fluctuation route. It is also proposal invariant, because the relevant quantity is the total variation of the intrinsic signed comb measure rather than the density of any particular sampling law.

## What the programme has established

The resulting picture is sharper than the earlier “integrability versus randomness” slogan.

1. **Signed exactness is cheap.** Finite patches are exact identities.
2. **Complete averaging is sufficient.** C-prime gives a small-data \(L^1\) representation after all continuous interior variables are integrated out.
3. **Pure importance sampling cannot rescue the canonical raw integrand.** The raw-barycenter theorem rules out every proposal change and auxiliary conditionally unbiased randomization that leaves the canonical raw marked contribution as its conditional mean.
4. **The remaining possible escape must be non-barycentric.** Any surviving random-mark construction has to redistribute signed mass between raw states before the first absolute moment is taken.

The theorem does **not** prove that complete averaging is necessary. Therefore C-prime should not be called minimal or optimal among all conceivable estimators. It is the fully averaged endpoint for which a complete \(L^1\) theorem is proved. Between it and the impossible raw-barycenter endpoint lies the honest remaining problem: partial averaging, antithetic/ghost coupling, control variates, or other signed reorganizations that still retain nontrivial continuous randomness.

## Analytic and probabilistic prerequisites

The background pages used by this chain include [Random fields in function spaces](entries/random-fields-in-function-spaces.md), [Conditional expectation and fluctuations of random fields](entries/conditional-expectation-and-fluctuations-of-random-fields.md), [Tonelli, Markov, and Borel--Cantelli](entries/tonelli-markov-and-borel-cantelli.md), [Disjoint-event lower bounds for compensated branching estimators](entries/disjoint-event-lower-bounds-for-compensated-branching-estimators.md), [Brownian confinement and heat-kernel positivity](entries/brownian-confinement-and-heat-kernel-positivity.md), [Lacunary and Hadamard-gap trigonometric series](entries/lacunary-and-hadamard-gap-trigonometric-series.md), and [Total variation, bounded variation, and derivative singularities](entries/total-variation-bounded-variation-and-derivative-singularities.md). The parabolic analytic layer is supplied by the Hölder, Schauder, weak-solution, and \(H^{-1}\) entries linked below.

## Reading map

A newcomer can read the PDE section in four layers.

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
- [Spatial jets, total derivatives, and Faà di Bruno](entries/spatial-jets-total-derivative-and-faa-di-bruno.md)
- [Viscosity solutions](entries/viscosity-solutions.md)
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

### Branching constructions and negative results

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
- [Skeleton-averaged \(L^1\) representation for the quadratic Hessian PDE (Theorem C-prime)](entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md)
- [Banach-scale obstruction for raw PDE patches](entries/banach-scale-obstruction-for-raw-pde-patches.md)
- [Joint centered-mark dichotomy for raw PDE patches](entries/joint-centered-mark-dichotomy-for-raw-pde-patches.md)
- [Raw-barycenter \(L^1\) obstruction for the quadratic Hessian PDE](entries/raw-marked-l1-obstruction-for-quadratic-hessian-pde.md)
- [\(L^1\) random-patch conjecture for the quadratic Hessian PDE](entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md)

The [reference list](meta/references.md) collects the literature cited throughout these pages.