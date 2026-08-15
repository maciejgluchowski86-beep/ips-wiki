# Student A writeup 001: closest-prior-work audit and manuscript plan

Date: 2026-08-15

Updated after full-text comparison with Aidan Sudbury (1999), *Hunting submartingales in the jumping voter model and the biased annihilating branching process*, Adv. Appl. Probab. 31, 839--854.

## Executive correction

The full Sudbury text changes the novelty assessment materially.

### 1. The historical `0.0347` mechanism is now source-verified

The project reconstruction is correct. Sudbury's BABP construction is literally a finite-window edge-corrector/submartingale construction with an `m`-site window and one unresolved exterior bit. His `m=8` computation is the source of the published `0.0347` number.

More precisely, after reflection of left and right edges,

- Sudbury's `m` is the project's `k`;
- his binary `m`-block state is the project's edge word `u`;
- his right-hand end-value `x_{m+1}` is the project's exterior bit `z`;
- his correction vector `S_i` is the project's bounded corrector `phi(u)` up to the harmless reflection/sign convention for the chosen edge;
- his local gain
  $$
  a_i+\sum_jq_{ij}(S_j-S_i)
  $$
  is the same finite-state generator drift that the project writes as
  $$
  D_{k,\lambda}(u,z;\phi).
  $$

Sudbury does not formulate this as one linear programme. Instead, he regards the exterior bit as a state-dependent adversarial choice, his "Maxwell's demon", and iterates to the worst end-value assignment. Because each exterior choice changes only the row corresponding to the current `m`-block state, requiring the score to be a submartingale for **every possible assignment of end-values** is equivalent to requiring the local drift inequality for both values `z=0,1` in every state. This is exactly the project's statewise robust finite-window condition.

Table 2 on p. 850 then states explicitly

$$
m=8,\qquad \lambda_8=0.0347.
$$

Sudbury also says these values were found "by trial and error" and explicitly says the tabulated decimal was not proved to be a true critical value. Thus the project's independently computed `k=8` zero

$$
0.0346195434755\ldots
$$

should no longer be described as merely a numerical calibration to a possibly different construction. It is a numerical refinement of the same `m=8` finite-window feasibility boundary. Sudbury's `0.0347` is the safe decimal-grid value used by his computation and continuation argument, not an exact algebraic threshold.

**Provenance verdict:** the historical-mechanism identification is now **verified from source**, not inferred.

### 2. The general corrector-to-convergence implication is not a new theorem-level idea

This is the significant correction.

Sudbury's Section 3 does not merely prove an edge-speed theorem. He defines, for a finite particle configuration with right and left edges `Ri,Le`, the two-edge corrected span

$$
L=Ri-Le+S_{i(Ri)}+S_{i(Le)}-(2m+2)
$$

when the span is large enough, and `L=0` otherwise; he then seeks one correction vector making this a submartingale for every possible exterior assignment. Lemmas 5--9 construct exactly such a robust finite-window submartingale.

Immediately before Theorem 7, on p. 852, Sudbury states that the Neuhauser--Sudbury (1993) stationary-state argument **relied on the existence of a suitable submartingale**, that Section 3 has extended this condition from the old `1/3` range to `0.0347`, and that "the argument of their Section 5 can then proceed unchanged." Theorem 7 then gives finite-seed convergence.

Therefore the logical principle

> a suitable robust finite-window edge submartingale/corrector is a sufficient threshold-dependent input for finite-seed BABP convergence

is already present in the 1993/1999 argument. The project's stronger hypothesis

$$
D_{k,\lambda}(u,z;\phi)\ge v>0
$$

is certainly sufficient for Sudbury's "suitable submartingale" condition. `BABP-CONV-001` is a correct and useful self-contained theorem, but **the implication itself should not be advertised as new**.

The project's proof remains substantially different from what Sudbury 1999 writes down. Sudbury uses a corrected **global span** and then imports Neuhauser--Sudbury Section 5. The 1999 paper contains none of the project's explicit internal-gap machinery:

- no genealogy of individual internal vacant gaps;
- no corrected tagged-gap width with drift `<=-2v`;
- no exponential gap-lifetime or maximum-width tail;
- no Poisson endpoint-displacement estimate;
- no all-space nucleation compensator;
- no fixed-window nonescape estimate of the form
  $$
  \limsup_{t\to\infty}\mathbf P(B_t\cap[-M,M]=\varnothing)\le Ce^{-cM}.
  $$

