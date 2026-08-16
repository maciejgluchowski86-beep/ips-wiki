#!/usr/bin/env python3
"""Exact checks for Student F Assignment 014.

No Monte Carlo.

Checks:
1. strict residual rational calibration and independent-reset decomposition;
2. h_* = pi_2(Y_2 Y_1) = -34/8775 at the standard rational point;
3. exact static decomposition
       E_{N,0} = centered two-site suffix measure + h_* delta_N^(2)
   for N=4,5;
4. finite-window indexing of delta_N^(2) as a two-step spatial shift defect;
5. exact decoupled-kernel dynamic normal form with a rational
   invariant-preserving left kernel and a rational one-site mixing eigenvalue;
6. the one-site kernel sends Y to m0 + z B(eta-r0);
7. h_* vanishes on the product surface a=b(1-c).
"""

import itertools
import sympy as sp


def generator(N, a, b, c, boundary=0):
    states = list(itertools.product((0, 1), repeat=N))
    index = {s: i for i, s in enumerate(states)}
    Q = sp.zeros(2**N)
    rates = {
        (0, 0): sp.Integer(1),
        (0, 1): 1 - c,
        (1, 0): b,
        (1, 1): a,
    }
    for s in states:
        i = index[s]
        for site in range(N):
            y = s[site + 1] if site < N - 1 else boundary
            r = rates[(s[site], y)]
            t = list(s)
            t[site] = 1 - s[site]
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
    return sp.Matrix([list(A.inv() * rhs)])


def marginal_matrix(N, positions):
    states = list(itertools.product((0, 1), repeat=N))
    positions = tuple(positions)
    outs = list(itertools.product((0, 1), repeat=len(positions)))
    index = {s: i for i, s in enumerate(outs)}
    R = sp.zeros(2**N, 2 ** len(positions))
    for i, s in enumerate(states):
        R[i, index[tuple(s[p] for p in positions)]] = 1
    return R


def weighted_left_matrix(N, drop, weight):
    states = list(itertools.product((0, 1), repeat=N))
    left = list(itertools.product((0, 1), repeat=N - drop))
    index = {s: i for i, s in enumerate(left)}
    W = sp.zeros(2**N, 2 ** (N - drop))
    for i, s in enumerate(states):
        W[i, index[s[:N-drop]]] = sp.factor(weight(s))
    return W


def J_matrix(N, B, c):
    states = list(itertools.product((0, 1), repeat=N))
    left = list(itertools.product((0, 1), repeat=N - 1))
    index = {s: i for i, s in enumerate(left)}
    J = sp.zeros(2**N, 2 ** (N - 1))
    for i, s in enumerate(states):
        J[i, index[s[:-1]]] = B * s[-1] - c
    return J


def product_kernel(Qleft, S):
    nleft = 0
    n = Qleft.rows
    while 2**nleft < n:
        nleft += 1
    assert 2**nleft == n
    leftstates = list(itertools.product((0, 1), repeat=nleft))
    states = list(itertools.product((0, 1), repeat=nleft + 1))
    li = {s: i for i, s in enumerate(leftstates)}
    P = sp.zeros(len(states))
    for i, x in enumerate(states):
        for j, y in enumerate(states):
            P[i, j] = Qleft[li[x[:-1]], li[y[:-1]]] * S[x[-1], y[-1]]
    return P


# Standard strict residual rational point.
a = sp.Rational(1, 10)
b = sp.Rational(3, 10)
c = sp.Rational(4, 5)
B = b + c - a
g = b - a
k = 1 - c
omega = a + k
r0 = 1 / (1 + b)
m0 = sp.factor(B * r0 - c)

assert 0 < a < b
assert sp.Rational(1, 2) <= c < 1
assert c >= a + b
assert b**2 >= 2 * (1 - c)**2
assert B == 1
assert g == sp.Rational(1, 5)
assert omega == sp.Rational(3, 10)
assert r0 == sp.Rational(10, 13)
assert m0 == -sp.Rational(2, 65)

# Independent reset decomposition: reset-to-1 at k, reset-to-0 at a,
# and when the right neighbour is zero a rate-B Bernoulli(c/B) refresh.
pstar = sp.factor(c / B)
qstar = sp.factor(g / B)
assert pstar + qstar == 1
assert k + B * pstar == 1
assert a + B * qstar == b

cache = {}
for N in range(1, 7):
    states, Q = generator(N, a, b, c)
    cache[N] = (states, Q, stationary_row(Q))


def Y(x):
    return B * x - c


# h_* = pi_2(Y_2 Y_1).
hstar = sp.factor(sum(
    pr * Y(s[-1]) * Y(s[-2])
    for pr, s in zip(list(cache[2][2]), cache[2][0])
))
assert hstar == -sp.Rational(34, 8775)

