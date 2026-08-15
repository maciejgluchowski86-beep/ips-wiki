# Assignment 002: from the edge corrector to finite-seed convergence

## Conclusion

The theorem bridge can be closed from the **finite-window corrector itself**, without a second parameter-dependent estimate and without using the 2025 particle-number growth theorem.

There is an important distinction from the question as initially phrased. Bare statements

```text
liminf R_t/t > 0,     limsup L_t/t < 0
```

do not by themselves control evacuation of a fixed window. What closes the bridge is the stronger statewise input already furnished by the edge certificate:

```text
there are k, a bounded corrector phi, and v>0 such that
D_{k,lambda}(u,z;phi) >= v for every edge state (u,z).
```

The same corrector can be put on the two populations bordering any finite internal vacant gap. The corrected gap width then has uniformly negative drift. This gives exponential tails for both the lifetime and maximal width of every tagged gap. Since distinct positive gaps cannot merge in one-dimensional BABP, one can sum these estimates over all gap nucleations and obtain a uniform late-time exponential tail for the vacant interval containing the origin. Consequently the empty component of any invariant subsequential limit is zero.

Thus, subject only to the standard one-dimensional subsequential-limit invariance theorem of Mountford / Ramírez--Varadhan and the known stationary-law classification, a uniformly positive finite-window edge corrector implies finite-seed convergence to Bernoulli equilibrium.

In particular, once project claim `BABP-EDGE-001` is accepted at its present mathematical content, the exact `k=10`, `lambda=1/40` certificate yields finite-seed convergence at

```text
lambda = 1/40 = 0.025,
```

strictly below the previously published `0.0347` range.

I do not change the status of `BABP-EDGE-001` here; it remains `claimed` pending the already requested independent audit.

---

## 1. External bridge inputs and what still had to be proved

Write `pi_q` for Bernoulli product measure of particle density

```text
q = lambda/(1+lambda).
```

Two external facts are used.

### 1.1 Subsequential limits are invariant

Mountford, *A coupling of finite particle systems*, J. Appl. Probab. 30 (1993), 258--262, states that for a large class of one-dimensional interacting particle systems started from a finite configuration, every weak limit along times tending to infinity is invariant. The paper explicitly applies this result to one-dimensional BABP in the then-known `lambda>1/3` range.

Ramírez--Varadhan, *Relative entropy and mixing properties of interacting particle systems*, J. Math. Kyoto Univ. 36 (1996), 869--875, gives a shorter relative-entropy proof of the same general principle for finite-state particle systems; its abstract explicitly identifies Mountford's one-dimensional result as the predecessor.

I did not obtain the full Mountford or Ramírez--Varadhan text through the available publisher interfaces in this session, so I am not pretending to have rechecked every hypothesis line-by-line. The parameter dependence in the published BABP application is, however, separated from the generic invariance statement in the accessible records: the first is a theorem for a large class of one-dimensional systems, while `>1/3` occurs in the BABP convergence application. The current Professor should still verify the generic theorem hypotheses against BABP before stable promotion of the convergence corollary. No new small-parameter estimate enters this input.

### 1.2 Classification of stationary laws

For one-dimensional BABP, every stationary probability measure is a convex combination

```text
alpha delta_empty + (1-alpha) pi_q,       alpha in [0,1].
```

This is the classical Neuhauser--Sudbury stationary-law classification, and Martinelli--Shapira--Toninelli (2025), Corollary 2.9 and the discussion preceding it, records the same all-parameter classification.

Therefore, if `mu_t` denotes the law from a finite nonempty seed and `mu_{t_n} => nu`, the only remaining issue after invariance is to prove

```text
nu != alpha delta_empty + (1-alpha) pi_q with alpha>0.
```

The correct quantitative criterion is stronger than a fixed-window positive occupation probability.

For `Lambda_M=[-M,M]`,

```text
nu(B cap Lambda_M = empty)
 = alpha + (1-alpha)(1-q)^(2M+1).
```

Hence `alpha=0` follows from

```text
lim_{M->infinity} limsup_{t->infinity}
P_B(B_t cap [-M,M] = empty) = 0.                 (NS)
```

A lower bound in one fixed window would only imply `alpha<1`; it would not rule out a nontrivial empty component. This is the precise nonescape statement required by the invariant-mixture reduction.

---

## 2. Edge-corrector hypothesis

Assume the following statewise condition.

**(EC)** There are `k>=1`, a bounded function

```text
phi : {0,1}^k -> R,
```

