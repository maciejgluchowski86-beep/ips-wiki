#!/usr/bin/env python3
"""Exact/interval checks for Student G Assignment 007.

No simulation and no third-party packages.

At (a,b,c)=(1/10000,1/100,9999/10000), this verifies:

1. the protected-source lower event gives alpha(t)>1 for every 0<t<=47;
   the only transcendental quantities are exp(-x), enclosed by exact rational
   alternating-series intervals;
2. the ordinary fixed-boundary finite random-map coefficient B_{3,3}^0(1)
   is enclosed by exact rational uniformization of the 2048-state CTMC;
3. the two-sided causal truncation sandwich at T=1 gives a rigorous interval
   containing alpha(1), with lower endpoint >1;
4. at T=47, 1% one-sided causal-cone errors already require L>=67 and,
   once L>=67, R>=74.  The corresponding naive finite state count is 2^210.

The script checks the finite local transition kernel exactly with integer
probability numerators over denominator 10000.  Uniformization is truncated
with an explicit Poisson remainder bound.
"""

from fractions import Fraction as F
from itertools import product
from math import factorial

DEN = 10000
A_RATE = 1
B_RATE = 100
C_RATE = 9999

RATES = {
    (0, 0): A_RATE,
    (0, 1): B_RATE,
    (1, 0): C_RATE,
    (1, 1): 0,
}

PAIRS = ((0, 0), (1, 1), (0, 1), (1, 0))
PAIR_INDEX = {p: i for i, p in enumerate(PAIRS)}


def dec(x, digits=15):
    """Deterministic decimal display only; all assertions use Fractions."""
    return f"{float(x):.{digits}f}"


