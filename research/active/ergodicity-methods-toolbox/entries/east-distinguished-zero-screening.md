---
method_id: east-distinguished-zero-screening
title: Distinguished-zero screening in the East model
category: kcsm-model-specific
targets:
  - convergence
  - mixing
model_scope: One-dimensional oriented East KCSM, especially nonequilibrium convergence of local observables
source_status: primary-checked
primary_source: Alessandra Faggionato, Fabio Martinelli, Cyril Roberto, and Cristina Toninelli, The East model: recent results and new progresses, Markov Processes and Related Fields 19(3) (2013), 407-452.
primary_pinpoint: Definition 8.1, Remark 8.1, Lemma 8.2, and the proof of Theorem 3.5 in Section 8, pp. 27-29 of arXiv:1205.1607v1
primary_url: https://arxiv.org/abs/1205.1607
application_source: Alessandra Faggionato, Fabio Martinelli, Cyril Roberto, and Cristina Toninelli, The East model: recent results and new progresses, Markov Processes and Related Fields 19(3) (2013), 407-452.
application_pinpoint: Theorem 3.5 and Section 8 proof
application_url: https://arxiv.org/abs/1205.1607
wiki_candidate: yes
---

# Distinguished-zero screening in the East model

## Criterion

In the East process a site may refresh only when its right neighbor is empty. Start from a configuration having a zero at site \(b\), declare that zero distinguished, and let \(\xi_t\) be its position: it stays at its current site until the next legal ring there, then moves one step to the right, and repeats. Definition 8.1 of Faggionato--Martinelli--Roberto--Toninelli makes \(\xi_t\) nondecreasing and ensures \(\eta_t(\xi_t)=0\) for all \(t\).

The key screening statement is Lemma 8.2. If initially the interval \([a,b)\) is distributed according to the Bernoulli equilibrium law and \(b\) is distinguished, then, conditional on the entire path \((\xi_s)_{s\le t}\), the configuration on the region left behind the distinguished zero,
\[
[a,\xi_t),
\]
is still exactly at equilibrium. In particular, the random moving vacancy acts as a regeneration boundary that shields the left region from the unequilibrated configuration farther to the right.

## Mechanism

The mechanism uses the strict orientation of East. Clock rings and coin tosses to the left of the distinguished zero cannot influence the future legal-ring times that determine its motion. Between successive jumps, the region behind the vacancy evolves as an East process with a frozen zero boundary and therefore preserves the product equilibrium law. At a jump, the site just left behind is refreshed by the legal ring with the equilibrium Bernoulli distribution. Induction over jump times proves the conditional equilibrium statement.

For nonequilibrium convergence, place a distinguished zero just to the right of the support of a local observable. Conditioning on its trajectory splits off a finite left interval whose equilibrium mean is already known. One then estimates deviations from equilibrium on that interval using the East Poincare inequality/spectral gap. The distinguished zero supplies the exact spatial shielding needed to apply equilibrium relaxation even though the original configuration to the right need not be equilibrated.

## Representative IPS use

Faggionato--Martinelli--Roberto--Toninelli Theorem 3.5 states exponential convergence of local observables for the infinite East process started from a nontrivial Bernoulli product law with density different from equilibrium. In Section 8, for a local \(f\), they choose the first zero to the right of \(\operatorname{supp} f\), distinguish it, use Lemma 8.2 to make the portion behind its path conditionally equilibrium, and then apply the positive East spectral gap to control the remaining variance. The resulting estimate decays exponentially in time.

The review attributes the distinguished-zero construction and the underlying conditional-equilibrium lemma to Aldous and Diaconis, *The Asymmetric One-Dimensional Constrained Ising Model: Rigorous Results* (2002). The later paper uses it as a modular nonequilibrium screening device.

## Limitations

This method exploits more than the existence of mobile defects: it uses the one-sided orientation strongly enough that the distinguished vacancy's future is unaffected by the region it leaves behind. A vacancy in a symmetric facilitated model generally does not create the same conditional independence. The method also does not by itself prove a positive spectral gap; the convergence proof of Theorem 3.5 imports the already-established East gap as a quantitative relaxation input. Product equilibrium and the refresh form of the update are used in the exact regeneration lemma. For initial laws with too few vacancies, or deterministic configurations where no suitable vacancy occurs to the right of the observable, additional arguments are needed.

## Sources

- Faggionato, Martinelli, Roberto, Toninelli, *The East model: recent results and new progresses*, Definition 8.1, Remark 8.1, Lemma 8.2 and Section 8 proof of Theorem 3.5, https://arxiv.org/abs/1205.1607.
- David Aldous and Persi Diaconis, *The Asymmetric One-Dimensional Constrained Ising Model: Rigorous Results*, Journal of Statistical Physics 107 (2002), 945-975, arXiv:math/0110023, https://arxiv.org/abs/math/0110023. The later review explicitly attributes the distinguished-zero notion and lemma to this source.
