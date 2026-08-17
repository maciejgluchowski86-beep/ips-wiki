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

Latest meeting: `meetings/024-bellman-slack-feedback-obstruction-stops-current-stationary-screening-test.md`, `state_narrowed: yes`.

Active work:

- Student G: `students/student-g/assignment-009.md`, bounded asymptotic route-decision block on `(J-SPEC)`; checkpoint `009a-canonical-j-recursion-checkpoint.md` is durable, but `(J-SPEC)` remains unresolved.
- Student F: idle. No F016 is authorized.
- No second proof route is active.

## Closed / stopped mechanisms

Closed or stopped mechanisms include fixed finite walls, cellwise nonnegative insertion, one-step centered `L^1`, crude scalar sup criteria, exposed-only and full nearest-neighbour scalar coupling products, depth-uniform finite common-mass mode closure, raw finite-window Hamming enumeration, and larger exposure-state ancestry tracking.

Abandoned as a load-bearing interface after Meeting 019:

- common-uniform global coalescence / zero-frequency disagreement occupation.

Recorded as exhausted after Meeting 021:

- the current centered predecessor-trail/profile implementation based on composing the present signed insertion through successive zero-boundary segments.

Consultation 002 returned `no-credible-route` for the architectures then on the table. Its exact trajectory-valued spatial kernel remains useful, but full path-space TV/KL contraction is impossible because

$$
Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot).
$$

Recorded as stopped after Meeting 024:

- the **current stationary boundary-control Bellman-corrector concatenation implementation** introduced in Meeting 023. The exact hierarchy remains valid, but no repeatable scale contraction was obtained and the natural additive block-corrector mechanism is refuted by a maximum-principle argument.

## Sole active branch: `(J-SPEC)`

The accepted predecessor-trail reduction gives the sufficient absolute-duration quantity

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du,
$$

where

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

For singleton depth `n`, the principal normalization is

$$
J_n=\frac gB N_n,
$$

and

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}.
$$

Student G checkpoint `2cb0696` reconstructs the exact reverse-transfer recursion. With

$$
S_n(u)=\pi_nP_{u_1}^n\mathcal J_nP_{u_2}^{n-1}\mathcal J_{n-1}\cdots P_{u_n}^1\mathcal J_1
$$

and

$$
R_n=\int\left(\prod_jw(u_j)\right)|S_n(u)|du,
$$

one has exactly

$$
S_n(u)=g^n\pi_n(F_u),
$$

$$
\boxed{
J_n=\frac Bg R_n=\frac gB N_n,
}
$$

so `R_n`, `J_n`, and `N_n` have the same exponential growth rate.

At the primary point

$$
(a,b,c)=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right),
$$

the checkpoint verifies

$$
\frac Bg=\frac{111}{10},\qquad Z=\frac{19100}{31},
$$

$$
J_1=\frac{190809}{31000},\qquad
N_1=\frac{21179799}{310000}.
$$

These are normalization checks only. G009 must still prove an asymptotic theorem, either `rho_J>1` at a strict residual point or a genuine opposite theorem. Larger finite-depth values do not count.

## Stationary boundary-control hierarchy: exact mathematics retained, active implementation stopped

Use complemented spins so `1` is the East facilitator. For a block `x in {0,1}^N` and fixed right-boundary value `u`, let `L_N^u` be the finite generator and define

$$
\mathcal K_N
=
\left\{
 m(x,u)\ge0:\ \sum m=1,
 \quad \sum_{x,u}m(x,u)L_N^uF(x)=0\ \forall F
\right\}.
$$

Meetings 023--024 establish:

1. every infinite-volume invariant law projects into `K_N`;
2. every `m in K_N` is the stationary occupation measure of a randomized state-dependent boundary controller;
3. the hierarchy is nested under block projection;
4. for local `h`,
   $$
   D_N(h)=\sup_{m\in K_N}m(h)-\inf_{m\in K_N}m(h)
   $$
   is nonincreasing;
5. exact LP duality gives upper/lower Bellman correctors `U_N,ell_N`, with `D_N=U_N-ell_N`;
6. `D_N(h)->0` for every local `h` would prove uniqueness of the invariant measure.

F015 sharpens scale extension. If `s_N^+` and `s_N^-` are optimal upper/lower Bellman slacks, then for every `M>N`,

$$
\boxed{
D_M(h)=D_N(h)
-\inf_{m\in K_M}m(s_N^+)
-\inf_{m\in K_M}m(s_N^-).
}
$$

Each slack is a weighted adaptive tracking error:

$$
\boxed{
s_F(x,u)=w_F(x)1_{\{u\ne\pi_F(x)\}},}
$$

where

$$
w_F(x)=d(x_{N-1})|F(x^{N-1})-F(x)|,
\qquad d(0)=b-a,\ d(1)=c.
$$

There is a controller-uniform **unweighted** mismatch theorem. With

$$
r_*=\min\{a,1-c\},
$$

for every Boolean target `pi` and every stationary controlled extension with physical interface spin `V=X_N`,

$$
\boxed{
P(V\ne\pi(X))\ge\frac{r_*}{N+1+r_*}.
}
$$

This does not control the weighted slack because mismatch may concentrate where `w_F` is small.

F015 also proves that no additive concatenation

$$
H(x,z)=F_N(x)+G(z)
$$

with arbitrary independently constructed appended-block corrector `G` can strictly improve either Bellman endpoint. Strict scale improvement requires genuinely joint cross-block dependence.

The exact remaining multiscale target is a weighted occupation theorem such as

$$
\inf_{K_{2N}}m(s_N^+)+\inf_{K_{2N}}m(s_N^-)
\ge \rho D_N(h)-Ce^{-\gamma N}.
$$

No independent mechanism for this estimate was obtained. The cited hard-East fixed/ergodic-boundary relaxation does not control the adaptive weighted feedback. Therefore no larger-`N`, wider-interface, or generic joint-corrector search is active.

This stop does **not** refute `D_N(h)->0` or every possible stationary-screening theorem.

## Current decision

G009 is the sole active block. F is idle.

If G proves `rho_J>1` at one strict residual point, the absolute-duration `J` domination is refuted there; the exact predecessor-trail identity survives, and any future use must retain right-region/duration cancellation.

If G proves `rho_J<1` on a genuine residual region, record the partial route theorem, but do not revive the exhausted profile implementation automatically.

If G returns unresolved without a genuine asymptotic mechanism, return to the Meeting-022 / consultation-002 state: **no presently identified proof architecture clears the continuation bar**, unless genuinely new external or principal input has arrived.

## Unresolved target-level facts

Open:

- `(J-SPEC)`;
- `D_N(h)->0` for the stationary occupation hierarchy;
- the weighted Bellman-slack occupation theorem;
- one- and two-step tail-shift agreement off the product surface;
- `Gamma_M->0` and general `J_{x,r}->0`;
- common-uniform extinction versus convective survival;
- weak ergodicity of the reachable trajectory kernel `Q`;
- full ergodicity in the residual chamber.

On `a=b(1-c)`, the zero-boundary invariant law is Bernoulli product and the signed insertion obstruction vanishes.

## Anti-circularity

Do not infer asymptotic `J` growth from finite depths; infer multiscale screening from shrinking finite LP widths; replace weighted Bellman mismatch by the proved unweighted mismatch bound; search larger LPs or additive block correctors after the Meeting-024 stop; invoke hard-East relaxation as if it controlled adaptive feedback; revive predecessor-trail/profile composition, global common-uniform occupation, or path-space `Q` contraction; or treat static uniqueness as full convergence.

## Wiki

Keep the live wiki frozen during research.
