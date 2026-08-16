#!/usr/bin/env python3
"""Exact symbolic checks for Student G Assignment 003.

Checks:
1. the E7 geometric minorant and its exponential height factor phi(lambda);
2. the same-parent restart pgf M(s) and the explicit admissible s-window;
3. the finite-height truncation correction used in the Foster inequality;
4. the near-East stress choice lambda=2, s=1+eps^2/4, for which the
   restart-corrected large-height multiplier tends to 16/21 < 1.
"""

import sympy as sp

B, omega, lam, h, s = sp.symbols(
    "B omega lam h s", positive=True
)

alpha = (B + omega) / (B + 2 * omega)

# K-minorant: P(kappa=0)=1-alpha, P(kappa=j)=alpha*2^{-j}, j>=1.
E_lam_minus_kappa = sp.simplify(
    (1 - alpha) + alpha / (2 * lam - 1)
)
phi = sp.simplify(lam * E_lam_minus_kappa)

target_phi_minus_one = (
    (lam - 1) * (-B + 2 * lam * omega - 2 * omega)
    / ((B + 2 * omega) * (2 * lam - 1))
)
assert sp.simplify((phi - 1) - target_phi_minus_one) == 0

lam_star = sp.simplify(1 / (2 * (1 - alpha)))
assert sp.simplify(
    lam_star - (B + 2 * omega) / (2 * omega)
) == 0

# Same-parent restart pgf from P(N>=n)<=h^(n-1).
M = sp.simplify((1 - h) * s / (1 - h * s))

# M(s)*phi<1 iff s < 1/[h+(1-h)phi].
s_star = sp.simplify(1 / (h + (1 - h) * phi))
target_gap = (
    1 - s * (h + (1 - h) * phi)
) / (1 - h * s)
assert sp.simplify((1 - M * phi) - target_gap) == 0

# Finite-height truncation correction:
# lambda E[lambda^{-min(kappa,H)}] - phi
# <= 2 alpha lambda (2 lambda)^(-H).
H = sp.symbols("H", integer=True, positive=True)
tail = alpha * 2 ** (-(H - 1))
correction_bound = sp.simplify(lam ** (1 - H) * tail)
assert sp.simplify(
    correction_bound - 2 * alpha * lam * (2 * lam) ** (-H)
) == 0

# Near-East stress path.
eps = sp.symbols("eps", positive=True)
a_e = eps**2
b_e = eps
c_e = 1 - eps**2
B_e = sp.simplify(b_e + c_e - a_e)
omega_e = sp.simplify(1 - c_e + a_e)
d_e = sp.simplify(b_e - a_e)

Den_e = sp.expand(
    (b_e + omega_e) * (1 + omega_e)
    - a_e * (1 - c_e)
)
h1_e = sp.simplify(
    (c_e * (b_e + omega_e) + (1 - c_e) * d_e) / Den_e
)
alpha_e = sp.simplify(
    (B_e + omega_e) / (B_e + 2 * omega_e)
)

# lambda=2, s=1+eps^2/4.
phi2_e = sp.simplify(
    2 * ((1 - alpha_e) + alpha_e / 3)
)
s_e = 1 + eps**2 / 4
M_e = sp.simplify(
    (1 - h1_e) * s_e / (1 - h1_e * s_e)
)
chi_e = sp.simplify(M_e * phi2_e)

assert sp.limit(h1_e, eps, 0, dir="+") == 1
assert sp.limit(alpha_e, eps, 0, dir="+") == 1
assert sp.limit(phi2_e, eps, 0, dir="+") == sp.Rational(2, 3)
assert sp.limit(M_e, eps, 0, dir="+") == sp.Rational(8, 7)
assert sp.limit(chi_e, eps, 0, dir="+") == sp.Rational(16, 21)

print("height minorant and phi(lambda): verified")
print("restart pgf and admissible s-window: verified")
print("finite-height correction: verified")
print(
    "near-East restart-corrected multiplier ->",
    sp.limit(chi_e, eps, 0, dir="+"),
)
