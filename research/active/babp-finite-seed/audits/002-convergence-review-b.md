# Independent convergence review B: statewise edge corrector to finite-seed convergence

Date: 2026-08-15

Role: fresh independent correctness reviewer. I did not participate in the proof, the Professor verification, or audit 001. I treated the repository as evidence, not authority. I rederived the gap argument from the BABP transition rules, checked the analytic estimates and their uniformity, and independently checked the external theorem interfaces against primary sources where accessible.

## Verdict

**PASS. `BABP-CONV-001` is correct as stated.**

For fixed `lambda>0`, the statewise corrector hypothesis

$$
\exists k\ge1,\ \phi:\{0,1\}^k\to\mathbb R\text{ bounded},\ v>0
\quad\text{such that}\quad
D_{k,\lambda}(u,z;\phi)\ge v
$$

for every `u in {0,1}^k` and `z in {0,1}` implies local weak convergence of one-dimensional BABP from every finite nonempty deterministic initial particle set to Bernoulli product equilibrium of particle density

$$
q=\frac{\lambda}{1+\lambda}.
$$

I found no hidden hypothesis on the initial finite configuration and no use, explicit or implicit, of the 2025 particle-number growth theorem.

The concrete corollary at

$$
\lambda=\frac1{40},\qquad k=10,\qquad
v=\frac{1033}{40000000}
$$

is therefore valid **provided the separately verified `BABP-EDGE-001` certificate is taken as an input**. I checked that the certificate/audit use the same particle convention and the same drift `D` as the convergence theorem. I did not repeat audit 001's independent evaluation of all 2048 rational inequalities; that claim is already the explicitly separated verified premise.

There is one source qualification, but it does not leave the theorem conditional. Mountford's 1993 paper is accessible to me only through its published abstract, and I could verify Ramírez--Varadhan (1996) bibliographically but could not obtain its full body. I therefore do **not** claim a line-by-line hypothesis check of either older proof. However, Jahnel--Köppl (2026), Theorem 2.5, is accessible in full and proves exactly the stationary-limit statement needed here under hypotheses that BABP satisfies directly. Thus the stationary-limit step itself is verified, not merely relied upon.

The only changes I would request before manuscript use are expository: add a standard localization sentence when applying the killed-generator inequality to the unbounded function `exp(theta Z)`, and state the generator/time-rescaling convention explicitly when citing Martinelli--Shapira--Toninelli. Neither affects the theorem.

---

## 1. Model convention and normalization

I use particle variables `xi(x) in {0,1}`, with `xi(x)=1` meaning a BABP particle. Put

$$
N_x(\xi)=\xi(x-1)+\xi(x+1).
$$

The project convention is the single-site flip process

$$
0\to1\quad\text{at rate }\lambda N_x(\xi),
\qquad
1\to0\quad\text{at rate }N_x(\xi).
$$

Equivalently, each particle places offspring on a vacant nearest neighbour at rate `lambda` and each occupied nearest neighbour contributes death rate `1` to a particle. This is the convention in Neuhauser--Sudbury (1993), whose published abstract explicitly describes offspring rate `lambda`, destruction rate `1`, and product density `lambda/(1+lambda)`.

Martinelli--Shapira--Toninelli (2025) use the complementary spin variable `eta=1-xi`, where `eta=0` is an infection. They write `q` for infection density, `p=1-q`, and

$$
c_x(\eta)=2-\eta_{x-1}-\eta_{x+1}=N_x(\xi).
$$

Their flip generator gives

$$
\eta_x:1\to0\text{ at rate }qN_x,
\qquad
\eta_x:0\to1\text{ at rate }pN_x.
$$

Therefore, after the deterministic time rescaling by `1/p`, their BABP is exactly the present convention with

$$
\lambda=\frac qp,
\qquad
q=\frac{\lambda}{1+\lambda},
\qquad
p=\frac1{1+\lambda}.
$$

Multiplying a generator by a positive constant does not change its stationary laws. Thus there is no parameter or normalization mismatch in the stationary-law citation.

---

## 2. External stationary-limit theorem

### 2.1 Mountford and Ramírez--Varadhan: what I could verify

