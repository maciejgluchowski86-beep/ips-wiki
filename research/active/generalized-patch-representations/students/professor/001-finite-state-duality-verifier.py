#!/usr/bin/env python3
"""Exact finite verifier for Assignment 001.

Checks the d=3 one-neighbour generator identity for every elementary physical
transition/rate-basis atom, including compatible/conflicting typed overlaps,
and checks the signed graphical generator + potential representation. Also
checks the exact d=2 reduction to the binary death/split/birth coefficients.

All arithmetic is integer/Fraction; there is no floating point and no Monte
Carlo.
"""

from fractions import Fraction
from itertools import product


def H(xi, physical):
    """Typed monomial. xi=None is the cemetery/zero state."""
    if xi is None:
        return 0
    return int(all(physical[i] == a for i, a in xi.items()))


def merge(xi, tau):
    """Compatible typed union; conflict goes to cemetery None."""
    if xi is None:
        return None
    out = dict(xi)
    for i, a in tau.items():
        if i in out and out[i] != a:
            return None
        out[i] = a
    return out


def theta(xi, source, source_outcome, tau):
    """Remove source, optionally reinsert with new type, then merge target."""
    out = dict(xi)
    out.pop(source, None)
    if source_outcome != 0:
        out[source] = source_outcome
    return merge(out, tau)


def elementary_branch_coefficients(d, r, x, y):
    """Branch coefficients for one physical x->y rate-basis coefficient = 1."""
    assert x != y
    a = {s: 0 for s in range(d)}
    c0r = int(x == 0 and y == r)
    a[0] = c0r
    for s in range(1, d):
        if s != r:
            a[s] = int(x == s and y == r) - c0r
    a[r] = -c0r - int(x == r and y != r)
    return a


def general_branch_coefficients(d, r, c):
    """Branch coefficients from arbitrary exact rate-basis coefficients.

    c[(x,y)] is the coefficient of one fixed neighbour target mode in the
    physical transition rate x->y.
    """
    zero = Fraction(0)
    c0r = c.get((0, r), zero)
    a = {s: zero for s in range(d)}
    a[0] = c0r
    for s in range(1, d):
        if s != r:
            a[s] = c.get((s, r), zero) - c0r
    a[r] = -c0r - sum(
        (c.get((r, y), zero) for y in range(d) if y != r),
        zero,
    )
    return a


def rate_basis(target_label, physical):
    """Neighbour tensor mode: 1 if None, otherwise 1{eta_1=label}."""
    return int(target_label is None or physical[1] == target_label)


def direct_atom(d, r, x, y, target_label, existing_neighbour, physical):
    """Direct physical generator action for one elementary rate-basis atom."""
    xi = {0: r}
    if existing_neighbour is not None:
        xi[1] = existing_neighbour
    if physical[0] != x or rate_basis(target_label, physical) == 0:
        return 0
    updated = list(physical)
    updated[0] = y
    return H(xi, tuple(updated)) - H(xi, physical)


def proposed_linear_atom(d, r, x, y, target_label, existing_neighbour, physical):
    """Right side of the typed generator-action formula."""
    xi = {0: r}
    if existing_neighbour is not None:
        xi[1] = existing_neighbour
    tau = {} if target_label is None else {1: target_label}
    a = elementary_branch_coefficients(d, r, x, y)
    return sum(
        coeff * H(theta(xi, 0, s, tau), physical)
        for s, coeff in a.items()
    )


def proposed_graphical_plus_potential(
    d, r, x, y, target_label, existing_neighbour, physical
):
    """D H + V H using absolute branch coefficients as jump rates.

    The empty-target source-survival branch (s=r,tau=empty) is omitted from D
    and inserted with its signed coefficient into V, exactly as the binary
    paper treats the empty-target birth coefficient.
    """
    xi = {0: r}
    if existing_neighbour is not None:
        xi[1] = existing_neighbour
    tau = {} if target_label is None else {1: target_label}
    a = elementary_branch_coefficients(d, r, x, y)
    h_current = H(xi, physical)

    D = 0
    total_jump_rate = 0
    diagonal_coefficient = a[r] if target_label is None else 0

    for s, coeff in a.items():
        if coeff == 0:
            continue
        if target_label is None and s == r:
            continue
        rate = abs(coeff)
        sign = 1 if coeff > 0 else -1
        h_target = H(theta(xi, 0, s, tau), physical)
        D += rate * (sign * h_target - h_current)
        total_jump_rate += rate

    V = total_jump_rate + diagonal_coefficient
    return D + V * h_current


def run_d3():
    d = 3
    checks = 0
    conflict_checks = 0

    for r in (1, 2):
        for x in range(d):
            for y in range(d):
                if x == y:
                    continue
                for target_label in (None, 1, 2):
                    for existing_neighbour in (None, 1, 2):
                        if (
                            target_label is not None
                            and existing_neighbour is not None
                            and target_label != existing_neighbour
                        ):
                            conflict_checks += 1
                        for physical in product(range(d), repeat=2):
                            direct = direct_atom(
                                d, r, x, y, target_label, existing_neighbour, physical
                            )
                            linear = proposed_linear_atom(
                                d, r, x, y, target_label, existing_neighbour, physical
                            )
                            graphical = proposed_graphical_plus_potential(
                                d, r, x, y, target_label, existing_neighbour, physical
                            )
                            assert direct == linear == graphical, (
                                r,
                                x,
                                y,
                                target_label,
                                existing_neighbour,
                                physical,
                                direct,
                                linear,
                                graphical,
                                elementary_branch_coefficients(d, r, x, y),
                            )
                            checks += 1

    assert checks == 972
    assert conflict_checks > 0

    # Local structural sanity checks.
    assert elementary_branch_coefficients(3, 1, 0, 1) == {0: 1, 1: -1, 2: -1}
    assert elementary_branch_coefficients(3, 1, 2, 1) == {0: 0, 1: 0, 2: 1}
    assert elementary_branch_coefficients(3, 1, 1, 2) == {0: 0, 1: -1, 2: 0}

    return checks, conflict_checks


def run_d2():
    d = 2
    checks = 0
    for r in (1,):
        for x, y in ((0, 1), (1, 0)):
            for target_label in (None, 1):
                for existing_neighbour in (None, 1):
                    for physical in product(range(d), repeat=2):
                        direct = direct_atom(
                            d, r, x, y, target_label, existing_neighbour, physical
                        )
                        linear = proposed_linear_atom(
                            d, r, x, y, target_label, existing_neighbour, physical
                        )
                        graphical = proposed_graphical_plus_potential(
                            d, r, x, y, target_label, existing_neighbour, physical
                        )
                        assert direct == linear == graphical
                        checks += 1

    assert checks == 32

    # Generic exact coefficient identification with the paper.
    A = Fraction(2, 3)   # c^{0->1}(tau)
    B = Fraction(-5, 7)  # c^{1->0}(tau), allowed to be signed after expansion
    a = general_branch_coefficients(2, 1, {(0, 1): A, (1, 0): B})
    assert a[0] == A
    assert a[1] == -A - B

    return checks, a


if __name__ == "__main__":
    d3_checks, conflict_checks = run_d3()
    d2_checks, binary_coeffs = run_d2()

    print("d=3 exact elementary generator/FK checks:", d3_checks)
    print("d=3 conflicting typed-target cases included:", conflict_checks)
    print("d=2 exact specialization checks:", d2_checks)
    print("binary generic branch coefficients:", binary_coeffs)
    print("all finite-state typed-duality checks passed")
