# Student G 010h checkpoint: recentered boundary block and the harmless scalar branch

**Status:** intermediate durable checkpoint for Assignment 010.  This isolates the last-coordinate nonreversibility more sharply; it does not by itself close the all-depth connected tail.

## 1. Recenter the newest coordinate at its autonomous boundary law

Keep

\[
\varepsilon=\frac9{10000},
\qquad
c_0=c-\varepsilon=\frac{999}{1000},
\qquad
g_0=g+\varepsilon=\frac{999}{10000},
\]

and define

\[
X_i:=B\eta_i-c_0=Y_i+\varepsilon.
\tag{1}
\]

The zero-boundary rightmost spin is the autonomous two-state chain

\[
0\to1\text{ at rate }1,
\qquad
1\to0\text{ at rate }b,
\]

whose invariant density is `1/(1+b)=10/11`.  Since `c_0=B/(1+b)`,

\[
E[X_N]=0
\]

for this autonomous boundary law.

The actual insertion is exactly

\[
\boxed{Y_N=X_N-\varepsilon.}
\tag{2}
\]

## 2. Exact symmetric last-coordinate block

Let `P_N` be the canonical coefficient projection onto monomials containing the old right boundary site `N`.  Starting from the `Y` block of 010c and substituting `Y_{N+1}=X_{N+1}-epsilon`, one obtains, for functions `u,v` on the first `N` sites,

\[
\boxed{
L_{N+1}u
=(L_N+c_0P_N)u+X_{N+1}P_Nu,
}
\tag{3}
\]

and

\[
\boxed{
L_{N+1}(X_{N+1}v)
=g_0c_0P_Nv
+X_{N+1}(L_N-rI+g_0P_N)v,
\qquad r=1+b.
}
\tag{4}
\]

The scalar term cancels because

\[
d+\varepsilon r=0,
\]

and the remaining coefficient is

\[
g(c-\varepsilon)+\varepsilon(c-\varepsilon)=g_0c_0.
\]

Thus in the unnormalised decomposition `f=u+X_{N+1}v`,

\[
\boxed{
L_{N+1}
=
\begin{pmatrix}
L_N+c_0P_N & g_0c_0P_N\\
P_N & L_N-rI+g_0P_N
\end{pmatrix}.
}
\tag{5}
\]

Normalize

\[
\phi_{N+1}=\frac{X_{N+1}}{s_0},
\qquad
s_0:=\sqrt{c_0g_0}.
\]

Then `(5)` becomes

\[
\boxed{
L_{N+1}
=
\begin{pmatrix}
L_N+c_0P_N & s_0P_N\\
s_0P_N & L_N-rI+g_0P_N
\end{pmatrix}.
}
\tag{6}
\]

The coupling to the newly appended coordinate is therefore symmetric.  All nonreversibility is inherited through the old block `L_N`; there is no additional asymmetric scalar defect at the newest interface.

## 3. The scalar insertion branch is strictly contractive

Let

\[
h(t):=w_*(t)\sigma(t).
\]

Since

\[
|\sigma(t)|=|1-2e^{-\tau t}|
\le1+2e^{-\tau t},
\]

\[
\int_0^\infty |h(t)|dt
\le Z_\omega+2Z_{\omega+\tau}.
\tag{7}
\]

For the actual rational data,

\[
Z_\omega=\frac{19100}{31},
\qquad
Z_{\omega+\tau}=\frac{197500}{6639}.
\]

Hence

\[
\boxed{
\varepsilon\int_0^\infty |h(t)|dt
\le
\varepsilon\left(Z_\omega+2Z_{\omega+\tau}\right)
=
\frac{4171497}{6860300}
<0.609<1.
}
\tag{8}
\]

Because subtraction of the invariant projection changes a function only by a constant,

\[
\operatorname{osc}(Q_Nf)
=\operatorname{osc}(H_Nf)
\le
\left(\int|h|\right)\operatorname{osc}(f).
\tag{9}
\]

Combining `(2)`, `(8)`, and `(9)`, the scalar branch `-epsilon f` of one insertion costs at most

\[
\frac{4171497}{6860300}<1
\]

in oscillation, uniformly in depth.

Thus the difficult part of the connected transfer is not the affine recentering defect.  It is the boundary-containing `X` branch in `(3)`--`(6)`, i.e. transmission through the old-boundary projection `P_N` before the newest centered boundary mode is refreshed.
