# Student A reconnaissance 001: opportunity cost against BABP

Date: 2026-08-15

## Recommendation

**I recommend replacing provisional BABP with the residual positive-rates problem for simple one-sided one-dimensional IPS, unless Student B has already found a genuinely new small-`lambda` lemma rather than merely reconstructed the historical obstruction.**

The preferred target is:

> Prove that every simple IPS with positive rates is ergodic; more narrowly, settle the remaining noisy-East parameter region left open after Głuchowski--Menz (2025, 2026).

This is not a neutral ranking. On present evidence I put it above BABP. The mathematical reason is not that BABP is unimportant; it is that the positive-rates target has a substantially stronger *group-specific leverage point*. The principal authored the two recent papers that reduce the problem to the noisy-East region, so the group begins with the exact parameter reduction, canonical coupling, time-scaling reduction, simulations, and the wall/long-lived-state mechanism already in hand. The residual obstruction is also sharply described: arbitrarily small positive noise should remove the exceptional East invariant state, but generic noise destroys reversibility and the explicit equilibrium structure used by standard East arguments.

BABP has a clean explicit gap, but the gap has survived since Sudbury's 1999 improvement to `lambda > 0.0347`; Martinelli--Shapira--Toninelli (2025) prove all-parameter DFP exponential ergodicity and all-parameter BABP linear growth and still leave deterministic finite-seed convergence open. That is strong evidence that the remaining local signed-observable problem is not removed by the modern inputs. Student B's audit could change this assessment if it produces a concrete new bridge lemma.

My ranking is:

1. **Residual positive-rates conjecture for simple IPS / noisy East** — replace BABP on present information.
2. **Sharp sublinear-time concentration of voter-model discordant edges on random regular graphs** — mathematically concrete but less group-specific leverage, and the source's literal very-small-time formulation needs care.
3. **Voter-model discordance on undirected heterogeneous configuration models** — important explicit open problem, but substantially more random-environment machinery and less immediate tractability.

I inspected the requested recent source pool: Martinelli--Shapira--Toninelli (2025), Hartarsky--Toninelli (2025), Capannoli--den Hollander (2024), and Ngoc--Schütz (2025), and searched additional 2024--2026 progress/open-problem sources. I do **not** recommend another FA/KCM off-equilibrium target, the open-boundary ASEP integrability problems in Ngoc--Schütz, or the `1<s<=2` long-range-random-graph contact-process problem over the three targets above.

---

## Baseline: BABP finite-seed convergence

The current working target is one-dimensional BABP with branching parameter `lambda>0`, from a finite nonempty seed, converging locally to Bernoulli equilibrium of particle density

$$
q=\frac{\lambda}{1+\lambda}.
$$

Sudbury proved convergence for

$$
\lambda>0.0347,
$$

improving the earlier `lambda>1/3` range. Martinelli--Shapira--Toninelli, Section 5, record the same finite-seed gap after proving two strong all-parameter inputs: exponential ergodicity of the DFP and linear growth of BABP from finite nonempty sets. Their Remark 5.4 still cites `lambda>0.0347` as the finite-seed convergence range.

The current obstruction is unusually clean but severe. BABP self-duality asks for decay, for every fixed finite test set `B'`, of

