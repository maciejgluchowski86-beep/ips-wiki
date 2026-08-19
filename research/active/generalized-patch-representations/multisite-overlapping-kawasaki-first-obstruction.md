# Overlapping Kawasaki blocks: first obstruction to the existing patch proof

Date: 2026-08-19

This note does one thing only: test the existing paper proof on a standard overlapping-edge exchange architecture and stop at the first step which genuinely fails. It does not attempt a workaround.

## Test model

Take nearest-neighbour exchange on edges. The clean zero-energy case (SSEP) is too degenerate for the signed-patch question: its monomial dual is itself an exclusion process with positive rates and no Feynman--Kac sign cancellation. To expose the first nontrivial issue while keeping the same Kawasaki geometry, modulate one edge exchange by one external spin.

For an edge `e={x,y}` and an external site `k`, consider

\[
L_e f(\eta)
=
1_{\{\eta_x\ne\eta_y\}}(1+\lambda\eta_k)
\bigl(f(\eta^e)-f(\eta)\bigr),
\qquad \lambda>0.
\]

On unequal endpoint configurations, flipping both endpoint spins is exactly exchanging them. This is a local Kawasaki-type exchange rule. The endpoint indicator is the usual exchange constraint; the factor `1+lambda eta_k` is the smallest nonconstant environmental dependence.

This slightly enlarges the user's formal `c_A` scope if `N(A)` is required to exclude the endpoints themselves. That bookkeeping issue is not the obstruction below: the obstruction comes from the nonconstant external mode `lambda eta_k` and remains for ordinary finite-range Kawasaki rates.

## Generator action

Let `B` be the support of a dual monomial. If either both or neither of `x,y` belong to `B`, exchanging `x,y` leaves `chi_B` unchanged. Suppose

\[
x\in B,\qquad y\notin B.
\]

Then

\[
1_{\{\eta_x\ne\eta_y\}}
\bigl(\chi_B(\eta^e)-\chi_B(\eta)\bigr)
=
\chi_{B\setminus\{x\}\cup\{y\}}-\chi_B.
\]

Hence

\[
L_e\chi_B
=
\bigl(\chi_{B-x+y}-\chi_B\bigr)
+
\lambda\bigl(
\chi_{(B-x+y)\cup\{k\}}
-
\chi_{B\cup\{k\}}
\bigr).
\]

The constant mode is harmless: it is exactly the generator of a positive exclusion jump `x->y`.

The first nonconstant mode is the decisive one:

\[
\boxed{
\lambda\chi_{(B-x+y)\cup\{k\}}
-
\lambda\chi_{B\cup\{k\}}.
}
\]

These are two genuinely off-diagonal monomials with opposite signs.

Thus the signed dual algebra itself still exists. One may regard the positive branch as

\[
B\longmapsto (B\setminus\{x\})\cup\{y,k\},
\]

and the negative branch as

\[
B\longmapsto B\cup\{k\}.
\]

Nothing has broken yet at the generator/Feynman--Kac level.

## How far the paper proof survives

The proof of the current paper proceeds schematically as follows.

1. Expand `L chi_B` into signed monomial transitions plus a diagonal potential.
2. Build the signed graphical dual.
3. Superpose selected nonempty-target branches into a successful record which hides the branch kind.
4. Because every hidden kind at a fixed record has the same target, the successful record still determines all incoming and outgoing patch boundaries.
5. Conditional on this geometry, define one local candidate process on each patch, express completeness of the skeleton as a product of local consistency events, and apply Mecke to factor the hidden marks.

For the Kawasaki mode above, steps 1--2 survive. Step 3 is where the first genuine obstruction appears.

## First real obstruction: branch kind determines the geometry

In the single-site paper, at a fixed source `i` and nonempty target `S`, the hidden split/death-vs-birth choice changes only whether the source survives. Both kinds activate exactly the same target `S`. Therefore the coarse record `(i,t,S)` can hide the sign-carrying kind while still determining:

- the outgoing boundary at `i`;
- every incoming boundary at sites in `S`;
- hence the entire patch geometry.

For the Kawasaki environmental mode, the two opposite-sign outcomes have different support geometry.

Positive branch:

\[
B\mapsto (B-x)\cup\{y,k\}.
\]

Negative branch:

\[
B\mapsto B\cup\{k\}.
\]

The positive branch removes `x` and activates `y`; the negative branch keeps `x` and does not activate `y`. Both add `k`.

Therefore there is no direct analogue of the paper's coarse successful record which simultaneously has the two required properties:

1. hide the sign-carrying branch choice so that the `+lambda` and `-lambda` contributions can be averaged locally before absolute values;
2. determine the spacetime patch boundaries.

If the record hides the branch, then after the record one does not know whether the active dual line continues at `x` or moves to `y`. The skeleton does not determine its own geometry.

If the record reveals the branch, the geometry is determined, but the signed `+/-` pair has already been separated at the skeleton level, so the exact cancellation which motivates patch averaging is lost.

This is earlier than the overlapping-Poisson-family problem and earlier than the Mecke factorization theorem. The old proof cannot even reach its definition of patch laws with the same information split between skeleton and hidden marks.

## Why SSEP does not show this

For `lambda=0`,

\[
L_e\chi_B=\chi_{B-x+y}-\chi_B,
\]

which is an honest positive Markov jump of the dual active set. The negative term is only the diagonal part of the exclusion generator. There is no hidden signed branch and hence no cancellation/geometry conflict. SSEP therefore gives a misleadingly easy overlapping-edge example.

The obstruction appears as soon as a nonconstant environmental mode produces two off-diagonal signed monomials, as ordinary interacting Kawasaki rates generically do after multilinear expansion.

## Relation to overlapping edge blocks

The edge blocks `e={x,y}` overlap on the lattice, and that causes an additional downstream issue: a change at a shared endpoint changes the local state of every incident edge block without an event on those other blocks. Thus disjoint-block patch laws cannot simply be reused.

But this is not the first failure. The first failure is already the geometry/cancellation conflict above: for a single selected exchange mode, the hidden signed outcome itself changes which endpoint carries the dual line.

Accordingly I stop here, as requested, rather than introducing hyperpatches, enriched boundary records, or another lifted dual to work around it.

## Bottom line

For genuinely interacting Kawasaki exchange, the existing paper proof survives through signed monomial duality and graphical realization. It first breaks at the successful-skeleton design.

The current paper relies on the special property

\[
\boxed{\text{hidden branch kind does not change the target geometry}.}
\]

Multi-site exchange loses that property. In the first nonconstant Kawasaki mode, hiding the sign-carrying outcome also hides whether dual activity stays at one endpoint or moves to the other. Hence the skeleton can no longer both retain the cancellation and determine the patches.
