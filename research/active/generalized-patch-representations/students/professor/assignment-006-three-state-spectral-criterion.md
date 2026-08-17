# Assignment 006: exact three-state spectral critical-point criterion

Date: 2026-08-17

Status: **queued, not yet executed**.

Assignment 005 ended `STOP-NO-FINITE-ENDPOINT-CRITERION`: zero-length and long-time coefficient inequalities do not control the two-mode `OI` transient in boundary-complete `d=3`. This assignment does **not** reopen that stopped endpoint route. It asks whether retaining the unique possible interior critical point yields an exact finite spectral criterion.

Applications and convergence remain out of scope.

## Goal

For boundary-complete `d=3`, derive a necessary-and-sufficient finite test for typed bulk patch positivity in terms of:

1. the Metzler/zero-length conditions already proved in Assignment 005;
2. long-time limits of the remaining `OI` numerators;
3. the exact value at the possible interior minimum of each two-mode numerator.

Decide whether this is a genuinely tractable criterion or merely a restatement of the semigroup definition.

## Fixed input

Under boundary completeness, Assignment 005 proved:

- `K` is Metzler;
- all incoming-initial `II/IO` families are automatic;
- for every outgoing row `p=(p0,p1,p2)`, zero-length conditions force
  \[
  p_1,p_2,p_0+p_1,p_0+p_2\ge0;
  \]
- all `OO` families are then automatic;
- only `OI` remains, with
  \[
  p e^{tK}f_b^I=E_b[g(Z_t)],
  \qquad
  g=(p_0,p_0+p_1,p_0+p_2).
  \]

The active `2 x 2` block of `K` has real nonpositive eigenvalues.

## Part A. Generic distinct-eigenvalue formula

Assume first that the two nonzero eigenvalues are

\[
-\mu,
\qquad
-\nu,
\qquad
0<\mu<\nu.
\]

For every remaining `OI` descriptor prove

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t}.
\]

Express `L,A,B` explicitly from `K`, the outgoing row `p`, and incoming terminal type `b`, without diagonalizing numerically.

## Part B. Exact interior-minimum criterion

Classify the sign of

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t}
\]

on `t>=0`.

Prove exactly that an interior minimum can occur only in the appropriate opposite-sign coefficient regime, derive its location from

\[
N'(t)=0,
\]

and write the minimum value as an explicit expression in `L,A,B,mu,nu`.

The criterion must be necessary and sufficient, not a sufficient cone.

## Part C. Degenerate spectral cases

Handle separately and exactly:

1. one active eigenvalue equal to zero;
2. repeated nonzero eigenvalue with diagonalizable active block;
3. repeated nonzero eigenvalue with a Jordan block, where the form may be
   \[
   L+(A+Bt)e^{-\mu t};
   \]
4. reducible reference-neighbour physical chains.

Do not silently impose irreducibility unless it is proved to follow from the boundary-complete hypothesis.

## Part D. Coefficient-level usability

Determine whether the resulting finite test can be evaluated from local physical rates and nonempty-target coefficient rows by a bounded amount of exact algebra.

Distinguish:

- a genuinely finite spectral criterion;
- an expression requiring unresolved transcendental sign comparison;
- a criterion so close to scanning all `t` that it has no practical mathematical gain over the semigroup definition.

## Part E. Exact binary reduction

Suppress type `2`.

The interior-critical condition must disappear because there is only one decaying mode, and the test must reduce exactly to

\[
c^0(S)+c^1(S)\le0,
\qquad
c^1(\emptyset)c^0(S)
\ge c^0(\emptyset)c^1(S),
\]

with the canonical degenerate clause.

No stronger binary condition is acceptable.

## Mandatory exact gate

Use both:

1. the Assignment-005 obstruction, for which the criterion must detect the exact negative minimum
   \[
   e^{-t_*}=13/153,
   \qquad N(t_*)=-1/1224;
   \]
2. at least one physically realizable boundary-complete `d=3` example with `p0<0` for which the endpoint conditions hold and the spectral test proves all relevant `OI` numerators nonnegative for every time.

No floating-point sign decisions and no Monte Carlo.

## Pre-registered outcomes

Return exactly one.

### `CONTINUE-EXACT-THREE-STATE-SPECTRAL-CRITERION`

A finite necessary-and-sufficient spectral criterion is proved for boundary-complete `d=3`, including all degenerate cases, exact binary reduction, and both mandatory gates. State the next question: whether this criterion has a natural coefficient simplification or structural subclass worth pursuing. Do not start applications.

### `STOP-SPECTRAL-CRITERION-NOT-FINITE`

The remaining sign test cannot be reduced to finitely many exact endpoint/critical-point evaluations because a degenerate or realizable case retains genuinely more complicated time dependence. Give the smallest exact obstruction.

### `STOP-SPECTRAL-CRITERION-NOT-TRACTABLE`

A formally finite critical-point expression exists but requires an unresolved/nonalgebraic sign comparison that is not materially more usable than the original all-time semigroup definition. Record the exact expression and why it fails the tractability target.

### `UNRESOLVED-THREE-STATE-SPECTRAL`

The generic case is settled but one named degenerate case remains unresolved. Do not enlarge to `d>3` or applications.

## Anti-loop rules

Do not:

- revive the endpoint-only criterion refuted in Assignment 005;
- replace the exact critical-value condition by entrywise nonnegativity or another stronger cone;
- assume irreducibility without proof;
- use numerical plots for sign certification;
- weaken the binary equivalence test;
- move to applications, convergence, or `d>3` in this block.

## Durability

Commit immediately after:

- generic two-mode criterion;
- each genuinely distinct degenerate spectral case;
- mandatory exact verifier;
- binary reduction;
- final tractability ruling.

Final report:

`students/professor/006-three-state-spectral-criterion.md`.

Final handoff:

`students/professor/006-handoff.md`.

No writes to `main`.
