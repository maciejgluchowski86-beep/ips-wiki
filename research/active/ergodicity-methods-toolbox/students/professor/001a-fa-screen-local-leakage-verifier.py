#!/usr/bin/env python3
"""Exact truth-table checks for FA-SCREEN-001 local leakage patterns.

Convention: 0 is vacancy, 1 occupied. At a site x with neighbours l,r,
a ring with refresh coin z sets x:=z iff l==0 or r==0; otherwise x stays.
"""
from itertools import product


def update(l, x, r, z):
    return z if (l == 0 or r == 0) else x

# Single distinguished vacancy: same screen-side data x=0,r=1,z=1,
# two protected neighbour values give different outputs.
assert update(0, 0, 1, 1) == 1
assert update(1, 0, 1, 1) == 0

# More generally classify all one-ring boundary leakage contexts.
leaks = []
for x, r, z in product((0, 1), repeat=3):
    out0 = update(0, x, r, z)
    out1 = update(1, x, r, z)
    if out0 != out1:
        leaks.append((x, r, z, out0, out1))
assert set(leaks) == {
    (0, 1, 1, 1, 0),  # vacancy tries to fill
    (1, 1, 0, 0, 1),  # occupied site tries to empty
}

# Dimer: protected l, inner a=0, outer b=0. A refresh-to-1 at the
# outer site is legal because a=0 and produces (a,b)=(0,1), independent
# of protected l and farther exterior c.
for l, c in product((0, 1), repeat=2):
    assert update(0, 0, c, 1) == 1  # update b, left neighbour a=0

# From the resulting vulnerable dimer state a=0,b=1, a refresh-to-1 at
# inner a again depends on protected l (right neighbour b=1).
assert update(0, 0, 1, 1) == 1
assert update(1, 0, 1, 1) == 0

# A faithful rule may declare failure at this dangerous mark without
# consulting the protected side. The danger set is exactly: outer
# neighbour=1 and refresh coin differs from current boundary spin.
for x, r, z in product((0, 1), repeat=3):
    dangerous = (r == 1 and z != x)
    depends = update(0, x, r, z) != update(1, x, r, z)
    assert dangerous == depends

print("single-marker leakage contexts:", leaks)
print("00 dimer reaches vulnerable 01 state independently of protected side")
print("danger criterion verified: r=1 and refresh coin differs from boundary spin")
