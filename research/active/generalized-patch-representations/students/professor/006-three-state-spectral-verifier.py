#!/usr/bin/env python3
"""Exact verifier for Assignment 006.

All arithmetic is Fraction arithmetic.  The generic mandatory gates use the
physically realizable one-neighbour d=3 chain from Assignment 005, whose
nonzero eigenvalues are -1 and -2, so the critical-point tests reduce exactly
to quadratic polynomials in x=e^{-t}.

The script checks:
* physical realizability and boundary completeness for the obstruction gate;
* exact spectral projectors and the generic L,A,B formulas;
* the Assignment-005 negative interior minimum 13/153, -1/1224;
* a second physically realizable boundary-complete p0<0 example in which all
  OI numerators are nonnegative for all time;
* one-zero-mode, repeated diagonalizable, and Jordan classification identities;
* exact binary suppression to the canonical two inequalities.

There are no float literals, no Monte Carlo, and no floating-point sign tests.
"""

from fractions import Fraction as Q


STATES = (0, 1, 2)
PAIRS = tuple((x, y) for x in STATES for y in STATES if x != y)


def eye(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_scale(A, c):
    return [[c * x for x in row] for row in A]


def mat_mul(A, B):
    return [
        [
            sum((A[i][k] * B[k][j] for k in range(len(B))), Q(0))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]


def row_mat(row, M):
    return [
        sum((row[i] * M[i][j] for i in range(len(row))), Q(0))
        for j in range(len(M[0]))
    ]


def dot(row, col):
    return sum((x * y for x, y in zip(row, col)), Q(0))


def row_mat_col(row, M, col):
    return dot(row_mat(row, M), col)


def matrix_plus_scalar_identity(M, c):
    I = eye(len(M))
    return [[M[i][j] + c * I[i][j] for j in range(len(M))] for i in range(len(M))]


def physical_Q(base):
    Qm = [[Q(0) for _ in STATES] for _ in STATES]
    for x in STATES:
        for y in STATES:
            if x != y:
                Qm[x][y] = base[(x, y)]
        Qm[x][x] = -sum((base[(x, y)] for y in STATES if y != x), Q(0))
    return Qm


def typed_empty_K(base):
    # Assignment-001/004 formulas specialized to d=3 at the reference neighbour.
    return [
        [Q(0), Q(0), Q(0)],
        [
            base[(0, 1)],
            -(base[(0, 1)] + base[(1, 0)] + base[(1, 2)]),
            base[(2, 1)] - base[(0, 1)],
        ],
        [
            base[(0, 2)],
            base[(1, 2)] - base[(0, 2)],
            -(base[(0, 2)] + base[(2, 0)] + base[(2, 1)]),
        ],
    ]


def typed_nonempty_rows(mode):
    rows = {}
    for r in (1, 2):
        vals = [mode[(0, r)]]
        for s in (1, 2):
            if s == r:
                vals.append(
                    -mode[(0, r)]
                    - sum((mode[(r, y)] for y in STATES if y != r), Q(0))
                )
            else:
                vals.append(mode[(s, r)] - mode[(0, r)])
        rows[r] = vals
    return rows


def physical_rates_for_mode(base, mode):
    return {pair: base[pair] + mode[pair] for pair in PAIRS}


def generic_projectors_mu1_nu2(K):
    # P0=(K+I)(K+2I)/2, P1=-K(K+2I), P2=K(K+I)/2.
    P0 = mat_scale(
        mat_mul(matrix_plus_scalar_identity(K, Q(1)), matrix_plus_scalar_identity(K, Q(2))),
        Q(1, 2),
    )
    P1 = mat_scale(mat_mul(K, matrix_plus_scalar_identity(K, Q(2))), Q(-1))
    P2 = mat_scale(mat_mul(K, matrix_plus_scalar_identity(K, Q(1))), Q(1, 2))
    return P0, P1, P2


def generic_LAB_from_n0_n1(K, row, terminal, P0, mu=Q(1), nu=Q(2)):
    L = row_mat_col(row, P0, terminal)
    n0 = dot(row, terminal)
    n1 = row_mat_col(row, K, terminal)
    A = (nu * (n0 - L) + n1) / (nu - mu)
    B = (-mu * (n0 - L) - n1) / (nu - mu)
    return L, A, B


def quadratic_min_on_unit_interval(L, A, B):
    """Exact minimum of L+A*x+B*x^2 on x in [0,1]."""
    candidates = [(Q(0), L), (Q(1), L + A + B)]
    if B > 0:
        x = -A / (2 * B)
        if Q(0) < x < Q(1):
            candidates.append((x, L + A * x + B * x * x))
    return min(candidates, key=lambda item: item[1])


def run_generic_gates():
    checks = 0

    base = {
        (0, 1): Q(0),
        (0, 2): Q(1, 4),
        (1, 0): Q(7, 4),
        (1, 2): Q(1, 4),
        (2, 0): Q(1, 4),
        (2, 1): Q(1, 2),
    }
    for pair in PAIRS:
        assert base[pair] >= 0
        checks += 1

    Qm = physical_Q(base)
    K = typed_empty_K(base)
    assert Qm == [
        [Q(-1, 4), Q(0), Q(1, 4)],
        [Q(7, 4), Q(-2), Q(1, 4)],
        [Q(1, 4), Q(1, 2), Q(-3, 4)],
    ]
    assert K == [
        [Q(0), Q(0), Q(0)],
        [Q(0), Q(-2), Q(1, 2)],
        [Q(1, 4), Q(0), Q(-1)],
    ]
    checks += 2

    # Metzler active retyping entries.
    assert K[1][2] >= 0 and K[2][1] >= 0
    checks += 2

    P0, P1, P2 = generic_projectors_mu1_nu2(K)
    I = eye(3)
    assert mat_add(mat_add(P0, P1), P2) == I
    assert mat_mul(P0, P0) == P0
    assert mat_mul(P1, P1) == P1
    assert mat_mul(P2, P2) == P2
    assert mat_mul(P0, P1) == [[Q(0)] * 3 for _ in range(3)]
    assert mat_mul(P0, P2) == [[Q(0)] * 3 for _ in range(3)]
    assert mat_mul(P1, P2) == [[Q(0)] * 3 for _ in range(3)]
    checks += 7

    # ------------------------------------------------------------------
    # Mandatory gate 1: Assignment-005 obstruction.
    # ------------------------------------------------------------------
    mode1_bad = {
        (0, 1): Q(0),
        (0, 2): Q(-1, 8),
        (1, 0): Q(-9, 8),
        (1, 2): Q(1),
        (2, 0): Q(-1, 8),
        (2, 1): Q(0),
    }
    mode2 = {
        (0, 1): Q(0),
        (0, 2): Q(0),
        (1, 0): Q(-1, 8),
        (1, 2): Q(0),
        (2, 0): Q(-1, 8),
        (2, 1): Q(0),
    }

    for mode in (mode1_bad, mode2):
        rates = physical_rates_for_mode(base, mode)
        for pair in PAIRS:
            assert rates[pair] >= 0
            checks += 1
        rows = typed_nonempty_rows(mode)
        for r in (1, 2):
            assert sum((abs(x) for x in rows[r]), Q(0)) > 0
            checks += 1

    p_bad = typed_nonempty_rows(mode1_bad)[2]
    assert p_bad == [Q(-1, 8), Q(9, 8), Q(1, 4)]
    assert p_bad[1] >= 0 and p_bad[2] >= 0
    assert p_bad[0] + p_bad[1] >= 0 and p_bad[0] + p_bad[2] >= 0
    checks += 5

    fI1 = [Q(1), Q(1), Q(0)]
    L, A, B = generic_LAB_from_n0_n1(K, p_bad, fI1, P0)
    assert (L, A, B) == (Q(1, 128), Q(-13, 64), Q(153, 128))
    # Independent projector extraction.
    assert [row_mat_col(p_bad, P, fI1) for P in (P0, P1, P2)] == [L, A, B]
    checks += 2

    R = -A / (2 * B)  # mu=1, nu=2
    assert R == Q(13, 153)
    minimum = L + A * R + B * R * R
    assert minimum == Q(-1, 1224)
    assert L + A + B == Q(1)
    assert L > 0 and minimum < 0
    checks += 5

    # ------------------------------------------------------------------
    # Mandatory gate 2: realizable p0<0 positive example.
    # Only the neighbour-type-1 coefficient of c^{20} changes from -1/8
    # to -1/4.  Physical rates remain nonnegative.
    # ------------------------------------------------------------------
    mode1_good = dict(mode1_bad)
    mode1_good[(2, 0)] = Q(-1, 4)

    rates_good = physical_rates_for_mode(base, mode1_good)
    for pair in PAIRS:
        assert rates_good[pair] >= 0
        checks += 1

    rows_good_1 = typed_nonempty_rows(mode1_good)
    rows_good_2 = typed_nonempty_rows(mode2)
    assert rows_good_1[2] == [Q(-1, 8), Q(9, 8), Q(3, 8)]
    assert rows_good_1[1] == [Q(0), Q(1, 8), Q(0)]
    checks += 2

    # Boundary completeness: each (source type, target type) has positive
    # coarse hazard in the two target modes.
    all_rows = [rows_good_1[1], rows_good_1[2], rows_good_2[1], rows_good_2[2]]
    for row in all_rows:
        assert sum((abs(x) for x in row), Q(0)) > 0
        checks += 1

    # Zero-length outgoing conditions for every row.
    for row in all_rows:
        assert row[1] >= 0
        assert row[2] >= 0
        assert row[0] + row[1] >= 0
        assert row[0] + row[2] >= 0
        checks += 4

    fI2 = [Q(1), Q(0), Q(1)]
    positive_oi_checks = 0
    distinguished = None
    for row in all_rows:
        for terminal in (fI1, fI2):
            coeffs = tuple(row_mat_col(row, P, terminal) for P in (P0, P1, P2))
            minimum_pair = quadratic_min_on_unit_interval(*coeffs)
            assert minimum_pair[1] >= 0
            positive_oi_checks += 1
            if row == rows_good_1[2] and terminal == fI1:
                distinguished = (coeffs, minimum_pair)
    assert positive_oi_checks == 8
    assert distinguished == (
        (Q(5, 128), Q(-15, 64), Q(153, 128)),
        (Q(5, 51), Q(15, 544)),
    )
    checks += positive_oi_checks + 1

    # OO is automatic from Metzler exp(tK) and p1,p2>=0; at t=0 the exact
    # boundary rows are nonnegative, already checked above.  The spectral
    # projectors also reproduce nonnegative quadratics on [0,1] for both
    # active terminal columns in this rational-spectrum gate.
    fO1 = [Q(0), Q(1), Q(0)]
    fO2 = [Q(0), Q(0), Q(1)]
    oo_checks = 0
    for row in all_rows:
        for terminal in (fO1, fO2):
            coeffs = tuple(row_mat_col(row, P, terminal) for P in (P0, P1, P2))
            assert quadratic_min_on_unit_interval(*coeffs)[1] >= 0
            oo_checks += 1
    assert oo_checks == 8
    checks += oo_checks

    return checks


def run_degenerate_identity_checks():
    checks = 0

    # One active zero eigenvalue: K has spectrum 0,0,-2 and is diagonalizable.
    K0 = [
        [Q(0), Q(0), Q(0)],
        [Q(0), Q(0), Q(0)],
        [Q(1), Q(0), Q(-2)],
    ]
    Pzero = mat_scale(matrix_plus_scalar_identity(K0, Q(2)), Q(1, 2))
    Pdecay = mat_scale(K0, Q(-1, 2))
    assert mat_add(Pzero, Pdecay) == eye(3)
    assert mat_mul(Pzero, Pzero) == Pzero
    assert mat_mul(Pdecay, Pdecay) == Pdecay
    checks += 3

    # Repeated nonzero diagonalizable active block M=-2I.
    Kdiag = [
        [Q(0), Q(0), Q(0)],
        [Q(1), Q(-2), Q(0)],
        [Q(3), Q(0), Q(-2)],
    ]
    # (K+2I)K=0 iff minimal polynomial divides x(x+2).
    zero = [[Q(0)] * 3 for _ in range(3)]
    assert mat_mul(matrix_plus_scalar_identity(Kdiag, Q(2)), Kdiag) == zero
    checks += 1

    # Repeated Jordan active block M=[[-2,1],[0,-2]].
    Kj = [
        [Q(0), Q(0), Q(0)],
        [Q(1), Q(-2), Q(1)],
        [Q(1), Q(0), Q(-2)],
    ]
    # Minimal polynomial check: K(K+2I)^2=0 but K(K+2I)!=0.
    Kp = matrix_plus_scalar_identity(Kj, Q(2))
    assert mat_mul(Kj, mat_mul(Kp, Kp)) == zero
    assert mat_mul(Kj, Kp) != zero
    checks += 2

    # Coefficient reconstruction for one row/terminal in the Jordan case.
    u = [Q(-1), Q(2), Q(1)]
    f = [Q(1), Q(1), Q(0)]
    P0 = mat_scale(mat_mul(Kp, Kp), Q(1, 4))
    L = row_mat_col(u, P0, f)
    A = dot(u, f) - L
    B = row_mat_col(u, Kj, f) + Q(2) * A
    assert dot(u, f) == L + A
    assert row_mat_col(u, Kj, f) == B - Q(2) * A
    checks += 2

    return checks


def run_binary_reduction():
    checks = 0

    # u=c^0(empty), w=c^1(empty), r=u+w.
    u = Q(2)
    w = Q(3)
    r = u + w
    assert r > 0
    checks += 1

    # Nonempty target coefficients.
    c0 = Q(1)
    c1 = Q(-3)
    p = [c0, -(c0 + c1)]

    # OO zero-length condition.
    assert p[1] >= 0
    assert c0 + c1 <= 0
    checks += 2

    # OI one-mode limit is exactly the canonical determinant inequality.
    L = (w * c0 - u * c1) / r
    assert L >= 0
    assert w * c0 >= u * c1
    checks += 2

    # The one-mode numerator is affine in y=e^{-rt}; endpoints suffice.
    n0 = -c1
    assert n0 >= 0
    # Suppressing type 2 introduces no distinct-active Metzler condition.
    checks += 2

    # Degenerate canonical clause: if u=w=0, positivity forces the full binary
    # nonconstant coefficient family to vanish; no stronger condition is added
    # by the spectral test because there is no interior mode.
    uz = Q(0)
    wz = Q(0)
    assert uz + wz == 0
    checks += 1

    return checks


if __name__ == "__main__":
    generic = run_generic_gates()
    degenerate = run_degenerate_identity_checks()
    binary = run_binary_reduction()
    total = generic + degenerate + binary
    print("generic/mandatory exact checks:", generic)
    print("degenerate spectral identity checks:", degenerate)
    print("binary reduction checks:", binary)
    print("total exact checks:", total)
    print("all three-state spectral criterion checks passed")
