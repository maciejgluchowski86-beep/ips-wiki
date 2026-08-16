"""Exact audit checks for Student F Assignment 007.

No Monte Carlo. This file checks the Phase-A claims up to the first failure:
segmentwise survival/resolvent, the near-East depth-two obstruction, and the
claim that max(c,g) Z < 1 has a nonempty residual subregion.
"""

import math
import sympy as sp

# General symbols.
a, b, c, alpha = sp.symbols("a b c alpha", positive=True)
B = b + c - a
g = b - a
omega = 1 - c + a

# Segmentwise killed chain. State order is (1,0); state 0 is killed at rate B.
K = sp.Matrix([[-a, a], [1, -(1 + B)]])
one = sp.Matrix([1, 1])
start1 = sp.Matrix([[1, 0]])
Zalpha = sp.factor((start1 * (alpha * sp.eye(2) - K).inv() * one)[0])
assert sp.factor(
    Zalpha
    - (alpha + 1 + B + a) / ((alpha + a) * (alpha + 1 + B) - a)
) == 0

Z = sp.factor(Zalpha.subs(alpha, omega))
assert sp.factor(
    Z - (omega + 1 + B + a) / ((omega + a) * (omega + 1 + B) - a)
) == 0
assert sp.factor(
    Z - (a + b + 2) / (2*a*b + 3*a - b*c + b - 2*c + 2)
) == 0

# Near-East exact finite-volume invariant moments.
e = sp.symbols("e", positive=True)
aa, bb, cc = e**2, e, 1 - e**2
pstar = (1 + e) / (1 + 2*e)
qstar = e / (1 + 2*e)

states = ((0, 0), (0, 1), (1, 0), (1, 1))


def flip_rate(x, y):
    """Centered-trail spin convention: c00=1,c01=1-c,c10=b,c11=a."""
    if (x, y) == (0, 0):
        return sp.Integer(1)
    if (x, y) == (0, 1):
        return e**2
    if (x, y) == (1, 0):
        return e
    return e**2


Q = sp.zeros(4)
for ii, state in enumerate(states):
    for site in (0, 1):
        x0 = state[site]
        y0 = state[site + 1] if site == 0 else 0  # zero right boundary
        rate = flip_rate(x0, y0)
        nxt = list(state)
        nxt[site] = 1 - x0
        jj = states.index(tuple(nxt))
        Q[ii, jj] += rate
        Q[ii, ii] -= rate

p0, p1, p2, p3 = sp.symbols("p0:4")
row = sp.Matrix([[p0, p1, p2, p3]])
stationary = sp.solve(
    list(row * Q) + [p0 + p1 + p2 + p3 - 1],
    [p0, p1, p2, p3],
    dict=True,
)[0]


def h(v):
    return sp.factor((v - pstar) / qstar)


M2 = sp.factor(sum(
    stationary[p] * h(st[0]) * h(st[1])
    for p, st in zip((p0, p1, p2, p3), states)
))
M2_expected = (1 + e) * (2*e - 1) / (2*e**2 + 5*e + 1)
assert sp.factor(M2 - M2_expected) == 0

m = sp.factor((1/(1 + e) - pstar) / qstar)
assert sp.factor(m + e/(1 + e)) == 0

# For 0<e<1/2, M2<0 while m^2>0, so A_2 changes sign.
assert M2.subs(e, sp.Rational(1, 4)) < 0

# Exact near-East resolvent.
Z_ne = sp.factor(Z.subs({a: aa, b: bb, c: cc}))
assert sp.factor(
    Z_ne - (e**2 + e + 2) / (e**2 * (3*e + 5))
) == 0
assert sp.limit(m**2 * Z_ne, e, 0, dir="+") == sp.Rational(2, 5)

