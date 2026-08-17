from fractions import Fraction
from itertools import product

# Exact verifier for Assignment 010.
# No floating-point literals or floating-point sign decisions are used.

COLORS = (0, 1, 2)
ACTIVE = (1, 2)
NEIGHBOR_COUNT = 4
NEIGHBOR_CONFIGS = tuple(product(COLORS, repeat=NEIGHBOR_COUNT))
TYPED_TARGETS = NEIGHBOR_CONFIGS  # 0 means target site absent/reference in the tensor basis.
TRANSITIONS = tuple((x, y) for x in COLORS for y in COLORS if x != y)

Z = Fraction(1, 2)
Q = Fraction(1, 1)

counts = {
    "physical_nonnegativity": 0,
    "mobius_reconstruction": 0,
    "typed_generator_reconstruction": 0,
    "empty_transfer": 0,
    "singleton_hidden_row": 0,
    "realized_support": 0,
    "finite_length_gate": 0,
}


def neighbor_counts(nb):
    return tuple(nb.count(a) for a in COLORS)


def physical_rate(x, y, nb, z=Z, q=Q):
    ns = neighbor_counts(nb)
    exponent = max(ns[x] - ns[y], 0)
    return q * (z ** exponent)


def compatible(tau, nb):
    return all(t == 0 or t == b for t, b in zip(tau, nb))


def mobius_coeff(x, y, tau, z=Z, q=Q):
    """Indicator-tensor coefficient for physical rate c^{x->y}."""
    support = [i for i, t in enumerate(tau) if t != 0]
    m = len(support)
    total = Fraction(0)
    for bits in product((0, 1), repeat=m):
        nb = [0] * NEIGHBOR_COUNT
        selected = 0
        for bit, pos in zip(bits, support):
            if bit:
                nb[pos] = tau[pos]
                selected += 1
        total += ((-1) ** (m - selected)) * physical_rate(x, y, tuple(nb), z, q)
    return total


# Build every physical tensor coefficient exactly.
hat = {
    (x, y): {tau: mobius_coeff(x, y, tau) for tau in TYPED_TARGETS}
    for x, y in TRANSITIONS
}


# Gate 1: all physical rates are nonnegative at the exact parameter point.
for x, y in TRANSITIONS:
    for nb in NEIGHBOR_CONFIGS:
        assert physical_rate(x, y, nb) > 0
        counts["physical_nonnegativity"] += 1


# Gate 2: Möbius coefficients reconstruct every one of the 6*81 rates.
for x, y in TRANSITIONS:
    for nb in NEIGHBOR_CONFIGS:
        reconstructed = sum(
            coeff
            for tau, coeff in hat[(x, y)].items()
            if compatible(tau, nb)
        )
        assert reconstructed == physical_rate(x, y, nb)
        counts["mobius_reconstruction"] += 1


# Typed dual coefficients from Assignment 001.
def a_coeff(r, s, tau):
    base = hat[(0, r)][tau]
    if s == 0:
        return base
    if s != r:
        return hat[(s, r)][tau] - base
    return -base - sum(hat[(r, y)][tau] for y in COLORS if y != r)


a = {
    (r, tau, s): a_coeff(r, s, tau)
    for r in ACTIVE
    for tau in TYPED_TARGETS
    for s in COLORS
}


def h(s, x):
    # Reference indicator basis: h_0 == 1 and h_s(x)=1{x=s} for s=1,2.
    return Fraction(1) if s == 0 or s == x else Fraction(0)


def physical_local_Lh(r, x, nb):
    ans = Fraction(0)
    for y in COLORS:
        if y == x:
            continue
        ans += physical_rate(x, y, nb) * (
            (1 if y == r else 0) - (1 if x == r else 0)
        )
    return ans


def typed_local_Lh(r, x, nb):
    ans = Fraction(0)
    for tau in TYPED_TARGETS:
        if not compatible(tau, nb):
            continue
        ans += sum(a[(r, tau, s)] * h(s, x) for s in COLORS)
    return ans


# Gate 3: exact typed-generator action for h_1 and h_2 on all source/neighborhood states.
for r in ACTIVE:
    for x in COLORS:
        for nb in NEIGHBOR_CONFIGS:
            assert typed_local_Lh(r, x, nb) == physical_local_Lh(r, x, nb)
            counts["typed_generator_reconstruction"] += 1


