---
title: Interaction cone
status: definition
audit: current
tags:
  - signed additive set process
  - successful interaction
  - patch
  - information spread
---

# Interaction cone

Fix a signed additive set process started from $A_0\Subset\Lambda$. For $T<\infty$, its interaction cone is

$$
\mathbf{Cone}_T
=
\bigcup_{(i,t,S)\in\mathcal I_T}
(\{i\}\cup S)\setminus\{\infty\},
$$

where $\mathcal I_T$ is the [successful-interaction](successful-interaction.md) skeleton. Thus $\mathbf{Cone}_T$ is the set of lattice sites reached by the skeleton by time $T$, and

$$
\mathbf{Cone}_0=A_0.
$$

The cones are increasing in $T$. The all-time reached set is

$$
\mathbf{Cone}_\infty
=
\bigcup_{T<\infty}\mathbf{Cone}_T.
$$

For $A_0\subseteq R\Subset\Lambda$, the event

$$
E_T^R=\{\mathbf{Cone}_T\subseteq R\}
$$

is the confinement event used in the [spatial-confinement estimate](undoing-duality-under-confined-interactions.md).

At every fixed finite horizon $T$, distinct end [patches](patch.md) have distinct sites, and each site reached by the skeleton carries exactly one end patch. Hence, almost surely,

$$
|\mathcal E_T|=|\mathbf{Cone}_T|.
$$

If no ordinary successful interaction occurs after time $T$, then the cone no longer grows. Each site in the common cone carries one full patch extending to infinity, whose truncation at time $t\ge T$ is the corresponding end patch at horizon $t$.
