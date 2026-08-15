# Probabilistic representations for nonlinear PDEs

This page is a compact map of branching and signed-weight representations for nonlinear PDEs. The recurring separation is between **exactness** of a signed probabilistic identity and **integrability** of the resulting random variable.

For prerequisites, follow the [PDE reading path](pde-reading-path.md).

## Mild equations and branching trees

A semilinear parabolic equation can be rewritten in [mild form](entries/mild-formulation-and-branching-diffusion-representation.md). Iterating the Duhamel term produces trees: diffusion edges carry the linear transition semigroup, while polynomial nonlinearities become products at branching vertices.

The basic probabilistic ingredients are:

- [Branching diffusions and Duhamel trees](entries/branching-diffusions-and-duhamel-trees.md);
- [Age-dependent branching and finite-horizon nonexplosion](entries/age-dependent-branching-and-nonexplosion.md);
- [Importance-sampling compensators](entries/importance-sampling-compensators.md).

Sampling lifetimes and offspring types can reproduce the deterministic integral recursion exactly. That signed identity alone does not imply finite first moment.

## Marked gradient branching

For polynomial dependence on $(u,Du)$, the HLOTW construction uses finitely many marks. Ordinary marks represent factors of $u$; gradient marks attach [automatic-differentiation weights](entries/gaussian-integration-by-parts-and-automatic-differentiation.md) to descendants. The published theorem and its small-maturity/small-nonlinearity moment hypotheses are summarized in [Marked branching diffusion for gradient nonlinearities](entries/marked-branching-diffusion-for-gradient-nonlinearities.md).

Derivative weights have short-time singularities. In the Brownian case a first derivative contributes a centered Gaussian score of size $r^{-1/2}$; a second derivative is represented by a Hermite score of size $r^{-1}$. Lifetime-density compensators and branching products therefore interact directly with moment estimates.

## Cancellation before absolute values

Heat-semigroup derivatives admit centered Gaussian/Hermite formulas. For example,

$$
\partial_{xx}P_r f(x)
=
\frac1r\mathbb E\left[He_2(Z)f(x+\sqrt r\,Z)\right],
\qquad He_2(z)=z^2-1.
$$

Because $\mathbb E He_2(Z)=0$, one may subtract a constant inside the expectation. If regularity converts the resulting increment into a positive power of $r$, the short-time absolute majorant improves. See [Hölder cancellation for heat-semigroup derivatives](entries/holder-cancellation-for-heat-semigroup-derivatives.md) and [Hermite polynomials and Gaussian chaos](entries/hermite-polynomials-and-gaussian-chaos.md).

More generally, delaying the first absolute value can permit exact cancellation among several signed marks or inside a conditional fiber. Such a local gain is useful only if it survives the recursion in which the marks are composed.

## Conditional coarsening and total variation

A marked contribution can be regarded as a finite signed measure $\mu=R\nu$. If a measurable map $\mathcal C$ retains only part of the raw information, then

$$
\|\mathcal C_\#\mu\|_{\mathrm{TV}}
=
\int\left|\mathbb E_\nu[R\mid\sigma(\mathcal C)]\right|\,d\nu
\leq
\int|R|\,d\nu.
\tag{1}
$$

The measure-theoretic background is in [Finite signed measures, pushforwards, and conditional barycenters](entries/finite-signed-measures-pushforwards-and-conditional-barycenters.md). Strict inequality in (1) requires genuine sign cancellation inside conditional fibers; ordinary resampling of a fixed retained signed measure cannot improve its total-variation cost.

Conditional independence is equally important for products. If different descendants use fresh independent randomness after a branching vertex, conditional expectations factorize across descendants. This mechanism is exact but can be destroyed by conditioning on a variable that was meant to remain available for a later centered cancellation.

## Exactness, moments, and limits

Any proposed branching representation has several separate obligations:

1. **finite-step exactness:** conditioning on the first branch or finite tree must reproduce the intended mild recursion;
2. **genealogical nonexplosion:** only finitely many particles are born before a finite horizon;
3. **absolute integrability:** the multiplicative estimator belongs to $L^1$ (or to the stronger moment class required by the theorem);
4. **passage to limits:** truncations or approximations are uniformly integrable or otherwise justified;
5. **PDE identification:** the expectation has the regularity or viscosity properties required to solve the target PDE, with uniqueness supplied separately when needed.

See [Uniform integrability and passage to expectations](entries/uniform-integrability-and-passage-to-expectations.md) for the limiting step. None of these obligations is implied merely by algebraic unbiasedness.

## How to evaluate a proposed coarsening

For a finite Gaussian/Hermite or Bismut mark cluster, a useful quantitative test is to compare the raw total variation with the variation after an exact conditioning/coarsening step. A strict factor smaller than one is only the first test. One must then determine whether the factor persists, multiplies, or disappears when two clusters are composed through the product structure of a branching tree. This finite-dimensional calibration can be studied independently of any particular PDE application.
