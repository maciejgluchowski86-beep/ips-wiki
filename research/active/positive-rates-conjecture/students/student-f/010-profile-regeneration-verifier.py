#!/usr/bin/env python3
"""Exact checks for Student F Assignment 010.

No Monte Carlo.

Checks:
1. exact right-suffix generator intertwining for the zero-boundary process;
2. exact centered insertion/marginal intertwining;
3. invariant suffix consistency at a strict rational residual point;
4. the local algebra behind the positive-frequency separated-gap resolvent;
5. the Poisson/Laplace finite-speed tail identity;
6. an exact rational separated-gap example;
7. the generator decomposition underlying the zero-frequency boundary-response
   formula, and that formula itself on an exact finite example.
"""

import itertools
import sympy as sp


a, b, c, lam = sp.symbols("a b c lam", positive=True)
B = b + c - a
gpar = b - a
omega = 1 - c + a
r0 = 1 / (1 + b)
q0 = b / (1 + b)


def local_rate(x, y):
    return {
        (0, 0): sp.Integer(1),
        (0, 1): 1 - c,
        (1, 0): b,
        (1, 1): a,
    }[(x, y)]


def generator(N, boundary=0):
    states = list(itertools.product((0, 1), repeat=N))
    index = {s: i for i, s in enumerate(states)}
    Q = sp.zeros(2**N)
    for s in states:
        i = index[s]
        for site in range(N):
            y = s[site + 1] if site < N - 1 else boundary
            rate = local_rate(s[site], y)
            t = list(s)
            t[site] = 1 - t[site]
            j = index[tuple(t)]
            Q[i, j] += rate
            Q[i, i] -= rate
    return states, Q


def marginal_kernel(N, M):
    """Matrix R with row-law marginalization nu -> nu R to rightmost M sites."""
    states_N = list(itertools.product((0, 1), repeat=N))
    states_M = list(itertools.product((0, 1), repeat=M))
    index_M = {s: i for i, s in enumerate(states_M)}
    R = sp.zeros(2**N, 2**M)
    for i, state in enumerate(states_N):
        R[i, index_M[state[N-M:]]] = 1
    return R


def insertion_kernel(N):
    """nu -> J_N nu, multiplying by B eta_N-c and dropping site N."""
    states_N = list(itertools.product((0, 1), repeat=N))
    states_L = list(itertools.product((0, 1), repeat=N - 1))
    index_L = {s: i for i, s in enumerate(states_L)}
    J = sp.zeros(2**N, 2**(N - 1))
    for i, state in enumerate(states_N):
        J[i, index_L[state[:-1]]] = B * state[-1] - c
    return J


def stationary_row(Q):
    """Exact invariant row vector for an irreducible finite generator."""
    n = Q.rows
    A = Q.T.copy()
    A[n - 1, :] = sp.ones(1, n)
    rhs = sp.zeros(n, 1)
    rhs[n - 1, 0] = 1
    col = A.inv() * rhs
    return sp.Matrix([list(col)])


# 1. Exact suffix generator intertwining Q_N R = R Q_M.
states3, Q3 = generator(3, boundary=0)
states2, Q2 = generator(2, boundary=0)
R32 = marginal_kernel(3, 2)
assert sp.simplify(Q3 * R32 - R32 * Q2) == sp.zeros(8, 4)

states4, Q4 = generator(4, boundary=0)
R43 = marginal_kernel(4, 3)
assert sp.simplify(Q4 * R43 - R43 * Q3) == sp.zeros(16, 8)

# 2. Exact insertion/marginal intertwining J_N R = R J_M.
J3 = insertion_kernel(3)
J2 = insertion_kernel(2)
R21 = marginal_kernel(2, 1)
assert sp.simplify(J3 * R21 - R32 * J2) == sp.zeros(8, 2)

J4 = insertion_kernel(4)
assert sp.simplify(J4 * R32 - R43 * J3) == sp.zeros(16, 4)

# 3. Exact invariant suffix consistency at a strict residual rational point.
aa = sp.Rational(1, 10)
bb = sp.Rational(3, 10)
cc = sp.Rational(4, 5)
subs = {a: aa, b: bb, c: cc}
assert aa < bb
assert cc >= aa + bb
assert bb**2 >= 2 * (1 - cc)**2

