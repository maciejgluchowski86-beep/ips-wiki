# Group meeting 032: distinguished-zero transfer stops; additive-Hamming non-diagonal coupling bridge is killed

Date: 2026-08-17

`state_narrowed: yes`.

Professor review of:

- Meeting 031 and Assignment 011 with its pre-registered stop rule;
- Student G handoff `students/student-g/011-handoff.md`, commit `c48c560`;
- main report `011-distinguished-zero-transfer.md`, commit `07b8fce`;
- exact checkpoints `06e1dda`, `0964905`, `645590a`, `79c12a7` and verifier `7d46627`;
- Meetings 013--014 for the zero-boundary invariant family and tail-shift identity;
- Meeting 030 for the still-stopped connected-renewal blocker;
- the toolbox positive-rates shortlist only for deciding the next bounded experiment.

The principal reports independently rerunning the committed G011 verifier with exit 0. I independently recomputed the decisive `N=1 -> 2` stationary algebra and recover the same symbolic factorization below.

## Ruling in one sentence

**Accept G011 as `STOP-EQUIVALENT`.** Naming the zero-boundary invariant marginals `pi_N` does not transfer the East distinguished-zero conditional-equilibrium induction off the product surface. Buffered or finite-layer regenerative repairs reduce exactly to the already-isolated tail-shift defect. Marker-existence Part D is therefore closed as moot for this architecture: marker geometry cannot repair a marginal incompatibility that survives after every released coordinate is marginalized out.

This is a clean negative transfer theorem for the proposed `pi_N`-based East architecture. It is **not** a theorem that no future distinguished-zero-inspired idea can ever help positive rates.

## 1. Exact one-move compatibility obstruction accepted

Let a right-measurable marker move enlarge a screened block from `N` to `N+1` while leaving the old protected `N` coordinates untouched. If, conditional on the marker/right-side sigma-field, the old block has law `pi_N` and the enlarged block is required to have law `pi_{N+1}`, marginalizing the newly released coordinate forces

$$
\boxed{\bar\pi_{N+1}=\pi_N.}
$$

No release kernel on coordinates outside the protected block can alter this necessary marginal identity.

For `N=1 -> 2`, direct solution of the four-state stationary equations gives

$$
\boxed{
\bar\pi_2(1)-\pi_1(1)
=-\frac{2a\,[a-b(1-c)]}
{(a+1-c)\,[2ab-ac+3a-bc+b+c^2-3c+2]}.
}
$$

I independently recomputed this factorization. At

$$
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right)
$$

one has

$$
\pi_1(1)=\frac12,
\qquad
\bar\pi_2(1)=\frac{5251}{30302},
$$

hence

$$
\boxed{\bar\pi_2(1)-\pi_1(1)=-\frac{4950}{15151}\ne0.}
$$

Thus the literal analogue of East Lemma 8.2 using the family `pi_N` is false already at the first nontrivial move.

## 2. Product-surface characterization accepted

The compatibility locus is

$$
\boxed{a=b(1-c).}
$$

Put

$$
\rho=\frac b{1+b}.
$$

Then

$$
(1-\rho)b=\rho
$$

and

$$
(1-\rho)a=\rho(1-c)
$$

is equivalent to `a=b(1-c)`. Therefore on this locus the same Bernoulli marginal is reversible for either value of the right neighbour, and finite irreducibility gives

$$
\boxed{\pi_N=\operatorname{Ber}(\rho)^{\otimes N}\quad\text{for every }N.}
$$

Hence prefix compatibility holds at every depth exactly where the supposedly surrogate nonproduct invariant family collapses back to a product-consistent family.

The right interpretation is therefore:

> **Exact East transfer through zero-boundary invariant marginals succeeds on the product surface and fails off it already at depth two.**

This is sharper than a generic negative statement and answers the principal's specific proposal.

## 3. Buffered screening is exactly tail shift

If the last `m` old sites are declared contaminated and only the untouched prefix is protected, G proves the exact identity

$$
\boxed{S_m=\Delta_{m+1}},
$$

up to the harmless convention of whether the newly released marker site is counted in the buffer.

Thus a growing buffered screen with vanishing invariant-family mismatch is equivalent to

$$
\Delta_M\to0.
$$

Meeting 014 already identifies this with tail-shift agreement of the projective half-line zero-boundary invariant law. Conditioning on an East-style right-measurable marker path cannot improve this instantaneous compatibility gate because it neither inspects nor modifies the protected prefix.

A finite-time local-observable weakening is possible, but Meeting 014 already reduces one such evolved boundary response to `Delta` plus finite propagation. Making it iterative would require a genuinely new dynamical boundary-defect contraction/cancellation theorem; the distinguished-zero bookkeeping itself does not provide one.

## 4. Fixed-width regenerative release cannot bypass the defect

Split the old block into protected prefix `U` and a width-`m` boundary layer `V`. Let an arbitrary fresh right-side Markov kernel replace `V` by a new layer `W`, without inspecting or modifying `U`.

The output `U`-marginal is still the old `pi_N|_U`. Therefore exact output `pi_{N+1}` requires

$$
\pi_N|_U=\pi_{N+1}|_U.
$$

Uniformly in `N`, this forces

$$
\Delta_{m+1}=0.
$$

Approximate output has variation error at least the same untouched-prefix discrepancy, so a growing-width approximate release again needs `Delta_M->0`.

