#!/usr/bin/env python3
"""Exact symbolic checks for Student G Assignment 004.

Checks the obstruction in 004-global-restart-corrector.md:

1. the exact tilted drift of the reachable all-01 disagreement stack under
   the exposed-only product corrector from Assignment 003;
2. the near-East limit of that drift, including e_0 -> 8/7 and
   drift -> (H-2)/7;
3. the 16-phase same-orientation local bulk formula, derived from the
   common-uniform transition law and exposure-entry bookkeeping;
4. the representative opposite-orientation bulk formula.

No Monte Carlo or floating-point calculation is used.
"""

import sympy as sp


# ---------------------------------------------------------------------------
# Parameters and the old exposed-only stack obstruction.
# ---------------------------------------------------------------------------

a, b, c, s, e0, lam = sp.symbols(
    "a b c s e0 lam", positive=True
)
H = sp.symbols("H", integer=True, positive=True)
omega = 1 - c + a

# Reachable all-01 stack, with coupled-zero bookkeeping boundaries.
# Leftmost coalescence moves the exposure right: tilted ratio s.
# An interior coalescence creates a second exposure: tilted ratio s*e0.
# Rightmost coalescence removes one unresolved height level: ratio lam^-1.
left = (1 - a) * (s - 1)
interior = (H - 2) * (1 - a) * (s * e0 - 1)
right = omega * (1 / lam - 1)
old_stack_drift = sp.expand(left + interior + right)

assert sp.simplify(
    old_stack_drift
    - (
        (1 - a) * (s - 1)
        + (H - 2) * (1 - a) * (s * e0 - 1)
        + omega * (1 / lam - 1)
    )
) == 0

# For s>1 and e0>=1 the interior coefficient is strictly positive.
assert sp.factor((s * e0 - 1) - (s - 1)) == s * (e0 - 1)


# ---------------------------------------------------------------------------
# Near-East stress path.
# ---------------------------------------------------------------------------

eps = sp.symbols("eps", positive=True)
a_e = eps**2
b_e = eps
c_e = 1 - eps**2
d_e = b_e - a_e
omega_e = sp.simplify(1 - c_e + a_e)

Den_e = sp.expand(
    (b_e + omega_e) * (1 + omega_e)
    - a_e * (1 - c_e)
)
h0_e = sp.simplify(
    (d_e * (1 + omega_e) + a_e * c_e) / Den_e
)
h1_e = sp.simplify(
    (c_e * (b_e + omega_e) + (1 - c_e) * d_e) / Den_e
)

s_e = 1 + eps**2 / 4
M_e = sp.simplify(
    (1 - h1_e) * s_e / (1 - h1_e * s_e)
)
e0_e = sp.simplify(
    s_e * ((1 - h0_e) + h0_e * M_e)
)

assert sp.limit((1 - h0_e) / eps, eps, 0, dir="+") == 2
assert sp.limit((1 - h1_e) / eps**2, eps, 0, dir="+") == 2
assert sp.limit(M_e, eps, 0, dir="+") == sp.Rational(8, 7)
assert sp.limit(e0_e, eps, 0, dir="+") == sp.Rational(8, 7)

near_east_drift = sp.simplify(
    old_stack_drift.subs(
        {
            a: a_e,
            b: b_e,
            c: c_e,
            s: s_e,
            e0: e0_e,
            lam: 2,
        }
    )
)
assert sp.simplify(
    sp.limit(near_east_drift, eps, 0, dir="+")
    - (H - 2) / 7
) == 0


# ---------------------------------------------------------------------------
# Exact finite 16-phase local tilted generator.
# ---------------------------------------------------------------------------

PAIRS = ("00", "11", "01", "10")


def diagonal(pair):
    return pair in ("00", "11")


def offdiag(pair):
    return pair in ("01", "10")


def exposure(alpha, beta):
    return diagonal(alpha) and offdiag(beta)


def entry_increment(alpha, beta, gamma, beta_new):
    """Number of newly created exposure edges when beta is updated."""
    return int((not exposure(alpha, beta)) and exposure(alpha, beta_new)) + int(
        (not exposure(beta, gamma)) and exposure(beta_new, gamma)
    )


q = {
    (alpha, beta): sp.symbols(f"q_{alpha}_{beta}", positive=True)
    for alpha in PAIRS
    for beta in PAIRS
}


def local_G(alpha, beta, gamma, outcomes):
    """Exact local tilted drift from a supplied common-uniform outcome law."""
    denominator = q[(alpha, beta)] * q[(beta, gamma)]
    value = 0
    for beta_new, probability in outcomes.items():
        if beta_new == beta:
            continue
        ratio = (
            q[(alpha, beta_new)] * q[(beta_new, gamma)]
            / denominator
        )
        value += probability * (
            s ** entry_increment(alpha, beta, gamma, beta_new)
            * ratio
            - 1
        )
    return sp.simplify(value)


# Same-orientation triple (01,01,01).
# Here p=r_00=a and p~=r_11=0, hence 01->00 with probability 1-a
# and 01->10 with probability a.
assert entry_increment("01", "01", "01", "00") == 1
assert entry_increment("01", "01", "01", "10") == 0
same_orientation = local_G(
    "01", "01", "01", {"00": 1 - a, "10": a}
)
expected_same = (
    (1 - a)
    * (
        s * q[("01", "00")] * q[("00", "01")]
        / q[("01", "01")] ** 2
        - 1
    )
    + a
    * (
        q[("01", "10")] * q[("10", "01")]
        / q[("01", "01")] ** 2
        - 1
    )
)
assert sp.simplify(same_orientation - expected_same) == 0

# Old exposed-only product: q_{00,01}=e0; every other phase appearing
# above has weight one. This is the positive bulk self-loop.
old_subs = {symbol: 1 for symbol in q.values()}
old_subs[q[("00", "01")]] = e0
old_subs[q[("00", "10")]] = e0
old_same = sp.simplify(same_orientation.subs(old_subs))
assert sp.simplify(old_same - (1 - a) * (s * e0 - 1)) == 0


# Opposite-orientation triple (01,10,01).
# Residual c>b. Here p=r_10=c and p~=r_01=b, so the middle pair
# goes to 11 with probability b, 00 with probability 1-c, and remains
# 10 with probability c-b. Both diagonal outcomes create an exposure.
assert entry_increment("01", "10", "01", "11") == 1
assert entry_increment("01", "10", "01", "00") == 1
opposite_orientation = local_G(
    "01", "10", "01", {"11": b, "00": 1 - c, "10": c - b}
)
expected_opposite = (
    b
    * (
        s * q[("01", "11")] * q[("11", "01")]
        / (q[("01", "10")] * q[("10", "01")])
        - 1
    )
    + (1 - c)
    * (
        s * q[("01", "00")] * q[("00", "01")]
        / (q[("01", "10")] * q[("10", "01")])
        - 1
    )
)
assert sp.simplify(opposite_orientation - expected_opposite) == 0


print("old exposed-only stack drift: verified")
print("near-East old-product drift -> (H-2)/7: verified")
print("16-phase same-orientation bulk formula: verified")
print("16-phase opposite-orientation bulk formula: verified")
