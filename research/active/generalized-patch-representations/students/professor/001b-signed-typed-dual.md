# 001b: local signed typed dual and binary specialization

Date: 2026-08-17

This note executes Parts C--D of Assignment 001, using the coefficients from `001a-typed-generator-action.md`.

## 1. Signed typed state

Let `X` be the set of finite typed partial maps

\[
\xi:\Lambda\rightharpoonup E_*=E\setminus\{0\},
\]

and adjoin a cemetery state `dagger` with `H_dagger=0`.

For `xi in X` and `sigma in {+,-}`, put

\[
H((\xi,\sigma),\eta)=\sigma H_\xi(\eta).
\]

The cemetery state has duality function zero, independent of sign.

For an active source `i` of dual type `r=xi(i)`, typed neighbour target `tau in T(N(i))`, and source outcome `s in E`, let

\[
\Theta_{i;s,\tau}(\xi)
\]

be the map from (3.8) of 001a: remove `i`, reinsert it with type `s` if `s ne 0`, then compatibly merge the typed target `tau`; incompatible overlap gives `dagger`.

Write

\[
a_{i,r}^s(\tau)
\]

for the exact signed coefficients (3.5)--(3.7) of 001a.

## 2. Fixed local graphical clocks

For every local tuple

\[
(i,r,s,\tau),
\qquad r\in E_*,\ s\in E,\ \tau\in T(N(i)),
\]

except the empty-target source-survival tuple `(s,tau)=(r,empty)`, define

\[
\lambda_{i,r}^s(\tau)=|a_{i,r}^s(\tau)|,
\qquad
\epsilon_{i,r}^s(\tau)=\operatorname{sgn}_{\pm}(a_{i,r}^s(\tau)).
\tag{2.1}
\]

Attach an independent Poisson clock of rate `lambda` to this tuple.

At a ring:

- if the process is already at `dagger`, do nothing;
- if site `i` is not active with type `r`, ignore the ring;
- if `xi(i)=r`, apply `Theta_{i;s,tau}` and multiply the sign by `epsilon` unless the result is `dagger`.

The clock rate depends only on the fixed local tuple `(i,r,s,tau)`. Existing target labels influence only the deterministic merge/cemetery outcome. Thus target conflicts do **not** create state-dependent clock rates.

Let `D` be the generator of this signed typed process.

## 3. Potential

For an ordinary typed state define

\[
V(\xi)
=\sum_{i\in\operatorname{supp}\xi}v_{i,\xi(i)},
\tag{3.1}
\]

where

\[
\boxed{
v_{i,r}
=
\sum_{\substack{s\in E,\ \tau\in T(N(i))\\(s,\tau)\ne(r,\emptyset)}}
|a_{i,r}^s(\tau)|
+
a_{i,r}^r(\emptyset).}
\tag{3.2}
\]

Put `V(dagger)=0`.

The omitted tuple `(r,empty)` is exactly diagonal in the typed active configuration. Formula (3.2) is the direct finite-state analogue of putting the binary empty-target birth coefficient into the Feynman--Kac potential.

## 4. Generator identity

### Theorem 4.1 (local signed typed generator duality)

For every finite typed active state `Y=(xi,sigma)` and physical configuration `eta`,

\[
\boxed{
L_\eta H(Y,\eta)
=
D H(Y,\eta)+V(\xi)H(Y,\eta).}
\tag{4.1}
\]

### Proof

For every included branch, multiplying its nonnegative rate by its sign recovers the signed coefficient:

\[
\lambda_{i,r}^s(\tau)\epsilon_{i,r}^s(\tau)
=a_{i,r}^s(\tau).
\]

Therefore

\[
\begin{aligned}
D H(Y,\eta)
={}&
\sigma
\sum_{i\in\operatorname{supp}\xi}
\sum_{\substack{s,\tau\\(s,\tau)\ne(\xi(i),\emptyset)}}
a_{i,\xi(i)}^s(\tau)
H_{\Theta_{i;s,\tau}(\xi)}(\eta)
\\
&-
\sum_{i\in\operatorname{supp}\xi}
\sum_{\substack{s,\tau\\(s,\tau)\ne(\xi(i),\emptyset)}}
|a_{i,\xi(i)}^s(\tau)|H(Y,\eta).
\end{aligned}
\tag{4.2}
\]

