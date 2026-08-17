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

No proof architecture is formally active. Student G is idle after Meetings 027--029; no G011. Student F is idle; no F016.

One G response was already generating before the idle ruling could be relayed. Meeting 029 instructs the principal not to destroy that in-flight response by clicking stop, but to send no further prompt after it returns. This is work-preservation, not formal reactivation.

The operative architecture assessment remains consultation 002 / Meeting 025: **no presently identified route clears the continuation bar**, unless the already-running G artifact supplies the actual-orbit theorem specified below.

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
\boxed{
J_n=\frac BgR_n=\frac gBN_n.
}
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

Define

$$
c_1=m_0,
$$

$$
c_k^\sigma
=\pi_kJ_kQ_{k-1}^\sigma J_{k-1}\cdots Q_1^\sigma J_1.
$$

Expanding every `H=zPi+Q` gives the exact recurrence

$$
\boxed{
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1.
}
\tag{REN}
$$

The fixed signed witness is dominated by the canonical absolute-duration norm, so supercritical growth of `V_n` proves `rho_J(P_*)>1`.

Commit `e4452de` exactly verifies the first seven rational coefficients with

$$
\lambda_1,\ldots,\lambda_5>0,
\qquad
\lambda_6,\lambda_7<0,
\qquad
\sum_{k=1}^7\lambda_k>1.
$$

The sufficient target

$$
\boxed{
\sum_{k\ge8}|\lambda_k|<\delta_7,
\qquad
\delta_7:=\sum_{k=1}^7\lambda_k-1>0,
}
\tag{CT}
$$

remains open.

## E3. Exact terminal high-pass contraction

G010 derives

$$
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}.
$$

For the actual fixed duration weight and filter, repaired verifier `ce77c9c` proves a depth-independent signed kernel bound with

$$
B\Theta_\sharp<1.
$$

Hence

$$
\boxed{
\operatorname{osc}
\left(
R_{N+1}Q_{N+1}(Y_{N+1}f)
\right)
\le q_\sharp\operatorname{osc}(f),
\qquad q_\sharp<1.
}
\tag{HP}
$$

The scalar multiplier

$$
R(x)=\frac{d+gx}{1+b+x}
$$

vanishes at `x=|d|/g=1/100`, blocking generic inversion of this one seminorm.

## E4. Exact boundary-resolvent elimination

Let

$$
q_N=Q_Nf_N,
\qquad
f_N=Y_NQ_{N-1}f_{N-1},
$$

and put

$$
r=1+b,
\qquad
S_N=(rI-L_N)^{-1},
\qquad
D_N=(I-L_N)S_N.
$$

Late checkpoint `75d0e8a`, accepted in Meeting 028, proves

$$
\boxed{
 c_{N+1}
 =A_N\!\left[
 \frac dr q_N
 +\left(g-\frac dr\right)B
 D_NP_NS_Nq_N
 \right].
}
\tag{BRE}
$$

At `P_*`,

$$
 c_{N+1}=A_N(\mathfrak B_Nq_N),
$$

where

$$
\mathfrak B_N
=-\varepsilon I
+g_0B(I-L_N)(rI-L_N)^{-1}
P_N(rI-L_N)^{-1}.
$$

Thus unrestricted tail-shift TV is not logically required for the connected coefficient. The residual problem is orbit-specific.

## E5. Complementary high-pass decomposition

Corrected late checkpoint `010h-recentered-boundary-channel-checkpoint.md` at `81a836c` gives

$$
\boxed{
R_N=m_0I+g_0(I-K_N),
\qquad K_N=r(rI-L_N)^{-1}.
}
\tag{CH}
$$

The `x=1/100` blind frequency is cancellation between these two channels. The genuine high-pass `I-K_N` has only the zero-frequency kernel.

For the actual fixed filter,

$$
\operatorname{osc}\bigl(g_0(I-K_N)Q_Nf\bigr)
\le\frac{999}{2750}\operatorname{osc}(f),
\tag{CH1}
$$

and

$$
\operatorname{osc}(m_0Q_Nf)
<\frac{660971283}{1210937500}\operatorname{osc}(f).
\tag{CH2}
$$

After one ordinary insertion,

$$
\boxed{
B\left(
\frac{999}{2750}
+
\frac{660971283}{1210937500}
\right)
<1.
}
\tag{CH3}
$$

