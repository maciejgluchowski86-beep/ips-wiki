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

## E0. Route status

Closed/stopped mechanisms include fixed walls, cellwise nonnegative insertion, one-step centered `L^1`, crude scalar sup criteria, exposed-only and full nearest-neighbour scalar coupling products, depth-uniform finite common-mass mode closure, raw finite-window Hamming enumeration, and larger exposure-state ancestry tracking.

Meeting 019 abandons common-uniform global coalescence / zero-frequency disagreement occupation as the load-bearing interface.

Meeting 021 records the current centered predecessor-trail/profile implementation as exhausted after recombination and finite propagation both terminate at zero-frequency spatial tail memory.

Consultation 002 proves the exact trajectory-valued spatial kernel `Q` but also

$$
Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot),
$$

so global path-space TV/KL contraction is unavailable.

Meeting 023 opens a genuinely different stationary occupation-control architecture. Meeting 024 keeps its exact hierarchy but stops the current Bellman-corrector concatenation implementation after F015 identifies the weighted adaptive-feedback bottleneck and refutes additive block concatenation.

Student G Assignment 009 is now the sole active block.

## E1. Predecessor-trail route-decision object

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

The accepted predecessor-trail reduction gives the sufficient absolute-duration quantity

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_kw(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
$$

For singleton depth `n`, the principal normalization is

$$
J_n=\frac gB N_n,
$$

and

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}.
$$

Student G Assignment 009 decides

$$
\boxed{
\rho_J>1\text{ at a strict residual point}
\quad\text{or}\quad
\rho_J<1\text{ on a genuine residual region.}
}
\tag{J-SPEC}
$$

Finite-depth growth alone is not decisive.

## E2. G009 checkpoint: exact reverse-transfer normalization

Define the insertion/drop map on signed measures by

$$
(\mathcal J_N\nu)(f)=\nu((B\eta_N-c)f).
$$

G checkpoint `2cb0696` reconstructs the exact scalar reverse transfer

$$
S_n(u_1,\ldots,u_n)
=
\pi_nP_{u_1}^n\mathcal J_nP_{u_2}^{n-1}\mathcal J_{n-1}\cdots P_{u_n}^1\mathcal J_1
$$

and proves

$$
\boxed{S_n(u)=g^n\pi_n(F_u).}
$$

Let

$$
R_n=\int\left(\prod_jw(u_j)\right)|S_n(u)|du.
$$

Then exactly

$$
\boxed{
J_n=\frac BgR_n=\frac gBN_n,
}
$$

hence

$$
\limsup R_n^{1/n}
=
\limsup J_n^{1/n}
=
\limsup N_n^{1/n}.
$$

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

the checkpoint verifies

$$
B/g=111/10,\qquad Z=19100/31,
$$

$$
J_1=190809/31000,
\qquad
N_1=21179799/310000.
$$

These values only calibrate the exact normalization; they do not decide `(J-SPEC)`.

## E3. Exhausted signed-profile interface

The old profile implementation established strict one-segment damping, exact operator-valued transfer, suffix projectivity, fixed-suffix positive-frequency localization, and exact two-insertion formulas.

F013 proves that the unsplit two-insertion transfer retains a genuine zero temporal-frequency projection. F014 proves that fixed-suffix mixing and finite propagation leave

$$
\Delta_M^{(2)}
=\|\theta^2\mu-\mu\|_{\mathcal F_M},
$$

with

$$
\Gamma_M
\le
c^2Z\Delta_{\lceil M/2\rceil}^{(2)}+Ce^{-\gamma M}.
$$

No independent theorem controls this law. Further local profile composition is stopped.

## E4. Exhausted common-uniform occupation interface

For finite common-uniform disagreement seeds, every fixed site eventually couples permanently and possible survival is convective escape. The retained first-exposure exploration has an explicit front tail, but G008 proves that the projected state forgets post-coalescence ancestry and robust zero-frequency closure loses every strict contraction factor.

