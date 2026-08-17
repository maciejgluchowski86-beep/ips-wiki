#!/usr/bin/env python3
"""Exact finite checks for Assignment 013 Gray scalar-edge obstruction.

The verifier checks the Boolean-map classification, the eventwise scalar-splice
inequalities, the hard-point rate violations in ordinary and checkerboard
gauges, and representative attractive/repulsive sanity points.
"""
from fractions import Fraction as Q
from itertools import product


def scalar_closure(F):
    f00, f01, f10, f11 = F
    return f01 in (f00, f11) and f10 in (f00, f11)


def monotone(F):
    f00, f01, f10, f11 = F
    return f00 <= f01 <= f11 and f00 <= f10 <= f11


def flip_vector(F):
    xs = (0, 0, 1, 1)
    return tuple(int(F[k] != xs[k]) for k in range(4))


all_maps = list(product((0, 1), repeat=4))
closure_maps = [F for F in all_maps if scalar_closure(F)]
assert len(closure_maps) == 10

# Optional order-gate diagnostic from checkpoint 013a: once diagonal source-swap
# events F00=1,F11=0 are excluded, scalar closure leaves exactly the monotone
# Boolean maps. The final obstruction below does not rely on excluding them.
no_source_crossing = [F for F in closure_maps if not (F[0] == 1 and F[3] == 0)]
monotone_maps = [F for F in all_maps if monotone(F)]
assert len(monotone_maps) == 6
assert set(no_source_crossing) == set(monotone_maps)

# Load-bearing eventwise inequalities from exact extremal scalar-splice closure:
#   v11 <= v00+v10,
#   v00 <= v01+v11.
for F in closure_maps:
    v00, v01, v10, v11 = flip_vector(F)
    assert v11 <= v00 + v10
    assert v00 <= v01 + v11

# Hard point.
a = Q(1, 10000)
b = Q(1, 100)
c = Q(9999, 10000)
delta0 = 1 - c
delta1 = Q(1)
lam = (a, b, delta0, delta1)
assert delta0 == Q(1, 10000)

# Ordinary gauge violates v11 <= v00+v10 after summing event rates:
# 1 <= a+(1-c).
ordinary_rhs = a + delta0
assert ordinary_rhs == Q(1, 5000)
assert delta1 > ordinary_rhs

# Checkerboard transform. At even parity the transformed rate vector is
# (b,a,1,1-c), and v00 <= v01+v11 requires b <= a+(1-c).
# At odd parity the vector is (1-c,1,a,b), and v11 <= v00+v10 gives the same.
even = (b, a, delta1, delta0)
odd = (delta0, delta1, a, b)
checker_rhs = a + delta0
assert even[0] > even[1] + even[3]
assert odd[3] > odd[0] + odd[2]
assert checker_rhs == Q(1, 5000)
assert b == Q(1, 100)

# Ordinary/checkerboard order-gate diagnostics from 013a.
assert a <= b and not (delta1 <= delta0)
assert delta1 - delta0 == c
assert b - a == Q(99, 10000)

# Attractive representative: standard monotone decomposition is admitted.
aA, bA, cA = Q(1, 4), Q(1, 2), Q(0)
d0A, d1A = 1 - cA, Q(1)
assert aA <= bA and d1A <= d0A
assert (aA, bA - aA, d1A, d0A - d1A) == (
    Q(1, 4), Q(1, 4), Q(1), Q(0)
)
# const1=1111, OR=0111, const0=0000, AND=0001
for F in [(1,1,1,1), (0,1,1,1), (0,0,0,0), (0,0,0,1)]:
    assert scalar_closure(F)

# Repulsive representative: checkerboard transform is attractive at both
# parities and in particular passes the weaker scalar-closure rate gate.
aR, bR, cR = Q(1, 2), Q(1, 4), Q(1, 2)
d0R, d1R = 1 - cR, Q(1)
evenR = (bR, aR, d1R, d0R)
oddR = (d0R, d1R, aR, bR)
assert evenR[0] <= evenR[1] and evenR[3] <= evenR[2]
assert oddR[0] <= oddR[1] and oddR[3] <= oddR[2]
assert bR <= aR + d0R

print("ordinary scalar-closure Boolean maps:", len(closure_maps))
print("closure maps without local extremal-source crossing:", len(no_source_crossing))
print("monotone Boolean maps:", len(monotone_maps))
print("P_h ordinary scalar gate: 1 > a+(1-c) =", ordinary_rhs)
print("P_h checkerboard scalar gate: b =", b, "> a+(1-c) =", checker_rhs)
print("attractive and repulsive sanity points verified exactly")
