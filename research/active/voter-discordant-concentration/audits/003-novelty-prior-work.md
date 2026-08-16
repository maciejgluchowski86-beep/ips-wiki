# Independent audit 003: novelty and closest prior work for `VOTER-CONC-001`

Date: 2026-08-16

Role: independent novelty / closest-prior-work auditor. I did not participate in development of the claim or in its correctness reviews. I treat the Professor reconstruction and the two hostile correctness reviews only as evidence that the project mathematics is correct; they are not evidence of novelty.

## Executive verdict

The central contribution claim does **not** survive the closest-prior-work audit under the project's standing novelty standard.

The fatal comparison is with the target source itself:

> Luca Avena, Rangel Baldasso, Rajat Subhra Hazra, Frank den Hollander, Matteo Quattropani, *Discordant edges for the voter model on regular random graphs*, ALEA 21 (2024), 431--464, DOI `10.30757/ALEA.v21-18`, arXiv:`2209.01037v2`.

Avena et al. already prove in the argument for Proposition 4.1, equation (4.2), the relevant **two-edge decoupling on the event of no cross-family interaction**. In Section 5 they define the four-endpoint cross-family interaction time in (5.5) and prove in (5.6)

$$
\mathbf P_{\nu\otimes\nu}^{G}(\tau^{e,f}\le t)
\le 4\mathbf P_{\pi\otimes\pi}^{G}(\tau_{\rm meet}\le t).
\tag{A}
$$

For Bernoulli initial opinions, the same no-interaction argument gives immediately, for the discordance indicators `X_e,X_f` of two edges,

$$
\operatorname{Cov}_u^G(X_e,X_f)
\le \mathbf P^G(\tau^{e,f}\le t).
\tag{B}
$$

Averaging (B) over the ordered pair of uniform edges and applying (A) gives the deterministic inequality

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_t)
\le 4\mathbf P_{\pi\otimes\pi}^{G}(\tau_{\rm meet}\le t).
}
\tag{C}
$$

This is the same deterministic reduction as the project theorem up to the numerical constant `4` in place of `2`. It immediately combines with the meeting estimate already used by Avena et al., in particular their (5.8), to give

$$
\operatorname{Var}_u^G(\mathcal D_{t_n})
=O_{\mathbb P}((1+t_n)/n)
$$

for deterministic `t_n=o(n)`, and `O_P(t_n/n)` for `1<=t_n=o(n)`, hence both of the project's random-regular concentration conclusions by Chebyshev.

Avena et al. did **not** state this corollary. Indeed they state the sharper scale in (1.9) as beyond their reach. Nevertheless, under the standing novelty rule, the project cannot count as a new theorem merely because it notices the corollary, improves the deterministic constant from `4` to `2`, and supplies a more elegant quotient-genealogy proof. The structural reduction to a two-walk meeting probability is already implicit in the source's printed decoupling and interaction estimates.

The small-time counterexample to literal (1.9) is a separate issue. I found no accessible source pointing it out, and the displayed quantifiers in (1.9) genuinely include arbitrarily small positive times. However, one highly relevant 2025 source, Federico Capannoli's PhD thesis *Opinion Dynamics on Random Graphs*, could not be obtained in full because the Leiden Repository returned HTTP 403. I therefore classify priority of that correction as unresolved rather than claim novelty.

### Required classifications

| Component | Classification | Reason |
|---|---|---|
| 1. Deterministic inequality | **prior art / immediate corollary of prior work** | Avena et al. (2024), Proposition 4.1 proof (4.2) + (5.5)--(5.6), gives the same meeting-probability reduction with constant `4`; the project improves the constant to `2`. |
| 2. Random-regular corrected concentration theorem | **prior art / immediate corollary of prior work** | Combine the preceding factor-`4` deterministic bound with source (5.8) and Chebyshev. |
| 3. Source-scale theorem for `1<=t_n=o(n)` | **prior art / immediate corollary of prior work** | Same combination, using the source's `q_t=O_P(t/n)` regime. |
| 4. Small-time correction of literal (1.9) | **priority unresolved** | Literal falsity is real and no accessible correction was found, but Capannoli's 2025 thesis is highly relevant and its full text was not accessible. |

