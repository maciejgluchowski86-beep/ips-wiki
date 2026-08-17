# 009a: literature-driven selection of a natural three-state application

Date: 2026-08-17

This note executes Part A of Assignment 009. The selection is committed **before** any typed coefficient or patch-positivity calculation for the selected model. Patch positivity is not used as a selection criterion.

## Candidate 1: Krone two-stage contact process

Source: S. M. Krone, *The two-stage contact process*, Ann. Appl. Probab. 9 (1999), 331--351, DOI 10.1214/aoap/1029962745. The model and its duality are revisited in E. Foxall, *New Results for the Two-Stage Contact Process* and *Duality and Complete Convergence for Multi-Type Additive Growth Models*.

Local states are

- `0`: vacant;
- `1`: juvenile/young;
- `2`: adult/mature.

On the standard homogeneous version, at site `x`,

\[
0\to1 \text{ at rate } \lambda n_2(x),
\qquad
1\to2 \text{ at rate } \gamma,
\]

\[
1\to0 \text{ at rate } 1+\delta,
\qquad
2\to0 \text{ at rate } 1,
\]

where `n_2(x)` is the number of adult neighbours. This is exactly the formulation used in Foxall's multitype-additive treatment; variants merely rescale the death-rate notation.

### Genuine three-state check

This is not a binary contact process with a passive color. State `1` is dynamically indispensable:

- newborns enter state `1`;
- only state `2` reproduces;
- the local conversion `1->2` occurs at positive rate `gamma`;
- the death rate of state `1` may differ from that of state `2` through `delta`.

For `gamma` finite and positive, eliminating the juvenile state changes the process.

### Single-site replacement check

Every event changes exactly one site. The only neighbour-dependent event is `0->1`; its rate depends on which neighbours are in active state `2`.

### Graphical/duality context

Krone's original analysis uses a multitype dual. Foxall gives a simplified duality proof and places the process in a general class of additive multitype growth models, with graphical/percolative representations and complete convergence. Thus any application claim must be compared against a strong existing duality theory rather than treating graphical duality itself as new.

### Irreducibility

The all-vacant configuration is absorbing, so the process is not irreducible. This is recorded but is not used against the model in selection.

## Candidate 2: stochastic spatial SIRS

Representative source: J. Joo and J. L. Lebowitz, *Pair approximation of the stochastic susceptible-infected-recovered-susceptible epidemic model on the hypercubic lattice*, Phys. Rev. E 70 (2004), 036114, DOI 10.1103/PhysRevE.70.036114; see also the later lattice-gas formulation of de Souza--Tome.

Local states are susceptible `S`, infected `I`, recovered/immune `R`, with continuous-time transitions

\[
S\to I \text{ at rate } \lambda n_I(x),
\qquad
I\to R \text{ at rate } \delta,
\qquad
R\to S \text{ at rate } \gamma.
\]

It is genuinely three-state for finite positive `delta,gamma`: the recovered state has a distinct residence time and feeds back to susceptibility. All physical events are single-site replacements. The all-susceptible configuration is absorbing, so irreducibility again fails and is not used as a selection criterion.

This is a natural application candidate, but the rigorous IPS literature around its graphical duality is less canonical than for the two-stage contact process. It is retained as a materially different second candidate if the selected model fails patch positivity structurally.

## Candidate 3: Neuhauser multitype contact process

Source: C. Neuhauser, *Ergodic theorems for the multitype contact process*, Probab. Theory Relat. Fields 91 (1992), 467--506, DOI 10.1007/BF01192067.

Local states are `0` vacant and active types `1,2`. A type-`i` particle dies at rate one, while a vacant site becomes type `i` at rate `lambda_i` times the local proportion (or, after a fixed normalization, number) of type-`i` neighbours.

This is a genuine three-state competition model: both types have independent reproduction mechanisms and compete for vacancies. It is single-site replacement and has an absorbing empty state. However, there is no local `1<->2` stage conversion. Relative to the current application question, it is therefore a less stringent test of whether the killed typed patch mechanism handles essential active-type evolution rather than simply two colored contact processes sharing vacancies.

## Selection ruling

**Select the two-stage contact process.**

The selection criteria, fixed before positivity calculation, are:

1. it is a classical published nonbinary IPS rather than a model invented for this programme;
2. all physical events are single-site replacements;
3. the third state is essential: juvenile and adult roles cannot be quotiented without changing the dynamics;
4. it contains both neighbour-driven reproduction and local active-type conversion, so the typed successful skeleton has genuinely multitype geometry;
5. it has an established nontrivial multitype duality literature, making it a hard test of whether the killed typed patch representation supplies anything beyond known duality.

No coefficient from the typed patch-positivity criterion has been computed in reaching this selection. In particular, no use has been made of whether the selected model is patch positive.

## Sources used

- Krone (1999), DOI 10.1214/aoap/1029962745.
- Foxall, arXiv:1401.2570 / J. Appl. Probab., *New Results for the Two-Stage Contact Process*.
- Foxall, arXiv:1410.4809 / Adv. Appl. Probab. 48 (2016), 32--51.
- Joo--Lebowitz (2004), DOI 10.1103/PhysRevE.70.036114.
- Neuhauser (1992), DOI 10.1007/BF01192067.
