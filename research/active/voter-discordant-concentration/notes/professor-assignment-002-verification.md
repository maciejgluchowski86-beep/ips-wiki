# Professor verification: genealogical variance inequality and sharp concentration

Date: 2026-08-16

Source under review:

- `students/student-d/002-four-walk-cancellation.md`, commit `e73fd25`;
- Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), especially (2.1), (5.5)--(5.8).

This note records an independent Professor reconstruction of the load-bearing argument. It is **not** an independent external audit and therefore does not make the central claim verified.

## 1. Conditional genealogy representation

Fix a finite simple `d`-regular graph `G=(V,E)`, `|V|=n`, `m=dn/2`, and time `t>=0`. Let `H_t` be the voter Harris arrows in `[0,t]`, excluding the i.i.d. Bernoulli(`u`) initial labels. For each `x in V`, let `a_t(x)` be the ancestor at time zero followed backward through the arrows.

Conditional on `H_t`,

$$
\eta_t(x)=\xi_{a_t(x)},
$$

where the initial labels `(xi_v)` are independent Bernoulli(`u`). Thus the nonempty sets

$$
C_v(t)=\{x:a_t(x)=v\}
$$

are ancestral clusters carrying independent labels.

For distinct ancestors `v,w`, let `N_vw` be the number of original graph edges joining `C_v` to `C_w`, and let

$$
J_t=\#\{\{x,y\}\in E:a_t(x)=a_t(y)\}
$$

be the number of original edges internal to ancestral clusters. If `p=2u(1-u)`, then

$$
D_t=\sum_{v<w}N_{vw}\mathbf 1_{\{\xi_v\ne\xi_w\}},
\qquad
\mathbf E[D_t/m\mid H_t]=p\left(1-\frac{J_t}{m}\right).
$$

I find no conditioning gap here: the genealogy is measurable from the Harris arrows and is independent of the initial Bernoulli labels.

## 2. Conditional variance bound

For unordered ancestor pairs `r={v,w}`, put `I_r=1_{xi_v != xi_w}` and weight `N_r=N_vw`. If `r` and `s` are disjoint, `I_r` and `I_s` are independent. For intersecting pairs, including `r=s`,

$$
|\operatorname{Cov}(I_r,I_s)|\le\frac14.
$$

Hence

$$
\operatorname{Var}(D_t\mid H_t)
\le\frac14\sum_{r,s:r\cap s\ne\varnothing}N_rN_s.
$$

For each ancestor `v`, define

$$
S_v=\sum_{w\ne v}N_{vw}.
$$

Every ordered intersecting pair `(r,s)` is counted at least once in `sum_v S_v^2` (and a diagonal pair twice), so

$$
\sum_{r,s:r\cap s\ne\varnothing}N_rN_s\le\sum_vS_v^2.
$$

Since `S_v` is the number of original edges leaving `C_v`,

$$
S_v\le d|C_v|.
$$

After division by `m^2=d^2n^2/4`,

$$
\mathbf E[\operatorname{Var}(\mathcal D_t\mid H_t)]
\le\frac1{n^2}\mathbf E\sum_v|C_v(t)|^2.
$$

But

$$
\sum_v|C_v(t)|^2
=\sum_{x,y}\mathbf 1_{\{a_t(x)=a_t(y)\}}.
$$

For fixed `x,y`, the two backward voter lineages evolve as independent rate-one continuous-time simple random walks until their first meeting, after which they coalesce. Consequently

$$
\mathbf P(a_t(x)=a_t(y))
=\mathbf P_{x,y}(\tau_{\rm meet}\le t).
$$

Averaging `x,y` independently uniformly gives

$$
\boxed{
\mathbf E[\operatorname{Var}(\mathcal D_t\mid H_t)]
\le q_t,
\qquad
q_t:=\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
}
$$

The source defines `tau_meet=inf{s>=0:X_s=Y_s}`, so the diagonal mass `1/n` at time zero is included, exactly as required by the cluster-square identity.

## 3. Conditional-mean variance and the four-family coupling

From the conditional mean,