and `v>0` such that for every `u in {0,1}^k` and `z in {0,1}`,

```text
D_{k,lambda}(u,z;phi) >= v.                       (2.1)
```

The drift `D` is the exact one from Assignment 001 / the Professor verification:

```text
D_{k,lambda}(u,z;phi)
 = lambda [1 + phi(T_+u)-phi(u)]
   + u_1[-1 + phi(T_-^z u)-phi(u)]
   + sum_{j=1}^k n_j^z(u)[lambda(1-u_j)+u_j]
       [phi(u^(j))-phi(u)].                         (2.2)
```

For a finite nonempty set `A`, let

```text
H_R(A) = R(A) + phi(U_R(A)),
```

where `U_R` is the right-edge word. Then

```text
L H_R(A) >= v.                                    (2.3)
```

By reflection define the left-edge word `U_L` and

```text
H_L(A) = L(A) - phi(U_L(A)).
```

Then

```text
L H_L(A) <= -v.                                   (2.4)
```

Add a constant to `phi` if convenient and fix

```text
K = ||phi||_infinity < infinity.
```

The Professor already checked that (EC) also gives outward linear speeds. We use substantially more of (EC) below than that asymptotic consequence.

---

## 3. Geometry and genealogy of internal gaps

An **internal gap** of a finite particle configuration is a maximal finite interval of vacant sites lying strictly between the leftmost and rightmost particles.

Three elementary one-dimensional facts are load-bearing.

### Lemma 3.1: gaps are born at length one

A new internal gap can only be created by death of a particle whose two neighbours are occupied. The newly created gap is the single vacant site where that particle died.

If a particle dies with exactly one occupied neighbour and one vacant neighbour, that death extends an already existing gap by one. A death at an outer edge changes the outer edge rather than nucleating an internal gap.

### Lemma 3.2: a positive gap changes only at its two boundaries

If a gap has length at least two, a birth into the gap can occur only at one of its two endpoint vacancies, so the gap shrinks by one. A boundary particle can die only if its neighbour on the particle side is occupied, in which case the gap extends by one.

If the gap has length one, a birth into its sole vacant site closes the gap. Its total rate is `2 lambda`, one `lambda` contribution from each bounding particle.

### Lemma 3.3: two positive gaps cannot merge

Suppose a particle lies between two positive gaps. Both of its nearest neighbours are vacant, so its death rate is zero. Hence that separating particle cannot disappear while both gaps are positive.

Consequently every internal gap has an unambiguous genealogy from its birth at length one until its closure at length zero. Gaps do not split or merge while alive.

This elementary fact is what makes it legitimate to sum later over gap births rather than over arbitrary empty intervals.

---

## 4. A tagged gap has a negative-drift corrected width

Fix one tagged internal gap while it is alive. Let

```text
A_t = particles on the left of the gap,
C_t = particles on the right of the gap.
```

Both are finite and nonempty throughout the gap lifetime. Let

```text
a_t = R(A_t),
b_t = L(C_t),
g_t = b_t-a_t-1 >= 1
```

be its physical width.

Up to the instant when the gap closes, the dynamics on `A_t` and `C_t` are exactly two standalone BABP dynamics as far as their own particles are concerned. For `g_t>=2` there is no update seeing particles from both sides. For `g_t=1`, the sole vacancy has two occupied neighbours; its birth rate `2 lambda` is the sum of the two standalone edge births, and either such birth is precisely the killing/closure event for the tagged gap.

Define

```text
Z_t = H_L(C_t) - H_R(A_t) - 1
    = g_t - phi(U_L(C_t)) - phi(U_R(A_t)).          (4.1)
```

While alive,

```text
g_t - 2K <= Z_t <= g_t + 2K.                       (4.2)
```

For the product dynamics of the two separated populations, (2.3)--(2.4) give

```text
L^x Z <= -2v.                                      (4.3)
```

At `g=1`, replace the two transitions that close the gap by killing. For any positive test function, replacing a transition value by zero can only decrease the killed generator. Thus inequalities obtained below for the product generator remain true for the killed tagged-gap process.

The jumps of `Z` are uniformly bounded. For example one may take

```text
J = 1 + 2K.                                        (4.4)
```

Only events in a fixed `k`-neighbourhood of the two inner edges can change `Z`. Their total rate is bounded uniformly over the global configuration; one convenient crude bound is

```text
rho = 2[lambda + 1 + 2k max(1,lambda)].            (4.5)
```

The exact value is immaterial.

