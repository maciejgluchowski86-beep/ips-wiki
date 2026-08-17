# Student G Assignment 013: scalar Gray splice-edge feasibility at the hard point

Date: 2026-08-17

This is a **final bounded structural test of the remaining toolbox PASS candidate**, not a reopening of a full positive-rates proof programme.

Meeting 033 accepts Assignment 012 as `STOP-PAIR-OBSTRUCTION`: every exact deterministic-Boolean mark-only support decomposition at `P_h` has a nondecaying two-copy intersection observable. Meeting 032 already killed the uniform additive-Hamming non-diagonal coupling bridge for every Markovian coupling. The only toolbox PASS idea not actually tested at its own load-bearing observable is Gray's nonadditive one-dimensional splice-edge geometry.

The purpose of this assignment is to make that geometry precise enough to test locally, or to show that doing so forces exactly the attractive/repulsive structure absent at the hard point.

## Goal

Decide whether a **scalar, two-type Gray-style splice edge** can close under the actual residual generator at

$$
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right).
$$

A successful result is one of:

1. **local obstruction:** prove that the exact hybrid/splice closure, no-crossing and coalescence identities force attraction/repulsion or another rate identity violated at `P_h`;
2. **exact infeasibility:** formulate the faithful finite local grand-coupling constraints and prove the rational feasibility problem empty at `P_h`;
3. **new bridge:** exhibit a concrete local scalar-edge grand coupling satisfying all local Gray identities at `P_h`, with a precise remaining global theorem and one bounded next test.

Do not replace this by Hamming drift. Meeting 032 already proves that additive-Hamming contraction is impossible and irrelevant to the nonadditive edge question.

## Required reading

On branch `research/positive-rates-conjecture` read:

- `CHATGPT.md`;
- `research/active/positive-rates-conjecture/state.md`;
- `research/active/positive-rates-conjecture/proof-spine.md`;
- `research/active/positive-rates-conjecture/programme-established-results.md`;
- Meetings 015, 017, 019, 030, 032 and 033;
- `students/student-g/006-common-coupling-survival.md` only for one-sided disagreement geometry, not as the coupling to reuse.

From branch `research/ergodicity-methods-toolbox` read:

- `docs/entries/one-dimensional-edge-coalescence-positive-rates.md`;
- `assessment/positive-rates-shortlist.md`, Gray candidate;
- `assessment/positive-rates-hostile-review-professor.md`, Gray candidate;
- `assessment/final-method-priorities.md`, positive-rates coupling family.

No broad literature search. The source-audited toolbox page is evidence, not authority: rederive every local identity you use.

## Part A. Reconstruct the load-bearing Gray object

Before writing an LP, state the minimum local structure that Gray's argument actually needs.

Separate:

1. **hybrid identity:** a process spliced from two source copies along a single edge agrees exactly with one source on one side and the other source on the other side;
2. **scalar closure:** after any local graphical event, the hybrid is still representable by the same two source copies with one scalar edge (possibly shifted by one site) and one of the two Gray edge types;
3. **protection:** while a left/right edge pair remains separated, changes outside the pair cannot alter the hybrid value in the protected interval;
4. **no crossing:** ordered edge positions cannot reverse order;
5. **permanent coalescence:** two edges that meet can thereafter be represented by one edge.

Identify exactly which of these Gray obtains from attraction/repulsion and which could, in principle, be imposed directly on a nonmonotone grand coupling.

The assignment tests only the **direct scalar/two-type replacement** of those identities. It does not allow an arbitrary finite-state interface whose state dimension is increased until closure appears.

## Part B. Define a faithful finite local feasibility problem

Use a common local grand coupling, not merely a pairwise coupling chosen separately for each initial pair.

You may represent a local graphical event by a random deterministic transition rule on the minimal neighborhood needed to update one site, or by an equivalent finite collection of joint-rate variables, provided:

- every source/hybrid marginal has exactly the target spin generator;
- the same event acts consistently on all source and hybrid configurations in the local test;
- scalar splice identities are pathwise, not only distributional;
- edge-type/position updates are predictable from the pre-event local state and the common event;
- no hidden total spin order is assumed.

Use the smallest local window that actually tests an event at a splice boundary. A three- or four-site window should be enough unless you prove otherwise.

