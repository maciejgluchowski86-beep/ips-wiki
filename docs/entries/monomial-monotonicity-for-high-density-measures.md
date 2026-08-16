---
title: Centered-moment order preservation
status: proved here
audit: current
tags:
  - patch positivity
  - centered moments
  - monotonicity
  - moment order
---

# Centered-moment order preservation

Let a spin system be [patch positive](patch-positivity-property.md), with [patch threshold profile](patch-critical-density.md) $\mathbf p^\star$. Use the centered monomials, order $\preceq_*$, and cone $\mathcal M_*$ from [centered-moment order and cones](high-density-measure.md).

## Centered end-factor expansion

For every end patch $P$ based at $i$, the map $z\mapsto C(z,P)$ is affine and nondecreasing, and it is nonnegative for $z\ge p_i^\star$. Define its slope

$$
\kappa(P)=\partial_z C(z,P)\ge0.
$$

Then

$$
C(z,P)
=
C(p_{i(P)}^\star,P)
+
\kappa(P)(z-p_{i(P)}^\star),
\qquad
C(p_{i(P)}^\star,P)\ge0.
\tag{1}
$$

Distinct end patches are based at distinct sites. Therefore, for every probability measure $\mu$,

$$
\begin{aligned}
&\mu\left(
\prod_{P\in\mathcal E_t}C(\eta(i(P)),P)
\right)\\
&\quad=
\sum_{\mathcal Q\subseteq\mathcal E_t}
\mu\left(
\chi^*_{\{i(P):P\in\mathcal Q\}}
\right)
\prod_{P\in\mathcal Q}\kappa(P)
\prod_{P\in\mathcal E_t\setminus\mathcal Q}
C(p_{i(P)}^\star,P).
\end{aligned}
\tag{2}
$$

If $\mu\in\mathcal M_*$, every term in (2) is nonnegative. Together with patch positivity, this makes the weight of each successful-interaction skeleton nonnegative. Formula (2) also immediately gives ordinary monomial comparisons under $\preceq_*$. Preservation of the centered order itself needs a separate centered-basis argument.

## Theorem

For probability measures $\mu$ and $\nu$,

$$
\mu\preceq_*\nu
\quad\Longrightarrow\quad
\mu P_t\preceq_*\nu P_t
\qquad(t\ge0).
\tag{3}
$$

No assumption that $\mu$ or $\nu$ belongs to $\mathcal M_*$ is required. The semigroup also preserves $\mathcal M_*$, and

$$
\mu\preceq_*\nu
\quad\Longrightarrow\quad
(\mu P_t)(\chi_A)\le(\nu P_t)(\chi_A)
\tag{4}
$$

for every finite $A$. In particular,

$$
(\mu_{\mathbf p^\star}P_t)(\chi_A)
\le
(\mu P_t)(\chi_A)
\qquad
(\mu\in\mathcal M_*).
$$

## Proof in the centered-monomial basis

For $S\subseteq N(i)$ set

$$
h_i(S)
=
c_i^0(S)-p_i^\star\bigl(c_i^0(S)+c_i^1(S)\bigr),
\tag{5}
$$

and, for nonempty $S$, set

$$
b_i(S)=-c_i^0(S)-c_i^1(S).
\tag{6}
$$

Patch positivity gives $b_i(S)\ge0$. It also gives $h_i(S)\ge0$: for nonempty $S$, this is exactly the threshold inequality encoded by the coefficient formula for $p_i^\star$; for $S=\varnothing$, it follows from the empty-neighbour bound

$$
p_i^\star
\le
\frac{c_i^0(\varnothing)}{c_i^0(\varnothing)+c_i^1(\varnothing)}.
$$

At a site with $r_i=c_i^0(\varnothing)+c_i^1(\varnothing)=0$, patch positivity forces $c_i\equiv0$, so all these coefficients vanish.

A direct generator calculation gives

$$
\mathcal L\chi_A^*
=
\sum_{i\in A}
\left[
-r_i\chi_A^*
+
\sum_{S\subseteq N(i)}
 h_i(S)\chi_S\chi_{A\setminus\{i\}}^*
+
\sum_{\substack{S\subseteq N(i)\\S\ne\varnothing}}
 b_i(S)\chi_S\chi_A^*
\right].
\tag{7}
$$

To express the products on the right in the centered basis, let $B,S\Subset\Lambda$. Since

$$
\eta(j)igl(\eta(j)-p_j^\star\bigr)
=(1-p_j^\star)\eta(j),
$$

and

$$
\eta(j)=p_j^\star+(\eta(j)-p_j^\star),
$$

one obtains

