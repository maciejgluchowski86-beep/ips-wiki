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
- Latest meeting: `meetings/007-natural-three-state-subclass.md`.
- Executor: Professor, because no graduate-student session is currently operational.

The principal asks whether the canonical binary patch-positivity framework extends to more general IPS: more local states, updates beyond binary flips, corresponding signed duals, a successful-interaction analogue hiding finite local information, generalized patches/positivity, and applications.

## Established generalized structure

Assignments 001--004 establish for arbitrary finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis:

1. an exact typed signed Feynman--Kac dual;
2. a successful record `(i,t,r,tau)` hiding post-source outcome;
3. exact killed/noncemetery patch factorization despite typed target conflicts;
4. an explicit typed patch representation with bulk/end separation;
5. exact local transfer
   \[
   K_i(0,\cdot)=0,
   \qquad K_i(r,s)=a_{i,r}^s(\emptyset);
   \]
6. typed bulk patch positivity as exact nonnegativity of local semigroup numerator families;
7. exact reduction at `d=2` to canonical binary patch positivity.

## Three-state criterion programme

### Assignment 005

Outcome: **`STOP-NO-FINITE-ENDPOINT-CRITERION`**.

A genuine `d=3` physical IPS has a required `OI` numerator with positive zero/long endpoints but exact negative interior minimum `-1/1224`. Thus binary-style endpoint inequalities do not characterize general three-state positivity.

### Assignment 006

Outcome: **`CONTINUE-EXACT-THREE-STATE-SPECTRAL-CRITERION`**.

Boundary-complete `d=3` typed bulk patch positivity has a finite necessary-and-sufficient spectral test. Every remaining `OI` numerator requires zero-length, long-time, and at most one explicitly computed interior critical-value check. Zero-eigenvalue, repeated, Jordan, and reducible cases are all handled exactly. Binary suppression is exactly canonical.

### Assignment 007

Outcome: **`CONTINUE-NATURAL-THREE-STATE-SUBCLASS`**.

For active-label exchange-symmetric reference-neighbour dynamics

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix},
\]

with exchange-symmetric nonempty-target coefficient family, boundary completeness gives the necessary Metzler condition

\[
\boxed{c\ge a.}
\]

Then typed bulk patch positivity is equivalent to the algebraic conditions, for every outgoing row `p=(p0,p1,p2)`,

\[
\boxed{
p_1,p_2,p_0+p_1,p_0+p_2\ge0,}
\]

\[
\boxed{(b+2a)p_0+a(p_1+p_2)\ge0.}
\]

This is necessary and sufficient inside the subclass.

The simplification is genuinely non-binary: the exact gate has `p_1!=p_2`, distinct active-state `OI` values, positive physical `1<->2` transitions, and target-dependent perturbations distinguishing active labels. The mechanism is ordered symmetric/antisymmetric decay, not quotienting.

Other Assignment-007 findings:

- lumpable dynamics plus lumped observables is exact but observably binary-reducible;
- one-way active retyping remains genuinely spectral;
- destination-rate refresh chains give a repeated-spectrum sibling subclass with exact one-mode criterion.

Decisive files:

- `research/active/generalized-patch-representations/students/professor/007a-lumpability-classification.md`, commit `6c41149d`;
- corrected `007b-symmetry-and-refresh-subclass.md`, commit `52e9e7ac`;
- `007c-triangular-still-spectral.md`, commit `c692967d`;
- verifier `007-natural-subclass-verifier.py`, commit `3a12ba34`;
- `007d-exact-subclass-criterion-and-binary-reduction.md`, commit `06199715`;
- final report `007-natural-spectral-simplification.md`, commit `5f9b4b8b`;
- handoff `007-handoff.md`, commit `d465af1d`;
- Meeting 007, commit `a22c87e4`.

## Current proof-spine edge

**Targeted novelty/closest-prior-work audit.**

The theorem stack is now stable enough to compare precisely with prior literature. No novelty claim is authorized until this audit is complete.

The audit should cover the arbitrary-finite-state typed dual and killed patch factorization, the exact transfer positivity formulation, the `d=3` finite spectral theorem, and the exchange-symmetric / refresh exact subclasses, including alternate terminology.

## Planned ordering after the audit

If the literature audit does not show that the generalized mechanism or criterion is already subsumed by prior work, **applications become the next active mathematical block immediately**.

The first application should be a genuinely non-binary finite-state single-site replacement IPS checked against either the symmetric/refresh algebraic criterion or the exact `d=3` spectral criterion.

A generic `d>3` tractable-positivity block is not next by default. The representation already covers arbitrary finite `d`. Further `d>3` criterion work should be activated only if:

- a concrete application naturally needs more than three local states; or
- the literature audit shows that the arbitrary-`d` criterion itself is the distinctive theorem worth developing.

This ordering is intended to prevent the principal's application question from receding indefinitely.

## Scope and publication boundary

Current proved general scope: arbitrary finite-state bounded finite-range single-site replacement dynamics in the reference-state indicator tensor basis. Tractable coefficient-level positivity is strongest in boundary-complete `d=3` and the exchange-symmetric / refresh subclasses.

Simultaneous multi-site physical updates remain outside scope.

Stable current research may be recorded only in the designated branch-only generalized-patch wiki section.

**Do not publish or merge any programme content to `main`.**

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` are outside the active write surface.

All previously stopped programmes remain closed.
