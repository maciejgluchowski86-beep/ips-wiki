# An exact finite-window certificate below Sudbury's BABP finite-seed range

Working research-note draft. Mathematical content is based on verified project claims `BABP-EDGE-001` and `BABP-CONV-001`. Historical attribution has been revised after full-text comparison with Sudbury (1999).

## Abstract

Consider the one-dimensional biased annihilating branching process (BABP) in particle variables, with a vacant site becoming occupied at rate `lambda` times the number of occupied nearest neighbours and an occupied site becoming vacant at rate equal to that number. Sudbury (1999) proved finite-seed convergence for `lambda>=0.0347` by a computer-assisted finite-window submartingale construction; his threshold is explicitly the value obtained from an eight-site window.

We extend the same finite-window mechanism to an exact rational ten-site certificate at

$$
\lambda=\frac1{40},
$$

with uniform statewise drift

$$
\frac{1033}{40000000}>0.
$$

Consequently BABP at `lambda=1/40`, started from every deterministic finite nonempty particle set, converges locally to Bernoulli equilibrium of density `1/41`.

For completeness we give a self-contained proof of the convergence implication under a strict statewise corrector hypothesis. The proof applies the same local corrector to the two particle populations bordering each internal vacant gap. The resulting corrected gap width has uniformly negative drift; localization of an exponential test gives uniform lifetime and maximum-width tails, and a spatially truncated compensator over gap nucleations yields a fixed-window nonescape estimate. Stationarity of subsequential limits and the one-dimensional classification of stationary BABP laws then identify the limit.

The finite-window method and its role as the threshold-dependent input for finite-seed convergence are classical; the new contribution here is the exact below-range certificate together with this self-contained modern proof.

## 1. Model, historical framework, and result

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

This is exactly Sudbury's 1999 normalization: his flip rate is

$$
c(x,\eta)
=
\bigl[\eta(x)+\lambda(1-\eta(x))\bigr]
\sum_{y\sim x}\eta(y).
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

### Theorem 1.1: self-contained strict-corrector convergence bridge

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

locally on `{0,1}^Z`.

Theorem 1.1 is a self-contained proof of a classical implication rather than a priority claim. Sudbury (1999), immediately before his Theorem 7, states that the Neuhauser--Sudbury (1993) finite-seed convergence argument relied on existence of a suitable finite-window submartingale and proceeds unchanged once that condition is extended to the `0.0347` range. Our hypothesis (1.5) is a strict statewise version of that classical submartingale condition.

### Corollary 1.2: exact ten-site certificate at `lambda=1/40`

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

for all `2^11=2048` edge states. Consequently

$$
\operatorname{Law}_B(B_t)\Longrightarrow\pi_{1/41}
\tag{1.9}
$$

for every deterministic finite nonempty initial set.

Sudbury's Theorem 7 gives finite-seed convergence for `lambda>=0.0347`; Martinelli--Shapira--Toninelli (2025), Remark 5.4, still records the historical `0.0347` range. Since `1/40=0.025`, (1.9) lies below that published range.

## 2. Exact finite-window edge generator

Put `u_0=1` and `u_{k+1}=z`. Define

$$
T_+u=(1,u_1,\ldots,u_{k-1}),
$$

$$
T_-^zu=(u_2,\ldots,u_k,z),
$$

and let `u^{(j)}` denote the word obtained by flipping `u_j`.

There are three classes of transitions that can change `H_R`.

A birth at `R+1` occurs at rate `lambda`, moves the edge one step right, and changes the word to `T_+u`. Its contribution is

$$
\lambda\bigl[1+\phi(T_+u)-\phi(u)\bigr].
$$

The rightmost particle can die only when `u_1=1`; then its death rate is one, the new edge is `R-1`, and the new word is `T_-^zu`. Its contribution is

$$
u_1\bigl[-1+\phi(T_-^zu)-\phi(u)\bigr].
$$

For `1<=j<=k`, the recorded site `R-j` has `u_{j-1}+u_{j+1}` occupied neighbours. Its flip rate is

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

Only one unrecorded bit is needed. A flip of the site carrying `z` may depend on the next site farther left, but that flip changes neither `R` nor the current word `u`, so it has zero instantaneous contribution to `L H_R`.

Since `phi` is bounded, `H_R` has uniformly bounded jumps and only a fixed number of local clocks can change it. After localization,

$$
M_t
=H_R(B_t)-H_R(B_0)-\int_0^t L H_R(B_s)\,ds
$$

is a martingale with predictable quadratic variation bounded by `Ct`. Hence `M_t/t -> 0` almost surely. Under (1.5),

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v
\qquad\text{a.s.},
\tag{2.2}
$$

and reflection gives

