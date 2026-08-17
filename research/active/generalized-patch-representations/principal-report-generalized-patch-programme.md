# Principal report: generalized finite-state patch representations

Date: 2026-08-17

This report summarizes the verified programme through Assignment 010. It is organized around the questions posed when the phase was opened. I separate mathematical correctness from research-contribution status throughout.

## 1. Can the binary construction be extended to more than two local states?

Yes at the representation level, for every finite local state space. Let

\[
E=\{0,1,\ldots,d-1\}
\]

with distinguished reference state `0`, and use the reference-indicator basis

\[
h_0\equiv1,
\qquad h_a(x)=1_{\{x=a\}},\quad a\ne0.
\]

For a finite typed partial configuration `xi`, define

\[
H_\xi(\eta)=\prod_{i\in\operatorname{supp}\xi}1_{\{\eta_i=\xi(i)\}}.
\]

Assignments 001--004 give, for arbitrary finite `d`, an exact signed Feynman--Kac dual, a successful-interaction skeleton, a killed patch factorization, an exact patch representation, and an exact local transfer description of bulk factors. At `d=2` the construction reduces exactly to the binary one; no surrogate or strengthened condition is inserted.

What is not established is a useful general coefficient-level positivity criterion for arbitrary `d`. The representation theorem is genuinely finite-state; the tractable positivity theory is not. The programme analyzed `d=3` because it is the first genuinely multistate case. I do not currently recommend a generic `d>3` positivity programme: the novelty audit identified the higher-dimensional sign problem as an instance of higher-order external positivity, which is already a substantial subject in control theory.

## 2. Can the physical dynamics be more general than binary flips?

Yes, for arbitrary bounded finite-range single-site replacements. The physical generator may be

\[
L f(\eta)
=
\sum_i\sum_{x\ne y}
1_{\{\eta_i=x\}}c_i^{x\to y}(\eta_{N(i)})
\bigl[f(\eta^{i,y})-f(\eta)\bigr],
\]

with completely general bounded rates depending on a finite neighbourhood. Thus a site may jump between any pair of local states, and the rate may depend arbitrarily on the local finite configuration.

The proved scope stops at single-site replacement. Genuine simultaneous multi-site physical updates have not been treated. Extending the geometry to such maps would be a separate problem rather than a formal corollary of the present construction.

## 3. What is the duality, and what is the dual process?

Expand each physical rate in the reference-indicator tensor basis,

\[
c_i^{x\to y}
=
\sum_\tau \widehat c_i^{x\to y}(\tau)H_\tau.
\]

For an active dual source type `r`, the exact local signed coefficients are

\[
a_{i,r}^{0}(\tau)=\widehat c_i^{0\to r}(\tau),
\]

\[
a_{i,r}^{s}(\tau)
=
\widehat c_i^{s\to r}(\tau)-\widehat c_i^{0\to r}(\tau),
\qquad s\ne0,r,
\]

and

\[
a_{i,r}^{r}(\tau)
=-\widehat c_i^{0\to r}(\tau)
-\sum_{y\ne r}\widehat c_i^{r\to y}(\tau).
\]

Use clocks of rates `|a|`, branch signs `sgn(a)`, and the corresponding local Feynman--Kac potential. This gives

\[
P_tH_{\xi}(\eta)
=
\mathbb E_\xi\left[
\sigma_t
\exp\left\{\int_0^tV(\xi_u)\,du\right\}
H_{\xi_t}(\eta)
\right],
\]

under the same sort of infinite-volume exponential-integrability hypothesis used in the binary paper.

The dual state is a finite typed active configuration together with a sign, plus a cemetery state `dagger` for incompatible typed overlaps. A branch at source `(i,r)` removes the source, optionally reinserts it with post-source type `s`, and merges a typed target `tau`. If incompatible active types are demanded at one site, the process enters cemetery. For `d>2`, genuine source retyping is a new branch type absent from the binary set-valued process.

For each nonempty target `tau`, all post-source outcomes are superposed into a coarse successful record

\[
(i,t,r,\tau),
\]

which reveals source site, time, pre-source type and typed target, but deliberately hides the post-source outcome `s`.

