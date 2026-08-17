# Student G 010i checkpoint: exact recentered insertion intertwining

**Status:** intermediate durable checkpoint for Assignment 010.  This identifies the precise branch which prevents the 010f high-pass contraction from iterating.  No tail theorem is claimed here.

## 1. Recenter the fresh coordinate

At `P_*`, retain

\[
r:=1+b=\frac{11}{10},\qquad
\varepsilon:=\frac9{10000},\qquad
d=-\varepsilon r,
\]

and put

\[
c_0:=c-\varepsilon=\frac{999}{1000},\qquad
g_0:=g+\varepsilon=\frac{999}{10000}.
\]

Thus

\[
B=c_0+g_0,
\qquad
X_i:=Y_i+\varepsilon=B\eta_i-c_0.
\tag{1}
\]

The variable `X_i` is centered under the Bernoulli law of density `1/(1+b)=10/11`, which is also the exact marginal law of the rightmost spin under every zero-boundary invariant law.

Let

\[
A_N:=-L_N.
\]

For functions on `N-1` sites, write `I_N` for the embedding which ignores the new coordinate, `M_{Y_N}` and `M_{X_N}` for multiplication by the new `Y_N` and `X_N`, and `P_{N-1}` for the old right-boundary `Y`-coefficient projection from 010c.

## 2. Two exact commutators

The 010c last-coordinate block gives, directly,

\[
\boxed{
A_N I_N
=I_NA_{N-1}-B\,M_{\eta_N}P_{N-1}.
}
\tag{2}
\]

Indeed `L_Nu=(L_{N-1}+cP_{N-1})u+Y_NP_{N-1}u` and `c+Y_N=B\eta_N`.

For the raw insertion, the same block gives

\[
A_NM_{Y_N}
=M_{Y_N}(A_{N-1}+r)
-dI_N-gB\,M_{\eta_N}P_{N-1}.
\tag{3}
\]

Using `M_X=M_Y+epsilon I`, `(2)`, and `d=-epsilon r`, the scalar defect cancels **exactly**:

\[
\boxed{
A_NM_{X_N}
=M_{X_N}(A_{N-1}+r)
-g_0B\,M_{\eta_N}P_{N-1}.
}
\tag{4}
\]

Thus a fresh recentered insertion shifts temporal frequency by the fixed amount `r=1.1`; the only failure of exact intertwining is the old right-boundary projection.

Equivalently, for every `s>0`,

\[
\boxed{
(s+A_N)^{-1}M_{X_N}
=M_{X_N}(s+r+A_{N-1})^{-1}
+g_0B(s+A_N)^{-1}M_{\eta_N}P_{N-1}(s+r+A_{N-1})^{-1}.
}
\tag{5}
\]

This is an exact resolvent identity, not a perturbative expansion.

## 3. Exact semigroup version

Changing signs in `(2)` and `(4)` and applying Duhamel gives

\[
e^{tL_N}M_{X_N}
=e^{-rt}M_{X_N}e^{tL_{N-1}}
+g_0B\int_0^t e^{(t-s)L_N}M_{\eta_N}P_{N-1}e^{-rs}e^{sL_{N-1}}\,ds,
\tag{6}
\]

and

\[
e^{tL_N}I_N
=I_Ne^{tL_{N-1}}
+B\int_0^t e^{(t-s)L_N}M_{\eta_N}P_{N-1}e^{sL_{N-1}}\,ds.
\tag{7}
\]

Subtracting `epsilon` times `(7)` from `(6)` yields the raw-insertion identity

\[
\boxed{
\begin{aligned}
e^{tL_N}M_{Y_N}
={}&e^{-rt}M_{Y_N}e^{tL_{N-1}}
+\varepsilon(e^{-rt}-1)I_Ne^{tL_{N-1}}\\
&+B\int_0^t e^{(t-s)L_N}M_{\eta_N}P_{N-1}
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}\,ds.
\end{aligned}
}
\tag{8}
\]

This separates every connected extension into three exact pieces:

1. a fresh high-frequency branch carrying `e^{-rt}`;
2. a non-shifted scalar branch carrying the small coefficient `epsilon`;
3. a boundary-transmission branch, and **only** that branch, containing `P_{N-1}`.

The coefficient in the boundary branch itself retains sign:

\[
g_0e^{-rs}-\varepsilon,
\tag{9}
\]

so replacing it by its absolute value before the time integration loses a genuine cancellation.

## 4. Why the first two branches are not the blocker

Write the fixed signed time kernel as

\[
h(t):=w_*(t)\sigma(t),
\qquad
H_N=\int_0^\infty h(t)e^{tL_N}\,dt.
\]

For the fresh branch in `(8)`, the time kernel is `h(t)e^{-rt}`.  Since the new centered variable `X_N` takes the values `-c_0,g_0`, multiplication by `X_N` has oscillation cost at most `B`.  The exact singleton calculation already made in 010c gives

\[
\int_0^\infty |h(t)|e^{-rt}\,dt
=|F(r)|
=\frac{5240305525}{6117276447}
\approx0.8566402991,
\tag{10}
\]

(the equality with the absolute integral holds because the filter sign-change occurs so late that the corresponding exponentially shifted scalar expression has the displayed sign; alternatively only the numerical interpretation of the last equality may be omitted and the rational `F(r)` retained).  In particular

\[
B|F(r)|\approx0.94136<1.
\tag{11}
\]

For the unshifted scalar branch, the completely crude admissibility bound `|sigma|<=1` already gives

\[
\varepsilon\int_0^\infty w_*(t)|\sigma(t)|\,dt
\le\varepsilon Z
=\frac9{10000}\frac{19100}{31}
\approx0.55452<1.
\tag{12}
\]

Hence neither the fresh shifted channel nor the scalar `Y=X-epsilon` defect is by itself supercritical in a depth-uniform oscillation estimate.

The unresolved term is precisely the last line of `(8)`: long-time boundary transmission through

\[
M_{\eta_N}P_{N-1}.
\tag{13}
\]

A proof which takes absolute values on `(9)` before using the centered structure is far too large, because the slow part of `h` survives.  Therefore an all-depth proof must retain cancellation in this boundary-transmission branch (or control `P_{N-1}` on the actual connected orbit by another seminorm).

## 5. A second exact positive identity for a fresh insertion

There is also a useful stationary second-moment identity.  From

\[
Y_N^2=(g-c)Y_N+cg
\]

and the 010e terminal identity

\[
\pi_N(Y_Nf)=A_{N-1}R_{N-1}f,
\qquad
R_{N-1}=gI-g_0K_{N-1},
\]

where

\[
K_{N-1}=r(rI-L_{N-1})^{-1}
\]

is Markov, one obtains for every real `f` on `N-1` sites

\[
\boxed{
\pi_N(Y_N^2f^2)
=A_{N-1}\Bigl[
 g^2I+(c-g)g_0K_{N-1}
\Bigr]f^2.
}
\tag{14}
\]

Both coefficients on the right are positive, and their sum is

\[
\boxed{
g^2+(c-g)g_0=\frac{9980091}{100000000}=0.09980091.}
\tag{15}
\]

Thus the `L^2` cost of a fresh insertion is itself a positive Markov-resolvent expression.  The remaining issue for turning `(14)` into a recursive Hilbert estimate is not the insertion but comparison of the prefix marginal `A_{N-1}` with the stationary law used by the preceding connected step.

## 6. Narrowed continuation target

Equations `(4)`--`(9)` rule out a vague attribution of the difficulty to the entire non-reversible hierarchy.  The exact remaining obstruction is the boundary-transmission branch.  A sufficient continuation would be either

- a two-component depth-uniform seminorm controlling both the connected profile and `P_N` of that profile, with strict contraction after integrating `(8)` against the fixed `h`; or
- an `L^2` comparison which combines `(14)` with the centered resolvent and closes uniformly in `N`.

No larger coefficient table or filter change is involved.
