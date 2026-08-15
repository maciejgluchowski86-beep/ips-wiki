# Assignment 003: infinite-front reduction and the hostile-front bottleneck

## Conclusion

For each fixed `lambda>0`, the infinite-front reduction proposed in `002-edge-environment-dual.md` is correct. The missing functional-analytic point is that cylinder functions are a core for the infinite-front generator. With that repair,

$$
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}
\mu(\lambda-u_1).
\tag{0.1}
$$

For every invariant front law,

$$
\mu(u_1=1)
=
\frac{\lambda}{1+\lambda}
\left(1+\frac12\mu(01)\right),
\tag{0.2}
$$

and hence

$$
\lim_{k\to\infty}v_k(\lambda)
=
\frac{\lambda}{1+\lambda}
\left(\lambda-rac12
\sup_{\mu\in\mathcal I_\lambda}\mu(01)\right).
\tag{0.3}
$$

So the proposed FRONT-GAP LEMMA

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda
\tag{FG}
$$

is indeed the exact finite-window target.

I did **not** prove `(FG)` for every positive `lambda`. Instead I found a distinction that should be explicit in the proof spine: the worst-invariant-front problem is stronger than positivity of the front selected from finite seeds. Martinelli--Shapira--Toninelli (2025), Application 1, together with reflection symmetry, implies that every Cesaro front limit selected from the singleton has strictly positive mean right-edge drift for every `lambda>0`. Thus any failure of `(FG)` would have to come from an additional invariant semi-infinite-tail phase not selected by the singleton dynamics.

Gap coordinates make the remaining issue structural. Away from the moving front, the process is a reversible coagulation/fragmentation system with iid geometric equilibrium gaps; the front is the only nonequilibrium forcing. A clean sufficient next lemma is therefore:

> **FRONT-UNIQUENESS LEMMA.** For every fixed `lambda>0`, the infinite right-front process has a unique invariant probability law.

This is stronger than `(FG)` but would close the all-parameter theorem immediately. I do not have a proof. A naive reset coupling by consecutive outward births is circular because later left shifts can expose the untouched tail unless positive current is already controlled.

No monotonicity or threshold statement in the parameter `lambda` is used below.

---

## 1. Infinite front process: Feller property and a core

Let

$$
E=\{0,1\}^{\mathbb N}
$$

with product topology. The implicit rightmost particle is `u_0=1`; `u_j` records the site `j` steps behind it. Define

$$
S_+u=(1,u_1,u_2,\ldots),
\qquad
S_-u=(u_2,u_3,\ldots).
$$

On cylinder functions,

$$
\begin{aligned}
Q_\infty f(u)
={}&\lambda[f(S_+u)-f(u)]
+u_1[f(S_-u)-f(u)]\\
&+\sum_{j\ge1}(u_{j-1}+u_{j+1})
[\lambda(1-u_j)+u_j]
[f(u^{(j)})-f(u)].
\end{aligned}
\tag{1.1}
$$

Only finitely many terms affect a cylinder function.

### Proposition 1.1

`Q_infinity` generates a conservative Feller process on `E`; cylinder functions are a core; and the invariant-law set `I_lambda` is nonempty.

### Proof

Write `Q_infinity=A+B`, where `A` is the standard half-line finite-range spin generator with fixed boundary `u_0=1` and

$$
Bf
=\lambda(f\circ S_+-f)+u_1(f\circ S_--f).
$$

The rates in `A` are uniformly bounded and finite-range, so the standard graphical construction yields a Feller semigroup and cylinders are a core. The maps `S_+` and `S_-` are continuous, and

$$
\|Bf\|_\infty\le2(\lambda+1)\|f\|_\infty.
$$

`B` is itself a bounded Markov jump generator. Bounded perturbation, or equivalently the Trotter product construction for `A` and `B`, yields a conservative Feller semigroup for `A+B`. Since `B` is bounded, the graph norms of `A` and `A+B` are equivalent; cylinders remain a core.

Finally `E` is compact, so Krylov--Bogoliubov averaging gives an invariant probability law. `square`

---

## 2. Exact finite LP dual

For `E_k={0,1}^k`, separate the raw edge displacement from the verified finite-window drift:

$$
D_{k,\lambda}(u,z;\phi)
=\lambda-u_1+Q_k^z\phi(u).
\tag{2.1}
$$

