# Disjoint update blocks: one-block patch reduction

Date: 2026-08-19

This is a granular exploratory note. It does not modify `paper/`.

Consider the multi-site flip generator

\[
L f(\eta)=\sum_{Q\in\mathcal Q}c_Q(\eta)\bigl(f(\eta^Q)-f(\eta)\bigr),
\]

where the allowed update blocks `Q` form a partition `\mathcal Q` of `\Lambda`, each block is finite, and the block sizes are uniformly bounded. The rates are local and bounded, with

\[
c_Q(\eta)=\sum_{S\subseteq N(Q)}c_Q(S)\chi_S(\eta).
\]

The point of the partition assumption is that every dual site belongs to a unique source block. This removes the cross-source ambiguity responsible for general hyperpatches.

## 1. Canonical block-local dual coefficients

For a dual monomial `chi_B`, write

\[
D=B\cap Q.
\]

If `D=emptyset`, flipping `Q` leaves `chi_B` unchanged and block `Q` contributes nothing.

For `D ne emptyset`, let

\[
\theta_D(J)=(-1)^{|J|}\quad(J\ne D),
\qquad
\theta_D(D)=(-1)^{|D|}-1.
\]

For a rate mode `S`, split

\[
S_Q=S\cap Q,
\qquad
T=S\setminus Q.
\]

If `S cap D ne emptyset`, then the flipped term vanishes and

\[
\chi_S\bigl(\chi_B(\eta^Q)-\chi_B(\eta)\bigr)
=-\chi_{B\cup S}.
\]

Thus the source block ends in local state

\[
R=D\cup S_Q
\]

with coefficient `-c_Q(S)`.

If `S cap D=emptyset`, then

\[
\chi_S\bigl(\chi_B(\eta^Q)-\chi_B(\eta)\bigr)
=\sum_{J\subseteq D}\theta_D(J)
\chi_{(B\setminus Q)\cup J\cup S_Q\cup T}.
\]

The local source-block outcome is

\[
R=J\cup S_Q.
\]

It is therefore natural to aggregate over internal rate modes and define, for external target `T subseteq Lambda\setminus Q`, pre-source state `D subseteq Q`, and post-source state `R subseteq Q`,

\[
a_{Q,D}^{R}(T)
=\sum_{\substack{S\subseteq N(Q)\\S\setminus Q=T}}
 c_Q(S)\,g_{D,S}(R),
\]

where

\[
g_{D,S}(R)=
\begin{cases}
-1,
& S\cap D\ne\varnothing,
\ R=D\cup S_Q,\\
\theta_D(J),
& S\cap D=\varnothing,
\ R=J\cup S_Q\text{ for }J\subseteq D,\\
0,&\text{otherwise}.
\end{cases}
\]

Then exactly

\[
\boxed{
L\chi_B
=
\sum_{Q\in\mathcal Q:\,B\cap Q\ne\varnothing}
\sum_T\sum_{R\subseteq Q}
 a_{Q,B\cap Q}^{R}(T)
 \chi_{(B\setminus Q)\cup R\cup T}.
}
\]

This is the useful normal form. At the dual level, each block is a finite local state space

\[
E_Q=\mathcal P(Q),
\]

with inactive state `emptyset`.

For `T=emptyset`, the coefficients are purely local block transitions. For `T ne emptyset`, they are block interactions with an external target.

As usual, represent every off-diagonal coefficient by a clock of rate `|a|` and sign `sgn(a)`, and put the diagonal empty-target coefficient into the Feynman--Kac potential. Thus, for `D ne emptyset`,

\[
v_Q(D)
=\sum_{(R,T)\ne(D,\emptyset)}|a_{Q,D}^{R}(T)|
+a_{Q,D}^{D}(\emptyset),
\qquad
v_Q(\emptyset)=0.
\]

The global potential is block-additive:

\[
V(B)=\sum_{Q\in\mathcal Q}v_Q(B\cap Q).
\]

## 2. The right successful record

A coarse successful nonempty-target source record should reveal

\[
(Q,t,D,T),
\qquad
D=B_{t-}\cap Q\ne\emptyset,
\qquad
T\ne\emptyset,
\]

and hide the selected post-source state `R subseteq Q`, whose conditional law is proportional to

\[
|a_{Q,D}^{R}(T)|.
\]

This is not yet enough to recover one-block conditional factorization, because an incoming target need not determine the full state of a target block.

For every target block `Q' ne Q` with

