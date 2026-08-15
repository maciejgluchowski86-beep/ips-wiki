# Proof spine

## Main target

For one-dimensional BABP with branching parameter `lambda>0`, started from any finite nonempty particle set `B`, prove local convergence to Bernoulli equilibrium `pi` with particle density

$$
q=\frac{\lambda}{1+\lambda}.
$$

Begin with `B={0}`. The programme is committed after Meeting 003 because the finite-window edge method produced an independently audited nontrivial certificate at `lambda=1/40`.

## E0. Finite-test convergence criterion

BABP self-duality gives, for finite `T`,

$$
\mathbf E_B\left[\left(-\frac1\lambda\right)^{|B(t)\cap T|}\right]
=
\mathbf E_T\left[\left(-\frac1\lambda\right)^{|T(t)\cap B|}\right].
$$

The functions indexed by subsets of a fixed finite window form a basis of local observables, and Bernoulli equilibrium has zero expectation for every nonempty such duality function. Hence decay of these finite-test observables implies local convergence.

**Status:** established external input; independently rederived by Student B.

## E1. Existing all-parameter literature inputs

For every `lambda>0` the current literature supplies:

- the one-dimensional stationary-law classification needed for finite-seed convergence arguments;
- exponential ergodicity of DFP on local observables;
- linear growth of BABP cardinality from finite nonempty seeds;
- exponential convergence from Bernoulli product initial laws.

**Status:** established external input.

## E2. Finite-window right-edge corrector

For a finite nonempty BABP configuration `B`, let `R=max B`. Encode the first `k` sites behind `R` by `u in {0,1}^k` and the next unresolved bit by `z`. For bounded `phi:{0,1}^k -> R`, put

$$
H(B)=R(B)+\phi(u(B)).
$$

The exact generator drift is

$$
\begin{aligned}
D_{k,\lambda}(u,z;\phi)
={}&\lambda[1+\phi(T_+u)-\phi(u)]\\
&+u_1[-1+\phi(T_-^zu)-\phi(u)]\\
&+\sum_{j=1}^k n_j^z(u)[\lambda(1-u_j)+u_j]
[\phi(u^{(j)})-\phi(u)].
\end{aligned}
$$

If `D>=v>0` uniformly, then for every finite nonempty initial configuration

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v
\qquad\text{a.s.},
$$

and by reflection

$$
\limsup_{t\to\infty}\frac{L(B_t)}t\le -v
\qquad\text{a.s.}
$$

The corrector argument does **not** by itself prove existence of limits `R(B_t)/t` or `L(B_t)/t`.

**Status:** verified by fresh independent hostile audit.

**Calibration:**

- `k=1`: strict feasibility iff `lambda>1/3`, analytically;
- `k=8`: independently reproduced numerical zero-drift threshold `0.0346195434755...`, with sign change between `0.03461954` and `0.03461955`;
- `k=10`, `lambda=1/40`: exact rational certificate with minimum drift

$$
\frac{1033}{40000000}>0.
$$

**Project claim:** `BABP-EDGE-001`, status `verified` in `research/claim-registry.md`.

**Decisive pointers:**

- `students/student-b/001-threshold-and-dfp.md`;
- `students/student-b/edge-corrector-certificate.py`;
- `notes/professor-edge-corrector-verification.md`;
- `audits/001-edge-corrector-audit.md`, commit `d1ef2ca`.

**Historical qualification.** The accessible Sudbury (1999) record confirms the published `0.0347` finite-seed convergence threshold, hunted-submartingale method, and edge-speed bounds. The full paper body was not accessible. Therefore the numerical `k=8` calibration is strong mechanism-level evidence but literal identity with Sudbury's LP, normalization, or an eight-site state encoding is unverified. The present verified claim stands independently of that provenance question.

## E3. DFP as a black-box route to finite-test observables

Let `y=sqrt(1+lambda)` and use the BABP--DFP quasi-duality one-site factors

$$
a=\frac1{y+1},\qquad b=-\frac1{y-1}.
$$

Student B showed, and the Professor checked the one-site algebra, that a deterministic finite-test self-duality cylinder cannot be represented by a probability law on DFP initial sets. On a finite ambient window the unique signed representation has total-variation norm growing like