$$
\mathbf E_B\left[\left(-\frac1\lambda\right)^{|B(t)\cap B'|}\right].
$$

When `lambda<1`, the local kernel has magnitude larger than one on nonempty intersections. Global growth of `|B(t)|` does not control this fixed-window signed quantity. The 2025 DFP theorem controls a different quasi-dual observable. Thus the historical threshold could disappear only if one can convert the new DFP/local-growth information into stable control of the self-dual finite-window observable, or if the historical proof exposes a different spatial lemma now available all-parameter.

**Opportunity-cost negative.** The problem is at least 27 years old in its present small-parameter form, and the 2025 authors had the modern DFP/quasi-duality toolkit available without closing it. The group has IPS expertise, but no uniquely BABP-specific new object has yet appeared. This is why a target in the principal's own recent line can outrank it.

Sources:

- Aidan Sudbury, *Hunting submartingales in the jumping voter model and the biased annihilating branching process*, Advances in Applied Probability 31 (1999), 839--854, DOI `10.1239/aap/1029955207`; abstract explicitly states the improvement to `lambda >= 0.0347`.
- Fabio Martinelli, Assaf Shapira, Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:`2510.20461`, especially Section 5, Remark 5.4.

---

## Candidate 1: finish the positive-rates conjecture for simple IPS

### Precise target

A simple IPS is a homogeneous, binary, one-dimensional, one-sided nearest-neighbor system. In the transition-probability notation

$$
r_{xy}:=P_0(1\mid xy),\qquad x,y\in\{0,1\},
$$

positive rates mean

$$
r_{11}<1,\qquad r_{10}<1,\qquad r_{01}>0,\qquad r_{00}>0.
$$

The target is:

> Prove that every simple IPS with positive rates is ergodic.

For a first programme one should use the sharper residual formulation from the latest paper rather than attack the whole four-parameter cube: prove ergodicity in the remaining region adjacent, after time-scaling and state symmetries, to the East boundary

$$
\{r_{11}=0,\ r_{10}=1,\ r_{01}>0,\ r_{00}=0\}.
$$

### Exact open-status evidence

Głuchowski--Menz, *Time-Scaling, Ergodicity, and Covariance Decay of Interacting Particle Systems*, Journal of Statistical Physics 192 (2025), article 6, Section 7, explicitly studies the open positive-rates problem for binary one-sided nearest-neighbor systems. It proves the additive subcase and says a small parameter region remains outside the known criteria.

Głuchowski--Menz, *Ergodicity Criterion for One-Sided, One-Dimensional IPS with a Long-Lived State*, Electronic Communications in Probability 31 (2026), DOI `10.1214/26-ECP767`, arXiv:`2508.08459`, sharpens this further. The introduction states that the only simple positive-rate IPS whose ergodicity remains unresolved are noisy versions of East. After Theorem 3.1 the paper identifies the residual region next to the East boundary above and explains why a positive-noise perturbation is expected to be ergodic but standard East methods cease to apply.

### Successor check through 2026-08-15

I searched the exact paper title, `positive rates conjecture simple IPS`, `noisy East ergodicity`, `one-sided nearest-neighbor IPS positive rates`, and combinations with 2026. I found the 2026 ECP publication of the long-lived-state criterion but no later paper resolving the noisy-East residual or the simple-IPS conjecture. This is a targeted successor check, not a proof of absence from all literature databases.

### Best known result and concrete obstruction

The 2026 criterion is the following. For a state `a`, define

$$
\beta(a)=\min_\zeta P_0(a\mid\zeta),
$$

and

$$
\delta(a)=\max_{\zeta:\zeta(0)=a}\bigl(1-P_0(a\mid\zeta)\bigr).
$$

If

$$
\delta(a)<\sqrt2\,\beta(a),
$$

then the IPS is ergodic. The proof uses a long-lived common state as a spacetime wall under the canonical coupling.

The residual near East is genuinely outside this one-site mechanism. This can be checked directly for both possible wall states.

For `a=0`,

$$
\beta(0)=1-\max_{x,y}r_{xy}\leq1-r_{10},
$$

while

$$
\delta(0)=\max\{r_{00},r_{01}\}\geq r_{01}.
$$

Hence the current criterion necessarily fails whenever

$$
r_{01}\geq\sqrt2(1-r_{10}),
\tag{1}
$$

which holds throughout a full wedge approaching the East boundary with `r_{01}` fixed away from zero.

For `a=1`,

$$
\beta(1)=\min_{x,y}r_{xy}\leq r_{00},
$$

and

$$
\delta(1)=\max\{1-r_{10},1-r_{11}\}\geq1-r_{11}.
$$

Thus the same criterion necessarily fails whenever

$$
1-r_{11}\geq\sqrt2\,r_{00},
\tag{2}
$$

again automatic sufficiently near the East boundary. Equations (1)--(2) show that simply choosing the other state as the one-site wall cannot close the residual.

The latest paper gives the deeper obstruction: East itself is exceptional but `almost ergodic`; its non-product extremal invariant behavior is unstable under noise. Yet almost any added noise makes the model non-reversible and destroys the explicit invariant measure, so the reversible spectral-gap machinery for East does not transfer.

### Cheap next falsification test

The first test should extend the *wall itself*, not invent another representation.

Use the canonical coupling for a residual noisy-East rule and replace the single common-state wall by the smallest nontrivial agreed block, length two. Condition on the exterior neighbor adversarially. The pair of coupled trajectories restricted to this block has finitely many agreement/disagreement states. Construct the killed finite-state chain in which killing means a disagreement has crossed the block from the influencing side before the block has regenerated to full agreement. Compute the Perron/next-generation factor for one attempted crossing.

The test is decisive in either direction:

- if its spectral radius is `<1` uniformly for every positive-noise point in the residual after time-scaling, it gives a concrete block-renewal mechanism not present in the one-site theorem;
- if it approaches or exceeds `1` throughout the residual as the East boundary is approached, the straightforward finite-wall extension should be killed before a long proof attempt.

This is a finite exact calculation, naturally suited to symbolic enumeration plus a proof of the resulting inequalities. It uses the same coupling geometry as the principal's latest theorem while asking a genuinely stronger question. The single-site calculation (1)--(2) already establishes why block length one cannot succeed.

### Group advantage

Very high. This is the principal's own current line. The repository/group already has:

- the simple-IPS four-parameter representation;
- the time-scaling reduction to boundary faces;
- the canonical coupling and disagreement picture;
- numerical classification of the parameter space;
- the long-lived-state wall mechanism and its exact failure region;
- 1D IPS experience independent of the now-released duality/cancellation preference.

This is exactly the sort of prior-work leverage the new architecture was meant to exploit.

### Expected value relative to BABP

**Higher.** Both problems are serious. The decisive comparison is leverage. BABP has a long-standing local-observable gap that survived the 2025 all-parameter DFP progress. Positive rates has a residual region carved out by the principal's own two recent advances and admits a cheap finite-block test of the next mechanism.

The risk is real: the East boundary is singular, and failure of the length-two wall test would sharply reduce this advantage. That is a good property for target selection because it gives the Professor an inexpensive early exit.

---

## Candidate 2: sharp concentration of voter-model discordant edges on random regular graphs

### Precise target

Let `G_{d,n}` be a random `d`-regular graph, let `D_t^n` be the set of discordant edges in the continuous-time voter model started from i.i.d. Bernoulli(`u`) opinions, and let

$$
\mathcal D_t^n=\frac{|D_t^n|}{dn/2}.
$$

Avena--Baldasso--Hazra--den Hollander--Quattropani, Section 1.4, Eq. (1.9), state the expected strengthening that for `t_n/n -> 0` and `C_n -> infinity`,

$$
\mathbf P\left(
\left|\mathcal D_{t_n}^n-\mathbf E\mathcal D_{t_n}^n\right|
>C_n\sqrt{t_n/n}
\right)\longrightarrow0
\tag{3}
$$

in their quenched-in-probability sense.

Their proved uniform concentration reaches polynomially sublinear windows `n^{1-delta}`; (3) is the sharp fluctuation-scale extension proposed by the authors.

### Exact open-status evidence

L. Avena, R. Baldasso, R. S. Hazra, F. den Hollander, M. Quattropani, *Discordant edges for the voter model on regular random graphs*, ALEA 21 (2024), 431--464, DOI `10.30757/ALEA.v21-18`, Section 1.4, Eq. (1.9).

### Successor check through 2026-08-15

Targeted searches found later work by the same circle on random rewiring and directed/heterogeneous graphs, but no paper proving Eq. (1.9) for the static undirected random regular graph. In particular, Avena--Baldasso--Hazra--den Hollander--Quattropani (arXiv:`2501.08703`) treats random rewiring, while Capannoli (arXiv:`2407.06318`) and Avena--Capannoli--Hazra--Garlaschelli (arXiv:`2506.12169`) treat directed heterogeneous settings.

### Cheap calculation: identify the fluctuation scale and the real drift obstruction

This candidate has a useful first-principles probe. Fix a `d`-regular graph with `n` vertices and `m=dn/2` edges. For a configuration `eta`, let

$$
D(\eta)=\#\{\{x,y\}\in E:\eta_x\neq\eta_y\},
\qquad
\mathcal D=D/m,
$$

and let `k_x` be the number of neighbors of `x` disagreeing with `x`.

At an update of `x`, a flip occurs with probability `k_x/d`; conditional on a flip, the number of discordant incident edges changes from `k_x` to `d-k_x`. Hence

$$
L D
=\sum_x\frac{k_x}{d}(d-2k_x).
$$

Define the wedge observable

$$
W(\eta)=\sum_x k_x(d-k_x).
$$

Since `sum_x k_x=2D` and `sum_x k_x^2=2dD-W`,

$$
L D=\frac{2}{d}W-2D,
$$

so

$$
L\mathcal D=\frac{4}{d^2n}W-2\mathcal D.
\tag{4}
$$

The martingale noise already has exactly the conjectured scale. One update changes `D` by at most `d`, hence

$$
|\Delta\mathcal D|\leq\frac2n.
$$

The total update rate is `n`, so for the martingale part `M_t` of `mathcal D_t`,

$$
\frac{d}{dt}\langle M\rangle_t\leq\frac4n,
\qquad
\langle M\rangle_t\leq\frac{4t}{n}.
\tag{5}
$$

Thus `sqrt(t/n)` is not wishful scaling: it is the intrinsic jump-martingale scale. The missing problem is to control the time-integrated centered drift in (4), i.e. a two-edge/wedge correlation observable, at the same scale.

There is no initial-variance disaster at ordinary fixed or growing times. Under Bernoulli(`u`) initial data, put `s=u(1-u)` and `r=2s`. For two incident edges the covariance of their discordance indicators is

$$
s-r^2=s(1-4s)=s(1-2u)^2.
$$

Therefore

$$
\operatorname{Var}(\mathcal D_0)
=
\frac{
 m r(1-r)+2n\binom d2 s(1-4s)
}{m^2}
=O(n^{-1}).
\tag{6}
$$

**Qualification.** The source literally states (3) for every sequence with `t_n/n -> 0`. Its intended very-small-time endpoint should be checked before adopting the theorem verbatim, because the initial fluctuation scale in (6) is `n^{-1/2}`, whereas `sqrt(t_n/n)` becomes smaller when `t_n -> 0`. A safe research target is the authors' moderate/sublinear-time sharpening with the intended lower-time convention made explicit, or a corrected scale `sqrt((1+t_n)/n)` if the authors agree that an initial term is required. I would not silently alter Eq. (1.9).

### Group advantage

Moderate. The problem is classical IPS and the calculation above isolates a concrete drift observable. Coalescing random walks and graphical representations are familiar. But the proof in the paper depends heavily on random-regular-graph geometry, meeting-time estimates, and weak-dependence of many coalescing walks. The group has less demonstrated comparative advantage there than for candidate 1.

### Expected value relative to BABP

Comparable, perhaps slightly higher in *local tractability* because (4)--(5) isolate a quantitative target and the conjectured scale is already visible. Lower than candidate 1 because random-graph concentration is not part of the principal's established technical line. I would switch from BABP to this only if Student B finds no concrete small-`lambda` mechanism **and** the positive-rates block test fails quickly.

---

## Candidate 3: discordance for the voter model on undirected heterogeneous configuration models

### Precise target

Extend the random-regular-graph voter-model scaling theory to an undirected configuration model with heterogeneous degrees. A reasonable first bounded version is a degree law supported on

$$
\{3,4,\dots,D\}
$$

with finite `D`, and i.i.d. Bernoulli(`u`) initial opinions. Determine the analogues of:

- the short/moderate-time discordance profile `f_d(t)`;
- the consensus-time diffusion constant `theta_d`; and
- the corresponding first-order law of the discordant-edge density.

### Exact open-status evidence

F. den Hollander, *Evolution of Discordance*, Mathematical Physics, Analysis and Geometry 28 (2025), article 21, DOI `10.1007/s11040-025-09518-y`, Section 2.4, states explicitly:

> It remains an open problem to extend Theorems 2.1--2.2 to the configuration model where the vertex degrees can be different.

The paper adds that there is not even a conjecture for the analogues of `theta_d` and `f_d(t)`.

Capannoli--den Hollander, *Interacting Particle Systems on Random Graphs*, arXiv:`2410.17766`, is the broader 2024 survey context: it surveys voter, Ising and contact processes on random graph ensembles and explicitly advertises open problems and future directions.

### Successor check through 2026-08-15

There has been meaningful progress for **directed** heterogeneous configuration models: Capannoli, arXiv:`2407.06318`, obtains discordance asymptotics on sparse digraphs, and Avena--Capannoli--Hazra--Garlaschelli, arXiv:`2506.12169`, treats heterogeneous directed networks and consensus-time asymptotics. Den Hollander's August 2025 overview nevertheless still labels the **undirected heterogeneous** extension open. My targeted 2026 search found no later undirected resolution.

### Cheap calculation: the correct conserved coordinate already changes

Let `G=(V,E)` be any finite undirected graph with degrees `d_x`, and let the voter model update vertex `x` at rate one by copying a uniformly chosen neighbor. Define

$$
M(\eta)=\sum_x d_x\eta_x.
$$

Then

$$
\begin{aligned}
L M
&=\sum_x d_x\frac1{d_x}\sum_{y\sim x}(\eta_y-\eta_x)\\
&=\sum_{(x,y)\text{ oriented edge}}(\eta_y-\eta_x)\\
&=0.
\end{aligned}
\tag{7}
$$

Thus the degree-weighted opinion density, not the unweighted density, is the exact martingale on a heterogeneous undirected graph. In the regular case this distinction disappears.

Equation (7) is a useful immediate diagnostic: a naive replacement of `d` by the mean degree in the regular-graph formulas cannot be structurally correct. The random-walk dual now has degree-biased stationary measure, and the local weak limit seen from a stationary edge is size-biased. Any candidate formula for `theta` and `f(t)` must be built from that environment.

This does not kill the target, but it shows why the open problem is not a small perturbation of the regular proof.

### Group advantage

Moderate-to-low. The model is an IPS and graphical/coalescing-walk reasoning is natural, but the decisive new ingredients are random environment, size-biased Galton--Watson local limits, mixing and meeting-time asymptotics. Those are not current group strengths. A bounded-degree first case makes the problem cleaner but not obviously short.

### Expected value relative to BABP

Lower. It is explicit and current, but the source itself says even the correct limiting constants are unknown. BABP has a much more localized theorem gap. Candidate 3 is a good reserve if the group wants to move toward random-graph IPS, not the best immediate replacement.

---

## Inspected but not shortlisted

### Hartarsky--Toninelli KCM open problems

Hartarsky--Toninelli, *Kinetically Constrained Models* (SpringerBriefs in Mathematical Physics 53, 2025), especially the out-of-equilibrium chapter, explicitly ends with questions about extending East-style detailed out-of-equilibrium theory to broader KCM. Martinelli--Shapira--Toninelli (2025) makes the FA-1f conjectures precise.

I do not recommend another target from this pool now. The group has just closed finite-seed FA-1f after two exact reductions, and the principal supplied additional negative evidence from extensive prior ChatGPT work on 1D FA-1f off-equilibrium convergence. Moving sideways to another nearby KCM because the models are familiar would violate the opportunity-cost lesson of that closure unless a survey problem came with a genuinely different concrete mechanism. I did not find one that outranks candidate 1 or BABP.

### Ngoc--Schütz open-boundary ASEP/KLS questions

Ngoc--Schütz, *Open interacting particle systems and Ising measures*, arXiv:`2505.16701v2` (2025), surveys open questions for open-boundary IPS and develops an open KLS-type ASEP. The surrounding literature also records open finite-lattice/open-boundary Bethe-ansatz and reverse-duality problems.

I do not shortlist these. They are serious but sit in integrable probability / reflection-equation / Bethe-ansatz technology where this group has little demonstrated leverage. Duality is no longer a preferred organizing ingredient, so there is no reason to choose this just because part of the formulation is algebraic.

### Long-range-random-graph contact process for `1<s<=2`

Gomes--Hilário--de Lima--Mountford, *The extinction of the contact process in a one-dimensional random environment with long-range interactions*, Random Structures & Algorithms 68 (2026), e70060, DOI `10.1002/rsa.70060`, proves a nontrivial subcritical phase for `s>2` and explicitly leaves `1<s<=2` open.

This is a clean and very recent open problem, but I rank it below BABP. The `s>2` proof uses cutpoints/renormalization, while the intermediate regime is precisely where that geometry disappears and unbounded-degree/long-edge effects become harder. The group has contact-process familiarity but no demonstrated leverage on long-range-percolation random environments.

---

## Direct comparison

| target | importance/open status | obstruction localization | group-specific leverage | cheap decisive test | present EV |
|---|---|---|---|---|---|
| noisy-East residual / simple PRC | explicit in 2025 J. Stat. Phys. and 2026 ECP | small residual parameter region; reversibility lost near East | **very high** | exact length-2 coupling-wall transfer | **highest** |
| BABP finite seed, all `lambda>0` | explicit 2025 progress paper; gap since 1999 | fixed-window signed self-duality at small `lambda` | moderate | Student B historical-interface audit | second unless B finds new lemma |
| voter discordance sharp concentration | explicit Eq. (1.9) in 2024 ALEA | centered wedge drift at martingale scale | moderate | (4)--(6) | competitive fallback |
| heterogeneous undirected voter discordance | explicit 2025 overview | limiting constants themselves unknown | moderate-low | degree-weighted martingale (7) | lower |
| long-range contact process `1<s<=2` | explicit 2026 paper | random-environment geometry changes regime | low-moderate | no comparably sharp local test found | lower |

## Suggested Professor decision

If Student B's first BABP handoff produces only the conclusion that the `0.0347` proof obstruction persists and the DFP theorem does not directly control the finite-test self-duality observable, I would **pivot immediately to the noisy-East residual positive-rates target**.

If Student B instead isolates a genuinely new lemma that is both sufficient for all small `lambda` and has a credible proof mechanism from the 2025 DFP inputs, compare that lemma against the following single test before choosing:

> Can the two-site agreed-block transfer under the canonical coupling be computed and shown subcritical anywhere beyond the 2026 one-site wall criterion, especially uniformly along the residual noisy-East region?

A positive answer would still favor positive rates because it supplies a concrete mechanism with unusually high principal-specific leverage. A negative answer would materially lower candidate 1 and could justify committing to BABP.

The important point is that these are now two falsifiable first lemmas rather than two broad themes.

## Source list

1. Maciej Głuchowski, Georg Menz, *Time-Scaling, Ergodicity, and Covariance Decay of Interacting Particle Systems*, Journal of Statistical Physics 192 (2025), article 6, DOI `10.1007/s10955-024-03387-5`, especially Section 7.
2. Maciej Głuchowski, Georg Menz, *Ergodicity Criterion for One-Sided, One-Dimensional IPS with a Long-Lived State*, Electronic Communications in Probability 31 (2026), DOI `10.1214/26-ECP767`; arXiv:`2508.08459`.
3. Fabio Martinelli, Assaf Shapira, Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:`2510.20461`, especially Section 5 and Remark 5.4.
4. Aidan Sudbury, *Hunting submartingales in the jumping voter model and the biased annihilating branching process*, Advances in Applied Probability 31 (1999), 839--854, DOI `10.1239/aap/1029955207`.
5. Luca Avena, Rangel Baldasso, Rajat Subhra Hazra, Frank den Hollander, Matteo Quattropani, *Discordant edges for the voter model on regular random graphs*, ALEA 21 (2024), 431--464, DOI `10.30757/ALEA.v21-18`, especially Section 1.4 and Eq. (1.9).
6. F. Capannoli, F. den Hollander, *Interacting Particle Systems on Random Graphs*, arXiv:`2410.17766`.
7. F. den Hollander, *Evolution of Discordance*, Mathematical Physics, Analysis and Geometry 28 (2025), article 21, DOI `10.1007/s11040-025-09518-y`, especially Section 2.4.
8. Federico Capannoli, *Evolution of discordant edges in the voter model on random sparse digraphs*, arXiv:`2407.06318`.
9. Luca Avena, Federico Capannoli, Rajat Subhra Hazra, Diego Garlaschelli, *Voter model on heterogeneous directed networks*, arXiv:`2506.12169`.
10. Ivailo Hartarsky, Cristina Toninelli, *Kinetically Constrained Models*, SpringerBriefs in Mathematical Physics 53 (2025), DOI `10.1007/978-3-031-93115-4`.
11. Ngo P. N. Ngoc, Gunter M. Schütz, *Open interacting particle systems and Ising measures*, arXiv:`2505.16701v2`.
12. Pablo A. Gomes, Marcelo R. Hilário, Bernardo N. B. de Lima, Thomas Mountford, *The Extinction of the Contact Process in a One-Dimensional Random Environment With Long-Range Interactions*, Random Structures & Algorithms 68 (2026), e70060, DOI `10.1002/rsa.70060`.

## Handoff

**Decisive file:** `research/active/babp-finite-seed/students/student-a/recon-001-open-problem-scan.md`.

**Spine conclusion O1:** present opportunity-cost evidence favors replacing provisional BABP with the residual simple-IPS positive-rates/noisy-East problem. The reason is unusually strong group-specific leverage plus a cheap block-coupling falsification test, not superficial proximity to previous IPS work.

**Conditional caveat:** Student B's current BABP audit should be allowed to return. If it has already isolated a genuinely new sufficient small-`lambda` lemma with a plausible route, the Professor should compare that exact lemma against the two-site noisy-East wall transfer before committing. If B has only confirmed the old signed-local-observable obstruction, pivot.