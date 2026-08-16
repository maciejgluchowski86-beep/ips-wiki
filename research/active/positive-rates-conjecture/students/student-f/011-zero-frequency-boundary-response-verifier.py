#!/usr/bin/env python3
"""Exact finite-volume checks for Student F Assignment 011.

No Monte Carlo.

The abstract reverse-martingale theorem in the report is analytic, not a finite
calculation.  This verifier checks the load-bearing finite-volume indexing:

1. exact zero-boundary invariant laws at a strict residual rational point;
2. Assignment-011 finite-window boundary response equals the corresponding
   adjacent spatial-window shift defect inside pi_N;
3. the finite-window defects satisfy the projection inequalities underlying
   monotonicity of Delta_M;
4. exact rational values for several windows;
5. the Laplace--Poisson identity used in the conditional one-next-segment lift.
"""

import itertools
import sympy as sp


def generator(N, a, b, c):
    states = list(itertools.product((0, 1), repeat=N))
    index = {s: i for i, s in enumerate(states)}
    Q = sp.zeros(2**N)

    def rate(x, y):
        return {
            (0, 0): sp.Integer(1),
            (0, 1): 1 - c,
            (1, 0): b,
            (1, 1): a,
        }[(x, y)]

    for s in states:
        i = index[s]
        for site in range(N):
            y = s[site + 1] if site < N - 1 else 0
            r = rate(s[site], y)
            t = list(s)
            t[site] = 1 - t[site]
            j = index[tuple(t)]
            Q[i, j] += r
            Q[i, i] -= r
    return states, Q


def stationary_row(Q):
    n = Q.rows
    A = Q.T.copy()
    A[n - 1, :] = sp.ones(1, n)
    rhs = sp.zeros(n, 1)
    rhs[n - 1, 0] = 1
    sol = sp.linsolve((A, rhs))
    vec = list(next(iter(sol)))
    return sp.Matrix([vec])


def marginal(pi, states, positions):
    """Return exact marginal vector on positions, preserving their order."""
    positions = tuple(positions)
    out = [sp.Rational(0) for _ in range(2 ** len(positions))]
    for pr, state in zip(list(pi), states):
        key = 0
        for p in positions:
            key = 2 * key + state[p]
        out[key] += pr
    return [sp.factor(x) for x in out]


def l1(p, q):
    return sp.factor(sum(abs(x - y) for x, y in zip(p, q)))


# Strict residual rational point used in F008--F010.
a = sp.Rational(1, 10)
b = sp.Rational(3, 10)
c = sp.Rational(4, 5)
assert 0 < a < b
assert sp.Rational(1, 2) <= c < 1
assert c >= a + b
assert b**2 >= 2 * (1 - c) ** 2

cache = {}


def piN(N):
    if N not in cache:
        states, Q = generator(N, a, b, c)
        cache[N] = (states, stationary_row(Q))
    return cache[N]


def assignment_window_defect(M, L):
    """N=M+L version of the finite window entering Delta_M."""
    N = M + L
    statesN, pi_N = piN(N)
    statesNm, pi_Nm = piN(N - 1)

    # Under bar pi_N: first L labelled sites of pi_N.
    left_N = marginal(pi_N, statesN, range(L))
    # Under pi_{N-1}: first L labelled sites of pi_{N-1}.
    left_Nm = marginal(pi_Nm, statesNm, range(L))
    return l1(left_N, left_Nm)


def adjacent_window_defect(M, L):
    """Same defect viewed as adjacent spatial windows inside pi_{M+L}."""
    N = M + L
    statesN, pi_N = piN(N)
    # X_M,...,X_{M+L-1} is original sites 1,...,L, reversed.
    # Reversal is a bijection, so compare sites 0,...,L-1 with 1,...,L.
    w0 = marginal(pi_N, statesN, range(L))
    w1 = marginal(pi_N, statesN, range(1, L + 1))
    return l1(w0, w1)


# Exact indexing identity from Proposition 3.1 for several nontrivial windows.
for M, L in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (4, 1), (4, 2)]:
    assert assignment_window_defect(M, L) == adjacent_window_defect(M, L)

# Exact rational diagnostics.
d21 = assignment_window_defect(2, 1)
d22 = assignment_window_defect(2, 2)
d31 = assignment_window_defect(3, 1)
d32 = assignment_window_defect(3, 2)
d41 = assignment_window_defect(4, 1)

assert d21 == sp.Rational(370, 149877)
assert d22 == d21
assert d31 == sp.Rational(396495755, 465375762033)
assert d32 == d31
assert d41 == sp.Rational(
    137507832833326083482555,
    4184267004326117334172112748,
)

# Finite-window data-processing inequalities:
# dropping the first coordinate from the two length-(L+1) windows at distance M
# gives the two length-L windows at distance M+1.
for M, L in [(2, 1), (2, 2), (3, 1), (3, 2), (4, 1)]:
    assert assignment_window_defect(M + 1, L) <= assignment_window_defect(M, L + 1)

# For fixed M, enlarging the observed window cannot decrease variation.
for M, L in [(2, 1), (2, 2), (3, 1), (4, 1)]:
    assert assignment_window_defect(M, L) <= assignment_window_defect(M, L + 1)

# Laplace--Poisson identity used after retaining the absolute value at each u.
lam = sp.symbols("lam", positive=True)
m = sp.symbols("m", integer=True, nonnegative=True)
n = sp.symbols("n", integer=True, nonnegative=True)
tail = sp.simplify(
    sp.summation((1 / (1 + lam)) ** (n + 1), (n, m, sp.oo))
)
assert sp.simplify(tail - 1 / (lam * (1 + lam) ** m)) == 0

print("strict residual rational point: verified")
print("finite-window boundary/shift indexing: verified")
print("finite-window projection monotonicity: verified")
print("d_{2,1} =", d21)
print("d_{3,1} =", d31)
print("d_{4,1} =", d41)
print("Laplace--Poisson tail =", tail)