T. S. Mountford, *A coupling of finite particle systems*, J. Appl. Probab. 30 (1993), 258--262, DOI `10.2307/3214638`, exists. Its published abstract states that for a large class of one-dimensional interacting particle systems started from a finite configuration, any limit measure along times tending to infinity is invariant. The same abstract says this is applied to one-dimensional BABP for the then-known parameter range `lambda>1/3`.

I could not obtain the paper body, so I cannot certify its exact class/hypotheses from the source itself. The abstract verifies the claimed theorem statement at the level needed to identify the result, but not a line-by-line interface audit.

A. F. Ramírez and S. R. S. Varadhan, *Relative entropy and mixing properties of interacting particle systems*, J. Math. Kyoto Univ. 36 (1996), 869--875, is also real; its bibliographic record is MR1443753 and the Project Euclid record is `euclid.kjm/1250518457`. I did not obtain the full text in this review. I therefore mark the exact Ramírez--Varadhan hypotheses **not independently verified from source**.

### 2.2 The required input is nevertheless verified via Jahnel--Köppl

B. Jahnel and J. Köppl, *Restriction and mixing properties of interacting particle systems with unbounded range*, arXiv:2603.21817 (2026), Theorem 2.5, is accessible in full. The paper explicitly presents its one-dimensional result as a generalization of Mountford and Ramírez--Varadhan. Theorem 2.5 says, in particular, that every weak limit point of the one-dimensional dynamics is stationary when `(L1)` and `(R1)--(R3)` hold with exponentially decaying influence.

BABP satisfies these assumptions directly for every fixed `lambda>0`:

- local state space is finite, `{0,1}`;
- updates are single-site, so update diameter is uniformly bounded (`R1`);
- the total rate at which a fixed site changes is at most
  $$
  2\max(1,\lambda),
  $$
  giving `(L1)`;
- changing a spin at `y` can alter the flip rate at `x` only when `|x-y|=1`, and the change is bounded by a constant depending only on `lambda`; hence the influence kernel has finite range and satisfies `(R3)` for every exponential profile allowed in the theorem.

The theorem does not require attractiveness, reversibility, shift-invariance of the initial law, or positive rates. It applies to the present scaled generator itself.

**Conclusion:** every weak subsequential limit of BABP from the finite seed is stationary. This imported step is verified.

---

## 3. Stationary-law classification

Martinelli--Shapira--Toninelli (2025), Corollary 2.9, states for the one-dimensional FA-1f process that every stationary law is a convex combination of equilibrium and the completely healthy configuration, and immediately states that the same conclusion holds for BABP (and the `delta`-West process). No translation-invariance assumption is imposed in one dimension; the preceding Theorem 2.5 is precisely the step removing that assumption.

Translated to particle variables and the present normalization, every stationary BABP law is therefore

$$
\nu=\alpha\delta_{\varnothing}+(1-\alpha)\pi_q,
\qquad \alpha\in[0,1],
$$

where `pi_q` is Bernoulli product measure of particle density `q=lambda/(1+lambda)`.

This is also consistent with the original Neuhauser--Sudbury (1993) source, whose published abstract states in the original offspring-`lambda`/death-`1` convention that the product law of density `lambda/(1+lambda)` and the empty state are the stationary laws on `Z`.

**Conclusion:** the stationary-law classification exists, is all-parameter for `lambda>0`, is genuinely one-dimensional without a translation-invariance hypothesis, and matches the project's convention after the explicit scalar time rescaling above.

---

## 4. Gap combinatorics

An internal gap is a maximal nonempty finite vacant interval strictly between the outermost particles.

### 4.1 Births of new gaps

A particle at `x` can die only if at least one nearest neighbour is occupied. If both neighbours are occupied and `x` dies, the new vacant component is exactly `{x}`, so a newly nucleated internal gap has width one.

If exactly one neighbour of `x` is occupied and the other is vacant, then the death at `x` enlarges the already existing gap adjacent to the vacant neighbour. It does not nucleate a new genealogy. A death at an outer edge changes the outer edge.

### 4.2 Interior births cannot split a gap

If a vacant site lies strictly inside a positive gap, neither nearest neighbour is occupied. Its birth rate is therefore zero. Births into a gap can occur only at the endpoint vacancies. Such a birth shrinks the gap by one; at width one it closes the gap.

