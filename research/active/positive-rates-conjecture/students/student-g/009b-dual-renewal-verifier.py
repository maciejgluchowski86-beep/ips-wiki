#!/usr/bin/env python3
"""Exact verifier for Student G 009b.

Everything asserted below is exact rational arithmetic.  No Monte Carlo and no
floating-point assertion is used.

Checks:
1. the rational duration filter sigma(u)=1-2 exp(-tau u), tau=4/125;
2. the functional-calculus matrices H_N^sigma at the strict growth point;
3. the separator/connected renewal coefficients through k=7;
4. lambda_1,...,lambda_5>0 and lambda_6,lambda_7<0;
5. sum_{k<=3} lambda_k>1 and sum_{k<=7} lambda_k>1.

The k=7 exact calculation uses a 128-state rational generator and can take a
few tens of seconds on an ordinary laptop.
"""

import itertools
import sympy as sp


a = sp.Rational(1, 1000)
b = sp.Rational(1, 10)
c = sp.Rational(9999, 10000)
B = sp.factor(b + c - a)
g = sp.factor(b - a)
omega = sp.factor(1 - c + a)
tau = sp.Rational(4, 125)


def generator(N):
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
            y = s[site + 1] if site < N - 1 else 0
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
    return (A.inv() * rhs).T


def J_matrix(N):
    states = list(itertools.product((0, 1), repeat=N))
    if N == 1:
        return sp.Matrix([[-c], [B - c]])
    left = list(itertools.product((0, 1), repeat=N - 1))
    index = {s: i for i, s in enumerate(left)}
    J = sp.zeros(2**N, 2 ** (N - 1))
    for i, s in enumerate(states):
        J[i, index[s[:-1]]] = B * s[-1] - c
    return J


cache = {}


def data(N):
    if N not in cache:
        states, Q = generator(N)
        cache[N] = (states, Q, stationary_row(Q), J_matrix(N))
    return cache[N]


# Scalar right-survival resolvent.
alpha = sp.symbols("alpha")
Zalpha = sp.factor(
    (alpha + 1 + B + a) / ((alpha + a) * (alpha + 1 + B) - a)
)
Z = sp.factor(Zalpha.subs(alpha, omega))
z = sp.factor(Z - 2 * Zalpha.subs(alpha, omega + tau))

assert Z == sp.Rational(19100, 31)
assert z == sp.Rational(114559900, 205809)
assert z > 0


def H(N, alpha0):
    """Integral int exp(-alpha0*u) s_1(u) P_u^N du by rational calculus."""
    Q = data(N)[1]
    I = sp.eye(2**N)
    A = alpha0 * I - Q
    numerator = A + (1 + B + a) * I
    denominator = (A + a * I) * (A + (1 + B) * I) - a * I
    return numerator * denominator.inv()


def H_sigma(N):
    return H(N, omega) - 2 * H(N, omega + tau)


def witness_without_first_Z(n):
    """r_n = pi_n J_n H_{n-1}J_{n-1}...H_1J_1."""
    nu = data(n)[2] * data(n)[3]
    for N in range(n - 1, 0, -1):
        nu = nu * H_sigma(N) * data(N)[3]
    return sp.factor(nu[0])


# The renewal coefficients can be recovered uniquely from v_n=z*r_n and
# v_n=sum_{k=1}^n a_k v_{n-k}, v_0=1.  This is algebraically equivalent to
# expanding each H_N^sigma as z Pi_N + Q_N^sigma.
v = [sp.Integer(1)]
a_conn = [sp.Integer(0)]
lambda_conn = [None]

for n in range(1, 8):
    rn = witness_without_first_Z(n)
    vn = sp.factor(z * rn)
    v.append(vn)
    an = sp.factor(vn - sum(a_conn[k] * v[n - k] for k in range(1, n)))
    a_conn.append(an)
    lambda_conn.append(sp.factor((-1) ** n * an))

for k in range(1, 6):
    assert lambda_conn[k] > 0
assert lambda_conn[6] < 0
assert lambda_conn[7] < 0

sum3 = sp.factor(sum(lambda_conn[1:4]))
sum5 = sp.factor(sum(lambda_conn[1:6]))
sum7 = sp.factor(sum(lambda_conn[1:8]))

assert sum3 > 1
assert sum5 > 1
assert sum7 > 1

# Exact rational quoted in the checkpoint for the first three coefficients.
expected_sum3 = sp.Rational(
    13527592705747857940057379920020048209153033809425644997909,
    13242140353695961074570637892809167079743173592358486400000,
)
assert sum3 == expected_sum3

print("Z =", Z)
print("z_sigma =", z)
for k in range(1, 8):
    print(f"lambda_{k} =", lambda_conn[k])
    print(f"lambda_{k} decimal =", sp.N(lambda_conn[k], 18))
print("sum lambda_1..lambda_3 =", sp.N(sum3, 18))
print("sum lambda_1..lambda_5 =", sp.N(sum5, 18))
print("sum lambda_1..lambda_7 =", sp.N(sum7, 18))
print("exact dual-renewal checks passed")
