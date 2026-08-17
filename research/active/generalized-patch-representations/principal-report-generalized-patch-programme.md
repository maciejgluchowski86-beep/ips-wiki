# Principal report: generalized finite-state patch representations

Date: 2026-08-17

This report summarizes the verified programme through Assignment 010. It is organized around the questions posed at the start of the phase. Mathematical correctness and research-contribution status are kept separate.

## 1. More general state spaces than two

### Established

Yes, at the representation level. Let

\[
E=\{0,1,\ldots,d-1\}
\]

be any finite local state space with distinguished reference state `0`. Use the reference-indicator tensor basis

\[
h_0\equiv1,
\qquad h_a(x)=1_{\{x=a\}},\quad a\ne0,
\]

and for a finite typed partial configuration `xi`,

\[
H_\xi(\eta)=\prod_{i\in\operatorname{supp}\xi}1_{\{\eta_i=\xi(i)\}}.
\]

Assignments 001--004 give an exact signed dual, successful skeleton, killed patch factorization, patch representation, and exact local transfer description for arbitrary finite `d`.

The binary theory is recovered exactly when `d=2`; no extra condition is introduced in that specialization.

### Not established

There is no general tractable coefficient criterion for patch positivity at arbitrary `d`. The representation is general; the usable positivity theory is not. The controlled `d=3` analysis was carried out because it is the first genuinely multistate case.

A generic `d>3` positivity programme is not currently recommended: after the novelty audit, higher-dimensional positivity is recognized as an instance of higher-order external positivity, a substantial pre-existing subject rather than an obviously project-specific theorem direction.

## 2. More general updates than binary flips

### Established

Yes, for arbitrary bounded finite-range **single-site replacement** dynamics. The physical generator may be

\[
L f(\eta)
=
\sum_i\sum_{x\ne y}
1_{\{\eta_i=x\}}
 c_i^{x\to y}(\eta_{N(i)})
\bigl[f(\eta^{i,y})-f(\eta)\bigr],
\]

with completely general bounded rates depending on a finite neighbourhood.

Thus the construction is not tied to flips `0<->1`: a site may change between any pair of local states, and the rate may depend arbitrarily on the local finite configuration.

### Not established

Simultaneous physical updates of several sites are outside the proved framework. Extending the construction from one-site replacement maps to genuine multi-site physical updates would require new geometry and has not been attempted in this phase.

## 3. What the duality is

### Established

Expand each physical rate in the reference-indicator tensor basis,

\[
c_i^{x\to y}
=
\sum_\tau \widehat c_i^{x\to y}(\tau)H_\tau.
\]

For an active dual source type `r`, the exact signed local coefficients are

\[
a_{i,r}^{0}(\tau)=\widehat c_i^{0\to r}(\tau),
\]

\[
a_{i,r}^{s}(\tau)
=
\widehat c_i^{s\to r}(\tau)-\widehat c_i^{0\to r}(\tau),
\qquad s\ne0,r,
\]

\[
a_{i,r}^{r}(\tau)
=-\widehat c_i^{0\to r}(\tau)
-\sum_{y\ne r}\widehat c_i^{r\to y}(\tau).
\]

Using clocks of rates `|a|`, branch signs `sgn(a)`, and a local Feynman--Kac potential gives the exact identity

\[
P_tH_{\xi}(\eta)
=
\mathbb E_\xi\left[
\sigma_t
\exp\left\{\int_0^tV(\xi_u)\,du\right\}
H_{\xi_t}(\eta)
\right],
\]

under the same kind of infinite-volume integrability hypothesis used in the binary paper.

### Novelty status

The audit does **not** regard finite-state or signed Feynman--Kac duality itself as a new contribution. Finite-state/product graphical dualities and signed finite-type Feynman--Kac dualities have direct predecessors, including Lloyd--Sudbury/Sudbury, Sturm--Swart/Latz--Swart, and Dawson--Greven. The present arbitrary-replacement indicator-basis assembly is useful, but its ingredients are too standard to carry the contribution claim by itself.

## 4. What the dual process is, and what replaces binary patches

### Established

The dual state is a finite **typed active configuration** together with a sign, plus a cemetery state `dagger` representing incompatible typed overlaps.

A local branch at source `(i,r)` removes the source, optionally reinserts it with post-source type `s`, and merges a typed target `tau` into the active configuration. If two incompatible active types are required at one site, the dual enters cemetery. For `d>2`, genuine source retyping `r->s` is a new branch type absent from the binary set-valued process.

