# Finite-window edge correctors and finite-seed convergence for the one-dimensional biased annihilating branching process

Working research-note draft. Mathematical content is based on verified project claims `BABP-EDGE-001` and `BABP-CONV-001`. Priority language is intentionally conservative pending full-text comparison with Sudbury (1998, 1999).

## Abstract

Consider the one-dimensional biased annihilating branching process (BABP) in particle variables, with a vacant site becoming occupied at rate `lambda` times the number of occupied nearest neighbours and an occupied site becoming vacant at rate equal to that number. We prove a finite-window criterion for convergence from a deterministic finite nonempty initial configuration. If the right edge admits a bounded local corrector whose generator drift is uniformly positive in every finite-window edge state, then the process converges locally to Bernoulli product equilibrium. The proof applies the same statewise corrector to the two particle populations bordering each internal vacant gap. The resulting corrected gap width has uniformly negative drift; localization of an exponential test gives uniform lifetime and maximum-width tails, and a spatially truncated compensator over gap nucleations yields a no-escape estimate for fixed windows. Stationarity of subsequential limits and the one-dimensional classification of stationary BABP laws then identify the limit.

An exact rational ten-site certificate satisfies the criterion at

$$
\lambda=\frac1{40},
$$

with minimum statewise drift `1033/40000000`. Hence BABP at `lambda=1/40`, started from every deterministic finite nonempty particle set, converges locally to Bernoulli equilibrium of density `1/41`. This parameter lies below the `lambda>0.0347` finite-seed range recorded by Martinelli--Shapira--Toninelli (2025, Remark 5.4).

## 1. Model and result

For a configuration `xi in {0,1}^Z`, write `xi(x)=1` when there is a particle at `x` and put

$$
N_x(\xi)=\xi(x-1)+\xi(x+1).
$$

The generator acts on local functions by

$$
L f(\xi)
=
\sum_{x\in\mathbb Z}
N_x(\xi)\bigl[\lambda(1-\xi(x))+\xi(x)\bigr]
\bigl(f(\xi^x)-f(\xi)\bigr),
\tag{1.1}
$$

where `xi^x` is obtained by flipping the state at `x`. Thus

$$
0\to1\text{ at rate }\lambda N_x,
\qquad
1\to0\text{ at rate }N_x.
\tag{1.2}
$$

The nontrivial product equilibrium is Bernoulli with particle density

$$
q=\frac{\lambda}{1+\lambda}.
\tag{1.3}
$$

A finite nonempty configuration never reaches the empty state, because an isolated particle has zero death rate.

For a finite nonempty particle set `B`, write

$$
R(B)=\max B,
\qquad
L(B)=\min B.
$$

Fix `k>=1`. Seen from the right edge, define

$$
u_j(B)=\mathbf 1_{\{R(B)-j\in B\}},
\qquad j=1,\ldots,k,
$$

and one exterior bit

$$
z(B)=\mathbf 1_{\{R(B)-k-1\in B\}}.
$$

For `u=(u_1,\ldots,u_k)`, let

$$
H_R(B)=R(B)+\phi(u(B)),
\tag{1.4}
$$

where `phi:{0,1}^k -> R` is bounded.

### Theorem 1.1: statewise edge corrector implies finite-seed convergence

Fix `lambda>0`. Suppose that for some `k>=1`, bounded `phi:{0,1}^k -> R`, and `v>0`, the exact drift of (1.4) satisfies

$$
D_{k,\lambda}(u,z;\phi)\ge v
\tag{1.5}
$$

for every `u in {0,1}^k` and `z in {0,1}`. Then for every deterministic finite nonempty initial particle set `B`,

$$
\operatorname{Law}_B(B_t)\Longrightarrow\pi_q
\qquad(t\to\infty)
\tag{1.6}
$$

locally on `{0,1}^Z`, where `pi_q` is Bernoulli product measure of density (1.3).

The hypothesis is the **statewise** inequality (1.5). We do not claim that a bare positive asymptotic velocity of the two outer edges is sufficient for (1.6).

### Corollary 1.2: an exact certificate at `lambda=1/40`

At

$$
\lambda=\frac1{40},
\qquad k=10,
\tag{1.7}
$$

there is a rational corrector `phi` with

