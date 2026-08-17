# Programme state

Date: 2026-08-17

## Active direction

Generalize the patch-representation / patch-positivity framework of the canonical paper `paper/` beyond binary flip spin systems.

Branch: `research/generalized-patch-representations`.

Workspace: `research/active/generalized-patch-representations/`.

Branch-only wiki section:

- `docs/generalized-patch-representations.md`;
- `docs/generalized-patch-representations/`.

Nothing from this programme is to be written or merged to `main` without a later principal instruction.

Latest meeting: `meetings/003-explicit-typed-patch-representation.md`.

## Assignment 001

Status: **`CONTINUE-TYPED-PATCH`**.

For finite `E={0,...,d-1}` with reference state `0`, the reference-state indicator tensor basis yields typed active configurations and an exact signed local Feynman--Kac dual for general bounded finite-range single-site replacement dynamics.

For nonempty target, the successful record

\[
(i,t,r,\tau)
\]

reveals the pre-source type and typed target while hiding the post-source outcome. The `d=2` specialization is exactly the canonical death/split/birth dual.

## Assignment 002

Status: **`CONTINUE-TYPED-REPRESENTATION`**.

One-site typed patch geometry survives, but bare conditional factorization given only the coarse record list fails because incoming typed conflicts can hit cemetery and remove all future no-record constraints.

The exact `d=3` gate gives

\[
P(K,B\mid G)=4/17\ne32/289=P(K\mid G)P(B\mid G).
\]

Since `H_dagger=0`, the representation-sufficient killed/noncemetery factorization is exact:

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

## Assignment 003

Status: **`CONTINUE-TYPED-POSITIVITY`**.

The explicit local intrinsic weight is

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

with `bar v_{i,0}=0`. The full patch weight is

\[
w_P=
\begin{cases}
A_P,&P\text{ bulk},\\
A_Ph_{X_T^P}(\eta_{i(P)}),&P\text{ end}.
\end{cases}
\]

On every noncemetery trajectory,

\[
\sigma_Te^{\int_0^TV(\xi_u)du}H_{\xi_T}(\eta)
=
\prod_Pw_P.
\]

Combining this pathwise identity with Assignment 002 gives the exact killed-skeleton representation

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

and are independent of terminal physical data. End contributions have the explicit one-site expansion

\[
C_T(x,P)
=B_0(P)+\sum_{a\in E_*}B_a(P)1_{\{x=a\}}.
\]

The `d=2` reduction is exactly the canonical binary patch weight and representation. Typed conflict disappears there, so the killed skeleton is the ordinary binary successful skeleton.

Decisive files:

- `students/professor/003a-local-typed-patch-weight.md`, commit `992552ca`;
- verifier `003-typed-representation-verifier.py`, commit `50f28f62`;
- `003b-pathwise-typed-patch-product.md`, commit `1f58d2f3`;
- `003c-exact-typed-semigroup-representation.md`, commit `6eebcaa5`;
- `003d-bulk-end-separation-and-binary-reduction.md`, commit `4f9c250b`;
- final report `003-typed-patch-representation.md`, commit `ed5492e8`;
- handoff `003-handoff.md`, commit `b46a63dc`;
- Meeting 003, commit `7d20767f`.

## Current proof-spine edge

**Characterize nonnegative bulk typed patch contributions.**

The object is now unambiguous:

\[
C(P)=E_P^{con}[A_P].
\]

The next bounded block should derive a finite-dimensional transfer-matrix / killed-CTMC formula for every bulk boundary type and determine what coefficient-level condition is equivalent to, or at least usefully sufficient for,

\[
C(P)\ge0
\]

for every finite bulk typed patch.

No generalized positivity criterion has yet been asserted.

## Scope, novelty and publication boundary

The proved class is finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

No literature novelty claim has yet been made for the generalized representation theorem. A targeted literature audit should occur after the positivity statement is stable enough to identify the theorem actually being claimed.

Existing patch pages under `docs/entries/` are source material and are not generalized in place. Stable current research may be kept only in the designated branch-only generalized-patch wiki section.

**Do not publish or merge any programme content to `main`.**

All previously stopped programmes remain closed at their existing rulings.