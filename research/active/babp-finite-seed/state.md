# Programme state

## Direction

Title: 1D BABP from a finite seed

Branch: `research/babp-finite-seed`

Professor lineage: persistent ChatGPT Professor

Active graduate-student lineage: Graduate Student B (to be created for BABP); Graduate Student A may concurrently perform bounded target-selection reconnaissance

Workspace: `research/active/babp-finite-seed/`

Latest group meeting: none yet

## Target

Consider the one-dimensional biased annihilating branching process (BABP) with branching parameter `lambda>0`, started from a finite nonempty particle set `B` (begin with `B={0}`). Prove local convergence to its nontrivial Bernoulli product equilibrium law of particle density

$$
q=\frac{\lambda}{1+\lambda}.
$$

Equivalently, remove the remaining small-parameter restriction in the classical finite-seed convergence theorem.

BABP is the current working target, not an irreversible commitment. The Professor will compare it against a bounded reconnaissance of recent high-quality open-problem/progress literature before investing deeply beyond the first obstruction audit.

## Why this target

This is an established open finite-seed problem with substantially more structure than the closed FA-1f direction.

Neuhauser--Sudbury proved the basic stationary-law structure for BABP. Finite-seed convergence was known for `lambda>1/3` and Sudbury improved the threshold to `lambda>0.0347`. Martinelli--Shapira--Toninelli (2025), Remark 5.4, records this as the current finite-seed convergence range while proving new all-parameter facts: exponential ergodicity of the double-flipping process (DFP), BABP self-duality/quasi-duality consequences, linear growth from every finite nonempty seed, and exponential convergence from Bernoulli product initial laws.

The canonical patch paper also identifies BABP from a finite nonempty particle set as an unresolved hard-model convergence problem and proves patch positivity with threshold equal to equilibrium density.

Unlike the closed FA-1f programme, the immediate task is not to discover basic geometry. BABP already has exact self-duality and quasi-duality with DFP, and the 2025 paper supplies a strong all-parameter mixing theorem for DFP. The research question is whether those ingredients can be sharpened or recombined to close the finite-seed gap.

However, the principal has now supplied additional opportunity-cost evidence: extensive prior ChatGPT work on the neighboring 1D FA-1f off-equilibrium problem did not yield results, and cancellation/duality is explicitly not a required organizing method. Accordingly BABP is being pursued because of its sharply localized historical gap and new auxiliary results, not because it is another duality problem. If the first obstruction audit shows that the 2025 inputs do not materially change the old threshold mechanism, the Professor will compare BABP immediately against the reconnaissance pool rather than manufacture another duality variant.

## Main obstruction

For finite initial `B`, BABP self-duality gives the convergence criterion that for every finite test set `B'`,

$$
\mathbf E_B\left[\left(-\frac1\lambda\right)^{|B(t)\cap B'|}\right]\longrightarrow 0.
$$

For small `lambda`, the kernel has magnitude larger than one whenever the finite intersection is nonempty, so global growth of `|B(t)|` does not directly control this local signed observable. The known finite-seed proofs use additional one-dimensional structure and currently stop at a positive threshold.

The 2025 quasi-duality with DFP controls different multiplicative weights and proves all-parameter exponential mixing for DFP. It is not yet clear whether one can represent or approximate the finite-test self-duality observable by DFP-controlled observables with uniform coefficients in the small-`lambda` regime.

## Present approach

Do **not** start by repeating local patch-weight contraction. The FA closure showed why a conservative positive transform can hide behind such decompositions, and for BABP the classical duality algebra is already known.

The first BABP line is an obstruction audit of the exact interface between:

1. the classical finite-seed convergence proofs and the numerical threshold `0.0347`;
2. BABP self-duality;
3. BABP--DFP quasi-duality/thinning;
4. the 2025 all-parameter DFP exponential-ergodicity theorem and BABP linear-growth theorem.

The aim is to isolate the smallest new lemma which, if proved, would remove the threshold. Duality is a diagnostic starting point because it is where the existing theorem is formulated; it is not a binding method. If the missing lemma is spatial, coupling-based, spectral, renewal-based, or otherwise non-dual, Student B should follow the mathematics.

Concurrently, Graduate Student A may perform a bounded opportunity-cost reconnaissance across recent serious progress/survey papers with explicit open problems. That task is target selection, not a second active scientific programme. It should return a small ranked set of concrete problems with exact open-status evidence, successor checks, and a tractability argument for this group.

## Proof spine

Path: `proof-spine.md`.

Current bottleneck: identify whether the modern DFP/quasi-duality machinery or the historical proof structure yields a genuinely tractable missing lemma for finite-seed BABP, while bounded reconnaissance tests whether BABP remains the best available target.

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
- Whether a different open problem identified in current progress/survey literature has materially higher expected value for this group.

## Strongest positive evidence

The target already has a nearly complete structural toolkit: exact dualities, all-parameter linear growth, all-parameter exponential mixing for the auxiliary DFP, and a historical finite-seed theorem covering all but a small parameter interval. This is materially more focused than the FA-1f target after its two failed reductions.

## Strongest negative evidence

The finite-seed gap has survived since 1999 despite strong algebraic dualities. The small-`lambda` self-duality weight is large and sign-changing, so naive use of growth or absolute values is badly conditioned. The 2025 authors had the DFP theorem in hand and still did not close finite-seed convergence, which is evidence that a nontrivial obstruction remains. More broadly, the principal's prior unsuccessful FA-1f effort is evidence against overinvesting in neighboring off-equilibrium KCM problems merely because they fit existing project machinery.

## Current assignments

Graduate Student B: reconstruct the best finite-seed BABP proof, locate the threshold exactly, and test whether the 2025 DFP/quasi-duality machinery changes that obstruction. Exact assignment: `students/student-b/assignment-001.md`.

Graduate Student A: bounded opportunity-cost reconnaissance across recent high-quality open-problem/progress literature, returning a small ranked candidate set and explicit comparison with BABP. Exact assignment: `students/student-a/assignment-recon-001.md`.

## Research delta

Latest meeting `state_narrowed`: not applicable; no BABP group meeting yet.

Consecutive no-narrowing meetings: 0

Stagnation consultation: none.
