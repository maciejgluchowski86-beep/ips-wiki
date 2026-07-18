---
title: Patch positivity for FA-1f
status: proved here
tags:
  - KCSM
  - FA-1f
  - duality
  - patch
  - positivity
---

# Patch positivity for FA-1f

This entry applies the [patch positivity property](patch-positivity-property.md) to the [FA-1f model](fa-1f-model.md), whose end-factor threshold is the [FA-1f patch critical density](patch-critical-density-for-fa-1f.md), and to [pure-noise perturbations](pure-noise-spin-system.md).

## FA-1f

The FA-1f model has the patch positivity property.

Indeed, the only nonzero nonempty-neighbour coefficients are

$$
c_i^0(N(i))=-p,
\qquad
c_i^1(N(i))=-q,
$$

and the empty-neighbour coefficients are

$$
c_i^0(\vn)=p,
\qquad
c_i^1(\vn)=q.
$$

The two inequalities in the patch positivity criterion become

$$
c_i^0(N(i))+c_i^1(N(i))=-1\le0,
\qquad
c_i^1(\vn)c_i^0(N(i))-c_i^0(\vn)c_i^1(N(i))=0.
$$

All other nonempty-neighbour coefficients are zero.

## Pure-noise perturbations

For the perturbation \(\mathcal L_{\mathrm{FA}}+\varepsilon\mathcal N^r\) with \(\varepsilon>0\), patch positivity is preserved if and only if

$$
r_i\ge p
$$

at every site with nonempty neighbour set and nontrivial FA-1f constraint. If \(\varepsilon=0\), the statement reduces to the unperturbed FA-1f case and is independent of \(r\).

The perturbation changes only the empty-neighbour coefficients, so

$$
c_i^0(\vn)=p+\varepsilon r_i,
\qquad
c_i^1(\vn)=q+\varepsilon(1-r_i),
$$

while \(c_i^0(N(i))=-p\) and \(c_i^1(N(i))=-q\). The first patch-positivity inequality is unchanged, and the second becomes

$$
\begin{aligned}
c_i^1(\vn)c_i^0(N(i))-c_i^0(\vn)c_i^1(N(i))
&=
\left(q+\varepsilon(1-r_i)\right)(-p)-\left(p+\varepsilon r_i\right)(-q)
\\
&=
\varepsilon(r_i-p).
\end{aligned}
$$

Thus the criterion is exactly \(r_i\ge p\) when \(\varepsilon>0\). Pure births correspond to \(r_i=1\), so they preserve patch positivity. Pure deaths correspond to \(r_i=0\), so they do not preserve it unless the FA-1f occupied density is zero.