$$
D_{10,1/40}(u,z;\phi)
\ge
\frac{1033}{40000000}
>0
\tag{1.8}
$$

for all `2^11=2048` edge states. Consequently, from every deterministic finite nonempty initial set,

$$
\operatorname{Law}_B(B_t)\Longrightarrow\pi_{1/41}.
\tag{1.9}
$$

Martinelli--Shapira--Toninelli (2025), Remark 5.4, record finite-seed convergence for `lambda>0.0347`. Since `1/40=0.025`, (1.9) lies below that recorded range. We make no priority claim stronger than this comparison in the present draft.

## 2. Exact finite-window edge generator

Put `u_0=1` and `u_{k+1}=z`. Define

$$
T_+u=(1,u_1,\ldots,u_{k-1}),
$$

$$
T_-^zu=(u_2,\ldots,u_k,z),
$$

and let `u^(j)` denote the word obtained by flipping `u_j`.

There are three classes of transitions that can change `H_R`.

First, a birth at `R+1` occurs at rate `lambda`, moves the edge one step right, and changes the word to `T_+u`. Its contribution is

$$
\lambda\bigl[1+\phi(T_+u)-\phi(u)\bigr].
$$

Second, the rightmost particle can die only when `u_1=1`; then its death rate is one, the new edge is `R-1`, and the new word is `T_-^zu`. Its contribution is

$$
u_1\bigl[-1+\phi(T_-^zu)-\phi(u)\bigr].
$$

Third, for `1<=j<=k`, the recorded site `R-j` has

$$
u_{j-1}+u_{j+1}
$$

occupied neighbours. Its flip rate is

$$
(u_{j-1}+u_{j+1})\bigl[\lambda(1-u_j)+u_j\bigr],
$$

and the edge does not move. Therefore

$$
\begin{aligned}
D_{k,\lambda}(u,z;\phi)
={}&
\lambda\bigl[1+\phi(T_+u)-\phi(u)\bigr]\\
&+u_1\bigl[-1+\phi(T_-^zu)-\phi(u)\bigr]\\
&+\sum_{j=1}^k
(u_{j-1}+u_{j+1})
\bigl[\lambda(1-u_j)+u_j\bigr]
\bigl[\phi(u^{(j)})-\phi(u)\bigr].
\end{aligned}
\tag{2.1}
$$

Only one unrecorded bit is needed. A flip of the site carrying `z` may depend on the next site farther left, but that flip changes neither `R` nor the current word `u` and hence has zero instantaneous contribution to `L H_R`. Uniformity over `z=0,1` handles its future effect.

Since `phi` is bounded, `H_R` has uniformly bounded jumps and only a fixed number of local clocks can change it. After the usual localization,

$$
M_t
=H_R(B_t)-H_R(B_0)-\int_0^t L H_R(B_s)\,ds
$$

is a martingale with predictable quadratic variation bounded by `Ct`. Hence `M_t/t -> 0` almost surely. Under (1.5),

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v
\qquad\text{a.s.}
\tag{2.2}
$$

Reflection gives

$$
\limsup_{t\to\infty}\frac{L(B_t)}t\le -v
\qquad\text{a.s.}
\tag{2.3}
$$

These are lower/upper asymptotic-velocity bounds; existence of limiting edge speeds is not asserted.

## 3. The rational certificate

For `k=10` and `lambda=1/40`, the corrector is stored in exact rational form in

`research/active/babp-finite-seed/students/student-b/edge-corrector-certificate.py`.

The certificate assigns one rational value to each of the `2^10=1024` words. Substitution into (2.1) gives 2048 exact rational inequalities, one for each pair `(u,z)`. The minimum is exactly

$$
v=\frac{1033}{40000000}.
\tag{3.1}
$$

The independent audit rederived (2.1), decoded the rational vector independently, checked all 2048 inequalities, and reproduced two calibrations:

1. for `k=1`, strict feasibility holds exactly when
   $$
   \lambda>\frac13;
   \tag{3.2}
   $$
2. for `k=8`, an independent numerical LP places the zero crossing at
   $$
   0.0346195434755\ldots.
   \tag{3.3}
   $$

The second number is consistent with the historical `0.0347` threshold, but we do not infer from this numerical match that Sudbury (1999) literally used the same eight-site window or normalization.

