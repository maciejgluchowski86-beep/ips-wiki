#!/usr/bin/env python3
"""Exact verifier for Graduate Student C assignment 002.

Requires sympy. No floating-point calculations are used in the certificates.

The verified chamber is the actual unresolved chamber after combining the
published 2025 criteria with the 2026 long-lived-state theorem on r11=0:
    0 < a=r00 < b=r01 < c=r10 < 1,
with additionally c>=1/2, c>=a+b, b>=sqrt(2)(1-c).
For the canonical coupling only c>b>a>0=r11 matters.

This script verifies two pieces needed for the East-boundary supremum:
1. The b->0 singular corner compactification a=alpha*b,
   c=1-gamma*b, including the exact seven-class effective generator and
   the bound max L_w(alpha,gamma) <= 5/6.
2. The fixed boundary b in (0,1], a=0, c=1.  It solves the full 24-state
   killed chain and certifies every unconditional factor <=5/6 by exact
   polynomial positivity after the Mobius substitution b=x/(1+x).
"""

from itertools import product
import sympy as sp

PAIRS = ((0, 0), (1, 1), (0, 1), (1, 0))
DIAG = {(0, 0), (1, 1)}
OFF = {(0, 1), (1, 0)}
EXT = (0, 1)
STATES = [
    s for s in product(PAIRS, repeat=3)
    if s[0] in DIAG and any(pair in OFF for pair in s)
]
INDEX = {s: i for i, s in enumerate(STATES)}
assert len(STATES) == 24


def build_symbolic_transition(r, rank):
    """Full 26-state embedded transition matrix (24 transient + C,R)."""
    C, R = 24, 25
    n = 26
    P = sp.zeros(n, n)

    def coupled(env0, env1):
        p, q = r[env0], r[env1]
        if rank[env0] >= rank[env1]:
            return {
                (0, 0): 1 - p,
                (1, 1): q,
                (1, 0): p - q,
                (0, 1): sp.Integer(0),
            }
        return {
            (0, 0): 1 - q,
            (1, 1): p,
            (0, 1): q - p,
            (1, 0): sp.Integer(0),
        }

    for i, state in enumerate(STATES):
        for site in range(3):
            here = state[site]
            right = EXT if site == 2 else state[site + 1]
            env0 = (here[0], right[0])
            env1 = (here[1], right[1])
            for new_pair, probability in coupled(env0, env1).items():
                if probability == 0:
                    continue
                probability = sp.expand(probability / 3)
                new_state = list(state)
                new_state[site] = new_pair
                new_state = tuple(new_state)
                if site == 0 and new_pair in OFF:
                    P[i, C] += probability
                elif all(pair in DIAG for pair in new_state):
                    P[i, R] += probability
                else:
                    P[i, INDEX[new_state]] += probability
    P[C, C] = 1
    P[R, R] = 1
    return P


