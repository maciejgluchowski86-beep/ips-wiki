#!/usr/bin/env python3
"""Exact checks for Student G 009a.

This verifier checks only the algebraic normalization/calibration in
009a-canonical-j-recursion-checkpoint.md.  It makes no asymptotic J-SPEC claim.
"""

import sympy as sp


a = sp.Rational(1, 1000)
b = sp.Rational(1, 10)
c = sp.Rational(9999, 10000)
B = sp.factor(b + c - a)
g = sp.factor(b - a)
omega = sp.factor(1 - c + a)
r0 = sp.factor(1 / (1 + b))
m0 = sp.factor(B * r0 - c)

assert B == sp.Rational(10989, 10000)
assert g == sp.Rational(99, 1000)
assert sp.factor(B / g) == sp.Rational(111, 10)
assert omega == sp.Rational(11, 10000)
assert r0 == sp.Rational(10, 11)
assert m0 == -sp.Rational(9, 10000)

alpha = sp.symbols("alpha")
Zalpha = sp.factor(
    (alpha + 1 + B + a) / ((alpha + a) * (alpha + 1 + B) - a)
)
Z = sp.factor(Zalpha.subs(alpha, omega))
assert Z == sp.Rational(19100, 31)

R1 = sp.factor((-m0) * Z)
J1 = sp.factor((B / g) * R1)
N1 = sp.factor((B / g) ** 2 * R1)

assert R1 == sp.Rational(1719, 3100)
assert J1 == sp.Rational(190809, 31000)
assert N1 == sp.Rational(21179799, 310000)

# The two stated normalization relations are exactly compatible.
assert sp.factor(J1 - (g / B) * N1) == 0
assert sp.factor(J1 - (B / g) * R1) == 0

print("B =", B)
print("g =", g)
print("B/g =", sp.factor(B/g))
print("omega =", omega)
print("m0 =", m0)
print("Z =", Z)
print("R1 =", R1)
print("J1 =", J1)
print("N1 =", N1)
print("exact normalization checks passed")
