# Programme state

Date: 2026-08-17

## Status

**CLOSED deliberately on opportunity-cost grounds.**

Branch: `research/generalized-patch-representations`.

Workspace: `research/active/generalized-patch-representations/`.

Latest meeting: `meetings/011-killed-cancellation-majorant-works-but-programme-stops.md`.

Branch-only wiki section:

- `docs/generalized-patch-representations.md`;
- `docs/generalized-patch-representations/`.

Nothing from this programme is to be written or merged to `main` without later principal instruction.

No Assignment 012 is queued.

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
7. typed bulk patch positivity as nonnegativity of realized local matrix-semigroup boundary responses;
8. exact reduction at `d=2` to canonical binary patch positivity.

The essential multistate modification is the cemetery repair: bare conditioning on the coarse successful-record list is false because a typed conflict can kill the dual and remove all future no-record constraints. Since the duality function vanishes at cemetery, inserting the noncemetery indicator restores exact weighted local factorization.

## Novelty status after Assignment 008

The bounded closest-prior-work audit gives the following contribution-status ruling:

1. finite-state typed signed duality: `known ingredients, assembly plausibly new`;
2. killed typed patch factorization / representation: **`plausibly new theorem/mechanism`**;
3. transfer-matrix bulk positivity: `known ingredients, assembly plausibly new`;
4. exact boundary-complete `d=3` spectral criterion: **`known / directly subsumed`** by third-order SISO external positivity;
5. exchange-symmetric exact algebraic criterion: `known ingredients, assembly plausibly new`;
6. combined generalized framework: **`plausibly new theorem/mechanism`**.

The strongest surviving novelty candidate is

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

Historical priority remains plausible rather than established. Do not claim novelty for finite-state duality, signed FK duality, partial graphical revelation, Metzler semigroups, scalar external positivity, or the Assignment-006 `d=3` spectral theorem individually.

## Three-state positivity analysis

Assignment 005 proves that binary endpoint inequalities do not characterize general `d=3` positivity: a physically realizable response

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

has positive endpoints and exact interior minimum `-1/1224`.

Assignment 006 gives a correct finite exact `d=3` spectral test, but that test is directly subsumed by third-order external-positivity theory and is not a contribution claim.

Assignment 007 identifies a genuinely nonbinary exchange-symmetric exact subclass. It remains a useful calculation, not the primary novelty anchor.

## Assignment 009: two-stage contact / SIRS

Outcome: **`STOP-APPLICATION-POSITIVITY-FAILS`**.

Krone's two-stage contact process was selected before any positivity calculation. Its successful record genuinely hides three post-source outcomes and realizes typed cemetery conflicts, but for each adult-neighbour target its source-type-1 outgoing row is

\[
(\lambda,-\lambda,-\lambda).
\]

A realized repeated-source `OO` patch is negative throughout the interacting birth range. At the exact verified gate

\[
\lambda=\gamma=\delta=1,
\qquad e^{-t}=1/2,
\]

\[
N_{OO}=-5/16,
\qquad D_{OO}=5/16,
\qquad C_{OO}=-1.
\]

Spatial SIRS has the same obstruction.

## Assignment 010: Potts Metropolis

Outcome: **`STOP-SECOND-APPLICATION-POSITIVITY-FAILS`**.

The selected three-state zero-field ferromagnetic Potts single-spin Metropolis dynamics is structurally distinct: every state is active and active colors directly retype.

For a source-type-1 singleton target-type-1 record,

\[
\mathbf a_{1;1,0}
=
\left(
qz^2(1-z^2),
q(z-1)(z^3+z^2-1),
-qz^2(1-z^2)
\right),
\]

so

\[
a_1^2(\tau)=-qz^2(1-z^2)<0
\]

for every interacting finite-temperature point `q>0`, `0<z<1`. Hidden outcome `2` can feed a later source-type-2 record, giving a negative short `OO` patch.

At

\[
z=1/2,
\quad q=1,
\quad t_*=(8/3)\log(5/4),
\]

\[
N_{OO}(t_*)=-3884/390625.
\]

The verified Potts verifier has 1,485 exact checks and zero float literals.

### General short-`OO` contrast lemma

Assignments 009--010 are unified by:

> if active types `r!=s` and a nonempty target `tau` satisfy
> \[
> a_r^s(\tau)=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0,
> \]
> hidden outcome `s` is realizable, and a source-`s` successful record can follow, then a realized arbitrarily short `OO` patch is negative.