$$
y^{|V\setminus T|}.
$$

Thus DFP exponential ergodicity is not a black-box solution; it would need a quantitative exponent beating this coefficient growth or a different spatial argument.

**Status:** algebraic obstruction verified for present use; DFP demoted to secondary route.

## E4. Ballistic edge bounds to local convergence

This is the **current first unresolved theorem-level edge**.

Determine whether the verified two-sided lower-asymptotic-velocity bounds, together with the known invariant-law classification and all-parameter growth information, are sufficient to imply finite-seed local convergence.

The immediate test parameter is

$$
\lambda=\frac1{40}.
$$

A valid proof must separate:

1. invariance of subsequential local weak limits;
2. classification of invariant limits as mixtures of the empty state and Bernoulli equilibrium;
3. exclusion of the empty component.

The ballistic hull bounds do not by themselves visibly imply item 3, so no downstream convergence claim is allowed until this bridge is established.

**Status:** open.

**Owner:** Graduate Student B, assignment `students/student-b/assignment-002.md`.

**If proved with no second parameter restriction:** `BABP-EDGE-001` immediately supplies the missing edge input at `lambda=1/40`, yielding a genuine finite-seed convergence theorem below the published `0.0347` convergence threshold. That theorem has not yet been proved.

## E5. Remove the finite-window edge threshold

For fixed `k`, define

$$
v_k(\lambda)=\sup_\phi\min_{u,z}D_{k,\lambda}(u,z;\phi)
$$

and

$$
\lambda_k=\inf\{\lambda>0:v_k(\lambda)>0\}.
$$

The computed values decrease sharply through `k=10`. The all-parameter target would follow from this route if E4 is sufficient and one proves

$$
\lambda_k\longrightarrow0,
$$

or otherwise constructs, for every fixed `lambda>0`, some finite `k` and bounded corrector with positive drift.

Possible analytic interpretations include a Poisson equation or hitting-time corrector for the environment seen from the edge, but no such representation is yet established.

**Status:** open, downstream of E4.

## H1. Historical provenance question

The exact relation between the present `k=8` LP and Sudbury's internal 1999 calculation is not source-verified because the full paper body was inaccessible to Student B and the independent auditor.

This question is **not load-bearing for E2**: `BABP-EDGE-001` has an independent proof and hostile audit. It is useful mainly for understanding the historical bridge E4. Student B should continue to seek the full proof as part of assignment 002. No separate research session will be spent solely to establish that Sudbury literally used the same eight-site LP.

**Status:** open provenance question, secondary to E4.

## O1. Opportunity-cost comparison

Graduate Student A's reconnaissance ranked the residual simple-IPS positive-rates/noisy-East problem above provisional BABP unless Student B found a genuinely new small-parameter lemma. Student B did: the exact `lambda=1/40` edge certificate is now independently audited and yields the concrete E4/E5 programme above.

Therefore BABP remains the next substantial investment. The noisy-East residual remains the strongest identified future candidate if BABP's bridge fails or the finite-window thresholds prove analytically sterile.

**Status:** bounded reconnaissance complete; Student A idle.

## Current first unresolved edge

**E4: establish or refute the ballistic-edge-bound-to-local-convergence bridge, first at `lambda=1/40`.**

Do not spend the main effort on `lambda_k -> 0` until the group knows that a positive finite-window corrector buys the convergence theorem or knows the exact extra lemma required.

## Routes demoted or excluded

- DFP change-of-basis as a black-box finite-seed solution: demoted by the coefficient-norm obstruction.
- Local patch-weight contraction: not an active route; BABP already has more direct finite-state edge structure.
- Closed FA-1f sibling-cancellation and related closed programmes remain closed.
- Do not infer local convergence from cardinality growth or hull expansion alone.

## Revision note

Independent audit 001 verified the generator, exact certificate, martingale consequence, `k=1` calibration, and numerical `k=8` crossing. It corrected three overstatements from Meeting 003: the certificate gives liminf/limsup ballistic bounds rather than speed-limit existence; literal historical `k=8` identity is unverified; and no improvement of Sudbury's published convergence theorem has yet been proved. `BABP-EDGE-001` is now `verified` with this narrower boundary.
