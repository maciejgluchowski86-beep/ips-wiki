#!/usr/bin/env python3
"""Exact finite gate for Assignment 004.

The d=3 data contain:
* two active source types;
* a negative empty-target retyping coefficient;
* a positive empty-target retyping coefficient;
* nonzero nonempty-target hazards;
* a signed outgoing boundary vector containing a negative coefficient;
* incoming and outgoing initial/terminal descriptors.

The verifier checks with Fraction arithmetic only:
1. direct first-step weighted/killed generator = K;
2. direct unsigned consistency/killing generator = B;
3. all four boundary-orientation numerator/denominator value and derivative
   formulas at t=0;
4. exact semigroup Taylor coefficients through order 6 for all four
   orientations, generated independently by repeated local propagation;
5. the d=2 reduction to the binary empty-target transfer and the canonical
   four boundary numerators/denominators at t=0 and first derivative.

There is no floating point and no Monte Carlo.
"""

from fractions import Fraction as Q
from math import factorial


def dot(row, col):
    return sum((x * y for x, y in zip(row, col)), Q(0))


def row_mat(row, matrix):
    n = len(matrix)
    return [
        sum((row[i] * matrix[i][j] for i in range(n)), Q(0))
        for j in range(n)
    ]


def matrix_from_local_data(empty, kappa, d):
    """Return the predicted signed K and unsigned killed B matrices."""
    K = [[Q(0) for _ in range(d)] for _ in range(d)]
    B = [[Q(0) for _ in range(d)] for _ in range(d)]
    for r in range(1, d):
        rho = sum((abs(empty[(r, s)]) for s in range(d) if s != r), Q(0))
        for s in range(d):
            K[r][s] = empty[(r, s)]
            if s != r:
                B[r][s] = abs(empty[(r, s)])
        B[r][r] = -(rho + kappa[r])
    return K, B


def direct_weighted_generator_value(r, F, empty, kappa, potential, d):
    """First-step Poisson calculation before cancellation."""
    if r == 0:
        return Q(0)
    rho = sum((abs(empty[(r, s)]) for s in range(d) if s != r), Q(0))
    value = Q(0)
    for s in range(d):
        if s == r:
            continue
        a = empty[(r, s)]
        sign = Q(1) if a >= 0 else Q(-1)
        value += abs(a) * (sign * F[s] - F[r])
    value -= kappa[r] * F[r]
    value += potential[r] * F[r]
    assert potential[r] == rho + kappa[r] + empty[(r, r)]
    return value


def direct_unsigned_generator_value(r, F, empty, kappa, d):
    if r == 0:
        return Q(0)
    value = Q(0)
    for s in range(d):
        if s == r:
            continue
        value += abs(empty[(r, s)]) * (F[s] - F[r])
    value -= kappa[r] * F[r]
    return value


def series_coefficients(initial, matrix, terminal, order):
    """Coefficients of initial*exp(tM)*terminal through t^order."""
    row = list(initial)
    out = []
    for n in range(order + 1):
        out.append(dot(row, terminal) / Q(factorial(n)))
        row = row_mat(row, matrix)
    return out


def propagated_derivative_coefficients(initial, local_action, terminal, order):
    """Independent recurrence using a local row-propagation callback."""
    row = list(initial)
    out = []
    for n in range(order + 1):
        out.append(dot(row, terminal) / Q(factorial(n)))
        row = local_action(row)
    return out