This is the structural reason the two natural application architectures fail patch positivity.

## Assignment 011: cancellation without bulk positivity

Outcome: **`STOP-CANCELLATION-NO-QUALITATIVE-GAIN`**.

Assignment 011 was pre-registered as the single final bounded continuation after independent verification of Assignment 010. It did not return to pointwise patch positivity or generic `d>3` algebra.

### Patch-variation kernel

In finite volume let `Q_t` be the exact signed FK kernel and `A_t` the raw absolute-FK kernel. The killed patch representation defines a positive kernel `R_t` by taking absolute values only after each hidden killed-patch expectation. Exactly,

\[
\boxed{|Q_t|\le R_t\le A_t}
\]

entrywise.

The gain is strict on the verified Potts model. At the positive-length gate,

\[
\boxed{
\frac{10178204}{38671875}
<
\frac{17919551}{38671875},}
\]

with gap

\[
\frac{2580449}{12890625}>0.
\]

### Composability

Deterministic time-cut refinement gives

\[
\boxed{R_{t+s}\le R_tR_s}
\]

entrywise. The compatible typed dual configuration at the cut is sufficient boundary memory.

Thus delayed hidden-mark averaging yields a genuine positive submultiplicative majorant, not merely a local triangle inequality.

### Renewal/oscillation criterion

For support weight `omega(zeta)=|supp zeta|`,

\[
\operatorname{Osc}(P_tH_\xi)\le(R_t\omega)(\xi).
\]

Suppressing spatial collisions yields a finite multitype renewal majorant with source-line kernels

\[
|b_u e^{tK}e_r|.
\]

A subcritical exponentially tilted next-generation kernel gives a volume-uniform exponential oscillation bound.

An exact one-neighbour Potts interpolation separates this from raw absolute FK. The integrated next-generation radii are

\[
\rho(G)=17/6,
\qquad
\rho(\bar G)=3.
\]

Scaling only nonempty target modes by

\[
\varepsilon=17/50
\]

gives

\[
\boxed{289/300<1<51/50.}
\]

So killed hidden-mark averaging can cross a first-moment contraction threshold that the corresponding raw absolute-FK criterion does not.

### Why the programme nevertheless stops

The specific intermediate majorant `R_t` and its submultiplicativity were not found in equivalent form and are retained as a **plausibly new corollary/extension** of the killed typed factorization mechanism.

However, the downstream oscillation/contraction conclusion belongs to established Dobrushin/representational-seminorm theory, and the multitype renewal spectral-radius step is standard machinery. The exact threshold-separation family is a structural interpolation, not a new difficult natural-model theorem.

Under Assignment 011's pre-registered continuation rule, that is insufficient to justify another block.

Decisive Assignment-011 files:

- assignment `assignment-011-killed-patch-cancellation-envelope.md`, `c4299330`;
- `011a-unnormalized-patch-variation-envelope.md`, `59115cb7`;
- `011b-potts-strict-hidden-mark-cancellation.md`, `4df18585`;
- `011c-submultiplicative-patch-variation-kernel.md`, `070598bc`;
- `011d-oscillation-renewal-majorant.md`, `85b8145b`;
- `011e-prior-work-and-value-ruling.md`, `f07a8c15`;
- exact verifiers `6dab532c` and `c1ffaafb`;
- final report `011-killed-patch-cancellation-envelope.md`, `78e725f7`;
- handoff `011-handoff.md`, `d8489a9b`;
- Meeting 011, `4d608d20`.

## Final programme ruling

The programme is **closed deliberately**, not exhausted.

Retain as verified mathematics:

- the arbitrary-finite-state typed dual and exact killed patch representation;
- the finite counterexample showing bare skeleton factorization is false;
- the cemetery-aware killed factorization repair;
- the finite-state transfer formulas;
- the short-`OO` contrast lemma explaining the two natural application failures;
- the patch-variation majorant
  \[
  |Q_t|\le R_t\le A_t,
  \qquad R_{t+s}\le R_tR_s.
  \]

Do not queue:

- Assignment 012;
- another positivity-driven application search;
- generic `d>3` external-positivity algebra;
- a cosmetic variant of the cancellation-envelope route.

A future principal decision may reuse or promote mature material, but autonomous research on this direction has stopped.

## Scope and publication boundary

Proved general scope: arbitrary finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

No programme content is to be promoted to `main` without later principal instruction. Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` remain outside the active write surface.

All other previously stopped programmes remain closed.