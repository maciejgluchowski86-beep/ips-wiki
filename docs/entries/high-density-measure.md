---
title: High-density measure
status: definition
tags:
  - Bernoulli product measure
  - patch critical density
  - stochastic domination
  - mixture
---

# High-density measure

A high-density measure for a patch-positive spin system is a mixture of [Bernoulli product measures](bernoulli-product-measure.md) whose one-density profiles lie above the [patch critical density](patch-critical-density.md).

**References.** None yet.

## Definition

Let

$$
\mathbf p^\star=(p_i^\star)_{i\in\Lambda}
$$

be the patch critical density profile, and define the profile interval

$$
\mathcal R_\star
=
\left\{
\mathbf r\in[0,1]^\Lambda:
\mathbf r\ge\mathbf p^\star
\right\}.
$$

A probability measure \(\nu\) on \(\{0,1\}^\Lambda\) is high-density if there is a probability measure \(\Pi\) on \(\mathcal R_\star\) such that

$$
\nu
=
\int_{\mathcal R_\star}
\mu_{\mathbf r}\,\Pi(d\mathbf r).
$$

The family of high-density measures is denoted by

$$
\mathcal M_\star.
$$

The mixing profile may be random and spatially inhomogeneous. Conditional on the profile \(\mathbf r\), the spins are independent with one-site densities \(r_i\).

## Basic properties

The family \(\mathcal M_\star\) is convex. It is also weakly compact, and hence weakly closed, when \(\Lambda\) is countable. Indeed, \(\mathcal R_\star\) and the space of probability measures on \(\mathcal R_\star\) are compact in their weak topologies, and the mixing map

$
\Pi
\longmapsto
\int_{\mathcal R_\star}\mu_{\mathbf r}\,\Pi(d\mathbf r)
$

is continuous when tested against local functions.

Every high-density measure stochastically dominates the critical Bernoulli product measure:

$$
\nu\in\mathcal M_\star
\quad\Longrightarrow\quad
\mu_{\mathbf p^\star}\le_{\mathrm{st}}\nu.
$$

The converse does not hold in general.

## Bernoulli-floor representation

The class has an equivalent representation using independent Bernoulli floor variables. Let \(\zeta\) have an arbitrary probability law on \(\{0,1\}^\Lambda\), and independently let

$$
B_i\sim\operatorname{Ber}(p_i^\star),
\qquad i\in\Lambda.
$$

Define

$$
\xi(i)=\zeta(i)\vee B_i.
$$

Then the law of \(\xi\) belongs to \(\mathcal M_\star\). Conversely, every measure in \(\mathcal M_\star\) has such a representation.

For the forward direction, conditional on \(\zeta\), the spins are independent with profile

$$
r_i(\zeta)
=
p_i^\star+(1-p_i^\star)\zeta(i)
\ge p_i^\star.
$$

For the converse, conditional on a profile \(\mathbf r\ge\mathbf p^\star\), independently choose \(\zeta(i)\) with density

$$
\frac{r_i-p_i^\star}{1-p_i^\star}
$$

when \(p_i^\star<1\), and then apply the Bernoulli floor. The resulting spin at \(i\) has density \(r_i\).

## Not preserved by FA-1f updates

The class \(\mathcal M_\star\) need not be preserved by the spin-system semigroup. In particular, it is not preserved by the hard [FA-1f model](fa-1f-model.md).

Let \(p\in(0,1)\) be the FA-1f one-density, let \(q=1-p\), and consider the two-vertex graph. The [FA-1f patch critical density](patch-critical-density-for-fa-1f.md) is \(p^\star=p\). Start from the product measure with profile \((p,1)\), which belongs to \(\mathcal M_\star\), and perform one attempted FA-1f update at the second site. The resulting law is

$$
\nu'(00)=q^2,
\qquad
\nu'(01)=pq,
\qquad
\nu'(10)=0,
\qquad
\nu'(11)=p.
$$

Every \(\nu\in\mathcal M_\star\) on these two sites satisfies

$$
q\nu(10)-p\nu(00)\ge0,
$$

because for each product component with profile \((r_1,r_2)\ge(p,p)\),

$$
q\mu_{\mathbf r}(10)-p\mu_{\mathbf r}(00)
=
(1-r_2)(r_1-p)\ge0.
$$

For \(\nu'\), the left-hand side is \(-pq^2<0\). Thus \(\nu'\notin\mathcal M_\star\).
