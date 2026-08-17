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
- Latest meeting: `meetings/005-three-state-endpoint-criterion-obstructed.md`.
- Executor: Professor, because no graduate-student session is currently operational.

The principal asks whether the canonical patch-positivity framework extends to more general IPS: more local states, updates beyond binary flips, corresponding signed duals, a successful-interaction analogue hiding finite local information, generalized patches/positivity, and applications.

The core mechanism is conditional averaging of hidden local marks inside spacetime patches before signed contributions are compared.

## Established generalized structure

### Assignment 001: finite-state typed duality

Outcome: **`CONTINUE-TYPED-PATCH`**.

For finite `E={0,...,d-1}` with reference state `0`, the indicator tensor basis gives typed active configurations and an exact fixed-local-clock signed Feynman--Kac dual for bounded finite-range single-site replacement IPS. Successful nonempty records reveal source/time/pre-source type/typed target and hide post-source outcome.

### Assignment 002: typed patch factorization

Outcome: **`CONTINUE-TYPED-REPRESENTATION`**.

Bare conditioning fails because incoming typed conflicts can hit cemetery and remove future no-record constraints. Since `H_dagger=0`, the killed/noncemetery weighted factorization is exact and sufficient for the semigroup representation.

### Assignment 003: explicit typed patch representation

Outcome: **`CONTINUE-TYPED-POSITIVITY`**.

Bulk contributions are

\[
C(P)=E_P^{con}[A_P]
\]

and are independent of terminal physical data. End contributions are one-site functions in the same indicator basis. The exact killed-skeleton semigroup representation is proved and specializes exactly to the canonical binary representation.

### Assignment 004: typed bulk transfer and exact positivity property

Outcome: **`CONTINUE-TYPED-POSITIVITY-CRITERION`**.

For active local type `r`, the weighted killed Feynman--Kac transfer has the exact finite generator

\[
K_i(0,\cdot)=0,
\qquad
K_i(r,s)=a_{i,r}^s(\emptyset).
\]

For terminal columns

\[
f_b^I=e_0^T+e_b^T,
\qquad
f_r^O=e_r^T,
\]

and outgoing initial row

\[
\mathbf a_{r,\tau}=(a_{i,r}^s(\tau))_{s\in E},
\]

typed bulk patch positivity is exactly nonnegativity of

\[
e_a e^{tK_i}f_b^I,
\qquad
e_a e^{tK_i}f_r^O,
\]

\[
\mathbf a_{r,\tau}e^{tK_i}f_b^I,
\qquad
\mathbf a_{r,\tau}e^{tK_i}f_{r_e}^O
\]

for every realizable descriptor and every `t>0`.

The binary specialization recovers exactly the canonical coefficient criterion; no stronger generalized definition is substituted.

### Assignment 005: boundary-complete three-state endpoint criterion

Outcome: **`STOP-NO-FINITE-ENDPOINT-CRITERION`**.

Boundary completeness forces the three-state empty-target transfer `K` to be Metzler. Hence all incoming-initial families are automatic. For an outgoing row

\[
p=(p_0,p_1,p_2),
\]

zero-length conditions force

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\]

which also makes every `OO` family automatic.

The remaining `OI` numerator has the exact physical Markov representation

\[
p e^{tK}f_b^I=E_b[g(Z_t)],
\qquad
 g=(p_0,p_0+p_1,p_0+p_2),
\]

where `Z` is the physical one-site chain with neighbours frozen in the reference state.

A genuine one-neighbour three-state IPS gives

\[
Q=
\begin{pmatrix}
-1/4&0&1/4\\
7/4&-2&1/4\\
1/4&1/2&-3/4
\end{pmatrix},
\qquad
K=
\begin{pmatrix}
0&0&0\\
0&-2&1/2\\
1/4&0&-1
\end{pmatrix}.
\]

For one boundary-complete outgoing row

\[
p=(-1/8,9/8,1/4),
\qquad
 g=(-1/8,1,1/8),
\]

the required `OI` numerator is

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}.
\]

Although

\[
N(0)=1,
\qquad N(\infty)=1/128,
\]

at

\[
e^{-t_*}=13/153
\]

one has

\[
N(t_*)=-1/1224.
\]

Thus zero-length and long-time endpoint inequalities do not characterize three-state typed patch positivity even under boundary completeness.

Suppressing type `2` recovers exactly the canonical binary inequalities, so this is not a binary mismatch.

Final verifier: `students/professor/005-three-state-endpoint-obstruction-verifier.py`, commit `fc8c999e`.

Final report: `students/professor/005-three-state-positivity-criterion.md`, commit `027bcbf8`.

Meeting 005: commit `ee43807e`.

## Current proof-spine edge

**Exact spectral critical-point criterion retaining the interior mode.**

The endpoint-only route is stopped, but in boundary-complete `d=3` every generic remaining `OI` numerator is a two-mode expression

\[
L+A e^{-\mu t}+B e^{-\nu t}.
\]

The next bounded question is whether endpoint conditions plus the exact possible interior critical-value inequality give a useful finite necessary-and-sufficient spectral criterion. This is materially different from the refuted binary-style endpoint collapse.

Applications and convergence remain downstream and are not active.

## Scope, novelty and publication boundary

Current proved scope: finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis.

Simultaneous multi-site physical updates remain outside scope.

No literature novelty claim has yet been made for the generalized theorem. A targeted literature audit remains necessary once a criterion-level theorem is stable enough to compare precisely.

Stable current research may be recorded only in the designated branch-only generalized-patch wiki section.

**Do not publish or merge any programme content to `main`.**

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` are outside the active write surface.

All previously stopped programmes remain closed and are not reopened by this direction.
