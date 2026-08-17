# Meeting 010: Potts Metropolis activates killed geometry but fails typed patch positivity

Date: 2026-08-17

`state_narrowed: yes`.

Evidence:

- literature-driven selection committed before positivity: `students/professor/010a-literature-driven-structural-selection.md`, commit `b56c10d4`;
- exact typed specialization: `010b-potts-metropolis-typed-specialization.md`, commit `b1b2a995`;
- exact short-patch obstruction and generalized contrast lemma: `010c-potts-metropolis-patch-positivity-obstruction.md`, commit `b4b5eca6`;
- exact verifier: `010-potts-metropolis-verifier.py`, commit `34afe2d4`;
- application-specific prior-work ruling: `010d-potts-prior-work-and-application-value.md`, commit `5ffd0c89`;
- final report `010-structurally-distinct-application.md`, commit `436ce4cf`;
- handoff `010-handoff.md`, commit `39253aba`.

## Ruling

Assignment 010 ends

**`STOP-SECOND-APPLICATION-POSITIVITY-FAILS`.**

The failure is nondegenerate: the selected model genuinely activates non-deterministic hidden marks, active-type retyping, and realizable typed cemetery conflicts.

## 1. Model selection was independent of positivity

The three-state zero-field ferromagnetic Potts model with single-spin Metropolis Glauber dynamics was selected from a bounded structurally distinct candidate set before any typed positivity calculation.

It was preferred to the cyclic particle system because Potts Metropolis has source-dependent, neighborhood-sensitive active-to-active replacement rather than a deterministic invasion/copy arrow. Irreducibility was recorded but not used as a selection criterion.

## 2. Exact specialization genuinely uses the killed typed mechanism

For source dual type `1` and a singleton target-neighbor of type `1`,

\[
\mathbf a_{1;1,0}
=
\left(
qz^2(1-z^2),
q(z-1)(z^3+z^2-1),
-qz^2(1-z^2)
\right),
\qquad z=e^{-\beta J}.
\]

For every `0<z<1`, hidden outcomes `0` and `2` both have positive absolute rate. The coarse successful record therefore genuinely forgets post-source information.

Typed target conflicts are realizable: a target requiring active type `1` can meet an already active type `2` produced by the same hidden mechanism or by empty-target retyping. Thus cemetery and the killed/noncemetery repair are not cosmetic.

## 3. Positivity nevertheless fails throughout the interacting finite-temperature regime

The decisive active hidden coefficient is

\[
a_1^2(\tau)
=\widehat c^{2\to1}(\tau)-\widehat c^{0\to1}(\tau)
=-qz^2(1-z^2)<0.
\]

The physical reason is Metropolis saturation:

\[
\widehat c^{0\to1}(\tau)=qz^2(1-z^2)>0,
\qquad
\widehat c^{2\to1}(\tau)=0.
\]

The hidden outcome `2` can be followed by a positive-hazard source-type-2 successful record, so the corresponding `OO` descriptor is realized at arbitrarily small positive lengths. Its numerator has negative zero-length limit and hence is negative for sufficiently short positive lengths.

Therefore typed patch positivity fails for every

\[
q>0,
\qquad0<z<1.
\]

The `z=1` boundary is neighborhood-independent pure refresh and has no nonempty successful interactions.

## 4. Exact finite gate

At

\[
z=1/2,
\qquad q=1,
\]

\[
p=(3/16,5/16,-3/16),
\]

\[
K=
\begin{pmatrix}
0&0&0\\
1/16&-33/16&15/16\\
1/16&15/16&-33/16
\end{pmatrix}.
\]

At

\[
t_*=(8/3)\log(5/4),
\]

\[
N_{OO}(t_*)=-3884/390625<0.
\]

The exact verifier reconstructs all six physical rates on all `3^4` neighbor configurations and independently reconstructs the typed generator before checking this finite-length obstruction.

## 5. The obstruction broadens Assignment 009's no-go

Assignment 009 isolated a catalytic-birth obstruction. Assignment 010 shows that the true local sign mechanism is broader.

For active types `r!=s`, if

\[
a_r^s(\tau)
=\widehat c^{s\to r}(\tau)-\widehat c^{0\to r}(\tau)<0
\]

and the hidden outcome `s` can feed a subsequent source-`s` successful record, then a realized arbitrarily short `OO` patch is negative.

This can happen even when:

- every physical state is active;
- every directed physical replacement has positive rate;
- the interaction is color symmetric;
- active states retype each other directly.

Thus the failure is not specific to vacancy/contact models.

## 6. Opportunity-cost ruling

Assignments 009 and 010 have now tested two materially distinct natural three-state application architectures:

1. contact/epidemic birth plus active conversion;
2. fully active symmetric Metropolis retyping.

Both genuinely activate hidden marks, and both fail typed patch positivity through realized short `OO` signs.

This substantially lowers the expected value of another search for a natural patch-positive multistate model. A third application search is **not** opened automatically.

Generic `d>3` coefficient algebra also remains deferred.

The representation theorem itself remains mathematically intact and retains Assignment 008's plausible novelty status. If the programme continues, the next scientifically distinct question is whether the killed typed patch representation can yield useful cancellation/representation consequences **without bulk patch positivity**. That question requires an explicit opportunity-cost decision after independent verification of this block; no Assignment 011 is queued here.
