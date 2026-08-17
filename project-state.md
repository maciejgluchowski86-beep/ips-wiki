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
- Current bounded assignment: `research/active/generalized-patch-representations/students/professor/assignment-001-finite-state-duality.md`.
- Executor: Professor, because no graduate-student session is currently operational.

The principal has superseded the previous direction and asked whether the patch-positivity paper can be extended to more general IPS: more than two local states, updates beyond flips, a corresponding signed dual process, a successful-interaction analogue which reveals a coarse spacetime skeleton while hiding a finite local mark, generalized patches and patch positivity, and applications.

The core mechanism to preserve is conditional averaging of hidden local marks inside spacetime patches before signed contributions are compared.

## Canonical binary benchmark

For the existing construction, the manuscript under `paper/`, *Patch representations and convergence for facilitated spin systems*, is authoritative.

The first block uses especially:

- `paper/sections/spin-systems.tex`;
- `paper/sections/signed-dual.tex`;
- `paper/sections/patches-body.tex`;
- `paper/sections/representation.tex`;
- `paper/sections/patch-positivity.tex`;
- `paper/appendices/monomial-dual.tex`.

The existing patch wiki pages under `docs/entries/` remain source/expository material. They are not being rewritten in place.

## First proof-spine edge

For a finite local state space `E={0,...,d-1}` with reference state `0`, test the one-site basis

$$
h_0\equiv1,
\qquad
h_a(x)=1_{\{x=a\}},\quad a\ne0,
$$

and the tensor observables indexed by finite typed active configurations.

For general bounded single-site replacement dynamics

$$
L f(\eta)
=\sum_i\sum_{x\ne y}1_{\{\eta_i=x\}}c_i^{x\to y}(\eta_{N(i)})
\bigl[f(\eta^{i,y})-f(\eta)\bigr],
$$

the first question is whether expansion of the neighbour rates in this tensor basis gives a **fixed local signed Feynman--Kac graphical dual** on typed active configurations. The locality standard is stronger than abstract finite-dimensional duality: Poisson clock rates must depend only on local event data, not on the rest of the current dual configuration.

The mandatory bounded stress test is `d=3` with one neighbour, including compatible and conflicting typed overlaps, together with an exact `d=2` specialization back to the paper.

Only after this layer is settled may the programme define a generalized successful-interaction skeleton or patch positivity.

## Wiki and publication boundary

The principal explicitly permits the research loop to keep and refine results in a **separate wiki section on the research branch**. Raw mathematics remains under the research workspace; stable notation/constructions may be copied into `docs/generalized-patch-representations/` on this branch.

**Do not publish or merge any of this programme to `main`.** Main was deliberately restored by the principal to the pre-research-loop tree and is outside the active write surface.

## Previous directions

The principal's new direction supersedes the previously active voter-discordance work and every queued publication/merge question.

Previously stopped positive-rates, FA-1f, BABP, noisy-East, voter-concentration, PDE and other recorded programmes remain closed at their existing rulings. This programme does not reopen them by analogy or reuse of terminology.
