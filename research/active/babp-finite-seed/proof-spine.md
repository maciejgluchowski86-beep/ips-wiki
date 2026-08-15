# Proof spine

## Main target

For one-dimensional BABP with branching parameter `lambda>0`, started from any finite nonempty particle set `B`, prove local convergence to Bernoulli equilibrium `pi` with particle density

$$
q=\frac{\lambda}{1+\lambda}.
$$

Begin with `B={0}`. The programme is committed. Meeting 004 produced a complete **claimed** bridge from a statewise positive finite-window edge corrector to finite-seed convergence; two fresh independent audits are pending before that theorem can be promoted.

## E0. Finite-test convergence criterion

BABP self-duality gives, for finite `T`,

$$
\mathbf E_B\left[\left(-\frac1\lambda\right)^{|B(t)\cap T|}\right]
=
\mathbf E_T\left[\left(-\frac1\lambda\right)^{|T(t)\cap B|}\right].
$$

The functions indexed by subsets of a fixed finite window form a basis of local observables, and Bernoulli equilibrium has zero expectation for every nonempty such duality function. Hence decay of these finite-test observables implies local convergence.

**Status:** established external input; independently rederived by Student B. Not used in the new gap bridge.

## E1. External stationary-limit inputs

For every fixed `lambda>0`:

1. every weak limit point of the one-dimensional BABP trajectory is stationary;
2. every stationary BABP law is a convex combination of the empty state and Bernoulli equilibrium.

For (1), the Professor checked Jahnel--Köppl (2026), Theorem 2.5. BABP has finite local state space, single-site updates, uniformly bounded site rate, and nearest-neighbour dependence, so its influence has finite range and satisfies the theorem's exponential-decay assumptions.

For (2), Martinelli--Shapira--Toninelli (2025), Corollary 2.9, states the one-dimensional BABP classification directly.

**Status:** external primary-source inputs checked by the Professor; audit 003 will independently verify the interface.

## E2. Finite-window right-edge corrector

For a finite nonempty BABP configuration `B`, let `R=max B`. Encode the first `k` sites behind `R` by `u in {0,1}^k` and the next unresolved bit by `z`. For bounded `phi:{0,1}^k -> R`, put

$$
H(B)=R(B)+\phi(u(B)).
$$

The exact generator drift is

$$
\begin{aligned}
D_{k,\lambda}(u,z;\phi)
={}&\lambda[1+\phi(T_+u)-\phi(u)]\\
&+u_1[-1+\phi(T_-^zu)-\phi(u)]\\
&+\sum_{j=1}^k n_j^z(u)[\lambda(1-u_j)+u_j]
[\phi(u^{(j)})-\phi(u)].
\end{aligned}
$$

If `D>=v>0` uniformly, then for every finite nonempty initial configuration

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v,
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-v
\quad\text{a.s.}
$$

The corrector argument does not assert existence of the corresponding limits.

**Status:** verified by fresh hostile audit `d1ef2ca` as claim `BABP-EDGE-001`.

**Calibration:**

- `k=1`: strict feasibility iff `lambda>1/3`;
- `k=8`: independently reproduced numerical zero crossing `0.0346195434755...`;
- `k=10`, `lambda=1/40`: exact rational certificate with minimum drift

$$
\frac{1033}{40000000}>0.
$$

Literal historical identity with Sudbury's internal `k=8` calculation remains unverified and is not load-bearing.

## E3. DFP black-box route

The deterministic finite-test self-duality cylinder has no probability-law representation by DFP initial sets, and its unique signed representation on a finite ambient window has total-variation norm growing exponentially with window size.

**Status:** algebraic obstruction established for present use; DFP demoted to a secondary route.

## E4. Statewise corrector to local convergence

This is the theorem proved in Student B assignment 002.

Assume the **statewise** condition `(EC)`:

$$
\exists k\ge1,\ \phi:\{0,1\}^k\to\mathbb R\text{ bounded},\ v>0
\quad\text{such that}\quad
D_{k,\lambda}(u,z;\phi)\ge v
$$

