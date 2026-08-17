---
method_id: survival-conditioned-renewal-multitype-contact
title: Survival-conditioned renewal points for complete convergence
category: lyapunov-regeneration
targets:
  - convergence
model_scope: Asymmetric multitype contact processes on Z^d with a fitter supercritical type
source_status: primary-checked
primary_source: Thomas Mountford, Pedro Luis Barrios Pantoja and Daniel Valesin, "The asymmetric multitype contact process," Stochastic Processes and their Applications 129 (2019), 2783--2820
primary_pinpoint: Theorems 1.1--1.2; Proposition 4.4; Section 5, "Ancestor process and renewal-type random times"
primary_url: https://doi.org/10.1016/j.spa.2018.08.006
application_source: Thomas Mountford, Pedro Luis Barrios Pantoja and Daniel Valesin, same paper
application_pinpoint: Theorem 1.2 and proof architecture summarized at the end of Section 1; Proposition 3.2
application_url: https://arxiv.org/abs/1803.01533
wiki_candidate: yes
---

# Survival-conditioned renewal points for complete convergence

## Criterion

For the two-type contact process on $\mathbb Z^d$, suppose type 1 has birth rate $\lambda_1>\lambda_2$ and $\lambda_1>\lambda_c$. Mountford--Barrios Pantoja--Valesin construct, on the event that the type-1 ancestry from $(0,0)$ survives forever, a random space-time point $(X,T)$ with a genuine renewal property. Proposition 4.4 gives the key package: there is a free selective infection path from $(0,0)$ to $(X,T)$; the graphical configuration viewed from $(X,T)$ has, conditional on survival, the same future law as a fresh surviving graphical system and is independent of the pre-$T$ information; and both $T$ and $\|X\|$ have exponential moments. The displacement also has a controlled mean drift.

This survival-conditioned restart is then iterated inside the ancestor process. Together with steering estimates for selective infection paths, it yields Theorem 1.1: on survival, the stronger type eventually clears the weaker type from a ball growing linearly in time. Theorem 1.2 upgrades this to complete convergence:

\[
\xi_t\Longrightarrow
\mathbb P(\mathcal S_1)\bar\mu_1
+\mathbb P(\mathcal S_1^c\cap\mathcal S_2)\bar\mu_2
+\mathbb P((\mathcal S_1\cup\mathcal S_2)^c)\delta_{\underline0}.
\]

In particular, the three displayed laws are the extremal stationary distributions.

## Mechanism

The proof does not restart the full contact configuration at deterministic block times. Instead it follows the graphical **ancestor process** backward/forward until it discovers a random point whose future ancestry is fresh conditional on infinite survival. Section 5 is devoted to constructing these renewal-type random times.

The exponential-tail control makes repeated attempts quantitative. Once a renewal point is found, the post-renewal graphical future can be treated as a new survival-conditioned experiment, while the spatial displacement accumulated over renewals behaves like a random walk with exponential increments. Separate steering lemmas then force a surviving type-1 infection path toward prescribed macroscopic regions. The renewal sequence therefore converts the difficult dependence created by conditioning on survival into almost independent increments and permits repeated successful steering.

This is distinct from the live two-level contact block/restart method. There, supercritical coarse blocks are combined with a backward dual and a forward/backward intersection argument. Here the decisive object is an **exact survival-conditioned renewal point in the ancestor process**, and no second backward process has to intersect a forward block process to obtain the final complete-convergence mixture.

## Representative IPS use

The asymmetric multitype contact process is a three-state IPS with competing birth rates. Theorem 1.1 shows that, starting from at least one type-1 particle, the fitter type survives with positive probability and, conditional on survival, eventually removes type 2 from a linearly expanding ball. Theorem 1.2 then classifies all extremal stationary laws and proves convergence from every deterministic initial configuration to the survival/extinction mixture above.

The method is useful beyond the exact statement because it isolates a recurring contact-process technique: condition on survival, find an essential/renewal space-time point with a fresh graphical future, prove exponential control of the restart increments, and iterate.

## Limitations

The renewal construction uses the Harris graphical representation and strong supercritical contact-process estimates. It also exploits the strict fitness ordering $\lambda_1>\lambda_2$ and the existence of a surviving one-type ancestor process; it is not a generic regeneration theorem for arbitrary multitype IPS. Conditioning on survival is essential, so the renewal law is not an unconditional stationary regeneration structure. Finally, the complete-convergence theorem depends on additional steering and comparison arguments after the renewal lemma; Proposition 4.4 alone does not imply the full mixture limit.

## Sources

- Mountford, Barrios Pantoja and Valesin, *The asymmetric multitype contact process*, Theorems 1.1--1.2, Proposition 4.4, and Section 5. DOI: https://doi.org/10.1016/j.spa.2018.08.006; inspected full text: https://arxiv.org/abs/1803.01533.
