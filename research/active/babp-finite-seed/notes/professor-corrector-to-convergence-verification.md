# Professor verification: finite-window corrector to BABP finite-seed convergence

Date: 2026-08-15

Status: verified after Professor reconstruction and two fresh independent correctness reviews.

Decisive student source: `students/student-b/002-edge-speed-to-convergence.md`, commit `f79d0fb`.

Independent reviews:

- `audits/002-convergence-review-a.md`, commit `abb05f6`;
- `audits/002-convergence-review-b.md`, commit `1aeb5a5`.

The two rigor points raised by Review A are incorporated below: localization for the unbounded exponential test function and finite spatial truncation before the infinite compensator sum. The convention/time-rescaling clarification requested by Review B is also incorporated.

## 1. Model convention and theorem boundary

Use particle variables `xi(x) in {0,1}`, with `xi(x)=1` meaning a BABP particle. Put

$$
N_x(\xi)=\xi(x-1)+\xi(x+1).
$$

The project generator is the single-site flip process

$$
0\to1\text{ at rate }\lambda N_x(\xi),
\qquad
1\to0\text{ at rate }N_x(\xi).
$$

Fix `lambda>0`. The load-bearing hypothesis is not merely a ballistic edge conclusion. Assume there are `k>=1`, a bounded function `phi:{0,1}^k -> R`, and `v>0` such that the exact right-edge corrector drift satisfies

$$
D_{k,\lambda}(u,z;\phi)\ge v
$$

for every edge word `u in {0,1}^k` and exterior bit `z in {0,1}`. Call this hypothesis `(EC)`.

The theorem verified here is:

> If `(EC)` holds, then one-dimensional BABP started from every finite nonempty deterministic particle set converges locally to Bernoulli equilibrium of particle density `q=lambda/(1+lambda)`.

The proof uses `(EC)` statewise on internal gaps. Bare statements about `liminf R_t/t` and `limsup L_t/t` are not asserted to imply convergence.

## 2. Gap genealogy

An internal gap is a maximal nonempty finite interval of vacant sites strictly between the outer particles.

A new internal gap is created only when a particle with both nearest neighbours occupied dies. Hence every post-time-zero gap genealogy is born with width one. If exactly one neighbour is vacant, the death merely extends the existing adjacent gap. If both neighbours are vacant, the death rate is zero.

A positive gap cannot split: a strictly interior vacant site has two vacant neighbours and therefore birth rate zero, so births occur only at endpoint vacancies and shrink the gap. Distinct positive gaps cannot merge. A particle block separating them may erode from its two exposed ends, but once only one separating particle remains, that particle has a vacant neighbour on each side and therefore death rate zero. Thus every positive internal gap has an unambiguous genealogy from nucleation until closure.

## 3. Corrected width of a tagged gap

Fix a tagged gap while alive. Let `A_t` be all particles to its left and `C_t` all particles to its right. Both are finite and nonempty until closure. Put

$$
a_t=R(A_t),\qquad b_t=L(C_t),\qquad g_t=b_t-a_t-1\ge1.
$$

For `g_t>=2`, no nearest-neighbour update sees particles on both sides of the gap, so the two inner-edge dynamics agree with standalone BABP dynamics on `A_t` and `C_t`. At `g_t=1`, the unique vacancy has two occupied neighbours and fills at total rate `2lambda`, exactly the sum of the rate-`lambda` outward birth from each side. Either such event closes the tagged gap. Death of either bounding particle depends only on its particle-side neighbour because the gap-side neighbour is vacant.

Let

$$
H_R(A)=R(A)+\phi(U_R(A)).
$$

By `(EC)`,

$$
\mathcal L H_R(A)\ge v
$$

for every finite nonempty `A`. Reflection gives

$$
H_L(C)=L(C)-\phi(U_L(C)),
\qquad
\mathcal L H_L(C)\le-v.
$$

Define

