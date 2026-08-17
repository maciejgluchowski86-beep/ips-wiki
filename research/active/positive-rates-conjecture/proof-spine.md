# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

## E0. Current route status

There is presently **no active proof architecture**.

Student G is idle after Meeting 030; no G011. Student F is idle; no F016.

The operative architecture assessment is consultation 002 / Meeting 025: **no presently identified route clears the continuation bar**. The late G010 material materially narrows the connected-renewal blocker but does not prove the required all-depth actual-orbit estimate.

## E1. Canonical predecessor-trail `J` quantity

Put

$$
B=b+c-a,
\qquad g=b-a,
\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

For singleton depth `n`,

$$
J_n=\frac BgR_n=\frac gBN_n.
$$

Hence

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}
$$

is also the root growth rate of `R_n` and `N_n`. `(J-SPEC)` remains open.

## E2. Exact fixed-filter renewal witness

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

fix

$$
\sigma(u)=1-2e^{-(4/125)u}.
$$

For

$$
H_N^\sigma=\int w(u)\sigma(u)P_u^Ndu,
\qquad
Q_N^\sigma=H_N^\sigma-z_\sigma\Pi_N,
$$

one has

$$
Q_N^\sigma\mathbf1=0,
\qquad
\pi_NQ_N^\sigma=0.
$$

Expanding every `H=zPi+Q` gives the exact recurrence

$$
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1.
\tag{REN}
$$

The fixed signed witness is dominated by the canonical absolute-duration norm, so supercritical root growth of `V_n` proves `rho_J(P_*)>1`.

Commit `e4452de` exactly verifies the first seven rational coefficients with

$$
\sum_{k=1}^7\lambda_k>1.
$$

The sufficient connected-tail theorem

$$
\boxed{
\sum_{k\ge8}|\lambda_k|<\delta_7,
\qquad
\delta_7:=\sum_{k=1}^7\lambda_k-1>0
}
\tag{CT}
$$

remains open.

## E3. Terminal high-pass contraction

G010 derives

$$
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}.
$$

The repaired exact verifier `ce77c9c` proves a depth-independent signed kernel estimate with

$$
B\Theta_\sharp<1,
$$

hence

$$
\operatorname{osc}
\left(
R_{N+1}Q_{N+1}(Y_{N+1}f)
\right)
\le q_\sharp\operatorname{osc}(f),
\qquad q_\sharp<1.
\tag{HP}
$$

The scalar multiplier of `R_N` vanishes at `x=1/100`, blocking generic inversion of this one seminorm.

## E4. Boundary-resolvent elimination

Late checkpoint `75d0e8a` eliminates the stationary discrepancy functional from the actual connected coefficient. Thus bare one-/two-step tail-shift TV is not logically required for the fixed-filter connected route.

The residual coefficient is an explicit boundary-resolvent expectation on the actual connected orbit. Any future claim of equivalence with the old F013/F014 tail-shift problem must survive this exact elimination.

## E5. Complementary channel split

The corrected recentered boundary-channel checkpoint gives

$$
R_N=m_0I+g_0(I-K_N),
\qquad
K_N=(1+b)((1+b)I-L_N)^{-1}.
\tag{CH}
$$

Thus the `x=1/100` zero is cancellation between a small scalar channel and a genuine high-pass channel; `I-K_N` itself vanishes only at temporal frequency zero.

Both channels satisfy depth-uniform one-step bounds, and after one ordinary insertion their channelwise triangle estimate is strictly below one. This is not an iterative vector norm because no depth-uniform frame/reverse estimate controls the next raw connected input from these two outputs.

## E6. Exact recentered insertion intertwining

Put

$$
r=1+b=11/10,
\qquad
\varepsilon=9/10000,
\qquad
X_N=Y_N+\varepsilon,
\qquad
g_0=999/10000,
$$

and `A_N=-L_N`. Then

$$
\boxed{
A_NM_{X_N}
=
M_{X_N}(A_{N-1}+r)
-g_0B M_{\eta_N}P_{N-1}.
}
\tag{INT}
$$

So a fresh recentered insertion shifts frequency by `r`; the sole failure of exact intertwining is the old right-boundary projection.

After regrouping `Y=X-\varepsilon`,

$$
\boxed{
\begin{aligned}
e^{tL_N}M_{Y_N}
={}&e^{-rt}M_{X_N}e^{tL_{N-1}}
-\varepsilon I_Ne^{tL_{N-1}}\\
&+B\int_0^t e^{(t-s)L_N}M_{\eta_N}P_{N-1}
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}\,ds.
\end{aligned}
}
\tag{TRI}
$$

The first two branches are individually subcritical under safe absolute-value estimates:

$$
BZ_{\omega+r}=\frac{1065933}{1068400}<1,
\qquad
\varepsilon Z=\frac{1719}{3100}<1.
\tag{SUB}
$$

