# Independent correctness review A: BABP corrector to finite-seed convergence

Date: 2026-08-15

Role: fresh independent correctness reviewer. I did not participate in the construction of the finite-window corrector or the convergence proof. I treated the repository arguments as claims to be rederived. I used the already independently audited `BABP-EDGE-001` only for its exact stated content: a statewise corrector inequality is available at `lambda=1/40`.

## Verdict

The claim survives hostile review.

For fixed `lambda>0`, the statewise hypothesis

$$
(EC)\qquad D_{k,\lambda}(u,z;\phi)\ge v>0
$$

for every edge word `u` and exterior bit `z` does imply local convergence of one-dimensional BABP from every finite nonempty deterministic initial set to Bernoulli equilibrium of particle density

$$
q=\frac{\lambda}{1+\lambda}.
$$

The statewise character of `(EC)` is genuinely load-bearing. Bare conclusions about the two outer edges, such as positive `liminf`/negative `limsup` velocities, do not supply the internal-gap estimate used below. The verified ten-site certificate at `lambda=1/40` supplies exactly the stronger statewise premise, so the corollary at `lambda=1/40` follows.

I found two minor rigor points that should be made explicit in a polished proof: the exponential test function should be handled by localization because it is unbounded as the gap width grows, and the infinite-space compensator sum should first be written with a finite spatial truncation and then passed to the limit by monotone convergence. Both repairs are standard and preserve the claimed theorem without any additional assumption.

## 1. Convention and transition rule

I use the project's particle convention. If `B subset Z` is the finite occupied set and

$$
N_x(B)=\mathbf 1_{\{x-1\in B\}}+\mathbf 1_{\{x+1\in B\}},
$$

then

$$
0\to1\text{ at rate }\lambda N_x(B),
\qquad
1\to0\text{ at rate }N_x(B).
$$

Thus every transition is a single-site flip. A nonempty finite configuration cannot hit the empty set: when only one particle remains its death rate is zero. The finite-particle chain is nonexplosive; its total jump rate is at most a constant times `|B|`, and each jump changes `|B|` by one.

The exact right-edge corrector generator used in `(EC)` has already been independently audited in `audits/001-edge-corrector-audit.md`. For the present review, the important point is that `(EC)` is uniform over every finite nonempty configuration because it is uniform over every possible local edge state `(u,z)`.

## 2. Gap genealogy

An internal gap is a maximal nonempty finite interval of vacant sites strictly between the leftmost and rightmost particles.

### Birth at width one

A genuinely new internal gap can only be created by death of a particle with both nearest neighbours occupied. The resulting vacant interval is the singleton consisting of the death site.

Indeed, if exactly one neighbour is vacant, the death merely extends the already existing vacant interval adjacent to that neighbour. If both neighbours are vacant, the particle has death rate zero. A death at an outer edge changes the outer edge and does not nucleate an internal gap.

Hence every post-time-zero internal-gap genealogy begins at width one.

### No splitting

For a positive gap of width at least two, a vacant site strictly inside the gap has two vacant neighbours and therefore birth rate zero. The only possible births into the gap are at its endpoint vacancies, each adjacent to a bounding particle. Such a birth shrinks the gap by one. At width one, the unique vacancy has two occupied neighbours and fills at total rate `2 lambda`, closing the gap. No birth can split a positive gap into two positive gaps.

### No merger of two positive gaps

Suppose two positive gaps are separated by a block of particles. Deaths at exposed particles can shorten that separating block. If the block reaches one particle, however, that particle has a vacant neighbour on each side, hence death rate zero. It cannot disappear while both gaps remain positive.

Thus two positive gaps cannot merge. One of them may first close, after which the surviving genealogy continues normally, but there is no merger of two live genealogies.

These facts are exactly what is needed for a compensator indexed by gap nucleations. There is a well-defined descendant gap from each birth until closure.

## 3. Corrector on a tagged internal gap

Fix a tagged gap before its closure. Let `A` be all particles to its left and `C` all particles to its right. Write

$$
a=R(A),\qquad b=L(C),\qquad g=b-a-1\ge1.
$$

Both `A` and `C` are finite and nonempty throughout the lifetime of the gap.

For `g>=2`, no nearest-neighbour transition sees particles from both sides of the gap. The transitions affecting `A` have exactly the same rates as in a standalone BABP configuration `A`, and similarly for `C`. In particular, the gap-side vacancy is simply empty exterior space for the relevant inner edge.

At `g=1`, the only cross-gap issue is the sole vacant site. It has two occupied neighbours and hence flips to occupied at total rate `2 lambda`. This rate is the sum of the rate-`lambda` right birth of `A` and the rate-`lambda` left birth of `C`. Either contribution closes the tagged gap. There is no additional simultaneous event. Death of either bounding particle is still determined only by its particle-side neighbour because the gap-side neighbour is vacant.

