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

Latest meeting: `meetings/004-typed-bulk-transfer-recovers-binary-positivity.md`.

## Assignment 001

Status: **`CONTINUE-TYPED-PATCH`**.

The reference-state indicator tensor basis gives typed active configurations and an exact fixed-local-clock signed Feynman--Kac dual for finite-state bounded finite-range single-site replacement IPS. Nonempty successful records are

\[
(i,t,r,\tau),
\]

revealing the pre-source type and typed target while hiding post-source outcome.

## Assignment 002

Status: **`CONTINUE-TYPED-REPRESENTATION`**.

Bare conditional factorization fails because incoming typed conflicts can hit cemetery and remove all future no-record constraints. The exact replacement is killed/noncemetery weighted factorization, valid because `H_dagger=0`.

## Assignment 003

Status: **`CONTINUE-TYPED-POSITIVITY`**.

The exact typed patch representation is proved. Bulk contributions are

\[
C(P)=E_P^{con}[A_P]
\]

and are independent of terminal physical data; end contributions are one-site indicator-basis functions.

## Assignment 004

Status: **`CONTINUE-TYPED-POSITIVITY-CRITERION`**.

### Signed interior transfer

For active local type `r`, the weighted killed Feynman--Kac transfer has generator

\[
\boxed{K_i(0,\cdot)=0,
\qquad K_i(r,s)=a_{i,r}^s(\emptyset).}
\]

This follows by exact cancellation of empty-target escape subtraction, nonempty-target no-success killing, and the local potential.

### Unsigned consistency transfer

\[
B_i(r,s)=|a_{i,r}^s(\emptyset)|\quad(s\ne r),
\]

\[
B_i(r,r)=
-\sum_{s\ne r}|a_{i,r}^s(\emptyset)|
-\sum_{\tau\ne\emptyset}\sum_s|a_{i,r}^s(\tau)|,
\]

with zero inactive row.

### Four exact bulk numerator families

For

\[
f_b^I=e_0^T+e_b^T,
\qquad f_r^O=e_r^T,
\]

and outgoing initial signed row

\[
\mathbf a_{r,\tau}=(a_{i,r}^s(\tau))_{s\in E},
\]

the four bulk contributions are ratios whose numerators are

\[
e_a e^{tK_i}f_b^I,
\qquad
e_a e^{tK_i}f_r^O,
\]

\[
\mathbf a_{r,\tau}e^{tK_i}f_b^I,
\qquad
\mathbf a_{r,\tau}e^{tK_i}f_{r_e}^O.
\]

The denominators use `e^{tB_i}` and absolute outgoing rows and are positive on realizable descriptors.

Therefore typed bulk patch positivity is **exactly** nonnegativity of these four numerator families for every realizable descriptor and every `t>0`.

### Small-time multi-state constraints

Among the immediate necessary conditions are

\[
a_{i,a}^{r}(\emptyset)\ge0
\quad(a\ne r)
\]

for realizable direct retyping `IO` patches, and

\[
a_{i,r}^{r_e}(\tau)\ge0
\]

for realizable zero-length `OO` limits.

### Binary acceptance test

The `d=2` transfer formulas reduce exactly to the canonical paper's patch formulas. All-length positivity is equivalent to

\[
c_i^0(S)+c_i^1(S)\le0,
\]

\[
c_i^1(\emptyset)c_i^0(S)
\ge
c_i^0(\emptyset)c_i^1(S)
\]

when `c_i^0(emptyset)+c_i^1(emptyset)>0`, and to `c_i\equiv0` in the degenerate case.

Thus there is no binary positivity mismatch.

### Final verifier

`students/professor/004-typed-transfer-verifier.py`, final commit `0bbfccd0`.

The final `d=3` gate reconstructs all typed data from a genuine one-neighbour three-state physical generator and checks physical-rate nonnegativity before transfer identities.

Decisive files:

- `004a-signed-interior-transfer.md`, commit `6248cc68`;
- `004b-unsigned-consistency-transfer.md`, commit `96197d46`;
- `004c-four-orientation-transfer-formulas.md`, commit `6f996224`;
- `004d-small-time-necessary-conditions.md`, commit `c24554c2`;
- `004e-binary-equivalence.md`, commit `f6485b2c`;
- verifier final commit `0bbfccd0`;
- final report `004-typed-bulk-positivity-transfer.md`, commit `be4429bc`;
- handoff `004-handoff.md`, commit `62b9a9fa`;
- Meeting 004, commit `b9673290`.

## Current proof-spine edge

**Tractable coefficient characterization of typed bulk patch positivity.**

The exact all-length semigroup-positive family is known. The next bounded block should determine whether it admits a finite/local coefficient criterion for a nontrivial multi-state class, or isolate the precise obstruction to such a criterion.

Do not move to applications or convergence yet.

## Scope, novelty and publication boundary

Current proved scope: finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis.

Simultaneous multi-site physical updates remain outside scope.

No novelty claim has yet been made for the generalized theorem. Literature audit remains downstream of a stable coefficient-level statement.

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` are not to be modified by this programme. Stable current research may be recorded only in the designated branch-only generalized-patch section.

**Do not publish or merge any programme content to `main`.**

All previously stopped programmes remain closed.