$$
Z=H_L(C)-H_R(A)-1
=g-\phi(U_L(C))-\phi(U_R(A)).
$$

The product generator before closure satisfies

$$
\mathcal L^\times Z\le-2v.
$$

At width one, replace either closing transition by killing. For any positive test function, the killed transition value is zero while the corresponding continuation value under the product generator is positive. Killing therefore only decreases the generator.

If `K=||phi||_infty`, then while the gap is alive

$$
g-2K\le Z\le g+2K.
$$

Only fixed `k`-neighbourhoods of the two inner edges can change `Z`. Hence there are deterministic constants `J,rho<infinity`, depending only on `(k,lambda,phi)`, such that every non-killing jump has `|Delta Z|<=J` and the total rate of `Z`-changing events is at most `rho`, uniformly in the ambient finite particle configuration.

## 4. Localized exponential estimate

For `f=e^{theta Z}` and `|y|<=J`,

$$
e^{\theta y}-1
\le \theta y+\frac{\theta^2}{2}e^{\theta J}y^2.
$$

Thus, statewise on alive tagged-gap states,

$$
\frac{\mathcal L^\dagger f}{f}
\le -2v\theta
+\frac{\theta^2}{2}e^{\theta J}\rho J^2.
$$

Choose `theta>0` so small that the second term is at most `v theta`, and put `gamma=v theta`. Then

$$
\mathcal L^\dagger e^{\theta Z}\le-\gamma e^{\theta Z}.
$$

Because `e^{theta Z}` is unbounded as the gap width grows, the probabilistic consequences are taken after localization. Let

$$
\sigma_n=\inf\{t<\tau:g_t\ge n\},
$$

where `tau` is the gap closure time, and if desired also stop after the first `n` jumps. On the stopped state space the exponential test is bounded, so Dynkin's formula applies to

$$
e^{\gamma(t\wedge\tau\wedge\sigma_n)}
 e^{\theta Z_{t\wedge\tau\wedge\sigma_n}}
$$

with cemetery value zero after closure. Letting the jump-count localization and then `n` tend to infinity, using positivity together with Fatou/monotone localization, gives the killed-semigroup estimate used below.

For a gap born at width one, `Z_0<=1+2K`, while on survival `Z_t>=1-2K`. Hence

$$
\mathbf P(\tau>t)\le C_0e^{-\gamma t}.
$$

Stopping instead at `sigma_m` gives

$$
\mathbf P(\sigma_m<\tau)\le C_1e^{-\theta m}.
$$

The constants depend only on `(k,lambda,phi,v)`, not on the surrounding finite configuration, the gap age, or the birth location. A deterministic initial gap of width `g_0` satisfies the same lifetime estimate with a finite prefactor depending on `g_0`.

## 5. Spatial displacement

Let `N_t` count changes of either endpoint of the tagged gap before closure. Each endpoint extends by one only when the bounding particle dies. Since its gap-side neighbour is vacant, the extension rate is at most one. Each endpoint shrinks by one through a birth into the adjacent vacancy at rate `lambda`. At width one, the two closing birth clocks have total rate `2lambda`. Therefore the predictable intensity of `N_t` is at most

$$
\beta=2(1+\lambda),
$$

so `N_t` is stochastically dominated by a rate-`beta` Poisson process.

A gap born as the singleton `{x}` that contains the origin at age `r` must have undergone at least `|x|` endpoint shifts. If `E_{m,r,x}` denotes the event that this genealogy is alive at age `r`, has width at least `m`, and contains zero, then

$$
E_{m,r,x}\subset
\{\sigma_m<\tau\}\cap\{\tau>r\}\cap\{N_r\ge|x|\}.
$$

No independence is needed. Using `P(A cap B cap C)<= [P(A)P(B)P(C)]^{1/3}` gives

$$
\mathbf P(E_{m,r,x})
\le C e^{-c_1m}e^{-c_2r}
\mathbf P(\operatorname{Pois}(\beta r)\ge|x|)^{1/3}.
$$

