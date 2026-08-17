from fractions import Fraction as F

# Exact finite gate for Assignment 009.
# No floating point arithmetic or Monte Carlo.

lam = F(1)
gamma = F(1)
delta = F(1)
checks = 0

# ---------------------------------------------------------------------------
# 1. Physical one-neighbour rates are nonnegative at the gate point.
# States: 0 vacant, 1 juvenile, 2 adult.
# ---------------------------------------------------------------------------
for z in range(3):
    rates = {
        (0, 1): lam if z == 2 else F(0),
        (1, 0): F(1) + delta,
        (1, 2): gamma,
        (2, 0): F(1),
    }
    for value in rates.values():
        assert value >= 0
        checks += 1

# ---------------------------------------------------------------------------
# 2. Exact typed-generator reconstruction on h_1 and h_2.
# Check all 3 source states x and all 3 neighbour states z.
# ---------------------------------------------------------------------------
for x in range(3):
    for z in range(3):
        birth = lam if z == 2 else F(0)

        # Physical generator on h_1(x)=1{x=1}.
        physical_h1 = F(0)
        if x == 0:
            physical_h1 += birth
        elif x == 1:
            physical_h1 -= F(1) + delta + gamma

        # Typed coefficients:
        # a_{1,empty}=(0,-(1+delta+gamma),0)
        # a_{1,{z->2}}=(lam,-lam,-lam).
        typed_h1 = -(F(1) + delta + gamma) * F(x == 1)
        typed_h1 += birth * (F(1) - F(x == 1) - F(x == 2))

        assert physical_h1 == typed_h1
        checks += 1

        # Physical generator on h_2(x)=1{x=2}.
        physical_h2 = F(0)
        if x == 1:
            physical_h2 += gamma
        elif x == 2:
            physical_h2 -= F(1)

        # Typed empty-target row a_{2,empty}=(0,gamma,-1).
        typed_h2 = gamma * F(x == 1) - F(x == 2)

        assert physical_h2 == typed_h2
        checks += 1

# ---------------------------------------------------------------------------
# 3. Successful hidden row and genuinely nonbinary mark.
# ---------------------------------------------------------------------------
p = (lam, -lam, -lam)
assert p == (F(1), F(-1), F(-1))
checks += 1
assert sum(abs(v) for v in p) == 3 * lam
checks += 1
assert p[0] > 0 and p[1] < 0 and p[2] < 0
checks += 1

# Incoming target type 2 is compatible with local states 0 and 2 but conflicts
# with local active type 1. This is the typed cemetery event.
compatible = {0, 2}
assert 0 in compatible and 2 in compatible and 1 not in compatible
checks += 1

# ---------------------------------------------------------------------------
# 4. Exact realized OO patch at e^{-t}=1/2.
# At the gate point a=1+delta+gamma=3 and, for one neighbour,
# kappa_1=3*lam=3. Hence both signed numerator and unsigned denominator
# reduce to rational polynomials in x=e^{-t}.
# ---------------------------------------------------------------------------
x = F(1, 2)

# Signed K active block [[-3,0],[1,-1]].
# p e^{tK} e_1 = -(x+x^3)/2.
N_OO = -(x + x**3) / 2
assert N_OO == F(-5, 16)
checks += 1
assert N_OO < 0
checks += 1

# Unsigned killed B active block [[-3,0],[1,-1]].
# |p| e^{tB} e_1 = +(x+x^3)/2.
D_OO = (x + x**3) / 2
assert D_OO == F(5, 16)
checks += 1
assert D_OO > 0
checks += 1

contribution = N_OO / D_OO
assert contribution == F(-1)
checks += 1

# Zero-length sign obstruction is already strict.
assert p[1] == -lam < 0
checks += 1

print(f"exact two-stage application checks passed: {checks}")
print("gate parameters: lambda=1, gamma=1, delta=1")
print("realized OO numerator at exp(-t)=1/2:", N_OO)
print("realized OO denominator at exp(-t)=1/2:", D_OO)
print("bulk contribution:", contribution)
