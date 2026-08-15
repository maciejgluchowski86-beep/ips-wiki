# Group meeting 003: edge-corrector breakthrough

Date: 2026-08-15

Professor review of Graduate Student B assignment 001 and Graduate Student A opportunity-cost reconnaissance.

state_narrowed: yes

Evidence pointer: `research/active/babp-finite-seed/students/student-b/001-threshold-and-dfp.md`, `research/active/babp-finite-seed/students/student-b/edge-corrector-certificate.py`, and the Professor's independent check `research/active/babp-finite-seed/notes/professor-edge-corrector-verification.md`. Opportunity-cost comparison: `research/active/babp-finite-seed/students/student-a/recon-001-open-problem-scan.md`.

## Post-meeting audit correction

Independent audit `audits/001-edge-corrector-audit.md` at commit `d1ef2ca` verified the mathematical core and identified three overstatements in the original Meeting 003 wording. They are corrected explicitly here rather than silently erased.

1. **Edge-speed terminology was too strong.** The corrector proves the lower asymptotic velocity bounds

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v,
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le -v
\quad\text{a.s.}
$$

It does not by itself prove that either ratio has a limit. Wherever the original note said "asymptotic edge speed" as if speed existence had been established, read it as the displayed liminf/limsup ballistic-edge conclusion.

2. **The historical identification was stated too confidently.** The accessible Sudbury (1999) record confirms the published `0.0347` finite-seed convergence threshold, hunted-submartingale method, and edge-speed bounds. The full body was not accessible, so literal identity with the present `k=8` LP, normalization, or eight-site encoding is unverified. The exact `k=1` calibration and numerical `k=8` calibration are strong mechanism-level evidence only.

3. **The phrase "strict improvement of the published cutoff" was too broad.** The present result is not yet an improvement of Sudbury's published convergence theorem. It gives a positive finite-window corrector and resulting ballistic-edge bound at `lambda=1/40<0.0347`. Finite-seed convergence at `lambda=1/40` remains conditional on the separate bridge now assigned to Student B.

After this audit, `BABP-EDGE-001` is promoted from `claimed` to `verified` with the narrower wording in `research/claim-registry.md`.

## Professor verification at the meeting

The finite-window LP is mathematically the correct right-edge submartingale problem for BABP.

For a finite nonempty particle configuration `B`, write `R=max B`, encode the first `k` sites behind `R` by `u in {0,1}^k`, retain the next bit `z`, and set

$$
H(B)=R(B)+\phi(u(B)).
$$

A direct generator calculation gives exactly Student B's drift

$$
\begin{aligned}
D_{k,\lambda}(u,z;\phi)
={}&\lambda[1+\phi(T_+u)-\phi(u)]\\
&+u_1[-1+\phi(T_-^zu)-\phi(u)]\\
&+\sum_{j=1}^k n_j^z(u)[\lambda(1-u_j)+u_j]
[\phi(u^{(j)})-\phi(u)].
\end{aligned}
$$

No omitted event changes `H` instantaneously. If this is uniformly at least `v>0`, the martingale decomposition plus bounded local jump rates gives

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v
$$

almost surely, and by reflection

$$
\limsup_{t\to\infty}\frac{L(B_t)}t\le -v
$$

almost surely.

I independently checked the `k=1` algebra. Uniform positive drift is feasible exactly for

$$
\lambda>\frac13.
$$

I also independently implemented the LP from the generator formula, without using Student B's certificate. For `k=8` the zero crossing is numerically `0.0346195435...`; the optimum is negative at `0.0346` and positive at `0.0347`. At `k=10, lambda=0.025` the independently solved LP is also strictly feasible.

The accessible published evidence did not expose Sudbury's internal state encoding. At the meeting I accepted a mechanism-level identification for research-direction purposes because the same exact BABP edge-generator hierarchy gives the old `1/3` cutoff at `k=1`, gives `0.0346195435...` at `k=8`, and Sudbury's paper explicitly combines hunted submartingales with edge-speed bounds and the `0.0347` convergence threshold. The hostile audit has now confirmed that exact historical equivalence remains unverified.

