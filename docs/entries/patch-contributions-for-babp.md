---
title: Patch contributions for BABP
status: definition
tags:
  - KCSM
  - BABP
  - duality
  - patch
---

# Patch contributions for BABP

This entry specializes the general [patch contribution](patch-contribution.md) formulas to the [biased annihilating branching process](babp-model.md). It uses the rates and signs from [monomial duality for BABP](monomial-duality-for-babp.md). The resulting end-factor threshold is identified under [patch critical density for BABP](patch-critical-density-for-babp.md).

Write \(p=1-q\), where \(q\) is the vacancy density, and fix a patch \(P\) based at \(i=i(P)\), with \(N(i)\ne\vn\). Evaluate the patch at \(t\in[s(P),e(P)]\), and put

$$
n=|N(i)|,
\qquad
\Delta_-=t-s(P),
\qquad
\Delta_+=e(P)-t,
\qquad
\Delta=e(P)-s(P).
$$

Every nonempty interaction target is a singleton \(S(P)=\{j\}\) with \(j\in N(i)\). Since all such targets have the same rates, the contribution depends on the target only through the patch labels. Substituting the BABP dual rates gives

$$
\begin{aligned}
\alpha_i&=(1+2p)n,
&
V_i&=2pn,
\\
\varphi_i(\Delta)
&=
\frac{
p+(1+p)e^{-(1+2p)n\Delta}
}{
1+2p
},
\\
\psi_i(\Delta_-,\Delta_+,z)
&=
p\left(1-e^{-n\Delta_-}\right)
+
ze^{-n\Delta_-}\varphi_i(\Delta_+).
\end{aligned}
\tag{1}
$$

When only one duration appears, write

$$
\psi_i(\Delta,z)
=
\psi_i(\Delta,0,z)
=
p\left(1-e^{-n\Delta}\right)+ze^{-n\Delta}.
\tag{2}
$$

## Contribution at an intermediate time

For every patch with positive consistency probability, the substitution in the four general patch rows gives

$$
C_t(z,P)
=
\begin{cases}
\dfrac{\psi_i(\Delta_-,\Delta_+,z)}{\varphi_i(\Delta)},
& \mathsf X(P)=\mathsf I,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.2em]
z e^{2pn\Delta_-},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf O),
\\[1.2em]
\dfrac{\psi_i(\Delta_-,\Delta_+,z)-p}
{p+\varphi_i(\Delta)},
& \mathsf X(P)=\mathsf O,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.2em]
z e^{2pn\Delta_-},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf O).
\end{cases}
\tag{3}
$$

The third row follows from the singleton split rate \(p\) with negative sign and singleton birth rate \(1\) with positive sign. This is the only row where the signed initial interaction enters the calculation.

When \(e(P)=\infty\), the occurrences of \(\varphi_i(\Delta_+)\) and \(\varphi_i(\Delta)\) in (3) mean their limits at infinity.

## Full-patch contributions

For a full patch \(P\in\mathcal P\), take \(t\uparrow e(P)\) and set \(z=1\) in (3). This gives

$$
C(P)
=
\begin{cases}
\dfrac{\psi_i(\Delta,1)}{\varphi_i(\Delta)},
& \mathsf X(P)=\mathsf I,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.2em]
e^{2pn\Delta},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf O),
\\[1.2em]
\dfrac{qe^{-n\Delta}}{p+\varphi_i(\Delta)},
& \mathsf X(P)=\mathsf O,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.2em]
e^{2pn\Delta},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf O).
\end{cases}
\tag{4}
$$

The functions in (4) are evaluated at \(\Delta=\infty\) by taking limits. The terminal-\(\mathsf O\) rows occur only for finite \(\Delta\).

## End-patch contributions

For an end patch \(P\in\mathcal E_t\), one has \(e(P)=t\) and \(\Delta_+=0\). Formula (3) therefore reduces to

$$
C(z,P)
=
\begin{cases}
\dfrac{\psi_i(\Delta,z)}{\varphi_i(\Delta)},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf E),
\\[1.2em]
\dfrac{(z-p)e^{-n\Delta}}{p+\varphi_i(\Delta)},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf E).
\end{cases}
\tag{5}
$$

The simplifications in (4)--(5) use

$$
\psi_i(\Delta,1)-p=qe^{-n\Delta},
\qquad
\psi_i(\Delta,z)-p=(z-p)e^{-n\Delta}.
$$

If \(N(i)=\vn\), BABP has no update at \(i\). No nonempty-target successful interaction can start or end a patch there, and an initially active isolated-site end patch has contribution \(C(z,P)=z\).
