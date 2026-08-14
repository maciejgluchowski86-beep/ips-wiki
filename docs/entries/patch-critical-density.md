---
title: Patch critical density
status: definition
audit: current
tags:
  - patch
  - patch positivity
  - critical density
  - spin systems
---

# Patch critical density

The patch critical density is a threshold defined from end-patch contributions. The definition below is retained independently of whether the current project formulas for those contributions are correct.

## Definition

For a site $i$, define

$$
p_i^\star
=
\inf\left\{
p\in[0,1]:
C(p,P)\ge0
\text{ for every possible end patch }P\text{ based at }i
\right\}.
$$

The patch critical density profile is

$$
\mathbf p^\star=(p_i^\star)_{i\in\Lambda}.
$$

For a translation-invariant model, when this profile is constant, denote its common value by $p^\star$.

This definition uses the end-patch contribution from [patch contribution](patch-contribution.md). Any explicit evaluation of the threshold inherits the unresolved status of the contribution formulas.

## Conditional coefficient formula

Assume the closed-form contribution identities in [patch contribution](patch-contribution.md) and the conditional [patch positivity property](patch-positivity-property.md). Under those assumptions, the current project calculation gives

$$
p_i^\star
=
\max\left\{
0,
\sup_{\substack{
\vn\ne S\subseteq N(i)\\
c_i^0(S)+c_i^1(S)<0
}}
\frac{c_i^0(S)}
{c_i^0(S)+c_i^1(S)}
\right\}.
\tag{1}
$$

The inner supremum is interpreted as $0$ when its index set is empty. Formula (1) is not currently a verified project result.

## Empty-neighbour bound

Assume the same unverified contribution and positivity identities as above, and suppose

$$
r_i=c_i^0(\vn)+c_i^1(\vn)>0,
\qquad
q_i=\frac{c_i^0(\vn)}{r_i}.
$$

Then the current project calculation gives, conditionally,

$$
p_i^\star\le q_i.
\tag{2}
$$

Indeed, for every nonempty $S\subseteq N(i)$ with $c_i^0(S)+c_i^1(S)<0$, the determinant inequality appearing in the conditional patch-positivity criterion is equivalent to

$$
\frac{c_i^0(S)}{c_i^0(S)+c_i^1(S)}
\le
\frac{c_i^0(\vn)}{c_i^0(\vn)+c_i^1(\vn)}.
$$

Thus (2) follows from the conditional coefficient formula (1). Both statements remain conditional until the contribution and positivity calculations are independently verified.