### 4.3 Positive gaps cannot merge

Suppose two positive gaps are separated by a finite block of particles. Deaths at the exposed ends of that block can reduce its length. If only one separating particle remains, both of its nearest neighbours are vacant. Its death rate is then zero. Hence the last separator cannot disappear while both gaps are positive.

There may be new gap nucleations inside a longer separating particle block, but this creates additional gap genealogies; it does not merge existing ones.

Thus each positive gap has an unambiguous genealogy from nucleation until closure, with neither splitting nor merging. This is exactly what the later compensator count needs.

---

## 5. Re-derivation of the corrected tagged-gap drift

Fix a tagged gap while it is alive. Let `A` be all particles strictly to its left and `C` all particles strictly to its right. Let

$$
a=R(A),\qquad b=L(C),\qquad g=b-a-1\ge1.
$$

Both `A` and `C` remain finite and nonempty before closure. In particular, if one side consists of a single particle, that particle has no occupied neighbour on the gap side and no occupied neighbour on its other side, so it cannot die.

Define

$$
H_R(A)=R(A)+\phi(U_R(A)).
$$

Hypothesis `(EC)` is exactly

$$
\mathcal L H_R(A)\ge v
$$

for every finite nonempty `A`. By reflection, if

$$
H_L(C)=L(C)-\phi(U_L(C)),
$$

then

$$
\mathcal L H_L(C)\le -v.
$$

Now put

$$
Z=H_L(C)-H_R(A)-1
=g-\phi(U_L(C))-\phi(U_R(A)).
$$

If `K=||phi||_infty`, then while the gap is alive,

$$
g-2K\le Z\le g+2K.
$$

For `g>=2`, no transition sees particles from both `A` and `C`: all nonzero rates decompose exactly into the two standalone BABP generators. Hence

$$
\mathcal L^{\times}Z
=\mathcal L_C H_L-\mathcal L_A H_R
\le -2v.
$$

The width-one case is the only possible cross-gap issue. If `g=1`, the sole vacancy has one occupied neighbour from each side, so its total birth rate in the original BABP is `2lambda`. This is exactly the sum of the standalone left-edge birth rate `lambda` and standalone right-edge birth rate `lambda`. Each such transition closes the gap.

For the killed tagged-gap process, define every closing transition to send the process to a cemetery state where the exponential test function below is zero. The corresponding product-generator transition would instead send it to a state where that test function is positive. Therefore killing can only decrease its generator. There is no omitted cross-gap event and no extra rate factor.

This verifies the central statewise implication: the same edge corrector gives a uniformly contracting corrected internal-gap width, with constants independent of gap age, position, surrounding configuration, or total particle number.

---

## 6. Uniform exponential lifetime and width tails

A single nonclosing transition can change only one of the two edge-corrector terms. Thus one may take

$$
J=1+2K
$$

as a uniform bound on `|Delta Z|`.

For each side, only the edge birth, possible edge death, and flips of the `k` recorded sites can change the corresponding `H`. Hence the total rate of `Z`-changing events is bounded by a deterministic constant such as

$$
\rho=2\bigl[\lambda+1+2k\max(1,\lambda)\bigr].
$$

For `f=e^{\theta Z}` and `|Delta Z|<=J`,

$$
e^{\theta\Delta Z}-1
\le \theta\Delta Z+
\frac{\theta^2}{2}e^{\theta J}(\Delta Z)^2.
$$

Therefore, for the product generator,

$$
\frac{\mathcal L^{\times}f}{f}
\le -2v\theta+
\frac{\theta^2}{2}e^{\theta J}\rho J^2.
$$

Choose `theta>0` so small that

$$
\frac{\theta}{2}e^{\theta J}\rho J^2\le v.
$$

Then, with `gamma=v theta`, the killed generator satisfies

$$
\mathcal L^{\dagger}e^{\theta Z}
\le -\gamma e^{\theta Z}.
$$

The function `e^{theta Z}` is unbounded as the gap width grows. This is not a problem, but the polished proof should say explicitly: stop at the first time `g` (or `Z`) reaches level `n`, apply Dynkin's formula to the bounded stopped process, and let `n->infinity` using Fatou/monotone localization. The bounded jump rate makes the standard localization immediate.