Thus

$$
v_k(\lambda)
=\sup_\phi\min_{u,z}
[\lambda-u_1+Q_k^z\phi(u)].
\tag{2.2}
$$

Let `M_k` be the set of nonnegative arrays `m(u,z)` satisfying

$$
\sum_{u,z}m(u,z)=1
\tag{2.3}
$$

and

$$
\sum_{u,z}m(u,z)Q_k^z f(u)=0
\qquad\text{for every }f:E_k\to\mathbb R.
\tag{2.4}
$$

`M_k` is nonempty: fix a deterministic exterior policy and take a stationary law of the resulting finite chain.

### Proposition 2.1

$$
v_k(\lambda)
=\min_{m\in M_k}\sum_{u,z}m(u,z)(\lambda-u_1)
=\lambda-\max_{m\in M_k}\sum_{u,z}m(u,z)u_1.
\tag{2.5}
$$

### Proof

The primal inequalities are

$$
-Q_k^z\phi(u)+v\le\lambda-u_1.
$$

Assigning a nonnegative dual multiplier to each inequality gives (2.3) from the coefficient of `v` and (2.4) from the coefficients of `phi`. The primal is feasible with `phi=0` and sufficiently negative `v`; the dual is feasible and has bounded objective. Finite-dimensional strong LP duality gives (2.5), with attainment. `square`

The adversarial exterior bit in the finite corrector problem is therefore exactly a stationary boundary control in the dual problem.

---

## 3. Exact infinite-front limit of the LPs

Put

$$
b(u)=\lambda-u_1,
\qquad
s_*(\lambda)=\inf_{\mu\in\mathcal I_\lambda}\mu(b).
$$

### Theorem 3.1

For every fixed `lambda>0`,

$$
\boxed{
\lim_{k\to\infty}v_k(\lambda)=s_*(\lambda).
}
\tag{3.1}
$$

### Upper bound

If `mu in I_lambda`, define

$$
m_k(u,z)=\mu(U_1,\ldots,U_k=u,U_{k+1}=z).
$$

For `f:E_k->R`, viewed as a cylinder on `E`,

$$
Q_\infty f=Q_k^{U_{k+1}}f
\tag{3.2}
$$

pointwise. Invariance makes `m_k` dual-feasible, hence

$$
v_k(\lambda)\le\mu(b).
$$

Therefore

$$
v_k(\lambda)\le s_*(\lambda).
\tag{3.3}
$$

### Reverse bound and the arbitrary-extension issue

Choose a dual minimizer `m_k`, let `rho_k` be its marginal on `E_k`, and extend `rho_k` arbitrarily to a probability law `tilde rho_k` on `E`, preserving its first `k` coordinates. Along a subsequence,

$$
\widetilde\rho_{k_n}\Longrightarrow\mu
$$

by compactness.

Fix a cylinder `f` depending on the first `ell` bits. Once `k_n>=ell+1`, `Q_infinity f` depends only on the first `ell+1` coordinates. Equivalently `Q_{k_n}^z f` is independent of the exterior control `z`. Thus the arbitrary extension after coordinate `k_n` is irrelevant and

$$
\widetilde\rho_{k_n}(Q_\infty f)
=\sum_{u,z}m_{k_n}(u,z)Q_{k_n}^z f(u)
=0.
\tag{3.4}
$$

Passing to the limit gives

$$
\mu(Q_\infty f)=0
$$

for every cylinder `f`.

By Proposition 1.1 cylinders are a core. Graph-norm approximation extends the identity to every `f in D(Q_infinity)`. If `P_t` is the Feller semigroup, then for `f in D(Q_infinity)`,

$$
\frac d{dt}\mu(P_t f)
=\mu(Q_\infty P_t f)=0,
$$

since `P_tD(Q_infinity) subset D(Q_infinity)`. Density of the generator domain in `C(E)` then gives `mu P_t=mu`. Hence `mu in I_lambda`.

The objective is the continuous first-coordinate function `b`, so

$$
\lim_n v_{k_n}(\lambda)=\mu(b)\ge s_*(\lambda).
\tag{3.5}
$$

For fixed `lambda`, the already proved nesting

$$
v_{k+1}(\lambda)\ge v_k(\lambda)
$$

