#!/usr/bin/env python3
"""Exact symbolic gate for Assignment 005.

This script constructs a genuine one-neighbour d=3 replacement IPS with:

* boundary-complete nonempty target modes 1 and 2;
* a Metzler typed interior transfer K;
* every zero-length outgoing OO/OI inequality nonnegative;
* every long-time outgoing OI limit nonnegative;
* one outgoing row with p0<0;
* an exact interior-time negative OI numerator invisible at both endpoints.

All arithmetic is Fraction arithmetic.  The local physical semigroup has
spectrum {0,-1,-2}, so every relevant OI numerator is represented exactly as
L + A*x + B*x^2 with x=e^{-t} in [0,1].  No floating-point sign decision and no
Monte Carlo are used.
"""

from fractions import Fraction as Q


STATES = (0, 1, 2)
ACTIVE = (1, 2)
TRANSITIONS = ((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1))


# ---------------------------------------------------------------------------
# Physical one-neighbour rate table
# ---------------------------------------------------------------------------
# q[(x,y)] is the rate when the neighbour is in reference state 0.
q = {
    (0, 1): Q(0),
    (0, 2): Q(1, 4),
    (1, 0): Q(7, 4),
    (1, 2): Q(1, 4),
    (2, 0): Q(1, 4),
    (2, 1): Q(1, 2),
}

# Indicator-basis coefficients for target label 1.
h1 = {
    (0, 1): Q(0),
    (0, 2): Q(-1, 8),
    (1, 0): Q(-9, 8),
    (1, 2): Q(1),
    (2, 0): Q(-1, 8),
    (2, 1): Q(0),
}

# A benign second target mode, included so incoming target types 1 and 2 and
# outgoing records from both active source types all have positive coarse rate.
h2 = {
    (0, 1): Q(0),
    (0, 2): Q(0),
    (1, 0): Q(-1, 8),
    (1, 2): Q(0),
    (2, 0): Q(-1, 8),
    (2, 1): Q(0),
}

MODES = {1: h1, 2: h2}


def physical_rate(neighbour, transition):
    if neighbour == 0:
        return q[transition]
    return q[transition] + MODES[neighbour][transition]


# Check all 18 one-neighbour physical rates exactly.
physical_nonnegativity_checks = 0
for z in STATES:
    for tr in TRANSITIONS:
        assert physical_rate(z, tr) >= 0, (z, tr, physical_rate(z, tr))
        physical_nonnegativity_checks += 1
assert physical_nonnegativity_checks == 18


# ---------------------------------------------------------------------------
# Typed coefficients from the physical rate table
# ---------------------------------------------------------------------------
def typed_row(coeff, r):
    """Return (a_r^0,a_r^1,a_r^2) for one neighbour basis mode."""
    out = [Q(0), Q(0), Q(0)]
    c0r = coeff[(0, r)]
    out[0] = c0r
    for s in ACTIVE:
        if s != r:
            out[s] = coeff[(s, r)] - c0r
    out[r] = -c0r - sum(
        (coeff[(r, y)] for y in STATES if y != r), Q(0)
    )
    return tuple(out)


# Empty-target K reconstructed from q.
K = (
    (Q(0), Q(0), Q(0)),
    typed_row(q, 1),
    typed_row(q, 2),
)
assert K == (
    (Q(0), Q(0), Q(0)),
    (Q(0), Q(-2), Q(1, 2)),
    (Q(1, 4), Q(0), Q(-1)),
)

# Boundary completeness forces and here visibly has all off-diagonals >= 0.
metzler_checks = 0
for r in STATES:
    for s in STATES:
        if r != s:
            assert K[r][s] >= 0
            metzler_checks += 1
assert metzler_checks == 6

rows = {}
for mode, coeff in MODES.items():
    for r in ACTIVE:
        rows[(mode, r)] = typed_row(coeff, r)

assert rows[(1, 1)] == (Q(0), Q(1, 8), Q(0))
assert rows[(1, 2)] == (Q(-1, 8), Q(9, 8), Q(1, 4))
assert rows[(2, 1)] == (Q(0), Q(1, 8), Q(0))
assert rows[(2, 2)] == (Q(0), Q(0), Q(1, 8))

# Both target labels and both active source types have positive coarse hazard.
boundary_support_checks = 0
for mode in (1, 2):
    for r in ACTIVE:
        hazard = sum((abs(x) for x in rows[(mode, r)]), Q(0))
        assert hazard > 0
        boundary_support_checks += 1
assert boundary_support_checks == 4


# ---------------------------------------------------------------------------
# Exact endpoint conditions
# ---------------------------------------------------------------------------
def value_vector(p):
    p0, p1, p2 = p
    return (p0, p0 + p1, p0 + p2)


zero_length_checks = 0
for key, p in rows.items():
    p0, p1, p2 = p
    # OO zero-length terminal types 1,2.
    assert p1 >= 0
    assert p2 >= 0
    # OI zero-length incoming terminal types 1,2.
    assert p0 + p1 >= 0
    assert p0 + p2 >= 0
    zero_length_checks += 4
assert zero_length_checks == 16

# The required nontrivial row has negative cemetery/deletion coefficient.
witness_p = rows[(1, 2)]
assert witness_p[0] == Q(-1, 8) < 0
assert value_vector(witness_p) == (Q(-1, 8), Q(1), Q(1, 8))


