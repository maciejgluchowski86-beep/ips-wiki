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
- Latest meeting: `meetings/008-novelty-audit-keeps-killed-typed-factorization.md`.
- Executor: Professor, because no graduate-student session is currently operational.

The principal asks whether the canonical binary patch framework extends to more general IPS: more local states, updates beyond binary flips, corresponding signed duals, a successful-interaction analogue hiding finite local information, generalized patches/positivity, and applications.

## Established mathematical framework

Assignments 001--004 prove, for arbitrary finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis:

1. an exact typed signed Feynman--Kac dual;
2. a successful record `(i,t,r,tau)` revealing source/time/pre-source type/typed target while hiding post-source outcome;
3. one-site typed spacetime patches;
4. an exact killed/noncemetery weighted factorization despite typed target conflicts;
5. an explicit bulk/end patch representation;
6. the exact signed local transfer
   \[
   K_i(0,\cdot)=0,
   \qquad K_i(r,s)=a_{i,r}^s(\emptyset);
   \]
7. typed bulk patch positivity as exact nonnegativity of local matrix-semigroup boundary responses;
8. exact specialization at `d=2` to canonical binary patch positivity.

The crucial multi-state modification is that bare conditioning on the coarse record list is false: an incoming typed-target conflict can enter cemetery and remove future no-record constraints. Since the duality function vanishes at cemetery, multiplying by the noncemetery indicator restores an exact weighted product of local consistency factors.

## Controlled three-state analysis

Assignment 005 proved a genuine structural difference from binary theory. A physically realizable `d=3` model has

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

with positive endpoints but exact interior minimum `-1/1224`; zero/long endpoint inequalities therefore do not characterize general three-state positivity.

Assignment 006 gave a correct finite necessary-and-sufficient spectral test for the remaining boundary-complete `d=3` responses, including all degenerate spectra.

Assignment 007 gave a genuinely nonbinary exchange-symmetric exact subclass. For

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix}
\]

with exchange-symmetric nonempty-target coefficients, boundary-complete typed patch positivity is equivalent to

\[
c\ge a,
\]

and, for every outgoing row `p=(p_0,p_1,p_2)`,

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\qquad
(b+2a)p_0+a(p_1+p_2)\ge0.
\]

These mathematical results remain established. Assignment 008 changes their **contribution status**, not their correctness.

## Assignment 008: novelty and closest-prior-work audit

Outcome: **`CONTINUE-TO-APPLICATIONS`**.

The audit gives a mixed item-by-item verdict rather than a global novelty claim.

### Component statuses

1. finite-state typed signed duality: **`known ingredients, assembly plausibly new`**;
2. killed typed patch factorization / representation: **`plausibly new theorem/mechanism`**;
3. transfer-matrix bulk positivity formulation: **`known ingredients, assembly plausibly new`**;
4. exact boundary-complete `d=3` finite spectral criterion: **`known / directly subsumed`**;
5. exchange-symmetric exact algebraic criterion: **`known ingredients, assembly plausibly new`**;
6. combined generalized patch framework: **`plausibly new theorem/mechanism`**.

### Negative novelty findings that constrain future framing

The literature already contains:

- classical and modern finite-state/product graphical IPS dualities;
- explicit signed finite-type Feynman--Kac duality;
- marked-Poisson ancestor and information-percolation constructions which reveal spacetime dependency geometry before all update randomness is processed;
- Metzler/internal positivity and scalar external positivity `C e^{tA}B>=0`;
- exact third-order real-pole external-positivity / nonnegative-impulse criteria.

In particular the Assignment-006 scalar `d=3` theorem is **directly subsumed** by third-order SISO external-positivity theory: multiplying `p e^{tK}f` by `e^{-dt}` preserves its sign and gives a stable third-order impulse response. It must not be presented as an independent novelty theorem.

### Strongest surviving novelty candidate

No equivalent source was found for the full interface

\[
\text{arbitrary finite-state replacement IPS}
\to
\text{signed typed FK dual}
\to
\text{coarse successful record hiding source outcome}
\]

followed by one-site signed patch averaging in the presence of typed target conflicts, where cemetery makes bare skeleton conditioning nonfactorizable and the exact representation is restored only through the killed/noncemetery weighted product identity.

This mechanism is the primary plausible contribution. Historical priority is **plausible**, not established.

Decisive audit files:

- `research/active/generalized-patch-representations/students/professor/008a-classical-duality-and-graphical-predecessors.md`, commit `e2966ae0`;
- `008b-feynman-kac-and-multistate-duality-comparison.md`, commit `02350f42`;
- `008c-signed-fk-and-hidden-skeleton-factorization.md`, commit `f139fde3`;
- `008d-external-positivity-overlap.md`, commit `41994e79`;
- `008e-component-status-and-chronology.md`, commit `0c91fe66`;
- final report `008-novelty-and-prior-work-audit.md`, commit `6db1efa8`;
- handoff `008-handoff.md`, commit `4524207b`;
- Meeting 008, commit `42719a83`.

## Current proof-spine edge

**Applications of the surviving generalized patch mechanism.**

Per the ordering fixed in Meeting 007 and enforced by Assignment 008, the next active mathematical block must start from a natural genuinely nonbinary finite-state single-site replacement IPS from the literature rather than a tuned coefficient example.

The application block should determine:

1. whether the typed dual/successful-skeleton construction specializes naturally;
2. whether bulk patch positivity actually holds;
3. whether the patch representation yields a useful consequence or structural viewpoint beyond a re-expression of already-known duality;
4. whether that application-specific consequence is new after its own prior-work comparison.

A negative patch-positivity finding is an acceptable outcome if it identifies a real structural obstruction.

## `d>3` ordering

A generic `d>3` tractable-positivity block is **not** next by default. The representation already holds for arbitrary finite `d`, whereas higher-dimensional matrix-response positivity overlaps the established external-positivity problem.

Reopen generic `d>3` criterion work only if:

- a natural application requires more than three local states; or
- a later structured-class opportunity gives independent mathematical value.

## Scope and publication boundary

Current proved mathematical scope: arbitrary finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

Stable current research may be recorded only in the designated branch-only generalized-patch section.

**Do not publish or merge programme content to `main`.**

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` remain outside the active write surface.

All previously stopped programmes remain closed.