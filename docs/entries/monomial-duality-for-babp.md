---
title: Monomial duality for BABP
status: proved here
tags:
  - duality
  - BABP
  - monomials
  - KCSM
---

# Monomial duality for BABP

This entry specializes [monomial duality for spin systems](monomial-duality-for-spin-systems.md) to the [biased annihilating branching process](babp-model.md). The calculation is organized in two steps: first expand the BABP flip rates in monomials, and then substitute those coefficients into the general dual-rate formulas. Write \(p=1-q\), where \(q\) is the vacancy density.

Only the rates listed below are nonzero. All omitted rates are zero, and signs attached to zero rates are irrelevant.

## Spin-rate coefficients

For a source site \(i\), the flip rate from \(0\) to \(1\) and the flip rate from \(1\) to \(0\) are

$$
\begin{aligned}
c_i^0(\eta)
&=
p\sum_{j\in N(i)}(1-\eta(j)),
&
c_i^1(\eta)
&=
q\sum_{j\in N(i)}(1-\eta(j)).
\end{aligned}
$$

Here \(c_i^0\) and \(c_i^1\) are the full flip-rate functions in the spin-system generator, including the Bernoulli refresh probability. They are not merely the neighbour-count update rate \(c_i\) from the model definition.

The number of vacant neighbours is affine in the neighbouring spins. Therefore the only nonzero monomial coefficients are

$$
\begin{aligned}
c_i^0(\vn)&=p|N(i)|,
&
c_i^1(\vn)&=q|N(i)|,
\\
c_i^0(\{j\})&=-p,
&
c_i^1(\{j\})&=-q,
\qquad j\in N(i).
\end{aligned}
\tag{1}
$$

In particular, every nonempty interaction target in the dual process is a singleton.

## Dual rates and signs

Substituting (1) into the general definitions gives

$$
\begin{aligned}
\delta_i(\vn)&=p|N(i)|,
&
\sigma_i^\delta(\vn)&=+,
\\
\delta_i(\{j\})&=p,
&
\sigma_i^\delta(\{j\})&=-,
\qquad j\in N(i),
\\
\beta_i(\{j\})&=1,
&
\sigma_i^\beta(\{j\})&=+,
\qquad j\in N(i).
\end{aligned}
\tag{2}
$$

As usual, the source-keeping empty update is omitted: \(\beta_i(\vn)=0\). To identify the Feynman--Kac weight, first sum the actual dual clock rates:

$$
\alpha_i
=
p|N(i)|
+
\sum_{j\in N(i)}(p+1)
=
(1+2p)|N(i)|.
$$

The omitted empty-birth coefficient is

$$
a_i^\beta(\vn)
=
-c_i^0(\vn)-c_i^1(\vn)
=
-|N(i)|.
$$

It follows that the site Feynman--Kac weight is

$$
V_i
=
\alpha_i+a_i^\beta(\vn)
=
2p|N(i)|.
\tag{3}
$$

Thus, for a finite active set \(A\),

$$
V(A)
=
2p\sum_{i\in A}|N(i)|.
$$

If \(N(i)=\vn\), all spin-rate coefficients at \(i\), all dual rates at \(i\), and \(V_i\) vanish. The patch formulas obtained from (2)--(3) are recorded under [patch contributions for BABP](patch-contributions-for-babp.md).

## BABP with pure deaths

Add pure deaths at rates \(d_i\ge0\). By the [duality noise lemma](duality-noise-lemma.md), the dual rates and signs in (2) do not change. Only the Feynman--Kac weight changes:

$$
V_i^d=2p|N(i)|-d_i.
$$
