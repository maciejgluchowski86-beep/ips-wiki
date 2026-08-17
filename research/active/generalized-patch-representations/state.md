# Programme state

Date: 2026-08-17

## Active direction

Generalize the canonical binary patch-representation / patch-positivity framework beyond binary flip spin systems.

Branch: `research/generalized-patch-representations`.

Workspace: `research/active/generalized-patch-representations/`.

Branch-only wiki section:

- `docs/generalized-patch-representations.md`;
- `docs/generalized-patch-representations/`.

Nothing from this programme is to be written or merged to `main` without a later principal instruction.

Latest meeting: `meetings/009-natural-contact-and-sirs-applications-fail-positivity.md`.

## Stable mathematical stack

Assignments 001--004 establish for arbitrary finite-state bounded finite-range **single-site replacement** IPS in the reference-state indicator tensor basis:

1. an exact typed signed Feynman--Kac dual;
2. successful records `(i,t,r,tau)` hiding post-source outcome;
3. exact killed/noncemetery patch factorization despite typed target conflicts;
4. an explicit typed patch representation with bulk/end separation;
5. exact local transfer
   \[
   K_i(0,\cdot)=0,
   \qquad K_i(r,s)=a_{i,r}^s(\emptyset);
   \]
6. typed bulk patch positivity as exact nonnegativity of local semigroup boundary responses;
7. exact binary reduction to canonical patch positivity.

Assignments 005--007 analyze controlled `d=3` positivity. Their mathematics remains correct, but Assignment 008 removed the generic scalar spectral theorem from the novelty claim because third-order external positivity is direct prior art.

## Assignment 008 novelty ruling

Outcome: **`CONTINUE-TO-APPLICATIONS`**.

Primary plausible novelty anchor:

\[
\text{signed typed dual}
\to
\text{hidden successful skeleton}
\to
\text{typed cemetery obstruction}
\to
\text{killed/noncemetery patch factorization}
\to
\text{exact finite-state patch representation}.
\]

Finite-state duality, signed FK duality, partial graphical revelation, matrix external positivity, and the generic third-order spectral criterion are not novelty claims.

## Assignment 009: first natural applications

Outcome: **`STOP-APPLICATION-POSITIVITY-FAILS`**.

### Literature-driven selection

Krone's **two-stage contact process** was selected before any positivity calculation from a bounded set containing spatial SIRS and Neuhauser's multitype contact process.

States:

\[
0=\text{vacant},\qquad1=\text{juvenile},\qquad2=\text{adult}.
\]

Physical rates:

\[
0\to1\text{ at }\lambda n_2(x),
\qquad1\to2\text{ at }\gamma,
\]

\[
1\to0\text{ at }1+\delta,
\qquad2\to0\text{ at }1.
\]

Selection used naturality, genuine three-state structure, single-site replacement, nontrivial graphical geometry, and strong prior duality literature. Patch positivity and irreducibility were not selection criteria.

### Exact typed specialization

For each adult-neighbour target `tau_j={j->2}`,

\[
\boxed{\mathbf a_{1,\tau_j}=(\lambda,-\lambda,-\lambda).}
\]

Empty-target rows are

\[
\mathbf a_{1,\emptyset}=(0,-(1+\delta+\gamma),0),
\]

\[
\mathbf a_{2,\emptyset}=(0,\gamma,-1),
\]

so

\[
K=
\begin{pmatrix}
0&0&0\\
0&-(1+\delta+\gamma)&0\\
0&\gamma&-1
\end{pmatrix}.
\]

Every successful record has source type `1`, target type `2`, and hides post-source outcome `0,1,2` with signs `+,-,-`. Incoming target type `2` can conflict with a type-1 active label, so typed cemetery and the killed-factorization repair are genuinely realized in this natural model.

### Exact positivity failure

A selected record can choose hidden outcome `1`, and the next successful record at the same source again requires pre-source type `1`. Thus a same-source `OO` descriptor is realized.

For `a=1+delta+gamma`, its numerator is

\[
N_{OO}(t)
=-\lambda\left[
e^{-at}+\gamma\frac{e^{-t}-e^{-at}}{a-1}
\right]
\]

when `a>1`, with the degenerate form `-lambda e^{-t}` when `a=1`.

Hence

\[
\boxed{N_{OO}(t)<0\quad\text{for all finite }t\ge0\text{ whenever }\lambda>0.}
\]

The killed-reference denominator is strictly positive. Therefore the published two-stage contact process is **not typed patch positive anywhere in its interacting birth range**.

Exact gate at

\[
\lambda=\gamma=\delta=1,
\qquad e^{-t}=1/2
\]

gives

\[
N_{OO}=-5/16,
\qquad D_{OO}=5/16,
\qquad C_{OO}=-1.
\]

Verifier: `students/professor/009-two-stage-application-verifier.py`, commit `d2576053`.

### Bounded second candidate

Spatial SIRS, with

\[
S\to I\text{ at }\lambda n_I,
\qquad I\to R,
\qquad R\to S,
\]

has the same nonempty outgoing row `(lambda,-lambda,-lambda)` and therefore the same realized negative repeated-source `OO` patch. No third candidate was opened.

### Catalytic-birth no-go

A reusable obstruction emerges:

> if a positive nonempty target mode appears in `0->r` but not in any active-source transition into `r`, then `a_r^r(tau)<0`; if the same source-`r` successful record can repeat after hidden outcome `r`, a realized arbitrarily short `OO` patch is negative.

This explains both the two-stage and SIRS failures and rules out a broad class of contact/epidemic growth models before any spectral calculation.

### Application-specific prior work

Krone already constructed the two-stage multitype dual; Foxall simplified it, proved further results and complete convergence in a general additive multitype growth framework; Sturm--Swart subsume Krone's duality in general pathwise duality.

The killed typed representation is genuinely different at the representation level and its cemetery mechanism is active here, but bulk positivity fails before it can yield a new model-specific comparison or convergence theorem.

Decisive files:

- `009a-literature-driven-model-selection.md`, `56ba8390`;
- `009b-two-stage-typed-specialization.md`, `232fe276`;
- `009c-two-stage-patch-positivity-obstruction.md`, `0174a59b`;
- verifier `009-two-stage-application-verifier.py`, `d2576053`;
- `009d-second-candidate-sirs-check.md`, `db0746f7`;
- `009e-two-stage-prior-work-and-application-value.md`, `423bee8e`;
- final report `009-natural-nonbinary-application.md`, `3d092827`;
- handoff `009-handoff.md`, `8d5305ed`;
- Meeting 009, `d9e8923b`.

## Current proof-spine edge

**One structurally distinct non-catalytic application class, if the programme continues.**

Repeating contact/SIRS-style catalytic birth models is now low-value because the no-go lemma decides them locally.

A next application block should therefore be literature-driven and select a natural three-state single-site replacement IPS where neighbour interactions can retype already-active states or otherwise contain compensating active-source target modes. Model selection must again be committed before any positivity calculation.

This is not permission to design a rate table to satisfy the criterion.

Generic `d>3` positivity algebra remains deferred. The arbitrary finite-state representation is already proved, and Assignment 009 gives no reason to insert higher-dimensional abstraction before one genuinely different application architecture is tested.

## Scope and publication boundary

Current proved mathematical scope: arbitrary finite-state bounded finite-range single-site replacement dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

No content is to be promoted to `main` without later principal instruction. Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` are outside the active write surface.

All previously stopped programmes remain closed.