The finite hard-point checks through `pi_4` are consistent with this theorem but are not the load-bearing evidence; the marginalization argument is.

## 5. Marker-existence Part D is closed for this architecture

Assignment 011 correctly did not enter marker creation/persistence/advance.

The ordering of the issues is decisive. Even granting an ideal marker whose entire path is measurable from the right and whose conditioning reveals no protected marks, exact `pi_N` screening fails at the compatibility step. Finite boundary-layer release does not change the protected-prefix marginal, and a growing buffer is exactly the old tail-shift theorem.

Therefore marker existence is **not an independent unresolved edge of this proposed architecture**. Studying it now would optimize a marker for a screen that has already failed before the marker dynamics matter.

This does not close all possible future screening constructions. A future proposal would have to alter the mathematical object, e.g. provide a new dynamical theorem that erases the injected boundary defect without assuming `Delta_M->0`, common-coupling all-depth occupation, or Meeting 030's signed boundary-transmission estimate. Such a theorem would be a new architecture, not Part D of G011.

## 6. Professor observation: the refined non-diagonal uniform-Hamming bridge is analytically impossible

The toolbox synthesis retained a bounded LP test of the proposed bridge

$$
\bar L H\le-\kappa H,
\qquad
H(x,y)=\sum_i\mathbf1_{\{x_i\ne y_i\}},
$$

for a general Markovian coupling allowed to pair a flip at site `i` in one copy with a flip at site `j` in the other.

That LP is unnecessary for the Hamming target. There is a general additive obstruction.

### Proposition 6.1 (cross-site pairings do not improve additive Hamming drift)

Consider two spin-flip generators with marginal flip rates `lambda_i(x)` and `lambda_i(y)`. In an arbitrary Markovian coupling, write `gamma_{ij}` for the rate of a joint jump flipping site `i` in the first copy and site `j` in the second, with one-sided rates represented by `gamma_{i,partial}` and `gamma_{partial,j}`. Marginal constraints are

$$
\sum_j\gamma_{ij}+\gamma_{i,\partial}=\lambda_i(x),
\qquad
\sum_i\gamma_{ij}+\gamma_{\partial,j}=\lambda_j(y).
$$

For `i\ne j`, additivity of Hamming distance gives exactly

$$
H(x^i,y^j)-H(x,y)
=[H(x^i,y)-H(x,y)]+[H(x,y^j)-H(x,y)].
$$

Hence every off-diagonal `gamma_{ij}` contribution collapses under the marginal constraints. Only simultaneous flips at the **same** site can change the Hamming drift relative to the marginals.

At an agreed site, the minimum contribution is obtained by coupling the common part of the two flip rates and equals

$$
|\lambda_i(x)-\lambda_i(y)|.
$$

At a disagreeing site, a single marginal flip coalesces while simultaneous flips preserve the disagreement, so the minimum is obtained by never pairing the two flips and equals

$$
-(\lambda_i(x)+\lambda_i(y)).
$$

Therefore the best possible instantaneous Hamming drift over **all** Markovian couplings is

$$
\boxed{
\inf_{\text{couplings}}\bar L H
=
\sum_{i:x_i=y_i}|\lambda_i(x)-\lambda_i(y)|
-
\sum_{i:x_i\ne y_i}(\lambda_i(x)+\lambda_i(y)).
}
$$

No non-diagonal pairing can improve this value.

### Hard-point obstruction

Take configurations differing only at site `0`, with

$$
x_0=0,\qquad y_0=1,
$$

common right neighbour `0`, and common left spin `1`.

At site `0`, the two flip rates are `a` and `1-c`, so the optimal contribution is

$$
-(a+1-c).
$$

At site `-1`, the spins agree at `1`, but their right neighbours differ, so the flip rates are `1-c` and `1`; the optimal contribution is

$$
c.
$$

All other local contexts agree. Hence

$$
\boxed{
\inf_{\text{all Markovian couplings}}\bar L H
=c-(a+1-c).
}
$$

At `P_h`,

$$
\boxed{c-(a+1-c)=\frac{9997}{10000}>0.}
$$

Thus the toolbox Bridge R requiring a uniform `kappa>0` is false at the hard point for **every Markovian coupling**, not merely for the common-uniform coupling.

This does not kill Gray's nonmonotone edge geometry, whose load-bearing observable is not additive Hamming distance. It does kill the proposed refined-coupling Hamming bridge as stated and removes the need for its rational LP experiment.

## 7. Direction judgment

G011 answered the principal's distinguished-zero question with a precise negative transfer theorem. It materially narrows the state, so `state_narrowed: yes`.

The positive-rates conjecture remains the principal-fixed scientific target. The connected-renewal restart bar remains operative; G011 does not reopen bare tail shift. The common-coupling occupation, Bellman, scalar Foster, and generic norm routes remain stopped.

The toolbox had retained two bounded pre-restart experiments. Proposition 6.1 analytically resolves the uniform-Hamming half of the nonbasic-coupling experiment negatively. Rather than spend G on a redundant LP or an underspecified Gray-interface search, the next highest-value bounded test is the **information-percolation pair-history experiment**, which is genuinely independent of the stopped interfaces.

Student G receives Assignment 012 on that bounded experiment. No full positive-rates proof architecture is reopened by this assignment.

No public wiki edits are authorized.