### Overall recommendation for `VOTER-CONC-001`

**`verified mathematics but not a new project result`**.

The factor-`2` theorem and genealogy-conditioned quotient-cut proof remain correct technical mathematics and may be useful as a sharper, cleaner proof. They should not be framed as resolving an open concentration problem by a new theorem mechanism. The small-time correction may be recorded separately as a source correction/observation pending a complete priority check, but it is not enough to rescue the central package as a substantive project result.

---

## 1. Exact closest-prior-work comparison

### 1.1 Source ingredients

I checked the version matching publication, arXiv:`2209.01037v2` (11 April 2024) and the ALEA bibliographic record.

The following source facts are load-bearing.

1. **Classical duality.** Section 2 builds the voter model from Harris arrows and states the dual system of coalescing random walks. A backward lineage is a rate-one continuous-time simple random walk; distinct lineages are independent until they meet and then coalesce.

2. **Two-edge no-interaction decoupling.** In the proof of Proposition 4.1, the source fixes two edges `e=(x,y)` and `e'=(x',y')` and defines the event that none of the two endpoint walks from the first edge interacts with either endpoint walk from the second before time `t`. Equation (4.2) proves, by an explicit path summation, a negative-dependence upper bound for simultaneous discordance on this no-interaction event. The later geometry in Proposition 4.1 is used to show that the interaction complement is unlikely; the decoupling inequality itself is the local probabilistic ingredient relevant here.

3. **Four-endpoint interaction.** In Section 5, equation (5.5) defines for two sampled oriented edges the interaction time as the minimum of the four cross meeting times between their endpoint walks.

4. **Reduction to stationary two-walk meeting.** Equation (5.6) proves

$$
\mathbf P_{\nu\otimes\nu}^{G}(\tau^{e_1,e_2}\le t)
\le
4\mathbf P_{\pi\otimes\pi}^{G}(\tau_{\rm meet}\le t)
$$

by the fact that both marginals of the uniform oriented-edge law `nu` are `pi` and a union bound over the four cross pairs.

5. **Short-time meeting estimate.** Equations (5.7)--(5.8) control the stationary meeting probability on random regular graphs. The bare `(5.7)` wording `O(t/n)` cannot be uniform to `t=0` because the two stationary starts coincide with probability `1/n`; the Aldous--Brown estimate quoted as (5.8), together with the high-probability `Theta(n)` stationary mean meeting time and spectral-gap input used in the paper, gives the stable bound

$$
q_t^G:=\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)
=O_{\mathbb P}((1+t)/n)
$$

along deterministic `t=o(n)`, and `O_P(t/n)` when `t>=1`.

The project correctness reviews independently noticed the same small-time qualification to (5.7); it is not relevant to novelty of the factor-`4` reduction.

### 1.2 The immediate factor-4 deterministic theorem

Here is the short corollary of the source ingredients, written explicitly because this is the decisive novelty point.

Fix a finite simple `d`-regular graph and i.i.d. Bernoulli(`u`) initial opinions. Let

$$
X_e(t)=\mathbf 1_{\{e\text{ is discordant at time }t\}}
$$

for an unoriented edge `e`. For two edges `e,f`, realize their four endpoint genealogies by four independent random-walk paths, with the usual coalescing identification within each voter genealogy. Let

$$
H_{e,f}(t)
=
\{\text{some endpoint path from }e\text{ meets some endpoint path from }f
\text{ by time }t\}.
$$

This is the event in source (5.5), up to orientation, which is irrelevant to `H_{e,f}`.

