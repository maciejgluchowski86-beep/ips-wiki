#!/usr/bin/env python3
"""Exact finite gate for Assignment 003.

The d=3 test uses the same two-record geometry as Assignment 002.
All hidden variables are discrete and all potential integrals are exact
fractions.  Exponentials are *not* numerically evaluated: a Feynman--Kac
weight is represented exactly as c*exp(q), where c is 0,+1,-1 and q is a
Fraction.  Multiplication multiplies c and adds q.

Checks:

* 32 hidden configurations in the d=3 two-record gate;
* 8 genuine incoming-target-conflict configurations;
* two physical terminal configurations for every hidden configuration;
* pathwise global/local weight equality on every noncemetery exact-two-record
  realization;
* exact zero on every cemetery realization;
* exact weighted representation identity on all 64 hidden/terminal cells;
* selected outgoing signs occur exactly once;
* the effective empty-target 2->1 retyping sign occurs exactly once;
* deletion/retyping changes the potential integral on the correct interval;
* bulk weights are independent of terminal physical data and end weights use
  only their one-site terminal factor;
* a separate d=2 typed/binary local-weight specialization.

There is no floating point and no Monte Carlo.
"""

from fractions import Fraction as Q
from itertools import product


class FormalWeight:
    """Exact symbolic c*exp(q), c in {-1,0,1}, q rational."""

    __slots__ = ("coefficient", "exponent")

    def __init__(self, coefficient=1, exponent=Q(0)):
        coefficient = int(coefficient)
        assert coefficient in (-1, 0, 1)
        if coefficient == 0:
            self.coefficient = 0
            self.exponent = Q(0)
        else:
            self.coefficient = coefficient
            self.exponent = Q(exponent)

    @classmethod
    def zero(cls):
        return cls(0, Q(0))

    def __mul__(self, other):
        if self.coefficient == 0 or other.coefficient == 0:
            return FormalWeight.zero()
        return FormalWeight(
            self.coefficient * other.coefficient,
            self.exponent + other.exponent,
        )

    def __eq__(self, other):
        return (
            self.coefficient == other.coefficient
            and self.exponent == other.exponent
        )

    def __repr__(self):
        return f"FormalWeight({self.coefficient}, exp={self.exponent})"


def h(active_type, physical_value):
    """Reference-state indicator basis, with h_0 == 1."""
    return int(active_type == 0 or physical_value == active_type)


# ---------------------------------------------------------------------------
# d=3 two-record geometry
# ---------------------------------------------------------------------------
# Times:
#   initial typed state at time 0: site 0 has type 1;
#   R1 at t=1: source 0, pre-type 1, target site 1 carrying type 1;
#   optional empty-target 2->1 retyping mark at t=3/2 on source line 0;
#   R2 at t=2: source 1, pre-type 1, target site 0 carrying type 1;
#   horizon T=3.
#
# Hidden variables are the same five fair variables as Assignment 002:
#   s1 in {1,2}: hidden post-source type at R1;
#   e  in {0,1}: absence/presence of the empty-target 2->1 mark;
#   s2 in {0,1}: hidden post-source type at R2;
#   b  in {0,1}: future nonempty-target point on site 0, source type 1;
#   c  in {0,1}: future nonempty-target point on site 1, source type 1.
#
# b,c are consistency-test marks exactly as in Assignment 002.  A fixed
# two-record skeleton is exact iff b=0 and either s2=0 or c=0, provided the R2
# incoming target does not conflict.

T = Q(3)
T1 = Q(1)
TE = Q(3, 2)
T2 = Q(2)

# Exact local potential values.  Inactive type 0 has potential zero.
V = {
    (0, 0): Q(0),
    (0, 1): Q(2),
    (0, 2): Q(5),
    (1, 0): Q(0),
    (1, 1): Q(-3),
    (1, 2): Q(7),
}

# Exact branch signs.
EPS_R1 = {1: 1, 2: -1}
EPS_EMPTY_2_TO_1 = -1
EPS_R2 = {0: -1, 1: 1}


