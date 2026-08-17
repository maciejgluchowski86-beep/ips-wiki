# Programme state

Date: 2026-08-17

## Active direction

Generalized finite-state patch representations for single-site replacement IPS.

Branch: `research/generalized-patch-representations`.

Workspace: `research/active/generalized-patch-representations/`.

Latest meeting: `meetings/010-potts-metropolis-activates-killed-geometry-but-fails-positivity.md`.

Branch-only wiki section:

- `docs/generalized-patch-representations.md`;
- `docs/generalized-patch-representations/`.

Nothing from this programme is to be written or merged to `main` without later principal instruction.

## Stable representation theorem stack

Assignments 001--004 establish for arbitrary finite-state bounded finite-range **single-site replacement** IPS in the reference-state indicator basis:

1. an exact typed signed Feynman--Kac dual;
2. successful records `(i,t,r,tau)` revealing source/time/pre-source type/typed target while hiding post-source outcome;
3. one-site typed patches;
4. an exact killed/noncemetery weighted factorization despite typed target conflicts;
5. an exact bulk/end patch representation;
6. the exact signed local transfer
   \[
   K_i(0,\cdot)=0,
   \qquad K_i(r,s)=a_{i,r}^s(\emptyset);
   \]
7. typed bulk patch positivity as exact nonnegativity of local matrix-semigroup boundary responses;
8. exact reduction at `d=2` to canonical binary patch positivity.

The essential multistate modification is the cemetery repair: bare conditioning on the coarse record list is false because an incoming incompatible typed target can kill the dual and thereby remove all future no-record constraints. Since the duality function vanishes at cemetery, multiplying by the noncemetery indicator restores an exact weighted product of local consistency factors.

## Three-state positivity analysis

Assignment 005 proves that binary-style zero/long endpoint inequalities do not characterize general `d=3` positivity: a physically realizable response has positive endpoints but exact interior minimum `-1/1224`.

Assignment 006 gives a correct finite necessary-and-sufficient `d=3` spectral test, but Assignment 008 later removes this from the novelty claim because third-order SISO external positivity is direct prior art.

Assignment 007 identifies a genuinely nonbinary exchange-symmetric exact subclass. These results remain mathematical tools but are not the primary contribution claim.

## Assignment 008: novelty ruling

Outcome: **`CONTINUE-TO-APPLICATIONS`**.

Component statuses remain:

1. finite-state typed signed duality: `known ingredients, assembly plausibly new`;
2. killed typed patch factorization / representation: `plausibly new theorem/mechanism`;
3. transfer-matrix bulk positivity formulation: `known ingredients, assembly plausibly new`;
4. exact boundary-complete `d=3` spectral criterion: `known / directly subsumed`;
5. exchange-symmetric exact algebraic criterion: `known ingredients, assembly plausibly new`;
6. combined generalized patch framework: `plausibly new theorem/mechanism`.

The strongest surviving novelty candidate is the interface

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

Historical priority remains plausible rather than established.

## Assignment 009: first natural application

Outcome: **`STOP-APPLICATION-POSITIVITY-FAILS`**.

Krone's two-stage contact process was selected from the literature before any positivity calculation. It genuinely realizes three hidden post-source outcomes and typed cemetery conflicts, but for each adult-neighbor target its source-type-1 outgoing row is

\[
(\lambda,-\lambda,-\lambda).
\]

A realized repeated-source `OO` patch has negative numerator for every finite patch length whenever `lambda>0`. Spatial SIRS gives the same obstruction.

The resulting catalytic-birth no-go is:

> if a positive target mode appears in `0->r` but not in active-source target-mode transitions into `r`, then `a_r^r(tau)<0`; if the source-`r` successful record can repeat after hidden outcome `r`, a realized arbitrarily short `OO` patch is negative.

## Assignment 010: structurally distinct Potts application

Outcome: **`STOP-SECOND-APPLICATION-POSITIVITY-FAILS`**.

### Literature-driven selection

Before any positivity calculation, the programme selected the **three-state zero-field ferromagnetic Potts model with single-spin Metropolis Glauber dynamics** over a three-color cyclic particle system.

The selection used naturality, genuine three-state structure, exact single-site replacement, active-to-active neighbor-sensitive retyping, and the fact that the Metropolis rule is not a deterministic invasion/copy arrow. Irreducibility was not used.

For source color `x`, target color `y!=x`, and neighbor counts `n_a`, write

\[
z=e^{-\beta J},
\qquad q>0.
\]

The continuous-time Poissonized local rates are

\[
\boxed{c^{x\to y}=qz^{(n_x-n_y)_+}.}
\]

