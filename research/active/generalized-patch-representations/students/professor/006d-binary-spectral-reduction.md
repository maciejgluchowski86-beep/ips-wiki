# 006d: exact binary reduction of the spectral criterion

Date: 2026-08-17

This note executes Part E of Assignment 006. It checks that the finite spectral criterion of `006c` introduces no stronger binary condition.

## 1. Binary interior transfer

Suppress type `2`. Write

\[
u=c^0(\emptyset),
\qquad
w=c^1(\emptyset),
\qquad
r=u+w.
\]

The typed transfer matrix is

\[
K=
\begin{pmatrix}
0&0\\
u&-r
\end{pmatrix}.
\tag{1.1}
\]

There is only one active eigenvalue, `-r`. Thus every remaining outgoing-to-incoming numerator has **one** decaying mode. There is no two-mode critical-point branch and no Jordan branch.

For a nonempty binary target `S`, the outgoing signed row is

\[
p=\bigl(c^0(S),-c^0(S)-c^1(S)\bigr).
\tag{1.2}
\]

The zero-length `OO` condition is

\[
-c^0(S)-c^1(S)\ge0,
\]

i.e.

\[
\boxed{c^0(S)+c^1(S)\le0.}
\tag{1.3}
\]

The zero-length `OI` value is

\[
p_0+p_1=-c^1(S).
\]

As in Assignment 004, (1.3) together with the long-time inequality below yields the exact canonical condition without a separate stronger requirement.

## 2. Nondegenerate case `r>0`

The physical one-site chain at the reference neighbour has stationary weights proportional to `(w,u)` in the physical convention used by the canonical paper. Directly from (1.1), or from the binary patch formula, the `OI` numerator is

\[
N(t)
=c^0(S)-\bigl(c^0(S)+c^1(S)\bigr)
\left(\frac{u}{r}+\frac{w}{r}e^{-rt}\right).
\tag{2.1}
\]

Its long-time limit is

\[
L
=\frac{w c^0(S)-u c^1(S)}{r}.
\tag{2.2}
\]

Since there is only one exponential, all-time nonnegativity is equivalent to nonnegativity at the two endpoints. Under (1.3), the numerator is minimized at the long-time endpoint exactly as in the canonical proof. Hence the spectral test gives

\[
\boxed{w c^0(S)\ge u c^1(S).}
\tag{2.3}
\]

Substituting the definitions of `u,w` gives precisely

\[
\boxed{
c^1(\emptyset)c^0(S)
\ge
c^0(\emptyset)c^1(S).}
\tag{2.4}
\]

Together, (1.3) and (2.4) are exactly the canonical binary patch-positivity inequalities.

No distinct-active Metzler condition survives the suppression because there is only one active type.

## 3. Degenerate case `r=0`

Physical nonnegativity gives

\[
u=w=0.
\]

The active transfer has only eigenvalue zero and the spectral criterion has no interior condition. As proved in Assignment 004, the all-patch transfer conditions then force the nonconstant coefficients of `c^1` and `c^0+c^1` to be nonpositive. Their constant coefficients vanish and the underlying physical rates are nonnegative, so the binary Möbius argument gives

\[
\boxed{c\equiv0.}
\tag{3.1}
\]

Conversely the zero generator is trivially patch positive.

Thus the spectral criterion recovers the canonical exceptional clause exactly.

## 4. Conclusion

Suppressing type `2` reduces the Assignment-006 criterion to

\[
c^0(S)+c^1(S)\le0,
\qquad
c^1(\emptyset)c^0(S)
\ge c^0(\emptyset)c^1(S)
\]

for every nonempty target when `r>0`, and to `c\equiv0` when `r=0`.

This is exactly the coefficient criterion of the canonical patch paper. The interior critical-point condition disappears rather than becoming a stronger binary constraint.
