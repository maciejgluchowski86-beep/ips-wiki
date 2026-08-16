# Student F 014: light-cone screening of the recombined defect

## Verdict

Assignment 014 asks whether the recombined two-insertion defect

\[
E_{N,u}(f)
=\kappa_{N,u}(f)-a(u)\pi_{N-2}(f)
\]

has a depth-uniform short-time light-cone bound, so that the existing trail weight kills the remaining late times.

The fixed-suffix part of this mechanism **does work**. Every centered observable of the autonomous rightmost two-site suffix has an explicit exponential separated-gap covariance bound, obtained from the neighbor-independent resets and finite propagation. The same estimate extends uniformly to the fixed two-site observable which appears after cutting the first boundary edge at positive time.

However, the actual recombined defect contains another term already at `u=0` which finite propagation cannot remove. Put

\[
H_N:=Y_NY_{N-1},
\qquad
h_*:=\pi_2(H_2)=a(0),
\]

and let

\[
\delta_N^{(2)}:=\bar{\bar\pi}_N-\pi_{N-2}
\]

be the difference between the double-left marginal of `pi_N` and the `(N-2)`-site zero-boundary invariant law. Then exactly

\[
\boxed{
E_{N,0}(f)
=\pi_N[(H_N-h_*)f]
+h_*\,\delta_N^{(2)}(f).
}
\tag{0.1}
\]

The first term is exponentially localized. The second is a genuine zero-frequency spatial boundary law. Define

\[
\Delta_M^{(2)}
:=
\sup_{N\ge M+2}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}f\subseteq\{1,\ldots,N-M-2\}}}
|\delta_N^{(2)}(f)|.
\tag{0.2}
\]

If `S_M` is the same remote norm of `E_{N,0}`, then for

\[
\gamma_*
:=
\min\left\{\frac\omega8,\ \log4-\frac34\right\}>0
\]

I prove

\[
\boxed{
\left|
S_M-|h_*|\Delta_M^{(2)}
\right|
\le
12c^2 e^{-\gamma_*M}.
}
\tag{0.3}
\]

On the projective half-line law `mu=pi_infty^0`,

\[
\boxed{
\Delta_M^{(2)}
=\|\theta^2\mu-\mu\|_{\mathcal F_M},
\qquad
\mathcal F_M=\sigma(X_j:j\ge M).
}
\tag{0.4}
\]

Hence

\[
\lim_{M\to\infty}\Delta_M^{(2)}
=
\|\theta^2\mu-\mu\|_{\mathcal T},
\qquad
\mathcal T=\bigcap_M\mathcal F_M.
\tag{0.5}
\]

Thus, whenever `h_*!=0`, the required static estimate `(L7)` is equivalent, up to the explicit exponentially localized fixed-suffix error, to exponential **two-step tail-shift localization**. At the standard strict residual point

\[
(a,b,c)=\left(\frac1{10},\frac3{10},\frac45\right),
\]

one has

\[
\boxed{h_*=-\frac{34}{8775}\ne0.}
\tag{0.6}
\]

So the required first subproblem does not follow from fixed-suffix positive-frequency localization plus finite propagation.

The same obstruction survives the positive-time no-crossing decomposition. Let

\[
Q_u=P_u^{N-2,0},
\qquad \lambda=1+b,
\]

and define

\[
G_u
:=
Y_N\left[m_0+B e^{-\lambda u}(\eta_{N-1}-r_0)\right].
\tag{0.7}
\]

Then `pi_N(G_u)=a(u)`. For every `1<=d<=M`, every remote `f` with `||f||_infty<=1`, there is a bounded function `q=q_{N,M,u,f}^{(d)}` supported at distance at least `M-d` from the right two-site suffix such that

\[
\boxed{
\begin{aligned}
\left|
E_{N,u}(f)-a(u)\delta_N^{(2)}(q)
\right|
\le{}&
12c^2e^{-\gamma_*(M-d)}\\
&+8c^2\,P(\operatorname{Pois}(u)\ge d)\\
&+2c^2\,P(\operatorname{Pois}(u)\ge M+1).
\end{aligned}
}
\tag{0.8}
\]

