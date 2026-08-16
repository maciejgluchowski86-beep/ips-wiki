#!/usr/bin/env python3
"""Exact rational certificate for Student G Assignment 005.

This verifies the balanced-circulation obstruction at

    (a,b,c) = (1/10000, 1/100, 9999/10000).

The certificate is independent of the 16 positive phase weights Q and of
s>1.  The mathematical implication is the weighted AM--GM lemma in the
accompanying report:

    sum_e mu_e G_Q(e) >= C_mu * (s**(R_mu/C_mu) - 1) > 0.

The script verifies exactly:
1. strict residual-chamber membership;
2. normalization and nonnegativity of the 28-triple circulation;
3. all 16 spatial flow identities;
4. all 16 Q-exponent balance identities;
5. the exact positive changing-update mass C_mu and restart flux R_mu.

Only fractions.Fraction is used.  No floating-point optimization enters the
certificate verification.
"""

from fractions import Fraction as F


A = ("00", "11", "01", "10")
PAIRS = tuple((alpha, beta) for alpha in A for beta in A)


def bits(pair):
    return int(pair[0]), int(pair[1])


def diagonal(pair):
    return pair in ("00", "11")


def off_diagonal(pair):
    return pair in ("01", "10")


def exposed(alpha, beta):
    return diagonal(alpha) and off_diagonal(beta)


def entry_increment(alpha, beta, gamma, beta_new):
    """Number of newly created exposure edges when beta is updated."""
    return int((not exposed(alpha, beta)) and exposed(alpha, beta_new)) + int(
        (not exposed(beta, gamma)) and exposed(beta_new, gamma)
    )


# Strict near-East residual point.
a = F(1, 10000)
b = F(1, 100)
c = F(9999, 10000)

assert 0 < a < b
assert F(1, 2) <= c < 1
assert c >= a + b
# b >= sqrt(2)*(1-c), checked without irrational arithmetic.
assert b * b > 2 * (1 - c) * (1 - c)

rates = {
    (0, 0): a,
    (0, 1): b,
    (1, 0): c,
    (1, 1): F(0),
}


def outcomes(beta, gamma):
    """Exact common-uniform law of the new middle pair."""
    x, y = bits(beta)
    u, v = bits(gamma)
    p = rates[(x, u)]
    p_tilde = rates[(y, v)]
    return {
        "11": min(p, p_tilde),
        "00": 1 - max(p, p_tilde),
        "10": max(p - p_tilde, F(0)),
        "01": max(p_tilde - p, F(0)),
    }


def delta(alpha, beta, gamma, beta_new):
    """Exponent change of the 16 edge weights under beta -> beta_new."""
    out = {phase: 0 for phase in PAIRS}
    out[(alpha, beta_new)] += 1
    out[(beta_new, gamma)] += 1
    out[(alpha, beta)] -= 1
    out[(beta, gamma)] -= 1
    return out


D = 35378973959396206576874982782015790

# Integer weights W_e.  All unlisted triple weights are zero.
W = {
    ("00", "00", "01"): 4445398949312905081615855043064000,
    ("00", "11", "00"): 91095378005220269980796203014000,
    ("00", "11", "01"): 58736277707417592363434243646558,
    ("00", "11", "10"): 70630552927090213332617368110942,
    ("00", "01", "01"): 28448549891729378692982951213700,
    ("00", "01", "10"): 5718765235555301816115306641886300,
    ("00", "10", "01"): 2949418712365070463554452020574200,
    ("00", "10", "10"): 14672250265018942560267863425800,
    ("11", "00", "01"): 115914969605660652497282417211242,
    ("11", "00", "10"): 16536617826918181602523909538758,
    ("11", "11", "01"): 1764590729389757134240690903500,
    ("11", "01", "10"): 60500868436807349497674934550058,
    ("11", "10", "01"): 70630552927090213332617368110942,
    ("01", "00", "00"): 1858737959368023216913230451744429,
    ("01", "00", "10"): 2947554344803171224512195974461242,
    ("01", "11", "00"): 26683959162339621558742260310200,
    ("01", "11", "11"): 1764590729389757134240690903500,
    ("01", "01", "11"): 28448549891729378692982951213700,
    ("01", "01", "01"): 158346233425721318082272145,
    ("01", "10", "00"): 3993023065113075401074624538915829,
    ("01", "10", "01"): 2918915497745675337952683261246087,
    ("10", "00", "00"): 2586660989944881864702624591319571,
    ("10", "00", "11"): 220462208639728075676847814771500,
    ("10", "00", "01"): 1185899866528465460695152132824758,
    ("10", "11", "00"): 14672250265018942560267863425800,
    ("10", "01", "00"): 4806292304171194441425426426205671,
    ("10", "01", "10"): 1132672458866641573414326223725558,
    ("10", "10", "11"): 14672250265018942560267863425800,
}

assert len(W) == 28
assert all(weight > 0 for weight in W.values())
assert sum(W.values()) == D


def mu(triple):
    return F(W.get(triple, 0), D)


# ---------------------------------------------------------------------------
# Spatial circulation identities.
# ---------------------------------------------------------------------------
for alpha, beta in PAIRS:
    outgoing = sum(mu((alpha, beta, gamma)) for gamma in A)
    incoming = sum(mu((delta_state, alpha, beta)) for delta_state in A)
    assert outgoing == incoming, (alpha, beta, outgoing, incoming)


# ---------------------------------------------------------------------------
# Q-exponent balance and restart/changing-update masses.
# ---------------------------------------------------------------------------
balance = {phase: F(0) for phase in PAIRS}
R_mu = F(0)
C_mu = F(0)

for alpha in A:
    for beta in A:
        for gamma in A:
            triple = (alpha, beta, gamma)
            mass = mu(triple)
            if mass == 0:
                continue
            for beta_new, probability in outcomes(beta, gamma).items():
                if probability == 0 or beta_new == beta:
                    continue
                for phase, exponent_change in delta(
                    alpha, beta, gamma, beta_new
                ).items():
                    balance[phase] += mass * probability * exponent_change
                R_mu += (
                    mass
                    * probability
                    * entry_increment(alpha, beta, gamma, beta_new)
                )
                C_mu += mass * probability

assert all(value == 0 for value in balance.values())

R_expected = F(
    40097221742150361438903,
    4060682358517754276494700,
)
C_expected = F(
    10111075801610946800285497,
    812136471703550855298940000,
)
ratio_expected = F(
    8019444348430072287780600,
    10111075801610946800285497,
)

assert R_mu == R_expected
assert C_mu == C_expected
assert R_mu > 0
assert C_mu > 0
assert R_mu / C_mu == ratio_expected
assert 0 < ratio_expected < 1


print("strict residual point: verified")
print("28-triple circulation normalization: verified")
print("16 spatial flow identities: verified")
print("16 Q-exponent balance identities: verified")
print("R_mu =", R_mu)
print("C_mu =", C_mu)
print("R_mu/C_mu =", R_mu / C_mu)
print(
    "AM-GM certificate: for every positive Q and s>1, "
    "sum mu_e G_Q(e) >= C_mu*(s**(R_mu/C_mu)-1) > 0"
)