## New project claim

Student B's exact rational certificate at

$$
\lambda=\frac1{40},\qquad k=10
$$

has minimum drift

$$
\frac{1033}{40000000}>0.
$$

The principal independently executed the committed standard-library verifier and reproduced that exact minimum. The Professor independently checked the generator criterion and positive LP feasibility. The fresh hostile audit then independently rederived the generator, decoded and checked all `2048` certificate inequalities, and verified the martingale consequence.

The verified project result is therefore:

> BABP at `lambda=1/40` admits a bounded 10-site right-edge corrector with uniform generator drift at least `1033/40000000`. Consequently every finite nonempty initial configuration satisfies the corresponding right-edge liminf and left-edge limsup ballistic bounds almost surely.

The claim does **not** include existence of limiting edge speeds or finite-seed convergence at `lambda=1/40`.

Claim-registry pointer: `research/claim-registry.md`, entry `BABP-EDGE-001`, status `verified`.

## DFP route

Student B also showed algebraically that the deterministic finite-test self-duality cylinder is not a black-box consequence of DFP quasi-duality: no probability law on the DFP initial set represents it, and the unique finite-window signed representation has total-variation norm growing like a positive exponential in the window size. I checked the one-site algebra and agree. DFP remains available only if a genuinely quantitative estimate beats that coefficient cost; it is no longer the main line.

## Opportunity-cost decision

Graduate Student A's reconnaissance ranked the residual positive-rates/noisy-East problem above provisional BABP **unless** Student B returned a genuinely new small-parameter lemma rather than only rediscovering the old obstruction. That condition was met: Student B found an exact finite-state ballistic-edge certificate below `0.0347` and exposed a concrete analytic programme, namely understanding the finite-window thresholds and the bridge from ballistic edge bounds to convergence.

The noisy-East residual remains an excellent future candidate and has unusually strong principal-specific leverage, but it is not clearly better than a direction that has produced an audited nontrivial mathematical result. I therefore do not pivot.

## Direction decision

**continue — BABP is a committed active programme.**

The proof spine is now substantially sharper:

1. a finite-window right-edge corrector hierarchy gives the historical numerical calibrations `1/3` and `0.0346195435...`;
2. the hierarchy has a verified positive certificate at `lambda=1/40`;
3. the immediate theorem-level gap is whether the verified two-sided ballistic edge bounds, together with the known stationary classification and modern growth inputs, yield finite-seed local convergence without another parameter-dependent hypothesis;
4. if that bridge is clean, the main analytic problem becomes constructing positive-drift finite-window correctors for every `lambda>0`, equivalently proving the finite-window threshold tends to zero.

This is not a duality/cancellation programme. The active mechanism is a finite-state Markov-additive edge corrector.

## Historical provenance decision

Obtaining the full Sudbury paper remains useful because Student B needs the historical bridge to local convergence. It is **not** necessary to establish the mathematics of `BABP-EDGE-001`, which now stands on its own hostile audit. No separate session will be spent solely to prove that Sudbury used literally the same `k=8` LP. The literal historical equivalence is recorded as an open provenance question and should be resolved if the full text is obtained naturally during the bridge reconstruction.

## Next work

Graduate Student B remains the active development student. Assignment `students/student-b/assignment-002.md` is to close the **ballistic-edge-bound-to-convergence bridge**, first at `lambda=1/40`, without assuming that the liminf/limsup bounds alone imply local convergence. If the bridge needs an additional local recurrence/coupling statement, isolate it exactly. Do not yet spend the main effort proving `lambda_k -> 0` until we know what theorem a positive corrector actually buys.

Graduate Student A is idle. The independent auditor has completed its task.
