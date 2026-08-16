# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** Proof routes may be closed or redirected; the target does not change.

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

Latest meeting: `meetings/007-student-g-exposure-resolvent-and-restart-bottleneck.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-007.md`, block contraction of the trail-generated mass/disagreement stack;
- Student G: `students/student-g/assignment-003.md`, coupling-side restart-count bridge for the same block theorem.

Operational note: Student G's session had silently stopped producing work during Meetings 003--006; after re-prompt it completed Assignment 002 at commit `c7a33b5` with verifier `e20847a`. The delay carries no mathematical meaning.

## Closed proof mechanisms

1. Fixed finite agreed-block / frozen-exterior wall crossing.
2. Cellwise last-exit/scaffold insertion positivity: one-cell regional integration works, but two-cell hidden transfer changes sign on short cells.
3. Meeting 005 one-generation centered-transfer contraction `(T)`: exact near-East depth-two ratios tend to `3/2` without right killing and `7/5` with it, so one-step `L^1` contraction is false.

The canonical predecessor-trail decomposition remains active.

## Canonical trail and current all-depth criterion

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The principal's centered-dual working reduction gives a canonical predecessor trail with positive factor

$$
e^{-\omega\tau}.
$$

The right region has the segmentwise bound

$$
|R_{\gamma,t}(\eta)|\le C_A\prod_k s_1(u_k).
$$

With

$$
w(u)=e^{-\omega u}s_1(u),
$$

and

$$
Z=\int_0^\infty w(u)du
=\frac{\omega+1+B+a}{(\omega+a)(\omega+1+B)-a},
$$

direct trail-depth decay is already proved when

$$
\max\{c,g\}Z<1.
$$

The hard near-East regime remains.

The correct global right-weighted invariant quantity is

$$
\boxed{
J_{x,r}
=B g^{n-1}
\int_{(0,\infty)^n}
\left(\prod_k w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|du.
}
$$

Showing `J_{x,r}->0` with trail depth is sufficient for the nonempty-exit term. The complementary no-exit term and full Poisson-Mecke factorization still require independent audit before a closing proof.

## Mass/disagreement decomposition and stack drift

For a law `mu` with rightmost density `r`, left marginal `bar mu`, and conditional left laws `mu^1,mu^0`,

$$
\boxed{
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).
}
$$

The first term is a signed mass channel; the second is a positive conditional-law disagreement channel. Near East the equilibrium mass coefficient is order `epsilon^2`, the disagreement coefficient order `epsilon`, and the right-weighted equilibrium mass multiplier tends to `2/5`.

The principal reset coupling gives negative drift for unresolved disagreement-stack height. Student F independently proved the related local fact that every disagreement under the common-uniform coupling has coalescence intensity at least

$$
q=1-c+a=\omega.
$$

Stack recurrence alone does not control signed branching.

## Student G Assignment 002: exact live-exposure resolvent

Student G's return gives the missing **single-exposure weighted control** for the high-risk local coupling state

$$
J_i=1_{\{D_i=0,D_{i+1}=1,X_i=Y_i=1\}}.
$$

This `J_i` is not the global trail quantity `J_{x,r}` above.

At any stopping time with `D_i=0,D_{i+1}=1`, stop when either `i` becomes a disagreement or `i+1` coalesces. Write

$$
d=b-a,\qquad k=1-c,\qquad q=1-c+a,
$$

and

$$
\mathfrak D=(b+q)(1+q)-a(1-c).
$$

The exposure is upper dominated by the killed two-state chain

$$
K\xrightarrow{a}J,\qquad K\xrightarrow{d}\text{child},
$$

$$
J\xrightarrow{k}K,\qquad J\xrightarrow{c}\text{child},
$$

with killing to right coalescence at rate `q`. Consequently

$$
P(\text{child before right coalescence}\mid\mathcal F)
\le h_x<1,
$$

where

$$
h_0=\frac{d(1+q)+ac}{\mathfrak D},
\qquad
h_1=\frac{c(b+q)+(1-c)d}{\mathfrak D}.
$$

The expected high-risk occupation during one exposure obeys

$$
\boxed{
E\left[\int J_i(t)dt\mid\mathcal F\right]
\le g_x,
\qquad
g_0=\frac a{\mathfrak D},
\quad
g_1=\frac{b+q}{\mathfrak D}.
}
$$

The exact child compensator on that exposure is

$$
\boxed{
P(\text{child before right coalescence}\mid\mathcal F)
=E\int\bigl[d+(c-d)J_i(t)\bigr]dt.
}
$$

This holds for non-rightmost disagreements inside arbitrary-depth stacks.

## Why G's crude global summation is not the block theorem

If `N_i(T)` counts exposure entries, G proves

$$
E\int_0^T J_i(t)dt
\le
\frac{b+q}{\mathfrak D}
\left[
1+\int_0^T u_i(t)dt+c\int_0^T u_{i+2}(t)dt
\right].
$$

Near East,

$$
q-(c-d)g_1=-1+O(\varepsilon),
$$

so inserting this crude all-time bound into the disagreement drift loses all damping. The failure is caused by **repeated exposure entries/restarts**, not by the one-exposure resolvent.

This does not refute `J_{x,r}->0`. It identifies the coupling-side version of the same branching/restart problem left by the mass/disagreement decomposition.

## Current bottleneck: block mass/disagreement contraction with restart control

The active target remains a parameter-dependent block theorem. Seek a norm on trail-generated signed mass components and coupled disagreement components, weighted by unresolved stack/restart state, and finite constants

$$
m_0<\infty,\qquad \theta<1
$$

such that

$$
\boxed{\|T^{m_0}\nu\|_*\le\theta\|\nu\|_*.}
$$

Student F attacks the complete block theorem. Student G attacks the complementary coupling problem: control the exposure-entry/restart count for the conditional-law disagreement channel strongly enough to enter such a block norm, or give an exact obstruction.

## Anti-circularity rule

Do not rescue one-step `(T)`, return to cellwise positivity, globally replace `J_i` by marginal `11`, or enumerate fixed depths. The next accepted progress must control signed branching/restarts structurally, prove `J_{x,r}->0` by another all-depth mechanism, or produce a rigorous obstruction.

## Wiki

Keep the live wiki frozen during research.
