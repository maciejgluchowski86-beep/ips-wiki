# PDEs for this project: reading path

This page is the pedagogical entry point for the PDE side of the project. The separate [probabilistic representations for nonlinear PDEs](pde-branching-representations.md) page is the advanced research map.

## Reader

The intended reader is a mathematically mature probability researcher with graduate probability and analysis, but no dependable PDE vocabulary. In particular, this path does **not** assume that the reader already knows the distinction between elliptic and parabolic equations, the standard notions of PDE solution, Schauder estimates, or Malliavin calculus.

The goal is not a general PDE course. It is the shortest self-contained knowledge tree needed to understand, check, and place the PDE results developed in this repository.

## How to use the path

Read approximately in the order below. Each technical term should eventually link to one atomic wiki entry. If an entry uses an object that has not yet been defined, that is a defect in the path rather than an instruction to guess the meaning.

Definitions should live in one place and be linked elsewhere. Standard PDE facts may be stated without a full proof when a reliable source is provided; project-specific results require complete proofs in their own entries or the manuscript.

## 0. PDE vocabulary

**Current wiki frontier: §0 item 6, the role of regularity assumptions and a first picture of existence, uniqueness, and a priori estimates.** Item 5 is now integrated and audited; the remaining vocabulary layer should continue to be built before later entries are treated as self-contained.

The reader should first acquire the following objects and distinctions:

1. [basic PDE objects and vocabulary](entries/partial-differential-equations-basic-vocabulary.md): what a partial differential equation is, its order, unknown, independent variables, and differential operator;
2. [initial, terminal, boundary, and initial-boundary value problems](entries/initial-terminal-and-boundary-value-problems.md);
3. [linear, semilinear, quasilinear, and fully nonlinear equations](entries/linear-semilinear-quasilinear-and-fully-nonlinear-equations.md);
4. [elliptic, parabolic, and hyperbolic equations](entries/elliptic-parabolic-and-hyperbolic-equations.md), first through canonical examples and only then through the general principal-part classification;
5. [classical, weak/distributional, mild, and viscosity solutions](entries/classical-weak-mild-and-viscosity-solutions.md)
6. the role of regularity assumptions and a first picture of existence, uniqueness, and a priori estimates.

These are deliberately prerequisites rather than compressed terminology lists. The autonomous wiki process should create focused entries for them by the reader-failure algorithm in `CHATGPT.md`.

## 1. The heat equation as the model parabolic PDE

Once the vocabulary layer is in place, use the heat equation repeatedly as the canonical example. The required chain is:

- heat equation and heat kernel;
- Brownian motion interpretation;
- heat semigroup and generator;
- smoothing;
- Duhamel/variation-of-constants formula;
- mild formulation.

Existing later-stage material includes [Mild formulation and branching-diffusion representation](entries/mild-formulation-and-branching-diffusion-representation.md), but it should not be the first introduction to these notions.

## 2. Linear probability/PDE interface

The next objective is to understand why a Markov process represents a linear parabolic PDE.

Read, after the missing prerequisites are supplied:

- [Itô diffusions and backward Kolmogorov representation](entries/ito-diffusions-and-backward-kolmogorov-representation.md);
- [Feynman--Kac formula for linear parabolic equations](entries/feynman-kac-formula-for-linear-parabolic-equations.md).

At the end of this layer the reader should be able to distinguish the probabilistic representation from the analytic existence theorem and understand the terminal-time convention.

## 3. From nonlinear Duhamel expansions to branching

The next chain explains why nonlinear products generate trees:

- Picard iteration of a mild equation;
- Duhamel trees;
- branching processes as randomized tree expansions;
- lifetime laws and finite-horizon nonexplosion;
- proposal laws and reciprocal compensators.

Existing entries:

- [Branching diffusions and Duhamel trees](entries/branching-diffusions-and-duhamel-trees.md);
- [Age-dependent branching and finite-horizon nonexplosion](entries/age-dependent-branching-and-nonexplosion.md);
- [Importance-sampling compensators](entries/importance-sampling-compensators.md).

The reader should leave this layer knowing the difference between a formal tree identity and an integrable random estimator.

## 4. Derivative weights and signed representations

Derivative nonlinearities require an additional mechanism. The route is:

- Gaussian integration by parts;
- Hermite polynomials as heat-semigroup derivative weights;
- centered derivative identities;
- automatic-differentiation/Malliavin/Bismut weights;
- why these weights are signed and may be singular at short times.