The missing all-depth return variable is itself a disagreement occupation quantity. Global common-uniform occupation is stopped as the proof interface.

## E5. Trajectory-valued spatial kernel

The one-sided stationary trajectory field is Markov in space on

$$
D(\mathbb R,\{0,1\})
$$

with kernel `Q` defined by the local graphical construction.

However constant-zero and constant-one inputs produce mutually singular stationary output path laws. Hence the full path-space Dobrushin coefficient is one and TV/KL may be transmitted isometrically.

Weak ergodicity of the reachable zero-boundary orbit remains open, but no independent rate-level mechanism is known.

## E6. Exact stationary occupation-control hierarchy retained

Use complemented spins so `1` is the East facilitator. Let `L_N^u` be the generator on `N` sites with right-boundary action `u in {0,1}`.

Define

$$
\boxed{
\mathcal K_N
=
\left\{
 m(x,u)\ge0:\ \sum m=1,
 \quad \sum_{x,u}m(x,u)L_N^uF(x)=0\ \forall F
\right\}.
}
\tag{K}
$$

Meetings 023--024 establish:

1. every infinite invariant law projects into `K_N`;
2. every `m in K_N` is realized by a finite chain with a randomized state-dependent boundary controller;
3. `K_{N+1}` projects into `K_N` by using the old interface spin as the new action.

For local `h`,

$$
D_N(h)
=
\sup_{m\in K_N}m(h)-\inf_{m\in K_N}m(h)
$$

satisfies

$$
\boxed{D_{N+1}(h)\le D_N(h).}
$$

If `D_N(h)->0` for every local `h`, the IPS has a unique invariant measure.

This remains an exact static reduction, not an active proof route after Meeting 024.

## E7. Exact Bellman dual and scale-extension formula

Finite LP duality gives

$$
U_N(h)=\inf_F\max_{x,u}(h-L_N^uF),
$$

$$
\ell_N(h)=\sup_F\min_{x,u}(h-L_N^uF),
$$

$$
D_N(h)=U_N(h)-\ell_N(h).
$$

For optimal correctors define

$$
s_N^+(x,u)=U_N-h(x)+L_N^uF_N^+(x),
$$

$$
s_N^-(x,u)=h(x)-L_N^uF_N^-(x)-\ell_N.
$$

F015 proves for every `M>N`

$$
\boxed{
U_N-U_M=\inf_{m\in K_M}m(s_N^+),
}
$$

$$
\boxed{
\ell_M-\ell_N=\inf_{m\in K_M}m(s_N^-),
}
$$

and therefore

$$
\boxed{
D_M=D_N
-\inf_{m\in K_M}m(s_N^+)
-\inf_{m\in K_M}m(s_N^-).
}
\tag{BSE}
$$

Thus scale contraction is exactly unavoidable stationary occupation of old Bellman slack after the physical controller is moved farther right.

## E8. Bellman slack is weighted adaptive tracking

Complementary slackness gives a tight action `pi_F(x)` at every old block state. Since the two actions differ only through the flip rate at the old rightmost site,

$$
\boxed{
s_F(x,u)=w_F(x)1_{\{u\ne\pi_F(x)\}},}
\tag{WT}
$$

with

$$
w_F(x)=d(x_{N-1})|F(x^{N-1})-F(x)|,
\qquad d(0)=b-a,\quad d(1)=c.
$$

Put

$$
r_*=\min\{a,1-c\}>0.
$$

F015 proves, uniformly over arbitrary state-dependent controls and Boolean targets `pi`,

$$
\boxed{
P(X_N\ne\pi(X_0,\ldots,X_{N-1}))
\ge\frac{r_*}{N+1+r_*}.
}
\tag{UM}
$$

This is only an **unweighted** mismatch theorem. `(BSE)` requires occupation of `w_F` on mismatch states. No theorem prevents the controller from placing unavoidable mismatch where `w_F` is small.