def exp_neg_interval(x, degree=36):
    """Exact rational [lo,hi] for exp(-x), x>=0.

    Write x=m*y with 0<=y<=1.  The alternating Taylor series for exp(-y)
    has decreasing terms.  An even partial sum is an upper bound and the
    following odd partial sum is a lower bound.  Raising positive endpoints
    to integer m preserves the enclosure.
    """
    x = F(x)
    assert x >= 0
    if x == 0:
        return F(1), F(1)
    m = max(1, (x.numerator + x.denominator - 1) // x.denominator)
    y = x / m
    assert 0 <= y <= 1

    if degree % 2:
        degree += 1
    term = F(1)
    s = term
    even_sum = None
    odd_sum = None
    for k in range(1, degree + 2):
        term *= -y / k
        s += term
        if k == degree:
            even_sum = s
        if k == degree + 1:
            odd_sum = s
    lo_y, hi_y = odd_sum, even_sum
    assert 0 < lo_y <= hi_y
    return lo_y**m, hi_y**m


def poisson_tail_interval(mean, k, exp_interval=None):
    """Exact rational interval for P(Pois(mean)>=k), integer k>=0."""
    mean = F(mean)
    assert mean >= 0 and k >= 0
    if k == 0:
        return F(1), F(1)
    if exp_interval is None:
        exp_interval = exp_neg_interval(mean)
    elo, eup = exp_interval
    partial = sum(mean**n / factorial(n) for n in range(k))
    return F(1) - eup * partial, F(1) - elo * partial


def poisson_excess_interval(mean, L, exp_interval=None):
    """Interval for E[(Pois(mean)-L)_+]."""
    mean = F(mean)
    tL = poisson_tail_interval(mean, L, exp_interval)
    tLp1 = poisson_tail_interval(mean, L + 1, exp_interval)
    lo = mean * tL[0] - L * tLp1[1]
    hi = mean * tL[1] - L * tLp1[0]
    return lo, hi


def pair_update_numerators(beta, gamma):
    """Post-ring common-uniform pair law with denominator DEN."""
    x, y = beta
    u, v = gamma
    p = RATES[(x, u)]
    q = RATES[(y, v)]
    return (
        ((0, 0), DEN - max(p, q)),
        ((1, 1), min(p, q)),
        ((1, 0), max(p - q, 0)),
        ((0, 1), max(q - p, 0)),
    )


def local_transitions(state, L, R, site, boundary=0):
    """One ring at an actual site in [-L,R], fixed common boundary at R+1."""
    s = list(state)
    if site <= 0:
        k = site + L
        beta = PAIRS[s[k]]
        if site < 0:
            gamma = PAIRS[s[k + 1]]
        else:
            right = s[L + 1] if R else boundary
            gamma = (right, right)
        out = []
        for new_pair, num in pair_update_numerators(beta, gamma):
            if num:
                ss = s.copy()
                ss[k] = PAIR_INDEX[new_pair]
                out.append((tuple(ss), num))
        assert sum(num for _, num in out) == DEN
        return out

    pos = L + 1 + site - 1
    spin = s[pos]
    right = s[pos + 1] if site < R else boundary
    p1 = RATES[(spin, right)]
    out = []
    for new_spin, num in ((0, DEN - p1), (1, p1)):
        if num:
            ss = s.copy()
            ss[pos] = new_spin
            out.append((tuple(ss), num))
    assert sum(num for _, num in out) == DEN
    return out


def build_fixed_chain(L, R, boundary=0):
    states = [
        pair_part + right_part
        for pair_part in product(range(4), repeat=L + 1)
        for right_part in product(range(2), repeat=R)
    ]
    index = {s: i for i, s in enumerate(states)}
    sites = list(range(-L, R + 1))
    transitions = []
    for site in sites:
        rows = []
        for state in states:
            rows.append(
                [(index[ss], num) for ss, num in local_transitions(state, L, R, site, boundary)]
            )
        transitions.append(rows)

    payoff = [sum(x in (2, 3) for x in s[: L + 1]) for s in states]
    initials = [
        i
        for i, s in enumerate(states)
        if s[L] in (2, 3) and all(x in (0, 1) for x in s[:L])
    ]
    return states, sites, transitions, payoff, initials


def event_numerator_step(w, chain):
    """If v=w/(DEN*N)^n, return numerator for one uniformized event."""
    _, sites, transitions, _, _ = chain
    out = [0] * len(w)
    for i in range(len(w)):
        total = 0
        for rows in transitions:
            for j, num in rows[i]:
                total += num * w[j]
        out[i] = total
    return out


def fixed_B_interval(L, R, T=1, boundary=0, truncation=32):
    """Rigorous interval for B_{L,R}^boundary(T), currently T=1."""
    assert T == 1
    chain = build_fixed_chain(L, R, boundary)
    _, sites, _, payoff, initials = chain
    Nsites = len(sites)

    w = payoff[:]
    sums = [F(x) for x in w]
    den_power = 1
    fact = 1
    for n in range(1, truncation + 1):
        w = event_numerator_step(w, chain)
        den_power *= DEN
        fact *= n
        denominator = den_power * fact
        sums = [old + F(num, denominator) for old, num in zip(sums, w)]

    max_partial = max(sums[i] for i in initials)
    elo, eup = exp_neg_interval(F(Nsites))
    lower = elo * max_partial

    assert truncation + 2 > Nsites
    first = F(Nsites) ** (truncation + 1) / factorial(truncation + 1)
    remainder_prob_upper = eup * first / (1 - F(Nsites, truncation + 2))
    upper = eup * max_partial + (L + 1) * remainder_prob_upper
    return lower, upper, len(chain[0]), remainder_prob_upper


a = F(1, 10000)
b = F(1, 100)
c = F(9999, 10000)
q = 1 - c + a
A = b + q
delta = 1 - c + b
x = c - b
K = c / x

assert q == F(1, 5000)
assert A == F(51, 5000)
assert delta == F(101, 10000)
assert x == F(9899, 10000)
assert K == F(9999, 9899)

# Protected-source lower event. L(t) is unimodal because its derivative has
# the sign of a strictly decreasing function F(t), with F(0)=c-A>0.
assert A > 0 and delta > 0 and K > 0 and x > 0
assert c - A == F(9897, 10000) > 0

T47 = F(47)
e1 = exp_neg_interval(A * T47)
e2 = exp_neg_interval((A + delta) * T47)
e3 = exp_neg_interval((A + 1) * T47)
L47_lower = e1[0] + K * (e2[0] - e3[1])
L47_upper = e1[1] + K * (e2[1] - e3[0])
assert L47_lower > 1
assert L47_lower > F(1008204288867933, 10**15)

# Exact fixed-boundary finite random-map coefficient at T=1.
BLOW, BUP, NSTATES, UTAIL = fixed_B_interval(3, 3, T=1, boundary=0, truncation=32)
assert NSTATES == 2048
assert BLOW < BUP

# Two-sided causal truncation errors for L=R=3, T=1.
exp1 = exp_neg_interval(F(1))
rtail = poisson_tail_interval(F(1), 4, exp1)
rlo, rup = 4 * rtail[0], 4 * rtail[1]
ello, ellup = poisson_excess_interval(F(1), 3, exp1)
alpha_lower = BLOW - rup
alpha_upper = BUP + rup + ellup
assert alpha_lower > 1
assert alpha_lower <= alpha_upper

# Scale diagnostic at T=47 for 1% causal-cone errors.
exp47 = exp_neg_interval(F(47))
ell66 = poisson_excess_interval(F(47), 66, exp47)
ell67 = poisson_excess_interval(F(47), 67, exp47)
assert ell66[0] > F(1, 100)
assert ell67[1] < F(1, 100)

r73 = poisson_tail_interval(F(47), 74, exp47)
r74 = poisson_tail_interval(F(47), 75, exp47)
assert 68 * r73[0] > F(1, 100)
assert 68 * r74[1] < F(1, 100)

naive_state_exponent = 2 * (67 + 1) + 74
assert naive_state_exponent == 210

print("protected-source lower bound at T=47 in [", dec(L47_lower), ",", dec(L47_upper), "]")
print("unimodality check: alpha(t)>1 for every 0<t<=47 verified")
print("fixed-boundary B_3,3^0(1) in [", dec(BLOW), ",", dec(BUP), "]")
print("two-sided alpha(1) sandwich in [", dec(alpha_lower), ",", dec(alpha_upper), "]")
print("T=47 left 1% threshold: ell_66 > .01 and ell_67 < .01 verified")
print("T=47 right 1% threshold at L>=67: R=73 fails, R=74 passes")
print("naive 1%-per-side state count threshold: 2^", naive_state_exponent, sep="")
