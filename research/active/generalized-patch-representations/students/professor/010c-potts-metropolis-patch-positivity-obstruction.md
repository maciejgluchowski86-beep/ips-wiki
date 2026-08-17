# 010c: Potts Metropolis fails typed patch positivity by an active-source contrast obstruction

Date: 2026-08-17

This note executes Assignment 010 Part C after the model selection in `010a` and exact specialization in `010b` were committed.

## 1. Decisive outgoing row

For the selected three-state ferromagnetic Potts Metropolis dynamics, fix reference color `0`. Let

\[
z=e^{-\beta J}\in(0,1),
\qquad q>0.
\]

Take a successful record with pre-source dual type `1` and one typed target-neighbor of color `1`. The exact outgoing row from `010b` is

\[
p=\mathbf a_{1;1,0}
=
\left(
qz^2(1-z^2),
q(z-1)(z^3+z^2-1),
-qz^2(1-z^2)
\right).
\tag{1.1}
\]

In particular

\[
\boxed{p_2=-qz^2(1-z^2)<0.}
\tag{1.2}
\]

Since the successful skeleton records only `(source,type,target-pattern)` and hides the post-source outcome, the hidden branch with outcome `2` occurs with positive absolute rate

\[
|p_2|=qz^2(1-z^2)>0.
\tag{1.3}
\]

## 2. Why the sign is negative: Metropolis saturation

The coefficient identity is

\[
a_1^2(\tau)
=
\widehat c^{2\to1}(\tau)
-
\widehat c^{0\to1}(\tau).
\tag{2.1}
\]

For the singleton target `tau={neighbor->1}`:

- with source `0`, all-reference neighbors give rate `qz^4`, while changing one neighbor from `0` to `1` gives rate `qz^2`; therefore
  \[
  \widehat c^{0\to1}(\tau)=q(z^2-z^4)=qz^2(1-z^2)>0;
  \]
- with source `2`, the move `2->1` already has Metropolis acceptance one with all-reference neighbors and still has acceptance one after that neighbor is changed to color `1`; therefore
  \[
  \widehat c^{2\to1}(\tau)=0.
  \]

Hence

\[
\boxed{
a_1^2(\tau)=0-qz^2(1-z^2)<0.}
\tag{2.2}
\]

This is not the vacancy/catalytic-birth mechanism of Assignment 009. Every physical Potts color is active and every directed color replacement has positive physical rate. The obstruction comes from a **difference of target-mode responses between two active source colors**: one response is positive while the other has saturated at the Metropolis ceiling and has zero increment.

## 3. The negative `OO` descriptor is realized

After the first successful record chooses hidden outcome `2`, the local dual active type is `2`.

By color symmetry, there are positive-rate successful records with pre-source type `2`; for example the color-swapped singleton row `a_{2;0,1}` has the same positive coarse hazard as (1.1). Thus the next successful record at the same source can have source type `2` after an arbitrarily short positive interval.

Choose an interval in which:

1. the first record takes hidden outcome `2`;
2. no intervening local mark changes the active type or kills consistency;
3. the next nonempty successful mark is one of the positive-hazard source-type-2 records.

This event has strictly positive reference probability for every positive interval length. Therefore the outgoing-to-outgoing boundary descriptor ending in active type `2` is a genuinely realized bulk patch, not an artificially completed boundary condition.

Its signed numerator is

\[
N_{OO}(t)=p e^{tK}e_2^T,
\tag{3.1}
\]

where

\[
K=q
\begin{pmatrix}
0&0&0\\
z^4&-(z^4+2)&1-z^4\\
z^4&1-z^4&-(z^4+2)
\end{pmatrix}.
\tag{3.2}
\]

At zero length,

\[
N_{OO}(0)=p_2=-qz^2(1-z^2)<0.
\tag{3.3}
\]

The matrix exponential is continuous in `t`, so for every fixed `0<z<1` there exists `epsilon(z)>0` such that

\[
\boxed{N_{OO}(t)<0\quad\text{for }0<t<\epsilon(z).}
\tag{3.4}
\]

The corresponding unsigned consistency denominator is strictly positive on every realized descriptor. Thus the bulk patch contribution itself is negative for all sufficiently short realized patches.

