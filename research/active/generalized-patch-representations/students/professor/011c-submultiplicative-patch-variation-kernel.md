# 011c: submultiplicative killed patch-variation kernel

Date: 2026-08-17

## 1. Statement

For the finite-volume patch-variation kernels `R_t` defined in 011a,

\[
\boxed{
R_{t+s}(\xi,\zeta)
\le
\sum_{\eta}R_t(\xi,\eta)R_s(\eta,\zeta)
}
\tag{1.1}
\]

for every compatible typed states `xi,zeta` and all `s,t>=0`.

Equivalently,

\[
\boxed{R_{t+s}\le R_tR_s}
\tag{1.2}
\]

entrywise. Thus `R_t` is a positive **submultiplicative kernel family**.

The only boundary memory needed at a deterministic cut is the finite compatible typed dual configuration at that time.

## 2. Cut a candidate successful skeleton

Fix a candidate successful skeleton `g` on `[0,t+s]`. Ignore the null event of a selected point exactly at time `t`.

Write

\[
g^-:=g\cap(0,t],
\qquad
g^+:=g\cap(t,t+s],
\]

with the second list shifted to `[0,s]` when convenient.

Every source-time patch of the whole skeleton is either contained in one side of the cut or crosses time `t`. Cut each crossing patch into a left and right half-patch.

Conditional on a chosen local type `x in E` at the cut, the Poisson clocks and selected hidden marks in the two half-strips are independent. The Feynman--Kac potential is additive and the sign is multiplicative. Therefore a crossing patch factor satisfies the exact gluing identity

\[
F_P^{\mathrm{whole}}
=\sum_{x\in E}
F_{P^-}^{x}F_{P^+}^{x},
\tag{2.1}
\]

where `x=0` represents an inactive source line. Terms inconsistent with either half-skeleton are zero.

For several patches crossing the cut, multiplying (2.1) and summing over their compatible local cut types is exactly the same as summing over the global compatible typed configuration `eta` at time `t`.

Hence the complete signed skeleton contribution from 011a satisfies

\[
\boxed{
\Phi_{t+s}(g;\xi,\zeta)
=
\sum_{\eta}
\Phi_t(g^-;\xi,\eta)
\Phi_s(g^+;\eta,\zeta).}
\tag{2.2}
\]

Typed conflicts cause no extra term. An incompatible cut assignment has zero local consistency factor, and cemetery histories carry zero killed FK weight exactly as in Assignment 002.

## 3. Absolute value after coarse versus refined grouping

Apply the triangle inequality only after the whole-horizon patch expectations have already been formed:

\[
|\Phi_{t+s}(g;\xi,\zeta)|
\le
\sum_\eta
|\Phi_t(g^-;\xi,\eta)|
|\Phi_s(g^+;\eta,\zeta)|.
\tag{3.1}
\]

This has a useful interpretation. The whole-horizon successful skeleton leaves the hidden type at the deterministic cut unobserved. Revealing that type refines the conditioning. The `L^1` norm of a conditional expectation can increase under refinement, never decrease. Equation (3.1) is the exact patchwise realization of that principle.

## 4. Reference skeleton measure splits across the cut

On every fixed discrete-label component, the candidate-record measure is

\[
m_{t+s}(dg)=\prod_k\Lambda_{i_k,r_k}(\tau_k)dt_k.
\]

Splitting ordered times at the deterministic cut and shifting the second segment gives the product of the corresponding candidate-list measures on the two intervals. Future candidate labels need not be pre-screened against the cut state; impossible labels simply have zero consistency factor in `Phi_s`.

Therefore integrating (3.1), applying Tonelli, and summing over all candidate lists gives

\[
\begin{aligned}
R_{t+s}(\xi,\zeta)
&=\int|\Phi_{t+s}(g;\xi,\zeta)|m_{t+s}(dg)\\
&\le\sum_\eta
\left(\int|\Phi_t(g^-;\xi,\eta)|m_t(dg^-)\right)
\left(\int|\Phi_s(g^+;\eta,\zeta)|m_s(dg^+)\right)\\
&=\sum_\eta R_t(\xi,\eta)R_s(\eta,\zeta).
\end{aligned}
\]

This proves (1.1).

## 5. Weighted norm consequence

For any strictly positive weight `w` on the finite compatible typed-dual state space, define

\[
\|R_t\|_w
:=\sup_\xi\frac1{w(\xi)}
\sum_\zeta R_t(\xi,\zeta)w(\zeta).
\tag{5.1}
\]

Then

\[
\boxed{\|R_{t+s}\|_w\le\|R_t\|_w\|R_s\|_w.}
\tag{5.2}
\]

Together with 011a,

\[
|Q_t|\le R_t\le A_t,
\]

so any `R_T` contraction immediately yields a signed-FK coefficient contraction, while `R_T` may be strictly smaller than the raw absolute majorant `A_T` by 011b.

The remaining Assignment-011 question is therefore no longer composability. It is **usefulness**: can this strict, composable improvement cross a meaningful contraction/growth threshold under a natural or structural condition, rather than merely sitting numerically between `|Q_t|` and `A_t`?