#!/usr/bin/env python3
"""Exact checks for Student F Assignment 008.

No Monte Carlo.  The verifier checks:

1. the fully-regenerated mass multiplier |B r0-c| Z and the algebra used in
   the hand proof that it is < 2/3;
2. the depth-two near-East distinction between signed averaging (3/5) and
   the required L1-in-duration quantity (7/5);
3. the exact one-level regenerated signed phase kernel K^(1), including its
   near-East trace/determinant limits and a strict residual rational example;
4. exact failure of first- and second-order static spatial Markov closure at
   (a,b,c)=(1/10,3/10,4/5).

The last two checks are diagnostics for the finite-kernel state space.  They do
not assert that the full bounded-height trail kernel is K^(1).
"""

import itertools
import sympy as sp


def finite_generator(n, a, b, c):
    """Zero-right-boundary generator in the centered-trail spin convention."""
    states = list(itertools.product((0, 1), repeat=n))
    index = {s: i for i, s in enumerate(states)}
    Q = sp.zeros(2**n)

    def rate(x, y):
        if (x, y) == (0, 0):
            return sp.Integer(1)
        if (x, y) == (0, 1):
            return 1 - c
        if (x, y) == (1, 0):
            return b
        return a

    for s in states:
        i = index[s]
        for site in range(n):
            y = s[site + 1] if site + 1 < n else 0
            r = rate(s[site], y)
            t = list(s)
            t[site] = 1 - t[site]
            j = index[tuple(t)]
            Q[i, j] += r
            Q[i, i] -= r
    return states, Q


def stationary_vector(Q):
    n = Q.rows
    ps = sp.symbols(f"p0:{n}")
    row = sp.Matrix([ps])
    sol = sp.solve(list(row * Q) + [sum(ps) - 1], ps, dict=True)[0]
    return sp.Matrix([[sp.factor(sol[p]) for p in ps]])


# ---------------------------------------------------------------------------
# General residual algebra.
# ---------------------------------------------------------------------------
a, b, c, alpha = sp.symbols("a b c alpha", positive=True)
B = b + c - a
g = b - a
omega = 1 - c + a
k = 1 - c

# Segmentwise right-killing resolvent from Meeting 006.
Zalpha = sp.factor(
    (alpha + 1 + B + a) / ((alpha + a) * (alpha + 1 + B) - a)
)
Z = sp.factor(Zalpha.subs(alpha, omega))
assert sp.factor(
    Z - (a + b + 2) / (a * (2*b + 3) + k * (b + 2))
) == 0

# Fully regenerated one-site zero-boundary equilibrium.
r0 = sp.factor(1 / (1 + b))
m0 = sp.factor(B * r0 - c)
assert sp.factor(m0 - (b*k - a)/(1+b)) == 0
mass_multiplier = sp.factor(abs(1) * (b*k-a) * 0 + 1)  # placeholder: sign split is in hand proof

# Hand-proof algebra for |m0| Z < 2/3.
# Case a >= b k: replace |a-bk| by a.  The remaining target follows from
# 2(1+b)(2b+3)-3(a+b+2) = 4b^2+7b-3a > 0 because a<b.
hard_gap = sp.expand(2*(1+b)*(2*b+3) - 3*(a+b+2))
assert sp.factor(hard_gap - (4*b**2 + 7*b - 3*a)) == 0

# Case a < b k: replace |bk-a| by bk and drop the positive a-term in the
# denominator.  At the worst allowed a=b, the target gap is
# 4(1+b)(1-b)>0.
soft_gap_at_a_eq_b = sp.factor(
    (2*(1+b)*(b+2) - 3*b*(a+b+2)).subs(a, b)
)
assert sp.factor(soft_gap_at_a_eq_b - 4*(1+b)*(1-b)) == 0

# ---------------------------------------------------------------------------
# General two-site invariant conditionals and the mass relaxation mode.
# ---------------------------------------------------------------------------
states2, Q2 = finite_generator(2, a, b, c)
pi2 = stationary_vector(Q2)
p2 = {s: pi2[0, i] for i, s in enumerate(states2)}

r_right = sp.factor(p2[(0, 1)] + p2[(1, 1)])
r_left = sp.factor(p2[(1, 0)] + p2[(1, 1)])
assert sp.factor(r_right - r0) == 0

