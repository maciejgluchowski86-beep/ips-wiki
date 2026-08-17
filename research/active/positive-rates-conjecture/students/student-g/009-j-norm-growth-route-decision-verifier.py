#!/usr/bin/env python3
"""Exact checks for Student G Assignment 009.

The verifier uses only the standard library.  It checks the rational
strong-growth constants, the East centered-basis generator identity that
underlies the short-sector Green transfer, and the exact renewal arithmetic.
It does not claim to decide rho_J; the report's conclusion is unresolved.
"""

from fractions import Fraction as F

# ---------------------------------------------------------------------------
# Hard strict point P* and exact canonical constants.
# ---------------------------------------------------------------------------
a = F(1, 1000)
b = F(1, 10)
c = F(9999, 10000)
k = 1 - c
B = b + c - a
g = b - a
omega = 1 - c + a

assert 0 < a < b
assert F(1, 2) <= c < 1
assert c >= a + b
assert b * b >= 2 * k * k

assert B == F(10989, 10000)
assert g == F(99, 1000)
assert omega == F(11, 10000)

Z = (a + b + 2) / (a * (2 * b + 3) + k * (b + 2))
assert Z == F(19100, 31)

r0 = 1 / (1 + b)
m0 = (b * k - a) / (1 + b)
assert r0 == F(10, 11)
assert m0 == -F(9, 10000)

S = a*b + 2*a + b*b - b*c + 2*b - 2*c + 2
Cstar = ((a + b*c - b) * (a*b + 2*a - b*b + b*c - 2*b)) / ((1+b)**2 * S)
assert S == F(11231, 100000)
assert Cstar == -F(8829, 11231000)
assert B * Cstar == -F(8820171, 10210000000)
assert -(B*Cstar)/(m0*m0) == F(1088910, 1021)

# ---------------------------------------------------------------------------
# Strong-growth scaling a=e, b=1/10, 1-c=e/10.
# ---------------------------------------------------------------------------
alpha = F(1)
kappa = F(1, 10)
d = alpha - b * kappa
assert d == F(99, 100)

r = F(10, 11)
z0 = (b + 2) / (alpha * (2*b + 3) + kappa * (b + 2))
assert z0 == F(210, 341)
mu = (d / (1 + b)) * z0
assert mu == F(189, 341)

lambda_fixed_depth = r + mu
assert r == F(310, 341)
assert lambda_fixed_depth == F(499, 341)
assert lambda_fixed_depth > 1

first_two_return_sum = mu * (1 + r)
assert first_two_return_sum == F(3969, 3751)
assert first_two_return_sum > 1

prefactor_limit = ((1+b)/b) * mu
assert prefactor_limit == F(2079, 341)
assert mu - r == -F(121, 341)
assert mu + r == F(499, 341)

# ---------------------------------------------------------------------------
# East centered-product basis and exact Green extraction identity.
# ---------------------------------------------------------------------------

def east_L_image(mask: int, m: int):
    out = {}

    def add(M, value):
        out[M] = out.get(M, F(0)) + value
        if out[M] == 0:
            del out[M]

    for i in range(m):
        if not ((mask >> i) & 1):
            continue
        if i == m - 1:
            add(mask, -(1 + b))
        elif not ((mask >> (i + 1)) & 1):
            add(mask, -b)
            add(mask | (1 << (i + 1)), F(1))
        else:
            add(mask, -F(1))
            add(mask & ~(1 << (i + 1)), b)
    return out


def ell(mask: int):
    if not (mask & 1):
        return F(0)
    return b ** mask.bit_count()


def ell_minus_L(mask: int, m: int):
    return sum((-coef) * ell(M) for M, coef in east_L_image(mask, m).items())


def ell_after_extraction(mask: int, m: int):
    boundary = 1 << (m - 1)
    if not (mask & boundary):
        return F(0)
    reduced = mask & ~boundary
    if m == 1:
        return b
    return b * ell(reduced)


for m in range(1, 10):
    for mask in range(1, 1 << m):
        lhs = ell_after_extraction(mask, m)
        rhs = r * ell_minus_L(mask, m)
        assert lhs == rhs, (m, mask, lhs, rhs)

for m in range(2, 10):
    for mask in range(1, 1 << m):
        expected = F(0)
        if (mask & 1) and (mask & (1 << (m-1))):
            expected = (1+b) * (b ** mask.bit_count())
        assert ell_minus_L(mask, m) == expected

for m in range(2, 10):
    forcing_ell = F(0)
    for i in range(m-1):
        forcing_ell += ell(1 << i)
        forcing_ell += ell((1 << i) | (1 << (i+1)))
    assert forcing_ell == b * (1+b)

q_ell = (r / (b * (1+b))) * (b * (1+b))
assert q_ell == r

print('P* strict residual point verified')
print('B =', B, 'g =', g, 'omega =', omega, 'Z =', Z)
print('m0 =', m0, 'Cstar =', Cstar)
print('strong-growth scaling: r =', r, 'mu =', mu)
print('fixed-depth binary-renewal base r+mu =', lambda_fixed_depth, '=', float(lambda_fixed_depth))
print('first two formal renewal return weights sum =', first_two_return_sum, '=', float(first_two_return_sum))
print('East Green extraction identity verified on all nonempty subsets through m=9')
print('fixed-depth supercritical limit is verified; no claim about rho_J at fixed epsilon is made')
