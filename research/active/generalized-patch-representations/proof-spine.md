# Proof spine: generalized patch representations

Date: 2026-08-17

## Target

Extend the patch representation / patch positivity mechanism beyond binary flip spin systems while preserving:

1. a tensor basis of local observables;
2. an exact signed Feynman--Kac dual;
3. a graphical process with a coarser successful-interaction skeleton;
4. conditional/weighted factorization into spacetime patches;
5. explicit patch contributions;
6. an exact local bulk nonnegativity property;
7. tractable coefficient criteria and then applications/consequences.

## E0. Binary benchmark

**Settled by the canonical paper.**

## E1. Canonical finite-state tensor basis

**Settled in Assignment 001.**

For finite `E={0,...,d-1}` with reference state `0`, use

\[
h_0\equiv1,
\qquad h_a(x)=1_{\{x=a\}},\quad a\ne0.
\]

Tensor observables are indexed by finite typed partial maps; conflicting labels give cemetery `dagger` with zero duality function.

## E2. Exact signed local dual

**Settled in Assignment 001.**

General bounded finite-range single-site replacement rates yield fixed local signed branch coefficients `a_{i,r}^s(tau)`. Absolute values are Poisson rates, signs are marks, source outcome deletes/preserves/retypes the source, and target conflicts only affect the deterministic merge.

The empty-target source-survival coefficient is diagonal and enters the Feynman--Kac potential. The binary specialization is exactly death/split/birth.

## E3. Typed successful record

**Settled in Assignment 001.**

For nonempty target, record

\[
(i,t,r,\tau)
\]

and hide post-source outcome `s`.

## E4. Typed patch factorization

**Settled in Assignment 002 with a necessary killed-skeleton modification.**

Bare conditioning on the coarse record list fails because an incoming typed conflict can send the dual to cemetery and remove all future no-record constraints. The exact finite gate gives

\[
P(K,B\mid G)=4/17\ne32/289=P(K\mid G)P(B\mid G).
\]

Since `H_dagger=0`, the exact replacement is the killed/noncemetery factorization

\[
E\left[h(G_T)1_{\{\tau_\dagger>T\}}\prod_Pf_P\right]
=
\int h(g)\prod_PE_P[f_P1_{Con(P)}]m_T(dg).
\]

## E5. Explicit typed patch representation

**Settled in Assignment 003.**

For each patch,

\[
A_P
=
\epsilon_{\rm out}(P)\epsilon_{\emptyset}(P)
\exp\left(\int\bar v_{i(P),X_u^P}\,du\right).
\]

Bulk contributions are

\[
C(P)=E_P^{con}[A_P],
\]

and end contributions are one-site functions in the same indicator basis. The exact semigroup representation is

\[
P_TH_{\xi_0}(\eta)
=
\int
\prod_{P\in\mathcal B_T}C(P)
\prod_{P\in\mathcal E_T}C_T(\eta_{i(P)},P)
\,\nu_T(dg).
\]

The binary specialization is exact.

## E6. Exact typed bulk patch positivity

**Settled in Assignment 004 at the transfer-matrix level.**

For active local type `r`, define

\[
\rho_{i,r}=\sum_{s\ne r}|a_{i,r}^s(\emptyset)|,
\qquad
\kappa_{i,r}=\sum_{\tau\ne\emptyset}\sum_s|a_{i,r}^s(\tau)|.
\]

The weighted killed Feynman--Kac transfer has generator

\[
\boxed{K_i(0,\cdot)=0,
\qquad K_i(r,s)=a_{i,r}^s(\emptyset).}
\]

The cancellation producing this matrix is exact: empty-target escape subtraction and nonempty-target no-success killing cancel against the corresponding pieces of the local potential.

The unsigned consistency transfer is

\[
B_i(r,s)=|a_{i,r}^s(\emptyset)|\quad(s\ne r),
\]

\[
B_i(r,r)=
-\sum_{s\ne r}|a_{i,r}^s(\emptyset)|-\kappa_{i,r},
\]

with zero inactive row.

For terminal columns

\[
f_b^I=e_0^T+e_b^T,
\qquad
f_r^O=e_r^T,
\]

and outgoing initial signed row

\[
\mathbf a_{r,\tau}=(a_{i,r}^s(\tau))_{s\in E},
\]

the four bulk contributions are ratios of the following signed numerators by positive killed-reference denominators:

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

Therefore **typed bulk patch positivity** is exactly nonnegativity of these four numerator families for every realizable descriptor and every `t>0`.

This is not replaced by entrywise nonnegativity of `K_i`.

### Binary benchmark

For `d=2`, the four transfer formulas reduce exactly to the canonical full-patch formulas. All-length positivity is equivalent to

\[
c_i^0(S)+c_i^1(S)\le0,
\]

\[
c_i^1(\emptyset)c_i^0(S)
\ge
c_i^0(\emptyset)c_i^1(S)
\]

when `c_i^0(emptyset)+c_i^1(emptyset)>0`, and to `c_i\equiv0` in the degenerate case. Thus the generalized property exactly recovers the paper's patch positivity criterion.

### New multi-state necessary constraints

Short-time expansions force, on realizable descriptors,

\[
a_{i,a}^{r}(\emptyset)\ge0
\quad(a\ne r)
\]

from `IO` patches and

\[
a_{i,r}^{r_e}(\tau)\ge0
\]

from zero-length `OO` limits, with further derivative constraints recorded in `004d-small-time-necessary-conditions.md`.

Decisive files: `004a`--`004e`, final verifier `004-typed-transfer-verifier.py` at `0bbfccd0`, and Meeting 004.

## E7. Tractable coefficient characterization

**Open and current load-bearing edge.**

The exact all-length positivity property is now known, but it is an infinite semigroup family. The next bounded problem is:

> characterize this family by tractable local coefficient inequalities for a nontrivial multi-state class, or determine precisely why no finite binary-style coefficient criterion exists without additional structure.

Acceptable progress includes:

- an exact finite coefficient criterion for a natural class of `K_i` / boundary vectors;
- a necessary-and-sufficient spectral or cone criterion that is genuinely checkable;
- a sharp obstruction showing that arbitrary `d>=3` positivity cannot collapse to finitely many first-order inequalities;
- a natural structural subclass preserving exact binary equivalence and admitting a closed criterion.

Do not start applications or convergence before this edge is materially narrowed.

## E8. Consequences, applications, and broader updates

**Blocked on E7 except for reconnaissance.**

Only after a usable positivity criterion exists should the programme study order preservation, comparison, convergence, genuinely non-binary models, or simultaneous multi-site physical updates.

## Novelty status

No literature novelty claim has yet been made for the generalized representation/positivity theorem. A targeted literature audit remains necessary once the coefficient-level theorem is stable enough to compare precisely.