Define the reflected left corrector by

$$
H_R(A)=R(A)+\phi(U_R(A)),
\qquad
H_L(C)=L(C)-\phi(U_L(C)).
$$

The statewise hypothesis `(EC)` and reflection give, for every finite nonempty `A,C`,

$$
\mathcal L H_R(A)\ge v,
\qquad
\mathcal L H_L(C)\le -v.
$$

Consequently, for

$$
Z=H_L(C)-H_R(A)-1
  =g-\phi(U_L(C))-\phi(U_R(A)),
$$

the product generator before closure satisfies

$$
\mathcal L^{\times}Z\le-2v.
$$

This is uniform in the gap width, its age, its location, the surrounding finite configuration, and the total particle number. This is the step for which a bare outer-edge speed theorem would be insufficient: the proof needs the generator inequality for the particular populations bordering the currently tagged gap.

If `K=||phi||_infinity`, then while the gap is alive

$$
g-2K\le Z\le g+2K.
$$

Singleton side populations cause no exception. A singleton has zero death rate at its outermost particle unless a neighbour is created; the same local edge generator formula still applies.

## 4. Killed exponential estimate and uniform tails

Only a fixed neighbourhood of the two inner edges can change `Z`. Hence there are deterministic constants `J,rho<infinity`, depending only on `(k,lambda,phi)`, such that every non-killing jump obeys

$$
|\Delta Z|\le J
$$

and the total rate of `Z`-changing events is at most `rho`. One may take, crudely,

$$
J=1+2K,
\qquad
\rho=2\bigl[\lambda+1+2k\max(1,\lambda)\bigr].
$$

At width one, replace the two rate-`lambda` closure contributions by killing. For a positive test function, the killed transition value is zero, whereas the corresponding continuation value under the product generator is positive. Therefore killing can only decrease the generator of that test function.

For `f=e^{\theta Z}` and `|y|<=J`,

$$
e^{\theta y}-1
\le \theta y+\frac{\theta^2}{2}e^{\theta J}y^2.
$$

Thus on every alive state,

$$
\frac{\mathcal L^\dagger f}{f}
\le -2v\theta
   +\frac{\theta^2}{2}e^{\theta J}\rho J^2.
$$

Choose `theta>0` sufficiently small that the second term is at most `v theta`; then

$$
\mathcal L^\dagger e^{\theta Z}\le-\gamma e^{\theta Z},
\qquad
\gamma=v\theta>0.
$$

For complete rigor, apply Dynkin's formula first after stopping when `g` reaches a finite level (and, if desired, after a finite jump-count localization), then let the localization level tend to infinity. This avoids using an unbounded test function outside its justified generator domain.

If a gap is born at width one, `Z_0<=1+2K`, while on survival `Z_t>=1-2K`. The killed semigroup estimate therefore gives a uniform lifetime tail

$$
\mathbf P(\tau>t)\le C_0e^{-\gamma t}.
$$

Likewise, stopping at

$$
\sigma_m=\inf\{t<\tau:g_t\ge m\}
$$

gives

$$
\mathbf P(\sigma_m<\tau)\le C_1e^{-\theta m}.
$$

The constants are uniform over the surrounding state and birth location. An initial deterministic gap of width `g_0` has the same exponential lifetime decay with a finite prefactor depending on `g_0`, which is sufficient because there are only finitely many initial gaps.

## 5. Boundary displacement

Let `N_t` count shifts of either endpoint of the tagged vacant interval before closure, keeping the count constant after closure.

Each endpoint can extend by one only when its bounding particle dies. Since its neighbour on the gap side is vacant, that death occurs at rate at most one and, if it occurs, the neighbour on the particle side must be occupied; consequently the endpoint moves exactly one lattice step, never farther. Each endpoint can shrink by one through a birth into its adjacent vacancy at rate at most `lambda`. At width one the closing vacancy has the two rate-`lambda` birth contributions, giving total rate `2 lambda`.

Therefore the predictable intensity of `N` is at most

$$
\beta=2(1+\lambda).
$$

Equivalently, using the graphical construction or the standard exponential bound for counting processes with bounded intensity,

$$
N_t\preceq \operatorname{Pois}(\beta t).
$$

If the gap is born as `{x}` and contains the origin at age `t`, then some endpoint has moved from `x` to the other side of, or to, zero. Since each endpoint change is one lattice step,

$$
N_t\ge |x|.
$$

If `E_{m,t,x}` is the event that the gap born at `x` is alive at age `t`, has width at least `m`, and contains zero, then

