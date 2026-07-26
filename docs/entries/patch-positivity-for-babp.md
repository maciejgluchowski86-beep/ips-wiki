---
title: Patch positivity for BABP
status: proved here
tags:
  - KCSM
  - BABP
  - duality
  - patch
  - positivity
---

# Patch positivity for BABP

This entry verifies the [patch positivity property](patch-positivity-property.md) for the [biased annihilating branching process](babp-model.md) and determines which [pure-noise perturbations](pure-noise-spin-system.md) preserve it.

## BABP

The BABP has the patch positivity property.

To check the coefficient criterion, it is enough to consider singleton targets because the only nonzero nonempty-neighbour coefficients are

$$
c_i^0(\{j\})=-p,
\qquad
c_i^1(\{j\})=-q,
\qquad
j\in N(i).
$$

The empty-neighbour coefficients are

$$
c_i^0(\vn)=p|N(i)|,
\qquad
c_i^1(\vn)=q|N(i)|.
$$

For every \(j\in N(i)\), the first inequality in the patch positivity criterion is

$$
c_i^0(\{j\})+c_i^1(\{j\})=-1\le0.
$$

The second inequality is saturated:

$$
\begin{aligned}
c_i^1(\vn)c_i^0(\{j\})
-c_i^0(\vn)c_i^1(\{j\})
&=
q|N(i)|(-p)-p|N(i)|(-q)
\\
&=
0.
\end{aligned}
$$

Thus both required inequalities hold for every possible nonempty target.

## Pure-noise perturbations

Let

$$
\mathbf p^+=(p_i^+)_{i\in\Lambda}
$$

be the one-density profile of the added noise. For \(\varepsilon>0\), the perturbation

$$
\cL_{\mathrm{BABP}}
+
\varepsilon\mathcal N^{\mathbf p^+}
$$

has patch positivity if and only if

$$
p_i^+\ge p
$$

at every site with \(N(i)\ne\vn\).

The reason is that the perturbation changes only the empty-neighbour coefficients:

$$
\begin{aligned}
c_i^0(\vn)&=p|N(i)|+\varepsilon p_i^+,
&
c_i^1(\vn)&=q|N(i)|+\varepsilon(1-p_i^+),
\end{aligned}
$$

while the singleton coefficients remain \(-p\) and \(-q\). Hence the first patch-positivity inequality is unchanged, and the determinant in the second becomes

$$
\begin{aligned}
c_i^1(\vn)c_i^0(\{j\})
-c_i^0(\vn)c_i^1(\{j\})
&=
\left(q|N(i)|+\varepsilon(1-p_i^+)\right)(-p)
\\
&\qquad-
\left(p|N(i)|+\varepsilon p_i^+\right)(-q)
\\
&=
\varepsilon(p_i^+-p).
\end{aligned}
$$

This proves the stated criterion. If \(\varepsilon=0\), the noise profile is irrelevant. Pure births have \(p_i^+=1\) and preserve patch positivity, while pure deaths have \(p_i^+=0\) and do not preserve it unless \(p=0\).
