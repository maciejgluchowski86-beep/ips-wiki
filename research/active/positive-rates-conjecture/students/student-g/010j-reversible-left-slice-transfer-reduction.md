# Student G 010j checkpoint: reversible left-slice transfer reduces to one killed channel

**Status:** intermediate durable checkpoint for Assignment 010.  This is an exact all-depth reduction for the frozen-weight reversible reference operator from 010d/010i.  It does not yet prove the actual `P_*` connected tail.  Its role is to identify the only reference channel which still needs a uniform estimate and to give that channel an exact two-component recursion.

## 1. Product-centered left slice at `P_0`

Work at

\[
P_0=(a_0,b,c_0)
=\left(\frac1{10000},\frac1{10},\frac{999}{1000}\right),
\]

with product reversible law

\[
\mu_0={\rm Bernoulli}(10/11)^{\otimes N}.
\]

Retain

\[
B=\frac{10989}{10000},\qquad
c_0=\frac{999}{1000},\qquad
g_0=\frac{999}{10000},
\qquad s_0:=\sqrt{c_0g_0},
\]

and define the product-centered normalized coordinate

\[
X_i=B\eta_i-c_0,
\qquad
\phi_i:=\frac{X_i}{s_0}.
\]

Then

\[
\mu_0(\phi_i)=0,
\qquad
\mu_0(\phi_i^2)=1.
\]

Slice a function on sites `1,...,N` at the **leftmost** coordinate:

\[
\boxed{f=u+\phi_1v,}
\tag{1}
\]

where `u,v` are functions of the suffix `2,...,N`.  Because the dynamics is one-sided, all updates in the suffix are independent of `eta_1`.

At `P_0` the update at site `1` is a constrained refresh from the same Bernoulli `10/11` law, with total refresh rate

\[
V_1(\eta_2)
=\omega+B\mathbf1_{\{\eta_2=0\}}
=\begin{cases}
1+b,&\eta_2=0,\\
\omega,&\eta_2=1,
\end{cases}
\qquad
\omega=\frac{11}{10000}.
\tag{2}
\]

Hence the site-1 generator kills the centered coordinate exactly:

\[
L_{0,1}(\phi_1v)=-V_1\phi_1v.
\]

After shifting the suffix to sites `1,...,N-1`, put

\[
\boxed{G_n:=L_{0,n}-V_1.}
\tag{3}
\]

Then `(1)` gives the exact orthogonal direct-sum recursion

\[
\boxed{
L_{0,N}
=L_{0,N-1}\oplus G_{N-1}
}
\tag{4}
\]

in `L^2(mu_0)`.  There is no forcing between the two blocks.  This is the function-space counterpart of the zero forcing `d/(1+b)=0` in the left-slice equation of 010b.

## 2. The fixed filtered connected operator respects the same direct sum

Keep the actual Assignment-010 duration kernel

\[
h(t)=w_*(t)\sigma(t)
\]

frozen as in 010d and define

\[
\widetilde H_{0,N}^\sigma
=\int_0^\infty h(t)e^{tL_{0,N}}\,dt,
\qquad
\widetilde Q_{0,N}^\sigma
=\widetilde H_{0,N}^\sigma-z_\sigma\Pi_{0,N}.
\]

Functional calculus applied to `(4)` gives

\[
\widetilde H_{0,N}^\sigma
=
\widetilde H_{0,N-1}^\sigma
\oplus H^\sigma(G_{N-1}),
\tag{5}
\]

where

\[
H^\sigma(G_n):=\int_0^\infty h(t)e^{tG_n}\,dt.
\]

Since `mu_0(phi_1)=0`, the invariant projection vanishes identically on the second block.  Therefore

\[
\boxed{
\widetilde Q_{0,N}^\sigma
=
\widetilde Q_{0,N-1}^\sigma
\oplus H^\sigma(G_{N-1}).
}
\tag{6}
\]

Let `J_N` be the **actual** insertion from Assignment 010,

\[
J_Nf=Y_Nf=(X_N+m_0)f,
\qquad m_0=-\frac9{10000}.
\]

For `N>=2`, this acts entirely inside the suffix and therefore preserves the decomposition `(1)`.  Define the frozen-reference connected transfer

\[
T_{0,N}:=\widetilde Q_{0,N}^\sigma J_N.
\]

Then `(6)` yields the exact recursion

\[
\boxed{
T_{0,N}
=T_{0,N-1}\oplus S_{N-1},
}
\tag{7}
\]

where the only new block is

\[
\boxed{
S_n:=H^\sigma(G_n)J_n.
}
\tag{8}
\]

All norms here are the natural product `L^2(mu_0)` norms on the corresponding suffixes.  Hence

\[
\boxed{
\|T_{0,N}\|_{2\to2}
=
\max\{\|T_{0,N-1}\|_{2\to2},\|S_{N-1}\|_{2\to2}\}.
}
\tag{9}
\]

Iterating,

\[
\boxed{
\sup_N\|T_{0,N}\|_{2\to2}<1
\quad\Longleftrightarrow\quad
\max\left\{\|T_{0,1}\|,\sup_{n\ge1}\|S_n\|\right\}<1.
}
\tag{10}
\]

Thus the growing mode space at the reversible reference has been eliminated exactly from the norm question: every increase in depth adds only the single killed block `(8)`.

## 3. Exact two-component recursion for the killed generator

The remaining family `G_n` itself has a closed left-slice recursion.  In the normalized binary basis `{1,phi_1}`, multiplication by `V_1` from `(2)` has the exact matrix

\[
\boxed{
M_{V_1}
=
\begin{pmatrix}
 g_0+\omega & -s_0\\
 -s_0 & c_0+\omega
\end{pmatrix}.
}
\tag{11}
\]

Indeed the upper-left entry is `mu_0(V_1)=g_0+omega`, the off-diagonal entry is `mu_0(V_1 phi_1)=-s_0`, and the lower-right entry follows from the binary identity for `phi_1^2`.

Combining `(4)` and `(11)`, for `n>=2`,

\[
\boxed{
G_n
=
\begin{pmatrix}
L_{0,n-1}-(g_0+\omega)I & s_0I\\
 s_0I & G_{n-1}-(c_0+\omega)I
\end{pmatrix}.
}
\tag{12}
\]

This matrix is self-adjoint in the product Hilbert space.  The coupling is the fixed scalar `s_0 I`; all depth dependence is confined to the previous `L` and `G` blocks.

The base case is the one-site killed operator

\[
G_1=L_{0,1}-V_1,
\]

with the zero right boundary inserted in `V_1` as usual.

## 4. Consequence for Assignment 010

The reference problem is now sharply localized.  A proof of

\[
\boxed{
\sup_{n\ge1}\|H^\sigma(G_n)J_n\|_{2\to2}\le q_0<1
}
\tag{13}
\]

would immediately give a depth-uniform contraction of the complete frozen-reference transfer through `(7)`--`(10)`.  Equation `(12)` gives a genuine two-channel self-adjoint recursion on which such a bound may be attacked by scalar functional calculus or a Schur-complement/energy argument.  No finite-dimensional mode closure is posited.

This does not yet settle `P_*`: even after `(13)`, one must transport the reference contraction through the actual local nonreversible defect `L_*-L_0`.  But it removes one ambiguity from 010i.  The reference transfer does not require a generic high-dimensional norm theorem; it is equivalent to the single killed family `(8)`.