But Sudbury 1999 delegates the actual convergence bridge to Neuhauser--Sudbury (1993), Section 5. Since that full section has still not been inspected, I do **not** claim that the project's tagged-gap proof technique is itself new. What is settled is the theorem-level priority question: the sufficiency of the finite-window submartingale is prior art.

### 3. The `lambda=1/40` result is a new range certificate inside Sudbury's mechanism, not a new mechanism

Sudbury's construction is generic in the window size `m`. Lemma 7 explicitly says that a submartingale for `m_1` extends to every larger `m_2` at the same parameter. More importantly, the minimax/end-value algorithm itself is defined for arbitrary fixed `m`; Sudbury simply reports BABP threshold searches only through `m=8` in Table 2.

The project calculation at

$$
k=10,\qquad \lambda=\frac1{40}
$$

therefore does **not** require a new conceptual device beyond Sudbury's finite-window submartingale mechanism. Under the exact identification above, the project's rational corrector is a valid `m=10` witness for Sudbury's local robust-submartingale problem. Feeding that witness into the old convergence architecture is enough in principle to extend the finite-seed theorem to `1/40`.

The genuinely new mathematical datum is the exact certificate/range extension:

$$
D_{10,1/40}(u,z;\phi)
\ge\frac{1033}{40000000}>0
$$

for all `2048` states. The project also gives a self-contained modern proof of convergence from this strict statewise inequality, with stronger intermediate noescape estimates than are stated in Sudbury 1999.

Thus the right description of the contribution is:

> extend Sudbury's finite-window submartingale computation from the published `m=8`, `0.0347` range to an exact rational `m=10` certificate at `lambda=1/40`, and give a self-contained internal-gap proof that such a strict statewise corrector implies finite-seed local convergence.

It is **not**:

> introduce the finite-window corrector method, or discover for the first time that such a corrector implies convergence.

## 1. Source-level comparison with Sudbury (1999)

### 1.1 Normalization is identical

Sudbury defines BABP by the flip rate

$$
c(x,\eta)
=
\bigl[\eta(x)+\lambda(1-\eta(x))\bigr]
\sum_{y\in N_x}\eta(y).
$$

Thus an occupied site dies at rate equal to its number of occupied nearest neighbours and a vacant site is born at rate `lambda` times that number. This is exactly the project convention

$$
0\to1\text{ at rate }\lambda N_x,
\qquad
1\to0\text{ at rate }N_x.
$$

There is no time rescaling and no parameter conversion between Sudbury's `lambda` and the project's `lambda`. His product density is exactly

$$
\frac{\lambda}{1+\lambda}.
$$

The MST conversion

$$
\lambda=q/p,
\qquad
L_{\mathrm{project}}=p^{-1}L_{\mathrm{MST}}
$$

is a separate modern convention issue and should remain explicit when MST is cited.

### 1.2 Exact state-space identification

Sudbury fixes the leftmost particle and records the `m` sites immediately to its right. Writing the configuration near that edge as

```text
... 0 1 x_1 ... x_m x_{m+1} ...
```

his finite state is the binary word `(x_1,...,x_m)` and `x_{m+1}` is the unresolved end-value. He emphasizes that for cancellative BABP there is no monotone worst choice for `x_{m+1}`.

Reflecting the picture gives the project right-edge state

```text
R, R-1, ..., R-k, R-k-1
```

with

```text
u=(u_1,...,u_k),
z=u_{k+1}.
```

So `m=k` literally, not only heuristically.

For a fixed assignment of end-values, Sudbury's `Q` is the infinitesimal generator of the `m`-block and

$$
a=\lambda\mathbf 1-b
$$

is the bare edge-position drift. The corrected one-edge gain in state `i` is

$$
a_i+\sum_jq_{ij}(S_j-S_i).
$$

This is the reflected version of `D_{k,lambda}(u,z;phi)`.

The important robust condition is Lemma 5: a single `S` makes the score a submartingale **for every possible assignment of end-values**. Since the end bit for each state may be selected independently, this is equivalent to statewise control for both `z=0` and `z=1` at every word `u`.

### 1.3 Sudbury's algorithm versus the project's LP

Sudbury's algorithm solves the same finite robust-control problem in a Bellman/minimax form:

1. assign one exterior bit to every `m`-block state;
2. solve the corresponding linear system `Q^*S=-a`;
3. change each assigned exterior bit according to the sign of the one-row perturbation `E^iS`;
4. iterate to a fixed worst assignment.

The project instead writes every local inequality simultaneously and optimizes the common margin `v` by linear programming.

