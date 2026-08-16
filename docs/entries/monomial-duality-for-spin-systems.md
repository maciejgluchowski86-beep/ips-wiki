---
title: Monomial Feynman-Kac duality for spin systems
status: proved here
audit: current
tags:
  - duality
  - spin systems
  - monomials
  - Feynman-Kac
---

# Monomial Feynman-Kac duality for spin systems

This entry records the signed monomial dual used in the canonical paper *Patch representations and convergence for facilitated spin systems*, including the generator calculation and the finite-volume passage to the infinite-volume Feynman-Kac formula.

Let

$$
\mathcal L f(\eta)
=
\sum_{i\in\Lambda}c_i(\eta)\bigl(f(\eta^i)-f(\eta)\bigr)
$$

be a uniformly bounded finite-range [spin system](spin-system.md). Write

$$
c_i(\eta)
=
(1-\eta(i))c_i^0(\eta)+\eta(i)c_i^1(\eta),
$$

where $c_i^x$ depends only on the finite neighbour set $N(i)$, and expand

$$
c_i^x(\eta)
=
\sum_{S\subseteq N(i)}c_i^x(S)\chi_S(\eta),
\qquad x\in\{0,1\}.
$$

For the [monomials](monomials.md)

$$
\chi_A(\eta)=\prod_{i\in A}\eta(i),
\qquad A\Subset\Lambda,
$$

set

$$
a_i^\delta(S)=c_i^0(S),
\qquad
a_i^\beta(S)=-c_i^0(S)-c_i^1(S).
$$

Define the dual rates and signs by

$$
\delta_i(S)=|a_i^\delta(S)|,
\qquad
\sigma_i^\delta(S)=\operatorname{sgn}_\pm(a_i^\delta(S)),
$$

and, for $S\ne\varnothing$,

$$
\beta_i(S)=|a_i^\beta(S)|,
\qquad
\sigma_i^\beta(S)=\operatorname{sgn}_\pm(a_i^\beta(S)),
$$

with $\beta_i(\varnothing)=0$. The associated [signed additive set process](signed-additive-set-process.md) has generator $\mathcal D$.

The empty-target coefficient $a_i^\beta(\varnothing)$ is diagonal and is placed in the Feynman-Kac potential. Put

$$
V(A)=\sum_{i\in A}V_i,
$$

where

$$
V_i
=
\sum_{S\subseteq N(i)}\delta_i(S)
+
\sum_{\substack{S\subseteq N(i)\\S\ne\varnothing}}\beta_i(S)
+a_i^\beta(\varnothing).
$$

The theorem uses the same Feynman-Kac integrability assumption as the paper:

$$
\mathbb E_A\left[
\exp\left(\int_0^tV(A_s)\,ds\right)
\right]
<\infty
\qquad
(A\Subset\Lambda,\ t\ge0).
\tag{FK}
$$

Uniform boundedness and finite range give nonexplosion of the signed dual from finite initial sets, but they do not replace (FK); (FK) is the domination hypothesis used in the infinite-volume Feynman-Kac passage.

## Theorem

For a signed active set $Y=(A,\sigma)$ define

$$
H(Y,\eta)=\sigma\chi_A(\eta).
$$

Then

$$
\mathcal L_\eta H(Y,\eta)
=
\mathcal D_YH(Y,\eta)+V(A)H(Y,\eta).
\tag{1}
$$

Consequently, if the signed dual starts from $(A,+)$, then for every $A\Subset\Lambda$, $t\ge0$, and $\eta\in\{0,1\}^\Lambda$,

$$
P_t\chi_A(\eta)
=
\mathbb E_A\left[
\sigma_t
\exp\left(\int_0^tV(A_s)\,ds\right)
\chi_{A_t}(\eta)
\right].
\tag{2}
$$

## Proof of the generator identity

Fix $A\Subset\Lambda$. If $i\notin A$, flipping $i$ leaves $\chi_A$ unchanged. If $i\in A$, then

$$
\begin{aligned}
c_i(\eta)\bigl(\chi_A(\eta^i)-\chi_A(\eta)\bigr)
={}&
c_i^0(\eta)\chi_{A\setminus\{i\}}(\eta)\\
&-\bigl(c_i^0(\eta)+c_i^1(\eta)\bigr)\chi_A(\eta).
\end{aligned}
$$

