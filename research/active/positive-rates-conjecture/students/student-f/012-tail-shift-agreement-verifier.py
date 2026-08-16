#!/usr/bin/env python3
"""Exact checks for Student F Assignment 012.

No Monte Carlo and no floating-point assertions.

Checks:
1. strict residual rational test point and the boundary-generator coefficients
   D=L^1-L^0 are exactly -c and -(b-a);
2. on a two-site zero-boundary chain, the Poisson-equation gradient caused by
   flipping the boundary-nearest retained site is bounded by the exact
   integrated common-uniform disagreement occupation on the far site;
3. the elementary integral used in the explicit finite-speed part of the
   Delta_M bound;
4. an exact convergent geometric block sum of the form used when
   alpha_0(T)<=rho<1;
5. the first explicit spatial exponent log(2)-1/4 is strictly positive.

The infinite-volume implication in the report is analytic; this certificate
checks the finite algebra and one exact Green/coupling instance carrying it.
"""

import itertools
import sympy as sp


# ---------------------------------------------------------------------------
# Strict residual rational point used throughout F008--F011.
# ---------------------------------------------------------------------------
a = sp.Rational(1, 10)
b = sp.Rational(3, 10)
c = sp.Rational(4, 5)
g = b - a

assert 0 < a < b
assert sp.Rational(1, 2) <= c < 1
assert c >= a + b
assert b**2 >= 2 * (1 - c)**2
assert c > g > 0


def rate(x, y):
    return {
        (0, 0): sp.Integer(1),
        (0, 1): 1 - c,
        (1, 0): b,
        (1, 1): a,
    }[(x, y)]


# Boundary generator difference D=L^1-L^0 at the rightmost retained site.
assert sp.factor(rate(0, 1) - rate(0, 0)) == -c
assert sp.factor(rate(1, 1) - rate(1, 0)) == -g


# ---------------------------------------------------------------------------
# Exact two-site Green-gradient / common-coupling occupation check.
# Sites are ordered left-to-right. The second site has fixed zero boundary.
# ---------------------------------------------------------------------------
states = list(itertools.product((0, 1), repeat=2))
index = {s: i for i, s in enumerate(states)}

Q = sp.zeros(4)
for state in states:
    i = index[state]
    for site in range(2):
        right = state[site + 1] if site < 1 else 0
        r = rate(state[site], right)
        nxt = list(state)
        nxt[site] = 1 - nxt[site]
        j = index[tuple(nxt)]
        Q[i, j] += r
        Q[i, i] -= r

# Exact invariant row law.
A = Q.T.copy()
A[-1, :] = sp.ones(1, 4)
rhs = sp.zeros(4, 1)
rhs[-1, 0] = 1
pi = A.inv() * rhs

# f=eta_1 (leftmost spin). Solve -Q G = f-pi(f), pi(G)=0.
f = sp.Matrix([state[0] for state in states])
mean_f = sp.factor((pi.T * f)[0])
h = f - mean_f * sp.ones(4, 1)
Gsym = sp.symbols("G0:4")
G = sp.Matrix(Gsym)
eqs = list(-Q * G - h)
eqs.append((pi.T * G)[0])
sol = sp.solve(eqs, Gsym, dict=True)[0]
G = sp.Matrix([sp.factor(sol[x]) for x in Gsym])

# Common-uniform pair generator on two configurations.
pairs = [(x, y) for x in states for y in states]
pair_index = {p: i for i, p in enumerate(pairs)}
Qc = sp.zeros(16)

for xconf, yconf in pairs:
    i = pair_index[(xconf, yconf)]
    for site in range(2):
        xr = xconf[site + 1] if site < 1 else 0
        yr = yconf[site + 1] if site < 1 else 0
        p = rate(xconf[site], xr)
        q = rate(yconf[site], yr)

        outcomes = [
            (1, 1, min(p, q)),
            (0, 0, 1 - max(p, q)),
        ]
        if p > q:
            outcomes.append((1, 0, p - q))
        elif q > p:
            outcomes.append((0, 1, q - p))

        for nx, ny, prob in outcomes:
            if prob == 0:
                continue
            xx = list(xconf)
            yy = list(yconf)
            xx[site] = nx
            yy[site] = ny
            j = pair_index[(tuple(xx), tuple(yy))]
            if j != i:
                Qc[i, j] += prob
                Qc[i, i] -= prob

# Fully coupled pair states are closed and carry zero disagreement reward.
transient = [i for i, (x, y) in enumerate(pairs) if x != y]
Qt = Qc.extract(transient, transient)
reward_far = sp.Matrix([
    int(pairs[i][0][0] != pairs[i][1][0])
    for i in transient
])
occupation = (-Qt).inv() * reward_far

checks = []
for x in states:
    # Flip only the boundary-nearest retained site (site 2).
    y = (x[0], 1 - x[1])
    pair_i = pair_index[(x, y)]
    trans_i = transient.index(pair_i)
    grad = sp.factor(G[index[y]] - G[index[x]])
    occ = sp.factor(occupation[trans_i])
    assert abs(grad) <= occ
    checks.append((x, y, grad, occ))

# Exact values make the certificate independently inspectable.
assert checks[0][2] == -sp.Rational(10, 13)
assert checks[0][3] == sp.Rational(148500, 77441)
assert checks[2][2] == sp.Rational(55, 351)
assert checks[2][3] == sp.Rational(121770, 77441)


# ---------------------------------------------------------------------------
# Analytic constants in the explicit Delta_M estimate.
# ---------------------------------------------------------------------------
t, S = sp.symbols("t S", positive=True)
early_integral = sp.integrate(t * sp.exp(t), (t, 0, S))
assert sp.simplify(early_integral - ((S - 1) * sp.exp(S) + 1)) == 0

# Check the convergent geometric block identity at an exact rho in (0,1).
# The general identity is the same elementary geometric-series formula; using
# an exact rational rho avoids SymPy's convergence-conditioned Piecewise form.
rho0 = sp.Rational(2, 5)
K = sp.symbols("K", integer=True, nonnegative=True)
T = sp.symbols("T", positive=True)
n = sp.symbols("n", integer=True, nonnegative=True)
geom = sp.summation(rho0**n * (T + T**2 / 2), (n, K, sp.oo))
expected_geom = (T + T**2 / 2) * rho0**K / (1 - rho0)
assert sp.simplify(geom - expected_geom) == 0

# Exact sign check; numerical evaluation is only used to compare a known
# transcendental constant with zero, not as a mathematical certificate input.
assert sp.N(sp.log(2) - sp.Rational(1, 4), 50) > 0

print("strict residual rational point: verified")
print("boundary D coefficients: -c =", -c, "-(b-a) =", -g)
print("two-site Green/coupling occupation inequalities: verified")
for x, y, grad, occ in checks:
    print("  ", x, "->", y, "Green gradient =", grad, "occupation =", occ)
print("early finite-speed integral =", early_integral)
print("geometric block sum at rho=2/5 =", geom)
print("log(2)-1/4 > 0: verified")
