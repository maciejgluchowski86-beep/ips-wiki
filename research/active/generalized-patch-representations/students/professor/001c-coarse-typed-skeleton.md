# 001c: coarse typed successful-interaction record

Date: 2026-08-17

This note executes Part E of Assignment 001. It establishes only the **geometric feasibility** of a generalized successful-interaction skeleton. Conditional factorization is the next theorem, not part of this checkpoint.

## 1. Superpose the source-outcome clocks

Fix a source site `i`, pre-interaction dual type `r in E_*`, and a nonempty typed target

\[
\tau\in T(N(i)),
\qquad
\operatorname{supp}\tau\ne\emptyset.
\]

For each source outcome `s in E`, the signed typed dual of 001b has a clock of rate

\[
\lambda_{i,r}^s(\tau)=|a_{i,r}^s(\tau)|.
\]

Their superposition is a Poisson process of rate

\[
\boxed{
\Lambda_{i,r}(\tau)
=\sum_{s\in E}|a_{i,r}^s(\tau)|.}
\tag{1.1}
\]

Conditional on a point of this superposed process, the hidden branch mark has law

\[
\boxed{
P(s=u\mid i,r,\tau)
=\frac{|a_{i,r}^u(\tau)|}{\Lambda_{i,r}(\tau)}}
\tag{1.2}
\]

when `Lambda>0`. Its sign is the deterministic label

\[
\epsilon_{i,r}^u(\tau)=\operatorname{sgn}_{\pm}(a_{i,r}^u(\tau)).
\]

Thus the finite hidden mark may be taken to be the source outcome `s`; the sign is carried by that mark.

## 2. Successful record

A nonempty-target clock point with index `(i,r,tau)` is **successful** when the current typed dual state is not `dagger` and

\[
\xi_{t-}(i)=r.
\]

The proposed coarse record is

\[
\boxed{(i,t,r,\tau).}
\tag{2.1}
\]

It records:

- source site `i`;
- time `t`;
- the pre-interaction source type `r`;
- the typed target `tau`;

but **not** the source outcome `s` and hence not whether the source is deleted, survives, or is retyped.

This is the direct multi-state analogue of the binary record `(i,t,S)`, where the unique source type is invisible and the hidden outcome is split versus birth.

## 3. Geometry is branch-independent

For every hidden source outcome `s`, the local map is

\[
\Theta_{i;s,\tau}(\xi).
\]

The interaction has one outgoing endpoint on the source line `i` and one incoming endpoint on every target line

\[
j\in\operatorname{supp}\tau.
\]

These site-lines depend only on `(i,tau)`, not on `s`. Therefore the hidden source outcome does not alter the spacetime patch boundaries created by the record.

This remains true when the typed target conflicts with an already active different type. The deterministic merge then sends the dual state to `dagger`, but the interaction still involves the same source and target site-lines for every `s`. How the cemetery event enters the conditional factorization/representation is a downstream issue; it is not a geometric branch dependence.

Hence the exact obstruction pre-registered as `STOP-NO-COARSE-SKELETON` does not occur.

## 4. Why the pre-interaction source type should normally be revealed

The even coarser record `(i,t,tau)` is geometrically meaningful, because `r` also does not change the set of involved site-lines. It is not the recommended analytical skeleton.

The reason is that the combined intensity (1.1) is generally type-dependent:

\[
\Lambda_{i,r}(\tau)
\ne
\Lambda_{i,r'}(\tau).
\]

Moreover, at an outgoing endpoint the local consistency condition is precisely that the pre-interaction local dual type equals the clock's source type `r`.

If `r` is hidden, both the hazard of a selected outgoing record and its consistency condition depend on the hidden state produced by the preceding patch. Revealing `r` moves this information onto the boundary record, exactly where a later typed patch law can condition on it.

Thus the natural first generalized skeleton is (2.1), not the minimally geometric `(i,t,tau)`.

## 5. Binary specialization

For `E={0,1}`, the only source type is `r=1`, so it carries no information and is suppressed. The two hidden outcomes are

- `s=0`: source deletion, giving death/split;
- `s=1`: source survival, giving birth.

For a nonempty target `S`, (1.1) becomes

\[
\delta_i(S)+\beta_i(S),
\]

and (1.2) becomes exactly the binary conditional split/birth law used at an outgoing patch boundary in the canonical paper.

Therefore the proposed typed record reduces exactly to the paper's successful-interaction record.

## 6. Decision for Assignment 001

Parts A--D give a fixed local signed graphical dual and exact binary specialization. The mandatory `d=3` verifier passes the complete elementary family. The typed-source record (2.1) hides a finite source-outcome mark without changing the successful-interaction geometry.

Accordingly Assignment 001 reaches

\[
\boxed{\texttt{CONTINUE-TYPED-PATCH}.}
\]

The next bridge is **generalized typed skeleton conditional factorization**, not patch positivity. The key new issue to test there is whether local patch consistency remains a product of source--time-strip events once incoming typed targets may conflict with the preceding local type and once outgoing source types are explicit boundary labels.
