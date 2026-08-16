# Group meeting 007: G's live-edge resolvent identifies restart count as the coupling-side block bottleneck

Date: 2026-08-16

Professor review of:

- Student G, commit `c7a33b5`, `students/student-g/002-density-to-regional-control.md`;
- exact verifier commit `e20847a`, `students/student-g/002-regional-moment-verifier.py`;
- Meeting 006 and the current block mass/disagreement target;
- Student F's live-coupling results from Assignments 003--004.

Operational correction: Meetings 003--006 recorded Student G as still working on Assignment 002, but the session was in fact producing only a stub `Completed` and committing nothing. The principal re-prompted it, after which the present report was produced. This explains the delay but has no mathematical bearing on the report.

state_narrowed: yes

Evidence pointer: `students/student-g/002-density-to-regional-control.md`, especially Sections 5--9, and `students/student-g/002-regional-moment-verifier.py`.

## What is old versus new

G independently reproduces the one-cell positive regional kernel and the two-hidden-cell sign failure

$$
\Psi_\Delta(z)=B K_\Delta(z)-c.
$$

This corroborates Student F Assignment 002 but does not reopen that closed route.

G also derives a two-site weighted `L^-` correlation ODE. It is correct and reusable, but it is not the present load-bearing object.

The new target-relevant content is a conditional **live-exposure resolvent** for the high-risk coupling state `J_i` inside an arbitrary-depth disagreement configuration.

## Professor verification: non-rightmost exposure chain

Write

$$
d=b-a,
\qquad k=1-c,
\qquad q=1-c+a.
$$

At a stopping time with

$$
D_i=0,
\qquad D_{i+1}=1,
$$

define

$$
K_i=1_{\{X_i=Y_i=0\}},
\qquad
J_i=1_{\{X_i=Y_i=1\}}
$$

on this exposure event. Stop at the first time `e` when either site `i` becomes a disagreement or site `i+1` coalesces.

Before `e`, the common spin at `i` has exact rates

$$
K\xrightarrow{a}J,
\qquad
K\xrightarrow{d}\text{child},
$$

$$
J\xrightarrow{k}K,
\qquad
J\xrightarrow{c}\text{child}.
$$

Meeting 004 gives predictable coalescence intensity at site `i+1` at least

$$
q=1-c+a
$$

regardless of whether that disagreement is rightmost and regardless of all deeper disagreements to its right. Replacing its actual killing rate by the constant lower rate `q` therefore gives a valid upper comparison for child probability and nonnegative occupation times.

Put

$$
\mathfrak D=(b+q)(1+q)-a(1-c).
$$

The killed two-state backward equations give

$$
h_0=\frac{d(1+q)+ac}{\mathfrak D},
\qquad
h_1=\frac{c(b+q)+(1-c)d}{\mathfrak D},
$$

with

$$
1-h_0=\frac{q(a+q+1)}{\mathfrak D}>0,
$$

$$
1-h_1=\frac{q(d+2q)}{\mathfrak D}>0,
$$

and `h_1>h_0`. Thus at every such exposure stopping time,

$$
\boxed{
P(\text{left child before right coalescence}\mid\mathcal F)
\le h_{X_i}<1.
}
$$

This extends the Assignment 003 one-source formula to every exposed edge inside an arbitrary-depth stack.

## Professor verification: exact `J_i` occupation and compensator

Let `g_x` denote expected time spent in the high-risk state `J` before the exposure ends in the constant-`q` comparison chain. The resolvent equations give

$$
\boxed{
g_0=\frac a{\mathfrak D},
\qquad
g_1=\frac{b+q}{\mathfrak D}.}
$$

Hence for the true exposure,

$$
\boxed{
E\left[\int_s^e J_i(t)\,dt\mid\mathcal F_s\right]
\le g_{X_i(s)}\le g_1.
}
$$

More importantly, before `e` the exact child-creation intensity is

$$
d+(c-d)J_i(t).
$$

Therefore the compensator identity is

$$
\boxed{
P(\text{child before right coalescence}\mid\mathcal F_s)
=
E\left[\int_s^e\bigl(d+(c-d)J_i(t)\bigr)dt\mid\mathcal F_s\right].
}
$$

This is the weighted occupation statement that the older marginal `11` estimate could not provide.

## Why crude all-time summation still fails

Let `N_i(T)` be the number of exposure intervals at edge `(i,i+1)` started by time `T`. G proves the pathwise bound

$$
N_i(T)\le1+C_i(T)+B_{i+1}(T),
$$

where `C_i` counts coalescences at `i` and `B_{i+1}` creations at `i+1`. Consequently

$$
E\int_0^T J_i(t)dt
\le
\frac{b+q}{\mathfrak D}
\left[
1+\int_0^T u_i(t)dt+c\int_0^T u_{i+2}(t)dt
\right].
$$

This estimate is valid but too crude for contraction. On the near-East path

$$
a=\varepsilon^2,
\quad b=\varepsilon,
\quad c=1-\varepsilon^2,
$$

one has

$$
q=2\varepsilon^2,
\qquad
g_1=1-2\varepsilon^2+O(\varepsilon^3),
$$

and therefore

$$
q-(c-d)g_1=-1+O(\varepsilon).
$$

So substituting this crude global `J_i` bound into the disagreement drift destroys the near-East gain.

The loss is not in a single exposure: the single-exposure compensator is exact. The loss is the **number of exposure re-entries/restarts** created by deaths, reinfections, and deeper ancestry.

## Notation collision with the current trail criterion

G's

$$
J_i=1_{\{D_i=0,D_{i+1}=1,X_i=Y_i=1\}}
$$

is a local coupling indicator.

Meeting 006's

$$
J_{x,r}
=B(b-a)^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du
$$

is the global right-weighted invariant trail quantity whose decay would control the nonempty-exit term.

They are **not the same object**. G's near-East obstruction does not refute `J_{x,r}->0` and does not contradict the active trail route. Instead it says that one cannot prove the needed block contraction merely by globally summing the local `J_i` occupation through the crude exposure-entry estimate.

## Relation to the Meeting 006 mass/disagreement stack

Meeting 006 decomposes each centered insertion as

$$
(b-a)\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).
$$

The second term is a conditional-law disagreement channel. G's exposure theorem supplies an exact local resolvent once such a coupled disagreement is exposed to the next unresolved site. Repeated exposure entries are the coupling-side manifestation of the same unresolved branching/restart issue that Meeting 006 left in the mass/disagreement block theorem.

Thus G's return does not change the main target again. It sharpens the block bottleneck:

> local disagreement transmission within one exposure is controlled; the missing estimate is a regeneration/restart-count bound that remains compatible with signed mass branching.

This is a genuine narrowing.

## Ruling and next work

Student F continues Assignment 007 unchanged: attack the complete block mass/disagreement contraction.

Student G is now routed to the complementary coupling side. It should convert its single-exposure resolvent into a renewal/corrector estimate for repeated exposure entries of the conditional-law disagreement channel, and either close a block contraction or produce an exact obstruction.

The next accepted G result must control the restart count structurally. Another per-exposure calculation or marginal occupation bound will not count.
