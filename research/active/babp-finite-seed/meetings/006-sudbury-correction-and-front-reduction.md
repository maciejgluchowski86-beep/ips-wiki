# Group meeting 006: Sudbury provenance correction and the invariant-front bottleneck

Date: 2026-08-15

Professor review of:

- Graduate Student A, `students/student-a/writeup-001-literature-and-manuscript-plan.md`, commits `0239d37` and `87d59d8`;
- the full text of Aidan Sudbury (1999), *Hunting submartingales in the jumping voter model and the biased annihilating branching process*, especially Section 3, Table 2, Lemmas 5 and 7, and Theorem 7;
- Graduate Student B, `students/student-b/003-front-gap.md`, commits `5c357ef` and `1365840`.

state_narrowed: yes

Evidence pointer: the Student A source comparison above; Sudbury (1999), pp. 847--852, especially the Maxwell's-demon construction, Lemma 5, Table 2, Lemma 7, and the paragraph immediately before Theorem 7; and Student B's `003-front-gap.md`.

## Source-verified correction to Meetings 003--005

The project previously had incomplete access to Sudbury (1999). That caused two novelty/provenance statements to be too strong. The full paper now resolves both.

First, the historical finite-window identification is exact, not merely a numerical calibration. Sudbury uses the same BABP normalization as the project,

$$
0\to1\text{ at rate }\lambda N_x,
\qquad
1\to0\text{ at rate }N_x.
$$

He follows the leftmost particle and records the `m` sites immediately to its right. Reflecting space identifies his window size `m` with the project `k`, his `m`-block with the edge word `u`, and the one site just beyond the window with the project exterior bit `z`. His correction values `S_i` are the project corrector `phi` up to this reflection. His corrected local gain

$$
a_i+\sum_j q_{ij}(S_j-S_i)
$$

is the project finite-window drift `D_{k,lambda}(u,z;phi)`.

The Maxwell's-demon equivalence is exact at the robust-condition level. Sudbury allows the exterior end-value to be chosen as a function of the current `m`-block state. An assignment of end-values is therefore a map from block states to `{0,1}`. Lemma 5 requires one correction vector to give a submartingale for **every** such assignment. The drift in row `i` depends only on the single end-value assigned to row `i`; hence requiring the inequality for every assignment is equivalent to requiring it for both possible end-values separately in every state. After reflection this is exactly the project's statewise requirement over both `z=0,1`.

Second, Sudbury's Lemma 7 really does give free extension in window size at fixed `lambda`: if a suitable submartingale exists for `m=m_1`, use the same correction on the first `m_1` sites of every larger `m_2` configuration. Since the `m_1` construction already works whatever the next end-value is, the extra sites do not spoil the submartingale. This is the historical counterpart of the project's exact window-nesting lemma.

Sudbury's Table 2 reports

```text
m    lambda_m
2    0.2653
3    0.1832
4    0.1154
5    0.0805
6    0.0589
7    0.0443
8    0.0347
```

and explicitly describes these as trial-and-error values rather than proved exact critical parameters. The project value `0.0346195434755...` is therefore a refinement of Sudbury's own eight-site boundary, not a merely similar number.

## Novelty correction

The theorem-level implication recorded as `BABP-CONV-001` is mathematically correct but is not a new general criterion.

Immediately before Theorem 7, Sudbury states that Neuhauser--Sudbury (1993) used the existence of a suitable submartingale in the stationary-state argument, that Section 3 of the 1999 paper extends this condition from `lambda>1/3` to `lambda>0.0347`, and that the argument of Neuhauser--Sudbury Section 5 then proceeds unchanged. Theorem 7 is the resulting finite-seed convergence theorem.

Thus the following language from the earlier project record was overstated and is superseded by this meeting:

- Meeting 004's description of the corrector-to-convergence implication as a "central new theorem";
- Meeting 005's framing of `BABP-CONV-001` as the programme's novel theorem-level contribution;
- the earlier claim-registry/results wording that left publication-level priority of the general implication open rather than recognizing it as prior art;
- Meeting 003's statement that literal identity of the `k=8` mechanism with Sudbury was unverified.

The corrected contribution is:

1. Sudbury's finite-window robust submartingale mechanism is classical and applies for arbitrary fixed window size.
2. The project supplies an independently audited exact rational ten-site certificate at
   $$
   \lambda=\frac1{40}
   $$
   with minimum drift
   $$
   \frac{1033}{40000000}>0.
   $$
