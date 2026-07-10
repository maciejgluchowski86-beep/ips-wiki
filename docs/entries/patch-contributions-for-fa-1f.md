---
title: Patch contributions for FA-1f
status: definition
tags:
  - KCSM
  - FA-1f
  - duality
  - patch
---

# Patch contributions for FA-1f

This entry specializes the general [patch contribution](patch-contribution.md) formulas to the hard [FA-1f model](fa-1f-model.md). It uses the rates and signs from [monomial duality for FA-1f](monomial-duality-for-fa-1f.md). Write \(p=1-q\), where \(q\) is the vacancy density, and assume \(N(i)\ne\vn\).

For a patch \(P=\{i\}\times[s_-,s_+)\), set \(\Delta=s_+-s_-\). The only nonempty target for source \(i\) is \(N(i)\), so in every \(\mathsf O\)-initial row the initial interaction target is \(S=N(i)\). The hard FA-1f substitution gives

$$
\begin{aligned}
\alpha&=1+2p,
&
V_i&=2p,
\\
\varphi(\Delta)
&=
\frac{p+(1+p)e^{-(1+2p)\Delta}}{1+2p},
&
\psi(\Delta,z)
&=
z e^{-\Delta}+p(1-e^{-\Delta}).
\end{aligned}
$$

The simplifications in the \(\mathsf O\)-initial rows use

$$
\psi(\Delta,1)-p=qe^{-\Delta},
\qquad
\psi(\Delta,\xi(i))-p=(\xi(i)-p)e^{-\Delta}.
$$

For a bulk patch \(P\in\mathcal B_T\), the contribution is

$$
C(P)
=
\begin{cases}
\dfrac{\psi(\Delta,1)}{\varphi(\Delta)},
& \operatorname{type}(P)\in\{\mathsf{SI},\mathsf{II}\},\\[1.2em]
e^{2p\Delta},
& \operatorname{type}(P)\in\{\mathsf{SO},\mathsf{IO}\},\\[1.2em]
\dfrac{q e^{-\Delta}}{p+\varphi(\Delta)},
& \operatorname{type}(P)=\mathsf{OI},\\[1.2em]
e^{2p\Delta},
& \operatorname{type}(P)=\mathsf{OO}.
\end{cases}
$$

For an end patch \(P\in\mathcal E_T\), the contribution is

$$
C(\xi,P)
=
\begin{cases}
\dfrac{\psi(\Delta,\xi(i))}{\varphi(\Delta)},
& \operatorname{type}(P)\in\{\mathsf{SE},\mathsf{IE}\},\\[1.2em]
\dfrac{(\xi(i)-p)e^{-\Delta}}{p+\varphi(\Delta)},
& \operatorname{type}(P)=\mathsf{OE}.
\end{cases}
$$

If \(N(i)=\vn\), hard FA-1f has no legal update at \(i\). No nonempty-target successful interaction can start or end a patch at that site, and an initially active isolated-site end patch has contribution \(C(\xi,P)=\xi(i)\).