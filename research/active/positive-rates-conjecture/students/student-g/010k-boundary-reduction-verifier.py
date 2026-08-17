#!/usr/bin/env python3
"""Exact scalar checks for Student G Assignment-010 checkpoints 010h--010j.

This does not verify the all-depth operator identities themselves; those are
algebraic identities in L_N, P_N and resolvents.  It verifies every quoted
parameter identity and strict scalar inequality used in the reductions and in
the component-weight obstruction.
"""

import sympy as sp


a = sp.Rational(1, 1000)
b = sp.Rational(1, 10)
c = sp.Rational(9999, 10000)
B = sp.factor(b + c - a)
g = sp.factor(b - a)
omega = sp.factor(1 - c + a)
r = 1 + b
tau = sp.Rational(4, 125)

epsilon = sp.Rational(9, 10000)
g0 = g + epsilon
c0 = c - epsilon
d = sp.factor(b * (1 - c) - a)
alpha = sp.factor(-d / g)

assert B == c0 + g0
assert d == -epsilon * r
assert alpha == sp.Rational(1, 100)
assert c0 == sp.Rational(999, 1000)
assert g0 == sp.Rational(999, 10000)


def Z(x):
    return sp.factor(
        (x + 1 + B + a) / ((x + a) * (x + 1 + B) - a)
    )


Z0 = Z(omega)
assert Z0 == sp.Rational(19100, 31)

# 010i: safe absolute-value bound on the fresh r-shifted branch.
Zshift = Z(omega + r)
assert Zshift == sp.Rational(2425, 2671)
BZshift = sp.factor(B * Zshift)
assert BZshift == sp.Rational(1065933, 1068400)
assert BZshift < 1

# The unshifted scalar Y=X-epsilon defect is individually subcritical under
# the crude admissibility bound |sigma| <= 1.
epsilon_Z = sp.factor(epsilon * Z0)
assert epsilon_Z < 1

# 010h: quoted completely crude boundary-resolvent prefactor.
Cstar = sp.factor(
    epsilon + 2 * c * g0 / r * (1 + b / r)
)
assert Cstar == sp.Rational(342081, 1718750)

# 010j: component-weight obstruction.
# The dimer inequality cannot hold at or below theta=99/100.
theta0 = sp.Rational(99, 100)
dimer_lhs = sp.factor(g * theta0 + c / theta0)
dimer_rhs = sp.factor(c + g + 2 * omega)
assert dimer_lhs == sp.Rational(110801, 100000)
assert dimer_rhs == sp.Rational(11011, 10000)
assert dimer_lhs > dimer_rhs

# The long-block constraint gives L_*=(c-alpha)/(c+omega).
Lstar = sp.factor((c - alpha) / (c + omega))
assert Lstar == sp.Rational(9899, 10010)
assert Lstar > sp.Rational(98, 100)

# F(theta)=g theta + alpha L_*/theta^2 is increasing on theta>=99/100.
# It is enough to bound the negative derivative contribution using L_*<1.
derivative_bad_upper = sp.factor(
    2 * alpha / theta0**3
)
assert derivative_bad_upper < g

# At theta=99/100 even the weaker L_*>98/100 lower bound violates the
# isolated-particle necessary condition.
isolated_lower = sp.factor(
    g * theta0 + alpha * sp.Rational(98, 100) / theta0**2
)
isolated_rhs = sp.factor(g + omega)
assert isolated_lower > isolated_rhs

print("B * Z_{omega+r} =", BZshift, "=", sp.N(BZshift, 20))
print("epsilon * Z =", epsilon_Z, "=", sp.N(epsilon_Z, 20))
print("C_* =", Cstar, "=", sp.N(Cstar, 20))
print("dimer lhs at theta=99/100 =", dimer_lhs)
print("dimer rhs =", dimer_rhs)
print("L_* =", Lstar)
print("isolated lower at theta=99/100 =", sp.N(isolated_lower, 20))
print("isolated rhs =", isolated_rhs)
print("exact 010h--010j scalar checks passed")
