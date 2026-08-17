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

The empty-target source-survival coefficient is diagonal and enters the additive Feynman--Kac potential.

The `d=2` specialization is exactly the paper's death/split/birth dual.

## E3. Typed successful record

**Settled geometrically in Assignment 001.**

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

For an inserted candidate record list `g`,

\[
\{\tau_\dagger>T\}\cap\{G_T=g\}
=
\bigcap_PCon(P).
\]

### Bare conditioning obstruction

Unlike the binary case, conditioning only on `G_T=g` does not generally factor. A selected incoming target can conflict after the record is selected; cemetery then removes every future no-record constraint globally.

The exact `d=3` gate gives

\[
P(K,B\mid G)=4/17\ne32/289=P(K\mid G)P(B\mid G).
\]

This failure must remain visible in every later theorem statement.

### Representation-sufficient repair

Because `H_dagger=0`, cemetery paths have zero Feynman--Kac weight. The weighted Mecke theorem is

\[
E\left[h(G_T)1_{\{\tau_\dagger>T\}}\prod_Pf_P\right]
=
\int h(g)\prod_PE_P[f_P1_{Con(P)}]m_T(dg),
\]

with

\[
m_T(dg)=\prod_k\Lambda_{i_k,r_k}(\tau_k)dt_k.
\]

Thus

\[
\nu_T(dg):=P(G_T\in dg,\tau_\dagger>T)
=
\prod_PP_P(Con(P))m_T(dg),
\]

and conditional on `G_T=g, tau_dagger>T` the patch variables are independent with normalized consistent laws.

Equivalently use a killed skeleton which collapses all cemetery paths to one zero-weight atom.

Decisive files: `002a`, `002b`, `002c`, and `002-typed-factorization-verifier.py`.

## E5. Explicit typed patch representation

**Open and current load-bearing edge.**

On a noncemetery trajectory the global Feynman--Kac weight should factor over typed one-site patches because:

- the potential is additive over active typed sites;
- every effective empty-target sign belongs to one source strip;
- every selected outgoing hidden-branch sign belongs to its outgoing-start patch;
- the terminal tensor observable is a product of one-site factors carried by end patches.

For a patch `P`, the expected local weight should contain:

1. outgoing-start hidden-branch sign when applicable;
2. signs of effective empty-target interior marks;
3. local potential factor
   \[
   \exp\left(\int_{s(P)}^{e(P)\wedge T}
   1_{\{X_u^P\ne0\}}v_{i(P),X_u^P}\,du\right);
   \]
4. end factor `h_{X_T^P}(eta_i)` at the terminal horizon.

The target representation is

\[
P_TH_{\xi_0}(\eta)
=
\int\prod_PE_P[w_P1_{Con(P)}]m_T(dg)
=
\int\prod_PC_P(\eta)\,\nu_T(dg),
\]

with `C_P=E_P^con[w_P]`.

Bulk contributions must be independent of the terminal physical configuration; end contributions may depend on its one-site spin.

## E6. Generalized patch positivity

**Blocked on E5.**

Once the explicit bulk contribution is proved, determine what local coefficient condition ensures every bulk typed patch contribution is nonnegative. It must reduce exactly to the binary patch-positivity inequalities.

## E7. Applications and broader updates

**Blocked on E6 except for reconnaissance.**

Priority examples should genuinely require more than two local states or non-flip replacement dynamics. Simultaneous multi-site physical updates remain outside the proved class and should be treated only after the single-site theory is complete enough to show which algebraic features matter.