makes the full sequence converge. Combining (3.3)--(3.5) proves (3.1). `square`

### Corollary 3.2

For fixed `lambda>0`, the following are equivalent:

1. `v_k(lambda)>0` for some finite `k`;
2. `lim_k v_k(lambda)>0`;
3. `inf_{mu in I_lambda} mu(lambda-u_1)>0`.

This is pointwise in `lambda`; no interval structure in the parameter is asserted.

---

## 4. First-bit balance and the exact FRONT-GAP criterion

Fix `mu in I_lambda` and set

$$
r=\mu(u_1=1),
\qquad
a=\mu(u_1=0,u_2=1),
\qquad
q=\frac{\lambda}{1+\lambda}.
$$

When `u_1=0`, its total `0->1` rate is

$$
\lambda+\lambda(1+u_2)=\lambda(2+u_2).
$$

When `u_1=1`, local death occurs at rate `1+u_2`, while edge death followed by the left shift changes the new first bit to zero exactly when `u_2=0`, at rate `1-u_2`. Thus the total `1->0` rate is identically two.

Stationarity gives

$$
\lambda[2(1-r)+a]=2r,
$$

hence

$$
\boxed{
r=q\left(1+\frac a2\right)
}
\tag{4.1}
$$

and

$$
\boxed{
\mu(\lambda-u_1)
=q\left(\lambda-\frac12\mu(01)\right).
}
\tag{4.2}
$$

Combining with Theorem 3.1 gives (0.3). Therefore `(FG)` is exactly equivalent to positive worst invariant front drift. For `lambda>1/2`, `(FG)` is trivial from `mu(01)<=1`; the hard regime is small `lambda`.

---

## 5. Every invariant front law has infinitely many tail particles

Let

$$
\mathcal F
=\left\{u:\sum_{j\ge1}u_j<\infty\right\}.
$$

Starting from a finite tail, the absolute BABP has finitely many particles at every finite time almost surely: its particle number is dominated by a finite-rate branching process. Starting from an infinite tail, it remains infinite at every fixed positive time almost surely. To see the latter, choose an infinite subset of initially occupied sites separated by distance at least three. In the standard bounded-rate graphical construction, each selected site's state is unchanged if its own dominating site-clock has no ring up to time `t`; these no-ring events are independent with a common positive probability. Borel--Cantelli therefore leaves infinitely many of the selected particles untouched. Frame shifts do not change the absolute number of particles.

Hence `F` and its complement are invariant events.

Suppose `mu in I_lambda` has `mu(F)>0`. Conditioning on `F` yields an invariant law `mu_F` supported on finite nonempty configurations. Let

$$
N(u)=1+\sum_{j\ge1}u_j.
$$

Martinelli--Shapira--Toninelli (2025), Application 1, proves that from every finite nonempty initial configuration

$$
N_t\longrightarrow\infty
\qquad\text{a.s.}
$$

indeed with linear growth. Therefore, for every fixed `M`, dominated convergence gives

$$
\mathbf P_{\mu_F}(N_t\le M)\longrightarrow0.
$$

Stationarity makes this probability equal to `mu_F(N<=M)` for every `t`. Since `N<infinity` almost surely under `mu_F`, some `M` has positive mass, a contradiction. Thus

$$
\boxed{
\mu(\mathcal F)=0
\quad\text{for every }\mu\in\mathcal I_\lambda.
}
\tag{5.1}
$$

---

## 6. Exact gap process and reversible bulk

By (5.1), under an invariant front law enumerate particles

$$
x_0=0>x_1>x_2>\cdots
$$

and set

$$
g_i=x_{i-1}-x_i-1\in\mathbb N_0.
$$

The exact gap dynamics is:

1. **Front birth**, rate `lambda`:
   $$
   (g_1,g_2,\ldots)\mapsto(0,g_1,g_2,\ldots).
   $$
2. **Front death**, rate one when `g_1=0`:
   $$
   (0,g_2,g_3,\ldots)\mapsto(g_2,g_3,\ldots).
   $$
3. **Fragmentation.** A gap `n>1` makes either
   $$
   n\mapsto(0,n-1),
   \qquad n\mapsto(n-1,0),
   $$
   each at rate `lambda`. For `n=1`, both channels lead to `(0,0)`, total rate `2lambda`.
