# Graduate Student B assignment 003: invariant front law and the all-parameter gap

Work on branch `research/babp-finite-seed`.

Read first:

- `project-state.md`;
- `research/active/babp-finite-seed/state.md`;
- `research/active/babp-finite-seed/proof-spine.md`;
- `research/active/babp-finite-seed/meetings/005-convergence-promotion.md`;
- `research/results/babp-finite-seed-convergence.md`;
- your `002-edge-environment-dual.md`, commit `b9fdc55`;
- your `001-edge-corrector-monotonicity.md`.

`BABP-CONV-001` is now verified. Do not rework the convergence bridge unless the present assignment exposes a genuine dependency error. The remaining scientific target is finite-seed convergence for every `lambda>0`.

## First responsibility: validate the infinite-front reduction

Do not take `002-edge-environment-dual.md` as established merely because the Professor found its core plausible for proof-spine use. Recheck it from first principles and repair anything needed.

For fixed `lambda>0`, write

$$
v_k(\lambda)=\sup_\phi\min_{u,z}D_{k,\lambda}(u,z;\phi).
$$

Let `Q_infinity` be the environment seen from the right edge and `I_lambda` its invariant probability measures. Establish rigorously, or refute, the proposed identity

$$
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}
\int(\lambda-u_1)\,d\mu.
$$

In particular check:

1. the infinite-front process is well-defined and Feller on `{0,1}^N`;
2. `I_lambda` is nonempty;
3. the finite LP dual really is the stated stationary occupation-measure problem;
4. the projection of an invariant infinite-front law gives a feasible finite dual measure;
5. in the reverse compactness argument, arbitrary extensions of finite marginals do not contaminate the cylinder-generator calculation;
6. stationarity on cylinder functions is enough to identify an invariant probability law for `Q_infinity`;
7. there is no missing boundary control or closure condition in the limit.

Write the corrected theorem with all hypotheses that are actually needed.

## Parameter-threshold caution

Do **not** use the shorthand equivalence

```text
lambda_k -> 0
```

as though it were already interchangeable with “for every fixed `lambda>0`, some finite `k` has `v_k(lambda)>0`.” Window monotonicity

$$
v_{k+1}(\lambda)\ge v_k(\lambda)
$$

is proved. Monotonicity or interval structure in the parameter `lambda` has not been proved. If you want to recover the threshold formulation, prove the relevant parameter monotonicity separately. Otherwise work directly at each fixed `lambda`.

## Second responsibility: derive and attack the front-gap lemma

Assuming the infinite-front reduction is correct, independently rederive the first-bit stationary balance. The proposed identity is

$$
\mu(u_1=1)
=
\frac{\lambda}{1+\lambda}
\left(1+\frac12\mu(u_1=0,u_2=1)\right).
$$

Hence the direct target is

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda
\qquad\text{for every fixed }\lambda>0.
$$

Call this the FRONT-GAP LEMMA only after the reduction has been checked.

Attack it rather than merely restating it. Suitable directions include, but are not limited to:

- derive the stationary balance hierarchy for `01`, `001`, `011`, gap length, and distance to the next particle;
- identify a Lyapunov function for the front environment whose stationary identity forces a strict deficit from `2lambda`;
- seek a regenerative description from edge births/deaths;
- prove uniqueness of the invariant front law plus positive mean front drift, if this can be done without circularly importing the desired result;
- compare the front law with a simpler birth--death or renewal process in a direction strong enough to control `mu(01)`;
- test whether the bound can fail by constructing approximate invariant laws concentrated on sparse fronts;
- use finite-state truncations/LP dual optimizers as diagnostics, but do not promote a numerical pattern without an analytic mechanism.

A useful negative result is also valuable: if there is an invariant front law with zero/nonpositive mean drift, or if the proposed finite-window-to-front dual fails, establish that sharply.

## Cheap checks before long development

For small symbolic windows and/or finite front truncations:

- compute stationary equations exactly where possible;
- inspect the dual optimizer responsible for the smallest drift;
- determine whether `mu(01)/(2lambda)` appears to approach one and at what scale;
- identify which local patterns carry the deficit.

Use computation to formulate a proof mechanism, not as a substitute for one.

## Durable output

Commit the decisive work to

`research/active/babp-finite-seed/students/student-b/003-front-gap.md`

with auxiliary code in the same directory if useful.

End with a short handoff stating one of:

- `front reduction verified; front-gap lemma proved`, with the all-parameter consequence;
- `front reduction verified; front-gap lemma reduced to Lemma X`, stating Lemma X precisely;
- `front reduction corrected`, with the exact corrected target;
- `front route refuted`, with the first fatal point.

Do not make a new all-parameter convergence claim unless the full chain from the verified convergence criterion through the front estimate is proved.