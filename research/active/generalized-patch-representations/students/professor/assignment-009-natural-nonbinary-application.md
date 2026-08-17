# Assignment 009: natural nonbinary application of the killed typed patch representation

Date: 2026-08-17

Status: **queued, not yet executed**.

Assignment 008 ended `CONTINUE-TO-APPLICATIONS`. The novelty audit removed the `d=3` scalar spectral test from the contribution claim as direct prior art in external-positivity theory, but retained the killed typed patch factorization/representation as the strongest plausible novelty anchor.

This assignment implements the sequencing fixed in Meetings 007--008: applications now come before any generic `d>3` positivity algebra.

## Goal

Test the generalized patch mechanism on a **natural published genuinely nonbinary finite-state single-site replacement IPS**.

The block is successful only if the model is selected independently of whether it flatters the positivity criterion, the typed representation specializes naturally, and the resulting representation/positivity analysis gives mathematically useful information beyond restating a known duality.

A rigorous negative patch-positivity finding is an acceptable outcome.

## Fixed novelty framing

Do not claim novelty for:

- finite-state or multistate graphical duality itself;
- signed Feynman--Kac duality itself;
- ancestor/backward graphical constructions themselves;
- the scalar condition `C e^{tA}B>=0` or the third-order external-positivity calculation;
- symmetry/lumpability spectral calculations by themselves.

The surviving project-specific mechanism to test is

\[
\text{signed typed dual}
\to
\text{successful skeleton hiding post-source outcome}
\to
\text{cemetery-aware killed patch factorization}
\to
\text{exact finite-state patch representation}.
\]

## Part A. Literature-driven candidate selection

Inspect a bounded set of natural published `d=3` single-site replacement IPS. Include at least:

1. a **two-stage / stage-structured contact process** with vacant, juvenile/intermediate, and mature/infective states;
2. a natural **three-state epidemic/contact process** such as an SIR/SIRS-type or two-type contact model, provided the update rule is genuinely single-site replacement;
3. at most one further `d=3` candidate if it is materially better aligned with the representation.

For each candidate record:

- exact local state meanings and transition rates from the source;
- whether the model is truly `d=3` rather than a binary model with a passive color;
- whether all physical updates change one site at a time;
- which neighbour states affect each transition;
- known graphical/duality constructions relevant to application novelty;
- whether the model is irreducible or has absorbing classes, without using irreducibility as a selection criterion.

**Selection rule:** choose the model with the strongest combination of naturality, genuine three-state dynamics, exact fit to single-site replacement, and a nontrivial successful-skeleton geometry. Do **not** use patch positivity as a model-selection criterion.

Commit the selection before computing the typed patch-positivity inequalities.

## Part B. Exact typed specialization

For the selected model:

1. choose and justify the reference state `0` in the indicator tensor basis;
2. write every physical replacement rate `c^{x->y}(eta_N)`;
3. compute the exact typed tensor coefficients `a_r^s(tau)`;
4. list the nonempty successful records `(i,t,r,tau)` and hidden post-source outcomes;
5. identify which typed target conflicts/cemetery events are actually realizable;
6. describe the one-site patch boundary types that occur.

Check the specialization against the physical generator exactly. If the model has parameters, keep them symbolic as long as possible and state every positivity/rate constraint.

## Part C. Patch positivity test

Test **the exact realized patch family**, not an artificially completed boundary family.

Use, as appropriate:

- the exact arbitrary-`d` transfer formulas of Assignment 004;
- the exchange-symmetric / refresh criterion of Assignment 007 if the selected model genuinely lies in that class;
- standard external-positivity theory or exact symbolic matrix analysis for a realized `d=3` response when it does not.

Do not present Assignment 006's spectral calculus as novel; it is only a computational tool here.

Determine one of:

1. a nonempty open/model-natural parameter region where every realized bulk patch is nonnegative;
2. an exact obstruction showing patch positivity fails throughout the natural parameter range;
3. a genuine mixed regime with an exact parameter criterion.

No numerical plotting or floating-point sign decisions may carry the result. Exact symbolic/rational gates are required for any claimed positive or negative parameter point.

