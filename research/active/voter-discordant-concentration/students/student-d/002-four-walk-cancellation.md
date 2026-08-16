# Student D 002: signed four-walk cancellation test

## Executive conclusion

The corrected sharp concentration theorem can be proved without controlling the integrated drift and without establishing a sign for the variance-differential covariance.

The key structural mechanism is to condition on the entire voter genealogy at the observation time. Conditional on the Harris arrows, the configuration at time `t` is obtained by assigning independent Bernoulli(`u`) labels to the ancestral clusters. The discordant-edge count is therefore a weighted cut statistic on the random quotient multigraph of ancestral clusters. Its conditional variance is controlled by the second moment of cluster sizes. The variance of its conditional mean is controlled by the number of original edges whose two ancestral lineages have coalesced. Both quantities reduce to the meeting probability of two stationary random walks. The published estimates (5.6)--(5.7) already give that meeting probability on the required `t=o(n)` scale.

This yields the deterministic-graph inequality

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_t)
\le 2\,\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)
}
\tag{0.1}
$$

for every finite simple `d`-regular graph, every `u\in(0,1)`, and every `t\ge0`, where `pi` is uniform on the vertices and the probability on the right is for two independent continuous-time simple random walks.

Avena--Baldasso--Hazra--den Hollander--Quattropani, equations (5.6)--(5.7), prove with high environment probability that

$$
\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)
=O(t/n)
\qquad (t=o(n)).
\tag{0.2}
$$

For `0\le t\le1`, monotonicity and (0.2) at `t=1` give `O(1/n)`. Consequently, for every deterministic sequence `t_n=o(n)`,

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}\left(\frac{1+t_n}{n}\right).
}
\tag{0.3}
$$

Chebyshev therefore proves the corrected target from Meeting 001: for every `C_n\to\infty`,

$$
\mathbf P_u^G\left(
\left|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n\right|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)
\xrightarrow{\mathbb P}0.
\tag{0.4}
$$

Moreover, whenever `t_n\ge1` and `t_n=o(n)`, (0.3) improves to `O_{\mathbb P}(t_n/n)`, which proves the original source scale `C_n\sqrt{t_n/n}` in that regime. Thus the only defect in the literal source Eq. (1.9) is the already identified very-small-time omission.

The assignment's same-time signed four-walk sum is still derived below. It has a compact adjacency/Laplacian form, but I did not prove the direct sign bound `Cov(Dcal,LDcal)<=C/n`. That route is no longer load-bearing because the genealogical conditional-variance argument closes the target directly.

## 1. Exact signed variance-differential expansion

Fix a simple `d`-regular graph `G=(V,E)` with `|V|=n`, and write

$$
S_{ab}(\sigma)=\sigma_a\sigma_b.
$$

Let

$$
\mathcal W
=\{(x;\{y,z\}):x\in V,\ y,z\in N(x),\ y\ne z\}/(y,z)\sim(z,y)
$$

be the set of centered length-two wedges. Thus `|W|=n binom(d,2)`, and the same endpoint pair may occur with multiplicity when it has more than one common neighbour.

The identities from assignment 001 are

$$
\mathcal D
=\frac12-\frac1{dn}\sum_{e=\{a,b\}\in E}S_{ab},
\tag{1.1}
$$

and

$$
L\mathcal D
=-\frac1d
+\frac{2}{dn}\sum_{f=\{c,d\}\in E}S_{cd}
-\frac{2}{d^2n}
\sum_{w=(x;\{c,d\})\in\mathcal W}S_{cd}.
\tag{1.2}
$$

For pair supports `q={a,b}`, `r={c,d}`, put

$$
K_t(q,r)
=\operatorname{Cov}_{1/2}^G(S_{ab}(\eta_t),S_{cd}(\eta_t)).
$$

Constants in (1.1)--(1.2) drop from covariance, so

$$
\boxed{
\operatorname{Cov}_{1/2}^G(\mathcal D_t,L\mathcal D_t)
=-\frac{2}{d^2n^2}\sum_{e,f\in E}K_t(e,f)
+\frac{2}{d^3n^2}\sum_{e\in E}\sum_{w\in\mathcal W}K_t(e,\partial w).
}
\tag{1.3}
$$

Here `partial w={c,d}` denotes the two endpoints of the wedge, retaining wedge multiplicity in the second sum.

