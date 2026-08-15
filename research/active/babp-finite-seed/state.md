# Programme state

## Direction

Title: 1D BABP from a finite seed

Branch: `research/babp-finite-seed`

Professor lineage: persistent ChatGPT Professor

Active graduate-student lineage: Graduate Student B (to be created)

Workspace: `research/active/babp-finite-seed/`

Latest group meeting: none yet

## Target

Consider the one-dimensional biased annihilating branching process (BABP) with branching parameter `lambda>0`, started from a finite nonempty particle set `B` (begin with `B={0}`). Prove local convergence to its nontrivial Bernoulli product equilibrium law of particle density

$$
q=\frac{\lambda}{1+\lambda}.
$$

Equivalently, remove the remaining small-parameter restriction in the classical finite-seed convergence theorem.

## Why this target

This is an established open finite-seed problem with substantially more structure than the closed FA-1f direction.

Neuhauser--Sudbury proved the basic stationary-law structure for BABP. Finite-seed convergence was known for `lambda>1/3` and Sudbury improved the threshold to `lambda>0.0347`. Martinelli--Shapira--Toninelli (2025), Remark 5.4, records this as the current finite-seed convergence range while proving new all-parameter facts: exponential ergodicity of the double-flipping process (DFP), BABP self-duality/quasi-duality consequences, linear growth from every finite nonempty seed, and exponential convergence from Bernoulli product initial laws.

The canonical patch paper also identifies BABP from a finite nonempty particle set as an unresolved hard-model convergence problem and proves patch positivity with threshold equal to equilibrium density.

Unlike the closed FA-1f programme, the immediate task is not to discover basic geometry. BABP already has exact self-duality and quasi-duality with DFP, and the 2025 paper supplies a strong all-parameter mixing theorem for DFP. The research question is whether those ingredients can be sharpened or recombined to close the finite-seed gap.

## Main obstruction

For finite initial `B`, BABP self-duality gives the convergence criterion that for every finite test set `B'`,

$$
\mathbf E_B\left[\left(-\frac1\lambda\right)^{|B(t)\cap B'|}\right]\longrightarrow 0.
$$

For small `lambda`, the kernel has magnitude larger than one whenever the finite intersection is nonempty, so global growth of `|B(t)|` does not directly control this local signed observable. The known finite-seed proofs use additional one-dimensional structure and currently stop at a positive threshold.

The 2025 quasi-duality with DFP controls different multiplicative weights and proves all-parameter exponential mixing for DFP. It is not yet clear whether one can represent or approximate the finite-test self-duality observable by DFP-controlled observables with uniform coefficients in the small-`lambda` regime.

## Present approach

Do **not** start by repeating local patch-weight contraction. The FA closure showed why a conservative positive transform can hide behind such decompositions, and for BABP the classical duality algebra is already known.

The first line is to audit the exact interface between:

1. the classical finite-seed convergence proofs and the numerical threshold `0.0347`;
2. BABP self-duality;
3. BABP--DFP quasi-duality/thinning;
4. the 2025 all-parameter DFP exponential-ergodicity theorem and BABP linear-growth theorem.

The aim is to isolate the smallest new lemma which, if proved, would remove the threshold.

## Proof spine

Path: `proof-spine.md`.

Current bottleneck: identify whether the modern DFP/quasi-duality machinery gives a genuinely new route to the finite-test self-duality observable, or whether the old threshold obstruction survives unchanged.

## Mathematical state

### Established from literature/canonical sources

- BABP has Bernoulli product equilibrium with particle density `lambda/(1+lambda)`.
- Classical BABP self-duality and BABP--DFP quasi-duality are available.
- Finite-seed convergence is known for `lambda>0.0347`.
- Martinelli--Shapira--Toninelli (2025) prove exponential ergodicity of DFP for every `lambda>0` and derive linear growth of BABP from finite nonempty seeds for every `lambda>0`.
- The canonical patch paper proves BABP patch positivity and identifies finite-seed convergence as unresolved for part of the parameter range.

These are external/canonical inputs, not new project claims.

### Open

- The exact load-bearing inequality or probabilistic event responsible for the `0.0347` threshold in the best classical proof.
- Whether DFP exponential ergodicity can control the finite-test BABP self-duality observable for deterministic finite seeds.
- Whether a thinning/quasi-duality representation exists with coefficients that remain stable as `lambda` becomes small.
- If not, what genuinely new one-dimensional lemma is needed.

## Strongest positive evidence

The target already has a nearly complete structural toolkit: exact dualities, all-parameter linear growth, all-parameter exponential mixing for the auxiliary DFP, and a historical finite-seed theorem covering all but a small parameter interval. This is materially more focused than the FA-1f target after its two failed reductions.

## Strongest negative evidence

The finite-seed gap has survived since 1999 despite strong algebraic dualities. The small-`lambda` self-duality weight is large and sign-changing, so naive use of growth or absolute values is badly conditioned. The 2025 authors had the DFP theorem in hand and still did not close finite-seed convergence, which is evidence that a nontrivial obstruction remains.

## Current assignment

Graduate Student B will reconstruct the best finite-seed proof, locate the threshold exactly, and test whether the 2025 DFP/quasi-duality machinery changes that obstruction. Exact assignment: `students/student-b/assignment-001.md`.

## Research delta

Latest meeting `state_narrowed`: not applicable; no group meeting yet.

Consecutive no-narrowing meetings: 0

Stagnation consultation: none.
