# Independent audit 002: genealogical variance theorem, review B

Date: 2026-08-16

Role: fresh independent correctness reviewer. I did not participate in the research or the Professor reconstruction, and I did not read or rely on Review A. In accordance with the assignment, I reconstructed the main argument before reading `notes/professor-assignment-002-verification.md`. I do not assess novelty or priority here.

## Conclusion

The central deterministic inequality is correct, with the natural convention that the regular degree is positive so that the discordant-edge density is defined:

\[
\operatorname{Var}_u^G(\mathcal D_t)
\le 2\,\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)
\]

for every finite simple `d`-regular graph with `d>=1`, every `u in (0,1)`, and every `t>=0`. Connectedness is not needed for this deterministic inequality.

The proof by conditioning on the Harris genealogy is sound. I find no hidden dependence in the cluster labels, no missing covariance cross term, and no unaccounted interaction caused by within-family coalescence. The factor `2` is justified.

The random-regular consequence is also correct for fixed `d>=3`. The primary-source interface needs one qualification: source equation (5.7), written as `O(t/n)` for `t=o(n)`, cannot literally be used uniformly down to `t=0`, because the two stationary starting vertices coincide with probability `1/n`. The project already repairs this correctly. Equation (5.8), together with the source's `Theta(n)` stationary mean meeting time and high-probability spectral-gap input, gives `O((1+t)/n)` on sublinear deterministic sequences, hence `O(t/n)` for `t>=1`; monotonicity gives `O(1/n)` for `t<1`.

Consequently the stated variance and Chebyshev consequences are valid:

\[
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}\!\left(\frac{1+t_n}{n}\right)
\]

for every deterministic `t_n=o(n)`, and the source scale `C_n sqrt(t_n/n)` is obtained for every deterministic `1<=t_n=o(n)`.

The claimed counterexample to the literal source statement (1.9), with `t_n=n^{-3}` and `C_n=log n`, is also correct.

I therefore find no mathematical repair needed to `VOTER-CONC-001`. I would make two editorial clarifications before stable use: state `d>=1` in the deterministic theorem (or retain the ambient `d>=3` convention), and cite (5.8), rather than the bare wording of (5.7), when explaining the all-small-time meeting bound.

---

## 1. Primary-source interface

I checked Avena--Baldasso--Hazra--den Hollander--Quattropani, *Discordant edges for the voter model on regular random graphs*, ALEA 21 (2024), 431--464, against arXiv:2209.01037v2, the April 2024 version corresponding to the published paper.

### 1.1 Voter and walk normalization

Section 2.1 defines the voter generator by

\[
(Lf)(\eta)=\sum_x\sum_{y\sim x}\frac1{d_x}
\bigl[f(\eta^{x\leftarrow y})-f(\eta)\bigr].
\]

Thus on a `d`-regular graph every vertex updates at total rate one and copies a uniformly chosen neighbour. The graphical representation attaches to each oriented edge `(x,y)` a Poisson process of rate `1/d`; a backward ancestral lineage is therefore a rate-one continuous-time simple random walk. The source explicitly states that distinct ancestral walks evolve independently until they meet and then coalesce.

This is exactly the convention used in the project claim. There is no factor-two discrepancy in the walk clock.

The source meeting time is

\[
\tau_{\rm meet}^{x,y}=\inf\{s\ge0:X_s^x=X_s^y\}.
\]

Hence two walks started at the same vertex meet at time zero. This matters for the diagonal `1/n` contribution below.

### 1.2 Source event (5.5) and estimate (5.6)

In Section 5 the source samples an oriented edge according to

\[
\nu(x,y)=\pi(x)\frac1d\mathbf 1_{\{x\sim y\}}.
\]

For a regular graph both marginals of `nu` are uniform `pi`. For two sampled edges `e_i,e_j`, equation (5.5) defines their interaction time as the minimum of the four meeting times between one endpoint walk from family `i` and one endpoint walk from family `j`. The four walks in this Section 5 construction are independent. If the two initial edges share a vertex, the source explicitly declares the interaction time to be zero.

Equation (5.6) is exactly

\[
\mathbf P_{\nu\otimes\nu}^G(\tau^{e_1,e_2}\le t)
\le 4\,\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t),
\]

