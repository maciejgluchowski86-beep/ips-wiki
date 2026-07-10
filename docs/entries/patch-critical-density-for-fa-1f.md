---
title: Patch critical density for FA-1f
status: proved here
tags:
  - FA-1f
  - patch
  - critical density
  - KCSM
---

# Patch critical density for FA-1f

For the hard [FA-1f model](fa-1f-model.md), the [patch critical density](patch-critical-density.md) equals the equilibrium density of ones.

Write \(q\) for the vacancy density and

$$
p=1-q
$$

for the density of ones. Assume \(N(i)\ne\vn\). The only nonzero coefficients with nonempty interaction target are

$$
c_i^0(N(i))=-p,
\qquad
c_i^1(N(i))=-q.
$$

Therefore

$$
\frac{c_i^0(N(i))}
{c_i^0(N(i))+c_i^1(N(i))}
=
\frac{-p}{-p-q}
=
p,
$$

and all other nonempty targets impose threshold \(0\). Hence

$$
p_i^\star=p.
$$

Thus the critical profile is constant and

$$
p^\star=p=1-q.
$$

Equivalently, the \(\mathsf{OE}\) end contribution in the explicit [FA-1f patch formula](patch-contributions-for-fa-1f.md) is a positive multiple of

$$
\xi(i)-p,
$$

so its affine Bernoulli average is nonnegative exactly when the terminal one-density is at least \(p\).

If \(N(i)=\vn\), no nonempty-target patch can occur at \(i\), and the convention gives \(p_i^\star=0\).