## Part D. What does the representation buy?

If the model is patch positive on a nontrivial region, identify the strongest **model-specific** consequence that the generalized patch representation can plausibly support.

Candidate consequences may include:

- a new signed/centered moment comparison;
- monotonicity in a parameter or in an initial-law cone not captured by ordinary attractiveness;
- a transparent invariant-limit or convergence reduction under an additional pure-death/noise component;
- a new finite-volume/infinite-volume representation useful for a known open question.

Do **not** automatically transplant the binary convergence theorem. State exactly which part of the binary argument requires a multi-state end-factor/order theorem that has not yet been proved.

If patch positivity fails, identify whether the failure is caused by:

- active retyping sign;
- outgoing hidden-row sign;
- an interior external-positivity transient;
- cemetery/boundary geometry;
- another exact mechanism.

A structurally informative failure can still justify the application block.

## Part E. Application-specific prior-work check

Before claiming any useful consequence as a contribution, compare it with the selected model's known duality, graphical construction, monotonicity, invariant-measure, and convergence literature.

Separate:

- what the model already has by standard coupling/attractiveness/additive duality;
- what the typed killed-patch representation reproduces in different notation;
- what, if anything, appears genuinely additional.

If the only consequence is already standard, say so and do not count the application as a research result.

## Mandatory exact gates

The selected model must have at least one exact parameter point at which:

1. all physical replacement rates are nonnegative;
2. the typed coefficient table is checked against the physical generator;
3. every realized bulk boundary numerator used in the positivity verdict is checked exactly or covered by a proved symbolic criterion;
4. at least one genuinely three-state feature is active with positive rate.

If claiming a positive parameter region, include both:

- one exact interior positive point;
- one exact boundary/failure point or proof showing where the criterion can break.

## Anti-tuning rule

After Part A commits the selected published model, do not alter its transition structure to make patch positivity hold. Varying parameters already present in the published model is allowed. Adding a new refresh/noise mechanism is a **different model** and may only be considered as a clearly separated secondary variant after the base model's verdict is complete.

## Pre-registered outcomes

Return exactly one programme-level application ruling.

### `CONTINUE-NATURAL-APPLICATION`

A natural genuinely nonbinary published IPS has a nontrivial patch-positive regime, and the killed typed patch representation supplies a model-specific consequence or reduction not already directly subsumed by prior work. State the next bounded theorem needed to turn that consequence into a finished application.

### `NARROW-APPLICATION-REPRESENTATION-NEW-CONSEQUENCE-OPEN`

A natural model has a nontrivial patch-positive regime and the representation is genuinely different from known model dualities, but the useful downstream consequence depends on one precise unproved multi-state order/end-factor statement. Record that statement and make it the next edge.

### `STOP-APPLICATION-POSITIVITY-FAILS`

The selected natural model fails typed patch positivity for a structural exact reason across its natural parameter range. Record the obstruction. If a second candidate from Part A is materially different, it may be checked inside this same bounded block; do not start an unbounded model search.

### `STOP-APPLICATION-ONLY-REEXPRESSES-KNOWN-DUALITY`

The representation specializes correctly and may even be patch positive, but the resulting model-specific statement is already directly available from known duality/coupling/attractiveness theory and no independent value survives.

### `UNRESOLVED-NATURAL-APPLICATION`

One explicit symbolic or literature comparison remains unresolved after the bounded candidate analysis. Record it exactly and do not switch to `d>3` algebra or another application family.

## `d>3` rule

Do not start generic `d>3` criterion work in this block. If the selected best application has more than three states despite the requested candidate set, record why it is superior and queue the needed structured higher-dimensional analysis separately rather than silently broadening scope.

## Durability

Commit immediately after:

- Part A candidate comparison and selected model;
- exact typed coefficient specialization;
- exact patch-positivity verdict;
- application-specific prior-work comparison;
- any model-specific consequence/reduction.

Final report:

`students/professor/009-natural-nonbinary-application.md`.

Final handoff:

`students/professor/009-handoff.md`.

No writes to `main`, `docs/entries/`, `docs/meta/`, or `mkdocs.yml`.