Existing entries:

- [Gaussian integration by parts and automatic differentiation](entries/gaussian-integration-by-parts-and-automatic-differentiation.md);
- [Hermite polynomials and Gaussian chaos](entries/hermite-polynomials-and-gaussian-chaos.md);
- [Malliavin and Bismut automatic differentiation](entries/malliavin-and-bismut-automatic-differentiation.md);
- [Hölder cancellation for heat-semigroup derivatives](entries/holder-cancellation-for-heat-semigroup-derivatives.md).

Malliavin calculus is not assumed background. Its project-relevant fragment must be explained before the corresponding entry is used as a prerequisite.

## 5. Integrability and cancellation before absolute values

This layer separates exact signed identities from genuine random variables. The reader needs:

- first moments and total variation of signed measures;
- conditional expectation and the integrability required to define it;
- uniform integrability when passing to limits;
- cancellation before taking absolute values;
- how conditional averaging/coarsening changes surviving signed variation.

Existing entries:

- [Finite signed measures, pushforwards, and conditional barycenters](entries/finite-signed-measures-pushforwards-and-conditional-barycenters.md);
- [Uniform integrability and passage to expectations](entries/uniform-integrability-and-passage-to-expectations.md).

This is the conceptual bridge from ordinary probabilistic representations to the cancellation programme.

## 6. Parabolic regularity used by the project

Only after the heat equation and solution notions are clear should the reader study the regularity machinery actually used in the proofs:

- parabolic scaling;
- spatial and parabolic Hölder spaces;
- maximum principles;
- Schauder estimates;
- interior Hölder estimates;
- the Hessian Duhamel estimate used in the quadratic-Hessian programme.

Existing entries:

- [Parabolic Hölder spaces](entries/parabolic-holder-spaces.md);
- [Parabolic maximum principle and Schauder estimates](entries/parabolic-maximum-principle-and-schauder-estimates.md);
- [Interior Hölder estimates for parabolic equations](entries/interior-holder-estimates-for-parabolic-equations.md);
- [Parabolic Hölder bound for the Hessian Duhamel operator](entries/parabolic-holder-bound-for-hessian-duhamel-operator.md).

The standard theory may be presented with proof sketches and textbook references. The project-specific operator estimates must remain checkable in full where they are used.

## 7. Reusable cancellation mechanisms

The terminated quadratic-Hessian theorem chain is not part of the core path. The surviving audited mechanism notes are:

- [Finite-depth Duhamel patch regrouping](entries/finite-depth-duhamel-patch-regrouping.md), for finite combinatorial reindexing into maximal-left patches;
- [Conditional factorization for finite PDE patches](entries/conditional-factorization-for-finite-pde-patches.md), for finite conditional independence with explicit integrability and fresh-mark hypotheses;
- [Joint centered-mark identities for Gaussian derivative weights](entries/joint-centered-mark-dichotomy-for-raw-pde-patches.md), for the two-mark mixed-difference gain and Gaussian bridge conditional-score identity;
- [Residual signed variation under coarsening](entries/residual-signed-variation-characterization-for-coarsened-patches.md), for the pushforward/conditional-expectation total-variation identity and its countable-family consequence.

These are reusable finite or measure-theoretic mechanisms. They do not form an active quadratic-Hessian theorem chain and do not by themselves supply an infinite-depth branching representation.

The [advanced PDE representation overview](pde-branching-representations.md) places these mechanisms in the broader branching and cancellation framework.

## 8. Literature and importance

The final layer is not optional. To audit the paper, the reader must be able to answer:

1. What exact problem is being solved?
2. Where was it stated as open?
3. What are the closest previous results and their assumptions?
4. What does the new result add?
5. Why does the cancellation mechanism matter rather than merely repackage an existing argument?

As the autonomous research programme selects its final application, the wiki should add a concise literature map with exact source locations for these questions. The final paper's novelty should be verifiable from that map without relying on agent assertions.

## Source spine

For deterministic PDE background, the project may use a small number of standard texts as a consistent notation/source spine rather than reproducing a general PDE textbook. The current manuscript already cites Evans for broad PDE foundations and Friedman/Lieberman for parabolic theory. Specialized entries should additionally cite the primary literature relevant to the representation being discussed.

Source material should be normalized to the wiki's notation and linked for further reading. Standard facts should not be duplicated across entries.