For every nonempty target `tau`, all post-source outcomes are superposed into a coarse successful record

\[
(i,t,r,\tau),
\]

which reveals source site, time, pre-source type, and typed target, but deliberately **hides the post-source outcome** `s`.

This produces one-site spacetime patches carrying the hidden signed local histories. The crucial multistate phenomenon is that incoming typed targets can conflict with the current hidden active type and send the dual to cemetery.

Bare conditioning on the coarse successful-record skeleton is therefore false: a cemetery event deletes future no-record constraints, coupling what would otherwise be separate patches. Assignment 002 contains an exact finite counterexample to bare factorization.

Because `H_\dagger=0`, the needed repair is exact: multiply by the noncemetery indicator, factor the killed weight patchwise, then average each signed local patch history. The resulting semigroup representation is

\[
P_tH_{\xi_0}(\eta)
=
\int
\left(\prod_{P\in\mathcal B_t}C(P)\right)
\left(\prod_{P\in\mathcal E_t}C_t(\eta_{i(P)},P)\right)
\nu_t(dg).
\]

Bulk factors depend only on local patch data; end factors are one-site functions of the terminal physical state.

### Novelty status

This is the strongest surviving contribution candidate from the audit.

The audit grades the **killed typed patch factorization / representation** as `plausibly new theorem/mechanism`, and the combined framework likewise as `plausibly new theorem/mechanism`. Partial Poisson revelation, ancestor clans, information-percolation skeletons, multistate duality, and signed FK weights all have predecessors. What was not found in equivalent form is their present interface:

\[
\text{signed typed dual}
\to
\text{hidden successful skeleton}
\to
\text{typed cemetery obstruction}
\to
\text{killed/noncemetery factorization}
\to
\text{exact patch representation}.
\]

This is a plausible novelty claim, not a claim that historical priority has been exhaustively proved.

## 5. What is the multistate equivalent of patch positivity?

### Established

For each local source site the signed interior transfer is exactly

\[
K_i(0,\cdot)=0,
\qquad
K_i(r,s)=a_{i,r}^{s}(\emptyset).
\]

There is also an unsigned killed-consistency transfer. Every realized bulk patch contribution is a ratio whose denominator is positive and whose numerator is one of four finite-dimensional boundary responses built from `e^{tK_i}`: incoming/incoming, incoming/outgoing, outgoing/incoming, and outgoing/outgoing. Thus **typed bulk patch positivity** is exactly nonnegativity of these realized signed matrix-semigroup responses for every patch length.

At `d=2` this reduces exactly to the binary coefficient inequalities from the canonical paper.

At `d=3`, Assignments 005--007 clarify what changes. Endpoint conditions alone fail: there is an exact physically realizable response

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

with positive endpoints but minimum `-1/1224`. Assignment 006 then gave a correct finite spectral criterion: endpoints plus at most one explicit interior critical value, including all degenerate spectral cases. Assignment 007 found a genuine exchange-symmetric nonbinary subclass with an exact algebraic criterion.

### Novelty status

The scalar `d=3` finite spectral theorem is **not** part of the contribution claim. The literature audit found it directly subsumed by third-order SISO external-positivity theory: after an exponential spectral shift, each required scalar response is an impulse response `C e^{tA}B`. Lin--Fang (1997) and Weller--Martin (2020) already give exact third-order external-positivity/nonnegative-response criteria.

The project-specific content is the derivation of the local transfer and the dictionary from patch boundaries to those responses, not the general scalar external-positivity theory itself.

## 6. Applications

Two deliberately unflattering, literature-selected three-state applications have now been checked. Both genuinely activate hidden outcomes and cemetery conflicts; neither is a binary model with a passive color, and neither was selected using patch positivity.

### 6.1 Two-stage contact process

For Krone's two-stage contact process,

\[
0=\text{vacant},\qquad1=\text{juvenile},\qquad2=\text{adult},
\]

with adult-driven births and juvenile maturation, the adult-neighbour successful record has hidden signed row

\[
(\lambda,-\lambda,-\lambda).
\]

The same-source outgoing-to-outgoing patch is realized and has strictly negative numerator for every finite patch length when `lambda>0`.

At the exact verified point

\[
\lambda=\gamma=\delta=1,
\qquad e^{-t}=1/2,
\]

