# Student G 010e checkpoint: a depth-uniform terminal positive-frequency contraction

**Status:** intermediate durable checkpoint for Assignment 010.  This proves a genuine all-depth connected estimate, but only for the terminal `pi J Q` interface; it does **not** yet prove the full tail `(T)` because the estimate has not yet been iterated through all internal insertions.

## 1. Exact boundary functional identity

Write

\[
r:=1+b,
\qquad
C_N(f):=\pi_{N+1}(Y_{N+1}f),
\]

for functions `f` on the first `N` sites, and let

\[
A_N(f):=\pi_{N+1}(f)
\]

be the corresponding prefix marginal functional.

Use the exact last-coordinate block recursion from 010c in the unnormalised `Y` basis.  With `P_N` the coefficient projection onto monomials containing site `N`, stationarity of `pi_{N+1}` gives, for all `u,v`,

\[
A_N(L_N+cP_N)+C_NP_N=0,
\tag{1}
\]

and

\[
A_N(dI+gcP_N)
+C_N(L_N-rI+gP_N)=0.
\tag{2}
\]

Multiplying `(1)` by `g` and eliminating `A_NP_N` from `(2)`, the `P_N` terms cancel **exactly**:

\[
C_N(rI-L_N)=A_N(dI-gL_N).
\]

Since `rI-L_N` is invertible,

\[
\boxed{
C_N=A_NR_N,
\qquad
R_N:=(dI-gL_N)(rI-L_N)^{-1}.
}
\tag{3}
\]

This identity is independent of depth and does not compare prefix marginals with `pi_N`.

At `P_*`, with

\[
\varepsilon=\frac9{10000},
\qquad
g_0:=g+\varepsilon=\frac{999}{10000},
\]

we have

\[
d=-\varepsilon r,
\qquad
d-gr=-g_0r.
\]

Therefore

\[
\boxed{
R_N=gI-g_0K_N,
\qquad
K_N:=r(rI-L_N)^{-1}.
}
\tag{4}
\]

`K_N` is the exponential-time resolvent Markov operator

\[
K_Nf=\int_0^\infty re^{-rt}P_t^Nf\,dt.
\tag{5}
\]

Thus `(3)` is a boundary high-pass identity: on an exact zero mode `R_N` acts by

\[
R_N(0)=\frac dr=-\varepsilon,
\]

while on fast modes its scalar multiplier approaches `g`.

## 2. Composition with the fixed connected resolvent

Let

\[
h(t):=w_*(t)\sigma(t),
\qquad
H_N=\int_0^\infty h(t)P_t^N\,dt,
\qquad
Q_N=H_N-z_\sigma\Pi_N.
\]

Since `R_N` is a rational function of `L_N`, it commutes with `H_N`, `Q_N`, and `Pi_N`.  Moreover

\[
R_N\Pi_N=-\varepsilon\Pi_N.
\]

Hence, modulo constants,

\[
R_NQ_N\equiv R_NH_N.
\tag{6}
\]

Using `(4)`--`(5)` and the semigroup property, `R_NH_N` is a signed time-convolution operator

\[
R_NH_Nf
=\int_0^\infty \kappa(t)P_t^Nf\,dt,
\tag{7}
\]

where

\[
\boxed{
\kappa
=g h-g_0(k_r*h),
\qquad
k_r(t)=re^{-rt}.
}
\tag{8}
\]

The kernel `kappa` is completely independent of `N`.

## 3. Exact algebraic `L1` bound for the terminal kernel

The actual one-particle survival transform is

\[
Z_\alpha
=\frac{\alpha+C}{(\alpha+\rho_-)(\alpha+\rho_+)},
\qquad
C=1+B+a,
\]

where

\[
\rho_\pm
=\frac{C\pm\sqrt{C^2-4aB}}2.
\]

Thus `h(t)=w_*(t)sigma(t)` is a four-exponential signed kernel.  Convolution with `k_r` adds only the exponent `r`, so `kappa` is a sum of five exponentials.

The exact verifier

`010e-terminal-kernel-verifier.py`

keeps the square root algebraic and proves the coefficient sign pattern exactly.  After combining equal exponents, the triangle inequality gives

\[
\boxed{
\|\kappa\|_{L^1(0,\infty)}
\le \Theta,
\qquad
\Theta
\approx0.9829802443964821630<1.
}
\tag{9}
\]

The strict inequality `Theta<1` is an exact symbolic comparison, not a floating-point assertion.

The same verifier checks

\[
\int_0^\infty\kappa(t)\,dt
=-\varepsilon z_\sigma
=-0.5009689080\ldots,
\tag{10}
\]

as required by the zero-frequency multiplier `R_N(0)=-epsilon`.

## 4. Uniform oscillation contraction

For a real function on a finite state space define

\[
\operatorname{osc}(f):=\max f-\min f.
\]

Every Markov semigroup contracts oscillation:

\[
\operatorname{osc}(P_t^Nf)\le\operatorname{osc}(f).
\]

The projection term in `R_NQ_N` is constant and therefore invisible to oscillation.  Equations `(7)`--`(9)` yield

\[
\boxed{
\operatorname{osc}(R_NQ_Nf)
\le
\Theta\,\operatorname{osc}(f),
\qquad
\Theta<1,
}
\tag{11}
\]

uniformly in `N`.

Furthermore

\[
\pi_NR_NQ_N
=-\varepsilon\pi_NQ_N=0.
\]

Therefore `R_NQ_Nf` has zero `pi_N`-mean, so its range straddles zero and

\[
\|R_NQ_Nf\|_\infty
\le\operatorname{osc}(R_NQ_Nf).
\tag{12}
\]

Since `A_N` in `(3)` is a probability functional, combining `(3)`, `(11)`, and `(12)` gives the all-depth terminal estimate

\[
\boxed{
|\pi_{N+1}J_{N+1}Q_Nf|
\le
\Theta\,\operatorname{osc}(f),
\qquad
\Theta<1.
}
\tag{13}
\]

## 5. What this does and does not solve

Equation `(13)` is a genuine positive-frequency contraction theorem for the exact connected operator.  It uses neither a finite-dimensional mode closure nor an invariant-law tail-shift estimate.  The prefix marginal `A_N` disappears behind a probability bound only **after** the exact stationarity cancellation `(1)`--`(3)` has inserted the high-pass factor `R_N`.

It also explains why simply bounding `Q_N` is the wrong problem: the stationary terminal insertion supplies an additional rational factor whose convolution with the fixed duration filter has total variation strictly below one.

However, `(13)` occurs only at the terminal `pi J Q` end of a connected block.  The internal maps are still

\[
Q_NJ_N,
\]

not `R_NQ_N`.  A proof of `(T)` now requires either:

1. an intertwining that propagates the factor `R_N` through an insertion so that `(11)` can be iterated; or
2. a second norm for the internal orbit which, together with the terminal contraction `(13)`, yields a summable all-depth bound.

Thus 010e materially narrows the connected-tail blocker but does not yet justify `(26.8)`.
