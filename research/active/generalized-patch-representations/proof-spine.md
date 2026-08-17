# Proof spine: generalized patch representations

Date: 2026-08-17

## Target

Extend the binary patch-representation mechanism to finite-state single-site replacement IPS, identify which parts are genuinely new, and demonstrate value on natural nonbinary models.

## E0. Binary benchmark

**Settled by the canonical paper.**

## E1. Arbitrary finite-state typed signed dual

**Mathematically settled in Assignment 001; novelty narrowed in Assignment 008.**

Reference-state indicator tensors give an exact signed Feynman--Kac dual for arbitrary bounded finite-range single-site replacement IPS, with successful records `(i,t,r,tau)` hiding post-source outcome.

Novelty status: **known ingredients, assembly plausibly new**.

## E2. Killed typed patch factorization

**Settled in Assignment 002. Primary plausible novelty anchor.**

Typed incoming target conflicts make bare skeleton conditioning false because cemetery entry deletes future no-record constraints. Since the duality function vanishes at cemetery, the killed/noncemetery weighted identity restores local factorization.

Novelty status after Assignment 008: **plausibly new theorem/mechanism**.

## E3. Exact typed patch representation

**Settled in Assignment 003.**

The killed factorization yields the exact bulk/end patch representation for arbitrary finite local state space.

## E4. Exact finite-state bulk transfer

**Settled in Assignment 004.**

\[
K_i(0,\cdot)=0,
\qquad K_i(r,s)=a_{i,r}^s(\emptyset).
\]

Typed bulk patch positivity is exact nonnegativity of local semigroup boundary responses. The `d=2` specialization is exactly canonical binary patch positivity.

## E5. Boundary-complete `d=3` reduction

**Settled in Assignment 005.**

Boundary completeness forces `K` Metzler, leaving only `OI` scalar responses. A genuine IPS has positive zero/long endpoints but a negative interior response, proving that the binary endpoint collapse fails in three states.

## E6. Exact `d=3` spectral test

**Mathematically settled in Assignment 006; novelty removed in Assignment 008.**

Every remaining response is decided by endpoints plus at most one critical value, including degenerate cases.

Novelty status: **known / directly subsumed** by third-order SISO external-positivity theory. Do not use this as a contribution claim.

## E7. Natural exact nonbinary algebraic subclass

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

plus, for every outgoing row `p=(p_0,p_1,p_2)`,

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\]

\[
(b+2a)p_0+a(p_1+p_2)\ge0.
\]

The class is genuinely nonbinary, but its scalar analytic content is structured external positivity rather than the main novelty anchor.

## E8. Novelty audit

**Settled in Assignment 008. Outcome `CONTINUE-TO-APPLICATIONS`.**

Broad ingredients are known: finite-state/product duality, signed finite-type FK duality, ancestor clans, information percolation, and external positivity. No equivalent source was found for the exact hidden-successful-record plus typed-cemetery killed patch factorization.

The plausible contribution remains the interface

\[
\text{signed typed dual}
\to
\text{hidden successful skeleton}
\to
\text{cemetery-aware killed patch factorization}
\to
\text{exact finite-state patch representation}.
\]

## E9. First natural application: two-stage contact process

**Settled negatively in Assignment 009. Outcome `STOP-APPLICATION-POSITIVITY-FAILS`.**

The model was selected from the literature before positivity calculation:

\[
0=\text{vacant},\quad1=\text{juvenile},\quad2=\text{adult},
\]

\[
0\to1\text{ at }\lambda n_2,
\quad1\to2\text{ at }\gamma,
\quad1\to0\text{ at }1+\delta,
\quad2\to0\text{ at }1.
\]

For every adult-neighbour target `tau`,

\[
\boxed{\mathbf a_{1,\tau}=(\lambda,-\lambda,-\lambda).}
\]

The successful record hides three outcomes `0,1,2`, and typed cemetery conflicts are genuinely realizable, so the distinctive killed-patch representation is active in this model.

However, the repeated-source `OO` descriptor is realized and has

\[
N_{OO}(0)=-\lambda<0.
\]

More strongly, with

\[
K=
\begin{pmatrix}
0&0&0\\
0&-(1+\delta+\gamma)&0\\
0&\gamma&-1
\end{pmatrix},
\]

one has

\[
N_{OO}(t)<0
\]

for every finite `t>=0` whenever `lambda>0`, while the reference denominator is positive.

At the exact gate `lambda=gamma=delta=1`, `e^{-t}=1/2`,

\[
N_{OO}=-5/16,
\qquad D_{OO}=5/16,
\qquad C_{OO}=-1.
\]

A bounded second candidate, spatial SIRS, has the same obstruction.

### Catalytic-birth no-go

Assignment 009 isolates the general mechanism:

> If a positive nonempty target mode appears in `0->r` but not in any active-source transition into `r`, then `a_r^r(tau)<0`. If the same source-`r` successful record can repeat after hidden outcome `r`, a realized arbitrarily short `OO` patch is negative.

This rules out a broad family of contact/epidemic catalytic-birth applications before any spectral work.

The two-stage model already has strong Krone/Foxall/Sturm--Swart duality theory, so no new model-level duality or convergence theorem is claimed. The killed typed representation is genuinely different but fails its positivity layer here.

Decisive files: `009a`--`009e`, verifier `009-two-stage-application-verifier.py`, final report, handoff, and Meeting 009.

## E10. Structurally distinct application architecture

**Open and current load-bearing edge if the programme continues.**

Repeating contact/SIRS-style catalytic birth models is low-value because E9's no-go decides them locally.

The next bounded application question should be:

> Is there a natural published genuinely three-state single-site replacement IPS in which neighbour interactions retype already-active states, or otherwise contain compensating active-source target modes, so the catalytic-birth no-go does not determine positivity in advance?

Model selection must again be literature-driven and committed before any positivity calculation. The model must not be chosen because its coefficients flatter the criterion.

A good candidate family would have genuinely interacting active labels, not a passive color or a deterministic voter-copying system whose duality is already entirely standard.

## E11. Generic `d>3` tractable positivity

**Deferred.**

The representation already holds for arbitrary finite `d`. Higher-order coefficient characterization overlaps established external-positivity theory and is not next by default.

Activate only if a concrete application needs more than three states or a structured higher-dimensional class has independent value.

## E12. Comparison/convergence and multi-site physical updates

**Downstream.**

Do not transplant binary comparison/convergence automatically. Simultaneous multi-site physical updates remain outside the proved representation class.

## Current novelty framing

Do not claim novelty for finite-state duality, signed FK duality, partial Poisson revelation, Metzler semigroups, or scalar external positivity individually.

The plausible contribution is the killed typed patch **interface**. Assignment 009 shows that this interface can occur naturally even when patch positivity fails, and supplies a structural no-go that should guide any further application search.
