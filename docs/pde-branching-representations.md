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

The [antithetic and ghost branching schemes](entries/antithetic-and-ghost-branching-schemes.md) are related variance/cancellation devices, but they are logically separate from the project-level patch construction below.

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

The positive project-level route is developed for the quadratic Hessian equation on the torus,

$$
\partial_tv
=
\frac12v_{xx}
+
\lambda(v_{xx})^2,
\qquad
v(0)=\phi,
$$

with

$$
z=v_{xx}.
$$

Then

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

A naive edge-by-edge randomization applies a centered Hessian weight at every derivative edge. That is exactly where short-edge absolute moments become dangerous. The central alternative is to regroup **consecutive Hessian events first** and delay absolute values until after the interior of a whole patch has been averaged.

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

With a uniform Schauder constant \(C_{\mathrm{Sch}}(\alpha,T)\), the explicit condition

$$
|\lambda|C_{\mathrm{Sch}}(\alpha,T)
\|\phi\|_{C^{2+\alpha}}
\leq
\frac18
$$

keeps the iteration coefficient in \([3/8,5/8]\), gives an \(H^{-1}\) contraction with ratio at most \(1/3\), and produces the unique small uniformly parabolic solution. Its implicit diffusion representation is obtained from [Itô's formula and the backward Kolmogorov equation](entries/ito-diffusions-and-backward-kolmogorov-representation.md). The [maximum-principle/Schauder](entries/parabolic-maximum-principle-and-schauder-estimates.md), [weak-solution](entries/weak-parabolic-solutions-on-the-torus.md), and [\(H^{-1}\) energy](entries/h-minus-one-energy-method.md) entries contain the supporting analytic tools.

The stronger representation statement is [Theorem C-prime: the skeleton-averaged \(L^1\) representation](entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md). Define

$$
(\mathcal Df)(t)
=
\int_0^t
\partial_x^2P_{t-s}f(s)\,ds.
$$

The [parabolic Hölder bound for \(\mathcal D\)](entries/parabolic-holder-bound-for-hessian-duhamel-operator.md) makes

$$
X_{\alpha,T}
=
C^{\alpha/2,\alpha}([0,T]\times\mathbb T)
$$

into a closing space for the quadratic map. If

$$
M=\|P_\cdot\phi''\|_{X_{\alpha,T}}
$$

and

$$
4|\lambda|C_{\mathcal D}(\alpha,T)M<1,
\tag{2}
$$

then the deterministic profiles attached to finite planar binary skeletons satisfy a Catalan majorant and

$$
\sum_S\|F_S\|_{X_{\alpha,T}}<\infty.
$$

Sampling a discrete skeleton \(S\) with any full-support probability mass function \(\pi\) and returning

$$
\widehat z(t,x)
=
\frac{F_S(t,x)}{\pi(S)}
$$

gives an unbiased \(L^1\) estimator of the absolutely summed solution profile. All branch times and Gaussian/Hermite variables inside \(S\) have been integrated out before the skeleton is sampled. Absolute convergence justifies both the nonlinear Cauchy product and the expectation/skeleton-sum interchange.

On their common small-data regime, C-prime is strictly stronger in conclusion than the deterministic theorem because it adds an integrable probabilistic representation. It is strictly weaker than the full random-patch conjecture because it removes the interior random marks.

## The fork: proved interior averaging versus open raw fluctuations

This is the current logical fork of the project.

**Average every patch interior first.** Fix a finite decorated skeleton and integrate out all continuous branch-time, Brownian, Gaussian/Hermite, and descendant variables inside its patches. The result is the deterministic profile \(F_S\). Under (2), these profiles are absolutely summable and the skeleton-only estimator is proved unbiased and \(L^1\). This is Theorem C-prime.

**Retain the interior marks.** The [full random-patch conjecture](entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md) asks for an \(L^1\) estimator that keeps those continuous marks random. That problem is still open. Direct pathwise Hölder control fails for one centered Hessian edge, and a fixed same-regularity Besov norm has the same high-frequency translation obstruction.

The [Banach-scale obstruction](entries/banach-scale-obstruction-for-raw-pde-patches.md) rules out the next natural repair. If generation \(k\) is measured in \(C^{\alpha_k}\) and the edge spends

$$
\delta_k=\alpha_{k-1}-\alpha_k,
$$

then the sharp one-edge first-moment cost is of order \(1/\delta_k\). Under any fixed total budget

$$
\sum_{k=1}^n\delta_k\leq\Delta,
$$

a stepwise first-moment Banach-scale proof incurs at least

$$
c^n\prod_{k=1}^n\delta_k^{-1}
\geq
c^n\left(\frac n\Delta\right)^n.
$$

The uniform budget \(\delta_k=\Delta/n\) is optimal; geometric budgets are worse. Chronological ordering does not restore a hidden \(1/n!\), because the nested time integral is a Dirichlet integral with factors \(\Gamma(\delta_k/2)\asymp1/\delta_k\).

This theorem rules out a proof architecture, not conjecture C itself. The high-frequency test saturating one edge has frequency \(N\asymp e^{c/\delta}\). At depth \(n\), the worst-case test frequency therefore changes with \(n\). No fixed smooth terminal datum is shown to saturate all generations. The theorem also does not exclude every genuine Nash--Moser smoothing-and-correction scheme; a frequency-aware telescoping construction falls outside the stepwise uniform first-moment Banach-scale argument.

For an integrable finite cutoff one may write

$$
H
=
\mathbb E[H\mid S]
+
R_S,
\qquad
\mathbb E[R_S\mid S]=0.
$$

The [conditional-expectation and fluctuation entry](entries/conditional-expectation-and-fluctuations-of-random-fields.md) explains this decomposition and the important caveat that ordinary conditional expectation requires integrability. C-prime controls the interior-average part by defining it directly through deterministic Duhamel integrals, not by conditioning a possibly non-\(L^1\) infinite functional. The remaining obstruction is the centered raw fluctuation \(R_S\).

The settled barriers now say that a successful proof cannot simply take a first-moment regularity norm after every centered edge. It must retain additional structure before absolute values are taken: frequency, frequency together with genealogy, a multiscale martingale or square-function structure, or cancellation across several centered marks.

That fluctuation problem is the present open endpoint of this PDE programme.

## Analytic and probabilistic prerequisites

The remaining background pages provide the tools used by the settled chain. [Random fields in function spaces](entries/random-fields-in-function-spaces.md) distinguishes pointwise random variables from Banach-valued random fields. [Tonelli, Markov, and Borel--Cantelli](entries/tonelli-markov-and-borel-cantelli.md) records the measure-theoretic arguments used in the obstruction proofs. [Interior Hölder estimates](entries/interior-holder-estimates-for-parabolic-equations.md) distinguish De Giorgi--Nash--Moser and Krylov--Safonov compactness from Schauder regularity. [Aronson--Nash Gaussian bounds](entries/aronson-nash-gaussian-bounds.md) records the divergence/nondivergence and adjoint caveats that prevent misuse of heat-kernel estimates.

## Reading map

A newcomer can read the PDE section in four layers.

### Foundations

- [Heat-reference fully nonlinear terminal PDE](entries/heat-reference-fully-nonlinear-pde.md)
- [Mild formulation and branching-diffusion representation](entries/mild-formulation-and-branching-diffusion-representation.md)
- [Feynman--Kac formula for linear parabolic equations](entries/feynman-kac-formula-for-linear-parabolic-equations.md)
- [Branching diffusions and Duhamel trees](entries/branching-diffusions-and-duhamel-trees.md)
- [Age-dependent branching and finite-horizon nonexplosion](entries/age-dependent-branching-and-nonexplosion.md)
- [Importance-sampling compensators](entries/importance-sampling-compensators.md)
- [Uniform integrability and passage to expectations](entries/uniform-integrability-and-passage-to-expectations.md)
- [Gaussian integration by parts and automatic differentiation](entries/gaussian-integration-by-parts-and-automatic-differentiation.md)
- [Malliavin and Bismut automatic differentiation](entries/malliavin-and-bismut-automatic-differentiation.md)
- [Hermite polynomials and Gaussian chaos](entries/hermite-polynomials-and-gaussian-chaos.md)
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
- [\(L^1\) random-patch conjecture for the quadratic Hessian PDE](entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md)

The [reference list](meta/references.md) collects the literature cited throughout these pages.