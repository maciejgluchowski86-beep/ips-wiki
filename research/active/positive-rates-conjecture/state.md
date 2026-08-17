# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** Proof routes may be closed or redirected; the target does not change.

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

Latest meeting: `meetings/029-fresh-insertion-sobolev-gain-narrows-route-but-current-generation-may-finish.md`, `state_narrowed: yes`.

Formal work status:

- Student G: idle; no G011. One response was already in flight before the idle ruling could be relayed; Meeting 029 instructs the principal not to destroy that response by clicking stop, but this is not formal reactivation. Do not prompt G again after the current response returns.
- Student F: idle; no F016.
- No proof architecture is formally active.

Operative proof-architecture status remains **`no-credible-route`** in the consultation-002 / Meeting-025 sense, unless the already-running G response produces a theorem clearing the explicit restart bar.

## Stopped / inactive interfaces

Stopped or inactive mechanisms include:

- common-uniform global coalescence / zero-frequency disagreement occupation (Meeting 019);
- the repeated-equilibrium centered predecessor-trail/profile implementation (Meeting 021);
- global path-space TV/KL contraction of the exact trajectory kernel `Q`;
- the stationary boundary-control Bellman-corrector concatenation implementation (Meeting 024);
- G009's singular fixed-depth short/long renewal continuation (Meeting 025);
- the fixed-filter connected dual-renewal continuation after the bounded Assignment 010 block (Meetings 027--028).

Operational overlaps after the stop are not treated as student disregard. Late checkpoints are retained and reviewed, but do not automatically reopen work.

## Canonical `J` quantity and exact fixed-filter renewal

For singleton depth `n`,

$$
\boxed{
J_n=\frac BgR_n=\frac gBN_n,
}
\qquad B=b+c-a,\quad g=b-a,
$$

so

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}
$$

is also the root growth rate of `R_n` and `N_n`. `(J-SPEC)` remains open.

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

with fixed filter

$$
\sigma(u)=1-2e^{-(4/125)u},
$$

the invariant projections can be extracted exactly as renewal separators. The fixed signed witness obeys

$$
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1.
$$

Commit `e4452de` exactly verifies the first seven rational coefficients, with

$$
\lambda_1,\ldots,\lambda_5>0,
\qquad
\lambda_6,\lambda_7<0,
\qquad
\sum_{k=1}^7\lambda_k>1.
$$

The sufficient tail target

$$
\sum_{k\ge8}|\lambda_k|
<
\delta_7,
\qquad
\delta_7:=\sum_{k=1}^7\lambda_k-1>0,
\tag{CT}
$$

remains open.

## G010 terminal high-pass theorem

Assignment 010 derives

$$
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}.
$$

For the actual fixed `P_*` duration weight and filter, repaired verifier `ce77c9c` proves

$$
\|\kappa\|_1\le\Theta_\sharp,
\qquad
B\Theta_\sharp<1,
$$

with `B Theta_sharp` about `0.98073728315`. Hence

$$
\operatorname{osc}\left(
R_{N+1}Q_{N+1}(Y_{N+1}f)
\right)
\le q_\sharp\operatorname{osc}(f),
\qquad q_\sharp=B\Theta_\sharp<1.
\tag{HP}
$$

The single multiplier

$$
R(x)=\frac{d+gx}{1+b+x}
$$

vanishes at `x=|d|/g=1/100`, so this one-high-pass seminorm cannot be generically inverted.

## Exact boundary-resolvent elimination

Late checkpoint `75d0e8a`, accepted in Meeting 028, eliminates the stationary marginal-discrepancy functional from the connected coefficient. With

$$
q_N=Q_Nf_N,
\qquad
f_N=Y_NQ_{N-1}f_{N-1},
$$

$$
r=1+b,
\qquad
S_N=(rI-L_N)^{-1},
\qquad
D_N=(I-L_N)S_N,
$$

one has exactly

$$
 c_{N+1}
 =A_N\!\left[
 \frac dr q_N
 +\left(g-\frac dr\right)B
 D_NP_NS_Nq_N
 \right].
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

Thus bare tail-shift TV is not logically required for the connected coefficient. The elementary supnorm bound from `75d0e8a` gives no depth decay.

## New complementary high-pass split

Late corrected checkpoint `010h-recentered-boundary-channel-checkpoint.md` at `81a836c` decomposes

$$
\boxed{
R_N=m_0I+g_0(I-K_N),
\qquad
K_N=r(rI-L_N)^{-1}.
}
\tag{CH}
$$