That hidden mark is what makes the multistate patch construction nontrivial. One-site spacetime patches carry the hidden signed source histories. Incoming typed targets can conflict with the current hidden active type and send the dual to cemetery. Because cemetery entry removes all future no-record constraints, bare conditioning on the coarse successful-record skeleton is not product. Assignment 002 contains an exact finite counterexample to the naive factorization.

Since `H_\dagger=0`, there is nevertheless an exact repair: multiply by the noncemetery indicator, factor the killed weight patchwise, and then average the signed local history inside each consistent patch. The resulting semigroup representation is

\[
P_tH_{\xi_0}(\eta)
=
\int
\left(\prod_{P\in\mathcal B_t}C(P)\right)
\left(\prod_{P\in\mathcal E_t}C_t(\eta_{i(P)},P)\right)
\nu_t(dg).
\]

Bulk factors depend only on local patch data, while end factors are one-site functions of the terminal physical state.

This killed typed factorization and representation is the strongest surviving novelty candidate from the programme. The audit explicitly does not regard finite-state duality, multistate graphical duality, signed Feynman--Kac duality, ancestor constructions, or partial Poisson revelation as new by themselves. Those ingredients have direct predecessors. What was not found in equivalent form is the full interface

\[
\text{signed typed dual}
\to
\text{hidden successful skeleton}
\to
\text{typed cemetery obstruction}
\to
\text{killed/noncemetery factorization}
\to
\text{exact finite-state patch representation}.
\]

The audit grades this as a `plausibly new theorem/mechanism`, not as established historical priority.

## 4. What is the multistate analogue of patch positivity?

The signed interior transfer at a source site is exactly

\[
K_i(0,\cdot)=0,
\qquad
K_i(r,s)=a_{i,r}^{s}(\emptyset).
\]

There is also an unsigned killed-consistency transfer. Every realized bulk patch contribution is a ratio with positive denominator and with numerator given by one of four finite-dimensional boundary responses built from `e^{tK_i}`: incoming/incoming, incoming/outgoing, outgoing/incoming, and outgoing/outgoing. Thus the exact multistate analogue of bulk patch positivity is simply nonnegativity of all realized signed matrix-semigroup boundary responses for every patch length.

At `d=2` this reduces exactly to the binary coefficient inequalities from the paper.

At `d=3`, the programme first proved that binary-style zero-length and long-time endpoint inequalities are insufficient. There is a physically realizable response

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

with positive endpoints and exact interior minimum

\[
-\frac1{1224}.
\]

Assignment 006 then gave a correct finite spectral test: endpoints plus at most one explicit interior critical value, including all repeated, zero-eigenvalue, Jordan and reducible cases. Assignment 007 found a genuinely nonbinary exchange-symmetric subclass in which the already-necessary Metzler ordering removes the interior obstruction and yields an exact algebraic criterion.

The important novelty correction is that the Assignment-006 `d=3` finite spectral criterion is not a project contribution. The literature audit found it directly subsumed by third-order SISO external-positivity theory: after an exponential spectral shift, each scalar patch response is an impulse response `C e^{tA}B`, and Lin--Fang (1997) and Weller--Martin (2020) already give exact third-order nonnegative-response criteria. That result remains correct and useful as a computational tool, but it is out of the contribution claim.

The project-specific content on the positivity side is therefore the derivation of the local transfer from the signed patch representation and the exact dictionary from patch boundaries to matrix responses, not the scalar external-positivity theory itself.

## 5. What applications does the generalized construction have?

Two deliberately unflattering, literature-selected three-state models have been tested. Both genuinely activate hidden outcomes and typed cemetery conflicts, and neither was selected because it looked patch positive. Both fail.

The first model was Krone's two-stage contact process,

\[
0=\text{vacant},\qquad1=\text{juvenile},\qquad2=\text{adult},
\]

with adult-driven births, juvenile maturation and stage-dependent death. For an adult-neighbour successful record the hidden signed row is

\[
(\lambda,-\lambda,-\lambda).
\]

A same-source outgoing-to-outgoing patch is genuinely realized and its numerator is strictly negative for every finite patch length whenever `\lambda>0`. At the exact verified point

\[
\lambda=\gamma=\delta=1,
\qquad e^{-t}=1/2,
\]

we obtain

\[
N_{OO}=-5/16,
\qquad D_{OO}=5/16,
\qquad C_{OO}=-1.
\]