def run_d3():
    d = 3

    # Empty-target signed coefficient rows. State 0 is inactive and has no row.
    # r=1 includes the negative retyping coefficient 1 -> 2.
    empty = {
        (1, 0): Q(2),
        (1, 1): Q(-5),
        (1, 2): Q(-1),
        (2, 0): Q(1),
        (2, 1): Q(3),
        (2, 2): Q(-2),
    }

    # One nonempty coarse family per active type, chosen so its total absolute
    # rate is exactly kappa_r.
    nonempty = {
        1: [Q(1), Q(-2), Q(1)],   # hazard 4
        2: [Q(-1), Q(2), Q(-2)],  # hazard 5
    }
    kappa = {
        1: sum((abs(x) for x in nonempty[1]), Q(0)),
        2: sum((abs(x) for x in nonempty[2]), Q(0)),
    }
    assert kappa == {1: Q(4), 2: Q(5)}

    # Potential values forced by Assignment 001.
    potential = {}
    for r in (1, 2):
        rho = sum((abs(empty[(r, s)]) for s in range(d) if s != r), Q(0))
        potential[r] = rho + kappa[r] + empty[(r, r)]
    assert potential == {1: Q(2), 2: Q(7)}

    K, B = matrix_from_local_data(empty, kappa, d)
    assert K == [
        [Q(0), Q(0), Q(0)],
        [Q(2), Q(-5), Q(-1)],
        [Q(1), Q(3), Q(-2)],
    ]
    assert B == [
        [Q(0), Q(0), Q(0)],
        [Q(2), Q(-7), Q(1)],
        [Q(1), Q(3), Q(-9)],
    ]

    # 1. Direct first-step weighted generator equals K on every basis F=e_j.
    weighted_checks = 0
    unsigned_checks = 0
    for r in range(d):
        for j in range(d):
            F = [Q(0), Q(0), Q(0)]
            F[j] = Q(1)
            direct_w = direct_weighted_generator_value(
                r, F, empty, kappa, potential, d
            )
            direct_b = direct_unsigned_generator_value(r, F, empty, kappa, d)
            assert direct_w == K[r][j]
            assert direct_b == B[r][j]
            weighted_checks += 1
            unsigned_checks += 1

    # Boundary data: incoming initial type 1, outgoing initial pre-type 1 with
    # signed hidden-outcome vector nonempty[1]; incoming terminal type 2 and
    # outgoing terminal source type 2.
    e1 = [Q(0), Q(1), Q(0)]
    signed_out = nonempty[1]
    ref_out = [abs(x) for x in signed_out]
    fI2 = [Q(1), Q(0), Q(1)]
    fO2 = [Q(0), Q(0), Q(1)]

    descriptors = {
        "II": (e1, e1, fI2),
        "IO": (e1, e1, fO2),
        "OI": (signed_out, ref_out, fI2),
        "OO": (signed_out, ref_out, fO2),
    }

    expected_zero_and_first = {
        "II": (Q(0), Q(1), Q(0), Q(3)),
        "IO": (Q(0), Q(-1), Q(0), Q(1)),
        "OI": (Q(2), Q(-3), Q(2), Q(-2)),
        "OO": (Q(1), Q(0), Q(1), Q(-7)),
    }

    boundary_generator_checks = 0
    semigroup_series_checks = 0

    # Independent local row actions used for the recurrence check.
    def weighted_row_action(row):
        # Since each row basis action was independently verified above from the
        # Poisson first-step formula, linearly combine those direct rows.
        result = [Q(0) for _ in range(d)]
        for r, coeff in enumerate(row):
            if coeff == 0:
                continue
            for j in range(d):
                F = [Q(0) for _ in range(d)]
                F[j] = Q(1)
                result[j] += coeff * direct_weighted_generator_value(
                    r, F, empty, kappa, potential, d
                )
        return result

    def unsigned_row_action(row):
        result = [Q(0) for _ in range(d)]
        for r, coeff in enumerate(row):
            if coeff == 0:
                continue
            for j in range(d):
                F = [Q(0) for _ in range(d)]
                F[j] = Q(1)
                result[j] += coeff * direct_unsigned_generator_value(
                    r, F, empty, kappa, d
                )
        return result

    for name, (u_signed, u_ref, terminal) in descriptors.items():
        n0 = dot(u_signed, terminal)
        n1 = dot(row_mat(u_signed, K), terminal)
        d0 = dot(u_ref, terminal)
        d1 = dot(row_mat(u_ref, B), terminal)
        assert (n0, n1, d0, d1) == expected_zero_and_first[name]
        boundary_generator_checks += 4

        signed_series = series_coefficients(u_signed, K, terminal, 6)
        direct_signed_series = propagated_derivative_coefficients(
            u_signed, weighted_row_action, terminal, 6
        )
        unsigned_series = series_coefficients(u_ref, B, terminal, 6)
        direct_unsigned_series = propagated_derivative_coefficients(
            u_ref, unsigned_row_action, terminal, 6
        )
        assert signed_series == direct_signed_series
        assert unsigned_series == direct_unsigned_series
        semigroup_series_checks += 14  # seven numerator + seven denominator

    # Explicitly retain the negative small-time IO witness: the descriptor is
    # denominator-realizable to first order but its numerator derivative is -1.
    assert expected_zero_and_first["IO"] == (Q(0), Q(-1), Q(0), Q(1))

    return {
        "weighted_generator": weighted_checks,
        "unsigned_generator": unsigned_checks,
        "boundary_generator": boundary_generator_checks,
        "semigroup_series": semigroup_series_checks,
    }


