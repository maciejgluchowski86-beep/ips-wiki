# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Active scientific direction

**Generalized patch representations and patch positivity for interacting particle systems.**

- Branch: `research/generalized-patch-representations`.
- Workspace: `research/active/generalized-patch-representations/`.
- Branch-only wiki hub: `docs/generalized-patch-representations.md`.
- Branch-only wiki section: `docs/generalized-patch-representations/`.
- Latest meeting: `meetings/004-typed-bulk-transfer-recovers-binary-positivity.md`.
- Executor: Professor, because no graduate-student session is currently operational.

The principal asks whether the canonical patch-positivity framework extends to more general IPS: more local states, updates beyond binary flips, corresponding signed duals, a successful-interaction analogue hiding finite local information, generalized patches/positivity, and applications.

The core mechanism is conditional averaging of hidden local marks inside spacetime patches before signed contributions are compared.

## Canonical binary benchmark

The manuscript under `paper/`, *Patch representations and convergence for facilitated spin systems*, is authoritative for the binary construction. Existing patch pages under `docs/entries/` remain source/expository material and are not generalized in place.

## Established generalized structure

### Assignment 001: finite-state typed duality

Outcome: **`CONTINUE-TYPED-PATCH`**.

For finite `E={0,...,d-1}` with reference state `0`, the indicator tensor basis gives typed active configurations and an exact fixed-local-clock signed Feynman--Kac dual for bounded finite-range single-site replacement IPS. Successful nonempty records are

\[
(i,t,r,\tau),
\]

revealing pre-source type and typed target while hiding post-source outcome.

### Assignment 002: typed patch factorization

Outcome: **`CONTINUE-TYPED-REPRESENTATION`**.

Bare conditioning fails because incoming typed conflicts can hit cemetery and remove future no-record constraints. Since `H_dagger=0`, the killed/noncemetery weighted factorization is exact and sufficient for the semigroup representation.

### Assignment 003: explicit typed patch representation

Outcome: **`CONTINUE-TYPED-POSITIVITY`**.

Bulk contributions are

\[
C(P)=E_P^{con}[A_P]
\]

and are independent of terminal physical data. End contributions are one-site functions in the same indicator basis. The exact killed-skeleton semigroup representation is proved and specializes exactly to the canonical binary representation.

### Assignment 004: typed bulk transfer and positivity

Outcome: **`CONTINUE-TYPED-POSITIVITY-CRITERION`**.

For active local type `r`, the weighted killed Feynman--Kac interior transfer has the exact finite generator

\[
\boxed{K_i(0,\cdot)=0,
\qquad K_i(r,s)=a_{i,r}^s(\emptyset).}
\]

The cancellation producing this matrix is exact: empty-target escape subtraction and nonempty-target no-success killing cancel against the corresponding pieces of the local potential.

The unsigned consistency transfer is

\[
B_i(r,s)=|a_{i,r}^s(\emptyset)|\quad(s\ne r),
\]

\[
B_i(r,r)=
-\sum_{s\ne r}|a_{i,r}^s(\emptyset)|
-\sum_{\tau\ne\emptyset}\sum_s|a_{i,r}^s(\tau)|,
\]

with zero inactive row.

For terminal columns

\[
f_b^I=e_0^T+e_b^T,
\qquad f_r^O=e_r^T,
\]

and outgoing initial signed row

\[
\mathbf a_{r,\tau}=(a_{i,r}^s(\tau))_{s\in E},
\]

typed bulk patch positivity is exactly nonnegativity of

\[
e_a e^{tK_i}f_b^I,
\qquad
e_a e^{tK_i}f_r^O,
\]

\[
\mathbf a_{r,\tau}e^{tK_i}f_b^I,
\qquad
\mathbf a_{r,\tau}e^{tK_i}f_{r_e}^O
\]

for every realizable descriptor and every `t>0`. The corresponding denominators use `B_i` and are positive on realized descriptors.

This is the exact generalized bulk positivity property; no entrywise-positive-matrix surrogate is imposed.

The binary specialization recovers **exactly** the canonical coefficient criterion

\[
c_i^0(S)+c_i^1(S)\le0,
\qquad
c_i^1(\emptyset)c_i^0(S)
\ge
c_i^0(\emptyset)c_i^1(S),
\]

when `c_i^0(emptyset)+c_i^1(emptyset)>0`, with the exact exceptional clause `c_i\equiv0` when that sum is zero.

Final verifier: `students/professor/004-typed-transfer-verifier.py`, commit `0bbfccd0`. The final `d=3` gate reconstructs all typed coefficient rows from an actual one-neighbour three-state generator with nonnegative physical rates.

Final report: `students/professor/004-typed-bulk-positivity-transfer.md`, commit `be4429bc`.

Meeting 004: commit `b9673290`.

## Current proof-spine edge

**Tractable coefficient characterization of typed bulk patch positivity.**

The exact all-length semigroup-positive family is known. The next bounded block should determine whether it admits finite/local coefficient inequalities for a nontrivial multi-state class, or isolate the obstruction to such a reduction.

Applications and convergence remain downstream and are not active.

## Scope, novelty and publication boundary

Current proved scope: finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis.

Simultaneous multi-site physical updates remain outside scope.

No literature novelty claim has yet been made for the generalized theorem. A targeted literature audit remains necessary once a coefficient-level statement is stable enough to compare precisely.

Stable current research may be recorded only in the designated branch-only generalized-patch wiki section.

**Do not publish or merge any programme content to `main`.**

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` are outside the active write surface.

All previously stopped programmes remain closed and are not reopened by this direction.
