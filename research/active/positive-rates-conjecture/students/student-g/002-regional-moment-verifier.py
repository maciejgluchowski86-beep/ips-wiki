#!/usr/bin/env python3
"""Exact symbolic checks for Student G Assignment 002.

Checks the decisive formulas in 002-density-to-regional-control.md:

1. regional zero-boundary transfer and the short-cell threshold;
2. the generic two-site L^- weighted-insertion ODE;
3. the killed two-state live-exposure child probabilities h_0,h_1;
4. the live-exposure J-occupation resolvent g_0,g_1;
5. the exact infection-compensator identities;
6. the near-East asymptotics used to show the crude global J bound is
   not itself contractive.

No numerical approximation or Monte Carlo is used.
"""

import sympy as sp

# ---------------------------------------------------------------------------
# Parameters.
# ---------------------------------------------------------------------------

a, b, c, Delta, z = sp.symbols("a b c Delta z", positive=True)
d = b - a
k = 1 - c
B = c + d
rho = c / B
q = 1 - c + a

# ---------------------------------------------------------------------------
# 1. Regional kernel and composition threshold.
# ---------------------------------------------------------------------------

K0 = (1 - sp.exp(-(1 + d) * Delta)) / (1 + d)
Psi0 = sp.expand(B * K0 - c)

# The asymptotic transfer is positive and the threshold identity is exact.
assert sp.factor(B - c * (1 + d) - d * k) == 0
Psi_inf = sp.simplify(B / (1 + d) - c)
assert sp.simplify(Psi_inf - d * k / (1 + d)) == 0

# At the proposed zero exp(-(1+d) Delta)=d k/B, Psi vanishes.
E = sp.symbols("E", positive=True)
Psi0_E = sp.expand(B * (1 - E) / (1 + d) - c)
assert sp.simplify(Psi0_E.subs(E, d * k / B)) == 0

# ---------------------------------------------------------------------------
# 2. Generic two-site L^- weighted insertion ODE.
# ---------------------------------------------------------------------------

x, y = sp.symbols("x y")
Mx, My, Mxy, H = sp.symbols("Mx My Mxy H")


def reduce_xy(poly):
    """Reduce modulo x^2=x, y^2=y."""
    p = sp.Poly(sp.expand(poly), x, y)
    out = 0
    for mon, coeff in p.terms():
        term = coeff
        if mon[0]:
            term *= x
        if mon[1]:
            term *= y
        out += term
    return sp.expand(out)


def flip(poly, var):
    return sp.expand(poly.subs(var, 1 - var) - poly)


def rate(var, right):
    # L^- canonical-spin flip rate:
    # 0->1 at 1-c*right, 1->0 at d*(1-right).
    return sp.expand((1 - var) * (1 - c * right) + var * d * (1 - right))


def Lxy(poly):
    return reduce_xy(
        rate(x, y) * flip(poly, x)
        + rate(y, z) * flip(poly, y)
    )


def expect(poly):
    p = sp.Poly(reduce_xy(poly), x, y)
    table = {
        (0, 0): sp.Integer(1),
        (1, 0): Mx,
        (0, 1): My,
        (1, 1): Mxy,
    }
    return sp.expand(sum(coeff * table[mon] for mon, coeff in p.terms()))


dMx = expect(Lxy(x))
dMy = expect(Lxy(y))
dMxy = expect(Lxy(x * y))
dH = sp.expand(dMxy - rho * dMx).subs(Mxy, H + rho * Mx)

forcing = -rho + (d / B) * Mx + (1 - c * d / B) * My
lam = 2 + d - B * z
assert sp.simplify(dH - (forcing - lam * H)) == 0

epsilon = sp.simplify(forcing.subs({Mx: rho, My: rho}))
assert sp.simplify(epsilon - c * d * k / B**2) == 0

# ---------------------------------------------------------------------------
# 3. Live-exposure killed chain.
# ---------------------------------------------------------------------------

Den = sp.expand((b + q) * (1 + q) - a * k)
h0 = sp.simplify((d * (1 + q) + a * c) / Den)
h1 = sp.simplify((c * (b + q) + k * d) / Den)

# Backward equations.
assert sp.simplify((b + q) * h0 - (d + a * h1)) == 0
assert sp.simplify((1 + q) * h1 - (c + k * h0)) == 0

# Exact positive gaps and ordering.
assert sp.simplify((1 - h0) - q * (a + q + 1) / Den) == 0
assert sp.simplify((1 - h1) - q * (d + 2 * q) / Den) == 0
assert sp.simplify((h1 - h0) - q * (c - d) / Den) == 0

# ---------------------------------------------------------------------------
# 4. J-occupation resolvent.
# ---------------------------------------------------------------------------

g0 = sp.simplify(a / Den)
g1 = sp.simplify((b + q) / Den)

# Resolvent equations for reward 1 in state J and reward 0 in state K.
assert sp.simplify((b + q) * g0 - a * g1) == 0
assert sp.simplify((1 + q) * g1 - (1 + k * g0)) == 0

# K-occupation times under the same comparison chain.
f0 = sp.simplify((1 + q) / Den)
f1 = sp.simplify(k / Den)

# Infection compensator = d*K occupation + c*J occupation = h_x.
assert sp.simplify(d * f0 + c * g0 - h0) == 0
assert sp.simplify(d * f1 + c * g1 - h1) == 0

# ---------------------------------------------------------------------------
# 5. Near-East stress path.
# ---------------------------------------------------------------------------

eps = sp.symbols("eps", positive=True)
subs = {
    a: eps**2,
    b: eps,
    c: 1 - eps**2,
}

q_e = sp.simplify(q.subs(subs))
g1_e = sp.simplify(g1.subs(subs))
assert sp.simplify(q_e - 2 * eps**2) == 0

# g1 = 1 - 2 eps^2 + O(eps^3).
series_g1 = sp.series(g1_e, eps, 0, 4).removeO()
assert sp.expand(series_g1 - (1 - 2 * eps**2 + eps**3)) == 0

# q-(c-d)g1 has constant term -1, so the crude global substitution
# cannot yield near-East same-site damping.
bad_damping = sp.simplify((q - (c - d) * g1).subs(subs))
assert sp.limit(bad_damping, eps, 0, dir="+") == -1

print("regional short-cell threshold: verified")
print("two-site weighted insertion ODE: verified")
print("live-exposure child probabilities: verified")
print("live-exposure J resolvent and compensator: verified")
print("near-East obstruction for crude global J summation: verified")
