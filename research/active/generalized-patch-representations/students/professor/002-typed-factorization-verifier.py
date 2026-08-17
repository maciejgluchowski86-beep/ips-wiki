#!/usr/bin/env python3
"""Exact finite gate for Assignment 002.

The test uses d=3 and two sites with two consecutive selected records.
It includes:

* two hidden source outcomes at each selected record;
* a genuine empty-target source-retyping mark between the records;
* an incoming typed-target conflict at the second record;
* future nonempty-target clocks in two different end patches.

All five hidden variables are taken independent and fair.  This is realizable
inside the Poisson reference construction: choose equal absolute branch rates
for the selected-record outcomes, and choose each relevant Poisson subinterval
so that P(at least one point)=1/2 (rate*time = log 2).  The script never uses
floating point; it works only with exact Fractions.

It proves three finite-gate facts:

1. on noncemetery histories, global exact-skeleton consistency is exactly the
   product of the one-patch consistency indicators;
2. conditioning only on the coarse record list does NOT factor because a
   target conflict sends the global dual to cemetery and removes all future
   no-record constraints at once;
3. after multiplying by the noncemetery/zero-weight indicator, the reference
   measure factors exactly over the three nontrivial patch variables.
"""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import product


# Two selected records.
# R1: source site 0, pre-type 1, target site 1 carrying type 1.
#     Hidden source outcome s1 is 1 or 2.
# R2: source site 1, pre-type 1, target site 0 carrying type 1.
#     Hidden source outcome s2 is 0 or 1.
#
# Between R1 and R2 an empty-target mark on site 0 is indexed by source type 2
# and outcome 1.  If present while site 0 has type 2, it retypes 2 -> 1.
#
# After R2:
# B is the presence of a nonempty-target clock on site 0 indexed by source
# type 1.  On a noncemetery history site 0 has type 1 after the incoming merge,
# so B=1 would create an extra selected record.
# C is the presence of a nonempty-target clock on site 1 indexed by source
# type 1.  It creates an extra record iff the hidden R2 outcome s2 is 1.

BASE_WEIGHT = Q(1, 32)  # five independent fair hidden variables

rows = []
full_mass = Q(0)
weighted_mass = Q(0)
conflict_mass_inside_full = Q(0)
full_b1_mass = Q(0)
full_conflict_b1_mass = Q(0)

# Joint tables for the representation-sufficient weighted law.
# A=(s1,e) is the patch from R1 on site 0 through the incoming R2 boundary.
# B is the site-0 end patch after R2.
# Cstate=(s2,c) is the site-1 outgoing end patch after R2.
weighted_joint = defaultdict(Q)
weighted_A = defaultdict(Q)
weighted_B = defaultdict(Q)
weighted_C = defaultdict(Q)

conflict_configs = 0
noncemetery_equivalence_checks = 0

