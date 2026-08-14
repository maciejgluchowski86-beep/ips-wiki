---
title: Uniform integrability and passage to expectations
status: standard fact
tags:
  - probability
  - measure theory
  - integrability
  - convergence
  - PDE
---

# Uniform integrability and passage to expectations

Almost-sure or probabilistic convergence does not by itself justify passing a limit through expectation. Uniform integrability is the standard condition that prevents mass from escaping into increasingly rare large values. It is used in branching representations when truncated trees or nearby starting parameters converge pointwise but the desired conclusion concerns their expectations.

**References.** Any graduate measure-theoretic probability text contains these results; see, for example, Patrick Billingsley, *Probability and Measure*, third edition, Wiley, 1995. See [References](../meta/references.md).

## Definition

A family \(\mathcal Y\) of integrable random variables is *uniformly integrable* if

$$
\lim_{R\to\infty}
\sup_{Y\in\mathcal Y}
\mathbb E\left[
|Y|\ind(|Y|>R)
\right]
=0.
\tag{1}
$$

For a parameterized family \(\{Y_\theta:\theta\in\Theta\}\), *local uniform integrability* means that (1) holds after restricting \(\theta\) to every compact subset of the parameter space.

Uniform integrability is stronger than a uniform \(L^1\) bound. A family can satisfy

$$
\sup_{Y\in\mathcal Y}\mathbb E|Y|<\infty
$$

while still concentrating a fixed amount of expectation in larger and larger rare values.

## An \(L^p\) criterion

If there is a number \(p>1\) such that

$$
\sup_{Y\in\mathcal Y}
\mathbb E|Y|^p<\infty,
\tag{2}
$$

then \(\mathcal Y\) is uniformly integrable. Indeed, on \(\{|Y|>R\}\),

$$
|Y|
\leq
R^{1-p}|Y|^p,
$$

so

$$
\mathbb E\left[
|Y|\ind(|Y|>R)
\right]
\leq
R^{1-p}\mathbb E|Y|^p.
\tag{3}
$$

Taking the supremum and then \(R\to\infty\) proves the claim.

This is why an \(L^2\) estimate for a branching estimator automatically supplies the uniform-integrability control needed for first moments.

## Vitali convergence

Suppose \(Y_n\to Y\) in probability and the family \(\{Y_n:n\geq1\}\) is uniformly integrable. Then

$$
Y\in L^1,
\qquad
\mathbb E|Y_n-Y|\longrightarrow0,
\tag{4}
$$

and in particular

$$
\mathbb E Y_n
\longrightarrow
\mathbb E Y.
\tag{5}
$$

This is often called the Vitali convergence theorem. Almost-sure convergence is more than enough for the convergence-in-probability hypothesis.

A common branching pattern is therefore:

1. prove that a truncated or perturbed random functional converges pointwise or in probability;
2. prove uniform integrability independently;
3. use (4)--(5) to identify the limit of expectations.

## Dominated convergence as a special case

If there is one integrable random variable \(G\) such that

$$
|Y_n|\leq G
$$

almost surely for every \(n\), then the family \(\{Y_n\}\) is uniformly integrable and dominated convergence applies. Branching functionals often do not admit such a common pointwise majorant, which is why moment estimates and uniform integrability are used instead.

## Conditional version

Let \(\mathcal G\) be a sigma-field. Conditional moment bounds can be used in the same spirit. For example, if

$$
\mathbb E\left[
|Y|^p\mid\mathcal G
\right]
\leq C
$$

almost surely for some \(p>1\), then the conditional tail satisfies

$$
\mathbb E\left[
|Y|\ind(|Y|>R)
\,\middle|\,
\mathcal G
\right]
\leq
C R^{1-p}.
\tag{6}
$$

Such estimates are useful when descendant branching functionals must be controlled uniformly after conditioning on an ancestral skeleton.

## Why this matters for branching representations

The [HLOTW marked branching construction](marked-branching-diffusion-for-gradient-nonlinearities.md) assumes local uniform integrability in its abstract representation theorem and obtains it from explicit \(L^q\) estimates under stronger hypotheses. The [representation-level dichotomy](representation-level-dichotomy.md) uses the same mechanism in its singular-lifetime extension: the moment majorant supplies uniform integrability, which then permits passage to expectations and continuity in the starting parameters.

Uniform integrability is logically separate from unbiased first-branch cancellation. Correct [importance-sampling compensators](importance-sampling-compensators.md) recover the signed Duhamel recursion, while uniform integrability controls the analytic passage from finite or parameter-dependent random objects to their expected limits.