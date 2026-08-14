---
title: Canonical raw signed measures for finite quadratic-Hessian trees
status: proved here
tags:
  - PDE
  - Duhamel tree
  - signed measure
  - total variation
  - Holder regularity
  - Hessian
  - patch
---

# Canonical raw signed measures for finite quadratic-Hessian trees

For the quadratic Hessian equation, later notions such as raw-faithfulness, coarsening, total variation, and conditional barycenters require an actual finite signed measure on an actual measurable raw mark space for every fixed finite Duhamel tree. This entry constructs that measure and proves its finiteness.

The key point is finite-depth rather than uniform-in-depth. A centered Hessian edge maps an \(L^1\)-valued \(C^\eta\) field into an \(L^1\)-valued \(C^\beta\) field for every \(0<\beta<\eta<1\), with an integrable time singularity \(r^{-1+(\eta-\beta)/2}\). Hence a fixed finite tree is absolutely integrable after spending an arbitrarily small positive amount of spatial regularity at each edge. The constants need not remain geometric as the depth grows. This is compatible with the [Banach-scale obstruction](banach-scale-obstruction-for-raw-pde-patches.md), whose \((cn/\Delta)^n\) lower bound concerns depth-uniform stepwise constants, not existence of a finite first moment at each fixed depth.

The construction below is the canonical centered raw object used by the [raw-barycenter obstruction](raw-marked-l1-obstruction-for-quadratic-hessian-pde.md), the [time-spine coarsening theorem](time-spine-coarsening-for-quadratic-hessian-patches.md), and the [residual signed variation characterization](residual-signed-variation-characterization-for-coarsened-patches.md).

## Setup

Fix

$$
0<\alpha<1,
\qquad
T>0,
\qquad
\lambda\in\mathbb R,
$$

and let

$$
g=\phi''\in C^\alpha(\mathbb T),
\qquad
\mathbb T=\mathbb R/(2\pi\mathbb Z).
$$

Only \(g\in C^\alpha\) is used in the construction. No higher derivative of \(g\), no smallness assumption, and no existence theorem for the infinite nonlinear PDE is needed.

Let \(\mathfrak T\) be the finite rooted planar full binary trees. For a leaf \(\bullet\), define

$$
F_\bullet(t,x)=P_tg(x).
\tag{1}
$$

For \(\tau=[\tau_1,\tau_2]\), define the deterministic tree profile recursively by

$$
F_\tau(t,x)
=
\lambda\int_0^t
\partial_x^2P_{t-s}
\left[
F_{\tau_1}(s)F_{\tau_2}(s)
\right](x)
\,ds.
\tag{2}
$$

The theorem below proves simultaneously that every fixed integral in (2) is well defined and that it is the total mass of the corresponding raw signed measure.

Write \(\gamma\) for standard Gaussian measure on \(\mathbb R\), and

$$
He_2(z)=z^2-1.
$$

All additions in the spatial coordinate are understood modulo \(2\pi\).

## Raw mark spaces and positive reference measures

The raw spaces are defined recursively.

For a leaf, let

$$
\Omega_\bullet=\mathbb R,
\qquad
\nu_\bullet=\gamma.
\tag{3}
$$

If \(\tau=[\tau_1,\tau_2]\), set

$$
\Omega_\tau
=
[0,T]\times\mathbb R\times
\Omega_{\tau_1}\times\Omega_{\tau_2},
\tag{4}
$$

with the product Borel sigma-field, and

$$
\nu_\tau
=
(ds)\otimes\gamma(dz)\otimes
\nu_{\tau_1}\otimes\nu_{\tau_2}.
\tag{5}
$$

Every \(\Omega_\tau\) is a finite product of standard Borel spaces and is therefore standard Borel. Every \(\nu_\tau\) is finite; if \(|\tau|\) denotes the number of internal vertices, then

$$
\nu_\tau(\Omega_\tau)=T^{|\tau|}.
\tag{6}
$$

The coordinate \(s\) in (4) is the branch time at the root of \(\tau\), the coordinate \(z\) is its centered Hessian Gaussian mark, and the two remaining coordinates contain all descendant raw marks. The chronological constraints are imposed by the density, rather than by changing the measurable space from one target time to another.

## Recursive raw density

For \(0\le t\le T\), \(x\in\mathbb T\), and \(\xi\in\Omega_\bullet\), define

