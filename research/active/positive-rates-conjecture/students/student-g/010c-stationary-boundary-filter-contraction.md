# Student G 010c checkpoint: stationary boundary identity and an all-depth filtered contraction

**Status:** durable positive checkpoint for Assignment 010. The theorem below is all-depth and uses the fixed filter, but it does **not yet** iterate through the full nonstationary connected orbit, so `(T)` is not yet proved.

This checkpoint gives an exact elimination of the stationary right-boundary covariance and a dimension-free contraction constant for the resulting filtered boundary channel.

## 1. Exact stationary boundary identity

Fix `N>=2`. Let `pi_N` be the invariant law of the `N`-site zero-right-boundary chain and let

\[
A_N:=\bar\pi_N
\]

be its left marginal on sites `1,...,N-1`. Put

\[
r_0=\frac1{1+b},
\qquad
q_0=1-r_0=\frac b{1+b},
\qquad
\xi_N=\eta_N-r_0,
\qquad
\lambda=1+b.
\]

Write `L=L_{N-1}` for the `(N-1)`-site zero-boundary generator. For a left function `f`, define

\[
C_N(f):=\pi_N(\xi_N f).
\]

The rightmost spin is autonomous, with

\[
L_N\xi_N=-\lambda\xi_N.
\tag{1}
\]

For a left function `f`, write

\[
L_Nf=Lf+\eta_NDf,
\tag{2}
\]

where `D=L^1-L^0` is the difference between the two generators obtained by freezing the right boundary of site `N-1` to `1` and `0`.

Stationarity of `f` gives

\[
A_N(Lf)+r_0A_N(Df)+C_N(Df)=0.
\tag{3}
\]

Using `(1)` and stationarity of `xi_N f`,

\[
0
=C_N(Lf)+\pi_N(\xi_N\eta_NDf)-\lambda C_N(f).
\]

Since

\[
\xi_N\eta_N=q_0\eta_N,
\]

and `(3)` gives

\[
\pi_N(\eta_NDf)
=r_0A_N(Df)+C_N(Df)
=-A_N(Lf),
\]

we obtain

\[
\boxed{
\lambda C_N(f)
=C_N(Lf)-q_0A_N(Lf).
}
\tag{4}
\]

Equivalently,

\[
\boxed{
C_N
=-q_0A_N L(\lambda I-L)^{-1}.
}
\tag{5}
\]

This identity is exact for every finite depth. It uses neither reversibility nor any spatial mixing statement.

## 2. Stationary insertion is a scalar functional calculus

Recall

\[
Y_N=B\eta_N-c
=m_0+B\xi_N,
\qquad
m_0=Br_0-c.
\]

Combining this with `(5)`, for every left function `f`,

\[
\boxed{
\pi_N(Y_Nf)=A_N\Phi(L)f,
}
\tag{6}
\]

where

\[
\boxed{
\Phi(L)
=m_0I-Bq_0L(\lambda I-L)^{-1}.
}
\tag{7}
\]

Since

\[
Bq_0=g-m_0,
\qquad g=b-a,
\]

this can also be written

\[
\boxed{
\Phi(L)
=gI-(g-m_0)\lambda(\lambda I-L)^{-1}.
}
\tag{8}
\]

Thus, on a mode with `L`-eigenvalue `-gamma`, the scalar multiplier is

\[
\phi(\gamma)
=m_0+(g-m_0)\frac{\gamma}{\lambda+\gamma}.
\tag{9}
\]

At `P_*`,

\[
m_0=-\frac9{10000},
\qquad
g=\frac{99}{1000},
\qquad
\lambda=\frac{11}{10}.
\]

In particular the stationary insertion damps the exact zero mode by `|m_0|`, while its high-frequency limit is only `g`.

## 3. Compose with the fixed dual-renewal filter

Let

\[
k(u):=w(u)\sigma(u),
\qquad
H_N^\sigma=\int_0^\infty k(u)P_u^N\,du.
\]

Because `Phi(L)` is a function of the same generator, it commutes with `H^sigma`. Put

\[
K_\lambda f
:=\lambda\int_0^\infty e^{-\lambda s}P_s f\,ds.
\]

`K_lambda` is a Markov operator. By `(8)`,

\[
\Phi(L)H^\sigma
=gH^\sigma-(g-m_0)K_\lambda H^\sigma.
\]

Therefore

\[
\boxed{
\Phi(L)H^\sigma
=\int_0^\infty \kappa(t)P_t\,dt,
}
\tag{10}
\]

with scalar kernel

