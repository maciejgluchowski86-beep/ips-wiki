# Assignment 005: three-state typed positivity criterion

Date: 2026-08-17

Status: **queued, not yet executed**.

Assignment 004 ended `CONTINUE-TYPED-POSITIVITY-CRITERION`. This assignment is written durably before execution. Applications and convergence remain out of scope.

## Goal

Determine whether the exact all-length typed bulk patch-positivity condition from Assignment 004 admits a finite/local coefficient characterization already for `d=3`, under a natural boundary-completeness hypothesis.

If not, isolate the precise semigroup-level obstruction rather than replacing the exact property by an unrelated sufficient cone.

## Fixed input

For one site `i`, local type space is

\[
E=\{0,1,2\}.
\]

The signed interior transfer is

\[
K(0,\cdot)=0,
\qquad
K(r,s)=a_r^s(\emptyset),\quad r\in\{1,2\}.
\]

Typed bulk patch positivity is exact nonnegativity, on realizable descriptors and every `t>0`, of

\[
e_a e^{tK}f_b^I,
\qquad
e_a e^{tK}f_r^O,
\]

\[
\mathbf a_{r,\tau}e^{tK}f_b^I,
\qquad
\mathbf a_{r,\tau}e^{tK}f_{r_e}^O,
\]

where

\[
f_b^I=e_0^T+e_b^T,
\qquad
f_r^O=e_r^T.
\]

## Boundary-complete hypothesis

For this bounded block assume the local/global skeleton support is rich enough that:

1. both active types `1,2` can occur as outgoing terminal source types at site `i`;
2. both active types `1,2` can occur as incoming terminal target types at site `i`;
3. every nonzero nonempty-target hidden outcome at an outgoing initial record is represented by a realizable `OO` or `OI` descriptor.

This hypothesis is not asserted globally in the general theory. It is a controlled test class designed to eliminate vacuous missing-boundary cases.

## Part A. Consequences for the interior matrix

Use the Assignment-004 short-time conditions to prove or refute:

> Under boundary completeness, typed patch positivity forces every off-diagonal entry of `K` to be nonnegative.

Deletion entries `K(r,0)=a_r^0(emptyset)` are already nonnegative because they are constant physical rates. The new issue is active retyping `K(1,2),K(2,1)`.

If the claim holds, `K` is Metzler and `e^{tK}` is entrywise nonnegative. Prove this implication directly in the present finite matrix setting.

## Part B. Incoming patches

Assuming the conclusion of Part A, determine whether all incoming-initial numerator families become automatically nonnegative:

\[
e_a e^{tK}f_b^I,
\qquad
e_a e^{tK}f_r^O.
\]

If so, remove them from the remaining positivity problem with proof.

## Part C. Outgoing boundary rows

For every nonempty target row

\[
p=\mathbf a_{r,\tau}=(p_0,p_1,p_2),
\]

boundary completeness and zero-length `OO/OI` limits force some finite sign inequalities. Derive all of them exactly.

Then analyze the remaining all-time conditions

\[
p e^{tK}f_b^I\ge0,
\qquad
p e^{tK}f_r^O\ge0.
\]

The central question is whether these are equivalent to finitely many coefficient inequalities involving only `p` and entries/eigen-data of `K`, or whether positivity can change sign at an interior time in a way not controlled by zero/infinite-time limits.

## Part D. Exact three-state semigroup analysis

Exploit the special `3 x 3` structure with absorbing state `0`. Reduce the active block to a `2 x 2` matrix and derive explicit formulas for the relevant entries of `e^{tK}`.

Do not make floating-point sign decisions. Use exact symbolic algebra, discriminants/eigenvalues, or rational certificates as appropriate.

Determine whether every numerator is a combination of at most two exponentials with sign behavior controlled by endpoint data, or whether an interior-time minimum/zero can occur independently.

## Part E. Binary consistency check

Suppress type `2` and verify that the resulting criterion reduces to the exact binary coefficient inequalities already proved in Assignment 004. Do not introduce any stronger binary condition.

## Mandatory finite/symbolic gate

Construct exact rational `d=3` coefficient data satisfying:

- physical realizability at one-neighbour level;
- boundary completeness for the tested local descriptors;
- nonnegative active retyping entries if Part A proves they are necessary;
- at least one outgoing row with `p_0<0` but all zero-length required combinations nonnegative, so the all-time question is genuinely nontrivial.

Use exact arithmetic/symbolic algebra to determine the sign of every relevant numerator for all `t>=0` in the chosen example.

The gate must distinguish:

1. finite endpoint inequalities sufficient in the example;
2. an interior-time sign obstruction invisible at zero/infinite time;
3. an unresolved symbolic sign problem.

## Pre-registered outcomes

Return exactly one.

### `CONTINUE-FINITE-THREE-STATE-CRITERION`

A finite necessary-and-sufficient coefficient criterion is proved for the boundary-complete `d=3` class, with exact binary reduction and mandatory gate. State the criterion and the next question: whether it extends to arbitrary `d` or useful structural subclasses. Do not start applications.

### `STOP-NO-FINITE-ENDPOINT-CRITERION`

Produce an exact `d=3` counterexample showing that all natural zero-length and long-time coefficient inequalities hold while a required numerator becomes negative at an interior time. Record the smallest exact witness. The exact semigroup definition remains valid; what stops is a binary-style endpoint criterion.

### `UNRESOLVED-THREE-STATE-SYMBOLIC`

Parts A--C reduce the problem genuinely, but one explicit symbolic sign question remains unresolved. Record the exact polynomial/exponential inequality and do not enlarge to `d>3` or applications.

### `STOP-BOUNDARY-COMPLETE-CLASS-EMPTY`

The boundary-completeness assumptions plus physical realizability and the Assignment-004 necessary conditions force the tested class to collapse to a trivial/binary-reducible system. Give the exact proof and stop this characterization route.

## Anti-loop rules

Do not:

- replace exact typed patch positivity by entrywise nonnegativity unless equivalence is proved in this class;
- search applications or convergence;
- enlarge to `d>3` before the three-state sign structure is settled;
- use numerical plotting as a sign proof;
- weaken the binary acceptance test;
- treat missing boundary descriptors as positivity evidence under the boundary-complete hypothesis.

## Durability

Commit immediately after:

- interior Metzler necessity/refutation;
- reduction of incoming families;
- exact outgoing-row inequalities;
- mandatory symbolic gate;
- finite criterion or counterexample.

Final report:

`students/professor/005-three-state-positivity-criterion.md`.

Final handoff:

`students/professor/005-handoff.md`.

No writes to `main`.
