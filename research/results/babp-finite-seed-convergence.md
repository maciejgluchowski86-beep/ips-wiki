# BABP finite-seed convergence from a statewise edge corrector

Status: verified project theorem.

Claim registry: `BABP-CONV-001` and `BABP-EDGE-001` in `research/claim-registry.md`.

## Model

Use particle variables `xi(x) in {0,1}` and

$$
N_x(\xi)=\xi(x-1)+\xi(x+1).
$$

One-dimensional BABP has single-site rates

$$
0\to1\text{ at rate }\lambda N_x(\xi),
\qquad
1\to0\text{ at rate }N_x(\xi),
$$

with `lambda>0`. Its Bernoulli product equilibrium has particle density

$$
q=\frac{\lambda}{1+\lambda}.
$$

For a finite nonempty particle set `A`, write `R(A)=max A`. Fix `k>=1`, encode the first `k` sites behind the right edge by `u in {0,1}^k` and the next site by `z in {0,1}`, and let

$$
H_R(A)=R(A)+\phi(u(A)).
$$

The exact finite-window drift is denoted by `D_{k,lambda}(u,z;phi)` as in `BABP-EDGE-001`.

## Theorem

Assume there are `k>=1`, a bounded `phi:{0,1}^k -> R`, and `v>0` such that

$$
D_{k,\lambda}(u,z;\phi)\ge v
$$

for every `u in {0,1}^k` and `z in {0,1}`. Then for every finite nonempty deterministic initial particle set `B`,

$$
\operatorname{Law}_B(B_t)\Longrightarrow\pi_q
\qquad(t\to\infty)
$$

locally on `{0,1}^Z`.

The statewise corrector hypothesis is essential to the proof below. The theorem does not assert that bare outer-edge liminf/limsup velocity bounds alone imply convergence.

## Internal-gap contraction

An internal gap is a maximal nonempty finite interval of vacant sites strictly between the outer particles. A newly nucleated gap has width one: it is created by death of a particle whose two neighbours are occupied. A positive gap cannot split because a strictly interior vacancy has no occupied neighbour and cannot be filled. Two positive gaps cannot merge: if the separating particle block erodes to one particle, that particle has vacancies on both sides and therefore death rate zero. Thus every positive gap has a unique genealogy from nucleation until closure.

Fix a tagged gap while alive. Let `A_t` and `C_t` be the particle populations to its left and right, and write

$$
g_t=L(C_t)-R(A_t)-1\ge1.
$$

By reflection define

$$
H_L(C)=L(C)-\phi(U_L(C)).
$$

The statewise edge inequality gives

$$
\mathcal L H_R(A)\ge v,
\qquad
\mathcal L H_L(C)\le-v
$$

for every finite nonempty `A,C`. Set

$$
Z=H_L(C)-H_R(A)-1.
$$

For gap width at least two, no nearest-neighbour transition sees both populations, so the product generator satisfies

$$
\mathcal L^\times Z\le-2v.
$$

At width one, the sole vacancy fills at total rate `2lambda`, the sum of the two outward birth clocks. Either event closes the gap. Replacing these closure transitions by killing decreases the generator of every positive test function. If `K=||phi||_infty`, then while the gap is alive

$$
g-2K\le Z\le g+2K.
$$

Only fixed neighbourhoods of the two inner edges can change `Z`. Hence there are constants `J,rho<infinity`, depending only on `(k,lambda,phi)`, which uniformly bound the jump size and the rate of `Z`-changing events.

Choose `theta>0` small enough that

$$
-2v\theta+
\frac{\theta^2}{2}e^{\theta J}\rho J^2
\le-v\theta.
$$

Then for the killed tagged-gap generator,

$$
\mathcal L^\dagger e^{\theta Z}
\le-\gamma e^{\theta Z},
\qquad
\gamma=v\theta.
$$

This use of the unbounded exponential test is localized. Stop first when the gap width reaches `n` and, if desired, after the first `n` jumps. Dynkin's formula applies on the stopped state space. Let the jump-count cutoff and then `n` tend to infinity, using positivity and Fatou/monotone localization. Consequently a gap born at width one has uniform tails

$$
\mathbf P(\tau>t)\le C_0e^{-\gamma t}
$$

for its lifetime and

$$
\mathbf P\left(\sup_{s<\tau}g_s\ge m\right)
\le C_1e^{-\theta m}
$$

for its maximal width. The constants are independent of the surrounding finite configuration and the birth location.

## Displacement and the sum over nucleations

Let `N_t` count endpoint shifts of a tagged gap before closure. Each endpoint extends at rate at most one and shrinks at rate `lambda`, so

$$
N_t\preceq\operatorname{Pois}(2(1+\lambda)t).
$$

A gap born at `x` which contains the origin at age `r` must have at least `|x|` endpoint shifts. Combining displacement, lifetime, and maximal-width estimates gives

$$
\mathbf P(E_{m,r,x})
\le C e^{-c_1m}e^{-c_2r}
\mathbf P(\operatorname{Pois}(\beta r)\ge|x|)^{1/3},
\qquad
\beta=2(1+\lambda),
$$

where `E_{m,r,x}` is the event that the descendant gap is alive at age `r`, contains zero, and has width at least `m`. No independence is used. The Poisson tail satisfies

