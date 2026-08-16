# Student D 001: sharp discordance concentration reduction

## Executive conclusion

The literal open statement (1.9) in Avena--Baldasso--Hazra--den Hollander--Quattropani is false as written because it quantifies over every sequence `t_n=o(n)`, including `t_n -> 0`, while the Bernoulli initial condition already has fluctuations of order `n^{-1/2}`. A positive-time counterexample is obtained with `t_n=n^{-3}` and `C_n=log n`.

The natural corrected target is

$$
\mathbf P_u^G\left(
\left|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n\right|
> C_n\sqrt{\frac{1+t_n}{n}}
\right)\xrightarrow{\mathbb P}0
$$

for every `t_n=o(n)` and every `C_n->infinity`, with fixed `d>=3` and `u in (0,1)`. Equivalently one may use the scale

$$
n^{-1/2}+\sqrt{t_n/n}.
$$

For sequences bounded away from zero this agrees, up to constants, with the scale proposed in (1.9). For the original scale `C_n sqrt(t_n/n)` to dominate the initial fluctuation when `t_n->0`, at least `C_n sqrt(t_n)->infinity` is necessary.

For the dynamics, the first-principles calculation confirms the candidate generator identity and gives an exact bracket bound: the normalized martingale part has second moment at most `4t/n` on every fixed `d`-regular graph. The non-martingale obstruction is therefore the integrated centered drift.

That drift is a spatial average of centered two-spin observables supported on edges and length-two wedges. Its two-time covariance has an exact staggered four-coalescing-walk representation. Thus four ancestral lineages are the generic minimal dual object. A second-moment estimate of order `t/n` for the integrated centered drift would close the corrected sharp theorem (apart from the already isolated initial `n^{-1/2}` term).

The published weak-dependence proof does not merely lose a constant. Its Section 5 proof samples `K_n=log^2 n` edges and discards every sampled edge whose dual pair interacts with another sampled dual pair. At shrinking target accuracy `delta`, this architecture simultaneously pays sampling noise of order `K^{-1/2}` and a worst-case deletion cost coming from interacting dual families. Pair interaction probabilities are naturally of order `t/n`. Balancing those two errors at the level of this deletion argument leads to the scale `(t/n)^{1/3}`, not `(t/n)^{1/2}`. Consequently the full sharp target cannot follow from a routine quantitative extension of the same discard-interactions argument. One needs either a genuinely sharper theorem controlling the *contribution* of interacting four-walk families, including cancellation, or a different corrector/martingale decomposition.

## 1. Source statement and actual frontier

Primary source: Luca Avena, Rangel Baldasso, Rajat Subhra Hazra, Frank den Hollander, Matteo Quattropani, *Discordant edges for the voter model on regular random graphs*, ALEA 21 (2024), 431--464, arXiv:2209.01037v2.

The model convention in the source is the continuous-time voter model on a uniformly random simple `d`-regular graph with fixed `d>=3`: every vertex rings at rate one and copies a uniformly chosen neighbour. The environment law is denoted `mathbb P`. For a fixed graph, `mathbf P_u` is the voter law with i.i.d. Bernoulli(`u`) initial opinions, `u in (0,1)`. The number of graph edges is

$$
m=\frac{dn}{2},
$$

and the discordant-edge density is

$$
\mathcal D_t^n=\frac{D_t}{m},
$$

where here and below `D_t` denotes the *number* of discordant edges.

### 1.1 The open statement (1.9)

Section 1.4 says that for every sequence `t_n` satisfying

$$
\frac{t_n}{n}\longrightarrow0
$$

and every `C_n->infinity`, the authors expect

$$
\mathbf P_u^G\left(
\left|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n\right|
> C_n\sqrt{\frac{t_n}{n}}
\right)
\xrightarrow{\mathbb P}0.
\tag{1.9-source}
$$

There is no hypothesis in the displayed open problem that `t_n->infinity`, `t_n>=1`, or is bounded away from zero.

### 1.2 What is already proved

There are two concentration statements that should not be conflated.

