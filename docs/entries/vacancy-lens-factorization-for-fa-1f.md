---
title: Vacancy-lens factorization for one-dimensional FA-1f
status: proved here
tags:
  - FA-1f
  - out of equilibrium
  - graphical construction
  - chronology
  - factorization
---

# Vacancy-lens factorization for one-dimensional FA-1f

This entry combines two [tagged-vacancy bridge factorizations](tagged-vacancy-bridge-factorization-for-fa-1f.md) into a two-sided spacetime lens. The boundary paths are always carried by vacancies. Conditional on their coarse paths and auxiliary bridge times, the complete update chronology inside the lens is left unrevealed and appears only through a positive regional transfer operator.

The statement is local in spacetime. It does not assert that a useful family of lenses occurs with sufficient density to prove convergence.

## Inward-priority tagged boundaries

Use vacancy indicators. Let a left tagged vacancy be at \(\ell\), and call \(L\) and \(R\) the vacancy indicators immediately outside and inside the prospective lens, respectively. When the tagged vacancy is filled, choose the new tag by the rule

* if the inside neighbor is vacant, transfer the tag inward;
* otherwise transfer it outward, which is then necessarily vacant.

The two jump rates are therefore

$$
r_{\mathrm{in}}=pR,
\qquad
r_{\mathrm{out}}=pL(1-R),
\tag{1}
$$

and

$$
r_{\mathrm{in}}+r_{\mathrm{out}}=p(L\vee R).
$$

Both rates factor into a nonnegative exterior factor and a nonnegative interior factor. For a right tagged boundary the reflected rule gives

$$
r_{\mathrm{in}}=pL,
\qquad
r_{\mathrm{out}}=pR(1-L).
\tag{2}
$$

The priority rule is auxiliary and does not alter the FA configuration.

## A fixed holding interval

Suppose that during \([a,b)\) the two tagged vacancies stay at fixed sites \(\ell<r\). Write

$$
I_s^- = \mathbf 1\{\ell+1\text{ is vacant at }s\},
\qquad
O_s^- = \mathbf 1\{\ell-1\text{ is vacant at }s\},
$$

for the inside and outside signals of the left boundary, and

$$
I_s^+ = \mathbf 1\{r-1\text{ is vacant at }s\},
\qquad
O_s^+ = \mathbf 1\{r+1\text{ is vacant at }s\}
$$

for the right boundary.

With the two boundary sites frozen vacant, the graphical randomness in the three spatial regions

$$
(-\infty,\ell),
\qquad
(\ell,r),
\qquad
(r,\infty)
$$

is independent before imposing the requirement that the tagged boundary vacancies survive.

For the left boundary, the survival factor is

$$
\exp\left[-p\int_a^b(O_s^-\vee I_s^-)\,ds\right]
=
\exp\left[-p\int_a^bO_s^-ds\right]
\exp\left[-p\int_a^bI_s^-ds\right]
\exp\left[p\int_a^bO_s^-I_s^-ds\right].
\tag{3}
$$

Expand the last factor as

$$
\sum_{m\ge0}p^m
\int_{a<u_1<\cdots<u_m<b}
\prod_{j=1}^mO_{u_j}^-I_{u_j}^-\,d\boldsymbol u.
\tag{4}
$$

The common times \(u_j\) are the left bridge times. Conditional on them, every factor in (3)--(4) splits into an exterior term depending on \(O^-\) and an interior term depending on \(I^-\). The same construction gives an independent list of right bridge times and splits the right-boundary survival factor into an interior and a right-exterior term.

Consequently, conditional on the two bridge-time lists, the weight of the fixed holding interval is a product

$$
W_{\mathrm L}\,W_{\mathrm{lens}}\,W_{\mathrm R},
\tag{5}
$$

where \(W_{\mathrm{lens}}\) is a nonnegative functional of the complete FA history on \((\ell,r)\) with frozen vacant boundary sites at \(\ell,r\). No clock time or update order in the lens interior has been revealed.

## Boundary jumps

At time \(b\), suppose one tagged boundary jumps. Formula (1) or (2) supplies the terminal factor. For example, for the left boundary,

* an inward jump contributes \(pI_b^-\), an interior factor;
* an outward jump contributes \(pO_b^-(1-I_b^-)\), the product of an exterior and an interior factor.

Thus a prescribed terminal jump direction preserves the product structure (5). After the jump, the lens endpoint moves by one lattice site and the same construction restarts.

Iterating over the union of the two boundary jump times gives the following factorization.

## Lens factorization

Fix two noncrossing nearest-neighbor tagged-vacancy paths up to their first meeting time. Augment every vertical path segment by its bridge-time list, and record every boundary jump direction. Then the joint weight of the graphical histories compatible with these data factorizes over the three complementary spacetime regions. In particular, the central factor is a positive transfer operator obtained by integrating the full FA chronology in the moving lens.

Equivalently, for nonnegative functionals \(F_{\mathrm L}\), \(F_{\mathrm{lens}}\), and \(F_{\mathrm R}\), the contribution of a fixed pair of boundary paths can be written as an integral over bridge times of

$$
\mathbb E_{\mathrm L}[F_{\mathrm L}W_{\mathrm L}]
\,
\mathbb E_{\mathrm{lens}}[F_{\mathrm{lens}}W_{\mathrm{lens}}]
\,
\mathbb E_{\mathrm R}[F_{\mathrm R}W_{\mathrm R}],
\tag{6}
$$

with nonnegative weights. Formula (6) is the two-sided analogue of a barrier factorization: the boundary-selection event has been converted into regional factors without conditioning on the order of the interior updates.

## Relation with a barrier--scaffold decomposition

The uploaded barrier--scaffold construction reveals a chain of boundary interactions, their predecessors, and certifying absence intervals. The vacancy lens has the same architecture with one new ingredient.

* A vertical tagged-vacancy segment replaces a forced active tube segment.
* A tag jump replaces a revealed boundary interaction.
* The survival requirement for a tagged vacancy replaces a certifying absence interval.
* Because FA facilitation is the OR of two neighboring vacancy signals, that survival requirement couples the two adjacent regions. The bridge expansion (3)--(4) is exactly the extra scaffold data needed to restore regional factorization.

Thus the bridge times are not a heuristic coarse graining. They are the algebraic correction forced by the two-sided constraint.

## Regional transfer operator

For a lens path \(\Gamma\) and bridge data \(B\), denote the resulting interior operator by

$$
K_{\Gamma,B}.
$$

It is a positive finite-volume FA transfer operator with moving vacant boundaries, additional nonnegative boundary killing factors, vacancy insertions at bridge times, and local boundary factors at jump times. It integrates every internal update chronology.

The next quantitative problem is to find a coarse class of path/bridge data for which the normalized operators \(K_{\Gamma,B}\) contract the dependence on the bottom configuration. The [regional sweep contraction](regional-sweep-contraction-for-fa-1f.md) handles static zero-boundary pieces; the remaining work is to concatenate those estimates through the local boundary jumps and bridge insertions.
