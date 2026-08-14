---
title: Disjoint-event lower bounds for compensated branching estimators
status: standard fact
tags:
  - probability
  - branching process
  - integrability
  - importance sampling
  - PDE
---

# Disjoint-event lower bounds for compensated branching estimators

A standard way to prove that a branching estimator is not in \(L^1\) is to restrict its absolute expectation to a sequence of pairwise disjoint genealogical events. On each event, the proposal probabilities and lifetime densities can cancel their reciprocal compensators exactly. The resulting nonnegative lower bounds then add, and divergence of their sum forces failure of \(L^1\).

This is an elementary combination of [Tonelli's theorem](tonelli-markov-and-borel-cantelli.md) and the [importance-sampling compensator identity](importance-sampling-compensators.md). It is recorded separately because the same lower-bound pattern appears in several branching obstructions.

**References.** No specialized reference is needed; the statements below are elementary measure-theoretic probability and importance sampling.

## Disjoint-event lower bound

Let \(X\) be an extended real-valued random variable and let \((E_m)_{m\geq1}\) be pairwise disjoint measurable events. Since

$$
\sum_{m\geq1}\ind(E_m)
\leq1,
$$

one has pointwise

$$
|X|
\geq
\sum_{m\geq1}|X|\ind(E_m).
$$

Tonelli's theorem therefore gives

$$
\mathbb E|X|
\geq
\sum_{m\geq1}
\mathbb E\left[|X|\ind(E_m)\right].
\tag{1}
$$

The right side may equal \(+\infty\). In particular, if

$$
\mathbb E\left[|X|\ind(E_m)\right]
\geq a_m
\tag{2}
$$

for numbers \(a_m\geq0\) satisfying

$$
\sum_m a_m=\infty,
$$

then

$$
X\notin L^1.
\tag{3}
$$

No independence assumption on the events \(E_m\) is required. Pairwise disjointness is what lets their absolute-moment contributions add without overcounting.

A particularly simple sufficient condition is that the lower bounds in (2) fail to tend to zero along an infinite subsequence.

## Why exact genealogy counts are useful

In a branching tree, events indexed by the exact number of selected branchings along a distinguished lineage are automatically disjoint. For example,

$$
E_m
=
\{\text{the distinguished lineage has exactly }m\text{ selected branchings}\}
$$

and \(E_\ell\) cannot both occur when \(m\neq\ell\).

This is often preferable to using nested events such as “at least \(m\) branchings,” because nested events cannot be summed directly in (1). The exact-count formulation turns a lower bound at each depth into an additive series.

## One continuous proposal variable

Let \(\Theta\) be sampled from a density \(q(\theta)>0\) on a measurable set \(D\), with respect to a reference measure \(d\theta\). Suppose a compensated estimator contains the factor

$$
\frac{A(\Theta,\Xi)}{q(\Theta)},
\tag{4}
$$

where \(\Xi\) denotes all remaining randomness. Then, whenever the expressions are measurable and nonnegative after taking absolute values,

$$
\begin{aligned}
\mathbb E\left[
\left|
\frac{A(\Theta,\Xi)}{q(\Theta)}
\right|
\ind(\Theta\in D_0)
\right]
&=
\int_{D_0}
\mathbb E\left[
|A(\theta,\Xi)|
\mid \Theta=\theta
\right]
\,d\theta
\end{aligned}
\tag{5}
$$

for measurable \(D_0\subseteq D\), in the usual regular-conditional-distribution formulation.

The proposal density has disappeared. No uniform positive lower bound on \(q\) is needed. It is enough that \(q>0\) on the restricted region so that the reciprocal compensator is defined.

Equation (5) is the absolute-moment counterpart of ordinary importance-sampling cancellation. It is especially useful for lower bounds because small proposal density does not suppress a selected event: the small probability is exactly offset by the large reciprocal weight.

## Discrete proposal choices

If a label \(I\) is sampled with probabilities \(p_i>0\) and the estimator contains \(A_I/p_I\), then for any subset \(J\) of labels,

$$
\mathbb E\left[
\left|
\frac{A_I}{p_I}
\right|
\ind(I\in J)
\right]
=
\sum_{i\in J}
\mathbb E|A_i|,
\tag{6}
$$

provided the remaining randomness has the stated conditional law. Again the probabilities \(p_i\) cancel completely.

The same identity may be applied conditionally at successive vertices of a finite genealogy.

## Lifetime and survival compensation

Suppose a branch lifetime \(\tau\) has density \(\rho>0\). Restricting to a prescribed branching time in \(ds\) contributes probability

$$
\rho(s)\,ds.
$$

If the estimator contains the reciprocal lifetime compensator \(1/\rho(s)\), then after taking absolute values the two factors cancel, leaving

$$
ds.
\tag{7}
$$

Likewise, if survival for a remaining duration \(r\) has probability \(\overline F(r)>0\) and the terminal weight contains \(1/\overline F(r)\), then restricting to survival leaves no survival-probability factor in the absolute-moment integral.

For a finite prescribed genealogy, iterating these identities removes products of lifetime densities, offspring-selection probabilities, and survival probabilities. What remains is the reference integration over branch times together with the absolute values of the model-dependent spatial or terminal factors.

## Generic restricted-genealogy formula

A useful abstract version is the following. Let \(E_m\) be a finite genealogical event parameterized by continuous marks \(\theta\in D_m\) and discrete choices whose joint proposal density/mass is \(Q_m(\theta)>0\). Suppose that on \(E_m\)

$$
X
=
\frac{A_m(\theta,\Xi)}{Q_m(\theta)},
\tag{8}
$$

where \(\Xi\) contains the remaining model randomness. Then

$$
\mathbb E\left[|X|\ind(E_m)\right]
=
\int_{D_m}
\mathbb E\left[
|A_m(\theta,\Xi)|
\mid \theta,E_m
\right]
\,d\theta,
\tag{9}
$$

with sums inserted for any remaining discrete reference variables.

Thus a lower bound on the right side of (9) is independent of how rarely the auxiliary proposal samples that genealogy, as long as the proposal gives it positive density or mass.

This cancellation is not a statement that the whole estimator is integrable. It is frequently used in the opposite direction: once the proposal factors have disappeared, singular derivative weights or large terminal factors may make the restricted absolute moment too large to sum over \(m\).

## Combining cancellation with disjoint genealogies

Suppose the genealogical events \((E_m)\) are pairwise disjoint and the proposal cancellation above yields

$$
\mathbb E\left[|X|\ind(E_m)\right]
\geq a_m.
$$

Then (1) gives

$$
\mathbb E|X|
\geq
\sum_m a_m.
\tag{10}
$$

Therefore

$$
\sum_m a_m=\infty
\quad\Longrightarrow\quad
X\notin L^1.
\tag{11}
$$

This is the reusable pattern behind the [repeated-Hessian obstruction for coding trees](repeated-hessian-obstruction-for-coding-trees.md): the selected genealogies are disjoint by depth, the auxiliary branching probabilities cancel their compensators, and the remaining deterministic lower bound is summed over the depth.