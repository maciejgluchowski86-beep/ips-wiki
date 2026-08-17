# Assignment 011: killed-patch cancellation envelope without bulk positivity

Date: 2026-08-17

Status: **active after verified Assignment 010**.

## Direction decision

Assignment 010 is independently verified. The programme will fund exactly **one bounded continuation block** on the surviving novelty anchor itself: the cemetery-aware killed typed patch representation and its ability to average signed hidden histories **before** absolute values are taken.

This block is chosen over both alternatives considered at Meeting 010:

- no third positivity-driven model search;
- no generic `d>3` external-positivity algebra.

If this block does not produce a composable, mathematically useful cancellation estimate, the programme stops rather than returning to either alternative.

## Goal

Determine whether the exact killed typed patch representation yields a rigorous **absolute-value/norm envelope strictly better than the raw absolute signed-Feynman--Kac dual**, in a form that survives concatenation and can support an actual finite-volume or model-independent estimate even when individual bulk patch contributions have mixed sign.

The block is not successful merely because

\[
|E[X]|\le E|X|
\]

holds patchwise. The point is to test whether the delayed absolute value enabled by killed patch factorization gives a **composable quantitative gain**.

Work first in finite volume, where all sums and skeleton integrals are finite and no infinite-volume integrability issue is present.

## Part A. Exact unnormalized patch-variation envelope

Use Assignment 003 in its unnormalized form

\[
P_tH_{\xi_0}(\eta)
=\int \prod_{P\in\mathcal P_t(g)}
F_P(\eta)\,m_t(dg),
\]

where

\[
F_P(\eta)
=E_P[w_P(\Sigma_P;\eta)1_{Con(P)}].
\]

Do **not** use conditional contributions `C(P)` as the primary norm object: Assignment 010 shows that consistency denominators may be tiny and conditional patch contributions can be badly scaled. The natural cancellation object is the unnormalized killed factor before dividing by consistency probability.

Define a positive patch-variation envelope by taking absolute values only **after** each local hidden-history expectation. For end patches use either the exact terminal-state supremum or, if a coefficient norm is more useful, an explicitly defined finite-state basis norm. State the definition precisely and prove

\[
|P_tH_{\xi_0}(\eta)|\le \mathcal R_t(\xi_0)
\]

for the chosen envelope.

Define in parallel the raw absolute FK envelope obtained by removing all branch signs **before** local averaging. Prove an exact comparison

\[
\boxed{\mathcal R_t(\xi_0)\le \mathcal A_t(\xi_0)}
\]

from the same killed factorization, with every cemetery/noncemetery indicator accounted for.

The comparison must be at the level of the actual finite-volume representation, not a heuristic independence argument.

## Part B. Strict-cancellation gate

Show that the inequality in Part A is sometimes genuinely strict because opposite hidden signs are averaged within one patch before absolute values.

Use at least one already-verified natural application from Assignments 009--010. Prefer the Potts Metropolis gate if it gives the cleanest exact arithmetic.

Produce an exact realized positive-length patch descriptor for which

\[
\left|E_P[w_P1_{Con(P)}]\right|
< E_P[|w_P|1_{Con(P)}].
\]

No floating-point sign decision is allowed. If strict local cancellation cannot be exhibited in either natural model despite their nondeterministic hidden marks, record that as evidence against the route.

This gate exists to distinguish a genuine use of hidden-mark averaging from a formal rewriting of the triangle inequality.

## Part C. Composability gate

This is the load-bearing part.

Determine whether the patch-variation envelope can be organized into a positive object that composes across deterministic time cuts without undoing the local cancellation. Acceptable forms include, for example:

1. a positive finite-volume operator family `R_t` satisfying
   \[
   R_{t+s}\le R_tR_s
   \]
   in a specified coefficient/order sense;
2. a weighted coefficient norm `||.||_*` for which
   \[
   ||P_{t+s}||_*\le ||P_t||_*||P_s||_*
   \]
   and the patch representation gives a strictly smaller computable majorant than raw absolute FK;
3. an exact renewal/semi-Markov kernel on successful skeletons whose positive convolution powers equal or dominate the patch-variation envelope and retain the strict local cancellation from Part B.

A merely finite-horizon scalar quantity with no concatenation or renewal structure is **not** enough for continuation.

If a natural composable object exists, derive it exactly and state which information must be retained at a time cut (typed boundary state, unfinished patch type, source label, etc.). Do not claim a Markov semigroup if the necessary boundary memory makes it only a renewal kernel.

If composability fails, isolate the precise obstruction. In particular distinguish:

- time-cutting through unfinished patches;
- absolute values destroying cancellation between different coarse skeletons;
- cemetery conditioning changing after the cut;
- terminal typed boundary data that cannot be summarized finitely;
- another exact mechanism.

