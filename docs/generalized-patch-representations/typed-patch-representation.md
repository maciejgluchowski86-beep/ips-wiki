# Explicit typed patch representation

> **Current research.** This page belongs only to `research/generalized-patch-representations`. It records the representation proved in the active research workspace and has not yet undergone an external novelty audit.

## Setting

Let

\[
E=\{0,1,\ldots,d-1\},\qquad E_*=E\setminus\{0\},
\]

and use the one-site basis

\[
h_0\equiv1,\qquad h_a(x)=1_{\{x=a\}},\quad a\in E_*.
\]

A finite typed active configuration `xi` is a finite partial map from sites into `E_*`, with tensor observable

\[
H_\xi(\eta)=\prod_{i\in\operatorname{supp}\xi}h_{\xi(i)}(\eta_i).
\]

For bounded finite-range single-site replacement dynamics, the [finite-state typed duality](finite-state-typed-duality.md) gives fixed local signed branches indexed by source type `r`, source outcome `s`, and typed target `tau`. Nonempty-target successful records are

\[
(i,t,r,\tau),
\]

and hide the post-source outcome `s`.

The [typed successful-skeleton factorization](typed-patch-factorization.md) shows that ordinary conditional independence given only this record list fails when an incoming typed target can conflict. The exact replacement is the killed/noncemetery skeleton measure

\[
\nu_T(dg)=P(G_T\in dg,\tau_\dagger>T).
\]

## Local patch weight

Let `P` be a one-site typed patch with local state

\[
X_u^P\in E,
\]

where `0` is dual-inactive. Put

\[
\bar v_{i,0}=0,
\qquad
\bar v_{i,r}=v_{i,r}\quad(r\in E_*).
\]

Define the intrinsic local factor

\[
A_P
=
\epsilon_{\rm out}(P)
\epsilon_{\emptyset}(P)
\exp\left(
\int_{b(P)}^{e(P)\wedge T}
\bar v_{i(P),X_u^P}\,du
\right).
\]

Here:

- `epsilon_out(P)=1` for an incoming start;
- at an outgoing start, `epsilon_out(P)` is the sign of the hidden selected source-outcome branch;
- `epsilon_empty(P)` is the product of signs of the effective empty-target jumps inside the patch.

The full patch weight is

\[
w_P(\Sigma_P;\eta)
=
\begin{cases}
A_P,&P\text{ is bulk},\\
A_Ph_{X_T^P}(\eta_{i(P)}),&P\text{ is an end patch}.
\end{cases}
\]

Every selected nonempty-target sign is assigned only to the outgoing-start patch at its source. Incoming target patches carry no duplicate sign.

## Pathwise identity

On every noncemetery realization through time `T`,

\[
\boxed{
\sigma_T
\exp\left(\int_0^TV(\xi_u)\,du\right)
H_{\xi_T}(\eta)
=
\prod_{P\in\mathcal P_T(G_T)}w_P(\Sigma_P;\eta).}
\]

The reason is local bookkeeping:

1. acting nonempty-target jumps are exactly the selected successful records and each sign belongs to one outgoing source patch;
2. acting empty-target jumps lie inside one source-time patch;
3. the additive potential splits over the one-site patch intervals;
4. the terminal typed tensor observable splits over the distinct end-patch sites.

Source deletion sets the local potential integrand to zero. Source retyping switches it to the potential associated with the new type. An idempotent incoming merge creates no additional sign.

## Exact semigroup representation

Cemetery paths have exact duality weight zero because `H_dagger=0`. Combining the pathwise identity with the killed weighted factorization gives

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int
\prod_{P\in\mathcal P_T(g)}
E_P\left[w_P1_{Con(P)}\right]
\,m_T(dg).}
\]

Equivalently, define normalized consistent contributions

\[
C_P(\eta)=E_P^{con}[w_P].
\]

Then

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int\prod_PC_P(\eta)\,\nu_T(dg).}
\]

One may instead view the outer variable as a killed successful skeleton with a single cemetery atom whose contribution is defined to be zero.

## Bulk/end separation

For a bulk patch,

\[
\boxed{C(P)=E_P^{con}[A_P].}
\]

This depends only on the source site, interval length, typed boundary data and orientations, and the local dual rates/signs/potential. It is independent of the physical terminal configuration.

For an end patch on site `i`,

\[
C_T(x,P)=E_P^{con}[A_Ph_{X_T^P}(x)].
\]

With

\[
B_a(P)=E_P^{con}[A_P1_{\{X_T^P=a\}}],
\]

we have

\[
\boxed{
C_T(x,P)
=B_0(P)+\sum_{a\in E_*}B_a(P)1_{\{x=a\}}.}
\]

Hence all terminal physical dependence is one-site and appears in the same reference-state indicator basis used to construct the dual.

The semigroup representation can therefore be written as

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int
\left(\prod_{P\in\mathcal B_T(g)}C(P)\right)
\left(\prod_{P\in\mathcal E_T(g)}C_T(\eta_{i(P)},P)\right)
\nu_T(dg).}
\]

## Binary specialization

For `d=2`, the unique active type is `1`.

- hidden source outcome `0` is death/split;
- hidden source outcome `1` is birth/survival;
- the selected outgoing sign is the canonical patch initial sign;
- effective empty-target deaths have positive sign;
- `v_{i,1}` is the binary patch potential `V_i`;
- the end factor is `eta_i^{X_T^P}`.

Typed target conflict is impossible because there is only one active type, so the killed skeleton reduces to the ordinary binary successful skeleton. The formula above is therefore the canonical binary patch representation itself.

## Current next question

The representation layer is complete for finite-state single-site replacement dynamics. The next local problem is to characterize when every bulk contribution satisfies

\[
C(P)\ge0.
\]

A natural first step is to express `C(P)` as a finite-dimensional killed-CTMC / transfer-matrix element on the local type space `E` and then compare the resulting condition with the binary patch-positivity inequalities.