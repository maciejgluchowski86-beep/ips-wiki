# Handoff: Assignment 002 typed patch factorization

Date: 2026-08-17

Outcome: **`CONTINUE-TYPED-REPRESENTATION`**.

## Read first

- `002-typed-patch-factorization.md`, commit `40b93ede`;
- `002c-weighted-typed-patch-factorization.md`, commit `925c8330`;
- `002-typed-factorization-verifier.py`, commit `b9e75b42`;
- `002b-finite-cemetery-factorization-gate.md`, commit `d8eca517`.

## What is proved

For a typed patch local state `X^P in E`, the exact local consistency conditions are:

1. no interior nonempty-target clock has source label equal to `X_{u-}^P`;
2. outgoing terminal `(r,tau)` requires `X_{e-}^P=r`;
3. incoming terminal type `a` requires `X_{e-}^P in {0,a}`;
4. end terminal has no extra condition.

On an inserted candidate skeleton `g`,

\[
1_{\{\tau_\dagger>T\}}1_{\{G_T=g\}}
=
\prod_P1_{\operatorname{Con}(P)}.
\]

Bare conditioning on `G_T=g` does **not** factor in general. The exact `d=3` two-record gate gives an incoming-target conflict and

\[
P(K,B\mid G)=4/17
\ne32/289
=P(K\mid G)P(B\mid G).
\]

The conflict sends the global dual to cemetery and removes future no-record constraints.

But `H_dagger=0`, so cemetery paths have exact Feynman--Kac weight zero. The representation-sufficient weighted Mecke theorem is

\[
E\left[h(G_T)1_{\{\tau_\dagger>T\}}\prod_Pf_P\right]
=
\int h(g)\prod_PE_P[f_P1_{Con(P)}]m_T(dg),
\]

with

\[
m_T(dg)=\prod_k\Lambda_{i_k,r_k}(\tau_k)dt_k.
\]

Thus the noncemetery skeleton submeasure is

\[
\nu_T(dg)=\prod_PP_P(Con(P))m_T(dg),
\]

and conditional on `G_T=g, tau_dagger>T` the patch variables are independent with laws `P_P^con`.

## Finite verifier expectations

Run

`python research/active/generalized-patch-representations/students/professor/002-typed-factorization-verifier.py`

Expected final line:

`all typed patch-factorization finite-gate checks passed`

It should report:

- 32 hidden configurations;
- 8 incoming-target-conflict configurations;
- 32 noncemetery global/local consistency equivalences;
- bare skeleton mass `17/32`;
- noncemetery weighted mass `9/32`;
- bare conditional joint `4/17` versus product `32/289`;
- 32 weighted factorization cells checked.

## Next exact task

Do **not** define positivity yet.

The next block is explicit typed patch representation. Factor the global Feynman--Kac variable on noncemetery paths into one local patch weight containing:

- outgoing-start hidden-branch sign;
- effective empty-target interior signs;
- the local potential integral;
- the terminal one-site indicator on end patches.

Then prove

\[
P_TH_{\xi_0}(\eta)=\int\prod_PE_P[w_P1_{Con(P)}]m_T(dg)
=\int\prod_PC_P(\eta)\,\nu_T(dg).
\]

Only after that theorem should the programme ask what nonnegative bulk contribution means.

## Scope boundary

The current theorem is for finite-state, finite-range, bounded **single-site replacement** dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

No writes to `main`.
