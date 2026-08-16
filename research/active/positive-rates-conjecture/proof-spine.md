# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

The scientific target is fixed by the principal. Proof routes may be abandoned; the target does not change.

## E0. Source reduction

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

The source-corrected unresolved chamber is

$$
\boxed{
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
}
$$

The older fixed finite-wall/frozen-exterior route remains closed.

## E1. Hidden-interaction algebra and conditional insertion lemma

In complemented canonical spins put

$$
B=b+c-a,\qquad \rho=\frac cB.
$$

A hidden successful rightward dual interaction has signed type average

$$
\boxed{B\eta_i-c=B(\eta_i-\rho).}
$$

For the noise-reduced process `L^-`, conditional on the full graphical history strictly to the right of `i`,

$$
\boxed{
\mathbb P^-\!\left(\eta_i(t)=1\mid\mathcal F^+_{i,t}\right)
\ge
\frac{1-e^{-(1-c)t}}{1+b-a}.
}
$$

Thus after

$$
T_\rho=
\frac1{1-c}\log\frac{B}{(b-a)(1-c)},
$$

nonnegative right-history-measurable companions satisfy

$$
\mathbb E^-[(B\eta_i(t)-c)F]\ge0.
$$

**Status:** Professor-checked reusable lemma. It no longer closes the proof by cellwise scaffold iteration because E5 below fails.

## E2. Direct transient information on the original dynamics

Student G's first report, Professor-checked at Meeting 001, gives

$$
\boxed{
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
}
$$

where `q_i=P(00)`.

Summing over an interval telescopes the spatial term and yields a boundary-uniform transient zero-density lower bound. One-sided graphical propagation gives an explicit finite-box concentration version.

For adjacent ones,

$$
\boxed{
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11).
}
$$

Hence near `b=0`, after time `log(1/b)/(1+b)`, boxes of length `o(1/b)` are in the no-adjacent-`11` hard-core sector with probability `1-o(1)`.

**Status:** Professor-checked target-relevant direct dynamics. This is currently the main positive input.

## E3. Naive composition of density with hidden insertion fails

The direct zero-density floor

$$
\frac1{1+b+c}
$$

is strictly below

$$
\rho=\frac c{b+c-a}
$$

throughout `R`, and the hard-core one-half-zero guarantee is also below `rho`. Moreover the direct density estimates concern `L`, whereas E1 is a weighted conditional statement for `L^-`.

Thus no proof edge may be created by merely saying that the two density statements are compatible.

## E4. One-cell regional insertion works

Student F Assignment 002 resolves the first half of Meeting 001's finite test.

Fix a predecessor interaction to be source-retaining. The left absence region is exactly a one-site zero-boundary `L^-` evolution. Writing `d=b-a`, its kernel is

$$
\boxed{
K_\Delta(z)
=
\frac1{1+d}
+
\left(z-\frac1{1+d}\right)e^{-(1+d)\Delta}.
}
$$

This factor is nonnegative and separates from the current source/right region. Hence after the E1 burn-in, the current hidden successful interaction has nonnegative one-cell contribution.

**Status:** Professor-checked. This shows regional integration really removes the raw Duhamel left-spin obstruction on one cell.

## E5. Two-cell composition fails: cellwise scaffold route closed

For actual composition, the predecessor interaction is itself hidden. Its source-retaining type contributes `+B K_Delta(z)`; its source-removing type contributes `-c`. Therefore the exact signed transfer between cells is

$$
\boxed{
\Psi_\Delta(z)=B K_\Delta(z)-c.
}
$$

At `z=0`,

$$
\Psi_\Delta(0)
=
\frac{B}{1+b-a}(1-e^{-(1+b-a)\Delta})-c.
$$

Since `Psi_0(0)=-c<0` and its long-time limit is

$$
\frac{(b-a)(1-c)}{1+b-a}>0,
$$

the sign changes at

$$
\boxed{
\tau_*
=
\frac1{1+b-a}
\log\frac{b+c-a}{(b-a)(1-c)}.
}
$$

Hence, for every residual parameter point,

$$
0<\Delta<\tau_*
\quad\Longrightarrow\quad
\Psi_\Delta(0)<0.
$$

Scaffold predecessor gaps can be arbitrarily short. Thus the mechanism

> hide each successful type, integrate one adjacent cell, obtain a nonnegative transfer, and iterate cell by cell

is false already at two-cell composition.

**Status:** Professor-checked route obstruction. The cellwise last-exit/scaffold positivity route is closed.

A hypothetical cancellation obtained only after summing random clusters of short cells would be a genuinely new mechanism. It is not an automatic continuation of E5.

## E6. Current load-bearing edge: live disagreement/regeneration under the true dynamics

The next route works directly with the canonical coupling and the actual lifetime of a disagreement source.

The source must evolve under the true coupled dynamics and be allowed to die. This avoids the frozen-exterior obstruction. No sign is required separately for every dual/scaffold cell, avoiding E5.

Target an actual finite-time statement such as:

- a contraction probability across a block/time slab before the source episode dies;
- a regeneration event with a quantitative lower bound;
- a Lyapunov drift for disagreement plus a local environmental badness variable;
- a state-dependent influence/branching estimate rendered subcritical by the true environment.

The direct zero-density and no-`11` estimates from E2 may be used, but a new disagreement representation without a contraction estimate is not progress.

Student F is attacking E6 in `students/student-f/assignment-003.md`. Student G is still completing the independent Assignment 002 and will be folded in when it returns.

## Anti-circularity checkpoint

Meeting 002 eliminates a concrete route rather than renaming its obstruction. Do not return immediately to larger/coarser scaffold cells. The next accepted spine edge must concern a quantitatively different object: a live disagreement episode or another direct dynamical mechanism.

## Current direction

Attack E6 while preserving the fixed positive-rates target.
