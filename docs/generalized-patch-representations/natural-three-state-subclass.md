# Natural three-state positivity subclass

> **Research-branch result.** This page belongs only to `research/generalized-patch-representations`. It is not published on `main` and has not yet completed the planned literature/novelty audit.

The general finite-state patch theory reduces bulk patch positivity to local transfer-semigroup inequalities. In boundary-complete three-state systems, those inequalities are generically spectral: a remaining `OI` numerator can contain two decaying modes and may have a negative interior minimum even when its zero-length and long-time values are positive.

There is, however, a natural genuinely three-state subclass in which the exact criterion becomes algebraic again.

## Exchange-symmetric reference dynamics

Let the physical one-site chain, with neighbours frozen in the reference state, be invariant under exchange of active labels `1` and `2`:

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix},
\qquad a,b,c\ge0.
\]

Assume the nonempty-target coefficient family is invariant under the same active-label exchange and the local skeleton support is boundary-complete.

The symmetric and antisymmetric decay rates are

\[
\lambda_s=2a+b,
\qquad
\lambda_a=b+2c.
\]

The typed empty-target transfer satisfies

\[
K(1,2)=K(2,1)=c-a.
\]

Short incoming-to-outgoing patches therefore force

\[
\boxed{c\ge a.}
\]

This is the exact Metzler condition. It implies

\[
\lambda_a\ge\lambda_s,
\]

so the antisymmetric active-type mode is never slower than the symmetric mode.

## Exact outgoing criterion

For an outgoing nonempty-target row

\[
p=(p_0,p_1,p_2),
\]

define

\[
g=(p_0,p_0+p_1,p_0+p_2).
\]

The zero-length `OO` and `OI` conditions are

\[
\boxed{
p_1,p_2,p_0+p_1,p_0+p_2\ge0.}
\]

The long-time `OI` value is nonnegative exactly when

\[
\boxed{(b+2a)p_0+a(p_1+p_2)\ge0.}
\]

These conditions, together with `c>=a`, are not merely sufficient.

### Theorem

Inside the boundary-complete exchange-symmetric three-state subclass, typed bulk patch positivity is equivalent to

\[
c\ge a,
\]

and, for every outgoing row,

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\]

\[
(b+2a)p_0+a(p_1+p_2)\ge0.
\]

### Why no interior critical check remains

Write

\[
m=\frac{g_1+g_2}{2},
\qquad
d=\frac{g_1-g_2}{2},
\]

and

\[
L=\frac{b g_0+2a m}{b+2a}.
\]

Then

\[
N_1(t)=L+(m-L)e^{-\lambda_s t}+d e^{-\lambda_a t},
\]

\[
N_2(t)=L+(m-L)e^{-\lambda_s t}-d e^{-\lambda_a t}.
\]

If `p_0<0`, the zero-length inequalities give `m>=0` and

\[
m-L=\frac{b}{b+2a}(m-p_0)\ge0.
\]

Because `lambda_a>=lambda_s`, whichever numerator carries a negative antisymmetric coefficient is bounded below by

\[
L+(g_b-L)e^{-\lambda_s t},
\]

a convex interpolation between its nonnegative zero-length value and the nonnegative long-time value. The other numerator has nonnegative modal coefficients.

Thus the generic spectral critical point is eliminated by an exact ordering argument.

## Genuine three-state gate

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
\end{pmatrix}.
\]

One physically realizable outgoing row is

\[
p=(-1/2,3/2,1),
\]

so

\[
g=(-1/2,1,1/2).
\]

Its two `OI` numerators are

\[
N_1(t)=\frac18+\frac58e^{-4t}+\frac14e^{-6t},
\]

\[
N_2(t)=\frac18+\frac58e^{-4t}-\frac14e^{-6t}.
\]

Both are nonnegative for all time, but

\[
N_1(0)=1\ne1/2=N_2(0).
\]

Therefore the active types remain observable; the system is not a binary quotient. The physical gate also has positive `1<->2` transition rates and target-dependent perturbations that distinguish the active labels.

## Related structural cases

### Lumpable observables

If the physical chain is lumpable with respect to `{0},{1,2}` and every tested row satisfies `p_1=p_2`, the `OI` observable factors through a two-state quotient. This gives an exact one-mode criterion but is observably binary-reducible and is not counted as the genuinely multi-state result.

### Three-state refresh chains

If

\[
q_{xy}=\rho_y\quad(x\ne y),
\]

then the reference chain is a finite-state refresh chain with one nonzero decay rate. Every `OI` numerator is one-mode and the exact long-time condition becomes

\[
R p_0+\rho_1p_1+\rho_2p_2\ge0,
\qquad R=\rho_0+\rho_1+\rho_2.
\]

The symmetric case `c=a` is a special instance.

### One-way active retyping

Triangular active transfer does not simplify the exact criterion. The previously constructed physical obstruction already has exactly one active retyping direction and retains a negative interior minimum.

## Binary reduction

After suppressing type `2`, the two-active-label symmetry conditions disappear. The criterion reduces exactly to

\[
c^0(S)+c^1(S)\le0,
\]

\[
c^1(\emptyset)c^0(S)
\ge
c^0(\emptyset)c^1(S),
\]

with the canonical degenerate clause. No stronger binary condition remains.
