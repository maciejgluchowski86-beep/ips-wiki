# 007b: active-type symmetry gives an exact non-binary subclass

Date: 2026-08-17

This note executes Part B of Assignment 007 and corrects an initial over-hasty symmetry classification. The correction is substantive: once the already-necessary Metzler inequalities from Assignment 005 are imposed, exchange symmetry does simplify the exact spectral criterion.

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

The three spectral modes are:

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

when `b+2a>0`. Direct projection gives

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

The modes separate, but an admissible row need not kill the antisymmetric mode: `d` may be nonzero.

## 2. The Assignment-005 Metzler condition changes the sign geometry

For the symmetric chain, the typed empty-target transfer has

\[
K(1,2)=K(2,1)=c-a.
\tag{2.1}
\]

Boundary completeness plus typed patch positivity therefore forces

\[
\boxed{c\ge a.}
\tag{2.2}
\]

This is exactly the short-`IO` Metzler condition. Consequently

\[
\lambda_a=b+2c\ge b+2a=\lambda_s.
\tag{2.3}
\]

Thus the antisymmetric mode is never slower than the symmetric mode.

The first draft of this note used `c<a` to produce an interior dip. That example violates (2.2) and therefore cannot test the candidate positivity class. It is discarded rather than used as evidence.

## 3. Exact endpoint criterion under symmetry

Assume now the zero-length outgoing inequalities from Assignment 005:

\[
p_1,p_2,g_1,g_2\ge0.
\tag{3.1}
\]

If `p_0=g_0>=0`, then `g>=0` and every `OI` numerator is automatic by Markov positivity.

Suppose `g_0<0`. Then `m>=0` and

\[
\boxed{
m-L=\frac{b}{b+2a}(m-g_0)\ge0.}
\tag{3.2}
\]

Assume also the long-time condition

\[
L\ge0.
\tag{3.3}
\]

We prove `N_1,N_2>=0` for all time.

Consider `N_1`. If `d>=0`, every term in (1.3) is nonnegative. If `d<0`, then by (2.3)

\[
e^{-\lambda_a t}\le e^{-\lambda_s t},
\]

and multiplication by the negative number `d` reverses the inequality:

\[
d e^{-\lambda_a t}\ge d e^{-\lambda_s t}.
\]

Hence

\[
N_1(t)
\ge L+(m-L+d)e^{-\lambda_s t}
=L+(g_1-L)e^{-\lambda_s t}.
\tag{3.4}
\]

The right side is a convex interpolation between `g_1>=0` and `L>=0`, so it is nonnegative. The proof for `N_2` is identical after replacing `d` by `-d`.

Therefore, inside the boundary-complete exchange-symmetric class, typed bulk patch positivity is equivalent to:

1. the Metzler inequality `c>=a`;
2. for every outgoing row,
   \[
   p_1,p_2,p_0+p_1,p_0+p_2\ge0;
   \]
3. the single long-time inequality
   \[
   \boxed{L=\frac{b p_0+a(p_0+p_1)+a(p_0+p_2)}{b+2a}\ge0.}
   \tag{3.5}
   \]

Equivalently, when `b+2a>0`,

\[
\boxed{(b+2a)p_0+a(p_1+p_2)\ge0.}
\tag{3.6}
\]

These conditions are **necessary and sufficient** within the subclass. No interior spectral evaluation remains.

## 4. This is genuinely non-binary

The simplification does not require `p_1=p_2`. The antisymmetric coefficient `d` may be nonzero, and then

\[
N_1(0)=g_1\ne g_2=N_2(0).
\]

Thus the tested observable does not factor through the quotient `{0},{1,2}`. The active-type distinction remains visible.

The mechanism is instead spectral ordering: the only potentially signed antisymmetric contribution decays at least as fast as the nonnegative symmetric contribution.

## 5. Exact non-binary positive gate

Take

\[
a=1,
\qquad b=2,
\qquad c=2.
\]

Then

\[
Q=
\begin{pmatrix}
-2&1&1\\
2&-4&2\\
2&2&-4
\end{pmatrix},
\tag{5.1}
\]

with decay rates `4` and `6`, and

\[
K=
\begin{pmatrix}
0&0&0\\
1&-5&1\\
1&1&-5
\end{pmatrix}.
\tag{5.2}
\]

For target type `1`, choose outgoing rows

\[
p^{1,1}=(0,1/4,1/4),
\qquad
p^{2,1}=(-1/2,3/2,1).
\tag{5.3}
\]

The corresponding indicator-basis rate perturbation in transition order
`01,02,10,12,20,21` is

\[
(0,-1/2,-5/4,1,-3/4,1/4).
\tag{5.4}
\]

Adding (5.4) to the reference rates `(1,1,2,2,2,2)` gives

\[
(1,1/2,3/4,3,5/4,9/4),
\tag{5.5}
\]

all strictly positive. For target type `2`, take the exact image under `1<->2`; the full one-neighbour system is exchange-symmetric and all 18 physical rates are nonnegative.

For the distinguished row,

\[
g=(-1/2,1,1/2),
\qquad
m=3/4,
\qquad
d=1/4,
\qquad
L=1/8.
\]

Hence

\[
N_1(t)=\frac18+\frac58e^{-4t}+\frac14e^{-6t},
\tag{5.6}
\]

\[
N_2(t)=\frac18+\frac58e^{-4t}-\frac14e^{-6t}.
\tag{5.7}
\]

Both are nonnegative for every `t>=0`, and `N_1(0)=1`, `N_2(0)=1/2` prove that the observable does not factor through a binary active block.

Both active physical states occur with positive stationary probability, the physical chain has positive transitions `1<->2`, and the target-type perturbations are swapped rather than identical. The model is therefore genuinely three-state under the honesty test.

## 6. Nonvacuity inside the same subclass

The same reference chain admits physically realizable outgoing rows satisfying all zero-length inequalities but violating the long-time condition. For example

\[
p=(-1/2,1,1/2)
\]

gives

\[
g=(-1/2,1/2,0),
\qquad
L=-1/8<0.
\]

It can be realized by pairing it with `p^{1,1}=(0,1/4,1/4)`; the resulting target-mode rate perturbation is

\[
(0,-1/2,-3/4,1/2,-1/4,1/4),
\]

which remains physical after adding the reference rates. Thus (3.6) is a genuine necessary condition, not an automatically satisfied consequence of realizability.

## 7. Refresh chains as a boundary case and broader one-mode subclass

When `c=a`, the two decay rates coincide. The symmetric chain becomes a three-state refresh chain with destination rates `(b,a,a)`.

More generally, if

\[
q_{xy}=\rho_y\quad(x\ne y),
\]

then the reference chain is a possibly asymmetric three-state refresh chain. Writing `R=sum_y rho_y` and `pi_y=rho_y/R`,

\[
e^{tQ}g=\pi(g)\mathbf1+e^{-Rt}(g-\pi(g)\mathbf1).
\]

Therefore all `OI` numerators are one-mode, even for `p_1!=p_2`. The exact criterion is the zero-length inequalities plus

\[
R p_0+\rho_1p_1+\rho_2p_2\ge0.
\]

This is another genuinely three-state exact subclass. It is a special repeated-spectrum mechanism, while the larger symmetric class with `c>a` works by ordered decay rates.
