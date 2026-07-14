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
\bigcup_{(i,t,S)\in\mathcal I_T}
\{i\}\cup S \setminus \{\infty\},
$$

where \(\mathcal I_T\) is the [successful-interaction](successful-interaction.md) set and \(\mathcal I_\infty=\mathcal I\). The initial skeleton \((\infty,0,A_0)\) contributes its target \(A_0\) but not its formal source. Thus \(\mathbf{Cone}_T\subseteq\Lambda\) is the set of lattice sites reached by time \(T\), and

$$
\mathbf{Cone}_0=A_0.
$$

The cones are increasing in time, and

$$
\mathbf{Cone}_\infty
=
\bigcup_{T<\infty}\mathbf{Cone}_T.
$$

At every fixed finite horizon \(T\ge0\), almost surely, sending an end [patch](patch.md) to its site is a bijection from \(\mathcal E_T\) to \(\mathbf{Cone}_T\). At time zero, \(\mathcal E_0\) consists of the zero-length \(\mathsf{IE}\) patches based at the sites of \(A_0\). In particular,

$$
|\mathcal E_T|=|\mathbf{Cone}_T|.
$$

If no ordinary successful interaction occurs after time \(T\), then \(\mathbf{Cone}_t=\mathbf{Cone}_T\) for every \(t\ge T\). Each site in this common cone then carries one infinite patch, whose truncation at time \(t\) is the corresponding element of \(\mathcal E_t\).