Let `tau` be the closure time of a gap born at width one. Since on survival

$$
Z_t\ge 1-2K,
$$

and initially

$$
Z_0\le1+2K,
$$

the killed-semigroup estimate yields a uniform constant `C_0` such that

$$
\mathbf P(\tau>t)\le C_0e^{-\gamma t}.
$$

Likewise, if

$$
\sigma_m=\inf\{t<\tau:g_t\ge m\},
$$

optional stopping of the localized positive supermartingale gives

$$
\mathbf P(\sigma_m<\tau)
\le C_1e^{-\theta m}.
$$

The constants depend only on `(k,lambda,phi,v)`. They do not depend on the global configuration, the gap's birth place, its age, or the number of particles elsewhere. For an initial deterministic gap of width `g_0`, the same lifetime estimate holds with a finite prefactor depending on `g_0`; this is sufficient because there are only finitely many initial gaps.

**Conclusion:** the uniformity claimed in the proof is genuine, not merely a per-gap asymptotic statement.

---

## 7. Displacement estimate

Let `N_t` count changes of either endpoint of the tagged vacant interval before closure.

For each boundary:

- an extension occurs when the boundary particle dies. Its gap-side neighbour is vacant, so at most its particle-side neighbour contributes to the death rate. Hence extension rate is at most `1`;
- a shrinkage occurs by birth into the adjacent gap vacancy at rate `lambda` from that boundary particle.

At width one the two closing birth clocks contribute total rate `2lambda`. Therefore the predictable intensity of `N_t` is bounded by

$$
\beta=2(1+\lambda).
$$

Using the standard thinning construction, `N_t` is stochastically dominated by a rate-`beta` Poisson process.

A gap born as the singleton `{x}` that contains the origin at age `r` must have moved at least one endpoint from `x` across distance `|x|`. Since every endpoint shift is by exactly one lattice unit,

$$
N_r\ge |x|.
$$

If `E_{m,r,x}` is the event that this genealogy is alive at age `r`, has width at least `m`, and contains the origin, then

$$
E_{m,r,x}
\subset
\{\sigma_m<\tau\}\cap\{\tau>r\}\cap\{N_r\ge|x|\}.
$$

For three events `A,B,C`,

$$
\mathbf P(A\cap B\cap C)
\le \min(\mathbf P(A),\mathbf P(B),\mathbf P(C))
\le [\mathbf P(A)\mathbf P(B)\mathbf P(C)]^{1/3}.
$$

No independence is required. Consequently

$$
\mathbf P(E_{m,r,x})
\le C e^{-c_1m}e^{-c_2r}
\mathbf P(\operatorname{Pois}(\beta r)\ge|x|)^{1/3}.
$$

Finally,

$$
\sum_{x\in\mathbb Z}
\mathbf P(\operatorname{Pois}(\beta r)\ge|x|)^{1/3}
\le C_\beta(1+r).
$$

Indeed, the `O(1+r)` sites up to a sufficiently large constant multiple of the mean contribute at most one each; beyond that cutoff the Chernoff bound

$$
\mathbf P(\operatorname{Pois}(\beta r)\ge n)
\le (e\beta r/n)^n
$$

is geometrically summable even after taking the cube root.

---

## 8. Compensator sum over nucleations

A new gap is nucleated at `x` exactly when `x` is occupied, both neighbours are occupied, and the particle at `x` dies. In the present convention the nucleation intensity at a fixed site is therefore at most `2`.

Because positive gaps neither merge nor split, every post-time-zero gap present at time `t` has one unique nucleation event `(x,s)` as ancestor.

Condition on such a nucleation. Immediately after the jump the new gap has width one, and Sections 6--7 give a future estimate uniform in the entire post-jump configuration. By the strong Markov property and the predictable compensator of the nucleation point process,

$$
\begin{aligned}
&\mathbf P(\text{some post-time-zero gap of width at least }m
\text{ contains }0\text{ at time }t)\\
&\quad\le
2\sum_{x\in\mathbb Z}\int_0^t
C e^{-c_1m}e^{-c_2(t-s)}
\mathbf P(\operatorname{Pois}(\beta(t-s))\ge|x|)^{1/3}\,ds\\
&\quad\le
C'e^{-c_1m}
\int_0^\infty e^{-c_2r}(1+r)\,dr\\
&\quad\le C''e^{-cm}.
\end{aligned}
$$

