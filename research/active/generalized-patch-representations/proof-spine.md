# Proof spine: generalized patch representations

Date: 2026-08-17

## Target

Extend the patch representation / patch positivity mechanism beyond binary flip spin systems while preserving:

1. a tensor basis of local observables;
2. an exact signed Feynman--Kac dual;
3. a graphical interaction process with a coarser successful-interaction skeleton;
4. conditional/weighted factorization into spacetime patches;
5. explicit patch contributions;
6. a local nonnegativity criterion on bulk patch contributions;
7. comparison/convergence consequences and concrete applications.

## E0. Binary benchmark

**Settled by the canonical paper.**

Binary monomials yield the signed death/split/birth set process. The successful skeleton records source/time/target but hides split versus birth. Conditioning on that skeleton yields independent one-site patch laws and an exact patch representation.

## E1. Canonical finite-state tensor basis

**Settled in Assignment 001.**

For `E={0,...,d-1}` with reference state `0`, use

\[
h_0\equiv1,
\qquad h_a(x)=1_{\{x=a\}},\quad a\ne0.
\]

Tensor observables are indexed by finite typed partial maps. Compatible overlaps merge; conflicting labels give cemetery `dagger` with zero duality function.

## E2. Exact signed local dual

**Settled in Assignment 001.**

For general bounded single-site replacement rates, expansion in the typed tensor basis gives fixed local branch coefficients `a_{i,r}^s(tau)`. Absolute values are local Poisson rates; signs are sign marks. Source outcome `s=0` deletes, `s=r` preserves, and other `s` retype the source. Target conflicts change only the deterministic result, never the clock rate.

The empty-target source-survival coefficient is diagonal and enters the additive Feynman--Kac potential. The `d=2` specialization is exactly the paper's death/split/birth dual.

## E3. Typed successful record

**Settled in Assignment 001.**

For nonempty target, superpose source-outcome clocks at fixed `(i,r,tau)` and record

\[
(i,t,r,\tau).
\]

The record reveals the pre-source type and typed target but hides post-source outcome `s`. All hidden outcomes have the same source/target endpoints.

## E4. Typed patch factorization

**Settled in Assignment 002, with a necessary killed-skeleton modification.**

The local patch state is `X^P in E`. Noncemetery consistency consists of:

- no interior unrecorded matching nonempty-target clock;
- correct revealed source type at an outgoing terminal;
- incoming compatibility
  \[
  X_{e-}^P\in\{0,a\}
  \]
  for incoming target type `a`.

Bare conditioning on the record list does not factor in general. A selected incoming target can conflict after the record is selected, hit cemetery, and simultaneously remove all future no-record constraints. The exact `d=3` gate gives

\[
P(K,B\mid G)=4/17\ne32/289=P(K\mid G)P(B\mid G).
\]

Because `H_dagger=0`, the representation-sufficient identity is instead

\[
E\left[h(G_T)1_{\{\tau_\dagger>T\}}\prod_Pf_P\right]
=
\int h(g)\prod_PE_P[f_P1_{Con(P)}]m_T(dg).
\]

Thus

\[
\nu_T(dg)=P(G_T\in dg,\tau_\dagger>T)
=
\prod_PP_P(Con(P))m_T(dg),
\]

and patch variables are conditionally independent given an ordinary value of the killed/noncemetery skeleton.

## E5. Explicit typed patch representation

**Settled in Assignment 003.**

For each patch define

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

where `bar v_{i,0}=0`. Then

\[
w_P=
\begin{cases}
A_P,&P\text{ bulk},\\
A_Ph_{X_T^P}(\eta_{i(P)}),&P\text{ end}.
\end{cases}
\]

On every noncemetery realization,

\[
\boxed{
\sigma_Te^{\int_0^TV(\xi_u)du}H_{\xi_T}(\eta)
=
\prod_Pw_P.}
\]

Applying the killed weighted factorization gives

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int
\left(\prod_{P\in\mathcal B_T(g)}C(P)\right)
\left(\prod_{P\in\mathcal E_T(g)}C_T(\eta_{i(P)},P)\right)
\nu_T(dg),}
\]

with

\[
C(P)=E_P^{con}[A_P]
\]

for bulk patches and

\[
C_T(x,P)
=B_0(P)+\sum_{a\in E_*}B_a(P)1_{\{x=a\}}
\]

for end patches.

Thus bulk contributions are independent of terminal physical data; end contributions are one-site functions in the same indicator basis.

The `d=2` specialization is exactly the canonical binary patch representation. In the binary case typed conflicts are impossible, so the killed skeleton reduces to the ordinary successful skeleton.

Decisive files: `003a`, `003b`, `003c`, `003d`, and `003-typed-representation-verifier.py`.

## E6. Generalized typed patch positivity

**Open and current load-bearing edge.**

The positivity object is now precise:

\[
\boxed{C(P)=E_P^{con}[A_P].}
\]

Question:

> For which finite-state single-site replacement coefficients is
> \[
> C(P)\ge0
> \]
> for every finite bulk typed patch shape and typed boundary label?

The first subproblem is to eliminate the path-space notation and write `C(P)` as a finite-dimensional transfer-matrix / killed-CTMC expression on local type space `E` for every boundary orientation.

That formula should expose:

1. how the hidden outgoing source-outcome distribution enters the initial vector;
2. how effective empty-target signed transitions and the local potential enter the interior semigroup;
3. how suppression of matching nonempty-target clocks enters the killing rates;
4. how incoming-terminal compatibility or outgoing-terminal source type enters the terminal functional.

Only after this exact matrix representation is derived should the programme search for coefficient-level necessary/sufficient inequalities or a useful sufficient cone.

The binary specialization must recover the paper's patch-positivity inequalities, not merely some stronger unrelated sufficient condition.

## E7. Consequences and applications

**Blocked on E6 except for reconnaissance.**

After a useful positivity condition exists, determine what order-preservation/comparison/convergence statements survive in the multi-state setting and identify genuinely non-binary models satisfying the condition.

Simultaneous multi-site physical updates remain outside the proved class and should be reconsidered only after the single-site theory reveals which algebraic interfaces are essential.

## Novelty status

No literature novelty claim has yet been made for the generalized representation theorem. A targeted literature audit should occur once the positivity theorem is stable enough to define the actual contribution precisely.