Verifier `adf50d9` checks these and the other scalar inequalities exactly.

## E7. Final G010 blocker: signed boundary transmission

Integrating the third branch of `(TRI)` against the fixed signed kernel `h(t)=w_*(t)\sigma(t)` gives

$$
\boxed{
\begin{aligned}
\mathcal V_N f
:={}&B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}\\
&\hspace{26mm}\times
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt.
\end{aligned}
}
\tag{V}
$$

For Assignment 010 the input is the actual connected orbit. Both the inner coefficient and the outer filter kernel change sign, so taking absolute values before the two integrations destroys the remaining cancellation.

No depth-uniform estimate for `\mathcal V_N` on the actual connected orbit was proved. This is now the sharpest residual object of the fixed-filter connected-renewal route.

## E8. Reversible reference Sobolev theorem

At the corrected reversible reference point

$$
P_0=(1/10000,1/10,999/1000),
$$

keep the actual `P_*` duration weight and filter frozen externally. Let `A_{0,N}=-L_{0,N}` and

$$
q(x)=Z_{\omega+x}-2Z_{\omega+\tau+x}.
$$

Verifier `56d47cb` proves

$$
|xq(x)|<1\qquad(x>0).
$$

The fresh centered insertion satisfies

$$
M_X^*A_{0,N}^{-1}M_X
\le
\frac{998001}{11000000}I,
$$

hence

$$
\|A_{0,N}^{1/2}\widetilde Q_{0,N}^\sigma(Y_Nf)\|_2
\le
\left(
\sqrt{\frac{998001}{11000000}}+\frac9{400}
\right)\|f\|_2
<\|f\|_2.
\tag{SQ}
$$

This is a genuine all-depth positive-frequency theorem for the frozen-weight reversible reference transfer, not for the actual `P_*` orbit.

## E9. Reversible left-slice reduction

Commit `c444db5` gives the exact orthogonal recursion

$$
L_{0,N}=L_{0,N-1}\oplus G_{N-1}
$$

in the product Hilbert space and therefore

$$
T_{0,N}=T_{0,N-1}\oplus S_{N-1},
\qquad
S_n=H^\sigma(G_n)J_n.
$$

Thus

$$
\sup_N\|T_{0,N}\|_{2\to2}<1
$$

reduces exactly to a uniform bound on the single killed channel family `S_n`. The killed family has a self-adjoint two-component recursion. This removes the growing reference mode space from the norm question but does not transport the result through the actual nonreversible defect.

## E10. Raw coefficient Lyapunov obstruction strengthened

Commit `d9c477e` tests the two-parameter degree/component norm

$$
\|f\|_{\theta,\phi}
=
\sum_{A\ne\varnothing}
\theta^{|A|}\phi^{\kappa(A)}|x_A|.
$$

Uniform nonexpansiveness of the actual nonconstant raw semigroup would require

$$
(c-\alpha)\frac\phi\theta\le c+\omega,
$$

$$
g\theta+\frac c\theta\le c+g+2\omega,
$$

$$
g\theta+\frac{\alpha}{\theta\phi}\le g+\omega,
\qquad \alpha=1/100.
$$

The dimer inequality forces `theta>99/100`; the long-block inequality then makes the singleton inequality impossible. Verifier `adf50d9` checks the decisive scalar inequalities exactly.

Hence multiplicative component-count weighting does not repair the 010a one-step coefficient Lyapunov route. Filter-level cancellation is load-bearing.

## E11. Stop rule / future restart

Assignment 010 is complete unresolved after substantive work. Meeting 030 issues no G011 and leaves both students idle.

A future restart of the connected-renewal branch requires **new input specifically controlling `(V)` on the actual connected orbit**, retaining its two-time cancellation strongly enough to give summable/geometric connected coefficients, or a materially different proof architecture.

Do not reactivate on generic requests to find another norm, extend the reversible comparison, optimize the filter, compute longer coefficient tables, prove bare tail shift, revisit common-coupling occupation, or search generic Bellman/joint correctors.

Consultation 002 / Meeting 025 `no-credible-route` is operative.

## E12. Other retained exact mathematics

The stationary occupation-control hierarchy, common-coupling fixed-site facts, exact trajectory-valued spatial kernel, previous predecessor-profile reductions, and G009 singular fixed-depth theorem remain correct but inactive as recorded in earlier meetings.

## Anti-circularity checkpoint

Do not infer `(CT)` from the finite renewal prefix; treat `(HP)` or the channelwise bounds as iterable without a frame/actual-orbit theorem; transfer `(SQ)` from `P_0` to `P_*` with a depth-growing perturbation norm; import the reversible point's canonical duration law; identify the connected route with bare tail shift despite the exact elimination; or treat `rho_J>1`, if later proved, as nonergodicity. It would refute only the sufficient absolute-duration route.
