---
title: Monomial convergence under uniform pure deaths
status: proved here
tags:
  - patch positivity
  - pure deaths
  - monomials
  - convergence
---

# Monomial convergence under uniform pure deaths

For a patch-positive spin system with a uniform pure-death component, evolved [monomials](monomials.md) have a common limit for a class of Bernoulli product initial laws extending below the patch critical density. On a polynomial-growth lattice the convergence is exponential, up to a polynomial prefactor. The limit is the contribution of the finite complete patch families.

**References.** None yet.

## Theorem

Let \(\Lambda\) be a [polynomial-growth lattice](polynomial-growth-lattice.md) with exponent \(D\), and let \(\cL\) be the generator of a uniformly bounded finite-range spin system with the [patch positivity property](patch-positivity-property.md). Suppose that there is \(\varepsilon>0\) such that

$$
c_i^1(\xi)\ge\varepsilon
\qquad
\text{for every }i\in\Lambda
\text{ and }\xi\in\{0,1\}^{\Lambda}.
$$

Equivalently,

$$
\cL
=
\cL^\varepsilon+\varepsilon\mathcal N^0,
\qquad
\mathcal N^0f(\xi)
=
\sum_{i\in\Lambda}
\xi(i)\left(f(\xi^{i,0})-f(\xi)\right),
$$

where \(\cL^\varepsilon\) is another spin-system generator. Let

$$
\mathbf p^-
=
\left(2\mathbf p^\star-\mathbf 1\right)\vee\mathbf 0.
$$

Then, for every \(A\Subset\Lambda\) and every one-density profile \(\mathbf p\ge\mathbf p^-\),

$$
\lim_{t\to\infty}
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
=
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind\left(\left|\mathcal P\right|<\infty\right)
\right].
$$

Here \(\mathcal P\) is the full [patch](patch.md) family of the signed dual started from \(A\), and the integrand is defined to be zero when \(\left|\mathcal P\right|=\infty\). The right-hand side is independent of \(\mathbf p\). Consequently, the same limit holds for every mixture of Bernoulli product measures supported on profiles above \(\mathbf p^-\).

Moreover, there is \(K_A<\infty\) such that

$$
\left|
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind\left(\left|\mathcal P\right|<\infty\right)
\right]
\right|
\le
K_A(1+t)^D e^{-\varepsilon t/2}.
$$

If

$$
\mathbf p^\star\le\frac12\mathbf 1,
$$

then the spin system is uniformly exponentially [ergodic](ergodicity.md) on local functions.

## Proof

By the [duality noise lemma](duality-noise-lemma.md), \(\cL\) and \(\cL^\varepsilon\) have the same signed dual process and the same full [successful-interaction](successful-interaction.md) set \(\mathcal I\). Write \(P_t^\varepsilon\) and \(C^\varepsilon\) for the semigroup and patch contributions associated with \(\cL^\varepsilon\).

The patch formulas give

$$
0\le C(P)\le C^\varepsilon(P)
$$

for every finite patch. If \(P\) has terminal type \(\mathsf O\), so that its type is \(\mathsf{XO}\) with \(\mathsf X\in\{\mathsf S,\mathsf I,\mathsf O\}\), then the patch is active throughout and the comparison is exact:

$$
C(P)
=
e^{-\varepsilon\Delta(P)}C^\varepsilon(P).
\tag{1}
$$

The patch critical density is unchanged because the pure-death perturbation changes only the empty coefficient \(c_i^1(\vn)\). Since

$$
\mathbf p+\mathbf 1\ge2\mathbf p^\star,
$$

the reflected comparison from [monomial monotonicity for high-density measures](monomial-monotonicity-for-high-density-measures.md#domination-below-the-critical-density) gives, for every end patch,

$$
\left|C^{\mathbf p}(P)\right|
\le
C^{\mathbf 1}(P)
\le
C^{\varepsilon,\mathbf 1}(P).
\tag{2}
$$

Set

$$
W_t^{\mathbf p}
=
\prod_{P\in\mathcal B_t}C(P)
\prod_{P\in\mathcal E_t}C^{\mathbf p}(P).
$$

The positive comparison weight is

$$
\widehat W_t
=
\prod_{P\in\mathcal B_t}C^\varepsilon(P)
\prod_{P\in\mathcal E_t}C^{\varepsilon,\mathbf 1}(P).
$$

Its total mass satisfies

$$
\mathbb E_A\left[\widehat W_t\right]
=
\mu_{\mathbf 1}\bigl(P_t^\varepsilon(\chi_A)\bigr)
\le1.
$$

The Bernoulli-averaged [patch representation](patch-representation-of-spin-systems.md) reads

$$
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
=
\mathbb E_A\left[W_t^{\mathbf p}\right].
\tag{3}
$$

For \(T<\infty\), let

$$
L_T
=
\left\{
\text{no successful interactions occur after time }T
\right\}.
$$

For \(t>T\), let

$$
L_{T,t}
=
\left\{
\text{no successful interactions occur between times }T\text{ and }t
\right\}.
$$

We first prove

$$
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_T^c)
\right]
\right|
\le
e^{-\varepsilon T}
+
K_A(1+T)^D e^{-\varepsilon(t-T)},
\qquad t>T.
\tag{4}
$$

