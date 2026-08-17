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

The first natural application was Krone's two-stage contact process, selected before any positivity calculation. Its successful interaction has hidden signed row

\[
(\lambda,-\lambda,-\lambda),
\]

and typed cemetery conflicts are genuinely realizable, so the new representation mechanism is active.

Nevertheless a realized same-source `OO` bulk patch has negative numerator for every finite patch length whenever `lambda>0`. A spatial SIRS process has the same obstruction.

This yields a structural catalytic-birth filter:

> a positive neighbour-dependent `0->r` target mode with no compensating active-source transition into `r` forces a negative source-preserving hidden coefficient; if the source-`r` record can repeat, typed patch positivity fails locally.

Thus ordinary contact/SIRS catalytic-birth models are poor candidates for positive applications of this particular indicator-basis patch positivity mechanism.

The next useful application test, if continued, should come from a structurally distinct published three-state replacement model with genuinely interacting active labels. Generic `d>3` positivity algebra remains deferred.