Moreover,

$$
\sum_{x\in\mathbb Z}
\mathbf P(\operatorname{Pois}(\beta r)\ge|x|)^{1/3}
\le C_\beta(1+r).
$$

Indeed, the `O(1+r)` sites up to a sufficiently large multiple of the Poisson mean contribute at most one each, and beyond that cutoff the standard Chernoff bound is exponentially summable even after taking a cube root.

## 6. Truncated compensator sum over nucleations

A new gap is nucleated at site `x` only when `x` is occupied, both neighbours are occupied, and the particle at `x` dies. Its predictable nucleation intensity is therefore at most two.

To avoid any implicit infinite-space interchange, first fix `N<infinity` and count only nucleations with `|x|<=N`. By the strong Markov property at a nucleation time and the uniform tagged-gap estimate, the expected number of those nucleations whose descendant gap at time `t` contains zero and has width at least `m` is at most

$$
2\sum_{|x|\le N}\int_0^t
C e^{-c_1m}e^{-c_2(t-s)}
\mathbf P(\operatorname{Pois}(\beta(t-s))\ge|x|)^{1/3}\,ds.
$$

The probability that at least one such genealogy contributes is bounded by this expected count. Now let `N->infinity`. The left-hand events increase with `N`, so monotone convergence applies. The spatial summability from the previous section gives

$$
\mathbf P(\text{a post-time-zero gap of width at least }m
\text{ contains }0\text{ at time }t)
\le C'e^{-cm}
$$

uniformly in `t`, because

$$
\int_0^\infty e^{-c_2r}(1+r)\,dr<\infty.
$$

There are only finitely many internal gaps at time zero. The probability that any fixed initial gap survives to time `t` tends to zero exponentially, with a finite prefactor depending on its deterministic initial width. Consequently, if

$$
G_m(t)=\{0\text{ lies in an internal gap of width at least }m\},
$$

then

$$
\limsup_{t\to\infty}\mathbf P_B(G_m(t))\le Ce^{-cm}.
$$

This is a uniform late-time estimate after summing all gap genealogies, not a per-gap statement.

## 7. Nonescape from fixed windows

The same statewise corrector gives the separately verified outer-edge bounds

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v,
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-v
\quad\text{a.s.}
$$

For fixed `M`,

$$
\mathbf P_B(R_t\le M\text{ or }L_t\ge-M)\to0.
$$

On the complementary event, if `B_t cap [-M,M]` is empty, then `[-M,M]` lies in an internal gap of width at least `2M+1`. Hence

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

The proof uses no property of the deterministic initial state beyond finiteness and nonemptiness.

## 8. Stationarity of weak limit points: direct source check

The historical Mountford and Ramírez--Varadhan results are useful provenance, but the verification does not depend on uninspected versions of those papers.

Jahnel--Köppl, *Restriction and mixing properties of interacting particle systems with unbounded range*, arXiv:2603.21817 (2026), Theorem 2.5, states for `S=Z` that every weak limit point is stationary when `(L1)` and `(R1)--(R3)` hold with `rho(r)=e^{-alpha r}` for some `alpha>0`. Their theorem explicitly says no shift-invariance or reversibility is required.

BABP fits their framework directly. Use singleton update regions `Delta={x}`. The rates are translation-invariant and continuous. For every site, the total flip rate is at most `2 max(1,lambda)`, so `(L1)` holds. Singleton updates have uniformly bounded diameter, so `(R1)` holds. For `rho(r)=e^{-alpha r}`, `(R2)` follows from the triangle inequality with constant one. A change at `y` can alter the flip rate at `x` only when `|x-y|=1`, and the oscillation is uniformly bounded by a constant depending only on `lambda`; hence the influence kernel has finite range and `(R3)` holds for every `alpha>0`. Thus Theorem 2.5 applies for every fixed `lambda>0`.

