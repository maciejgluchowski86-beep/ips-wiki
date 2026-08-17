# Assignment 010 final report: structurally distinct Potts application

Date: 2026-08-17

Outcome:

\[
\boxed{\texttt{STOP-SECOND-APPLICATION-POSITIVITY-FAILS}.}
\]

## 1. Goal and anti-selection discipline

Assignment 010 asked for one natural published genuinely three-state single-site replacement IPS structurally distinct from the contact/SIRS catalytic-birth models rejected in Assignment 009.

The model had to be selected before any patch-positivity calculation, and a positive verdict would count only if the model genuinely activated non-deterministic hidden post-source outcomes and the typed cemetery/killed-factorization mechanism.

The selection was committed first in `010a-literature-driven-structural-selection.md`.

## 2. Selected model

The selected model is the **three-state zero-field ferromagnetic Potts model with single-spin Metropolis Glauber dynamics** on the square lattice.

For source color `x`, proposed target color `y!=x`, and neighbor counts `n_0,n_1,n_2`, write

\[
z=e^{-\beta J}\in(0,1],
\qquad q>0.
\]

The continuous-time Poissonization of the standard single-spin Metropolis rule has local replacement rates

\[
\boxed{
c^{x\to y}=qz^{(n_x-n_y)_+}.}
\]

The common factor `q` is the proposal-clock rate and only rescales time.

The model was selected over the three-color cyclic particle system because:

- all three Potts colors are genuine and symmetric;
- every event is single-site replacement;
- active colors directly retype into one another;
- acceptance depends on the source color and the local energy comparison;
- the graphical update is not merely a deterministic invasion/copy arrow;
- the model has substantial independent metastability/mixing literature.

No coefficient or positivity test was used in the selection.

## 3. Exact typed specialization

Reference color `0` was fixed by symmetry. For a typed target containing `k_1` color-1 and `k_2` color-2 sites, every physical indicator-tensor coefficient is given exactly by Möbius inversion:

\[
\widehat c^{x\to y}_{k_1,k_2}
=
\sum_{i=0}^{k_1}\sum_{j=0}^{k_2}
(-1)^{k_1-i+k_2-j}
\binom{k_1}{i}\binom{k_2}{j}
qz^{(n_x(i,j)-n_y(i,j))_+},
\]

with

\[
n_0=4-i-j,
\qquad n_1=i,
\qquad n_2=j.
\]

`010b` records the complete 14 target-count rows for source dual type `1`; source type `2` follows by exact color exchange.

The empty-target signed transfer is

\[
\boxed{
K=q
\begin{pmatrix}
0&0&0\\
z^4&-(z^4+2)&1-z^4\\
z^4&1-z^4&-(z^4+2)
\end{pmatrix}.}
\]

Thus even the no-success interior dynamics contains genuine active-type retyping for `0<z<1`.

## 4. Hidden-mark and cemetery honesty gate

Take a singleton typed target of color `1` and pre-source dual type `1`. Its outgoing row is

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

For every `0<z<1`,

\[
a_1^0>0,
\qquad a_1^2<0.
\]

Hence the same coarse successful record hides at least two distinct post-source outcomes with positive absolute branch rates. Generically it hides all three.

Typed cemetery conflicts are also realizable: a record whose target requires type `1` can meet an already active type-2 dual label, obtainable from this hidden outcome, from initial data, or from the positive empty-target retyping in `K`.

Therefore this model **genuinely exercises the surviving novelty anchor**. Its failure below is not a deterministic/coalescing/additive collapse and does not trigger the Part-D degenerate-pass ruling.

## 5. Exact positivity obstruction

For the decisive singleton target `tau`,

\[
a_1^2(\tau)
=
\widehat c^{2\to1}(\tau)-\widehat c^{0\to1}(\tau).
\]

The target-mode increments are

\[
\widehat c^{0\to1}(\tau)=qz^2(1-z^2)>0,
\]

\[
\widehat c^{2\to1}(\tau)=0.
\]

The second equality is a Metropolis-saturation effect: `2->1` is already accepted at maximal rate before the extra color-1 neighbor is inserted, so that target-mode perturbation contributes no increment.

Thus

\[
\boxed{a_1^2(\tau)=-qz^2(1-z^2)<0.}
\]

The hidden outcome `2` has positive absolute rate, and by color symmetry a positive-hazard source-type-2 successful record can immediately follow. Therefore a same-source outgoing-to-outgoing descriptor ending in source type `2` is realized at arbitrarily short positive patch lengths.

