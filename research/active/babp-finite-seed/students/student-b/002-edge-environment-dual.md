# E5 reduction: LP duality and the infinite edge environment

This note begins the second strand of Assignment 002 after the corrector-to-convergence bridge was closed in `002-edge-speed-to-convergence.md`.

The finite-window optimization has an exact infinite-volume interpretation. It turns the question

```text
lambda_k -> 0 ?
```

into a stationary estimate for the one-sided environment seen from the rightmost particle.

## 1. Finite-window generator and LP dual

Fix `lambda>0` and `k>=1`. Let

```text
E_k = {0,1}^k.
```

For `u in E_k` and `z in {0,1}`, let `Q_k^z` be the generator on functions `phi:E_k->R` obtained from the edge-word transitions in the exact drift formula, so that

```text
D_{k,lambda}(u,z;phi)
 = b(u) + Q_k^z phi(u),

b(u) = lambda-u_1.                                  (1.1)
```

Thus

```text
v_k(lambda)
 = sup_phi min_{u,z} [b(u)+Q_k^z phi(u)].            (1.2)
```

Adding a constant to `phi` changes nothing.

Define `M_k` to be the set of nonnegative arrays `m(u,z)` satisfying

```text
sum_{u,z} m(u,z) = 1,                               (1.3)

sum_{u,z} m(u,z) Q_k^z f(u) = 0
for every f:E_k->R.                                 (1.4)
```

These are exactly stationary occupation measures for the continuous-time Markov decision problem in which the left exterior bit `z` may be chosen, possibly randomly and state-dependently, as a control.

### Proposition 1.1: exact dual formula

```text
v_k(lambda)
 = min_{m in M_k} sum_{u,z}m(u,z)(lambda-u_1)
 = lambda - max_{m in M_k} sum_{u,z}m(u,z)u_1.       (1.5)
```

**Proof.** Write the primal inequalities as

```text
-Q_k^z phi(u) + v <= b(u),       (u,z) in E_k x {0,1}.
```

Finite-dimensional linear-programming duality assigns a nonnegative multiplier `m(u,z)` to every inequality. The coefficient of `v` gives (1.3); the coefficients of `phi` give (1.4), with the single redundant balance equation supplied by the row-sum-zero property of every `Q_k^z`. The dual objective is the first expression in (1.5). `square`

This formula is useful conceptually: the adversarial bit in the primal is not merely a proof nuisance. The dual asks for the worst stationary way of feeding the unresolved left boundary into the finite edge window.

## 2. Infinite environment seen from the edge

Let

```text
E_infinity = {0,1}^N,

u=(u_1,u_2,...).
```

The implicit particle at the right edge is `u_0=1`. Define the infinite edge-environment generator `Q_infinity` on cylinder functions as follows.

1. A birth at the site to the right of the edge, at rate `lambda`, shifts the frame right:

```text
S_+ u = (1,u_1,u_2,...).
```

2. If `u_1=1`, death of the rightmost particle occurs at rate one and shifts the frame left:

```text
S_- u = (u_2,u_3,...).
```

3. For each `j>=1`, flip `u_j` at rate

```text
(u_{j-1}+u_{j+1})[lambda(1-u_j)+u_j].               (2.1)
```

Hence for a cylinder function `f`,

```text
Q_infinity f(u)
 = lambda[f(S_+u)-f(u)]
   + u_1[f(S_-u)-f(u)]
   + sum_{j>=1}(u_{j-1}+u_{j+1})
       [lambda(1-u_j)+u_j][f(u^j)-f(u)],             (2.2)
```

where only finitely many terms in the last sum can change `f`.

This is the natural environment seen from the rightmost particle. It is a standard bounded finite-range spin dynamics on the half-line supplemented by two continuous shift maps of bounded total rate, so it defines a Feller process on the compact product space `E_infinity`.

Let `I_lambda` denote its set of invariant probability measures; it is nonempty by compactness and Krylov--Bogoliubov.

Define the minimum stationary edge drift

