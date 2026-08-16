# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed by the principal until the principal changes or stops it: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/008-restart-tail-and-empty-supnorm-region.md`, `state_narrowed: yes`.
- Student F: `students/student-f/assignment-008.md`, bounded-height signed mass/disagreement kernel, conditional on the global Foster lift.
- Student G: `students/student-g/assignment-004.md`, rigorous global restart-corrector Foster lift.

On the normalized face `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the residual chamber remains

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

The frozen-exterior finite-wall route, cellwise nonnegative scaffold-transfer route, and Meeting 005 one-step centered-transfer norm `(T)` are closed.

### Active predecessor-trail reduction

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The canonical centered predecessor trail remains the active reduction. The nonempty-exit term is controlled by the right-weighted invariant quantity

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du,
$$

where `w(u)=e^{-omega u}s_1(u)` includes segmentwise right survival. Showing `J_{x,r}->0` with depth is sufficient for that term. The full Poisson-Mecke factorization and the no-exit complement still require independent audit before a closing proof.

Student F Assignment 007 corrects an earlier claim about the crude scalar criterion. With

$$
Z=\int_0^\infty w(u)du
=\frac{a+b+2}{2ab+3a-bc+b-2c+2},
$$

one has throughout the residual chamber

$$
c>b-a
\qquad\text{and}\qquad
\boxed{cZ>1}.
$$

Hence `max{c,b-a}Z<1` has **no residual solutions**. Meeting 006's statement that it already proves a residual subregion is corrected.

### Mass/disagreement block mechanism

Each centered insertion splits exactly as

$$
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).
$$

The first term is signed mass; the second is a positive conditional-law disagreement channel. Near East the equilibrium right-weighted mass multiplier tends to `2/5`, whereas crude one-step absolute values expand (`3/2` and `7/5`).

### Student G same-parent restart theorem

Meeting 007 gives a uniform single-exposure child probability `h_1<1`. Student G Assignment 003 proves that if `N` counts exposure entries of one fixed parent disagreement before that same parent first coalesces, then

$$
\boxed{P(N\ge n\mid\mathcal F)\le h_1^{n-1}.}
$$

Thus for `1<=s<h_1^{-1}`,

$$
\boxed{E[s^N\mid\mathcal F]\le\frac{(1-h_1)s}{1-h_1s}.}
$$

This is Professor-checked. It removes arbitrary same-parent re-entry as an uncontrolled variable.

The stack-clearing height algebra also gives a candidate near-East restart/height factor tending to

$$
\frac{16}{21}<1.
$$

This is **not** a multiplier for global `J_{x,r}` and does not conflict with `cZ>1`.

### Remaining two lemmas

1. **Global restart-corrector Foster lift.** G's report proposes a product corrector over all unresolved levels, but the global phase bookkeeping is not yet Professor-verified. Inactive/exposed/child-alive phases and later new-parent reinfections must be represented explicitly and checked transition by transition.
2. **Bounded-height signed kernel.** Conditional on the Foster reduction to finitely many heights/phases, F must prove that the finite right-weighted signed mass/disagreement kernel has block spectral radius `<1`, or give an exact obstruction.

If both succeed, combine them to prove `J_{x,r}->0`; only then reconstruct the full trail/no-exit convergence argument.

## Most recently completed programme: random-regular voter discordance concentration

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard.

## Wiki freeze

The live wiki remains frozen during active research.
