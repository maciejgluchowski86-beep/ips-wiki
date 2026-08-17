# Programme state

Date: 2026-08-17

## Active direction

Generalize the canonical patch-representation / patch-positivity framework beyond binary flip spin systems.

Branch: `research/generalized-patch-representations`.

Workspace: `research/active/generalized-patch-representations/`.

Branch-only wiki section:

- `docs/generalized-patch-representations.md`;
- `docs/generalized-patch-representations/`.

Nothing from this programme is to be written or merged to `main` without a later principal instruction.

Latest meeting: `meetings/007-natural-three-state-subclass.md`.

## Established theorem stack

### Assignment 001 — finite-state typed duality

Outcome: **`CONTINUE-TYPED-PATCH`**.

For arbitrary finite local state space with reference state `0`, the indicator tensor basis gives typed active configurations and an exact fixed-local-clock signed Feynman--Kac dual for bounded finite-range single-site replacement IPS. Successful nonempty records reveal source, time, pre-source type, and typed target while hiding post-source outcome.

### Assignment 002 — killed typed patch factorization

Outcome: **`CONTINUE-TYPED-REPRESENTATION`**.

Bare conditioning fails because incoming typed conflicts can hit cemetery and remove future no-record constraints. Since `H_dagger=0`, killed/noncemetery weighted factorization is exact and sufficient for the semigroup representation.

### Assignment 003 — explicit typed patch representation

Outcome: **`CONTINUE-TYPED-POSITIVITY`**.

Bulk contributions are

\[
C(P)=E_P^{con}[A_P]
\]

and are independent of terminal physical data. End contributions are one-site indicator-basis functions. The exact killed-skeleton representation and exact binary specialization are proved.

### Assignment 004 — exact typed bulk positivity transfer

Outcome: **`CONTINUE-TYPED-POSITIVITY-CRITERION`**.

For active local type `r`, the weighted interior transfer is

\[
K_i(0,\cdot)=0,
\qquad
K_i(r,s)=a_{i,r}^s(\emptyset).
\]

Typed bulk patch positivity is exactly nonnegativity of four finite-dimensional numerator families built from `e^{tK_i}` for every realizable descriptor and every patch length. The `d=2` specialization is exactly the canonical binary patch-positivity criterion.

### Assignment 005 — endpoint-only three-state criterion

Outcome: **`STOP-NO-FINITE-ENDPOINT-CRITERION`**.

Under boundary completeness, `K` is forced Metzler; incoming-initial and `OO` families become automatic after zero-length constraints. Only `OI` remains.

A genuine one-neighbour physical IPS gives

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

with positive zero/long endpoints but exact interior minimum `-1/1224`. Thus binary-style endpoint inequalities do not characterize general `d=3` positivity.

### Assignment 006 — exact finite three-state spectral criterion

Outcome: **`CONTINUE-EXACT-THREE-STATE-SPECTRAL-CRITERION`**.

Every remaining boundary-complete `d=3` `OI` numerator has at most two decaying modes. In the generic case

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t},
\qquad0<\mu<\nu,
\]

so all-time nonnegativity is equivalent to endpoint values plus at most one explicitly computed interior critical value. Repeated, zero-eigenvalue, Jordan, and reducible cases are also classified exactly.

The criterion is genuinely finite: no time mesh or scan remains. It reduces exactly to the canonical binary inequalities.

### Assignment 007 — natural exact non-binary subclass

Outcome: **`CONTINUE-NATURAL-THREE-STATE-SUBCLASS`**.

Assume exchange-symmetric reference-neighbour dynamics

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix}
\]

and an exchange-symmetric nonempty-target coefficient family.

Boundary completeness gives the necessary Metzler condition

\[
\boxed{c\ge a.}
\]

For every outgoing row

\[
p=(p_0,p_1,p_2),
\]

typed bulk patch positivity is then equivalent to

\[
\boxed{
p_1,p_2,p_0+p_1,p_0+p_2\ge0,}
\]

\[
\boxed{(b+2a)p_0+a(p_1+p_2)\ge0.}
\]

These conditions are necessary and sufficient inside the subclass.

The mechanism is spectral ordering, not binary quotienting: the antisymmetric active mode decays at least as fast as the symmetric mode. The exact positive gate has `p_1!=p_2`, distinct `OI` values from initial active states 1 and 2, positive physical `1<->2` transitions, and target-dependent perturbations distinguishing the active labels.

Lumpable dynamics plus lumped observables was classified as binary-reducible. One-way active retyping remains genuinely spectral. Destination-rate three-state refresh chains form a repeated-spectrum sibling subclass with an exact one-mode criterion.

Decisive files:

- `students/professor/007a-lumpability-classification.md`, commit `6c41149d`;
- corrected `007b-symmetry-and-refresh-subclass.md`, commit `52e9e7ac`;
- `007c-triangular-still-spectral.md`, commit `c692967d`;
- verifier `007-natural-subclass-verifier.py`, commit `3a12ba34`;
- `007d-exact-subclass-criterion-and-binary-reduction.md`, commit `06199715`;
- final report `007-natural-spectral-simplification.md`, commit `5f9b4b8b`;
- handoff `007-handoff.md`, commit `d465af1d`;
- Meeting 007, commit `a22c87e4`.

## Current proof-spine edge

**Novelty/literature validation before applications.**

The mathematical construction now answers the finite-state representation question at arbitrary finite `d` and provides both an exact `d=3` positivity criterion and a genuinely non-binary algebraic subclass.

Before further abstraction, perform one bounded literature/novelty audit covering:

1. finite-state indicator-tensor / Feynman--Kac duality for interacting particle systems;
2. coarse successful-record skeletons hiding local post-source marks;
3. killed/noncemetery local factorization into spacetime patches;
4. transfer-matrix characterizations of local signed patch positivity;
5. the boundary-complete three-state spectral criterion;
6. the exchange-symmetric / refresh exact subclasses.

No novelty claim is authorized before this audit.

## Ordering after the literature audit

If the audit does **not** show that the generalized mechanism/criterion is already subsumed by prior work, **applications become the next active mathematical block immediately**.

Applications are ready when:

- the genuinely non-binary exact criterion from Assignment 007 remains mathematically available;
- literature does not eliminate the contribution in equivalent terminology; and
- a concrete finite-state single-site replacement model can be written in the typed coefficients and checked against either the symmetric/refresh criterion or the exact `d=3` spectral criterion.

A generic `d>3` tractable-positivity block is **not** next by default. It should activate only if:

- a concrete application naturally requires more than three local states; or
- the literature audit indicates that the arbitrary-`d` criterion itself is the distinctive theorem worth developing.

This ordering is deliberate: the arbitrary finite-state representation has already been proved, whereas continued `d>3` coefficient algebra could postpone the principal's application question indefinitely.

## Scope and publication boundary

Current proved scope: arbitrary finite-state, bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis. Tractable coefficient-level positivity is currently strongest in boundary-complete `d=3` and in the exchange-symmetric / refresh subclasses.

Simultaneous multi-site physical updates remain outside scope.

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` are outside the active write surface.

Stable current research may be recorded only in the designated branch-only generalized-patch section.

**Do not publish or merge any programme content to `main`.**

All previously stopped programmes remain closed.