On `H_{e,f}(t)^c`, the two ancestral families use disjoint initial Bernoulli labels. Conditional on the four paths:

- if the two endpoint lineages of `e` have already coalesced then `X_e(t)=0`;
- otherwise `X_e(t)=1` with probability `p=2u(1-u)`;
- the same holds for `f`;
- because the two families have disjoint ancestors, their Bernoulli-label events are independent.

Thus, if `M_e` and `M_f` denote the within-edge meeting times of the two independent raw path families,

$$
\begin{aligned}
\mathbf P_u^G(X_e=X_f=1,H_{e,f}^c)
&=p^2\mathbf P(M_e>t,M_f>t,H_{e,f}^c)\\
&\le p^2\mathbf P(M_e>t)\mathbf P(M_f>t)\\
&=\mathbf P_u^G(X_e=1)\mathbf P_u^G(X_f=1).
\end{aligned}
\tag{1.1}
$$

The inequality is exactly the Bernoulli-initial analogue of the source's Proposition 4.1 / equation (4.2) decoupling. Adding back the interaction event gives

$$
\operatorname{Cov}_u^G(X_e,X_f)
\le \mathbf P^G(H_{e,f}(t)).
\tag{1.2}
$$

No absolute covariance bound is needed: summing the upper bounds is sufficient for the variance.

Let `m=dn/2`. Since

$$
\mathcal D_t=m^{-1}\sum_{e\in E}X_e(t),
$$

we have

$$
\begin{aligned}
\operatorname{Var}_u^G(\mathcal D_t)
&=\frac1{m^2}\sum_{e,f\in E}\operatorname{Cov}(X_e,X_f)\\
&\le\frac1{m^2}\sum_{e,f\in E}\mathbf P^G(H_{e,f}(t))\\
&=\mathbf P_{\nu\otimes\nu}^G(\tau^{e,f}\le t)\\
&\le4\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
\end{aligned}
\tag{1.3}
$$

The orientation step is harmless because `H_{e,f}` is invariant under reversing either sampled edge. If `e=f` or the edges share a vertex, the source convention declares cross interaction at time zero, so (1.2) is trivially valid there.

Equation (1.3) is qualitative/theorem-level equivalent to the project's

$$
\operatorname{Var}_u^G(\mathcal D_t)\le2q_t.
$$

The project's extra achievements relative to (1.3) are:

- the numerical factor `2` instead of `4`;
- an exact law-of-total-variance decomposition through the full Harris genealogy;
- the quotient-multigraph random-cut representation;
- a clean cluster-square identity for the conditional variance;
- a separate four-family estimate for the variance of the conditional mean.

I did not find that exact factor `2` or that exact quotient-cut proof in the audited literature. But the standing novelty standard explicitly excludes a result whose theorem-level advance is only a better constant within an already available arbitrary-graph mechanism. The reduction `Var(discordance) <= C * stationary meeting probability` is already an immediate source corollary.

### 1.3 Earliest date I can support

The arXiv record dates version 1 of Avena et al. to 2 September 2022 and version 2 to 11 April 2024; version 2 matches the published paper. I directly checked the relevant proposition/equations only in the publication-matching version. I did **not** obtain a version-specific full text establishing that both (4.2) and (5.6) were already present in v1. Therefore the earliest exact priority date I claim for the fatal combination is the checked 2024 version/publication, not September 2022.

---

## 2. Component 1: deterministic inequality

### Classification

**`prior art / immediate corollary of prior work`**.

This classification applies under the project's standing novelty standard, not because the exact displayed constant `2` was found verbatim. The closest source gives the same theorem architecture with constant `4` after the short derivation above.

The extension from the source's connected random-regular setting to arbitrary finite regular graphs, including disconnected graphs and degrees `d=1,2`, does not alter the argument: the oriented-edge marginals are still uniform on a regular graph and walks in different components simply never meet. This is a routine hypothesis extension, not a structural contribution.

### Older conceptual prior work checked