pi3 = stationary_row(Q3.subs(subs))
pi2 = stationary_row(Q2.subs(subs))
assert sp.simplify(pi3 * R32 - pi2) == sp.zeros(1, 4)

# 4. Positive-frequency boundary-response algebra.
eta = sp.symbols("eta")
phi = eta - r0
for ev in (0, 1):
    assert sp.factor(
        (phi * eta - q0 * (phi + r0)).subs(eta, ev)
    ) == 0

# Boundary generator difference D=L^1-L^0 at the last retained site.
assert sp.factor(local_rate(0, 1) - local_rate(0, 0) + c) == 0
assert sp.factor(local_rate(1, 1) - local_rate(1, 0) + gpar) == 0

prefactor = sp.factor(q0 * r0 * c * 2 / (1 + b))
assert sp.factor(prefactor - 2 * b * c / (1 + b) ** 3) == 0

# 5. Poisson/Laplace finite-speed tail identity.
# Integrating each Poisson term first yields this geometric series.
n = sp.symbols("n", integer=True, nonnegative=True)
m = sp.symbols("m", integer=True, nonnegative=True)
tail_laplace = sp.simplify(
    sp.summation((1 / (1 + lam)) ** (n + 1), (n, m, sp.oo))
)
assert sp.simplify(
    tail_laplace - 1 / (lam * (1 + lam) ** m)
) == 0

# 6. Exact separated-gap example at (1/10,3/10,4/5).
# N=3, f=eta_1, so the gap parameter in Theorem 5.1 is M=2.
BB = sp.factor(B.subs(subs))
rr = sp.factor(r0.subs(subs))
assert BB == 1

corr_vals = sp.Matrix([
    BB * (state[2] - rr) * state[0]
    for state in states3
])
defect = sp.factor((pi3 * corr_vals)[0])
assert defect == -sp.Rational(170, 1948401)

Mgap = 2
gap_bound = sp.factor(
    2 * BB * bb * cc
    / ((1 + bb) ** 3 * (2 + bb) ** (Mgap - 1))
)
assert gap_bound == sp.Rational(4800, 50531)
assert abs(defect) < gap_bound

# 7. Generator decomposition and zero-frequency boundary response.
# For f on the first N-1 sites:
# Q_N E = E Q^0 + diag(eta_N) E (Q^1-Q^0).
states2b, Q20 = generator(2, boundary=0)
_, Q21 = generator(2, boundary=1)
D2 = sp.simplify(Q21 - Q20)

index2 = {s: i for i, s in enumerate(states2b)}
E = sp.zeros(8, 4)
diag_eta3 = sp.zeros(8)
for i, state in enumerate(states3):
    E[i, index2[state[:2]]] = 1
    diag_eta3[i, i] = state[2]

assert sp.simplify(
    Q3 * E - E * Q20 - diag_eta3 * E * D2
) == sp.zeros(8, 4)

# Exact Poisson-equation response for f=eta_1 at the rational point.
Q20e = Q20.subs(subs)
D2e = D2.subs(subs)
f2 = sp.Matrix([state[0] for state in states2b])
mean_f2 = sp.factor((pi2 * f2)[0])
h2 = f2 - mean_f2 * sp.ones(4, 1)

Gsyms = sp.symbols("G0:4")
Gvec = sp.Matrix(Gsyms)
eqs = list(-Q20e * Gvec - h2)
eqs.append((pi2 * Gvec)[0])
sol = sp.solve(eqs, Gsyms, dict=True)[0]
Gvec = sp.Matrix([sp.factor(sol[x]) for x in Gsyms])

f3_emb = E * f2
lhs = sp.factor((pi3 * f3_emb)[0] - mean_f2)
DG = D2e * Gvec
DG_emb = E * DG
rhs_vals = sp.Matrix([
    state[2] * DG_emb[i]
    for i, state in enumerate(states3)
])
rhs = sp.factor((pi3 * rhs_vals)[0])
assert sp.factor(lhs - rhs) == 0
assert lhs != 0

print("suffix generator intertwining: verified")
print("centered insertion intertwining: verified")
print("rational invariant suffix consistency: verified")
print("Poisson/Laplace tail =", tail_laplace)
print("separated-gap defect =", defect)
print("separated-gap bound =", gap_bound)
print("zero-frequency boundary response =", lhs)
