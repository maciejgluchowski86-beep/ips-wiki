# Assignment 001: finite-state tensor duality and graphical locality

Date: 2026-08-17

Status: active after this file is committed.

The Professor is executing because no graduate-student session is currently operational. This assignment is deliberately bounded and its stop/continue rule is frozen before the mathematics.

## Goal

Determine whether the binary monomial/Feynman--Kac dual from the canonical patch paper has a genuinely local signed analogue for **finite-state single-site replacement IPS**, using the simplest canonical real basis.

This is the algebraic prerequisite for any later generalized successful-interaction skeleton or patch positivity statement.

## Required reading

Read before deriving anything:

- `project-state.md`, `README.md`, `CHATGPT.md`;
- this workspace's `state.md` and `proof-spine.md`;
- `paper/sections/spin-systems.tex`;
- `paper/sections/signed-dual.tex`;
- `paper/sections/patches-body.tex`;
- `paper/appendices/monomial-dual.tex`;
- as expository checks only, the existing `docs/entries/monomial-duality-for-spin-systems.md`, `successful-interaction.md`, and `patch-representation-of-spin-systems.md`.

The paper is authoritative for the binary construction.

## Model class

Let `E={0,1,...,d-1}`, `d>=2`, with distinguished reference state `0`.

For each site `i`, let `N(i)` be finite. Consider the general bounded single-site replacement generator

\[
L f(\eta)
=\sum_i\sum_{x\ne y}
1_{\{\eta_i=x\}}c_i^{x\to y}(\eta_{N(i)})
\bigl[f(\eta^{i,y})-f(\eta)\bigr].
\]

No reversibility, attractiveness, refresh form, or translation invariance is assumed.

Do **not** enlarge to simultaneous multi-site updates in this assignment.

## Part A. Fix the local algebra

Test the reference-state indicator basis

\[
h_0\equiv1,
\qquad
h_a(x)=1_{\{x=a\}},\quad a\in E\setminus\{0\}.
\]

A typed active configuration is a finite partial map

\[
\xi:\Lambda\rightharpoonup E\setminus\{0\},
\]

with

\[
H_\xi(\eta)=\prod_{i\in\operatorname{supp}\xi}h_{\xi(i)}(\eta_i).
\]

Prove explicitly that these `H_xi` form a basis of every finite cylinder algebra.

Define the multiplication/merge operation for typed partial maps. Equal labels at an overlap are idempotent; unequal labels give the zero observable. Decide whether the cleanest dual state space uses a cemetery state `dagger` with `H_dagger=0`, or another equivalent convention.

Expand every neighbour rate `c_i^{x->y}` uniquely in the typed tensor basis on `N(i)`.

## Part B. Derive the generator action exactly

For a typed active source `i` with current dual label `r=xi(i)`, derive the coefficient of each resulting typed monomial produced by an elementary physical transition `x->y` and one typed neighbour-basis term.

The derivation must distinguish at least:

1. physical transitions `r -> y`, `y != r`;
2. physical transitions `x -> r`, `x != r`;
3. `x=0` versus `x != 0` in the second case;
4. compatible versus conflicting overlap between the spawned neighbour target and the pre-existing typed active configuration.

Do not jump directly to a matrix formula. Write the local map on typed configurations.

## Part C. Local signed Feynman--Kac representation

Try to represent the signed coefficients from Part B by nonnegative fixed Poisson rates plus a finite sign/branch mark.

The required locality standard is:

> after the rate functions are expanded, ordinary graphical clocks are indexed only by local data such as `(i, source dual type r, typed target tau, branch mark b)` and have rates independent of the rest of the current dual configuration. The current configuration may determine the deterministic effect of the mark, including compatible merge or transition to the zero/cemetery state, but it must not determine the clock rate.

Identity/no-change coefficients may be placed in a Feynman--Kac potential exactly as in the binary paper.

Prove the generator identity

\[
L_\eta H(Y,\eta)=D H(Y,\eta)+V(Y)H(Y,\eta)
\]