\[
\boxed{
\kappa(t)
=gk(t)
-(g-m_0)\lambda
\int_0^t e^{-\lambda(t-s)}k(s)\,ds.
}
\tag{11}
\]

Define

\[
y(t)
:=\lambda\int_0^t e^{-\lambda(t-s)}k(s)\,ds.
\tag{12}
\]

Then `y'=lambda(k-y)`, so

\[
\boxed{
\kappa(t)=m_0y(t)+\frac g\lambda y'(t).
}
\tag{13}
\]

This form exposes the cancellation created by the fixed filter without making any spectral-normality assumption on `L`.

## 4. A rigorous all-depth operator bound at `P_*`

Extend `k` by zero to negative times. The convolution kernel

\[
\lambda e^{-\lambda t}1_{\{t\ge0\}}
\]

is a probability density, hence convolution contracts both `L^1` norm and total variation. Therefore

\[
\|y\|_{L^1}\le\|k\|_{L^1},
\qquad
\operatorname{TV}(y)\le\operatorname{TV}(k_{\rm ext}).
\tag{14}
\]

Now `w` is positive and decreasing from `1` to `0`: `s_1` is a survival probability and `w=e^{-\omega t}s_1(t)`. Also

\[
\sigma(t)=1-2e^{-\tau t}
\]

is increasing from `-1` to `1`. Hence

\[
\operatorname{TV}_{[0,\infty)}(w)=1,
\qquad
\operatorname{TV}_{[0,\infty)}(\sigma)=2,
\]

and the product variation bound gives

\[
\operatorname{TV}_{[0,\infty)}(k)
\le
\|\sigma\|_\infty\operatorname{TV}(w)
+\|w\|_\infty\operatorname{TV}(\sigma)
\le3.
\]

The extension by zero has one additional jump of magnitude `|k(0)|=1`, so

\[
\boxed{
\operatorname{TV}(k_{\rm ext})\le4.
}
\tag{15}
\]

Also `|sigma|<=1`, so

\[
\|k\|_{L^1}\le\int_0^\infty w(t)dt=Z.
\tag{16}
\]

Combining `(13)`--`(16)`,

\[
\boxed{
\|\kappa\|_{L^1}
\le |m_0|Z+\frac{4g}{1+b}.
}
\tag{17}
\]

At `P_*`, the exact survival resolvent gives

\[
Z=\frac{19100}{31}.
\]

Thus

\[
|m_0|Z+\frac{4g}{1+b}
=
\frac9{10000}\frac{19100}{31}
+4\frac{99/1000}{11/10}
=
\boxed{\frac{567}{620}}
<1.
\tag{18}
\]

Since every Markov semigroup is a contraction on `L^infty`, `(10)` and `(18)` imply the **dimension-free filtered boundary contraction**

\[
\boxed{
\|\Phi(L_N)H_N^\sigma f\|_\infty
\le\frac{567}{620}\|f\|_\infty
\qquad\text{for every }N\ge1.
}
\tag{19}
\]

By duality, the same constant bounds the total-variation norm of the corresponding signed-measure operator.

No spectral gap, no finite-dimensional mode closure, and no tail-shift estimate enters `(19)`.

## 5. Direct implication for one stationary connected block

Because `Q_N^sigma` kills constants, for arbitrary `f`

\[
Q_N^\sigma f
=H_N^\sigma(f-\pi_N(f)).
\]

Combining this with `(6)` and `(19)` gives

\[
\boxed{
\left|
\pi_{N+1}\!\left(
Y_{N+1}Q_N^\sigma f
\right)
\right|
\le
\frac{567}{620}
\|f-\pi_N(f)\|_\infty.
}
\tag{20}
\]

This is the first rigorous all-depth contraction obtained in Assignment 010 for the **fixed** filter.

## 6. Remaining issue

The connected coefficient `c_k^sigma` contains one stationary boundary insertion at its outer end, so `(20)` controls that end uniformly. But after the first connected transfer the profile is a nonstationary signed measure/function. Reapplying `(20)` would require proving that the same stationary-extension structure is preserved, which has **not** been established.

Thus `(19)` is not yet `(T)`. The remaining question is sharply localized:

> can the nonstationary connected profile be decomposed into the stationary boundary channel `(19)` plus a transient channel which is itself uniformly contractive, without reintroducing the old zero-frequency spatial tail?

Checkpoint 010b gives an independent left-slice triangularization of precisely that transient channel as a killed Feynman--Kac resolvent. The next step is to combine the two exact decompositions rather than search for a new generic finite mode closure.