Theorem 1.2(1) already gives **pointwise fixed-epsilon concentration throughout the whole sublinear regime**: for every `t_n` with `t_n/n->0` and every fixed `epsilon>0`,

$$
\sup_{\xi\in\{0,1\}^V}
\mathbf P_\xi^G\left(
\left|\mathcal D_{t_n}^n-\mathbf E_\xi^G\mathcal D_{t_n}^n\right|>\epsilon
\right)
\xrightarrow{\mathbb P}0.
\tag{1.2.1}
$$

Theorem 1.3 is a different strengthening: for every fixed `u in (0,1)` and `delta,epsilon>0`,

$$
\mathbf P_u^G\left(
\sup_{0\le t\le n^{1-\delta}}
\left|\mathcal D_t^n-\mathbf E_u^G\mathcal D_t^n\right|>\epsilon
\right)
\xrightarrow{\mathbb P}0.
\tag{1.3}
$$

Thus the genuinely open issue in (1.9) is the **sharp shrinking fluctuation scale**, not merely extending fixed-epsilon concentration to larger sublinear times.

### 1.3 Where the polynomial time restriction enters

Section 5 proves Proposition 5.1 by sampling

$$
K_n=\log^2 n
$$

random edges and studying the `2K_n` endpoint walks. For two sampled edges `e_i,e_j`, their interaction time is the minimum of the four cross meeting times between their two endpoint walks, equation (5.5). Equations (5.6)--(5.7) give, for `t=o(n)`,

$$
\mathbf P_{\nu\otimes\nu}(\tau^{e_i,e_j}\le t)
\le 4\mathbf P_{\pi\otimes\pi}(\tau_{\rm meet}\le t)
=O(t/n)
$$

with high environment probability.

The stronger polynomial restriction `t<=n^{1-epsilon}` appears in Lemma 5.3. The proof first imposes the path-count event

$$
P_{\rm tot}=\{\text{every walk makes at most }n^{\epsilon/2}t\text{ jumps by time }t\}.
$$

The conditional meeting estimate when one of the two sampled edges has appeared previously is then bounded in (5.21) by

$$
\frac{8n^{\epsilon/2}t}{n}.
$$

After enumerating possible interaction graphs the proof obtains, in (5.22),

$$
\Gamma
=
\sqrt{\frac{8(n^{\epsilon/2}t+K_n)}{n}},
$$

and closes because

$$
K_n^2\Gamma\le n^{-\epsilon/5}
$$

for all large `n`. This is the exact point at which a fixed polynomial gap from `n` is consumed.

This loss can certainly be quantitatively improved, but doing so is not by itself a project result and, more importantly, does not address the sharp shrinking scale obstruction discussed in Section 6 below.

### 1.4 Successor check

A targeted successor/citation search through 2026-08-16 did not identify a primary source resolving the static random-regular-graph statement (1.9). The 2025 Avena--Baldasso--Hazra--den Hollander--Quattropani paper on random regular graphs **with random rewiring** studies a different dynamic environment. Capannoli's 2024/2025 work studies sparse directed configuration models. This is evidence of continued openness, not a proof of absence.

## 2. Exact semimartingale decomposition

Fix an arbitrary simple `d`-regular graph `G=(V,E)` with `|V|=n`. For a configuration `eta`, let

$$
k_x(\eta)=|\{y\sim x:\eta(y)\ne\eta(x)\}|.
$$

At a ring at `x`, a flip occurs exactly when the copied neighbour disagrees with `x`, hence at rate

$$
\frac{k_x}{d}.
$$

If `x` flips, its `k_x` discordant incident edges become concordant and its `d-k_x` concordant incident edges become discordant. Therefore

$$
D(\eta^x)-D(\eta)=(d-k_x)-k_x=d-2k_x.
$$

Consequently the voter generator gives the exact identity

$$
LD(\eta)
=\sum_{x\in V}\frac{k_x}{d}(d-2k_x).
\tag{2.1}
$$

Since

$$
\sum_x k_x=2D,
$$

if

$$
W(\eta)=\sum_x k_x(d-k_x),
$$

