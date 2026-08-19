# Multi-site flip extension of the binary patch construction

Date: 2026-08-19

This is a loose technical note, not a paper edit. It records the parts of the multi-site extension which look structurally correct enough to keep.

Consider a binary IPS

\[
L f(\eta)=\sum_{A\Subset\Lambda}c_A(\eta)\bigl(f(\eta^A)-f(\eta)\bigr),
\]

where `eta^A` flips all spins in `A`, and `c_A` depends only on

\[
N(A)=\bigcup_{i\in A}N(i).
\]

Assume the usual uniform bounded-arity/local-incidence hypotheses needed for a Harris construction and finite propagation. Expand

\[
c_A(\eta)=\sum_{S\subseteq N(A)}c_A(S)\chi_S(\eta).
\]

## 1. Exact monomial algebra

For a dual monomial `chi_B`, put

\[
D=A\cap B.
\]

Then

\[
\chi_B(\eta^A)
=\chi_{B\setminus D}(\eta)\prod_{i\in D}(1-\eta_i),
\]

so

\[
\chi_B(\eta^A)-\chi_B(\eta)
=\sum_{J\subseteq D}\theta_D(J)\chi_{(B\setminus D)\cup J}(\eta),
\]

where

\[
\theta_D(J)=(-1)^{|J|}\quad(J\neq D),
\qquad
\theta_D(D)=(-1)^{|D|}-1.
\]

Hence

\[
L\chi_B
=\sum_A\sum_{S\subseteq N(A)}\sum_{J\subseteq D}
 c_A(S)\theta_D(J)
 \chi_{(B\setminus D)\cup J\cup S},
\qquad D=A\cap B.
\]

This is the canonical monomial dual algebra. The corresponding signed dual transition is

\[
B\longmapsto (B\setminus D)\cup J\cup S
\]

with coefficient

\[
a_{A,D,J}(S)=c_A(S)\theta_D(J),
\]

applicable when `B cap A=D`. Absolute values give jump rates, signs give the sign coordinate, and the diagonal discrepancy is put into the Feynman--Kac potential as in the single-site paper.

For `|D|=1`, the two coefficients are `+1` for deletion and `-2` for source survival, exactly the source-independent single-site flip algebra. For `|D|>=2`, one physical flip gives a genuinely joint source-block branch.

At fixed `(A,D,S)`, the `J`-branches can be superposed. Their total absolute coefficient is

\[
\sum_{J\subseteq D}|\theta_D(J)|
=2^{|D|}-(-1)^{|D|}.
\]

Thus a successful coarse record can reveal `(A,t,D,S)` and hide the joint post-source subset `J`, with conditional law proportional to `|theta_D(J)|`.

The dual is no longer additive: applicability depends on the full pattern `B cap A`, not separately on the active source sites.

## 2. A useful lifted cylinder dual

There is also a cleaner exact lift which should be kept in mind, although it does not by itself give scalar patches.

Let a dual state be a finite partial assignment

\[
\xi:\Lambda\rightharpoonup\{0,1\},
\qquad
H_\xi(\eta)=\prod_{i\in\operatorname{supp}\xi}1_{\{\eta_i=\xi_i\}}.
\]

Let `T_A xi` toggle all assigned labels on `A`, and let `M_S` merge the constraint `eta=1` on `S`, with incompatible assignments sent to cemetery `dagger`. Then

\[
H_\xi(\eta^A)=H_{T_A\xi}(\eta)
\]

and therefore exactly

\[
\boxed{
L H_\xi
=\sum_{A,S}c_A(S)
\bigl(H_{M_ST_A\xi}-H_{M_S\xi}\bigr).
}
\]

The empty-target coefficient `c_A(emptyset)=c_A(0)>=0` is an honest positive block-toggle clock on the dual labels. For `S ne emptyset`, the two branches have equal absolute rate `|c_A(S)|` and opposite signs: toggle `A` first, or do not toggle it, then impose target `S`.

Expanding `1_{eta_i=0}=1-eta_i` recovers the monomial `J`-branch algebra above. This cylinder dual explains what the hidden multi-site mark really is, but it propagates boundary label information across successful records; consequently it naturally leads to operator-valued/tensor-network patches rather than the scalar patch factors of the paper. For a direct extension of the paper's scalar factorization, the monomial dual is the better starting point.

## 3. Why the old one-site patches fail

The old successful skeleton is not enough to make one-site patch interiors independent.