def d3_consistency(s1, e, s2, b, c):
    """Return conflict/noncemetery/exact-two-record consistency data."""
    x0_before_r2 = s1
    if e == 1 and x0_before_r2 == 2:
        x0_before_r2 = 1

    compatible = x0_before_r2 in (0, 1)
    conflict = not compatible
    con_b = b == 0
    con_c = (s2 == 0) or (c == 0)
    exact_two_record = compatible and con_b and con_c
    return conflict, compatible, con_b, con_c, exact_two_record


def d3_direct_global_weight(s1, e, s2, eta):
    """Direct global FK weight after R1,R2, before any future extra record.

    Returns zero exactly when R2's incoming target conflicts.  This function is
    compared to the fixed-skeleton local product only on exact-two-record
    histories; on a noncemetery history with b/c creating an extra record the
    actual later skeleton is different, as it should be.
    """
    sign = EPS_R1[s1]

    # Site 0 initial active interval [0,1].
    exponent = V[(0, 1)] * (T1 - Q(0))

    # Site 1 is activated by R1 and remains type 1 on [1,2].
    exponent += V[(1, 1)] * (T2 - T1)

    # Site 0 on [1,2], including the possible effective 2->1 retyping.
    x0_before_r2 = s1
    if s1 == 2 and e == 1:
        exponent += V[(0, 2)] * (TE - T1)
        exponent += V[(0, 1)] * (T2 - TE)
        sign *= EPS_EMPTY_2_TO_1
        x0_before_r2 = 1
    else:
        exponent += V[(0, s1)] * (T2 - T1)

    # Incoming target type 1 at R2.
    if x0_before_r2 not in (0, 1):
        return FormalWeight.zero()

    # R2 hidden source branch and the two end intervals [2,3].
    sign *= EPS_R2[s2]
    exponent += V[(0, 1)] * (T - T2)
    exponent += V[(1, s2)] * (T - T2)

    terminal = h(1, eta[0]) * h(s2, eta[1])
    return FormalWeight(sign * terminal, exponent)


def d3_local_patch_weights(s1, e, s2, eta):
    """Five patch weights for the inserted two-record skeleton.

    Returns (named_weights, sign_tag_counts).  The five patches are:

    P0-pre : site 0, initial incoming -> R1 outgoing, [0,1];
    P0-mid : site 0, R1 outgoing -> R2 incoming, [1,2];
    P1-mid : site 1, R1 incoming -> R2 outgoing, [1,2];
    P0-end : site 0, R2 incoming -> horizon, [2,3];
    P1-end : site 1, R2 outgoing -> horizon, [2,3].
    """
    named = {}
    tags = {"R1": 0, "R2": 0, "EMPTY_2_TO_1": 0}

    # Bulk patch P0-pre.  No selected sign belongs to the terminal R1 boundary;
    # R1's sign belongs to the next outgoing-start patch.
    named["P0-pre"] = FormalWeight(1, V[(0, 1)] * (T1 - Q(0)))

    # Bulk patch P0-mid starts at outgoing R1 and therefore owns R1's sign.
    sign_mid = EPS_R1[s1]
    tags["R1"] += 1
    if s1 == 2 and e == 1:
        exponent_mid = (
            V[(0, 2)] * (TE - T1)
            + V[(0, 1)] * (T2 - TE)
        )
        sign_mid *= EPS_EMPTY_2_TO_1
        tags["EMPTY_2_TO_1"] += 1
    else:
        exponent_mid = V[(0, s1)] * (T2 - T1)
    named["P0-mid"] = FormalWeight(sign_mid, exponent_mid)

    # Bulk patch P1-mid begins incoming at R1.  It carries no copy of R1 sign.
    named["P1-mid"] = FormalWeight(1, V[(1, 1)] * (T2 - T1))

    # End patch on site 0 begins incoming at R2 and carries only eta_0.
    named["P0-end"] = FormalWeight(
        h(1, eta[0]),
        V[(0, 1)] * (T - T2),
    )

    # End patch on site 1 begins outgoing at R2 and owns R2's selected sign.
    tags["R2"] += 1
    named["P1-end"] = FormalWeight(
        EPS_R2[s2] * h(s2, eta[1]),
        V[(1, s2)] * (T - T2),
    )

    return named, tags


