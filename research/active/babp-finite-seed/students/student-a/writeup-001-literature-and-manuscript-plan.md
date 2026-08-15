# Student A writeup 001: closest-prior-work audit and manuscript plan

Date: 2026-08-15

## Executive conclusion

The verified project result is mathematically ready for a focused note, but the priority language should remain deliberately asymmetric.

For the **concrete finite-seed convergence result at**

$$
\lambda=\frac1{40}=0.025,
$$

I found no source through 2026-08-15 proving the same one-dimensional BABP finite-seed convergence theorem at any parameter below the `0.0347` range recorded by Martinelli--Shapira--Toninelli (2025). The closest same-target theorem I found is Sudbury (1999), whose published abstract says that finite nonzero initial configurations converge to Bernoulli equilibrium for `lambda >= 0.0347` and that edge-speed bounds are obtained. Martinelli--Shapira--Toninelli, Section 5 and Remark 5.4, still record the finite-seed range as `lambda>0.0347` after proving their new all-parameter DFP and BABP results. Searches of successor literature, alternate terminology, author/citation pages, recent preprints, and a 2026 IPS reference book did not reveal a later below-threshold theorem.

I therefore rate the concrete range improvement as **strongly supported by the accessible literature search**, but I do **not** recommend a publication-level sentence of the form "first", "best known", or "improves the best known threshold" yet. The main reason is source incompleteness, not a positive indication of overlap: I could not inspect the body of Sudbury (1999), and its exact finite-window construction and convergence bridge are the closest possible predecessor.

For the **general theorem that a uniformly positive statewise finite-window edge corrector implies finite-seed local convergence**, priority is **unresolved**. The project proof is verified, but Sudbury's 1998 finite-boundary computational method and 1999 "hunting submartingales" paper are methodologically close enough that the exact overlap cannot responsibly be judged from abstracts. The new proof's internal-gap genealogy, corrected-gap contraction, uniform gap tails, spatial compensator, and nonescape argument may be genuinely new, but I cannot call that new without the full Sudbury (1999) text or an expert who knows it closely.

I found no accessible theorem that makes the `lambda=1/40` corollary a straightforward consequence of known work. The older accessible statements either retain a positive parameter restriction, assume translation-invariant initial laws, give only stationary/invariance inputs, or concern a different annihilating-branching model.

## 1. Search scope and terminology

I searched specifically for both possible novelty failures:

1. a theorem already proving deterministic finite-seed one-dimensional BABP convergence below `0.0347`;
2. a general theorem whose hypotheses are automatically satisfied by `BABP-EDGE-001`, making `BABP-CONV-001` a routine corollary.

The search ran through 2026-08-15 and used combinations of the following names and mechanisms:

- `biased annihilating branching process`;
- `biased annihilating process`;
- `annihilating branching process`;
- `branching annihilating process`;
- `branching-annihilating process` and `branching-annihilating random walk`;
- `jumping voter model`;
- `finite particle system`;
- `finite seed`, `finite nonzero initial configuration`, `finite non-null initial configuration`;
- `edge speed`, `front speed`, `interface`, `boundary`, `submartingale`, `edge submartingale`;
- `complete convergence` and `local convergence`;
- `duality`, `quasi-duality`, `thinning`, `double-flipping process`;
- the numerical strings `0.0347`, `0.03461954`, and combinations with `BABP`;
- title/author searches around Neuhauser, Sudbury, Mountford, Lloyd, Martinelli, Shapira, Toninelli, Swart, and later papers citing the historical BABP papers.

I checked the Cambridge records and Crossref citation lists for the 1993 and 1999 papers, the ScienceDirect record for Sudbury (1997), Monash publication records for Sudbury (1998), the Annals/Monash record for Lloyd--Sudbury (1997), the 2025 Martinelli--Shapira--Toninelli preprint, 2024--2026 papers returned by alternate-term searches, and the 2026 Cambridge book *A Course in Interacting Particle Systems* as a recent reference/citation-chain check. I also searched for papers citing Sudbury (1999) and for recent work using generic `annihilating branching process` terminology.

This is a serious targeted search, not an exhaustive bibliometric proof of absence. In particular, Google Scholar-style citation graphs can contain records not exposed by Crossref or ordinary web indexing.