### Lemma 4.1: exponential killed-generator inequality

There are constants `theta>0` and `gamma>0`, depending only on `(k,lambda,phi,v)`, such that for

```text
f = exp(theta Z)
```

on alive tagged-gap states,

```text
L^dagger f <= -gamma f,                            (4.6)
```

where `L^dagger` is the killed generator at gap closure.

**Proof.** For one jump `Delta Z`, `|Delta Z|<=J`, hence

```text
e^{theta Delta Z}-1
 <= theta Delta Z
    + (theta^2/2) e^{theta J} (Delta Z)^2.
```

Therefore, before killing,

```text
(L^x f)/f
 <= theta L^x Z
    + (theta^2/2)e^{theta J} rho J^2
 <= -2v theta
    + (theta^2/2)e^{theta J} rho J^2.
```

Choose `theta>0` small enough that

```text
(theta/2)e^{theta J} rho J^2 <= v.
```

Then the last display is at most `-v theta`. Put `gamma=v theta`. At a closure transition the killed generator uses terminal value zero, whereas the product generator would use the nonnegative value of `f` after the corresponding standalone birth. Thus killing only decreases the generator. This proves (4.6). `square`

### Corollary 4.2: lifetime tail

Let `tau` be the lifetime of a tagged gap. If it is born at length one, then uniformly over the surrounding configuration,

```text
P(tau > t) <= C_0 e^{-gamma t}.                    (4.7)
```

Indeed the killed semigroup estimate from (4.6) gives

```text
E[e^{theta Z_t}; tau>t]
 <= e^{-gamma t} e^{theta Z_0}.
```

On the alive event `Z_t >= 1-2K`, while at birth `Z_0<=1+2K`.

For a gap present initially with deterministic finite width `g_0`, the same estimate holds with a finite prefactor depending on `g_0`.

### Corollary 4.3: maximum-width tail

For a gap born at length one and

```text
sigma_m = inf{t<tau : g_t >= m},
```

there is `C_1<infinity` such that

```text
P(sigma_m < tau) <= C_1 e^{-theta m}.              (4.8)
```

Use the positive killed supermartingale `e^{theta Z}` stopped at `sigma_m wedge tau`. On `{sigma_m<tau}`, (4.2) gives `Z_{sigma_m}>=m-2K`; at birth `Z_0<=1+2K`.

The gap estimate is therefore not an asymptotic edge-speed statement. It is a uniform statewise contraction valid for every internal gap, including one embedded in an arbitrarily complicated finite cloud.

---

## 5. Spatial displacement of a tagged gap

To control a fixed observation window, lifetime and width are not enough: a gap born far away could travel to the origin. We therefore also bound the number of physical boundary shifts.

For a tagged gap let `N_t` count changes of either endpoint of its vacant interval before closure. Each side can:

- extend by one when its bounding particle dies, at rate at most `1`;
- shrink by one by a birth into the adjacent vacancy, at rate `lambda`.

At width one the closing birth has total rate `2 lambda`, exactly one `lambda` contribution from each side. Hence the predictable intensity of `N_t` is at most

```text
beta = 2(1+lambda).                                (5.1)
```

Thus `N_t` is stochastically dominated by a Poisson variable `P_t` of mean `beta t`.

Suppose a gap is born as the singleton vacancy `{x}`. If at age `t` its vacant interval contains the origin, then one of its endpoints has moved by at least `|x|`; consequently

```text
N_t >= |x|.                                        (5.2)
```

For a gap born at `x`, let `E_{m,t,x}` be the event that at age `t` it is alive, its width is at least `m`, and it contains the origin. Then

```text
E_{m,t,x}
 subset {sigma_m<tau} cap {tau>t} cap {N_t>=|x|}.
```

No independence is needed. Since the probability of an intersection is at most the geometric mean of any three upper bounds for its components, (4.7), (4.8), and (5.1)--(5.2) yield

```text
P(E_{m,t,x})
 <= C e^{-theta m/3} e^{-gamma t/3}
       P(Pois(beta t)>=|x|)^{1/3}.                  (5.3)
```

We need one elementary summability bound.

### Lemma 5.1: Poisson displacement summation

For `P_t ~ Pois(beta t)`,

```text
sum_{x in Z} P(P_t>=|x|)^{1/3} <= C_beta(1+t).      (5.4)
```

**Proof.** The terms with `|x|<=2e(beta t+1)` contribute `O(1+t)`. For larger `n=|x|`, the Chernoff bound

