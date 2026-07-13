---
title: Interaction cone
status: definition
tags:
  - signed additive set process
  - successful interaction
  - patch
  - information spread
---

# Interaction cone

Fix a [signed additive set process](signed-additive-set-process.md) started from \(A_0\Subset\Lambda\). For \(T\le\infty\), its interaction cone is

$$
\mathbf{Cone}_T
=
A_0
\cup
\bigcup_{(i,t,S)\in\mathcal I_T}
\bigl(\{i\}\cup S\bigr),
$$

where \(\mathcal I_T\) is the [successful-interaction](successful-interaction.md) set and \(\mathcal I_\infty=\mathcal I\). Thus \(\mathbf{Cone}_T\) is the set of sites reached from the initial set by time \(T\).

The cones are increasing in time, and

$$
\mathbf{Cone}_\infty
=
\bigcup_{T<\infty}\mathbf{Cone}_T.
$$

At every fixed finite horizon \(T\), almost surely, sending an end [patch](patch.md) to its site is a bijection from \(\mathcal E_T\) to \(\mathbf{Cone}_T\). In particular,

$$
|\mathcal E_T|=|\mathbf{Cone}_T|.
$$

If no successful interaction occurs after time \(T\), then \(\mathbf{Cone}_t=\mathbf{Cone}_T\) for every \(t\ge T\). Each site in this common cone then carries one infinite patch, whose truncation at time \(t\) is the corresponding element of \(\mathcal E_t\).
