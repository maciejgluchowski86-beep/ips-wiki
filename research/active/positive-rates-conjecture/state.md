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

Latest meeting: `meetings/030-signed-boundary-transmission-is-final-g010-blocker-no-restart.md`, `state_narrowed: yes`.

Active work:

- Student G: idle; no G011.
- Student F: idle; no F016.
- No proof architecture is currently active.

Operative proof-architecture status: **`no-credible-route`**, in the consultation-002 / Meeting-025 sense. This does not say the conjecture is false or that every conceivable proof architecture is impossible.

Assignment 010 is complete unresolved after substantive work. The out-of-order / in-flight checkpoints are treated as orchestration overlaps, not student disregard of the stop.

## Canonical `J` quantity and fixed-filter renewal

For singleton depth `n`,

$$
J_n=\frac BgR_n=\frac gBN_n,
\qquad
B=b+c-a,\quad g=b-a,
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

The sufficient connected-tail target

$$
\sum_{k\ge8}|\lambda_k|<\delta_7,
\qquad
\delta_7:=\sum_{k=1}^7\lambda_k-1>0,
\tag{CT}
$$

remains open.

## Accepted G010 positive-frequency mathematics

The stationary terminal factor is

$$
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}.
$$

The repaired verifier `ce77c9c` proves a depth-independent signed kernel bound with

$$
B\Theta_\sharp<1,
$$

hence

$$
\operatorname{osc}\left(
R_{N+1}Q_{N+1}(Y_{N+1}f)
\right)
\le q_\sharp\operatorname{osc}(f),
\qquad q_\sharp<1.
\tag{HP}
$$

The scalar multiplier of `R_N` vanishes at positive frequency `x=1/100`, so this one high-pass seminorm cannot be generically inverted.

Late checkpoint `75d0e8a`, accepted in Meeting 028, eliminates the stationary marginal-discrepancy / bare tail-shift functional from the connected coefficient. Thus unrestricted tail-shift TV is not logically required for the connected fixed-filter coefficient.

The corrected complementary split is

$$
R_N=m_0I+g_0(I-K_N),
\qquad
K_N=(1+b)((1+b)I-L_N)^{-1}.
\tag{CH}
$$

The positive-frequency zero is cancellation between these two channels. The genuine high-pass `I-K_N` has only the zero-frequency kernel. Each channel has a depth-uniform one-step estimate and their post-insertion channelwise triangle bound is strictly below one, but no frame/reverse estimate makes this an iterable two-component norm.

## Fresh-coordinate recentering and exact transmission branch

Put

$$
r=1+b=11/10,
\qquad
\varepsilon=9/10000,
\qquad
X_N=Y_N+\varepsilon,
\qquad
g_0=999/10000.
$$

With `A_N=-L_N`, the fresh recentered insertion satisfies

$$
\boxed{
A_NM_{X_N}
=
M_{X_N}(A_{N-1}+r)
-g_0B M_{\eta_N}P_{N-1}.
}
\tag{INT}
$$

Thus the only failure of exact fresh frequency shift is transmission through the old right-boundary projection. After regrouping `Y=X-\varepsilon`, the exact semigroup identity is

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

The fresh shifted branch and scalar branch are individually subcritical under safe absolute-value bounds:

$$
BZ_{\omega+r}
=\frac{1065933}{1068400}<1,
\qquad
\varepsilon Z
=\frac{1719}{3100}<1.
\tag{SUB}
$$

Verifier `010k-boundary-reduction-verifier.py` at `adf50d9` exactly checks these scalar identities and the other quoted rational inequalities in the late G010 reductions.

The only uncontrolled branch in `(TRI)` is therefore the signed boundary-transmission Volterra operator

$$
\boxed{
\begin{aligned}
\mathcal V_N f
:={}&B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}\\
&\hspace{26mm}\times
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt,
\end{aligned}
}
\tag{V}
$$

where `h(t)=w_*(t)\sigma(t)` is the fixed signed filter kernel. Both the inner coefficient and `h` change sign. No depth-uniform estimate retaining this two-time cancellation was proved.

This is now the sharpest residual formulation of the connected-renewal route: control `\mathcal V_N` on the **actual connected orbit** strongly enough to make the renewal coefficients summable/geometric.

## Reversible reference results retained

At the corrected reversible reference point

$$
P_0=(1/10000,1/10,999/1000),
$$

with the actual `P_*` duration weight and filter frozen externally, verifier `56d47cb` proves

$$
|xq(x)|<1\qquad(x>0),
$$

and the fresh centered insertion satisfies the dimension-free variational estimate

$$
M_X^*A_{0,N}^{-1}M_X
\le
\frac{998001}{11000000}I.
$$

Hence the frozen-reference transfer has a strict fresh-insertion Sobolev bound

$$
\|A_{0,N}^{1/2}\widetilde Q_{0,N}^\sigma(Y_Nf)\|_2
\le
\left(
\sqrt{\frac{998001}{11000000}}+\frac9{400}
\right)\|f\|_2
<\|f\|_2.
$$

Commit `c444db5` further gives an exact orthogonal left-slice decomposition

$$
L_{0,N}=L_{0,N-1}\oplus G_{N-1},
$$

and hence

$$
T_{0,N}=T_{0,N-1}\oplus H^\sigma(G_{N-1})J_{N-1}.
$$

Thus the entire frozen-reference transfer norm reduces to a single killed self-adjoint channel family. This does not transport automatically to the actual nonreversible `P_*` orbit.

## Raw one-step coefficient obstruction strengthened

Commit `d9c477e` proves that no norm

$$
\|f\|_{\theta,\phi}
=
\sum_{A\ne\varnothing}
\theta^{|A|}\phi^{\kappa(A)}|x_A|
$$

with `theta,phi>0` makes the actual nonconstant raw coefficient semigroup uniformly nonexpansive in depth. Long blocks, separated dimers, and separated singletons give incompatible necessary inequalities. The scalar contradiction is checked in `adf50d9`.

Therefore a multiplicative component-count weight does not repair the 010a one-step Lyapunov route. Filter/resolvent-level cancellation remains load-bearing.

## Current blocker and restart bar

Assignment 010 is closed. The restart bar is now specific:

> New input must control the signed boundary-transmission operator `(V)` on the actual connected orbit, retaining its two-time cancellation strongly enough to yield summable/geometric connected coefficients, or supply a materially different proof architecture.

A generic search for another norm, another reversible comparison, another filter, larger finite coefficient tables, bare tail-shift agreement, common-coupling occupation, or Bellman/joint-corrector variants does not clear the bar.

No G011; no F016; both students idle; no active proof architecture. Consultation 002 / Meeting 025 `no-credible-route` is operative pending genuinely new principal, external, or literature input.

## Other retained exact mathematics

The stationary occupation-control hierarchy, common-coupling fixed-site facts, exact trajectory-valued spatial kernel, previous predecessor-profile reductions, and G009 singular fixed-depth theorem remain correct but inactive as recorded in earlier meetings.

## Unresolved target-level facts

Open:

- `(J-SPEC)` and `(CT)`;
- the actual-orbit signed boundary-transmission estimate `(V)`;
- one-/two-step tail-shift agreement off the product surface;
- `Gamma_M->0` and general `J_{x,r}->0`;
- common-uniform extinction versus convective survival;
- stationary diameter collapse `D_N(h)->0`;
- full ergodicity in the residual chamber.

## Wiki

Keep the live wiki frozen during research.