For a publication version, the machine-readable rational vector and a minimal independent verifier should be supplementary material. The body only needs (2.1), the certificate format, the exact minimum (3.1), and a reproducibility statement.

## 4. Internal vacant gaps

An **internal gap** is a maximal nonempty finite interval of vacant sites strictly between the leftmost and rightmost particles.

Three elementary one-dimensional facts make internal gaps genealogically tractable.

**New gaps are born at width one.** A new internal vacant component is created only when a particle with both neighbours occupied dies. The resulting new gap is the singleton consisting of that site. If exactly one neighbour was vacant, the death merely enlarges an existing gap.

**A positive gap cannot split.** A vacant site strictly inside a gap has two vacant neighbours and hence birth rate zero. Births can occur only at the endpoint vacancies, shrinking the gap by one. At width one, a birth closes it.

**Two positive gaps cannot merge while both are alive.** If the particle block separating them erodes to a single particle, that particle has a vacant neighbour on each side and therefore death rate zero.

Thus each post-time-zero positive gap has a unique genealogy from nucleation to closure.

Fix one tagged live gap. Let `A_t` be all particles to its left and `C_t` all particles to its right, and write

$$
g_t=L(C_t)-R(A_t)-1\ge1.
$$

Define the reflected left-edge corrector by

$$
H_L(C)=L(C)-\phi(U_L(C)).
$$

Reflection of (1.5) gives

$$
L H_L(C)\le-v
$$

for every finite nonempty `C`. Put

$$
Z=H_L(C)-H_R(A)-1.
\tag{4.1}
$$

If `K=||phi||_infty`, then while the gap is alive,

$$
g-2K\le Z\le g+2K.
\tag{4.2}
$$

For `g>=2`, no nearest-neighbour transition sees particles on both sides of the gap, so the two side generators decouple and

$$
L^\times Z\le-2v.
\tag{4.3}
$$

At width one, the sole vacancy fills at total rate `2lambda`; either such birth closes the gap. Passing to the killed tagged-gap process only decreases the generator of a positive test function. Thus (4.3) is the drift input for the killed process as well, in the sense needed below.

This is the point where the statewise nature of (1.5) is essential. The two particle sets `A_t` and `C_t` are random internal populations created by the current gap genealogy, not the original process viewed only at its outer edges.

## 5. Localized exponential estimate

Only fixed neighborhoods of the two inner particle edges can change `Z`. Consequently there are deterministic finite constants `J` and `rho`, depending only on `(k,lambda,phi)`, such that each non-killing jump satisfies

$$
|\Delta Z|\le J
$$

and the total rate of `Z`-changing jumps is at most `rho`.

For `theta>0` and `|y|<=J`,

$$
e^{\theta y}-1
\le
\theta y+
\frac{\theta^2}{2}e^{\theta J}y^2.
$$

Using (4.3), choose `theta>0` small enough that

$$
-2v\theta+
\frac{\theta^2}{2}e^{\theta J}\rho J^2
\le-v\theta.
$$

With `gamma=v theta`, the killed generator formally satisfies

$$
L^\dagger e^{\theta Z}
\le
-\gamma e^{\theta Z}.
\tag{5.1}
$$

The exponential is unbounded as the gap width grows, so (5.1) is used only after **localization**. Let `tau_n` be the first time the live gap width, or equivalently `Z` up to the bounded correction (4.2), reaches a fixed level `n`; one may also stop after a finite number of jumps. Apply Dynkin's formula to the bounded stopped process. Then remove the jump cutoff and send `n` to infinity using positivity and Fatou/monotone localization. This is the order of argument needed to justify the unbounded exponential test.

For a gap born at width one, the result is uniform exponential control of its closure time `tau` and maximal width:

$$
\mathbf P(\tau>t)
\le C_0e^{-\gamma t},
\tag{5.2}
$$

$$
\mathbf P\left(\sup_{s<\tau}g_s\ge m\right)
\le C_1e^{-\theta m}.
\tag{5.3}
$$

The constants are independent of the gap's birth location and of the surrounding finite particle configuration.

## 6. Spatial displacement and the nucleation compensator

