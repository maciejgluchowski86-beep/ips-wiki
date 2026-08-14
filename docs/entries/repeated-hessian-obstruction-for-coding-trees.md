---
title: Repeated-Hessian obstruction for coding trees
status: proved here
tags:
  - PDE
  - coding tree
  - Feynman-Kac formula
  - integrability
  - branching process
---

# Repeated-Hessian obstruction for coding trees

The [Nguwi--Penent--Privault coding tree](npp-coding-tree.md) contains a three-child Hessian branch that can be repeated along one distinguished lineage. Restricting to genealogies made only from these branches gives a lower bound on the absolute expectation of the tree functional. The lifetime, offspring-selection, and survival probabilities cancel their reciprocal factors exactly, so repeated branching costs only an ordered-simplex factor. As a result, sufficiently fast growth of even jet derivatives at the terminal condition forces failure of \(L^1\) integrability.

**References.** The code set, mechanism, and multiplicative functional are those of Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882, Definitions 2.1, 2.2, and 4.1. The obstruction theorem below is proved here.

Fix the [heat-reference terminal PDE](heat-reference-fully-nonlinear-pde.md), a direction \(j\in\{0,\ldots,n\}\), and assume

$$
\phi^{(j+1)}\not\equiv0.
$$

Let \(g^*\) be a composite code, so

$$
g
=
a\,\partial_{z_0}^{\lambda_0}\cdots\partial_{z_n}^{\lambda_n}f
$$

for some \(a\ne0\) and nonnegative integers \(\lambda_0,\ldots,\lambda_n\). For a bounded measurable set \(B\subseteq\mathbb R\), define

$$
D_m(B;g,j)
=
\int_B
\left|
\partial_{z_j}^{2m}g(J_n\phi(y))
\right|\,dy.
\tag{1}
$$

## Theorem

If, for some bounded measurable \(B\),

$$
\limsup_{m\to\infty}
\left(
\frac{D_m(B;g,j)}{m!}
\right)^{1/m}
=
\infty,
\tag{2}
$$

then for every \(t<T\) and every \(x\in\mathbb R\),

$$
\mathbb E\left[
\left|H(\mathcal T_{t,x,g^*})\right|
\right]
=
\infty.
\tag{3}
$$

## Proof

Fix \(t<T\) and \(x\), and write \(h=T-t\). Define recursively

$$
g_0=g,
\qquad
 g_r
=
\left(-\frac12\right)^r
\partial_{z_j}^{2r}g,
\qquad r\geq1.
\tag{4}
$$

Each \(g_r^*\) is again an allowed composite code: the code class permits arbitrary jet derivatives of \(f\) together with arbitrary nonzero real scalar coefficients. Definition 2.2 contains, for every composite code \(g_{r-1}^*\), the Hessian tuple

$$
Z_r
:=
\left(
 g_r^*,
 \partial_x^{j+1},
 \partial_x^{j+1}
\right)
=
\left(
-\frac12(\partial_{z_j}^2g_{r-1})^*,
\partial_x^{j+1},
\partial_x^{j+1}
\right).
\tag{5}
$$

Thus this branch can be repeated indefinitely along the first child.

For \(m\geq1\), let \(E_m\) be the event on which the distinguished composite lineage has exactly \(m\) branchings before time \(t+h/2\), every branching uses the tuple (5), every one of the \(2m\) side children survives to \(T\), and the distinguished composite child created at the \(m\)-th branching also survives to \(T\). Writing the distinguished branching times as \(s_1<\cdots<s_m\), their allowed region is

$$
\Delta_m
=
\left\{
(t<s_1<\cdots<s_m<t+h/2)
\right\},
$$

with volume

$$
|\Delta_m|
=
\frac{(h/2)^m}{m!}.
\tag{6}
$$

The events \(E_m\) are pairwise disjoint because the distinguished lineage has exactly \(m\) internal vertices on \(E_m\).

Consider the expectation restricted to one such genealogy. At the \(r\)-th distinguished branching, the lifetime density contributes

$$
\rho(s_r-s_{r-1})\,ds_r,
\qquad s_0=t,
$$

and selecting the prescribed tuple contributes

$$
q_r
:=
q_{g_{r-1}^*}(Z_r)
>0.
$$

These factors cancel the corresponding reciprocal factor

$$
\frac{1}{q_r\rho(s_r-s_{r-1})}
$$

in the [multiplicative functional](npp-coding-tree.md). A side child born at time \(s_r\) survives with probability \(\overline F(T-s_r)\), which cancels its terminal denominator \(1/\overline F(T-s_r)\). The same cancellation holds for the final distinguished child. Hence the restriction leaves ordinary Lebesgue measure on \(\Delta_m\), together with the Brownian terminal factors. The terminal composite code is \(g_m^*\), so its absolute terminal value contributes

$$
2^{-m}
\left|
\partial_{z_j}^{2m}g(J_n\phi(Y))
\right|.
\tag{7}
$$

It remains to bound the Brownian transfers uniformly in \(m\). Choose \(R>0\) and put \(K=[x-R,x+R]\). Conditional on the branching times, the Brownian pieces along the distinguished lineage concatenate to a standard Brownian path up to \(s_m\). Therefore

$$
\alpha
=
\mathbb P\left(
\sup_{0\leq r\leq h/2}|B_r|\leq R
\right)
>0
\tag{8}
$$

is a lower bound, independent of \(m\) and of the points of \(\Delta_m\), for the event that every distinguished branching position lies in \(K\).

Write \(\psi=\phi^{(j+1)}\). Since \(\psi\) is continuous and not identically zero, strict positivity of the heat kernel gives

$$
\beta
=
\inf_{\substack{z\in K\\ r\in[h/2,h]}}
P_r|\psi|(z)
>0.
\tag{9}
$$

For the bounded set \(B\), the Gaussian heat kernel \(p_r\) also satisfies

$$
\kappa_B
=
\inf_{\substack{z\in K,\ y\in B\\ r\in[h/2,h]}}
p_r(y-z)
>0.
\tag{10}
$$

Conditioning first on the distinguished branching times and positions preserves independence of the side-child Brownian motions. On the confinement event from (8), each side child contributes at least \(\beta\) after taking absolute terminal expectation, while the final distinguished child contributes at least

$$
2^{-m}\kappa_B D_m(B;g,j).
$$

Combining (6)--(10) yields

$$
\mathbb E\left[
|H(\mathcal T_{t,x,g^*})|\ind(E_m)
\right]
\geq
\alpha\kappa_B
\left(\frac{h\beta^2}{4}\right)^m
\frac{D_m(B;g,j)}{m!}.
\tag{11}
$$

The strictly positive lifetime density and the positive offspring probabilities in the Nguwi--Penent--Privault construction ensure that these restricted finite genealogies are legitimate events; no lower bound on those sampling probabilities is needed because they have already cancelled in (11).

Finally, nonnegativity and disjointness give

$$
\mathbb E\left[
|H(\mathcal T_{t,x,g^*})|
\right]
\geq
\sum_{m\geq1}
\mathbb E\left[
|H(\mathcal T_{t,x,g^*})|\ind(E_m)
\right].
$$

Under (2), the right-hand side of (11) fails even to tend to zero along a subsequence, since \(h\beta^2/4>0\) is fixed. The series therefore diverges, proving (3).
