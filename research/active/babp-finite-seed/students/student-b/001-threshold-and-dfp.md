# Assignment 001: BABP threshold obstruction and DFP diagnostic

## Executive conclusion

The historical `0.0347` cutoff is not caused by self-duality or by a particle-number-growth estimate. It is a finite-state **right-edge submartingale** condition. One can formulate it as a linear program for a bounded corrector depending on the first `k` sites behind the rightmost particle.

This reconstruction passes two strong checks:

1. for `k=1`, the condition is feasible with strictly positive drift iff `lambda>1/3`, reproducing the Neuhauser--Sudbury/Mountford cutoff exactly;
2. for `k=8`, the zero-drift LP threshold is numerically

   ```text
   0.03461954...
   ```

   which is the `0.0347` quoted in Sudbury's 1999 theorem.

The full Sudbury paper was not accessible through the available publisher interface, so I am not asserting a line-by-line identification with his internal notation. But the title/abstract explicitly says he hunts submartingales and obtains edge-speed bounds, and the independent finite-window calculation reproduces both historical numerical cutoffs. This identifies the load-bearing mechanism with very high confidence.

There is also a genuine new mathematical datum. A `k=10` rational corrector at

```text
lambda = 1/40 = 0.025
```

has exact minimum generator drift

```text
1033/40000000 = 0.000025825 > 0.
```

The exact certificate is committed in

`students/student-b/edge-corrector-certificate.py`.

Thus the old *edge-speed* cutoff itself is not intrinsic: a larger finite window already pushes it below `0.0347`. I do **not** yet claim finite-seed convergence at `lambda=1/40`, because the final step from the edge-speed estimate to Sudbury's convergence theorem must still be reconstructed from the full paper (or reproved directly).

The strongest next route is therefore not DFP algebra. It is to prove that the optimal finite-window edge threshold `lambda_k` tends to zero as `k -> infinity`, and in parallel verify/reprove the exact edge-speed-to-local-convergence implication.

## 1. Conventions

Use the particle variables of Neuhauser--Sudbury/Sudbury. For a finite nonempty set `B subset Z`, each particle creates a particle at a vacant nearest neighbour at rate `lambda`, and an occupied site is annihilated by each occupied nearest neighbour at rate `1`.

The nontrivial equilibrium is Bernoulli product measure of particle density

```text
q = lambda/(1+lambda),
p = 1/(1+lambda).
```

Let

```text
R(B) = max B,
L(B) = min B.
```

## 2. E0: the finite-test self-duality criterion

For a finite test set `T`, put

```text
r = -1/lambda,
F_T(C) = r^{|C cap T|}.
```

BABP self-duality gives

```text
E_B F_T(B(t)) = E_T r^{|T(t) cap B|}.
```

The implication to local convergence is elementary. On one site,

```text
r^{xi_x} = 1 + (r-1) xi_x,
```

and `r != 1`, so for a finite set `S` the tensor products

```text
{F_T : T subset S}
```

form a basis of all functions of `xi|_S`.

For equilibrium particle density `q=lambda/(1+lambda)`,

```text
E_pi r^{xi_x}
 = (1-q) + q(-1/lambda)
 = 1/(1+lambda) - 1/(1+lambda)
 = 0.
```

Hence

```text
pi(F_T)=0
```

for every nonempty `T`. Therefore, if

```text
E_B F_T(B(t)) -> 0
```

for every finite nonempty `T`, then every finite-dimensional distribution of `B(t)` converges to the Bernoulli product equilibrium `pi`. This is the content used in Martinelli--Shapira--Toninelli, Remark 5.3.

The difficulty for small `lambda` is genuinely local: `|r|>1`, so the finite-test observable cannot be bounded using global cardinality growth by taking absolute values.

## 3. Exact finite-window edge-corrector criterion

Fix `k>=1`. For a finite nonempty configuration `B`, write `R=R(B)` and encode the first `k` sites behind the right edge by

```text
u_j = 1_{R-j in B},      j=1,...,k,
z   = 1_{R-k-1 in B}.
```

Thus `u=(u_1,...,u_k) in {0,1}^k`; `z` is the single unresolved exterior bit needed to compute the rates at the left boundary of this window.

Let

```text
phi : {0,1}^k -> R
```

be a bounded corrector, and define

```text
H(B)=R(B)+phi(u(B)).
```

For `u in {0,1}^k`, define

```text
T_+ u = (1,u_1,...,u_{k-1}),
```

