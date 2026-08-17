# Student G 010c checkpoint: exact last-coordinate block recursion and fast singleton channel

**Status:** intermediate durable checkpoint for Assignment 010. This does **not** yet prove the connected-tail target `(T)`.

The purpose of this checkpoint is to expose the algebra behind a possible bounded-step connected estimate.  In the Bernoulli-`p_*` orthogonal basis from 010b, adjoining one new rightmost coordinate gives an exact `2 x 2` operator recursion.  A potentially troublesome scalar created by the invariant-centering subtraction is then seen to enter the next step through an exact fast eigenmode, not through a slow zero-frequency mode.

## 1. Last-coordinate decomposition

Fix volume `{1,...,N+1}`.  Let

\[
P_NY_A={\bf1}_{\{N\in A\}}Y_A
\]

be the orthogonal projection, in the `Y`-monomial basis on the first `N` sites, onto monomials containing the old right boundary `N`.

Every function on `N+1` sites has a unique decomposition

\[
f=u+Y_{N+1}v,
\tag{1}
\]

with `u,v` functions of the first `N` coordinates.  Comparing the old zero-boundary action at site `N` with the new interior action gives exactly

\[
\boxed{
L_{N+1}u
=(L_N+cP_N)u+Y_{N+1}P_Nu.
}
\tag{2}
\]

For the second block, the same monomial calculation gives

\[
\boxed{
L_{N+1}(Y_{N+1}v)
=
(dI+gcP_N)v
+Y_{N+1}
\bigl(L_N-(1+b)I+gP_N\bigr)v.
}
\tag{3}
\]

Thus, in the unnormalised pair `(u,v)`,

\[
\boxed{
L_{N+1}
=
\begin{pmatrix}
L_N+cP_N & dI+gcP_N\\
P_N & L_N-(1+b)I+gP_N
\end{pmatrix}.
}
\tag{4}
\]

No finite-volume approximation is involved.

## 2. Orthogonal normalization

Under the product measure

\[
\mu_*={\rm Bernoulli}(p_*)^{\otimes N},
\qquad
p_*={c\over B},
\]

010b showed that the `Y_A` are orthogonal and

\[
\|Y_i\|_{L^2(\mu_*)}^2=cg.
\]

Put

\[
\phi_i={Y_i\over\sqrt{cg}},
\qquad
s:=\sqrt{cg},
\qquad
\delta:={d\over\sqrt{cg}}.
\]

Writing instead

\[
f=u+\phi_{N+1}v,
\]

identifies the product Hilbert space on `N+1` sites isometrically with two copies of the `N`-site Hilbert space.  In this orthogonal splitting `(4)` becomes

\[
\boxed{
L_{N+1}
=
\begin{pmatrix}
L_N+cP_N & \delta I+sP_N\\
sP_N & L_N-(1+b)I+gP_N
\end{pmatrix}.
}
\tag{5}
\]

The `P_N` couplings are symmetric.  The **only** asymmetric off-diagonal piece is the scalar soft term

\[
\delta I={d\over\sqrt{cg}}I.
\tag{6}
\]

At `P_*`,

\[
s=\sqrt{\frac{989901}{10000000}},
\qquad
\delta=-\frac{99/100000}{s},
\]

so `|delta|` is about `3.15 x 10^{-3}`.  This recursively localizes the non-reversible part more sharply than the raw growing-mode description.

## 3. The boundary singleton is an exact fast eigenmode

The newest site is autonomous under the zero right boundary.  From 010a,

\[
L_NY_N=d-(1+b)Y_N.
\]

Its invariant mean is therefore

\[
m_0:=\pi_N(Y_N)={d\over1+b}=-\frac9{10000},
\tag{7}
\]

independently of `N`.  Hence

\[
\boxed{
\psi_N:=Y_N-m_0
}
\]

satisfies the exact all-volume eigenfunction identity

\[
\boxed{
L_N\psi_N=-(1+b)\psi_N.
}
\tag{8}
\]

For the fixed filter, define the scalar spectral multiplier

\[
q(x)
:=
Z_{\omega+x}-2Z_{\omega+\tau+x},
\tag{9}
\]

where

\[
Z_\alpha
={\alpha+1+B+a\over(\alpha+a)(\alpha+1+B)-a}.
\]

Since `H_N^sigma 1=z_sigma 1`, functional calculus and `(8)` give

\[
H_N^\sigma Y_N
=z_\sigma m_0\,1+q(1+b)\psi_N.
\]

Subtracting the invariant projection therefore yields

\[
\boxed{
Q_N^\sigma Y_N
=q(1+b)(Y_N-m_0).
}
\tag{10}
\]

At `P_*`, exact rational arithmetic gives

\[
\boxed{
q(1+b)
=-\frac{5240305525}{6117276447}
\approx-0.8566402991.
}
\tag{11}
\]

Thus the singleton channel is uniformly separated from the zero-frequency multiplier `z_sigma`.

## 4. Why `(10)` matters for a two-step connected estimate

For any input `f`,

\[
Q_N^\sigma f
\]

has zero `\pi_N`-mean, but its expansion in the product-orthogonal `Y` basis can contain a constant coefficient.  The next connected insertion multiplies that constant by `Y_{N+1}`, producing precisely the newest-site singleton.

Equation `(10)` shows that this scalar part does **not** feed an uncontrolled slow centered mode at the next resolvent.  It is sent through the fixed multiplier `q(1+b)` before any further geometry is created.

This supplies a concrete algebraic explanation for why a bounded-step connected norm can succeed even though the one-step positive coefficient norm of 010a fails: one step may transfer mass into the scalar coordinate used to enforce `\pi_NQ_N=0`, but after the next insertion that coordinate lies in a fixed fast spectral channel.

The remaining theorem is to control the genuinely nonconstant block in `(5)` uniformly enough that this fast singleton channel closes a two- or bounded-step contraction for the actual connected orbit.
