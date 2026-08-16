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

The previous fixed-wall programme closed only the fixed finite agreed-block / frozen-exterior route. No block-length escalation is allowed.

## E1. Exact hidden-interaction algebra

Student F's first report, Professor-checked at Meeting 001, identifies the exact sign in the principal's remembered last-exit construction.

In complemented canonical spins let

$$
B=b+c-a,\qquad \rho=\frac cB.
$$

At a successful rightward dual interaction, the source-retaining type has coefficient `+B` and the source-removing type has coefficient `-c`. If location and time are revealed but type is hidden, their signed average is

$$
\boxed{B\eta_i-c=B(\eta_i-\rho).}
$$

The old barrier--scaffold note had a local generator derivation typo: the diagonal `-c_{11}H(A)` term was omitted in one displayed line, although the later Feynman--Kac potential was already corrected. Meeting 001 verified the corrected algebra.

**Status:** established intermediate algebra.

## E2. Noise-reduced conditional insertion estimate

Delete the environment-independent rate-`a` noise, obtaining `L^-`. Conditional on the complete graphical history strictly to the right of site `i`, the canonical spin at `i` is a two-state time-inhomogeneous chain. Uniformly over initial configurations,

$$
\boxed{
\mathbb P^-\!\left(\eta_i(t)=1\mid\mathcal F^+_{i,t}\right)
\ge q(t)=\frac{1-e^{-(1-c)t}}{1+b-a}.
}
$$

Since

$$
T_\rho=
\frac1{1-c}\log\frac{B}{(b-a)(1-c)}
$$

satisfies `q(t)>=rho` for `t>=T_rho`, one obtains

$$
\boxed{
F\ge0,\ F\text{ right-history measurable}
\Longrightarrow
\mathbb E^-[(B\eta_i(t)-c)F]\ge0
}
$$

for `t>=T_rho`.

This is a finite-time estimate independent of ergodicity or invariant laws. The previously vague high-density sign is therefore no longer an unproved density hypothesis.

**Status:** Professor-checked target-relevant lemma; no independent audit yet because it is intermediate rather than a promoted central claim.

## E3. Original-dynamics finite-box density estimates

Student G independently derived actual transient information for the original normalized IPS.

With

$$
m_i=\mathbb E\eta_i,\qquad q_i=\mathbb P(00),
\qquad k=1+b+c,\qquad A=b+c-a,
$$

one has the exact transport--dissipation identity

$$
\boxed{
\frac d{dt}m_i
=(b+c)-km_i-Aq_i+c(m_i-m_{i+1}).
}
$$

Summing over an interval telescopes the transport term and gives

$$
\boxed{
\frac1L\sum_{i\in I}\mathbb P(\eta_i(t)=0)
\ge
\frac{1-e^{-kt}}{k}\left(1-\frac cL\right)
}
$$

uniformly over initial states and prescribed right-boundary histories.

One-sided graphical propagation gives boundary error

$$
H_R(t)=\mathbb P(\operatorname{Pois}(t)\ge R),
$$

which yields a high-probability finite-box version by residue-class independence after truncation.

For adjacent ones,

$$
\boxed{
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11).
}
$$

Hence at time `log(1/b)/(1+b)`, boxes of length `o(1/b)` contain no adjacent `11` pair with probability `1-o(1)` as `b->0`.

**Status:** Professor-checked target-relevant transient estimates; they do not by themselves imply ergodicity.

## E4. Non-composition of the present density bounds

The F and G estimates concern the same physical density after translating conventions, but they do not presently compose.

F's sign condition is a **conditional weighted insertion statement for `L^-`**. G's bounds are **unweighted spatial-density statements for the original process `L`**.

Even if one ignores this structural mismatch, G's asymptotic guaranteed zero-density floor

$$
\theta_G=\frac1{1+b+c}
$$

is strictly below the hidden-type threshold

$$
\rho=\frac c{b+c-a}
$$

throughout `R`. Indeed

$$
c(1+b+c)-(b+c-a)
=a+c^2-b(1-c)>0.
$$

Also `rho>1/2`, since `b-a<c`, so the mesoscopic hard-core guarantee of at least one-half zeros is not enough either.

**Status:** checked obstruction to the naive composition "density estimate + hidden interaction sign".

## E5. Raw Duhamel and patchwise positivity are insufficient

The exact comparison generators satisfy

$$
L^+=L^-+2cC,
$$

so

$$
U^-_{s,t}-U^+_{s,t}
=-2c\int_s^t U^-_{s,u}C_uU^+_{u,t}\,du.
$$

However, for `f(eta)=eta_{i-1}`,

$$
D_i(U_t^+f)=t(c+B\eta_{i-1})+O(t^2),
$$

so the raw companion factor depends on a left spin and E2 cannot simply be inserted.

Separately, long OI patches of the original process have limiting sign

$$
\frac{b(1-c)-a}{1+b}.
$$

Thus in the hard subregion

$$
a>b(1-c)
$$

patchwise positivity/absolute-value domination fails.

These are route exclusions, not failures of the coarser hidden-type scaffold cancellation.

## E6. Current load-bearing edge: regional insertion positivity

Take the **smallest nontrivial scaffold cell** containing a hidden successful interaction and a left predecessor branch. Reveal only the geometry/no-crossing data needed for the cell, keep the birth-versus-jump type hidden, and integrate all other marks with the corrected dynamic boundary rules.

Let `F` be the resulting companion kernel at the source. Determine whether, after the relevant burn-in,

$$
\boxed{
\mathbb E^-[\eta_iF]\ge\rho\,\mathbb E^-[F].
}
$$

Right-history measurability plus `F>=0` is sufficient, but not necessary. A coarser regional cancellation proving the displayed inequality directly is enough.

This is deliberately finite-dimensional and falsifiable.

- If the inequality fails on the minimal cell, the principal's old last-exit route is closed in its present form.
- If it holds on one cell, test two-cell composition immediately. One-cell positivity that does not iterate is not target progress.
- If two-cell composition works, the next edge is to iterate along the trail and combine it with the exact deleted-noise factor `e^{-a u}`.

Students F and G are both assigned to this composition-or-kill question with broad methodological freedom.

## Anti-circularity checkpoint

The previous bottleneck was a vague high-density premise. It has been replaced by E6, a finite regional inequality with an explicit threshold. That is genuine narrowing.

Do not add another proof-spine edge unless it proves a new estimate/obstruction or makes E6 strictly easier. Unweighted density improvements, new dual variables, or new finite-box language do not count without a demonstrated interface to E6 or to ergodicity.

## Current direction

Attack E6. Preserve the fixed positive-rates target.
