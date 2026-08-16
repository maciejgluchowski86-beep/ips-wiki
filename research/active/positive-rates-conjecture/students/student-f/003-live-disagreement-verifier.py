"""Closed-form checks for Student F assignment 003.

No simulation is used.  The script checks:

1. the exact rightmost-source child-before-death formulas;
2. the pointwise local coupling inequality on rational residual samples;
3. the genuine residual near-East path a=e^2, b=e, c=1-e^2 and the
   lower bound showing that a perfect no-11/all-zero environment can still
   transmit a live disagreement with probability tending to one.
"""

from fractions import Fraction
from math import exp


PAIR_STATES = ((0, 0), (1, 1), (0, 1), (1, 0))


def rate(x, y, a, b, c):
    if (x, y) == (0, 0):
        return a
    if (x, y) == (0, 1):
        return b
    if (x, y) == (1, 0):
        return c
    return Fraction(0)


def local_disagreement_probability(si, sr, a, b, c):
    x, xt = PAIR_STATES[si]
    y, yt = PAIR_STATES[sr]
    return abs(rate(x, y, a, b, c) - rate(xt, yt, a, b, c))


def D(pair_state):
    x, xt = PAIR_STATES[pair_state]
    return int(x != xt)


def J(si, sr):
    """High-risk birth state: source site agreed 1, right site disagrees."""
    x, xt = PAIR_STATES[si]
    return int(x == xt == 1 and D(sr) == 1)


def check_pointwise_bridge(a, b, c):
    d = b - a
    for si in range(4):
        for sr in range(4):
            delta = local_disagreement_probability(si, sr, a, b, c)
            rhs = (c - a) * D(si) + d * D(sr) + (c - d) * J(si, sr)
            assert delta <= rhs, (si, sr, delta, rhs)


def source_formulas(a, b, c):
    d = b - a
    q = 1 - c + a
    determinant = (b + q) * (1 + q) - a * (1 - c)
    h0 = (d * (1 + q) + a * c) / determinant
    h1 = (c * (b + q) + (1 - c) * d) / determinant
    gap0 = 1 - h0
    gap1 = 1 - h1
    assert gap0 == q * (a + q + 1) / determinant
    assert gap1 == q * (d + 2 * q) / determinant
    assert h1 - h0 == q * (c - d) / determinant
    return d, q, determinant, h0, h1, gap1


# Strict residual sample used in Assignment 002 as well.
a = Fraction(1, 10)
b = Fraction(3, 10)
c = Fraction(4, 5)
assert 0 < a < b
assert Fraction(1, 2) <= c < 1
assert c >= a + b
# b > sqrt(2)(1-c): square both positive sides.
assert b * b > 2 * (1 - c) * (1 - c)

check_pointwise_bridge(a, b, c)
d, q, determinant, h0, h1, delta = source_formulas(a, b, c)
assert h0 == Fraction(17, 38)
assert h1 == Fraction(13, 19)
assert delta == Fraction(6, 19)

T = 2.0
delta_T = float(q / (q + c)) * (1.0 - exp(-float(q + c) * T))
assert delta_T > 0

print("strict residual sample")
print(f"d={float(d):.12g}, q={float(q):.12g}")
print(f"h0={float(h0):.12g}")
print(f"h1={float(h1):.12g}")
print(f"childless gap delta={float(delta):.12g}")
print(f"finite-slab gap delta_T(T=2)={delta_T:.12g}")


# Exhaustive rational grid of residual samples for the local bridge.
for den in (10, 20):
    for ai in range(1, den):
        for bi in range(ai + 1, den):
            for ci in range((den + 1) // 2, den):
                aa = Fraction(ai, den)
                bb = Fraction(bi, den)
                cc = Fraction(ci, den)
                if cc < aa + bb:
                    continue
                if bb * bb < 2 * (1 - cc) * (1 - cc):
                    continue
                check_pointwise_bridge(aa, bb, cc)
                _, qq, _, hh0, hh1, gg = source_formulas(aa, bb, cc)
                assert qq > 0
                assert 0 <= hh0 <= hh1 < 1
                assert gg > 0


# Genuine residual near-East path: a=e^2, b=e, c=1-e^2.
e = Fraction(1, 100)
aa = e * e
bb = e
cc = 1 - e * e
assert 0 < aa < bb
assert Fraction(1, 2) <= cc < 1
assert cc >= aa + bb
assert bb * bb >= 2 * (1 - cc) * (1 - cc)

dd, qq, _, hh0, hh1, gg = source_formulas(aa, bb, cc)

# Starting from an all-zero common environment except for one off-diagonal
# source, a child birth at the left neighbour has rate d.  Before that birth,
# count as competing failures: source death q, a common 0->1 update at the
# child site (rate a), and a common 0->1 update at the source's right neighbour
# (rate a).  Poisson splitting gives the exact lower bound below.
hard_core_transmission_lower_bound = dd / (dd + qq + 2 * aa)
assert hard_core_transmission_lower_bound == (1 - e) / (1 + 3 * e)

print("near-East hard-core diagnostic")
print(f"epsilon={float(e):.12g}")
print(f"h0={float(hh0):.12g}")
print(f"h1={float(hh1):.12g}")
print(f"uniform childless gap={float(gg):.12g}")
print(
    "hard-core first-transmission lower bound="
    f"{float(hard_core_transmission_lower_bound):.12g}"
)
