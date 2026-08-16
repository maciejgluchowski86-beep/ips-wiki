# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed by the principal until the principal changes or stops it: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/002-cellwise-insertion-composition-fails.md`, `state_narrowed: yes`.
- Student F is on `students/student-f/assignment-003.md`, attacking live disagreement/regeneration under the true dynamics.
- Student G is still finishing `students/student-g/assignment-002.md`; its return will be folded into the next meeting.

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

The older fixed-finite-wall / frozen-exterior route remains closed.

### Reusable estimates

Student F established and the Professor checked the hidden successful-type factor

$$
B\eta_i-c,
\qquad
B=b+c-a,
\qquad
\rho=\frac cB,
$$

and the noise-reduced conditional estimate

$$
\mathbb P^-\!\left(\eta_i(t)=1\mid\mathcal F^+_{i,t}\right)
\ge
\frac{1-e^{-(1-c)t}}{1+b-a}.
$$

After

$$
T_\rho=
\frac1{1-c}\log\frac{b+c-a}{(b-a)(1-c)},
$$

this is at least `rho`, yielding nonnegative insertion against nonnegative right-history-measurable companions.

Student G independently proved on the original dynamics the transport--dissipation identity

$$
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
$$

plus a boundary-uniform transient zero-density estimate, a finite-box concentration version, and

$$
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11),
$$

which yields a mesoscopic no-adjacent-`11` regime near the East boundary.

### Meeting 002: cellwise scaffold route closes

Student F's Assignment 002 resolves the composition test pre-specified at Meeting 001.

With a predecessor interaction fixed source-retaining, the left regional factor is the positive zero-boundary `L^-` kernel

$$
K_\Delta(z)
=
\frac1{1+b-a}
+
\left(z-\frac1{1+b-a}\right)e^{-(1+b-a)\Delta}.
$$

Thus one-cell regional integration really removes the raw Duhamel left dependence.

But when the predecessor interaction is itself hidden for composition, the exact signed transfer is

$$
\boxed{
\Psi_\Delta(z)=(b+c-a)K_\Delta(z)-c.
}
$$

For `z=0`, every residual parameter point has

$$
\Psi_\Delta(0)<0
$$

throughout

$$
0<\Delta<
\frac1{1+b-a}
\log\frac{b+c-a}{(b-a)(1-c)}.
$$

Consecutive predecessor time gaps have no positive lower bound. Therefore nonnegative regional insertion cannot be propagated cell by cell along the last-exit scaffold.

**Closed mechanism:** reveal scaffold geometry, hide each successful type, integrate one adjacent cell, and iterate a nonnegative insertion-preserving transfer cell by cell. The failure occurs already at two-cell composition and throughout the residual chamber.

The old scaffold algebra, one-cell kernel, insertion lemma, and deleted-noise trail factor remain valid technical mathematics, but they no longer form a closing proof spine. A hypothetical coarser random-cluster cancellation would be a genuinely new mechanism, not the automatic next step.

### Current proof direction

Move to an **actual live disagreement/regeneration episode** under the canonical coupling. The exterior source must evolve and be allowed to die, unlike the frozen-wall route; no sign is demanded separately for every successful-interaction cell, unlike the closed scaffold route.

The next accepted progress must be a quantitative contraction/regeneration estimate for the true coupled dynamics, or a concrete obstruction showing why the existing transient density/no-`11` estimates cannot provide one. A new disagreement representation without such an estimate does not count.

## Most recently completed programme: random-regular voter discordance concentration

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard; the project factor-`2` variance bound and quotient-genealogy proof remain verified technical mathematics.

## Wiki freeze

The live wiki remains frozen during active research.