def multiply_weights(named):
    out = FormalWeight(1, Q(0))
    for value in named.values():
        out = out * value
    return out


def run_d3():
    hidden_configs = 0
    conflict_configs = 0
    cemetery_terminal_checks = 0
    pathwise_noncemetery_checks = 0
    weighted_cells = 0
    selected_sign_ledger_checks = 0
    effective_empty_sign_checks = 0
    bulk_eta_independence_checks = 0
    end_one_site_checks = 0

    etas = ((1, 1), (1, 2))

    for s1, e, s2, b, c in product((1, 2), (0, 1), (0, 1), (0, 1), (0, 1)):
        hidden_configs += 1
        conflict, compatible, con_b, con_c, exact = d3_consistency(
            s1, e, s2, b, c
        )
        if conflict:
            conflict_configs += 1

        # Verify bulk factors are eta-independent before multiplying end data.
        bulk_snapshots = []
        end_snapshots = []
        for eta in etas:
            named, tags = d3_local_patch_weights(s1, e, s2, eta)
            bulk_snapshots.append(
                (named["P0-pre"], named["P0-mid"], named["P1-mid"])
            )
            end_snapshots.append((named["P0-end"], named["P1-end"]))

            # Selected signs are assigned exactly once, to source-start patches.
            assert tags["R1"] == 1
            assert tags["R2"] == 1
            selected_sign_ledger_checks += 2

            expected_empty_count = int(s1 == 2 and e == 1)
            assert tags["EMPTY_2_TO_1"] == expected_empty_count
            if expected_empty_count:
                effective_empty_sign_checks += 1

            direct = d3_direct_global_weight(s1, e, s2, eta)
            local_product = multiply_weights(named)

            # Pathwise theorem on the fixed inserted skeleton.
            if exact:
                assert direct == local_product, (
                    s1, e, s2, b, c, eta, direct, local_product
                )
                pathwise_noncemetery_checks += 1

            # Cemetery histories have zero global duality weight, independently
            # of terminal physical data.
            if conflict:
                assert direct == FormalWeight.zero()
                cemetery_terminal_checks += 1

            # Exact weighted representation cell:
            # 1_{noncemetery, G=g} W_global
            # = product_P (w_P 1_{Con(P)}).
            lhs = direct if exact else FormalWeight.zero()
            rhs = local_product if (compatible and con_b and con_c) else FormalWeight.zero()
            assert lhs == rhs, (s1, e, s2, b, c, eta, lhs, rhs)
            weighted_cells += 1

            # End dependence is one-site only.  Recompute each end patch after
            # changing the *other* physical coordinate.
            eta_other0 = (eta[0], 1 if eta[1] == 2 else 2)
            named_other0, _ = d3_local_patch_weights(s1, e, s2, eta_other0)
            assert named["P0-end"] == named_other0["P0-end"]
            eta_other1 = (2 if eta[0] == 1 else 1, eta[1])
            named_other1, _ = d3_local_patch_weights(s1, e, s2, eta_other1)
            assert named["P1-end"] == named_other1["P1-end"]
            end_one_site_checks += 2

        assert bulk_snapshots[0] == bulk_snapshots[1]
        bulk_eta_independence_checks += 1

    assert hidden_configs == 32
    assert conflict_configs == 8
    assert cemetery_terminal_checks == 16
    assert pathwise_noncemetery_checks == 18  # 9 exact skeletons x 2 eta
    assert weighted_cells == 64
    assert selected_sign_ledger_checks == 128
    assert effective_empty_sign_checks == 16
    assert bulk_eta_independence_checks == 32
    assert end_one_site_checks == 128

    # Explicit potential-segmentation tests, independent of the path loop.
    # Retyping 2->1 halfway through [1,2] changes the exponent to 7/2.
    retyped_mid, _ = d3_local_patch_weights(2, 1, 0, (1, 1))
    assert retyped_mid["P0-mid"].exponent == Q(7, 2)
    assert retyped_mid["P0-mid"].coefficient == 1  # R1(-) * empty(-)

    # If R1 leaves type 1, the entire middle interval has potential 2.
    type1_mid, _ = d3_local_patch_weights(1, 0, 0, (1, 1))
    assert type1_mid["P0-mid"].exponent == Q(2)

    # R2 deletion makes site 1 inactive on [2,3], while survival retains v=-3.
    deleted_end, _ = d3_local_patch_weights(1, 0, 0, (1, 1))
    active_end, _ = d3_local_patch_weights(1, 0, 1, (1, 1))
    assert deleted_end["P1-end"].exponent == Q(0)
    assert active_end["P1-end"].exponent == Q(-3)

    return {
        "hidden": hidden_configs,
        "conflicts": conflict_configs,
        "cemetery": cemetery_terminal_checks,
        "pathwise": pathwise_noncemetery_checks,
        "weighted": weighted_cells,
        "sign_ledger": selected_sign_ledger_checks,
        "empty_sign": effective_empty_sign_checks,
        "bulk_eta": bulk_eta_independence_checks,
        "end_local": end_one_site_checks,
    }