This is the exact light-cone normal form. Choosing `d=floor(M/2)` and `u<=M/8` makes the entire remainder exponentially small in `M`. The only nonlocal term left before the light cone reaches the test is

\[
a(u)\delta_N^{(2)}(q).
\]

It is **initial spatial boundary memory**, not influence propagated across the gap during the duration `u`.

Consequently the requested pointwise estimates `(L4)`--`(L5)` are, at every parameter with `h_*!=0`, at least as strong as exponential two-step tail-shift localization; conversely exponential decay of `Delta_M^(2)` combined with `(0.8)` gives the requested short-time bound. At the rational point `(0.6)`, the two statements are equivalent up to constants.

For the integrated quantity there is a useful conditional statement. Using `d=floor(M/2)`, `u<=M/8`, the Poisson large-deviation bound in `(0.8)`, and Meeting 020's late-time estimate gives constants `C,gamma>0` such that

\[
\boxed{
\Gamma_M
\le
c^2 Z\,\Delta_{\lceil M/2\rceil}^{(2)}
+C e^{-\gamma M}.
}
\tag{0.9}
\]

Therefore

\[
\Delta_M^{(2)}\to0
\quad\Longrightarrow\quad
\Gamma_M\to0,
\tag{0.10}
\]

and exponential two-step tail-shift localization implies exponential `Gamma_M` localization. But `(0.4)`--`(0.5)` show that this missing input is itself a zero-frequency spatial tail theorem. It is not supplied by the fixed-suffix resets or by finite propagation.

I therefore do **not** prove or refute `Gamma_M->0`. I do refute the proposed light-cone screening mechanism as an independent replacement for the zero-frequency theorem: after the fixed-suffix and causal-crossing pieces are fully controlled, the no-crossing block still retains `delta_N^(2)`.

On the already known product surface `a=b(1-c)`, `J_N pi_N=0`, so `Gamma_M=0` identically; there is no obstruction there.

Exact finite algebra and the rational calibration are checked in

`students/student-f/014-light-cone-screening-verifier.py`.

## 1. Setup

Work at a fixed strict residual parameter point. Put

\[
B=b+c-a,
\qquad
g=b-a,
\qquad
\omega=1-c+a,
\qquad
r_0=\frac1{1+b},
\]

\[
Y_j=B\eta_j-c,
\qquad
m_0=Br_0-c.
\]

Since `Y_j` takes the two values `-c` and `g`, and `g<c` in the residual chamber,

\[
|Y_j|\le c.
\tag{1.1}
\]

The zero-boundary flip rates have the exact graphical decomposition

- reset to `1` at rate `1-c`;
- reset to `0` at rate `a`;
- when the right neighbour is zero, refresh at rate `B` to Bernoulli `c/B`.

The first two marks are neighbour-independent and occur at total rate

\[
\omega=a+1-c>0.
\tag{1.2}
\]

I use only these independent reset marks in the fixed-suffix mixing argument.

## 2. Uniform mixing of the autonomous two-site suffix

Let `S_t^{(2)}` be the semigroup of the rightmost two-site zero-boundary chain. Couple two copies from arbitrary initial states by the common graphical construction.

The rightmost site becomes permanently coupled at its first neighbour-independent reset. After that time, the next neighbour-independent reset of the left suffix site couples that site permanently as well. Therefore the full two-site coupling time is stochastically dominated by the sum of two independent `Exp(omega)` variables. Hence

\[
P(\tau_{\rm coup}>t)
\le e^{-\omega t}(1+\omega t).
\tag{2.1}
\]

If `h` is a function of the two-site suffix with

\[
\pi_2(h)=0,
\]

coupling one chain to a stationary copy gives

\[
\boxed{
\|S_t^{(2)}h\|_\infty
\le
2\|h\|_\infty e^{-\omega t}(1+\omega t).
}
\tag{2.2}
\]

Using

\[
(1+x)e^{-x}\le2e^{-x/2},
\qquad x\ge0,
\]

this also gives

\[
\|S_t^{(2)}h\|_\infty
\le4\|h\|_\infty e^{-\omega t/2}.
\tag{2.3}
\]

This is a fixed two-site statement and uses no depth-uniform mixing of the full chain.

## 3. Centered fixed-suffix covariance localizes exponentially

### Proposition 3.1