\[
T_{Q'}=T\cap Q'\ne\emptyset,
\]

let

\[
E_{Q'}=B_{t-}\cap Q'
\]

be its pre-incoming local dual state. Enlarge the successful record to include all these finite boundary labels:

\[
\boxed{
\mathfrak r
=\left(Q,t,D,T;\,(E_{Q'})_{Q':T\cap Q'\ne\emptyset}\right).
}
\]

After the interaction, target block `Q'` starts from the deterministic state

\[
E_{Q'}\cup T_{Q'}.
\]

The hidden source state `R` remains unrecorded, so the intended local cancellation at the source is preserved.

This is the exact analogue of revealing the pre-source type in the finite-state typed construction: the boundary state is part of the skeleton, while the signed post-source outcome remains hidden inside the next source patch.

## 3. One-block patches

For each block `Q`, cut its time line at every successful incidence involving `Q`:

- an outgoing incidence when `Q` is the source;
- an incoming incidence when `Q` contains some site of the external target `T`.

A block patch is one interval between consecutive such incidences.

Its local process is

\[
X_u^P\in\mathcal P(Q).
\]

The initial state is:

- fixed to `E_Q union T_Q` after an incoming start;
- the hidden selected post-source state `R` after an outgoing start.

The terminal consistency condition is:

- `X_{e-}=D` if the next boundary is outgoing and its record reveals source pre-state `D`;
- `X_{e-}=E_Q` if the next boundary is incoming and its record reveals target-block pre-state `E_Q`;
- no terminal condition at the time horizon.

Inside the patch, only empty-external-target clocks `T=emptyset` may act without producing a skeleton record. Every unselected `T ne emptyset` clock is required to be unsuccessful, which is a condition only on the current block state `X_{u-}` and the clock's pre-source label `D`.

Therefore **every consistency condition for a block patch is local to that block-time strip** once the enlarged boundary states are included in the skeleton.

Distinct block patches use disjoint time restrictions of independent block-clock families and independent hidden outcomes at their outgoing initial records. This is exactly the structural input used in the paper's one-site Mecke proof.

Hence the expected factorization theorem is the direct block analogue:

> conditional on the enriched successful skeleton, the hidden variables of distinct block patches are independent and have their reference laws conditioned on the corresponding local consistency events.

This has not yet been written as a line-by-line proof, but unlike the general overlapping-block hyperpatch claim it appears to require only notational modification of the paper's argument.

## 4. Pathwise FK factorization

The block-additive potential gives

\[
\int_0^tV(B_u)\,du
=\sum_P\int_{s(P)}^{e(P)\wedge t}v_{Q(P)}(X_u^P)\,du.
\]

Every selected nonempty-target branch sign belongs to the unique outgoing-start block patch at its source. Every effective empty-target branch sign belongs to one patch interior.

At the terminal horizon, the monomial factor decomposes over the disjoint blocks:

\[
\chi_{B_t}(\eta)
=\prod_{P\in\mathcal E_t}
\chi_{X_t^P}(\eta_{Q(P)}).
\]

Thus the exact FK variable factors pathwise over block patches. After conditional averaging one obtains the same formal representation as in the paper, with one-site factors replaced by one-block factors.

For a completed block patch `P`, write its scalar averaged factor as `C(P)`. For an end patch on block `Q`, the contribution is the multilinear polynomial

\[
C_Q(z,P)
=E_P^{con}\left[
A_P\prod_{i\in X_t^P}z_i
\right],
\qquad z=(z_i)_{i\in Q}.
\]

For Bernoulli product initial law of profile `p`, simply evaluate this polynomial at `z_i=p_i`.

## 5. Positivity consequences in the disjoint-block class

There is a clean abstract bulk condition:

\[
C(P)\ge0
\]

for every completed block patch.

Because `|Q|` is uniformly bounded, every local block process has uniformly bounded finite state space. Empty-target transfer is a finite matrix indexed by subsets of `Q`; outgoing records give signed boundary rows. Thus all bulk positivity tests are finite-dimensional with dimension at most `2^{sup |Q|}`.

This is much closer to the current paper than the generic hyperpatch problem, although one should not expect the two scalar coefficient inequalities from the singleton case.

For centered-moment order, the end factor has centered expansion

\[
C_Q(z,P)
=\sum_{R\subseteq Q}
\kappa_R(P)
\prod_{i\in R}(z_i-p_i^*).
\]

If all bulk factors are nonnegative and every end-patch coefficient satisfies

\[
\kappa_R(P)\ge0,
\]

including `R=emptyset`, then the paper's centered-end expansion works block by block. Since terminal block patches have disjoint physical supports, multiplying these expansions again produces only nonnegative coefficients of global centered monomials. Under this strengthened block-end condition, preservation of the centered-moment cone and order should carry over with minimal changes.

A coordinatewise scalar threshold formula is not automatic: admissibility is now a finite family of inequalities for each block end polynomial.

## 6. What this special case does and does not buy

This disjoint-block class is the first multi-site subclass in which the existing paper proof architecture survives almost literally:

- finite local source state instead of a single active bit;
- enriched boundary labels instead of only `I/O`;
- scalar bulk contribution per block patch;
- multilinear rather than affine end contribution.

No spacetime hyperpatch gluing is needed.

It still does **not** automatically restore the paper's pure-death comparison or convergence theorem. Independent physical `1->0` noise changes the local block FK weight by

\[
\exp\left(-\varepsilon\int |X_u^P|\,du\right),
\]

which varies across hidden block histories. Even if both averaged block contributions are nonnegative, monotonicity under changing `epsilon` does not follow from positivity alone. A stronger death-monotonicity/Laplace-positivity property would be needed.

The next useful calculation is therefore local rather than global: write the exact finite matrix formulas for the four basic boundary orientations in the simplest nontrivial case `|Q|=2`, and see whether bulk positivity plus centered end positivity has a tractable coefficient form. Standard overlapping-edge models such as Kawasaki dynamics are *not* covered by the partition assumption and should be treated later using the general hyperpatch construction.
