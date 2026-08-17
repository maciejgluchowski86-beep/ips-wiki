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

Latest meeting: `meetings/002-weighted-typed-patch-factorization.md`.

## Assignment 001

Status: **`CONTINUE-TYPED-PATCH`**.

For finite `E={0,...,d-1}` with reference state `0`, the indicator tensor basis gives finite typed active configurations and an exact signed local Feynman--Kac dual for general bounded single-site replacement dynamics.

For active source type `r`, target `tau`, and source outcome `s`, the branch coefficients are fixed local numbers `a_{i,r}^s(tau)`. Their absolute values are Poisson rates; signs are branch marks; target conflicts affect only the deterministic transition to cemetery.

For nonempty target, the successful record is

\[
(i,t,r,\tau),
\]

which reveals pre-source type and typed target but hides post-source outcome `s`.

Decisive report/verifier:

- `students/professor/001-finite-state-duality.md`, commit `2f37d6bf`;
- `001-finite-state-duality-verifier.py`, commit `c8e47458`.

## Assignment 002

Status: **`CONTINUE-TYPED-REPRESENTATION`**.

The one-site typed patch geometry survives, with local state `X^P in E` and new incoming compatibility condition

\[
X_{e-}^P\in\{0,a\}
\]

for an incoming target type `a`.

On an inserted candidate record list `g`, exact noncemetery skeleton consistency is

\[
\boxed{
\{\tau_\dagger>T\}\cap\{G_T=g\}
=
\bigcap_P\operatorname{Con}(P).}
\]

### Bare conditional factorization fails

A selected incoming target may conflict, sending the global dual to cemetery and simultaneously removing all future no-record constraints. The exact `d=3` two-record gate gives

\[
P(K,B\mid G)=\frac4{17}
\ne
\frac{32}{289}
=P(K\mid G)P(B\mid G).
\]

Thus patch variables are not independent conditional only on the coarse record list.

### Weighted/killed factorization succeeds

Since `H_dagger=0`, cemetery histories have exact Feynman--Kac weight zero. The representation-sufficient theorem is

\[
E\left[h(G_T)1_{\{\tau_\dagger>T\}}\prod_Pf_P\right]
=
\int h(g)\prod_PE_P[f_P1_{Con(P)}]m_T(dg),
\]

where

\[
m_T(dg)=\prod_k\Lambda_{i_k,r_k}(\tau_k)dt_k.
\]

The noncemetery skeleton submeasure therefore has density

\[
\nu_T(dg)=\prod_PP_P(Con(P))m_T(dg),
\]

and conditional on `G_T=g, tau_dagger>T` the patch variables are independent with laws `P_P^con`.

Equivalently collapse every cemetery history to one outer atom and use the killed successful skeleton.

Decisive files:

- `students/professor/002a-typed-patch-local-consistency.md`, commit `08108e32`;
- `002b-finite-cemetery-factorization-gate.md`, commit `d8eca517`;
- `002-typed-factorization-verifier.py`, commit `b9e75b42`;
- `002c-weighted-typed-patch-factorization.md`, commit `925c8330`;
- final report `002-typed-patch-factorization.md`, commit `40b93ede`;
- handoff `002-handoff.md`, commit `1ea088af`.

## Current proof-spine edge

**Explicit typed patch representation.**

Before any positivity definition, factor the noncemetery Feynman--Kac variable into one local weight per typed patch:

1. outgoing-start hidden-branch sign;
2. signs of effective empty-target interior marks;
3. local potential integral;
4. one-site terminal tensor factor on end patches.

Target formula:

\[
P_TH_{\xi_0}(\eta)
=
\int\prod_PE_P[w_P1_{Con(P)}]m_T(dg)
=
\int\prod_PC_P(\eta)\,\nu_T(dg).
\]

Bulk contributions should not depend on the physical terminal configuration; end contributions may.

Patch positivity remains downstream.

## Scope and publication boundary

The current construction covers finite-state, bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

Existing patch pages under `docs/entries/` are source material and are not generalized in place. No programme content is to be published to `main` unless the principal later gives a separate instruction.

All previously stopped programmes remain closed at their existing rulings.