These are two solution procedures for the same finite-window drift problem. Sudbury's later edge-speed Section 4 makes the common-margin form explicit: for a number `U_0` he seeks

$$
\sum_jq_{ij}(S_j-S_i)+a_i\ge U_0
$$

for all admissible end-value matrices, and deduces a lower edge-speed bound. This is directly the project's statewise `D>=v` formulation with `U_0=v`, after reflection.

### 1.4 The eight-site provenance is literal

Sudbury's Table 2, p. 850, is headed "Values of lambda for which a submartingale exists" and lists

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

He immediately explains that these are trial values rather than proved exact critical values. The `m=2` example is explicit: values at or above `0.2653` tried successfully while values at or below `0.2652` did not.

The project's `k=8` LP zero

$$
0.0346195434755\ldots
$$

therefore refines the same object. The published `0.0347` is a safe upper decimal from Sudbury's search, not a different normalization and not an unrelated speed threshold.

On p. 851 Sudbury explicitly calls the anchor `lambda_8=0.0347`; on p. 852 Lemma 9 extends the robust submartingale condition to every `lambda>=0.0347`, followed immediately by Theorem 7.

## 2. Convergence bridge: what is old and what is different

### 2.1 What Sudbury proves/uses

Sudbury's finite-configuration score is

$$
L
=
Ri-Le+S_{i(Ri)}+S_{i(Le)}-(2m+2)
$$

when `Ri-Le>=2m+1`, and zero otherwise. The correction at each outer edge is local; the score is a corrected total span.

His Section 3 establishes the existence of a suitable robust submartingale for every `lambda>=0.0347`. The final paragraph before Theorem 7 is decisive: Neuhauser--Sudbury's stationary-state proof relied on such a submartingale at `lambda>=1/3`; Sudbury has extended "this condition" to `0.0347`; their Section 5 then proceeds unchanged.

Hence a project statement asserting that **the existence of the appropriate finite-window statewise corrector is a sufficient input for finite-seed convergence** cannot be claimed as a new theorem-level principle.

### 2.2 What the project proof adds as a proof architecture

The project does not reuse Sudbury's global corrected span or the uninspected Neuhauser--Sudbury Section 5 proof. It gives an independent route:

1. place the same right/left corrector on the two particle populations bordering a tagged internal gap;
2. use one-dimensional gap genealogy to show births at width one, no splitting, and no merging of live positive gaps;
3. obtain a corrected gap width with drift at most `-2v`;
4. localize before applying the exponential test and obtain uniform lifetime and maximum-width tails;
5. dominate boundary displacement by a Poisson process;
6. truncate the all-space gap-nucleation compensator to `|x|<=N`, then remove the truncation by monotone convergence;
7. derive fixed-window nonescape;
8. combine stationarity of weak limits with stationary-law classification.

Sudbury 1999 does not state these intermediate results. In particular, its Section 4 edge-speed theorem is separate from the convergence proof and does not contain an internal-hole estimate.

This makes the present proof self-contained and quantitatively informative. It does **not**, on the evidence currently available, justify saying that the internal-gap proof idea itself is historically new, because the precise proof inside Neuhauser--Sudbury (1993), Section 5 remains uninspected.

### 2.3 Strength comparison

As hypotheses, the project theorem is not stronger than Sudbury's historical framework. It assumes a uniform strict margin `v>0`; Sudbury phrases the convergence input as existence of a suitable submartingale robust to all end-values, and his edge-speed section separately formulates positive common gain `U_0`.

As intermediate conclusions, the project proof is stronger/more explicit than anything stated in Sudbury 1999: it yields exponential tagged-gap tails and a quantitative fixed-window nonescape bound. The final convergence conclusion is the same type of deterministic finite-seed local convergence.

## 3. Does Sudbury already give convergence below `0.0347`?

No such result appears in the paper.

- Table 2 stops at `m=8`.
- Lemma 9 and Theorem 7 stop at `lambda>=0.0347`.
- Section 4 gives edge-speed bounds for selected parameters and reports BABP calculations for `m=4` and `m=8`, not a lower finite-seed convergence threshold.

But there is also no conceptual barrier in Sudbury's method at eight sites. The construction and the minimax algorithm are defined for arbitrary fixed `m`. Therefore the project `k=10` certificate is best viewed as extending the same method computationally and certifiably.

In particular, `lambda=1/40` does **not** require a new convergence mechanism once the `m=10` certificate is known: Sudbury's own logic says the stationary-state argument can be rerun whenever a suitable finite-window submartingale is available. The project's self-contained `BABP-CONV-001` is useful because it removes reliance on that historical black box and records all hypotheses cleanly, not because the abstract implication was absent from the literature.

