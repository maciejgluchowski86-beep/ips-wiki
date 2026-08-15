# Literature and prior-work record

## Primary target source

Luca Avena, Rangel Baldasso, Rajat Subhra Hazra, Frank den Hollander, Matteo Quattropani, *Discordant edges for the voter model on regular random graphs*, ALEA 21 (2024), 431--464, DOI `10.30757/alea.v21-18`, arXiv `2209.01037`.

The paper studies the two-opinion voter model on a uniformly random simple `d`-regular graph, `d>=3`, started from i.i.d. Bernoulli(`u`) opinions. It tracks

$$
\mathcal D_t^n=\frac{|D_t^n|}{dn/2},
$$

the fraction of discordant edges.

The source proves expected-value asymptotics across short, moderate, and consensus time scales and develops a weak-dependence method for concentration of discordance. Section 1.4 states an expected strengthening, Eq. (1.9), at the `sqrt(t/n)` scale throughout sublinear time. Graduate Student D must copy the exact quantifiers/probability mode and the precise proved comparison theorem from source before treating this as the programme target.

## Successor check

Targeted searches through 2026-08-16 found later work on voter models with random rewiring and on directed/heterogeneous sparse random graphs, but no identified paper resolving the static random-regular-graph concentration strengthening posed in Eq. (1.9).

Relevant adjacent sources include:

- Avena--Baldasso--Hazra--den Hollander--Quattropani, *The voter model on random regular graphs with random rewiring*, arXiv `2501.08703`;
- Federico Capannoli, *Evolution of discordant edges in the voter model on random sparse digraphs*, arXiv `2407.06318`.

This is a targeted check, not proof of absence. Before any major novelty claim, repeat citation/successor searching.

## Prior reconnaissance

Graduate Student A's earlier opportunity-cost note on branch `research/babp-finite-seed`, file

`research/active/babp-finite-seed/students/student-a/recon-001-open-problem-scan.md`,

ranked this as the strongest reserve after noisy East. It records the candidate generator identity and the observation that the martingale part has the conjectured fluctuation scale. Those calculations are not authority; Graduate Student D must rederive them.

## First literature tasks

Assignment 001 must locate and record:

1. the exact source statement of Eq. (1.9);
2. the exact theorem giving the currently proved concentration window;
3. the point in the proof where the moderate-time restriction enters;
4. the dual coalescing-walk formula for discordant-edge indicators used in the concentration proof;
5. any later citation that specifically strengthens the static random-regular concentration window.
