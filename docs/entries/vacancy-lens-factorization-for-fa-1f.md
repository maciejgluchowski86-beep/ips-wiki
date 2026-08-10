---
title: Vacancy-lens factorization for one-dimensional FA-1f
status: conditional
tags:
  - FA-1f
  - out of equilibrium
  - graphical construction
  - chronology
  - factorization
---

# Vacancy-lens factorization for one-dimensional FA-1f

This entry combines two [tagged-vacancy bridge factorizations](tagged-vacancy-bridge-factorization-for-fa-1f.md) into a two-sided spacetime lens. The fixed-segment identities are exact. The iteration over an arbitrary moving path is a Duhamel/Poisson-disintegration construction; a fully global scaffold theorem is recorded separately rather than claimed here.

The boundary paths are always carried by vacancies. Conditional on their coarse paths and auxiliary bridge times, the complete update chronology inside a fixed lens segment is left unrevealed and appears only through a positive regional transfer operator.

## A globally compatible tie rule

A tagged vacancy that is filled must transfer its tag to a vacant neighbor. If exactly one neighbor is vacant, transfer there. If both neighbors are vacant, use an independent fair coin. This rule is global: the same tagged path can serve as the right boundary of one region and the left boundary of another.

Write

$$
L=\mathbf 1\{x-1\text{ is vacant}\},
\qquad
R=\mathbf 1\{x+1\text{ is vacant}\}.
$$

The left- and right-jump intensities of a tag at \(x\) are

$$
r_-=pL\left(1-\frac12R\right),
\qquad
r_+=pR\left(1-\frac12L\right),
\tag{1}
$$

and

$$
r_-+r_+=p(L\vee R).
\tag{2}
$$

Each jump intensity is a product of a nonnegative left factor and a nonnegative right factor. This is the property needed for regional factorization.

For one isolated lens one may instead use an inward-priority rule. That local choice was used in an earlier draft of this entry, but it is not compatible with a global tessellation because a shared tagged vacancy is simultaneously the left boundary of one lens and the right boundary of another.

## A fixed holding interval

Suppose that during \([a,b)\) two tagged vacancies stay at fixed sites \(\ell<r\). Write

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

The common times \(u_j\) are the left bridge times. Conditional on them, every factor in (3)--(4) splits into an exterior term depending on \(O^-\) and an interior term depending on \(I^-\). The same construction gives a right bridge-time list and splits the right-boundary survival factor into an interior and a right-exterior term.

Consequently, conditional on the two bridge-time lists, the weight of the fixed holding interval is a product

$$
W_{\mathrm L}\,W_{\mathrm{lens}}\,W_{\mathrm R},
\tag{5}
$$

where \(W_{\mathrm{lens}}\) is a nonnegative functional of the complete FA history on \((\ell,r)\) with frozen vacant boundary sites at \(\ell,r\). No clock time or update order in the lens interior has been revealed.

## Boundary jumps

At time \(b\), suppose the left tagged boundary jumps. Formula (1) gives

$$
\begin{aligned}
\text{left jump:}&\qquad p\,O_b^-\left(1-\frac12 I_b^-\right),\\
\text{right jump:}&\qquad p\,I_b^-\left(1-\frac12 O_b^-\right).
\end{aligned}
\tag{6}
$$

Both are products of one exterior and one interior factor. The analogous statement holds for the right tagged boundary. Thus prescribing a terminal jump direction preserves the product form (5).

After the jump, the lens endpoint moves by one lattice site and the same fixed-segment construction restarts. If the two tagged paths meet, the lens terminates.

## What is already exact

For a prescribed pair of noncrossing tagged paths with finitely many jumps, multiply the fixed-segment survival factors and terminal jump factors and expand every overlap factor as in (4). By Tonelli's theorem, each term in the resulting positive series is a product of three regional functionals. This gives the desired left/lens/right factorization for that prescribed finite path skeleton.

What still requires a separate theorem is the construction of a useful random global path/scaffold and the corresponding regular conditional law. In particular, one must not infer independence merely from the fact that the geometric paths are disjoint: the event selecting those paths contains survival information, and the bridge expansion is precisely what removes that coupling.

## Relation with a barrier--scaffold decomposition

The uploaded barrier--scaffold construction reveals a chain of boundary interactions, their predecessors, and certifying absence intervals. The vacancy lens has the same architecture with one new ingredient.

* A vertical tagged-vacancy segment replaces a forced active tube segment.
* A tag jump replaces a revealed boundary interaction.
* The survival requirement for a tagged vacancy replaces a certifying absence interval.
* Because FA facilitation is the OR of two neighboring vacancy signals, that survival requirement couples the two adjacent regions. The bridge expansion (3)--(4) is exactly the extra scaffold data needed to restore regional factorization.

Thus the bridge times are not a heuristic coarse graining. They are the algebraic correction forced by the two-sided constraint.

## Regional transfer operator

For a prescribed lens path \(\Gamma\) and bridge data \(B\), denote the resulting interior operator by

$$
K_{\Gamma,B}.
$$

It is a positive finite-volume FA transfer operator with moving vacant boundaries, additional nonnegative boundary killing factors, bridge-time vacancy insertions, and local boundary factors at jump times. It integrates every internal update chronology.

The next quantitative problem is to identify path/bridge data for which the normalized operators \(K_{\Gamma,B}\) lose dependence on the bottom configuration. The ordinary finite-volume FA semigroup has a uniform spectral gap at fixed \(q\), but the boundary killing and bridge insertions must be handled explicitly rather than discarded.