$$
\operatorname{Var}(\mathbf E[\mathcal D_t\mid H_t])
=\frac{p^2}{m^2}\operatorname{Var}(J_t).
$$

Write

$$
Y_e=\mathbf 1_{\{a_t(e^-)=a_t(e^+)\}},
\qquad J_t=\sum_{e\in E}Y_e.
$$

For two edges `e,f`, consider the two ancestral lineages from `e` and the two from `f`. Couple their joint Harris evolution to two **independent** two-lineage systems until the first meeting between a lineage from the `e` family and a lineage from the `f` family. Before this first cross-family meeting the two family histories are independent and identical to their marginals. Therefore, if `H_{e,f}` is the first-cross-meeting event,

$$
|\operatorname{Cov}(Y_e,Y_f)|\le \mathbf P(H_{e,f}).
$$

A subtle point is within-family coalescence. It does not invalidate the comparison with the source's four independent walks: one may construct the two isolated pairs from four independent walk paths and identify the two paths in a family after their meeting. Any cross-family meeting in the resulting coalescing-family construction is contained in the event that one of the four original independent cross pairs meets. Thus the source interaction event from (5.5) is an admissible upper bound.

A uniform unoriented edge with an independent fair orientation has law

$$
\nu(x,y)=\pi(x)d^{-1}\mathbf 1_{\{x\sim y\}}.
$$

The cross-interaction event is orientation invariant. Hence averaging over the ordered pair `(e,f)` yields

$$
\frac{1}{m^2}\operatorname{Var}(J_t)
\le \mathbf P_{\nu\otimes\nu}^G(\tau^{e,f}\le t).
$$

Equation (5.6) of the source states on every regular graph

$$
\mathbf P_{\nu\otimes\nu}^G(\tau^{e,f}\le t)
\le4q_t.
$$

Since `p<=1/2`,

$$
\boxed{
\operatorname{Var}(\mathbf E[\mathcal D_t\mid H_t])
\le4p^2q_t\le q_t.
}
$$

## 4. Deterministic graph theorem

Total variance now gives

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)
}
$$

for every finite simple `d`-regular graph, every `u in (0,1)`, and every `t>=0`.

This also passes the `t=0` sanity check: `q_0=1/n`, while the exact Bernoulli initial variance is of order `1/n`.

## 5. Random-regular source interface

The source's (5.7) is exactly

$$
q_t=O(t/n)
$$

with high probability for sublinear `t`, derived from the Aldous--Brown short-time hitting inequality (5.8), the stationary mean meeting time `Theta(n)`, and a spectral gap bounded away from zero with high probability.

There is a small-time wording issue already noticed by Student D: because `q_0=1/n`, the literal `O(t/n)` cannot be uniform as `t downarrow 0`. The proof interface needed here is clean:

- for deterministic `1<=t_n=o(n)`, (5.8) on the standard high-probability graph event gives `q_{t_n}<=C t_n/n`;
- for `0<=t_n<1`, monotonicity gives `q_{t_n}<=q_1<=C/n` on the same type of graph event.

Therefore

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}\left(\frac{1+t_n}{n}\right)
$$

for every deterministic `t_n=o(n)`, and in the regime `t_n>=1`,

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)=O_{\mathbb P}(t_n/n).
$$

Chebyshev gives the corrected all-sublinear concentration theorem and the original source scale whenever `t_n>=1`.

## 6. Professor verdict and audit boundary

I find the proof internally coherent and the external source interface correct. In particular, the genealogy-first decomposition removes the time integral and sample-size multiplier that blocked the earlier routes.

The central theorem is therefore strong enough to enter **claimed** status and independent audit. It is not yet `verified`: the protocol requires genuinely independent hostile correctness reviews, and publication-level novelty/closest-prior-work checking remains pending.

Load-bearing points for the independent auditors are:

1. the conditional cut-variance combinatorics;
2. the exact cluster-square/meeting identity;
3. the coupling behind `|Cov(Y_e,Y_f)|<=P(H_{e,f})`, especially within-family coalescence versus the source's four independent walks;
4. oriented/unoriented edge averaging;
5. the sequence-wise quenched-in-probability use of source (5.7)/(5.8);
6. the claim boundary for small times.
