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

Latest meeting: `meetings/025-fixed-depth-j-renewal-is-supercritical-but-nonuniform-j-spec-stops.md`, `state_narrowed: yes`.

Active work:

- Student G: idle; no G010.
- Student F: idle; no F016.
- No proof architecture is currently active.

Operative proof-architecture status: **`no-credible-route`**. This is consultation 002's conclusion, now strengthened by Meetings 024--025. It is not a statement that the positive-rates conjecture is false or that every conceivable proof architecture is impossible.

## Closed / stopped mechanisms

Closed or stopped mechanisms include fixed finite walls, cellwise nonnegative insertion, one-step centered `L^1`, crude scalar sup criteria, exposed-only and full nearest-neighbour scalar coupling products, depth-uniform finite common-mass mode closure, raw finite-window Hamming enumeration, and larger exposure-state ancestry tracking.

Abandoned as a load-bearing interface after Meeting 019:

- common-uniform global coalescence / zero-frequency disagreement occupation.

Recorded as exhausted after Meeting 021:

- the current centered predecessor-trail/profile implementation based on composing the present signed insertion through successive zero-boundary segments.

Stopped after Meeting 024:

- the current stationary boundary-control Bellman-corrector concatenation implementation. The exact occupation hierarchy survives, but F015 obtained no repeatable weighted-slack theorem and independently constructed additive block correctors cannot improve the Bellman endpoints.

Stopped after Meeting 025:

- the authorized internal `(J-SPEC)` route-decision branch. G009 did not prove `rho_J>1` or `<1` at fixed strict rates; larger-depth continuation is not authorized.

Consultation 002's exact trajectory-valued spatial kernel remains useful, but full path-space TV/KL contraction is impossible because

$$
Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot).
$$

## Canonical predecessor-trail quantity and `(J-SPEC)` status

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

The accepted predecessor-trail reduction gives the sufficient absolute-duration quantity

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
$$

For singleton depth `n`, G checkpoint `2cb0696` reconstructs an exact reverse-transfer norm `R_n` and the principal normalization `N_n` with

$$
\boxed{
J_n=\frac BgR_n=\frac gBN_n.
}
$$

Hence all three sequences have the same exponential growth rate

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}.
$$

`(J-SPEC)` remains mathematically open:

$$
\rho_J>1\text{ at a strict residual point}
\quad\text{versus}\quad
\rho_J<1\text{ on a genuine residual region}.
$$

No active task is assigned to it.

## G009 fixed-depth singular renewal theorem

Along the strict residual scaling

$$
a=\varepsilon,
\qquad b=\frac1{10},
\qquad 1-c=\frac\varepsilon{10},
\qquad 0<\varepsilon<\frac1{10},
$$

which contains

$$
P_*=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right),
$$

G009 proves that for every fixed depth `n`, with

$$
I_n(\varepsilon)
=\int_{(0,\infty)^{n-1}}
\left(\prod_{j=1}^{n-1}w(u_j)\right)|A_n(u)|du,
$$

one has

$$
\boxed{
\lim_{\varepsilon\downarrow0}
\frac{I_n(\varepsilon)}{|m_0(\varepsilon)|}
=
\left(\frac{499}{341}\right)^{n-1},
}
$$

and therefore

$$
\boxed{
\lim_{\varepsilon\downarrow0}J_n(\varepsilon)
=
\frac{2079}{341}
\left(\frac{499}{341}\right)^{n-1}.
}
$$

The base splits exactly as

$$
\frac{499}{341}
=
\underbrace{\frac{10}{11}}_{\text{short East Green channel}}
+
\underbrace{\frac{189}{341}}_{\text{long regenerated-mass channel}}
>1.
$$

The short channel has the all-depth East identity

$$
\ell_{m-1}E_m(-L_m^E)^{-1}
=\frac{10}{11}\ell_m.
$$

The long channel is only a fixed-volume invariant reset. Making it repeat at fixed `epsilon` uniformly in depth requires the same spatial reset/tail-shift control isolated by F014. Therefore the fixed-depth supercritical limit does **not** imply `rho_J(P_*)>1`.

G009 also proves that invertible suffix-compatible factorized duration resolvents cannot possess a nonzero exact finite-cylinder reproduction cycle. This rules out that finite-memory Perron--Frobenius implementation, not `(J+)` itself.

## Recurrent zero-frequency spatial-memory bottleneck

The same all-depth spatial reset/tail-shift information has now appeared independently from:

1. F013's unsplit two-insertion invariant spectral projection;
2. F014's short-time light-cone screening normal form;
3. G009's attempt to repeat the long regenerated renewal channel uniformly in depth.

This convergence of obstructions is the main reason no further representation-level variant is active.

## Stationary occupation-control hierarchy retained as exact mathematics

In complemented spins, let `L_N^u` be the `N`-site generator with right-boundary control `u in {0,1}` and define

$$
\mathcal K_N
=\left\{
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

F015 proves

$$
D_M=D_N-\inf_{K_M}m(s_N^+)-\inf_{K_M}m(s_N^-),
$$

where

$$
s_F(x,u)=w_F(x)1_{\{u\ne\pi_F(x)\}}.
$$

There is a controller-uniform **unweighted** mismatch theorem, but no theorem controlling the Bellman weight. Additive independently constructed block correctors give no strict improvement by a maximum principle. Any future stationary screening theorem therefore needs genuinely new joint cross-block control of adaptive weighted feedback.

## Current decision

The positive-rates conjecture remains the fixed scientific target, but there is presently **no identified proof architecture that justifies another substantial internal block**.

Do not activate by default:

- larger-depth `(J-SPEC)` numerics or another fixed-memory `J` certificate;
- one-/two-step tail-shift as a bare target;
- `(ML)`, `(JT)`, or `(MR)` merely from sampled signed-resolvent cancellation;
- generic trajectory exactness / `g`-measure variation / `bar d` / Hellinger searches;
- generic joint Bellman-corrector searches or larger controlled LPs;
- alternative common-uniform coupling/norm variants.

Work should resume only after genuinely new principal, external, or literature input supplies a concrete rate-level mechanism that is not a restatement of the stopped zero-frequency/spatial-reset, occupation, trajectory-contraction, or Bellman-weight problems.

## Unresolved target-level facts

Open:

- `(J-SPEC)`;
- one- and two-step tail-shift agreement off the product surface;
- `Gamma_M->0` and general `J_{x,r}->0`;
- common-uniform extinction versus convective survival;
- weak ergodicity of the reachable trajectory kernel `Q`;
- stationary diameter collapse `D_N(h)->0`;
- full ergodicity in the residual chamber.

On the exact surface `a=b(1-c)`, the zero-boundary invariant law is Bernoulli product and the signed insertion obstruction vanishes.

## Anti-circularity

Do not interchange the fixed-depth `epsilon->0` limit with the fixed-rate `n->infinity` limit; infer asymptotic `J` growth from finite depths; revive tail-shift as a renamed long-reset theorem; treat shrinking finite `D_N` values as multiscale screening; invoke hard-East relaxation as if it controlled adaptive state-dependent feedback; revive stopped coupling/profile architectures; or treat static uniqueness as full convergence.

## Wiki

Keep the live wiki frozen during research.
