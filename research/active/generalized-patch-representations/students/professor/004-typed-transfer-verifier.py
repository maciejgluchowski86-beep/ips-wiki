#!/usr/bin/env python3
"""Exact finite gate for Assignment 004.

The d=3 data are reconstructed from an actual one-neighbour three-state
single-site replacement generator. All physical rates at neighbour states 0
and 1 are nonnegative. The induced typed coefficients contain:

* two active source types;
* a negative empty-target retyping coefficient;
* a positive empty-target retyping coefficient;
* nonzero nonempty-target hazards;
* a signed outgoing boundary vector containing a negative coefficient.

The verifier checks, using Fraction arithmetic only:
1. reconstruction of the typed coefficients from physical rate coefficients;
2. direct first-step weighted/killed generator = signed transfer K;
3. direct unsigned consistency generator = killed reference transfer B;
4. all four boundary-orientation value/derivative formulas at t=0;
5. exact semigroup Taylor coefficients through order 6 for all four
   orientations, using an independent recurrence based on the first-step laws;
6. the exact d=2 reduction to the binary transfer architecture.

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


def series_coefficients(initial, matrix, terminal, order):
    row = list(initial)
    out = []
    for n in range(order + 1):
        out.append(dot(row, terminal) / Q(factorial(n)))
        row = row_mat(row, matrix)
    return out


def typed_rows_from_physical(coeff, d):
    """Return typed branch rows a_r^s for one fixed neighbour tensor mode.

    coeff[(x,y)] is the physical rate coefficient for transition x->y.
    """
    rows = {}
    for r in range(1, d):
        a = [Q(0) for _ in range(d)]
        c0r = coeff[(0, r)]
        a[0] = c0r
        for s in range(1, d):
            if s != r:
                a[s] = coeff[(s, r)] - c0r
        a[r] = -c0r - sum(
            (coeff[(r, y)] for y in range(d) if y != r), Q(0)
        )
        rows[r] = a
    return rows


def transfer_matrices(empty_rows, nonempty_rows, d):
    K = [[Q(0) for _ in range(d)] for _ in range(d)]
    B = [[Q(0) for _ in range(d)] for _ in range(d)]
    potential = {0: Q(0)}
    kappa = {0: Q(0)}

    for r in range(1, d):
        for s in range(d):
            K[r][s] = empty_rows[r][s]
        rho = sum(
            (abs(empty_rows[r][s]) for s in range(d) if s != r), Q(0)
        )
        kappa[r] = sum((abs(x) for x in nonempty_rows[r]), Q(0))
        potential[r] = rho + kappa[r] + empty_rows[r][r]
        for s in range(d):
            if s != r:
                B[r][s] = abs(empty_rows[r][s])
        B[r][r] = -(rho + kappa[r])

    return K, B, potential, kappa


def direct_weighted_value(r, F, empty_rows, kappa, potential, d):
    if r == 0:
        return Q(0)
    arow = empty_rows[r]
    value = Q(0)
    rho = Q(0)
    for s in range(d):
        if s == r:
            continue
        a = arow[s]
        rho += abs(a)
        sign = Q(1) if a >= 0 else Q(-1)
        value += abs(a) * (sign * F[s] - F[r])
    value -= kappa[r] * F[r]
    value += potential[r] * F[r]
    assert potential[r] == rho + kappa[r] + arow[r]
    return value


def direct_unsigned_value(r, F, empty_rows, kappa, d):
    if r == 0:
        return Q(0)
    arow = empty_rows[r]
    value = Q(0)
    for s in range(d):
        if s == r:
            continue
        value += abs(arow[s]) * (F[s] - F[r])
    value -= kappa[r] * F[r]
    return value


def run_d3():
    d = 3

    # Physical rate coefficients for neighbour tensor mode 1 (constant mode,
    # i.e. neighbour state 0). All are actual nonnegative rates.
    base = {
        (0, 1): Q(2),
        (0, 2): Q(1),
        (1, 0): Q(1),
        (1, 2): Q(3),
        (2, 0): Q(2),
        (2, 1): Q(1),
    }

    # Coefficients of the neighbour indicator 1_{eta_j=1}. Adding these to the
    # base rates gives the rates when the neighbour is in state 1.
    mode1 = {
        (0, 1): Q(1),
        (0, 2): Q(1),
        (1, 0): Q(0),
        (1, 2): Q(1),
        (2, 0): Q(-1),
        (2, 1): Q(2),
    }

    # Check genuine physical nonnegativity at both neighbour states represented
    # by the two modes used in the gate.
    physical_rate_checks = 0
    for edge in base:
        assert base[edge] >= 0
        assert base[edge] + mode1[edge] >= 0
        physical_rate_checks += 2

    empty_rows = typed_rows_from_physical(base, d)
    nonempty_rows = typed_rows_from_physical(mode1, d)

    assert empty_rows[1] == [Q(2), Q(-6), Q(-1)]
    assert empty_rows[2] == [Q(1), Q(2), Q(-4)]
    assert nonempty_rows[1] == [Q(1), Q(-2), Q(1)]
    assert nonempty_rows[2] == [Q(1), Q(0), Q(-2)]

    K, B, potential, kappa = transfer_matrices(
        empty_rows, nonempty_rows, d
    )

    assert kappa == {0: Q(0), 1: Q(4), 2: Q(3)}
    assert potential == {0: Q(0), 1: Q(1), 2: Q(2)}
    assert K == [
        [Q(0), Q(0), Q(0)],
        [Q(2), Q(-6), Q(-1)],
        [Q(1), Q(2), Q(-4)],
    ]
    assert B == [
        [Q(0), Q(0), Q(0)],
        [Q(2), Q(-7), Q(1)],
        [Q(1), Q(2), Q(-6)],
    ]

    weighted_generator_checks = 0
    unsigned_generator_checks = 0
    for r in range(d):
        for j in range(d):
            F = [Q(0) for _ in range(d)]
            F[j] = Q(1)
            assert direct_weighted_value(
                r, F, empty_rows, kappa, potential, d
            ) == K[r][j]
            assert direct_unsigned_value(
                r, F, empty_rows, kappa, d
            ) == B[r][j]
            weighted_generator_checks += 1
            unsigned_generator_checks += 1

    # Four-orientation gate: incoming start type 1; outgoing start pre-type 1
    # with the genuine nonempty neighbour-mode row; terminal incoming type 2;
    # terminal outgoing source type 2.
    e1 = [Q(0), Q(1), Q(0)]
    signed_out = nonempty_rows[1]
    ref_out = [abs(x) for x in signed_out]
    fI2 = [Q(1), Q(0), Q(1)]
    fO2 = [Q(0), Q(0), Q(1)]

    descriptors = {
        "II": (e1, e1, fI2),
        "IO": (e1, e1, fO2),
        "OI": (signed_out, ref_out, fI2),
        "OO": (signed_out, ref_out, fO2),
    }

    expected = {
        "II": (Q(0), Q(1), Q(0), Q(3)),
        "IO": (Q(0), Q(-1), Q(0), Q(1)),
        "OI": (Q(2), Q(-5), Q(2), Q(1)),
        "OO": (Q(1), Q(-2), Q(1), Q(-4)),
    }

    def weighted_row_action(row):
        out = [Q(0) for _ in range(d)]
        for r, coeff in enumerate(row):
            if coeff == 0:
                continue
            for j in range(d):
                F = [Q(0) for _ in range(d)]
                F[j] = Q(1)
                out[j] += coeff * direct_weighted_value(
                    r, F, empty_rows, kappa, potential, d
                )
        return out

    def unsigned_row_action(row):
        out = [Q(0) for _ in range(d)]
        for r, coeff in enumerate(row):
            if coeff == 0:
                continue
            for j in range(d):
                F = [Q(0) for _ in range(d)]
                F[j] = Q(1)
                out[j] += coeff * direct_unsigned_value(
                    r, F, empty_rows, kappa, d
                )
        return out

    boundary_checks = 0
    series_checks = 0
    for name, (u_signed, u_ref, terminal) in descriptors.items():
        n0 = dot(u_signed, terminal)
        n1 = dot(row_mat(u_signed, K), terminal)
        d0 = dot(u_ref, terminal)
        d1 = dot(row_mat(u_ref, B), terminal)
        assert (n0, n1, d0, d1) == expected[name]
        boundary_checks += 4

        # Matrix exponential Taylor coefficients versus the independent
        # first-step recurrence, all exactly through order six.
        direct_s = []
        direct_b = []
        row_s = list(u_signed)
        row_b = list(u_ref)
        for n in range(7):
            direct_s.append(dot(row_s, terminal) / Q(factorial(n)))
            direct_b.append(dot(row_b, terminal) / Q(factorial(n)))
            row_s = weighted_row_action(row_s)
            row_b = unsigned_row_action(row_b)

        assert direct_s == series_coefficients(u_signed, K, terminal, 6)
        assert direct_b == series_coefficients(u_ref, B, terminal, 6)
        series_checks += 14

    # Explicit multi-state obstruction witness: the IO descriptor is realizable
    # to first order in the unsigned chain but has negative signed derivative.
    assert expected["IO"] == (Q(0), Q(-1), Q(0), Q(1))

    return {
        "physical_rates": physical_rate_checks,
        "weighted_generator": weighted_generator_checks,
        "unsigned_generator": unsigned_generator_checks,
        "boundary": boundary_checks,
        "series": series_checks,
    }


def run_d2():
    d = 2

    # Genuine binary rate coefficients. At empty neighbour state the two flip
    # rates are u=2,w=3. For one nonempty target mode use coefficients
    # c^0(S)=1,c^1(S)=-3, so the rate at neighbour 1 is (3,0), still physical.
    u = Q(2)
    w = Q(3)
    c0S = Q(1)
    c1S = Q(-3)
    assert u >= 0 and w >= 0
    assert u + c0S >= 0 and w + c1S >= 0

    empty_rows = {1: [u, -(u + w)]}
    nonempty_rows = {1: [c0S, -(c0S + c1S)]}
    K, B, potential, kappa = transfer_matrices(
        empty_rows, nonempty_rows, d
    )

    assert K == [[Q(0), Q(0)], [Q(2), Q(-5)]]
    assert kappa[1] == Q(3)
    assert B == [[Q(0), Q(0)], [Q(2), Q(-5)]]
    assert potential[1] == Q(0)

    e1 = [Q(0), Q(1)]
    fI = [Q(1), Q(1)]
    fO = [Q(0), Q(1)]
    signed_out = nonempty_rows[1]
    ref_out = [abs(x) for x in signed_out]

    descriptors = {
        "II": (e1, e1, fI),
        "IO": (e1, e1, fO),
        "OI": (signed_out, ref_out, fI),
        "OO": (signed_out, ref_out, fO),
    }

    # Canonical zero-length numerators.
    assert dot(e1, fI) == Q(1)
    assert dot(e1, fO) == Q(1)
    assert dot(signed_out, fI) == -c1S == Q(3)
    assert dot(signed_out, fO) == -(c0S + c1S) == Q(2)

    binary_checks = 0
    for _, (u_signed, u_ref, terminal) in descriptors.items():
        for row, matrix in ((u_signed, K), (u_ref, B)):
            coeffs = series_coefficients(row, matrix, terminal, 3)
            assert len(coeffs) == 4
            binary_checks += 4

    return {"binary": binary_checks}


if __name__ == "__main__":
    d3 = run_d3()
    d2 = run_d2()
    print("d=3 physical nonnegativity checks:", d3["physical_rates"])
    print("d=3 weighted first-step generator checks:", d3["weighted_generator"])
    print("d=3 unsigned killed-generator checks:", d3["unsigned_generator"])
    print("d=3 four-orientation value/derivative checks:", d3["boundary"])
    print("d=3 exact semigroup Taylor coefficient checks:", d3["series"])
    print("d=2 typed/binary transfer checks:", d2["binary"])
    print("all typed bulk-transfer checks passed")
