# Assignment 007: natural simplifications of the exact three-state spectral criterion

Date: 2026-08-17

Status: **queued, not yet executed**.

Assignment 006 ended `CONTINUE-EXACT-THREE-STATE-SPECTRAL-CRITERION`. The exact boundary-complete `d=3` positivity test is finite but generically retains one spectral critical inequality involving `R^{mu/(nu-mu)}`.

Applications, convergence, and `d>3` remain out of scope.

## Goal

Determine whether a mathematically natural non-binary structural subclass makes the exact Assignment-006 critical condition algebraic, monotone, or one-mode, while preserving **necessity and sufficiency within the subclass** and exact binary reduction.

Do not replace the exact property by an arbitrary sufficient cone.

## Fixed input

Under boundary completeness:

- `K` is Metzler;
- incoming-initial and `OO` families are automatic after zero-length conditions;
- every remaining `OI` numerator is decided by the exact finite spectral criterion of Assignment 006;
- in the generic case
  \[
  N(t)=L+A e^{-\mu t}+B e^{-\nu t};
  \]
- Assignment 005 proves that deleting the interior critical check in the general class is invalid.

## Part A. Active-type lumpability

Study the natural physical condition that the reference-neighbour one-site chain is lumpable with respect to

\[
\{0\},\qquad\{1,2\}.
\]

Determine exactly when the `OI` value functions arising from outgoing coefficient rows descend to the same two-block quotient.

If both the dynamics and relevant value function lump, prove or refute that the numerator becomes one-mode and the exact positivity criterion reduces to endpoint inequalities.

Distinguish a genuinely three-state system with hidden active-type dynamics from a literal binary encoding.

## Part B. Active-type symmetry

Test the stronger but natural subclass invariant under exchanging active types `1` and `2` at the reference-neighbour level and in the nonempty-target coefficient rows.

Determine whether the symmetric/antisymmetric spectral modes separate so that every admissible `OI` row kills the antisymmetric mode, leaving a one-mode exact criterion.

Prove necessity and sufficiency inside the symmetric subclass if the reduction holds.

## Part C. One-way active retyping

Study triangular active transfer blocks, where exactly one of

\[
K(1,2),\qquad K(2,1)
\]

vanishes.

This class is physically natural for irreversible type conversion. Determine whether the exact critical inequality simplifies algebraically, or whether the two distinct decay modes still create a genuinely transcendental critical comparison.

If an interior critical obstruction survives, give an exact physically realizable witness and stop treating triangularity as a simplification.

## Part D. Non-binary honesty check

Any successful subclass must contain a genuine `d=3` IPS in which both active physical states occur with positive probability and at least one local mechanism distinguishes them.

A class whose exact criterion works only because the model is dynamically or observably equivalent to a binary system does **not** count as the desired multi-state simplification; record it as binary-reducible.

## Part E. Binary reduction

Suppress type `2`. Every proposed exact subclass criterion must reduce to the canonical binary inequalities

\[
c^0(S)+c^1(S)\le0,
\qquad
c^1(\emptyset)c^0(S)
\ge c^0(\emptyset)c^1(S),
\]

with the canonical degenerate clause and no extra condition.

## Mandatory exact gates

For each candidate subclass that survives the structural analysis:

1. give one exact physically realizable non-binary positive example satisfying the subclass and verify all relevant `OI` numerators;
2. give either a negative example inside the subclass or prove exact positivity equivalence from the subclass criterion;
3. use exact arithmetic/symbolic algebra only for sign decisions.

## Pre-registered outcomes

Return exactly one.

### `CONTINUE-NATURAL-THREE-STATE-SUBCLASS`

At least one genuinely non-binary natural subclass has an exact necessary-and-sufficient coefficient/endpoint criterion materially simpler than the generic spectral critical test. State the subclass and criterion. Do not start applications.

### `STOP-SIMPLIFICATIONS-BINARY-REDUCIBLE`

Every exact simplification found in the tested lumpable/symmetric classes works only because the relevant patch observable factors through a two-state quotient. Record the exact reduction and do not advertise it as a new multi-state positivity class.

### `STOP-TRIANGULAR-STILL-SPECTRAL`

The natural one-way-retyping class retains a genuine two-mode interior critical obstruction and the lumpable/symmetric routes are either binary-reducible or do not simplify the exact criterion. Give the exact witness.

### `UNRESOLVED-NATURAL-SUBCLASS`

One named candidate remains mathematically unresolved after the bounded analysis. Record the exact missing inequality and do not move to applications.

## Anti-loop rules

Do not:

- revive the endpoint-only general criterion refuted in Assignment 005;
- call a merely sufficient cone an exact subclass criterion;
- count a binary quotient as a genuinely multi-state result;
- enlarge to arbitrary `d`;
- start applications or convergence;
- make a novelty claim before literature audit.

## Durability

Commit immediately after each candidate subclass is classified.

Final report:

`students/professor/007-natural-spectral-simplification.md`.

Final handoff:

`students/professor/007-handoff.md`.

No writes to `main`.