def corner_certificate():
    t, alpha, gamma = sp.symbols("t alpha gamma", nonnegative=True)
    rank = {(1, 0): 3, (0, 1): 2, (0, 0): 1, (1, 1): 0}
    r = {
        (0, 0): alpha * t,
        (0, 1): t,
        (1, 0): 1 - gamma * t,
        (1, 1): sp.Integer(0),
    }
    P = build_symbolic_transition(r, rank)
    P0 = P.subs(t, 0)
    P1 = P.diff(t).subs(t, 0)

    recurrent_states = [
        "R",
        ((0, 0), (0, 0), (1, 0)),
        ((0, 0), (1, 0), (0, 0)),
        ((0, 0), (0, 1), (1, 0)),
        ((0, 0), (0, 1), (0, 0)),
        ((1, 1), (0, 0), (1, 0)),
        "C",
    ]
    rec = [25 if s == "R" else 24 if s == "C" else INDEX[s]
           for s in recurrent_states]
    trans = [i for i in range(26) if i not in rec]

    Q0 = P0.extract(trans, trans)
    S0 = P0.extract(trans, rec)
    Btrans = (sp.eye(len(trans)) - Q0).inv() * S0
    B = sp.zeros(26, len(rec))
    for m, ri in enumerate(rec):
        B[ri, m] = 1
    for ii, i in enumerate(trans):
        for m in range(len(rec)):
            B[i, m] = sp.simplify(Btrans[ii, m])
    assert all(sp.simplify(sum(B[i, m] for m in range(len(rec))) - 1) == 0
               for i in range(26))

    Qeff = sp.zeros(len(rec), len(rec))
    for m, ri in enumerate(rec):
        for n in range(len(rec)):
            Qeff[m, n] = sp.simplify(sum(P1[ri, k] * B[k, n]
                                           for k in range(26)))
    assert all(sp.simplify(sum(Qeff[m, n] for n in range(len(rec)))) == 0
               for m in range(len(rec)))

    expected_Q = sp.Matrix([
        [0, 0, 0, 0, 0, 0, 0],
        [(gamma+1)/3, -(2*alpha+gamma+1)/3, 0, alpha/3, 0, alpha/3, 0],
        [alpha/2+gamma/3, alpha/6, -(2*alpha+gamma+1)/3, 0, 0, 0, sp.Rational(1,3)],
        [sp.Rational(1,6), gamma/3, 0, -2*gamma/3-sp.Rational(1,2), gamma/3, 0, sp.Rational(1,3)],
        [alpha/3+gamma/3+sp.Rational(1,6), 0, 0, alpha/6, -alpha/2-gamma/3-sp.Rational(1,2), 0, sp.Rational(1,3)],
        [(gamma+1)/3, gamma/3, 0, alpha/6, 0, -alpha/6-2*gamma/3-sp.Rational(1,2), sp.Rational(1,6)],
        [0, 0, 0, 0, 0, 0, 0],
    ])
    assert Qeff == expected_Q

    live = [1, 2, 3, 4, 5]
    Qtt = Qeff.extract(live, live)
    qC = sp.Matrix([Qeff[i, 6] for i in live])
    h = -Qtt.inv() * qC

    D = (
        8*alpha**3*gamma + 18*alpha**3
        + 54*alpha**2*gamma**2 + 139*alpha**2*gamma + 81*alpha**2
        + 80*alpha*gamma**3 + 252*alpha*gamma**2 + 264*alpha*gamma + 90*alpha
        + 32*gamma**4 + 128*gamma**3 + 186*gamma**2 + 117*gamma + 27
    )
    assert sp.expand(D - sp.denom(sp.cancel(h[2]))) == 0

    class_values = [sp.Integer(0)] + list(h) + [sp.Integer(1)]
    words = ((0,0,1), (0,1,1), (1,0,1), (1,1,1))
    L = {}
    for w in words:
        start = tuple((z,z) for z in w[:2]) + ((1,0),)
        i = INDEX[start]
        L[w] = sp.factor(sum(B[i,m]*class_values[m] for m in range(len(rec))))

    L111 = L[(1,1,1)]
    pos = (
        8*alpha**3 + 54*alpha**2*gamma + 43*alpha**2
        + 80*alpha*gamma**2 + 126*alpha*gamma + 45*alpha
        + 32*gamma**3 + 80*gamma**2 + 66*gamma + 18
    )
    assert sp.simplify(sp.Rational(5,6) - L111 - gamma*pos/(3*D)) == 0

    for w in words[:-1]:
        numerator = sp.Poly(sp.cancel(2*D*(L111-L[w])), alpha, gamma)
        assert all(coef > 0 for coef in numerator.coeffs())

    assert sp.simplify(L111.subs(gamma, 0) - sp.Rational(5,6)) == 0
    print("corner certificate: exact, sharp supremum 5/6")
    print("effective generator Q =")
    print(Qeff)


def mobius_positive(poly, b, x):
    """Certificate p(b)>0 on 0<=b<1 via b=x/(1+x), x>=0."""
    p = sp.Poly(sp.expand(poly), b)
    q = sp.cancel((1+x)**p.degree() * p.as_expr().subs(b, x/(1+x)))
    q = sp.Poly(q, x)
    return q.all_coeffs()


def fixed_boundary_certificate():
    b, x = sp.symbols("b x", nonnegative=True)
    rank = {(1, 0): 3, (0, 1): 2, (0, 0): 1, (1, 1): 1}
    r = {
        (0, 0): sp.Integer(0),
        (0, 1): b,
        (1, 0): sp.Integer(1),
        (1, 1): sp.Integer(0),
    }
    P = build_symbolic_transition(r, rank)
    K = P[:24, :24]
    cross = P[:24, 24]
    h = (sp.eye(24)-K).inv() * cross

    factors = {}
    for word in product((0,1), repeat=3):
        if word[2] == 1:
            attack, pair = sp.Integer(1), (1,0)
        else:
            attack, pair = b, (0,1)
        start = tuple((z,z) for z in word[:2]) + (pair,)
        factors[word] = sp.cancel(attack*h[INDEX[start]])

    common_den = sp.denom(factors[(1,1,1)])
    coeffs_den = mobius_positive(-common_den, b, x)
    assert all(coef > 0 for coef in coeffs_den)

    certificate_vectors = {}
    for word, value in factors.items():
        diff = sp.cancel(sp.Rational(5,6)-value)
        num, den = sp.fraction(diff)
        if sp.Poly(den,b).degree() == 8:
            signed_num = -num
        else:
            assert all(coef > 0 for coef in sp.Poly(den,b).all_coeffs())
            signed_num = num
        coeffs = mobius_positive(signed_num, b, x)
        assert all(coef >= 0 for coef in coeffs)
        assert any(coef > 0 for coef in coeffs)
        certificate_vectors[word] = coeffs

    assert sp.limit(factors[(1,1,1)], b, 0, dir="+") == sp.Rational(5,6)
    print("fixed-b boundary certificate: every factor <= 5/6 exactly")
    print("-common-denominator Mobius coefficients:", coeffs_den)
    for word in sorted(certificate_vectors):
        print(word, certificate_vectors[word])


def main():
    corner_certificate()
    fixed_boundary_certificate()
    print("all assignment-002 exact certificates passed")


if __name__ == "__main__":
    main()
