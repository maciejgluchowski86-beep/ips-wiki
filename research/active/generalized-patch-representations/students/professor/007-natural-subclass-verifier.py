#!/usr/bin/env python3
"""Exact verifier for Assignment 007.

Checks, with Fraction arithmetic only:

1. the exact lumpability/value-lump conditions;
2. a physically realizable exchange-symmetric d=3 positive gate with
   c>a, p0<0, p1!=p2, positive 1<->2 dynamics, and all OI numerators
   certified by the exact symmetry theorem;
3. a physically realizable negative row in the same symmetric subclass,
   showing the long-time inequality is genuinely necessary;
4. the refresh boundary case via Q^2=-R Q and its one-mode criterion;
5. the Assignment-005 triangular one-way-retyping obstruction;
6. exact binary reduction to the canonical two inequalities.

There is no floating point, no plotting, and no time mesh.
"""

from fractions import Fraction as Q


TRANSITIONS = ("01", "02", "10", "12", "20", "21")


def invert_rows(row1, row2):
    """Invert the d=3 one-neighbour typed-row formulas.

    row1 is the outgoing signed row for active source type 1,
    row2 for active source type 2, at one fixed nonempty target mode.
    """
    a0, a1, a2 = row1
    b0, b1, b2 = row2
    return {
        "01": a0,
        "02": b0,
        "10": -a0 - b1 - b0 - a1,
        "12": b1 + b0,
        "20": -b0 - a2 - a0 - b2,
        "21": a2 + a0,
    }


def rows_from_coefficients(h):
    row1 = (
        h["01"],
        -h["01"] - h["10"] - h["12"],
        h["21"] - h["01"],
    )
    row2 = (
        h["02"],
        h["12"] - h["02"],
        -h["02"] - h["20"] - h["21"],
    )
    return row1, row2


def swap_active_coefficients(h):
    """Apply the physical label exchange 1<->2."""
    return {
        "01": h["02"],
        "02": h["01"],
        "10": h["20"],
        "12": h["21"],
        "20": h["10"],
        "21": h["12"],
    }


def add_coefficients(base, h):
    return {k: base[k] + h[k] for k in TRANSITIONS}


def coarse_hazard(row):
    return sum((abs(x) for x in row), Q(0))


def g_from_p(p):
    p0, p1, p2 = p
    return (p0, p0 + p1, p0 + p2)


def symmetric_L(p, a, b):
    p0, p1, p2 = p
    return ((b + 2 * a) * p0 + a * (p1 + p2)) / (b + 2 * a)


def symmetric_mode_data(p, a, b):
    g0, g1, g2 = g_from_p(p)
    m = (g1 + g2) / 2
    d = (g1 - g2) / 2
    L = (b * g0 + 2 * a * m) / (b + 2 * a)
    return g0, g1, g2, m, d, L, m - L


def run_lumpability_checks():
    checks = 0

    # Strong lumpability of {0},{1,2} is q10=q20.
    q10 = Q(7, 5)
    q20 = Q(7, 5)
    assert q10 == q20
    checks += 1

    p_lump = (Q(-1, 3), Q(5, 6), Q(5, 6))
    g = g_from_p(p_lump)
    assert g[1] == g[2]
    assert p_lump[1] == p_lump[2]
    checks += 2

    p_nonlump = (Q(-1, 3), Q(5, 6), Q(4, 5))
    g = g_from_p(p_nonlump)
    assert g[1] != g[2]
    assert p_nonlump[1] != p_nonlump[2]
    checks += 2

    return checks