I also searched older voter/coalescence literature so as not to mistake classical genealogy for novelty.

- **Aldous--Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 14.3.** The graphical voter/coalescing-walk construction on finite regular graphs and the induced partition into ancestral/opinion clusters are classical. Section 14.3.4 treats the partition-valued voter process and quantities built from cluster squares and boundaries. I did not locate the discordant-edge variance-to-meeting inequality there.

- **Chen--Choi--Cox, *On the convergence of densities of finite voter models to the Wright--Fisher diffusion* (2016; arXiv:1311.5786).** This work treats the discordant oriented-pair density `p_{10}` as the predictable quadratic-variation density of the voter density and uses two- and four-walk conditions. It contains dual formulas for expectations and moment/integral controls, but I did not locate the fixed-time variance bound for the discordant-edge density that is at issue here.

- **Steif--Tykesson, *Generalized Divide and Color models* (2017).** The random-partition-plus-independent-block-coloring viewpoint is established in generality and includes voter-related examples. I did not locate a quotient-cut variance theorem implying the claimed inequality.

These sources show that the genealogy and random cluster coloring are classical. They are not the fatal sources. The fatal source is Avena et al. itself because it already contains the edge-pair no-interaction covariance mechanism and the averaged four-walk interaction estimate needed for (1.3).

---

## 3. Component 2: corrected all-sublinear random-regular concentration

### Classification

**`prior art / immediate corollary of prior work`**.

From (1.3), for a uniformly random simple fixed-`d>=3` regular graph,

$$
\operatorname{Var}_u^G(\mathcal D_{t_n})\le4q_{t_n}^G.
$$

Avena et al. (5.8), with the same mean-meeting-time and spectral-gap inputs they invoke, yields along every deterministic `t_n=o(n)`

$$
q_{t_n}^G=O_{\mathbb P}((1+t_n)/n).
$$

Therefore

$$
\operatorname{Var}_u^G(\mathcal D_{t_n})
=O_{\mathbb P}((1+t_n)/n),
$$

and Chebyshev gives, for every deterministic `C_n\to\infty`,

$$
\mathbf P_u^G\left(
|\mathcal D_{t_n}-\mathbf E_u^G\mathcal D_{t_n}|
>C_n\sqrt{(1+t_n)/n}
\right)
\xrightarrow{\mathbb P}0.
$$

Thus the corrected concentration theorem does not require the project's factor `2`, quotient-cut representation, or its new proof. It follows from the source's own printed ingredients with a constant `4` that disappears at the `O_P`/Chebyshev level.

This is particularly important because Avena et al. themselves did not make this combination and state their sharper proposed scale as beyond reach. The fact that the authors missed a short consequence of their own estimates does not make the consequence new under the project's pre-committed standard: the ingredients already encode it directly.

---

## 4. Component 3: source scale for deterministic `1<=t_n=o(n)`

### Classification

**`prior art / immediate corollary of prior work`**.

For `t_n>=1`, the source meeting estimate gives

$$
q_{t_n}^G=O_{\mathbb P}(t_n/n).
$$

Combining with the factor-`4` bound (1.3),

$$
\operatorname{Var}_u^G(\mathcal D_{t_n})=O_{\mathbb P}(t_n/n).
$$

Chebyshev then gives exactly the proposed shrinking scale

$$
C_n\sqrt{t_n/n}
$$

for every deterministic `1<=t_n=o(n)` and `C_n\to\infty`.

Therefore the theorem in the regime in which the source scaling is mathematically sensible is already a short corollary of the 2024 paper. It is not rescued by the fact that source equation (1.9) calls this type of strengthening beyond reach.

---

## 5. Component 4: very-small-time correction to literal (1.9)

### Mathematical/source judgment

The literal displayed statement is false.

Avena et al. Section 1.4 says, in (1.9), that for every sequence `t_n` with

$$
t_n/n\to0
$$

