---
title: BABP out of equilibrium
status: literature
audit: current
tags:
  - BABP
  - out of equilibrium
  - convergence
---

# BABP out of equilibrium

This entry records published long-time results for the [biased annihilating branching process](babp-model.md): stationary-measure classification, convergence from product initial laws, and finite-particle results. The arguments in the cited literature use classical duality and quasi-duality methods.

**References.** Neuhauser and Sudbury, *The biased annihilating branching process*; Sudbury and Lloyd, *Quantum operators in classical probability theory. II. The concept of duality in interacting particle systems*; Sudbury and Lloyd, *Quantum operators in classical probability theory. IV. Quasi-duality and thinnings of interacting particle systems*; Sudbury, *Hunting submartingales in the jumping voter model and the biased annihilating branching process*; Martinelli, Shapira, and Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*.

Throughout, BABP is on \(\Z^d\) with nearest-neighbour sets, \(q\in(0,1)\) is the equilibrium density of zeros, \(p=1-q\), and \((P_t)_{t\ge0}\) is its semigroup.

## Stationary measures

The Bernoulli product measure \(\mu_q\) is reversible, while the point mass \(\delta_{\mathbf1}\) at the all-one configuration is invariant. On \(\Z\), every stationary probability measure is of the form

$$
a\mu_q+(1-a)\delta_{\mathbf1},
\qquad
a\in[0,1].
$$

In every dimension, the same classification holds among translation-invariant stationary probability measures.

The one-dimensional statement is due to Neuhauser and Sudbury; Martinelli, Shapira, and Toninelli give the general KCM argument and its translation-invariant higher-dimensional form in Corollary 2.9.

## Homogeneous product initial laws

For every initial vacancy density \(q_0>0\), BABP started from the homogeneous product law \(\mu_{q_0}\) converges exponentially to \(\mu_q\). More precisely, for every [local function](local-functions.md) \(f\), there are constants \(c>0\) and \(C_f<\infty\) such that

$$
\left|
\mu_{q_0}(P_tf)-\mu_q(f)
\right|
\le
C_fe^{-ct}.
\tag{1}
$$

This holds for every \(q\in(0,1)\) and every \(d\ge1\). It is Application 2 and Section 5.1.1 of Martinelli, Shapira, and Toninelli. Their proof combines BABP self-duality and quasi-duality with exponential ergodicity of the double-flip process.

The quasi-thinning argument also treats some inhomogeneous product laws. If

$$
\mathbf p_0=(p_{0,i})_{i\in\Z^d}
$$

is the initial one-density profile and

$$
p_{0,i}\le\sqrt p
\qquad
\text{for every }i\in\Z^d,
\tag{2}
$$

then \(\mu_{\mathbf p_0}P_t\) converges exponentially to \(\mu_q\). This is the inhomogeneous extension in their Remark 5.5.

## Finite particle starts

Let

$$
B_t=\{i\in\Z^d:\eta_t(i)=0\}
$$

be the BABP particle set. Starting from any finite nonempty \(B_0\), there are positive constants \(a,c,C\) such that

$$
\mathbb P\left(|B_t|\le at\right)
\le
Ce^{-ct}
$$

for all sufficiently large \(t\). In one dimension, finite propagation also gives a linear upper bound, so \(|B_t|\) is of linear order almost surely.

The exponential lower-tail estimate is Application 1 and Section 5.1.1 of Martinelli, Shapira, and Toninelli.

Convergence from a finite nonempty particle set is a different question. On \(\Z\), it is known when

$$
\lambda=\frac qp>0.0347.
$$

This is Sudbury's Theorem 7; Martinelli, Shapira, and Toninelli summarize the finite-seed status in Remark 5.4. The corresponding convergence statement for every \(\lambda>0\) remains open.