for the proposed signed typed dual `Y`, at least first in finite volume. State the integrability/nonexplosion condition needed for the infinite-volume Feynman--Kac formula; do not oversell it if it needs an additional hypothesis.

A formal transpose of a finite generator matrix is **not** sufficient. The point is the local graphical structure.

## Part D. Binary specialization

Set `d=2` and identify the sole non-reference label with binary activity.

Show line by line how the proposed typed dual reduces to the paper's death/split/birth signed set process, including:

- typed target -> ordinary subset target;
- source deletion/retyping/survival -> binary death/split/birth alternatives;
- sign conventions;
- which empty-target term belongs to the potential.

If the reduction needs a nontrivial regrouping of clocks, state it exactly.

## Part E. First coarse-skeleton feasibility test

Only after Parts A--D succeed, ask the smallest patch-facing question.

Can nonempty-target local clocks be superposed into a coarser successful record which retains

- source site;
- time;
- typed target;

while hiding a **finite branch mark** describing source deletion/retyping/survival, so that the hidden branch can in principle be averaged inside a later patch?

Do not prove patch factorization yet.

The test is whether the coarse record and the current typed dual state determine which site-lines are involved without revealing the hidden branch. If source retyping or target conflicts make even the geometry branch-dependent, isolate the exact obstruction.

## Mandatory finite verifier

Before any broad theorem claim, implement the complete `d=3`, one-neighbour test.

Use `E={0,1,2}` and one source site with one neighbour. Enumerate:

- both active source labels `r in {1,2}`;
- all physical transitions `x->y`, `x != y`;
- all neighbour tensor-basis modes `1, 1_{1}, 1_{2}`;
- compatible and conflicting existing neighbour labels;
- all physical configurations on the two sites.

For every elementary rate-basis atom, compare direct generator action on `H_xi` with the proposed signed-dual local transition identity. Use exact integer/rational arithmetic only.

The verifier must also check the `d=2` reduction separately.

## Pre-registered outcomes

Return exactly one of the following.

### `CONTINUE-TYPED-PATCH`

Parts A--D yield a fixed local signed graphical dual, the finite verifier passes, and Part E identifies a finite hidden branch mark whose omission does not already destroy the successful-interaction geometry. State the precise next bridge: generalized skeleton/factorization, not positivity yet.

### `STOP-NO-LOCAL-GRAPHICAL-DUAL`

The canonical indicator tensor basis gives an exact linear duality but no representation by fixed local graphical clocks satisfying Part C. Give the smallest exact obstruction, preferably in the mandatory `d=3` test. Stop before searching alternative bases.

### `STOP-NO-COARSE-SKELETON`

A fixed local signed graphical dual exists and passes the binary reduction, but the branch mark cannot be hidden while retaining branch-independent successful-interaction geometry even in the bounded `d=3` test. State the exact counterexample and stop before patch factorization.

### `UNRESOLVED-BOUNDED`

The finite-state algebra and test produce a genuine candidate but neither prove the local graphical theorem nor exhibit a decisive obstruction. Record the exact missing identity; do not enlarge the state space/update class.

## Anti-loop rules

Do not:

- switch bases after a negative result inside this block;
- enlarge to block updates;
- call an arbitrary finite-matrix transpose a patch-relevant dual;
- define patch positivity before a coarse skeleton exists;
- hide dependence of clock rates on the current remote dual configuration;
- treat the binary case as evidence for `d>=3` without the mandatory exact test;
- claim novelty before a later literature audit.

## Durability

Commit immediately after any of these becomes durable:

- typed tensor algebra and merge/cemetery convention;
- exact generator-action formula;
- local signed duality theorem or counterexample;
- mandatory finite verifier;
- binary specialization;
- coarse-skeleton feasibility result.

Final report:

`students/professor/001-finite-state-duality.md`.

Final handoff:

`students/professor/001-handoff.md`.

No writes to `main`.
