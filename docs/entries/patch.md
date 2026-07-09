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

Fix a [signed additive set process](signed-additive-set-process.md), its [graphical construction](graphical-construction-of-signed-additive-set-process.md), and a horizon \(T<\infty\). Let \(\mathcal I_T^S\) be the type-\(S\) [successful interaction](successful-interaction.md) set.

A type-\(S\) successful interaction \((i,t,\alpha,S)\) touches its source \(i\) as an outgoing touch and each target \(j\in S\) as an incoming touch.

For \(i\in\Lambda\), define

$$
\mathcal T_T^{\mathsf I}(i)
=
\{t\le T:\exists j\in\Lambda,\ \exists S\ne\vn,\ \exists\alpha\in\{\delta,\beta\}
\text{ with }(j,t,\alpha,S)\in\mathcal I_T^S\text{ and }i\in S\},
$$

and

$$
\mathcal T_T^{\mathsf O}(i)
=
\{t\le T:\exists S\ne\vn,\ \exists\alpha\in\{\delta,\beta\}
\text{ with }(i,t,\alpha,S)\in\mathcal I_T^S\}.
$$

The source-keeping outgoing touch times are

$$
\mathcal T_T^{\mathsf O,\beta}(i)
=
\{t\le T:\exists S\ne\vn
\text{ with }(i,t,\beta,S)\in\mathcal I_T^S\}.
$$

Define the possible initial and terminal boundary times by

$$
\mathcal S_T(i)
=
\bigl(\{0\}:i\in A_0\bigr)
\cup\mathcal T_T^{\mathsf I}(i)
\cup\mathcal T_T^{\mathsf O,\beta}(i),
$$

and

$$
\mathcal E_T(i)
=
\{T\}\cup\mathcal T_T^{\mathsf I}(i)\cup\mathcal T_T^{\mathsf O}(i).
$$

Here \((\{0\}:i\in A_0)\) means \(\{0\}\) if \(i\in A_0\), and \(\vn\) otherwise.

A patch at \(i\) is a spacetime interval

$$
\{i\}\times [s,t)
$$

where \(s\in\mathcal S_T(i)\), \(t\in\mathcal E_T(i)\), \(s<t\), and there is no element of \(\mathcal S_T(i)\cup\mathcal E_T(i)\) strictly between \(s\) and \(t\). The set of all patches before horizon \(T\) is denoted by \(\mathcal P_T\).

The initial boundary type of \(\{i\}\times[s,t)\) is \(\mathsf S\), \(\mathsf I\), or \(\mathsf O\) according as

$$
s=0,
\qquad
s\in\mathcal T_T^{\mathsf I}(i),
\qquad
s\in\mathcal T_T^{\mathsf O,\beta}(i).
$$

The terminal boundary type is \(\mathsf E\), \(\mathsf I\), or \(\mathsf O\) according as

$$
t=T,
\qquad
t\in\mathcal T_T^{\mathsf I}(i),
\qquad
t\in\mathcal T_T^{\mathsf O}(i).
$$

The patch type is the ordered pair of boundary types. The possible types are

$$
\mathsf{SI},\ \mathsf{SO},\ \mathsf{SE},\quad
\mathsf{II},\ \mathsf{IO},\ \mathsf{IE},\quad
\mathsf{OI},\ \mathsf{OO},\ \mathsf{OE}.
$$

The patches cover the active spacetime region between successful touches. Spacetime regions that are never active are not covered by patches.

On the null event of simultaneous successful touches at the same site, use the deterministic ordering of marks fixed in the graphical construction.