Even with empty target, a multi-source event with `|D|>=2` jointly updates several source lines through the common hidden subset `J`. More importantly, the condition that an unrecorded block clock `(A,D,...)` does not act is a condition on the whole pattern `B cap A=D`. It cannot be checked from one site strip alone.

A constant pair flip is already enough to see the first issue. If `A={i,j}` and both dual sites are active, then

\[
\chi_{\{i,j\}}(\eta^A)-\chi_{\{i,j\}}(\eta)
=1-\eta_i-\eta_j.
\]

The same hidden block event produces the three branches

\[
\varnothing\quad(+),
\qquad\{i\}\quad(-),
\qquad\{j\}\quad(-).
\]

Those two site lines therefore do not carry independent interior marks.

## 4. Natural hyperpatch construction

Keep the same philosophy as the paper: retain the nonempty-target dual interactions which actually act, but now record enough source information to determine the block condition. A successful record is naturally

\[
(A,t,D,S),
\qquad
D=A\cap B_{t-}\neq\varnothing,
\qquad S\neq\varnothing,
\]

and hides `J subseteq D`.

Ignoring for the moment degeneracies caused by overlaps of `S` and `D`, the record gives outgoing boundaries at the source sites in `D` and incoming boundaries at the target sites in `S`. As before, one may first cut every site line into atomic strips between consecutive successful incidences.

These atomic strips are not the final patches. Build an overlap graph on them. Put two strips in the same component whenever a hidden block clock or a consistency test can depend on their states jointly. Concretely, whenever their time intervals overlap and their sites occur together in some physical flip block `A` with a nonzero dual clock family, connect them. Also connect the outgoing strips born at the same successful block record because their initial active/inactive states share the single hidden subset `J`.

A **hyperpatch** is a connected component of this overlap graph in spacetime.

It is a multi-leg object: it can contain several site lines, several incoming boundaries and several outgoing boundaries. A hyperpatch reaching the terminal horizon has several terminal legs, so its end contribution is a multi-affine function of all terminal spins on those legs.

The reason this is the right level is that every ingredient of the FK weight is then component-local:

- hidden `J` marks at successful block records;
- all omitted block clocks;
- the consistency event saying that there are no additional successful nonempty-target records;
- the block-local diagonal/FK correction, which is a sum over flip blocks and depends on the active pattern `B cap A`.

Distinct hyperpatches use disjoint Poisson families and disjoint hidden record marks. Therefore the same Mecke argument as in the paper should give conditional independence **between hyperpatches**, although not between their constituent site strips. The resulting pathwise FK weight factors as a product over hyperpatches.

This reduces exactly to the paper's one-site patches when every physical flip block is a singleton.

A useful special case is when the overlap hypergraph of the genuine multi-site flip blocks has uniformly bounded connected components (for example a partition into disjoint finite update blocks). Then every hyperpatch has uniformly bounded spatial support and the extension becomes a finite-state block transfer problem. In the general overlapping case, hyperpatch spatial support is not uniformly bounded, although it is finite at finite horizon under the usual local-finiteness assumptions.

## 5. Patch positivity

There is a natural abstract positivity notion:

\[
C(P)\ge0
\]

for every completed bulk hyperpatch `P`, where `C(P)` is the conditional expectation of its full signed FK factor under the consistent hyperpatch law.

For a fixed hyperpatch with spatial support `U`, its hidden interior is finite-state. One can encode its contribution by a transfer matrix on subsets of `U`, or equivalently by a finite tensor contraction built from:

- empty-target block transfers;
- the signed boundary rows `a_{A,D,J}(S)`;
- consistency/killing at the prescribed successful boundaries.

So positivity is perfectly well-defined and finite-dimensional **for each fixed hyperpatch**.

What is lost is the paper's universal one-site criterion. In an overlapping multi-site system, `|U|` is not uniformly bounded and there is no fixed finite catalogue of boundary types. Generic hyperpatch positivity is therefore an unbounded family of external-positivity/tensor-sign conditions, not two coefficient inequalities.

There is also an immediate short-patch diagnostic. At a record `(A,D,S)`, the zero-length signed branch coefficient for hidden outcome `J` is

\[
c_A(S)\theta_D(J).
\]

