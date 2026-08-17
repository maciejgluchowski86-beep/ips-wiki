# Proof spine: generalized patch representations

Date: 2026-08-17

## Target

Extend the binary patch-representation mechanism to finite-state single-site replacement IPS, identify which parts are genuinely new, and demonstrate value on natural nonbinary models.

## E0. Binary benchmark

**Settled by the canonical paper.**

## E1. Arbitrary finite-state typed signed dual

**Mathematically settled in Assignment 001. Contribution status narrowed by Assignment 008.**

Reference-state indicator tensors give an exact signed Feynman--Kac dual for arbitrary bounded finite-range single-site replacement IPS, with successful records `(i,t,r,tau)` hiding post-source outcome.

Novelty status: **known ingredients, assembly plausibly new**. Finite-state/product duality, multistate graphical duality, and signed finite-type FK duality all have direct predecessors.

## E2. Killed typed patch factorization

**Mathematically settled in Assignment 002. Primary plausible novelty anchor after Assignment 008.**

Typed incoming target conflicts make bare skeleton conditioning false: cemetery entry deletes future no-record constraints. Because the duality function vanishes at cemetery, the exact killed/noncemetery weighted identity restores local factorization.

No equivalent combination was found in the ancestor-clan, information-percolation, signed-FK, or multistate-duality literatures.

Novelty status: **plausibly new theorem/mechanism**.

## E3. Exact typed patch representation

**Settled in Assignment 003.**

The killed factorization yields the exact bulk/end patch representation for arbitrary finite local state space. This is part of the surviving generalized mechanism.

## E4. Exact finite-state bulk transfer

**Settled in Assignment 004.**

The signed interior transfer is

\[
K_i(0,\cdot)=0,
\qquad K_i(r,s)=a_{i,r}^s(\emptyset).
\]

The cancellation of empty-target escape and no-success killing against the FK potential gives the exact local realization. Typed bulk patch positivity becomes nonnegativity of finitely parameterized matrix-semigroup boundary responses.

Novelty status: **known ingredients, assembly plausibly new**. The IPS-to-transfer dictionary appears project-specific; positivity of matrix responses is standard positive-systems theory.

## E5. Binary specialization

**Settled exactly.**

At `d=2` the generalized representation and positivity property recover the canonical binary patch construction and its coefficient inequalities, with no stronger surrogate condition.

## E6. Boundary-complete `d=3` reduction and endpoint obstruction

**Settled in Assignment 005.**

Boundary completeness forces `K` Metzler, leaving only `OI` scalar responses. A genuine IPS gives an exact positive-endpoint/negative-interior witness, proving that the binary endpoint collapse fails in three states.

This remains a genuine structural difference between binary and multistate patch positivity.

## E7. Exact `d=3` spectral test

**Mathematically settled in Assignment 006; novelty removed in Assignment 008.**

Every remaining response is decided by endpoints plus at most one critical value, with all degenerate cases handled.

Novelty status: **known / directly subsumed**. For any `d_0>0`,

\[
p e^{tK}f\ge0
\iff
p e^{t(K-d_0I)}f\ge0,
\]

so the problem is external positivity of a stable third-order SISO realization. Exact real-pole third-order criteria predate this project (Lin--Fang 1997; Weller--Martin 2020).

Do not use Assignment 006 as a novelty claim.

## E8. Natural exact nonbinary subclass

**Settled in Assignment 007.**

For exchange-symmetric reference-neighbour dynamics

\[
Q=
\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix},
\]

boundary-complete typed patch positivity is exactly

\[
c\ge a,
\]

and, for every outgoing row `p=(p_0,p_1,p_2)`,

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\]

\[
(b+2a)p_0+a(p_1+p_2)\ge0.
\]

The class is genuinely nonbinary, but its scalar analytic content is a structured external-positivity consequence.

Novelty status: **known ingredients, assembly plausibly new**. Treat it as an application-ready exact gate, not the primary contribution.

## E9. Novelty audit

**Settled in Assignment 008. Outcome `CONTINUE-TO-APPLICATIONS`.**

Closest predecessor families reconstructed:

- Lloyd--Sudbury/Sudbury product IPS dualities;
- Sturm--Swart and Latz--Swart finite-state/multistate graphical dualities;
- Dawson--Greven signed finite-type FK duality;
- Fernández--Ferrari--Garcia clans of ancestors;
- Lubetzky--Sly information percolation;
- classical/modern positive-systems and external-positivity theory;
- recent multistate epidemic dualities.

The broad ingredients are known. The exact killed typed patch factorization/representation was not found in equivalent form and remains the load-bearing plausible novelty.

## E10. Natural application

**Open and current load-bearing edge.**

The next question is no longer another abstract coefficient theorem. It is:

> Does the surviving generalized patch mechanism specialize naturally to a genuinely nonbinary finite-state IPS from the literature, and does it yield a useful statement beyond rephrasing known duality?

The application block must:

1. start from a natural published model, not tune rates to the criterion;
2. write its physical generator in the exact single-site replacement form;
3. derive the typed coefficients and successful skeleton;
4. test patch positivity honestly;
5. if positive, identify a concrete consequence or representation benefit;
6. compare that consequence with application-specific prior work before claiming value.

A negative positivity finding is acceptable if it identifies a structural obstruction.

Likely search classes include genuinely multistate contact/epidemic or stage-structured models, but model selection is part of the application assignment and must be literature-driven.

## E11. Generic `d>3` tractable positivity

**Deferred.**

The representation already holds for arbitrary finite `d`. Higher-order coefficient characterization overlaps the established external-positivity problem and is not next by default.

Activate it only if:

- a concrete application naturally requires more than three states; or
- a later structured-class opportunity gives independent mathematical value.

## E12. Comparison/convergence and multi-site physical updates

**Downstream.**

Do not generalize the binary comparison/convergence theorems automatically. First learn from applications which positivity/order object is actually useful. Simultaneous multi-site physical updates remain outside the proved representation class.

## Current novelty framing

The project must not claim novelty for finite-state duality, signed FK duality, partial Poisson revelation, Metzler semigroups, or third-order external positivity individually.

The plausible contribution is the **interface**:

\[
\text{signed typed dual}
\to
\text{hidden successful skeleton}
\to
\text{cemetery-aware killed patch factorization}
\to
\text{exact finite-state patch representation}.
\]

Historical priority remains plausible rather than established.