$$
\mathscr R_\bullet^{t,x}(\xi)
=
g(x+\sqrt t\,\xi).
\tag{7}
$$

Now let \(\tau=[\tau_1,\tau_2]\). For

$$
\omega=(s,z,\omega_1,\omega_2)
\in\Omega_\tau
$$

with \(0<s<t\), put

$$
r=t-s,
\qquad
x_z=x+\sqrt r\,z,
$$

and define

$$
\begin{aligned}
\mathscr R_\tau^{t,x}(\omega)
={}&
\lambda\frac{He_2(z)}{r}
\Bigl[
\mathscr R_{\tau_1}^{s,x_z}(\omega_1)
\mathscr R_{\tau_2}^{s,x_z}(\omega_2)\\
&\hspace{4.4em}
-
\mathscr R_{\tau_1}^{s,x}(\omega_1)
\mathscr R_{\tau_2}^{s,x}(\omega_2)
\Bigr].
\end{aligned}
\tag{8}
$$

Set \(\mathscr R_\tau^{t,x}=0\) when \(s\ge t\), including the diagonal \(s=t\). Equation (8) is exactly the centered one-edge realization

$$
\frac{He_2(z)}r
\bigl[H(x+\sqrt r z)-H(x)\bigr]
$$

applied to the product of two independent descendant raw fields. The shifted and unshifted terms use the **same descendant marks** \((\omega_1,\omega_2)\); this is the canonical centered coupling used throughout the raw-faithful part of the project.

### Joint measurability

For every finite \(\tau\), the map

$$
(t,x,\omega)
\longmapsto
\mathscr R_\tau^{t,x}(\omega)
$$

is jointly Borel measurable on

$$
[0,T]\times\mathbb T\times\Omega_\tau.
\tag{9}
$$

This is immediate by induction. The leaf map is continuous. At an internal vertex, the set \(\{(t,s):0<s<t\}\) is Borel, the maps \(r=t-s\) and \(x+\sqrt r z\) are Borel on that set, and (8) is obtained from the jointly measurable child densities by multiplication and subtraction. Assigning the value zero on \(s\ge t\) removes the apparent singularity from the definition on the diagonal.

Thus \(\Omega_\tau\) is an honest measurable space and \(\mathscr R_\tau^{t,x}\) is an honest measurable function on it. What remains is to prove that this density belongs to \(L^1(\nu_\tau)\).

## An \(L^1\)-valued Holder norm

Let \((E,\mathcal E,m)\) be a finite positive measure space. For a jointly measurable field \(H:\mathbb T\times E\to\mathbb R\) and \(0<\eta<1\), set

$$
\begin{aligned}
\|H\|_{\mathcal H^\eta(m)}
={}&
\sup_{x\in\mathbb T}
\int_E|H(x,e)|\,dm(e)\\
&+
\sup_{x\ne y}
\frac{
\displaystyle
\int_E|H(x,e)-H(y,e)|\,dm(e)
}{d_{\mathbb T}(x,y)^\eta}.
\end{aligned}
\tag{10}
$$

This is the \(C^\eta\) norm of the map \(x\mapsto H(x,\cdot)\) with values in \(L^1(m)\). It does **not** take a pathwise Holder norm before expectation.

For a time-dependent raw field write

$$
\|H\|_{\mathcal H_T^\eta(m)}
=
\sup_{0\le t\le T}
\|H(t,\cdot;\cdot)\|_{\mathcal H^\eta(m)}.
\tag{11}
$$

## One centered edge with a strict regularity loss

Let \(0<\beta<\eta<1\). Given \(H:\mathbb T\times E\to\mathbb R\), define

$$
(\mathcal K_rH)(x,z,e)
=
\frac{He_2(z)}r
\left[
H(x+\sqrt r z,e)-H(x,e)
\right].
\tag{12}
$$

### Lemma

For every \(T>0\) there is a finite constant \(C_{\beta,\eta,T}\) such that, for \(0<r\le T\),

$$
\boxed{
\|\mathcal K_rH\|_{\mathcal H^\beta(\gamma\otimes m)}
\le
C_{\beta,\eta,T}
\,r^{-1+(\eta-\beta)/2}
\|H\|_{\mathcal H^\eta(m)}.
}
\tag{13}
$$

Consequently

$$
\int_0^T
\|\mathcal K_rH\|_{\mathcal H^\beta}
\,dr
\le
C'_{\beta,\eta,T}
\|H\|_{\mathcal H^\eta},
\tag{14}
$$