$$
\limsup_{t\to\infty}\frac{L(B_t)}t\le-v
\qquad\text{a.s.}
\tag{2.3}
$$

Existence of limiting edge speeds is not asserted.

## 3. Exact relation with Sudbury's finite-window construction

Sudbury fixes the leftmost particle and records the `m` sites immediately to its right. In a local picture

```text
... 0 1 x_1 ... x_m x_{m+1} ...
```

his binary `m`-block is `(x_1,...,x_m)`, while `x_{m+1}` is the unresolved end-value. Reflecting the configuration identifies

$$
m=k,
$$

his block state with `u`, and his end-value with `z`.

For a fixed assignment of end-values, Sudbury writes `Q` for the block generator and

$$
a=\lambda\mathbf 1-b
$$

for the bare edge-position drift. The corrected gain in state `i` is

$$
a_i+\sum_jq_{ij}(S_j-S_i).
\tag{3.1}
$$

Equation (3.1) is precisely (2.1) after reflection and the identification `S_i=phi(u)`.

The cancellative issue is that the worst exterior bit depends on the current block state. Sudbury describes this as a Maxwell's demon. His Lemma 5 constructs a single correction vector which makes the score a submartingale for **every possible assignment of end-values**. Because an end-value assignment can choose `0` or `1` independently for every block state, this is equivalent to imposing the statewise inequality for both exterior bits at every `u`.

Sudbury solves the robust finite-state problem by an iterative minimax algorithm. The project solves it directly as a linear programme maximizing a common lower margin. Sudbury's Section 4 makes the common-margin version explicit: for `U_0` he requires

$$
\sum_jq_{ij}(S_j-S_i)+a_i\ge U_0
\tag{3.2}
$$

for all possible end-value matrices. Equation (3.2) is the project condition `D>=v` with `U_0=v`.

### The historical `0.0347` value

Sudbury's Table 2 states:

```text
m    lambda_m
2    0.2653
3    0.1832
4    0.1154
5    0.0805
6    0.0589
7    0.0443
8    0.0347
```

He explicitly says these are values found by trial and error and that the listed decimal is not proved to be the true critical value. Thus the independently computed project crossing

$$
\lambda_8^*=0.0346195434755\ldots
\tag{3.3}
$$

is a refinement of the **same** eight-site feasibility boundary, not merely a coincidentally close calibration.

The historical provenance is therefore settled: the published `0.0347` comes literally from an eight-site finite-window submartingale in the same normalization.

## 4. The exact rational `k=10` certificate

For `k=10` and `lambda=1/40`, the corrector is stored in exact rational form in

`research/active/babp-finite-seed/students/student-b/edge-corrector-certificate.py`.

The certificate assigns one rational value to each of the `2^10=1024` words. Substitution into (2.1) gives 2048 exact rational inequalities, one for each pair `(u,z)`. The minimum is exactly

$$
v=\frac{1033}{40000000}.
\tag{4.1}
$$

The independent audit rederived (2.1), decoded the rational vector independently, and checked all 2048 inequalities.

Conceptually this certificate is an `m=10` witness in Sudbury's established finite-window framework. Sudbury's paper reports BABP threshold searches only through `m=8`; the construction itself is defined for arbitrary fixed `m`. The range extension at `1/40` is therefore computational/certificational rather than a new submartingale mechanism.

For a publication version, the rational vector and a minimal independent verifier should be supplementary material. The body needs (2.1), the certificate format, (4.1), and a reproducibility statement.

## 5. Internal vacant gaps

We now give a self-contained proof of Theorem 1.1 rather than importing the Neuhauser--Sudbury convergence argument used by Sudbury.

An **internal gap** is a maximal nonempty finite interval of vacant sites strictly between the leftmost and rightmost particles.

Three one-dimensional facts make internal gaps genealogically tractable.

**New gaps are born at width one.** A new internal vacant component is created only when a particle with both neighbours occupied dies. If exactly one neighbour is vacant, the death enlarges an existing gap.

**A positive gap cannot split.** A vacant site strictly inside a gap has two vacant neighbours and hence birth rate zero. Births occur only at endpoint vacancies and shrink the gap.

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
\tag{5.1}
$$

If `K=||phi||_infty`, then while the gap is alive,

$$
g-2K\le Z\le g+2K.
\tag{5.2}
$$

For `g>=2`, no nearest-neighbour transition sees particles on both sides of the gap, so the two side generators decouple and

$$
L^\times Z\le-2v.
\tag{5.3}
$$

At width one, the sole vacancy fills at total rate `2lambda`; either such birth closes the gap. Passing to the killed tagged-gap process only decreases the generator of a positive test function.

The statewise nature of (1.5) is essential here: `A_t` and `C_t` are random internal populations, not merely the two outer edges of the original cloud.

