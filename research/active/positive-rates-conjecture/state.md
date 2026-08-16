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

Latest meeting: `meetings/002-cellwise-insertion-composition-fails.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-003.md`, direct live-disagreement/regeneration attack;
- Student G: still finishing `students/student-g/assignment-002.md`; its independent return will be folded into the next meeting.

## Established reusable mathematics from the first two blocks

In complemented canonical spins set

$$
B=b+c-a,\qquad \rho=\frac cB.
$$

A hidden successful rightward dual interaction has signed type average

$$
B\eta_i-c=B(\eta_i-\rho).
$$

For the noise-reduced process `L^-`, uniformly over initial configurations and full right-hand graphical histories,

$$
\mathbb P^-\!\left(\eta_i(t)=1\mid\mathcal F^+_{i,t}\right)
\ge
\frac{1-e^{-(1-c)t}}{1+b-a}.
$$

After

$$
T_\rho=
\frac1{1-c}\log\frac{B}{(b-a)(1-c)},
$$

this yields nonnegative insertion against every nonnegative right-history-measurable companion.

Student G independently proved on the **original** normalized dynamics the exact transport--dissipation identity

$$
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
$$

and hence a boundary-uniform transient zero-density lower bound, a finite-box high-probability version via one-sided propagation, and

$$
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11),
$$

which gives a mesoscopic no-adjacent-`11` regime near the East boundary.

These remain target-relevant inputs.

## Closed route: cellwise last-exit/scaffold insertion

Meeting 002 resolves the finite question left by Meeting 001.

With a predecessor interaction fixed source-retaining, regional integration of the left absence cell gives the positive zero-boundary `L^-` kernel

$$
K_\Delta(z)
=
\frac1{1+b-a}
+
\left(z-\frac1{1+b-a}\right)e^{-(1+b-a)\Delta}.
$$

Thus the **one-cell** insertion step works: the raw Duhamel left dependence is removed by regional integration.

But under composition the predecessor interaction is itself hidden. The exact signed transfer becomes

$$
\boxed{
\Psi_\Delta(z)=(b+c-a)K_\Delta(z)-c.
}
$$

At `z=0`, for every residual parameter point,

$$
\Psi_\Delta(0)<0
$$

for all

$$
0<\Delta<
\tau_*:=
\frac1{1+b-a}
\log\frac{b+c-a}{(b-a)(1-c)}.
$$

Consecutive predecessor gaps have no positive lower bound. Hence nonnegative regional insertion does **not** propagate cell by cell along the scaffold. An explicit strict example is recorded in Student F's report and verifier.

The following mechanism is therefore closed:

> reveal scaffold geometry, hide each successful type, integrate its adjacent region, demand a nonnegative insertion-preserving transfer, and iterate those transfers cell by cell.

Do not continue by adding more cells to the same positivity argument. A hypothetical random-cluster cancellation would require a genuinely new mechanism and is not the automatic next route.

## What survives from the principal's old route

The corrected generator/boundary algebra, hidden-type insertion identity, right-conditioned `L^-` lemma, positive one-cell kernel, and deleted-noise trail factor remain correct technical mathematics. They no longer form a closing proof spine through cellwise composition.

## Current bottleneck: actual live disagreement episodes

The main positive inputs now come from the direct dynamics. The next route attacks the canonical coupling with the exterior disagreement source evolving according to the true process rather than being frozen.

The desired next gain is an episode-level contraction or regeneration estimate: a bound on the probability/lifetime of a disagreement source and its propagation through a block or time slab, potentially using the proved zero-density/no-`11` estimates.

This is distinct from both closed mechanisms:

- no permanently frozen exterior source;
- no sign required for every successful-interaction cell.

Student F is assigned to this direct problem now. Student G completes its already-running independent bridge attempt before being rerouted.

## Anti-circularity rule

A new disagreement representation does not count. The next block must prove a quantitative live-source contraction/regeneration estimate or exhibit a concrete obstruction showing why the existing density information cannot provide one.

## Wiki

Keep the live wiki frozen during research.