This is a strict **channelwise one-step** bound, not an iterative two-component norm: no frame/reverse estimate yet converts the two outputs into control of the next raw input.

Recentring at the autonomous boundary mean removes the scalar `I` off-diagonal but does not make the old boundary projection orthogonal. In product-centered coordinates,

$$
\beta=-\frac{\sqrt{10}}{1110},
\qquad |\beta|<1/300
$$

is the explicit local non-orthogonal tilt.

## E6. Exact fresh-coordinate intertwining

With `A_N=-L_N` and the product-centered fresh coordinate `X_N`, G proves

$$
\boxed{
A_NM_{X_N}
=
M_{X_N}(A_{N-1}+r)
-g_0B M_{\eta_N}P_{N-1}.
}
\tag{INT}
$$

Thus a fresh insertion shifts temporal frequency by the fixed amount `r=11/10`; the sole failure of exact intertwining is the old-boundary transmission term. The semigroup/Duhamel version separates the raw `Y` insertion into a fresh shifted branch, a small scalar branch, and this boundary-transmission branch.

## E7. Reversible fresh-insertion Sobolev theorem

At the corrected reversible reference point

$$
P_0=(1/10000,1/10,999/1000),
$$

keep the actual `P_*` duration weight and fixed filter frozen externally. Let

$$
A_{0,N}=-L_{0,N}
$$

in `L^2(mu_0)` and

$$
q(x)=Z_{\omega+x}-2Z_{\omega+\tau+x}.
$$

Commit `56d47cb` exactly verifies

$$
\boxed{|xq(x)|<1\qquad(x>0).}
\tag{SQ1}
$$

For the fresh product-centered insertion `M_Xf=X_Nf`, the site-`N` Dirichlet contribution gives

$$
\boxed{
M_X^*A_{0,N}^{-1}M_X
\le
\frac{c_0g_0}{r}I
=
\frac{998001}{11000000}I.
}
\tag{SQ2}
$$

Therefore

$$
\boxed{
\|A_{0,N}^{1/2}\widetilde Q_{0,N}^\sigma M_Xf\|_2
\le
\sqrt{\frac{998001}{11000000}}\,\|f\|_2.
}
\tag{SQ3}
$$

For the actual insertion `Y=X+m_0`, still under the frozen-weight reversible reference transfer,

$$
\boxed{
\|A_{0,N}^{1/2}\widetilde Q_{0,N}^\sigma(Y_Nf)\|_2
\le
\left(
\sqrt{\frac{998001}{11000000}}
+
\frac9{400}
\right)\|f\|_2
<\|f\|_2.
}
\tag{SQ4}
$$

This is a genuine dimension-free positive-frequency theorem, but it is not yet a theorem on the actual `P_*` connected orbit.

## E8. Current blocker / restart rule

The live mathematical bottleneck is no longer simply “find another high-pass” or “prove tail shift.” The local ingredients are explicit:

- complementary channels `(CH)` with strict one-step margin `(CH3)`;
- fresh-coordinate frequency shift with only the explicit boundary-transmission defect `(INT)`;
- a dimension-free fresh-insertion negative-Sobolev gain and filtered `H^1` output `(SQ2)`--`(SQ4)`.

What is still missing is an **actual-orbit iteration theorem**. A qualifying restart requires either:

1. a depth-uniform two-seminorm/energy inequality propagating `(SQ4)` through the actual nonreversible defect `L_*-L_0` and the explicit boundary tilt/transmission term; or
2. an orbit-specific theorem giving summable/geometric decay of the connected coefficients.

A naive use of the reference spectral gap to return from `H^1` to `L^2` loses the margin. The current checkpoints do not yet supply the required frame/energy closure.

Meeting 029 therefore does not issue G011. The already-running G response may finish without destructive interruption; after it returns, no further prompt is sent before Professor review.

## E9. Other retained exact mathematics

The stationary occupation-control hierarchy, common-coupling facts, exact trajectory kernel, previous profile reductions, and G009 singular fixed-depth theorem remain correct but inactive as recorded in earlier meetings.

## Anti-circularity checkpoint

Do not treat `(CH3)` as an iterable vector contraction without a frame estimate; do not transfer `(SQ4)` from `P_0` to `P_*` by a depth-growing perturbation norm; do not import the reversible point's canonical duration weight; do not infer `(CT)` from finite coefficients; and do not identify the connected route with bare tail shift despite `(BRE)` without additional mathematics.