Consequently

\[
\boxed{
\text{three-state ferromagnetic Potts Metropolis dynamics is not typed patch positive for any }0<z<1.}
\tag{3.5}
\]

Equivalently, typed patch positivity fails for every finite positive inverse temperature `beta J>0`.

At `z=1` (`beta=0`) the dynamics becomes source/neighborhood-independent pure color refresh: all nonempty target coefficients vanish, so there are no successful interactions to test. That is a degenerate noninteracting boundary, not a positive interacting regime.

## 4. Exact finite positive-length gate

Take

\[
z=1/2,
\qquad q=1.
\tag{4.1}
\]

Then

\[
p=(3/16,5/16,-3/16),
\tag{4.2}
\]

and

\[
K=
\begin{pmatrix}
0&0&0\\
1/16&-33/16&15/16\\
1/16&15/16&-33/16
\end{pmatrix}.
\tag{4.3}
\]

The active block has symmetric decay rate `9/8` and antisymmetric decay rate `3`. Decomposing `(p_1,p_2)` into symmetric and antisymmetric parts gives

\[
\frac{p_1+p_2}{2}=1/16,
\qquad
\frac{p_1-p_2}{2}=1/4.
\]

Hence

\[
N_{OO}(t)
=
\frac1{16}e^{-9t/8}
-
\frac14 e^{-3t}.
\tag{4.4}
\]

Choose the strictly positive exact patch length

\[
t_*=rac83\log\frac54.
\tag{4.5}
\]

Then

\[
e^{-9t_*/8}=(4/5)^3=64/125,
\qquad
 e^{-3t_*}=(4/5)^8=65536/390625.
\]

Therefore

\[
\boxed{
N_{OO}(t_*)
=
\frac4{125}-\frac{16384}{390625}
=-\frac{3884}{390625}<0.}
\tag{4.6}
\]

The denominator is strictly positive. Indeed the initial absolute hidden-outcome-2 weight is `3/16>0`, and the no-intervening-mark path followed by the source-type-2 terminal successful record gives a positive contribution to the unsigned reference transfer. No numerical tolerance is involved.

## 5. General short-`OO` contrast lemma

The Potts calculation reveals a broader obstruction than the Assignment-009 birth formulation.

### Lemma

Fix active types `r!=s` and a nonempty target pattern `tau`. Suppose

\[
a_r^s(\tau)
=
\widehat c^{s\to r}(\tau)
-
\widehat c^{0\to r}(\tau)
<0.
\tag{5.1}
\]

Assume:

1. the successful record `(r,tau)` is realizable, so the hidden outcome `s` occurs with positive absolute branch rate;
2. after that outcome, a successful record with pre-source type `s` can occur at the same source with positive hazard.

Then the corresponding realized `OO` numerator satisfies

\[
N_{OO}(0)=a_r^s(\tau)<0,
\]

and hence is negative for all sufficiently short positive patch lengths. Typed bulk patch positivity fails.

### Proof

The outgoing row is `a_{r,tau}` and the terminal outgoing source type is `s`, so the transfer numerator is

\[
a_{r,tau}e^{tK}e_s^T.
\]

At `t=0` this equals `a_r^s(tau)`. Realizability gives a positive denominator and arbitrary short positive patch lengths. Continuity gives the result. `square`

Assignment 009's catalytic-birth no-go is the special case where `widehat c^{0->r}(tau)>0` and every active-source target-mode contribution into `r` vanishes. The Potts example shows that the same local obstruction can arise with **all states active and all physical replacement rates positive**, through unequal target-mode sensitivity among active sources.

## 6. Hidden-mark honesty verdict

The model fails positivity, but it passes the Assignment-010 Part D honesty check in the substantive sense:

- the decisive successful record has more than one hidden post-source outcome with positive absolute rate;
- an inconsistent typed target merge can genuinely hit cemetery;
- the killed/noncemetery factorization is therefore not vacuous;
- the model is not a deterministic voter/cyclic-copy dual in disguise.

Thus the negative application verdict is informative about the killed typed framework itself rather than a degenerate failure to activate it.
