#!/usr/bin/env python3
"""Exact finite decision-tree checks for FA-INFO-002.

Spin 0 is vacancy.  All arithmetic is Fraction; there is no Monte Carlo.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product


def bit_prob(bit, q):
    return q if bit == 0 else 1 - q


def fa_ring(z, x, left, right):
    return z if (left == 0 or right == 0) else x


def s1(bits, z):
    x, left, right = bits
    return fa_ring(z, x, left, right)


def s2(bits, z1, z0):
    xm1, x0, x1, x2 = bits
    y1 = fa_ring(z1, x1, x0, x2)
    return fa_ring(z0, x0, xm1, y1)


def essential_variables(func, nvars):
    ans = []
    for i in range(nvars):
        for a in product((0, 1), repeat=nvars):
            b = list(a)
            b[i] = 1 - b[i]
            if func(a) != func(tuple(b)):
                ans.append(i)
                break
    return tuple(ans)


def optimal_decision_cost(func, nvars, q, q0=None, mode="l2"):
    """Optimize over every exact deterministic predictable decision tree.

    Randomizing the next query cannot improve either linear objective, so this
    dynamic program also gives the optimum over randomized predictable rules.
    """
    assignments = tuple(product((0, 1), repeat=nvars))
    values = {a: func(a) for a in assignments}

    if mode == "l2":
        assert q0 is not None
        weights = {
            0: q0 * q0 / q,
            1: (1 - q0) * (1 - q0) / (1 - q),
        }

    @lru_cache(None)
    def rec(partial):
        known = dict(partial)
        possible = [
            a for a in assignments
            if all(a[i] == b for i, b in known.items())
        ]
        outputs = {values[a] for a in possible}
        if len(outputs) == 1:
            return (Q(1), None) if mode == "l2" else (Q(0), None)

        best = None
        for i in range(nvars):
            if i in known:
                continue
            if mode == "l2":
                cost = Q(0)
                for bit in (0, 1):
                    child, _ = rec(tuple(sorted(partial + ((i, bit),))))
                    cost += weights[bit] * child
            elif mode == "count":
                cost = Q(1)
                for bit in (0, 1):
                    child, _ = rec(tuple(sorted(partial + ((i, bit),))))
                    cost += bit_prob(bit, q) * child
            else:
                raise ValueError(mode)
            if best is None or cost < best[0]:
                best = (cost, i)
        return best

    return rec(tuple())


def output_vacancy_probability(func, nvars, input_q):
    total = Q(0)
    for a in product((0, 1), repeat=nvars):
        pa = Q(1)
        for bit in a:
            pa *= bit_prob(bit, input_q)
        if func(a) == 0:
            total += pa
    return total


def average_s1(q, q0):
    l2 = count = out_q0 = out_q = Q(0)
    for z in (0, 1):
        wz = bit_prob(z, q)
        func = lambda a, z=z: s1(a, z)
        l2 += wz * optimal_decision_cost(func, 3, q, q0, "l2")[0]
        count += wz * optimal_decision_cost(func, 3, q, None, "count")[0]
        out_q0 += wz * output_vacancy_probability(func, 3, q0)
        out_q += wz * output_vacancy_probability(func, 3, q)
    return l2, count, out_q0, out_q


def average_s2(q, q0):
    l2 = count = out_q0 = out_q = Q(0)
    for z1, z0 in product((0, 1), repeat=2):
        wz = bit_prob(z1, q) * bit_prob(z0, q)
        func = lambda a, z1=z1, z0=z0: s2(a, z1, z0)
        l2 += wz * optimal_decision_cost(func, 4, q, q0, "l2")[0]
        count += wz * optimal_decision_cost(func, 4, q, None, "count")[0]
        out_q0 += wz * output_vacancy_probability(func, 4, q0)
        out_q += wz * output_vacancy_probability(func, 4, q)
    return l2, count, out_q0, out_q


def centered_top_coefficient_s2(q):
    """Return E_q[h_2 * prod(V_i-q)] / (q(1-q))^4 exactly."""
    p = 1 - q
    numerator = Q(0)
    for bits_vac in product((0, 1), repeat=4):
        # Convert vacancy indicators V=1 to spin bits x=0.
        spin_bits = tuple(0 if v else 1 for v in bits_vac)
        h = Q(0)
        for z1, z0 in product((0, 1), repeat=2):
            wz = bit_prob(z1, q) * bit_prob(z0, q)
            if s2(spin_bits, z1, z0) == 0:
                h += wz
        prob = Q(1)
        phi = Q(1)
        for v in bits_vac:
            prob *= q if v else p
            phi *= p if v else -q
        numerator += prob * h * phi
    return numerator / (q * p) ** 4


q = Q(1, 10)
p = 1 - q

# Mark-only essential predecessor check.
for z in (0, 1):
    assert essential_variables(lambda a, z=z: s1(a, z), 3) == (0, 1, 2)

expected_s2_essential = {
    (0, 0): (0, 1, 2, 3),
    (0, 1): (),
    (1, 0): (0, 1, 2, 3),
    (1, 1): (0, 1),
}
for coins, expected in expected_s2_essential.items():
    z1, z0 = coins
    assert essential_variables(lambda a, z1=z1, z0=z0: s2(a, z1, z0), 4) == expected

# The centered four-body coefficient is nonzero and equals -q.
assert centered_top_coefficient_s2(q) == -q

for q0 in (Q(1, 20), Q(1, 5)):
    l2_1, count_1, r1, req1 = average_s1(q, q0)
    l2_2, count_2, r2, req2 = average_s2(q, q0)
    c0 = (q0 - q) ** 2 / (q * p)
    c1 = l2_1 - 1
    c2 = l2_2 - 1
    x1 = (r1 - q) ** 2 / (q * p)
    x2 = (r2 - q) ** 2 / (q * p)

    assert req1 == q and req2 == q
    assert count_1 == Q(671, 500)
    assert count_2 == Q(58829, 50000)
    assert c1 > c0 and c2 > c0
    assert x1 < c0 and x2 < c0
    assert x2 > x1

    if q0 == Q(1, 20):
        assert c0 == Q(1, 36)
        assert l2_1 == Q(24135341, 23328000)
        assert c1 / c0 == Q(807341, 648000)
        assert r1 == Q(439, 8000)
        assert x1 / c0 == Q(130321, 160000)

        assert l2_2 == Q(86648193941, 83980800000)
        assert c2 / c0 == Q(2667393941, 2332800000)
        assert r2 == Q(84741, 1600000)
        assert x2 / c0 == Q(5663917081, 6400000000)
        assert x2 / x1 == Q(15689521, 14440000)
    else:
        assert c0 == Q(1, 9)
        assert l2_1 == Q(108719, 91125)
        assert c1 / c0 == Q(17594, 10125)
        assert r1 == Q(41, 250)
        assert x1 / c0 == Q(256, 625)

        assert l2_2 == Q(94564781, 82012500)
        assert c2 / c0 == Q(12552281, 9112500)
        assert r2 == Q(1107, 6250)
        assert x2 / c0 == Q(232324, 390625)
        assert x2 / x1 == Q(58081, 40000)

    print("q0 =", q0)
    print("  baseline chi2 C0 =", c0)
    print("  S1 optimal expected queries =", count_1)
    print("  S1 raw transcript excess / C0 =", c1 / c0)
    print("  S1 exact output chi2 / C0 =", x1 / c0)
    print("  S2 optimal expected queries =", count_2)
    print("  S2 raw transcript excess / C0 =", c2 / c0)
    print("  S2 exact output chi2 / C0 =", x2 / c0)
    print("  S2 output chi2 / S1 output chi2 =", x2 / x1)

print("S1 mark-only support: all 3 predecessor bits for each fixed coin")
print("S2 essential sets by coin pair:", expected_s2_essential)
print("S2 normalized four-body centered coefficient =", centered_top_coefficient_s2(q))
print("all exact FA-INFO finite-circuit checks passed")