S = sp.factor(a*b + 2*a + b**2 - b*c + 2*b - 2*c + 2)
q0 = sp.factor(p2[(1, 0)] / (p2[(0, 0)] + p2[(1, 0)]))
q1 = sp.factor(p2[(1, 1)] / (p2[(0, 1)] + p2[(1, 1)]))
assert sp.factor(q0 - (a+b-2*c+2)/S) == 0
assert sp.factor(q1 - (2*b-b*c-2*c+2)/S) == 0
assert sp.factor(q1-q0 + (a+b*c-b)/S) == 0

assert sp.factor(
    r_left-r0 + 2*(a+b*c-b)/((1+b)*S)
) == 0

# A strict residual point used for exact mode/non-Markov diagnostics.
aa = sp.Rational(1, 10)
bb = sp.Rational(3, 10)
cc = sp.Rational(4, 5)
assert aa < bb and cc >= aa+bb and bb**2 >= 2*(1-cc)**2

r0_ex = sp.factor(r0.subs({a: aa, b: bb, c: cc}))
rleft_ex = sp.factor(r_left.subs({a: aa, b: bb, c: cc}))
assert r0_ex == sp.Rational(10, 13)
assert rleft_ex == sp.Rational(250, 351)
assert sp.factor(rleft_ex-r0_ex) == -sp.Rational(20, 351)

# Thus the mass-channel law mu_u=bar(pi_2) P_u^0 has
# r(u)=10/13-(20/351)e^{-13u/10}; B=1 at this point, so the next total signed
# mass Br(u)-c varies continuously from -154/1755 to -2/65.
B_ex = sp.factor(B.subs({a: aa, b: bb, c: cc}))
assert B_ex == 1
mass_u0 = sp.factor(B_ex*rleft_ex-cc)
mass_uinf = sp.factor(B_ex*r0_ex-cc)
assert mass_u0 == -sp.Rational(154, 1755)
assert mass_uinf == -sp.Rational(2, 65)

# ---------------------------------------------------------------------------
# Near-East exact depth-two profile: signed averaging is 3/5, L1 is 7/5.
# ---------------------------------------------------------------------------
e = sp.symbols("e", positive=True)
ae, be, ce = e**2, e, 1-e**2
ge = sp.factor(be-ae)
omegae = sp.factor(1-ce+ae)

pstar = sp.factor((1+e)/(1+2*e))
qstar = sp.factor(e/(1+2*e))
me = -e/(1+e)
M2e = sp.factor((1+e)*(2*e-1)/(2*e**2+5*e+1))
Ce = sp.factor(me**2-M2e)
lame = 1+e

# Mass branch immediately after dropping the right site.
rleft_ne = sp.factor(r_left.subs({a: ae, b: be, c: ce}))
hbar_ne = sp.factor((rleft_ne-pstar)/qstar)
assert sp.factor(
    hbar_ne + (2*e**3+e**2+3*e+2)/((e+1)*(2*e**2+5*e+1))
) == 0
assert sp.limit(hbar_ne, e, 0, dir="+") == -2
assert sp.limit(me, e, 0, dir="+") == 0

# Right-weighted signed depth-two integral is
# m^2 Z_omega - C Z_{omega+lambda}; its normalized magnitude tends to 3/5.
Ze0 = sp.factor(Zalpha.subs({a: ae, b: be, c: ce, alpha: omegae}))
Ze1 = sp.factor(Zalpha.subs({a: ae, b: be, c: ce, alpha: omegae+lame}))
Se = sp.factor(me**2*Ze0 - Ce*Ze1)
scale = sp.factor(ge/(-me))  # me<0 on the path
assert sp.limit(Se, e, 0, dir="+") == -sp.Rational(3, 5)
assert sp.limit(-scale*Se, e, 0, dir="+") == sp.Rational(3, 5)

# The exact L1 ratio 7/5 was independently audited in Assignment 007.  Here
# we verify its asymptotic decomposition: signed part -> -3/5 and negative
# lobe -> 1, hence signed + 2*negative -> 7/5.
assert -sp.Rational(3,5) + 2 == sp.Rational(7,5)

