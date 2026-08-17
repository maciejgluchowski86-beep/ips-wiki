# Assignment 009 report: natural nonbinary application

Date: 2026-08-17

Outcome:

\[
\boxed{\texttt{STOP-APPLICATION-POSITIVITY-FAILS}.}
\]

## 1. Goal

Test the killed typed patch representation on a natural published genuinely three-state single-site replacement IPS, with model selection fixed before any patch-positivity calculation.

## 2. Literature-first model selection

Three published candidates were compared before computing typed coefficients:

1. Krone's two-stage contact process;
2. the spatial stochastic SIRS process;
3. Neuhauser's multitype contact process.

The **two-stage contact process** was selected because it is a classical rigorous IPS, genuinely requires all three states, uses only single-site replacements, combines neighbour-driven reproduction with local active-type conversion, and has an established nontrivial multitype-duality literature. Patch positivity was not evaluated or used in the selection.

The physical states and rates are

\[
0=\text{vacant},\quad1=\text{juvenile},\quad2=\text{adult},
\]

\[
0\to1 \text{ at rate }\lambda n_2(x),
\qquad1\to2 \text{ at rate }\gamma,
\]

\[
1\to0 \text{ at rate }1+\delta,
\qquad2\to0 \text{ at rate }1.
\]

The all-vacant state is absorbing; irreducibility played no role in selection.

Decisive selection note: `009a-literature-driven-model-selection.md`, commit `56ba8390`.

## 3. Exact typed specialization

Use vacancy as reference state `0`. For each neighbour `j`, let

\[
\tau_j=\{j\mapsto2\}.
\]

The only nonzero nonempty physical tensor coefficient is

\[
\widehat c^{0\to1}(\tau_j)=\lambda.
\]

The exact dual rows are

\[
\boxed{
\mathbf a_{1,\emptyset}
=(0,-(1+\delta+\gamma),0),}
\]

\[
\boxed{
\mathbf a_{2,\emptyset}
=(0,\gamma,-1),}
\]

and, for every adult-neighbour target,

\[
\boxed{
\mathbf a_{1,\tau_j}
=(\lambda,-\lambda,-\lambda).}
\]

Thus the signed interior transfer is

\[
\boxed{
K=
\begin{pmatrix}
0&0&0\\
0&-(1+\delta+\gamma)&0\\
0&\gamma&-1
\end{pmatrix}.}
\]

Every successful record has source type `1`, target type `2`, and hides post-source outcome

\[
S\in\{0,1,2\}
\]

with reference probabilities `1/3,1/3,1/3` and signs `+,-,-`.

Typed cemetery conflicts are genuinely realizable: an incoming target type `2` conflicts with an existing type-1 active label. Hence the killed/noncemetery factorization is operative rather than vacuous in this model.

Decisive specialization note: `009b-two-stage-typed-specialization.md`, commit `232fe276`.

## 4. Exact patch-positivity obstruction

Write

\[
a=1+\delta+\gamma,
\qquad
p=\lambda(1,-1,-1).
\]

A selected outgoing record can choose hidden outcome `S=1` with positive reference probability. The next successful record at the same source again requires pre-source type `1`. Therefore the corresponding outgoing-to-outgoing bulk descriptor is realized.

Its numerator is

\[
N_{OO}(t)=p e^{tK}e_1^T.
\]

For `a>1`,

\[
\boxed{
N_{OO}(t)
=-\lambda\left[
e^{-at}
+\gamma\frac{e^{-t}-e^{-at}}{a-1}
\right]<0.}
\]

If `a=1`, necessarily `gamma=delta=0`, and

\[
N_{OO}(t)=-\lambda e^{-t}<0.
\]

The killed-reference denominator is strictly positive for every finite patch length whenever `lambda>0`.

Therefore

\[
\boxed{
\text{the two-stage contact process is not typed patch positive for any }\lambda>0.}
\]