$$
E_{m,t,x}\subset
\{\sigma_m<\tau\}\cap\{\tau>t\}\cap\{N_t\ge|x|\}.
$$

No independence is needed: for three events with probabilities at most `a,b,c`, the probability of their intersection is at most `min(a,b,c)<= (abc)^{1/3}`. Hence

$$
\mathbf P(E_{m,t,x})
\le C e^{-c_1m}e^{-c_2t}
   \mathbf P(\operatorname{Pois}(\beta t)\ge|x|)^{1/3}.
$$

Finally,

$$
\sum_{x\in\mathbb Z}
\mathbf P(\operatorname{Pois}(\beta t)\ge|x|)^{1/3}
\le C_\beta(1+t).
$$

To see this directly, bound the `O(1+t)` terms with `|x|` up to a fixed multiple of `beta t+1` by one. Beyond that cutoff, the Chernoff estimate

$$
\mathbf P(\operatorname{Pois}(\beta t)\ge n)
\le (e\beta t/n)^n
$$

remains exponentially summable after taking the one-third power.

## 6. Compensator over nucleations

A new gap is nucleated at `x` only when the occupied site `x` dies while both neighbours are occupied. Its predictable intensity is therefore bounded by `2` at each site.

For rigor, first count nucleations with `|x|<=N`. By the strong Markov property at a nucleation time and the uniform tagged-gap estimate above, the expected number of such nucleations whose descendant gap at time `t` contains zero and has width at least `m` is bounded by

$$
2\sum_{|x|\le N}\int_0^t
 C e^{-c_1m}e^{-c_2(t-s)}
 \mathbf P(\operatorname{Pois}(\beta(t-s))\ge|x|)^{1/3}\,ds.
$$

The probability that at least one genealogy contributes is bounded by this expected count. Let `N->infinity`. Monotone convergence and the spatial summability just proved yield

$$
\begin{aligned}
\mathbf P(&\text{a post-time-zero gap of width at least }m
\text{ contains }0\text{ at time }t)\\
&\le C e^{-c_1m}\int_0^\infty e^{-c_2r}(1+r)\,dr
\le C'e^{-cm},
\end{aligned}
$$

uniformly in `t`.

There is no hidden total-particle-number factor in this estimate. Sitewise nucleation rates are summed against a spatial displacement kernel whose sum is finite. Nonexplosion ensures only finitely many actual jumps on each bounded time interval, and non-merger/non-splitting gives each nucleation an unambiguous live genealogy until closure.

The deterministic finite initial state has finitely many initial internal gaps. The lifetime estimate makes the probability that any fixed initial gap survives until time `t` tend to zero exponentially. Therefore, with

$$
G_m(t)=\{0\text{ lies in an internal gap of width at least }m\},
$$

we obtain the genuinely late-time-uniform statement

$$
\limsup_{t\to\infty}\mathbf P_B(G_m(t))\le Ce^{-cm}.
$$

This is not merely a per-gap estimate.

## 7. Nonescape from fixed windows

The statewise corrector also gives the already audited outer-edge conclusions

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v,
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-v
\quad\text{a.s.}
$$

For fixed `M`, it follows that

$$
\mathbf P_B(R(B_t)\le M\text{ or }L(B_t)\ge-M)\longrightarrow0.
$$

On the complementary event, particles lie strictly on both sides of `[-M,M]`. If the whole window is nevertheless empty, then `[-M,M]` is contained in an internal gap of width at least `2M+1`. Consequently

$$
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le
\mathbf P_B(R_t\le M\text{ or }L_t\ge-M)
+\mathbf P_B(G_{2M+1}(t)).
$$

Taking `limsup` gives

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM},
$$

and hence

$$
\lim_{M\to\infty}\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)=0.
$$

This is the needed nonescape estimate.

## 8. External stationary-limit inputs

I independently checked the two external interfaces rather than relying on the project summaries.

### Weak limit points are stationary

The classical Mountford record does state the relevant one-dimensional principle for a large class of finite-state interacting particle systems, and Ramírez--Varadhan is a later relative-entropy route to the same phenomenon. I did not rely on an uninspected reconstruction of their exact hypotheses, because there is now a clean current primary source that directly covers BABP.

Jahnel--Köppl, *Restriction and mixing properties of interacting particle systems with unbounded range*, arXiv:2603.21817, Theorem 2.5, proves that for an interacting particle system on `Z` satisfying their bounded-rate/bounded-update and exponentially decaying influence assumptions, every weak limit point of the measure-valued dynamics is stationary. The theorem explicitly does not require shift invariance or reversibility.

