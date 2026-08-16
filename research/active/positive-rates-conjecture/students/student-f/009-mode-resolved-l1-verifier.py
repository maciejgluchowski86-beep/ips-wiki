#!/usr/bin/env python3
"""Exact symbolic checks for Student F Assignment 009.

Checks:
1. the equilibrium/transient right-weighted mass costs;
2. the exact positive gap proving kappa_T < 1;
3. the near-East expansion kappa_T = 1 - 13 eps^2/3 + 38 eps^3/9 + ...;
4. the strict rational-point values kappa_E=48/533 and kappa_T=185/301;
5. the local degree-raising identity and the B^j top-degree coefficient in
   L_N^j eta_1 for the first several depths, certifying the general hand proof.

No Monte Carlo is used.
"""

from collections import defaultdict
import sympy as sp


a, b, c, alpha = sp.symbols("a b c alpha", positive=True)
k = sp.symbols("k", positive=True)
B = b + c - a
omega = 1 - c + a

# Right-killing survival resolvent.
Zalpha = sp.factor(
    (alpha + 1 + B + a) / ((alpha + a) * (alpha + 1 + B) - a)
)
Z = sp.factor(Zalpha.subs(alpha, omega))

# One-site zero-boundary equilibrium mass coefficient.
r0 = sp.factor(1 / (1 + b))
m0 = sp.factor(B * r0 - c)
assert sp.factor(m0 - (b * (1-c) - a)/(1+b)) == 0

# Transient mode rate lambda0=1+b.
lambda0 = 1 + b
ZT = sp.factor(Zalpha.subs(alpha, omega + lambda0))

# Rewrite with k=1-c.
subs_k = {c: 1-k}
B_k = sp.factor(B.subs(subs_k))
ZT_k = sp.factor(ZT.subs(subs_k))
denT = 4*a*b + 5*a + 2*b**2 + 2*b*k + 5*b + 3*k + 3
numZT = a + 2*b + 3
assert sp.factor(ZT_k - numZT/denT) == 0

kappaT = sp.factor(B_k * ZT_k)
gapT = sp.factor(denT - B_k * numZT)
expected_gap = a**2 + 5*a*b + a*k + 7*a + 4*b*k + 6*k
assert sp.factor(gapT - expected_gap) == 0

# Near-East expansion.
eps = sp.symbols("eps", positive=True)
near = {a: eps**2, b: eps, k: eps**2}
kappaT_ne = sp.factor(kappaT.subs(near))
assert sp.limit(kappaT_ne, eps, 0, dir="+") == 1
assert sp.limit((1-kappaT_ne)/eps**2, eps, 0, dir="+") == sp.Rational(13, 3)
series_ne = sp.series(kappaT_ne, eps, 0, 4)
assert series_ne.removeO().expand().coeff(eps, 2) == -sp.Rational(13, 3)
assert series_ne.removeO().expand().coeff(eps, 3) == sp.Rational(38, 9)

# Strict rational residual point.
aa = sp.Rational(1, 10)
bb = sp.Rational(3, 10)
cc = sp.Rational(4, 5)
kk = 1 - cc
BB = sp.factor(B.subs({a: aa, b: bb, c: cc}))
omega_ex = sp.factor(omega.subs({a: aa, b: bb, c: cc}))
Z_ex = sp.factor(Zalpha.subs({a: aa, b: bb, c: cc, alpha: omega_ex}))
m0_ex = sp.factor(m0.subs({a: aa, b: bb, c: cc}))
kapE_ex = sp.factor(-m0_ex * Z_ex)  # m0<0 here
kapT_ex = sp.factor(kappaT.subs({a: aa, b: bb, k: kk}))
assert BB == 1
assert kapE_ex == sp.Rational(48, 533)
assert kapT_ex == sp.Rational(185, 301)

# ---------------------------------------------------------------------------
# Degree-raising identity.
# On {0,1}^2 the signed flip factor for an observable containing x is
# c(x,y)(1-2x) = 1 - c y - (1+b)x + Bxy.
# Check all four binary values against the rate table.
# ---------------------------------------------------------------------------
x, y = sp.symbols("x y")
local_poly = 1 - c*y - (1+b)*x + B*x*y
rate_table = {
    (0, 0): 1,
    (0, 1): 1-c,
    (1, 0): b,
    (1, 1): a,
}
for xv in (0, 1):
    for yv in (0, 1):
        lhs = sp.factor(local_poly.subs({x: xv, y: yv}))
        rhs = sp.factor(rate_table[(xv, yv)] * (1 - 2*xv))
        assert sp.factor(lhs-rhs) == 0

# Polynomial functions are represented as dict support -> coefficient,
# with support a frozenset of site labels.  This implements L_N exactly on
# monomials using the local identity above and zero boundary at N+1.
def add_term(out, support, coeff):
    coeff = sp.expand(coeff)
    if coeff != 0:
        out[frozenset(support)] += coeff


def generator_on_poly(poly, N):
    out = defaultdict(lambda: sp.Integer(0))
    for S, coeff in poly.items():
        S = set(S)
        for i in list(S):
            base = S - {i}
            # +1 term
            add_term(out, base, coeff)
            # -c eta_{i+1}; zero if i=N because boundary is fixed zero.
            if i < N:
                add_term(out, base | {i+1}, -c * coeff)
            # -(1+b) eta_i
            add_term(out, base | {i}, -(1+b) * coeff)
            # +B eta_i eta_{i+1}; zero at the fixed boundary.
            if i < N:
                add_term(out, base | {i, i+1}, B * coeff)
    return {S: sp.factor(v) for S, v in out.items() if sp.factor(v) != 0}


# Check the top-degree theorem symbolically for N up to 7.  The report gives
# the all-N induction: degree can rise by at most one, and the unique chain
# attaining degree j+1 is {1}->{1,2}->...->{1,...,j+1}.
N = 7
poly = {frozenset({1}): sp.Integer(1)}
for j in range(N):
    target = frozenset(range(1, j+2))
    assert sp.factor(poly.get(target, 0) - B**j) == 0
    max_degree = max(len(S) for S in poly)
    assert max_degree == j+1
    if j < N-1:
        poly = generator_on_poly(poly, N)

print("Z_alpha =", Zalpha)
print("transient Z_T =", ZT_k)
print("kappa_T denominator gap =", gapT)
print("near-East kappa_T series =", series_ne)
print("rational kappa_E =", kapE_ex)
print("rational kappa_T =", kapT_ex)
print("degree-raising orbit checked symbolically through depth", N)
