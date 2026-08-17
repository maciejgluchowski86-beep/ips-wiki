# 008a: classical duality and graphical predecessors

Date: 2026-08-17

This note records the first source-by-source novelty comparison for Assignment 008. It is a literature audit, not a correctness proof.

## 1. Lloyd--Sudbury and algebraic product duality

Relevant sources:

- A. Sudbury and P. Lloyd, *Quantum operators in classical probability theory II: The concept of duality in interacting particle systems*, Ann. Probab. 23 (1995), 1816--1830, DOI 10.1214/aop/1176987804.
- A. Sudbury and P. Lloyd, *Quantum operators in classical probability theory IV: Quasi-duality and thinnings of interacting particle systems*, Ann. Probab. 25 (1997), 96--114.
- A. Sudbury, *Dual families of interacting particle systems on graphs*, J. Theoret. Probab. 13 (2000), 695--716.
- A. Sturm, J. Swart and F. Voellering, *The algebraic approach to duality: an introduction*, arXiv:1802.07150.

These sources make clear that generator-level duality with product/local duality functions and single-site operator calculus are classical. The 1995--2000 Lloyd--Sudbury programme gives systematic algebraic dualities for nearest-neighbour IPS, and the later survey explicitly places this inside the general operator/intertwining framework.

**Novelty consequence.** The following pieces of package A cannot be claimed as new by themselves:

- using a product/tensor local observable basis;
- deriving a dual operator from a generator identity;
- using local operator algebra to organize duality.

What was not found in these sources is the Assignment-001 construction for arbitrary finite-state single-site replacement IPS in which arbitrary signed tensor coefficients are realized as a branching/retyping signed graphical process plus an additive Feynman--Kac potential, followed by the later hidden-outcome patch construction. The classical Lloyd--Sudbury results are therefore a close predecessor to the *duality ingredient*, not direct subsumption of package A as a whole.

Provisional status for item 1 (finite-state typed signed duality): **known ingredients, assembly plausibly new**. The tensor expansion itself is standard/elementary and receives no novelty credit.

## 2. Sturm--Swart pathwise duality for finite local state spaces

Source:

- A. Sturm and J. M. Swart, *Pathwise duals of monotone and additive Markov processes*, J. Theoret. Probab. 31 (2018), 932--983; arXiv:1510.06284.

The paper develops random-mapping/Poisson graphical constructions for finite-state Markov processes and extends monotone/additive pathwise duality to interacting particle systems with finite local state spaces. In particular, its Section 2.2 writes finite generators as random mapping representations and constructs stochastic flows from Poisson marks; Section 5 passes to infinite products of finite local spaces.

This is a strong predecessor for the statements "finite local state space", "local graphical maps", and "dual process read backward through a Poisson construction". It also explicitly notes earlier local-state work for binary and three-state systems.

However, its hypotheses and mechanism are order-theoretic: monotone/additive maps produce an honest pathwise dual. Assignment 001 instead treats arbitrary bounded finite-range single-site replacement rates, allows signed branch coefficients, and repairs non-Markov generator pieces using signs and Feynman--Kac potential. The later typed target conflicts/cemetery and hidden-source-outcome factorization do not appear in the Sturm--Swart construction.

**Novelty consequence.** Finite-state graphical duality is directly known in substantial structured classes. The generalized project must not frame "finite-state graphical duality" itself as the contribution.

## 3. Jansen--Kurt and general duality/intertwining framework

Source:

- S. Jansen and N. Kurt, *On the notion(s) of duality for Markov processes*, Probab. Surv. 11 (2014), 59--120; arXiv:1210.7193.

This source systematically treats generator/semigroup duality, pathwise duality, rescaling, intertwining, symmetries and convex-geometric formulations. Together with the algebraic-duality literature, it establishes that much of Assignment 001 at the abstract operator level is standard finite-dimensional duality technology.

It does not supply the later patch mechanism: no coarser successful-interaction skeleton, no local hidden-mark conditional averaging, no killed/cemetery patch factorization, and no bulk positivity criterion of the present type was located.

## 4. Information percolation: closest predecessor for partial revelation

Source:

- E. Lubetzky and A. Sly, *Information percolation and cutoff for the stochastic Ising model*, arXiv:1401.6065 (2014/2015).

This is the closest source found so far to the *geometry* of the patch idea. Their construction runs the graphical update history backward in spacetime. Updates carry independent auxiliary randomness; some updates are "oblivious" and kill a dependency branch, while non-oblivious updates split the history into neighbours. Dependency histories merge into spacetime clusters. They explicitly condition on/handle cluster information and, in the information-percolation analysis, separate geometric dependency information from additional update randomness; variants even defer some update randomness and sprinkle it later.

This shows that the high-level strategy

> reveal a coarser spacetime dependency geometry while leaving some local update randomness to be integrated later

is not unique to the patch programme and must not be advertised as new in that broad form.

The mathematical object is nevertheless different in decisive respects:

1. the process is an ordinary Glauber dynamics, not a signed dual/Feynman--Kac process;
2. the hidden randomness determines spins/dependencies, not signs/source-survival branches in a dual expansion;
3. there is no local factorization of a signed Feynman--Kac weight into one-site patch contributions;
4. there is no typed target-conflict cemetery phenomenon and therefore no killed/noncemetery repair analogous to Assignment 002;
5. there is no bulk patch positivity property or coefficient/transfer criterion.

Thus information percolation is a conceptual predecessor for partial graphical revelation and spacetime clusterization, but does not directly subsume packages A--D.

## 5. Provisional package implications after this source group

The search so far forces the following conservative framing:

- finite tensor/product duality: **standard ingredient**;
- Poisson graphical/random-mapping duality with finite local state spaces: **known in major structured classes**;
- revealing dependency geometry while retaining hidden update randomness: **known conceptual mechanism** (information percolation and related backward-history methods);
- combining an arbitrary finite-state signed Feynman--Kac dual with a coarser successful skeleton, hidden source-outcome averaging, typed cemetery conflicts, and exact patchwise factorization: **not directly found in these sources**.

No global novelty ruling is made yet. The next comparisons must target Feynman--Kac/branching representations, signed matrix semigroups, cluster/factorization constructions, and criterion-level positive-semigroup literature.