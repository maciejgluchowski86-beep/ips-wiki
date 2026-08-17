# Assignment 003: explicit typed patch representation

Date: 2026-08-17

Status: **queued, not yet executed**.

Assignment 002 ended `CONTINUE-TYPED-REPRESENTATION`. This assignment is written durably before any execution because the Professor remains the only operational session.

## Goal

Prove the exact finite-horizon patch representation for the finite-state typed dual, using the killed/noncemetery factorization from Assignment 002.

Do **not** define generalized patch positivity in this block. The output must first be an explicit local contribution formula and exact semigroup representation.

## Fixed input

For finite-state bounded finite-range single-site replacement dynamics:

- typed active configurations are finite partial maps into `E_*`;
- `H_dagger=0`;
- the signed local branch coefficients are `a_{i,r}^s(tau)`;
- the additive potential is
  \[
  V(\xi)=\sum_{i\in\operatorname{supp}\xi}v_{i,\xi(i)};
  \]
- successful nonempty-target records are `(i,t,r,tau)` and hide source outcome `s`;
- on an inserted record list `g`,
  \[
  1_{\{\tau_\dagger>T\}}1_{\{G_T=g\}}
  =\prod_P1_{Con(P)};
  \]
- the weighted Mecke theorem is
  \[
  E[h(G_T)1_{\{\tau_\dagger>T\}}\prod_Pf_P]
  =\int h(g)\prod_PE_P[f_P1_{Con(P)}]m_T(dg).
  \]

Bare conditional factorization given only `G_T` is false and must not be silently restored.

## Part A. Define the local patch weight

For every typed patch `P`, define a local multiplicative weight `w_P` containing exactly the global Feynman--Kac data belonging to its source-time strip.

At minimum account for:

1. **outgoing initial boundary sign:** if `P` starts at a selected outgoing record, include the sign of its hidden source-outcome branch;
2. **effective empty-target interior signs:** multiply the sign of every empty-target jump whose source type matches the current local state and therefore actually acts;
3. **local potential:** include
   \[
   \exp\left(\int_{s(P)}^{e(P)\wedge T}
   1_{\{X_u^P\ne0\}}v_{i(P),X_u^P}\,du\right);
   \]
4. **terminal physical factor:** for an end patch truncated at `T`, include
   \[
   h_{X_T^P}(\eta_{i(P)}),
   \qquad h_0\equiv1,
   \]
   and include no terminal physical factor for a bulk patch.

Prove that no sign or potential contribution is counted twice or omitted at shared patch boundaries.

## Part B. Pathwise product identity

On every noncemetery realization through `T`, prove exactly

\[
\boxed{
\sigma_T
\exp\left(\int_0^TV(\xi_u)\,du\right)
H_{\xi_T}(\eta)
=
\prod_{P\in\mathcal P_T(G_T)}w_P(\Sigma_P;\eta).}
\]

This must be a pathwise identity before taking conditional expectations.

Pay particular attention to:

- selected nonempty-target signs: they belong to the outgoing-start source patch only;
- incoming boundaries: they reset/merge the local type but carry no duplicated branch sign;
- an idempotent incoming merge into an already equal type;
- a source deletion `s=0`, after which the potential contribution from that source line stops until reactivation;
- source retyping `s notin {0,r}`;
- empty-target retyping/deletion signs;
- end patches with local state `0`, whose terminal factor is `1`.

## Part C. Exact semigroup representation

Combine the pathwise identity with Assignment 002 to prove

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int
\prod_{P\in\mathcal P_T(g)}
E_P\left[w_P(\Sigma_P;\eta)1_{Con(P)}\right]
\,m_T(dg).}
\]

Equivalently, with the noncemetery skeleton submeasure

\[
\nu_T(dg)=\prod_PP_P(Con(P))m_T(dg),
\]

define

\[
C_P(\eta)=E_P^{con}[w_P(\Sigma_P;\eta)]
\]

and prove

\[
\boxed{
P_TH_{\xi_0}(\eta)
=
\int\prod_PC_P(\eta)\,\nu_T(dg).}
\]

State the equivalent killed-skeleton expectation with one cemetery atom of contribution zero if useful.

## Part D. Bulk/end separation

Prove that for a bulk patch the contribution depends only on:

- its source site and interval length;
- initial/terminal orientation and typed boundary labels;
- the local dual coefficients/rates;

and **not** on the physical terminal configuration `eta`.

End patch contributions may depend on `eta_i` only through the one-site factor `h_{X_T^P}(eta_i)` inside the consistent expectation.

This separation is the prerequisite for a meaningful later definition of typed patch positivity.

## Part E. Binary specialization

For `d=2`, reduce the local weight and representation to the canonical paper's patch contribution architecture:

- source outcome `0` is split/death and source outcome `1` is birth/survival;
- selected outgoing sign is the binary initial-boundary sign;
- effective empty-target jumps are binary deaths;
- the additive potential is the binary patch potential;
- the end factor is the binary monomial factor.

Exact equality of notation is not required, but the mathematical weight must be the same after the obvious suppression of the unique active type.

## Mandatory finite verifier

Use the same `d=3` two-record geometry as Assignment 002, including the incoming target-conflict configuration.

Assign explicit exact rational branch signs and local potential values. Enumerate every hidden configuration used by the gate and check:

1. on each noncemetery configuration, the direct global Feynman--Kac weight equals the product of local patch weights;
2. on each cemetery configuration, the global duality weight is zero;
3. selected outgoing signs appear exactly once;
4. an effective empty-target retyping sign appears exactly once;
5. source deletion/retyping changes the local potential integral on exactly the correct time interval;
6. the product representation remains correct for at least two physical terminal configurations `eta`;
7. the `d=2` specialization passes a separate exact check.

Exact rational arithmetic only; no Monte Carlo.

## Pre-registered outcomes

Return exactly one.

### `CONTINUE-TYPED-POSITIVITY`

The pathwise local-weight identity, exact semigroup representation, bulk/end separation, mandatory finite verifier, and binary specialization all pass. State the precise next question: characterize nonnegative **bulk** typed patch contributions.

### `STOP-NONLOCAL-FK-WEIGHT`

Some sign or potential contribution cannot be assigned to a unique one-site patch without retaining cross-patch hidden information, and the mandatory finite gate gives an exact counterexample. Stop before positivity.

### `STOP-NO-BULK-END-SEPARATION`

The exact representation exists, but a bulk contribution necessarily depends on terminal physical data or another nonlocal/end variable, so patch positivity cannot be a local bulk condition in the intended sense. Give the smallest exact obstruction and stop.

### `UNRESOLVED-BOUNDED`

The finite verifier passes but the general pathwise/Mecke representation has one precise unresolved interface. Record it and do not define positivity.

## Anti-loop rules

Do not:

- alter the tensor basis;
- replace the killed skeleton by the false bare conditional factorization;
- absorb cross-patch terms into a definition of `C_P` without a pathwise product identity;
- define positivity before bulk/end separation is proved;
- enlarge to simultaneous multi-site physical updates;
- make a novelty claim before later literature audit.

## Durability

Commit immediately after:

- local weight definition;
- mandatory finite verifier;
- pathwise product theorem;
- semigroup representation;
- binary reduction/bulk-end separation.

Final report:

`students/professor/003-typed-patch-representation.md`.

Final handoff:

`students/professor/003-handoff.md`.

No writes to `main`.