### 1.1 Simultaneous four-lineage formula at `u=1/2`

For four labelled starting vertices `a,b,c,d`, run the simultaneous backward coalescing system from time `t` to time zero, and let `Pi_t` be the partition of the labels according to their common ancestor at time zero. For i.i.d. symmetric initial spins, a product has nonzero expectation exactly when every initial spin appears with even multiplicity. Hence

$$
\mathbf E_{1/2}^G[S_{ab}(\eta_t)S_{cd}(\eta_t)]
=\mathbf P_{\rm CRW}^G(\text{every block of }\Pi_t\text{ has even size}).
\tag{1.4}
$$

If `a,b,c,d` are distinct, this is exactly

$$
\begin{aligned}
&\mathbf P(\Pi_t=ab\mid cd)
+\mathbf P(\Pi_t=ac\mid bd)
+\mathbf P(\Pi_t=ad\mid bc)\\
&\qquad
+\mathbf P(\Pi_t=abcd),
\end{aligned}
\tag{1.5}
$$

where, for example, `ab|cd` means exactly the two blocks `{a,b}` and `{c,d}`, and `abcd` means one four-label block. Also

$$
\mathbf E_{1/2}^G[S_{ab}(\eta_t)]
=\mathbf P_{\rm CRW}^G(a\sim b\text{ by time }t).
\tag{1.6}
$$

Therefore, for four distinct labels,

$$
\boxed{
\begin{aligned}
K_t((a,b),(c,d))
={}&\mathbf P(ab\mid cd)+\mathbf P(ac\mid bd)+\mathbf P(ad\mid bc)\\
&+\mathbf P(abcd)
-\mathbf P(a\sim b)\mathbf P(c\sim d).
\end{aligned}
}
\tag{1.7}
$$

When starting supports overlap, (1.4) is the clean formulation; equivalently one may use (1.7) with immediate identifications of coincident labels.

Thus (1.3) is the requested full signed global four-walk sum. No absolute cross-meeting bound has been inserted into it.

## 2. Incidence identity: adjacency/Laplacian form

Let `A` be the adjacency matrix, `P=A/d` the simple-random-walk transition matrix, and `Q=I-P` the normalized graph Laplacian. Since

$$
\sum_{\{x,y\}\in E}\sigma_x\sigma_y
=\frac12\sigma^T A\sigma,
$$

we can rewrite (1.1) as

$$
\boxed{
\mathcal D(\sigma)
=\frac1{2n}\sigma^TQ\sigma.
}
\tag{2.1}
$$

For the wedge sum,

$$
\sum_{x\in V}\sum_{\{y,z\}\subset N(x)}\sigma_y\sigma_z
=\frac12\sigma^T A^2\sigma-\frac{nd}{2}.
\tag{2.2}
$$

Substitution into (1.2) cancels the explicit constant and gives

$$
\boxed{
L\mathcal D(\sigma)
=\frac1n\sigma^T(P-P^2)\sigma
=\frac1n\sigma^TPQ\sigma
=\frac1n\sigma^T(Q-Q^2)\sigma.
}
\tag{2.3}
$$

This is an exact incidence cancellation: the edge and wedge coefficients are not arbitrary; together they form the Laplacian polynomial `PQ=Q-Q^2`. In particular the drift matrix annihilates the constant vector.

I did not find a general argument converting (2.3) into

$$
\operatorname{Cov}(\mathcal D_t,L\mathcal D_t)\le C/n.
$$

The obstacle is that `PQ` is not positive or negative semidefinite: on an adjacency eigenvector with transition eigenvalue `lambda`, it has eigenvalue `lambda(1-lambda)`, which changes sign when `lambda<0`. Thus a direct quadratic-form monotonicity argument is unavailable.

The next section gives a different structural decomposition that makes this same-time route unnecessary.

## 3. Genealogical quotient representation

Let `H_t` be the Harris graphical randomness in the time slab `[0,t]`, excluding the initial opinions. For every vertex `x`, let

$$
a_t(x)\in V
$$

be its ancestor at time zero obtained by following the voter arrows backward. For `v\in V`, define the ancestral cluster

$$
C_v(t)=\{x\in V:a_t(x)=v\}.
$$

The nonempty clusters form a partition of `V`.

