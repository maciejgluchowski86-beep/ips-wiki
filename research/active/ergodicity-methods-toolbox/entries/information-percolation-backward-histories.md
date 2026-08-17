---
method_id: information-percolation-backward-histories
title: Information percolation and backward update histories
category: graphical-duality
targets:
  - mixing
  - coupling-agreement
model_scope: Finite-volume Glauber dynamics admitting a graphical random-mapping representation with backward update supports, especially high-temperature Ising dynamics
source_status: primary-checked
primary_source: Eyal Lubetzky and Allan Sly, Information percolation and cutoff for the stochastic Ising model, Journal of the American Mathematical Society 29 (2016), 729-774; arXiv:1401.6065v3
primary_pinpoint: Theorem 1, pp. 2-3; Section 1.2, pp. 5-6; Section 2.2, pp. 8-9; Definition 2.3 and equation (2.7), pp. 10-11
primary_url: https://arxiv.org/abs/1401.6065
application_source: Eyal Lubetzky and Allan Sly, Information percolation and cutoff for the stochastic Ising model, Journal of the American Mathematical Society 29 (2016), 729-774
application_pinpoint: Theorem 1, pp. 2-3, continuous-time Glauber dynamics for the Ising model on (Z/nZ)^d for every beta below beta_c
application_url: https://doi.org/10.1090/jams/841
wiki_candidate: yes
---

# Information percolation and backward update histories

## Criterion

Fix a target time $t$ for a graphical single-site dynamics. For each top vertex $v$, reveal backward the minimal update support $H_v(s)$: the set of spins at time $s<t$ whose values are still needed to determine $X_t(v)$ after the update marks on $(s,t]$ are fixed. Join intersecting histories into space-time clusters. In the Lubetzky--Sly framework, a cluster is **red** if its support reaches time $0$, **blue** if it dies before time $0$ and has one top vertex, and **green** otherwise.

After conditioning on the green histories, blue top spins are independent of the initial configuration, while all remaining initial-state dependence is carried by the random red set $R$. A reusable sufficient mixing estimate is therefore to show that, for independent copies $R,R'$, the conditional exponential intersection moment satisfies

\[
\mathbb E\!\left[2^{|R\cap R'|}\mid H_{\mathrm{Green}}\right]
\longrightarrow 1.
\]

Equation (2.7) in Lubetzky--Sly uses precisely this criterion. Via the Miller--Peres $L^2$ estimate, it forces the total-variation distance between dynamics from different initial states to vanish. Thus one need not make every backward history die; it is enough that the surviving information clusters are sufficiently sparse and weakly intersecting.

## Mechanism

The graphical update sequence consists of sites, times and auxiliary uniform variables. An **oblivious update** writes a fresh spin independently of its neighbors, so a backward dependency branch stops there. A non-oblivious update replaces the current dependency by the neighboring spins on which that update actually depends. Lubetzky--Sly define the update support $F_{\mathrm{sup}}(A,s,t)$ as the minimal set at time $s$ determining the spins of $A$ at time $t$ once the update marks are known.

At very high temperature this backward genealogy behaves like a subcritical branching process: branches are frequently killed by oblivious updates. The full method is more flexible. Histories may merge, split and lose vertices when a nominal dependency becomes logically irrelevant. Their connected components reveal exactly which top spins share information from the initial state.

The red/blue/green decomposition then separates initial-state information from equilibrium noise. Green clusters may have complicated internal dependence but, after conditioning on their histories, their law is independent of the initial state. Blue sites supply a large product-like background. The proof task is reduced to showing that the sparse red clusters are statistically lost inside this background. This is strictly weaker than coupling all starting states by time $t$ and is why information percolation can locate mixing more sharply than the coalescence time of the monotone grand coupling.

## Representative IPS use

For continuous-time Glauber dynamics of the ferromagnetic Ising model on $(\mathbb Z/n\mathbb Z)^d$, Theorem 1 of Lubetzky--Sly proves that for every $\beta<\beta_c$ the chain has total-variation cutoff with an $O(1)$ window around

\[
t_m=\inf\{t:m_t(v)\le |\Lambda|^{-1/2}\},
\]

where $m_t(v)$ is the magnetization from the all-plus initial state. Lemma 2.1 supplies exponential decay of the backward update support throughout the one-phase regime, while Sections 3--5 refine the naive branching picture sufficiently to cover the full high-temperature region, even where a simple subcritical-branching domination is no longer valid.

In one dimension, Example 2.4 makes the genealogy especially transparent: each history is a continuous-time random walk that moves at non-oblivious updates and dies at oblivious ones, and different histories coalesce.

## Limitations

The method needs a usable random-mapping representation and quantitative control of backward supports. At very high temperature a crude subcritical branching comparison may suffice; closer to criticality the histories are not naively subcritical and the proof requires model-specific refinements, conditioning and multiscale estimates. At low temperature persistent macroscopic information clusters are expected, so the same small-red-cluster estimates fail.

Information percolation is not synonymous with coupling from the past. CFTP asks for a backward random map to coalesce sufficiently far in the past, often to produce an exact stationary sample. Information percolation may prove ordinary or sharp mixing while some histories still reach the initial time, provided those red histories are sparse. Likewise, clan-of-ancestors/perfect-simulation methods typically seek almost surely finite backward dependency clans; they warrant a separate entry.

## Sources

Primary source: Eyal Lubetzky and Allan Sly, *Information percolation and cutoff for the stochastic Ising model*, Journal of the American Mathematical Society 29 (2016), 729-774, Theorem 1, Sections 1.2 and 2.2-2.3, especially Definition 2.3 and (2.7). https://arxiv.org/abs/1401.6065

Published version: https://doi.org/10.1090/jams/841