## 2. Closest same-model predecessors

### 2.1 Neuhauser--Sudbury (1993), *The biased annihilating branching process*

This is the model-defining source. Its accessible Cambridge abstract uses the same normalization in words: offspring are placed on empty neighboring sites at rate `lambda` and neighboring particles kill/coalesce at rate `1`. It identifies Bernoulli product equilibrium of density

$$
\frac{\lambda}{1+\lambda}
$$

and the empty state as the stationary laws in one dimension. It also contains the original one-dimensional spreading/convergence theory in a restricted parameter regime.

What it contributes relative to the project theorem:

- **statewise finite-window corrector hypothesis:** not visible in the accessible source record;
- **outer-edge/spreading input:** yes, in the historical restricted regime;
- **local internal-gap/nonescape argument:** not established from the accessible record;
- **below-0.0347 finite-seed theorem:** no;
- **stationary-law classification:** yes, historical source for the classification used later by Martinelli--Shapira--Toninelli.

It does not make the `lambda=1/40` result an accessible corollary.

### 2.2 Mountford (1993), *A coupling of finite particle systems*

The published Cambridge abstract says that for a large class of one-dimensional IPS started from a finite configuration, every subsequential limit measure along times tending to infinity is invariant. It then applies this to one-dimensional BABP with parameter `>1/3`, for finite non-null initial configurations, to obtain convergence to the upper invariant law.

This is very close to the **last step** of the project proof, but it is not the new noescape input. In the verified project proof the same logical role is now filled by Jahnel--Köppl (2026), whose full theorem was directly checked.

What Mountford contributes:

- **statewise corrector hypothesis:** not indicated by the abstract;
- **outer-edge speed:** not the advertised theorem;
- **stationary subsequential limits:** yes;
- **finite-seed convergence:** yes, but only in the then-known `lambda>1/3` range;
- **local gap/nonescape bridge from an edge corrector:** not source-verified.

**Source limitation:** I could obtain the published abstract and bibliographic record but not the full paper body. I therefore do not claim a line-by-line comparison of Mountford's coupling hypotheses or proof with the present gap argument.

### 2.3 Sudbury (1997), *The convergence of the biased annihilating branching process and the double-flipping process in Z^d*

The ScienceDirect abstract is unambiguous about the initial-law scope: the convergence theorem assumes the **initial measure is translation-invariant**. In that setting finite-range stochastic Ising systems with zero flip rates converge, and BABP converges to a mixture of the product law and the empty state. The method is relative entropy.

This does not contain the deterministic finite-seed theorem: a finite deterministic configuration on `Z` is not translation-invariant. It is important stationary/ergodic background, but it is not a simple-rescaling route around the finite-seed obstruction.

Classification for the audit:

- **statewise corrector:** no evidence;
- **outer-edge speed:** no;
- **local noescape/gap:** no, at least not in the theorem advertised by the abstract;
- **initial law:** translation-invariant, hence different from the project theorem;
- **method:** relative entropy, genuinely different.

### 2.4 Lloyd--Sudbury (1997), quasi-duality and thinnings

The paper develops quasi-duality and thinning relations between interacting particle systems. Martinelli--Shapira--Toninelli explicitly credit these ideas as antecedents for the modern BABP--DFP arguments in their Section 5.

I found no statement in the accessible metadata or in the 2025 paper saying that this quasi-duality yields deterministic finite-seed BABP convergence below `0.0347`. Martinelli--Shapira--Toninelli have this toolkit available and still state the finite-seed restriction in Remark 5.4. Therefore quasi-duality is related structure, not an accessible theorem subsuming `BABP-CONV-001`.

### 2.5 Sudbury (1998), *A method for finding bounds on critical values for non-attractive interacting particle systems*

This source matters mainly for **methodological priority**. The indexed bibliographic record confirms the paper. An accessible abstract reproduction describes a computer-assisted method that searches for a function with a sign-definite expected drift by enumerating all relevant `0/1` configurations near the boundary of a finite one-dimensional process. It applies the method to a branching-annihilating random walk and to contact-process bounds.

That description is plainly close in spirit to the present finite-window LP/corrector construction. It does **not**, from the material I could inspect, state the present BABP `lambda=1/40` result or the general statewise-corrector-to-convergence theorem.

