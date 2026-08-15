---
title: Total variation, bounded variation, and derivative singularities
status: standard fact
audit: current
tags:
  - analysis
  - measure theory
  - bounded variation
  - total variation
  - PDE
---

# Total variation, bounded variation, and derivative singularities

Total variation measures the total amount by which a function moves, without allowing cancellations between increases and decreases. For absolutely continuous functions it is exactly the integral of the absolute derivative. This makes total variation a natural way to convert derivative singularities into non-cancelling lower bounds.

The same language extends to signed measures: the distributional derivative of a one-dimensional function of bounded variation is a finite signed measure, and the variation of the function is the total variation of that derivative measure.

**References.** These are standard facts from real analysis and the theory of functions of bounded variation; see, for example, Lawrence C. Evans and Ronald F. Gariepy, *Measure Theory and Fine Properties of Functions*.

## Variation of a function

Let \(I=[a,b]\subset\mathbb R\) and let \(g:I\to\mathbb R\). For a partition

$$
\Pi:
a=x_0<x_1<\cdots<x_n=b,
$$

define

$$
V(g;\Pi)
=
\sum_{j=1}^n
|g(x_j)-g(x_{j-1})|.
\tag{1}
$$

The *total variation* of \(g\) on \(I\) is

$$
\operatorname{Var}_I(g)
=
\sup_\Pi V(g;\Pi),
\tag{2}
$$

where the supremum is over all finite partitions of \(I\). The value \(+\infty\) is allowed.

A function belongs to \(BV(I)\), the space of functions of bounded variation, if

$$
\operatorname{Var}_I(g)<\infty.
$$

Variation is insensitive to sign cancellation: traversing upward by one unit and then downward by one unit contributes two units of variation.

## Local variation and disjoint intervals

If

$$
a<c<b,
$$

then

$$
\operatorname{Var}_{[a,b]}(g)
=
\operatorname{Var}_{[a,c]}(g)
+
\operatorname{Var}_{[c,b]}(g).
\tag{3}
$$

More generally, if \(I_1,\ldots,I_M\) are pairwise disjoint subintervals of \(I\), then

$$
\operatorname{Var}_I(g)
\geq
\sum_{j=1}^M
\operatorname{Var}_{I_j}(g).
\tag{4}
$$

To prove (4), choose partitions of the \(I_j\)'s that nearly attain their variations and combine those partition points into one partition of \(I\). The extra increments in the gaps are nonnegative and can only increase the partition sum.

Consequently, for a countable family of pairwise disjoint intervals \((I_j)\),

$$
\operatorname{Var}_I(g)
\geq
\sum_{j=1}^\infty
\operatorname{Var}_{I_j}(g),
\tag{5}
$$

where the right side may be infinite. Thus lower bounds produced on disjoint spatial regions add without cancellation.

## Absolutely continuous functions

Suppose \(g\) is absolutely continuous on \([a,b]\). Then \(g'\) exists almost everywhere, belongs to \(L^1(a,b)\), and

$$
g(y)-g(x)
=
\int_x^y g'(s)\,ds.
$$

In this case,

$$
\operatorname{Var}_{[a,b]}(g)
=
\int_a^b|g'(s)|\,ds.
\tag{6}
$$

In particular, (6) holds for every \(C^1\) function.

The upper bound in (6) follows immediately from the triangle inequality applied to the integral on every partition interval. The reverse inequality follows by approximating the sign of \(g'\) with simple functions, or equivalently from the standard characterization of absolutely continuous functions of bounded variation.

Equation (6) is the basic mechanism by which a derivative lower bound becomes a total-variation lower bound.

## Derivative singularities

Suppose \(g\) is absolutely continuous on each compact subinterval of

$$
(a-r,a)\cup(a,a+r)
$$

for some \(r>0\). If

$$
\int_{a-r}^{a}|g'(x)|\,dx
+
\int_a^{a+r}|g'(x)|\,dx
=
\infty,
\tag{7}
$$

with the integrals interpreted as improper integrals, then \(g\) has infinite total variation on every interval containing \(a\).

A common borderline singularity is logarithmic. If, for some \(c>0\),

$$
|g'(x)|
\geq
\frac{c}{|x-a|}
$$

for \(\varepsilon<|x-a|<r\), then

$$
\operatorname{Var}_{[a-r,a-\varepsilon]}(g)
+
\operatorname{Var}_{[a+\varepsilon,a+r]}(g)
\geq
2c\log\frac r\varepsilon.
\tag{8}
$$

Thus a \(1/|x-a|\) derivative singularity generates logarithmically diverging variation as the cutoff \(\varepsilon\downarrow0\).

More generally, one need not know the exact derivative. Any lower bound of the form

$$
\int_{J_\varepsilon}|g'|
\geq
A(\varepsilon),
\qquad
A(\varepsilon)\longrightarrow\infty,
$$

on shrinking or expanding regions gives the same lower bound for variation by (6).

## Several separated singular regions

Suppose \((J_m)\) are pairwise disjoint intervals and \(g\) is absolutely continuous on each \(J_m\). If

$$
\int_{J_m}|g'(x)|\,dx
\geq a_m,
\tag{9}
$$

then (4) and (6) give

$$
\operatorname{Var}_I(g)
\geq
\sum_m a_m
$$

for every interval \(I\) containing all the \(J_m\)'s. Hence

$$
\sum_m a_m=\infty
\quad\Longrightarrow\quad
\operatorname{Var}_I(g)=\infty.
\tag{10}
$$

This disjoint-region principle is often more useful than trying to analyze the signs of the derivative globally.

## Distributional derivative and variation measure

If \(g\in BV(a,b)\), then its distributional derivative \(Dg\) is a finite signed Radon measure. Conversely, if the distributional derivative of an \(L^1\) function is a finite signed Radon measure, then the function has a representative in \(BV\).

For a finite signed measure \(\mu\), its total variation measure \(|\mu|\) is defined by

$$
|\mu|(A)
=
\sup
\left\{
\sum_j|\mu(A_j)|:
A=\bigsqcup_jA_j,
\text{ finite measurable partition}
\right\}.
\tag{11}
$$

For a one-dimensional \(BV\) function,

$$
|Dg|((a,b))
=
\operatorname{Var}_{(a,b)}(g),
\tag{12}
$$

up to the usual endpoint convention. If \(g\) is absolutely continuous, then

$$
Dg=g'(x)\,dx,
\qquad
|Dg|=|g'(x)|\,dx,
$$

so (12) reduces to (6).

This measure formulation is useful when a limiting derivative develops jump or singular components: total variation still records the non-cancelling mass even when no classical derivative exists everywhere.

## Distinguishing two uses of total variation

The phrase *total variation* is used in two closely related senses:

- \(\operatorname{Var}_I(g)\) for the variation of a function on an interval;
- \(|\mu|\) or \(\|\mu\|_{TV}=|\mu|(I)\) for the total variation of a signed measure.

For one-dimensional \(BV\) functions the two notions are connected exactly by the distributional derivative identity (12). They should not be confused with the total-variation distance between two probability measures, which is a different application of the same signed-measure norm.
