#!/usr/bin/env python3
"""Exact scalar checks for the Assignment 012 pair-intersection obstruction.

The analytic argument uses the exact ancestry polytope from 012a.  Uniformly
across that polytope at P_h,

    u := d+j <= 1/5000,
    r >= 4999/5000.

For two independent support histories and block time T=8, a width-one good
cell requires no loss mark (death/right-jump) at sites i,i+1 in either copy
and at least one branch mark at i in each copy.  Its probability is at least

    exp(-4*u*T) * (1-exp(-r*T))^2.

This script checks exact rational lower bounds implying that the bad-cell
probability is < 1/100.  The remaining Peierls contour step is analytic.
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

# r*T > 7 and e^7 > 1000, so exp(-r*T) < 1/1000.
assert r * T > 7
partial_e7 = sum(F(7) ** k / factorial(k) for k in range(12))
assert partial_e7 > 1000
branch_each_lower = F(999, 1000)

p_lower = no_loss_lower * branch_each_lower**2
q_upper = 1 - p_lower
assert p_lower == F(619758621, 625000000)
assert q_upper == F(5241379, 625000000)
assert q_upper < F(1, 100)

# In the contour proof, at least half of the bad cells on a contour are
# mutually independent.  At most 2*3^m contours of length m are used.
# q<1/100 implies 3*sqrt(q)<3/10, so the union bound is strictly below
#   2 * sum_{m>=1} (3/10)^m = 6/7 < 1.
assert F(6, 7) < 1
survival_lower = 1 - F(6, 7)
assert survival_lower == F(1, 7)

print("uniform loss bound u <=", u)
print("uniform branch bound r >=", r)
print("good-cell probability >", p_lower)
print("bad-cell probability <", q_upper, "< 1/100")
print("Peierls contour union bound < 6/7; survival probability > 1/7")