Its numerator is

\[
N_{OO}(t)=\mathbf a_{1;1,0}e^{tK}e_2^T,
\]

so

\[
N_{OO}(0)=a_1^2(\tau)<0.
\]

Continuity implies negative realized bulk patches for every interacting finite-temperature parameter point:

\[
\boxed{
\text{typed patch positivity fails for every }q>0,\ 0<z<1.}
\]

At `z=1` the dynamics is neighborhood-independent pure color refresh and all nonempty target coefficients vanish, so that boundary is noninteracting rather than a positive interacting regime.

## 6. Mandatory exact finite-length gate

At

\[
z=1/2,
\qquad q=1,
\]

one obtains

\[
p=(3/16,5/16,-3/16),
\]

\[
K=
\begin{pmatrix}
0&0&0\\
1/16&-33/16&15/16\\
1/16&15/16&-33/16
\end{pmatrix}.
\]

The active symmetric and antisymmetric decay rates are `9/8` and `3`. Hence

\[
N_{OO}(t)=\frac1{16}e^{-9t/8}-\frac14e^{-3t}.
\]

At the exact positive patch length

\[
t_*=(8/3)\log(5/4),
\]

\[
e^{-9t_*/8}=(4/5)^3,
\qquad e^{-3t_*}=(4/5)^8,
\]

and therefore

\[
\boxed{N_{OO}(t_*)=-3884/390625<0.}
\]

The unsigned denominator is strictly positive because the hidden outcome-2 absolute weight and the terminal source-type-2 successful hazard are both positive, and the no-intervening-mark event has positive probability.

The exact verifier `010-potts-metropolis-verifier.py` reconstructs all physical rates and typed-generator actions before checking this gate.

## 7. Generalized short-OO contrast obstruction

The Potts calculation yields a broader local lemma.

Let `r!=s` be active types and `tau` a nonempty target pattern. If

\[
\boxed{
a_r^s(\tau)
=
\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0,}
\]

and:

1. the hidden outcome `s` is realized by the successful record `(r,tau)`;
2. a positive-hazard source-type-`s` successful record can follow at the same source,

then the realized `OO` numerator equals `a_r^s(tau)<0` at zero length and remains negative for all sufficiently short positive lengths. Typed patch positivity fails.

Assignment 009's catalytic-birth no-go is a special case. Potts Metropolis shows that the same obstruction occurs when all physical states are active and every directed replacement has positive rate; unequal target-mode **sensitivity** among active source colors is enough.

This is the main new mathematical information obtained in Assignment 010.

## 8. Application-specific prior work

The selected model already has substantial theory:

- Nardi--Zocca analyze low-temperature tunneling and mixing asymptotics;
- Bet--Gallo--Nardi identify critical configurations and typical tunneling paths for zero-field Potts Metropolis dynamics;
- Potts Glauber dynamics has extensive coupling, block-dynamics, critical-mixing and random-cluster literature.

The bounded search did not identify the particular signed hidden-outcome/cemetery-aware patch factorization in Potts language, but that absence does not establish priority beyond Assignment 008's existing `plausibly new` status for the general representation.

Since bulk patch positivity fails, this block claims no new Potts comparison, convergence, mixing, metastability, invariant-measure, or duality theorem.

## 9. Programme implication

Assignments 009 and 010 now test two materially different natural architectures:

1. vacancy/birth + local stage conversion (two-stage contact/SIRS);
2. fully active symmetric neighbor-sensitive retyping (Potts Metropolis).

Both genuinely activate nontrivial hidden marks; both fail typed bulk patch positivity through realized short `OO` patches.

Therefore continuing to search natural models **because they might be patch positive** now has low expected value. The evidence points to typed patch positivity being substantially more restrictive in multistate systems than the representation itself.

No third model search is opened automatically, and no generic `d>3` coefficient block is opened.

If this programme continues after independent verification, the mathematically distinct question is whether the killed typed patch representation has useful consequences **without** assuming bulk patch positivity. That requires a fresh opportunity-cost decision rather than another positivity-fitted application.

## Decisive files

- `010a-literature-driven-structural-selection.md`, selection commit before positivity;
- `010b-potts-metropolis-typed-specialization.md`, exact coefficients and hidden/cemetery geometry;
- `010c-potts-metropolis-patch-positivity-obstruction.md`, all-parameter obstruction and contrast lemma;
- `010-potts-metropolis-verifier.py`, exact gate;
- `010d-potts-prior-work-and-application-value.md`, application-specific prior-work ruling.
