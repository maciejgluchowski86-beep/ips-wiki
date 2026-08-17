# Generalized patch representations

> **Research-branch section.** This section exists only on `research/generalized-patch-representations`. It is not published on `main`. Statements marked as current research have not automatically completed independent audit.

This section develops extensions of the patch representation from binary flip spin systems to more general interacting particle systems.

The binary benchmark is the canonical manuscript *Patch representations and convergence for facilitated spin systems* under `paper/`, together with the existing [patch](entries/patch.md), [successful interaction](entries/successful-interaction.md), [monomial duality](entries/monomial-duality-for-spin-systems.md), [patch representation](entries/patch-representation-of-spin-systems.md), and [patch positivity](entries/patch-positivity-property.md) entries.

The programme proceeds through finite-state duality, killed patch factorization, explicit representation, positivity analysis, novelty audit, and applications.

## Current pages

- [Finite-state typed tensor duality](generalized-patch-representations/finite-state-typed-duality.md): canonical reference-state indicator basis, typed active configurations, exact local signed dual for general single-site replacement rates, and the first successful-interaction record.
- [Typed successful-skeleton factorization](generalized-patch-representations/typed-patch-factorization.md): one-site typed patches, the incoming target-conflict obstruction to bare conditional independence, and the exact killed/noncemetery weighted factorization which repairs it.
- [Explicit typed patch representation](generalized-patch-representations/typed-patch-representation.md): local Feynman--Kac patch weight, pathwise product identity, exact killed-skeleton semigroup representation, bulk/end separation, and exact binary reduction.
- [Typed bulk patch positivity via transfer matrices](generalized-patch-representations/typed-patch-positivity-transfer.md): exact signed and unsigned local transfer matrices, four bulk boundary formulas, short-time multi-state constraints, and exact equivalence with canonical binary patch positivity.
- [Three-state endpoint obstruction](generalized-patch-representations/three-state-endpoint-obstruction.md): boundary completeness forces a Metzler interior transfer, but a physically realizable two-mode `OI` numerator is negative at an interior time despite strictly positive zero-length and long-time endpoints.
- [Exact three-state spectral positivity criterion](generalized-patch-representations/three-state-spectral-criterion.md): mathematically correct exact `d=3` spectral test. The later novelty audit found this scalar theorem directly subsumed by third-order SISO external-positivity theory, so it is not a project novelty claim.
- [Natural three-state positivity subclass](generalized-patch-representations/natural-three-state-subclass.md): exchange-symmetric genuinely nonbinary systems with an exact algebraic endpoint criterion; useful as a structured application gate, but not the primary novelty anchor.
- [Two-stage contact application obstruction](generalized-patch-representations/two-stage-contact-application-obstruction.md): literature-selected genuine three-state contact process where the killed typed representation is nonvacuous but a realized `OO` patch is strictly negative throughout the interacting range, yielding a catalytic-birth no-go.
- [Potts Metropolis application obstruction](generalized-patch-representations/potts-metropolis-application-obstruction.md): fully active symmetric three-state Metropolis dynamics genuinely realizes hidden outcomes and typed cemetery conflicts but still fails patch positivity through a short-`OO` source-response contrast.

## Novelty status

A dedicated closest-prior-work audit found substantial predecessor theory for finite-state graphical duality, signed finite-type Feynman--Kac duality, partial graphical revelation, and matrix external positivity.

The strongest surviving plausible novelty candidate is the **combined interface**

\[
\text{signed typed dual}
\to
\text{successful skeleton hiding source outcome}
\to
\text{typed cemetery obstruction}
\to
\text{killed/noncemetery patch factorization}
\to
\text{exact finite-state patch representation}.
\]

Historical priority is plausible rather than established.

## Application status

Two materially different natural three-state application architectures have now been tested after literature-driven selection committed before positivity calculation.

### Two-stage contact / SIRS

Krone's two-stage contact process genuinely realizes hidden signed outcomes and cemetery conflicts but has a repeated-source `OO` patch which is negative throughout its interacting birth range. Spatial SIRS has the same obstruction.

This yields a catalytic-birth filter: a positive target mode in `0->r` with no matching active-source response into `r` produces a negative hidden coefficient which, when it can feed the next outgoing record, forces a negative short patch.

### Three-state Potts Metropolis

The second application removes the vacancy/birth architecture. Every Potts color is active, every directed replacement has positive physical rate at finite temperature, and active colors retype one another directly.

For a source-type-1 singleton target-type-1 record,

\[
\mathbf a_{1;1,0}
=
\left(
qz^2(1-z^2),
q(z-1)(z^3+z^2-1),
-qz^2(1-z^2)
\right),
\qquad z=e^{-\beta J}.
\]

The record hides multiple post-source outcomes and typed cemetery conflicts are realizable, so the killed representation is genuinely active. Nevertheless

\[
a_1^2(\tau)=-qz^2(1-z^2)<0
\]

for every interacting finite-temperature point `0<z<1`, and a source-type-2 record can follow. Hence a realized arbitrarily short `OO` patch is negative.

This broadens the no-go to a source-response contrast:

> if
> \[
> a_r^s(\tau)=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0
> \]
> and hidden outcome `s` can feed a subsequent source-`s` successful record, typed patch positivity fails locally.

The Potts example shows that this can happen even in a fully active color-symmetric model through Metropolis saturation.

## Current direction

The representation theorem remains intact and plausibly novel at the combined-interface level, but the two natural application blocks substantially weaken the case for **bulk patch positivity** as the generic multistate application engine.

No third positivity-driven model search is currently active, and generic `d>3` positivity algebra remains deferred.

If the programme continues, the next scientifically distinct question is whether the killed typed patch representation has useful cancellation or representation consequences **without** imposing nonnegativity of every bulk patch.
