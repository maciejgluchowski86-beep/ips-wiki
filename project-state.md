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
- Latest meeting: `meetings/003-explicit-typed-patch-representation.md`.
- Next bounded assignment: `students/professor/assignment-004-typed-bulk-positivity-transfer.md`, queued and not yet executed.
- Executor: Professor, because no graduate-student session is currently operational.

The principal asks whether the patch-positivity framework can be extended to more general IPS: more local states, updates beyond binary flips, corresponding signed duals, a successful-interaction analogue which reveals a coarse spacetime skeleton while hiding finite local information, generalized patches/positivity, and applications.

The core mechanism is conditional averaging of hidden local marks inside spacetime patches before signed contributions are compared.

## Canonical binary benchmark

The manuscript under `paper/`, *Patch representations and convergence for facilitated spin systems*, is authoritative for the binary construction. Existing patch pages under `docs/entries/` remain source/expository material and are not generalized in place.

## Assignment 001: finite-state typed duality

Outcome: **`CONTINUE-TYPED-PATCH`**.

For finite `E={0,...,d-1}` with reference state `0`, the reference-state indicator tensor basis gives typed active configurations and an exact local signed Feynman--Kac dual for general bounded finite-range single-site replacement dynamics.

For nonempty target, the successful record

\[
(i,t,r,\tau)
\]

reveals the pre-interaction source type and typed target while hiding the post-source outcome. The `d=2` specialization is exactly the canonical death/split/birth dual.

## Assignment 002: typed patch factorization

Outcome: **`CONTINUE-TYPED-REPRESENTATION`**.

Typed incoming target conflicts make bare conditional factorization false. The exact `d=3` gate gives

\[
P(K,B\mid G)=4/17\ne32/289=P(K\mid G)P(B\mid G).
\]

Since `H_dagger=0`, cemetery histories have exact Feynman--Kac weight zero and the killed/noncemetery factorization succeeds:

\[
E\left[h(G_T)1_{\{\tau_\dagger>T\}}\prod_Pf_P\right]
=
\int h(g)\prod_PE_P[f_P1_{Con(P)}]m_T(dg).
\]

Thus

\[
\nu_T(dg)=P(G_T\in dg,\tau_\dagger>T)
=\prod_PP_P(Con(P))m_T(dg).
\]

## Assignment 003: explicit typed patch representation

Outcome: **`CONTINUE-TYPED-POSITIVITY`**.

For patch `P`, let

\[
A_P
=
\epsilon_{\rm out}(P)
\epsilon_{\emptyset}(P)
\exp\left(
\int_{b(P)}^{e(P)\wedge T}
\bar v_{i(P),X_u^P}\,du
\right),
\]

with `bar v_{i,0}=0`, and

\[
w_P=
\begin{cases}
A_P,&P\text{ bulk},\\
A_Ph_{X_T^P}(\eta_{i(P)}),&P\text{ end}.
\end{cases}
\]

On every noncemetery path,

\[
\sigma_Te^{\int_0^TV(\xi_u)du}H_{\xi_T}(\eta)
=
\prod_Pw_P.
\]

The exact semigroup representation is

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int
\left(\prod_{P\in\mathcal B_T(g)}C(P)\right)
\left(\prod_{P\in\mathcal E_T(g)}C_T(\eta_{i(P)},P)\right)
\nu_T(dg).}
\]

Bulk contributions are

\[
C(P)=E_P^{con}[A_P]
\]

and are independent of terminal physical data. End contributions are one-site functions

\[
C_T(x,P)=B_0(P)+\sum_{a\in E_*}B_a(P)1_{\{x=a\}}.
\]

The `d=2` reduction is exactly the canonical binary patch weight and representation. Typed conflicts disappear in the binary case, so the killed skeleton becomes the ordinary successful skeleton.

Decisive Assignment-003 files:

- `students/professor/003a-local-typed-patch-weight.md`, commit `992552ca`;
- verifier `003-typed-representation-verifier.py`, commit `50f28f62`;
- `003b-pathwise-typed-patch-product.md`, commit `1f58d2f3`;
- `003c-exact-typed-semigroup-representation.md`, commit `6eebcaa5`;
- `003d-bulk-end-separation-and-binary-reduction.md`, commit `4f9c250b`;
- final report `003-typed-patch-representation.md`, commit `ed5492e8`;
- handoff `003-handoff.md`, commit `b46a63dc`;
- Meeting 003, commit `7d20767f`.

## Current proof-spine edge

**Typed bulk patch positivity.**

The object is now exact:

\[
C(P)=E_P^{con}[A_P].
\]

Assignment 004 is pre-registered to derive a finite-dimensional signed transfer matrix and the corresponding unsigned consistency/killing matrix for every bulk boundary orientation, then determine the exact numerator inequalities equivalent to all-patch nonnegativity.

A key candidate cancellation to prove or refute is that the signed interior transfer generator reduces to the matrix of empty-target coefficients after the local potential cancels the ordinary jump-rate subtraction and nonempty-target no-success killing.

No generalized patch-positivity criterion has yet been asserted.

## Scope, novelty and publication boundary

The proved class is finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

No literature novelty claim has yet been made for the generalized representation theorem. A targeted literature audit should occur after the positivity theorem is stable enough to identify the actual claimed contribution.

The research loop may keep stable current results only in the separate branch-only section `docs/generalized-patch-representations/`.

**Do not publish or merge any programme content to `main`.**

All previously stopped programmes remain closed at their existing rulings and are not reopened by this direction.