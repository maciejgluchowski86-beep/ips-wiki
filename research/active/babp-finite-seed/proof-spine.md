# Proof spine

## Main target

For one-dimensional BABP with branching parameter `lambda>0`, started from any finite nonempty particle set `B`, prove local convergence to Bernoulli equilibrium `pi_q` with

$$
q=\frac{\lambda}{1+\lambda}.
$$

The programme now has a verified theorem below the previously recorded finite-seed range. The remaining target is all `lambda>0`.

## E0. Finite-test convergence criterion

BABP self-duality gives the standard finite-test criterion for local convergence.

**Status:** established external input; not used in the new corrector-to-convergence bridge.

## E1. Stationary-limit and stationary-law inputs

For every fixed `lambda>0`:

1. every weak limit point of the BABP law is stationary;
2. every stationary one-dimensional BABP law is a convex combination of the empty state and Bernoulli equilibrium.

For (1), Jahnel--Köppl (2026), Theorem 2.5, was checked from the full source. BABP satisfies `(L1)` and `(R1)--(R3)` with `rho(r)=e^{-alpha r}`: updates are single-site, site rates are uniformly bounded, and influence is nearest-neighbour.

For (2), Martinelli--Shapira--Toninelli (2025), Corollary 2.9, applies after the explicit constant time rescaling

$$
\lambda=q/p,
\qquad
L_{\mathrm{project}}=p^{-1}L_{\mathrm{MST}}.
$$

**Status:** verified external interfaces for present use. Mountford and Ramírez--Varadhan remain historical antecedents but are not needed as unchecked hypotheses.

## E2. Finite-window right-edge corrector

For a finite nonempty BABP configuration, let `R` be its right edge and let `u in {0,1}^k`, `z in {0,1}` encode the first `k+1` sites behind it. For bounded `phi`, put

$$
H(B)=R(B)+\phi(u(B)).
$$

The exact drift is `D_{k,lambda}(u,z;phi)`. If

$$
D_{k,\lambda}(u,z;\phi)\ge v>0
$$

uniformly, then

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v,
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-v
\quad\text{a.s.}
$$

for every finite nonempty initial state.

**Status:** verified claim `BABP-EDGE-001`, audit `d1ef2ca`.

At `k=10`, `lambda=1/40`, the exact minimum drift is

$$
\frac{1033}{40000000}>0.
$$

## E3. DFP black-box route

The finite-test self-duality cylinder has no probability-law DFP representation, and its finite-window signed representation has exponentially growing coefficient norm.

**Status:** demoted.

## E4. Statewise corrector to finite-seed convergence

Assume `(EC)`:

$$
\exists k,\phi,v>0\quad
D_{k,\lambda}(u,z;\phi)\ge v
\quad\text{for every }(u,z).
$$

Then for every finite nonempty deterministic initial set,

$$
\operatorname{Law}_B(B_t)\Longrightarrow\pi_q.
$$

The proof uses `(EC)` on internal gaps, not merely on the two outer edges. Positive gaps have unique genealogies. The corrected width of a tagged gap has drift at most `-2v`; after localization, exponential tilting gives uniform lifetime and width tails. Poisson boundary displacement and a compensator sum, first truncated to `|x|<=N` and then passed to `N=infinity` by monotone convergence, yield

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

E1 then excludes the empty component of every subsequential limit.

No particle-number growth theorem is used.

**Status:** verified claim `BABP-CONV-001` after Professor reconstruction and two fresh independent correctness reviews:

- `audits/002-convergence-review-a.md`, commit `abb05f6`;
- `audits/002-convergence-review-b.md`, commit `1aeb5a5`.

Stable proof: `research/results/babp-finite-seed-convergence.md`.

**Concrete verified corollary:** finite-seed convergence at

$$
\lambda=\frac1{40}=0.025,
$$

below the `0.0347` range recorded in Martinelli--Shapira--Toninelli (2025), Remark 5.4.

## E5. Positive correctors for every `lambda>0`

This is the current first development edge.

For fixed `lambda`, define

$$
v_k(\lambda)=\sup_\phi\min_{u,z}D_{k,\lambda}(u,z;\phi).
$$

Window monotonicity is exact:

$$
v_{k+1}(\lambda)\ge v_k(\lambda).
$$

Student B's `002-edge-environment-dual.md`, commit `b9fdc55`, proposes an infinite-volume dual. Let `Q_infinity` be the environment seen from the right edge and `I_lambda` its invariant laws. The core proposed identity is

$$
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}
\int(\lambda-u_1)\,d\mu.
$$

For every invariant front law, stationarity of the first bit gives

$$
\mu(u_1=1)
=
\frac{\lambda}{1+\lambda}
\left(1+\frac12\mu(u_1=0,u_2=1)\right).
$$

Hence the proposed reduction is

$$
\lim_{k\to\infty}v_k(\lambda)
=
\frac{\lambda}{1+\lambda}
\left(\lambda-rac12
\sup_{\mu\in\mathcal I_\lambda}\mu(01)\right).
$$

The direct all-parameter target is therefore the **front-gap lemma**:

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda
\qquad\text{for every fixed }\lambda>0.
$$

If the infinite-front dual identity is correct and the front-gap lemma holds, E4 gives the full all-parameter finite-seed theorem.

**Status:** front reduction claimed for research use, not independently audited. Graduate Student B owns its validation and the front-gap attack in assignment 003.

**Parameter-threshold caution:** the shorthand statement `lambda_k -> 0`, with `lambda_k=inf{lambda:v_k(lambda)>0}`, should not be treated as equivalent to the all-parameter corrector statement unless the relevant monotonicity/interval structure in the parameter `lambda` is proved. Monotonicity in the window size `k` does not by itself supply this.

## N1. Publication-level novelty

A targeted search through 2026-08-15 found no later theorem removing the `0.0347` restriction, and the 2025 progress paper records that as the known range. Publication-level priority/closest-prior-work checking remains pending.

**Owner:** Graduate Student A as part of the writeup assignment, followed by independent literature audit before submission-level confidence.

## Current first unresolved edge

**E5: verify the infinite-front reduction and prove positive worst invariant front drift for every fixed `lambda>0`, preferably through the front-gap lemma.**

## Reserve

The residual simple-IPS positive-rates/noisy-East problem remains the strongest identified reserve if the all-parameter BABP front problem becomes analytically sterile.