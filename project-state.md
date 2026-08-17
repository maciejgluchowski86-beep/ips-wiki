# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because the computation is exact or the constant is better. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed until changed or stopped by the principal: prove that every one-dimensional homogeneous binary one-sided nearest-neighbour simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/032-distinguished-zero-transfer-stops-and-hamming-coupling-killed.md`, `state_narrowed: yes`.
- Student G: active on Assignment 012, optimized information-percolation pair-history test.
- Student F: idle; no F016.
- No full proof architecture is reopened. Assignment 012 is a bounded pre-restart experiment.

## Most recent principal-directed result: distinguished-zero transfer

Student G Assignment 011 is accepted as **`STOP-EQUIVALENT`**.

The proposed transfer of East distinguished-zero screening by substituting the finite zero-boundary invariant family `pi_N` for Bernoulli equilibrium fails off the product surface.

If a right-measurable marker move leaves the old protected `N`-site block untouched and exact enlarged law is required to be `pi_{N+1}`, then necessarily

$$
\bar\pi_{N+1}=\pi_N.
$$

At the first nontrivial depth,

$$
\bar\pi_2(1)-\pi_1(1)
=-\frac{2a\,[a-b(1-c)]}
{(a+1-c)\,[2ab-ac+3a-bc+b+c^2-3c+2]}.
$$

Thus exact compatibility holds precisely on

$$
a=b(1-c),
$$

the product/reversible surface where

$$
\pi_N=\operatorname{Ber}\!\left(\frac b{1+b}\right)^{\otimes N}.
$$

At the hard point the defect equals `-4950/15151` exactly. The principal reran G's verifier successfully; the Professor independently recomputed the symbolic factorization.

Allowing a contaminated boundary buffer gives exactly the old tail-shift defect `Delta_M`; an arbitrary fresh finite release kernel cannot change the untouched-prefix marginal, so exact release requires a finite tail-shift identity and approximate release is bounded below by the same discrepancy.

Therefore marker-existence Part D is closed as moot **for this architecture**. This is a clean negative transfer theorem for the proposed `pi_N`-based East induction, not a universal theorem against every future screening idea.

## New exact coupling obstruction

Meeting 032 also proves that cross-site pairing cannot improve instantaneous drift of additive Hamming distance under any Markovian coupling of spin-flip chains. The optimal Hamming drift is

$$
\inf_{\text{couplings}}\bar L H
=
\sum_{i:x_i=y_i}|\lambda_i(x)-\lambda_i(y)|
-
\sum_{i:x_i\ne y_i}(\lambda_i(x)+\lambda_i(y)).
$$

At

$$
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

a one-disagreement local pattern has best possible drift

$$
\frac{9997}{10000}>0.
$$

Hence the toolbox refined-coupling bridge requiring uniform negative additive-Hamming drift is false for **every** Markovian coupling at the hard point. Its proposed non-diagonal Hamming LP is canceled as redundant. This does not refute a nonadditive Gray splice-edge geometry.

## Active bounded experiment

Student G Assignment 012, commit `be3d4e0ba6a81a6019de42d86a15858d47cefcb2`, tests the remaining independent toolbox candidate: information percolation / minimal backward histories.

The task derives the exact deterministic Boolean-map decomposition polytope of the residual generator, translates it into ancestry death/jump/branch rates, and studies **two independent backward support processes** through

$$
\Psi(A,A')=2^{|A\cap A'|}-1.
$$

Naive supercritical expected ancestor count is not a kill criterion. Computation is capped at relative width `W<=8` unless a structural recursion is discovered. A full proof block may reopen only if G finds a concrete pair-level contraction/obstruction theorem or another genuinely iterable Miller--Peres-type state.

## Connected-renewal route remains stopped

The sharp blocker remains the signed boundary-transmission Volterra operator on the actual connected orbit,

$$
\mathcal V_N f
=B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt.
$$

Both temporal factors change sign. No depth-uniform estimate preserving the two-time cancellation has been proved.

Bare tail shift, another `pi_N` distinguished-zero buffer, common-coupling all-depth occupation, Bellman/scalar Foster variants, reversible perturbation, generic norm searches, and longer coefficient tables remain stopped.

## Retained mathematics

The predecessor-trail reduction and canonical `J` quantity, projective zero-boundary invariant family and exact tail-shift identity, common-coupling fixed-site/local-erasure and actual-front results, stationary boundary-control hierarchy, exact trajectory-valued spatial kernel obstruction, G009 singular fixed-depth theorem, and G010 positive-frequency/renewal structure remain retained background.

## Wiki freeze

The live wiki remains frozen during active research. No `docs/` or `mkdocs.yml` edits are authorized by the current work.