Let `N_t` count shifts of either endpoint of a tagged gap before it closes. At each boundary, an extension occurs only when the bounding particle dies, at rate at most `1`, and a shrinkage occurs by a birth into the adjacent vacancy at rate at most `lambda`. Therefore

$$
N_t\preceq\operatorname{Pois}(\beta t),
\qquad
\beta=2(1+\lambda).
\tag{6.1}
$$

A gap born at `x` that contains the origin at age `r` must have accumulated at least `|x|` endpoint shifts. Combining (5.2), (5.3), and (6.1) without any independence assumption gives constants `C,c_1,c_2>0` such that

$$
\mathbf P(E_{m,r,x})
\le
C e^{-c_1m}e^{-c_2r}
\mathbf P\bigl(\operatorname{Pois}(\beta r)\ge|x|\bigr)^{1/3},
\tag{6.2}
$$

where `E_{m,r,x}` is the event that the descendant gap is alive at age `r`, contains zero, and has width at least `m`. Moreover,

$$
\sum_{x\in\mathbb Z}
\mathbf P\bigl(\operatorname{Pois}(\beta r)\ge|x|\bigr)^{1/3}
\le C_\beta(1+r).
\tag{6.3}
$$

A new gap can be nucleated at a fixed site at predictable rate at most `2`. The all-space compensator is justified in the following order.

First fix `N<infinity` and count only nucleations at sites `|x|<=N`. By the strong Markov property at each nucleation time and (6.2), the expected number of such genealogies that produce a width-`m` gap containing zero at time `t` is at most

$$
2\sum_{|x|\le N}
\int_0^t
C e^{-c_1m}e^{-c_2(t-s)}
\mathbf P\bigl(\operatorname{Pois}(\beta(t-s))\ge|x|\bigr)^{1/3}
\,ds.
\tag{6.4}
$$

Only after obtaining this finite spatial sum do we send `N` to infinity. The counted events increase with `N`, so **monotone convergence** applies. Using (6.3) then yields

$$
\limsup_{t\to\infty}
\mathbf P_B(G_m(t))
\le Ce^{-cm},
\tag{6.5}
$$

where `G_m(t)` is the event that zero lies in an internal gap of width at least `m`. The finitely many gaps present at time zero contribute only exponentially decaying survival probabilities.

## 7. Nonescape from fixed windows

Fix `M`. By (2.2)--(2.3),

$$
\mathbf P_B\bigl(R(B_t)\le M\text{ or }L(B_t)\ge-M\bigr)
\longrightarrow0.
\tag{7.1}
$$

On the complementary event there are particles on both sides of `[-M,M]`. If the entire window is nevertheless empty, then it lies inside an internal gap of width at least `2M+1`. By (6.5),

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
\tag{7.2}
$$

In particular,

$$
\lim_{M\to\infty}
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)=0.
\tag{7.3}
$$

This is the target-level information not supplied by total particle-number growth alone.

## 8. Stationary limits and identification of the limit

The configuration space `{0,1}^Z` is compact, so every time sequence has weakly convergent subsequences.

Jahnel--Köppl (2026), Theorem 2.5, gives stationarity of weak limit points for one-dimensional interacting particle systems under locality/rate hypotheses that BABP satisfies directly: updates are single-site, the site flip rate is uniformly bounded by `2 max(1,lambda)`, and influence is nearest-neighbour. Thus every subsequential limit of `Law_B(B_t)` is stationary.

For stationary-law classification we use Martinelli--Shapira--Toninelli (2025), Corollary 2.9. Their variables are complementary infection variables. Write their infection density as `q` and `p=1-q`. Their BABP update rates are proportional to their nearest-neighbour constraint, with infected-to-healthy rate `p` and healthy-to-infected rate `q`. The present convention is obtained by the constant rescaling

$$
\lambda=\frac qp,
\qquad
L_{\mathrm{project}}=p^{-1}L_{\mathrm{MST}}.
\tag{8.1}
$$

A positive constant time rescaling does not change stationary laws. Hence every stationary one-dimensional BABP law in the convention (1.2) is

$$
\nu=\alpha\delta_\varnothing+(1-\alpha)\pi_q,
\qquad \alpha\in[0,1].
\tag{8.2}
$$

Let `nu` be a subsequential limit. For each fixed `M`, emptiness of `[-M,M]` is a clopen cylinder, so (7.2) passes to the limit:

