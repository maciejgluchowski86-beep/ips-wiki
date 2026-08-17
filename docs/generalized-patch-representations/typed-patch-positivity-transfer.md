# Typed bulk patch positivity via transfer matrices

> **Research-branch page.** This page exists only on `research/generalized-patch-representations`. It is not published on `main` and has not yet completed an external literature audit.

This page records the exact finite-dimensional form of bulk patch contributions for finite-state bounded finite-range single-site replacement dynamics in the reference-state indicator basis.

## Local type space

Let

\[
E=\{0,1,\ldots,d-1\},
\]

where `0` means dual-inactive and `E_*=E\setminus\{0\}` are active dual types.

For active source type `r`, source outcome `s`, and typed target `tau`, write

\[
a_{i,r}^s(\tau)
\]

for the signed branch coefficient from the typed duality construction.

## Signed interior transfer

Define

\[
\rho_{i,r}=\sum_{s\ne r}|a_{i,r}^s(\emptyset)|,
\qquad
\kappa_{i,r}=\sum_{\tau\ne\emptyset}\sum_s|a_{i,r}^s(\tau)|.
\]

The local Feynman--Kac potential is

\[
v_{i,r}=\rho_{i,r}+\kappa_{i,r}+a_{i,r}^r(\emptyset).
\]

A direct first-step calculation shows that the signed killed Feynman--Kac transfer has generator

\[
\boxed{K_i(0,\cdot)=0,
\qquad K_i(r,s)=a_{i,r}^s(\emptyset),\quad r\in E_*.}
\]

Thus the entire signed interior transfer is

\[
e^{tK_i}.
\]

The nonempty-target no-success hazard disappears from this numerator generator because it cancels exactly against the corresponding part of the local potential.

## Consistency denominator

The consistency normalizer has killed Markov generator

\[
B_i(r,s)=|a_{i,r}^s(\emptyset)|\quad(s\ne r),
\]

\[
B_i(r,r)=
-\sum_{s\ne r}|a_{i,r}^s(\emptyset)|-\kappa_{i,r},
\]

with zero inactive row.

Its semigroup `e^{tB_i}` is substochastic and nonnegative. A denominator is positive exactly on a realizable source-line descriptor.

## Boundary vectors

For an incoming terminal type `b`, use

\[
f_b^I=e_0^T+e_b^T.
\]

For an outgoing terminal source type `r`, use

\[
f_r^O=e_r^T.
\]

For an outgoing initial record with pre-source type `r` and nonempty target `tau`, define

\[
\mathbf a_{r,\tau}=(a_{i,r}^s(\tau))_{s\in E},
\qquad
|\mathbf a_{r,\tau}|=(|a_{i,r}^s(\tau)|)_{s\in E}.
\]

The selected-record normalizer cancels between numerator and denominator.

## Four bulk contributions

For a bulk patch of length `t`, the four orientation formulas are

\[
C_{II}(a,b;t)
=
\frac{e_a e^{tK_i}f_b^I}
{e_a e^{tB_i}f_b^I},
\]

\[
C_{IO}(a,r;t)
=
\frac{e_a e^{tK_i}f_r^O}
{e_a e^{tB_i}f_r^O},
\]

\[
C_{OI}(r,\tau;b;t)
=
\frac{\mathbf a_{r,\tau}e^{tK_i}f_b^I}
{|\mathbf a_{r,\tau}|e^{tB_i}f_b^I},
\]

\[
C_{OO}(r,\tau;r_e;t)
=
\frac{\mathbf a_{r,\tau}e^{tK_i}f_{r_e}^O}
{|\mathbf a_{r,\tau}|e^{tB_i}f_{r_e}^O}.
\]

## Typed bulk patch positivity

Because every realized denominator is positive, the exact generalized bulk positivity property is:

\[
e_a e^{tK_i}f_b^I\ge0,
\qquad
e_a e^{tK_i}f_r^O\ge0,
\]

\[
\mathbf a_{r,\tau}e^{tK_i}f_b^I\ge0,
\qquad
\mathbf a_{r,\tau}e^{tK_i}f_{r_e}^O\ge0
\]

for every realizable descriptor and every `t>0`.

This is an exact reformulation of nonnegative bulk patch contributions. It is **not** replaced by entrywise nonnegativity of `K_i` or `e^{tK_i}`.

## Short-time constraints

For distinct active types `a != r`, a realizable short `IO` patch gives

\[
\frac{d}{dt}\Big|_{t=0}
e_a e^{tK_i}e_r^T
=a_{i,a}^{r}(\emptyset).
\]

Hence typed bulk patch positivity forces

\[
a_{i,a}^{r}(\emptyset)\ge0
\]

whenever that descriptor is realizable.

Likewise a zero-length `OO` limit forces

\[
a_{i,r}^{r_e}(\tau)\ge0
\]

for every realizable active hidden outcome `r_e`.

These retyping constraints have no binary counterpart.

## Binary specialization

For `d=2`, write

\[
u=c_i^0(\emptyset),
\qquad
w=c_i^1(\emptyset),
\qquad
r=u+w.
\]

Then

\[
K_i=
\begin{pmatrix}
0&0\\u&-r
\end{pmatrix}.
\]

The resulting transfer functions are exactly the canonical `psi_i(t,1)` and `varphi_i(t)`. For nonempty target `S`, the outgoing signed row is

\[
(c_i^0(S),-c_i^0(S)-c_i^1(S)).
\]

Consequently all-length transfer positivity is equivalent to the paper's coefficient criterion

\[
c_i^0(S)+c_i^1(S)\le0,
\]

\[
c_i^1(\emptyset)c_i^0(S)
\ge
c_i^0(\emptyset)c_i^1(S)
\]

when `u+w>0`, and to `c_i\equiv0` when `u+w=0`.

Thus the finite-state transfer definition recovers canonical binary patch positivity exactly.

## Current open problem

The exact all-length semigroup-positive family is now known. The next question is whether it admits a tractable finite coefficient characterization for a nontrivial multi-state class, or whether a binary-style finite inequality criterion requires additional structure.

Applications and convergence are deliberately downstream of this coefficient problem.
