---
title: Finite signed measures, pushforwards, and conditional barycenters
status: standard fact
tags:
  - measure theory
  - probability
  - signed measure
  - total variation
  - conditional expectation
  - importance sampling
  - PDE
---

# Finite signed measures, pushforwards, and conditional barycenters

The coarsening results for branching representations are most transparent when a raw marked contribution is treated as a finite signed measure rather than as one particular importance-sampling random variable. This page collects the measure-theoretic facts needed for that viewpoint.

A reader who knows ordinary conditional expectation and the Radon--Nikodym theorem can regard all of the statements below as standard. The purpose of the page is to fix notation and make the later PDE entries self-contained.

**References.** These are standard consequences of the Jordan decomposition, Radon--Nikodym theorem, conditional Jensen inequality, and the elementary divisibility theorem for finite nonatomic measures. The relation to branching proposals is explained in [Importance-sampling compensators](importance-sampling-compensators.md). The distinction between function variation and signed-measure variation is recorded in [Total variation, bounded variation, and derivative singularities](total-variation-bounded-variation-and-derivative-singularities.md).

## Finite signed measures and total variation

Let \((\Omega,\mathcal F)\) be a measurable space. A finite signed measure \(\mu\) has a Jordan decomposition

$$
\mu=\mu^+-\mu^-,
$$

where \(\mu^+\) and \(\mu^-\) are finite positive measures carried by disjoint measurable sets. Its total-variation measure is

$$
|\mu|
=\mu^++\mu^-,
$$

and its total-variation norm is

$$
\|\mu\|_{\mathrm{TV}}
=|\mu|(\Omega).
\tag{1}
$$

Equivalently,

$$
\|\mu\|_{\mathrm{TV}}
=
\sup
\left\{
\sum_{j=1}^m|\mu(A_j)|:
\Omega=\bigsqcup_{j=1}^m A_j,
\text{ finite measurable partition}
\right\}.
\tag{2}
$$

In particular,

$$
|\mu(\Omega)|
\leq
\|\mu\|_{\mathrm{TV}}.
\tag{3}
$$

The inequality may be strict because positive and negative mass can cancel in \(\mu(\Omega)\) but not in \(|\mu|(\Omega)\).

## Densities with respect to a positive reference measure

Let \(\nu\) be a finite positive measure. If

$$
\mu\ll\nu,
$$

the Radon--Nikodym theorem gives an integrable density

$$
R
=
\frac{d\mu}{d\nu}
\in L^1(\nu)
$$

such that

$$
\mu(A)
=
\int_A R\,d\nu.
\tag{4}
$$

For such a representation,

$$
|\mu|(A)
=
\int_A|R|\,d\nu,
$$

and therefore

$$
\boxed{
\|\mu\|_{\mathrm{TV}}
=
\int_\Omega|R|\,d\nu.
}
\tag{5}
$$

The choice of \(\nu\) is not intrinsic. Formula (5) gives the same number for every positive reference measure which dominates \(\mu\).

## Pushforward of a signed measure

Let

$$
\mathcal C:\Omega\to Y
$$

