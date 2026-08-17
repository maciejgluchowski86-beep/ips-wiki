# 007d: exact symmetric-subclass criterion, honesty check, and binary reduction

Date: 2026-08-17

This note consolidates Parts D--E of Assignment 007 after the candidate classifications in `007a`--`007c`.

## 1. Exact boundary-complete symmetric criterion

Assume the reference-neighbour physical generator is

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix},
\qquad a,b,c\ge0,
\tag{1.1}
\]

and the full nonempty-target coefficient family is invariant under exchanging active labels `1` and `2`.

Under the boundary-complete hypothesis, typed bulk patch positivity is equivalent to the following local conditions.

### Interior condition

\[
\boxed{c\ge a.}
\tag{1.2}
\]

Indeed `K(1,2)=K(2,1)=c-a`, so (1.2) is exactly the short-`IO` Metzler condition from Assignment 005.

### Outgoing zero-length conditions

For every nonempty-target outgoing row

\[
p=(p_0,p_1,p_2),
\]

require

\[
\boxed{
p_1\ge0,
\qquad p_2\ge0,
\qquad p_0+p_1\ge0,
\qquad p_0+p_2\ge0.}
\tag{1.3}
\]

These are exactly the `OO` and `OI` zero-length conditions.

### Long-time condition

When `b+2a>0`, require

\[
\boxed{
(b+2a)p_0+a(p_1+p_2)\ge0.}
\tag{1.4}
\]

This is the stationary-average condition `L>=0`.

### Theorem 1.1

Conditions (1.2)--(1.4) are necessary and sufficient for typed bulk patch positivity inside the boundary-complete exchange-symmetric `d=3` subclass.

### Proof

Necessity of (1.2) and (1.3) is Assignment 005. Necessity of (1.4) follows by taking the long-patch limit of either `OI` numerator.

Under (1.2), `K` is Metzler, so all incoming-initial families are automatic. Under `p_1,p_2>=0`, all `OO` families are automatic.

For `OI`, use `007b`. With

\[
g=(p_0,p_0+p_1,p_0+p_2),
\qquad
m=(g_1+g_2)/2,
\qquad
d=(g_1-g_2)/2,
\]

one has

\[
N_1(t)=L+(m-L)e^{-(2a+b)t}+d e^{-(b+2c)t},
\]

\[
N_2(t)=L+(m-L)e^{-(2a+b)t}-d e^{-(b+2c)t}.
\]

If `p_0>=0`, then `g>=0` and Markov positivity settles both functions. If `p_0<0`, then `m-L>=0`. Moreover (1.2) gives

\[
b+2c\ge b+2a.
\]

For whichever of `N_1,N_2` has a negative antisymmetric coefficient, bound the faster exponential by the slower one. This gives the lower bound

\[
L+(g_b-L)e^{-(2a+b)t},
\]

which is a convex interpolation between the nonnegative endpoint values `L` and `g_b`. The other numerator has all modal coefficients nonnegative. Thus both are nonnegative for every time. This proves sufficiency. `square`

The criterion is endpoint/coefficient algebra only. The generic Assignment-006 critical power disappears.

## 2. Non-binary honesty

The exact positive gate in `007b` takes

\[
a=1,
\qquad b=2,
\qquad c=2
\]

and contains the outgoing row

\[
p=(-1/2,3/2,1).
\]

Its physical value vector is

\[
g=(-1/2,1,1/2).
\]

Thus

\[
N_1(0)=1\ne1/2=N_2(0).
\]

No observable on the two-block quotient `{0},{1,2}` can reproduce both initial values. The active labels remain observable.

The same physical gate has strictly positive transitions `1->2` and `2->1`, both active states have positive stationary mass, and the target-type-1 and target-type-2 rate perturbations are nontrivial label-swaps rather than identical perturbations.

Therefore the subclass is genuinely three-state according to Part D. Its simplification comes from spectral ordering forced by symmetry plus Metzler positivity, not from binary quotienting.

## 3. Why lumpability is not being advertised as the result

If additionally every outgoing row satisfies `p_1=p_2`, then every tested value function is constant on the active block. This is the exact lumpable quotient of `007a`, but it is observably binary and therefore does not count as the desired multi-state result.

The symmetric theorem above explicitly allows `p_1!=p_2`.

## 4. Why triangularity is not being advertised as the result

The Assignment-005 obstruction has exactly one active retyping direction and still has a negative interior critical value. Thus one-way conversion retains the generic spectral difficulty. `007c` records the exact witness.

## 5. Exact binary reduction

Suppress active type `2`. There is now only one active state, so all exchange-symmetry conditions involving two active labels disappear. In particular, (1.2) leaves **no** extra binary condition.

Write the binary reference-neighbour rates as

\[
u=c^0(\emptyset),
\qquad
w=c^1(\emptyset),
\qquad
r=u+w.
\]

Every two-state continuous-time chain is automatically a two-state refresh chain with destination rates `rho_1=u`, `rho_0=w`. For a nonempty binary target `S`, the outgoing signed row is

\[
p=(p_0,p_1)
=\bigl(c^0(S),-c^0(S)-c^1(S)\bigr).
\tag{5.1}
\]

The zero-length `OO` condition is

\[
p_1\ge0
\iff
\boxed{c^0(S)+c^1(S)\le0.}
\tag{5.2}
\]

The binary long-time condition is

\[
r p_0+u p_1\ge0.
\]

Substituting (5.1),

\[
r c^0(S)-u(c^0(S)+c^1(S))
=w c^0(S)-u c^1(S),
\]

so this is exactly

\[
\boxed{
c^1(\emptyset)c^0(S)
\ge
c^0(\emptyset)c^1(S).}
\tag{5.3}
\]

The binary zero-length `OI` value is

\[
p_0+p_1=-c^1(S).
\]

It imposes no stronger condition. Indeed, if `r>0` and (5.2)--(5.3) hold but `c^1(S)>0`, then (5.2) gives `c^0(S)<0`, and

\[
w c^0(S)-u c^1(S)<0,
\]

contradicting (5.3). Hence `c^1(S)<=0` follows from the canonical two inequalities exactly as in Assignment 004.

If `r=0`, then `u=w=0` and the exact degenerate analysis of Assignment 004 gives `c\equiv0`.

Thus suppressing type `2` recovers **exactly** the canonical binary patch-positivity criterion, with no stronger residual symmetry or endpoint condition.

## 6. Assignment-007 ruling

At least one tested natural subclass survives every gate:

- it is physically realizable;
- it is genuinely three-state;
- its criterion is necessary and sufficient inside the subclass;
- it is materially simpler than the generic spectral criterion;
- its binary reduction is exact.

Therefore the registered outcome is

\[
\boxed{\texttt{CONTINUE-NATURAL-THREE-STATE-SUBCLASS}.}
\]

No application or convergence claim is made in this block.