Indeed, when $\eta(i)=0$ only the first term remains, while when $\eta(i)=1$ the right-hand side is $-c_i^1(\eta)\chi_{A\setminus\{i\}}(\eta)$.

Insert the multilinear expansions of $c_i^0$ and $c_i^1$. Since

$$
\chi_S\chi_{A\setminus\{i\}}
=
\chi_{(A\setminus\{i\})\cup S},
\qquad
\chi_S\chi_A=\chi_{A\cup S},
$$

one obtains

$$
\mathcal L\chi_A
=
\sum_{i\in A}\sum_{S\subseteq N(i)}
a_i^\delta(S)\chi_{(A\setminus\{i\})\cup S}
+
\sum_{i\in A}\sum_{S\subseteq N(i)}
a_i^\beta(S)\chi_{A\cup S}.
\tag{3}
$$

The first sum gives deaths when $S=\varnothing$ and splits when $S\ne\varnothing$. The nonempty-target terms in the second sum give births. Its empty-target term is diagonal because $A\cup\varnothing=A$.

Now let $Y=(A,\sigma)$. Multiplying each dual rate by its sign recovers the corresponding signed coefficient, so

$$
\begin{aligned}
\mathcal D H(Y,\eta)
={}&
\sigma\sum_{i\in A}\sum_{S\subseteq N(i)}
a_i^\delta(S)
\chi_{(A\setminus\{i\})\cup S}(\eta)\\
&+
\sigma\sum_{i\in A}
\sum_{\substack{S\subseteq N(i)\\S\ne\varnothing}}
a_i^\beta(S)
\chi_{A\cup S}(\eta)\\
&-
\sum_{i\in A}
\left(
\sum_{S\subseteq N(i)}\delta_i(S)
+
\sum_{\substack{S\subseteq N(i)\\S\ne\varnothing}}\beta_i(S)
\right)H(Y,\eta).
\end{aligned}
$$

Adding $V(A)H(Y,\eta)$ cancels the total jump-rate subtraction and restores the diagonal coefficient

$$
\left(\sum_{i\in A}a_i^\beta(\varnothing)\right)H(Y,\eta).
$$

The resulting expression is $\sigma$ times the right-hand side of (3). This proves (1).

## Finite-volume Feynman-Kac formula

Fix $R\Subset\Lambda$ containing $A$. Let $P_t^{R,0}$ be the spin-system semigroup with zero boundary outside $R$, and let $E_t^R$ be the event that the signed-dual interaction cone stays inside $R$ through time $t$. Equivalently, kill the dual at the first successful interaction leaving $R$.

The killed dual is finite state. Applying the ordinary finite-state Feynman-Kac formula to (1) gives

$$
P_t^{R,0}\chi_A(\eta)
=
\mathbb E_A\left[
\sigma_t
\exp\left(\int_0^tV(A_s)\,ds\right)
\chi_{A_t}(\eta)
\mathbf1_{E_t^R}
\right].
\tag{4}
$$

## Passage to infinite volume

Take a finite exhaustion $R\uparrow\Lambda$. Local finiteness of the graphical dual implies

$$
E_t^R\uparrow\Omega
$$

almost surely. By (FK), the absolute value of the integrand in (4) is bounded by the integrable random variable

$$
\exp\left(\int_0^tV(A_s)\,ds\right).
$$

On the spin-system side, [finite propagation for zero-boundary restrictions](finite-propagation-for-zero-boundary-restrictions.md) gives

$$
P_t^{R,0}\chi_A\longrightarrow P_t\chi_A
$$

uniformly along the exhaustion. Dominated convergence on the right-hand side of (4) therefore gives (2).

## Pure deaths

The environment-independent calm-to-facilitating noise generator satisfies

$$
\mathcal N^{\mathbf0}\chi_A=-|A|\chi_A.
$$

Hence adding $\varepsilon\mathcal N^{\mathbf0}$ leaves the dual jumps unchanged and replaces the potential by

$$
V(A)-\varepsilon|A|.
$$

This is why the independent spin transitions $1\to0$ are called **pure deaths** in the dual language. The same observation supplies the exact exponential factors used in the [pure-death comparison](pure-death-comparison-under-patch-positivity.md) and [convergence proof](exponential-relaxation-under-confined-late-interactions.md).

The [successful-interaction skeleton](successful-interaction.md) retains only the nonempty-target interactions that act on this dual. Conditioning on that skeleton and averaging the omitted marks gives the [patch representation](patch-representation-of-spin-systems.md).