4. **Coagulation.** The particle between adjacent gaps `(a,b)` dies at rate
   $$
   1_{\{a=0\}}+1_{\{b=0\}},
   $$
   and
   $$
   (a,b)\mapsto a+b+1.
   $$

The boundary particle-index current is

$$
J(\mu)=\lambda-\mu(g_1=0)=\mu(\lambda-u_1).
\tag{6.1}
$$

Put

$$
p=\frac1{1+\lambda},
\qquad
q=\frac{\lambda}{1+\lambda},
\qquad
\gamma(n)=q p^n.
$$

The iid product geometric gap law is the gap form of Bernoulli equilibrium. Every bulk fragmentation/coagulation pair satisfies detailed balance because

$$
\frac{\gamma(0)\gamma(n-1)}{\gamma(n)}
=\frac qp=\lambda.
\tag{6.2}
$$

For `n=1`, the common factor two appears on both sides.

The front boundary is the only nonequilibrium drive. Relative to the geometric reference, the prepend/delete-zero pair has activity ratio

$$
\frac\lambda{\gamma(0)}
=\frac\lambda q
=1+\lambda>1.
\tag{6.3}
$$

This suggests an entropy/current route: in a finite system with no second reservoir, positive affinity would force nonnegative stationary current. On the half-line, however, a semi-infinite tail can in principle supply compensating entropy/current from particle-index infinity. I have not proved the required no-incoming-flux statement, so (6.3) is structural evidence rather than a proof of `(FG)`.

---

## 7. The one-gap hierarchy and a sharp local no-go

The target event `01` is exactly `{g_1=1}`. The first gap is not autonomous because deaths can expose or merge with `g_2`. For example, writing `p_n=mu(g_1=n)`, stationarity of `{g_1=1}` gives

$$
3\lambda p_1
+\mu(g_1=1,g_2=0)
=
\lambda p_2
+\mu(g_1=0,g_2=1)
+2\mu(g_1=0,g_2=0).
\tag{7.1}
$$

Thus the first closed balance (4.1) is exceptional; the next equation already requires the second gap.

There is also a rigorous no-go showing that deeper information is essential. Consider any corrector

$$
H=R+h(g_1),
$$

with arbitrary `h:N_0->R`, and fix `h(0)=0`, `h_1=h(1)`. If its drift were strictly positive in every gap state, then the state `(g_1,g_2)=(0,0)` would give

$$
\mathcal LH=\lambda-1+2h_1>0,
$$

so

$$
h_1>\frac{1-\lambda}{2}.
\tag{7.2}
$$

On the other hand, in a state `g_1=1`, `g_2>0`, three rate-`lambda` births have increments `1-h_1`, `-h_1`, `-h_1`, while no adjacent-particle death can enlarge the first gap. Hence

$$
\mathcal LH=\lambda(1-3h_1)>0,
$$

so

$$
h_1<\frac13.
\tag{7.3}
$$

Equations (7.2)--(7.3) force

$$
\lambda>\frac13.
\tag{7.4}
$$

Thus no corrector seeing only the nearest gap can improve the old `1/3` boundary. The verified smaller-parameter correctors necessarily exploit deeper gap correlations.

---

## 8. Positive all-parameter current for the front selected by a singleton

This is the main positive result of the front-gap attack.

Start BABP from `{0}`. Let `U_t` be its right-edge environment and `R_t,L_t` its outer edges. The exact compensator gives

$$
\mathbf E R_t
=\int_0^t\mathbf E[\lambda-U_1(s)]\,ds.
\tag{8.1}
$$

Martinelli--Shapira--Toninelli Application 1 gives a constant `c_lambda>0` such that the particle number has a linear lower bound with exponentially small failure probability. In particular,

$$
\liminf_{t\to\infty}\frac{\mathbf E|B_t|}{t}
\ge c_\lambda>0.
\tag{8.2}
$$

Since

$$
R_t-L_t\ge |B_t|-1
$$

and the singleton law is reflection symmetric,

$$
\mathbf E R_t=-\mathbf E L_t.
$$

Therefore

$$
\liminf_{t\to\infty}\frac{\mathbf E R_t}{t}
\ge\frac{c_\lambda}{2}>0.
\tag{8.3}
$$

Define Cesaro front laws

$$
\overline\mu_t
=\frac1t\int_0^t\operatorname{Law}(U_s)\,ds.
$$

