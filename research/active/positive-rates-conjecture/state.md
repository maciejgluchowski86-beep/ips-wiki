# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** The Professor may close or redirect proof routes but does not pivot to another scientific problem.

Target:

> Every simple one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

Write

$$
r_{xy}=P_0(1\mid xy).
$$

Positive rates are

$$
r_{11}<1,\qquad r_{10}<1,\qquad r_{01}>0,\qquad r_{00}>0.
$$

On the normalized face `r11=0`, put

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

The source-corrected unresolved chamber is

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

Latest meeting: `meetings/001-density-estimates-and-regional-kernel.md`, `state_narrowed: yes`.

Active students:

- Student F, next assignment `students/student-f/assignment-002.md`;
- Student G, next assignment `students/student-g/assignment-002.md`.

## What the first research block established

Student F reconstructed the principal's last-successful-interaction route far enough to replace the vague "high density" premise by an exact signed insertion problem.

In the complemented canonical spin convention, set

$$
B=b+c-a,\qquad \rho=\frac cB.
$$

If a successful rightward dual interaction is revealed but its source-retaining/source-removing type is kept hidden, the signed type average is

$$
B\eta_i-c=B(\eta_i-\rho).
$$

After deleting the environment-independent rate-`a` noise, the resulting process `L^-` obeys the Professor-checked conditional lower bound

$$
\mathbb P^-\!\left(\eta_i(t)=1\mid\mathcal F^+_{i,t}\right)
\ge
q(t)=\frac{1-e^{-(1-c)t}}{1+b-a}
$$

uniformly over initial configurations and complete graphical histories strictly to the right. Since

$$
T_\rho=
\frac1{1-c}\log\frac{B}{(b-a)(1-c)}
$$

satisfies `q(t)>=rho` for `t>=T_rho`, every nonnegative right-history-measurable `F` satisfies

$$
\mathbb E^-[(B\eta_i(t)-c)F]\ge0.
$$

The density/sign part of the remembered route is therefore an actual finite-time estimate; it is not the present blocker.

F also established two route limitations:

- the raw Duhamel gradient is not right-measurable; already for `f(eta)=eta_{i-1}` it depends on the left spin at first order;
- on `a>b(1-c)`, sufficiently long OI patches of the original process have negative contribution, so patchwise absolute-value/positivity arguments cannot close the hard subregion.

Student G independently proved transient estimates on the **original** normalized IPS. With

$$
k=1+b+c,\qquad A=b+c-a,
$$

the exact one-density identity is

$$
\frac d{dt}m_i
=(b+c)-km_i-Aq_i+c(m_i-m_{i+1}),
$$

where `q_i=P(00)`. Summing over an interval telescopes the transport term and yields, uniformly over initial state and prescribed right-boundary history,

$$
\frac1L\sum_{i\in I}\mathbb P(\eta_i(t)=0)
\ge
\frac{1-e^{-kt}}{k}\left(1-\frac cL\right).
$$

One-sided finite propagation gives a Poisson-tail boundary error and hence an explicit finite-box high-probability version. G also proved

$$
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11),
$$

so near `b=0`, after time `log(1/b)/(1+b)`, every box of length `o(1/b)` is in the no-adjacent-`11` hard-core subshift with probability `1-o(1)`.

These are genuine original-dynamics estimates and do not assume an invariant law or convergence.

## The two density results do not yet compose

Meeting 001 checked this explicitly.

F needs a conditional/weighted insertion inequality for `L^-`; G gives unweighted spatial density information for `L`. Even ignoring that semigroup and conditioning mismatch, G's asymptotic guaranteed zero-density floor

$$
\theta_G=\frac1{1+b+c}
$$

is strictly below F's threshold

$$
\rho=\frac c{b+c-a}
$$

throughout `R`, because

$$
c(1+b+c)-(b+c-a)=a+c^2-b(1-c)>0.
$$

Likewise the hard-core guarantee of one-half zeros is below `rho`, since `b-a<c` implies `b+c-a<2c`.

Therefore the next block is **not** "combine the density bounds". The missing mathematics is regional cancellation/weighted insertion.

## Current bottleneck: regional insertion positivity

After revealing the minimal last-exit/scaffold geometry around a hidden successful interaction, keeping its type hidden, and integrating all unrevealed marks in the adjacent regions, determine whether the resulting companion kernel `F` satisfies

$$
\mathbb E^-[\eta_iF]\ge\rho\,\mathbb E^-[F]
$$

after the required burn-in.

Right-history measurability is sufficient but not necessary. A coarser regional cancellation proving the inequality directly would suffice.

This is a finite-region question. The first nontrivial cell must be proved or falsified before any larger scaffold argument. If one-cell positivity holds, it must immediately be tested under two-cell composition.

## Closed route retained as negative knowledge

The fixed finite agreed-block / frozen-exterior wall route remains closed. Do not restart it by increasing block length or changing the one-attack statistic.

The new regional-kernel question is different: it concerns cancellation after hidden interaction types are averaged, not adversarial repeated crossing of a fixed wall.

## Anti-circularity rule

A substantial block counts only if it proves a new one-way implication, new target-relevant estimate, material obstruction, or finite/local reduction with quantitative error. New dual/profile/finite-box language without a new inequality does not count.

The next meeting must rule on the actual regional kernel or on a genuinely stronger replacement mechanism.

## Wiki

Keep the live wiki frozen during research.