The blind frequency of `R_N` is therefore cancellation between a small scalar channel and a genuine high-pass channel; `I-K_N` itself vanishes only at frequency zero.

For the fixed filter, uniformly in depth,

$$
\operatorname{osc}\bigl(g_0(I-K_N)Q_Nf\bigr)
\le\frac{999}{2750}\operatorname{osc}(f),
$$

and

$$
\operatorname{osc}(m_0Q_Nf)
<\frac{660971283}{1210937500}\operatorname{osc}(f).
$$

After one ordinary insertion the channelwise triangle estimate is strictly below one:

$$
B\left(
\frac{999}{2750}
+
\frac{660971283}{1210937500}
\right)
<
\frac{12097480772637}{12109375000000}
<1.
\tag{CHC}
$$

This is not yet an iterative two-component contraction: no depth-uniform frame/reverse estimate recovers the next raw connected input from the two outputs.

The correction at `81a836c` is load-bearing. Recentring removes the scalar `I` off-diagonal, but the old `Y`-coefficient projection becomes a small non-orthogonal tilt in the product-centered `X` geometry,

$$
\beta=-\frac{\sqrt{10}}{1110},
\qquad |\beta|<1/300,
$$

rather than an orthogonal projection.

## Exact fresh-coordinate intertwining

The recentered insertion obeys

$$
\boxed{
A_NM_{X_N}
=
M_{X_N}(A_{N-1}+r)
-g_0B M_{\eta_N}P_{N-1},
\qquad A_N=-L_N.
}
\tag{INT}
$$

Thus a fresh `X` insertion shifts temporal frequency by the fixed amount `r=11/10`; the only failure of exact intertwining is transmission through the old right-boundary projection. The Duhamel form separates the raw `Y` insertion into a fresh shifted branch, a small scalar branch, and this boundary-transmission branch.

## New reversible fresh-insertion Sobolev theorem

At the corrected reversible reference point

$$
P_0=(1/10000,1/10,999/1000),
$$

keep the **actual `P_*` duration weight and filter frozen externally**. Let

$$
A_{0,N}=-L_{0,N}
$$

in the product reversible space and define

$$
q(x)=Z_{\omega+x}-2Z_{\omega+\tau+x}.
$$

Commit `56d47cb` exactly verifies the rational multiplier and

$$
\boxed{|xq(x)|<1\qquad(x>0).}
\tag{SQ1}
$$

For the fresh product-centered insertion `M_Xf=X_Nf`, the site-`N` Dirichlet form gives the dimension-free variational estimate

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

For the actual insertion `Y=X+m_0`, the same frozen-weight reference transfer satisfies

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

This is accepted as a genuine all-depth fresh-insertion positive-frequency theorem for the reversible reference model. It is not yet an estimate on the actual `P_*` connected orbit.

## Current blocker and restart bar

The new checkpoints materially improve the local mechanism:

- the blind frequency is split into explicit complementary channels with strict channelwise one-step bounds;
- the only failure of exact fresh-coordinate frequency shift is the old-boundary transmission term;
- the reversible fresh insertion gains one half derivative, and the fixed filter converts it into an `H^1` output with a large exact margin.

But the restart bar is not yet cleared. What remains is either:

1. a depth-uniform two-seminorm/energy inequality propagating `(SQ4)` through the **actual** nonreversible defect `L_*-L_0` and the explicit boundary tilt/transmission term; or
2. an orbit-specific theorem giving summable/geometric decay of the connected coefficients.

A naive use of the reference spectral gap to convert the `H^1` output back to `L^2` loses the margin. No acceptable actual-orbit iteration theorem is yet supplied.

Meeting 029 therefore does not formally reactivate G. The principal should let the response already in flight finish rather than destroy it, then route the result and send no further prompt before a new ruling.

## Other retained exact mathematics

The stationary occupation-control hierarchy, common-coupling facts, exact trajectory kernel, and earlier profile reductions remain correct but inactive as recorded in previous meetings.

## Unresolved target-level facts

Open:

- `(J-SPEC)` and `(CT)`;
- an actual-`P_*` propagation/iteration theorem for `(CH)`--`(SQ4)`;
- one-/two-step tail-shift agreement off the product surface;
- `Gamma_M->0` and general `J_{x,r}->0`;
- common-uniform extinction versus convective survival;
- stationary diameter collapse `D_N(h)->0`;
- full ergodicity in the residual chamber.

## Wiki

Keep the live wiki frozen during research.