and the paper says this follows from the definition of `nu` and a union bound. This is precisely the estimate used by the project.

### 1.3 Source meeting estimate (5.7)--(5.8)

Equation (5.7) is printed as

\[
\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)=O(t/n)
\qquad (t=o(n))
\]

with high environment probability. The proof immediately invokes Lemma 5.2, equation (5.8), an Aldous--Brown short-time hitting estimate for the product walk on `G\otimes G` hitting the diagonal. In the source application,

- the initial law is `pi tensor pi`;
- the hitting set is the diagonal;
- the stationary mean hitting/meeting time is `Theta(n)` with high probability, by Proposition 3.7 and the preceding random-regular inputs;
- the nontrivial spectral gap is bounded away from zero with high probability, using Friedman.

The displayed estimate (5.8) yields, on an event whose environment probability tends to one,

\[
q_t^G:=\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)
\le C\left(\frac{t}{n}+\frac{t^2}{n^2}+\frac1n\right)
\]

for `0<=t<=c n`, after choosing deterministic high-probability bounds on the mean meeting time and the spectral gap. Therefore, along every deterministic `t_n=o(n)`,

\[
q_{t_n}^G=O_{\mathbb P}((1+t_n)/n).
\]

If `t_n>=1`, the additive `1/n` is absorbed and

\[
q_{t_n}^G=O_{\mathbb P}(t_n/n).
\]

For `0<=t_n<1`, one may equivalently use monotonicity:

\[
q_{t_n}^G\le q_1^G=O_{\mathbb P}(1/n).
\]

This is exactly the regime split claimed by the project.

There is a minor imprecision in the source's sentence following (5.8): it treats the error term there as `O(t/n)` whenever `t/n->0`, but at `t=0` the meeting probability is already `1/n` because the two stationary starts can coincide. This does not damage the source argument in its intended regime and does not damage the project theorem, because the project explicitly keeps the additive small-time scale.

### 1.4 Source statement (1.9) and centering mode

The source's Section 1.4 states (1.9) for **every** sequence `t_n` satisfying `t_n/n -> 0` and every `C_n->infinity`; the displayed statement contains no hypothesis that `t_n->infinity`, `t_n>=1`, or even that it is bounded away from zero.

The source reserves `mathbb P` for the random graph environment and uses the voter/random-walk law on a fixed quenched graph inside. Thus the project's centering by the quenched expectation `mathbf E_u^G mathcal D_t` and its convergence in environment probability match the source convention.

---

## 2. Independent derivation of the conditional genealogy representation

Fix a finite simple `d`-regular graph `G=(V,E)`, `|V|=n`, with `d>=1`, and let `m=dn/2`. Let `H_t` be the sigma-field generated by all Harris arrows in the slab `[0,t]`, excluding the initial Bernoulli opinions.

For each vertex `x`, follow its unique backward arrow path from `(x,t)` to time zero and write `a_t(x)` for its ancestor at time zero. Because the graph is finite and the Poisson processes are locally finite, `a_t` is measurable with respect to `H_t`.

The initial opinions `(xi_v)_{v in V}` are i.i.d. Bernoulli(`u`) and independent of all Harris arrows. Therefore, conditional on `H_t`,

\[
\eta_t(x)=\xi_{a_t(x)},
\]

and the labels attached to **distinct ancestral vertices** remain independent Bernoulli(`u`). No additional conditioning on path shapes or coalescence times is required. All graphical dependence is already contained in the deterministic map `a_t` after conditioning.

Let

\[
C_v(t)=\{x:a_t(x)=v\}
\]

be the ancestral clusters. For distinct ancestors `v,w`, let `N_{vw}` be the number of original graph edges with one endpoint in `C_v` and the other in `C_w`, and let

\[
J_t=\#\{\{x,y\}\in E:a_t(x)=a_t(y)\}.
\]

Then, exactly,

\[
D_t=\sum_{v<w}N_{vw}\mathbf 1_{\{\xi_v\ne\xi_w\}},
\qquad
\sum_{v<w}N_{vw}=m-J_t.
\]

With `p=2u(1-u)`, this gives

\[
\mathbf E[\mathcal D_t\mid H_t]
=p\left(1-\frac{J_t}{m}\right).
\]