The exact missing weighted theorem is schematically

$$
\boxed{
\inf_{K_{2N}}m(s_N^+)+\inf_{K_{2N}}m(s_N^-)
\ge \rho D_N(h)-Ce^{-\gamma N}.
}
\tag{WB}
$$

No independent mechanism for `(WB)` is known.

## E9. Additive block correctors are refuted

F015 proves that both boundary actions are tight somewhere for every optimal upper/lower corrector. Therefore for any appended right block and arbitrary function `G` on that block,

$$
H(x,z)=F_N(x)+G(z)
$$

cannot strictly improve either Bellman endpoint. At a maximum/minimum of `G`, the appended generator has the wrong sign for improvement and one chooses an old state where the realized interface action is tight.

Hence independently solved block correctors **do not concatenate**. Any strict improvement must use genuinely joint cross-block dependence.

At `(a,b,c)=(1/10,3/10,4/5)`, exact `N=2` correctors also satisfy both-action tightness in each one-spin interface cylinder, so the same obstruction kills an arbitrary correction depending on that single old interface spin plus the appended block.

This does not refute all joint correctors of growing interface width, but it kills the natural repeatable mechanism tested by Assignment 015.

## E10. Hard-East input does not control adaptive feedback

At one controlled spin,

$$
U_1=\frac{b}{b+1-c},
\qquad
\ell_1=\frac{a}{a+1},
$$

whereas fixed-boundary stationary densities are

$$
p_0=\frac{a}{a+1-c},
\qquad
p_1=\frac{b}{1+b}.
$$

At `(1/10,3/10,4/5)`,

$$
U_1=3/5,\quad \ell_1=1/11,
\quad p_0=1/3,\quad p_1=3/13.
$$

Thus adaptive state-dependent feedback is substantially stronger than either fixed boundary. The cited hard-East relaxation theorems with fixed or exogenous ergodic boundaries do not imply `(WB)`.

A future stationary-screening theorem would require a new robustness principle specifically controlling weighted adaptive feedback.

## E11. Meeting-024 stop decision

Meeting 023 authorized one feasibility block and required a repeatable theorem for continuation. F015 returns exact structural progress but no recursion forcing `D_N(h)->0`.

Decision:

- retain `(K)`, monotonicity, the Bellman dual, `(BSE)`, `(WT)`, and `(UM)` as reusable mathematics;
- stop the current stationary boundary-control corrector-concatenation implementation;
- no larger-`N` LP continuation;
- no generic search over wider joint interface correctors;
- no F016;
- Student F idle.

This is an expected-value stop, not a theorem that `D_N(h)->0` is false.

## E12. Current decision tree

Only G009 is active.

If G proves `rho_J>1` at a strict residual point, close the absolute-duration `J` domination there and retain the exact predecessor-trail identity only with additional signed right-region/duration cancellation.

If G proves `rho_J<1` on a genuine region, record the partial theorem but do not revive the exhausted profile implementation automatically.

If G returns unresolved without an asymptotic mechanism, the programme returns to consultation 002's `no-credible-route` state unless genuinely new principal/external input has arrived.

## E13. Static-to-dynamic gap

Even a future proof `D_N(h)->0` would establish uniqueness, not convergence from arbitrary initial laws. A separate uniform distributional-screening theorem would still be required before using the finite-seed local-coupling result to prove ergodicity.

## Anti-circularity checkpoint

Do not infer asymptotic `J` growth from finite depths; infer stationary screening from shrinking finite LP widths; replace weighted Bellman occupation by unweighted mismatch; continue by larger LPs/additive correctors/wider interface search without a new mechanism; invoke pure-East fixed-boundary mixing as if it controlled adaptive feedback; treat uniqueness as convergence; or revive stopped predecessor-trail/common-coupling/path-space contraction routes.
