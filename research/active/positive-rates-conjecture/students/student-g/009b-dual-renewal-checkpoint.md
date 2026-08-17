# Student G 009b checkpoint: exact dual-renewal reduction

**Status:** intermediate durable checkpoint for Assignment 009. This file does **not** decide `(J-SPEC)`.

The purpose of this checkpoint is to replace the finite-depth growth fit by an exact all-depth scalar recurrence. It also records a concrete obstruction to the most naive positive-renewal closure.

## 1. `L^1` duality produces repeatable signed witnesses

Use the raw reverse-transfer scalar `S_n` and norm `R_n` from `009a-canonical-j-recursion-checkpoint.md`:

\[
R_n
=
\int\left(\prod_{j=1}^n w(u_j)\right)|S_n(u)|\,du.
\]

Let `sigma:[0,infty)->[-1,1]` be any fixed measurable function. Since the first duration is inessential under the invariant initial law, define

\[
W_n^{\sigma}
:=
Z\int_{(0,\infty)^{n-1}}
\left(\prod_{j=2}^n w(u_j)\sigma(u_j)\right)
S_n(0,u_2,\ldots,u_n)\,du_2\cdots du_n,
\tag{1}
\]

where

\[
Z=\int_0^\infty w(u)\,du.
\]

Then pointwise `|sigma|<=1` and the triangle inequality give the rigorous lower witness

\[
\boxed{R_n\ge |W_n^{\sigma}|.}
\tag{2}
\]

Consequently any fixed `sigma` for which

\[
\limsup_n|W_n^{\sigma}|^{1/n}>1
\]

proves `rho_J>1`, because `R_n,J_n,N_n` have the same root growth by 009a.

This is an asymptotic mechanism: `sigma` is fixed once and for all and is reused at every depth.

## 2. Exact connected/separator decomposition

For the `N`-site zero-boundary chain define

\[
H_N^\sigma
:=
\int_0^\infty w(u)\sigma(u)P_u^N\,du,
\qquad
z_\sigma
:=
\int_0^\infty w(u)\sigma(u)\,du.
\tag{3}
\]

Let

\[
\Pi_N={\bf 1}\otimes\pi_N
\]

be the invariant projection and put

\[
Q_N^\sigma:=H_N^\sigma-z_\sigma\Pi_N.
\tag{4}
\]

Thus

\[
H_N^\sigma=z_\sigma\Pi_N+Q_N^\sigma,
\qquad
Q_N^\sigma{\bf1}=0,
\qquad
\pi_NQ_N^\sigma=0.
\tag{5}
\]

Write `mathcal J_N` for multiplication by `Y_N=B eta_N-c` followed by deletion of site `N`.

Define the connected block scalars

\[
c_1:=m_0:=\pi_1(Y_1),
\tag{6}
\]

and, for `k>=2`,

\[
\boxed{
 c_k^\sigma
:=
\pi_k\mathcal J_k
Q_{k-1}^\sigma\mathcal J_{k-1}
Q_{k-2}^\sigma\mathcal J_{k-2}
\cdots
Q_1^\sigma\mathcal J_1.
}
\tag{7}
\]

These are genuine depth-`k` connected coefficients; no finite-volume limit is being taken.

Let

\[
r_n^\sigma:=W_n^\sigma/Z.
\]

Expanding every internal factor

\[
H_j^\sigma=z_\sigma\Pi_j+Q_j^\sigma
\]

and using

\[
\nu\Pi_j=\nu(1)\pi_j
\]

together with projective suffix consistency yields the exact composition formula

\[
\boxed{
 r_n^\sigma
=
\sum_{\ell_1+\cdots+\ell_s=n}
 z_\sigma^{s-1}
 \prod_{i=1}^s c_{\ell_i}^\sigma.
}
\tag{8}
\]

The sum is over all ordered compositions of `n`. A factor `z_sigma Pi` is exactly a separator: it replaces the current signed profile by its total mass times the invariant law, so the portions to its two sides factor.

Set

\[
v_0:=1,
\qquad
v_n:=z_\sigma r_n^\sigma,
\qquad
 a_k:=z_\sigma c_k^\sigma.
\tag{9}
\]

Then (8) is equivalent to the exact renewal recurrence

\[
\boxed{
 v_n=\sum_{k=1}^n a_kv_{n-k},
\qquad v_0=1.
}
\tag{10}
\]

At the strong point below the observed witness has alternating sign, so it is convenient to put

\[
V_n:=(-1)^n v_n,
\qquad
\lambda_k:=(-1)^k a_k.
\tag{11}
\]

Then, with no approximation,

\[
\boxed{
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1.
}
\tag{12}
\]

Thus `(J-SPEC)` has a precise renewal formulation for every fixed dual filter `sigma`.

## 3. A rational filter with exact finite algebra

Take the primary point

\[
(a,b,c)=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right)
\tag{P*}
\]

and choose

\[
\boxed{
\sigma(u)=1-2e^{-\tau u},
\qquad
\tau=\frac4{125}.
}
\tag{13}
\]

This is admissible because `-1<=sigma(u)<=1` for all `u>=0`.

