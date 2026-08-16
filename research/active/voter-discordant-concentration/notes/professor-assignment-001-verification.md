# Professor verification: corrected discordance concentration target and four-walk obstruction

Date: 2026-08-16

Source under review:

- `students/student-d/001-sharp-concentration-reduction.md`, commit `fe88c7d`;
- Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), especially Theorems 1.2--1.3, Eq. (1.9), and Section 5.

## 1. Source statement and very-small-time correction

The published/arXiv-v2 source states Eq. (1.9) for **every** sequence `t_n` with `t_n/n -> 0` and every `C_n -> infinity`; the displayed statement contains no condition `t_n -> infinity`, `t_n >= 1`, or `inf_n t_n>0`. Thus sequences with `t_n -> 0` are literally included.

Fix a simple `d`-regular graph, `d>=3`, and Bernoulli(`u`) initial opinions. Write

$$
a=u(1-u),\qquad m=dn/2,
$$

and let `I_e` be the initial discordance indicator of edge `e`. Then

$$
\operatorname{Var}(I_e)=2a(1-2a).
$$

If two distinct edges share one endpoint,

$$
\mathbf E[I_eI_f]=a,
\qquad
\operatorname{Cov}(I_e,I_f)=a(1-4a),
$$

while disjoint edges are independent. Since there are `m` edges and `n binom(d,2)` unordered adjacent-edge pairs,

$$
\operatorname{Var}(D_0)
=nd\,a[d-(4d-2)a],
$$

and hence

$$
\boxed{
\operatorname{Var}(\mathcal D_0)
=\frac{4a[d-(4d-2)a]}{dn}.
}
$$

The coefficient is strictly positive for `u in (0,1)`. The centered edge variables have a dependency graph of bounded degree, so their fourth moment is `O_d(n^2)`; Paley--Zygmund applied to the squared centered sum gives constants `c_1,c_2>0` such that

$$
\mathbf P_u^G\left(
|\mathcal D_0-\mathbf E_u\mathcal D_0|\ge c_1n^{-1/2}
\right)\ge c_2
$$

uniformly over every simple `d`-regular graph.

Take

$$
t_n=n^{-3},\qquad C_n=\log n.
$$

The total voter-clock rate is `n`, so the no-ring event has probability

$$
e^{-nt_n}=e^{-n^{-2}}\to1.
$$

Also every normalized jump has absolute size at most `2/n`, whence `|L\mathcal D|<=2` and

$$
|\mathbf E\mathcal D_{t_n}-\mathbf E\mathcal D_0|\le2t_n.
$$

But

$$
C_n\sqrt{t_n/n}=\frac{\log n}{n^2}=o(n^{-1/2}).
$$

Therefore the probability in literal Eq. (1.9) stays bounded away from zero. The source's open statement is false as written.

A natural corrected all-sublinear target is

$$
\mathbf P_u^G\left(
|\mathcal D_{t_n}-\mathbf E_u^G\mathcal D_{t_n}|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)\xrightarrow{\mathbb P}0,
$$

for every `t_n=o(n)` and `C_n->infinity`. Equivalently use `n^{-1/2}+sqrt(t_n/n)`. This correction is mathematically necessary at small times; it is not yet proved sufficient throughout `t=o(n)`.

## 2. Generator and bracket

For configuration `eta`, let `k_x` be the number of neighbours of `x` disagreeing with `x`. Vertex `x` flips at rate `k_x/d`; on a flip,

$$
D(\eta^x)-D(\eta)=d-2k_x.
$$

Hence

$$
\boxed{
LD=\sum_x\frac{k_x}{d}(d-2k_x).
}
$$

With

$$
W=\sum_xk_x(d-k_x),
$$

this is `LD=(2/d)W-2D`. For `\mathcal D=D/m`, Dynkin's formula gives

$$
\mathcal D_t=\mathcal D_0+M_t+\int_0^t h(\eta_s)\,ds,
\qquad h=L\mathcal D.
$$

The predictable bracket satisfies exactly

$$
\frac d{dt}\langle M\rangle_t
=\frac{4}{d^3n^2}
\sum_xk_x(d-2k_x)^2
\le\frac4n.
$$

Therefore

$$
\mathbf E[(M_t-M_0)^2]\le\frac{4t}{n}
$$

on every fixed `d`-regular graph. The martingale part already has the desired dynamical scale.

## 3. Local quadratic drift and four-walk covariance