because \(\eta-\beta>0\).

### Proof

The supremum part follows from the Holder increment in the input:

$$
\begin{aligned}
\sup_x
\int|\mathcal K_rH(x,z,e)|
\,d\gamma(z)dm(e)
&\le
r^{-1}
\mathbb E\left[
|He_2(Z)|
\,d_{\mathbb T}(\sqrt rZ,0)^\eta
\right]
[H]_{\mathcal H^\eta}\\
&\le
c_{2,\eta}
 r^{-1+\eta/2}
[H]_{\mathcal H^\eta}.
\end{aligned}
\tag{15}
$$

For the spatial increment of the output, let \(d=d_{\mathbb T}(x,y)\). There are two bounds. Applying the input Holder estimate to both translated terms gives

$$
\int
|\mathcal K_rH(x)-\mathcal K_rH(y)|
\le
C r^{-1}d^\eta
\|H\|_{\mathcal H^\eta}.
\tag{16}
$$

Using (15) at the two points instead gives

$$
\int
|\mathcal K_rH(x)-\mathcal K_rH(y)|
\le
C r^{-1+\eta/2}
\|H\|_{\mathcal H^\eta}.
\tag{17}
$$

If \(d\le\sqrt r\), divide (16) by \(d^\beta\); if \(d>\sqrt r\), divide (17) by \(d^\beta\). Both cases give the scale

$$
r^{-1+(\eta-\beta)/2}.
$$

Together with (15), after absorbing the harmless large-\(r\) factor into a constant depending on \(T\), this proves (13). Integrating the power of \(r\) proves (14). \(\square\)

The strict loss \(\eta-\beta>0\) is load-bearing. The same-regularity \(L^1\)-valued Holder estimate has the nonintegrable scale \(r^{-1}\).

## Product of independent descendant fields

If \(H_i:\mathbb T\times E_i\to\mathbb R\) and \(m_i\) are finite positive measures, define

$$
H(x,e_1,e_2)
=H_1(x,e_1)H_2(x,e_2).
$$

Then

$$
\boxed{
\|H\|_{\mathcal H^\eta(m_1\otimes m_2)}
\le
\|H_1\|_{\mathcal H^\eta(m_1)}
\|H_2\|_{\mathcal H^\eta(m_2)}.
}
\tag{18}
$$

Indeed, the \(L^1\) norm factorizes, and

$$
H_1(x)H_2(x)-H_1(y)H_2(y)
=
[H_1(x)-H_1(y)]H_2(x)
+H_1(y)[H_2(x)-H_2(y)].
$$

Integrating on the product space gives (18).

## Theorem: every fixed tree has a finite canonical raw measure

### Theorem

Assume only

$$
g=\phi''\in C^\alpha(\mathbb T),
\qquad 0<\alpha<1.
\tag{19}
$$

For every finite planar full binary tree \(\tau\), every \(0<\beta<\alpha\), and every \(T>0\),

$$
\boxed{
\sup_{0\le t\le T}
\left\|
\mathscr R_\tau^{t,\cdot}
\right\|_{\mathcal H^\beta(\nu_\tau)}
<\infty.
}
\tag{20}
$$

In particular, for every fixed target \((t,x)\),

$$
\mathscr R_\tau^{t,x}
\in L^1(\nu_\tau).
\tag{21}
$$

Hence

$$
\boxed{
\mu_\tau^{t,x}(A)
:=
\int_A
\mathscr R_\tau^{t,x}(\omega)
\,d\nu_\tau(\omega),
\qquad A\in\mathcal B(\Omega_\tau),
}
\tag{22}
$$

defines a genuine finite countably additive signed measure on \(\Omega_\tau\).

Moreover,

$$
\boxed{
\mu_\tau^{t,x}(\Omega_\tau)
=
F_\tau(t,x).
}
\tag{23}
$$

No smallness condition on \(g\) or \(\lambda\) is required for this fixed-tree statement.

### Proof

We first prove (20) by induction on the number of internal vertices.

For the leaf, (7) gives

$$
\sup_{t,x}
\int
|\mathscr R_\bullet^{t,x}(\xi)|d\gamma(\xi)
\le
\|g\|_\infty,
$$

and translation invariance gives the \(C^\alpha\) increment bound directly from \([g]_{C^\alpha}\). Thus the leaf belongs uniformly to \(\mathcal H^\beta(\gamma)\) for every \(0<\beta\le\alpha\).

