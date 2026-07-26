---
title: BABP out of equilibrium
status: proved here
tags:
  - BABP
  - out of equilibrium
  - convergence
  - patch positivity
---

# BABP out of equilibrium

This entry records established long-time results for the [biased annihilating branching process](babp-model.md) and proves a convergence result for high-density initial laws using [monomial monotonicity](monomial-monotonicity-for-high-density-measures.md). The literature results rely on the classical self-duality of BABP and its quasi-duality with the double-flip process; the high-density result instead uses the patch critical density \(p^\star=p\).

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

## High-density initial laws

The patch method treats a high-one-density range, including profiles above the quasi-thinning threshold. The [common invariant-limit theorem](common-invariant-limit-under-uniform-pure-deaths.md) is not applicable because the BABP rates vanish at the all-one configuration. Instead, the proof compares the initial law with a homogeneous product law whose convergence is already known from (1).

**Proposition.** Let \(\mathbf p_0=(p_{0,i})_{i\in\Z^d}\) satisfy

$$
p\le p_{0,i}\le p_+<1
\qquad
\text{for every }i\in\Z^d.
\tag{3}
$$

Then \(\mu_{\mathbf p_0}P_t\) converges exponentially to \(\mu_q\) on local functions.

More generally, the same conclusion holds for every probability measure \(\nu\in\mathcal M_\star\) such that

$$
0
\le
\nu(\chi_B^\star)
\le
(p_+-p)^{|B|}
\qquad
\text{for every }B\Subset\Z^d.
\tag{4}
$$

### Proof

The goal is to place the initial centered moments between those of equilibrium and those of one homogeneous product law. Since the [BABP patch critical density](patch-critical-density-for-babp.md) is \(p^\star=p\), for every nonempty finite \(B\),

$$
\begin{aligned}
\mu_q(\chi_B^\star)&=0,
\\
\mu_{\mathbf p_0}(\chi_B^\star)
&=
\prod_{i\in B}(p_{0,i}-p),
\\
\mu_{q_-}(\chi_B^\star)
&=
(p_+-p)^{|B|},
\qquad
q_-:=1-p_+>0.
\end{aligned}
\tag{5}
$$

Here \(\mu_{q_-}\) is written in the KCSM convention: its zero density is \(q_-\), so its one density is \(p_+\). Assumption (3) makes the middle term in (5) lie between the other two. BABP has bounded finite-range rates and patch positivity, so the centered-moment monotonicity theorem applies and gives, for every \(A\Subset\Z^d\),

$$
p^{|A|}
=
\mu_q(P_t\chi_A)
\le
\mu_{\mathbf p_0}(P_t\chi_A)
\le
\mu_{q_-}(P_t\chi_A).
\tag{6}
$$

The homogeneous convergence theorem (1), applied with initial vacancy density \(q_->0\), shows that the last term in (6) converges exponentially to \(p^{|A|}\). Hence the middle term does as well. Every local function is a finite linear combination of monomials, so the same conclusion holds for all local functions.

Under (4), the centered moments of \(\nu\) satisfy the same lower and upper comparisons as the middle term in (5). Repeating (6) with \(\nu\) in place of \(\mu_{\mathbf p_0}\) proves the general statement.

Condition (3) allows \(p_{0,i}>\sqrt p\), which is outside the quasi-thinning range (2), provided the profile remains uniformly bounded away from \(1\).

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
