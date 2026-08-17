# Meeting 002: typed patch factorization survives via killed skeleton

Date: 2026-08-17

`state_narrowed: yes`.

## Inputs

Assignment 002 was executed by the Professor because no graduate-student session is currently operational.

Decisive files:

- local typed patch consistency: `students/professor/002a-typed-patch-local-consistency.md`, commit `08108e32`;
- exact finite conflict gate: `002b-finite-cemetery-factorization-gate.md`, commit `d8eca517`;
- finite verifier: `002-typed-factorization-verifier.py`, commit `b9e75b42`;
- weighted Mecke theorem: `002c-weighted-typed-patch-factorization.md`, commit `925c8330`;
- final report: `002-typed-patch-factorization.md`, commit `40b93ede`;
- handoff: `002-handoff.md`, commit `1ea088af`.

## Ruling

Assignment 002 ends

**`CONTINUE-TYPED-REPRESENTATION`.**

The one-site patch decomposition remains viable for finite-state single-site replacement dynamics, but the outer skeleton must be interpreted as a noncemetery/killed skeleton for exact conditional independence.

## 1. Local typed consistency

A patch carries local state `X^P in E`. The binary interior and outgoing conditions generalize directly. The new incoming condition is

\[
X_{e-}^P\in\{0,a\}
\]

when the selected record brings target type `a` to that site.

A different active type is a conflict and sends the global typed dual to cemetery.

For an inserted candidate record list `g`,

\[
\{\tau_\dagger>T\}\cap\{G_T=g\}
=
\bigcap_P Con(P).
\]

Thus exact **noncemetery** skeleton consistency is still a product of source--time-strip events.

## 2. Bare record-list factorization is false

The mandatory `d=3` gate deliberately includes a typed incoming conflict.

Two consecutive selected records are arranged so that the hidden outcome of the first record, together with one intervening empty-target retyping mark, determines whether the second record's incoming target conflicts.

After the second record, future nonempty clocks lie in end patches. If conflict occurred, the process is already in cemetery and these future clocks are unconstrained; if no conflict occurred, they must be suppressed to keep the same record list.

With five independent fair hidden variables, the bare two-record skeleton has mass `17/32` and its noncemetery part mass `9/32`.

For conflict event `K` and future mark `B`,

\[
P(K\mid G)=8/17,
\qquad
P(B\mid G)=4/17,
\]

but

\[
P(K,B\mid G)=4/17\ne32/289.
\]

Therefore the binary statement “patch variables are independent conditional only on the successful record list” is false for the typed generalization.

This failure is now part of the theorem statement and must not be forgotten later.

## 3. Cemetery weighting repairs the theorem exactly

The signed typed dual has `H_dagger=0`. Hence every cemetery history has exact Feynman--Kac weight zero.

The weighted Mecke theorem is

\[
E\left[h(G_T)1_{\{\tau_\dagger>T\}}\prod_Pf_P\right]
=
\int h(g)\prod_PE_P[f_P1_{Con(P)}]m_T(dg),
\]

with typed record intensity

\[
m_T(dg)=\prod_k\Lambda_{i_k,r_k}(\tau_k)dt_k.
\]

Consequently the noncemetery skeleton submeasure is

\[
\nu_T(dg)=\prod_PP_P(Con(P))m_T(dg),
\]

and conditional on `G_T=g, tau_dagger>T` the patch variables are independent with normalized consistent laws.

Equivalently, collapse every cemetery path to one outer skeleton atom `dagger`; ordinary killed-skeleton values have the product conditional law, while the cemetery atom contributes zero to the semigroup representation.

## 4. Why neither stop condition fires

`STOP-NO-LOCAL-CONSISTENCY` is false: on noncemetery histories exact skeleton consistency is local and multiplicative.

`STOP-TYPED-CONFLICT-COUPLING` is also false: target conflict does create cross-patch dependence under bare conditioning, but that dependence is entirely carried by paths whose Feynman--Kac duality weight is identically zero.

No approximation or discarded nonzero term is used.

## 5. Next proof-spine edge

Do not define generalized patch positivity yet.

The next bounded theorem is the explicit typed patch representation. On a noncemetery path the additive potential and sign coordinate must be allocated to one-site patches, and the terminal tensor observable must be allocated to end patches. The target formula is

\[
P_TH_{\xi_0}(\eta)
=
\int\prod_PE_P[w_P1_{Con(P)}]m_T(dg)
=
\int\prod_PC_P(\eta)\,\nu_T(dg).
\]

Bulk contributions should depend only on patch shape/local dual data. End contributions may depend on the terminal physical configuration through the one-site basis factor.

Only after this exact representation is proved should the programme define typed patch positivity.

## Publication boundary

All material remains on `research/generalized-patch-representations`. No write or merge to `main` is authorized.