# Static decomposition E0 = centered suffix covariance measure + h_* delta^(2).
for N in (4, 5):
    piN = cache[N][2]
    WH = weighted_left_matrix(N, 2, lambda s: Y(s[-1]) * Y(s[-2]))
    WHc = weighted_left_matrix(
        N, 2, lambda s: Y(s[-1]) * Y(s[-2]) - hstar
    )
    L2 = marginal_matrix(N, range(N - 2))
    E0 = sp.simplify(piN * WH - hstar * cache[N - 2][2])
    centered = sp.simplify(piN * WHc)
    delta2 = sp.simplify(piN * L2 - cache[N - 2][2])
    assert sp.simplify(E0 - centered - hstar * delta2) == sp.zeros(
        1, 2 ** (N - 2)
    )

# Finite-window indexing: the double-left marginal of pi_{M+L+2}
# and pi_{M+L} are two-step-shifted windows inside the larger pi.
for M, L in ((1, 1), (1, 2), (2, 1), (2, 2)):
    N = M + L + 2
    piN = cache[N][2]
    w_far = piN * marginal_matrix(N, range(L))
    w_near = cache[N - 2][2] * marginal_matrix(N - 2, range(L))
    w_near_inside = piN * marginal_matrix(N, range(2, L + 2))
    assert sp.simplify(w_near - w_near_inside) == sp.zeros(1, 2**L)
    assert sp.simplify(w_far - w_near) == sp.simplify(
        w_far - w_near_inside
    )

# Exact decoupled dynamic normal form at N=4.
N = 4
lam = sp.Rational(7, 5)
Q2 = cache[2][1]
Qleft = sp.simplify(lam * (lam * sp.eye(4) - Q2).inv())
assert sp.simplify(cache[2][2] * Qleft - cache[2][2]) == sp.zeros(1, 4)

# Rational one-site kernel with stationary pi_1 and nonconstant eigenvalue z.
z = sp.Rational(2, 5)
pi1 = cache[1][2]
Pi1 = sp.ones(2, 1) * pi1
S = sp.simplify(Pi1 + z * (sp.eye(2) - Pi1))
assert sp.simplify(pi1 * S - pi1) == sp.zeros(1, 2)

Yvec = sp.Matrix([Y(0), Y(1)])
SY = sp.simplify(S * Yvec)
targetY = sp.Matrix([
    m0 + z * B * (sp.Integer(0) - r0),
    m0 + z * B * (sp.Integer(1) - r0),
])
assert sp.simplify(SY - targetY) == sp.zeros(2, 1)

Pcut = product_kernel(Qleft, S)
nu4 = cache[4][2] * J_matrix(4, B, c)
kcut = sp.simplify(nu4 * Pcut * J_matrix(3, B, c))

# G_z = Y_4 [m0 + z B(eta_3-r0)].
WG = weighted_left_matrix(
    4, 2, lambda s: Y(s[-1]) * (m0 + z * B * (s[-2] - r0))
)
Gleft = sp.simplify(cache[4][2] * WG)
az = sp.factor(sum(Gleft))
leftm = sp.simplify(cache[4][2] * marginal_matrix(4, range(2)))
centered = sp.simplify(Gleft - az * leftm)
delta2 = sp.simplify(leftm - cache[2][2])

lhs = sp.simplify(kcut - az * cache[2][2])
rhs = sp.simplify((centered + az * delta2) * Qleft)
assert sp.simplify(lhs - rhs) == sp.zeros(1, 4)
assert az == -sp.Rational(112, 114075)

# Product surface a=b(1-c) makes h_* vanish (and J pi vanishes).
b0 = sp.Rational(1, 5)
c0 = sp.Rational(9, 10)
a0 = b0 * (1 - c0)
B0 = b0 + c0 - a0
states2, Q20 = generator(2, a0, b0, c0)
pi20 = stationary_row(Q20)
Y0 = lambda x: B0 * x - c0
h0 = sp.factor(sum(
    pr * Y0(s[-1]) * Y0(s[-2])
    for pr, s in zip(list(pi20), states2)
))
assert h0 == 0
assert sp.simplify(pi20 * J_matrix(2, B0, c0)) == sp.zeros(1, 2)

print("strict residual rational point: verified")
print("independent reset decomposition: verified, omega =", omega)
print("h_* = pi_2(Y_2 Y_1) =", hstar)
print("static E0 = centered suffix + h_* delta^(2): verified through N=5")
print("two-step finite-window shift indexing: verified")
print("decoupled dynamic normal form: verified")
print("decoupled scalar a_z =", az)
print("product surface h_*=0 and J pi=0: verified")
