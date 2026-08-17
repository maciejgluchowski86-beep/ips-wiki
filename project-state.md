# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

A quantitatively improved instance of an established method does not count as a new project result merely because the calculation is exact or improves a constant. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Scientific direction status

**No active scientific direction.**

The generalized finite-state patch-representation programme on branch `research/generalized-patch-representations` is **closed deliberately on opportunity-cost grounds** after verified Assignment 010 and the final bounded Assignment 011 cancellation block.

Workspace: `research/active/generalized-patch-representations/`.

Latest meeting: `research/active/generalized-patch-representations/meetings/011-killed-cancellation-majorant-works-but-programme-stops.md`.

No Assignment 012 is queued.

Nothing from this programme is to be written or merged to `main` without later principal instruction.

## Generalized finite-state representation: verified mathematical output

Assignments 001--004 establish for arbitrary finite-state bounded finite-range **single-site replacement** IPS in a reference-state indicator tensor basis:

1. an exact typed signed Feynman--Kac dual;
2. successful records `(i,t,r,tau)` hiding the post-source outcome;
3. one-site typed spacetime patches;
4. an exact counterexample showing bare conditioning on the coarse successful skeleton need not factor;
5. an exact cemetery-aware killed/noncemetery weighted factorization;
6. an exact bulk/end patch representation;
7. the signed local transfer
   \[
   K_i(0,\cdot)=0,
   \qquad K_i(r,s)=a_{i,r}^s(\emptyset);
   \]
8. typed bulk patch positivity as nonnegativity of realized local matrix-semigroup boundary responses;
9. exact binary reduction to the canonical patch construction.

The strongest project-specific mechanism is the interface

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

## Novelty status

Assignment 008's bounded closest-prior-work audit remains controlling:

1. finite-state typed signed duality: `known ingredients, assembly plausibly new`;
2. killed typed patch factorization / representation: **`plausibly new theorem/mechanism`**;
3. transfer-matrix bulk positivity: `known ingredients, assembly plausibly new`;
4. exact boundary-complete `d=3` scalar spectral criterion: **`known / directly subsumed`** by third-order SISO external positivity;
5. exchange-symmetric exact algebraic criterion: `known ingredients, assembly plausibly new`;
6. combined generalized framework: **`plausibly new theorem/mechanism`**.

Do not claim novelty for finite-state duality, signed FK duality, partial graphical revelation, Metzler semigroups, scalar external positivity, or the Assignment-006 `d=3` spectral theorem individually.

Historical priority of the killed typed factorization remains plausible rather than exhaustively established.

## Natural application results

### Assignment 009: two-stage contact / SIRS

Outcome: `STOP-APPLICATION-POSITIVITY-FAILS`.

Krone's two-stage contact process was selected before positivity calculation and genuinely activates hidden outcomes and typed cemetery conflicts. Nevertheless, its adult-neighbour successful record has row

\[
(\lambda,-\lambda,-\lambda),
\]

and a realized repeated-source `OO` patch is negative throughout the interacting birth range.

Exact verified gate:

\[
N_{OO}=-5/16,
\qquad D_{OO}=5/16,
\qquad C_{OO}=-1.
\]

Spatial SIRS has the same obstruction.

### Assignment 010: three-state Potts Metropolis

Outcome: `STOP-SECOND-APPLICATION-POSITIVITY-FAILS`.

This structurally distinct model has all states active, direct active-to-active retyping, nondeterministic hidden outcomes and realizable cemetery conflicts. Yet

\[
a_1^2(\tau)=-qz^2(1-z^2)<0
\]

for every interacting finite-temperature point `q>0`, `0<z<1`, producing a negative realized short `OO` patch.

Exact verified gate:

\[
N_{OO}\left((8/3)\log(5/4)\right)
=-3884/390625.
\]

The independent verifier passed 1,485 exact checks with zero float literals.

### General short-`OO` contrast obstruction

The two failures are unified by:

> if active types `r!=s` and nonempty target `tau` satisfy
> \[
> a_r^s(\tau)=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0,
> \]
> hidden outcome `s` is realizable, and a source-`s` successful record can follow, then a realized arbitrarily short `OO` patch is negative.

This substantially lowers the value of further positivity-driven multistate model search.

## Final bounded continuation: Assignment 011

After independent verification of Assignment 010, the Professor chose one final bounded continuation on the surviving representation/cancellation mechanism rather than generic `d>3` positivity or another model search.

Assignment 011 ended

**`STOP-CANCELLATION-NO-QUALITATIVE-GAIN`.**

### Killed patch-variation kernel

In finite volume, let `Q_t` be the exact signed FK kernel and `A_t` the raw absolute-FK kernel. The killed successful-skeleton representation defines a positive kernel `R_t` by taking absolute values only after each hidden killed-patch expectation. Exactly,

\[
\boxed{|Q_t|\le R_t\le A_t}
\]

entrywise.

The improvement is strict on the verified Potts model. At the exact positive-length gate,

\[
\boxed{
\frac{10178204}{38671875}
<
\frac{17919551}{38671875}.}
\]

### Composability

Deterministic time-cut refinement gives

\[
\boxed{R_{t+s}\le R_tR_s}
\]

entrywise. Thus the delayed hidden-mark cancellation survives concatenation in a finite-memory positive kernel family.

### Renewal/oscillation consequence and exact separation

Support-weight domination gives a finite multitype renewal criterion for volume-uniform exponential oscillation decay. It can be strictly stronger than the corresponding raw absolute-FK first-moment criterion.

For an exact one-neighbour Potts structural gate,

\[
\rho(G)=17/6,
\qquad
\rho(\bar G)=3.
\]

Scaling nonempty neighbour-dependent tensor modes by

\[
\varepsilon=17/50
\]

gives

\[
\boxed{289/300<1<51/50.}
\]

So the patch-cancelled majorant can cross a contraction threshold that raw absolute FK does not.

### Why this still stops

The specific intermediate majorant `R_t` and its submultiplicativity remain a **plausibly new corollary/extension** of the killed typed patch mechanism; no equivalent source was identified in the bounded audit.

However, the downstream oscillation/contraction implication is established Dobrushin/representational-seminorm territory, and the multitype renewal spectral-radius argument is standard. The exact separating family is a structural interpolation rather than a new difficult natural-model theorem.

Under the pre-registered Assignment-011 continuation rule, this is insufficient to justify another block.

Decisive final files:

- Assignment 011: `research/active/generalized-patch-representations/students/professor/assignment-011-killed-patch-cancellation-envelope.md`, `c4299330`;
- envelope theorem `011a`, `59115cb7`;
- strict cancellation `011b`, `4df18585`;
- submultiplicativity `011c`, `070598bc`;
- renewal/oscillation theorem `011d`, `85b8145b`;
- prior-work/value ruling `011e`, `f07a8c15`;
- exact verifiers `6dab532c` and `c1ffaafb`;
- final report `78e725f7`;
- handoff `d8489a9b`;
- closing Meeting 011 `4d608d20`.

## Final programme ruling

The generalized-patch programme is **closed deliberately**, not exhausted.

Retain as verified mathematics:

- arbitrary-finite-state typed signed FK duality for single-site replacement IPS;
- exact failure of bare successful-skeleton factorization;
- cemetery-aware killed factorization and exact finite-state patch representation;
- finite-state transfer formulas;
- the short-`OO` contrast obstruction;
- the patch-variation majorant
  \[
  |Q_t|\le R_t\le A_t,
  \qquad R_{t+s}\le R_tR_s.
  \]

Do not queue or reopen by default:

- another positivity-driven application search;
- generic `d>3` external-positivity algebra;
- another cancellation-envelope variant.

A later principal decision may reuse or promote mature material, but autonomous work on this direction has stopped.

## Scope and publication boundary

Proved general scope: arbitrary finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

The branch-only generalized-patch documentation remains research material.

**Do not publish or merge programme content to `main`.**

Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` remain outside the active write surface.

All other previously stopped programmes remain closed.