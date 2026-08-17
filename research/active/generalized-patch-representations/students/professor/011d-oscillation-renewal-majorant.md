# 011d: oscillation renewal majorant and exact qualitative separation

Date: 2026-08-17

## 1. Why support weight is the right downstream norm

For a finite physical volume and a compatible typed configuration `zeta`, put

\[
\omega(\zeta)=|\operatorname{supp}\zeta|,
\qquad \omega(\emptyset)=0.
\]

For a physical function `f`, use the standard site-oscillation seminorm

\[
\operatorname{Osc}(f)
=\sum_i\delta_i f,
\]

where `delta_i f` is the maximal change in `f` when only site `i` is changed.

Every indicator tensor satisfies

\[
\operatorname{Osc}(H_\zeta)\le\omega(\zeta).
\]

Therefore 011a gives

\[
\boxed{
\operatorname{Osc}(P_tH_\xi)
\le (R_t\omega)(\xi).}
\tag{1.1}
\]

The weight `omega` is additive under disjoint unions and subadditive under compatible merges. That makes it possible to dominate the interacting patch skeleton by a collision-free **first-moment** patch tree without reverting to total-variation weights of complete branching configurations.

## 2. Finite local patch types

Assume for the moment a homogeneous finite-range replacement IPS, so there are finitely many local successful-record labels

\[
\alpha=(r_\alpha,\tau_\alpha),
\qquad
\Lambda_\alpha=\sum_s|a_{r_\alpha}^s(\tau_\alpha)|>0.
\]

Use two kinds of source-line patch starts:

- `I_a`, an incoming patch whose local active type after the merge is `a in E_*`;
- `O_alpha`, a patch starting at outgoing record `alpha`, whose hidden signed initial row is
  \[
  b_{O_\alpha}=\mathbf a_\alpha/\Lambda_\alpha.
  \]

For `I_a`, put `b_{I_a}=e_a`.

Let `K` be the exact empty-target signed transfer from Assignment 004.

## 3. Terminal survival and next-record kernels

For a patch type `u`, define its patch-averaged active terminal weight

\[
h_u(t)
=\sum_{b\in E_*}
\left|b_u e^{tK}e_b^T\right|.
\tag{3.1}
\]

For a possible next successful record `beta`, define

\[
\boxed{
k_{u\beta}(t)
=\Lambda_\beta
\left|b_u e^{tK}e_{r_\beta}^T\right|.}
\tag{3.2}
\]

This is exactly the unnormalized source-line patch variation density for ending at record `beta` after age `t`.

At record `beta`, the collision-free descendants are:

1. the source continuation patch `O_beta`;
2. one incoming child `I_{\tau_\beta(j)}` for each target site `j in supp(tau_beta)`.

Let `n_beta(v)` be this deterministic offspring multiplicity.

Define the finite matrix-valued renewal kernel

\[
\mathcal K_{uv}(t)
=\sum_\beta k_{u\beta}(t)n_\beta(v).
\tag{3.3}
\]

## 4. Collision-free patch-tree domination

Let `Z_u(t)` be the first-moment terminal support weight of the collision-free patch tree starting from patch type `u`, with every source-line factor averaged signed-first and then absolutized as in `R_t`.

Removing spatial merges and typed cemetery conflicts can only increase this positive first-moment envelope:

- a compatible merge replaces two descendant supports by their union, whose size is at most the sum;
- an incompatible merge sends the exact killed representation to cemetery and contributes zero;
- suppressing the incoming termination and allowing both lineages to continue independently removes possible cancellation and therefore majorizes patch variation.

Consequently, for an initial typed dual configuration `xi`,

\[
\boxed{
(R_t\omega)(\xi)
\le\sum_{i\in\operatorname{supp}\xi} Z_{I_{\xi(i)}}(t).}
\tag{4.1}
\]

The collision-free first moment satisfies the linear renewal system

\[
\boxed{
Z_u(t)
=h_u(t)
+\sum_v\int_0^t\mathcal K_{uv}(s)Z_v(t-s)ds.}
\tag{4.2}
\]

The linearity is the reason for using support/oscillation weight rather than total coefficient variation: offspring support weights add.

## 5. Exponential renewal criterion

For `gamma>=0` below the exponential decay rates of the local source-line transfer, define

\[
\widehat{\mathcal K}_\gamma
=\int_0^\infty e^{\gamma t}\mathcal K(t)dt.
\tag{5.1}
\]

Suppose there is a strictly positive vector `c`, `theta<1`, and `H<infty` such that

\[
\widehat{\mathcal K}_\gamma c\le\theta c,
\tag{5.2}
\]

and

\[
h_u(t)\le H c_u e^{-\gamma t}
\quad\text{for every }u,t.
\tag{5.3}
\]

Iterating (4.2) in the exponentially weighted sup norm gives

\[
\boxed{
Z_u(t)\le \frac{H}{1-\theta}c_u e^{-\gamma t}.}
\tag{5.4}
\]

Combining (1.1), (4.1), and (5.4),

\[
\boxed{
\operatorname{Osc}(P_tH_\xi)
\le
\frac{H}{1-\theta}e^{-\gamma t}
\sum_{i\in\operatorname{supp}\xi}c_{I_{\xi(i)}}.}
\tag{5.5}
\]

The estimate is independent of the finite volume because the collision-free tree uses only local record types. Standard finite propagation then transfers such a uniform local-observable bound to the infinite-volume semigroup whenever the usual construction hypotheses hold.