The failure is already visible at zero length:

\[
N_{OO}(0)=a_1^1(\tau_j)=-\lambda.
\]

The mechanism is an **outgoing hidden-row sign obstruction**, not an interior external-positivity transient and not cemetery geometry.

Decisive obstruction note: `009c-two-stage-patch-positivity-obstruction.md`, commit `0174a59b`.

## 5. Mandatory exact gate

At the published-model interior parameter point

\[
\lambda=\gamma=\delta=1,
\]

the verifier checks exact physical-rate nonnegativity and reconstructs the physical generator from the typed coefficients on every source/neighbour state for both active indicator observables.

At the exact patch length defined by

\[
e^{-t}=1/2,
\]

the realized `OO` patch has

\[
N_{OO}=-5/16,
\qquad
D_{OO}=5/16,
\]

and hence exact contribution

\[
C_{OO}=-1.
\]

Verifier: `009-two-stage-application-verifier.py`, commit `d2576053`.

## 6. Bounded second candidate

The spatial SIRS process was retained in Part A as the materially different second candidate. With

\[
0=S,\quad1=I,\quad2=R,
\]

and transitions

\[
0\to1\text{ at }\lambda n_1,
\qquad1\to2\text{ at }\delta,
\qquad2\to0\text{ at }\gamma,
\]

its infection target mode gives the same outgoing signed row

\[
(\lambda,-\lambda,-\lambda).
\]

A realized repeated-source `OO` patch again has zero-length numerator `-lambda` and remains negative for every finite positive length.

Thus a cyclic epidemic model with a different target type and different local progression has the same obstruction. No third candidate was opened.

Decisive second-candidate note: `009d-second-candidate-sirs-check.md`, commit `db0746f7`.

## 7. Reusable catalytic-birth no-go lemma

The application exposes a general local obstruction.

Suppose a nonempty target mode `tau` and active type `r` satisfy

\[
\widehat c^{0\to r}(\tau)=b>0,
\]

while all target-mode coefficients into `r` from active source states vanish, and the same source-type successful record can occur again after hidden outcome `r`.

Then the typed row has

\[
\boxed{a_r^r(\tau)=-b<0.}
\]

Hence the realized zero-length `OO` numerator ending at source type `r` is negative, and typed patch positivity fails.

Both the two-stage contact process and spatial SIRS instantiate this lemma.

This is the main structural information learned from the application block.

## 8. Application-specific prior work

The two-stage process already has a strong duality and convergence theory:

- Krone constructed its multitype dual;
- Foxall simplified the duality proof and resolved most of Krone's open questions;
- Foxall's general additive multitype growth theory includes the two-stage model and proves complete convergence for a large subclass;
- Sturm--Swart's pathwise-duality framework explicitly includes Krone's duality.

Therefore ordinary graphical duality, additivity, survival/monotonicity statements, and complete convergence are not new consequences available to this application.

The typed killed-patch representation is genuinely different at the representation level: it hides a three-valued post-source mark and requires cemetery-aware killed factorization. But because bulk positivity fails, it supplies no additional patch-positive moment comparison, monotonicity, or convergence theorem for the base model.

Decisive prior-work note: `009e-two-stage-prior-work-and-application-value.md`, commit `423bee8e`.

## 9. Programme-level interpretation

This block answers the principal's application question negatively for the strongest literature-selected three-state growth model and one materially different epidemic model.

It does **not** refute the arbitrary finite-state killed typed representation proved in Assignments 001--004. Indeed, the two-stage specialization shows that its distinctive hidden-mark/cemetery mechanism occurs naturally.

What fails is the positivity layer for a broad and natural catalytic-birth architecture.

The correct next decision is therefore not to tune the two-stage model or append noise. If the programme continues application work, it should target a structurally different published family in which neighbour interactions do more than create an active type from the reference state, so that the catalytic-birth no-go lemma does not decide the answer in advance.