and every `C_n\to\infty`, the deviation scale is

$$
C_n\sqrt{t_n/n}.
$$

The displayed statement does not add `t_n\to\infty`, `t_n>=1`, or `\inf_n t_n>0`. The surrounding prose presents (1.9) as a desired sharpening and says it is beyond reach; I found no sentence restricting the displayed quantifier to a lower-time regime.

At time zero, for Bernoulli(`u`) initial data on any fixed-degree regular graph,

$$
\operatorname{Var}(\mathcal D_0)=\Theta(1/n)
$$

for every `u\in(0,1)`. Taking

$$
t_n=n^{-3},\qquad C_n=\log n
$$

makes the proposed threshold

$$
C_n\sqrt{t_n/n}=\frac{\log n}{n^2}=o(n^{-1/2}),
$$

while with probability tending to one no voter clock rings before `t_n`; the initial `n^{-1/2}` fluctuation therefore survives. The project's counterexample is a genuine correction of the literal quantifiers.

### Priority classification

**`priority unresolved`**.

I found no accessible erratum, later arXiv version, paper, or review that records this small-time correction. The arXiv page shows v2 (11 April 2024) as the publication-matching latest version, with no later version. Den Hollander's 2025 open-access review *Evolution of Discordance* restates the static random-regular results but I did not find this correction there.

However, Federico Capannoli's 2025 Leiden PhD thesis *Opinion Dynamics on Random Graphs* is highly relevant: Chapter 3 is devoted to discordant edges and the thesis supervisors include Frank den Hollander, Rajat Hazra, and Luca Avena. The Leiden landing page was accessible, but the repository handle `1887/4283502` returned HTTP 403, so I could not inspect the thesis text. Under the assignment's source-discipline rule, I therefore do not certify priority for the small-time correction.

Even if later inspection establishes that the counterexample is new, its role should be described narrowly: it is a literal quantifier/source correction and identifies the missing initial `n^{-1/2}` scale. It is not the difficult sharp-concentration theorem the source intended to pose.

---

## 6. Successor and citation-chain search

I searched through 2026-08-16 for successor work resolving or restating the static random-regular sharp concentration problem.

### Sources checked

1. **Federico Capannoli, *Evolution of discordant edges in the voter model on random sparse digraphs*, EJP 30 (2025), arXiv:2407.06318.** This extends discordant-edge asymptotics to directed configuration models. The accessible source emphasizes asymptotics/expectations and the directed geometry; I found no static random-regular `sqrt(t/n)` concentration theorem superseding the comparison above.

2. **Avena--Baldasso--Hazra--den Hollander--Quattropani, *The voter model on random regular graphs with random rewiring*, arXiv:2501.08703.** This treats a dynamically rewired graph, not the static graph theorem audited here.

3. **F. den Hollander, *Evolution of Discordance*, Mathematical Physics, Analysis and Geometry 28 (2025), Article 21; arXiv:2410.17808.** This is an overview of the area and restates the static random-regular results. I did not find a theorem at the source's proposed shrinking concentration scale or the small-time correction.

4. **Avena--Capannoli--Hazra--Garlaschelli, *Voter model on heterogeneous directed networks*, arXiv:2506.12169.** This concerns heterogeneous directed networks and consensus-time asymptotics, not the static regular sharp concentration theorem.

5. **Capannoli, *Opinion Dynamics on Random Graphs*, Leiden PhD thesis (2025).** Landing page and chapter summary checked; **full text not checked** because the repository returned HTTP 403. This is the main explicit access limitation in the successor audit.

### Citation-index limitation

I also checked bibliographic/citation landing pages and title-based citing searches. The available indexes gave inconsistent citation counts (for example, a university CRIS page reported four Scopus citations while ResearchGate displayed eleven). I therefore do not claim an exhaustive citation graph. The negative novelty verdict does not rely on exhaustion of successors because the fatal prior-art comparison is already the 2024 target source itself.

