---
title: Integrable regime of the coding tree
status: observation
tags:
  - PDE
  - coding tree
  - integrability
  - branching process
---

# Integrable regime of the coding tree

The absolute-integrability hypothesis in the [Nguwi--Penent--Privault Feynman--Kac theorem](npp-coding-tree-feynman-kac-theorem.md) is nonvacuous: there are simple choices of the nonlinearity for which every code-rooted functional is integrable. Separately, the uniform offspring-probability bound used in the printed proof of Nguwi--Penent--Privault Proposition 4.3 appears not to be available for the full infinite code class. This is an observation about that sufficient-condition argument, not about the coding-tree construction or Theorem 4.2 itself.

**References.** Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882, Definitions 2.1--2.2 and Proposition 4.3.

## Observation

Consider the linear heat equation obtained by taking

$$
f\equiv0,
$$

with smooth terminal data \(\phi\) whose derivatives have finite heat-kernel averages; bounded derivatives are more than sufficient. For an identity-rooted tree, a branching event produces the zero composite code \(f^*\), so every branched contribution vanishes. The only nonzero contribution is the event that the root survives to \(T\), and cancellation of the survival probability gives

$$
\mathbb E\left[
|H(\mathcal T_{t,x,\operatorname{Id}})|
\right]
=
P_{T-t}|\phi|(x)
<\infty.
$$

The same reasoning applies to a root \(\partial_x^k\): survival gives \(P_{T-t}|\phi^{(k)}|(x)\), while every branching term contains a derivative of \(f\) and therefore vanishes. Composite codes built from derivatives of \(f\) have zero terminal value and zero contribution. Thus the all-code \(L^1\) requirement is realized in this elementary regime.

## Observation on Proposition 4.3

In the Nguwi--Penent--Privault construction, the offspring tuple \(I_c\) is sampled uniformly from the finite mechanism set \(\mathcal M(c)\). Hence, for fixed \(c\),

$$
q_c(I_c)
=
\frac{1}{|\mathcal M(c)|}.
\tag{1}
$$

Proposition 4.3 assumes a decreasing lifetime density and uses the displayed condition

$$
\rho(T)
>
\frac{1}{\min_{c\in\mathcal C}q_c(I_c)}.
\tag{2}
$$

Its proof then bounds every internal reciprocal sampling factor by the same quantity involving \(\min_{c\in\mathcal C}q_c(I_c)\).

For the full code class, Definition 2.2 gives mechanism sets \(\mathcal M(\partial_x^k)\) whose cardinalities grow with \(k\). One can already see this from the Faà di Bruno terms obtained by splitting \(k\) into two distinct positive derivative orders: for each

$$
1\leq a<k-a,
$$

there is a distinct tuple containing spatial derivative codes of orders \(a\) and \(k-a\). Consequently,

$$
|\mathcal M(\partial_x^k)|
\geq
\left\lfloor\frac{k-1}{2}\right\rfloor,
$$

and therefore

$$
\inf_{c\in\mathcal C}q_c(I_c)=0.
\tag{3}
$$

Thus the positive uniform lower bound on offspring-selection probabilities used in the printed proof is not available on the unrestricted code class. As written, this leaves a gap in that uniform argument unless the family of codes is restricted, the offspring law is modified, or another estimate supplies the missing uniform control.

This observation should be read narrowly. Proposition 4.3 is presented as a sufficient small-time criterion; the issue above concerns the scope of its printed uniform proof. The [coding-tree Feynman--Kac theorem](npp-coding-tree-feynman-kac-theorem.md) itself remains conditional on all-code \(L^1\) integrability, and the elementary example above shows that this condition is not empty.