I find no measurability or independence subtlety missing here.

---

## 3. Conditional cut variance

Write `I_{vw}=1_{xi_v != xi_w}` for `v!=w`. For two unordered ancestor pairs `r,s`:

- if `r` and `s` are disjoint, `I_r` and `I_s` depend on disjoint initial labels and are independent;
- if they intersect, `|Cov(I_r,I_s)|<=1/4`, since they are indicators.

For distinct `w,z`, a direct calculation gives, with `a=u(1-u)`,

\[
\operatorname{Cov}(I_{vw},I_{vz})
=a(1-4a)=a(2u-1)^2\ge0,
\]

but the sign is not needed.

Conditional on `H_t`,

\[
\operatorname{Var}(D_t\mid H_t)
\le \frac14\sum_{r,s:\,r\cap s\ne\varnothing}N_rN_s.
\]

For each ancestor `v`, set

\[
S_v=\sum_{w\ne v}N_{vw}.
\]

Expanding `sum_v S_v^2`, every ordered pair `(r,s)` with nonempty intersection is counted at least once; a diagonal pair `r=s` is counted twice, once for each endpoint. Hence

\[
\sum_{r,s:\,r\cap s\ne\varnothing}N_rN_s
\le \sum_v S_v^2.
\]

The quantity `S_v` is exactly the number of original graph edges leaving cluster `C_v`. Since the graph is `d`-regular,

\[
S_v\le d|C_v|.
\]

Therefore

\[
\mathbf E\left[\operatorname{Var}(\mathcal D_t\mid H_t)\right]
\le \frac{1}{n^2}\mathbf E\sum_v|C_v(t)|^2.
\]

Finally,

\[
\sum_v|C_v(t)|^2
=\sum_{x,y\in V}\mathbf 1_{\{a_t(x)=a_t(y)\}}.
\]

For fixed `x,y`, the two backward lineages evolve as two independent rate-one continuous-time simple random walks until their first meeting, and after meeting they coalesce. Thus

\[
\mathbf P(a_t(x)=a_t(y))
=\mathbf P_{x,y}(\tau_{\rm meet}\le t).
\]

Averaging independently uniform `x,y` gives the exact identity

\[
\frac1{n^2}\mathbf E\sum_v|C_v(t)|^2
=q_t^G.
\]

The `x=y` terms match the convention `tau_meet=0` for equal starts, contributing exactly the diagonal `1/n` mass.

Hence

\[
\boxed{
\mathbf E\left[\operatorname{Var}(\mathcal D_t\mid H_t)\right]
\le q_t^G.
}
\]

There is no omitted covariance term in this part.

---

## 4. Conditional-mean variance: the delicate four-family step

From the conditional mean,

\[
\operatorname{Var}(\mathbf E[\mathcal D_t\mid H_t])
=\frac{p^2}{m^2}\operatorname{Var}(J_t),
\qquad p=2u(1-u)\le\frac12.
\]

For an unoriented original edge `e={x,y}`, put

\[
Y_e=\mathbf 1_{\{a_t(x)=a_t(y)\}},
\qquad J_t=\sum_{e\in E}Y_e.
\]

The load-bearing point is to bound `Cov(Y_e,Y_f)` without falsely treating the two genealogical edge families as globally independent.

### 4.1 Coupling to two independent coalescing pairs

Take two edges `e,f`. Construct two independent coalescing two-walk systems, one from the endpoints of `e` and one from the endpoints of `f`. Couple them to the four-lineage voter genealogy up to the first time a lineage belonging to the `e` family meets a lineage belonging to the `f` family.

This is legitimate because a finite coalescing-walk system has the standard construction from independent random walks: before any cross-family meeting, the evolution of each family depends only on the independent walk randomness assigned to that family. Within-family meetings are allowed and cause the two trajectories of that family to coalesce; they do not couple the two families.

Let `Y'_e,Y'_f` be the within-pair meeting indicators in the two independent pair systems. They are independent, and each has the same marginal law as `Y_e,Y_f` respectively. On the event of no cross-family meeting up to time `t`, the pair meeting indicators in the true four-lineage system coincide with `Y'_e,Y'_f`. Consequently

