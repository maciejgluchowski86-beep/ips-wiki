from itertools import combinations, product
import sympy as sp

rho = sp.symbols("rho")
p = sp.symbols("p0:4")
SITES = tuple(range(4))
Q = frozenset({1, 2})
HALF = sp.Rational(1, 2)


def subsets(items):
    items = tuple(items)
    for r in range(len(items) + 1):
        for tup in combinations(items, r):
            yield frozenset(tup)


def sigma(bit):
    return 2 * bit - 1


def rate(bits):
    """Dimer Metropolis rate: rho iff both boundary bonds are aligned."""
    s = [sigma(bit) for bit in bits]
    both_aligned = s[0] * s[1] == 1 and s[2] * s[3] == 1
    return rho if both_aligned else sp.Integer(1)


def flip(bits):
    bits = list(bits)
    for i in Q:
        bits[i] = 1 - bits[i]
    return tuple(bits)


def x_half(A, bits):
    value = sp.Integer(1)
    for i in A:
        value *= sp.Rational(2 * bits[i] - 1, 2)
    return value


def half_centered_coefficient(values, B):
    """Coefficient of prod_{i in B}(eta_i-1/2) by exact Walsh inversion."""
    total = sp.Integer(0)
    for bits in product((0, 1), repeat=4):
        sign = sp.Integer(1)
        for i in B:
            sign *= sigma(bits[i])
        total += values[bits] * sign
    return sp.factor(sp.Rational(2 ** len(B), 16) * total)


# Exact half-centered expansion of the rate.
rate_values = {bits: rate(bits) for bits in product((0, 1), repeat=4)}
rate_coeff = {
    B: half_centered_coefficient(rate_values, B)
    for B in subsets(SITES)
}
rate_coeff = {B: c for B, c in rate_coeff.items() if c != 0}

expected_rate_coeff = {
    frozenset(): (rho + 3) / 4,
    frozenset({0, 1}): rho - 1,
    frozenset({2, 3}): rho - 1,
    frozenset({0, 1, 2, 3}): 4 * (rho - 1),
}
assert set(rate_coeff) == set(expected_rate_coeff)
for B, expected in expected_rate_coeff.items():
    assert sp.simplify(rate_coeff[B] - expected) == 0


# Full 16 x 16 local generator matrix in the half-centered monomial basis.
matrix = {}
for A in subsets(SITES):
    values = {}
    for bits in product((0, 1), repeat=4):
        values[bits] = sp.expand(
            rate(bits) * (x_half(A, flip(bits)) - x_half(A, bits))
        )
    for B in subsets(SITES):
        matrix[(A, B)] = half_centered_coefficient(values, B)

nonzero_offdiag = []
for (A, B), coeff in matrix.items():
    if A == B or coeff == 0:
        continue
    quotient = sp.simplify(coeff / (1 - rho))
    assert quotient.is_Rational
    assert quotient > 0
    nonzero_offdiag.append((A, B, coeff))

# The interacting dimer has genuine off-diagonal centered transitions.
assert len(nonzero_offdiag) == 24


# General-profile expansion machinery, used only to verify uniqueness of p=1/2.
def phi_p(A, bits):
    value = sp.Integer(1)
    for i in A:
        value *= bits[i] - p[i]
    return sp.expand(value)


def boolean_mobius(values):
    """Multilinear eta-monomial coefficients from values on {0,1}^4."""
    coeff = {}
    for S in subsets(SITES):
        value = sp.Integer(0)
        for T in subsets(sorted(S)):
            bits = tuple(1 if i in T else 0 for i in SITES)
            value += (-1) ** (len(S) - len(T)) * values[bits]
        coeff[S] = sp.expand(value)
    return coeff


def general_centered_coefficient(A, B):
    values = {}
    for bits in product((0, 1), repeat=4):
        values[bits] = sp.expand(
            rate(bits) * (phi_p(A, flip(bits)) - phi_p(A, bits))
        )
    eta_coeff = boolean_mobius(values)

    # eta_S = prod_{i in S} (x_i + p_i).
    value = sp.Integer(0)
    for S, coeff in eta_coeff.items():
        if not B.issubset(S):
            continue
        constant = sp.Integer(1)
        for i in S - B:
            constant *= p[i]
        value += coeff * constant
    return sp.factor(value)


internal_obstruction = general_centered_coefficient(
    frozenset({1, 2}), frozenset({0, 3})
)
expected_internal = (rho - 1) * (
    2 * (p[1] - HALF) ** 2 + 2 * (p[2] - HALF) ** 2
)
assert sp.simplify(internal_obstruction - expected_internal) == 0

subs_internal = {p[1]: HALF, p[2]: HALF}

left_positive = sp.factor(
    general_centered_coefficient(frozenset({1}), frozenset()).subs(subs_internal)
)
left_negative = sp.factor(
    general_centered_coefficient(frozenset({0, 1}), frozenset({0})).subs(
        subs_internal
    )
)
right_positive = sp.factor(
    general_centered_coefficient(frozenset({2}), frozenset()).subs(subs_internal)
)
right_negative = sp.factor(
    general_centered_coefficient(frozenset({2, 3}), frozenset({3})).subs(
        subs_internal
    )
)

assert sp.simplify(
    left_positive + (2 * p[0] - 1) * (rho - 1) / 4
) == 0
assert sp.simplify(
    left_negative - (2 * p[0] - 1) * (rho - 1) / 4
) == 0
assert sp.simplify(
    right_positive + (2 * p[3] - 1) * (rho - 1) / 4
) == 0
assert sp.simplify(
    right_negative - (2 * p[3] - 1) * (rho - 1) / 4
) == 0

# For 0 < rho < 1, Metzler nonnegativity of the displayed pairs forces
# p1=p2=1/2 first, then simultaneously p0>=1/2 and p0<=1/2, and likewise p3.

print("dimer Metropolis centered-basis Metzler positivity verified")
print("nonzero off-diagonal entries:", len(nonzero_offdiag))
print("all are positive rational multiples of 1-rho")
print("unique interacting local centering: p0=p1=p2=p3=1/2")
