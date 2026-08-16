# Group meeting 002: genealogical variance theorem enters audit

Date: 2026-08-16

Professor review of Graduate Student D assignment 002:

- `students/student-d/002-four-walk-cancellation.md`, commit `e73fd25`;
- Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), especially definitions (2.1) and estimates (5.5)--(5.8);
- independent Professor reconstruction `notes/professor-assignment-002-verification.md`.

state_narrowed: yes

Evidence pointer: Student D's report and `notes/professor-assignment-002-verification.md`; the source interface was checked directly against the published/arXiv-v2 paper.

## Professor verdict

The claimed proof survives the Professor's independent reconstruction and is promoted to **claimed**, not verified.

The decisive new mechanism is to condition on the entire voter genealogy at the observation time instead of decomposing the path in time. Conditional on the Harris arrows, ancestral clusters receive independent Bernoulli initial labels and the discordant-edge count is a weighted cut statistic on the quotient multigraph of clusters.

Let

$$
q_t^G=\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t),
$$

with meeting time defined as in the source, so walkers starting at the same vertex meet at time zero. The reconstruction gives the deterministic-graph inequality

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_t)
\le2q_t^G
}
$$

for every finite simple `d`-regular graph, every `u in (0,1)`, and every `t>=0`.

The two terms in total variance are controlled separately:

1. conditional cut variance is bounded by the second moment of ancestral cluster sizes, exactly giving at most `q_t^G` after averaging;
2. the variance of the conditional mean is the variance of the number `J_t` of original edges whose endpoints have coalesced genealogically. Pairwise covariances of the indicators `Y_e` are bounded by the probability that the two ancestral edge-families cross-interact. Averaging over edge pairs and using source (5.6) gives at most `4p^2q_t^G<=q_t^G`, where `p=2u(1-u)<=1/2`.

The potentially delicate coupling in the second item was checked explicitly. Within-family coalescence does not create an extra interaction term: the coalescing family process may be obtained from four independent walk paths by identification after within-family meetings, and any cross-family interaction is contained in the source event from (5.5).

## Random-regular consequence

The source's (5.7), via (5.8), the stationary mean meeting time `Theta(n)`, and a high-probability spectral-gap bound, gives

$$
q_{t_n}^G=O_{\mathbb P}(t_n/n)
$$

for deterministic `1<=t_n=o(n)`. Because `q_0=1/n`, the source's bare `O(t/n)` wording cannot be used uniformly below time one; instead monotonicity gives

$$
q_{t_n}^G\le q_1^G=O_{\mathbb P}(1/n)
$$

for `0<=t_n<1`.

Hence

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}\left(\frac{1+t_n}{n}\right)
}
$$

for every deterministic `t_n=o(n)`. Chebyshev gives the corrected theorem

$$
\mathbf P_u^G\left(
|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)\xrightarrow{\mathbb P}0
$$

for every `C_n->infinity`.

For every `t_n>=1` with `t_n=o(n)`, the stronger variance bound `O_P(t_n/n)` proves the scale proposed in source Eq. (1.9). Combined with Meeting 001's explicit counterexample at `t_n=n^{-3}`, the current claimed picture is: the displayed source statement is false because of its unrestricted very-small-time quantifier, while its intended sharp dynamical scale holds from time one onward.

## Standing novelty standard

This is not a larger-window, larger-order, or better-constant instantiation of an existing method. If correct and novel, it is structural mathematics: a deterministic graph inequality reducing the variance of voter discordance to a two-walk meeting probability, followed by resolution of the corrected all-sublinear target and of the source scale for `t_n>=1`.

However, research-contribution status is **pending an independent closest-prior-work audit**. The fact that the 2024 paper posed Eq. (1.9) as open is strong evidence, not sufficient publication-level priority checking.

## Verification status and next action

Register the central package as `VOTER-CONC-001`, status `claimed`.

It is not promoted to `verified`. Two genuinely independent hostile correctness reviews are now required. If both survive with no substantive objection, run a dedicated novelty/closest-prior-work audit before verified promotion or manuscript contribution language.

The two correctness reviews are assigned in:

- `audits/assignment-001-review-a.md`;
- `audits/assignment-002-review-b.md`.

Graduate Student D is idle while the independent reviews run.

## Wiki trigger

A central theorem has now entered independent audit, so the protocol's wiki-freeze review trigger fires. Professor recommendation remains **keep the live wiki frozen** until correctness and novelty audits are complete. Nothing is promoted to `docs/` at this meeting.

## Direction decision

**continue through independent audit.** No further development assignment is issued until the claimed theorem is stress-tested.
