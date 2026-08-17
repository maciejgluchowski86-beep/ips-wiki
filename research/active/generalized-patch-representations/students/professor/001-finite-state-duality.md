# Assignment 001 report: finite-state typed duality

Date: 2026-08-17

## Verdict

**`CONTINUE-TYPED-PATCH`.**

For every finite local state space with a distinguished reference state, the canonical reference-state indicator tensor basis gives an exact **local signed Feynman--Kac graphical dual** for completely general bounded single-site replacement rates depending on finite neighbourhoods.

The dual state is a finite typed active configuration, augmented by a cemetery/zero state for incompatible typed overlaps. The binary signed death/split/birth process is recovered exactly.

For nonempty typed targets, the branch clocks can be superposed into successful records

\[
(i,t,r,\tau),
\]

which retain the pre-interaction source type `r` and typed target `tau` but hide the finite post-interaction source outcome `s`. Deletion, survival, and retyping all have the same record endpoints, so the hidden mark does not obstruct patch geometry.

The next theorem is typed-skeleton conditional factorization. Patch positivity is not yet defined.

## 1. Canonical multi-state analogue of monomials

Let

\[
E=\{0,1,\ldots,d-1\},
\qquad E_*=E\setminus\{0\}.
\]

Use

\[
h_0\equiv1,
\qquad
h_a(x)=1_{\{x=a\}},\quad a\in E_*.
\]

For a finite typed partial map

\[
\xi:\Lambda\rightharpoonup E_*,
\]

put

\[
H_\xi(\eta)
=\prod_{i\in\operatorname{supp}\xi}1_{\{\eta_i=\xi(i)\}}.
\]

On `K` sites there are

\[
\sum_{A\subseteq K}(d-1)^{|A|}=d^{|K|}
\]

such functions, and explicit Boolean-lattice Möbius inversion proves that they form a basis of all functions on `E^K`.

If two typed partial maps agree on every overlap, their observables multiply by union. If they assign different non-reference types at one site, their product is zero. Adjoin `dagger` with `H_dagger=0` to encode this exactly.

## 2. General replacement generator

Consider

\[
L f(\eta)
=
\sum_i\sum_{x\ne y}
1_{\{\eta_i=x\}}c_i^{x\to y}(\eta_{N(i)})
\bigl[f(\eta^{i,y})-f(\eta)\bigr].
\]

Expand each neighbour rate as

\[
c_i^{x\to y}
=
\sum_\tau\widehat c_i^{x\to y}(\tau)H_\tau.
\]

Fix an active dual source type `r`. Only physical transitions entering or leaving `r` affect `H_xi`.

After using

\[
1_{\{\eta_i=0\}}
=1-\sum_{s\in E_*}1_{\{\eta_i=s\}},
\]

the exact signed coefficient for source outcome `s in E` and typed target `tau` is

\[
\boxed{
a_{i,r}^{0}(\tau)
=\widehat c_i^{0\to r}(\tau),}
\]

\[
\boxed{
a_{i,r}^{s}(\tau)
=
\widehat c_i^{s\to r}(\tau)
-
\widehat c_i^{0\to r}(\tau),
\quad s\in E_*\setminus\{r\},}
\]

\[
\boxed{
a_{i,r}^{r}(\tau)
=-\widehat c_i^{0\to r}(\tau)
-
\sum_{y\ne r}\widehat c_i^{r\to y}(\tau).}
\]

The local map removes the source, reinserts it with type `s` when `s ne 0`, and compatibly merges `tau`; conflict gives `dagger`.

Thus

\[
L H_\xi
=
\sum_{i\in\operatorname{supp}\xi}
\sum_\tau\sum_{s\in E}
 a_{i,\xi(i)}^s(\tau)
 H_{\Theta_{i;s,\tau}(\xi)}.
\]

Crucially, the coefficient and hence clock rate is independent of the rest of `xi`. Existing typed targets affect only the deterministic merge result.

## 3. Fixed local signed graphical dual

For every tuple `(i,r,s,tau)` except the empty-target source-survival tuple `(s,tau)=(r,empty)`, use rate and sign

\[
\lambda_{i,r}^s(\tau)=|a_{i,r}^s(\tau)|,
\qquad
\epsilon_{i,r}^s(\tau)=\operatorname{sgn}_{\pm}(a_{i,r}^s(\tau)).
\]

