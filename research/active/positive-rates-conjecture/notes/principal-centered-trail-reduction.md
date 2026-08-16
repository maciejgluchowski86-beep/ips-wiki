# Principal centered-trail exploration: durable research note

Date: 2026-08-16

Provenance: this note records the load-bearing content of a separate principal ChatGPT exploration supplied to the Professor as a rendered-page text capture. The capture warns that subscripts/superscripts may be mangled by rendering. The formulas below have been normalized to the notation currently used in the positive-rates workspace. This note is research evidence, not yet a publication-level audited theorem.

## 1. Centered dual and canonical predecessor trail

Use the normalized centered character

$$
H_p(A,\eta)=\prod_{i\in A}h_p(\eta_i),
\qquad
h_p(u)=\frac{u-p}{q},\quad q=1-p.
$$

For local coefficients `c00,c01,c10,c11`, the centered dual coefficients in the principal calculation are

$$
\delta=c_{00}-\frac pq c_{10},
$$

$$
\lambda=c_{01}-c_{00}-\frac pq(c_{11}-c_{10}),
$$

$$
\beta=c_{00}+c_{10}-c_{01}-c_{11}.
$$

When these are nonnegative, the FK coefficient is

$$
v=\delta+\lambda+\beta-c_{00}-c_{10}=-\frac{c_{11}}q.
$$

For a finite interval `R=[ell,r]` and finite initial dual set `A subset R`, define `tau_R(t)` using every successful birth/jump mark whose source is active, including refresh coin zero. On `{tau_R(t)>0}`, start at the final relevant interaction leaving `R` and recursively choose the last relevant predecessor entering the current trail site. This gives a unique root `x in A`, spatial trail

$$
x_k=x+k,
\qquad
n=n_x=r-x+1,
$$

and times

$$
0=t_0<t_1<\cdots<t_n=\tau_R(t).
$$

The selected intermediate refresh coins are one; the final coin may be zero or one. The trail site is active throughout each vertical segment, so there are no death/jump marks on those segments. The resulting no-mark probability contributes `exp(-(delta+lambda)t_n)`. Combined with the FK weight on the trail, the vertical factor is

$$
\exp\{(v-\delta-\lambda)t_n\}
=
\exp\{-(c_{01}+c_{11})t_n\}.
$$

This is positive and exponentially decreasing whenever `c01+c11>0`.

## 2. Left/trail/right factorization

The canonical trail partitions spacetime into a left region, the trail, and a right region. Conditional on the decorated trail, the relevant Poisson families separate. The left dual is killed by a successful crossing into the trail that would contradict the predecessor choice; selected birth/jump types determine whether the old trail site is inserted into the left set. The right dual contains ordinary right-region marks together with the extra trail-source birth clocks and the selected refresh projections.

The pathwise active-set decomposition splits both the terminal centered monomial and the FK integral. A Poisson-Mecke disintegration then gives an exact predecessor-trail formula. In the general nonnegative-coefficient case, if `alpha_B=beta`, `alpha_J=lambda`, the nonempty-trail contribution has the form

$$
\sum_{x\in A}\sum_{\kappa}\sum_{z=0}^1
\int_{0<t_1<\cdots<t_n\le t}
 e^{-(c_{01}+c_{11})t_n}
 q^{n-1}p^{1-z}q^z
 \Bigl(\prod_{k=1}^n\alpha_{\kappa_k}\Bigr)
 L_\gamma(\eta)U_{\gamma,z}(\eta)\,dt.
\tag{13}
$$

The count `n=r-x+1` is fixed by the root. Extra rightward interactions are part of the right region, not additional canonical trail steps.

## 3. Residual normalized family

For the unresolved normalized family the principal calculation uses

$$
c_{00}=1,
\qquad
c_{01}=1-c,
\qquad
c_{10}=b,
\qquad
c_{11}=a.
$$

Put

$$
B=b+c-a,
\qquad
p_*=\rho=\frac cB,
\qquad
q_* = \frac{b-a}{B},
\qquad
\omega=1-c+a.
$$

Then

$$
\beta=B,
\qquad
\lambda=0,
\qquad
\delta_* = \frac{b(1-c)-a}{b-a}.
$$

The selected trail interactions are births. When `delta_*<0`, the signed-death convention uses rate `|delta_*|`; the vertical no-death factor cancels the corresponding positive part of the FK potential. In either sign case the residual trail factor is

$$
e^{-\omega\tau}.
$$

Averaging the final refresh coin gives the residual formula