```text
s_*(lambda)
 = inf_{mu in I_lambda} int (lambda-u_1) dmu.        (2.3)
```

### Theorem 2.1: finite windows converge exactly to the worst invariant front drift

```text
lim_{k->infinity} v_k(lambda) = s_*(lambda).         (2.4)
```

**Proof.** The sequence `v_k` is already known to be nondecreasing by the exact extension argument in `001-edge-corrector-monotonicity.md`, so its limit exists.

**Upper bound.** Fix `mu in I_lambda`. Define

```text
m_k(u,z)
 = mu(U_1,...,U_k=u, U_{k+1}=z).                    (2.5)
```

For every `f:E_k->R`, viewed as a cylinder function on `E_infinity`, the pointwise identity

```text
Q_infinity f = Q_k^{U_{k+1}} f                     (2.6)
```

holds. Invariance of `mu` therefore makes `m_k` satisfy (1.3)--(1.4). Proposition 1.1 gives

```text
v_k(lambda) <= int(lambda-u_1)dmu.
```

Take the infimum over `mu` and then `k->infinity`:

```text
lim_k v_k(lambda) <= s_*(lambda).                   (2.7)
```

**Lower bound.** For each `k` choose a dual minimizer `m_k in M_k` and let `mu_k` be its marginal on `E_k`. Extend `mu_k` arbitrarily to a probability measure on `E_infinity` (for example, append zero coordinates). By compactness take a weakly convergent subsequence

```text
mu_{k_n} => mu.
```

Fix a cylinder function `f` depending on the first `ell` coordinates. If `k_n>=ell+1`, then `Q_k^z f` is independent of the adversarial bit `z`: the right shift uses only the first `ell-1` old bits, the left shift uses through `u_{ell+1}`, and every local flip affecting `f` uses at most `u_{ell+1}`. Consequently

```text
int Q_infinity f dmu_{k_n}
 = sum_{u,z}m_{k_n}(u,z)Q_{k_n}^z f(u)
 = 0.                                               (2.8)
```

Pass to the weak limit. Since `Q_infinity f` is again a cylinder function,

```text
int Q_infinity f dmu = 0
```

for every cylinder `f`, so `mu in I_lambda`. The objective depends only on the first coordinate, hence

```text
lim_n v_{k_n}(lambda)
 = int(lambda-u_1)dmu
 >= s_*(lambda).                                    (2.9)
```

Because the full sequence `v_k` has a limit, (2.9) gives the reverse inequality to (2.7). `square`

### Corollary 2.2: exact E5 criterion

For a fixed `lambda>0`, the following are equivalent:

```text
(i)  v_k(lambda)>0 for some finite k;
(ii) s_*(lambda)>0;
(iii) every invariant law of the infinite edge environment has mean edge drift
      bounded below by one common strictly positive number.
```

Thus the all-parameter finite-window programme is exactly an invariant-front problem, not merely an asymptotic numerical observation.

In particular,

```text
lambda_k -> 0
```

would follow once `s_*(lambda)>0` is proved for every `lambda>0`.

## 3. A one-gap stationary identity

There is a useful exact reduction of `s_*` to one local pattern.

Fix `mu in I_lambda` and put

```text
r = mu(u_1=1),

a = mu(u_1=0,u_2=1),

q = lambda/(1+lambda).                              (3.1)
```

Consider the first bit `u_1`.

When `u_1=0`, it changes to one by either:

- the right-edge birth/shift, rate `lambda`;
- a local birth at site 1, rate `lambda(1+u_2)`.

Therefore its total `0 -> 1` rate is

```text
lambda(2+u_2).                                      (3.2)
```

When `u_1=1`, it changes to zero by either:

- local death at site 1, rate `1+u_2`;
- death of the rightmost particle followed by the left shift, which changes the new first bit to zero exactly when `u_2=0`, rate `1-u_2`.

The total `1 -> 0` rate is therefore identically

```text
2.                                                    (3.3)
```

Stationarity of `u_1` gives the exact flow balance

