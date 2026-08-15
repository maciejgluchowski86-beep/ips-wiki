#!/usr/bin/env python3
"""
Exact verifier for Graduate Student C assignment 001.

Uses only the Python standard library. All transition probabilities are Fractions.

State convention:
- block sites are 0 (left) and 1 (right), exterior site is 2;
- a coupled-site state is a pair (zeta, xi);
- transient states have site 0 agreed and site 1 disagreed;
- crossing absorption occurs when an update of site 0 creates disagreement;
- regeneration absorption occurs when an update of site 1 restores agreement.

The embedded chain observes successive clock rings in the two-site block. Since
both clocks have rate one, each ring is at site 0 or site 1 with probability 1/2.
"""

from fractions import Fraction
from math import sqrt
from itertools import product

OFF = ((0, 1), (1, 0))
DIAG = ((0, 0), (1, 1))
TRANSIENT = tuple((a, bc) for a in (0, 1) for bc in OFF)
INDEX = {s: i for i, s in enumerate(TRANSIENT)}


def canonical_pair(p, q):
    """Canonical coupling of Bernoulli(p) and Bernoulli(q), exactly."""
    return {
        (0, 0): 1 - max(p, q),
        (1, 1): min(p, q),
        (0, 1): max(q - p, Fraction(0)),
        (1, 0): max(p - q, Fraction(0)),
    }


def solve_fraction(A, b):
    """Gauss-Jordan solve over Fractions."""
    n = len(b)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if M[i][col] != 0)
        M[col], M[pivot] = M[pivot], M[col]
        z = M[col][col]
        M[col] = [x / z for x in M[col]]
        for i in range(n):
            if i == col:
                continue
            z = M[i][col]
            if z:
                M[i] = [M[i][j] - z * M[col][j] for j in range(n + 1)]
    return [M[i][-1] for i in range(n)]


def build_killed_kernel(r, exterior=(0, 1)):
    """
    Return K, x, y for the two-site killed excursion.

    r[(x,y)] = P(1 | x y).
    K is the transient-to-transient embedded kernel.
    x is one-step crossing absorption probability.
    y is one-step regeneration absorption probability.
    """
    K = [[Fraction(0) for _ in TRANSIENT] for _ in TRANSIENT]
    x = [Fraction(0) for _ in TRANSIENT]
    y = [Fraction(0) for _ in TRANSIENT]
    e, f = exterior

    for i, (a, bc) in enumerate(TRANSIENT):
        b, c = bc

        # Site 0 updates. Off-diagonal output means disagreement crossed.
        out = canonical_pair(r[(a, b)], r[(a, c)])
        for pair, prob in out.items():
            prob /= 2
            if pair in OFF:
                x[i] += prob
            else:
                K[i][INDEX[(pair[0], bc)]] += prob

        # Site 1 updates. Diagonal output means the block regenerated.
        out = canonical_pair(r[(b, e)], r[(c, f)])
        for pair, prob in out.items():
            prob /= 2
            if pair in DIAG:
                y[i] += prob
            else:
                K[i][INDEX[(a, pair)]] += prob

    return K, x, y


def crossing_probabilities(r, exterior=(0, 1)):
    K, x, y = build_killed_kernel(r, exterior)
    n = len(TRANSIENT)
    I_minus_K = [
        [Fraction(int(i == j)) - K[i][j] for j in range(n)]
        for i in range(n)
    ]
    h = solve_fraction(I_minus_K, x)
    return K, x, y, h


def attack_crossing_probability(r, full_block, exterior=(0, 1)):
    """
    One boundary attack: condition on a clock ring at site 1 while the block
    is fully agreed. If this ring leaves the block agreed, the attempt ends
    as regeneration; otherwise follow the killed excursion.
    """
    left, right = full_block
    _, _, _, h = crossing_probabilities(r, exterior)
    e, f = exterior
    out = canonical_pair(r[(right, e)], r[(right, f)])
    total = Fraction(0)
    for pair, prob in out.items():
        if pair in OFF:
            total += prob * h[INDEX[(left, pair)]]
    return total


def residual_path(eps):
    # Strictly inside the unresolved wedge for all sufficiently small eps:
    # r11=0, r10=1-eps^2, r01=eps/2, r00=eps.
    return {
        (0, 0): eps,
        (0, 1): eps / 2,
        (1, 0): 1 - eps * eps,
        (1, 1): Fraction(0),
    }


def closed_form_attack(eps):
    # Exact F_2(eps) from the report, starting from agreed 11 and exterior 01.
    num = 2 * (1 - eps * eps) * (3 + 2 * eps - 2 * eps * eps - 2 * eps**3)
    den = 6 + 7 * eps + 6 * eps * eps + 4 * eps**3
    return num / den


def closed_form_h1(eps):
    num = 2 * (3 + 2 * eps - 2 * eps * eps - 2 * eps**3)
    den = 6 + 7 * eps + 6 * eps * eps + 4 * eps**3
    return num / den


def residual_two_state_spectral_radius(eps):
    # K on states (0;10),(1;10); exact algebraic Perron root evaluated numerically.
    e = float(eps)
    return (
        3 - 2 * e - 2 * e * e
        + sqrt((1 - e) ** 2 + 2 * e**3)
    ) / 4


def main():
    for eps in (Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)):
        r = residual_path(eps)
        K, x, y, h = crossing_probabilities(r, (0, 1))

        # Exact stochastic bookkeeping.
        for i in range(len(TRANSIENT)):
            assert sum(K[i]) + x[i] + y[i] == 1

        F = attack_crossing_probability(r, (1, 1), (0, 1))
        assert F == closed_form_attack(eps)

        # Entry state after a successful attack is (left common 1, right 10).
        assert h[INDEX[(1, (1, 0))]] == closed_form_h1(eps)

        # Both exterior orientations agree by copy-label symmetry.
        assert F == attack_crossing_probability(r, (1, 1), (1, 0))

        all_attacks = [
            (attack_crossing_probability(r, full, ext), full, ext)
            for full in product((0, 1), repeat=2)
            for ext in OFF
        ]
        worst = max(all_attacks)

        print(f"eps={eps}")
        print(f"  h_entry = {h[INDEX[(1, (1, 0))]]} = {float(h[INDEX[(1, (1, 0))]]):.12f}")
        print(f"  F2       = {F} = {float(F):.12f}")
        print(f"  worst    = {worst[0]} at full={worst[1]}, ext={worst[2]}")
        print(f"  rho(K10) = {residual_two_state_spectral_radius(eps):.12f}")
        print()

    print("all exact checks passed")


if __name__ == "__main__":
    main()
