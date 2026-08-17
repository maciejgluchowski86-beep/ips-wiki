# 005b: outgoing rows reduce to a three-state Markov semigroup sign problem

Date: 2026-08-17

This note executes Part C and the structural part of Part D of Assignment 005 after the Metzler reduction in `005a`.

## 1. Zero-length outgoing inequalities

Fix a nonempty-target outgoing signed row

\[
p=\mathbf a_{r,\tau}=(p_0,p_1,p_2).
\]

Boundary completeness makes both active outgoing terminal types realizable. The `OO` numerator at zero length is

\[
p f_s^O=p_s,
\qquad s\in\{1,2\}.
\]

Hence typed patch positivity forces

\[
\boxed{p_1\ge0,\qquad p_2\ge0.}
\tag{1.1}
\]

Both incoming terminal types are also realizable. The `OI` zero-length numerators are

\[
p f_1^I=p_0+p_1,
\qquad
p f_2^I=p_0+p_2,
\]

so positivity forces

\[
\boxed{p_0+p_1\ge0,\qquad p_0+p_2\ge0.}
\tag{1.2}
\]

These are all zero-length sign conditions for one outgoing row. In particular `p_0` itself may be negative.

## 2. The `OO` families become automatic

By `005a`, `e^{tK}` is entrywise nonnegative. Its zeroth row is `(1,0,0)`, because state `0` is absorbing for the local dual transfer. Thus for active terminal `s`,

\[
p e^{tK}e_s^T
=p_1(e^{tK})_{1s}+p_2(e^{tK})_{2s}.
\]

By (1.1) every factor on the right is nonnegative. Therefore

\[
\boxed{p e^{tK}f_s^O\ge0\quad\text{for all }t\ge0,\ s=1,2.}
\tag{2.1}
\]

After the boundary-complete Metzler reduction, **all `OO` inequalities are automatic from their zero-length limits**.

The only remaining families are `OI`.

## 3. Exact physical Markov interpretation of `OI`

Let

\[
Q(x,y)=q_{xy}\quad(x\ne y),
\qquad
Q(x,x)=-\sum_{y\ne x}q_{xy}
\]

be the physical one-site continuous-time Markov generator obtained by freezing every neighbour in the reference state.

For a coefficient row `p`, define its values on physical states by

\[
g_0=p_0,
\qquad
g_1=p_0+p_1,
\qquad
g_2=p_0+p_2.
\tag{3.1}
\]

Equivalently, if

\[
R=
\begin{pmatrix}
1&0&0\\
1&1&0\\
1&0&1
\end{pmatrix},
\]

then `g=R p^T`.

A direct multiplication using the physical form (1.1) of `005a` gives the exact intertwining

\[
\boxed{R K^T=Q R.}
\tag{3.2}
\]

Therefore

\[
R e^{tK^T}=e^{tQ}R.
\tag{3.3}
\]

The column `f_b^I=e_0^T+e_b^T` evaluates an indicator-basis coefficient row at physical state `b`. Hence (3.3) gives

\[
\boxed{
p e^{tK}f_b^I
=(e^{tQ}g)_b
=E_b[g(Z_t)],
\qquad b=1,2,
}
\tag{3.4}
\]

where `Z` is the physical reference-neighbour three-state chain with generator `Q`.

Thus the remaining typed positivity problem has an elementary interpretation:

> start the physical local chain from either active state and ask whether the expectation of a function `g` stays nonnegative, knowing only that `g_1,g_2>=0` while `g_0` may be negative.

If `p_0>=0`, then `g>=0` and (3.4) is automatic. The genuinely nontrivial case is

\[
p_0<0,
\qquad g_1,g_2\ge0.
\tag{3.5}
\]

## 4. Why three states are structurally different from two

Under the Metzler inequalities, the active block of `K` is

\[
A=\begin{pmatrix}-\alpha&\beta\\\gamma&-\delta\end{pmatrix},
\qquad\beta,\gamma\ge0.
\]

Its eigenvalues are

\[
\lambda_{\pm}
=-\frac{\alpha+\delta}{2}
\pm\frac12\sqrt{(\alpha-\delta)^2+4\beta\gamma},
\tag{4.1}
\]

which are real and nonpositive by `005a`. Since `K` and `Q` are similar after the indicator-basis change, the spectrum of `Q` is

\[
\{0,\lambda_+,\lambda_-\}.
\]

In the generic distinct-eigenvalue case every `OI` numerator therefore has the form

\[
\boxed{N_b(t)=L_b+A_b e^{\lambda_+t}+B_b e^{\lambda_-t}.}
\tag{4.2}
\]

When the local physical chain is irreducible, `L_b` is the stationary average `pi(g)` and is independent of `b`.

The two-state theory has only one decaying exponential, so zero-length and long-time endpoint signs control the full interval. Formula (4.2) has two decaying modes. Endpoint signs alone do not algebraically preclude cancellation between them at an interior time.

The mandatory exact gate will decide whether physical realizability and the full boundary-complete endpoint constraints nevertheless forbid such an interior dip. If an exact dip exists, Assignment 005 has pre-registered `STOP-NO-FINITE-ENDPOINT-CRITERION` rather than permission to replace the exact property by a stronger cone.