BABP satisfies the assumptions in the present convention: the local state space is finite; updates are single-site; the rate at which any fixed site changes is at most `2 max(1,lambda)`; and the flip rate depends only on the two nearest neighbours, so the influence is finite-range and therefore satisfies every required exponential-decay bound. Thus the stationary-limit theorem applies for every fixed `lambda>0`, including `1/40`.

### Stationary-law classification and normalization

Martinelli--Shapira--Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461, define BABP in variables where state `0` is an infection and

$$
c_x=2-\eta_{x-1}-\eta_{x+1}
$$

is the number of infected neighbours. Their flip generator gives infected-to-healthy rate `p c_x` and healthy-to-infected rate `q c_x`, with `p=1-q`. They set

$$
\lambda=q/p.
$$

After the constant time-rescaling by `1/p`, these become exactly death rate `1` and birth rate `lambda` per infected neighbour, as in this project. Stationary measures are unchanged by this constant time-rescaling, and `q=lambda/(1+lambda)`.

Their Corollary 2.9 states directly that every stationary law of one-dimensional BABP is a convex combination of product Bernoulli equilibrium and the completely healthy configuration. In particle-set notation this is

$$
\nu=\alpha\delta_\varnothing+(1-\alpha)\pi_q,
\qquad \alpha\in[0,1].
$$

The same paper, Remark 5.4, records the historical finite-seed convergence range `lambda>0.0347` after the earlier `lambda>1/3` result. Sudbury's 1999 abstract independently records the `0.0347` extension. Thus there is no convention or normalization mismatch in the external inputs used here.

## 9. Final subsequence argument

The configuration space `{0,1}^Z` is compact in the product topology. Given any sequence `t_n->infinity`, extract a weakly convergent subsequence with limit `nu`. The stationary-limit theorem makes `nu` stationary, hence

$$
\nu=\alpha\delta_\varnothing+(1-\alpha)\pi_q.
$$

For fixed `M`, the cylinder event

$$
\{B\cap[-M,M]=\varnothing\}
$$

is clopen. Therefore its probability converges along the chosen subsequence, and the nonescape estimate gives

$$
\nu(B\cap[-M,M]=\varnothing)\le Ce^{-cM}.
$$

On the other hand, the mixture formula gives

$$
\nu(B\cap[-M,M]=\varnothing)
=\alpha+(1-\alpha)(1-q)^{2M+1}\ge\alpha.
$$

Letting `M->infinity` yields `alpha=0`. Hence every subsequential limit equals `pi_q`. Compactness then implies convergence of the full trajectory:

$$
\operatorname{Law}_B(B_t)\Longrightarrow\pi_q.
$$

The clopen-cylinder argument and the order of limits are correct.

## 10. Scope

The proof requires the initial configuration to be:

- nonempty, so its outer edges and the edge correctors are defined and the process stays nonempty;
- finite, so the edge populations are finite at finite times and there are only finitely many initial internal gaps;
- deterministic only to keep initial-state-dependent constants nonrandom in the statement.

No connectedness assumption is used. No parity assumption is used. No lower bound on the initial number of particles is used. In particular, a singleton seed is covered.

The Martinelli--Shapira--Toninelli particle-number growth theorem is not used anywhere in this bridge.

A random almost surely finite nonempty initial state could likely be handled by conditioning with an integrability/tightness check on the initial-gap prefactors, but that extension is not part of the claim and I do not certify it here.

## 11. Concrete `lambda=1/40` corollary

`BABP-EDGE-001` has already been independently verified and supplies, at

$$
\lambda=\frac1{40},\qquad k=10,
$$

a bounded corrector satisfying the statewise inequality with

$$
v=\frac{1033}{40000000}>0.
$$

That is exactly hypothesis `(EC)`, not merely its outer-edge consequence. Applying the theorem just checked gives local convergence from every finite nonempty deterministic seed at `lambda=1/40=0.025`. Since `0.025<0.0347`, this lies strictly below the previously published finite-seed convergence range.

## 12. Corrections recommended for the proof record

These are rigor/exposition corrections, not theorem restrictions.

1. In the exponential-tilting step, explicitly localize before applying Dynkin's formula or optional stopping to `e^{theta Z}`, since it is unbounded as `g->infinity`, and then remove the localization.
2. In the nucleation-compensator step, first sum over `|x|<=N` and then pass `N->infinity` by monotone convergence using the proved spatial summability. This makes the infinite-space point-process argument completely explicit.
3. For external theorem attribution, the current Jahnel--Köppl Theorem 2.5 is a cleaner directly checked stationary-limit input than relying on a partial reconstruction of Mountford/Ramírez--Varadhan hypotheses. Mountford/Ramírez--Varadhan remain valid historical provenance, but they are not needed as an unchecked black box.

No change to `BABP-CONV-001`'s theorem statement is required.

```text
VERIFIED
```