With spins `sigma_x=2eta(x)-1`, direct algebra gives

$$
\mathcal D
=\frac12-\frac1{dn}\sum_{\{x,y\}\in E}\sigma_x\sigma_y
$$

and

$$
h(\sigma)
=-\frac1d
+\frac{2}{dn}\sum_{\{x,y\}\in E}\sigma_x\sigma_y
-\frac{2}{d^2n}
\sum_x\sum_{\{y,z\}\subset N(x)}\sigma_y\sigma_z.
$$

Thus the centered drift is a spatial average of centered two-spin observables supported on edges and length-two wedges. Its integrated variance is exactly a signed double sum of two-time covariances.

For a two-spin observable at time `s` and another at time `r<=s`, the common graphical representation starts two backward lineages at time `s`, adds two more at time `r`, and coalesces all active lineages to time zero. If `Pi` is the partition of the four labels by common ancestor and `mu=2u-1`, then

$$
\mathbf E[Z_q(s)Z_{q'}(r)]
=\mathbf E_{\rm CRW}[\mu^{N_{\rm odd}(\Pi)}].
$$

Subtracting the two pair expectations gives the exact covariance kernel. Generic disjoint pair supports genuinely require four labels; cross meetings are exactly what couple the two pair families. At `u=1/2`, only even-block final partitions contribute, which makes this the cleanest first case for a signed-cancellation attack.

Consequently the sufficient estimate

$$
\mathbf E_u^G\left[
\left(\int_0^t(h(\eta_s)-\mathbf E h(\eta_s))\,ds\right)^2
\right]
\lesssim_{\mathbb P}\frac tn
$$

for `1<=t=o(n)` would imply the corrected theorem by the initial variance, bracket bound, and Chebyshev.

## 4. Section 5 method: what is and is not ruled out

The source's Section 5 proof samples `K` edges, resolves the empirical density with a Chernoff error of order `K^{-1/2}`, and removes every sampled edge whose dual pair interacts with another sampled pair. For `x=t/n`, a pair of sampled dual families interacts with probability `O(x)` in the relevant sublinear regime. Thus the expected bad-edge fraction in this discard-at-unit-cost architecture is of order `Kx`.

To resolve an error `delta`, the visible requirements are

$$
K\delta^2\to\infty,
\qquad
Kx=o(\delta).
$$

Balancing `K^{-1/2}` and `Kx` gives the characteristic error scale

$$
x^{1/3}.
$$

At the desired `delta=C\sqrt{x}`, the two requirements are incompatible for arbitrary `C_n->infinity` and arbitrary `x_n->0`. Therefore the **sample-and-discard interacting families at unit cost** architecture cannot by routine parameter tuning reach the sharp scale.

This is not a theorem that every refinement of the paper's weak-dependence ideas fails. A proof that evaluates the signed contribution of interacting four-walk families rather than deleting them would be a qualitatively different use of the same duality and remains viable.

## 5. Additional reduction for the next block

There is a potentially simpler equivalent route to the sharp variance scale. Put

$$
V(t)=\operatorname{Var}_u^G(\mathcal D_t).
$$

For any finite-state Markov chain,

$$
V'(t)
=2\operatorname{Cov}_u^G(\mathcal D_t,L\mathcal D_t)
+\mathbf E_u^G\Gamma(\mathcal D)(\eta_t),
$$

where

$$
\Gamma(f)=L(f^2)-2fLf.
$$

The bracket computation gives

$$
\mathbf E\Gamma(\mathcal D)(\eta_t)\le4/n.
$$

Therefore a uniform bound

$$
\operatorname{Cov}_u^G(\mathcal D_t,L\mathcal D_t)\le C/n
$$

through `t=o(n)` would immediately yield

$$
V(t)\lesssim\frac{1+t}{n}.
$$

This same-time covariance is again a signed edge/wedge four-spin sum, but avoids the double time integral and staggered dual start. It is the first structural calculation to test before committing to the harder integrated-drift estimate.

## 6. Judgment

Assignment 001 materially narrows the programme. The literal published open statement is refuted at very small times, the corrected scale is explicit, the martingale part is completely controlled, and the remaining issue is localized to a signed four-walk correlation problem. The published discard-interactions proof cannot reach that scale by a routine quantitative extension.

The programme should continue for one bounded structural cancellation block. It should not pursue incremental extensions of the Section 5 polynomial window.