The spatial sum is finite for each `r`, so Tonelli/compensator interchange is legitimate. The time integral is finite because of the exponential lifetime factor. This is the point at which a merely per-gap estimate would have been insufficient; the displacement factor makes the sum over all possible birth locations convergent.

There are finitely many internal gaps initially. Each has a deterministic finite width and hence a survival probability tending to zero exponentially in `t` with a finite initial-width-dependent prefactor. Their contribution disappears after taking `limsup_{t->infinity}`.

Thus, if

$$
G_m(t)=\{0\text{ lies in an internal gap of width at least }m\},
$$

then

$$
\limsup_{t\to\infty}\mathbf P_B(G_m(t))
\le Ce^{-cm},
$$

with `C,c` independent of `m` and of late time `t`.

This verifies the strongest analytic point requested in the audit: the result is a uniform late-time bound after summing all nucleations, not a collection of unrelated per-gap tail estimates.

---

## 9. From internal-gap control to local nonescape

The already verified consequence of `(EC)` is

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v,
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-v
\quad\text{a.s.}
$$

for every finite nonempty initial set. The process cannot hit the empty state from such an initial set: once only one particle remains, its death rate is zero. Hence the two edges are always defined.

For each fixed `M`, the ballistic bounds imply

$$
\mathbf P_B(R_t\le M\text{ or }L_t\ge-M)\to0.
$$

On the complementary event, if `B_t` has no particle in `[-M,M]`, then particles lie strictly to both sides of that window, so `[-M,M]` is contained in an internal gap of width at least `2M+1`. Hence

$$
\begin{aligned}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
&\le
\mathbf P_B(R_t\le M\text{ or }L_t\ge-M)
+\mathbf P_B(G_{2M+1}(t)).
\end{aligned}
$$

Taking `limsup` in `t` gives

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

Crucially, the constants come from the uniform tagged-gap analysis and are independent of `M`. Therefore

$$
\lim_{M\to\infty}\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)=0.
$$

---

## 10. The clopen-cylinder argument forces `alpha=0`

The configuration space `{0,1}^Z` is compact and metrizable in the product topology. Take any sequence `t_n->infinity` and a weakly convergent subsequence of the laws, with limit `nu`.

By the verified one-dimensional stationary-limit theorem, `nu` is stationary. By the verified stationary classification,

$$
\nu=\alpha\delta_{\varnothing}+(1-\alpha)\pi_q.
$$

For fixed `M`, the event

$$
E_M=\{B\cap[-M,M]=\varnothing\}
$$

is a finite-coordinate cylinder and therefore clopen. Weak convergence gives exact convergence of its probabilities:

$$
\nu(E_M)=\lim_n\mathbf P_B(B_{t_n}\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

On the other hand, the mixture formula is

$$
\nu(E_M)
=\alpha+(1-\alpha)(1-q)^{2M+1}
\ge\alpha.
$$

Hence

$$
\alpha\le Ce^{-cM}
$$

for every `M`, and `M->infinity` yields `alpha=0`.

Every subsequential limit is therefore `pi_q`. Compactness then implies the full local weak convergence

$$
\operatorname{Law}_B(B_t)\Longrightarrow\pi_q.
$$

The clopen-cylinder step is exact and does not merely prove `alpha<1`.

---

## 11. Scope and dependency audit

### Initial state

The proof uses only:

1. the initial set is finite, so the outer edges and finitely many initial gaps are well defined;
2. it is nonempty, so the process never reaches the empty configuration and the edge correctors remain defined.

No connectedness, minimum particle number, parity, initial gap bound uniform over a class, or spatial-location assumption is used. Therefore the claimed scope “every finite nonempty deterministic initial particle set” is correct.

### Particle-number growth

The Martinelli--Shapira--Toninelli 2025 linear-growth result for `|B_t|` is not used. The proof instead uses:

- statewise edge corrector drift for the two outer edges;
- the same statewise drift on the two populations bordering each internal gap;
- bounded local jump rates;
- Poisson displacement;
- the nucleation compensator;
- generic one-dimensional stationary-limit invariance;
- stationary-law classification.

No step requires a lower bound on `|B_t|` or on its growth rate.

---

## 12. The `lambda=1/40` corollary and published boundary

The exact certificate in `students/student-b/edge-corrector-certificate.py` is in the same time-scaled convention audited here, and audit 001 independently verified

$$
D_{10,1/40}(u,z;\phi)
\ge \frac{1033}{40000000}>0
$$

for all `2^11` edge states. Thus the hypothesis `(EC)` of the theorem is satisfied at `lambda=1/40`.

Martinelli--Shapira--Toninelli (2025), Remark 5.4, records finite-seed convergence for `lambda>1/3` from Mountford and the improved threshold `lambda>0.0347` from Sudbury (1999), Theorem 7. Sudbury's published abstract states the corresponding extension at `lambda>=0.0347` and gives edge-speed bounds. The strict inequality/equality convention at the historical endpoint is irrelevant here because

$$
\frac1{40}=0.025<0.0347.
$$

Therefore the project corollary is a genuine strict extension below the previously published finite-seed convergence range.

---

## 13. Minor proof-writing repairs, not mathematical objections

I would make the following two edits before promoting this argument into a paper.

1. **Localize the exponential test function.** `e^{theta Z}` is unbounded over all possible gap widths. The killed-generator calculation is valid statewise, but the semigroup/optional-stopping consequences should be written with a stopping level `g<=n` (or `Z<=n`) and then `n->infinity`. Bounded jump sizes and bounded `Z`-changing rate make this routine.

2. **State the time rescaling at the stationary-law citation.** Martinelli--Shapira--Toninelli's `q,p` refresh normalization is a factor `p` slower than the project's death-rate-one convention. Write explicitly `lambda=q/p` and `L_project=p^{-1}L_MST` to prevent a reader from suspecting a parameter mismatch.

Neither repair changes a hypothesis, constant, or conclusion.

---

## Final decision

I find no failing step.

The implication

$$
(EC)\Longrightarrow\text{finite-seed local convergence to }\pi_{\lambda/(1+\lambda)}
$$

is correct for every fixed `lambda>0` for which `(EC)` holds, from every finite nonempty deterministic initial set.

Combined with verified `BABP-EDGE-001`, this proves finite-seed convergence at `lambda=1/40`.

I therefore recommend that this audit be counted as an **accepting independent review** of `BABP-CONV-001`. Per the project protocol, this review by itself should not change the registry status; promotion remains the Professor's action after the other independent audit is received and any objections are reconciled.

## Sources checked

- T. S. Mountford, *A coupling of finite particle systems*, Journal of Applied Probability 30 (1993), 258--262, DOI `10.2307/3214638`. Published abstract checked; full theorem hypotheses not independently checked because the body was not available to me.
- A. F. Ramírez and S. R. S. Varadhan, *Relative entropy and mixing properties of interacting particle systems*, Journal of Mathematics of Kyoto University 36 (1996), 869--875, MR1443753, Project Euclid `euclid.kjm/1250518457`. Existence/bibliography checked; full theorem body not obtained.
- B. Jahnel and J. Köppl, *Restriction and mixing properties of interacting particle systems with unbounded range*, arXiv:2603.21817 (2026), especially assumptions `(L1)`, `(R1)--(R3)` and Theorem 2.5. Full source checked and used for the stationary-limit interface.
- F. Martinelli, A. Shapira, and C. Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461 (2025), especially equations (1.4)--(1.9), Corollary 2.9, and Remark 5.4. Full HTML source checked.
- C. Neuhauser and A. Sudbury, *The biased annihilating branching process*, Advances in Applied Probability 25 (1993), 24--38, DOI `10.2307/1427494`. Published abstract checked for the original rate convention, equilibrium density, and stationary-law statement.
- A. Sudbury, *Hunting submartingales in the jumping voter model and the biased annihilating branching process*, Advances in Applied Probability 31 (1999), 839--854, DOI `10.1239/aap/1029955207`. Published abstract checked for the `0.0347` finite-seed range and edge-speed statement.