A clock acts only when the current source has dual type `r`. It applies `Theta` and multiplies the sign by `epsilon`.

Define

\[
V(\xi)
=
\sum_{i\in\operatorname{supp}\xi}
\left[
\sum_{(s,\tau)\ne(\xi(i),\emptyset)}
|a_{i,\xi(i)}^s(\tau)|
+
a_{i,\xi(i)}^{\xi(i)}(\emptyset)
\right].
\]

Then exactly

\[
\boxed{
L_\eta H(Y,\eta)
=D H(Y,\eta)+V(\xi)H(Y,\eta).}
\]

With finite state space, uniformly bounded neighbourhood size and physical rates, the dual jump rate per active site is uniformly bounded and each jump creates only boundedly many new active sites. Hence the dual is nonexplosive.

For infinite-volume Feynman--Kac duality, retain the same type of exponential-integrability hypothesis as in the canonical binary paper. Nonexplosion alone is not claimed to imply that hypothesis.

## 4. Exact binary recovery

For `E={0,1}`, the unique active type is `r=1`, and a typed target is just a subset `S`.

The source-deletion coefficient is

\[
a_{i,1}^{0}(S)=c_i^0(S),
\]

which is the paper's death/split coefficient.

The source-survival coefficient is

\[
a_{i,1}^{1}(S)=-c_i^0(S)-c_i^1(S),
\]

which is the paper's birth coefficient.

Thus:

- deletion + empty target = death;
- deletion + nonempty target = split;
- survival + nonempty target = birth;
- survival + empty target = the diagonal coefficient placed in the potential.

No regrouping is needed.

## 5. New multi-state branch: retyping

For `d>2`, there are genuine source-retyping branches

\[
s\in E_*\setminus\{r\},
\]

with coefficient

\[
\widehat c_i^{s\to r}(\tau)
-
\widehat c_i^{0\to r}(\tau).
\]

This is the first structural difference from the binary set process. The hidden local mark is no longer merely survive/delete; it is a finite source outcome in `E`.

## 6. Coarse successful-interaction record

For nonempty `tau`, superpose all source-outcome clocks at fixed `(i,r,tau)`:

\[
\Lambda_{i,r}(\tau)
=
\sum_{s\in E}|a_{i,r}^s(\tau)|.
\]

Conditional on a superposed point, the hidden outcome has probability proportional to the corresponding absolute coefficient.

The successful record is

\[
\boxed{(i,t,r,\tau)}
\]

when the pre-interaction dual source type is `r`.

All hidden outcomes have the same spacetime endpoints:

- outgoing endpoint at `i`;
- incoming endpoints at every site in `supp tau`.

Therefore deletion/survival/retyping does not change patch geometry.

The source type `r` should normally be revealed. Its aggregate intensity and outgoing consistency condition generally depend on `r`; hiding it would push state dependence across the preceding patch boundary. In the binary case `r` is unique and disappears, recovering `(i,t,S)`.

Typed target conflicts do not change the record geometry and do not alter the fixed clock rate, but they can send the dual to `dagger`. Their effect on conditional factorization is the main next issue.

## 7. Exact finite verifier

`001-finite-state-duality-verifier.py` checks:

- the full `d=3`, one-neighbour elementary family;
- both active source types;
- all six physical transitions;
- all three neighbour tensor modes;
- absent/same/conflicting existing target labels;
- all nine physical two-site configurations;
- direct generator action = typed coefficient expansion = signed graphical generator plus potential;
- exact `d=2` specialization;
- branch-independent nonempty-target record geometry;
- an explicit example in which the superposed record intensity depends on source type.

The core `d=3` generator/FK comparison contains 972 exact configuration checks.

## 8. Scope and novelty

This block proves a structural extension of the binary algebra to arbitrary finite state space and general single-site replacement rates. It has **not** yet undergone an external literature/novelty audit, so no claim is made here that the abstract typed duality theorem is new in the literature.

What matters for the programme is that the dual is local and has the correct hidden-mark structure to justify continuing to the patch-factorization question.

## Decision

Assignment 001 ends

**`CONTINUE-TYPED-PATCH`.**

Next bridge: generalized typed successful-skeleton conditional factorization, with cemetery/target-compatibility treated explicitly. Do not define generalized patch positivity before that factorization is proved or refuted.