## 4. Revised novelty verdict

### 4.1 Concrete range improvement

**Status: strongly supported as a genuine literature-range extension.**

The full closest predecessor now confirms that its finite-seed theorem stops at `lambda>=0.0347`, and that this number came from an `m=8` finite-window computation. The earlier successor search through 2026-08-15 found no later same-model finite-seed theorem below that range.

Thus the defensible contribution is:

> an exact rational ten-site certificate extends Sudbury's finite-window submartingale method to `lambda=1/40=0.025`, yielding deterministic finite-seed convergence below Sudbury's published `0.0347` range.

I still recommend against absolute bibliometric language such as "first ever" or "best known" unless a fresh independent literature auditor repeats the successor search. But the former reason for withholding range-priority language -- inability to inspect Sudbury itself -- is gone.

### 4.2 General statewise-corrector criterion

**Status as novelty: refuted.**

The project theorem is mathematically verified but should not be sold as a new theorem-level implication. Sudbury 1999 explicitly identifies the suitable finite-window submartingale as the threshold-dependent hypothesis on which the earlier convergence proof relies and applies that implication to obtain Theorem 7.

A safe description is:

> We give a self-contained proof, via internal-gap contraction and nonescape, of the finite-window-submartingale convergence implication used in the classical BABP argument.

Whether this **particular proof** is new remains unresolved until Neuhauser--Sudbury (1993), Section 5 is read in full.

### 4.3 Finite-window method

**Status as novelty: refuted.**

Sudbury 1999 explicitly uses the same `m`-block, one exterior end-value, worst-case state-dependent assignment, and corrected edge score. Sudbury 1998 is an additional methodological predecessor. The project should not say it introduces finite-window edge correctors, state-dependent boundary optimization, or the underlying finite-state submartingale search.

### 4.4 What is clearly project-specific

- the exact rational `k=10`, `lambda=1/40` certificate;
- the exact minimum drift `1033/40000000` verified over all `2048` states;
- the direct LP formulation and exact machine-checkable certificate format;
- the self-contained tagged-internal-gap proof with localization and finite-spatial-truncation repairs;
- the current all-parameter front-environment reduction, if it survives its separate audit.

## 5. Remaining source limitations

### Mountford (1993)

Still not obtained in full. Its published abstract supports the historical stationary-limit role, but its exact hypotheses and proof were not checked line by line. This is no longer a correctness dependency because Jahnel--Köppl (2026) supplies the stationary-limit theorem used by `BABP-CONV-001`.

### Ramírez--Varadhan (1996)

Still not obtained in full. Exact hypotheses remain unverified from source. Again this is provenance only, not a theorem dependency.

### Neuhauser--Sudbury (1993), Section 5

The full proof referred to by Sudbury 1999 has not been inspected. This no longer leaves the **logical corrector-to-convergence implication** unresolved -- Sudbury 1999 explicitly says that is the condition his theorem reuses -- but it does leave open whether the project's detailed internal-gap proof architecture is historically new.

### Sudbury (1998)

Full text remains uninspected. It is already clear that finite-boundary computational submartingales predate the project. A full read would improve methodological attribution but is no longer needed to settle the central 1999 provenance question.

## 6. Revised manuscript packaging

Keep the staged short note, but change its center of gravity.

The note should **not** be presented as introducing a new convergence criterion. It should present:

1. Sudbury's finite-window framework in modern statewise-corrector notation;
2. the exact rational `k=10`, `lambda=1/40` certificate as the range-extending result;
3. a self-contained proof of the classical corrector-to-convergence bridge through internal gaps and nonescape;
4. the modern stationary-limit/stationary-law interfaces with explicit normalization;
5. a short discussion of the all-parameter front problem.

A better working title is:

> **An exact finite-window certificate below Sudbury's BABP finite-seed range**

or, if the self-contained proof is emphasized,

> **Finite-window submartingales and finite-seed convergence for the one-dimensional biased annihilating branching process**

## 7. Safe novelty language after the full-text audit

Recommended introduction language:

> Sudbury proved finite-seed convergence for one-dimensional BABP for `lambda>=0.0347` using a computer-assisted finite-window submartingale construction. His `0.0347` value comes from an eight-site window. We extend the same finite-window mechanism to an exact rational ten-site certificate at `lambda=1/40`, with uniform statewise drift `1033/40000000`. This yields finite-seed convergence at `lambda=1/40`. For completeness, we give a self-contained convergence proof from a strict statewise corrector, based on contraction of internal vacant gaps and a fixed-window nonescape estimate.