If a later realizable boundary can distinguish that hidden outcome before it has been averaged with the other `J`'s, a negative value gives a negative arbitrarily short hyperpatch. Since `theta_D(J)` alternates in sign, genuine multi-source interactions have many such potential obstructions. This is the direct multi-site analogue of the short-`OO` obstruction found in the finite-state programme. It is not an automatic no-go, because a hyperpatch can force several `J` outcomes to remain grouped and cancel before any boundary distinguishes them.

## 6. End factors and centered-moment order

A terminal hyperpatch generally has several horizon legs. Its end contribution is therefore not affine in one scalar `z`; it is multi-affine in a vector

\[
z=(z_i)_{i\in T(P)}.
\]

For Bernoulli product initial data this is not a problem: averaging simply evaluates the multi-affine end factor at the density profile on its terminal legs. Thus the exact product-law patch representation should survive essentially verbatim with scalar end factors replaced by multivariate ones.

For the centered-moment order, bulk hyperpatch positivity alone is no longer enough. The one-site proof uses the fact that every end factor has the form

\[
C(p_i^*,P)+\kappa(P)(z-p_i^*),
\qquad C(p_i^*,P),\kappa(P)\ge0.
\]

The correct replacement is a cone condition on every end hyperpatch. For a profile `p^*`, require the centered expansion

\[
C(z,P)
=\sum_{R\subseteq T(P)}
\kappa_R(P)
\prod_{i\in R}(z_i-p_i^*)
\]

with

\[
\kappa_R(P)\ge0
\]

for every `R`, including the constant coefficient. Under bulk positivity plus this **centered end-hyperpatch positivity**, the same expansion argument gives preservation of the centered-moment cone `M_*` and the order `preceq_*`.

Thus a scalar threshold profile is no longer the natural object. One should expect an admissible set of profiles `p^*` defined by nonnegativity of all centered coefficients of all end hyperpatches. There is no reason for this set to factor coordinatewise or admit the paper's explicit threshold formula.

## 7. Which earlier results survive

### Survive essentially structurally

- Exact monomial Feynman--Kac duality: yes, with the nonadditive source-block dual above.
- Harris/local-finiteness and finite propagation: yes under bounded block size, bounded neighbourhood size and bounded local incidence/rates.
- Successful-interaction representation: yes, but the record must contain the active source pattern `D=A cap B`.
- Exact patch representation: yes in hyperpatch form, assuming the componentwise Mecke/factorization argument is written carefully.
- Product Bernoulli initial laws: yes; end factors are multi-affine and are evaluated at the product density profile.

### Survive only after strengthening the positivity hypothesis

- Centered-moment order and preservation of `M_*`: bulk positivity must be supplemented by nonnegative centered coefficients of every multi-leg end factor.
- Any comparison based on patchwise nonnegative weights must be reformulated at hyperpatch level.

### Do not survive automatically

- The two local coefficient inequalities characterizing patch positivity.
- The scalar patch-threshold profile and its explicit formula.
- The pure-death comparison from the paper. If an independent single-site `1->0` component is added, it still acts diagonally on monomials, but inside a signed hyperpatch it changes the weight by a path-dependent factor. Nonnegativity of the averaged hyperpatch contribution does not by itself imply monotonicity when that killing is changed. A stronger `death-monotone` or Laplace-positivity property of hyperpatch contributions would be needed.
- The common-invariant-limit theorem and its rate do not follow verbatim. Finite propagation and a causal hyperedge ancestry argument should still be available, but the proof uses both patchwise comparison with the death-removed dynamics and the exact one-site outgoing-chain factor `exp(-epsilon Delta)`. Those are no longer consequences of bulk hyperpatch positivity alone.
- Uniform exponential ergodicity therefore also does not transfer without additional work.

## 8. Bottom line

The multi-site extension does not break the basic representation mechanism. It changes its dimensionality.

For single-site flips, the hidden interior dynamics is one-dimensional on each site line, so patches are scalar one-site objects and positivity collapses to local coefficient inequalities.

For simultaneous flips, the hidden dynamics is carried by connected source blocks. The natural objects are multi-leg hyperpatches, and a fixed hyperpatch contribution is a finite-state transfer/tensor contraction. The exact representation should survive, but the simple positivity/order/convergence package does not survive for free.

If this is incorporated into the paper, I would state the general multi-site representation first and be conservative afterward: define hyperpatch positivity abstractly, prove the centered-order consequence only under the stronger centered end-factor cone condition, and leave a tractable coefficient criterion and the pure-death convergence theorem as separate questions. The bounded-overlap/disjoint-block case is the first place where one should expect an explicit positivity theory comparable to the current paper.