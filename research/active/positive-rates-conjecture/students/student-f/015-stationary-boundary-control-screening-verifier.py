#!/usr/bin/env python3
"""Exact checks for Student F Assignment 015.

No Monte Carlo and no floating-point assertions.

Checks at the strict residual rational point
    (a,b,c)=(1/10,3/10,4/5):
1. N=1 upper/lower Bellman correctors and slacks;
2. exact fixed-boundary versus state-dependent-feedback stationary densities;
3. exact enumeration of all deterministic N=2 controllers, giving
       U_2=3/8, ell_2=31/137;
4. the N=1 -> 2 Bellman-slack occupation identities
       U_1-U_2=9/40,
       ell_2-ell_1=204/1507;
5. exact N=2 upper/lower Bellman correctors and inequalities;
6. both actions are tight in each one-spin interface cylinder at N=2;
7. a finite exact check of the controller-uniform mismatch lower bound.
"""

import itertools
import sympy as sp


a = sp.Rational(1, 10)
b = sp.Rational(3, 10)
c = sp.Rational(4, 5)
g = b - a
k = 1 - c
rstar = min(a, k)

assert 0 < a < b
assert sp.Rational(1, 2) <= c < 1
assert c >= a + b
assert b**2 >= 2 * (1 - c) ** 2


def states(N):
    return list(itertools.product((0, 1), repeat=N))


def action_generator(N, u):
    S = states(N)
    idx = {s: i for i, s in enumerate(S)}
    Q = sp.zeros(2**N)
    for s in S:
        i = idx[s]
        for j in range(N):
            y = s[j + 1] if j < N - 1 else u
            rate = a + g * y if s[j] == 0 else k + c * y
            t = list(s)
            t[j] = 1 - t[j]
            jj = idx[tuple(t)]
            Q[i, jj] += rate
            Q[i, i] -= rate
    return S, Q


def policy_generator(N, policy):
    S = states(N)
    Qs = [action_generator(N, u)[1] for u in (0, 1)]
    Q = sp.zeros(2**N)
    for i, u in enumerate(policy):
        Q[i, :] = Qs[u][i, :]
    return S, Q


def stationary_column(Q):
    n = Q.rows
    A = Q.T.copy()
    A[n - 1, :] = sp.ones(1, n)
    rhs = sp.zeros(n, 1)
    rhs[n - 1] = 1
    return A.inv() * rhs


def policy_average(N, policy, reward):
    S, Q = policy_generator(N, policy)
    pi = stationary_column(Q)
    return sp.factor(sum(pi[i] * reward(S[i]) for i in range(len(S)))), pi


# ---------------------------------------------------------------------------
# N=1 Bellman data.
# ---------------------------------------------------------------------------
S1, Q10 = action_generator(1, 0)
_, Q11 = action_generator(1, 1)
h1 = sp.Matrix([0, 1])

U1 = sp.factor(b / (b + k))
ell1 = sp.factor(a / (a + 1))
assert U1 == sp.Rational(3, 5)
assert ell1 == sp.Rational(1, 11)

Fup1 = sp.Matrix([0, -1 / (b + k)])
Flo1 = sp.Matrix([0, -1 / (a + 1)])

qU1 = [[sp.factor(h1[i] - (Q * Fup1)[i]) for Q in (Q10, Q11)] for i in range(2)]
qL1 = [[sp.factor(h1[i] - (Q * Flo1)[i]) for Q in (Q10, Q11)] for i in range(2)]

for i in range(2):
    for u in range(2):
        assert qU1[i][u] <= U1
        assert qL1[i][u] >= ell1

slackU1 = [[sp.factor(U1 - qU1[i][u]) for u in range(2)] for i in range(2)]
slackL1 = [[sp.factor(qL1[i][u] - ell1) for u in range(2)] for i in range(2)]

assert slackU1 == [[sp.Rational(2, 5), 0], [0, sp.Rational(8, 5)]]
assert slackL1 == [[0, sp.Rational(2, 11)], [sp.Rational(8, 11), 0]]

# Fixed boundary laws versus adaptive one-site feedback.
p_fixed0 = sp.factor(a / (a + k))
p_fixed1 = sp.factor(b / (1 + b))
assert p_fixed0 == sp.Rational(1, 3)
assert p_fixed1 == sp.Rational(3, 13)
assert ell1 < min(p_fixed0, p_fixed1)
assert U1 > max(p_fixed0, p_fixed1)


