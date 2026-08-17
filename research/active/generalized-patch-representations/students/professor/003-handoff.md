# Assignment 003 handoff

Date: 2026-08-17

Outcome: **`CONTINUE-TYPED-POSITIVITY`**.

## What is now established

For finite-state bounded finite-range single-site replacement IPS in the reference-state indicator tensor basis, the signed typed dual from Assignment 001 and killed/noncemetery factorization from Assignment 002 yield an exact finite-horizon patch representation.

The local intrinsic patch weight is

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

and

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

Using the killed Mecke theorem, not bare conditioning,

\[
P_TH_{\xi_0}(\eta)
=
\int\prod_PE_P[w_P1_{Con(P)}]m_T(dg)
=
\int\prod_PC_P(\eta)\nu_T(dg).
\]

The outer measure is

\[
\nu_T(dg)=P(G_T\in dg,\tau_\dagger>T),
\]

or equivalently one may use the killed skeleton with a single cemetery atom of contribution zero.

## Bulk/end separation

For bulk patches,

\[
C(P)=E_P^{con}[A_P]
\]

is independent of terminal physical data and depends only on local typed boundary data, interval length, source site, and local dual coefficients.

For end patches,

\[
C_T(x,P)=B_0(P)+\sum_{a\in E_*}B_a(P)1_{\{x=a\}},
\]

where

\[
B_a(P)=E_P^{con}[A_P1_{\{X_T^P=a\}}].
\]

Thus all physical terminal dependence is one-site and in the same basis used for the dual.

## Exact binary reduction

At `d=2`, the selected hidden outcome is split/death versus birth/survival, effective empty-target deaths have positive sign, `v_{i,1}` is exactly the paper's `V_i`, and the end factor is `eta_i^{X_T}`. Typed conflict disappears, so `nu_T` becomes the ordinary binary successful-skeleton law. The representation is mathematically the canonical binary patch representation.

## Mandatory verifier

`students/professor/003-typed-representation-verifier.py`, commit `50f28f62`.

Expected final output includes:

- `d=3 hidden configurations checked: 32`;
- `d=3 incoming-target-conflict configurations: 8`;
- `cemetery x terminal-configuration zero checks: 16`;
- `noncemetery exact-skeleton pathwise weight checks: 18`;
- `weighted representation cells checked: 64`;
- `selected outgoing sign-ledger checks: 128`;
- `effective empty-target sign checks: 16`;
- `bulk eta-independence checks: 32`;
- `end one-site locality checks: 128`;
- `d=2 typed/binary specialization checks: 8`;
- `all explicit typed patch-representation checks passed`.

The script uses `Fraction` arithmetic and exact symbolic weights `c exp(q)`. It does not evaluate exponentials numerically.

## Decisive files

- `003a-local-typed-patch-weight.md`, commit `992552ca`;
- verifier `003-typed-representation-verifier.py`, commit `50f28f62`;
- `003b-pathwise-typed-patch-product.md`, commit `1f58d2f3`;
- `003c-exact-typed-semigroup-representation.md`, commit `6eebcaa5`;
- `003d-bulk-end-separation-and-binary-reduction.md`, commit `4f9c250b`;
- final report `003-typed-patch-representation.md`, commit `ed5492e8`.

## Important caveat retained from Assignment 002

Do not state ordinary conditional independence given only the typed successful record list. It is false on cemetery-capable skeletons. The exact representation uses `1_{tau_dagger>T}`, the noncemetery submeasure `nu_T`, or the killed skeleton with cemetery atom.

## Next proof-spine edge

The next question is finally the principal's positivity question in a precise form:

> characterize or obtain useful coefficient-level sufficient conditions for
> \[
> C(P)=E_P^{con}[A_P]\ge0
> \]
> for **every bulk typed patch shape and typed boundary label**.

A useful first step is to write each bulk contribution as a finite-dimensional signed Feynman--Kac / killed-CTMC matrix element on local type space `E`, then determine what positivity property of those transfer matrices corresponds to all-patch nonnegativity.

No generalized positivity condition has yet been asserted, and no literature novelty audit has yet been performed.

No writes to `main`.