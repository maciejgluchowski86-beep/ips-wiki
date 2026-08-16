# Group meeting 004: novelty audit fails; voter-concentration programme closes

Date: 2026-08-16

Professor review of:

- novelty / closest-prior-work audit: commit `5ab5dce`, `audits/003-novelty-prior-work.md`;
- Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), especially Proposition 4.1 proof (4.2), equations (5.5)--(5.6), and Lemma 5.2 / equation (5.8);
- the two previously passed hostile correctness reviews of `VOTER-CONC-001`.

state_narrowed: yes

Evidence pointer: `audits/003-novelty-prior-work.md`, together with the primary-source equations listed above.

## Professor verification of the fatal prior-art comparison

I agree with the novelty auditor.

Avena et al. already contain the two ingredients that make the project's random-regular concentration conclusions an immediate corollary up to an irrelevant constant.

First, in the proof of Proposition 4.1, equation (4.2), they prove the relevant two-edge negative-dependence/decoupling statement on the event that the two endpoint-walk families do not cross-interact. For i.i.d. Bernoulli initial opinions, the same pathwise separation gives for discordance indicators `X_e(t),X_f(t)`

$$
\operatorname{Cov}(X_e(t),X_f(t))
\le \mathbf P(\tau^{e,f}\le t).
$$

Second, their equation (5.5) defines the four-endpoint cross-family interaction time and equation (5.6) gives

$$
\mathbf P_{\nu\otimes\nu}(\tau^{e,f}\le t)
\le 4\mathbf P_{\pi\otimes\pi}(\tau_{\rm meet}\le t).
$$

Averaging over ordered uniform edge pairs therefore yields immediately

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le 4\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
$$

The project's correctness-reviewed theorem improves the constant `4` to `2` and gives a cleaner genealogy-conditioned quotient-cut proof, but it does not change the theorem-level mechanism needed for the random-regular consequences.

Finally, source equation (5.8), together with the mean-meeting-time and spectral-gap inputs used in the same paper, gives the stable meeting bound `O_P((1+t)/n)` on deterministic sublinear sequences and `O_P(t/n)` when `t>=1`. Thus the corrected all-sublinear concentration theorem and the source-scale theorem for deterministic `1<=t_n=o(n)` already follow from the source ingredients by Chebyshev.

This is exactly the kind of distinction the standing novelty rule is meant to enforce: a sharper constant and a new proof remain useful mathematics, but do not convert an immediate prior-work corollary into a new project theorem.

## Status of `VOTER-CONC-001`

Mathematical correctness is unaffected.

The claim is promoted from `claimed` to **`verified`** because it has survived the Professor reconstruction and two genuinely independent hostile correctness reviews with no mathematical repair.

Its research-contribution status is simultaneously set to:

**not a new project result under the standing novelty standard.**

Closest prior work is Avena et al. (2024), Proposition 4.1 proof (4.2) plus (5.5)--(5.6), which imply the same variance-to-meeting reduction with constant `4`; their (5.8) then gives the same asymptotic concentration conclusions. The project's factor `2` inequality and quotient-genealogy proof are retained as verified technical mathematics.

## Small-time correction

The literal counterexample to source Eq. (1.9) remains mathematically correct. Its priority remains unresolved because the novelty auditor could not inspect Federico Capannoli's 2025 thesis *Opinion Dynamics on Random Graphs*.

I am **not** requesting that thesis as an active research task. Even if the literal small-time correction turns out to be new, it is a narrow quantifier/source correction rather than the substantive sharp-concentration theorem this programme was selected to solve. Settling its priority is below the opportunity cost of starting the next scientific direction. If the thesis is supplied later, attribution can be updated without reopening the programme.

## Programme decision

**Close the voter-discordant-concentration programme.**

Outcome: mathematically verified technical record, but no new project result under the standing novelty standard.

Do not reopen this programme merely to optimize the constant `2`, further streamline the genealogy proof, or repackage the immediate factor-`4` corollary. A future return would require a genuinely different theorem beyond what follows directly from the 2024 source ingredients.

Graduate Student D becomes idle with this lineage.

## Opportunity-cost pivot

The next active direction is the remaining highest-ranked credible target from Student A's reconnaissance that has not already been closed: **voter-model discordance on undirected heterogeneous configuration models**.

Den Hollander's 2025 overview explicitly states that extending the regular-graph discordance theorems to the configuration model with unequal vertex degrees remains open and that even the analogues of the regular constants/profile are unknown. The directed heterogeneous case has progressed separately and does not resolve the undirected problem.

This is a genuinely new direction rather than another concentration-window variant. It also reuses the random-walk/voter duality knowledge acquired here without pretending that the closed theorem package is a contribution.

A new persistent Graduate Student E should receive a source-grounded first assignment whose first objective is to derive or refute a credible candidate for the heterogeneous short-time profile and consensus-time constant in a bounded-degree configuration model, before attempting a full proof.

## Wiki

Keep the live wiki frozen. No `proved here` promotion follows from this programme because the verified theorem package is not a new project result.