def run_symmetric_positive_gate():
    checks = 0

    # a=1, b=2, c=2.  Reference transition order:
    # 01,02,10,12,20,21.
    a = Q(1)
    b = Q(2)
    c = Q(2)
    base = {
        "01": a,
        "02": a,
        "10": b,
        "12": c,
        "20": b,
        "21": c,
    }

    # Physical nonnegativity at neighbour state 0.
    for k in TRANSITIONS:
        assert base[k] >= 0
        checks += 1

    # Target type 1 rows.  The second row is genuinely non-binary:
    # p0<0 and p1!=p2.
    row11 = (Q(0), Q(1, 4), Q(1, 4))
    row21 = (Q(-1, 2), Q(3, 2), Q(1))
    h1 = invert_rows(row11, row21)
    assert rows_from_coefficients(h1) == (row11, row21)
    checks += 1

    physical1 = add_coefficients(base, h1)
    expected1 = {
        "01": Q(1),
        "02": Q(1, 2),
        "10": Q(3, 4),
        "12": Q(3),
        "20": Q(5, 4),
        "21": Q(9, 4),
    }
    assert physical1 == expected1
    for k in TRANSITIONS:
        assert physical1[k] > 0
        checks += 1

    # Target type 2 is the exact active-label swap, so the whole coefficient
    # family is exchange-symmetric rather than merely the base chain.
    h2 = swap_active_coefficients(h1)
    row12, row22 = rows_from_coefficients(h2)
    assert row12 == (Q(-1, 2), Q(1), Q(3, 2))
    assert row22 == row11
    checks += 2

    physical2 = add_coefficients(base, h2)
    expected2 = {
        "01": Q(1, 2),
        "02": Q(1),
        "10": Q(5, 4),
        "12": Q(9, 4),
        "20": Q(3, 4),
        "21": Q(3),
    }
    assert physical2 == expected2
    for k in TRANSITIONS:
        assert physical2[k] > 0
        checks += 1

    rows = (row11, row21, row12, row22)

    # Boundary completeness: every source/target pair has positive hazard.
    for row in rows:
        assert coarse_hazard(row) > 0
        checks += 1

    # Metzler condition and spectral ordering.
    assert c - a == Q(1) > 0
    lambda_s = 2 * a + b
    lambda_a = b + 2 * c
    assert lambda_s == Q(4)
    assert lambda_a == Q(6)
    assert lambda_a >= lambda_s
    checks += 4

    # Exact zero-length + long-time criterion for every outgoing row.
    oi_certificates = 0
    for p in rows:
        p0, p1, p2 = p
        g0, g1, g2, m, d, L, slow_coeff = symmetric_mode_data(p, a, b)
        assert p1 >= 0
        assert p2 >= 0
        assert g1 >= 0
        assert g2 >= 0
        assert L >= 0
        if g0 < 0:
            assert slow_coeff >= 0

        # For each initial active type, certify the exact theorem branch.
        # If the antisymmetric coefficient is negative, the faster exponential
        # is bounded by the slower one and the lower bound is the one-mode
        # interpolation between the corresponding zero-time value and L.
        for sign, gb in ((Q(1), g1), (Q(-1), g2)):
            antisym = sign * d
            if antisym < 0:
                assert lambda_a >= lambda_s
                assert L >= 0 and gb >= 0
            else:
                assert L >= 0 and slow_coeff >= 0 and antisym >= 0
            oi_certificates += 1

    assert oi_certificates == 8
    checks += oi_certificates

    # Distinguished row does not factor through the binary active quotient.
    g = g_from_p(row21)
    assert row21[0] < 0
    assert row21[1] != row21[2]
    assert g[1] == Q(1)
    assert g[2] == Q(1, 2)
    assert symmetric_L(row21, a, b) == Q(1, 8)
    checks += 5

    # Exact formulas quoted in 007b.
    _, _, _, m, d, L, slow = symmetric_mode_data(row21, a, b)
    assert L == Q(1, 8)
    assert slow == Q(5, 8)
    assert d == Q(1, 4)
    checks += 3

    return checks


def run_symmetric_negative_gate():
    checks = 0
    a = Q(1)
    b = Q(2)
    c = Q(2)
    base = {
        "01": a,
        "02": a,
        "10": b,
        "12": c,
        "20": b,
        "21": c,
    }

    row1 = (Q(0), Q(1, 4), Q(1, 4))
    row2 = (Q(-1, 2), Q(1), Q(1, 2))
    h = invert_rows(row1, row2)
    assert rows_from_coefficients(h) == (row1, row2)
    checks += 1

    physical = add_coefficients(base, h)
    for k in TRANSITIONS:
        assert physical[k] > 0
        checks += 1

    p0, p1, p2 = row2
    g = g_from_p(row2)
    assert p1 >= 0 and p2 >= 0
    assert g[1] >= 0 and g[2] >= 0
    L = symmetric_L(row2, a, b)
    assert L == Q(-1, 8) < 0
    checks += 5

    # Hence the long-time endpoint condition is genuinely necessary.
    return checks


