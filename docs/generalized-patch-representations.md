# Generalized patch representations

> **Research-branch section.** This section exists only on `research/generalized-patch-representations`. It is not published on `main`. Statements marked as current research have not automatically completed independent audit.

This section develops extensions of the patch representation from binary flip spin systems to more general interacting particle systems.

The binary benchmark is the canonical manuscript *Patch representations and convergence for facilitated spin systems* under `paper/`, together with the existing [patch](entries/patch.md), [successful interaction](entries/successful-interaction.md), [monomial duality](entries/monomial-duality-for-spin-systems.md), [patch representation](entries/patch-representation-of-spin-systems.md), and [patch positivity](entries/patch-positivity-property.md) entries.

The generalization programme keeps the same structural order:

1. choose a tensor basis for local observables;
2. derive a local signed Feynman--Kac dual;
3. identify a coarse successful-interaction skeleton that hides a finite local mark;
4. prove representation-sufficient killed/weighted factorization into generalized patches;
5. define explicit patch contributions;
6. characterize nonnegative bulk patch contributions;
7. audit novelty and closest prior work;
8. then test applications and consequences.

## Current pages

- [Finite-state typed tensor duality](generalized-patch-representations/finite-state-typed-duality.md): canonical reference-state indicator basis, typed active configurations, exact local signed dual for general single-site replacement rates, and the first successful-interaction record.
- [Typed successful-skeleton factorization](generalized-patch-representations/typed-patch-factorization.md): one-site typed patches, the incoming target-conflict obstruction to bare conditional independence, and the exact killed/noncemetery weighted factorization which repairs it.
- [Explicit typed patch representation](generalized-patch-representations/typed-patch-representation.md): local Feynman--Kac patch weight, pathwise product identity, exact killed-skeleton semigroup representation, bulk/end separation, and exact binary reduction.
- [Typed bulk patch positivity via transfer matrices](generalized-patch-representations/typed-patch-positivity-transfer.md): exact signed and unsigned local transfer matrices, four bulk boundary formulas, short-time multi-state constraints, and exact equivalence with canonical binary patch positivity.
- [Three-state endpoint obstruction](generalized-patch-representations/three-state-endpoint-obstruction.md): boundary completeness forces a Metzler interior transfer, but a physically realizable two-mode `OI` numerator is negative at an interior time despite strictly positive zero-length and long-time endpoints.
- [Exact three-state spectral positivity criterion](generalized-patch-representations/three-state-spectral-criterion.md): necessary-and-sufficient boundary-complete `d=3` test using endpoint values and at most one explicit interior critical value, including degenerate spectra and exact binary reduction.
- [Natural three-state positivity subclass](generalized-patch-representations/natural-three-state-subclass.md): exchange-symmetric non-binary systems where the necessary Metzler ordering makes the signed active-type mode decay faster, giving an exact algebraic endpoint criterion; includes the refresh boundary case.

## Current status

For arbitrary finite-state bounded finite-range **single-site replacement** dynamics, the typed dual, killed patch factorization, exact patch representation, and transfer-semigroup definition of bulk positivity are established on this research branch.

For boundary-complete `d=3`, the generic positivity problem has an exact finite spectral criterion. Assignment 007 additionally identifies a genuinely non-binary exchange-symmetric subclass with an exact algebraic criterion:

\[
c\ge a,
\]

and, for every outgoing row `p=(p_0,p_1,p_2)`,

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\]

\[
(b+2a)p_0+a(p_1+p_2)\ge0.
\]

The next programme block is a targeted literature/novelty audit. If the mechanism is not already subsumed by prior work, applications are planned immediately afterward. A generic `d>3` positivity-criterion block is deferred unless an application or the literature makes it necessary.