\[
\begin{aligned}
|\operatorname{Cov}(Y_e,Y_f)|
&=|\mathbf E[Y_eY_f]-\mathbf E[Y'_eY'_f]|\\
&\le \mathbf P(\text{cross-family meeting by time }t).
\end{aligned}
\]

If `e,f` share an endpoint, the cross-family time is zero and the bound is trivial.

### 4.2 Why within-family coalescence is covered by source (5.5)

The source's event (5.5) is defined using four **independent** random-walk paths, without coalescing within either sampled edge family. This is still an upper bound for the cross-family meeting event of the two coalescing pairs.

To see this pathwise, realize each coalescing pair from two independent paths and, after its within-family meeting, choose one constituent path to continue as the common path. If this coalesced family later meets the other family, then one of the original constituent paths from the first family has met one of the original constituent paths from the second family. Thus every cross-family interaction of the coalescing families is contained in the union of the four independent cross-pair meeting events appearing in source (5.5).

Therefore

\[
|\operatorname{Cov}(Y_e,Y_f)|
\le \mathbf P^G(\tau^{e,f}\le t),
\]

where the right-hand side can be taken to be the source interaction event.

This addresses the main possible failure mode flagged in the assignment: within-family coalescence does **not** generate an additional interaction outside (5.5).

### 4.3 Unoriented versus oriented edge averaging

There are `m=dn/2` unoriented edges. A uniformly sampled unoriented edge, followed by an independent fair orientation, assigns probability

\[
\frac1{2m}=\frac1{dn}
\]

to each oriented edge `(x,y)`. Since `pi(x)=1/n`, this is exactly

\[
\nu(x,y)=\pi(x)\frac1d\mathbf 1_{\{x\sim y\}}
\]

from Section 5 of the source.

The event in (5.5) is invariant under reversing either edge orientation. Therefore averaging the covariance bound over ordered pairs of **unoriented** edges is identical to averaging the source interaction event under `nu tensor nu` after the harmless random orientations. Hence

\[
\frac1{m^2}\operatorname{Var}(J_t)
\le \mathbf P_{\nu\otimes\nu}^G(\tau^{e,f}\le t).
\]

Source (5.6) now gives

\[
\frac1{m^2}\operatorname{Var}(J_t)
\le4q_t^G.
\]

Since `p<=1/2`,

\[
\boxed{
\operatorname{Var}(\mathbf E[\mathcal D_t\mid H_t])
\le4p^2q_t^G\le q_t^G.
}
\]

No additional cross term exists: the law of total variance separates the initial-label variance conditional on the genealogy from the variance of the conditional mean exactly.

---

## 5. Deterministic graph inequality and the constant 2

The law of total variance gives

\[
\operatorname{Var}(\mathcal D_t)
=
\mathbf E[\operatorname{Var}(\mathcal D_t\mid H_t)]
+
\operatorname{Var}(\mathbf E[\mathcal D_t\mid H_t]).
\]

The two preceding sections bound the two terms by `q_t^G` separately. Therefore

\[
\boxed{
\operatorname{Var}_u^G(\mathcal D_t)
\le 2q_t^G.
}
\]

This proof uses only regularity for the normalization and the bound `S_v<=d|C_v|`. It does not use expansion, randomness, transitivity, or connectedness. The deterministic claim is therefore genuinely valid on arbitrary finite simple regular graphs of positive degree.

At `t=0`, `q_0^G=1/n`, so the right-hand side is `2/n`, consistent with the exact initial variance calculation below.

---

## 6. Random-regular consequence and probability mode

Fix `d>=3` and let `G` be uniform among simple `d`-regular graphs on `n` vertices. From the source inputs described in Section 1.3, for any deterministic `t_n=o(n)`,

\[
q_{t_n}^G=O_{\mathbb P}((1+t_n)/n).
\]

Combining with the deterministic inequality gives

\[
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}((1+t_n)/n).
\]

This is a sequence-wise quenched statement. No uniform-in-`t` bound is needed. More explicitly, the high-probability bounds on the spectral gap and stationary mean meeting time can be chosen with deterministic constants on an environment event whose probability tends to one, and (5.8) can then be applied at the single deterministic time `t_n`.

If `X_n(G)` denotes

\[
X_n(G)=\frac{n}{1+t_n}\operatorname{Var}_u^G(\mathcal D_{t_n}^n),
\]

