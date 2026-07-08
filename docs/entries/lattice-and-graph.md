---
title: Lattice and graph
status: definition
tags:
  - lattice
  - graph
  - neighbourhoods
  - site space
---

# Lattice and graph

A lattice is the default index set for configurations in this wiki. It is denoted by \(\Lambda\), and the standard examples are \(\Z\) and \(\Z^d\). A lattice may also be described as a graph by specifying which sites are neighbours.

## Configuration space

Given a lattice \(\Lambda\) and a single-site state space \(\mathcal S\), the configuration space is

$$
\Omega=\mathcal S^\Lambda.
$$

For \(A\subset\Lambda\) and \(\eta\in\Omega\), write \(\eta|_A\) or \(\eta_A\) for the restriction of \(\eta\) to \(A\). These restrictions are used in the definition of [local functions](local-functions.md) and local transition rates for [interacting particle systems](interacting-particle-system.md).

## Neighbourhood description

A neighbourhood system assigns to each \(i\in\Lambda\) a set \(N(i)\subset\Lambda\setminus\{i\}\). The set \(N(i)\) consists of the neighbours of \(i\) and does not contain \(i\). Write

$$
N_*(i)=N(i)\cup\{i\}
$$

for the neighbourhood together with the site itself.

A local update rate at \(i\) typically depends on \(\eta|_{N_*(i)}\), or on a specified finite subset of \(N_*(i)\). For a [spin system](spin-system.md), this means that the flip rate at \(i\) depends only on the spin at \(i\) and finitely many neighbouring spins.

## Translation-invariant lattice convention

On \(\Lambda=\Z^d\), locality is often described by a finite neighbourhood shape \(N\subset\Z^d\setminus\{0\}\). Then

$$
N(i)=i+N,
\qquad
N_*(i)=i+(N\cup\{0\}).
$$

Here \(N(i)\) does not contain \(i\), while \(N_*(i)\) does.

## Graph description

The same data can be encoded by a directed graph \(G=(\Lambda,E_G)\), with

$$
N(i)=\{j\in\Lambda:(i,j)\in E_G\}.
$$

For an undirected graph, this becomes

$$
N(i)=\{j\in\Lambda:\{i,j\}\in E_G\}.
$$

A translation-invariant neighbourhood shape \(N\subset\Z^d\setminus\{0\}\) corresponds to the directed graph with edges \((i,i+u)\) for \(u\in N\). If \(N=-N\), the corresponding graph can be treated as undirected.

## Finite range

A lattice model has finite range if the relevant update rates depend only on \(\eta|_{N_*(i)}\) for a finite neighbourhood shape \(N\). On a graph, the analogous condition is finite dependence on a neighbourhood of uniformly bounded graph distance.
