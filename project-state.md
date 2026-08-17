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
- Latest meeting: `meetings/002-weighted-typed-patch-factorization.md`.
- Executor: Professor, because no graduate-student session is currently operational.

The principal asks whether the patch-positivity framework can be extended to more general IPS: more local states, updates beyond binary flips, corresponding signed duals, a successful-interaction analogue which reveals a coarse spacetime skeleton while hiding finite local information, generalized patches/positivity, and applications.

The core mechanism is conditional averaging of hidden local marks inside spacetime patches before signed contributions are compared.

## Canonical binary benchmark

The manuscript under `paper/`, *Patch representations and convergence for facilitated spin systems*, is authoritative for the binary construction. Existing patch pages under `docs/entries/` remain source/expository material and are not generalized in place.

## Assignment 001: finite-state typed duality

Outcome: **`CONTINUE-TYPED-PATCH`**.

For finite `E={0,...,d-1}` with reference state `0`, the indicator tensor basis gives typed active configurations and an exact local signed Feynman--Kac dual for general bounded finite-range single-site replacement dynamics.

For nonempty target, the successful record

\[
(i,t,r,\tau)
\]

reveals the pre-interaction source type and typed target while hiding the post-interaction source outcome. The `d=2` specialization is exactly the canonical death/split/birth dual.

Decisive report/verifier:

- `research/active/generalized-patch-representations/students/professor/001-finite-state-duality.md`, commit `2f37d6bf`;
- `001-finite-state-duality-verifier.py`, commit `c8e47458`.

## Assignment 002: typed patch factorization

Outcome: **`CONTINUE-TYPED-REPRESENTATION`**.

A typed patch carries local state `X^P in E`. The new incoming terminal condition is

\[
X_{e-}^P\in\{0,a\}
\]

for incoming target type `a`; a different active type causes cemetery.

For inserted record list `g`, exact noncemetery consistency is patch-local:

\[
\{\tau_\dagger>T\}\cap\{G_T=g\}
=
\bigcap_PCon(P).
\]

### Bare conditional independence fails

The mandatory `d=3` two-record gate exhibits genuine conflict-induced dependence:

\[
P(K,B\mid G)=\frac4{17}
\ne
\frac{32}{289}
=P(K\mid G)P(B\mid G).
\]

A selected incoming target can conflict and send the dual to cemetery, after which every future no-record constraint disappears.

### Killed/noncemetery factorization succeeds exactly

Since `H_dagger=0`, cemetery histories have exact Feynman--Kac weight zero. The weighted Mecke identity is

\[
E\left[h(G_T)1_{\{\tau_\dagger>T\}}\prod_Pf_P\right]
=
\int h(g)\prod_PE_P[f_P1_{Con(P)}]m_T(dg),
\]

with

\[
m_T(dg)=\prod_k\Lambda_{i_k,r_k}(\tau_k)dt_k.
\]

Hence the noncemetery skeleton submeasure satisfies

\[
\nu_T(dg)=\prod_PP_P(Con(P))m_T(dg),
\]

and conditional on `G_T=g, tau_dagger>T` the patch variables are independent with normalized consistent laws.

Decisive files:

- `students/professor/002-typed-factorization-verifier.py`, commit `b9e75b42`;
- `002c-weighted-typed-patch-factorization.md`, commit `925c8330`;
- final report `002-typed-patch-factorization.md`, commit `40b93ede`;
- handoff `002-handoff.md`, commit `1ea088af`;
- Meeting 002, commit `edabce75`.

## Current proof-spine edge

**Explicit typed patch representation.**

Before any positivity definition, factor the noncemetery Feynman--Kac variable into one local weight per typed patch: outgoing hidden-branch sign, effective empty-target signs, local potential integral, and end-patch terminal one-site tensor factor.

Target:

\[
P_TH_{\xi_0}(\eta)
=
\int\prod_PE_P[w_P1_{Con(P)}]m_T(dg)
=
\int\prod_PC_P(\eta)\,\nu_T(dg).
\]

Only after this theorem should the programme define typed patch positivity.

## Scope, novelty and publication boundary

The proved class is finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

No literature novelty claim has yet been made for the generalized theorem; a targeted literature audit should occur once the representation/positivity statement is stable enough to compare precisely.

The research loop may keep stable notation and constructions in `docs/generalized-patch-representations/` on this branch.

**Do not publish or merge any of this programme to `main`.** Main is outside the active write surface.

Previously stopped programmes remain closed at their existing rulings and are not reopened by this direction.