Review B could inspect this source in full. Mountford (1993) was accessible only through its published abstract, and Ramírez--Varadhan (1996) was verified bibliographically but not line by line; neither inaccessible older source is needed for the theorem.

## 9. Stationary-law classification and time-rescaling convention

Martinelli--Shapira--Toninelli (2025) use complementary spin variables `eta=1-xi`, where `eta=0` is an infection. Their constraint is

$$
c_x(\eta)=2-\eta_{x-1}-\eta_{x+1}=N_x(\xi).
$$

Their BABP generator has healthy-to-infected rate `q c_x` and infected-to-healthy rate `p c_x`, where `p=1-q`. After multiplying their generator by `1/p`, the rates become

$$
0\to1\text{ in particle variables at rate }(q/p)N_x,
\qquad
1\to0\text{ at rate }N_x.
$$

Thus the present parameter is

$$
\lambda=\frac qp,
\qquad
q=\frac{\lambda}{1+\lambda},
\qquad
p=\frac1{1+\lambda},
$$

and

$$
L_{\mathrm{project}}=p^{-1}L_{\mathrm{MST}}.
$$

A positive scalar time-rescaling does not change stationary laws. Martinelli--Shapira--Toninelli, Corollary 2.9, therefore gives in the present convention that every stationary one-dimensional BABP law is

$$
\alpha\delta_\varnothing+(1-\alpha)\pi_q,
\qquad \alpha\in[0,1].
$$

Review B checked the full 2025 source and the original Neuhauser--Sudbury convention. No normalization mismatch remains.

## 10. Subsequence argument

The configuration space `{0,1}^Z` is compact in the product topology. Given any sequence `t_n->infinity`, extract a weakly convergent subsequence with limit `nu`. Section 8 makes `nu` stationary, and Section 9 gives

$$
\nu=\alpha\delta_\varnothing+(1-\alpha)\pi_q.
$$

For each fixed `M`, the event

$$
E_M=\{B:B\cap[-M,M]=\varnothing\}
$$

is a clopen cylinder. Hence probabilities converge along the subsequence and the nonescape estimate gives

$$
\nu(E_M)\le Ce^{-cM}.
$$

The mixture formula gives

$$
\nu(E_M)
=\alpha+(1-\alpha)(1-q)^{2M+1}\ge\alpha.
$$

Letting `M->infinity` yields `alpha=0`. Every subsequential limit is therefore `pi_q`, so the full trajectory converges locally to `pi_q`.

The 2025 particle-number growth theorem is not used.

## 11. Concrete corollary

Verified project claim `BABP-EDGE-001` supplies `(EC)` at

$$
\lambda=\frac1{40},\qquad k=10,
\qquad v=\frac{1033}{40000000}>0.
$$

Therefore the theorem above yields local convergence from every finite nonempty deterministic initial particle set at `lambda=1/40`.

Martinelli--Shapira--Toninelli (2025), Remark 5.4, records finite-seed convergence only for `lambda>0.0347` after the earlier `lambda>1/3` result. Since `1/40=0.025<0.0347`, this corollary lies strictly below that recorded published range.

A targeted successor search through 2026-08-15 found no later theorem removing the `0.0347` finite-seed restriction. This is current evidence for novelty, not a substitute for the independent closest-prior-work audit required before publication-level novelty confidence.

## 12. Verification decision

The internal proof has been reconstructed by the Professor and accepted independently by two fresh hostile correctness reviewers. Both reviews confirm the statewise character of `(EC)` is essential to the present proof and find no hidden initial-condition or particle-growth hypothesis. Review A's localization and finite-truncation rigor requests are explicitly built into Sections 4 and 6 above. Review B's convention/time-rescaling request is explicitly built into Section 9.

Accordingly `BABP-CONV-001` may be promoted to `verified` for mathematical use. Publication-level novelty checking remains a separate pending task.