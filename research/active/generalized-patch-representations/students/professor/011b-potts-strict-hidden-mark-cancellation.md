# 011b: exact strict hidden-mark cancellation in the Potts gate

Date: 2026-08-17

## 1. Descriptor

Use the verified Assignment-010 point

\[
z=1/2,\qquad q=1.
\]

For a source-type-1 successful record with singleton target type `1`, the outgoing signed row is

\[
p=(3/16,5/16,-3/16),
\qquad
\Lambda=\sum_s|p_s|=11/16.
\tag{1.1}
\]

End the source patch at an **incoming target of type `2`**. The corresponding terminal consistency column is

\[
f_2^I=e_0^T+e_2^T.
\]

This descriptor is realizable. Assignment 010 already verifies a positive-hazard source-type-2 singleton-target record; translating that record to a neighboring source gives an incoming target requiring type `2` at the present site. The outgoing hidden outcomes `0` and `2` both have positive absolute mass and are both compatible with that incoming target.

Thus this is exactly the geometry in which the successful record hides opposite signed outcomes that later coalesce into the same compatible incoming boundary.

## 2. Signed and raw-absolute interior transfer

At this parameter point,

\[
K=
\begin{pmatrix}
0&0&0\\
1/16&-33/16&15/16\\
1/16&15/16&-33/16
\end{pmatrix}.
\tag{2.1}
\]

All empty-target off-diagonal coefficients are nonnegative. Therefore the local raw-absolute FK transfer has the same matrix `M=K`; the only sign cancellation in this descriptor comes from the outgoing hidden row `p`.

For `F(t)=e^{tK}f_2^I`, write its active coordinates as

\[
F_1(t)=s(t)+d(t),
\qquad
F_2(t)=s(t)-d(t).
\]

Then

\[
s(t)=\frac1{18}+\frac49e^{-9t/8},
\qquad
d(t)=-\frac12e^{-3t}.
\tag{2.2}
\]

The signed unnormalized numerator is

\[
N(t)=pF(t)
=\frac3{16}+\frac{s(t)}8+\frac{d(t)}2,
\tag{2.3}
\]

while removing the outgoing signs before local averaging gives

\[
G(t)=|p|F(t)
=\frac3{16}+\frac{s(t)}2+\frac{d(t)}8.
\tag{2.4}
\]

The actual one-patch factors under the selected-record reference law are `N/Lambda` and `G/Lambda`.

## 3. Exact positive-length gate

Use the same exact positive length as Assignment 010,

\[
t_*=(8/3)\log(5/4).
\]

Then

\[
e^{-9t_*/8}=(4/5)^3=64/125,
\qquad
e^{-3t_*}=(4/5)^8=65536/390625.
\]

Hence

\[
s(t_*)=637/2250,
\qquad
d(t_*)=-32768/390625.
\]

Substitution into (2.3)--(2.4) gives

\[
N(t_*)=\frac{2544551}{14062500},
\]

\[
G(t_*)=\frac{17919551}{56250000}.
\]

After division by the common positive normalizer `Lambda=11/16`,

\[
\boxed{
|E_P[w_P1_{Con(P)}]|
=\frac{10178204}{38671875}
<
\frac{17919551}{38671875}
=E_P[|w_P|1_{Con(P)}].}
\tag{3.1}
\]

The exact gap is

\[
\frac{2580449}{12890625}>0.
\tag{3.2}
\]

This verifies that Assignment 011's envelope `R_t` can be strictly below the raw absolute-FK envelope `A_t` on a natural published model whose hidden-mark/cemetery geometry is already independently verified.

## 4. Interpretation

The gain is not due to signed empty-target evolution: `M=K` here. It comes solely from postponing the absolute value until after hidden outcomes `0` and `2` have propagated to the same incoming compatibility event.

Thus the strictness uses precisely the successful-skeleton coarse graining that survives the Assignment-008 novelty audit. The next question is whether this gain survives deterministic time cuts in a composable positive object.