## 6. Localized exponential gap estimate

Only fixed neighbourhoods of the two inner particle edges can change `Z`. Consequently there are finite deterministic `J,rho`, depending only on `(k,lambda,phi)`, such that every non-killing jump satisfies

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

Choose `theta>0` so small that

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
\tag{6.1}
$$

The exponential is unbounded as the gap width grows, so (6.1) is used only after **localization**. Stop when the live gap width, or equivalently `Z` up to the bounded correction (5.2), reaches a finite level `n`; one may also stop after a finite number of jumps. Apply Dynkin's formula to the bounded stopped process. Remove the jump cutoff and send `n` to infinity using positivity and Fatou/monotone localization.

For a gap born at width one this gives uniform constants such that

$$
\mathbf P(\tau>t)
\le C_0e^{-\gamma t},
\tag{6.2}
$$

and

$$
\mathbf P\left(\sup_{s<\tau}g_s\ge m\right)
\le C_1e^{-\theta m}.
\tag{6.3}
$$

The constants are independent of the gap's birth location and surrounding finite configuration.

## 7. Spatial displacement and the nucleation compensator

Let `N_t` count shifts of either endpoint of a tagged gap before closure. At each boundary, extension occurs only when the bounding particle dies, at rate at most `1`, while shrinkage occurs by a birth into the adjacent vacancy at rate at most `lambda`. Hence

$$
N_t\preceq\operatorname{Pois}(\beta t),
\qquad
\beta=2(1+\lambda).
\tag{7.1}
$$

A gap born at `x` that contains the origin at age `r` must have accumulated at least `|x|` endpoint shifts. Combining (6.2), (6.3), and (7.1), without an independence assumption, gives

$$
\mathbf P(E_{m,r,x})
\le
C e^{-c_1m}e^{-c_2r}
\mathbf P\bigl(\operatorname{Pois}(\beta r)\ge|x|\bigr)^{1/3},
\tag{7.2}
$$

where `E_{m,r,x}` is the event that the descendant gap is alive at age `r`, contains zero, and has width at least `m`. Moreover,

$$
\sum_{x\in\mathbb Z}
\mathbf P\bigl(\operatorname{Pois}(\beta r)\ge|x|\bigr)^{1/3}
\le C_\beta(1+r).
\tag{7.3}
$$

A new gap can be nucleated at a fixed site at predictable rate at most `2`. The all-space compensator is justified in the following order.

First fix `N<infinity` and count only nucleations at sites `|x|<=N`. By the strong Markov property at each nucleation time and (7.2), the expected number of such genealogies producing a width-`m` gap containing zero at time `t` is at most

$$
2\sum_{|x|\le N}
\int_0^t
C e^{-c_1m}e^{-c_2(t-s)}
\mathbf P\bigl(\operatorname{Pois}(\beta(t-s))\ge|x|\bigr)^{1/3}
\,ds.
\tag{7.4}
$$

Only after obtaining this finite spatial sum do we send `N` to infinity. The counted events increase with `N`, so **monotone convergence** applies. Using (7.3) yields

$$
\limsup_{t\to\infty}
\mathbf P_B(G_m(t))
\le Ce^{-cm},
\tag{7.5}
$$

where `G_m(t)` is the event that zero lies in an internal gap of width at least `m`.

## 8. Nonescape and local convergence

Fix `M`. By (2.2)--(2.3),

$$
\mathbf P_B\bigl(R(B_t)\le M\text{ or }L(B_t)\ge-M\bigr)
\longrightarrow0.
\tag{8.1}
$$

On the complementary event there are particles on both sides of `[-M,M]`. If the entire window is empty, then it lies inside an internal gap of width at least `2M+1`. Therefore

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
\tag{8.2}
$$

In particular,

$$
\lim_{M\to\infty}
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)=0.
\tag{8.3}
$$

Jahnel--Köppl (2026), Theorem 2.5, gives stationarity of weak limit points for one-dimensional IPS under locality/rate hypotheses BABP satisfies directly.

For stationary-law classification use Martinelli--Shapira--Toninelli (2025), Corollary 2.9. Their variables are complementary infection variables. If their infection density is `q` and `p=1-q`, then

$$
\lambda=\frac qp,
\qquad
L_{\mathrm{project}}=p^{-1}L_{\mathrm{MST}}.
\tag{8.4}
$$

A positive constant time rescaling does not change stationary laws. Hence every stationary one-dimensional BABP law in the convention (1.2) is

$$
\nu=\alpha\delta_\varnothing+(1-\alpha)\pi_q.
\tag{8.5}
$$

Let `nu` be a subsequential limit. For each fixed `M`, emptiness of `[-M,M]` is a clopen cylinder, so (8.2) passes to the limit. But (8.5) gives