\[
N_{OO}=-5/16,
\qquad D_{OO}=5/16,
\qquad C_{OO}=-1.
\]

Spatial SIRS gives the same local obstruction. Existing Krone/Foxall/Sturm--Swart duality and complete-convergence theory also means no model-level novelty is claimed merely from obtaining another representation.

### 6.2 Three-state Potts Metropolis dynamics

To avoid repeating contact/epidemic architecture, Assignment 010 selected the three-state ferromagnetic Potts model with single-spin Metropolis dynamics. Here all three states are active, active states directly retype one another, and the successful record has genuinely nondeterministic hidden outcomes.

For one singleton target,

\[
a_1^2(\tau)
=-qz^2(1-z^2)<0,
\qquad 0<z=e^{-\beta J}<1.
\]

The hidden outcome `2` can feed a later source-type-2 successful record, so a realized arbitrarily short `OO` patch is negative throughout the finite-temperature interacting regime.

At the exact verified point

\[
z=1/2,
\qquad q=1,
\qquad t_*=(8/3)\log(5/4),
\]

\[
p=(3/16,5/16,-3/16),
\]

and

\[
N_{OO}(t_*)=-3884/390625<0.
\]

This is not the catalytic-birth failure in disguise: every physical state is active and every directed replacement rate is positive.

### 6.3 Single lemma explaining both failures

The two application blocks are instances of one short-patch obstruction.

For active types `r!=s` and nonempty target `tau`, if

\[
\boxed{
a_r^s(\tau)
=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0,}
\]

and hidden outcome `s` is realizable and can feed a subsequent source-`s` successful record, then a realized arbitrarily short outgoing-to-outgoing patch has negative numerator. Hence typed patch positivity fails.

The two-stage/SIRS catalytic-birth lemma is the special case where the target mode acts in `0->r` but has no compensating active-source transition into `r`. Potts shows the more general mechanism: unequal target-mode sensitivity between active sources is enough.

This negative result is useful because it sharply limits where positive multistate patch applications can exist.

### What a genuinely positive application would have to look like

A satisfactory positive example would need all of the following.

1. It must be a natural published genuinely multistate single-site replacement IPS, not a tuned coefficient table.
2. Successful records must retain nontrivial hidden post-source randomness; a deterministic voter/coalescing/additive graphical dual is a degenerate pass.
3. Typed target conflicts should genuinely occur, so the killed/noncemetery factorization is actually needed.
4. It must evade the short-`OO` contrast obstruction: whenever hidden outcome `s` can lead to a later source-`s` record, the relevant outgoing coefficients cannot have the negative contrast above.
5. All longer realized patch responses must also be nonnegative.
6. Most importantly, the resulting representation must yield a model-specific theorem or reduction not already available from standard coupling, attractiveness, additive duality, or existing graphical methods.

No such example has been found in this phase.

## 7. Opportunity-cost view

I do **not** recommend a generic `d>3` positivity block now. The representation already covers arbitrary finite state spaces, while higher-order response positivity overlaps established external-positivity theory and the two natural application tests give no evidence that more coefficient algebra is the bottleneck.

I also do **not** recommend a third positivity-driven model search. Two materially different natural architectures -- contact/epidemic growth and fully active symmetric Metropolis retyping -- genuinely exercise the killed typed machinery and both fail locally through the same general short-`OO` contrast lemma. Searching until a flattering model appears would have poor evidential value.

The one continuation I would still fund is a **single bounded block on the killed representation without bulk positivity**: ask whether conditioning and local cancellation before absolute values gives a useful identity, norm estimate, comparison, or other consequence that standard graphical duality does not provide, even when some individual bulk patch factors are negative.

That question goes directly at the surviving plausible novelty anchor rather than its failed positivity corollary. It should have a pre-registered stop rule: if one bounded attempt produces no concrete model-independent consequence or no natural problem where the cancellation survives globally, close the programme rather than return to `d>3` algebra or another application search.

So my ordering is:

\[
\boxed{\text{one bounded representation/cancellation block} \;>\; \text{stop} \;>\; \text{generic }d>3.}
\]

The programme has produced a genuine finite-state representation theorem and a new-looking cemetery-aware factorization mechanism, but it has not yet produced a positive multistate application theorem. Correctness of the surrounding duality and positivity calculations should not be confused with independent research contribution; the novelty audit already removed the `d=3` spectral centerpiece from that category.