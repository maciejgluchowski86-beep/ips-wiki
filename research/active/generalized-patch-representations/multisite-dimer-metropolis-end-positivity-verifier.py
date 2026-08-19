from itertools import combinations, product
import sympy as sp

rho = sp.symbols("rho")
VARS = (0, 1, 2, 3)
Q = frozenset({1, 2})
D = frozenset({1})
TARGET = frozenset({0})


def spin(bit):
    return 2 * bit - 1


def rate(bits):
    conf = dict(zip(VARS, bits))
    sigma = {i: spin(conf[i]) for i in VARS}
    aligned_left = sigma[0] * sigma[1] == 1
    aligned_right = sigma[2] * sigma[3] == 1
    return rho if aligned_left and aligned_right else sp.Integer(1)


# Values f(1_T).
f = {}
for bits in product((0, 1), repeat=len(VARS)):
    T = frozenset(i for i, bit in zip(VARS, bits) if bit)
    f[T] = rate(bits)


# Multilinear/Mobius coefficients.
coeff = {}
for r in range(len(VARS) + 1):
    for S_tuple in combinations(VARS, r):
        S = frozenset(S_tuple)
        value = sp.Integer(0)
        for k in range(r + 1):
            for T_tuple in combinations(S_tuple, k):
                T = frozenset(T_tuple)
                value += (-1) ** (r - k) * f[T]
        value = sp.expand(value)
        if value != 0:
            coeff[S] = value

assert sp.factor(coeff[frozenset({0})]) == 1 - rho
assert sp.factor(coeff[frozenset({0, 1})]) == -2 * (1 - rho)
assert sp.factor(coeff[frozenset({0, 2})]) == -(1 - rho)
assert sp.factor(coeff[frozenset({0, 1, 2})]) == 2 * (1 - rho)


def theta(D, J):
    if J == D:
        return (-1) ** len(D) - 1
    return (-1) ** len(J)


# Canonically aggregate the block-dual row at pre-state D and external target {0}.
row = {}
for S, c in coeff.items():
    if frozenset(S - Q) != TARGET:
        continue
    S_Q = frozenset(S & Q)

    if S & D:
        R = frozenset(D | S_Q)
        row[R] = sp.expand(row.get(R, 0) - c)
    else:
        D_list = tuple(sorted(D))
        for r in range(len(D_list) + 1):
            for J_tuple in combinations(D_list, r):
                J = frozenset(J_tuple)
                R = frozenset(J | S_Q)
                row[R] = sp.expand(row.get(R, 0) + c * theta(D, J))

row = {R: sp.factor(a) for R, a in row.items() if sp.expand(a) != 0}

assert row == {
    frozenset(): 1 - rho,
    frozenset({2}): -(1 - rho),
}

# Exact rational gate rho=1/2.
gate = {R: sp.simplify(a.subs(rho, sp.Rational(1, 2))) for R, a in row.items()}
assert gate == {
    frozenset(): sp.Rational(1, 2),
    frozenset({2}): sp.Rational(-1, 2),
}

# For 0<rho<1, total absolute row rate is 2(1-rho), so the normalized
# zero-length outgoing end factor is (1-u2)/2.
u1, u2, p1, p2 = sp.symbols("u1 u2 p1 p2")
C = sp.Rational(1, 2) * (1 - u2)
centered = sp.expand(
    sp.Rational(1, 2) * (1 - p2)
    - sp.Rational(1, 2) * (u2 - p2)
)
assert sp.expand(C - centered) == 0
assert sp.diff(C, u2) == sp.Rational(-1, 2)
assert sp.diff(C, u1) == 0

# At rho=1 the row disappears, confirming that only the trivial constant-rate
# limit avoids this particular obstruction.
assert all(sp.simplify(a.subs(rho, 1)) == 0 for a in row.values())

print("dimer Metropolis block-end positivity obstruction verified")
print("row:", row)
print("normalized end factor:", C)
print("centered singleton coefficient kappa_{2} =", sp.diff(C, u2))
