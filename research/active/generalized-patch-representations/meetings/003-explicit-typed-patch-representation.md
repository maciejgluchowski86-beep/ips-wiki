# Meeting 003: explicit typed patch representation closes; positivity edge opens

Date: 2026-08-17

`state_narrowed: yes`.

Evidence:

- `students/professor/003a-local-typed-patch-weight.md`, commit `992552ca`;
- exact verifier `students/professor/003-typed-representation-verifier.py`, commit `50f28f62`;
- `students/professor/003b-pathwise-typed-patch-product.md`, commit `1f58d2f3`;
- `students/professor/003c-exact-typed-semigroup-representation.md`, commit `6eebcaa5`;
- `students/professor/003d-bulk-end-separation-and-binary-reduction.md`, commit `4f9c250b`;
- final report `students/professor/003-typed-patch-representation.md`, commit `ed5492e8`;
- handoff `students/professor/003-handoff.md`, commit `b46a63dc`.

## Ruling

Assignment 003 ends

**`CONTINUE-TYPED-POSITIVITY`.**

The finite-state typed dual now has the full representation layer requested by the principal before positivity:

1. explicit one-patch Feynman--Kac weight;
2. pathwise product identity;
3. exact semigroup representation using the killed/noncemetery skeleton;
4. bulk/end separation;
5. exact binary specialization.

Neither `STOP-NONLOCAL-FK-WEIGHT` nor `STOP-NO-BULK-END-SEPARATION` occurs.

## 1. Local weight

For patch `P`, define

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

with `bar v_{i,0}=0`. The full weight is

\[
w_P=
\begin{cases}
A_P,&P\text{ bulk},\\
A_Ph_{X_T^P}(\eta_{i(P)}),&P\text{ end}.
\end{cases}
\]

Every selected nonempty-target sign belongs to the unique outgoing-start patch at its source. Every effective empty-target sign belongs to the unique patch interior containing that mark. The diagonal empty-target source-survival coefficient remains in the local potential.

## 2. Pathwise theorem

On every noncemetery realization,

\[
\sigma_T
\exp\left(\int_0^TV(\xi_u)du\right)
H_{\xi_T}(\eta)
=
\prod_{P\in\mathcal P_T(G_T)}w_P.
\]

Source deletion and retyping are local: deletion turns off the local potential integrand; retyping switches it to the new type potential. Idempotent incoming typed merges introduce no extra sign and only split the potential integral at a measure-zero boundary time.

## 3. Exact semigroup representation

The representation retains Assignment 002's cemetery correction. Bare conditional factorization is still false and is not used.

Let

\[
\nu_T(dg)=P(G_T\in dg,\tau_\dagger>T)
=\prod_PP_P(Con(P))m_T(dg).
\]

Then

\[
P_TH_{\xi_0}(\eta)
=
\int\prod_PE_P[w_P1_{Con(P)}]m_T(dg)
=
\int\prod_PC_P(\eta)\nu_T(dg).
\]

Equivalently use the killed successful skeleton with one cemetery atom assigned contribution zero.

## 4. Bulk/end separation

For bulk patches,

\[
C(P)=E_P^{con}[A_P]
\]

is independent of terminal physical data. It depends only on the source site, interval length, typed boundary labels/orientations, and local dual coefficients/rates/potentials.

For an end patch on site `i`,

\[
C_T(x,P)
=B_0(P)+\sum_{a\in E_*}B_a(P)1_{\{x=a\}},
\]

where

\[
B_a(P)=E_P^{con}[A_P1_{\{X_T^P=a\}}].
\]

Thus all terminal physical dependence is one-site and lies in the same reference-state indicator basis used to construct the dual.

This is the exact structural prerequisite for a meaningful bulk patch-positivity condition.

## 5. Binary specialization

At `d=2`:

- source outcome `0` is death/split and outcome `1` is birth/survival;
- the selected outgoing sign is the canonical patch initial sign;
- effective empty-target deaths have positive sign;
- `v_{i,1}` is exactly the canonical `V_i`;
- the end factor is `eta_i^{X_T}`;
- typed target conflicts are impossible, so `nu_T` is the ordinary successful-skeleton law.

The resulting formula is mathematically the paper's patch representation.

## 6. Finite gate

The mandatory `d=3` verifier uses the same two-record geometry as Assignment 002. It represents a Feynman--Kac exponential exactly by its rational exponent rather than evaluating it.

The gate includes:

- 32 hidden configurations;
- 8 incoming typed conflicts;
- two terminal physical configurations;
- direct pathwise identities on all exact-two-record noncemetery cases;
- killed weighted identities on all hidden/terminal cells;
- sign-ledger checks;
- exact type-dependent potential segmentation;
- bulk/end locality checks;
- a separate binary reduction.

## 7. Next edge

The representation layer is now complete enough to ask the principal's positivity question without ambiguity:

> For which finite-state single-site replacement generators are all bulk typed patch contributions
> \[
> C(P)=E_P^{con}[A_P]
> \]
> nonnegative for every finite typed patch shape and boundary label?

The next block should first derive a finite-dimensional transfer-matrix formula for `C(P)` and determine whether all-patch nonnegativity has a tractable coefficient-level characterization or useful sufficient cone.

Do **not** jump directly to applications before understanding this positivity object.

## Novelty and scope

No novelty claim is made yet. Literature comparison should occur after the generalized representation and positivity statement are stable enough to identify the actual theorem class.

The proved scope remains finite-state bounded finite-range **single-site replacement** dynamics. Simultaneous multi-site updates remain downstream.

No writes to `main`; branch-only wiki policy is unchanged.