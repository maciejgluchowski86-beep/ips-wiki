# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because the computation is exact, the witness is larger, or the constant is better. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed until changed or stopped by the principal: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/024-bellman-slack-feedback-obstruction-stops-current-stationary-screening-test.md`, `state_narrowed: yes`.
- Student G: sole active student, on `students/student-g/assignment-009.md`, the asymptotic `(J-SPEC)` route decision. Durable checkpoint `009a-canonical-j-recursion-checkpoint.md` fixes the exact recursion/normalization but does not decide `(J-SPEC)`.
- Student F: idle; no F016.

On `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the residual chamber is

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

### Route status

Meeting 019 abandons common-uniform global coalescence / zero-frequency disagreement occupation as the load-bearing proof interface.

Meeting 021 records the current centered predecessor-trail/profile implementation as exhausted after recombination and finite propagation both reduce to one-/two-step spatial tail memory.

Consultation 002 constructs an exact trajectory-valued spatial kernel `Q` but proves

$$
Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot),
$$

so global path-space TV/KL contraction is unavailable.

Meeting 024 stops the **current stationary boundary-control Bellman-corrector concatenation implementation**. The exact occupation hierarchy remains valid, but F015 obtained no repeatable scale theorem and proved that independently constructed additive block correctors cannot improve the Bellman endpoints.

### Sole active route-decision question `(J-SPEC)`

For singleton depth `n`, the canonical predecessor-trail absolute-duration quantity satisfies

$$
J_n=\frac gB N_n,
\qquad B=b+c-a,\quad g=b-a,
$$

and

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}.
$$

G checkpoint `2cb0696` reconstructs an exact reverse-transfer scalar `R_n` with

$$
\boxed{J_n=\frac BgR_n=\frac gBN_n,}
$$

so `R_n`, `J_n`, and `N_n` have the same exponential growth rate. At

$$
(a,b,c)=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right),
$$

the checkpoint verifies `B/g=111/10`, `Z=19100/31`, `J_1=190809/31000`, and `N_1=21179799/310000`; these are normalization checks only.

G009 must still prove an asymptotic theorem: `rho_J>1` at a strict residual point or a genuine opposite theorem. Larger finite-depth numerics do not count.

If G009 is unresolved without a new asymptotic mechanism, the programme returns to consultation 002's `no-credible-route` state unless genuinely new principal/external input arrives.

### Stationary occupation-control hierarchy retained as exact mathematics

In complemented spins, let `L_N^u` be the `N`-site generator with right-boundary control `u in {0,1}` and define

$$
\mathcal K_N
=
\left\{
 m(x,u)\ge0:\ \sum m=1,
 \quad \sum_{x,u}m(x,u)L_N^uF(x)=0\ \forall F
\right\}.
$$

Meetings 023--024 establish:

- every infinite invariant law projects into `K_N`;
- every `m in K_N` is realized by a finite chain with a randomized state-dependent boundary controller;
- the hierarchy is nested, so for local `h`,
  $$
  D_N(h)=\sup_{K_N}m(h)-\inf_{K_N}m(h)
  $$
  is nonincreasing;
- exact LP duality gives Bellman endpoints `U_N,ell_N` with `D_N=U_N-ell_N`;
- `D_N(h)->0` for every local `h` would prove uniqueness of the invariant measure.

F015 proves the exact scale-extension identity

$$
\boxed{
D_M=D_N-\inf_{K_M}m(s_N^+)-\inf_{K_M}m(s_N^-),
}
$$

where each Bellman slack is a weighted adaptive boundary-action mismatch

$$
\boxed{
s_F(x,u)=w_F(x)1_{\{u\ne\pi_F(x)\}}.}
$$

It also proves a controller-uniform unweighted mismatch bound

$$
P(X_N\ne\pi(X))\ge
\frac{\min(a,1-c)}{N+1+\min(a,1-c)},
$$

but no theorem prevents the mismatch from concentrating where the Bellman weight `w_F` is small.

Further, for arbitrary appended-block `G`, a corrector `F_N(x)+G(z)` gives no strict Bellman endpoint improvement by a maximum-principle argument. Any successful scale contraction therefore requires genuinely joint cross-block dependence.

The cited hard-East fixed/ergodic-boundary relaxation does not control this adaptive weighted feedback. No larger-`N`, wider-interface, or generic joint-corrector continuation is active.

This stop does not refute `D_N(h)->0` or every possible stationary-screening theorem.

## Most recently completed programme

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard.

## Wiki freeze

The live wiki remains frozen during active research.
