# Proof spine: generalized patch representations

Date: 2026-08-17

## Programme status

**CLOSED deliberately after Assignment 011.**

The programme achieved an arbitrary-finite-state killed typed patch representation and several structural corollaries, but did not produce a new natural-model theorem strong enough to justify further autonomous work. There is no active proof-spine edge and no Assignment 012.

## E0. Binary benchmark

**Settled by the canonical paper.**

## E1. Arbitrary finite-state typed signed dual

**Settled in Assignment 001; novelty narrowed in Assignment 008.**

Reference-state indicator tensors give an exact signed Feynman--Kac dual for arbitrary bounded finite-range single-site replacement IPS. Successful nonempty records reveal `(i,t,r,tau)` and hide the post-source outcome.

Novelty status: `known ingredients, assembly plausibly new`.

## E2. Killed typed patch factorization

**Settled in Assignment 002. Primary plausible novelty anchor.**

Typed incoming target conflicts make bare skeleton conditioning false because cemetery entry deletes future no-record constraints. Since the duality function vanishes at cemetery, the killed/noncemetery weighted identity restores exact local factorization.

Novelty status after Assignment 008: **`plausibly new theorem/mechanism`**.

## E3. Exact typed patch representation

**Settled in Assignment 003.**

The killed factorization yields the exact bulk/end patch representation for arbitrary finite local state space.

## E4. Exact finite-state bulk transfer

**Settled in Assignment 004.**

\[
K_i(0,\cdot)=0,
\qquad K_i(r,s)=a_{i,r}^s(\emptyset).
\]

Typed bulk patch positivity is exact nonnegativity of realized local semigroup boundary responses. At `d=2` this is canonical binary patch positivity.

## E5. Three-state endpoint obstruction

**Settled in Assignment 005.**

A physically realizable response

\[
\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

has positive endpoints and exact interior minimum `-1/1224`. Thus the binary endpoint collapse fails in `d=3`.

## E6. Exact `d=3` spectral test

**Correct, but novelty removed in Assignment 008.**

Assignment 006 gives a finite endpoint/critical-point criterion, including degenerate spectra.

Contribution status: **`known / directly subsumed`** by third-order SISO external-positivity theory. It is not part of the contribution claim.

## E7. Natural nonbinary algebraic subclass

**Settled in Assignment 007.**

The exchange-symmetric subclass has an exact algebraic criterion. Its scalar content is structured external positivity, so it remains a useful calculation rather than a primary novelty claim.

## E8. Novelty audit

**Settled in Assignment 008.**

The strongest surviving plausible contribution is the interface

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

Finite-state duality, signed FK duality, partial graphical revelation and external positivity themselves are established ingredients.

## E9. First natural application

**Settled negatively in Assignment 009. Outcome `STOP-APPLICATION-POSITIVITY-FAILS`.**

Krone's two-stage contact process genuinely activates hidden outcomes and typed cemetery conflicts but has a negative repeated-source `OO` patch throughout the interacting birth range. Spatial SIRS has the same obstruction.

Exact gate:

\[
N_{OO}=-5/16,
\qquad D_{OO}=5/16,
\qquad C_{OO}=-1.
\]

## E10. Structurally distinct natural application

**Settled negatively in Assignment 010. Outcome `STOP-SECOND-APPLICATION-POSITIVITY-FAILS`.**

Three-state Potts Metropolis has all states active, direct active-to-active retyping, nondeterministic hidden outcomes and realizable cemetery conflicts, yet a short realized `OO` patch is negative throughout the interacting finite-temperature regime.

Exact gate:

\[
N_{OO}\left((8/3)\log(5/4)\right)=-3884/390625.
\]

### General short-`OO` contrast obstruction

The two application failures are unified by:

\[
a_r^s(\tau)
=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0,
\]

plus a realizable hidden outcome `s` that can feed a subsequent source-`s` successful record. Then a realized arbitrarily short `OO` patch is negative.

This substantially lowers the value of further positivity-driven application search.

## E11. Killed patch-variation majorant

**Settled in Assignment 011.**

The final bounded continuation dropped pointwise bulk positivity and tested delayed absolute values directly.

For finite-volume exact signed FK kernel `Q_t`, raw absolute-FK kernel `A_t`, and killed patch-variation kernel `R_t`,

\[
\boxed{|Q_t|\le R_t\le A_t}
\]

entrywise.

The inequality can be strict in the verified Potts model. At the exact positive-length gate,

\[
\frac{10178204}{38671875}
<
\frac{17919551}{38671875}.
\]

This strict gain comes from averaging hidden outcomes before taking absolute values.

## E12. Composability of the cancellation envelope

**Settled positively in Assignment 011.**

Deterministic time-cut refinement gives

\[
\boxed{R_{t+s}\le R_tR_s}
\]

entrywise. The intermediate typed dual configuration is sufficient boundary memory.

Thus `R_t` is a genuine positive submultiplicative kernel family, not merely a one-horizon inequality.

Contribution status: **plausibly new corollary/extension** of the killed typed factorization, historical priority not established.

## E13. Renewal/oscillation consequence

**Settled mathematically; insufficient for continuation.**

Support weight and collision-free domination produce a finite multitype renewal kernel with source-line responses

\[
|b_u e^{tK}e_r|.
\]

A subcritical exponentially tilted next-generation kernel yields volume-uniform exponential site-oscillation decay.

The criterion can be strictly stronger than the raw absolute-FK first-moment criterion. An exact one-neighbour Potts interpolation has

\[
\rho(G)=17/6,
\qquad
\rho(\bar G)=3,
\]

and after scaling nonempty target modes by `17/50`,

\[
\boxed{289/300<1<51/50.}
\]

However, the downstream contraction/ergodicity implication is established Dobrushin/representational-seminorm territory, and the multitype renewal step is standard machinery. The exact separating family is a structural gate rather than a new theorem for a natural difficult model.

## E14. Final value ruling

**Assignment 011 outcome: `STOP-CANCELLATION-NO-QUALITATIVE-GAIN`.**

The final block proved more than local cancellation but did not produce a sufficiently independent natural-model or model-independent consequence to justify another research block.

Accordingly the programme stops rather than moving to:

- another positivity-driven application;
- generic `d>3` external-positivity algebra;
- another cancellation-envelope variant.

## E15. Multi-site physical updates

**Unstudied and outside the closed programme's proved scope.**

Simultaneous multi-site physical updates remain outside the single-site replacement representation theorem. This is not an active edge.

## Final retained contribution framing

Verified mathematics retained:

1. arbitrary finite-state typed signed FK representation for single-site replacement IPS;
2. exact failure of bare successful-skeleton factorization;
3. cemetery-aware killed patch factorization;
4. exact finite-state bulk/end patch representation;
5. local transfer formulas;
6. general short-`OO` contrast obstruction;
7. patch-variation majorant
   \[
   |Q_t|\le R_t\le A_t,
   \qquad R_{t+s}\le R_tR_s.
   \]

Plausible contribution anchor: the **killed typed patch interface**, supplemented by the patch-variation majorant. The `d=3` spectral criterion is explicitly outside the contribution claim.

There is no active scientific edge on this branch.