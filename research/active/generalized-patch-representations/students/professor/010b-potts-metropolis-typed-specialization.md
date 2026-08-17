# 010b: exact typed specialization of three-state Potts Metropolis dynamics

Date: 2026-08-17

This note executes Assignment 010 Part B for the model selected and frozen in `010a` before any positivity calculation.

## 1. Physical single-site replacement rates

Use colors

\[
E=\{0,1,2\}
\]

on the square lattice, with reference color `0`. Let `n_a` be the number of the four nearest neighbors in color `a`. Put

\[
z=e^{-\beta J}\in(0,1],
\qquad q>0,
\]

where `q` is the common proposal-rate prefactor for either alternative color.

For source color `x` and proposed target color `y!=x`, the Metropolis energy difference is

\[
H(\eta^{i:x\to y})-H(\eta)=J(n_x-n_y).
\]

Hence the continuous-time Poissonized replacement rate is

\[
\boxed{
c^{x\to y}(n_0,n_1,n_2)
=qz^{(n_x-n_y)_+}.}
\tag{1.1}
\]

All six replacement rates are strictly positive for `q>0` and `z>0`. No vacancy/birth distinction is present: every color directly replaces every other color.

## 2. Exact indicator-tensor coefficients

Let a typed target pattern `tau` contain `k_1` specified neighbors of type `1` and `k_2` specified neighbors of type `2`, with

\[
k_1+k_2\le4.
\]

All other target sites are absent from `tau`. By color/permutation symmetry the physical tensor coefficient depends only on `(k_1,k_2)`.

For a physical transition `x->y`, Möbius inversion in the reference-state indicator basis gives

\[
\boxed{
\widehat c^{x\to y}_{k_1,k_2}
=
\sum_{i=0}^{k_1}\sum_{j=0}^{k_2}
(-1)^{k_1-i+k_2-j}
\binom{k_1}{i}\binom{k_2}{j}
qz^{(n_x(i,j)-n_y(i,j))_+},}
\tag{2.1}
\]

where

\[
n_0(i,j)=4-i-j,
\qquad n_1(i,j)=i,
\qquad n_2(i,j)=j.
\tag{2.2}
\]

Equation (2.1) is a complete exact specification of every target coefficient. In particular, reconstructing the physical rate at an arbitrary neighbor configuration gives

\[
c^{x\to y}(\eta_N)
=
\sum_{\tau\subseteq\eta_N^{\ne0}}
\widehat c^{x\to y}(\tau),
\tag{2.3}
\]

where the sum is over typed subpatterns compatible with the nonreference neighbors. The exact verifier checks this identity for all `3^4` neighbor configurations and all six directed color replacements.

## 3. Typed dual coefficient rows

For active dual type `r`, write

\[
\mathbf a_{r;k_1,k_2}
=(a_r^0,a_r^1,a_r^2).
\]

Assignment 001 gives

\[
a_r^0=\widehat c^{0\to r},
\]

\[
a_r^s=\widehat c^{s\to r}-\widehat c^{0\to r}
\quad(s\ne0,r),
\]

\[
a_r^r=-\widehat c^{0\to r}-\sum_{y\ne r}\widehat c^{r\to y}.
\tag{3.1}
\]

For `r=1`, the nonempty target-count rows are as follows. Every displayed polynomial is multiplied by `q`.

\[
\begin{array}{c|ccc}
(k_1,k_2)&a_1^0/q&a_1^1/q&a_1^2/q\\ \hline
(0,1)&-z^3(z-1)&z^3(z-1)&(z-1)(z+1)(z^2-z+1)\\
(1,0)&-z^2(z-1)(z+1)&(z-1)(z^3+z^2-1)&z^2(z-1)(z+1)\\
(0,2)&z^2(z-1)^2&-z^2(z-1)^2&-(z-1)^3(z+1)\\
(1,1)&z(z-1)^2(z+1)&-(z-1)(z^3-z-1)&-(z-1)(z^3-z+1)\\
(2,0)&(z-1)^2(z+1)^2&-(z-1)^2(z^2+2z+2)&-(z-1)^2(z+1)^2\\
(0,3)&-z(z-1)^3&z(z-1)^3&(z-1)^3(z+1)\\
(1,2)&-(z-1)^3(z+1)&z(z-1)(z^2-z-1)&(z-1)(z^3-z^2-2z+3)\\
(2,1)&-z(z-1)(z^2-2)&(z-1)(z^3-z-3)&(z-1)^2(z^2+z-1)\\
(3,0)&-(z-1)(z+1)(z^2-2)&(z-1)(z^3-z-4)&(z-1)(z+1)(z^2-2)\\
(0,4)&(z-1)^4&-(z-1)^4&0\\
(1,3)&(z-1)(z^3-2z^2+2)&-(z-1)(z^3-2z^2+2)&-(z-1)(z^3-z^2-3z+5)\\
(2,2)&(z-1)^2(z^2-2)&-(z-1)(z^3-z^2-2)&-(z-1)(z^3-z^2-3z+5)\\
(3,1)&z(z-1)(z^2-3)&-(z-1)(z^3-6)&-(z-1)(z^3-3z+1)\\
(4,0)&(z-1)(z+1)(z^2-3)&-(z-1)(3z^3-z^2-3z-7)&-(z-1)(z+1)(z^2-3)
\end{array}
\tag{3.2}
\]

