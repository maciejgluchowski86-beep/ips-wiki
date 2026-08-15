# Professor verification: finite-window corrector to BABP finite-seed convergence

Date: 2026-08-15

Status: Professor-checked; the resulting convergence theorem is a new project claim and remains `claimed` pending independent hostile review.

Decisive student source: `students/student-b/002-edge-speed-to-convergence.md`.

## 1. Precise theorem boundary

The load-bearing hypothesis is not merely a ballistic edge conclusion. Fix `lambda>0` and assume there are `k>=1`, a bounded `phi:{0,1}^k -> R`, and `v>0` such that the exact right-edge corrector drift satisfies

$$
D_{k,\lambda}(u,z;\phi)\ge v
$$

for every edge word `u in {0,1}^k` and exterior bit `z in {0,1}`.

Call this hypothesis `(EC)`.

The claim checked here is:

> `(EC)` implies local convergence of one-dimensional BABP from every finite nonempty deterministic initial particle set to Bernoulli equilibrium of particle density `q=lambda/(1+lambda)`.

The proof uses the statewise corrector inequality on internal gaps. Bare statements about `liminf R_t/t` and `limsup L_t/t` are insufficient by themselves.

## 2. Gap genealogy

An internal gap is a maximal nonempty finite interval of vacant sites strictly between the outer particles.

A new internal gap is created only when a particle with both nearest neighbours occupied dies. Hence every nucleated gap is born with width one.

A positive gap cannot merge with another positive gap. If two gaps are separated by a block of particles, deaths at the two exposed ends may shorten that separating block. If only one separating particle remains, both of its nearest neighbours are vacant, so its death rate is zero. Thus the final separator cannot disappear while both gaps are positive. Interior births cannot split a gap because an interior vacant site has no occupied nearest neighbour. Therefore each positive gap has a well-defined genealogy from its birth until closure.

This point is correct and is essential for the later compensator sum over nucleations.

## 3. Corrected width of a tagged gap

Fix a tagged gap while alive. Let `A_t` be all particles to its left and `C_t` all particles to its right. Both remain finite and nonempty until closure. Put

$$
a_t=R(A_t),\qquad b_t=L(C_t),\qquad g_t=b_t-a_t-1\ge1.
$$

Before closure, the dynamics of the left and right populations agree with two standalone BABP systems at their inner edges. For `g_t>=2` no local transition sees particles on both sides. For `g_t=1`, the unique vacant site receives two birth contributions of rate `lambda`, one from each side; either event closes the tagged gap.

Let `H_R(A)=R(A)+phi(U_R(A))`. By `(EC)`,

$$
\mathcal L H_R(A)\ge v.
$$

By reflection, with `H_L(C)=L(C)-phi(U_L(C))`,

$$
\mathcal L H_L(C)\le -v.
$$

Hence for

$$
Z=H_L(C)-H_R(A)-1
=g-phi(U_L(C))-phi(U_R(A))
$$

the product generator before closure satisfies

$$
\mathcal L^{\times}Z\le-2v.
$$

At width one, replacing either closing transition by killing sends the exponential test function to zero rather than to a positive post-transition value. Thus killing only decreases the generator. There is no missing cross-gap event.

If `K=||phi||_infty`, then while alive

$$
g-2K\le Z\le g+2K.
$$

Only fixed neighbourhoods of the two inner edges change `Z`; jump sizes and the total rate of `Z`-changing events are uniformly bounded in the ambient finite particle configuration.

## 4. Exponential lifetime and width tails

Let `J` bound `|Delta Z|` and `rho` bound the rate of `Z`-changing events. For sufficiently small `theta>0`, Taylor's inequality gives

$$
\frac{\mathcal L^\dagger e^{\theta Z}}{e^{\theta Z}}
\le
\theta\mathcal L^\times Z
+\frac{\theta^2}{2}e^{\theta J}\rho J^2
\le -\gamma
$$

for some `gamma>0`, uniformly over every alive tagged-gap state.

Therefore a gap born with width one has uniform exponential lifetime tail

$$
P(\tau>t)\le C e^{-\gamma t}
$$

and uniform maximum-width tail

$$
P\left(\sup_{s<\tau}g_s\ge m\right)\le C e^{-\theta m}.
$$

The constants depend only on the corrector data, not on the surrounding finite configuration or the gap's birth location. For each deterministic initial gap, the same lifetime estimate holds with a finite prefactor depending on its initial width.

I find this exponential-tilting step correct.

## 5. Spatial displacement

Let `N_t` count inner-boundary shifts of a tagged gap before closure. Each boundary extends by one only when its bounding particle dies; because the gap-side neighbour is vacant, that death rate is at most one. Each boundary shrinks by a birth into the adjacent vacancy at rate `lambda`; at width one the two closing births contribute total rate `2 lambda`. Thus the predictable intensity of `N_t` is at most

$$
\beta=2(1+\lambda).
$$

Consequently `N_t` is stochastically dominated by a rate-`beta` Poisson process.

A gap born at the singleton `{x}` that contains the origin at age `r` must have undergone at least `|x|` boundary shifts. Combining lifetime, maximum-width, and displacement bounds gives, without any independence assumption,

$$
P(E_{m,r,x})
\le C e^{-c_1m}e^{-c_2r}
P(\operatorname{Pois}(\beta r)\ge|x|)^{1/3}.
$$