then

$$
LD=\frac{2}{d}W-2D.
\tag{2.2}
$$

For the normalized discordance `mathcal D=D/m`, `m=dn/2`, put

$$
h(\eta)=L\mathcal D(\eta)
=\frac{4}{d^2n}W(\eta)-2\mathcal D(\eta).
\tag{2.3}
$$

Dynkin's formula yields

$$
\mathcal D_t
=\mathcal D_0+M_t+\int_0^t h(\eta_s)\,ds,
\tag{2.4}
$$

where `M` is a càdlàg martingale with `M_0=0`.

### 2.1 Exact predictable quadratic variation

A flip at `x` changes `mathcal D` by

$$
\Delta_x\mathcal D=\frac{d-2k_x}{m}.
$$

Thus

$$
\frac{d}{dt}\langle M\rangle_t
=\sum_x\frac{k_x(\eta_t)}{d}
\left(\frac{d-2k_x(\eta_t)}{m}\right)^2
=\frac{4}{d^3n^2}\sum_x k_x(\eta_t)(d-2k_x(\eta_t))^2.
\tag{2.5}
$$

Because `0<=k_x<=d`,

$$
\frac{d}{dt}\langle M\rangle_t\le\frac4n,
\qquad
\langle M\rangle_t\le\frac{4t}{n},
\qquad
\mathbf E_u^G[M_t^2]\le\frac{4t}{n}.
\tag{2.6}
$$

So the martingale part alone is uniformly on the proposed `sqrt(t/n)` scale for every time regime. No random-graph input is needed for this fact.

## 3. The literal (1.9) is false at very small times

The obstruction is present already at time zero and is environment-independent.

Let

$$
a=u(1-u),
\qquad
p=2u(1-u)=2a,
$$

and for `e={x,y}` put

$$
I_e=\mathbf 1_{\{\eta_0(x)\ne\eta_0(y)\}}.
$$

Then `D_0=sum_e I_e`. Disjoint edges depend on disjoint initial Bernoulli variables and hence are independent. For two distinct edges sharing one endpoint,

$$
\mathbf E_u[I_{xy}I_{xz}]
=u(1-u)^2+(1-u)u^2=a,
$$

so

$$
\operatorname{Cov}_u(I_{xy},I_{xz})
=a-4a^2=a(1-4a).
$$

There are `m=dn/2` edges and `n binom(d,2)` unordered adjacent edge pairs. Therefore, on **every** simple `d`-regular graph,

$$
\operatorname{Var}_u(D_0)
=m\,2a(1-2a)
+2n\binom d2 a(1-4a)
=nd\,a\big[d-(4d-2)a\big].
\tag{3.1}
$$

After division by `m^2`,

$$
\operatorname{Var}_u(\mathcal D_0)
=
\frac{4a\,[d-(4d-2)a]}{dn}.
\tag{3.2}
$$

The constant is strictly positive for every `u in (0,1)`. In particular, at `u=1/2`,

$$
\operatorname{Var}_{1/2}(\mathcal D_0)=\frac{1}{2dn}.
$$

Variance alone is not enough for a lower-tail obstruction, so we record a uniform fourth-moment bound. The centered edge variables

$$
X_e=I_e-p
$$

have a dependency graph equal to the line graph of `G`, of degree at most `2(d-1)`, and `|X_e|<=1`. In the expansion of

$$
S^4,\qquad S=\sum_e X_e,
$$

a term vanishes whenever one edge index occurs in a dependency component by itself, because that centered factor is independent of the other factors. Hence every nonzero ordered four-tuple splits into either one dependency cluster of size at least two or two clusters of size two. Since the dependency degree is bounded in `d`, the number of such tuples is `O_d(m^2)`. Therefore

$$
\mathbf E_u[S^4]\le C_d m^2\le C'_d n^2.
\tag{3.3}
$$

Combining (3.1) and (3.3), Paley--Zygmund applied to `S^2` gives constants `c_1,c_2>0`, depending only on `d,u`, such that for every simple `d`-regular graph and all `n`,

