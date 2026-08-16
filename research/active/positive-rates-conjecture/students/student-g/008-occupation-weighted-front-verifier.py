#!/usr/bin/env python3
from fractions import Fraction as F

# Hard near-East point.
a = F(1, 10000)
b = F(1, 100)
c = F(9999, 10000)
g = b - a
k = 1 - c
q = 1 - c + a

# Exact one-source-episode comparison from G002/G003.
Den = (b + q) * (1 + q) - a * k
h0 = (g * (1 + q) + a * c) / Den
h1 = (c * (b + q) + k * g) / Den

assert q == F(1, 5000)
assert g == F(99, 10000)
assert k == F(1, 10000)
assert Den == F(1020203, 100000000)
assert h0 == F(1000197, 1020203)
assert h1 == F(1019997, 1020203)
assert F(1, 2) < h0 < h1 < 1
assert 1 - h0 == F(20006, 1020203)
assert 1 - h1 == F(206, 1020203)

# First-step equations for one D episode killed at the exact comparison rate q.
# Common target spin 0: 0->1 at a, child at g, source kill at q.
# Common target spin 1: 1->0 at k, child at c, source kill at q.
assert (b + q) * h0 == g + a * h1
assert (1 + q) * h1 == c + k * h0

# Actual-history non-Markov gap after a source coalescence to common zero.
# If the hidden right neighbour is coupled, no source re-entry is possible.
# If it is disagreeing, the source clock beats that neighbour's clock with
# probability 1/2 and then creates disagreement with mark measure g.
reentry_gap = g / 2
assert reentry_gap == F(99, 20000)

# A.s.-finite but unbounded distinct source episodes are already fatal without
# a quantitative tail: N q-killed episodes have failure at most (1-h0)^N.
def finite_episode_failure(N: int) -> F:
    return (1 - h0) ** N

assert 1 - finite_episode_failure(4) > F(999999, 1000000)
assert 1 - finite_episode_failure(5) > F(99999999, 100000000)

# Stronger recursive finite-depth state-only closure.  After a failed local
# episode, a depth-(n-1) hidden return mechanism may recreate the source; once
# it does, the projected Bellman state has reset, so the continuation value is
# again r_n.  Thus r_n = h0 + (1-h0) r_{n-1} r_n.
def rnext(r: F) -> F:
    return h0 / (1 - (1 - h0) * r)

rs = [h0]
for _ in range(8):
    rs.append(rnext(rs[-1]))

for n in range(1, len(rs)):
    assert rs[n] > rs[n-1]
    assert rs[n] < 1
    assert rs[n] == h0 + (1 - h0) * rs[n-1] * rs[n]

ratio = (1 - h0) / h0
assert ratio == F(20006, 1000197)
assert ratio < F(1, 49)
for n, r in enumerate(rs):
    assert 1 - r <= ratio ** (n + 1)

# Concrete thresholds and the general positive-weight obstruction.
assert rs[1] > F(9996, 10000)
assert rs[2] > F(99999, 100000)
assert rs[3] > F(9999998, 10000000)

for theta in [F(9,10), F(99,100), F(999,1000), F(999999,1000000),
              F(999999999,1000000000), F(999999999999999,10**15)]:
    r = h0
    n = 0
    while r <= theta:
        r = rnext(r)
        n += 1
    assert r > theta

print('q =', q)
print('g =', g)
print('single-episode h0 =', h0, '=', f'{float(h0):.15f}')
print('single-episode h1 =', h1, '=', f'{float(h1):.15f}')
print('actual C0 hidden-ancestry re-entry gap >=', reentry_gap, '=', f'{float(reentry_gap):.8f}')
print('deficit contraction ratio (1-h0)/h0 =', ratio, '=', f'{float(ratio):.15f}')
for n in range(5):
    print(f'depth {n}: 1-r_n = {float(1-rs[n]):.18e}; r_n = {float(rs[n]):.15f}')
print('zero-frequency finite-depth closed two-spin envelope: contraction-factor supremum = 1')
