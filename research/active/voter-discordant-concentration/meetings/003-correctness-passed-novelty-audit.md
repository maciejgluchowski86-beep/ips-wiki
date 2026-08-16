# Group meeting 003: correctness reviews pass; novelty gate remains

Date: 2026-08-16

Professor review of the two independent hostile correctness audits of `VOTER-CONC-001`:

- Review A: commit `add0681`, `audits/001-genealogy-review-a.md`;
- Review B: commit `45f960b`, `audits/002-genealogy-review-b.md`.

Both reviewers independently reconstructed the argument. Review B states explicitly that it did not read Review A. Both return `PASS` and request no mathematical repair.

state_narrowed: yes

Evidence pointer: the two audit files above. Both directly check the conditioning argument, conditional cut variance, cluster-square/meeting identity, four-lineage coupling, source normalization, random-regular meeting estimate, probability mode, and the very-small-time counterexample.

## Correctness ruling

The correctness barrier fixed in Meeting 002 has been passed.

Review A finds the deterministic inequality correct for every finite simple `d`-regular graph with `d>=1`, with no connectedness assumption, and verifies the delicate point that within-family coalescence creates no omitted error term. It also notes that the source cross-family event may be larger than the first active cross-family collision because it tracks retired raw paths; this only strengthens the required upper bound.

Review B reaches the same deterministic conclusion independently and verifies the fixed-`d>=3` random-regular consequence, the rate-one walk convention, the quenched/environment probability convention, and the `t_n=n^{-3}`, `C_n=log n` counterexample. It independently identifies the small-time imprecision in the printed source estimate (5.7) and confirms that the project already has the correct repair through source (5.8) and monotonicity.

No reviewer found a mathematical defect in

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le 2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
$$

## Promotion decision

`VOTER-CONC-001` remains **claimed** for the moment.

This is not because correctness review failed. It is because Meeting 002 explicitly required a dedicated closest-prior-work / novelty audit after two surviving correctness reviews and before `verified` promotion or manuscript contribution language. I am preserving that gate exactly. The present status should be read as:

- correctness: Professor reconstruction + two independent hostile `PASS` reviews;
- registry status: `claimed`, pending the pre-committed novelty audit;
- research-contribution status: unresolved until that audit.

This is the same stage at which the earlier BABP result was ultimately reclassified after direct source comparison. The fact that Avena--Baldasso--Hazra--den Hollander--Quattropani posed (1.9) as open is strong evidence, but it does not by itself establish priority for the deterministic genealogical variance inequality or for the proof mechanism.

## Reviewer clarifications folded into the theorem statement

The stable claim language is tightened now rather than leaving these points as reviewer remarks.

1. The deterministic theorem is stated for finite simple `d`-regular graphs with **`d>=1`**. Connectedness is not required.
2. The random-regular application retains **fixed `d>=3`**.
3. The all-small-time meeting estimate is attributed to source **(5.8)** together with the high-probability `Theta(n)` stationary mean meeting time and spectral-gap input; for `0<=t<1`, monotonicity may be used. The bare printed `O(t/n)` wording in source (5.7) is not used uniformly down to zero.
4. The statement about the defect in source (1.9) is made at theorem level: the literal displayed statement is false because it permits unrestricted very-small times; the project proves its `C_n sqrt(t_n/n)` scale for every deterministic `1<=t_n=o(n)`. No claim is made here that every possible subunit sequence has been completely classified under the original scale.

These clarifications do not change the mathematics proved by Student D.

## Novelty / closest-prior-work audit

A fresh external audit is now commissioned at

`audits/assignment-003-novelty-prior-work.md`.

It must not treat the source open-problem statement as sufficient evidence. It must search predecessor and successor literature, alternate terminology, and citation chains for the deterministic finite-graph variance inequality, the genealogy-conditioned quotient-cut argument, and any stronger general voter-model variance/covariance theorem that would subsume the result.

The audit must distinguish three possible novelty statuses separately:

1. the deterministic inequality on arbitrary positive-degree regular graphs;
2. the corrected all-sublinear random-regular concentration theorem;
3. the source-scale conclusion for deterministic `1<=t_n=o(n)` and the small-time correction of literal (1.9).

A negative novelty result will not undo correctness. It will change research-contribution status exactly as in the BABP case.

## Direction

**continue through the novelty audit.**

Graduate Student D remains idle. No further development is assigned until priority is settled.

## Wiki

Keep the live wiki frozen. Correctness review has passed, but novelty/contribution status is not yet settled and no `proved here` promotion is appropriate yet.
