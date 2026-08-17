# Assignment 002: typed successful-skeleton factorization

Date: 2026-08-17

Status: **queued, not yet executed**.

This assignment follows Assignment 001, which ended `CONTINUE-TYPED-PATCH`. It is written durably before execution because the Professor is currently the only operational research session.

## Goal

Decide whether the typed successful-interaction record from Assignment 001 yields a genuine patchwise conditional factorization analogous to the binary theorem.

Do **not** define generalized patch positivity in this block. The only target is the factorization/representation layer.

## Fixed input from Assignment 001

Finite local state space

\[
E=\{0,1,\ldots,d-1\},
\qquad E_*=E\setminus\{0\}.
\]

Typed active configurations are finite partial maps into `E_*`; conflicts go to cemetery `dagger` with duality function zero.

For active source type `r`, typed target `tau`, and source outcome `s in E`, the signed local branch coefficient is `a_{i,r}^s(tau)` and the branch rate is its absolute value.

For nonempty target, the proposed successful record is

\[
(i,t,r,\tau),
\]

which reveals the pre-interaction source type and typed target but hides the post-interaction source outcome `s`.

## Part A. Define typed patch boundaries and local state

Using the realized successful records, retain the same one-site vertical patch geometry as the binary paper.

Every target occurrence `j in supp tau` gives an incoming boundary at `j` carrying the type `tau(j)`.

Every source record gives an outgoing boundary at `i` carrying at least the pre-source type `r` and the typed target `tau` needed for the hidden-branch law.

Define the local patch state

\[
X_u^P\in E,
\]

where `0` means dual-inactive and `a in E_*` means active with type `a`.

Specify exact initial and terminal data for all four finite boundary orientations and end patches.

## Part B. Reference patch law

For a patch on source line `i`, the interior mark space contains all fixed local clocks `(r,s,tau)` outgoing from `i` during the patch interval.

At an outgoing initial boundary with record `(i,t,r,tau)`, sample the hidden source outcome with law

\[
P(s=u\mid i,r,\tau)
=\frac{|a_{i,r}^{u}(\tau)|}{\sum_v|a_{i,r}^{v}(\tau)|}.
\]

At an incoming initial boundary carrying type `a`, set the local post-boundary state to `a`.

Read empty-target marks chronologically and let matching source-type marks update the local type. An unselected nonempty-target mark is allowed only when its source type does not match the current local type; otherwise it would be another successful record.

## Part C. Exact local consistency conditions

Test whether the global statement “the selected records are exactly the successful skeleton and the typed dual has not already hit cemetery” is equivalent to a product of one local consistency event per patch.

Candidate terminal conditions:

1. outgoing terminal record with source type `r'`: require `X_{e-}^P=r'`;
2. incoming terminal record carrying target type `a`: require
   \[
   X_{e-}^P\in\{0,a\};
   \]
   a different active type is a conflict;
3. end terminal: no extra boundary condition.

After a compatible incoming record, the next patch starts at type `a` whether the previous local state was `0` or already `a`.

The load-bearing question is the cemetery case. A conflicting incoming target kills the **global** dual and suppresses all future records. Decide whether:

- such histories can be removed from the semigroup representation because their duality function is zero, leaving a factorization on noncemetery skeletons; or
- cemetery/no-future-record information couples otherwise disjoint patches and prevents the required factorization.

This must be proved, not described.

## Part D. Mecke/Radon--Nikodym proof or exact obstruction

If the local consistency equivalence holds, reproduce the binary factorization proof with the typed record intensity

\[
\Lambda_{i,r}(\tau)=\sum_s|a_{i,r}^{s}(\tau)|.
\]

Show explicitly that, conditional on a finite noncemetery typed skeleton, the hidden patch marks are independent with the corresponding consistent patch laws.

If full conditional-law factorization fails on cemetery skeletons but every such skeleton has zero Feynman--Kac contribution, state and prove the weaker **weighted factorization** actually sufficient for the semigroup representation.

If neither works, isolate the first finite counterexample.

## Mandatory finite gate

Before attempting the general Mecke argument, use a `d=3` two-site or three-site example with two consecutive selected records and enumerate all local hidden source outcomes/empty-target marks needed to test the consistency decomposition.

The gate must include at least one incoming target conflict case.

The finite calculation must distinguish:

- full conditional factorization;
- factorization only after multiplying by the zero/cemetery weight;
- genuine cross-patch dependence that survives in the weighted representation.

Exact arithmetic only; no Monte Carlo.

## Pre-registered outcomes

Return exactly one.

### `CONTINUE-TYPED-REPRESENTATION`

A full or representation-sufficient weighted patch factorization is proved, with the `d=3` finite gate passing. State the exact generalized patch representation theorem that should be proved next. Do not yet formulate positivity inequalities.

### `STOP-TYPED-CONFLICT-COUPLING`

A finite typed target-conflict pattern creates cross-patch dependence that survives even after zero/cemetery weighting, so the one-site patch factorization fails for the canonical indicator basis. Give the smallest exact counterexample and stop before trying another basis or larger patch geometry.

### `STOP-NO-LOCAL-CONSISTENCY`

Even without target conflict, the event that the selected typed records are exactly the successful skeleton cannot be written as a product of one source--time-strip consistency event per patch. Give the smallest exact obstruction and stop.

### `UNRESOLVED-BOUNDED`

The finite gate works but the general conditional/weighted Mecke step remains unproved for a precise reason. Record the missing lemma and do not move to positivity.

## Anti-loop rules

Do not:

- change the tensor basis;
- enlarge patches to multi-site spacetime cells merely to rescue a failed one-site factorization;
- ignore cemetery paths without proving their weighted contribution is zero in the exact representation;
- define patch positivity before factorization;
- infer independence from disjoint Poisson strips without checking the conditioning event;
- enlarge beyond the mandatory finite gate if it already produces a stop outcome.

## Durability

Commit immediately after:

- typed patch-boundary/local-state definition;
- finite conflict/factorization verifier;
- local consistency equivalence or counterexample;
- Mecke/Radon--Nikodym factorization theorem;
- weighted-factorization repair if full factorization fails.

Final report:

`students/professor/002-typed-patch-factorization.md`.

Final handoff:

`students/professor/002-handoff.md`.

No writes to `main`.
