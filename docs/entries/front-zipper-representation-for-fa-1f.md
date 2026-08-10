---
title: Front zipper representation for one-dimensional FA-1f
status: proved here
tags:
  - FA-1f
  - out of equilibrium
  - front
  - chronology
  - Feynman--Kac
---

# Front zipper representation for one-dimensional FA-1f

This entry records an exact moving-boundary representation for one-dimensional [FA-1f](fa-1f-model.md) when the configuration has a rightmost vacancy. It does not prove convergence to equilibrium. Its purpose is to isolate a geometry in which the update chronology behind a vacancy front is averaged as a whole.

Use the convention that \(0\) is vacant and write \(p=1-q\). For a configuration with finitely many vacancies, let

$$
X(\eta)=\max\{x:\eta_x=0\}
$$

and, for the FA process, define the configuration seen from its rightmost vacancy by

$$
\xi_k(t)=\eta_{X_t-k}(t),\qquad k\in\mathbb N_0.
$$

Thus \(\xi_0(t)=0\), while every site strictly to the right of the front is occupied.

## Moving-frame generator

Let \(\mathcal L^0\) be FA-1f on \(\{1,2,\ldots\}\) with a frozen vacancy at \(0\). In particular the site \(1\) refreshes without constraint. Define

$$
(S_+\xi)_0=0,\quad (S_+\xi)_1=0,\quad (S_+\xi)_k=\xi_{k-1}\quad(k\ge2),
$$

and, on the event \(\xi_1=0\),

$$
(S_-\xi)_0=0,\quad (S_-\xi)_k=\xi_{k+1}\quad(k\ge1).
$$

The process seen from the front has generator

$$
\mathcal Gf(\xi)
=
\mathcal L^0f(\xi)
+q\bigl(f(S_+\xi)-f(\xi)\bigr)
+p(1-\xi_1)\bigl(f(S_-\xi)-f(\xi)\bigr).
\tag{1}
$$

Indeed, the occupied site immediately ahead of the front becomes vacant at rate \(q\), which advances the front. The front becomes occupied at rate \(p\) precisely when the site immediately behind it is vacant, which retreats the front. All other transitions are ordinary FA updates behind a frozen vacant boundary.

## Chronology-averaged strips

Put

$$
V(\xi)=p(1-\xi_1),
\qquad
K_t=\exp\bigl(t(\mathcal L^0-V)\bigr).
\tag{2}
$$

Equivalently,

$$
K_tf(\xi)
=
\mathbb E_\xi^0\left[
\exp\left(-p\int_0^t(1-\xi_1(s))\,ds\right)f(\xi(t))
\right].
\tag{3}
$$

The operator \(K_t\) is positivity preserving. More importantly, it already averages every internal clock order during the interval. No deterministic FA update word remains.

Writing

$$
\mathcal G=(\mathcal L^0-V-qI)+qS_++VS_-,
$$

the Duhamel expansion is a sum over nearest-neighbor front paths. A holding interval of length \(s\) contributes the positive strip operator \(e^{-qs}K_s\); a right jump contributes \(qS_+\), and a left jump contributes \(VS_-\). Hence, conditional on the coarse front path, the spacetime between successive front jumps is integrated as a complete Feynman--Kac FA evolution.

## Boundary signal

There is an additional one-dimensional factorization. Under \(\mathcal L^0\), the coordinate \(\xi_1\) is an autonomous Bernoulli-\(q\) refresh chain because the front at \(0\) is permanently vacant. The Feynman--Kac factor in (3) depends only on this autonomous coordinate. Conditional on its path, the sites \(\{2,3,\ldots\}\) evolve as FA-1f with a prescribed time-dependent boundary signal.

Every front advance also resets the boundary coordinate to a vacancy: \((S_+\xi)_1=0\). Thus record advances of the front are separated by nested nearest-neighbor retreat excursions, and each excursion is a chronology-averaged spacetime chamber rather than a selected microscopic word.

Martinelli, Shapira, and Toninelli, [arXiv:2510.20461](https://arxiv.org/abs/2510.20461), prove for every \(q>0\) that a finite FA vacancy cloud has linearly growing radius and span, together with exponentially small probabilities of large retracing excursions. These estimates support using the record-front chambers at all vacancy densities, but do not themselves prove relaxation behind the front.

The remaining problem is to combine this moving-boundary decomposition with a regional loss-of-memory estimate, such as [regional sweep contraction](regional-sweep-contraction-for-fa-1f.md), while controlling the local boundary weight \(V\) and the nested retreat excursions.
