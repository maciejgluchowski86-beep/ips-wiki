# Potts Metropolis application obstruction

> **Research-branch result.** This page records Assignment 010 on `research/generalized-patch-representations`. It is not published on `main`.

## Model

Consider the three-state zero-field ferromagnetic Potts model with colors

\[
E=\{0,1,2\}
\]

and nearest-neighbor Hamiltonian

\[
H(\eta)=-J\sum_{\{x,y\}}\mathbf 1\{\eta_x=\eta_y\},
\qquad J>0.
\]

Under single-spin Metropolis Glauber dynamics, write

\[
z=e^{-\beta J}\in(0,1],
\]

and let `q>0` be the common proposal-clock prefactor. If the source color is `x`, proposed target color is `y!=x`, and `n_a` is the number of neighboring sites of color `a`, then the Poissonized continuous-time replacement rate is

\[
\boxed{c^{x\to y}=qz^{(n_x-n_y)_+}.}
\]

This is a genuinely three-state active-to-active model: there is no vacancy state, and at finite temperature every directed physical color replacement has positive rate.

## Exact typed transfer

Choose reference color `0`. For a typed target with `k_1` color-1 and `k_2` color-2 sites, the physical indicator-tensor coefficient is

\[
\widehat c^{x\to y}_{k_1,k_2}
=
\sum_{i=0}^{k_1}\sum_{j=0}^{k_2}
(-1)^{k_1-i+k_2-j}
\binom{k_1}{i}\binom{k_2}{j}
qz^{(n_x(i,j)-n_y(i,j))_+},
\]

where

\[
n_0=4-i-j,
\qquad n_1=i,
\qquad n_2=j.
\]

The empty-target signed transfer is

\[
K=q
\begin{pmatrix}
0&0&0\\
z^4&-(z^4+2)&1-z^4\\
z^4&1-z^4&-(z^4+2)
\end{pmatrix}.
\]

Thus for `0<z<1` the interior transfer itself retypes the two active dual labels.

## A non-deterministic successful record

Take pre-source dual type `1` and a singleton typed target of color `1`. The outgoing signed row is

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

For every `0<z<1`, both hidden outcomes `0` and `2` have positive absolute branch rates. Hence the coarse successful skeleton genuinely hides post-source information.

Typed cemetery conflicts are also realizable: a target requiring label `1` can encounter an already-active label `2`, for example one produced by the same hidden-outcome mechanism.

Therefore the killed/noncemetery patch factorization is not vacuous in this model.

## Patch positivity fails

For the same singleton target,

\[
a_1^2(\tau)
=
\widehat c^{2\to1}(\tau)-\widehat c^{0\to1}(\tau).
\]

The two target-mode responses are

\[
\widehat c^{0\to1}(\tau)=qz^2(1-z^2)>0,
\]

\[
\widehat c^{2\to1}(\tau)=0.
\]

The second vanishes because `2->1` is already accepted at the Metropolis ceiling; adding one color-1 neighbor does not further increase its rate.

Hence

\[
\boxed{a_1^2(\tau)=-qz^2(1-z^2)<0.}
\]

The hidden outcome `2` can be followed by a positive-hazard source-type-2 successful record. Thus a realized outgoing-to-outgoing patch has numerator

\[
N_{OO}(t)=\mathbf a_{1;1,0}e^{tK}e_2^T
\]

with

\[
N_{OO}(0)<0.
\]

By continuity it is negative for all sufficiently short positive patch lengths. Therefore

\[
\boxed{
\text{three-state Potts Metropolis dynamics is not typed patch positive for any }0<z<1.}
\]

At `z=1`, all nonempty target coefficients vanish, so the model is the neighborhood-independent noninteracting boundary.

## Exact gate

At

\[
z=1/2,
\qquad q=1,
\]

\[
p=(3/16,5/16,-3/16),
\]

and

\[
K=
\begin{pmatrix}
0&0&0\\
1/16&-33/16&15/16\\
1/16&15/16&-33/16
\end{pmatrix}.
\]

For

\[
t_*=(8/3)\log(5/4),
\]

\[
\boxed{N_{OO}(t_*)=-3884/390625<0.}
\]

The exact verifier reconstructs every physical rate and the typed generator before checking this sign.

## General short-`OO` contrast obstruction

The calculation yields a model-independent local test.

Let `r!=s` be active types and `tau` a nonempty typed target. If

\[
\boxed{
a_r^s(\tau)
=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0,}
\]

and:

1. hidden outcome `s` is realized by the successful record `(r,tau)`;
2. a source-type-`s` successful record can follow with positive hazard,

then the corresponding realized `OO` numerator is negative for all sufficiently short positive patch lengths.

The contact/SIRS catalytic-birth obstruction is one special case. Potts Metropolis shows that the same phenomenon can occur in a fully active color-symmetric system through unequal source-state sensitivity to the same neighbor mode.

## Interpretation

The generalized killed typed **representation** survives this example and is genuinely exercised by it. What fails is the stronger bulk-positivity property.

Together with the two-stage/SIRS application, this suggests that multistate patch positivity is substantially more restrictive than the representation itself. Further application work should not simply search for another model whose coefficients happen to satisfy positivity.
