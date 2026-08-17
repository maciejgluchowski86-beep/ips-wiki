# Proof spine: generalized patch representations

Date: 2026-08-17

## Target

Extend the binary patch-representation mechanism to finite-state single-site replacement IPS, identify which parts are genuinely new, and determine whether the generalized representation has useful nonbinary consequences.

## E0. Binary benchmark

**Settled by the canonical paper.**

## E1. Arbitrary finite-state typed signed dual

**Settled in Assignment 001; novelty narrowed in Assignment 008.**

Reference-state indicator tensors give an exact signed Feynman--Kac dual for arbitrary bounded finite-range single-site replacement IPS. Successful nonempty records reveal `(i,t,r,tau)` and hide the post-source outcome.

Novelty status: **known ingredients, assembly plausibly new**.

## E2. Killed typed patch factorization

**Settled in Assignment 002. Primary plausible novelty anchor.**

Typed incoming target conflicts make bare skeleton conditioning false because cemetery entry deletes future no-record constraints. Since the duality function vanishes at cemetery, the killed/noncemetery weighted identity restores exact local factorization.

Novelty status: **plausibly new theorem/mechanism** after the bounded Assignment-008 audit.

## E3. Exact typed patch representation

**Settled in Assignment 003.**

The killed factorization yields the exact bulk/end patch representation for arbitrary finite local state space.

## E4. Exact finite-state bulk transfer

**Settled in Assignment 004.**

\[
K_i(0,\cdot)=0,
\qquad K_i(r,s)=a_{i,r}^s(\emptyset).
\]

Typed bulk patch positivity is exact nonnegativity of local semigroup boundary responses. The `d=2` specialization is canonical binary patch positivity.

## E5. Three-state positivity differs structurally from binary

**Settled in Assignment 005.**

Boundary-complete `d=3` can have a two-mode `OI` response with positive zero/long endpoints and a negative interior minimum. Thus the binary endpoint collapse does not survive automatically.

## E6. Exact `d=3` scalar spectral test

**Mathematically settled in Assignment 006; novelty removed in Assignment 008.**

Every boundary-complete `d=3` scalar response is decided by finitely many endpoint/critical evaluations.

Novelty status: **known / directly subsumed** by third-order SISO external-positivity theory. Do not use this as a contribution claim.

## E7. Natural exact nonbinary algebraic subclass

**Settled in Assignment 007.**

Exchange-symmetric reference dynamics yields an exact algebraic criterion after the necessary Metzler ordering. This is genuinely nonbinary but is a structured external-positivity consequence, not the primary novelty anchor.

## E8. Novelty audit

**Settled in Assignment 008. Outcome `CONTINUE-TO-APPLICATIONS`.**

Broad ingredients are known: finite-state/product duality, signed finite-type FK duality, ancestor/history constructions and external positivity. No equivalent source was found for the precise hidden-successful-record plus typed-cemetery killed factorization interface.

The plausible contribution remains

\[
\text{signed typed dual}
\to
\text{hidden successful skeleton}
\to
\text{cemetery-aware killed patch factorization}
\to
\text{exact finite-state patch representation}.
\]

## E9. First natural application: two-stage contact process / SIRS

**Settled negatively in Assignment 009. Outcome `STOP-APPLICATION-POSITIVITY-FAILS`.**

The literature-selected two-stage contact process genuinely realizes hidden outcomes and cemetery conflicts, but a realized repeated-source `OO` patch is negative throughout its interacting birth range. Spatial SIRS has the same obstruction.

### Catalytic-birth no-go

If a positive nonempty target mode appears in `0->r` but not in active-source transitions into `r`, then the relevant outgoing hidden coefficient is negative; if the source record can repeat after that hidden outcome, a realized arbitrarily short `OO` patch is negative.

## E10. Structurally distinct application: Potts Metropolis

**Settled negatively in Assignment 010. Outcome `STOP-SECOND-APPLICATION-POSITIVITY-FAILS`.**

The model was selected before positivity calculation: three-state zero-field ferromagnetic Potts with single-spin Metropolis Glauber dynamics.

For

\[
z=e^{-\beta J},
\]

and common proposal rate `q`,

\[
c^{x\to y}=qz^{(n_x-n_y)_+}.
\]

The exact empty-target transfer is

\[
K=q
\begin{pmatrix}
0&0&0\\
z^4&-(z^4+2)&1-z^4\\
z^4&1-z^4&-(z^4+2)
\end{pmatrix}.
\]

A source-type-1 singleton target-type-1 successful record has outgoing row

\[
\mathbf a_{1;1,0}
=
\left(
qz^2(1-z^2),
q(z-1)(z^3+z^2-1),
-qz^2(1-z^2)
\right).
\]

Thus for every `0<z<1`, hidden outcomes are genuinely nondeterministic and

\[
a_1^2=-qz^2(1-z^2)<0.
\]

A source-type-2 successful record can follow, so a realized short `OO` patch is negative. Therefore Potts Metropolis is not typed patch positive at any interacting finite-temperature point.

This is nondegenerate with respect to the novelty anchor: hidden marks and typed cemetery conflicts are genuinely realized.

At the exact gate

\[
z=1/2,
\qquad q=1,
\qquad t_*=(8/3)\log(5/4),
\]

\[
N_{OO}(t_*)=-3884/390625<0.
\]

### General short-`OO` contrast lemma

Assignment 010 identifies the broader local obstruction:

> if active types `r!=s` and a nonempty target `tau` satisfy
> \[
> a_r^s(\tau)=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0,
> \]
> the hidden outcome `s` is realizable, and a positive-hazard source-`s` successful record can follow, then a realized arbitrarily short `OO` patch is negative.

Assignment 009's catalytic-birth obstruction is a special case. Potts shows the same sign obstruction with all states active, every directed physical replacement positive, and direct active-to-active retyping.

## E11. Multistate bulk positivity as an application engine

**Evidence now negative. No automatic third application search.**

Two materially different natural architectures have genuinely activated the killed typed geometry and nevertheless failed bulk positivity by local short-`OO` signs:

1. contact/epidemic birth plus local stage/recovery conversion;
2. symmetric active-to-active Metropolis retyping.

This is enough to lower the expected value of further model search based on hoping for patch positivity. The programme should not continue by testing cosmetic model variants.

## E12. Representation-only consequences

**Open only as an opportunity-cost question, not yet an assigned block.**

The representation theorem survives both negative applications. The next scientifically distinct question, if the programme continues, is:

> Can the cemetery-aware killed typed patch representation yield a useful cancellation identity, norm estimate, finite-volume formula, or comparison that does **not** require every bulk contribution to be nonnegative?

A positive answer would use the actual surviving novelty anchor rather than the increasingly restrictive positivity property.

No Assignment 011 is queued. Independent verification of Assignment 010 and an explicit Professor opportunity-cost decision should precede any continuation.

## E13. Generic `d>3` tractable positivity

**Deferred.**

The representation already holds for arbitrary finite `d`, while higher-order scalar response positivity overlaps established external-positivity theory. Do not activate generic `d>3` algebra by default.

## E14. Multi-site physical updates

**Downstream/outside current scope.**

Simultaneous multi-site physical updates remain outside the proved representation class.

## Current novelty framing

Do not claim novelty for finite-state duality, signed FK duality, partial Poisson revelation, Metzler semigroups or scalar external positivity individually.

The plausible contribution remains the killed typed patch **interface**. Assignments 009--010 show both that this interface occurs naturally and that bulk positivity is much more restrictive than the representation itself.
