# Professor Assignment FA-INFO-002: exact adaptive causal-information test

Date: 2026-08-17

**Queued, not yet executed.**

This is the independent reserve architecture retained by the hostile FA review after `FA-SCREEN-001` stopped at its fixed-boundary scaling obstruction. It is a bounded feasibility experiment, not a full proof-program reopening.

The assignment is written durably before execution because the Professor is currently the only operational research session.

## Scientific target

For one-dimensional hard FA-1f with equilibrium vacancy density `q in (0,1)` and initial Bernoulli vacancy density `q0>0`, prove local convergence from `mu_{q0}` to `mu_q`.

The target of this assignment is much smaller:

> Decide whether a **state-adaptive causal reveal process** for one terminal site has an exact pair/likelihood statistic with a finite-block contraction mechanism which is genuinely absent from the mark-only ancestor process and the conservative centered dual.

## Required reading

On branch `research/ergodicity-methods-toolbox`:

- `project-state.md`, `README.md`, `CHATGPT.md`;
- current `research/active/ergodicity-methods-toolbox/state.md` and `proof-spine.md`;
- Meeting 024;
- `assessment/fa1f-east-hostile-review-g.md`, Candidate 3;
- `assessment/final-method-priorities.md`, FA-INFO section;
- final `FA-SCREEN-001` report only for the anti-loop distinction.

For negative background only, read the closed FA finite-seed proof spine if needed. Do not reuse its conservative transformed dual as the reveal process.

## Part A. Define the exact adaptive evaluator

Use the actual FA graphical construction. A site ring carries its refresh coin `z in {0,1}`. To evaluate a terminal spin backwards through a ring at site `i`, legality is the Boolean OR

$$
1_{\{\eta_{i-1}=0\text{ or }\eta_{i+1}=0\}}.
$$

A valid adaptive evaluator may choose one neighbour to inspect first.

- If the first revealed neighbour is vacant, legality is certified and the second neighbour need not be queried merely for legality.
- If the first is occupied, the second neighbour must be evaluated.
- If the ring is legal, the post-ring spin equals the refresh coin and the older history of site `i` is discarded.
- If the ring is illegal, the old-site history remains necessary.
- Recursive queries may merge when they ask for the same space-time value.

The reveal order may depend predictably on already revealed graphical marks and spin values, but not on unrevealed time-zero spins.

First formalize this as an exact decision tree/algorithm and prove that its transcript determines the terminal spin. Distinguish:

1. graphical marks known without querying the initial law;
2. queried spin values at positive times, recursively resolved;
3. residual time-zero queries.

Do not call the residual query set a Markov process unless closure is actually proved.

## Part B. Derive the likelihood comparison, do not quote it

Let `Q` denote the full adaptive query transcript under the stationary product initial law `mu_q`, including the queried time-zero sites and their revealed bits. Let `L(Q)` be the likelihood ratio of the same transcript under `mu_{q0}` relative to `mu_q`.

Derive `L(Q)` directly from product independence and the predictable query rule. In particular, show exactly when it is legitimate to write it as the product of one-site likelihood ratios over the queried time-zero bits despite the query set being value-dependent.

Then derive an exact second-moment/chi-square upper bound for the terminal-spin law or for the full finite terminal block. The bound must expose a **two-copy overlap/information object**. If the usual simple `2^{|R cap R'|}` form fails because the query set is value-dependent, derive the correct weighted replacement rather than forcing the Ising formula.

This likelihood identity is load-bearing. A first-moment leaf count is diagnostic only.

## Part C. Smallest exact one/two-block experiment

Work on one terminal site and the smallest space-time slab that contains a genuine two-sided constrained decision. Use exact enumeration/rational integration over a bounded graphical event class or exact uniformization; no Monte Carlo.

At minimum compare:

1. the mark-only support which retains both neighbours whenever the update map is globally two-parent;
2. the adaptive reveal tree which short-circuits the second neighbour after an actual vacancy is found;
3. both natural left-first/right-first reveal orders and any genuinely different predictable order justified by the local state.

Then compose **two temporal blocks** using the same state variable. The question is not whether one block has fewer expected leaves, but whether the exact pair/likelihood state is closed enough to iterate.

Stress at a low equilibrium vacancy density, e.g. `q=1/10`, and at more than one nondegenerate `q0` if the likelihood weight depends materially on `q0`.

Computational cap: keep the terminal spatial radius at most 4 and at most two temporal blocks unless an exact structural recursion is discovered. Do not enlarge merely because the first calculation is inconclusive.

## Part D. Required implication chain for a positive signal

A finite calculation counts as `CONTINUE` only if it identifies an object `Phi` such that:

1. `Phi` is defined from the actual adaptive reveal transcript/pair, not from the conservative dual;
2. a block composition rule for `Phi` is exact or has a rigorously controlled remainder;
3. there is a strict contraction or another decay inequality at the low-`q` stress point;
4. iterating that inequality would imply a chi-square/total-variation bound for a fixed observation block without assuming the desired ergodicity.

A one-block numerical advantage with no compositional state is evidence only.

## Pre-registered outcomes

Return exactly one of:

### `STOP-ADAPTIVE-PAIR-OBSTRUCTION`

Prove an exact pair/likelihood lower bound, valid for every allowed local reveal order in the bounded class, which prevents the required information statistic from contracting. This must be a pair-level obstruction, not merely supercritical expected query count.

### `STOP-NO-ITERABLE-STATE`

Adaptive short-circuiting is real, but after exact one/two-block composition the residual information cannot be represented by the same bounded state without retaining additional history whose only proposed continuation is an enlarging hierarchy. State the precise closure failure and stop; do not increase radius/depth.

### `UNRESOLVED-BOUNDED`

The bounded experiment gives a genuine pair-level improvement but neither an exact obstruction nor a rigorously iterable contraction. Record the evidence and exact missing theorem; do not enlarge automatically.

### `CONTINUE-ADAPTIVE-BRIDGE`

Produce a concrete adaptive pair/likelihood state with an exact or rigorously controlled block composition and a strict decay mechanism. State the bridge lemma precisely and give one next assignment-sized proof test.

## Anti-circularity

Do not:

- use convergence/mixing of the FA quench to estimate the reveal tree;
- replace actual time-zero product spins by an exogenous refreshed field;
- identify the adaptive query set with the centered/harmonic finite-set dual;
- use mark-only ancestor extinction as the criterion;
- quote Miller--Peres/Lubetzky--Sly conditional independence without deriving the corresponding likelihood identity for this value-adaptive tree;
- treat a smaller expected number of leaves as sufficient;
- enlarge into a multiscale information-percolation programme unless the bounded pair state first closes.

## Durability

Commit immediately after any of the following becomes durable:

- exact adaptive evaluator/decision-tree definition;
- exact transcript likelihood-ratio identity;
- exact two-copy pair statistic;
- one/two-block contraction or obstruction;
- a finite-state closure failure.

Final report:

`research/active/ergodicity-methods-toolbox/students/professor/002-fa-info.md`

Final handoff:

`research/active/ergodicity-methods-toolbox/students/professor/002-fa-info-handoff.md`

No `docs/` or `mkdocs.yml` edits.
