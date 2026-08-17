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
- Latest meeting: `meetings/006-exact-three-state-spectral-criterion.md`.
- Executor: Professor, because no graduate-student session is currently operational.

The principal asks whether the canonical binary patch-positivity framework extends to more general IPS: more local states, updates beyond binary flips, corresponding signed duals, a successful-interaction analogue hiding finite local information, generalized patches/positivity, and applications.

## Established generalized structure

Assignments 001--004 established, for finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis:

1. an exact typed signed Feynman--Kac dual;
2. a typed successful skeleton revealing `(i,t,r,tau)` and hiding post-source outcome;
3. exact killed/noncemetery patch factorization despite typed target conflicts;
4. an explicit typed patch representation with bulk/end separation;
5. the exact local bulk transfer
   \[
   K_i(0,\cdot)=0,
   \qquad K_i(r,s)=a_{i,r}^s(\emptyset);
   \]
6. typed bulk patch positivity as exact nonnegativity of finitely parameterized semigroup numerator families built from `e^{tK_i}`;
7. exact reduction at `d=2` to the canonical binary patch-positivity coefficient criterion.

## Assignment 005: endpoint-only `d=3` criterion fails

Outcome: **`STOP-NO-FINITE-ENDPOINT-CRITERION`**.

Under boundary completeness, `K` is forced Metzler. Incoming-initial and `OO` families then become automatic after their zero-length constraints. Only `OI` remains.

A genuine one-neighbour physical IPS gives

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

with positive endpoints

\[
N(0)=1,
\qquad N(\infty)=1/128,
\]

but exact interior minimum

\[
e^{-t_*}=13/153,
\qquad N(t_*)=-1/1224.
\]

Thus binary-style zero-length plus long-time inequalities do not characterize three-state positivity. The exact semigroup property and binary theory remain intact.

## Assignment 006: exact finite spectral criterion

Outcome: **`CONTINUE-EXACT-THREE-STATE-SPECTRAL-CRITERION`**.

For boundary-complete `d=3`, every remaining `OI` numerator admits a finite exact spectral test.

If the active eigenvalues are distinct and negative,

\[
-\mu,-\nu,
\qquad0<\mu<\nu,
\]

then

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t}.
\]

The coefficients are obtained from local transfer data without eigenvectors:

\[
P_0=\frac{(K+\mu I)(K+\nu I)}{\mu\nu},
\quad L=uP_0f,
\quad n_0=uf,
\quad n_1=uKf,
\]

\[
A=\frac{\nu(n_0-L)+n_1}{\nu-\mu},
\qquad
B=\frac{-\mu(n_0-L)-n_1}{\nu-\mu}.
\]

There is at most one interior minimum. It occurs exactly when

\[
A<0<B,
\qquad
0<R=-\frac{\mu A}{\nu B}<1,
\]

and then

\[
\boxed{
N(t_*)
=L+\frac{\nu-\mu}{\nu}
A R^{\mu/(\nu-\mu)}.}
\]

Thus each generic descriptor is decided by zero-length, long-time, and at most one critical-value check.

All degenerate spectra are also finite:

- one zero active eigenvalue: one decaying mode;
- repeated nonzero diagonalizable active block: one decaying mode;
- repeated nonzero Jordan block:
  \[
  N(t)=L+(A+Bt)e^{-\mu t},
  \]
  again with at most one interior minimum;
- reducible reference-neighbour chains introduce no additional time-dependence class.

The mandatory exact verifier reproduces the Assignment-005 negative minimum and verifies a separate physically realizable boundary-complete `p_0<0` positive row

\[
p=(-1/8,9/8,3/8)
\]

with nontrivial minimum

\[
e^{-t_*}=5/51,
\qquad N(t_*)=15/544>0.
\]

Suppressing type `2` removes the interior-critical branch and recovers exactly the canonical binary coefficient inequalities.

Decisive files:

- `research/active/generalized-patch-representations/students/professor/006a-generic-two-mode-critical-criterion.md`, commit `e79a94a5`;
- `006b-degenerate-spectral-cases.md`, commit `96127a9b`;
- verifier `006-three-state-spectral-verifier.py`, commit `419196b4`;
- `006c-finite-spectral-criterion-and-usability.md`, commit `54334311`;
- `006d-binary-spectral-reduction.md`, commit `93dad82b`;
- final report `006-three-state-spectral-criterion.md`, commit `5957a9cf`;
- handoff `006-handoff.md`, commit `23488674`;
- Meeting 006, commit `80f51dc6`.

## Current proof-spine edge

**Natural simplification / structural subclass for the exact three-state spectral criterion.**

The criterion is genuinely finite but not generally a purely algebraic coefficient cone: the generic critical value retains

\[
R^{\mu/(\nu-\mu)}.
\]

The next bounded problem is to identify a mathematically natural non-binary subclass in which the exact critical inequality becomes algebraic, monotone, or otherwise transparent, and prove necessity and sufficiency within that subclass while preserving exact binary reduction.

Applications and convergence remain downstream and are not active.

## Scope, novelty and publication boundary

Current proved general scope: finite-state bounded finite-range single-site replacement dynamics in the reference-state indicator tensor basis.

The finite spectral criterion is currently proved for the controlled boundary-complete `d=3` class.

Simultaneous multi-site physical updates remain outside scope.

No literature novelty claim has yet been made. A targeted literature audit remains necessary once the theorem package is stable enough to compare precisely.

Stable current research may be recorded only in the designated branch-only generalized-patch wiki section.

**Do not publish or merge any programme content to `main`.**

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` are outside the active write surface.

All previously stopped programmes remain closed.
