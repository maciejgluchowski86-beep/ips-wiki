#!/usr/bin/env python3
"""Finite exact checks for the FA-SCREEN fixed-boundary scaling obstruction.

The analytic proof compares two FA boundary updates with the protected neighbour
fixed to 0 versus 1, under identical screen-side state and graphical marks.
From every common state (x1,x2) a three-unit prescribed event causes the first
boundary discrepancy. The Poisson factor is exp(-6); this script checks the
state logic and an exact rational lower bound exp(-6)>1/500 via e<11/4.
"""
from fractions import Fraction as F
from itertools import product


def upd(l, x, r, z):
    return z if (l == 0 or r == 0) else x


def ring(state0, state1, site, coin):
    """Update sites 1 or 2 in two copies; protected site 0 is 0/1 respectively.

    We only track (x1,x2). Site 3 is irrelevant for the prescribed sequences:
    every site-2 update used below is legal because x1=0.
    """
    a0, b0 = state0
    a1, b1 = state1
    if site == 1:
        a0 = upd(0, a0, b0, coin)
        a1 = upd(1, a1, b1, coin)
    elif site == 2:
        # Every prescribed site-2 ring is used when x1=0 in both copies,
        # so legality is guaranteed independently of site 3.
        assert a0 == a1 == 0
        b0 = coin
        b1 = coin
    else:
        raise ValueError(site)
    return (a0, b0), (a1, b1)


# Prescribed three one-unit phases for each common initial (x1,x2).
# None = no rings at sites 1,2 in that phase.
def prescription(x1, x2):
    if x2 == 1:
        return [None, None, (1, 1-x1)]
    if x1 == 0:  # x2=0
        return [None, (2, 1), (1, 1)]
    return [(1, 0), (2, 1), (1, 1)]

for x1, x2 in product((0, 1), repeat=2):
    s0 = (x1, x2)
    s1 = (x1, x2)
    for action in prescription(x1, x2):
        if action is not None:
            s0, s1 = ring(s0, s1, *action)
    assert s0[0] != s1[0], (x1, x2, s0, s1)

# Exact elementary bound e < 11/4:
# e = 1+1+1/2+1/6+sum_{n>=4}1/n!
# and tail <= (1/24) sum_{k>=0} (1/4)^k = 1/18.
e_upper = F(1)+F(1)+F(1,2)+F(1,6)+F(1,18)
assert e_upper == F(49,18)
assert e_upper < F(11,4)
assert F(11,4)**6 < 500
# Hence exp(-6)>1/500.

# Low-q stress point used for the route-level obstruction.
q = F(1,10)
p = 1-q
delta_rational = q*p*p/F(500)
assert delta_rational == F(81,500000)
assert delta_rational > 0

print("all four common (x1,x2) states forced to boundary discrepancy in 3 phases")
print("exact bound: e < 49/18 < 11/4 and (11/4)^6 < 500, hence exp(-6) > 1/500")
print("at q=1/10, each 3-unit block has conditional failure probability >", delta_rational)