because a birth from `R` to `R+1` makes the old edge the first occupied site behind the new edge. If `u_1=1`, annihilation of the rightmost particle makes `R-1` the new edge, so

```text
T_-^z u = (u_2,...,u_k,z).
```

Let `u^(j)` denote `u` with bit `j` flipped. Put `u_0=1` and `u_{k+1}=z`. The number of occupied neighbours of the target `R-j` is

```text
n_j^z(u)=u_{j-1}+u_{j+1}.
```

A vacant target flips to occupied at rate `lambda n_j^z(u)` and an occupied target flips to vacant at rate `n_j^z(u)`.

Therefore the exact generator drift of `H` at a configuration with boundary data `(u,z)` is

```text
D_{k,lambda}(u,z;phi)
 = lambda [1 + phi(T_+u)-phi(u)]
 + u_1[-1 + phi(T_-^z u)-phi(u)]
 + sum_{j=1}^k n_j^z(u)[lambda(1-u_j)+u_j]
       [phi(u^(j))-phi(u)].
```

No event farther than `R-k-1` changes `H`, so this is the whole generator.

### Edge-submartingale lemma

If there are `v>0` and `phi` such that

```text
D_{k,lambda}(u,z;phi) >= v
```

for every `u in {0,1}^k` and `z in {0,1}`, then

```text
H(B(t)) - vt
```

is a submartingale. Since `phi` is bounded, the standard martingale decomposition and the strong law for its bounded-jump martingale part give

```text
liminf_{t->infinity} R(B(t))/t >= v
```

almost surely. By reflection,

```text
limsup_{t->infinity} L(B(t))/t <= -v.
```

For fixed `k,lambda`, maximizing `v` over `phi` is a finite linear program with `2^k` corrector variables and `2^{k+1}` drift inequalities. Fixing `phi(0,...,0)=0` removes the additive gauge.

This is the precise load-bearing inequality that the numerical cutoff measures.

## 4. The old `1/3` cutoff appears already at `k=1`

Write

```text
phi(0)=0,
phi(1)=a.
```

The four boundary drifts reduce to three distinct expressions:

```text
D(0,0) = lambda(1+2a),
D(0,1) = lambda(1+3a),
D(1,0) = D(1,1) = lambda-1-2a.
```

For a feasible positive drift, the relevant inequalities require

```text
a > -1/3,
a < -(1-lambda)/2.
```

Such an `a` exists iff

```text
lambda > 1/3.
```

Thus the classical threshold is exactly the one-site edge-corrector condition.

## 5. Reconstructing `0.0347`

Solving the finite LP numerically gives the following zero-speed thresholds `lambda_k`:

```text
k     lambda_k
1     0.3333333333
2     0.2652391706
3     0.1831057937
4     0.1153336497
5     0.0804020712
6     0.0588301835
7     0.0442801224
8     0.0346195435
9     0.0278105113
10    0.0227326209
```

The `k=8` value rounds upward at four significant decimal places to the historical `0.0347` cutoff. This, together with Sudbury's explicit statement that his theorem comes from hunted submartingales and edge-speed bounds, isolates the historical obstruction: **the proof had only constructed a positive-drift finite-window edge corrector down to this parameter**.

This also shows that `0.0347` is a proof artifact rather than a visible dynamical transition: the same construction with a larger window continues below it.

The numerical sequence strongly suggests

```text
lambda_k -> 0.
```

The data are compatible with a roughly polynomial decay (approximately order `k^{-2}` over this short range), but I do not regard that asymptotic as established.

## 6. Exact certificate below the classical cutoff

A floating LP search at

```text
k=10,
lambda=1/40
```

produced a corrector which was rounded coordinatewise to denominator `10^6`. I then evaluated all `2^11=2048` drift inequalities using exact rational arithmetic.

The exact minimum is

```text
min_{u,z} D_{10,1/40}(u,z;phi)
 = 1033/40000000
 = 0.000025825 > 0.
```

It is attained at

```text
u=(0,1,1,1,1,1,0,0,1,1),
z=1.
```

The complete rational corrector is embedded compactly in

`edge-corrector-certificate.py`.

Running that file requires only the Python standard library. It decompresses the 1024 integer numerators, evaluates every inequality with `fractions.Fraction`, and asserts the exact minimum above. Thus the positivity certificate does not rely on floating-point LP output.

**Established project claim:** BABP at `lambda=1/40` admits a bounded 10-site right-edge corrector with uniform strictly positive generator drift. Consequently its right and left edges have strictly positive outward asymptotic speed in the sense of the edge-submartingale lemma above.

