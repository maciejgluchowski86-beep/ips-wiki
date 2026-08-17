# Student G Assignment 012: optimized backward-history pair-intersection test

Date: 2026-08-17

This is a **bounded pre-restart feasibility experiment**, not a reopening of a full positive-rates proof architecture.

Meeting 032 accepts G011 as `STOP-EQUIVALENT` and closes the `pi_N`-based distinguished-zero transfer. The same meeting also proves analytically that the toolbox Bridge R requiring uniform negative additive-Hamming drift is impossible at the hard point for **every** Markovian coupling, so the previously proposed non-diagonal Hamming LP is no longer worth running.

The remaining genuinely different bounded experiment from the toolbox synthesis is information percolation / optimized backward histories.

## Goal

Decide whether the positive-rates residual generator admits a random-map representation whose **pair of minimal backward supports** shows a concrete intersection-decay mechanism not reducible to naive first-moment ancestor extinction.

A positive return does not need to prove ergodicity. It must exhibit a precise pair-history object with a strict finite-time or finite-depth contraction signal and a credible theorem-level route to iteration.

A negative return should identify a structural obstruction tied to pair intersections, not merely report that the mean ancestor count is supercritical.

## Required reading

On branch `research/positive-rates-conjecture` read:

- `CHATGPT.md`;
- `research/active/positive-rates-conjecture/state.md`;
- `research/active/positive-rates-conjecture/proof-spine.md`;
- `research/active/positive-rates-conjecture/programme-established-results.md`;
- `research/active/positive-rates-conjecture/meetings/032-distinguished-zero-transfer-stops-and-hamming-coupling-killed.md`.

From branch `research/ergodicity-methods-toolbox` read:

- `docs/entries/information-percolation-backward-histories.md`;
- `research/active/ergodicity-methods-toolbox/assessment/positive-rates-shortlist.md`, Candidate 3;
- `research/active/ergodicity-methods-toolbox/assessment/positive-rates-hostile-review-professor.md`, Candidate 3;
- `research/active/ergodicity-methods-toolbox/assessment/final-method-priorities.md`, positive-rates information-percolation section.

No broad literature search is requested. Repository claims are evidence, not authority; rederive the actual residual random-map algebra.

## Fixed model and stress point

Work first at

$$
P_h=\left(a,b,c\right)
=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right)
$$

on the normalized face `r11=0`.

The spin-flip rates at a site with current spin `x` and right neighbour `y` are

$$
0\to1:\quad a\ (y=0),\quad b\ (y=1),
$$

$$
1\to0:\quad 1-c\ (y=0),\quad 1\ (y=1).
$$

Do not assume the rate-one common-uniform map is the optimal history representation. A continuous-time random-map decomposition may use independent Poisson marks for arbitrary deterministic Boolean maps `F:{0,1}^2->{0,1}`, with no-op effects allowed, provided the induced marginal generator is exact.

## Part A. Exact random-map polytope

Let `q_F>=0` be the rate of a deterministic local map `F(x,y)`.

Derive the exact linear constraints

$$
\sum_{F:F(x,y)\ne x}q_F=\lambda_{xy}
$$

for all four inputs, where `lambda_xy` is the actual flip rate above. Maps that are globally identical to the identity may be discarded.

For each Boolean map, classify its **essential backward parent set**:

- `emptyset`: constant map, history dies;
- `{self}`;
- `{right}`;
- `{self,right}`.

Two maps with the same essential parent set have the same mark-only support transition, although their spin function differs.

Tasks:

1. characterize the exact attainable region of aggregate ancestry rates
   $$
   (d,s,j,r)
   $$
   for death / self-only / right-only / two-parent marks;
2. maximize `d` and, subject to that, minimize the genuinely branching two-parent rate `r`, but do **not** treat this lexicographic optimizer as automatically optimal for pair intersection;
3. identify whether the canonical four-mark decomposition
   - reset to 1 at rate `a`,
   - reset to 0 at rate `1-c`,
   - `x OR y` at rate `b-a`,
   - `x AND (NOT y)` at rate `c`,
   is extremal or improvable in the ancestry polytope.

Use exact rational LP/algebra. Commit a verifier if the polytope calculation is nontrivial.

A first-moment statistic such as `r-d` or expected offspring is **diagnostic only**. It is not a kill criterion.

