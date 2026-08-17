# Proof spine: generalized patch representations

Date: 2026-08-17

## Target

Extend the patch representation / patch positivity mechanism beyond binary flip spin systems while preserving the core architecture:

1. a tensor basis of local observables;
2. an exact signed Feynman--Kac dual;
3. a graphical interaction process with a coarser successful-interaction skeleton;
4. conditional factorization into spacetime patches after hidden marks are averaged;
5. a local nonnegativity criterion on bulk patch contributions;
6. consequences such as order preservation, comparison, or convergence in concrete models.

## E0. Binary benchmark

Established by the canonical paper.

For binary spins, monomials `chi_A` form a cylinder-function basis. The generator sends each monomial to a signed linear combination of monomials. Absolute coefficients become rates of a signed additive set process; a diagonal mismatch becomes a Feynman--Kac potential. Nonempty-target interactions at active sources define the successful skeleton, which records source/time/target but hides whether the source survives (birth versus split). Conditioning on that skeleton decomposes site lines into one-site patches and factorizes the hidden marks.

Any generalization must specialize exactly to this construction, not merely produce some abstract finite-state duality.

## E1. Canonical local basis for a finite state space

Open.

Candidate: for a finite state space `E` with distinguished reference state `0`, use the one-site basis

- `h_0 = 1`;
- `h_a(x)=1{x=a}` for `a in E\{0}`.

A finite typed active configuration is a finite partial map `xi: Lambda -> E\{0}` and

`H_xi(eta)=prod_{i in supp xi} h_{xi(i)}(eta(i))`.

This is a basis for every finite cylinder algebra. Products are idempotent on equal types and vanish on conflicting types. The resulting compatible-union/cemetery algebra is the first object to test.

## E2. Exact signed dual for single-site replacement dynamics

Open and first load-bearing edge.

Consider bounded rates

`c_i^{x->y}(eta_{N(i)})`, `x != y`,

with generator

`L f(eta) = sum_i sum_{x != y} 1{eta_i=x} c_i^{x->y}(eta_N) [f(eta^{i,y})-f(eta)]`.

Question: after expanding each neighbour-rate function in the typed tensor basis, can `L H_xi` be represented by fixed local signed interaction clocks whose rates depend only on `(i, source type, local typed target/branch mark)`, with a Feynman--Kac potential for identity terms?

A merely formal matrix dual on the full finite cylinder space is not enough. The transition structure must be local and graphical enough to support a later skeleton/patch construction.

## E3. Hidden mark / successful interaction analogue

Blocked on E2.

If E2 succeeds, determine whether nonempty typed-target interactions can be superposed into records `(source, time, typed target)` while hiding a finite branch mark controlling source deletion/retyping/survival, exactly as binary records hide birth versus split.

Potential obstruction: incompatible typed targets can send the observable to zero, and source retyping may carry information not reconstructible from the coarse skeleton. This must be resolved before patch geometry is defined.

## E4. Generalized patch factorization

Blocked on E3.

Need a skeleton-measurable decomposition for which hidden marks in distinct patches are conditionally independent. The binary one-site vertical patch geometry may or may not survive unchanged.

## E5. Generalized patch positivity

Blocked on E4.

Need a local criterion ensuring every bulk patch contribution is nonnegative. It should reduce to the paper's multilinear coefficient inequalities in the binary case.

## E6. Applications

Blocked on E5, except for reconnaissance.

Priority examples should genuinely use more than two local states or a non-flip replacement mechanism and should not be contrived encodings of binary spin systems.