Conditional on `H_t`, the voter state is

$$
\eta_t(x)=\xi_{a_t(x)},
\tag{3.1}
$$

where `(xi_v)_{v\in V}` are the independent Bernoulli(`u`) initial labels.

For distinct ancestors `v,w`, let

$$
N_{vw}(t)
=\#\{\{x,y\}\in E:a_t(x)=v,\ a_t(y)=w\}.
\tag{3.2}
$$

This is the edge multiplicity between clusters `C_v(t)` and `C_w(t)` in the ancestral quotient multigraph. Let

$$
J_t
=\#\{\{x,y\}\in E:a_t(x)=a_t(y)\}
\tag{3.3}
$$

be the number of original edges internal to ancestral clusters. Then

$$
\sum_{v<w}N_{vw}(t)=m-J_t,
\qquad m=dn/2.
\tag{3.4}
$$

For `v\ne w`, set

$$
I_{vw}=\mathbf1_{\{\xi_v\ne\xi_w\}}.
$$

The discordant-edge count has the exact conditional representation

$$
D_t=\sum_{v<w}N_{vw}(t)I_{vw}.
\tag{3.5}
$$

Put

$$
p=\mathbf E[I_{vw}]=2u(1-u)\le\frac12.
$$

Then

$$
\boxed{
\mathbf E_u^G[\mathcal D_t\mid H_t]
=p\left(1-\frac{J_t}{m}\right).
}
\tag{3.6}
$$

This is the key replacement for the integrated-drift decomposition.

## 4. Conditional variance is controlled by ancestral cluster sizes

For unordered distinct ancestor pairs `r={v,w}`, write `I_r=I_{vw}` and `N_r=N_{vw}`. If two pairs `r,s` are disjoint, then `I_r` and `I_s` depend on disjoint initial labels and hence are independent. If they intersect, their covariance is bounded in absolute value by `1/4`, because both are indicators. More explicitly, writing `a=u(1-u)`,

$$
\operatorname{Var}(I_{vw})=2a(1-2a),
$$

and for distinct `w,z`,

$$
\operatorname{Cov}(I_{vw},I_{vz})
=a(1-4a)=a(2u-1)^2\ge0.
\tag{4.1}
$$

Thus, conditional on `H_t`,

$$
\operatorname{Var}(D_t\mid H_t)
\le\frac14
\sum_{r,s:\,r\cap s\ne\varnothing}N_rN_s.
\tag{4.2}
$$

For an ancestor `v`, let

$$
S_v=\sum_{w\ne v}N_{vw}.
$$

Every ordered pair `(r,s)` with nonempty intersection is counted at least once in `sum_v S_v^2`, while an identical pair is merely counted twice, so

$$
\sum_{r,s:\,r\cap s\ne\varnothing}N_rN_s
\le\sum_vS_v^2.
\tag{4.3}
$$

Moreover `S_v` is the number of original graph edges leaving the cluster `C_v(t)`, hence

$$
S_v\le d|C_v(t)|.
\tag{4.4}
$$

Combining (4.2)--(4.4), dividing by `m^2`, and averaging over the graphical randomness gives

$$
\mathbf E\left[\operatorname{Var}(\mathcal D_t\mid H_t)\right]
\le\frac{d^2}{4m^2}\mathbf E\left[\sum_v|C_v(t)|^2\right]
=\frac1{n^2}\mathbf E\left[\sum_v|C_v(t)|^2\right].
\tag{4.5}
$$

Now

$$
\sum_v|C_v(t)|^2
=\sum_{x,y\in V}\mathbf1_{\{a_t(x)=a_t(y)\}}.
\tag{4.6}
$$

For fixed `x,y`, the event on the right is exactly that the two backward ancestral walks from `x,y` have met by time `t`. Hence, if `X,Y` are independent uniform vertices and `tau_meet` is the meeting time of two independent continuous-time simple random walks,

$$
\frac1{n^2}\mathbf E\left[\sum_v|C_v(t)|^2\right]
=\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
\tag{4.7}
$$

Therefore

$$
\boxed{
\mathbf E\left[\operatorname{Var}(\mathcal D_t\mid H_t)\right]
\le q_t,
\qquad
q_t:=\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
}
\tag{4.8}
$$

