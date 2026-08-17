# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Active scientific direction

**Generalized patch representations and patch positivity for interacting particle systems.**

- Branch: `research/generalized-patch-representations`.
- Workspace: `research/active/generalized-patch-representations/`.
- Branch-only wiki hub: `docs/generalized-patch-representations.md`.
- Branch-only wiki section: `docs/generalized-patch-representations/`.
- Latest meeting: `meetings/001-finite-state-typed-duality-opens-patch-factorization.md`.
- Next bounded assignment: `students/professor/assignment-002-typed-patch-factorization.md`, queued but not yet executed.
- Executor: Professor, because no graduate-student session is currently operational.

The principal has superseded the previous direction and asked whether the patch-positivity paper can be extended to more general IPS: more than two local states, updates beyond flips, a corresponding signed dual process, a successful-interaction analogue which reveals a coarse spacetime skeleton while hiding a finite local mark, generalized patches and patch positivity, and applications.

The core mechanism to preserve is conditional averaging of hidden local marks inside spacetime patches before signed contributions are compared.

## Canonical binary benchmark

For the existing construction, the manuscript under `paper/`, *Patch representations and convergence for facilitated spin systems*, is authoritative. Existing patch wiki pages under `docs/entries/` remain expository source material and are not being generalized in place.

## Assignment 001: finite-state typed duality

Outcome: **`CONTINUE-TYPED-PATCH`**.

For finite local state space `E={0,...,d-1}` with reference state `0`, the indicator tensor basis

$$
h_0\equiv1,
\qquad h_a(x)=1_{\{x=a\}},\quad a\ne0,
$$

produces typed active configurations and spans every finite cylinder algebra.

For general bounded single-site replacement dynamics, expansion of the neighbour rates gives exact source-outcome coefficients

$$
a_{i,r}^{0}(\tau)=\widehat c_i^{0\to r}(\tau),
$$

$$
a_{i,r}^{s}(\tau)=\widehat c_i^{s\to r}(\tau)-\widehat c_i^{0\to r}(\tau),
\quad s\ne0,r,
$$

$$
a_{i,r}^{r}(\tau)
=-\widehat c_i^{0\to r}(\tau)-\sum_{y\ne r}\widehat c_i^{r\to y}(\tau).
$$

Their absolute values are fixed local Poisson rates; signs are sign marks. The source outcome deletes, preserves, or retypes the source. Typed target conflicts go to a cemetery/zero state but do not alter clock rates.

The empty-target source-survival coefficient is placed in the Feynman--Kac potential, giving an exact local graphical generator duality. The `d=2` specialization is exactly the canonical death/split/birth dual.

For nonempty typed target `tau`, the first successful-interaction record is

$$
(i,t,r,\tau),
$$

retaining the pre-interaction source type and typed target while hiding the post-interaction source outcome. All hidden outcomes have the same interaction endpoints, so one-site patch geometry passes the first gate.

Decisive files:

- `students/professor/001a-typed-generator-action.md`;
- `students/professor/001b-signed-typed-dual.md`;
- `students/professor/001c-coarse-typed-skeleton.md`;
- exact verifier `students/professor/001-finite-state-duality-verifier.py`, final commit `c8e47458`;
- final report `students/professor/001-finite-state-duality.md`, commit `2f37d6bf`;
- handoff `students/professor/001-handoff.md`, commit `6bdd26ef`.

The result is not yet literature-audited for novelty.

## Current proof-spine edge

**Typed successful-skeleton conditional factorization.**

The next theorem must decide whether conditioning on typed successful records still decomposes hidden marks into independent source--time-strip patch laws.

The main new issue is incoming typed-target compatibility. If target type `a` arrives at a site whose current local dual type is a different `b`, the merge hits cemetery and the global dual contribution becomes zero. Assignment 002 must decide whether such conflict histories can be represented by local zero factors / weighted factorization, or whether they create genuine cross-patch dependence.

Patch positivity is downstream and is not yet defined.

## Wiki and publication boundary

The research loop may keep stable notation and constructions in the **separate branch-only wiki section** `docs/generalized-patch-representations/`.

**Do not publish or merge any of this programme to `main`.** Main is outside the active write surface.

## Previous directions

The principal's new direction supersedes the previously active voter-discordance work and every queued publication/merge question.

Previously stopped positive-rates, FA-1f, BABP, noisy-East, voter-concentration, PDE and other recorded programmes remain closed at their existing rulings. This programme does not reopen them by analogy or reuse of terminology.
