# Assignment 010: structurally distinct non-catalytic three-state application

Date: 2026-08-17

Status: **queued, not yet executed**.

Assignment 009 ended `STOP-APPLICATION-POSITIVITY-FAILS`. The literature-selected two-stage contact process and one bounded SIRS candidate both fail typed patch positivity because of the same catalytic-birth no-go:

> a positive nonempty target mode in `0->r`, with no compensating active-source target-mode transition into `r`, forces `a_r^r(tau)<0`; if the source-`r` record can repeat, a realized short `OO` patch is negative.

This assignment does not tune those models or add noise. It asks for one structurally different application architecture.

## Goal

Select from the literature, **before any positivity calculation**, a natural genuinely three-state finite-state single-site replacement IPS in which neighbour interactions can retype already-active states or otherwise contain compensating active-source target modes, so the Assignment-009 catalytic-birth no-go does not determine the answer in advance.

Then specialize the killed typed patch representation and give an honest positive or negative application verdict.

## Part A. Literature-driven candidate set

Inspect a bounded set of at most three published three-state IPS from structurally distinct families. Prioritize models such as:

- multistate/cyclic voter or biased voter systems with genuine active-to-active replacement;
- spatial stochastic Lotka--Volterra / cyclic competition systems with neighbour-driven type replacement;
- another well-established three-state spin system in which a neighbour interaction changes an already-active type, if it is mathematically cleaner and genuinely nonbinary.

Do not select a model merely because its coefficients look patch positive.

For every candidate record:

1. exact local states and rates from the source;
2. whether every event is single-site replacement;
3. whether all three states are dynamically/observably genuine;
4. whether the neighbour mechanism acts on active sources, rather than only creating activity from a reference state;
5. known graphical/duality theory;
6. whether the model is essentially deterministic voter copying or another case whose duality already leaves no room for the killed hidden-mark mechanism.

### Selection rule

Choose the strongest combination of:

- mathematical naturality and published significance;
- genuine three-state interaction;
- exact fit to the proved single-site replacement framework;
- nontrivial hidden-outcome/signed geometry after tensor expansion;
- application value beyond a colored binary encoding or deterministic copy process.

**Do not compute patch positivity before committing the selection.**

## Part B. Exact specialization

For the selected model:

1. choose and justify the reference state;
2. write all physical rates `c^{x->y}`;
3. compute all nonzero typed coefficients `a_r^s(tau)`;
4. list realized successful records and hidden outcomes;
5. determine whether typed cemetery conflicts occur;
6. identify the exact realized patch boundary family.

Check the typed generator against the physical generator exactly.

## Part C. Exact positivity verdict

Test only realized bulk patches.

Use the arbitrary finite-state transfer theorem, and standard external-positivity theory only as a computational tool. Do not claim novelty for scalar matrix-response positivity.

Determine exactly one of:

1. a nontrivial patch-positive parameter region;
2. a structural all-parameter obstruction;
3. a mixed exact parameter criterion.

All sign decisions must be symbolic/exact or covered by a proved criterion. Include an exact finite gate.

## Part D. Hidden-mark honesty check

A positive application counts only if the selected model genuinely exercises the surviving novelty anchor.

If every successful record has a deterministic post-source outcome, or the construction reduces directly to a standard coalescing/additive graphical dual with no nontrivial hidden mark and no cemetery-aware factorization issue, record that explicitly.

A patch-positive model that only reproduces a standard deterministic voter dual is **not** a successful application of the killed typed mechanism.

## Part E. Model-specific consequence and prior work

If patch positivity holds nontrivially, identify one exact consequence or reduction that depends on the typed patch representation and compare it with the model's known coupling/duality/monotonicity literature before claiming value.

If positivity fails, classify the mechanism precisely and decide whether it is genuinely distinct from the Assignment-009 catalytic-birth obstruction.

## Pre-registered outcomes

Return exactly one.

### `CONTINUE-STRUCTURALLY-DISTINCT-APPLICATION`

A natural genuinely nonbinary model has a nontrivial patch-positive regime, genuinely activates hidden-mark/killed-factorization structure, and yields a model-specific consequence or precise next theorem not already subsumed by prior work.

### `NARROW-SECOND-APPLICATION-CONSEQUENCE-OPEN`

A natural model is patch positive and genuinely activates the killed typed representation, but one precise unproved multi-state end-factor/order statement blocks the useful consequence. Make that statement the next edge.

### `STOP-SECOND-APPLICATION-POSITIVITY-FAILS`

The literature-selected structurally distinct model fails patch positivity for an exact mechanism. Record whether the obstruction is new or another instance of a broader no-go. Do not open a third application search automatically.

### `STOP-SECOND-APPLICATION-ONLY-KNOWN-DUALITY`

The selected natural model may be patch positive, but the typed construction collapses to a deterministic/standard graphical dual or every useful consequence is already directly known. Do not count it as an application of the surviving novelty anchor.

### `UNRESOLVED-SECOND-APPLICATION`

One explicit symbolic or literature comparison remains unresolved. Record it and stop without moving to `d>3` algebra.

## Anti-loop rules

Do not:

- tune a published transition structure to make positivity hold;
- add noise or refresh before the base model verdict;
- choose a deterministic voter-copy model merely because its transfer rows are nonnegative;
- treat irreducibility as a selection criterion;
- reopen catalytic contact/SIRS variants already decided by the no-go;
- start generic `d>3` coefficient algebra;
- modify `docs/entries/`, `docs/meta/`, or `mkdocs.yml`.

## Durability

Commit immediately after:

- candidate comparison and selected model;
- exact typed specialization;
- positivity verdict;
- application-specific prior-work comparison;
- final model-specific consequence or stop.

Final report:

`students/professor/010-structurally-distinct-application.md`.

Final handoff:

`students/professor/010-handoff.md`.

No writes to `main`.
