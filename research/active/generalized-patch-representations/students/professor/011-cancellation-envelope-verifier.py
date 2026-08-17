from fractions import Fraction

# Exact verifier for Assignment 011 Part B.
# No floating-point literals or numerical sign decisions.

counts = {
    "potts_gate": 0,
    "eigenmodes": 0,
    "signed_response": 0,
    "raw_response": 0,
    "strict_gap": 0,
}

# Assignment-010 Potts gate: z=1/2, q=1.
p = (Fraction(3, 16), Fraction(5, 16), Fraction(-3, 16))
Lambda = sum(abs(x) for x in p)
assert Lambda == Fraction(11, 16)
counts["potts_gate"] += 1

# Incoming terminal target type 2: f_2^I=e_0+e_2.
# Active symmetric/antisymmetric modes of F(t)=exp(tK) f_2^I are
# s(t)=1/18+(4/9)e^{-9t/8}, d(t)=-(1/2)e^{-3t}.
# At t_*=(8/3)log(5/4), both exponentials are rational.
exp_symmetric = Fraction(4, 5) ** 3
exp_antisymmetric = Fraction(4, 5) ** 8
assert exp_symmetric == Fraction(64, 125)
counts["eigenmodes"] += 1
assert exp_antisymmetric == Fraction(65536, 390625)
counts["eigenmodes"] += 1

s = Fraction(1, 18) + Fraction(4, 9) * exp_symmetric
d = -Fraction(1, 2) * exp_antisymmetric
assert s == Fraction(637, 2250)
counts["eigenmodes"] += 1
assert d == Fraction(-32768, 390625)
counts["eigenmodes"] += 1

# Signed local numerator p exp(tK) f_2^I.
N = Fraction(3, 16) + s / 8 + d / 2
assert N == Fraction(2544551, 14062500)
counts["signed_response"] += 1
assert N > 0
counts["signed_response"] += 1

# Raw absolute local numerator |p| exp(tK) f_2^I.
# Here the empty-target K is Metzler, so the raw absolute interior transfer M equals K.
G = Fraction(3, 16) + s / 2 + d / 8
assert G == Fraction(17919551, 56250000)
counts["raw_response"] += 1
assert G > 0
counts["raw_response"] += 1

F_signed = N / Lambda
F_raw = G / Lambda
assert F_signed == Fraction(10178204, 38671875)
counts["strict_gap"] += 1
assert F_raw == Fraction(17919551, 38671875)
counts["strict_gap"] += 1
assert F_signed < F_raw
counts["strict_gap"] += 1
assert F_raw - F_signed == Fraction(2580449, 12890625)
counts["strict_gap"] += 1

# Zero-length diagnostic: hidden outcomes 0 and 2 cancel exactly at an incoming type-2 boundary.
assert p[0] + p[2] == 0
counts["strict_gap"] += 1
assert abs(p[0]) + abs(p[2]) == Fraction(3, 8)
counts["strict_gap"] += 1

print("Assignment 011 cancellation-envelope verifier passed")
for name, value in counts.items():
    print(f"{name}: {value}")
print(f"total: {sum(counts.values())}")
print(f"signed normalized patch factor: {F_signed}")
print(f"raw absolute normalized patch factor: {F_raw}")
print(f"exact strict gap: {F_raw - F_signed}")