## Part B. Exact backward support process

For a fixed decomposition, define the mark-only minimal support `A_t` for one terminal site by running graphical marks backward:

- constant mark: remove the current site;
- self-only mark: keep it;
- right-only mark: replace it by its right neighbour;
- two-parent mark: replace it by the union of itself and its right neighbour;
- merge duplicate ancestors immediately.

This is a finite-set Markov process on the one-sided line. Write its generator explicitly in terms of `(d,j,r)`; self-only marks may be omitted because they do not change support.

Then take two conditionally independent copies `A_t,A_t'` using independent backward marks and define the pair-intersection observable

$$
\Psi(A,A')=2^{|A\cap A'|}-1.
$$

The target is the pair object, not `E|A_t|`.

## Part C. Bounded pair-intersection experiment

Construct the smallest rigorous finite calculation that can distinguish a real information-percolation signal from naive branching failure.

Preferred implementation:

1. exploit translation invariance to quotient a pair `(A,A')` by common translation and truncate relative width at `W`;
2. use exact uniformization / rational interval bounds for the pair-support generator;
3. test a small finite list of decompositions including every extremal point of the ancestry-rate polytope and any decomposition that is genuinely better for the pair statistic;
4. search for a block time `T` and a nonnegative finite-state weight `Phi` dominating `Psi` on the retained states such that
   $$
   E[\Phi(A_T,A_T')]
   \le \rho\,\Phi(A_0,A_0')
   $$
   with `rho<1`, plus an explicit controlled truncation/escape error.

You may replace this by another exact pair-support criterion if it is closer to the Miller--Peres interface, but explain the implication.

A positive finite calculation is evidence only unless you identify why the same state variable can iterate uniformly in width. The assignment is to find that state variable or discover that the simple pair-support architecture has no such signal.

## Part D. Strong negative outcomes that count

A negative result clears the bar only if it concerns the pair-history object itself. Examples:

1. prove that every admissible decomposition dominates a common finite-state/pair process for which `Psi` has a nondecaying positive lower bound;
2. prove an exact variational lower bound on the pair-support semigroup preventing any strict block contraction for all decompositions;
3. prove that every decomposition with maximal oblivious-death rate necessarily contains an unavoidable one-sided branching component whose **two-copy intersection** survives with positive probability, with the implication to `Psi` shown explicitly.

Merely proving supercritical expected ancestor count, positive drift of `|A_t|`, or failure of one arbitrary truncation is not enough.

## Pre-registered stop condition

Do not turn this into a large-state computation.

- Derive the exact decomposition/ancestry polytope first.
- Use at most widths `W<=8` and a bounded set of block times unless a structural recursion is discovered.
- If all observed behavior is simply "first moment is supercritical" with no pair-level theorem or contraction signal, return `STOP-NO-PAIR-SIGNAL`; do not enlarge `W`.
- If a strict pair contraction appears only because of a favorable truncation boundary and cannot be converted to a rigorous full-process bound, return `UNRESOLVED-BOUNDED`, not `CONTINUE`.
- Continue only if there is a concrete pair-history state/inequality that is plausibly iterable without assuming ergodicity, common-coupling extinction, tail-shift agreement, or Meeting 030's signed boundary-transmission estimate.

Permitted final statuses are exactly:

- `STOP-PAIR-OBSTRUCTION`;
- `STOP-NO-PAIR-SIGNAL`;
- `UNRESOLVED-BOUNDED`;
- `CONTINUE-PAIR-BRIDGE`.

If `CONTINUE-PAIR-BRIDGE`, state the bridge lemma precisely and give one next assignment-sized proof test. Then stop for Professor review.

## Durability and output

Commit durable intermediate results immediately, especially:

- the exact random-map/ancestry polytope;
- any decomposition-independent pair lower bound;
- any exact finite pair contraction certificate;
- any rigorous truncation-error estimate.

Final report:

`research/active/positive-rates-conjecture/students/student-g/012-information-percolation-pair-history.md`

Final handoff:

`research/active/positive-rates-conjecture/students/student-g/012-handoff.md`

## Scope discipline

- No broad literature search.
- No return to G010 coefficient tables or filter optimization.
- No common-coupling occupation theorem.
- No generic norm/coupling search.
- No `docs/` or `mkdocs.yml` edits.
