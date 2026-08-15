#!/usr/bin/env python3
"""
Exact symbolic persistence check for Graduate Student C assignment 001.

Requires sympy. It constructs the full length-three killed embedded chain along
    r11=0, r10=1-e^2, r01=e/2, r00=e,
valid for 0<e<1/2 (ordering r10>r00>r01>r11), with exterior disagreement 01.
Transient states have site 0 agreed and at least one disagreement in the block.
Crossing absorbs when site 0 becomes disagreed; regeneration absorbs when all
three block sites become agreed.
"""

from itertools import product
import sympy as sp

E = sp.symbols("e", positive=True)
PAIRS = ((0, 0), (1, 1), (0, 1), (1, 0))
DIAG = {(0, 0), (1, 1)}
OFF = {(0, 1), (1, 0)}
EXT = (0, 1)

r = {
    (0, 0): E,
    (0, 1): E / 2,
    (1, 0): 1 - E**2,
    (1, 1): sp.Integer(0),
}
# Strict ordering for 0<e<1/2.
rank = {(1, 0): 3, (0, 0): 2, (0, 1): 1, (1, 1): 0}


def canonical_pair(env_zeta, env_xi):
    p = r[env_zeta]
    q = r[env_xi]
    if rank[env_zeta] >= rank[env_xi]:
        return {
            (0, 0): 1 - p,
            (1, 1): q,
            (1, 0): p - q,
            (0, 1): sp.Integer(0),
        }
    return {
        (0, 0): 1 - q,
        (1, 1): p,
        (0, 1): q - p,
        (1, 0): sp.Integer(0),
    }


def build_length_three():
    states = [
        s
        for s in product(PAIRS, repeat=3)
        if s[0] in DIAG and any(pair in OFF for pair in s)
    ]
    index = {s: i for i, s in enumerate(states)}
    n = len(states)
    assert n == 24
    K = sp.zeros(n, n)
    cross = sp.zeros(n, 1)
    regen = sp.zeros(n, 1)

    for i, state in enumerate(states):
        for site in range(3):
            here = state[site]
            right = EXT if site == 2 else state[site + 1]
            out = canonical_pair((here[0], right[0]), (here[1], right[1]))
            for new_pair, probability in out.items():
                probability /= 3
                if probability == 0:
                    continue
                new_state = list(state)
                new_state[site] = new_pair
                new_state = tuple(new_state)
                if site == 0 and new_pair in OFF:
                    cross[i] += probability
                elif all(pair in DIAG for pair in new_state):
                    regen[i] += probability
                else:
                    K[i, index[new_state]] += probability

    assert all(
        sp.simplify(
            sum(K[i, j] for j in range(n)) + cross[i] + regen[i] - 1
        ) == 0
        for i in range(n)
    )
    return states, K, cross


def main():
    states, K, cross = build_length_three()
    h = (sp.eye(len(states)) - K).inv() * cross

    # If the rightmost agreed state is 1, a boundary attack against exterior 01
    # enters with orientation 10 and probability r10=1-e^2 -> 1.
    starts = {
        (0, 0, 1): ((0, 0), (0, 0), (1, 0)),
        (0, 1, 1): ((0, 0), (1, 1), (1, 0)),
        (1, 0, 1): ((1, 1), (0, 0), (1, 0)),
        (1, 1, 1): ((1, 1), (1, 1), (1, 0)),
    }
    expected = {
        (0, 0, 1): sp.Rational(43, 75),
        (0, 1, 1): sp.Rational(4, 5),
        (1, 0, 1): sp.Rational(19, 30),
        (1, 1, 1): sp.Rational(9, 10),
    }

    limits = {}
    for full, transient in starts.items():
        value = sp.cancel(h[states.index(transient)])
        lim = sp.limit(value, E, 0, dir="+")
        assert lim == expected[full]
        limits[full] = lim
        print(f"full={full}: conditional crossing limit = {lim}")

    # If the rightmost agreed state is 0, the attack probability is
    # r00-r01=e/2, hence its unconditional crossing factor tends to 0.
    assert max(limits.values()) == sp.Rational(9, 10)
    print("adversarial length-three one-attack factor limit = 9/10")
    print("all exact symbolic checks passed")


if __name__ == "__main__":
    main()
