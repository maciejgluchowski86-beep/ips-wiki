# Proof spine

## Main target

Prove the corrected sharp concentration theorem for the discordant-edge density in the voter model on random `d`-regular graphs:

$$
\mathbf P_u^G\left(
|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)\xrightarrow{\mathbb P}0
$$

for fixed `d>=3`, `u in (0,1)`, every `t_n=o(n)`, and every `C_n->infinity`.

For `t_n->infinity`, this is the `sqrt(t_n/n)` scale intended by Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), Eq. (1.9).

## E0. Source correction

Literal Eq. (1.9) quantifies over every `t_n=o(n)` and hence includes `t_n->0`. Bernoulli initial conditions already have variance

$$
\operatorname{Var}(\mathcal D_0)
=\frac{4u(1-u)[d-(4d-2)u(1-u)]}{dn}.
$$

The choice

$$
t_n=n^{-3},\qquad C_n=\log n
$$

is a counterexample to the displayed source statement: with probability tending to one no clock rings, while the threshold is `(log n)/n^2=o(n^{-1/2})`.

**Status:** independently Professor-checked mathematical correction. Not yet promoted to a stable project claim.

## E1. Exact semimartingale and martingale scale

For a fixed `d`-regular graph, let `D` be the number of discordant edges and `k_x` the number of disagreeing neighbours of `x`. Then

$$
LD=\sum_x\frac{k_x}{d}(d-2k_x).
$$

For `\mathcal D=D/(dn/2)`,

$$
\mathcal D_t=\mathcal D_0+M_t+\int_0^tL\mathcal D(\eta_s)\,ds,
$$

and

$$
\frac d{dt}\langle M\rangle_t
=\frac{4}{d^3n^2}\sum_xk_x(d-2k_x)^2
\le\frac4n.
$$

Thus

$$
\mathbf E[M_t^2]\le4t/n.
$$

**Status:** verified for proof-spine use. The martingale is not the obstruction.

## E2. Local quadratic drift

With spins `sigma_x=2eta(x)-1`,

$$
\mathcal D
=\frac12-\frac1{dn}\sum_{\{x,y\}\in E}\sigma_x\sigma_y,
$$

and

$$
L\mathcal D
=-\frac1d
+\frac{2}{dn}\sum_{\{x,y\}\in E}\sigma_x\sigma_y
-\frac{2}{d^2n}
\sum_x\sum_{\{y,z\}\subset N(x)}\sigma_y\sigma_z.
$$

Hence the drift is a signed spatial average of two-spin observables on edges and length-two wedges.

**Status:** exact.

## E3. Four-lineage covariance representation

For two two-spin observables at times `s>=r`, voter duality gives an exact staggered system of four coalescing ancestral lineages. If `Pi` is the final partition of four labels by common ancestor and `mu=2u-1`, then

$$
\mathbf E[Z_q(s)Z_{q'}(r)]
=\mathbf E_{\rm CRW}[\mu^{N_{\rm odd}(\Pi)}].
$$

Subtracting the separate pair expectations gives the covariance. Generic disjoint supports require all four labels. Cross meetings are exactly the dependence events.

At `u=1/2`, only final partitions with all blocks of even size contribute.

**Status:** exact dual reduction.

## E4. Sufficient integrated-drift estimate

Centering the semimartingale gives

$$
X_t=X_0+M_t+
\int_0^t\widetilde h_s\,ds.
$$

Therefore the corrected theorem follows from

$$
\boxed{
\mathbf E_u^G\left[
\left(\int_0^t\widetilde h_s\,ds\right)^2
\right]
=O_{\mathbb P}(t/n)
}
$$

uniformly for `1<=t=o(n)`, together with the initial `O(1/n)` variance and E1.

**Status:** sufficient target, unproved.

## E5. Variance-differential route

A potentially simpler route avoids the double time integral. Let

$$
V(t)=\operatorname{Var}_u^G(\mathcal D_t).
$$

Then

$$
V'(t)
=2\operatorname{Cov}_u^G(\mathcal D_t,L\mathcal D_t)
+\mathbf E_u^G\Gamma(\mathcal D)(\eta_t),
$$

with

$$
\mathbf E_u^G\Gamma(\mathcal D)(\eta_t)\le4/n.
$$

Thus it is enough to prove

$$
\boxed{
\operatorname{Cov}_u^G(\mathcal D_t,L\mathcal D_t)\le C/n
}
$$

through `t=o(n)`. This covariance is a signed same-time edge/wedge four-spin sum and has a simultaneous four-walk representation.

**Status:** current first structural test.

## E6. Why the published discard method does not reach the sharp scale routinely

Section 5 samples `K` edges and discards sampled families that interact with another sampled family. At target error `delta`, the visible architecture pays

$$
K^{-1/2}
$$

for sampling and approximately

$$
K(t/n)
$$

for the fraction of interacting sampled families. Balancing gives the characteristic scale `(t/n)^{1/3}`.

At `delta=C sqrt(t/n)`, no choice of `K` can simultaneously make the sampling error and unit-cost deletion error negligible for arbitrary `C_n->infinity` and arbitrary `t_n/n->0`.

**Status:** structural obstruction to routine tuning of the sample-and-discard-at-unit-cost implementation. It does not rule out a signed four-walk refinement of the duality method.

## Current first unresolved edge

At `u=1/2`, expand

$$
\operatorname{Cov}(\mathcal D_t,L\mathcal D_t)
$$

as the full signed edge/wedge four-walk sum and determine whether the incidence coefficients cancel the leading cross-meeting contribution, or whether a Poisson/corrector observable removes it.

If the same-time route fails for a precise structural reason, return to E4 only if time integration creates a new cancellation not visible in E5.

**Owner:** Graduate Student D, assignment `students/student-d/assignment-002.md`.

## Novelty and opportunity-cost guardrail

Do not optimize the exponent in the published moderate-time window. A larger polynomial window is diagnostic only.

Meeting 001 pre-commits to reassessment if assignment 002 produces only absolute cross-meeting estimates with excessive time growth and no signed cancellation, corrector, or other structural mechanism.
