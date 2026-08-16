# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed by the principal until changed or stopped: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/010-exposed-product-refuted-and-16-phase-foster-reduction.md`, `state_narrowed: yes`.
- Student F: `students/student-f/assignment-009.md`, mode-resolved `L^1(w)` signed block operator.
- Student G: `students/student-g/assignment-005.md`, 16-phase all-height coupling Foster feasibility.

On the normalized face `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the unresolved residual chamber is

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

Closed mechanisms include fixed finite walls, cellwise nonnegative scaffold insertion, one-step centered `L^1` contraction, the crude scalar criterion `max{c,b-a}Z<1` on the residual chamber, and Student G Assignment 003's exposed-only global product Foster lift.

### Current trail reduction

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The centered predecessor-trail working reduction leaves the global right-weighted invariant target

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du,
$$

with `w(u)=e^{-omega u}s_1(u)`. Proving `J_{x,r}->0` with depth is sufficient for the nonempty-exit term. The exact Poisson--Mecke factorization and no-exit complement still require independent audit before a closing proof.

### Mass/disagreement mechanism

Each centered insertion splits exactly as

$$
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).
$$

Student G's same-parent geometric restart tail remains Professor-checked. The separate scalar height/restart stress factor can tend to `16/21<1` near East, but Meeting 010 proves that it does **not** lift to Assignment 003's global product corrector.

### Meeting 010: old global Foster product refuted

Student G Assignment 004, commit `4128cee` with verifier commits `bec4dda` and `4586833`, gives a reachable all-`01` disagreement stack for which the exposed-only product has exact tilted drift

$$
\boxed{
\frac{\mathscr L_sV}{V}
=(1-a)(s-1)
+(H-2)(1-a)(s e_0-1)
+\omega(\lambda^{-1}-1).
}
$$

For `s>1`, `lambda>1`, `e_0>=1`, the interior term grows positively with height, so the proposed product cannot be superharmonic uniformly in `H`. With the old near-East choices this drift tends to `(H-2)/7`.

The coupling-side replacement is an exact 16-edge-phase nearest-neighbour product/coboundary feasibility problem. Let `A={00,11,01,10}` and choose positive weights `q_{alpha beta}`. For the product `C_Q=prod q_{sigma_{i-1},sigma_i}`, each of the 64 triples has an exact local tilted drift `G_Q(alpha,beta,gamma)`. Uniform all-height interior control is equivalent to finding a phase potential `psi` with

$$
G_Q(\alpha,\beta,\gamma)
\le
\psi(\alpha,\beta)-\psi(\beta,\gamma)
$$

for all triples, equivalently no positive cycle on the associated 16-vertex de Bruijn graph. Full Foster contraction additionally requires finitely many boundary/height/insertion inequalities. Student G Assignment 005 attacks this exact finite feasibility problem.

### Student F: regenerated mass and duration modes

For the one-site zero-boundary equilibrium density

$$
r_0=\frac1{1+b},
$$

Student F proves, and the Professor checks,

$$
\boxed{|Br_0-c|Z<\frac23}
$$

throughout the strict residual chamber.

A mass branch carries a transient relaxation mode

$$
r(u)=r_0+(r-r_0)e^{-(1+b)u}.
$$

Near East,

$$
\frac g{|m_\varepsilon|}\left|\int w(u)A_{2,\varepsilon}(u)du\right|\to\frac35,
$$

but the quantity compatible with `J_{x,r}` is

$$
\boxed{
\frac g{|m_\varepsilon|}\int w(u)|A_{2,\varepsilon}(u)|du\to\frac75.
}
$$

Therefore duration cannot be integrated before the block absolute-value norm. Short static spin words also fail to close the invariant law. Student F Assignment 009 seeks the correct mode-resolved `L^1(w)` operator.

### Current proof target

Two interfaces remain:

1. **G:** prove or refute the 16-phase nearest-neighbour product/coboundary Foster inequalities, including boundary/height transitions;
2. **F:** prove or refute a mode-resolved `L^1(w)` signed block contraction retaining equilibrium mass, transient mass/reset modes, disagreement phases, and duration information until the norm.

If both close positively, combine them to prove `J_{x,r}->0`; only then reconstruct the full trail/no-exit convergence argument.

## Most recently completed programme

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard.

## Wiki freeze

The live wiki remains frozen during active research.
