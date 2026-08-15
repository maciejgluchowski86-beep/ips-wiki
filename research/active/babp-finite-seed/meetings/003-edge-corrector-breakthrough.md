# Group meeting 003: edge-corrector breakthrough

Date: 2026-08-15

Professor review of Graduate Student B assignment 001 and Graduate Student A opportunity-cost reconnaissance.

state_narrowed: yes

Evidence pointer: `research/active/babp-finite-seed/students/student-b/001-threshold-and-dfp.md`, `research/active/babp-finite-seed/students/student-b/edge-corrector-certificate.py`, and the Professor's independent check `research/active/babp-finite-seed/notes/professor-edge-corrector-verification.md`. Opportunity-cost comparison: `research/active/babp-finite-seed/students/student-a/recon-001-open-problem-scan.md`.

## Professor verification

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

almost surely, and by reflection the left edge has strictly negative outward speed.

I independently checked the `k=1` algebra. Uniform positive drift is feasible exactly for

$$
\lambda>\frac13.
$$

I also independently implemented the LP from the generator formula, without using Student B's certificate. For `k=8` the zero crossing is numerically `0.0346195435...`; the optimum is negative at `0.0346` and positive at `0.0347`. At `k=10, lambda=0.025` the independently solved LP is also strictly feasible.

The accessible published evidence does not expose Sudbury's internal state encoding, so I do not claim to have verified line by line that his 1999 calculation is literally this `k=8` LP. But the calibration is much stronger than a coincidental nearby number: the same exact BABP edge-generator hierarchy gives the old `1/3` cutoff at `k=1`, then gives `0.0346195435...` at `k=8`, while Sudbury's paper is explicitly about hunting submartingales, extends the theorem to `0.0347`, and states that it obtains edge-speed bounds. I accept the identification of the historical threshold mechanism for research-direction purposes. Exact historical equivalence is included in the independent-audit request.

## New project claim

Student B's exact rational certificate at

$$
\lambda=\frac1{40},\qquad k=10
$$

has minimum drift

$$
\frac{1033}{40000000}>0.
$$

The principal independently executed the committed standard-library verifier and reproduced that exact minimum. The Professor has independently checked the generator criterion and obtained positive feasibility at the same parameter with a separately written LP.

I therefore accept the following as a **claimed project result pending independent audit**:

> BABP at `lambda=1/40` admits a bounded 10-site right-edge corrector with uniform strictly positive generator drift, hence strictly positive outward asymptotic edge speeds.

Since `1/40=0.025<0.0347`, this strictly improves the finite-window edge-submartingale/edge-speed certificate beyond the historical published cutoff associated with Sudbury's theorem.

The claim does **not** currently include finite-seed convergence at `lambda=1/40`. The bridge from positive edge speed to local convergence remains unresolved in this workspace.

Claim-registry pointer: `research/claim-registry.md`, entry `BABP-EDGE-001`, status `claimed`.

## DFP route

Student B also showed algebraically that the deterministic finite-test self-duality cylinder is not a black-box consequence of DFP quasi-duality: no probability law on the DFP initial set represents it, and the unique finite-window signed representation has total-variation norm growing like a positive exponential in the window size. I checked the one-site algebra and agree. DFP remains available only if a genuinely quantitative estimate beats that coefficient cost; it is no longer the main line.

## Opportunity-cost decision

Graduate Student A's reconnaissance ranked the residual positive-rates/noisy-East problem above provisional BABP **unless** Student B returned a genuinely new small-parameter lemma rather than only rediscovering the old obstruction. That condition has now been met more strongly than anticipated: Student B found an exact finite-state certificate below the historical numerical cutoff and exposed a concrete analytic programme, namely understanding the finite-window thresholds and the bridge from edge speed to convergence.

The noisy-East residual remains an excellent future candidate and has unusually strong principal-specific leverage, but at this meeting it is not clearly better than a direction that has just produced a nontrivial new mathematical datum. I therefore do not pivot.

## Direction decision

**continue — BABP graduates from provisional to committed active programme.**

The proof spine is now substantially sharper:

1. the historical numerical obstruction is a finite-window right-edge corrector problem;
2. that obstruction can already be pushed below the published `0.0347` cutoff;
3. the immediate theorem-level gap is whether positive two-sided edge speed, together with the known stationary classification and modern growth inputs, yields finite-seed local convergence without another parameter-dependent hypothesis;
4. if the bridge is clean, the main analytic problem becomes constructing positive-drift finite-window correctors for every `lambda>0`, equivalently proving the finite-window threshold tends to zero.

This is not a duality/cancellation programme. The active mechanism is a finite-state Markov-additive edge corrector.

## Audit decision

This is the right moment to pay for a fresh independent auditor. A single finite-state generator/certificate calculation currently carries the strategy, and an error in the event enumeration would invalidate the apparent breakthrough.

The auditor should independently check:

- the BABP generator convention and the exact edge-corrector drift formula;
- the positive-drift-to-edge-speed implication;
- the `k=1` threshold;
- the exact `k=10, lambda=1/40` certificate;
- an independent `k=8` calibration;
- and, as a separate literature question, how strongly the accessible 1999 source supports identification with Sudbury's published `0.0347` mechanism.

Audit request: `audits/001-edge-corrector-request.md`.

Until that audit returns, `BABP-EDGE-001` remains `claimed`, not `verified`.

## Next work

Graduate Student B remains the active development student. The next assignment is to close the **edge-speed-to-convergence bridge**, first at `lambda=1/40`, without assuming that positive edge speed alone is enough. If the bridge needs an additional local recurrence/coupling statement, isolate it exactly. Do not yet spend the main effort proving `lambda_k -> 0` until we know what theorem a positive corrector actually buys.

Graduate Student A becomes idle after completing the reconnaissance. The fresh independent auditor occupies the second in-flight session slot alongside Student B.

Next assignment: `students/student-b/assignment-002.md`.