Thus the killed-patch cancellation mechanism yields a **checkable finite-dimensional sufficient criterion for volume-uniform exponential oscillation decay** without requiring pointwise bulk patch positivity.

## 6. Raw absolute-FK comparison

Define the raw absolute source-line transfer `M` by keeping the same diagonal as `K` and replacing every empty-target off-diagonal coefficient by its absolute value. For outgoing starts replace

\[
b_{O_\alpha}=\mathbf a_\alpha/\Lambda_\alpha
\]

by

\[
\bar b_{O_\alpha}=|\mathbf a_\alpha|/\Lambda_\alpha.
\]

Standard signed-semigroup domination gives

\[
|b_u e^{tK}e_r^T|
\le \bar b_u e^{tM}e_r^T.
\]

Hence the raw absolute renewal kernel `bar Kcal` dominates the patch-cancelled kernel entrywise:

\[
\boxed{
\mathcal K(t)\le\overline{\mathcal K}(t).}
\tag{6.1}
\]

The inequality can be strict because the left side retains cancellation among hidden source outcomes over a complete source-line patch.

## 7. Exact qualitative separation gate

This subsection is a **structural physical gate**, not a claimed published-model application.

Take the one-neighbour three-state Potts Metropolis local rule at

\[
z=1/2,\qquad q=1.
\]

The empty-target transfer is

\[
K=
\begin{pmatrix}
0&0&0\\
1/2&-5/2&1/2\\
1/2&1/2&-5/2
\end{pmatrix}.
\tag{7.1}
\]

There are four nonzero successful-record classes:

\[
(1;1),\quad(1;2),\quad(2;1),\quad(2;2),
\]

with outgoing rows and hazards

\[
(1;1):\ (1/2,1/2,-1/2),\quad\Lambda=3/2,
\]

\[
(1;2):\ (1/2,-1/2,-1),\quad\Lambda=2,
\]

and their color swaps.

For the active `2x2` block of `K`, the symmetric and antisymmetric decay rates are `2` and `3`. Exact integration of the absolute two-mode responses gives, for patch starts,

\[
I_1:\ (5/12,1/12),
\]

\[
O_{11}:\ (1/9,1/9),
\qquad
O_{12}:\ (7/48,11/48),
\]

with color-swapped values for `I_2,O_{21},O_{22}`.

Removing the outgoing hidden signs changes only

\[
O_{11},O_{22}:\quad
(1/9,1/9)\longmapsto(1/6,1/6).
\]

By color symmetry the Perron eigenvalue is read from a three-class quotient. The patch-cancelled integrated next-generation matrix is

\[
G=
\begin{pmatrix}
7/4&3/4&1\\
7/9&1/3&4/9\\
21/16&9/16&3/4
\end{pmatrix},
\]

with characteristic polynomial

\[
\lambda^2(6\lambda-17)/6,
\]

so

\[
\boxed{\rho(G)=17/6.}
\tag{7.2}
\]

The raw absolute quotient is

\[
\bar G=
\begin{pmatrix}
7/4&3/4&1\\
7/6&1/2&2/3\\
21/16&9/16&3/4
\end{pmatrix},
\]

with characteristic polynomial

\[
\lambda^2(\lambda-3),
\]

so

\[
\boxed{\rho(\bar G)=3.}
\tag{7.3}
\]

Now scale every **nonempty neighbour-dependent tensor coefficient** by

\[
\varepsilon=17/50
\]

while leaving empty-target coefficients fixed. At the physical-rate level this is

\[
c_\varepsilon^{x\to y}(\eta_N)
=(1-\varepsilon)c^{x\to y}(0)
+\varepsilon c^{x\to y}(\eta_N),
\tag{7.4}
\]

so all physical rates remain nonnegative for `0<=epsilon<=1`; at `17/50` the neighbour dependence is genuinely active.

Under this interpolation, `K` and normalized outgoing rows are unchanged, every successful-record hazard scales by `epsilon`, and therefore both integrated next-generation matrices scale linearly. Hence

\[
\boxed{
\rho(G_\varepsilon)
=\frac{17}{50}\frac{17}{6}
=\frac{289}{300}<1,}
\tag{7.5}
\]

whereas

\[
\boxed{
\rho(\bar G_\varepsilon)
=\frac{17}{50}\,3
=\frac{51}{50}>1.}
\tag{7.6}
\]

Because the local transfer has exponential tails and (7.5) is strict, continuity in the exponential tilt implies that (5.2) holds for some `gamma>0`. Thus the patch-cancelled renewal criterion gives exponential oscillation control in this exact physical interpolation while the corresponding raw absolute-FK first-moment criterion is supercritical at zero tilt.

This is the mandatory qualitative-gain gate. It proves that the new criterion is not algebraically equivalent to the raw absolute majorant.

It is deliberately **not** counted as a natural application result: the interaction-strength interpolation was chosen as a structural separation test after the two published base-model verdicts were already complete.

## 8. What remains for Assignment 011

Parts A--D now produce a real theorem beyond triangle inequality:

- a killed patch-variation kernel `R_t`;
- exact sandwich `|Q_t|<=R_t<=A_t`;
- submultiplicativity across time cuts;
- a local finite-type renewal criterion controlling physical oscillation;
- an exact physical coefficient family where that criterion is subcritical while the raw absolute criterion is not.

The remaining decision is contribution status after the required prior-work sanity check. Standard renewal, branching, oscillation and signed-semigroup domination ingredients are not themselves novelty claims.