# ---------------------------------------------------------------------------
# Enumerate all deterministic N=2 boundary policies exactly.
# Every randomized stationary occupation optimum is attained at a deterministic
# policy for this finite average-reward MDP; enumeration is only used here as
# an exact certificate at the calibration point.
# ---------------------------------------------------------------------------
S2 = states(2)
records = []
for policy in itertools.product((0, 1), repeat=4):
    avg, pi = policy_average(2, policy, lambda s: sp.Integer(s[0]))
    avg_slack_u = sp.factor(
        sum(pi[i] * slackU1[S2[i][0]][S2[i][1]] for i in range(4))
    )
    avg_slack_l = sp.factor(
        sum(pi[i] * slackL1[S2[i][0]][S2[i][1]] for i in range(4))
    )
    records.append((policy, avg, avg_slack_u, avg_slack_l, pi))

U2 = max(r[1] for r in records)
ell2 = min(r[1] for r in records)
min_slack_u = min(r[2] for r in records)
min_slack_l = min(r[3] for r in records)

assert U2 == sp.Rational(3, 8)
assert ell2 == sp.Rational(31, 137)
assert min_slack_u == U1 - U2 == sp.Rational(9, 40)
assert min_slack_l == ell2 - ell1 == sp.Rational(204, 1507)

upper_policies = [r[0] for r in records if r[1] == U2]
lower_policies = [r[0] for r in records if r[1] == ell2]
assert upper_policies == [(1, 0, 0, 1)]
assert lower_policies == [(0, 1, 1, 0)]


# ---------------------------------------------------------------------------
# Exact N=2 Bellman correctors from the optimal deterministic policies.
# We verify the dual inequalities directly.
# ---------------------------------------------------------------------------
Q20 = action_generator(2, 0)[1]
Q21 = action_generator(2, 1)[1]
h2 = sp.Matrix([s[0] for s in S2])

# F=-V where V solves average reward = h + Q^policy V.
Fup2 = -sp.Matrix([0, sp.Rational(45, 128), sp.Rational(345, 128), sp.Rational(235, 128)])
Flo2 = -sp.Matrix([0, sp.Rational(10, 137), sp.Rational(300, 137), sp.Rational(440, 411)])

qU2 = [[sp.factor(h2[i] - (Q * Fup2)[i]) for Q in (Q20, Q21)] for i in range(4)]
qL2 = [[sp.factor(h2[i] - (Q * Flo2)[i]) for Q in (Q20, Q21)] for i in range(4)]

for i in range(4):
    assert max(qU2[i]) == U2
    assert min(qL2[i]) == ell2
    for u in range(2):
        assert qU2[i][u] <= U2
        assert qL2[i][u] >= ell2

# In each cylinder defined by the old rightmost spin, both actions occur as
# tight actions. Therefore the one-spin-interface maximum-principle obstruction
# in the report applies to these exact N=2 correctors.
for boundary_spin in (0, 1):
    tight_upper = set()
    tight_lower = set()
    for i, s in enumerate(S2):
        if s[1] != boundary_spin:
            continue
        for u in (0, 1):
            if qU2[i][u] == U2:
                tight_upper.add(u)
            if qL2[i][u] == ell2:
                tight_lower.add(u)
    assert tight_upper == {0, 1}
    assert tight_lower == {0, 1}


# ---------------------------------------------------------------------------
# Finite exact check of the mismatch lemma for N=1.
# The theorem in the report is analytic for arbitrary N. Here we enumerate
# every deterministic two-site controller and every Boolean target pi(x_0).
# ---------------------------------------------------------------------------
mismatch_bound = sp.factor(rstar / (2 + rstar))
assert mismatch_bound == sp.Rational(1, 21)

for target in itertools.product((0, 1), repeat=2):
    best = None
    for policy, avg, rsu, rsl, pi in records:
        mismatch = sp.factor(
            sum(
                pi[i] * sp.Integer(S2[i][1] != target[S2[i][0]])
                for i in range(4)
            )
        )
        if best is None or mismatch < best:
            best = mismatch
    assert best >= mismatch_bound

print("strict residual rational point: verified")
print("N=1 Bellman endpoints U1=", U1, "ell1=", ell1)
print("N=1 upper/lower Bellman slacks: verified")
print("fixed boundary densities p0=", p_fixed0, "p1=", p_fixed1)
print("adaptive feedback exits fixed-boundary range: verified")
print("N=2 exact endpoints U2=", U2, "ell2=", ell2)
print("upper slack occupation U1-U2 =", min_slack_u)
print("lower slack occupation ell2-ell1 =", min_slack_l)
print("N=2 exact Bellman inequalities: verified")
print("both actions tight in every one-spin interface cylinder: verified")
print("N=1 controller-uniform mismatch lower bound =", mismatch_bound, "verified")
