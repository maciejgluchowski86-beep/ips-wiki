---
title: Exponential relaxation under confined late interactions
status: proved here
tags:
  - patch
  - ergodicity
  - spin systems
  - convergence to equilibrium
---

# Exponential relaxation under confined late interactions

The representation obtained by [undoing duality under confined late interactions](undoing-duality-under-confined-late-interactions.md) turns the confined patch term into the semigroup of a modified spin system. Uniform mixing of its zero-boundary component therefore gives exponential convergence of that term.

## Assumptions

For \(R\Subset\Lambda\), let \(\cL_R^0\) be the zero-boundary restriction of the original spin system to \(R\):

$$
\cL_R^0 f(\eta)
=
\sum_{i\in R}
c_i(\eta 0_{R^c})
\left(
f(\eta^i)-f(\eta)
ight),
\qquad
\eta\in\{0,1\}^R.
$$

Assume that there are \(C_1<\infty\) and \(\gamma_1>0\), independent of \(R\), such that \(\cL_R^0\) has a unique invariant measure \(
u_R\) and

$$
\sup_{\eta\in\{0,1\}^R}
\left\|
\delta_\eta P_s^{R,0}-
u_R
ight\|_{\mathrm{TV}}
\le
C_1e^{-\gamma_1s}.
	ag{1}
$$

Set

$$
\gamma_2
=
\inf_{i\in\Lambda}
\inf_{x\in\{0,1\}}
c_i^x(\mathbf0),
\qquad
\gamma
=
\min(\gamma_1,\gamma_2),
$$

and assume \(\gamma_2>0\). For \(i
otin R\), put

$$
q_i
=
rac{c_i^0(\mathbf0)}
{c_i^0(\mathbf0)+c_i^1(\mathbf0)}.
$$

The modified generator \(\cL_R\) has the unique invariant measure

$$
\mu_R
=

u_R
\otimes
igotimes_{i
otin R}\operatorname{Ber}(q_i).
	ag{2}
$$

## Lemma

For every \(A\Subset\Lambda\), \(T<\infty\), and \(R\Subset\Lambda\), there is \(C_{A,T}<\infty\) such that, for every \(t\ge T\),

$$
\sup_{\xi\in\{0,1\}^\Lambda}
\left|
\mathbb E_A
\left[
W_t^\xi\ind(L_{T,t}^R)
ight]
-
\mu_R\left(P_T(\chi_A)ight)
ight|
\le
C_{A,T}e^{-\gamma(t-T)}.
	ag{3}
$$

In particular, the limit is the same for every initial configuration \(\xi\).

## Proof

Set \(s=t-T\) and \(g=P_T(\chi_A)\). The confined-interaction representation gives

$$
\mathbb E_A
\left[
W_t^\xi\ind(L_{T,t}^R)
ight]
=
P_s^R g(\xi).
	ag{4}
$$

The generator \(\cL_R\) is the product of the zero-boundary process on \(R\) and independent two-state chains on \(R^c\). By (1), the process on \(R\) can be coupled to equilibrium so that the two copies disagree somewhere in \(R\) with probability at most \(C_1e^{-\gamma_1s}\). For \(i
otin R\), the two-state chain at \(i\) has relaxation rate

$$
c_i^0(\mathbf0)+c_i^1(\mathbf0)\ge\gamma_2,
$$

so its two coupled copies disagree at time \(s\) with probability at most \(e^{-\gamma_2s}\).

Run the original graphical construction for time \(T\) from the two configurations obtained at time \(s\). The value of \(\chi_A\) at the end depends only on the spins in the finite backward influence set of \(A\) over this interval. Its expected size is finite under the standing finite-range bounded-rate assumptions. A union bound over this influence set therefore gives

$$
\sup_\xi
\left|
P_s^R g(\xi)-\mu_R(g)
ight|
\le
\left(
C_1+C_{A,T}'
ight)e^{-\gamma s}
$$

for some \(C_{A,T}'<\infty\). Together with (4), this proves (3).