The sum over `x` is `O(1+r)`: terms up to a constant multiple of `r+1` are counted crudely, and the remaining Poisson tail is exponentially summable. This is sufficient for the nucleation sum.

## 6. Summation over gap nucleations

A post-time-zero internal gap is nucleated at `x` only when the particle at `x` dies with both neighbours occupied. The sitewise nucleation intensity is therefore at most two.

Because gap genealogies do not merge, the event that some post-time-zero gap of width at least `m` contains the origin at time `t` is bounded by the expected number of gap nucleations whose descendants have that property. The predictable compensator and the strong Markov property at a nucleation time give

$$
\begin{aligned}
P(G_m(t);\text{post-time-zero genealogy})
&\le
2\sum_{x\in\mathbb Z}\int_0^t
C e^{-c_1m}e^{-c_2(t-s)}
P(\operatorname{Pois}(\beta(t-s))\ge|x|)^{1/3}\,ds\\
&\le C'e^{-cm}.
\end{aligned}
$$

The infinite spatial sum is legitimate because the Poisson displacement weights are summable. No bound on the total particle number is used.

There are finitely many initial internal gaps for a finite initial seed. Their survival probabilities tend to zero exponentially, with initial-width-dependent prefactors. Hence

$$
\limsup_{t\to\infty}P(G_m(t))\le Ce^{-cm}.
$$

This is genuinely a uniform late-time bound in the required `limsup` sense; it is not merely a separate estimate for each tagged gap.

## 7. Nonescape

The same statewise corrector also gives the already verified ballistic bounds

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v,
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-v
\quad\text{a.s.}
$$

Thus for each fixed `M`,

$$
P(R_t\le M\text{ or }L_t\ge-M)\to0.
$$

If both outer edges lie beyond `[-M,M]` and the window contains no particle, that window lies inside an internal gap of width at least `2M+1`. Therefore

$$
\limsup_{t\to\infty}
P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

Consequently

$$
\lim_{M\to\infty}\limsup_{t\to\infty}
P_B(B_t\cap[-M,M]=\varnothing)=0.
$$

This is exactly the estimate required to rule out any positive empty-state component in a stationary subsequential limit.

## 8. External stationary-limit inputs

Student B left the theorem conditional on checking the generic Mountford / Ramirez--Varadhan subsequential-invariance hypothesis. I checked a cleaner current primary source.

Benedikt Jahnel and Jonas Koeppl, *Restriction and mixing properties of interacting particle systems with unbounded range*, arXiv:2603.21817 (2026), Theorem 2.5, proves in one dimension that every weak limit point of an IPS is stationary under assumptions `(L1)` and `(R1)--(R3)` with exponentially decaying influence.

BABP satisfies these hypotheses directly:

- the state space is finite, `{0,1}^Z`;
- updates are single-site, so the update diameter is uniformly bounded;
- each site flips at rate at most `2 max(1,lambda)`, giving `(L1)`;
- a flip rate depends only on the two nearest neighbours, so the influence kernel has finite range and therefore satisfies `(R3)` for every exponential profile.

Thus subsequential-limit invariance applies at `lambda=1/40` and in fact at every `lambda>0`; no positivity-of-rates assumption is needed here.

For stationary-law classification, Martinelli--Shapira--Toninelli, arXiv:2510.20461 (2025), Corollary 2.9, states explicitly that every stationary law of one-dimensional BABP is a convex combination of equilibrium and the completely healthy configuration. In particle variables this is

$$
\alpha\delta_\varnothing+(1-\alpha)\pi_q.
$$

Therefore the external inputs required by the gap proof do apply in the convention used here.

## 9. Convergence conclusion

The configuration space is compact. Let `t_n -> infinity` and take any weakly convergent subsequence of the laws, with limit `nu`. The one-dimensional stationary-limit theorem gives stationarity of `nu`, and the BABP classification gives

$$
\nu=\alpha\delta_\varnothing+(1-\alpha)\pi_q.
$$

For each `M`, the cylinder event of being empty on `[-M,M]` is clopen, and the nonescape estimate yields

$$
\nu(B\cap[-M,M]=\varnothing)\le Ce^{-cM}.
$$

The mixture formula gives the lower bound `>=alpha`. Sending `M -> infinity` yields `alpha=0`. Every subsequential limit is therefore `pi_q`, hence the full law converges locally to `pi_q`.

No particle-number growth theorem is used.

No assumption on the deterministic initial configuration is needed beyond being finite and nonempty. The proof can likely be extended to almost surely finite nonempty random initial configurations by conditioning, but that extension is not part of the present claim.

## 10. Concrete corollary and status

Verified claim `BABP-EDGE-001` supplies `(EC)` at

$$
\lambda=\frac1{40},\qquad k=10,\qquad
v=\frac{1033}{40000000}>0.
$$

Therefore the bridge proof yields local finite-seed convergence at `lambda=1/40`, strictly below the `0.0347` finite-seed range recorded in the 2025 progress paper.

I accept this as a **claimed** project theorem, not yet verified. It is substantially stronger than `BABP-EDGE-001`, so audit `d1ef2ca` does not verify it. Two fresh independent correctness reviews are requested before promotion.
