# 004b: unsigned consistency transfer

Date: 2026-08-17

This note executes Part B of Assignment 004.

## 1. Reference source-line process

Keep the notation of 004a. For active type `r in E_*`, define

\[
\rho_{i,r}=\sum_{s\ne r}|a_{i,r}^s(\emptyset)|,
\qquad
\kappa_{i,r}=\sum_{\tau\ne\emptyset}\sum_s|a_{i,r}^s(\tau)|.
\]

Under the reference patch law, while the local state is `r`:

- an empty-target branch `r -> s`, `s != r`, occurs at rate `|a_{i,r}^s(emptyset)|`;
- a matching nonempty-target branch occurs at total rate `kappa_{i,r}` and violates interior consistency;
- there is no Feynman--Kac potential and no sign weight.

State `0` is inactive and absorbing.

For a terminal test function `F:E -> R`, define

\[
(S_tF)(x)
=E_x[1_{\{\zeta>t\}}F(X_t)],
\tag{1.1}
\]

where `zeta` is the first matching nonempty-target clock.

## 2. Killed-Markov generator

The first-step expansion gives, for `r in E_*`,

\[
\boxed{
(B_iF)(r)
=
\sum_{s\ne r}|a_{i,r}^s(\emptyset)|
\bigl(F(s)-F(r)\bigr)
-\kappa_{i,r}F(r).
}
\tag{2.1}
\]

For the inactive state,

\[
\boxed{(B_iF)(0)=0.}
\tag{2.2}
\]

Equivalently, in matrix form,

\[
B_i(r,s)=|a_{i,r}^s(\emptyset)|\quad(s\ne r),
\]

\[
B_i(r,r)=-(\rho_{i,r}+\kappa_{i,r}),
\qquad r\in E_*,
\tag{2.3}
\]

and the entire row indexed by `0` is zero.

Thus

\[
\boxed{S_t=e^{tB_i}.}
\tag{2.4}
\]

The matrix `B_i` is the generator of a substochastic finite-state chain killed at the matching nonempty-target hazard.

## 3. Positivity and realizability

Every entry of `e^{tB_i}` is nonnegative. More precisely, for `t>0`,

\[
(e^{tB_i})(x,y)>0
\]

if and only if there is a directed path

\[
x=x_0\to x_1\to\cdots\to x_n=y
\]

using empty-target transitions with strictly positive rates

\[
|a_{i,x_k}^{x_{k+1}}(\emptyset)|>0,
\]

with the convention that `x=y` is allowed via the no-jump path. Finite killing rates only multiply such path probabilities by strictly positive survival factors and therefore do not change this reachability criterion.

For an initial probability row vector `mu` and a terminal consistency indicator `f>=0`,

\[
\mu e^{tB_i}f>0
\tag{3.1}
\]

exactly when at least one state in the support of `mu` can reach at least one state where `f=1` through positive-rate empty-target transitions before time `t`.

This is precisely the source-line realizability condition for the corresponding bulk descriptor under the killed skeleton. Consequently the denominators in the four formulas of 004c are strictly positive exactly for descriptors that can occur with positive noncemetery skeleton density.

At `t=0`, the same statement reduces to direct support overlap:

\[
\mu f>0.
\]

## 4. Contrast with the signed transfer

The numerator generator from 004a is

\[
K_i(r,s)=a_{i,r}^s(\emptyset)
\]

on active rows, with zero inactive row. The denominator generator instead keeps

- absolute off-diagonal empty-target rates;
- the full escape subtraction `-rho_{i,r}`;
- the nonempty-target killing `-kappa_{i,r}`.

There is no cancellation in `B_i` because the consistency normalizer carries neither jump signs nor the Feynman--Kac potential.
