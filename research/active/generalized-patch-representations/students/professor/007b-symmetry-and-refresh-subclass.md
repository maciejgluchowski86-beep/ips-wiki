# 007b: active-type symmetry and the genuine refresh subclass

Date: 2026-08-17

This note executes Part B of Assignment 007 and identifies the surviving genuinely non-binary subclass.

## 1. Exchange-symmetric reference chain

Assume the physical reference-neighbour generator is invariant under exchanging active types `1` and `2`. Then for nonnegative rates `a,b,c`,

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix}.
\tag{1.1}
\]

The active-block partition is lumpable. The three spectral modes are:

- constants, eigenvalue `0`;
- the symmetric `0` versus active-block contrast, decay rate
  \[
  \lambda_s=2a+b;
  \]
- the antisymmetric active-type contrast `(0,1,-1)`, decay rate
  \[
  \lambda_a=b+2c.
  \]

For an outgoing row `p`, write

\[
g=(p_0,p_0+p_1,p_0+p_2),
\qquad
m=\frac{g_1+g_2}{2},
\qquad
d=\frac{g_1-g_2}{2}.
\]

The stationary average is

\[
L=\frac{b g_0+2a m}{b+2a}
\tag{1.2}
\]

when `b+2a>0`. Direct projection onto the symmetric and antisymmetric eigenspaces gives

\[
\boxed{
N_1(t)=L+(m-L)e^{-(2a+b)t}+d e^{-(b+2c)t},}
\tag{1.3}
\]

\[
\boxed{
N_2(t)=L+(m-L)e^{-(2a+b)t}-d e^{-(b+2c)t}.}
\tag{1.4}
\]

Thus active-type symmetry alone does **not** remove the two-mode critical comparison. It removes it in the observable-lumpable case `d=0`, but that is exactly the binary-reducible case `p_1=p_2` from `007a`.

## 2. Exact symmetric counterexample

Take

\[
a=1,
\qquad b=2,
\qquad c=0,
\]

so

\[
Q=
\begin{pmatrix}
-2&1&1\\
2&-2&0\\
2&0&-2
\end{pmatrix}.
\tag{2.1}
\]

The two decay rates are `4` and `2`. Choose the target-type-1 outgoing rows

\[
p^{1,1}=(0,1/4,0),
\qquad
p^{2,1}=(-4/5,17/20,11/4).
\tag{2.2}
\]

The corresponding indicator-basis rate perturbation, in transition order
`01,02,10,12,20,21`, is

\[
(0,-4/5,-3/10,1/20,-39/20,0).
\tag{2.3}
\]

Adding this to the reference rates `(1,1,2,0,2,0)` gives

\[
(1,1/5,17/10,1/20,1/20,0),
\tag{2.4}
\]

so every physical rate remains nonnegative.

For target type `2`, take the exact image of (2.3) under the exchange `1<->2`. The full one-neighbour coefficient family is therefore exchange-symmetric. Both source types and both target labels have positive coarse nonempty-target rate, so the local test is boundary-complete.

For the row `p^{2,1}`, the value function is

\[
g=(-4/5,1/20,39/20).
\]

Equation (1.3) gives

\[
N_1(t)=\frac1{10}-\frac{19}{20}e^{-2t}+\frac9{10}e^{-4t}.
\tag{2.5}
\]

Its endpoints are positive, but at `e^{-2t}=19/36`,

\[
N_1(t)=-217/1440<0.
\tag{2.6}
\]

Hence even full exchange symmetry of the reference dynamics and nonempty-target coefficient family does not by itself simplify Assignment 006.

## 3. Spectral coincidence inside the symmetric class

The two decay rates coincide exactly when

\[
2a+b=b+2c
\iff
\boxed{c=a.}
\tag{3.1}
\]

In that case every off-diagonal rate is determined only by the destination:

\[
q_{x0}=b\quad(x\ne0),
\qquad
q_{x1}=a\quad(x\ne1),
\qquad
q_{x2}=a\quad(x\ne2).
\tag{3.2}
\]

Thus the reference chain is a three-state refresh chain: at rate `b+2a`, refresh the state from

\[
\pi=(b,a,a)/(b+2a).
\]

The antisymmetric mode is not killed. Rather, it has the **same** decay rate as the symmetric mode. This distinction is important for the non-binary honesty check.

## 4. General refresh subclass

The symmetry assumption is unnecessary for this mechanism. Let

\[
\rho_0,\rho_1,\rho_2\ge0,
\qquad
R=\rho_0+\rho_1+\rho_2,
\]

and assume

\[
\boxed{q_{xy}=\rho_y\quad\text{for every }x\ne y.}
\tag{4.1}
\]

Then

\[
Q=R(\mathbf 1\pi-I),
\qquad
\pi=(\rho_0,\rho_1,\rho_2)/R,
\tag{4.2}
\]

when `R>0`, and hence

\[
\boxed{
e^{tQ}g
=\pi(g)\mathbf1+e^{-Rt}(g-\pi(g)\mathbf1).}
\tag{4.3}
\]

Equivalently, the typed transfer is

\[
K=
\begin{pmatrix}
0&0&0\\
\rho_1&-R&0\\
\rho_2&0&-R
\end{pmatrix}.
\tag{4.4}
\]

The two active decay modes are genuinely two-dimensional but spectrally degenerate.

## 5. Exact patch-positivity criterion in the refresh subclass

Under boundary completeness, Assignment 005 already makes incoming-initial and `OO` families automatic after the zero-length conditions. For every outgoing row

\[
p=(p_0,p_1,p_2),
\qquad
g=(p_0,p_0+p_1,p_0+p_2),
\]

require

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0.
\tag{5.1}
\]

For either incoming terminal type `b`, (4.3) gives

\[
N_b(t)
=L_p+(g_b-L_p)e^{-Rt},
\tag{5.2}
\]

with

\[
\boxed{
L_p=\pi(g)
=p_0+\frac{\rho_1p_1+\rho_2p_2}{R}.}
\tag{5.3}
\]

Therefore, when `R>0`, typed bulk patch positivity in the boundary-complete refresh subclass is **equivalent** to the finite algebraic conditions

\[
\boxed{
\begin{aligned}
p_1&\ge0,\\
p_2&\ge0,\\
p_0+p_1&\ge0,\\
p_0+p_2&\ge0,\\
R p_0+\rho_1p_1+\rho_2p_2&\ge0
\end{aligned}}
\quad\text{for every outgoing row }p.}
\tag{5.4}
\]

Necessity is given by zero-length and long-time patch limits. Sufficiency follows from the one-mode interpolation (5.2). No sufficient subcone is being substituted.

If `R=0`, the reference chain is frozen and the criterion reduces to the corresponding zero-length conditions, with the realizability restrictions inherited from the physical coefficient system.

## 6. Non-binary honesty

The refresh subclass is not a binary quotient. A row may have `p_1 != p_2`, hence `g_1 != g_2`, and (5.2) then gives distinct `N_1(0)` and `N_2(0)`. No observable on the quotient `{0},{1,2}` can reproduce both values.

The one-mode form comes instead from the repeated nonzero eigenvalue of the genuine three-state refresh generator.

The mandatory gate will use `rho=(2,1,1)` and a row with `p_1 != p_2`, positive internal physical transitions `1<->2`, and target-dependent rate perturbations which distinguish the active labels. Thus both active physical states remain present and observable.
