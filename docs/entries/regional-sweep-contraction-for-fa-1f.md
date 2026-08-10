---
title: Regional sweep contraction for one-dimensional FA-1f
status: proved here
tags:
  - FA-1f
  - relaxation
  - chronology
  - projections
  - coarse graining
---

# Regional sweep contraction for one-dimensional FA-1f

This entry records an order-robust contraction estimate for a finite FA-1f region with a facilitating boundary. It is intended for use inside the [discrepancy zipper route](discrepancy-zipper-route-for-fa-1f.md), where the geometry leaves regional update chronology unrevealed.

## One-site heat-bath updates are projections

Let \(I\subset\mathbb Z\) be a finite interval and impose boundary conditions making the FA-1f chain on \(I\) irreducible, for example one fixed vacant boundary site. Write \(\pi_I\) for the Bernoulli equilibrium law on \(I\).

For \(x\in I\), let \(E_x\) be Bernoulli-\(q\) resampling at \(x\), viewed as the conditional-expectation operator in \(L^2(\pi_I)\), and let \(c_x\in\{0,1\}\) be the FA-1f constraint. The one-ring heat-bath operator is

$$
T_x=(1-c_x)I+c_xE_x.
\tag{1}
$$

The constraint does not depend on the state at \(x\), hence multiplication by \(c_x\) commutes with \(E_x\). Since \(E_x\) is an orthogonal projection,

$$
T_x^*=T_x,
\qquad
T_x^2=T_x.
\tag{2}
$$

Thus \(T_x\) is an orthogonal projection. Put

$$
Q_x=I-T_x.
$$

Then \(Q_x\) is also an orthogonal projection and the finite-volume FA generator satisfies

$$
-\mathcal L_I=\sum_{x\in I}Q_x.
\tag{3}
$$

Moreover, \(Q_x\) and \(Q_y\) commute whenever \(|x-y|\ge2\). Hence each local projector fails to commute with at most two other site projectors.

## One complete sweep

Let

$$
\gamma_I=\operatorname{gap}(-\mathcal L_I)>0.
$$

For any permutation \(x_1,\dots,x_{|I|}\) of the sites of \(I\) and every \(f\in L^2(\pi_I)\) with \(\pi_I(f)=0\),

$$
\left\|
T_{x_{|I|}}\cdots T_{x_1}f
\right\|_{2}^{2}
\le
\frac{1}{1+\gamma_I/4}
\|f\|_2^2.
\tag{4}
$$

To see this, apply the arbitrary-order detectability lemma of Anshu, Arad, and Vidick, [arXiv:1602.01210](https://arxiv.org/abs/1602.01210), to the projectors \(Q_x\). Their Hamiltonian is exactly (3), their common ground space is the constants, and the noncommutation degree is at most \(g=2\). The detectability bound gives

$$
\left\|
\prod_{x\in I}(I-Q_x)f
\right\|_2^2
\le
\frac{1}{1+\gamma_I/g^2}\|f\|_2^2,
$$

which is (4).

For one-dimensional FA-1f with a facilitating boundary and fixed \(q>0\), the finite-volume spectral gap is bounded below uniformly in the interval length. Consequently the factor in (4) can be replaced by a number \(\kappa(q)<1\) independent of \(|I|\).

## Fixed counts with repeated updates

The estimate extends directly to the fixed-count chronology used in shuffle calculations. Let a word \(w\) contain \(n_x\ge1\) occurrences of each site \(x\in I\), and put

$$
M=\max_{x\in I}n_x.
$$

Then, for every ordering of this multiset and every mean-zero \(f\),

$$
\|T_wf\|_2^2
\le
\frac{1}{1+\gamma_I/(4M^2)}
\|f\|_2^2.
\tag{5}
$$

Indeed, label the \(n_x\) copies of \(Q_x\) separately and apply the same detectability lemma to

$$
H_w=\sum_{x\in I}n_xQ_x.
$$

Since every \(n_x\ge1\),

$$
H_w\ge -\mathcal L_I
$$

as quadratic forms, so the gap of \(H_w\) above the constants is at least \(\gamma_I\). A copy of \(Q_x\) can fail to commute only with the copies at \(x-1\) and \(x+1\), at most \(2M\) projectors. Formula (5) follows.

In particular, if \(K_{\boldsymbol n}\) is the operator obtained by averaging uniformly over all update words with the fixed count vector \(\boldsymbol n\), then

$$
\|K_{\boldsymbol n}f\|_2
\le
\frac{1}{\sqrt{1+\gamma_I/(4M^2)}}\|f\|_2.
\tag{6}
$$

Thus regional averaging over update order is automatically contractive once every site of the region has been updated and the maximal count is controlled. No sign statement for individual words is required.

## Poisson chronology

For a continuous-time slab, conditional on the site-ring counts \((n_x)_{x\in I}\), all interleavings of those rings are uniform. Therefore (6) applies directly on the event

$$
1\le n_x\le M
\qquad\text{for every }x\in I.
\tag{7}
$$

The complement of (7) is controlled by elementary Poisson tails. For a fixed spatial region, choosing the slab length and \(M\) appropriately gives a strict contraction for the full chronology-averaged regional kernel.

The significance for the zipper construction is that the hard global issue is geometric rather than chronological: once a spacetime component has been isolated with a facilitating boundary and its internal clocks have been left unrevealed, the regional update order no longer needs a separate positivity lemma. The complete regional chronology can be integrated as one contracting kernel.
