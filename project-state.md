# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed by the principal until the principal changes or stops it: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/001-density-estimates-and-regional-kernel.md`, `state_narrowed: yes`.
- Active students: F and G, both routed to second assignments on the regional-insertion/composition bottleneck.

Write

$$
r_{xy}=P_0(1\mid xy).
$$

On the normalized face `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the source-corrected unresolved chamber remains

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

The earlier fixed-finite-wall route remains closed; no block-length escalation is allowed.

### First-block mathematical progress

Student F reconstructed the principal's remembered last-successful-interaction route far enough to identify the exact hidden-type sign. In complemented spins,

$$
B=b+c-a,\qquad \rho=\frac cB,
$$

and hiding the successful birth-versus-jump type gives the signed source factor

$$
B\eta_i-c=B(\eta_i-\rho).
$$

For the noise-reduced process `L^-`, F proved and the Professor checked the uniform conditional estimate

$$
\mathbb P^-\!\left(\eta_i(t)=1\mid\mathcal F^+_{i,t}\right)
\ge
\frac{1-e^{-(1-c)t}}{1+b-a}.
$$

After the explicit burn-in

$$
T_\rho=
\frac1{1-c}\log\frac{b+c-a}{(b-a)(1-c)},
$$

this is at least `rho`, so the hidden signed type is nonnegative against every nonnegative companion measurable from the right-hand history.

The raw Duhamel companion is not of that form: its first-order gradient already depends on a left spin. In addition, on `a>b(1-c)` long OI patches have negative averaged contribution, so patchwise absolute-value/positivity arguments cannot close the hard subregion.

Student G independently proved transient estimates for the **original** normalized IPS. The one-density satisfies

$$
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
$$

with `q_i=P(00)`. Summing over intervals telescopes the transport term and yields a boundary-uniform positive zero-density after `O(1)` burn-in, with an explicit high-probability finite-box version from one-sided Poisson-tail propagation. G also proved

$$
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11),
$$

which gives a mesoscopic no-adjacent-`11` regime near the East boundary.

These are genuine estimates, not invariant-measure or dual reformulations.

### Current bottleneck

The F and G density statements do **not** directly compose. F needs a conditional/weighted insertion inequality for `L^-`; G provides unweighted spatial density for `L`. Even numerically, throughout the residual chamber,

$$
\frac1{1+b+c}
<
\frac c{b+c-a},
$$

and the hard-core half-zero guarantee is also below `rho`.

The next load-bearing question is finite and falsifiable:

> After revealing the minimal scaffold geometry around one hidden successful interaction and a left predecessor branch, and integrating all unrevealed histories, does the resulting companion kernel satisfy
> $$
> \mathbb E^-[\eta_iF]\ge\rho\,\mathbb E^-[F]?
> $$

One-cell success must be tested under two-cell composition immediately. Failure on the minimal cell closes the old last-exit route in its present form.

Student F assignment: `research/active/positive-rates-conjecture/students/student-f/assignment-002.md`.

Student G assignment: `research/active/positive-rates-conjecture/students/student-g/assignment-002.md`.

### Anti-circularity instruction

Representations are not progress by themselves. The next meeting must resolve the regional kernel, eliminate that route, or produce a genuinely stronger estimate linked explicitly to ergodicity. Further unweighted density bounds without such an interface do not count as narrowing.

## Most recently completed programme: random-regular voter discordance concentration

`VOTER-CONC-001` is mathematically **verified** but **not a new project result under the standing novelty standard**. Avena--Baldasso--Hazra--den Hollander--Quattropani (2024) already contain an immediate factor-`4` variance-to-meeting corollary giving the same asymptotic concentration conclusions; the project factor `2` and quotient-genealogy proof are retained as verified technical mathematics.

## Superseded unstarted direction

`research/heterogeneous-voter-discordance` was initialized but shelved by principal direction before substantive student work.

## Earlier closed programmes/routes

Closed routes include the fixed finite-wall noisy-East route, the BABP finite-window programme, and the other closures recorded in Git history. The positive-rates conjecture itself is explicitly active despite the fixed-wall closure.

## Wiki freeze

The live wiki remains frozen during active research.
