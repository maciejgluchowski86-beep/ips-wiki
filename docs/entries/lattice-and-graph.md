---
title: Lattice and graph
status: definition
tags:
  - site space
  - graph
  - lattice
  - neighbourhoods
---

# Lattice and graph

The site space specifies where the components of a configuration live and which sites may influence which updates. It is used to define the configuration space of an [interacting particle system](interacting-particle-system.md), the flip rates of a [spin system](spin-system.md), and the dependence sets of [local functions](local-functions.md).

## Site set

A site set is a countable set \(I\). For a single-site state space \(E\), the configuration space is

$$
\Omega=E^I.
$$

For \(A\subset I\) and \(\eta\in\Omega\), write \(\eta|_A\) or \(\eta_A\) for the restriction of \(\eta\) to \(A\).

## Graph description

A graph description consists of a countable simple graph \(G=(I,E_G)\). The graph may be undirected or directed. For a directed graph, define the out-neighbourhood and in-neighbourhood by

$$
N^+(i)=\{j\in I:(i,j)\in E_G\},
\qquad
N^-(i)=\{j\in I:(j,i)\in E_G\}.
$$

For an undirected graph these coincide, and one writes

$$
N(i)=\{j\in I:\{i,j\}\in E_G\}.
$$

It is often convenient to include the site itself and write

$$
N_*(i)=N(i)\cup\{i\}.
$$

For a local spin system, the flip rate at \(i\) typically depends on \(\eta|_{N_*(i)}\) or on a specified finite subset of \(N_*(i)\).

## Lattice-neighbourhood description

On \(I=\Z^d\), locality is often described by a finite neighbourhood shape \(N\subset\Z^d\setminus\{0\}\). Then

$$
N(i)=i+N,
\qquad
N_*(i)=i+(N\cup\{0\}).
$$

This description is equivalent to a translation-invariant directed graph with edges \((i,i+u)\) for \(u\in N\). If \(N=-N\), the corresponding graph can be treated as undirected.

## Finite range

A lattice model has finite range if there is a finite set \(N\) such that all rates at site \(i\) depend only on \(\eta|_{i+N_*}\). On a general graph, the analogous condition is that each update has a finite dependence set, usually uniformly bounded in size or graph distance.
