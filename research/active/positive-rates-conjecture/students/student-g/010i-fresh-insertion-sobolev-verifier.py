#!/usr/bin/env python3
"""Exact scalar verifier for Student G checkpoint 010i.

Checks the fixed-filter inequality |x q(x)|<1 for x>0 by coefficient
positivity, the rational L1 bound imported from corrected checkpoint 010h,
and the exact margin in the reversible-reference fresh-insertion H^1 bound.
"""

import sympy as sp

x = sp.symbols("x", nonnegative=True)
a = sp.Rational(1, 1000)
B = sp.Rational(10989, 10000)
omega = sp.Rational(11, 10000)
tau = sp.Rational(4, 125)

# Reversible reference P_0 and fresh centered coordinate X.
c0 = sp.Rational(999, 1000)
g0 = sp.Rational(999, 10000)
r = sp.Rational(11, 10)
m0 = -sp.Rational(9, 10000)


def Z(alpha):
    return sp.factor(
        (alpha + 1 + B + a) / ((alpha + a) * (alpha + 1 + B) - a)
    )


q = sp.factor(Z(omega + x) - 2 * Z(omega + tau + x))
num, den = sp.fraction(q)

# den>0 on x>=0 from its displayed positive-coefficient factorisation.
den_expected = (
    (100000 * x**2 + 210210 * x + 341)
    * (2500000 * x**2 + 5415250 * x + 179253)
)
assert sp.expand(den - den_expected) == 0

# 1 +/- x q(x)>0 for x>=0.  Both numerators have strictly positive
# coefficients, so this is an exact all-x certificate.
minus_poly = sp.Poly(sp.expand(den - x * num), x)
plus_poly = sp.Poly(sp.expand(den + x * num), x)
assert all(coef > 0 for coef in minus_poly.all_coeffs())
assert all(coef > 0 for coef in plus_poly.all_coeffs())

# Imported exact 010h bound ||h||_1 < h_L1_upper < 625.
h_L1_upper = sp.Rational(881295044, 1453125)
assert h_L1_upper < 625

# The fresh-insertion variational constant is sqrt(c0*g0/r).
fresh_sq = sp.factor(c0 * g0 / r)
assert fresh_sq == sp.Rational(998001, 11000000)

# From |xq|<1 and |q|<=||h||_1<625, sqrt(x)|q(x)|<25.
# Hence the actual Y=X+m0 reference transfer obeys
# ||A_0^(1/2) Q_0 M_Y f|| <= (sqrt(fresh_sq)+25|m0|)||f||.
scalar_part = 25 * abs(m0)
assert scalar_part == sp.Rational(9, 400)
assert fresh_sq < (1 - scalar_part) ** 2

print("q(x) =", q)
print("den - x*num coefficients =", minus_poly.all_coeffs())
print("den + x*num coefficients =", plus_poly.all_coeffs())
print("fresh_sq =", fresh_sq)
print("25*|m0| =", scalar_part)
print("sqrt(fresh_sq) + 25*|m0| < 1 verified exactly")