For priority language, however, this paper means that we should not describe the finite-window computational device itself as a new general methodology. The safe contribution is the exact new certificate/range plus the verified convergence bridge, not "introducing" boundary correctors or finite-state drift searches.

**Source limitation:** I verified the primary bibliographic record but not the full article body; the detailed method description available to me came through an indexed abstract reproduction rather than a line-by-line primary-text inspection.

### 2.6 Sudbury (1999), *Hunting submartingales in the jumping voter model and the biased annihilating branching process*

This is the closest prior theorem and the main unresolved priority interface.

The Cambridge primary abstract states that for one-dimensional BABP started from a finite nonzero initial configuration, the previous convergence result is extended from `lambda >= 1/3` to

$$
\lambda\ge0.0347,
$$

and that bounds on the edge speed are obtained. The paper is explicitly organized around hunting submartingales.

The independent project audit has calibrated the present finite-window LP against the historical numbers without assuming identity:

- at window size `k=1`, strict feasibility occurs exactly for `lambda>1/3`;
- a fresh `k=8` implementation has zero crossing

$$
0.0346195434755\ldots,
$$

which rounds to the published `0.0347` scale;
- at `k=10`, the project obtains strict positive drift at `lambda=1/40`.

This is strong evidence that the current corrector family is closely related to the historical submartingale machinery. It is **not** source verification that Sudbury used the identical LP, the identical window convention, or literally an eight-site window.

Most importantly for the current writeup, I could not obtain the full article body legitimately through the available web interfaces. Cambridge exposes the abstract, references, and access page, but the nominal PDF route redirects to the access page. Therefore I cannot answer from source whether Sudbury already proves a theorem of the form

> statewise positive finite-window edge drift implies finite-seed local convergence,

nor whether his convergence bridge uses an internal-gap argument equivalent to ours.

This prevents a strong priority claim for the **general criterion**, even though it does not undermine the mathematical result.

### 2.7 Martinelli--Shapira--Toninelli (2025)

This is the strongest current state-of-the-art source I found and the main evidence that the concrete parameter improvement is real.

Their Section 5 revisits BABP using self-duality, quasi-duality with DFP, and a new all-parameter exponential-ergodicity result for DFP. They derive all-parameter BABP structural consequences, including linear growth from finite nonempty sets, and convergence from suitable Bernoulli product initial laws. Nevertheless, their Remark 5.4 still records deterministic finite-seed BABP convergence only in the historical range `lambda>0.0347`, citing Mountford and Sudbury.

This distinction is load-bearing:

- **DFP exponential ergodicity:** all parameters, but for the auxiliary process;
- **BABP linear growth from finite seeds:** all parameters, but does not control local holes;
- **BABP convergence from product initial laws:** all parameters in the stated product-law setting;
- **BABP convergence from a finite deterministic nonempty seed:** still recorded only for `lambda>0.0347`.

The project proof does not use the 2025 particle-number growth theorem. It instead obtains a target-level nonescape estimate from the statewise corrector.

Their convention must be translated explicitly in the manuscript. They use complementary infection variables with infection density `q` and `p=1-q`; for BABP their constraint is the number of particle neighbors. In project particle variables,

$$
\lambda=\frac qp,
\qquad
L_{\mathrm{project}}=p^{-1}L_{\mathrm{MST}}.
$$

This scalar time change preserves stationary laws.

## 3. Successor and alternate-model checks

### 3.1 Papers citing Sudbury (1999)

The Cambridge/Crossref cited-by list exposed only four records: Sudbury (2001) on critical infection bounds, Steif--Sudbury (2006) on a catalytic model, Sun--Swart (2008) on the Brownian net, and Maillard--Penington (2024) on branching random walk with non-local competition. None is a same-model theorem superseding the `0.0347` finite-seed range.

Crossref citation lists are incomplete, so I did not treat this as an exhaustive successor check. I separately searched the exact title, model name, threshold, author names, and the 2025 progress paper through 2026-08-15. I found no later same-target theorem.

