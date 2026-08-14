---
title: Discrepancy zipper route for one-dimensional FA-1f
status: conditional
audit: current
tags:
  - FA-1f
  - out of equilibrium
  - chronology
  - coarse graining
  - patches
---

# Discrepancy zipper route for one-dimensional FA-1f

This entry records a geometric route for averaging update chronology in the remaining Bernoulli-quench problem for one-dimensional two-sided [FA-1f](fa-1f-model.md). The local zipper identities below are exact. The regional factorization proposed afterwards has not yet been proved.

The point of the construction is to keep the single discrepancy responsible for the desired sign on a one-dimensional spacetime interface. Updates meeting that interface have a positive local expansion. Updates away from it are not expanded one at a time; they are left hidden inside spacetime regions and averaged there as complete FA evolutions or ordinary positive patches.

This differs from the [chronology-averaged sign route](chronology-averaged-sign-route-for-fa-1f.md), where one asks directly for positivity of a full fixed-count shuffle polynomial.

## Fixed-count recurrence

Use the three-colour variables

$$
R=r,
\qquad
S=p-r,
\qquad
Q=q,
$$

and abbreviate

$$
P=R+S=p,
\qquad
H=R+S+Q=1.
$$

For a function \(F\) indexed by finite subsets of \(\mathbb Z\), the one-ring recurrence operator at \(j\) is

$$
\mathcal R_jF(A)
=
\begin{cases}
H F(A), & j\notin A,\\[0.4em]
P F(A\setminus\{j\})
-P F((A\setminus\{j\})\cup N(j))
+H F(A\cup N(j)), & j\in A,
\end{cases}
\tag{1}
$$

where \(N(j)=\{j-1,j+1\}\). The negative middle term is the local obstruction to a one-ring positivity proof.

For \(i\notin A\), define the marked discrepancy

$$
D_iF(A)=P F(A)-H F(A\cup\{i\}).
\tag{2}
$$

At time zero, for the Bernoulli radial function \(F_0(A)=r^{|A|}\),

$$
D_iF_0(A)=r^{|A|}(p-r)\ge0
\tag{3}
$$

throughout the unresolved range \(0\le r\le p\), with no shield assumption on \(A\).

## Positive zipper identities

The crucial observation is that the negative term in (1) disappears whenever the update touches the marked discrepancy.

### Center update

For every \(i\notin A\),

$$
D_i(\mathcal R_iF)(A)
=H D_iF(A\cup N(i)).
\tag{4}
$$

Indeed, \(i\notin A\), so \(\mathcal R_iF(A)=HF(A)\), while

$$
\mathcal R_iF(A\cup\{i\})
=P F(A)-P F(A\cup N(i))+H F(A\cup\{i\}\cup N(i)).
$$

Substitution into (2) gives (4).

### Neighbor update with absent neighbor

Let \(j=i\pm1\). If \(j\notin A\), then

$$
D_i(\mathcal R_jF)(A)=H D_iF(A).
\tag{5}
$$

Both configurations in the discrepancy omit \(j\), so the same factor \(H\) is produced.

### Neighbor update with present neighbor

Let \(j=i\pm1\) belong to \(A\), and put \(k=2j-i\), the other neighbor of \(j\). Then

$$
D_i(\mathcal R_jF)(A)
=
P D_iF(A\setminus\{j\})
+Q D_jF((A\setminus\{j\})\cup\{i,k\}).
\tag{6}
$$

This follows by expanding the two terms in (2) using (1) and collecting them into the two displayed discrepancies.

Since \(H=P+Q=1\), formula (6) has a probabilistic interpretation. When a neighboring update meets the zipper and the neighboring site belongs to the background set, the marked discrepancy either

* stays at \(i\), removes \(j\) from the background, with weight \(p\); or
* moves from \(i\) to \(j\), with both neighbors \(i,k\) placed in the background, with weight \(q\).

The center move (4) and the absent-neighbor move (5) are deterministic after the normalization \(H=1\). Thus updates touching the mark evolve it by a positive stochastic rule. No signed coefficient is carried by the zipper itself.

## Why distant updates are the only obstruction

If \(|j-i|\ge2\), insertion of the marked site \(i\) does not change whether the update at \(j\) is applied. Algebraically, the discrepancy commutes through that local operation. If \(j\in A\), however, one obtains

$$
P D_iF(A\setminus\{j\})
-P D_iF((A\setminus\{j\})\cup N(j))
+H D_iF(A\cup N(j)),
\tag{7}
$$