$$
\mathbf P_u^G\left(
\left|\mathcal D_0-\mathbf E_u\mathcal D_0\right|
\ge \frac{c_1}{\sqrt n}
\right)\ge c_2.
\tag{3.4}
$$

Now take

$$
t_n=n^{-3},
\qquad
C_n=\log n.
$$

The total clock-ring rate is `n`, so

$$
\mathbf P(\text{no voter clock rings before }t_n)
=e^{-nt_n}=e^{-n^{-2}}\longrightarrow1.
\tag{3.5}
$$

Also each normalized jump has absolute size at most `2/n` and the total rate is `n`, hence

$$
|L\mathcal D|\le2,
\qquad
\left|\mathbf E_u^G\mathcal D_{t_n}-\mathbf E_u^G\mathcal D_0\right|
\le2t_n.
\tag{3.6}
$$

On the no-ring event, `mathcal D_{t_n}=mathcal D_0`. Meanwhile the threshold in (1.9-source) is

$$
C_n\sqrt{\frac{t_n}{n}}
=\frac{\log n}{n^2}
=o(n^{-1/2}).
$$

Equations (3.4)--(3.6) therefore imply

$$
\liminf_{n\to\infty}
\mathbf P_u^G\left(
\left|\mathcal D_{t_n}-\mathbf E_u^G\mathcal D_{t_n}\right|
>C_n\sqrt{t_n/n}
\right)
\ge c_2>0
\tag{3.7}
$$

uniformly over the graph environment. Thus (1.9) is literally false.

### 3.1 Corrected formulation by time regime

The initial fluctuation and dynamical martingale suggest the combined variance scale

$$
\frac{1+t}{n}.
$$

A corrected all-sublinear-times conjecture is therefore

$$
\boxed{
\mathbf P_u^G\left(
\left|\mathcal D_{t_n}-\mathbf E_u^G\mathcal D_{t_n}\right|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)
\xrightarrow{\mathbb P}0
}
\tag{3.8}
$$

for every `t_n=o(n)` and `C_n->infinity`.

The regimes are:

- `t_n->0`: the `n^{-1/2}` initial term is dominant; the literal source scale is false for arbitrary `C_n->infinity`.
- `t_n=Theta(1)`: `sqrt((1+t_n)/n)` and `sqrt(t_n/n)` are comparable, so the source scale is consistent.
- `t_n->infinity`, `t_n=o(n)`: the initial term is negligible and the target becomes exactly `sqrt(t_n/n)`.

If one insists on retaining the source threshold `C_n sqrt(t_n/n)` for a particular very-small-time sequence, then the necessary condition coming from (3.4) is

$$
C_n\sqrt{t_n}\longrightarrow\infty.
$$

## 4. The centered drift is an edge/wedge two-spin average

Write spins

$$
\sigma_x=2\eta(x)-1\in\{-1,+1\}.
$$

Let

$$
S_x=\sum_{y\sim x}\sigma_y.
$$

Then

$$
k_x=\frac{d-\sigma_xS_x}{2},
\qquad
k_x(d-k_x)=\frac{d^2-S_x^2}{4}.
$$

Since

$$
S_x^2=d+2\sum_{\{y,z\}\subset N(x)}\sigma_y\sigma_z,
$$

we obtain

$$
W
=\frac{n(d^2-d)}4
-\frac12\sum_{x\in V}\sum_{\{y,z\}\subset N(x)}\sigma_y\sigma_z.
\tag{4.1}
$$

Also

$$
\mathcal D
=\frac12-\frac{1}{dn}\sum_{\{x,y\}\in E}\sigma_x\sigma_y.
\tag{4.2}
$$

Substituting (4.1)--(4.2) into (2.3) gives the exact local quadratic form

$$
\boxed{
 h(\sigma)
 =-\frac1d
 +\frac{2}{dn}\sum_{\{x,y\}\in E}\sigma_x\sigma_y
 -\frac{2}{d^2n}
 \sum_{x\in V}\sum_{\{y,z\}\subset N(x)}\sigma_y\sigma_z.
}
\tag{4.3}
$$