$$
\sum_{x\in\mathbb Z}
\mathbf P(\operatorname{Pois}(\beta r)\ge|x|)^{1/3}
\le C_\beta(1+r).
$$

A gap is nucleated at a fixed site at predictable rate at most two. For complete rigor, first sum only nucleations at sites `|x|<=N`. The strong Markov property at nucleation times and the preceding uniform estimate give

$$
2\sum_{|x|\le N}\int_0^t
C e^{-c_1m}e^{-c_2(t-s)}
\mathbf P(\operatorname{Pois}(\beta(t-s))\ge|x|)^{1/3}\,ds.
$$

The relevant events increase with `N`, so monotone convergence removes the spatial truncation. The spatial sum is `O(1+r)` and the lifetime factor is exponentially integrable. Therefore, if `G_m(t)` is the event that zero lies in an internal gap of width at least `m`,

$$
\limsup_{t\to\infty}\mathbf P_B(G_m(t))
\le Ce^{-cm}.
$$

The finitely many gaps present in the deterministic finite initial configuration contribute only exponentially decaying survival probabilities.

## Nonescape

The same statewise corrector gives

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v,
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-v
\quad\text{a.s.}
$$

For fixed `M`, the probability that either outer edge has not passed the corresponding side of `[-M,M]` tends to zero. If both edges have passed and `[-M,M]` is empty, then this window lies inside an internal gap of width at least `2M+1`. Hence

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM},
$$

and therefore

$$
\lim_{M\to\infty}\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)=0.
$$

## External stationary-limit interface

Jahnel--Köppl, *Restriction and mixing properties of interacting particle systems with unbounded range* (2026), Theorem 2.5, proves that on `Z` every weak limit point is stationary under assumptions `(L1)` and `(R1)--(R3)` with an exponentially decaying influence profile. BABP satisfies these assumptions directly. Use singleton update regions. The site flip rate is bounded by `2 max(1,lambda)`, update diameter is bounded, and changing a spin can affect the flip rate only at its two nearest neighbours. With `rho(r)=e^{-alpha r}`, `(R2)` follows from the triangle inequality and `(R3)` follows from finite-range influence. No shift-invariance or reversibility of the initial law is required.

For stationary-law classification, Martinelli--Shapira--Toninelli (2025), Corollary 2.9, use complementary infection variables `eta=1-xi`. Their constraint is

$$
c_x(\eta)=2-\eta_{x-1}-\eta_{x+1}=N_x(\xi),
$$

and their rates are infected-to-healthy `p c_x` and healthy-to-infected `q c_x`. With

$$
\lambda=\frac qp,
$$

the present generator is exactly `p^{-1}` times theirs. This constant time rescaling does not alter stationary laws. Thus every stationary one-dimensional BABP law in the present convention is

$$
\alpha\delta_\varnothing+(1-\alpha)\pi_q.
$$

## Completion of the proof

The configuration space `{0,1}^Z` is compact. Take any sequence `t_n->infinity` and any weakly convergent subsequence of the laws, with limit `nu`. The stationary-limit theorem makes `nu` stationary, so

$$
\nu=\alpha\delta_\varnothing+(1-\alpha)\pi_q.
$$

For fixed `M`, the event of being empty on `[-M,M]` is a clopen cylinder. The nonescape estimate gives

$$
\nu(B\cap[-M,M]=\varnothing)\le Ce^{-cM}.
$$

The mixture formula gives

$$
\nu(B\cap[-M,M]=\varnothing)
=\alpha+(1-\alpha)(1-q)^{2M+1}\ge\alpha.
$$

Sending `M` to infinity yields `alpha=0`. Every subsequential limit is `pi_q`, hence the full trajectory converges locally.

## Verified concrete corollary at `lambda=1/40`

`BABP-EDGE-001` supplies a ten-site corrector at

$$
\lambda=\frac1{40}
$$

with uniform statewise drift

$$
D_{10,1/40}(u,z;\phi)
\ge\frac{1033}{40000000}>0.
$$

Therefore one-dimensional BABP at `lambda=1/40`, started from every finite nonempty deterministic particle set, converges locally to Bernoulli product equilibrium of density `1/41`.

Martinelli--Shapira--Toninelli (2025), Remark 5.4, records the previous finite-seed convergence range as `lambda>0.0347`. Thus `1/40=0.025` lies strictly below that recorded range.

## Verification record and scope

The edge certificate was independently audited in commit `d1ef2ca`, `research/active/babp-finite-seed/audits/001-edge-corrector-audit.md`.

The convergence theorem was independently reviewed in:

- commit `abb05f6`, `research/active/babp-finite-seed/audits/002-convergence-review-a.md`;
- commit `1aeb5a5`, `research/active/babp-finite-seed/audits/002-convergence-review-b.md`.

Both reviews accepted the theorem. The localization and finite-spatial-truncation points requested by Review A are included above. Review B independently checked the generator/time-rescaling convention and the Jahnel--Köppl stationary-limit interface.

No convergence rate is claimed. The initial condition is restricted to finite nonempty deterministic sets. The all-parameter statement remains open. A targeted successor search through 2026-08-15 found no later theorem removing the `0.0347` restriction, but publication-level closest-prior-work/novelty review remains pending.