for every `u,z`.

Then for every finite nonempty deterministic initial `B`,

$$
\operatorname{Law}_B(B_t)\Longrightarrow\pi_q.
$$

The proof is not an inference from the outer liminf/limsup bounds alone. It reuses `(EC)` on every internal gap:

1. positive gaps are born at width one, do not split, and distinct positive gaps do not merge;
2. applying the right/left corrector to the populations bordering a tagged gap gives a corrected width with drift at most `-2v` until closure;
3. exponential tilting gives uniform exponential tails for gap lifetime and maximal width;
4. boundary displacement is Poisson dominated;
5. a compensator sum over gap nucleations yields

$$
\limsup_{t\to\infty}
\mathbf P_B(0\text{ lies in an internal gap of width at least }m)
\le Ce^{-cm};
$$

6. combining this with the outer ballistic bounds yields

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM};
$$

7. E1 then forces every subsequential stationary mixture to have zero empty-state coefficient.

No particle-number growth theorem is used. The initial condition is only assumed finite, deterministic, and nonempty.

**Status:** `claimed` as project claim `BABP-CONV-001`. Professor independently reconstructed the load-bearing gap argument and external theorem interface. Two fresh independent audits are pending:

- `audits/002-corrector-to-convergence-request.md`;
- `audits/003-corrector-to-convergence-request.md`.

**Concrete claimed corollary:** verified `BABP-EDGE-001` supplies `(EC)` at `lambda=1/40`, so finite-seed convergence holds there. This lies below the `0.0347` range recorded in Martinelli--Shapira--Toninelli (2025), Remark 5.4. Do not promote this conclusion until both audits are resolved.

## E5. Remove the finite-window corrector threshold

Assuming E4 survives audit, this becomes the first development bottleneck.

For fixed `k`, define

$$
v_k(\lambda)=\sup_\phi\min_{u,z}D_{k,\lambda}(u,z;\phi)
$$

and

$$
\lambda_k=\inf\{\lambda>0:v_k(\lambda)>0\}.
$$

The all-parameter target follows if one proves that for every `lambda>0` there is some finite `k` and bounded `phi` satisfying `(EC)`. A sufficient formulation is

$$
\lambda_k\longrightarrow0,
$$

provided the threshold definition behaves as expected.

The computed values decrease sharply through `k=10`, but no analytic proof is known. Candidate interpretations include a Poisson equation/hitting-time corrector for the environment seen from the edge or an explicit multiscale family of correctors.

**Status:** open. Development is paused until audits 002 and 003 settle E4, because any repair to E4 may change the right object to generalize.

## H1. Historical provenance

The exact relation between the present `k=8` LP and Sudbury's internal 1999 calculation remains unverified because the full paper body has not been obtained. This is not load-bearing for E2 or E4. It may still illuminate the historical convergence proof, but no separate session is assigned solely to provenance.

## O1. Opportunity-cost comparison

The residual simple-IPS positive-rates/noisy-East problem remains the strongest identified reserve. BABP continues to outrank it after the verified edge certificate and now a complete claimed convergence proof at `lambda=1/40`.

## Current first unresolved edge

**Correctness audit of E4 / `BABP-CONV-001`.**

There is no new development assignment until two independent reviews return. If the theorem survives, E5 becomes the first mathematical development edge.

## Routes demoted or excluded

- Bare outer ballistic bounds are not to be substituted for the statewise corrector in E4.
- DFP change-of-basis is not the current finite-seed route.
- Local patch-weight contraction is not active.
- Closed FA-1f routes remain closed.

## Revision note

Meeting 004 materially narrowed the programme. The statewise finite-window corrector was shown to control not only outer spreading but internal-gap persistence. This yields a complete claimed bridge to finite-seed convergence and, combined with verified `BABP-EDGE-001`, a claimed convergence theorem at `lambda=1/40`. Because this is substantially stronger than the audited edge claim, it is separately registered and awaits two independent hostile reviews.