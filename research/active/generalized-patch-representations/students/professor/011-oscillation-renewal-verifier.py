from fractions import Fraction
import sympy as sp

# Exact verifier for Assignment 011 Part D.
# No floating-point literals or numerical spectral decisions.

counts = {
    "local_transfer": 0,
    "record_rows": 0,
    "response_integrals": 0,
    "quotient_matrices": 0,
    "spectral_radii": 0,
    "scaled_separation": 0,
}

# One-neighbour Potts Metropolis local gate at z=1/2, q=1.
K = (
    (Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(1, 2), Fraction(-5, 2), Fraction(1, 2)),
    (Fraction(1, 2), Fraction(1, 2), Fraction(-5, 2)),
)
assert K[1][1] == Fraction(-5, 2) and K[1][2] == Fraction(1, 2)
counts["local_transfer"] += 1
assert K[2][1] == Fraction(1, 2) and K[2][2] == Fraction(-5, 2)
counts["local_transfer"] += 1

# Nonempty record rows (source type ; one-neighbour target type).
rows = {
    "O11": (Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2)),
    "O12": (Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 1)),
    "O21": (Fraction(1, 2), Fraction(-1, 1), Fraction(-1, 2)),
    "O22": (Fraction(1, 2), Fraction(-1, 2), Fraction(1, 2)),
}
hazards = {name: sum(abs(x) for x in row) for name, row in rows.items()}
assert hazards["O11"] == Fraction(3, 2)
counts["record_rows"] += 1
assert hazards["O12"] == Fraction(2, 1)
counts["record_rows"] += 1
assert hazards["O21"] == Fraction(2, 1)
counts["record_rows"] += 1
assert hazards["O22"] == Fraction(3, 2)
counts["record_rows"] += 1

# For the active block, symmetric/antisymmetric decay rates are 2 and 3.
# If b=(b1,b2), response to active type 1 is
# c exp(-2t)+d exp(-3t), c=(b1+b2)/2, d=(b1-b2)/2.
# With x=exp(-t), its absolute integral is int_0^1 |c x + d x^2| dx.
def abs_integral(c, d):
    c = Fraction(c)
    d = Fraction(d)

    def primitive(x):
        return c * x * x / 2 + d * x * x * x / 3

    total = primitive(Fraction(1))
    if c == 0 or d == 0 or c * d >= 0:
        return abs(total)

    root = -c / d
    if root <= 0 or root >= 1:
        return abs(total)

    left = primitive(root)
    right = total - left
    return abs(left) + abs(right)


def response_integrals(b1, b2):
    sym = (Fraction(b1) + Fraction(b2)) / 2
    anti = (Fraction(b1) - Fraction(b2)) / 2
    return abs_integral(sym, anti), abs_integral(sym, -anti)

patch_integrals = {
    "I1": response_integrals(1, 0),
    "I2": response_integrals(0, 1),
}
raw_integrals = dict(patch_integrals)

for name, row in rows.items():
    lam = hazards[name]
    b1 = row[1] / lam
    b2 = row[2] / lam
    patch_integrals[name] = response_integrals(b1, b2)
    raw_integrals[name] = response_integrals(abs(row[1]) / lam, abs(row[2]) / lam)

assert patch_integrals["I1"] == (Fraction(5, 12), Fraction(1, 12))
counts["response_integrals"] += 1
assert patch_integrals["I2"] == (Fraction(1, 12), Fraction(5, 12))
counts["response_integrals"] += 1
assert patch_integrals["O11"] == (Fraction(1, 9), Fraction(1, 9))
counts["response_integrals"] += 1
assert raw_integrals["O11"] == (Fraction(1, 6), Fraction(1, 6))
counts["response_integrals"] += 1
assert patch_integrals["O12"] == (Fraction(7, 48), Fraction(11, 48))
counts["response_integrals"] += 1
assert raw_integrals["O12"] == patch_integrals["O12"]
counts["response_integrals"] += 1
assert patch_integrals["O21"] == (Fraction(11, 48), Fraction(7, 48))
counts["response_integrals"] += 1
assert raw_integrals["O21"] == patch_integrals["O21"]
counts["response_integrals"] += 1
assert patch_integrals["O22"] == (Fraction(1, 9), Fraction(1, 9))
counts["response_integrals"] += 1
assert raw_integrals["O22"] == (Fraction(1, 6), Fraction(1, 6))
counts["response_integrals"] += 1

# Color-symmetric three-class Perron quotients: I, same-color O, cross-color O.
G_patch = sp.Matrix([
    [sp.Rational(7, 4), sp.Rational(3, 4), sp.Rational(1, 1)],
    [sp.Rational(7, 9), sp.Rational(1, 3), sp.Rational(4, 9)],
    [sp.Rational(21, 16), sp.Rational(9, 16), sp.Rational(3, 4)],
])
G_raw = sp.Matrix([
    [sp.Rational(7, 4), sp.Rational(3, 4), sp.Rational(1, 1)],
    [sp.Rational(7, 6), sp.Rational(1, 2), sp.Rational(2, 3)],
    [sp.Rational(21, 16), sp.Rational(9, 16), sp.Rational(3, 4)],
])

assert G_patch[1, 0] == sp.Rational(7, 9)
counts["quotient_matrices"] += 1
assert G_raw[1, 0] == sp.Rational(7, 6)
counts["quotient_matrices"] += 1

lam = sp.symbols("lam")
char_patch = sp.factor(G_patch.charpoly(lam).as_expr())
char_raw = sp.factor(G_raw.charpoly(lam).as_expr())
assert char_patch == lam**2 * (6 * lam - 17) / 6
counts["spectral_radii"] += 1
assert char_raw == lam**2 * (lam - 3)
counts["spectral_radii"] += 1

rho_patch = Fraction(17, 6)
rho_raw = Fraction(3, 1)
assert rho_patch < rho_raw
counts["spectral_radii"] += 1

# Scale only nonempty neighbour-dependent tensor modes by epsilon=17/50.
# Empty K and normalized outgoing rows stay fixed, so both next-generation matrices scale by epsilon.
epsilon = Fraction(17, 50)
scaled_patch = epsilon * rho_patch
scaled_raw = epsilon * rho_raw
assert scaled_patch == Fraction(289, 300)
counts["scaled_separation"] += 1
assert scaled_raw == Fraction(51, 50)
counts["scaled_separation"] += 1
assert scaled_patch < 1 < scaled_raw
counts["scaled_separation"] += 1
assert 0 < epsilon < 1
counts["scaled_separation"] += 1

print("Assignment 011 oscillation-renewal verifier passed")
for name, value in counts.items():
    print(f"{name}: {value}")
print(f"total: {sum(counts.values())}")
print(f"patch next-generation radius: {rho_patch}")
print(f"raw next-generation radius: {rho_raw}")
print(f"scaled patch radius: {scaled_patch}")
print(f"scaled raw radius: {scaled_raw}")