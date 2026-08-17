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

Latest meeting: `meetings/023-stationary-boundary-control-hierarchy-reopens-one-proof-test.md`, `state_narrowed: yes`.

Active work:

- Student G: `students/student-g/assignment-009.md`, bounded asymptotic route-decision block on `(J-SPEC)`; mathematical task unchanged, with an intermediate-commit durability addendum after two session freezes.
- Student F: `students/student-f/assignment-015.md`, bounded feasibility test of stationary boundary-control corrector concatenation.
- No third route/session is authorized.

## Closed / stopped mechanisms

Closed or stopped mechanisms include fixed finite walls, cellwise nonnegative insertion, one-step centered `L^1`, crude scalar sup criteria, exposed-only and full nearest-neighbour scalar coupling products, depth-uniform finite common-mass mode closure, raw finite-window Hamming enumeration, and larger exposure-state ancestry tracking.

Abandoned as a load-bearing interface after Meeting 019:

- common-uniform global coalescence / zero-frequency disagreement occupation.

Recorded as exhausted after Meeting 021:

- the current centered predecessor-trail/profile implementation based on composing the present signed insertion through successive zero-boundary segments.

Outside consultation 002 returned `no-credible-route` for the architectures then on the table. Its exact trajectory-valued spatial kernel remains useful, but full path-space TV/KL contraction is impossible because

$$
Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot).
$$

Meeting 023 records that the principal's later stationary occupation-control hierarchy is **not** the same path-space architecture and is not ruled out by that theorem.

## Route-decision branch: `(J-SPEC)`

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

The principal's independent finite-box study suggests that the singleton absolute-duration norm may itself be supercritical at strict residual points. With

$$
J_n=\frac gB N_n,
$$

define

$$
\boxed{
\rho_J(a,b,c)
=
\limsup_{n\to\infty}J_n^{1/n}.
}
$$

Student G Assignment 009 must decide asymptotically whether

$$
\rho_J>1
$$

at the strong-growth point

$$
\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right),
$$

or prove a genuine opposite theorem. Larger finite-depth values alone do not count.

If G is unresolved without an asymptotic mechanism, stop the `J-SPEC` branch. Meeting 023 supersedes the older instruction that such an outcome automatically stops the whole programme, because F015 now tests genuinely new input.

## New architecture: stationary boundary-control hierarchy

Durable note:

`notes/principal-stationary-boundary-control-strategy.md`.

Use the complemented spin `xi=1-eta`, so `1` is the East facilitator. For a block `x in {0,1}^N` and fixed right-boundary value `u`, let `L_N^u` be the finite generator and define

$$
\boxed{
\mathcal K_N
=
\left\{
 m(x,u)\ge0:
 \sum_{x,u}m(x,u)=1,
 \quad
 \sum_{x,u}m(x,u)L_N^uF(x)=0
 \ \forall F
\right\}.
}
$$

Meeting 023 independently checks:

1. every infinite-volume invariant law projects to an element of `K_N`;
2. every `m in K_N` is the stationary occupation measure of a finite chain with a randomized state-dependent boundary controller;
3. projecting `K_{N+1}` to the first `N` sites with the old `N`th spin as boundary control lands in `K_N`;
4. therefore the stationary diameter
   $$
   D_N(h)=\sup_{m\in K_N}m(h)-\inf_{m\in K_N}m(h)
   $$
   is nonincreasing in `N` for fixed local `h`;
5. finite LP duality gives
   $$
   U_N(h)=\inf_F\max_{x,u}(h(x)-L_N^uF(x)),
   $$
   $$
   \ell_N(h)=\sup_F\min_{x,u}(h(x)-L_N^uF(x)),
   $$
   with
   $$
   D_N(h)=U_N(h)-\ell_N(h).
   $$

Hence

$$
\boxed{D_N(h)\to0\text{ for every local }h}
\tag{S}
$$

would prove uniqueness of the invariant measure without assuming spatial translation invariance.

This static theorem would not yet prove convergence from arbitrary initial states.

## Proposed multiscale target

The principal proposes a scale recursion such as

$$
\boxed{
D_{2N}(h)
\le
(1-\rho)D_N(h)+Ce^{-\gamma N}
}
\tag{R}
$$

for fixed residual rates and all large `N`.

The suggested mechanism is that neighbour-independent soft resets create facilitators and hard-East relaxation then screens a macroscopic left block from the far-right boundary.

The Professor checked the cited KCM-book inputs:

- East Theorem 7.6 gives exponential convergence of local observables once a facilitator is present in the oriented future;
- East Theorem 7.8 gives linear finite-volume mixing time with empty or ergodic boundary.

These do **not** directly prove `(R)` for the noisy process under arbitrary state-dependent boundary control. The missing theorem is a robustness/concatenation statement which uses the actual soft resets rather than conditioning them away.

Student F Assignment 015 must determine whether finite Bellman/Poisson correctors concatenate into a repeatable scale theorem, or identify a precise obstruction. Smaller numerical `D_N` values or larger finite LP certificates without repeatability do not count.

## Later dynamic upgrade

If static screening `(S)` is proved, a later step would need uniform distributional screening of far-right perturbations, schematically

$$
S_N(h)
\le
C_h\left(D_{\lfloor N/2\rfloor}(h)+e^{-\gamma N}\right).
\tag{ZF}
$$

Combined with finite-seed local coupling, this would give convergence from arbitrary initial laws. `(ZF)` is not active until the static route is established.

## Other unresolved facts

Still open:

- `(J-SPEC)`;
- the stationary screening recursion `(R)`;
- one- and two-step tail-shift agreement off the product surface;
- `Gamma_M->0` and general `J_{x,r}->0`;
- common-uniform extinction versus convective survival;
- weak ergodicity of the reachable trajectory kernel `Q`;
- full ergodicity in the residual chamber.

On the exact surface `a=b(1-c)`, the zero-boundary invariant law is Bernoulli product and the signed insertion obstruction vanishes.

## Anti-circularity

Do not infer asymptotic `J` growth from finite depths; treat shrinking finite `D_N` values as a multiscale theorem; invoke hard-East relaxation without proving robustness to the soft controlled dynamics; revive predecessor-trail/profile composition, global common-uniform occupation, or path-space `Q` contraction; or treat static uniqueness as full convergence.

## Wiki

Keep the live wiki frozen during research.
