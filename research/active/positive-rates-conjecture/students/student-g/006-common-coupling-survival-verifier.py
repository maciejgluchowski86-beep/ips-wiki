#!/usr/bin/env python3
"""Exact checks for Student G Assignment 006.

This file checks the finite local algebra used by
006-common-coupling-survival.md. It is not a simulation.

At the strict near-East point
    (a,b,c)=(1/10000,1/100,9999/10000)
it verifies:
1. all 16 pair/right-pair common-uniform transitions satisfy
       L D_i <= -q D_i + c D_{i+1};
2. if D_i=D_{i+1}=0, disagreement cannot be created at i;
3. the two exposed creation probabilities are d=b-a and c;
4. q=1/5000 and the explicit spatially weighted choice z=10000 has
       kappa=q-c/z=10001/100000000>0;
5. the worst short-time single-seed geometry used in the report has
       d/dt E|D_t||_{t=0}=c-q=9997/10000>0.

Only fractions.Fraction is used.
"""

from fractions import Fraction as F


A = ("00", "11", "01", "10")


def bits(pair):
    return int(pair[0]), int(pair[1])


def disagrees(pair):
    return pair in ("01", "10")


a = F(1, 10000)
b = F(1, 100)
c = F(9999, 10000)
d = b - a
q = 1 - c + a

rates = {
    (0, 0): a,
    (0, 1): b,
    (1, 0): c,
    (1, 1): F(0),
}


def disagreement_probability(beta, gamma):
    """Post-update disagreement probability at the middle site."""
    x, y = bits(beta)
    u, v = bits(gamma)
    return abs(rates[(x, u)] - rates[(y, v)])


# Exact local additive drift inequality.
for beta in A:
    for gamma in A:
        Di = F(int(disagrees(beta)))
        Dip1 = F(int(disagrees(gamma)))
        local_drift = disagreement_probability(beta, gamma) - Di
        rhs = -q * Di + c * Dip1
        assert local_drift <= rhs, (beta, gamma, local_drift, rhs)

        if not disagrees(beta) and not disagrees(gamma):
            assert disagreement_probability(beta, gamma) == 0

# At an exposed edge, common child 0 creates at rate d and common child 1
# creates at rate c, independently of the parent orientation.
for parent in ("01", "10"):
    assert disagreement_probability("00", parent) == d
    assert disagreement_probability("11", parent) == c

assert q == F(1, 5000)
assert d == F(99, 10000)

z = F(10000)
kappa = q - c / z
assert kappa == F(10001, 100000000)
assert kappa > 0

# Single disagreement at 0, right common 0, left common 1:
# source coalescence contributes -q and child creation contributes +c.
initial_hamming_derivative = c - q
assert initial_hamming_derivative == F(9997, 10000)
assert initial_hamming_derivative > 0

print("16 local additive drift inequalities: verified")
print("no spontaneous disagreement from two agreed local pairs: verified")
print("exposed creation rates d and c: verified")
print("q =", q)
print("z =", z, "kappa=q-c/z =", kappa)
print("short-time single-seed Hamming derivative =", initial_hamming_derivative)
