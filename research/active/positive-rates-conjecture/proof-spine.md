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

The older fixed finite-wall / frozen-exterior route remains closed.

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

After the explicit burn-in `T_rho`, this makes the hidden insertion nonnegative against nonnegative right-history-measurable companions.

**Status:** Professor-checked reusable lemma. It does not close by cellwise scaffold iteration because E5 fails.

## E2. Direct transient information on the original dynamics

Student G Assignment 001, Professor-checked at Meeting 001, gives

$$
\boxed{
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
}
$$

where `q_i=P(00)`.

Summing over intervals telescopes the transport term and yields a boundary-uniform transient zero-density lower bound, with a finite-box high-probability version from one-sided propagation.

Also

$$
\boxed{
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11).
}
$$

Hence near `b=0`, after time `log(1/b)/(1+b)`, boxes of length `o(1/b)` are in the no-adjacent-`11` sector with probability `1-o(1)`.

**Status:** Professor-checked direct dynamical input.

## E3. Naive density/insertion composition fails

The direct zero-density floor is strictly below the hidden insertion threshold `rho` throughout `R`, and the hard-core half-zero guarantee is also below `rho`. The two statements also concern different semigroups / conditioning.

**Status:** checked obstruction. Do not create a proof edge merely by calling the density estimates compatible.

## E4. One-cell regional insertion works

Fix a predecessor interaction source-retaining. Regional integration gives the positive zero-boundary `L^-` kernel

$$
\boxed{
K_\Delta(z)
=
\frac1{1+b-a}
+
\left(z-\frac1{1+b-a}\right)e^{-(1+b-a)\Delta}.
}
$$

This removes the raw Duhamel left-spin obstruction on one cell.

**Status:** Professor-checked reusable local fact.

## E5. Cellwise scaffold composition fails

When the predecessor interaction is itself hidden, the exact transfer is

$$
\boxed{
\Psi_\Delta(z)=(b+c-a)K_\Delta(z)-c.
}
$$

At `z=0`, every residual parameter point has `Psi_Delta(0)<0` for all sufficiently short positive `Delta`. Consecutive scaffold gaps have no positive lower bound.

**Status:** Professor-checked route obstruction. The cellwise last-exit/scaffold positivity mechanism is closed. A coarser random-cluster cancellation would require genuinely new mathematics and is not an automatic continuation.

## E6. Rightmost live-source contraction under the true coupling

Student F Assignment 003 replaces the frozen-source picture by the actual common-uniform coupling.

Suppose `j` is a rightmost disagreement, the half-line strictly right of `j` is coupled, and `j-1` is still agreed. Let `tau` be death of the source at `j` and `sigma` creation of the first child at `j-1`. Put

$$
d=b-a>0,
\qquad
q=1-c+a>0,
$$

and

$$
D=(b+q)(1+q)-a(1-c)>0.
$$

Conditional on any actual common right-hand history, source death has intensity at least `q`. Before the first child, the agreed left spin is a two-state chain: from zero, child rate `d` and common transition `0->1` rate `a`; from one, child rate `c` and common transition `1->0` rate `1-c`.

Solving the killed chain gives

$$
\boxed{
\mathbb P(\sigma<\tau\mid\mathcal F)
\le1-\delta,
\qquad
\delta=\frac{q(d+2q)}D>0.
}
$$

The stronger gap when the agreed left spin is zero is

$$
1-h_0=\frac{q(a+q+1)}D.
$$

There is also a finite-slab regeneration bound

$$
\boxed{
\mathbb P(\tau<\sigma,\ \tau\le T\mid\mathcal F)
\ge
\frac{1-c+a}{1+a}(1-e^{-(1+a)T})>0.
}
$$

**Status:** Professor-checked target-relevant live-source contraction. This is genuinely different from the frozen-wall statistic because the source evolves and may die.

The estimate is not yet spatially iterable: once the first child exists, it is not rightmost and may die and be reinfected while the parent remains alive.

## E7. Coupling drift and the correct environmental badness variable

For

$$
D_i=1_{\{X_i\ne Y_i\}},
$$

and

$$
J_i=1_{\{D_i=0,\ D_{i+1}=1,\ X_i=Y_i=1\}},
$$

a complete local case split gives

$$
\boxed{
\mathcal L^{\rm coup}D_i
\le
-qD_i+dD_{i+1}+(c-d)J_i.
}
$$

`J_i=1` forces an adjacent `11` in exactly one copy, but substituting the marginal `11` estimate from E2 creates an additive error independent of disagreement density. Thus the next useful density input would have to control `J_i` conditionally / weighted by disagreement, not merely control `P(11)`.

**Status:** Professor-checked bridge and obstruction to the present marginal-density closure.

## E8. East-boundary scaling of the one-source estimate

Along the genuine residual path

$$
a=\varepsilon^2,
\qquad
b=\varepsilon,
\qquad
c=1-\varepsilon^2,
$$

one has

$$
d\sim\varepsilon,
\qquad
q=2\varepsilon^2,
\qquad
\delta\sim2\varepsilon^2\to0.
$$

Even from an all-zero / no-`11` local environment, a first-child event can beat the simplest competing local changes with probability

$$
\frac{1-\varepsilon}{1+3\varepsilon}\to1.
$$

**Ruling:** zero-rich / hard-core snapshots cannot yield a residual-uniform first-generation childless gap. This does not kill the pointwise positive-rate programme: `c=1` is outside the target, and post-birth child killing/reinfection dynamics is not represented in the one-source statistic.

## E9. Current load-bearing edge: two-generation episode with reinfection

After the first child at `j-1` is born, retain the true parent at `j` and include every child death and reinfection cycle until either:

- a grandchild disagreement is created at `j-2`; or
- both `j` and `j-1` become coupled, after which the half-line from `j-1` rightward is permanently coupled.

The desired finite statement is a parameter-point contraction

$$
\boxed{
\mathbb P(\sigma_2<\tau_2)\le1-\delta_2(a,b,c),
\qquad \delta_2>0,
}
$$

or an exact obstruction showing this is false in the relevant restart states.

A favorable two-generation number is not enough. Any positive result must identify a restart state or finite family of episode states that can plausibly compose spatially. The near-East asymptotic must be computed explicitly, but degeneration of constants at the excluded boundary is not itself failure.

Student F is attacking E9 in `students/student-f/assignment-004.md`. Student G is still completing its independent Assignment 002 and will be folded into the next meeting.

## Anti-circularity checkpoint

Meeting 003 proves a new live-source estimate and narrows the remaining difficulty from one source to a specific reinfecting parent-child episode. The next accepted spine change must control that two-generation episode or falsify it. Another first-child probability, marginal density estimate, frozen-source statistic, or representation without a hitting/drift conclusion is not progress.

## Current direction

Attack E9 while preserving the fixed positive-rates target.