The 2026 Cambridge book *A Course in Interacting Particle Systems* still cites Sudbury (1997), Sudbury (1999), and Lloyd--Sudbury in its current reference apparatus. I found no indication in the searchable book record of a new finite-seed BABP theorem or a lower threshold. This is supporting evidence only, not a substitute for a citation-index audit.

### 3.2 `Branching-annihilating random walk` is dangerously ambiguous

Several recent papers returned by alternate terminology concern different processes and do not subsume this BABP.

Birkner--Callegaro--Cerny--Gantert--Oswald (2024), *Survival and complete convergence for a branching annihilating random walk*, studies a discrete-time BARW with offspring/jump and annihilation rules different from the present nearest-neighbor BABP generator. Its "complete convergence" title is therefore a false positive for this audit.

Latz--Swart (2022/2023) use `annihilating branching process` for what they rebrand the **cancellative contact process**, a process with contact-type infection modulo two and an independent death mechanism. That is also not the present BABP, whose death/coalescence rate is generated by occupied neighbors.

Older `branching annihilating process` and parity-preserving BARW terminology similarly contains models with diffusion, double offspring, or parity constraints. A result for those models cannot be imported merely from the common words `branching` and `annihilating`.

### 3.3 Later duality and general-IPS literature

Modern duality papers and the 2026 Swart text contain useful general theory and historical references, but I found no theorem whose hypotheses transparently turn `BABP-EDGE-001` into deterministic finite-seed convergence at `lambda=1/40`. The verified project bridge is therefore not presently identifiable as a routine corollary of a generic complete-convergence theorem.

Jahnel--Köppl (2026) does make one piece routine in a modern way: every weak subsequential limit is stationary under hypotheses directly satisfied by BABP. That theorem replaces reliance on uninspected historical stationary-limit arguments, but it does not prove that the stationary limit has no empty component. The new gap/nonescape estimate is still needed.

## 4. Exact status of the older unavailable sources

These limitations should be stated in the manuscript preparation record rather than hidden.

### Mountford (1993)

Available: published abstract and bibliographic record.

Verified from that abstract: a general one-dimensional finite-particle stationary-limit principle and its application to finite non-null BABP for parameter `>1/3`.

Not verified from source: exact hypotheses, exact coupling construction, or any finer relationship to the current internal-gap proof.

### Ramírez--Varadhan (1996)

Available: bibliographic records, author bibliography, and Project Euclid identifier.

The Project Euclid body was not obtainable through the available interface. I therefore have **not** independently checked its theorem statements or hypotheses line by line. The project theorem does not need it because Jahnel--Köppl (2026) supplies the required stationary-limit statement from an accessible current source.

### Sudbury (1999)

Available: Cambridge abstract, references, bibliographic metadata, citation list, and DOI.

Verified directly: finite-seed convergence extended to the `0.0347` range and edge-speed bounds; submartingale is central enough to appear in the title and keywords.

Not verified: the internal finite-window calculation, the precise corrector state space, exact normalization, literal window size, or the convergence bridge from the hunted submartingale to local convergence.

Accordingly, the project's identification of the historical threshold mechanism is **numerically calibrated rather than source-verified**: exact `k=1` reproduction of the old `1/3` threshold and independent `k=8` crossing at `0.0346195434755...` strongly indicate the connection, but they do not substitute for the text of Sudbury's proof.

This is the single most important remaining literature issue before submission-level priority confidence.

## 5. Does accessible prior work already imply the project theorem?

I found no such implication.

A decomposition of the required logic makes the point clear. From a statewise corrector the project proves:

1. two-sided outer-edge linear motion;
2. the same corrector applied to the two particle populations bordering **every internal gap** gives a corrected gap with uniformly negative drift;
3. after localization, exponential tilting yields uniform gap lifetime and maximum-width tails;
4. Poisson endpoint displacement plus a spatially truncated compensator and monotone convergence control gaps nucleated anywhere in space;
5. this gives a uniform no-escape estimate for fixed windows;
6. a stationary-limit theorem plus stationary-law classification then forces the Bernoulli component and excludes the empty state.

Accessible earlier theorems supply pieces of step 6 and, in restricted regimes, some form of step 1. Sudbury (1997) treats different initial laws. Martinelli--Shapira--Toninelli (2025) supplies strong all-parameter global growth but still records the finite-seed gap. None of the accessible statements supplies steps 2--5 under the statewise corrector hypothesis.