$$
\chi_S\chi_B^*
=
\left(\prod_{j\in S\cap B}(1-p_j^\star)\right)
\sum_{R\subseteq S}
\left(\prod_{j\in S\setminus R}p_j^\star\right)
\chi_{R\cup(B\setminus S)}^*.
\tag{8}
$$

Every coefficient in (8) is nonnegative.

Fix a finite zero-boundary volume. In the finite family of centered monomials supported there, (7)-(8) show that the matrix of $\mathcal L$ has nonnegative off-diagonal entries: all coefficients that move one centered monomial into another are built from the nonnegative $h_i(S)$, $b_i(S)$, $p_j^\star$, and $1-p_j^\star$. A zero-boundary restriction only removes terms whose coefficient sets meet the exterior, so it preserves these signs.

A finite matrix with nonnegative off-diagonal entries is Metzler. Its exponential therefore has nonnegative entries. Hence, in finite volume, if a finite signed measure $\lambda$ satisfies

$$
\lambda(\chi_B^*)\ge0
\qquad\text{for every finite }B,
$$

then

$$
(\lambda P_t^{R,0})(\chi_A^*)\ge0
$$

for every $A$ supported in the volume.

By [finite propagation](finite-propagation-for-zero-boundary-restrictions.md), $P_t^{R,0}\chi_A^*$ converges uniformly to $P_t\chi_A^*$ along an exhaustion. Passing to the limit gives

$$
(\lambda P_t)(\chi_A^*)\ge0.
\tag{9}
$$

Apply (9) to $\lambda=\nu-\mu$. The hypothesis $\mu\preceq_*\nu$ is exactly the assertion that $\lambda(\chi_B^*)\ge0$ for every finite $B$, so (9) proves (3).

Apply (9) directly to $\lambda=\mu$ when $\mu\in\mathcal M_*$. This proves preservation of $\mathcal M_*$. Finally,

$$
\chi_A
=
\sum_{B\subseteq A}
\left(\prod_{i\in A\setminus B}p_i^\star\right)
\chi_B^*,
\tag{10}
$$

and all coefficients in (10) are nonnegative. Combining (3) with (10) gives the ordinary monomial comparison (4).

## Product-profile comparisons

Let $\mu_{\mathbf p}$ denote the Bernoulli product law with calm-state density profile $\mathbf p$.

If

$$
\mathbf p^\star\le\mathbf p\le\mathbf q,
$$

then, for every finite $B$,

$$
\mu_{\mathbf p}(\chi_B^*)
=
\prod_{i\in B}(p_i-p_i^\star)
\le
\prod_{i\in B}(q_i-p_i^\star)
=
\mu_{\mathbf q}(\chi_B^*).
$$

Thus $\mu_{\mathbf p}\preceq_*\mu_{\mathbf q}$ and

$$
(\mu_{\mathbf p}P_t)(\chi_A)
\le
(\mu_{\mathbf q}P_t)(\chi_A).
\tag{11}
$$

There is also a comparison across the centering profile. If

$$
\mathbf q\le\mathbf p
\qquad\text{and}\qquad
\mathbf q+\mathbf p\ge2\mathbf p^\star,
$$

then

$$
|q_i-p_i^\star|\le p_i-p_i^\star
$$

for each $i$, and hence

$$
\prod_{i\in B}(q_i-p_i^\star)
\le
\left|\prod_{i\in B}(q_i-p_i^\star)\right|
\le
\prod_{i\in B}(p_i-p_i^\star).
$$

Therefore $\mu_{\mathbf q}\preceq_*\mu_{\mathbf p}$ and (11) again holds. These are centered-moment and monomial-moment comparisons, not stochastic-domination statements. The same arguments apply to mixtures of product laws whenever the mixing profiles can be coupled to satisfy the corresponding coordinatewise inequalities almost surely.

## Convergence by centered-moment comparison

Suppose

$$
\underline\mu\preceq_*\mu\preceq_*\overline\mu.
$$

If both $\underline\mu P_t$ and $\overline\mu P_t$ converge weakly to the same probability measure $\pi$, then

$$
\mu P_t\Rightarrow\pi.
\tag{12}
$$

Indeed, (3) traps every centered moment of $\mu P_t$ between the corresponding centered moments of the two comparison laws. Centered monomials determine weak convergence on $\{0,1\}^\Lambda$.

More quantitatively, if $\rho(t)\to0$ and for each finite $A$,

$$
\max_{\lambda\in\{\underline\mu,\overline\mu\}}
\left|
(\lambda P_t)(\chi_A^*)-\pi(\chi_A^*)
\right|
\le C_A\rho(t),
$$

then every local function $f$, expanded in the centered-monomial basis, satisfies

$$
|(\mu P_t)(f)-\pi(f)|
\le C_f\rho(t)
$$

for some finite $C_f$.