so the negative coefficient from (1) reappears.

This identifies a geometric division of labour. An update at distance at most one from the current mark belongs to the zipper and is treated by (4)--(6). An update farther away belongs to the background and should not be exposed individually.

## The update heap

For a finite word of site updates, regard each occurrence as a spacetime brick centred at its site. Two bricks are dependent when their sites differ by at most one. Updates at sites at distance at least two commute, so swapping their order does not change the resulting operator. The equivalence class of a word under these commuting swaps is its nearest-neighbour dependency heap.

Start with a marked discrepancy at the top. Trace backwards through the heap. Whenever a maximal brick meets the current marked site or one of its neighbors, expose that brick and apply the positive rule (4), (5), or (6). Bricks that do not meet the current mark are left unexposed. When the mark moves, the exposed bricks form a nearest-neighbor path in the heap. The old portion of the path separates off components of unexposed bricks. These are the **zipper regions**.

The interface may leave a branching scaffold even though the marked discrepancy itself never branches: the scaffold records the last dependent bricks needed to certify that no unexposed brick connects two different regions. This is the two-sided analogue of the barrier--scaffold closure used elsewhere in the patch construction.

## Continuous-time zipper scaffold

In the Poisson graphical construction, the same idea can be formulated without first conditioning on a complete update word. Starting from a terminal marked point \((i,t)\), reveal backwards only the latest update points whose sites are within distance one of the current marked site. Every such reveal also records the corresponding no-later-dependent-update intervals. Whenever the mark moves by the \(q\)-branch of (6), continue from the new marked site. Close the revealed set under nearest-neighbor predecessors until every unrevealed update belongs to one connected component of the complement and cannot interact across two components without crossing the revealed scaffold.

The intended factorization statement is:

> **Zipper factorization target.** Conditional on the marked zipper, its predecessor scaffold, the local branch choices in (6), and the certifying absence intervals, the unrevealed graphical randomness factorizes over the zipper regions. Within each region the complete order of the remaining updates retains its conditional Poisson law. In particular, no deterministic chronology inside a region is selected by the conditioning.

The proof should follow the same Poisson-disintegration pattern as [patch factorization](patch-factorization.md): fix the revealed boundary data, identify the event that these are exactly the zipper/scaffold data as an intersection of regional consistency events, and use independence of disjoint source-time strips before conditioning.

## Regional averaging

The point of the zipper factorization is that (7) should never be used ring by ring. A region cut off from the zipper is evaluated only after all of its internal updates have been averaged.

There are two possible mechanisms for doing this.

1. **Patch mechanism.** If the regional boundary data can be matched to the ordinary signed-dual patch boundary data, then every unmarked bulk region contributes a standard FA patch factor. Its sign is an additional input and is not established by this entry.
2. **Projection mechanism.** In the primal heat-bath representation, one-site FA update operators are orthogonal projections in \(L^2(\mu_q)\). A region carrying a vacancy boundary therefore has a finite-volume gapped FA generator. Products containing a sufficiently rich collection of regional updates contract the orthogonal complement of local equilibrium; averaging the Poisson chronology gives the regional semigroup directly.

The first mechanism is closer to the existing sign calculation. The second asks only for contraction and may therefore avoid proving a finite-time sign inequality altogether.

## Relation with one-dimensional vacancy geometry

The construction needs a supply of vacancy-bearing spacetime boundaries, not a new proof that vacancies spread. Martinelli, Shapira, and Toninelli prove in [arXiv:2510.20461](https://arxiv.org/abs/2510.20461), Theorem 6.2, that for every \(q>0\) an FA-1f process started from finitely many vacancies has spatial span growing linearly in time. Their proof already uses finite-volume mixing behind the expanding infection cloud.

Thus the remaining geometric problem is more specific: build the zipper/scaffold so that the activity generated by the two-sided FA geometry supplies regional boundaries while leaving each regional chronology hidden.

## Immediate proof target

The next useful statement is not the full Bernoulli convergence theorem. It is the zipper factorization target together with the following regional closure statement:

> After the zipper scaffold is fixed, every connected unmarked component can be integrated out into a nonnegative scalar weight or into a strictly contracting regional kernel, uniformly over the finite boundary data exposed by the scaffold.

If this holds, the only object connecting time \(0\) to the terminal shield discrepancy is the marked zipper. Its local transition weights are nonnegative by (4)--(6), and its time-zero discrepancy is nonnegative by (3). This would place all chronology cancellation inside the regions before any absolute value or sign comparison is taken.
