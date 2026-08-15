# Verified BABP finite-window technical record

Status: verified project mathematics retained for reuse. **This file does not record a new project research result under the standing novelty standard in `CHATGPT.md`.**

Claim registry: `BABP-EDGE-001` and `BABP-CONV-001` in `research/claim-registry.md`.

## Research-contribution correction

Earlier versions of this record successively overstated two things. First, before the full text of Sudbury (1999) was available, the project treated the finite-window mechanism and the corrector-to-convergence implication as potentially new. The full source shows that both are classical. Second, after that provenance correction, the project still described the exact ten-site `lambda=1/40` calculation as a project contribution or new range result. The principal has now supplied a standing novelty standard: running an existing method at a larger window/order/degree or analogous complexity parameter to obtain a quantitatively better constant does not count as a new result, even when the arithmetic is exact.

That standard applies directly here.

Sudbury's Section 3 is already a finite-window edge-corrector/submartingale construction for BABP. He follows an outer particle, records an `m`-site block, keeps the single next site as an unresolved end-value, and adds a correction `S_i` indexed by the block state. After reflection,

- his `m` is the present `k`;
- his `m`-block is the present edge word `u`;
- his end-value `x_{m+1}` is the present exterior bit `z`;
- his corrected local gain

$$
a_i+\sum_jq_{ij}(S_j-S_i)
$$

is the present finite-window drift `D_{k,lambda}(u,z;phi)`.

The Maxwell's-demon formulation is exactly the robust exterior-bit issue. Sudbury lets the end-value be chosen as a function of the current block state, and Lemma 5 requires one correction vector to give a submartingale for every assignment of those end-values. Since the drift in a given block state depends only on that state's single end-value, this is equivalent to requiring the statewise inequality for both `z=0` and `z=1` in every `u`.

Sudbury's Table 2 reports trial values through `m=8`, `lambda_m=0.0347`, and explicitly says they were obtained by trial and error rather than proved exact critical values. Lemma 7 extends any successful window to every larger window by ignoring the additional coordinates.

Immediately before Theorem 7, Sudbury states that Neuhauser--Sudbury (1993) used existence of a suitable submartingale in their stationary-state argument, that his Section 3 extends that condition from the old `1/3` range to `0.0347`, and that their Section 5 argument then proceeds unchanged. Therefore the theorem-level principle “a suitable robust finite-window corrector suffices for finite-seed convergence” is classical, not a project discovery.

The exact rational `k=10` certificate at

$$
\lambda=\frac1{40}=0.025
$$

with uniform margin

$$
\frac{1033}{40000000}>0
$$

is mathematically correct and independently audited. It is a useful larger-window witness inside Sudbury's arbitrary-`m` framework. Under the principal's standing novelty standard, it is **not counted as a new project result or contribution**. The independently computed `k=8` crossing `0.0346195434755...` is likewise a refinement of Sudbury's reported decimal for the same eight-site problem, not a research result.

The proof below is retained because it is a clean, audited, self-contained modern proof of the classical corrector-to-convergence implication and may be useful as technical infrastructure. No novelty claim is made for its tagged-gap architecture until Neuhauser--Sudbury (1993), Section 5, is inspected.

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

## Self-contained corrector-to-convergence proposition

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

This proposition is retained as verified mathematics, not as a novelty claim. The statewise corrector hypothesis is essential to the proof below. Bare outer-edge liminf/limsup velocity bounds alone are not asserted to imply convergence.

## Internal-gap contraction

An internal gap is a maximal nonempty finite interval of vacant sites strictly between the outer particles. A newly nucleated gap has width one. A positive gap cannot split because a strictly interior vacancy has no occupied neighbour and cannot be filled. Two positive gaps cannot merge: if the separating particle block erodes to one particle, that particle has vacancies on both sides and therefore death rate zero. Thus every positive gap has a unique genealogy from nucleation until closure.

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
\mathcal L H_L(C)\le-v.
$$

Set `Z=H_L(C)-H_R(A)-1`. For gap width at least two, no nearest-neighbour transition sees both populations, so

$$
\mathcal L^\times Z\le-2v.
$$

