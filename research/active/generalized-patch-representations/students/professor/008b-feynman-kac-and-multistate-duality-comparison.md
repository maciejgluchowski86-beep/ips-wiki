# 008b: Feynman--Kac, signed matrix, and multistate duality predecessors

Date: 2026-08-17

This note continues Assignment 008. Its purpose is to test whether package A is already present once one searches outside the binary/additive IPS vocabulary.

## 1. General Feynman--Kac genealogical particle representations are standard

Relevant sources include:

- P. Del Moral and L. Miclo, *Branching and interacting particle systems approximations of Feynman--Kac formulae with applications to non-linear filtering*, Séminaire de Probabilités XXXIV (2000), 1--145.
- P. Del Moral, *Feynman--Kac Formulae: Genealogical and Interacting Particle Systems with Applications*, Springer, 2004.
- M. Arnaudon and P. Del Moral, *A duality formula and a particle Gibbs sampler for continuous time Feynman--Kac measures on path spaces*, Electron. J. Probab. 25 (2020), paper 108; arXiv:1805.05044.

These works make genealogical/branching particle representations of Feynman--Kac path measures a mature theory. Therefore the generalized patch project cannot claim novelty merely from representing an FK semigroup by a branching or genealogical particle system.

The purpose of those particle systems is different: they represent or approximate positive/normalized Feynman--Kac measures and their genealogies. I did not find in these sources the project-specific coarse successful skeleton which hides a signed source outcome and then factors the exact signed weight over source-time strips.

## 2. Finite matrix exponentials already have Markov-path multiplicative-functional representations

Two adjacent sources are particularly relevant.

- J. A. Acebrón, *A Monte Carlo method for computing the action of a matrix exponential on a vector*, arXiv:1904.12759 (2019). It represents the action of a class of matrix exponentials through continuous-time Markov paths and multiplicative functionals.
- P. Y. Gaudreau Lamarre, *Probabilistic Representations of Ordered Exponentials: Vector-Valued Schrödinger Semigroups and the Combinatorics of Anderson Localization*, arXiv:2311.08564 (2023). Its abstract describes an elementary probabilistic representation of matrix ordered exponentials generalizing finite-dimensional Feynman--Kac and finite-state change of measure.

The first source is restricted in matrix structure and is motivated computationally. The second is much more general; notably, the author describes the exact ordered-exponential representation as "seemingly unknown", which is evidence that one should not casually label every arbitrary signed-matrix stochastic representation classical folklore.

For the present audit the conservative conclusion is:

- the *idea* of replacing a finite linear system or matrix exponential by a finite-state Markov path carrying a multiplicative functional is known;
- signs and non-Markov linear coefficients can be encoded probabilistically in adjacent matrix/FK literature;
- the specific Assignment-001 branch bookkeeping is not enough on its own to support a strong novelty claim.

This further lowers the novelty status of item 1.

## 3. Multistate pathwise IPS duality is directly known

The most important modern comparison is:

- J. N. Latz and J. M. Swart, *Commutative monoid duality*, J. Theoret. Probab. 36 (2023), 1088--1115; arXiv:2108.01492.

Their introduction explicitly considers product spaces `S^Lambda` with finite local state space and Poisson random-map stochastic flows. They construct pathwise dual maps by reversing the marked Poisson flow. Their stated motivation is to generalize additive and cancellative dualities beyond two local states, and they exhibit genuinely new dualities for local state spaces with three or more elements.

This source directly rules out a novelty claim of the form

> multistate IPS admit local graphical/pathwise dualities built from finite local maps.

The mathematical restriction is equally important. Latz--Swart require local update maps belonging to algebraically dualizable homomorphism/module classes arising from commutative monoids or semirings. Their dual is an honest pathwise Markov dual with nonnegative clock rates. The generalized patch construction instead starts from arbitrary bounded single-site replacement rates, expands the generator in the reference-state indicator basis, and permits signed branch coefficients plus an additive Feynman--Kac potential.

No successful-skeleton/hidden-outcome patch factorization or typed cemetery mechanism was found in Latz--Swart.

Related predecessor:

- A. Sturm and J. M. Swart, *Pathwise duals of monotone and additive Markov processes*, J. Theoret. Probab. 31 (2018), 932--983; arXiv:1510.06284.

This develops finite-state random-mapping duality for monotone/additive maps and extends it to IPS with finite local spaces. Again the duality is structural/pathwise rather than the arbitrary signed FK construction of Assignment 001.

## 4. Multitype additive systems already have duality and positivity criteria

Relevant source:

- E. Foxall, *Duality and Complete Convergence for Multi-type Additive Growth Models*, Adv. Appl. Probab. 48 (2016), 250--273; arXiv:1410.4809.

Foxall studies finite sets of local types in additive growth systems, proves additivity equivalent to existence of a dual in the class, gives a spacetime/percolation characterization, and proves a necessary-and-sufficient condition for preservation of positive correlations.

This is a particularly important warning for packages B--D: a theorem saying "multitype IPS + duality + coefficient inequalities imply a positivity property" is not novel at that level of abstraction. The hypotheses, order structure, and positivity object have to be compared exactly.

Foxall's positivity is preservation of positive correlations in an additive growth class. It is not nonnegativity of conditional signed patch contributions, and the source does not contain the Assignment-004 local transfer cancellation or the four patch-boundary semigroup inequalities.

## 5. Current item-1 ruling

After the classical, modern multistate, and Feynman--Kac comparisons, I revise item 1 as follows:

### Finite-state typed signed duality

**Status: `known ingredients, assembly plausibly new`.**

The following pieces are directly known and receive no standalone novelty credit:

- finite product/tensor duality functions;
- Poisson random-map graphical duality;
- genuinely multistate pathwise IPS dualities;
- Feynman--Kac genealogical particle representations;
- finite matrix/path multiplicative-functional representations.

What was not found is an equivalent theorem for arbitrary bounded finite-range single-site replacement IPS that simultaneously gives the project's exact typed indicator-basis signed branching/retyping process, the designated diagonal FK potential, and the later successful-record interface used for patch factorization.

This is deliberately not upgraded to `plausibly new theorem/mechanism` by itself. The audit is treating Assignment 001 primarily as an enabling assembly of known technologies unless the later patch mechanism makes that assembly essential.

## 6. Consequence for the combined package

The combined framework can only carry novelty through the interfaces that these predecessor theories do **not** supply:

1. coarse successful-record revelation that forgets the signed source outcome;
2. exact local averaging/factorization of signed FK weights conditional on that coarse geometry;
3. typed target conflicts and the killed/noncemetery repair;
4. use of those averaged local factors as a positivity/comparison object.

Those interfaces are the next audit target.