3. Combining that certificate with the classical convergence implication gives finite-seed convergence at `lambda=1/40`, a strict extension below Sudbury's published `0.0347` range inside his mechanism.
4. The project also supplies a self-contained tagged-internal-gap proof of the implication. No novelty claim is made for that proof architecture until Neuhauser--Sudbury (1993), Section 5, is inspected.

`BABP-EDGE-001` is unaffected mathematically. Its provenance is now stronger: the finite-window mechanism and the historical `m=8` comparison are source-verified, while the exact `k=10`, `lambda=1/40` rational certificate remains a genuine new project datum.

`BABP-CONV-001` remains `verified` because the correction is about novelty, not correctness. Its registry entry now explicitly labels the implication classical.

## Student B's E5 reduction

The novelty correction lowers the value of stopping at `lambda=1/40`, but Student B's new work materially strengthens the case for continuing toward all parameters.

I checked the core of `003-front-gap.md` for proof-spine use. For fixed `lambda>0`, the infinite right-front process on `{0,1}^N` is Feller; the local half-line generator has cylinder functions as a core, and the frame-shift part is a bounded perturbation. Finite-dimensional LP duality and compactness then give the exact fixed-parameter reduction

$$
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}\mu(\lambda-u_1).
$$

The reverse compactness step is not contaminated by arbitrary tail extensions: for a cylinder depending on the first `ell` coordinates, once `k>=ell+1`, its front generator depends only on coordinates already contained in the finite marginal and is independent of the exterior control. The cylinder-core argument then upgrades infinitesimal stationarity to invariance.

Stationarity of the first front bit gives

$$
\mu(\lambda-u_1)
=
\frac{\lambda}{1+\lambda}
\left(\lambda-\frac12\mu(01)\right),
$$

so the exact finite-window target is

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda.
$$

Student B also proves an important separation: every Cesaro invariant front law selected from the singleton has strictly positive current for every `lambda>0`, using the all-parameter finite-seed cardinality growth theorem plus reflection symmetry. Therefore a failure of the finite-window programme could occur only through an additional invariant semi-infinite-tail phase not selected from finite seeds. The nearest-gap-only corrector no-go recovers the `1/3` obstruction, confirming that genuinely deeper front correlations are needed.

This is a real narrowing. The current obstruction is no longer "make the finite LP work at small lambda". It is a phase-selection problem for the infinite front.

## Opportunity-cost decision

**continue**, but with the scientific payoff redefined.

The `lambda=1/40` result is a range extension inside Sudbury's method, not a new mechanism or new general convergence principle. That materially lowers its standalone novelty relative to what Meeting 005 believed.

I nevertheless keep BABP as the active direction for the next substantial block because the all-parameter target remains genuinely open and Student B has just reduced the finite-window route to a sharply stated invariant-front obstruction. In particular, the physical front already has positive current for every parameter; the only remaining issue is whether a hostile invariant semi-infinite-tail phase exists. This is substantially more localized than the problem at Meeting 005 and is a qualitatively different theorem question from merely increasing the LP window.

The next block is not open-ended. If the hostile-phase/uniqueness attack produces no theorem-level narrowing, the next group meeting should explicitly re-run the opportunity-cost comparison against Student A's noisy-East reserve rather than continue numerical windows by inertia.

## Neuhauser--Sudbury (1993), Section 5

It is worth obtaining and inspecting the full Section 5 if the principal can provide it. This is now a **publication/attribution** question, not a mathematical dependency of the range extension or the all-parameter programme. It will settle whether the project's tagged-gap nonescape proof is merely a modern reproof of the same local mechanism or a genuinely different proof architecture.

Do not spend a new independent research session solely acquiring it. If the principal supplies the text, Student A or the Professor should perform the bounded comparison and update the manuscript attribution.

## Wiki and stable surface

The live-wiki freeze should remain in force. The prior-art correction makes immediate `proved here` wiki language especially inappropriate until the research note is reframed around the exact range certificate and the all-parameter question.

The stable `main` surface must be corrected now because the claim registry, theorem note, and project state currently carry the stronger novelty framing. The mathematical verification statuses remain unchanged.

## Next work

Graduate Student B remains the active development student. The next assignment is `students/student-b/assignment-004.md`, aimed at proving or refuting exclusion of hostile invariant front phases, with front uniqueness as one sufficient route but not a mandatory formulation.

Graduate Student A becomes idle after completing the full-text literature comparison. If Neuhauser--Sudbury (1993), Section 5, is supplied, A may perform a bounded source comparison without reopening a second scientific direction.