A useful formalization is to keep two source configurations `X,Y` and the two hybrids obtained by splicing `X|Y` and `Y|X` at an edge. For every local source state and common event, require each updated hybrid to equal one of the allowed post-event scalar splices of the updated sources, with edge shift at most the interaction range. But do **not** impose this for arbitrary source pairs if Gray's actual local object only requires a smaller, explicitly justified edge-state class; over-strengthening is a false kill.

Your first task is therefore to derive the correct finite allowed edge-state class from the hybrid identities, not guess it.

## Part C. Exact hard-point test

Once the local edge-state class is fixed, solve the exact feasibility question at `P_h`.

Preferred outcomes, in descending strength:

### C1. Analytic rate obstruction

Derive necessary inequalities on `(a,b,c)` from scalar splice closure/no-crossing/coalescence and show they reduce to the attractive or repulsive region, or otherwise fail at `P_h`.

If this works, give the symbolic parameter locus and stop. This is stronger than any finite LP.

### C2. Rational local infeasibility certificate

If the conditions are naturally linear in joint event rates, solve the exact rational LP and produce a dual/Farkas certificate or another exact finite proof of infeasibility. A floating-point solver result is not enough.

### C3. Feasible local mechanism

If feasible, write the actual grand-coupling event rules/rates explicitly and verify:

- all marginal flip rates;
- scalar hybrid closure for every allowed local edge state;
- no crossing for adjacent edges;
- permanent coalescence after meeting;
- protected-region identity for the smallest nontrivial edge pair.

A small-window feasible point is evidence only. If found, formulate the exact global bridge lemma still missing and one next bounded falsification test.

## Part D. Anti-overstrengthening checks

Before declaring an obstruction, test it against the known attractive/repulsive cases.

Your local definition must admit Gray's architecture on at least a representative attractive point and, after the alternating spin transform, a representative repulsive point. If it rejects those, the definition is too strong and cannot be used to kill the nonmonotone route.

Similarly, do not infer failure merely because a particular deterministic Boolean-map decomposition contains a nonmonotone map. A grand coupling may redistribute local event mass. The obstruction must concern **every** exact local grand coupling satisfying the stated scalar-edge identities.

## Pre-registered stop condition

This is not permission for another open-ended interface programme.

**STOP-SCALAR-EDGE-OBSTRUCTION** if a valid local definition passes the attractive/repulsive sanity checks and is analytically or exactly infeasible at `P_h`.

**STOP-NO-FAITHFUL-LOCALIZATION** if, after reconstructing Gray's identities, no finite scalar/two-type local state can even state the protected hybrid identities without already assuming a global order. Explain precisely why; do not replace it by a larger interface state.

**CONTINUE-GRAY-BRIDGE** only if an exact scalar/two-type local grand coupling exists at `P_h` and you can name a global theorem strictly weaker than ergodicity that would complete Gray's edge-density/coalescence argument.

If the scalar/two-type test fails, **do not** enlarge to 4, 8, 16, ... edge phases, matrix-product edges, ancestry counters, or a generic nonlocal coupling. Meeting 033 pre-registers that as the stopping point for the toolbox-derived Gray route.

## Durability and output

Commit durable intermediate results immediately, especially:

- the faithful local scalar-edge definition;
- the attractive/repulsive sanity check;
- any symbolic necessary-rate theorem;
- any exact infeasibility certificate;
- any explicit feasible local grand coupling.

Final report:

`research/active/positive-rates-conjecture/students/student-g/013-gray-scalar-edge-feasibility.md`

Final handoff:

`research/active/positive-rates-conjecture/students/student-g/013-handoff.md`

Final status must be exactly one of:

- `STOP-SCALAR-EDGE-OBSTRUCTION`;
- `STOP-NO-FAITHFUL-LOCALIZATION`;
- `CONTINUE-GRAY-BRIDGE`.

Then stop for Professor review.

## Scope discipline

- No Hamming contraction or common-uniform coupling repair.
- No state-adaptive information-history escalation.
- No return to tail shift, Bellman, Foster, PR1 coefficient tables, filter optimization, or reversible perturbation.
- No broad literature search.
- No `docs/` or `mkdocs.yml` edits.
