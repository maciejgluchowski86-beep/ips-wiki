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

We first prove

$$
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_T^c)
\right]
\right|
\le
e^{-\varepsilon T},
\qquad t>T.
\tag{4}
$$

Every successful interaction \((i,u,S)\) has a trail of patches leading to its source. To construct it, trace the active source at time \(u\) backwards. It either descends from an initially active site or was activated as the target of an earlier successful interaction. Iterating backwards and then reversing the sequence gives a trail from time \(0\) to time \(u\). Every patch in the trail ends at an outgoing touch, hence is of type \(\mathsf{XO}\), and

$$
\sum_{P\text{ in the trail}}\Delta(P)\ge u.
\tag{5}
$$

On \(L_T^c\), choose the first successful interaction after time \(T\), and let \(u\) be its time. If \(u\le t\), equations (1) and (5) contribute a factor at most

$$
e^{-\varepsilon u}
\le
e^{-\varepsilon T}.
$$

If \(u>t\), the trail crosses the time horizon. Up to time \(t\) it consists of \(\mathsf{XO}\) patches followed by one active end patch, and its total length is \(t>T\). Applying the noise comparison before integrating the final active patch again gives a factor at most \(e^{-\varepsilon T}\). Thus in both cases the trail supplies the required exponential factor. Equations (1) and (2) dominate all remaining factors by the nonnegative all-one patch weight of \(\cL^\varepsilon\). Therefore

$$
\begin{aligned}
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_T^c)
\right]
\right|
&\le
e^{-\varepsilon T}
\,\mu_{\mathbf 1}\bigl(P_t^\varepsilon(\chi_A)\bigr)
\\
&\le
e^{-\varepsilon T},
\end{aligned}
$$

which proves (4).

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
\tag{6}
$$

Fix \(T<\infty\). On \(L_T\), the set \(\mathcal B_t\) is independent of \(t\) once \(t>T\). The sites carrying end patches are also independent of \(t\), because starting or ending a patch requires a successful interaction. Denote the corresponding infinite patches by \(\mathcal E_\infty\).

Every \(P\in\mathcal E_t\) has length at least \(t-T\). The explicit end-patch formulas and the pure-death comparison give

$$
\left|
\prod_{P\in\mathcal E_t}C^{\mathbf p}(P)
-
\prod_{P\in\mathcal E_\infty}C(P)
\right|
\le
K\left|\mathcal E_T\right|
e^{-\varepsilon(t-T)}
$$

after the remaining factors have been dominated by the all-one contributions of \(\cL^\varepsilon\). The sites carrying end patches are precisely the initially active sites together with the sites touched by successful interactions before time \(T\). Finite spread of information and polynomial volume growth therefore give

$$
\mathbb E_A\left[\left|\mathcal E_T\right|\right]
\le
K_A(1+T)^D.
$$

Consequently,

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
K_A(1+T)^D e^{-\varepsilon(t-T)}.
\tag{7}
$$

All full-patch contributions are nonnegative. On \(L_\infty\setminus L_T\), the finite complete patch family contains a successful interaction after time \(T\), hence an \(\mathsf{XO}\)-trail of total length greater than \(T\). The same comparison used in (4) gives

$$
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind(L_\infty\setminus L_T)
\right]
\le
e^{-\varepsilon T}.
\tag{8}
$$

Combining (3), (4), (7), and (8) gives

$$
\begin{aligned}
\left|
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind\left(\left|\mathcal P\right|<\infty\right)
\right]
\right|
\le{}&
2e^{-\varepsilon T}
\\
&+
K_A(1+T)^D e^{-\varepsilon(t-T)}.
\end{aligned}
\tag{9}
$$

Taking \(T=t/2\) proves the stated estimate and the limit. The estimates are uniform in \(\mathbf p\ge\mathbf p^-\), so averaging over a mixing law gives the same result for mixtures.

Finally, if \(\mathbf p^\star\le\frac12\mathbf 1\), then \(\mathbf p^-=\mathbf 0\). Every deterministic law is a product measure because

$$
\delta_\xi=\mu_{\mathbf \xi}.
$$

Thus \(P_t(\chi_A)(\xi)\) has the same limit for every initial configuration \(\xi\), with a bound uniform in \(\xi\). Finite monomial expansions extend this to all local functions. Compactness gives a limiting probability measure, the semigroup property makes it invariant, and convergence from every initial law makes it unique. Absorbing the polynomial factor into a slightly smaller exponential rate proves uniform exponential ergodicity on local functions.
