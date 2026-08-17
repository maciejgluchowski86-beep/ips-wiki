# Student G 010b checkpoint: left-slice triangularization and the killed connected channel

**Status:** intermediate durable checkpoint for Assignment 010. This does **not** prove the connected-tail estimate `(T)`.

The purpose of this checkpoint is to isolate an exact infinite-depth operator which is strictly smaller than the full growing mode hierarchy and in which the invariant separator has disappeared. This is the object that remains to be bounded.

## 1. Recursive moment coordinates

Work at a fixed positive-rate point and put

\[
k=1-c,
\qquad
B=1+b-a-k,
\qquad
\omega=a+k,
\qquad
r_0=\frac1{1+b},
\qquad
d=bk-a.
\]

For a signed row measure `nu` on sites `1,...,N`, slice at the **leftmost** spin:

\[
\nu_0(f)=\nu(1_{\{\eta_1=0\}}f),
\qquad
\nu_1(f)=\nu(1_{\{\eta_1=1\}}f),
\]

where `f` is a function of the suffix `2,...,N`. Define the suffix marginal and centered left-slice profile

\[
A:=\nu_0+\nu_1,
\qquad
C:=\nu_1-r_0A.
\tag{1}
\]

Thus

\[
\nu_0=(1-r_0)A-C,
\qquad
\nu_1=r_0A+C.
\tag{2}
\]

Iterating `(1)` down the chain gives exactly the tensor moment coordinates associated with

\[
\xi_i:=\eta_i-r_0.
\]

In particular, for `theta>0`,

\[
\|\nu\|_{\theta,N}
:=\sum_{E\subseteq\{1,\ldots,N\}}
\theta^{|E|}\,|\nu(\xi_E)|
\tag{3}
\]

has the recursive identity

\[
\boxed{
\|\nu\|_{\theta,N}
=\|A\|_{\theta,N-1}
+\theta\|C\|_{\theta,N-1}.
}
\tag{4}
\]

No finite-dimensional closure is being asserted; `(4)` is just a recursive norm on the full `2^N`-dimensional signed-measure space.

## 2. Exact left-slice evolution

Let `L_{N-1}` denote the ordinary zero-right-boundary generator on the suffix, after shifting sites `2,...,N` to `1,...,N-1`. The suffix is autonomous because the dynamics is one-sided: site `1` does not affect any site to its right.

For the leftmost spin, conditional on the first suffix spin `y`, the flip rates are

\[
p_0=1,\quad q_0=b,
\qquad
p_1=k,\quad q_1=a,
\]

for `0->1` and `1->0`, respectively. Hence the slice measures solve

\[
\dot\nu_0
=\nu_0L_{N-1}-\nu_0p+\nu_1q,
\qquad
\dot\nu_1
=\nu_1L_{N-1}+\nu_0p-\nu_1q,
\tag{5}
\]

where `p,q` act by multiplication by the corresponding functions of the first suffix spin.

Adding the equations gives the exact autonomous marginal equation

\[
\boxed{
\dot A=A L_{N-1}.
}
\tag{6}
\]

For `C=nu_1-r_0A`, direct substitution gives

\[
\boxed{
\dot C
=C\bigl(L_{N-1}-V_1\bigr)
+\frac{d}{1+b}\,A\,1_{\{\eta_1=1\}},
}
\tag{7}
\]

where

\[
\boxed{
V_1(\eta)
=\omega+B\,1_{\{\eta_1=0\}}
=
\begin{cases}
1+b,&\eta_1=0,\\
\omega,&\eta_1=1.
\end{cases}
}
\tag{8}
\]

Indeed, the forcing coefficient is

\[
(1-r_0)k-r_0a
=\frac{bk-a}{1+b}
=\frac d{1+b}.
\]

At the primary point `P_*`,

\[
\frac d{1+b}
=-\frac9{10000}.
\tag{9}
\]