The `r=2` table is obtained exactly by exchanging colors `1` and `2`: replace `(k_1,k_2)` by `(k_2,k_1)` and exchange row components `1` and `2`.

This table plus the empty-target rows below is the complete typed coefficient specialization.

## 4. Empty-target transfer

With every neighbor in reference color `0`, (3.1) gives

\[
\mathbf a_{1;0,0}
=
q\bigl(z^4,-(z^4+2),1-z^4\bigr),
\tag{4.1}
\]

\[
\mathbf a_{2;0,0}
=
q\bigl(z^4,1-z^4,-(z^4+2)\bigr).
\tag{4.2}
\]

Therefore the signed weighted interior transfer is

\[
\boxed{
K=q
\begin{pmatrix}
0&0&0\\
z^4&-(z^4+2)&1-z^4\\
z^4&1-z^4&-(z^4+2)
\end{pmatrix}.}
\tag{4.3}
\]

For `0<z<=1`, `K` is Metzler. The two active types retype each other at positive signed-transfer rate `q(1-z^4)` whenever `z<1`.

## 5. A decisive singleton successful record

Take a target pattern consisting of one neighbor with typed target color `1`, so `(k_1,k_2)=(1,0)`, and pre-source dual type `r=1`. From (3.2),

\[
\boxed{
\mathbf p:=\mathbf a_{1;1,0}
=
\left(
qz^2(1-z^2),
q(z-1)(z^3+z^2-1),
-qz^2(1-z^2)
\right).}
\tag{5.1}
\]

For every finite positive inverse temperature,

\[
0<z<1,
\]

one has

\[
p_0=qz^2(1-z^2)>0,
\qquad
p_2=-qz^2(1-z^2)<0.
\tag{5.2}
\]

Hence this successful record has at least two distinct post-source outcomes `0` and `2` with positive **absolute** hidden branch rates. Except at one isolated algebraic value where `p_1=0`, it has all three hidden outcomes. In particular the post-source outcome is not deterministic.

This directly passes the first half of Assignment 010's hidden-mark honesty gate: the successful skeleton genuinely forgets local information that affects the signed patch contribution.

## 6. Realizable typed cemetery conflicts

The same coefficient family contains successful records whose target pattern requires a neighboring active label of type `1` and, by color symmetry, records requiring type `2`.

A target type `1` merged onto a dual site currently carrying type `2` is inconsistent and sends the typed dual to cemetery. Such a type-2 active label is realizable, for example, from the hidden outcome `2` in (5.1), from an initial type-2 observable, or from the positive empty-target retyping in (4.3).

Thus typed target conflict/cemetery is not a formal possibility absent from this model. The killed/noncemetery repair of Assignment 002 is genuinely relevant to conditioning on the coarse successful skeleton.

## 7. Exact physical-generator check to be used in the verifier

At the exact gate

\[
z=1/2,
\qquad q=1,
\tag{7.1}
\]

all physical replacement rates in (1.1) are positive rationals. The mandatory verifier will:

1. construct every coefficient by (2.1) using `fractions.Fraction`;
2. reconstruct all six rates for all `81` nearest-neighbor color configurations;
3. reconstruct the corresponding typed generator action;
4. check the singleton row (5.1), the transfer matrix (4.3), and the realized hidden/cemetery support exactly.

No floating-point sign decision is needed.