Every successful interaction \((i,u,S)\) has a trail of patches leading to its source. To construct it, trace the active source at time \(u\) backwards. It either descends from an initially active site or was activated as the target of an earlier successful interaction. Iterating backwards and then reversing the sequence gives a trail from time \(0\) to time \(u\). Every patch in the trail ends at an outgoing touch, hence is of type \(\mathsf{XO}\), and

$$
\sum_{P\text{ in the trail}}\Delta(P)\ge u.
\tag{5}
$$

First consider \(L_T^c\cap L_{T,t}^c\). Choose the first successful interaction after time \(T\), and let \(u\le t\) be its time. Equations (1) and (5) contribute a factor at most

$$
e^{-\varepsilon u}
\le
e^{-\varepsilon T}.
$$

Equations (1) and (2) dominate all remaining factors by \(\widehat W_t\), so this part of the expectation is at most \(e^{-\varepsilon T}\).

It remains to consider \(L_T^c\cap L_{T,t}\).

Although a successful interaction occurs after \(t\), there need not be an \(\mathsf{XO}\)-trail reaching time \(T\) within the horizon-\(t\) patch family. Instead, at least one end-patch site must remain active throughout the interval from \(T\) to \(t\). Indeed, without a successful interaction during that interval, a site that becomes inactive cannot be reactivated, and extinction of all end-patch sites would make every later successful interaction impossible.

For this estimate, temporarily undo the patch-internal averaging in \(W_t^{\mathbf p}\) and use the pre-averaged factors from the patch representation. Then

$$
\begin{aligned}
&\ind\left(
L_T^c\cap L_{T,t}
\right)
\\
&\qquad\le
\sum_{P\in\mathcal E_t}
\ind\left(
L_T^c\cap L_{T,t}
\cap
\left\{
X_u^P=1
\text{ for every }u\in[T,t]
\right\}
\right).
\end{aligned}
\tag{6}
$$

Condition on \(\cG_t\). This fixes the end patches and leaves their internal data independent. On the event in the summand of (6), the pure-death noise acts for at least \(t-T\) units of active time. Removing this noise and replacing the terminal density by \(\mathbf 1\) bounds that summand by

$$
e^{-\varepsilon(t-T)}\widehat W_t.
$$

On \(L_{T,t}\), the end-patch sites at time \(t\) are the end-patch sites at time \(T\). Finite spread of information on a polynomial-growth lattice gives the marked comparison estimate

$$
\mathbb E_A\left[
\left|\mathcal E_T\right|\widehat W_t
\right]
\le
K_A(1+T)^D.
\tag{7}
$$

Summing (6), taking the conditional expectation, and then removing the conditioning gives the second term in (4). This proves the late-term estimate.

Define

$$
L_\infty
=
\bigcup_{T<\infty}L_T.
$$

Local finiteness gives

$$
L_\infty
=
\left\{
\left|\mathcal I\right|<\infty
\right\}
=
\left\{
\left|\mathcal P\right|<\infty
\right\}.
\tag{8}
$$

Fix \(T<\infty\). On \(L_T\), the set \(\mathcal B_t\) is independent of \(t\) once \(t>T\). The sites carrying end patches are also independent of \(t\), because starting or ending a patch requires a successful interaction. Denote the corresponding infinite patches by \(\mathcal E_\infty\).

For \(P\in\mathcal E_\infty\), let \(P^{(t)}\in\mathcal E_t\) be its truncation and set

$$
\widehat C_t(P)
=
C^{\varepsilon,\mathbf 1}(P^{(t)}),
\qquad
\Delta_t(P)
=
\left|
C^{\mathbf p}(P^{(t)})-C(P)
\right|.
$$

The comparison cannot in general be made relative to \(C(P)\), because the limiting contribution may vanish. Instead, the patch formulas give a uniform \(\kappa<\infty\) such that