---

## 7. Alternate-terminology and predecessor searches performed

The assignment required reporting what was searched, not only what was found. I used combinations of the following terminology, with and without `voter model` and `coalescing random walks`:

- `discordant edges`, `disagreeing edges`, `interfaces`, `edge boundary`, `boundary size`, `cut size`, `random cut`;
- `variance`, `covariance`, `concentration`, `second moment`, `Efron--Stein`, `Poincare`;
- `Harris graphical representation`, `ancestral partition`, `genealogy`, `ancestral clusters`, `coalescing random walks`;
- `cluster coloring`, `divide and color`, `quotient graph`, `quotient multigraph`, `weighted cut`;
- `voter polynomial observables`, `two-point function`, `four-walk`, `four lineages`;
- `meeting probability`, `meeting time`, `finite graph voter concentration`;
- exact-title and citation searches for the 2024 Avena et al. paper, including `correction`, `erratum`, `Eq. (1.9)`, `sqrt(t/n)`, and `small time`;
- successor searches for `2024`, `2025`, `2026`, random rewiring, directed configuration models, heterogeneous directed networks, and overview/thesis material.

I also searched generic weighted-cut variance literature for a theorem that would independently subsume the conditional quotient-cut calculation. The results found were generic MaxCut/random-cut concentration papers, not a voter-genealogy theorem tied to meeting probabilities. No stronger fatal source was needed once the Avena self-corollary was identified.

### Sources not obtained / not fully checked

- Capannoli 2025 PhD thesis: landing page checked; full thesis **not checked** due HTTP 403.
- Avena et al. arXiv v1 (September 2022): bibliographic existence checked; I did **not** verify the exact presence of both fatal equations (4.2) and (5.6) in that version, so I do not backdate the exact corollary to v1.
- Proprietary citation databases: not exhaustively available; no claim of complete citation enumeration.

---

## 8. What, if anything, remains new in the project proof?

The audit does not say the project proof is valueless. Relative to the source-immediate factor-`4` theorem, the project supplies:

1. the stronger explicit constant `2`;
2. a genealogy-first law-of-total-variance proof;
3. an exact representation of discordance as a weighted Bernoulli cut on the ancestral quotient multigraph;
4. a cluster-square control of conditional variance;
5. a clean separation between conditional-label noise and genealogical randomness.

I did not find this exact proof in the audited sources. It may be a useful lemma/proof technique to retain, and perhaps worth communicating as a simplification of the existing weak-dependence machinery.

But under this project's standing novelty standard, the theorem-level difference is a constant improvement/new proof of a reduction already implicit in Avena et al. The random-regular concentration consequences do not use the improved constant. Therefore they cannot carry a new project-result claim.

The situation is closely analogous in principle to the BABP precedent: mathematically valid sharpening remains valid, but the source comparison changes contribution status.

---

## 9. Recommended repository/status changes

I recommend that the Professor, not this auditor, make the state/registry edits, with the following substance:

1. Promote correctness separately if the protocol permits, because this novelty audit does not challenge the two hostile correctness `PASS` judgments.
2. Set the research-contribution status of `VOTER-CONC-001` to **not a new project result under the standing novelty standard**.
3. Record Avena et al. (2024), Proposition 4.1 proof (4.2) plus (5.5)--(5.6), as the closest prior work and record the immediate factor-`4` deterministic inequality (1.3) above.
4. Describe the project's `2q_t` theorem as a sharper constant and a new/cleaner proof unless further literature establishes that proof architecture too.
5. Do not claim that the group newly resolves source (1.9) on `1<=t_n=o(n)`: that conclusion is already an immediate corollary of the source ingredients.
6. Keep the tiny-time counterexample as a separate correction with **priority unresolved** until the inaccessible Capannoli thesis or an equivalent complete priority source is checked.

## Final recommendation

**`verified mathematics but not a new project result`**.
