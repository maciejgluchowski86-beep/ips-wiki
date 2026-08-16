# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** The Professor may close or redirect proof routes but does not pivot to another scientific problem.

Target:

> Every simple one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with source-corrected residual chamber

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

Latest meeting: `meetings/003-live-source-contraction.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-004.md`, exact two-generation parent-child episode with reinfection;
- Student G: still finishing `students/student-g/assignment-002.md`; its independent return will be folded into the next meeting.

## Reusable mathematics from the earlier blocks

In complemented canonical spins set

$$
B=b+c-a,\qquad \rho=\frac cB.
$$

A hidden successful interaction has signed type average `B eta_i-c`. For the noise-reduced process `L^-`, uniformly over initial configurations and full right-hand histories,

$$
\mathbb P^-\!\left(\eta_i(t)=1\mid\mathcal F^+_{i,t}\right)
\ge
\frac{1-e^{-(1-c)t}}{1+b-a},
$$

so after the explicit burn-in `T_rho` the hidden insertion is nonnegative against nonnegative right-history-measurable companions.

Student G independently proved on the original dynamics the transport--dissipation identity

$$
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
$$

plus a boundary-uniform transient zero-density bound, a finite-box high-probability version, and

$$
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11).
$$

These remain direct dynamical inputs.

## Closed route: cellwise last-exit/scaffold insertion

Meeting 002 established that one-cell regional integration is positive but two-cell composition is not. With

$$
K_\Delta(z)
=\frac1{1+b-a}
+\left(z-\frac1{1+b-a}\right)e^{-(1+b-a)\Delta},
$$

the hidden predecessor transfer is

$$
\Psi_\Delta(z)=(b+c-a)K_\Delta(z)-c.
$$

For `z=0`, `Psi_Delta(0)<0` on every sufficiently short positive cell at every residual parameter point. Hence the mechanism "hide each type, integrate one cell, iterate a nonnegative transfer" is closed. Do not revive it by increasing the number of cells without a genuinely new cluster-cancellation theorem.

The older frozen-exterior fixed-wall route remains closed as well.

## New established live-source estimate

Student F Assignment 003, Professor-checked at Meeting 003, works directly with the true common-uniform coupling.

Suppose `j` is a rightmost disagreement, the whole half-line strictly right of `j` is coupled, and `j-1` is still agreed. Let `tau` be source death at `j` and `sigma` creation of the first child disagreement at `j-1`. Put

$$
d=b-a,
\qquad
q=1-c+a,
$$

and

$$
D=(b+q)(1+q)-a(1-c).
$$

Conditional on any evolving common right-hand history, source death has intensity at least `q`. The agreed left spin is a two-state chain with child-creation rate `d` from zero and `c` from one. Solving the killed chain gives

$$
\boxed{
\mathbb P(\sigma<\tau\mid\mathcal F)
\le1-\delta,
\qquad
\delta=\frac{q(d+2q)}D>0.
}
$$

If the agreed left spin is zero, the stronger childless gap is

$$
1-h_0=\frac{q(a+q+1)}D.
$$

For every `T>0`, there is also the finite-slab regeneration event

$$
\boxed{
\mathbb P(\tau<\sigma,\ \tau\le T\mid\mathcal F)
\ge
\delta_T
=
\frac{1-c+a}{1+a}(1-e^{-(1+a)T})>0.
}
$$

This is a true live-source estimate: the exterior source runs on its actual clock and may die; the right environment evolves arbitrarily.

F also derived the coupling drift bridge

$$
\boxed{
\mathcal L^{\rm coup}D_i
\le
-qD_i+dD_{i+1}+(c-d)J_i,
}
$$

where `J_i` is the state in which the right site disagrees while the agreed left spin is one. Marginal `11` suppression controls `E J_i` only additively, so the current density estimates do not yet close this drift inequality.

## East-boundary diagnostic

Along

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

one has `d~epsilon` but `q=2 epsilon^2`, so

$$
\delta\sim2\varepsilon^2\to0.
$$

Even from an all-zero/no-`11` local environment, the first-transmission probability before the simplest competing local changes tends to one:

$$
\frac{1-\varepsilon}{1+3\varepsilon}\to1.
$$

Ruling: this kills any hope for a **residual-uniform first-generation** childless gap obtained merely from zero-rich/no-`11` snapshots. It does **not** close the live-episode route, because the theorem is pointwise on strict positive-rate parameters and the post-first-child dynamics includes fast killing mechanisms absent from the one-source estimate.

## Current bottleneck: two generations with reinfection

Once the first child at `j-1` is born, it is not rightmost. It may die while its parent remains alive and then be reinfected. Therefore the factor `1-delta` cannot be multiplied site by site.

The next finite question is the entire parent-child episode:

- `sigma_2`: creation of a grandchild disagreement at `j-2`;
- `tau_2`: elimination of both parent and child so that the half-line from `j-1` rightward is permanently coupled.

Student F must include all child-death / parent-reinfection cycles and determine whether

$$
\mathbb P(\sigma_2<\tau_2)\le1-\delta_2(a,b,c)
$$

with `delta_2>0`, or produce an exact obstruction. A positive two-generation number is not enough by itself: the restart state / finite renewal kernel needed for spatial composition must be identified immediately.

## Anti-circularity rule

The next accepted progress must control the two-generation live episode including reinfection, or falsify such control. Another first-child calculation, marginal density estimate, frozen-source statistic, or finite-state representation without a hitting/drift conclusion does not count.

## Wiki

Keep the live wiki frozen during research.
