# Student G 009a checkpoint: canonical `J` recursion and normalization

**Status:** intermediate durable checkpoint for Assignment 009. This file does **not** decide `(J-SPEC)`.

## 1. Exact reverse transfer

Work on a zero-right-boundary interval

\[
\Lambda_N=\{1,\ldots,N\}.
\]

Let `P_u^N` be its Markov semigroup and `pi_N` its invariant law. Put

\[
B=b+c-a,\qquad g=b-a,\qquad p_*=\frac cB,
\qquad \omega=1-c+a,
\]

and

\[
Y(z):=Bz-c.
\]

The normalized centered character satisfies the exact identity

\[
\boxed{Y(\eta_N)=g h_{p_*}(\eta_N).}
\tag{1}
\]

For a signed row measure `nu` on `Lambda_N`, define the insertion/drop map

\[
(\mathcal J_N\nu)(f)
:=\nu\bigl(Y(\eta_N)f\bigr),
\qquad f=f(\eta_1,\ldots,\eta_{N-1}),
\tag{2}
\]

and the duration-resolved reverse transfer

\[
\mathcal T_N(u)\nu
:=\mathcal J_N(\nu P_u^N).
\tag{3}
\]

This is the measure-side centered transfer already isolated in F009/F010. Iterating it gives the canonical singleton invariant integrand. Namely, with a harmless choice of reverse ordering for the duration labels, define

\[
S_n(u_1,\ldots,u_n)
:=
\pi_n P_{u_1}^n\mathcal J_n
P_{u_2}^{n-1}\mathcal J_{n-1}\cdots
P_{u_n}^{1}\mathcal J_1.
\tag{4}
\]

The right side is a scalar. Since every `mathcal J_k` is exactly multiplication by `g h_{p_*}` followed by deletion of the current rightmost site, induction in the number of insertions gives

\[
\boxed{
S_n(u)=g^n\pi_n(F_u),
}
\tag{5}
\]

where `F_u` is the canonical depth-`n` left centered-transfer function in the predecessor-trail reduction. In particular the first duration is inessential because

\[
\pi_nP_{u_1}^n=\pi_n,
\tag{6}
\]

but its `w`-integral remains as the corresponding scalar factor in the canonical duration integral.

Equation (5) is the exact recursion that any lower-sector or embedded positive-operator certificate for G009 must respect. It is not a finite-depth fit.

## 2. Raw transfer norm versus `J_n` and the principal's `N_n`

Put

\[
w(u)=e^{-\omega u}s_1(u)
\]

as in the current proof spine and define the raw reverse-transfer norm

\[
R_n
:=
\int_{(0,\infty)^n}
\left(\prod_{j=1}^n w(u_j)\right)
|S_n(u)|\,du.
\tag{7}
\]

The canonical singleton quantity is

\[
J_n
=B g^{n-1}
\int
\left(\prod_jw(u_j)\right)
|\pi_n(F_u)|\,du.
\]

Using (5),

\[
\boxed{
J_n=\frac Bg R_n.
}
\tag{8}
\]

Assignment 009 fixes the principal normalization by

\[
\boxed{
J_n=\frac gB N_n.
}
\tag{9}
\]

Combining (8) and (9) gives

\[
\boxed{
N_n=\left(\frac Bg\right)^2R_n.
}
\tag{10}
\]

All factors relating `R_n`, `J_n`, and `N_n` are independent of depth. Hence

\[
\boxed{
\limsup_{n\to\infty}R_n^{1/n}
=
\limsup_{n\to\infty}J_n^{1/n}
=
\limsup_{n\to\infty}N_n^{1/n}.
}
\tag{11}
\]

This independently confirms the normalization relayed after the two lost sessions: for the principal's `N_n`, the permissible relation is `J_n=(g/B)N_n`. A proof of supercriticality may therefore work with the cleaner raw transfer `R_n`, provided the final statement is translated back by (8)--(10).

## 3. Exact depth-one calibration at the primary point

At

\[
(a,b,c)=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right)
\tag{P*}
\]

one has

\[
B=\frac{10989}{10000},\qquad
 g=\frac{99}{1000},\qquad
\frac Bg=\frac{111}{10},\qquad
\omega=\frac{11}{10000}.
\]

The one-site zero-boundary stationary one-density is

\[
r_0=\frac1{1+b}=\frac{10}{11},
\]

so the first inserted signed mass is

\[
m_0:=Br_0-c=-\frac9{10000}.
\tag{12}
\]

Using the accepted right-survival resolvent

\[
Z_\alpha
=
\frac{\alpha+1+B+a}
{(\alpha+a)(\alpha+1+B)-a},
\qquad
Z=Z_\omega,
\]

gives

\[
Z=\frac{19100}{31}.
\]

Therefore

\[
R_1=Z|m_0|=\frac{1719}{3100},
\]

\[
J_1=\frac BgR_1=\frac{190809}{31000},
\]

and

\[
N_1=\left(\frac Bg\right)^2R_1
=\frac{21179799}{310000}.
\]

These numbers are only an exact normalization check. Their size has no bearing on `(J-SPEC)`, which is an asymptotic question.

## 4. Consequence for the route-decision block

The load-bearing object is now unambiguous: seek a repeatable lower sector for the exact sequence of maps

\[
\nu\mapsto\mathcal J_N(\nu P_u^N)
\]

with the absolute value applied only after all depth-`n` transfers at fixed duration vector, followed by integration against `prod w(u_j)du_j`. A finite-depth scalar growth fit which is not invariant under this recursion cannot establish `rho_J>1`.