$$
\nu(B\cap[-M,M]=\varnothing)
=
\alpha+(1-\alpha)(1-q)^{2M+1}
\ge\alpha.
$$

Sending `M` to infinity yields `alpha=0`. Every subsequential limit is `pi_q`, proving Theorem 1.1.

Neither Mountford (1993) nor Ramírez--Varadhan (1996) is needed as an unchecked theorem input; Jahnel--Köppl provides the stationary-limit interface used here.

## 9. Relation to Sudbury's convergence theorem

The closest prior result is now source-checked in full.

Sudbury's Section 3 defines, for a finite particle cloud with right and left edges `Ri,Le`, the global corrected span

$$
L
=
Ri-Le+S_{i(Ri)}+S_{i(Le)}-(2m+2)
$$

when `Ri-Le>=2m+1`, and `L=0` otherwise. Lemmas 5--9 construct a robust finite-window submartingale. Table 2 gives `m=8`, `lambda_8=0.0347`.

Immediately before Theorem 7, Sudbury explains that Neuhauser--Sudbury (1993), Section 5 had used existence of a suitable submartingale as the threshold-dependent input to exclude the null limiting measure. Since his Section 3 extends this condition to `lambda>=0.0347`, that earlier argument proceeds unchanged. Thus the **logical corrector-to-convergence principle is prior work**.

The proof given in Sections 5--8 above is nevertheless not the argument written in Sudbury 1999. Sudbury does not analyze internal-gap genealogies or prove the exponential gap and spatial-compensator estimates used here; he delegates the convergence bridge to Neuhauser--Sudbury Section 5. Until that older section is inspected, no priority claim should be made for the specific internal-gap proof architecture.

The project contribution should therefore be described as an exact range extension within the classical finite-window framework, plus a self-contained modern convergence proof.

## 10. Novelty and scope

The literature audit through 2026-08-15 found no later same-model finite-seed theorem below the `0.0347` range. With Sudbury's full text now checked, the source-level picture is:

- **finite-window submartingale method:** classical;
- **literal eight-site origin of `0.0347`:** verified;
- **finite-window submartingale as sufficient threshold-dependent input for finite-seed convergence:** classical;
- **exact rational `k=10`, `lambda=1/40` certificate:** project contribution;
- **finite-seed convergence at `lambda=1/40`:** range extension beyond Sudbury's published theorem;
- **tagged-gap/nonescape proof:** project self-contained proof; historical proof-method priority still unverified against Neuhauser--Sudbury (1993), Section 5;
- **all-parameter statement:** open.

A safe introduction sentence is:

> Sudbury proved finite-seed convergence for one-dimensional BABP for `lambda>=0.0347` using an eight-site finite-window submartingale. We extend the same finite-window mechanism to an exact rational ten-site certificate at `lambda=1/40`, yielding finite-seed convergence at `0.025`. We also give a self-contained proof of the convergence implication from a strict statewise corrector by controlling internal vacant gaps.

Do not claim that the finite-window method or the abstract corrector-to-convergence implication is new.

## 11. Open front problem

For fixed `lambda`, define

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

The present result leaves open:

> Does every `lambda>0` admit a finite-window statewise corrector with positive margin, or must smaller parameters be handled by a different mechanism?

## References for the focused note

- T. S. Mountford, *A coupling of finite particle systems*, Journal of Applied Probability 30 (1993), 258--262.
- C. Neuhauser and A. Sudbury, *The biased annihilating branching process*, Advances in Applied Probability 25 (1993), 24--38.
- A. Sudbury, *The convergence of the biased annihilating branching process and the double-flipping process in Z^d*, Stochastic Processes and their Applications 68 (1997), 255--264.
- A. Sudbury and P. Lloyd, *Quantum operators in classical probability theory IV: Quasi-duality and thinnings of interacting particle systems*, Annals of Probability 25 (1997), 96--114.
- A. Sudbury, *A method for finding bounds on critical values for non-attractive interacting particle systems*, Journal of Physics A 31 (1998), 8323--8331.
- A. Sudbury, *Hunting submartingales in the jumping voter model and the biased annihilating branching process*, Advances in Applied Probability 31 (1999), 839--854; especially Section 3, Table 2, Lemmas 5--9 and Theorem 7.
- F. Martinelli, A. Shapira and C. Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461 (2025).
- B. Jahnel and J. Köppl, *Restriction and mixing properties of interacting particle systems with unbounded range*, arXiv:2603.21817 (2026).

For any eventual claim that the **specific internal-gap proof mechanism** is new, inspect Neuhauser--Sudbury (1993), Section 5 in full. This is no longer needed for the range-extension or finite-window provenance claims.