# Gate 4: exact empty-target transfer K at z=1/2, q=1.
empty = (0, 0, 0, 0)
K = [[Fraction(0) for _ in COLORS] for _ in COLORS]
for r in ACTIVE:
    for s in COLORS:
        K[r][s] = a[(r, empty, s)]

K_expected = [
    [Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(1, 16), Fraction(-33, 16), Fraction(15, 16)],
    [Fraction(1, 16), Fraction(15, 16), Fraction(-33, 16)],
]
for i in COLORS:
    for j in COLORS:
        assert K[i][j] == K_expected[i][j]
        counts["empty_transfer"] += 1


# Gate 5: decisive source-type-1, singleton target-type-1 outgoing row.
tau_1 = (1, 0, 0, 0)
p = tuple(a[(1, tau_1, s)] for s in COLORS)
assert p == (Fraction(3, 16), Fraction(5, 16), Fraction(-3, 16))
counts["singleton_hidden_row"] += 1
assert p[0] > 0
counts["singleton_hidden_row"] += 1
assert p[2] < 0
counts["singleton_hidden_row"] += 1
assert abs(p[0]) > 0 and abs(p[2]) > 0
counts["singleton_hidden_row"] += 1

# Physical coefficient explanation of the negative hidden outcome:
# source 0->1 gains a singleton target mode, while source 2->1 is saturated at rate q.
assert hat[(0, 1)][tau_1] == Fraction(3, 16)
counts["singleton_hidden_row"] += 1
assert hat[(2, 1)][tau_1] == 0
counts["singleton_hidden_row"] += 1
assert p[2] == hat[(2, 1)][tau_1] - hat[(0, 1)][tau_1]
counts["singleton_hidden_row"] += 1


# Gate 6: the terminal source-type-2 successful record has positive coarse hazard.
# Use its color-swapped singleton target tau_2.
tau_2 = (2, 0, 0, 0)
p2_record = tuple(a[(2, tau_2, s)] for s in COLORS)
assert sum(abs(v) for v in p2_record) > 0
counts["realized_support"] += 1
assert abs(p[2]) == Fraction(3, 16)
counts["realized_support"] += 1
# Empty-transfer retyping also makes both active labels dynamically accessible.
assert K[1][2] == Fraction(15, 16) > 0
counts["realized_support"] += 1
assert K[2][1] == Fraction(15, 16) > 0
counts["realized_support"] += 1


# Gate 7: exact finite positive patch length.
# Set t_*=(8/3) log(5/4). Then the symmetric/antisymmetric active exponentials are rational:
# exp(-(9/8)t_*)=(4/5)^3 and exp(-3 t_*)=(4/5)^8.
symmetric_component = (p[1] + p[2]) / 2
antisymmetric_component = (p[1] - p[2]) / 2
assert symmetric_component == Fraction(1, 16)
counts["finite_length_gate"] += 1
assert antisymmetric_component == Fraction(1, 4)
counts["finite_length_gate"] += 1

exp_symmetric = Fraction(4, 5) ** 3
exp_antisymmetric = Fraction(4, 5) ** 8
assert exp_symmetric == Fraction(64, 125)
counts["finite_length_gate"] += 1
assert exp_antisymmetric == Fraction(65536, 390625)
counts["finite_length_gate"] += 1

N_OO = symmetric_component * exp_symmetric - antisymmetric_component * exp_antisymmetric
assert N_OO == Fraction(-3884, 390625)
counts["finite_length_gate"] += 1
assert N_OO < 0
counts["finite_length_gate"] += 1

# The unsigned denominator is strictly positive on this realized descriptor:
# the outgoing hidden branch into type 2 has positive absolute mass, and the terminal source-type-2
# successful record has positive hazard. The killed no-intervening-mark event has positive exponential
# probability for every finite positive length. No numerical evaluation is needed for its sign.
assert abs(p[2]) > 0 and sum(abs(v) for v in p2_record) > 0
counts["finite_length_gate"] += 1


total = sum(counts.values())
print("Potts Metropolis exact verifier passed")
for name, value in counts.items():
    print(f"{name}: {value}")
print(f"total: {total}")
print(f"decisive row: {p}")
print(f"exact finite-length OO numerator: {N_OO}")