**Not yet established:** that this alone upgrades the complete finite-seed convergence theorem from `lambda>0.0347` to include `lambda=1/40`. The remaining literature dependency must be checked/reproved.

## 7. What the 2025 all-parameter growth theorem does and does not replace

Martinelli--Shapira--Toninelli, Application 1, proves for every `lambda>0` that a BABP started from a finite nonempty seed has cardinality growing linearly in `t` (with an exponential lower-tail estimate). Immediately after this, Remark 5.4 still records finite-seed convergence only above the Sudbury threshold.

This is consistent with the edge audit. Cardinality growth implies only

```text
R(t)-L(t)+1 >= |B(t)|,
```

so it gives linear growth of the span. It does not give separate outward speeds for the two edges, nor does it by itself control how the growing cloud intersects a fixed local test set. The old threshold mechanism is precisely an **edge drift** estimate, and the 2025 cardinality theorem does not supply that estimate.

Hence the new 2025 growth theorem does not remove the load-bearing `0.0347` ingredient. It supplies a strong global fact that may simplify later recurrence/local-density steps, but it is not a substitute for the finite-window edge submartingale.

## 8. DFP diagnostic on the actual finite-test observable

Let

```text
y=sqrt(1+lambda),
a=1/(y+1),
b=-1/(y-1),
r=-1/lambda.
```

For a DFP initial set `D`, the BABP--DFP quasi-duality kernel evaluated at a finite particle configuration `C` is

```text
K_D(C)=a^{|C cap D|} b^{|C cap D^c|}.
```

We want the finite-test self-duality cylinder

```text
F_S(C)=r^{|C cap S|},
```

which has one-site factor `r` on `S` and neutral factor `1` outside `S`.

### No representation by a random DFP initial set

Suppose `D` is random. For a singleton `C={x}`, only the marginal

```text
beta_x=P(x in D)
```

matters, and exact representation requires

```text
beta_x a + (1-beta_x)b
 = r,   x in S,
 = 1,   x notin S.
```

Since

```text
a-b = 2y/lambda,
```

the unique solutions are

```text
beta_x = 1/2,       x in S,
beta_x = (y+1)/2,   x notin S.
```

But `y>1`, so `(y+1)/2>1`. Therefore **no probability law on D, correlated or independent, can represent `F_S` exactly**. The obstruction already appears for `S={0}` and hence also for `S={0,1}`.

### Exact signed representations have exponentially growing coefficient norm

On a finite window `V superset S`, the one-site two-kernel transform is invertible. Therefore the signed measure on `D cap V` representing `F_S` is unique. It is the tensor product of the one-site signed weights

```text
x in S:
    (D absent, D present) = (1/2,1/2),

x in V\S:
    (D absent, D present) = ((1-y)/2,(1+y)/2).
```

The one-site total variation norm is `1` on `S` and `y` outside `S`, hence the exact coefficient norm on `V` is

```text
y^{|V\S|}.
```

Thus there is no bounded-total-variation infinite-volume signed representation: the norm diverges as `V` grows. With a finite-propagation window of linear size in time, the exact signed expansion carries an exponential coefficient cost.

This does not prove that DFP can never help. It proves that Theorem 5.2 is not a black-box solution of the deterministic finite-test observable: one would need a quantitative DFP mixing rate strong enough to dominate this coefficient growth after truncation, or a nontrivial cancellation avoiding the unique raw signed expansion. The 2025 paper supplies neither such comparison nor a finite-seed conclusion.

Accordingly E3 should be downgraded from a likely main route to a secondary quantitative possibility.

## 9. Revised dependency map

The best current map is:

1. **Finite-test criterion:** self-duality decay for every finite test set implies local convergence. Established.
2. **Invariant-law endpoint:** the only one-dimensional stationary laws are the empty law and the Bernoulli equilibrium mixtures. Established in the literature/current survey.
3. **Finite-seed global growth:** `|B(t)|` grows linearly for every `lambda>0`. Established by Martinelli--Shapira--Toninelli.
4. **Historical threshold ingredient:** a bounded local corrector giving strictly positive outward edge drift. Reconstructed here; the classical `1/3` and `0.0347` numbers are finite-window feasibility thresholds.
5. **New project progress:** the same edge criterion is feasible with an exact rational certificate at `lambda=1/40`, so the historical numerical barrier is already penetrated.
6. **Remaining load-bearing literature step:** verify exactly how Sudbury/Mountford turn the edge-speed bound into convergence to the nontrivial invariant law, and identify whether any additional inequality besides positive edge speed is threshold-dependent.
7. **Main new analytic lemma if step 6 has no second threshold:** prove `lambda_k -> 0` for the finite-window edge LP, or construct an explicit family `phi_k` with positive drift for every prescribed `lambda>0` once `k` is large enough.