then `X_n=O_P(1)`. For any deterministic `C_n->infinity`, quenched Chebyshev gives

\[
\mathbf P_u^G\left(
|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n|
>C_n\sqrt{(1+t_n)/n}
\right)
\le \frac{X_n(G)}{C_n^2}.
\]

Since an `O_P(1)` sequence divided by `C_n^2->infinity` converges to zero in environment probability, the claimed corrected concentration follows.

When `t_n>=1`, source (5.8) gives `q_{t_n}^G=O_P(t_n/n)`, hence the same calculation gives the original source scale `C_n sqrt(t_n/n)`.

The centering is the same quenched centering used by the source.

---

## 7. Small-time counterexample to literal source (1.9)

The source's quantifiers really allow `t_n->0`, so this issue must be checked rather than interpreted away.

At time zero, let

\[
a=u(1-u),\qquad I_e=\mathbf1_{\{\eta_0(x)\ne\eta_0(y)\}}
\]

for `e={x,y}`. Disjoint edges have independent indicators. Two distinct edges sharing one vertex have covariance

\[
a-4a^2=a(1-4a).
\]

Counting `m=dn/2` edges and `n binom(d,2)` unordered adjacent edge pairs gives, on every finite simple `d`-regular graph,

\[
\operatorname{Var}_u(\mathcal D_0)
=
\frac{4a\,[d-(4d-2)a]}{dn}.
\]

For fixed `d` and `u in (0,1)`, the coefficient is strictly positive.

To obtain a probability lower bound rather than only a variance lower bound, center the edge indicators. Their dependency graph is the line graph of `G`, whose degree is bounded by `2(d-1)`. Expanding the fourth moment, only index quadruples with no isolated dependency component contribute. There are `O_d(n^2)` such quadruples, so

\[
\mathbf E[(D_0-\mathbf E D_0)^4]=O_{d,u}(n^2).
\]

Paley--Zygmund applied to the square then yields constants `c_1,c_2>0`, depending only on `d,u`, such that

\[
\mathbf P_u^G\left(
|\mathcal D_0-\mathbf E\mathcal D_0|\ge c_1n^{-1/2}
\right)\ge c_2
\]

uniformly over the graph.

Now take exactly

```text
t_n = n^{-3},
C_n = log n.
```

The total voter clock rate is `n`, so the probability of no clock ring by time `t_n` is

\[
e^{-nt_n}=e^{-n^{-2}}\to1.
\]

On that event the observed discordance equals its time-zero value. Also every normalized jump has size at most `2/n`, so `|L mathcal D|<=2` and

\[
|\mathbf E\mathcal D_{t_n}-\mathbf E\mathcal D_0|\le2t_n.
\]

The source threshold is

\[
C_n\sqrt{t_n/n}=\frac{\log n}{n^2}=o(n^{-1/2}).
\]

Thus the source probability in (1.9) stays bounded away from zero along this sequence. The literal displayed open statement is false. The corrected scale `sqrt((1+t_n)/n)` retains the unavoidable initial `n^{-1/2}` fluctuation.

---

## 8. Comparison with the Professor reconstruction

Only after completing the derivation above did I read `notes/professor-assignment-002-verification.md`. I found no mathematical disagreement with it. The same two points emerged as the ones needing explicit care:

1. the coupling from two genealogical coalescing edge families to the independent-walk interaction event in source (5.5), including within-family coalescence;
2. the additive `1/n` term implicit in source (5.8) at very small times.

Both are handled correctly in the claimed theorem.

## 9. Scope

What I regard as established by this audit is exactly:

- deterministic variance inequality on every finite simple regular graph of positive degree;
- fixed-`d>=3` random-regular variance `O_P((1+t_n)/n)` for every deterministic `t_n=o(n)`;
- corrected Chebyshev concentration on scale `C_n sqrt((1+t_n)/n)`;
- source scale `C_n sqrt(t_n/n)` for deterministic `1<=t_n=o(n)`;
- failure of the literal source (1.9) for unrestricted very small times, with the stated `n^{-3}` counterexample.

No uniform-in-time supremum concentration statement is proved here or needed. No novelty or priority judgment is made.

VERDICT: PASS