At `u=1/2` one can sharpen the conditional calculation: edge-cut indicators associated with two distinct quotient edges are pairwise uncorrelated even when the edges share one ancestral vertex. Consequently

$$
\operatorname{Var}_{1/2}(D_t\mid H_t)
=\frac14\sum_{v<w}N_{vw}(t)^2.
\tag{4.9}
$$

The coarser bound (4.8), however, already works uniformly for every `u\in(0,1)`.

## 5. Conditional-mean variance is a four-walk interaction term

By (3.6),

$$
\operatorname{Var}\left(\mathbf E[\mathcal D_t\mid H_t]\right)
=\frac{p^2}{m^2}\operatorname{Var}(J_t).
\tag{5.1}
$$

Write

$$
Y_e=\mathbf1_{\{a_t(e^-)=a_t(e^+)\}},
\qquad
J_t=\sum_{e\in E}Y_e.
\tag{5.2}
$$

Fix two edges `e,f`. Couple the four-lineage coalescing system to two independent two-lineage systems, one started from the endpoints of `e` and the other from the endpoints of `f`. Until the first cross-family meeting, these constructions agree. Let `H_{e,f}(t)` be the event that a cross-family meeting occurs before time `t`.

The marginal law of `Y_e` in the four-lineage system is exactly the law of the meeting indicator for the isolated pair from `e`, and similarly for `f`. The two isolated pair indicators are independent. Under the coupling, their product differs from `Y_eY_f` only on `H_{e,f}(t)`. Therefore

$$
\boxed{
|\operatorname{Cov}(Y_e,Y_f)|
\le \mathbf P(H_{e,f}(t)).
}
\tag{5.3}
$$

If the two edges share an endpoint, the right-hand side is one because the cross-interaction time is zero, so the same statement still holds.

A uniformly sampled unoriented edge with an independent uniform orientation has the distribution `nu` used by Avena--Baldasso--Hazra--den Hollander--Quattropani in Section 5:

$$
\nu(x,y)=\pi(x)\frac1d\mathbf1_{\{x\sim y\}}.
$$

Hence averaging (5.3) over all ordered edge pairs gives

$$
\frac1{m^2}\operatorname{Var}(J_t)
\le
\mathbf P_{\nu\otimes\nu}^G(\tau^{e,f}\le t),
\tag{5.4}
$$

where `tau^{e,f}` is precisely the cross-family interaction time in their equation (5.5). Their equation (5.6) gives on every regular graph

$$
\mathbf P_{\nu\otimes\nu}^G(\tau^{e,f}\le t)
\le4\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)
=4q_t.
\tag{5.5}
$$

Since `p\le1/2`, (5.1), (5.4), and (5.5) imply

$$
\boxed{
\operatorname{Var}\left(\mathbf E[\mathcal D_t\mid H_t]\right)
\le4p^2q_t\le q_t.
}
\tag{5.6}
$$

This is the only place a four-walk cross-interaction bound is used. Crucially, it appears once, with no time integration and no sampling multiplier.

## 6. Deterministic-graph variance theorem

The law of total variance, (4.8), and (5.6) give the promised bound.

### Proposition 6.1

For every finite simple `d`-regular graph `G`, every `u\in(0,1)`, and every `t\ge0`,

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
}
\tag{6.1}
$$

### Proof

By total variance,

$$
\operatorname{Var}(\mathcal D_t)
=
\mathbf E[\operatorname{Var}(\mathcal D_t\mid H_t)]
+
\operatorname{Var}(\mathbf E[\mathcal D_t\mid H_t]).
$$

Apply (4.8) and (5.6). `square`

This proposition is independent of random-regular geometry. The graph enters only through the stationary two-walk meeting probability.

## 7. Closing the corrected random-regular theorem

The source proves in equations (5.6)--(5.7) that, with high probability over the random `d`-regular graph, for all sublinear times in the regime considered there,

$$
q_t
=\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)
=O(t/n)
\qquad (t=o(n)).
\tag{7.1}
$$

The derivation uses the Aldous--Brown short-time hitting estimate (their Lemma 5.2), the fact that the product-chain spectral gap is bounded away from zero with high probability, and the stationary mean meeting time `Theta(n)`.

For a deterministic sequence `t_n=o(n)` with `t_n\ge1`, Proposition 6.1 and (7.1) give

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}(t_n/n).
\tag{7.2}
$$