# Numerical checks of the absolute-value ratios using exact exponential formulas.
def near_east_ratios(eps):
    mv = -eps/(1 + eps)
    Mv = (1 + eps)*(2*eps - 1)/(2*eps**2 + 5*eps + 1)
    C = mv*mv - Mv
    lam = 1 + eps
    om = 2*eps*eps
    gv = eps*(1-eps)
    ustar = math.log(C/(mv*mv))/lam

    # Plain Laplace kernel.
    signed = mv*mv/om - C/(om + lam)
    neg = (
        C*(1-math.exp(-(om+lam)*ustar))/(om+lam)
        - mv*mv*(1-math.exp(-om*ustar))/om
    )
    plain_abs = signed + 2*neg

    # Right survival is a two-exponential mixture.
    Bv = 1 + eps - 2*eps*eps
    av = eps*eps
    disc = math.sqrt((av+1+Bv)**2 - 4*av*Bv)
    rp = (av+1+Bv+disc)/2
    rm = (av+1+Bv-disc)/2

    def zfull(al):
        return (al+1+Bv+av)/((al+av)*(al+1+Bv)-av)

    def ztrunc(al, u):
        return (
            rp*(1-math.exp(-(al+rm)*u))/(al+rm)
            - rm*(1-math.exp(-(al+rp)*u))/(al+rp)
        )/(rp-rm)

    signed_w = mv*mv*zfull(om) - C*zfull(om+lam)
    neg_w = C*ztrunc(om+lam, ustar) - mv*mv*ztrunc(om, ustar)
    right_abs = signed_w + 2*neg_w

    scale = gv/abs(mv)
    return scale*plain_abs, scale*right_abs


p_ratio, r_ratio = near_east_ratios(0.002)
assert abs(p_ratio - 1.5) < 0.03
assert abs(r_ratio - 1.4) < 0.03

# Phase-A item 5: the claimed "easy residual subregion" is empty.
# Since c >= a+b and a>0, g=b-a < b < c, so max(c,g)=c.
# c Z < 1 would require F := denominator - c*numerator > 0.
F = sp.factor(
    (2*a*b + 3*a - b*c + b - 2*c + 2) - c*(a+b+2)
)
x = sp.symbols("x", positive=True)
Fx = sp.expand(F.subs(c, 1-x))
assert sp.factor(Fx - (a*(2*b+x+2) + x*(2*b+4) - b - 2)) == 0

# The hand proof splits at 2b+x=1 and
# b0 = 1/(2+1/sqrt(2)). These are the endpoint values used there.
b0 = sp.simplify(1/(2 + 1/sp.sqrt(2)))

G1 = 2*b**2 + b + 3*b*x + 4*x - 2
Q1 = sp.factor(G1.subs(x, b/sp.sqrt(2)))
assert sp.simplify(
    Q1.subs(b, b0) - 2*(-43 + 30*sp.sqrt(2))/49
) == 0
assert float(Q1.subs(b, b0)) < 0

G1_boundary = sp.factor(G1.subs(x, 1-2*b))
assert sp.simplify(G1_boundary + 2*(2*b**2 + 2*b - 1)) == 0
assert sp.simplify(
    (2*b**2+2*b-1).subs(b, b0) - (43-30*sp.sqrt(2))/49
) == 0
assert float((2*b**2+2*b-1).subs(b, b0)) > 0

G2 = -2*b**2 - b*x - b - x**2 + 3*x
G2_sqrt = sp.factor(G2.subs(x, b/sp.sqrt(2)))
assert sp.simplify(
    G2_sqrt + b*(sp.sqrt(2)*b + 5*b - 3*sp.sqrt(2) + 2)/2
) == 0
bracket = (sp.sqrt(2)+5)*b - 3*sp.sqrt(2) + 2
assert sp.simplify(
    bracket.subs(b, b0) - (32-22*sp.sqrt(2))/7
) == 0
assert float(bracket.subs(b, b0)) > 0

G2_half = sp.factor(G2.subs(x, sp.Rational(1, 2)))
assert sp.simplify(G2_half + (2*b-1)*(4*b+5)/4) == 0

print("Z =", Z)
print("near-East m =", m)
print("near-East M2 =", M2)
print("near-East Z =", Z_ne)
print("epsilon=.002 absolute ratios:", p_ratio, r_ratio)
print("Phase-A item 5: endpoint certificate proves c*Z > 1 throughout residual chamber.")
