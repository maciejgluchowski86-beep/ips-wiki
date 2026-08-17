# Student G 010h checkpoint: exact recentered boundary channel and complementary high-pass split

**Status:** intermediate durable checkpoint for Assignment 010.  This sharpens the 010c/010f block algebra and identifies the complementary observable missing from the positive-frequency factor `R_N`.  It does **not** by itself prove the connected tail `(T)`: the remaining issue is to turn the two channel bounds below into an iterable estimate on the actual connected orbit.

**Correction note.**  The first version of this checkpoint correctly conjugated the last-coordinate block but then incorrectly called the resulting `P_N` coupling symmetric in the product `X`-Hilbert structure.  `P_N` is the coefficient projection in the old `Y` basis, and after recentering it is a small non-orthogonal tilt of the `X`-coordinate projection.  Equations `(1)`--`(5)` and all of Sections 3--5 are unchanged; Section 2 below gives the corrected geometry.

## 1. Recenter at the autonomous right-boundary mean

Retain

\[
r=1+b=\frac{11}{10},\qquad
m_0=\frac dr=-\frac9{10000}.
\]

Instead of the insertion coordinate `Y_i`, put

\[
\boxed{X_i:=Y_i-m_0=Y_i+\frac9{10000}.}
\tag{1}
\]

Then

\[
c_0:=c+m_0=\frac{999}{1000},\qquad
g_0:=g-m_0=\frac{999}{10000},
\tag{2}
\]

and

\[
X_i\in\{-c_0,g_0\},\qquad c_0+g_0=B.
\]

This is exactly the product-centered coordinate of the nearby reversible point from 010d.  The actual connected insertion is

\[
\boxed{Y_i=X_i+m_0.}
\tag{3}
\]

Thus the failure of product centering is an explicit scalar channel of size `|m_0|=9/10000`.

## 2. The scalar `I` off-diagonal disappears, but the boundary projection is tilted

In the `Y` decomposition `f=u+Y_{N+1}v`, 010c proved

\[
L_{N+1}
=
\begin{pmatrix}
L_N+cP_N & dI+gcP_N\\
P_N & L_N-rI+gP_N
\end{pmatrix},
\tag{4}
\]

where `P_N` is the coefficient projection onto `Y`-monomials containing the old rightmost site `N`.

Since

\[
f=u_X+X_{N+1}v=(u_X-m_0v)+Y_{N+1}v,
\]

conjugating `(4)` in the **newest coordinate only** gives the exact algebraic block identity

\[
\boxed{
L_{N+1}
=
\begin{pmatrix}
L_N+c_0P_N & c_0g_0P_N\\
P_N & L_N-rI+g_0P_N
\end{pmatrix}
}
\tag{5}
\]

in the `(u_X,v)` coordinates.  The scalar top-right term cancels because

\[
d-m_0r=0,
\]

and the remaining coefficient factors exactly as

\[
gc-cm_0+gm_0-m_0^2=(c+m_0)(g-m_0)=c_0g_0.
\]

The important qualification is that `P_N` in `(5)` has **not** become the orthogonal projection associated with the product-centered coordinate `X_N`.  Put

\[
s_0:=\sqrt{c_0g_0},\qquad
\phi_N:=\frac{X_N}{s_0}.
\]

For a function written in the product decomposition

\[
f=u+\phi_Nv,
\]

we have

\[
f=\left(u-\frac{m_0}{s_0}v\right)+Y_N\frac{v}{s_0},
\]

and hence

\[
\boxed{
P_N(u+\phi_Nv)=\phi_Nv+\beta v,
\qquad
\beta:=\frac{m_0}{s_0}
=-\frac{\sqrt{10}}{1110}.
}
\tag{6}
\]

Thus, in the product `X`-Hilbert structure, the old `Y`-projection is the rank-one idempotent

\[
\boxed{
P_N^{(X)}=
\begin{pmatrix}
0&\beta I\\
0&I
\end{pmatrix},
}
\tag{7}
\]