$$
\boxed{
E_A[W_t^\eta;\tau_R(t)>0]
=
\sum_{x\in A} B(b-a)^{n_x-1}
\int_{\Delta_{n_x}(t)}
 e^{-\omega t_{n_x}}
 L_\gamma(\eta)
 \bigl[\rho U_{\gamma,0}(\eta)+q_*U_{\gamma,1}(\eta)\bigr]\,dt.
}
\tag{13'}
$$

Thus the trail itself is sign-free even outside the original patch-positive region. Crude scalar absolute values are not useful near East because the centered insertion cancels the small refresh probability and simplex integration produces powers of `1/omega`.

## 4. Spin-system realization and the right-region bound

The left contribution is an original spin system with a moving zero boundary, with multiplication by centered characters at selected birth times. The right contribution is an original spin system with boundary killing, projections at selected times, and final coin-averaged refresh.

After averaging the final coin before taking absolute values, the right-region operators are sup-norm contractions: ordinary Markov semigroups, projections, sub-Markov killed semigroups, and multiplication by `eta_y`. Hence for fixed initial monomial `A`,

$$
\boxed{
\sup_{\gamma,t,\eta}|R_{\gamma,t}(\eta)|\le C_A,
}
\tag{R}
$$

where one may take

$$
C_A=\max\left\{1,\frac{p_*}{q_*}\right\}^{|A|}.
$$

The constant may be poor near East, but `A` is fixed and `C_A` does not grow with `R` or trail depth. No right-region mixing estimate is required.

## 5. Reduction to a left invariant expectation

Write trail gaps

$$
u_k=t_k-t_{k-1},
\qquad
\tau=|u|=\sum_{k=1}^n u_k,
\qquad
s=t-\tau.
$$

Let `m=min A`. The left contribution can be written

$$
L_{\gamma,t}=P_s^{<r+1,0}F_{x,u},
$$

where `F_{x,u}` is obtained by alternating zero-boundary semigroups and centered multiplications at the trail sites.

For fixed `R`, the zero-boundary finite chain on `[m,r]` is irreducible in the strict residual chamber. Therefore

$$
P_s^{[m,r],0}F\longrightarrow \pi^0_{m,r}(F)
$$

uniformly in the initial configuration as `s to infinity`. The mixing time may depend arbitrarily on `R` because the intended order of limits is first `t to infinity`, then `R to infinity`.

The complementary recent-exit region `s<T_R` has `tau>t-T_R`; for fixed depth `n`, the factor `e^{-omega tau}` makes its scalar mass vanish as `t to infinity` because `omega>0` at every strict positive-rate residual parameter point.

Combining finite-volume relaxation with (R) reduces the nonempty-trail term to the invariant quantity

$$
\limsup_{t\to\infty}\sup_\eta |D_R(t,\eta)|
\le
C_A\sum_{x\in A}
B(b-a)^{n_x-1}
\int_{(0,\infty)^{n_x}}
 e^{-\omega|u|}
 \left|\pi^0_{m,r}(F_{x,u})\right|\,du.
\tag{15}
$$

Hence the substantive left-region target is

$$
\boxed{
B(b-a)^{n-1}
\int_{(0,\infty)^n}
 e^{-\omega|u|}
 \left|\pi^0_{m,r}(F_{x,u})\right|\,du
\longrightarrow0
\quad(n=r-x+1\to\infty).
}
\tag{L}
$$

The full ergodicity reduction also requires the complementary no-exit part of the barrier decomposition to be checked in the reconstructed proof; the principal exploration treats that part as belonging to the existing finite-volume argument.

## 6. Exact East cancellation

For the exact East heat-bath model with facilitating zero boundary, the finite-volume invariant law is product Bernoulli. The final selected trail interaction is a birth, so the final left insertion has the form

$$
F_{x,u}=h_{p_*}(\eta_r)G_{x,u}(\eta_{<r})
$$

with the preceding factor independent of `eta_r`. Therefore

$$
\boxed{
\pi^0_{m,r}(F_{x,u})=0.
}
$$

The East equilibrium contribution is exactly zero, not merely small. The exact East point has `omega=0`, so the positive-rate recent-exit domination by `e^{-omega tau}` is absent there; East is a structural limit, not part of the strict positive-rate residual chamber.

## 7. Sufficient all-depth centered-transfer estimate

For a signed measure `nu` on sites up to `y`, define the residual centered transfer

$$
(\mathcal C_{y,u}\nu)(f)
=
\nu\bigl(h_{p_*}(\eta_y)P_u^{<y,0}f\bigr),
\qquad f=f(\eta_{<y}).
$$

Successive transfers produce the invariant integrands in (L). A sufficient all-depth estimate is the existence of norms on the generated signed-measure class and a parameter-point constant `theta<1` such that

$$
\boxed{
(b-a)\int_0^\infty e^{-\omega u}
\|\mathcal C_{y,u}\nu\|_{*,y-1}\,du
\le
\theta\|\nu\|_{*,y}
}
\tag{T}
$$

uniformly in interval and depth, together with uniform control of the starting invariant measure and final test functional. Iteration would give exponential spatial decay `O(theta^n)` in (L).

The norm cannot simply be total variation on all signed measures because multiplication by `h_{p_*}` has size `1/q_*`; it must retain centering cancellation and only needs to control the generated class.

The residual family is favorable because the centered dual jump coefficient is exactly zero. In a general centered dual a jump term would be noncentered and would need to be included in the transfer estimate.

## 8. Near-East scale check and current warning

Along

$$
a=\varepsilon^2,
\qquad
b=\varepsilon,
\qquad
c=1-\varepsilon^2,
$$

one has

$$
\omega=2\varepsilon^2,
\qquad
b-a=\varepsilon(1-\varepsilon),
\qquad
\delta_*=-\varepsilon.
$$

For the one-site zero-boundary invariant law,

$$
\pi^0_{\{r\}}(h_{p_*})=rac{\delta_*}{1+b},
$$

so the constant-mode Laplace factor is

$$
\boxed{
\frac{b-a}{\omega}
\left|\pi^0_{\{r\}}(h_{p_*})\right|
=
\frac{1-\varepsilon}{2(1+\varepsilon)}<\frac12.
}
$$

Thus the scale required by (T) is consistent with the one-site calculation despite the small `omega`.

The principal exploration reports a further running calculation: at two levels the scalar invariant integrand changes sign as the inter-trail time varies. That claim has not yet been independently reconstructed in the group record. If correct, it rules out pointwise positivity and simple scalar sign iteration, but not a signed-measure norm contraction of the form (T).

## Current interpretation

This is an all-depth route, not a revival of the closed cellwise scaffold-positivity argument. The closed route demanded a nonnegative transfer at every individual scaffold cell and failed because short hidden cells had negative sign. The present reduction first integrates the full left region to its zero-boundary invariant expectation and asks only for decay of the resulting centered signed transfer across arbitrary depth. Sign changes are allowed.
