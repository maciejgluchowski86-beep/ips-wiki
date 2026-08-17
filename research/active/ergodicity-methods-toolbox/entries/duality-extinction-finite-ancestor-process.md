---
method_id: duality-extinction-finite-ancestor-process
title: Duality plus extinction of a finite ancestor process
category: graphical-duality
targets:
  - uniqueness
  - convergence
  - extinction
model_scope: Additive/contact-type IPS with a finite-set graphical dual or backward ancestor process
source_status: primary-checked
primary_source: Daniel Remenik, The Contact Process in a Dynamic Random Environment, Annals of Applied Probability 18 (2008), 2392-2420; corrected arXiv version 0901.2480v2
primary_pinpoint: Proposition 2.2 and condition (S1), pp. 7-8 of the arXiv version; Proposition 2.1, pp. 6-7; Theorem 2, pp. 4-5
primary_url: https://arxiv.org/abs/0901.2480
application_source: Daniel Remenik, The Contact Process in a Dynamic Random Environment, Annals of Applied Probability 18 (2008), 2392-2420; corrected arXiv version 0901.2480v2
application_pinpoint: Proposition 2.2, condition (S1), and Theorem 2
application_url: https://arxiv.org/abs/0901.2480
wiki_candidate: yes
---

# Duality plus extinction of a finite ancestor process

## Criterion

Suppose an attractive particle system has an absorbing lower state and a finite-set dual. In the simplest additive form, for primal occupied set $A$ and finite dual set $C$ one has a relation of the type

\[
\mathbb P^{A}(X_t\cap C\neq\varnothing)
=
\mathbb P^{C}(\widehat X_t\cap A\neq\varnothing).
\]

If the primal is started from its maximal configuration, the right side becomes the probability that the finite dual starting from $C$ is still nonempty at time $t$. Hence, if

\[
\mathbb P^{C}(\widehat X_t\neq\varnothing)\longrightarrow0
\qquad\text{for every finite }C,
\]

then every finite local occupation event has the same limiting probability under the upper process as under the absorbing lower process. Thus the upper and lower invariant laws coincide. Attractiveness then gives uniqueness of the invariant law; in settings where the extremal processes sandwich arbitrary initial states, it also gives convergence to that law.

The conclusion is stronger when a complete-convergence theorem is available: the long-time law is a mixture of the absorbing and upper invariant laws with weights given by extinction and survival probabilities. In the extinction regime the mixture collapses to the absorbing invariant law.

## Mechanism

The graphical representation is read in two directions. Forward active paths determine which initial particles can influence a site at time $t$. Starting from a finite test set at time $t$ and tracing the same arrows backward produces the dual ancestor set. The local question "is the primal occupied somewhere in $C$ at time $t$?" is therefore exactly a survival/intersection question for a process with finitely many initial ancestors.

This is useful because extinction of a finite particle system is often more tractable than direct comparison of two infinite-volume laws. One may dominate the dual by a subcritical branching process, use a Lyapunov function, exploit a one-dimensional random-walk representation, or prove a block/percolation extinction theorem. Duality then transfers that extinction statement to loss of dependence on the primal initial condition.

The argument is algebraic or graphical before any norm estimate: it does not require a direct contraction of the full primal semigroup. It also separates the two tasks cleanly. First identify an exact duality; then prove extinction or coalescence for the finite dual.

## Representative IPS use

Remenik studies a contact process whose occupied sites live in an independently evolving blocking environment. With the environment initially at equilibrium, Proposition 2.2 constructs the dual by reversing the graphical active paths and proves the self-duality identity (2.2). Taking one set finite gives condition (S1): survival from a finite nonempty occupied set is equivalent to nontriviality of the upper invariant measure.

Proposition 2.1 identifies lower and upper invariant laws. Consequently, if every finite occupied dual dies out, the upper invariant law equals the lower law, so the stationary law is unique. Theorem 2 proves complete convergence for the model:

\[
\mathcal L(\eta_t)\Longrightarrow
\mathbb P(\tau<\infty)\,\underline\nu
+
\mathbb P(\tau=\infty)\,\overline\nu.
\]

In the extinction regime $\mathbb P(\tau=\infty)=0$, giving convergence to the lower invariant law. The ordinary contact process is the classical prototype of the same self-duality/extinction mechanism.

## Limitations

An exact useful dual is highly model-dependent. For nonadditive spin systems the backward object may branch with signs, carry extra marks, or fail to remain finite, and extinction may be no easier than the original ergodicity problem. Self-duality can also require a special initial law for an auxiliary environment, as in Remenik's model.

Dual extinction proves loss of memory only for observables represented by the duality function; one must know that these observables determine the law. In additive binary systems, finite intersection/emptiness events do so, but this need not hold for an arbitrary duality. Finally, survival of the finite dual does not imply nonergodicity in every model; additional invariant-law structure is needed before reversing the implication.

## Sources

Primary source: Daniel Remenik, *The Contact Process in a Dynamic Random Environment*, Annals of Applied Probability 18 (2008), 2392-2420. The corrected arXiv version is used because it repairs an unrelated statement in Theorem 1(c). Proposition 2.2 gives graphical self-duality, condition (S1) identifies finite-set survival with nontriviality of the upper invariant law, and Theorem 2 gives complete convergence. https://arxiv.org/abs/0901.2480
