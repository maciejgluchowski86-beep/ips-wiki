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

This entry applies the [patch positivity property](patch-positivity-property.md) to the [FA-1f model](fa-1f-model.md) and its soft perturbation. Write \(p=1-q\), where \(q\) is the vacancy density.

For hard and soft FA-1f, including the hard case \(arepsilon_i=0\), the relevant spin-rate coefficients are

$$
\begin{aligned}
c_i^0(\vn)&=p,
&
 c_i^1(\vn)&=q,
\\
c_i^0(N(i))&=-(1-\varepsilon_i)p,
&
 c_i^1(N(i))&=-(1-\varepsilon_i)q.
\end{aligned}
$$

All other nonempty coefficients are zero. Therefore

$$
\begin{aligned}
c_i^0(N(i))+c_i^1(N(i))&=-(1-\varepsilon_i)\le0,
\\
c_i^1(\vn)c_i^0(N(i))-c_i^0(\vn)c_i^1(N(i))&=0.
\end{aligned}
$$

Thus hard FA-1f and soft FA-1f satisfy patch positivity.

Adding physical pure deaths at rate \(d_i\) changes the empty occupied-neighbour coefficient to \(c_i^1(\vn)=q+d_i\), while the nonempty coefficients are unchanged. The second patch-positivity inequality becomes

$$
(q+d_i)(-(1-\varepsilon_i)p)-p (-(1-\varepsilon_i)q)
=-(1-\varepsilon_i)p d_i.
$$

Consequently, pure-death perturbations preserve patch positivity only in the degenerate cases \(d_i=0\), \(p=0\), or \(arepsilon_i=1\). In the usual nontrivial regime \(p>0\), \(d_i>0\), and \(arepsilon_i<1\), pure deaths destroy the patch positivity property.