```text
P(P_t>=n) <= (e beta t/n)^n
```

is exponentially summable in `n` uniformly after this cutoff. Taking the one-third power changes only the exponential constant. `square`

---

## 6. Uniform exponential tail for large internal gaps at the origin

Let

```text
G_m(t) = {the origin lies in an internal gap of B_t of width >= m}.
```

We show

```text
limsup_{t->infinity} P_B(G_m(t)) <= C e^{-c m}.     (6.1)
```

The constants depend on the corrector data and `lambda`, but not on `m,t` or the birth location of the gap.

A new internal gap can be nucleated at site `x` only by death of the particle at `x` when both neighbours are occupied. The total death rate at a site is at most `2`, so the predictable nucleation intensity at each `x` is at most `2`.

Use the gap genealogy from Section 3. For gaps born after time zero, a union bound through the birth compensator and the uniform conditional estimate (5.3) gives

```text
P(some post-time-0 gap contributes to G_m(t))
 <= 2 sum_x integral_0^t
       C e^{-theta m/3} e^{-gamma(t-s)/3}
       P(Pois(beta(t-s))>=|x|)^{1/3} ds

 <= C' e^{-theta m/3}
       integral_0^infinity e^{-gamma r/3}(1+r) dr

 <= C'' e^{-c m}.                                  (6.2)
```

The second line uses Lemma 5.1.

There are only finitely many internal gaps at time zero because the initial seed is finite. By Corollary 4.2, the probability that any one of those initial gaps is still alive at time `t` tends to zero exponentially (with a prefactor depending on its initial width). Therefore its contribution vanishes in the `limsup_{t->infinity}`. This proves (6.1).

This is the missing local statement. It is substantially stronger than global cardinality growth.

---

## 7. Nonescape from the origin

The edge corrector gives, by the Professor's already checked martingale argument,

```text
liminf R_t/t >= v,
limsup L_t/t <= -v                                (7.1)
```

almost surely (after reflection for the left edge).

Fix `M`. Hence

```text
P(R_t <= M or L_t >= -M) -> 0.                    (7.2)
```

On the complementary event there are particles strictly to both sides of `[-M,M]`. If nevertheless

```text
B_t cap [-M,M] = empty,
```

then `[-M,M]` is contained in an internal gap of width at least `2M+1`. Thus

```text
P_B(B_t cap [-M,M]=empty)
 <= P(R_t<=M or L_t>=-M) + P(G_{2M+1}(t)).         (7.3)
```

Take `limsup_{t->infinity}` and use (6.1)--(7.2):

```text
limsup_{t->infinity}
P_B(B_t cap [-M,M]=empty)
 <= C e^{-c M}.                                    (7.4)
```

Therefore

```text
lim_{M->infinity} limsup_{t->infinity}
P_B(B_t cap [-M,M]=empty) = 0.                     (7.5)
```

This is exactly (NS).

---

## 8. Convergence theorem under the generic invariance input

### Theorem 8.1

Consider one-dimensional nearest-neighbour BABP at a fixed `lambda>0`, started from any finite nonempty deterministic particle set `B`. Assume:

1. every local weak subsequential limit of the law from a finite initial configuration is stationary (the Mountford / Ramírez--Varadhan generic input);
2. every stationary BABP law is `alpha delta_empty + (1-alpha)pi_q`;
3. the finite-window edge-corrector condition (EC) holds.

Then

```text
Law_B(B_t) => pi_q                 as t -> infinity.     (8.1)
```

**Proof.** The configuration space `{0,1}^Z` is compact, so any sequence `t_n->infinity` has a locally weakly convergent subsequence, say to `nu`. By (1), `nu` is stationary. By (2),

```text
nu = alpha delta_empty + (1-alpha) pi_q.
```

For each fixed `M`, the cylinder event of being empty on `[-M,M]` is clopen, hence

```text
nu(B cap [-M,M]=empty)
 = lim_n P_B(B_{t_n} cap [-M,M]=empty)
 <= C e^{-cM}
```

by (7.4). But the mixture formula gives

```text
nu(B cap [-M,M]=empty)
 = alpha + (1-alpha)(1-q)^(2M+1)
 >= alpha.
```

Let `M->infinity`. Then `alpha=0`, so `nu=pi_q`. Every subsequential limit is therefore `pi_q`, proving the full convergence. `square`

### Corollary 8.2: the `lambda=1/40` consequence

Project claim `BABP-EDGE-001` supplies (EC) at

```text
lambda = 1/40,
k = 10,
v = 1033/40000000 > 0.
```