Thus the only forcing from the autonomous marginal channel into the centered left-slice channel is exactly the same small non-product coefficient already visible in the canonical `Y` generator.

Writing

\[
G_n:=L_n-V_1,
\tag{10}
\]

the Duhamel form of `(7)` is

\[
\boxed{
C_t
=C_0e^{tG_{N-1}}
+\frac d{1+b}
\int_0^t A_0P_s^{N-1}
1_{\{\eta_1=1\}}
 e^{(t-s)G_{N-1}}\,ds.
}
\tag{11}
\]

The semigroup `e^{tG_n}` is a genuine positive Feynman--Kac semigroup. For a positive initial measure its total mass is the path expectation of

\[
\exp\left(-\int_0^t
[\omega+B1_{\{\eta_1(s)=0\}}]ds\right).
\tag{12}
\]

In particular, the homogeneous `C` channel has no stationary component at all.

## 3. Exact triangularization of the connected transfer

Let

\[
T_N:=Q_N^\sigma\mathcal J_N
\]

in the row-measure convention: first apply `Q_N^sigma`, then multiply by `Y_N=B eta_N-c` and delete the rightmost site. Since `J_N` acts only at the right edge, it respects the left-slice decomposition.

In the recursive moment coordinates `(A,C)`, `T_N` therefore has the exact block form

\[
\boxed{
T_N=
\begin{pmatrix}
T_{N-1}&R_N\\
0&S_N
\end{pmatrix}.
}
\tag{13}
\]

Here the lower-left zero is exact: a pure centered left-slice input has `A=0`, and by `(6)` its suffix marginal remains zero for all times. The top-left block is exactly the shifted `(N-1)`-site connected transfer by suffix autonomy and projective consistency.

The new lower-right block is explicit. For a pure `C` input, the total mass is zero, so the invariant-projection term in `Q_N^sigma` vanishes identically. Therefore

\[
\boxed{
S_N
=
\left[
\int_0^\infty
w(u)\sigma(u)e^{uG_{N-1}}\,du
\right]\mathcal J_{N-1}.
}
\tag{14}
\]

After shifting indices, `(14)` is a signed resolvent of the killed suffix process `(10)` followed by the ordinary right insertion/drop.

This is the main durable reduction of the checkpoint.

## 4. Why `(14)` is genuinely different from the stopped zero-frequency tail

The old F013/F014 obstruction arose because an unsplit/recombined transfer retained a nonzero multiple of a spatial shift defect of the invariant law in its **zero temporal-frequency projection**.

That mechanism is absent from `(14)` for an algebraic reason, not a heuristic one:

1. a pure `C` input has total mass zero;
2. hence `Pi_N` is annihilated before any estimate is made;
3. the remaining semigroup is `e^{uG}`, whose potential satisfies `V_1>=omega>0` pointwise;
4. consequently this channel has no invariant eigenvector and no zero-frequency stationary projection to identify with a tail shift.

Thus an all-depth bound on `S_N` would be a genuinely positive-frequency theorem. Conversely, if this channel fails to admit a sufficiently strong depth-uniform bound, that failure cannot be attributed merely to the old invariant tail-shift term.

## 5. What remains

Equation `(13)` says that enlarging the volume adds only one new channel. The old channel is literally `T_{N-1}`; all new difficulty is carried by the forcing block `R_N` from `(11)` and the killed block `S_N` from `(14)`.

A successful continuation can therefore be substantially narrower than a norm on the full growing mode hierarchy. It is enough to prove a recursive estimate in which

- `S_N` is uniformly contractive in a depth-independent norm, and
- the forcing `R_N`, whose coefficient is exactly `d/(1+b)`, is absorbed by the slack of the previous level (or is shown to be a coboundary in the invariant quotient).

The crude total-variation estimate obtained only from `V_1>=omega` is far too weak at `P_*`; the occupation-dependent killing `B1_{\{eta_1=0\}}` and the signed filter must be used. This is now a specific Feynman--Kac problem, not the already-refuted finite mode closure.