Thus the concrete `lambda=1/40` theorem is not an **accessible straightforward corollary** of the literature I found. The unresolved caveat is whether Sudbury (1999) already contains essentially steps 2--5 in its body.

## 6. Recommended manuscript packaging

I recommend a **staged approach**:

1. prepare a complete short standalone note now, centered on the general statewise-corrector criterion and the exact `lambda=1/40` certificate;
2. continue the all-parameter front programme separately;
3. if the front-gap problem is later solved, either enlarge the note before submission if timing and exposition remain clean, or publish the strengthening separately.

Do not hold a complete verified finite-seed improvement indefinitely for E5. The present result has a coherent proof mechanism and a concrete below-recorded-range corollary. Conversely, do not inflate it into a broad BABP paper before the all-parameter argument exists.

A suitable working title is:

> **Finite-window edge correctors and finite-seed convergence for the one-dimensional biased annihilating branching process**

The note can be short because the logical spine is narrow.

### Proposed structure

#### 1. Introduction

- define the exact finite-seed question;
- state that Sudbury (1999) proves convergence in the `0.0347` range and that Martinelli--Shapira--Toninelli (2025), Remark 5.4, still records that range;
- state the general statewise-corrector theorem and `lambda=1/40` corollary;
- explicitly avoid a priority adjective pending the final historical audit.

#### 2. BABP and finite-window edge correctors

State the project convention:

$$
0\to1\text{ at rate }\lambda N_x,
\qquad
1\to0\text{ at rate }N_x.
$$

Give the exact edge-window generator. For right edge `R`, word `u=(u_1,\ldots,u_k)`, exterior bit `z`, set `u_0=1`, `u_{k+1}=z`,

$$
T_+u=(1,u_1,\ldots,u_{k-1}),
$$

$$
T_-^zu=(u_2,\ldots,u_k,z),
$$

and let `u^(j)` flip the `j`th bit. Then

$$
\begin{aligned}
D_{k,\lambda}(u,z;\phi)
={}&\lambda\left[1+\phi(T_+u)-\phi(u)\right]\\
&+u_1\left[-1+\phi(T_-^zu)-\phi(u)\right]\\
&+\sum_{j=1}^k
(u_{j-1}+u_{j+1})\bigl[\lambda(1-u_j)+u_j\bigr]
\left[\phi(u^{(j)})-\phi(u)\right].
\end{aligned}
$$

State the statewise hypothesis and prove the basic outer-edge consequence by the bounded-jump martingale decomposition.

#### 3. Exact rational certificate at `lambda=1/40`

State the `k=10` certificate, exact minimum

$$
\frac{1033}{40000000},
$$

and the verification format. The full 1024-entry rational vector is better supplied as machine-readable supplementary material than typeset in the body. Include an exact checksum or reproducibility statement and independently useful calibrations:

- `k=1` threshold exactly `lambda>1/3`;
- `k=8` numerical crossing `0.0346195434755...` as historical calibration, explicitly **not** as a claim about Sudbury's literal internal window.

#### 4. Statewise edge corrector contracts internal gaps

Give the gap genealogy first: new positive gaps are born at width one, positive gaps do not split, and two positive gaps cannot merge while both live.

For a tagged gap between particle populations `A` and `C`, define

$$
Z=H_L(C)-H_R(A)-1.
$$

Prove the uniform drift `L Z <= -2v` before closure and record `g-2||phi||_infty <= Z <= g+2||phi||_infty`.

#### 5. Uniform gap tails and the all-space nucleation sum

This section must visibly include Review A's two rigor repairs.

First localize `exp(theta Z)`: stop when the gap width or `Z` reaches a finite level, apply Dynkin/optional stopping to the bounded stopped process, and only then remove the localization. Derive uniform exponential lifetime and width tails.

Then dominate endpoint displacement by a Poisson process of rate `2(1+lambda)` and sum over new gap nucleations. **First truncate the spatial compensator to `|x|<=N`; only after obtaining the finite sum pass to `N->infinity` by monotone convergence.** This should be written in the main proof, not left as a footnote.

#### 6. Nonescape and local convergence