It is convenient to regard the edge terms and wedge-endpoint terms as a multiset `mathscr Q` of unordered vertex pairs. Give each edge pair coefficient

$$
b_q=\frac2d
$$

and each wedge-endpoint occurrence coefficient

$$
b_q=-\frac{2}{d^2}.
$$

Multiplicities are retained when two vertices share more than one common centre. If

$$
Z_q(\sigma)=\sigma_{q^-}\sigma_{q^+},
$$

then

$$
h(\sigma)=-\frac1d+\frac1n\sum_{q\in\mathscr Q}b_qZ_q(\sigma).
\tag{4.4}
$$

There are `O_d(n)` entries in `mathscr Q`, all coefficients are bounded in `d`, and every term is supported at graph distance at most two.

## 5. Exact integrated-drift reduction

For the Bernoulli(`u`) voter law on a fixed graph define

$$
X_t=\mathcal D_t-\mathbf E_u^G\mathcal D_t,
\qquad
\widetilde h_t=h(\eta_t)-\mathbf E_u^G h(\eta_t).
$$

Centering (2.4) gives

$$
X_t=X_0+M_t+\int_0^t\widetilde h_s\,ds.
\tag{5.1}
$$

By (4.4),

$$
\widetilde h_s
=\frac1n\sum_{q\in\mathscr Q}b_q
\left(Z_q(s)-\mathbf E_u^G Z_q(s)\right).
\tag{5.2}
$$

Therefore the variance of the integrated drift is **exactly**

