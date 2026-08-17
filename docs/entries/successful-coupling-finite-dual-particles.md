---
title: Successful coupling of finite dual particle systems
status: literature
audit: current
tags:
  - duality
  - coupling
  - invariant measures
---

# Successful coupling of finite dual particle systems

## Criterion

Let an interacting particle system admit a duality function $D(\xi,\eta)$ with finite dual configurations $\xi$. Suppose the dual preserves particle number, and write $\Omega_n$ for the $n$-particle sector. A **successful coupling** on $\Omega_n$ is a coupling $(\xi_t,\xi'_t)$ of two dual processes started from arbitrary $\xi,\xi'\in\Omega_n$ such that their coupling time

\[
\tau_{\xi,\xi'}=\inf\{t:\xi_s=\xi'_s\text{ for every }s\ge t\}
\]

is almost surely finite. Equivalently, the probability that the coupled copies still disagree tends to zero.

Redig and van Wiechen prove the following consequence. If such a successful coupling exists and $\mu$ is a tempered invariant measure for the primal system, then its dual transform

\[
\widehat\mu(\xi)=\int D(\xi,\eta)\,\mu(d\eta)
\]

is constant on each $\Omega_n$: there is a function $f$ with $\widehat\mu(\xi)=f(n)$ whenever $|\xi|=n$. If $\mu$ is also ergodic, then $f(n)=f(1)^n$. Under their moment-determining hypotheses this identifies $\mu$ as one of the product measures $\mu_\theta$ and yields the classification of tempered extremal invariant measures in Theorem 3.2.

## Mechanism

Duality turns invariance of $\mu$ into harmonicity of $\widehat\mu$ for the finite dual. Starting two dual configurations in the same particle-number sector and coupling them successfully gives

\[
|\widehat\mu(\xi)-\widehat\mu(\xi')|
\leq C_n\,\mathbb P(\xi_t\neq\xi'_t),
\]

with the required bound supplied by temperedness. The right-hand side vanishes as $t\to\infty$, so bounded dual-harmonic information cannot distinguish configurations inside $\Omega_n$.

The second step uses ergodicity of the primal invariant measure. Far-separated dual particles probe asymptotically independent translates of local observables, while the first step says the transform depends only on their number. This forces multiplicativity in $n$. Thus the coupling does not make the dual disappear; it collapses the space of harmonic functions on every conserved sector.

This is distinct from finite-dual extinction, where memory vanishes because the ancestor set hits an absorbing empty state, and from voter duality, where ancestral lineages merge and the effective number of ancestors decreases. Here both coupled duals retain the same fixed number of particles and are made to agree configuration by configuration.

## Representative IPS use

Section 4 treats multi-layer versions of symmetric exclusion, symmetric inclusion, and independent random walkers. The authors label finitely many dual particles and couple their internal layer states and spatial motions. Interactions are handled by repeatedly spreading particles apart and restarting the coupling attempts. Theorem 4.1 combines this successful finite-particle coupling with the duality classification to show that the stated product measures are the only tempered ergodic invariant measures for the models considered.

## Limitations

The method needs a useful duality, control of dual moments strong enough to pass coupling estimates through the dual transform, and successful coupling in every finite particle-number sector. Conserved quantities can leave a parameter family of invariant laws; the conclusion is classification within the tempered class, not uniqueness of one global invariant measure across all densities. Successful coupling can also be difficult when finite dual particles have additional conserved labels, trapping geometry, or interactions that prevent two copies from meeting and remaining together.

## Sources

Frank Redig and Hidde van Wiechen, *Ergodic Theory of Multi-layer Interacting Particle Systems*, Journal of Statistical Physics **190** (2023), Article 88. Section 3.2 defines successful coupling; Theorems 3.1--3.2 turn it into the invariant-measure classification. Section 4 and Theorem 4.1 establish the coupling and resulting classification for the multi-layer exclusion, inclusion, and independent-walker examples. DOI: https://doi.org/10.1007/s10955-023-03099-2
