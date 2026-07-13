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

This entry specializes the general [patch contribution](patch-contribution.md) formulas to the hard [FA-1f model](fa-1f-model.md). The associated end-factor threshold is recorded as the [patch critical density for FA-1f](patch-critical-density-for-fa-1f.md). It uses the rates and signs from [monomial duality for FA-1f](monomial-duality-for-fa-1f.md). Write \(p=1-q\), where \(q\) is the vacancy density, and assume \(N(i)\ne\vn\).

Fix a patch \(P\), evaluate it at \(t\in[s(P),e(P)]\), and put

$$
\Delta_-=t-s(P),
\qquad
\Delta_+=e(P)-t,
\qquad
\Delta=e(P)-s(P)=\Delta_-+\Delta_+.
$$

The only nonempty target for source \(i=i(P)\) is \(N(i)\), so every \(\mathsf O\)-initial patch has \(S(P)=N(i)\). The hard FA-1f substitution gives

$$
\begin{aligned}
\alpha&=1+2p,
&
V_i&=2p,
\\
\varphi(\Delta)
&=
\frac{p+(1+p)e^{-(1+2p)\Delta}}{1+2p},
\\
\psi(\Delta_-,\Delta_+,z)
&=
p\left(1-e^{-\Delta_-}\right)
+
z e^{-\Delta_-}\varphi(\Delta_+).
\end{aligned}
$$

When only one duration appears, write

$$
\psi(\Delta,z)
=
\psi(\Delta,0,z)
=
p\left(1-e^{-\Delta}\right)+ze^{-\Delta}.
$$

For every patch with positive consistency probability,

$$
C_t(z,P)
=
\begin{cases}
\dfrac{\psi(\Delta_-,\Delta_+,z)}{\varphi(\Delta)},
& \mathsf X(P)=\mathsf I,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.2em]
z e^{2p\Delta_-},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf O),
\\[1.2em]
\dfrac{\psi(\Delta_-,\Delta_+,z)-p}{p+\varphi(\Delta)},
& \mathsf X(P)=\mathsf O,
\quad
\mathsf Y(P)\in\{\mathsf I,\mathsf E\},
\\[1.2em]
z e^{2p\Delta_-},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf O).
\end{cases}
\tag{1}
$$

When \(e(P)=\infty\), the occurrences of \(\varphi(\Delta_+)\) and \(\varphi(\Delta)\) in (1) mean their limits at infinity.

For a bulk patch \(P\in\mathcal B_t\), set \(t=e(P)\) and \(z=1\). Thus

$$
C(P)
=
\begin{cases}
\dfrac{\psi(\Delta,1)}{\varphi(\Delta)},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf I),
\\[1.2em]
e^{2p\Delta},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf O),
\\[1.2em]
\dfrac{q e^{-\Delta}}{p+\varphi(\Delta)},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf I),
\\[1.2em]
e^{2p\Delta},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf O).
\end{cases}
\tag{2}
$$

For an end patch \(P\in\mathcal E_t\), one has \(e(P)=t\) and \(\Delta_+=0\), so

$$
C(z,P)
=
\begin{cases}
\dfrac{\psi(\Delta,z)}{\varphi(\Delta)},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf I,\mathsf E),
\\[1.2em]
\dfrac{(z-p)e^{-\Delta}}{p+\varphi(\Delta)},
& (\mathsf X(P),\mathsf Y(P))=(\mathsf O,\mathsf E).
\end{cases}
\tag{3}
$$

The last rows of (2) and (3) use

$$
\psi(\Delta,1)-p=qe^{-\Delta},
\qquad
\psi(\Delta,z)-p=(z-p)e^{-\Delta}.
$$

If \(N(i)=\vn\), hard FA-1f has no legal update at \(i\). No nonempty-target successful interaction can start or end a patch at that site, and an initially active isolated-site end patch has contribution \(C(z,P)=z\).