$$
\nu(B\cap[-M,M]=\varnothing)\le Ce^{-cM}.
$$

But (8.2) gives

$$
\nu(B\cap[-M,M]=\varnothing)
=
\alpha+(1-\alpha)(1-q)^{2M+1}
\ge\alpha.
$$

Sending `M` to infinity yields `alpha=0`. Every subsequential limit is `pi_q`, proving Theorem 1.1.

Neither the Mountford (1993) nor Ramírez--Varadhan (1996) stationary-limit theorem is needed as an unchecked input: Jahnel--Köppl provides the required current source. Their older papers remain relevant historical antecedents.

## 9. Relation to earlier BABP work

Neuhauser--Sudbury (1993) introduced and analyzed BABP, including its product equilibrium and stationary-law structure. Mountford (1993) gave a finite-particle stationary-limit/coupling argument and finite-seed convergence in the earlier `lambda>1/3` regime. Sudbury (1997) proved convergence for translation-invariant initial measures by relative entropy. Lloyd--Sudbury (1997) developed the quasi-duality/thinning machinery later reused in modern BABP--DFP arguments. Sudbury (1998) developed a computer-assisted finite-boundary method for sign-definite drift functions in non-attractive one-dimensional systems. Sudbury (1999) extended finite-seed BABP convergence to the `0.0347` range and obtained edge-speed bounds by submartingale methods.

Martinelli--Shapira--Toninelli (2025) prove new all-parameter results, including exponential ergodicity for the DFP and linear growth for BABP from finite seeds, but their Remark 5.4 still records finite-seed local convergence only above `0.0347`.

Our exact `k=1` and `k=8` calibrations show that the present edge-corrector LP is very likely close to Sudbury's historical submartingale calculation. The full Sudbury (1999) body was not available in the present literature audit, so we do not claim literal identity of the constructions or priority for the general corrector criterion.

The safe statement is the concrete mathematical one: the exact `k=10` certificate at `lambda=1/40`, together with Theorem 1.1, proves finite-seed local convergence at `0.025`, below the range recorded in the 2025 progress paper.

## 10. Open front problem

For fixed `lambda`, define the optimal `k`-window margin

$$
v_k(\lambda)
=
\sup_\phi\min_{u,z}D_{k,\lambda}(u,z;\phi).
$$

The project has proved window monotonicity

$$
v_{k+1}(\lambda)\ge v_k(\lambda).
$$

A current research reduction relates the infinite-window limit to invariant laws of the environment seen from the right edge and suggests a one-dimensional front-gap inequality as a route to `v_k(lambda)>0` for every `lambda>0`. That reduction is not part of the verified theorem in this note and should remain outside the main theorem until independently audited.

The present result therefore leaves open the all-parameter question:

> Does every `lambda>0` admit a finite-window statewise corrector with positive margin, or can finite-seed convergence for smaller parameters be proved by a different mechanism?

## References to check in final manuscript

- T. S. Mountford, *A coupling of finite particle systems*, Journal of Applied Probability 30 (1993), 258--262.
- C. Neuhauser and A. Sudbury, *The biased annihilating branching process*, Advances in Applied Probability 25 (1993), 24--38.
- A. Sudbury, *The convergence of the biased annihilating branching process and the double-flipping process in Z^d*, Stochastic Processes and their Applications 68 (1997), 255--264.
- A. Sudbury and P. Lloyd, *Quantum operators in classical probability theory IV: Quasi-duality and thinnings of interacting particle systems*, Annals of Probability 25 (1997), 96--114.
- A. Sudbury, *A method for finding bounds on critical values for non-attractive interacting particle systems*, Journal of Physics A 31 (1998), 8323--8331.
- A. Sudbury, *Hunting submartingales in the jumping voter model and the biased annihilating branching process*, Advances in Applied Probability 31 (1999), 839--854.
- F. Martinelli, A. Shapira and C. Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461 (2025).
- B. Jahnel and J. Köppl, *Restriction and mixing properties of interacting particle systems with unbounded range*, arXiv:2603.21817 (2026).

Before submission-level priority language, obtain and inspect the full Sudbury (1998, 1999) texts, especially the 1999 BABP convergence bridge.