This is a materially sharper E4 than “control the signed finite-test observable.”

## 10. Suggested next mathematical tasks

### Priority A: close the historical dependency

Obtain the full text of Sudbury (1999), especially Theorem 7 and the edge-speed lemmas, and check whether **positive outward edge speed is the only lambda-dependent hypothesis** entering the finite-seed convergence argument. If yes, the exact `lambda=1/40` certificate immediately improves the theorem's parameter range, and `lambda_k -> 0` would solve the all-parameter problem.

If the full text remains inaccessible, reprove the bridge directly using Mountford's invariant-subsequence theorem plus the one-dimensional stationary classification and an argument excluding the empty component from subsequential limits.

### Priority B: understand the finite-window LP analytically

Let

```text
v_k(lambda)=sup_phi min_{u,z} D_{k,lambda}(u,z;phi),
lambda_k=inf{lambda>0 : v_k(lambda)>0}.
```

The computation suggests `lambda_k downarrow 0`. Questions that now look concrete:

- prove monotonicity or an approximate embedding `lambda_{k+1} <= lambda_k`;
- identify a probabilistic representation of the optimal corrector (e.g. a finite hitting-time/Poisson equation for the environment seen from the edge);
- derive an explicit `k(lambda)` with positive drift;
- explain the observed roughly `k^{-2}` scale.

This is a finite-state Markov-additive problem, not a cancellation problem.

### Priority C: keep DFP as a secondary route only

The exact signed-mixture norm calculation above is enough to reject “apply DFP ergodicity after a harmless change of basis.” Revisit DFP only if its quantitative exponent can be shown to beat the forced `y^{O(t)}` coefficient growth, or if a different spatial coupling emerges.

## 11. Source status

Sources checked:

- A. Sudbury, *Hunting submartingales in the jumping voter model and the biased annihilating branching process*, Adv. Appl. Probab. 31 (1999), 839--854, DOI `10.1239/aap/1029955207`. Publisher abstract: finite-seed convergence improved from `lambda>=1/3` to `lambda>=0.0347`; edge-speed bounds are given. Full text was not accessible in this session.
- T. S. Mountford, *A coupling of finite particle systems*, J. Appl. Probab. 30 (1993), 258--262. Publisher abstract: subsequential limits from finite configurations are invariant for a broad class; application gives BABP convergence for `lambda>1/3`.
- F. Martinelli, A. Shapira, C. Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461, Section 5, especially (5.2)--(5.4), Theorem 5.2, Application 1, Remarks 5.3--5.5.
- P. Lloyd and A. Sudbury, quasi-duality/thinning paper, Ann. Probab. 25 (1997), 96--114, for the algebraic origin of the DFP transform.
- The canonical project paper `paper/`, BABP subsection and Discussion, for patch statements and the explicit statement that finite-seed hard-model convergence is not obtained by the patch convergence theorem.

A targeted successor search found no post-2025 theorem removing the finite-seed `0.0347` restriction.

## Handoff to the Professor

Exact decisive files:

```text
research/active/babp-finite-seed/students/student-b/001-threshold-and-dfp.md
research/active/babp-finite-seed/students/student-b/edge-corrector-certificate.py
```

Suggested proof-spine changes:

```text
E2: mark substantially resolved. Replace “locate the historical threshold” by the
finite-window edge-corrector drift D_{k,lambda}; record k=1 -> 1/3 and
k=8 -> 0.03461954... -> historical 0.0347.

E3: record the DFP obstruction: no probability-law representation of the finite-test
cylinder; the unique finite-window signed representation has TV norm y^{|V\S|}.
Keep DFP only as a quantitative secondary route.

E4: replace the vague local-observable lemma by two concrete edges:
(a) verify/reprove that positive two-sided edge speed plus existing invariant-law/global-growth
inputs implies finite-seed local convergence;
(b) prove lambda_k -> 0, equivalently construct bounded finite-window edge correctors with
positive drift for every lambda>0.

New established project datum to audit: at lambda=1/40, k=10, there is an exact rational
corrector with uniform drift 1033/40000000 > 0. The verifier is the second file above.
```