Now let \(\tau=[\tau_1,\tau_2]\), fix \(0<\beta<\alpha\), and choose

$$
\eta
=
\frac{\alpha+\beta}{2},
\qquad
\beta<\eta<\alpha.
\tag{24}
$$

By the induction hypothesis, both child raw fields have finite uniform \(\mathcal H^\eta\) norms. For fixed child time \(s\), their product

$$
H_s^x(\omega_1,\omega_2)
=
\mathscr R_{\tau_1}^{s,x}(\omega_1)
\mathscr R_{\tau_2}^{s,x}(\omega_2)
$$

therefore has finite \(\mathcal H^\eta(\nu_{\tau_1}\otimes\nu_{\tau_2})\) norm by (18), uniformly in \(s\).

Equation (8) is \(\lambda\mathcal K_{t-s}H_s\). Applying (13) and integrating the root branch-time coordinate gives

$$
\begin{aligned}
\sup_{t\le T}
\|\mathscr R_\tau^{t,\cdot}\|_{\mathcal H^\beta(\nu_\tau)}
&\le
|\lambda|C_{\beta,\eta,T}
\int_0^T
r^{-1+(\eta-\beta)/2}\,dr\\
&\qquad\times
\sup_{s\le T}
\|\mathscr R_{\tau_1}^{s,\cdot}\|_{\mathcal H^\eta}
\sup_{s\le T}
\|\mathscr R_{\tau_2}^{s,\cdot}\|_{\mathcal H^\eta}
<\infty.
\end{aligned}
\tag{25}
$$

This proves (20). In particular (21) holds, so (22) is the signed measure with \(L^1\) density \(\mathscr R_\tau^{t,x}\) with respect to the finite positive measure \(\nu_\tau\). Countable additivity is therefore automatic, and

$$
\|\mu_\tau^{t,x}\|_{\mathrm{TV}}
=
\int_{\Omega_\tau}
|\mathscr R_\tau^{t,x}|d\nu_\tau
<\infty.
\tag{26}
$$

It remains to prove the mass identity (23). For a leaf,

$$
\mu_\bullet^{t,x}(\Omega_\bullet)
=
\int g(x+\sqrt t\xi)d\gamma(\xi)
=
P_tg(x)
=
F_\bullet(t,x).
\tag{27}
$$

Assume the identity for the two children. Since the root density is absolutely integrable, Fubini is legitimate. Integrating first over the child spaces in (8) gives

$$
\begin{aligned}
\mu_\tau^{t,x}(\Omega_\tau)
={}&
\lambda\int_0^t\int_\mathbb R
\frac{He_2(z)}{t-s}
\Bigl[
F_{\tau_1}(s,x_z)F_{\tau_2}(s,x_z)\\
&\hspace{7em}
-
F_{\tau_1}(s,x)F_{\tau_2}(s,x)
\Bigr]
\,d\gamma(z)ds.
\end{aligned}
\tag{28}
$$

The mass functions inherit spatial Holder regularity from (20), so the centered Gaussian Hessian identity applies. The inner integral in (28) is

$$
\partial_x^2P_{t-s}
\left[
F_{\tau_1}(s)F_{\tau_2}(s)
\right](x).
$$

Therefore (28) is exactly the deterministic recursion (2), proving (23). \(\square\)

## What regularity is actually used

The proof uses only one positive spatial Holder exponent at the leaves. It never differentiates \(g\). Thus

$$
g=\phi''\in C^\alpha,
\qquad 0<\alpha<1,
$$

is sufficient.

The strict loss at each raw edge is not a hidden strengthening of the data hypothesis. For a fixed finite tree, one can always choose intermediate exponents below the original \(\alpha\). What fails with depth is geometric control of the constants, not finiteness at any one depth.

This also explains the precise reading of the \((cn/\Delta)^n\) theorem. Given a tree of depth \(n\), a finite regularity budget may be divided into \(n\) positive losses, producing a finite \(L^1\) bound. The theorem says that the best constants in a stepwise first-moment argument then grow at least supergeometrically; it does **not** say that a fixed depth has infinite first moment.

By contrast, if no positive spatial regularity is assumed, the centered one-edge estimate no longer supplies an integrable power of the short duration. The present theorem therefore does not claim the same result for arbitrary bounded measurable \(g\).

## Exact criterion after the finite construction

