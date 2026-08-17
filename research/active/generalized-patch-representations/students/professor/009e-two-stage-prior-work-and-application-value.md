# 009e: prior work and application value for the two-stage contact process

Date: 2026-08-17

This note executes Parts D--E of Assignment 009 after the selected model has been proved not typed patch positive on its interacting parameter range.

## 1. Existing duality and graphical theory is strong

The two-stage contact process was not chosen because it lacked a duality theory. The opposite is true.

### Krone 1999

Krone introduced the model and constructed a multitype dual process as a central tool in its analysis.

Source: S. M. Krone, *The two-stage contact process*, Ann. Appl. Probab. 9 (1999), 331--351, DOI 10.1214/aoap/1029962745.

### Foxall

Foxall later gave a simplified proof of Krone's duality relation and resolved most of the open questions posed in the original paper.

Source: E. Foxall, *New Results for the Two-Stage Contact Process*, J. Appl. Probab.; arXiv:1401.2570.

Foxall also placed the model inside a broader class of additive multitype growth models, proving that additivity is equivalent to existence of an appropriate dual, giving graphical/percolative descriptions, a positive-correlation criterion, and complete convergence for a large subclass including the two-stage contact process.

Source: E. Foxall, *Duality and Complete Convergence for Multi-Type Additive Growth Models*, Adv. Appl. Probab. 48 (2016), 32--51; arXiv:1410.4809.

### General pathwise duality

Sturm--Swart's general theory of pathwise duals of monotone and additive Markov processes explicitly includes the duality due to Krone for the two-stage contact process among its examples.

Thus neither multitype graphical duality, additivity, nor complete convergence is available as a novelty claim for the present application.

## 2. What the typed killed-patch representation does differently

The specialization in `009b` is not merely Krone/Foxall notation.

For each adult-neighbour target, the selected typed successful record has signed hidden row

\[
(\lambda,-\lambda,-\lambda),
\]

so it hides three post-source possibilities:

- deletion to reference state `0`;
- persistence as juvenile type `1`;
- retyping to adult type `2`.

An incoming target carries adult type `2`. It conflicts with an existing type-1 active label and sends the typed dual to cemetery. Such a conflict is actually realizable in the two-stage process.

Consequently the exact representation uses the Assignment-002 killed/noncemetery factorization rather than a bare product law conditioned only on the successful record list.

This is a genuinely different representation interface from the standard additive dual. It tests the surviving novelty anchor from Assignment 008 in a natural published model.

## 3. But the positivity mechanism fails before it yields a consequence

The realized consecutive-source `OO` bulk numerator is strictly negative for every interacting parameter value `lambda>0`, by `009c`:

\[
N_{OO}(t)<0\qquad(t\ge0).
\]

The denominator is strictly positive. Hence the model is not typed patch positive anywhere in its nontrivial birth range.

Therefore the generalized patch representation cannot presently yield, for the base two-stage model,

- a patch-positive signed/centered moment order;
- a patch-positive parameter comparison;
- a patch-positive invariant-limit reduction;
- a direct transplant of the binary pure-death convergence theorem.

No downstream end-factor/order theorem can repair this, because the failure is already a negative **bulk** contribution.

## 4. Comparison with known model consequences

Known theory already supplies strong consequences by additive duality and graphical methods: survival/extinction information, monotonicity in model parameters, upper invariant-measure statements, and complete convergence for the two-stage process.

The typed representation does reproduce the physical generator exactly and gives a new local decomposition with cemetery-aware conditioning, but in this model its positivity test rejects the process rather than yielding an additional monotonicity or convergence theorem.

Accordingly:

> the application does **not** produce a new model-specific theorem beyond known duality/coupling results.

The mathematically useful information from this block is negative and structural: the generalized patch formalism exposes why a broad catalytic-birth architecture is incompatible with typed patch positivity in the reference-state indicator basis.

## 5. Structural lesson from the second candidate

The bounded SIRS check in `009d` shows the same outgoing hidden-row obstruction in a materially different cyclic epidemic model. Therefore the failure is not caused by Krone additivity, stage-dependent death, or the choice of adult target type.

The common mechanism is:

\[
0\to r
\]

at a positive neighbour-dependent target mode, with no compensating target-mode transition into `r` from active source states. The indicator-basis expansion then forces

\[
a_r^r(\tau)<0,
\]

and if the same source-type record can repeat, an arbitrarily short realized `OO` patch is negative.

This no-go statement is a useful filter for future applications: many contact/epidemic models built from catalytic birth into an active state will fail typed patch positivity immediately, even though their killed typed patch representation remains valid.

## 6. Application ruling

The selected natural model fails typed patch positivity for an exact structural reason across its natural interacting range, and a materially different second candidate has the same obstruction.

The pre-registered Assignment-009 outcome is therefore

\[
\boxed{\texttt{STOP-APPLICATION-POSITIVITY-FAILS}.}
\]

This is an application-level stop, not a refutation of the generalized representation. Assignments 001--004 and the surviving novelty status of killed typed factorization remain intact.