Use the two outer edges plus the large-gap estimate to prove

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

Then invoke Jahnel--Köppl for stationarity of weak limits and Martinelli--Shapira--Toninelli for the one-dimensional stationary-law classification. State the convention conversion at the point of citation:

$$
\lambda=\frac qp,
\qquad
L_{\mathrm{project}}=p^{-1}L_{\mathrm{MST}}.
$$

The empty-window estimate forces the coefficient of `delta_empty` to vanish.

#### 7. Discussion

- explain that the hypothesis is statewise and stronger than a bare ballistic-edge statement;
- make no convergence-rate claim;
- mention the open all-parameter positive-corrector/front problem;
- discuss the relation to Sudbury's submartingale method conservatively until his proof has been inspected.

## 7. Safe novelty language

### Safe now

The following wording is supported by the verified mathematics plus the current literature audit:

> We construct an exact rational ten-site edge corrector for one-dimensional BABP at `lambda=1/40` and prove that any uniformly positive statewise finite-window edge corrector implies local convergence from every finite nonempty deterministic initial configuration. Consequently BABP at `lambda=1/40` converges locally to Bernoulli equilibrium. The parameter `1/40=0.025` lies below the `lambda>0.0347` finite-seed range recorded by Martinelli--Shapira--Toninelli (2025, Remark 5.4).

Also safe:

> We found no later theorem in our search through 2026-08-15 that removes the `0.0347` finite-seed restriction.

provided it is presented as a literature-search statement rather than mathematical proof of priority.

### Not safe yet

Do not presently write:

- "the first improvement since Sudbury";
- "the best known finite-seed threshold";
- "the first proof below `0.0347`";
- "Sudbury used exactly the same eight-site LP";
- "our corrector-to-convergence theorem is new";
- "positive edge speed implies convergence".

The first five require stronger source/priority checking; the last is mathematically stronger than the verified theorem.

## 8. Recommended final literature check before submission

The remaining check is narrow enough to give to a fresh specialist rather than repeat a broad search.

Ask the specialist to obtain and read the full bodies of:

1. Sudbury (1999), especially the BABP theorem, finite-boundary/submartingale construction, and convergence bridge;
2. Sudbury (1998), to determine exactly which finite-window/corrector formalism is already stated there;
3. Mountford (1993), only to clarify historical provenance of the stationary-limit bridge, not because the project proof depends on it;
4. Ramírez--Varadhan (1996), likewise for provenance if the manuscript discusses the older stationary-limit literature.

The specialist's key comparison question should be:

> Does Sudbury (1999), perhaps together with Mountford (1993), already state or prove that a uniformly positive **statewise finite-window** edge submartingale/corrector yields deterministic finite-seed local convergence, including control of internal holes/gaps? If yes, which exact hypotheses and theorem numbers, and does the present `k=10`, `lambda=1/40` certificate plug into them without new argument?

If the answer is yes, package the project contribution as a new exact certificate/range extension under an existing convergence bridge. If the answer is no, the current verified internal-gap bridge is a stronger candidate for a separate theorem-level novelty claim.

## Handoff to Professor

**Closest prior theorem found:** Sudbury (1999), finite nonzero initial configuration, convergence to Bernoulli equilibrium in the `lambda>=0.0347` range, with edge-speed bounds and submartingale methodology.

**Novelty status:** concrete convergence at `lambda=1/40`: **strongly supported** as below the range recorded in the current 2025 progress paper, with no successor below `0.0347` found through 2026-08-15. Priority of the general statewise-corrector-to-convergence criterion: **unresolved** because the body of Sudbury (1999) was not obtainable for exact comparison.

**Recommended paper scope:** staged short standalone note now: general verified corrector criterion + exact `lambda=1/40`, `k=10` certificate/corollary. Do not wait for the all-parameter front-gap programme, but keep E5 out of the main theorem unless it is completed in time.

**Exact literature issue requiring fresh specialist audit:** full-text comparison with Sudbury (1999), with Sudbury (1998) as methodological predecessor. Mountford (1993) and Ramírez--Varadhan (1996) also remain not line-by-line source-verified, but the theorem itself no longer depends on them because Jahnel--Köppl (2026) supplies the stationary-limit input directly.
