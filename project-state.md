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
- Latest meeting: `meetings/009-natural-contact-and-sirs-applications-fail-positivity.md`.
- Executor: Professor, because no graduate-student session is currently operational.

The principal asks whether the canonical binary patch framework extends to more general IPS: more local states, updates beyond binary flips, corresponding signed duals, a successful-interaction analogue hiding finite local information, generalized patches/positivity, and applications.

## Established generalized framework

Assignments 001--004 prove, for arbitrary finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis:

1. an exact typed signed Feynman--Kac dual;
2. successful records `(i,t,r,tau)` hiding post-source outcome;
3. exact killed/noncemetery patch factorization despite typed target conflicts;
4. an explicit bulk/end patch representation;
5. exact signed local transfer
   \[
   K_i(0,\cdot)=0,
   \qquad K_i(r,s)=a_{i,r}^s(\emptyset);
   \]
6. typed bulk patch positivity as exact nonnegativity of local semigroup boundary responses;
7. exact specialization at `d=2` to canonical binary patch positivity.

The crucial multi-state modification is that bare conditioning on the coarse record list is false: an incoming typed-target conflict can enter cemetery and remove future no-record constraints. Since the duality function vanishes at cemetery, multiplying by the noncemetery indicator restores exact weighted local factorization.

## Three-state positivity analysis

Assignment 005 proves that binary-style endpoint inequalities do not characterize general three-state positivity: a physically realizable response has positive endpoints but exact negative interior minimum `-1/1224`.

Assignment 006 gives a correct finite necessary-and-sufficient spectral test for boundary-complete `d=3`, but Assignment 008 later removes it from the novelty claim because third-order external positivity is direct prior art.

Assignment 007 gives a genuinely nonbinary exchange-symmetric exact subclass. For

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix},
\]

boundary-complete typed patch positivity is equivalent to

\[
c\ge a,
\]

and, for every outgoing row `p=(p_0,p_1,p_2)`,

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\qquad
(b+2a)p_0+a(p_1+p_2)\ge0.
\]

These remain correct mathematical tools but are not the primary novelty claim.

## Assignment 008: novelty audit

Outcome: **`CONTINUE-TO-APPLICATIONS`**.

Component statuses:

1. finite-state typed signed duality: `known ingredients, assembly plausibly new`;
2. killed typed patch factorization / representation: `plausibly new theorem/mechanism`;
3. transfer-matrix bulk positivity formulation: `known ingredients, assembly plausibly new`;
4. exact boundary-complete `d=3` spectral criterion: `known / directly subsumed`;
5. exchange-symmetric exact algebraic criterion: `known ingredients, assembly plausibly new`;
6. combined generalized patch framework: `plausibly new theorem/mechanism`.

The strongest surviving novelty candidate is the full interface

\[
\text{signed typed dual}
\to
\text{hidden successful skeleton}
\to
\text{typed cemetery obstruction}
\to
\text{killed/noncemetery patch factorization}
\to
\text{exact finite-state patch representation}.
\]

Historical priority remains plausible rather than established.

## Assignment 009: natural nonbinary application

Outcome: **`STOP-APPLICATION-POSITIVITY-FAILS`**.

### Selected model

Krone's two-stage contact process was selected from the literature **before** positivity calculation, against spatial SIRS and Neuhauser's multitype contact process.

States and rates:

\[
0=\text{vacant},\quad1=\text{juvenile},\quad2=\text{adult},
\]

\[
0\to1\text{ at }\lambda n_2,
\quad1\to2\text{ at }\gamma,
\quad1\to0\text{ at }1+\delta,
\quad2\to0\text{ at }1.
\]

The model is genuinely three-state and single-site replacement. Irreducibility was not used in selection.

### Typed specialization

For every adult-neighbour target `tau`,

\[
\boxed{\mathbf a_{1,\tau}=(\lambda,-\lambda,-\lambda).}
\]

The successful record hides post-source outcomes `0,1,2` with signs `+,-,-`. Incoming adult target type `2` can conflict with an existing juvenile active label, so the typed cemetery mechanism and killed-factorization repair are genuinely realized in this natural model.

The signed interior transfer is

\[
K=
\begin{pmatrix}
0&0&0\\
0&-(1+\delta+\gamma)&0\\
0&\gamma&-1
\end{pmatrix}.
\]

### Exact positivity failure

A same-source outgoing-to-outgoing bulk descriptor is realized. Its numerator satisfies

\[
N_{OO}(0)=-\lambda,
\]

and in fact

\[
N_{OO}(t)<0
\]

for every finite patch length whenever `lambda>0`; the killed-reference denominator is strictly positive.

Thus the two-stage contact process is **not typed patch positive anywhere in its interacting birth range**.

At the exact gate point

\[
\lambda=\gamma=\delta=1,
\qquad e^{-t}=1/2,
\]

\[
N_{OO}=-5/16,
\qquad D_{OO}=5/16,
\qquad C_{OO}=-1.
\]

Verifier: `research/active/generalized-patch-representations/students/professor/009-two-stage-application-verifier.py`, commit `d2576053`.

### Catalytic-birth no-go

A bounded second candidate, spatial SIRS, has the same obstruction. Assignment 009 therefore isolates a reusable local filter:

> if a positive nonempty target mode appears in `0->r` but not in active-source transitions into `r`, then `a_r^r(tau)<0`; if the same source-`r` successful record can repeat after hidden outcome `r`, a realized arbitrarily short `OO` patch is negative.

This rules out a broad family of contact/epidemic catalytic-birth applications before any spectral analysis.

### Application-specific prior work

The two-stage process already has strong Krone/Foxall/Sturm--Swart multitype duality and complete-convergence theory. The typed killed-patch representation is genuinely different and nonvacuous, but the bulk positivity failure prevents a new patch-positive comparison or convergence theorem for the base model.

Decisive files:

- `research/active/generalized-patch-representations/students/professor/009a-literature-driven-model-selection.md`, commit `56ba8390`;
- `009b-two-stage-typed-specialization.md`, `232fe276`;
- `009c-two-stage-patch-positivity-obstruction.md`, `0174a59b`;
- verifier `009-two-stage-application-verifier.py`, `d2576053`;
- `009d-second-candidate-sirs-check.md`, `db0746f7`;
- `009e-two-stage-prior-work-and-application-value.md`, `423bee8e`;
- final report `009-natural-nonbinary-application.md`, `3d092827`;
- handoff `009-handoff.md`, `8d5305ed`;
- Meeting 009, `d9e8923b`.

## Current proof-spine edge

**One structurally distinct non-catalytic application architecture, if the programme continues.**

Repeating contact/SIRS-style catalytic-birth variants is now low-value because the no-go lemma decides them locally.

A next bounded application block should select, from the literature and before any positivity calculation, a genuinely three-state single-site replacement IPS in which neighbour interactions can retype already-active states or otherwise contain compensating active-source target modes.

The model must not be chosen because its coefficients satisfy patch positivity. A deterministic colored/voter reformulation whose duality is already entirely standard would also not be enough.

Generic `d>3` positivity algebra remains deferred. The representation already holds for arbitrary finite `d`.

## Scope and publication boundary

Current proved mathematical scope: arbitrary finite-state bounded finite-range single-site replacement dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

Stable current research may be recorded only in the designated branch-only generalized-patch section.

**Do not publish or merge programme content to `main`.**

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` remain outside the active write surface.

All previously stopped programmes remain closed.