---
title: Spin system
status: definition
tags:
  - interacting particle systems
  - Markov generator
  - flip rates
---

# Spin system

This entry fixes the baseline object for the wiki: a continuous-time Markov process whose state is an assignment of spins to sites. Most later entries, including [ergodicity](ergodicity.md), use this language.

**Status.** Definition and convention.

**Links.** Related entry: [ergodicity](ergodicity.md).

**Main references.** Liggett, *Interacting Particle Systems*; Liggett, *Stochastic Interacting Systems*.

!!! definition "Spin system"
    Let \(\Lambda\) be a countable site set and let \(E\) be a finite single-site spin space. A spin system is a continuous-time Markov process \((\eta_t)_{t\ge0}\) on
    \[
        \Omega=E^\Lambda.
    \]
    For a two-state flip system, with \(E=\{0,1\}\) or \(E=\{-1,+1\}\), the generator has the form
    \[
        \cL f(\eta)
        =\sum_{x\in\Lambda} c(x,\eta)\bigl(f(\eta^x)-f(\eta)\bigr),
    \]
    where \(\eta^x\) is obtained from \(\eta\) by flipping the spin at \(x\), and \(c(x,\eta)\ge0\) is the flip rate at \(x\) in configuration \(\eta\).

The sum in the generator is interpreted first on local functions. A local function depends on only finitely many coordinates of \(\eta\). Additional hypotheses on the rates, such as finite range, translation invariance, boundedness, or continuity in the product topology, are imposed entry-by-entry.

!!! convention "Default lattice convention"
    Unless another site set is specified, the wiki uses \(\Lambda=\Z\) or \(\Lambda=\Z^d\). For the one-dimensional one-sided models in the research notes, the default site set is \(\Z\).

!!! remark "Terminology"
    In this wiki, spin system is used as a broad continuous-time interacting particle system with finite single-site space. The term does not by itself imply attractiveness, monotonicity, reversibility, finite range, positive rates, or uniqueness of an invariant measure.

!!! remark "Positive rates"
    For a two-state flip system, positive rates usually means that the allowed local flip rates are strictly positive for every local neighborhood configuration. The precise lower bound, locality assumption, and dependence set must be stated in each theorem or route where positive rates are used.
