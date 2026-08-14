# Probabilistic representations for nonlinear PDEs

This page is a compact map of the representation and cancellation mechanisms used on the PDE side of the wiki. The linear starting point is the heat or diffusion semigroup; nonlinear Duhamel terms generate trees; derivative nonlinearities introduce signed weights; and integrability must be checked separately from signed exactness.

For prerequisites, follow the [PDE reading path](pde-reading-path.md).

## Mild equations and tree expansions

A semilinear or derivative-dependent parabolic equation is first rewritten in mild form. Iterating the Duhamel term produces a finite tree expansion at every fixed Picard depth. A branching process can randomize that finite or infinite tree family by sampling lifetimes and offspring types.

Relevant background pages are:

- [Mild formulation and branching-diffusion representation](entries/mild-formulation-and-branching-diffusion-representation.md);
- [Branching diffusions and Duhamel trees](entries/branching-diffusions-and-duhamel-trees.md);
- [Age-dependent branching and finite-horizon nonexplosion](entries/age-dependent-branching-and-nonexplosion.md);
- [Importance-sampling compensators](entries/importance-sampling-compensators.md).

Reciprocal proposal densities can make a sampled tree term unbiased, but unbiasedness is only a signed identity. It does not imply that the absolute first moment is finite.

## Derivative weights and local cancellation

Heat-semigroup derivatives admit Gaussian/Hermite representations. A centered second derivative may be written
\[
\partial_{xx}P_r f(x)
=
\frac1r
\mathbb E\left[
He_2(Z)
\bigl(f(x+\sqrt r\,Z)-f(x)\bigr)
\right],
\qquad
He_2(z)=z^2-1.
\tag{1}
\]
The subtraction uses \(\mathbb E He_2(Z)=0\). If regularity of \(f\) turns the increment into a positive power of \(r\), the centered formula can improve the short-time absolute majorant.

The general background is in [Gaussian integration by parts and automatic differentiation](entries/gaussian-integration-by-parts-and-automatic-differentiation.md), [Hermite polynomials and Gaussian chaos](entries/hermite-polynomials-and-gaussian-chaos.md), and [Hölder cancellation for heat-semigroup derivatives](entries/holder-cancellation-for-heat-semigroup-derivatives.md).

Two reusable finite calculations are isolated in [Joint centered-mark identities for Gaussian derivative weights](entries/joint-centered-mark-dichotomy-for-raw-pde-patches.md):

- a two-mark mixed difference can be estimated before the first absolute value, giving an integrable short-time product singularity;
- conditioning independent Gaussian increments on their total displacement averages bridge coordinates and replaces the product of second-order scores by one higher Hermite score.

These are local identities. They do not by themselves control products accumulated over arbitrary branching depth.

## Finite regrouping and conditional factorization

There are two distinct finite operations that should not be conflated with an infinite representation theorem.

[Finite-depth Duhamel patch regrouping](entries/finite-depth-duhamel-patch-regrouping.md) records a purely combinatorial reindexing of finite planar binary trees by maximal left-child chains and their ordered side attachments.

[Conditional factorization for finite PDE patches](entries/conditional-factorization-for-finite-pde-patches.md) records the probabilistic counterpart: if distinct child pieces use conditionally independent fresh seeds and the relevant products are integrable, their conditional expectation factorizes. A centered Gaussian mark must remain outside the conditioning sigma-field until the stage where its mean-zero cancellation is used.

Both statements are finite. Neither supplies depth-uniform moment control.

## Signed measures, coarsening, and first moments

A useful way to separate signed exactness from integrability is to regard a marked contribution as a finite signed measure
\[
\mu=R\nu
\]
relative to a finite positive measure \(\nu\). If a measurable map \(\mathcal C\) retains only part of the mark information, then [Residual signed variation under coarsening](entries/residual-signed-variation-characterization-for-coarsened-patches.md) gives
\[
\|\mathcal C_\#\mu\|_{\mathrm{TV}}
=
\int
\left|
\mathbb E_\nu[R\mid\sigma(\mathcal C)]
\right|\,d\nu.
\tag{2}
\]
Conditional Jensen shows that further coarsening cannot increase this residual total variation.

For a countable family of signed contributions, sampling the family label and then sampling each coarsened signed measure from a dominating positive proposal gives
\[
\mathbb E|Y|
=
\sum_\tau
\|(\mathcal C_\tau)_\#\mu_\tau\|_{\mathrm{TV}}.
\tag{3}
\]
Thus the first-moment problem is a summability problem for the variation that survives conditional averaging.

The underlying measure-theoretic vocabulary is collected in [Finite signed measures, pushforwards, and conditional barycenters](entries/finite-signed-measures-pushforwards-and-conditional-barycenters.md), and limiting arguments require the separate [uniform-integrability](entries/uniform-integrability-and-passage-to-expectations.md) checks appropriate to the construction.

## Scope

The reusable mechanism is cancellation before absolute values: perform an exact finite algebraic or conditional averaging step while signs are still present, and only then estimate the resulting object. The possible gain may come from spatial increments, joint Gaussian marks, conditional independence, or coarsening of signed measures.

Three issues remain logically separate in any proposed application:

1. **exactness:** does the finite or infinite representation equal the intended PDE quantity?
2. **integrability:** is the estimator an \(L^1\) random variable, with all limiting operations justified?
3. **problem relevance:** does the cancellation gain close a published analytic or probabilistic criterion that matters for the target PDE?

The current research programme is in SEARCH and uses these pages as background mechanisms rather than as an active quadratic-Hessian theorem chain.