This formula remains correct when `Theta=dagger`, because the corresponding target duality function is zero.

Adding (3.1)--(3.2) cancels the total jump-rate term and restores exactly

\[
\sigma\sum_{i\in\operatorname{supp}\xi}
a_{i,\xi(i)}^{\xi(i)}(\emptyset)H_\xi(\eta),
\]

which is the omitted diagonal branch of the exact generator expansion (3.9) in 001a. Hence (4.1) follows. `square`

## 5. Graphical locality and nonexplosion

Assume

\[
d<\infty,
\qquad
\sup_i|N(i)|\le m<\infty,
\qquad
\sup_{i,x\ne y,\eta}c_i^{x\to y}(\eta)\le C<\infty.
\tag{5.1}
\]

By the Mobius formula for the typed tensor basis,

\[
|\widehat c_i^{x\to y}(\tau)|
\le 2^{|\operatorname{supp}\tau|}C
\le2^m C.
\]

There are at most `d^m` typed targets and `d` source outcomes. Consequently the total dual clock rate at one active site is bounded by a constant depending only on `(d,m,C)`. One event adds at most `m` target sites. Therefore `|supp xi_t|` is dominated by a continuous-time branching process with linear rate and bounded offspring increment, so the typed dual is nonexplosive on bounded time intervals.

As in the binary paper, this does **not** by itself imply the exponential integrability required by the Feynman--Kac weight for every time. For an infinite-volume semigroup statement impose the analogue

\[
\boxed{
E_\xi\left[\exp\left(\int_0^t V(\xi_s)\,ds\right)\right]<\infty
\quad\text{for every finite }\xi\text{ and }t\ge0.}
\tag{5.2}
\]

Under the usual finite-speed exhaustion for the physical finite-state IPS and (5.2), the same finite-volume Feynman--Kac plus dominated-convergence argument as in `paper/appendices/monomial-dual.tex` gives

\[
\boxed{
P_tH_\xi(\eta)
=E_{\xi}\left[
\sigma_t
\exp\left(\int_0^tV(\xi_s)\,ds\right)
H_{\xi_t}(\eta)
\right],}
\tag{5.3}
\]

with `H_dagger=0`.

The genuinely new point for later patch work is not abstract existence of (5.3), but that the dual has **fixed local graphical clocks** and a finite source-outcome mark.

## 6. Exact binary specialization

Take

\[
E=\{0,1\},
\qquad r=1.
\]

A typed active configuration is now just a finite subset `A`: the unique non-reference type is suppressed. A typed target `tau` is exactly a subset `S subseteq N(i)`.

There are only two source outcomes.

### Source deletion

For `s=0`,

\[
a_{i,1}^{0}(S)
=\widehat c_i^{0\to1}(S).
\]

With the paper's notation this is

\[
\boxed{a_{i,1}^{0}(S)=c_i^0(S)=a_i^\delta(S).}
\]

The typed map removes the source and adds `S`:

\[
(A\setminus\{i\})\cup S.
\]

Thus `S=empty` is a death and `S ne empty` is a split.

### Source survival

For `s=r=1`,

\[
a_{i,1}^{1}(S)
=-\widehat c_i^{0\to1}(S)
-\widehat c_i^{1\to0}(S),
\]

so

\[
\boxed{a_{i,1}^{1}(S)
=-c_i^0(S)-c_i^1(S)=a_i^\beta(S).}
\]

The typed map leaves `i` active and unions `S`, exactly the paper's birth map.

For `S ne empty`, its absolute coefficient and sign are precisely `beta_i(S)` and `sigma_i^beta(S)`. For `S=empty`, the active set is unchanged and the coefficient is omitted from `D` and inserted directly in (3.2), exactly as `a_i^beta(empty)` is inserted in the binary potential.

Hence the typed construction specializes **identically**, without regrouping, to the paper's signed death/split/birth set process.

## 7. Exact finite verifier

`001-finite-state-duality-verifier.py` checks the local identity on the complete `d=3`, one-neighbour elementary basis family and separately checks the `d=2` reduction. It includes conflicting pre-existing typed target labels and verifies both the raw generator expansion and `D+V` identity.
