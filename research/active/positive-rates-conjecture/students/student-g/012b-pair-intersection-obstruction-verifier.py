#!/usr/bin/env python3
"""Exact scalar checks for the Assignment 012 pair-intersection obstruction.

The analytic argument uses the exact ancestry polytope from 012a. Uniformly
across that polytope at P_h,

    u := d+j <= 1/5000,
    r >= 4999/5000.

For two independent support histories and block time T=8, a width-one good
cell requires no loss mark (death/right-jump) at sites i,i+1 in either copy
and at least one branch mark at i in each copy. Its probability is at least

    exp(-4*u*T) * (1-exp(-r*T))^2.

This script checks exact rational lower bounds implying that the bad-cell
probability is < 1/128. The remaining Peierls cut-contour step is analytic.
"""

from fractions import Fraction as F
from math import factorial

u = F(1, 5000)
r = F(4999, 5000)
T = 8

# e^{-x} > 1-x for x>0.
x = 4 * u * T
assert x == F(4, 625)
no_loss_lower = 1 - x
assert no_loss_lower == F(621, 625)

# r*T > 31/4 and the first 12 positive Taylor terms for exp(31/4)
# already exceed 2000. Hence exp(-r*T) < 1/2000.
assert r * T > F(31, 4)
y = F(31, 4)
partial = sum(y ** k / factorial(k) for k in range(12))
assert partial > 2000
branch_each_lower = F(1999, 2000)

p_lower = no_loss_lower * branch_each_lower**2
q_upper = 1 - p_lower
assert p_lower == F(2481516621, 2500000000)
assert q_upper == F(18483379, 2500000000)
assert q_upper < F(1, 128)

# In the contour proof, at least half of the bad cells on a fixed contour are
# mutually independent. Allow at most 2*m*3^m anchored contours of length m.
# Since q<1/128<(4/45)^2, one has 3*sqrt(q)<4/15. Therefore
#
#   sum_{m>=1} 2*m*(3*sqrt(q))^m
#     < 2 * sum_{m>=1} m*(4/15)^m
#     = 120/121 < 1.
assert F(1, 128) < F(16, 2025)
contour_union_upper = F(120, 121)
assert contour_union_upper < 1
survival_lower = 1 - contour_union_upper
assert survival_lower == F(1, 121)

print("uniform loss bound u <=", u)
print("uniform branch bound r >=", r)
print("good-cell probability >", p_lower)
print("bad-cell probability <", q_upper, "< 1/128")
print("Peierls contour union bound < 120/121; survival probability > 1/121")