## Part D. Usefulness / qualitative-gain gate

Even a composable envelope is not enough if it is only a repackaging of the raw total-variation dual.

Establish at least one of the following:

### D1. Qualitative natural-model gain

For one natural published model already in the programme (two-stage contact, SIRS, or Potts Metropolis), exhibit an exact parameter point or symbolic region where the patch-averaged envelope gives a qualitative improvement over raw absolute FK, for example:

- a subcritical/contractive renewal kernel while the raw absolute dual majorant is noncontractive;
- a strictly smaller exponential growth bound crossing a meaningful threshold;
- a finite-volume norm contraction not available from the raw absolute process.

### D2. Model-independent theorem with downstream force

Prove a structural theorem giving a checkable condition under which local hidden-mark cancellation forces a volume-uniform norm/contraction estimate, and identify one concrete downstream statement it would imply if the condition is verified in a model.

The theorem must use the killed patch averaging essentially. A condition equivalent to ordinary generator dissipativity, ordinary Markov sup-norm contraction, or the standard absolute dual bound does not count.

## Part E. Prior-work sanity check

If Parts C--D succeed, compare the resulting object with standard signed-semigroup domination, Duhamel/Dyson absolute-value bounds, cluster/Polymer expansions, renewal inequalities, and positive majorants for Feynman--Kac representations before calling it a contribution.

A generic inequality such as `|e^{tK}|<=e^{tM}` or `|E X|<=E|X|` is standard and is not a novelty claim. The project-specific question is whether the **successful-skeleton / killed-patch grouping** produces a composable stronger majorant.

Do not launch a broad literature review if Parts C--D already fail.

## Mandatory exact gates

If the block claims continuation, it must include:

1. an exact finite-volume proof of `R_t <= A_t` with cemetery handled correctly;
2. one exact strict-cancellation patch from a natural verified model;
3. an exact composability/submultiplicativity or renewal statement;
4. one exact qualitative-gain gate under Part D;
5. a verifier for any nontrivial finite arithmetic or matrix certificate used in the continuation claim.

No numerical plot or floating-point sign decision may carry a conclusion.

## Pre-registered outcomes

Return exactly one programme-level ruling.

### `CONTINUE-KILLED-CANCELLATION`

Parts A--D all succeed: the killed patch representation yields a composable positive cancellation envelope strictly below raw absolute FK, with either a qualitative gain on a natural model or a model-independent contraction theorem with concrete downstream force. State the next bounded theorem/application needed.

### `NARROW-CANCELLATION-CONSEQUENCE-OPEN`

Parts A--C succeed and the envelope is genuinely stronger/composable, but Part D reduces usefulness to **one precise unproved inequality or model verification** that is not another generic search. State that single edge. This outcome is allowed only if the missing statement is sharply formulated and the existing work already gives a nontrivial theorem beyond triangle inequality.

### `STOP-CANCELLATION-ONLY-LOCAL`

Patchwise delayed absolute values give strict local cancellation, but no finite-memory/submultiplicative/renewal object preserves it across time cuts. Record the exact composability obstruction and **stop the programme**.

### `STOP-CANCELLATION-NO-QUALITATIVE-GAIN`

A composable envelope exists, but it is equivalent to or no more useful than standard raw absolute-FK / signed-semigroup majorants, or it yields no qualitative gain under the bounded natural-model/model-independent tests. Record the strongest theorem retained and **stop the programme**.

### `STOP-CANCELLATION-NO-STRICT-GAIN`

Even the strict local cancellation gate fails in the verified natural models or the proposed envelope collapses identically to the raw absolute envelope. **Stop the programme.**

### `UNRESOLVED-KILLED-CANCELLATION`

One explicit algebraic/composability question remains genuinely unresolved after the bounded block. Record it exactly. Do not respond by opening `d>3`, another model search, or a second vague cancellation block.

## Anti-loop rules

Do not:

- return to pointwise bulk patch positivity as the target;
- search for a third flattering model;
- start generic `d>3` external-positivity algebra;
- count a triangle inequality by itself as a result;
- replace the killed patch representation by a standard raw signed-FK majorant and call that progress;
- enlarge the state carried at a time cut without stating exactly what information is needed and whether it remains finite;
- modify `docs/entries/`, `docs/meta/`, or `mkdocs.yml`.

## Durability

Commit immediately after:

- Part A envelope/comparison theorem;
- Part B strict natural-model cancellation gate;
- Part C composability decision;
- Part D usefulness ruling;
- any verifier.

Final report:

`students/professor/011-killed-patch-cancellation-envelope.md`.

Final handoff:

`students/professor/011-handoff.md`.

If the ruling is a stop, also record a programme-closing meeting and update `state.md`, `proof-spine.md`, and root `project-state.md` accordingly.

No writes to `main`.