# ---------------------------------------------------------------------------
# d=2 binary specialization
# ---------------------------------------------------------------------------

def binary_typed_weight(hidden_s, death_present, eta_value):
    """Typed local weight on one outgoing-start end patch [0,1].

    hidden_s=0 is deletion; hidden_s=1 is survival.  If hidden_s=1 and the
    empty-target binary death is present at time 1/2, the state becomes 0.
    The binary empty-target death sign is +1, exactly as in the canonical
    paper.
    """
    V1 = Q(4)
    half = Q(1, 2)
    selected_sign = -1 if hidden_s == 0 else 1

    if hidden_s == 0:
        occupation = Q(0)
        x_end = 0
    elif death_present:
        occupation = half
        x_end = 0
    else:
        occupation = Q(1)
        x_end = 1

    return FormalWeight(
        selected_sign * h(x_end, eta_value),
        V1 * occupation,
    )


def binary_canonical_weight(hidden_s, death_present, eta_value):
    """Same patch written in canonical binary notation.

    F(z,P)=sigma(P)*exp(V*int X)*z^{X_1}; binary death has positive sign.
    """
    V1 = Q(4)
    half = Q(1, 2)
    sigma_P = -1 if hidden_s == 0 else 1

    if hidden_s == 0:
        active_time = Q(0)
        x_end = 0
    elif death_present:
        active_time = half
        x_end = 0
    else:
        active_time = Q(1)
        x_end = 1

    terminal = 1 if x_end == 0 else int(eta_value == 1)
    return FormalWeight(sigma_P * terminal, V1 * active_time)


def run_d2():
    checks = 0
    for hidden_s, death_present, eta_value in product((0, 1), (0, 1), (0, 1)):
        typed = binary_typed_weight(hidden_s, death_present, eta_value)
        canonical = binary_canonical_weight(hidden_s, death_present, eta_value)
        assert typed == canonical, (hidden_s, death_present, eta_value, typed, canonical)
        checks += 1
    assert checks == 8
    return checks


if __name__ == "__main__":
    stats = run_d3()
    d2_checks = run_d2()

    print("d=3 hidden configurations checked:", stats["hidden"])
    print("d=3 incoming-target-conflict configurations:", stats["conflicts"])
    print("cemetery x terminal-configuration zero checks:", stats["cemetery"])
    print("noncemetery exact-skeleton pathwise weight checks:", stats["pathwise"])
    print("weighted representation cells checked:", stats["weighted"])
    print("selected outgoing sign-ledger checks:", stats["sign_ledger"])
    print("effective empty-target sign checks:", stats["empty_sign"])
    print("bulk eta-independence checks:", stats["bulk_eta"])
    print("end one-site locality checks:", stats["end_local"])
    print("d=2 typed/binary specialization checks:", d2_checks)
    print("all explicit typed patch-representation checks passed")