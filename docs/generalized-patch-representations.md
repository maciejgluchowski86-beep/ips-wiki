# Generalized patch representations

> **Research-branch section.** This section exists only on `research/generalized-patch-representations`. It is not published on `main`. Statements marked as current research have not automatically completed independent audit.

This section develops extensions of the patch representation from binary flip spin systems to more general interacting particle systems.

The binary benchmark is the canonical manuscript *Patch representations and convergence for facilitated spin systems* under `paper/`, together with the existing [patch](entries/patch.md), [successful interaction](entries/successful-interaction.md), [monomial duality](entries/monomial-duality-for-spin-systems.md), [patch representation](entries/patch-representation-of-spin-systems.md), and [patch positivity](entries/patch-positivity-property.md) entries.

The generalization programme keeps the same structural order:

1. choose a tensor basis for local observables;
2. derive a local signed Feynman--Kac dual;
3. identify a coarse successful-interaction skeleton that hides a finite local mark;
4. prove conditional or representation-sufficient weighted factorization into generalized patches;
5. define explicit patch contributions;
6. characterize nonnegative bulk patch contributions;
7. derive comparison/convergence consequences and test concrete models.

## Current pages

- [Finite-state typed tensor duality](generalized-patch-representations/finite-state-typed-duality.md): canonical reference-state indicator basis, typed active configurations, exact local signed dual for general single-site replacement rates, and the first successful-interaction record.
- [Typed successful-skeleton factorization](generalized-patch-representations/typed-patch-factorization.md): one-site typed patches, the incoming target-conflict obstruction to bare conditional independence, and the exact killed/noncemetery weighted factorization which repairs it.
- [Explicit typed patch representation](generalized-patch-representations/typed-patch-representation.md): local Feynman--Kac patch weight, pathwise product identity, exact killed-skeleton semigroup representation, bulk/end separation, and exact binary reduction.

## Current bottleneck

The representation layer is now complete for finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator basis.

For a bulk typed patch,

\[
C(P)=E_P^{con}[A_P]
\]

is a scalar depending only on local typed boundary data, interval length, source site, and local dual coefficients. The current research question is to characterize or find useful coefficient-level sufficient conditions for

\[
C(P)\ge0
\]

for every finite bulk typed patch.

The next step is to rewrite these contributions as finite-dimensional transfer-matrix / killed-CTMC expressions before proposing a generalized patch-positivity criterion.