Let `h` be a centered function of `(eta_{N-1},eta_N)` and let `f` be supported on

\[
\{1,\ldots,N-M-2\},
\qquad M\ge1.
\]

Then

\[
\boxed{
|\pi_N(hf)|
\le
6\|h\|_\infty\|f\|_\infty e^{-\gamma_*M},
}
\tag{3.1}
\]

where

\[
\gamma_*
=
\min\left\{\frac\omega8,\log4-\frac34\right\}.
\]

### Proof

Run the full `N`-site chain in stationarity for a time `T`. The rightmost two sites form the autonomous suffix process `Z_t`.

Construct a modified left evolution using the same initial configuration and the same graphical marks at sites `1,...,N-2`, but freeze the boundary input at site `N-1` at its time-zero value. Let `\widehat f_T` be the value of `f` under this modified evolution.

Conditional on the initial configuration, `\widehat f_T` uses no future suffix marks, while `h(Z_T)` uses only suffix marks. Thus

\[
E[h(Z_T)\widehat f_T\mid\eta_0]
=(S_T^{(2)}h)(Z_0)
E[\widehat f_T\mid\eta_0].
\]

Therefore, by `(2.2)`,

\[
|E[h(Z_T)\widehat f_T]|
\le
2\|h\|_\infty\|f\|_\infty
 e^{-\omega T}(1+\omega T).
\tag{3.2}
\]

For the true and modified left evolutions to disagree on the support of `f`, influence from the boundary site `N-1` must cross the ordered sites

\[
N-2,N-3,\ldots,N-M-2.
\]

There are `M+1` required rate-one clock rings in the correct order. Hence

\[
P(f(\eta_T)\ne\widehat f_T)
\le
P(\operatorname{Pois}(T)\ge M+1).
\tag{3.3}
\]

Stationarity gives

\[
\pi_N(hf)=E[h(Z_T)f(\eta_T)].
\]

Combining `(3.2)`--`(3.3)`,

\[
|\pi_N(hf)|
\le
2\|h\|_\infty\|f\|_\infty
\left[
 e^{-\omega T}(1+\omega T)
+P(\operatorname{Pois}(T)\ge M+1)
\right].
\tag{3.4}
\]

Take `T=M/4`. Then

\[
e^{-\omega M/4}(1+\omega M/4)
\le2e^{-\omega M/8},
\]

and the standard Poisson Chernoff bound gives

\[
P(\operatorname{Pois}(M/4)\ge M+1)
\le
P(\operatorname{Pois}(M/4)\ge M)
\le
\exp\left[-M\left(\log4-\frac34\right)\right].
\]

This proves `(3.1)`. `square`

This proposition confirms the positive part suggested in Meeting 020: a centered fixed two-site suffix observable really is exponentially local.

## 4. The static recombined defect contains a second term

Put

\[
H_N=Y_NY_{N-1},
\qquad
h_*=\pi_2(H_2).
\]

Suffix projectivity gives

\[
\pi_N(H_N)=h_*
\]

for all `N>=2`. Also, for a function on sites `1,...,N-2`,

\[
\pi_N(f)=\bar{\bar\pi}_N(f).
\]

Therefore

\[
\begin{aligned}
E_{N,0}(f)
&=\pi_N(H_Nf)-h_*\pi_{N-2}(f)\\
&=\pi_N[(H_N-h_*)f]
+h_*(\bar{\bar\pi}_N-\pi_{N-2})(f).
\end{aligned}
\]

This proves `(0.1)`.

Since `|H_N|<=c^2` and `|h_*|<=c^2`,

\[
\|H_N-h_*\|_\infty\le2c^2.
\]

Applying Proposition 3.1 gives

\[
\left|
E_{N,0}(f)-h_*\delta_N^{(2)}(f)
\right|
\le12c^2e^{-\gamma_*M}\|f\|_\infty.
\tag{4.1}
\]

Taking remote operator norms proves `(0.3)`.

At the rational residual point `(1/10,3/10,4/5)`, the exact two-site invariant calculation gives

\[
h_*=a(0)=-\frac{34}{8775}.
\tag{4.2}
\]

Thus the second term is genuinely present at a strict residual point.

