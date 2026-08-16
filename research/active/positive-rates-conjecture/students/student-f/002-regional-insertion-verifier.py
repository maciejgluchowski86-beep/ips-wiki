"""Exact arithmetic/formula check for Student F assignment 002.

The script verifies the explicit residual parameter point
    a=1/10, b=3/10, c=4/5,
computes the one-site zero-boundary L^- cell kernel
    K_Delta(z)=p0+(z-p0) exp(-(1+d)Delta),
and checks that the hidden predecessor transfer
    Psi_Delta(z)=B K_Delta(z)-c
is negative for a short cell but positive after the one-site burn-in.

No simulation is used.
"""

from fractions import Fraction
from math import exp, log, sqrt


a = Fraction(1, 10)
b = Fraction(3, 10)
c = Fraction(4, 5)

d = b - a
k = 1 - c
B = b + c - a
rho = c / B
lam = 1 + d
p0 = 1 / lam

assert 0 < a < b
assert Fraction(1, 2) <= c < 1
assert c >= a + b
assert float(b) >= sqrt(2.0) * float(1 - c)


def K(delta: float, z: int) -> float:
    return float(p0) + (z - float(p0)) * exp(-float(lam) * delta)


def Psi(delta: float, z: int) -> float:
    return float(B) * K(delta, z) - float(c)


tau_star = log(float(B / (d * k))) / float(lam)
T_rho = log(float(B / (d * k))) / float(k)

# A short predecessor cell.
delta = 0.1
psi_short = Psi(delta, 0)
assert delta < tau_star
assert psi_short < 0

# A long source cell, beyond the Professor-verified one-site burn-in.
u = 20.0
psi_long = Psi(u, 0)
assert u > T_rho
assert psi_long > 0

product = psi_short * psi_long
assert product < 0

print(f"a={float(a):.12g}, b={float(b):.12g}, c={float(c):.12g}")
print(f"B={float(B):.12g}, rho={float(rho):.12g}")
print(f"tau_star={tau_star:.12g}")
print(f"T_rho={T_rho:.12g}")
print(f"K(0.1,0)={K(delta,0):.12g}")
print(f"Psi(0.1,0)={psi_short:.12g}")
print(f"K(20,0)={K(u,0):.12g}")
print(f"Psi(20,0)={psi_long:.12g}")
print(f"two_cell_product={product:.12g}")