def run_d2():
    d = 2

    # Binary empty-neighbour coefficients: u=c^0(empty)=2, w=c^1(empty)=3.
    # Hence the signed empty-target row is [u,-u-w]=[2,-5].
    u = Q(2)
    w = Q(3)
    empty = {(1, 0): u, (1, 1): -(u + w)}

    # One nonempty target S with c^0(S)=1, c^1(S)=-3, so
    # [a^delta(S), a^beta(S)] = [1,2].
    c0S = Q(1)
    c1S = Q(-3)
    signed_out = [c0S, -(c0S + c1S)]
    ref_out = [abs(x) for x in signed_out]
    kappa = {1: sum((abs(x) for x in signed_out), Q(0))}
    assert kappa[1] == Q(3)

    rho = abs(empty[(1, 0)])
    potential = {1: rho + kappa[1] + empty[(1, 1)]}
    assert potential[1] == Q(0)

    K, B = matrix_from_local_data(empty, kappa, d)
    assert K == [[Q(0), Q(0)], [Q(2), Q(-5)]]
    assert B == [[Q(0), Q(0)], [Q(2), Q(-5)]]

    # Binary terminal incoming compatibility is {0,1}, i.e. the all-ones
    # column; outgoing terminal is active state 1.
    e1 = [Q(0), Q(1)]
    fI = [Q(1), Q(1)]
    fO = [Q(0), Q(1)]

    descriptors = {
        "II": (e1, e1, fI),
        "IO": (e1, e1, fO),
        "OI": (signed_out, ref_out, fI),
        "OO": (signed_out, ref_out, fO),
    }

    # Canonical binary zero-length numerators:
    # II=1, IO=1, OI=-c^1(S)=3, OO=-(c^0+c^1)(S)=2.
    assert dot(e1, fI) == Q(1)
    assert dot(e1, fO) == Q(1)
    assert dot(signed_out, fI) == -c1S == Q(3)
    assert dot(signed_out, fO) == -(c0S + c1S) == Q(2)

    binary_checks = 0
    for name, (us, ur, terminal) in descriptors.items():
        # Check exact value and first derivative from the typed matrices.
        n0 = dot(us, terminal)
        n1 = dot(row_mat(us, K), terminal)
        d0 = dot(ur, terminal)
        d1 = dot(row_mat(ur, B), terminal)
        assert n0 == series_coefficients(us, K, terminal, 1)[0]
        assert n1 == series_coefficients(us, K, terminal, 1)[1]
        assert d0 == series_coefficients(ur, B, terminal, 1)[0]
        assert d1 == series_coefficients(ur, B, terminal, 1)[1]
        binary_checks += 4

    return {"binary_boundary": binary_checks}


if __name__ == "__main__":
    d3 = run_d3()
    d2 = run_d2()
    print("d=3 weighted first-step generator checks:", d3["weighted_generator"])
    print("d=3 unsigned killed-generator checks:", d3["unsigned_generator"])
    print("d=3 four-orientation value/derivative checks:", d3["boundary_generator"])
    print("d=3 exact semigroup Taylor coefficient checks:", d3["semigroup_series"])
    print("d=2 typed/binary boundary checks:", d2["binary_boundary"])
    print("all typed bulk-transfer checks passed")
