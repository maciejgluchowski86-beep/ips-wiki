# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because the computation is exact, the witness is larger, or the constant is better. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed until changed or stopped by the principal: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/025-fixed-depth-j-renewal-is-supercritical-but-nonuniform-j-spec-stops.md`, `state_narrowed: yes`.
- Student G: idle; no G010.
- Student F: idle; no F016.
- No proof architecture is currently active.

On `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the residual chamber is

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

### Operative route status

Consultation 002's `RECOMMENDATION: no-credible-route` is again the operative **proof-architecture** assessment. Meetings 024--025 add exact structural information supporting that stop. This is not a claim that the conjecture is false or that all conceivable approaches are impossible.

Stopped/abandoned interfaces include:

- common-uniform global coalescence / zero-frequency disagreement occupation (Meeting 019);
- the current centered predecessor-trail/profile composition, which terminates at one-/two-step spatial tail memory (Meeting 021);
- global path-space contraction of the exact trajectory kernel `Q`, since
  $$
  Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot);
  $$
- the current stationary boundary-control Bellman-corrector concatenation implementation (Meeting 024);
- the internal `(J-SPEC)` route-decision branch (Meeting 025).

### G009: fixed-depth singular `J` renewal

For singleton depth `n`, G's exact normalization is

$$
J_n=\frac BgR_n=\frac gBN_n,
\qquad B=b+c-a,\quad g=b-a,
$$

so `R_n`, `J_n`, and `N_n` have the same exponential growth rate

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}.
$$

`(J-SPEC)` remains open: neither `rho_J>1` at a strict residual point nor `rho_J<1` on a genuine residual region has been proved.

Along

$$
a=\varepsilon,
\qquad b=\frac1{10},
\qquad 1-c=\frac\varepsilon{10},
$$

G009 proves for every fixed depth `n`

$$
\lim_{\varepsilon\downarrow0}
\frac{I_n(\varepsilon)}{|m_0(\varepsilon)|}
=
\left(\frac{499}{341}\right)^{n-1},
$$

hence

$$
\lim_{\varepsilon\downarrow0}J_n(\varepsilon)
=
\frac{2079}{341}
\left(\frac{499}{341}\right)^{n-1}.
$$

The supercritical fixed-depth base decomposes as

$$
\frac{499}{341}
=
\frac{10}{11}+\frac{189}{341}>1.
$$

The `10/11` short multiplier comes from an all-depth East Green extraction identity. The `189/341` long multiplier comes from a finite-volume regenerated-mass reset. Repeating that long channel uniformly at fixed positive `epsilon` requires the same all-depth spatial reset/tail-shift control isolated by F014. Therefore the singular fixed-depth theorem does **not** imply `rho_J>1`.

G also proves that invertible suffix-compatible factorized resolvents cannot possess a nonzero exact finite-cylinder reproduction cycle. This rules out that finite-memory Perron--Frobenius implementation, not `(J+)` itself.

### Recurrent zero-frequency bottleneck

The same all-depth spatial reset/tail-shift information has now appeared from three distinct reductions:

- F013's unsplit two-insertion invariant projection;
- F014's short-time light-cone normal form;
- G009's attempt to repeat the long regenerated renewal channel uniformly in depth.

No further local representation-level variant is authorized without genuinely new input.

### Stationary occupation-control hierarchy retained

Meetings 023--024 establish an exact nested occupation hierarchy `K_N` for one-time stationary marginals under arbitrary state-dependent right-boundary control. For local `h`,

$$
D_N(h)=\sup_{K_N}m(h)-\inf_{K_N}m(h)
$$

is nonincreasing, and `D_N(h)->0` for every local `h` would prove uniqueness of the invariant measure.

F015 proves the exact scale-extension formula

$$
D_M=D_N-\inf_{K_M}m(s_N^+)-\inf_{K_M}m(s_N^-),
$$

with Bellman slack

$$
s_F(x,u)=w_F(x)1_{\{u\ne\pi_F(x)\}}.
$$

A controller-uniform unweighted mismatch bound is available, but no theorem controls the Bellman weight. Additive independently constructed appended-block correctors cannot strictly improve the Bellman endpoints. Hence the present implementation is stopped; no larger controlled LP or generic joint-corrector search is active.

### Current decision

The positive-rates conjecture remains the scientific target, but **no presently identified proof architecture clears the continuation bar for another substantial internal block**.

Do not restart larger-depth `J` calculations, bare tail-shift, common-coupling occupation, generic trajectory-kernel exactness/metric searches, generic joint Bellman-corrector searches, or `(ML)/(JT)/(MR)` solely from the existing sampled signed-resolvent evidence.

Work resumes only after genuinely new principal, external, or literature input supplies a concrete rate-level mechanism that is not a restatement of the stopped bottlenecks.

## Most recently completed programme

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard.

## Wiki freeze

The live wiki remains frozen during active research.
