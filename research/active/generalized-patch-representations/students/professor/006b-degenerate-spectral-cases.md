# 006b: exact degenerate spectral cases

Date: 2026-08-17

This note executes Part C of Assignment 006. No irreducibility assumption is used.

## 1. Why zero eigenvalues are semisimple

Assignment 005 proved the exact intertwining

\[
R K^T=Q R,
\]

where `R` is invertible and `Q` is the physical three-state Markov generator with every neighbour frozen in the reference state. Thus `K^T` and `Q` are similar.

For every `t>=0`, `exp(tQ)` is a stochastic matrix, hence bounded. Therefore `Q`, and hence `K`, cannot have a nontrivial Jordan block at eigenvalue zero: such a block would produce polynomial growth in `exp(tQ)`.

This remains true for reducible chains. Irreducibility is not needed anywhere below.

## 2. One active eigenvalue equal to zero

Suppose the active `2 x 2` block has eigenvalues `0,-nu` with `nu>0`. The full spectrum of `K` is then `0,0,-nu`, and zero is semisimple by Section 1.

The minimal polynomial divides

\[
x(x+\nu),
\]

so

\[
e^{tK}=P_0+e^{-\nu t}P_\nu,
\]

with

\[
P_0=\frac{K+\nu I}{\nu},
\qquad
P_\nu=-\frac K\nu.
\]

Every remaining `OI` numerator has the one-mode form

\[
N(t)=L+A e^{-\nu t}.
\tag{2.1}
\]

Its derivative has fixed sign. Hence

\[
N(t)\ge0\ \forall t\ge0
\quad\Longleftrightarrow\quad
N(0)\ge0\ \text{and}\ L\ge0.
\tag{2.2}
\]

If both active eigenvalues are zero, the boundedness argument makes `K` diagonalizable with only eigenvalue zero, hence `K=0`; all numerators are constant.

## 3. Repeated nonzero active eigenvalue: diagonalizable

Suppose the active block has repeated eigenvalue `-mu<0` and is diagonalizable. A diagonalizable `2 x 2` matrix with only one eigenvalue is `-mu I`. The full matrix `K` therefore has minimal polynomial dividing

\[
x(x+\mu).
\]

Again every numerator is one-mode:

\[
N(t)=L+A e^{-\mu t},
\]

and endpoint nonnegativity is necessary and sufficient.

This includes reducible cases with two decoupled active modes having the same decay rate.

## 4. Repeated nonzero active eigenvalue: Jordan case

Now suppose the active block is non-diagonalizable with repeated eigenvalue `-mu<0`. Its nilpotent part has square zero. Since zero remains a distinct semisimple eigenvalue, the full minimal polynomial divides

\[
x(x+\mu)^2.
\]

Thus for every row/terminal pair

\[
\boxed{
N(t)=L+(A+Bt)e^{-\mu t}.}
\tag{4.1}
\]

The coefficients can be obtained without a Jordan basis. The zero spectral projector is

\[
P_0=\frac{(K+\mu I)^2}{\mu^2}.
\tag{4.2}
\]

Hence

\[
L=uP_0f,
\qquad
A=N(0)-L=uf-L,
\tag{4.3}
\]

and from

\[
N'(0)=B-\mu A=uKf
\]

we obtain

\[
\boxed{B=uKf+\mu A.}
\tag{4.4}
\]

Differentiate (4.1):

\[
N'(t)=e^{-\mu t}\bigl[B-\mu A-\mu Bt\bigr].
\tag{4.5}
\]

The bracket is affine. Therefore there is at most one positive critical point.

If `B>=0`, any positive critical point is a maximum, because at a critical point

\[
N''(t_*)=-\mu B e^{-\mu t_*}\le0.
\]

If `B<0`, a positive critical point is a minimum exactly when

\[
B-\mu A<0,
\tag{4.6}
\]

which says that the derivative starts negative and the affine bracket, whose slope is `-mu B>0`, crosses zero at positive time. Then

\[
\boxed{
t_*=\frac{B-\mu A}{\mu B}>0.}
\tag{4.7}
\]

At the critical point, (4.5) gives

\[
A+Bt_*=\frac B\mu,
\]

so

\[
\boxed{
N(t_*)
=L+\frac B\mu
\exp\left(-\frac{B-\mu A}{B}\right).}
\tag{4.8}
\]

Consequently the Jordan-case condition `N(t)>=0` for all `t>=0` is exactly:

1. `N(0)=L+A>=0`;
2. `L>=0`;
3. if `B<0` and `B-mu A<0`, also the single critical-value inequality (4.8) `>=0`.

No other time needs to be checked.

## 5. Reducible reference-neighbour chains

Reducibility does not create a new time-dependence class. The possibilities are exhausted by the spectrum of the active `2 x 2` block:

- two distinct negative eigenvalues: generic two-mode case of `006a`;
- one zero and one negative eigenvalue: Section 2;
- repeated negative diagonalizable: Section 3;
- repeated negative Jordan: Section 4;
- two zero active eigenvalues: constant case.

The long-time projector `P_0` may have rank greater than one in a reducible chain, so the limit `L=uP_0f` can depend on the starting active type. This changes the coefficient `L` but not the finite critical-point classification.

## 6. Structural reason no further degeneracy occurs

For a Metzler active block

\[
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad b,c\ge0,
\]

the discriminant is

\[
(a-d)^2+4bc\ge0.
\]

Thus complex conjugate active eigenvalues cannot occur. A repeated eigenvalue requires

\[
a=d,\qquad bc=0,
\]

so the only repeated case is either `M=-mu I` or a one-sided triangular Jordan block. Hence Sections 3--4 are exhaustive even before using the Markov similarity.
