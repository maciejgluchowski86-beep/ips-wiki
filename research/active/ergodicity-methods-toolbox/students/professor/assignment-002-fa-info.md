# Professor Assignment FA-INFO-002: exact adaptive causal-information test

Date: 2026-08-17

**Active bounded experiment. Stop rule frozen before mathematics.**

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

A valid adaptive evaluator may query any currently unresolved predecessor value whose value can logically short-circuit the output. In particular it may exploit both of the exact Boolean simplifications:

- if a queried neighbour is vacant, legality is certified and the other neighbour need not be queried merely for legality;
- if the old-site value equals the refresh coin, the output equals that common value regardless of legality, so the legality branches need not be queried.

If legality is certified and the old-site value has not already short-circuited the decision, the post-ring spin equals the refresh coin and the older history of site `i` is discarded. If illegality is certified, the old-site history remains necessary. Recursive queries may merge when they ask for the same space-time value.

The reveal order may depend predictably on already revealed graphical marks and spin values, but not on unrevealed time-zero spins.

First formalize this as an exact decision tree/algorithm and prove that its transcript determines the terminal spin. Distinguish:

1. graphical marks known without querying the initial law;
2. queried spin values at positive times, recursively resolved;
3. residual time-zero queries.

Do not call the residual query set a Markov process unless closure is actually proved.

## Part B. Derive the likelihood comparison, do not quote it

Let `Q` denote the full adaptive query transcript under the stationary product initial law `mu_q`, including the queried time-zero sites and their revealed bits. Let `L(Q)` be the likelihood ratio of the same transcript under `mu_{q0}` relative to `mu_q`.

Derive `L(Q)` directly from product independence and the predictable query rule. In particular, show exactly when it is legitimate to write it as the product of one-site likelihood ratios over the queried time-zero bits despite the query set being value-dependent.

Then derive an exact second-moment/chi-square upper bound for the terminal-spin law or for the full finite terminal block. The bound must expose a **two-copy overlap/information object** if a sharper statistic than the raw transcript is used. If the usual simple `2^{|R cap R'|}` form fails because the query set is value-dependent, derive the correct weighted replacement rather than forcing the Ising formula.

This likelihood identity is load-bearing. A first-moment leaf count is diagnostic only.

## Part C. Frozen finite-block falsifier

The first mathematical test is fixed in advance. Do not replace it by a friendlier block after seeing the answer.

### Circuit S1: one constrained ring

Condition on one ring at site `0`, with known refresh coin `z`. Let the three predecessor bits immediately below the ring be

$$
(X,L,R)=(\eta_0,\eta_{-1},\eta_1).
$$

The output is

$$
F_z(X,L,R)=
\begin{cases}
z,&L=0\text{ or }R=0,\\ X,&L=R=1.\end{cases}
$$

Enumerate **all exact predictable decision trees** for this Boolean function, not only left-first/right-first trees. For each `z`, and after averaging over the equilibrium refresh coin, compute exactly:

1. the mark-only globally essential predecessor set;
2. the minimum expected number of queried predecessors under `mu_q` (diagnostic only);
3. the minimum raw transcript likelihood cost
   $$
   \boxed{\mathcal C_1(q,q_0):=\inf_A\left(E_{\mu_q}[L_A(Q)^2]-1\right),}
   $$
   where the infimum is over exact predictable evaluators `A`;
4. the exact output chi-square
   $$
   \boxed{\mathcal X_1(q,q_0):=\chi^2(\Law_{\mu_{q0}}(F_Z),\Ber(q)).}
   $$

Stress at

$$
q=\frac1{10},\qquad q_0\in\left\{\frac1{20},\frac15\right\}.
$$

### Circuit S2: the first adjacent composition

Use two chronologically ordered rings: first at site `1`, then at site `0`, with known refresh coins `z_1,z_0`. No other ring is inserted into this frozen circuit. This is the smallest composition in which the right-neighbour query at the terminal ring is itself the output of a constrained ring and shares predecessor variables with the terminal old-site branch.

The bottom variables lie in radius `2`. Compose the exact Boolean maps and again enumerate all exact predictable decision trees. Compute the analogues `C_2` and `X_2`, with exact averaging over `(z_1,z_0)`.

This circuit is a **local closure gate**, not a claim that conditioning on this skeleton represents the full continuous-time process. A positive result must later control all skeletons/remainders; a closure failure already visible here is admissible negative evidence because every exact block composition must handle this circuit.

### Candidate state and non-negotiable closure test

The starting candidate state is the smallest information state actually justified by Part B:

- raw adaptive transcript likelihood if it contracts; otherwise
- the smallest explicitly derived weighted pair/overlap state which still upper-bounds terminal chi-square.

A scalar output chi-square is **not** considered closed merely because `X_1<X_0`: S2 must admit an exact update of the same state without importing extra lower-layer correlations or a larger decision-tree history.

The radius/depth cap remains radius `4`, two temporal blocks. No third block and no larger state hierarchy is authorized inside this assignment.

## Pre-registered decision rule

The following rule is frozen before computing S1/S2.

1. If every exact S1 evaluator has `C_1 >= C_0`, where
   $$
   C_0=\chi^2(\Ber(q_0),\Ber(q)),
   $$
   while the exact output nevertheless has `X_1<C_0`, then the **raw transcript likelihood is rejected as the iterable state**. Continue only to S2 to test whether the Part-B weighted pair state repairs this loss; do not optimize larger trees.
2. If S1 has a contracting transcript/pair state, S2 must update that same state exactly (or with a proved remainder) and retain a strict contraction at both registered `q0` stress values. Otherwise stop.
3. If S1 output contracts but S2 requires new correlation/history coordinates not present in the S1 state, and the only repair is to carry the larger composed decision tree or enlarge radius/depth, return `STOP-NO-ITERABLE-STATE`.
4. `CONTINUE-ADAPTIVE-BRIDGE` requires a single bounded state `Phi` surviving both S1 and S2, with a strict exact contraction at both stress values and a stated route to averaging arbitrary graphical skeletons without assuming quench mixing.
5. A smaller expected leaf count, one favorable reveal order, or contraction of the exact output law on S1 alone can never trigger continuation.

## Pre-registered outcomes

Return exactly one of:

### `STOP-ADAPTIVE-PAIR-OBSTRUCTION`

Prove an exact pair/likelihood lower bound, valid for every allowed local reveal order in the bounded class, which prevents the required information statistic from contracting. This must be a pair-level obstruction, not merely supercritical expected query count.

### `STOP-NO-ITERABLE-STATE`

Adaptive short-circuiting is real, but after exact S1/S2 composition the residual information cannot be represented by the same bounded state without retaining additional history whose only proposed continuation is an enlarging hierarchy. State the precise closure failure and stop; do not increase radius/depth.

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
- S1/S2 contraction or obstruction;
- a finite-state closure failure.

Final report:

`research/active/ergodicity-methods-toolbox/students/professor/002-fa-info.md`

Final handoff:

`research/active/ergodicity-methods-toolbox/students/professor/002-fa-info-handoff.md`

No `docs/` or `mkdocs.yml` edits.
