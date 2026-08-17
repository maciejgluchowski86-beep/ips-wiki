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
6. define a nonnegativity criterion;
7. derive comparison/convergence consequences and test concrete models.

## Current pages

- [Finite-state typed tensor duality](generalized-patch-representations/finite-state-typed-duality.md): canonical reference-state indicator basis, typed active configurations, exact local signed dual for general single-site replacement rates, and the first successful-interaction record.
- [Typed successful-skeleton factorization](generalized-patch-representations/typed-patch-factorization.md): one-site typed patches, the incoming target-conflict obstruction to bare conditional independence, and the exact killed/noncemetery weighted factorization which repairs it.

## Current bottleneck

The next theorem is the **explicit typed patch representation**. On noncemetery paths, the global signed Feynman--Kac weight should factor into one local multiplicative weight per typed patch, using the outgoing hidden-branch sign, effective empty-target signs, the local additive-potential integral, and the terminal one-site tensor factor on end patches.

Patch positivity is not yet defined. It is downstream of this representation theorem.