Because every fixed \(\mu_\tau^{t,x}\) is finite, all later finite-measure operations are legitimate:

- a positive proposal \(Q_\tau\) may dominate \(\mu_\tau^{t,x}\), and \(d\mu_\tau^{t,x}/dQ_\tau\) is an ordinary Radon--Nikodym density;
- raw-faithfulness is an ordinary conditional-barycenter condition;
- every measurable coarsening has a genuine pushforward signed measure;
- its residual total variation is finite for that fixed tree;
- the only infinite-depth question is summability over the countable tree family.

For example, if the skeleton label is retained and no coarsening is performed, the canonical raw sampler has first moment

$$
\sum_{\tau\in\mathfrak T}
\|\mu_\tau^{t,x}\|_{\mathrm{TV}},
\tag{29}
$$

whenever the sum is finite, and is non-\(L^1\) when the sum diverges. For a coarsening \(\mathcal C_\tau\), the corresponding quantity is

$$
\sum_{\tau\in\mathfrak T}
\|(\mathcal C_\tau)_\#\mu_\tau^{t,x}\|_{\mathrm{TV}}.
\tag{30}
$$

The [residual signed variation theorem](residual-signed-variation-characterization-for-coarsened-patches.md) identifies (30) exactly with the sum of conditional \(L^1\) norms of the raw densities.

## Bijection with decorated maximal-left-patch skeletons

The tree-indexed construction above is also the patch-indexed construction used later, but the word *decorated* must be precise.

For a non-leaf tree \(\tau\), follow the maximal left-child chain from the root. Suppose it contains \(m\ge1\) internal vertices. Let

$$
\sigma_1,\ldots,\sigma_m
$$

be the successive **right subtrees in chain order**, from the root of the patch to its bottom vertex. The last left child is a leaf. Define recursively

$$
\mathsf D(\bullet)=\bullet,
$$

and

$$
\mathsf D(\tau)
=
\left(
 m;
 \mathsf D(\sigma_1),\ldots,\mathsf D(\sigma_m)
\right).
\tag{31}
$$

A *decorated maximal-left-patch skeleton* means exactly an object generated by this recursion. Thus the decoration records not only the length \(m\) of a contracted patch but also the ordered side-attachment slot \(j\) of every descendant patch.

### Proposition

The map

$$
\mathsf D:
\{\text{finite planar full binary trees}\}
\longrightarrow
\{\text{decorated maximal-left-patch skeletons}\}
$$

is a bijection.

### Proof

Injectivity and surjectivity follow from an explicit inverse. Given

$$
\left(m;D_1,\ldots,D_m\right),
$$

construct a chain of \(m\) internal vertices connected successively through left children. Attach \(\mathsf D^{-1}(D_j)\) as the right subtree at the \(j\)-th vertex, and make the left child of the bottom vertex a leaf. Apply the same construction recursively to every \(D_j\). This produces one finite planar full binary tree, and it is immediate from the construction that the two maps are inverse. \(\square\)

A contracted patch graph decorated **only** by chain lengths would not be enough: it could forget at which vertex of a long patch a side subtree was attached. The ordered side slots in (31) are therefore part of the definition.

Consequently later sections may index a measure either by the original tree \(\tau\) or by its decorated patch skeleton \(\mathsf D(\tau)\). This is a reindexing of the same measurable space, reference measure, and signed measure; no second raw measure is being defined.

## Compatibility with the fixed-datum comb obstruction

For the right-comb tree \(\tau_m\), the measure used in the raw-barycenter obstruction is the restriction of \(\mu_{\tau_m}^{h,x}\) to the stated duration cylinder. The Fourier projection used there is compatible with the common-seed centered coupling in (8).

Indeed, write

$$
p_s^{\mathbb T}(x,y)=q_s(y-x).
$$

If a terminal Brownian increment is \(U=y-x\), the bounded projector

$$
\frac{\kappa_h}{q_s(U)}e^{-ikU}
$$

depends on the increment \(U\) and the remaining time \(s\), but **not** on the starting point \(x\). Hence exactly the same raw-state test is applied to the shifted and unshifted child terms in (8). Integrating the leaf mark gives the pure Fourier mode used in the comb proof, and every subsequent centered edge contributes the factor

$$
\frac{He_2(Z)}r
\left(e^{iK\sqrt rZ}-1\right).
$$

Thus the existing comb total-variation lower bound is a lower bound for the canonical measures constructed here, not for a different raw coupling.