$$
\boxed{
\mathbf E_u^G\left[
\left(\int_0^t\widetilde h_s\,ds\right)^2
\right]
=
\frac1{n^2}
\sum_{q,q'\in\mathscr Q}b_qb_{q'}
\int_0^t\int_0^t
\operatorname{Cov}_u^G\big(Z_q(s),Z_{q'}(r)\big)
\,ds\,dr.
}
\tag{5.3}
$$

This exposes the single load-bearing covariance sum. No placeholder such as "control correlations" remains.

### 5.1 A sufficient sharp estimate

A pointwise-in-time estimate sufficient for the corrected theorem is the following.

For every deterministic sequence `t_n` with `1<=t_n=o(n)`, prove that under the environment law

$$
\frac{n}{t_n}
\mathbf E_u^G\left[
\left(\int_0^{t_n}\widetilde h_s\,ds\right)^2
\right]
=O_{\mathbb P}(1).
\tag{DRIFT}
$$

An all-time version may be written with `Ct/n` for `t>=1`; for `t<1` the same upper bound is harmless and the initial `n^{-1/2}` term dominates anyway.

Indeed, (3.2), (2.6), (5.1), and (DRIFT) give

$$
\mathbf E_u^G[X_t^2]
\lesssim_{d,u}\frac{1+t}{n}
$$

up to a fixed constant factor by `(a+b+c)^2<=3(a^2+b^2+c^2)`. Chebyshev then yields (3.8) for every `C_n->infinity`.

Thus, after correcting the very-small-time formulation, (DRIFT) is an explicit single estimate carrying the sharp theorem.

## 6. Four-walker dual representation of the covariance kernel

Let

$$
\mu=\mathbf E_u[\sigma_x]=2u-1.
$$

Fix `0<=r<=s`, `q={a,b}`, and `q'={c,d}`. Construct the voter dual backwards in the common graphical representation as follows:

1. start lineages labelled `1,2` at `(a,s),(b,s)`;
2. run them backwards to time `r`, coalescing on meeting;
3. at time `r` add labels `3,4` at `(c,r),(d,r)`;
4. run all active lineages backwards to time zero, coalescing on every meeting.

Let

$$
\Pi_{s,r}^{q,q'}
$$

be the resulting partition of the four labels according to their common ancestor at time zero. For a partition `Pi`, let

$$
N_{\rm odd}(\Pi)
=\#\{B\in\Pi:|B|\text{ is odd}\}.
$$

Conditional on the dual partition, different ancestral spins at time zero are independent with mean `mu`, while an ancestral spin raised to an even power equals one. Hence

$$
\boxed{
\mathbf E_u^G[Z_q(s)Z_{q'}(r)]
=\mathbf E_{\rm CRW}^G\left[
\mu^{N_{\rm odd}(\Pi_{s,r}^{q,q'})}
\right].
}
\tag{6.1}
$$

For one pair, if `p_q(s)` is the probability that its two ancestral lineages have coalesced by time zero, then

$$
\mathbf E_u^G Z_q(s)
=\mu^2+(1-\mu^2)p_q(s),
\tag{6.2}
$$

and similarly for `q'` at time `r`. Therefore

$$
\boxed{
\operatorname{Cov}_u^G(Z_q(s),Z_{q'}(r))
=
\mathbf E_{\rm CRW}^G\left[
\mu^{N_{\rm odd}(\Pi_{s,r}^{q,q'})}
\right]
-
\big[\mu^2+(1-\mu^2)p_q(s)\big]
\big[\mu^2+(1-\mu^2)p_{q'}(r)\big].
}
\tag{6.3}
$$

This is the exact dual kernel to insert in (5.3).

At `u=1/2`, `mu=0`, equation (6.1) simplifies: the joint moment is the probability that every final ancestral block has even cardinality. The contributing final partitions are a single block of four or two blocks of two; the possible two-two pairings include the designated pairing `(12)(34)` and the two cross pairings `(13)(24)` and `(14)(23)`.

### 6.1 Which collision events matter

There are two internal meeting types,

$$
1\leftrightarrow2,
\qquad
3\leftrightarrow4,
$$

and four generic cross meeting types,

$$
1\leftrightarrow3,
\quad
1\leftrightarrow4,
\quad
2\leftrightarrow3,
\quad
2\leftrightarrow4.
$$

Internal meetings determine the separate pair expectations in (6.2). Dependence between the two pair observables is created only when the two dual families have a cross meeting. Before their first cross meeting the two pair systems can be realised as independent coalescing pairs. Thus a coupling gives the useful crude bound

$$
\left|\operatorname{Cov}_u^G(Z_q(s),Z_{q'}(r))\right|
\le 2\,\mathbf P_{\rm CRW}^G(	ext{a cross meeting occurs}).
\tag{6.4}
$$

The constant is unimportant; the point is the support of the dependence.

For generic disjoint `q,q'`, four lineages are genuinely required: the joint product depends on which cross pairing/coalescence partition is produced. Fewer than four walkers cannot encode these alternatives. When some endpoints coincide, the system degenerates to fewer active lineages, but the covariance sum (5.3) contains generic four-lineage terms.

Equation (6.4) also explains why taking absolute values pair-by-pair is unlikely to be sharp after summing over `O(n^2)` pairs. The signed coefficients `b_qb_{q'}` in (5.3) and/or a more refined cancellation among four-walk collision patterns must be used if the crude cross-meeting sum is too large.

## 7. Assessment of the source weak-dependence method

The source Section 5 architecture is:

1. sample `K` edges to estimate the global discordant fraction;
2. run the `2K` endpoint dual walks;
3. declare a sampled edge bad if its pair has any cross meeting with another sampled pair;
4. discard all bad sampled edges, paying their fraction as a worst-case error;
5. on the remaining noninteracting families, use negative dependence and binomial concentration.

This is extremely effective for fixed error `delta>0`. It is not automatically compatible with the sharp shrinking error.

Let

$$
x=\frac tn,
\qquad
\delta=\text{desired error scale}.
$$

The source Chernoff step (5.2) has exponent of order `K delta^2`, so a shrinking-error implementation needs

$$
K\delta^2\longrightarrow\infty.
\tag{7.1}
$$

On the other hand, a pair of sampled dual edge-families interacts with probability of order `x` after mixing and at most `O(x)` throughout the source's sublinear regime; equations (5.6)--(5.8) are precisely the relevant meeting estimate. In the sparse-interaction regime the natural bad-edge fraction is therefore of order

$$
Kx.
$$

Because the Section 5 argument treats every bad edge as an arbitrary `[0,1]` contribution, absorbing this deletion into an error budget `delta` requires at the level of this architecture

$$
Kx=o(\delta).
\tag{7.2}
$$

The two scale requirements (7.1)--(7.2) ask for

$$
\delta^{-2}\ll K\ll \frac{\delta}{x}.
$$

Such a window requires

$$
x=o(\delta^3).
\tag{7.3}
$$

Equivalently, optimizing the two visible errors

$$
K^{-1/2}+Kx
$$

over `K` gives the characteristic scale

$$
x^{1/3}.
\tag{7.4}
$$

For the proposed sharp scale

$$
\delta=C\sqrt{x},
$$

condition (7.3) becomes

$$
C^3\sqrt{x}\longrightarrow\infty.
\tag{7.5}
$$

But (1.9) quantifies over arbitrary `C_n->infinity` and arbitrary `x_n=t_n/n->0`; (7.5) can fail badly. For example,

$$
t_n=n^{1/2},
\qquad
C_n=\log n
$$

gives `C_n^3 sqrt(x_n)=(log n)^3 n^{-1/4}->0`.

This is a structural warning about the proof mechanism, not a claim that the true fluctuations are of order `x^{1/3}`. The `x^{1/3}` scale is the best balance visible when one both resolves the global density by subsampling and then throws away every interacting family at unit cost.

Therefore reaching the sharp scale requires one of the following qualitatively stronger inputs:

- a four-walk theorem that evaluates or cancels the *signed contribution* of interacting pair-families rather than deleting them;
- a covariance summation theorem directly proving (DRIFT), exploiting the edge/wedge coefficients in (5.3);
- or a different martingale/corrector decomposition in which the local drift is solved away.

Merely replacing `n^{epsilon/2}` by a slower slack, increasing `K_n`, or extending Lemma 5.3 from `n^{1-epsilon}` to `n/polylog(n)` is not enough to answer the sharp problem and would fall under the standing novelty exclusion.

## 8. What changed in the proof spine

The mathematical state after this assignment is:

- **E0:** exact source frontier established. Theorem 1.2(1) already gives fixed-epsilon pointwise concentration for all `t=o(n)`; Theorem 1.3 gives uniform fixed-epsilon concentration up to `n^{1-delta}`; Eq. (1.9) asks for a shrinking `sqrt(t/n)` rate for every sublinear sequence.
- **E1:** verified. Equations (2.1)--(2.6) give the exact generator, semimartingale, and bracket. The martingale is not the obstruction.
- **E4:** resolved negatively. Literal Eq. (1.9) is false at `t_n->0`; replace it by (3.8), or impose a lower-time condition sufficient to dominate `n^{-1/2}` initial fluctuations.
- **E2:** sharpened to the exact single estimate (DRIFT), with the covariance sum (5.3).
- **E3:** sharpened to the exact staggered four-coalescing-walk kernel (6.3). Four walkers are generically minimal; cross meetings are the dependence events.
- **new method assessment:** the source's discard-interacting-samples architecture has a shrinking-scale sampling/deletion tension summarized by (7.1)--(7.4). A full sharp proof requires controlling interacting four-walk contributions rather than only proving they are rare at fixed density.

## 9. Recommended next mathematical task

The Professor should replace the literal source target by the corrected all-sublinear theorem (3.8). The next bounded technical assignment, if the programme continues, should not be a longer time-window version of Lemma 5.3. It should test (DRIFT) on the actual signed edge/wedge covariance sum (5.3): either derive a cancellation identity reducing the four-walk cross-meeting contributions to `O(t/n)`, or produce a lower bound/counterexample showing that `t/n` is not the correct integrated-drift variance.

A particularly informative first subtask is the symmetric case `u=1/2`, where (6.1) becomes an even-block partition probability and the collision taxonomy is discrete. The goal there should be a structural signed-sum identity, not a finite-window numerical estimate.

replace target by corrected concentration theorem
