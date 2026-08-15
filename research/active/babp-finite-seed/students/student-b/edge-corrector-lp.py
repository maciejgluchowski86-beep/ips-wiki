#!/usr/bin/env python3
"""Finite-window right-edge corrector LP for one-dimensional BABP.

Requires scipy. For fixed k and lambda, maximize the uniform generator drift
v of H(B)=R(B)+phi(u(B)), where u records the k sites immediately behind the
rightmost particle and the next unresolved bit is treated adversarially.
"""

from __future__ import annotations

import argparse
import itertools

import numpy as np
from scipy.optimize import brentq, linprog


def solve(k: int, lam: float):
    states = list(itertools.product((0, 1), repeat=k))
    index = {state: i for i, state in enumerate(states)}
    n = len(states)

    rows = []
    rhs = []

    for u in states:
        i = index[u]
        for z in (0, 1):
            coeff = np.zeros(n)
            constant = lam - u[0]

            def add(rate, new_u):
                if rate:
                    coeff[index[new_u]] += rate
                    coeff[i] -= rate

            # Birth from the rightmost particle to R+1.
            add(lam, (1,) + u[:-1])

            # Death of the rightmost particle if R-1 is occupied.
            if u[0]:
                add(1.0, u[1:] + (z,))

            # Flips inside the k-site edge window.
            for j in range(k):
                left_neighbor = 1 if j == 0 else u[j - 1]
                right_neighbor = z if j == k - 1 else u[j + 1]
                occupied_neighbors = left_neighbor + right_neighbor
                rate = occupied_neighbors * (lam if u[j] == 0 else 1.0)
                if rate:
                    flipped = list(u)
                    flipped[j] = 1 - flipped[j]
                    add(rate, tuple(flipped))

            # D >= v is -coeff.phi + v <= constant.
            row = np.zeros(n + 1)
            row[:n] = -coeff
            row[-1] = 1.0
            rows.append(row)
            rhs.append(constant)

    # Gauge phi(0,...,0)=0.
    a_eq = np.zeros((1, n + 1))
    a_eq[0, index[(0,) * k]] = 1.0

    objective = np.zeros(n + 1)
    objective[-1] = -1.0

    result = linprog(
        objective,
        A_ub=np.asarray(rows),
        b_ub=np.asarray(rhs),
        A_eq=a_eq,
        b_eq=[0.0],
        bounds=[(None, None)] * (n + 1),
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    return result.x[-1], result.x[:-1]


def threshold(k: int, lo: float = 1e-6, hi: float = 0.5):
    f_lo = solve(k, lo)[0]
    f_hi = solve(k, hi)[0]
    if f_lo >= 0:
        return lo
    if f_hi <= 0:
        raise ValueError("threshold not bracketed")
    return brentq(
        lambda lam: solve(k, lam)[0],
        lo,
        hi,
        xtol=1e-10,
        rtol=1e-10,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("k", type=int)
    parser.add_argument("--lambda-value", type=float)
    parser.add_argument("--threshold", action="store_true")
    args = parser.parse_args()

    if args.threshold:
        print(threshold(args.k))
    else:
        if args.lambda_value is None:
            parser.error("give --lambda-value or --threshold")
        v, _ = solve(args.k, args.lambda_value)
        print(v)


if __name__ == "__main__":
    main()