The advantage over a hard short/long threshold is exact arithmetic. Recall

\[
Z_\alpha
=
\int_0^\infty e^{-\alpha u}s_1(u)\,du
=
\frac{\alpha+1+B+a}
{(\alpha+a)(\alpha+1+B)-a}.
\tag{14}
\]

For the `N`-site generator `L_N`, functional calculus gives the exact matrix identity

\[
\mathscr H_N(\alpha)
:=
\int_0^\infty e^{-\alpha u}s_1(u)P_u^N\,du
\]

\[
\boxed{
=
\bigl[A_\alpha+(1+B+a)I\bigr]
\Bigl[(A_\alpha+aI)(A_\alpha+(1+B)I)-aI\Bigr]^{-1},
\qquad
A_\alpha:=\alpha I-L_N.
}
\tag{15}
\]

Therefore

\[
\boxed{
H_N^\sigma
=\mathscr H_N(\omega)-2\mathscr H_N(\omega+\tau),
}
\tag{16}
\]

and every finite matrix entry is rational at `(P*)`. Likewise

\[
z_\sigma=Z_\omega-2Z_{\omega+\tau}
=\frac{114559900}{205809}
\approx556.63212007249.
\tag{17}
\]

The verifier computes the connected coefficients by exact rational matrix algebra. The first seven transformed renewal coefficients are

\[
\begin{array}{c|r}
k&\lambda_k\\ \hline
1&\phantom{-}0.500968908065245\ldots\\
2&\phantom{-}0.411924883422103\ldots\\
3&\phantom{-}0.108662569072765\ldots\\
4&\phantom{-}0.023748492346787\ldots\\
5&\phantom{-}0.002014744316807\ldots\\
6&-0.000063246581641\ldots\\
7&-0.000100593312263\ldots
\end{array}
\tag{18}
\]

In particular the following are exact strict inequalities, not floating-point assertions:

\[
\boxed{
\lambda_1,\ldots,\lambda_5>0,
\qquad
\lambda_6,\lambda_7<0.
}
\tag{19}
\]

and

\[
\boxed{
\lambda_1+\lambda_2+\lambda_3
=1.021556360560113\ldots>1.
}
\tag{20}
\]

The exact rational number in (20) is checked in the verifier. Also

\[
\sum_{k=1}^5\lambda_k
=1.047319597223708\ldots,
\tag{21}
\]

and

\[
\boxed{
\sum_{k=1}^7\lambda_k
=1.047155757329804\ldots>1.
}
\tag{22}
\]

## 4. What this proves and what it refutes

The renewal recurrence (12) is an exact all-depth representation of a fixed admissible `L^1` dual witness. It is therefore a legitimate asymptotic route, unlike extrapolating ratios of `N_n`.

However, (19) gives a rigorous obstruction to the simplest desired lower sector. One cannot declare the first few connected block types to be a positive renewal system and simply discard all longer connected blocks: the exact connected coefficients cease to be positive already at lengths six and seven for the rational filter (13).

So the finite positive truncation

\[
V_n\stackrel{?}{\ge}
\lambda_1V_{n-1}+\cdots+\lambda_5V_{n-5}
\]

has **not** been proved and is not justified merely by (19)--(22).

## 5. The remaining asymptotic theorem is now a connected-tail bound

The exact recurrence gives a much narrower sufficient target. If, for example, one proves

\[
\boxed{
\sum_{k\ge8}|\lambda_k|
<
\sum_{k=1}^7\lambda_k-1,
}
\tag{23}
\]

then

\[
\sum_{k\ge1}\lambda_k>1.
\]

Absolute summability makes

\[
F(r):=\sum_{k\ge1}\lambda_kr^{-k}
\]

continuous for `r>=1`, with `F(1)>1` and `F(r)->0` as `r->infty`. Hence there is `r_*>1` with `F(r_*)=1`. The generating function of (12) is

\[
\sum_{n\ge0}V_nz^n
=
\frac1{1-\sum_{k\ge1}\lambda_kz^k},
\tag{24}
\]

so its radius of convergence is at most `1/r_*`. Therefore

\[
\limsup_n|V_n|^{1/n}\ge r_*>1.
\]

By (2), this would prove

\[
\rho_J>1.
\]

Numerically, the required margin in (23) is approximately

\[
0.0471557573.
\]

The uncommitted finite calculations beyond `k=7` suggest that the actual tail is vastly smaller than this margin, but Assignment 009 requires an all-depth theorem, so those calculations are not promoted to evidence of (23).

The exact remaining object is the connected operator

\[
\boxed{
\mathcal K_N^\sigma
:=Q_N^\sigma\mathcal J_N.
}
\tag{25}
\]

A proof of a depth-uniform geometric bound on the connected orbit generated by (25), strong enough to imply (23), would settle `(J-SPEC)` positively. F009's growing exact mode hierarchy explains why this does not reduce automatically to a fixed finite matrix. On the other hand, unlike the exhausted zero-frequency profile tail, `Q_N^\sigma` annihilates the invariant projection, so this is genuinely a positive-frequency connected-profile problem rather than a rephrasing of the old tail-shift defect.
