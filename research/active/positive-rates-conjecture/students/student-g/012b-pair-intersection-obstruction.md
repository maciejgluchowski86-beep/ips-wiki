# Student G 012b: decomposition-independent pair-intersection obstruction

## Result

At the hard point `P_h`, **every** exact deterministic-Boolean random-map decomposition from Assignment 012 has a pair of independent mark-only backward supports whose intersection survives with positive probability. In particular there is a universal constant `epsilon>0` such that, starting from

$$
A_0=A'_0=\{0\},
$$

one has along the block times `t=8n`

$$
\boxed{
\mathbb E\left[2^{|A_{8n}\cap A'_{8n}|}-1\right]
\ge
\mathbb P(A_{8n}\cap A'_{8n}\ne\varnothing)
\ge \epsilon
}
\tag{1}
$$

for every `n`.

A crude explicit choice from the proof is `epsilon>1/7`.

This is a pair-history obstruction, not a first-moment argument. It rules out decay of the exact Assignment-012 pair observable for **all** ancestry points in the random-map polytope, including decompositions that sacrifice oblivious death or replace the canonical OR mark.

The proof uses only a width-one recursion. No truncation boundary is introduced.

## 1. Uniform ancestry bounds from the exact polytope

Write

$$
u:=d+j.
$$

The exact polytope `(P)` in `012a-random-map-polytope.md` gives

$$
d+2s+j\le\frac1{5000},
$$

hence

$$
\boxed{u=d+j\le\frac1{5000}.}
\tag{2}
$$

It also gives

$$
d+r\ge c,
\qquad
j+r\ge c,
\qquad
c=\frac{9999}{10000}.
$$

Therefore

$$
r\ge c-\min(d,j).
$$

Since

$$
\min(d,j)\le\frac{d+j}{2}\le\frac1{10000},
$$

we have the decomposition-independent branching bound

$$
\boxed{r\ge\frac{4999}{5000}.}
\tag{3}
$$

Self-only marks do not change the support.

Thus every admissible support process has branching rate at least `4999/5000` per active ancestor while the total rate of marks which remove that ancestor from its present site (death or right-jump) is at most `1/5000`.

## 2. A width-one good cell for two independent histories

Run two independent support processes `A_t,A'_t`. For `T=8`, site `i`, and block `n`, define `G_{i,n}` using only the graphical marks in

$$
\{i,i+1\}\times[nT,(n+1)T]
$$

of the two support histories.

The cell is good when:

1. neither copy has a death or right-only mark at `i` or `i+1` during the block;
2. each copy has at least one two-parent branch mark at `i` during the block.

If

$$
i\in A_{nT}\cap A'_{nT}
$$

and `G_{i,n}` occurs, then no loss mark removes `i`, each copy branches from `i` to `i+1`, and no later loss mark removes the new `i+1`. Hence

$$
\boxed{
\{i,i+1\}
\subseteq A_{(n+1)T}\cap A'_{(n+1)T}.
}
\tag{4}
$$

This is an exact implication of the support generator. Extra branch marks and self-only marks can only add ancestors or do nothing and therefore cannot spoil `(4)`.

Because the four loss processes involved in the cell have total rate at most `4u` and the two required branch processes each have rate at least `r`,

$$
\mathbb P(G_{i,n})
\ge
 e^{-4uT}(1-e^{-rT})^2.
\tag{5}
$$

Using `(2)`--`(3)` and `T=8`,

$$
4uT\le\frac4{625}.
$$

The elementary inequality `e^{-x}>1-x` gives

$$
e^{-4uT}>\frac{621}{625}.
$$

Also

$$
rT\ge\frac{4999}{625}>7.
$$

Since the first twelve terms of the positive Taylor series for `e^7` already exceed `1000`,

$$
e^{-rT}<\frac1{1000}.
$$

Therefore

$$
\boxed{
\mathbb P(G_{i,n})
>
\frac{621}{625}\left(\frac{999}{1000}\right)^2
=
\frac{619758621}{625000000}.
}
\tag{6}
$$

If `q` denotes the bad-cell probability, then

$$
\boxed{
q<\frac{5241379}{625000000}<\frac1{100}.
}
\tag{7}
$$

The rational inequalities in `(6)`--`(7)` are checked by `012b-pair-intersection-obstruction-verifier.py`.

## 3. Dependence structure of the good-cell field

The cells have exactly the finite dependence needed below.

- Different time layers use disjoint Poisson intervals and are independent.
- In the same time layer, `G_{i,n}` and `G_{j,n}` are independent whenever `|i-j|>=2`, because their site sets `{i,i+1}` and `{j,j+1}` are disjoint.

Thus the bad-cell field is one-dependent in space and independent in time.

Define the oriented lower cluster recursively by

$$
C_0=\{0\},
$$

$$
C_{n+1}
=
\bigcup_{i\in C_n:\,G_{i,n}}
\{i,i+1\}.
\tag{8}
$$

Induction using `(4)` gives

$$
\boxed{C_n\subseteq A_{nT}\cap A'_{nT}}
\tag{9}
$$

for every `n`.

It remains only to show that the high-density one-dependent oriented process `(8)` survives with positive probability.

## 4. Elementary Peierls lemma

### Lemma

Consider the oriented lattice with edges

$$
(i,n)\to(i,n+1),\qquad(i,n)\to(i+1,n+1).
$$

Suppose site variables are independent between time layers, one-dependent within each layer, and each site is bad with probability at most `q<1/100`. If a good reached site opens both outgoing edges, then the open cluster of `(0,0)` has positive probability to be infinite. In fact the crude contour estimate below gives survival probability greater than `1/7`.

### Proof

If the reached good cluster is finite, its outer oriented vertex boundary contains a finite connected bad cut contour separating the root from arbitrarily high time levels. This is the standard planar boundary of a finite cluster in the two-child oriented lattice: every boundary vertex which could be entered from the reached cluster must be bad, otherwise it would itself be reached.

A contour of length `m` has at most two possible initial orientations and, after the first step, at most three non-backtracking choices at each step. Hence the number of length-`m` candidate contours is at most

$$
2\,3^m.
$$

Within the bad vertices of one fixed contour, dependence can occur only between horizontally adjacent vertices in the same time layer. The corresponding dependency graph is a union of one-dimensional paths, so it has an independent set containing at least half of the contour vertices. The selected bad-cell events use disjoint site sets within a layer, and different layers are independent. Therefore

$$
\mathbb P(\text{a fixed length-}m\text{ contour is bad})
\le q^{m/2}.
$$

A union bound gives

$$
\mathbb P(\text{some finite bad contour})
\le
2\sum_{m\ge1}(3\sqrt q)^m.
$$

By `q<1/100`, `3\sqrt q<3/10`, and hence

$$
2\sum_{m\ge1}(3\sqrt q)^m
<
2\sum_{m\ge1}\left(\frac3{10}\right)^m
=
\frac67<1.
$$

Thus with probability greater than `1/7` there is no finite bad cut contour, so by local finiteness/Konig's lemma there is an infinite reached oriented path. `square`

The constants are intentionally crude; their only role is to make the conclusion uniform over the entire ancestry polytope.

## 5. Consequence for the pair observable

On the survival event from the lemma, `C_n` is nonempty for every `n`. By `(9)`,

$$
A_{8n}\cap A'_{8n}\ne\varnothing
$$

for every `n`. Therefore

$$
2^{|A_{8n}\cap A'_{8n}|}-1\ge1
$$

on an event of probability greater than `1/7`, proving `(1)`.

This directly concerns the pair-history object requested by Assignment 012. It is not inferred from positive drift of `|A_t|`, supercritical expected offspring, common-coupling disagreement survival, tail-shift agreement, or the signed boundary-transmission operator.

## 6. Scope of the obstruction

The theorem kills the **simple optimized mark-only Boolean-map pair-support architecture** being tested: no choice of exact deterministic-map decomposition can make

$$
\mathbb E\left[2^{|A_t\cap A'_t|}-1\right]\to0
$$

even for a one-site terminal support at the hard point.

It does not prove nonergodicity of the spin system. It also does not rule out every conceivable information-percolation construction that reveals additional spin values and dynamically prunes an essential parent after conditioning on that value. Such a state-adaptive reveal object is not the mark-only support process defined in Assignment 012 and would be a different architecture requiring a new assignment and a new anti-circularity check.

For the present bounded experiment, however, this is the requested strong negative outcome: a decomposition-independent positive lower bound for the two-copy intersection observable itself.
