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

This entry applies the [patch positivity property](patch-positivity-property.md) to the [FA-1f model](fa-1f-model.md) and to [pure-noise perturbations](pure-noise-spin-system.md). Write \(p=1-q\), where \(q\) is the FA-1f vacancy density.

## FA-1f

Hard FA-1f has the patch positivity property. More generally, the standard soft FA-1f with constraint \(1-(1-\varepsilon_i)\chi_{N(i)}\) has patch positivity for every \(\varepsilon_i\in[0,1]\).

Indeed, the only nonzero nonempty-neighbour coefficients are

$$
 c_i^0(N(i))=-(1-\varepsilon_i)p,
\qquad
 c_i^1(N(i))=-(1-\varepsilon_i)q,
$$

while

$$
 c_i^0(\vn)=p,
\qquad
 c_i^1(\vn)=q.
$$

The two patch-positivity inequalities are therefore

$$
\begin{aligned}
 c_i^0(N(i))+c_i^1(N(i))&=-(1-\varepsilon_i)\le0,
\\
 c_i^1(\vn)c_i^0(N(i))-c_i^0(\vn)c_i^1(N(i))&=0.
\end{aligned}
$$

All other nonempty-neighbour coefficients are zero, so the criterion holds at every source site.

## Pure-noise perturbations

Add pure noise at site \(i\) with rate \(\lambda_i\ge0\) and occupied-site density \(p_i^{\mathrm{noise}}\). Equivalently, its vacancy density is \(q_i^{\mathrm{noise}}=1-p_i^{\mathrm{noise}}\). This changes only the empty-neighbour coefficients:

$$
 c_i^0(\vn)=p+\lambda_i p_i^{\mathrm{noise}},
\qquad
 c_i^1(\vn)=q+\lambda_i q_i^{\mathrm{noise}}.
$$

The first patch-positivity inequality is unchanged. The second becomes

$$
\begin{aligned}
&\left(q+\lambda_i q_i^{\mathrm{noise}}\right)\left(-(1-\varepsilon_i)p\right)
-
\left(p+\lambda_i p_i^{\mathrm{noise}}\right)\left(-(1-\varepsilon_i)q\right)
\\
&\qquad
=\lambda_i(1-\varepsilon_i)\left(qp_i^{\mathrm{noise}}-p q_i^{\mathrm{noise}}\right)
=\lambda_i(1-\varepsilon_i)\left(p_i^{\mathrm{noise}}-p\right).
\end{aligned}
$$

Thus a pure-noise perturbation preserves patch positivity exactly when

$$
 p_i^{\mathrm{noise}}\ge p,
$$

apart from the automatic cases \(\lambda_i=0\) or \(\varepsilon_i=1\). Equivalently, the noise vacancy density satisfies \(q_i^{\mathrm{noise}}\le q\). Pure births correspond to \(p_i^{\mathrm{noise}}=1\), so they preserve patch positivity; pure deaths correspond to \(p_i^{\mathrm{noise}}=0\), so they do not preserve it in the nontrivial regime \(p>0\).