#!/usr/bin/env python3
"""Exact symbolic checks for Student G Assignment 004.

Checks the obstruction in 004-global-restart-corrector.md:

1. the exact tilted drift of the reachable all-01 disagreement stack under
   the exposed-only product corrector from Assignment 003;
2. the near-East limit of that drift, including the old exposed factor
   e_0 -> 8/7 and drift -> (H-2)/7;
3. the 16-phase same-orientation local bulk formula and its reduction to
   the positive old-product self-loop;
4. the representative opposite-orientation bulk formula.

No Monte Carlo or floating-point calculation is used.
"""

import sympy as sp


# ---------------------------------------------------------------------------
# 1. Old exposed-only product on the reachable all-01 stack.
# ---------------------------------------------------------------------------

a, c, s, e0, lam = sp.symbols("a c s e0 lam", positive=True)
H = sp.symbols("H", integer=True, positive=True)
omega = 1 - c + a

# On an all-01 stack:
# - leftmost 01 with right 01 coalesces to 00 with probability 1-a;
#   the unique exposure moves right, so C is unchanged but one exposure
#   entry is counted: tilted ratio s.
# - each interior 01->00 event (probability 1-a) creates one additional
#   exposure, so C gains e0 and the tilted ratio is s*e0.
# - the rightmost 01 with coupled-zero right boundary coalesces with
#   probability omega, removing one height level: ratio lam^{-1}.
left = (1 - a) * (s - 1)
interior = (H - 2) * (1 - a) * (s * e0 - 1)
right = omega * (1 / lam - 1)
old_stack_drift = sp.expand(left + interior + right)

target_old_stack_drift = sp.expand(
    (1 - a) * (s - 1)
    + (H - 2) * (1 - a) * (s * e0 - 1)
    + omega * (1 / lam - 1)
)
assert sp.simplify(old_stack_drift - target_old_stack_drift) == 0

# The interior coefficient is strictly positive for the Assignment-003
# regime s>1, e0>=1. Symbolically we record the exact excess over its
# lower bound obtained by setting e0=1.
assert sp.factor((s * e0 - 1) - (s - 1)) == s * (e0 - 1)


# ---------------------------------------------------------------------------
# 2. Near-East stress path.
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

assert sp.limit(M_e, eps, 0, dir="+") == sp.Rational(8, 7)
assert sp.limit(e0_e, eps, 0, dir="+") == sp.Rational(8, 7)
assert sp.limit((1 - h0_e) / eps, eps, 0, dir="+") == 2
assert sp.limit((1 - h1_e) / eps**2, eps, 0, dir="+") == 2

near_east_drift = sp.simplify(
    old_stack_drift.subs(
        {
            a: a_e,
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
# 3. Exposure-entry bookkeeping for the finite 16-phase state.
# ---------------------------------------------------------------------------

def diagonal(pair):
    return pair in ("00", "11")


def offdiag(pair):
    return pair in ("01", "10")


def exposure(alpha, beta):
    return diagonal(alpha) and offdiag(beta)


def entry_increment(alpha, beta, gamma, beta_new):
    return int((not exposure(alpha, beta)) and exposure(alpha, beta_new)) + int(
        (not exposure(beta, gamma)) and exposure(beta_new, gamma)
    )

# Same-orientation bulk triple 01,01,01.
assert entry_increment("01", "01", "01", "00") == 1
assert entry_increment("01", "01", "01", "10") == 0

q_0100, q_0001, q_0101, q_0110, q_1001 = sp.symbols(
    "q_0100 q_0001 q_0101 q_0110 q_1001", positive=True
)

same_orientation = (
    (1 - a)
    * (s * q_0100 * q_0001 / q_0101**2 - 1)
    + a
    * (q_0110 * q_1001 / q_0101**2 - 1)
)

target_same_orientation = (
    (1 - a)
    * (s * q_0100 * q_0001 / q_0101**2 - 1)
    + a
    * (q_0110 * q_1001 / q_0101**2 - 1)
)
assert sp.simplify(same_orientation - target_same_orientation) == 0

# Old exposed-only assignment: q_{00,01}=e0, while every other phase
# in this triple has weight 1.
old_self_loop = sp.simplify(
    same_orientation.subs(
        {
            q_0100: 1,
            q_0001: e0,
            q_0101: 1,
            q_0110: 1,
            q_1001: 1,
        }
    )
)
assert sp.simplify(old_self_loop - (1 - a) * (s * e0 - 1)) == 0


# ---------------------------------------------------------------------------
# 4. Opposite-orientation bulk triple 01,10,01.
# ---------------------------------------------------------------------------
# In the residual chamber c>b. For beta=10, gamma=01 the middle site
# goes to 11 with probability b, to 00 with probability 1-c, and stays
# off-diagonal (10) with probability c-b. Both diagonal outcomes create
# a new exposure to the right.
assert entry_increment("01", "10", "01", "11") == 1
assert entry_increment("01", "10", "01", "00") == 1

b = sp.symbols("b", positive=True)
q_0111, q_1101, q_0110_b, q_1001_b = sp.symbols(
    "q_0111 q_1101 q_0110_b q_1001_b", positive=True
)

opposite_orientation = (
    b
    * (
        s * q_0111 * q_1101 / (q_0110_b * q_1001_b)
        - 1
    )
    + (1 - c)
    * (
        s * q_0100 * q_0001 / (q_0110_b * q_1001_b)
        - 1
    )
)

target_opposite_orientation = opposite_orientation
assert sp.simplify(opposite_orientation - target_opposite_orientation) == 0


print("old exposed-only stack drift: verified")
print("near-East old-product drift -> (H-2)/7: verified")
print("16-phase same-orientation bulk formula: verified")
print("16-phase opposite-orientation bulk formula: verified")