### Exact typed specialization

For a typed target with `k_1` color-1 and `k_2` color-2 sites,

\[
\widehat c^{x\to y}_{k_1,k_2}
=
\sum_{i=0}^{k_1}\sum_{j=0}^{k_2}
(-1)^{k_1-i+k_2-j}
\binom{k_1}{i}\binom{k_2}{j}
qz^{(n_x(i,j)-n_y(i,j))_+}.
\]

The complete target-count table is in `010b-potts-metropolis-typed-specialization.md`.

The empty-target signed transfer is

\[
K=q
\begin{pmatrix}
0&0&0\\
z^4&-(z^4+2)&1-z^4\\
z^4&1-z^4&-(z^4+2)
\end{pmatrix}.
\]

For pre-source type `1` and a singleton target-neighbor of color `1`,

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

Thus every `0<z<1` has genuinely nondeterministic hidden outcomes: at least outcomes `0` and `2` carry positive absolute mass. Typed target conflicts are also genuinely realizable, so the killed/noncemetery mechanism is active rather than decorative.

### Exact positivity failure

For the same singleton target,

\[
a_1^2(\tau)
=
\widehat c^{2\to1}(\tau)-\widehat c^{0\to1}(\tau)
=-qz^2(1-z^2)<0.
\]

The physical mechanism is Metropolis saturation:

\[
\widehat c^{0\to1}(\tau)=qz^2(1-z^2)>0,
\qquad
\widehat c^{2\to1}(\tau)=0.
\]

Hidden outcome `2` can be followed by a positive-hazard source-type-2 successful record, so a realized same-source `OO` patch has negative zero-length limit and is negative for all sufficiently short positive lengths.

Therefore

\[
\boxed{
\text{Potts Metropolis is not typed patch positive for any }q>0,\ 0<z<1.}
\]

At `z=1` all nonempty target coefficients vanish; that is neighborhood-independent pure refresh, not an interacting positive regime.

Exact finite gate at

\[
z=1/2,
\qquad q=1,
\qquad t_*=(8/3)\log(5/4)
\]

gives

\[
p=(3/16,5/16,-3/16),
\]

\[
N_{OO}(t_*)=-3884/390625<0.
\]

Verifier: `students/professor/010-potts-metropolis-verifier.py`, commit `34afe2d4`. It is designed for 1,485 exact checks and contains no float literals.

### General short-OO contrast lemma

Assignment 010 broadens the Assignment-009 obstruction.

If active types `r!=s` and a nonempty target `tau` satisfy

\[
\boxed{
a_r^s(\tau)
=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0,}
\]

and hidden outcome `s` is realizable and can feed a subsequent source-`s` successful record at the same site, then a realized arbitrarily short `OO` patch is negative.

This can occur even when every physical state is active and every directed physical replacement has positive rate. Unequal target-mode sensitivity among active source states is enough.

Decisive Assignment-010 files:

- `010a-literature-driven-structural-selection.md`, commit `b56c10d4`;
- `010b-potts-metropolis-typed-specialization.md`, commit `b1b2a995`;
- `010c-potts-metropolis-patch-positivity-obstruction.md`, commit `b4b5eca6`;
- verifier `010-potts-metropolis-verifier.py`, commit `34afe2d4`;
- `010d-potts-prior-work-and-application-value.md`, commit `5ffd0c89`;
- final report `010-structurally-distinct-application.md`, commit `436ce4cf`;
- handoff `010-handoff.md`, commit `39253aba`;
- Meeting 010, commit `939b30e1`.

## Current programme edge

**Opportunity-cost decision: representation-only consequences or close.**

Two materially different natural three-state application architectures have now genuinely activated hidden marks and cemetery conflicts and nevertheless failed typed bulk patch positivity through local realized short-`OO` signs:

1. contact/epidemic birth plus stage/recovery dynamics;
2. fully active symmetric Metropolis retyping.

This substantially lowers the expected value of another search for a natural patch-positive multistate model. No third application search is active.

Generic `d>3` positivity algebra also remains deferred.

If the programme continues after independent verification of Assignment 010, the next scientifically distinct question is whether the killed typed patch **representation itself**, without a bulk-positivity assumption, yields a useful cancellation identity, norm bound, comparison, or other model-independent consequence unavailable from standard graphical/duality methods.

No Assignment 011 is queued. This next step requires an explicit opportunity-cost judgment rather than automatic continuation.

## Scope and publication boundary

Current proved mathematical scope: arbitrary finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

No programme content is to be promoted to `main` without later principal instruction. Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` remain outside the active write surface.

All previously stopped programmes remain closed.