## 5. Exact interpretation as a two-step tail-shift defect

Let `mu=pi_infty^0` be the projective half-line law in coordinates

\[
X_0,X_1,X_2,\ldots
\]

from the fixed boundary outward, and let

\[
\theta(x_0,x_1,x_2,\ldots)=(x_1,x_2,x_3,\ldots).
\]

For `N=M+L+2`, the leftmost `L` sites under `\bar{\bar\pi}_N` correspond, after reversing order, to

\[
X_{M+2},\ldots,X_{M+L+1},
\]

whereas the same labelled sites under `\pi_{N-2}` correspond to

\[
X_M,\ldots,X_{M+L-1}.
\]

Taking the supremum over all finite lengths `L` gives

\[
\Delta_M^{(2)}
=\|\theta^2\mu-\mu\|_{\mathcal F_M}.
\]

Exactly as in F011, reverse-martingale convergence then gives `(0.5)`.

This is weaker than one-step tail-shift agreement in the sense that one-step agreement implies two-step agreement. The converse is not automatic because a period-two spatial phase is not excluded by measure theory alone. I do not assume such an exclusion here.

## 6. Positive-time cut decomposition

The static obstruction is not an isolated `u=0` algebraic accident. The natural no-crossing decomposition retains the same double-left boundary law.

Let

\[
Q_u=P_u^{N-2,0}
\]

be the zero-boundary semigroup on sites `1,...,N-2`, and let `S_u` be the autonomous one-site zero-boundary semigroup on site `N-1`. Cut the dependence of site `N-2` on site `N-1`; the resulting semigroup on `1,...,N-1` is

\[
\widehat P_u=Q_u\otimes S_u.
\]

The one-site identity is

\[
S_uY_{N-1}
=m_0+B e^{-(1+b)u}(\eta_{N-1}-r_0).
\tag{6.1}
\]

Hence, with `G_u` from `(0.7)`,

\[
\widehat\kappa_{N,u}(f)
:=\pi_N[Y_N\widehat P_u(Y_{N-1}f)]
=\pi_N[G_uQ_uf].
\tag{6.2}
\]

Since the rightmost site of the `(N-1)`-site chain is autonomous, cutting its influence to the left does not change the scalar mass:

\[
\pi_N(G_u)=a(u).
\tag{6.3}
\]

Therefore

\[
\boxed{
\widehat E_{N,u}(f)
=
\pi_N[(G_u-a(u))Q_uf]
+a(u)\delta_N^{(2)}(Q_uf).
}
\tag{6.4}
\]

The first term is a centered fixed two-site suffix covariance. The second is the same double-left zero-frequency law, evolved only by the decoupled left semigroup.

## 7. Quantitative light-cone normal form

The true and cut semigroups differ on the support of `f` only if influence crosses from site `N-1` through `M+1` ordered leftward sites. Since `|Y_j|<=c`,

\[
|E_{N,u}(f)-\widehat E_{N,u}(f)|
\le
2c^2P(\operatorname{Pois}(u)\ge M+1).
\tag{7.1}
\]

Now use the accepted F010 finite-speed truncation on `Q_uf`. For every `1<=d<=M`, choose `q=q^{(d)}_{N,M,u,f}` with

\[
\|q\|_\infty\le1,
\qquad
\operatorname{supp}q
\subseteq\{1,\ldots,N-M-2+d\},
\]

such that

\[
\|Q_uf-q\|_\infty
\le2P(\operatorname{Pois}(u)\ge d).
\tag{7.2}
\]

Because `S_u` is Markov and `|Y|<=c`,

\[
|G_u|\le c^2,
\qquad
|a(u)|\le c^2,
\qquad
\|G_u-a(u)\|_\infty\le2c^2.
\tag{7.3}
\]

Apply Proposition 3.1 to the centered suffix function `G_u-a(u)` and the truncated test `q`, whose remaining gap is `M-d`. Then

\[
|\pi_N[(G_u-a(u))Q_uf]|
\le
12c^2e^{-\gamma_*(M-d)}
+4c^2P(\operatorname{Pois}(u)\ge d).
\tag{7.4}
\]

Also, since `delta_N^(2)` is a difference of probability measures,