not an orthogonal projection.  Its non-orthogonal tilt is nevertheless explicit and small:

\[
|\beta|=\frac{\sqrt{10}}{1110}<\frac1{300}.
\tag{8}
\]

So recentering removes the scalar `dI` defect **exactly**, but it does not make the full boundary interface reversible.  What remains is a fixed local tilt of size `|beta|` attached to the boundary projection.

There is still a useful basis-free interpretation of the diagonal blocks.  If `L_N^0=L_N` is the zero-boundary generator and `L_N^1` is the generator with the old right boundary fixed to one, then

\[
L_N^1-L_N^0=BP_N.
\]

Therefore

\[
L_N+c_0P_N=\frac{g_0}{B}L_N^0+\frac{c_0}{B}L_N^1,
\]

\[
L_N+g_0P_N=\frac{c_0}{B}L_N^0+\frac{g_0}{B}L_N^1.
\tag{9}
\]

Both are genuine Markov generators; the lower diagonal block in `(5)` is such a Markov generator minus the fixed killing `r`.

The durable gain over 010c is therefore more precise than the original wording: the scalar asymmetric `I` channel has been absorbed by recentering, and the remaining fresh-coordinate non-orthogonality is the explicit local parameter `beta`, rather than an unspecified depth-growing defect.

## 3. Complementary decomposition of the terminal high-pass

The 010e terminal operator is

\[
R_N=(dI-gL_N)(rI-L_N)^{-1}.
\]

Using `m_0=d/r` and `g_0=g-m_0`, put

\[
K_N:=r(rI-L_N)^{-1}.
\]

Then `K_N` is a Markov resolvent and

\[
\boxed{
R_N=m_0I+g_0(I-K_N).
}
\tag{10}
\]

Thus the positive-frequency zero of `R_N` at `x=|d|/g=1/100` is caused by cancellation of two distinct channels:

- the scalar low-frequency channel `m_0 I`;
- the genuine zero-frequency high-pass `g_0(I-K_N)`.

The second factor vanishes only at temporal frequency zero, not at `x=1/100`.

The same recentering appears directly in the stationary insertion functional.  If `A_N` is the left marginal of `pi_{N+1}`, then

\[
\boxed{
\pi_{N+1}(X_{N+1}f)
=g_0A_N(I-K_N)f.
}
\tag{11}
\]

Indeed 010e gives `pi_{N+1}(Y_{N+1}f)=A_NR_Nf` and `pi_{N+1}(f)=A_Nf`, so subtracting `m_0A_Nf` and using `(10)` proves `(11)`.

## 4. A uniform kernel bound for the complementary high-pass

Write, as before,

\[
h(t)=w_*(t)\sigma(t),\qquad
H_N=\int_0^\infty h(t)P_t^N\,dt.
\]

Modulo constants, `Q_N` may be replaced by `H_N` inside oscillation.  Let

\[
y(t):=r\int_0^t e^{-r(t-s)}h(s)\,ds.
\]

Then

\[
y'=r(h-y),
\]

and hence

\[
(I-K_N)H_N
=\int_0^\infty (h-y)(t)P_t^N\,dt
=\frac1r\int_0^\infty y'(t)P_t^N\,dt.
\tag{12}
\]

As in 010c, extend `h` by zero to negative times.  Convolution with the exponential probability kernel contracts total variation, and the previous product-variation argument gives

\[
\operatorname{TV}(h_{\rm ext})\le4.
\]

Therefore

\[
\|y'\|_{L^1}\le4
\]

and, uniformly in depth,

\[
\boxed{
\operatorname{osc}\!\left(g_0(I-K_N)Q_Nf\right)
\le \frac{4g_0}{r}\operatorname{osc}(f)
=\frac{999}{2750}\operatorname{osc}(f).
}
\tag{13}
\]

Numerically `999/2750=0.3632727...`.  After one ordinary `Y` insertion, whose oscillation cost is at most `B`, this channel alone has the exact contraction factor

\[
\boxed{
B\frac{999}{2750}
=\frac{998001}{2500000}
=0.3992004<1.
}
\tag{14}
\]