be measurable. The pushforward signed measure \(\mathcal C_\#\mu\) is defined by

$$
(\mathcal C_\#\mu)(B)
=
\mu(\mathcal C^{-1}(B)),
\qquad B\subseteq Y\text{ measurable}.
\tag{6}
$$

The total mass is preserved:

$$
(\mathcal C_\#\mu)(Y)
=
\mu(\Omega).
\tag{7}
$$

Total variation cannot increase:

$$
\boxed{
\|\mathcal C_\#\mu\|_{\mathrm{TV}}
\leq
\|\mu\|_{\mathrm{TV}}.
}
\tag{8}
$$

One way to see (8) is to pull a finite measurable partition of \(Y\) back to a partition of \(\Omega\) and use (2).

If \(\mathcal C\) is a measurable bijection onto its image with measurable inverse, then no information is discarded and

$$
\|\mathcal C_\#\mu\|_{\mathrm{TV}}
=
\|\mu\|_{\mathrm{TV}}.
\tag{9}
$$

If \(\mathcal C\) is constant, then the pushforward has one atom of signed mass \(\mu(\Omega)\), so

$$
\|\mathcal C_\#\mu\|_{\mathrm{TV}}
=|\mu(\Omega)|.
\tag{10}
$$

Thus a pushforward may reduce total variation precisely by allowing positive and negative mass from different raw states to meet in the same retained state.

## Conditional expectation under a finite positive measure

Let \(\nu\) be finite positive, let \(R\in L^1(\nu)\), and let \(\mathcal G\subseteq\mathcal F\) be a sigma-field. The conditional expectation

$$
\mathbb E_\nu[R\mid\mathcal G]
$$

is the \(\mathcal G\)-measurable integrable function characterized by

$$
\int_A
\mathbb E_\nu[R\mid\mathcal G]\,d\nu
=
\int_A R\,d\nu,
\qquad A\in\mathcal G.
\tag{11}
$$

If \(\nu(\Omega)>0\), this is the ordinary conditional expectation after normalizing \(\nu\) to the probability measure \(\nu/\nu(\Omega)\). The zero measure is trivial.

Conditional Jensen gives

$$
\int
\left|
\mathbb E_\nu[R\mid\mathcal G]
\right|d\nu
\leq
\int|R|d\nu.
\tag{12}
$$

If \(\mathcal G_1\subseteq\mathcal G_2\), then the tower property gives

$$
\mathbb E_\nu[R\mid\mathcal G_1]
=
\mathbb E_\nu[
\mathbb E_\nu[R\mid\mathcal G_2]
\mid\mathcal G_1],
$$

and therefore

$$
\int
\left|
\mathbb E_\nu[R\mid\mathcal G_1]
\right|d\nu
\leq
\int
\left|
\mathbb E_\nu[R\mid\mathcal G_2]
\right|d\nu.
\tag{13}
$$

More conditioning retains more signed variation; more averaging can only remove it.

## Positive proposals and exact first-moment cost

Let \(Q\) be a probability measure dominating a finite signed measure \(\mu\). The canonical importance-sampling weight is

$$
W
=
\frac{d\mu}{dQ}.
$$

Then

$$
\mathbb E_Q[W]
=
\mu(\Omega),
$$

while

$$
\boxed{
\mathbb E_Q|W|
=
\|\mu\|_{\mathrm{TV}}.
}
\tag{14}
$$

Thus changing the positive proposal changes the sampled density but not the first absolute moment attached to a fixed signed measure.

Now let \(Y\in L^1(Q)\) use additional auxiliary randomness and suppose that, after a retained state \(U\) is exposed,

$$
\mathbb E_Q[Y\mid U]
=W(U).
\tag{15}
$$

Conditional Jensen gives

$$
\boxed{
\mathbb E_Q|Y|
\geq
\mathbb E_Q|W|
=
\|\mu\|_{\mathrm{TV}}.
}
\tag{16}
$$

The canonical Radon--Nikodym estimator attains equality. Hence, once the retained signed measure is fixed, auxiliary conditionally unbiased randomness cannot improve its first-moment cost.

## Nonatomic measures contain arbitrarily small nonnull pieces

A finite positive measure \(\lambda\) is *nonatomic* if no measurable set of positive measure is an atom. Equivalently for the use below, every set \(A\) with \(\lambda(A)>0\) contains a measurable subset \(B\subset A\) with

$$
0<\lambda(B)<\lambda(A).
$$

The standard divisibility theorem for finite nonatomic measures implies that for every \(A\) with \(\lambda(A)>0\) and every

$$
0<\varepsilon<\lambda(A),
$$

there exists measurable \(B\subset A\) such that

$$
0<\lambda(B)\leq\varepsilon.
\tag{17}
$$

In fact one can prescribe any value in \([0,\lambda(A)]\). For the PDE application only (17) is needed.

If \(\mu=R\nu\) and \(\nu\) is nonatomic, then

$$
|\mu|=|R|\nu
$$

is also nonatomic. Indeed, an atom of \(|\mu|\) would contain a subset on which \(\nu\) can be divided while \(|R|\nu\) remains positive, contradicting atomicity. Consequently every nonzero finite raw patch measure whose reference law has continuous Gaussian or time coordinates has nonnull sets of arbitrarily small positive total-variation mass.

This is the only measure-theoretic input needed for the sparse full-state retention construction in the capstone theorem.

## Relation to coarsened branching representations

In the quadratic-Hessian patch construction, a finite skeleton \(\tau\) has an intrinsic signed raw measure \(\mu_\tau\). A coarsening is a measurable map \(\mathcal C_\tau\) which forgets some raw variables, producing

$$
(\mathcal C_\tau)_\#\mu_\tau.
$$

The [residual signed variation characterization](residual-signed-variation-characterization-for-coarsened-patches.md) identifies the density of this pushforward with a conditional barycenter of the raw density and proves that summability of the resulting total variations is exactly the \(L^1\) criterion for the skeleton-preserving coarsened class.
