# Student G Assignment 004: coupling, interfaces, duals, and graphical limits

Read before working: root `project-state.md`, `README.md`, `CHATGPT.md`; `research/active/ergodicity-methods-toolbox/state.md`, `proof-spine.md`, Meeting 012, `entry-template.md`, your `handoff-003.md`, and the live toolbox hub `docs/ergodicity-methods.md`.

## Objective

Fill seven graphical/coupling interfaces that remain genuinely distinct after the first four waves. Several targets are deliberately narrow and model-specific. Preserve that specificity rather than translating everything into generic coupling language.

Do not force seven entries. If primary-source inspection shows that a target is already represented by a live proof interface, record that result and substitute another uncovered source-supported method.

## Targets

1. **Successful coupling of finite dual particle systems.** Find a theorem where two copies of a finite interacting dual are coupled until they agree, and this successful coupling is used to classify invariant laws or prove convergence of the original IPS. This must be distinct from finite-dual extinction, voter coalescence, and parity duality.

2. **Second-class-particle or shock coupling.** Find a conservative IPS application where a distinguished discrepancy/second-class particle or shock has its own stochastic dynamics and is the load-bearing object in proving convergence, invariant-law classification, stability of shocks, or another ergodic conclusion.

3. **Literal maximal local coupling for a nonmonotone spin system.** The source should construct a maximal or otherwise optimized coupling of local conditional update laws because monotone/basic coupling is unavailable. The resulting local agreement estimate must genuinely drive mixing/convergence, and must be distinct from the live block-resampling and path-coupling pages.

4. **Regeneration of a disagreement or competition interface.** Find a model where the renewal object is a coupling discrepancy, competition interface, or interface between phases and regeneration times yield a long-time law or coupling result. Keep this distinct from the live physical reactive-front regeneration page unless the source shows they are the same mechanism.

5. **Complete convergence via restart/block construction in contact or multitype systems.** Find a primary source where supercritical oriented-percolation/block construction is combined with restart, survival/extinction decomposition, or local coupling to prove complete convergence. The proof interface must be materially distinct from the live Sturm--Swart ADBARW page, whose percolative construction is tied to parity-duality classification.

6. **Boundary-uniform projective graphical transfer.** Find a theorem where finite-volume couplings or backward influence estimates are uniform in boundary conditions and pass to infinite volume to yield uniqueness/convergence. This must be distinct from the live finite-speed equilibrium-semigroup transfer page: the boundary-uniform graphical coupling itself should be the limiting interface.

7. **Nonmonotone Wasserstein/reflection/jump coupling in an infinite interacting system.** Find a source where reflection, synchronous-plus-jump, concave transport cost, or another nontrivial Wasserstein coupling proves contraction/ergodicity for an interacting infinite-dimensional model. It must be distinct from the existing weighted synchronous `W_1` contraction page.

## Taxonomy constraints

Keep the following live interfaces separate unless the primary source forces a correction:

- finite-dual extinction;
- voter coalescing ancestry;
- parity branching-annihilating duality;
- CFTP;
- ancestor-clan perfect simulation;
- information percolation;
- static and dynamical disagreement percolation;
- block coupling by joint resampling;
- weighted synchronous Wasserstein contraction;
- refined non-diagonal exclusion discrepancy coupling;
- physical front regeneration.

A generic common/basic graphical-coupling page remains **unwarranted** by the previous source search. Do not revisit it merely to fill a slot unless a new primary theorem exposes a genuinely separate reusable interface.

## Entry standard

For each successful target, create one file under `research/active/ergodicity-methods-toolbox/entries/` using the current staging template. State the criterion/theorem, mechanism, representative application, limitations, and at least one actually inspected primary source with exact theorem/proposition/lemma/section/page pinpoint and stable URL/DOI/arXiv identifier.

Model-specific methods are explicitly desired. Generic coupling theory qualifies only with a concrete interacting-process application in which that coupling theorem is load-bearing.

If a target collapses into an already-live method or lacks a clean primary application, **do not pad**. Substitute another uncovered graphical/coupling/duality mechanism and document the negative taxonomy decision in the handoff.

## Durability

Mandatory: **commit every finished entry immediately as its own substantive commit.** Do not batch the wave and do not rely on chat as the durable record.

Do not edit `docs/` or `mkdocs.yml`.

At completion, commit `students/student-g/004-handoff.md` with the entry/commit list, source qualifications, taxonomy/substitution decisions, negative searches that should not be repeated, and further uncovered families. Mechanical validation remains the principal/orchestrator's structural check and is not mathematical/source verification.
