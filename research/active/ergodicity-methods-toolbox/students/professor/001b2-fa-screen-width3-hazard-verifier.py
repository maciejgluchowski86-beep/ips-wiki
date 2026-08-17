#!/usr/bin/env python3
"""Exact width<=3 active-vacancy hazard for FA-SCREEN-001.

A screen-side state is active only if one of sites 1,2,3 is a certified
vacancy.  We prescribe four one-unit phases, freezing site 3 throughout.
By phase 3, site 1 is vacant for the entire phase, so the protected endpoint
(site 0) is legal and its unrevealed refresh marks can leave it either 0 or 1.
Phase 4 is then a site-1 refresh-to-1 with site 2 occupied, whose outcome
therefore depends on that hidden protected value.
"""
from fractions import Fraction as F
from itertools import product


def update(l, x, r, z):
    return z if (l == 0 or r == 0) else x


def apply_screen_action(state, action):
    """Apply the unique prescribed ring; site 3 has no rings in every phase.

    state=(x1,x2,x3).  Only actions at sites 1 or 2 occur.  For site 1 we
    use protected neighbour 1 merely to verify screen-side legality when it
    is supposed to be exterior-certified; the final dangerous action is not
    applied here.  Site 2 uses its common neighbours x1,x3.
    """
    x1,x2,x3=state
    if action is None:
        return state
    i,z=action
    if i==1:
        # The only non-final site-1 action is used when x2=0, hence legal
        # independently of the protected neighbour.
        assert x2==0
        x1=z
    elif i==2:
        assert x1==0 or x3==0
        x2=z
    else:
        raise ValueError(i)
    return (x1,x2,x3)


def prescription(state):
    x1,x2,x3=state
    assert 0 in state
    # Four phases. Phase 4 is always the dangerous site-1 coin=1 and is
    # checked separately after phase 3.
    if x1==0 and x2==1:
        return [None, None, None]
    if x1==0 and x2==0:
        return [None, None, (2,1)]
    if x1==1 and x2==0:
        return [None, (1,0), (2,1)]
    # Only remaining active state has x1=x2=1 and x3=0.
    assert (x1,x2,x3)==(1,1,0)
    return [(2,0),(1,0),(2,1)]

active=[]
for state in product((0,1), repeat=3):
    if 0 not in state:
        continue
    active.append(state)
    s=state
    actions=prescription(state)
    for k,a in enumerate(actions, start=1):
        s=apply_screen_action(s,a)
        if k==3:
            # During phase 3 there is no site-1 ring and x1 is already 0;
            # hence site 0 is legal throughout that phase.
            assert s[0]==0
    # At start of phase 4, x1=0,x2=1. A site-1 coin=1 is dangerous:
    # protected neighbour 0 -> 1, protected neighbour 1 -> stays 0.
    assert s[0:2]==(0,1)
    assert update(0,0,1,1)==1
    assert update(1,0,1,1)==0

assert len(active)==7

# Probability lower bound. Each of four phases specifies either no rings on
# sites 1,2,3 or exactly one ring at one prescribed site and no rings at the
# other two. Poisson factor = exp(-12). The worst coin factor is q^2 p^2.
# Use e<49/18<11/4 and (11/4)^12<200000.
e_upper=F(49,18)
assert e_upper < F(11,4)
assert F(11,4)**12 < 200000
q=F(1,10); p=1-q
delta=q*q*p*p/F(200000)
assert delta==F(81,2000000000)
assert delta>0

print("active width-3 states checked:", len(active))
print("all reach a full phase with x1=0, then dangerous state (x1,x2)=(0,1)")
print("exact bound: exp(-12)>1/200000")
print("at q=1/10, four-phase exterior hazard probability >", delta)