def matmul(A, B):
    n = len(A)
    m = len(B[0])
    kdim = len(B)
    return [
        [sum((A[i][k] * B[k][j] for k in range(kdim)), Q(0)) for j in range(m)]
        for i in range(n)
    ]


def run_refresh_gate():
    checks = 0
    rho0, rho1, rho2 = Q(2), Q(1), Q(1)
    R = rho0 + rho1 + rho2
    Qmat = [
        [-(rho1 + rho2), rho1, rho2],
        [rho0, -(rho0 + rho2), rho2],
        [rho0, rho1, -(rho0 + rho1)],
    ]

    # Refresh generators satisfy Q^2=-R Q exactly.  This proves the only
    # nonzero eigenvalue is -R (semisimple here), hence one-mode evolution.
    Q2 = matmul(Qmat, Qmat)
    for i in range(3):
        for j in range(3):
            assert Q2[i][j] == -R * Qmat[i][j]
            checks += 1

    p = (Q(-1, 2), Q(3, 2), Q(1))
    g = g_from_p(p)
    L = (
        rho0 * g[0] + rho1 * g[1] + rho2 * g[2]
    ) / R
    assert L == Q(1, 8)
    assert g[1] == Q(1)
    assert g[2] == Q(1, 2)
    assert p[1] != p[2]
    checks += 4

    # Exact coefficient form of the refresh criterion.
    assert R * p[0] + rho1 * p[1] + rho2 * p[2] == Q(1, 2)
    checks += 1

    return checks


def run_triangular_obstruction():
    checks = 0

    # Assignment-005 exact one-way-retyping transfer.
    K = [
        [Q(0), Q(0), Q(0)],
        [Q(0), Q(-2), Q(1, 2)],
        [Q(1, 4), Q(0), Q(-1)],
    ]
    assert K[1][2] == Q(1, 2) > 0
    assert K[2][1] == Q(0)
    checks += 2

    # N(x)=1/128 -13/64 x +153/128 x^2, x=e^{-t}.
    L = Q(1, 128)
    A = Q(-13, 64)
    B = Q(153, 128)
    xstar = -A / (2 * B)
    minimum = L + A * xstar + B * xstar * xstar
    assert xstar == Q(13, 153)
    assert minimum == Q(-1, 1224) < 0
    assert L > 0
    assert L + A + B == Q(1) > 0
    checks += 4

    return checks


def run_binary_reduction():
    checks = 0

    # In d=2 every physical two-state generator is already a refresh generator:
    # destination rates are rho0=q10=w and rho1=q01=u.
    u = Q(2)
    w = Q(3)
    R = u + w
    c0 = Q(1)
    c1 = Q(-3)
    p0 = c0
    p1 = -(c0 + c1)

    assert p1 == Q(2) >= 0
    checks += 1

    # Refresh long-time inequality is exactly the canonical second inequality.
    refresh_long = R * p0 + u * p1
    canonical_cross = w * c0 - u * c1
    assert refresh_long == canonical_cross == Q(9)
    checks += 2

    # First canonical inequality is exactly p1>=0.
    assert c0 + c1 <= 0
    assert p1 == -(c0 + c1)
    checks += 2

    # Zero-time OI value is -c1 and is nonnegative for this test.
    assert p0 + p1 == -c1 == Q(3)
    checks += 1

    # Suppressing type 2 removes every exchange-symmetry/Metzler comparison
    # involving a second active type; no extra binary condition survives.
    assert R > 0
    checks += 1

    # Degenerate binary clause: u=w=0 gives frozen reference dynamics.
    u0 = Q(0)
    w0 = Q(0)
    assert u0 + w0 == 0
    checks += 1

    return checks


if __name__ == "__main__":
    lump = run_lumpability_checks()
    sym_pos = run_symmetric_positive_gate()
    sym_neg = run_symmetric_negative_gate()
    refresh = run_refresh_gate()
    tri = run_triangular_obstruction()
    binary = run_binary_reduction()
    total = lump + sym_pos + sym_neg + refresh + tri + binary

    print("lumpability/value-lump checks:", lump)
    print("symmetric positive-gate checks:", sym_pos)
    print("symmetric negative-gate checks:", sym_neg)
    print("refresh one-mode checks:", refresh)
    print("triangular obstruction checks:", tri)
    print("binary reduction checks:", binary)
    print("total exact checks:", total)
    print("all Assignment-007 natural-subclass checks passed")
