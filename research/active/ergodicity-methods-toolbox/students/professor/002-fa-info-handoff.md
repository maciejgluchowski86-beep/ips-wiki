# FA-INFO-002 handoff

Date: 2026-08-17

Status: **`STOP-NO-ITERABLE-STATE`**.

Assignment: `students/professor/assignment-002-fa-info.md`, stop rule frozen before mathematics at commit `ef3dfcfe`.

## Decisive result

Adaptive pruning is real but the bounded likelihood architecture does not close.

At

\[
q=\frac1{10},
\qquad q_0\in\left\{\frac1{20},\frac15\right\},
\]

all exact S1/S2 decision-tree and pair calculations are rational and verifier-backed.

- S1 mark-only support has 3 predecessors for either fixed coin; the optimal adaptive evaluator uses only `671/500` queries on average.
- Nevertheless optimal raw transcript `L^2` expands the baseline one-bit chi-square at both quenches:
  `807341/648000` and `17594/10125`.
- Exact fully averaged output chi-square contracts from the initial product bit, but S2 is larger than S1 at both quenches:
  `15689521/14440000` and `58081/40000`.
- The exact same-graphical-history pair state also increases S1 -> S2 at both quenches; at `q_0=1/20` it is already above the baseline on S1.
- Exact full-predecessor chi-square SDPI coefficients are below one, but paying the predecessor-vector divergence gives factors above one at both stresses.
- A right-to-left staircase of `m` adjacent rings creates a full centered correlation coefficient `(-q)^(m-1)`, so exact output composition generates new correlation order indefinitely.

Thus every bounded state actually derived in the registered experiment has one of two defects:

1. enough transcript/graphical information to compose, but no contraction;
2. enough averaging to recover contraction, but no bounded exact state for the next constrained ring.

The only exact repair visible is the growing joint transcript/correlation hierarchy, which the assignment explicitly forbids.

## Files

- `002a-fa-info-adaptive-likelihood.md`, commit `ae910cd9`;
- `002b-fa-info-finite-circuit-closure.md`, commit `c5113b6e`;
- `002c-fa-info-shared-mark-pair.md`, commit `4d76c8c0`;
- final verifier `002-fa-info-finite-circuit-verifier.py`, commit `5bcf597c`;
- final report `002-fa-info.md`, commit `e63191d7`.

## Verifier

Run

`python research/active/ergodicity-methods-toolbox/students/professor/002-fa-info-finite-circuit-verifier.py`

Expected final line:

`all exact FA-INFO finite-circuit checks passed`

It also prints the exact S1/S2 transcript, shared-mark pair, output-chi-square, SDPI, and four-body-coefficient certificates.

## Scope

Killed/stopped:

> the bounded state-adaptive likelihood/pair implementation pre-registered in FA-INFO-002.

Not proved impossible:

- every conceivable adaptive-information proof of FA convergence;
- a materially different inequality which controls the growing correlation hierarchy without carrying it explicitly;
- a different moving-boundary theorem outside stopped FA-SCREEN.

However none of those is currently an A/B architecture with its own bounded positive signal. Do not enlarge this assignment to a third block, radius above 4, larger transcript state, or multiscale hierarchy.

No `docs/` file or `mkdocs.yml` was edited.
