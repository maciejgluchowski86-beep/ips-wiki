#!/usr/bin/env python3
"""Exact checks for Assignment 011 distinguished-zero transfer.

The normalized simple-IPS random-map convention used by the programme is:
at each rate-one ring, a site currently in state x with right neighbour y is
reset to 1 with probability r[x,y].  On r11=0 we write

    r00=a, r01=b, r10=c, r11=0.

This script verifies symbolically the depth-1/depth-2 prefix incompatibility
and exactly checks the hard point

    P_h = (a,b,c) = (1/10000, 1/100, 9999/10000).

It also checks the first three fixed-width release-prefix gates at P_h:
append only (pi_1 versus the left prefix of pi_2), one-site boundary-layer
release (pi_2 versus pi_3 on the untouched first site), and two-site
boundary-layer release (pi_3 versus pi_4 on the untouched first site).
"""

from itertools import product
import sympy as sp


a, b, c = sp.symbols("a b c")


def reset_one_prob(x, y, aa, bb, cc):
    return {
        (0, 0): aa,
        (0, 1): bb,
        (1, 0): cc,
        (1, 1): sp.Integer(0),
    }[(x, y)]


def generator(n, aa, bb, cc):
    states = list(product((0, 1), repeat=n))
    index = {state: i for i, state in enumerate(states)}
    qmat = sp.zeros(len(states), len(states))
    for state in states:
        i = index[state]
        for site in range(n):
            x = state[site]
            y = state[site + 1] if site + 1 < n else 0
            p1 = reset_one_prob(x, y, aa, bb, cc)
            flip_rate = p1 if x == 0 else 1 - p1
            new_state = list(state)
            new_state[site] = 1 - x
            new_state = tuple(new_state)
            qmat[i, index[new_state]] += flip_rate
            qmat[i, i] -= flip_rate
    return states, qmat


def stationary(n, aa, bb, cc):
    states, qmat = generator(n, aa, bb, cc)
    size = len(states)
    amat = qmat.T.copy()
    rhs = sp.zeros(size, 1)
    amat[size - 1, :] = sp.ones(1, size)
    rhs[size - 1] = 1
    vec = amat.inv() * rhs
    assert all(sp.factor(x) >= 0 for x in vec) if all(
        z.is_number for z in (aa, bb, cc)
    ) else True
    assert sp.factor(sum(vec) - 1) == 0
    return states, [sp.factor(x) for x in vec]


# Symbolic pi_1.
pi1_one = sp.factor(a / (a + 1 - c))

# Symbolic pi_2 by direct stationarity equations.
states2, q2 = generator(2, a, b, c)
p00, p01, p10, p11 = sp.symbols("p00 p01 p10 p11")
prow = sp.Matrix([[p00, p01, p10, p11]])
eqs = list((prow * q2).reshape(4, 1)) + [p00 + p01 + p10 + p11 - 1]
sol = sp.solve(eqs, (p00, p01, p10, p11), dict=True, simplify=True)[0]

left_pi2_one = sp.factor(sol[p10] + sol[p11])
prefix_difference = sp.factor(left_pi2_one - pi1_one)
expected_difference = sp.factor(
    -2 * a * (a - b * (1 - c))
    / (
        (a + 1 - c)
        * (2 * a * b - a * c + 3 * a - b * c + b + c**2 - 3 * c + 2)
    )
)
assert sp.factor(prefix_difference - expected_difference) == 0

# Since a>0 in the residual chamber, exact one-move prefix compatibility has
# the symbolic locus a=b(1-c), apart from singular/zero-rate degeneracies.
assert sp.factor(sp.together(prefix_difference).as_numer_denom()[0]) == -2 * a * (
    a + b * c - b
)

# Hard point exact values.
ah = sp.Rational(1, 10000)
bh = sp.Rational(1, 100)
ch = sp.Rational(9999, 10000)
assert pi1_one.subs({a: ah, b: bh, c: ch}) == sp.Rational(1, 2)

hard_pi2 = {
    key: sp.factor(value.subs({a: ah, b: bh, c: ch})) for key, value in sol.items()
}
assert hard_pi2[p00] == sp.Rational(20101, 60604)
assert hard_pi2[p01] == sp.Rational(30001, 60604)
assert hard_pi2[p10] == sp.Rational(10201, 60604)
assert hard_pi2[p11] == sp.Rational(301, 60604)
assert left_pi2_one.subs({a: ah, b: bh, c: ch}) == sp.Rational(5251, 30302)
assert prefix_difference.subs({a: ah, b: bh, c: ch}) == -sp.Rational(4950, 15151)

# Fixed-width exact release can never repair the marginal of an untouched
# prefix.  The first three maximal-boundary-layer tests at P_h already fail.
left_one = {}
for n in range(1, 5):
    states, pi = stationary(n, ah, bh, ch)
    left_one[n] = sp.factor(sum(prob for state, prob in zip(states, pi) if state[0] == 1))

assert left_one[1] == sp.Rational(1, 2)
assert left_one[2] == sp.Rational(5251, 30302)
assert left_one[3] == sp.Rational(11370875388409, 108705150384068)
assert left_one[4] == sp.Rational(
    78409794768042325663808452851130987,
    381758660287521745898004222070796774,
)
assert left_one[2] - left_one[1] == -sp.Rational(4950, 15151)
assert left_one[3] - left_one[2] == -sp.Rational(
    7466519657025, 108705150384068
)
assert left_one[4] - left_one[3] == sp.Rational(
    76953453677050193761435735134480075,
    763517320575043491796008444141593548,
)

print("symbolic one-move prefix difference:", prefix_difference)
print("compatibility locus in the positive-rate chamber: a = b(1-c)")
print("P_h pi_1(1) =", sp.Rational(1, 2))
print("P_h bar pi_2(1) =", sp.Rational(5251, 30302))
print("P_h difference =", -sp.Rational(4950, 15151))
print("fixed-width untouched-prefix gates through pi_4: all nonzero")