A bounded check of spatial SIRS gives the same local obstruction. Existing Krone/Foxall/Sturm--Swart theory is already strong enough that the mere existence of another dual representation would not by itself be a model-level contribution.

The second model was chosen specifically to avoid repeating the vacancy/catalytic-birth architecture: the three-state ferromagnetic Potts model with single-spin Metropolis dynamics. Here all three states are active, all active states retype one another, every directed physical replacement has positive rate in the finite-temperature regime, the successful record has genuinely nondeterministic hidden outcomes, and cemetery conflicts are realizable.

Nevertheless, for one singleton target,

\[
a_1^2(\tau)
=-qz^2(1-z^2)<0,
\qquad0<z=e^{-\beta J}<1.
\]

The hidden outcome `2` can feed a later source-type-2 successful record, so a realized arbitrarily short `OO` patch is negative throughout the finite-temperature interacting regime. At the exact verified point

\[
z=1/2,
\qquad q=1,
\qquad t_*=(8/3)\log(5/4),
\]

with

\[
p=(3/16,5/16,-3/16),
\]

we get

\[
N_{OO}(t_*)=-3884/390625<0.
\]

This is not the two-stage obstruction in disguise. Its physical mechanism is unequal source sensitivity caused by Metropolis saturation.

Both failures are instances of one short-patch lemma. If active types `r\ne s` and a nonempty target `tau` satisfy

\[
\boxed{
a_r^s(\tau)
=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0,}
\]

and hidden outcome `s` is realizable and can feed a subsequent source-`s` successful record, then a realized arbitrarily short outgoing-to-outgoing patch has negative numerator. Therefore typed patch positivity fails.

The contact/SIRS catalytic-birth lemma is the special case in which a target mode acts in `0\to r` but has no compensating active-source transition into `r`. Potts shows that the actual obstruction is broader: unequal target-mode sensitivity between active source states is enough. This negative result is useful because it explains the failures rather than leaving two isolated counterexamples.

A genuinely positive application would have to satisfy several conditions simultaneously. It would have to be a natural published genuinely multistate single-site replacement IPS, not a tuned rate table. Its successful records would need nontrivial hidden post-source randomness; a deterministic voter/coalescing/additive dual would be a degenerate pass. Typed target conflicts should genuinely occur, so the killed factorization is actually needed. The model would have to evade the short-`OO` contrast obstruction whenever a hidden outcome can seed another successful record, and all longer realized patch responses would still need to be nonnegative. Finally, and most importantly, the resulting representation would need to prove or reduce something model-specific that is not already available from coupling, attractiveness, additive duality, or the model's standard graphical construction.

No such positive example has been found.

## Opportunity-cost view

I do not recommend a generic `d>3` positivity block now. The finite-state representation is already arbitrary in `d`, while higher-order positivity is already recognizable as external-positivity theory, and the two natural application blocks give no evidence that more coefficient algebra is the missing ingredient.

I also do not recommend a third positivity-driven model search. We have now tested two materially different natural architectures: contact/epidemic growth with stage/recovery dynamics, and fully active symmetric Metropolis retyping. Both genuinely exercise the killed typed machinery and both fail locally through the same general short-`OO` contrast mechanism. Continuing to search until a flattering model appears would have weak evidential value.

The only continuation I would fund is one bounded block on the killed representation **without assuming bulk positivity**. The question would be whether conditioning on the successful skeleton and averaging signed local histories before absolute values yields a useful cancellation identity, norm estimate, comparison, or other consequence unavailable from standard graphical duality even when individual bulk factors have mixed sign.

That directly tests the surviving plausible novelty anchor rather than another positivity corollary. I would pre-register a hard stop: if one bounded attempt produces neither a concrete model-independent consequence nor a natural problem in which the cancellation survives globally, close the programme rather than return to generic `d>3` algebra or another model search.

My opportunity-cost ordering is therefore

\[
\boxed{\text{one bounded representation/cancellation block}\;>\;\text{stop}\;>\;\text{generic }d>3.}
\]

The programme has produced a correct arbitrary-finite-state patch representation and a new-looking cemetery-aware factorization mechanism. It has not yet produced a positive multistate application theorem. The novelty audit already removed the `d=3` spectral centerpiece from the contribution claim, and the two application failures substantially weaken the case for multistate patch positivity as the main application engine.