Recommended historical sentence:

> The finite-window mechanism itself and its use as the threshold-dependent input for finite-seed convergence are due to Neuhauser--Sudbury and Sudbury; our contribution is the exact below-range certificate and the self-contained internal-gap proof recorded here.

Do not write:

- "we introduce finite-window edge correctors";
- "we prove for the first time that a positive statewise edge corrector implies finite-seed convergence";
- "the `0.0347` mechanism was previously unknown";
- "Sudbury's threshold merely happens numerically to match our `k=8` LP".

Potentially safe after one independent successor-literature confirmation:

- "we improve Sudbury's published finite-seed parameter range";
- "the first parameter improvement over the `0.0347` range found in the literature since Sudbury".

I would still avoid "best known" without a broader bibliographic check than this project has performed.

## 8. Claim-registry correction requested

The **mathematical statements** of `BABP-EDGE-001` and `BABP-CONV-001` do not need weakening. Their novelty/provenance wording does need correction.

### `BABP-EDGE-001`

Replace the current historical boundary saying literal identity with Sudbury's internal computation is unverified.

Suggested replacement:

> Historical provenance: Sudbury (1999), Section 3, uses the same finite-window robust edge-submartingale mechanism. His `m`-block is the reflected version of the present `k`-site edge word and his unresolved end-value is the present exterior bit. Table 2 explicitly gives the `m=8` value `0.0347`. The independently computed project zero `0.0346195434755...` is a refinement of this same eight-site feasibility boundary; Sudbury reports `0.0347` as a trial value rather than an exact critical root.

### `BABP-CONV-001`

Keep the verified theorem and the tagged-gap proof record, but revise the novelty paragraph.

Suggested replacement:

> Historical provenance: Sudbury (1999), immediately before Theorem 7, states that the Neuhauser--Sudbury (1993) finite-seed convergence argument relies on existence of a suitable finite-window submartingale and that, once his Section 3 extends that condition to `lambda>=0.0347`, their Section 5 proceeds unchanged. Thus the abstract implication from an appropriate finite-window submartingale to finite-seed convergence is classical rather than a new project principle. The project proof is an independent self-contained proof under the stronger uniform statewise margin hypothesis, using tagged internal gaps, exponential gap tails, a spatial compensator, and nonescape. Priority of this specific proof mechanism has not been checked against the full Neuhauser--Sudbury (1993) Section 5.

Replace the current novelty-status sentence with:

> Novelty status: the exact `lambda=1/40`, `k=10` certificate appears to extend the published finite-seed range beyond Sudbury's `m=8`, `0.0347` computation; the finite-window method and corrector-to-convergence principle themselves are prior work. A successor search through 2026-08-15 found no later below-`0.0347` finite-seed theorem.

The Professor should make this registry change because it is stable-main provenance metadata. I have not edited the registry in this student assignment.

## Handoff to Professor

**Closest prior theorem:** Sudbury (1999), Theorem 7, with Section 3 Lemmas 5--9 and Table 2.

**Historical mechanism:** **verified from source**. The published `0.0347` is literally the `m=8` finite-window submartingale computation in the same normalization as the project. The project's `k=8` LP is the same finite-state problem written directly as statewise drift inequalities.

**General criterion novelty:** **refuted**. Sudbury explicitly says the earlier finite-seed convergence argument relies on a suitable submartingale and proceeds unchanged once his finite-window condition is extended. `BABP-CONV-001` is a self-contained reproof under a strict statewise hypothesis, not a new theorem-level implication.

**Concrete range novelty:** **strongly supported**. Sudbury stops at `m=8`, `lambda>=0.0347`; no successor below that range was found in the prior search. The `k=10`, `lambda=1/40` certificate is a range extension within Sudbury's mechanism.

**Does a larger Sudbury window trivially reach `1/40`?** Yes in the conceptual sense: his construction is defined for arbitrary fixed `m`, and the project's `k=10` witness is exactly a valid `m=10` witness. The new content is finding and exactly certifying that witness, not inventing a new finite-window mechanism.

**Remaining historical uncertainty:** only proof-method priority at the level of the project's detailed internal-gap/nonescape argument, because Neuhauser--Sudbury (1993), Section 5 remains uninspected. Mountford (1993) and Ramírez--Varadhan (1996) also remain unavailable in full, but are not correctness dependencies.

**Claim registry:** provenance/novelty wording should change as specified in Section 8; the mathematical verified claim statements need not change.