$$
0\le C(P)\le\widehat C_t(P),
\qquad
\Delta_t(P)
\le
\kappa e^{-\varepsilon(t-T)}\widehat C_t(P).
\tag{9}
$$

To see the second inequality, compare the finite and infinite versions of the same end patch before integrating its internal randomness. They differ only on the part of the local patch law on which the site remains active until time \(t\). Since the patch starts no later than \(T\), pure-death noise contributes at most \(e^{-\varepsilon(t-T)}\) on this part. Removing that noise and replacing the terminal density by \(\mathbf 1\) gives \(\widehat C_t(P)\). In the unnormalized patch factor one may take \(\kappa=1\); the uniform constant above also covers the fixed consistency normalizations in the displayed patch formulas.

Expanding each finite contribution as its limit plus an error and applying (9) gives

$$
\left|
\prod_{P\in\mathcal E_t}C^{\mathbf p}(P)
-
\prod_{P\in\mathcal E_\infty}C(P)
\right|
\le
\prod_{P\in\mathcal E_\infty}\widehat C_t(P)
\left[
\left(
1+\kappa e^{-\varepsilon(t-T)}
\right)^{|\mathcal E_\infty|}
-1
\right].
\tag{10}
$$

We now use finite spread in the stronger factorial-moment form required by (10). Put \(N_T=|\mathcal E_T|\). For every \(k\ge1\), graphical path counting gives

$$
\mathbb E_A\left[
\widehat W_t
\binom{N_T}{k}
\ind(L_T)
\right]
\le
\frac{\left(K_A(1+T)^D\right)^k}{k!}.
\tag{11}
$$

Indeed, every end-patch site is either in \(A\) or is reached by a graphical path of successful interactions before time \(T\). For \(k\) distinct sites, sum over the corresponding \(k\)-tuples of graphical paths. Uniformly bounded finite-range interaction rates give the usual finite-speed path bound, and polynomial volume growth leaves at most order \((1+T)^{Dk}\) choices. Division by \(k!\) removes the ordering of the selected sites. The positive all-one comparison weight has total mass at most one, so the same counting applies with the factor \(\widehat W_t\).

Let

$$
a_{t,T}
=
\kappa e^{-\varepsilon(t-T)}.
$$

Multiplying (10) by the bulk factors, using their comparison with \(C^\varepsilon\), expanding the power, and applying (11) yields

$$
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_T)
\right]
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind(L_T)
\right]
\right|
\le
\exp\left(
K_A(1+T)^D a_{t,T}
\right)-1.
\tag{12}
$$

All full-patch contributions are nonnegative. On \(L_\infty\setminus L_T\), the finite complete patch family contains a successful interaction after time \(T\), hence an \(\mathsf{XO}\)-trail of total length greater than \(T\). The same comparison used for the first part of (4) gives

$$
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind(L_\infty\setminus L_T)
\right]
\le
e^{-\varepsilon T}.
\tag{13}
$$

Combining (3), (4), (12), and (13) gives

$$
\begin{aligned}
&\left|
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind\left(\left|\mathcal P\right|<\infty\right)
\right]
\right|
\\
&\qquad\le
2e^{-\varepsilon T}
+
K_A(1+T)^D e^{-\varepsilon(t-T)}
\\
&\qquad\quad+
\exp\left(
K_A(1+T)^D\kappa e^{-\varepsilon(t-T)}
\right)-1.
\end{aligned}
\tag{14}
$$

Take \(T=t/2\). For all sufficiently large \(t\), the exponent in the last line is at most one, so \(e^x-1\le2x\) shows that the right-hand side is bounded by

$$
K_A'(1+t)^D e^{-\varepsilon t/2}.
$$

Increasing \(K_A'\) handles bounded \(t\), proving the stated estimate and the limit. The estimates are uniform in \(\mathbf p\ge\mathbf p^-\), so averaging over a mixing law gives the same result for mixtures.

Finally, if \(\mathbf p^\star\le\frac12\mathbf 1\), then \(\mathbf p^-=\mathbf 0\). Every deterministic law is a product measure because

$$
\delta_\xi=\mu_{\mathbf \xi}.
$$

Thus \(P_t(\chi_A)(\xi)\) has the same limit for every initial configuration \(\xi\), with a bound uniform in \(\xi\). Finite monomial expansions extend this to all local functions. Compactness gives a limiting probability measure, the semigroup property makes it invariant, and convergence from every initial law makes it unique. Absorbing the polynomial factor into a slightly smaller exponential rate proves uniform exponential ergodicity on local functions.
