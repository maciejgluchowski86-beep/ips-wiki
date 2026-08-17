# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

A quantitatively improved instance of an established method does not count as a new project result merely because the calculation is exact or improves a constant. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Active scientific direction

**Generalized patch representations for finite-state interacting particle systems.**

- Branch: `research/generalized-patch-representations`.
- Workspace: `research/active/generalized-patch-representations/`.
- Branch-only wiki hub: `docs/generalized-patch-representations.md`.
- Branch-only wiki section: `docs/generalized-patch-representations/`.
- Latest meeting: `meetings/010-potts-metropolis-activates-killed-geometry-but-fails-positivity.md`.
- Executor: Professor, because no graduate-student session is currently operational.

## Stable generalized representation

Assignments 001--004 establish for arbitrary finite-state bounded finite-range **single-site replacement** IPS in a reference-state indicator tensor basis:

1. an exact typed signed Feynman--Kac dual;
2. successful records `(i,t,r,tau)` hiding post-source outcome;
3. one-site typed spacetime patches;
4. a necessary cemetery-aware killed/noncemetery weighted factorization, because bare conditioning on the coarse skeleton is false;
5. an exact bulk/end patch representation;
6. the signed local transfer
   \[
   K_i(0,\cdot)=0,
   \qquad K_i(r,s)=a_{i,r}^s(\emptyset);
   \]
7. typed bulk patch positivity as exact nonnegativity of local matrix-semigroup boundary responses;
8. exact binary reduction to the canonical patch construction.

The strongest project-specific mechanism is not finite-state duality itself. It is the interface

\[
\text{signed typed dual}
\to
\text{hidden successful skeleton}
\to
\text{typed cemetery obstruction}
\to
\text{killed/noncemetery factorization}
\to
\text{exact finite-state patch representation}.
\]

## Novelty audit

Assignment 008 ended **`CONTINUE-TO-APPLICATIONS`** with mixed component statuses:

1. finite-state typed signed duality: `known ingredients, assembly plausibly new`;
2. killed typed patch factorization / representation: `plausibly new theorem/mechanism`;
3. transfer-matrix bulk positivity: `known ingredients, assembly plausibly new`;
4. exact boundary-complete `d=3` scalar spectral criterion: `known / directly subsumed` by third-order external positivity;
5. exchange-symmetric exact algebraic criterion: `known ingredients, assembly plausibly new`;
6. combined generalized framework: `plausibly new theorem/mechanism`.

Do not claim novelty for finite-state duality, signed FK duality, partial graphical revelation, Metzler semigroups or scalar external positivity individually.

## Assignment 009: two-stage contact / SIRS application

Outcome: **`STOP-APPLICATION-POSITIVITY-FAILS`**.

Krone's two-stage contact process was selected from the literature before any positivity calculation. Its successful record genuinely hides three post-source outcomes and realizes typed cemetery conflicts, but for each adult-neighbor target the source-type-1 outgoing row is

\[
(\lambda,-\lambda,-\lambda).
\]

A realized repeated-source `OO` patch is negative throughout the interacting birth range. Spatial SIRS has the same obstruction.

This yields the catalytic-birth no-go: a positive target mode in `0->r` with no matching active-source target-mode response into `r` creates a negative hidden coefficient which, if it can feed the next outgoing record, forces a negative short patch.

## Assignment 010: structurally distinct Potts application

Outcome: **`STOP-SECOND-APPLICATION-POSITIVITY-FAILS`**.

The second model was again selected before positivity calculation: the **three-state zero-field ferromagnetic Potts model with single-spin Metropolis Glauber dynamics**.

For source color `x`, target `y!=x`, and neighbor counts `n_a`, set

\[
z=e^{-\beta J},
\qquad q>0.
\]

The Poissonized continuous-time local rates are

\[
\boxed{c^{x\to y}=qz^{(n_x-n_y)_+}.}
\]

This is a materially different architecture from Assignment 009: every state is active, every directed color replacement has positive physical rate at finite temperature, and active colors retype each other directly.

### Exact hidden geometry

For source dual type `1` and one target-neighbor of type `1`,

\[
\boxed{
\mathbf a_{1;1,0}
=
\left(
qz^2(1-z^2),
q(z-1)(z^3+z^2-1),
-qz^2(1-z^2)
\right).}
\]

Thus every `0<z<1` has genuinely nondeterministic hidden outcomes. Typed target conflicts are also realizable, so the cemetery-aware killed factorization is genuinely operative. This is not a deterministic voter/cyclic-copy degeneration.

The empty-target transfer is

\[
K=q
\begin{pmatrix}
0&0&0\\
z^4&-(z^4+2)&1-z^4\\
z^4&1-z^4&-(z^4+2)
\end{pmatrix}.
\]

### Exact positivity failure

For the same singleton target,

\[
a_1^2(\tau)
=\widehat c^{2\to1}(\tau)-\widehat c^{0\to1}(\tau)
=-qz^2(1-z^2)<0.
\]

The physical reason is Metropolis saturation: the `0->1` rate responds positively to the extra color-1 neighbor, while `2->1` is already at full acceptance and has zero target-mode increment.

Hidden outcome `2` can be followed by a positive-hazard source-type-2 record. Hence a realized same-source `OO` patch is negative for all sufficiently short positive lengths, and

\[
\boxed{\text{Potts Metropolis is not typed patch positive for any }q>0,\ 0<z<1.}
\]

At the exact gate

\[
z=1/2,
\qquad q=1,
\qquad t_*=(8/3)\log(5/4),
\]

\[
N_{OO}(t_*)=-3884/390625<0.
\]

Verifier: `research/active/generalized-patch-representations/students/professor/010-potts-metropolis-verifier.py`, commit `34afe2d4`; designed for 1,485 exact checks and zero float literals.

### General short-OO contrast lemma

The Potts calculation broadens Assignment 009's obstruction:

> if active types `r!=s` and nonempty target `tau` satisfy
> \[
> a_r^s(\tau)=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0,
> \]
> hidden outcome `s` is realizable, and a source-`s` successful record can follow, then a realized arbitrarily short `OO` patch is negative.

This can occur even with no vacancy state and with every directed physical replacement positive.

Decisive Assignment-010 commits:

- selection `b56c10d4`;
- typed specialization `b1b2a995`;
- positivity obstruction `b4b5eca6`;
- verifier `34afe2d4`;
- prior-work/application ruling `5ffd0c89`;
- final report `436ce4cf`;
- handoff `39253aba`;
- Meeting 010 `939b30e1`.

## Current proof-spine edge

**No third positivity-driven application is active.**

Assignments 009 and 010 tested two materially different natural three-state architectures. Both genuinely activate hidden marks and cemetery conflicts; both fail typed bulk positivity through realized short `OO` signs. This lowers the expected value of another model search based on hoping to satisfy the positivity property.

Generic `d>3` positivity algebra also remains deferred.

If the programme continues after independent verification of Assignment 010, the next scientifically distinct question is whether the **killed typed patch representation itself** yields a useful cancellation identity, norm estimate, finite-volume formula, or comparison **without** assuming all bulk patches are nonnegative.

No Assignment 011 is queued. Continuation now requires an explicit opportunity-cost decision rather than automatic model search.

## Scope and publication boundary

Current proved general scope: arbitrary finite-state bounded finite-range single-site replacement dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

Stable research may be recorded only in the designated branch-only generalized-patch section.

**Do not publish or merge programme content to `main`.**

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` remain outside the active write surface.

All previously stopped programmes remain closed.
