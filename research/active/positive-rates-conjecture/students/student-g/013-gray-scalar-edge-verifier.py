#!/usr/bin/env python3
"""Exact finite checks for Assignment 013 Gray scalar-edge obstruction."""
from fractions import Fraction as Q
from itertools import product

def scalar_closure(F):
    f00,f01,f10,f11=F
    return f01 in (f00,f11) and f10 in (f00,f11)

def monotone(F):
    f00,f01,f10,f11=F
    return f00<=f01<=f11 and f00<=f10<=f11

def flip_vector(F):
    xs=(0,0,1,1)
    return tuple(int(F[k]!=xs[k]) for k in range(4))

all_maps=list(product((0,1), repeat=4))
closure_maps=[F for F in all_maps if scalar_closure(F)]
assert len(closure_maps)==10
no_source_crossing=[F for F in closure_maps if not (F[0]==1 and F[3]==0)]
monotone_maps=[F for F in all_maps if monotone(F)]
assert len(monotone_maps)==6
assert set(no_source_crossing)==set(monotone_maps)
for F in closure_maps:
    v=flip_vector(F)
    assert v[3] <= v[0]+v[1]+v[2]

a=Q(1,10000); b=Q(1,100); c=Q(9999,10000)
delta0=1-c; delta1=Q(1)
lam=(a,b,delta0,delta1)
assert lam[0]+lam[1]+lam[2]==Q(51,5000)
assert lam[3] > lam[0]+lam[1]+lam[2]
assert a<=b and not (delta1<=delta0)
assert delta1-delta0==c

even=(b,a,delta1,delta0)
odd=(delta0,delta1,a,b)
assert not (even[0]<=even[1])
assert even[3]<=even[2]
assert odd[0]<=odd[1]
assert not (odd[3]<=odd[2])
assert b-a==Q(99,10000)

# Attractive sanity point.
aA,bA,cA=Q(1,4),Q(1,2),Q(0)
d0A,d1A=1-cA,Q(1)
assert aA<=bA and d1A<=d0A
assert (aA,bA-aA,d1A,d0A-d1A)==(Q(1,4),Q(1,4),Q(1),Q(0))

# Repulsive sanity point after checkerboard transform.
aR,bR,cR=Q(1,2),Q(1,4),Q(1,2)
d0R,d1R=1-cR,Q(1)
evenR=(bR,aR,d1R,d0R)
oddR=(d0R,d1R,aR,bR)
assert evenR[0]<=evenR[1] and evenR[3]<=evenR[2]
assert oddR[0]<=oddR[1] and oddR[3]<=oddR[2]

print('ordinary scalar-closure Boolean maps:',len(closure_maps))
print('closure maps without local extremal-source crossing:',len(no_source_crossing))
print('monotone Boolean maps:',len(monotone_maps))
print('classes agree:',set(no_source_crossing)==set(monotone_maps))
print('P_h ordinary closure rate gate: 1 >',lam[0]+lam[1]+lam[2])
print('P_h ordinary order defect c =',c)
print('P_h checkerboard order defect b-a =',b-a)
print('attractive and repulsive sanity points verified exactly')
