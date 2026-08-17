# Student G 010f checkpoint: insertion plus terminal high-pass is uniformly contractive

**Status:** intermediate durable checkpoint for Assignment 010.  This sharpens 010e to a strict contraction after one connected insertion, but the output norm contains the terminal high-pass factor `R_N`; an all-depth tail proof still requires an iterable comparison.

## 1. Sharpening the terminal kernel without root-finding

Keep the notation of 010e:

\[
R_NQ_N\equiv \int_0^\infty \kappa(t)P_t^N\,dt
\quad\hbox{modulo constants}.
\]

The coefficientwise exponential triangle bound in 010e was

\[
\|\kappa\|_1\le0.9829802443\ldots.
\]

The exact exponential decomposition contains, among other terms, a slow negative term

\[
-n e^{-\lambda t}
\]

and the corresponding `tau`-shifted positive term

\[
p e^{-(\lambda+\tau)t},
\qquad \tau=\frac4{125}.
\]

The exact verifier proves

\[
\frac pn>7.
\tag{1}
\]

For `3<=t<=50`,

\[
e^{\tau t}\le e^{8/5}<6<7.
\tag{2}
\]

The strict bound `e^{8/5}<6` is obtained without floating point from

\[
e^x<(1-x/10)^{-10}
\quad(0<x<10),
\]

at `x=8/5`, followed by the rational inequality

\[
\left(\frac{25}{21}\right)^{10}<6.
\]

Hence on the whole interval `[3,50]` the positive term dominates the negative one.  Pairing just these two terms improves the global triangle bound by at least twice the integral of the slow negative term on that interval.

Using only

\[
e^{-x}\ge1-x
\]

and the exact fact `1-50 lambda>0`,

\[
\int_3^{50}n e^{-\lambda t}\,dt
\ge47n(1-50\lambda).
\]

Therefore the exact algebraic quantity

\[
\boxed{
\Theta_\sharp
:=\Theta_{\rm tri}-94n(1-50\lambda)
}
\tag{3}
\]

satisfies

\[
\boxed{
\|\kappa\|_1\le\Theta_\sharp
\approx0.8924718201406568466.
}
\tag{4}
\]

The updated `010e-terminal-kernel-verifier.py` checks all algebraic premises and proves exactly

\[
\boxed{B\Theta_\sharp<1.}
\tag{5}
\]

Numerically,

\[
B\Theta_\sharp
\approx0.9807372831525678087.
\]

## 2. Oscillation cost of one centered insertion

Let `f` be a real function whose range contains zero.  Write

\[
m:=\min f\le0\le M:=\max f.
\]

The insertion multiplies by the new independent coordinate

\[
Y_{N+1}\in\{-c,g\},
\qquad c>g>0.
\]

Thus the range of `Y_{N+1}f` is contained in the four endpoint products

\[
-cM,\quad -cm,\quad gm,\quad gM.
\]

Consequently

\[
\operatorname{osc}(Y_{N+1}f)
\le
\max(cM,-gm)+\max(-cm,gM).
\]

Each maximum is bounded by the corresponding `c` or `g` contribution, giving the sharp elementary estimate

\[
\boxed{
\operatorname{osc}(Y_{N+1}f)
\le(c+g)(M-m)
=B\operatorname{osc}(f).
}
\tag{6}
\]

In the connected orbit every output of `Q_N` has zero `pi_N`-mean, so its range contains zero and `(6)` applies at every insertion.

## 3. A strict sandwiched connected contraction

Combining `(4)` and `(6)` with 010e gives, for every `pi_N`-centered `f`,

\[
\boxed{
\operatorname{osc}
\left(
R_{N+1}Q_{N+1}igl(Y_{N+1}f\bigr)
\right)
\le
q_\sharp\operatorname{osc}(f),
}
\tag{7}
\]

where

\[
\boxed{
q_\sharp:=B\Theta_\sharp<1.
}
\tag{8}
\]

This estimate is uniform in depth and uses the **actual** fixed filter and the actual generators at `P_*`.

It is a bounded-step/sign-sensitive contraction of precisely the kind not ruled out by 010a.  The cancellation occurs in the positive-frequency time kernel before absolute values are taken.

## 4. Remaining iteration problem

The actual connected orbit is

\[
f_{N+1}=Y_{N+1}Q_Nf_N.
\]

Estimate `(7)` controls `R_{N+1}Q_{N+1}f_{N+1}` by `osc(Q_Nf_N)`, or equivalently controls a full insertion when the **output** is measured through the high-pass seminorm

\[
f\mapsto\operatorname{osc}(R_Nf).
\]

What is still missing is a depth-uniform reverse comparison strong enough to recover `osc(Q_Nf_N)` from the preceding high-pass quantity.  Such a comparison cannot follow from invertibility of `R_N` on the full centered space: the scalar multiplier

\[
\frac{d+gx}{r+x}
\]

vanishes at the positive frequency

\[
x=\frac{|d|}{g}=\frac1{100}.
\]

Thus the next step must either use a second complementary high-pass observable or exploit additional structure of the **actual** connected orbit.  A one-norm iteration through `R_N^{-1}` is not available.