For `0\le t_n<1`, monotonicity of `q_t` gives

$$
q_{t_n}\le q_1=O_{\mathbb P}(1/n),
$$

so in all cases

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}\left(\frac{1+t_n}{n}\right).
}
\tag{7.3}
$$

Now fix any `C_n\to\infty`. On any environment event on which the right-hand side of (7.3) is at most `K(1+t_n)/n`, Chebyshev gives

$$
\mathbf P_u^G\left(
|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)
\le\frac{K}{C_n^2}.
\tag{7.4}
$$

The good-environment event has probability tending to one, while `K/C_n^2\to0`. Therefore

$$
\boxed{
\mathbf P_u^G\left(
|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)
\xrightarrow{\mathbb P}0.
}
\tag{7.5}
$$

This is exactly the corrected concentration target in the current proof spine.

For every `t_n\ge1` with `t_n=o(n)`, the same argument with (7.2) gives

$$
\mathbf P_u^G\left(
|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n|
>C_n\sqrt{t_n/n}
\right)
\xrightarrow{\mathbb P}0,
\tag{7.6}
$$

which is the source's intended sharp dynamical scale. Combined with assignment 001, the original Eq. (1.9) fails only because it allowed very small times without the initial `n^{-1/2}` scale.

## 8. Relation to the assignment's cancellation question

The signed covariance route does have a nontrivial exact incidence identity, namely (2.3): edge and wedge terms combine to `PQ=Q-Q^2`. I did not establish an exact cancellation among the pairing classes in (1.7), nor a uniform direct sign estimate for `Cov(Dcal,LDcal)`.

The target nevertheless closes because the genealogy-first decomposition changes the place where four-walk dependence enters. In the semimartingale/integrated-drift route, taking absolute cross-meeting probabilities before time integration risks extra powers of `t`. In the Section 5 sample-and-discard route, the same interaction probability is multiplied by the sample size `K`. In the quotient-genealogy decomposition, the four-walk interaction probability appears only in the static variance of `J_t`, with exactly one factor

$$
q_t=O((1+t)/n).
$$

Thus this block does **not** trigger the Meeting 001 abandonment condition: an absolute cross-meeting estimate is used, but its time growth is already exactly the required variance scale because a new structural mechanism removes both the time integral and the sample multiplier.

## 9. Checks and possible audit points

The proof should be independently audited at the following load-bearing points.

1. **Conditional cut covariance.** Verify (4.1)--(4.4), especially that disjoint quotient-edge indicators are independent under product Bernoulli labels and that all remaining covariances are bounded by `1/4`.
2. **Cluster-square identity.** Verify (4.6)--(4.7), including the convention that two stationary walks started at the same vertex have meeting time zero.
3. **Four-family coupling.** Verify (5.3) carefully using consistency of the coalescing system and a coupling to two independent coalescing pairs up to first cross meeting.
4. **Unoriented/oriented edge averaging.** Verify that averaging over uniform unoriented edge pairs is identical for the orientation-invariant interaction event to the `nu tensor nu` law in source equation (5.6).
5. **Small times in source (5.7).** The source writes `O(t/n)` for `t=o(n)`. Since `q_0=1/n` under `pi tensor pi`, use the statement only at `t>=1`; for `t<1`, monotonicity and the `t=1` estimate give `O(1/n)`. This is why (7.3) is written with `1+t`.
6. **Environment mode.** The result needed is sequence-wise quenched-in-probability, not a uniform-in-all-sublinear-times bound. Source (5.7) is sufficient in this mode.

No incremental refinement of Lemma 5.3 is used anywhere in the proof.

## 10. Proof-spine consequence if audited

If Proposition 6.1 and its use of source (5.7) pass independent checking, the main corrected target is proved. E4 and E5 cease to be load-bearing. The useful replacement proof spine is:

1. source correction at very small times;
2. deterministic genealogical variance inequality (6.1);
3. published stationary meeting estimate (5.7);
4. Chebyshev.

The result is structural rather than a larger-window instantiation: it identifies a deterministic graph variance inequality reducing voter discordance fluctuations to a two-walk meeting probability, and it resolves the corrected all-sublinear concentration target.

Recommendation: `develop signed four-walk theorem`
