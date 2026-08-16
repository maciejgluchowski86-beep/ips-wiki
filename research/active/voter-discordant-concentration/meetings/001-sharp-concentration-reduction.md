# Group meeting 001: source correction and four-walk reduction

Date: 2026-08-16

Professor review of Graduate Student D assignment 001:

- `students/student-d/001-sharp-concentration-reduction.md`, commit `fe88c7d`;
- Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), Theorems 1.2--1.3, Eq. (1.9), and Section 5;
- independent Professor reconstruction `notes/professor-assignment-001-verification.md`.

state_narrowed: yes

Evidence pointer: Student D's report and the Professor verification note above, with the source-level statement checked against arXiv v2/published-version content.

## Source correction

The literal open statement Eq. (1.9) is false as written.

The source quantifies over every `t_n` with `t_n/n -> 0` and every `C_n -> infinity`, without requiring `t_n` to stay bounded away from zero. For Bernoulli(`u`) initial opinions on any simple fixed `d`-regular graph,

$$
\operatorname{Var}(\mathcal D_0)
=\frac{4u(1-u)\,[d-(4d-2)u(1-u)]}{dn},
$$

with a strictly positive coefficient for `u in (0,1)`. A bounded-dependency fourth-moment estimate gives a uniform positive probability of fluctuations of order `n^{-1/2}`.

Taking

$$
t_n=n^{-3},\qquad C_n=\log n
$$

leaves the process unchanged with probability tending to one, while the Eq. (1.9) threshold is `(log n)/n^2=o(n^{-1/2})`. Hence the displayed conjecture fails.

The programme target is replaced by the corrected scale

$$
\boxed{
\mathbf P_u^G\left(
|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)\xrightarrow{\mathbb P}0
}
$$

for every `t_n=o(n)` and every `C_n->infinity`.

Equivalently use `n^{-1/2}+sqrt(t_n/n)`. For `t_n` bounded away from zero this is equivalent up to constants to the scale intended in Eq. (1.9); for `t_n->infinity` it becomes exactly `sqrt(t_n/n)`.

This is a genuine correction of the source formulation, but it is not yet being promoted to a stable project claim or manuscript result. The substantive target is the corrected theorem.

## Exact dynamical reduction

For a fixed `d`-regular graph and `k_x` the number of disagreeing neighbours of `x`,

$$
LD=\sum_x\frac{k_x}{d}(d-2k_x).
$$

For normalized discordance `\mathcal D=D/(dn/2)`, Dynkin's martingale has bracket

$$
\frac d{dt}\langle M\rangle_t
=\frac{4}{d^3n^2}\sum_xk_x(d-2k_x)^2
\le\frac4n.
$$

Thus the martingale already has variance at most `4t/n` on every graph. It is not the obstruction.

Writing spins `sigma_x=2eta(x)-1`, the drift is exactly a signed spatial average of two-spin observables on edges and length-two wedges:

$$
h(\sigma)
=-\frac1d
+\frac{2}{dn}\sum_{\{x,y\}\in E}\sigma_x\sigma_y
-\frac{2}{d^2n}
\sum_x\sum_{\{y,z\}\subset N(x)}\sigma_y\sigma_z.
$$

Therefore the remaining variance problem is a signed covariance sum. Its exact two-time voter-dual representation uses four coalescing ancestral lineages in the generic case. At `u=1/2`, only even-block final partitions contribute, making the symmetric case the cleanest cancellation test.

A sufficient estimate is

$$
\mathbf E_u^G\left[
\left(\int_0^t(h(\eta_s)-\mathbf Eh(\eta_s))\,ds\right)^2
\right]
=O_{\mathbb P}(t/n)
$$

uniformly for `1<=t=o(n)`.

The Professor also records a potentially simpler route. If

$$
V(t)=\operatorname{Var}_u^G(\mathcal D_t),
$$

then

$$
V'(t)=2\operatorname{Cov}_u^G(\mathcal D_t,L\mathcal D_t)
+\mathbf E_u^G\Gamma(\mathcal D)(\eta_t),
$$

with the carré-du-champ term at most `4/n`. Hence the same-time bound

$$
\operatorname{Cov}_u^G(\mathcal D_t,L\mathcal D_t)\le C/n
$$

would immediately give the corrected variance scale. This replaces the staggered four-walk problem by a simultaneous four-walk signed sum and is the first calculation to test next.

## Published weak-dependence method

Section 5 samples `K` edges and discards sampled edge-families that interact with another sampled family. At shrinking target error `delta`, the visible requirements of this architecture are

$$
K\delta^2\to\infty
$$

from sampling concentration, and

$$
K(t/n)=o(\delta)
$$

if interacting families are still discarded at unit cost. Balancing the corresponding errors gives the characteristic scale `(t/n)^{1/3}`.

This is a structural limitation of the **sample-and-discard-at-unit-cost implementation**, not a theorem that all uses of the source's duality fail. Reaching the corrected sharp scale requires evaluating/cancelling the contribution of interacting four-walk families, or using a different corrector/martingale decomposition.

## Direction decision

**continue for one bounded structural cancellation block.**

The programme has not merely extended a time exponent. It has corrected the literal open formulation and reduced the corrected theorem to a concrete signed four-lineage problem. There is enough structure for one further high-value attack.

The next assignment must not tune `K_n`, improve the polynomial window, or replace one discard threshold by another. It must test whether the signed edge/wedge coefficients produce the cancellation needed for the `O((1+t)/n)` variance scale.

### Pre-committed opportunity-cost condition

After the next substantial block, if the best available estimates still come only from taking absolute values of cross-meeting probabilities and therefore grow with `t` too strongly to yield `O((1+t)/n)`, with no new cancellation, Poisson-equation, or variance-differential mechanism, the programme will be reassessed against the remaining opportunity-cost candidates rather than continued by incremental Section 5 refinements.

Graduate Student D remains the active persistent student.

No stable project claim is registered at this meeting.
