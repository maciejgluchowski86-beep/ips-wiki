---
title: Classical, weak, mild, and viscosity solutions
status: standard fact
audit: current
tags:
  - PDE
  - classical solution
  - weak solution
  - mild solution
  - viscosity solution
---

# Classical, weak, mild, and viscosity solutions

Classical, distributional or weak, mild, and viscosity solutions are four different ways to give mathematical meaning to a PDE. They are not a global hierarchy. Relations among them depend on the equation, domain, function spaces, boundary or initial data, and separate regularity or comparison theorems.

## Prerequisites

Read the vocabulary chain in order: [Partial differential equations: basic vocabulary](partial-differential-equations-basic-vocabulary.md), [Initial, terminal, boundary, and initial-boundary value problems](initial-terminal-and-boundary-value-problems.md), [Linear, semilinear, quasilinear, and fully nonlinear equations](linear-semilinear-quasilinear-and-fully-nonlinear-equations.md), and [Elliptic, parabolic, and hyperbolic equations](elliptic-parabolic-and-hyperbolic-equations.md).

## One equation, four interpretations

Use the forced heat equation as a common example,

$$
\partial_tu-\Delta u=f,
\qquad
u(0,\cdot)=u_0.
\tag{1}
$$

The four notions below answer different questions about what it means for $u$ to satisfy (1).

### Classical solution: evaluate the PDE pointwise

A classical solution has enough derivatives for every term in the PDE to be evaluated pointwise. For (1), a typical interior requirement is $u\in C^{1,2}$ in time and space, together with enough continuity of the data to make

$$
\partial_tu(t,x)-\Delta u(t,x)=f(t,x)
$$

an ordinary equality at every interior point. Initial and boundary conditions are then imposed in the pointwise sense when the relevant traces are continuous.

Classical solvability is therefore a regularity statement as well as an equation statement. A function may solve the same PDE in a weaker sense even when the derivatives in (1) do not exist pointwise.

### Distributional identity: move derivatives to test functions

Suppose only that $u$ and $f$ are locally integrable in the open space-time region. Equation (1) holds in the sense of distributions when

$$
\int u\,(-\partial_t\varphi-\Delta\varphi)
=
\int f\varphi
\tag{2}
$$

for every compactly supported smooth test function $\varphi$, with the integrals taken over space-time. Formula (2) defines the derivatives of $u$ by duality; it does not require $\partial_tu$ or $D^2u$ to exist as functions.

A bare interior distributional identity does not by itself encode the function space, boundary trace, or initial trace appropriate to a particular PDE problem. Those are extra parts of the formulation.

### Weak solution: an equation-specific function-space formulation

The term *weak solution* is not a universal synonym for "distributional solution." In PDE practice it usually means a distributional or integration-by-parts identity together with function-space hypotheses chosen for the equation.

For example, an energy formulation of the heat equation may require

$$
u\in L^2(0,T;H^1(\Omega)),
\qquad
\partial_tu\in L^2(0,T;H^{-1}(\Omega)),
$$

and interpret (1) through

$$
\langle \partial_tu,v\rangle_{H^{-1},H^1}
+
\int_\Omega \nabla u\cdot\nabla v
=
\langle f,v\rangle
\tag{3}
$$

for admissible test functions $v$. The exact spaces and the way initial or boundary data enter (3) depend on the problem. Thus "weak solution" must always be read with its accompanying definition.

Evans gives standard examples of this distinction in §§6.1.2 and 7.1.1 (pp. 373--375); §6.3.1, Theorem 3 is an example of the separate regularity theory needed to strengthen weak solutions.

### Mild solution: use the linear semigroup

Let $S(t)=e^{t\Delta}$ denote the heat semigroup. A mild formulation of (1) is the variation-of-constants identity

$$
u(t)
=
S(t)u_0
+
\int_0^t S(t-s)f(s)\,ds.
\tag{4}
$$

For a semilinear equation, the same formula has a nonlinear term depending on $u$ inside the integral. Definition (4) can make sense in a Banach space even when the pointwise derivatives in (1) do not.

A mild solution is therefore not automatically a classical solution. A separate regularity theorem is needed. Pazy, Chapter 6, §1, Definition 1.1 gives the abstract mild formulation, while Theorem 1.5 gives one concrete upgrade: in the $C_0$-semigroup setting, with continuously differentiable nonlinearity and initial datum in the generator domain, the mild solution is classical.

### Viscosity solution: test by smooth functions that touch

For a nonlinear second-order equation written as

$$
F(t,x,u,\partial_tu,Du,D^2u)=0,
\tag{5}
$$

a viscosity solution need not possess the derivatives appearing in (5). Instead, smooth test functions touching the candidate from above or below supply the derivatives used in the subsolution and supersolution inequalities.

For the heat equation, one may take

$$
F(t,x,r,q,p,X)=q-\operatorname{tr}X-f(t,x).
$$

With the standard degenerate-elliptic convention that $X\leq Y$ implies $F(\cdots,X)\geq F(\cdots,Y)$, every smooth classical solution is a viscosity solution: at a touching point, first derivatives agree and the Hessians have the order required by ellipticity. This is a consistency statement, not a general equivalence theorem.

Comparison and uniqueness are also separate theorems. Crandall--Ishii--Lions, §2, Definition 2.2 gives the basic viscosity definition and consistency discussion; §3, Theorem 3.3 gives a comparison theorem under explicit structural hypotheses. Without such hypotheses, one should not infer uniqueness merely from the word "viscosity."

## What can and cannot be inferred

Some implications are routine once their hypotheses are stated. A sufficiently integrable classical solution satisfies the corresponding distributional identity. Under the degenerate-elliptic convention above, a smooth classical solution of (5) is a viscosity solution. A mild or weak solution may become classical when a regularity theorem applies.

None of these statements gives a universal equivalence diagram. Weak formulations differ by equation and function space; mild formulations depend on a chosen semigroup or evolution family; viscosity comparison depends on structural assumptions. Any claimed equivalence must therefore cite the theorem that supplies the missing regularity, trace, uniqueness, or comparison input.

## Specialist handoffs

For an equation-specific weak formulation, continue to [Weak parabolic solutions on the torus](weak-parabolic-solutions-on-the-torus.md). For semigroup formulas and their branching use, continue to [Mild formulation and branching-diffusion representation](mild-formulation-and-branching-diffusion-representation.md). For the full touching-test definition, sign convention, and comparison discussion, continue to [Viscosity solutions](viscosity-solutions.md).

## Reader check

After this entry, a reader should be able to classify a proposed PDE statement as pointwise, test-function/distributional, semigroup-integral, or touching-test/viscosity; identify which derivatives are not being assumed to exist in each formulation; distinguish a bare distributional identity from an equation-specific weak solution; and reject any claimed equivalence between the four notions unless the needed regularity, trace, or comparison hypotheses are stated.

## Sources

- Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., American Mathematical Society, 2010: §§6.1.2, 6.3.1 Theorem 3, and 7.1.1, pp. 373--375.
- Amnon Pazy, *Semigroups of Linear Operators and Applications to Partial Differential Equations*, Springer, 1983: Chapter 6, §1, Definition 1.1 and Theorem 1.5.
- Michael G. Crandall, Hitoshi Ishii, and Pierre-Louis Lions, *User's guide to viscosity solutions of second order partial differential equations*, *Bulletin of the American Mathematical Society* **27** (1992), 1--67: §2, Definition 2.2 and the consistency discussion; §3, Theorem 3.3.
