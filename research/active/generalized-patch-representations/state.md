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

Latest meeting: `meetings/006-exact-three-state-spectral-criterion.md`.

## Established structure

### Assignment 001 — finite-state typed duality

Outcome: **`CONTINUE-TYPED-PATCH`**.

For finite local state space with reference state `0`, the indicator tensor basis gives typed active configurations and an exact fixed-local-clock signed Feynman--Kac dual for bounded finite-range single-site replacement IPS. Successful nonempty records reveal source/time/pre-source type/typed target and hide post-source outcome.

### Assignment 002 — typed patch factorization

Outcome: **`CONTINUE-TYPED-REPRESENTATION`**.

Bare conditioning fails because incoming typed conflicts can hit cemetery and remove future no-record constraints. Since `H_dagger=0`, killed/noncemetery weighted factorization is exact and sufficient for the semigroup representation.

### Assignment 003 — explicit typed patch representation

Outcome: **`CONTINUE-TYPED-POSITIVITY`**.

Bulk contributions are

\[
C(P)=E_P^{con}[A_P]
\]

and are independent of terminal physical data; end contributions are one-site indicator-basis functions. The exact killed-skeleton representation and exact binary specialization are proved.

### Assignment 004 — exact typed bulk positivity transfer

Outcome: **`CONTINUE-TYPED-POSITIVITY-CRITERION`**.

For active local type `r`, the weighted interior transfer is

\[
K_i(0,\cdot)=0,
\qquad
K_i(r,s)=a_{i,r}^s(\emptyset).
\]

Typed bulk patch positivity is exactly nonnegativity of the four finite-dimensional numerator families built from `e^{tK_i}` for every realizable descriptor and `t>0`. The `d=2` specialization is exactly the canonical binary patch-positivity criterion.

### Assignment 005 — endpoint-only three-state criterion

Outcome: **`STOP-NO-FINITE-ENDPOINT-CRITERION`**.

Under boundary completeness, `K` is forced Metzler; incoming-initial and `OO` families become automatic after zero-length constraints. Only `OI` remains.

A genuine one-neighbour physical IPS gives

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t},
\]

with

\[
N(0)=1,
\qquad N(\infty)=1/128,
\]

but

\[
e^{-t_*}=13/153,
\qquad N(t_*)=-1/1224.
\]

Thus binary-style zero/long endpoint inequalities do not characterize `d=3` positivity. The exact semigroup definition remains valid and binary suppression remains exactly canonical.

### Assignment 006 — exact three-state spectral criterion

Outcome: **`CONTINUE-EXACT-THREE-STATE-SPECTRAL-CRITERION`**.

Boundary-complete `d=3` typed bulk patch positivity has a finite necessary-and-sufficient spectral test.

After the Assignment-005 Metzler/zero-length reduction, only

\[
N_{p,b}(t)=p e^{tK}(e_0^T+e_b^T),
\qquad b=1,2,
\]

must be checked.

If the active eigenvalues are distinct and negative,

\[
-\mu,-\nu,
\qquad0<\mu<\nu,
\]

then

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t}.
\]

With

\[
P_0=\frac{(K+\mu I)(K+\nu I)}{\mu\nu},
\quad L=uP_0f,
\quad n_0=uf,
\quad n_1=uKf,
\]

\[
A=\frac{\nu(n_0-L)+n_1}{\nu-\mu},
\qquad
B=\frac{-\mu(n_0-L)-n_1}{\nu-\mu}.
\]

There is at most one interior minimum. It occurs exactly when

\[
A<0<B,
\qquad
0<R=-\frac{\mu A}{\nu B}<1,
\]

and then its exact value is

\[
\boxed{
N(t_*)
=L+\frac{\nu-\mu}{\nu}
A R^{\mu/(\nu-\mu)}.}
\]

Thus each generic `OI` descriptor is decided by zero-length, long-time, and at most one critical-value check.

All degenerate cases are also finite:

- one zero active eigenvalue: one decaying mode;
- repeated nonzero diagonalizable active block: one decaying mode;
- repeated nonzero Jordan block:
  \[
  N(t)=L+(A+Bt)e^{-\mu t},
  \]
  again with at most one interior minimum;
- reducible reference-neighbour chains create no additional time-dependence class because `K` is similar to a finite-state Markov generator and zero is semisimple.

The mandatory exact verifier reproduces the negative Assignment-005 witness and a separate physically realizable boundary-complete `p_0<0` positive example with

\[
p=(-1/8,9/8,3/8),
\]

whose nontrivial critical value is

\[
e^{-t_*}=5/51,
\qquad N(t_*)=15/544>0.
\]

Suppressing type `2` removes the interior-critical branch and recovers exactly the canonical binary coefficient inequalities, with no stronger condition.

Decisive files:

- `students/professor/006a-generic-two-mode-critical-criterion.md`, commit `e79a94a5`;
- `006b-degenerate-spectral-cases.md`, commit `96127a9b`;
- `006-three-state-spectral-verifier.py`, commit `419196b4`;
- `006c-finite-spectral-criterion-and-usability.md`, commit `54334311`;
- `006d-binary-spectral-reduction.md`, commit `93dad82b`;
- final report `006-three-state-spectral-criterion.md`, commit `5957a9cf`;
- handoff `006-handoff.md`, commit `23488674`;
- Meeting 006, commit `80f51dc6`.

## Current proof-spine edge

**Natural simplification / structural subclass for the exact spectral criterion.**

The `d=3` all-time semigroup condition is now finite, but its generic critical inequality contains the genuinely spectral quantity

\[
R^{\mu/(\nu-\mu)}.
\]

Assignment 005 shows this interior information cannot simply be deleted.

The next bounded question is whether there is a mathematically natural non-binary subclass for which the critical condition becomes algebraic, monotone, or otherwise transparent while remaining necessary and sufficient **within that subclass** and retaining exact binary reduction.

Do not move to applications, convergence, or `d>3` yet.

## Scope, novelty and publication boundary

Current proved scope: finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis.

The finite spectral criterion is proved only for the controlled boundary-complete `d=3` class.

Simultaneous multi-site physical updates remain outside scope.

No novelty claim has yet been made. A targeted literature audit remains necessary once the theorem package is stable enough to compare precisely.

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` remain outside the active write surface.

**Do not publish or merge programme content to `main`.**

All previously stopped programmes remain closed.
