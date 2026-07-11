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

For a patch-positive spin system with a uniform pure-death component, evolved [monomials](monomials.md) have a common limit for a class of Bernoulli product initial laws extending below the patch critical density. The limit is the contribution of the finite complete patch families.

**References.** None yet.

## Theorem

Let \(\cL\) be the generator of a spin system with the [patch positivity property](patch-positivity-property.md), and suppose that there is \(\varepsilon>0\) such that

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

If

$$
\mathbf p^\star\le\frac12\mathbf 1,
$$

then the spin system is [ergodic](ergodicity.md).

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

At horizon \(t>T\), write

$$
L_{T,t}
=
\left\{
\text{no successful interactions occur between times }T\text{ and }t
\right\}.
$$

These events decrease to \(L_T\) as \(t\to\infty\). We split (3) using \(L_{T,t}\), which is determined by the successful-interaction skeleton up to the current horizon.

We first prove

$$
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_{T,t}^c)
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

On \(L_{T,t}^c\), choose the first successful interaction after time \(T\), and let \(u\le t\) be its time. Equations (1) and (5) contribute a factor at most

$$
e^{-\varepsilon u}
\le
e^{-\varepsilon T}.
$$

Thus the trail supplies the required exponential factor. Equations (1) and (2) dominate all remaining factors by the nonnegative all-one patch weight of \(\cL^\varepsilon\). Therefore

$$
\begin{aligned}
\left|
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_{T,t}^c)
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

Fix \(T<\infty\). On \(L_T\), all finite full patches have stabilized once \(t>T\), while every end patch at horizon \(t\) is the truncation of an infinite full patch and has length at least \(t-T\). By the definition of the [contribution of an infinite patch](patch-contribution.md#contributions-of-full-patches), each end contribution converges to \(C(P)\), independently of \(\mathbf p\). Since only finitely many patches occur on \(L_T\), the patch product converges. On \(L_T^c\), a successful interaction occurs after \(T\), so \(L_{T,t}\) fails for all sufficiently large \(t\). Therefore

$$
W_t^{\mathbf p}\ind(L_{T,t})
\longrightarrow
\left(
\prod_{P\in\mathcal P}C(P)
\right)
\ind(L_T).
$$

The comparison with the all-one patch weights of \(\cL^\varepsilon\) permits passage to expectations, so

$$
\lim_{t\to\infty}
\mathbb E_A\left[
W_t^{\mathbf p}\ind(L_{T,t})
\right]
=
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind(L_T)
\right].
\tag{7}
$$

All full-patch contributions in (7) are nonnegative. Since \(L_T\) increases to \(L_\infty\), monotone convergence gives

$$
\lim_{T\to\infty}
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind(L_T)
\right]
=
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind\left(\left|\mathcal P\right|<\infty\right)
\right].
\tag{8}
$$

Combining (3), (4), (7), and (8), for every \(T<\infty\),

$$
\begin{aligned}
\limsup_{t\to\infty}
\left|
\mu_{\mathbf p}\bigl(P_t(\chi_A)\bigr)
-
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind\left(\left|\mathcal P\right|<\infty\right)
\right]
\right|
\le{}&
e^{-\varepsilon T}
\\
&+
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind(L_\infty\setminus L_T)
\right].
\end{aligned}
$$

The right-hand side tends to zero as \(T\to\infty\), proving the limit. The estimates are uniform in \(\mathbf p\ge\mathbf p^-\), so averaging over a mixing law gives the same result for mixtures.

Finally, if \(\mathbf p^\star\le\frac12\mathbf 1\), then \(\mathbf p^-=\mathbf 0\). Every deterministic law is a product measure because

$$
\delta_\xi=\mu_{\mathbf \xi}.
$$

Thus \(P_t(\chi_A)(\xi)\) has the same limit for every initial configuration \(\xi\). Finite monomial expansions extend this to all local functions. Compactness gives a limiting probability measure, the semigroup property makes it invariant, and convergence from every initial law makes it unique. Hence the spin system is ergodic.
