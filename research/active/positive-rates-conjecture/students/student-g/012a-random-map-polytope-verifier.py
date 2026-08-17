#!/usr/bin/env python3
"""Exact random-map / ancestry-polytope checks for Student G Assignment 012.

At P_h=(a,b,c)=(1/10000,1/100,9999/10000), enumerate all 15 nonidentity
Boolean maps F:{0,1}^2->{0,1}.  A rate q_F contributes to the four flip
rates according to whether F(x,y) differs from x.

The script:
1. classifies each map by essential parent set;
2. enumerates every basic feasible exact random-map decomposition;
3. projects them to ancestry rates (d,s,j,r);
4. verifies the exact H-description of the projected polytope;
5. verifies that the H-polytope has exactly 11 vertices and that every one
   is realized by an exact decomposition;
6. checks the canonical and lexicographically optimized decompositions.

All arithmetic is exact SymPy rational arithmetic.
"""

from itertools import combinations, product
import sympy as sp

a = sp.Rational(1, 10000)
b = sp.Rational(1, 100)
c = sp.Rational(9999, 10000)
lam = sp.Matrix([a, b, 1-c, 1])
g = b-a

INPUTS = ((0,0),(0,1),(1,0),(1,1))

def classify(bits):
    dep_self = bits[0] != bits[2] or bits[1] != bits[3]
    dep_right = bits[0] != bits[1] or bits[2] != bits[3]
    if not dep_self and not dep_right:
        return "d"
    if dep_self and not dep_right:
        return "s"
    if not dep_self and dep_right:
        return "j"
    return "r"

maps = []
for bits in product((0,1), repeat=4):
    flips = tuple(int(bits[k] != INPUTS[k][0]) for k in range(4))
    cls = classify(bits)
    if flips == (0,0,0,0):
        continue
    maps.append((bits, cls, flips))

assert len(maps) == 15
assert sum(cls == "d" for _,cls,_ in maps) == 2
assert sum(cls == "s" for _,cls,_ in maps) == 1
assert sum(cls == "j" for _,cls,_ in maps) == 2
assert sum(cls == "r" for _,cls,_ in maps) == 10

cols = [sp.Matrix(flips) for _,_,flips in maps]
A = sp.Matrix.hstack(*cols)

def aggregate(q):
    out = {k:sp.Rational(0) for k in "dsjr"}
    for qi,(_,cls,_) in zip(q,maps):
        out[cls] += qi
    return tuple(sp.factor(out[k]) for k in "dsjr")

# The equality matrix has rank 4, so every vertex has at most four positive
# coordinates.  Enumerate all basic feasible decompositions exactly.
bfs = {}
for k in range(1,5):
    for idxs in combinations(range(len(maps)), k):
        M = sp.Matrix.hstack(*[cols[i] for i in idxs])
        if M.rank() != k:
            continue
        solset = sp.linsolve((M, lam))
        if solset is sp.EmptySet:
            continue
        sol = next(iter(solset))
        if any(v.free_symbols for v in sol):
            continue
        if any(v < 0 for v in sol):
            continue
        q = [sp.Rational(0)] * len(maps)
        for i,v in zip(idxs, sol):
            q[i] = sp.factor(v)
        q = tuple(q)
        assert A * sp.Matrix(q) == lam
        bfs[q] = aggregate(q)

assert len(bfs) == 40
projected = set(bfs.values())
assert len(projected) == 26

# Exact projected H-description at P_h, for y=(d,s,j,r):
#
# d,s,j >= 0,
# j+r >= c,
# d+r >= c,
# d+s+j+r >= 1,
# d+2s+j <= a+(1-c)=1/5000,
# 2d+4s+2j+r <= a+b+(1-c)+1=5051/5000.
ineq = [
    ((-1, 0, 0, 0), 0),
    ((0,-1, 0, 0), 0),
    ((0, 0,-1, 0), 0),
    ((0, 0,-1,-1), -c),
    ((-1,0, 0,-1), -c),
    ((-1,-1,-1,-1), -1),
    ((1, 2, 1, 0), a + (1-c)),
    ((2, 4, 2, 1), a + b + (1-c) + 1),
]

def feasible_y(y):
    for coeff,rhs in ineq:
        lhs = sum(sp.Rational(coeff[k]) * y[k] for k in range(4))
        if lhs > rhs:
            return False
    return True

assert all(feasible_y(y) for y in projected)

# Enumerate vertices of the H-polytope by intersections of four active facets.
h_vertices = set()
for idxs in combinations(range(len(ineq)), 4):
    M = sp.Matrix([ineq[i][0] for i in idxs])
    if M.rank() < 4:
        continue
    rhs = sp.Matrix([ineq[i][1] for i in idxs])
    y = tuple(sp.factor(v) for v in M.LUsolve(rhs))
    if feasible_y(y):
        h_vertices.add(y)

expected_vertices = {
    (0,0,0,1),
    (0,0,0,sp.Rational(5051,5000)),
    (0,0,sp.Rational(1,10000),c),
    (0,0,sp.Rational(1,5000),c),
    (0,0,sp.Rational(1,5000),sp.Rational(5049,5000)),
    (0,sp.Rational(1,10000),0,c),
    (0,sp.Rational(1,10000),0,sp.Rational(5049,5000)),
    (sp.Rational(1,10000),0,0,c),
    (sp.Rational(1,10000),0,sp.Rational(1,10000),sp.Rational(4999,5000)),
    (sp.Rational(1,5000),0,0,c),
    (sp.Rational(1,5000),0,0,sp.Rational(5049,5000)),
}
assert h_vertices == expected_vertices
assert h_vertices.issubset(projected)

def map_index(bitstr):
    bits = tuple(int(ch) for ch in bitstr)
    return next(i for i,(bb,_,_) in enumerate(maps) if bb == bits)

# Canonical decomposition:
# 1111 at a, 0000 at 1-c, OR=0111 at g=b-a,
# x AND (NOT y)=0010 at c.
q_can = [sp.Rational(0)] * len(maps)
q_can[map_index("1111")] = a
q_can[map_index("0000")] = 1-c
q_can[map_index("0111")] = g
q_can[map_index("0010")] = c
assert A * sp.Matrix(q_can) == lam
assert aggregate(q_can) == (a + 1-c, 0, 0, c+g)
assert aggregate(q_can) == (
    sp.Rational(1,5000),0,0,sp.Rational(5049,5000)
)

# Subject to maximal death, minimal branching is attained by replacing OR by
# XOR and reducing the 0010 rate accordingly.
q_lex = [sp.Rational(0)] * len(maps)
q_lex[map_index("1111")] = a
q_lex[map_index("0000")] = 1-c
q_lex[map_index("0110")] = g
q_lex[map_index("0010")] = c-g
assert A * sp.Matrix(q_lex) == lam
assert aggregate(q_lex) == (a+1-c,0,0,c)

max_d = max(y[0] for y in h_vertices)
min_r_at_max_d = min(y[3] for y in h_vertices if y[0] == max_d)
assert max_d == a + (1-c) == sp.Rational(1,5000)
assert min_r_at_max_d == c

print("15 nonidentity Boolean maps classified exactly")
print("40 basic feasible decompositions; 26 projected ancestry points")
print("ancestry polytope H-description verified; 11 exact vertices")
print("max d =", max_d)
print("min r at max d =", min_r_at_max_d)
print("canonical ancestry =", aggregate(q_can))
print("lexicographic optimizer ancestry =", aggregate(q_lex))
