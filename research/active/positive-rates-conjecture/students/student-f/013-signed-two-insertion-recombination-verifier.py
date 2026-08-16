#!/usr/bin/env python3
"""Exact checks for Student F Assignment 013.

No Monte Carlo and no floating-point assertions.

Checks:
1. exact strict-residual rational calibration and suffix projectivity;
2. volume-independence of the scalar first-insertion mass/transient data;
3. the exact two-insertion recombination identity using a rational Markov
   resolvent kernel (the proof only needs a Markov kernel preserving pi);
4. the zero-frequency invariant projection gives exactly m0*rho_{N-1};
5. rho_n = m0*delta_n + B*covariance_n as signed measures;
6. on the exceptional surface a=b(1-c), the invariant law is exactly the
   Bernoulli product law and J_N pi_N vanishes.
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
            rate = rates[(s[site], y)]
            t = list(s)
            t[site] = 1 - s[site]
            j = index[tuple(t)]
            Q[i, j] += rate
            Q[i, i] -= rate
    return states, Q


def stationary_row(Q):
    n = Q.rows
    A = Q.T.copy()
    A[n - 1, :] = sp.ones(1, n)
    rhs = sp.zeros(n, 1)
    rhs[n - 1, 0] = 1
    col = A.inv() * rhs
    return sp.Matrix([list(col)])


def J_matrix(N, B, c):
    states = list(itertools.product((0, 1), repeat=N))
    left = list(itertools.product((0, 1), repeat=N - 1))
    index = {s: i for i, s in enumerate(left)}
    J = sp.zeros(2**N, 2 ** (N - 1))
    for i, s in enumerate(states):
        J[i, index[s[:-1]]] = B * s[-1] - c
    return J


def phi_matrix(N, r0):
    states = list(itertools.product((0, 1), repeat=N))
    left = list(itertools.product((0, 1), repeat=N - 1))
    index = {s: i for i, s in enumerate(left)}
    J = sp.zeros(2**N, 2 ** (N - 1))
    for i, s in enumerate(states):
        J[i, index[s[:-1]]] = s[-1] - r0
    return J


def left_marginal_matrix(N):
    states = list(itertools.product((0, 1), repeat=N))
    left = list(itertools.product((0, 1), repeat=N - 1))
    index = {s: i for i, s in enumerate(left)}
    R = sp.zeros(2**N, 2 ** (N - 1))
    for i, s in enumerate(states):
        R[i, index[s[:-1]]] = 1
    return R


def right_marginal_matrix(N, M):
    states = list(itertools.product((0, 1), repeat=N))
    suffix = list(itertools.product((0, 1), repeat=M))
    index = {s: i for i, s in enumerate(suffix)}
    R = sp.zeros(2**N, 2**M)
    for i, s in enumerate(states):
        R[i, index[s[-M:]]] = 1
    return R


# ---------------------------------------------------------------------------
# Symbolic scalar identities.
# ---------------------------------------------------------------------------
a, b, c = sp.symbols("a b c", positive=True)
B = b + c - a
g = b - a
r0 = 1 / (1 + b)
m0 = sp.factor(B * r0 - c)
assert sp.factor(m0 - (b * (1 - c) - a) / (1 + b)) == 0

S = a * b + 2 * a + b**2 - b * c + 2 * b - 2 * c + 2
Cstar = sp.factor(
    (a + b * c - b)
    * (a * b + 2 * a - b**2 + b * c - 2 * b)
    / ((1 + b) ** 2 * S)
)
assert sp.factor(Cstar.subs(a, b * (1 - c))) == 0


# ---------------------------------------------------------------------------
# Strict residual rational point used throughout F008--F012.
# ---------------------------------------------------------------------------
aa = sp.Rational(1, 10)
bb = sp.Rational(3, 10)
cc = sp.Rational(4, 5)
subs = {a: aa, b: bb, c: cc}
BB = sp.factor(B.subs(subs))
rr = sp.factor(r0.subs(b, bb))
mm = sp.factor(m0.subs(subs))

assert 0 < aa < bb
assert sp.Rational(1, 2) <= cc < 1
assert cc >= aa + bb
assert bb**2 >= 2 * (1 - cc) ** 2
assert BB == 1
assert rr == sp.Rational(10, 13)
assert mm == -sp.Rational(2, 65)

cache = {}
for N in range(1, 5):
    states, Q = generator(N, aa, bb, cc)
    cache[N] = (states, Q, stationary_row(Q))


# Exact suffix projectivity of pi_N.
for N, M in [(3, 2), (4, 2), (4, 3)]:
    R = right_marginal_matrix(N, M)
    assert sp.simplify(cache[N][2] * R - cache[M][2]) == sp.zeros(1, 2**M)


# ---------------------------------------------------------------------------
# First-insertion signed measures and volume-independent scalar data.
# ---------------------------------------------------------------------------
nu = {}
rho = {}
for N in range(2, 5):
    J = J_matrix(N, BB, cc)
    nu[N] = cache[N][2] * J
    rho[N] = sp.simplify(nu[N] - mm * cache[N - 1][2])
    assert sp.factor(sum(nu[N])) == mm
    assert sp.factor(sum(rho[N])) == 0

CC = sp.factor(Cstar.subs(subs))
assert CC == -sp.Rational(22, 4563)

for N in (2, 3, 4):
    states_left = cache[N - 1][0]
    eta_right = sp.Matrix([s[-1] for s in states_left])
    cN = sp.factor((nu[N] * eta_right)[0] - rr * mm)
    assert cN == CC

# If z=e^{-(1+b)u}, then a_N(u)=m0^2+B*Cstar*z.
z = sp.symbols("z")
a_of_z = sp.factor(mm**2 + BB * CC * z)
assert a_of_z.subs(z, 0) == sp.Rational(4, 4225)
assert a_of_z.subs(z, 1) == -sp.Rational(34, 8775)


# ---------------------------------------------------------------------------
# Exact recombination identity.
# Use a rational Markov resolvent kernel P=lambda(lambda I-Q)^{-1} on the
# three-site zero-boundary chain. The identity proved in the report only uses
# P1=1 and pi P=pi, so this is an exact finite arithmetic check of the same
# algebra without symbolic matrix exponentials.
# ---------------------------------------------------------------------------
N = 4
n = 3
Qn = cache[n][1]
lam = sp.Rational(7, 5)
P = sp.simplify(lam * (lam * sp.eye(2**n) - Qn).inv())
one = sp.ones(2**n, 1)

assert sp.simplify(P * one - one) == sp.zeros(2**n, 1)
assert sp.simplify(cache[n][2] * P - cache[n][2]) == sp.zeros(1, 2**n)

J3 = J_matrix(3, BB, cc)
kappa = sp.simplify(nu[4] * P * J3)
aK = sp.factor(sum(kappa))
sigma = sp.simplify(rho[4] * P * J3)

# Measure form of
# E(f)=m0*rho_3(f)+rho_4 P[Y_3(f-pi_2 f)].
rhs = sp.simplify(
    mm * rho[3]
    + sigma
    - sp.factor(sum(sigma)) * cache[2][2]
)
lhs = sp.simplify(kappa - aK * cache[2][2])
assert sp.simplify(lhs - rhs) == sp.zeros(1, 4)


# ---------------------------------------------------------------------------
# Zero temporal frequency: replace P by its invariant projection.
# ---------------------------------------------------------------------------
Pinf = sp.ones(2**n, 1) * cache[n][2]
assert sp.simplify(Pinf * Pinf - Pinf) == sp.zeros(2**n)

kappa_inf = sp.simplify(nu[4] * Pinf * J3)
a_inf = sp.factor(sum(kappa_inf))
defect_inf = sp.simplify(kappa_inf - a_inf * cache[2][2])

assert a_inf == mm**2
assert sp.simplify(defect_inf - mm * rho[3]) == sp.zeros(1, 4)


# ---------------------------------------------------------------------------
# Exact spatial decomposition rho_n=m0*delta_n+B*covariance_n.
# ---------------------------------------------------------------------------
for n in (2, 3, 4):
    L = left_marginal_matrix(n)
    delta = sp.simplify(cache[n][2] * L - cache[n - 1][2])
    covariance = sp.simplify(cache[n][2] * phi_matrix(n, rr))
    assert sp.simplify(rho[n] - mm * delta - BB * covariance) == sp.zeros(
        1, 2 ** (n - 1)
    )


# ---------------------------------------------------------------------------
# Exceptional surface m0=0: exact product invariant law and zero insertion.
# ---------------------------------------------------------------------------
b0 = sp.Rational(1, 5)
c0 = sp.Rational(9, 10)
a0 = b0 * (1 - c0)
B0 = b0 + c0 - a0
r00 = 1 / (1 + b0)
m00 = sp.factor(B0 * r00 - c0)
assert m00 == 0

states4, Q4 = generator(4, a0, b0, c0)
pi4 = stationary_row(Q4)
prod = []
for s in states4:
    p = sp.Integer(1)
    for x in s:
        p *= r00 if x else 1 - r00
    prod.append(sp.factor(p))
prod = sp.Matrix([prod])

assert sp.simplify(pi4 - prod) == sp.zeros(1, 16)
assert sp.simplify(pi4 * J_matrix(4, B0, c0)) == sp.zeros(1, 8)


print("strict residual rational point: verified")
print("suffix projectivity through N=4: verified")
print("m0 =", mm, "Cstar =", CC)
print("a(z) =", a_of_z)
print("recombined defect identity with exact resolvent kernel: verified")
print("zero-frequency projection defect = m0*rho_{N-1}: verified")
print("rho = m0*delta + B*covariance through N=4: verified")
print("m0=0 surface product example: J pi = 0 verified")