## 5. A rational improvement for the scalar channel

The complementary scalar channel is `m_0Q_N`.  A direct triangle estimate gives

\[
\operatorname{osc}(m_0Q_Nf)
\le |m_0|\,\|h\|_1\operatorname{osc}(f).
\tag{15}
\]

The crude bound `\|h\|_1\le Z=19100/31` is slightly too wasteful when combined with `(13)`.  It is enough to bank a simple exact improvement which uses only the first twenty units of time.

The one-particle weight has the exact two-exponential form

\[
w(t)=u_-e^{-(\omega+\rho_-)t}+u_+e^{-(\omega+\rho_+)t},
\qquad u_->0>u_+,\quad u_-+u_+=1.
\]

Since `rho_+>rho_-`,

\[
w(t)\ge e^{-(\omega+\rho_-)t}.
\tag{16}
\]

The smaller root obeys `rho_-<a`: the quadratic defining the roots is positive at `0` and equals `-a<0` at `a`.  Hence, for `0\le t\le20`,

\[
w(t)>e^{-(\omega+a)t}\ge1-(\omega+a)t\ge1-20\frac{21}{10000}=\frac{479}{500}.
\tag{17}
\]

Also `20\tau=16/25<\log2`, so `sigma<0` on `[0,20]` and

\[
1-|\sigma(t)|=2(1-e^{-\tau t}).
\]

Using the alternating Taylor lower bound

\[
e^{-x}\ge1-x+\frac{x^2}{2}-\frac{x^3}{6},\qquad 0\le x\le1,
\]

at `x=20\tau=16/25`, one obtains exactly

\[
\int_0^{20}2(1-e^{-\tau t})\,dt
\ge\frac{3776}{375}.
\]

Combining with `(17)`,

\[
\int_0^{20}w(t)(1-|\sigma(t)|)\,dt
>\frac{452176}{46875}.
\tag{18}
\]

Since `Z=\int w`, this yields the rational bound

\[
\boxed{
\|h\|_1
<\frac{19100}{31}-\frac{452176}{46875}
=\frac{881295044}{1453125}.
}
\tag{19}
\]

Consequently

\[
\boxed{
|m_0|\,\|h\|_1
<\frac{660971283}{1210937500}
=0.54583434\ldots .
}
\tag{20}
\]

If the two channels in `(10)` are bounded separately before recombination, `(13)` and `(20)` give

\[
B\left(
\frac{999}{2750}
+\frac{660971283}{1210937500}
\right)
<
\boxed{
\frac{12097480772637}{12109375000000}
<1.
}
\tag{21}
\]

Thus even the **channelwise** triangle estimate, retaining no cancellation between `m_0Q_N` and `g_0(I-K_N)Q_N`, is strictly sandwiched-contractive after one insertion.

## 6. What `(21)` does and does not give

Equation `(21)` is not an iteration theorem.  It controls the two complementary outputs of `R_NQ_N` from the raw oscillation of the input.  To iterate it one would still need a depth-uniform frame/reverse estimate recovering the relevant raw connected input from these two channel observables, or a direct two-step argument showing that a vector which is nearly invisible to one channel is forced into the other after the next fresh insertion.

The gain over 010f is structural:

1. the problematic positive-frequency zero of `R_N` has been removed by the exact split `(10)`;
2. the genuine high-pass channel alone has a large contraction margin `(14)`;
3. the remaining low-frequency channel is multiplied by the explicit small scalar `m_0` and satisfies `(20)`;
4. recentering removes the scalar `I` defect from the newest-coordinate block, while the remaining non-orthogonality is the explicit local tilt `beta=-sqrt(10)/1110` in `(6)`--`(8)`.

Therefore the next bounded target is now a **two-channel observability/two-step estimate** for the actual connected orbit in the recentered `X` block.  A failure of such an estimate would have to survive both the complementary high-pass split and the small explicit projection tilt; it cannot be attributed merely to the positive-frequency zero of `R_N`.
