---
title: Patch
status: definition
tags:
  - signed additive set process
  - graphical construction
  - successful interaction
  - patch
---

# Patch

Fix a [signed additive set process](signed-additive-set-process.md), its [graphical construction](graphical-construction-of-signed-additive-set-process.md), and the full successful-interaction set \(\mathcal I\). A successful interaction \((i,t,S)\) touches its source \(i\) as an outgoing touch and every target \(j\in S\) as an incoming touch.

For \(i\in\Lambda\), define

$$
\begin{aligned}
\mathcal T^{\mathsf I}(i)
&=
\left\{
t\ge0:
\text{some }(j,t,S)\in\mathcal I
\text{ satisfies }i\in S
\right\},
\\
\mathcal T^{\mathsf O}(i)
&=
\left\{
t\ge0:
\text{some }(i,t,S)\in\mathcal I
\right\}.
\end{aligned}
$$

The possible starting times at \(i\) are

$$
\mathcal S(i)
=
\mathcal S^0(i)
\cup\mathcal T^{\mathsf I}(i)
\cup\mathcal T^{\mathsf O}(i),
\qquad
\mathcal S^0(i)
=
\begin{cases}
\{0\}, & i\in A_0,\\
\vn, & i\notin A_0.
\end{cases}
$$

For \(s\in\mathcal S(i)\), let

$$
e_i(s)
=
\inf\left\{
u>s:
u\in\mathcal T^{\mathsf I}(i)\cup\mathcal T^{\mathsf O}(i)
\right\},
$$

with \(\inf\vn=\infty\).

## Full patches

The patch beginning at \((i,s)\) is the labeled object

$$
P
=
\{i(P)\}\times[s(P),e(P))
\times
\left\{\bigl(\mathsf X(P)\mathsf Y(P),S(P)\bigr)\right\},
$$

where

$$
i(P)=i,
\qquad
s(P)=s,
\qquad
e(P)=e_i(s).
$$

In particular,

$$
i(P)\in\Lambda,
\qquad
0\le s(P)\le e(P)\le\infty.
$$

The initial target set is defined as follows. If \(s(P)=0\), set

$$
S(P)=A_0.
$$

If \(s(P)>0\), then \(P\) begins at a successful-interaction skeleton \((j,s(P),S)\) that touches \(i(P)\), either at its source or in its target. Set

$$
S(P)=S.
$$

Thus \(S(P)\Subset\Lambda\) is part of the patch data.

The initial label is

$$
\mathsf X(P)
=
\begin{cases}
\mathsf S, & s(P)=0,\\
\mathsf I, & s(P)>0\text{ and }i(P)\in S(P),\\
\mathsf O, & s(P)>0\text{ and }i(P)\notin S(P).
\end{cases}
$$

Indeed, an incoming patch begins at a target of its initial interaction, while an outgoing patch begins at its source. Since interaction targets lie in \(N(i(P))\), they do not contain their source.

The terminal label is

$$
\mathsf Y(P)
=
\begin{cases}
\mathsf I, & e(P)<\infty
\text{ and }e(P)\in\mathcal T^{\mathsf I}(i(P)),\\
\mathsf O, & e(P)<\infty
\text{ and }e(P)\in\mathcal T^{\mathsf O}(i(P)),\\
\mathsf E, & e(P)=\infty.
\end{cases}
$$

Thus

$$
\mathsf X(P)\in\{\mathsf S,\mathsf I,\mathsf O\},
\qquad
\mathsf Y(P)\in\{\mathsf I,\mathsf O,\mathsf E\}.
$$

The label \(\mathsf E\) records that the patch has no successful-touch terminal boundary. For a full patch this occurs precisely when the patch is infinite. The same label will be used below when a patch is cut at a finite time horizon.

The family of all full patches is denoted by \(\mathcal P\). A patch is finite when \(e(P)<\infty\) and infinite when \(e(P)=\infty\). Every initially active site begins a patch at time zero. Every successful interaction cuts spacetime at its source and target sites, ending the preceding patches and beginning new ones at those sites. Every active spacetime point lies in the spacetime projection of a patch.

Under the local-finiteness assumption, starting from \(A_0\Subset\Lambda\),

$$
|\mathcal P|<\infty
\quad\Longleftrightarrow\quad
|\mathcal I|<\infty.
$$

Indeed, every successful interaction creates patch boundaries. Conversely, finitely many successful interactions touch only finitely many sites and create only finitely many patches, including the final infinite patches.

On the null event of simultaneous successful touches at the same site, use the deterministic ordering fixed in the graphical construction to determine the successive boundary labels.

## Truncation at a time horizon

For \(t\ge0\) and \(P\in\mathcal P\), define

$$
P^{(t)}=\vn
\qquad\text{when }t\le s(P).
$$

When \(t>s(P)\), define

$$
e^{(t)}(P)=\min\{e(P),t\}
$$

and

$$
\mathsf Y^{(t)}(P)
=
\begin{cases}
\mathsf Y(P), & e(P)\le t,\\
\mathsf E, & s(P)<t<e(P).
\end{cases}
$$

The truncation of \(P\) at time \(t\) is

$$
P^{(t)}
=
\{i(P)\}\times[s(P),e^{(t)}(P))
\times
\left\{\bigl(\mathsf X(P)\mathsf Y^{(t)}(P),S(P)\bigr)\right\}.
$$

Thus truncation preserves the site, start time, initial label, and initial target set. If the time horizon cuts the patch, its terminal label is replaced by \(\mathsf E\). If the patch has already ended, then \(P^{(t)}=P\), including its original terminal label.

The bulk patches completed by time \(t\) are

$$
\mathcal B_t
=
\{P\in\mathcal P:P^{(t)}=P\}.
$$

The full patches cut by time \(t\) are

$$
\mathcal C_t
=
\left\{
P\in\mathcal P:
\vn\ne P^{(t)}\ne P
\right\}.
$$

Their truncations are the end patches

$$
\mathcal E_t
=
\{P^{(t)}:P\in\mathcal C_t\}.
$$

The finite-horizon patch family is

$$
\mathcal P_t
=
\mathcal B_t\cup\mathcal E_t.
$$

Sending a cut patch to its truncation is a bijection

$$
\mathcal C_t\longrightarrow\mathcal E_t,
\qquad
P\longmapsto P^{(t)}.
$$

The possible labels in \(\mathcal P_t\) are

$$
\mathsf{SI},\ \mathsf{SO},\ \mathsf{SE},\qquad
\mathsf{II},\ \mathsf{IO},\ \mathsf{IE},\qquad
\mathsf{OI},\ \mathsf{OO},\ \mathsf{OE}.
$$

Every end patch has terminal label \(\mathsf E\). The label does not separately record whether the patch is a finite truncation or a full infinite patch; that distinction is carried by the patch family and its end time.

Set \(P^{(\infty)}=P\) and \(\mathcal P_\infty=\mathcal P\).

For every fixed \(t>0\), almost surely, sending an end patch to its site is a bijection from \(\mathcal E_t\) to the [interaction cone](interaction-cone.md) \(\mathbf{Cone}_t\). Consequently,

$$
|\mathcal C_t|
=
|\mathcal E_t|
=
|\mathbf{Cone}_t|.
$$

The local laws and factors associated with these labeled objects are defined in [patch consistency event](patch-consistency-event.md) and [patch contribution](patch-contribution.md).