Every weak limit is invariant: for a cylinder `f`,

$$
\overline\mu_t(Q_\infty f)
=\frac{\mathbf E[f(U_t)-f(U_0)]}{t}\to0,
$$

and the core argument from Section 3 applies. Moreover (8.1) gives

$$
\overline\mu_t(\lambda-u_1)
=\frac{\mathbf E R_t}{t}.
$$

Hence every Cesaro limit `mu_phys` selected from the singleton satisfies

$$
\boxed{
\mu_{\rm phys}(\lambda-u_1)
\ge\frac{c_\lambda}{2}>0.
}
\tag{8.4}
$$

Therefore the finite-seed front itself has positive invariant current at every positive parameter. The only possible obstruction in Theorem 3.1 is an additional invariant semi-infinite-tail phase with smaller, possibly nonpositive, current.

---

## 9. Why the hostile-phase issue is real rather than formal

At `lambda=0`, the front process is highly nonunique. For example

$$
(0,1,0,1,0,1,\ldots)
$$

is absorbing: there are no births, no adjacent tail particles can die, and `u_1=0` prevents front death. Many other hard-core tails with `u_1=0` are likewise absorbing.

This is **not** a counterexample for any positive `lambda`, but it shows that the limit `lambda downarrow0` is singular. Front uniqueness for positive `lambda` cannot be justified by continuity from zero.

It also clarifies why the finite LP is stronger than finite-seed growth. An obstruction that survives all window sizes converges, by Theorem 3.1, to a genuine invariant semi-infinite front law. Application 1 controls only the finite-tail basin selected from finite seeds and does not exclude another phase at infinity.

---

## 10. Precise next lemma

The clean sufficient statement is:

### FRONT-UNIQUENESS LEMMA

For every fixed `lambda>0`, `Q_infinity` has a unique invariant probability law `mu_lambda`.

If true, the unique law is necessarily a Cesaro limit from the singleton, so (8.4) yields

$$
\mu_\lambda(\lambda-u_1)>0.
$$

Theorem 3.1 then implies

$$
\lim_k v_k(\lambda)>0.
$$

Since `v_k(lambda)` is nondecreasing in `k`, some finite window has positive drift. Verified `BABP-CONV-001` then yields finite-seed convergence at that fixed `lambda`. Doing this pointwise for every `lambda>0` proves the all-parameter theorem.

Uniqueness is stronger than necessary. A weaker sufficient phase-selection statement is that every invariant front law lies in the closed convex hull of the singleton Cesaro limit set; (8.4) would then give the same positive lower bound on all invariant currents.

I do not have a proof of either statement. A coupling based only on long runs of outward births is circular because later edge deaths can shift the frame back into the unrefreshed tail. The reversible-gap/positive-boundary-affinity structure in Section 6 suggests an entropy-production proof if one can rule out incoming entropy flux from particle-index infinity; that is the most concrete alternate route I see.

---

## Handoff

```text
front reduction verified; front-gap lemma not proved.

Exact fixed-lambda theorem:

    lim_{k->infinity} v_k(lambda)
      = inf_{mu invariant for Q_infinity}
          mu(lambda-u_1)

and every invariant front law satisfies

    mu(lambda-u_1)
      = [lambda/(1+lambda)]
        [lambda - mu(01)/2].

New all-parameter positive result:
Every Cesaro front limit selected from the singleton satisfies

    mu(lambda-u_1) >= c_lambda/2 > 0,

by Martinelli--Shapira--Toninelli Application 1 plus reflection symmetry.
Thus the only possible obstruction to the finite-window method is an additional
invariant semi-infinite-tail phase not selected from finite seeds.

Structural reduction:
In particle-gap coordinates the bulk is reversible coagulation/fragmentation
with iid geometric gaps gamma(n)=q p^n. The moving front is the only drive,
with boundary activity ratio lambda/q=1+lambda.

Rigorous local no-go:
Any corrector R+h(g_1) with uniform positive drift requires lambda>1/3.
Small-parameter progress must use correlations beyond the nearest gap.

Precise sufficient next lemma:
FRONT-UNIQUENESS -- Q_infinity has a unique invariant probability law for every
fixed lambda>0.

File:
research/active/babp-finite-seed/students/student-b/003-front-gap.md
```
