#!/usr/bin/env python3
"""Exact algebraic verifier for Student G checkpoints 010e/010f.

The only non-rational objects are the two algebraic decay rates of the
one-particle survival function. SymPy keeps their square root exactly and all
algebraic inequalities below are exact symbolic comparisons.

Checks:
1. the phase-type decomposition of the actual P_* duration kernel;
2. the five exponential coefficients of the terminal kernel kappa;
3. their sign pattern;
4. the coefficientwise L1 upper bound theta_triangle < 1;
5. a cancellation-improved algebraic bound theta_sharp < 1/B, using only
   elementary exponential inequalities described in 010f.
"""

import sympy as sp


a = sp.Rational(1, 1000)
b = sp.Rational(1, 10)
c = sp.Rational(9999, 10000)
B = b + c - a
g = b - a
omega = 1 - c + a
tau = sp.Rational(4, 125)
r = 1 + b

epsilon = sp.Rational(9, 10000)
g0 = g + epsilon

d = b * (1 - c) - a
assert d == -epsilon * r
assert d - g * r == -g0 * r

# The Laplace transform of s_1 is
#   Z_alpha=(alpha+C)/((alpha+rho_-)(alpha+rho_+)).
C = 1 + B + a
disc = sp.factor(C**2 - 4 * a * B)
sqrt_disc = sp.sqrt(disc)
rho_minus = sp.factor((C - sqrt_disc) / 2)
rho_plus = sp.factor((C + sqrt_disc) / 2)
assert rho_minus > 0
assert rho_plus > rho_minus
assert sp.simplify(rho_minus + rho_plus - C) == 0
assert sp.simplify(rho_minus * rho_plus - a * B) == 0

u_minus = sp.factor(rho_plus / (rho_plus - rho_minus))
u_plus = sp.factor(-rho_minus / (rho_plus - rho_minus))
assert u_minus > 0
assert u_plus < 0
assert sp.factor(u_minus + u_plus) == 1

# h(t)=w_*(t) sigma(t) as a four-exponential signed kernel.
h_terms = [
    (u_minus, omega + rho_minus),
    (-2 * u_minus, omega + tau + rho_minus),
    (u_plus, omega + rho_plus),
    (-2 * u_plus, omega + tau + rho_plus),
]

# R(L)=g I-g0*r*(r I-L)^(-1). If h contains A exp(-lambda t),
# then convolution with r exp(-r t) contributes
# r A (exp(-lambda t)-exp(-r t))/(r-lambda).
kappa_terms = []
coef_r = sp.Integer(0)
for amplitude, lam in h_terms:
    coef_lam = sp.factor(amplitude * (g - g0 * r / (r - lam)))
    kappa_terms.append((coef_lam, lam))
    coef_r += sp.factor(amplitude * g0 * r / (r - lam))
coef_r = sp.factor(coef_r)

# Sign pattern, in increasing decay-rate order except for the separate r term.
assert kappa_terms[0][0] < 0
assert kappa_terms[1][0] > 0
assert kappa_terms[2][0] < 0
assert kappa_terms[3][0] > 0
assert coef_r < 0

# Integral of kappa equals R(0) H(0)=(-epsilon) z_sigma.
def Z(alpha):
    return sp.factor(
        (alpha + 1 + B + a) / ((alpha + a) * (alpha + 1 + B) - a)
    )

z_sigma = sp.factor(Z(omega) - 2 * Z(omega + tau))
assert z_sigma == sp.Rational(114559900, 205809)
int_kappa = sp.factor(
    sum(coef / lam for coef, lam in kappa_terms) + coef_r / r
)
assert sp.factor(int_kappa + epsilon * z_sigma) == 0

# Coefficientwise triangle inequality after combining equal exponentials.
theta_triangle = sp.factor(
    -kappa_terms[0][0] / kappa_terms[0][1]
    + kappa_terms[1][0] / kappa_terms[1][1]
    - kappa_terms[2][0] / kappa_terms[2][1]
    + kappa_terms[3][0] / kappa_terms[3][1]
    - coef_r / r
)
assert theta_triangle > 0
assert theta_triangle < 1

# Sharpen by pairing the first negative exponential -n exp(-lambda t)
# with the tau-shifted positive exponential p exp(-(lambda+tau)t).
# On [3,50], p exp(-(lambda+tau)t) >= n exp(-lambda t).
# Algebraic premises:
n = sp.factor(-kappa_terms[0][0])
p = sp.factor(kappa_terms[1][0])
lam = sp.factor(kappa_terms[0][1])
assert n > 0
assert p > 0
assert sp.factor(kappa_terms[1][1] - lam) == tau
assert p / n > 7

# For t <= 50, exp(tau*t) <= exp(8/5). The elementary inequality
# exp(x) < (1-x/10)^(-10), x=8/5, gives exp(8/5)<(25/21)^10<6<7.
exp_upper_rational = sp.Rational(25, 21) ** 10
assert exp_upper_rational < 6
assert 6 < 7

# Hence the positive term dominates the negative one on [3,50]. Pairing
# them saves twice the integral of the negative term there. Use only
# exp(-x) >= 1-x to lower-bound that integral:
# int_3^50 n exp(-lam t) dt >= 47*n*(1-50*lam).
assert 1 - 50 * lam > 0
cancellation_lower = sp.factor(2 * 47 * n * (1 - 50 * lam))
theta_sharp = sp.factor(theta_triangle - cancellation_lower)
assert theta_sharp > 0
assert B * theta_sharp < 1

print("disc =", disc)
for j, (coef, lam_j) in enumerate(kappa_terms, 1):
    print(f"lambda_{j} =", sp.N(lam_j, 20))
    print(f"coef_{j} =", sp.N(coef, 20))
print("lambda_r =", r)
print("coef_r =", sp.N(coef_r, 20))
print("integral kappa =", sp.N(int_kappa, 20))
print("theta_triangle =", sp.N(theta_triangle, 30))
print("cancellation_lower =", sp.N(cancellation_lower, 30))
print("theta_sharp =", sp.N(theta_sharp, 30))
print("B * theta_sharp =", sp.N(B * theta_sharp, 30))
print("exact B * theta_sharp < 1 verified")