At width one, the sole vacancy fills at total rate `2lambda`; replacing either closing transition by killing decreases the generator of a positive test function. If `K=||phi||_infty`, then while the gap is alive

$$
g-2K\le Z\le g+2K.
$$

Only fixed neighbourhoods of the two inner edges can change `Z`. Let `J` and `rho` uniformly bound its jump size and the rate of `Z`-changing events. For sufficiently small `theta>0`,

$$
\mathcal L^\dagger e^{\theta Z}
\le-\gamma e^{\theta Z}
$$

for some `gamma>0`.

This use of the unbounded exponential test is localized: stop first when the gap width reaches `n` and, if desired, after the first `n` jumps; apply Dynkin's formula on the stopped state space; then remove the localization. Consequently a gap born at width one has uniform exponential tails for both lifetime and maximal width.

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
\beta=2(1+\lambda).
$$

The spatial Poisson tail is summable:

$$
\sum_{x\in\mathbb Z}
\mathbf P(\operatorname{Pois}(\beta r)\ge|x|)^{1/3}
\le C_\beta(1+r).
$$

A gap is nucleated at a fixed site at predictable rate at most two. First sum only over `|x|<=N`; the strong Markov property gives the corresponding finite compensator bound. Monotone convergence then removes the spatial truncation. Hence, if `G_m(t)` is the event that zero lies in an internal gap of width at least `m`,

$$
\limsup_{t\to\infty}\mathbf P_B(G_m(t))
\le Ce^{-cm}.
$$

The finitely many initial gaps contribute only exponentially decaying survival probabilities.

## Nonescape

The same corrector gives

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v,
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-v
\quad\text{a.s.}
$$

If both outer edges have passed `[-M,M]` and that window is empty, the window lies inside an internal gap of width at least `2M+1`. Therefore

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

## External stationary-limit interface

Jahnel--Köppl (2026), Theorem 2.5, makes every weak limit point stationary for one-dimensional IPS satisfying `(L1)` and `(R1)--(R3)` with exponential influence. BABP satisfies these assumptions directly: updates are single-site, site rates are uniformly bounded, and influence has nearest-neighbour support.

Martinelli--Shapira--Toninelli (2025), Corollary 2.9, use complementary infection variables. With `lambda=q/p`, the present generator is exactly `p^{-1}` times theirs, so stationary laws are unchanged. Every stationary one-dimensional BABP law is therefore

$$
\alpha\delta_\varnothing+(1-\alpha)\pi_q.
$$

## Completion of the proof

Take any weak subsequential limit `nu` of the laws. It is stationary, hence has the mixture form above. For fixed `M`, the event of being empty on `[-M,M]` is clopen, so the nonescape estimate gives

$$
\nu(B\cap[-M,M]=\varnothing)\le Ce^{-cM}.
$$

But the mixture probability is at least `alpha`. Letting `M` tend to infinity gives `alpha=0`. Thus every subsequential limit is `pi_q`, and the full trajectory converges locally.

## Exact `lambda=1/40` technical consequence

`BABP-EDGE-001` supplies

$$
D_{10,1/40}(u,z;\phi)
\ge\frac{1033}{40000000}>0
$$

for every edge state. Hence BABP at `lambda=1/40`, from every finite nonempty deterministic particle set, converges locally to Bernoulli equilibrium of density `1/41`.

Sudbury (1999), Theorem 7, reports the `0.0347` finite-seed range using the same finite-window framework. The `1/40` statement is a correct larger-window quantitative extension inside that framework. It is **not counted as a project research result** under the standing novelty standard.

## Verification record and scope

The edge certificate was independently audited in commit `d1ef2ca`, `research/active/babp-finite-seed/audits/001-edge-corrector-audit.md`.

The convergence proof was independently reviewed in:

- commit `abb05f6`, `research/active/babp-finite-seed/audits/002-convergence-review-a.md`;
- commit `1aeb5a5`, `research/active/babp-finite-seed/audits/002-convergence-review-b.md`.

No convergence rate is claimed. The initial condition is restricted to finite nonempty deterministic sets. The all-parameter statement remains open. Under the standing novelty standard, the verified finite-window calculations and classical convergence implication are retained as technical infrastructure rather than counted as programme results.