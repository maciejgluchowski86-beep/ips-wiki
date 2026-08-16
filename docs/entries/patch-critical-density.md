---
title: Patch threshold profile
status: proved here
audit: current
tags:
  - patch
  - patch positivity
  - threshold profile
  - spin systems
---

# Patch threshold profile

For a patch-positive spin system, the **patch threshold profile**

$$
\mathbf p^\star=(p_i^\star)_{i\in\Lambda}
$$

records the calm-state density above which every end-patch contribution is nonnegative. It is a threshold for the sign of terminal patch factors, not an ergodicity threshold or a phase-transition critical density.

## Definition

For each site $i$,

$$
p_i^\star
=
\inf\left\{
p\in[0,1]:
C(p,P)\ge0
\text{ for every end patch based at }i
\right\}.
\tag{1}
$$

Incoming end patches are nonnegative for every $p\in[0,1]$. The restriction comes from outgoing end patches.

## Theorem: coefficient formula

Under [patch positivity](patch-positivity-property.md),

$$
p_i^\star
=
\max\left\{
0,
\sup_{\substack{
\varnothing\ne S\subseteq N(i)\\
c_i^0(S)+c_i^1(S)<0
}}
\frac{c_i^0(S)}{c_i^0(S)+c_i^1(S)}
\right\}.
\tag{2}
$$

If the index set in the supremum is empty, it imposes no positive restriction.

## Proof

An incoming end patch has contribution

$$
C(p,P)
=
\frac{\psi_i(\Delta,p)}{\varphi_i(\Delta)},
$$

which is nonnegative for every $p\in[0,1]$. Thus only outgoing end patches matter.

Put

$$
r_i=c_i^0(\varnothing)+c_i^1(\varnothing).
$$

If $r_i=0$, patch positivity forces $c_i\equiv0$. There are then no outgoing end patches based at $i$, so $p_i^\star=0$, agreeing with (2).

Assume now that $r_i>0$. Let $P$ be an outgoing end patch based at $i$ with nonempty initial target $S$. Its denominator is positive, while its numerator is

$$
N_{i,S}(\Delta,p)
=
c_i^0(S)
-
\bigl(c_i^0(S)+c_i^1(S)\bigr)\psi_i(\Delta,p).
\tag{3}
$$

Patch positivity gives

$$
c_i^0(S)+c_i^1(S)\le0,
$$

so $N_{i,S}(\Delta,p)$ is nondecreasing in $p$. The empty-neighbour relaxation formula is

$$
\psi_i(\Delta,p)
=
\frac{c_i^0(\varnothing)}{r_i}
+
\left(
p-
\frac{c_i^0(\varnothing)}{r_i}
\right)e^{-r_i\Delta}.
\tag{4}
$$

At zero length,

$$
N_{i,S}(0,p)
=
c_i^0(S)
-
\bigl(c_i^0(S)+c_i^1(S)\bigr)p.
\tag{5}
$$

In the long-patch limit,

$$
\lim_{\Delta\to\infty}N_{i,S}(\Delta,p)
=
\frac{
c_i^1(\varnothing)c_i^0(S)
-
c_i^0(\varnothing)c_i^1(S)
}{r_i},
\tag{6}
$$

which is nonnegative by the second inequality in the patch-positivity criterion.

For fixed $p$, expression (3) is affine in $e^{-r_i\Delta}$. Therefore its minimum over $\Delta\ge0$ occurs at one of the two endpoints represented by (5) and (6). Since (6) is already nonnegative, $N_{i,S}(\Delta,p)$ is nonnegative for every patch length exactly when the short-patch value (5) is nonnegative.

If

$$
c_i^0(S)+c_i^1(S)=0,
$$

then the second patch-positivity inequality gives $c_i^0(S)\ge0$, so $S$ imposes no restriction on $p$.

If instead

$$
c_i^0(S)+c_i^1(S)<0,
$$

then (5) is nonnegative exactly when

$$
p
\ge
\frac{c_i^0(S)}{c_i^0(S)+c_i^1(S)}.
\tag{7}
$$

Taking the supremum over nonempty targets with negative coefficient sum and imposing $p\ge0$ proves (2). Patch positivity also implies that every ratio appearing in (2) is at most $1$, so the right-hand side is a valid density threshold.

## Corollary: empty-neighbour bound

If $r_i>0$, then

$$
p_i^\star
\le
\frac{c_i^0(\varnothing)}{c_i^0(\varnothing)+c_i^1(\varnothing)}.
\tag{8}
$$

### Proof

For every nonempty $S$ with

$$
c_i^0(S)+c_i^1(S)<0,
$$

the second patch-positivity inequality

$$
c_i^1(\varnothing)c_i^0(S)
\ge
c_i^0(\varnothing)c_i^1(S)
$$

is equivalent, after dividing by the negative denominator in (7) and by the positive $r_i$, to

$$
\frac{c_i^0(S)}{c_i^0(S)+c_i^1(S)}
\le
\frac{c_i^0(\varnothing)}{c_i^0(\varnothing)+c_i^1(\varnothing)}.
$$

Taking the supremum in (2) proves (8).

The profile $\mathbf p^\star$ is the centering profile for the [centered-moment order and cones](high-density-measure.md).
