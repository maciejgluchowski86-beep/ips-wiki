"""Exact verifier for Student F assignment 004.

Requires sympy. No Monte Carlo is used.

Checks:
1. the uniform local coalescence lower bound q=1-c+a;
2. the two-generation ordered-clearing bound [q/(1+q)]^2;
3. the exact 24-state post-first-child CTMC on the near-East path
   a=e^2, b=e, c=1-e^2;
4. fixed right-boundary asymptotics and a stronger adaptive-control HJB
   certificate for the structured state (00,01,01).
"""

import sympy as sp

PAIR = ((0, 0), (1, 1), (0, 1), (1, 0))

# --- General residual local coalescence lower bound.
A, B, C = sp.symbols("A B C", positive=True)
Q = 1-C+A
coal_general = (Q, 1-B, 1-A, 1-C+B)
diff_general = tuple(sp.factor(x-Q) for x in coal_general)
assert diff_general == (0, C-A-B, C-2*A, B-A)
# On the residual chamber: C>=A+B and B>A, hence C>2A.
# Therefore all four differences are nonnegative.

p_clear_general = sp.factor(Q/(1+Q))
delta2_general = sp.factor(p_clear_general**2)

# --- Near-East path used for the exact finite-state asymptotic.
e = sp.symbols("e", positive=True)
a = e**2
b = e
c = 1 - e**2
q = 1-c+a
delta2 = sp.factor((q/(1+q))**2)
assert sp.series(delta2, e, 0, 6) == 4*e**4 + sp.O(e**6)


def rate(x, y):
    if (x, y) == (0, 0):
        return a
    if (x, y) == (0, 1):
        return b
    if (x, y) == (1, 0):
        return c
    return sp.Integer(0)


def update_pair(pair_i, pair_r):
    """Common-uniform update kernel on the near-East path.

    Ordering of the four rates is fixed for all sufficiently small e>0.
    We use e=1/100 only to select which symbolic difference is positive.
    """
    x, xt = pair_i
    y, yt = pair_r
    p = rate(x, y)
    pt = rate(xt, yt)
    pv = float(p.subs(e, sp.Rational(1, 100)))
    qv = float(pt.subs(e, sp.Rational(1, 100)))
    out = {
        (1, 1): p if pv <= qv else pt,
        (0, 0): 1 - (pt if pv <= qv else p),
    }
    if pv > qv:
        out[(1, 0)] = sp.factor(p-pt)
    elif qv > pv:
        out[(0, 1)] = sp.factor(pt-p)
    return {k: sp.factor(v) for k, v in out.items() if v != 0}


# State = (grandchild site pair, child pair, parent pair).
# Before grandchild creation the first pair is agreed. Success is absorption
# when child and parent are both agreed.
states = [
    (g, ch, p)
    for g in PAIR[:2]
    for ch in PAIR
    for p in PAIR
    if not (ch[0] == ch[1] and p[0] == p[1])
]
index = {s: i for i, s in enumerate(states)}
assert len(states) == 24
S0 = ((0, 0), (0, 1), (0, 1))


def solve_policy(parent_boundary_rule):
    """Solve the linear hitting equations for a fixed state-feedback rule."""
    n = len(states)
    A = sp.zeros(n)
    rhs = sp.zeros(n, 1)
    for s, i in index.items():
        for site in range(3):
            if site < 2:
                right = s[site+1]
            else:
                z = parent_boundary_rule(s)
                right = (z, z)
            for new_pair, rate_ in update_pair(s[site], right).items():
                if new_pair == s[site]:
                    continue
                ns = list(s)
                ns[site] = new_pair
                ns = tuple(ns)
                A[i, i] -= rate_
                if site == 0 and new_pair[0] != new_pair[1]:
                    # grandchild creation: failure value 1
                    rhs[i, 0] -= rate_
                elif ns[1][0] == ns[1][1] and ns[2][0] == ns[2][1]:
                    # both child and parent coupled: success value 0
                    pass
                else:
                    A[i, index[ns]] += rate_
    sol = list(sp.linsolve((A, rhs)))[0]
    return tuple(sp.factor(x) for x in sol)


fixed0 = solve_policy(lambda s: 0)
fixed1 = solve_policy(lambda s: 1)
V0 = fixed0[index[S0]]
V1 = fixed1[index[S0]]
assert sp.series(V0, e, 0, 3) == sp.Rational(3,5) - sp.Rational(24,25)*e + sp.Rational(1349,250)*e**2 + sp.O(e**3)
assert sp.series(V1, e, 0, 3) == sp.Rational(1,3) + sp.Rational(2,9)*e + sp.Rational(11,54)*e**2 + sp.O(e**3)


def near_east_policy(s):
    """Candidate maximizing HJB policy for all sufficiently small e>0.

    Choose right boundary 1 exactly when the child disagrees and the parent is
    either common 1 or has the same disagreement orientation as the child.
    """
    g, ch, p = s
    child_dis = ch[0] != ch[1]
    return int(child_dis and (p == (1, 1) or (p[0] != p[1] and p == ch)))


controlled = solve_policy(near_east_policy)
Vstar = controlled[index[S0]]
assert sp.series(Vstar, e, 0, 4) == (
    1 - sp.Rational(9,2)*e + sp.Rational(135,4)*e**2
    - sp.Rational(3233,12)*e**3 + sp.O(e**4)
)

S1 = ((1, 1), (0, 1), (0, 1))
Vstar1 = controlled[index[S1]]
assert sp.series(Vstar1, e, 0, 4) == (
    1 - e + sp.Rational(11,24)*e**2
    + sp.Rational(1205,72)*e**3 + sp.O(e**4)
)

# HJB verification: with V from the candidate policy, compare the parent-site
# generator action for z=1 versus z=0. Each advantage is rational and analytic
# at e=0. Its first nonzero Taylor coefficient has the sign prescribed by the
# policy. Since there are finitely many states, the policy is optimal for all
# sufficiently small positive e.
for s, i in index.items():
    actions = []
    for z in (0, 1):
        lv = 0
        for new_pair, rate_ in update_pair(s[2], (z, z)).items():
            if new_pair == s[2]:
                continue
            ns = (s[0], s[1], new_pair)
            if ns[1][0] == ns[1][1] and ns[2][0] == ns[2][1]:
                nv = 0
            else:
                nv = controlled[index[ns]]
            lv += rate_ * (nv - controlled[i])
        actions.append(sp.factor(lv))
    advantage = sp.factor(actions[1]-actions[0])
    num, den = sp.fraction(sp.cancel(advantage))
    assert den.subs(e, 0) != 0
    poly = sp.Poly(sp.series(advantage, e, 0, 5).removeO(), e)
    nonzero = [(mon[0], coeff) for mon, coeff in poly.terms() if coeff != 0]
    # Poly.terms() is descending; choose the smallest exponent.
    exponent, coeff = min(nonzero, key=lambda x: x[0])
    if near_east_policy(s) == 1:
        assert coeff > 0, (s, exponent, coeff)
    else:
        assert coeff < 0, (s, exponent, coeff)

print("two-generation general clearing gap =", delta2_general)
print("fixed z=0:", sp.series(V0, e, 0, 3))
print("fixed z=1:", sp.series(V1, e, 0, 3))
print("adaptive controlled upper envelope, g=0:", sp.series(Vstar, e, 0, 4))
print("adaptive controlled upper envelope, g=1:", sp.series(Vstar1, e, 0, 4))
