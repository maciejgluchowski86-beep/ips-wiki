# Assignment 004: typed bulk transfer matrices and positivity target

Date: 2026-08-17

Status: **queued, not yet executed**.

Assignment 003 ended `CONTINUE-TYPED-POSITIVITY`. This assignment is written durably before execution because the Professor remains the only operational research session.

## Goal

Eliminate the path-space notation from the bulk contribution

\[
C(P)=E_P^{con}[A_P]
\]

and derive an exact finite-dimensional transfer-matrix formula for every typed bulk boundary orientation.

Then determine the mathematically correct first notion of **typed patch positivity**: a condition equivalent to, or usefully sufficient for,

\[
C(P)\ge0
\]

for every finite bulk typed patch.

Do not move to applications or convergence consequences in this block.

## Fixed input

For a source site `i`, local state space is

\[
E=\{0,1,\ldots,d-1\},
\]

with `0` dual-inactive.

The exact intrinsic bulk weight is

\[
A_P
=
\epsilon_{\rm out}(P)
\epsilon_{\emptyset}(P)
\exp\left(
\int_{b(P)}^{e(P)}
\bar v_{i,X_u^P}\,du
\right).
\]

Interior consistency forbids every nonempty-target clock whose source type matches the current local type. Empty-target clocks may act and can delete or retype the source.

Bulk terminal consistency is either:

- outgoing: `X_{e-}=r_e`;
- incoming: `X_{e-} in {0,a_e}`.

Initial state is either:

- incoming: deterministic type `a`;
- outgoing record `(i,b,r,tau)`: hidden outcome `s` with probability
  \[
  q_{i,r,\tau}(s)=|a_{i,r}^s(\tau)|/\Lambda_{i,r}(\tau),
  \]
  while the intrinsic weight contains its sign.

## Part A. Derive the unnormalized signed interior transfer

For each source site `i`, construct the finite linear operator on functions/vectors over `E` which represents

\[
E_x\left[
\epsilon_{\emptyset}
\exp\left(\int_0^t\bar v_{i,X_u}du\right)
1_{\{\text{no matching nonempty-target clock before }t\}}
F(X_t)
\right].
\]

Do this directly from the Poisson clocks.

The key candidate identity to **prove or refute** is that cancellation between

1. the reference empty-target jump-rate subtraction;
2. the no-success killing rate from nonempty-target clocks; and
3. the local potential `v_{i,r}`

reduces the signed transfer generator to the matrix of **empty-target signed coefficients** `a_{i,r}^s(emptyset)` (with the inactive row treated explicitly).

Do not assume this cancellation from heuristic generator bookkeeping.

## Part B. Derive the denominator transfer

The consistency probability

\[
P_P(Con(P))
\]

has no signs and no Feynman--Kac potential. Derive its finite killed-Markov transfer matrix explicitly.

Separate clearly:

- empty-target physical transition rates `|a_{i,r}^s(emptyset)|`;
- killing rate
  \[
  \kappa_{i,r}
  =\sum_{\tau\ne\emptyset}\Lambda_{i,r}(\tau)
  \]
  from matching nonempty-target clocks;
- inactive state `0`.

Prove the denominator is strictly positive exactly on the realizable bulk descriptors considered by the killed skeleton.

## Part C. Four boundary-orientation formulas

For each bulk orientation

\[
II,\ IO,\ OI,\ OO,
\]

write `C(P)` as an explicit ratio

\[
\frac{\text{signed initial vector}\;\times\;\text{signed transfer}\;\times\;\text{terminal functional}}
{\text{reference initial vector}\;\times\;\text{killed reference transfer}\;\times\;\text{same terminal consistency functional}}.
\]

The formulas must show exactly:

- incoming initial type `a`;
- outgoing hidden branch coefficients `a_{i,r}^s(tau)`;
- outgoing terminal source type `r_e`;
- incoming terminal compatibility set `{0,a_e}`.

Since the denominator is positive on a realized descriptor, identify the exact numerator inequalities equivalent to bulk patch nonnegativity.

## Part D. Small-time necessary conditions

Expand the numerator transfer at `t=0` and derive the first coefficient-level inequalities forced by all-patch nonnegativity.

At minimum determine:

- zero-length boundary limits;
- first derivative conditions for each orientation;
- whether retyping coefficients create sign constraints absent in the binary theory.

The purpose is to obtain falsifiable necessary conditions before searching for a large sufficient cone.

## Part E. Binary specialization

Set `d=2` and reduce the four transfer formulas to the canonical binary patch contribution formulas.

The block passes the binary benchmark only if the resulting all-length nonnegativity condition recovers the paper's patch-positivity inequalities, or if an exact proof is given that the transfer condition is equivalent to them.

A stronger condition which excludes binary patch-positive models is not an acceptable definition of the generalized property.

## Mandatory finite gate

Use `d=3` with one source site and at least two active types.

Construct exact rational local coefficient data containing:

- at least one nontrivial empty-target retyping coefficient;
- at least one negative signed coefficient;
- at least one nonempty-target coarse hazard;
- one incoming and one outgoing initial boundary type;
- both incoming and outgoing terminal functionals.

The verifier must compare, using exact arithmetic/symbolic algebra:

1. direct one-step/local generator expansion of the weighted killed process;
2. the proposed signed transfer generator;
3. the unsigned consistency/killing generator;
4. all four boundary-orientation numerator/denominator formulas at the generator or finite semigroup level;
5. the `d=2` reduction.

No Monte Carlo and no floating-point positivity decisions.

## Pre-registered outcomes

Return exactly one.

### `CONTINUE-TYPED-POSITIVITY-CRITERION`

The finite transfer formulas are proved, the mandatory gate passes, and bulk patch nonnegativity is reduced to an explicit family of finite-dimensional numerator inequalities with correct binary specialization. State the next bounded problem: characterize that semigroup-positive family by tractable coefficient inequalities or identify useful model classes satisfying it.

### `STOP-NO-LOCAL-TRANSFER`

The intrinsic bulk expectation cannot be represented by a fixed finite local transfer operator because some path information from nonempty-target marks or another patch is still required after conditioning. Give the smallest exact obstruction and stop.

### `STOP-BINARY-POSITIVITY-MISMATCH`

A local transfer formula exists, but the proposed generalized positivity family does not specialize to the canonical binary patch-positivity property and no exact equivalence repair is available inside the fixed representation. Give the mismatch and stop before applications.

### `UNRESOLVED-BOUNDED`

The finite gate and transfer derivation produce a genuine candidate but one precise interface remains unproved. Record it and do not move to applications or coefficient searches.

## Anti-loop rules

Do not:

- change the tensor basis;
- use bare skeleton conditioning instead of the killed/noncemetery construction;
- define positivity by an unrelated entrywise-nonnegative matrix condition unless it is proved equivalent to all bulk `C(P)>=0`;
- impose a sufficient cone before deriving the exact four boundary formulas and small-time necessary conditions;
- enlarge to simultaneous multi-site physical updates;
- search applications before the binary specialization is checked;
- make a novelty claim before the later literature audit.

## Durability

Commit immediately after:

- signed interior transfer derivation;
- unsigned consistency transfer derivation;
- exact four-orientation contribution formulas;
- mandatory finite verifier;
- small-time necessary conditions;
- binary equivalence or mismatch.

Final report:

`students/professor/004-typed-bulk-positivity-transfer.md`.

Final handoff:

`students/professor/004-handoff.md`.

No writes to `main`.