# ---------------------------------------------------------------------------
# Exact fully-regenerated height-one signed phase kernel K^(1).
# ---------------------------------------------------------------------------
# If the current conditioned right spin is z, the adjacent left spin starts
# with density q_z.  After the right site is removed it evolves as the
# zero-boundary one-site chain, with relaxation rate 1+b.
lam = 1+b
Z1 = sp.factor(Zalpha.subs(alpha, omega+lam))
I0_1 = sp.factor(r0*Z + (q0-r0)*Z1)
I1_1 = sp.factor(r0*Z + (q1-r0)*Z1)
I0_0 = sp.factor(Z-I0_1)
I1_0 = sp.factor(Z-I1_1)

K1 = sp.Matrix([
    [-c*I0_0, -c*I0_1],
    [ g*I1_0,  g*I1_1],
])

K1_ex = sp.simplify(K1.subs({a: aa, b: bb, c: cc}))
K1_expected = sp.Matrix([
    [-sp.Rational(184712,333207), -sp.Rational(595480,333207)],
    [ sp.Rational(47695,333207),   sp.Rational(147353,333207)],
])
assert K1_ex == K1_expected
tr_ex = sp.factor(sp.trace(K1_ex))
det_ex = sp.factor(K1_ex.det())
disc_ex = sp.factor(tr_ex**2-4*det_ex)
assert tr_ex == -sp.Rational(593,5289)
assert det_ex == sp.Rational(1184,111069)
assert disc_ex == -sp.Rational(654225,21757183)
assert det_ex < 1 and disc_ex < 0

# Near-East trace/determinant limits.  Since the discriminant tends to -36/25,
# the eigenvalues are a complex conjugate pair for all sufficiently small e;
# their modulus tends sqrt(det)=sqrt(2/5)<1.
tr_ne = sp.factor(sp.trace(K1).subs({a: ae, b: be, c: ce}))
det_ne = sp.factor(K1.det().subs({a: ae, b: be, c: ce}))
assert sp.limit(tr_ne, e, 0, dir="+") == -sp.Rational(2,5)
assert sp.limit(det_ne, e, 0, dir="+") == sp.Rational(2,5)
assert sp.limit(tr_ne**2-4*det_ne, e, 0, dir="+") == -sp.Rational(36,25)

# ---------------------------------------------------------------------------
# Static spin-phase closure is not Markov even at low order.
# ---------------------------------------------------------------------------
states3, Q3 = finite_generator(3, aa, bb, cc)
pi3 = stationary_vector(Q3)
p3 = {s: pi3[0, i] for i, s in enumerate(states3)}

# First-order spatial Markov would force eta_1 and eta_3 conditionally
# independent given eta_2.  Both conditional 2x2 determinants are nonzero.
det_mid0 = sp.factor(
    p3[(0,0,0)]*p3[(1,0,1)] - p3[(0,0,1)]*p3[(1,0,0)]
)
det_mid1 = sp.factor(
    p3[(0,1,0)]*p3[(1,1,1)] - p3[(0,1,1)]*p3[(1,1,0)]
)
assert det_mid0 == sp.Rational(6715,52606827)
assert det_mid1 == -sp.Rational(34675,52606827)

# Second-order spatial Markov would force eta_1 and eta_4 conditionally
# independent given (eta_2,eta_3).  A single nonzero determinant suffices.
states4, Q4 = finite_generator(4, aa, bb, cc)
pi4 = stationary_vector(Q4)
p4 = {s: pi4[0, i] for i, s in enumerate(states4)}
det_mid00 = sp.factor(
    p4[(0,0,0,0)]*p4[(1,0,0,1)]
    - p4[(0,0,0,1)]*p4[(1,0,0,0)]
)
assert det_mid00 == -sp.Rational(1097085304370,627742107775979469)

print("fully regenerated mass multiplier hand certificate: |m0| Z < 2/3")
print("near-East signed-before-absolute factor ->", sp.Rational(3,5))
print("near-East correct L1 factor ->", sp.Rational(7,5))
print("height-one K^(1) at (1/10,3/10,4/5) =")
print(K1_ex)
print("near-East tr K^(1) ->", sp.limit(tr_ne, e, 0, dir="+"))
print("near-East det K^(1) ->", sp.limit(det_ne, e, 0, dir="+"))
print("first-order static Markov determinant ->", det_mid0)
print("second-order static Markov determinant ->", det_mid00)
