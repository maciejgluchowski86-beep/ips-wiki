#!/usr/bin/env python3
"""
Exact symbolic checks for Student G assignment 002.

Variables are canonical spins (v,x,y) in {0,1}, with prescribed right
boundary z in {0,1}. On the normalized residual face set

    d = b-a,  k = 1-c,  B = c+d,  rho = c/B.

For L^- the local rates at a source s with right neighbour r are

    0 -> 1 at rate 1-c r,
    1 -> 0 at rate d(1-r).

The script verifies:
  (1) the two-site insertion ODE for H=E[(y-rho)x];
  (2) the complete three-site rho-centered moment system used for
      two-cell composition;
  (3) the exact density-only counterexample at
      (a,b,c)=(1,11,999)/1000.
"""

import sympy as sp

c, d, z = sp.symbols("c d z", positive=True)
B = c + d
k = 1 - c
rho = c / B
h = d * k / B
r = d / B

v, x, y = sp.symbols("v x y")
V, X, Y = sp.symbols("V X Y")


def multilinear(poly):
    """Reduce a polynomial modulo v^2=v, x^2=x, y^2=y."""
    p = sp.Poly(sp.expand(poly), v, x, y)
    out = 0
    for mon, coeff in p.terms():
        term = coeff
        if mon[0]:
            term *= v
        if mon[1]:
            term *= x
        if mon[2]:
            term *= y
        out += term
    return sp.expand(out)


def flip_increment(poly, var):
    return sp.expand(poly.subs(var, 1 - var) - poly)


def local_rate(var, right):
    return sp.expand((1 - var) * (1 - c * right) + var * d * (1 - right))


def L(poly):
    out = (
        local_rate(v, x) * flip_increment(poly, v)
        + local_rate(x, y) * flip_increment(poly, x)
        + local_rate(y, z) * flip_increment(poly, y)
    )
    return multilinear(out)


# ---------------------------------------------------------------------------
# Two-site insertion equation.
# ---------------------------------------------------------------------------

Mx, My, Mxy = sp.symbols("Mx My Mxy")
H = sp.symbols("H")


def expect_xy(poly):
    p = sp.Poly(multilinear(poly), x, y)
    table = {
        (0, 0): sp.Integer(1),
        (1, 0): Mx,
        (0, 1): My,
        (1, 1): Mxy,
    }
    return sp.expand(sum(coeff * table[mon] for mon, coeff in p.terms()))


def Lxy(poly):
    out = (
        local_rate(x, y) * flip_increment(poly, x)
        + local_rate(y, z) * flip_increment(poly, y)
    )
    return multilinear(out)


dMx = expect_xy(Lxy(x))
dMy = expect_xy(Lxy(y))
dMxy = expect_xy(Lxy(x * y))
dH = sp.expand(dMxy - rho * dMx).subs(Mxy, H + rho * Mx)

lam = 2 + d - B * z
forcing = -rho + (d / B) * Mx + (1 - c * d / B) * My

assert sp.simplify(dH - (forcing - lam * H)) == 0

epsilon = sp.simplify(forcing.subs({Mx: rho, My: rho}))
assert sp.simplify(epsilon - c * d * k / B**2) == 0


# ---------------------------------------------------------------------------
# Three-site centered-moment system.
# ---------------------------------------------------------------------------

gv = v - rho
gx = x - rho
gy = y - rho


def centered_coefficients(poly):
    expr = sp.expand(L(poly).subs({v: V + rho, x: X + rho, y: Y + rho}))
    return {
        mon: sp.factor(coeff)
        for mon, coeff in sp.Poly(expr, V, X, Y).terms()
    }


expected = {
    "u2": {
        (0, 0, 1): -(1 + d - B * z),
        (0, 0, 0): h,
    },
    "u1": {
        (0, 1, 1): B,
        (0, 1, 0): -(k + d),
        (0, 0, 0): h,
    },
    "u0": {
        (1, 1, 0): B,
        (1, 0, 0): -(k + d),
        (0, 0, 0): h,
    },
    "u12": {
        (0, 1, 1): -(2 + d - B * z),
        (0, 1, 0): r,
        (0, 0, 1): h,
    },
    "u01": {
        (1, 1, 1): B,
        (1, 1, 0): -(2 + d - c),
        (1, 0, 0): r,
        (0, 1, 0): h,
    },
    "u02": {
        (1, 1, 1): B,
        (1, 0, 1): -(2 + 2 * d - c - B * z),
        (1, 0, 0): h,
        (0, 0, 1): h,
    },
    "u012": {
        (1, 1, 1): -(3 + d - B * z),
        (1, 1, 0): r,
        (1, 0, 1): r,
        (0, 1, 1): h,
    },
}

actual = {
    "u2": centered_coefficients(gy),
    "u1": centered_coefficients(gx),
    "u0": centered_coefficients(gv),
    "u12": centered_coefficients(gx * gy),
    "u01": centered_coefficients(gv * gx),
    "u02": centered_coefficients(gv * gy),
    "u012": centered_coefficients(gv * gx * gy),
}

for name in expected:
    keys = set(expected[name]) | set(actual[name])
    for key in keys:
        lhs = actual[name].get(key, 0)
        rhs = expected[name].get(key, 0)
        assert sp.simplify(lhs - rhs) == 0, (name, key, lhs, rhs)


# ---------------------------------------------------------------------------
# Exact density-only counterexample.
# ---------------------------------------------------------------------------

a0 = sp.Rational(1, 1000)
b0 = sp.Rational(11, 1000)
c0 = sp.Rational(999, 1000)
d0 = b0 - a0
B0 = c0 + d0
rho0 = c0 / B0
p0 = 1 / (1 + d0)
w0 = 2 * p0 - 1

counter = sp.simplify(
    c0 * (p0 - rho0)
    + B0 * (w0 - rho0 * p0)
)
assert counter == -sp.Rational(4041, 50954500)

print("two-site insertion ODE: verified")
print("three-site centered moment system: verified")
print("density-only counterexample:", counter)