\[
|a(u)\delta_N^{(2)}(Q_uf-q)|
\le
4c^2P(\operatorname{Pois}(u)\ge d).
\tag{7.5}
\]

Combining `(6.4)` and `(7.1)`--`(7.5)` proves `(0.8)`.

Take `d=floor(M/2)` and restrict to `0<=u<=M/8`. Standard Poisson large deviations then give constants `C_1,gamma_1>0`, depending only on the fixed rates, such that

\[
\boxed{
\left|
E_{N,u}(f)-a(u)\delta_N^{(2)}(q)
\right|
\le C_1e^{-\gamma_1M}.
}
\tag{7.6}
\]

Thus the no-crossing graphical argument succeeds exactly up to the term it cannot affect: the double-left initial boundary law.

## 8. Consequences for `(L4)`, `(L5)`, and `Gamma_M`

At `u=0`, `(0.3)` shows that if `h_*!=0`, either `(L4)` or `(L5)` implies exponential decay of `Delta_M^(2)`.

Conversely, if

\[
\Delta_M^{(2)}\le C_0e^{-\eta M},
\]

then `(0.8)` with `d=floor(M/2)` proves `(L4)` for `0<=u<=M/8` after adjusting constants. Hence, at the rational point `(0.6)`, the requested pointwise light-cone estimate is equivalent, up to fixed constants, to exponential two-step tail-shift localization.

More generally, without assuming a rate, `(0.8)` gives for `0<=u<=M/8`

\[
\|E_{N,u}\|_{\mathrm{remote},M}
\le
c^2\Delta_{\lceil M/2\rceil}^{(2)}
+C_1e^{-\gamma_1M}.
\tag{8.1}
\]

Integrating this over the short-time interval uses only

\[
\int_0^{M/8}w(u)du\le Z.
\]

For `u>=M/8`, Meeting 020 gives

\[
\int_{M/8}^\infty
w(u)\|E_{N,u}\|_{\mathrm{remote},M}du
\le
\frac{2c^2}{\omega}e^{-\omega M/8}.
\]

Combining the two gives `(0.9)` after changing `C,gamma`.

Therefore the light-cone calculation has completely separated the two issues:

1. **causal propagation and centered fixed-suffix memory:** exponentially controlled;
2. **pre-existing two-step spatial boundary phase:** exactly `Delta_M^(2)` and not controlled by finite propagation.

The second item is a zero-frequency tail theorem. Proving it by generic observability or mixing is outside the authorized mechanism and would return to the type of global theorem Meeting 020 explicitly declined to request.

## 9. Scope

This report does not prove that `Delta_M^(2)` fails to vanish, and therefore does not prove that `Gamma_M` fails to vanish. It proves instead that the proposed light-cone mechanism cannot decide `Gamma_M` without an additional two-step tail-shift theorem: the unresolved law is already present before the light cone starts propagating.

The actual fixed-suffix and finite-speed parts are not the blocker; they are proved here with explicit exponential bounds.

According to the stopping rule in Assignment 014, this leaves no sharper authorized predecessor-trail/profile mechanism inside the present implementation.

## Handoff

`unresolved after substantive work; exact screening blocker: centered observables of the fixed two-site suffix do localize exponentially, and the positive-time no-crossing comparison has the explicit normal form E_{N,u}(f)=a(u) delta_N^(2)(q)+O(exp(-gamma M)) for u<=M/8, with q still separated by order M from the suffix. Here delta_N^(2)=barbar pi_N-pi_{N-2}, and its remote norm is exactly Delta_M^(2)=||theta^2 pi_infty^0-pi_infty^0||_{F_M}. At u=0 the remote norm of E differs from |pi_2(Y_2Y_1)| Delta_M^(2) by at most 12c^2 exp(-gamma_* M); at the strict rational point pi_2(Y_2Y_1)=-34/8775. Thus the requested light-cone estimate is equivalent there to exponential two-step tail-shift localization, while the light-cone remainder itself is already exponentially controlled. Moreover Gamma_M <= c^2 Z Delta_{ceil(M/2)}^(2)+C exp(-gamma M), so two-step tail-shift agreement would suffice, but it is an additional zero-frequency spatial theorem rather than a finite-propagation consequence. Gamma_M itself is not proved or refuted.`