# ---------------------------------------------------------------------------
# Exact physical semigroup: Q has spectrum {0,-1,-2}
# ---------------------------------------------------------------------------
# Projector matrices P0,P1,P2 such that exp(tQ)=P0+x P1+x^2 P2, x=e^{-t}.
P0 = (
    (Q(11, 16), Q(1, 16), Q(1, 4)),
    (Q(11, 16), Q(1, 16), Q(1, 4)),
    (Q(11, 16), Q(1, 16), Q(1, 4)),
)
P1 = (
    (Q(3, 8), Q(-1, 8), Q(-1, 4)),
    (Q(3, 8), Q(-1, 8), Q(-1, 4)),
    (Q(-9, 8), Q(3, 8), Q(3, 4)),
)
P2 = (
    (Q(-1, 16), Q(1, 16), Q(0)),
    (Q(-17, 16), Q(17, 16), Q(0)),
    (Q(7, 16), Q(-7, 16), Q(0)),
)


def mat_vec_row(row, vec):
    return sum((row[j] * vec[j] for j in STATES), Q(0))


def oi_polynomial(p, start):
    """Return (L,A,B) for p exp(tK) f_start^I = L+A*x+B*x^2."""
    g = value_vector(p)
    return (
        mat_vec_row(P0[start], g),
        mat_vec_row(P1[start], g),
        mat_vec_row(P2[start], g),
    )


def poly_value(poly, x):
    L, A, B = poly
    return L + A * x + B * x * x


def exact_quadratic_min(poly):
    """Exact minimum of L+A*x+B*x^2 on [0,1]."""
    L, A, B = poly
    candidates = [(Q(0), L), (Q(1), L + A + B)]
    if B > 0:
        xv = -A / (2 * B)
        if Q(0) < xv < Q(1):
            candidates.append((xv, poly_value(poly, xv)))
    return min(candidates, key=lambda item: item[1])


# Check every outgoing OI family.  All long-time limits are >=0; every family
# except the designated witness is nonnegative for all t.
long_time_checks = 0
alltime_nonwitness_checks = 0
polynomials = {}
for key, p in rows.items():
    for start in ACTIVE:
        poly = oi_polynomial(p, start)
        polynomials[(key, start)] = poly
        assert poly[0] >= 0  # x=0, t=infinity
        assert poly_value(poly, Q(1)) >= 0  # t=0
        long_time_checks += 1
        if not (key == (1, 2) and start == 1):
            _, minimum = exact_quadratic_min(poly)
            assert minimum >= 0, (key, start, poly, minimum)
            alltime_nonwitness_checks += 1

assert long_time_checks == 8
assert alltime_nonwitness_checks == 7

# Exact witness polynomial.
witness_poly = polynomials[((1, 2), 1)]
assert witness_poly == (Q(1, 128), Q(-13, 64), Q(153, 128))
assert poly_value(witness_poly, Q(1)) == Q(1)
assert witness_poly[0] == Q(1, 128)

# Its unique interior minimum is at x=e^{-t}=13/153.
x_star = Q(13, 153)
assert Q(0) < x_star < Q(1)
assert x_star == -witness_poly[1] / (2 * witness_poly[2])
assert poly_value(witness_poly, x_star) == Q(-1, 1224) < 0

# The other incoming terminal for the same row remains nonnegative for all t.
other_witness_poly = polynomials[((1, 2), 2)]
assert other_witness_poly == (Q(1, 128), Q(39, 64), Q(-63, 128))
_, other_min = exact_quadratic_min(other_witness_poly)
assert other_min >= 0


# ---------------------------------------------------------------------------
# OO all-time families are automatic from p1,p2>=0 and Metzler K.
# For this triangular K the active block exponential is explicit:
# row 1 active columns = (x^2, (x-x^2)/2), row 2 = (0,x).
# Check each OO polynomial exactly on x in [0,1].
# ---------------------------------------------------------------------------
def oo_polynomials(p):
    _, p1, p2 = p
    # terminal 1 and terminal 2 respectively
    return (
        (Q(0), Q(0), p1),
        (Q(0), p2 + p1 / 2, -p1 / 2),
    )


oo_checks = 0
for p in rows.values():
    for poly in oo_polynomials(p):
        _, minimum = exact_quadratic_min(poly)
        assert minimum >= 0
        oo_checks += 1
assert oo_checks == 8


# ---------------------------------------------------------------------------
# Binary suppression check
# ---------------------------------------------------------------------------
# Remove physical type 2 and target mode 2.  Then u=q01=0, w=q10=7/4.
# For target mode 1, c0(S)=h01=0 and c1(S)=h10=-9/8.
# The exact canonical binary inequalities are satisfied, with no additional
# active-retyping condition because no second active type remains.
u = q[(0, 1)]
w = q[(1, 0)]
c0S = h1[(0, 1)]
c1S = h1[(1, 0)]
assert u == Q(0)
assert w == Q(7, 4)
assert c0S == Q(0)
assert c1S == Q(-9, 8)
assert c0S + c1S <= 0
assert w * c0S >= u * c1S

# Binary typed outgoing row is exactly (c0S,-c0S-c1S).
binary_row = (c0S, -c0S - c1S)
assert binary_row == (Q(0), Q(9, 8))
assert binary_row[1] >= 0
assert sum(binary_row) >= 0
binary_checks = 8


if __name__ == "__main__":
    print("physical one-neighbour nonnegativity checks:", physical_nonnegativity_checks)
    print("Metzler off-diagonal checks:", metzler_checks)
    print("boundary-complete positive-hazard checks:", boundary_support_checks)
    print("zero-length outgoing endpoint checks:", zero_length_checks)
    print("long-time OI endpoint checks:", long_time_checks)
    print("all-time non-witness OI checks:", alltime_nonwitness_checks)
    print("OO all-time checks:", oo_checks)
    print("binary suppression checks:", binary_checks)
    print("witness polynomial (L,A,B):", witness_poly)
    print("witness x*=e^{-t*}:", x_star)
    print("witness minimum:", poly_value(witness_poly, x_star))
    print("all three-state endpoint-obstruction checks passed")