```text
lambda E[(1-u_1)(2+u_2)] = 2E[u_1],                 (3.4)
```

or

```text
lambda[2(1-r)+a] = 2r.                              (3.5)
```

Solving,

```text
r = q(1+a/2).                                       (3.6)
```

Consequently the mean edge drift under `mu` is

```text
lambda-r
 = q(lambda-a/2).                                  (3.7)
```

### Corollary 3.1: E5 is a strict one-vacancy-gap estimate

Combining Theorem 2.1 and (3.7),

```text
lim_{k->infinity}v_k(lambda)
 = q [lambda - (1/2) sup_{mu in I_lambda}mu(01)].   (3.8)
```

Therefore the finite-window thresholds tend to zero if and only if for every fixed `lambda>0`,

```text
sup_{mu in I_lambda} mu(u_1=0,u_2=1) < 2lambda.     (3.9)
```

The pattern `01` has a direct physical interpretation: the rightmost particle is separated from the next particle by exactly one vacant site. Thus the remaining all-parameter problem has been reduced to a uniform stationary estimate on a single one-vacancy gap in the front process.

This identity also explains why a corrector depending only linearly on the occupation bits is too weak: the obstruction sits at the first nontrivial spatial correlation, not at the one-site density alone.

## 4. Numerical asymptotic clue, not a claim

The already computed optimal thresholds are

```text
k=1:  0.3333333333...
k=2:  0.2652391706...
k=3:  0.1831057937...
k=4:  0.1153336497...
k=5:  0.0804020712...
k=6:  0.0588301835...
k=7:  0.0442801224...
k=8:  0.0346195435...
k=9:  0.0278105...
k=10: approximately 0.02273 from exploratory floating-point LP.
```

The products `k^2 lambda_k` over the last few accessible values are around `2.2--2.3`. This suggests a diffusive boundary-penetration scale `k ~ lambda^{-1/2}` and possibly `lambda_k=Theta(k^{-2})`, but there is presently no proof and this observation should not be promoted.

A useful interpretation is that an adversarial occupied bit inserted at distance `k` can influence the front only through the dynamics of sparse particles/gaps, whose transport is plausibly diffusive at small `lambda`.

## 5. Next mathematical lemma

The next E5 target can now be stated without reference to the finite LP.

```text
FRONT-GAP LEMMA.
For every lambda>0 there is epsilon(lambda)>0 such that every invariant
probability measure mu of the infinite right-edge environment Q_infinity
satisfies

    mu(u_1=0,u_2=1) <= 2lambda-epsilon(lambda).
```

By (3.8), this lemma is equivalent to

```text
lim_k v_k(lambda) >= q epsilon(lambda)/2 > 0,
```

and hence gives a finite positive-drift corrector for that `lambda`. Combined with `002-edge-speed-to-convergence.md`, proving the FRONT-GAP LEMMA for every `lambda>0` would complete the all-parameter finite-seed convergence theorem.

A second possible route is uniqueness plus positive speed for the infinite front process: if `Q_infinity` has a unique invariant law `mu_lambda` and its mean drift is positive, then (2.4) immediately supplies a finite corrector. The dual formula shows precisely why proving positive speed only for one accessible front law would not be enough without uniqueness: the finite LP sees the worst invariant front law.

## Handoff for E5

```text
The finite-window problem has an exact infinite-volume dual:

    lim_k v_k(lambda)
      = inf_{mu invariant for the infinite edge environment}
          [lambda-mu(u_1=1)].

For every invariant front law,

    mu(u_1=1)
      = q [1 + (1/2)mu(u_1=0,u_2=1)],

so

    lim_k v_k(lambda)
      = q [lambda - (1/2)sup_mu mu(01)].

Thus E5 should be replaced analytically by the FRONT-GAP LEMMA

    sup_mu mu(01) < 2lambda

for every lambda>0, or by uniqueness + positive mean speed for the infinite
front process.

Exact file:
research/active/babp-finite-seed/students/student-b/002-edge-environment-dual.md
```