Therefore Theorem 8.1 gives finite-seed convergence to Bernoulli equilibrium at `lambda=1/40`, conditional only on the claimed certificate retaining its present content after the independent audit and on the standard generic invariance theorem being verified to apply to BABP at this parameter.

There is **no second small-parameter inequality** in the new bridge.

The 2025 all-parameter linear growth of `|B_t|` is not used.

---

## 9. Historical dependency map

The full Sudbury (1999) proof was still not available through the publisher interface in this session, so the following separates source-supported facts from the new proof rather than inventing internal lemma numbers.

### Source-supported historical facts

- Neuhauser--Sudbury (1993) identify `pi_q` and the empty state as the only stationary distributions on `Z`, and prove the then-known finite-seed result in the `lambda>1/3` spreading range.
- Mountford (1993) proves a generic one-dimensional theorem that subsequential limits from finite configurations are invariant, and applies it to BABP for the then-known `lambda>1/3` range.
- Sudbury (1999) states that the finite-seed convergence range is extended to `0.0347` and that bounds on edge speed are obtained.
- Martinelli--Shapira--Toninelli (2025) still record finite-seed convergence only above the historical `0.0347` threshold while proving all-parameter DFP ergodicity and finite-seed cardinality growth.

### What the present argument shows about dependency

The convergence route can be decomposed as

```text
finite-window positive corrector
        |
        +--> outward edge speeds
        |
        +--> exponential tagged-gap lifetime/width tails
                 |
                 +--> local nonescape (NS)

subsequential-limit invariance + stationary-law classification + NS
        |
        +--> finite-seed convergence to pi_q.
```

Thus the corrector provides both the global spreading input and the local no-escape input needed to exclude the empty stationary component. One does not need to import a separate cardinality-growth theorem or a second parameter restriction.

I have not verified whether Sudbury's published proof organizes the local no-escape step by exactly this gap argument. That historical equivalence is not needed for the mathematical bridge proved here.

---

## 10. What changes in the proof spine

E4 should be replaced by the following statement.

```text
E4 (corrector to convergence): RESOLVED modulo verification of the standard
Mountford / Ramirez--Varadhan subsequential-invariance hypotheses for BABP.

A uniformly positive finite-window edge corrector gives more than outer edge
speed. Applied to the two populations bordering an internal gap, it yields a
negative-drift corrected gap width. This gives uniform exponential gap tails,
then

limsup_{t->infinity} P_B(B_t cap [-M,M]=empty) <= C exp(-cM).

Together with subsequential-limit invariance and the all-parameter stationary
classification, this forces every subsequential limit to equal pi_q.

Consequently BABP-EDGE-001, if it survives its pending independent audit,
implies finite-seed convergence at lambda=1/40.
```

E5 is now genuinely theorem-bearing rather than speculative: if one proves that for every `lambda>0` some finite-window corrector satisfies (EC), equivalently in the present optimization language `lambda_k -> 0` (subject to the precise monotonicity/threshold definitions already recorded), then the all-parameter finite-seed convergence theorem follows from Theorem 8.1.

---

## Handoff

```text
bridge proved at the corrector level; lambda=1/40 convergence follows
conditional on BABP-EDGE-001 retaining its claimed certificate after audit and
on the standard Mountford / Ramirez--Varadhan subsequential-limit invariance
theorem being checked against BABP's finite-range rates.

Decisive new mechanism:
internal gaps never merge. For a tagged gap, put the existing right-edge
corrector on its left population and the reflected corrector on its right
population. The corrected gap width has drift <= -2v. Exponential tilting gives
uniform exponential lifetime and maximum-width tails. A Poisson bound on gap
boundary displacement plus a compensator sum over gap births yields

limsup_{t->infinity} P(origin lies in an internal gap of width >=m)
    <= C exp(-c m).

Outward edge speeds then imply

limsup_{t->infinity} P_B(B_t cap [-M,M]=empty) <= C exp(-cM).

Every invariant subsequential limit is alpha delta_empty+(1-alpha)pi_q, so the
last estimate forces alpha=0.

No second lambda restriction appears. The 2025 cardinality-growth theorem is
not used.

Exact file:
research/active/babp-finite-seed/students/student-b/002-edge-speed-to-convergence.md

Suggested proof-spine change:
mark E4 resolved modulo the generic subsequential-invariance source check; make
E5 (lambda_k -> 0 / correctors for every lambda>0) the first mathematical
bottleneck.
```