for s1, e, s2, b, c in product((1, 2), (0, 1), (0, 1), (0, 1), (0, 1)):
    # ----- Global source-line evolution before R2 -----
    # Immediately after R1, site 0 has the hidden source outcome s1 and site 1
    # is active with incoming type 1.
    x0_before_r2 = s1

    # Optional empty-target local dual mark 2 -> 1 on site 0.
    if e == 1 and x0_before_r2 == 2:
        x0_before_r2 = 1

    # R2 carries incoming target type 1 to site 0.  It is compatible precisely
    # with local pre-state 0 or 1.  In this gate x0_before_r2 is 1 or 2.
    compatible = x0_before_r2 in (0, 1)
    conflict = not compatible
    if conflict:
        conflict_configs += 1

    # ----- Local patch consistency factors -----
    # Patch A terminates at the incoming R2 boundary on site 0.
    con_A = compatible

    # If R2 is compatible, site 0 starts its next incoming patch at type 1.
    # Hence any B point is an unselected successful nonempty-target clock.
    con_B = b == 0

    # The site-1 end patch starts at hidden R2 outcome s2.  A future clock C is
    # successful only when that local type is 1.
    con_C = (s2 == 0) or (c == 0)

    product_consistency = con_A and con_B and con_C

    # ----- Direct global exact-skeleton simulation -----
    # R2 is selected because site 1 has pre-source type 1.  If the incoming
    # target conflicts, the global dual hits cemetery at R2.  Thereafter all
    # future clocks are automatically absent from the successful skeleton.
    if conflict:
        noncemetery = False
        exact_two_record_skeleton = True
    else:
        noncemetery = True
        # R2 makes site 0 type 1 and makes site 1 equal to hidden outcome s2.
        extra_record_site0 = b == 1
        extra_record_site1 = (s2 == 1 and c == 1)
        exact_two_record_skeleton = not (extra_record_site0 or extra_record_site1)

    weighted_exact = noncemetery and exact_two_record_skeleton

    # This is the finite version of the load-bearing local-consistency lemma.
    assert weighted_exact == product_consistency
    assert exact_two_record_skeleton == (conflict or product_consistency)
    noncemetery_equivalence_checks += 1

    rows.append(
        (s1, e, s2, b, c, compatible, product_consistency,
         exact_two_record_skeleton, weighted_exact)
    )

    if exact_two_record_skeleton:
        full_mass += BASE_WEIGHT
        if conflict:
            conflict_mass_inside_full += BASE_WEIGHT
        if b == 1:
            full_b1_mass += BASE_WEIGHT
        if conflict and b == 1:
            full_conflict_b1_mass += BASE_WEIGHT

    if weighted_exact:
        weighted_mass += BASE_WEIGHT
        A = (s1, e)
        B = b
        Cstate = (s2, c)
        weighted_joint[(A, B, Cstate)] += BASE_WEIGHT
        weighted_A[A] += BASE_WEIGHT
        weighted_B[B] += BASE_WEIGHT
        weighted_C[Cstate] += BASE_WEIGHT


assert len(rows) == 32
assert noncemetery_equivalence_checks == 32
assert conflict_configs == 8  # s1=2, empty-target 2->1 mark absent

# Exact masses.
assert full_mass == Q(17, 32)
assert weighted_mass == Q(9, 32)
assert conflict_mass_inside_full == Q(1, 4)

# ----- Full conditional factorization fails -----
p_conflict_given_full = conflict_mass_inside_full / full_mass
p_b1_given_full = full_b1_mass / full_mass
p_conflict_b1_given_full = full_conflict_b1_mass / full_mass

assert p_conflict_given_full == Q(8, 17)
assert p_b1_given_full == Q(4, 17)
assert p_conflict_b1_given_full == Q(4, 17)
assert p_conflict_b1_given_full != p_conflict_given_full * p_b1_given_full
assert p_conflict_given_full * p_b1_given_full == Q(32, 289)

# ----- Weighted/noncemetery factorization is exact -----
# Check the entire normalized joint table, not merely one covariance.
A_values = ((1, 0), (1, 1), (2, 0), (2, 1))
B_values = (0, 1)
C_values = ((0, 0), (0, 1), (1, 0), (1, 1))

factorization_cells_checked = 0
for A in A_values:
    for B in B_values:
        for Cstate in C_values:
            lhs = weighted_joint[(A, B, Cstate)] / weighted_mass
            rhs = (
                weighted_A[A] / weighted_mass
                * weighted_B[B] / weighted_mass
                * weighted_C[Cstate] / weighted_mass
            )
            assert lhs == rhs, (A, B, Cstate, lhs, rhs)
            factorization_cells_checked += 1

assert factorization_cells_checked == 32

# The local consistent-patch masses multiply to the weighted skeleton mass:
# P(A compatible)=3/4, P(no B)=1/2,
# P(s2 inactive or no C | source-outcome/end-patch reference)=3/4.
assert sum(weighted_A.values()) == weighted_mass
assert Q(3, 4) * Q(1, 2) * Q(3, 4) == weighted_mass

print("d=3 two-record hidden configurations checked:", len(rows))
print("incoming-target-conflict configurations checked:", conflict_configs)
print("noncemetery global/local consistency equivalences:", noncemetery_equivalence_checks)
print("bare two-record skeleton mass:", full_mass)
print("noncemetery weighted skeleton mass:", weighted_mass)
print("P(conflict | bare skeleton):", p_conflict_given_full)
print("P(future B | bare skeleton):", p_b1_given_full)
print("P(conflict and future B | bare skeleton):", p_conflict_b1_given_full)
print("product of bare conditional marginals:", p_conflict_given_full * p_b1_given_full)
print("weighted factorization cells checked:", factorization_cells_checked)
print("all typed patch-factorization finite-gate checks passed")
